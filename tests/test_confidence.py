"""
Confidence scoring — verification.confidence (T#1 v3 §10 DoD: ≥3 sources for high conf).
"""
from __future__ import annotations

from core.verification.confidence import compute_confidence


def test_zero_sources_zero_confidence():
    assert compute_confidence([]) == 0.0


def test_single_government_source_below_threshold():
    """Single source — even Tier 1 — should not exceed 0.5 alone."""
    assert compute_confidence(["government"]) <= 0.5


def test_three_sources_can_exceed_threshold():
    """3+ sources of mixed tiers should be able to reach ≥0.7."""
    c = compute_confidence(["government", "regional", "public_data"])
    assert c >= 0.7


def test_diminishing_returns_same_tier():
    """Two government sources < two distinct tier sources."""
    c_two_gov = compute_confidence(["government", "government"])
    c_gov_regional = compute_confidence(["government", "regional"])
    assert c_gov_regional > c_two_gov


def test_conflict_penalty_lowers_score():
    base = compute_confidence(["government", "regional", "producer"])
    penalized = compute_confidence(["government", "regional", "producer"], num_conflicts=2)
    assert penalized < base


def test_confidence_bounded_to_unit_interval():
    c = compute_confidence(["government"] * 10 + ["regional"] * 10)
    assert 0.0 <= c <= 1.0
