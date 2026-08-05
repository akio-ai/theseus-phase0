# Next Actions

> **Official state document.** Written 2026-08-05 from verified repository state.
> Ordered by what unblocks the most work, not by effort.
> Companion to [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`DECISIONS.md`](DECISIONS.md).

## Legend

**🔴 Blocked on Akio** — execution cannot proceed without a decision.
**🟡 Ready** — authorized, can start immediately.
**⚪ Deferred** — deliberately not started; do not pick up without instruction.

---

## 1. 🔴 Approve Batch 8 (producer research)

**Batches 5, 6 and 7 are closed and committed** (D-2026-08-05-07). Execution stopped after Batch 7
as instructed. **Batch 8 is proposed but must not start without approval.**

Coverage now **359 / 704 bottles (51.0%)** across **44 dossiers**. Remaining: **138 producers /
345 bottles**. The curve is flat from here — no remaining producer unlocks more than 5 bottles.

Proposed, ranked by OBP bottles unlocked (`research/producers/coverage.py` reproduces the ranking):

| Producer | OBP bottles | canonical | note |
|---|---|---|---|
| **Jacques Selosse — finish** | (0 new) | exists | 🔴 see below |
| Taittinger | 5 | exists | Champagne, blanc de blancs |
| Domaine Roulot | 5 | exists | Meursault |
| Domaine Bachelet-Monnot | 5 | exists | Côte de Beaune whites |
| **Michel Niellon** | 5 | **absent** | Chassagne-Montrachet |
| Domaine de L'Arlot | 5 | exists | Nuits-Saint-Georges |
| **Clos de la Coulée de Serrant (Nicolas Joly)** | 5 | exists (alias) | Loire; the only non-Burgundy/Champagne block left at 5 |

**Total 30 bottles** → coverage to roughly **55%**.

**Alternative shape worth considering instead.** Six of the eighteen dossiers just delivered are
below the 70% bar purely because a producer-authored source could not be found or could not be
read. Four of those are recoverable with work already scoped:

| Dossier | Current | Blocker | Fix |
|---|---|---|---|
| **Gosset** | ~35% | cuvée pages are JS-rendered | **browser rendering** — highest value per unit of work in the whole set |
| **Mayacamas** | 70%+ | `trade_assets` blocked to scripts | browser rendering → per-vintage data for all 6 OBP bottles |
| **DuMOL** | ~45% | two `/about/` sub-pages unread | fetch two pages |
| **Domaine Laroche** | 70%+ | history page JS-rendered | browser rendering |

A "repair batch" would add **0 bottles of coverage** but would lift four dossiers and close roughly
half the outstanding `awaiting material from the team` items. **Which shape to run is Akio's call.**

**Bordeaux remains excluded** (Margaux 8, Haut-Brion 6, Latour 6, Mouton-Rothschild 6, Giscours 6,
d'Yquem 6, Palmer 5, Cos d'Estournel 4 — **47 bottles**), per the standing reason below. It is now
by far the largest single block left.

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

2026-08-05 (updated after Batch 4)
