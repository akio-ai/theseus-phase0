"""
Personal deck — includes BOTH public + private layer (Tier 5 Akio's Notes).
For Akio's CMS prep only. NEVER export to staff or customers.
"""
from __future__ import annotations

from typing import Iterable

from .card_generator import Card, generate_cards


def build_personal_deck(entities: Iterable[dict]) -> list[Card]:
    """All entities (public + private) are eligible."""
    cards = generate_cards(entities)
    # Personal deck explicit tag for easy filtering in Anki UI
    for c in cards:
        if "personal" not in c.tags:
            c.tags.append("personal")
    return cards
