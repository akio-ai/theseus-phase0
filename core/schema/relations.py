"""
Relation types — typed edges between entities.

Phase 0 のグラフは shallow (cuvée → producer / vineyard / appellation / vintage 程度)。
Phase 2 で Neo4j 移行する場合の前提として、関係も provenance + confidence を持つ。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum

from .entities import SourceRef


class RelationType(StrEnum):
    PRODUCES = "produces"                       # Producer  → Cuvee
    BOTTLED_FROM = "bottled_from"               # Cuvee     → Vineyard (parcellaire 等)
    LOCATED_IN = "located_in"                   # Vineyard  → Appellation
    SUB_APPELLATION_OF = "sub_appellation_of"   # Appellation → Appellation
    OF_VINTAGE = "of_vintage"                   # Cuvee     → Vintage
    BLENDS_WITH = "blends_with"                 # Cuvee     → Cuvee (assemblage cross-ref)


@dataclass
class Relation:
    subject_id: str
    predicate: RelationType
    object_id: str
    source_refs: list[SourceRef] = field(default_factory=list)
    confidence: float = 0.0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    extra: dict = field(default_factory=dict)
