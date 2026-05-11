"""
Anki layer isolation — compass enforcement.

Asserts:
- Staff deck contains ZERO private-layer entities
- Staff deck contains ZERO cards tagged 'private'
- Personal deck includes both layers
- Akio's personal name does NOT leak into staff card fronts or backs
"""
from __future__ import annotations

import re

import pytest

from anki.personal_version import build_personal_deck
from anki.staff_version import build_staff_deck
from anki.exporter import to_anki_txt


# Personal name patterns we forbid in staff output (compass + user_name_kanji.md)
FORBIDDEN_PATTERNS = [
    re.compile(r"\bAkio\b", re.IGNORECASE),
    re.compile(r"\bMatsumoto\b", re.IGNORECASE),
    re.compile(r"松本昭生"),
    re.compile(r"昭生"),
]


@pytest.fixture
def mixed_entities():
    """Sample set with both public and private entities."""
    return [
        # Public — should appear in BOTH personal and staff
        {
            "id": "appellation:champagne",
            "entity_type": "appellation",
            "name": "Champagne",
            "layer": "public",
            "facts": {"country": "France", "permitted_varieties": ["Chardonnay", "Pinot Noir", "Pinot Meunier"]},
        },
        {
            "id": "producer:krug",
            "entity_type": "producer",
            "name": "Krug",
            "layer": "public",
            "facts": {"founded_year": 1843, "house_style": "extended lees ageing with oxidative profile"},
        },
        {
            "id": "cuvee:krug-grande-cuvee-170",
            "entity_type": "cuvee",
            "name": "Krug Grande Cuvée 170",
            "layer": "public",
            "facts": {"cepage": {"chardonnay": 0.45, "pinot_noir": 0.40, "pinot_meunier": 0.15},
                      "dosage_g_l": 5.0, "aging_months": 84},
        },
        # PRIVATE — Akio's tasting note. MUST NOT appear in staff deck.
        {
            "id": "producer:krug",  # same id, but with private commentary
            "entity_type": "producer",
            "name": "Krug",
            "layer": "private",
            "facts": {"founded_year": 1843,
                      "house_style": "Akio's personal observation: tighter Vintage 2008 disgorgement reads more linear"},
        },
        {
            "id": "cuvee:obscure-grower",
            "entity_type": "cuvee",
            "name": "Akio's pet grower champagne",
            "layer": "private",
            "facts": {"dosage_g_l": 2.5},
        },
    ]


def test_staff_deck_has_no_private_layer_entries(mixed_entities):
    cards = build_staff_deck(mixed_entities)
    assert len(cards) > 0
    for c in cards:
        assert "private" not in c.tags, f"private tag leaked: {c}"


def test_staff_deck_drops_private_named_cuvee(mixed_entities):
    cards = build_staff_deck(mixed_entities)
    for c in cards:
        for pat in FORBIDDEN_PATTERNS:
            assert not pat.search(c.front), f"forbidden name in front: {c.front}"
            assert not pat.search(c.back),  f"forbidden name in back:  {c.back}"


def test_personal_deck_includes_private(mixed_entities):
    cards = build_personal_deck(mixed_entities)
    private_cards = [c for c in cards if "private" in c.tags]
    assert len(private_cards) > 0, "personal deck must contain private-layer cards"


def test_staff_export_text_has_no_personal_names(mixed_entities):
    cards = build_staff_deck(mixed_entities)
    txt = to_anki_txt(cards)
    for pat in FORBIDDEN_PATTERNS:
        m = pat.search(txt)
        assert m is None, f"forbidden name leaked into staff export: {m.group()!r}"


def test_personal_export_is_personal_tagged(mixed_entities):
    cards = build_personal_deck(mixed_entities)
    txt = to_anki_txt(cards)
    assert "personal" in txt
