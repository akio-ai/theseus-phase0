"""
Wikidata extractor — Tier 4 public data (CC0).

Wikidata has a clean SPARQL endpoint. Phase 0 query: all Champagne houses
(instance of Q1133779 "winery" with country=France, region containing "Champagne").

We use SPARQL JSON, not HTML — so output is already structured. We bypass the LLM
structurer for Wikidata and emit Entities directly.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterator

import httpx

from control.kill_switch import is_killed
from core.schema.entities import Layer, Producer, SourceRef, SourceTier
from crawler.config import USER_AGENT, lookup
from crawler.ethical_guardrails import assert_allowed
from llm.structurer import _entity_id  # reuse slug helper


SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

# Producers in Champagne region (Q23148). Wikidata QID 'Q1133779' = winery.
QUERY_CHAMPAGNE_PRODUCERS = """
SELECT ?house ?houseLabel ?founded ?regionLabel WHERE {
  ?house wdt:P31/wdt:P279* wd:Q1133779 .
  ?house wdt:P131* wd:Q23148 .
  OPTIONAL { ?house wdt:P571 ?founded . }
  OPTIONAL { ?house wdt:P131 ?region . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 500
"""


def iter_producers() -> Iterator[Producer]:
    """Yield Producer entities directly from Wikidata SPARQL (no LLM needed)."""
    if is_killed():
        return
    assert_allowed(SPARQL_ENDPOINT)  # robots + rate limit
    src = lookup("query.wikidata.org") or lookup("wikidata.org")
    if not src:
        return

    headers = {"User-Agent": USER_AGENT, "Accept": "application/sparql-results+json"}
    with httpx.Client(headers=headers, timeout=30.0) as client:
        resp = client.get(SPARQL_ENDPOINT, params={"query": QUERY_CHAMPAGNE_PRODUCERS})
    resp.raise_for_status()
    payload = resp.json()

    for binding in payload.get("results", {}).get("bindings", []):
        name = binding.get("houseLabel", {}).get("value", "").strip()
        if not name:
            continue
        founded = binding.get("founded", {}).get("value")
        founded_year = None
        if founded:
            try:
                founded_year = int(founded[:4])
            except (ValueError, TypeError):
                founded_year = None

        wikidata_uri = binding.get("house", {}).get("value", "")
        sr = SourceRef(
            url=wikidata_uri or "https://www.wikidata.org/",
            tier=SourceTier.PUBLIC_DATA,
            license="CC0",
            fetched_at=datetime.now(timezone.utc),
        )
        yield Producer(
            id=_entity_id("producer", name),
            name=name,
            layer=Layer.PUBLIC,
            source_refs=[sr],
            country="France",
            region="Champagne",
            founded_year=founded_year,
            extra_facts={"wikidata_uri": wikidata_uri},
        )
