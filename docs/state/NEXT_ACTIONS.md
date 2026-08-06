# Next Actions

> **Official state document.** Written 2026-08-05 from verified repository state.
> Ordered by what unblocks the most work, not by effort.
> Companion to [`CURRENT_STATE.md`](CURRENT_STATE.md) and [`DECISIONS.md`](DECISIONS.md).

## Legend

**🔴 Blocked on Akio** — execution cannot proceed without a decision.
**🟡 Ready** — authorized, can start immediately.
**⚪ Deferred** — deliberately not started; do not pick up without instruction.

---

## 1. ✅ Batch 11 is closed — 6 of 6

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

2026-08-06 (updated after Batch 11 close-out — 6 of 6)
