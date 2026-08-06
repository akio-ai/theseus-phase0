# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> **reached_70: YES (~88%) / confidence: High**
> 🔍 **canonical にこの生産者のレコードは 3 件**（`haut-brion-1855` / `haut-brion-1993` / `haut-brion-1987`）。
> 🔍 **`producer` フィールド一致 3 件 / prose のみの部分文字列一致 20 件**（`D-2026-08-05-08` の誤検出源。§Canonical Conflict ⑥）。
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト `haut-brion.com`（造り手自身）／公式フィッシュ・テクニック PDF／公式ボトルショットのラベル面**
> `✅g` **`domaineclarencedillon.com`（グループ site。編集責任者は同一法人だが、城ではなくグループの筆致）**
> `🏛` **公的登録**（`recherche-entreprises.api.gouv.fr` / Agence Bio / INAO 官報 CDC）
> `📄` **Internet Archive に残る造り手自身の旧ページ**
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出 ／ `❓` 未解決
> `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://www.haut-brion.com/`（FR 原本）**
> 走査元: **`sitemap_index.xml` → `wine-sitemap.xml`（赤 1989–2025・白 1990–2025・Le Clarence 2007–2025・La Clarté 2009–2025）＋ `gammes-sitemap.xml`（4 レンジ）＋ `page-sitemap.xml`（20 URL）**
> 併用: ✅ **公式フィッシュ・テクニック 8 点（FR 6 / EN 2。全点 `%PDF` 実体・テキストレイヤーあり）**
> 併用: ✅ **公式ボトルショット 11 点（1989 / 1990 / 1993 / 1997 / 2000 / 2003 / 2004 / 2005 / 2008 / 2011 / 2015 / 2018 / 2019 赤＋2019 白）のラベル面を実読**
> 併用: 🏛 **INAO 消費者向け正本 CDC「PESSAC-LÉOGNAN」（arrêté du 10 décembre 2024・JORF 2024-12-12・BO agri 2024-12-19）**
> 🔍 **OBP 側の走査対象は 2 層。混同しないこと ——**
> 🔍 **intake 層 = `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行。`match_state` / `confidence` / `source_quality_flags` / `_parts` を持つ唯一の artifact。`coverage.py` の算出元）**
> 🔍 **store 層 = `research/out/t-01/{inventory,mapping}.json` / `research/store/t-01/shells.json`（別スキーマ。`match_state` / `confidence` を持たない）**
>
> ---
>
> 🔴 **① canonical の `classification = "1855 Médoc Classification · 1er Grand Cru Classé"` は事実として誤りである。三層すべてで否定された。**
> 🏛 **INAO の正本 CDC はこの格付を「`le classement des vins de Bordeaux de 1855`」と呼ぶ。**
> ✅ **城自身の沿革は「`la Classification des Vins de la Gironde en 1855`」と呼ぶ。**
> ✅ **そして実ラベル（1989/1990/1993/2003）は「`Premier Grand Cru Classé en 1855`」としか刷っていない。**
> 🔴 **どこにも `Médoc` の語は無い。しかも同じレコードの `description` 自身が「メドック以外から選ばれた唯一の城」と書いており、レコードは自分自身と矛盾している。** → §Canonical Conflict ①
>
> 🔴 **② AOC ペサック＝レオニャンは `décret du 9 septembre 1987` で創設された。1987 年産のブドウはその後に収穫されている。**
> 🏛 **INAO 正本 CDC:「`initialement reconnue par le décret du 9 septembre 1987`」。**
> 📄 **造り手の旧ページ（Wayback 1997 年捕捉）が 1987 年の収穫日を「`28 sept.-13 octobre`」と記録している。すなわち収穫は政令の 19 日後に始まった。**
> 🔴 **したがって 1987 年産がこの AOC を名乗ることは法的に可能である。だが「実際に 1987 のラベルにそう刷ってあるか」は未確認である。公式が持つ最古のラベル画像は 1989 で、それには `Appellation Pessac Léognan Contrôlée` が刷られている。** → §Location・Open Questions 1
>
> 🔴 **③ ラベルの書式は 2004 年ヴィンテージで断絶している。OBP 6 行はこの断層をまたいでいる。**
> ✅ **〜2003: `CHATEAU HAUT-BRION` / `<年>` / `CRU CLASSÉ DE(S) GRAVES` / `Pessac-Léognan` / `Appellation Pessac-Léognan Contrôlée` / `Premier Grand Cru Classé en 1855`**
> ✅ **2004〜: `CHATEAU HAUT-BRION` / `Premier Grand Cru Classé` / `<年>` / `Domaine Clarence Dillon Propriétaire` —— これだけ。**
> 🔴 **すなわち 2011・2015・2018・2019 の表ラベルには `Pessac-Léognan` の 6 文字が一度も現れない。それでも OBP はこの 4 行に `Pessac-Léognan` と印字している。**
> 🔴 **メニューが間違っているのではない。メニューは AOC を書いており、それは正しい。表ラベルが AOC を裏に回しただけである。** → §Important Cuvées
>
> 🔴 **④ 造り手自身の公式資料の内部で、2018 と 2019 のセパージュが食い違っている。媒体で割れている。**
> ✅ **HTML（FR・EN 両方）: 2018 = `Cabernet franc 11,9 % / Cabernet sauvignon 38,7 %`。2019 = `Cabernet franc 8,1 % / Cabernet sauvignon 43,2 %`。**
> ✅ **フィッシュ・テクニック PDF（FR・EN 両方）: 2018 = `Cabernet Sauvignon : 11,9 % ; Cabernet Franc : 38,7 %`。2019 = `Cabernet Sauvignon : 8,1 % ; Cabernet Franc : 43,2 %`。**
> 🔴 **2 つのカベルネの数値が入れ替わっている。どちらも合計 100.0% になるので算術では決まらない。PDF 抽出のアーティファクトではない（`-bbox-layout` で語の座標を実測し、別行に別々に置かれていることを確認した）。**
> 🔴 **2011・2015・1993 では両媒体が完全に一致する。ずれているのは 2018 と 2019 だけである。** → §Winemaking
>
> 🔴 **⑤ canonical の `grapes` は 1993 で実測と矛盾し、しかも 2 レコードに byte 同一で複製されている。**
> **canonical `haut-brion-1993` = `CS 45% / Merlot 37% / CF 18%`。**
> ✅ **公式 1993 = `Merlot Noir : 53 % ; Cabernet Sauvignon : 29 % ; Cabernet Franc : 18 %`（HTML とフィッシュで一致）。**
> 🔴 **メルロが 37 と 53 で 16 ポイント、CS が 45 と 29 で 16 ポイント違う。主要品種が入れ替わっている。**
> 🔴 **そして同じ配列が `haut-brion-1855` にも入っている。Batch 10 の Roederer 型（1 文字列を多数レコードへ複製）が、ここでは typed field に現れた。** → §Canonical Conflict ②
>
> 🔴 **⑥ 「ワイン名が印字されていない」という事実を、intake は正しく検出し、matcher が上書きし、store が潰す。3 層でそれぞれ別のことが起きている。**
> 🔍 **検出**: `obp_intake_normalized_20260804.json` の 6 行はすべて **`_parts.label: null`**（＝パーサは「ラベル語が無い」と正しく判定している）。
> 🔍 **上書き**: にもかかわらず同じ 6 行が **`proposed_canonical_cuvee: "Château Haut-Brion"` / `cuvee_state: "exact"`** を持ち、evidence 行に
> **「`名称トークン集合一致: 'pessac leognan' ≡ 'Château Haut-Brion'`」** と書く。🔴 **この 2 つのトークン集合は 1 語も共有していない。**
> 🔍 **潰し**: `research/store/t-01/shells.json` の `rs:pro:7e4577c3f98cf640` が、2019 の行を `source_transcription` とし残る 5 行を `source_lines` に束ね、
> `canonical` は `{producer_id: producer:chateau-haut-brion}` のみ（cuvée なし・vintage なし）、`excluded_from_recommendations: true`。
> 🔴 **すなわち store 層は空の `product_name` を正しく保存しており、潰しているのは shell の identity key に vintage が無いことである。** → §Canonical Conflict ⑤（未採番）
>
> ⚠️ **調査上の制約**
> **① 1987 について造り手の現行サイトは何も持たない。**ヴィンテージページ・フィッシュ PDF ともに HTTP 404。赤の公式アーカイヴは **1989 が最古**である。
>    🔴 **これは「六形」のうち「site frozen at an old vintage」ではなく「publishing archive begins later than the bottle」型である。**
>    📄 **Wayback の 1997 年捕捉が気候・収穫日・生産量を持つが、セパージュは持たない。** → Open Questions 2
> **② Agence Bio は SIRET 完全一致 7 件すべてに `{"nbTotal":0,"items":[]}` を返した。**有効な陰性である。→ §Farming
> **③ 1959 年グラーヴ格付の原典（arrêté）そのものには到達できなかった。**INAO 正本 CDC がその存在と件数（16 軒）を明記しているので、事実は 🏛 で確定しているが、**白が格付に含まれるかは確定していない。** → Open Questions 4

---

## Identity

| | |
|---|---|
| **OBP 印字** | **`Haut-Brion`**（producer_heading）／**`Pessac-Léognan`**（classification_text）／**`product_name` は空文字** |
| **公式表記（ワイン名）** | ✅ **`Château Haut-Brion Rouge` / `Château Haut-Brion Blanc`**（サイトのレンジ名）<br>✅ **ラベル面は `CHATEAU HAUT-BRION`（1990〜）／`CHATEAU HAUT BRION`（1989 はハイフン無し）** |
| 🔴 **法人（公式・mentions légales）** | ✅ **`DOMAINE CLARENCE DILLON S.A.S.`**<br>**`Société par Actions Simplifiée au capital de 2 179 400 Euros`／siège `Paris 75008 – 31, Avenue Franklin D. Roosevelt`／`RCS Paris n° B 572 179 026`／`représentée par Philippe Vidal`** |
| 🔴 **法人（🏛 公的登録）** | 🏛 **SIREN `572179026`／`nom_complet: DOMAINE CLARENCE DILLON`／`nature_juridique 5710`（SAS）／`date_creation: 1957-01-01`／`activite_principale 01.21Z`（ブドウ栽培）／`etat_administratif: A`／TVA `FR64572179026`**<br>🔴 **公式の RCS 番号と公的登録の SIREN が完全一致した（真正性チェック合格）。** |
| 🔴 **SIRET（本件の城）** | 🏛 **`57217902600024` — `liste_enseignes: ["CHATEAU HAUT BRION"]`／住所 `CHATEAU HAUT BRION 133 AVENUE JEAN JAURES 33600 PESSAC`／`date_creation 1995-04-01`／NAF `01.21Z`／稼働中** |
| 🔴 **SIRET（同 SIREN の他事業所）** | 🏛 **`57217902600073` `nom_commercial: CHATEAU HAUT-BRION`（135 av. Jean Jaurès, Pessac）**<br>🏛 **`57217902600081` `nom_commercial: CHATEAU LA MISSION HAUT-BRION`（67 rue de Peybouquey, 33400 Talence）**<br>🏛 **`57217902600099` `nom_commercial: CENTRE DE CONDITIONNEMENT LA TOUR HAUT-BRION`（141 av. Vieille Tour, Talence）**<br>🏛 **`57217902600065` 本店（Paris 75008、2015-10-15 開設）** |
| 🔴 **経営陣（🏛 登録）** | 🏛 **`DE LUXEMBOURG Robert`（1968 年生）／`DELMAS Jean-Philippe`（1969 年生、`Directeur général délégué`）／`VIDAL Philippe`（1961 年生、`Directeur général délégué`）／`SCHANKER (LE BELLEGARD) Rozenn`／`MOREL Julien`／`BRYAN Douglas Dillon`／`CUNNINGHAM (DE LUXEMBOURG/NASSAU) Charlotte` ほか** |
| **経営陣（✅ 公式）** | ✅ **`Prince Robert de Luxembourg` = `président`、「`la 4ème génération de la famille`」**<br>✅ **`Jean-Philippe Delmas` = `Directeur général délégué – Vins et Propriétés`、「`3ème génération de sa famille à être responsable de l'élaboration des vins`」**<br>✅ **`Jean-Philippe Masclef` = `Directeur technique`／`Florence Forgas` = `Maître de chai`（2014 年着任・2021 年 DNO 取得）／`Grégoire Bucaille` = `Chef de culture`** |
| **サイト制作 / ホスティング** | ✅ **`DISKO`（ALTAVIA DISKO, RCS Paris 521 097 774）／`ALTAVIA JETPULP`（SIREN 419 623 152）／AWS EMEA** |
| 🔴 **取得年** | ✅ **1935 年。「`L'achat sera conclu le 13 mai 1935`」。買主は `Clarence Dillon`、ニューヨークの銀行家。** |
| **認証（公式）** | 🔴 **公式サイトのどこにも農法の認証名が無い。**（HVE / bio / Terra Vitis / ISO のいずれも 0 件）<br>⚠️ **`Certifiés Haute Qualité Environnementale` は 2012 年の「建物」の認証であり、畑の認証ではない。** → §Farming |
| 🔴 **認証（🏛 有機）** | 🏛 **Agence Bio に登録なし。SIREN 572179026 の全 SIRET で `{"nbTotal":0,"items":[]}`。**<br>🏛 **企業登録側も `complements.est_bio: false`／全事業所 `liste_id_bio: null`。** |
| **canonical id** | 🔍 **3 件**（`haut-brion-1855` / `haut-brion-1993` / `haut-brion-1987`） |

### 🔴 ⚠️ 同名・近名の別実体 —— **SIREN で分離した結果、ブリーフの前提が一部崩れた**

| 🏛 SIREN | 名称 | NAF | 住所 | 判定 |
|---|---|---|---|---|
| 🔴 **572179026** | **DOMAINE CLARENCE DILLON**（SAS） | 01.21Z | Paris 75008 | 🔴 **本ドシエの対象** |
| 🔴 **572179026** | ⚠️ **CHATEAU LA MISSION HAUT-BRION** | 01.21Z | Talence | 🔴 **別 SIREN ではない。同一 SIREN の別 SIRET（`…081`）である** |
| 🔴 **572179026** | ⚠️ **CENTRE DE CONDITIONNEMENT LA TOUR HAUT-BRION** | 01.21Z | Talence | 🔴 **同上（`…099`）** |
| ⚠️ **389905811** | **QUINTUS SAS** | **11.01Z** | Paris 75008（同住所） | ⚠️ **別 SIREN。NAF は蒸留（11.01Z）で、ブドウ栽培ではない** |
| ⚠️ **480805639** | **CLARENCE DILLON WINES** | 46.34Z | Paris 75008／Talence | ⚠️ **別 SIREN。ネゴシアン。🔴 有機登録を持つのはこちら（下記 §Farming）** |
| ⚠️ **341826170** | 🔴 **CHATEAU LES CARMES HAUT BRION** | 01.21Z | 20 av. de Canteranne 33600 Pessac | 🔴 **完全な別法人・別所有者。canonical `les-carmes-haut-brion-2018` はこれ** |
| ⚠️ **340567809** | **CHATEAU LARRIVET HAUT BRION** | 01.21Z | 84 av. de Cadaujac 33850 Léognan | ⚠️ **完全な別法人。ブリーフの列挙に無かった 3 つ目の罠** |
| ⚠️ 他 12 件 | `SCI HAUT BRION`（×4）／`PHARMACIE HAUT BRION`／`HAUT BRION 2026`（Chamonix）／`KER HAUT-BRION` ほか | 68.20B ほか | 各地 | **ワインと無関係。名前検索は 550 件を返す** |

🔴 **ブリーフへの反証 ——「SIREN/SIRET で分離を確認せよ」「同じ持株会社が La Mission Haut-Brion と Quintus を所有しているので厳格に分けよ」という指示のうち、前半は La Mission について成立しない。**
🔴 **`Château La Mission Haut-Brion` は Domaine Clarence Dillon の子会社でも別法人でもなく、`同一 SIREN 572179026 の一事業所`である。SIREN では分離できない。分離できるのは SIRET（`…024` vs `…081`）だけである。**
🔴 **一方 `Château Quintus` は別 SIREN（389905811）であり、こちらは SIREN で分離できる。**
→ 🔴 **すなわち「SIREN で分ける」は同じグループ内で銘柄ごとに効いたり効かなかったりする。ワイン名の分離には SIRET 粒度が要る。** → §Canonical Conflict ⑦（未採番）

---

## Overview

✅ **シャトー・オー・ブリオンは、ボルドー市の南西数キロ、ペサックのコミューンにある。**
✅ **「`Le vignoble de Château Haut-Brion est situé sur la commune de Pessac, à quelques kilomètres au sud-ouest de Bordeaux. Il fait partie de l'appellation Pessac-Léognan, au nord de la région viticole des Graves de Bordeaux.`」**

🔴 ✅ **城が自らを一文で定義するとき、使う言葉はこれである ——**
✅ **「`Château Haut-Brion est le seul à avoir la double distinction de Premier Grand Cru Classé en 1855 et Cru Classé de Graves.`」**
🔴 **すなわち城が名乗る格付は「1855 年第一級」と「グラーヴのクリュ・クラッセ」の 2 つである。canonical はこの 2 つ目を 3 レコードとも持っていない。**

✅g **グループ site はさらに踏み込む ——「`conduit celle-ci à obtenir la rare distinction de Premier Grand Cru Classé au Classement de 1855, seul cru en dehors du Médoc à être retenu dans ce prestigieux classement`」。**
🔴 **「メドック以外で唯一」という主張は、造り手自身が公式に述べている。canonical の主張内容そのものは正しい。誤っているのは、その格付の名前を `1855 Médoc Classification` と呼んだことだけである。**

🏛 **公的側からも同じ位置づけが確認できる。INAO 正本 CDC の「lien avec la zone géographique」節 ——**
🏛 **「`Le classement de la totalité des « Crus Classés de Graves » (classement de 1959) au sein de la zone géographique, soit 16 « Châteaux » ou « Domaines », représentant environ le tiers des exploitations, témoigne de la notoriété historique des vins de « Pessac-Léognan ». Le plus illustre d'entre eux est le « Château Haut-Brion », « Premier Grand Cru » du classement des vins de Bordeaux de 1855.`」**

✅ **畑は 51 ヘクタール。うち 48 が赤（merlot, cabernet sauvignon, cabernet franc, petit verdot）、3 ヘクタール弱が白（sémillon, sauvignon blanc, sauvignon gris）。**

🔍 **THÉSEUS における状態は、Batch 11 までのどの生産者とも違う形をしている。**
🔍 **canonical はこの生産者に 3 レコードを割り当てているが、そのうち 1 件（`haut-brion-1855`）は `vintage: "—"` の格付レコードで、`resolved_bottles.json` では `vintage: {}` すなわち空になる。**
🔍 **にもかかわらずこのレコードは cuvée 層の `_stub` facts の供給源になっており、`grapes` と `aging` の誤った値が、レコードを持たない 4 ヴィンテージにまで既定値として降りてくる構造になっている。** → §Canonical Conflict ③

---

## History

✅ **公式沿革（`/histoire`）は 20 項目の年表。全文が静的 HTML に含まれる。以下は本ドシエの検証に関わる項目のみ。**

| 年 | 出来事 ✅ |
|---|---|
| **1 世紀** | **クロード帝の貨幣がグラーヴの croupe から出土。トポニム `Haut-Brion` のケルト起源と符合する** |
| 🔴 **1521** | 🔴 **ジロンド県文書館の 1521・1526 年の 2 つの写本に `Aubrion` / `Haulbrion` と `cru` の連結が現れる。「この 2 つのテキストが、3 世紀以上をかけて Haut-Brion を `Premier Cru Classé` へ導く流れを告げる —— `dans la Classification des Vins de la Gironde en 1855`」**<br>🔴 **公式がこの格付を呼ぶときの語がこれである。`Médoc` ではない。** |
| **1525 / 1533** | **1525 年に Jean de Pontac が Jeanne de Bellon と結婚。「`Elle lui apportera en dot une partie des terres`」。1533 年に Jean Duhalde からセニョリーの権利を取得**<br>⚠️ **canonical は「1525 年、結婚の持参金として Haut-Brion の土地がシャトーに加わり」と書くが、公式は「土地の一部」であり、権利取得は 1533 年である** |
| **1549** | **現在の城館の建設着工。Jean de Pontac は 1589 年 4 月 5 日に 101 歳で没する** |
| **1660** | ✅ **「`Charles II accède au trône d'Angleterre et sert Haut-Brion à sa table pour la première fois`」。王室のカーヴ帳簿に「`169 bouteilles … de vin de Hobrion … 21 shillings et 4 pennies par bouteille`」** |
| **1663** | ✅ **Samuel Pepys の日記「`… je bus une sorte de vin français appelé Ho Bryan …`」** |
| **1666** | ✅ **ロンドンに `Pontack's Head` 開店。「`7 shillings la bouteille, contre les 2 shillings habituels`」** |
| **1677** | ✅ **John Locke が 5 月 14 日に来訪** |
| **1787** | ✅ **5 月 25 日、Joseph de Fumel が Thomas Jefferson を迎える** |
| **1801** | **Talleyrand が購入、1804 年に売却** |
| 🔴 **1855** | 🔴 ✅ **「`à l'occasion de l'Exposition Universelle qui se tient à Paris, le Syndicat des Courtiers en vins de Bordeaux rédige, à la demande de la Chambre de Commerce de la Gironde, un classement officiel des meilleurs vins de Bordeaux. Les courtiers rendent leurs conclusions en se basant sur les prix atteints, sur le marché, au cours des siècles précédents. Château Haut-Brion devient l'un des quatre « Premiers Grands Crus Classés » en rouge, aux côtés de Margaux, Lafite et Latour.`」**<br>🔴 **起草者＝ボルドー仲買人組合、依頼者＝ジロンド商工会議所、機会＝パリ万博。基準＝過去数世紀の市場価格。`Médoc` の語は一度も現れない。** |
| **1880** | **フィロキセラが襲来。Eugène Larrieu が `vitis riparia` 台木で植え直す** |
| 🔴 **1923** | 🔴 ✅ **「`A partir du millésime 1923, Château Haut-Brion est l'un des premiers à pratiquer la mise en bouteille au château.`」**<br>🔴 **canonical は「18 世紀末にボルドーで先駆けてシャトーでのビン詰めを開始」「Pioneered château-bottling in Bordeaux in the late 18th century」と書く。公式は `1923 年` かつ `l'un des premiers`（先駆者の一人）である。年代が 125 年ずれ、単独性の主張も公式にはない。** → §Canonical Conflict ① |
| **1925 / 1935** | **1925 年 1 月に André Gibert が購入、10 年保有。1935 年 5 月 13 日に Clarence Dillon が取得。甥の Seymour Weller が gérant** |
| **1939** | **第二次大戦勃発時、城は仏軍将校のための病院に転用される** |
| 🔴 **1961** | 🔴 ✅ **「`En 1961, le cuvier est entièrement modernisé grâce à l'installation de cuves de fermentation en acier inoxydable.`」**<br>🔴 **公式は「1961 年にステンレス発酵槽で醸造設備を全面刷新した」と書くだけで、「ボルドーで最初」とは書いていない。canonical の "First stainless steel fermentation tanks in Bordeaux" は公式に根拠を持たない。** |
| **1975–2008** | **Joan Dillon（Clarence の孫娘）が城内を全面改装。1979 年に夫 Duc de Mouchy が合流。1991 年に高技術 cuvier を開設** |
| **2004** | **マヨット島の海食洞で 1850 年代とみられる Haut-Brion の 1 本が発見され、現在は城に戻っている。Château Quintus のボトル造形の着想源になった** |
| **2011 / 2012 / 2021** | ✅g **2011 年に Quintus 取得（2013・2021 に隣地を追加、現在 45 ha）／2012 年に Prince Robert 体制で建物改修完了／2021 年に Pavillon Catelan 開業** |

⚠️ **公式沿革に無いもの**: 1959 年グラーヴ格付への編入の経緯、Bahans Haut-Brion の初ヴィンテージ、白の初ヴィンテージ、INRA とのクローン研究。→ Open Questions

---

## Location

| | |
|---|---|
| **Country / Region** | France ／ **Bordeaux** ✅ |
| 🔴 **AOC** | 🔴 🏛 **`Pessac-Léognan`。`initialement reconnue par le décret du 9 septembre 1987`**（INAO 正本 CDC・Chapitre I-I）<br>🏛 **「`L'appellation d'origine contrôlée « Pessac-Léognan » est réservée aux vins tranquilles blancs et rouges.`」（同 I-III）** |
| 🔴 **AOC は赤白両方** | 🔴 🏛 **メドックの村名 AOC と違い、ペサック＝レオニャンは赤と白の両方を許す。**<br>🏛 **白の品種: `muscadelle B, sauvignon B, sauvignon gris G, sémillon B`**<br>🏛 **赤の品種: `cabernet franc N, cabernet-sauvignon N, carmenère N, cot N (ou malbec), merlot N, petit verdot N`**<br>🔴 **したがって `Château Haut-Brion`（赤）と `Château Haut-Brion Blanc`（白）は、同じ城の名前で、同じ AOC の下に、色だけを変えて併存する。** |
| **コミューン（🏛 10 村）** | 🏛 **`Cadaujac, Canéjan, Gradignan, Léognan, Martillac, Mérignac, Pessac, Saint-Médard-d'Eyrans, Talence, Villenave-d'Ornon`** |
| **区画区分（🏛）** | 🏛 **`comité national` の 1994-11-03/04、1997-09-10、2006-03-08/09、2011-02-10、2021-02-11 の各会期で承認された aire parcellaire** |
| **本件の所在** | ✅ **コミューン `Pessac`。🏛 SIRET `57217902600024` の住所は `133 avenue Jean Jaurès 33600 PESSAC`（lat 44.8163 / long −0.6126）** |
| 🔴 **面積** | 🔴 ✅ **`51 ヘクタール`。「`Le vignoble s'étend sur 51 hectares, 48 sont plantés de cépages rouges (merlot, cabernet sauvignon, cabernet franc et petit verdot) et près de 3 en vignes blanches (cépages sémillon, sauvignon blanc et sauvignon gris).`」** |
| 🔴 **土壌** | 🔴 ✅ **「`Ces graves … sont de petits cailloux, formés de différentes variétés de quartz. Les sols de graves reposent sur un sous-sol unique d'argile, de sable, de calcaire et de faluns (calcaire coquillé)`」**<br>✅ **「`D'une épaisseur variant d'une vingtaine de centimètres à plus de 3 mètres`」。croupe を形成し、Peugue・Serpent という 2 本の小川（ガロンヌの支流）が自然排水を助ける** |
| **向かい** | ✅ **「`La propriété fait face à Château La Mission Haut-Brion et partage avec lui cette vaste terrasse de belles graves dénommée Haut-Brion sur les cartes et chartes anciennes.`」** |
| **樹木・公園** | ✅ **`4 ヘクタールの樹林`、うち `3.5 ヘクタールの公園`** |

### 🔴 1987 と 1993 のボトルは、どの appellation を名乗り得たか

| | 判定 |
|---|---|
| 🔴 **1993** | 🔴 ✅ **決着済み。公式ボトルショットの 1993 ラベルに `Pessac-Léognan` と `Appellation Pessac-Léognan Contrôlée` が刷られている。実読した。** |
| 🔴 **1987** | 🔴 🏛 **法的には可能。**AOC は `décret du 9 septembre 1987` で創設され、📄 造り手の旧ページが 1987 年の収穫日を `28 sept.-13 octobre` と記録している。**収穫は政令の 19 日後に始まっている。**<br>🔴 ⚠️ **だが実ラベルは未確認である。**公式が持つ最古の赤ラベル画像は **1989**（`Appellation Pessac Léognan Contrôlée`、ハイフン無し表記）。**1987・1988 のページもフィッシュも HTTP 404。**<br>→ 🔴 **「1987 は Pessac-Léognan を名乗れた」は言ってよい。「1987 のラベルには Pessac-Léognan と刷ってある」は、実物を見るまで言ってはならない。** → Open Questions 1 |

### 🔴 ✅ ラベル書式の実測（**公式ボトルショット 13 点を実読。2004 年ヴィンテージで断絶する**）

| ヴィンテージ | ✅ 表ラベルの段組（実読） |
|---|---|
| 🔴 **1989** | `CHATEAU HAUT BRION`（**ハイフン無し**）/ `1989` / `CRU CLASSE **DE** GRAVES` / `Premier Grand Cru Classé en 1855` / `Appellation Pessac Léognan Contrôlée`（**ハイフン無し**）/ `Mis en bouteille au Château` / `Domaine Clarence Dillon s.a. Pessac, Gironde` |
| **1990 / 1993 / 1997 / 2000 / 2003** | `CHATEAU HAUT-BRION` / `<年>` / `CRU CLASSÉ **DES** GRAVES`（2003 は `DE`）/ `Pessac-Léognan` / `Appellation Pessac-Léognan Contrôlée` / `Premier Grand Cru Classé en 1855` / `Mis en bouteille au Château` / `Domaine Clarence Dillon s.a. propriétaire, Pessac, Gironde` |
| 🔴 **2004 / 2005 / 2008 / 2011 / 2015 / 2018 / 2019** | 🔴 **`CHATEAU HAUT-BRION` / `Premier Grand Cru Classé` / `<年>` / `Domaine Clarence Dillon Propriétaire` —— 以上で全部。**<br>🔴 **`Pessac-Léognan` なし。`Appellation … Contrôlée` なし。`CRU CLASSÉ DE GRAVES` なし。`en 1855` なし。** |
| 🔴 **白 2019** | 🔴 **`CHATEAU HAUT-BRION` / `2019` / `Domaine Clarence Dillon Propriétaire` —— 以上で全部。**<br>🔴 **`Premier Grand Cru Classé` の行すら無い。すなわち現行書式では、表ラベル上で赤と白を分けているのはこの 1 行と、印字色（赤＝金／白＝黒銀）だけである。** |

⚠️ **これは表ラベルのみの観察である。**AOC は法令上どこかに表示されねばならないので、2004 年以降は裏ラベルに移ったと考えるのが自然だが、**公式ボトルショットは裏面を持たない。** → Open Questions 3

---

## Farming

🔴 **本節の要点は 2 つ。① この城は農法の認証を 1 つも公表していない。② グループの中で有機登録を持っているのは、城ではなくネゴシアン会社であり、その対象は別ブランドである。**

### 🔴 🏛 有機 —— **SIRET 完全一致でゼロを実測した（proved negative）**

| 照会（SIRET 完全一致） | 🏛 結果 |
|---|---|
| 🔴 **`57217902600024`**（CHATEAU HAUT BRION, Pessac） | 🔴 **`{"nbTotal":0,"items":[]}`** |
| **`57217902600073`**（Château Haut-Brion, 135 av. Jean Jaurès） | **`{"nbTotal":0,"items":[]}`** |
| **`57217902600081`**（Château La Mission Haut-Brion） | **`{"nbTotal":0,"items":[]}`** |
| **`57217902600099`**（Centre de conditionnement La Tour Haut-Brion） | **`{"nbTotal":0,"items":[]}`** |
| **`57217902600065`**（本店 Paris） | **`{"nbTotal":0,"items":[]}`** |
| **`34182617000027`**（Château Les Carmes Haut Brion。別法人・参考） | **`{"nbTotal":0,"items":[]}`** |
| **企業登録の相互参照** | 🏛 **SIREN 572179026 の `complements.est_bio: false`／全 7 事業所の `liste_id_bio: null`** |

🔴 **`D-2026-08-05-08` の要件を満たす。名前検索ではなく SIRET 完全一致がゼロを返したので、これは有効な陰性である。**

### 🔴 ⚠️ ただし「Domaine Clarence Dillon は有機に無縁」ではない —— **別法人・別ブランドが持っている**

🏛 **`CLARENCE DILLON WINES`（SIREN `480805639`、SIRET `48080563900030`、`PAVILLON DILLON` 3 rue Avison 33400 Talence）は Agence Bio に登録がある。**

| 項目 | 🏛 登録内容 |
|---|---|
| **numeroBio** | **`50873`** |
| **認証機関 / EU 番号** | **`Ecocert France` / `FR-BIO-01`** |
| 🔴 **`etatCertification`** | 🔴 **`ENGAGEE`**（＝証明発行済みではなく engagement 状態） |
| 🔴 **`datePremierEngagement`** | 🔴 **`2023-03-10`** |
| **categories / activites** | **`Grossistes`／`Préparation` ＋ `Distribution`** |
| **productions** | **`11.02 Vins de raisin` = `AB`（2026）／`46.34.12 Commerce de gros de boissons alcoolisées` = `AB` ＋ `CNS`（2026）** |
| 🔴 **登録された公式サイト** | 🔴 **`https://www.clarendelle.com`** |
| **mixite** | **`Oui`**（＝有機と非有機を併せて扱う） |

🔴 **すなわち有機登録は「ネゴシアン会社が、`Clarendelle` ブランドについて、2023 年 3 月から」持っているものである。**
🔴 **城（SIREN 572179026）とは別法人であり、NAF も 46.34Z（酒類卸）で栽培ではない。**

✅g **さらにグループ site は、有機を名乗るワイン群を明示的に別のものとして紹介している ——**
✅g **「`En 2024 … la famille Dillon et le Prince Robert de Luxembourg ont choisi de concentrer leur attention sur une autre région française … en lançant Klara, la nouvelle famille de vins biologiques du sud de la France.`」**
🔴 **`vins biologiques` の語がグループ公式に現れるのは、この `Klara`（南仏、2024 年〜）ただ 1 か所である。ボルドーの城については一度も現れない。**

### 🔴 温度差の罠（`2e` 温度トラップ）

🔴 **OBP の 6 本は 1987〜2019 である。有機側の最古の日付は 2023-03-10 であり、しかも別法人・別ブランドである。**
🔴 **したがって OBP のどの 1 本についても、「有機である」も「有機でない」も、認証を根拠には言えない。** → §Staff Notes ⚠️

### ✅ 公式が名指しする実務（**認証ではなく実践**）

✅ **「`La protection de l'environnement est très ancienne, liée à la protection du terroir, transmise de génération en génération. Celle-ci passe par le respect des sols et de leurs caractéristiques, la limitation des interventions, l'absence d'insecticide.`」**
🔴 **公式が農薬について述べる唯一の具体は `l'absence d'insecticide`（殺虫剤を使わない）である。除草剤・殺菌剤については何も述べていない。**

✅ **土壌 ——「`Nous favorisons un enracinement profond de la vigne et maintenons un couvert végétal spontané le plus longtemps possible pendant l'hiver pour réduire l'érosion des sols. Les interventions mécaniques sont limitées en profondeur et en fréquence, et un amendement annuel par l'apport de compost est fait en fonction des besoins : chaque parcelle ne reçoit que le strict nécessaire. Le compost utilisé est produit à la propriété, à partir des sarments de taille et après un cycle de compostage de huit mois.`」**
✅ **「`En 2024, des mesures de conductivité ont été entreprises sur l'ensemble du vignoble pour affiner notre connaissance des sols et améliorer notre carte pédologique.`」**

✅ **生物多様性 ——「40 種超の鳥類（うち 14 が patrimoniales、28 が保護種）、265 taxons の昆虫・無脊椎動物（Grand Capricorne、Lucane cerf-volant、Andrenideae 属の野生蜂を含む）」。刈り取りは可能な限り遅く、緑の廃棄物の一部は現場に残す。**

✅ **収穫 ——「`Les raisins sont récoltés à la main en fonction de leur maturité, puis triés et éraflés`」（手摘み・選果・除梗）。**

⚠️ **HVE のレベル、Terra Vitis、SME、カーボン、被覆作物の草種、防除カレンダーは公式に一切記載が無い。** → Open Questions 5

---

## Winemaking

### ✅ 公式が述べる工程（`/savoir-faire`）

✅ **醸造**: 「`Les baies sont encuvées ; doucement la température va s'élever et les fermentations vont pouvoir démarrer.`」「`Le vinificateur sait, grâce à la technologie et à une gestion précise des températures, contrôler ces fermentations. Deux semaines plus tard … il est temps d'écouler les cuves. Véritable moment de vérité, puisque de chacune d'entre elles surgit un vin possédant sa propre personnalité.`」

🔴 ✅ **熟成 —— canonical と正面から食い違う一文がここにある。**
🔴 ✅ **「`Les plus grands vins seront sélectionnés pour entrer dans Château Haut-Brion et placés dans des fûts de chêne neufs durant dix-huit à vingt mois.`」（＝18〜20 か月）**
🔴 ✅ **「`Chaque année, la part de barriques neuves est adaptée, en fonction du vin et des caractéristiques du millésime.`」（＝新樽比率は毎年変える）**
✅ **「`le vin est fréquemment soutiré « à l'esquive » … Durant cette opération, la clarté du vin est constamment vérifiée, à la lumière d'une bougie.`」（蝋燭の光での澱引き）**

🔴 **canonical は 3 レコードとも `aging = "24 months barrel (new oak 100%)"` を持つ。公式は `18〜20 か月` であり、新樽比率は年ごとに変わる（実測 62〜90%）。両方の数値が誤っている。**
⚠️ **なお公式の文は「新しい樫樽に置く」と書いており、これだけを読むと 100% 新樽とも取れる。しかし同じ公式がヴィンテージごとに `Fûts neufs 62 %`〜`90 %` と明記しているので、100% は公式内で否定されている。**

✅ **アッサンブラージュ**: 「`la silhouette définitive du vin est dessinée très tôt et c'est donc l'assemblage final qui est présenté lors des dégustations « en primeurs », au printemps suivant.`」「`La transmission de ce savoir-faire se fait exclusivement en interne au sein de Domaine Clarence Dillon.`」

### 🔴 ✅ ヴィンテージ実データ（**公式 HTML とフィッシュ・テクニック PDF の両方から機械的に転記**）

| VT | 収穫日 | セパージュ（**HTML 側**） | セパージュ（**フィッシュ PDF 側**） | 新樽 | Alc | 瓶詰 |
|---|---|---|---|---|---|---|
| **1989**（参考・最古） | 8/31–9/20 | — | `Merlot Noir 41 % ; CS 50 % ; CF 9 %` | 🔴 **`90 %`** | 13 % | 1991/7/8–25 |
| 🔴 **1993** ⭐OBP | **9/16–9/29** | **`Merlot 53 % / CS 29 % / CF 18 %`** | **`Merlot Noir 53 % ; CS 29 % ; CF 18 %`** ✅一致 | ⚠️ **記載なし** | **12,5 %** | **1995/9/5–22** |
| 🔴 **2011** ⭐OBP | **8/31–9/27** | **`Merlot 35 % / CS 46 % / CF 19 %`** | **同一** ✅一致 | **`72 %`** | **13,5 %** | **2013/6/12–14** |
| 🔴 **2015** ⭐OBP | **9/8–10/5** | **`Merlot 50 % / CF 8 % / CS 42 %`** | **`Merlot Noir 50 % ; CS 42 % ; CF 8 %`** ✅一致 | **`78 %`** | **15,0 %** | **2017/6/29–7/4** |
| 🔴 **2018** ⭐OBP | **9/6–10/2** | 🔴 **`Merlot 49,4 % / CF 11,9 % / CS 38,7 %`** | 🔴 **`Merlot Noir 49,4 % ; CS 11,9 % ; CF 38,7 %`** ❌**不一致** | **`62 %`** | **14,5 %** | ⚠️ **FR `6/23–7/3` / EN `6/26–7/3`** |
| 🔴 **2019** ⭐OBP | **9/10–10/3** | 🔴 **`Merlot 48,7 % / CF 8,1 % / CS 43,2 %`** | 🔴 **`Merlot Noir 48,7 % ; CS 8,1 % ; CF 43,2 %`** ❌**不一致** | **`79 %`** | **15 %** | **2021/5/17–20** |
| 🔴 **1987** ⭐OBP | 📄 **9/28–10/13** | 🔴 **公式に存在しない（HTTP 404）** | 🔴 **公式に存在しない（HTTP 404）** | ❓ | ❓ | ❓ |

### 🔴 2018・2019 の矛盾 —— **✅ と ✅ がぶつかっている。片方に寄せない**

🔴 **不一致は「言語」ではなく「媒体」で割れている。**
- ✅ **FR HTML と EN HTML は一致する**（`Cabernet franc 11,9 % / Cabernet sauvignon 38,7 %`）。
- ✅ **FR PDF と EN PDF は一致する**（`Cabernet Sauvignon: 11,9 % ; Cabernet Franc: 38,7 %`）。
- 🔴 **HTML 群と PDF 群が食い違う。**

🔴 **PDF 抽出のアーティファクトではないことを実測で確認した。**`pdftotext -bbox-layout` で語の座標を取ると、2018 の PDF は
`y=607.2` に `Assemblage Merlot Noir : 49,4 % ; Cabernet Sauvignon : 11,9 %`、`y=618.0` に `Cabernet Franc : 38,7 %` と、**別行の別 y に置かれている。**
**同じ組版テンプレートの 2011・2015 では両媒体が一致する。したがって 2018・2019 の PDF には、値そのものが入れ替わって入っている可能性が高い。**
🔴 **だが「PDF が誤っている」と断定はしない。両方を記録し、どちらの数値も単独で断定的に言わない。** → §Staff Notes ⚠️

⚠️ **瓶詰日も 2018 で FR/EN が割れている（`23 juin` ⟷ `June 26th`）。これは媒体ではなく言語で割れており、上の矛盾とは別軸である。**

⚠️ **公式に一切記載が無いもの**: 酵母、マロラクティック発酵の有無と場所、発酵温度、圧搾、樽材の産地・樽職人、フィルタリング、生産本数（1987 の 📄 10,000 caisses を除く）。→ Open Questions 6

---

## Style

### ✅ 城自身のレンジ記述

✅ **赤**: 「`Elégant et complexe, le vin rouge de Château Haut-Brion est très minéral et d'une complexité rare, il se distingue par une étonnante longueur, cette persistance aromatique étant le privilège des très grandes origines.`」
✅ **白**: 「`Évoquer le vin blanc de Château Haut-Brion, c'est conjuguer la rareté, l'excellence et la richesse aromatique. Château Haut-Brion Blanc reste une icône dans le monde des vins blancs d'exception. La preuve la plus éclatante que Bordeaux sait aussi produire de très grands vins blancs !`」

### ✅ 公式テイスティングノート（**OBP 対象ヴィンテージのみ。造り手の言葉だけを使う**）

| VT | ✅ 公式ノート |
|---|---|
| 🔴 **1993** | 「**この vin を前にした我々の驚きと満足は大きい。色は非常に深く、しっかりしている。香りは cru に典型的で、`fruits rouges intenses et mûrs`（強く熟した赤い果実）の調子。タンニンの構造は `soyeuse et riche`（絹のようで豊か）。ワインは複雑で完璧に均衡している。文句なく、Haut-Brion の非常に美しい 1 本である。**」 |
| 🔴 **2011** | 「**色は美しい深い赤。香りはよく熟した黒い果実が強く、`fèves de cacao`（カカオ豆）の調子と混ざる。空気に触れると複雑さが爆発し、`les notes fumées réglissées si typiques de Haut-Brion`（Haut-Brion にかくも典型的な燻煙とリコリスの調子）がすでに透けて見える。口中のアタックは繊細で非常に優雅、そこから決して衝突することなく急速に力を増し、常に包まれたタンニンをもって、長く味わい豊かな美しい終盤へ開花する。**」 |
| 🔴 **2015** | 「**深いガーネット赤の非常に美しい色。第一の香りは熟して強い。攪拌すると複雑さが現れ、過剰さのないよく熟した赤と黒の果実。`Les épices se mêlent aux fruits, réglisse, légère note de clou de girofle…`（スパイスが果実と混ざる、リコリス、丁子の軽い調子）。口中のアタックは満ち、愛撫するよう。ワインは硬さなく即座に口蓋を満たす —— 高さ、幅、奥行きのすべての次元で。終盤は長く `notes de moka`（モカ）、それに `la légère amertume du café`（コーヒーの軽い苦味）が重なる。**」 |
| 🔴 **2018** | 「**濃く強い赤。第一の香りは深く、スパイシーで、熟した黒い果実、信じ難いほど複雑。アタックは柔らかく、すぐに織り目が立つ。ついでワインは、常に包まれたタンニンの織り目の上で満ちてゆく。ヴォリュームは圧倒的。終盤は信じ難いほど長く、粗さも重さもなく、味わいに富む。`Indéniablement, un grand Haut-Brion !`**」 |
| 🔴 **2019** | 「**見事な深い紫がかった赤。第一の香りは強さと繊細さを同時に持つ。果実味は熟し、攪拌が芳香の複雑さを明かす。口中のアタックは信じ難いほどの `suavité et délicatesse`。ついで、決して「筋肉を見せる」ことなく口を満たしてゆく。タンニンは硬さなく密で、微妙で、魅了する。終盤は長く、香り高い。`Encore une fois, Haut-Brion étonne par sa capacité à sublimer la complémentarité du merlot, du cabernet franc et du cabernet sauvignon.`**」 |
| 🔴 **1987** | 📄 **「`Le vin est strict, fin, fruité. Une bouteille très agréable.`」（FR 版）／「`This wine is tart but fruity and with a lot of finesse. A pleasant bottle.`」（EN 版）**<br>📄 **見出しは `BONNE ANNEE` / `A GOOD YEAR`。飲み頃は `Boire à partir de 1992 / 2000`。**<br>🔴 **これは造り手自身の言葉だが、1997 年に凍結された旧サイトのものである。現行サイトには存在しない。** |

⚠️ **点数・受賞・第三者評価の掲載は、公式サイトに一切無い。canonical の `points: 92`（1993）と `points: 88`（1987）は、公式に対応物を持たず、出典の記載も無い。**

---

## Important Cuvées

### ✅ 公式の現行レンジ（**全 4 品目。`gammes-sitemap.xml` と `/nos-vins` が完全に一致**）

| # | ✅ 公式のレンジ名 | 色 | ✅ 公式サイトが持つヴィンテージ範囲 | OBP |
|---|---|---|---|---|
| 1 | 🔴 **`Château Haut-Brion Rouge`** | 赤 | 🔴 **1989 – 2025**（1991・1995 等を含む。**1988 以前は無い**） | 🔴 ⭐**OBP 6 行すべての本体** |
| 2 | **`Château Haut-Brion Blanc`** | 白 | **1990, 1992 – 2025**（**1991 が欠落**） | — |
| 3 | 🔴 **`Le Clarence de Haut-Brion`**（セカンド・赤） | 赤 | 🔴 **2007 – 2025** | — |
| 4 | **`La Clarté de Haut-Brion`**（白） | 白 | **2009 – 2025** | — |

🔴 **この 4 品目の外に、公式が現在紹介しているワインは無い。**
🔴 **`Château Bahans Haut-Brion` の名前は、公式の現行ページには 1 か所しか現れない —— 改称の説明の中だけである。**

### 🔴 ✅ 改称 —— `Château Bahans Haut-Brion` → `Le Clarence de Haut-Brion`

✅ **公式 `/nos-vins` の原文 ——**
✅ **「`Très proche en élégance et en style de Château Haut-Brion, ce second vin est une excellente entrée en matière pour découvrir les vins rouges de Domaine Clarence Dillon. Anciennement nommé Château Bahans Haut-Brion dès les premiers millésimes du XXème siècle, ce second vin est rebaptisé Le Clarence de Haut-Brion, à partir du millésime 2007, en hommage à Clarence Dillon, acquéreur de la propriété en 1935.`」**

🔴 **これは Batch 10 が Billecart-Salmon で記録した「改称の過渡期に旧称が残る」形（未採番）と同じ形状である。番号は開かない。以下を証拠として当該の形に追加する ——**

| 観点 | 本件の実測 |
|---|---|
| **旧称 / 新称** | **`Château Bahans Haut-Brion` → `Le Clarence de Haut-Brion`** |
| 🔴 **切替点が明示されている** | 🔴 **`à partir du millésime 2007`。すなわちヴィンテージ境界で切り替わり、日付境界ではない。** |
| 🔴 **公式サイトの在庫表示と一致する** | 🔴 **`wine-sitemap.xml` の `le-clarence-de-haut-brion` は 2007 が最古で、2006 以前は 1 件も無い。宣言と実装が一致している。** |
| 🔴 **旧称のヴィンテージは公式から完全に消えている** | 🔴 **`Bahans` を含む URL は sitemap 全体（wine / gammes / page / post）に 0 件。**<br>🔴 **Billecart 型との差異はここである。Billecart では旧称が残存していた。ここでは旧称は改称の説明文 1 か所にしか残っていない。** |
| ⚠️ **OBP への影響** | ⚠️ **本 producer の OBP 6 行はいずれもセカンドではないので、直接の影響は 0 本。** |

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 6 本。すべてグラン・ヴァン赤**）

🔴 **本 producer の OBP 行は 2 つの別々の artifact に存在する。層ごとにスキーマが違うので、引用のたびにどちらかを明示する。**

🔍 **① intake 層 —— `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）。`research/producers/coverage.py` がカバレッジを算出する artifact であり、`match_state` / `confidence` / `source_quality_flags` / `_parts` を持つのはこちらである。**
🔍 **`source_producer_raw = "Haut-Brion"` / `source_wine_raw = "Pessac-Léognan"` / `source_section = "FRANCE | RED > BORDEAUX"` / `_parts = {"label": null, "appellation": "pessac leognan", "appellation_display": "Pessac-Léognan"}`**

🔍 **② store 層 —— `research/out/t-01/inventory.json`（行 1034–1039）／`research/out/t-01/mapping.json`／`research/store/t-01/shells.json`。**
🔍 **`producer_heading = "Haut-Brion"` / `product_name = ""`（空文字）/ `classification_text = "Pessac-Léognan"` / `layout = "producer_heading"` / `section_path = ["FRANCE | RED", "BORDEAUX"] / p.17`**
🔍 **この層は `match_state` も `confidence` も持たない。スキーマにそれらのフィールドが無いためであり、欠落ではない。**

🔴 **したがって「メニューは appellation をワイン名の欄に印字している」（intake の `source_wine_raw`）と「メニューはワイン名を印字していない」（store の `product_name` と intake の `_parts.label: null`）は、矛盾ではなく同じ 1 つの事実の 2 つの記録である。**
🔴 **メニューの当該欄には `Pessac-Léognan` が刷られており、それはワイン名ではなく appellation である。intake は生の印字を `source_wine_raw` に保存したうえで、`_parts.label: null` として「ラベル語は無い」と正しく分解している。** → §Canonical Conflict ⑤

| # | VT | 価格 | 🔍 intake `match_state` / `confidence` | ✅ **これは実際に何か** | 🔍 canonical |
|---|---|---|---|---|---|
| 1 | **2019** | **$2,740** | 🔍 **`unresolved` / `0.0`**<br>（`vintage_state: unresolved`） | 🔴 ✅ **`Château Haut-Brion Rouge 2019`。グラン・ヴァン。**公式に専用ページとフィッシュあり。`Merlot 48,7 % / CF 8,1 % / CS 43,2 %`（HTML）、新樽 79%、Alc 15%。🔴 **表ラベルに `Pessac-Léognan` は刷られていない** | 🔴 **レコード無し＝vintage gap** |
| 2 | **2018** | **$2,820** | 🔍 **`unresolved` / `0.0`** | 🔴 ✅ **同上 2018。**新樽 62%、Alc 14,5%。🔴 **セパージュは公式内で 2 通りある**（§Winemaking） | 🔴 **レコード無し＝vintage gap** |
| 3 | **2015** | **$2,820** | 🔍 **`unresolved` / `0.0`** | ✅ **同上 2015。**`Merlot 50 % / CS 42 % / CF 8 %`（両媒体一致）、新樽 78%、Alc 15,0% | 🔴 **レコード無し＝vintage gap** |
| 4 | **2011** | **$2,440** | 🔍 **`unresolved` / `0.0`** | ✅ **同上 2011。**`Merlot 35 % / CS 46 % / CF 19 %`（両媒体一致）、新樽 72%、Alc 13,5% | 🔴 **レコード無し＝vintage gap** |
| 5 | **1993** | **$1,800** | 🔴 🔍 **`exact` / `1.0`** | 🔴 ✅ **同上 1993。**`Merlot 53 % / CS 29 % / CF 18 %`、Alc 12,5%、瓶詰 1995/9。🔴 **実ラベルに `Appellation Pessac-Léognan Contrôlée` と `CRU CLASSÉ DES GRAVES` と `Premier Grand Cru Classé en 1855` の 3 行がある** | 🔴 **`haut-brion-1993` あり。だが `grapes` が公式と矛盾** |
| 6 | **1987** | **$2,400** | 🔴 🔍 **`exact` / `1.0`** | 🔴 📄 **同上 1987。ただし現行公式は何も持たない。**旧サイト（1997 捕捉）が `28 sept.-13 octobre` の収穫、`3262°` の積算温度、`352 mm` の降水、`10000 caisses` の生産量を記録。🔴 **セパージュは公式・旧公式ともに記載なし** | 🔴 **`haut-brion-1987` あり。だが `grapes` は照合不能** |

🔍 **上の `match_state` / `confidence` はすべて `obp_intake_normalized_20260804.json` の実測値である。store 層（`mapping.json` / `shells.json`）はこれらのフィールドを持たない。**
🔴 **6 行とも `producer_state: exact` かつ `cuvee_state: exact`。分岐しているのは `vintage_state` だけであり、`match_state` はそれをそのまま反映している。**
🔴 **すなわち 1993 と 1987 の `exact` / `1.0` は「ワインが同定できた」ことを意味しない。`⚠️ match_state = exact は canonical との一致度であって実在の裏づけではない` という Batch 11 の警告が、ここでは最も強い形で成立する —— `cuvee_state: exact` の根拠が、1 語も重ならないトークン集合の「一致」だからである（§Canonical Conflict ⑤）。**

### 🔴 セカンド／サードワインの印字は、このバッチのボルドー欄に 1 件も無い

🔍 **`Clarence` / `Clarté` / `Bahans` / `Pavillon` / `Forts de` / `Petit Mouton` / `Aile d` / `Pagodes` / `Sirène` / `Ygrec` / `Carruades` / `Goulée` / `Labory` を正規表現で走査した結果 ——**
🔍 **`obp_intake_normalized_20260804.json` 全 704 行に 0 件。`research/out/t-01/inventory.json` / `mapping.json` / `research/store/t-01/shells.json` にも 0 件。**
🔴 **すなわち OBP のボルドー欄は、どの生産者についてもセカンドワイン名を一度も印字していない。**
🔴 **本 producer の 6 行をすべてグラン・ヴァンと判定した根拠は造り手側の証拠（`Le Clarence` は 2007 以降しか存在せず、白は別レンジ）であるが、この走査はそれを独立に裏づける。**

### 🔴 メニューはどちら側にあるか —— **本件はメニューが正しい側である**

🔴 **`D-2026-08-05-…` の「メニューが defective とは限らない」原則の、はっきりした 4 例目にあたる。**

| 検証項目 | 結論 |
|---|---|
| **`Pessac-Léognan` は正しいか** | 🔴 ✅ **正しい。**🏛 INAO 正本 CDC がこの AOC を赤にも認めており、城自身も「`Il fait partie de l'appellation Pessac-Léognan`」と書く。**6 行すべてで正しい。** |
| **セクション `FRANCE \| RED > BORDEAUX` は正しいか** | ✅ **正しい。**6 本ともグラン・ヴァン赤である。 |
| **6 ヴィンテージは実在するか** | 🔴 ✅ **1993・2011・2015・2018・2019 は公式ページとフィッシュで実在確認。1987 は 📄 旧公式ページで実在確認。6/6 実在する。** |
| 🔴 **セカンドや白の混入はないか** | 🔴 **ない。**`Le Clarence` は 2007 以降しか無く、1987・1993 には存在しない。白は別レンジで、1987 の白は公式に無く（白は 1990 が最古）、2011/2015/2018/2019 の白は存在するが、**メニューはこれらを `FRANCE \| RED` に置いている。**混同の余地はない。 |
| 🔴 **ではなぜ 4 行が unresolved なのか** | 🔴 **canonical が 2019・2018・2015・2011 のレコードを持っていないからである。**🔍 **intake の evidence 行がそのまま述べている ——「`canonical の 'Château Haut-Brion' に vintage 2019 無し（保有: 1987, 1993）`」。**🔴 **メニューにも造り手にも欠陥はない。純粋な `vintage gap` である。** |
| 🔴 **セカンドワイン名の混入はコーパス全体でもゼロか** | 🔴 **ゼロ。**🔍 **13 個のセカンド／サード名を `obp_intake_normalized_20260804.json` 全 704 行と store 層の 3 artifact に対して走査し、いずれも 0 件。** |

⚠️ **ただしメニューが「不完全」ではある。**表ラベルの 2004 年以降の書式では `Pessac-Léognan` が表に出ないので、**卓上でメニューとボトルを見比べた客は、ラベルに appellation が見つからない。**これはメニューの誤りではないが、説明を要する。→ §Staff Notes 🔴 ③

---

## Staff Notes

### 🔴 芯 3 点（**これだけで、嘘を言わずにフロアに立てる**）

🔴 **① 「ペサック＝レオニャンにある、1855 年の第一級。ただしメドックではない。」**
**城自身の言葉で言えば「`Château Haut-Brion est le seul à avoir la double distinction de Premier Grand Cru Classé en 1855 et Cru Classé de Graves`」。**
**格付は 2 つある —— 1855 年の第一級（赤 4 本のうちの 1 本）と、グラーヴのクリュ・クラッセ。**
🔴 **1855 年の格付を「メドック格付」と呼んではいけない。INAO は `le classement des vins de Bordeaux de 1855` と呼び、城は `la Classification des Vins de la Gironde en 1855` と呼ぶ。この城は 1855 年の赤のリストで唯一メドック外の城である。**

🔴 **② 「AOC は 1987 年 9 月 9 日の政令で生まれた。テーブルの 1987 は、その 19 日後に収穫されている。」**
🏛 **`décret du 9 septembre 1987`。📄 造り手の旧ページによる 1987 年の収穫日は `28 sept.-13 octobre`。**
**それ以前の Haut-Brion は AOC グラーヴだった。テーブルの 6 本のうち、AOC が存在しない時代のものは 1 本も無い。**
⚠️ **ただし 1987 のラベルに実際に何が刷ってあるかは、店の実物を見るまで言わない。**

🔴 **③ 「新しいヴィンテージのラベルには、appellation が書かれていない。」**
🔴 **2004 年ヴィンテージから表ラベルは `CHATEAU HAUT-BRION / Premier Grand Cru Classé / <年> / Domaine Clarence Dillon Propriétaire` の 4 行だけになった。**
🔴 **2011・2015・2018・2019 の 4 本は、表に `Pessac-Léognan` も `CRU CLASSÉ DE GRAVES` も無い。1993 のラベルには両方ある。**
**これはメニューの誤りではなく、城のラベル刷新である。客が「ラベルに appellation が無い」と言ったら、これで答えられる。**

### ⚠️ 言ってはいけないこと（**必読**）

⚠️ **① 「1855 年メドック格付の第一級です」—— 言ってはならない。** メドック格付ではない。この城はメドックにない。正しくは「1855 年ボルドー格付」「1855 年ジロンド格付」あるいは単に「1855 年の第一級」。

⚠️ **② 「グラーヴから唯一メドック格付に選ばれた城です」—— 半分だけ正しく、危険。** 「唯一メドック外である」は公式に裏づけがある。だがそれを「メドック格付」と呼ぶ部分が誤りである。

⚠️ **③ 「セパージュは CS 45%、メルロ 37%、CF 18% です」—— 言ってはならない。** これは canonical の値で、造り手の実データと合わない。1993 は `Merlot 53 / CS 29 / CF 18`、2011 は `Merlot 35 / CS 46 / CF 19`、2015 は `Merlot 50 / CS 42 / CF 8`。**毎年変わる。**

⚠️ **④ 「2018（または 2019）のカベルネ・フランは○%です」—— 言ってはならない。** 城の HTML と城のフィッシュ PDF で 2 つのカベルネの数値が入れ替わっている。どちらが正しいか本調査では決着していない。**言えるのは「メルロが約 49%」までである。**

⚠️ **⑤ 「1987 のブレンドは…」—— 言ってはならない。** 造り手は 1987 のセパージュを現行サイトにも旧サイトにも公表していない。canonical の `CS 48 / M 35 / CF 17` は照合できない。**1993 の値が実測で外れていた以上、1987 の値も信用してはならない。**

⚠️ **⑥ 「24 か月の新樽 100% です」—— 言ってはならない。** 公式は `18〜20 か月`、新樽比率は年ごとに変える（実測 1989=90% / 2011=72% / 2015=78% / 2018=62% / 2019=79%）。**1993 は新樽比率が公表されていない。**

⚠️ **⑦ 「ボルドーで最初にシャトー元詰めをした城です」—— 言ってはならない。** 公式は「`A partir du millésime 1923 … l'un des premiers`」（1923 年から、先駆者の一人）。「18 世紀末」でも「最初」でもない。

⚠️ **⑧ 「1961 年にボルドーで初めてステンレスタンクを入れた城です」—— 言ってはならない。** 公式は「1961 年に cuvier をステンレス発酵槽で全面刷新した」としか書いていない。「ボルドー初」は公式に根拠が無い。

⚠️ **⑨ 「有機です」も「有機ではありません」も、言ってはならない。** 城の全 SIRET が Agence Bio にゼロ。同時に、城は農法の認証を 1 つも公表していない。**言えるのは「殺虫剤を使わないと公式に述べている」「冬の間できるだけ自生の草生を残す」「堆肥は自家製で 8 か月熟成」まで。**

⚠️ **⑩ 「Clarence Dillon は有機認証を持っています」—— 危険。** 有機登録（Ecocert、numeroBio 50873、`ENGAGEE`、2023-03-10〜）を持つのは **別法人 `CLARENCE DILLON WINES`（SIREN 480805639）** で、対象は **`Clarendelle`**。さらにグループが `vins biologiques` と呼ぶのは **2024 年に南仏で始めた `Klara`** だけである。**Haut-Brion ではない。**

⚠️ **⑪ 「Château Les Carmes Haut-Brion は Haut-Brion のセカンドです」—— 言ってはならない。** 完全な別法人（SIREN 341826170）、別所有者、Pessac の別住所。`Château Larrivet Haut-Brion`（SIREN 340567809、Léognan）も同様に無関係。

⚠️ **⑫ 「La Mission Haut-Brion は別会社です」—— 不正確。** 🏛 同一法人（SIREN 572179026）の一事業所である（SIRET `…081`）。**別のワイン、別の畑、別の城だが、法人は同じ。**

⚠️ **⑬ 「白の Haut-Brion Blanc は AOC ボルドー・ブランです」—— 言ってはならない。** メドックの村名 AOC と違い、🏛 ペサック＝レオニャンは白も認める（`réservée aux vins tranquilles blancs et rouges`）。**ただし 2019 の白の表ラベルには appellation の記載が無い。どこに書かれているかは未確認である。**

⚠️ **⑭ 「La Clarté de Haut-Brion は Haut-Brion の白のセカンドです」—— 不正確。** 公式は「`issue de raisins cultivés sur le terroir de Haut-Brion, elle est née de deux domaines prestigieux : Château Haut-Brion et Château La Mission Haut-Brion`」と書く。**2 つの城にまたがる。**

⚠️ **⑮ 「92 点」「88 点」を出典なしで言ってはならない。** 公式サイトには点数の掲載が一切無く、canonical の点数は誰の評価か記録されていない。

⚠️ **⑯ 「今が飲み頃のピークです」—— canonical の言い回しをそのまま使ってはならない。** 造り手が 1987 について残した唯一の飲み頃表示は 📄 `Boire à partir de 1992 / 2000` である。canonical の `Now–2027` / `Now–2030` は出典を持たない。

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

🔴 **本節は 7 件を提起する。うち 4 件は既存の族（`C-5` / `C-4` / `V-*` / `CAT-*`）に証拠を足すもの、3 件は既存のどれにも当たらない。**
🔒 **REGISTER.md も canonical も本書では一切編集していない。番号を開いてもいない。**

### 🔴 ① `classification` が事実として誤っている —— **`CAT-5 layer_boundary` ではなく、単純な事実誤り**

**1. 対象 canonical ID**: **`haut-brion-1855`**、`classification = "1855 Médoc Classification · 1er Grand Cru Classé"`

**2. なぜ誤りに見えるのか**
🔴 **格付の名前に `Médoc` が入っているが、この城はメドックに無い。しかも同じレコードの `description` が「メドック以外からメドック格付に選ばれた唯一の 1855 年第 1 級シャトー」と書いており、レコードは自分自身と衝突している。**

**3. 証拠（三層すべて）**
- 🏛 **INAO 正本 CDC「PESSAC-LÉOGNAN」（arrêté du 10 décembre 2024）**:
  「`Le plus illustre d'entre eux est le « Château Haut-Brion », « Premier Grand Cru » du classement des vins de Bordeaux de 1855.`」
- ✅ **城の公式沿革（`/histoire`, 1521 の項）**: 「`… amènera Haut-Brion au rang de "Premier Cru Classé" dans la Classification des Vins de la Gironde en 1855.`」
- ✅ **城の公式沿革（1855 の項）**: 「`le Syndicat des Courtiers en vins de Bordeaux rédige, à la demande de la Chambre de Commerce de la Gironde, un classement officiel des meilleurs vins de Bordeaux`」
- ✅ **実ラベル 4 点（1989 / 1990 / 1993 / 2003）**: 刷られているのは `Premier Grand Cru Classé en 1855` のみ。
- ✅g **グループ site**: 「`Premier Grand Cru Classé au Classement de 1855, seul cru en dehors du Médoc`」
- 🔴 **4 つの独立した出典のいずれにも `Médoc` は現れない。**

**4. あわせて欠落しているもの**
🔴 **3 レコードのどれも `Cru Classé de Graves` を持たない。** 城自身が「二重の顕彰」と呼び、🏛 INAO の CDC が表示規則まで定め（「`La mention « Cru Classé de Graves » peut figurer en remplacement de l'unité géographique plus grande`」）、実ラベルにも 2003 年まで刷られていた格付が、canonical には存在しない。

**5. OBP への影響**: 🔴 **6 本すべて。**`haut-brion-1855` が cuvée 層の stub 供給源なので、この文字列は 6 行すべての説明に降りうる。

**6. 推奨する解決（🔒 実行していない）**
- **`classification` を `Premier Grand Cru Classé en 1855`（ラベル準拠）または `Premier Grand Cru — classement des vins de Bordeaux de 1855`（INAO 準拠）に置換。**
- **`Cru Classé de Graves` を第 2 の格付として別フィールドに持つ。**🔴 **1 本のワインが 2 つの独立した格付制度に属し得るという事実は、単一の `classification` 文字列では表現できない。これはスキーマ側の判断であり、本書では実行しない。**

**7. Confidence**: 🔴 **High。** 🏛＋✅＋✅ラベル の三層一致。

---

### 🔴 ② `grapes` が 1993 で矛盾し、かつ 2 レコードに byte 同一で複製されている —— **Roederer 型が typed field に出た**

**1. 対象 canonical ID**: **`haut-brion-1993`** と **`haut-brion-1855`**（同一配列）／**`haut-brion-1987`**（別配列だが照合不能）

**2. 実測**

| レコード | canonical `grapes` | ✅ 公式 | 判定 |
|---|---|---|---|
| **`haut-brion-1855`** | `CS 45% / Merlot 37% / CF 18%` | 🔴 **ヴィンテージ非依存の値は公式に存在しない。**terroir 頁は品種名のみ列挙し、`petit verdot` を含む | 🔴 **無根拠。しかも同レコードの `obp_note` は `Merlot 45% / CS 44% / CF 10% / PV 1%` と書いており、typed field と自己矛盾** |
| **`haut-brion-1993`** | `CS 45% / Merlot 37% / CF 18%`（**上と byte 同一**） | 🔴 **`Merlot Noir 53 % ; CS 29 % ; CF 18 %`**（HTML・フィッシュ PDF の両方） | 🔴 **矛盾。メルロ ±16pt、CS ±16pt。主要品種が逆転** |
| **`haut-brion-1987`** | `CS 48% / Merlot 35% / CF 17%` | 🔴 **公式・旧公式ともに沈黙**（頁 404・フィッシュ 404・Wayback 頁にセパージュ欄なし） | ❓ **照合不能。②の実績から信用してはならない** |

🔴 **`haut-brion-1855` と `haut-brion-1993` が同一の配列を持つことは、Batch 10 の Roederer（同一 `house_style` を 16 レコードに複製）・Batch 11 の Allemand（同一 `description` を 5 レコードに複製）と同じ形である。**
🔴 **ただし本件は prose ではなく typed field で起きている点が新しい。しかも複製元（`haut-brion-1855`）は実在するボトルではなく格付レコードなので、「どのヴィンテージのものでもない値」が実在ヴィンテージに複製されている。**

**3. OBP への影響**: 🔴 **少なくとも 1 本（1993, $1,800）が公式と矛盾する値で説明される。**
🔴 **さらに `resolved_bottles.json` の `cuvee:chateau-haut-brion-chateau-haut-brion` の `facts` にこの配列が `_stub: true` で入っているため、レコードを持たない 2019・2018・2015・2011 の 4 本にも既定値として降りる。実効影響は 5 本。**

**4. 推奨（🔒 実行していない）**
- 🔴 **`grapes` はヴィンテージ層の属性であって、cuvée 層の属性ではない。**Haut-Brion の実測（1989: M41/CS50/CF9 → 2019: M48.7/CS43.2/CF8.1）は年ごとに 20pt 以上動く。**cuvée 層に `grapes` を置く設計そのものを見直す必要がある。**
- **1993 は公式値 `Merlot 53 / CS 29 / CF 18` に置換可能。**
- 🔴 **1987 は照合不能なので、値を消して `unverified` にするのが安全。**

**5. Confidence**: 🔴 **High**（1993）／**High**（複製の事実）／**Medium**（1987 は「誤り」ではなく「不明」）。

---

### 🔴 ③ `haut-brion-1855` は「格付をボトルとして格納したレコード」で、しかも stub の供給源になっている

**1. 対象**: **`haut-brion-1855`**（`vintage: "—"`、U+2014 センチネル）

**2. 実測**
- 🔍 **`resolved_bottles.json` において、このレコードは `producer` と `cuvee` を生成するが `vintage: {}`（空オブジェクト）を返す。すなわち vintage 層には何も存在しない。**
- 🔍 **にもかかわらず `cuvee:chateau-haut-brion-chateau-haut-brion` の `facts` は `_stub: true` を持ち、`vintage: "—"` を含んだまま `grapes` / `aging` / `tasting` / `terroir` を保持している。**
- 🔴 **したがってこのレコードは「ボトルではない」のに「全ボトルの既定値」になっている。**

**3. 既存族との関係**
- ⚠️ **`C-2`（非ワインレコードの混入）とは異なる。**`C-2` は第三者批評家のプロフィール記事だった。本件は**造り手のレコードであり、内容も概ね正しい。誤っているのは層である。**
- ⚠️ **`S-4`（entity 境界が未文書化）の `appellation_references 1` に近いが、本件は appellation ではなく `classification` を主体としている。**
- 🔴 **ブリーフが述べる「`vintage: "—"` が 328 件」というスイープ結果の、本 producer における実例が 1 件確認された。**

**4. OBP への影響**: 🔴 **間接だが 6 本すべて。**（②経由）

**5. 推奨（🔒 実行していない）**: **格付・producer プロフィールを vintage 層から切り離し、`_stub` の供給源にしない。**`S-4` と同じ処置系だが、**「造り手自身のレコードだが層が違う」型は分離基準に明記されていない。**

**6. Confidence**: 🔴 **High**（構造は実測）。

---

### 🔴 ④ `aging` が 3 レコードすべてで公式と矛盾する —— **byte 同一の第 2 例**

**1. 対象**: `haut-brion-1855` / `haut-brion-1993` / `haut-brion-1987`、いずれも `aging = "24 months barrel (new oak 100%)"`（**3 件 byte 同一**）

**2. 証拠**
- ✅ **`/savoir-faire`: 「`placés dans des fûts de chêne neufs durant dix-huit à vingt mois`」（18〜20 か月）** → **24 か月は矛盾。**
- ✅ **`/savoir-faire`: 「`Chaque année, la part de barriques neuves est adaptée`」** → **100% 固定は矛盾。**
- ✅ **実測: 1989 `90 %` / 2011 `72 %` / 2015 `78 %` / 2018 `62 %` / 2019 `79 %`。1993 は公式に記載なし。**
- 🔴 **さらに `haut-brion-1855` の `obp_note` 自身が「年により約 20 ヶ月」と書いており、同レコードの typed `aging`（24 か月）と自己矛盾している。**

**3. OBP への影響**: 🔴 **6 本すべて**（stub 経由）。

**4. 推奨（🔒 実行していない）**: **`aging` の期間を `18–20 months` に、新樽率をヴィンテージ層へ移す。**

**5. Confidence**: 🔴 **High**。

---

### 🔴 ⑤ **未採番 — CTO's call**: 「ワイン名が無い」を **検出 → 上書き → 潰し** の 3 層が別々に扱う

🔴 **これは 1 つのバグではなく、3 つの層が同じ事実に対して 3 通りに振る舞う連鎖である。層ごとに artifact を明示して記す。**

---

#### 🔴 第 1 層 —— **検出は正しい**（artifact: `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`、704 行）

🔍 **本 producer の 6 行はすべて `_parts.label: null` を持つ。パーサは「ラベル語（ワイン名）が印字されていない」と正しく判定している。**
🔍 **`_parts` の全体は `{"label": null, "appellation": "pessac leognan", "appellation_display": "Pessac-Léognan", "printed_rest": "Pessac-Léognan", "varietal": null, "style": null, "rank": null}`。appellation として正しく分類されている。**

🔴 **同 artifact をコーパス全体で走査した実測 ——**

| 走査（すべて `obp_intake_normalized_20260804.json`） | 実測 |
|---|---|
| 🔴 **`_parts.label is null`** | 🔴 **704 行中 292 行（41.5%）** |
| 🔴 **`source_section` に `BORDEAUX` を含む行のうち `_parts.label is null`** | 🔴 **69 行中 69 行。例外ゼロ。** |
| 🔴 **`_parts.label is null` かつ `proposed_canonical_cuvee` が出力されている** | 🔴 **152 行** |

🔴 **ボルドーが 69/69 であることは、本 producer の 6 行が例外事例ではなく、セクション全体の構造であることを意味する。**

---

#### 🔴 第 2 層 —— **matcher が検出結果を上書きする**（同 artifact）

🔴 **`_parts.label: null` にもかかわらず、6 行すべてが次を持つ ——**
🔍 **`normalized_cuvee: "Pessac-Léognan"` ／ `proposed_canonical_cuvee: "Château Haut-Brion"` ／ `proposed_canonical_cuvee_id: "cuvee:chateau-haut-brion-chateau-haut-brion"` ／ 🔴 **`cuvee_state: "exact"`**

🔴 **そしてその根拠として evidence 配列に書かれている文字列がこれである ——**
🔴 **「`名称トークン集合一致: 'pessac leognan' ≡ 'Château Haut-Brion'`」**

🔴 **`{pessac, leognan}` と `{château, haut, brion}` は 1 語も共有していない。トークン集合の共通部分は空である。matcher は「トークン集合が一致した」と明記した上で `exact` を返している。**

🔴 **上記 152 行の内訳を実測すると、`cuvee_state` は `exact` 147 / `alias` 3 / `candidate` 2。**
🔴 **すなわち「ワイン名が印字されていない」と検出された 152 行のうち 96.7% で、matcher は留保なしに `exact` を主張している。**

🔴 **これは Mouton 担当が反対側から独立に到達した所見と同一である**（matcher が `'pauillac' ≡ 'Château Mouton-Rothschild'` を出力し、共通トークンゼロで `cuvee_state: exact` を返す）。**同じ機構が、appellation しか印字されないボルドー欄の全域で作動している。**

🔴 **重要な帰結**: 本 producer の 1993・1987 は `match_state: exact` / `confidence: 1.0` だが、その `cuvee_state: exact` の根拠は上の偽の一致主張である。**分岐しているのは `vintage_state` だけで、cuvée の同定は 6 行とも同じ（誤った）根拠に立っている。**
⚠️ **`match_state = exact` が「canonical との一致度であって実在の裏づけではない」という Batch 11 の警告の、最も強い実例。**

---

#### 🔴 第 3 層 —— **store が 6 行を 1 個に潰す**（artifact: `research/store/t-01/shells.json` / `research/out/t-01/mapping.json`）

🔍 **OBP 6 行（`source_line_no` 1034–1039）がすべて `rs:pro:7e4577c3f98cf640` という 1 個の product-level shell に解決している。**
🔍 **`source_transcription` は 2019 の行（$2,740）。残る 5 行は `source_lines` 配列に束ねられている。**
🔍 **`identity_basis: "source_exact"`／`canonical: {producer_id: "producer:chateau-haut-brion"}` のみ（cuvée なし・vintage なし）／`verification_status: "unverified"`／`excluded_from_recommendations: true`。**
🔍 **`mapping.json` でも 6 行すべてが `resolved_to: "research_shell"` かつ同一 `shell_id`。**

🔴 **store 層はここでは誤っていない。`product_name` を空文字のまま正しく保存しており、intake の `_parts.label: null` と一致している。**
🔴 **潰しの原因は shell の identity key に `vintage` が入っていないことであり、key が（producer, product_name="", classification_text="Pessac-Léognan"）で 6 行とも同一になる。**

🔴 **なお store 層が intake 層の判定を引き継いでいない（`match_state` / `confidence` を持たない）ことは、既知の intake↔store 乖離の 5 例目以降にあたる。**
🔴 **既報: Bachelet-Monnot / Clos de Tart / Armand Heitz / Hundred Acre。本件はボルドーでの初例である。**

---

**既存族との関係**
- 🔴 **`C-4`（識別語を持たないキュヴェ名、canonical 38 レコード）の極限形。**`C-4` は「スタイル語のみで生産者を特定する語を含まない」名前を扱う。**本件はメニュー側の名前が空である。`C-4` の記述はこの場合を含んでいない。**
- 🔴 **`C-5`（cuvée 名 == producer 名、Bordeaux グランヴァン型、69 レコード / OBP 63 本）に接する。**本 producer は `producer='Château Haut-Brion'` / `cuvee='Château Haut-Brion'` でまさに `C-5` の形。🔴 **`C-5` は「matcher がこれを特別扱いする分岐を持たないと Bordeaux が一切解決しない」と述べる。実測はその分岐が存在することを示すが、その分岐が `exact` を返す代償に偽の evidence 文字列を生成している。`C-5` の記述はここまで踏み込んでいない。**
- ⚠️ **`V-*` 族とは層が違う。**`V-1`〜`V-4` は「vintage 層に識別子が足りない」話で、本件は「shell の key に vintage が入っていない」話である。

**OBP への影響**: 🔴 **本 producer で 6 本（$1,800・$2,400・$2,440・$2,820・$2,820・$2,740、合計 $14,940）が 1 個の未検証 shell に潰れ、`excluded_from_recommendations: true` で推薦から外れている。**
🔴 **コーパス全体では、第 1・第 2 層の影響は 292 行・152 行に及ぶ（本 producer 以外は本書の担当外）。**

**推奨（🔒 実行していない）**
- **product-level shell の identity key に `vintage` を含める。**
- 🔴 **`_parts.label is null` のとき、matcher が `cuvee_state: exact` を返すことを禁じる。少なくとも evidence に「トークン集合一致」と書くことは、共通部分が空である以上できない。**
- 🔴 **`layout: "producer_heading"` かつ `_parts.label is null` の行では、`producer_heading` が実質的にワイン名を兼ねている。この組み合わせを欠損ではなく「グラン・ヴァン」の明示的指標として扱えるか、が設計判断である。**
- ⚠️ **いずれも本書では実行しない。**

**Confidence**: 🔴 **High**（3 層とも artifact 上で実測。292 / 69 / 152 / 147 の各数値は再現可能）。

---

### 🔴 ⑥ prose のみの部分文字列一致 20 件 —— `D-2026-08-05-08` の実測

🔍 **canonical 928 レコードを `brion`（大小無視）で走査すると 23 件が当たる。内訳 ——**

| 種別 | 件数 | 内容 |
|---|---|---|
| 🔴 **本 producer** | **3** | `haut-brion-1855` / `haut-brion-1993` / `haut-brion-1987` |
| 🔴 **別実体（`id` と `producer` で当たる）** | **1** | 🔴 **`les-carmes-haut-brion-2018`（`producer='Les Carmes Haut-Brion'`）。🏛 SIREN 341826170 の完全な別法人。** |
| 🔴 **prose のみ（`obp_note` / `description` だけで当たる）** | 🔴 **19** | 🔴 **`bordeaux-vintage-*-guide` 17 件（1964–1987）＋ `la-lagune-1855` ＋ `guilbert-gillet-savigny-rouge-2022`** |

🔴 **prose 側の 19 件はいずれも第三者批評家のヴィンテージ評である。**`bordeaux-vintage-1972-guide` は本文に「`Parker's disclaimer`」と明記しており、由来が第三者であることが記録上も確認できる。
🔴 **`guilbert-gillet-savigny-rouge-2022` は Burgundy の生産者で、`Haut-Brion` は「そこで研修した」という経歴の記述として現れる。**
🔴 **`la-lagune-1855` は「メドックで最南の格付château（Haut-Brion を除く）」という比較文で現れる。**

→ 🔴 **すなわち `Haut-Brion` を単純な部分文字列で引くと、23 件中 19 件（83%）が誤検出になる。しかもその 19 件は本 producer の説明文としてもっともらしく読める。`D-2026-08-05-08` はこの producer で最悪の形で成立する。**
🔴 **さらに `les-carmes-haut-brion-2018` は `producer` フィールドでも当たるので、フィールド限定でも防げない。SIREN でしか分離できない。**

**Confidence**: 🔴 **High**（機械的走査）。

---

### 🔴 ⑦ **未採番 — CTO's call**: SIREN では分離できない同名ブランドがある

**1. 実測**
🏛 **`Château Haut-Brion` と `Château La Mission Haut-Brion` と `Château La Tour Haut-Brion`（の瓶詰センター）は、いずれも SIREN `572179026` の事業所である。SIRET でしか分かれない。**
🏛 **一方 `Château Quintus` は SIREN `389905811` で分かれ、`Château Les Carmes Haut-Brion` は SIREN `341826170` で分かれる。**

**2. なぜ問題か**
🔴 **`D-2026-08-05-08` は「SIREN/SIRET で曖昧性を解消せよ」と定める。だが同じ 3 語（`Haut-Brion`）を含む 5 つのブランドのうち、SIREN で分離できるのは 2 つだけである。**
🔴 **残る 3 つは同一 SIREN であり、「同じ法人だから同じ生産者」と扱うと 3 つの城が 1 つに潰れる。**
🔴 **`exact-SIRET` を proved negative の唯一の形とする規則（`D-2026-08-05-08`）は Agence Bio 照会には正しく効いた（本件で 7/7 が有効な陰性）。だが `identity の分離` の道具としては、SIREN と SIRET で粒度が違うことを明示する必要がある。**

**3. 推奨（🔒 実行していない）**: **producer identity の外部キーを SIREN ではなく SIRET（または SIRET + enseigne/nom_commercial）に置く。**

**4. Confidence**: 🔴 **High**（🏛 実測）。

---

### 🔴 検証したフィールド数と失敗数

🔴 **3 レコードの typed field および `obp_note` 内の検証可能な言明を、公式・公的出典に対して 1 件ずつ照合した。**

| レコード | 照合した項目 | ✅ 一致 | 🔴 矛盾 | ⚠️ 無根拠 | ❓ 照合不能 |
|---|---|---|---|---|---|
| **`haut-brion-1855`** | **26** | **10** | 🔴 **6** | **9** | **1** |
| **`haut-brion-1993`** | **18** | **9** | 🔴 **3** | **6** | **0** |
| **`haut-brion-1987`** | **17** | **8** | 🔴 **2** | **5** | **2** |
| 🔴 **合計** | 🔴 **61** | **27** | 🔴 **11** | **20** | **3** |

🔴 **矛盾 11 件の内訳** ——
`classification`（1855 Médoc）×1 ／ `grapes`（1993 実測差）×1 ／ `grapes`（1855 レコード内の自己矛盾）×1 ／ `aging`（期間 24 か月）×3 ／ `aging`（新樽 100%）×3（1855/1993/1987 各 1）※期間と新樽を 1 件ずつ数えた ／ 元詰めの年代・単独性 ×1 ／ 白の「Sémillon+SB 各 50%」×1。
🔴 **無根拠 20 件の代表** —— `points 92` / `points 88` / `drinking_window` ×3 / `food_pairings` ×3 / `glassware` ×3 / `serving_temp` ×3 / 「INRA と 1975 年からクローン研究・500 種以上」/「1961 年ボルドー初のステンレス」/「1649 年からアルノー 3 世が澱引き・ウイヤージュ導入」/「La Clarté の旧称 Les Plantiers」/ `tasting` の内容 ×2。
🔴 **照合不能 3 件** —— `haut-brion-1987` の `grapes` / 1987 の新樽比率 / `haut-brion-1855` の「encépagement Merlot 45 / CS 44 / CF 10 / PV 1」。

🔴 **失敗率は 11/61 = 18.0%（矛盾のみ）、34/61 = 55.7%（矛盾＋無根拠＋照合不能）。**
🔴 **すなわち Batch 8–11 の「14 軒中 13 軒で canonical が公式と食い違う」という base rate は、15 軒目でも崩れなかった。**
⚠️ **ただし本 producer では `producer` / `name` / `subregion` / `color` / `region` / `country` といった識別用の typed field は 3 レコードとも正しい。壊れているのは `classification` / `grapes` / `aging` と prose である。**

---

## Sources

### ✅ 採用した公式ドメイン（**§2a 真正性チェック合格**）

| URL | 層 | 真正性の根拠 |
|---|---|---|
| 🔴 **`https://www.haut-brion.com/`** | ✅ | 🔴 **`/mentions-legales` が「`Les sites www.domaineclarencedillon.com, www.haut-brion.com et www.mission-haut-brion.com sont produits par la société DOMAINE CLARENCE DILLON S.A.S. … immatriculée au registre du commerce et des sociétés de Paris sous le n° B 572 179 026 représentée par Philippe Vidal`」と名乗る。**<br>🔴 **🏛 `recherche-entreprises.api.gouv.fr` の SIREN `572179026`（`DOMAINE CLARENCE DILLON`、SAS、01.21Z）と完全一致。代表者 `VIDAL Philippe`（`Directeur général délégué`）も一致。合格。** |
| **`https://www.domaineclarencedillon.com/`** | ✅g | **同一の mentions légales・同一 SIREN。合格。**<br>⚠️ **ただしグループの筆致であり、城の筆致とは別の authorship layer として扱った。本書で `✅g` を付した引用はすべてこちら。** |
| 📄 **`https://web.archive.org/web/19970120081920/http://www.haut-brion.com/chb/vintage/v3en.cgi?year=1987`**（および `v3fr.cgi`） | 📄 | **同一ドメイン `haut-brion.com` の 1997-01-20 捕捉。**<br>⚠️ **1997 年当時のページに mentions légales ブロックは存在しない。したがって §2 の 📄 要件を厳密には満たさない。**<br>🔴 **本書は、現行の同一ドメインが 🏛 と一致することを根拠にこれを 📄 として採用し、そのことを明記した上で 1987 の気候・収穫日・生産量のみに用いた。セパージュの推定には一切用いていない。** |

### 🏛 公的登録・法令

| URL / 照会 | 内容 |
|---|---|
| **`https://recherche-entreprises.api.gouv.fr/search?q=domaine%20clarence%20dillon`** | SIREN 572179026 の全 7 事業所・役員・NAF・TVA |
| **`…?q=haut-brion` / `…?q=chateau%20quintus` / `…?q=les%20carmes%20haut%20brion` / `…?q=CLARENCE+DILLON+WINES`** | 同名別実体の分離（550 件 / 1 件 / 2 件 / 1 件） |
| **`https://opendata.agencebio.org/api/gouv/operateurs/?siret=<7 件>`** | 全件 `{"nbTotal":0,"items":[]}` |
| **`https://opendata.agencebio.org/api/gouv/operateurs/?numeroBio=50873`** | CLARENCE DILLON WINES の Ecocert 登録（`ENGAGEE`, 2023-03-10, `clarendelle.com`） |
| 🔴 **`https://info.agriculture.gouv.fr/boagri/document_administratif-eafa5b1a-119b-4042-814b-a0a10646c996/telechargement`** | 🔴 **AOC「PESSAC-LÉOGNAN」CDC 正本。`Homologué par l'arrêté du 10 décembre 2024 publié au JORF du 12 décembre 2024`／BO agri 2024-12-19。`%PDF` 実体確認済（232,518 bytes）。**<br>🔴 **本書の 🏛 引用はすべてこの正本から取った（PNO 草案からではない）。** |
| **`https://extranet.inao.gouv.fr/fichier/3-CDC-Pessac-Léognan-v170619.pdf`** | ⚠️ **PNO 2020 草案。正本と本書の引用箇所は一致することを確認した上で、引用は正本側を採用。`%2c` 節の「PNO 草案の打消し線混在」の罠は本件では発現しなかった。** |
| **`https://www.inao.gouv.fr/produit/pessac-leognan-rouge-20054`** | 正本 CDC への導線・homologation 情報 |
| **`https://extranet.inao.gouv.fr/fichier/CDC---Graves-et-Graves-supérieures---PNO-2023.pdf`** | ⚠️ **参照したが、1959 年グラーヴ格付への言及は無かった。** |

### ✅ 造り手の一次資料（**取得・実読したもの**）

- **ページ**: `/`, `/histoire/`, `/nos-vins/`, `/terroir/`, `/savoir-faire/`, `/mentions-legales`
- **ヴィンテージページ（FR）**: 1989, 1990, 1993, 1997, 2000, 2003, 2004, 2005, 2008, 2011, 2015, 2018, 2019（赤）／2019（白）
- **ヴィンテージページ（EN）**: 2018, 2019（赤）
- **フィッシュ・テクニック（`%PDF` 実体確認済）**: `Fiche-technique_ChateauHBR_{1989,1993,2011,2015,2018,2019}_FR.pdf` ／ `…_{2018,2019}_EN.pdf`
- 🔴 **ボトルショット（ラベル面を実読）**: `HBR-{1989,1990,1993,1997,2000,2003,2004,2005,2008,2011,2015,2018,2019}-min.png` ／ `HBB-2019-min.png`
- **sitemap**: `sitemap_index.xml` → `wine-sitemap.xml` / `gammes-sitemap.xml` / `page-sitemap.xml` / `post-sitemap.xml` / `category-sitemap.xml`

### 🔍 THÉSEUS 内部 artifact（**走査したもの。層ごとにスキーマが違う**）

| artifact | 層 | 本書での用途 |
|---|---|---|
| 🔴 **`/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`**（704 行） | **intake** | 🔴 **`match_state` / `confidence` / `producer_state` / `cuvee_state` / `vintage_state` / `evidence` / `source_quality_flags` / `_parts` の唯一の出所。**§Important Cuvées の状態表と §Canonical Conflict ⑤ の 292 / 69 / 152 / 147 はすべてここからの実測 |
| **`research/out/t-01/inventory.json`** | **store** | 生の行（`source_line_no` 1034–1039）・`product_name` の空文字・`layout` |
| **`research/out/t-01/mapping.json`**（768 行） | **store** | `resolved_to` / `shell_id` |
| **`research/store/t-01/shells.json`** | **store** | `rs:pro:7e4577c3f98cf640` の全内容 |
| **`research/out/t-01/review.json`**（113 行） | **store** | 本 producer の行は 0 件（fuzzy candidate 無し）を確認 |
| **`research/out/t-01/duplicates.json`** | **store** | 本 producer の該当 0 件を確認 |
| **`migration/out/export/db_wine_canonical.json`**（928 件） | **canonical** | 3 レコードの全フィールド照合・`brion` 走査 23 件 |
| **`migration/out/export/resolved_bottles.json`**（893 件） | **canonical** | `cuvee:…` の `_stub` facts・`haut-brion-1855` の `vintage: {}` |
| **`research/canonical_conflicts/REGISTER.md`** | **登録票** | 🔒 **読取のみ。`C-2` / `C-4` / `C-5` / `S-4` / `V-*` の記述範囲を確認するために参照。編集していない** |

### 🔴 到達しなかった／存在しなかった URL（**「無い」ことの記録**）

| URL | 結果 |
|---|---|
| 🔴 **`/nos-vins/chateau-haut-brion-rouge/chateau-haut-brion-rouge-1987/`** | 🔴 **HTTP 404** |
| 🔴 **`…/Fiche-technique_ChateauHBR_1987_FR.pdf`** | 🔴 **HTTP 404（本文は HTML。`%PDF` ではない）** |
| **`…/Fiche-technique_ChateauHBR_1988_FR.pdf`** | **HTTP 404** |
| **`/en/legal-notice`** | **HTTP 404**（正しくは `/en/legal-mentions/`） |
| 🔴 **1959 年グラーヴ格付の arrêté 原典** | 🔴 **Légifrance / INAO / BO-Agri のいずれからも本文に到達できなかった。**🏛 INAO 正本 CDC が「`classement de 1959`」「16 Châteaux ou Domaines」と明記するので存在と規模は確定しているが、**リストと色の別は未確認。** → Open Questions 4 |

### 🔴 §2a により **却下**したドメイン

🔴 **本調査で却下したドメインは 0 件である。**
🔴 **理由: `haut-brion.com` を採用する前に mentions légales を先に取得し、🏛 SIREN と突合してから 1 語も使わない手順を守ったため、look-alike に触れる前に確定した。**
⚠️ **ただし以下は「触れていないが罠になりうる」ものとして記録する ——**
- ⚠️ **`mission-haut-brion.com`**: 同一 mentions légales に列挙されており真正だが、**別の城のサイトである。本書では 1 語も使っていない。**
- ⚠️ **`clarendelle.com`**: 🏛 Agence Bio に `CLARENCE DILLON WINES` の公式サイトとして登録されている。**別法人・別ブランドのサイトであり、本書では 1 語も使っていない。**
- ⚠️ **`les-carmes-haut-brion` を名乗るドメイン群**: 🏛 SIREN 341826170 の別法人。**一切参照していない。**

### 🚫 使用していないもの

🚫 **Wikipedia、ワイン商・オークション・批評サイト（Wine-Searcher / Vivino / Decanter / Wine Advocate / Vinous ほか）、ネゴシアン資料は、事実の出典として一切使用していない。**
⚠️ **`bordeaux-vintage-*-guide` の canonical レコードが Parker のヴィンテージ評であることは §Canonical Conflict ⑥ で「canonical に何が入っているか」の記述として言及したが、事実の根拠としては用いていない。**

---

## Open Questions

### 🔴 物理ラベル・タスク（**店の実物でしか決着しない。番号付き**）

🔴 **1. 1987 の実ボトルのラベル 4 点を撮る。** ① `Appellation Pessac-Léognan Contrôlée` の有無（AOC は収穫の 19 日前に創設されている。名乗れたはずだが実装は未確認）／② `Pessac-Léognan` の独立行の有無／③ `CRU CLASSE DE GRAVES` の綴り（1989 は `DE`、1990–2000 は `DES`、2003 は `DE`）／④ `Premier Grand Cru Classé en 1855` の位置（1989 は appellation の**上**、1990 以降は**下**）。
🔴 **これが決まれば、1987 が「グラーヴ表記の最後の世代」か「ペサック＝レオニャン表記の最初の世代」かが確定する。**

🔴 **2. 2011 / 2015 / 2018 / 2019 の裏ラベルを撮る。** 表ラベルに appellation が無い以上、法定表示は裏にあるはずである。**`Appellation Pessac-Léognan Contrôlée` の実文言、アルコール度数、`Mis en bouteille au Château` の有無、輸入者表示。**

🔴 **3. 在庫している 2018 のボトルで、可能ならインポーターの成分表示（背面ラベル）を確認する。** 🔴 **城の HTML と城の PDF でカベルネの数値が入れ替わっている問題（§Winemaking）は、第三の造り手系資料が出れば決着する可能性がある。**

**4. 1993 のボトルで `CRU CLASSÉ DES GRAVES` の綴りを実読する。** 公式ボトルショットでは `DES` に読めるが、2003 のショットは `DE` である。🏛 CDC の法文は `Cru Classé de Graves`（単数）。**どちらが実際に刷られているかで、canonical に入れるべき文字列が変わる。**

### ❓ 公式が沈黙している事項

🔴 **5. 1987 のセパージュ。** 現行サイト・旧サイトのいずれにも無い。**canonical の `CS 48 / M 35 / CF 17` の出所は不明。**城に直接問い合わせる以外に手が無い。

🔴 **6. 1959 年グラーヴ格付の原典と、白の扱い。** 🏛 INAO 正本 CDC は「16 の Châteaux ou Domaines」と件数を書くが、リストも色の別も書かない。
🔴 **ブリーフは「Haut-Brion は 1959 年グラーヴ格付に赤・白の両方で載っている」と述べるが、本調査ではこれを確認できなかった。**むしろ **2019 年の白の表ラベルには `Cru Classé de Graves` の行が無い**（赤の 2003 年以前にはある）。**これは反証ではない（表ラベルに書かないだけかもしれない）が、確認されてもいない。** → §6.8

**7. 1993 の新樽比率。** 公式フィッシュに `Fûts neufs` の行が無い（1989 と 2011 以降にはある）。**「1993 も 72〜79% だった」とは言えない。**

**8. `Château Haut-Brion Blanc` の appellation 表示場所。** 表ラベルに無い。裏ラベルか首ラベルか。

**9. `La Clarté de Haut-Brion` の旧称。** canonical は「旧 Les Plantiers」と書くが、公式サイトに `Plantiers` の語は 1 度も現れない。**改称なのか新設なのかも公式からは判定できない。**

**10. INRA とのクローン研究。** canonical は「1975 年から、500 種以上」と書くが、公式サイトに `INRA` も `clone` も現れない。

**11. 1949 年以前の Bahans Haut-Brion。** 公式は「`dès les premiers millésimes du XXème siècle`」としか書かず、初ヴィンテージ年を特定していない。

**12. マロラクティック発酵。** 公式 `/savoir-faire` は発酵と熟成を詳述するが、MLF に一言も触れていない。**canonical の `obp_note` は「マロラクティック発酵後」と書く。公式に根拠が無い。**

### 🔍 THÉSEUS 側の未決事項

🔴 **13. `cuvee_state: exact` の根拠となっている evidence 文字列を、matcher 側で潰すべきか。**
🔍 **6 行すべてが `cuvee_state: "exact"` を持ち、その evidence が「`名称トークン集合一致: 'pessac leognan' ≡ 'Château Haut-Brion'`」である。共通トークンは空である。**
🔴 **この文字列は人間のレビュアーに対して、実際には行われていない照合が行われたと述べている。`source_quality_flags` は 6 行とも空配列で、警告も立っていない。**
🔴 **`_parts.label is null` の 152 行のうち 147 行が同じ形である。matcher 側の設計判断であり、本書では実行しない。** → §Canonical Conflict ⑤

**14. `haut-brion-1855` の `subregion = "Pessac-Léognan"`。** ヴィンテージを持たないレコードに AOC を付けると、1987 年 9 月 9 日以前を含む全期間について AOC を主張することになる。**時間軸を持たない層に時間依存の属性を置いてよいかは設計判断。**
