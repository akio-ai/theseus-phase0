# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 昇格判断は未実施**
> 🔴 **canonical にこの生産者のレコードは 5 件存在する**（ピュリニー村名 2 / ピュリニー 1er Cru 3）。
> **本書は研究記録であり、canonical を一行も変更していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者の公式サイトで確認**（一次資料）── 🔴 **本ドシエでは 1 件も使えていない。理由は下記。**
> `📄` 単一の非公式資料のみ（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `🏛` **公的登録簿・認証機関・appellation 公式資料**（SIRENE/RNE、Agence Bio、INSEE、INAO、BIVB）
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05
>
> ---
>
> 🔴 **本ドシエ最大の事実 ①ーー この生産者に公式サイトは存在しない。**
> **`bachelet-monnot.com` というドメインは実在する**（Namebay 登録、Microsoft 365 の MX、
> `v=spf1 include:spf.mailjet.com include:spf.protection.outlook.com -all`）**が、
> A レコードも AAAA レコードも無い。つまりメール専用ドメインであり、web サイトは立っていない。**
> `www.bachelet-monnot.com` も応答しない。**候補 12 ドメインを DNS で総当たりしたが、すべて NXDOMAIN か A レコード無し。**
> 🔴 **Agence Bio の公的登録簿でも `siteWebs` は空配列である。**
> → **したがって本ドシエは `✅`（公式サイト）レイヤーを一切持たない。**
> **代わりに `🏛`（公的登録簿・認証機関・appellation 公式資料）だけで組み立てた。**
>
> 🔴 **本ドシエ最大の事実 ②ーー 蔵はピュリニーに無い。Dezize-lès-Maranges（Saône-et-Loire 県）にある。**
> **2 つの独立した公的登録簿（SIRENE/RNE と Agence Bio）が同一住所を示す ——
> `15 GRANDE RUE, 71150 DEZIZE-LÈS-MARANGES`。**
> **OBP のリストに載っているのはピュリニー＝モンラッシェの 5 本だけだが、この造り手はピュリニーの造り手ではない。**
> → §Staff Notes 芯①
>
> 🔴 **本ドシエ最大の事実 ③ーー 有機認証の状態が「宙に浮いている」。**
> **Agence Bio の公的登録簿によれば、2023-08-04 に Ecocert France（`FR-BIO-01`）へ engagement。
> 2024 年参照の生産状態は `AB` と `C2` が併存。
> しかし証明書の状態は `ARRETEE`（＝停止）で、`dateArret` は 2025-02-25。
> Ecocert の証明書 URL は現在 404 を返す。**
> → **「ビオです」とも「ビオではありません」とも言えない状態である。** → §Farming / §Staff Notes ⚠️ ③

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Bachelet-Monnot**（`producer_heading`。🔍 intake の全 5 行が同一見出し） |
| **canonical 表記** | 🔍 **Domaine Bachelet-Monnot**（5 レコードすべて） |
| 🔴 **登記上の商号** | 🏛 **`DOMAINE BACHELET-MONNOT`**（SIREN **481461374**、SIRET `48146137400011`） |
| 🔴 **法人形態** | 🏛 **EARL**。INSEE カテゴリ juridique **`6598` = 「Exploitation agricole à responsabilité limitée」**（INSEE 公式ノメンクラチュア API で照合） |
| **主活動** | 🏛 **NAF `01.21Z` = 「Culture de la vigne」**（INSEE 公式ノメンクラチュア API で照合） |
| 🔴 **所在** | 🏛 **`15 GRANDE RUE, 71150 DEZIZE-LÈS-MARANGES`（Saône-et-Loire 県 / commune INSEE `71174`）**。緯度経度 `46.9109, 4.6549`（SIRENE）/ `46.9109, 4.6541`（Agence Bio） |
| 🔴 **経営者** | 🏛 **BACHELET, Marc Bernard André（1980 年 3 月生）ーー Gérant**<br>🏛 **BACHELET, Alexandre Julien Edouard（1982 年 11 月生）ーー Gérant**<br>（RNE 最終更新 2024-05-18） |
| **登記上の設立** | 🏛 **2005-01-31**。⚠️ **ただし `date_debut_activite`（活動開始日）は 2008-01-01 と別の日付である** |
| ⚠️ **事業所の商号** | 🏛 🔴 **事業所（SIRET `…0011`）の `nom_commercial` は `JEAN-FRANCOIS BACHELET`。** ❓ **登記はこの人物と法人の関係を説明していない** |
| 🔴 **同住所の別法人 ①** | 🏛 **`BACHELET - MONNOT`（SIREN **533569992**）ーー SAS（INSEE `5710`）、2011-07-01 設立、活動中。**<br>**NAF `46.34Z` = 「Commerce de gros (commerce interentreprises) de boissons」。**<br>**Marc = Président de SAS、Alexandre = Directeur Général。** ❓ **この SAS が何をしているかは登記から読み取れない** |
| **同住所の別法人 ②** | 🏛 **`GRPT FONCIER VITICOLE VIGNE BLANCHE`（SIREN 479996233）、`15 GRANDE RUE` 同番地、2004-11-22 設立、NAF `68.20B`** |
| **兄弟が関与する別法人** | 🏛 **`SCI PATERNE`（SIREN 881864805）ーー 2020-02-12 設立、2025-01-01 より本店 `3 RUE DU PIED DE LA FORÊT, 21190 MEURSAULT`、NAF `68.20B`。Marc = Gérant、Alexandre = Gérant et associé** |
| **公式サイト** | 🔴 **無し。** `bachelet-monnot.com` は MX のみ（A レコード無し）。Agence Bio 登録簿の `siteWebs` も空 |
| **連絡先** | 🏛 **Tel `03 85 91 16 82` / `contact@bachelet-monnot.com`**（Agence Bio 公的登録簿） |
| 🔴 **有機認証** | 🏛 ⚠️ **Agence Bio 事業者番号 `55726`。Ecocert France（`FR-BIO-01`）に 2023-08-04 engagement。<br>証明書状態 `ARRETEE`、`dateArret` 2025-02-25。証明書 URL は 404。** → §Farming |
| **canonical id（生産者）** | 🔍 **`producer:domaine-bachelet-monnot`**（intake パイプラインが導出。canonical に生産者マスタのファイルは無い） |

---

## Overview

🏛 🔴 **Dezize-lès-Maranges（Saône-et-Loire 県）に本拠を置く EARL。
現在の gérant は Marc Bachelet と Alexandre Bachelet の 2 名である。**

🔴 ⚠️ **この造り手について「造り手自身が語った言葉」を、本調査は一行も入手できていない。**
**公式サイトが存在せず、生産者が書いた fiche technique も見つからなかったからである。**
**したがって本ドシエには、テイスティングノートも、栽培哲学も、醸造工程も無い。**
**あるのは、公的登録簿が記録している「誰が・どこで・どういう法人形態で・どういう認証状態か」だけである。**

🏛 ✅ **Maranges は「Côte de Beaune の村名アペラシオン」である。**
BIVB（Bureau Interprofessionnel des Vins de Bourgogne）の公式アペラシオン資料は、こう書いている ——
**「Côte de Beaune の村名アペラシオン、Saône-et-Loire 県。（…）
生産地区は Saône-et-Loire 県に位置するが、このアペラシオンは Côte de Beaune の不可分の一部をなす。」**
**「Maranges の畑は、Côte-d'Or と Saône-et-Loire を結ぶ連結点をなす。」**

🔴 🏛 **そして、INAO の Puligny-Montrachet 原産地呼称仕様書（cahier des charges）は、
`Dezize-lès-Maranges` を
「aire de proximité immédiate（近接区域）」の Saône-et-Loire 県側リストに明記している。**
**この近接区域は「vinification、élaboration、élevage について例外的に認められる区域」と定義されている。**
→ 🔴 **つまり、Dezize に蔵を構えたまま Puligny-Montrachet を仕込み・熟成させることは、
appellation 規定上まったく正規の手続きである。**
**これは推測ではなく、仕様書 IV 章 3° に書かれた条文の帰結である。** → §Staff Notes 芯②

🔍 **THÉSEUS における状態は、Batch 5–8 でも異例に良い。**
**OBP 掲載 5 本のうち 3 本（1er Cru）が canonical release に直結し、
残る 2 本（村名）も生産者レベルまでは `producer:domaine-bachelet-monnot` に確定している。**
🔴 **だから本ドシエの価値はマッチングではない。中身が空であること、
そして空でない 2 件の中身が第三者点数で埋まっていることを、はっきりさせる点にある。** → §Canonical Conflict

---

## History

🔴 ⚠️ **本調査は、この造り手の沿革をほとんど取得できなかった。**
**公式サイトが存在しないため、創業の経緯・世代交代・畑の取得履歴は一切不明である。**

🏛 **公的登録簿から機械的に確定できるのは、以下の日付だけである。**

| 年月日 | 出来事（🏛 登記上の記録） |
|---|---|
| **2004-11-22** | **`GRPT FONCIER VITICOLE VIGNE BLANCHE` が `15 Grande Rue` に設立される**（NAF 68.20B・土地保有目的の法人形態） |
| **2005-01-31** | 🔴 **`DOMAINE BACHELET-MONNOT`（EARL、SIREN 481461374）が登記される** |
| **2008-01-01** | ⚠️ **同事業所の `date_debut_activite`。** ❓ **2005 年の登記と 2008 年の活動開始が 3 年ずれている理由は登記から読み取れない** |
| **2011-07-01** | 🔴 **`BACHELET - MONNOT`（SAS、SIREN 533569992）が同住所に設立される。NAF 46.34Z（飲料の卸売）** |
| **2020-02-12** | **`SCI PATERNE` 設立**（兄弟 2 名が経営） |
| **2023-08-04** | 🔴 **Agence Bio に有機の engagement。認証機関は Ecocert France（FR-BIO-01）** |
| **2025-01-01** | **`SCI PATERNE` の本店が Meursault（`3 rue du Pied de la Forêt, 21190`）に置かれる** |
| **2025-02-25** | 🔴 **Ecocert 証明書の `dateArret`。状態は `ARRETEE`** |

⚠️ 🔴 **「兄弟が 2005 年にドメーヌを創設した」とは、本ドシエでは言わない。**
**登記は「EARL が 2005-01-31 に設立された」ことと「現在の gérant が Marc と Alexandre である」ことを
別々に記録しているだけで、両者を結ぶ記述は無い。**
**さらに、事業所の `nom_commercial` は今も `JEAN-FRANCOIS BACHELET` のままである。**
→ §Staff Notes ⚠️ ②

⚠️ 🔴 **屋号の「Monnot」が何に由来するかは、公的登録簿にも appellation 資料にも一切現れない。**
**登記上の経営者に Monnot 姓の人物は存在しない。** → §Staff Notes ⚠️ ⑤

---

## Location

| | |
|---|---|
| **Country** | France 🏛 |
| **Region** | **Bourgogne** 🏛 |
| 🔴 **蔵の所在** | 🏛 **`15 Grande Rue, 71150 Dezize-lès-Maranges`（Saône-et-Loire 県 / INSEE commune `71174`）** |
| 🔴 **蔵が属する appellation** | 🏛 **Maranges**（Dezize-lès-Maranges は Maranges の 3 村の 1 つ） |
| **OBP 掲載ワインの appellation** | 🏛 **Puligny-Montrachet（Côte-d'Or 県）ーー 蔵とは別の県である** |
| 🔴 **両者の法的な接続** | 🏛 **Puligny-Montrachet 仕様書の「aire de proximité immédiate」に `Dezize-lès-Maranges` が明記されている** |
| ⚠️ **自社畑の面積・区画** | 🔴 **公的資料に一切存在しない。本ドシエでは面積を一切主張しない。** → §Staff Notes ⚠️ ① |

### 🏛 Maranges（蔵のある側）ーー BIVB 公式アペラシオン資料

- **「Côte de Beaune の村名アペラシオン、Saône-et-Loire 県。」**
- **生産 3 村: Cheilly-lès-Maranges / Dezize-lès-Maranges / Sampigny-lès-Maranges**
- **「生産地区は Saône-et-Loire 県に位置するが、このアペラシオンは Côte de Beaune の不可分の一部をなす。」**
- **Premier Cru に格付けされた Climat は 7 つ。**
  🏛 **Dezize-lès-Maranges の 1er Cru: `La Fussière` / `Le Croix Moines` / `Le Clos de la Fussière`**
- 🏛 **テロワール（BIVB）**ーー「**斜面は Côte de Beaune の並びには従わないが、地質的な起源と性質は同じである。
  多様な丘と斜面の織物。最も多い南／南東向きの露出は、標高 240〜400 m の間にある。**」
  「**Sampigny と Dezize は、Santenay 南部の Climat を共有する ―― 褐色石灰質土壌と石灰質マルヌ。**」
- 🏛 **生産規模（2022 年時点の栽培面積）**: 赤 **180.77 ha**（うち 1er Cru 80.04 ha）／白 **19.11 ha**（うち 1er Cru 5.82 ha）
  → 🔴 **Maranges は圧倒的に赤（Pinot Noir）の産地であり、白は全体の 1 割に満たない。**
- 🏛 **AOC 誕生は 1988 年収穫から。**
- 🏛 **INAO 仕様書**: 「**ブドウの収穫、醸造、élaboration、élevage は、Saône-et-Loire 県の以下の commune の領域で行われる ――
  Cheilly-lès-Maranges、Dezize-lès-Maranges、Sampigny-lès-Maranges。**」

### 🏛 Puligny-Montrachet（OBP に載っている側）ーー BIVB / INAO 公式

- **「Côte de Beaune の村名アペラシオン、Côte-d'Or 県。」** **AOC 制定は 1937 年。**
- 🏛 **INAO 仕様書 IV 章 1°**: 「**ブドウの収穫、醸造、élaboration、élevage は、
  Côte-d'Or 県の Puligny-Montrachet の commune の領域で行われる。**」
- 🔴 🏛 **同 IV 章 3°「aire de proximité immédiate」**（vinification / élaboration / élevage について例外的に認められる区域）
  **の Saône-et-Loire 県リストに、`Cheilly-lès-Maranges`・`Dezize-lès-Maranges`・`Sampigny-lès-Maranges` の 3 村がすべて入っている。**
- 🏛 **テロワール（BIVB）**ーー「**畑はしばしば褐色石灰質土壌、あるいはマルヌ質の泥灰岩‐石灰質の層が交互に現れる石灰岩を占め、
  時に深く、時に硬い岩の直上にある。粘土質シルトは上部で厚く、斜面の下部では細粒になる。
  東向きおよび南東向きの露出、標高 230〜320 m。**」
- 🏛 **1er Cru に格付けされた Climat は 17。**
  **Sous le Puits / La Garenne / Hameau de Blagny / La Truffière / Champ Gain / Les Chalumaux /
  Champ Canet / Clos de la Garenne / `Les Folatières` / Le Cailleret / Les Demoiselles / Les Pucelles /
  Clavaillon / Les Perrières / Clos de la Mouchère / Les Combettes / `Les Referts`**
  → 🔴 **OBP の 2 つの 1er Cru 名は、いずれも公式の 17 climat リストに実在する。**
- 🏛 **生産規模（2018 年時点）**: 白 **95.92 ha**（うち 1er Cru **90.97 ha**）／赤 **0.36 ha**
  → 🔴 **Puligny は事実上ほぼ全部が白であり、しかも 1er Cru の面積が村名を上回るという、極めて特異な構成である。**

---

## Farming

🔴 🏛 **本ドシエで最も価値のある一次情報は、この節にある。ただし結論は「確定していない」である。**

**Agence Bio（フランス農業省所管の有機農業公的機関）の公開登録簿には、次のレコードが存在する。**

| 項目 | 値（🏛 Agence Bio 公開 API） |
|---|---|
| **事業者番号** | **`55726`** |
| **商号** | **`DOMAINE BACHELET-MONNOT`** ／ 通称 `DOMAINE BACHELET-MONNOT  BACHELET Alexandre` |
| **SIRET** | `48146137400011`（SIRENE の記録と一致） |
| **代表** | `ALEXANDRE BACHELET` |
| **活動** | **`Production` / 年鑑カテゴリ `Viticulture`** |
| 🔴 **生産品目** | **`Raisin de cuve`（醸造用ブドウ、コード 01.21.12）**<br>**`Jachère, gel entrant en rotation`（休閑地・緩衝帯を含む輪作休耕地）** |
| 🔴 **生産状態（2024 年参照管理）** | 🔴 **`AB` と `C2` の両方が併記されている**（両品目とも） |
| **認証機関** | 🏛 **`Ecocert France`（EU 管理番号 `FR-BIO-01`）** |
| 🔴 **証明書の状態** | 🔴 ⚠️ **`ARRETEE`（停止）** |
| **engagement 日** | **2023-08-04**（`datePremierEngagement` も同日） |
| 🔴 **arrêt 日** | 🔴 **2025-02-25** |
| **証明書 URL** | ⚠️ **`certificat.ecocert.com/entreprise/75AEE785-…` は現在 `404`（「お探しのページは存在しません」）を返す** |
| **`mixite`** | **`Non`**（＝有機と慣行の混在経営ではない、と申告されている） |
| **販売区分** | 個人向け販売 / 小売業者向け / 飲食店向け（卸売は `false`） |

### 🔴 この登録簿から言えること・言えないこと

**言えること（🏛 一次資料）**
1. **この造り手は 2023 年 8 月 4 日に、フランスの公的な有機農業の枠組みに正式に登録した。**
   **それが初回の engagement である（`datePremierEngagement` = `dateEngagement`）。**
2. **2024 年の参照管理年において、品目「醸造用ブドウ」には `AB`（認証済み有機）と
   `C2`（転換 2 年目）の両方の状態が記録されている。**
   → **区画によって進捗が違う、いわゆる段階的転換の途中にあった、と読むのが登録簿の記法に忠実である。**
3. **認証機関は Ecocert France であった。**
4. 🔴 **その証明書は 2025-02-25 付で `ARRETEE`（停止）となっており、Ecocert の証明書ページは現在 404 を返す。**

**言えないこと（⚠️ 出典が沈黙している）**
- ⚠️ 🔴 **`ARRETEE` が「認証をやめた」のか「認証機関を乗り換えた」のかは、登録簿から判別できない。**
  **Agence Bio の当該レコードには証明書が 1 件しか無く、別の認証機関のレコードは存在しない**
  （SIRET 検索・事業者番号検索の両方で `nbTotal = 1`）。
- ⚠️ **転換開始前（2023 年 8 月より前）に何をしていたかは、この登録簿の範囲外である。**
- ⚠️ **有機以外の認証（HVE / Demeter / Biodyvin / Terra Vitis）への言及は、
  本調査が参照したどの公的資料にも一切現れなかった。**
- ⚠️ **栽培密度・仕立て・樹齢・収量の実績値は、公的資料には無い。**

### 🏛 appellation レベルの栽培規定（**domaine 固有ではない。混同禁止**）

🔴 **以下は INAO の Puligny-Montrachet 仕様書の条文であり、すべての生産者に等しくかかる規定である。
「Bachelet-Monnot はこうしている」という意味では断じてない。**

| 項目 | Puligny-Montrachet 仕様書の規定 |
|---|---|
| **白の品種** | **`chardonnay B` および `pinot blanc B`** 🔴 **（＝仕様書上は 100% Chardonnay とは限らない）** |
| **赤の品種** | 主要品種 `pinot noir N`、補助品種 `chardonnay B` / `pinot blanc B` / `pinot gris G` |
| **灌漑** | 禁止 |
| **1er Cru の収量** | **白 55 hl/ha**（butoir 62 hl/ha） |
| **村名の収量** | ⚠️ 🔴 **抽出テキストが `45 57` と二重に出る。**この文書は 2010 年の全国異議申立手続版で、削除線と太字が本文抽出では区別できない。**本ドシエでは村名の基準収量を数字で断定しない**（butoir は 64 hl/ha） |
| **補糖後の上限アルコール** | **村名 13.5% / 1er Cru 14%** |
| 🔴 **木片の使用** | 🔴 **「L'utilisation de morceaux de bois est interdite」ーー オーク・チップの使用は禁止** |
| **連続式圧搾機** | 禁止 |
| **赤のリンゴ酸** | 瓶詰め段階で 0.4 g/L 以下 |
| **残糖上限** | 白 3 g/L（総酸 2.7 g/L H₂SO₄ 以上なら 4 g/L）、赤 2 g/L |

---

## Winemaking

🔴 ⚠️ **本調査は、この造り手の醸造について一件も確定できなかった。**

**公式サイトが存在せず、生産者が書いた fiche technique も発見できなかった。
発酵容器、樽のサイズ、新樽比率、élevage の月数、バトナージュの有無、澱との接触、
瓶詰め時期、アルコール度数、生産本数 ―― そのいずれについても一次資料が存在しない。**

⚠️ 🔴 **輸入元・小売・評論のページには醸造の数字が書かれている。本ドシエはそれを一切採用しない。**
**理由は、それらのページが domaine による執筆であることを立証できなかったからである**
（レターヘッド、署名、domaine 名義の PDF、domaine サイトからのリンクのいずれも確認できない）。
→ §Sources「棄却した資料」

🔴 ⚠️ **にもかかわらず、canonical にはすでに醸造の数字が書かれている。**
**`bachelet-monnot-puligny-2022` / `-2023` の `aging` は `"10 months barrel and tank"`、
`winemaking` は「樽とタンクの組み合わせで発酵・熟成（10ヶ月）」である。**
**この数字を裏づける一次資料を、本調査は発見していない。** → §Canonical Conflict **CC-3**

**言えるのは appellation 規定だけである** ―― 🏛 **オーク・チップの使用は Puligny-Montrachet では禁止されている。
連続式圧搾機も禁止されている。補糖後の総アルコールは村名 13.5%、1er Cru 14% を超えられない。**

---

## Style

🔴 ⚠️ **この造り手自身のテイスティングノートは、本調査では 1 件も入手できていない。**
**造り手が自分のワインをどう説明しているかは、完全に不明である。**

🏛 **以下は BIVB のアペラシオン公式資料による「アペラシオンの一般的性格」であり、
Bachelet-Monnot のワインの描写ではない。フロアで使う際は必ず「ピュリニーというアペラシオンは」と前置きすること。**

### 🏛 Puligny-Montrachet 白（BIVB 公式）

「**金糸で縫われたような輝く衣に、緑がかった反射の光輪。この色調は年齢とともに強度を増す。
ブーケはサンザシ、熟した葡萄、アーモンドペースト、ヘーゼルナッツ、琥珀、レモングラス、青りんごを束ねる。
乳性の香り（バター、焼きたてのクロワッサン）と鉱物的な香り（火打石）は常であり、蜂蜜もそうである。
ボディとブーケが繊細な調和へ融け合う ―― 揺るぎない性質と際立った凝縮のもとに、あらゆる優美さが宿る。**」

🏛 **BIVB のソムリエ助言** ――「**凝縮と大いなる気品が Puligny-Montrachet とその Premier Cru の生地をなす。
均衡に満ちたこの大きな芳香的複雑さは、洗練された様式と結びついて、
繊細でありながら同時に豊かな料理を要求する。
ソースを纏った見事な家禽にも、きのこを添えた仔牛のポワレにも等しく寛ぐ。
フォワグラ、オマール、ラングスト、海の魚のグリルやポワレとは見事に響き合う。
チーズではシェーヴルとルブロション、そしてブリ・ド・モーのような白カビの軟質チーズを求める。**」
🏛 **供出温度 11〜13 °C。**

### 🏛 Maranges 白（BIVB 公式。**参考。OBP には Maranges は載っていない**）

「**繊細な金色。白い花（サンザシ、アカシア、スイカズラ）を母語のように語り、
年齢とともに火打石や蜂蜜の調子が加わって個性をつくる。
しなやかで繊細な調子に展開し、押し出しは強くないが細部を仕上げることに心を砕く。**」

⚠️ 🔴 **canonical にはこの造り手のワインの `tasting` / `tasting_en` が既に書かれている
（村名 2 件のみ。「石灰岩の湿り気、グリーンアップル、柑橘の皮、白桃、石、塩気」等）。
これは造り手の言葉ではない。**出典は canonical 内に記録されていない。 → §Canonical Conflict **CC-3**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake / mapping より。**全 5 本**）

| # | OBP 印字（`original_raw_line` 由来） | VT | 価格 | 🔍 解決状態 | 🏛 appellation 側の裏取り |
|---|---|---|---|---|---|
| 1 | **Puligny-Montrachet** | **2023** | **$380** | 🔴 **`research_shell`（`rs:pro:3b2de71b94633613`）。生産者は `producer:domaine-bachelet-monnot` に確定。cuvée / vintage は canonical に紐づいていない** | 🏛 **AOC Puligny-Montrachet は実在。1937 年制定** |
| 2 | **Puligny-Montrachet** | **2022** | **$320** | 🔴 **同上（同一 shell に 2 行が束ねられている）** | 🏛 同上 |
| 3 | **'Les Folatières,' Puligny-Montrachet Premier Cru** | **2023** | **$880** | ✅🔍 **`canonical_release`**<br>`cuvee:domaine-bachelet-monnot-les-folatieres` / `vintage:…-2023` | 🔴 🏛 **`Les Folatières` は INAO 仕様書の 1er Cru climat リストに実在** |
| 4 | **'Les Folatières,' Puligny-Montrachet Premier Cru** | **2022** | **$680** | ✅🔍 **`canonical_release`** / `vintage:…-2022` | 🔴 🏛 同上 |
| 5 | **'Les Referts,' Puligny-Montrachet Premier Cru** | **2022** | **$640** | ✅🔍 **`canonical_release`**<br>`cuvee:domaine-bachelet-monnot-les-referts` / `vintage:…-2022` | 🔴 🏛 **`Les Referts` は INAO 仕様書の 1er Cru climat リストに実在** |

🔴 **セクションは 5 行とも `FRANCE | WHITE > BURGUNDY`、`section_start_page` は 12。**
**メニュー原文の引用符は タイポグラフィック引用符（`‘…,’`）である。**

⚠️ 🔴 **依頼時の申し送りでは「5 本すべてが `match_state = exact`」とされていたが、
`research/out/t-01/mapping.json` を実読した結果は異なる。**
**canonical release に到達しているのは 3 本（1er Cru）だけで、
村名 2 本は `resolved_to: "research_shell"`（`status: research_pending` / `published: false` /
`excluded_from_recommendations: true`）である。**
🔍 **生産者レベルでは 5 本とも exact に解決している** ので、
**「生産者は 5/5 確定、release は 3/5 確定」というのが機械的に正確な言い方である。** → Open Questions 1

### 🏛 `Les Folatières` とは何か（INAO 仕様書ベース。**domaine の話ではない**）

🔴 **`Les Folatières` は、単一の地籍地名ではなく 4 つの lieudit を束ねた climat である。**
**INAO 仕様書の 1er Cru 表は、climat `Les Folatières` に対して次の 4 つの lieudit を並べている ――**

| climat | lieudit | 色 |
|---|---|---|
| **Les Folatières** | **Es Folatières** | Blanc, rouge |
| | **En la Richarde dit Les Folatières** | Blanc, rouge |
| | **Peux Bois dit Les Folatières** | Blanc, rouge |
| | **Au Chaniot dit Les Folatières** | Blanc, rouge |

→ 🔴 **つまり「Folatières」と名乗れる範囲は、地籍上は 4 つの区画にまたがる。
造り手ごとに、その中のどこを持っているかは違いうる。**
⚠️ **Bachelet-Monnot がこの 4 つのどこを持っているかは、本調査では一切不明である。**

### 🏛 `Les Referts` とは何か（INAO 仕様書ベース）

| climat | lieudit | 色 |
|---|---|---|
| **Les Referts** | **Les Referts** | Blanc, rouge |
| **Les Perrières** | 🔴 **Les Perrières dit Les Referts** | Blanc, rouge |

→ 🔴 **仕様書上、`Les Referts` という地名は 2 か所に現れる ――
climat `Les Referts` 本体と、climat `Les Perrières` の下にある lieudit「Les Perrières dit Les Referts」である。**
**したがって「Referts」という語だけでは、仕様書レベルでも climat が一意に決まらない。**
⚠️ **ラベル表記としてどちらを名乗っているかは、本調査では確認できていない。** → Open Questions 4

### 🏛 参考 ―― Puligny-Montrachet の 1er Cru 昇格に関する条文

🔴 🏛 **仕様書 IV 章 2° c)** ――「**`Montrachet`、`Chevalier-Montrachet`、`Bâtard-Montrachet`、
`Bienvenues-Bâtard-Montrachet`、`Criots-Bâtard-Montrachet` の各原産地呼称の区画境界内に位置する畑から得られたワインは、
原産地の climat 名を付さずに『premier cru』の表示を伴う原産地呼称 `Puligny-Montrachet` を名乗ることもできる。**」
→ **「climat 名の無い Puligny 1er Cru」が制度上ありうる、ということ。OBP の 3 本はいずれも climat 名付きである。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① リストにあるのはピュリニーだけだが、この造り手はピュリニーの造り手ではない。蔵はマランジュにある。**
「**バシュレ＝モノの蔵は、ピュリニー＝モンラッシェではなく、
その南、ソーヌ＝エ＝ロワール県のドゥジーズ＝レ＝マランジュにあります。**
**マランジュはコート・ド・ボーヌの村名アペラシオンで、
ボルドーでいえば県境をまたいだ位置にあたります。**
**ブルゴーニュワイン委員会（BIVB）の公式資料は
『生産地区はソーヌ＝エ＝ロワール県に位置するが、このアペラシオンはコート・ド・ボーヌの不可分の一部をなす』
と書いています。**
**当店のリストに載っているのは彼らのピュリニーだけですが、彼らの本拠地はマランジュです。**」

**② 「マランジュの蔵でピュリニーを造る」のは、規定上まったく正規である。**
「**INAO の原産地呼称仕様書には『近接区域（aire de proximité immédiate）』という規定があり、
醸造・熟成についてはこの区域内で行うことが例外的に認められています。**
**ピュリニー＝モンラッシェの近接区域リストに、ドゥジーズ＝レ＝マランジュは明記されています。**
**つまり、ブドウはピュリニーで穫り、蔵はマランジュ ―― これは規定に沿った正規の形です。**」

**③ 2 つの畑名は、どちらもピュリニーの公式な 1er Cru クリマである。フォラティエールは 4 つの地籍地名の束。**
「**ピュリニー＝モンラッシェのプルミエ・クリュは公式に 17 クリマあり、
『レ・フォラティエール』も『レ・ルフェール』もその中に実在します。**
**とくにフォラティエールは、地籍上は 4 つの地名 ――
Es Folatières、En la Richarde、Peux Bois、Au Chaniot ―― を束ねた大きなクリマです。
だから造り手によって、同じフォラティエールでも見ている斜面が違います。**
**なお、ピュリニーは白の畑 95.92 ヘクタールのうち 90.97 ヘクタールがプルミエ・クリュという、
村名よりプルミエ・クリュの方が広いという珍しい村です。**」

### 追加で使える一手

- **アペラシオンの性格を言うとき（BIVB 公式の言葉として）**: 「委員会の公式資料は、ピュリニーの白を
  『**サンザシ、熟した葡萄、アーモンドペースト、ヘーゼルナッツ、琥珀、レモングラス、青りんご**』、
  そして『**バターや焼きたてのクロワッサンといった乳性の香りと、火打石のような鉱物的な香りは常である**』
  と描いています。**ただしこれはアペラシオンの一般的性格であって、この造り手のワインの描写ではありません。**」
- **合わせ**: 「委員会の助言では **フォワグラ、オマール、ラングスト、海の魚のグリルやポワレ**、
  チーズなら **シェーヴル、ルブロション、ブリ・ド・モー**。**供出は 11〜13 度**とされています。」
- **テロワール**: 「ピュリニーの畑は **標高 230〜320 メートル、東から南東向き**。
  **褐色石灰質土壌、あるいは泥灰岩と石灰岩が交互に現れる層**で、
  **上部では粘土質シルトが厚く、斜面の下では細粒になる**と公式資料は書いています。」
- **有機について訊かれたら**（⚠️ **下の禁止事項 ③ を必ず読んでから**）:
  「**フランスの有機農業公的登録簿（Agence Bio）には、2023 年 8 月にエコセールで登録した記録があります。
  ただし現在の証明書の状態は『停止』となっており、
  乗り換えなのか取りやめなのかは公的資料からは判別できません。
  ですので当店では『ビオです』とは申し上げていません。**」

### ⚠️ 言ってはいけないこと（**一次資料に根拠が無い／出典が沈黙している**）

1. 🔴 ⚠️ **面積を言わない。ヘクタール数を一切口にしない。**
   **自社畑の面積、所有区画、買いブドウの有無 ―― どれも公的資料に存在しない。**
   **「20 ヘクタール」「24 ヘクタール」といった数字が世に流布しているが、
   本ドシエはそれを裏づける一次資料を持っていない。**
2. 🔴 ⚠️ **「兄弟が 2005 年にドメーヌを創設した」と言わない。**
   **登記が記録しているのは「EARL が 2005-01-31 に設立された」ことと
   「現在の gérant が Marc（1980 年生）と Alexandre（1982 年生）である」ことだけで、両者を結ぶ記述は無い。**
   **さらに活動開始日は 2008-01-01 と別であり、事業所の商号は今も `JEAN-FRANCOIS BACHELET` である。**
   言うなら「**現在は Marc と Alexandre の Bachelet 兄弟が経営しています**」まで。
3. 🔴 ⚠️ **「ビオです」「オーガニックです」「ビオディナミです」と言い切らない。**
   **公的登録簿の証明書状態は `ARRETEE`（2025-02-25 付）であり、Ecocert の証明書ページは 404 を返す。
   2024 年参照の生産状態は `AB` と `C2` が併存しており、全区画が認証済みだったとも言えない。**
   **ビオディナミについては、認証団体（Demeter / Biodyvin）のどの資料にも一切現れなかった。**
4. 🔴 ⚠️ **醸造の数字を言わない。**
   **樽のサイズ、新樽比率、熟成月数、バトナージュ、澱との接触、野生酵母、アルコール度数、生産本数 ――
   一次資料はゼロである。**
   🔴 **canonical に書かれている `"10 months barrel and tank"` も、本調査では裏が取れていない。フロアで復唱しない。**
5. ⚠️ **屋号の「Monnot」の由来を説明しない。**
   **公的登記の経営者に Monnot 姓の人物はおらず、由来を述べた一次資料は存在しない。**
6. 🔴 ⚠️ **`Domaine Denis Bachelet` と混同しない。これは完全に別のドメーヌである。**
   🏛 **Denis Bachelet は `RUE DE LA PETITE ISSUE, 21220 GEVREY-CHAMBERTIN`（Côte-d'Or 県、コート・ド・ニュイ）。**
   🏛 **Bachelet-Monnot は `15 GRANDE RUE, 71150 DEZIZE-LÈS-MARANGES`（Saône-et-Loire 県、コート・ド・ボーヌ南端）。**
   **県が違い、コートが違い、色が違う（ドニ・バシュレは赤、バシュレ＝モノは白）。**
   **当店のリストでは、ドニ・バシュレは `FRANCE | RED > BURGUNDY`（2006 コート・ド・ニュイ $380 /
   1991 ジュヴレ $720）に、バシュレ＝モノは `FRANCE | WHITE > BURGUNDY` に載っている。**
7. 🔴 ⚠️ **「バシュレ」という姓だけで話を進めない。ドゥジーズ村には別のバシュレが何軒もいる。**
   🏛 **同じ Dezize-lès-Maranges の公的登記に、`EARL DOMAINE BERTRAND BACHELET`（4 rue des Maranges、2020 年設立）、
   `JEAN BACHELET`（Grande Rue、1988 年設立）、`BERNARD BACHELET`、`BACHELET FRÈRES` などが存在する。**
   **必ず「バシュレ＝モノ」とハイフンまで込みで言うこと。**
8. ⚠️ **「ピュリニーの畑を持っています」以上のことを畑について言わない。**
   **フォラティエールの 4 つの lieudit のどれを持っているか、ルフェールが climat 本体か
   『Les Perrières dit Les Referts』側かは、いずれも本調査では不明である。**
9. ⚠️ **「シャルドネ 100%」と断定しない。**
   🏛 **INAO 仕様書は、Puligny-Montrachet 白の品種を `chardonnay B` **および** `pinot blanc B` と定めている。**
   **この造り手が 100% シャルドネであると述べた一次資料は存在しない。**
   （canonical の村名 2 件には `grapes: ["Chardonnay 100%"]` と書かれているが、出典は記録されていない。）
10. ⚠️ **第三者点数を口にしない。**
    🔴 **canonical の村名 2 件には `points: 91` / `points: 90`、`obp_note` に「89〜91点（ヴィナス）」と書かれているが、
    本調査ではその出典を確認していない。**
    **公式ソース原則により、評論媒体の点数は本ドシエの根拠にならない。**
11. ⚠️ **公式サイトを案内しない。存在しない。**
    **`bachelet-monnot.com` はメール用のドメインであって、web サイトは立っていない。**
12. ⚠️ **同住所の SAS `BACHELET - MONNOT`（飲料卸売）を「ネゴシアン部門です」と説明しない。**
    **登記は NAF コードしか語っておらず、何を扱っているかは書かれていない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **3 件を escalate する。いずれも実行していない。**

---

### **CC-1 — `S-2`（銘柄名に二重引用符が埋め込まれている）**

1. **衝突する canonical ID**
   - `bachelet-monnot-referts-2022` → `name` = `"\"Les Referts\""`
   - `bachelet-monnot-folatieres-2022` → `name` = `"\"Les Folatières\""`
   - `bachelet-monnot-folatieres-2023` → `name` = `"\"Les Folatières\""`
2. **なぜ問題か**
   **`name` フィールドの値そのものに `"` 文字が 2 つ含まれている。表示層で引用符を付ける実装と二重になり、
   また文字列比較・スラグ生成・fuzzy マッチのスコアに影響する。**
3. **証拠**
   🔍 **`~/Theseus_Project/index.html` の canonical レコードを JSON パースして確認。3 件とも `name` の先頭と末尾が `"` である。**
   🔍 **副作用が実測できている ―― `research/out/t-01/review.json` の別行（`Les Faconnières` / `Les Fuées` /
   `Les Murgers`）の fuzzy 候補として、`cuvee:domaine-bachelet-monnot-les-folatieres`（`"Les Folatières"`）と
   `cuvee:domaine-bachelet-monnot-les-referts`（`"Les Referts"`）が 0.72〜0.76 のスコアで浮上している。**
4. **OBP への影響**
   **今回の 5 本の解決は妨げていない（3 本は exact に到達）。ただし他生産者の climat 名に対する誤候補を生んでいる。**
5. **推奨（🔴 DO NOT EXECUTE）**
   **`S-2` ファミリー（Batch 5–7 で計 9 件確認済み）の一括処理に合流させる。新しい番号は開かない。単独修正はしない。**
6. **Confidence: High**（機械的に確認済み）

---

### **CC-2 — 同一 cuvée 内で `classification` 文字列が揺れている（未採番）**

1. **衝突する canonical ID**
   - `bachelet-monnot-folatieres-2022` → `classification` = **`"Puligny-Montrachet Premier Cru"`**
   - `bachelet-monnot-folatieres-2023` → `classification` = **`"Puligny-Montrachet 1er Cru"`**
   - （`bachelet-monnot-referts-2022` は `"Puligny-Montrachet Premier Cru"`）
2. **なぜ問題か**
   🔴 **同じ cuvée（`cuvee:domaine-bachelet-monnot-les-folatieres`）の 2 ヴィンテージが、
   異なる格付け文字列を持っている。`subregion` は 3 件とも `"Puligny-Montrachet Premier Cru"` で揃っており、
   ずれているのは `classification` だけである。**
   **格付けでの絞り込み・グルーピング・表示が、ヴィンテージによって別扱いになる。**
3. **証拠** 🔍 **canonical レコードの直接パース（上記 3 件）。**
4. **OBP への影響**
   **マッチングは通っている（`Les Folatières` 2022 / 2023 とも `canonical_release`）。影響は表示と集計側に限られる。**
5. **推奨（🔴 DO NOT EXECUTE）**
   **`Premier Cru` / `1er Cru` の表記ゆれは、本生産者だけの問題ではない可能性が高い。
   全 canonical を横断して同種のゆれを数えてから、正規表記を 1 つ決めるべきである。**
   ⚠️ 🔴 **既知ファミリー（`C-1` / `V-1` / `V-3` / `V-4` / `S-2`）のいずれにも当てはまらない。
   新しい番号を本ドシエで勝手に開くことはしない。採番の要否は owner 判断とする。**
6. **Confidence: High**（機械的に確認済み。ただし「新ファミリーか単発か」は未調査）

---

### **CC-3 — canonical の中身に、出典不明の醸造数値と第三者点数が入っている**

1. **衝突する canonical ID**
   - `bachelet-monnot-puligny-2022`
   - `bachelet-monnot-puligny-2023`
2. **なぜ問題か**
   🔴 **この 2 件には、本調査がどの一次資料でも確認できなかった内容が書かれており、
   しかもその一部は `obp_note` としてフロアが読み上げる前提の文面になっている。**

   | フィールド | 値 | 本調査での裏取り |
   |---|---|---|
   | `aging` | `"10 months barrel and tank"` | ⚠️ **一次資料なし** |
   | `winemaking` | 「樽とタンクの組み合わせで発酵・熟成（10ヶ月）」 | ⚠️ **一次資料なし** |
   | `grapes` | `["Chardonnay 100%"]` | ⚠️ **INAO 仕様書は `chardonnay B` と `pinot blanc B` を認めている。domaine 側の言明なし** |
   | `points` | `91`（2022）/ `90`（2023） | ⚠️ **出典が canonical 内に記録されていない** |
   | `obp_note` / `obp_note_en` | **「89〜91点（ヴィナス）」を含む** | 🔴 ⚠️ **評論媒体の点数がフロア用文面に直接埋め込まれている** |
   | `tasting` / `terroir` | 「石灰岩の湿り気、グラニー・スミス…」等 | ⚠️ **造り手の言葉ではない。出典不明** |

   🔴 **なお `description` の「ドメーヌ・バシュレ＝モノはマランジュ拠点」という記述だけは、
   本調査が 2 つの公的登録簿で裏を取れた。正しい。**
3. **証拠** 🔍 **canonical レコードの直接パース。🏛 対照は INAO 仕様書・BIVB 公式資料・Agence Bio・SIRENE。**
4. **OBP への影響**
   🔴 **直接的。`obp_note` はフロアが読む文面であり、
   本ドシエの §Staff Notes ⚠️ ④・⑨・⑩ と正面から矛盾する。**
   **さらに構造的な非対称がある ―― 価格の高い 3 本（$880 / $680 / $640、いずれも 1er Cru）の canonical は
   `name` / `vintage` / `subregion` / `classification` / `glassware` / `serving_temp` / `tags` だけの空殻で、
   `description` も `tasting` も `obp_note` も無い。**
   **一方、安い 2 本（$380 / $320、村名）だけが出典不明の内容で満たされている。**
   🔴 **つまり、いま OBP で最も語りにくいのは最も高いボトルである。**
5. **推奨（🔴 DO NOT EXECUTE）**
   - **`points` と `obp_note` 内の評論点数の扱い方針（残す／出典必須にする／落とす）を先に決める。
     これは本生産者ローカルの問題ではなく、canonical 全体の方針判断である。**
   - **`aging` / `winemaking` / `grapes` は、生産者由来の一次資料が得られるまで
     「暫定」であることが読み手に分かる形に落とすのが安全である。**
   - **1er Cru 3 件の空殻を埋める作業は、埋める材料が無い以上、着手すべきでない。**
6. **Confidence: High**（canonical 側の記載は機械確認済み。「一次資料が存在しない」ことの確証は
   本調査の探索範囲内での不在証明であり、Medium-High）

---

### 🔴 **偽陽性として除外リストに載せるもの（重複ではない）**

**`Domaine Denis Bachelet`（canonical: `bachelet-cote-de-nuits-2006` / `bachelet-gevrey-1991`）は、
`Domaine Bachelet-Monnot` とはまったく別のドメーヌである。canonical の重複ではない。**

| | Domaine Bachelet-Monnot | Domaine Denis Bachelet |
|---|---|---|
| 🏛 **登記住所** | **15 Grande Rue, 71150 Dezize-lès-Maranges** | **Rue de la Petite Issue, 21220 Gevrey-Chambertin** |
| 🏛 **SIREN** | **481461374**（EARL、2005 設立） | **424004547**（`DOMAINE BACHELET`、NAF 01.21Z、1999 設立）／ **349338939**（`DENIS BACHELET`、NAF 68.20B、1986 設立） |
| **県 / コート** | Saône-et-Loire / **Côte de Beaune 南端** | Côte-d'Or / **Côte de Nuits** |
| 🔍 **OBP セクション** | `FRANCE \| WHITE > BURGUNDY` | `FRANCE \| RED > BURGUNDY` |
| 🔍 **canonical の色** | Blanc | Rouge |

🔴 **これは canonical conflict として報告しない。近似名の衝突として除外リストに永続保存する。**
**同種の衝突リスクとして、Dezize-lès-Maranges 村内の別 Bachelet 法人も併記しておく ――
🏛 `EARL DOMAINE BERTRAND BACHELET`（SIREN 888070463）、`JEAN BACHELET`（349861393）、
`BERNARD BACHELET`（778580324、閉鎖）、`BACHELET FRÈRES`（411750987、閉鎖）。**

---

## Sources

### 🔴 公式サイトの真正性チェック（**必須手順。結論: 公式サイトは存在しない**）

**手順と結果**

| 手順 | 結果 |
|---|---|
| **候補ドメインの DNS 総当たり（12 件）** | `bachelet-monnot.com` / `.fr` / `.net` / `.eu` / `.wine`、`bacheletmonnot.*`、`domaine-bachelet-monnot.*`、`domainebacheletmonnot.com` ―― **`bachelet-monnot.com` 以外はすべて NXDOMAIN** |
| 🔴 **`bachelet-monnot.com` の実体** | **A / AAAA レコード無し。** `www` も同様。**HTTP / HTTPS とも接続不能（`http=000`）**<br>**存在するのは MX（`bacheletmonnot-com02b.mail.protection.outlook.com`）、TXT（`MS=ms19654780`、`v=spf1 include:spf.mailjet.com include:spf.protection.outlook.com -all`）、NS（`dns1/dns2.namebay.com`）のみ** → **メール専用ドメイン** |
| 🏛 **公的登録簿による裏取り** | **Agence Bio のレコードは `email: contact@bachelet-monnot.com` を持ちながら `siteWebs: []`。**<br>→ **ドメイン所有と「サイトが無い」ことが、公的登録簿側からも整合する** |
| **偽公式サイトの有無** | 🔴 **今回は 1 件も出現しなかった。**「公式サイトを騙るページ」は存在せず、検索に出るのはすべて小売・輸入元・評論であり、いずれも自らを domaine 公式とは名乗っていない。<br>→ **したがって `NOT_THE_PRODUCER_*.html` の保存対象は無し。** |

### 🏛 使用した一次資料（公的登録簿・認証機関・appellation 公式資料のみ）

| 資料 | 取得した情報 | 真正性の担保 |
|---|---|---|
| 🔴 **`recherche-entreprises.api.gouv.fr`（フランス政府公式の企業検索 API。SIRENE / RNE 由来）** | **SIREN 481461374 / SIRET 48146137400011、商号、法人形態 6598、NAF 01.21Z、住所、設立日、活動開始日、gérant 2 名（氏名・生年月）**<br>同住所の SAS 533569992、GFV 479996233、Dezize 村の他 Bachelet 法人 11 件、Gevrey の Denis Bachelet 2 件 | **`api.gouv.fr` ＝ フランス政府 API プラットフォーム。INSEE の SIRENE と RNE を出典とする一次データ** |
| 🔴 **`opendata.agencebio.org/api/gouv/operateurs/`（Agence Bio 公開 API）** | **事業者番号 55726、SIRET 一致、Ecocert France（FR-BIO-01）、engagement 2023-08-04、状態 `ARRETEE`、`dateArret` 2025-02-25、2024 年参照の `AB` / `C2` 併存、品目、住所、電話、メール、`siteWebs: []`** | **Agence Bio ＝ フランス農業省所管の有機農業開発振興機関。`/api/gouv/` は公的公開エンドポイント** |
| **`certificat.ecocert.com/entreprise/75AEE785-…`** | ⚠️ 🔴 **HTTP 404。「La page que vous recherchez n'existe pas」** ―― `ARRETEE` 状態と整合 | Ecocert = 認証機関本体 |
| 🔴 **`api.insee.fr/metadonnees/V1/codes/cj/n3/…` および `/nafr2/sousClasse/…`（INSEE 公式ノメンクラチュア API）** | **`6598` = "Exploitation agricole à responsabilité limitée"**<br>**`5710` = "SAS, société par actions simplifiée"**<br>**`01.21Z` = "Culture de la vigne"**<br>**`46.34Z` = "Commerce de gros (commerce interentreprises) de boissons"** | **INSEE 公式。コード解釈を記憶に頼らず照合した** |
| 🔴 **INAO `extranet.inao.gouv.fr/fichier/pnocdcpuligny-montrachet.pdf`**（450 KB、真正の PDF） | **Puligny-Montrachet 仕様書 v2.2（2010-09-15）。1er Cru 17 climat の全表（`Les Folatières` の 4 lieudit、`Les Referts`、`Les Perrières dit Les Referts`）、aire géographique、🔴 aire de proximité immédiate に `Dezize-lès-Maranges`、encépagement、収量、補糖上限、木片禁止、連続式圧搾機禁止、分析規格** | ⚠️ 🔴 **ファイル名は `PNOCDC-Puligny-Montrachet.pdf` ではなく全小文字ハイフン無しの `pnocdcpuligny-montrachet.pdf`。**大文字・ハイフン入りの 6 変種はすべて HTTP 200 で HTML の「Fichier non trouvé」を返した。**`file` コマンドで PDF であることを検証済み** |
| 🔴 **INAO `extranet.inao.gouv.fr/fichier/PNOCDC-Maranges.pdf`**（435 KB、真正の PDF） | **Maranges 仕様書 v2.2（2010-09-16）。生産 3 村、1er Cru 7 climat の全表（Dezize の `La Fussière` / `Le Croix Moines`、地籍 C 119 の `Clos de la Fussière` 特例）** | **`file` コマンドで PDF であることを検証済み** |
| 🏛 **BIVB `vins-bourgogne.fr/…/57565.pdf`（Puligny-Montrachet 公式アペラシオン資料）** | **「Côte de Beaune の村名アペラシオン、Côte-d'Or 県」「1937 年制定」「1er Cru 17 climat」「Grand Cru 5」、テロワール記述、白 95.92 ha / 1er Cru 90.97 ha、公式テイスティング記述、ソムリエ助言、供出温度** | **BIVB ＝ ブルゴーニュワイン生産者・商社の公式業際組織** |
| 🏛 **BIVB `vins-bourgogne.fr/…/77706.pdf`（Maranges 公式アペラシオン資料、fiche n°46）** | **「Côte de Beaune の村名アペラシオン、Saône-et-Loire 県」「Côte de Beaune の不可分の一部」、3 村、1er Cru 7 climat の村別内訳、テロワール、標高 240〜400 m、1988 年収穫から AOC、面積・平均収穫量** | 同上 |
| 🏛 **BIVB プレスリリース `…/79194.pdf`（Saint-Vincent Tournante 2026 / 2025-01-25）** | **「Côte de Beaune のマランジュ」がホストであること。**⚠️ **Bachelet の語は 1 件も出現しない** | 同上 |

### ⚠️ 🔴 棄却した資料（**事実の根拠として一切使用していない**）

**検索で出現した以下はすべて小売・輸入元・評論・集約サイトであり、公式ソース原則により事実の根拠から除外した。**
**wine-searcher / Vivino / Vinous / Inside Burgundy / Skurnik Wines / Grand Cru Selections /
Crush Wine / wine.com / Hedonism / Bibendum / Great Domaines / Galiena / Caves Carrière /
crus.fr / La Passion du Vin / vignes.info / pagesjaunes / le-site-de.com / societe.com / Wikipedia。**

🔴 **とくに次の 2 点を明記する。**
- **輸入元のページには樹齢・樽容量・熟成月数といった具体的な数字が書かれている。
  しかし本調査は、それらが domaine による執筆であることを立証できなかった
  （レターヘッド無し、署名無し、domaine 名義の PDF 無し、domaine サイトからのリンク無し ――
  そもそも domaine サイトが存在しない）。したがって「domaine 執筆の輸入元テクニカルシート」の
  例外規定は適用できず、全面的に不採用とした。**
- **`societe.com` は SIRENE の再配布サイトである。同じ情報を政府の一次 API から直接取り直したため、
  本ドシエは `societe.com` を出典としていない。**

### 🔍 canonical / OBP（THÉSEUS DB。**読み取りのみ・無変更**）

| 対象 | 実測 |
|---|---|
| **canonical レコード** | **`Domaine Bachelet-Monnot` = 5 件**（`…-puligny-2022` / `-puligny-2023` / `-referts-2022` / `-folatieres-2022` / `-folatieres-2023`）。**`Domaine Denis Bachelet` = 2 件。**他に Bachelet を含む生産者名は無し |
| **OBP intake** | **`research/out/t-01/inventory.json` 5 行**（`source_line_no` 483–487、`section_start_page` 12、セクション `FRANCE \| WHITE > BURGUNDY`、`producer_heading` = `Bachelet-Monnot`、`flags` はすべて空） |
| 🔴 **mapping 実測** | **`research/out/t-01/mapping.json`** ―― **483 / 484 は `resolved_to: "research_shell"`（`rs:pro:3b2de71b94633613`、`canonical.producer` のみ確定）**、**485 / 486 / 487 は `resolved_to: "canonical_release"`（producer + cuvee + vintage）** |
| **shell 状態** | **`research/store/t-01/shells.json`** ―― 当該 shell は `status: "research_pending"` / `published: false` / `excluded_from_recommendations: true` / `identity_basis: "source_exact"` |
| **review キュー** | **`research/out/t-01/review.json`** に本生産者の行は 1 件も無い。**ただし他 3 生産者の fuzzy 候補として本生産者の cuvée が浮上している**（→ CC-1） |

**キャッシュ先**: `/Users/akiomatsumoto/Theseus_Phase0/research/producers/_sources/domaine-bachelet-monnot/`
（`sirene_*.json`、`agencebio_*.json`、`cj_*.json`、`naf_*.json`、`CDC-Puligny-Montrachet.pdf` +
`puligny.txt`、`PNOCDC-Maranges.pdf` + `maranges.txt`、`BIVB-Puligny-Montrachet.pdf`、
`BIVB-Maranges.pdf`、`BIVB-SVT2026-Maranges.pdf`、`ecocert_cert.html`、DNS 探索の probe ファイル。gitignore 対象）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | **SIREN / SIRET / 法人形態 / NAF / 住所 / gérant 2 名の氏名と生年月まで、政府 API の一次データで確定。コード解釈も INSEE ノメンクラチュア API で照合済み。**⚠️ 事業所商号 `JEAN-FRANCOIS BACHELET` の意味だけ未解決 |
| **Overview** | **Medium** | **所在と法人構造は確定。**🔴 **ただし「造り手自身の言葉」がゼロである。**この造り手が何を目指しているかは一切書けていない |
| **History** | 🔴 **Low** | **登記日付 7 点のみ。**創業の経緯・世代・畑の取得史はすべて空白。**公式サイトが無いため、埋める手段が現時点で無い** |
| **Location** | 🔴 **High** | **蔵の所在が 2 つの独立した公的登録簿で一致。**🔴 **さらに INAO 仕様書で「Dezize が Puligny の近接区域に含まれる」という法的接続まで取れた。**appellation 側のテロワール・面積・climat 一覧も公式 |
| **Farming** | **Medium** | 🔴 **公的登録簿からの実データがある**（Ecocert・engagement 日・AB/C2 併存・`ARRETEE` と `dateArret`）。**これは本ドシエ最大の収穫の一つ。**⚠️ **ただし `ARRETEE` の理由が判別できず、「認証状態」として結論が出せていない。栽培の実務（密度・仕立て・樹齢・被覆作物）は完全にゼロ** |
| **Winemaking** | 🔴 **None** | **一次資料ゼロ。**樽・熟成・酵母・分析値のいずれも不明。appellation 規定（木片禁止・連続式圧搾機禁止・補糖上限）しか書けていない |
| **Style** | 🔴 **None（domaine レベル）** | **造り手のテイスティングノートは 1 件も無い。**BIVB のアペラシオン一般記述のみ。**フロアでの前置きを必須にした** |
| **Important Cuvées** | 🔴 **High** | 🔴 **OBP 5 本すべてについて、appellation 側の実在を INAO 仕様書で確認**（AOC Puligny-Montrachet、1er Cru climat `Les Folatières` と `Les Referts`）。**さらに `Les Folatières` が 4 lieudit の束であること、`Les Referts` が仕様書上 2 か所に現れることまで取れた。**⚠️ **どの区画を所有しているかは不明** |
| **Staff Notes** | 🔴 **High** | ⚠️ **12 項目。**🔴 **面積・創業ストーリー・「ビオです」・醸造数値・シャルドネ 100%・第三者点数・Denis Bachelet 混同・村内の同姓ドメーヌ ―― 8 つの実在する事故経路を塞いだ** |
| **Canonical Conflict** | **High** | **3 件とも canonical を直接パースして機械確認済み** |
| 🔴 **総合** | **Medium — staff-usable。70% を超える。** | 🔴 **フロアは「誰が・どこで・どのアペラシオンの・どの climat を」を、一つも嘘を言わずに語れる。**<br>**欠けているのは造り手の声（沿革・栽培哲学・醸造・テイスティング）で、これは全部同じ一つの理由 ―― 公式サイトが存在しない ―― から来ている。**<br>**したがって、この生産者は「調べ方を変えない限り、これ以上は埋まらない」タイプである。**→ Open Questions 2 |

**reached_70: YES.**

🔴 **ただし条件付きである。** 必須 7 項目のうち **Identity / Overview / Location / Farming /
Important Cuvées（OBP 連結あり）/ Staff Notes 芯 3 / ⚠️ 言ってはいけないことリスト** はすべて満たしている。
**満たしていないのは繰延べ可の項目（沿革の細部・醸造の数値・第三者評価）だけである。**
**そして本ドシエは薄い分、⚠️ リストを 12 項目まで厚くした。**

---

## Open Questions

1. 🔴 **村名ピュリニー 2 本（2023 $380 / 2022 $320）が canonical release に到達していない。**
   🔍 **`mapping.json` 実測では `resolved_to: "research_shell"`。生産者は確定しているが、
   村名キュヴェの canonical レコード（`bachelet-monnot-puligny-2022` / `-2023`）と intake が結線していない。**
   ⚠️ 🔴 **依頼時の申し送り「5 本すべて `match_state = exact`」とは食い違う。**
   **canonical レコード自体は 5 件存在するので、結線の問題である可能性が高い。**
   → **intake 側の cuvée 解決ロジックの確認が要る。canonical への書き込みは本書では行っていない。**
2. 🔴 **公式サイトが無い以上、造り手の声を得る経路は 3 つしか残っていない。**
   **(a) `contact@bachelet-monnot.com` に直接 fiche technique を請求する**（⚠️ **送信は Akio の判断事項。本書では行っていない**）
   **(b) 輸入元（canonical の tag は `Grand Cru Selections`）から、domaine 名義・レターヘッド付きの
   テクニカルシートを取り寄せる**ーー **domaine 執筆であることが立証できれば一次資料として使える**
   **(c) 蔵出しラベルの実物を撮影して、記載事項（アルコール度数、mis en bouteille 表記、認証ロゴの有無）を読む**
   → 🔴 **(c) は現地在庫があれば今日にでもできる。認証ロゴの有無は §Farming の `ARRETEE` 問題に直接効く。**
3. 🔴 **有機認証の `ARRETEE`（2025-02-25）は何なのか。**
   **認証機関の乗り換えか、認証の取りやめか、経営体の再編に伴う登録の付け替えか。**
   **Agence Bio 側には証明書が 1 件しか無く、他機関のレコードは存在しない。**
   → **Agence Bio または Ecocert への直接照会が要る。**
   ⚠️ **それまでは「ビオです」と言わない。**
4. **`Les Referts` はどちらの climat か。**
   🏛 **INAO 仕様書には climat `Les Referts` と、climat `Les Perrières` の lieudit
   「Les Perrières dit Les Referts」の 2 つが存在する。**
   → **ラベル実物での確認が要る。**
5. **`Les Folatières` の 4 lieudit（Es Folatières / En la Richarde / Peux Bois / Au Chaniot）のうち、
   どこを所有しているか。** **公的資料には出ない。造り手か輸入元にしか答えられない。**
6. 🔴 **同住所の SAS `BACHELET - MONNOT`（SIREN 533569992、NAF 46.34Z＝飲料卸売、2011 年設立）の役割。**
   **EARL（畑）と SAS（飲料卸売）が同じ住所で並立している。**
   ❓ **販売会社なのか、それ以上のものなのかは登記から読み取れない。**
   ⚠️ **フロアで「ネゴシアン部門」と説明してはならない。**
7. **事業所の `nom_commercial` が `JEAN-FRANCOIS BACHELET` である理由。**
   ❓ **EARL の設立（2005）と活動開始（2008）が 3 年ずれていることと関係する可能性があるが、登記は説明していない。**
8. **屋号の「Monnot」の由来。** **公的資料に一切現れない。**
9. 🔴 **canonical の村名 2 件に入っている `points` と「89〜91点（ヴィナス）」の扱い。**
   **これは本生産者ローカルの問題ではなく、canonical 全体で第三者点数をどう扱うかの方針判断である。**
   → §Canonical Conflict CC-3。**Akio / CTO 判断。**
10. **`Premier Cru` と `1er Cru` の表記ゆれ（CC-2）が canonical 全体で何件あるか未計測。**
    **本生産者だけで 1 件見つかったが、横断調査は行っていない。**
11. **INAO 仕様書が 2010 年の全国異議申立手続版（v2.2）である。**
    ⚠️ **より新しい統合版が官報（`info.agriculture.gouv.fr/boagri/`）側にある可能性がある。**
    **本ドシエの数値（とくに村名の収量）は、削除線と太字が本文抽出で区別できないため断定を避けた。**
