"""
Daily orchestrator. Cron: 0 2 * * * (02:00 NJT).

Workflow:
  1. Pre-flight: kill switch off? budget under cap? DB reachable?
  2. For each extractor: pull tuples → LLM structurer → upsert
  3. On EthicalViolation / KillSwitchTripped / BudgetExceeded → graceful stop
  4. Write run summary (entries +N, conflicts +M, USD $X.YY, errors [...])
  5. Stash summary at ops/last_run.json for the morning briefing

This is intentionally simple: serial extractors, no async. Phase 1 may
parallelize once the throughput floor is established.
"""
from __future__ import annotations

import json
import logging
import os
import sys
import traceback
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from control.kill_switch import is_killed, KillReason, engage_kill
from cost.budget_enforcer import BudgetExceeded, status as budget_status, guard
from cost.cost_db import query_window
from core.db.conflict_detect import open_conflict_count
from crawler.ethical_guardrails import EthicalViolation
from crawler.extractors import civc, inao_fr, producer_websites, wikidata
from llm.structurer import structure_entity

logger = logging.getLogger("theseus.orchestrator")


@dataclass
class RunSummary:
    started_at: str
    ended_at: str = ""
    entries_attempted: int = 0
    entries_upserted: int = 0
    entries_conflicted: int = 0
    cost_usd_start: float = 0.0
    cost_usd_end: float = 0.0
    errors: list[dict] = field(default_factory=list)
    stopped_reason: str = ""

    @property
    def cost_delta_usd(self) -> float:
        return round(self.cost_usd_end - self.cost_usd_start, 4)

    def to_dict(self) -> dict[str, Any]:
        return {
            **self.__dict__,
            "cost_delta_usd": self.cost_delta_usd,
            "open_conflicts": None,  # filled in by finalize()
        }


SUMMARY_PATH = Path(os.environ.get(
    "THESEUS_LAST_RUN",
    str(Path.home() / "Theseus_Phase0" / "ops" / "last_run.json"),
))


def _pg_available() -> bool:
    try:
        from core.db.connection import get_connection
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
        return True
    except Exception as e:
        logger.warning("PG pre-flight failed: %s", e)
        return False


def _process_one(summary: RunSummary, kind: str, url: str, excerpt: str,
                 tier, license_) -> None:
    summary.entries_attempted += 1
    try:
        entity = structure_entity(
            entity_kind=kind, source_url=url, excerpt=excerpt,
            source_tier=tier, license=license_,
        )
        from core.db.upsert import upsert_entity
        result = upsert_entity(entity, actor=f"crawler.{kind}")
        summary.entries_upserted += 1
        if result["conflicts"]:
            summary.entries_conflicted += 1
    except EthicalViolation as e:
        engage_kill(KillReason.ETHICAL_VIOLATION, actor="orchestrator", note=str(e))
        summary.errors.append({"kind": "EthicalViolation", "url": url, "msg": str(e)})
        summary.stopped_reason = "ethical_violation"
        raise
    except BudgetExceeded as e:
        summary.errors.append({"kind": "BudgetExceeded", "msg": str(e)})
        summary.stopped_reason = "budget_exceeded"
        raise
    except Exception as e:
        summary.errors.append({
            "kind": e.__class__.__name__,
            "url": url,
            "msg": str(e),
            "tb": traceback.format_exc(limit=3),
        })


def run() -> RunSummary:
    summary = RunSummary(started_at=datetime.now(timezone.utc).isoformat())
    summary.cost_usd_start = query_window("day")["usd"]

    if is_killed():
        summary.stopped_reason = "kill_switch_engaged"
        return _finalize(summary)

    try:
        guard()
    except BudgetExceeded as e:
        summary.stopped_reason = f"budget: {e}"
        return _finalize(summary)

    if not _pg_available():
        summary.stopped_reason = "pg_unavailable"
        return _finalize(summary)

    # Wikidata first (no LLM cost — pure SPARQL)
    try:
        from core.db.upsert import upsert_entity
        for entity in wikidata.iter_producers():
            if is_killed():
                summary.stopped_reason = "kill_switch_during_wikidata"
                break
            summary.entries_attempted += 1
            try:
                result = upsert_entity(entity, actor="crawler.wikidata")
                summary.entries_upserted += 1
                if result["conflicts"]:
                    summary.entries_conflicted += 1
            except Exception as e:
                summary.errors.append({"kind": e.__class__.__name__, "id": entity.id,
                                       "msg": str(e)})
    except Exception as e:
        summary.errors.append({"kind": "WikidataFailure", "msg": str(e),
                               "tb": traceback.format_exc(limit=3)})

    # Then LLM-backed extractors
    extractors = [
        ("civc", civc.iter_extracts),
        ("inao_fr", inao_fr.iter_extracts),
        ("producer_websites", producer_websites.iter_extracts),
    ]
    for ext_name, ext_iter in extractors:
        if is_killed():
            break
        try:
            for kind, url, excerpt, tier, license_ in ext_iter():
                if is_killed():
                    break
                try:
                    _process_one(summary, kind, url, excerpt, tier, license_)
                except (EthicalViolation, BudgetExceeded):
                    break
        except Exception as e:
            summary.errors.append({"kind": f"{ext_name}.iter_failure",
                                   "msg": str(e),
                                   "tb": traceback.format_exc(limit=3)})

    return _finalize(summary)


def _finalize(summary: RunSummary) -> RunSummary:
    summary.ended_at = datetime.now(timezone.utc).isoformat()
    summary.cost_usd_end = query_window("day")["usd"]
    payload = summary.to_dict()
    try:
        payload["open_conflicts"] = open_conflict_count()
    except Exception:
        pass
    payload["budget_status"] = {
        w: {"spent_usd": s.spent_usd, "limit_usd": s.limit_usd, "breached": s.breached}
        for w, s in budget_status().items()
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(payload, indent=2, default=str))
    return summary


def main() -> int:
    logging.basicConfig(
        level=os.environ.get("THESEUS_LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    summary = run()
    print(json.dumps(summary.to_dict(), indent=2, default=str))
    return 0 if not summary.stopped_reason else 2


if __name__ == "__main__":
    sys.exit(main())
