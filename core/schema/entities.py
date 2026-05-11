"""
Theseus Core entity definitions (Phase 0 — Champagne focus).

Design principles:
- Every entity carries source_refs[] (provenance) and confidence (0.0-1.0)
- Layer separation: PUBLIC (公的 layer, collective) vs PRIVATE (Akio's notes, Tier 5)
- Schema is JSONB-friendly: extra_facts dict for evolving fields without migration
- IDs are deterministic where possible (slug from canonical name) for cross-source merge

Compass alignment:
- No personal-name fields on public entities
- PRIVATE layer entries do not surface in public renderers (enforced by Layer enum +
  tests/test_anki_layer_isolation.py at Batch 3)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import IntEnum, StrEnum
from typing import Any, Optional


class Layer(StrEnum):
    """Public/private layer separation (compass §1)."""
    PUBLIC = "public"     # Collective knowledge, customer-facing OK
    PRIVATE = "private"   # Akio's notes / internal training only, never商品化


class SourceTier(IntEnum):
    """Source tier ranking — used in confidence calculation."""
    GOVERNMENT = 1        # INAO / EU / TTB / 国税庁
    REGIONAL = 2          # CIVC / BIVB / 日本酒造組合
    PRODUCER = 3          # 生産者公式 (robots OK)
    PUBLIC_DATA = 4       # Wikidata / Wikipedia
    AKIOS_NOTES = 5       # Human curation, differentiation asset
    LICENSED = 6          # ARR $1M 後 — Phase 0 では未使用


@dataclass(frozen=True)
class SourceRef:
    """Provenance for a single fact."""
    url: str
    tier: SourceTier
    license: str                            # 例: "CC0", "CC-BY-SA-4.0", "producer_official", "akio_notes"
    fetched_at: datetime
    excerpt_hash: Optional[str] = None      # SHA256 of source excerpt — for re-verification, NOT raw text
    note: str = ""                          # 任意 (例: "from CIVC 2024 cahier des charges")

    def __post_init__(self):
        # 評論家点数の URL を含むものは reject（著作権）
        forbidden_hosts = (
            "robertparker.com", "winespectator.com", "decanter.com",
            "vinous.com", "jamessuckling.com",
        )
        if any(h in self.url.lower() for h in forbidden_hosts):
            raise ValueError(
                f"SourceRef forbidden: critic-score sites are excluded per Phase 0 ethics policy "
                f"(url={self.url})"
            )


@dataclass
class _EntityBase:
    """Common fields for all entities."""
    id: str                                 # slug-style, e.g. "producer:krug" / "cuvee:krug-grande-cuvee-170eme-edition"
    name: str                               # canonical name (公的 layer に出る)
    layer: Layer = Layer.PUBLIC
    source_refs: list[SourceRef] = field(default_factory=list)
    confidence: float = 0.0                 # 0.0–1.0、verification.confidence で計算
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    extra_facts: dict[str, Any] = field(default_factory=dict)  # JSONB へ載る evolving fields


@dataclass
class Producer(_EntityBase):
    """Winery / Champagne house / sake brewery."""
    country: str = ""
    region: str = ""                        # e.g. "Champagne", "Burgundy"
    appellation_id: Optional[str] = None    # 主たる appellation
    founded_year: Optional[int] = None
    house_style: str = ""                   # 公的 layer の "team voice" 由来の記述、Akio 個人名は出さない


@dataclass
class Cuvee(_EntityBase):
    """A specific bottling (e.g. Krug Grande Cuvée 170ème Édition)."""
    producer_id: str = ""
    vintage_year: Optional[int] = None      # None = NV / multi-vintage
    appellation_id: Optional[str] = None
    cepage: dict[str, float] = field(default_factory=dict)   # {"chardonnay": 0.45, "pinot_noir": 0.40, "pinot_meunier": 0.15}
    dosage_g_l: Optional[float] = None
    aging_months: Optional[int] = None
    base_year: Optional[int] = None         # NV の base year


@dataclass
class Vineyard(_EntityBase):
    """A specific vineyard / climat / lieu-dit."""
    appellation_id: Optional[str] = None
    classification: str = ""                # "Grand Cru" / "Premier Cru" / "Climat" 等
    area_ha: Optional[float] = None
    soil: str = ""
    exposure: str = ""


@dataclass
class Appellation(_EntityBase):
    """AOC / AVA / DOC / 産地."""
    country: str = ""
    parent_appellation_id: Optional[str] = None  # hierarchy (e.g. Mâcon → Bourgogne)
    rule_uri: Optional[str] = None          # 公式 cahier des charges への link
    permitted_varieties: list[str] = field(default_factory=list)


@dataclass
class Vintage(_EntityBase):
    """A vintage year for a region (e.g. Champagne 2008)."""
    year: int = 0
    region: str = ""                        # 同年でも region 毎に評価違うため必須
    quality_score: Optional[float] = None   # 0-100、Tier 1-2 公式評価のみ採用 (critic不可)
    notes: str = ""
    weather_summary: str = ""


# Phase 0 では Champagne に focus するが、schema 自体は generic に作っている。
# Phase 1 で Sake / Burgundy / Bordeaux に拡張する際、entities 追加 (e.g. SakeYeast, RiceVariety) は
# 既存 schema を壊さずできる設計。
