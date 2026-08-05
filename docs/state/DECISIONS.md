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

2026-08-05 (updated after Batch 9 close-out; adds D-2026-08-05-13 and -14)
