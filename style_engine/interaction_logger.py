"""
Interaction logger — captures Akio's choices/edits/responses as INPUT signal
for future style learning. All writes go to a private SQLite DB, NEVER to the
public PG instance.

Phase 0 captures only — no model training yet (Phase 2 builds on top).

Hard constraints:
- File path locked under ~/Theseus_Phase0/style_engine/private/  (gitignored)
- Records never propagate to Anki staff deck, tenant briefing, or any
  customer-facing output (enforced by tests/test_style_engine_isolation)
- Records have a `commercialization_ban` flag set TRUE permanently
"""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Any, Iterator, Optional


class InteractionKind(StrEnum):
    ENTITY_FLAG = "entity_flag"           # Akio flagged an entry as suspect
    ENTITY_EDIT = "entity_edit"           # Akio corrected a field
    PAIRING_CHOICE = "pairing_choice"     # Akio chose a pairing among candidates
    ANKI_ANSWER = "anki_answer"           # Akio's quiz response
    BRIEFING_REACT = "briefing_react"     # Akio's reaction to the briefing
    FREE_NOTE = "free_note"               # Free-form note Akio added


def _db_path() -> Path:
    """Default path is under private/ which is in .gitignore."""
    return Path(os.environ.get(
        "THESEUS_STYLE_DB",
        str(Path.home() / "Theseus_Phase0" / "style_engine" / "private" / "interactions.db"),
    ))


@contextmanager
def _conn() -> Iterator[sqlite3.Connection]:
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(str(path), isolation_level=None)
    c.row_factory = sqlite3.Row
    try:
        yield c
    finally:
        c.close()


def _init() -> None:
    with _conn() as c:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS interactions (
                id                     INTEGER PRIMARY KEY AUTOINCREMENT,
                ts                     TEXT    NOT NULL,
                kind                   TEXT    NOT NULL,
                entity_id              TEXT,
                context                TEXT,                     -- JSON
                response               TEXT,                     -- JSON
                commercialization_ban  INTEGER NOT NULL DEFAULT 1  -- always 1
            )
            """
        )
        c.execute("CREATE INDEX IF NOT EXISTS idx_interactions_kind ON interactions(kind, ts)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_interactions_entity ON interactions(entity_id, ts)")


def log_interaction(
    kind: InteractionKind,
    *,
    entity_id: Optional[str] = None,
    context: Optional[dict[str, Any]] = None,
    response: Optional[dict[str, Any]] = None,
) -> int:
    """
    Returns the new row id. Writes to PRIVATE DB only.
    """
    import json
    _init()
    with _conn() as c:
        cur = c.execute(
            "INSERT INTO interactions (ts, kind, entity_id, context, response) VALUES (?,?,?,?,?)",
            (
                datetime.now(timezone.utc).isoformat(),
                kind.value,
                entity_id,
                json.dumps(context or {}),
                json.dumps(response or {}),
            ),
        )
        return cur.lastrowid


def count_by_kind(kind: Optional[InteractionKind] = None) -> int:
    _init()
    with _conn() as c:
        if kind is None:
            r = c.execute("SELECT COUNT(*) AS n FROM interactions").fetchone()
        else:
            r = c.execute("SELECT COUNT(*) AS n FROM interactions WHERE kind = ?",
                          (kind.value,)).fetchone()
        return int(r["n"])


def assert_no_public_leak() -> None:
    """
    Guard for tests: confirms style DB path is under 'private/' AND under Theseus root.
    Raises AssertionError otherwise. Called by test_style_engine_isolation.
    """
    p = _db_path().resolve()
    assert "private" in p.parts, f"style DB must live under private/ : {p}"
    assert "Theseus" in str(p) or os.environ.get("THESEUS_STYLE_DB"), \
        f"style DB must be under Theseus_Phase0 (or explicit env override): {p}"
