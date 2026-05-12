"""
Citation validator.

A citation is "verified" when its host is in CLEAN_SOURCES (Tier 1-4).
Phase 1 completion criterion: 95%+ of QA results have at least one verified citation.
"""
from __future__ import annotations

from urllib.parse import urlparse

from crawler.config import lookup, is_denied
from .theseus_qa import QAResult


def is_verified_citation(url: str) -> bool:
    if not url:
        return False
    host = (urlparse(url).hostname or "").lower()
    if is_denied(host):
        return False
    return lookup(host) is not None


def validate_citations(results: list[QAResult]) -> dict:
    """
    Returns:
      {
        "total": int,
        "with_citation": int,
        "with_verified_citation": int,
        "verified_rate": float,           # of total
        "violations": [{"qid": ..., "bad_urls": [...]}],
      }
    """
    total = len(results)
    with_any = 0
    with_verified = 0
    violations: list[dict] = []
    for r in results:
        if r.citations:
            with_any += 1
            verified = [c for c in r.citations if is_verified_citation(c)]
            unverified = [c for c in r.citations if not is_verified_citation(c)]
            if verified:
                with_verified += 1
            if unverified:
                violations.append({"qid": r.question_id, "bad_urls": unverified})
    return {
        "total": total,
        "with_citation": with_any,
        "with_verified_citation": with_verified,
        "verified_rate": round(with_verified / total, 3) if total else 0.0,
        "violations": violations,
    }
