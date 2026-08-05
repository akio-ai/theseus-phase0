# Next Actions

> **Official state document.** Written 2026-08-05 from verified repository state.
> Ordered by what unblocks the most work, not by effort.
> Companion to [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`DECISIONS.md`](DECISIONS.md).

## Legend

**🔴 Blocked on Akio** — execution cannot proceed without a decision.
**🟡 Ready** — authorized, can start immediately.
**⚪ Deferred** — deliberately not started; do not pick up without instruction.

---

## 1. 🔴 Approve Batch 9 (producer research)

**Batch 8 is closed and committed** (D-2026-08-05-10). **Batch 9 is proposed but must not start
without approval.**

Coverage now **389 / 704 bottles (55.3%)** across **50 dossiers**. Remaining: **132 producers /
315 bottles**. The curve is flat and getting flatter — **no remaining producer unlocks more than 5
bottles**, and after the 5-bottle tier is exhausted the next tier is 4.

### Shape A — six more new producers (+30 bottles → ~59.6%)

Ranked by OBP bottles unlocked (`research/producers/coverage.py` reproduces the ranking):

| Producer | OBP bottles | canonical | note |
|---|---|---|---|
| **Harlan Estate** | 5 | to verify | Napa; publishes per-vintage data |
| **Hundred Acre** | 5 | to verify | Napa |
| **Abreu** | 5 | to verify | Napa |
| **Clos de Tart** | 5 | to verify | Burgundy monopole Grand Cru |
| **Armand Heitz** | 5 | to verify | Côte de Beaune |
| **Bergström** | 5 | to verify | Oregon |

🔴 **Note the composition shift.** The 5-bottle tier is now **majority New World** (Harlan, Hundred
Acre, Abreu, Bergström). On the Batch 4 evidence — Pride Mountain and Grgich Hills both reached
**High** confidence because US wineries publish per-vintage technical data — this batch is likely to
land *higher* than Batch 8, which was dominated by small Burgundian domaines that publish nothing.
`Famille Mousse` (5, Champagne) is also available if a French producer is wanted in the mix.

### Shape B — repair batch (+0 bottles, lifts 6–8 existing dossiers)

**Eight dossiers now sit below the bar.** Batch 8 added two, and both are **permanently blocked by
absence of any producer-authored text** — no amount of browser rendering will fix them:

| Dossier | Current | Blocker | Fix |
|---|---|---|---|
| **Gosset** | ~35% | cuvée pages JS-rendered | **browser rendering** — still the best value in the set |
| **Mayacamas** | 70%+ | `trade_assets` blocked to scripts | browser rendering → per-vintage data, 6 bottles |
| **DuMOL** | ~45% | two `/about/` sub-pages unread | fetch two pages |
| **Domaine Laroche** | 70%+ | history page JS-rendered | browser rendering |
| **Michel Niellon** | ~60% | 🔴 **no site exists**; Instagram is the only channel | render Instagram captions; query the syndicat |
| **Domaine Roulot** | ~60% | 🔴 **no site exists** (OVH placeholder) | **procurement only** — domaine-authored sheet |
| Ganevat / Comtes Lafon / Ramonet / PY Colin-Morey / Caroline Morey / Pierre Girardin | 25–55% | same | **procurement only** |

🔴 **Shape B is now mostly a procurement task, not a research task.** Only the top four rows are
recoverable by execution. **Which shape to run is Akio's call.**

### Shape C — data-integrity sweep (+0 bottles, unblocks the matcher)

Batch 8 surfaced two defects whose **true scope is unknown** and which are cheap to measure:
1. **Unsourced prose in `obp_note`** — critic scores and claims contradicted by official sources are
   already reaching floor-facing copy (Coulée de Serrant, Bachelet-Monnot). **Nobody knows how many
   records are affected.**
2. **The `S-2` quote-mark sweep across all 781 cuvées**, still outstanding from Batch 7 and now
   6 records larger.

**Bordeaux remains excluded** (Margaux 8, Haut-Brion 6, Latour 6, Mouton-Rothschild 6, Giscours 6,
d'Yquem 6, Palmer 5, Cos d'Estournel 4 — **47 bottles**), per the standing reason below. It remains
by far the largest single block left, and is now **15% of everything outstanding**.

## 2. ⚪ Bordeaux batch — proposed, explicitly not started

Bordeaux grands vins print only the appellation on the menu and require `facts.subregion` matching
(see the trap list in the OBP gap analysis). Handling **Margaux (8) / Giscours (6) / d'Yquem (6)**
and their neighbours as one dedicated batch is more efficient than folding them into a Burgundy
batch one at a time. **Do not start without instruction.**

## 3. 🔴 Review PR #5

`research/producer-layer-batch1-3` is pushed; **PR #5** is open against `main`
(https://github.com/akio-ai/theseus-phase0/pull/5). It carries the Research Layer, the conflict
register, the t-01 workspace, `docs/state/`, and the Batch 4 dossiers.

One sub-decision remains open:

- **Should `research/producers/_sources/` enter history?** It is currently gitignored (the cache is
  several hundred MB of third-party HTML/PDF; one file alone is 76MB). Provenance is preserved as
  URLs in each dossier's `## Sources`.
  → See [`DECISIONS.md`](DECISIONS.md) D-2026-08-05-02. Reversing this later is cheap;
  reversing the opposite choice requires history rewriting.

## 3c. 🔴 Questions raised by Batches 5–7 that research cannot answer

1. 🔴 **Six dossiers are `awaiting material from the team`** — Ganevat (~55%), Comtes Lafon (~45%),
   Ramonet (~35%), Pierre-Yves Colin-Morey (~30%), Caroline Morey (~30%), Pierre Girardin (~25%),
   plus Selosse (~60%) and DuMOL (~45%) partially. **All need an importer technical sheet or a
   working producer site.** This is a procurement task, not a research task.
2. 🔴 **Domaine d'Eugénie's three OBP white bottles cannot be attributed.** The official wine list
   is 11 wines, all Pinot Noir; the estate page claims holdings in Chassagne-Montrachet and
   Meursault but publishes no white cuvées. **Needs a physical label check before canonical
   registration.**
3. 🔴 **Article and colour normalisation in the matcher** — Ramonet stalls at `candidate` on
   canonical `Le Montrachet Grand Cru` vs menu `Montrachet Grand Cru` (leading article) and on
   `Chassagne-Montrachet Blanc` vs `Chassagne-Montrachet` (colour word in the name). The first is
   the same family as Batch 4's `Clos de Roi` / `Clos du Roi`; the second is solvable from the OBP
   section. **Matcher fix, not a canonical addition.**
4. 🔴 **Accent variants split one cuvée into two canonical records** — Gosset carries both
   `Célébris …` and `Celebris Vintage`, which is what stalls the two OBP Celebris rows. Same shape
   as **C-1**.
5. 🔴 **Quote marks are embedded in 9 canonical cuvée names** across Batches 5–7 (7 double-quoted,
   2 single-quoted). **A sweep of all 781 cuvées should establish the true count** before anyone
   decides how to fix it. Recorded under **S-2**.
6. 🔴 **Disgorgement date is an identifier for Selosse** — the menu prints `(disgorged 2025)` on
   five bottles and lists `Initial` twice at different prices. Canonical vintages are all `nv` and
   carry no date, so `cuvée × NV` cannot separate them. Same shape as **V-1** (Krug édition) and
   **V-4** (Prévost lot).
7. **Site authenticity is now a standing pre-check.** Four sites in Batches 6–7 looked like the
   producer and were not (a self-declared fan page, a domain-for-sale page, a wedding photographer,
   a Marseille photographer). Verify by legal notice, disclaimer text, reciprocal link from the
   owner or appellation body, or an address matching a public register — before using any content.

## 3d. 🔴 Questions raised by Batch 8 that research cannot answer

1. 🔴 **Two new conflict IDs are proposed and unadjudicated — `REGISTER.md` was not written to.**
   **`C-6`** (colour-axis mis-assignment: a ROSÉ-section row proposed against a Blanc de Blancs
   record, because canonical holds only one `Comtes de Champagne` cuvée) and **`P-8`**
   (`founded_year = 1734` for Taittinger has no basis on the official site; the house's own origin
   is **1932**). Both are High confidence. **Accept, reject or renumber.**
2. 🔴 **Three shapes were deliberately left unnumbered** because they fit no existing family:
   (a) **geographic granularity** — `climat + sub-parcel` (`Les Chaumées, Clos de la Truffière`)
   cannot be expressed by a one-string cuvée model; akin to `V-3` but on a different axis;
   (b) **a non-year sentinel** — `roulot-perrieres` holds `vintage = '—'` (U+2014), which is neither
   `V-1`/`V-4` (meaningful release identifiers) nor `S-2`; **a DB-wide sweep for non-4-digit
   vintages should precede numbering**; (c) **classification drift inside one cuvée** —
   `folatieres-2022` says `Puligny-Montrachet Premier Cru`, `folatieres-2023` says
   `Puligny-Montrachet 1er Cru`.
3. 🔴 **Unsourced canonical prose is reaching floor-facing copy, and the scope is unmeasured.**
   Verifying the Coulée de Serrant record against official sources found `extended aging` **wrong**
   (official élevage is 6–8 months), a `classification` carrying the **superseded** appellation name,
   a `subregion` flattening three AOCs, and a market-price claim with no basis. Bachelet-Monnot
   carries a **Vinous score inside `obp_note`**. **This is a canonical-quality question, not a
   research one** — and it is the highest-severity finding of the batch, because this text is what
   staff read.
4. 🔴 **The intake file and the store-layer mapping disagree on what is resolved.** Bachelet-Monnot
   is `match_state = exact` on all five rows in `obp_intake_normalized_20260804.json`, but
   `research/out/t-01/mapping.json` binds only the three 1er Crus to `canonical_release` — the two
   village Pulignys fall to a `research_shell` **despite their canonical records existing**. Reads
   as a wiring gap. **Until adjudicated, "resolved" counts must state which artifact they came from.**
5. 🔴 **Four rows now need a physical label** — no online source can settle them:
   `Clos de la Maltroie` (Niellon; **supported by no source at all** — INAO and the domaine both
   write `La Maltroie`), `Clos de` vs `Clos des Bouchères` (Roulot; INAO records neither, only
   `Les Bouchères`), `La Coulée de Serrant` vs the menu's `Clos de la Coulée de Serrant` (the latter
   **appears nowhere on the domaine's site**), and Taittinger row 5 (Rosé 2012 vs BdB 2012 — both
   genuinely exist; only the menu's section heading distinguishes them).
6. 🔴 **The OBP menu misstates the appellation on three Coulée de Serrant bottles** ($500 / $400 /
   $600 print `Savennières`; they are **AOC Coulée de Serrant**). Triple-sourced. **Menu-side
   correction, not a canonical edit.**
7. **`Les Champs Gains` needs an explicit alias, not a normalisation rule.** INAO writes
   `Les Champs gain` (singular, lowercase `g`), the syndicat writes `Le Champgains`, the menu writes
   `Les Champs Gains` — **three variants, and a plural difference no rule bridges.**
8. **Article normalisation must not be applied blindly.** Meursault's own 1er cru list is internally
   inconsistent — INAO writes `Les Bouchères` **with** an article and `Perrières` **without** one —
   so a blanket `de`/`des`/`Les` rule would introduce errors. Any fix must diff against the INAO
   list per appellation. This qualifies the request in §3c-3 and §3b-2.

## 3b. 🔴 Two model questions raised by Batch 4 (research cannot answer these)

1. **Per-vintage appellation strings.** Pride Mountain's label appellation changes every year —
   `64% Napa / 36% Sonoma`, `65% Sonoma / 35% Napa`, `Napa County`, `Napa Valley` — because the
   county line runs through the estate. **The current one-`subregion`-per-cuvée model cannot express
   this.** All 10 OBP bottles are affected.
2. **Article normalisation in the matcher.** De Montille's four Corton rows stall at `candidate`
   because the menu prints `Clos de Roi` and both canonical and the producer print `Clos du Roi`.
   A `de`/`du`/`des` normalisation rule would resolve all four. **This is a matcher fix, not a
   canonical addition.**

Both are recorded in the dossiers and **not acted on**.

## 4. 🔴 ARIADNE — three decisions that gate all UI work

1. **Hero artwork.** `~/Downloads/赤い線画の夢幻的な女性肖像.png` (1254×1254) was found but never
   confirmed as the intended asset. The Home slot is already built and waiting.
2. **Schema changes.** Aroma intensity 0–10, aroma complexity, and the 11-family taxonomy each
   require a migration. Blocked by the standing "do not touch the DB" instruction.
   If approved: migration **plus reverse migration**, on a separate branch.
3. **Fruit Basket — ship or not.** Explore ⇄ List two-mode prototype is distributed on a public
   QA URL (no login). Verified across 3 widths × light/dark.
   🔴 **44pt touch targets are proven unreachable on the image** (min 15.6pt at 320px; 0 of 48
   reach 44pt) → **shipping requires the List mode alongside it.**

## 5. 🟡 Resolve `Les Hautes Mottes, Brut Nature 2018` (OBP, $345)

Confirmed: `Les Hautes Mottes` is a **lieu-dit in Le Mesnil-sur-Oger**, the old-vine parcel
feeding Cœur de Mesnil, Authentique and Grand Cru Millésimé (4 official sources).

**No cuvée of that name exists on gonet.fr** — verified 2026-08-05 against `pages-sitemap.xml`
(53 URLs) and the `/boutique` product list.

**Do not assert it is a later vintage of Grand Cru Millésimé.** Needs the physical bottle label
or an importer technical sheet. This is a floor task, not a research task.

## 6. 🟡 OCR the Michel Gonet technical sheets

7 PDFs are captured in `research/producers/_sources/michel-gonet/ts_*.pdf` but are outline-only
with no text layer (extraction returned one fragment). OCR would likely yield pH, total acidity,
alcohol and disgorgement dates. Not attempted.

## 7. 🟡 Refresh stale state records

- `docs/ai/project_state.md` still records **Phase 3B-U2**; U3 is merged. Now superseded by
  `docs/state/CURRENT_STATE.md` but not deleted.
- `docs/ai/work_queue.md` lists U2/U3 as Ready.
- U3 specification status markers are stale (left intentionally to avoid an unmerged branch)
  → fix in a small PR.
- Local integration worktree is 2 commits behind (`58f2bd9` vs `c4ddde1`) → fetch + fast-forward.

## 8. ⚪ Deferred — do not start without instruction

- **ARIADNE Phase 3B-U4.** Dependencies (U2 + U3) are satisfied and evidence C1/C3/C4/AQ-5 is
  outstanding, but design has not begun. 🔴 **AQ-3 Application Cutover Gate is irreversible
  after the first real observation** — it must be decided before implementation, not during.
- **ADR-002.** Explicitly not to be started.
- **Any new architecture work.** Explicitly not to be started.
- **Canonical writes of any kind.** Including the two obvious Michel Gonet additions
  (`Vindey-Montgueux Blanc de Blancs Extra Brut NV`; vintage `2016` on the existing
  `Mesnil-sur-Oger Grand Cru Blanc de Blancs`). Promotion is Akio / CTO's call.
- **IQ-6** (`required_for_complete`) — unadjudicated. U3 does not depend on it; U4 may.
- **`feature/ariadne-tasting-format`** (`418d99a`) is superseded by PR #10; awaiting deletion
  permission. **`feature/ariadne-backend-verification`** (`9c2ca2f`) is unpushed.
- **Win³** — STANDBY since 2026-06-03 (account $0.11, disarmed). No new deploys until capital
  returns. Re-arming the dead-man trigger is mandatory at that point.

## Last Updated

2026-08-05 (updated after Batch 8)
