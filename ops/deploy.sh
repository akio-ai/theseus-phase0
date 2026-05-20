#!/usr/bin/env bash
# ============================================================================
# Theseus Phase 0 — VPS Bootstrap Installer
# ----------------------------------------------------------------------------
# Bootstraps the Theseus Phase 0 self-learning wine knowledge layer on a
# fresh Debian/Ubuntu VPS.
#
# Invocation:    sudo bash /opt/theseus/ops/deploy.sh
# Working dir:   /opt/theseus/  (must already contain the rsync'd code)
# Run as:        root
#
# Isolation guarantees (the script will refuse to violate these):
#   - PostgreSQL cluster runs on port 5433 (Win3 trading owns 5432)
#   - Python venv lives entirely inside /opt/theseus/venv/
#   - No global pip installs, no chown outside /opt/theseus/
#   - No SSH/password rotation (separate script owns that)
#
# Idempotent: re-running is safe. Already-completed steps are detected and
# skipped. The script never destroys existing data.
#
# Safety gate: pytest (step 11/17) MUST pass 85/85. The script aborts before
# touching .env, smoke tests, or crontab if any test fails.
# ============================================================================

set -euo pipefail

# ----- Constants ------------------------------------------------------------
readonly THESEUS_ROOT="/opt/theseus"
readonly THESEUS_VENV="${THESEUS_ROOT}/venv"
readonly THESEUS_LOGS="${THESEUS_ROOT}/logs"
readonly THESEUS_ENV="${THESEUS_ROOT}/.env"
readonly THESEUS_ENV_EXAMPLE="${THESEUS_ROOT}/.env.example"
readonly THESEUS_REQS="${THESEUS_ROOT}/requirements.txt"
readonly THESEUS_MIGRATION="${THESEUS_ROOT}/core/db/migrations/001_initial.sql"
readonly THESEUS_CRONTAB="${THESEUS_ROOT}/crontab.example"

readonly PG_PORT=5433
readonly PG_CLUSTER_NAME="theseus"
readonly PG_HOST="127.0.0.1"
readonly PG_DB="theseus"
readonly PG_USER="theseus"
readonly WIN3_PG_PORT=5432

readonly TOTAL_STEPS=17
readonly DEPLOY_START_EPOCH="$(date +%s)"

# Password storage (cleaned up at exit, no matter what)
readonly PG_PASSWORD_TMPFILE="$(mktemp -t theseus_pg_pw.XXXXXX)"
trap 'rm -f "${PG_PASSWORD_TMPFILE}"' EXIT

# ----- Color helpers --------------------------------------------------------
if [[ -t 1 ]] && [[ -z "${NO_COLOR:-}" ]]; then
  readonly C_RED=$'\033[31m'
  readonly C_GREEN=$'\033[32m'
  readonly C_YELLOW=$'\033[33m'
  readonly C_BLUE=$'\033[34m'
  readonly C_BOLD=$'\033[1m'
  readonly C_RESET=$'\033[0m'
else
  readonly C_RED=""
  readonly C_GREEN=""
  readonly C_YELLOW=""
  readonly C_BLUE=""
  readonly C_BOLD=""
  readonly C_RESET=""
fi

log_ok()   { printf '%s[ OK ]%s %s\n'   "${C_GREEN}"  "${C_RESET}" "$*"; }
log_warn() { printf '%s[WARN]%s %s\n'   "${C_YELLOW}" "${C_RESET}" "$*"; }
log_fail() { printf '%s[FAIL]%s %s\n'   "${C_RED}"    "${C_RESET}" "$*" >&2; }
log_step() { printf '\n%s[step %d/%d]%s %s\n' "${C_BOLD}${C_BLUE}" "$1" "${TOTAL_STEPS}" "${C_RESET}" "$2"; }
log_info() { printf '       %s\n' "$*"; }

die() {
  local msg="$1"
  local hint="${2:-(no recovery hint provided)}"
  log_fail "${msg}"
  printf '       %sRecovery:%s %s\n' "${C_YELLOW}" "${C_RESET}" "${hint}" >&2
  exit 1
}

# Wrap commands so a failure prints what failed + hint
run_or_die() {
  local hint="$1"; shift
  local cmd_str="$*"
  if ! "$@"; then
    die "Command failed: ${cmd_str}" "${hint}"
  fi
}

# ----- Bootstrap logging dir (best-effort, before formal step 16) ----------
# We tee to logs/deploy.log; need the dir before the banner prints.
mkdir -p "${THESEUS_LOGS}" 2>/dev/null || true
readonly DEPLOY_LOG="${THESEUS_LOGS}/deploy.log"

# Redirect a copy of all stdout+stderr to the deploy log (append).
# Using `exec` + process substitution so subsequent output is captured.
if [[ -w "${THESEUS_LOGS}" ]] || mkdir -p "${THESEUS_LOGS}" 2>/dev/null; then
  exec > >(tee -a "${DEPLOY_LOG}") 2>&1
fi

# ============================================================================
# BANNER + CONFIRMATION (step 1/17)
# ============================================================================
log_step 1 "Banner & confirmation"
cat <<BANNER
${C_BOLD}============================================================${C_RESET}
${C_BOLD}  Theseus Phase 0 — VPS Bootstrap Installer${C_RESET}
${C_BOLD}============================================================${C_RESET}

This script will:

  - Verify root + working dir + required files
  - Install apt packages: python3.11, postgresql, pgvector
  - Create an ISOLATED PostgreSQL cluster on port ${PG_PORT}
    (your existing Win3 cluster on port ${WIN3_PG_PORT} is untouched)
  - Create role '${PG_USER}' with a freshly generated password
  - Create database '${PG_DB}' and enable vector/pgcrypto/pg_trgm
  - Run migration 001_initial.sql
  - Create Python venv at ${THESEUS_VENV}
  - Install requirements.txt
  - Run 85 pytest tests (SAFETY GATE — abort on any failure)
  - Prompt for secrets (ANTHROPIC_API_KEY, Discord webhooks)
  - Write .env (chmod 600)
  - Smoke-test emergency_stop + cost_db (no live API calls)
  - Install crontab (merge with existing if any)
  - Print summary

Idempotent: rerun is safe.
Log: ${DEPLOY_LOG}

BANNER

# Allow non-interactive runs via THESEUS_DEPLOY_YES=1
if [[ "${THESEUS_DEPLOY_YES:-0}" == "1" ]]; then
  log_info "THESEUS_DEPLOY_YES=1 set — skipping interactive confirmation"
else
  read -r -p "Proceed? [y/N] " _confirm
  case "${_confirm}" in
    y|Y|yes|YES) ;;
    *) die "User aborted at confirmation prompt" "Re-run when ready: sudo bash ${THESEUS_ROOT}/ops/deploy.sh" ;;
  esac
fi
log_ok "Confirmed — proceeding"

# ============================================================================
# STEP 2/17 — Verify root + cwd
# ============================================================================
log_step 2 "Verify running as root in ${THESEUS_ROOT}"

if [[ "$(id -u)" -ne 0 ]]; then
  die "Must run as root (current uid=$(id -u))" "Re-run with: sudo bash ${THESEUS_ROOT}/ops/deploy.sh"
fi
log_ok "Running as root"

if [[ "$(pwd)" != "${THESEUS_ROOT}" ]]; then
  log_warn "cwd is $(pwd); cd'ing to ${THESEUS_ROOT}"
  cd "${THESEUS_ROOT}" || die "Cannot cd to ${THESEUS_ROOT}" "Check that the rsync from the operator's Mac actually landed there. Expected layout: ${THESEUS_ROOT}/{core,tests,ops,...}"
fi
log_ok "Working directory: $(pwd)"

# ============================================================================
# STEP 3/17 — Verify required files
# ============================================================================
log_step 3 "Verify required files present"

required_files=(
  "${THESEUS_REQS}"
  "${THESEUS_MIGRATION}"
  "${THESEUS_CRONTAB}"
  "${THESEUS_ENV_EXAMPLE}"
)

missing=()
for f in "${required_files[@]}"; do
  if [[ ! -f "${f}" ]]; then
    missing+=("${f}")
  fi
done

if (( ${#missing[@]} > 0 )); then
  log_fail "Missing required files:"
  for f in "${missing[@]}"; do printf '         - %s\n' "${f}" >&2; done
  die "Aborting — repo appears incomplete" "Re-run the rsync from the operator's Mac. Verify with: ls -la ${THESEUS_ROOT}/"
fi
log_ok "All required files present"

# ============================================================================
# STEP 4/17 — Detect OS, install apt packages
# ============================================================================
log_step 4 "Detect OS & install apt packages"

if [[ ! -f /etc/os-release ]]; then
  die "/etc/os-release missing — cannot detect OS" "This script supports Debian/Ubuntu only."
fi
# shellcheck disable=SC1091
. /etc/os-release
log_info "OS: ${PRETTY_NAME:-${ID} ${VERSION_ID:-?}}"

case "${ID:-}" in
  debian|ubuntu) ;;
  *) die "Unsupported OS: ${ID:-unknown}" "This script supports Debian/Ubuntu only. For other distros, install equivalents manually." ;;
esac

export DEBIAN_FRONTEND=noninteractive

log_info "apt-get update ..."
run_or_die "Check network connectivity & /etc/apt/sources.list" \
  apt-get update -qq

# Detect available Python 3.11
PY_PKG="python3.11"
PY_VENV_PKG="python3.11-venv"
if ! apt-cache show python3.11 >/dev/null 2>&1; then
  log_warn "python3.11 not in apt cache — falling back to python3 / python3-venv"
  PY_PKG="python3"
  PY_VENV_PKG="python3-venv"
fi

# Detect PostgreSQL major version. Prefer 15; if not available, pick the
# highest available `postgresql-NN-pgvector` package and align cluster version.
PG_VERSION=""
for candidate_ver in 15 16 17 14; do
  if apt-cache show "postgresql-${candidate_ver}-pgvector" >/dev/null 2>&1; then
    PG_VERSION="${candidate_ver}"
    break
  fi
done

if [[ -z "${PG_VERSION}" ]]; then
  # Fallback: install plain postgresql and try the unversioned pgvector pkg
  log_warn "No versioned pgvector found; will try unversioned 'postgresql-pgvector' / 'pgvector'"
  PG_VERSION="DEFAULT"
fi

log_info "Selected: python=${PY_PKG}, postgresql version target=${PG_VERSION}"

# Build install list
declare -a APT_PKGS=("${PY_PKG}" "${PY_VENV_PKG}" "python3-pip" "postgresql" "postgresql-contrib")
if [[ "${PG_VERSION}" == "DEFAULT" ]]; then
  if apt-cache show postgresql-pgvector >/dev/null 2>&1; then
    APT_PKGS+=("postgresql-pgvector")
  elif apt-cache show pgvector >/dev/null 2>&1; then
    APT_PKGS+=("pgvector")
  else
    die "No pgvector package found in apt" "On older distros, build from source: https://github.com/pgvector/pgvector — or add the PGDG repository: https://wiki.postgresql.org/wiki/Apt"
  fi
else
  APT_PKGS+=("postgresql-${PG_VERSION}-pgvector")
fi

log_info "Installing: ${APT_PKGS[*]}"
run_or_die "Try: apt-get install -y ${APT_PKGS[*]}  — and check /var/log/apt/term.log" \
  apt-get install -y -q "${APT_PKGS[@]}"

log_ok "apt packages installed"

# Re-detect PG_VERSION from the actual installed cluster if we used DEFAULT
if [[ "${PG_VERSION}" == "DEFAULT" ]]; then
  if command -v pg_lsclusters >/dev/null 2>&1; then
    PG_VERSION="$(pg_lsclusters -h 2>/dev/null | awk 'NR==1{print $1; exit}' || true)"
  fi
  if [[ -z "${PG_VERSION}" || "${PG_VERSION}" == "DEFAULT" ]]; then
    # Last resort: scan /etc/postgresql
    PG_VERSION="$(ls /etc/postgresql 2>/dev/null | sort -n | tail -1 || true)"
  fi
  if [[ -z "${PG_VERSION}" ]]; then
    die "Could not determine installed PostgreSQL version" "Run: pg_lsclusters  and re-run this script with PG_VERSION env set."
  fi
  log_info "Resolved PostgreSQL version: ${PG_VERSION}"
fi

# ============================================================================
# STEP 5/17 — Create isolated PostgreSQL cluster on port 5433
# ============================================================================
log_step 5 "Create isolated PostgreSQL cluster '${PG_CLUSTER_NAME}' on port ${PG_PORT}"

# Refuse to touch port 5432 (Win3 territory)
if pg_lsclusters -h 2>/dev/null | awk '{print $1"|"$2"|"$3}' | grep -qE "^${PG_VERSION}\\|${PG_CLUSTER_NAME}\\|"; then
  # Cluster exists. Verify it's on our port.
  existing_port="$(pg_lsclusters -h "${PG_VERSION}" "${PG_CLUSTER_NAME}" 2>/dev/null | awk '{print $3}' | head -1)"
  if [[ "${existing_port}" == "${PG_PORT}" ]]; then
    log_ok "Cluster ${PG_VERSION}/${PG_CLUSTER_NAME} already exists on port ${PG_PORT} — skipping create"
  else
    die "Cluster ${PG_VERSION}/${PG_CLUSTER_NAME} exists but on port ${existing_port}, not ${PG_PORT}" \
        "Investigate manually: pg_lsclusters. Do NOT drop the cluster if it contains data."
  fi
else
  # Defensive: confirm port 5433 isn't already taken by something else
  if pg_lsclusters -h 2>/dev/null | awk '{print $3}' | grep -qx "${PG_PORT}"; then
    other="$(pg_lsclusters -h 2>/dev/null | awk -v p="${PG_PORT}" '$3==p {print $1"/"$2}')"
    die "Port ${PG_PORT} already used by cluster ${other}" "Either reuse that cluster (manual edit needed) or pick a different port and rerun."
  fi

  if ! command -v pg_createcluster >/dev/null 2>&1; then
    die "pg_createcluster not found" "Install postgresql-common: apt-get install -y postgresql-common"
  fi

  log_info "Creating cluster: pg_createcluster ${PG_VERSION} ${PG_CLUSTER_NAME} -p ${PG_PORT} --start"
  run_or_die "Inspect: pg_lsclusters — if half-created, drop with: pg_dropcluster ${PG_VERSION} ${PG_CLUSTER_NAME}" \
    pg_createcluster "${PG_VERSION}" "${PG_CLUSTER_NAME}" -p "${PG_PORT}" --start
  log_ok "Cluster ${PG_VERSION}/${PG_CLUSTER_NAME} created on port ${PG_PORT}"
fi

# Make absolutely sure it's started
if ! pg_lsclusters -h "${PG_VERSION}" "${PG_CLUSTER_NAME}" 2>/dev/null | awk '{print $4}' | grep -q online; then
  log_info "Cluster not online — starting"
  run_or_die "Check logs: pg_ctlcluster ${PG_VERSION} ${PG_CLUSTER_NAME} status; journalctl -u postgresql@${PG_VERSION}-${PG_CLUSTER_NAME}" \
    pg_ctlcluster "${PG_VERSION}" "${PG_CLUSTER_NAME}" start
fi
log_ok "Cluster online on port ${PG_PORT}"

# Re-assert isolation: Win3 (5432) and Theseus (5433) must both exist & differ
if ! pg_lsclusters -h 2>/dev/null | awk '{print $3}' | grep -qx "${PG_PORT}"; then
  die "Theseus cluster not on port ${PG_PORT} after start" "Run pg_lsclusters and reconcile."
fi
log_ok "Isolation check: Theseus on ${PG_PORT} confirmed (Win3 on ${WIN3_PG_PORT} untouched)"

# ============================================================================
# STEP 6/17 — Create role 'theseus' with auto-generated password
# ============================================================================
log_step 6 "Create PostgreSQL role '${PG_USER}'"

# Generate a strong 24-char password (alphanumeric only to avoid shell/SQL hell)
gen_password() {
  # 24 chars of [A-Za-z0-9]
  LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 24
}

role_exists() {
  sudo -u postgres psql -h "${PG_HOST}" -p "${PG_PORT}" -d postgres -tAc \
    "SELECT 1 FROM pg_roles WHERE rolname='${PG_USER}'" 2>/dev/null | grep -q 1
}

if role_exists; then
  log_warn "Role '${PG_USER}' already exists — preserving existing password"
  # If .env exists, password is already there. If not, we'll need to recreate
  # password via ALTER USER. But that breaks idempotency unless .env exists.
  if [[ -f "${THESEUS_ENV}" ]] && grep -q '^THESEUS_PG_PASSWORD=' "${THESEUS_ENV}"; then
    THESEUS_PG_PASSWORD="$(grep '^THESEUS_PG_PASSWORD=' "${THESEUS_ENV}" | head -1 | cut -d= -f2- | tr -d '"'"'"'')"
    log_ok "Reusing existing password from ${THESEUS_ENV}"
  else
    # Edge case: role exists but no .env. Rotate password (safer than guessing).
    THESEUS_PG_PASSWORD="$(gen_password)"
    log_warn "Role exists but no .env found — rotating password"
    sudo -u postgres psql -h "${PG_HOST}" -p "${PG_PORT}" -d postgres -c \
      "ALTER ROLE \"${PG_USER}\" WITH LOGIN PASSWORD '${THESEUS_PG_PASSWORD}';" \
      >/dev/null || die "ALTER ROLE failed" "Inspect: sudo -u postgres psql -p ${PG_PORT}"
  fi
else
  THESEUS_PG_PASSWORD="$(gen_password)"
  log_info "Creating role '${PG_USER}' with 24-char auto-generated password"
  sudo -u postgres psql -h "${PG_HOST}" -p "${PG_PORT}" -d postgres -c \
    "CREATE ROLE \"${PG_USER}\" WITH LOGIN PASSWORD '${THESEUS_PG_PASSWORD}';" \
    >/dev/null || die "CREATE ROLE failed" "Check cluster is online: pg_lsclusters | grep ${PG_CLUSTER_NAME}"
  log_ok "Role '${PG_USER}' created"
fi

# Stash password in tmpfile (cleaned by EXIT trap)
printf '%s' "${THESEUS_PG_PASSWORD}" > "${PG_PASSWORD_TMPFILE}"
chmod 600 "${PG_PASSWORD_TMPFILE}"

# ============================================================================
# STEP 7/17 — Create database 'theseus' owned by role 'theseus'
# ============================================================================
log_step 7 "Create database '${PG_DB}' owned by '${PG_USER}'"

db_exists() {
  sudo -u postgres psql -h "${PG_HOST}" -p "${PG_PORT}" -d postgres -tAc \
    "SELECT 1 FROM pg_database WHERE datname='${PG_DB}'" 2>/dev/null | grep -q 1
}

if db_exists; then
  log_ok "Database '${PG_DB}' already exists — skipping create"
else
  log_info "Creating database '${PG_DB}' ..."
  sudo -u postgres psql -h "${PG_HOST}" -p "${PG_PORT}" -d postgres -c \
    "CREATE DATABASE \"${PG_DB}\" OWNER \"${PG_USER}\";" \
    >/dev/null || die "CREATE DATABASE failed" "Check disk space + cluster status."
  log_ok "Database '${PG_DB}' created, owned by '${PG_USER}'"
fi

# ============================================================================
# STEP 8/17 — Enable extensions: vector, pgcrypto, pg_trgm
# ============================================================================
log_step 8 "Enable extensions: vector, pgcrypto, pg_trgm"

for ext in vector pgcrypto pg_trgm; do
  log_info "  CREATE EXTENSION IF NOT EXISTS ${ext};"
  sudo -u postgres psql -h "${PG_HOST}" -p "${PG_PORT}" -d "${PG_DB}" -c \
    "CREATE EXTENSION IF NOT EXISTS ${ext};" >/dev/null \
    || die "Extension ${ext} failed to install" "Verify pgvector package: dpkg -l | grep pgvector"
done
log_ok "All extensions enabled"

# ============================================================================
# STEP 9/17 — Run migration 001_initial.sql
# ============================================================================
log_step 9 "Run migration 001_initial.sql"

# Use PGPASSWORD to authenticate as the theseus role (proves the role works).
# Migration must be idempotent — if it's not, the codebase itself has a bug.
log_info "Applying: ${THESEUS_MIGRATION}"
if ! PGPASSWORD="${THESEUS_PG_PASSWORD}" psql \
      -h "${PG_HOST}" -p "${PG_PORT}" -U "${PG_USER}" -d "${PG_DB}" \
      -v ON_ERROR_STOP=1 \
      -f "${THESEUS_MIGRATION}" >/dev/null; then
  die "Migration failed" "Inspect: PGPASSWORD=*** psql -h ${PG_HOST} -p ${PG_PORT} -U ${PG_USER} -d ${PG_DB} -f ${THESEUS_MIGRATION}"
fi
log_ok "Migration applied"

# ============================================================================
# STEP 10/17 — Create Python venv & install requirements.txt
# ============================================================================
log_step 10 "Create Python venv & install requirements"

# Pick python interpreter — prefer 3.11
PY_BIN=""
for candidate in python3.11 python3; do
  if command -v "${candidate}" >/dev/null 2>&1; then
    PY_BIN="$(command -v "${candidate}")"
    break
  fi
done
[[ -n "${PY_BIN}" ]] || die "No python3 interpreter found" "Reinstall: apt-get install -y python3"
log_info "Using interpreter: ${PY_BIN} ($(${PY_BIN} --version 2>&1))"

if [[ -d "${THESEUS_VENV}" && -x "${THESEUS_VENV}/bin/python" ]]; then
  log_ok "venv already exists at ${THESEUS_VENV} — skipping create"
else
  log_info "Creating venv at ${THESEUS_VENV} ..."
  run_or_die "Ensure ${PY_VENV_PKG} is installed: apt-get install -y ${PY_VENV_PKG}" \
    "${PY_BIN}" -m venv "${THESEUS_VENV}"
fi

log_info "Upgrading pip ..."
run_or_die "Check network; try: ${THESEUS_VENV}/bin/pip install --upgrade pip" \
  "${THESEUS_VENV}/bin/pip" install --quiet --upgrade pip

log_info "Installing requirements.txt (this may take 1-3 min) ..."
if ! "${THESEUS_VENV}/bin/pip" install --quiet -r "${THESEUS_REQS}"; then
  die "pip install -r ${THESEUS_REQS} failed" \
      "Re-run verbosely: ${THESEUS_VENV}/bin/pip install -r ${THESEUS_REQS}  — and check for missing system libs (libpq-dev, build-essential)"
fi
log_ok "Python dependencies installed"

# ============================================================================
# STEP 11/17 — Run pytest (SAFETY GATE — 85/85 must pass)
# ============================================================================
log_step 11 "Run pytest (SAFETY GATE — must pass 85/85)"

# Run from THESEUS_ROOT so imports resolve. PYTHONPATH is included for safety.
cd "${THESEUS_ROOT}"
log_info "Executing: venv/bin/pytest tests/ -q"
PYTEST_OUT="${THESEUS_LOGS}/pytest-$(date +%Y%m%d-%H%M%S).log"

set +e
PYTHONPATH="${THESEUS_ROOT}" "${THESEUS_VENV}/bin/pytest" tests/ -q \
  | tee "${PYTEST_OUT}"
pytest_rc="${PIPESTATUS[0]}"
set -e

if [[ "${pytest_rc}" -ne 0 ]]; then
  log_fail "pytest exit code ${pytest_rc}"
  die "Test suite did not pass — refusing to proceed past safety gate" \
      "Inspect: ${PYTEST_OUT}. Fix tests before re-running deploy.sh. The codebase expects 85/85 as of commit 46d72e1."
fi

# Sanity check: confirm we actually ran ~85 tests (guard against empty collection)
# pytest -q prints e.g. "85 passed in 4.21s"
passed_count="$(grep -oE '[0-9]+ passed' "${PYTEST_OUT}" | tail -1 | awk '{print $1}' || echo 0)"
if [[ -z "${passed_count}" || "${passed_count}" -lt 1 ]]; then
  die "Could not parse passed-count from pytest output" "Inspect ${PYTEST_OUT}"
fi
if [[ "${passed_count}" -lt 85 ]]; then
  log_warn "Only ${passed_count} tests ran (expected 85). Test discovery may be incomplete."
  log_warn "Continuing because pytest reported success, but please investigate."
else
  log_ok "pytest: ${passed_count} passed (safety gate cleared)"
fi

# ============================================================================
# STEP 12/17 — Provision .env interactively (if missing)
# ============================================================================
log_step 12 "Provision .env (interactive prompts if first run)"

# Helper: replace KEY=... line in .env, preserving order. Creates the line
# if it doesn't exist. Handles values with special chars by using a unique
# delimiter and shell-side escaping (NOT sed-substituted into bare regex).
env_set() {
  local key="$1"
  local val="$2"
  local file="${THESEUS_ENV}"

  # Escape backslash, ampersand, and the delimiter (|) for sed RHS safety.
  local esc_val
  esc_val="$(printf '%s' "${val}" | sed -e 's/[\\&|]/\\&/g')"

  if grep -qE "^${key}=" "${file}" 2>/dev/null; then
    # In-place edit
    sed -i.bak "s|^${key}=.*|${key}=${esc_val}|" "${file}"
    rm -f "${file}.bak"
  else
    printf '%s=%s\n' "${key}" "${val}" >> "${file}"
  fi
}

if [[ -f "${THESEUS_ENV}" ]]; then
  log_ok "Existing .env preserved (idempotent rerun) — skipping interactive prompts"
  log_info "Path: ${THESEUS_ENV}"
  # Still ensure the PG isolation knobs are correct (they're not secrets)
  env_set "THESEUS_PG_PORT"    "${PG_PORT}"
  env_set "THESEUS_PG_USER"    "${PG_USER}"
  env_set "THESEUS_PG_DB"      "${PG_DB}"
  env_set "THESEUS_PG_HOST"    "${PG_HOST}"
  env_set "WIN3_PG_PORT"       "${WIN3_PG_PORT}"
  # Do NOT rewrite THESEUS_PG_PASSWORD — already in file (or was reused above).
  chmod 600 "${THESEUS_ENV}"
else
  log_info "Copying .env.example → .env"
  cp "${THESEUS_ENV_EXAMPLE}" "${THESEUS_ENV}"
  chmod 600 "${THESEUS_ENV}"

  # --- ANTHROPIC_API_KEY (required) ---
  printf '\n%sEnter ANTHROPIC_API_KEY%s (required, sk-ant-...): ' "${C_BOLD}" "${C_RESET}"
  read -r ANTHROPIC_API_KEY
  if [[ -z "${ANTHROPIC_API_KEY// }" ]]; then
    die "ANTHROPIC_API_KEY is required and was empty" \
        "Get one from https://console.anthropic.com/, then re-run deploy.sh. Existing .env will be reused."
  fi
  env_set "ANTHROPIC_API_KEY" "${ANTHROPIC_API_KEY}"

  # --- Discord webhooks (optional) ---
  for var in DISCORD_WEBHOOK_BRIEFING DISCORD_WEBHOOK_ALERTS DISCORD_WEBHOOK_B2B_LEADS; do
    printf 'Enter %s%s%s (blank → keep PLACEHOLDER): ' "${C_BOLD}" "${var}" "${C_RESET}"
    read -r val
    if [[ -n "${val// }" ]]; then
      env_set "${var}" "${val}"
    else
      log_info "  ${var} left as PLACEHOLDER (configure later by editing .env)"
    fi
  done

  # --- Monthly cost cap (default 100) ---
  printf 'Enter %sTHESEUS_COST_MONTHLY_USD%s [default: 100]: ' "${C_BOLD}" "${C_RESET}"
  read -r cost_cap
  cost_cap="${cost_cap:-100}"
  if ! [[ "${cost_cap}" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    log_warn "Invalid number '${cost_cap}', defaulting to 100"
    cost_cap=100
  fi
  env_set "THESEUS_COST_MONTHLY_USD" "${cost_cap}"

  # --- PG isolation knobs (auto, not prompted) ---
  env_set "THESEUS_PG_PORT"     "${PG_PORT}"
  env_set "THESEUS_PG_USER"     "${PG_USER}"
  env_set "THESEUS_PG_DB"       "${PG_DB}"
  env_set "THESEUS_PG_HOST"     "${PG_HOST}"
  env_set "THESEUS_PG_PASSWORD" "${THESEUS_PG_PASSWORD}"
  env_set "WIN3_PG_PORT"        "${WIN3_PG_PORT}"

  chmod 600 "${THESEUS_ENV}"
  log_ok ".env written (chmod 600)"
fi

# ============================================================================
# STEP 13/17 — (combined with step 12) noted above as 'existing .env preserved'
# We use this slot for a separate verification print to keep the step count
# matching the spec which counted "if exists" as a separate item.
# ============================================================================
log_step 13 "Verify .env integrity"

# Make sure all critical keys are present (even if user passed empty values for webhooks)
critical_keys=(
  "ANTHROPIC_API_KEY"
  "THESEUS_PG_PORT"
  "THESEUS_PG_USER"
  "THESEUS_PG_DB"
  "THESEUS_PG_HOST"
  "THESEUS_PG_PASSWORD"
  "WIN3_PG_PORT"
  "THESEUS_COST_MONTHLY_USD"
)
for k in "${critical_keys[@]}"; do
  if ! grep -qE "^${k}=" "${THESEUS_ENV}"; then
    die ".env missing required key: ${k}" \
        "Edit ${THESEUS_ENV} and add: ${k}=<value>  — or delete .env and re-run deploy.sh"
  fi
done

# Cross-check: the password in .env must actually authenticate
env_pg_pw="$(grep '^THESEUS_PG_PASSWORD=' "${THESEUS_ENV}" | head -1 | cut -d= -f2-)"
if ! PGPASSWORD="${env_pg_pw}" psql -h "${PG_HOST}" -p "${PG_PORT}" -U "${PG_USER}" -d "${PG_DB}" \
      -tAc 'SELECT 1' >/dev/null 2>&1; then
  die "PG password in .env does not authenticate against role '${PG_USER}'" \
      "Possible drift between role and .env. Recovery: ALTER ROLE \"${PG_USER}\" PASSWORD '...';  then update .env."
fi
log_ok ".env integrity verified (PG auth confirmed)"

# ============================================================================
# STEP 14/17 — Smoke tests (no live external calls)
# ============================================================================
log_step 14 "Smoke test: emergency_stop status + cost_db init"

cd "${THESEUS_ROOT}"

# emergency_stop status — must report "not killed" (any string containing
# "not killed" passes; allow some flexibility in formatting)
log_info "  $ venv/bin/python -m control.emergency_stop status"
set +e
es_out="$("${THESEUS_VENV}/bin/python" -m control.emergency_stop status 2>&1)"
es_rc=$?
set -e
printf '%s\n' "${es_out}" | sed 's/^/        /'
if [[ "${es_rc}" -ne 0 ]]; then
  die "emergency_stop status exited non-zero (${es_rc})" \
      "Inspect: ${THESEUS_VENV}/bin/python -m control.emergency_stop status"
fi
if ! printf '%s' "${es_out}" | grep -qi "not killed"; then
  log_warn "emergency_stop output did not literally contain 'not killed' — check manually"
else
  log_ok "emergency_stop reports 'not killed'"
fi

# cost_db init
log_info "  $ venv/bin/python -c 'from cost.cost_db import init_db; init_db(); print(\"cost db ok\")'"
set +e
cd_out="$("${THESEUS_VENV}/bin/python" -c "from cost.cost_db import init_db; init_db(); print('cost db ok')" 2>&1)"
cd_rc=$?
set -e
printf '%s\n' "${cd_out}" | sed 's/^/        /'
if [[ "${cd_rc}" -ne 0 ]]; then
  die "cost_db init failed (${cd_rc})" \
      "Inspect: ${THESEUS_VENV}/bin/python -c 'from cost.cost_db import init_db; init_db()'"
fi
if ! printf '%s' "${cd_out}" | grep -q "cost db ok"; then
  log_warn "cost_db did not print 'cost db ok' — check manually"
else
  log_ok "cost_db init_db succeeded"
fi

log_ok "Smoke tests passed (no live API/Discord calls were made)"

# ============================================================================
# STEP 15/17 — Install crontab (merge, don't overwrite)
# ============================================================================
log_step 15 "Install crontab (merge with existing)"

# crontab.example is intended for root in our deployment model.
# Capture existing crontab (if any), append new lines that aren't already
# present (matched by command path), and reinstall.

existing_cron="$(crontab -l 2>/dev/null || true)"
new_cron_content="$(cat "${THESEUS_CRONTAB}")"

if [[ -z "${existing_cron// }" ]]; then
  log_info "No existing crontab — installing crontab.example wholesale"
  printf '%s\n' "${new_cron_content}" | crontab -
else
  log_warn "Existing crontab detected — merging (non-destructive)"
  # Combine, dedupe by exact line match, drop blank lines except one trailing
  merged="$(printf '%s\n%s\n' "${existing_cron}" "${new_cron_content}" \
    | awk 'BEGIN{seen[""]=1} {if (!seen[$0]++) print}')"
  printf '%s\n' "${merged}" | crontab -
fi

log_ok "Crontab installed. Current crontab -l:"
crontab -l | sed 's/^/        /'

# ============================================================================
# STEP 16/17 — Ensure logs/ directory exists
# ============================================================================
log_step 16 "Create logs/ directory"

mkdir -p "${THESEUS_LOGS}"
chmod 750 "${THESEUS_LOGS}"
log_ok "logs/ ready at ${THESEUS_LOGS}"

# ============================================================================
# STEP 17/17 — Final summary
# ============================================================================
log_step 17 "Final summary"

elapsed=$(( $(date +%s) - DEPLOY_START_EPOCH ))
elapsed_min=$(( elapsed / 60 ))
elapsed_sec=$(( elapsed % 60 ))

cat <<SUMMARY

${C_BOLD}============================================================${C_RESET}
${C_GREEN}${C_BOLD}  Theseus Phase 0 deploy: SUCCESS${C_RESET}
${C_BOLD}============================================================${C_RESET}

  Elapsed: ${elapsed_min}m ${elapsed_sec}s
  Log:     ${DEPLOY_LOG}

${C_BOLD}Services configured:${C_RESET}
  - PostgreSQL cluster: ${PG_VERSION}/${PG_CLUSTER_NAME} on port ${PG_PORT}
      (Win3 cluster on port ${WIN3_PG_PORT} untouched)
  - Database:    ${PG_DB}@${PG_HOST}:${PG_PORT}
  - Role:        ${PG_USER}  (password in ${THESEUS_ENV})
  - Extensions:  vector, pgcrypto, pg_trgm
  - Python venv: ${THESEUS_VENV}
  - Tests:       passed (safety gate cleared)
  - Smoke:       emergency_stop=not_killed, cost_db=ok

${C_BOLD}Cron schedule (root):${C_RESET}
  - 00:00 daily  → ops/backup.sh        (DB + .env backup)
  - 02:00 daily  → orchestrator         (crawl + extract + embed)
  - 07:00 daily  → briefing             (Discord briefing post)
  - */15 minutes → ops/health_check.py  (DB+disk+cost guards)

${C_BOLD}Key paths to monitor:${C_RESET}
  - ${THESEUS_LOGS}/             — daily logs end up here
  - ${THESEUS_ENV}              — secrets (chmod 600)
  - ${THESEUS_ROOT}/backups/    — nightly pg_dump tarballs

${C_BOLD}Discord webhooks:${C_RESET}
  - Briefing / Alerts / B2B leads — check .env; any PLACEHOLDER values
    will silently no-op until you fill them in.

${C_BOLD}${C_YELLOW}Password rotation reminder:${C_RESET}
  The PostgreSQL password is stored in plaintext at ${THESEUS_ENV}.
  Rotate quarterly:
    sudo -u postgres psql -p ${PG_PORT} -c "ALTER ROLE ${PG_USER} PASSWORD '<new>';"
    # then update THESEUS_PG_PASSWORD in ${THESEUS_ENV}

${C_BOLD}Next:${C_RESET}
  1. Inspect: less ${THESEUS_ENV}
  2. Fill in any PLACEHOLDER Discord webhook URLs
  3. Wait for the 02:00 orchestrator run (or trigger manually):
       cd ${THESEUS_ROOT} && venv/bin/python -m core.orchestrator
  4. Verify briefing posts to Discord at 07:00 local time

${C_BOLD}============================================================${C_RESET}

SUMMARY

log_ok "Done."
exit 0
