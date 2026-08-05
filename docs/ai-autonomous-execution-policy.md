# AI Autonomous Execution Policy

> **Official policy document.** Standing rules for autonomous execution on THÉSEUS.
> Created 2026-08-05 to hold the **Research Verification Policy** (`D-2026-08-05-13`); no document
> of this kind previously existed in the repository.
>
> Related: [`state/DECISIONS.md`](state/DECISIONS.md) is the decision log of record;
> [`ai/github_projects_operations.md`](ai/github_projects_operations.md) holds the Status/Gate
> execution boundary. This document does not replace either.

---

## Research Verification Policy

**Status** In force · **Authority** Akio · **Decision** `D-2026-08-05-13` · **Date** 2026-08-05

**Default for all future Producer Research batches.**

### The rule

> **Verify only the scope that changed.**

Verification exists to protect quality. It is not an occasion to re-audit the repository.

### Always verify

Every batch, no exceptions:

| Check | What it means |
|---|---|
| **Required dossier structure** | The fixed heading sequence, unchanged and in order: `# Producer` → `## Identity` → `## Overview` → `## History` → `## Location` → `## Farming` → `## Winemaking` → `## Style` → `## Important Cuvées` → `## Staff Notes` → `## Akio's Insight` → `## Canonical Conflict` → `## Sources` → `## Confidence` → `## Open Questions` |
| **Required sections** | Present and filled to the 70% bar — Identity, Overview, Location, Farming, Important Cuvées with OBP linkage, Staff Notes' 芯 3 点, and the ⚠️ must-not-say list. `## Sources`, `## Confidence` and `## Open Questions` filled regardless of depth. **`## Akio's Insight` left unwritten.** |
| **Canonical remains untouched** | The canonical DB was not written to |
| **`REGISTER.md` remains untouched** | Unless conflicts were **deliberately adjudicated** as part of this task |

### Do not repeatedly perform

Unless the current task **explicitly modifies** those areas:

- repository-wide `git` inspection
- repository-wide integrity sweeps
- repeated `REGISTER.md` verification
- repeated mtime verification
- repeated canonical-wide scans

### Why this changed

Producer Research has matured. Broad audits were correct while the workflow was being
established — they are what caught the look-alike-site trap, the intake↔mapping divergence, and
the untrustworthy `obp_note` prose. By Batch 9 they were mostly **re-proving stable facts**:
canonical had not been written to in nine consecutive batches, and each re-verification cost
tokens that bought no new information.

**Objective: reduce unnecessary token consumption while preserving quality.**

### What is traded away

Drift *outside* the changed scope is caught later rather than immediately — for example, a
canonical edit made by another workstream between batches. This is accepted because canonical
writes require CEO approval and would be announced, and because the always-verify list still
covers the one failure that would actually corrupt the Research Layer.

### Scope

This policy governs **checking, not writing.** It relaxes no research rule. Still in force,
unchanged:

- Do not invent facts; preserve uncertainty rather than deleting it
- Never mix the four evidence layers (verified fact / source-derived / Akio's insight / unresolved)
- Official sources only; **Wikipedia is prohibited outright**
- A site is not treated as official until its authenticity is checked (`D-2026-08-05-09`)
- **`## Akio's Insight` is Akio's alone** (`D-2026-08-04-04`)
- **Canonical is read-only; conflicts are escalated, never resolved** (`D-2026-08-04-03`)
- The 70% completeness bar (`D-2026-08-04-02`)
- Report, propose, **stop**. Never auto-advance to the next batch (`D-2026-08-05-06`)

---

## Last Updated

2026-08-05
