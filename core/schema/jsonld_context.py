"""
JSON-LD context for Theseus entities — makes data portable to schema.org
consumers and future SPARQL/Neo4j migration.

Phase 0 ではエクスポート時に使う。Phase 1 で API 公開時、Schema.org compatible
を保つことで SEO / third-party integration が安く済む。
"""
from __future__ import annotations

THESEUS_NS = "https://theseus.egal.io/ns#"
SCHEMA_NS = "https://schema.org/"

JSONLD_CONTEXT = {
    "@version": 1.1,
    "theseus": THESEUS_NS,
    "schema": SCHEMA_NS,
    # Entity types
    "Producer":     "theseus:Producer",
    "Cuvee":        "theseus:Cuvee",
    "Vineyard":     "theseus:Vineyard",
    "Appellation":  "theseus:Appellation",
    "Vintage":      "theseus:Vintage",
    # Core fields
    "name":         "schema:name",
    "country":      "schema:addressCountry",
    "region":       "schema:addressRegion",
    "founded_year": "schema:foundingDate",
    # Theseus-specific
    "cepage":       "theseus:cepage",
    "dosage_g_l":   "theseus:dosageGramsPerLiter",
    "aging_months": "theseus:agingMonths",
    "appellation_id":            {"@id": "theseus:appellation",       "@type": "@id"},
    "producer_id":               {"@id": "theseus:producer",          "@type": "@id"},
    "parent_appellation_id":     {"@id": "theseus:parentAppellation", "@type": "@id"},
    # Provenance
    "source_refs":  "theseus:sourceRefs",
    "confidence":   "theseus:confidence",
    "layer":        "theseus:layer",
}


def wrap_jsonld(entity_dict: dict) -> dict:
    """Wrap a serialized entity in JSON-LD envelope."""
    out = {"@context": JSONLD_CONTEXT}
    out.update(entity_dict)
    return out
