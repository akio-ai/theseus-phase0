"""
Invite tracker. Rules (T#1 v3 §10):
  - 1 month free per accepted invite
  - 3+ accepted invites → user is "store lead" (likely managing a team)
"""
from __future__ import annotations

from datetime import datetime, timezone

from . import _db

STORE_LEAD_THRESHOLD = 3


def record_invite(inviter_id: str, invitee_id: str, accepted: bool = False) -> int:
    _db.init()
    with _db.conn() as c:
        cur = c.execute(
            "INSERT INTO invites (ts, inviter_id, invitee_id, accepted) VALUES (?,?,?,?)",
            (datetime.now(timezone.utc).isoformat(), inviter_id, invitee_id, int(accepted)),
        )
        return cur.lastrowid


def mark_accepted(invite_id: int) -> None:
    _db.init()
    with _db.conn() as c:
        c.execute("UPDATE invites SET accepted = 1 WHERE id = ?", (invite_id,))


def invite_count(inviter_id: str, accepted_only: bool = False) -> int:
    _db.init()
    with _db.conn() as c:
        if accepted_only:
            r = c.execute(
                "SELECT COUNT(*) AS n FROM invites WHERE inviter_id=? AND accepted=1",
                (inviter_id,),
            ).fetchone()
        else:
            r = c.execute(
                "SELECT COUNT(*) AS n FROM invites WHERE inviter_id=?", (inviter_id,),
            ).fetchone()
        return int(r["n"])


def is_store_lead(inviter_id: str) -> bool:
    return invite_count(inviter_id, accepted_only=True) >= STORE_LEAD_THRESHOLD
