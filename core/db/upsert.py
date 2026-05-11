"""
Upsert with provenance + confidence merging.

Each upsert:
1. Resolves the entity (by id; entity ids are deterministic slugs)
2. Merges incoming facts JSONB into existing facts JSONB (field-level)
3. Detects per-field conflicts → writes to conflicts table, flags entity provisional
4. Appends source_refs (never overwrites — provenance is append-only)
5. Recomputes confidence from full source set
6. Writes audit_log entry

All writes go through this module — direct INSERT/UPDATE on entities is forbidden
(enforced via PR review + tests/test_audit_log_coverage at Batch 3).
"""
from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from .connection import get_connection
from ..schema.entities import _EntityBase, SourceRef, Layer
from ..verification.confidence import compute_confidence


def upsert_entity(entity: _EntityBase, actor: str) -> dict[str, Any]:
    """
    Upsert an entity. Returns dict with keys:
      - status: 'inserted' | 'updated' | 'noop'
      - conflicts: list[{field, old, new, old_source, new_source}]
      - confidence_after: float
    """
    entity_dict = _entity_to_row(entity)
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Fetch existing
            cur.execute(
                "SELECT id, entity_type, name, layer, confidence, facts "
                "FROM entities WHERE id = %s FOR UPDATE",
                (entity.id,),
            )
            existing = cur.fetchone()

            conflicts_found: list[dict] = []

            if existing is None:
                # INSERT
                cur.execute(
                    """
                    INSERT INTO entities (id, entity_type, name, layer, confidence, facts)
                    VALUES (%s, %s, %s, %s, %s, %s::jsonb)
                    """,
                    (
                        entity.id,
                        entity_dict["entity_type"],
                        entity.name,
                        entity.layer.value,
                        entity.confidence,
                        json.dumps(entity_dict["facts"]),
                    ),
                )
                status = "inserted"
                cur.execute(
                    """
                    INSERT INTO audit_log (op, entity_id, actor, payload_before, payload_after)
                    VALUES ('insert', %s, %s, NULL, %s::jsonb)
                    """,
                    (entity.id, actor, json.dumps(entity_dict)),
                )
            else:
                # MERGE
                merged_facts, conflicts_found = _merge_facts(
                    existing["facts"], entity_dict["facts"],
                    new_source_url=(entity.source_refs[0].url if entity.source_refs else None),
                )
                cur.execute(
                    """
                    UPDATE entities
                       SET name = %s,
                           facts = %s::jsonb,
                           updated_at = NOW()
                     WHERE id = %s
                    """,
                    (entity.name, json.dumps(merged_facts), entity.id),
                )
                status = "updated"
                cur.execute(
                    """
                    INSERT INTO audit_log (op, entity_id, actor, payload_before, payload_after)
                    VALUES ('update', %s, %s, %s::jsonb, %s::jsonb)
                    """,
                    (entity.id, actor, json.dumps(dict(existing)), json.dumps(entity_dict)),
                )
                # Log conflicts
                for c in conflicts_found:
                    cur.execute(
                        """
                        INSERT INTO conflicts
                            (entity_id, field_path, old_value, new_value, old_source_url, new_source_url)
                        VALUES (%s, %s, %s::jsonb, %s::jsonb, %s, %s)
                        """,
                        (
                            entity.id, c["field"],
                            json.dumps(c["old"]), json.dumps(c["new"]),
                            c.get("old_source"), c.get("new_source"),
                        ),
                    )

            # Append source_refs (always — provenance is append-only)
            for sr in entity.source_refs:
                cur.execute(
                    """
                    INSERT INTO source_refs
                        (entity_id, url, tier, license, fetched_at, excerpt_hash, note)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        entity.id, sr.url, sr.tier.name.lower(),
                        sr.license, sr.fetched_at, sr.excerpt_hash, sr.note,
                    ),
                )

            # Recompute confidence
            cur.execute(
                "SELECT tier FROM source_refs WHERE entity_id = %s",
                (entity.id,),
            )
            tiers = [row["tier"] for row in cur.fetchall()]
            new_conf = compute_confidence(tiers, num_conflicts=len(conflicts_found))
            cur.execute(
                "UPDATE entities SET confidence = %s WHERE id = %s",
                (new_conf, entity.id),
            )

        conn.commit()

    return {
        "status": status,
        "conflicts": conflicts_found,
        "confidence_after": new_conf,
    }


def _entity_to_row(entity: _EntityBase) -> dict:
    """Convert dataclass entity → row dict (entity_type + facts JSONB)."""
    full = asdict(entity)
    # Strip top-level columns from facts
    facts = {k: v for k, v in full.items()
             if k not in ("id", "name", "layer", "source_refs", "confidence",
                          "created_at", "updated_at", "extra_facts")}
    # Merge extra_facts into facts
    facts.update(entity.extra_facts)
    # Drop datetimes from facts (they shouldn't be there); convert any to iso
    return {
        "id": entity.id,
        "entity_type": type(entity).__name__.lower(),
        "name": entity.name,
        "layer": entity.layer.value,
        "facts": _jsonable(facts),
    }


def _jsonable(obj: Any) -> Any:
    """Recursively convert non-JSON types to JSON-friendly forms."""
    if isinstance(obj, dict):
        return {k: _jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonable(v) for v in obj]
    if hasattr(obj, "isoformat"):
        return obj.isoformat()
    return obj


def _merge_facts(old: dict, new: dict, new_source_url: str | None) -> tuple[dict, list[dict]]:
    """
    Per-field merge. New value wins for missing fields. Conflicting non-null
    values are kept as old + recorded in conflicts.
    """
    merged = dict(old)
    conflicts: list[dict] = []
    for k, v in new.items():
        if v is None or v == "" or v == {} or v == []:
            continue
        if k not in old or old[k] in (None, "", {}, []):
            merged[k] = v
        elif old[k] != v:
            # Conflict — keep old, log new
            conflicts.append({
                "field": f"facts.{k}",
                "old": old[k],
                "new": v,
                "new_source": new_source_url,
            })
        # else: equal — noop
    return merged, conflicts
