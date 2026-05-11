"""
pgvector semantic search. Embeddings populated by Batch 2 structurer.

Usage:
    hits = search_similar(query_embedding=[...1536 dims...], k=10, layer='public')
"""
from __future__ import annotations

from typing import Optional

from .connection import get_connection


def search_similar(
    query_embedding: list[float],
    k: int = 10,
    entity_type: Optional[str] = None,
    layer: Optional[str] = "public",
) -> list[dict]:
    """Return top-k nearest entities by cosine distance on embedding."""
    where_parts = ["embedding IS NOT NULL"]
    params: list = []
    if entity_type:
        where_parts.append("entity_type = %s")
        params.append(entity_type)
    if layer:
        where_parts.append("layer = %s")
        params.append(layer)
    where_sql = " AND ".join(where_parts)
    params.append(query_embedding)
    params.append(k)

    sql = f"""
        SELECT id, entity_type, name, layer, confidence, facts,
               (embedding <=> %s::vector) AS distance
          FROM entities
         WHERE {where_sql}
         ORDER BY embedding <=> %s::vector
         LIMIT %s
    """
    # Rearrange params: the two %s for the <=> operator come first in the prepared bind list
    # ordering in psycopg is positional in execute(), so build accordingly:
    final_params = [*params[:-2], query_embedding, query_embedding, k] if False else None
    # simpler: rebuild
    bind = []
    if entity_type:
        bind.append(entity_type)
    if layer:
        bind.append(layer)
    bind.extend([query_embedding, query_embedding, k])

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, bind)
            return [dict(r) for r in cur.fetchall()]


def set_embedding(entity_id: str, embedding: list[float]) -> None:
    """Write an embedding vector (1536 dims expected)."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE entities SET embedding = %s::vector WHERE id = %s",
                (embedding, entity_id),
            )
        conn.commit()
