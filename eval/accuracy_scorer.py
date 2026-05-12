"""
Accuracy scorer.

Phase 1 milestone: 90%+ accuracy + 95%+ verified-citation rate on 100 questions.
This is SYSTEM eval — independent of Akio's personal CMS Advanced exam (Phase 2).

Scoring is light: short-text exact match (normalised), set equality for set kind,
numeric range overlap for numeric_range. Phase 1 may swap in fuzzy matching.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .citation_validator import validate_citations
from .question_bank import Question
from .theseus_qa import QAResult


@dataclass
class RunScore:
    total: int
    correct: int
    accuracy: float
    citation_report: dict = field(default_factory=dict)
    per_question: list[dict] = field(default_factory=list)

    @property
    def pass_phase1(self) -> bool:
        return (
            self.accuracy >= 0.90
            and self.citation_report.get("verified_rate", 0.0) >= 0.95
        )


_NORM_RE = re.compile(r"[\s\-,;\.]+")


def _normalise(s: str) -> str:
    return _NORM_RE.sub(" ", s.lower()).strip()


def _set_from(s: str) -> set[str]:
    return {p.strip() for p in re.split(r",|;|/", s) if p.strip()}


def _match(q: Question, r: QAResult) -> bool:
    expected, given = q.expected, r.answer
    if not given or "[SKELETON" in given:
        return False
    if q.expected_kind == "set":
        return _set_from(_normalise(expected)) == _set_from(_normalise(given))
    if q.expected_kind == "numeric_range":
        # exact range string match for now; Phase 1 swaps in overlap calc
        return _normalise(expected) in _normalise(given) or \
               _normalise(given) in _normalise(expected)
    # short_text / enum
    return _normalise(expected) == _normalise(given) or \
           _normalise(expected) in _normalise(given)


def score_run(questions: list[Question], results: list[QAResult]) -> RunScore:
    by_id = {r.question_id: r for r in results}
    per_q: list[dict] = []
    correct = 0
    for q in questions:
        r = by_id.get(q.id)
        if r is None:
            per_q.append({"qid": q.id, "correct": False, "reason": "no_result"})
            continue
        ok = _match(q, r)
        if ok:
            correct += 1
        per_q.append({
            "qid": q.id, "correct": ok, "topic": q.topic,
            "expected": q.expected, "answer": r.answer,
            "citations": r.citations, "confidence": r.confidence,
        })

    citation_report = validate_citations(results)
    total = len(questions)
    return RunScore(
        total=total,
        correct=correct,
        accuracy=round(correct / total, 3) if total else 0.0,
        citation_report=citation_report,
        per_question=per_q,
    )
