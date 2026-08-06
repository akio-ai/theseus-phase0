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

## D-2026-08-06-07 — Batch 14 closed Batch 13's remainder and extended by two on restaurant value

**Date** 2026-08-06 · **Authority** Execution · **Status** Done · **Scope** Batch 14 only

**Decision.** Phase 14 ran **six** producers, not four. The four named in the resume order
(**Dom Pérignon, Turley, Dominus Estate, Chappellet**) close Batch 13. Two further producers
(**Château-Figeac, Promontory**) were added to keep the agent pool at its cap rather than idle,
selected on the standing selection priority — **highest restaurant value first**. Promontory is
**$10,740 across three rows**, by a wide margin the most expensive producer remaining on the menu;
Figeac is **$3,920 across three** and extends the Bordeaux block already completed in Batch 12.

**Why this was execution's call, not Akio's.** `D-2026-08-06-06` §7 removed the per-batch approval
gate, and the instruction for Phase 14 was *continue Producer Research* with a resume **priority
order**, not a fixed count. Adding producers of the same type, from the same standing selection
criteria, is continuation rather than scope expansion. It is recorded here so it can be reversed
deliberately.

**Concurrency.** Held at **3 agents** throughout, per `D-2026-08-06-06` §4. A freed slot was
refilled twice; after the sixth producer launched, the last free slot was **left empty** rather
than extended a third time, so the batch closes at a size consistent with Batches 8–13.

**Result.** **6 of 6 cleared the 70% bar. Zero sub-bar dossiers** — the third such batch, after
Batches 4, 10 and 12. Coverage **521 → 539 / 704 (74.0% → 76.6%)**; dossiers **78 → 84**; the
binding producer criterion **78/182 → 84/182 (42.9% → 46.2%)**.

**The Batch 9 precedent held for a third time.** Dom Pérignon (28 MB / 449 files) and Turley
(2.4 MB / 14 files) were written from their existing caches with **no research sweep**, exactly as
Hundred Acre / Abreu / Bergström were. **A spend-limit stop costs the writing pass, not the
research.** This is no longer a prediction; it is a measured pattern with two independent
confirmations. Turley's cache is the sharper demonstration: `page_trade-assets.html`, already on
disk, held the URLs of the official tech-sheet PDFs for the exact 2023 vintages on the menu.

**Caches were left byte-intact** (Turley's 14 original files retain their 11:08 mtimes). Four new
caches were built — `dominus-estate` (131 files / 54 MB), `chappellet` (85 / 13 MB),
`chateau-figeac` (74), `promontory` (51) — so a future stop again costs only writing.

---

## D-2026-08-06-06 — Research runs to completion; engineering defects go to Codex

**Date** 2026-08-06 · **Authority** Akio · **Status** In force · **Scope** Permanent, from Batch 13

**Decision.** Seven standing workflow adjustments, adopted before Batch 13. They change **operations
only**. The research methodology — the fixed template, the 70% bar, the four-layer separation, the
no-invention rule, official-sources-only, the site-authenticity pre-check, canonical read-only, and
escalation-not-resolution for conflicts — is **unchanged**.

1. **Producer Research continues, and it is the highest priority.** Research does **not** pause for
   matcher work, canonical cleanup, or repository-wide investigations.
2. **`CURRENT_STATE.md`'s completion criteria (`D-2026-08-06-05`) remain the definition of done.**
   Completeness is measured by **producer completion**, not by wine-level resolution.
3. **A matcher defect is not a reason to stop.** Record it when it is encountered naturally in the
   course of a dossier. Do **not** investigate it further.
4. **Any pipeline, matcher, mapping or canonical implementation defect that is not required to
   complete the dossier in hand is filed as a separate engineering task for Codex** —
   `docs/state/CODEX_TASKS.md`. No further research time is spent on it.
5. **Maximum 3 concurrent producer agents; prefer 2–3.** Raising it requires explicit approval.
6. **Verification policy is unchanged: verify only the scope that changed.** Never run
   repository-wide verification unless explicitly requested (`D-2026-08-05-13`).
7. **The primary objective is completing the Producer Research Layer.** Everything else is
   secondary until it is complete.

**What this supersedes.**

- 🔴 **`D-2026-08-06-03` is reversed on the concurrency figure.** Batch 12 ran at **8** concurrent
  agents and that decision recorded higher parallelism as validated. Adjustment 5 caps it at **3**.
  The Batch 12 *finding* — that independent producer research does not contaminate across agents —
  stands; the **operating limit** does not.
- 🔴 **`NEXT_ACTIONS.md` §1's three-way choice is decided.** It offered Shape C (data-integrity),
  the `Krug`/`Dom Pérignon` register-adjudication route, and a conventional producer batch, and held
  the choice for Akio. Adjustments 1 and 7 select **producer research**. **Shape B and Shape C are
  deferred**; the parts of them that are engineering work are filed under adjustment 4.
- ⚠️ **The standing "nothing auto-advances" rule (`policy_producer_research_workflow`) is narrowed,
  not removed.** Research continues without a per-batch approval gate. What still requires Akio are
  the things that were always outside execution scope: canonical writes, `REGISTER.md`
  adjudication, remote git operations, and raising concurrency above 3.

**Reason.** Under `D-2026-08-06-05` the binding constraint is criterion 1 — **76 / 182 producers
(41.8%)**, with 106 remaining. Every defect the workstream has surfaced sits downstream of the
Research Layer and none of them block a dossier from being written. Batches 8–12 progressively
shifted attention toward those defects; this decision puts it back.

**Consequence for the label-null override.** It remains the highest-severity item the workstream has
produced (`NEXT_ACTIONS.md` §3h-1, 152 rows, 147 `exact`) and it is **already measured**. Under
adjustment 4 it is a **Codex task**, not a research task. Research neither studies it further nor
waits on it.

**Applied as.** Recorded here; `docs/state/CODEX_TASKS.md` created as the engineering queue;
`NEXT_ACTIONS.md` §1 updated to record that the choice is made. **No dossier, no canonical record and
no intake row was changed by this decision.**

**Reversal.** Delete this entry. Concurrency reverts to `D-2026-08-06-03`, the §1 choice reopens, and
the per-batch approval gate returns.

---

## D-2026-08-06-05 — Research Layer completion criteria

**Date** 2026-08-06 · **Authority** Akio · **Status** In force

**Decision.** The Research Layer is complete when, and only when, all three hold:

1. **Every OBP producer has a dossier.**
2. **Every OBP bottle is linked to a producer.**
3. **Every producer has a documented confidence level.**

**Unknown information is allowed. Invented information is never allowed.**
**The objective is completeness of evidence, not completeness of knowledge.**

**Reason.** These criteria are stated over *producers*, not bottles, and criterion 2 requires a
link to a **producer** — not to a cuvée, not to a vintage, not to a specific wine. That is
deliberate and it changes the completion path in two directions at once:

- **It removes the hardest blocker.** The 78 rows awaiting a physical label are *wine*-level
  identification. Criterion 2 does not ask for that, so those rows do not block completion.
  This ratifies **D-2026-08-06-04** as the general rule rather than a Bordeaux exception.
- **It moves the headline number down.** The project has been steering by *bottle* coverage
  (**515 / 704 = 73.2%**). Criterion 1 is *producer* coverage: **76 / 182 = 41.8%**. The
  remaining 106 producers cost roughly the same per dossier as the first 76 and return 189
  bottles instead of 515. The curve is flat from here and the criteria say so plainly.

**Relationship to `D-2026-08-04-02`.** Unchanged and orthogonal. The 70% bar governs *how deep a
single dossier goes*; these criteria govern *when the layer is done*. A layer of 182 dossiers all
sitting at 70% satisfies these criteria. "Completeness of evidence, not of knowledge" is the same
principle as the 70% bar, stated at layer scope.

**Consequence for the pipeline defect.** "Invented information is never allowed" is now a
completion criterion, not only a drafting rule. The Batch 12 finding is therefore in scope and
measured: the parser correctly detects *no cuvée printed* on **292 / 704** rows; on **152** of
those the matcher proposes a canonical cuvée anyway, and **147 are marked `exact`**. **0 of the
152 carry a reviewer note**; only 19 carry any `source_quality_flags`. That is invented data
published at the highest confidence tier. It sits in intake, not in the dossiers — the dossiers
are clean — but it feeds the same product and it violates criterion 3's premise.

**Applied as.** Recorded here; `NEXT_ACTIONS.md` and `CURRENT_STATE.md` report against these
three criteria. No dossier, no canonical record and no intake row was changed by this decision.

**Reversal.** Delete this entry; the layer reverts to being measured by bottle coverage alone.

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

## D-2026-08-05-07 — Batches 5, 6 and 7 are approved as one run; stop after 7

**Date** 2026-08-05 · **Authority** Akio · **Status** In force · **Supersedes** D-2026-08-05-06

**Decision.** Run Batch 5, Batch 6 and Batch 7 back to back without pausing for approval between
them, then **stop automatically after Batch 7**. All standing research rules remain in force: the
70% bar, official sources only, technical-sheet PDFs whenever available, preserve uncertainty,
`## Akio's Insight` left empty, canonical read-only, canonical conflicts escalated only, and
`docs/state/` updated after every completed batch.

**Consequence.** D-2026-08-05-06 ("Batch 5 does not start until approved") is satisfied and
superseded for these three batches only. The rule itself — report, propose, stop, never
auto-advance — resumes at the end of Batch 7.

**Batch composition.** Batch 5 was the six already proposed in `NEXT_ACTIONS.md`. Batches 6 and 7
were composed by execution from the same ranking (OBP bottles unlocked, then absence from
canonical, then restaurant importance). **Bordeaux remained excluded** — the standing "do not start
without instruction" on the Bordeaux batch was not lifted.

**Outcome.** 18 dossiers delivered, **+114 OBP bottles (245 → 359 of 704; 34.8% → 51.0%)**.
Canonical untouched. **No new conflict-register entries**; evidence added to C-1, C-4, C-5, S-2,
P-1, P-7, V-1, V-3 and V-4. **Six dossiers are deliberately below the 70% bar and marked
`awaiting material from the team`** — Ganevat, Comtes Lafon, Ramonet, Pierre-Yves Colin-Morey,
Caroline Morey, Pierre Girardin (Selosse and DuMOL are partial). Execution stopped after Batch 7 as
instructed; Batch 8 is proposed in `NEXT_ACTIONS.md`, not started.

---

## D-2026-08-05-10 — Batch 8 runs on the six proposed producers; stop after 8 unless capacity allows 9

**Date** 2026-08-05 · **Authority** Akio · **Status** Applied

**Decision.** Run **Batch 8** as the six producers already proposed in `NEXT_ACTIONS.md` —
Taittinger, Domaine Roulot, Domaine Bachelet-Monnot, Michel Niellon, Domaine de L'Arlot,
Clos de la Coulée de Serrant. On completion, **assess remaining context and usage**; continue
directly into Batch 9 only if sufficient, otherwise **stop automatically**. **Batch 10 is
prohibited.** All standing rules remain in force: the 70% bar, official sources only, technical
sheet PDFs whenever available, preserve uncertainty, never invent, `## Akio's Insight` left empty,
canonical read-only, canonical conflicts escalated only, **ADR-002 not started**, **Bordeaux batch
not started**, and `docs/state/` updated after every completed batch.

**Outcome.** 6 dossiers delivered, **+30 OBP bottles (359 → 389 of 704; 51.0% → 55.3%)**, 50
dossiers total. Canonical untouched (`db_wine_canonical.json` mtime unchanged at 2026-07-28);
`REGISTER.md` untouched. **Four cleared the bar** — L'Arlot ~88%, Coulée de Serrant ~88%,
Taittinger ~85%, Bachelet-Monnot ~75%. **Two are deliberately below it** — Roulot ~60% and Michel
Niellon ~60%, both marked `awaiting material from the team`.

**Reason the two shortfalls are not execution failures.** In both cases the absence of a
producer-authored source was **proved rather than assumed**: `domaineroulot.fr` is genuinely
registered to Domaine Guy Roulot but serves an empty OVH placeholder; Michel Niellon has no domain
at all and the village syndicat lists Instagram as the domaine's only channel. Padding either to
70% would have required inventing winemaking and style, which the standing rules forbid. **A thin
dossier with a heavy Must-Not-Say list is the correct deliverable here** — Niellon's list runs to
12 entries, the longest in the batch.

**What Batch 8 changed methodologically.** The no-official-site fallback established with Ganevat
(Agence Bio → certifier → INAO) was extended with the **French state company register**
(`recherche-entreprises.api.gouv.fr`) and the **DGFiP/Etalab cadastre**. That pairing settled
`Les Luchets` — absent from the INAO Meursault cahier des charges, therefore **not** a Premier Cru,
but present in the cadastre as a real lieu-dit. Two silent-failure traps are now on record:
**INAO extranet filename conventions differ per appellation** (hyphenated, lowercase-unhyphenated,
and fully unhyphenated forms all occur) and a wrong guess returns **HTTP 200 with HTML**; and
**Coulée de Serrant's English pages are machine translations carrying different numbers from the
French** — always take the French.

**Escalated, not resolved.** Two new IDs are **proposed only** — `C-6` (colour-axis mis-assignment)
and `P-8` (`founded_year = 1734` unsupported; the official origin is 1932). Three further shapes
were left **deliberately unnumbered** because they fit no existing family: geographic
*climat + sub-parcel* granularity, a non-year sentinel `vintage = '—'`, and classification drift
within one cuvée. **`REGISTER.md` was not written to.** Numbering is CTO's call.

**Applied as.** Six dossiers under `research/producers/`, plus the Batch 8 map in
`research/producers/coverage.py`. **Reversal** is deletion of those files; nothing else was changed.

---

## D-2026-08-05-11 — Batch 9 stops at 3 of 6; a cached source is not a dossier

**Date** 2026-08-05 · **Authority** Execution (forced) · **Status** Applied

**Decision.** Batch 9 was authorised to run directly after Batch 8 if context and usage allowed.
It ran on six producers and **stopped at three**: the **monthly API spend limit** was reached while
four agents were mid-run. **Count only the three dossiers actually written.** The three unwritten
producers are **excluded from `coverage.py`** even though their source caches are complete.

**Reason.** Coverage must mean "a sommelier can speak from this", not "bytes were fetched".
`hundred-acre` (122 cached files), `bergstrom-wines` (70) and `abreu-vineyards` (42) have full
research on disk and **no dossier**. Counting them would inflate the figure with work no one can
read. This is the same discipline as the 70% bar: **the deliverable is the dossier.**

**Outcome.** 3 dossiers delivered, **+15 OBP bottles (389 → 404 of 704; 55.3% → 57.4%)**, 53
dossiers total. Canonical untouched; `REGISTER.md` untouched. Harlan Estate ~85%, Clos de Tart
~90%, Armand Heitz ~90% — **all three cleared the bar**, supporting the proposal's hypothesis that
New World and corporate-estate producers publish enough to score higher than small Burgundian
domaines. **Armand Heitz's dossier was fully written before its agent died**; only the agent's
report back was lost, and the file was verified independently.

**Resumption is cheap and should be step 1.** All three surviving agents reported research complete
and were composing the dossier when killed. **Resuming costs the writing pass, not the research.**

**Escalated, not resolved.** A **new shape, deliberately unnumbered**: a producer/cuvée same-string
collision (Clos de Tart), where `producer` and cuvée `name` are identical and producer-name tokens
bleed into cuvée matching — `La Forge de Tart` scores 0.7143 against `Clos de Tart` on `de` + `Tart`.
A canonical-wide inventory (`Clos des Lambrays`, `Château Latour`, …) must precede numbering. Also
escalated: **`The Mascot` is a separate legal entity from Harlan Estate**, so 3 OBP rows are
misattributed; and **`Oakville Proprietary Blend` is not a cuvée name** — the third instance of the
menu printing a category word, after Mayacamas and Grgich.

**Reversal.** Deletion of the three dossiers and their `coverage.py` entries; nothing else changed.

**Superseded in part by `D-2026-08-05-14`**, which records the resumption and closes Batch 9 at 6
of 6. The prediction above held exactly: resuming cost the writing pass, not the research.

---

## D-2026-08-05-13 — Research Verification Policy: verify only the scope that changed

**Date** 2026-08-05 · **Authority** Akio · **Status** In force · **Default for all future batches**

**Decision.** Producer-research verification is **scoped to what the task changed**.

**Always verify** (every batch, no exceptions):
- required dossier structure — the fixed `# Producer` → … → `## Open Questions` heading sequence
- required sections present and filled to the 70% bar; `## Akio's Insight` left unwritten
- **canonical remains untouched**
- **`REGISTER.md` remains untouched**, unless conflicts were deliberately adjudicated in this task

**Do not repeatedly perform**, unless the current task explicitly modifies those areas:
- repository-wide `git` inspection
- repository-wide integrity sweeps
- repeated `REGISTER.md` verification
- repeated mtime verification
- repeated canonical-wide scans

**Reason.** Producer Research has matured. The broad audits were correct while the workflow was
being established — they are what caught the look-alike-site trap, the intake↔mapping divergence
and the untrustworthy `obp_note` prose. They are now mostly **re-proving stable facts**: canonical
has not been written to in nine consecutive batches, and each re-verification costs tokens that buy
no new information. **Verification should protect quality, not re-audit the whole repository.**

**What is traded away.** Drift *outside* the changed scope will be caught later rather than
immediately — for instance, a canonical edit made by another workstream between batches. Accepted:
canonical writes require CEO approval and would be announced, and the always-verify list still
covers the one thing that would actually corrupt the Research Layer.

**Applied as.** This entry; the constraint list in
[`CURRENT_STATE.md`](CURRENT_STATE.md); and
[`../ai-autonomous-execution-policy.md`](../ai-autonomous-execution-policy.md), which did not exist
in the repository and was created to hold it. Also mirrored into the standing producer-research
policy in Claude's memory, which is what loads at session start.

**Reversal.** Delete this entry and the policy document, and restore full-sweep verification. No
data is affected either way — this rule governs *checking*, not *writing*.

---

## D-2026-08-05-14 — Batch 9 resumed from cache and closed at 6 of 6

**Date** 2026-08-05 · **Authority** Akio · **Status** Applied

**Decision.** Resume **Batch 9 only** — Hundred Acre, Abreu, Bergström — from their existing
`_sources` caches, at **maximum 2 agents in parallel**. Do not restart completed research, do not
run repository-wide sweeps, do not investigate canonical prose globally, do not touch canonical or
`REGISTER.md`, and do not work the five physical-label cases. Stop when Batch 9 is closed.

**Reason.** All three agents killed by the spend limit had finished research and were composing
when they died. The cheapest remaining coverage in the entire backlog was the writing pass on work
already paid for.

**Outcome.** 3 dossiers, **+15 OBP bottles (404 → 419 of 704; 57.4% → 59.5%)**, **56 dossiers**.
All three cleared the bar: Bergström ~85%, Abreu ~82%, Hundred Acre ~78%. Caches left byte-intact;
no new research sweep was run. Canonical untouched; `REGISTER.md` untouched.

**Escalated, not resolved.**
- **Hundred Acre: 4 of 5 OBP rows are not Hundred Acre wines** — `Fortunate Son` and `Summer Dreams`
  are sibling brands of `One True Vine, LLC`, and Summer Dreams' 2025 labels file under a **separate
  legal entity**. Second instance of the Harlan/Mascot brand-axis shape in one batch. Cited to the
  **proposed** category `CAT-3 brand_axis`; no number opened, because `CAT-1`…`CAT-9` are still
  proposals awaiting adjudication.
- **Attribute provenance — a new shape, unnumbered.** Canonical gives the Hundred Acre `Ark` a
  `subregion` of `Napa Valley — Howell Mountain`; the TTB-approved label and both COLAs say
  **`NAPA VALLEY`**, and `Howell` appears in no producer source and none of 105 TTB records. Fits
  none of `P-1`…`S-4` or `CAT-1`…`CAT-9` — those are naming, layer, key-design and entity-boundary
  problems; this is an unsourced attribute.
- **Abreu is a gap, not a conflict.** Absent from canonical entirely, along with all six of its
  vineyard names. No register class covers "producer not present"; forcing one would be wrong.
- **`Cabernet Sauvignon` as a menu-side classification** (Abreu) — fourth instance of the menu
  printing a category word as fact, after Harlan, Mayacamas and Grgich.
- **Canonical `region` has no Oregon** — all 79 USA records are `California`. Blocks Bergström.
- **The intake↔mapping divergence is now four instances**, and Hundred Acre's is different in kind:
  two rows are **parse-broken in `shells.json`** with no producer at all, where the intake package
  reports `producer_state: exact`.

**Three physical-label tasks added**, bringing the floor total to eight: Hundred Acre `'Ark'` 2022's
printed appellation, Abreu's label brand and type designation, and Bergström row 5's cuvée name.
**Bergström row 5 was deliberately left unresolved** despite four converging lines of evidence
pointing to `Bergström Vineyard Pinot Noir` — indication is not a source.

**Reversal.** Delete the three dossiers and their `coverage.py` entries; coverage returns to 57.4%.

---

## D-2026-08-05-15 — Batch 10 runs on the proposed producers at max 2 concurrent agents; stop after 10

**Date** 2026-08-05 · **Authority** Akio · **Status** Applied

**Decision.** Run **Batch 10** on the producers already proposed in `NEXT_ACTIONS.md`, resolving any
priority ambiguity by (1) highest remaining OBP bottle coverage, (2) restaurant importance,
(3) availability of official sources, (4) existing source cache. **Maximum 2 concurrent producer
agents — never more without explicit approval.** Verify only the scope the batch changed
(`D-2026-08-05-13`): after each producer, dossier structure, required sections, canonical untouched.
**No repository-wide integrity sweeps and no repository-wide git inspection.** All standing research
rules remain in force: the 70% bar, official sources only, technical-sheet PDFs whenever available,
preserve uncertainty, never invent, `## Akio's Insight` left empty, canonical read-only, canonical
conflicts escalated only, **`REGISTER.md` not modified**, **ADR-002 not started**, **Bordeaux batch
not started**. Commit completed work; **do not push**. **Stop automatically after Batch 10.**

**Composition.** Famille Moussé (5 bottles), Louis Roederer, Billecart-Salmon, Laurent-Perrier,
Chateau Montelena, Olivier Leflaive Frères (4 each). The other six 4-bottle candidates — Vilmart &
Cie, Thierry Allemand, René & Vincent Dauvissat, Henri Giraud, Anne et Hervé Sigaut, Alvina Pernot —
were **deliberately excluded on criterion (3)**: none has a known producer-authored web source, so
all six carry the Roulot / Niellon profile. Selecting *for* published fiches techniques was the
batch's explicit hypothesis.

**Outcome.** 6 dossiers, **+25 OBP bottles (419 → 444 of 704; 59.5% → 63.1%)**, **62 dossiers**.
Remaining: 120 producers / 260 bottles. **All six cleared the bar and all six are Confidence High** —
Roederer ~88%, Billecart ~88%, Olivier Leflaive ~82%, Moussé ~80%, Laurent-Perrier ~80%,
Montelena ~80%. **The first batch since Batch 4 with no sub-bar dossier**, and the +25 estimate was
exact. Canonical untouched (`db_wine_canonical.json` mtime unchanged at 2026-07-28 14:12);
`REGISTER.md` untouched (mtime 2026-08-04 22:02). Site authenticity **6 of 6 passed with zero
look-alikes** — the first clean batch since `D-2026-08-05-09`.

**What Batch 10 changed methodologically.** The batch was composed to test whether *selecting for
producers that publish technical sheets* removes the sub-bar problem. **It does** — but the finding
that matters is the opposite one: the better the producer's own documentation, **the more clearly
canonical is shown to be wrong.** Every one of the six contradicted canonical, which is why the
count now stands at **10 of 10 producers examined across Batches 8–10.** Also established as
routine: reading a public-register `liste_id_bio` / SIRET pairing to find certifications a producer's
own site never mentions (Billecart), and using multiple SIRENs to prove entity separation before
trusting a name (four Leflaive companies; one Moussé company under two names).

**Escalated, not resolved.** Recorded in full in `NEXT_ACTIONS.md` §3f. The load-bearing items:
- 🔴 **Canonical's stored values contradict producer-official sources, and it is not confined to
  prose** — Billecart carries **19 contradicted items across four records**; a single false
  `house_style` string is **duplicated verbatim across all 16 Roederer records**, asserting a Demeter
  certification the house does not hold and a rosé method it explicitly does not use. Includes
  **typed fields** (`grapes`, `dosage`, `aging`, `founded_year`) and an **invented parcel name**.
- 🔴 **The matcher never reads the menu section heading** — proven by a **byte-identical intake
  `evidence` string across all four Roederer rows including the ROSÉ one.** Roederer and Billecart
  are both **counter-examples to `C-6` as written**: canonical already carries the colour axis, so
  **fixing canonical alone does not fix the row.** `C-6` needs restating, not just accepting.
- 🔴 **`V-1` admits no surrogate key.** Grand Siècle's three base vintages **overlap between
  itérations**, so there is **no correct value for the `vintage` field** — a "fix the vintage field"
  migration has nothing to write. Adding Nº27 also makes **`(cuvée, vintage="NV")` non-unique inside
  canonical.** `V-2` is undercounted (4 magnums, 3 with no sibling); `V-3` needs
  **itération × format × disgorgement state**.
- ✅🔴 **`P-2` is answered and its recorded impact is wrong.** One SIRET (`449 670 702 00025`) bears
  both `SARL CHAMPAGNE MOUSSÉ FILS` and `SARL FAMILLE MOUSSÉ` — **one house, two names**. But the
  measured impact is **1 bottle, not 3**: `P-2` = 1 entity-split + 2 vintage gaps. **Not executed.**
- 🔴 **Four new unnumbered shapes** — a superseded cuvée name during a rename (Billecart); the
  **brand axis inside the cuvée string** (`Récolte du Domaine`, with no separate entity to point at);
  over-splitting a product name that legitimately contains its appellation (**the inverse of `C-4`**);
  and a cross-producer collective designation embedded in a name (`Special Club`, supported by
  **zero** occurrences in the producer's site or the Club's own roster).
- 🔴 **`D-2026-08-05-08`'s failure condition demonstrated live** — of 16 canonical records matching
  `leflaive`, **0 are Olivier Leflaive** and **9 match only on other producers' prose**.
- ⚠️ **The menu is not reliably the defective side.** Three counter-examples, and the "category word
  as cuvée name" pattern **did not recur**. Montelena's `subregion` **is** label-backed — a
  counter-example to Batch 9's attribute-provenance shape. **Pattern existence is not evidence.**

**Ten physical-label tasks added**, bringing the floor total to **eighteen**.

**Applied as.** Six dossiers under `research/producers/`, plus the Batch 10 map in
`research/producers/coverage.py`. One structural correction was made by the orchestrator: the
`olivier-leflaive.md` dossier carried an extra `##` heading before `## Identity`, which was demoted
to `###` so the fixed template sequence holds; **no content was changed.** **Reversal** is deletion
of those files and their `coverage.py` entries; coverage returns to 59.5%. Nothing else was touched.

---

## D-2026-08-06-04 — Coverage counts a Bordeaux row without resolving which wine it is

**Date** 2026-08-06 · **Authority** Execution · **Status** Applied

**Decision.** Count all 47 Bordeaux rows as covered even though **not one of them can be resolved to
grand vin vs second vs third wine** from any available source.

**Reason.** The bar is `D-2026-08-04-02`: *a sommelier can speak about the producer on the floor
without saying anything false.* Every dossier states the ambiguity explicitly, names the candidate
wines, and routes the identification to a physical-label task. **Saying "this is one of Château
Palmer, Alter Ego or the white, and here is how to tell" is not false; saying "this is Château
Palmer" would be.** Counting these rows measures dossier coverage, **not** row attribution — the
same distinction already recorded for Hundred Acre (4 of 5 rows are sibling brands) and Famille
Moussé (one house, two menu spellings).

**Applied as.** `research/producers/coverage.py`, Batch 12 block, with the reasoning in a comment so
the number cannot be misread later. **515 / 704 (73.2%), 76 dossiers.**

**Reversal.** Remove the eight Batch 12 keys from the map; coverage returns to 468 / 704 (66.5%).

---

## D-2026-08-06-03 — Producer research runs at 8 concurrent agents

**Date** 2026-08-06 · **Authority** Execution · **Status** In force · **Supersedes** the max-2 practice

**Decision.** Run producer research at up to **8 concurrent agents**, one producer per agent, with no
shared state and no cross-reading between agents.

**Reason.** Batches 10 and 11 ran at a maximum of 2. Batch 12 ran 8 and delivered **8 of 8 above the
bar, all Confidence High**, with no cross-contamination. **The parallelism also produced evidence a
serial run could not**: three agents independently converged on the same matcher defect from three
different angles (Mouton via a zero-overlap token-set evidence string, Palmer via the same shape
stated as *false* rather than *absent* information, Haut-Brion and Giscours via the store-layer
collapse). Independent convergence is corroboration; sequential discovery would have been one
agent's claim.

**Traded away.** Nothing structural. The one cost was a briefing defect amplified 8× — see
`D-2026-08-06-02`.

**Reversal.** Lower the agent count in the batch brief. No artifact depends on it.

---

## D-2026-08-06-02 — The batch brief must state the intake artifact's absolute path

**Date** 2026-08-06 · **Authority** Execution · **Status** In force

**Decision.** Every producer-research brief must give the absolute path of the intake package —
`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` (704 rows) — and state that it
is the source of `match_state`, `confidence` and `source_quality_flags`, and the artifact
`research/producers/coverage.py` computes coverage from.

**Reason.** The intake package lives **outside the repository**. Batch 12's brief quoted values from
it without saying where it was, and **four of eight agents independently concluded the values did not
exist**, each having found the store layer's separate `flags` field inside the repo and reasoned from
its emptiness. Two went on to assert in writing that the pipeline does not detect a defect it does
detect. **All four were corrected; the fault was the briefing's, not the agents'.** The standing rule
that every count must name its artifact (Batch 8, Bachelet-Monnot) is necessary but insufficient if
the brief itself does not say where the artifact is.

**Applied as.** `NEXT_ACTIONS.md` §1 "Workflow fixes Batch 12 earned", item 1.

**Corollary, recorded because it nearly cost the batch a real finding.** The flag vocabulary is real:
11 tokens over 704 rows, of which **all 6 `format_in_name` rows are d'Yquem** and **2 of 3
`section_colour_conflict` rows are Cos d'Estournel**. The correct reading is not "the pipeline is
blind" but **"the pipeline detects it at intake and loses it before the store layer."**

---

## D-2026-08-06-01 — Batch 11 runs the six producers already selected; stop after 11

**Date** 2026-08-06 · **Authority** Akio · **Status** Applied

**Decision.** Run **Batch 11** on the producers already selected in `NEXT_ACTIONS.md` §1 — the
remainder of the 4-bottle tier. **Maximum 2 concurrent producer agents.** Objectives: increase
restaurant coverage, continue producing high-quality dossiers, **do not expand architecture
investigations**. Verify **only the scope this batch changed** (`D-2026-08-05-13`) — after every
completed producer: dossier structure, required sections, canonical untouched. **No repository-wide
integrity sweeps, no repository-wide git inspection, no expansion of the canonical-contradiction
investigation** — that evidence is now considered sufficient, and new canonical issues are recorded
**only when encountered naturally during producer research**. All standing rules remain in force:
the 70% bar, official sources only, technical-sheet PDFs whenever available, preserve uncertainty,
never invent, `## Akio's Insight` left empty, canonical read-only, canonical conflicts escalated
only, **`REGISTER.md` not modified**, **ADR-002 not started**, **Bordeaux batch not started**.
Commit completed work with **explicit paths only**; **do not push**. **Stop automatically after
Batch 11.**

**Composition.** Vilmart & Cie, Henri Giraud, Alvina Pernot, Anne et Hervé Sigaut, René & Vincent
Dauvissat, Thierry Allemand — 4 OBP bottles each. These are exactly the six that `D-2026-08-05-15`
**excluded from Batch 10 on criterion (3)**, having no known producer-authored web source.

**Outcome.** 6 dossiers, **+24 OBP bottles (444 → 468 of 704; 63.1% → 66.5%)**, **68 dossiers**.
Remaining: 114 producers / 236 bottles. **The +24 estimate was exact.** **Four cleared the bar** —
Vilmart ~85% (High), Sigaut ~78% (Medium-High), Giraud ~76% (Medium), Alvina Pernot ~74% (Medium).
**Two are deliberately below it and marked `awaiting material from the team`** — Dauvissat ~64%,
Thierry Allemand ~62%, the first sub-bar dossiers since Batch 8. Canonical untouched (SHA-256
`200e96bc…5408`, unchanged, mtime 2026-07-28 14:12); `REGISTER.md` untouched (SHA-256
`4609cc34…6968`, mtime 2026-08-04 22:02) — both verified after every producer.

**Reason the two shortfalls are not execution failures.** In both cases the absence of any
producer-authored source was **proved rather than assumed**, and by a route stronger than Batch 8's:
Thierry Allemand has **never registered a domain at all** (`.com` ×3 → Verisign RDAP 404, `.fr` ×2 →
AFNIC `NOT_FOUND_DOMAIN_NAME_WITH_NAME`, Wayback HTTP 200 with `archived_snapshots: {}` — a
resolving negative, not a gate), and Dauvissat's Agence Bio record carries a `Site Officiel` entry
whose `url` is an **empty string**. Padding either to 70% would have required inventing history,
winemaking and style. **A thin dossier with a heavy must-not-say list is the correct deliverable.**

**What Batch 11 changed methodologically.**
- 🔴 **"The producer publishes nothing" is at least six distinct conditions, not one, and they need
  different remedies.** Batch 8 proved three (OVH placeholder / MX-only / no domain). Batch 11 adds
  **publishing stopped but site live** (Giraud), **site frozen at a past vintage** (Sigaut, stops at
  2019 while the OBP rows are 2022–2023), **domain owned but never published** (Alvina Pernot, a
  9-byte body), **domain never registered** (Allemand), and **an Agence Bio `Site Officiel` whose
  `url` is empty** (Dauvissat). → **`awaiting material from the team` is too coarse a status**, and
  Shape B's row list should be re-cut on *did the material ever exist publicly* rather than on score.
- ✅ **Internet-Archive recovery of a producer's own former pages is now an established route.**
  Giraud's entire cuvée substance came from archived copies **authenticated by the mentions-légales
  block embedded in each capture**, tagged `📄` and held strictly distinct from `✅` live content.
  ⚠️ Wayback returned **HTTP 429** for another agent in the same batch — **a gate is not evidence
  of absence.**
- 🔴 **Only an exact-SIRET negative counts as a proved negative.** **Agence Bio's own search API
  returns `LALLEMAND` entries for a `nom=allemand` query** — the `D-2026-08-05-08` defect appearing
  inside a public register's search, not just inside canonical.
- 🔴 **Site authenticity must be checked even when the briefing asserts the domain.** The
  orchestrator supplied `vilmart.fr` as Vilmart's likely official site; it is a **Dovendi
  domain-for-sale parking page**. **Nine look-alikes were rejected in this batch — more than the
  previous five batches combined**, including two Dovendi/`Nomio24` pages by the same registrant
  and one domain **one character** from the genuine one.

**Escalated, not resolved.** Recorded in full in `NEXT_ACTIONS.md` §3g. The load-bearing items:
- 🔴 **`D-2026-08-05-12`'s reading of `'NV'` needs restating per appellation.** That sweep held the
  88 `'NV'` records **legitimate for non-vintage Champagne**; `allemand-chaillot-nv` is a **Cornas**,
  which the INAO CDC reserves for *vins tranquilles rouges* and anchors to the `déclaration de
  récolte`. **The bucket is mixed**, which matters because the three-meanings partition is the
  stated basis for treating any vintage migration as three separate cases. The record is **distinct,
  not a phantom** — it uniquely carries **`dosage: "N/A — Still Wine"`, a Champagne field on a Rhône
  record** — and is **template-derived**.
- 🔴 **Blanket article/accent normalisation is refuted by a worked counter-example.** `La Forest`
  occurs **0 times** in either INAO Chablis cahier, and **`La Forêt` / `Sur la Forêt` genuinely
  exist under a different umbrella (`Vau Ligneau`) — so normalisation lands the row on the wrong
  vineyard.** Requires an **explicit alias**, not a rule. Also: **`Les Clos` is the only Chablis
  Grand Cru climat carrying an article — do not strip it.**
- 🔴 **`S-2`'s invisibility is demonstrated and explains the 175.** The matcher's own evidence reads
  `'La Garenne' ≡ '"La Garenne"'` at **`confidence: 1.0`**, and Allemand shows the same corruption
  handled **two different ways within four rows of one producer**.
- 🔴 **A new unnumbered shape: a canonical record that is *empty* rather than *wrong*.** All four
  Alvina Pernot records lack 8 fields **as keys** while every row reads `match_state = exact` at
  `confidence 1.0` against a $360/$640/$720/$720 lineup.
- 🔴 **`match_state = exact` is repeatedly under-specified rather than correct** — three independent
  instances, including Giraud row 1 where **the dosage axis is not compared at all** (menu
  `Brut Nature` / canonical `Brut` / the house says neither), and Vilmart where **the only row
  intake called resolved is the only row that could not be confirmed officially.**
- 🔴 **A `P-1`-shaped cross-producer binding hazard, twice** — `arlaud-les-sentiers-2021` (same
  climat as Sigaut row 4) and `raveneau-montee-de-tonnerre-2021` (same climat **and vintage** as
  Dauvissat row 3).
- 🔴 **The temporal certification trap now has three instances** (Moussé, Giraud `C2`, Dauvissat
  `2021-04-27` scoped `Agriculteur` — farming only, not winemaking). **A current certification says
  nothing about a bottle whose vintage predates it.** Separately, **Allemand holds no certification
  of any kind**, proved three ways — **contradicting canonical's `Biodynamic` tag outright.**
- 🔴 **A fourth counter-example to "the menu is the defective side", and the first clean case where
  the menu *is*** — canonical alone writes `"La Pièce Sous le Bois"` against INAO ×2 and BIVB, while
  OBP misspells `Theirry Allemand` on all four Rhône rows.
- ✅ **Cadastral evidence resolved a below-INAO-granularity case Batch 8 could not.** `Chaillot` and
  `Reynard` appear 0 times in the Cornas cahier but **DGFiP/Etalab confirms both as real cadastral
  lieux-dits**, and **CDC XII.2°a) permits a smaller unit on the label if it is a lieu-dit cadastré**
  — a legal pathway Chassagne lacks. **The Niellon question should be re-asked per appellation.**
- ⚠️ **A third INAO filename convention exists — `PNO<year>AOP<Name>.pdf`** — and 🔴 **several of
  these files are opposition-procedure drafts whose extracted text merges struck-through old values
  with new ones**, found independently by three agents. **Bare number extraction would silently
  quote superseded figures.**

**Twenty-one physical-label tasks added**, bringing the floor total to **thirty-nine**. The
load-bearing ones: **Allemand's sulfites declaration** (no producer source exists for any of
1998/1999/2001/2006 and third-party accounts disagree — **no claim was made in either direction**),
**Giraud row 4's "2022"** (a `MILLÉSIME` or an MV-style base year — **this alone decides `V-1` vs an
ordinary vintage**), and **Alvina Pernot's `mis en bouteille` wording** (the only thing that can
settle whether `AP WINES SAS`, NAF **`46.90Z` wholesale, not `01.21Z` viticulture**, is domaine or
négoce).

**Applied as.** Six dossiers under `research/producers/`, plus the Batch 11 map in
`research/producers/coverage.py`. **No structural correction was required on any of the six** —
all fourteen `##` headings in the mandated order, `## Akio's Insight` left empty, on every dossier.
**Reversal** is deletion of those files and their `coverage.py` entries; coverage returns to 63.1%.
Nothing else was touched.

---

## D-2026-08-05-12 — The canonical integrity sweep is measurement, not adjudication

**Date** 2026-08-05 · **Authority** Execution · **Status** Applied · **Reversible**

**Decision.** Answer the two questions Batch 8 left open with a checked-in, reproducible script —
`research/canonical_conflicts/sweep_integrity.py` — that **reads canonical and writes nothing.**
`REGISTER.md` is not modified; numbering and remedy remain the CTO's call under D-2026-08-04-03.

**Findings.** Both defects are an order of magnitude larger than the estimates that prompted them:

| | Prior estimate | **Measured** | Share of canonical |
|---|---|---|---|
| `S-2` embedded quote marks in cuvée names | 9 (Batch 7) | **175** | **18.9%** |
| `vintage = '—'` em-dash sentinel | 1 (Batch 8) | **328** across **182 producers** | **35.3%** |

**Reason the numbers moved.** The Batch 7 figure of 9 was a **sample** of the producers then being
researched, never a count. Nobody had swept the whole set.

🔴 **The load-bearing finding is not the size — it is that the `vintage` field carries three
different meanings at once.** `'—'` is a true null (328); `'NV'` is legitimate and correct for
non-vintage Champagne (88); and **24 records encode a base year inside the vintage string in five
mutually incompatible notations** — `NV · based on 2006`, `NV (Base: 2018)`, `NV · 2022 Base`,
`NV (LC21)`, `NV（2022）` (full-width parentheses). That third group is family **`V-1`**, not a
sentinel. **A single "fix the vintage field" migration would destroy the Krug base-year data.**

The sweep also isolates **78 records whose names contain a legitimate French elision**
(`L'Esprit`, `Réserve de l'Abbaye`). **These are correct and must not be caught by any `S-2` fix** —
which is precisely why the script classifies paired quote marks separately from apostrophes rather
than counting quote characters.

**Reversal.** Delete the script; it has no side effects.

---

## D-2026-08-05-09 — A site is not treated as official until its authenticity is checked

**Date** 2026-08-05 · **Authority** Execution · **Status** In force

**Decision.** Before any website is used as a producer's own source, confirm authenticity by at
least one of: (a) a legal notice / mentions légales naming a publisher tied to the producer,
(b) the absence of a disclaimer denying affiliation, (c) a reciprocal link from the owner or the
appellation body, or (d) an address matching a public register such as Agence Bio. Cache anything
rejected under a filename that says so (`FANPAGE_…`, `NOT_THE_PRODUCER_…`).

**Reason.** Batches 6 and 7 hit four sites that carried the producer's exact name and were not the
producer: `comtes-lafon.com` (self-declared "independent fan page … not affiliated with or endorsed
by the official company", written in the first person with `/history` and `/philosophy` pages),
`ramonet.fr` (Dovendi domain-for-sale page), `caroline-morey.com` (a Newport Beach wedding
photographer), `pierregirardin.com` (a Marseille photographer). The first would have produced a
plausible, detailed, entirely unusable dossier.

**Consequence.** "Official sources only" is not satisfied by a matching domain name. Two sites
passed the check in these batches: `brunoclair.com` (legal notice + contact) and
`domaine-eugenie.com` (reciprocal link from Artémis Domaines, its owner).

---

## D-2026-08-05-08 — OBP coverage is recomputed from a checked-in script, not carried forward

**Date** 2026-08-05 · **Authority** Execution · **Status** Applied · **Reversible**

**Decision.** Compute OBP coverage with `research/producers/coverage.py`, which holds an
explicit hand-verified map from dossier slug to the producer strings used in
`obp_intake_normalized_20260804.json`, and errors loudly on any name it cannot match.

**Reason.** The pre-Batch-5 figure of record was **256 / 704 (36.4%)** for 26 dossiers. It could not
be reproduced: the same 26 dossiers resolve to **245 / 704 (34.8%)**. Fuzzy name matching is the
likely cause (for example `Olivier Leflaive Frères` and `Anne-Claude Leflaive` are separate
producers that a substring match folds into `Domaine Leflaive`). Rather than pick a number, the
count is now derived by a script that lives next to the dossiers.

**Applied as.** `research/producers/coverage.py`. Post-Batch-5: **289 / 704 (41.1%)**, 32 dossiers.
Post-Batch-6: **325 / 704 (46.2%)**, 38 dossiers. Post-Batch-7: **359 / 704 (51.0%)**, 44 dossiers,
138 producers / 345 bottles remaining.

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

2026-08-06 (updated after Batch 12 close-out; adds D-2026-08-06-02, -03, -04, **-05**)
