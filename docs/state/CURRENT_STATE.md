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

**Status: Batch 10 complete — 6 of 6.** Famille Moussé, Louis Roederer, Billecart-Salmon,
Laurent-Perrier, Chateau Montelena, Olivier Leflaive Frères. **All six cleared the 70% bar**, all
six at Confidence High. Run at a maximum of **2 concurrent agents** throughout. See §"Batch 10
notes" below.

| | |
|---|---|
| Dossiers | **62** — `research/producers/*.md` |
| OBP coverage | **444 / 704 bottles (63.1%)** — Batch 5 **+44**, Batch 6 **+36**, Batch 7 **+34**, Batch 8 **+30**, Batch 9 **+30** (15 + 15 on resume), Batch 10 **+25** |
| Remaining | **120 producers / 260 bottles** |
| Conflicts register | `research/canonical_conflicts/REGISTER.md` — 20 true conflicts, 54 false positives separated. **Batches 5–10 wrote no new entries.** Batch 8 proposes `C-6` and `P-8`; Batch 10 added evidence to `C-1`, `C-4`, `V-1`, `V-2`, `V-3`, `S-2` and **corrected the recorded impact of `P-2` downward**, and leaves **five further unnumbered shapes** — all awaiting CTO adjudication, none written |
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
| **Batch 10 (6)** | **Famille Moussé, Louis Roederer, Billecart-Salmon, Laurent-Perrier, Chateau Montelena, Olivier Leflaive Frères** |

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

1. **Batch 11 approval** (producer research) — Batch 10 is complete; nothing auto-advances.
   ⚠️ **The 4-bottle tier is now exhausted of producers that publish anything**: the six that
   remain at 4 bottles (Vilmart & Cie, Thierry Allemand, René & Vincent Dauvissat, Henri Giraud,
   Anne et Hervé Sigaut, Alvina Pernot) carry the Roulot / Niellon risk profile. **Shape C is now
   the better-value shape** — see `NEXT_ACTIONS.md` §1
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
4. 🔴 **Canonical's stored values contradict producer-official sources — 10 of 10 producers
   examined.** No longer confined to `obp_note` prose: Batch 10 found the same failure in **typed
   fields** (`grapes`, `dosage`, `aging`, `founded_year`), including **19 contradicted items across
   Billecart-Salmon's four records** and **one false `house_style` string duplicated verbatim across
   all 16 Roederer records**. **The scope is still unmeasured, and measurement is cheap** — this is
   the highest-severity open item, because the text is what floor staff read
5. **Canonical `region` vocabulary has no Oregon** — all 79 USA records are `California`. Blocks
   Bergström promotion and every future Pacific-Northwest producer
6. Hero artwork confirmation (ARIADNE)
7. Schema-change permission (aroma intensity / complexity / 11-family taxonomy — all need migrations)
8. Fruit Basket: ship or not
9. `Les Hautes Mottes 2018` — physical bottle or importer sheet needed
10. **Physical-label checks now blocking eighteen rows** — the original eight (`Clos de la
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

2026-08-05 (updated after Batch 10, complete — 6 of 6)
