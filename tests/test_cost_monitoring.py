"""
Cost monitoring tests — gap #3.

Verifies:
- Pricing math correctness
- Cost DB insert + window queries
- Soft hourly warn does NOT kill
- Hard daily cap engages kill switch with correct reason
- Monthly cap engages kill switch
- LLM client refuses calls when killed / over budget
- All LLM-calling modules go through cost.cost_tracker.wrap (no bare anthropic import)
"""
from __future__ import annotations

import os
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_cost_db(tmp_path, monkeypatch):
    """Redirect cost.db to tmp for every test."""
    p = tmp_path / "cost.db"
    monkeypatch.setenv("THESEUS_COST_DB", str(p))
    # Re-import so module-level cached paths refresh
    import importlib
    from cost import cost_db, cost_tracker, budget_enforcer
    importlib.reload(cost_db)
    importlib.reload(cost_tracker)
    importlib.reload(budget_enforcer)
    yield p


def test_pricing_math():
    from cost.cost_tracker import usd_for
    # 1M input tokens @ $15 = $15
    assert abs(usd_for("claude-opus-4-5", 1_000_000, 0) - 15.0) < 1e-6
    # 1M output tokens @ $75 = $75
    assert abs(usd_for("claude-opus-4-5", 0, 1_000_000) - 75.0) < 1e-6
    # Mixed
    assert abs(usd_for("claude-opus-4-5", 100_000, 50_000) - (1.5 + 3.75)) < 1e-6


def test_log_then_query_window(isolated_cost_db, monkeypatch):
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_SOFT_HOURLY_USD", "1000")
    from cost.cost_tracker import log_cost
    from cost.cost_db import query_window
    log_cost("claude-opus-4-5", 100_000, 50_000, caller="test")
    day = query_window("day")
    assert day["calls"] == 1
    assert day["usd"] > 0


def test_soft_hourly_does_not_kill(isolated_cost_db, monkeypatch):
    monkeypatch.setenv("THESEUS_COST_SOFT_HOURLY_USD", "0.001")
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "1000")
    from cost.cost_tracker import log_cost
    from control.kill_switch import is_killed
    assert not is_killed()
    # Logs $1.50 input + $3.75 output = $5.25 → way over soft $0.001
    log_cost("claude-opus-4-5", 100_000, 50_000, caller="test")
    assert is_killed() is False, "soft cap should not engage kill switch"


def test_hard_daily_engages_kill_switch(isolated_cost_db, monkeypatch):
    monkeypatch.setenv("THESEUS_COST_SOFT_HOURLY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "0.001")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "1000")
    from cost.cost_tracker import log_cost
    from control.kill_switch import is_killed, last_engagement
    assert not is_killed()
    log_cost("claude-opus-4-5", 100_000, 50_000, caller="test")
    assert is_killed() is True
    rec = last_engagement()
    assert rec["reason"] == "cost_hard_cap"


def test_monthly_cap_engages_kill_switch(isolated_cost_db, monkeypatch):
    monkeypatch.setenv("THESEUS_COST_SOFT_HOURLY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "0.001")
    from cost.cost_tracker import log_cost
    from control.kill_switch import is_killed, last_engagement
    log_cost("claude-opus-4-5", 100_000, 50_000, caller="test")
    assert is_killed() is True
    rec = last_engagement()
    assert rec["reason"] == "cost_monthly_cap"


def test_guard_raises_when_over_daily(isolated_cost_db, monkeypatch):
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "0.001")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_SOFT_HOURLY_USD", "1000")
    from cost.cost_tracker import log_cost
    from cost.budget_enforcer import BudgetExceeded, guard
    log_cost("claude-opus-4-5", 100_000, 50_000, caller="test")
    with pytest.raises(BudgetExceeded):
        guard()


def test_wrap_decorator_extracts_usage(isolated_cost_db, monkeypatch):
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_SOFT_HOURLY_USD", "1000")
    from cost.cost_tracker import wrap
    from cost.cost_db import query_window

    class FakeUsage:
        input_tokens = 1000
        output_tokens = 500

    class FakeResponse:
        usage = FakeUsage()
        model = "claude-opus-4-5"

    @wrap(caller="test.wrap")
    def fake_call():
        return FakeResponse()

    fake_call()
    day = query_window("day")
    assert day["calls"] == 1
    assert day["input_tok"] == 1000
    assert day["output_tok"] == 500


def test_llm_client_refuses_when_killed(isolated_cost_db, monkeypatch):
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "1000")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "1000")
    from control.kill_switch import KillReason, engage_kill
    engage_kill(KillReason.MANUAL, actor="test")
    from llm.claude_client import LLMUnavailable, call_claude
    with pytest.raises(LLMUnavailable, match="kill switch"):
        call_claude(system="x", user="y")


def test_llm_module_uses_cost_wrapper():
    """Static check: llm.claude_client._call_messages must be cost-wrapped."""
    from llm.claude_client import _call_messages
    assert getattr(_call_messages, "__theseus_cost_wrapped__", False), \
        "_call_messages must be decorated with cost.cost_tracker.wrap"
    assert getattr(_call_messages, "__theseus_cost_caller__", "") == "llm.call_claude"
