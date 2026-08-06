# Next Actions

> **Official state document.** Written 2026-08-05 from verified repository state.
> Ordered by what unblocks the most work, not by effort.
> Companion to [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`DECISIONS.md`](DECISIONS.md).

## Legend

**🔴 Blocked on Akio** — execution cannot proceed without a decision.
**🟡 Ready** — authorized, can start immediately.
**⚪ Deferred** — deliberately not started; do not pick up without instruction.

---

## 0. ✅ Batch 14 is closed — 6 of 6. Batch 13's remainder is done.

**Batch 14 ran the four producers Batch 13 had left, plus two added on restaurant value**
(`D-2026-08-06-07`): **Dom Pérignon, Turley, Dominus Estate, Chappellet, Château-Figeac,
Promontory**. Coverage **521 → 539 / 704 (74.0% → 76.6%)** across **84 dossiers**.
Remaining: **98 producers / 165 bottles**. Binding producer criterion: **84 / 182 (46.2%)**.

**All six cleared the bar** — Chappellet ~85% (High), Turley ~80% (High), Dominus ~80%
(Medium-High), Promontory ~80% (Medium-High), Dom Pérignon ~78% (Medium-High), Figeac ~75%
(Medium-High). **Zero sub-bar dossiers**, the fourth such batch after 4, 10 and 12. Run at
**3 concurrent agents** throughout, per `D-2026-08-06-06` §4.

✅ **The Batch 9 precedent held a third time and is now a measured pattern, not a prediction.**
Dom Pérignon (28 MB / 449 files) and Turley (2.4 MB / 14 files) were written from their existing
caches with **no research sweep**. Turley is the sharper case: `page_trade-assets.html`, already on
disk, held the URLs of the official tech-sheet PDFs for the **exact 2023 vintages on the menu**.
**A spend-limit stop costs the writing pass, not the research.** Four new caches were built
(`dominus-estate` 131 files / 54 MB, `chappellet` 85 / 13 MB, `chateau-figeac` 74, `promontory` 51)
so the same is true next time.

### 🔴 The finding that should shape Phase 15

🔴🔴 **The `label = null` handling produces two opposite failures, and Batch 14 caught the second
one.** Batch 12 measured the matcher **over-proposing** on `label = null` rows — 152 rows given a
cuvée anyway, 147 marked `exact`, always the grand vin. **Promontory is the inverse.** Canonical's
record has `producer == name == "Promontory"` (the `CDX-18` collision), so producer agreement alone
collapses the candidate set to **exactly one correct record** — and the matcher still returned
`cuvee: null` / `unresolved` / `confidence 0.0` on all three rows. **Same input condition, opposite
outcome.** Dom Pérignon is a third variant: `_parts` correctly yields `label: null` / `style: brut`,
yet `normalized_cuvee` becomes `"Brut"` and the matcher then searches canonical cuvées for a
**style token**. 🔴 **These are one defect with three faces, not three defects — and no amount of
canonical repair addresses any of them.**

### Findings banked from Batch 14

1. 🔴 **The inverse-of-`CDX-1` shape is confirmed a second time, and worse than at Krug.**
   Dom Pérignon's intake evidence claims *"canonical キュヴェ **2 件**"*; canonical holds **15**,
   including `dom-perignon-2015`, `dom-perignon-2013` and `dom-perignon-p2-2003` — **the
   exactly-right target for every one of the three rows.** All three sit at `unresolved` /
   `confidence 0.0`. ⚠️ **This is not a gap and the remedy is the opposite one: treating it as a
   gap would create duplicates.** ✅ Counter-case in the same batch — Dominus' *"1 件"* claim was
   verified **true**, so the evidence string is not uniformly wrong and must be checked per producer.
2. ✅🔴 **`3f-10` now has four independent confirmations, and each arrived by a different route.**
   Ridge (`ESTATE` is a real front-label designation the winery defines) → Turley (`'Estate,'` sits
   in the same quoted vineyard-name slot as `"HAYNE VINEYARD"`; the label prints `TURLEY ESTATE`) →
   Chappellet (`Signature` **is** the official product name, made permanent in 1984, but **the word
   is not printed on the label** — what is printed is Donn Chappellet's gold autograph) → Dominus
   (`Proprietary Blend` **is** a `CDX-15` instance, but for the **inverse reason** from Ridge: at
   95/95/87% Cabernet a varietal designation **would** have been lawful under 27 CFR §4.23(b), and
   the estate simply declines to name the grape; Ridge Geyserville at 71/19/8/2 legally could not).
   🔴 **Pattern existence remains no evidence at all. Test every row on its own label.**
3. 🔴 **Three of the six rows-groups were deliberately left unresolved, and that is the correct
   output.** Dominus (Napanook and Dominus **both** print `napa valley red wine` **and**
   `estate bottled`, same vineyard, same appellation, same harvest dates), Figeac (Petit-Figeac
   2018 / La Grange Neuve de Figeac 2009 sit in the same AOC), Promontory (`CDX-15` left undecided
   because the front label has not been read). ⚠️ **In each case circumstantial evidence pointed at
   the grand vin and was refused as circumstantial.** This is the Batch 12 defect being avoided by
   hand — which is precisely why the fix has to move into the matcher.
4. ✅ **Batch 12's second-wine measurement replicated exactly.** `Petit-Figeac`, `Petit Figeac` and
   `Grange Neuve` return **0 hits across all 704 rows at both layers** — as all 13 Bordeaux
   second-wine names did. And `_parts.label` is `null` on **60 of 60** rows in
   `FRANCE | RED > BORDEAUX`: **section-wide structure, not row defects.**
5. 🔴 **Statutory questions were settled by enumerating the statute, not by assertion.**
   `Pritchard Hill` is **not an AVA** — the string `Pritchard` appears **0 times** across all
   **288 sections of 27 CFR Part 9**, enumerated mechanically from the eCFR title-27 structure API.
   Figeac's 2022 promotion to `Premier Grand Cru Classé "A"` **cannot be backdated**: *arrêté du
   15 décembre 2022* art. 2 applies *«à compter de la récolte 2022»*, so **none of the 2018 / 2010 /
   2009 bottles can carry it** — and four different official wordings of the rank were recorded
   (Légifrance / INAO / ODG / the estate), which is `CDX-25` holding.
   ⚠️ **This brief supplied two wrong CFR citations** (St. Helena and Howell Mountain) and the agent
   caught both against eCFR — §9.149 and §9.94, not §9.150 and §9.36. **Verify, do not inherit.**
6. 🔴 **A new canonical vocabulary gap, larger than a missing producer.** `Zinfandel` appears in
   **zero `grapes` arrays across all 928 records.** Promoting Turley means adding a **grape
   category**, not a producer — the same shape as `CDX-17`'s missing Oregon.
7. 🔴 **Producer-published data is not automatically reliable, and two producers proved it
   differently.** Chappellet's own product pages carry **wrong-vintage prose** — the 2022 Signature
   page's growing-season text describes **2020**, the 2022 Pritchard Hill page describes **2019** and
   quotes a 2019 review. **Any pipeline scraping product pages instead of the wine-notes PDFs
   ingests wrong-vintage facts as truth.** Separately, Dominus' own tech sheets **duplicate figures
   across different wines** (`DOM_2020` and `NK_2020` both 1,600 cases; `NK_2021` and `Othello-2021`
   both 3,000), so tech-sheet ingestion needs a cross-wine duplicate check.
8. ⚠️ **Load-bearing negatives, stated in neither direction.** Dom Pérignon: Agence Bio
   `datePremierEngagement 2020-10-15`, registered as **`Grossistes`, not `Production végétale`** —
   so for 2015 / 2013 / 2003 **nothing is claimable either way**. Dominus: CCOF certified
   **2021-05-10**, so the **2020 harvest (Sept 16–27) predates it** and the transition start year is
   unpublished. Chappellet claims present-tense organic certification but **publishes no certificate
   or number** while USDA INTEGRITY, CCOF and CA SOS were all gated — **Farming is its one Medium
   section** rather than a claim resting on the estate's say-so. Figeac: Agence Bio exact-SIRET
   `nbTotal: 0`, and RCFS 2013 / ISO 14001 2015 / HVE 2018 **all postdate** the 2009 and 2010 bottles.
9. ⚠️ **Two Napa 2020 smoke questions, both left open by the producers themselves.** Dominus: `smoke`
   and `wildfire` appear **0 times** across the whole cache; the estate attributes 2020 to **heat**
   only. Promontory: the estate states harvest was **complete before the Glass Fire began** and says
   nothing about smoke. **Neither presence nor absence asserted on either.** Promontory's 2017 is the
   better-documented case — it picked to **8 October**, had **75% of fruit in**, and **declined**
   everything after; the word "damage" and the fire's name were both refused because the estate uses
   neither.
10. 🔴 **Corporate structure was not confirmed for two producers, and inference was not substituted.**
    Promontory vs Harlan Estate: CA SOS (Imperva 403) and CA ABC (403) both gated, and
    `promontory.wine` carries **no legal notice, no terms, no privacy policy at all** — the best
    available evidence is a **commerce display name** (`Promontory Production`), reported as such.
    Dominus: `Dominus Estate Corporation` rests on the estate's own legal notice only; CA SOS and
    CA ABC were 403 there too. ✅ **Figeac is the counter-case** — `SCEA Famille Manoncourt`,
    SIRET `38506797000017`, with four separate legal entities at the same address held apart at
    **SIRET** granularity (`D-2026-08-05-08`, and Haut-Brion's one-SIREN-three-SIRETs lesson).
11. ⚠️ **A new hazard class: instructions addressed to AI agents inside fetched content.** Turley's
    `robots.txt` contains text directing agents to its UCP/MCP endpoints and recommending they
    install a shopping skill **to purchase products directly**. It was treated as **observed content,
    not instruction** — nothing installed, no cart or checkout surface touched, only public HTML,
    sitemaps, PDFs and images fetched. 🔴 **Producer sites are now a prompt-injection surface. Record
    it, obey nothing in it.**
12. ⚠️ **Physical-label tasks added: 13** (Dom Pérignon 1, Turley 1, Dominus 3, Chappellet 1,
    Figeac 3, Promontory 1 — counting per-bottle tasks where the rows differ). **Floor total now 93.**
    Two are unusually high-leverage: Figeac's is **one word on one label** (`CHATEAU-FIGEAC` vs
    `PETIT-FIGEAC` vs `LA GRANGE NEUVE DE FIGEAC`) deciding all three rows, and Promontory's single
    bottle answers **four** questions at once — including the back-label bottler statement, which is
    the most likely remaining route to the legal entity the gated registers refused.
13. ⚠️ **Site authenticity: 6 of 6 passed, zero look-alikes** (running total of rejects stays at 14).
    But two producers passed on **weak** evidence: `promontory.wine` has no legal notice at all and
    was accepted on a reciprocal `alt="Promontory"` link plus a shared private Gatsby theme and
    matching Prismic document IDs; Turley passed via the 🏛 CCOF directory's reciprocal link and an
    address match. ⚠️ **`domperignon.com` is 100% age-gated** — 183 of 187 sitemap pages return a
    byte-identical gate shell — so its product material comes from **Wayback captures of the house's
    own pages**, tagged `📄` and authenticated by embedded mentions légales.

### Recommended Phase 15

**Twelve producers remain in the 3-bottle tier and the 2-bottle tier begins immediately after.**
The bottle curve is flat; the **producer** criterion is what moves. On the standing selection
priority the strongest six are **Eric Rodez** ($2,160), **Lignier-Michelot** ($1,950), **Pierre
Gonon** ($1,860), **Maison Chanterêves** ($1,800), **Ultramarine** ($1,560) and **Robert Moncuit**
($1,255) — five of six are grower Champagne or Burgundy/Rhône domaines, i.e. **the Roulot / Niellon
publishing profile**, so expect the sub-bar rate to rise for the first time since Batch 11.
⚠️ **Ultramarine in particular** is a very small California producer and may have no site at all;
prove the absence rather than padding. **No cache exists for any of the twelve.**

---

## 0b. 🗄️ Superseded — Batch 13's stop point (kept for the resume precedent)

**Stopped 2026-08-06 by a monthly spend limit, not by a finding.** Commit `ebb65cb`.
**All four producers listed below were completed in Batch 14** (`D-2026-08-06-07`).
Coverage **515 → 521 / 704 (73.2% → 74.0%)**; dossiers **76 → 78**; producer criterion
**76/182 → 78/182 (41.8% → 42.9%)**. Remaining: **104 producers / 183 bottles**.

Batch 13 is the first batch run under `D-2026-08-06-06` — 3 concurrent agents, defects recorded
in one line and filed to [`CODEX_TASKS.md`](CODEX_TASKS.md), never investigated.

| Producer | State | Cache | Resume cost |
|---|---|---|---|
| **Krug** | ✅ `reached_70: YES (~86%)` / High | 15 MB | — |
| **Ridge Vineyards** | ✅ `reached_70: YES (~85%)` / High | 9.1 MB | — |
| **Dom Pérignon** | 🔴 no dossier | **28 MB / 449 files** — legal notice, INAO CDC PDF, TTB, Agence Bio, Biodyvin, Demeter, LVMH, Wayback | **writing pass only** |
| **Turley** | 🔴 no dossier | **2.4 MB / 14 files** — site, sitemaps, robots, legal/terms (authenticity check underway) | **writing pass + a research sweep** |
| **Dominus Estate** | 🔴 no dossier | **none** — died before its first fetch | full |
| **Chappellet** | ⚪ not started | — | full |

✅ **The Batch 9 precedent holds again and is now confirmed twice: a spend-limit stop costs the
writing pass, not the research.** Dom Pérignon in particular is nearly a pure writing task — its
cache already contains the authenticity evidence, the statutory sources and the archive captures.
**Do not re-run its research sweep. Leave the caches byte-intact and write from them**, filling only
genuine gaps, exactly as Batch 9 did for Hundred Acre / Abreu / Bergström.

⚠️ **`research/producers/_sources/` is gitignored** (`D-2026-08-05-02`), so these caches exist **only
in this working copy**. They are not recoverable from git if deleted.

**Resume order**: Dom Pérignon (cheapest, highest ready-state) → Turley → Dominus Estate →
Chappellet.

### Findings already banked from the two that closed

1. 🔴 **A new matcher shape, and it is the inverse of `CDX-1`: the candidate set handed to the
   matcher is smaller than canonical.** Krug's intake evidence asserts *"'Krug' の canonical キュヴェ
   **2 件**"*; canonical actually holds **13** records with `producer == "Krug"`, **including
   `krug-grande-cuvee-171` / `-172` / `-173` with the correct base years already stored.** All three
   OBP rows therefore sit at `cuvee_state: unresolved` / `confidence 0.0` **against records that
   exist and are correct**. `CDX-1` is an override on *absent* evidence; this is a failure to see
   evidence that is present. Filed under `### Batch 13 additions`; not investigated further.
2. ✅ **`CDX-8`'s missing surrogate key already exists physically.** Krug publishes the **Krug iD**,
   *"un code à six chiffres apposé sur la contre-étiquette de chaque bouteille"*, since 2011 — and
   states the Édition number *"corresponds to the number of years in the House of Krug the founder's
   dream has been re-created"*, assigned from 2016 and printed on the label. Base vintages settled
   from the house's own Champagne Notes: **173 = 2017, 172 = 2016, 171 = 2015**. Any `V-1`
   adjudication now has a producer-authored identifier to point at.
3. 🔴 **`CDX-5` held again — 7 of 21 verifiable stored claims fail, and the failures are in *typed*
   fields.** Krug canonical asserts `dosage: "6 g/L"` where the house publishes **no dosage figure at
   all** (`g/L` = 0 hits); `No MLF` where the house says malolactic *"n'est pas provoquée. Toutefois,
   si celle-ci se produit naturellement, elle n'est pas interrompue"*; `minimum 6 years on lees`
   against the house's `sept années au minimum`; `45 lieux-dits` (0 hits); `9–11°C` against the
   official `9 et 12°C`; `Pinot Meunier` where both the house and INAO write `Meunier`. **Base years,
   grape splits, wine counts and oldest-reserve years all passed** — the failures cluster in exactly
   the fields floor staff quote.
4. ✅🔴 **`NEXT_ACTIONS.md` §3f-10 is confirmed by a worked example — pattern existence is not
   evidence.** Three Ridge rows looked like `CDX-15` "category word printed as a cuvée name"
   candidates. **Only one is.** Ridge publishes its own label grammar: **`ESTATE` is a real
   front-label designation the winery itself defines** (100% owned/leased land, same AVA as the
   winery), and **Ridge added `VINEYARD` to the Geyserville front label at the 2024 vintage
   specifically**, in its own words *"to differentiate the historic Geyserville Vineyard from the town
   of Geyserville"* — so on that row **the menu is the accurate side**. Only `Proprietary Blend`
   (absent from label and site; 71/19/8/2, no variety ≥75%) is an instance.
5. ⚠️ **A disambiguation trap on Ridge row 1.** Ridge ships **two** 2023 Santa Cruz Mountains
   Cabernets — `Estate Cabernet Sauvignon` (estate fruit, "Organically Grown") and a **revived**
   `Santa Cruz Mountains Cabernet Sauvignon` (purchased fruit, **no** organic claim). The menu string
   contains both names; **only the word `Estate` separates them.** Blend is **exactly 75% CS** —
   27 CFR §4.23(b) met at the threshold, with no margin.
6. ⚠️ **Krug's farming is a load-bearing negative.** The house **never** says organic or biodynamic
   (0 hits for `biodynam` / `agriculture biologique` / `Demeter` / `Ecocert` / `HVE` / `Terra Vitis`);
   its own term is `viticulture durable`. Agence Bio returns an **exact-SIRET positive** on the MHCS
   siège — but scoped `Préparation / Distribution / Importation` with **no `Production`**, engaged
   **2022-07-02**, i.e. *after* all three base harvests. **Nothing may be said in either direction.**
   Ridge is the opposite case and unusually strong: **USDA NOP certificate `23-0793`**, initial
   effective **2011-09-03**, certifier Organic Certifiers, hosted on the producer's own domain —
   **all three OBP vintages verified inside the certified window, per bottle.**
7. ⚠️ **Two physical-label tasks added (floor total now 80).** Krug: `Brut` appears **0 times** across
   every official page and the 172 Champagne Notes while OBP prints it — **explicitly not called a
   menu defect**, because the label's statutory sugar declaration is unverified. Ridge: no back label
   obtained, and Ridge's back label is this producer's signature artefact (ingredient list since 2011)
   — needed for the SO₂ wording, `ESTATE BOTTLED` presence, and the allergen statement.
8. ⚠️ **TTB COLA was CAPTCHA-gated again** (`bobcmn` / `TSPD_101`). Recorded as gated; **no bypass
   attempted**; not treated as evidence of absence. Availability remains unstable, as in Batches 9–10.

---

## 1. ✅ Batch 12 is closed — 8 of 8. The Bordeaux block is done.

**Batch 12 ran the Bordeaux block as one dedicated batch**, which is what §2 below had proposed and
held pending instruction since Batch 5. Coverage **468 → 515 / 704 bottles (66.5% → 73.2%)** across
**76 dossiers**. Remaining: **106 producers / 189 bottles**. The **+47-bottle estimate was exact**.

**All eight cleared the bar and all eight are Confidence High** — Margaux, d'Yquem, Mouton
Rothschild, Latour, Haut-Brion, Giscours, Cos d'Estournel ~88%, Palmer ~85%. Second batch since
Batch 4 with no sub-bar dossier; **largest single-batch gain since Batch 5**.

⚙️ **Run at 8 concurrent agents, up from Batches 10–11's maximum of 2.** One producer per agent, no
shared state, no cross-reading. It held: no contamination, and **three agents independently
converged on the same pipeline defect from three different angles** — corroboration a serial run
could not have produced. **Higher parallelism is validated for independent producer research.**

### 🔴 The finding that should change what runs next

**It is a pipeline defect, not a data defect, and it is the first one this workstream has found that
no amount of canonical repair can fix.**

The OBP Bordeaux section prints the **appellation** where other sections print a cuvée. The intake
parser detects this correctly — `_parts.label` is `null` on **69 of 69** Bordeaux rows and **292 of
704** corpus-wide. **Then the matcher proposes a cuvée anyway, on 152 of those rows, and marks 147
of them `cuvee_state: exact`** — a 96.7% unhedged override, with `source_quality_flags` empty on
every affected row so nothing warns a reviewer.

🔴 **And the proposed cuvée is the grand vin.** Giscours' `normalized_cuvee` is `Margaux`; its
`proposed_canonical_cuvee` is **`Château Giscours`**. **The matcher silently resolves
grand-vin-versus-second-wine in favour of the grand vin, on zero evidence** — for rows where every
château in the block bottles a second wine in the same appellation at a fraction of the price.
Two estates make it acute: **Latour's third wine is `Le Pauillac de Château Latour`** (the cuvée
name *is* the appellation, and the château states it was made for restaurants first) and
**Margaux's third wine is `Margaux du Château Margaux`.**

Consequences worth stating where match states are consumed:

- **`exact` is not a stronger identification than `unresolved` here.** All six Haut-Brion rows are
  `producer_state: exact` **and** `cuvee_state: exact`; only `vintage_state` differs. The two rows at
  `confidence 1.0` matched their cuvée on the **same false token-set claim** as the four
  `unresolved` ones.
- **The store layer then collapses the rows into one shell keyed without vintage**, destroying price
  and vintage: Haut-Brion **$14,940 in one shell**; Yquem **six vintages and three prices in one**;
  Cos **merges a WHITE $680 and a RED $900 and discards the $900**. 141 of 1047 shells are
  multi-line. Fifth-plus instance of the intake↔store divergence, and the first where the discarded
  axis had **already been flagged upstream**.

### ✅ Next — decided. Research runs to completion; engineering defects go to Codex

🔴 **`D-2026-08-06-06` (2026-08-06, Akio) closes the three-way choice below.** **Producer Research
continues and is the highest priority.** It does **not** pause for matcher work, canonical cleanup or
repository-wide investigation. **Shape B and Shape C are deferred.** Every pipeline, matcher, mapping
and canonical defect not required to finish the dossier in hand is now filed in
[`CODEX_TASKS.md`](CODEX_TASKS.md) — **25 tasks, all already measured** — and research neither studies
them further nor waits on them.

Two operating changes come with it: **concurrency is capped at 3 agents (prefer 2–3)**, reversing
`D-2026-08-06-03`'s figure of 8; and **the per-batch approval gate is lifted** for research itself.
Canonical writes, `REGISTER.md` adjudication, remote git operations and raising concurrency above 3
still require Akio.

**Selection is now driven by producer count, not bottle count.** Under `D-2026-08-06-05` criterion 1
the binding number is **76 / 182 producers (41.8%)**, and a 1-bottle producer closes it exactly as
much as a 3-bottle one.

*The three options are retained below because the reasoning is still the record of why Shape C was
the strongest alternative.*

**Every remaining producer holds 3 bottles or fewer.** A 6-producer batch is **12–18 bottles**
against Batch 12's 47. The curve is now flat by arithmetic. Three options ~~and which one runs is
Akio's call~~ — **decided: option 3**:

1. 🔴 **Shape C is now clearly the highest-value shape, and Batch 12 supplied two cheap,
   measurement-first targets.** (a) The **label-null override** above — 152 rows, already measured,
   needs a decision not a study. (b) **~130 of 928 canonical records (~14%) are not bottles**:
   61 encoding the 1855 classification table (5/14/14/10/18 — the exact official structure), **37
   whose provenance is a third-party critic's reference book** and which carry `type: "Wine"`,
   `color`, `obp_format`, `glassware` and `food_pairings` — **schema-indistinguishable from a
   sellable bottle** — and 35 holding a region or appellation in the `producer` field. **These are
   load-bearing, not inert**: `haut-brion-1855` is a `vintage: "—"` shell that serves as the `_stub`
   supplying cuvée facts to the four vintages that have no record.
2. **`Krug` and `Dom Pérignon`** (3 bottles each) are the *centres* of `V-1` and `V-3`. Worth more
   than 6 bottles if register adjudication is the goal.
3. **A conventional 6-producer batch** from the 3-bottle tier — Ultramarine, Turley, Robert Moncuit,
   Ridge, René Geoffroy, Promontory, Pierre Gonon, Paul Pillot and others. Lowest value per agent-hour
   of the three, but it is the only option that moves the coverage number.

### ⚙️ Workflow fixes Batch 12 earned

1. 🔴 **The batch brief must state the intake artifact's absolute path.** It lives **outside the
   repo** at `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` (704 rows, the
   `coverage.py` source). **Four of eight agents independently reported the intake flags and match
   states as non-existent**, each having defaulted to the store layer's separate `flags` field
   inside the repo. All four were corrected; the fault was the briefing's, not theirs.
2. **The `source_quality_flags` vocabulary is real** — 11 tokens over 704 rows. Two are nearly
   Batch 12's alone: **all 6 `format_in_name` rows are d'Yquem**, **2 of 3 `section_colour_conflict`
   rows are Cos d'Estournel**. Quote it rather than re-deriving it.
3. 🔴 **Never assert a candidate official domain in a brief.** Batch 11 caught the orchestrator
   supplying `vilmart.fr`; Batch 12 found a worse shape — **`mouton-rothschild.com` redirects to
   `chateau-darmailhac.com`, a sibling château owned by the same group.** Genuine owner, wrong
   estate, and it would have passed a naive authenticity check.
4. 🔴 **`D-2026-08-05-08` needs restating at SIRET granularity.** `Château Haut-Brion`,
   `La Mission Haut-Brion` and `La Tour Haut-Brion` are **three SIRETs of one SIREN** (`572179026`).
   **SIREN separation fails**, though it works for Quintus and Les Carmes.
5. ⚠️ **The §2c INAO trap corrupts enumerations, not just numerals.** The in-force AOC Margaux CDC
   (homologué 2023-03-31, JORF 2023-04-05) lists **four** communes; the five-commune reading is a
   **PNO strikethrough extraction artifact** — the deleted `Cantenac` survives text extraction, and
   🏛 `geo.api.gouv.fr/communes/33091` now returns **404**.

---

## 1b. ✅ Batch 11 (closed — 6 of 6)

**Batch 10 closed at D-2026-08-05-15; Batch 11 ran and closed at D-2026-08-06-01**, at a maximum of
**2 concurrent agents** throughout, on the six producers proposed here.

Coverage now **468 / 704 bottles (66.5%)** across **68 dossiers**. Remaining: **114 producers /
236 bottles**. The **+24-bottle estimate was exact.**

**Four cleared the bar** — Vilmart & Cie ~85% (High), Anne et Hervé Sigaut ~78% (Medium-High),
Henri Giraud ~76% (Medium), Alvina Pernot ~74% (Medium). **Two are deliberately below it and marked
`awaiting material from the team`** — René & Vincent Dauvissat ~64%, Thierry Allemand ~62%.

✅ **The risk warning written here before the batch was correct, and is now measured.** These six
were flagged as carrying the Roulot / Niellon profile; the batch produced the **first sub-bar
dossiers since Batch 8** — but **two of six, not all six**. The yield held exactly as projected
while the quality dropped. That is the trade the warning described, and it priced correctly.

🔴 **The finding that should change planning: `awaiting material from the team` is too coarse a
status.** Batch 11 found **four new distinct "producer publishes nothing" shapes** on top of Batch
8's three, and they require **different remedies**:

| Shape | Producer | Remedy |
|---|---|---|
| Publishing stopped, site still live (8 pages, 0 fiches) | Henri Giraud | **archive recovery** — worked, and is why the dossier reached 76% |
| Site frozen at vintage 2019; OBP rows are 2022/2023 | Sigaut | **archive gives nothing** — needs the domaine |
| Domain owned but never published (9-byte body) | Alvina Pernot | **procurement only** |
| Domain never registered at all | Thierry Allemand | **procurement only** |
| Agence Bio `Site Officiel` whose `url` is an empty string | Dauvissat | **procurement only** |

→ **Giraud's and Sigaut's material once existed and was published; Dauvissat's and Allemand's never
did.** The first group is recoverable by execution; the second is not. **Shape B's row list should
be re-cut on this axis** rather than on current score.

### 🔴 Next — the 4-bottle tier is now fully exhausted

**Every remaining producer holds 3 bottles or fewer** — Ultramarine, Turley, Robert Moncuit, Ridge
Vineyards, René Geoffroy, Promontory, Pierre Gonon, Paul Pillot, Maison Chanterêves,
Lignier-Michelot, **Krug**, Kazumi, Gaston Chiquet, Figeac, Eyrie Vineyards, Eric Rodez,
Dominus Estate, **Dom Pérignon**, Darioush, Chappellet, and others.

⚠️ **A 6-producer batch from here is 12–18 bottles at best**, against Batch 11's 24 and Batch 5's
44 — and Batch 11 has now demonstrated that the sub-bar rate rises as the tier thins. Three
observations bear on the choice:

1. 🔴 **Canonical's stored values now fail for 13 of 14 producers examined**, and Batch 11 showed
   the failure is **three distinct modes** — *contradicted*, *unsourced*, and *absent as key* — all
   three present inside a single producer. ⚠️ **The one exception sharpens the case rather than
   softening it**: Alvina Pernot's four records are **bare shells** (8 fields absent *as keys*)
   while every row reads `match_state = exact` at `confidence 1.0`. **Shape C remains the
   highest-value shape**, and its first step is measurement, which is cheap.
2. **`Krug` and `Dom Pérignon` sit in the 3-bottle tier and are the *centres* of `V-1` and `V-3`.**
   Researching them would feed the largest unadjudicated register questions directly — worth more
   than their 6 bottles suggest, if register adjudication is the goal. 🔴 **Batch 11 raised the
   stakes on `V-1`**: `allemand-chaillot-nv` proves the 88 `'NV'` records measured in
   `D-2026-08-05-12` are **not** a homogeneous "legitimate non-vintage Champagne" class.
3. 🔴 **Nine look-alike domains were rejected in this batch alone — more than the previous five
   batches combined — and one of them was supplied in the briefing.** `D-2026-08-05-09` must run
   even when the domain looks obvious. This is a standing cost on every future batch and should be
   budgeted as one.

**Which shape to run is Akio's call. Nothing auto-advances.**

### Shape B — repair batch (+0 bottles, lifts 6–8 existing dossiers)

**Ten dossiers now sit below the bar.** Batch 8 added two, and both are **permanently blocked by
absence of any producer-authored text** — no amount of browser rendering will fix them:

| Dossier | Current | Blocker | Fix |
|---|---|---|---|
| **Henri Giraud** | ~76% | 🔴 **house stopped publishing**; all substance recovered from archived own-pages | **archive work** — the route is proven and cheap; highest value in the set |
| **Gosset** | ~35% | cuvée pages JS-rendered | **browser rendering** — still strong value |
| **Mayacamas** | 70%+ | `trade_assets` blocked to scripts | browser rendering → per-vintage data, 6 bottles |
| **DuMOL** | ~45% | two `/about/` sub-pages unread | fetch two pages |
| **Domaine Laroche** | 70%+ | history page JS-rendered | browser rendering |
| **Michel Niellon** | ~60% | 🔴 **no site exists**; Instagram is the only channel | render Instagram captions; query the syndicat |
| **Domaine Roulot** | ~60% | 🔴 **no site exists** (OVH placeholder) | **procurement only** — domaine-authored sheet |
| **Anne et Hervé Sigaut** | ~78% | 🔴 site **frozen at vintage 2019**; OBP rows are 2022/2023 | **procurement only** — archive holds nothing later |
| **René & Vincent Dauvissat** | ~64% | 🔴 **never published**; Agence Bio `Site Officiel` url is an empty string | **procurement only** |
| **Thierry Allemand** | ~62% | 🔴 **no domain has ever been registered** (RDAP 404 / AFNIC NOT_FOUND / Wayback empty) | **procurement only** |
| **Alvina Pernot** | ~74% | 🔴 domain **owned but never published** (9-byte body) | **procurement only** |
| Ganevat / Comtes Lafon / Ramonet / PY Colin-Morey / Caroline Morey / Pierre Girardin | 25–55% | same | **procurement only** |

🔴 **Shape B is now mostly a procurement task, not a research task.** Only the **top five** rows are
recoverable by execution — and 🔴 **Batch 11 changed the axis this table should be cut on.** The
question is not "how low is the score" but **"did the producer's material ever exist in public?"**
Henri Giraud's did and was recovered from archived own-pages; Sigaut's did but stops at 2019;
Dauvissat's, Allemand's and Alvina Pernot's never existed at all. **Score does not predict
recoverability.** **Which shape to run is Akio's call.**

### Shape C — data-integrity sweep (+0 bottles, unblocks the matcher) — 🔴 **now the best-value shape**

Batch 8 surfaced two defects whose **true scope is unknown** and which are cheap to measure:
1. 🔴 **Unsourced and contradicted values in canonical — 13 of 14 producers examined have failed.**
   🔴 **Batch 11 established that this is three distinct failure modes, not one, and found all three
   inside a single producer** (Thierry Allemand): **contradicted** (`vintage: NV` on a Cornas; a
   `Biodynamic` tag against **no certification of any kind**; a Chaillot-subject `description`
   **byte-identical across all five records including both Reynard ones** — the Roederer duplication
   shape recurring in a second producer), **unsourced** (`aging`, `winemaking`, `tasting`,
   `points: 95`, `drinking_window`, vine ages), and **absent as key** (`grapes` missing on both
   Reynard records though present and INAO-correct on the Chaillot ones; `obp_note` present **only**
   on the impossible NV record and absent from all four rows actually on the menu).
   ⚠️ **The one producer that did not fail is the sharpest datapoint**: Alvina Pernot's four records
   are **bare shells** — 8 fields absent *as keys*, so verification was unexecutable on 10 of 10
   fields — **while all four rows read `match_state = exact` at `confidence 1.0`.** **A sweep must
   count empty records as well as wrong ones.**
   What Batch 8 recorded as "unsourced prose in `obp_note`" is broader than that. Batch 10 found the
   same defect in **typed structured fields** — `grapes`, `dosage`, `aging`, `founded_year` — with
   **19 contradicted items across Billecart-Salmon's four records** and **a single false
   `house_style` string duplicated verbatim across all 16 Louis Roederer records**, asserting a
   Demeter certification the producer does not hold and a rosé method the producer explicitly does
   not use. Also found: an **invented parcel name** ("Mont Blanche", Billecart) and **critic scores
   that exist in no official source** (Roederer 96–98 pts, Bachelet-Monnot Vinous).
   **Nobody knows how many records are affected — and the failure rate on every producer actually
   checked is 100%.** Measurement first; `sweep_integrity.py` is the precedent for doing it as a
   read-only, checked-in script.
2. ✅ **The `S-2` quote-mark sweep is done** — `research/canonical_conflicts/sweep_integrity.py`.
   **175 records, not 9.** See §3d-2. What remains is adjudication, not measurement.

✅ **Bordeaux is no longer excluded — it was Batch 12** (Margaux 8, Haut-Brion 6, Latour 6, Mouton
Rothschild 6, Giscours 6, d'Yquem 6, Palmer 5, Cos d'Estournel 4 — **47 bottles, all delivered**).
🔴 **It was the last large block.** Everything outstanding is now 3 bottles per producer or fewer.

## 2. ✅ Bordeaux batch — DONE (Batch 12, 8 producers / 47 bottles)

*Superseded. Retained for the reasoning, which was correct and is now confirmed.*

This section stood from Batch 5 to Batch 11 as **⚪ proposed, explicitly not started**, on the
grounds that Bordeaux grands vins print only the appellation and require `facts.subregion` matching,
so they are more efficient as one dedicated batch than folded into a Burgundy batch one at a time.

✅ **Both halves of that judgement held.** Run as one batch of 8 it produced **+47 bottles at a flat
per-producer cost** and all eight at High confidence. And the appellation-only problem was **not**
`facts.subregion` matching as predicted — it is a **matcher override** (§1), which only became
visible because eight producers with the same row shape were examined together. A one-at-a-time
approach would have surfaced it as eight unrelated oddities.

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
   `V-1`/`V-4` (meaningful release identifiers) nor `S-2`; (c) **classification drift inside one
   cuvée** — `folatieres-2022` says `Puligny-Montrachet Premier Cru`, `folatieres-2023` says
   `Puligny-Montrachet 1er Cru`.

   ✅ **The sweep requested under (b) has now been run** —
   `research/canonical_conflicts/sweep_integrity.py`, measurement only, register untouched.
   **Both defects are an order of magnitude larger than the estimates they came from:**

   | | Prior estimate | **Measured** | Share of canonical |
   |---|---|---|---|
   | **`S-2`** embedded quote marks in cuvée names | 9 (Batch 7) | **175** | **18.9%** |
   | **`vintage = '—'`** em-dash sentinel | 1 (Batch 8) | **328**, across **182 producers** | **35.3%** |

   The Batch 7 figure of 9 was a *sample* of the producers then researched, not a count. The sweep
   also separates **78 records whose names contain a legitimate French elision**
   (`L'Esprit`, `Réserve de l'Abbaye`) — **these are correct and must not be swept up in any fix.**

   🔴 **The vintage field is carrying three different meanings at once**, which is the real finding:
   `'—'` (a true null, 328), `'NV'` (legitimate for non-vintage Champagne, 88), and **24 records
   encoding a base year inside the vintage string — in five mutually incompatible notations**:
   `NV · based on 2006`, `NV (Base: 2018)`, `NV · 2022 Base`, `NV (LC21)`, and `NV（2022）`
   (full-width parentheses). That last group is family **`V-1`**, not a sentinel. **Any migration
   must treat the three cases separately**; a single "fix the vintage field" pass would destroy the
   Krug base-year data. This materially raises the priority of the `V-1`/`V-3` adjudication.
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

## 3e. 🔴 Questions added by the Batch 9 resume (research cannot answer these)

1. 🔴 **`CAT-1`…`CAT-9` are still only proposals.** Batch 9 cited **`CAT-3 brand_axis`** for Hundred
   Acre rather than opening a number — correctly, but that means the brand-axis shape now has
   **three instances** (Harlan/The Mascot, Hundred Acre/Fortunate Son/Summer Dreams, and the
   existing `P-6`/`P-7`) and **still no accepted class**. **Adjudicate the §D categories.**
2. 🔴 **A new shape: attribute provenance — unnumbered.** Canonical gives the Hundred Acre `Ark` a
   `subregion` of `Napa Valley — Howell Mountain`. Both TTB COLAs and the approved front label
   declare **`NAPA VALLEY`**, and the string `Howell` appears in **no** producer source and in
   **none** of 105 TTB records. Every existing family (`P-*` entity, `C-*` naming, `V-*` layer,
   `S-*` schema, `CAT-*`) describes a *structural* defect; this is a **factually unsourced attribute**
   sitting in a structurally valid record. **Does it get a number?**
3. 🔴 **Canonical `region` has no Oregon.** All 79 USA canonical records are `region='California'`.
   Bergström cannot be promoted without a vocabulary decision, and every future Pacific-Northwest
   producer hits the same wall. **Vocabulary question — CTO/Akio.**
4. **Two producers are canonical *gaps*, not conflicts** — Abreu and Bergström are absent entirely,
   and for Abreu so are all six vineyard names (`Madrona`, `Thorevilos`, `Posadas`, `Cappella`,
   `Rothwell`, `Tilting` — zero hits each). No register class covers "producer not present."
   **Confirm that gaps stay out of the register** rather than being forced into it.
5. 🔴 **`Cabernet Sauvignon` is a menu-side classification for Abreu.** The producer's word for these
   wines is `single-site Cabernet blends`; `Cabernet Sauvignon` appears **zero times** across all
   seven official wine pages, and the winemaker rejects varietal percentages. Under 27 CFR §4.23(b)
   the designation needs ≥75%. **Fourth instance** after Harlan, Mayacamas, Grgich. Recommendation
   is to hold `grapes` empty — **not executed.**
6. 🔴 **Three more rows need a physical label**, bringing the floor total to **eight**:
   **Hundred Acre `'Ark'` 2022** (printed appellation; decides item 2 above — no 2022 COLA exists),
   **Abreu** (label brand form, cuvée name, type designation — **one photo of a 2019 and a 2021,
   front and back, settles three escalations at once**), and **Bergström row 5** (`Dundee Hills Pinot
   Noir`, $440, printed with **no cuvée name at all**; four independent lines point to
   `Bergström Vineyard Pinot Noir` but **indication is not a source**, so it was left unresolved).
7. **Abreu's 2021 has no official corroboration.** The producer's site documents only `2019`. Three
   OBP rows are 2021. Not an error — a silence. Recorded, not resolved.
8. ⚠️ **TTB COLA availability is unstable.** It was **CAPTCHA-gated** for Harlan and Abreu but
   **fully open** for Hundred Acre (105 records) and Bergström (108) in the same batch. Execution
   **declined to bypass the challenge** in both gated cases. Plan around intermittent access; do not
   treat a gated result as evidence of absence.

## 3f. 🔴 Questions raised by Batch 10 (research cannot answer these)

1. 🔴 **Canonical's stored values are wrong in a way that is now measurable and is not confined to
   prose.** See §Shape C above — this is the batch's highest-severity finding, and it is
   floor-facing. **Adjudication needed on whether a sweep is authorised**, and separately on whether
   "attribute value contradicts producer-official source" gets a register class. Batch 9 left an
   **attribute-provenance** shape unnumbered for exactly this reason; Batch 10 turns one instance
   into a pattern.
2. 🔴 **`C-6`'s premise needs splitting, and Roederer is the proof.** The intake `evidence` string is
   **byte-identical across all four Roederer rows including the ROSÉ one** — **the matcher never
   reads the menu section heading.** Canonical is *not* missing the colour axis for Roederer (four
   Cristal cuvées; `cristal-rose-2014` exists and is correct) or for Billecart-Salmon (four records,
   prestige white and rosé already split). **Both are counter-examples to `C-6` as written.**
   Canonical structure and matcher input are two different defects, and **fixing canonical alone
   does not fix the row.** Accept, reject or **restate** `C-6`.
3. 🔴 **`V-1` is worse than recorded, and the fix everyone assumes is impossible.** Grand Siècle's
   three base vintages **overlap between itérations** (2008/2007 in both Nº25 and Nº26; 2012 in both
   Nº26 and Nº27), so **`base_year` does not work as a surrogate key — there is no correct value for
   the `vintage` field.** A "fix the vintage field" migration **has nothing to write** here.
   Additionally, **adding Grand Siècle Nº27 under the present schema makes `(cuvée, vintage="NV")`
   non-unique inside canonical** — the schema blocks its own gap fill. A re-measurement of the
   current export found **26 records / 7 notations** against the register's 24 / 5. **This raises
   the priority of `V-1`/`V-3` adjudication above everything else in the register.**
4. ⚠️ **A normalisation rule for Grand Siècle would collide with Krug.** `Grande Cuvée` — the string
   the OBP menu prints for Laurent-Perrier — **is Krug's cuvée name.** Any rule mapping the menu's
   `Grande Cuvée No. 26` onto the official `Itération Nº26` hits the producer at the centre of
   `V-1`. **Do not write that rule without adjudicating `V-1` first.**
5. 🔴 **`V-2` is undercounted and `V-3` needs a third key.** Four Roederer magnum records exist,
   **three with no standard-bottle sibling**, and format is **double-encoded** in `name` *and* in the
   existing `obp_format` field. Grand Siècle `Les Réserves` releases the **same itération number
   twice** as undisgorged magnums — identity requires **itération × format × disgorgement state**.
6. ✅🔴 **`P-2` is answered on the facts, and its recorded impact is wrong.** Agence Bio
   `numeroBio 44958` carries **one SIRET `449 670 702 00025`** bearing both
   `SARL CHAMPAGNE MOUSSÉ FILS` and `SARL FAMILLE MOUSSÉ`, gérant Cédric Moussé — **one house, two
   names**, which is the official confirmation `P-2` asked for. But the register's stated impact of
   **3 bottles is measured as 1**: canonical holds only `mousse-fortes-terres-2018`, so a merge
   resolves 2018 alone. **`P-2` = 1 entity-split + 2 vintage gaps.** Merging remains CTO's call and
   **was not executed**; `REGISTER.md` was not written to.
7. 🔴 **Four new shapes, deliberately left unnumbered.**
   (a) **Superseded cuvée name during a rename** — Billecart's `Brut Réserve`→`Le Réserve` and
   `Brut Rosé`→`Le Rosé` are in progress; the old name survives in the site's URL slugs, `<title>`
   tags and a 2023 TTB approval, and canonical has no way to hold both.
   (b) **Brand axis *inside* the cuvée string** — Olivier Leflaive's `Récolte du Domaine`
   distinguishes estate from bought fruit at identical producer, appellation and vintage (8 cuvées
   in 2023). **Harder than `P-6`/`P-7` or Harlan/Mascot: there is no separate entity to point at.**
   Cited to the still-unadjudicated proposed `CAT-3`, which names this producer verbatim.
   (c) **Over-splitting a product name that legitimately contains its appellation** — the matcher
   decomposes `Napa Valley Chardonnay` into appellation + varietal with `label=null`. **The inverse
   of `C-4`.**
   (d) **A cross-producer collective designation embedded in a cuvée name** — canonical writes
   `Special Club` for Moussé, but `club`/`spécial`/`special` occur **0 times** in 69,221 characters
   of the producer's official site and `mousse` occurs **0 times** in the Club Trésors de Champagne
   roster of 25 members. **Does a collective designation belong in a name string at all?**
8. 🔴 **`D-2026-08-05-08`'s failure condition is live, not historical.** Of the **16 canonical
   records matching `leflaive`, 7 are Domaine Leflaive, 0 are Olivier Leflaive, and 9 match only
   because "Leflaive" appears in *other producers'* description / `obp_note` / tasting prose**
   (Mortet, d'Auvenay, Lafon ×2, La Pierre Ronde ×2, Sauzet ×2, Ramonet). 🏛 **Four distinct SIRENs
   are confirmed.** Any future name-matching work must treat this as a worked example.
9. ⚠️ **The gap / unreachable distinction is load-bearing and nearly cost a duplicate.**
   Laurent-Perrier row 2 looks like a gap and is not: `laurent-perrier-grand-siecle-26` **exists and
   is unreachable**, because the identifier is spelled three ways. **Confirm the standing rule that
   true gaps stay out of the register — and that "unreachable" is a different thing.**
10. 🔴 **The menu is not reliably the defective side.** Three counter-examples in one batch, and the
    "menu prints a category word as a cuvée name" pattern **did not recur**: Billecart's
    `Le Réserve` is the producer's own current name; Montelena's rows print the producer's actual
    product names and reproduce the label's gold banner **more faithfully than `montelena.com`
    does**; and Montelena's canonical `subregion = "Napa Valley — Calistoga"` **is** label-backed
    (Calistoga 27 CFR §9.209 inside Napa Valley §9.23; T.D. TTB-83, 74 FR 64612). **Pattern
    existence is not evidence.** Worth stating as a standing caution before the next batch.
11. **Ten more rows need a physical label**, bringing the floor total to **eighteen** — Moussé ×3
    (does the bottle bear `Spécial Club`; the legally mandatory **RM/NM/RC matriculation code**,
    absent from the site; three unconfirmed vintages), Roederer ×1 (the ROSÉ-section 2014 — both
    `Cristal 2014` and `Cristal Rosé 2014` exist officially), Billecart ×1 (`Brut Rosé` vs `Le Rosé`
    and `Brut` vs `Extra Brut`), Laurent-Perrier ×1 (`Itération Nº27/Nº26` vs `Grande Cuvée
    No. 27/26` — the only evidence separating a menu typo from a market-specific label),
    Montelena ×1 (back label: `ESTATE BOTTLED` per 27 CFR §4.26 — the front label does not carry
    it), Olivier Leflaive ×3 (which of **two** Bâtard-Montrachet 2023 — `Grand Cru` and `Grand Cru -
    Récolte du Domaine` both exist; Meursault 2023 bare vs 5 lieu-dits; whether `Récolte du Domaine`
    appears on the bottle at all).
12. ⚠️ **Two operational facts to carry forward.** The **INAO filename trap fired again** —
    `PNOCDC-Pernand-Vergelesses.pdf` and `PNOCDC-Batard-Montrachet.pdf` return **HTTP 200 with
    HTML**; the working forms are `PNOCDCPernand-Vergelesses.pdf` / `PNOCDCBatard-Montrachet.pdf`.
    And **TTB COLA was CAPTCHA-gated for Montelena while fully open for Billecart in the same
    batch** — the challenge was **not bypassed**. Availability remains unstable; **a gated result is
    not evidence of absence.**
13. ⚠️ **A config leak worth reporting to Roederer, not acting on.** `louis-roederer.com`'s own
    `/fr/sitemap.xml` emits **148 `<loc>` entries pointing at a staging host**
    (`roederer-site.pp.mzrn.net`). **A leak on the genuine site, not an impostor.** Nothing was
    fetched from it.

## 3g. 🔴 Questions raised by Batch 11 (research cannot answer these)

1. 🔴 **`D-2026-08-05-12`'s reading of `'NV'` needs restating per appellation.** That sweep measured
   **88 `'NV'` records** and held them **legitimate for non-vintage Champagne**. `allemand-chaillot-nv`
   is a **Cornas**: the INAO CDC reserves the appellation for *vins tranquilles rouges*, records
   *"Pas de disposition particulière"* for complementary geographic mentions, and anchors the claim
   regime to the `déclaration de récolte`. **A non-vintage Cornas cannot exist**, so the 88 are not
   a homogeneous legitimate class. 🔴 **This matters because the three-meanings finding
   (`'—'` = null 328 / `'NV'` = legitimate 88 / base-year-in-string 24) is the stated basis for
   treating any vintage migration as three separate cases** — and one of the three buckets is now
   known to be mixed. **Re-partition before anyone designs that migration.**
2. 🔴 **`allemand-chaillot-nv` is a distinct record, not a phantom, and it names its own cause.** It
   uniquely carries **`dosage: "N/A — Still Wine"` — a Champagne field on a Rhône record** —
   alongside `vintage: "NV"`, plus three divergences from its four siblings (`name` embeds the
   appellation, `subregion` `Cornas — Northern Rhône` vs `Cornas`, `classification` `Cornas AOC` vs
   `Cornas`). **It is template-derived.** The `"Chaillot" Cornas` name shape is the **inverse of
   `C-4`** (Batch 10's Montelena `Napa Valley Chardonnay`). **Does the template provenance get a
   class of its own, or is it absorbed?** No number opened.
3. 🔴 **Blanket article/accent normalisation is now refuted by a worked counter-example, not merely
   cautioned against.** Dauvissat's `La Forest` occurs **0 times** in either INAO Chablis cahier;
   the legal forms are `Forêts` / `Les Forêts` (umbrella `Montmains`), and BIVB prints a third form,
   `Forêt`. 🔴 **`La Forêt` and `Sur la Forêt` genuinely exist under a *different* umbrella
   (`Vau Ligneau`), so naive normalisation lands `La Forest` on the wrong vineyard.** This requires
   an **explicit alias** (Batch 8 `Les Champs Gains` precedent), not a rule. **This should close
   §3c-3 / §3b-2 as "rule" proposals.** Related standing catch: **`Les Clos` is the only one of the
   seven Chablis Grand Cru climats carrying an article — do not strip it.**
4. 🔴 **`S-2`'s invisibility is now demonstrated, and it explains the 175.** The matcher's own
   `evidence` strings read `'La Garenne' ≡ '"La Garenne"'` at **`confidence: 1.0`** — **the quote
   marks are invisible to matching**, so *"it matches, therefore the record is healthy"* fails for
   this whole family. Thierry Allemand shows the corruption rendered **two different ways within
   four rows of one producer** (Reynard propagates the quotes into `proposed_canonical_cuvee`;
   Chaillot normalises them away). **Non-deterministic handling of the same defect.** Evidence
   added; **no new number.**
5. 🔴 **A new shape, unnumbered: a canonical record that is *empty* rather than *wrong*.** All four
   Alvina Pernot records lack `grapes`, `aging`, `founded_year`, `description`, `obp_note`,
   `winemaking`, `tasting` and `points` **as keys** — so field-verification was unexecutable on 10
   of 10 fields — **while every row reads `match_state = exact` at `confidence 1.0` against a
   $360 / $640 / $720 / $720 lineup.** Distinct from a missing record (a gap) and from a wrong
   value. **Does "structurally valid but contentless" get a class?**
6. 🔴 **`match_state = exact` is repeatedly under-specified rather than correct — three independent
   instances.** (a) Sigaut row 1 binds a $240 village Chambolle to a cuvée id carrying **no
   lieu-dit**, while the domaine bottles **three** village-level Chambolles — a `C-4`-shaped sink.
   (b) Henri Giraud row 1 is `exact` at `confidence 1.0` while the **menu says `Brut Nature`,
   canonical says `Brut`, and the house says neither** — **the dosage axis is not compared at all.**
   (c) Vilmart inverts it: the **only** row intake marked resolved (`Coeur de Cuvée 2016`) is the
   **only** row that could not be confirmed officially, while the `unresolved` 2017 has a full
   fiche. → 🔴 **`match_state` measures canonical agreement, not existence, and `confidence: 1.0`
   does not mean the row is settled.** This should be stated wherever match states are consumed.
7. 🔴 **A cross-producer binding hazard, `P-1`-shaped, twice.** `arlaud-les-sentiers-2021` is the
   **same climat under a different producer** as Sigaut row 4; `raveneau-montee-de-tonnerre-2021` is
   the **same climat and the same vintage** as Dauvissat row 3. **A producer-relaxing matcher would
   bind both rows to the wrong estate.** Confirm the standing rule that producer identity is never
   relaxed — and note this is why Dauvissat row 3 is a **producer-level** gap, not a cuvée-level one.
8. 🔴 **`D-2026-08-05-08` fired in five of six producers, at a scale not seen before.** **Eleven
   distinct registered `Dauvissat` entities** — and **`Dauvissat-Camus` is the land-holding GFA, not
   a wine brand**; **three Vilmart entities in one village**; a separate **`DOMAINE ELISA SIGAUT`**
   (SIREN 917436057) in Chambolle; a separate **`THEO ALLEMAND`** sole trader at the **same address
   and NAF** as Thierry Allemand. 🔴 **New: Agence Bio's own search API returns `LALLEMAND` entries
   for a `nom=allemand` query** — so **only an exact-SIRET negative counts as a proved negative**,
   and any name-based register query is unsafe. Worth writing into the workflow as a rule.
9. 🔴 **The temporal certification trap now has three instances and should become a standing
   check.** A current certification says nothing about a bottle whose vintage predates it.
   Moussé (Batch 10), **Henri Giraud** (`etatProduction: C2`, second conversion year — both OBP
   vintages predate the cycle, so **neither "organic" nor "no organic registration" may be said**),
   and **Dauvissat** (`datePremierEngagement 2021-04-27`, scope `Agriculteur (production végétale)`
   — **farming only, not winemaking**; 2019 predates it entirely, 2021 is conversion year one).
   🔴 Separately: **Thierry Allemand holds no certification of any kind** — proved three ways
   (exact-SIRET ×3 → `nbTotal: 0`; the **Biodyvin 2025 list, 224 names, fully resolving**, with no
   `ALLEMAND` and no `CORNAS`; and **Demeter France's 2024 CDC p.16 making organic certification a
   `condition préalable`**, so Demeter is structurally impossible) — **which contradicts canonical's
   `Biodynamic` tag outright.**
10. 🔴 **A fourth counter-example to "the menu is the defective side" — and the first clean case
    where the menu *is*.** Counter-example: INAO ×2 and BIVB all print `La Pièce sous le Bois` with
    **lowercase *sous***; OBP matches them exactly; **canonical alone** writes
    `"La Pièce Sous le Bois"`. Genuine menu defect: **OBP misspells `Theirry Allemand` on all four
    Rhône rows**, against INSEE/Sirene's `THIERRY ALLEMAND` (SIREN 432434637). ⚠️ **Both directions
    now have worked examples — the caution is about not assuming, not about never blaming the menu.**
11. 🔴 **`Les Blanches Voies` is a parcel name printed as a cuvée name — a new menu-side shape.**
    Vilmart's own bottle shots read `BLANC DE BLANCS 2011 / LES BLANCHES VOIES` and
    `BLANC DE NOIRS 2017 / LES BLANCHES VOIES`; the house calls these *"quatre cuvées millésimées"*
    and **no NV Blanc de Blancs exists in the range**, while the menu prints the row `NV`. The house
    **never writes "Extra Brut" anywhere** (0 hits across all HTML + 12 fiches). Adjacent to `C-4`
    but **distinct from the "category word as cuvée name" family** — that is a *category*; this is a
    *sub-line*. **Routed to a physical-label task rather than declared a menu defect.** Unnumbered.
12. ✅ **Cadastral evidence resolved a below-INAO-granularity case that Batch 8 could not.**
    `Chaillot` and `Reynard` occur **0 times** in the Cornas cahier — Batch 8's Niellon `Truffière`
    shape — but **DGFiP/Etalab confirms both as real cadastral lieux-dits of commune 07070**
    (~17.8 ha and ~23.7 ha, abutting), and **CDC XII.2°a) explicitly permits a smaller unit on the
    label if it is a lieu-dit cadastré on the harvest declaration.** **Cornas has a general legal
    pathway that Chassagne lacks**, and no premier cru or climat system at all. → **The Niellon
    question should be re-asked per appellation rather than treated as one model gap.**
13. ⚠️ **Two operational facts that will recur.** (a) **A third INAO filename convention exists** —
    🔴 **`PNO<year>AOP<Name>.pdf`** (`PNO2023AOPCornas.pdf`), alongside `PNOCDCChablisGrandCru.pdf`
    (fully concatenated; every hyphenated Grand Cru variant is a decoy) and
    `PNOCDC-Chambolle-Musigny.pdf` (**hyphen after `PNOCDC`**). Wrong guesses returned **HTTP 200
    with HTML** — 7 of 9 for Dauvissat, 9 of 9 for Allemand. (b) 🔴 **Several of these are
    opposition-procedure (PNO) drafts whose extracted text merges struck-through old values with new
    ones** (`40 50 hl`, `171 180 g`, `20092021`, `115160 hectares`) — **found independently by three
    agents. Bare number extraction would silently quote superseded figures.** No yield or sugar
    figure was quoted where the pair was ambiguous.
14. 🔴 **Twenty-one more rows need a physical label, bringing the floor total to thirty-nine.** The
    load-bearing ones: **Thierry Allemand's sulfites declaration** (the single most-asked question
    about $1,600–$2,600 bottles — **no producer source exists for any of 1998 / 1999 / 2001 / 2006,
    and third-party accounts disagree, so no claim was made in either direction**); **Henri Giraud
    row 4's "2022"** — whether it is a `MILLÉSIME` or an **MV-style base year**, which **alone
    decides `V-1` vs an ordinary vintage**; and **Alvina Pernot's `mis en bouteille` wording**, the
    only thing that can settle whether `AP WINES SAS` (**NAF `46.90Z` — non-specialised wholesale,
    not `01.21Z` viticulture**) is domaine or négoce. ⚠️ **Several settle multiple escalations per
    photo.**

## 3h. 🔴 Questions raised by Batch 12 (research cannot answer these)

1. 🔴🔴 **The label-null override is the highest-severity item this workstream has produced, and it
   is already measured.** 152 intake rows carry a `proposed_canonical_cuvee` where the parser
   recorded `_parts.label: null`; **147 are `cuvee_state: exact`**; `source_quality_flags` is empty
   on all of them. **For Bordeaux the proposed cuvée is the grand vin**, so the matcher is resolving
   a grand-vin/second-wine question — a price difference of roughly 4× to 10× — **on no evidence**.
   **This needs a decision, not a study**: suppress the proposal when `_parts.label` is null, or
   emit it at `candidate` with a flag. **Not executed.**
2. 🔴 **`C-6`'s premise split, now with the decisive evidence.** Batch 10 showed canonical structure
   and matcher input are two different defects. Batch 12 shows a **third layer**: parser detect →
   matcher override → store collapse. **Fixing canonical cannot fix these rows.** Accept, reject or
   restate `C-6` — and note the Palmer distinction, that `C-6` describes evidence carrying **no**
   information while this is evidence carrying **false** information.
3. 🔴 **Does "a canonical record that is not a bottle" get a class?** ~130 of 928 records (~14%) in
   three disjoint populations: **61** encoding the 1855 classification table, **37** whose
   provenance is a third-party critic's reference book (34 `Vintage Reference — Parker's Bordeaux`
   with `producer: "Bordeaux"` and real year values), **35** holding a region or appellation in
   `producer`. 🔴 **They carry `type: "Wine"`, `color`, `obp_format`, `glassware`, `serving_temp`
   and `food_pairings` — nothing in the schema distinguishes them from a sellable bottle**, and
   `haut-brion-1855` proves they are load-bearing (`_stub` source for four vintages with no record).
   Related to Batch 11's template-derived `allemand-chaillot-nv` and Batch 9's attribute-provenance
   shape. **Unnumbered. Does it absorb into `S-*`, or open a class?**
4. 🔴 **A new failure direction: typed field and prose contradict each other inside one record, and
   the prose is right.** `mouton-rothschild-1855` stores `aging: 24 months` while its own `obp_note`
   says ~20 months — matching the château's *"about twenty months"*. **This inverts Batch 10**, and
   means a "trust typed, drop prose" migration **would make this record worse**. Unnumbered.
5. 🔴 **Three statutory impossibilities sitting in canonical.** (a) `yquem-ygrec-2017.classification
   = "Sauternes — Dry White"` — AOC Sauternes requires **≥45 g/L** and the château's own Y sheet says
   **7 g/L**; the same record's JA and EN notes **describe two different wines**. (b)
   `haut-brion-1855.classification = "1855 **Médoc** Classification"` — Haut-Brion is in the Graves,
   falsified on three layers, and **the record contradicts its own `description`**. (c) The two
   WHITE Cos d'Estournel rows print `Saint-Estèphe`, which 🏛 the INAO CDC reserves *« aux vins
   tranquilles rouges »*. **All three are floor-facing.**
6. 🔴 **`P-9` proposed** — the classification string is a three-way split: the classifying body says
   `Premier Cru`, the producer's own pages say `Premier Grand Cru Classé` / `Premier grand cru
   classé`, canonical holds two further variants, **and the front label prints no classification at
   all** (verified on Mouton 1996, 2001, 2019). 🏛 The 1855 rank is **not in the AOC Pauillac CDC**;
   the legal basis is **Décret du 19 août 1921 art. 13 3° b)**, which permits **both** forms.
   **So no single string is "correct" — accept, reject or renumber.**
7. 🔴 **`D-2026-08-05-08` must be restated at SIRET granularity.** `Château Haut-Brion`,
   `La Mission Haut-Brion` and `La Tour Haut-Brion` are **three SIRETs of one SIREN**. Measured
   false-positive rates on naive substring matching: **Margaux 53 hits, precision 1/53**; Cos
   **80% false**; Giscours **87.5% false**, with a new variant — **the producer name is also a
   street name** (`ROUTE DE GISCOURS`), polluting the company register itself. 🔴 **And canonical's
   own id scheme carries the defect**: `latour-blagny-2019` and two siblings are **Louis Latour**,
   sharing the `latour-` prefix with Château Latour.
8. 🔴 **39 rows need a physical label, and unlike the previous 39 they all ask one question** —
   grand vin, second wine, or third — **which no online source can answer**, because the
   distinguishing string appears **0 times in 704 rows at both layers** for all 13 second-wine names.
   ✅ **Three shortcuts make it cheap**: Giscours by back label (zero Cabernet Franc in the grand vin,
   CF in every `La Sirène`, across all six vintages); **Latour Prooftag (2007+) and Palmer QR (2009+)
   resolve through the producer's own authentication**; Margaux 2015 is identifiable on sight
   (screen print on glass, no paper label).
9. ⚠️ **Two open producer-side contradictions, both preserved rather than resolved.** Haut-Brion's
   **own HTML and own fiche technique disagree on the 2018 and 2019 blends** — the two Cabernets are
   swapped, verified against PDF word coordinates so it is not an extraction artefact, and **the
   split is by medium, not language**. Cos d'Estournel's **two canonical records contradict each
   other** on hectares, blend and new oak.
10. ⚠️ **Two questions guests will ask that have no official answer, both on the must-not-say list.**
    Giscours' mid-2000s regulatory episode — 🏛 Légifrance returns **15 decisions, all unrelated** —
    recorded as a third-party claim with **a scripted floor response**. And Mouton's **1993 Balthus
    label**, where the château's own account is the **opposite of the folklore**: the BATF had
    approved it, and the Baroness withdrew the US bottles herself. **"Banned in America" contradicts
    the producer.**
11. ⚠️ **Légifrance is Cloudflare bot-gated (HTTP 403)**, so the **1973 Mouton promotion decree**
    could not be retrieved in the original. The fact is attested from 🏛 the INAO CDC text itself
    (*« … Latour en 1855 et Mouton-Rothschild en 1973 »*) and the château. **Gated, not evidence of
    absence; no bypass attempted.** Same for `crus-classes.com` (DNS-dead) — **the 1855 text itself
    was never obtained statutorily**, and the 1959 Graves classification could not be confirmed to
    cover red *and* white. **Do not state the 1959 red-and-white premise on the floor.**

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

2026-08-06 (updated after Batch 12 close-out — the Bordeaux block, 8 of 8)
