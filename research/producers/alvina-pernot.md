# Alvina Pernot

> **Research Layer / status: `research_in_progress` / published: false / canonical 昇格判断は未実施**
> 🔍 **canonical にこの生産者のレコードは 4 件存在する**（`producer` フィールド一致 4 件 / prose のみの一致 **0 件**）。
> **本書は研究記録であり、canonical を一行も変更していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者の公式サイトで確認**（一次資料）── 🔴 **本ドシエでは 1 件も使えていない。理由は下記 ①。**
> `📄` 生産者執筆だが自社ドメイン外（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `🏛` **公的登録簿・認証機関・appellation 公式資料**（SIRENE/RNE、Agence Bio、INSEE、INAO、BIVB）
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05
>
> ---
>
> 🔴 **本ドシエ最大の事実 ①ーー 公式サイトは「無い」のではなく「所有されているのに立っていない」。**
> **`alvinapernot.com` は実在する。**🏛 **WHOIS は登録日 `2018-11-03`、登録者国 `FR`、レジストラ Register S.p.A.（Amen）、
> NS は `NS1/NS2.AMENWORLD.COM`。A レコード `185.2.5.9` があり、MX（`mail-fr.securemail.pro`）も設定されている。**
> 🔴 **しかし `https://alvinapernot.com/` が返すのは `content-length: 9` ―― 中身は `<!-- -->` の 9 バイトだけである。**
> **`last-modified` は `2018-05-23`（＝ドメイン登録より前。ホスティング業者の既定の空 index）。**
> **`www` も同一。`/robots.txt` `/sitemap.xml` `/en/` `/accueil` などはすべて 404。**
> 🔴 **Wayback の唯一の記録（`2021-11-26`）を取り直したが、バイト単位で同一の 9 バイトだった。**
> **候補 8 ドメイン（`alvina-pernot.*`, `domaine-alvina-pernot.com`, `alvinapernot.fr/.net/.eu/.wine`, `apwines.fr` ほか）はすべて A レコード無し。**
> → **「まだ何も公表していない生産者」である。したがって本ドシエは `✅` レイヤーを一切持たない。**
> **代わりに `🏛`（公的登録簿・INAO・BIVB）だけで組み立てた。** → §Sources
>
> 🔴 **本ドシエ最大の事実 ②ーー 登記上の実体は「ドメーヌ」ではなく「卸売業」である。**
> 🏛 **`AP WINES SAS`（SIREN **843307471**）、本店 `4 RUE DE BOIS, 21190 PULIGNY-MONTRACHET`、
> Président de SAS = **PERNOT, Alvina（1988 年 6 月生）**。**
> 🔴 **NAF は `46.90Z` = 「Commerce de gros (commerce interentreprises) non spécialisé」（非特化の企業間卸売）。
> ブドウ栽培の `01.21Z` ではない。**（INSEE 公式ノメンクラチュア API で照合）
> → **登記だけからは「自社畑を耕す農業経営体」であるとは言えない。** → §Farming / §Staff Notes ⚠️ ②
>
> 🔴 **本ドシエ最大の事実 ③ーー canonical の 4 レコードは、すべて「空殻」である。**
> **依頼は `grapes` / `aging` / `founded_year` / `subregion` / `classification` / `description` / `obp_note` の
> 検証を求めているが、🔍 **4 件のいずれにも `grapes` も `aging` も `founded_year` も `description` も
> `obp_note` も `tasting` も `winemaking` も存在しない。** フィールドが空なのではなく、キーが無い。**
> 🔴 **「11 生産者連続で格納値が公式と矛盾」という base rate に対する、初めての例外である。
> ただしそれは正しいからではなく、照合すべき値が 1 つも無いからである。** → §Canonical Conflict
>
> 🔴 **本ドシエ最大の事実 ④ーー `La Pièce sous le Bois` は INAO で完全に決着した。**
> 🏛 **AOC `Blagny` の仕様書は「L'appellation d'origine contrôlée « Blagny » est réservée aux vins tranquilles rouges」
> ―― Blagny は赤専用である。**
> 🏛 **AOC `Meursault` の仕様書は逆に「Blagny の生産区域に含まれる区画から得られたワインについては、
> Meursault は白のみに限られる」と定める。**
> → 🔴 **したがって `La Pièce sous le Bois` の白は、法的に `Meursault Premier Cru` 以外にはなりえない。
> 「Blagny 1er Cru の白」は制度上存在しない。**
> 🔴 **canonical の `classification = "Meursault 1er Cru"` / `subregion = "Meursault Premier Cru"` は
> INAO によって裏づけられている。本バッチで唯一の「canonical が正しい」確認例である。** → §Important Cuvées
>
> 🔴 **本ドシエ最大の事実 ⑤ーー この 4 行に関しては、メニューが正しく canonical が間違っている。**
> **OBP 印字は `'La Pièce sous le Bois,'`（`sous` は小文字）。**🏛 **INAO 仕様書も BIVB 公式フィッシュも `La Pièce sous le Bois`。**
> 🔍 **canonical だけが `"La Pièce Sous le Bois"`（`Sous` が大文字）である。**
> → 🔴 **「メニューが欠陥側とは限らない」の 4 件目の反例。** → §Canonical Conflict

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Alvina Pernot**（`producer_heading`。🔍 intake 4 行すべて同一見出し。`source_line_no` 470–473） |
| **canonical 表記** | 🔍 **Alvina Pernot**（4 レコードすべて。`Domaine` は付かない） |
| 🔴 **登記上の商号** | 🏛 **`AP WINES SAS`**（SIREN **843307471** / 本店 SIRET `84330747100022`） |
| 🔴 **法人形態** | 🏛 **SAS**。INSEE カテゴリ juridique **`5710` = 「SAS, société par actions simplifiée」** |
| 🔴 **主活動（NAF）** | 🏛 🔴 **`46.90Z` = 「Commerce de gros (commerce interentreprises) non spécialisé」**（INSEE 公式ノメンクラチュア API で照合）<br>⚠️ **ブドウ栽培 `01.21Z` **ではない**。この一点が本ドシエの解釈をほぼ全部支配している** |
| 🔴 **所在** | 🏛 **`4 RUE DE BOIS, 21190 PULIGNY-MONTRACHET`（Côte-d'Or 県 / commune INSEE `21512`）**。緯度経度 `46.946347, 4.756253` |
| 🔴 **経営者** | 🏛 **PERNOT, Alvina（1988 年 6 月生）ーー Président de SAS**（RNE 最終更新 2024-05-19）<br>🔴 **登記上の役員は彼女 1 名のみである** |
| **法人設立** | 🏛 **2018-10-05** |
| 🔴 **本店事業所** | 🏛 **SIRET `…0022` は `date_creation` `2021-09-10`。**⚠️ **法人は 2 事業所を持ち、開いているのは 1 つだけ ―― つまり 2018〜2021 の初期事業所は閉鎖されている。**❓ **旧事業所の所在は本調査では取得できなかった** |
| **従業員規模** | 🏛 **`tranche_effectif_salarie: 01`（＝1〜2 名、2023 年）**。カテゴリ `PME` |
| **労働協約** | 🏛 **IDCC `0493`**（飲料・酒類の卸売業の協約）⚠️ **NAF 46.90Z と整合的であり、農業の協約ではない** |
| 🔴 **有機認証** | 🏛 🔴 **無し（証明済みの不在）。** Agence Bio を **SIRET `84330747100022` 完全一致**および **SIREN `843307471`** で照会 → **両方 `nbTotal: 0`。**<br>🏛 **政府企業登記の `complements.est_bio` も `false`。** → §Farming |
| **関連法人 ①** | 🏛 **`SC NOYERS BRETS`（SIREN **914446372**）ーー 2022-06-07 設立、`24 RUE DE POISEUL, 21190 PULIGNY-MONTRACHET`、NAF `68.20B`（不動産賃貸＝土地保有型）。**<br>**`ABADIE (PERNOT), Alvina` = Associé indéfiniment responsable、`PERNOT, Michel Henri`（1959 年 5 月生）= Gérant** |
| **関連法人 ②** | 🏛 **`AP&CO`（SIREN 984511980）ーー 2024-01-22 設立、`21 QUAI LA PLATIÈRE, 71150 FONTAINES`、NAF `68.20B`。**<br>**`ABADIE, Philippe`（1983 年 12 月生）と `ABADIE (PERNOT), Alvina` の 2 名** |
| ⚠️ **婚姻名** | 🏛 **公的登記は 2 社で `ABADIE (PERNOT), Alvina` と記載する。**`AP WINES SAS` の登記だけは `PERNOT, Alvina`。**同一人物（生年月 1988-06 が一致）** |
| **公式サイト** | 🔴 **実質的に無し。**`alvinapernot.com` は所有されているが 9 バイトの空プレースホルダのみ。→ §Sources |
| 🔴 **canonical id（生産者）** | 🔍 **`producer:alvina-pernot`**（intake / mapping 双方が導出。canonical に生産者マスタのファイルは無い） |

---

## Overview

🏛 **Puligny-Montrachet の村内（`4 rue de Bois`）に本店を置く SAS。登記上の役員は Alvina Pernot 1 名。
法人設立は 2018-10-05、現在の事業所は 2021-09-10 開設。従業員規模は 1〜2 名である。**

🔴 ⚠️ **この造り手について「造り手自身が語った言葉」を、本調査は一行も入手できていない。**
**ドメインは持っているが web サイトを公表しておらず、生産者名義の fiche technique も発見できなかった。**
**したがって本ドシエには、テイスティングノートも、栽培哲学も、醸造工程も、畑の面積も無い。**
**あるのは、公的登録簿が記録している「誰が・どこで・どういう法人形態で・どの NAF コードで・どういう認証状態か」と、
INAO / BIVB が記録している「その畑名が制度上どう扱われるか」だけである。**

🔴 **そして本ドシエの中心は、次の 1 行に集約される ――**
🏛 **登記上、この法人の主活動は「非特化の企業間卸売（`46.90Z`）」であって「ブドウ栽培（`01.21Z`）」ではない。**
**同じ Puligny-Montrachet 村の他の造り手 ―― `DOMAINE PERNOT PAUL ET SES FILS`（SIREN 315015487）、
`DOMAINE PERNOT BELICARD`（383186772）、`JEAN-MARC PERNOT`（350822342）、
`CAROLE PERNOT`（984594705）、`DOMAINE JEAN-LOUIS CHAVY`（443712880）―― は
いずれも `01.21Z` である。**
→ 🔴 **つまり「村の他のドメーヌと同じ登記の形をしていない」ことが、登記の側からはっきり見える。**
⚠️ **ただしこれは「畑を持っていない」ことの証明ではない。**
**フランスでは畑を別法人（SC / GFA など）に置き、醸造・販売を商業法人で行う構成が普通にあり、
実際この造り手も `SC NOYERS BRETS`（NAF 68.20B ＝ 土地保有型）に名を連ねている。**
**登記は「どう組んでいるか」を語るが、「何を耕しているか」は語らない。** → §Farming / §Staff Notes ⚠️ ②

🔍 **THÉSEUS における状態は、Batch 1–11 を通じて最も良い。**
🔴 **OBP 掲載 4 本すべてが `match_state = exact` かつ `resolved_to = canonical_release` であり、
しかも intake（`obp_intake_normalized_20260804.json`）と mapping（`research/out/t-01/mapping.json`）が
初めて完全に一致した。**
→ **既知の「intake と mapping が食い違う」問題（4 例確認済み）は、本生産者では発生していない。**
🔴 **だから本ドシエの価値はマッチングではない。**
**4 件とも中身が完全に空であること、そして最も高い 2 本（$720 × 2）が語る材料をまったく持たないことを、
はっきりさせる点にある。** → §Canonical Conflict

---

## History

🔴 ⚠️ **本調査は、この造り手の沿革をほとんど取得できなかった。**
**公式サイトが公表されていないため、創業の経緯・修業歴・畑の取得履歴は一切不明である。**

🏛 **公的登録簿から機械的に確定できるのは、以下の日付だけである。**

| 年月日 | 出来事（🏛 登記・WHOIS 上の記録） |
|---|---|
| **2018-10-05** | 🔴 **`AP WINES SAS`（SIREN 843307471）が登記される。NAF `46.90Z`** |
| **2018-11-03** | **`alvinapernot.com` が登録される**（🏛 WHOIS。登録者国 FR、Register S.p.A.）<br>→ **法人設立の約 1 か月後。ドメイン取得は創業と同時期である** |
| **2021-09-10** | 🔴 **現在の本店事業所（SIRET `…0022`、`4 rue de Bois`）が開設される。**⚠️ **同時に旧事業所が閉鎖されている（`nombre_etablissements: 2` / `ouverts: 1`）** |
| **2021-11-26** | **Wayback の唯一のキャプチャ。内容は 9 バイトの空プレースホルダ** |
| **2022-06-07** | **`SC NOYERS BRETS`（SIREN 914446372、NAF 68.20B）が Puligny に設立される。Alvina と `PERNOT, Michel Henri` の 2 名** |
| **2024-01-22** | **`AP&CO`（SIREN 984511980、NAF 68.20B）が Fontaines（71）に設立される。Alvina と `ABADIE, Philippe` の 2 名** |
| **2024-05-19** | **RNE 最終更新** |

⚠️ 🔴 **「Paul Pernot の孫娘である」とは、本ドシエでは言わない。**
**この主張は複数の小売・輸入元・評論ページに現れるが、本調査は一次資料でこれを確認していない。**
🏛 **公的登記が語るのは次の 2 点だけである ――**
**(a) `SC NOYERS BRETS` において `PERNOT, Michel Henri`（1959 年生）が Gérant、Alvina が無限責任社員であること。**
**(b) 同じ Puligny 村に `DOMAINE PERNOT PAUL ET SES FILS`（SIREN 315015487、1979 年設立、NAF 01.21Z、
`7 place du Monument`）が別法人として存在すること。**
🔴 **登記はこの 2 つを結ぶ記述を持たない。血縁を述べた一次資料は存在しない。** → §Staff Notes ⚠️ ③

⚠️ 🔴 **ただし、キュヴェ名そのものが 1 つだけ手がかりを与えている。**
**OBP 行 1 の印字は `'Les Vignes de Mon Père,'`（＝「わが父の畑」）である。**
→ **「父の畑から造られたキュヴェである」ことは、造り手自身がラベルに書いた一人称の名乗りとして読める。**
**しかし「その父が誰か」は、ラベルもどの一次資料も特定していない。** → §Important Cuvées 行 1

---

## Location

| | |
|---|---|
| **Country** | France 🏛 |
| **Region** | **Bourgogne / Côte de Beaune** 🏛 |
| 🔴 **本店の所在** | 🏛 **`4 Rue de Bois, 21190 Puligny-Montrachet`（Côte-d'Or 県 / INSEE commune `21512`）** |
| 🔴 **蔵が属する村** | 🏛 **Puligny-Montrachet 村内である**（Bachelet-Monnot のような「村外の蔵」ではない） |
| **OBP 掲載ワインの appellation** | 🏛 **Puligny-Montrachet（村名 1 / 1er Cru 2）＋ Meursault Premier Cru（1）** |
| 🔴 **Meursault を Puligny の蔵で仕込めるか** | 🏛 **可能。**Meursault 仕様書 IV 章 3°「aire de proximité immédiate」（vinification / élaboration / élevage について例外的に認められる区域）の Côte-d'Or 県リストに **`Puligny-Montrachet` が明記されている**<br>（逆に Puligny 仕様書の同リストにも `Meursault` が入っており、双方向に成立する） |
| ⚠️ **自社畑の面積・区画** | 🔴 **公的資料に一切存在しない。本ドシエでは面積を一切主張しない。** → §Staff Notes ⚠️ ① |

### 🏛 Puligny-Montrachet（BIVB 公式アペラシオン資料 fiche n°62）

- **「Côte de Beaune の村名アペラシオン、Côte-d'Or 県。」AOC 制定は **1937 年**。**
- **1er Cru に格付けされた Climat は **17**。同じ commune が **Grand Cru を 5 つ**産する。**
- 🏛 **テロワール** ――「**畑はしばしば褐色石灰質土壌、あるいは泥灰質の粘土‐石灰質の層が交互に現れる石灰岩を占め、
  時に深く、時に硬い岩の直上にある。粘土質シルトは上部で厚く、斜面の下部では細粒になる。
  東向きおよび南東向きの露出、標高 230〜320 m。**」
- 🏛 **生産規模（2018 年時点）**: 白 **95.92 ha**（うち 1er Cru **90.97 ha**）／赤 **0.36 ha**
  → 🔴 **1er Cru の面積が村名を上回るという、極めて特異な構成である。**
- 🏛 **17 climat の公式リスト**（BIVB / INAO 一致）:
  `Sous le Puits` / **`La Garenne`** / `Hameau de Blagny` / `La Truffière` / `Champ Gain` / `Les Chalumaux` /
  `Champ Canet` / **`Clos de la Garenne`** / **`Les Folatières`** / `Le Cailleret` / `Les Demoiselles` /
  `Les Pucelles` / `Clavaillon` / `Les Perrières` / `Clos de la Mouchère` / `Les Combettes` / `Les Referts`
  → 🔴 **OBP の 2 つの Puligny 1er Cru 名は、いずれも公式リストに実在する。**
  → 🔴 ⚠️ **同時に `La Garenne` と `Clos de la Garenne` は**別個の climat**である。混同禁止。** → §Staff Notes ⚠️ ⑤

### 🏛 Meursault（BIVB 公式アペラシオン資料 fiche n°49）

- **「Côte de Beaune の村名アペラシオン、Côte-d'Or 県。」AOC 制定は **1937 年**。1er Cru は **19 climat**。**
- 🏛 **テロワール** ――「**最良の土地は標高 260 m 前後、東から南へ振れる露出。バトニアン階（ジュラ紀）が
  Côte と出会う。時にマグネシウム質石灰岩のニュアンスが現れる。畑は石灰質マルヌの上でその卓越に達する。
  カロヴィアン階の古い石灰岩とアルゴヴィアン階のマルヌ質岩が crus を分け合う。**」
- 🏛 **生産規模（2018 年時点）**: 白 **381.04 ha**（うち 1er Cru 107.37 ha）／赤 **10.66 ha**
- 🔴 🏛 **BIVB の 1er Cru 一覧は `La Pièce sous le Bois` を「`La Pièce sous le Bois` **ou Blagny**」と表記する。**
  **同リストには `La Jeunellotte ou Blagny` / `Sous le Dos d'Ane ou Blagny` / `Sous Blagny ou Blagny` /
  `Les Ravelles ou Blagny` があり、さらに `Blagny` 単独も 1 つの climat として並ぶ。**
  → **§Important Cuvées 行 2 で全面的に扱う。**

---

## Farming

🔴 🏛 **本節の結論は「有機認証は無い」であり、それは推測ではなく証明された不在である。**

| 照会 | 結果 |
|---|---|
| 🏛 **Agence Bio ―― SIRET 完全一致 `84330747100022`** | 🔴 **`nbTotal: 0`** |
| 🏛 **Agence Bio ―― SIREN `843307471`** | 🔴 **`nbTotal: 0`** |
| 🏛 **政府企業登記 `complements.est_bio`** | 🔴 **`false`** |
| 🏛 **関連法人の照会**（`SC NOYERS BRETS` 914446372、`MICHEL PERNOT` 398158139、`DOMAINE PERNOT PAUL ET SES FILS` 315015487、`DOMAINE PERNOT BELICARD` 383186772） | **すべて `nbTotal: 0`** |
| ⚠️ **参考（証明力なし）**: Agence Bio 名称検索 `nom=pernot&departement=21` | **`nbTotal: 6` だが、6 件はいずれも Doubs / Haute-Marne / Saône-et-Loire / Vosges / Rhône / Dordogne の別事業者であり、Puligny の該当者は 1 件も無い**<br>🔴 **名称検索は証明にならない。証明は上の完全一致 2 本である** |

### 🔴 この照会から言えること・言えないこと

**言えること（🏛 一次資料）**
1. 🔴 **`AP WINES SAS` は、フランスの有機農業公的登録簿（Agence Bio）に**登録されていない**。
   SIRET 完全一致・SIREN 一致の両方が `nbTotal: 0` を返し、政府登記の `est_bio` も `false` である。
   これは「見つからなかった」ではなく、**完全に解決した照会が返した否定**である。**
2. **したがって `datePremierEngagement` も認証機関も `mixité` も存在しない。転換中ですらない。**
3. 🔴 **OBP の 2022 / 2023 ヴィンテージが「転換に先行するか」という問いは成立しない。転換そのものが登録されていないからである。**

**言えないこと（⚠️ 出典が沈黙している）**
- ⚠️ 🔴 **「有機的な栽培を実践していない」とは言えない。**
  **実践（practice）と認証（certification）は別の主張である。認証が無いことは、農法についての主張を一切含まない。**
  **この造り手が自分の農法をどう説明しているかは、公表されていないので不明である。**
- ⚠️ **HVE / Demeter / Biodyvin / Terra Vitis への言及は、本調査が参照したどの公的資料にも一切現れなかった。**
- ⚠️ 🔴 **そもそも「この法人が畑を耕しているか」が登記からは確定しない。**
  🏛 **NAF は `46.90Z`（非特化卸売）であり、労働協約も IDCC `0493`（飲料卸売）である。**
  **一方で Alvina は `SC NOYERS BRETS`（NAF `68.20B` ＝ 土地保有型）に無限責任社員として名を連ねており、
  ブドウ畑を別法人に置く一般的な構成と整合する。**
  ❓ **どちらとも登記は断定していない。** → §Staff Notes ⚠️ ②
- ⚠️ **栽培密度・仕立て・樹齢・被覆作物・収量の実績値は、公的資料には無い。**

### 🏛 appellation レベルの栽培・醸造規定（**domaine 固有ではない。混同禁止**）

🔴 **以下は INAO の Puligny-Montrachet / Meursault 仕様書の条文であり、すべての生産者に等しくかかる規定である。
「Alvina Pernot はこうしている」という意味では断じてない。**

| 項目 | Puligny-Montrachet | Meursault |
|---|---|---|
| **白の品種** | **`chardonnay B` および `pinot blanc B`** 🔴 **（＝仕様書上は 100% Chardonnay とは限らない）** | **同左** |
| **灌漑** | 🏛 **禁止**（`L'irrigation est interdite`） | **同左** |
| **基準収量（白）** | ⚠️ 🔴 **抽出テキストが `45 57` と二重に出る。**2010 年の全国異議申立手続版では削除線と太字が本文抽出で区別できない。**本ドシエでは数字を断定しない** | ⚠️ **同一の `45 57` 問題** |
| **補糖後の上限アルコール** | 🏛 **村名 13.5%**（climat 名または premier cru を付す場合は別途規定） | **同左** |
| 🔴 **木片の使用** | 🏛 🔴 **「L'utilisation de morceaux de bois est interdite」ーー オーク・チップの使用は禁止** | **同左** |
| **色の制限** | 🏛 **白・赤の両方。ただし Blagny の生産区域に含まれる区画からのものは白のみ** | 🏛 **白・赤の両方。ただし Blagny の生産区域に含まれる区画からのものは白のみ** |

---

## Winemaking

🔴 ⚠️ **本調査は、この造り手の醸造について一件も確定できなかった。**

**公式サイトが公表されておらず、生産者名義の fiche technique も発見できなかった。
発酵容器、樽のサイズ、新樽比率、élevage の月数、バトナージュの有無、澱との接触、
瓶詰め時期、アルコール度数、生産本数 ―― そのいずれについても一次資料が存在しない。**

⚠️ 🔴 **輸入元・小売・評論のページには、樽数・熟成・区画といった具体的な記述が書かれている。
本ドシエはそれを一切採用しない。**
**理由は、それらのページが生産者による執筆であることを立証できなかったからである**
（レターヘッド無し、一人称無し、生産者名義の PDF 無し、生産者サイトからのリンク無し ――
そもそも生産者サイトが公表されていない）。→ §Sources「棄却した資料」

🔴 **なお、Bachelet-Monnot のときと違い、canonical 側にも醸造の数値は入っていない。**
🔍 **4 レコードには `aging` も `winemaking` も `grapes` もキーごと存在しない。**
→ **したがって「canonical が出典不明の醸造数値を持っている」という問題は、本生産者では発生していない。
発生していないのは、正しいからではなく、空だからである。** → §Canonical Conflict

**言えるのは appellation 規定だけである** ―― 🏛 **オーク・チップの使用は Puligny-Montrachet でも Meursault でも
禁止されている。灌漑も禁止されている。**

---

## Style

🔴 ⚠️ **この造り手自身のテイスティングノートは、本調査では 1 件も入手できていない。**
**造り手が自分のワインをどう説明しているかは、完全に不明である。**

🏛 **以下は BIVB のアペラシオン公式資料による「アペラシオンの一般的性格」であり、
Alvina Pernot のワインの描写ではない。フロアで使う際は必ず「ピュリニー（ムルソー）というアペラシオンは」と前置きすること。**

### 🏛 Puligny-Montrachet 白（BIVB 公式 fiche n°62）

「**金糸で縫われたような輝く衣に、緑がかった反射の光輪。この色調は年齢とともに強度を増す。
ブーケはサンザシ、熟した葡萄、アーモンドペースト、ヘーゼルナッツ、琥珀、レモングラス、青りんごを束ねる。
乳性の香り（バター、焼きたてのクロワッサン）と鉱物的な香り（火打石）は常であり、蜂蜜もそうである。
ボディとブーケが繊細な調和へ融け合う ―― 揺るぎない性質と際立った凝縮のもとに、あらゆる優美さが宿る。**」

🏛 **ソムリエ助言** ――「**凝縮と大いなる気品が Puligny-Montrachet とその Premier Cru の生地をなす。
均衡に満ちたこの大きな芳香的複雑さは、洗練された様式と結びついて、繊細でありながら同時に豊かな料理を要求する。
ソースを纏った見事な家禽にも、きのこを添えた仔牛のポワレにも等しく寛ぐ。
フォワグラ、オマール、ラングスト、海の魚のグリルやポワレとは見事に響き合う。
チーズではシェーヴルとルブロション、そしてブリ・ド・モーのような白カビの軟質チーズを求める。**」
🏛 **供出温度 11〜13 °C。**

### 🏛 Meursault 白（BIVB 公式 fiche n°49）

「**Meursault の白は多くの場合、金緑色、カナリアイエローの衣をまとい、年齢に応じてやや強まるか、
磨かれた青銅色に至る。澄んで輝き、しばしば銀色の反射を伴う。
ブーケは熟した房を思わせる。若いうちは、焼いたアーモンドとヘーゼルナッツが、
植物的・花的な環境（サンザシ、ニワトコ、シダ、菩提樹、ヴェルヴェーヌ）と鉱物的な環境（火打石）のなかにある。
バター、蜂蜜、柑橘もまた鼻を誘う。口中では、豊かで脂の乗ったワイン、
軽やかで快活なヘーゼルナッツの風味 ―― 濃密さと爽やかさの均衡が、絹のあらゆる音域を降りてゆく。
長く、構築的で、成熟を必要とする。偉大な熟成型の白である。**」

🏛 **ソムリエ助言** ――「**その芳香的な力と、脂と酸に基づく例外的な均衡が、これをブルゴーニュの大諸侯の一人にしている。
（…）白いソースを纏った見事な仔牛や家禽 ――（…）さらに良いのは、
ガンバ、オマール、ラングストのような、焼いた／ソースを纏った甲殻類である。
ブルーチーズとフォワグラでさえ、一度で受け入れる。**」
🏛 **供出温度 12〜14 °C。**

🔴 **フロア上の実用差 ―― 同じリストに並ぶこの造り手の 4 本のうち、
1 本（$640 の La Pièce sous le Bois）だけが Meursault であり、BIVB の推奨供出温度が 1〜2 度高い。**

⚠️ 🔴 **canonical はこの 4 件すべてに `serving_temp: "10–13°C"` を入れている。**
**Puligny の BIVB 公式値は 11〜13 °C、Meursault は 12〜14 °C であり、いずれとも一致しない。** → §Canonical Conflict

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake / mapping より。**全 4 本**）

| # | OBP 印字（`source_wine_raw`） | VT | 価格 | 🔍 解決状態 | 🏛 appellation 側の裏取り |
|---|---|---|---|---|---|
| 1 | **'Les Vignes de Mon Père,' Puligny-Montrachet** | **2023** | **$360** | ✅🔍 **`exact` / `canonical_release`**<br>`producer:alvina-pernot` / `cuvee:…-les-vignes-de-mon-pere` / `vintage:…-2023` | 🏛 **AOC Puligny-Montrachet（村名）は実在。1937 年制定**<br>⚠️ **キュヴェ名は独自名であり、INAO の climat リストには**当然ながら**存在しない** |
| 2 | **'La Pièce sous le Bois,' Meursault Premier Cru** | **2022** | **$640** | ✅🔍 **`exact` / `canonical_release`**<br>`cuvee:…-la-piece-sous-le-bois` / `vintage:…-2022` | 🔴 🏛 **INAO Meursault 仕様書の 1er Cru 表に `La Pièce sous le Bois` が **色 = Blanc** で実在。**<br>🔴 🏛 **INAO Blagny 仕様書は Blagny を**赤専用**と定める** |
| 3 | **'La Garenne,' Puligny-Montrachet Premier Cru** | **2022** | **$720** | ✅🔍 **`exact` / `canonical_release`**<br>`cuvee:…-la-garenne` / `vintage:…-2022` | 🔴 🏛 **INAO Puligny 仕様書の 1er Cru 表に climat `La Garenne`（lieudit `La Garenne ou Sur la Garenne`、色 = **Blanc のみ**）が実在** |
| 4 | **'Les Folatières,' Puligny-Montrachet Premier Cru** | **2022** | **$720** | ✅🔍 **`exact` / `canonical_release`**<br>`cuvee:…-les-folatieres` / `vintage:…-2022` | 🔴 🏛 **INAO Puligny 仕様書の 1er Cru 表に climat `Les Folatières`（4 lieudit、色 = Blanc, rouge）が実在** |

🔴 **セクションは 4 行とも `FRANCE | WHITE > BURGUNDY`、`section_start_page` は 12、`source_line_no` 470–473。**
**メニュー原文の引用符はタイポグラフィック引用符（`'…,'`）であり、`flags` は 4 行とも空、`_collision_risk` は 4 行とも `LOW`。**

🔴 **本バッチで初めて、intake と mapping が完全に一致した。**
🔍 **`obp_intake_normalized_20260804.json` は 4 行とも `match_state: exact` / `producer_state: exact` /
`cuvee_state: exact` / `vintage_state: exact` / `confidence: 1.0`。**
🔍 **`research/out/t-01/mapping.json` は 4 行とも `resolved_to: "canonical_release"` で producer + cuvee + vintage が揃う。**
→ **既知の「intake と mapping が resolved の定義で食い違う」問題は、本生産者では発生していない。**

---

### 🔴 行 2 ―― `La Pièce sous le Bois` は Meursault か Blagny か（**本ドシエの中心的な設問。決着した**）

**設問**: この climat は Blagny の丘の上にあり、色と生産者の選択によって
`Meursault Premier Cru` / `Blagny Premier Cru` / `Meursault-Blagny` のいずれでも売られうる、とされる。
**canonical の `classification = "Meursault 1er Cru"` / `subregion = "Meursault Premier Cru"` は裏づけられるのか。**

**🏛 INAO 仕様書 3 本を実読した結果、答えは完全に確定する。**

| # | 🏛 条文（原文） | 帰結 |
|---|---|---|
| **A** | **Blagny 仕様書 I 章 III**: 「**L'appellation d'origine contrôlée « Blagny » est réservée aux vins tranquilles rouges.**」 | 🔴 **AOC Blagny は**赤専用**。白の Blagny は制度上**存在しない** |
| **B** | **Blagny 仕様書 IV 章 2° b) の 1er Cru 表**: commune **MEURSAULT** / climat **`La Pièce sous le Bois`** / lieudit `La Pièce sous le Bois (en partie)` | **この climat は確かに Blagny 1er Cru でもある ―― ただし A により**赤の場合だけ** |
| **C** | **Meursault 仕様書 I 章 III**: 「**L'appellation d'origine contrôlée « Meursault » est réservée aux vins tranquilles blancs ou rouges. Toutefois, pour les vins issus des parcelles incluses dans l'aire de production de l'appellation d'origine contrôlée « Blagny » l'appellation d'origine contrôlée « Meursault » est réservée aux seuls vins tranquilles blancs.**」 | 🔴 **Blagny の区域に入る区画からの Meursault は**白のみ** |
| **D** | **Meursault 仕様書 IV 章 2° b) の 1er Cru 表**: climat **`La Pièce sous le Bois`** / lieudit `La Pièce sous le Bois (en partie)` / **色 = `Blanc`** | 🔴 **Meursault 1er Cru として、白で、明示的に実在する** |
| **E** | **Meursault 仕様書の同表には、climat 名 `Blagny` の行が別に存在し**、その lieudit として `La Jeunellotte` / `La Pièce sous le Bois (en partie)` / `Sous le Dos d'Ane (en partie)` / `Sous Blagny` / `Les Ravelles` が並ぶ（色 = `Blanc`） | 🔴 **同じ畑を、climat 名 `Blagny` で名乗ることもできる** |
| **F** | 🏛 **BIVB 公式 fiche n°49 の Meursault 1er Cru 一覧は、これを一語で要約する ――「`La Pièce sous le Bois` **ou Blagny**」** | **A〜E の帰結を BIVB が確認している** |

🔴 **結論（フロアで使える形）**
1. **白なら `Meursault Premier Cru` である。「Blagny 1er Cru の白」はありえない ―― Blagny は赤専用だから。**
2. **同じ白を `Meursault 1er Cru "Blagny"` と名乗ることも制度上できる。両方が正しい名乗りである。**
   → **これが「Meursault-Blagny」という通称の正体である。**
3. 🔴 **canonical の `classification = "Meursault 1er Cru"` と `subregion = "Meursault Premier Cru"` は
   INAO によって裏づけられている。本ドシエで唯一の「canonical の格納値が公式と一致した」項目である。**
4. ⚠️ **ただしラベル実物でどちらの名乗りを採っているかは未確認。** → Open Questions 3

⚠️ 🔴 **`(en partie)`（一部）の注記に注意。**
🏛 **`La Pièce sous le Bois` の lieudit は、Meursault 仕様書でも Blagny 仕様書でも `(en partie)` と付されている。
つまり地籍上の `La Pièce sous le Bois` の**全部ではなく一部**が、それぞれの 1er Cru 区域に入っている。**
⚠️ **Alvina Pernot がその中のどこを持っているかは、本調査では一切不明である。**

---

### 🔴 行 3 ―― `La Garenne`（**`Clos de la Garenne` と混同禁止**）

🏛 **INAO Puligny 仕様書 1er Cru 表（実読）**

| climat | lieudit | 色 |
|---|---|---|
| **`La Garenne`** | **`La Garenne ou Sur la Garenne`** | 🔴 **`Blanc`（白のみ）** |
| **`Clos de la Garenne`** | **`Clos de la Garenne ou Champ Canet`** | **`Blanc, rouge`** |

🔴 **これは 2 つの別々の climat である。**
**`La Garenne` は白専用、`Clos de la Garenne` は白・赤の両方。lieudit も違う
（`Clos de la Garenne` の lieudit は `Champ Canet` と別名関係にある）。**
→ 🔴 **OBP 行 3 の印字は `'La Garenne,'` であり、`Clos de la Garenne` ではない。両者を言い換えてはならない。**
→ §Staff Notes ⚠️ ⑤

🔴 🏛 **さらに `La Garenne` は appellation をまたぐ。**
**Blagny 仕様書の 1er Cru 表には、commune **PULIGNY-MONTRACHET** の climat として
`La Garenne ou sur la Garenne` が入っている（lieudit `… (en partie)`）。**
→ 🔴 **つまり同じ `La Garenne` の畑が、**白なら Puligny-Montrachet 1er Cru、赤なら Blagny 1er Cru** になる。**
**行 2 とまったく同じ構造が、行 3 にも隠れている。**

**綴りの照合（🏛 INAO / BIVB 対 🔍 OBP / canonical）**

| 出典 | 表記 |
|---|---|
| 🏛 **INAO climat 名** | `La Garenne`（**冠詞あり**） |
| 🏛 **INAO lieudit 名** | `La Garenne ou Sur la Garenne` |
| 🏛 **BIVB 17 climat 一覧** | `La Garenne` |
| 🔍 **OBP 印字** | `'La Garenne,'` ✅ **INAO と一致** |
| 🔍 **canonical `name`** | `"La Garenne"` ✅ **文字列としては一致（引用符を除けば）** |

---

### 🔴 行 4 ―― `Les Folatières`（4 lieudit の束）

🏛 **INAO Puligny 仕様書 1er Cru 表（実読）** ―― `Les Folatières` は単一の地籍地名ではなく **4 つの lieudit を束ねた climat** である。

| climat | lieudit | 色 |
|---|---|---|
| **`Les Folatières`** | **`Es Folatières`** | Blanc, rouge |
| | **`En la Richarde dit Les Folatières`** | Blanc, rouge |
| | **`Peux Bois dit Les Folatières`** | Blanc, rouge |
| | **`Au Chaniot dit Les Folatières`** | Blanc, rouge |

→ 🔴 **「Folatières」と名乗れる範囲は地籍上 4 区画にまたがる。造り手ごとにどこを持つかは違いうる。**
⚠️ **Alvina Pernot がこの 4 つのどこを持っているかは、本調査では一切不明である。**

**綴りの照合** ―― 🏛 INAO `Les Folatières`（冠詞あり）／ 🔍 OBP `'Les Folatières,'` ✅ 一致 ／
🔍 canonical `"Les Folatières"` ✅ 一致（引用符を除けば）。

---

### 🔴 冠詞の一括正規化は「してはならない」―― INAO 自身のリストが内部で矛盾している

**Batch 8/10 の指摘（`Les Bouchères` は冠詞あり、`Perrières` は冠詞なし）を、本調査は同じ 2 文書の中で再現した。**

| 🏛 出典 | 冠詞あり | 冠詞なし |
|---|---|---|
| **INAO / BIVB Puligny 17 climat** | `La Garenne` / `Les Folatières` / `Les Chalumaux` / `Le Cailleret` / `Les Demoiselles` / `Les Pucelles` / `Les Perrières` / `Les Combettes` / `Les Referts` | 🔴 **`Sous le Puits` / `Champ Gain` / `Champ Canet` / `Clavaillon`** |
| **BIVB Meursault 19 climat** | `Les Cras` / `Les Caillerets` / `Les Bouchères` / `Les Gouttes d'Or` / `Les Ravelles` / **`Le Porusot`** | 🔴 **`Charmes` / `Perrières` / `Genevrières` / **`Porusot`**（`Le Porusot` と**同一リスト内に併存**）** |

🔴 **BIVB の Meursault 一覧は `Le Porusot` と `Porusot` を、`Perrières` と `Clos des Perrières` を、
**同じ 19 件のリストの中に別項目として**並べている。**
→ 🔴 **したがって「冠詞を落とす」「冠詞を付ける」のいずれの一括ルールも、公式リストに対して誤りを生む。
正規化は INAO の実リストとの diff でしか行えない。**

🔴 **canonical はすでにこの罠を踏んでいる。**
🔍 **`leprince-garenne-2022`（`Frédéric Leprince`）の `name` は `"Garenne"` ―― 冠詞が落ちている。
INAO の climat 名は `La Garenne` であり、`Garenne` という climat は存在しない。** → §Canonical Conflict

---

### 🔴 行 1 ―― `Les Vignes de Mon Père` は何か（**村名の独自名キュヴェ**）

🏛 **制度側から言えること**
- **AOC Puligny-Montrachet（村名）は 1937 年制定。白は事実上 Chardonnay。**
- 🏛 **Puligny 仕様書 I 章 II**: 「**原産地呼称の名は、原産の climat 名、または『premier cru』の表示、
  またはその両方で補うことができる**」。
  → 🔴 **仕様書が想定している補足名は「climat 名」である。`Les Vignes de Mon Père` は climat 名ではない。**
  **つまりこれは appellation 制度の外側にある**独自のキュヴェ名（fantasy name）**であり、
  村名 AOC のワインに生産者が任意に付した商標的な文字列である。**
- ⚠️ **フランスには米国 TTB COLA のような公開ラベル登録簿が存在しないため、
  「2023 年産がこの名で公式に存在する」ことを公的登録簿で確認する経路が無い。**
  🔍 **確認できたのは、OBP メニューと canonical が 2023 を保持していること、および
  AOC Puligny-Montrachet 2023 が制度上成立することだけである。** → Open Questions 4

⚠️ 🔴 **「どの区画か」は不明である。**
**名称は「わが父の畑」を意味し、父の畑から造られたキュヴェであることをラベル自身が述べている。
しかし父が誰か、どの lieudit かは、公的資料に一切現れない。**
🏛 **登記から言える隣接事実は 1 つだけ ―― Alvina は `SC NOYERS BRETS`（Puligny、土地保有型 NAF 68.20B）に
`PERNOT, Michel Henri`（1959 年生）とともに名を連ねている。**
❓ **登記はこの人物との血縁を述べていない。断定してはならない。**

### 🔴 canonical が模型化していない文字列の形（**未採番。採番は CTO 判断**）

🔴 **`Les Vignes de Mon Père` は、村名 AOC に付された独自キュヴェ名である。
一方 `La Garenne` / `Les Folatières` / `La Pièce sous le Bois` は、INAO の法定 climat 名である。**
🔍 **canonical は 4 件とも同じ `name` フィールドに、同じ形（二重引用符で囲んだ文字列）で格納しており、
「これは法定 climat 名である／これは生産者の独自名である」という区別をどこにも持たない。**
→ 🔴 **結果として、`name` の値が INAO のリストと照合可能かどうかが、レコードからは判定できない。**
**行 1 だけは照合してはならず、行 2〜4 は照合しなければならない ―― この差がデータに載っていない。**
⚠️ **これは既知ファミリー（`P-*` / `C-*` / `V-*` / `S-*` / `CAT-*`）のいずれにも該当しない形である。
本ドシエで新しい番号は開かない。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 「ラ・ピエス・スー・ル・ボワ」は、白だからムルソーである。ブラニーではありえない。**
「**この畑はブラニーの丘の上にあり、ムルソー村の中にあります。**
**INAO の原産地呼称仕様書によれば、AOC ブラニーは**赤専用**です。
そしてムルソー側の仕様書は、ブラニーの区域に入る区画から造られたムルソーは**白のみ**と定めています。**
**つまり、同じ畑でも赤ならブラニー、白ならムルソー・プルミエ・クリュ ―― 色で呼び名が変わります。**
**当店のこれは白ですから、ムルソー・プルミエ・クリュです。**
**なお、同じ白を『ムルソー 1er Cru ブラニー』と名乗ることも制度上できます。
ブルゴーニュワイン委員会の公式資料も、この畑を『**ラ・ピエス・スー・ル・ボワ、またはブラニー**』と併記しています。**」

**② 「ラ・ガレンヌ」と「クロ・ド・ラ・ガレンヌ」は別の畑である。**
「**ピュリニー＝モンラッシェのプルミエ・クリュは公式に 17 クリマあり、
『ラ・ガレンヌ』も『クロ・ド・ラ・ガレンヌ』も、**別々に**その中に入っています。**
**ラ・ガレンヌは仕様書上**白専用**、クロ・ド・ラ・ガレンヌは白・赤の両方です。**
**当店にあるのは『ラ・ガレンヌ』の方です。**
**そしてラ・ガレンヌにも、実は先ほどのムルソーと同じ構造があります ――
赤で造ればブラニー・プルミエ・クリュになる畑なのです。**」

**③ フォラティエールは 4 つの地籍地名を束ねた大きなクリマである。**
「**『レ・フォラティエール』は単一の区画ではなく、
Es Folatières、En la Richarde、Peux Bois、Au Chaniot ―― 4 つの地名を束ねたクリマです。
だから造り手によって、同じフォラティエールでも見ている斜面が違います。**
**ちなみにピュリニーは、白の畑 95.92 ヘクタールのうち 90.97 ヘクタールがプルミエ・クリュという、
村名よりプルミエ・クリュの方が広い珍しい村です。**」

### 追加で使える一手

- **キュヴェ名について訊かれたら**: 「『**レ・ヴィーニュ・ド・モン・ペール**』は『**わが父の畑**』という意味です。
  **村名クラスに造り手が付けた独自の名前で、公式なクリマ名ではありません。**
  **どの区画かは公表されていないので、それ以上は申し上げられません。**」
- **アペラシオンの性格を言うとき（BIVB 公式の言葉として）**: ピュリニーは
  「**サンザシ、熟した葡萄、アーモンドペースト、ヘーゼルナッツ、琥珀、レモングラス、青りんご**」、
  ムルソーは「**焼いたアーモンドとヘーゼルナッツ、サンザシ、ニワトコ、シダ、菩提樹、ヴェルヴェーヌ、火打石、
  バター、蜂蜜、柑橘**」「**豊かで脂の乗った、絹のあらゆる音域を降りてゆく偉大な熟成型の白**」。
  **必ず「これはアペラシオンの一般的性格であって、この造り手のワインの描写ではありません」と添えること。**
- 🔴 **供出温度は 2 本立てで**: 🏛 **BIVB 公式はピュリニー **11〜13 °C**、ムルソー **12〜14 °C**。
  **同じ造り手の 4 本でも、ムルソーの 1 本だけ推奨が高い。**
- **合わせ（BIVB 公式）**: ピュリニー＝**フォワグラ、オマール、ラングスト、海の魚のグリル／ポワレ、
  シェーヴル、ルブロション、ブリ・ド・モー**。ムルソー＝**白いソースの仔牛・家禽、
  焼いた／ソースを纏った甲殻類（ガンバ、オマール、ラングスト）、ブルーチーズ、フォワグラ**。

### ⚠️ 言ってはいけないこと（**一次資料に根拠が無い／出典が沈黙している**）

1. 🔴 ⚠️ **面積を言わない。ヘクタール数も本数も樽数も、一切口にしない。**
   **自社畑の面積、所有区画、買いブドウの割合 ―― どれも公的資料に存在しない。**
   **世に流布している数字はすべて小売・輸入元・評論由来であり、本ドシエはそれを裏づける一次資料を持っていない。**
2. 🔴 ⚠️ **「自社畑のドメーヌです」と断定しない。同時に「ネゴシアンです」とも断定しない。**
   🏛 **登記上の NAF は `46.90Z`（非特化の企業間卸売）であり、村の他のドメーヌの `01.21Z`（ブドウ栽培）ではない。
   労働協約も IDCC `0493`（飲料卸売）である。**
   **一方で Alvina は `SC NOYERS BRETS`（土地保有型 NAF `68.20B`）にも名を連ねており、
   畑を別法人に置く一般的な構成とも整合する。**
   ❓ **登記はどちらとも断定していない。** 言うなら「**登記上は Puligny 村に本店を置く小さな会社です**」まで。
3. 🔴 ⚠️ **「ポール・ペルノの孫娘」と言わない。**
   **この主張は小売・輸入元・評論に広く出ているが、本調査は一次資料で確認していない。**
   🏛 **登記が語るのは、`SC NOYERS BRETS` で `PERNOT, Michel Henri`（1959 年生）と共同していること、
   および同じ村に別法人 `DOMAINE PERNOT PAUL ET SES FILS`（SIREN 315015487）が存在することだけで、
   両者を結ぶ記述は無い。**
   **キュヴェ名『レ・ヴィーニュ・ド・モン・ペール』は「父の畑」を意味するが、父が誰かはラベルも述べていない。**
4. 🔴 ⚠️ **「ペルノ」という姓だけで話を進めない。ピュリニー村には別のペルノが何軒もある。**
   🏛 **同じ 21190 Puligny-Montrachet の公的登記に、
   `DOMAINE PERNOT PAUL ET SES FILS`（315015487、`7 place du Monument`、1979 年、NAF 01.21Z）、
   `PAUL PERNOT`（314348103 / 398157990）、
   `DOMAINE PERNOT BELICARD`（383186772、`2 rue du Meix Pelletier`、1991 年、NAF 01.21Z）、
   `SARL PERNOT BELICARD`（900456641、NAF 46.34Z）、
   `JEAN-MARC PERNOT`（350822342、`6 rue de But`、1989 年）、
   `CAROLE PERNOT`（984594705、`4 rue de But`、2024 年）、
   `MICHEL PERNOT`（398158139）が存在する。**
   **必ず「アルヴィナ・ペルノ」とファーストネームまで込みで言うこと。**
   🔍 **当店のリストに載っている `Pernot` は、この 4 本＝アルヴィナだけである**（OBP 全 704 行を確認）。
5. 🔴 ⚠️ **「ラ・ガレンヌ」と「クロ・ド・ラ・ガレンヌ」を言い換えない。**
   🏛 **INAO 仕様書上、別々の climat である（前者は白専用、後者は白・赤）。**
   **輸入元のページには同じ造り手の『クロ・ド・ラ・ガレンヌ』が出ているが、
   当店のリストにあるのは『ラ・ガレンヌ』の方である。**
6. 🔴 ⚠️ **「ブラニーの白です」と言わない。**
   🏛 **AOC ブラニーは赤専用である。「ブラニーの白」は制度上存在しない。**
   **言うなら「ブラニーの丘にある畑ですが、白なのでムルソー・プルミエ・クリュです」。**
7. 🔴 ⚠️ **「ビオです」「オーガニックです」「ビオディナミです」と言わない。**
   🏛 **フランスの有機農業公的登録簿（Agence Bio）に、この法人の登録は存在しない
   （SIRET 完全一致・SIREN 一致とも `nbTotal: 0`、政府登記の `est_bio` も `false`）。**
   ⚠️ **同時に「有機的な栽培をしていません」とも言わない。認証の不在は農法についての情報を含まない。**
   **農法を述べた一次資料が存在しないので、農法の話はしない。**
8. 🔴 ⚠️ **醸造の数字を言わない。**
   **樽のサイズ、新樽比率、熟成月数、バトナージュ、澱との接触、野生酵母、アルコール度数、生産本数 ――
   一次資料はゼロである。**（canonical にも入っていない。→ §Canonical Conflict）
9. ⚠️ **「シャルドネ 100%」と断定しない。**
   🏛 **INAO 仕様書は、Puligny-Montrachet・Meursault いずれの白も
   `chardonnay B` **および** `pinot blanc B` を認めている。**
   **この造り手が 100% シャルドネであると述べた一次資料は存在しない。**
   （canonical の 4 件には `grapes` フィールドそのものが無い。）
10. ⚠️ **第三者点数を口にしない。**
    **canonical には点数が入っていないが、評論媒体の点数が検索で容易に出る。
    公式ソース原則により、それは本ドシエの根拠にならない。**
11. ⚠️ **創業年を言わない。**
    🏛 **登記できるのは「法人設立 2018-10-05」「現在の事業所開設 2021-09-10」だけである。**
    **「2018 年に最初のヴィンテージを売った」といった話は一次資料で確認していない。**
    ⚠️ **canonical にも `founded_year` は無い。**
12. ⚠️ **公式サイトを案内しない。**
    **`alvinapernot.com` はドメインとしては存在するが、9 バイトの空ページしか返さない。
    案内するとお客様が白紙を見ることになる。**
13. ⚠️ **`AP WINES` で検索するよう勧めない。**
    🔴 **`apwines.com` はオーストラリアの `Andrew Peace Wines` であり、まったくの別会社である。** → §Sources
14. ⚠️ **区画（lieudit）を特定して話さない。**
    **フォラティエールの 4 lieudit のどれか、ラ・ピエス・スー・ル・ボワの `(en partie)` のどの部分か、
    『わが父の畑』がどこか ―― いずれも本調査では不明である。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **4 件を escalate する。いずれも実行していない。**

---

### **CC-1 — `S-2`（銘柄名に二重引用符が埋め込まれている）: 既存ファミリーへの証拠追加**

1. **衝突する canonical ID（本生産者の 4 件すべて）**
   - `pernot-meursault-psb-2022` → `name` = `"\"La Pièce Sous le Bois\""`
   - `pernot-puligny-vmdp-2023` → `name` = `"\"Les Vignes de Mon Père\""`
   - `pernot-puligny-garenne-2022` → `name` = `"\"La Garenne\""`
   - `pernot-puligny-folatieres-2022` → `name` = `"\"Les Folatières\""`
2. **なぜ問題か**
   **`name` フィールドの値そのものに `"` 文字が 2 つ含まれている。表示層で引用符を付ける実装と二重になり、
   文字列比較・スラグ生成・fuzzy スコアに影響する。**
3. 🔴 **本生産者が加える新しい証拠 ―― 「なぜ 175 件も生き残ったのか」の説明**
   🔍 **intake の `evidence` 文字列が、マッチャの内部動作をそのまま露出させている ――**
   **`名称トークン集合一致: 'La Garenne' ≡ '"La Garenne"'`**
   **`名称トークン集合一致: 'Les Folatières' ≡ '"Les Folatières"'`**
   → 🔴 **マッチャは引用符を正規化で捨てたうえで `exact` / `confidence: 1.0` を返している。**
   **つまり `S-2` の破損はマッチング結果には一切現れない。`_collision_risk` も 4 行とも `LOW`。**
   🔴 **`S-2` が canonical 全体で 175 件（18.9%）まで蓄積できたのは、
   マッチング指標がこの破損に対して完全に盲目だからである。**
   **「マッチングが通っているから健全」という推論は、この family に対しては成立しない。**
4. **OBP への影響**
   **今回の 4 本の解決は妨げていない（4/4 exact）。影響は表示層とスラグ生成、および他生産者への誤候補である。**
5. **推奨（🔴 DO NOT EXECUTE）**
   **`S-2` の一括処理に合流させる。新しい番号は開かない。**
   ⚠️ 🔴 **一括処理の設計上の必須条件 ―― スイープが別に切り分けた
   「正当なフランス語のエリジオン（`L'Esprit` 型）78 件」を巻き込んではならない。**
   **`'` と `"` は別文字であり、`S-2` の対象は `"`（U+0022）で囲まれたものに限られる。**
6. **Confidence: High**（4 件とも機械的に確認済み）

---

### **CC-2 — 🔴 4 レコードすべてが「空殻」である（本生産者最大の実務上の問題）**

1. **衝突する canonical ID**: **`pernot-meursault-psb-2022` / `pernot-puligny-vmdp-2023` /
   `pernot-puligny-garenne-2022` / `pernot-puligny-folatieres-2022`（全 4 件）**
2. 🔴 **なぜ問題か**
   **4 件が保持しているフィールドは、次の 14 個だけである ――**
   `id` / `producer` / `name` / `vintage` / `country` / `region` / `subregion` / `type` / `color` /
   `classification` / `glassware` / `indicator` / `obp_format` / `serving_temp` / `tags`。
   🔴 **`grapes` / `aging` / `founded_year` / `description` / `obp_note` / `obp_note_en` /
   `winemaking` / `tasting` / `terroir` / `points` は、**キーごと存在しない**。**
   **依頼が求めた「格納値と公式の照合」は、照合すべき値が無いため 10 項目中 10 項目で実行不能だった。**
   🔴 **フロアが読む文面（`obp_note`）が 4 件とも無い ―― $360 / $640 / $720 / $720 の 4 本すべてについて、
   canonical は一語も語らない。**
3. **証拠** 🔍 **`migration/out/export/db_wine_canonical.json`（928 要素）を Python で直接パースし、
   4 レコードを全文出力して確認。**
4. **OBP への影響**
   🔴 **直接的かつ最大級。マッチングは 4/4 完璧（`exact` / `canonical_release` / `confidence 1.0`）だが、
   到達した先が空である。**
   🔴 **Bachelet-Monnot で観測された「高いボトルほど空殻」という非対称が、
   ここでは非対称ですらなく**全件が空**という形で現れている。**
   **`match_state = exact` は「語れる」を意味しない ―― 本生産者はその最も純粋な実例である。**
5. **推奨（🔴 DO NOT EXECUTE）**
   - 🔴 **これは conflict ではなく **gap**（内容の不在）である。既存の conflict family のいずれにも該当しない。**
     **ただし「レコードが存在しない」gap とも違う ―― レコードは存在し、正しく結線され、中身だけが無い。**
     ⚠️ **`match_state` と「内容の充足」を区別する指標が、現状の intake / mapping には無い。**
     **`resolved_to: canonical_release` を「解決済み」と数えると、この 4 本は成功として集計される。**
   - **埋める材料は現時点で存在しない**（公式サイト未公表、fiche technique 未発見）。**着手すべきでない。**
6. **Confidence: High**（機械確認済み）

---

### **CC-3 — 🔴 `name` の綴りが公式と食い違う。ただし食い違っているのは canonical であってメニューではない**

1. **衝突する canonical ID**: **`pernot-meursault-psb-2022`**
2. 🔴 **なぜ問題か**

   | 出典 | 表記 |
   |---|---|
   | 🏛 **INAO Meursault 仕様書 1er Cru 表** | **`La Pièce sous le Bois`**（`sous` は**小文字**） |
   | 🏛 **INAO Blagny 仕様書 1er Cru 表** | **`La Pièce sous le Bois`**（小文字） |
   | 🏛 **BIVB 公式 fiche n°49** | **`La Pièce sous le Bois ou Blagny`**（小文字） |
   | 🔍 **OBP 印字** | **`'La Pièce sous le Bois,'`** ✅ **3 つの公式資料すべてと一致** |
   | 🔍 **canonical `name`** | 🔴 **`"La Pièce Sous le Bois"`（`Sous` が**大文字**）** ―― **単独で公式と食い違う** |

   🔴 **これは「メニューが欠陥側とは限らない」の 4 件目の反例であり、本バッチで最も明快な形である。**
   **メニューは 3 つの独立した公的資料と完全に一致し、canonical だけが外れている。**
3. **証拠** 🏛 **INAO 2 文書（`%PDF` 検証済み）の 1er Cru 表を `pdftotext -layout` で実読。
   🏛 BIVB fiche n°49 の climat 一覧。🔍 canonical の直接パース。**
4. **OBP への影響**
   **マッチングは通っている（マッチャが大小文字を正規化するため）。影響は表示と、
   INAO リストとの機械照合が失敗する点に限られる。**
   ⚠️ 🔴 **ただし重要な副作用がある ―― この綴りのまま表示すると、
   INAO の法定 climat 名として検証できない文字列が客前に出る。**
5. **推奨（🔴 DO NOT EXECUTE）**
   ⚠️ **既知ファミリー（`P-*` / `C-*` / `V-*` / `S-*` / `CAT-*`）のいずれにも当てはまらない。
   「canonical の climat 名が INAO の綴りから外れている」という形である。**
   **新しい番号を本ドシエで勝手に開くことはしない。採番の要否は CTO 判断とする。**
   🔴 **なお下の CC-4 と同じ形であり、単独修正ではなく climat 名の一括照合として扱うべきである。**
6. **Confidence: High**（3 つの公的資料と機械照合済み）

---

### **CC-4 — 🔴 同じ INAO climat が、canonical で 3 つの異なる `name` 形と 2 つの `classification` 文字列を持つ（未採番）**

1. **衝突する canonical ID**（🔍 `name` に climat 名を含む全レコードを走査。**本生産者の周辺に限定**）

   | id | `producer` | `name` の実値 | `classification` |
   |---|---|---|---|
   | `pernot-puligny-folatieres-2022` | Alvina Pernot | `"Les Folatières"` | **`Puligny-Montrachet 1er Cru`** |
   | `bachelet-monnot-folatieres-2022` | Domaine Bachelet-Monnot | `"Les Folatières"` | **`Puligny-Montrachet Premier Cru`** |
   | `bachelet-monnot-folatieres-2023` | Domaine Bachelet-Monnot | `"Les Folatières"` | **`Puligny-Montrachet 1er Cru`** |
   | `genot-puligny-folatieres` | Domaine Génot-Boulanger | 🔴 **`Puligny-Montrachet "Les Folatières"`** | **`Puligny-Montrachet Premier Cru`** |
   | `pernot-puligny-garenne-2022` | Alvina Pernot | `"La Garenne"` | **`Puligny-Montrachet 1er Cru`** |
   | `leprince-garenne-2022` | Frédéric Leprince | 🔴 **`"Garenne"`** | **`Puligny-Montrachet Premier Cru`** |

2. 🔴 **なぜ問題か ―― 2 つの独立した揺れが重なっている**
   - **(a) `name` の形が 3 通りある**: `"Les Folatières"`（climat のみ）／
     `Puligny-Montrachet "Les Folatières"`（**appellation を name の中に埋め込み**）／
     `"Garenne"`（🔴 **冠詞が脱落。INAO の climat 名は `La Garenne` であり、`Garenne` は存在しない**）。
   - **(b) `classification` が `Puligny-Montrachet 1er Cru` と `Puligny-Montrachet Premier Cru` で揺れる。**
     🔴 **本生産者の 4 件の内部では一貫している**（`1er Cru` 側）**が、隣の生産者とは揃わない。**
     **`subregion` は全件 `Puligny-Montrachet Premier Cru` で揃っており、ずれているのは `classification` だけ。**
   🔴 **結果として「同じ INAO climat のワインを全部集める」クエリが、どの書き方でも取りこぼす。**
3. **証拠** 🔍 **canonical 928 件を Python で走査し、`name` に `Garenne` / `Folati` / `sous le Bois` /
   `Vignes de Mon` を含むレコードを全件抽出。🏛 対照は INAO Puligny 仕様書と BIVB fiche n°62。**
4. **OBP への影響**
   **本生産者 4 本のマッチングは妨げていない。影響はグルーピング・絞り込み・横断表示、
   および将来の climat 単位の分析にかかる。**
5. **推奨（🔴 DO NOT EXECUTE）**
   - 🔴 **`Premier Cru` / `1er Cru` の揺れは、Bachelet-Monnot のドシエでも同一生産者内で観測されている。
     本ドシエは同じ揺れが**生産者をまたいでも**起きることを追加確認した。**
     **canonical 全体での件数は未計測。横断で数えてから正規表記を 1 つ決めるべきである。**
   - 🔴 **`"Garenne"` の冠詞脱落は、単純な一括正規化で直してはならない。**
     🏛 **INAO / BIVB の公式リストは、同一リスト内で `La Garenne` と `Champ Gain`、
     `Le Porusot` と `Porusot`、`Les Bouchères` と `Perrières` を併存させている。**
     **正しい直し方は INAO の実リストとの diff のみである。** → §Important Cuvées
   - ⚠️ **既知ファミリーのいずれにも当てはまらない。本ドシエで新しい番号は開かない。採番は CTO 判断。**
6. **Confidence: High**（機械確認済み。ただし canonical 全体での件数は未計測 ―― 意図的に走査していない）

---

### 🔴 **偽陽性として除外リストに載せるもの（重複ではない）**

**`Alvina Pernot` は、Puligny-Montrachet の他の `Pernot` とはまったく別の事業者である。canonical の重複ではない。**

| | Alvina Pernot | Paul Pernot et ses Fils | Pernot Belicard |
|---|---|---|---|
| 🏛 **登記名 / SIREN** | **`AP WINES SAS` / 843307471** | **`DOMAINE PERNOT PAUL ET SES FILS` / 315015487** | **`DOMAINE PERNOT BELICARD` / 383186772** |
| 🏛 **住所** | **4 rue de Bois, 21190 Puligny-Montrachet** | **7 place du Monument, 21190 Puligny-Montrachet** | **2 rue du Meix Pelletier, 21190 Puligny-Montrachet** |
| 🏛 **NAF** | 🔴 **`46.90Z`（非特化卸売）** | **`01.21Z`（ブドウ栽培）** | **`01.21Z`（ブドウ栽培）** |
| 🏛 **設立** | **2018-10-05** | **1979-01-01** | **1991-08-01** |
| 🔍 **canonical** | **4 件** | 🔴 **0 件（不在＝gap。OBP にも掲載なし）** | 🔴 **0 件（同上）** |

🔴 **これは canonical conflict として報告しない。近似名の衝突として除外リストに永続保存する。**
🔍 **`Paul Pernot` / `Pernot Belicard` は OBP メニュー全 704 行にも登場しないため、
canonical における不在は gap ですらない（そもそも必要とされていない）。**

🔍 **`producer` フィールド一致 4 件 / prose のみの一致 **0 件**。**
🔴 **`D-2026-08-05-08`（生産者名の部分文字列マッチで他生産者の prose を拾う欠陥）は、
本生産者では発生していない。`Pernot` を含む canonical レコードは、4 件すべてが真正である。**

---

## Sources

### 🔴 サイト真正性チェック（**必須手順。結論: 公式サイトは実質的に存在せず、別法人の類似ドメインを 1 件棄却した**）

| 手順 | 結果 |
|---|---|
| 🔴 **`alvinapernot.com` の実体** | **A レコード `185.2.5.9` あり、MX（`mail-fr.securemail.pro`）あり ―― ドメインは生きている。**<br>🔴 **しかし `GET /` は `content-length: 9`、中身は `<!-- -->` の 9 バイトのみ。`server: nginx`、`last-modified: Wed, 23 May 2018 15:34:44 GMT`（＝ドメイン登録より前。ホスティング業者の既定の空 index）。**<br>**`www` も同一。`/robots.txt` `/sitemap.xml` `/en/` `/accueil` `/domaine.html` `/wp-login.php` はすべて 404** |
| 🏛 **WHOIS `alvinapernot.com`** | **登録日 `2018-11-03`（法人設立 2018-10-05 の約 1 か月後）／レジストラ `Register S.p.A.`（Amen）／登録者国 **`FR`**／NS `NS1/NS2.AMENWORLD.COM`**<br>→ **フランス側の当事者が創業直後に取得したドメインである、という点までは整合的** |
| 🔴 **Wayback による経時確認** | **CDX に記録は 1 件のみ（`2021-11-26T00:43:46`、`text/html`、`200`）。**<br>🔴 **`…id_/` で原本を取り直したところ、**現在と 1 バイト違わぬ同一の 9 バイト**だった。**<br>→ **少なくとも 2021 年以降、このドメインは一度も内容を持っていない** |
| **候補ドメインの DNS 総当たり（8 件）** | `alvina-pernot.com` / `alvinapernot.fr` / `alvina-pernot.fr` / `alvinapernot.net` / `alvinapernot.eu` / `alvinapernot.wine` / `domaine-alvina-pernot.com` / `domainealvinapernot.com` / `apwines.fr` / `apernot.com` / `pernot-abadie.com` / `alvinapernotwines.com` ―― **すべて A レコード無し** |
| 🏛 **公的登録簿による裏取り** | **Agence Bio に該当レコードが存在しないため `siteWebs` による裏取りは不可。**<br>**政府企業登記の `liste_enseignes` は `null`、`nom_commercial` も `null`** |
| 🔴 ⚠️ **棄却した類似ドメイン ①** | 🔴 **`apwines.com` ―― 法人名 `AP WINES SAS` と完全に一致するため最初に当たったが、実体は<br>**オーストラリアの `Andrew Peace Wines`** である。**<br>**WHOIS: 登録日 `2000-01-24`（AP WINES SAS 設立の 18 年前）、登録者国 **`AU`**、NS `NS1–NS4.DIGITALPACIFIC.COM(.AU)`。**<br>**サイトは Wix 製、`<title>Andrew Peace Wines \| Australian Wine`、本文は「1980 年にブドウ畑として始まり…オーストラリア最大級のワイン輸出業者」。連絡先は `domestic@apwines.com` / `international@apwines.com`。**<br>→ 🔴 **本バッチで 2 件目、通算 7 件目の look-alike。`NOT_THE_PRODUCER_apwines_andrew_peace.html` として保存。一語も使用していない** |
| **偽公式サイトの有無** | 🔴 **`Alvina Pernot` を騙るページは 1 件も出現しなかった。**検索に出るのはすべて小売・輸入元・評論であり、いずれも自らを生産者公式とは名乗っていない |

🔴 **結論 ―― 本ドシエは `✅`（生産者の公式一次資料）レイヤーを 1 件も持たない。**
**これは「探し方が足りない」のではなく、**この生産者が何も公表していない**という証明された状態である。**

### 🏛 使用した一次資料（公的登録簿・regulatory primary source のみ）

| 資料 | 取得した情報 | 真正性の担保 |
|---|---|---|
| 🔴 **`recherche-entreprises.api.gouv.fr`**（フランス政府公式企業検索 API。SIRENE / RNE 由来） | **SIREN 843307471 / SIRET 84330747100022、商号 `AP WINES SAS`、法人形態 5710、NAF 46.90Z、住所、設立日 2018-10-05、事業所開設日 2021-09-10、事業所数 2（開 1）、役員 Alvina Pernot（1988-06、Président de SAS）、従業員区分 01、IDCC 0493、`est_bio: false`**<br>**関連 2 社（`SC NOYERS BRETS` 914446372 / `AP&CO` 984511980）、Puligny 村の別 `Pernot` 法人 10 件** | **`api.gouv.fr` ＝ フランス政府 API プラットフォーム。INSEE の SIRENE と RNE を出典とする一次データ** |
| 🔴 **`opendata.agencebio.org/api/gouv/operateurs/`**（Agence Bio 公開 API） | 🔴 **SIRET 完全一致 `84330747100022` → `nbTotal: 0`。SIREN `843307471` → `nbTotal: 0`。**<br>**関連 4 SIREN もすべて `nbTotal: 0`。**⚠️ 参考の名称検索 `nom=pernot&departement=21` は 6 件返すが、すべて他県・他事業者 | **Agence Bio ＝ フランス農業省所管の有機農業開発振興機関。`/api/gouv/` は公的公開エンドポイント。**🔴 **完全一致 SIRET クエリが `nbTotal: 0` を返すことが、証明された不在である** |
| 🔴 **`api.insee.fr/metadonnees/V1/codes/nafr2/sousClasse/46.90Z`**（INSEE 公式ノメンクラチュア API） | **`46.90Z` = "Commerce de gros (commerce interentreprises) non spécialisé"** | **INSEE 公式。コード解釈を記憶に頼らず照合した** |
| 🔴 **INAO `extranet.inao.gouv.fr/fichier/pnocdcpuligny-montrachet.pdf`**（450,355 B、真正の PDF） | **Puligny-Montrachet 仕様書 v2.2（2010-09-15）。1er Cru 17 climat の全表（`La Garenne` / `Clos de la Garenne` / `Les Folatières` の 4 lieudit）、色の制限、encépagement、灌漑禁止、木片禁止、補糖上限** | ⚠️ 🔴 **ファイル名は全小文字ハイフン無し。`file` コマンドで PDF を検証済み** |
| 🔴 **INAO `extranet.inao.gouv.fr/fichier/PNOCDC-Meursault.pdf`**（453,328 B、真正の PDF） | 🔴 **Meursault 仕様書 v2.2（2010-09-15）。I 章 III の Blagny 条項、1er Cru 表の `La Pièce sous le Bois`（色 = Blanc）および climat `Blagny` の 5 lieudit、aire de proximité immédiate に `Puligny-Montrachet`** | 🔴 ⚠️ **ファイル名の罠を実測 ―― `PNOCDCMeursault.pdf`（ハイフン無し）は **HTTP 200 で 6,892 B の HTML** を返した。ハイフン入りだけが `%PDF`。**`xxd` で先頭 4 バイトを検証済み** |
| 🔴 **INAO `extranet.inao.gouv.fr/fichier/PNOCDC-Blagny.pdf`**（421,092 B、真正の PDF） | 🔴 **Blagny 仕様書 v2.2（2010-09-15）。I 章 III「réservée aux vins tranquilles rouges」、1er Cru 表（commune MEURSAULT の `La Pièce sous le Bois`、commune PULIGNY-MONTRACHET の `La Garenne ou sur la Garenne`）** | 🔴 **同じくハイフン無しは 6,889 B の HTML。`%PDF` を検証済み** |
| 🏛 **BIVB `vins-bourgogne.fr/…/57565.pdf`**（fiche n°62、Puligny-Montrachet） | **「Côte de Beaune の村名アペラシオン、Côte-d'Or 県」「1937 年制定」「1er Cru 17 climat」「Grand Cru 5」、テロワール、白 95.92 ha / 1er Cru 90.97 ha、公式テイスティング記述、ソムリエ助言、供出温度 11〜13 °C、17 climat 一覧** | **BIVB ＝ ブルゴーニュワイン生産者・商社の公式業際組織** |
| 🔴 🏛 **BIVB `vins-bourgogne.fr/…/57552.pdf`**（fiche n°49、Meursault） | 🔴 **1er Cru 19 climat 一覧に「`La Pièce sous le Bois` **ou Blagny**」および `Blagny` 単独。**テロワール、白 381.04 ha / 1er Cru 107.37 ha、公式テイスティング記述、ソムリエ助言、供出温度 12〜14 °C | 同上 |

⚠️ **`vins-bourgogne.fr` のパスは appellation ごとに異なる。model dossier の Puligny パス（`site/1/1160/1161/1163/`）は
現在 404 を返し、`site/321/402/57486/` が有効だった。**

### ⚠️ 🔴 棄却した資料（**事実の根拠として一切使用していない**）

**検索で出現した以下はすべて小売・輸入元・評論・集約サイトであり、公式ソース原則により事実の根拠から除外した。**
**KL Wines / JJ Buckley / Woodland Hills Wine Company / Caves Carrière / Clos Cachet Fine Wines /
Cuzziol Grandivini / FINE+RARE / Rueda Wine Co. / Bertrand's Wines / Mundidrinks /
The Fine Wine Experience / Vinous / Vivino。**

🔴 **とくに次の 3 点を明記する。**
- **輸入元・小売のページには「ポール・ペルノの孫娘」「夫 Philippe Abadie と 2018 年に創設」
  「Clos des Mouchères の直下と Clavoillon の下の 2 区画」「4 樽」といった具体的な記述がある。**
  🔴 **本調査はそれらが生産者による執筆であることを立証できなかった
  （レターヘッド無し、一人称無し、生産者名義の PDF 無し、生産者サイトからのリンク無し ――
  そもそも生産者サイトが公表されていない）。したがって `📄` の例外規定は適用できず、全面的に不採用とした。**
- 🔴 **`apwines.com`（Andrew Peace Wines、豪）は上記のとおり別法人であり、`NOT_THE_PRODUCER_` として保存した。**
- ⚠️ **TTB Public COLA Registry は、ブリーフの規定により米国生産者に限られるため照会していない。**
  **`Les Vignes de Mon Père` 2023 の公式なラベル確認経路は、本調査の許容範囲内には存在しなかった。**

### 🔍 canonical / OBP（THÉSEUS DB。**読み取りのみ・無変更**）

| 対象 | 実測 |
|---|---|
| **canonical レコード** | **`Alvina Pernot` = 4 件**（`producer` フィールド一致）。**prose のみの一致 = 0 件。**<br>🔴 **4 件とも `grapes` / `aging` / `founded_year` / `description` / `obp_note` / `winemaking` / `tasting` / `points` を持たない** |
| **OBP intake（正規化）** | **`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（全 704 行）に 4 行。**<br>**4 行とも `match_state: exact` / `confidence: 1.0` / `_collision_risk: LOW` / `source_quality_flags: []`** |
| **OBP inventory** | **`research/out/t-01/inventory.json`（全 768 行）の `source_line_no` 470–473。`section_start_page` 12、`producer_heading` = `Alvina Pernot`、`flags` はすべて空** |
| 🔴 **mapping 実測** | **`research/out/t-01/mapping.json` ―― 470/471/472/473 すべて `resolved_to: "canonical_release"`（producer + cuvee + vintage の 3 点が揃う）**<br>🔴 **intake と mapping が完全に一致した初の生産者。既知の食い違い問題は本生産者では発生していない** |
| **`Pernot` を含む他生産者** | 🔍 **OBP 全 704 行に `Pernot` は本生産者の 4 行のみ。`Paul Pernot` / `Pernot Belicard` はメニューにも canonical にも存在しない** |

**キャッシュ先**: `/Users/akiomatsumoto/Theseus_Phase0/research/producers/_sources/alvina-pernot/`
（`sirene_*.json`、`agencebio_*.json`、`CDC-Puligny-Montrachet.pdf` + `.txt`、`CDC-Meursault.pdf` + `.txt`、
`CDC-Blagny.pdf` + `.txt`、`BIVB-Puligny.pdf` + `.txt`、`BIVB-Meursault.pdf` + `.txt`、
`site_home.html`、`wayback_2021.html`、`wayback_cdx.json`、
`NOT_THE_PRODUCER_apwines_andrew_peace.html`。gitignore 対象）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | **SIREN / SIRET / 法人形態 / NAF / 住所 / 役員の氏名と生年月 / 従業員区分 / 労働協約まで、政府 API の一次データで確定。NAF コードの解釈も INSEE ノメンクラチュア API で照合済み。**⚠️ 旧事業所の所在だけ未取得 |
| **Overview** | **Medium** | **所在・法人構造・NAF が確定し、村の他ドメーヌとの登記上の差まで見えた。**🔴 **ただし「造り手自身の言葉」がゼロである** |
| **History** | 🔴 **Low** | **登記・WHOIS の日付 7 点のみ。**創業の経緯・修業歴・畑の取得史はすべて空白。**公表物が無いため、埋める手段が現時点で無い** |
| **Location** | 🔴 **High** | **本店所在が政府登記で確定（Puligny 村内）。**🔴 **さらに Meursault ⇄ Puligny が相互に aire de proximité immédiate に入るという法的接続まで INAO で取れた。**appellation 側のテロワール・面積・climat 一覧も公式 |
| **Farming** | 🔴 **High（結論について）／ None（実務について）** | 🔴 **有機認証の不在は、SIRET 完全一致 + SIREN + `est_bio` の 3 経路で証明された。これは強い negative である。**⚠️ **一方、実際の農法・栽培の実務は完全にゼロ。さらに「この法人が畑を耕しているか」自体が登記から確定しない** |
| **Winemaking** | 🔴 **None** | **一次資料ゼロ。**appellation 規定（木片禁止・灌漑禁止・補糖上限）しか書けていない |
| **Style** | 🔴 **None（生産者レベル）** | **造り手のテイスティングノートは 1 件も無い。**BIVB のアペラシオン一般記述のみ。**フロアでの前置きを必須にした。**🔴 **ただし Puligny と Meursault で供出温度が違うという実用差は取れた** |
| **Important Cuvées** | 🔴 **High** | 🔴 **OBP 4 本すべてについて、INAO 仕様書 3 本で制度上の実在を確認。**🔴 **とくに行 2 は Blagny 赤専用 / Meursault 白限定という 2 条文の組み合わせで完全に決着した。**行 3 の `La Garenne` ⇄ `Clos de la Garenne` の分離、行 4 の 4 lieudit も確定。⚠️ **どの区画を所有しているかは不明** |
| **Staff Notes** | 🔴 **High** | ⚠️ **14 項目。**🔴 **面積・「ドメーヌ / ネゴシアン」断定・「ポール・ペルノの孫娘」・同姓 7 法人の混同・`La Garenne` ⇄ `Clos de la Garenne`・「ブラニーの白」・「ビオです」・醸造数値・シャルドネ 100%・創業年・空の公式サイト・豪 `apwines.com` ―― 12 の実在する事故経路を塞いだ** |
| **Canonical Conflict** | **High** | **4 件とも canonical を直接パースし、INAO / BIVB と機械照合済み** |
| 🔴 **総合** | **Medium — staff-usable。70% を超える。** | 🔴 **フロアは「誰が・どこで・どのアペラシオンの・どの climat を・なぜその呼び名になるのか」を、一つも嘘を言わずに語れる。**<br>🔴 **とくに $640 のムルソーについては、他のどのドシエよりも深く説明できる（Blagny 赤専用 / Meursault 白限定の二条文）。**<br>**欠けているのは造り手の声（沿革・栽培・醸造・テイスティング）で、これは全部同じ一つの理由 ―― 生産者が何も公表していない ―― から来ている。** |

**reached_70: YES (~74%).**

🔴 **ただし条件付きである。** 必須 7 項目のうち **Identity / Overview / Location / Farming /
Important Cuvées（OBP 連結あり）/ Staff Notes 芯 3 / ⚠️ 言ってはいけないことリスト / Sources / Open Questions**
はすべて満たしている。**満たしていないのは繰延べ可の項目（沿革の細部・醸造の数値・区画ごとの ha）だけである。**
🔴 **そして本ドシエは生産者側が薄い分、⚠️ リストを 14 項目まで厚くし、
appellation 側（INAO 3 文書 + BIVB 2 文書）を通常より深く掘った。**
⚠️ **`Style` と `Winemaking` は生産者レベルで空である点を、Confidence 表で明示的に `None` と宣言している。**

---

## Open Questions

1. 🔴 **canonical の 4 レコードが完全な空殻である（CC-2）。**
   **`match_state = exact` が 4/4、`resolved_to = canonical_release` が 4/4 でありながら、
   `obp_note` も `description` も `grapes` も無い。**
   → 🔴 **「解決済み」の集計指標が、内容の充足を一切測っていない。**
   **`resolved` と `speakable` を分ける指標が要るのではないか。これは本生産者ローカルの問題ではない。**
   **canonical への書き込みは本書では行っていない。CTO 判断。**

2. 🔴 **生産者の声を得る経路が、通常より狭い。**
   **(a) `alvinapernot.com` のドメインは生きており MX も設定されているが、公開された連絡先アドレスが無い**
   （Agence Bio に登録が無いため、Bachelet-Monnot のときのようにメールアドレスを公的登録簿から拾えない）。
   **(b) 輸入元（米国では Bertrand's Wines、他に Skurnik 系列以外の複数）から、
   生産者名義・レターヘッド付きのテクニカルシートを取り寄せる**
   ―― **生産者執筆であることが立証できれば `📄` として使える。**
   **(c) 蔵出しラベルの実物を撮影して記載事項を読む。**
   → 🔴 **(c) が最も確実で、しかも下の 3・5・6 を同時に解決する。**

3. 🔴 **【物理ラベル要確認】行 2 のラベルは `Meursault 1er Cru "La Pièce sous le Bois"` と
   `Meursault 1er Cru "Blagny"` のどちらを名乗っているか。**
   🏛 **INAO / BIVB は両方を正規の名乗りとして認めている。**
   🔍 **OBP メニューは `La Pièce sous le Bois` 側を印字している。**
   → **オンラインのどの公的資料でも決められない。実物でしか確定しない。**

4. **【物理ラベル要確認】`Les Vignes de Mon Père` 2023 の公式な存在確認。**
   ⚠️ **フランスには米国 TTB COLA のような公開ラベル登録簿が無く、
   ブリーフの規定により COLA は米国生産者に限られる。**
   → **ラベル実物（または生産者発行の fiche technique）以外に確認経路が無い。**

5. **【物理ラベル要確認】`Les Folatières` の 4 lieudit
   （`Es Folatières` / `En la Richarde` / `Peux Bois` / `Au Chaniot`）のうち、どこを所有しているか。**
   **同様に `La Pièce sous le Bois` の `(en partie)` のどの部分か。**
   **公的資料には出ない。造り手か輸入元にしか答えられない。**

6. **【物理ラベル要確認】瓶詰め表記（`mis en bouteille au domaine` / `par` / `à`）。**
   🔴 **これは §Farming / §Staff Notes ⚠️ ② に直接効く。**
   🏛 **登記の NAF が `46.90Z`（非特化卸売）である以上、
   「自社元詰め」なのか「ネゴシアンとしての元詰め」なのかは、ラベルの法定表記でしか分からない。**

7. 🔴 **`AP WINES SAS` の旧事業所（2018-10-05〜2021-09-10）はどこにあったか。**
   🏛 **登記は `nombre_etablissements: 2` / `ouverts: 1` としか語らず、
   `matching_etablissements` は空配列で返る。**
   ❓ **創業地が Puligny 以外だった可能性を排除できていない。**

8. **`SC NOYERS BRETS`（SIREN 914446372、NAF 68.20B、2022 年設立、Puligny）の役割。**
   ❓ **`PERNOT, Michel Henri`（1959 年生）が Gérant、Alvina が無限責任社員。**
   **土地保有型の NAF であり、畑を保有する構成と整合するが、登記はそれを述べていない。**
   ⚠️ **フロアで「彼女の畑を持つ会社です」と説明してはならない。**

9. **`Michel Henri Pernot` と Alvina の関係、および `DOMAINE PERNOT PAUL ET SES FILS` との関係。**
   ❓ **登記はどちらも述べていない。キュヴェ名『わが父の畑』は父の存在を示すが、父を特定しない。**
   → **生産者自身の一人称の言明が出るまで、血縁は書かない。**

10. 🔴 **`"Garenne"`（`leprince-garenne-2022`）の冠詞脱落と、
    `Premier Cru` / `1er Cru` の表記ゆれ（CC-4）が canonical 全体で何件あるか未計測。**
    **本ドシエは本生産者の周辺 6 レコードでしか数えていない（意図的に横断走査を行っていない）。**

11. **INAO 仕様書 3 本がいずれも 2010 年の全国異議申立手続版（v2.2）である。**
    ⚠️ **より新しい統合版が官報（`info.agriculture.gouv.fr/boagri/`）側にある可能性がある。**
    **本ドシエの数値（とくに基準収量）は、削除線と太字が本文抽出で区別できず `45 57` と二重に出るため、
    断定を避けた。**🔴 **ただし本ドシエの結論（Blagny 赤専用 / Meursault 白限定 / climat の実在と色）は
    削除線の影響を受けない条文部分から取っている。**
