"""
Eval Harness skeleton — gap #5.

Phase 0 = 10 sample questions, runs end-to-end.
Phase 1 = expand to 100, achieve 90%+ accuracy + 95%+ verified-citation to mark
          Phase 1 complete. This is SYSTEM eval, independent of Akio's personal
          CMS Advanced exam (which is a Phase 2 marker, not a gate).
"""
from .question_bank import load_questions, Question
from .theseus_qa import answer_question, QAResult
from .citation_validator import validate_citations
from .accuracy_scorer import score_run, RunScore

__all__ = ["load_questions", "Question",
           "answer_question", "QAResult",
           "validate_citations", "score_run", "RunScore"]
