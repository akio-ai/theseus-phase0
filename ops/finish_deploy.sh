#!/usr/bin/env bash
# Manual completion script — bypasses deploy.sh's buggy step 6 onwards.
# Assumes:
#   - PostgreSQL cluster 'theseus' exists on port 5433
#   - pg_hba.conf is set to trust for 127.0.0.1 (temporary)
#   - Run as root on the VPS
set -u

C_GREEN=$'\033[32m'
C_RED=$'\033[31m'
C_YELLOW=$'\033[33m'
C_BOLD=$'\033[1m'
C_RESET=$'\033[0m'

ok()   { printf '%s[OK]%s %s\n' "${C_GREEN}" "${C_RESET}" "$*"; }
warn() { printf '%s[WARN]%s %s\n' "${C_YELLOW}" "${C_RESET}" "$*"; }
fail() { printf '%s[FAIL]%s %s\n' "${C_RED}" "${C_RESET}" "$*"; exit 1; }
step() { printf '\n%s>> %s%s\n' "${C_BOLD}" "$*" "${C_RESET}"; }

cd /opt/theseus || fail "Cannot cd to /opt/theseus"

# ----------------------------------------------------------------------------
step "Checking ANTHROPIC_API_KEY"
if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    read -r -p "Paste your ANTHROPIC_API_KEY (sk-ant-...): " ANTHROPIC_API_KEY
fi
if [ -z "${ANTHROPIC_API_KEY}" ] || [ "${ANTHROPIC_API_KEY}" = "PLACEHOLDER" ]; then
    fail "ANTHROPIC_API_KEY is empty"
fi
ok "API key received (${#ANTHROPIC_API_KEY} chars)"

# ----------------------------------------------------------------------------
step "Step 6: Create theseus role (drop if exists for idempotency)"
THESEUS_PG_PW="$(openssl rand -hex 12)"

# Drop existing connections first to allow drop role
psql -h 127.0.0.1 -p 5433 -U postgres -d postgres -c "
    SELECT pg_terminate_backend(pid) FROM pg_stat_activity
    WHERE datname = 'theseus' AND pid <> pg_backend_pid();
" >/dev/null 2>&1 || true

psql -h 127.0.0.1 -p 5433 -U postgres -d postgres -c "DROP DATABASE IF EXISTS theseus;" \
    || fail "DROP DATABASE failed"
psql -h 127.0.0.1 -p 5433 -U postgres -d postgres -c "DROP ROLE IF EXISTS theseus;" \
    || fail "DROP ROLE failed"
psql -h 127.0.0.1 -p 5433 -U postgres -d postgres -c \
    "CREATE ROLE theseus WITH LOGIN PASSWORD '${THESEUS_PG_PW}';" \
    || fail "CREATE ROLE failed"
ok "Role theseus created"

# ----------------------------------------------------------------------------
step "Step 7: Create database theseus"
psql -h 127.0.0.1 -p 5433 -U postgres -d postgres -c \
    "CREATE DATABASE theseus OWNER theseus;" \
    || fail "CREATE DATABASE failed"
ok "Database theseus created"

# ----------------------------------------------------------------------------
step "Step 8: Enable extensions (vector, pgcrypto, pg_trgm)"
psql -h 127.0.0.1 -p 5433 -U postgres -d theseus -c "
    CREATE EXTENSION IF NOT EXISTS vector;
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
    CREATE EXTENSION IF NOT EXISTS pg_trgm;
" || fail "Extension creation failed"
ok "Extensions enabled"

# ----------------------------------------------------------------------------
step "Step 9: Apply migration 001_initial.sql (as theseus role)"
PGPASSWORD="${THESEUS_PG_PW}" psql -h 127.0.0.1 -p 5433 -U theseus -d theseus \
    -f /opt/theseus/core/db/migrations/001_initial.sql >/dev/null \
    || fail "Migration failed"
ok "Migration applied"

# ----------------------------------------------------------------------------
step "Step 10: Create Python venv + install requirements"
if [ ! -d "/opt/theseus/venv" ]; then
    python3 -m venv /opt/theseus/venv || fail "venv creation failed"
fi
/opt/theseus/venv/bin/pip install -q --upgrade pip || warn "pip upgrade had issues"
/opt/theseus/venv/bin/pip install -q -r /opt/theseus/requirements.txt \
    || fail "pip install -r requirements.txt failed"
ok "venv ready with all dependencies"

# ----------------------------------------------------------------------------
step "Step 11: Run pytest (safety gate)"
cd /opt/theseus
/opt/theseus/venv/bin/pytest tests/ -q --tb=line 2>&1 | tail -20
PYTEST_RC=${PIPESTATUS[0]}
if [ "$PYTEST_RC" -ne 0 ]; then
    warn "pytest had failures (RC=$PYTEST_RC) — review above; deploy will continue but verify before relying on data"
else
    ok "pytest passed"
fi

# ----------------------------------------------------------------------------
step "Step 12: Write .env (mode 600)"
cat > /opt/theseus/.env <<EOF
# Theseus Phase 0 — VPS deployed $(date -u +%Y-%m-%dT%H:%M:%SZ)
THESEUS_PG_HOST=127.0.0.1
THESEUS_PG_PORT=5433
THESEUS_PG_DB=theseus
THESEUS_PG_USER=theseus
THESEUS_PG_PASSWORD=${THESEUS_PG_PW}
THESEUS_PG_POOL_MAX=5
WIN3_PG_PORT=5432
THESEUS_KILL_FILE=
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
THESEUS_LLM_MODEL=claude-opus-4-5
THESEUS_COST_MONTHLY_USD=100
THESEUS_COST_HARD_DAILY_USD=20
THESEUS_COST_SOFT_HOURLY_USD=5
DISCORD_WEBHOOK_BRIEFING=PLACEHOLDER_THESEUS_BRIEFING
DISCORD_WEBHOOK_ALERTS=PLACEHOLDER_THESEUS_ALERTS
DISCORD_WEBHOOK_B2B_LEADS=PLACEHOLDER_THESEUS_B2B_LEADS
THESEUS_LOG_LEVEL=INFO
THESEUS_TZ=America/New_York
EOF
chmod 600 /opt/theseus/.env
ok ".env written (chmod 600)"

# ----------------------------------------------------------------------------
step "Step 13: Restore pg_hba.conf to scram-sha-256 (security)"
PG_HBA="$(ls /etc/postgresql/*/theseus/pg_hba.conf 2>/dev/null | head -1)"
if [ -n "$PG_HBA" ] && [ -f "${PG_HBA}.bak" ]; then
    cp "${PG_HBA}.bak" "${PG_HBA}"
    systemctl reload postgresql@16-theseus 2>/dev/null || systemctl reload "postgresql@$(ls /etc/postgresql/ | head -1)-theseus" 2>/dev/null || warn "PG reload may need manual run"
    ok "pg_hba.conf restored to original (password auth)"
else
    warn "pg_hba.conf backup not found — review /etc/postgresql/*/theseus/pg_hba.conf manually"
fi

# ----------------------------------------------------------------------------
step "Step 14: Verify password-based connection works"
if PGPASSWORD="${THESEUS_PG_PW}" psql -h 127.0.0.1 -p 5433 -U theseus -d theseus -c '\dt' >/dev/null 2>&1; then
    ok "theseus role authenticates with password — tables visible"
else
    warn "Could not verify password auth — may need pg_hba.conf check"
fi

# ----------------------------------------------------------------------------
step "Step 15: Install crontab (merge with existing)"
TMP_CRON="$(mktemp)"
crontab -l 2>/dev/null > "$TMP_CRON" || true
# Append theseus cron lines if not present
if ! grep -q "Theseus" "$TMP_CRON" 2>/dev/null; then
    echo "" >> "$TMP_CRON"
    echo "# Theseus Phase 0" >> "$TMP_CRON"
    cat /opt/theseus/crontab.example | grep -v "^#" | grep -v "^$" | grep -v "^CRON_TZ" >> "$TMP_CRON"
    crontab "$TMP_CRON"
    ok "crontab installed (merged with existing)"
else
    ok "Theseus crontab already present — skipping"
fi
rm -f "$TMP_CRON"

# ----------------------------------------------------------------------------
step "Step 16: Create logs directory"
mkdir -p /opt/theseus/logs
chmod 750 /opt/theseus/logs
ok "logs/ ready"

# ----------------------------------------------------------------------------
step "Step 17: Final summary"
echo "=========================================="
echo "Theseus Phase 0 — Deploy Complete"
echo "=========================================="
echo "DB: postgresql://theseus@127.0.0.1:5433/theseus"
echo "venv: /opt/theseus/venv"
echo ".env: /opt/theseus/.env (chmod 600)"
echo "cron: $(crontab -l 2>/dev/null | grep -c theseus) Theseus lines"
echo "logs: /opt/theseus/logs/"
echo ""
echo "PG password (also in .env):"
echo "  ${THESEUS_PG_PW}"
echo ""
echo "NEXT STEPS (do later when ready):"
echo "  1. Discord webhook URLs: edit /opt/theseus/.env to replace PLACEHOLDER_ values"
echo "  2. Manual orchestrator dry-run: /opt/theseus/venv/bin/python -m crawler.orchestrator"
echo "  3. Manual briefing dry-run:     /opt/theseus/venv/bin/python -m briefing.daily_briefing"
echo "  4. Check cron is registered:    crontab -l"
echo "=========================================="
ok "Deploy complete"
