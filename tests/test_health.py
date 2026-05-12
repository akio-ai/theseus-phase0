"""
Health check smoke tests.

The full health check has hard external dependencies (PG, disk, real backups).
We test the individual sub-checks in isolation + the aggregator's CRITICAL logic.
"""
from __future__ import annotations

from ops import health_check


def test_kill_switch_check_says_running(isolated_kill_file):
    r = health_check._check_kill_switch()
    assert r["status"] == "running"
    assert r["level"] == "OK"


def test_kill_switch_check_picks_up_engagement(isolated_kill_file):
    from control.kill_switch import KillReason, engage_kill
    engage_kill(KillReason.MANUAL, actor="pytest", note="health test")
    r = health_check._check_kill_switch()
    assert r["status"] == "killed"
    assert r["reason"] == "manual"


def test_backups_check_no_dir(monkeypatch, tmp_path):
    monkeypatch.setattr(health_check, "BACKUP_DIR", tmp_path / "nonexistent")
    r = health_check._check_backups()
    assert r["status"] == "no_backup_dir"
    assert r["level"] == "CRITICAL"


def test_backups_check_no_dumps(monkeypatch, tmp_path):
    monkeypatch.setattr(health_check, "BACKUP_DIR", tmp_path)
    r = health_check._check_backups()
    assert r["status"] == "no_dumps"
    assert r["level"] == "CRITICAL"


def test_backups_check_fresh(monkeypatch, tmp_path):
    (tmp_path / "theseus-20260509T120000Z.dump").write_bytes(b"x")
    monkeypatch.setattr(health_check, "BACKUP_DIR", tmp_path)
    r = health_check._check_backups()
    assert r["level"] == "OK"
    assert r["count"] == 1


def test_disk_check_returns_pct():
    r = health_check._check_disk()
    assert "used_pct" in r
    assert 0 <= r["used_pct"] <= 100


def test_is_critical_detects(monkeypatch):
    report = {
        "kill_switch": {"level": "OK"},
        "db":          {"level": "CRITICAL"},
        "backups":     {"level": "OK"},
    }
    crit, dims = health_check.is_critical(report)
    assert crit is True
    assert "db" in dims


def test_is_critical_clean():
    report = {
        "kill_switch": {"level": "OK"},
        "db":          {"level": "OK"},
        "backups":     {"level": "OK"},
        "disk":        {"level": "WARN"},
    }
    crit, dims = health_check.is_critical(report)
    assert crit is False
    assert dims == []
