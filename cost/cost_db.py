"""
SQLite cost ledger. Local to ~/Theseus_Phase0/cost/cost.db.

Why SQLite (not main PG): cost tracking must survive PG outages — if PG is down,
we still need to enforce hourly/daily caps. Tiny single-file DB is the right fit.

Schema: (timestamp, model, input_tok, output_tok, usd, caller, op_id)
"""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterator, Optional


def _db_path() -> Path:
    return Path(os.environ.get(
        "THESEUS_COST_DB",
        str(Path.home() / "Theseus_Phase0" / "cost" / "cost.db"),
    ))


@contextmanager
def _conn() -> Iterator[sqlite3.Connection]:
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(str(path), isolation_level=None)  # autocommit
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=NORMAL")
    try:
        yield c
    finally:
        c.close()


def init_db() -> None:
    with _conn() as c:
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS llm_calls (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                ts          TEXT    NOT NULL,        -- ISO8601 UTC
                model       TEXT    NOT NULL,
                input_tok   INTEGER NOT NULL,
                output_tok  INTEGER NOT NULL,
                usd         REAL    NOT NULL,
                caller      TEXT    NOT NULL,        -- e.g. 'structurer.cuvee', 'briefing.daily'
                op_id       TEXT                     -- nullable, for correlating multi-call ops
            )
            """
        )
        c.execute("CREATE INDEX IF NOT EXISTS idx_llm_calls_ts ON llm_calls(ts)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_llm_calls_caller ON llm_calls(caller, ts)")


def insert(model: str, input_tok: int, output_tok: int, usd: float,
           caller: str, op_id: Optional[str] = None) -> int:
    init_db()
    with _conn() as c:
        cur = c.execute(
            "INSERT INTO llm_calls (ts, model, input_tok, output_tok, usd, caller, op_id) "
            "VALUES (?,?,?,?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), model, input_tok, output_tok, usd,
             caller, op_id),
        )
        return cur.lastrowid


def query_window(window: str) -> dict:
    """
    Sum cost over a time window.
    window: 'hour' | 'day' | 'month'
    Returns: {'usd': float, 'calls': int, 'input_tok': int, 'output_tok': int, 'since': iso}
    """
    init_db()
    now = datetime.now(timezone.utc)
    if window == "hour":
        since = now - timedelta(hours=1)
    elif window == "day":
        since = now - timedelta(days=1)
    elif window == "month":
        # Calendar month: from month start
        since = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        raise ValueError(f"unknown window: {window}")
    with _conn() as c:
        row = c.execute(
            """
            SELECT COALESCE(SUM(usd), 0.0) AS usd,
                   COALESCE(SUM(input_tok), 0) AS input_tok,
                   COALESCE(SUM(output_tok), 0) AS output_tok,
                   COUNT(*) AS calls
              FROM llm_calls
             WHERE ts >= ?
            """,
            (since.isoformat(),),
        ).fetchone()
    return {
        "usd": float(row["usd"]),
        "calls": int(row["calls"]),
        "input_tok": int(row["input_tok"]),
        "output_tok": int(row["output_tok"]),
        "since": since.isoformat(),
    }


def throughput_today() -> dict:
    """For Daily Briefing 'entries per dollar' metric (Akio: 機械学習のスピードみたい)."""
    cost = query_window("day")
    # Entries added today is computed elsewhere (from main PG); this returns cost half.
    return cost
