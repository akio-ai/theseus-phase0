"""
Lead signals — heuristic scoring for "this user behaves like a head sommelier".

Phase 0 signals (weights are empirical guesses; refined when real data flows in):
  - query_volume_30d   (>= 50 queries → +0.3)
  - pairing_requests   (>= 20 in 30d  → +0.3)
  - anki_completion    (>= 80% on staff deck within 30d → +0.2)
  - briefing_engagement (>= 14 daily briefings opened → +0.2)
  - invite_acceptances (>= 1 → +0.2 — they care enough to recommend)

Returns a score in [0, 1]. Above LEAD_THRESHOLD (0.6) → eligible for B2B flag.
"""
from __future__ import annotations

from . import _db

LEAD_THRESHOLD = 0.6


def _count_events(user_id: str, kind: str, days: int) -> int:
    _db.init()
    with _db.conn() as c:
        r = c.execute(
            "SELECT COUNT(*) AS n FROM events WHERE user_id=? AND kind=? "
            "AND ts >= datetime('now', ?)",
            (user_id, kind, f"-{days} days"),
        ).fetchone()
        return int(r["n"])


def score_lead(user_id: str) -> dict:
    score = 0.0
    breakdown: dict[str, float] = {}

    if _count_events(user_id, "query", 30) >= 50:
        score += 0.3
        breakdown["query_volume_30d"] = 0.3
    if _count_events(user_id, "pairing_request", 30) >= 20:
        score += 0.3
        breakdown["pairing_requests_30d"] = 0.3
    if _count_events(user_id, "anki_card_done", 30) >= 100:
        score += 0.2
        breakdown["anki_completion"] = 0.2
    if _count_events(user_id, "briefing_view", 30) >= 14:
        score += 0.2
        breakdown["briefing_engagement"] = 0.2

    # Invite acceptances
    from .invite_tracker import invite_count
    if invite_count(user_id, accepted_only=True) >= 1:
        score += 0.2
        breakdown["invite_acceptances"] = 0.2

    return {
        "user_id": user_id,
        "score": min(1.0, round(score, 3)),
        "above_threshold": score >= LEAD_THRESHOLD,
        "breakdown": breakdown,
    }
