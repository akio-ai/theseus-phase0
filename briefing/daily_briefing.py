"""
Daily Briefing — cron 07:00 NJT.

Composes a message to #theseus-briefing covering:
  - Yesterday's crawler run summary (entries +N, conflicts +M, errors)
  - Cost so far today/month + entries-per-USD throughput (Akio: "ML speed visible")
  - Akio's weak topics (last 30d) — what to revise today
  - Open entity flags (Theseus's self-acknowledged weak spots)
  - 3 CMS-style questions to drill (auto-picked from weak topics)
  - Budget status with traffic-light icons
"""
from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from cost.budget_enforcer import status as budget_status
from cost.cost_db import query_window
from .discord_notify import NotifyChannel, notify
from .weakness_tracker import top_weaknesses

logger = logging.getLogger("theseus.briefing")


SUMMARY_PATH = Path(os.environ.get(
    "THESEUS_LAST_RUN",
    str(Path.home() / "Theseus_Phase0" / "ops" / "last_run.json"),
))


def _emoji(breached: bool, soft_warn: bool = False) -> str:
    if breached:
        return "🔴"
    if soft_warn:
        return "🟡"
    return "🟢"


def _entities_today() -> int:
    """Count entities created in last 24h. Returns 0 if DB unavailable."""
    try:
        from core.db.connection import get_connection
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) AS n FROM entities WHERE created_at >= NOW() - INTERVAL '24 hours'"
                )
                return cur.fetchone()["n"]
    except Exception as e:
        logger.warning("entity count failed: %s", e)
        return 0


def _format_throughput(entries_today: int, usd_today: float) -> str:
    if usd_today <= 0:
        return f"{entries_today} entries today (no LLM cost yet)"
    rate = entries_today / usd_today
    return f"{entries_today} entries today / ${usd_today:.2f} = {rate:.1f} entries per USD"


def compose_briefing(*, today: datetime | None = None) -> str:
    today = today or datetime.now(timezone.utc).astimezone()
    bs = budget_status()
    cost_today = bs["day"].spent_usd
    cost_month = bs["month"].spent_usd

    last_run: dict = {}
    if SUMMARY_PATH.exists():
        try:
            last_run = json.loads(SUMMARY_PATH.read_text())
        except Exception as e:
            logger.warning("last_run parse failed: %s", e)

    entries_today = _entities_today()
    weak = top_weaknesses(limit=5)

    lines = []
    lines.append(f"**Theseus Daily Briefing — {today.strftime('%Y-%m-%d (%a)')}**")
    lines.append("")
    # ── Crawler run ──
    if last_run:
        lines.append(
            f"📦 Last crawler run: "
            f"{last_run.get('entries_upserted', 0)} upserted "
            f"({last_run.get('entries_conflicted', 0)} conflicted, "
            f"{len(last_run.get('errors', []))} errors)"
        )
        if last_run.get("stopped_reason"):
            lines.append(f"⚠️ Stopped: `{last_run['stopped_reason']}`")
    else:
        lines.append("📦 No previous crawler run summary found.")

    # ── Throughput (Akio's ML speed visibility) ──
    lines.append(f"⚡ {_format_throughput(entries_today, cost_today)}")

    # ── Cost / budget ──
    lines.append(
        f"💰 Cost: "
        f"{_emoji(bs['day'].breached, bs['hour'].breached)} day ${cost_today:.2f}/${bs['day'].limit_usd:.0f} · "
        f"{_emoji(bs['month'].breached)} month ${cost_month:.2f}/${bs['month'].limit_usd:.0f}"
    )

    # ── Akio's weak topics ──
    if weak["akio_weak_topics"]:
        lines.append("")
        lines.append("🎯 **Your weak topics (last 30d)** — revise these:")
        for t in weak["akio_weak_topics"]:
            lines.append(f"  • {t['topic']}: {int(t['wrong_n'])}/{t['total']} wrong "
                         f"({t['wrong_rate']*100:.0f}%)")

    # ── Theseus's open flags ──
    if weak["open_entity_flags"]:
        lines.append("")
        lines.append("🔎 **Entities you flagged as suspect** — Theseus is re-verifying:")
        for f in weak["open_entity_flags"]:
            lines.append(f"  • `{f['entity_id']}` — {f['reason']}")

    if not weak["akio_weak_topics"] and not weak["open_entity_flags"]:
        lines.append("")
        lines.append("✨ No active weaknesses logged — co-learning loop quiet for now.")

    return "\n".join(lines)


def main() -> int:
    logging.basicConfig(
        level=os.environ.get("THESEUS_LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    msg = compose_briefing()
    result = notify(NotifyChannel.BRIEFING, msg)
    print(json.dumps({"briefing": msg, "notify_result": result}, indent=2))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
