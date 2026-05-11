"""
Anthropic client wrapper. Every Claude call goes through `call_claude`, which is
decorated with `cost.cost_tracker.wrap` — so cost logging is mandatory.

Direct `anthropic.Anthropic().messages.create()` calls from elsewhere in the
codebase are forbidden (tests/test_cost_monitoring.py enforces — it checks that
all LLM-using modules import this module, not anthropic directly).

Kill switch: every call checks is_killed() first.
Budget guard: every call checks budget pre-flight.
"""
from __future__ import annotations

import logging
import os
from typing import Optional

from control.kill_switch import is_killed
from cost.budget_enforcer import guard as budget_guard
from cost.cost_tracker import wrap

logger = logging.getLogger("theseus.llm")


class LLMUnavailable(RuntimeError):
    pass


def _get_client():
    try:
        import anthropic
    except ImportError as e:
        raise LLMUnavailable("anthropic SDK not installed") from e
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key or api_key == "CHANGEME":
        raise LLMUnavailable("ANTHROPIC_API_KEY not set")
    return anthropic.Anthropic(api_key=api_key)


def default_model() -> str:
    return os.environ.get("THESEUS_LLM_MODEL", "claude-opus-4-5")


@wrap(caller="llm.call_claude")
def _call_messages(*, model: str, system: str, user: str,
                   max_tokens: int = 2048,
                   temperature: float = 0.0):
    """Inner — actually hits Anthropic. Wrapped by cost tracker."""
    client = _get_client()
    return client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=system,
        messages=[{"role": "user", "content": user}],
    )


def call_claude(*, system: str, user: str,
                model: Optional[str] = None,
                max_tokens: int = 2048,
                temperature: float = 0.0,
                op_id: Optional[str] = None):
    """
    Public entry. Enforces:
      1. Kill switch not engaged
      2. Budget guard not breached (raises BudgetExceeded if so)
      3. Cost logged via wrap()
    """
    if is_killed():
        raise LLMUnavailable("kill switch engaged — refusing LLM call")
    budget_guard()  # raises BudgetExceeded if over
    chosen_model = model or default_model()
    return _call_messages(
        model=chosen_model, system=system, user=user,
        max_tokens=max_tokens, temperature=temperature,
        _op_id=op_id,  # consumed by wrap() decorator
    )
