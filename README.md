# Theseus Phase 0

Self-learning wine/champagne knowledge layer, Champagne-only proof of concept (3 months).

**Status**: Batch 1 (Foundation + Safety) — initial commit.

## What's in this repo (Batch 1)

```
core/
  schema/       entities, relations, JSON-LD context
  db/           PostgreSQL connection, migrations, upsert with provenance, conflict detection, pgvector search
  verification/ confidence scoring, source tracking
crawler/
  config.py             allow-listed clean sources (Option A+)
  ethical_guardrails.py robots.txt + rate limit + raw-text blocker + critic-host deny
  fetcher.py            HTTP client wrapping guardrails
control/        kill switch + emergency stop CLI (gap #1)
ops/            backup.sh (gap #2 — disaster guard)
tests/          isolation, kill switch, ethics, confidence
```

Coming in Batch 2: crawler extractors, LLM structurer, cost monitoring (gap #3), tenant layer, briefing, anki.

Coming in Batch 3: style engine, funnel instrumentation, eval harness (gap #5), restore.sh, health_check, full docs.

## Quick test (no DB needed for unit tests)

```bash
cd ~/Theseus_Phase0
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/test_isolation.py tests/test_kill_switch.py tests/test_crawler_ethics.py tests/test_confidence.py -v
```

## Kill switch usage

```bash
# Engage:
python -m control.emergency_stop stop --reason "manual investigation"

# Check:
python -m control.emergency_stop status

# Clear (after investigation):
python -m control.emergency_stop clear --confirm yes-clear-kill
```

The file `control/.killed` is the source of truth. Any subprocess or shell can
engage by simply `touch control/.killed`.

## Compass / privacy posture

- All public-facing entities use **institutional voice** (no individual sommelier name).
- Akio's personal notes live in the `private` layer (Tier 5) — not yet ingested in Batch 1.
- `tests/test_anki_layer_isolation.py` (Batch 3) enforces no private leakage to public outputs.
- Critic scores (Wine Advocate / Wine Spectator / Decanter etc.) are **banned** in `crawler/config.DENIED_HOSTS` and `SourceRef.__post_init__`.

## Win³ isolation

Theseus runs in its own PG instance, its own venv, its own cron set, its own
Discord webhooks, its own `.env`. `tests/test_isolation.py` enforces no cross-import.

## Cost budget (confirmed 2026-05-09)

- Soft warn:  $5/hour
- Hard kill:  $20/day
- Monthly cap: **$100/month**

Enforced in Batch 2 via `cost/budget_enforcer.py`.

## See also

- `T#1 v3` spec — the source-of-truth implementation prompt.
- `~/.claude/.../memory/project_theseus_compass.md` — design compass.
