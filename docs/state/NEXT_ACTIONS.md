# Next Actions

> **Official state document.** Written 2026-08-05 from verified repository state.
> Ordered by what unblocks the most work, not by effort.
> Companion to [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`DECISIONS.md`](DECISIONS.md).

## Legend

**🔴 Blocked on Akio** — execution cannot proceed without a decision.
**🟡 Ready** — authorized, can start immediately.
**⚪ Deferred** — deliberately not started; do not pick up without instruction.

---

## 1. 🔴 Approve Batch 4 (producer research)

Batch 1–3 are closed and committed. **Batch 4 is proposed but must not start without approval.**

Proposed, ranked by OBP bottles unlocked (`obp_intake_normalized_20260804.json`, 704 rows):

| Producer | OBP bottles | canonical record |
|---|---|---|
| Dujac | 10 | exists |
| **Pride Mountain** | 10 | **absent** |
| De Montille | 8 | exists |
| Denis Mortet | 8 | exists |
| Jacques-Frédéric Mugnier | 8 | exists |
| **Grgich Hills** | 8 | **absent** |

**Total 54 bottles.** Pride Mountain and Grgich Hills satisfy both priority ① (unlock count)
and ② (absent from THÉSEUS).

**Château Margaux (8 bottles) was deliberately excluded.** Bordeaux grands vins print only the
appellation on the menu and require `facts.subregion` matching; Margaux / Giscours / d'Yquem
are more efficiently handled as a dedicated **Bordeaux batch**.

Alternative if preferred: run the Bordeaux batch first.

## 2. 🔴 Decide push / PR for the Research Layer commit

`research/producer-layer-batch1-3` @ `cc9c1e1` exists **locally only**. Operating rules forbid
pushing without CEO approval.

Two sub-decisions:

- **Push and open a PR?** (base would be `origin/main` @ `30d90d1`.)
- **Should `research/producers/_sources/` (296MB) enter history?** It is currently gitignored.
  One file alone is 76MB; the contents are third-party brochures and site captures.
  Provenance is preserved as URLs in each dossier's `## Sources`.
  → See [`DECISIONS.md`](DECISIONS.md) D-2026-08-05-02. Reversing this later is cheap;
  reversing the opposite choice requires history rewriting.

## 3. 🔴 ARIADNE — three decisions that gate all UI work

1. **Hero artwork.** `~/Downloads/赤い線画の夢幻的な女性肖像.png` (1254×1254) was found but never
   confirmed as the intended asset. The Home slot is already built and waiting.
2. **Schema changes.** Aroma intensity 0–10, aroma complexity, and the 11-family taxonomy each
   require a migration. Blocked by the standing "do not touch the DB" instruction.
   If approved: migration **plus reverse migration**, on a separate branch.
3. **Fruit Basket — ship or not.** Explore ⇄ List two-mode prototype is distributed on a public
   QA URL (no login). Verified across 3 widths × light/dark.
   🔴 **44pt touch targets are proven unreachable on the image** (min 15.6pt at 320px; 0 of 48
   reach 44pt) → **shipping requires the List mode alongside it.**

## 4. 🟡 Resolve `Les Hautes Mottes, Brut Nature 2018` (OBP, $345)

Confirmed: `Les Hautes Mottes` is a **lieu-dit in Le Mesnil-sur-Oger**, the old-vine parcel
feeding Cœur de Mesnil, Authentique and Grand Cru Millésimé (4 official sources).

**No cuvée of that name exists on gonet.fr** — verified 2026-08-05 against `pages-sitemap.xml`
(53 URLs) and the `/boutique` product list.

**Do not assert it is a later vintage of Grand Cru Millésimé.** Needs the physical bottle label
or an importer technical sheet. This is a floor task, not a research task.

## 5. 🟡 OCR the Michel Gonet technical sheets

7 PDFs are captured in `research/producers/_sources/michel-gonet/ts_*.pdf` but are outline-only
with no text layer (extraction returned one fragment). OCR would likely yield pH, total acidity,
alcohol and disgorgement dates. Not attempted.

## 6. 🟡 Refresh stale state records

- `docs/ai/project_state.md` still records **Phase 3B-U2**; U3 is merged. Now superseded by
  `docs/state/CURRENT_STATE.md` but not deleted.
- `docs/ai/work_queue.md` lists U2/U3 as Ready.
- U3 specification status markers are stale (left intentionally to avoid an unmerged branch)
  → fix in a small PR.
- Local integration worktree is 2 commits behind (`58f2bd9` vs `c4ddde1`) → fetch + fast-forward.

## 7. ⚪ Deferred — do not start without instruction

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

2026-08-05
