"""
Ethical guardrails — hard rule enforcement (T#1 v3 §4).
"""
from __future__ import annotations

import pytest

from crawler.config import CLEAN_SOURCES, DENIED_HOSTS, USER_AGENT, lookup, is_denied
from crawler.ethical_guardrails import (
    EthicalViolation, assert_no_raw_text_storage, excerpt_hash,
)


def test_user_agent_is_honest():
    """UA must identify Theseus + provide contact (no spoofing)."""
    assert "Theseus" in USER_AGENT
    assert "@" in USER_AGENT or "://" in USER_AGENT, "UA missing contact"


def test_denied_hosts_present():
    """Critic-score hosts must be in DENIED set (T#1 v3 §4.1)."""
    must_deny = {"robertparker.com", "winespectator.com", "decanter.com",
                 "vinous.com", "jamessuckling.com"}
    assert must_deny.issubset(DENIED_HOSTS)


def test_is_denied_matches_subdomain():
    assert is_denied("robertparker.com")
    assert is_denied("www.robertparker.com")
    assert is_denied("api.winespectator.com")
    assert not is_denied("champagne.fr")


def test_lookup_returns_clean_source():
    src = lookup("champagne.fr")
    assert src is not None
    assert src.host == "champagne.fr"


def test_lookup_subdomain():
    src = lookup("www.champagne.fr")
    assert src is not None


def test_lookup_unknown_host_returns_none():
    assert lookup("random-blog.example.com") is None


def test_source_ref_rejects_critic_host():
    from datetime import datetime, timezone
    from core.schema.entities import SourceRef, SourceTier
    with pytest.raises(ValueError, match="critic-score"):
        SourceRef(
            url="https://www.robertparker.com/some/review",
            tier=SourceTier.PUBLIC_DATA,
            license="quoted",
            fetched_at=datetime.now(timezone.utc),
        )


def test_excerpt_hash_deterministic():
    h1 = excerpt_hash("Krug Grande Cuvée 170ème Édition")
    h2 = excerpt_hash("Krug Grande Cuvée 170ème Édition")
    assert h1 == h2
    assert len(h1) == 64  # SHA256 hex


def test_no_raw_text_blocks_large_strings():
    payload = {"name": "X", "facts": {"notes": "x" * 3000}}
    with pytest.raises(EthicalViolation, match="raw-text-like"):
        assert_no_raw_text_storage(payload)


def test_no_raw_text_allows_normal_payload():
    payload = {
        "name": "Krug",
        "facts": {
            "founded_year": 1843,
            "house_style": "extended lees ageing, oxidative profile",
            "cepage": {"chardonnay": 0.45, "pinot_noir": 0.40, "pinot_meunier": 0.15},
        },
    }
    assert_no_raw_text_storage(payload)  # no raise


def test_clean_sources_have_tier_and_license():
    for src in CLEAN_SOURCES:
        assert src.host
        assert src.tier is not None
        assert src.license
        assert src.min_delay_seconds >= 1.0


# Note: assert_allowed() makes a real robots.txt fetch — skipped in unit tests.
# It's covered in integration tests at Batch 3 (tests/test_crawler_integration.py).
