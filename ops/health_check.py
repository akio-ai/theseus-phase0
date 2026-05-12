"""
Health check — cron every 15min. Aggregates 7 health dimensions.

Engages kill switch + alerts Discord on CRITICAL.

Checks:
  1. Kill switch state (if engaged, surface reason)
  2. DB reachable
  3. Backups present + fresh (<48h)
  4. Disk usage <85%
  5. Conflict rate <5% (Phase 0 DoD)
  6. Cost month/day not breached
  7. Last crawler run age + outcome
"""
from __future__ import annotations

import json
import logging
import os
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger("theseus.health")


THESEUS_DIR = Path(os.environ.get("THESEUS_DIR", str(Path.home() / "Theseus_Phase0")))
BACKUP_DIR = THESEUS_DIR / "backups"
LAST_RUN_PATH = Path(os.environ.get("THESEUS_LAST_RUN", str(THESEUS_DIR / "ops" / "last_run.json")))


def _check_kill_switch() -> dict:
    from control.kill_switch import is_killed, last_engagement
    if is_killed():
        rec = last_engagement() or {}
        return {"status": "killed", "level": "WARN",  # killed != health critical (intentional state)
                "reason": rec.get("reason"), "actor": rec.get("actor"), "note": rec.get("note")}
    return {"status": "running", "level": "OK"}


def _check_db() -> dict:
    try:
        from core.db.connection import get_connection
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM v_health")
                row = cur.fetchone()
        return {"status": "ok", "level": "OK", "data": dict(row) if row else {}}
    except Exception as e:
        return {"status": "unreachable", "level": "CRITICAL", "error": str(e)}


def _check_backups() -> dict:
    if not BACKUP_DIR.exists():
        return {"status": "no_backup_dir", "level": "CRITICAL"}
    dumps = sorted(BACKUP_DIR.glob("theseus-*.dump"))
    if not dumps:
        return {"status": "no_dumps", "level": "CRITICAL"}
    latest = dumps[-1]
    age_h = (datetime.now() - datetime.fromtimestamp(latest.stat().st_mtime)).total_seconds() / 3600
    level = "OK" if age_h < 48 else "CRITICAL"
    return {"status": "ok", "level": level, "latest": latest.name,
            "age_hours": round(age_h, 2), "count": len(dumps)}


def _check_disk() -> dict:
    total, used, free = shutil.disk_usage(str(THESEUS_DIR))
    pct = used / total
    level = "OK"
    if pct >= 0.85:
        level = "WARN"
    if pct >= 0.95:
        level = "CRITICAL"
    return {"status": "ok", "level": level,
            "used_pct": round(pct * 100, 1),
            "free_gb": round(free / 1e9, 2)}


def _check_conflict_rate() -> dict:
    try:
        from core.db.conflict_detect import conflict_rate
        rate = conflict_rate()
        level = "OK"
        if rate >= 0.05:
            level = "CRITICAL"   # Phase 0 DoD breach
        return {"status": "ok", "level": level, "rate": round(rate, 4)}
    except Exception as e:
        return {"status": "unknown", "level": "WARN", "error": str(e)}


def _check_cost() -> dict:
    try:
        from cost.budget_enforcer import status as budget_status
        s = budget_status()
        any_breach = any(v.breached for v in s.values())
        level = "CRITICAL" if any_breach else ("WARN" if s["hour"].pct >= 1.0 else "OK")
        return {
            "status": "ok",
            "level": level,
            "windows": {w: {"spent": v.spent_usd, "limit": v.limit_usd,
                             "breached": v.breached, "pct": round(v.pct, 3)}
                        for w, v in s.items()},
        }
    except Exception as e:
        return {"status": "unknown", "level": "WARN", "error": str(e)}


def _check_last_run() -> dict:
    if not LAST_RUN_PATH.exists():
        return {"status": "no_run", "level": "WARN"}
    try:
        payload = json.loads(LAST_RUN_PATH.read_text())
        end = payload.get("ended_at") or payload.get("started_at")
        age_h = None
        if end:
            ended = datetime.fromisoformat(end.replace("Z", "+00:00"))
            age_h = (datetime.now(timezone.utc) - ended).total_seconds() / 3600
        level = "OK"
        if age_h is not None and age_h > 26:  # 24h cron + 2h slack
            level = "WARN"
        if payload.get("stopped_reason"):
            level = "WARN"
        return {"status": "ok", "level": level,
                "age_hours": round(age_h, 2) if age_h is not None else None,
                "entries_upserted": payload.get("entries_upserted"),
                "errors": len(payload.get("errors", [])),
                "stopped_reason": payload.get("stopped_reason")}
    except Exception as e:
        return {"status": "unparseable", "level": "WARN", "error": str(e)}


def run_health() -> dict[str, Any]:
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "kill_switch":    _check_kill_switch(),
        "db":             _check_db(),
        "backups":        _check_backups(),
        "disk":           _check_disk(),
        "conflict_rate":  _check_conflict_rate(),
        "cost":           _check_cost(),
        "last_run":       _check_last_run(),
    }


def is_critical(report: dict) -> tuple[bool, list[str]]:
    crit = []
    for k, v in report.items():
        if isinstance(v, dict) and v.get("level") == "CRITICAL":
            crit.append(k)
    return (len(crit) > 0), crit


def main() -> int:
    logging.basicConfig(
        level=os.environ.get("THESEUS_LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    report = run_health()
    print(json.dumps(report, indent=2, default=str))

    critical, dims = is_critical(report)
    if critical:
        from control.kill_switch import KillReason, engage_kill, is_killed
        from briefing.discord_notify import NotifyChannel, notify
        msg = f"🚨 Theseus health CRITICAL: {', '.join(dims)}\n```json\n{json.dumps(report, default=str)[:1500]}\n```"
        notify(NotifyChannel.ALERTS, msg)
        if not is_killed():
            engage_kill(KillReason.HEALTH_CRITICAL, actor="ops.health_check",
                        note=f"critical dims: {dims}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
