# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 一部登録済（2 件）**
> 🔴 **本書は昇格前の研究記録であり、canonical を一切変更していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **一次資料で確認**（生産者公式／INAO cahier des charges／フランス国家公的登記／認証機関）
> `📄` 単一の非公式資料のみ（**本書では事実の根拠として一切使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake、または公的オープンデータから機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05
>
> ---
>
> ## 🔴🔴 本ドシエ最大の結論 —— **公式サイトは存在しない**
>
> **`domaineroulot.fr` は実在し、AFNIC（フランス国家ドメイン登記）の WHOIS で
> 保有者コンタクトが `Domaine Guy Roulot` であることを確認した。2004-11-10 登録、
> 有効期限 2027-10-24、レジストラ OVH。つまりドメインは間違いなく本人のものである。**
> 🔴 **しかしそのドメインが返すのは OVH の `Site en construction`（工事中）プレースホルダーだけで、
> 中身は 1 文字も無い。** ✅
> 🔴 **さらに Agence Bio（フランス国家有機登録簿）の当該事業者レコードの `siteWebs` フィールドは
> 空配列 `[]` である。国家登録簿の側にも、この生産者のウェブサイトは登録されていない。** ✅
>
> **他の候補ドメイン（`domaine-roulot.com` / `.fr` / `domaineroulot.com` / `roulot-meursault.com` /
> `domaine-roulot.net` / `roulot-vins.fr` / `guy-roulot.fr` / `domaineguyroulot.fr` /
> `jean-marc-roulot.com`）はいずれも DNS で解決しない。**
> ⚠️ **`roulot.fr` は解決するが `https://www.ip-vs.fr/` へ 301 リダイレクトする無関係のサイトである。**
>
> 🔴 **したがって本ドシエには、生産者自身の言葉が一行も無い。**
> **醸造・スタイル・沿革・畑の面積・樹齢は、公式資料が存在しないため全面的に空白である。**
> **それらを一般的なブルゴーニュ知識で埋めることはしていない。**
>
> ---
>
> ## 🔴 では何が確定したのか —— **国家登記と認証機関に全面的に依拠した**
>
> **公式サイトが無い代わりに、フランス国家の公的登録簿から異例に堅い事実が取れた。**
> **① Agence Bio（国家有機登録簿・API）② Ecocert France 発行の認証証書 PDF 実物
> ③ INSEE/Sirene 企業登記（`recherche-entreprises.api.gouv.fr`）
> ④ INAO『Meursault』cahier des charges ⑤ DGFiP 地籍オープンデータ（Etalab）**
>
> 🔴 **最大の収穫は 2 つ。**
> **(a) `Les Luchets` は プルミエ・クリュではない。** INAO の Meursault 1er Cru 一覧に存在せず、
>     DGFiP 地籍には Meursault（INSEE 21412）の**リュー・ディとして実在する**。**村名格である。**
> **(b) Domaine Roulot は「認証を受けた有機栽培」である。** Ecocert France（`FR-BIO-01`）、
>     **初回コミット 2010-04-15**、証書上 **「Récoltes 2014 et suivantes」**、
>     Agence Bio 上 **`mixité: Non`（有機と慣行の併存なし＝全園有機）**。

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Roulot** |
| **canonical 表記** | 🔍 **`Domaine Roulot`**（canonical レコード 2 件がこの表記） |
| 🔴 **公式表記** | ⚠️ **公式サイトが存在しないため、生産者自身による表記は確認できない。** |
| 🔴 **認証機関の表記** | ✅ **`DOMAINE ROULOT - ROULOT Jean Marc SCEA`**（Ecocert France 発行証書 PDF の I.3 欄・原文ママ） |
| **国家有機登録簿の表記** | ✅ **`DOMAINE ROULOT`** / `denominationCourante: DOMAINE ROULOT - ROULOT Jean Marc`（Agence Bio） |
| 🔴 **法人①（経営体）** | ✅ **`DOMAINE ROULOT`** — SIREN **327945143** / SIRET **32794514300011**。**設立 1983-08-08**。NAF **`01.21Z`（ブドウ栽培）**。法定形態コード **6597**。**Ecocert 証書は `SCEA` と明記**。状態 **A（活動中）** |
| 🔴 **法人②（土地保有体）** | ✅ **`GFA DOMAINE ROULOT`** — SIREN **752507582**。**設立 2012-06-14**。NAF `68.20B`。法定形態コード **6534**（GFA＝Groupement Foncier Agricole）。**同一住所**。状態 **A** |
| 🔴 **登記上の役員（SCEA）** | ✅ **`ROULOT FÉLICIEN GUY`（1996 年生）= Gérant et associé indéfiniment responsable（業務執行社員）**／`ROULOT JEAN-MARC ALAIN`（1955 年生）= 無限責任社員／`ROULOT LÉONCE CYPRIEN`（2008 年生）= 無限責任社員／`ESSID (FALCE) RAPHAËLE`（1976 年生）= 無限責任社員 |
| 🔴 **登記上の役員（GFA）** | ✅ **`ROULOT JEAN-MARC ALAIN` = Gérant**／`JAVOUHEY (ROULOT) MICHELLE HUGUETTE`（1952 年生）= Gérant／`ESSID (FALCE) RAPHAËLE` |
| **所在** | ✅ **`1 rue Charles Giraud, 21190 Meursault, France`**（Ecocert 証書・Agence Bio・Sirene の 3 者が完全一致） |
| **座標** | 🔍 ✅ **lat 46.977024 / long 4.775102**（Sirene）。Agence Bio は 46.976726 / 4.774813 |
| **従業員規模** | ✅ **INSEE 区分コード `11`（2023 年基準）** |
| 🔴 **有機認証** | ✅ **Ecocert France `FR-BIO-01`。`etatCertification: ENGAGEE`。初回コミット `2010-04-15`。停止日・終了日ともに `null`** |
| **Bio 番号** | ✅ **`numeroBio: 108891`**（Agence Bio） |
| 🔴 **販売形態（国家登録簿の申告）** | ✅ **`venteProsGros: true` のみ。** 個人向け販売・小売向け・レストラン向けはいずれも `false` |
| **公式サイト** | 🔴 ✅ **存在しない。** `domaineroulot.fr` は本人保有だが OVH の工事中ページ。Agence Bio の `siteWebs` も `[]` |
| **canonical id** | 🔍 **`roulot-clos-de-boucheres-2022` / `roulot-perrieres` の 2 件のみ** |

⚠️ **`Guy Roulot` と `Jean-Marc Roulot` の関係、当主交代の時期、世代数は、
公式資料が無いため本ドシエでは一切主張しない。**
🔴 **ただし国家登記が示す事実として、SCEA の業務執行社員は 1996 年生まれの `Félicien Guy Roulot` であり、
1955 年生まれの `Jean-Marc Alain Roulot` は SCEA では無限責任社員、GFA では業務執行社員である。**
**これは登記上の記載であって、実務上の役割分担を意味するとは限らない。** → Open Questions 3

---

## Overview

🔴 ⚠️ **この節は、通常なら生産者自身の自己規定で書かれる。本件にはそれが無い。**
**以下はすべてフランス国家の公的登録簿と認証機関の文書から取れた事実だけである。**

✅ **Meursault 村の中心部、`1 rue Charles Giraud` に本拠を置く家族経営のブドウ栽培・醸造事業体。**
**経営体 `DOMAINE ROULOT`（SCEA、1983 年設立）と、土地保有体 `GFA DOMAINE ROULOT`（2012 年設立）の
2 法人構成をとる。両者は同一住所で、役員は Roulot 姓の複数世代で構成されている。** ✅

🔴 ✅ **本ドシエで最も確度の高い事実は、この生産者が「認証を受けた有機栽培」であることである。**
**Ecocert France（管理機関コード `FR-BIO-01`）による欧州規則 `(UE) 2018/848` に基づく認証を保持し、
Agence Bio における最初のコミット日は `2010-04-15`。停止も終了も記録されていない。**
**Agence Bio の `mixité` 欄は `Non` —— すなわち有機と慣行の併存が無く、経営体全体が有機である。** ✅

🔴 ✅ **Ecocert 証書に記載された事業活動は 4 つ —— `Exportation, Préparation, Production, Stockage`
（輸出・醸造/加工・生産・貯蔵）。** すなわち **栽培から醸造・貯蔵・輸出まで自ら行う。**

🔴 ✅ **証書の「製品目録（Répertoire des produits）」は、白ワインだけでなく赤ワインも含む。**
「**Vin rouge (Toutes appellations) Récoltes 2014 et suivantes — Biologique**」
「**Vin blanc (Toutes appellations) Récoltes 2014 et suivantes — Biologique**」
「**Raisin de cuve — Biologique**」
→ 🔴 **したがって「白しか造らない生産者」と言ってはならない。** → §Staff Notes ⚠️ ⑤

🔍 ✅ **国家登録簿の販売申告は `venteProsGros`（業者卸）のみが `true`。**
**個人への直販・小売・飲食店への直販はいずれも `false` と申告されている。**
⚠️ **これは申告上の分類であり、実態の全部を意味するとは限らない。**

🔍 **THÉSEUS における状態は中途半端である。canonical に生産者名 `Domaine Roulot` のレコードは
2 件だけ存在し、OBP 掲載 5 本のうち `producer_state` は全 5 行が `exact`。
しかしキュヴェ照合は 5 本中 1 本しか一致しない。** → §Canonical Conflict

---

## History

🔴 ⚠️ **本ドシエは沿革を持たない。**

**公式サイトが存在せず、生産者が公表した沿革文書が一件も見つからなかったためである。**
**創業年・世代・当主交代の経緯・Guy Roulot と Jean-Marc Roulot の関係は、
一次資料が無いため本書では一切主張しない。**

✅ **国家登記から機械的に読める「日付」だけを、事実として並べる。**
**これは沿革ではなく、法人の登記事象にすぎない。**

| 日付 | 登記事象 ✅ | 出典 |
|---|---|---|
| **1983-08-08** | **経営体 `DOMAINE ROULOT`（SIREN 327945143）設立** | INSEE / Sirene |
| **2004-11-10** | 🔴 **ドメイン `domaineroulot.fr` が `Domaine Guy Roulot` 名義で登録される**（22 年経った現在も中身は無い） | AFNIC WHOIS |
| **2008-01-01** | **本店事業所の活動開始日（`date_debut_activite`）** | INSEE / Sirene |
| **2010-04-15** | 🔴 **有機認証への初回コミット（`datePremierEngagement`）** | Agence Bio |
| **2012-06-14** | **土地保有体 `GFA DOMAINE ROULOT`（SIREN 752507582）設立** | INSEE / Sirene |
| **2014 年収穫〜** | 🔴 **Ecocert 証書の製品目録が「Récoltes 2014 et suivantes」を有機として明示** | Ecocert 証書 PDF |
| **2022-11-03 〜 2024-03-31** | **本調査で実物を取得できた Ecocert 証書の有効期間** | Ecocert 証書 PDF |

⚠️ **上表を「沿革」として客に語ってはならない。登記日は創業年でも当主交代年でもない。**
→ §Staff Notes ⚠️ ①

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Bourgogne**（Burgundy） ✅ |
| **Commune** | ✅ **Meursault（Côte-d'Or 21）。INSEE コミューン番号 `21412`** |
| **住所** | ✅ **`1 rue Charles Giraud, 21190 Meursault`**（Ecocert / Agence Bio / Sirene の 3 者一致） |
| **座標** | 🔍 ✅ **46.977024 N, 4.775102 E** |
| **畑の所在** | ❓ **不明。所有区画のリスト・面積・リュー・ディ名を示す一次資料は存在しない** |

### 🔴 ✅ 付加価値の産地情報 —— **appellation レベルの公的事実**

⚠️ **以下は AOC『Meursault』全体に対する INAO の規定であり、Domaine Roulot 固有の情報ではない。**
**この区別は絶対に崩さないこと。**

✅ **INAO cahier des charges「Meursault」 Version n° 2.2 du 15/09/2010 より** —
**AOC「Meursault」は 1937 年 7 月 31 日の政令によって初めて認められた**
（「**initialement reconnue par le décret du 31 juillet 1937**」）。
**白・赤の静止ワインに限られる。**

✅ **白の品種は `chardonnay B` と `pinot blanc B`。**
**赤は主要品種 `pinot noir N`、補助品種に `chardonnay B` / `pinot blanc B` / `pinot gris G`。**

✅ **収量（rendement butoir・上限）** —
**AOC「Meursault」白 = 64 hl/ha。climat 名または「premier cru」を伴う白 = 62 hl/ha。**
**赤 = 58 hl/ha。**
⚠️ **基準収量（rendement）の行は PDF 上に旧値と新値が併記された状態で出力される
（白「45 57」・赤「40 50」）ため、本ドシエでは基準収量の数値を主張しない。**
**climat 名／premier cru を伴う場合の基準収量は「白 55 hl/ha・赤 48 hl/ha」と単一の値で読める。**

---

## Farming

🔴 ✅ **本ドシエで唯一、完全に確定している節である。**
**公式サイトが無いにもかかわらず、フランス国家の登録簿と認証機関の証書という
「公式サイトより強い」一次資料が取れたためである。**

### ✅ 有機認証 —— 国家登録簿（Agence Bio）

| 項目 | 値 ✅ |
|---|---|
| 事業者名 | **`DOMAINE ROULOT`**（`DOMAINE ROULOT - ROULOT Jean Marc`） |
| **Bio 番号** | **`108891`** |
| **管理機関** | 🔴 **`Ecocert France`／EU 管理コード `FR-BIO-01`** |
| **認証状態** | 🔴 **`ENGAGEE`（有効）。`dateSuspension: null` / `dateArret: null`** |
| 🔴 **初回コミット日** | 🔴 **`2010-04-15`**（`datePremierEngagement` / `dateEngagement` とも同日） |
| **通知日** | `2010-04-14`（`dateNotification`） |
| 🔴 **`mixité`** | 🔴 **`Non`** —— **有機と慣行の併存が無い。経営体全体が有機である** |
| **活動** | **`Production`（生産）＋ `Préparation`（醸造・加工）** |
| **年鑑上の業種** | **`Viticulture`** |
| **レコード最終更新** | `2025-02-04` |

### ✅ 認証下の生産品目（Agence Bio・管理基準年 **2026**）

| 品目 | 状態 ✅ |
|---|---|
| **Vins de raisin（ブドウ酒）** | 🔴 **`AB`（＝転換期間を終えた有機。転換中 `C1`/`C2`/`C3` ではない）** |
| **Raisin de cuve（醸造用ブドウ）** | 🔴 **`AB`** |
| **Jachère / 休閑・輪作に入る緑地（緩衝帯を含む）** | **`AB`** |
| **Plants（苗木・接ぎ穂等）** | **`AB`** |

🔴 **4 品目すべてが `AB` であり、転換中を示す区分が一つも無い。**

### ✅ Ecocert 発行証書の実物（PDF を取得・保存済み）

| 欄 | 記載 ✅ |
|---|---|
| 根拠法 | 🔴 **「Certificat en vertu de l'article 35, paragraphe 1, du règlement (UE) 2018/848」** |
| 文書番号 | **`23/110885/120520231857`** |
| **I.3 事業者** | 🔴 **`DOMAINE ROULOT - ROULOT Jean Marc SCEA` / 1 rue Charles Giraud / 21190 Meursault - France** |
| **I.4 管理機関** | **`ECOCERT FRANCE SAS` / `FR-BIO-01` / Lieudit Lamothe Ouest, 32600 L'Isle Jourdain** |
| **I.5 活動** | 🔴 **`Exportation, Préparation, Production, Stockage`** |
| **I.6 製品カテゴリー** | 🔴 **(A) 未加工の植物および植物産品 —— 「production biologique, **sauf durant la période de conversion**」（＝転換期間中ではない、完全な有機生産）／(F) Vin —— 「production de produits biologiques」** |
| **II.1 製品目録** | 🔴 **`Vin rouge (Toutes appellations) Récoltes 2014 et suivantes` = Biologique ／ `Vin blanc` = Biologique ／ `Vin blanc (Toutes appellations) Récoltes 2014 et suivantes` = Biologique ／ `Raisin de cuve` = Biologique** |
| **I.7 発行** | **2023-05-12、l'Isle Jourdain。署名: 総裁 `Thierry Stoedzel`** |
| **I.8 有効期間** | ⚠️ **2022-11-03 〜 2024-03-31** |

⚠️ **本調査で取得できた証書は有効期間が 2024-03-31 までのものである
（Ecocert のダウンロード API は 2023-05-12 公開版のみ 200 を返し、より新しい日付は 404 だった）。**
🔴 **ただし Agence Bio 側は認証状態を `ENGAGEE`、管理基準年 `2026` の全品目を `AB` として保持しており、
停止日・終了日はいずれも `null` である。したがって認証は現在も有効と読める。**
→ Open Questions 4

### 🔴 ⚠️ ビオディナミについて —— **沈黙**

⚠️ **`Demeter` および `Biodyvin` の認証を Domaine Roulot が保持することを示す一次資料は、
本調査では一件も見つからなかった。**
🔴 **Agence Bio のレコードに記載された管理機関は `Ecocert France` の 1 件のみであり、
Ecocert 証書に現れる規格も `(UE) 2018/848`（有機）だけである。ビオディナミ規格の記載は無い。**
→ 🔴 **したがって「ビオディナミです」と言ってはならない。** → §Staff Notes ⚠️ ④

### ❓ 公的資料が沈黙している栽培項目

❓ **自社畑の総面積・区画ごとの面積・樹齢・植密度・仕立て・馬耕の有無・収穫方法・収量の実績値。**
**これらを示す一次資料は存在しない。本ドシエでは一切主張しない。**

⚠️ **INAO cahier des charges には「palissage された葉層の高さは最低 1.50 m」等の
栽培規定があるが、これは AOC Meursault を名乗る全生産者に課される最低基準であって、
Domaine Roulot が何をしているかの説明ではない。**

---

## Winemaking

🔴 ⚠️ **本ドシエは醸造について一件も確定できなかった。**

**理由は明快である —— 公式サイトが存在せず、生産者が公表した醸造記述が一件も無いからである。**

⚠️ **以下はすべて「公的資料が沈黙している」項目である。**
❓ **圧搾・デブルバージュ・発酵温度・酵母・樽の種類とサイズ・新樽比率・バトナージュの有無と頻度・
シュール・リーの期間・熟成期間・マロラクティック発酵の扱い・SO₂ 量・清澄と濾過・
硫黄添加のタイミング・ボトリング時期。**

🔴 **これらについて、一般的なブルゴーニュの慣行や他の Meursault 生産者の手法を援用して
埋めることはしていない。** → §Staff Notes ⚠️ ⑥

✅ **醸造について公的資料から言える唯一のことは、Ecocert 証書の I.5 欄が
`Préparation`（醸造・加工）と `Stockage`（貯蔵）を事業活動に含めていること、
すなわち自社で醸造・熟成していること、そしてそれが有機ワインとして認証されていることだけである。**

⚠️ **AOC Meursault の cahier des charges には醸造に関する appellation レベルの規定があるが、
それは全生産者への最低基準であって Domaine Roulot の手法ではない。混同しないこと。**

---

## Style

🔴 ⚠️ **本ドシエはテイスティングノートを持たない。**

**生産者による公式のテイスティングノートが存在しない（サイトが無い）。**
**輸入元・小売店・評論家によるノートは本調査規約により事実の根拠として使用できない。**

❓ **香り・味わい・骨格・熟成能力・飲み頃について、本ドシエは何も主張しない。**

🔴 ⚠️ **これは §Staff Notes において最も危険な空白である。**
**スタッフは Domaine Roulot のワインの味を、本ドシエを根拠に語ることが一切できない。**
→ §Staff Notes ⚠️ ⑦、および **reached_70: NO** の主因

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本。全行 `producer_state = exact`**）

**セクションはすべて `FRANCE | WHITE > BURGUNDY`。**

| # | OBP 印字 | VT | 価格 | canonical 照合 🔍 | ✅ **appellation レベルで確定したこと** |
|---|---|---|---|---|---|
| 1 | **`Meursault`**（リュー・ディ表記なし） | 2018 | $1,280 | 🔴 **unresolved** —— canonical に `meursault` に当たるキュヴェが無い | ✅ **村名 AOC「Meursault」白。品種は `chardonnay B` および `pinot blanc B` に限られる（INAO）** |
| 2 | **`'Les Luchets,' Meursault`** | 2019 | $1,580 | 🔴 **unresolved** —— `Les Luchets` は canonical に存在しない | 🔴 ✅ **`Les Luchets` は プルミエ・クリュではない。村名格のリュー・ディである。** 下記 ★ 参照 |
| 3 | **`'Clos de Bouchères,' Meursault Premier Cru`** | 2022 | $2,000 | ✅ **exact**（`roulot-clos-de-boucheres-2022`） | ⚠️ **INAO の 1er Cru 名は `Les Bouchères`。`Clos de/des Bouchères` は cahier des charges に存在しない。** 下記 ★★ 参照 |
| 4 | **`'Clos de Bouchères,' Meursault Premier Cru`** | 2019 | $1,980 | 🔴 **unresolved** —— canonical に 2019 が無い | 同上 |
| 5 | **`'Clos de Bouchères,' Meursault Premier Cru`** | 2018 | $2,480 | 🔴 **unresolved** —— canonical に 2018 が無い | 同上 |

🔴 **5 本中、canonical と一致するのは 1 本だけである（#3）。**
🔴 **一方 canonical には OBP に無い `"Les Perrières"` が 1 件ある。** → §Canonical Conflict

---

### ★ 🔴 `Les Luchets` —— **プルミエ・クリュではない。二重に証明した。**

**① INAO による否定的証明** ✅
**cahier des charges「Meursault」 v2.2 (15/09/2010) の
「La liste des climats classés en « premier cru »」の表を全文走査した。
`Luchet` という文字列は、この cahier des charges のどこにも一度も現れない。**
🔴 **したがって `Les Luchets` は Meursault のプルミエ・クリュ climat ではない。**

**② DGFiP 地籍による肯定的証明** ✅
**フランス国家地籍オープンデータ（Etalab / DGFiP、コミューン `21412` Meursault）の
リュー・ディ層に `LES LUCHETS` が実在する。**
**当該コミューンには 165 の固有リュー・ディがあり、`LES LUCHETS` はその一つである。**
🔍 **地籍区画層と幾何的に突き合わせたところ、`LES LUCHETS` は
`AL` 区画 3・4・5・6・8・13・14・15・16・118・119・120・121・122・155・216・217・218・219
の 19 筆から成る**（区画重心による点内包判定。**本判定は THÉSEUS 側の機械的導出であり、
INAO の公式区画図そのものではない**）。

**③ 村名格で climat 名を名乗る法的根拠** ✅
**cahier des charges 第 XII 章 2° は次のように定める** ——
**「プルミエ・クリュに格付けされていない区画から得られたワインについては、
下表に掲げる区画、およびプルミエ・クリュに格付けされた climat と同一の名称については、
climat 名の使用が禁止される。」**
🔴 **すなわち、それ以外の村名格区画は climat 名（リュー・ディ名）を名乗ってよい。**
🔍 **同表が `AL` 区画について挙げる禁止番号は 160・162・163・173・181・182・183・184 であり、
上記の `LES LUCHETS` 19 筆はいずれもこれに該当しない。**

🔴 ✅ **さらに印字規則が両者を決定的に分ける** ——
**プルミエ・クリュ由来のワインで climat 名を付す場合、その文字は
「高さ・幅ともに appellation 名の寸法を超えてはならない」。**
🔴 **プルミエ・クリュ以外の区画の場合、climat 名の文字は
「appellation 名の寸法の `半分` を超えてはならない」。**
→ 🔴 **ラベル上で climat 名が AOC 名の半分の大きさなら、それは村名格である。**
**これは floor で使える、appellation レベルの確実な見分け方である。**

---

### ★★ 🔴 `Clos de Bouchères` / `Clos des Bouchères` —— **冠詞は解決していない。escalate する。**

✅ **INAO cahier des charges が定める Meursault プルミエ・クリュ climat の正式名称は
`Les Bouchères` である**（NOM DU CLIMAT = **`Les Bouchères`**、対応 LIEUDIT = `Les Bouchères (en partie)`、
色は **`Rouge ou blanc`**）。

🔴 ✅ **`Clos de Bouchères` も `Clos des Bouchères` も、cahier des charges には存在しない。**
**すなわち、法的に保護された appellation 上の名称は `Meursault Premier Cru Les Bouchères` であり、
`Clos …` は その上に載る clos 名／銘柄名である。**

🔴 ✅ **DGFiP 地籍にも `Clos …Bouchères` という名のリュー・ディは無い。**
**Meursault の地籍リュー・ディに `LES BOUCHERES` は存在するが（`BO` 区画・19 筆）、
`CLOS` を冠したものは `CLOS DE LA BARRE` / `CLOS DE MAZERAY` / `CLOS DES MOUCHES` の 3 つだけで、
Bouchères 系の clos は登録されていない。**
→ 🔴 **つまりこの clos は地籍上の独立したリュー・ディではなく、`Les Bouchères` の内部にある囲い地である。**

🔴 ✅ **比較のための決定的な材料 —— 同じ cahier des charges の中に `Clos des Perrières` がある。**
**Meursault の 1er Cru 一覧には `Clos des Perrières`（対応 LIEUDIT = `Les Perrières Dessous (en partie)`）が
独立した climat として掲げられている。**
🔴 **INAO が Meursault で唯一公認している clos 名は `Clos ` + `des` + 複数形リュー・ディ名 の形をとる。**
⚠️ **ただしこれは類推の材料にすぎず、`Clos des Bouchères` が正しい綴りであることの証明ではない。**

❓ **モノポール（単独所有）かどうか** —— ⚠️ **公的資料は完全に沈黙している。**
**INAO の cahier des charges はモノポールを記載しない。地籍は所有者を公開しない。**
**生産者の公式資料は存在しない。**
🔴 **したがって本ドシエは「モノポールである」とも「モノポールでない」とも主張しない。**
→ Open Questions 1 / §Staff Notes ⚠️ ③

🔴 **canonical `"Clos de Bouchères"`／OBP 印字 `'Clos de Bouchères,'`／INAO `Les Bouchères` の
三者が食い違っている。本書では解決しない。** → §Canonical Conflict `A-1`

---

### 🔴 canonical `"Les Perrières"` について —— **同じ冠詞問題がもう一件ある**

✅ **cahier des charges の 1er Cru 一覧における NOM DU CLIMAT は `Perrières`（冠詞なし）である。**
**対応する LIEUDIT が `Les Perrières Dessus (en partie)` / `Aux Perrières (en partie)` /
`Les Perrières Dessous (en partie)` の 3 つ。**
🔴 **canonical は `"Les Perrières"` と冠詞を付けている。INAO の climat 名にこの冠詞は無い。**
⚠️ **なお `Clos des Perrières` は これとは別の独立した 1er Cru climat である。取り違えないこと。**
→ §Canonical Conflict `A-2`

---

### ✅ 参考: INAO が定める Meursault プルミエ・クリュ climat 全一覧

⚠️ **これは appellation レベルの公的事実であり、Domaine Roulot の所有畑リストではない。**

| NOM DU CLIMAT ✅ | 色 |
|---|---|
| **Les Cras** | Rouge ou blanc |
| **Les Caillerets** | Rouge ou blanc |
| **Les Santenots Blancs** | Blanc |
| **Les Plures** | Blanc |
| **Les Santenots du Milieu** | Blanc |
| **Charmes** | Rouge ou blanc |
| **La Jeunellotte** | Blanc |
| **La Pièce sous le Bois** | Blanc |
| **Sous le Dos d'Ane** | Blanc |
| **Sous Blagny** | Blanc |
| 🔴 **Perrières**（冠詞なし） | Rouge ou blanc |
| 🔴 **Clos des Perrières** | Rouge ou blanc |
| **Genevrières** | Rouge ou blanc |
| **Porusot** | Rouge ou blanc |
| **Le Porusot** | Rouge ou blanc |
| 🔴 **Les Bouchères** ⭐OBP | Rouge ou blanc |
| **Les Gouttes d'Or** | Rouge ou blanc |
| **Les Ravelles** | Blanc |
| **Blagny** | Blanc |

🔴 **`Les Luchets` はこの表に無い。** ✅

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 生産者自身が何も公表していない。だから「造り手はこう言っています」は使えない。**
「**ムルソー村の中心、`1 rue Charles Giraud` にある家族経営の造り手**です。
**この生産者は公式サイトを持っていません。**
ドメイン名自体は 2004 年から `Domaine Guy Roulot` 名義で押さえられていますが、
**中身は今も空のままです。**
ですので、**造り手自身の言葉としてお伝えできることは、私どもには一つもありません。**
その代わり、**フランス国の登録簿で確認できることだけを、確実にお伝えします。**」

**② 確実に言えるのは「認証を受けた有機」であること。ここは非常に強い。**
「**フランス国の有機登録簿（Agence Bio）と、認証機関 Ecocert フランスの証書で確認できます。**
**認証機関コードは `FR-BIO-01`、最初のコミットは 2010 年 4 月 15 日**です。
**証書の製品目録には『2014 年収穫以降』と明記**されています。
**登録簿の『混在（mixité）』欄は『Non』——
つまり有機と慣行を併用しておらず、経営体まるごとが有機**です。
**認証は現在も有効で、停止・終了の記録はありません。**」

**③ 『レ・リュシェ』はプルミエ・クリュではありません。村名格の区画名です。**
「**リストの『レ・リュシェ』は、ムルソーの村名格のリュー・ディ**です。
**INAO のムルソーの原産地呼称明細書（cahier des charges）にあるプルミエ・クリュの一覧に、
この名前は一度も出てきません。**
一方で、**フランス国の地籍にはムルソーのリュー・ディとして実在**します。
**メニューに『プルミエ・クリュ』と書かれていないのは、正しい表記**です。
**ちなみにラベルで見分けられます。**
プルミエ・クリュなら区画名は呼称名と同じ大きさまで許されますが、
**村名格の場合、区画名は呼称名の『半分』を超えてはいけない**と明細書が定めています。」

### 追加で使える一手

- **『クロ・ド・ブシェール』について（$2,000 / $1,980 / $2,480）**:
  「**INAO が定めるムルソーのプルミエ・クリュの正式名は『レ・ブシェール（Les Bouchères）』**です。
  **『クロ』を冠した名前は原産地呼称明細書には載っていません。**
  つまり **法的に保護された呼称は『ムルソー プルミエ・クリュ レ・ブシェール』**で、
  **『クロ…』はその中にある囲い地の名前**、ということになります。
  **地籍にも『クロ…ブシェール』というリュー・ディは登録されていません。**」
- **村名『ムルソー』2018（$1,280）について**:
  「**区画名のない村名格のムルソー**です。
  **INAO の規定では、ムルソーの白はシャルドネとピノ・ブランに限られます。**」
- **ムルソーという呼称そのものについて**:
  「**AOC ムルソーは 1937 年 7 月 31 日の政令で初めて認められた**呼称です。
  **白と赤の両方が認められています**（実際には白で知られていますが）。」
- **赤も造っていることについて**（聞かれた場合のみ）:
  「**認証証書の製品目録には、白ワインだけでなく『Vin rouge（全呼称）2014 年収穫以降』も
  有機として記載**されています。**赤も造っている造り手**です。
  ただし**当店のリストにあるのは白のみ**です。」

### ⚠️ 言ってはいけないこと（**根拠が無い／出典が沈黙している**）

🔴 **本ドシエは情報が薄い。したがってこの一覧が本書で最も重要な成果物である。**

1. 🔴 ⚠️ **創業年・世代数・当主交代の経緯を言わない。**
   **公式資料が存在せず、本調査は沿革を一行も確定できていない。**
   **法人 `DOMAINE ROULOT` の登記設立日 1983-08-08 は creation of a legal entity であって
   創業年ではない。** これを創業年として語ってはならない。
2. 🔴 ⚠️ **『Guy Roulot が…』『Jean-Marc Roulot が…』という物語を語らない。**
   **本ドシエが持つのは国家登記上の役員名・生年・肩書だけである。**
   **人物の経歴・役割・エピソードを裏づける一次資料は一件も無い。**
3. 🔴 ⚠️ **『モノポール』と言わない。**
   **INAO の明細書はモノポールを記載せず、地籍は所有者を公開せず、生産者の公式資料は存在しない。**
   **本調査ではモノポールであることを確認できていない。**
4. 🔴 ⚠️ **『ビオディナミ』と言わない。**
   **確認できているのは `Ecocert France` による欧州有機規則 `(UE) 2018/848` の認証のみ。**
   **`Demeter` / `Biodyvin` の認証を示す資料は一件も見つかっていない。**
   言うなら「**認証を受けた有機栽培**」まで。
5. ⚠️ **『白しか造らない造り手』と言わない。**
   **Ecocert 証書の製品目録に `Vin rouge (Toutes appellations)` が有機として明記されている。**
6. 🔴 ⚠️ **醸造を一切語らない。**
   **樽・新樽比率・バトナージュ・マロラクティック・熟成期間・SO₂・濾過 ——
   これらについて本ドシエは根拠を一つも持たない。**
   **『ブルゴーニュでは普通こうです』で埋めてはならない。**
7. 🔴 ⚠️ **味のノートを、造り手の言葉として語らない。**
   **公式のテイスティングノートは存在しない。**
   **自分で試飲した感想を述べるのは構わないが、それを『造り手によれば』と言ってはならない。**
8. 🔴 ⚠️ **畑の面積・樹齢・区画数・所有クリュの一覧を言わない。**
   **一次資料が一件も無い。数字を出してはならない。**
9. ⚠️ **『レ・リュシェ』をプルミエ・クリュと言わない。**
   **INAO のプルミエ・クリュ一覧に存在しない。村名格のリュー・ディである。**
   **メニューが『Meursault』とだけ書いているのは正しい。**
10. 🔴 ⚠️ **『クロ・ド・ブシェール』か『クロ・デ・ブシェール』かを、断定して言い直さない。**
    **canonical と OBP は `Clos de Bouchères`、INAO の climat 名は `Les Bouchères`。**
    **正式な綴りは本調査で確定できていない。**
    言うなら「**プルミエ・クリュ『レ・ブシェール』の中の区画**」と、appellation 名で受ければ安全である。
11. ⚠️ **`Les Perrières` を INAO の正式名として復唱しない。**
    **明細書上の climat 名は `Perrières`（冠詞なし）である。**
    **なお `Clos des Perrières` はこれとは別の独立した 1er Cru である。**
12. ⚠️ **第三者点数・評論家評を言わない。** **本調査ではいかなる点数も取得していない。**
13. 🔴 ⚠️ **輸入元の資料に書かれている内容を、造り手の説明として語らない。**
    **本調査は輸入元（Kermit Lynch）の生産者シートを取得したが、
    三人称で書かれた輸入元自身の販促文書であり、生産者が書いたものではないため、
    事実の根拠として一切採用していない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **本生産者について、**escalate すべき衝突が **4 件** ある。
🔴 **いずれも DO NOT EXECUTE。canonical は読み取りのみで、一切変更していない。**

---

### `S-2`（既存ファミリー） —— canonical キュヴェ名に二重引用符が埋め込まれている

1. **衝突する canonical ID**
   - `roulot-clos-de-boucheres-2022` … `name = "Clos de Bouchères"`（**前後の `"` が値の一部**）
   - `roulot-perrieres` … `name = "Les Perrières"`（**同上**）
2. **なぜ問題か**
   **キュヴェ名の値に引用符そのものが含まれている。**
   **文字列一致による OBP 照合、表示、ソート、URL slug 生成のすべてに影響する。**
   **Batch 5–7 で 9 件見つかっている既知のファミリー `S-2` と完全に同一の形である。**
3. **証拠**
   🔍 canonical レコード 2 件の `name` フィールドの生値。
4. **OBP への影響**
   🔴 **OBP 5 行のうち 3 行が `Clos de Bouchères` を印字するが、
   canonical 側の値が `"Clos de Bouchères"` であるため、素朴な文字列一致は必ず失敗する。**
   **実際に一致しているのは 2022 の 1 行のみで、これは別経路で解決されたと見られる。**
5. **推奨する解決（DO NOT EXECUTE）**
   **`S-2` の一括処理に合流させる。単独で修正しない。**
   **正規化は「値から引用符を剥がす」であり、剥がした後に `A-1`（下記）の冠詞問題が残る。**
   **順序は `S-2` → `A-1` である。逆順にすると冠詞判定が引用符に阻まれる。**
6. **Confidence: High**（機械的に確認できる）

---

### `A-1`（既存の冠詞正規化ファミリー） —— `Clos de Bouchères` / `Clos des Bouchères` / `Les Bouchères`

⚠️ **Batch 4 の `Clos de Roi` / `Clos du Roi`、Batch 6 の Ramonet `Le Montrachet` と同型。
新しい番号は開かない。**

1. **衝突する canonical ID**
   - `roulot-clos-de-boucheres-2022`（`name = "Clos de Bouchères"` / `subregion = Meursault Premier Cru`）
2. **なぜ問題か**
   **三者が食い違っている。**
   - canonical: **`Clos de Bouchères`**
   - OBP メニュー印字: **`'Clos de Bouchères,' Meursault Premier Cru`**
   - 🔴 INAO cahier des charges の 1er Cru climat 名: **`Les Bouchères`（`Clos` も `de/des` も無い）**
   **`de` か `des` かという冠詞差に加えて、そもそも `Clos …` という名称が
   appellation の法的名称ではないという層のずれが重なっている。**
3. **証拠**
   ✅ INAO『Meursault』cahier des charges v2.2 (15/09/2010) の 1er Cru 一覧 = **`Les Bouchères`**。
   ✅ 同一覧に **`Clos des Perrières`** が独立 climat として存在する（**`des` を使う形が Meursault に前例あり**）。
   ✅ DGFiP 地籍（21412）のリュー・ディ層に **`LES BOUCHERES` は存在するが `CLOS …BOUCHERES` は存在しない**
   （同層には `CLOS DE LA BARRE` / `CLOS DE MAZERAY` / `CLOS DES MOUCHES` が別途存在するので、
   clos 名が地籍に載る場合は載る、という対照が取れている）。
   ⚠️ **生産者の公式資料が存在しないため、生産者自身がどう綴るかは確認できていない。**
4. **OBP への影響**
   🔴 **OBP 3 行（2022 / 2019 / 2018、計 $6,460）がこのキュヴェ名に依存する。**
   **綴りを誤って正規化すると 3 行すべてが誤った canonical に固定される。**
   **さらに `Les Bouchères` に丸めてしまうと、同じ 1er Cru の他生産者のワインと区別できなくなる。**
5. **推奨する解決（DO NOT EXECUTE）**
   🔴 **`A-1` の一括方針の決定を待つこと。単独で `de` → `des` に書き換えてはならない。**
   **設計上の示唆としては、`appellation_climat`（＝ INAO の法的名称 `Les Bouchères`）と
   `clos_name`（＝ `Clos de/des Bouchères`）を別フィールドで持てば、この衝突は構造的に消える。**
   **これは設計判断であり、本書では実行していない。**
   🔴 **綴りの確定にはラベル実物か生産者からの直接確認が要る。** → Open Questions 1
6. **Confidence: Medium-High**
   （**INAO 名が `Les Bouchères` であることは High。`de` / `des` のどちらが生産者の綴りかは未確定。**）

---

### `A-2`（同じ冠詞正規化ファミリー） —— canonical `Les Perrières` vs INAO `Perrières`

1. **衝突する canonical ID**
   - `roulot-perrieres`（`name = "Les Perrières"` / `subregion = Meursault Premier Cru`）
2. **なぜ問題か**
   ✅ **INAO cahier des charges の NOM DU CLIMAT は `Perrières`（冠詞なし）である。**
   **canonical は `Les` を付与している。`A-1` と同じ冠詞正規化の問題である。**
   ⚠️ **さらに危険なのは、Meursault には `Perrières` と `Clos des Perrières` という
   2 つの別個の 1er Cru climat が存在することである。**
   **冠詞を機械的に付け外しする正規化を入れると、この 2 つが衝突しうる。**
3. **証拠**
   ✅ cahier des charges 1er Cru 表: NOM DU CLIMAT = **`Perrières`**（LIEUDIT = `Les Perrières Dessus (en partie)` / `Aux Perrières (en partie)` / `Les Perrières Dessous (en partie)`）。
   ✅ 同表に別行で NOM DU CLIMAT = **`Clos des Perrières`**（LIEUDIT = `Les Perrières Dessous (en partie)`）。
4. **OBP への影響**
   🔍 **直接の影響は無い。OBP に Roulot の Perrières は 1 本も無い。**
   🔴 **ただし `roulot-perrieres` は OBP に対応行を持たない canonical レコードである
   （＝ 在庫に無いワインが canonical に登録されている）。**
   **`A-1` の一括正規化を Meursault 全体に流す際、このレコードが巻き込まれる。**
5. **推奨する解決（DO NOT EXECUTE）**
   **`A-1` と同一バッチで扱う。**
   **冠詞の付け外しを一律ルールにしないこと —— Meursault の 1er Cru 名は
   `Les Bouchères`（冠詞あり）と `Perrières`（冠詞なし）が同一表内に共存しており、
   INAO 自身が一貫していない。ルールではなく INAO 一覧への突き合わせで解くべきである。**
6. **Confidence: High**（INAO 一覧を直接確認済み）

---

### `V-新`（**新しい形。番号は提案のみ。開いていない。**） —— vintage フィールドに年でない値

1. **衝突する canonical ID**
   - `roulot-perrieres` … 🔴 **`vintage = '—'`（EM DASH `U+2014`。年ではない）**
2. **なぜ問題か**
   🔴 **`vintage` は年を保持するフィールドであるにもかかわらず、値が全角ダッシュ 1 文字である。**
   **数値変換・年による絞り込み・ヴィンテージ順ソート・OBP の年一致照合のすべてが破綻する。**
   **`NULL` でも空文字でもなく、「不明」を表す**字形**が値として入っている点が本質的な問題である。**
3. **証拠**
   🔍 canonical レコード `roulot-perrieres` の `vintage` フィールドの生値 = `—`。
4. 🔴 **既知ファミリーとの照合結果 —— どれとも形が違う。**
   - **`V-1` / `V-4`（release-identifier-in-vintage）とは異なる。** これらは `vintage` に
     リリース識別子（`P2` 等）という**意味のある文字列**が入る事例である。
     `—` は識別子ではなく **null の代替字形（sentinel）** であり、意味を持たない。
   - **`V-3`（層のずれ）とも異なる。** `V-3` は同一年に複数のリリース層が存在するために
     `cuvée × vintage` が一意にならない問題であり、値の型の問題ではない。
   - **`S-2` とも異なる。** `S-2` は `name` フィールドの引用符混入であり、対象フィールドが違う。
   🔴 **したがってこれは `vintage` フィールドへの非年 sentinel 混入という新しい形である。**
   🔍 **ただし新番号の採番は CTO / Akio の権限であり、本書では番号を確定していない。**
   **他の producer dossier に同型が無いかの横断走査が先に要る。** → Open Questions 5
5. **OBP への影響**
   🔍 **直接の影響は無い**（OBP に Roulot の Perrières 行が無い）。
   🔴 **ただし潜在的な影響は大きい。**
   **`Clos de Bouchères` の 2019 / 2018 が `unresolved` である理由は
   「canonical に 2022 しか無い」ことにある。**
   **もし将来ヴィンテージ非依存のレコードを `—` で表現する運用が広がると、
   `vintage` による照合そのものが機能しなくなる。**
   **`roulot-perrieres` はその運用が既に発生している実例である。**
6. **Confidence: High**（値そのものを確認済み）／**分類の Confidence: Medium**（新規性は横断走査で要確認）

---

### 🔍 参考: 衝突ではないが unresolved な OBP 行（**canonical にレコードが無いだけ**）

| OBP 行 | 状態 | 機械的な理由 |
|---|---|---|
| `Meursault` 2018 | unresolved | 🔍 **canonical に村名 Meursault のキュヴェが 1 件も無い**（存在するのは 1er Cru 2 件のみ） |
| `'Les Luchets,' Meursault` 2019 | unresolved | 🔍 **`Les Luchets` は canonical に存在しない。** ✅ **INAO / 地籍では実在が確認できている**ので、登録可能な実体である |
| `'Clos de Bouchères'` 2019 | unresolved | 🔍 **canonical に 2019 のヴィンテージレコードが無い**（2022 のみ） |
| `'Clos de Bouchères'` 2018 | unresolved | 🔍 **同上** |

🔴 **これらは「衝突」ではなく「不在」である。**
**したがって conflict としては起票しない。canonical への追加可否は Akio / CTO の判断。**
→ Open Questions 2

---

## Sources

### 🔴 サイト真正性の事前確認 —— **実施結果**

| 候補 | 判定 | **どう検証したか** |
|---|---|---|
| 🔴 **`www.domaineroulot.fr`** | ⚠️ **本人保有だが中身なし。事実源として使用不可。** | **(b)+(c) 公的登記との突合で検証。** **AFNIC（フランス国家ドメイン登記）の WHOIS で `holder-c: DGR64-FRNIC` → コンタクト名 `Domaine Guy Roulot` を確認。** 登録 2004-11-10、失効 2027-10-24、レジストラ OVH、status ACTIVE。**ドメインは真正に本人のものである。** 🔴 **しかし HTTP 200 で返るのは `<title>Site en construction</title>`、`<meta name="Author" content="OVHcloud">`、リンク先はすべて `ovhcloud.com` / `docs.ovh.com` という OVH の工事中プレースホルダーであり、生産者の記述が 1 文字も無い。** → `NOT_THE_PRODUCER_domaineroulot.fr_OVH_parked.html` として保存し、**事実の根拠として一切使用していない。** |
| ⚠️ **`roulot.fr`** | 🔴 **別人のサイト。使用せず。** | **HTTP で `301 Moved Permanently` → `https://www.ip-vs.fr/`。`X-Redirect-By: WordPress`。Roulot 家とは無関係。** |
| **`domaine-roulot.com` / `domaine-roulot.fr` / `domaineroulot.com` / `domaine-roulot.net` / `roulot-meursault.com` / `roulot-vins.fr` / `guy-roulot.fr` / `domaineguyroulot.fr` / `jean-marc-roulot.com`** | **存在しない** | **すべて DNS で解決しない（`dig +short` が空）。** |
| 🔴 **Agence Bio レコードの `siteWebs`** | **空配列 `[]`** | **国家有機登録簿の側にも、この事業者のウェブサイトは登録されていない。** |

🔴 ✅ **結論: Domaine Roulot に公式ウェブサイトは存在しない。**
**これは「見つけられなかった」ではなく、
「本人保有ドメインが空である」＋「国家登録簿にも未登録である」という積極的な確認である。**

🔴 **したがって本ドシエは、指示された fallback ルート
（Agence Bio → 認証機関 → INAO cahier des charges）を全面的に採用した。**

---

### 一次資料（**実際に取得し、`_sources/domaine-roulot/` に保存したもの**）

| 資料 | 種別 | 取得した情報 |
|---|---|---|
| 🔴 **Agence Bio 公開 API** `opendata.agencebio.org/api/gouv/operateurs/?nom=roulot` → `agencebio_roulot.json` | **フランス国家有機登録簿** | 🔴 **`DOMAINE ROULOT` / Bio 番号 108891 / SIRET 32794514300011 / NAF 01.21Z / 住所 / 座標 / Ecocert France `FR-BIO-01` / `etatCertification: ENGAGEE` / `datePremierEngagement: 2010-04-15` / `dateSuspension: null` / `dateArret: null` / `mixité: Non` / 4 品目すべて `AB`（基準年 2026）/ 活動 Production+Préparation / `annuaireActivites: Viticulture` / `venteProsGros: true` のみ / `siteWebs: []` / `dateMaj: 2025-02-04`** |
| 🔴 **Ecocert 証書ページ** `certificat.ecocert.com/entreprise/724653C2-…` → `ecocert_roulot.html` | **認証機関** | **`DOMAINE ROULOT - ROULOT Jean Marc` / 住所 / 活動「Agriculteur (production végétale), Fabricant & Transformateur」/ 規格「Agriculture biologique Europe (EU) 2018/848 [FR]」/ 製品カテゴリー「Boissons alcoolisées」「Fruits, noix, légumes et dérivés」「Plantes & Dérivés」「Surface de biodiversité」** |
| 🔴 **Ecocert 証書 PDF 実物** `certificat.ecocert.com/fr/certificate/724653C2-…/09A4271F-…/fr/2023-05-12` → `ecocert_cert_roulot.pdf` | **認証機関発行の法定文書** | 🔴 **文書番号 23/110885/120520231857 / I.3 `DOMAINE ROULOT - ROULOT Jean Marc SCEA` / I.4 ECOCERT FRANCE SAS `FR-BIO-01` / I.5 `Exportation, Préparation, Production, Stockage` / I.6 (A)「sauf durant la période de conversion」+(F) Vin / II.1 製品目録（Vin rouge・Vin blanc「Récoltes 2014 et suivantes」・Raisin de cuve、すべて Biologique）/ I.7 2023-05-12 署名 Thierry Stoedzel / I.8 有効 2022-11-03〜2024-03-31** |
| 🔴 **INSEE / Sirene** `recherche-entreprises.api.gouv.fr` → `annuaire_scea_roulot.json` / `annuaire_gfa_roulot.json` | **フランス国家企業登記** | 🔴 **`DOMAINE ROULOT` SIREN 327945143・設立 1983-08-08・NJ 6597・NAF 01.21Z・état A・効数区分 11(2023)・役員 4 名（生年つき）／`GFA DOMAINE ROULOT` SIREN 752507582・設立 2012-06-14・NJ 6534・NAF 68.20B・役員 3 名／両者同一住所／`est_bio: true`** |
| 🔴 **INAO cahier des charges「Meursault」 v2.2 du 15/09/2010** → `cdc_meursault.pdf` / `cdc_meursault.txt` | **原産地呼称明細書（appellation レベル）** | 🔴 **1937-07-31 政令 / 品種（白 chardonnay B・pinot blanc B）/ プルミエ・クリュ climat 全一覧（`Les Bouchères`・`Perrières`・`Clos des Perrières` を含む）/ `Luchet` は全文に一度も現れない / 第 XII 章の表示・ラベル規則（1er Cru は同寸法まで、村名格は半分まで）/ 村名格での climat 名使用の禁止区画表 / rendement butoir（白 64・climat 付き白 62・赤 58）** |
| 🔴 **DGFiP 地籍オープンデータ（Etalab）** `cadastre.data.gouv.fr/.../21/21412/cadastre-21412-lieux_dits.json.gz` → `cadastre_21412_lieux_dits.json` | **フランス国家地籍** | 🔴 **Meursault の全リュー・ディ 165 件。`LES LUCHETS` の実在を確認。`LES BOUCHERES` の実在を確認。`CLOS DE LA BARRE`/`CLOS DE MAZERAY`/`CLOS DES MOUCHES` は存在するが `CLOS …BOUCHERES` は存在しない** |
| **DGFiP 地籍 区画層** `cadastre-21412-parcelles.json.gz` → `parcelles.json` | **フランス国家地籍** | 🔍 **`LES LUCHETS` = `AL` 区画 19 筆（3,4,5,6,8,13,14,15,16,118,119,120,121,122,155,216,217,218,219）。`LES BOUCHERES` = `BO` 区画 19 筆。**（区画重心の点内包判定による **THÉSEUS 側の機械的導出**） |
| 🔴 **AFNIC WHOIS** `whois domaineroulot.fr` → `whois_domaineroulot.fr.txt` | **フランス国家ドメイン登記** | 🔴 **holder コンタクト `Domaine Guy Roulot` / 登録 2004-11-10 / 失効 2027-10-24 / registrar OVH / status ACTIVE** |

### 🔴 取得したが **事実の根拠として採用しなかった** もの

| 資料 | 理由 |
|---|---|
| 🔴 **`IMPORTER_kermitlynch_domaine-roulot.pdf`**（`kermitlynch.com/files/domaine-roulot.pdf`） | 🔴 **輸入元 Kermit Lynch 自身が作成した販促用生産者シートである。** **全文が三人称の紹介文で、生産者の署名も「notes from the domaine」の表記も無く、フッターは `www.kermitlynch.com` / `info@kermitlynch.com`。** **生産者が書いた技術資料であることを示せなかったため、本調査規約により事実の根拠として一切使用していない。** ⚠️ **同シートには畑の面積・樹齢・沿革が記載されているが、本ドシエはそれを一切採用していない。** |
| 🔴 **`NOT_THE_PRODUCER_domaineroulot.fr_OVH_parked.html`** | **OVH の工事中プレースホルダー。生産者の記述が 1 文字も無い。** |
| ⚠️ **各種小売店・評論サイト・Wikipedia** | **本調査規約により全面禁止。参照していない。** |

### 取得できなかったもの / 存在しなかったもの

- 🔴 **生産者の公式サイト —— 存在しない。**（上記の真正性確認の通り）
- 🔴 **生産者による醸造記述・テイスティングノート・沿革 —— 一件も存在しない。**
- 🔴 **自社畑の面積・区画・樹齢・所有クリュ —— 一次資料が無い。**
- ⚠️ **`Clos de Bouchères` の正式な綴りと、モノポールか否か —— 公的資料が沈黙している。**
- ⚠️ **有効期限内（2024-04-01 以降）の Ecocert 証書 PDF。**
  **ダウンロード API は 2023-05-12 公開版のみ 200 を返し、他の `dataset_id` / 新しい日付はすべて 404 だった。**
  **ただし Agence Bio が基準年 2026 で `AB` を保持しているため、認証の現行性は別経路で確認できている。**
- ⚠️ **INPI（商標登記）は `HTTP 403` で拒否された。**
  **`Clos des Bouchères` が商標登録されているかを確認できていない。** → Open Questions 1

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical レコード 2 件** —— `roulot-clos-de-boucheres-2022`（`"Clos de Bouchères"` / 2022 /
Meursault Premier Cru / Blanc / grapes=None）、`roulot-perrieres`（`"Les Perrières"` / **`—`** /
Meursault Premier Cru / Blanc / grapes=None）。
🔍 **OBP 掲載 5 本**（全行 `producer_state = exact`、セクションは全て `FRANCE | WHITE > BURGUNDY`。
**キュヴェ照合は 5 本中 1 本のみ `exact`、4 本が `unresolved`**）。
🔍 **両 canonical レコードとも `grapes = None`。** ✅ **INAO は Meursault 白を
`chardonnay B` / `pinot blanc B` に限定しているので、appellation レベルの制約は分かっている。**
⚠️ **ただし当該キュヴェの実際の品種構成を示す一次資料は無いため、canonical への品種入力は本書では推奨しない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | **国家企業登記・国家有機登録簿・認証機関証書の 3 者が住所と事業者名で完全一致。法人 2 体制・設立日・役員名と生年・SCEA という法定形態まで一次で取れた。**⚠️ 公式表記だけが不明 |
| **Overview** | ⚠️ **Medium-Low** | 🔴 **生産者の自己規定が一行も無い。**登記と認証から書けることは書いたが、**造り手が何を目指しているかは完全な空白** |
| **History** | 🔴 **None** | 🔴 **沿革は一件も確定していない。**表にあるのは登記事象の日付だけで、**創業年も世代も当主交代も不明** |
| **Location** | **Medium-High** | **住所・コミューン・座標は 3 者一致で確定。**appellation レベルの産地規定も INAO から確定。🔴 **ただし所有畑の所在は完全に不明** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **本ドシエで最も強い節。**国家登録簿＋認証機関証書実物で、**認証機関・EU 規格・初回コミット日 2010-04-15・`mixité: Non`・全品目 `AB`・「Récoltes 2014 et suivantes」**まで確定。⚠️ **面積・樹齢・具体的な栽培作業は不明** |
| 🔴 **Winemaking** | 🔴 **None** | 🔴 **一件も確定していない。**言えるのは Ecocert 証書が `Préparation`/`Stockage` を活動に含むことだけ |
| 🔴 **Style** | 🔴 **None** | 🔴 **公式テイスティングノートが存在しない。**本ドシエは味について何も言えない |
| **Important Cuvées** | ⚠️ **Medium** | 🔴 **`Les Luchets` が村名格リュー・ディであることを INAO（否定）と地籍（肯定）の二重で確定。`Les Bouchères` が 1er Cru 正式名であることも確定。**⚠️ **しかし Roulot 自身のキュヴェ一覧は不明で、`Clos de/des` の綴りとモノポール性は未解決。OBP 5 本中 4 本が unresolved のまま** |
| **Staff Notes** | 🔴 **High** | ⚠️ **13 項目。**🔴 **「創業年」「人物の物語」「モノポール」「ビオディナミ」「白専業」「醸造」「味のノート」「畑の数字」という 8 つの、この生産者で最も踏みやすい誤りを塞いだ** |
| **Canonical Conflict** | **High** | 🔴 **`S-2` 2 件・`A-1`・`A-2`・`V-新` を根拠つきで起票。既知ファミリーには番号を新設していない** |
| 🔴 **総合** | 🔴 **Low-Medium —— staff-usable ではない。約 60%。** | **必須項目そのものは全て埋まっている（Identity / Overview / Location / **Farming** / Important Cuvées の OBP 連結 / Staff Notes 芯 3 点 / Must-Not-Say）。**🔴 **しかし History・Winemaking・Style が三つとも完全な空白であり、生産者自身の言葉が一行も無い。**🔴 **スタッフは「誰が・どこで・有機であること・レ・リュシェが村名格であること」しか語れず、$1,280〜$2,480 のワインについて味も造りも一切語れない。**🔴 **公式サイトが存在しないため、この空白は追加調査では埋まらない。team からの資料提供が要る。** |

🔴 **reached_70: NO（約 60%）。**

🔴 **ブロッカー（正確に）:**
**Domaine Roulot には公式ウェブサイトが存在しない
（本人保有ドメイン `domaineroulot.fr` は OVH の工事中ページで中身が無く、
Agence Bio の `siteWebs` も空。他の候補ドメインはすべて DNS 不通）。
そのため生産者が公表した醸造記述・テイスティングノート・沿革・畑の面積が
一件も存在せず、`## History` / `## Winemaking` / `## Style` の 3 節が
公的資料の代替では原理的に埋められない。**
**Agence Bio・Ecocert・INSEE/Sirene・INAO・DGFiP 地籍という
利用可能な公的経路はすべて使い切っており、追加のウェブ調査では改善しない。**

🔴 **本ドシエのステータス: `awaiting material from the team`.**
**必要なのは、生産者が作成した資料そのものである ——
輸入元経由で入手する「ドメーヌ作成の technical sheet（生産者の署名または
"notes from the domaine" の明示があるもの）」、
または蔵からの直接回答（キュヴェ一覧・区画面積・醸造・`Clos` の正式綴り・モノポールの可否）。**
⚠️ **輸入元が自ら書いた販促シートでは要件を満たさない。**

---

## Open Questions

1. 🔴 **`Clos de Bouchères` か `Clos des Bouchères` か。そしてモノポールか否か。**
   ✅ **INAO の 1er Cru 正式名は `Les Bouchères` で、`Clos …` 形は cahier des charges に無い。**
   ✅ **地籍にも `CLOS …BOUCHERES` というリュー・ディは無い（＝ `Les Bouchères` 内の囲い地）。**
   ⚠️ **同じ明細書に `Clos des Perrières` があるので `des` 形は Meursault に前例があるが、
   これは証明ではない。**
   ⚠️ **INPI（商標登記）は `HTTP 403` で拒否され、商標側から確認できなかった。**
   → 🔴 **ラベル実物の確認、または蔵への直接照会が要る。**
   → **§Canonical Conflict `A-1`。本書では解決していない。**

2. 🔴 **canonical に何を追加するか（Akio / CTO 判断）。**
   🔍 **OBP 5 本中 4 本が `unresolved`。内訳は
   ① 村名 `Meursault`（canonical に村名キュヴェが 1 件も無い）
   ② `Les Luchets`（canonical に無いが、**INAO と地籍で実在を確定済み**なので登録可能な実体）
   ③④ `Clos de Bouchères` の 2019 / 2018（キュヴェは在るがヴィンテージが無い）。**
   🔴 **`Les Luchets` を登録するなら、`A-1` の冠詞方針を先に決めておかないと
   `Clos de/des Bouchères` と同じ轍を踏む。**
   → **canonical への書き込みは本書では行っていない。**

3. ⚠️ **登記上の役員構成が示唆する当主交代を、どう扱うか。**
   ✅ **SCEA `DOMAINE ROULOT` の `Gérant` は 1996 年生まれの `ROULOT FÉLICIEN GUY` であり、
   1955 年生まれの `ROULOT JEAN-MARC ALAIN` は SCEA では無限責任社員、
   GFA `DOMAINE ROULOT` では `Gérant` である。**
   ⚠️ **これは登記上の記載にすぎず、実務上の役割・世代交代の有無・時期を意味しない。**
   🔴 **本ドシエでは一切解釈していない。** → **裏づけには生産者からの確認が要る。**

4. ⚠️ **有効期限内の Ecocert 証書。**
   **取得できたのは有効期間 2022-11-03〜2024-03-31 の版のみ
   （ダウンロード API は 2023-05-12 公開版だけが 200、他の `dataset_id` と新しい日付はすべて 404）。**
   🔴 **Agence Bio が基準年 2026 で全品目 `AB`・`ENGAGEE`・停止/終了 `null` を保持しているため
   認証の現行性そのものは確認できているが、最新証書の実物が手元に無い。**
   → **Ecocert に直接照会すれば取得できる（証書 PDF に「Seule la version électronique …faisant foi」と明記）。**

5. 🔴 **`roulot-perrieres` の `vintage = '—'` は、DB 全体で何件あるのか。**
   🔍 **既知ファミリー `V-1`/`V-4`（release identifier）とも `V-3`（層のずれ）とも
   `S-2`（引用符）とも形が違う、`vintage` フィールドへの非年 sentinel 混入である。**
   🔴 **新番号を採番する前に、canonical 全体を `vintage` が 4 桁数字でないレコードで
   横断走査する必要がある。本書では走査していない（指示範囲外のため）。**
   → **採番は CTO / Akio の権限。**

6. 🔴 **`## Winemaking` と `## Style` を埋める唯一の経路。**
   **公式サイトが無い以上、ウェブ調査では埋まらない。**
   **必要なのは「ドメーヌが作成した technical sheet」（生産者の署名または
   `notes from the domaine` の明示があるもの）か、蔵からの直接回答である。**
   ⚠️ **輸入元が自ら書いた販促シート（本調査で取得した Kermit Lynch のものなど）は要件を満たさない。**

7. ⚠️ **Roulot の村名 `Meursault`（OBP 行 1・2018・$1,280）は、名前のついたブレンドなのか。**
   ⚠️ **公的資料は完全に沈黙している。**
   ✅ **appellation レベルで言えるのは「村名 AOC Meursault の白であり、
   品種は chardonnay B / pinot blanc B に限られる」ことだけである。**
   🔴 **区画名のない村名格ワインは canonical のキュヴェ名としても表現しにくい
   （「キュヴェ名なし」をどう持つかの設計判断が要る）。** → Open Questions 2 と同じ判断に属する。

8. ⚠️ **Roulot は赤も造っている（Ecocert 証書の製品目録に `Vin rouge (Toutes appellations)`）。**
   ❓ **どの appellation の赤かは公的資料から特定できない。**
   🔍 **OBP には Roulot の赤は 1 本も無い。**

9. ⚠️ **`GFA DOMAINE ROULOT`（2012 年設立・NAF 68.20B）が保有する土地の範囲。**
   ❓ **GFA は土地保有体だが、保有区画は公開されていない。**
   **畑の面積・所在を公的に確定する経路は本調査では見つからなかった。**
