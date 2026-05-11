"""
Structuring prompts. Phase 0 focuses on Champagne entities.

Prompt design principles (compass-aligned):
- Output JSON only (no prose) — parsed strictly
- Refuse if input contains critic-score numerical evaluations
- Emit `confidence_note` if unsure, instead of inventing
- Never invent producer names / dosage values
- All numbers must be traceable to the source excerpt (cited verbatim)
"""
from __future__ import annotations

SYSTEM_BASE = """\
You are a structured-extraction module for Theseus, a wine knowledge layer.
You receive a verbatim excerpt from an OFFICIAL wine source (government, regional
trade body, producer official site, or public-data repository).

Your only output is a JSON object matching the requested schema. No prose, no
markdown, no code fences. If the excerpt does not contain enough information for
a field, set it to null and add a brief `confidence_note`.

Hard rules:
- Do NOT invent facts not present in the excerpt.
- Do NOT include critic scores (Robert Parker, Wine Spectator, Decanter, Vinous, etc.).
- Do NOT include marketing prose; only structured facts.
- All values must be in their original units; do not convert.
- If the excerpt is purely promotional with no extractable facts, return
  {"extractable": false, "reason": "<short>"}.
"""


CUVEE_SCHEMA_HINT = """\
Schema for Cuvée extraction:
{
  "entity_type": "cuvee",
  "name": "string (canonical bottling name)",
  "producer_name": "string (winery / champagne house name)",
  "appellation": "string | null  (e.g. 'Champagne', 'Brut Nature')",
  "vintage_year": "int | null  (null for NV)",
  "base_year": "int | null  (for NV: base year if disclosed)",
  "cepage": {"chardonnay": 0.0-1.0, "pinot_noir": 0.0-1.0, "pinot_meunier": 0.0-1.0, "other": 0.0-1.0} | null,
  "dosage_g_l": "float | null  (grams of sugar per liter)",
  "aging_months": "int | null  (total months on lees)",
  "vineyards": ["string"]  (named vineyards / lieux-dits, empty if not specified),
  "confidence_note": "string | null"
}
"""


PRODUCER_SCHEMA_HINT = """\
Schema for Producer extraction:
{
  "entity_type": "producer",
  "name": "string (canonical house / domaine name)",
  "country": "string (ISO country name, e.g. 'France')",
  "region": "string (e.g. 'Champagne', 'Burgundy')",
  "appellation": "string | null  (primary appellation)",
  "founded_year": "int | null",
  "house_style": "string | null  (factual description of method; NO marketing adjectives)",
  "confidence_note": "string | null"
}
NOTE: 'house_style' must be a *factual* description (e.g. 'extended lees ageing
with malolactic blocked'), not promotional copy ('artisanal', 'exceptional').
"""


APPELLATION_SCHEMA_HINT = """\
Schema for Appellation extraction:
{
  "entity_type": "appellation",
  "name": "string (canonical AOC name)",
  "country": "string",
  "parent_appellation": "string | null  (e.g. 'Champagne' for 'Côteaux Champenois')",
  "permitted_varieties": ["string"],  (grape varieties from the cahier des charges)
  "rule_uri": "string | null  (URL to the official rules if present in excerpt)",
  "confidence_note": "string | null"
}
"""


def build_structuring_prompt(entity_kind: str, source_url: str, excerpt: str) -> tuple[str, str]:
    """
    Returns (system_prompt, user_message).
    entity_kind: 'cuvee' | 'producer' | 'appellation'
    """
    hint_map = {
        "cuvee": CUVEE_SCHEMA_HINT,
        "producer": PRODUCER_SCHEMA_HINT,
        "appellation": APPELLATION_SCHEMA_HINT,
    }
    if entity_kind not in hint_map:
        raise ValueError(f"unknown entity_kind: {entity_kind}")

    system = SYSTEM_BASE + "\n" + hint_map[entity_kind]
    user = (
        f"Source URL: {source_url}\n"
        f"Source excerpt (verbatim, do not paraphrase facts not present):\n"
        f"---\n{excerpt}\n---\n"
        f"Return the JSON object now."
    )
    return system, user
