"""
Discord webhook notifier. 3 channels (Akio creates webhooks in Batch 3 deploy):
  - briefing  → daily summary
  - alerts    → kill switch, ethical violations, cost soft-warn
  - b2b_leads → funnel-detected sales signals (Batch 3 funnel module)
"""
from __future__ import annotations

import logging
import os
from enum import StrEnum
from typing import Optional

import httpx

logger = logging.getLogger("theseus.discord")


class NotifyChannel(StrEnum):
    BRIEFING = "briefing"
    ALERTS = "alerts"
    B2B_LEADS = "b2b_leads"


def _webhook(channel: NotifyChannel) -> Optional[str]:
    key = {
        NotifyChannel.BRIEFING:  "DISCORD_WEBHOOK_BRIEFING",
        NotifyChannel.ALERTS:    "DISCORD_WEBHOOK_ALERTS",
        NotifyChannel.B2B_LEADS: "DISCORD_WEBHOOK_B2B_LEADS",
    }[channel]
    url = os.environ.get(key, "")
    if not url or url.startswith("PLACEHOLDER"):
        return None
    return url


def notify(channel: NotifyChannel, content: str, *, dry_run: bool = False) -> dict:
    """
    Send a message to a Discord channel.
    Returns: {"sent": bool, "reason": str | None}
    If webhook env var is unset/placeholder → returns {"sent": False, "reason": "no_webhook"}
    so cron jobs don't fail in pre-deploy state.
    """
    url = _webhook(channel)
    if dry_run or url is None:
        logger.info("notify[%s] dry/no-webhook: %s", channel.value, content[:200])
        return {"sent": False, "reason": "dry_run" if dry_run else "no_webhook"}

    payload = {"content": content[:2000]}  # Discord 2000-char limit
    try:
        with httpx.Client(timeout=10.0) as client:
            r = client.post(url, json=payload)
            r.raise_for_status()
        return {"sent": True, "reason": None}
    except Exception as e:
        logger.error("discord notify failed for %s: %s", channel.value, e)
        return {"sent": False, "reason": str(e)}
