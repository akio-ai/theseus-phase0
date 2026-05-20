#!/usr/bin/env bash
#
# bootstrap_mac.sh — Mac-side pre-flight + rsync for Theseus Phase 0 VPS deploy
#
# What it does (on this Mac, BEFORE you SSH into the VPS):
#   1) Sanity-checks the local repo (git clean + pytest)
#   2) rsyncs ~/Theseus_Phase0/ to the VPS at root@HOST:/opt/theseus/
#   3) Prints the exact next-step command to SSH in and run ops/deploy.sh
#
# It does NOT auto-SSH and run deploy.sh — deploy.sh is interactive and needs
# a real tty for prompts (Anthropic API key + Discord webhooks).
#
# Usage:
#   ops/bootstrap_mac.sh [--host IP] [--user USER] [--remote-path PATH]
#                       [--dry-run] [--skip-git-check]
#
set -euo pipefail

# ---------- defaults ----------
HOST="64.176.222.33"
USER_REMOTE="root"
REMOTE_PATH="/opt/theseus"
LOCAL_SRC="${HOME}/Theseus_Phase0"
DRY_RUN=0
SKIP_GIT_CHECK=0

# ---------- timing ----------
SCRIPT_START_EPOCH=$(date +%s)

# ---------- colors ----------
if [[ -n "${NO_COLOR:-}" ]] || [[ ! -t 1 ]]; then
    C_RESET=""
    C_GREEN=""
    C_YELLOW=""
    C_RED=""
    C_BLUE=""
    C_BOLD=""
    C_DIM=""
else
    C_RESET=$'\033[0m'
    C_GREEN=$'\033[32m'
    C_YELLOW=$'\033[33m'
    C_RED=$'\033[31m'
    C_BLUE=$'\033[34m'
    C_BOLD=$'\033[1m'
    C_DIM=$'\033[2m'
fi

ok()    { printf "%s[ OK ]%s   %s\n" "${C_GREEN}" "${C_RESET}" "$*"; }
warn()  { printf "%s[WARN]%s   %s\n" "${C_YELLOW}" "${C_RESET}" "$*"; }
fail()  { printf "%s[FAIL]%s   %s\n" "${C_RED}" "${C_RESET}" "$*" >&2; }
info()  { printf "%s[INFO]%s   %s\n" "${C_BLUE}" "${C_RESET}" "$*"; }
step()  { printf "\n%s==>%s %s%s%s\n" "${C_BLUE}" "${C_RESET}" "${C_BOLD}" "$*" "${C_RESET}"; }

usage() {
    cat <<EOF
Usage: $(basename "$0") [options]

Options:
  --host IP_OR_HOST     VPS host (default: ${HOST})
  --user USER           SSH user (default: ${USER_REMOTE})
  --remote-path PATH    Remote install path (default: ${REMOTE_PATH})
  --dry-run             Show what would happen, do not rsync
  --skip-git-check      Allow rsync with dirty git tree, skip pytest
  -h, --help            Show this help
EOF
}

# ---------- arg parsing ----------
while [[ $# -gt 0 ]]; do
    case "$1" in
        --host)
            [[ $# -ge 2 ]] || { fail "--host needs a value"; exit 2; }
            HOST="$2"; shift 2 ;;
        --user)
            [[ $# -ge 2 ]] || { fail "--user needs a value"; exit 2; }
            USER_REMOTE="$2"; shift 2 ;;
        --remote-path)
            [[ $# -ge 2 ]] || { fail "--remote-path needs a value"; exit 2; }
            REMOTE_PATH="$2"; shift 2 ;;
        --dry-run)
            DRY_RUN=1; shift ;;
        --skip-git-check)
            SKIP_GIT_CHECK=1; shift ;;
        -h|--help)
            usage; exit 0 ;;
        *)
            fail "Unknown argument: $1"
            usage
            exit 2 ;;
    esac
done

# ---------- cleanup on exit ----------
on_exit() {
    local rc=$?
    local elapsed=$(( $(date +%s) - SCRIPT_START_EPOCH ))
    printf "\n%s---%s elapsed: %ss  exit: %s\n" "${C_DIM}" "${C_RESET}" "${elapsed}" "${rc}"
    if [[ ${rc} -eq 0 ]]; then
        ok "bootstrap_mac.sh finished cleanly"
    else
        fail "bootstrap_mac.sh exited with code ${rc}"
    fi
}
trap on_exit EXIT

# ---------- banner ----------
printf "\n"
printf "%s========================================================%s\n" "${C_BOLD}" "${C_RESET}"
printf "%s  Theseus Phase 0 — Mac bootstrap%s\n" "${C_BOLD}" "${C_RESET}"
printf "%s========================================================%s\n" "${C_BOLD}" "${C_RESET}"
printf "  Local source : %s\n" "${LOCAL_SRC}"
printf "  Target host  : %s@%s\n" "${USER_REMOTE}" "${HOST}"
printf "  Remote path  : %s\n" "${REMOTE_PATH}"
printf "  Dry run      : %s\n" "$([[ ${DRY_RUN} -eq 1 ]] && echo yes || echo no)"
printf "  Skip checks  : %s\n" "$([[ ${SKIP_GIT_CHECK} -eq 1 ]] && echo yes || echo no)"
printf "%s--------------------------------------------------------%s\n" "${C_BOLD}" "${C_RESET}"

# ---------- step 1: verify local source ----------
step "Step 1/5  Verify local source directory"

if [[ ! -d "${LOCAL_SRC}" ]]; then
    fail "Local source not found: ${LOCAL_SRC}"
    exit 1
fi
ok "Found ${LOCAL_SRC}"

if [[ ! -d "${LOCAL_SRC}/.git" ]]; then
    fail "${LOCAL_SRC} is not a git repository"
    exit 1
fi
ok "It's a git repo"

# ---------- step 2: git cleanliness ----------
step "Step 2/5  Check git working tree"

cd "${LOCAL_SRC}"

if [[ ${SKIP_GIT_CHECK} -eq 1 ]]; then
    warn "--skip-git-check given, skipping git status check"
else
    DIRTY=$(git status --porcelain || true)
    if [[ -n "${DIRTY}" ]]; then
        fail "Local repo has uncommitted changes:"
        printf "%s\n" "${DIRTY}" | sed 's/^/        /'
        printf "\n"
        warn "Commit your changes first, or rerun with --skip-git-check"
        exit 1
    fi
    ok "Working tree clean"

    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "?")
    CURRENT_COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "?")
    info "Branch: ${CURRENT_BRANCH}  Commit: ${CURRENT_COMMIT}"
fi

# ---------- step 3: pytest ----------
step "Step 3/5  Run local pytest"

if [[ ${SKIP_GIT_CHECK} -eq 1 ]]; then
    warn "--skip-git-check given, skipping pytest"
elif [[ -x "${LOCAL_SRC}/venv/bin/pytest" ]]; then
    info "Running: venv/bin/pytest tests/ -q"
    if "${LOCAL_SRC}/venv/bin/pytest" tests/ -q; then
        ok "Local tests pass"
    else
        fail "Local pytest failed — refusing to ship broken code"
        warn "Fix tests first, or rerun with --skip-git-check (not recommended)"
        exit 1
    fi
elif [[ -x "${LOCAL_SRC}/.venv/bin/pytest" ]]; then
    info "Running: .venv/bin/pytest tests/ -q"
    if "${LOCAL_SRC}/.venv/bin/pytest" tests/ -q; then
        ok "Local tests pass"
    else
        fail "Local pytest failed — refusing to ship broken code"
        warn "Fix tests first, or rerun with --skip-git-check (not recommended)"
        exit 1
    fi
else
    fail "No venv found at ${LOCAL_SRC}/venv or ${LOCAL_SRC}/.venv"
    warn "Create one with:"
    warn "    cd ${LOCAL_SRC} && python3 -m venv venv && \\"
    warn "    venv/bin/pip install -r requirements.txt"
    warn "Then rerun this script. (Or rerun with --skip-git-check to bypass — not recommended.)"
    exit 1
fi

# ---------- step 4: rsync ----------
step "Step 4/5  rsync to ${USER_REMOTE}@${HOST}:${REMOTE_PATH}"

SSH_OPTS="ssh -o IdentitiesOnly=yes -o PreferredAuthentications=password -o PubkeyAuthentication=no"

# Build rsync args as an array so quoting is safe.
RSYNC_ARGS=(
    -av
    --delete
    --stats
    --human-readable
    --exclude='__pycache__'
    --exclude='.git'
    --exclude='venv'
    --exclude='.venv'
    --exclude='backups/'
    --exclude='logs/'
    --exclude='control/.killed*'
    --exclude='style_engine/private/'
    --exclude='cost/cost.db'
    --exclude='briefing/learn.db'
    --exclude='funnel/funnel.db'
    --exclude='.env'
    --exclude='.DS_Store'
    --exclude='ops/last_run.json'
    -e "${SSH_OPTS}"
    "${LOCAL_SRC}/"
    "${USER_REMOTE}@${HOST}:${REMOTE_PATH}/"
)

info "rsync command:"
printf "        rsync"
for a in "${RSYNC_ARGS[@]}"; do
    # quote anything with spaces or quotes for legibility
    if [[ "${a}" == *" "* || "${a}" == *"'"* ]]; then
        printf " '%s'" "${a}"
    else
        printf " %s" "${a}"
    fi
done
printf "\n\n"

if [[ ${DRY_RUN} -eq 1 ]]; then
    warn "--dry-run given, not actually running rsync"
    RSYNC_RC=0
else
    info "You may be prompted for the SSH password for ${USER_REMOTE}@${HOST}."
    info "Starting transfer..."
    printf "\n"
    RSYNC_START=$(date +%s)
    set +e
    rsync "${RSYNC_ARGS[@]}"
    RSYNC_RC=$?
    set -e
    RSYNC_ELAPSED=$(( $(date +%s) - RSYNC_START ))
    printf "\n"
    if [[ ${RSYNC_RC} -ne 0 ]]; then
        fail "rsync failed with exit code ${RSYNC_RC}"
        exit ${RSYNC_RC}
    fi
    ok "rsync complete in ${RSYNC_ELAPSED}s"
fi

# ---------- step 5: next-step instructions ----------
step "Step 5/5  Next step — run deploy.sh on the VPS"

cat <<EOF

  ${C_BOLD}Code is on the VPS. Now SSH in and run the deploy:${C_RESET}

      ${C_GREEN}ssh -o IdentitiesOnly=yes -o PreferredAuthentications=password -o PubkeyAuthentication=no ${USER_REMOTE}@${HOST}${C_RESET}

  ${C_BOLD}Once you're logged in:${C_RESET}

      ${C_GREEN}cd ${REMOTE_PATH}${C_RESET}
      ${C_GREEN}bash ops/deploy.sh${C_RESET}

  ${C_YELLOW}Heads up:${C_RESET} deploy.sh is interactive. It will prompt for:
      - Anthropic API key            (required)
      - Discord webhook: ops         (optional — press Enter to skip)
      - Discord webhook: briefing    (optional — press Enter to skip)
      - Discord webhook: pulse       (optional — press Enter to skip)

  Have those handy before you start. This script is NOT auto-running
  deploy.sh because the prompts need a real tty.

EOF

ok "Bootstrap done. Over to you."
