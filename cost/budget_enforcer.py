"""
Budget enforcer — gap #3.

Thresholds (confirmed by Akio 2026-05-09):
  - soft hourly: $5/hr   → Discord warn only
  - hard daily:  $20/day → engage kill switch
  - monthly cap: $100/mo → engage kill switch (separate reason)

Soft warn does not stop work; hard caps engage kill_switch.engage_kill().

Env overrides (for testing / future adjustment):
  THESEUS_COST_SOFT_HOURLY_USD
  THESEUS_COST_HARD_DAILY_USD
  THESEUS_COST_MONTHLY_USD
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass

from control.kill_switch import KillReason, engage_kill, is_killed
from . import cost_db

logger = logging.getLogger("theseus.budget")


class BudgetExceeded(Exception):
    """Raised by guard() — typically caught + converted to kill_switch engagement."""


@dataclass
class WindowStatus:
    window: str
    spent_usd: float
    limit_usd: float
    breached: bool

    @property
    def pct(self) -> float:
        return (self.spent_usd / self.limit_usd) if self.limit_usd > 0 else 0.0


def _limits() -> dict[str, float]:
    return {
        "hour":  float(os.environ.get("THESEUS_COST_SOFT_HOURLY_USD", "5")),
        "day":   float(os.environ.get("THESEUS_COST_HARD_DAILY_USD", "20")),
        "month": float(os.environ.get("THESEUS_COST_MONTHLY_USD",   "100")),
    }


def status() -> dict[str, WindowStatus]:
    limits = _limits()
    out = {}
    for window, limit in limits.items():
        spent = cost_db.query_window(window)["usd"]
        out[window] = WindowStatus(window=window, spent_usd=spent, limit_usd=limit,
                                   breached=spent >= limit)
    return out


def check_budgets() -> dict[str, WindowStatus]:
    """
    Called after every LLM cost log. Engages kill switch on hard caps.
    Returns the status dict for callers (briefing, etc).
    """
    s = status()
    # Hourly: soft warn, do not kill
    if s["hour"].breached:
        logger.warning(
            "cost-soft-warn: hourly $%.2f / $%.2f (%.0f%%)",
            s["hour"].spent_usd, s["hour"].limit_usd, s["hour"].pct * 100,
        )
        # (Discord warn is sent by briefing/discord_notify when this status is shown.)

    # Daily: hard kill
    if s["day"].breached and not is_killed():
        engage_kill(
            KillReason.COST_HARD_CAP,
            actor="cost.budget_enforcer",
            note=f"daily spent ${s['day'].spent_usd:.2f} >= cap ${s['day'].limit_usd:.2f}",
        )
        logger.error("cost-hard-kill: daily $%.2f >= $%.2f — kill switch engaged",
                     s["day"].spent_usd, s["day"].limit_usd)

    # Monthly: hard kill (separate reason for post-mortem clarity)
    if s["month"].breached and not is_killed():
        engage_kill(
            KillReason.COST_MONTHLY_CAP,
            actor="cost.budget_enforcer",
            note=f"month spent ${s['month'].spent_usd:.2f} >= cap ${s['month'].limit_usd:.2f}",
        )
        logger.error("cost-monthly-kill: month $%.2f >= $%.2f — kill switch engaged",
                     s["month"].spent_usd, s["month"].limit_usd)

    return s


def guard() -> None:
    """Call before initiating a batch of LLM work; raises if already over."""
    s = status()
    if s["day"].breached:
        raise BudgetExceeded(
            f"daily cap reached: ${s['day'].spent_usd:.2f} >= ${s['day'].limit_usd:.2f}"
        )
    if s["month"].breached:
        raise BudgetExceeded(
            f"monthly cap reached: ${s['month'].spent_usd:.2f} >= ${s['month'].limit_usd:.2f}"
        )
