"""
INAO (Institut national de l'origine et de la qualité) — Tier 1 government.

Provides the official AOC cahiers des charges. Phase 0 grabs the Champagne AOC
document and its sub-AOCs (Coteaux Champenois, Rosé des Riceys).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from core.schema.entities import SourceTier
from crawler.config import lookup
from crawler.fetcher import fetch


@dataclass
class InaoSeed:
    url: str
    appellation_name: str


SEEDS: list[InaoSeed] = [
    # Cahier des charges Champagne (PDF often; HTML preferred)
    InaoSeed(
        url="https://www.inao.gouv.fr/Espace-professionnel-et-outils/Produits-officiels-de-qualite/Champagne",
        appellation_name="Champagne",
    ),
    InaoSeed(
        url="https://www.inao.gouv.fr/Espace-professionnel-et-outils/Produits-officiels-de-qualite/Coteaux-champenois",
        appellation_name="Coteaux Champenois",
    ),
    InaoSeed(
        url="https://www.inao.gouv.fr/Espace-professionnel-et-outils/Produits-officiels-de-qualite/Rose-des-Riceys",
        appellation_name="Rosé des Riceys",
    ),
]


def iter_extracts(max_excerpt_bytes: int = 4096) -> Iterator[tuple[str, str, str, SourceTier, str]]:
    src = lookup("inao.gouv.fr")
    if not src:
        return
    for seed in SEEDS:
        result = fetch(seed.url)
        excerpt = result.text[:max_excerpt_bytes]
        yield "appellation", result.url, excerpt, src.tier, src.license
