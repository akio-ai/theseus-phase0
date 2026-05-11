"""
Cost tracker — decorator + helper for LLM calls.

USAGE PATTERN (mandatory — all LLM calls go through here):

    from cost.cost_tracker import wrap

    @wrap(caller="structurer.cuvee")
    def call_claude(...) -> AnthropicResponse:
        return client.messages.create(...)

    response = call_claude(...)   # automatically logs tokens + USD + checks budget

The wrapper:
1. Calls the wrapped function
2. Extracts (input_tok, output_tok, model) from the response
3. Computes USD cost from PRICING table
4. Inserts a row into cost_db
5. Calls budget_enforcer.check_budgets() — which may engage kill switch

Pricing table is kept in this module for transparency. Update when Anthropic changes prices.
"""
from __future__ import annotations

import functools
from typing import Any, Callable, Optional

from . import cost_db


# USD per 1M tokens. Source: anthropic.com pricing, as of T#1 v3 lock (2026-05-09).
# Update when Anthropic publishes new pricing.
PRICING_PER_M_TOK: dict[str, dict[str, float]] = {
    # Phase 0 default: Opus 4.5
    "claude-opus-4-5":      {"input": 15.0, "output": 75.0},
    "claude-opus-4-5-20251201": {"input": 15.0, "output": 75.0},
    # Conservative default for unknown models — falls back to Opus pricing
    "_default":             {"input": 15.0, "output": 75.0},
}


def usd_for(model: str, input_tok: int, output_tok: int) -> float:
    p = PRICING_PER_M_TOK.get(model) or PRICING_PER_M_TOK["_default"]
    return (input_tok * p["input"] + output_tok * p["output"]) / 1_000_000.0


def log_cost(model: str, input_tok: int, output_tok: int, caller: str,
             op_id: Optional[str] = None) -> dict:
    """Direct logging path (for non-decorator call sites)."""
    usd = usd_for(model, input_tok, output_tok)
    cost_db.insert(model, input_tok, output_tok, usd, caller, op_id)
    from .budget_enforcer import check_budgets
    return check_budgets()  # returns {hourly, daily, monthly} with status


def track(response: Any, *, caller: str, op_id: Optional[str] = None) -> dict:
    """
    Log a single Anthropic response. Works with both the SDK's Message object
    (response.usage.input_tokens / response.usage.output_tokens / response.model)
    and a plain dict shape.
    """
    if hasattr(response, "usage"):
        input_tok = int(response.usage.input_tokens)
        output_tok = int(response.usage.output_tokens)
        model = str(getattr(response, "model", "_default"))
    elif isinstance(response, dict):
        usage = response.get("usage", {})
        input_tok = int(usage.get("input_tokens", 0))
        output_tok = int(usage.get("output_tokens", 0))
        model = str(response.get("model", "_default"))
    else:
        raise TypeError(f"track() cannot extract usage from {type(response)}")
    return log_cost(model, input_tok, output_tok, caller, op_id)


def wrap(*, caller: str) -> Callable:
    """
    Decorator. The wrapped function must return an object with `.usage.input_tokens`
    and `.usage.output_tokens` (Anthropic SDK shape) — or a dict with `usage` key.
    """
    def deco(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            op_id = kwargs.pop("_op_id", None)
            response = fn(*args, **kwargs)
            track(response, caller=caller, op_id=op_id)
            return response
        inner.__theseus_cost_wrapped__ = True  # type: ignore[attr-defined]
        inner.__theseus_cost_caller__ = caller  # type: ignore[attr-defined]
        return inner
    return deco
