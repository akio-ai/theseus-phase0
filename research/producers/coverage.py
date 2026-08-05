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
