"""
Theseus QA — answer eval questions via the live system (DB + LLM).

Phase 0 returns a `QAResult` even if the underlying answerer is mocked. The
harness runs end-to-end on 10 sample questions to confirm wiring; the answers
themselves are not graded for accuracy in Phase 0 (skeleton).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Protocol

from .question_bank import Question


@dataclass
class QAResult:
    question_id: str
    answer: str
    citations: list[str] = field(default_factory=list)   # URLs from source_refs
    confidence: float = 0.0
    notes: str = ""


class Answerer(Protocol):
    def __call__(self, q: Question) -> QAResult: ...


def _default_answerer(q: Question) -> QAResult:
    """
    Phase 0 stub. In Batch 3 deploy this gets replaced with a real implementation
    that:
      1. Uses pgvector to find candidate entities matching the question
      2. Asks Claude to compose an answer using only those entities' facts
      3. Returns the cited source URLs

    Today: returns a sentinel that says the skeleton is wired but not answering.
    """
    return QAResult(
        question_id=q.id,
        answer="[SKELETON — not yet answering; Batch 3 deploy wires up vector + LLM]",
        citations=[],
        confidence=0.0,
        notes="phase0_skeleton",
    )


def answer_question(q: Question, *, answerer: Optional[Answerer] = None) -> QAResult:
    fn = answerer or _default_answerer
    return fn(q)


def run_bank(questions: list[Question],
             *, answerer: Optional[Answerer] = None) -> list[QAResult]:
    return [answer_question(q, answerer=answerer) for q in questions]
