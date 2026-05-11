"""
Allow-list of clean sources (Option A+ ethical scope).

Anything outside this list is rejected by ethical_guardrails.is_allowed_host().
Adding sources requires explicit Tier classification + license attribution.
"""
from __future__ import annotations

from dataclasses import dataclass

from core.schema.entities import SourceTier


@dataclass(frozen=True)
class CleanSource:
    host: str                    # e.g. 'maisons-champagne.com'
    tier: SourceTier
    license: str                 # 'CC0' / 'CC-BY-SA-4.0' / 'producer_official' / 'public_domain' etc.
    min_delay_seconds: float     # rate limit (producer sites = 5s+, others = 1s+)
    note: str = ""


CLEAN_SOURCES: list[CleanSource] = [
    # Tier 1 — Government / Treaty body
    CleanSource(
        host="inao.gouv.fr",
        tier=SourceTier.GOVERNMENT,
        license="public_sector_information_fr",
        min_delay_seconds=2.0,
        note="French AOC official",
    ),
    CleanSource(
        host="ec.europa.eu",
        tier=SourceTier.GOVERNMENT,
        license="eu_decision_2011_833",
        min_delay_seconds=2.0,
        note="EU eAmbrosia GI register",
    ),
    CleanSource(
        host="ttb.gov",
        tier=SourceTier.GOVERNMENT,
        license="us_gov_works_public_domain",
        min_delay_seconds=2.0,
        note="US Alcohol Tax & Trade Bureau",
    ),

    # Tier 2 — Regional / Trade body (Champagne focus for Phase 0)
    CleanSource(
        host="champagne.fr",
        tier=SourceTier.REGIONAL,
        license="civc_attribution",
        min_delay_seconds=3.0,
        note="CIVC — Comité Champagne",
    ),
    CleanSource(
        host="maisons-champagne.com",
        tier=SourceTier.REGIONAL,
        license="champagne_houses_union",
        min_delay_seconds=3.0,
    ),

    # Tier 4 — Public data
    CleanSource(
        host="wikidata.org",
        tier=SourceTier.PUBLIC_DATA,
        license="CC0",
        min_delay_seconds=1.0,
    ),
    CleanSource(
        host="en.wikipedia.org",
        tier=SourceTier.PUBLIC_DATA,
        license="CC-BY-SA-4.0",
        min_delay_seconds=1.0,
    ),
    CleanSource(
        host="fr.wikipedia.org",
        tier=SourceTier.PUBLIC_DATA,
        license="CC-BY-SA-4.0",
        min_delay_seconds=1.0,
    ),

    # Tier 3 — Producer sites added per-producer in Batch 2 (require robots.txt re-check per fetch)
]


# Explicit DENY list — even within Tier 3 producers, these are off-limits (critic scores etc.)
DENIED_HOSTS: set[str] = {
    "robertparker.com",
    "winespectator.com",
    "decanter.com",
    "vinous.com",
    "jamessuckling.com",
    "wineadvocate.com",
}


def lookup(host: str) -> CleanSource | None:
    host = host.lower().lstrip(".")
    for src in CLEAN_SOURCES:
        if host == src.host or host.endswith("." + src.host):
            return src
    return None


def is_denied(host: str) -> bool:
    host = host.lower()
    return any(h in host for h in DENIED_HOSTS)


# User-Agent — must be honest (no spoofing)
USER_AGENT = "TheseusBot/0.1 (+https://egal.io/bot; contact@egal.io)"
