"""
Generic card generator from Theseus entity dicts.

Cards have a tag set; consumers filter by tag for personal vs staff decks.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Sequence


@dataclass
class Card:
    front: str
    back: str
    tags: list[str] = field(default_factory=list)


def _appellation_card(e: dict) -> list[Card]:
    facts = e.get("facts", {})
    out = []
    name = e["name"]
    country = facts.get("country", "")
    out.append(Card(
        front=f"Where is the appellation {name}?",
        back=f"{country}, parent: {facts.get('parent_appellation_id') or '—'}",
        tags=["appellation", "geography", e["layer"]],
    ))
    pv = facts.get("permitted_varieties") or []
    if pv:
        out.append(Card(
            front=f"Permitted varieties in {name}?",
            back=", ".join(pv),
            tags=["appellation", "varieties", e["layer"]],
        ))
    return out


def _producer_card(e: dict) -> list[Card]:
    facts = e.get("facts", {})
    out = []
    out.append(Card(
        front=f"Founded year of {e['name']}?",
        back=str(facts.get("founded_year") or "unknown"),
        tags=["producer", e["layer"]],
    ))
    if facts.get("house_style"):
        out.append(Card(
            front=f"What is the house style of {e['name']}?",
            back=facts["house_style"],
            tags=["producer", "style", e["layer"]],
        ))
    return out


def _cuvee_card(e: dict) -> list[Card]:
    facts = e.get("facts", {})
    out = []
    name = e["name"]
    if facts.get("cepage"):
        cep_str = ", ".join(f"{k} {int(v*100)}%" for k, v in facts["cepage"].items() if v)
        if cep_str:
            out.append(Card(
                front=f"Cépage of {name}?",
                back=cep_str,
                tags=["cuvee", "cepage", e["layer"]],
            ))
    if facts.get("dosage_g_l") is not None:
        out.append(Card(
            front=f"Dosage of {name} (g/L)?",
            back=f"{facts['dosage_g_l']} g/L",
            tags=["cuvee", "dosage", e["layer"]],
        ))
    if facts.get("aging_months") is not None:
        out.append(Card(
            front=f"Aging months of {name}?",
            back=f"{facts['aging_months']} months on lees",
            tags=["cuvee", "aging", e["layer"]],
        ))
    return out


_BUILDERS = {
    "appellation": _appellation_card,
    "producer":    _producer_card,
    "cuvee":       _cuvee_card,
}


def generate_cards(entities: Iterable[dict]) -> list[Card]:
    cards: list[Card] = []
    for e in entities:
        builder = _BUILDERS.get(e.get("entity_type", ""))
        if builder:
            cards.extend(builder(e))
    return cards
