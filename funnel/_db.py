"""Shared SQLite for funnel state. Separate from cost/learn DBs."""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


def db_path() -> Path:
    return Path(os.environ.get(
        "THESEUS_FUNNEL_DB",
        str(Path.home() / "Theseus_Phase0" / "funnel" / "funnel.db"),
    ))


@contextmanager
def conn() -> Iterator[sqlite3.Connection]:
    p = db_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(str(p), isolation_level=None)
    c.row_factory = sqlite3.Row
    try:
        yield c
    finally:
        c.close()


def init() -> None:
    with conn() as c:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                ts      TEXT NOT NULL,
                user_id TEXT NOT NULL,
                kind    TEXT NOT NULL,     -- 'query', 'anki_card_done', 'pairing_request', 'briefing_view', etc.
                payload TEXT
            )
            """
        )
        c.execute("CREATE INDEX IF NOT EXISTS idx_events_user ON events(user_id, ts)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_events_kind ON events(kind, ts)")

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS invites (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                ts          TEXT NOT NULL,
                inviter_id  TEXT NOT NULL,
                invitee_id  TEXT NOT NULL,
                accepted    INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        c.execute("CREATE INDEX IF NOT EXISTS idx_invites_inviter ON invites(inviter_id)")

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS b2b_flags (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                ts           TEXT NOT NULL,
                user_id      TEXT NOT NULL,
                signal_score REAL NOT NULL,
                rationale    TEXT,
                notified_at  TEXT
            )
            """
        )
