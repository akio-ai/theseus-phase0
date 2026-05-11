"""
CIVC (Comité Champagne) extractor — Tier 2 regional.

Seeds are listed inline; orchestrator drives the loop. Each yielded tuple has
the schema needed by llm.structurer.structure_entity().
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from core.schema.entities import SourceTier
from crawler.fetcher import fetch
from crawler.config import lookup


@dataclass
class Seed:
    url: str
    entity_kind: str       # 'cuvee' | 'producer' | 'appellation'
    excerpt_selector: str  # CSS-style hint (extracted by BeautifulSoup in Batch 3; for now: pass full body up to 4KB)


# Phase 0 starter seeds. Expand in batches as we verify each producer page renders cleanly.
SEEDS: list[Seed] = [
    Seed(url="https://www.champagne.fr/en/from-vine-to-wine/the-aoc-champagne/the-appellation-area",
         entity_kind="appellation", excerpt_selector="main"),
    Seed(url="https://www.champagne.fr/en/from-vine-to-wine/the-aoc-champagne/the-grape-varieties",
         entity_kind="appellation", excerpt_selector="main"),
]


def iter_extracts(max_excerpt_bytes: int = 4096) -> Iterator[tuple[str, str, str, SourceTier, str]]:
    """
    Yields: (entity_kind, url, excerpt, tier, license).
    Excerpt is bounded — we do not store raw text long-term (only excerpt_hash).
    """
    for seed in SEEDS:
        src = lookup("champagne.fr")
        if not src:
            continue
        result = fetch(seed.url)
        # Crude excerpt: head of body. Batch 3 swaps in BeautifulSoup selector.
        excerpt = result.text[:max_excerpt_bytes]
        yield seed.entity_kind, result.url, excerpt, src.tier, src.license
