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
    # Two of the four Cos rows are printed in the WHITE section under a red-only
    # AOC (Saint-Estephe, decret 14 Nov 1936). They are counted because the dossier
    # documents both candidate whites; the appellation printed on those two rows is
    # legally impossible either way. Escalated, not fixed.
 "chateau-cos-d-estournel":["Château Cos d'Estournel"],
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
