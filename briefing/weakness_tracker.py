"""
Bidirectional weakness tracker — Co-learning loop core (T#1 v3 §9).

Records:
  A. Akio's quiz answers (right/wrong) — for next day's review focus
  B. Entity flags from Akio's review ("this entry seems wrong") — for crawler/structurer to re-verify

Local SQLite (separate from main PG): survives PG outages, fast, no schema overhead.
"""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator


def _db_path() -> Path:
    return Path(os.environ.get(
        "THESEUS_LEARN_DB",
        str(Path.home() / "Theseus_Phase0" / "briefing" / "learn.db"),
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
        # A. Akio answers
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS akio_answers (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                ts          TEXT    NOT NULL,
                topic       TEXT    NOT NULL,       -- e.g. 'champagne.dosage_categories'
                question    TEXT    NOT NULL,
                expected    TEXT,
                given       TEXT,
                correct     INTEGER NOT NULL        -- 0/1
            )
            """
        )
        c.execute("CREATE INDEX IF NOT EXISTS idx_akio_answers_topic ON akio_answers(topic, ts)")
        # B. Entity flags (Akio reports a suspect entry)
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS entity_flags (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                ts          TEXT    NOT NULL,
                entity_id   TEXT    NOT NULL,
                reason      TEXT    NOT NULL,       -- 'wrong_dosage' / 'wrong_cepage' / 'missing_vintage' / 'free_text'
                note        TEXT,
                resolved_at TEXT
            )
            """
        )
        c.execute("CREATE INDEX IF NOT EXISTS idx_entity_flags_open ON entity_flags(entity_id) WHERE resolved_at IS NULL")


def record_akio_answer(topic: str, question: str, expected: str, given: str, correct: bool) -> None:
    _init()
    with _conn() as c:
        c.execute(
            "INSERT INTO akio_answers (ts, topic, question, expected, given, correct) "
            "VALUES (?,?,?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), topic, question, expected, given, int(correct)),
        )


def record_entity_flag(entity_id: str, reason: str, note: str = "") -> None:
    _init()
    with _conn() as c:
        c.execute(
            "INSERT INTO entity_flags (ts, entity_id, reason, note) VALUES (?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), entity_id, reason, note),
        )


def top_weaknesses(limit: int = 5) -> dict:
    """
    Returns the bidirectional snapshot for briefing:
      {
        "akio_weak_topics": [{"topic": ..., "wrong_n": ..., "total": ..., "wrong_rate": ...}, ...],
        "open_entity_flags": [{"entity_id": ..., "reason": ..., "ts": ...}, ...]
      }
    """
    _init()
    with _conn() as c:
        akio_weak = c.execute(
            """
            SELECT topic,
                   SUM(1 - correct) AS wrong_n,
                   COUNT(*) AS total,
                   ROUND(AVG(1 - correct), 3) AS wrong_rate
              FROM akio_answers
             WHERE ts >= datetime('now', '-30 days')
             GROUP BY topic
             HAVING total >= 3 AND wrong_rate >= 0.34
             ORDER BY wrong_rate DESC, wrong_n DESC
             LIMIT ?
            """,
            (limit,),
        ).fetchall()
        flags = c.execute(
            """
            SELECT entity_id, reason, note, ts
              FROM entity_flags
             WHERE resolved_at IS NULL
             ORDER BY ts DESC
             LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return {
        "akio_weak_topics": [dict(r) for r in akio_weak],
        "open_entity_flags": [dict(r) for r in flags],
    }
