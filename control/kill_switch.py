"""
Central Kill Switch — gap #1.

All long-running components (crawler, orchestrator, briefing, anki, llm callers)
MUST poll `is_killed()` at:
  - startup (refuse to run)
  - top of each work loop iteration
  - before any external API call

The kill flag is a file (`THESEUS_KILL_FILE`, default `~/Theseus_Phase0/control/.killed`).
File-based so any subprocess / cron / shell can engage without needing the running
process. Clear via `clear_kill()` or `rm` the file.

Triggers (auto-engagement from other modules):
  - crawler/ethical_guardrails.EthicalViolation
  - cost/budget_enforcer over hard threshold
  - core/db/conflict_detect rate > 5%
  - ops/health_check critical failures

Engagement writes a JSON record (reason, actor, ts) so post-mortem is possible.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Optional


class KillReason(StrEnum):
    MANUAL = "manual"                      # `python -m control.emergency_stop`
    ETHICAL_VIOLATION = "ethical_violation"
    COST_HARD_CAP = "cost_hard_cap"
    COST_MONTHLY_CAP = "cost_monthly_cap"
    CONFLICT_RATE_EXCEEDED = "conflict_rate_exceeded"
    HEALTH_CRITICAL = "health_critical"
    UNKNOWN = "unknown"


def _kill_file_path() -> Path:
    return Path(os.environ.get(
        "THESEUS_KILL_FILE",
        str(Path.home() / "Theseus_Phase0" / "control" / ".killed"),
    ))


def is_killed() -> bool:
    return _kill_file_path().exists()


def engage_kill(reason: KillReason, actor: str, note: str = "") -> Path:
    """
    Engage the kill switch. Returns the path of the kill file written.
    Idempotent: if already engaged, appends a new record to the file
    (newline-delimited JSON).
    """
    path = _kill_file_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "reason": reason.value,
        "actor": actor,
        "note": note,
        "ts": datetime.now(timezone.utc).isoformat(),
    }
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    return path


def clear_kill() -> Optional[Path]:
    """
    Clear the kill switch. Returns the path that was removed (or None if not engaged).
    NOTE: clearing does NOT erase audit history (audit_log table is unaffected).
    Use only after the underlying cause has been investigated + resolved.
    """
    path = _kill_file_path()
    if not path.exists():
        return None
    # Move to archive instead of delete, for post-mortem
    archive = path.with_suffix(f".cleared_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}")
    path.rename(archive)
    return archive


def last_engagement() -> Optional[dict]:
    """Return the most recent engagement record (or None if not engaged)."""
    path = _kill_file_path()
    if not path.exists():
        return None
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if not lines:
        return None
    return json.loads(lines[-1])
