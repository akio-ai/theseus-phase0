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

**Status: Batch 9 complete — 6 of 6.** The three producers stranded by the earlier spend-limit
stop (Hundred Acre, Abreu, Bergström) were resumed from their existing `_sources` caches and
written without re-running research. The prediction held: resuming cost the writing pass only.
See §"Batch 9 notes" below.

| | |
|---|---|
| Dossiers | **56** — `research/producers/*.md` |
| OBP coverage | **419 / 704 bottles (59.5%)** — Batch 5 **+44**, Batch 6 **+36**, Batch 7 **+34**, Batch 8 **+30**, Batch 9 **+30** (15 + 15 on resume) |
| Remaining | **126 producers / 285 bottles** |
| Conflicts register | `research/canonical_conflicts/REGISTER.md` — 20 true conflicts, 54 false positives separated. **Batches 5–8 wrote no new entries.** Batch 8 added evidence to C-1, C-4 and S-2 and **proposes two new IDs (`C-6`, `P-8`) plus three unnumbered shapes — all awaiting CTO adjudication, none written** |
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
| **Batch 9 (6)** | Harlan Estate, Clos de Tart, Armand Heitz, **Hundred Acre, Abreu Vineyards, Bergström Wines** (last three resumed from cache) |

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

1. **Batch 10 approval** (producer research) — Batch 9 is complete; nothing auto-advances
2. Review / merge of PR #5
3. **Conflict-register adjudication, now spanning Batches 8 and 9** — accept or reject proposed
   `C-6` and `P-8`; adjudicate the **`CAT-1`…`CAT-9` category proposals in §D**, which are still
   only proposals (Batch 9 cited `CAT-3 brand_axis` for Hundred Acre precisely because no *accepted*
   class fits); and decide whether these unnumbered shapes get numbers — the geographic *climat +
   sub-parcel* gap (Niellon), a non-year sentinel `vintage = '—'` (Roulot), classification drift
   within one cuvée (Bachelet-Monnot), the producer/cuvée same-string collision (Clos de Tart), and
   **attribute-provenance** (Hundred Acre `Ark`: a canonical `subregion` with no primary source)
4. **Unsourced canonical prose in floor-facing copy** — `obp_note` fields carry critic scores and
   claims contradicted by official sources (Coulée de Serrant, Bachelet-Monnot, Clos de Tart).
   Scope unknown; a sweep is warranted before anyone treats `obp_note` as trustworthy
5. **Canonical `region` vocabulary has no Oregon** — all 79 USA records are `California`. Blocks
   Bergström promotion and every future Pacific-Northwest producer
6. Hero artwork confirmation (ARIADNE)
7. Schema-change permission (aroma intensity / complexity / 11-family taxonomy — all need migrations)
8. Fruit Basket: ship or not
9. `Les Hautes Mottes 2018` — physical bottle or importer sheet needed
10. **Physical-label checks now blocking eight rows** — `Clos de la Maltroie` (Niellon, unsupported
    by any source), `Clos de` vs `Clos des Bouchères` (Roulot), `La` vs `Clos de la Coulée de
    Serrant`, Taittinger row 5 Rosé-vs-BdB 2012, Armand Heitz Chevalier `?` vintage, **Hundred Acre
    `'Ark'` 2022 appellation**, **Abreu label brand/type designation (one photo of a 2019 and a 2021
    front+back settles three escalations at once)**, and **Bergström row 5's cuvée name**. All are
    floor tasks, not research tasks

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

2026-08-05 (updated after Batch 9, complete — 6 of 6)
