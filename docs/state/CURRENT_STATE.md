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

**Status: Batch 14 complete — 6 of 6.** Batch 14 closed the four producers **Batch 13** had left
when a monthly spend limit stopped it at 2 of 6, and added two more on restaurant value
(`D-2026-08-06-07`): **Dom Pérignon, Turley, Dominus Estate, Chappellet, Château-Figeac,
Promontory**. **All six cleared the 70% bar; zero sub-bar dossiers** — the fourth such batch, after
4, 10 and 12. Run at **3 concurrent agents** throughout, per `D-2026-08-06-06` §4.
See §"Batch 14 notes" below, and `NEXT_ACTIONS.md` §0 for the findings and the Phase 15 proposal.

**Coverage: 539 / 704 bottles (76.6%) across 84 dossiers. Remaining: 98 producers / 165 bottles.**
The binding producer criterion is **84 / 182 (46.2%)**.

---

**(Historical) Batch 12 — 8 of 8.** The **Bordeaux block**, run as one dedicated batch per
`NEXT_ACTIONS.md` §2: Château Margaux, Château d'Yquem, Château Mouton Rothschild, Château Latour,
Château Haut-Brion, Château Giscours, Château Palmer, Château Cos d'Estournel. **All eight cleared
the 70% bar and all eight are Confidence High** — the second batch since Batch 4 with no sub-bar
dossier, and the first ever at eight producers. Run at **8 concurrent agents**, up from Batch 10–11's
maximum of 2. See §"Batch 12 notes" below.

### Completion criteria scorecard — `D-2026-08-06-05`

> Measured 2026-08-06 against `obp_intake_normalized_20260804.json` (704 rows) and
> `research/producers/*.md` (76 files). **Nothing below is carried over from memory.**

| # | Criterion | State | Measured |
|---|---|---|---|
| **1** | Every OBP producer has a dossier | 🔴 **46.2%** | **84 / 182 producers** (was 76/182 when this scorecard was written; Batch 13 +2, Batch 14 +6). **98 remain.** This — not the 76.6% bottle figure — is the binding constraint |
| **2** | Every OBP bottle is linked to a producer | 🟡 **blocked only by ①** | All **704 / 704** rows carry a well-formed producer name (**0** null, **0** malformed). 550 carry a canonical producer id; the **154** that do not are a *canonical* gap, not a research gap — they include producers already dossiered (Pride Mountain 10, Grgich Hills 8, Ganevat 7, Pol Roger 6). Criterion 2 asks for a **producer**, so the **78** rows awaiting a physical label do **not** block it |
| **3** | Every producer has a documented confidence level | 🟡 **76 / 76 documented, 4 formats** | **Zero dossiers lack a confidence statement.** But it is expressed four incompatible ways: 58 carry the machine-readable header `reached_70: … / confidence: High`; 71 carry a `## Confidence` **section** (per-section table, not a producer-level rollup); 2 use Japanese `確信度`; `chateau-cos-d-estournel.md` has **neither** the header nor a `## Confidence` section — only per-finding `確信度` rows, so it has no producer-level value. **A formatting fix, not research** |

🔴 **The one live violation of "invented information is never allowed."** Not in the dossiers —
in intake. The parser correctly detects *no cuvée printed* on **292 / 704** rows; on **152** of
those the matcher proposes a canonical cuvée anyway, and **147 are marked `exact`**. **0 of the
152 carry a reviewer note**; only **19** carry any `source_quality_flags`. Under `D-2026-08-06-05`
this is in scope for completion, and no amount of canonical repair fixes it — it is a matcher
defect. See §"Batch 12 notes".

| | |
|---|---|
| Dossiers | **84** — `research/producers/*.md` |
| OBP coverage | **539 / 704 bottles (76.6%)** — Batch 5 **+44**, Batch 6 **+36**, Batch 7 **+34**, Batch 8 **+30**, Batch 9 **+30** (15 + 15 on resume), Batch 10 **+25**, Batch 11 **+24**, Batch 12 **+47**, Batch 13 **+6** (stopped at 2 of 6), Batch 14 **+18** |
| Remaining | **98 producers / 165 bottles** |
| Conflicts register | `research/canonical_conflicts/REGISTER.md` — 20 true conflicts, 54 false positives separated. **Batches 5–11 wrote no new entries.** Batch 8 proposes `C-6` and `P-8`; Batch 10 added evidence to `C-1`, `C-4`, `V-1`, `V-2`, `V-3`, `S-2`, **corrected the recorded impact of `P-2` downward** and left five unnumbered shapes; Batch 11 added evidence to `C-4`, `S-2`, `P-1` and **produced a counter-example to `D-2026-08-05-12`'s reading of `'NV'`**, leaving four further unnumbered shapes; **Batch 12 added evidence to `C-1`, `C-4`, `C-5`, `C-6`, `S-2`, `V-1`, `V-2`, `V-3`, proposes `P-9`, and leaves nine further unnumbered shapes** — all awaiting CTO adjudication, none written |
| Canonical writes | **Zero.** Read-only throughout |

⚠️ **Coverage figure corrected.** The pre-Batch-5 number was recorded as **256 / 704 (36.4%)**.
Recomputing it from `obp_intake_normalized_20260804.json` with an explicit, hand-verified
dossier→producer map gives **245 / 704 (34.8%)** for the same 26 dossiers. The 11-bottle gap could
not be reproduced from the intake file; the counting script is now kept at
`research/producers/coverage.py` so the figure is reproducible. **All numbers in this
document use the recomputed basis.**

| Batch | Producers |
|---|---|
| Pre-batch (2) | Domaine Leflaive, Louis Latour |
| Batch 1 (5) | DRC, Faiveley, Simon Bize et Fils, Château Lafite-Rothschild, Jean-Louis Chave |
| Batch 2 (7) | Doyard, Dunoyer de Segonzac, Larmandier-Bernier, Les Monts Fournois, Michel Gonet, Pascal Agrapart, Pierre Péters |
| Batch 3 (6) | Egly-Ouriet, Drappier, Pierre Gimonnet & Fils, Laherte Frères, Jérôme Prévost, Frédéric Savart |
| Batch 4 (6) | Pride Mountain Vineyards, Grgich Hills Estate, Domaine Dujac, Jacques-Frédéric Mugnier, Domaine Denis Mortet, Domaine de Montille |
| Batch 5 (6) | Domaine Armand Rousseau, Ganevat, Domaine Billaud-Simon, Joseph Drouhin, Olivier Bernstein, Pol Roger |
| Batch 6 (6) | Domaine Bruno Clair, Domaine d'Eugénie, Domaine des Comtes Lafon, Jean-Claude Ramonet, Pierre-Yves Colin-Morey, Caroline Morey |
| Batch 7 (6) | Domaine Laroche, Pierre Girardin, Mayacamas Vineyards, DuMOL, Jacques Selosse, Gosset |
| Batch 8 (6) | Taittinger, Domaine Roulot, Domaine Bachelet-Monnot, Michel Niellon, Domaine de L'Arlot, Clos de la Coulée de Serrant (Famille Joly) |
| Batch 9 (6) | Harlan Estate, Clos de Tart, Armand Heitz, Hundred Acre, Abreu Vineyards, Bergström Wines (last three resumed from cache) |
| Batch 10 (6) | Famille Moussé, Louis Roederer, Billecart-Salmon, Laurent-Perrier, Chateau Montelena, Olivier Leflaive Frères |
| Batch 11 (6) | Vilmart & Cie, Henri Giraud, Alvina Pernot, Anne et Hervé Sigaut, René & Vincent Dauvissat, Thierry Allemand |
| Batch 12 (8) | Château Margaux, Château d'Yquem, Château Mouton Rothschild, Château Latour, Château Haut-Brion, Château Giscours, Château Palmer, Château Cos d'Estournel — the Bordeaux block |
| Batch 13 (2 of 6) | Krug, Ridge Vineyards — **stopped by a monthly spend limit**, not by a finding |
| **Batch 14 (6)** | **Dom Pérignon, Turley, Dominus Estate, Chappellet** (Batch 13's remainder, the first two resumed from cache) **+ Château-Figeac, Promontory** (added on restaurant value, `D-2026-08-06-07`) |

**Batch 4 notes.** Two producers (Pride Mountain, Grgich Hills) had **no canonical producer record at
all** — 18 OBP bottles were `producer_state = unresolved` purely for that reason. Both US dossiers
reached **High** confidence because both wineries publish per-vintage technical data. Two structural
findings are recorded in the dossiers and **not acted on**: Pride Mountain's appellation string
changes per vintage (`64% Napa / 36% Sonoma` / `Napa County` / `Napa Valley`), which the current
one-subregion-per-cuvée model cannot express; and de Montille's four Corton rows stall at
`candidate` on a single character (`Clos de Roi` vs `Clos du Roi`).

**Batch 5 notes.**
- **Joseph Drouhin covers 10 bottles, not 7** — the same dossier resolves `Joseph Drouhin` (7),
  `Drouhin-Vaudon` (2) and `Drouhin` = Domaine Drouhin Oregon (1), which are three separate
  canonical producers. Drouhin publishes a per-wine **`Supply:`** field stating whether each wine is
  estate fruit, estate + purchased, or **purchased only** — two OBP bottles are purchased-only.
- 🔴 **Ganevat is the first dossier deliberately left below the bar: `reached_70: NO (~55%)`.**
  Its official site (`ganevat.fr`) returns a maintenance page with no content, so there is no
  producer-authored source at all. The dossier is built entirely from **Agence Bio** (French public
  register), **Ecocert** and **Demeter France** (certifiers) and the **INAO cahier des charges**.
  History, winemaking and style are recorded as unavailable rather than inferred. Treat as
  **`awaiting material from the team`**.
- **Billaud-Simon's legal notice names `Mrs Eve Faiveley` as Publication Director** — a direct link
  to the existing `domaine-faiveley.md` dossier. The site says nothing about ownership, so the
  dossier states only what the legal notice states.
- **Two OBP rows printed `Joseph Drouhin | Côte de Beaune | 2023 | $240` are not a duplicate** —
  one is in the WHITE section and one in RED, and Drouhin makes both.
- **A systematic canonical defect surfaced across three Batch-5 producers**: cuvée names stored with
  literal double quotes (`"Clos Saint-Jacques"`, `"Les Preuses"`, `"Mont de Milieu"`,
  `"Marquis de Laguiche"`). Recorded under **S-2**, not as new entries.

**Batch 6 notes.**
- 🔴🔴 **Three of the six had no usable producer source, and the failure mode was a trap, not an
  absence.** `comtes-lafon.com` presents as the official site — first person, `/history`,
  `/philosophy`, `/vineyards` — but its bundle carries the line *"This account is an independent fan
  page … not affiliated with or endorsed by the official company."* `ramonet.fr` is a Dovendi
  domain-for-sale page. `caroline-morey.com` is a Newport Beach wedding photographer. **None of
  their content was used.**
  → **New standing check before any site is treated as official: legal notice, disclaimer text,
  reciprocal link from the owner/appellation body, or address matching a public register.**
  In Batch 6 only `brunoclair.com` (legal notice + contact) and `domaine-eugenie.com` (reciprocal
  link from Artémis Domaines) passed.
- **Four dossiers are deliberately below the bar** — Comtes Lafon (~45%), Ramonet (~35%),
  Pierre-Yves Colin-Morey (~30%), Caroline Morey (~30%). All are built from INAO cahiers des charges
  and the Agence Bio register only, and all are marked **`awaiting material from the team`**.
- **Bruno Clair states in writing why it is *not* certified organic** — to keep synthetic mildew
  treatments available in years like 2016 — while using none in years like 2019–2020. It also
  publishes a per-wine, per-vintage *drink now / lay down* table: **5 of the 6 OBP bottles are
  `lay down` by the producer's own judgement.**
- 🔴 **Domaine d'Eugénie's official wine list is 11 wines, all Pinot Noir — the three OBP whites
  (Chassagne `Les Perclos`, Meursault 1er `Porusots`, Montrachet GC) are not on it**, although the
  estate page does claim holdings in Chassagne-Montrachet and Meursault. **Their attribution is
  unresolved and the dossier refuses to assert it.**
- **Ramonet located the cause of two `candidate` stalls**: canonical `Le Montrachet Grand Cru` vs
  menu `Montrachet Grand Cru` (leading article), and canonical `Chassagne-Montrachet Blanc` vs menu
  `Chassagne-Montrachet` (colour word in the name). The first is the same article-normalisation
  issue already recorded from Batch 4's de Montille; the second is solvable from the OBP section.

**Batch 7 notes.**
- **A fourth same-name trap**: `pierregirardin.com` is a Marseille photographer's portfolio. Not
  used. Running total of sites that look like the producer and are not: **4** (Comtes Lafon,
  Ramonet, Caroline Morey, Pierre Girardin).
- **Mayacamas is the strongest winemaking record in the three batches** — per-varietal fermentation
  vessel, maceration length, fermentation temperature, foudre volumes and wood origin, new-oak
  percentage, total élevage and bottle conditioning, and *"Malolactic fermentation is prohibited"*
  for the Chardonnay. Its site blocks scripted access outright (Cloudflare WAF), so the text was
  read by ordinary browser viewing; no challenge was circumvented. Two internal contradictions are
  preserved: estate size **475 vs 465 acres**, Cabernet blocks **12 vs 26**.
- **`Mount Veeder Proprietary Blend` is not a cuvée name** — the producer calls it `Red Wine`. Same
  shape as Batch 4's Grgich `'Estate,'`: the menu prints a category word as if it were the cuvée.
- 🔴 **Selosse's `Le Bout du Clos` is on the menu under BLANC DE NOIRS, but the producer states the
  parcel is 80% Pinot Noir / 20% Chardonnay** — the one exception among the six Lieux-Dits.
- **Gosset's cuvée pages are entirely JS-rendered**, so only the official cuvée names could be
  fixed. That was still decisive: the official name is **`Grande Réserve`** (both OBP *and*
  canonical write `Grand Réserve`), `Celebris` **2002 is absent** from the official range, and
  canonical carries **`Célébris` and `Celebris` as two accent variants** — which is exactly what
  stalls the two OBP Celebris rows at `candidate`. Same shape as **C-1**.
- **Three dossiers below the bar**: Selosse (~60%), DuMOL (~45%), Pierre Girardin (~25%).
- **Quote-marks in canonical cuvée names reached 9 records** across Batches 5–7 (7 double-quoted,
  2 single-quoted). A full sweep of all 781 cuvées is now warranted under **S-2**.

**Batch 8 notes.**
- **Four of six cleared the bar** — Domaine de L'Arlot (~88%), Clos de la Coulée de Serrant (~88%),
  Taittinger (~85%), Bachelet-Monnot (~75%). **Two are deliberately below it and marked
  `awaiting material from the team`**: Domaine Roulot (~60%) and Michel Niellon (~60%). In both
  cases the blocker is the same and is now proven rather than assumed — **there is no
  producer-authored text in existence to read.**
- 🔴 **Absence of an official site was *proved*, not merely reported.** `domaineroulot.fr` is
  genuinely registered to `Domaine Guy Roulot` (AFNIC WHOIS, since 2004) but serves an empty OVH
  placeholder; `bachelet-monnot.com` resolves **MX-only** (Microsoft 365 + SPF, no A/AAAA record) —
  an email-only domain; Michel Niellon has no domain at all (five candidates, all NXDOMAIN), and the
  village syndicat lists **Instagram** as the domaine's "site internet". Agence Bio independently
  corroborates each with an empty `siteWebs` field.
- 🔴 **Public-register research now substitutes for a missing website, and it works.** The
  Ganevat route (Agence Bio → certifier → INAO) was extended with the **French state company
  register** (`recherche-entreprises.api.gouv.fr` — SIREN, address, officers, NAF) and the
  **DGFiP/Etalab cadastre** (lieu-dit parcels). `Les Luchets` was settled by exactly this pairing:
  **absent from the INAO Meursault cahier des charges** (therefore not a Premier Cru) but **present
  in the cadastre** as a real lieu-dit of commune 21412. Farming for Roulot — no website at all —
  is nonetheless the best-evidenced section in that dossier (Ecocert `FR-BIO-01`, first engagement
  **2010-04-15**, `mixité: Non`, certificate covering *"Récoltes 2014 et suivantes"*).
- 🔴 **Taittinger's canonical `founded_year = 1734` has no basis on the official site.** A full-site
  scan found the only genuine 1734 refers to the **construction of the Château de la Marquetterie**,
  a building. The house's own account of its origin is **1932** (Pierre Taittinger and Paul Evêque
  acquiring Forest-Fourneaux, whose founding year the site never states). Proposed as **`P-8`**.
  This one is floor-facing, which is what makes it urgent.
- 🔴 **The matcher crossed a colour boundary.** OBP row 5 for Taittinger is printed in the **ROSÉ**
  section but was proposed against the canonical **Blanc de Blancs** record. `Comtes de Champagne
  Rosé` is a genuinely distinct wine — own product page, own technical sheet, Pinot-dominant with
  Bouzy red, 12 years' ageing against 10. Canonical holds **only one** `Comtes de Champagne` record,
  so the matcher has no structural means to discriminate colour. Proposed as **`C-6`**; same root
  cause as **C-4**.
- 🔴 **The OBP menu misstates the appellation on three bottles.** Coulée de Serrant's five rows all
  print `Savennières`, but only `Les Vieux Clos` is AOC Savennières; the three `Coulée de Serrant`
  bottles ($500 / $400 / $600) are **AOC Coulée de Serrant**, a standalone appellation. Triple-
  sourced (domaine statement, INAO cahier des charges, Demeter product list). INAO further records
  that the AOC was homologated as `Savennières Coulée de Serrant` in **November 2011** and
  **renamed `Coulée de Serrant` in 2014** — so canonical's `classification` field carries the
  **superseded** name. Same family as the Bordeaux `facts.subregion` trap.
- 🔴 **Canonical prose is carrying unsourced assertions into floor-facing copy.** Verifying the
  Coulée de Serrant record against official sources found `extended aging` **wrong** (official
  élevage is **6–8 months**), `subregion` flattening three AOCs into one string, and the drinking
  window, tasting notes and *"market price from $100"* resting on nothing — the domaine publishes no
  per-vintage notes at all. INAO gives the vineyard as **6 ha 87 a**, not the 7 ha canonical states.
  Bachelet-Monnot shows the same shape from the other side: its two village records carry a Vinous
  score (`89〜91点（ヴィナス）`) inside `obp_note`, while the **$880 / $680 / $640 1er Crus are empty
  shells**. The most expensive bottles are the hardest to talk about.
- **Michel Niellon: only 1 of 5 printed climat names matches INAO.** `Les Chenevottes` is exact;
  `Clos Saint Jean` → `Clos Saint-Jean`, `Les Chaumees` → `Les Chaumées`, `Les Champs Gains` →
  `Les Champs gain` (singular, lowercase `g` — a **plural difference no normalisation rule bridges**,
  requiring an explicit alias). 🔴 **`Clos de la Maltroie` is supported by no source whatsoever** —
  INAO records `La Maltroie`, and the domaine's own list writes `« La Maltroie »`. Needs a physical
  label. Confusion risk with the separate **Château de la Maltroye** is recorded in Must-Not-Say.
- **A model gap on the geographic axis.** Niellon row 4 prints `'Les Chaumees, Clos de la
  Truffiere,'` — a 1er Cru climat *plus* a named clos inside it. `Truffière` occurs **zero times**
  anywhere in the Chassagne cahier des charges: it sits **below the appellation's legal
  granularity**. A one-string cuvée model cannot express *climat + sub-parcel*. Structurally akin to
  `V-3` (one key is insufficient) but on the geographic rather than the release axis. **No new
  number was opened** — absorb-or-open is CTO's call.
- **L'Arlot's monopole map corrects a likely floor assumption.** Three clos are monopoles —
  `Clos des Forêts Saint Georges` (7.2 ha), `Clos de l'Arlot`, `Clos du Chapeau` (1.6 ha) — while
  **Les Suchots and Romanée-Saint-Vivant are not.** The cheapest OBP row ($210 Clos du Chapeau)
  *is* a monopole; the $3,700 Romanée-Saint-Vivant is not. **RSV 2023 is officially confirmed**
  (producer-signed fiche technique; first Arlot vintage was **1991**).
- ⚠️ **A producer can contradict itself, and both readings must be kept.** L'Arlot's website gives
  three different organic dates in one sentence (practices since 2000 / AB certification 2014 /
  organic farming initiated 2003); the Agence Bio register gives `datePremierEngagement`
  **2010-07-16**. Neither is asserted alone. Similarly Roulot's two legal entities (SCEA 1983, GFA
  2012) are reported as registry data and explicitly **not** interpreted as a succession story.
- **Importer sheets were rejected on authorship, not on content.** A Kermit Lynch PDF for Roulot
  carrying vineyard hectares, vine ages and a founding date was refused — third-person marketing,
  no domaine byline — and cached as `IMPORTER_…`. The same test excluded Skurnik and Grand Cru
  Selections for Bachelet-Monnot. **The importer-technical-sheet exception requires demonstrable
  domaine authorship; none of these met it.**
- ⚠️ **Two silent-failure traps to carry forward.** (1) **INAO extranet filenames are inconsistent
  across appellations** — hyphenated works for Chassagne-Montrachet, all-lowercase-no-hyphen
  (`pnocdcpuligny-montrachet.pdf`) for Puligny, and **no hyphens at all**
  (`PNOCDCSavennieresCouleeDeSerrant.pdf`) for Savennières. A wrong guess returns **HTTP 200 with
  HTML**, so it fails silently; always verify the body is a real PDF. (2) **Coulée de Serrant's
  English pages are degraded machine translation** with *different numbers* from the French
  (`Coulée`→"Casting", `rendement`→"output"). **Always take the French.**
- **Site authenticity: zero look-alikes adopted, and one instructive near-miss.** No fake producer
  site appeared in Batch 8. The Chassagne-Montrachet village syndicat site passed three of four
  checks — its Niellon page's address matches the company register **exactly** — but has **no legal
  notice**, so it was capped at `📄` and never `✅`, with every narrative claim drawn from it sealed
  in Must-Not-Say. Two adjacency risks were held strictly separate: Nicolas Joly's
  `renaissance-des-appellations.com` (his association, not the domaine) and his books, neither used
  as a fact source.
- ⚠️ **The intake file and the store-layer mapping disagree.** For Bachelet-Monnot,
  `obp_intake_normalized_20260804.json` reports all five rows `match_state = exact`, but
  `research/out/t-01/mapping.json` resolves only the three 1er Crus to `canonical_release`; both
  village Pulignys fall to a `research_shell` (`rs:pro:3b2de71b94633613`) with only the producer
  bound. Accurate phrasing is **producer 5/5, release 3/5**. Canonical records for the village wines
  *do* exist, so this reads as a wiring gap rather than missing data. **Coverage figures in this
  document are computed from the intake file** via `coverage.py` and are unaffected, but the
  discrepancy needs adjudication before anyone reports "resolved" counts from the store layer.

**Batch 9 notes (complete — 6 of 6).**
- **All six cleared the bar**: Clos de Tart ~90%, Armand Heitz ~90%, Bergström ~85%, Harlan Estate
  ~85%, Abreu ~82%, Hundred Acre ~78%. The New World / corporate-estate hypothesis in the Batch 9
  proposal held — these producers publish per-vintage technical data, and none needed the
  no-website fallback route.
- ✅ **The resume prediction was correct.** `hundred-acre`, `abreu-vineyards` and `bergstrom-wines`
  were written from their existing caches (122 / 42 / 70 files) with **no new research sweep** —
  only targeted gap-filling. The caches were left byte-intact. This is now a demonstrated pattern:
  **a spend-limit stop mid-batch costs the writing pass, not the research.**
- 🔴 **Hundred Acre: 4 of its 5 OBP rows are not Hundred Acre wines.** One company (`One True Vine,
  LLC`) runs three separately-branded wineries. `'Fortunate Son'` (rows 3–4) is bought-in fruit at
  a different winery — the proprietor writes verbatim *"Make no mistake this wine is NOT Hundred
  Acre"*. `'Summer Dreams'` (rows 1–2) files its 2025 labels under a **separate legal entity**,
  `Summer Dreams Wines LLC`, Healdsburg. **Only row 5 (`'Ark'`) is Hundred Acre.** This is the
  **second instance** of the Harlan/Mascot brand-axis shape in one batch. Escalated, not fixed.
- 🔴 **The `Ark` label says `NAPA VALLEY`, not Howell Mountain.** Both TTB COLAs declare the
  appellation as Napa Valley and the approved front label prints it; the string `Howell` appears in
  **no** producer source and in **none** of the 105 TTB records. Canonical's
  `subregion = "Napa Valley — Howell Mountain"` has no primary-source backing — an
  **attribute-provenance** problem that fits none of `P-1`…`S-4` or `CAT-1`…`CAT-9`.
- 🔴 **Abreu is absent from canonical entirely, and so is every one of its vineyard names.** 928
  records / 383 distinct producers: zero hits for `Abreu`, and zero for `Madrona`, `Thorevilos`,
  `Posadas`, `Cappella`, `Rothwell`, `Tilting`. The matcher never even raised a candidate. Recorded
  as a **gap, not a conflict** — no register class covers "producer not present", and forcing one
  would be wrong.
- **Abreu's `Napa Valley` on Thorevilos is correct, not menu sloppiness.** David Abreu states on the
  official page that Thorevilos *"doesn't belong to any sub-appellation"* — the vineyard sits
  between the St. Helena and Howell Mountain AVAs. **No conflict was manufactured.** Two of the
  three menu cuvée names are abbreviations, though: official forms are **`Las Posadas Howell
  Mountain`** and **`Madrona Ranch`**.
- 🔴 **Abreu never calls these wines "Cabernet Sauvignon."** The word appears **zero times** across
  all seven official wine pages; the self-description is `single-site Cabernet blends`, and the
  winemaker explicitly rejects varietal percentages. Under 27 CFR §4.23(b) a `Cabernet Sauvignon`
  designation needs ≥75%. Same shape as Harlan's `Proprietary Blend` and Mayacamas' `Red Wine` —
  now a **fourth** instance of the menu printing a category word as fact.
- 🔴 **Bergström's certification question is settled in both directions.** All five vineyard pages
  carry the producer's own field `Farming Style: 0% conventional, non-certified BD/regenerative-
  ecological` — *the producer itself says non-certified* — while the marketing copy says "We are
  Biodynamic farmers". Demeter USA's directory was browsed by letter and **resolves completely for
  `B` (13 entries, Bergström absent)**, with four other Oregon members present, so this is a
  **proved negative, not a coverage artefact**. USDA Organic INTEGRITY was a JS shell and the Oregon
  Wine Board was Cloudflare-gated, so **no claim is made about organic certification**.
- ⚠️ **Bergström OBP row 5 (`Dundee Hills Pinot Noir`, 2023, $440) carries no cuvée name at all.**
  Four independent lines point to **`Bergström Vineyard Pinot Noir`** — sole Dundee Hills estate
  vineyard, sole 2023 Dundee Hills red in the producer's catalogue, and a price within $3 of the
  measured markup. **It was routed to Open Questions as a physical-bottle task, not written as
  fact.**
- **Canonical holds zero Oregon producers.** All 79 USA records are `region='California'`. A
  vocabulary decision, not a Bergström-specific miss.
- ✅ **TTB COLA was reachable for both US producers this time** (108 Bergström records, 105 Hundred
  Acre) — unlike Harlan and Abreu in the same batch, where it returned a CAPTCHA and execution
  **declined to bypass it**. Same registry, different outcomes; availability is not stable.
- 🔴 **`Harlan Estate` and `The Mascot` are different legal entities.** `The Mascot, LLC.` is named
  verbatim in its own legal terms, and draws fruit from the **younger vines of three separate
  estates** (Harlan Estate, Promontory, the BOND vineyards), vinified at each winery and combined
  only at the final blending table. `harlanestate.com` never mentions it. **3 of the 5 Harlan OBP
  rows are therefore attributed to the wrong producer.** Escalated, not fixed.
- 🔴 **A third instance of the menu printing a category word as a cuvée name.**
  `Oakville Proprietary Blend` ($5,600) is not a name — the wine is simply **`Harlan Estate`**, and
  the string `Proprietary Blend` appears in no official source. Identical to Batch 7's Mayacamas
  (`Red Wine`) and Batch 4's Grgich (`'Estate,'`). Related catch: **`Oakville` must not be recorded
  as the appellation** — 27 CFR §9.134 puts the AVA's western boundary at the 500-foot contour while
  the producer's own geology essay places the vineyards at **325–550 feet**, straddling it, and the
  official site states no appellation at all.
- 🔴 **A producer/cuvée same-string collision — a new shape, left unnumbered.** For Clos de Tart the
  `producer` and the cuvée `name` are the identical string, producing the entity
  `cuvee:clos-de-tart-clos-de-tart`. Demonstrable harm: `La Forge de Tart` scores **0.7143** against
  `Clos de Tart` on the tokens `de` + `Tart` — **both of them producer-name tokens** bleeding into
  cuvée matching. A canonical-wide inventory is needed (`Clos des Lambrays`, `Château Latour` … are
  the same shape) **before** anyone assigns a number.
- **Clos de Tart's statutory basis for `La Forge de Tart` was found, not assumed.** Morey-Saint-Denis
  cahier des charges **IV.2°c)** lets wine from the delimited Clos de Tart parcels claim MSD premier
  cru ***sans nom du climat d'origine***. `La Forge` is an estate sub-plot name, not a classified
  climat. Ownership is **Artémis Domaines since 2018** (Mommessin 1932–2018), and the Ecocert
  registration `dateEngagement 2018-04-16` closes the prior Bureau Veritas registration **on the
  same day** — a clean handover matching the ownership change.
- 🔴 **Canonical prose failed verification for a third and fourth producer.** `clos-de-tart-2018`
  states `aging: "new oak 50%"` against an official **80%**, `7.5ha` against **7.53**, names two
  winemakers found in **no** official source, carries an unsourced `points: 96`, and its Japanese
  description calls the owner a retail conglomerate rather than Artémis Domaines. This now spans
  Coulée de Serrant, Bachelet-Monnot, Clos de Tart and (per Armand Heitz) canonical élevage months.
  **`obp_note` and `description` are not trustworthy without verification.**
- ⚠️ **Armand Heitz bounded an unanswerable question rather than guessing it.** OBP row 5
  ($3,400 Chevalier-Montrachet) prints `?` for the vintage. The producer states 2013 was its first
  millésime, so the candidate set is "2013 onward" — **the dossier establishes the ceiling and
  refuses to name a year.** The parcel is **0.0966 ha**. Also confirmed: INAO *and* the producer
  both write **`Perrières` without the article**; only the menu adds `Les`.
- 🔴 **The intake ↔ mapping divergence is now confirmed four times** — Bachelet-Monnot (Batch 8),
  Clos de Tart, Armand Heitz, and now Hundred Acre. In the first three,
  `obp_intake_normalized_20260804.json` reports a cuvée-level `exact` match that
  `research/out/t-01/mapping.json` does not carry. **Hundred Acre is worse and different in kind**:
  in this checkout's `research/store/t-01/shells.json` (2026-07-29) the two Summer Dreams rows are
  **parse-broken** — `producer_or_brand` swallowed the whole line
  (`"2024\t\t'Summer Dreams, The Sun Also Rises,'"`), `original_raw_line` retains only the tail, and
  `canonical` is `{}`. So in the snapshot on disk those rows have **no producer at all**, where the
  intake package reports `producer_state: exact`. **Three independent agents have now flagged this
  unprompted, two of them pushing back on a briefing premise.** Systematic, not incidental.
  **Coverage figures in this document come from the intake file via `coverage.py` and are
  unaffected**, but no "resolved" count should be quoted without naming its artifact.
- **A fifth look-alike site, and a refusal worth recording.** `themascotwine.com` is a GoDaddy
  parking lander; the real site is **`mascotwine.com`** — a one-letter trap. Separately, when the
  **TTB COLA registry** returned a bot challenge demanding a CAPTCHA, execution **declined to
  bypass it** and recorded the label data as unverified rather than substituting a merchant source.
- **Two more INAO filename forms** beyond Batch 8's three: `PNOCDCClos-de-Tart.pdf` and
  `PNOCDC-MoreySaintDenis.pdf`. Seven wrong guesses again returned **HTTP 200 with HTML**. Also:
  `clos-de-tart.com` publishes **no `robots.txt` and no sitemap**, and every unknown URL returns a
  183 KB soft-404 at HTTP 200 — URL structure had to be read off the homepage navigation.

**Batch 10 notes (complete — 6 of 6).**
- **All six cleared the bar and all six are Confidence High** — Roederer ~88%, Billecart-Salmon
  ~88%, Olivier Leflaive ~82%, Famille Moussé ~80%, Laurent-Perrier ~80%, Chateau Montelena ~80%.
  This is the **first batch since Batch 4 with no sub-bar dossier**, and the reason is selection:
  every one of the six is a commercially substantial house that publishes **fiches techniques**.
  The batch ran at a **maximum of 2 concurrent agents** throughout.
- 🔴🔴 **The dominant finding, and it is now a base rate rather than a sample: canonical's stored
  values contradict producer-official sources for all six producers.** Batches 8–9 recorded this as
  *unsourced prose* in `obp_note` / `description` for four producers. Batch 10 shows it **extends
  into typed structured fields** — `grapes`, `dosage`, `aging`, `founded_year`, `subregion`.
  Ten of ten producers examined this way have now failed:
  - **Billecart-Salmon — 19 contradicted items across all 4 records.** Grape splits inverted,
    dosages `5 / 6 / 7 g/L` against official **3.9 / 3.8 / Extra Brut**, `founded 1816` against
    **1818**, an **invented parcel ("Mont Blanche")**, an "1830s rosé tradition" against the
    domaine's official **1970s**, and unsourced MLF and hand-disgorgement claims.
  - **Louis Roederer — one `house_style` string duplicated verbatim across all 16 records**,
    asserting (i) rosé "via **saignée** … with red wine" and (ii) fruit "**Demeter-certified**".
    **Both are false.** The house's own word is `infusion`; `saignée` appears in no official source,
    and Demeter France returns zero results. The same field also carries **96–98 point scores that
    exist nowhere official.**
  - **Laurent-Perrier** — `saignée` and `MLF performed` asserted where the house says `macération`
    exclusively; `Ch 55 / PN 45` matching **neither** official figure; "#26 is the latest release"
    when **Nº27 shipped January 2026**.
  - **Famille Moussé** — `grapes = Pinot Meunier 100%` against official **80% Meunier / 20% Pinot
    Noir**; `dosage 3 g/L` against **2.5** and **0.5**.
  - **Chateau Montelena** — `100% CS` against **94.1 / 99 / 99** across the three vintages;
    "restrained new oak" against **45% new**; a *Bottle Shock* film claim appearing in **zero**
    producer sources.
  - **Olivier Leflaive** — the **intake** `evidence` string asserts a négociant arm "separated in
    1984"; **both halves are unsupported by any official source.**
  🔴 **This is the highest-severity finding of the batch, and it is floor-facing text.** It is
  measurement, not adjudication, that is missing — nobody has swept the field.
- 🔴 **The matcher never reads the menu section heading, and Roederer proves it.** The intake
  `evidence` string is **byte-identical across all four Roederer rows including the ROSÉ one.**
  Canonical is **not** missing the colour axis here: it carries four Cristal cuvées, and row 4's
  correct target `cristal-rose-2014` **already exists and is factually correct**. **Billecart-Salmon
  is a second counter-example** — four records, prestige white and prestige rosé already split.
  ⚠️ **Consequence for `C-6`: its premise needs splitting.** Canonical structure and matcher input
  are two different defects, and **fixing canonical alone does not fix the row.** Evidence added to
  `C-6`'s second recommendation only; the direct family for these rows is **`C-4`**.
- 🔴 **`V-1` is sharper than the register records, and Laurent-Perrier is why.** Grand Siècle's
  three base vintages **overlap between itérations** — 2008/2007 in both Nº25 and Nº26, 2012 in both
  Nº26 and Nº27. So unlike Krug, **`base_year` does not even work as a surrogate key: there is no
  correct value for the `vintage` field.** A "fix the vintage field" migration would not merely
  mangle this data — **it has nothing to write.** Worse, adding Nº27 under the present schema makes
  **`(cuvée, vintage="NV")` non-unique inside canonical**, so the schema blocks its own gap fill.
  Roederer's `Collection 246` (= the house's **246th assemblage**, base vintage **2021**) would be a
  further notation; a re-measurement of the current export found **26 records / 7 notations** against
  the register's 24 / 5 — **noted, not adjudicated.**
  ⚠️ **`Grande Cuvée` is Krug's cuvée name.** Any normalisation rule mapping the menu's
  `Grande Cuvée No. 26` onto the official `Itération Nº26` **would collide with the producer at the
  centre of `V-1`.**
- 🔴 **`V-2` is undercounted and `V-3` extends.** Four magnum records exist, **three with no
  standard-bottle sibling**, and format is **double-encoded** in `name` *and* in the existing
  `obp_format` field. Grand Siècle `Les Réserves` releases the **same itération number twice** as
  undisgorged magnums, so identity needs **itération × format × disgorgement state** — two keys are
  insufficient, not just one.
- 🔴 **`P-2`'s recorded impact is wrong, and downward.** The register states 3 OBP bottles held in
  false unresolved. **Measured: 1.** Canonical holds a single Fortes Terres record
  (`mousse-fortes-terres-2018`); OBP has 2018 / 2019 / 2020, so an entity merge resolves **2018
  only**. **`P-2` decomposes into 1 entity-split + 2 vintage gaps.**
  ✅ **The official confirmation `P-2` asked for has been obtained.** Agence Bio operator
  `numeroBio 44958` carries **one SIRET `449 670 702 00025`** bearing **both** names —
  `raisonSociale = SARL CHAMPAGNE MOUSSÉ FILS` and `denominationcourante = SARL FAMILLE MOUSSÉ`,
  gérant Cédric Moussé. **One house, two names.** Merging remains **the CTO's call, not executed**;
  `REGISTER.md` was not written to.
- 🔴 **A new brand-axis sub-shape, and it is harder than the three known instances: the axis lives
  *inside* the cuvée string.** Olivier Leflaive's **`Récolte du Domaine`** distinguishes estate fruit
  from bought fruit at **identical producer, appellation and vintage** — 8 cuvées carry it in 2023,
  proven three ways (page `<h2>`, official fiche PDF title line, and the EN page leaving it
  untranslated). Unlike Harlan/The Mascot or `P-6`/`P-7`, **there is no separate entity to point
  at.** Cited to the **proposed** `CAT-3`, which names this producer verbatim and is still
  unadjudicated. **No number opened.**
- 🔴 **`D-2026-08-05-08`'s failure condition was demonstrated live.** Olivier Leflaive is absent from
  canonical **at the producer layer**. Of the **16 records matching `leflaive`: 7 are Domaine
  Leflaive, 0 are Olivier Leflaive, and 9 matched only because "Leflaive" appears in *other
  producers'* prose** (Mortet, d'Auvenay, Lafon ×2, La Pierre Ronde ×2, Sauzet ×2, Ramonet).
  🏛 **Four distinct SIRENs confirmed** — Olivier Leflaive Frères `332 160 092` (NAF 11.02B),
  Domaine Leflaive `778 245 316` (NAF 01.21Z, different street), Domaines Leflaive `490 715 836`,
  Valentin Leflaive `808 335 251`. **Substring matching on `Leflaive` is exactly the defect that
  corrupted the coverage figure by 11 bottles.**
- **Canonical gaps widened across the batch** — Roederer's whole `Collection` line, `cristal-2016`
  and essentially the entire non-Cristal range; Laurent-Perrier's Nº27 and Alexandra 2012 (7 of 9
  official cuvées absent); Montelena's Chardonnay and non-Estate Cabernet (**one** record total, and
  it carries `vintage='—'`, so rows 3 and 4 cannot both resolve to it); Moussé's 7 of 10 cuvées.
  **These stay out of the register as gaps.**
- ⚠️ **Laurent-Perrier row 2 is *not* a gap** — `laurent-perrier-grand-siecle-26` exists and is
  **unreachable**, because the identifier is spelled three ways. **Treating it as a gap would have
  created a duplicate record.** The gap/unreachable distinction is load-bearing.
- 🔴 **The menu is not reliably the defective side — three counter-examples in one batch, and the
  "category word as cuvée name" pattern did not recur.** (1) Billecart's `Le Réserve` **is** the
  producer's own current name: the house has renamed its NV range (`Brut Réserve`→`Le Réserve`,
  `Brut Rosé`→`Le Rosé`) and moved the Collection to Extra Brut dosage — the residue is **a rename
  in progress that canonical has no way to express** (new shape, unnumbered). (2) Montelena rows 1–2
  print the producer's **actual product names**, and rows 3–4 reproduce the **label's gold banner**;
  the menu is **more faithful to the label than `montelena.com`**, which uses three different forms
  of the same wine's name on one page — **the instability is the producer's, not the menu's.**
  (3) Montelena's canonical `subregion = "Napa Valley — Calistoga"` **is** primary-source backed
  (label reads `CALISTOGA · NAPA VALLEY`; Calistoga **27 CFR §9.209** sits inside Napa Valley
  §9.23, established by **T.D. TTB-83, 74 FR 64612**, petitioned by Chateau Montelena's own Bo
  Barrett) — **a clean counter-example to Batch 9's attribute-provenance shape.**
  **Pattern existence is not evidence that a given row is another instance.**
- ⚠️ **"Practised vs certified" decided the Farming section for all six, landing differently every
  time.** Moussé: Ecocert `FR-BIO-01`, **first engagement 2022-09-01** — **all three OBP vintages
  predate conversion**, so these bottles must not be called organic, and the site never mentions
  certification at all. Roederer: **135 ha certified organic** (Ecocert, engagement 2018-03-12,
  `mixité: Oui`), **Demeter France returns zero** — its biodynamic language stops at *practice*.
  Billecart: an active Ecocert certification **the official site never mentions**, but scoped to
  **`Préparation` only** — so **both** "Billecart is organic" and "Billecart has no certification"
  are false, and the must-not-say list blocks both directions. Montelena: the producer publishes
  **nothing** — Farming is **Low** and marked so, and a distributor's "solar power / conscious
  farming" claims were **routed to must-not-say rather than used**. Olivier Leflaive: organic
  absence **proved** (Agence Bio `nbTotal: 0`, `est_bio: false`), with **HVE 3 on 15 of 74 cuvées
  and `Raisonnée` on 58** — and the marker and the certification **do not coincide** (the 8
  `Récolte du Domaine` wines are all HVE 3, but 7 further HVE 3 wines do not carry the name).
  **No rule was invented; it went to Open Questions.**
- **Site authenticity: 6 of 6 passed and zero look-alikes were encountered** — the first batch with
  no reject since the check became standing (`D-2026-08-05-09`). Two adjacency risks were held
  strictly separate: Roederer's sibling estates (Deutz, Delas, Pichon Comtesse, Roederer Estate …)
  and the four Leflaive legal entities — **`domaine-leflaive.com` and `leflaive.fr` were never
  opened.** `billecart-salmon.com` is **NXDOMAIN** (an IP Twins defensive registration) — unusable,
  **not fraudulent**. ⚠️ Roederer's own `/fr/sitemap.xml` emits **148 entries pointing at a staging
  host** (`roederer-site.pp.mzrn.net`) — **a config leak on the genuine site, not an impostor**;
  nothing was fetched from it.
- ⚠️ **Traps, re-confirmed and extended.** The **INAO filename trap fired again**:
  `PNOCDC-Pernand-Vergelesses.pdf` and `PNOCDC-Batard-Montrachet.pdf` return **HTTP 200 with HTML**;
  the working names are `PNOCDCPernand-Vergelesses.pdf` / `PNOCDCBatard-Montrachet.pdf`. **TTB COLA
  was CAPTCHA-gated for Montelena and fully open for Billecart in the same batch** — availability
  remains unstable and **the challenge was not bypassed**; Montelena's label data came from
  producer-published bottle-shot imagery and is flagged as such. **Alcohol age gates are
  self-declarations, not bot challenges** (Moussé, Roederer, US wineries) and were entered via each
  site's own link.
- ⚠️ **`Special Club` has no basis in the producer's own sources.** Canonical's cuvée name embeds
  it, but `club` / `spécial` / `special` occur **0 times** across 69,221 characters of Moussé's
  official site, and `mousse` occurs **0 times** in the Club Trésors de Champagne roster of 25
  members. Whether a **cross-producer collective designation** belongs inside a name string at all
  is a real modelling question — **described, not decided.**
- **Physical-label tasks added: 10**, bringing the floor total to **18**. See `NEXT_ACTIONS.md` §3f.

**Batch 11 notes (complete — 6 of 6).**
- **Four cleared the bar** — Vilmart & Cie ~85% (High), Anne et Hervé Sigaut ~78% (Medium-High),
  Henri Giraud ~76% (Medium), Alvina Pernot ~74% (Medium). **Two are deliberately below it and
  marked `awaiting material from the team`** — René & Vincent Dauvissat ~64%, Thierry Allemand ~62%.
  **+24 bottles; the estimate was exact.** The batch ran at a **maximum of 2 concurrent agents**
  throughout.
- ✅ **`NEXT_ACTIONS.md`'s risk warning was correct and is now measured.** The six remaining
  4-bottle producers were flagged as carrying the Roulot / Niellon profile, and the batch produced
  the **first sub-bar dossiers since Batch 8** — but only two of six, not all six. **The yield held
  (+24, exactly as projected) while the quality dropped**, which is the trade the warning described.
- 🔴🔴 **The dominant methodological finding: "the producer publishes nothing" is not one condition
  but at least six, and they need different responses.** Batch 8 proved absence for Roulot (OVH
  placeholder), Bachelet-Monnot (MX-only) and Niellon (no domain). Batch 11 adds **four more
  distinct shapes in a single batch**:
  - **Publishing stopped, site still live** (Henri Giraud) — `champagne-giraud.com` is now a splash
    + legal site: 8 pages, 4 PDFs, all 2025 event programmes, **zero fiches techniques**.
  - **Site frozen at a past vintage** (Sigaut) — all 11 wine pages stop at **2019**, last news item
    **2020-12-29**. Every OBP row (2022, 2023) is a vintage the domaine has never documented.
  - **Domain owned but never published** (Alvina Pernot) — `alvinapernot.com` has a live A record
    and MX, registered one month after incorporation, and `GET /` returns **9 bytes** (`<!-- -->`).
    The sole Wayback capture is byte-identical.
  - **Domain never registered at all** (Thierry Allemand) — `.com` ×3 → Verisign RDAP 404, `.fr` ×2
    → AFNIC `NOT_FOUND_DOMAIN_NAME_WITH_NAME`, Wayback returns HTTP **200** with
    `archived_snapshots: {}` (a resolving negative, not a gate).
  - A fifth register-side variant: **Agence Bio holding a `Site Officiel` record whose `url` is an
    empty string** (Dauvissat) — neither Roulot's `[]` nor Pernot's blank body.
  🔴 **Consequence: `awaiting material from the team` is too coarse a status.** Giraud's and
  Sigaut's material *existed and was published*; Dauvissat's and Allemand's never did. The first
  two are recoverable by archive work, the last two only by procurement.
- ✅ **Internet-Archive recovery of a producer's own former pages is now an established route.**
  Henri Giraud's entire cuvée substance came from archived copies of the house's own pages,
  **authenticated by the mentions-légales block embedded in each capture** and tagged `📄`
  throughout, kept strictly distinct from `✅` live content. ⚠️ Wayback returned **HTTP 429** for
  one agent in the same batch — **a gate is not evidence of absence.**
- 🔴🔴 **Site authenticity: nine look-alikes rejected in one batch — more than the previous five
  batches combined, and one of them was in the briefing.** `vilmart.fr` (**Dovendi** domain-for-sale
  parking, the same operator as Batch 6's `ramonet.fr`), `champagnegiraud.com` (Afternic parking,
  **one character** from the real domain), `apwines.com` (**Andrew Peace Wines, Australia**),
  `dauvissat.fr` (Dovendi for-sale, WHOIS holder `Nomio24` — **the same registrant as the Vilmart
  catch**), `dauvissat.com` (redirects to a personal LinkedIn), `domaine-dauvissat.fr` (**a
  genuinely different estate, at Beine**), `allemand.fr` (unrelated Wix 404). **Zero words were
  used from any of them.**
  🔴 **`vilmart.fr` was supplied to the agent by the orchestrator as the likely official domain.**
  The pre-check caught it. **This is the strongest evidence yet that `D-2026-08-05-09` must run even
  when the domain looks obvious — including when the briefing asserts it.**
- 🔴 **`D-2026-08-05-08` (substring matching on a name) fired in five of six producers**, and the
  entity counts are larger than any previous batch: **11 distinct registered `Dauvissat` entities**
  (the subject is three co-located legal persons, and **`Dauvissat-Camus` is the land-holding GFA,
  not a wine brand**); **three Vilmart entities in one village**; a separate
  **`DOMAINE ELISA SIGAUT`** (SIREN 917436057) in Chambolle; a separate **`THEO ALLEMAND`** sole
  trader at the same address and NAF as the subject; and `ALLEMAND INVEST` / `GARAGE ALLEMAND` in
  the register. 🔴 **A new place for it to fire: Agence Bio's own search API returns `LALLEMAND`
  entries for a `nom=allemand` query** — which is precisely why **only an exact-SIRET negative
  counts as a proved negative.**
- 🔴 **A non-vintage Cornas is a counter-example to `D-2026-08-05-12`'s reading of `'NV'`.** That
  sweep measured 88 `'NV'` records and held them **legitimate for non-vintage Champagne**.
  `allemand-chaillot-nv` is a **Cornas** — the INAO CDC reserves the appellation for
  *vins tranquilles rouges*, records "Pas de disposition particulière" for complementary geographic
  mentions, and anchors the whole claim regime to the `déclaration de récolte`. **So the 88 cannot
  be treated as a homogeneous legitimate class; the reading needs restating per appellation.**
  The record is **distinct, not a phantom**: it uniquely carries `dosage: "N/A — Still Wine"` — a
  **Champagne field on a Rhône record** — alongside `vintage: "NV"`, plus three sibling divergences
  (`name` embeds the appellation, `subregion`, `classification`). Template-derived. The
  `"Chaillot" Cornas` name shape is the **inverse of `C-4`** (Batch 10's Montelena finding).
  **No number opened.**
- 🔴 **`S-2` gains its sharpest evidence yet, and it explains why the count reached 175.** At Alvina
  Pernot the matcher's own `evidence` strings read `'La Garenne' ≡ '"La Garenne"'` at
  **`confidence: 1.0`** — **the quote-mark corruption is invisible to matching**, so
  *"it matches, therefore the record is healthy"* fails for this entire family. Thierry Allemand
  shows the same defect rendered **two different ways within four rows of one producer**: the
  Reynard rows propagate the quotes downstream into `proposed_canonical_cuvee`, the Chaillot rows
  normalise them away. **Evidence added; no new number.**
- 🔴 **Blanket article/accent normalisation is now refuted by a concrete counter-example, not just
  cautioned against.** Dauvissat's `La Forest` appears **0 times** in either INAO Chablis cahier;
  the legal forms are `Forêts` / `Les Forêts` (under the `Montmains` umbrella) and BIVB prints a
  third form, `Forêt`. 🔴 **And `La Forêt` and `Sur la Forêt` genuinely exist under a *different*
  umbrella (`Vau Ligneau`) — so naive normalisation lands `La Forest` on the wrong vineyard.**
  This needs an **explicit alias**, the Batch 8 `Les Champs Gains` precedent. Related floor-facing
  catch: **`Les Clos` is the only one of the seven Chablis Grand Cru climats carrying an article —
  do not strip it.** Sigaut independently reproduced INAO self-inconsistency inside a single
  24-row list, including one row where INAO prints two spellings itself
  (`Les Feusselottes (ou Les Feusselotes)`).
- 🔴 **Canonical's stored values: the count is now 13 of 14 producers, and Batch 11 separates three
  distinct failure modes that had been collapsed into one.** Thierry Allemand carries all three at
  once: **contradicted** (`vintage: NV`; a `Biodynamic` tag with **no certification of any kind**;
  a Chaillot-subject `description` **byte-identical across all five records including both Reynard
  ones** — the Roederer duplication shape), **unsourced** (`aging "18+ months"`, `winemaking`,
  `tasting`, `points: 95`, `drinking_window`, vine ages), and **absent as key** (`grapes` missing
  on both Reynard records though present and INAO-correct on the Chaillot ones; `obp_note` present
  **only** on the impossible NV record and absent from all four rows actually on the menu).
  🔴 **Alvina Pernot is the exception and it is instructive: all four of her records are bare
  shells** — `grapes`, `aging`, `founded_year`, `description`, `obp_note`, `winemaking`, `tasting`,
  `points` absent **as keys**, so field-verification was unexecutable on 10 of 10 fields. **Canonical
  is not wrong there; it is empty** — while all four rows read `match_state = exact` at
  `confidence 1.0` against a $360 / $640 / $720 / $720 lineup. **A distinct shape, unnumbered.**
- 🔴 **A fourth counter-example to "the menu is the defective side" — and, for the first time since
  the caution was written, a clean case where the menu *is* the defective side.**
  Counter-example: INAO ×2 and BIVB all print `La Pièce sous le Bois` with **lowercase *sous***;
  OBP matches them exactly; **canonical alone** writes `"La Pièce Sous le Bois"`.
  The genuine menu defect: **OBP misspells `Theirry Allemand` on all four Rhône rows** (i/r
  transposition), against INSEE/Sirene's `THIERRY ALLEMAND` (SIREN 432434637).
  ⚠️ **Both directions now have worked examples. The caution is about not assuming — not about
  never blaming the menu.**
- 🔴 **`match_state = exact` is repeatedly under-specified rather than correct.** Sigaut row 1 binds
  a $240 village Chambolle to a cuvée id carrying **no lieu-dit**, while the domaine bottles
  **three** village-level Chambolles (`village`, `Derrière le Four`, `Les Bussières`) — a `C-4`-shaped
  sink. Henri Giraud row 1 is `exact` at `confidence 1.0` while the **menu says `Brut Nature`,
  canonical says `Brut`, and the house says neither** — the dosage axis is simply not compared.
  Vilmart inverts it: **the only row intake marked resolved (`Coeur de Cuvée 2016`) is the only row
  that could not be confirmed officially**, while the `unresolved` 2017 has a full fiche.
  **`match_state` measures canonical agreement, not existence.**
- 🔴 **A cross-producer binding hazard, `P-1`-shaped.** `arlaud-les-sentiers-2021` is the **same
  climat under a different producer** as Sigaut's row 4. A producer-relaxing matcher would bind the
  row to Domaine Arlaud. Dauvissat has the identical shape:
  `raveneau-montee-de-tonnerre-2021` is the same climat **and the same vintage** as its row 3 —
  which is why that row is a **producer-level** gap, not a cuvée-level one.
- ⚠️ **"Practised vs certified" landed in four more distinct configurations, and the temporal trap
  is now the recurring one.** Giraud: 🏛 Agence Bio `ENGAGEE` but **`etatProduction: C2`** (second
  conversion year), `activites: [Production]` only — **the exact inverse of Billecart's
  `Préparation`-only** — so both OBP vintages (2016, 2022) predate the current cycle and **neither
  "organic" nor "no organic registration" may be said.** Dauvissat: Ecocert `FR-BIO-01`,
  **`datePremierEngagement 2021-04-27`**, scope `Agriculteur (production végétale)` — **farming
  only, not winemaking** — so 2019 predates certification entirely and 2021 is conversion year one.
  Allemand: **no certification of any kind**, proved three ways (exact-SIRET ×3 → `nbTotal: 0`;
  the **Biodyvin 2025 member list, 224 names, fully resolving** → no `ALLEMAND`, no `CORNAS`; and
  **Demeter France's 2024 CDC p.16 makes organic certification a `condition préalable`**, so Demeter
  is structurally impossible) — **which contradicts canonical's `Biodynamic` tag outright.**
  Pernot and Sigaut: proved negatives by exact SIRET (`nbTotal: 0`, ×4 entities for Sigaut).
  🔴 **The temporal trap now has three instances** (Moussé, Giraud, Dauvissat): **a current
  certification says nothing about a bottle whose vintage predates it.**
- 🔴 **Thierry Allemand's most-asked question was refused, deliberately.** The sulphur regime for
  1998 / 1999 / 2001 / 2006 has **no producer source for any year**, and third-party accounts
  disagree among themselves. **No blanket claim was made in either direction** — it is the first
  item on the must-not-say list and a physical-label task. These are the batch's most expensive
  bottles ($1,600–$2,600).
- ✅ **Cadastral evidence settled a below-INAO-granularity question.** `Chaillot` and `Reynard`
  occur **0 times** in the Cornas cahier — the Batch 8 Niellon `Truffière` shape — but DGFiP/Etalab
  confirms both as **real cadastral lieux-dits of commune 07070** (Chaillot ~17.8 ha, Reynard
  ~23.7 ha, abutting), and CDC XII.2°a) **explicitly permits a smaller unit on the label if it is a
  lieu-dit cadastré on the harvest declaration.** Unlike Chassagne, **Cornas has a general legal
  pathway** — and no premier cru or climat system at all.
- 🔴 **`Les Blanches Voies` is a parcel name, not a cuvée name.** Read off Vilmart's own bottle
  shots: `BLANC DE BLANCS 2011 / LES BLANCHES VOIES` and `BLANC DE NOIRS 2017 / LES BLANCHES VOIES`.
  The house calls these part of *"quatre cuvées millésimées"* and **no NV Blanc de Blancs exists in
  the range**, while the menu prints the row `NV` — and the house **never writes "Extra Brut"
  anywhere** (0 hits across all HTML + 12 fiches). A new menu-side shape — **a label's parcel
  sub-line printed as the cuvée name** — adjacent to `C-4` but distinct from the "category word as
  cuvée name" family. Routed to a physical-label task rather than declared a menu defect.
- ⚠️ **The INAO filename trap fired four more times and produced a *third* naming convention.**
  Working: `PNOCDCChablis.pdf`, `PNOCDCChablisGrandCru.pdf` (fully concatenated — every hyphenated
  Grand Cru variant is a decoy), `PNOCDC-Chambolle-Musigny.pdf` (**hyphen after `PNOCDC`**), and
  🔴 **`PNO2023AOPCornas.pdf` — the form `PNO<year>AOP<Name>.pdf`, unlike anything on record.**
  Failing guesses returned **HTTP 200 with HTML** (7 of 9 for Dauvissat, 9 of 9 for Allemand).
  🔴 **New caveat, found independently by three agents: several of these are opposition-procedure
  (PNO) drafts that merge struck-through old values with new ones in the extracted text**
  (`40 50 hl`, `171 180 g`, `20092021`, `115160 hectares`). **Bare number extraction would silently
  quote superseded figures** — only unmerged single values were used, and no yield or sugar figures
  were quoted where the pair was ambiguous.
- **Physical-label tasks added: 21**, bringing the floor total to **39**. See `NEXT_ACTIONS.md` §3g.

**Batch 12 notes (complete — 8 of 8). The Bordeaux block.**
- **All eight cleared the bar and all eight are Confidence High** — Margaux ~88%, d'Yquem ~88%,
  Mouton Rothschild ~88%, Latour ~88%, Haut-Brion ~88%, Giscours ~88%, Cos d'Estournel ~88%,
  Palmer ~85%. **+47 bottles; the estimate was exact.** Coverage **468 → 515 / 704 (66.5% → 73.2%)**.
  🔴 **This is the largest single-batch gain since Batch 5, and it came from the block every batch
  since Batch 5 had deferred.** The deferral reason (`NEXT_ACTIONS.md` §2) was that Bordeaux needs
  `facts.subregion` matching and is more efficient as one dedicated batch — which is what it got.
- ⚙️ **Run at 8 concurrent agents against Batches 10–11's maximum of 2, one producer per agent, no
  shared state.** No agent read another's producer. The parallelism held: no cross-contamination
  appeared, and **three agents independently converged on the same matcher defect from three
  different angles** (see below), which is corroboration a serial run would not have produced.
- 🔴🔴 **The dominant finding, and it is a pipeline defect rather than a data defect: the intake
  parser detects that no cuvée name was printed, and the matcher proposes one anyway.**
  Every OBP Bordeaux row prints the **appellation** in the wine-name column — `Margaux`, `Pauillac`,
  `Pessac-Léognan`, `Saint-Estèphe`, `Sauternes` — and the parser records this correctly:
  `_parts.label` is `null` on **69 of 69 Bordeaux rows** and on **292 of 704 rows corpus-wide**.
  🔴 **But 152 of those label-null rows still emit a `proposed_canonical_cuvee`, and 147 of the 152
  are marked `cuvee_state: exact`.**
  🔴🔴 **And the proposed cuvée is not an echo of the appellation — it is the grand vin.** For
  Giscours, `normalized_cuvee` holds `Margaux` while `proposed_canonical_cuvee` holds
  **`Château Giscours`** (`cuvee:chateau-giscours-chateau-giscours`); the six rows read `unresolved`
  only through `vintage_state`, never through `cuvee_state`. **So the matcher does not merely invent
  a cuvée from an appellation — it silently resolves grand-vin-versus-second-wine, on zero evidence,
  in favour of the grand vin, for exactly the rows this batch proves are undecidable from official
  sources.** Every château in the block bottles a second wine in the same appellation at a fraction
  of the price. Three independent demonstrations, none of which knew about the others:
  - **Mouton** — all six rows carry the evidence string
    `名称トークン集合一致: 'pauillac' ≡ 'Château Mouton-Rothschild'`. **The token sets share zero
    members.** `cuvee_state` is `exact` regardless, and two rows reach `confidence 1.0` on nothing
    but "a row with that vintage exists."
  - **Palmer** — the same shape (`{margaux}` vs `{château, palmer}`, zero overlap) with the
    distinction stated precisely: **`C-6` is evidence carrying *no* information; this is evidence
    carrying *false* information**, which actively misleads a reviewer rather than merely failing to
    help one.
  - **Haut-Brion / Giscours** — the store layer then preserves the empty `product_name` correctly
    and collapses the rows into a single shell keyed **without vintage**.
  → 🔴 **Detect → override → collapse, across three layers.** Fixing canonical cannot fix these rows.
  This is the sharpest available evidence for the **`C-6` premise split** Batch 10 asked for.
  🔴 **The override is unhedged in 96.7% of cases** (147 `exact`, 3 `alias`, 2 `candidate`), and
  `source_quality_flags` is **empty on every affected row**, so nothing warns a reviewer.
- 🔴 **A consequence that should be stated wherever match states are consumed: `exact` is not a
  stronger identification than `unresolved` here.** All six Haut-Brion rows are `producer_state:
  exact` **and** `cuvee_state: exact`; only `vintage_state` differs. **The 1993 and 1987 rows that
  read `match_state = exact` at `confidence 1.0` matched their cuvée on the same false token-set
  claim as the four `unresolved` rows** — the difference between them is purely whether canonical
  happens to hold that vintage. This is the fourth and sharpest instance of Batch 11's finding that
  **`match_state` measures canonical agreement, not existence.**
- 🔴 **The store-layer collapse is now measured, and it destroys price and vintage.** Haut-Brion:
  **$14,940 of listings in one shell** (`rs:pro:7e4577c3f98cf640`). Yquem: **six vintages and three
  prices in one shell** (`rs:pro:434164aa9498d56f`), vintage absent from shell identity, only the
  2017 transcription retained. Cos: `rs:rel:1354e538b20bd449` merges the **WHITE $680** and
  **RED $900** rows and **discards the $900 price**. **141 of 1047 shells are multi-line.**
  This is the **fifth-plus instance** of the intake↔store divergence (Bachelet-Monnot, Clos de Tart,
  Armand Heitz, Hundred Acre) and the first where the discarded axis had **already been flagged
  upstream**.
- ⚠️ **The intake `source_quality_flags` vocabulary is real, populated, and was nearly written off.**
  Eleven tokens over 704 rows: `missing_price` 28, `producer_spelling` 13, `cross_section_duplicate`
  8, `cuvee_spelling` 7, `canonical_model_note` 6, `format_in_name` 6, `disgorgement_in_name` 4,
  `section_colour_conflict` 3, `section_region_conflict` 2, `malformed_vintage` 2,
  `disgorgement_unknown` 1. 🔴 **Two flags are almost entirely Batch 12's**: all **6** `format_in_name`
  rows are Yquem, and **2 of the 3** `section_colour_conflict` rows are Cos d'Estournel.
  🔴 **Four of eight agents independently reported these flags as non-existent** — because the intake
  package lives **outside the repo** at `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`
  and each defaulted to the store layer's separate `flags` field inside it. **That was a defect in the
  batch briefing, not in the agents**, and all four were corrected. → workflow fix recorded in
  `NEXT_ACTIONS.md` §1.
- 🔴🔴 **Canonical is storing reference tables as wine records, and the scale is now measured at
  roughly 130 of 928 (~14%).** Three disjoint populations found independently:
  - **61 records** carry `1855 Médoc Classification · Nème Grand Cru Classé` and break down
    **5 / 14 / 14 / 10 / 18 — exactly the official 1855 red-list structure.** Canonical is holding
    the classification table itself. (Margaux corroborates from the other side: a **second**
    classification-string schema, `Premier Grand Cru Classé (1855)`, 5 records, attaches **only** to
    real bottles — so shell and bottle are distinguishable, and Lafite and Château Margaux are the
    only two premiers crus with **zero** bottle records.)
  - **37 records (4.0%)** whose provenance is a **third-party critic's reference book** — 34
    `Vintage Reference — Parker's Bordeaux` carrying `producer: "Bordeaux"` and **real year values**,
    2 `Château Profile`, 1 `Appellation Reference`. 🔴 **They carry `type: "Wine"`, `color`,
    `obp_format`, `glassware`, `serving_temp` and `food_pairings` — schema-indistinguishable from a
    sellable bottle.**
  - **35 records** hold a **region or appellation name in the `producer` field.**
  🔴 **Worse than inert: the shells are load-bearing.** `haut-brion-1855` is `vintage: "—"` and
  resolves to `vintage: {}`, yet it is the `_stub` source for cuvée facts — **its wrong values
  default onto the four vintages that have no record of their own.**
- 🔴 **The canonical base rate held for producers 15–22, but the shape is now more precisely
  characterised.** Failure counts: Margaux 18/33, Cos 21/33, Latour 20/40, Giscours 23/34,
  Mouton 23/48, Haut-Brion 34/61, Palmer 15/27, d'Yquem (2 records fully checked, 8 contradicted +
  8 unsourced of 38). ⚠️ **But Mouton supplies a real counter-example and it should temper the
  claim**: its **51-entry artist-label archive 1973–2023 matches the official list exactly, all 51**,
  and geography passes cleanly. **Failures concentrate in numeric specs, not enumerations** —
  *"canonical is wrong on numbers"* is what the evidence supports; *"canonical is wrong"* overstates it.
- 🔴 **A new failure direction: typed field and prose contradict each other *inside one record*, and
  the prose is the correct one.** `mouton-rothschild-1855` stores `aging: 24 months` while its own
  `obp_note` says ~20 months, which matches the château's *"about twenty months"*. **This inverts
  Batch 10's finding**, and means a "trust the typed field, drop the prose" migration would make
  this record actively worse. Unnumbered.
- 🔴 **Verbatim string duplication reappears in typed fields, twice.** `grapes` `CS45/M37/CF18` is
  **byte-identical** on `haut-brion-1855` and `haut-brion-1993` — official 1993 is
  **`Merlot 53 / CS 29 / CF 18`**, so the principal variety is inverted and every value is wrong;
  `aging "24 months (new oak 100%)"` is byte-identical across all three Haut-Brion records against an
  official *"dix-huit à vingt mois"* and an adaptive new-oak share measured at 62–90%. Yquem's
  `terroir` (103 ha vs the producer's 113/104/100) and `serving_temp` are duplicated across all nine
  of its records. **Same shape as Roederer's `house_style` and Allemand's `description`.**
- 🔴 **Statutory impossibilities found in three canonical records.**
  (a) `yquem-ygrec-2017.classification = "Sauternes — Dry White"` — the AOC Sauternes CDC requires
  **≥45 g/L fermentable sugar** and the château's own Y sheet says **7 g/L**; a dry wine cannot be
  AOC Sauternes. The same record's `obp_note` (JA, correctly dry) and `obp_note_en` (109 g/L, sweet)
  **describe two different wines.**
  (b) `haut-brion-1855.classification = "1855 **Médoc** Classification"` — falsified on three layers
  (INAO consolidated CDC, arrêté 10 déc 2024, says *« Premier Grand Cru » du classement des vins de
  Bordeaux de 1855*; the château says *la Classification des Vins de la Gironde*; four real labels
  print only `Premier Grand Cru Classé en 1855`). **The record contradicts itself** — its own
  `description` says "the only non-Médoc château". **`Cru Classé de Graves` is absent from all three
  records** though the château calls it a "double distinction".
  (c) The two WHITE Cos d'Estournel rows print **`Saint-Estèphe`**, which 🏛 the INAO CDC reserves
  *« aux vins tranquilles rouges »* (décret 14 Nov 1936, six black varieties, no white).
- 🔴 **The single most consequential floor fact of the batch: not one of the 47 rows can be resolved
  to a specific wine from menu data, and this is provable rather than merely unattempted.** Every
  château in the block bottles a second (and often third) wine in the **same appellation** — and a
  corpus-wide regex sweep for **every** such name (`Pavillon`, `Forts de`, `Petit Mouton`, `Aile d`,
  `Clarence`, `Clarté`, `Bahans`, `Alter Ego`, `Sirène`, `Pagodes`, `Goulée`, `Labory`, `Ygrec`,
  `Carruades`) returns **zero hits across all 704 rows at both the intake and store layers.**
  **Elimination-by-absence therefore fails for every producer in the block.** Two estates make it
  acute: **Latour's third wine is `Le Pauillac de Château Latour` — the cuvée name *is* the
  appellation**, and the château states it was designed *« pour le proposer en priorité à la
  restauration »*; **Margaux's third wine is `Margaux du Château Margaux`.** 🔴 **This is a four-way
  collision — producer / cuvée / AOC / commune — strictly worse than Batch 9's Clos de Tart shape,
  where the same string was *redundant* (one referent); here it is *ambiguous* (three referents).**
  → **39 of the 47 rows carry a physical-label task for this reason alone.**
  ✅ **Three producers were nonetheless resolved on producer evidence**: all six Haut-Brion rows are
  the grand vin rouge, all six d'Yquem rows are the grand vin (none is Ygrec, none a non-declared
  year), and all five Palmer rows are the grand vin — each confirmed against the château's own
  per-vintage fiches.
- ✅ **Two producer-published discriminators were found that make the label task cheaper.**
  **Giscours: the grand vin contains zero Cabernet Franc in all six vintages; `La Sirène` contains
  CF in all six** — a back-label reading settles it. **Latour and Palmer both run producer-operated
  bottle authentication** (Latour Prooftag from vintage 2007, Palmer QR from 2009), so 2009–2017
  bottles are resolvable through the producer's own tool; only 1996 and 2000 need visual inspection.
  Margaux adds a third: **the 2015 grand vin carries a screen print applied directly to the glass in
  place of paper labels**, so that row is identifiable on sight.
- 🔴 **`D-2026-08-05-08` fired in every producer, and Haut-Brion qualifies the disambiguation rule
  the project relies on.** 🔴 **SIREN is not granular enough**: `Château Haut-Brion`,
  `Château La Mission Haut-Brion` and `La Tour Haut-Brion` are **three SIRETs of one SIREN**
  (`572179026`), while Quintus (389905811) and Les Carmes (341826170) *do* separate cleanly.
  **Identity keys need SIRET granularity.** Measured false-positive rates on naive substring
  matching: Margaux **53 hits, precision 1/53** (including Château Lagrange in Saint-Julien, not even
  in the appellation); Cos **10 hits for 2 real records (80% false)**, one of them a Burgundy record
  hit via a winemaker's CV line; Giscours **7 of 8 false (87.5%)**, with a new variant — **the
  producer name is also a street name** (`ROUTE DE GISCOURS`), which pollutes the company register
  itself. 🔴 **And canonical's id scheme carries the defect too**: `latour-blagny-2019`,
  `latour-vignes-franches-2022` and `latour-epenots-2022` are **Louis Latour**, a different producer
  with its own dossier, sharing the `latour-` prefix with Château Latour.
- 🔴 **A domain trap of a kind not previously recorded, and it is the most dangerous one yet.**
  `mouton-rothschild.com` — the most obvious-looking domain — **redirects to
  `chateau-darmailhac.com`, a sibling château owned by the same group.** Not parking, not a fan page,
  not a look-alike: **the genuine owner serves a different estate's content from the obvious
  address.** Trusting it would have written Château d'Armailhac's material into this dossier under a
  clean authenticity check. Zero words used. **It must never enter a canonical `url` field.**
  Also rejected: `chateau-latour.fr` (invalid TLS, 139-byte nginx 404 — *more* obvious-looking than
  the real domain), and 🔴 `chateau-giscours.fr`, whose AFNIC holder is
  **`SOC D'EXPLOITATION DU CHATEAU GISCOURS` — the estate itself** — serving nothing with **0 Wayback
  captures. Third-party sites still cite it as official; they are wrong.** That is the Batch 11
  "domain owned but never published" shape (Alvina Pernot), now recurring.
  ✅ **Overall the block was clean: 7 of 8 producers adopted a domain that passed §2a on first
  inspection**, and `gcc-1855.fr` was independently authenticity-verified by four agents
  (SIRET `48484166300012`).
- ⚠️ **`Cru Classé` is not one string, and no single form is "correct".** Mouton: 🏛 the 1855 rank is
  **not in the AOC Pauillac cahier des charges at all** (its étiquetage clause reads *"Pas de
  disposition particulière"*); the legal basis is **Décret du 19 août 1921, art. 13 3° b)**, which
  permits **both** `cru classé` and `grand cru classé`. 🔴 **And the front label prints no
  classification whatsoever** — verified on 1996, 2001 and 2019 labels spanning the whole OBP range,
  which closes off "older vintages carried it". The château itself uses two forms (EN
  `Premier Cru Classé`, FR `Premier grand cru classé`). Proposed as **`P-9`** — a three-way naming
  split between the classifying body, the producer and canonical.
- ✅ **Mouton's 1973 promotion and the 1855 ranks are attested from a statutory instrument, not
  folklore** — the INAO CDC text itself reads *« dont les premiers Lafite-Rothschild, Latour en 1855
  et Mouton-Rothschild en 1973 »*. ⚠️ The **Journal officiel** original of the 1973 decree could not
  be retrieved: **Légifrance is Cloudflare bot-gated (HTTP 403)**. Recorded as **gated, not evidence
  of absence**; no bypass attempted. Same for `crus-classes.com` (DNS-dead) and
  `inao.gouv.fr/produit/saint-estephe-16807` (403 WAF).
- 🔴 **The §2c INAO filename trap fired again and produced a new failure mode: a struck-through
  *list item*, not a number.** Palmer established that the **in-force** consolidated CDC (homologué
  **31 March 2023**, JORF 5 April 2023) lists **four** communes for AOC Margaux —
  `Arsac, Labarde, Margaux-Cantenac et Soussans` — and that **the five-commune reading is a PNO
  strikethrough extraction artifact**, because the deleted `Cantenac` survives text extraction.
  🏛 `geo.api.gouv.fr/communes/33268` confirms `Margaux-Cantenac` with `anciensCodes: ["33091"]`:
  **the commune of Cantenac no longer exists.** ⚠️ **So the trap is not confined to merged numeric
  pairs (`40 50 hl`, `115160 hectares`) — it corrupts enumerations too**, and Giscours had already
  recorded two mutually inconsistent five-commune readings from a 2009 décret and a 2022 PNO before
  the in-force text settled it. Also confirmed: `3-CDC-Margaux.pdf` and `PNOCDCMargaux.pdf` are
  **both** PNO drafts; all three Latour CDC guesses returned **HTTP 200 with 8,354 bytes of HTML**.
- ⚠️ **Producers contradict themselves, and both readings were kept every time.** 🔴 The sharpest:
  **Haut-Brion's own HTML and its own downloadable fiche technique disagree on the 2018 and 2019
  blends — the two Cabernets' figures are swapped** (2018: CF 11.9 / CS 38.7 vs CS 11.9 / CF 38.7).
  FR and EN agree *within* each medium, so **the split is by medium, not language**; verified against
  PDF word coordinates, so it is not an extraction artefact, and both readings sum to 100.0%.
  Also: Mouton's **84 ha vs 90 ha on the same page**, three harvest-date mismatches, and its own
  artist list containing **four non-artist years** (1953, 1977, 2000, 2003) against its "a different
  artist every year since 1945" claim; Cos's two canonical records contradicting **each other** on
  hectares, blend and new oak.
- ⚠️ **"Practised vs certified" and the temporal trap decided Farming for all eight, and the trap
  fired hardest yet.** **Palmer** is the extreme case: it holds **three** registrations
  (🏛 Agence Bio/Ecocert `numeroBio 157054`, `datePremierEngagement 2011-09-08`; 🏛 Demeter France;
  🏛 Biodyvin) and its own timeline runs 2009 trial → *« intégralement converti à la biodynamie à
  partir du millésime 2014 »* — 🔴 **yet not one of its five OBP bottles can carry any of the three
  labels** (1996 predates the first trial by 13 years; 2012/2013 sit inside the partial conversion).
  **Mouton**: the group SA *is* registered (`numeroBio 1816`, engagement 2019-09-04) but **Le Pouyalet
  is not among its four registered `lieux d'activité`**, and exact-SIRET queries on both the vineyard
  establishment and the label's proprietor GFA return **`nbTotal: 0` — proved negatives**; the
  château's own site returns **zero hits for all 13 certification terms**. **Haut-Brion**: exact-SIRET
  `nbTotal: 0` on **all seven SIRETs**; the group's organic registration belongs to a **different
  legal person** (`CLARENCE DILLON WINES`, SIREN 480805639, engagement 2023-03-10) whose only organic
  wine is Klara, Sud de la France. **Giscours**: `est_bio: true` sits on a **different legal person
  with the wrong scope at the same address** — recorded as an unnumbered shape.
  🔴 **In every one of these cases both "organic" and "not organic" are on the must-not-say list.**
- 🔴 **`awaiting material from the team` gained a seventh shape — and it is the opposite of the other
  six.** Château Margaux publishes a **live, deep, actively-maintained site** (358 URLs, a page per
  vintage back to 1900) that contains **no technical winemaking content at all**. Not a dead domain,
  not a frozen site, not archive-recoverable in the Giraud sense: **a rich site with one deliberately
  empty section.** d'Yquem shows the Batch 11 "publishing stopped, site still live" shape instead —
  the current `yquem.fr` is a **6-URL brochure whose `sitemap.xml` emits `http://localhost/` for every
  `<loc>`** — and **archive recovery worked**, yielding vintage pages 1893–2014.
- 🔴 **Counter-examples to "the menu is the defective side" reached ten in one batch, the largest
  count yet.** d'Yquem: **four vintages absent from canonical but proven to exist from the château's
  own fiches** — the menu is right, canonical is missing them. Haut-Brion: the front label was
  **redesigned at the 2004 vintage** and no longer prints the appellation, so four of six OBP bottles
  carry **no `Pessac-Léognan` on the front** while the menu prints it correctly — **the menu is right
  and the label moved it.** Giscours: the single word `Margaux` **correctly excludes** the estate's
  Haut-Médoc third wine — **the column works**; what it cannot do is separate grand vin from second.
  Latour: 🔴 **neither side is defective** — an appellation-only Bordeaux list is a standard
  restaurant convention, not damage, which is a **third direction** beyond the two worked examples
  Batches 10–11 established.
- 🔴 **Canonical claims refuted outright by the producer, worth listing because they are
  floor-facing.** `giscours-1855` states the owner "also owns Château du Tertre" — **refuted by both
  the producer (AJ Domaines = Giscours + Caiarossa only) and the register** (du Tertre's operating
  company SIREN 894341353, associés Les Grands Chais de France / Terres Bordelaises) — **and the
  false claim is duplicated across four fields**. It also says "Eric owns since 1995" (he died 2018)
  and calls the estate a "pioneer of rosé" against the producer's own "2019, newest in the range".
  `palmer-1855` calls **Alter Ego a "second wine"** — the château's terms are
  *« L'autre grand vin »* / *"THE OTHER WINE"*, and `second vin` / `second wine` / `deuxième vin`
  return **0 hits across 67 FR + 2 EN pages**; it presents `CS 47 / Merlot 47 / PV 6` as the estate's
  permanent encépagement when that string is **verbatim the official 2016 vintage assemblage** and
  the château publishes no planting percentages at all (**a value with a time axis stored in a field
  that has none** — unnumbered); and it garbles the Historical wine (`Blend`→**`Wine`**,
  **15%**→**10% syrah**, and an unsourced "Vin de France"). `latour-1855`'s `lutte raisonnée` is
  **stale by a decade** and understates biodynamics **~4.7×**, and it **inverts** the official
  *"the oldest document dates from 1331"* into "records go back to *before* 1331".
- ⚠️ **Two producer-side facts that will be asked about and have no official source.** Giscours:
  a widely-repeated mid-2000s regulatory episode — 🏛 **Légifrance juri search returns 15 decisions,
  all unrelated** (succession / GFA / lease; one candidate checked and confirmed to concern a
  different Bommes estate). **Recorded as a third-party claim with no official source, placed on the
  must-not-say list with a scripted floor response.** Mouton: the **1993 Balthus label** — the
  château's own account is the **opposite of the folklore** (the BATF *had approved* it; the Baroness
  withdrew the US bottles herself and asked for the approval to be rescinded). **"Banned in America"
  contradicts the producer.**
- **Physical-label tasks added: 39**, bringing the floor total to **78**. See `NEXT_ACTIONS.md` §3h.

**Batch 13 notes (partial — 2 of 6).** Krug ~86% and Ridge Vineyards ~85%, both High, **+6 bottles**.
Stopped by a **monthly spend limit, not by a finding**. The four unwritten producers were completed
in Batch 14. The full findings — the inverse-of-`CDX-1` shape at Krug, the **Krug iD** as a physical
surrogate key for `V-1`/`CDX-8`, and Ridge's worked confirmation of `3f-10` — are recorded in
`NEXT_ACTIONS.md` §0b and in the two dossiers.

**Batch 14 notes (complete — 6 of 6).**
- **All six cleared the bar** — Chappellet ~85% (High), Turley ~80% (High), Dominus Estate ~80%
  (Medium-High), Promontory ~80% (Medium-High), Dom Pérignon ~78% (Medium-High), Château-Figeac ~75%
  (Medium-High). **+18 bottles.** Run at **3 concurrent agents**, the cap set by `D-2026-08-06-06`.
  The last free slot was **deliberately left empty** rather than extended a third time.
- ✅🔴 **The Batch 9 resume precedent held a third time, and it is now a measured pattern rather than
  a prediction.** Dom Pérignon (**28 MB / 449 files**) and Turley (**2.4 MB / 14 files**) were
  written from their existing caches with **no research sweep**, caches left byte-intact. Turley is
  the sharper demonstration: `page_trade-assets.html`, **already on disk**, held the URLs of the
  official tech-sheet PDFs for the **exact 2023 vintages printed on the menu**. **A spend-limit stop
  costs the writing pass, not the research.**
- 🔴🔴 **The dominant finding: `label = null` handling produces two opposite failures, and this batch
  caught the second.** Batch 12 measured the matcher **over-proposing** on `label = null` rows (152
  rows given a cuvée anyway, 147 marked `exact`, always the grand vin). **Promontory is the
  inverse** — canonical's record has `producer == name == "Promontory"` (the `CDX-18` collision), so
  producer agreement alone collapses the candidate set to **exactly one correct record**, and the
  matcher still returned `cuvee: null` / `unresolved` / `confidence 0.0` on all three rows.
  **Dom Pérignon is a third face**: `_parts` correctly yields `label: null` / `style: "brut"`, yet
  `normalized_cuvee` becomes `"Brut"` and the matcher searches canonical cuvées for a **style
  token**. 🔴 **One defect, three faces — and none of them is fixable by repairing canonical.**
- 🔴 **The inverse-of-`CDX-1` shape is confirmed a second time and is worse than at Krug.**
  Dom Pérignon's intake evidence claims *"canonical キュヴェ **2 件**"*; canonical holds **15**,
  including `dom-perignon-2015`, `dom-perignon-2013` and `dom-perignon-p2-2003` — **the
  exactly-right target for all three rows**, each sitting at `confidence 0.0`. ⚠️ **This is not a
  gap, and treating it as one would create duplicates.** ✅ **Counter-case in the same batch:**
  Dominus' *"1 件"* claim was verified **true**. The evidence string is not uniformly wrong; it must
  be checked per producer.
- ✅🔴 **`3f-10` now has four independent confirmations, each by a different route, and one of them
  inverts the rule's own example.** Turley: `'Estate,'` sits in the same quoted vineyard-name slot as
  `"HAYNE VINEYARD"` and the label prints `TURLEY ESTATE` — **not** a category word. Chappellet:
  `Signature` **is** the official product name (made permanent in **1984**), but **the word is not
  printed on the front label** — what is printed is Donn Chappellet's **gold autograph**, so the menu
  is right and *"it says Signature on the label"* is false. Dominus: `Proprietary Blend` **is** a
  `CDX-15` instance, but for the **opposite reason** from Ridge — at **95 / 95 / 87%** Cabernet a
  varietal designation **would** have been lawful under 🏛 **27 CFR §4.23(b)** and the estate simply
  **declines to name the grape**, whereas Ridge Geyserville (71/19/8/2) legally **could not**.
  🔴 **Pattern existence remains no evidence. Test every row on its own label.**
- 🔴 **Three row-groups were deliberately left unresolved, and that is the correct output.**
  **Dominus** — the estate publishes that Napanook produces three wines, and the official bottle
  shots show **Dominus and Napanook both printing `napa valley red wine` *and* `estate bottled`**,
  same vineyard, same appellation, same harvest dates. **Figeac** — `Petit-Figeac` (2018) and
  `La Grange Neuve de Figeac` (2009) sit in the same AOC. **Promontory** — `CDX-15` left undecided
  because the front label has not been read. ⚠️ **In every case circumstantial evidence pointed at
  the grand vin and was refused as circumstantial.** This is the Batch 12 defect being avoided by
  hand, which is exactly why the fix belongs in the matcher.
- ✅ **Batch 12's second-wine measurement replicated exactly.** `Petit-Figeac`, `Petit Figeac` and
  `Grange Neuve` return **0 hits across all 704 rows at both layers**, as all 13 Bordeaux second-wine
  names did. And `_parts.label` is `null` on **60 of 60** rows in `FRANCE | RED > BORDEAUX` —
  **section-wide structure, not row defects.** The parser also writes `_parts.rank: "Grand Cru"` by
  slicing those words out of the **appellation name** `Saint-Émilion Grand Cru`.
- 🔴 **Statutory questions were settled by enumerating the statute rather than asserting it.**
  `Pritchard Hill` is **not an AVA** — the string `Pritchard` appears **0 times** across all **288
  sections of 27 CFR Part 9**, enumerated mechanically from the eCFR title-27 structure API; it is
  simultaneously a place name and the cuvée-position designation, and the appellation of origin
  printed is `NAPA VALLEY`. Figeac's 2022 promotion to `Premier Grand Cru Classé "A"` **cannot be
  backdated to any OBP bottle**: *arrêté du 15 décembre 2022* art. 2 applies *«à compter de la
  récolte 2022»*, and **four different official wordings** of the rank were recorded (Légifrance /
  INAO / ODG / the estate) — `CDX-25` holding.
  ⚠️ **The orchestrator's brief supplied two wrong CFR citations and the agent caught both against
  eCFR** — St. Helena is **§9.149** and Howell Mountain **§9.94**, not §9.150 / §9.36.
  **Verify citations; do not inherit them from a brief.**
- 🔴 **A canonical vocabulary gap larger than a missing producer.** `Zinfandel` appears in **zero
  `grapes` arrays across all 928 records.** Promoting Turley means adding a **grape category**, not
  a producer — the same shape as `CDX-17`'s missing Oregon. Turley, Chappellet and Figeac are all
  **gaps, not conflicts** (`CDX-23`); Figeac's 6 substring hits are all `producer='Bordeaux'`
  vintage-guide records, i.e. the ~130 **non-bottle** class Batch 12 measured.
- 🔴 **Producer-published data is not automatically reliable, and two producers failed differently.**
  **Chappellet's own product pages carry wrong-vintage prose** — the 2022 Signature page's growing
  season describes **2020**, the 2022 Pritchard Hill page describes **2019** and quotes a 2019
  review. **Any pipeline scraping product pages instead of the wine-notes PDFs ingests wrong-vintage
  facts as truth.** **Dominus' own tech sheets duplicate figures across different wines**
  (`DOM_2020` and `NK_2020` both 1,600 cases; `NK_2021` and `Othello-2021` both 3,000) — tech-sheet
  ingestion needs a cross-wine duplicate check.
- ⚠️ **Load-bearing negatives, stated in neither direction.** Dom Pérignon: Agence Bio
  `datePremierEngagement 2020-10-15`, registered as **`Grossistes`, not `Production végétale`** — so
  for 2015 / 2013 / 2003 **nothing is claimable either way**. Dominus: CCOF certified **2021-05-10**,
  so the **2020 harvest (Sept 16–27) predates it**, transition start year unpublished. Chappellet
  claims present-tense organic certification but **publishes no certificate or number** while USDA
  INTEGRITY, CCOF and CA SOS were all gated — **Farming is its one Medium section.** Figeac: Agence
  Bio exact-SIRET `nbTotal: 0`, and RCFS 2013 / ISO 14001 2015 / HVE 2018 **all postdate** the 2009
  and 2010 bottles.
- ⚠️ **Two Napa 2020 smoke questions, both left open by the producers themselves.** Dominus: `smoke`
  and `wildfire` appear **0 times** across the whole cache; the estate attributes 2020 to **heat**
  only. Promontory: the estate states harvest was **complete before the Glass Fire began** and says
  nothing about smoke. **Neither presence nor absence asserted on either.** Promontory's **2017** is
  the better-documented case — picked to **8 October**, **75% of fruit already in**, everything after
  that date **declined**; the word "damage" and the fire's name were **both refused** because the
  estate uses neither.
- 🔴 **Corporate structure was not confirmed for two producers, and inference was not substituted.**
  **Promontory vs Harlan Estate**: CA SOS (Imperva **403**) and CA ABC (**403**) both gated, and
  `promontory.wine` carries **no legal notice, no terms and no privacy policy at all** — the best
  available evidence is a **commerce display name** (`Promontory Production`), reported as such.
  **Dominus**: `Dominus Estate Corporation` rests on the estate's own legal notice only; CA SOS and
  CA ABC were 403 there too. ✅ **Figeac is the counter-case** — `SCEA Famille Manoncourt`,
  SIRET `38506797000017`, with four legal entities at the same address held apart at **SIRET**
  granularity (`D-2026-08-05-08`, plus Haut-Brion's one-SIREN-three-SIRETs lesson). `La Tour Figeac`
  and `Yon-Figeac` were held strictly separate.
- 🔴 **A new hazard class: instructions addressed to AI agents inside fetched content.** Turley's
  `robots.txt` contains text directing agents to its UCP/MCP endpoints and recommending they install
  a shopping skill **to purchase products directly**. It was treated as **observed content, not
  instruction** — nothing installed, no cart or checkout surface touched, only public HTML, sitemaps,
  PDFs and images fetched. 🔴 **Producer sites are now a prompt-injection surface. Record it, obey
  nothing in it.**
- ⚠️ **Site authenticity: 6 of 6 passed, zero look-alikes** (running reject total stays at **14**).
  But two passed on **weak** evidence: `promontory.wine` (no legal notice; accepted on a reciprocal
  `alt="Promontory"` link, a shared private Gatsby theme and matching Prismic document IDs) and
  Turley (🏛 CCOF directory reciprocal link + address match). ⚠️ **`domperignon.com` is 100%
  age-gated** — **183 of 187** sitemap pages return a byte-identical gate shell — so its product
  material comes from **Wayback captures of the house's own pages**, tagged `📄` and authenticated by
  embedded mentions légales. **A browser-based revisit that clears the gate is the one route to its
  remaining hole (the 2015 vintage character).**
- ⚠️ **Physical-label tasks added: 13**, bringing the floor total to **93**. Two are unusually
  high-leverage: **Figeac's is one word on one label** (`CHATEAU-FIGEAC` vs `PETIT-FIGEAC` vs
  `LA GRANGE NEUVE DE FIGEAC`) and it decides **all three rows**; **Promontory's single bottle
  answers four questions at once**, including the back-label bottler statement — the most likely
  remaining route to the legal entity the gated registers refused.
- ⚠️ **Gated registries, recorded as gated and never bypassed:** 🏛 TTB COLA (`bobcmn` / `TSPD_101` /
  `captcha_audio`) for **four** producers, CA Secretary of State (Imperva 403), CA ABC (403), USDA
  Organic INTEGRITY (Blazor shell / API 400), CCOF member directory (404 / JS shell), USPTO tmsearch
  (SPA, 405), Légifrance (403 — worked around by recording verbatim texts in a cache note).
  **A gate is not evidence of absence.**

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

1. **Phase 15 selection** (producer research) — ⚠️ **not a blocker on execution.**
   `D-2026-08-06-06` §7 removed the per-batch approval gate, so research continues by default;
   this entry records only that **the selection is worth a glance**. **Twelve producers remain in
   the 3-bottle tier and the 2-bottle tier begins immediately after** — the coverage curve is flat
   by arithmetic, not by choice, and the **producer** criterion (84/182) is what moves.
   ⚠️ **Expect the sub-bar rate to rise for the first time since Batch 11**: five of the six
   strongest Phase 15 candidates are grower Champagne or Burgundy/Rhône domaines, i.e. the
   **Roulot / Niellon publishing profile**, and **no cache exists for any of the twelve**.
   See `NEXT_ACTIONS.md` §0 "Recommended Phase 15".
   🔴 **Batches 12 and 14 together materially raised the value of Shape C.** The `label = null`
   defect is now measured **in both directions** — over-proposing (Batch 12: 152 rows, 147 marked
   `exact`, always the grand vin) and **under-proposing** (Batch 14: Promontory, where the single
   correct record was the only candidate and still went `unresolved` at `0.0`). Together with the
   reference-table contamination (~130 of 928 records), these are **measurement-first, cheap and
   floor-facing** — see `NEXT_ACTIONS.md` §0 and §1
2. Review / merge of PR #5
3. **Conflict-register adjudication, now spanning Batches 8, 9 and 10** — accept or reject proposed
   `C-6` and `P-8`; adjudicate the **`CAT-1`…`CAT-9` category proposals in §D**, which are still
   only proposals (Batch 9 cited `CAT-3 brand_axis` for Hundred Acre precisely because no *accepted*
   class fits); and decide whether these unnumbered shapes get numbers — the geographic *climat +
   sub-parcel* gap (Niellon), a non-year sentinel `vintage = '—'` (Roulot), classification drift
   within one cuvée (Bachelet-Monnot), the producer/cuvée same-string collision (Clos de Tart), and
   **attribute-provenance** (Hundred Acre `Ark`: a canonical `subregion` with no primary source).
   🔴 **Batch 10 adds five more unnumbered shapes** — attribute *values* (not just prose)
   contradicting producer-official sources; no way to express a **superseded cuvée name during a
   rename** (Billecart); the **brand axis inside the cuvée string** (`Récolte du Domaine`); the
   matcher **over-splitting a product name that legitimately contains its appellation**
   (`Napa Valley Chardonnay` — the inverse of `C-4`); and a **cross-producer collective
   designation embedded in a name** (`Special Club`). It also **corrects `P-2`'s recorded impact
   from 3 bottles to 1** and supplies the official entity confirmation `P-2` asked for
4. 🔴 **Canonical's stored values contradict producer-official sources — 21 of 22 producers
   examined.** 🔴 **Batch 12 adds eight and reframes the item: alongside wrong values, canonical is
   carrying ~130 of 928 records (~14%) that are not bottles at all** — 61 encoding the 1855
   classification table (breaking down 5/14/14/10/18, the exact official structure), 37 whose
   provenance is a **third-party critic's reference book** and which are **schema-indistinguishable
   from sellable bottles**, and 35 holding a region or appellation in the `producer` field.
   **They are not inert**: `haut-brion-1855` is `vintage: "—"`, resolves to `vintage: {}`, and is the
   `_stub` supplying cuvée facts — so its wrong values **default onto the four vintages with no
   record of their own**. ⚠️ **Mouton supplies the first real counter-example and it should temper
   the wording**: its 51-entry artist archive matches officially **51/51**, and geography passes —
   **failures concentrate in numeric specs, not enumerations.** No longer confined to `obp_note` prose: Batch 10 found the same failure in **typed
   fields** (`grapes`, `dosage`, `aging`, `founded_year`), including **19 contradicted items across
   Billecart-Salmon's four records** and **one false `house_style` string duplicated verbatim across
   all 16 Roederer records**. 🔴 **Batch 11 separates three failure modes that had been collapsed
   into one — *contradicted*, *unsourced*, and *absent as key* — and finds all three inside a single
   producer** (Thierry Allemand, which also reproduces the Roederer duplication shape: one
   Chaillot-subject `description` byte-identical across five records including both Reynard ones).
   ⚠️ **Alvina Pernot is the one exception and it sharpens the item rather than softening it: all
   four of her records are bare shells** — 8 fields absent *as keys* — **while every row reads
   `match_state = exact` at `confidence 1.0`.** **The scope is still unmeasured, and measurement is
   cheap** — this is the highest-severity open item, because the text is what floor staff read
5. **Canonical `region` vocabulary has no Oregon** — all 79 USA records are `California`. Blocks
   Bergström promotion and every future Pacific-Northwest producer
6. Hero artwork confirmation (ARIADNE)
7. Schema-change permission (aroma intensity / complexity / 11-family taxonomy — all need migrations)
8. Fruit Basket: ship or not
9. `Les Hautes Mottes 2018` — physical bottle or importer sheet needed
10. **Physical-label checks now blocking seventy-eight rows** — 🔴 **Batch 12 adds thirty-nine, and
    they are structurally different from the previous thirty-nine.** The earlier tasks each settle a
    *spelling, an appellation or an identity detail*. **All 47 Bordeaux rows share one question —
    grand vin, second wine, or third? — and 39 of them cannot be answered from any online source**,
    because the distinguishing string was never printed on the menu and appears nowhere in the
    corpus (0 hits / 704 rows, both layers, for all 13 second-wine names). ⚠️ **These are the most
    expensive rows on the list** ($280–$6,890; Margaux alone is eight bottles between $2,440 and
    $6,890). ✅ **Three producer-published shortcuts cut the cost sharply**: Giscours is settled by
    a back label (**zero Cabernet Franc in the grand vin across all six vintages; CF in every
    `La Sirène`**); **Latour (Prooftag, vintages 2007+) and Palmer (QR, 2009+) both run
    producer-operated bottle authentication**, so 2009–2017 resolve through the producer's own tool
    and only 1996/2000 need visual inspection; and **Margaux 2015 is identifiable on sight** (screen
    print applied directly to the glass, no paper label). The remaining eight are ordinary reads:
    d'Yquem 375 mL capacity marking and the Ygrec appellation line, Haut-Brion's 1987 label
    (decides whether it is the last Graves-form or first Pessac-Léognan-form bottle), Cos
    d'Estournel's two WHITE-row appellation lines, Palmer's Historical XIXth Century Wine
    designation and white-wine name, and Mouton's classification wording.
    ⚠️ **Several settle multiple escalations per photo.** The original thirty-nine follow —
    **Batch 11 added twenty-one**: Vilmart
    ×2 (row 4 `Les Blanches Voies` — cuvée-name stacking, missing millésime, the never-published
    `Extra Brut`, RM/NM code; and whether `Coeur de Cuvée 2016` exists at all, since OBP holds it
    in stock at $440 while no official 2016 fiche could be found), Henri Giraud ×4 (rows 2 and 4
    identity; 🔴 **whether row 4's "2022" is a `MILLÉSIME` or an MV-style base year — this single
    check decides `V-1` vs an ordinary vintage**; whether the Esprit Nature back label says
    `Brut Nature`; whether Argonne carries `2016` and a bottle number), Alvina Pernot ×5 (which
    name row 2's label bears, `La Pièce sous le Bois` vs `Blagny`; official existence of the 2023
    `Les Vignes de Mon Père`; which of the four `Les Folatières` lieudits; the `(en partie)`
    portion of PSB; and 🔴 **the `mis en bouteille` wording — the only thing that can resolve the
    `46.90Z` domaine-vs-négoce question**), Sigaut ×4 (lieu-dit / `Vieilles Vignes` on row 1's
    label; producer form on rows 2–4; `mis en bouteille` + importer; ABV on all four, absent from
    every official source), Dauvissat ×1 consolidated (settles the `La Forest` alias target,
    whether row 1's village Chablis carries a cuvée name, and the canonical producer name),
    Thierry Allemand ×5 (🔴 **the sulfites declaration — the single most-asked question about these
    $1,600–$2,600 bottles, and unanswerable from any public source**; the name spelling across
    three conflicting renderings; the cuvée-name label form; ABV against the 13.5% cap; and whether
    any vintage-less Chaillot physically exists, which bears directly on `allemand-chaillot-nv`).
    The original eight (`Clos de la
    Maltroie` (Niellon, unsupported by any source), `Clos de` vs `Clos des Bouchères` (Roulot),
    `La` vs `Clos de la Coulée de Serrant`, Taittinger row 5 Rosé-vs-BdB 2012, Armand Heitz
    Chevalier `?` vintage, Hundred Acre `'Ark'` 2022 appellation, Abreu label brand/type
    designation, Bergström row 5's cuvée name) **plus ten from Batch 10**: Moussé ×3 (does the
    bottle bear `Spécial Club`; the mandatory RM/NM/RC matriculation code, absent from the site;
    three unconfirmed vintages), Roederer ×1 (the ROSÉ-section 2014 — both `Cristal 2014` and
    `Cristal Rosé 2014` exist officially), Billecart ×1 (row 3: `Brut Rosé` or `Le Rosé`, `Brut` or
    `Extra Brut`), Laurent-Perrier ×1 (`Itération Nº27/Nº26` or `Grande Cuvée No. 27/26` — the only
    evidence separating a menu typo from a market-specific label), Montelena ×1 (back label:
    `ESTATE BOTTLED` per 27 CFR §4.26 — the front label does not carry it), Olivier Leflaive ×3
    (which of two Bâtard-Montrachet 2023; Meursault 2023 bare vs 5 lieu-dits; whether
    `Récolte du Domaine` appears on the bottle at all). All are floor tasks, not research tasks.
    ⚠️ **Several settle multiple escalations per photo**

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
- **Verify only the scope that changed.** Producer-research verification is limited to dossier
  structure, required sections, and the untouched-ness of canonical and `REGISTER.md`. Repository-
  wide git inspection, integrity sweeps, canonical-wide scans and repeated mtime checks are **not**
  run unless the task explicitly modifies those areas. See `D-2026-08-05-13` and
  [`../ai-autonomous-execution-policy.md`](../ai-autonomous-execution-policy.md).

## Last Updated

2026-08-06 (updated after **Batch 14** — complete, 6 of 6; closed Batch 13's remainder and added
two producers on restaurant value, `D-2026-08-06-07`. Coverage **539 / 704 = 76.6%** across
**84 dossiers**; producer criterion **84 / 182 = 46.2%**. Figures recomputed with
`research/producers/coverage.py`, not carried over from memory)
