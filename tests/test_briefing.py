"""
Briefing tests — weakness tracker round-trip + dry-run notify.
"""
from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def isolated_learn_db(tmp_path, monkeypatch):
    p = tmp_path / "learn.db"
    monkeypatch.setenv("THESEUS_LEARN_DB", str(p))
    import importlib
    from briefing import weakness_tracker
    importlib.reload(weakness_tracker)
    yield p


def test_record_and_query_akio_weakness():
    from briefing.weakness_tracker import record_akio_answer, top_weaknesses
    # 3 wrong out of 4 on the same topic
    for _ in range(3):
        record_akio_answer("champagne.dosage", "what is brut nature dosage?", "0-3 g/L", "5", correct=False)
    record_akio_answer("champagne.dosage", "what is brut nature dosage?", "0-3 g/L", "0-3", correct=True)
    w = top_weaknesses()
    topics = {t["topic"] for t in w["akio_weak_topics"]}
    assert "champagne.dosage" in topics


def test_record_entity_flag():
    from briefing.weakness_tracker import record_entity_flag, top_weaknesses
    record_entity_flag("cuvee:fake-x", "wrong_dosage", "Akio: I think this is 6 not 8")
    w = top_weaknesses()
    assert any(f["entity_id"] == "cuvee:fake-x" for f in w["open_entity_flags"])


def test_dry_run_notify_returns_no_webhook(monkeypatch):
    monkeypatch.delenv("DISCORD_WEBHOOK_BRIEFING", raising=False)
    from briefing.discord_notify import NotifyChannel, notify
    r = notify(NotifyChannel.BRIEFING, "test")
    assert r["sent"] is False
    assert r["reason"] == "no_webhook"


def test_placeholder_webhook_treated_as_unset(monkeypatch):
    monkeypatch.setenv("DISCORD_WEBHOOK_BRIEFING", "PLACEHOLDER_THESEUS_BRIEFING")
    from briefing.discord_notify import NotifyChannel, notify
    r = notify(NotifyChannel.BRIEFING, "test")
    assert r["sent"] is False
    assert r["reason"] == "no_webhook"


def test_compose_briefing_renders_without_db(monkeypatch, tmp_path):
    """compose_briefing should produce a string even if main PG is down."""
    monkeypatch.setenv("THESEUS_PG_PORT", "1")  # nonexistent
    monkeypatch.setenv("THESEUS_COST_HARD_DAILY_USD", "20")
    monkeypatch.setenv("THESEUS_COST_MONTHLY_USD", "100")
    monkeypatch.setenv("THESEUS_COST_SOFT_HOURLY_USD", "5")
    monkeypatch.setenv("THESEUS_LAST_RUN", str(tmp_path / "missing.json"))
    monkeypatch.setenv("THESEUS_COST_DB", str(tmp_path / "cost.db"))
    monkeypatch.setenv("THESEUS_LEARN_DB", str(tmp_path / "learn.db"))
    import importlib
    from briefing import daily_briefing, weakness_tracker
    from cost import cost_db, budget_enforcer
    importlib.reload(cost_db)
    importlib.reload(budget_enforcer)
    importlib.reload(weakness_tracker)
    importlib.reload(daily_briefing)
    msg = daily_briefing.compose_briefing()
    assert "Theseus Daily Briefing" in msg
    assert "💰 Cost:" in msg
