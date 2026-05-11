"""
Ethical Guardrails — hard enforcement of Option A+ clean scope.

Every fetch must pass through `assert_allowed(url)`. Violations raise EthicalViolation,
which fetcher.py catches → logs to Discord + sets kill switch.

Phase 0 rules (compass + section §4 of T#1 v3):
- robots.txt obeyed
- Only allow-listed hosts (crawler/config.CLEAN_SOURCES)
- No login-required sites
- No paywall bypass / CAPTCHA / residential proxy
- User-Agent honest
- Rate limit per host (producer = 5s+, others = 1s+)
- Raw text NOT stored (only structured facts + SHA256 excerpt_hash)
- Critic scores (WA/WS/Decanter etc.) banned (config.DENIED_HOSTS)
"""
from __future__ import annotations

import hashlib
import logging
import time
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

from .config import CLEAN_SOURCES, USER_AGENT, is_denied, lookup

logger = logging.getLogger("theseus.guardrails")


class EthicalViolation(Exception):
    """Raised when a fetch attempt violates Phase 0 ethical scope."""


@dataclass
class _RateState:
    last_fetch: float = 0.0
    robots_cache: dict[str, RobotFileParser] = field(default_factory=dict)


_STATE = _RateState()
_HOST_LAST_FETCH: dict[str, float] = {}


def _host(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def assert_allowed(url: str) -> None:
    """
    Hard gate before any HTTP fetch.
    Raises EthicalViolation if any rule fails.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise EthicalViolation(f"non-http scheme: {url}")

    host = parsed.hostname or ""
    if not host:
        raise EthicalViolation(f"missing host: {url}")

    if is_denied(host):
        raise EthicalViolation(f"denied host (critic-score policy): {host}")

    src = lookup(host)
    if src is None:
        raise EthicalViolation(
            f"host not in CLEAN_SOURCES allow-list: {host} "
            f"(to add, register in crawler/config.py with Tier + license)"
        )

    # robots.txt check (cached per host)
    rp = _STATE.robots_cache.get(host)
    if rp is None:
        rp = RobotFileParser()
        rp.set_url(f"{parsed.scheme}://{host}/robots.txt")
        try:
            rp.read()
        except Exception as e:
            # If robots is unreachable, treat as DISALLOW (fail-closed)
            raise EthicalViolation(f"robots.txt unreachable for {host}: {e}") from e
        _STATE.robots_cache[host] = rp

    if not rp.can_fetch(USER_AGENT, url):
        raise EthicalViolation(f"robots.txt disallows: {url}")

    # Rate limit (per host)
    now = time.time()
    last = _HOST_LAST_FETCH.get(host, 0.0)
    elapsed = now - last
    if elapsed < src.min_delay_seconds:
        wait = src.min_delay_seconds - elapsed
        logger.debug("rate-limit sleep %.2fs for %s", wait, host)
        time.sleep(wait)
    _HOST_LAST_FETCH[host] = time.time()


def excerpt_hash(text: str) -> str:
    """SHA256 of an excerpt — for re-verification without storing raw text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def assert_no_raw_text_storage(payload: dict) -> None:
    """
    Sanity check before passing to upsert — payload should be structured facts,
    not raw HTML / scraped text blobs.
    Any string field > 2000 chars is flagged.
    """
    def _walk(obj, path="$"):
        if isinstance(obj, dict):
            for k, v in obj.items():
                _walk(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                _walk(v, f"{path}[{i}]")
        elif isinstance(obj, str) and len(obj) > 2000:
            raise EthicalViolation(
                f"raw-text-like string at {path} (len={len(obj)}); "
                f"only structured facts + excerpt_hash may be stored"
            )
    _walk(payload)


def tier_for_url(url: str) -> Optional["SourceTier"]:  # type: ignore[name-defined]
    from core.schema.entities import SourceTier
    src = lookup(_host(url))
    return src.tier if src else None
