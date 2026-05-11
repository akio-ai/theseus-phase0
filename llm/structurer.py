"""
Structurer — turns a crawler FetchResult excerpt into a Theseus Entity dataclass.

Pipeline:
  fetch (httpx) → extract excerpt (per-source extractor) →
    structurer.structure_entity() → upsert.upsert_entity() →
      audit + confidence + conflict detection
"""
from __future__ import annotations

import json
import logging
import re
from datetime import datetime, timezone
from typing import Any, Optional

from core.schema.entities import (
    Appellation, Cuvee, Layer, Producer, SourceRef, SourceTier,
)
from crawler.ethical_guardrails import assert_no_raw_text_storage

from .claude_client import call_claude
from .prompts import build_structuring_prompt

logger = logging.getLogger("theseus.structurer")


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = _SLUG_RE.sub("-", s).strip("-")
    return s[:80]


def _entity_id(kind: str, name: str, vintage: Optional[int] = None) -> str:
    base = f"{kind}:{slugify(name)}"
    if vintage:
        base += f"-{vintage}"
    return base


def _parse_json(text: str) -> dict:
    """LLM might wrap JSON in markdown despite instructions; strip code fences."""
    text = text.strip()
    if text.startswith("```"):
        # remove leading and trailing fences
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def structure_entity(
    *,
    entity_kind: str,
    source_url: str,
    excerpt: str,
    source_tier: SourceTier,
    license: str,
    op_id: Optional[str] = None,
):
    """
    Returns one of (Producer | Cuvee | Appellation) populated with one SourceRef.
    Raises ValueError if LLM declines (extractable=false) or schema mismatches.

    NOTE: caller is responsible for passing source_url + tier from a CleanSource —
    structurer trusts upstream guard checks.
    """
    system, user = build_structuring_prompt(entity_kind, source_url, excerpt)

    resp = call_claude(system=system, user=user, op_id=op_id)
    # Extract text content from Anthropic Message
    text_chunks = []
    for block in getattr(resp, "content", []):
        if getattr(block, "type", None) == "text":
            text_chunks.append(block.text)
    raw = "\n".join(text_chunks).strip()

    parsed = _parse_json(raw)

    if parsed.get("extractable") is False:
        raise ValueError(f"LLM declined extraction: {parsed.get('reason', 'unknown')}")

    sr = SourceRef(
        url=source_url,
        tier=source_tier,
        license=license,
        fetched_at=datetime.now(timezone.utc),
    )

    if entity_kind == "cuvee":
        entity = _build_cuvee(parsed, sr)
    elif entity_kind == "producer":
        entity = _build_producer(parsed, sr)
    elif entity_kind == "appellation":
        entity = _build_appellation(parsed, sr)
    else:
        raise ValueError(f"unknown kind: {entity_kind}")

    # Final ethical check on the structured payload
    assert_no_raw_text_storage(entity.extra_facts)
    return entity


def _build_cuvee(p: dict, sr: SourceRef) -> Cuvee:
    name = p["name"]
    vintage = p.get("vintage_year")
    return Cuvee(
        id=_entity_id("cuvee", f"{p.get('producer_name', 'unknown')}-{name}", vintage),
        name=name,
        layer=Layer.PUBLIC,
        source_refs=[sr],
        producer_id=_entity_id("producer", p.get("producer_name", "unknown")) if p.get("producer_name") else "",
        vintage_year=vintage,
        appellation_id=_entity_id("appellation", p["appellation"]) if p.get("appellation") else None,
        cepage=p.get("cepage") or {},
        dosage_g_l=p.get("dosage_g_l"),
        aging_months=p.get("aging_months"),
        base_year=p.get("base_year"),
        extra_facts={
            "vineyards": p.get("vineyards", []),
            "confidence_note": p.get("confidence_note"),
        },
    )


def _build_producer(p: dict, sr: SourceRef) -> Producer:
    return Producer(
        id=_entity_id("producer", p["name"]),
        name=p["name"],
        layer=Layer.PUBLIC,
        source_refs=[sr],
        country=p.get("country", ""),
        region=p.get("region", ""),
        appellation_id=_entity_id("appellation", p["appellation"]) if p.get("appellation") else None,
        founded_year=p.get("founded_year"),
        house_style=p.get("house_style", "") or "",
        extra_facts={"confidence_note": p.get("confidence_note")},
    )


def _build_appellation(p: dict, sr: SourceRef) -> Appellation:
    return Appellation(
        id=_entity_id("appellation", p["name"]),
        name=p["name"],
        layer=Layer.PUBLIC,
        source_refs=[sr],
        country=p.get("country", ""),
        parent_appellation_id=_entity_id("appellation", p["parent_appellation"])
            if p.get("parent_appellation") else None,
        rule_uri=p.get("rule_uri"),
        permitted_varieties=p.get("permitted_varieties", []) or [],
        extra_facts={"confidence_note": p.get("confidence_note")},
    )
