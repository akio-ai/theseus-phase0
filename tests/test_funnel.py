"""
Funnel tests.
"""
from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def isolated_funnel_db(tmp_path, monkeypatch):
    p = tmp_path / "funnel.db"
    monkeypatch.setenv("THESEUS_FUNNEL_DB", str(p))
    import importlib
    from funnel import _db, invite_tracker, lead_signals, b2b_pipeline, usage_analytics
    for m in (_db, invite_tracker, lead_signals, b2b_pipeline, usage_analytics):
        importlib.reload(m)
    yield p


def test_invite_count_and_store_lead():
    from funnel.invite_tracker import (
        invite_count, is_store_lead, mark_accepted, record_invite,
    )
    id1 = record_invite("alice", "bob",   accepted=False)
    id2 = record_invite("alice", "carol", accepted=True)
    _   = record_invite("alice", "dave",  accepted=True)
    _   = record_invite("alice", "eve",   accepted=True)
    assert invite_count("alice") == 4
    assert invite_count("alice", accepted_only=True) == 3
    assert is_store_lead("alice") is True

    # Accept bob too — still 4 total, 4 accepted
    mark_accepted(id1)
    assert invite_count("alice", accepted_only=True) == 4


def test_score_lead_below_threshold():
    from funnel.lead_signals import LEAD_THRESHOLD, score_lead
    s = score_lead("nobody")
    assert s["score"] < LEAD_THRESHOLD
    assert s["above_threshold"] is False


def test_score_lead_aggregates_signals():
    from funnel.invite_tracker import record_invite
    from funnel.lead_signals import score_lead
    from funnel.usage_analytics import record_event

    for _ in range(50):
        record_event("u1", "query")
    for _ in range(20):
        record_event("u1", "pairing_request")
    for _ in range(100):
        record_event("u1", "anki_card_done")
    for _ in range(14):
        record_event("u1", "briefing_view")
    record_invite("u1", "buddy", accepted=True)

    s = score_lead("u1")
    assert s["above_threshold"] is True
    assert s["score"] >= 0.6
    assert "query_volume_30d" in s["breakdown"]
    assert "invite_acceptances" in s["breakdown"]


def test_b2b_flag_no_double_notify_within_30d(monkeypatch):
    monkeypatch.delenv("DISCORD_WEBHOOK_B2B_LEADS", raising=False)  # ensure dry run
    from funnel.b2b_pipeline import b2b_pipeline_status, flag_for_b2b
    r1 = flag_for_b2b("u9", 0.9, "looks like a sommelier")
    r2 = flag_for_b2b("u9", 0.92, "still looks like one")
    assert r1["flag_id"] != r2["flag_id"]
    # No real notify happens; both notified=False due to no webhook
    assert r1["notified"] is False
    assert r2["notified"] is False
    s = b2b_pipeline_status()
    assert s["total_flags"] == 2


def test_usage_summary_groups_by_kind():
    from funnel.usage_analytics import record_event, usage_summary
    record_event("u1", "query")
    record_event("u1", "query")
    record_event("u2", "pairing_request")
    s = usage_summary(days=1)
    assert s["unique_users"] == 2
    kinds = {e["kind"]: e["n"] for e in s["events_by_kind"]}
    assert kinds.get("query") == 2
    assert kinds.get("pairing_request") == 1
