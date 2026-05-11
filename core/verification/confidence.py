"""
Confidence calculation from source tier set + conflict count.

Heuristic v0 (Phase 0 — refined empirically in Phase 1):
- Each tier contributes a weight; sum, then saturate to [0, 1]
- Conflicts penalize multiplicatively
- DoD: ≥3 sources required to exceed 0.7 confidence

Tier weights (intentionally biased toward Tier 1-2 official sources):
    government     → 0.45
    regional       → 0.40
    producer       → 0.25
    public_data    → 0.20
    akios_notes    → 0.35  (human-curated, differentiation asset)
    licensed       → 0.40

Per-source diminishing returns: same tier counted twice = 1.5x first weight, not 2x.
"""
from __future__ import annotations

from collections import Counter
from typing import Iterable

TIER_WEIGHTS: dict[str, float] = {
    "government":  0.45,
    "regional":    0.40,
    "producer":    0.25,
    "public_data": 0.20,
    "akios_notes": 0.35,
    "licensed":    0.40,
}


def compute_confidence(tiers: Iterable[str], num_conflicts: int = 0) -> float:
    counts = Counter(tiers)
    raw = 0.0
    for tier, n in counts.items():
        w = TIER_WEIGHTS.get(tier, 0.0)
        # Diminishing returns: 1st = 1.0x, 2nd = 0.5x, 3rd = 0.25x ...
        for i in range(n):
            raw += w * (0.5 ** i)
    # Conflict penalty: each open conflict shaves 15%, floored to 0
    penalty = max(0.0, 1.0 - 0.15 * num_conflicts)
    score = min(1.0, raw) * penalty
    return round(score, 3)
