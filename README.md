# Theseus Phase 0

Self-learning wine/champagne knowledge layer, Champagne-only proof of concept (3 months).

**Status**: Batch 1+2+3 complete — ready for VPS deploy.

---

## What this is

Layer 1+2 of the Theseus architecture (`project_theseus_compass.md`):
- **Crawler** pulling from Tier 1-4 clean sources (Option A+ ethical scope)
- **PostgreSQL + pgvector** core with provenance, confidence, conflict detection
- **Co-learning loop**: Akio is taught while Theseus learns from his corrections
- **Safety nets**: kill switch, cost cap ($100/mo hard), backup/restore, conflict gate

Phase 0 deliberately does NOT do:
- Reasoning (Pairing Engine etc.) — Phase 2
- Tenant SaaS β — Phase 2
- Burgundy / Bordeaux / Sake — Phase 1
- Style Engine model training — Phase 2 (Phase 0 only logs the inputs)

See `T#1 v3` spec for the full scope.

---

## Repo layout

```
core/
  schema/              entities (Producer/Cuvee/Vineyard/Appellation/Vintage), relations, JSON-LD
  db/                  PG connection (isolation check), migrations, upsert w/ conflict detect, pgvector
  verification/        confidence scoring (tier-weighted), source tracking
crawler/
  config.py            CLEAN_SOURCES allow-list (Tier 1-4 only) + DENIED_HOSTS (critic scores)
  ethical_guardrails.py robots.txt + rate limit + raw-text blocker + critic deny
  fetcher.py           httpx wrapper, kill-switch gate
  extractors/          civc (T2), inao_fr (T1), producer_websites (T3 — explicit registry),
                       wikidata (T4 SPARQL, no LLM)
  orchestrator.py      daily 02:00 NJT cron entry
llm/                   claude_client (cost-wrapped), structurer (JSON-strict), prompts
cost/                  cost_db (SQLite), cost_tracker (@wrap), budget_enforcer (gap #3)
control/               kill_switch + emergency_stop CLI (gap #1)
ops/
  backup.sh            pg_dump custom format, 30-day rotation
  restore.sh           --dry-run / --execute, safety locked behind kill switch
  health_check.py      7-dim health, engages kill on CRITICAL, alerts Discord
tenant/                TenantConfig, obp_loader (compass validator), obp_inventory.json
briefing/              discord_notify (3 channels), weakness_tracker (bidirectional),
                       daily_briefing (07:00 NJT cron)
anki/                  card_generator, personal_version (all layers), staff_version (public only),
                       exporter (Anki .txt)
style_engine/          interaction_logger + PRIVATE_LAYER.md (Phase 2 training data, never商品化)
funnel/                lead_signals, invite_tracker, b2b_pipeline, usage_analytics
eval/                  question_bank (10 Champagne questions), theseus_qa, citation_validator,
                       accuracy_scorer (gap #5 — Phase 1 gate is independent of Akio CMS)
tests/                 75+ tests covering all of the above
.env.example           Akio fills in deploy. NEVER commit .env.
crontab.example        Cron entries for backup/orchestrator/briefing/health
requirements.txt       Python 3.11+ deps
```

---

## Compass posture (T#1 v3 §1, §8)

- All public-facing entities use **institutional voice**, NEVER an individual name.
- Personal patterns: `Akio` / `Matsumoto` / `松本昭生` are rejected in `obp_loader`,
  in `SourceRef` URL validation, in `staff_version` card output, and asserted in tests.
- `style_engine/` is the only place that captures Akio-specific interaction; its DB
  lives under `private/` (gitignored), every row carries `commercialization_ban = 1`.
- Critic scores (Robert Parker / Wine Spectator / Decanter / Vinous / James Suckling)
  are banned at three layers: `crawler/config.DENIED_HOSTS`, `SourceRef.__post_init__`
  (constructor reject), and citation validator.

---

## Co-learning loop

Akio teaches Theseus by correcting; Theseus teaches Akio by drilling weak spots.
Same DB, same daily briefing.

```
crawler → structurer → entity upsert → Daily Briefing (07:00 NJT) →
  Akio reads + Anki personal version + flags suspect entries →
    weakness_tracker (bidirectional SQLite):
      A) Akio wrong answers  → tomorrow's revision focus
      B) Entity flagged      → crawler re-verifies, confidence drops
    → loop
```

CMS Advanced 2027-02 = observation marker (not a gate). System Eval 90%+/95%
citation = Phase 1 completion (Theseus-level, independent of Akio).

---

## Safety nets

### Kill switch (gap #1)
File-based: `control/.killed`. Any subprocess or shell can engage by `touch`-ing
it. Every long-running module polls `is_killed()` at startup + each loop iteration.

```bash
# Engage:
python -m control.emergency_stop stop --reason "investigating CIVC drop"

# Check:
python -m control.emergency_stop status

# Clear (after fix):
python -m control.emergency_stop clear --confirm yes-clear-kill
```

Auto-engagement reasons: `ethical_violation` / `cost_hard_cap` / `cost_monthly_cap`
/ `conflict_rate_exceeded` / `health_critical` / `manual`.

### Backup / restore (gap #2)
- `ops/backup.sh` — daily 00:00 NJT, custom-format pg_dump, 30-day rotation
- `ops/restore.sh --dry-run` first, then `--execute`. Refuses to execute unless
  kill switch is engaged (forces conscious decision to halt crawler).

### Cost monitoring (gap #3)
Confirmed by Akio 2026-05-09:

| Window | Limit | Behaviour |
|---|---|---|
| Hour  | $5  | Discord warn (no halt) |
| Day   | $20 | Hard kill switch (`cost_hard_cap`) |
| Month | $100 | Hard kill switch (`cost_monthly_cap`) |

Enforced via `cost.cost_tracker.wrap(caller="...")` decorator. Direct
`anthropic.Anthropic().messages.create()` is forbidden — `tests/test_cost_monitoring.py`
checks that `llm.claude_client._call_messages` carries the decorator marker.

### Conflict guard
`core.db.conflict_detect.conflict_rate()` ≥ 5% → `ops/health_check.py` engages
kill switch (`conflict_rate_exceeded`). Phase 0 DoD is < 5%.

### Win³ isolation
- Separate venv, cron, `.env`, PG instance (port 5433 vs Win³'s 5432)
- `tests/test_isolation.py` enforces no `win3.*` import + PG port separation
- Discord webhooks separate (3 channels: `theseus-briefing` / `theseus-alerts` /
  `b2b-leads`)

---

## Deploy on VPS

```bash
# 1. Clone / rsync
rsync -av --exclude='__pycache__' --exclude='.git' --exclude='venv' \
    ~/Theseus_Phase0/ vps:/opt/theseus/
ssh vps

# 2. Python env
cd /opt/theseus
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. PostgreSQL — NEW instance on port 5433
sudo -u postgres createuser -P theseus      # set password, save it
sudo -u postgres createdb -O theseus theseus
sudo -u postgres psql -d theseus -c 'CREATE EXTENSION vector; CREATE EXTENSION pgcrypto; CREATE EXTENSION pg_trgm;'
psql -h 127.0.0.1 -p 5433 -U theseus -d theseus -f core/db/migrations/001_initial.sql

# 4. Discord — create 3 webhooks in your server:
#    #theseus-briefing  → DISCORD_WEBHOOK_BRIEFING
#    #theseus-alerts    → DISCORD_WEBHOOK_ALERTS
#    #b2b-leads         → DISCORD_WEBHOOK_B2B_LEADS

# 5. .env
cp .env.example .env
# Edit .env: set THESEUS_PG_PASSWORD, ANTHROPIC_API_KEY, DISCORD_WEBHOOK_*

# 6. Smoke tests
pytest tests/ -v        # expect 75+/75+ pass

# 7. Manual one-shot
python -m crawler.orchestrator     # writes ops/last_run.json
python -m briefing.daily_briefing  # sends to #theseus-briefing
python -m ops.health_check         # OK = exit 0, CRITICAL = exit 2

# 8. Cron
mkdir -p logs
crontab crontab.example
```

---

## Operational runbook

### Daily morning
1. Check `#theseus-briefing` — should land 07:00 NJT
2. Look at `entries_upserted`, `conflicted`, `errors`, `entries per USD`
3. Anki personal deck for revision (5-10 min)

### When alerts fire (#theseus-alerts)
| Alert | Action |
|---|---|
| `ethical_violation` | Inspect URL/host → if false positive, allowlist; if real, leave killed + escalate |
| `cost_hard_cap` | Check `cost/cost.db` for runaway caller → fix code → clear kill |
| `cost_monthly_cap` | Decide: raise monthly cap or pause until next month |
| `health_critical` | Read latest health_check output (logs/health.log) for failing dimension |
| `conflict_rate_exceeded` | Review `core/db/conflicts` table; resolve top items |

### Disaster recovery
```bash
python -m control.emergency_stop stop --reason "restoring DB"
ls backups/                                              # find latest
ops/restore.sh --dry-run backups/theseus-YYYYMMDDTHHMMSSZ.dump
ops/restore.sh --execute backups/theseus-YYYYMMDDTHHMMSSZ.dump
python -m control.emergency_stop clear --confirm yes-clear-kill
```

### Adding a producer to the crawler
1. Verify their robots.txt allows `TheseusBot/0.1`
2. Add a `CleanSource(host="X.com", tier=PRODUCER, license="producer_official", min_delay_seconds=5.0)` to `crawler/config.py`
3. Add a `ProducerSeed` in `crawler/extractors/producer_websites.py`
4. Run a manual `python -m crawler.orchestrator` and confirm no `EthicalViolation`

### Funnel data
- `funnel/funnel.db` — events, invites, b2b_flags
- Daily briefing surfaces `usage_summary` after Phase 0 wires it in
- B2B notifications dedup'd to 1 per user per 30 days

---

## Phase 0 completion checklist (DoD)

- [ ] Champagne entries ≥ 3,000
- [ ] All entries with ≥ 3 distinct sources
- [ ] Conflict-flag rate < 5%
- [ ] Zero ethical violations
- [ ] 14 consecutive daily briefings sent
- [ ] Anki cards ≥ 140 (both personal + staff variants)
- [ ] OBP inventory PoC: tenant filter returns sensible subset
- [ ] Win³ isolation: all `test_isolation` tests pass on VPS
- [ ] Funnel instrumentation operating (data may be 0 — wiring confirmed)
- [ ] Eval harness skeleton runs end-to-end on 10 questions
- [ ] Kill switch smoke-tested in production env
- [ ] Cost monitoring smoke-tested in production env
- [ ] Backup + restore --dry-run validated against a real dump

---

## Compass references

- `~/.claude/.../memory/project_theseus_compass.md` — design compass
- `~/.claude/.../memory/user_name_kanji.md` — privacy posture
- `~/.claude/.../memory/preference_sake_db_detail.md` — sake schema policy (Phase 1)
- `T#1 v3` spec (in conversation history of 2026-05-09 session)

## Cost / time provenance

- Cost cap confirmed by Akio: 2026-05-09 ($100/month)
- T#1 spec approved by Akio: 2026-05-09 (A path — sequential Batch 1→2→3)
- Build timeline: 2026-05-09, 3 batches, ~75+ tests passing
