#!/usr/bin/env bash
# Theseus DB restore — gap #2 disaster guard.
#
# Usage:
#   ops/restore.sh --dry-run path/to/backups/theseus-YYYYMMDDTHHMMSSZ.dump
#   ops/restore.sh --execute path/to/backups/theseus-YYYYMMDDTHHMMSSZ.dump
#
# --dry-run lists what pg_restore would do (no DB writes).
# --execute actually restores. ALWAYS run --dry-run first.
#
# Safety:
#   - Refuses to run unless kill switch is engaged (force conscious halt of crawler first)
#   - Pass --i-know-what-im-doing to bypass the kill-switch check (rare; production rescue only)
set -euo pipefail

THESEUS_DIR="${THESEUS_DIR:-$HOME/Theseus_Phase0}"

MODE=""
DUMP=""
FORCE=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run)   MODE=dry; shift ;;
        --execute)   MODE=execute; shift ;;
        --i-know-what-im-doing) FORCE=1; shift ;;
        -h|--help)
            sed -n '2,15p' "$0"; exit 0 ;;
        *)
            DUMP="$1"; shift ;;
    esac
done

if [[ -z "$MODE" || -z "$DUMP" ]]; then
    echo "usage: $0 --dry-run|--execute <dump-file>" >&2
    exit 2
fi

if [[ ! -f "$DUMP" ]]; then
    echo "dump file not found: $DUMP" >&2
    exit 2
fi

# Load env if present
if [[ -f "${THESEUS_DIR}/.env" ]]; then
    set -a; . "${THESEUS_DIR}/.env"; set +a
fi

export PGHOST="${THESEUS_PG_HOST:-127.0.0.1}"
export PGPORT="${THESEUS_PG_PORT:-5433}"
export PGUSER="${THESEUS_PG_USER:-theseus}"
export PGDATABASE="${THESEUS_PG_DB:-theseus}"
export PGPASSWORD="${THESEUS_PG_PASSWORD:-}"

# Safety: require kill switch in --execute mode unless forced
KILL_FILE="${THESEUS_KILL_FILE:-$THESEUS_DIR/control/.killed}"
if [[ "$MODE" == "execute" && ! -f "$KILL_FILE" && "$FORCE" -ne 1 ]]; then
    echo "REFUSING: kill switch not engaged." >&2
    echo "Engage with: python -m control.emergency_stop stop --reason 'restoring DB'" >&2
    echo "Then re-run, or pass --i-know-what-im-doing" >&2
    exit 3
fi

if [[ "$MODE" == "dry" ]]; then
    echo "[dry-run] would restore $DUMP to ${PGDATABASE}@${PGHOST}:${PGPORT}"
    pg_restore --list "$DUMP" | head -40
    echo "..."
    echo "[dry-run] table-of-contents lines: $(pg_restore --list "$DUMP" | wc -l)"
    exit 0
fi

# Execute
echo "[execute] restoring $DUMP → ${PGDATABASE}@${PGHOST}:${PGPORT}"
pg_restore --clean --if-exists --no-owner --no-privileges \
           --dbname="${PGDATABASE}" "$DUMP"
echo "[execute] restore OK at $(date -u +%FT%TZ)"
echo "Remember to clear kill switch when ready:"
echo "  python -m control.emergency_stop clear --confirm yes-clear-kill"
