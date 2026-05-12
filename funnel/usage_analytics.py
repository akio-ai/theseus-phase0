"""
Generic event recorder + aggregator. Surfaces stats for the daily briefing.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Optional

from . import _db


def record_event(user_id: str, kind: str, payload: Optional[dict[str, Any]] = None) -> int:
    _db.init()
    with _db.conn() as c:
        cur = c.execute(
            "INSERT INTO events (ts, user_id, kind, payload) VALUES (?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), user_id, kind,
             json.dumps(payload or {})),
        )
        return cur.lastrowid


def usage_summary(days: int = 1) -> dict:
    _db.init()
    with _db.conn() as c:
        rows = c.execute(
            "SELECT kind, COUNT(*) AS n FROM events "
            "WHERE ts >= datetime('now', ?) GROUP BY kind ORDER BY n DESC",
            (f"-{days} days",),
        ).fetchall()
        unique_users = c.execute(
            "SELECT COUNT(DISTINCT user_id) AS n FROM events "
            "WHERE ts >= datetime('now', ?)", (f"-{days} days",),
        ).fetchone()["n"]
    return {
        "window_days": days,
        "unique_users": int(unique_users),
        "events_by_kind": [{"kind": r["kind"], "n": int(r["n"])} for r in rows],
    }
