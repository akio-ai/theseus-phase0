# Decisions

> **Official state document.** A decision log of record.
> Only decisions that have actually been made are recorded here — no discussion, no options,
> no proposals. Proposals live in [`NEXT_ACTIONS.md`](NEXT_ACTIONS.md).
>
> **Authority:** decisions marked *Akio* were made by Akio. Decisions marked *Execution* were
> made inside the standing autonomous-execution scope and are recorded so they can be reversed
> deliberately rather than discovered accidentally.
>
> Related: [`../ai/ceo_decisions.md`](../ai/ceo_decisions.md) is an empty template and records
> nothing. This file does not replace ADRs; architecture decisions belong in ADRs.

---

## D-2026-08-05-01 — Research Layer is committed; canonical is not

**Date** 2026-08-05 · **Authority** Akio · **Status** Applied

**Decision.** Commit the Research Layer. Do not commit canonical.

**Applied as.** Branch `research/producer-layer-batch1-3` @ `cc9c1e1`, branched from
`origin/main` @ `30d90d1`. Staged with explicit paths only. `migration/` (the canonical DB) is
gitignored on this branch; `intake/` left untracked. Not pushed at the time of this decision;
push and PR were approved separately — see **D-2026-08-05-04**.

**Reason.** The Research Layer precedes canonical promotion by design. Keeping the two apart in
version control preserves that boundary rather than relying on discipline.

---

## D-2026-08-05-02 — `research/producers/_sources/` stays out of git history

**Date** 2026-08-05 · **Authority** Execution · **Status** Applied · **Reversible**

**Decision.** Gitignore the 296MB raw source cache (third-party HTML and PDF captures, largest
single file 76MB). Commit the dossiers, the conflicts register and the t-01 workspace.

**Reason.** Three reasons, in order. (1) Provenance does not depend on it — every dossier's
`## Sources` section carries the URLs, and the cache is reproducible from them. (2) The
asymmetry: adding the cache later costs one command, while removing it later requires rewriting
shared history. (3) The cache is third-party copyrighted material (producer brochures, press
kits) redistributed by a repository rather than merely read locally.

**Reversal.** Delete the `research/producers/_sources/` line from `.gitignore` and commit. The
files are intact on disk.

---

## D-2026-08-05-03 — `docs/state/` is the official state record

**Date** 2026-08-05 · **Authority** Akio · **Status** Applied

**Decision.** `docs/state/CURRENT_STATE.md`, `NEXT_ACTIONS.md` and `DECISIONS.md` are the
project's official state documents, populated from verified repository state.

**Consequence.** `docs/ai/project_state.md` (last updated 2026-07-30, still recording Phase
3B-U2) is **superseded**. It has not been deleted. `docs/ai/work_queue.md` remains a lagging
mirror; the GitHub Project remains the execution source of truth for Status / Gate / Health.

**Verification rule.** Every SHA and PR state in these files is resolved with `git rev-parse`
after `git fetch --all`, and `gh pr list`, at the time of writing. **Do not populate them from
memory.** Applying this rule on 2026-08-05 corrected PR #10's head from `8d42c47` to `601a2ba`.

---

## D-2026-08-05-06 — Batch 5 does not start until approved

**Date** 2026-08-05 · **Authority** Akio · **Status** In force

**Decision.** Batch 4 is closed. Batch 5 is proposed but **must not begin** until Akio approves.
The Bordeaux batch is separately proposed and explicitly **not** started.

**Reason.** Standing rule of the producer research workflow: after a batch completes, report,
propose, and stop. Never auto-advance.

---

## D-2026-08-05-05 — Batch 4 runs on six named producers; Bordeaux waits

**Date** 2026-08-05 · **Authority** Akio · **Status** Applied

**Decision.** Research, in order: Pride Mountain, Grgich Hills, Dujac, Jacques-Frédéric Mugnier,
Denis Mortet, De Montille. Keep all existing research rules. Do not begin the Bordeaux batch, do
not modify canonical, do not begin ADR-002, **do not resolve canonical conflicts**.

**Outcome.** Six dossiers delivered, all at `reached_70: YES` (four at High confidence). OBP
coverage **204 → 256 of 704 bottles (29% → 36.4%)**. Canonical untouched. **No new canonical
conflict was registered** — the one duplicate found (Denis Mortet's two `Lavaux-Saint-Jacques`
cuvée records) is already registered as **C-3**, so the dossier adds primary-source evidence to
the existing entry rather than opening a new one.

---

## D-2026-08-05-04 — The Research Layer branch is pushed and reviewed as one PR

**Date** 2026-08-05 · **Authority** Akio · **Status** Applied

**Decision.** Push `research/producer-layer-batch1-3` and open a single PR containing the producer
dossiers, the canonical conflict register, the t-01 workspace, and the three `docs/state/`
documents — and nothing else. Exclude canonical data, `migration/`, `intake/`, and
`research/producers/_sources/`.

**Applied as.** **PR #5** → `main` (base `30d90d1`).
Verified: `git log --name-only origin/main..HEAD | grep -E "^(migration|intake)/"` returns nothing,
and the PR file list contains no excluded path. The PR description states, as required, that
canonical is unchanged, that the raw source cache is intentionally excluded, that the research
layer is non-canonical, and how to roll back each layer.

---

## D-2026-08-04-01 — Producer research runs in parallel batches of 5–6

**Date** 2026-08-04 · **Authority** Akio · **Status** In force · **Supersedes** one-at-a-time

**Decision.** Research producers in parallel batches of 5–6, presented to Akio per batch.

**Reason.** OBP's coverage curve is flat: **69 producers are needed to cover 70% of bottles**
(17 for 30%, 39 for 50%). Depth on the top few producers structurally cannot get there.

---

## D-2026-08-04-02 — Completeness bar is 70%, not 100%

**Date** 2026-08-04 · **Authority** Akio · **Status** In force

**Decision.** Ship a dossier at ~70% and move on; add depth later. Breadth over depth.

**70% means a sommelier can speak about the producer on the floor without saying anything
false.** Required: Identity / Overview / Location / **Farming** / Important Cuvées with OBP
linkage / the three core Staff Notes / ⚠️ **the must-not-say list**. Deferrable: History detail,
winemaking numbers (new-oak %, MLF, yeast, bâtonnage), third-party scores, per-parcel hectares.

**Corollary.** The thinner the dossier, the more important the ⚠️ list — thin records are the
ones improvised around on the floor. `## Sources` and `## Open Questions` are filled even at 70%.
`## Akio's Insight` is always left empty.

---

## D-2026-08-04-03 — Canonical conflicts are escalated, never resolved

**Date** 2026-08-04 · **Authority** Akio · **Status** In force

**Decision.** When multiple canonical records appear to point at the same producer or cuvée:
do not pick one, do not rewrite canonical, open a `## Canonical Conflict` section and report six
items — conflicting IDs, why it looks duplicated, evidence, OBP impact, recommended resolution
(**not executed**), confidence.

**Reason.** A canonical conflict is an architecture problem, not a research problem.

**Register.** `research/canonical_conflicts/REGISTER.md` — **20 true conflicts** and 54 false
positives (colour variants, different appellations, different châteaux) separated so the
screening is not redone every time. A batch that rediscovers an existing entry adds evidence to
it; it does not open a new number.

---

## D-2026-08-04-04 — `## Akio's Insight` is Akio's alone

**Date** 2026-08-04 · **Authority** Akio · **Status** In force

**Decision.** Never write, replace, summarize or "improve" the `## Akio's Insight` section. It
is a separate layer from sourced fact and is left empty until Akio fills it.

**Related standing rules.** Do not invent facts. Never mix the four evidence layers (verified
fact / source-derived / Akio's professional insight / unresolved question). Do not delete
uncertain information — mark the uncertainty and keep it. Official sources only; **Wikipedia is
prohibited outright**; when no official source exists, record "awaiting material from the team".

---

## Template

```
## D-YYYY-MM-DD-NN — <one-line decision>

**Date** YYYY-MM-DD · **Authority** Akio | Execution · **Status** Applied | In force | Reversed

**Decision.** What was decided, in the imperative.

**Reason.** Why. If it was a trade-off, name what was traded away.

**Applied as / Reversal.** Where it landed; how to undo it.
```

## Last Updated

2026-08-05 (updated after Batch 4)
