import json, collections
OBP="/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json"
rows=json.load(open(OBP))
# explicit dossier -> OBP proposed_canonical_producer (or raw) mapping. Verified by hand.
M={
 "chateau-lafite-rothschild":["Château Lafite-Rothschild"],
 "domaine-de-la-romanee-conti":["Domaine de la Romanée-Conti"],
 "domaine-de-montille":["Domaine de Montille"],
 "domaine-denis-mortet":["Domaine Denis Mortet"],
 "domaine-dujac":["Domaine Dujac"],
 "domaine-faiveley":["Domaine Faiveley"],
 "domaine-jean-louis-chave":["Domaine Jean-Louis Chave"],
 "domaine-leflaive":["Domaine Leflaive"],
 "domaine-les-monts-fournois":["Domaine Les Monts Fournois"],
 "domaine-simon-bize-et-fils":["Domaine Simon Bize et Fils"],
 "doyard":["Doyard"],
 "drappier":["Drappier"],
 "dunoyer-de-segonzac":["Dunoyer de Segonzac"],
 "egly-ouriet":["Egly-Ouriet"],
 "frederic-savart":["Frédéric Savart"],
 "grgich-hills-estate":["Grgich Hills"],
 "jacques-frederic-mugnier":["Domaine J.-F. Mugnier"],
 "jerome-prevost":["Jérôme Prévost"],
 "laherte-freres":["Laherte Frères"],
 "larmandier-bernier":["Larmandier-Bernier"],
 "louis-latour":["Louis Latour"],
 "michel-gonet":["Michel Gonet"],
 "pascal-agrapart":["Pascal Agrapart"],
 "pierre-gimonnet-et-fils":["Pierre Gimonnet & Fils"],
 "pierre-peters":["Pierre Péters"],
 "pride-mountain-vineyards":["Pride Mountain"],
 # Batch 5
 "domaine-armand-rousseau":["Domaine Armand Rousseau"],
 "ganevat":["Ganevat"],
 "domaine-billaud-simon":["Domaine Billaud-Simon"],
 "joseph-drouhin":["Joseph Drouhin","Domaine Drouhin-Vaudon","Drouhin"],
 "olivier-bernstein":["Olivier Bernstein"],
 "pol-roger":["Pol Roger"],
    # Batch 6
 "domaine-bruno-clair":["Bruno Clair"],
 "domaine-eugenie":["Eugénie"],
 "domaine-des-comtes-lafon":["Domaine des Comtes Lafon"],
 "jean-claude-ramonet":["Jean-Claude Ramonet"],
 "pierre-yves-colin-morey":["Pierre-Yves Colin-Morey"],
 "caroline-morey":["Caroline Morey"],
    # Batch 7
 "domaine-laroche":["Domaine Laroche"],
 "pierre-girardin":["Pierre Girardin"],
 "mayacamas-vineyards":["Mayacamas Vineyards"],
 "dumol":["DuMOL"],
 "jacques-selosse":["Jacques Selosse"],
 "gosset":["Gosset"],
    # Batch 8
 "taittinger":["Taittinger"],
 "domaine-roulot":["Domaine Roulot"],
 "domaine-bachelet-monnot":["Domaine Bachelet-Monnot"],
 "michel-niellon":["Michel Niellon"],
 "domaine-de-l-arlot":["Domaine de L'Arlot"],
 "clos-de-la-coulee-de-serrant":["Clos de la Coulée de Serrant (Nicolas Joly)"],
    # Batch 9 (complete - 6 of 6; the final three were resumed from their
    # existing _sources caches after the earlier spend-limit stop).
 "harlan-estate":["Harlan Estate"],
 "clos-de-tart":["Clos de Tart"],
 "armand-heitz":["Armand Heitz"],
    # NOTE: 'Hundred Acre' counts all 5 OBP rows because the dossier documents all
    # five. But the dossier's finding is that 4 of those 5 are Fortunate Son /
    # Summer Dreams wines - sibling brands, one of which files under a separate
    # legal entity. Coverage here means "a sommelier can speak to the row without
    # lying", NOT "the row is correctly attributed in canonical". See the
    # brand-axis escalation in hundred-acre.md.
 "hundred-acre":["Hundred Acre"],
 "abreu-vineyards":["Abreu"],
 "bergstrom-wines":["Bergström"],
    # Batch 10.
    # 'Famille Mousse' counts all 5 OBP rows: the menu prints the same house two
    # ways ('Famille Musse' in BLANC DE NOIRS, 'Musse Famille' in SPECIAL CLUB)
    # and the dossier documents both. One house, proven by a single SIRET
    # carrying both names - see the P-2 evidence in famille-mousse.md.
 "famille-mousse":["Famille Mousse"],
 "louis-roederer":["Louis Roederer"],
 "billecart-salmon":["Billecart-Salmon"],
 "laurent-perrier":["Laurent-Perrier"],
 "chateau-montelena":["Chateau Montelena"],
    # 'Olivier Leflaive Freres' has no proposed_canonical_producer at all - it is
    # absent from canonical at the producer layer - so this key is the raw menu
    # string. Do NOT fold it into 'Domaine Leflaive': four separate SIRENs exist
    # and substring matching on 'Leflaive' is the exact D-2026-08-05-08 defect.
 "olivier-leflaive":["Olivier Leflaive Frères"],
    # Batch 11. All six are 4-bottle producers, selected in NEXT_ACTIONS.md as the
    # remainder of the 4-bottle tier. Four cleared the bar; Dauvissat (~64%) and
    # Thierry Allemand (~62%) are deliberately below it and marked
    # 'awaiting material from the team' - both publish nothing at all. They are
    # still counted: the dossier exists and a sommelier can speak from it without
    # saying anything false, which is what the bar measures (D-2026-08-04-02).
 "vilmart-et-cie":["Vilmart & Cie"],
 "henri-giraud":["Henri Giraud"],
 "alvina-pernot":["Alvina Pernot"],
 "domaine-anne-et-herve-sigaut":["Domaine Anne et Hervé Sigaut"],
    # 'Rene & Vincent Dauvissat' has no proposed_canonical_producer - the producer is
    # absent from canonical entirely (0 hits across all 928 records), so this key is
    # the raw menu string and key() falls back to source_producer_raw. Recorded as a
    # GAP, not a conflict - the Abreu precedent (D-2026-08-05-14).
 "rene-et-vincent-dauvissat":["René & Vincent Dauvissat"],
    # The menu misspells this producer 'Theirry Allemand' on all four rows (i/r
    # transposition); the key below is the proposed_canonical_producer, which the
    # matcher resolved correctly at producer_state='alias'.
 "thierry-allemand":["Thierry Allemand"],
    # Batch 12 - the Bordeaux block, run as one dedicated batch per NEXT_ACTIONS.md
    # section 2. All 47 rows print the APPELLATION where other sections print a
    # cuvee, so every key below is a producer key only; NONE of these rows can be
    # resolved to grand vin vs second wine from menu data. Measured across the
    # intake file: _parts.label is null on 69 of 69 Bordeaux rows, and a regex
    # sweep for every second/third-wine name in the block (Pavillon, Forts de,
    # Petit Mouton, Aile d, Clarence, Clarte, Bahans, Alter Ego, Sirene, Pagodes,
    # Goulee, Labory, Ygrec, Carruades) returns ZERO hits in all 704 rows at
    # either layer. Coverage here means "a sommelier can speak to the row without
    # lying" (D-2026-08-04-02), NOT "the row is attributed to a single wine".
    # 39 of the 47 rows carry a physical-label task for exactly that reason.
 "chateau-margaux":["Château Margaux"],
 "chateau-d-yquem":["Château d'Yquem"],
 "chateau-mouton-rothschild":["Château Mouton-Rothschild"],
    # 'Chateau Latour' must not be folded together with 'Louis Latour', which is a
    # separate Burgundy negociant with its own dossier - different SIREN, different
    # departement. Canonical shares the id prefix 'latour-' across both producers
    # (latour-blagny-2019 etc. are Louis Latour), which is the D-2026-08-05-08
    # substring defect sitting inside the id scheme rather than in a name field.
 "chateau-latour":["Château Latour"],
    # Haut-Brion qualifies the disambiguation rule the project relies on: Chateau
    # Haut-Brion, La Mission Haut-Brion and La Tour Haut-Brion are three SIRETs of
    # ONE SIREN (572179026), so SIREN separation fails for three of the five
    # Haut-Brion brands. Quintus and Les Carmes do separate cleanly by SIREN.
 "chateau-haut-brion":["Château Haut-Brion"],
 "chateau-giscours":["Château Giscours"],
 "chateau-palmer":["Château Palmer"],
    # Batch 13 (partial - stopped at 2 of 6 by a monthly spend limit, not by a
    # finding). Selection changed basis here: under D-2026-08-06-05 the binding
    # criterion is PRODUCER count (76/182), so bottle yield no longer drives the
    # pick. Both of these are 3-bottle producers.
    #
    # 'Krug' resolves producer_state=exact on all three rows but cuvee_state=
    # unresolved at confidence 0.0, because the matcher was handed a candidate set
    # of 2 canonical cuvees when canonical actually holds 13 Krug records -
    # INCLUDING krug-grande-cuvee-171/-172/-173 with the correct base years already
    # stored. That is the inverse of CDX-1 (which overrides on absent evidence);
    # filed as a Batch 13 addition in docs/state/CODEX_TASKS.md, not investigated.
    # Counted because the dossier lets a sommelier speak to all three rows without
    # saying anything false (D-2026-08-04-02).
 "krug":["Krug"],
    # The menu prints 'Ridge'; the matcher resolves it to 'Ridge Vineyards'. Only
    # 1 of the 3 rows is a CDX-15 'category word as cuvee name' instance
    # ('Proprietary Blend', row 3). 'Estate' is a real front-label designation Ridge
    # itself defines, and Ridge added 'VINEYARD' to the Geyserville front label at
    # the 2024 vintage specifically - so on that row the MENU is the accurate side.
    # Worked confirmation of NEXT_ACTIONS.md 3f-10.
 "ridge-vineyards":["Ridge Vineyards"],
    # Two of the four Cos rows are printed in the WHITE section under a red-only
    # AOC (Saint-Estephe, decret 14 Nov 1936). They are counted because the dossier
    # documents both candidate whites; the appellation printed on those two rows is
    # legally impossible either way. Escalated, not fixed.
 "chateau-cos-d-estournel":["Château Cos d'Estournel"],
    # Batch 14 (Phase 14). The first four below CLOSE Batch 13, which had stopped at
    # 2 of 6 on a monthly spend limit. Dom Perignon and Turley were written from
    # their existing _sources caches (28 MB / 2.4 MB); Dominus and Chappellet were
    # full research passes. The Batch 9 precedent held for the third time: a
    # spend-limit stop costs the WRITING pass, not the research.
    #
    # Dom Perignon: producer_state=exact on all 3 rows, cuvee_state=unresolved at
    # confidence 0.0. The intake evidence claims 'canonical キュヴェ 2 件'; canonical
    # actually holds 15 records, INCLUDING dom-perignon-2015 / -2013 / -p2-2003 -
    # the exactly-right target for every one of the three rows. Second instance of
    # the inverse-of-CDX-1 shape after Krug, and worse. Filed, not investigated.
    # Rows 1-2 print 'Brut', which is a statutory sugar term, not a cuvee name
    # (0 hits in 397 KB of house material AND 0 in the AOC Champagne CDC) - but the
    # menu is NOT called defective: the label may print it. Physical-label task.
 "dom-perignon":["Dom Pérignon"],
    # Turley is absent from canonical entirely - a GAP, not a conflict (CDX-23).
    # Stronger than a missing producer: 'Zinfandel' appears in ZERO grapes arrays
    # across all 928 records, so promoting Turley means adding a grape category.
    # No proposed_canonical_producer, so this key is the raw menu string. Do NOT
    # fold in the 5 substring hits on 'Turley' - they are all Helen Turley
    # (Marcassin / Aubert) or Ehren Jordan's biography. D-2026-08-05-08.
    # 'Estate' on row 1 is NOT a category word: it sits in the same quoted
    # vineyard-name slot as "HAYNE VINEYARD" and the front label prints
    # 'TURLEY ESTATE'. Second consecutive producer where CDX-15 did not replicate.
 "turley":["Turley"],
    # Dominus: the intake's 'canonical キュヴェ 1 件' claim was verified TRUE (unlike
    # Dom Perignon's). All 3 rows have _parts.label null and are NOT resolved: the
    # estate publishes that Napanook produces three wines (Dominus, Napanook,
    # Othello), and the official bottle shots show Dominus AND Napanook both
    # printing 'napa valley red wine' + 'estate bottled', same vineyard, same
    # appellation, same harvest dates. Nothing in the row separates them.
    # Counted under D-2026-08-04-02 ("a sommelier can speak to the row without
    # lying"), NOT because the row is attributed to a single wine. 3 physical-label
    # tasks. 'Proprietary Blend' IS a CDX-15 instance here, but for the inverse
    # reason from Ridge: all three vintages are >=75% CS (95/95/87), so a varietal
    # designation WOULD have been lawful under 27 CFR 4.23(b) - the estate simply
    # declines to name the grape. Ridge Geyserville (71/19/8/2) legally could not.
 "dominus-estate":["Dominus Estate"],
    # Chappellet is absent from canonical entirely (producer exact 0, whole-record
    # substring 0) - a GAP (CDX-23), and the matcher is NOT at fault. Raw menu key.
    # 'Pritchard Hill' is NOT an AVA: the string 'Pritchard' appears 0 times across
    # all 288 sections of 27 CFR Part 9, enumerated mechanically from the eCFR
    # title-27 structure API. It is simultaneously a place name and the cuvee-position
    # designation; the appellation of origin printed is NAPA VALLEY.
    # 'Signature' is the correct official product name (made permanent in 1984) but
    # the word is NOT printed on the front label - what is printed is Donn
    # Chappellet's gold autograph. Third route to the same 3f-10 lesson.
 "chappellet":["Chappellet"],
    # Batch 14 additions beyond the Batch 13 remainder. Selected on restaurant value
    # per the standing selection priority; both are 3-bottle producers, because the
    # 4-bottle tier is exhausted and the binding criterion is PRODUCER count.
    #
    # Figeac: absent from canonical - GAP (CDX-23). The 6 substring hits on 'Figeac'
    # are all producer='Bordeaux' vintage-guide reference records, i.e. the ~130
    # non-bottle class Batch 12 measured. Raw menu key ('Figeac', not the estate's
    # own 'Château-Figeac'). All 3 rows print the APPELLATION where other sections
    # print a cuvee (_parts.label null on 60 of 60 Bordeaux rows - section-wide),
    # so NONE can be separated from the second wine: Petit-Figeac (2018) and
    # La Grange Neuve de Figeac (2009) sit in the same AOC. Batch 12 replicated
    # exactly: 'Petit-Figeac' / 'Petit Figeac' / 'Grange Neuve' return 0 hits across
    # all 704 rows at both layers. Counted per D-2026-08-04-02; 3 physical-label
    # tasks. The 2022 'A' promotion CANNOT be backdated to any of these bottles -
    # arrete du 15 decembre 2022 art. 2 applies 'a compter de la recolte 2022'.
 "chateau-figeac":["Figeac"],
    # Promontory: highest-value producer remaining on the menu ($10,740 / 3 rows).
    # The wine's official name is 'Promontory' - string-identical to the producer,
    # i.e. the CDX-18 collision. Producer agreement alone therefore collapses the
    # candidate set to exactly one correct record, and the matcher STILL returned
    # cuvee null / unresolved / 0.0 on all three rows. This is the INVERSE of the
    # Batch 12 Bordeaux defect (which over-proposed the grand vin on label=null
    # rows); both failures originate in the same label=null handling.
    # The estate never says 'Cabernet Sauvignon' - 0 hits across 6 pages and 102 CMS
    # documents, more absolute than Abreu - but CDX-15 is left UNDECIDED because the
    # front label has not been read (3f-10). Corporate structure vs Harlan Estate is
    # NOT confirmed: CA SOS and CA ABC both 403-gated and promontory.wine carries no
    # legal notice at all. No inference substituted.
 "promontory":["Promontory"],
}
def key(r): return r.get('proposed_canonical_producer') or r.get('source_producer_raw')
c=collections.Counter(key(r) for r in rows)
covered=set()
tot=0
for slug,names in M.items():
    n=sum(c.get(x,0) for x in names)
    miss=[x for x in names if x not in c]
    if miss: print("!! unmatched name(s) for",slug,miss)
    tot+=n; covered.update(names)
print(f"dossiers={len(M)}  bottles_covered={tot}/{len(rows)}  = {tot/len(rows)*100:.1f}%")
rem=[(n,p) for p,n in c.items() if p not in covered]
rem.sort(reverse=True)
print(f"remaining producers={len(rem)} bottles={sum(n for n,_ in rem)}")
print("--- next candidates (non-Bordeaux) ---")
BDX={'Château Margaux',"Château d'Yquem",'Château Giscours','Château Haut-Brion','Château Latour','Château Mouton-Rothschild','Château Palmer',"Château Cos d'Estournel"}
k=0
for n,p in rem:
    if p in BDX: continue
    print(f"  {n:>3}  {p}"); k+=1
    if k>=26: break
