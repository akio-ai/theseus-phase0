"""
Conflict detection & resolution helpers.

Phase 0 では auto-resolve しない（human review queue 行き）。
Phase 1 で 「Tier 1 が新値 vs Tier 4 が旧値 → 新値採用」のような rule-based resolver を追加予定。
"""
from __future__ import annotations

from .connection import get_connection


def open_conflict_count() -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) AS n FROM conflicts WHERE resolved_at IS NULL")
            return cur.fetchone()["n"]


def conflict_rate() -> float:
    """Open conflicts / total entities. Phase 0 DoD requires < 5%."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) AS n FROM entities")
            total = cur.fetchone()["n"]
            if total == 0:
                return 0.0
            cur.execute("SELECT COUNT(*) AS n FROM conflicts WHERE resolved_at IS NULL")
            open_n = cur.fetchone()["n"]
            return open_n / total


def list_open_conflicts(limit: int = 50) -> list[dict]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT c.id, c.entity_id, e.name, c.field_path,
                       c.old_value, c.new_value, c.old_source_url, c.new_source_url,
                       c.detected_at
                  FROM conflicts c
                  JOIN entities e ON e.id = c.entity_id
                 WHERE c.resolved_at IS NULL
                 ORDER BY c.detected_at DESC
                 LIMIT %s
                """,
                (limit,),
            )
            return [dict(r) for r in cur.fetchall()]


def resolve_conflict(conflict_id: int, note: str) -> None:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE conflicts SET resolved_at = NOW(), resolution_note = %s WHERE id = %s",
                (note, conflict_id),
            )
        conn.commit()
