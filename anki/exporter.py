"""
Anki .txt exporter (tab-separated format with tags).

Format: Front<TAB>Back<TAB>tag1 tag2 tag3
This is the standard Anki "import .txt" format.
"""
from __future__ import annotations

from typing import Iterable

from .card_generator import Card


def to_anki_txt(cards: Iterable[Card]) -> str:
    lines = []
    for c in cards:
        front = c.front.replace("\t", " ").replace("\n", "<br>")
        back  = c.back.replace("\t", " ").replace("\n", "<br>")
        tags  = " ".join(c.tags)
        lines.append(f"{front}\t{back}\t{tags}")
    return "\n".join(lines) + "\n"
