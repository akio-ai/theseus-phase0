# Codex Engineering Tasks

> **Official state document.** Created 2026-08-06 under [`D-2026-08-06-06`](DECISIONS.md).
>
> This is the queue for **pipeline, matcher, mapping and canonical implementation defects**.
> Everything here was found by Producer Research and is **already recorded and already measured**
> in [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`NEXT_ACTIONS.md`](NEXT_ACTIONS.md).
>
> 🔴 **Research does not work these items and does not investigate them further.** When a batch
> encounters one naturally, it appends a line here and moves on. Nothing in this file blocks a
> dossier, and nothing in this file blocks the Research Layer from reaching completion under
> [`D-2026-08-06-05`](DECISIONS.md).
>
> **Nothing here is authorised to execute.** Canonical writes, `REGISTER.md` adjudication and
> schema migrations remain Akio / CTO calls. This file states *what is broken and where the
> evidence is*, not *what to change*.

## How to read a row

| Field | Meaning |
|---|---|
| **Layer** | `parser` · `matcher` · `store` · `canonical` · `schema` — where the defect lives |
| **Measured** | The number is counted, not estimated. The source of the count is named |
| **Evidence** | Section of `NEXT_ACTIONS.md` / `CURRENT_STATE.md` holding the worked example |
| **Blocked on** | What must be decided before code can be written |

Artifacts referenced below, by absolute path:

- Intake: `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` (704 rows)
- Store mapping: `research/out/t-01/mapping.json`, `research/store/t-01/shells.json`
- Canonical export: `migration/` (gitignored, 928 records)
- Coverage script: `research/producers/coverage.py`
- Integrity sweep: `research/canonical_conflicts/sweep_integrity.py`

---

## P0 — measured, floor-facing, decision-ready

### CDX-1 · The label-null cuvée override

**Layer** `matcher` · **Measured** 152 rows / 147 `exact` / 0 reviewer notes · **Evidence**
`NEXT_ACTIONS.md` §1, §3h-1

The parser correctly records `_parts.label: null` when no cuvée is printed — **292 of 704** rows,
**69 of 69** Bordeaux rows. The matcher then proposes a `proposed_canonical_cuvee` anyway on **152**
of them and marks **147** `cuvee_state: exact`. `source_quality_flags` is **empty on all 152**, so
nothing warns a reviewer.

🔴 **The proposed cuvée is the grand vin.** Giscours' `normalized_cuvee` is `Margaux`; its
`proposed_canonical_cuvee` is `Château Giscours`. The matcher is silently resolving
grand-vin-versus-second-wine — a 4× to 10× price difference — **on zero evidence**. Latour's third
wine is `Le Pauillac de Château Latour` and Margaux's is `Margaux du Château Margaux`: for those two
the cuvée name *is* the appellation.

**Shape of the fix** (decision, not study): suppress the proposal when `_parts.label` is null, **or**
emit it at `candidate` with an explicit flag. **Blocked on** which of the two.

### CDX-2 · `exact` is not a stronger identification than `unresolved`

**Layer** `matcher` · **Evidence** `NEXT_ACTIONS.md` §1, §3g-6

Consumers of `match_state` are reading it as a confidence signal and it is not one.

- All six Haut-Brion rows are `producer_state: exact` **and** `cuvee_state: exact`; only
  `vintage_state` differs. The two rows at `confidence 1.0` matched their cuvée on the **same false
  token-set claim** as the four `unresolved` ones.
- Alvina Pernot: four **contentless** canonical records (8 fields absent *as keys*) against a
  $360 / $640 / $720 / $720 lineup — every row `exact` at `confidence 1.0`.
- Henri Giraud row 1: `exact` at `1.0` while the menu says `Brut Nature`, canonical says `Brut`, and
  the house says neither. **The dosage axis is not compared at all.**
- Vilmart inverts it: the only row intake marked resolved is the only row that could not be
  confirmed officially.
- `S-2` quote marks are **invisible to matching** — evidence strings read
  `'La Garenne' ≡ '"La Garenne"'` at `confidence 1.0`.

**`match_state` measures canonical agreement, not existence.** This needs stating wherever match
states are consumed, and probably needs a separate field.

### CDX-3 · The store layer collapses rows and discards price and vintage

**Layer** `store` · **Measured** 141 of 1047 shells are multi-line · **Evidence** `NEXT_ACTIONS.md`
§1

Rows are keyed without vintage, so they merge: Haut-Brion **$14,940 in one shell**; d'Yquem **six
vintages and three prices in one**; Cos d'Estournel **merges a WHITE $680 and a RED $900 and
discards the $900**.

This is the **fifth-plus** instance of the intake ↔ store divergence, and the first where the
discarded axis had already been flagged upstream by the parser.

### CDX-4 · The intake file and the store mapping disagree on what is resolved

**Layer** `store` / `mapping` · **Confirmed 5×** — Bachelet-Monnot, Clos de Tart, Armand Heitz,
Hundred Acre, and the Batch 12 block · **Evidence** `NEXT_ACTIONS.md` §3d-4, `CURRENT_STATE.md`
Batch 8 / Batch 9 notes

`obp_intake_normalized_20260804.json` reports cuvée-level `exact` matches that
`research/out/t-01/mapping.json` does not carry — rows fall to a `research_shell` **despite their
canonical records existing**. Hundred Acre is worse in kind: in `research/store/t-01/shells.json`
the two Summer Dreams rows are **parse-broken** (`producer_or_brand` swallowed the whole line,
`canonical` is `{}`), so on disk those rows have **no producer at all** where intake reports
`producer_state: exact`.

**Three independent agents flagged this unprompted, two of them pushing back on a briefing premise.**
Until adjudicated, no "resolved" count may be quoted without naming its artifact. Coverage figures
in `CURRENT_STATE.md` come from the intake file via `coverage.py` and are unaffected.

### CDX-5 · Canonical stored values contradict producer-official sources — 13 of 14 producers checked

**Layer** `canonical` · **Failure rate on producers actually checked: 100% (Batch 10) / 13 of 14
(Batch 11)** · **Evidence** `NEXT_ACTIONS.md` Shape C, §3f-1

Not confined to prose. It reaches **typed structured fields** — `grapes`, `dosage`, `aging`,
`founded_year`, `subregion`. Worked examples:

- **Billecart-Salmon — 19 contradicted items across 4 records.** Inverted grape splits; dosages
  `5 / 6 / 7 g/L` against official `3.9 / 3.8 / Extra Brut`; `founded 1816` against **1818**; an
  **invented parcel name** ("Mont Blanche"); an "1830s rosé tradition" against the house's **1970s**.
- **Louis Roederer — one `house_style` string duplicated verbatim across all 16 records**, asserting
  a **Demeter certification the house does not hold** and a **`saignée` rosé method it explicitly
  does not use**, plus 96–98 point scores that exist in no official source.
- **Taittinger `founded_year = 1734`** has no basis on the official site; the house's own origin is
  **1932**. Proposed as `P-8`.
- **Three statutory impossibilities**: `yquem-ygrec-2017` classified AOC Sauternes (requires
  ≥45 g/L; the château's own sheet says 7 g/L); `haut-brion-1855` classified "1855 **Médoc**"
  (Haut-Brion is in the Graves, and the record contradicts its own `description`); two WHITE Cos
  d'Estournel rows under `Saint-Estèphe`, which the INAO CDC reserves for red.
- **Three failure modes, all three inside one producer** (Thierry Allemand): *contradicted*,
  *unsourced*, and **absent as key**.

⚠️ **A sweep must count empty records as well as wrong ones**, and must not assume typed beats prose:
`mouton-rothschild-1855` stores `aging: 24 months` while its own `obp_note` says ~20 — **the prose is
the correct one**. A "trust typed, drop prose" migration would make that record worse.

**Blocked on** authorisation to sweep. `sweep_integrity.py` is the precedent for doing it read-only.

---

## P1 — measured, structural

### CDX-6 · ~130 of 928 canonical records are not bottles, and nothing in the schema says so

**Layer** `schema` / `canonical` · **Measured** ~130 (~14%), three disjoint populations ·
**Evidence** `NEXT_ACTIONS.md` §3h-3

**61** encode the 1855 classification table (5/14/14/10/18 — the exact official structure); **37**
have a third-party critic's reference book as provenance (34 are `Vintage Reference — Parker's
Bordeaux` with `producer: "Bordeaux"`); **35** hold a region or appellation in the `producer` field.

🔴 They carry `type: "Wine"`, `color`, `obp_format`, `glassware`, `serving_temp` and `food_pairings`
— **schema-indistinguishable from a sellable bottle** — and they are **load-bearing**:
`haut-brion-1855` is a `vintage: "—"` shell serving as the `_stub` that supplies cuvée facts to four
vintages with no record of their own. Related: the template-derived `allemand-chaillot-nv`, which
carries `dosage: "N/A — Still Wine"` — a Champagne field on a Rhône record.

### CDX-7 · The vintage field carries three different meanings

**Layer** `schema` · **Measured** `'—'` 328 across 182 producers / `'NV'` 88 / base-year-in-string 24
in **five mutually incompatible notations** · **Evidence** `NEXT_ACTIONS.md` §3d-2, §3g-1

🔴 **And the `'NV'` bucket is now known to be mixed.** `allemand-chaillot-nv` is a **Cornas**; the
INAO CDC reserves the appellation for *vins tranquilles rouges*. A non-vintage Cornas cannot exist,
so the 88 are not a homogeneous legitimate class and the three-way partition must be **re-cut before
any migration is designed**.

⚠️ **A single "fix the vintage field" pass would destroy the Krug base-year data.**

### CDX-8 · `V-1` has no surrogate key to migrate to

**Layer** `schema` · **Evidence** `NEXT_ACTIONS.md` §3f-3, §3f-5

Grand Siècle's three base vintages **overlap between itérations** (2008/2007 in both Nº25 and Nº26;
2012 in both Nº26 and Nº27), so `base_year` does not work as a surrogate key — **there is no correct
value for the `vintage` field**, and a migration has nothing to write. Worse, adding Nº27 under the
present schema makes `(cuvée, vintage="NV")` **non-unique inside canonical**: the schema blocks its
own gap fill.

Format is **double-encoded** in `name` *and* in `obp_format`; four magnum records exist, three with
no standard-bottle sibling. Grand Siècle `Les Réserves` releases the same itération twice as
undisgorged magnums, so identity needs **itération × format × disgorgement state** — three keys.

⚠️ **Do not write a `Grande Cuvée No. 26` → `Itération Nº26` normalisation rule.** `Grande Cuvée` is
**Krug's** cuvée name, the producer at the centre of `V-1`.

### CDX-9 · Substring matching on a producer name — `D-2026-08-05-08` needs restating at SIRET granularity

**Layer** `matcher` / `canonical ids` · **Evidence** `NEXT_ACTIONS.md` §3f-8, §3g-8, §3h-7

Measured false-positive rates on naive substring matching: **Margaux 53 hits, precision 1/53**; Cos
**80% false**; Giscours **87.5% false** — and for Giscours the producer name is also a **street name**
(`ROUTE DE GISCOURS`), which pollutes the French company register itself. Of 16 canonical records
matching `leflaive`, **7 are Domaine Leflaive, 0 are Olivier Leflaive, and 9 match only because
"Leflaive" appears in *other producers'* prose.** This defect corrupted the coverage figure by 11
bottles before `coverage.py` was written.

🔴 **SIREN separation is not sufficient.** `Château Haut-Brion`, `La Mission Haut-Brion` and
`La Tour Haut-Brion` are **three SIRETs of one SIREN** (`572179026`). Quintus and Les Carmes do
separate cleanly by SIREN. **Restate the rule at SIRET granularity.**

🔴 **Canonical's own id scheme carries the defect**: `latour-blagny-2019` and two siblings are
**Louis Latour**, sharing the `latour-` prefix with Château Latour.

🔴 **Only an exact-SIRET negative counts as a proved negative** — Agence Bio's search API returns
`LALLEMAND` entries for a `nom=allemand` query.

### CDX-10 · Name normalisation must be aliases, not rules

**Layer** `matcher` · **Evidence** `NEXT_ACTIONS.md` §3g-3, §3d-7, §3d-8

Blanket article/accent normalisation is **refuted by a worked counter-example, not merely cautioned
against**: Dauvissat's `La Forest` occurs 0 times in either INAO Chablis cahier, and `La Forêt` /
`Sur la Forêt` genuinely exist under a **different umbrella** (`Vau Ligneau`) — so naive
normalisation lands it on the **wrong vineyard**. `Les Clos` is the only Chablis Grand Cru climat
carrying an article and **must not be stripped**. INAO writes `Les Bouchères` **with** an article and
`Perrières` **without** one, inside the same appellation.

Cases needing an **explicit alias** each: `Clos de Roi`/`Clos du Roi` (de Montille, 4 rows),
`Le Montrachet Grand Cru`/`Montrachet Grand Cru`, `Chassagne-Montrachet Blanc`/`Chassagne-Montrachet`,
`Célébris`/`Celebris` (accent split, 2 rows), `Les Champs Gains`/`Les Champs gain`/`Le Champgains`
(a **plural difference no rule bridges**), `Grande Réserve`/`Grand Réserve` (Gosset).

**This closes §3c-3 and §3b-2 as "rule" proposals.**

### CDX-11 · The matcher never reads the menu section heading

**Layer** `matcher` · **Evidence** `NEXT_ACTIONS.md` §3f-2, `CURRENT_STATE.md` Batch 8 / 10 notes

The intake `evidence` string is **byte-identical across all four Roederer rows including the ROSÉ
one**. Canonical is *not* missing the colour axis there — it carries four Cristal cuvées and
`cristal-rose-2014` **exists and is factually correct**. Billecart-Salmon is a second counter-example.
Taittinger row 5 is printed in **ROSÉ** and was proposed against the **Blanc de Blancs** record.

🔴 **Canonical structure and matcher input are two different defects. Fixing canonical alone does not
fix the row.** This is why `C-6` as written needs splitting.

### CDX-12 · Embedded quote marks in cuvée names — `S-2`

**Layer** `canonical` · **Measured 175 records, 18.9% of canonical** (prior estimate: 9) ·
**Evidence** `NEXT_ACTIONS.md` §3d-2

Measurement is **done** (`sweep_integrity.py`); what remains is a fix. ⚠️ The sweep separates **78
records whose names contain a legitimate French elision** (`L'Esprit`, `Réserve de l'Abbaye`) —
**these are correct and must not be swept up.** Handling is **non-deterministic today**: within one
producer (Thierry Allemand), Reynard propagates the quotes into `proposed_canonical_cuvee` while
Chaillot normalises them away.

### Batch 13 additions

- 🔴 **The matcher's per-producer candidate set is smaller than canonical.** All three Krug rows
  (`obp-beverage-2026-08:6576a45bb2` / `7ea95401c0` / `b82ab723da`) carry the intake evidence
  `'Krug' の canonical キュヴェ 2 件に一致無し`, yet `migration/out/export/db_wine_canonical.json`
  holds **13 records with `producer == "Krug"`**, including `krug-grande-cuvee-171`, `-172` and
  `-173` — **exact counterparts of all three rows, with the correct base years already stored**.
  The 13 records collapse to exactly **2 cuvée families** (`Grande Cuvée` ×12, `Rosé` ×1), so the
  "2" is plausibly a family count reaching the matcher where a record count was needed. **Not
  investigated further** (`D-2026-08-06-06`). Evidence: `research/producers/krug.md` §Canonical
  Conflict ①.

- 🔴 **`CDX-20` now has a case where the over-split string is a real product name *and* collides
  with a second real product in the same vintage.** Ridge rows 1 and 2
  (`obp-beverage-2026-08:43436ec6c8` / `f70b019945`) are decomposed into
  `appellation='santa cruz mountains'` + `varietal='cabernet sauvignon'`. Ridge ships **two**
  distinct 2023 wines: `Estate Cabernet Sauvignon` (estate-farmed, Monte Bello, `Organically
  Grown`) and `Santa Cruz Mountains Cabernet Sauvignon` (**revived in 2023 for purchased fruit**,
  no organic claim). The only token separating them is `Estate`, which the split discards into
  `_parts.label`. **Not investigated further** (`D-2026-08-06-06`). Evidence:
  `research/producers/ridge-vineyards.md` §Important Cuvées 行 1.

- ⚠️ **`_parts.varietal` is a typed field but accepts non-varieties.** Ridge row 3
  (`obp-beverage-2026-08:717413779c`) stores `varietal = "proprietary blend"`. The producer's own
  label-grammar page uses `Proprietary Name` and `field blend`; `Proprietary Blend` appears on
  neither the front label (`71% ZINFANDEL, 19% CARIGNANE, 8% PETITE SIRAH, 2% ALICANTE BOUSCHET`)
  nor anywhere on `ridgewine.com`. Related to `CDX-15` but the harm is the typed field, not the
  cuvée string. **Not investigated further** (`D-2026-08-06-06`). Evidence:
  `research/producers/ridge-vineyards.md` §Important Cuvées 行 3.

### Batch 14 additions

> Recorded once, per `D-2026-08-06-06` §2–3. **None was investigated beyond the dossier that met
> it**, and no repository-wide sweep was run to produce this section.

- 🔴🔴 **The `label = null` path fails in *both* directions, and that reframes the Batch 12 finding.**
  Batch 12 measured **over-proposing**: 152 rows with `_parts.label = null` were given a cuvée
  anyway and **147 marked `exact`**, always the grand vin. **Promontory is the inverse.** Canonical
  holds one record whose `producer` **and** `name` are both the string `Promontory` — so producer
  agreement alone reduces the candidate set to **exactly one, and it is correct** — yet all three
  rows (`obp-beverage-2026-08:` `…`, 2021 / 2020 / 2017) return `proposed_canonical_cuvee: null`,
  `cuvee_state: unresolved`, `confidence 0.0`. 🔴 **A fix that only suppresses over-proposing will
  leave this half untouched. Both behaviours originate in the same `label = null` handling and must
  be specified together.** Evidence: `research/producers/promontory.md` §Canonical Conflict.

- 🔴 **A third face of the same defect: parser output is discarded and a *style token* is used as a
  cuvée query.** For Dom Pérignon rows 1–2 (`5cbde63539` / `5a8f29e841`) `_parts` correctly yields
  `label: null` and `style: "brut"`, yet `normalized_cuvee` becomes `"Brut"` and the matcher then
  searches canonical **cuvée** names for it. `Brut` is a statutory sugar term: **0 occurrences**
  across 397 KB of the house's own material **and 0 in the AOC Champagne cahier des charges**.
  Evidence: `research/producers/dom-perignon.md` §Important Cuvées.

- 🔴 **The inverse-of-`CDX-1` shape recurs, worse than at Krug — and it is *not* uniform.**
  Dom Pérignon's three rows carry the evidence `'Dom Pérignon' の canonical キュヴェ 2 件に一致無し`;
  canonical holds **15** records, including `dom-perignon-2015`, `dom-perignon-2013` and
  `dom-perignon-p2-2003` — **the exactly-right target for every one of the three rows**, all at
  `confidence 0.0`. ⚠️ **This must not be handled as a gap: the records exist, and creating them
  would duplicate.** ✅ **Counter-case in the same batch:** Dominus' `canonical キュヴェ 1 件` claim
  was verified **true** (exactly one record, 928 scanned). **The evidence string is unreliable per
  producer, not uniformly wrong — any fix must re-derive the count, not distrust the field.**
  Evidence: `research/producers/dom-perignon.md` / `dominus-estate.md` §Canonical Conflict.

- 🔴 **A canonical vocabulary gap one level above a missing producer: `Zinfandel` appears in ZERO
  `grapes` arrays across all 928 records.** Turley cannot be promoted without adding a **grape
  category**. Structurally identical to `CDX-17` (no Oregon in `region`), and the same question
  will recur for every producer outside the current varietal vocabulary. Evidence:
  `research/producers/turley.md` §Canonical Conflict.

- 🔴 **`_parts.appellation` conflates two different things — the label's appellation of origin and
  the vineyard's location / sub-AVA.** Turley rows 1–2 print `Saint Helena`, but the producer's own
  tech sheets record `AVA: Napa Valley` / `Sub-AVA: Saint Helena`, the JSON-LD `Appellation` field
  says `Napa Valley`, and the front label's first line reads `NAPA VALLEY`. Same class as the
  Hundred Acre `Ark` finding (`CDX-16`) **but on the OBP side rather than canonical's.** Evidence:
  `research/producers/turley.md` §Important Cuvées.

- ⚠️ **The Bordeaux `label = null` condition is section-wide structure, not row defects.**
  `_parts.label` is `null` on **60 of 60** rows in `FRANCE | RED > BORDEAUX`. Related: the parser
  writes `_parts.rank: "Grand Cru"` by slicing those words out of the **appellation name**
  `Saint-Émilion Grand Cru` — the 5 Bordeaux rows carrying a `rank` are exactly the 5 rows printing
  that appellation (Figeac ×3, Cheval Blanc ×2). A same-row contradiction follows:
  `cuvee_state: "unresolved"` + `_parts.label: null` while `normalized_cuvee` holds an
  **appellation**. Evidence: `research/producers/chateau-figeac.md` §Canonical Conflict.

- ⚠️ **Ingesting producer-published pages is not safe, and two distinct failure modes were measured.**
  (1) **Wrong-vintage prose on the producer's own product pages** — Chappellet's 2022 Signature page
  carries a growing-season narrative describing **2020**, and its 2022 Pritchard Hill page describes
  **2019** and quotes a 2019 review. **A pipeline scraping product pages instead of the per-wine
  notes PDFs will ingest wrong-vintage facts as truth.** (2) **Duplicated figures across different
  wines inside the producer's own technical sheets** — Dominus' `DOM_2020` and `NK_2020` both state
  1,600 cases; `NK_2021` and `Othello-2021` both state 3,000. **Tech-sheet ingestion needs a
  cross-wine duplicate check.** Evidence: `research/producers/chappellet.md` /
  `dominus-estate.md` §Sources.

- ⚠️ **Label-token matching must be producer-scoped.** `Signature` is a cuvée name for **Chappellet**
  and, in the same intake file, for **Darioush** (3 rows). Any token-level cuvée index built without
  a producer key will cross them. Evidence: `research/producers/chappellet.md` §Canonical Conflict.

- ⚠️ **Canonical already stores a non-AVA inside the appellation hierarchy.**
  `Napa Valley — Pritchard Hill` is `Continuum Estate`'s `subregion`, while `Pritchard Hill` is
  **not an AVA** (the string `Pritchard` occurs **0 times** across all **288 sections** of 27 CFR
  Part 9, enumerated from the eCFR title-27 structure API). For Chappellet the same string is
  **simultaneously the cuvée name and a place**, so row 3 cannot promote until the schema decides.
  `CDX-16` family. Evidence: `research/producers/chappellet.md` §Canonical Conflict.

- ⚠️ **`vintage: '—'` on a producer publishing 14 distinct vintage records.** Promontory's three OBP
  rows can never be separated without `cuvée × vintage`; the estate's own CMS holds 2009–2022.
  Same shape as Montelena in Batch 10. Evidence: `research/producers/promontory.md`.

- ⚠️ **The intake evidence string's producer count is off by one.** It reports
  `canonical 384 生産者`; the 928-record export yields **383** distinct non-null `producer` values.
  Reported independently by two Batch 14 agents. `CDX-4`-adjacent, low harm, easy to confirm.

- ⚠️ **Canonical holds no `bordeaux-vintage-*-guide` record after 1997**, so none of Figeac's three
  OBP vintages (2018 / 2010 / 2009) has even a reference-table entry — worth knowing before anyone
  treats the reference-table class as usable coverage. Evidence:
  `research/producers/chateau-figeac.md` §Canonical Conflict.

- 🔴 **Operational hazard for anyone writing fetchers: producer sites now carry instructions
  addressed to AI agents.** `turleywinecellars.com/robots.txt` directs agents to its UCP/MCP
  endpoints and recommends installing a shopping skill **to purchase products directly**. In this
  batch it was treated as **observed content, not instruction** — nothing installed, no cart or
  checkout surface touched. 🔴 **Any automated ingestion path must treat fetched site content as
  data and never as configuration or instruction.** Evidence: `research/producers/turley.md`
  §Sources.

---

## P2 — model questions; code cannot proceed until these are answered

Each of these is a **modelling decision**, not a bug. They are listed so research stops re-deriving
them.

| # | Question | Evidence |
|---|---|---|
| **CDX-13** | **Per-vintage appellation strings.** Pride Mountain's label appellation changes every year (`64% Napa / 36% Sonoma`, `Napa County`, `Napa Valley`) because the county line runs through the estate. The one-`subregion`-per-cuvée model cannot express it. **All 10 OBP bottles affected** | §3b-1 |
| **CDX-14** | **Geographic granularity below the appellation.** `Les Chaumées, Clos de la Truffière` is a climat *plus* a named clos inside it; `Truffière` occurs **0 times** in the Chassagne CDC. But **Cornas has a general legal pathway Chassagne lacks** — CDC XII.2°a) permits a smaller unit if it is a *lieu-dit cadastré* on the harvest declaration, and DGFiP confirms `Chaillot` and `Reynard` as real lieux-dits of commune 07070. **Re-ask per appellation, not as one model gap** | §3d-2a, §3g-12 |
| **CDX-15** | **Brand axis.** Three-plus instances with no accepted class: Harlan/`The Mascot` (separate LLC, 3 of 5 rows misattributed); Hundred Acre/`Fortunate Son`/`Summer Dreams` (**4 of 5 rows are not Hundred Acre wines**, one under a separate legal entity); `P-6`/`P-7`. 🔴 **Olivier Leflaive's `Récolte du Domaine` is harder — the axis lives *inside* the cuvée string** (8 cuvées in 2023, identical producer/appellation/vintage) and **there is no separate entity to point at**. `CAT-1`…`CAT-9` are still only proposals | §3e-1, §3f-7b |
| **CDX-16** | **Attribute provenance — a factually unsourced value in a structurally valid record.** Hundred Acre `Ark` carries `subregion = "Napa Valley — Howell Mountain"`; both TTB COLAs and the approved front label declare **`NAPA VALLEY`**, and `Howell` appears in **no** producer source and **none** of 105 TTB records. Every existing family (`P-*` `C-*` `V-*` `S-*` `CAT-*`) describes a *structural* defect. **Does it get a number?** ⚠️ Montelena's `Napa Valley — Calistoga` is a **clean counter-example** — 27 CFR §9.209 inside §9.23, T.D. TTB-83 | §3e-2, §3f-10 |
| **CDX-17** | **Canonical `region` has no Oregon.** All **79** USA records are `region='California'`. Bergström cannot be promoted without a vocabulary decision, and every future Pacific-Northwest producer hits the same wall | §3e-3 |
| **CDX-18** | **Producer/cuvée same-string collision.** `cuvee:clos-de-tart-clos-de-tart`. Demonstrable harm: `La Forge de Tart` scores **0.7143** against `Clos de Tart` on the tokens `de` + `Tart` — **both producer-name tokens bleeding into cuvée matching**. `Clos des Lambrays`, `Château Latour` are the same shape. **A canonical-wide inventory is needed before a number is assigned** | Batch 9 notes |
| **CDX-19** | **Superseded name during a rename.** Billecart's `Brut Réserve`→`Le Réserve` and `Brut Rosé`→`Le Rosé` are in progress; the old name survives in URL slugs, `<title>` tags and a 2023 TTB approval. **Canonical has no way to hold both** | §3f-7a |
| **CDX-20** | **Over-splitting a product name that legitimately contains its appellation.** The matcher decomposes `Napa Valley Chardonnay` into appellation + varietal with `label=null` — **the inverse of `C-4`**. Same inverse shape: `"Chaillot" Cornas` | §3f-7c, §3g-2 |
| **CDX-21** | **A cross-producer collective designation inside a cuvée name.** Canonical writes `Special Club` for Moussé, but `club`/`spécial`/`special` occur **0 times** in 69,221 characters of the producer's site and `mousse` occurs **0 times** in the Club Trésors de Champagne roster of 25 members. **Does a collective designation belong in a name string at all?** | §3f-7d |
| **CDX-22** | **"Structurally valid but contentless" — does it get a class?** All four Alvina Pernot records lack 8 fields **as keys**, so verification was unexecutable on 10 of 10 — while every row reads `exact` at `confidence 1.0`. Distinct from a gap and from a wrong value | §3g-5 |
| **CDX-23** | **Gaps stay out of the register — confirm, and keep "unreachable" separate.** Abreu and Bergström are absent from canonical entirely (Abreu: 0 hits for the producer **and** all six vineyard names). But Laurent-Perrier row 2 **looks** like a gap and is not — `laurent-perrier-grand-siecle-26` **exists and is unreachable**, spelled three ways. **Treating it as a gap would have created a duplicate.** The distinction is load-bearing | §3e-4, §3f-9 |
| **CDX-24** | **Producer identity must never be relaxed in matching.** `arlaud-les-sentiers-2021` is the **same climat under a different producer** as Sigaut row 4; `raveneau-montee-de-tonnerre-2021` is the **same climat and vintage** as Dauvissat row 3. A producer-relaxing matcher binds both to the wrong estate | §3g-7 |
| **CDX-25** | **Classification strings are a three-way split with no correct value — `P-9`.** The classifying body says `Premier Cru`; the producers say `Premier Grand Cru Classé` / `Premier grand cru classé`; canonical holds two further variants; **the front label prints no classification at all** (verified on Mouton 1996, 2001, 2019). The 1855 rank is **not** in the AOC Pauillac CDC — the basis is **Décret du 19 août 1921 art. 13 3° b)**, which permits **both** forms. **So no single string is "correct."** Related drift inside one cuvée: `folatieres-2022` says `Premier Cru`, `folatieres-2023` says `1er Cru` | §3h-6, §3d-2c |

---

## Standing cautions for whoever writes this code

1. 🔴 **The menu is not reliably the defective side.** Four counter-examples: Billecart's `Le Réserve`
   **is** the house's current name; Montelena's rows reproduce the label **more faithfully than
   `montelena.com` does**; INAO and BIVB print `La Pièce sous le Bois` with lowercase *sous* and OBP
   matches them exactly while **canonical alone** capitalises it; Montelena's `Calistoga` subregion is
   label-backed. There is also one clean menu defect (OBP misspells `Theirry Allemand` on four rows).
   **Pattern existence is not evidence that a given row is another instance.**
2. ⚠️ **The vintage field, the `'NV'` bucket, and the label-null rows are three separate migrations.**
   Any single pass over "the vintage field" destroys data in at least one of them.
3. ⚠️ **`_sources/` is gitignored and stays that way** (`D-2026-08-05-02`). Provenance lives as URLs
   in each dossier's `## Sources`.
4. ⚠️ **78 rows await a physical label.** They do **not** block Research Layer completion
   (`D-2026-08-06-05` criterion 2 asks for a *producer*), and they must not be auto-resolved.
   39 of them ask a single question — grand vin, second wine, or third — and the distinguishing
   string appears **0 times in 704 rows at both layers** for all 13 second-wine names.

## Last Updated

2026-08-06 — **Batch 14 additions appended.** Created under `D-2026-08-06-06`, populated from findings already recorded through
Batch 12. **No new investigation was performed to write this file.**
