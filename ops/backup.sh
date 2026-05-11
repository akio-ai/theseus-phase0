#!/usr/bin/env bash
# Theseus DB backup — gap #2 disaster guard.
# Run via cron daily 00:00 NJT. Keeps 30-day rolling window.
#
# Env required:
#   THESEUS_PG_HOST, THESEUS_PG_PORT, THESEUS_PG_DB, THESEUS_PG_USER, PGPASSWORD
#
# Output:
#   ~/Theseus_Phase0/backups/theseus-YYYYMMDDTHHMMSSZ.dump  (custom pg_dump format)
#
# Behaviour:
#   - On success → silent
#   - On failure → exit 1, intended to be picked up by ops/health_check.py
#   - Old files (> 30 days) deleted
set -euo pipefail

THESEUS_DIR="${THESEUS_DIR:-$HOME/Theseus_Phase0}"
BACKUP_DIR="${THESEUS_DIR}/backups"
mkdir -p "${BACKUP_DIR}"

TS="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="${BACKUP_DIR}/theseus-${TS}.dump"

# Load env if .env present (so cron picks it up)
if [ -f "${THESEUS_DIR}/.env" ]; then
    # shellcheck disable=SC1091
    set -a; . "${THESEUS_DIR}/.env"; set +a
fi

# Map THESEUS_PG_* → libpq env
export PGHOST="${THESEUS_PG_HOST:-127.0.0.1}"
export PGPORT="${THESEUS_PG_PORT:-5433}"
export PGUSER="${THESEUS_PG_USER:-theseus}"
export PGDATABASE="${THESEUS_PG_DB:-theseus}"
export PGPASSWORD="${THESEUS_PG_PASSWORD:-}"

echo "[$(date -u +%FT%TZ)] backup → ${OUT}"
pg_dump --format=custom --no-owner --no-privileges --file="${OUT}"

# Rotate: remove .dump files older than 30 days
find "${BACKUP_DIR}" -maxdepth 1 -type f -name 'theseus-*.dump' -mtime +30 -print -delete

echo "[$(date -u +%FT%TZ)] backup OK; total kept: $(ls -1 "${BACKUP_DIR}"/theseus-*.dump 2>/dev/null | wc -l)"
