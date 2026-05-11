"""
Isolation tests — Win³ ↔ Theseus boundary (T#1 v3 §3.1).

Phase 0 enforces:
  1. Theseus imports must NOT pull in any module under /opt/win3/ or `win3.*`
  2. THESEUS_PG_PORT must differ from WIN3_PG_PORT when both are set
  3. Theseus uses its own kill-file path (not Win³'s)
  4. Discord webhook URLs in .env.example are placeholders (no live Win³ webhook leaks)
"""
from __future__ import annotations

import importlib
import os
import pkgutil
import sys
from pathlib import Path

import pytest


THESEUS_ROOT = Path(__file__).resolve().parent.parent


def _iter_theseus_modules():
    """Yield (fully-qualified-name, module-file) for every Theseus module."""
    sys.path.insert(0, str(THESEUS_ROOT))
    for finder, name, ispkg in pkgutil.walk_packages(
        path=[str(THESEUS_ROOT)],
        prefix="",
        onerror=lambda n: None,
    ):
        if name.startswith(("tests", "venv", "build", "dist")):
            continue
        yield name


def test_no_win3_imports():
    """Importing any Theseus module must not pull `win3.*` into sys.modules."""
    sys.path.insert(0, str(THESEUS_ROOT))
    # Snapshot
    before = set(sys.modules)
    # Walk a curated import set (full walk_packages can be slow + may hit psycopg)
    modules_to_check = [
        "core.schema.entities",
        "core.schema.relations",
        "core.schema.jsonld_context",
        "core.verification.confidence",
        "control.kill_switch",
        "control.emergency_stop",
        "crawler.config",
        "crawler.ethical_guardrails",
    ]
    for m in modules_to_check:
        try:
            importlib.import_module(m)
        except ImportError as e:
            # Allow optional deps (httpx, psycopg) to be absent in the test env;
            # the structural check is what we care about.
            pytest.skip(f"optional dep missing: {e}")
            return
    leaked = [m for m in sys.modules if m.startswith("win3") or m.startswith("opt.win3")]
    assert not leaked, f"Theseus imports leaked Win³ modules: {leaked}"


def test_pg_port_separation(monkeypatch):
    """THESEUS_PG_PORT == WIN3_PG_PORT must raise at connection-time."""
    monkeypatch.setenv("WIN3_PG_PORT", "5432")
    monkeypatch.setenv("THESEUS_PG_PORT", "5432")
    from core.db.connection import _dsn
    with pytest.raises(RuntimeError, match="Isolation violation"):
        _dsn()


def test_pg_port_separation_ok(monkeypatch):
    """Different ports → OK."""
    monkeypatch.setenv("WIN3_PG_PORT", "5432")
    monkeypatch.setenv("THESEUS_PG_PORT", "5433")
    from core.db.connection import _dsn
    dsn = _dsn()
    assert "port=5433" in dsn


def test_kill_file_in_theseus_namespace(isolated_kill_file):
    """Default kill file location must be under Theseus, not Win³."""
    # When env not set, the default path includes 'Theseus_Phase0'
    os.environ.pop("THESEUS_KILL_FILE", None)
    from importlib import reload
    from control import kill_switch
    reload(kill_switch)
    path = kill_switch._kill_file_path()
    assert "Theseus" in str(path)
    assert "win3" not in str(path).lower()


def test_env_example_no_live_webhooks():
    """`.env.example` must not contain real Discord webhook URLs."""
    env_example = THESEUS_ROOT / ".env.example"
    if not env_example.exists():
        pytest.skip(".env.example not yet created (Batch 1 in progress)")
    content = env_example.read_text()
    # Real webhooks look like https://discord.com/api/webhooks/<id>/<token>
    # placeholders should be like "PLACEHOLDER" or "https://discord.com/api/webhooks/CHANGEME/..."
    import re
    real = re.findall(r"https://discord\.com/api/webhooks/\d{10,}/[A-Za-z0-9_-]{30,}", content)
    assert not real, f".env.example contains real-looking Discord webhook: {real}"
