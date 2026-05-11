"""
Kill switch behaviour tests — gap #1.
"""
from __future__ import annotations

import json

import pytest

from control.kill_switch import (
    KillReason, engage_kill, clear_kill, is_killed, last_engagement,
)


def test_not_killed_by_default():
    assert is_killed() is False


def test_engage_creates_file_and_sets_state(isolated_kill_file):
    path = engage_kill(KillReason.MANUAL, actor="pytest", note="unit-test")
    assert is_killed() is True
    assert path.exists()
    rec = last_engagement()
    assert rec["reason"] == "manual"
    assert rec["actor"] == "pytest"
    assert rec["note"] == "unit-test"


def test_engage_is_append_only(isolated_kill_file):
    engage_kill(KillReason.MANUAL, actor="a", note="first")
    engage_kill(KillReason.COST_HARD_CAP, actor="b", note="second")
    lines = isolated_kill_file.read_text().strip().split("\n")
    assert len(lines) == 2
    second = json.loads(lines[1])
    assert second["reason"] == "cost_hard_cap"


def test_clear_archives_not_deletes(isolated_kill_file):
    engage_kill(KillReason.MANUAL, actor="pytest")
    assert is_killed()
    archived = clear_kill()
    assert archived is not None
    assert archived.exists()
    assert is_killed() is False


def test_clear_noop_when_not_engaged():
    assert clear_kill() is None


def test_fetcher_refuses_when_killed(monkeypatch, isolated_kill_file):
    """fetcher.fetch() must raise KillSwitchTripped when killed."""
    engage_kill(KillReason.MANUAL, actor="pytest")
    try:
        from crawler.fetcher import KillSwitchTripped, fetch
    except ImportError:
        pytest.skip("httpx not installed in test env")
        return
    with pytest.raises(KillSwitchTripped):
        fetch("https://champagne.fr/")


@pytest.mark.parametrize("reason", list(KillReason))
def test_all_kill_reasons_serializable(isolated_kill_file, reason):
    """Every KillReason value must round-trip through engage/last_engagement."""
    engage_kill(reason, actor="pytest")
    rec = last_engagement()
    assert rec["reason"] == reason.value
