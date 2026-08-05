# Next Actions

> **Official state document.** Written 2026-08-05 from verified repository state.
> Ordered by what unblocks the most work, not by effort.
> Companion to [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`DECISIONS.md`](DECISIONS.md).

## Legend

**🔴 Blocked on Akio** — execution cannot proceed without a decision.
**🟡 Ready** — authorized, can start immediately.
**⚪ Deferred** — deliberately not started; do not pick up without instruction.

---

## 1. 🔴 Approve Batch 5 (producer research)

Batch 4 is closed and committed. **Batch 5 is proposed but must not start without approval.**

Proposed, ranked by OBP bottles unlocked (`obp_intake_normalized_20260804.json`, 704 rows):

| Producer | OBP bottles | canonical record | current match states |
|---|---|---|---|
| Armand Rousseau | 7 | exists | 2 exact / 1 alias / 4 unresolved |
| **Ganevat** | 7 | **absent** | 7 unresolved |
| Billaud-Simon | 7 | exists | 2 exact / 5 unresolved |
| Joseph Drouhin | 7 | exists | 2 exact / 5 unresolved |
| Olivier Bernstein | 7 | exists | 1 exact / 6 unresolved |
| **Pol Roger** | 6 | **absent** | 6 unresolved |

**Total 41 bottles** → would take coverage to roughly **42%**. Ganevat and Pol Roger satisfy both
priority ① (unlock count) and ② (absent from THÉSEUS); Pol Roger also scores high on ③ (restaurant
importance).

**Château Margaux (8 bottles) is again excluded**, per the standing reason below.

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
