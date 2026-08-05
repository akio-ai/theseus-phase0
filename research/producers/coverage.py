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
