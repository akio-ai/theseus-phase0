"""
Source tracking helpers — used by briefing/eval/citation_validator.
"""
from __future__ import annotations

from ..db.connection import get_connection


def distinct_source_count(entity_id: str) -> int:
    """Count distinct source URLs for an entity (DoD: ≥3 for completion)."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(DISTINCT url) AS n FROM source_refs WHERE entity_id = %s",
                (entity_id,),
            )
            return cur.fetchone()["n"]


def entities_below_source_threshold(min_sources: int = 3, limit: int = 100) -> list[dict]:
    """Find entities with fewer than `min_sources` distinct sources (crawler backlog)."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT e.id, e.name, e.entity_type, COUNT(DISTINCT s.url) AS n_sources
                  FROM entities e
                  LEFT JOIN source_refs s ON s.entity_id = e.id
                 GROUP BY e.id, e.name, e.entity_type
                HAVING COUNT(DISTINCT s.url) < %s
                 ORDER BY n_sources ASC, e.id ASC
                 LIMIT %s
                """,
                (min_sources, limit),
            )
            return [dict(r) for r in cur.fetchall()]
