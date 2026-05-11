"""
Staff deck — Tier 1-4 only. Private layer entities are DROPPED.

Compass enforcement: zero Akio's-Notes content in staff output.
tests/test_anki_layer_isolation.py asserts this at hard fail level.
"""
from __future__ import annotations

from typing import Iterable

from .card_generator import Card, generate_cards


def build_staff_deck(entities: Iterable[dict]) -> list[Card]:
    """
    Filter to layer == 'public' only, BEFORE card generation.
    Double-filter: also drop any card whose tags include 'private'.
    """
    public_only = [e for e in entities if e.get("layer") == "public"]
    cards = generate_cards(public_only)
    # Defensive: drop any card tagged private (should be none, but enforce)
    cards = [c for c in cards if "private" not in c.tags]
    # Tag for filtering
    for c in cards:
        if "staff" not in c.tags:
            c.tags.append("staff")
    return cards
