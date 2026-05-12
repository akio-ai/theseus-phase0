"""
B2B pipeline — flag individual users for sales outreach.

When `score_lead(user_id).above_threshold` OR `is_store_lead(user_id)`:
  - Record b2b_flag row
  - Send a #b2b-leads Discord notification (once, dedup by user_id + 30d window)
"""
from __future__ import annotations

from datetime import datetime, timezone

from . import _db


def _already_notified_recently(user_id: str, days: int = 30) -> bool:
    _db.init()
    with _db.conn() as c:
        r = c.execute(
            "SELECT COUNT(*) AS n FROM b2b_flags "
            "WHERE user_id=? AND notified_at IS NOT NULL "
            "AND notified_at >= datetime('now', ?)",
            (user_id, f"-{days} days"),
        ).fetchone()
        return r["n"] > 0


def flag_for_b2b(user_id: str, signal_score: float, rationale: str,
                 *, send_notification: bool = True) -> dict:
    """
    Record and (optionally) notify. Returns {"flag_id": int, "notified": bool}.
    Idempotent within a 30-day window.
    """
    _db.init()
    now_iso = datetime.now(timezone.utc).isoformat()
    with _db.conn() as c:
        cur = c.execute(
            "INSERT INTO b2b_flags (ts, user_id, signal_score, rationale) VALUES (?,?,?,?)",
            (now_iso, user_id, signal_score, rationale),
        )
        flag_id = cur.lastrowid

    notified = False
    if send_notification and not _already_notified_recently(user_id):
        from briefing.discord_notify import NotifyChannel, notify
        msg = (
            f"**B2B lead candidate** — user `{user_id}`\n"
            f"signal_score={signal_score:.2f}\n"
            f"rationale: {rationale}"
        )
        r = notify(NotifyChannel.B2B_LEADS, msg)
        if r.get("sent"):
            with _db.conn() as c:
                c.execute("UPDATE b2b_flags SET notified_at = ? WHERE id = ?",
                          (datetime.now(timezone.utc).isoformat(), flag_id))
            notified = True

    return {"flag_id": flag_id, "notified": notified}


def b2b_pipeline_status() -> dict:
    """Summary for the daily briefing."""
    _db.init()
    with _db.conn() as c:
        total = c.execute("SELECT COUNT(*) AS n FROM b2b_flags").fetchone()["n"]
        last_30d = c.execute(
            "SELECT COUNT(*) AS n FROM b2b_flags WHERE ts >= datetime('now', '-30 days')"
        ).fetchone()["n"]
        recent = c.execute(
            "SELECT user_id, signal_score, rationale, ts FROM b2b_flags "
            "ORDER BY ts DESC LIMIT 5"
        ).fetchall()
    return {
        "total_flags": int(total),
        "last_30d_flags": int(last_30d),
        "recent": [dict(r) for r in recent],
    }
