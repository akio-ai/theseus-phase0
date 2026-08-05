# Current State

> **Official state document.** Populated from verified repository state on **2026-08-05**
> (updated the same day after Batch 4).
> Every SHA below was resolved with `git rev-parse` after `git fetch --all`, and every PR
> with `gh pr list`, on the date above. Nothing here is carried over from memory unverified.
>
> This file supersedes [`../ai/project_state.md`](../ai/project_state.md), which is **stale**
> (last updated 2026-07-30, still records Phase 3B-**U2** as the current unit).

## Repositories

⚠️ **The project spans two repositories.** Identify with `git remote -v` and `git fetch`
before searching for a file. Assuming a single repo has previously produced false
"file not found" reports.

| Repo | Local path | Purpose |
|---|---|---|
| `akio-ai/theseus-phase0` | `~/Theseus_Phase0` | Governance docs, migration/canonical pipeline, **Research Layer** |
| `akio-ai/theseus-project` | `~/Theseus_Project` | The application. `main` auto-deploys to production |

### `theseus-phase0` — verified refs (2026-08-05)

| Ref | SHA | Note |
|---|---|---|
| `origin/main` | `30d90d1` | Baseline |
| `origin/docs/ai-autonomous-execution-policy` | `625f8ea` | **PR #4 open** → `main` |
| `research/producer-layer-batch1-3` | `6b4cc30` → | **PR #5 open** → `main`. Research Layer + `docs/state/`. Batch 4 commits sit on the same branch |

Untracked and deliberately **not** committed: `migration/` (canonical DB — gitignored on the
research branch), `intake/`, `research/producers/_sources/` (source cache — gitignored).

### `theseus-project` — verified refs (2026-08-05)

| Ref | SHA | Note |
|---|---|---|
| `origin/main` | `c9f3897` | **Unchanged.** Production auto-deploy target. ARIADNE not yet shipped here |
| `origin/integration/ariadne-current-main` | `c4ddde1` | Phase 3B U1+U2+U3 + specification system |
| `origin/feature/ariadne-hybrid-ui` | **`601a2ba`** | **PR #10 open**, base = `integration/...`, not draft |
| `origin/feature/phase3b-u3` | `450f44a` | Merged via PR #9 |

🔴 **PR #10's head is `601a2ba`.** Earlier notes recorded `8d42c47`; that is out of date.

Local worktrees exist under session scratchpad directories; three are marked **prunable**
(`ariadne-integration` @ `58f2bd9`, `u3-impl` @ `450f44a`, `ariadne-audit` @ `2ab6841`).
The working checkout `~/Theseus_Project` sits on `feature/theseus-logo-mark` @ `cd03b3f`
with modified icon assets in the working tree.

## Active workstream — Producer Research Layer

**Status: Batch 4 complete. Awaiting approval before Batch 5.**

| | |
|---|---|
| Dossiers | **26** — `research/producers/*.md` |
| OBP coverage | **256 / 704 bottles (36.4%)** — Batch 4 added **+52 bottles (+7.4 pts)** |
| Remaining | **160 producers / 448 bottles** |
| Conflicts register | `research/canonical_conflicts/REGISTER.md` — 20 true conflicts, 54 false positives separated. **Batch 4 added no new entries** (it confirmed C-3 with primary-source evidence) |
| Canonical writes | **Zero.** Read-only throughout |

| Batch | Producers |
|---|---|
| Pre-batch (2) | Domaine Leflaive, Louis Latour |
| Batch 1 (5) | DRC, Faiveley, Simon Bize et Fils, Château Lafite-Rothschild, Jean-Louis Chave |
| Batch 2 (7) | Doyard, Dunoyer de Segonzac, Larmandier-Bernier, Les Monts Fournois, Michel Gonet, Pascal Agrapart, Pierre Péters |
| Batch 3 (6) | Egly-Ouriet, Drappier, Pierre Gimonnet & Fils, Laherte Frères, Jérôme Prévost, Frédéric Savart |
| **Batch 4 (6)** | **Pride Mountain Vineyards, Grgich Hills Estate, Domaine Dujac, Jacques-Frédéric Mugnier, Domaine Denis Mortet, Domaine de Montille** |

**Batch 4 notes.** Two producers (Pride Mountain, Grgich Hills) had **no canonical producer record at
all** — 18 OBP bottles were `producer_state = unresolved` purely for that reason. Both US dossiers
reached **High** confidence because both wineries publish per-vintage technical data. Two structural
findings are recorded in the dossiers and **not acted on**: Pride Mountain's appellation string
changes per vintage (`64% Napa / 36% Sonoma` / `Napa County` / `Napa Valley`), which the current
one-subregion-per-cuvée model cannot express; and de Montille's four Corton rows stall at
`candidate` on a single character (`Clos de Roi` vs `Clos du Roi`).

Governing workflow: fixed template, **70% completeness bar**, four evidence layers never mixed
(verified fact / source-derived / Akio's insight / unresolved), `## Akio's Insight` is
**Akio-only and never written or rewritten by anyone else**, official sources only
(Wikipedia prohibited), canonical duplicates are **escalated, never resolved**.

## Paused workstream — ARIADNE Phase 3B

- Phase 3B **U3 complete**, merged via PR #9. **U4 not started.**
- **PR #10 (Hybrid UI) is open and unmerged.**
- The aroma-selection redesign (Fruit Basket Explore/List) is **prototype only** — neither PR #10
  nor the DB was touched by it.
- **U4's decisive branch point is the Application Cutover Gate (AQ-3)** — irreversible after the
  first real observation is written.

## Blockers

Everything below is **waiting on Akio**, not on execution capacity. See
[`NEXT_ACTIONS.md`](NEXT_ACTIONS.md).

1. Batch 5 approval (producer research)
2. Review / merge of PR #5
3. Hero artwork confirmation (ARIADNE)
4. Schema-change permission (aroma intensity / complexity / 11-family taxonomy — all need migrations)
5. Fruit Basket: ship or not
6. `Les Hautes Mottes 2018` — physical bottle or importer sheet needed

## Operating constraints in force

- **No push without CEO approval.** Commit freely; do not push.
- **Never `--amend` on a shared repo.** Verify HEAD is your own commit first.
- `git add -A`, `git clean -fdx`, `rebase`, force-push are **prohibited**. Explicit paths only.
- PRs reference `Tracks #N`; **`Closes` is prohibited**.
- **Done** = merged **and** validated **and** documentation updated **and** acceptance criteria met.
- Project field writes are not granted; report required transitions instead.
- **This machine has no `node`.** Run JS/tests with `jsc`.
- `gh` can silently switch active account → `gh auth status` → `gh auth switch --user akio-ai`
  → `gh auth setup-git`.
- `docs/specifications/` TEMPLATE / style-guide / README are **frozen**; changes require an ADR.

## Last Updated

2026-08-05
