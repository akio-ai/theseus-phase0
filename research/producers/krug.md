# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical に `producer == "Krug"` のレコードは 13 件ある**（Grande Cuvée 12 件＋Rosé 1 件）。
> 🔴 **OBP 3 行に対応する `krug-grande-cuvee-171` / `-172` / `-173` は canonical に**実在し、base year も正しい**。
> 🔴 **にもかかわらず intake の evidence は「`'Krug' の canonical キュヴェ 2 件に一致無し`」と書く。** → §Canonical Conflict ①・`CODEX_TASKS.md` Batch 13 additions
> 本書は昇格前の研究記録であり、**canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト `www.krug.com`（FR 原本）／公式 Champagne Notes PDF**（一次資料・producer-authored）
> `🏛` **公的登録／法令**（recherche-entreprises.api.gouv.fr / opendata.agencebio.org / INAO CDC「CHAMPAGNE」/ geo.api.gouv.fr）
> `📄` 造り手の旧ページを Internet Archive から復元したもの（本調査では **未使用**）
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出 ／ `❓` 未解決
> `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 (JST) ／ 一次資料: **`https://www.krug.com/fr/`（FR 原本）**
> 走査元: **`robots.txt` → `sitemap.xml`（2 ページ・URL 2,827 件、うち `/fr/` 313 件）→ FR 側の非 Ambassade ページ 29 件から中核 13 ページを全文取得**
> 併用: ✅ **公式 `Champagne Notes` PDF 1 点（`Champagne-Notes_Krug-Grande-Cuvee-172eme-Edition.pdf`。`%PDF` 実体・1 頁・155,412 B）**
> 併用: 🏛 **AOC「CHAMPAGNE」CDC（`homologué par l'arrêté du 30 novembre 2022, publié au JORF du 10 décembre 2022`。BO du MASA 2022-12-15、26 頁）**
> 併用: 🏛 **企業登録（SIREN 完全一致）・Agence Bio（SIRET 完全一致で陽性 1 件・陰性 1 件）・geo.api.gouv.fr（コミューン 4 件）**
>
> ---
>
> 🔴 **① 本ドシエの最重要事実 —— Édition 番号の意味は、造り手が 2 か所で明文化している。**
> ✅ **公式 172 Champagne Notes（EN、producer-authored）: 「`The Édition number identifies a specific creation of Krug Grande Cuvée. It corresponds to the number of years in the House of Krug the founder's dream has been re-created.`」**
> ✅ **公式 `/fr/notre-histoire`（FR）: 「`À partir de 2016`, la Maison Krug attribue un numéro d'Édition à chaque nouvelle création de Krug Grande Cuvée et Krug Rosé. Ce numéro, `visible sur l'étiquette`, permet d'identifier plus facilement les différentes créations de ces champagnes. `Il indique combien de fois, dans l'histoire de la Maison, Krug Grande Cuvée ou Krug Rosé ont été recréés.`」**
> 🔴 **すなわち Édition 番号は「創業以来、その champagne が何回目の再創造か」を数える**通し番号**であって、ヴィンテージでも熟成年数でもロット番号でもない。**
> ✅ **「`Jusqu'au milieu des années 2010, les bouteilles quittant nos caves à Reims ne portaient pas de numéro d'Édition`, et les bouteilles plus anciennes peuvent ne pas avoir de Krug iD.」**
>
> 🔴 **② ベースとなる収穫年も、造り手が 1 本ずつ明記している。OBP 3 行はすべて確定した。**
> ✅ **171ème = `Créée autour des vendanges de 2015` ／ 172ème = `Créée autour des vendanges de 2016` ／ 173ème = `Composée autour des vendanges de 2017`。**
> 🔍 **canonical の `NV · based on 2015` / `NV · based on 2016` / `NV · based on 2017` は、**この 3 行に限れば公式と一致する**。** → §Canonical Conflict ②
> 🔴 **ただし `vintage` フィールドの多義性そのものは `CDX-7` / `CDX-8` の問題であり、本ドシエは解決しない（`D-2026-08-06-06`）。**
>
> 🔴 **③ 造り手自身の識別子は `Krug iD`。6 桁で、貼られている場所も公式が書いている。**
> ✅ **「`En 2011`, la Maison Krug introduit le Krug iD, `un code à six chiffres apposé sur la contre-étiquette de chaque bouteille Krug`.」**
> ✅ **EN: 「`Enter your bottle's six-digit code` to discover the story of your bottle …」**
> 🔴 **すなわち Krug は「Édition 番号（表ラベル）」と「Krug iD（裏ラベル 6 桁）」の 2 系統の識別子を自ら公表している。THÉSEUS が探している surrogate key の候補は、造り手の側にすでに存在する。**
>
> 🔴 **④ 「マロラクティック発酵をしない」と言ってはならない。造り手はそう書いていない。**
> ✅ **FR: 「la clarification est naturelle, et `la fermentation malolactique n'est pas provoquée`. `Toutefois, si celle-ci se produit naturellement, elle n'est pas interrompue.`」**
> ✅ **EN: 「`malolactic fermentation never provoked, but if it happens naturally, it is not interrupted`」**
> 🔴 **canonical は 3 レコードすべてで `aging` 文字列に `(no MLF)` を、`tags` に `"No MLF"` を、`winemaking` に `Pas de FML` を書いている。公式と一致しない。** → §Canonical Conflict ②
>
> 🔴 **⑤ ドサージュの数値は、造り手が意図的に公表していない。**
> ✅ **「`Chez Krug, il n'existe pas de règle concernant le niveau de dosage, mais plutôt une philosophie.`」**
> ✅ **EN: 「`At Krug, there are no rules around the dosage amount, but rather a philosophy.`」**
> 🔴 **取得した公式 FR/EN 全ページと 172 Champagne Notes を全文検索して、`g/L` の表記は 0 件。**
> 🔴 **canonical は 3 レコードすべてに `dosage: "6 g/L"` を書いている。出典が確認できない。** → §Canonical Conflict ②
>
> 🔴 **⑥ 熟成の下限は「7 年」。「6 年」ではない。**
> ✅ **「chaque nouvelle Édition de Krug Grande Cuvée rejoint les caves de la Maison Krug, `où elle va reposer pendant sept années au minimum`.」**
> ✅ **EN: 「they will `rest for at least seven years`」**／✅ **172 Champagne Notes: 「`A stay of around seven years in Krug's cellars`」**
> 🔴 **canonical の 171 と 173 は `minimum 6 years on lees`、172 だけ `7+ years on lees`。同一プロダクト内で不整合であり、かつ 6 年は公式と食い違う。** → §Canonical Conflict ②
>
> 🔴 **⑦ 栽培 —— Krug は「オーガニック」「ビオディナミ」を一度も名乗っていない。自称は `viticulture durable` である。**
> 🔴 **取得した公式 FR/EN 全ページを `biodynam` / `agriculture biologique` / `Demeter` / `Ecocert` / `HVE` / `Terra Vitis` / `VDC` で全文検索 → `0 件`。**
> 🏛 **Agence Bio は `SIRET 50955345900033`（MHCS 本店）で陽性 1 件を返すが、`activites` は `Préparation` / `Distribution` / `Importation` の 3 つだけで、**`Production`（栽培）が無い**。`dateEngagement` は `2022-07-02`。**
> 🔴 **MHCS は Krug 単独の法人ではない（→ §Identity）。したがってこの登録を Krug の畑に結びつけることはできず、まして 2015 / 2016 / 2017 収穫のボトルには時系列で届かない。** → §Farming
>
> 🔴 **⑧ 「農薬を使いません」と言ってはならない。造り手の記述はもっと限定的で、しかも注記付きである。**
> ✅ **「Chez Krug, la viticulture est `exempte d'herbicide ou d'insecticide*`, et utilise `exclusivement des engrais organiques, du cuivre et du soufre`.」**
> ✅ **脚注: 「`*à l'exception des parcelles soumises au traitement obligatoire de la flavescence dorée.`」**
> 🔴 **除草剤と殺虫剤の話であって、殺菌剤の話ではない。銅と硫黄は使う。そして法定防除は例外である。** → §Staff Notes ⚠️ ⑤
>
> ⚠️ **調査上の制約**
> ⚠️ **① 公式 `Champagne Notes` PDF は 172ème Édition の 1 点しか存在を確認できなかった。**171 / 173 / 174 / 170 について同一命名規則の URL を叩いたが**全て `404`（HTML 本文が返る偽 PDF）**であり、内容は一切使っていない。
> ⚠️ **② `Brut` という語が、取得した公式 FR/EN ページと 172 Champagne Notes のどこにも 0 件である。**OBP は `Brut` を印字している。**どちらが誤りとも言えない**（実ラベルの法定表示が未確認）。 → Open Questions 1
> ⚠️ **③ Krug 自身の栽培面積・区画数は公式のどこにも無い。**出てくる ha は `Clos du Mesnil 1,84 ha` と `Clos d'Ambonnay 0,68 ha` の 2 つだけである。 → Open Questions 3
> ⚠️ **④ AOC「CHAMPAGNE」の CDC は 2022-11-30 homologué 版を取得した。**⚠️ **その後 `arrêté du 25 janvier 2024` と `arrêté du 31 juillet 2025` による homologation が存在することを確認したが、本調査ではそのテキストを取得していない。**本ドシエが引く CDC 条文は **2022 年版のもの**である。 → Open Questions 6
> ⚠️ **⑤ プレスページ（`/fr/password/view.press.listing`）は認証ゲートの向こう側にある。**回避行為は行っていない。 → Open Questions 7

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`Krug`**（`source_producer_raw`。3 行すべて同一） |
| **公式表記** | ✅ **`Krug` / `Maison Krug` / `Champagne Krug`**（`<title>` は `… \| Champagne Krug`。ワイン名は常に `Krug Grande Cuvée` の形で書かれる） |
| **Canonical Name（本ドシエの提案）** | **`Krug`** — 🔍 canonical の `producer` フィールドと一致（13 件すべて `"Krug"`） |
| **Aliases** | ✅ **`Maison Krug`** / ✅ **`Champagne Krug`** / 🔍 **`Krug Vins Fins de Champagne`**（🏛 旧法人商号。→ 下記）<br>⚠️ **`Champagne Krug, Vins Fins de Champagne` などの表記ゆれは実ラベルでのみ決着する。** → Open Questions 1 |
| 🔴 **サイト発行者（✅ 公式 mentions légales、`Dernière mise à jour : juin 2023`）** | ✅ **「Le site Internet `www.krug.com` … est édité par `MHCS`, `Société en commandite simple`」**<br>✅ **`capital social : 433 193 789 euros`**／✅ **`numéro d'immatriculation: 509 553 459 RCS Reims`**<br>✅ **`numéro de TVA : FR 44 509 553 459`**／✅ **`N° tél : + 33 (0)3 26 51 20 00`**<br>✅ **`adresse du siège social : 9 Avenue de Champagne 51200 EPERNAY, France`**<br>✅ **`Directeur de publication : Mélanie Boury, International Marketing & Communication and Hospitality Director`**<br>✅ **ホスティング: `ACCENTURE SAS, 118 Avenue de France, 75013 Paris`（`RCS Paris: 732 075 312` / `Code NAF: 6202A`）** |
| 🔴 **サイト発行者（🏛 公的登録）** | 🏛 **SIREN `509553459` / `nom_complet: M H C S`**<br>🏛 **本店 SIRET `50955345900033`／住所 `9 AVENUE DE CHAMPAGNE 51200 EPERNAY`／NAF `11.02A`（発泡性ワインの製造）**<br>🏛 **TVA `FR44509553459`／`nature_juridique 5599`／`etat_administratif: A`／`date_creation: 2008-12-12`**<br>🏛 **`nombre_etablissements: 17`（うち `ouverts: 12`）／`est_bio: true`**<br>🏛 **`dirigeants` に `MOET HENNESSY`・`MOET HENNESSY INVESTISSEMENTS`・`SOCIETE JAS HENNESSY & CO`（いずれも `Administrateur`）、`FORVIS MAZARS SA`（`Commissaire aux comptes titulaire`）** |
| 🔴 ⚠️ **法人格の食い違い** | ⚠️ **公式 mentions légales は `Société en commandite simple` と書き、🏛 登録の `nature_juridique` は `5599` である。**<br>🔴 **本ドシエはどちらも書き換えず、両論を保存する。卓上で法人格に言及する必要はない。** |
| 🔴 **旧法人（🏛 実測。閉鎖済み）** | 🏛 **`KRUG VINS FINS DE CHAMPAGNE` / SIREN `335580296`**<br>🏛 **本店 SIRET `33558029600010`／`5 RUE COQUEBERT 51100 REIMS`／NAF `11.02A`／`date_creation: 1955-01-01`／`date_fermeture: 2009-12-31`／`etat_administratif: C`**<br>🏛 **第 2 事業所 `33558029600028`／`65 AV DE LA GRANDE ARMEE 75016 PARIS 16`／NAF `47.25Z`／同日閉鎖**<br>🔴 **`5 rue Coquebert` は現在も ✅ 公式が `La Maison de Famille Krug` の所在地として名指しする住所である（→ §Location）。法人としては 2009 年に閉じている。** |
| 🔴 **経営・技術（✅ 公式が名指し）** | ✅ **`Julie Cavil` — `Chef de Caves de la Maison Krug`**<br>✅ **`Olivier Krug` — `Sixième génération de la famille Krug & Directeur de la Maison Krug`**<br>✅ **`Éric Lebel` — `Précédent Chef de Caves & Directeur Délégué de la Maison Krug`**（✅「Je me souviens de ma première création, `la 154ème Édition de Krug Grande Cuvée`」）<br>✅ **`Isabelle Bui` — `Responsable Développement Oenologie & Membre du Comité de Dégustation`**<br>✅ **`Jérôme Jacoillot` — `Responsable Développement Vigne & Vin et membre du Comité de Dégustation`**<br>✅ **`Soline Bérêche` — `Experte Viticole en charge des relations Vignoble et membre du Comité de Dégustation`**<br>✅ **`Laurent Halbin` — `Responsable des opérations oenologie & Membre du Comité de Dégustation`**<br>✅ **`Arnaud Lallement` — Maison de Famille の厨房を指揮する `Chef`（`étoilé au guide Michelin`）** |
| **canonical id** | 🔍 **13 件**（`krug-grande-cuvee-162` 〜 `-173` の 12 件＋`krug-rose-27`。→ §Canonical Conflict） |

### 🔴 ✅ サイト真正性の事前チェック（`D-2026-08-05-09`）

🔴 **本ブリーフは候補ドメインを名指ししていない。以下は本調査が自力で特定し、検証した結果である。**

| 条件 | 判定 | 根拠 |
|---|---|---|
| 🔴 **(a) 法的表示 ⟷ 公的登録の一致** | 🔴 ✅ **合格（完全一致）** | ✅ mentions légales の `509 553 459 RCS Reims` / `FR 44 509 553 459` / `9 Avenue de Champagne 51200 EPERNAY` が、🏛 企業登録の SIREN `509553459`・TVA `FR44509553459`・本店住所 `9 AVENUE DE CHAMPAGNE 51200 EPERNAY` と**一字一句一致する**。 |
| **(c) 住所の一致** | ✅ **合格** | 上記に同じ。加えて 🏛 登録の `dirigeants` に `MOET HENNESSY` 系 3 社が入っており、mentions légales の法人像と整合する。 |
| 🔴 **(b) 所有者・アペラシオン団体からの相互リンク** | ⚠️ **本調査では取得できなかった** | ⚠️ **`lvmh.com/en/houses/wines-spirits/krug` は `HTTP 404`。`moethennessy.com/en/our-maisons/krug/` は `HTTP 200` を返すが、返る HTML は JS 描画前のシェルで `<title>` が `LVMH, leader mondial des produits de haute qualité`、`krug.com` の出現回数は `0`。**<br>🔴 **これは「相互リンクが存在しない」証明ではない。取得できなかったという記録である。** |
| 🔴 **(d) 追加の真正性シグナル** | 🔴 ✅ **合格** | 🔴 **`/fr/fiche-produit-des-qualites-et-caracteristiques-environnementales` が、`décret 2022-748 du 29 avril 2022`（loi AGEC 13-I 条）に基づく法定の製品情報を、Krug の実 SKU 名（`GRANDE CUVEE 75CL EDITION 171` / `… EDITION 172` / `… EDITION 173` 等）で列挙している。**<br>🔴 **この開示義務を負うのは製造者・輸入者・販売者であって、第三者サイトではない。** |
| **総合判定** | 🔴 ✅ **`www.krug.com` を一次資料として採用する** | **(a)(c)(d) が成立。(b) のみ未取得であり、それを理由に採用を取り下げる根拠は無い。** |

### ⚠️ 同名・近名の別事業者 —— `CDX-9`（部分文字列一致は安全でない）の実測

🔴 **`?q=KRUG&departement=51` は 7 件を返す。SIREN が別なら別法人である。**

| 🏛 SIREN | 🏛 商号 | 🏛 住所 / NAF / 状態 | 判定 |
|---|---|---|---|
| 🔴 **`335580296`** | **`KRUG VINS FINS DE CHAMPAGNE`** | `5 RUE COQUEBERT 51100 REIMS` / `11.02A` / **`C`（2009-12-31 閉鎖）** | 🔴 **本件の旧法人。現在は閉鎖。** |
| `385370978` | `COMITE SOCIAL ET ECONOMIQUE VCP/KRUG` | `12 RUE DU TEMPLE 51100 REIMS` / `94.20Z` / `A` | ⚠️ **労使組織。ワイン生産者ではない。** |
| `494638141` | `REMI KRUG` | `10 RUE DU CLOITRE 51100 REIMS` / `70.22Z` / `C` | ⚠️ **個人名の法人（経営コンサル NAF）。閉鎖。ドシエの記述には一切使っていない。** |
| `494603012` | `R.K.CONSEIL` | `10 RUE DU CLOITRE 51100 REIMS` / `70.22Z` / `C` | ⚠️ **同上。** |
| `852572288` | `PAUL KRUG` | `15 RUE PRIEUR DE LA COTE D'OR 21000 DIJON` / `74.90B` / `C` | ⚠️ **Côte-d'Or。無関係。** |
| `528646888` | `SCI DU PELICAN` | `10 RUE DU CLOITRE 51100 REIMS` / `68.20B` / `A` | ⚠️ **不動産 SCI。** |
| ⚠️ **`340318740`** | **`SON CIV IMMOB DU MESNIL`** | `2 RUE PASTEUR 51190 LE MESNIL-SUR-OGER` / `68.20B` / `C` | ⚠️ **`Le Mesnil` という語で当たるが、不動産 SCI であり `Clos du Mesnil` との関係は登録から決まらない。使用していない。** |

🔴 **canonical 側の混同は起きていない。** 🔍 canonical 928 件を `krug` で全文走査 → 18 件。うち `producer == "Krug"` が 13 件、
残り 5 件は他生産者の prose に `Krug` が現れるだけ（`cristal-2015` / `dom-perignon-p2-2003` / `dom-perignon-oenotheque` / `alfred-gratien-brut-nv` / `dehours-grande-reserve-brut-nv`）。**別生産者への取り違えは 0 件。**

---

## Overview

✅ **Krug は 1843 年に `Joseph Krug` が Reims で創業したシャンパーニュのメゾンである。
現在の Chef de Caves は `Julie Cavil`、Maison の Directeur は創業家 6 代目の `Olivier Krug`。
サイトを発行する法人は `MHCS`（🏛 SIREN 509553459、本店 Épernay）である。**

🔴 ✅ **公式が自らの署名として名指しするものは、はっきりと 3 つある —— `savoir-faire` の「3 本の柱」である。**

🔴 ✅ **① `INDIVIDUALITÉ`（一区画・一ワイン）。**
「**Chez Krug, notre philosophie consiste à `récolter et isoler chaque parcelle pour en extraire un vin unique`, révélant ses nuances et caractéristiques propres.
`Il n'y a aucune hiérarchie dans notre sélection : aucune parcelle n'est privilégiée.`**」（Julie Cavil、`/fr/savoir-faire`）

🔴 ✅ **② `L'ART DE L'ASSEMBLAGE`（アッサンブラージュ）。**
「**Après avoir consigné `environ 5 000 notes de dégustation` sur `près de 400 vins` provenant de `plus de 10 millésimes différents`, Julie Cavil met en œuvre l'art de l'assemblage.**」

🔴 ✅ **③ `PATIENCE`（時間）。**
「**`Il faut plus de 20 ans` pour donner naissance à une nouvelle Édition de Krug Grande Cuvée …
Chaque Krug Grande Cuvée résulte de l'assemblage `d'au moins 120 vins issus de plus de 10 années différentes`, `le plus ancien remontant toujours à plus d'une décennie`.**」（`/fr/savoir-faire/patience`）

🔴 ✅ **そして Krug Grande Cuvée そのものの自己規定はこうである ——**
「**`Krug Grande Cuvée dépasse la notion même de millésime.` Il est le fruit de l'assemblage de `plus de 120 vins individuels`, issus `d'une dizaine d'années différentes`.
Combiner autant de vins et d'années permet d'obtenir `une richesse de saveurs et d'arômes impossible à exprimer avec les vins d'une seule année`.**」（`/fr/champagne/krug-grande-cuvee-173eme-edition`）
✅ **172 Champagne Notes（EN）の言い回し: 「`It is the full orchestra, playing together the symphony of Champagne.`」**

🔍 **THÉSEUS における状態は、Palmer とは正反対の形である。
canonical はこの生産者について 13 レコードを持ち、OBP 3 行に対応する 3 件は**すでに存在し、base year も正しい**。
それでも 3 行はすべて `unresolved` に落ちている。すなわち主たる問題は `不在` でも `矛盾` でもなく、**マッチャが自分の在庫を見つけられていない**ことである。
その上に、格納値の側の誤り（`6 g/L` / `No MLF` / `6 years` / `45 lieux-dits`）が重なっている。**

---

## History

✅ **公式の沿革は `/fr/notre-histoire`・`/fr/savoir-faire`・`/fr/savoir-faire/individualite`・`/fr/nos-lieux-emblematiques` に分散している。以下は公式の記述のみ。**

| 年 | 出来事 ✅ |
|---|---|
| 🔴 **1843** | 🔴 ✅ **創業。「`En 1843, Joseph Krug fonde la Maison Krug`, guidé par sa conviction : `créer le meilleur champagne possible, chaque année, quelles que soient les variations climatiques.`」**<br>✅ **「`Depuis 1843`, la Maison Krug est guidée par la vision de Joseph Krug」／`Six générations de la famille Krug` ont perpétué ce rêve.」** |
| 🔴 **1848** | 🔴 ✅ **創業者の手帳。「`En 1848`, Joseph Krug a consigné sa vision dans les pages de `son carnet personnel couleur cerise noire`, initiant une tradition de transmission.」**<br>✅ **引用（verbatim）: 「`On ne peut obtenir de bons vins sans y employer de bons éléments et des vins de bons crus.` On a pu obtenir d'apparence de bonnes cuvées en employant des éléments et des crus moyens ou même médiocres ; mais ce sont des exceptions sur lesquelles il ne faut jamais compter : `on risque de manquer son opération, ou de perdre sa réputation.`」** |
| 🔴 **1868** | 🔴 ✅ **「`La Maison de Famille Krug` est située au `5, rue Coquebert, à Reims, depuis 1868`.」** |
| 🔴 **1876** | 🔴 ✅ **「`Notre plus ancien contrat en vigueur remonte à 1876`, et `100 % de nos engagements concernent des parcelles spécifiques`.」** |
| 🔴 **1971** | 🔴 ✅ **「`En 1971`, `Rémi et Henri Krug`, `cinquième génération` de la famille Krug, font l'acquisition de vignes dans le village du `Mesnil-sur-Oger`, réputé pour son Chardonnay, `dont une parcelle murée de 1,84 hectare` au cœur du village.」**<br>✅ **壁の刻銘（公式が verbatim で掲げる）: 「`En l'an 1698, cette muraille a été construite par Claude Jannin et Pierre Dehée Metoen et la même année, la vigne a été plantée par Gaspard Jannin, fils de Claude.`」**<br>⚠️ **`/fr/notre-histoire` は同じ出来事を「`Au début des années 1970`」と書く。年を 1 点に絞るなら `/fr/savoir-faire/individualite` の `1971` を採る。** |
| 🔴 **1976** | 🔴 ✅ **「`En 1976`, les deux frères ont une nouvelle vision : créer un champagne rosé, inspiré de l'art de l'assemblage emblématique de la Maison, qui pourrait être recréé chaque année. `Le premier Krug Rosé voit le jour sept ans plus tard.`」**<br>⚠️ **公式は「7 年後」としか書かず、西暦を書いていない。年号を口にしない。** |
| 🔴 **1979** | 🔴 ✅ **「`En 1979`, les frères Krug décident de créer un champagne exclusivement issu des raisins récoltés cette même année au sein du Clos. `Krug Clos du Mesnil 1979` voit alors le jour, `à une époque où la tradition champenoise repose principalement sur l'art de l'assemblage`.」** |
| 🔴 **1991** | 🔴 ✅ **「`sept années de recherche` aboutissent à `la découverte du Clos d'Ambonnay en 1991`. Cette parcelle de `0,68 hectare`, située au bord du village, `sur le flanc sud-est de la Montagne de Reims`, est `protégée de murs qui l'entourent depuis 1766`.」** |
| 🔴 **1995 / 2007** | 🔴 ✅ **「`Élaboré dans le plus grand secret`, `Krug Clos d'Ambonnay 1995`, le premier champagne issu de cette parcelle unique, et d'une même année, `a été présenté en 2007`.」** |
| 🔴 **2004 →** | 🔴 ✅ **「`Depuis 2004`, la Maison Krug a obtenu les certifications `ISO 14001`, `ISO 22000 & FSSC`, `ISO 50001` et `ISO 9001`, attestant de nos standards en matière de `gestion environnementale, de sécurité alimentaire, de qualité et d'énergie`.」** |
| 🔴 **2011** | 🔴 ✅ **「`En 2011`, la Maison Krug introduit le `Krug iD`, `un code à six chiffres apposé sur la contre-étiquette de chaque bouteille Krug`.」**<br>✅ **同年: 「`En 2011`, nous avons fait appel à `Riedel`, le célèbre maître verrier, pour concevoir un verre capable de sublimer toute la palette aromatique de Krug Grande Cuvée.」（`Le Verre Joseph`）** |
| 🔴 **2016 →** | 🔴 ✅ **「`À partir de 2016`, la Maison Krug attribue `un numéro d'Édition` à chaque nouvelle création de Krug Grande Cuvée et Krug Rosé.」** → §Important Cuvées |
| **2017** | ✅ **`La Maison de Famille Krug` が「`entièrement rénovée en 2017`」。** |
| **2023** | ✅ **「`En 2023`, la Maison Krug a inauguré `La Loge`, qui surplombe l'un de ses vignobles du village de `Trépail`.」** |
| 🔴 **2024** | 🔴 ✅ **「`Inauguré en 2024 après sept années de travail`, le site de vinification `Joseph` est situé au `Clos d'Ambonnay` de Krug.」**<br>✅ **「`Certifié HQE à niveau dit « exceptionnel »`」／「réunit `toutes les activités de vinification et de création` de la Maison Krug `dans un même lieu`」** |

⚠️ **公式沿革に無いもの**: Joseph Krug の出自と創業前の経歴、2 代目〜4 代目の名前と年、
`Krug Vins Fins de Champagne`（🏛 SIREN 335580296、1955 年設立・2009 年閉鎖）と現行法人の関係、MHCS への統合年、
Édition 番号を最初に付けたのが何番の Édition か。 → Open Questions 2・4

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ 🏛 |
| 🔴 **Appellation** | 🔴 🏛 **`AOC Champagne`。**🏛 **「Seuls peuvent prétendre à l'appellation d'origine contrôlée " Champagne ", `reconnue initialement par le décret du 29 juin 1936`, les vins répondant aux dispositions du présent cahier des charges ainsi qu'aux dispositions de la `loi du 6 mai 1919` relative à la protection des appellations d'origine.」**<br>**出典: `Cahier des charges de l'AOC « CHAMPAGNE » homologué par l'arrêté du 30 novembre 2022, publié au JORF du 10 décembre 2022`（BO du MASA、2022-12-15） |
| 🔴 **Village（メゾン所在）** | 🔴 ✅ 🏛 **`Reims`（INSEE `51454`、CP `51100`、`anciensCodes: ["51401"]`）。**<br>✅ **「`La Maison Krug, établie à Reims depuis sa fondation en 1843`」／「La Maison de Famille Krug est située au `5, rue Coquebert, à Reims, depuis 1868`.」**<br>🔴 ⚠️ **一方、サイトを発行する法人 MHCS の登記本店は `9 Avenue de Champagne 51200 EPERNAY` である（✅ mentions légales と 🏛 登録が一致）。メゾンの所在地と登記本店は別のコミューンにある。** |
| 🔴 **Key Vineyards ①** | 🔴 ✅ **`Clos du Mesnil` —— `1,84 hectare`、`Le Mesnil-sur-Oger` の村の中心にある壁で囲まれた単一区画。Chardonnay。**<br>🏛 **`Le Mesnil-sur-Oger` は INSEE `51367`、CP `51190`。**🏛 **CDC II 章 b) の `grand cru` 併記が認められる 17 コミューンの 1 つ。**<br>✅ **「réputé pour son Chardonnay」／壁の刻銘は `1698`。** |
| 🔴 **Key Vineyards ②** | 🔴 ✅ **`Clos d'Ambonnay` —— `0,68 hectare`、`Ambonnay` の村はずれ、`sur le flanc sud-est de la Montagne de Reims`。Pinot Noir。壁は `1766` 年から。**<br>🏛 **`Ambonnay` は INSEE `51007`、CP `51150`。**🏛 **同じく CDC の `grand cru` 併記コミューン 17 件の 1 つ。** |
| **Key Vineyards ③** | ✅ **`Trépail` に Krug の vignoble があり、2023 年に `La Loge` がそれを見下ろす形で開かれた。**<br>🏛 **`Trépail` は INSEE `51580`、CP `51380`。**🏛 **CDC II 章 c) の `premier cru` 併記コミューン。** |
| 🔴 **醸造施設** | 🔴 ✅ **`Joseph`（2024 年開設）—— `situé au Clos d'Ambonnay de Krug`。すなわち Ambonnay。**<br>✅ **`La Maison de Famille Krug`（5 rue Coquebert, Reims）—— 「repose au-dessus des `caves historiques` de la Maison ainsi que de sa `bibliothèque de vins de réserve`」／1 階に `salle de dégustation` と `Mur des 400 Vins`。** |
| 🔴 **ブドウの供給構造（✅ 公式）** | 🔴 ✅ **「Dans la région champenoise … `la majorité des vignobles appartiennent à des vignerons indépendants` … Chez Krug, cultiver des liens privilégiés avec les vignerons a toujours été une priorité.」**<br>🔴 ✅ **「Aujourd'hui, `le Cercle des Vignerons Krug` réunit `une centaine de membres` issus de `toute l'appellation Champagne`.」**<br>🔴 ✅ **「`Notre plus ancien contrat en vigueur remonte à 1876`, et `100 % de nos engagements concernent des parcelles spécifiques`.」**<br>🔴 **すなわち Krug Grande Cuvée のブドウは「Reims の畑」ではなく、アペラシオン全域の自社畑＋Cercle 会員の特定区画から来る。** → §Staff Notes ⚠️ ⑦ |
| 🏛 **CDC の品種** | 🏛 **`cépages principaux`: `Arbane B`, `Chardonnay B`, `Meunier N`, `Petit meslier B`, `Pinot blanc B`, `Pinot gris G`, `Pinot noir N`（`≥ 95 %` de l'encépagement）**<br>🏛 **`variété d'intérêt à fin d'adaptation`: `Voltis B`（`≤ 5 %`、INAO/ODG/事業者間の convention 締結が条件）**<br>🔴 **法令上の綴りは `Meunier N` であって `Pinot Meunier` ではない。**✅ **Krug も一貫して `Meunier` と書く。** |
| 🏛 **CDC の熟成規定** | 🏛 **「Le dégorgement `ne peut être effectué avant une période de douze mois à compter de la date de tirage`」**<br>🏛 **「Les vins ne sont mis en marché à destination du consommateur qu'à l'issue d'une période d'élevage de `quinze mois minimum` à compter de la date du tirage en bouteille.」**<br>🏛 **「Les vins susceptibles d'être présentés avec l'indication du millésime … `trente-six mois minimum`」**<br>🔴 **Krug 自身の下限は `sept années au minimum`。法定下限（15 か月）の 5 倍以上である。** |
| 🔴 ⚠️ **自社畑の面積** | 🔴 ⚠️ **公式サイトに Krug 自身の総栽培面積・区画数の記載が無い。**取得した公式ページで ha が出るのは `1,84 ha`（Clos du Mesnil）と `0,68 ha`（Clos d'Ambonnay）の 2 つだけである。 → Open Questions 3 |

❓ **公式に無い**: 自社畑の総面積・区画数・村別内訳、Cercle des Vignerons Krug の会員名簿、
Grande Cuvée に用いられた村・区画の一覧、土壌の記述（白亜／craie についての記述が公式ページに無い）。

---

## Farming

🔴 **本節の要点は 3 つ。**
🔴 **① Krug は自らを `viticulture durable`（持続可能な栽培）と呼び、`bio` / `biodynamie` を一度も名乗っていない。**
🔴 **② 🏛 Agence Bio に SIRET 完全一致の陽性はあるが、それは MHCS のもので、`Production`（栽培）を含まない。**
🔴 **③ したがって OBP の 3 本（base 2015 / 2016 / 2017）に、どの有機ラベルも貼れない。**

### 🔴 ✅ ① 造り手自身の記述（`/fr/savoir-faire/individualite` §`NOS ENGAGEMENTS DURABLES`）

🔴 ✅ **「Cette philosophie se traduit dans notre approche de la viticulture : `100% des matières premières de la Maison Krug sont produites selon des normes exigeantes d'excellence et de respect de l'environnement`,
qu'il s'agisse de `nos vignes`, ou des `parcelles cultivées par la communauté du Cercle des Vignerons Krug`.」**

🔴 ✅ **「Chez Krug, `la viticulture est exempte d'herbicide ou d'insecticide*`, et `utilise exclusivement des engrais organiques, du cuivre et du soufre`.
Afin de limiter l'érosion, `les inter-rangs sont toujours enherbés en période de dormance de la vigne`,
et `des essais de couverts végétaux et d'infusions de compost sont réalisés chaque année`.
Par ailleurs, `des audits de biodiversité menés par des écologues` nous ont guidés dans `la création de haies` et l'adaptation de nouvelles plantations.」**

🔴 ✅ **脚注（公式が自ら付している）: 「`*à l'exception des parcelles soumises au traitement obligatoire de la flavescence dorée.`」**

⚠️ 🔴 **FR / EN の食い違い（1 件）。**
✅ **FR: 「`du cuivre et du soufre`」（銅と硫黄）** ⟷ ✅ **EN: 「`the utilisation of organic fertiliser only, and of copper sulphate`」（硫酸銅）。**
⚠️ **`cuivre et soufre`（2 物質）と `copper sulphate`（1 化合物）は同じではない。**🔴 **本ドシエは FR を原本として採用し、EN の差を記録にとどめる。卓上でこの細部に踏み込まない。**

🔴 ✅ **認証（造り手が名指しするもの、全 5 件）**
- ✅ **`ISO 14001` / `ISO 22000 & FSSC` / `ISO 50001` / `ISO 9001` —— 「`Depuis 2004`」**
- ✅ **`HQE`「`niveau exceptionnel`」—— 対象は **建物**（醸造施設 `Joseph`）であって畑ではない。**
- ✅ **Isabelle Bui の但し書き（公式が掲げる）: 「`Il ne s'agit pas d'accumuler des labels.` L'approche HQE a été `un véritable outil de pilotage`, intégré dès le début du projet et appliqué à chaque décision.」**

✅ **その他の実務**: 「`le transport aérien est proscrit` et n'est envisagé qu'en cas d'absolue nécessité」／
「le nouveau site Joseph `consomme moins d'eau que le site historique` et `zéro énergie fossile`」／
「`Tous les déchets sont triés, et réutilisés pour produire de l'énergie`」／「un `coffret cadeau 100 % recyclable`」。

### 🔴 🏛 ② 公的登録の実測 —— **陽性 1 件・陰性 1 件、どちらも Krug の畑を保証しない**

🔴 **`GET https://opendata.agencebio.org/api/gouv/operateurs/?siret=50955345900033` → `nbTotal: 1`（SIRET 完全一致）**

| 項目 | 🏛 登録値（verbatim） |
|---|---|
| **raisonSociale** | **`M H C S`** |
| 🔴 **numeroBio** | 🔴 **`18379`** |
| 🔴 **certificats[0]** | 🔴 **`Ecocert France` / `etatCertification: ENGAGEE` / `dateEngagement: 2022-07-02` / `datePremierEngagement: null`**<br>🏛 **証明 URL `https://certificat.ecocert.com/entreprise/C2CCD7D5-1887-4BA7-8217-84A5F38B6602`** |
| **certificats[1]** | **`Bureau Veritas Certification France` / `etatCertification: ARRETEE` / `dateEngagement: 2020-10-19`**（🏛 `https://certifie.bureauveritas.fr/organisme/145302`） |
| 🔴 **activites** | 🔴 **`Préparation` / `Distribution` / `Importation` の 3 つ。**🔴 **`Production`（栽培）は無い。** |
| **adressesOperateurs** | **`RUE DES MARDILLES PARC INDUSTRIEL` / `9 AV DE CHAMPAGNE`**（🔴 **どちらも Krug の Reims / Ambonnay の所在地ではない**） |

🔴 **`GET .../operateurs/?siret=33558029600010`（旧法人 `KRUG VINS FINS DE CHAMPAGNE` 本店）→ `nbTotal: 0`。**
🔴 **これは `CDX-9` の意味での**証明された陰性**である（exact-SIRET 一致による否定）。**

### 🔴🔴 温度差の罠 —— **OBP の 3 本に、どの有機ラベルも貼れない**

| OBP 行 | ベース収穫 | 🏛 Agence Bio | ✅ 造り手の自称 | 🔴 卓上で言えること |
|---|---|---|---|---|
| 🔴 **171ème Édition** | ✅ **2015**（最古のリザーヴは 2000） | 🔴 **MHCS の `dateEngagement 2022-07-02` の **7 年前**。しかも登録に `Production` が無い** | ✅ **`viticulture durable`** | 🔴 **「オーガニック」「ビオディナミ」「Ecocert」を**一切言ってはならない**。言えるのは「除草剤・殺虫剤を使わない栽培だと造り手が公表しています」まで** |
| 🔴 **172ème Édition** | ✅ **2016**（最古 1998） | 🔴 **同上（6 年前）** | ✅ **同上** | 🔴 **同上** |
| 🔴 **173ème Édition** | ✅ **2017**（最古 2001） | 🔴 **同上（5 年前）** | ✅ **同上** | 🔴 **同上** |

→ 🔴 **加えて、リザーヴワインの最古は 1998 / 2000 / 2001 である。1 本のボトルの中身は 20 年以上の幅を持つ。**
→ 🔴 **「このボトルは何年の栽培方針で造られたか」という問い自体が、Grande Cuvée では単一の答えを持たない。**
→ 🔴 **これは Palmer の 5 本と同じ構造の罠だが、Krug では**1 本の中で**時間幅が発生している点が違う。**

⚠️ **公式に無い**: 有機・ビオディナミの取得意思の有無、銅の年間使用量、被覆作物の草種、
Cercle des Vignerons Krug の会員に課される具体的な栽培基準、自社畑と Cercle 畑の比率。 → Open Questions 5

---

## Winemaking

### 🔴 ✅ 発酵 —— **小さな古い樽。「一区画・一ワイン」のための道具**

🔴 ✅ **「Pour préserver au mieux la richesse et l'expression unique de chaque parcelle avant l'assemblage, `nous limitons nos interventions pendant la vinification`.
Afin de garantir l'agilité nécessaire pour notre approche `« une parcelle, un vin »` qui peut concerner `des parcelles aussi petites qu'un jardin`,
`nos vins prennent naissance dans de petits fûts de chêne anciens`.」**（`/fr/savoir-faire/individualite`）

🔴 **`fûts de chêne anciens`（古い樽）であって新樽ではない。公式は続けて `Dans ces fûts neutres` と書き、EN 版は `which are neutral and thus do not impact the flavour of the wines` と補う。**

### 🔴🔴 ✅ マロラクティック発酵 —— **「しない」ではない**

🔴 ✅ **FR: 「la clarification est naturelle, et `la fermentation malolactique n'est pas provoquée`.
`Toutefois, si celle-ci se produit naturellement, elle n'est pas interrompue.`」**
🔴 ✅ **EN: 「clarification is natural and `malolactic fermentation never provoked, but if it happens naturally, it is not interrupted`」**

🔴 **正確な言い方は「誘導しない。ただし自然に起これば止めない」である。**
🔴 **canonical の `No MLF` / `(no MLF)` / `Pas de FML` は、この 2 文目を落としている。** → §Canonical Conflict ②

### ✅ 清澄・貯蔵

✅ **「Les vins sont ensuite clarifiés grâce à `un soutirage traditionnel à la fontaine` et réceptionnés dans `de petites cuves en acier inoxydable` où ils patientent `sur lies fines` le temps des dégustations et de la décision finale d'assemblage ou de mise en réserve.」**
✅ **EN 版は `naturally clarified by gravity through traditional racking` と補足する。**

### 🔴 ✅ アッサンブラージュ —— **儀式として公表されている**

🔴 ✅ **「`Chaque matin à 11 heures précises`, lors des `six mois qui suivent la vendange`, le Comité de Dégustation se réunit `à huis clos`.
… `Les dégustations à l'aveugle ne portent jamais sur plus de 15 vins par jour.`
La personnalité de chacun d'entre eux est minutieusement consignée … Au total, `environ 5 000 notes de dégustation sont enregistrées chaque année`, avant même d'envisager l'assemblage des différentes cuvées.」**

🔴 ✅ **「Chaque année, le Comité de Dégustation de la Maison déguste `environ 400 de ces individualités`,
dont `250 vins de l'année`, et `150 vins de réserve` issus de `près de 15 années de vendanges précédentes`.」**

✅ **Comité de Dégustation の性格: 「`Ce cercle restreint rassemble des femmes et des hommes d'horizons, de générations et de sensibilités tout aussi diverses que complémentaires`, où `chaque voix compte autant que les autres` dans la décision finale.」**

### 🔴 ✅ 熟成 —— **最低 7 年。フォーマットで加算される**

🔴 ✅ **「Chaque année, une fois la composition finale créée, chaque nouvelle Édition de Krug Grande Cuvée rejoint les caves de la Maison Krug, `où elle va reposer pendant sept années au minimum`.」**
🔴 ✅ **EN: 「they will `rest for at least seven years`」**／✅ **172 Champagne Notes: 「`A stay of around seven years in Krug's cellars` gives Krug Grande Cuvée 172ème Édition its distinct expression and elegance.」**

🔴 ✅ **「Comparé à une bouteille de `75cl` de Krug Grande Cuvée, `un Magnum (150cl) repose une année supplémentaire en cave`, et `un Jéroboam (300cl) deux ans de plus`.
En raison de leur taille, ces champagnes évoluent plus lentement et nécessitent davantage de temps pour atteindre leur pleine expression.」**

✅ **他のキュヴェ: 「`Krug Millésime, Krug Clos du Mesnil et Krug Clos d'Ambonnay passent généralement plus de dix ans en cave`. `Krug Collection`, la seconde vie de Krug Millésime, `repose quant à lui plus de 20 ans en cave`」**

### 🔴 ✅ ドサージュ —— **数値は公表されていない。これは欠落ではなく方針である**

🔴 ✅ **「`Chez Krug, il n'existe pas de règle concernant le niveau de dosage, mais plutôt une philosophie.`
Après plusieurs années au sein de nos caves, cette ultime étape de l'élaboration de chaque cuvée vient `préciser l'harmonie du champagne sans jamais en modifier le caractère`.」**
✅ **Henri Krug の言葉（公式が掲げる）: 「`Si on ne dose pas la bouteille, on risque de le sentir ; du fait d'une certaine dureté en finale, par exemple… Mais à l'inverse, lorsqu'on dose, nous ne devons pas le sentir !`」**
✅ **EN 版の言い回し: 「`For Krug, the right dosage is the one whose absence would be missed, but whose presence is imperceptible.`」**

🔴 **取得した公式 FR/EN ページ＋172 Champagne Notes を `g/L` で全文検索 → `0 件`。**

### ✅ 哲学（造り手の一文）

✅ **「Au sein de la Maison Krug, `le temps n'est pas une contrainte, mais une force et un allié`.」**
✅ **Éric Lebel: 「De la sélection des raisins à la lente maturation de nos champagnes, `la patience est notre force motrice essentielle`. `Krug ne peut être précipité.` Le temps est une force et un allié.」**
✅ **Julie Cavil: 「`Notre obsession est de préserver l'origine et le caractère de chaque parcelle à travers son vin.`」**

⚠️ **公式に無い**: 発酵温度、酵母、樽の容量（`petits fûts` としか書かない）と本数、圧搾方式、
tirage 日、dégorgement 日、アルコール度数、生産本数、樽職人名。

---

## Style

### ✅ 公式のスタイル記述（**造り手自身の言葉のみ**）

| 対象 | ✅ 公式の記述 |
|---|---|
| 🔴 **Krug Grande Cuvée（総論）** | **「`L'expression la plus généreuse du Champagne`」（全ページ共通の副題）**<br>**「`Krug Grande Cuvée dépasse la notion même de millésime.` Il est le fruit de l'assemblage de `plus de 120 vins individuels`, issus `d'une dizaine d'années différentes`. Combiner autant de vins et d'années permet d'obtenir `une richesse de saveurs et d'arômes impossible à exprimer avec les vins d'une seule année`.」**<br>✅ **EN（172 Champagne Notes）: 「`It is the full orchestra, playing together the symphony of Champagne.`」** |
| 🔴 **171ème Édition** | **「Visuellement, ce champagne se pare d'une `robe couleur or pâle` et se meut de `fines bulles vives` … Des arômes de `fleurs, d'agrumes mûrs, confits et séchés`, ainsi que de `pâte d'amande et de pain d'épices` stimulent le nez.<br>Des notes de `noisette, de nougat, de sucre d'orge, de fruits et de gelée d'agrumes, d'amandes, de brioche et de miel` explosent en bouche.」** |
| 🔴 **172ème Édition** | ⚠️ **FR ページは 171 と同一のテイスティング・ノートを掲げている**（上と一字一句同じ）。<br>🔴 ✅ **一方 172 の公式 Champagne Notes（EN）は**別の内容**を書く ——「At first sight, `intense yellow gold`. An `elegant and aromatic nose of white flowers, lavender and almond` holds the promise of finesse upon the first sip. The palate is `delicate and intense, long, fresh and persistent`. `White fruits dominate over yellow` and are complemented by citrus through Krug Grande Cuvée's `characteristic lemony notes`. Gentle nuances of `white flowers and violet` caress the palate, giving way to hints of `eucalyptus and menthol`.」**<br>🔴 **172 を語るなら Champagne Notes の側を使う。** → Open Questions 8 |
| 🔴 **173ème Édition** | **「Visuellement, ce champagne se pare d'une `robe couleur or`.<br>Le nez est `expressif, parfumé et puissant`, avec des arômes `toastés et briochés`, de `fruits à noyau, de verveine, de crème pâtissière vanillée, de pain perdu et de baba au rhum`.<br>En bouche, ce champagne est `onctueux, crémeux et généreux` … Des nuances de `fruits juteux, de pêche au sirop et d'agrumes mûrs`, laissent place à des notes `encaustiques, toastées et de pignon de pin`. `Une texture généreuse et précise, avec une note finale nette de citron.`」** |
| 🔴 **提供温度（公式）** | ✅ **「Nous vous conseillons de servir les Champagnes Krug à `une température entre 9 et 12°C` pour révéler pleinement leur richesse. `Servir votre bouteille trop fraîche empêcherait l'expression des arômes.`」**<br>🔍 **canonical は 3 件とも `serving_temp: "9–11°C"` と書く。公式は `9 et 12°C`。** → §Canonical Conflict ② |
| 🔴 **グラス（公式）** | ✅ **「`En 2011`, nous avons fait appel à `Riedel` … pour concevoir un verre capable de sublimer toute la palette aromatique de Krug Grande Cuvée.」（`Le Verre Joseph`）**<br>🔍 **canonical は 3 件とも `glassware: "White Burgundy / Krug ID glass"`。**⚠️ **公式が名指しするのは `Le Verre Joseph`（Riedel 製）であって「Krug ID glass」ではない。** |
| **熟成の方向（公式）** | ✅ **「`Tous les champagnes Krug gagnent en complexité et en patine avec le temps.` Nous vous recommandons de les conserver à `la même température que celle à laquelle vous les servirez`, soit entre 9°C et 12°C.」** |

⚠️ 🔴 **公式サイトに点数・受賞・格付比較の掲載は一切無い。**
⚠️ **公式は「プレステージ・キュヴェ」「トップ・キュヴェ」に相当する序列表現を使わない。**逆に「`une Maison où tous les champagnes sont portés au même niveau d'excellence`（すべてのシャンパーニュが同じ卓越性の水準にあるメゾン）」と書く。 → §Staff Notes ⚠️ ①

### ✅ 公式の食事の合わせ方（OBP 3 行に共通で使える）

✅ **「Krug Grande Cuvée se prête à `une myriade d'accords culinaires, du plus simple au plus sophistiqué`, accompagnant aussi bien `un parmesan vieux` qu'`un turbot à la truffe`.
Il se déguste en apéritif avec `du jambon de Jabugo et du comté vieux` ou accompagné `d'huîtres, de crevettes grillées, de plats indiens ou marocains`,
mais aussi en dessert avec `du gâteau à la carotte, une tarte Tatin ou du cheesecake`.」**（171 / 172 の FR ページ、ほぼ同文）
✅ **173 は加えて「`des plats orientaux ou indiens`」「`turbot à la truffe`」「`comté affiné`」を挙げる。**

---

## Important Cuvées

### 🔴 ✅ 「Édition 番号」とは何か —— **本ドシエの中核。造り手が明文化している**

| 問い | ✅ 造り手自身の答え（verbatim） |
|---|---|
| 🔴 **番号は何を数えているか** | 🔴 ✅ **EN（172 Champagne Notes）: 「`The Édition number identifies a specific creation of Krug Grande Cuvée. It corresponds to the number of years in the House of Krug the founder's dream has been re-created.`」**<br>🔴 ✅ **FR（`/fr/notre-histoire`）: 「`Il indique combien de fois, dans l'histoire de la Maison, Krug Grande Cuvée ou Krug Rosé ont été recréés.`」** |
| 🔴 **いつから付いているか** | 🔴 ✅ **「`À partir de 2016`, la Maison Krug attribue un numéro d'Édition à chaque nouvelle création de Krug Grande Cuvée `et Krug Rosé`.」**<br>🔴 ✅ **「`Jusqu'au milieu des années 2010, les bouteilles quittant nos caves à Reims ne portaient pas de numéro d'Édition`, et les bouteilles plus anciennes peuvent ne pas avoir de Krug iD.」** |
| 🔴 **どこに刷られているか** | 🔴 ✅ **「Ce numéro, `visible sur l'étiquette`」（＝表ラベル）** |
| 🔴 **番号はヴィンテージか** | 🔴 ✅ **違う。「`Krug Grande Cuvée dépasse la notion même de millésime.`」**🔴 **番号は通し番号であり、収穫年でも熟成年数でもロット番号でもない。** |
| 🔴 **では収穫年はどこにあるか** | 🔴 ✅ **各 Édition のページ本文にある。`Créée / Composée autour des vendanges de <YYYY>` という定型で、造り手が 1 本ずつ書いている（下表）。**<br>🔴 **これがラベルに刷られているという記述は公式に無い。** → Open Questions 1 |

### 🔴 ✅ Krug 自身の識別子 —— `Krug iD`

🔴 ✅ **「`En 2011`, la Maison Krug introduit le `Krug iD`, `un code à six chiffres apposé sur la contre-étiquette de chaque bouteille Krug`.
En le saisissant en ligne ou en le scannant via l'application Krug, il révèle `l'histoire de la bouteille, sa composition, des suggestions de service, des inspirations d'accords mets et vins`, et bien plus encore.」**
🔴 ✅ **EN: 「`Enter your bottle's six-digit code` to discover the story of your bottle, Krug's Cellar Master impressions of the year it was created, food pairing suggestions, music pairings and more.」**
✅ **172 Champagne Notes 末尾: 「Discover more about your bottle of Krug with the Krug iD on the Krug app, Twitter or Google. `http://app.krug.com`, `@krug` or `krug.com`.」**

🔴 **すなわち Krug は、ボトル 1 本を一意に指す識別子を**自ら発行し、裏ラベルに刷り、公開照合口を持っている**。
`CDX-8` が探している surrogate key の候補は、少なくとも Krug については造り手の側に既に存在する。本ドシエはこの事実の記録にとどめ、schema 設計には踏み込まない（`D-2026-08-06-06`）。**

### ✅ 公式の現行レンジ（`/fr/` グローバルナビ `Nos champagnes`）

| # | 公式のワイン名 | 公式が並べる直近の 3 点 | OBP |
|---|---|---|---|
| 1 | 🔴 **`Krug Grande Cuvée`** | 🔴 **`173ème Édition` / `172ème Édition` / `171ème Édition`** | 🔴 **OBP 3 行すべてがここ** |
| 2 | **`Krug Rosé`** | **`29ème Édition` / `28ème Édition` / `27ème Édition`** | — |
| 3 | **`Krug Millésime`**（EN: `Krug Vintage`） | **`2013` / `2011` / `2008`** | — |
| 4 | **`Krug Clos du Mesnil`** | **`2009` / `2008` / `2006`** | — |
| 5 | **`Krug Clos d'Ambonnay`** | **`2008` / `2006` / `2002`** | — |
| 6 | **`Krug Collection`** | **`1996` / `1995` / `1990`** | — |

⚠️ **サイトマップにはさらに `krug-clos-dambonnay-rose` / `krug-clos-dambonnay-rose-2008` の 2 URL が存在する。ナビには出ない。**
✅ **`Krug Collection` の定義（公式）: 「`La seconde vie de Krug Millésime.` Un nombre limité de bouteilles de Krug Millésime est conservé dans des conditions idéales dans les caves de la Maison」**

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 3 本。全て `unresolved`**）

🔍 **3 行はいずれも `source_section = "FRANCE | SPARKLING > CHAMPAGNE | BLENDS"`、`source_producer_raw = "Krug"`、`source_vintage_raw = null`、`source_price_raw = 850`。**
🔍 **`_parts` は 3 行とも `label: "Grande Cuvée, NNNème Édition"` / `appellation: ""` / `appellation_display: "Brut"` / `printed_rest: "Brut"` / `style: "brut"` / `varietal: null` / `rank: null` / `flags: []`。**
🔍 **`_collision_risk: "LOW"`。**🔴 **`_parts.label` は **null ではない** ため、本 3 行は `CDX-1`（label-null override）の母集団には入らない。**

| # | `source_row_id` | OBP 印字 | 価格 | intake | 🔴 **実際に何のワインか（✅ 公式による判定）** |
|---|---|---|---|---|---|
| 1 | **`obp-beverage-2026-08:6576a45bb2`** | **`'Grande Cuvée, 173ème Édition,' Brut`** | **$850** | 🔴 **`unresolved`**（`producer_state: exact` / `cuvee_state: unresolved` / `vintage_state: unresolved` / `confidence: 0.0`） | 🔴 ✅ **`Krug Grande Cuvée 173ème Édition`。**<br>🔴 ✅ **`Composée autour des vendanges de 2017`／`un assemblage de 150 vins issus de 13 années différentes`／最も若い vin は `2017`、最も古い vin は `2001`／リザーヴ `31 %`／`44 % de Pinot Noir, 34 % de Chardonnay et 22 % de Meunier`／`plus de 20 ans de travail minutieux`** |
| 2 | **`obp-beverage-2026-08:7ea95401c0`** | **`'Grande Cuvée, 172ème Édition,' Brut`** | **$850** | 🔴 **`unresolved`**（同上） | 🔴 ✅ **`Krug Grande Cuvée 172ème Édition`。公式 `Champagne Notes` PDF が実在（唯一取得できた 1 点）。**<br>🔴 ✅ **`Créée autour des vendanges de 2016`／`146 vins de 11 années différentes`／最若 `2016`、最古 `1998`／リザーヴ `42 %`／`44 % de Pinot Noir, 36 % de Chardonnay et 20 % de Meunier`／`A stay of around seven years in Krug's cellars`／`FORMATS: Bottle (75 cl)`**<br>🔴 ✅ **収穫: 「`Les vendanges marathon se sont déroulées du 9 septembre au 2 octobre`」** |
| 3 | **`obp-beverage-2026-08:b82ab723da`** | **`'Grande Cuvée, 171ème Édition,' Brut`** | **$850** | 🔴 **`unresolved`**（同上） | 🔴 ✅ **`Krug Grande Cuvée 171ème Édition`。**<br>🔴 ✅ **`Créée autour des vendanges de 2015`／`131 vins de 12 années différentes`／最若 `2015`、最古 `2000`／リザーヴ `42 %`／`45 % de Pinot Noir, 37 % de Chardonnay et 18 % de Meunier`** |

#### 🔴 各 Édition の造り手自身の解説（Julie Cavil、公式ページ本文）

| Édition | ✅ Chef de Caves の言葉（verbatim） |
|---|---|
| 🔴 **171ème** | **「`Les Chardonnays et les Meuniers de 2015 étaient un peu sur la retenue`, alors nous nous sommes tournés vers `des années plus fraîches des réserves de notre vinothèque, notamment les récoltes de 2008, 2013 et 2014`, pour apporter `de la vivacité et de la tension` à l'assemblage. … vous trouverez également `des Chardonnays issus d'années plus chaudes et d'une météo capricieuse telles que 2000 et 2006`, qui apportent `de la matière et un côté toasté`. `Les Pinots noirs exceptionnels de 2015` ont été complétés par `une trentaine d'autres expressions` … Enfin, `les Meuniers ont été sélectionnés parmi quatre années de vendanges`」** |
| 🔴 **172ème** | **「… une année aux conditions climatiques si contrastées qu'elles en sont devenues `une caricature du pendule climatique`. `Un printemps extrêmement humide, avec 70 % de précipitations en plus que la norme pour la période entre avril et juin`, a rendu le travail de la vigne difficile et a augmenté le risque de propagation de maladies. Un temps clément s'est installé à partir de la floraison … `suivi par la canicule en fin de maturation`. `Les vendanges marathon se sont déroulées du 9 septembre au 2 octobre`」** |
| 🔴 **173ème** | **「`Les vins plus âgés des années 2000 apportent une patine d'élégance, de rondeur et de générosité à l'assemblage final.`」** |

#### 🔴 「メニュー側は defective か」—— **本件では「否」と言える**

| 問い | 実測による答え |
|---|---|
| 🔴 **`Grande Cuvée, 173ème Édition` は実在する製品名か** | 🔴 ✅ **実在する。公式の製品ページ・グローバルナビ・法定 AGEC 製品シートの 3 系統が `173ème Édition` を並べる。**<br>🔴 **カンマの有無（OBP `Grande Cuvée, 173ème Édition` ⟷ canonical `Grande Cuvée 173ème Édition`）だけが違う。**⚠️ **公式表記は `Krug Grande Cuvée 173ème Édition`（カンマ無し）だが、これは「メニューが誤り」ではなく `CDX-10`（正規化はルールでなく alias で解くべき）の典型例である。** |
| 🔴 **`Brut` は誰の語か** | 🔴 ⚠️ **決まらない。**🔴 **取得した公式 FR/EN ページと 172 Champagne Notes を全文検索して `Brut` は `0 件`。**<br>🔴 **しかし「公式サイトに書いていない」は「ラベルに無い」ではない。**🏛 **EU/仏の表示規則上、発泡性ワインには糖分表示が要る。**<br>🔴 **したがってこれは**実ラベルでしか決着しない**。「メニューが余計な語を足した」と断定してはならない（`D-2026-08-06` の standing caution 1）。** → Open Questions 1 |
| 🔴 **`vintage: NV` は正しいか** | 🔴 **法的には正しい。**🏛 **CDC は millésime 表示を条件付きの任意規定として置いており、Grande Cuvée はそれを使っていない。**<br>🔴 **しかし「NV」は Édition 番号もベース収穫年も捨てる表現であり、**同一価格 $850 の 3 行が区別できなくなる**。これが `CDX-7` / `CDX-8` の実害そのものである。** |
| 🔴 **`unresolved` の原因はどちら側か** | 🔴 **canonical 側でも parser 側でもなく、**マッチャ側**である。**<br>🔴 **canonical には `krug-grande-cuvee-171` / `-172` / `-173` が実在し、`vintage` の base year も公式と一致する。**<br>🔴 **にもかかわらず intake の evidence は「canonical キュヴェ **2 件**」と書く。** → §Canonical Conflict ① |

---

## Staff Notes

### 🔴 芯 3 点（**これだけ言えれば卓上で嘘をつかない**）

🔴 **①「クリュッグのグランド・キュヴェです。番号は『何年ものか』ではなく、**創業以来この champagne が何回目の再創造か**を数える通し番号です。
171、172、173 と数字が上がるほど新しい創造で、それぞれ 2015 年、2016 年、2017 年の収穫を軸に組まれています。」**
**—— ✅ 公式 172 Champagne Notes「`It corresponds to the number of years in the House of Krug the founder's dream has been re-created.`」**
**—— ✅ 公式 `/fr/notre-histoire`「`Il indique combien de fois, dans l'histoire de la Maison, Krug Grande Cuvée ou Krug Rosé ont été recréés.`」**
**—— ✅ 各ページの `Créée / Composée autour des vendanges de 2015 / 2016 / 2017`。**

🔴 **②「1 本のなかに、10 年以上ちがう年のワインが入っています。
173 なら 13 の収穫年から 150 種、いちばん古いのは 2001 年。172 なら 11 年から 146 種、最古は 1998 年。171 なら 12 年から 131 種、最古は 2000 年です。
造り手は『ひとつの年のワインでは絶対に出せない豊かさ』と書いています。」**
**—— ✅ 3 ページとも造り手が数字を明記。**✅ **「une richesse de saveurs et d'arômes `impossible à exprimer avec les vins d'une seule année`」。**

🔴 **③「組み上がったあと、蔵で**最低 7 年**寝かせます。マグナムはさらに 1 年、ジェロボアムは 2 年長くなります。」**
**—— ✅ 公式 `/fr/savoir-faire/patience`「`où elle va reposer pendant sept années au minimum`」／「un Magnum (150cl) `repose une année supplémentaire`, un Jéroboam (300cl) `deux ans de plus`」。**
🔴 **「6 年」と言ってはならない（canonical の値）。**

### ⚠️ 言ってはいけないこと（**must-not-say**）

⚠️ **①「クリュッグのなかで一番上のキュヴェです」／「グランド・キュヴェはスタンダードで、上にクロ・デュ・メニルがあります」。**
🔴 **✅ 公式はワイン間に序列を置かない ——「il a fondé `une Maison où tous les champagnes sont portés au même niveau d'excellence`, d'une qualité incontestée」。**
🔴 **✅ Clos の位置づけも「上位」ではなく「`les solistes de Krug`（独奏者）」であり、Grande Cuvée は「`le full orchestra`」である。**
✅ **安全な言い方 ——「クロは 1 区画・1 品種・1 年のソリスト、グランド・キュヴェはオーケストラ全体、と造り手は言っています。」**

⚠️ **②「マロラクティック発酵はしません」／「ノン・マロです」。**
🔴 **✅ 公式は「`la fermentation malolactique n'est pas provoquée. Toutefois, si celle-ci se produit naturellement, elle n'est pas interrompue.`」と書く。**
🔴 **「誘導しないが、自然に起きたら止めない」であって「しない」ではない。**
🔴 **canonical は 3 レコードすべての `aging` / `tags` / `winemaking` に `No MLF` / `Pas de FML` を書いている。canonical をそのまま読み上げてはならない。**

⚠️ **③「ドサージュは 6 グラムです」。**
🔴 **✅ 公式は「`il n'existe pas de règle concernant le niveau de dosage, mais plutôt une philosophie`」と明言し、数値を一切出していない（`g/L` の全文検索で 0 件）。**
🔴 **canonical の `dosage: "6 g/L"` は出典が確認できない。**
✅ **安全な言い方 ——「クリュッグはドサージュの量に決まりを置かない、と公表しています。アンリ・クリュッグの言葉で『足りなければ気づかれるが、あって気づかれてはいけない』量だ、と。」**

⚠️ **④「オーガニックです」／「ビオディナミです」／「エコセール認証です」（171 / 172 / 173 のボトルについて）。**
🔴 **🏛 Agence Bio の SIRET 完全一致の陽性は `MHCS`（SIREN 509553459）のものであり、`activites` は `Préparation` / `Distribution` / `Importation` の 3 つ。**`Production`（栽培）が無い**。**
🔴 **🏛 `dateEngagement` は `2022-07-02`。3 本のベース収穫（2015 / 2016 / 2017）はいずれもそれ以前である。**
🔴 **🏛 旧法人 `KRUG VINS FINS DE CHAMPAGNE`（SIRET `33558029600010`）は Agence Bio で `nbTotal: 0`（証明された陰性）。**
🔴 **✅ そして Krug 自身が `bio` / `biodynamie` を一度も名乗っていない（公式全ページで 0 件）。**
⚠️ **同時に「オーガニックではありません」とも言ってはならない。**造り手は「`100 % des matières premières … produites selon des normes exigeantes … de respect de l'environnement`」と書いている。**
🔴 **「認証」という語をボトルに結びつけない。**

⚠️ **⑤「農薬を使っていません」。**
🔴 **✅ 公式が書くのは「`exempte d'herbicide ou d'insecticide`」＝**除草剤と殺虫剤**であり、しかも「`*à l'exception des parcelles soumises au traitement obligatoire de la flavescence dorée`」という脚注が付く。**
🔴 **✅ 同じ文が「`utilise exclusivement des engrais organiques, du cuivre et du soufre`」＝**銅と硫黄は使う**と書いている。**
✅ **安全な言い方 ——「除草剤と殺虫剤は使わない栽培です。ただしフラベッセンス・ドレという法定防除の対象区画だけは例外だ、と造り手自身が注記しています。」**

⚠️ **⑥「HQE 認証を取ったビオのシャンパーニュです」。**
🔴 **✅ `HQE`「`niveau exceptionnel`」は **2024 年に開いた醸造施設 `Joseph` という建物**の認証であって、畑の認証ではない。**
🔴 **✅ 場所も Reims ではなく `Ambonnay`（`situé au Clos d'Ambonnay de Krug`）である。**
✅ **公式自身が釘を刺している ——「`Il ne s'agit pas d'accumuler des labels.`」（Isabelle Bui）**

⚠️ **⑦「ランスの畑のシャンパーニュです」／「45 のリュー・ディから造られています」。**
🔴 **✅ Reims にあるのは `La Maison de Famille Krug`（5, rue Coquebert、1868 年から）と歴史的なカーヴ・リザーヴワイン庫であって、ブドウの産地ではない。**
🔴 **✅ ブドウは自社畑と `Cercle des Vignerons Krug`（`une centaine de membres` が `toute l'appellation Champagne` から）の特定区画から来る。「`100 % de nos engagements concernent des parcelles spécifiques`」。**
🔴 **canonical の `terroir` は 3 件とも「45 の厳選リュー・ディから調達」と書くが、`lieu-dit` / `lieux-dits` は公式全ページで 0 件。出典が確認できない。**

⚠️ **⑧「171 は 1971 年のことです」／「番号は蔵で寝かせた年数です」／「番号はロット番号です」。**
🔴 **✅ 番号は「創業以来、何回目の再創造か」を数える通し番号である（芯 ①）。**
🔴 **✅ さらに「`À partir de 2016`」に始まった仕組みであり、「`Jusqu'au milieu des années 2010, les bouteilles … ne portaient pas de numéro d'Édition`」。古いボトルには番号自体が無い。**

⚠️ **⑨「クリュッグのグランド・キュヴェは毎年同じ味を再現しています」。**
🔴 **✅ 公式は逆を書く ——「`Chaque année, l'inspiration reste la même, mais la création est totalement unique et différente.`」（Olivier Krug）**
✅ **安全な言い方 ——「めざすところは毎年同じですが、できあがるものは毎年まったく別物です、と造り手は言っています。」**

⚠️ **⑩「ピノ・ムニエが 22% 入っています」（品種名の綴り）。**
🔴 **✅ Krug は一貫して `Meunier` と書く。**🏛 **INAO の CDC も `Meunier N` である（`Pinot Meunier` という表記は CDC に無い）。**
🔍 **canonical は 3 件とも `"Pinot Meunier NN%"` と書く。比率そのものは公式と一致するので、直すべきは綴りだけである。**
⚠️ **卓上で「ピノ・ムニエ」と言っても通じるが、造り手の表記を尋ねられたら `Meunier` と答える。**

⚠️ **⑪「クロ・デュ・メニルのブドウはグランド・キュヴェには絶対に入りません」。**
🔴 **✅ 公式は逆のことを書いている ——毎年の判断は「`créer un nouveau millésime de Krug Clos du Mesnil, ou intégrer ce vin à l'assemblage des nouvelles Éditions de Krug Grande Cuvée ou Krug Rosé, en y apportant caractère et fraîcheur`」の二択である。**
🔴 **すなわち Clos du Mesnil を単独で出さない年には、その区画のワインが Grande Cuvée / Rosé に入る。**

⚠️ **⑫「サービス温度は 9〜11 度です」。**
🔴 **✅ 公式は 3 ページとも「`entre 9 et 12°C`」と書く。**🔍 **canonical は 3 件とも `9–11°C`。上限が 1 度違う。**
✅ **公式のグラスは `Le Verre Joseph`（2011 年に Riedel と設計）。**🔍 **canonical の `Krug ID glass` という名称は公式に無い。**

⚠️ **⑬「シャンパーニュの法定熟成は 15 か月なので、クリュッグもそのくらいです」。**
🏛 **法定下限は確かに「`quinze mois minimum à compter de la date du tirage`」（非ミレジメ）だが、**
🔴 **✅ Krug 自身の下限は `sept années au minimum` であり、法定の 5 倍以上である。数字を並べるなら両方を並べる。**

### 🔴 追加の一手（**客に訊かれたら強い。すべて公式の言葉**）

🔴 ✅ **「裏ラベルに 6 桁の番号があります。`Krug iD` といって、2011 年から全ボトルに入っています。入力するとそのボトルの composition と、シェフ・ド・カーヴのその年についてのコメントが出ます。」**
**—— `un code à six chiffres apposé sur la contre-étiquette de chaque bouteille Krug`。**

🔴 ✅ **「収穫のあとの半年間、毎朝 11 時ちょうどに試飲委員会が非公開で集まります。ブラインドで、1 日 15 種類まで。年間およそ 5000 のテイスティング・ノートを取ってから、ようやくアッサンブラージュに入ります。」**
**—— `Chaque matin à 11 heures précises` / `à huis clos` / `jamais sur plus de 15 vins par jour` / `environ 5 000 notes de dégustation`。**

🔴 ✅ **「毎年およそ 400 の『個』を味わいます。その年のワインが 250、リザーヴが 150 で、リザーヴは 15 年ぶんくらいの収穫にまたがっています。」**
**—— `environ 400 de ces individualités, dont 250 vins de l'année, et 150 vins de réserve issus de près de 15 années`。**

🔴 ✅ **「1 区画 1 ワインで、小さな**古い**樽で発酵させます。庭くらいの小さな区画も別々に仕込むための道具です。樽は中立で、樽の香りは付けません。」**
**—— `des parcelles aussi petites qu'un jardin` / `de petits fûts de chêne anciens` / `Dans ces fûts neutres`。**

✅ **「ランスの本家は 5 rue Coquebert に 1868 年からあります。1 階の試飲室に『400 のワインの壁（`Mur des 400 Vins`）』があって、毎年オーディションを受ける約 400 のワインへのオマージュです。」**

🔴 ✅ **「クロは 2 つだけです。ル・メニル・シュル・オジェのクロ・デュ・メニルが 1.84 ヘクタールのシャルドネ、アンボネのクロ・ダンボネが 0.68 ヘクタールのピノ・ノワール。アンボネの壁は 1766 年から立っています。」**

🔴 ✅ **「172 は 2016 年が軸で、4〜6 月の雨が平年より 70% 多く、そのあと猛暑が来た年です。造り手は『気候の振り子のカリカチュア』と書いていて、収穫は 9 月 9 日から 10 月 2 日までのマラソンでした。」**
**—— `une caricature du pendule climatique` / `70 % de précipitations en plus` / `du 9 septembre au 2 octobre`。**

🔴 ✅ **「171 は 2015 年のシャルドネとムニエが控えめだったので、2008・2013・2014 という涼しい年のリザーヴを足して緊張感を出した、とシェフ・ド・カーヴが説明しています。」**

🔴 ✅ **「173 は 2000 年代の古いワインが『エレガンスと丸みの艶（`une patine d'élégance`）』を与えている、と。ムニエが 22% とここ数年でいちばん高いエディションです。」**

✅ **「2024 年に Joseph という新しい醸造所ができました。アンボネのクロ・ダンボネにあって、7 年かけて建てたものです。」**

✅ **「創業者の 1848 年の手帳がいまも指針です。『良い要素と良いクリュのワインを使わずに良いワインは造れない』と書かれています。」**

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

🔒 **本節は escalation のみ。`REGISTER.md` は書き換えていない。`migration/` は読み取りのみ。番号の採否は CTO の判断である。**

### 🔍 canonical の実測（`migration/out/export/db_wine_canonical.json`、928 要素）

| 走査 | 結果 |
|---|---|
| **`krug` を含むレコード（全文字列）** | 🔍 **18 件** |
| 🔴 **`producer == "Krug"` のレコード** | 🔴 **13 件** — `krug-grande-cuvee-162` … `-170`（9 件）、`-171`、`-172`、`-173`、`krug-rose-27` |
| 🔍 **prose のみで `krug` に当たるレコード** | 🔍 **5 件** — `cristal-2015` / `dom-perignon-p2-2003` / `dom-perignon-oenotheque` / `alfred-gratien-brut-nv` / `dehours-grande-reserve-brut-nv` |
| 🔴 **別生産者への取り違え** | 🔴 **0 件** |
| 🔴 **canonical の「キュヴェ族」の数** | 🔴 **2**（`Grande Cuvée` ×12、`Rosé` ×1） |

### 🔴 ① 【escalate】マッチャの候補集合が canonical より小さい —— **OBP 3 行が落ちた直接の原因**

1. **conflicting canonical IDs** — `krug-grande-cuvee-171` / `krug-grande-cuvee-172` / `krug-grande-cuvee-173`（および同族 10 件）。
2. **why it looks like a duplicate** — 🔴 **重複ではない。**これは「実在する正しいレコードに、マッチャが到達していない」形である。3 レコードは OBP 3 行の**完全な対応物**であり、`name`（`Grande Cuvée 171ème Édition` 等）も `vintage`（`NV · based on 2015` 等）も公式と一致する。
3. **evidence** — 🔍 intake の evidence は 3 行とも `"'Krug' の canonical キュヴェ 2 件に一致無し: 'Grande Cuvée, 17Nème Édition'"`。🔍 実測は `producer == "Krug"` が **13 件**。🔴 **13 件を `Grande Cuvée` / `Rosé` の 2 族に畳むと `2` になる。**⚠️ **「族の数がレコード数として渡っている」という読みは**仮説**であり、本ドシエは検証していない（`D-2026-08-06-06`）。**⚠️ **intake が別スナップショットの canonical に対して走った可能性も潰していない。**
4. **OBP impact** — 🔴 **3 行 × $850。3 行とも `confidence 0.0` / `cuvee_state: unresolved`。**🔴 **canonical 側に受け皿が完備しているのに 0 行が解決している。**
5. **recommended resolution（実行しない）** — 🔴 **マッチャの per-producer 候補集合の構築を、レコード単位で数え直す。**🔴 **`CDX-1`（label-null override）とは母集団が別である（本 3 行の `_parts.label` は非 null）。**🔴 **`CODEX_TASKS.md` の `### Batch 13 additions` に 1 項目として記録済み。**
6. **confidence** — 🔴 **High**（両側の実測が取れている。原因の**特定**だけが Medium）。

### 🔴 ② 【escalate】格納値の実測 —— **検証可能な 21 主張のうち 7 が失敗**

🔴 **`krug-grande-cuvee-171` / `-172` / `-173` の全フィールドを公式・法令と突き合わせた。**

| # | canonical の主張（3 件共通、断りある場合を除く） | ✅/🏛 の値 | 判定 |
|---|---|---|---|
| 1 | `producer: "Krug"` | ✅ **公式表記と一致** | ✅ **PASS** |
| 2 | `name: "Grande Cuvée 171/172/173ème Édition"` | ✅ **公式は `Krug Grande Cuvée NNNème Édition`** | ✅ **PASS**（producer と結合すれば一致） |
| 3 | `country: "France"` / `region: "Champagne"` | 🏛 **一致** | ✅ **PASS** |
| 4 | `subregion: "Reims"` | ✅ **メゾンの所在としては正しい（`5, rue Coquebert, à Reims, depuis 1868`）** | ⚠️ **PASS（ただし「ブドウの産地」を格納する欄としては誤読を招く。原料はアペラシオン全域）** |
| 5 | `type: "Champagne"` / `color: "Blanc"` | 🏛 **一致** | ✅ **PASS** |
| 6 | 🔴 **`vintage: "NV · based on 2015 / 2016 / 2017"`** | 🔴 ✅ **公式の `vendanges de 2015 / 2016 / 2017` と**完全一致** | 🔴 ✅ **PASS**（🔴 **base year の値そのものは正しい。問題は表記法であって値ではない** → ③） |
| 7 | 🔴 **`grapes` の比率**（171 `45/37/18`、172 `44/36/20`、173 `44/34/22`） | 🔴 ✅ **公式の 3 ページと**すべて一致** | 🔴 ✅ **PASS** |
| 8 | ⚠️ **`grapes` の綴り `"Pinot Meunier"`** | ✅ **Krug は `Meunier`。**🏛 **CDC も `Meunier N`** | ⚠️ **PARTIAL FAIL（比率は正・名称は非公式表記）** |
| 9 | **wine 数・年数・最古年**（171 `131/12/2000`、172 `146/11/1998`、173 `150/13/2001`） | ✅ **公式 3 ページと**すべて一致** | ✅ **PASS** |
| 10 | **リザーヴ比率**（171 `42%`、172 `42%`、173 `31%`） | ✅ **公式と一致** | ✅ **PASS** |
| 11 | 🔴 **`aging` に `(no MLF)`／`tags` に `"No MLF"`／`winemaking` に `Pas de FML`** | 🔴 ✅ **公式は「n'est pas provoquée. `Toutefois, si celle-ci se produit naturellement, elle n'est pas interrompue.`」** | 🔴 **FAIL（2 文目を落として意味が反転している）** |
| 12 | 🔴 **`aging: "… minimum 6 years on lees"`（171・173）** | 🔴 ✅ **公式は `sept années au minimum`** | 🔴 **FAIL（下限が 1 年短い）** |
| 13 | **`aging: "7+ years on lees"`（172 のみ）** | ✅ **172 Champagne Notes の `around seven years` と整合** | ⚠️ **PASS（🔴 ただし同一プロダクト 3 件のあいだで文字列が食い違っている）** |
| 14 | 🔴 **`dosage: "6 g/L"`（3 件とも）** | 🔴 ✅ **公式は「`il n'existe pas de règle concernant le niveau de dosage`」。`g/L` の全文検索は 0 件** | 🔴 **FAIL（出典なし。かつ造り手の方針に反する）** |
| 15 | 🔴 **`terroir`: 「`45 の厳選リュー・ディから調達`」** | 🔴 **`lieu-dit` / `lieux-dits` は公式全ページで 0 件** | 🔴 **FAIL（出典なし）** |
| 16 | **`terroir`: 「Clos du Mesnil (1.84ha, Mesnil-sur-Oger)」** | ✅ **面積・村とも公式と一致** | ✅ **PASS** |
| 17 | ⚠️ **`terroir`: 「Montagne de Reims (PN)、Côte des Blancs (CH)、Vallée de la Marne (PM)」** | ⚠️ **公式はこの 3 対応を書いていない。**🏛 **CDC の地誌節は `la Montagne de Reims, la vallée de la Marne …` を地形として挙げるが、品種の割り当ては書かない** | ⚠️ **UNSOURCED（否定はできないが、公式には無い）** |
| 18 | 🔴 **`serving_temp: "9–11°C"`** | 🔴 ✅ **公式は 3 ページとも `entre 9 et 12°C`** | 🔴 **FAIL（上限が 1 度低い）** |
| 19 | ⚠️ **`glassware: "White Burgundy / Krug ID glass"`** | ✅ **公式が名指しするのは `Le Verre Joseph`（2011 年、Riedel）** | ⚠️ **UNSOURCED（`Krug ID glass` という名称は公式に無い）** |
| 20 | **`winemaking`: 「Fermentation en petits fûts de chêne」** | ✅ **公式「`nos vins prennent naissance dans de petits fûts de chêne anciens`」** | ⚠️ **PASS（🔴 ただし `anciens`／`neutres` が落ちており、「新樽発酵」と誤読されうる）** |
| 21 | **`obp_format: "By the bottle"`（3 件とも）** | ✅ **172 Champagne Notes の `FORMATS: Bottle (75 cl)`**／✅ **AGEC 製品シートは 171・172・173 の `75CL` を列挙** | ✅ **PASS** |

🔴 **失敗 7 件の内訳: 出典なし 3（`6 g/L` / `45 lieux-dits` / — ）・矛盾 3（`No MLF` / `6 years` / `9–11°C`）・表記 1（`Pinot Meunier`）。**
🔴 **注意すべきは、**構造化フィールドのほうが誤っている**という点である（`dosage` / `aging` / `serving_temp` は typed field）。`CDX-5` の「typed が prose に勝つとは限らない」がここでも成立する。**

1. **conflicting canonical IDs** — `krug-grande-cuvee-171` / `-172` / `-173`（および同族 10 件。同じ文字列が使い回されている可能性が高い）。
2. **why it looks like a duplicate** — 🔴 **重複ではない。**同一プロダクトの 3 レコードが**同じ誤りを共有**し、かつ `aging` だけ 172 が違う、という「テンプレート由来のドリフト」の形。
3. **evidence** — 上表 21 件。出典は ✅ `krug.com` FR/EN 13 ページ、✅ 172 Champagne Notes PDF、🏛 CDC「CHAMPAGNE」。
4. **OBP impact** — 🔴 **3 行 × $850。**🔴 **canonical をそのまま卓上に流すと、`No MLF` / `6 g/L` / `6 years` / `45 lieux-dits` の 4 つの嘘が出る。**
5. **recommended resolution（実行しない）** — 🔴 **`CDX-5` の read-only sweep 母集団に Krug 13 件を含める。**🔴 **`No MLF` は `tags` にも入っているため、タグ語彙の側も点検が要る。**
6. **confidence** — 🔴 **High**（21 件すべて一次資料と 1 対 1 で突き合わせた）。

### 🔴 ③ 【記述のみ・番号を開かない】`vintage` の表記 —— `CDX-7` / `CDX-8`

🔍 **Krug 13 件の `vintage` 値は 2 通りある。**

| 表記 | 件数 | 例 |
|---|---|---|
| **`NV · based on <YYYY>`** | **12** | `krug-grande-cuvee-162` … `-173` |
| ⚠️ **`NV · blend 2005–2015`** | **1** | `krug-rose-27` |

🔴 **前者の**値**は公式と一致する（本ドシエ ② の #6）。すなわち Krug においては「情報が正しく入っているのに、入れ物が悪い」。**
⚠️ **後者は base year ではなく**範囲**であり、`CDX-7` が数えた 5 表記のいずれとも形が違う。**
🔴 **本ドシエは番号を開かない。`CDX-7` / `CDX-8` を引くにとどめる（`D-2026-08-06-06`）。**

🔴 **`CDX-8` の警告「`Grande Cuvée` は Krug のキュヴェ名である。Laurent-Perrier の `Grande Cuvée No. 26` → `Itération Nº26` 正規化ルールを書いてはならない」は、本ドシエの実測で裏づけられた ——
✅ **Krug の公式ナビ・製品ページ・法定 AGEC シートの 3 系統すべてが `Grande Cuvée` を Krug 自身のワイン名として使っている。**

### ⚠️ ④ 【記述のみ】`krug-grande-cuvee-162` の「初のナンバリング」主張

🔍 **canonical `krug-grande-cuvee-162` の `obp_note` は「`エディションナンバー表記の第一号（162ème）`」、`obp_note_en` は「`The first numbered edition (162ème)`」、`tags` に `"First Numbered Edition"` を持つ。**
✅ **公式が書くのは「`À partir de 2016`, la Maison Krug attribue un numéro d'Édition …」という**年**だけで、**どの Édition が最初か**を書いていない。**
✅ **公式 162ème ページ本文にも「初」に相当する記述は無い（`premier` / `première` を検索して該当なし）。**
⚠️ **すなわちこの主張は**公式で確認も否定もできない**。**🔴 **卓上で「162 が最初のナンバリングです」と断定してはならない。**
🔴 **本ドシエは番号を開かない。OBP 3 行に影響しないためである（162 は OBP に無い）。**

### 🔍 ⑤ 【gap・conflict ではない】canonical に無いもの

🔴 **`D-2026-08-05-14`（Abreu 先例）の方針どおり、`不在` は conflict ではなく gap として記録する。**

- 🔍 **`Krug Millésime` / `Krug Clos du Mesnil` / `Krug Clos d'Ambonnay` / `Krug Collection` のレコードは canonical に **0 件**。**
- 🔍 **`Krug Rosé` は `krug-rose-27` の 1 件のみ（公式は 17ème 〜 30ème を掲載）。**
- 🔍 **`Grande Cuvée` は `162` 〜 `173` の 12 件で、`161` 以下と `174`（現行）が無い。**
- 🔴 **いずれも OBP 3 行には影響しない。gap として記録するにとどめる。**

---

## Sources

### 🔴 ✅ サイト真正性の事前チェック（`D-2026-08-05-09`）

| ドメイン | 判定 | 根拠 |
|---|---|---|
| ✅ **`www.krug.com`** | ✅ **採用** | ✅ **`/fr/mentions-legales` が `MHCS` / `509 553 459 RCS Reims` / `FR 44 509 553 459` / `9 Avenue de Champagne 51200 EPERNAY` / `Directeur de publication : Mélanie Boury` を明示。**<br>🏛 **企業登録の SIREN `509553459`・TVA `FR44509553459`・本店住所と完全一致。**<br>🔴 ✅ **加えて `décret 2022-748`（loi AGEC）の法定製品シートを実 SKU 名で掲載しており、これは製造者・輸入者・販売者にしか負えない義務である。**<br>⚠️ **相互リンク（条件 b）は取得できなかった。**⚠️ **年齢確認ゲート・bot チャレンジには遭遇していない（回避行為なし）。** |
| ⚠️ **`www.lvmh.com/en/houses/wines-spirits/krug`** | ⚠️ **到達せず** | **`HTTP 404`。内容不使用。** |
| ⚠️ **`www.moethennessy.com/en/our-maisons/krug/`** | ⚠️ **却下（内容不使用）** | **`HTTP 200` だが、返る HTML は JS 描画前のシェル。`<title>` が `LVMH, leader mondial des produits de haute qualité`、`krug.com` の出現 0 回。**🔴 **相互リンクの証拠としては使えない。** |
| ⚠️ **`extranet.inao.gouv.fr/fichier/CDCChampagne.pdf` / `…/CDC-Champagne.pdf`** | ⚠️ **却下** | **`HTTP 200` だが `Content-Type: text/html`（PDF ではない soft-404）。内容不使用。** |
| ⚠️ **`www.krug.com/…/Champagne-Notes_Krug-Grande-Cuvee-{170,171,173,174}eme-Edition.pdf`** | ⚠️ **不在** | **4 本とも `HTTP 404`（HTML 本文が返る）。**🔴 **キャッシュから削除済み。内容は一切使用していない。** |
| ❌ **小売／オークション／評論家／アグリゲータ** | ❌ **一切不使用** | **本調査は 1 語も使っていない。** |
| ❌ **Wikipedia** | ❌ **不使用** | — |

### ✅ 公式サイト（`https://www.krug.com/fr/`、FR 原本）

- ✅ `robots.txt` → `sitemap.xml`（sitemapindex 2 ページ）→ **URL 2,827 件**（ロケール `en-int` 324 / `en-us` 314 / `en-hk` 314 / `en-gb` 314 / `ja` 313 / `fr` 313 / `ko` 312 / `it` 311 / `de` 311）
- ✅ `/fr/mentions-legales`（🔴 **MHCS / RCS / TVA / 資本金 / 本店 / 掲載責任者 / ホスティング**）
- ✅ `/fr/notre-histoire`（🔴 **1843 / 1848 の手帳 / 1970 年代前半 / 1976 / Krug iD 2011 / 番号 2016〜 / Joseph 2024**）
- ✅ `/fr/savoir-faire`（🔴 **3 本の柱・Julie Cavil の哲学**）
- ✅ `/fr/savoir-faire/individualite`（🔴 **古い小樽・MLF・soutirage à la fontaine・1971 / 1698 / 1991 / 1766・NOS ENGAGEMENTS DURABLES・Cercle des Vignerons Krug**）
- ✅ `/fr/savoir-faire/art-de-lassemblage`（🔴 **毎朝 11 時・1 日 15 種まで・年 5000 ノート・Comité de Dégustation**）
- ✅ `/fr/savoir-faire/patience`（🔴 **最低 7 年・Magnum +1 / Jéroboam +2・ドサージュの哲学・Éric Lebel / Henri Krug**）
- ✅ `/fr/nos-lieux-emblematiques`（🔴 **5 rue Coquebert 1868・Mur des 400 Vins・La Loge 2023 Trépail・Clos 2 件の面積・Joseph の HQE**）
- ✅ `/fr/krug-grande-cuvee`（総論・最新 Édition・レンジ 6 種の定義）
- ✅ `/fr/champagne/krug-grande-cuvee-171eme-edition`（🔴 **OBP 3 行目**）
- ✅ `/fr/champagne/krug-grande-cuvee-172eme-edition`（🔴 **OBP 2 行目**）
- ✅ `/fr/champagne/krug-grande-cuvee-173eme-edition`（🔴 **OBP 1 行目**）
- ✅ `/fr/champagne/krug-grande-cuvee-174eme-edition`（現行。比較用。⚠️ **FR ページの本文が英語のまま**）
- ✅ `/fr/champagne/krug-grande-cuvee-162eme-edition`（④ の検証用）
- ✅ `/fr/krug-id`（🔴 **6 桁コード**）／✅ `/fr/conservation-service`
- 🔴 ✅ `/fr/fiche-produit-des-qualites-et-caracteristiques-environnementales`（🔴 **`décret 2022-748 du 29 avril 2022`（loi AGEC 13-I 条）に基づく法定製品シート。`GRANDE CUVEE 75CL EDITION 171 / 172 / 173` を含む実 SKU を列挙**）
- ✅ `/en-int/krug-id` / `/en-int/craftsmanship/individuality` / `/en-int/craftsmanship/patience` / `/en-int/our-story`（🔴 **FR との差の確認用。採用は FR。ただし `copper sulphate` の差を §Farming に記録**）

### ✅ 公式 `Champagne Notes` PDF

| ファイル | 対象 | 実体 |
|---|---|---|
| ✅ **`Champagne-Notes_Krug-Grande-Cuvee-172eme-Edition.pdf`** | 🔴 **OBP 2 行目（172ème Édition）** | **`%PDF` 実体・PDF 1.7・1 頁・155,412 B。**🔴 **Édition 番号の定義・`around seven years`・`FORMATS: Bottle (75 cl)`・EN のテイスティングノート** |

⚠️ **171 / 173 / 174 / 170 について同一命名規則の URL を試したが 4 本とも `404`。取得できたのはこの 1 点のみ。**

### 🏛 公的登録・規制一次資料

| 出典 | 取得内容 |
|---|---|
| 🏛 **`recherche-entreprises.api.gouv.fr/search?q=509553459`** | 🔴 **SIREN `509553459` / `M H C S` / 本店 SIRET `50955345900033` / `9 AVENUE DE CHAMPAGNE 51200 EPERNAY` / NAF `11.02A` / TVA `FR44509553459` / `nature_juridique 5599` / `etat_administratif A` / `date_creation 2008-12-12` / 17 事業所（12 開設）/ `est_bio: true` / `dirigeants` に `MOET HENNESSY`・`MOET HENNESSY INVESTISSEMENTS`・`SOCIETE JAS HENNESSY & CO`・`FORVIS MAZARS SA`** |
| 🏛 **同 `?q=KRUG&departement=51`** | 🔴 **7 件。`KRUG VINS FINS DE CHAMPAGNE`（SIREN `335580296`、`5 RUE COQUEBERT 51100 REIMS`、`date_creation 1955-01-01`、`date_fermeture 2009-12-31`）ほか 6 件はすべて別法人（`CDX-9` の実測）** |
| 🏛 **同 `?q=KRUG VINS FINS DE CHAMPAGNE`** | 🏛 **事業所 2 件（`33558029600010` Reims / `33558029600028` Paris 16）。両方 `etat F`、`date_fermeture 2009-12-31`** |
| 🔴 🏛 **`opendata.agencebio.org/api/gouv/operateurs/?siret=50955345900033`** | 🔴 **`nbTotal: 1`。`numeroBio 18379` / `Ecocert France` / `ENGAGEE` / `dateEngagement 2022-07-02` / `datePremierEngagement: null` / `activites: Préparation, Distribution, Importation`（**`Production` 無し**）/ 証明 URL `certificat.ecocert.com/entreprise/C2CCD7D5-1887-4BA7-8217-84A5F38B6602`** |
| 🔴 🏛 **同 `?siret=33558029600010`** | 🔴 **`nbTotal: 0` —— exact-SIRET による**証明された陰性**（`CDX-9`）** |
| 🔴 🏛 **`info.agriculture.gouv.fr/gedei/site/bo-agri/document_administratif-3b36a01e-8edd-4742-ade7-fbd3251816c4/telechargement`** | 🔴 **AOC「CHAMPAGNE」CDC（`homologué par l'arrêté du 30 novembre 2022, publié au JORF du 10 décembre 2022`。BO du MASA 2022-12-15）。`%PDF` 実体・PDF 1.5・26 頁・954,359 B。**<br>🔴 **品種（`Arbane B, Chardonnay B, Meunier N, Petit meslier B, Pinot blanc B, Pinot gris G, Pinot noir N` + `Voltis B`）／`grand cru` 17 コミューン／`premier cru` コミューン／`dégorgement` 12 か月／非ミレジメ `15 mois` / ミレジメ `36 mois`** |
| ⚠️ **Légifrance `JORFTEXT000049041513`（2024-01-25）/ `JORFTEXT000052045089`（2025-07-31）** | ⚠️ **AOC「CHAMPAGNE」の後続 homologation が存在することのみ確認。**🔴 **テキストは未取得。本ドシエの CDC 引用はすべて 2022 年版である。** → Open Questions 6 |
| 🏛 **`geo.api.gouv.fr/communes/51454`** | **`{"nom":"Reims","code":"51454","codesPostaux":["51100"],"anciensCodes":["51401"]}`** |
| 🏛 **`geo.api.gouv.fr/communes?nom=…&departement=51`** | **`Le Mesnil-sur-Oger` `51367` / CP `51190`；`Ambonnay` `51007` / CP `51150`；`Trépail` `51580` / CP `51380`** |

### 🔍 THÉSEUS 内部

- 🔍 `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行中 `Krug` 3 行）
- 🔍 `migration/out/export/db_wine_canonical.json`（928 要素。**読み取りのみ**）
- 🔍 `docs/state/CODEX_TASKS.md`（`CDX-1` / `CDX-5` / `CDX-7` / `CDX-8` / `CDX-9` / `CDX-10` を引用。`### Batch 13 additions` に 1 項目を追記）

**キャッシュ先**: `research/producers/_sources/krug/`（gitignored、`D-2026-08-05-02`）
`robots.txt` / `sitemap.xml` / `sitemap_{1,2}.xml` / `urls.txt` / `mentions_legales.{html,txt}` /
`site/fr_*.{html,txt}`（FR 13 ページ）／`site/en_*.{html,txt}`（EN 4 ページ）／
`fiche_172.{pdf,txt}` / `cdc_champagne.{pdf,txt}` /
`krug_siren_51.json` / `krug_vfc.json` / `mhcs.json` / `mhcs_siren.json` / `mhcs_full.json` / `coquebert.json` /
`agencebio_mhcs_siege.json` / `mh_krug.html`

---

## Confidence

```
reached_70: YES (~86%)
confidence: High
```

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🔴 **サイト発行者の法人・RCS・SIRET・TVA・資本金・掲載責任者が mentions légales で確定し、🏛 企業登録と完全一致。**🔴 **旧法人 `KRUG VINS FINS DE CHAMPAGNE`（1955–2009）を SIREN で特定。**🔴 **`?q=KRUG&departement=51` の 7 件を全件突き合わせ、`CDX-9` の substring 罠を潰した。**⚠️ **法人格の表記（`SCS` ⟷ `nature_juridique 5599`）と、MHCS ⟷ Krug の内部的な関係だけが未確定** |
| **Overview** | **High** | ✅ **`savoir-faire` の 3 本柱と Grande Cuvée の自己規定が、すべて一次で verbatim 取得できた** |
| 🔴 **History** | 🔴 **Medium-High** | ✅ **1843 / 1848 / 1868 / 1876 / 1971 / 1976 / 1979 / 1991 / 1995・2007 / 2004 / 2011 / 2016 / 2017 / 2023 / 2024 の 15 点を公式で確定。**⚠️ **2 代目〜4 代目が不在。**⚠️ **旧法人と現行法人の接続（1955 / 2009 / MHCS）が公式沿革に無い** |
| 🔴 **Location** | 🔴 **High** | 🔴 **🏛 コミューン 4 件を `geo.api.gouv.fr` で INSEE コードまで確定。**🏛 **CDC で `Le Mesnil-sur-Oger` / `Ambonnay` が grand cru 併記コミューン、`Trépail` が premier cru 併記コミューンであることを確認。**✅ **Clos 2 件の面積と壁の年を公式で確定。**🔴 ⚠️ **自社畑の総面積だけが公式に無く、そこが埋まらない** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **✅ 造り手の記述（herbicide/insecticide・engrais organiques・cuivre et soufre・enherbement・haies・ISO 4 種・HQE）を verbatim で確定。**🔴 **🏛 Agence Bio を SIRET 完全一致で陽性 1・陰性 1 まで実測し、`activites` に `Production` が無いことを確認。**🔴 **その 2 つを突き合わせて、OBP 3 本すべてに「認証を結びつけない」線を引き切った。**⚠️ **FR/EN の `cuivre et soufre` ⟷ `copper sulphate` の差だけが未解決** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **古い小樽・MLF の 2 文・soutirage à la fontaine・ステンレス小槽・毎朝 11 時/15 種/5000 ノート・400 個体（250+150）・最低 7 年・フォーマット加算・ドサージュの方針が、すべて公式 verbatim。**⚠️ **発酵温度・酵母・樽容量・度数・生産本数が全面的に不在** |
| **Style** | **Medium-High** | ✅ **3 Édition の公式テイスティング・ノートと造り手コメントを全文取得。**🔴 ⚠️ **171 と 172 の FR ページが**同一のノート**を掲げており、172 は Champagne Notes（EN）を採るしかない** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **ブリーフの中核 3 問（Édition 番号の意味・3 本の base vintage・造り手の識別子）を**すべて公式 verbatim で確定**。**🔴 **171/172/173 の wine 数・年数・最古年・リザーヴ比率・品種比率を 1 本ずつ確定。**🔴 **公式レンジ 6 種を確定。**⚠️ **`Brut` の表示だけが未決着** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **21 主張を 1 件ずつ検証して 7 の失敗を確定。**🔴 **canonical 13 件 ⟷ intake「2 件」の食い違いを両側実測で示した。**⚠️ **その**原因**の特定は Medium（仮説にとどめ、`D-2026-08-06-06` に従って追わなかった）** |
| **Staff Notes** | 🔴 **High** | 🔴 **芯 3 点＋ must-not-say 13 項目。canonical をそのまま読むと出る 6 つの嘘（No MLF / 6 g/L / 6 years / 45 lieux-dits / 9–11°C / Krug ID glass）と、現場で出やすい 7 つを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を超過。実感としては 86% 前後）。** | **OBP 3 行すべてについて、造り手の正式名・Édition 番号の意味・ベース収穫年・ブレンドの構成本数と年数・最古リザーヴ・品種比率・熟成下限・提供温度・食事合わせを、公式の言葉でそのまま言える。**<br>**栽培は「造り手は何と言っているか」と「登録は何を保証しているか」を分けて述べたうえで、3 本すべてに認証を結びつけない安全な線が引けている。**<br>**欠けているのは ① `Brut` を含む実ラベルの法定表示、② 自社畑の面積、③ 醸造の分析値、④ 172 以外の Champagne Notes。**<br>**②③④ は「言わない」で回避でき、① は物理ラベルで決着する。卓上で嘘をつく経路は塞いである。** |

---

## Open Questions

1. 🔴 **【物理ラベル・タスク】OBP 3 本の実ラベルの記載事項。**
   🔴 **確認すべきは 4 点 —— ① 表ラベルの `Brut`（または他の糖分表示）の有無と綴り。**取得した公式 FR/EN ページと 172 Champagne Notes に `Brut` は `0 件`だが、これは「ラベルに無い」証明ではない**。
   🔴 **② 表ラベルの `Édition` 番号の刷り方（✅ 公式は「`visible sur l'étiquette`」としか書かない）。③ 裏ラベルの `Krug iD` 6 桁の位置。④ ベース収穫年がラベルに刷られているか（公式サイトにはあるが、ラベル表示の記述は無い）。**
   🔴 **これが埋まると、`CDX-7` / `CDX-8` の surrogate key 議論に「造り手が実際に印字している識別子は何か」という物証が入る。**

2. ⚠️ **`KRUG VINS FINS DE CHAMPAGNE`（🏛 SIREN 335580296、1955-01-01 設立・2009-12-31 閉鎖）と現行の `MHCS` の関係。**
   🏛 **旧法人の本店は `5 RUE COQUEBERT 51100 REIMS` ＝ ✅ 公式が今も `La Maison de Famille Krug` と呼ぶ住所である。**
   ⚠️ **統合・吸収の形式（TUP / fusion / 単純閉鎖）は登録からは決まらない。**⚠️ **公式沿革はこの件について一語も書かない。**
   🔴 **canonical の `producer: "Krug"` を法人にひもづける日が来たら、この対応を先に決める必要がある。**

3. 🔴 **Krug 自身の栽培面積（ha）と区画数。**
   **公式で ha が出るのは `Clos du Mesnil 1,84 ha` と `Clos d'Ambonnay 0,68 ha` の 2 つだけ。自社畑の総面積・村別内訳・区画数はどこにも無い。**
   ⚠️ **`Cercle des Vignerons Krug` は「`une centaine de membres`」とあるが、名簿も、自社畑と Cercle 畑の比率も公表されていない。**

4. ⚠️ **Édition 番号を最初に付けたのは何番の Édition か。**
   ✅ **公式は「`À partir de 2016`」という年しか書かない。**🔍 **canonical `krug-grande-cuvee-162` は `First Numbered Edition` と断定するが、公式で確認も否定もできない。**
   ⚠️ **決着するのは ① 造り手への直接照会、② 162ème と 161ème の実ラベル比較のいずれか。**

5. ⚠️ **栽培の細部。**
   ⚠️ **① 有機・ビオディナミの取得意思の有無（公式は `viticulture durable` としか言わない）。② 銅の年間使用量。③ 被覆作物の草種。④ `Cercle des Vignerons Krug` の会員に課される具体的な栽培基準と、その遵守をだれが監査するか。**
   ⚠️ **⑤ FR の `cuivre et soufre`（銅と硫黄）と EN の `copper sulphate`（硫酸銅）のどちらが正しいか。**

6. ⚠️ **AOC「CHAMPAGNE」CDC の最新版。**
   **本調査は `arrêté du 30 novembre 2022`（BO du MASA 2022-12-15）版を取得した。**
   ⚠️ **Légifrance に `arrêté du 25 janvier 2024`（`JORFTEXT000049041513`）と `arrêté du 31 juillet 2025`（`JORFTEXT000052045089`）による後続 homologation が存在する。テキストは未取得。**
   🔴 **本ドシエが引く条文（品種・grand cru コミューン・熟成月数）は 2022 年版のものである。数を引用する場合は版を明示すること。**

7. ⚠️ **公式プレス素材（未取得）。**
   **`/fr/password/view.press.listing?destination=/en-int/press` は認証ゲートの向こう側にある。**🔴 **回避行為は行っていない（`gated` と記録する。これは不在の証拠ではない）。**
   ⚠️ **171 / 173 の `Champagne Notes` PDF はここにある可能性が高い。**

8. ⚠️ **公式 FR ページの内部不一致（2 件）。**
   🔴 **① `171ème` と `172ème` の FR ページのテイスティング・ノートが**一字一句同一**である。**🔴 **一方 172 の公式 Champagne Notes（EN）は別内容を書く。造り手側の更新漏れと読めるが、断定しない。両論を保存してある。**
   ⚠️ **② `/fr/champagne/krug-grande-cuvee-174eme-edition` の本文が**英語のまま**（`Composed around the harvest of 2018…`）。174 は OBP に無いため本ドシエの記述には使っていない。**

9. ⚠️ **`Krug iD` の 6 桁コードの意味論。**
   ✅ **公式は「ボトルの物語・composition・サービス提案が出る」としか書かない。**
   ❓ **6 桁が ① ボトル固有の連番なのか、② ロット（Édition × dégorgement）単位のキーなのかは公表されていない。**🔴 **`CDX-8` の surrogate key 議論に直結するが、本ドシエは追わない（`D-2026-08-06-06`）。**

10. ⚠️ **MHCS の 17 事業所のうち、Krug の Reims / Ambonnay の施設に対応する SIRET。**
    🏛 **`?q=COQUEBERT&code_postal=51100` は 246 件を返すが、上位 10 件に MHCS の事業所は現れない（ページング未走査）。**
    ⚠️ **これが特定できれば、Agence Bio の SIRET 完全一致を「Krug の施設」の粒度で問い直せる。**🔴 **`CDX-9` が求める SIRET 粒度の議論そのものであり、本ドシエは踏み込まない。**
