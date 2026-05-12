"""
Style engine isolation tests — gap-compass enforcement.

Asserts:
- DB path lives under a 'private/' directory segment
- Logging round-trips
- All rows carry commercialization_ban = 1
"""
from __future__ import annotations

import sqlite3

import pytest

from style_engine.interaction_logger import (
    InteractionKind, assert_no_public_leak, count_by_kind, log_interaction,
)


@pytest.fixture(autouse=True)
def isolated_style_db(tmp_path, monkeypatch):
    p = tmp_path / "private" / "interactions.db"
    monkeypatch.setenv("THESEUS_STYLE_DB", str(p))
    import importlib
    from style_engine import interaction_logger
    importlib.reload(interaction_logger)
    yield p


def test_db_under_private_dir():
    assert_no_public_leak()  # raises AssertionError if not


def test_log_round_trip():
    log_interaction(
        InteractionKind.PAIRING_CHOICE,
        entity_id="cuvee:x",
        context={"food": "scallop tartare"},
        response={"chose": "krug grande cuvee"},
    )
    assert count_by_kind(InteractionKind.PAIRING_CHOICE) == 1


def test_commercialization_ban_always_one(isolated_style_db):
    log_interaction(InteractionKind.FREE_NOTE, response={"text": "x"})
    with sqlite3.connect(str(isolated_style_db)) as c:
        rows = c.execute("SELECT commercialization_ban FROM interactions").fetchall()
    assert rows
    for (b,) in rows:
        assert b == 1, "commercialization_ban must be 1 on every row"


def test_no_kind_count_isolated():
    log_interaction(InteractionKind.ENTITY_FLAG, entity_id="cuvee:y")
    log_interaction(InteractionKind.ENTITY_EDIT, entity_id="cuvee:y")
    assert count_by_kind(InteractionKind.ENTITY_FLAG) == 1
    assert count_by_kind(InteractionKind.ENTITY_EDIT) == 1
    assert count_by_kind() == 2
