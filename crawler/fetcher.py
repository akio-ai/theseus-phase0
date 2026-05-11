"""
HTTP fetcher — wraps `httpx` with ethical_guardrails enforcement.

All crawler extractors MUST use this module. Direct `httpx.get()` from extractor
code is forbidden (caught by tests/test_crawler_ethics.py).
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

import httpx

from control.kill_switch import is_killed
from .config import USER_AGENT
from .ethical_guardrails import (
    EthicalViolation,
    assert_allowed,
    excerpt_hash as _excerpt_hash,
)

logger = logging.getLogger("theseus.fetcher")


@dataclass
class FetchResult:
    url: str
    status: int
    text: str
    fetched_at: datetime
    excerpt_hash: str
    content_type: str


class KillSwitchTripped(Exception):
    """Raised when fetch is attempted while kill switch is engaged."""


def fetch(url: str, *, timeout: float = 15.0) -> FetchResult:
    if is_killed():
        raise KillSwitchTripped("kill switch engaged — refusing fetch")

    assert_allowed(url)  # raises EthicalViolation if any rule fails

    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/json,*/*;q=0.5"}
    with httpx.Client(headers=headers, follow_redirects=True, timeout=timeout) as client:
        resp = client.get(url)

    text = resp.text
    return FetchResult(
        url=str(resp.url),
        status=resp.status_code,
        text=text,
        fetched_at=datetime.now(timezone.utc),
        excerpt_hash=_excerpt_hash(text[:4096]),  # hash of leading 4KB
        content_type=resp.headers.get("content-type", ""),
    )
