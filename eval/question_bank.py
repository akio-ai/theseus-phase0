"""
Question bank — Phase 0 starter (10 CMS-style Champagne questions).

Phase 1 expands to 100+ across Champagne / Burgundy / Bordeaux / Loire / Rhône.

Schema:
  topic        — coarse category (used by weakness_tracker)
  question     — natural language
  expected     — canonical answer (short — for exact/normalised match)
  expected_kind — 'numeric_range' | 'enum' | 'set' | 'short_text'
  tags         — for filtering subsets
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Question:
    id: str
    topic: str
    question: str
    expected: str
    expected_kind: str = "short_text"
    tags: list[str] = field(default_factory=list)


# Phase 0 baseline — 10 questions. Real bank loaded from JSON at Batch-3-deploy.
PHASE_0_QUESTIONS: list[Question] = [
    Question(
        id="ch-001", topic="champagne.dosage",
        question="What is the dosage range (g/L) for Brut Nature Champagne?",
        expected="0-3 g/L", expected_kind="numeric_range",
        tags=["champagne", "dosage", "regulations"],
    ),
    Question(
        id="ch-002", topic="champagne.dosage",
        question="What is the dosage range (g/L) for Extra Brut Champagne?",
        expected="0-6 g/L", expected_kind="numeric_range",
        tags=["champagne", "dosage", "regulations"],
    ),
    Question(
        id="ch-003", topic="champagne.dosage",
        question="What is the dosage range (g/L) for Brut Champagne?",
        expected="0-12 g/L", expected_kind="numeric_range",
        tags=["champagne", "dosage", "regulations"],
    ),
    Question(
        id="ch-004", topic="champagne.aging",
        question="Minimum total aging (months) for non-vintage Champagne?",
        expected="15", expected_kind="short_text",
        tags=["champagne", "aging", "regulations"],
    ),
    Question(
        id="ch-005", topic="champagne.aging",
        question="Minimum total aging (months) for vintage Champagne?",
        expected="36", expected_kind="short_text",
        tags=["champagne", "aging", "regulations"],
    ),
    Question(
        id="ch-006", topic="champagne.grapes",
        question="Name the three principal grape varieties used in Champagne.",
        expected="Chardonnay, Pinot Noir, Pinot Meunier",
        expected_kind="set",
        tags=["champagne", "varieties"],
    ),
    Question(
        id="ch-007", topic="champagne.grapes",
        question="List the four 'forgotten' permitted varieties in Champagne.",
        expected="Pinot Blanc, Pinot Gris (Fromenteau), Arbane, Petit Meslier",
        expected_kind="set",
        tags=["champagne", "varieties"],
    ),
    Question(
        id="ch-008", topic="champagne.geography",
        question="Name the five main subregions of Champagne.",
        expected="Montagne de Reims, Vallée de la Marne, Côte des Blancs, Côte de Sézanne, Côte des Bar",
        expected_kind="set",
        tags=["champagne", "geography"],
    ),
    Question(
        id="ch-009", topic="champagne.method",
        question="What is the maximum pressure (atm) for liqueur de tirage during second fermentation?",
        expected="6 atm", expected_kind="short_text",
        tags=["champagne", "method"],
    ),
    Question(
        id="ch-010", topic="champagne.method",
        question="Term for the bottle position adjustment during riddling?",
        expected="remuage", expected_kind="enum",
        tags=["champagne", "method", "vocabulary"],
    ),
]


def load_questions(path: Optional[str | Path] = None) -> list[Question]:
    """Load from JSON if path given, otherwise return baseline."""
    if path is None:
        return list(PHASE_0_QUESTIONS)
    raw = json.loads(Path(path).read_text())
    return [Question(**r) for r in raw]


def dump_questions(questions: list[Question], path: str | Path) -> None:
    Path(path).write_text(json.dumps([asdict(q) for q in questions], indent=2))
