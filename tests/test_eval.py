"""
Eval harness skeleton tests — gap #5 wiring (Phase 0 doesn't require correct answers,
just that the harness runs end-to-end).
"""
from __future__ import annotations

from eval.accuracy_scorer import score_run
from eval.citation_validator import is_verified_citation, validate_citations
from eval.question_bank import PHASE_0_QUESTIONS, dump_questions, load_questions
from eval.theseus_qa import QAResult, answer_question, run_bank


def test_question_bank_phase0_size():
    qs = load_questions()
    assert len(qs) == 10
    assert all(q.topic.startswith("champagne.") for q in qs)


def test_question_bank_round_trip(tmp_path):
    p = tmp_path / "questions.json"
    dump_questions(PHASE_0_QUESTIONS, p)
    loaded = load_questions(p)
    assert len(loaded) == len(PHASE_0_QUESTIONS)
    assert loaded[0].id == PHASE_0_QUESTIONS[0].id


def test_default_answerer_returns_skeleton_marker():
    q = PHASE_0_QUESTIONS[0]
    r = answer_question(q)
    assert isinstance(r, QAResult)
    assert "SKELETON" in r.answer


def test_run_bank_returns_one_per_question():
    qs = load_questions()
    results = run_bank(qs)
    assert len(results) == len(qs)
    assert {r.question_id for r in results} == {q.id for q in qs}


def test_skeleton_run_fails_phase1_gate():
    qs = load_questions()
    results = run_bank(qs)
    score = score_run(qs, results)
    assert score.total == 10
    assert score.correct == 0
    assert not score.pass_phase1


def test_is_verified_citation_clean_source():
    assert is_verified_citation("https://www.champagne.fr/some/page") is True
    assert is_verified_citation("https://wikidata.org/entity/Q123") is True


def test_is_verified_citation_denied_host():
    assert is_verified_citation("https://www.robertparker.com/x") is False
    assert is_verified_citation("https://random-blog.example.com/y") is False


def test_validate_citations_aggregates():
    results = [
        QAResult(question_id="q1", answer="x",
                 citations=["https://www.champagne.fr/a"]),
        QAResult(question_id="q2", answer="y",
                 citations=["https://random-blog.example.com/b"]),
        QAResult(question_id="q3", answer="z", citations=[]),
    ]
    rep = validate_citations(results)
    assert rep["total"] == 3
    assert rep["with_citation"] == 2
    assert rep["with_verified_citation"] == 1
    assert rep["verified_rate"] == round(1 / 3, 3)
    assert len(rep["violations"]) == 1


def test_correct_answer_path():
    """Provide an answerer that returns the canonical expected text; should pass."""
    qs = load_questions()

    def perfect(q):
        return QAResult(question_id=q.id, answer=q.expected,
                        citations=["https://www.champagne.fr/regs"],
                        confidence=0.9)

    results = run_bank(qs, answerer=perfect)
    score = score_run(qs, results)
    assert score.correct == len(qs)
    assert score.accuracy == 1.0
    # All cited from clean source → pass_phase1 should be True
    assert score.pass_phase1 is True
