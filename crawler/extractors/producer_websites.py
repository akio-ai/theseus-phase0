"""
Producer official websites — Tier 3.

Each producer must be registered (with robots-allowed) in PRODUCER_REGISTRY.
We do NOT scrape any producer without an explicit registry entry — even if
their domain technically passes robots.txt.

This is the safest gate: the team must add a producer to the registry (a
deliberate human decision) before crawling.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from core.schema.entities import SourceTier
from crawler.config import CleanSource, CLEAN_SOURCES
from crawler.fetcher import fetch


@dataclass
class ProducerSeed:
    domain: str            # 'krug.com'
    house_name: str
    seed_urls: list[str]   # canonical pages: /about, /cuvees, /winery


# Phase 0 starter — 3 houses to validate the pipeline end-to-end.
# Expand to ~50 once orchestrator runs cleanly in production.
PRODUCER_REGISTRY: list[ProducerSeed] = [
    # NOTE: registry entries below are illustrative; before any production
    # crawl, the team must:
    #   1. Verify robots.txt allows TheseusBot
    #   2. Register the domain in crawler/config.CLEAN_SOURCES with Tier=producer
    #   3. Confirm seed_urls render structured product pages (not SPA-only)
    ProducerSeed(
        domain="krug.com",
        house_name="Krug",
        seed_urls=["https://www.krug.com/en/maison-krug/our-history"],
    ),
    ProducerSeed(
        domain="bollinger.com",
        house_name="Bollinger",
        seed_urls=["https://www.bollinger.com/en/the-house/the-history"],
    ),
    ProducerSeed(
        domain="ruinart.com",
        house_name="Ruinart",
        seed_urls=["https://www.ruinart.com/en-ww/the-house-of-ruinart"],
    ),
]


def _ensure_registered(domain: str) -> CleanSource | None:
    """Producer must already be in CLEAN_SOURCES — orchestrator adds them at startup."""
    for src in CLEAN_SOURCES:
        if src.host == domain or domain.endswith("." + src.host):
            return src
    return None


def iter_extracts(max_excerpt_bytes: int = 4096) -> Iterator[tuple[str, str, str, SourceTier, str]]:
    for seed in PRODUCER_REGISTRY:
        src = _ensure_registered(seed.domain)
        if src is None:
            # Skip silently — the orchestrator surfaces this in the briefing as
            # "unregistered producer in seed list".
            continue
        for url in seed.seed_urls:
            result = fetch(url)
            excerpt = result.text[:max_excerpt_bytes]
            yield "producer", result.url, excerpt, src.tier, src.license
