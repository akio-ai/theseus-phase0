# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件しか存在しない**（`ridge-monte-bello`）。
> **928 レコードの export 全体を機械走査し、`producer` フィールドが `Ridge Vineyards` であるレコードが
> 1 件であることを実測した。OBP は 3 行。すなわち 3 行中 2 行は canonical の「欠落（gap）」である。**
> 🔒 **gap は conflict ではない（`CDX-23`）。canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式資料で確認**（`www.ridgewine.com` 本体・同ドメイン配信の公式 PDF・公式ボトルショット画像）
> `🏛` **公的登録簿／規制一次資料** —— **27 CFR Part 9 / Part 4（eCFR 現行版）**、
>    **USDA National Organic Program 認証書（認証機関 Organic Certifiers 発行、証書番号 `23-0793`）**
> `📄` **生産者著作だが生産者ドメイン外で配信されている資料**（**本書では 0 件。使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している／第三者の主張であって未確認**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://www.ridgewine.com/`**
> 走査元: **`robots.txt` → `sitemap_index.xml`（15 本の子サイトマップ）**、
> **`page-sitemap.xml`（559 URL）/ `wine-sitemap.xml` + `wine-sitemap2.xml`（合計 1,134 のワイン個別ページ）/
> `vineyard-sitemap.xml`（44 畑）/ `news_item-sitemap.xml`**、および公式サイト内検索（`/?s=`）
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ① —— Ridge は「自社ラベルの文法」を自分で公開している。**
> **`/about/news/a-deep-dive-into-the-ridge-label/` は、フロントラベルを `Top Block` と `Bottom Block` に分解し、
> どの語がどの条件で載るかを造り手自身が逐条で説明した文書である。**
> 🔴 **この 1 頁があるおかげで、本バッチの核心（`Estate` と `Proprietary Blend` はキュヴェ名かカテゴリー語か）は
> 推測ではなく造り手の定義で決着する。** → §Important Cuvées
>
> 🔴 **本ドシエ最大の収穫 ② —— 3 行の判定は「3 行とも同じ」ではない。行ごとに違う。**
> | OBP 行 | 判定 |
> |---|---|
> | **1. `'Estate,' … Cabernet Sauvignon`** | 🔴 **`ESTATE` はフロントラベル Top Block に実在する。カテゴリー語ではない。反復パターン不成立** |
> | **2. `'Monte Bello,' … Cabernet Sauvignon`** | ⚠️ **`Monte Bello` はラベル実在。**🔴 **しかし `Cabernet Sauvignon` は Top Block に無い**（Bottom Block の構成比表示に `86% CABERNET SAUVIGNON` として現れるだけ） |
> | **3. `'Geyserville Vineyard,' … Proprietary Blend`** | 🔴 **`GEYSERVILLE VINEYARD` はラベル実在。しかも造り手が 2024 年から `VINEYARD` を足したばかりで、2024 年ヴィンテージに限って正しい。**⚠️ **`Proprietary Blend` はラベルにも公式サイトにも存在しない語** |
> → 🔴 **つまり「メニューがカテゴリー語をキュヴェ名にした」型（`CDX-15`）は 3 行中 1 行（3 行目の varietal 部分）にしか当たらず、
> しかもその同じ行のキュヴェ名部分は、メニューのほうがヴィンテージ単位で正確である。**
>
> 🔴 **本ドシエ最大の収穫 ③ —— 1 行目には「同一ヴィンテージの取り違え先」が実在する。**
> 🔴 **Ridge は 2023 年に `Estate Cabernet Sauvignon` と `Santa Cruz Mountains Cabernet Sauvignon` の 2 本を並行して出している。**
> **前者は自社栽培（Monte Bello 畑）、後者は 2023 年から復活させた買いブドウのラベルである。**
> **OBP 1 行目の印字 `'Estate,' Santa Cruz Mountains Cabernet Sauvignon` は、この 2 つの製品名を 1 行に含んでいる。**
> → 🔴 **`Estate` の 1 語だけが両者を分ける。ここを落とすと別のワインを語ることになる。** → §Staff Notes ⚠️ ②
>
> 🔴 **本ドシエ最大の収穫 ④ —— 有機認証が「証書そのもの」で確認できた。稀有な事例である。**
> 🏛 **USDA NOP 証書 `23-0793`（`RIDGE VINEYARDS, INC.` 宛、初回発効 `09/03/2011`）と、
> 区画ごとの面積つき対象地一覧 PDF を、生産者自身が自社ドメインで配信している。**
> 🔴 **OBP 3 本のヴィンテージ（2022 / 2023 / 2024）はいずれも、造り手が「自社畑 100% 有機認証」と述べる 2022 年収穫以降にある。**
> → **ただし「organically grown」と「organic wine」は別物である。** → §Farming
>
> ⚠️ **調査上の制約 ① —— 🏛 TTB Public COLA Registry は本調査でも CAPTCHA でゲートされていた。**
> **`publicSearchColasBasic.do` は F5/Shape 系 bot 防御（`bobcmn` / `TSPD_101`）を返し、
> ページ内に `captcha_audio` が実在した。ルールに従い突破は試みていない。**
> **⚠️ ゲートされたことは「ラベルが存在しない」ことの証拠ではない。**
> **代替として、生産者自身が配信するボトルショット画像を実読して label evidence とした。**
> **これは生産者の公表物であって連邦承認記録ではない。両者を混同しない。**
>
> ⚠️ **調査上の制約 ② —— 裏ラベルの画像を 1 枚も取得できていない。**
> 🔴 **Ridge は 2011 年ヴィンテージ以降、全ワインの裏ラベルに成分表を載せる稀有な生産者であり、
> その内容は本来この蔵を語る最大の武器である。造り手は裏ラベルの「文法」を公開しているが、
> 該当 3 ヴィンテージの裏ラベル現物は本調査では読めていない。** → Open Questions 1（実ボトル案件）

---

## Identity

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Ridge`** |
| **Canonical Name** | ✅ **`Ridge Vineyards`** |
| 🔴 **法人名** | ✅ 🏛 🔴 **`RIDGE VINEYARDS, INC.`**<br>✅ **Privacy Policy 冒頭：「This Privacy Policy (“Policy”) describes how **Ridge Vineyards, Inc.** and its affiliate and related entities (collectively, “Ridge Vineyards,” “we,” “us,” or “our”) collects, uses, discloses, and retains personal information about visitors to our website, **www.ridgewine.com** (the “Site”)」**<br>🏛 **USDA NOP 証書の宛名も `RIDGE VINEYARDS, INC.`** |
| 🔴 **ラベル上のブランド名** | ✅ 🔴 **`RIDGE`（単独）。**造り手自身の説明：「**The first element of the Top Block is always the word RIDGE… This use of Ridge also fulfills the TTB requirement for a Brand Name to be present on the front label. Note that the word RIDGE by itself is a trademark of Ridge Vineyards.**」 |
| **Aliases** | 🔍 **`Ridge`**（OBP 印字）／✅ **`RIDGE`**（ラベル・公式表記）／🔍 **`Ridge Vineyards`**（canonical `producer` 値） |
| 🔴 **所在（Monte Bello ワイナリー）** | ✅ **`17100 Montebello Road, Cupertino, CA 95014-5435`／`408.867.3233`／Fax `408.868.1350`**<br>🔴 **同住所が 3 本の OBP 該当ボトルのフロントラベル下部にそのまま印字されている**（`17100 MONTEBELLO ROAD, CUPERTINO, CALIFORNIA 95014`） |
| 🔴 **郵送先（法人）** | ✅ 🏛 🔴 **`P.O. Box 1810, Cupertino, CA 95015`。**<br>**Privacy Policy の Contact Us と、🏛 USDA NOP 証書の宛先が完全に一致する** |
| **他の拠点** | ✅ **Lytton Springs（Healdsburg, Sonoma County）`707.433.7721`／Paso Robles `805.840.2414`** |
| 🔴 **Head Winemaker & CEO** | ✅ 🔴 **`John Olney`。**公式：「**John Olney joined Ridge in 1996 and worked in both the Monte Bello and Lytton Springs wineries before becoming Head Winemaker & COO in 2021 and then CEO in 2026.**」<br>🔴 **OBP 3 本すべてのテイスティングノートの署名 `JO` は彼である** |
| **醸造チーム** | ✅ **Lytton Springs VP of Winemaking `Shauna Rosenblum`／Lytton Springs Assistant Winemaker `Michael Bairdsmith`（2014 年〜）／Monte Bello Assistant Winemaker `Lauren Lyall`（2025 年に Lab Manager から昇格）** |
| 🔴 **Winemaker Emeritus** | ✅ 🔴 **`Paul Draper`。**公式頁の見出しがそのまま「**Paul Draper - Winemaker Emeritus / Joined Ridge in 1969**」。<br>⚠️ **公式頁に「退任年」の記載は無い。**（canonical は「2016年退任」と書くが、造り手の言葉では裏づけが取れなかった） → §Canonical Conflict |
| 🔴 **創業（現体制）** | ✅ 🔴 **1962 年。**公式：「**Ridge Vineyards was founded in 1962 as a partnership by four Stanford Research Institute engineers; Dave Bennion, Hew Crane, Charlie Rosen, and Howard Ziedler.**」<br>⚠️ **畑と蔵の起源は 1885/1886 年に遡る（→ §History）。「創業 1962 年」と「畑 1885 年」を混ぜない** |
| 🔴 **企業グループ** | ✅ 🔴 **`Otsuka Group` に属する。**根拠は**生産者ドメイン上の 2 件**：① `Otsuka Employee Gift` 頁が Otsuka 社員を自社会員として扱い「**As an Otsuka employee, you already have an active account with us**」と書く ② `/policies/business-partner-code-of-ethics/` が **`Otsuka Group Business Partner Code of Ethics`** そのものである<br>⚠️ **出資比率・取得年は公式サイトに書かれていない。本書は主張しない** → Open Questions 6 |
| 🔴 **有機認証** | ✅ 🏛 🔴 **USDA NOP 証書 `23-0793`。初回発効 `09/03/2011`／発行 `09/06/2023`／更新日 `09/03/2024`。**<br>**認証機関 = `Organic Certifiers`（`6500 Casitas Pass Road, Ventura, CA 93001`）、署名者 `Susan D. Siple, Executive Director`。**<br>**Product(s) = `100% Organic Wine Grapes - Ridge Vineyards Inc`／Category = `Crops`** → §Farming |
| **canonical id** | 🔍 🔴 **`ridge-monte-bello` の 1 件のみ**（`producer='Ridge Vineyards'` / `name='Monte Bello'` / `vintage='—'` / `subregion='Santa Cruz Mountains'` / `color='Rouge'` / `classification='Santa Cruz Mountains Bordeaux Blend'`） |

---

## Overview

✅ **カリフォルニア、サンタクルーズ山脈の尾根の上。1962 年に 4 人のスタンフォード研究所のエンジニアが
再興した蔵で、以来「単一畑（single-vineyard）」を一貫して掲げている。**
公式の言葉：「**In 1962, Ridge Vineyards made its first Monte Bello, and two years later its first zinfandel.
Since that time, Ridge has championed single-vineyard winemaking, searching California for those rare and
exceptional vineyards where climate, soil, and variety are ideally matched.**」

🔴 ✅ **蔵の自己規定は 3 つの語に集約される —— `single-vineyard`、`pre-industrial`、`transparency`。**
「**At RIDGE, we call our approach to winemaking “pre-industrial.” We believe that for anyone attempting to
make fine wine, modern additives and industrial processing limit true quality.**」
「**Since the 2011 vintage, Ridge Vineyards has included a list of all ingredients on our back label to
demonstrate how little intervention is necessary to produce fine wine.**」

🔴 ✅ **有機栽培は「言っているだけ」ではなく、証書を自分で公開している。**
「**Ridge Vineyards is one of the largest farmers of organically certified grapes in Sonoma County and
the Santa Cruz Mountains Appellation.**」
🔴 **公式サイトから USDA NOP 認証書 PDF と対象地一覧 PDF が直接ダウンロードできる。** → §Farming

🔴 **OBP 3 行は、この蔵の 3 つの顔をちょうど 1 本ずつ拾っている。**
**Monte Bello（山上の自社畑・ボルドー品種）、Estate Cabernet（同じ畑の別選抜）、
Geyserville（ソノマの 19 世紀の混植畑・ジンファンデル主体）。**

🔍 **THÉSEUS における状態は「3 行に対して 1 レコード」であり、
しかもその 1 レコードは `vintage='—'` の `Monte Bello` 1 本のみ。
`Estate Cabernet Sauvignon` も `Geyserville` も canonical に存在しない。**

---

## History

### Foundation（畑・蔵の起源）

| 年 | 出来事 | 典拠 |
|---|---|---|
| 🔴 **1885** | 🔴 **`Osea Perrone` 医師（サンフランシスコのイタリア人社会の名士）が Monte Bello Ridge 山頂近くの 180 エーカーを購入。斜面を段々畑にし、地元の石灰岩で Monte Bello Winery を建てた。** | ✅ **公式 History：「the history of Ridge Vineyards begins in 1885, when Osea Perrone, a doctor who became a prominent member of San Francisco's Italian community, bought 180 acres near the top of Monte Bello Ridge」** |
| **1886** | **Monte Bello の最初の区画が植えられ、ワイナリー建設が始まる。** | ✅ **2022 Monte Bello 公式 History 欄** |
| **1892** | 🔴 **Monte Bello 名義の最初のヴィンテージ。** | ✅ **公式：「producing the first vintage under that name in 1892」。**🔴 **この 1892 年の石造りの蔵が現在も Ridge の醸造施設である（標高 2600 フィート、山腹に 3 層）** |
| **1920–1933** | **禁酒法。畑は十分に維持されず、1940 年代には事実上放棄された。** | ✅ **公式：「During Prohibition (1920-1933), the vineyard was not fully maintained; some vines survived into the late 30's, but by the 1940s they were effectively abandoned.」** |
| **1940 年代後半** | 🔴 **神学者 `William Short` が放棄されたワイナリーと畑を購入し、いくつかの区画をカベルネ・ソーヴィニヨンに植え替えた（1949 年に 8 エーカー）。**この樹が後の「middle vineyard（Torre Ranch）」。 | ✅ **公式 History／2022 Monte Bello 公式 History 欄** |

### Generations（現体制）

| 年 | 出来事 | 典拠 |
|---|---|---|
| **1959** | **4 人のスタンフォード研究所エンジニア（`Dave Bennion` / `Hew Crane` / `Charlie Rosen` / `Howard Ziedler`）が Monte Bello Ridge 山頂の土地を取得。** | ✅ **公式 Monte Bello 畑頁「Begun in 1959」** |
| 🔴 **1962** | 🔴 **ワイナリーを re-bond し、最初の商業リリース `Ridge Monte Bello` を出す。Dave Bennion が S.R.I. を離れ醸造専任に。** | ✅ **公式 History。**⚠️ **公式は「創業 1962 年」をこの年に置いている** |
| **1964** | **最初のジンファンデル（尾根を下った 19 世紀の小さな畑から）。同年、ラベルのデザインを商業美術家 `Jim Robertson` に依頼（報酬はワイン、$495 相当・33 時間分）。** | ✅ **公式 History／`A Deep Dive Into The RIDGE Label`** |
| 🔴 **1966** | 🔴 **最初の `Geyserville` ジンファンデル。以後 1 年も欠かさず単一畑として造り続けている。** | ✅ **公式：「Ridge has made Geyserville as a single-site zinfandel every year since 1966.」** |
| **1968–69** | **生産量が年 3,000 ケース弱に。1969 年に `Paul Draper` がパートナーシップに参加。**哲学の学位を持つスタンフォード卒で、直前までチリの海岸山脈でワイナリーを立ち上げていた。**「a practical winemaker, not an enologist」。** | ✅ **公式 History／公式 Paul Draper 頁** |
| **1969〜** | **Draper の下で Perrone の旧ワイナリー（前年取得）を修復、優良畑をリース・購入し、国際的評価を確立。** | ✅ **公式 History** |
| **1978** | 🔴 **Monte Bello 畑のうち「早く開く」区画群をまとめた `Santa Cruz Mountains` カベルネを初めて造る。** | ✅ **2023 Santa Cruz Mountains Cabernet Sauvignon 公式 History 欄** |
| **1991** | **`Lytton Springs`（Sonoma County）が Ridge の自社畑になる。** | ✅ **公式 History** |
| 🔴 **2008** | 🔴 **上記 `Santa Cruz Mountains` の名を `Estate Cabernet Sauvignon` に改称。**理由も公式が明記：**全量が Ridge 自社栽培で Monte Bello 畑由来であることを示すため。** | ✅ **公式：「In 2008, the name changed to Estate Cabernet to highlight the fact that all the grapes for that wine are grown by Ridge and come from the Monte Bello vineyard.」** |
| **2008** | **有機認証への移行を開始（→ §Farming）。** | ✅ **公式 Organic Certification 頁** |
| **2011** | 🔴 **2011 年ヴィンテージから全ワインの裏ラベルに成分表を掲載開始。** | ✅ **公式 `A Deep Dive Into The RIDGE Label`** |
| **2021** | **`John Olney` が Head Winemaker & COO に。** | ✅ **公式 Winemaking 頁** |
| 🔴 **2023** | 🔴 **`Santa Cruz Mountains Cabernet Sauvignon` のラベルを復活させる。**理由も公式が明記：**この年から外部生産者のブドウを購入したため、自社栽培の `Estate` と区別する必要が生じた。** | ✅ **公式：「In 2023, we purchased grapes from several high-quality growers in the Santa Cruz Mountains. We decided to revive this label to indicate that the grapes for this wine, rather than being farmed by Ridge, come from outside growers.」** |
| 🔴 **2024** | 🔴 **`Geyserville` のフロントラベルに `VINEYARD` の語を追加。** | ✅ **公式：「We added “vineyard” to the front label in 2024 to differentiate the historic Geyserville Vineyard from the town of Geyserville.」** |
| **2026** | **`John Olney` が CEO に就任（Head Winemaker と兼務）。** | ✅ **公式 Winemaking 頁** |

⚠️ 🔴 **`Monte Bello` の商標について：公式は「1962 年の最初のラベルには `Monte Bello` の語を使えなかった。
当時 Osea Perrone の Montebello Wine Company の法人上の後継者が商標を握っていたため。
数年後に Ridge が商標を取得した」と書いている。**（**取得年は書かれていない**） → Open Questions 5

---

## Location

| | |
|---|---|
| **Country** | **USA**（California） |
| 🔴 **Region ①** | 🏛 **`Santa Cruz Mountains`（27 CFR § 9.31）。**「**The name of the viticultural area described in this section is “Santa Cruz Mountains.”**」<br>🏛 **境界画定用の承認地形図は USGS 24 葉（うち `Cupertino Quadrangle, California`、`Castle Rock Ridge Quadrangle` を含む）**<br>→ **OBP 1・2 行目** |
| 🔴 **Region ②** | 🏛 **`Alexander Valley`（27 CFR § 9.53）。**「**The Alexander Valley viticultural area is located in northeastern Sonoma County, California.**」<br>🏛 **承認地形図 7 葉のうち 1 葉が `Geyserville Quadrangle, California—Sonoma County`**<br>→ **OBP 3 行目** |
| **Village / 所在** | **Monte Bello ワイナリー = `17100 Montebello Road, Cupertino`（Santa Clara County）／Lytton Springs = `Healdsburg`（Sonoma County）** |

### 🔴 ✅ Key Vineyard ① —— `Monte Bello`（OBP 1・2 行目）

| | ✅ 公式の記述 |
|---|---|
| 🔴 **標高** | 🔴 **`1300′ 〜 2700′`（約 396〜823 m）。**「**The Monte Bello vineyard ranges in elevation from 1300′ to 2700′ above sea level**」 |
| 🔴 **土壌** | 🔴 **「**composed of unique green stone and clay soils layered over decomposing limestone**」。**<br>🔴 **公式は石灰岩を明確に差別化点として挙げる：「**Limestone is not found in the well-known Cabernet producing areas of Napa and Sonoma Valleys, making the soil composition at Monte Bello a unique and important contributor to the wine's distinctive character.**」**<br>**別頁では「underlain by decomposing limestone and Franciscan rock」** |
| **海からの距離／気候** | **「**located only 15 miles from the Pacific Ocean, is part of the Santa Cruz Mountains AVA, California's coolest cabernet producing area**」** |
| 🔴 **収量** | 🔴 **「**very low-yielding vines (less than two tons per acre)**」** |
| **ワイナリー** | **標高 2600 フィート、1892 年に Osea Perrone が建てた石造りの蔵（3 層）。周囲が「upper vineyard」＝ `Perrone Ranch`** |
| 🔴 **歴史的ランチ名** | 🔴 🏛 **NOP 対象地一覧（面積つき）で確認できる Monte Bello 側の区画：**<br>**`Jimsomare (Klein)` Site 28 – 13350 Montebello Road … `57.60` acres**<br>**`Middle Vineyard (Torre)` Sites 01, 07 – 17100 Montebello Road … `34.80` acres**<br>**`Rousten (Ortmann)` Sites 06, 09 – 15050 Montebello Road … `28.40` acres**<br>**`Upper Vineyard (Perrone)` Site 02 – 18100 Montebello Road … `26.50` acres**<br>**`Asiago` – 17655 Montebello Road … `5.00` acres／`Jensen/Douglas Crest` – 17700 Montebello Rd … `1.25` acres** |

⚠️ **第三者（Decanter / JebDunnuck.com）は Monte Bello の標高を `1600–2700 ft` と書いているが、
生産者自身は `1300′–2700′` と書いている。本書は生産者の値を採る。**

### 🔴 ✅ Key Vineyard ② —— `Geyserville`（OBP 3 行目）

| | ✅ 公式の記述 |
|---|---|
| **位置づけ** | 🔴 **公式頁の見出しがそのまま「**Ridge's Alexander Valley Estate**」** |
| **位置** | **「**the vineyard's position three miles south of Geyserville, on the western edge of Alexander Valley**」** |
| 🔴 **構成** | 🔴 **「**The grapes are grown in three adjoining vineyards on a single soil type**」。**<br>**「**approximately one-and-a-quarter miles long and a half-mile wide**」**<br>🏛 **NOP 対象地一覧の Geyserville Avenue 系 3 区画がこれに対応する：`Fredson` Site 28, Blocks 1-3 – 18600 Geyserville Ave … `14.60` acres／`Whitton Ranch` Sites 29, 01 – 19170 Geyserville Ave … `32.80` acres／`Trentadue` Sites 33A, 33B – 19170 Geyserville Ave … `3.74` acres**<br>⚠️ **3 区画名と「three adjoining vineyards」の対応は本書の推定ではなく住所の一致による観察である。造り手が明示的に対応づけているわけではない** |
| 🔴 **土壌** | 🔴 **「**deposited by an ancient washout of the Russian River that carried river stone and gravel**」／「**deep gravelly loam mixed with larger river rocks**」。**<br>**公式はここから「distinctive mineral quality」が来ると述べる** |
| 🔴 **樹齢** | 🔴 **「**Geyserville is home to the oldest vines we farm. The “Old Patch” section of the vineyard contains vines that are more than 130 years of age.**」** |
| 🔴 **起源** | 🔴 **`Trentadue` 家。**「**Leo and Evelyn Trentadue sold the Monte Bello Winery to the four founding partners of Ridge, and the founders purchased fruit from the oldest vines on the Trentadue's Sonoma ranch on the southern edge of the Geyserville township. From that purchase, the first vintage of Ridge Geyserville was born. The close relationship with the Trentadues continues to this day.**」 |

❓ **公式に無い**: Monte Bello の総エーカー数（NOP 一覧の合計は算出できるが、造り手が「畑の総面積」として述べた数値は無い）、
区画ごとの植樹年、台木、樹齢構成の全体。

---

## Farming

### 🔴 Organic —— **本節は本ドシエで最も強い。証書そのものが読めている。**

🏛 🔴 **USDA National Organic Program 認証書（生産者が自社ドメインで配信）**

```
CERTIFICATE — According to NATIONAL ORGANIC PROGRAM
Issued to: RIDGE VINEYARDS, INC.
           P.O. BOX 1810, CUPERTINO, CALIFORNIA, 95015
Certified to the USDA organic regulations 7CFR Part 205.
Organic Production Category: Crops
Product(s): 100% Organic Wine Grapes - Ridge Vineyards Inc
Certificate Number: 23-0793
Initial Effective Date: 09/03/2011
Anniversary Date: 09/03/2024
Issued Date: 09/06/2023
Authorized by: Susan D. Siple, Executive Director
```
🔴 **認証機関は `Organic Certifiers`（`6500 Casitas Pass Road, Ventura, CA 93001`）。証書のレターヘッドから実読した。**
🔴 **証書本文の継続条項：「**Once certified, a production or handling operation's organic certification continues
in effect until surrendered, suspended or revoked.**」**

### ⚠️ 認証の時間軸（**`D-2026-08-05-XX` の温度差ルール。ヴィンテージごとに確認する**）

✅ **造り手自身の年表（`/about/sustainability/organic-certification/`）:**

| 年 | 公式の記述 |
|---|---|
| **2008** | **「**after more than a decade of sustainably farming our estate vineyards, and after five years of experimenting with new organic treatments, we began the process of organic certification**」**（**移行期間は米国では 3 年**） |
| **2011** | 🔴 **「**76 acres at Monte Bello and 135 acres at Lytton Springs and Geyserville were certified organic**」**（**証書の Initial Effective Date `09/03/2011` と一致する**） |
| **2014** | **「**A second wave of blocks at both our Geyserville and Lytton Springs Vineyards completed certification**」** |
| 🔴 **2015** | 🔴 **「**The remaining blocks of the Geyserville Vineyard were certified organic**」** |
| **2021** | **「**As of harvest, the total of our organically farmed vines has reached 379 acres**」** |
| 🔴 **2022** | 🔴 **「**As of harvest, 100% of our estate vineyards are certified organic, including Monte Bello, Lytton Springs, Geyserville, and East Bench.**」**<br>**別頁（Monte Bello 畑）も「**100% of our Monte Bello Vineyard has been certified organic since harvest 2022.**」** |

🔴 **OBP 3 本への当てはめ（ヴィンテージが認証の範囲に入っているかを 1 本ずつ確認した）**

| OBP 行 | VT | 認証の射程 | 公式ワイン頁の表示 |
|---|---|---|---|
| **2. Monte Bello** | **2022** | 🔴 **入る。**2022 年収穫から Monte Bello 畑 100% 認証 | ✅ **`Organically Grown`／「Hand-harvested; estate grown Monte Bello Vineyard grapes」** |
| **1. Estate Cabernet** | **2023** | 🔴 **入る。**同上（同じ Monte Bello 畑） | ✅ **`Organically Grown`／「Hand-harvested, estate-grown grapes」** |
| **3. Geyserville Vineyard** | **2024** | 🔴 **入る。**Geyserville は 2015 年に全区画認証済み | ✅ **`Organically Grown`／🔴「**Hand-harvested organic grapes**」** |

🔴 ⚠️ **「organically grown」の意味を造り手自身が限定している。ここを混ぜない。**
✅ **「**At that point, a wine produced from the certified grapes can be labeled as “organically grown”
if 100% of the grapes are certified.**」**
✅ **ラベル成分表の規則欄でも「**\*Grapes must be 100% certified organic in order to make the statement
“organically grown.”**」**
→ 🔴 **これは「ブドウが 100% 有機認証」という意味であって、「オーガニックワイン（NOP の `organic wine` 表示）」ではない。**
**本調査で得た証書の Product は `100% Organic Wine Grapes`（＝ Crops カテゴリー）であり、ワインの認証ではない。** → §Staff Notes ⚠️ ④

### Biodynamic

🔴 ⚠️ **本調査で読んだ公式頁のいずれにも `biodynamic` / `Demeter` / `biodynamie` の語は一件も現れなかった。**
→ **ビオディナミは主張しない。**

### Sustainable

✅ **公式の `Industry Recognition & Certifications` 欄が自ら挙げている枠組み:**
**`Organically Certified Vineyards` / `Lytton Springs: A Sustainable Winery` / `California Sustainable
Winegrowing Alliance` / `Robert Parker Green Emblem` / `IWCA Member`。**
✅ **「**RIDGE strives to be a thought leader for climate action in the wine industry… we commit ourselves to
transparency and will share our progress here.**」（カーボンニュートラルを目標として掲げる）**
⚠️ 🔴 **ただし本調査では、これら 5 つのうち有機認証以外について、認証番号・発効日・対象範囲を示す一次文書を取得していない。**
→ **卓上では「有機認証」以外を具体的な認証名で語らない。** → §Staff Notes ⚠️ ⑤

### Other（造り手の栽培哲学）

✅ **「**Starting in 2008, we began the transition to farming our estate vineyards organically in order to bring
our vineyard management techniques in line with our traditional winemaking practices, which employ only the
non-invasive treatments used in fine winemaking prior to Prohibition.**」**
✅ **投入資材の抑制：「**Seeding our vineyards with non-vine plants attracts beneficial predatory insects,
which mitigates the need to apply an insecticide that might cause harm to non-targeted species like bees.**」**
✅ **土壌：「**To preserve soil structure, we only cultivate every other row between grapevines. At both of our
winery facilities, we collect the stems and pomace left over from winemaking to make organic compost.**」**
✅ **Monte Bello 畑：「**We do not add anything to the vineyard that is not natural.**」**

⚠️ 🔴 **サイト内の温度差を記録する。**`/vineyards/geyserville/` の本文は依然として
「**our commitment to sustainable agriculture**」としか書いておらず、有機認証に触れていない。
一方、同じ畑の 2024 年ワイン頁は「**Hand-harvested organic grapes**」と書く。
→ **新しい情報（ワイン頁・認証頁）のほうが具体的である。畑紹介頁の古い文言だけを引かない。**

---

## Winemaking

### ✅ 造り手の原則（`pre-industrial`）

✅ **「**We ferment our wines using the native yeasts from the vineyard rather than cultured yeast strains.**」**
✅ **「**We extract color, flavor, and tannins from the grapes without the use of commercial enzymes or nutrients.**」**
🔴 ✅ **「**Once asked what the single most important device was for making fine wine, Paul Draper responded,
“the wine glass.”**」——「**we make our major winemaking decisions based on blind tasting rather than a
pre-determined recipe.**」**
✅ **Monte Bello 畑頁：「**keeping all grape varieties and all parcels separate, fermenting in small fermentors
using only natural yeasts, and transferring the separate lots into air-dried American oak barrels to undergo
full, natural malolactic fermentation**」**

### 🔴 ✅ OBP 3 本の技術仕様（**公式ワイン頁の定型欄をそのまま実測**）

| 項目 | **2023 Estate Cabernet Sauvignon** | **2022 Monte Bello** | **2024 Geyserville Vineyard** |
|---|---|---|---|
| 🔴 **セパージュ** | 🔴 **75% Cabernet Sauvignon / 19% Merlot / 3% Cabernet Franc / 3% Petit Verdot** | 🔴 **86% Cabernet Sauvignon / 10% Merlot / 2% Petit Verdot / 2% Cabernet Franc** | 🔴 **71% Zinfandel / 19% Carignane / 8% Petite Sirah / 2% Alicante Bouschet** |
| **畑** | **Monte Bello** | **Monte Bello** | **Geyserville** |
| **AVA** | **Santa Cruz Mountains** | **Santa Cruz Mountains** | **Alexander Valley** |
| **アルコール** | **13.4%** | **13.8%** | **14.6%** |
| **収穫** | **9 September – 5 October** | **13 September – 10 October** | **2 September – 9 October** |
| **Brix / TA / pH** | **23.4° / 7.2 g/L / 3.41** | **23.6° / 9.13 g/L / 3.36** | **24.7° / 5.2 g/L / 3.68** |
| 🔴 **発酵** | **除梗・選果、100% 全粒（whole berries）、野生酵母** | 🔴 **除梗、100% whole-berry fermentation、野生酵母、自発的マロラクティック** | **Full Crush、100% floating cap、一次・二次とも自発、毎日のポンピングオーバー** |
| 🔴 **樽** | 🔴 **100% 空気乾燥アメリカンオーク（新樽 55%、2 年 10%、4 年 35%）** | 🔴 **新樽 100%（アメリカン 95% / フレンチ 5%）** | 🔴 **100% 空気乾燥アメリカンオーク（新 15%、1 年 15%、2 年 10%、3 年 30%、4 年 30%）** |
| **樽熟** | **17 か月** | 🔴 **21 か月**（＋選抜前の期間） | **16 か月** |
| 🔴 **選抜** | **「the most approachable lots from the Monte Bello vineyard」** | 🔴 **「Eighteen of thirty-one lots were selected by blind tasting」→ Eighteen Monte Bello parcels** | **「individual lots were selected, assembled, and racked to American oak for thirteen months」** |
| 🔴 **成分表（造り手の定型文）** | **「Hand-harvested, estate-grown grapes; destemmed and sorted; fermented on indigenous yeast; calcium carbonate; full malolactic on the naturally occurring bacteria; minimum effective sulfur (35 ppm at crush, 85 ppm during aging).」** | **「Hand-harvested; estate grown Monte Bello Vineyard grapes, destemmed and sorted; fermented on the native yeasts; full malolactic on the naturally occurring bacteria; oak from barrel aging; minimum effective sulfur (35 ppm at crush, 114 ppm during aging); depth filtered at bottling.」** | **「Hand-harvested organic grapes; destemmed and crushed; fermented on the native yeasts, followed by full malolactic on the naturally-occurring bacteria; oak from barrel aging; minimum effective sulfur for this wine (35 ppm at crush, 170 ppm over the course of aging); pad filtered at bottling.」** |
| **共通の結語** | \* | 🔴 **3 本すべてが「**In keeping with our philosophy of minimal intervention, this is the sum of our actions.**」で終わる** | \* |

⚠️ 🔴 **カルシウム・カーボネート（炭酸カルシウム）は 2023 Estate Cabernet にのみ現れる。**
造り手の定義：「**Small addition during fermentation, only used to moderate unusually high natural acidity.**」
→ **2022 Monte Bello と 2024 Geyserville には入っていない。3 本を一括りにしない。**

⚠️ 🔴 **`minimum effective` という表現について。**造り手のラベル解説には
「**SO2 (The phrase minimum effective was used until 2019 when the TTB ruled we could no longer use it.**」とある。
🔴 **すなわちウェブ上の技術情報では今も `minimum effective sulfur` と書かれているが、ラベル上の文言は 2019 年以降変わっている可能性が高い。**
⚠️ **本調査では該当 3 本の裏ラベル現物を読めていないため、ラベル上の実際の文言は主張しない。** → Open Questions 1

### Philosophy —— **成分表（Ingredient labeling）**

🔴 ✅ **2011 年ヴィンテージから全ワインの裏ラベルに成分表を載せている。造り手の説明:**
「**Although an ingredient list is not required by the TTB, if a winery chooses to add a list of ingredients
to its back label it must list ALL ingredients.**」
🔴 ✅ **常時記載される項目（造り手が列挙）:** **Grapes / Hand harvested / Sustainably Grown または Organically Grown（該当時）/
Estate（該当時）/ Indigenous yeasts / Naturally occurring malolactic bacteria / Oak from barrel aging / SO2。**
🔴 ✅ **使用時のみ記載:** **% Water Addition / Calcium Carbonate / Tartaric Acid。**
✅ **卵白（Egg Whites）を使った場合は FDA のアレルゲン表示「Contains Egg」が必要になる、と造り手自身が書いている。**

---

## Style

### ✅ 公式ワインメーカーノート（**署名 `JO` = John Olney。OBP 3 本すべて存在する**）

| ワイン | 公式ノート（逐語） |
|---|---|
| 🔴 **2022 Monte Bello** | 「**Saturated ruby color. Intense aromas of blackberry, black currant, fennel, dry chaparral, tobacco leaf, crushed stone, and toasted oak. On the palate, rich mountain bramble and cassis, polished tannins, and full bodied. Natural firm acidity leads to a long finish showing limestone minerality.**」JO (11/24) |
| 🔴 **2023 Estate Cabernet Sauvignon** | 「**Deep ruby red with toasty oak and blackberry fruit on the nose. Full-bodied, structured with firm tannins, bright acid and notes of mint on the finish.**」JO (1/26) |
| 🔴 **2024 Geyserville Vineyard** | 「**Raspberry, vanilla and licorice on the nose. Palate of focused black cherry, nutmeg, subtle tannins, balanced acidity and a long finish.**」JO (1/26) |

### ✅ 公式ヴィンテージノート（**年の性格を造り手の言葉で言える**）

| 年 | 公式の記述 |
|---|---|
| 🔴 **2022**（Monte Bello） | 🔴 **「**A third year of drought accompanied by a heat wave during ripening, reduced yields. To manage tannins, all grapes were fermented as whole berries, pressed once dry, and transferred to American oak for natural malolactic… This classic Monte Bello will evolve over the next twenty to twenty-five years.**」**<br>**Growing Season 欄：**「Rainfall: 28 inches (below normal) / Bloom: Late May / **Two heat spells, one in late July and the other in late August, pushed the vines to an early harvest.**」 |
| 🔴 **2023**（Estate Cabernet） | 🔴 **「**Heavy winter rains ended our three-year drought. Due to an unusually cool growing season, harvest was late; beginning in October and not finishing until mid-November. We extended fermentations to better extract full color while balancing the tannins and firm acidity. In tasting, we selected the most approachable lots from the Monte Bello vineyard for the Estate. This appealing vintage will be at its best over the next fifteen years.**」**<br>**Growing Season 欄：**「Rainfall: **84 inches (above average)** / Bloom: **Late June**」 |
| 🔴 **2024**（Geyserville） | 🔴 **「**A rainy winter, mild spring, and warm summer advanced ripening. Harvest began early on August 30th and finished by September 14th. After malolactic, individual lots were selected, assembled, and racked to American oak for thirteen months. This wine shows the unique expression of soil and microclimate coupled with the complexity of a field blend. Delicious.**」**<br>**Growing Season 欄：**「Rainfall: 46 inches (above average) / Bloom: Early May / **A cool start to the season. From early June on, the weather was warm to hot, leading to a condensed harvest.**」 |

⚠️ 🔴 **2024 Geyserville は、ヴィンテージノートの収穫日（`began early on August 30th and finished by September 14th`）と
Winemaking 欄の `Harvest Dates: 2 September – 9 October` が食い違っている。同一頁内の矛盾である。**
→ **卓上で具体的な収穫日を言わない。「早い年だった」までにとどめる。** → §Staff Notes ⚠️ ⑦

### 🔴 ✅ スタイルの骨格（造り手の自己記述）

- 🔴 **Monte Bello = ボルドー型のアッサンブラージュ。**「**Monte Bello has often been called America's First Growth,
  as it is the finest domestic example of a classic Bordeaux blend in which cabernet sauvignon predominates.
  Exhaustive tasting of test blends during the assemblage process determines how much, if any, merlot,
  petit verdot, or cabernet franc will be included in the finished wine.**」
  🔴 ✅ **品種ごとの寄与も造り手が言語化している：「cabernet sauvignon often showing cassis and adding tannin,
  merlot giving plum character and a bit of softness, petit verdot contributing dark color and earthiness,
  and cabernet franc adding fragrance and a hint of spice」**
- 🔴 **Geyserville = 混植（field blend）。**「**Geyserville is a traditional field blend of zinfandel and its
  complementary varieties: carignane, petite sirah, and mataro (mourvedre).**」
  🔴 **「**Geyserville's unique flavor characteristics are often attributed to the relatively higher percentage of
  carignane, added to the petite sirah found in most of our other zinfandels. Among the most age-worthy of
  Ridge wines, Geyserville often drinks beautifully well beyond 10 years of age.**」**
  ⚠️ **2024 年の実際の構成に `mataro / mourvedre` は入っていない（Alicante Bouschet 2% が入る）。年により動く。**

---

## Important Cuvées

### 🔴 まず造り手のラベル文法（**`A Deep Dive Into The RIDGE Label` の逐語。ここが本節の土台**）

✅ **フロントラベルは `Top Block`（ワインの identity）と `Bottom Block`（追加情報）の 2 段構成。**

| Top Block の要素 | ✅ 造り手自身の条件 |
|---|---|
| **(A) Brand Name** | **「**always the word RIDGE**」** |
| **(B) Vintage Year** | **「**per TTB regulations at least 95% of the grapes used to make the wine must be harvested in the vintage year**」** |
| 🔴 **(C) Grape Variety** | 🔴 **「**We use the primary grape variety in the Top Block when 1) the wine contains at least 75% of that variety per TTB regulation and 2) we have chosen not to use a proprietary name for the wine.**」** |
| 🔴 **(D) Estate** | 🔴 **「**A wine will carry the Estate designation in the top block when 1) 100% of the grapes used to make the wine are grown on land that Ridge owns or leases and is in the same AVA as the winery location per TTB regulation and 2) we have chosen not to use another descriptive term or proprietary name for the wine.**」** |
| 🔴 **Vineyard Name** | 🔴 **「**The TTB requires that 95% of the grapes used to make the wine must come from the named vineyard and that the name used is the one currently found on official maps of the vineyard. In some cases we have chosen to use a historical name for the vineyard, in which case the TTB will consider it to be a Proprietary Name.**」** |
| 🔴 **Proprietary Name** | 🔴 **「**When Ridge uses a proprietary name in the Top Block, in most cases we will not include a grape variety in the Top Block. This allows for the production of a wine in which no single varietal must account for 75% or more of the wine.**」**（例として `Three Valleys`） |
| **AVA** | **「**Ridge uses an AVA in the Top Block if the wine is made from grapes from multiple vineyards within the AVA**」**（例として `Paso Robles`） |

| Bottom Block の要素 | ✅ 造り手自身の説明 |
|---|---|
| **(A) Vineyard Name** | **単一畑ワインでは畑名を 1 行目に置く** |
| 🔴 **(B) Grape Variety(s)** | 🔴 **「**We use the Bottom Block to list all of the varietals used to make the wine and show the percentage each one contributes to the blend.**」** |
| **(C) AVA** | **「**We always try to include the most specific AVA in which the grapes were grown**」** |
| **(D) Alcohol by Volume** | **「**Ridge's policy is to use the most accurate measurement possible even though the regulations allow for a variance of +/- 0.5%**」** |
| 🔴 **(E) Production Statement** | 🔴 **「**If Ridge has grown the grapes then the statement will be “Grown, Produced, and Bottled by Ridge Vineyards”… If Ridge purchased the grapes then the statement will simply be “Produced and Bottled by Ridge Vineyards”**」** |
| **(F) Address** | **醸造したワイナリーの住所** |

---

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 3 行。3 行とも `match_state = unresolved` / `confidence 0.0`**）

#### 🔴 行 1 —— `obp-beverage-2026-08:43436ec6c8`
**印字 `'Estate,' Santa Cruz Mountains Cabernet Sauvignon` / VT 2023 / $300 / `UNITED STATES | RED > SANTA CRUZ`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。公式製品名は `2023 Estate Cabernet Sauvignon`**（`/wines/2023-estate-cabernet-sauvignon/`） |
| 🔴 **ラベル実読**（公式ボトルショット `23CRE-web2.png`） | 🔴 **Top Block: `RIDGE` ／ `2023` ／ `ESTATE` ／ `CABERNET SAUVIGNON`**<br>🔴 **Bottom Block: `MONTE BELLO VINEYARD` ／ `75% CABERNET SAUVIGNON, 19% MERLOT, 3% CABERNET FRANC, 3% PETIT VERDOT` ／ `SANTA CRUZ MOUNTAINS` ／ `13.4% ALCOHOL BY VOLUME` ／ `GROWN, PRODUCED & BOTTLED BY RIDGE VINEYARDS, INC.` ／ `17100 MONTEBELLO ROAD, CUPERTINO, CALIFORNIA 95014`** |
| 🔴 **`'Estate,'` はカテゴリー語か** | 🔴 **違う。Top Block に大きく `ESTATE` と印字されている。**<br>🔴 **さらに造り手は `Estate` を「designation（指定語）」として定義し、その条件（自社所有・リース地 100%、ワイナリーと同一 AVA）まで公開している。**<br>→ 🔴 **`CDX-15` の反復パターン（カテゴリー語をキュヴェ名として印字）は、本行では成立しない。** |
| 🏛 **`Cabernet Sauvignon` の表示は適法か** | 🔴 **75% ちょうど。**🏛 **27 CFR § 4.23(b)：「**the name of a single grape variety may be used as the type designation if not less than 75 percent of the wine is derived from grapes of that variety, the entire 75 percent of which was grown in the labeled appellation of origin area**」**<br>→ 🔴 **閾値ちょうどで成立している。「ほぼ全部カベルネ」ではない** |
| ⚠️ **取り違えリスク** | 🔴 **同じ 2023 年に `2023 Santa Cruz Mountains Cabernet Sauvignon` が別に存在する**（81% CS / 15% Merlot / 4% PV、13.2%、Bates Ranch・Fellom Ranch・Monte Bello・Vidovich Vineyards の**買いブドウ**、**`Organically Grown` の表示なし**）。<br>🔴 **メニュー印字はこの 2 製品名を 1 行に含む。分けるのは `Estate` の 1 語だけである** |
| 🔍 **canonical** | 🔴 **対応レコード無し（gap）** |

#### 🔴 行 2 —— `obp-beverage-2026-08:f70b019945`
**印字 `'Monte Bello,' Santa Cruz Mountains Cabernet Sauvignon` / VT 2022 / $990 / `UNITED STATES | RED > SANTA CRUZ`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。公式製品名は `2022 Monte Bello`**（`/wines/2022-monte-bello/`）。**「Cabernet Sauvignon」は製品名に含まれない** |
| 🔴 **ラベル実読**（公式ボトルショット `22CMB-web.png`） | 🔴 **Top Block: `RIDGE` ／ `2022` ／ `MONTE BELLO`。**🔴 **品種名は Top Block に無い。**<br>🔴 **Bottom Block: `MONTE BELLO VINEYARD` ／ `86% CABERNET SAUVIGNON, 10% MERLOT, 2% PETIT VERDOT, 2% CABERNET FRANC` ／ `SANTA CRUZ MOUNTAINS` ／ `13.8% ALCOHOL BY VOLUME` ／ `GROWN, PRODUCED & BOTTLED BY RIDGE VINEYARDS` ／ `17100 MONTEBELLO RD, CUPERTINO, CALIFORNIA 95014`** |
| 🔴 **メニューの `Cabernet Sauvignon` の扱い** | ⚠️ 🔴 **ラベルの Top Block には無い語である。**Bottom Block の構成比表示の第 1 項として `86% CABERNET SAUVIGNON` が現れるのみ。<br>🔴 **造り手のラベル文法によれば、Monte Bello は proprietary name であり「in most cases we will not include a grape variety in the Top Block」の類型に当たる。**<br>→ **「86% がカベルネ・ソーヴィニヨン」は事実。しかし「ラベルにカベルネ・ソーヴィニヨンと書いてある」は事実ではない。** |
| 🔍 **canonical** | ⚠️ **`ridge-monte-bello` が 1 件あるが `vintage='—'`。**🔴 **intake は `cuvee_state: exact` を出しながら evidence に「canonical の 'Monte Bello' に vintage 2022 無し（保有: ゼロ件）」と書いている。`CDX-2` の形（`exact` は `unresolved` より強い同定ではない）。1 行で記録し、深追いしない** |

#### 🔴 行 3 —— `obp-beverage-2026-08:717413779c`
**印字 `'Geyserville Vineyard,' Alexander Valley Proprietary Blend` / VT 2024 / $175 / `UNITED STATES | RED > SONOMA`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。公式製品名は `2024 Geyserville Vineyard`**（`/wines/2024-geyserville-vineyard/`） |
| 🔴 **ラベル実読**（公式ボトルショット `24ZGY-web2.png`） | 🔴 **Top Block: `RIDGE` ／ `2024` ／ `GEYSERVILLE` ／ `VINEYARD`**<br>🔴 **Bottom Block: `71% ZINFANDEL, 19% CARIGNANE, 8% PETITE SIRAH, 2% ALICANTE BOUSCHET` ／ `ALEXANDER VALLEY` ／ `SONOMA COUNTY` ／ `14.6% ALCOHOL BY VOLUME` ／ `GROWN, PRODUCED & BOTTLED BY RIDGE VINEYARDS` ／ `17100 MONTEBELLO ROAD, CUPERTINO, CALIFORNIA 95014`** |
| 🔴 **`'Geyserville Vineyard,'` は正しいか** | 🔴 **正しい。しかも 2024 年に限って正しい。**造り手自身が同じ頁で説明している：「**This year's Geyserville release is the same Geyserville that RIDGE has been producing since 1966. We added “vineyard” to the front label in 2024 to differentiate the historic Geyserville Vineyard from the town of Geyserville.**」<br>🔴 **公式サイトの URL スラッグも 2023 年までは `geyserville`、2024 年から `geyserville-vineyard` に変わっている。**<br>→ 🔴 **メニューはヴィンテージ単位でラベルに追随している。ここは OBP のほうが正確である** |
| ⚠️ **`Proprietary Blend` は何か** | 🔴 **ラベルに存在しない。公式サイトにも存在しない語である。**<br>🔴 **造り手が使う語は `Proprietary Name`（Top Block の指定語）と `field blend`（Geyserville の構成の呼び名）であって、`Proprietary Blend` ではない。**<br>→ 🔴 **これはメニュー側のカテゴリー語である。`CDX-15` の反復パターンに当たる 1 例。**<br>⚠️ **ただし内容としては誤りではない：71/19/8/2 で 75% に達する品種が無いため、🏛 27 CFR § 4.23(b) の下で品種名を type designation にできない。造り手のラベル文法もそう説明している** |
| 🔍 **canonical** | 🔴 **対応レコード無し（gap）。**`Geyserville` を含むレコードは canonical に 0 件 |

### ✅ 生産者の主要ラインナップ（**canonical には 1 件も無い。参考**）

🔍 **`wine-sitemap.xml` + `wine-sitemap2.xml` の 1,134 URL から機械的に確認できた系列:**
🔴 **`Monte Bello`（1962〜）**⭐OBP／🔴 **`Estate Cabernet Sauvignon`（2008〜。それ以前は `Santa Cruz Mountains Estate`）**⭐OBP／
🔴 **`Geyserville` / `Geyserville Vineyard`（1966〜）**⭐OBP／
**`Santa Cruz Mountains Cabernet Sauvignon`（1978–2007、2023 年に買いブドウで復活）／`Monte Bello Chardonnay`／
`Estate Chardonnay`／`Lytton Estate` 系（Petite Sirah・Rosé ほか）／`Jimsomare Zinfandel`／`Rousten Cabernet Franc`**
✅ **44 の畑が `vineyard-sitemap.xml` に個別頁として存在する**（`Lytton Springs`, `Pagani Ranch`, `Monte Rosso`,
`East Bench`, `Dusi Ranch`, `Evangelho`, `Bedrock`, `York Creek`, `Fellom Ranch`, `Bates Ranch`, `Vidovich Vineyards` ほか）。

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 1962 年創業のサンタクルーズ山脈の蔵。「単一畑」「pre-industrial（前産業的）」「透明性」の 3 つで一貫している。**
「**サンフランシスコの南、サンタクルーズ山脈の尾根の上**にある蔵です。
**畑と石造りの蔵そのものは 1885〜1892 年**、ペローネというイタリア系の医師が拓いたもので、
禁酒法で一度放棄されました。**いまの Ridge は 1962 年、スタンフォード研究所のエンジニア 4 人が
ワイナリーを再登録して始まっています。1969 年に加わったポール・ドレイパーが今も
`Winemaker Emeritus`（名誉醸造家）**として公式に名を連ねています。
**現在の醸造責任者は 1996 年入社のジョン・オルニーで、2026 年から CEO も兼ねています。
グラスに書いてあるテイスティングノートの `JO` はこの人の署名です。**
造り手は自分たちの造りを **`pre-industrial`（前産業的）**と呼びます。
**野生酵母のみ、市販の酵素も栄養剤も使わない、機械的な補正もしない。
そして 2011 年ヴィンテージから、全部のワインの裏ラベルに成分をすべて書いています。**」

**② 有機認証は「言っている」のではなく「証書を公開している」。ただし『オーガニックワイン』ではない。**
「🔴 **Ridge は USDA の全米有機プログラムの認証書そのものを自社サイトで公開しています。
証書番号 `23-0793`、初回発効は 2011 年 9 月 3 日、認証機関は Organic Certifiers。
対象地の一覧も、区画ごとの面積つきで出ています。**
**造り手の年表では、2011 年に Monte Bello の 76 エーカーと Lytton Springs / Geyserville の 135 エーカーが認証、
2015 年に Geyserville が全区画、2022 年の収穫から自社畑 100% が認証済みです。**
🔴 **今日お出しする 3 本は 2022・2023・2024 なので、いずれもその範囲に入っています。**
⚠️ **ただし正確には『**Organically Grown**（有機栽培のブドウ）』であって『オーガニックワイン』ではありません。
造り手自身が『ブドウが 100% 認証されている場合にのみこの表示ができる』と書いています。**」

**③ ラベルの読み方を造り手が公開している。だから 3 本の名前の違いに意味がある。**
「🔴 **Ridge のラベルは上下 2 段です。上段（Top Block）が『このワインが何か』、下段が追加情報。
造り手はどの語がどの条件で上段に載るかを自分で公開しています。**
🔴 **`ESTATE` は指定語で、"ブドウの 100% が Ridge の所有地かリース地で、ワイナリーと同じ AVA 内で穫れたとき" に載ります。
だから 2023 年の Estate カベルネは Monte Bello 畑の自社栽培だけです。**
🔴 **`MONTE BELLO` は畑の名（proprietary name）なので、上段に品種名は入りません。
下段に `86% CABERNET SAUVIGNON` と構成比が出るだけです。**
🔴 **`GEYSERVILLE VINEYARD` の `VINEYARD` は 2024 年から付きました。
造り手が『歴史的な Geyserville 畑と、Geyserville という町とを区別するために足した』と明記しています。
つまりこのメニューの表記は、2024 年のラベルどおりです。**」

### 追加で使える一手（**すべて公式一次資料**）

- 🔴 **3 本の対比（$300 / $990 / $175）**：「**同じ Monte Bello 畑から 2 本、ソノマの混植畑から 1 本**です。
  **2022 Monte Bello（$990）は 31 ロットのうち 18 ロットをブラインドテイスティングで選抜し、
  新樽 100%（アメリカン 95%・フレンチ 5%）で 21 か月。造り手は『今後 20〜25 年かけて開く』と書いています。
  86% カベルネ・ソーヴィニヨン、アルコール 13.8%。**
  **2023 Estate カベルネ（$300）は同じ畑から『いちばん早く開くロット』を選んだほう。
  新樽 55% を含むアメリカンオーク 17 か月、造り手は『今後 15 年が飲み頃』。75% カベルネ・ソーヴィニヨン、13.4%。**
  **2024 Geyserville（$175）は 71% ジンファンデル、19% カリニャン、8% プティット・シラー、2% アリカンテ・ブーシェ。
  130 年を超える古木を含む混植畑です。**」
- 🔴 **Monte Bello の石灰岩**：「**造り手が差別化点として名指しするのは石灰岩です。
  『**Limestone is not found in the well-known Cabernet producing areas of Napa and Sonoma Valleys**』
  ——ナパやソノマのカベルネ産地には石灰岩が無い、と。標高は 1300〜2700 フィート、太平洋から 15 マイル、
  造り手いわく『カリフォルニアで最も冷涼なカベルネ産地』。収量はエーカーあたり 2 トン未満です。**」
- 🔴 **Geyserville の古木**：「**『Old Patch』と呼ばれる区画には樹齢 130 年を超える樹があります。
  蔵が農作業をしている畑の中でいちばん古い。1966 年から一年も欠かさず単一畑として造り続けていて、
  もともとは Monte Bello のワイナリーを創業者たちに売った Trentadue 家のブドウから始まりました。
  土壌はロシアン・リバーの古い氾濫が運んだ礫と川石まじりの深いローム。**」
- 🔴 **年の性格**：「**2022 は 3 年目の干ばつ＋熟期の熱波。造り手はタンニンを抑えるため全房ではなく
  全粒（whole berry）で発酵させ、乾いた時点で圧搾したと書いています。
  2023 は逆に、雨量 84 インチで 3 年の干ばつが終わり、冷涼で収穫が 10 月から 11 月中旬まで長引いた年。
  2024 は雨の冬・穏やかな春・暑い夏で熟期が前倒しになった年です。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／第三者の主張にすぎない**）

1. 🔴 ⚠️ **『メニューの "Geyserville Vineyard" は表記ゆれです』と言わない。**
   **2024 年のフロントラベルにその通り印字されている。造り手が 2024 年から `VINEYARD` を足したと明記している。
   むしろ 2023 年以前のヴィンテージには `VINEYARD` が無い。ヴィンテージを跨いで一般化しない。**
2. 🔴 ⚠️ **1 行目を `Santa Cruz Mountains Cabernet Sauvignon` として語らない。**
   🔴 **Ridge は 2023 年に `Estate Cabernet Sauvignon` と `Santa Cruz Mountains Cabernet Sauvignon` の
   2 本を並行して出している。前者は自社栽培（Monte Bello 畑・`Organically Grown` 表示あり）、
   後者は買いブドウ（Bates Ranch / Fellom Ranch / Monte Bello / Vidovich、公式頁に `Organically Grown` の表示なし）。**
   **メニューが `'Estate,'` と書いている以上、前者である。ここを混ぜると有機の話まで嘘になる。**
3. 🔴 ⚠️ **『Monte Bello のラベルにはカベルネ・ソーヴィニヨンと書いてあります』と言わない。**
   **Top Block は `RIDGE / 2022 / MONTE BELLO` だけ。品種名は無い。
   下段の構成比表示に `86% CABERNET SAUVIGNON` と出るだけである。
   「86% がカベルネ」は言ってよい。「ラベルにカベルネと書いてある」は言わない。**
4. 🔴 ⚠️ **『オーガニックワインです』と言わない。**
   **造り手が公開しているのは 🏛 NOP の `Crops`（作物）カテゴリーの証書で、Product は `100% Organic Wine Grapes`。
   ワインの認証ではない。公式サイトの表示も一貫して `Organically Grown` である。
   造り手自身が「ブドウが 100% 認証されている場合にのみ `organically grown` と表示できる」と書いている。**
5. 🔴 ⚠️ **有機以外の認証名を具体的に語らない。**
   **公式は `California Sustainable Winegrowing Alliance`、`Robert Parker Green Emblem`、`IWCA Member`、
   `Lytton Springs: A Sustainable Winery` を掲げているが、本調査ではそれぞれの認証番号・発効日・対象範囲を
   示す一次文書を取得していない。「サステナビリティにも取り組んでいる」までにとどめる。**
6. 🔴 ⚠️ **『ビオディナミ』と言わない。** **公式資料に語が一件も無い。**
7. 🔴 ⚠️ **2024 Geyserville の収穫日を具体的に言わない。**
   **同じ公式頁の中で「began early on August 30th and finished by September 14th」と
   「Harvest Dates: 2 September – 9 October」が食い違っている。「早い年だった」までにとどめる。**
8. 🔴 ⚠️ **『1976 年のパリの試飲会で 5 位、2006 年の再戦で 1 位』と言わない。**
   🔴 **本調査で読んだ生産者著作の頁に、この順位を造り手自身が述べた記述は 1 件も見つからなかった。**
   **`/about/news/` は第三者媒体の引用集であり、本書は事実の典拠として一切採用していない。**
   **（THÉSEUS の DB はこの順位を書いているが、造り手の言葉ではない。）** → §Canonical Conflict ②
9. 🔴 ⚠️ **『ポール・ドレイパーは 2016 年に退任した』と言わない。**
   **公式頁の見出しは `Paul Draper - Winemaker Emeritus / Joined Ridge in 1969` で、退任年の記載が無い。
   造り手が公表しているのは「1969 年入社」と「Winemaker Emeritus」の 2 点だけである。**
10. 🔴 ⚠️ **『Estate Bottled（エステート・ボトルド）です』と言わない。**
    🏛 **`Estate bottled` は 27 CFR § 4.26 の法定用語で、(1) 瓶詰め蔵が表示 AVA 内にあること
    (2) 使用ブドウ全量を表示 AVA 内の蔵の所有・支配地で栽培したこと
    (3) 破砕・発酵・仕上げ・熟成・瓶詰めを連続工程で行ったこと、の 3 要件すべてを要する。**
    **本調査で読めたのはフロントラベルのみで、そこにあるのは `ESTATE`（Top Block の指定語）と
    `GROWN, PRODUCED & BOTTLED BY RIDGE VINEYARDS, INC.` の生産表示であって、`ESTATE BOTTLED` の 2 語ではない。**
    **裏ラベルは未取得、TTB COLA は CAPTCHA でゲートされていた。どちらとも言わない。**
11. 🔴 ⚠️ **『Estate カベルネはほぼ全部カベルネ・ソーヴィニヨンです』と言わない。**
    **2023 年は `75%` ちょうど。🏛 27 CFR § 4.23(b) の下限そのものである。残り 25% はメルロ 19%、
    カベルネ・フラン 3%、プティ・ヴェルド 3%。**
12. ⚠️ **成分表の文言をラベル上のものとして引用しない。**
    **ウェブ上の技術情報は `minimum effective sulfur` と書いているが、造り手自身が
    「the phrase minimum effective was used until 2019 when the TTB ruled we could no longer use it」と書いている。
    裏ラベル現物を読めていない以上、ラベル上の実際の文言は主張しない。**
13. ⚠️ **炭酸カルシウム・水・酒石酸を 3 本一律に語らない。**
    **炭酸カルシウムは 2023 Estate カベルネにのみ記載がある。2022 Monte Bello と 2024 Geyserville には無い。**
14. ⚠️ **第三者点数を蔵の説明として使わない。**
    **公式ワイン頁には点数が並ぶが、いずれも第三者媒体の記述である。本書は事実の典拠として採用していない。**
15. ⚠️ **オーナーシップを断定しない。**
    **生産者ドメイン上で確認できるのは「Otsuka Group に属する」ことまで（社員向け頁と Otsuka Group の
    Business Partner Code of Ethics）。出資比率も取得年も公式には書かれていない。**
16. ⚠️ **『1962 年創業の畑』と言わない。**
    **1962 年はワイナリー再登録・初商業リリースの年。畑と蔵は 1885〜1892 年、禁酒法で放棄され、
    1940 年代後半に William Short が植え直している。この 3 つを混ぜない。**

---

## Akio's Insight

🖋 （この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **canonical（`migration/`）も `research/canonical_conflicts/REGISTER.md` も一切変更していない。**
🔒 **以下はすべて escalate であり、実行はしていない。**

---

### 🔴 ① **gap —— 3 行に対して canonical レコードは 1 件。2 行は当てる先が存在しない。**

1. **衝突する canonical ID**: 🔴 **無い（これは衝突ではなく不在である）。**
   🔍 **canonical 全 928 レコードを機械走査し、`producer` フィールドが `Ridge Vineyards` のレコードが
   `ridge-monte-bello` の 1 件のみであることを実測した。文字列 `Geyserville` は canonical に 0 件。**
2. **なぜ重複に見えるか**: 🔴 **見えない。**行 1（Estate Cabernet）と行 3（Geyserville Vineyard）は
   `cuvee_state: unresolved` で、intake の evidence が
   「`'Ridge Vineyards'` の canonical キュヴェ 1 件に一致無し」と正しく記録している。
3. **証拠**: 🔍 **intake の 3 行すべてで `proposed_canonical_cuvee_id` が
   行 1 = `null`、行 3 = `null`、行 2 のみ `cuvee:ridge-vineyards-monte-bello`。**
   ✅ **一方、生産者側には 3 本とも公式製品頁・ラベル・技術仕様が完備している。**
4. **OBP への影響**: 🔴 **$300 と $175 の 2 本が canonical から見えない。合計 $475 分。**
   ⚠️ **さらに行 2 も `vintage='—'` の 1 レコードしか無いため 2022 に解決できない。実質 3 行とも未解決である。**
5. **推奨する解決（実行しない）**: 🔒 **`CDX-23`（gap は register に入れない、`unreachable` と分ける）の扱いに従う。
   本件は純粋な gap であり、`unreachable` ではない（Laurent-Perrier 型ではない）。**
6. **Confidence**: 🔴 **High**（機械走査＋公式一次資料の両方向で確定）

---

### 🔴 ② **`ridge-monte-bello` の記述が一次資料と合わない／出所が確認できない（5 点）**

1. **衝突する canonical ID**: 🔴 **`ridge-monte-bello`**
2. **なぜ重複に見えるか**: 🔴 **重複ではない。単一レコードの内容の問題である。**
3. **証拠**:

| # | canonical の記述 | 一次資料 | 判定 |
|---|---|---|---|
| **②-1** | 「**1976年「Judgment of Paris」で5位入賞、2006年30周年再戦では1位となった**」 | 🔴 ⚠️ **本調査で読んだ生産者著作の頁（About / History / Winemaking / Critical Acclaim / 畑頁 / ラベル解説 / 該当ワイン頁）に、この順位を造り手自身が述べた記述が 1 件も無い。**`/about/news/` は第三者媒体の引用集である | 🔴 **出所不明。造り手の言葉ではない。卓上に流れると造り手が語っていない主張を語ることになる** |
| **②-2** | 「**Santa Cruz Mountains の標高400-790m自家畑**」 | 🔴 ✅ **公式：「**The Monte Bello vineyard ranges in elevation from 1300′ to 2700′ above sea level**」（約 396〜823 m）** | ⚠️ **上限が食い違う（790 m vs 823 m）。下限はほぼ一致** |
| **②-3** | 「**Paul Draper（醸造責任者として2016年退任までほぼ50年）**」 | 🔴 ✅ **公式頁は `Paul Draper - Winemaker Emeritus / Joined Ridge in 1969` のみ。退任年の記載が無い。**✅ **現 Head Winemaker は 2021 年就任の John Olney** | ⚠️ **退任年が公式で裏づけられない** |
| **②-4** | `classification` = 「**Santa Cruz Mountains Bordeaux Blend**」 | 🔴 ✅ **フロントラベルの Top Block は `RIDGE / 2022 / MONTE BELLO` のみで、classification に当たる語が無い。**✅ **`Bordeaux blend` は造り手が畑頁の散文で用いる表現（「the finest domestic example of a classic Bordeaux blend」）であって、ラベル上の class/type ではない** | ⚠️ **属性の出所（attribute provenance）の形。`CDX-16` と同型。番号は開かない** |
| **②-5** | `obp_note` = 「**市場価格 $300〜$450/btl**」／`tags` に `$300-500` | 🔍 **OBP 行 2 は `$990`** | ⚠️ **帯を完全に外れている。市場価格を canonical に静的に持つこと自体の設計問題（Montelena で報告済みの形と同型）** |

4. **OBP への影響**: 🔴 **②-1 は最も重い。canonical から staff 表示に流れると、
   造り手が公表していない順位を $990 のボトルの説明として語ることになる。**
   ②-4 は `classification` を UI が「格付け」として表示する場合に、存在しない格付けを示すことになる。
5. **推奨する解決（実行しない）**: 🔒 **`CDX-5`（canonical 格納値が生産者公式と矛盾する）の族に属する。
   ②-4 は `CDX-16`（属性の出所）の族。いずれも新番号は開かない。**
6. **Confidence**: 🔴 **High**（②-2〜②-5）／⚠️ **Medium-High**（②-1 —— 「読んだ範囲に無い」は
   「存在しない」ではない。生産者サイトは 559 頁あり、全頁は読んでいない）

---

### ⚠️ ③ **既存の族に該当するもの（新しい番号は開かない）**

- ⚠️ **`CDX-2`** —— 🔍 **行 2 は `cuvee_state: exact` でありながら evidence が
  「canonical の 'Monte Bello' に vintage 2022 無し（保有: ゼロ件）」。`exact` は同定の強さではない。**（1 行で記録、深追いしない）
- ⚠️ **`CDX-15`** —— 🔍 **行 3 の `_parts.varietal = "proprietary blend"`。
  ラベルにも公式サイトにも存在しない語であり、メニュー側のカテゴリー語である。**
  🔴 **ただし行 1 の `'Estate,'` は同じ型ではない（ラベル Top Block に実在する指定語）。
  `NEXT_ACTIONS.md` §3f-10 の「パターンの存在は個々の行の証拠ではない」がそのまま当たった事例として記録する。**
- ⚠️ **`CDX-20`** —— 🔍 **行 1・2 で matcher が `Santa Cruz Mountains Cabernet Sauvignon` を
  `appellation='santa cruz mountains'` ＋ `varietal='cabernet sauvignon'` に分解している。
  🔴 本生産者ではその文字列が実在の製品名（`2023 / 2024 Santa Cruz Mountains Cabernet Sauvignon`）でもあり、
  かつ同一ヴィンテージに別製品（`Estate Cabernet Sauvignon`）が併存する。**
- ⚠️ **`CDX-23`** —— **本件の行 1・3 は純粋な gap であり `unreachable` ではない。**
- ⚠️ **`CDX-9`（生産者名の部分一致）** —— 🔍 **OBP 704 行の走査で、文字列 `Ridge` は
  `Turley` の `'Rattlesnake Ridge,' Howell Mountain Zinfandel`（`obp-beverage-2026-08:4c8a44755d`）にも現れる。
  canonical 側にも `switchback-ridge-peterson`（生産者 `Switchback Ridge`）と、
  `mt-eden-estate-cab` の説明文中の `Ridge Monte Bello` への言及がある。**
  🔴 **本書はすべて `producer` フィールドの完全一致（`Ridge Vineyards`）で判定し、部分一致は使っていない。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY / `D-2026-08-05-09`**）

🔴 **本ブリーフは候補ドメインを名指ししていない。以下は本調査が自力で特定し、検証した結果である。**

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の運営者名** | ✅ 🔴 **合格。**`https://www.ridgewine.com/policies/privacy-policy/` 冒頭に「**This Privacy Policy (“Policy”) describes how Ridge Vineyards, Inc. and its affiliate and related entities … collects, uses, discloses, and retains personal information about visitors to our website, www.ridgewine.com (the “Site”)**」と明記 |
| **(b) 非関連の免責表示が無い** | ✅ **合格。**「ファンサイト」「非公式」の類の表記は無い。**全ページ末尾は `© 2026 RIDGE VINEYARDS`** |
| **(c) 公的資料と一致する所在** | ✅ 🏛 🔴 **合格（本ドシエで最も強い検証）。**<br>**Privacy Policy の Contact Us が `Postal address: P.O. Box 1810, Cupertino, CA 95015`。**<br>🏛 **USDA NOP 認証書 `23-0793` の宛名が `RIDGE VINEYARDS, INC., P.O. BOX 1810, CUPERTINO, CALIFORNIA, 95015` —— 完全一致。**<br>**さらに Contact 頁の `17100 Montebello Road, Cupertino, CA 95014-5435` が、3 本のフロントラベル下部の印字（`17100 MONTEBELLO ROAD/RD, CUPERTINO, CALIFORNIA 95014`）および NOP 対象地一覧の `Middle Vineyard (Torre): Sites 01, 07 - 17100 Montebello Road` と一致する** |
| **(d) 商業・法務フッターの整合** | ✅ **合格。**`/policies/` に Privacy Policy / Shipping Policy / Return Policy / Accessibility Statement / **Business Partner Code of Ethics** / **Integrity Hotline** が揃う。Cookie Settings、CCPA 選択肢、会員ログイン、実在する EC 導線あり |
| **年齢ゲート** | ✅ **静的取得では年齢ゲートに掛からなかった**（`robots.txt` / sitemap / ワイン頁 / PDF / 画像すべて直接取得できた） |
| **bot 検出の兆候** | **無し。**`www.ridgewine.com` 側の CAPTCHA・チャレンジには一度も遭遇していない |

🔴 **本調査で `NOT_THE_PRODUCER_*` として退けたサイトは無い。**
（**WebSearch は URL 候補の発見にのみ用い、検索結果の要約文は事実として一切採用していない。**
**Wikipedia は検索結果に出現したが、規約どおり開いておらず、参照もしていない。**）
🔴 **生産者ドメイン外の資料は本書では 1 件も事実の典拠に使っていない（`📄` 0 件、`IMPORTER_*` 0 件）。**

### 一次資料（**`www.ridgewine.com` および同ドメイン配信の公式 PDF・公式画像**）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt` → `sitemap_index.xml`** | **子サイトマップ 15 本。WordPress + Yoast SEO 構成** |
| **`page-sitemap.xml`（559 URL）/ `wine-sitemap.xml` + `wine-sitemap2.xml`（1,134 URL）/ `vineyard-sitemap.xml`（44 URL）/ `news_item-sitemap.xml`** | **ラインナップ・ヴィンテージ範囲・畑の全体像を機械的に確定** |
| 🔴 **`/wines/2022-monte-bello/`** | 🔴 **OBP 行 2。**86% CS / 10% Merlot / 2% PV / 2% CF・13.8%・収穫 9/13–10/10・Brix 23.6°・TA 9.13・pH 3.36・**新樽 100%（American 95% / French 5%）・樽 21 か月・31 ロット中 18 ロットをブラインド選抜**・`Organically Grown`・ワインメーカーノート・ヴィンテージノート・History |
| 🔴 **`/wines/2023-estate-cabernet-sauvignon/`** | 🔴 **OBP 行 1。**75% CS / 19% Merlot / 3% CF / 3% PV・13.4%・収穫 9/9–10/5・Brix 23.4°・TA 7.2・pH 3.41・**American oak 新樽 55%・樽 17 か月**・`Organically Grown`・**「With the 2008 vintage, the name of this stylistically distinct wine became the Ridge Estate Cabernet Sauvignon」** |
| 🔴 **`/wines/2024-geyserville-vineyard/`** | 🔴 **OBP 行 3。**71% Zinfandel / 19% Carignane / 8% Petite Sirah / 2% Alicante Bouschet・14.6%・Brix 24.7°・TA 5.2・pH 3.68・**American oak 新樽 15%・樽 16 か月**・`Organically Grown`・**🔴「We added “vineyard” to the front label in 2024 to differentiate the historic Geyserville Vineyard from the town of Geyserville.」** |
| 🔴 **`/wines/2023-santa-cruz-mountains-cabernet-sauvignon/`** | 🔴 **取り違え先の実体確認。**81% CS / 15% Merlot / 4% PV・13.2%・畑 = Bates Ranch, Fellom Ranch, Monte Bello, Vidovich Vineyards・**`Organically Grown` の表示なし**・**「In 2023 we had the opportunity to purchase grapes from outside growers…」** |
| 🔴 **`/about/news/a-deep-dive-into-the-ridge-label/`** | 🔴 **本ドシエの中核。**Top Block / Bottom Block の逐条説明、`Estate` の定義、`Grape Variety` の 75% 条件、`Vineyard Name` の 95% 条件、`Proprietary Name` の扱い、生産表示（`Grown, Produced, and Bottled by` と `Produced and Bottled by` の違い）、裏ラベルの成分表の全項目、1964 年の Jim Robertson によるラベル設計、`Monte Bello` 商標の経緯 |
| 🔴 **`/about/sustainability/organic-certification/`** | 🔴 **有機の年表（2008 / 2011 / 2014 / 2015 / 2021 / 2022）、認証プロセスの説明、`organically grown` 表示の条件、証書 PDF 2 点へのリンク** |
| 🔴 **`/wp-content/uploads/2024/04/RIDGE-VINEYARDS-INC.-23-0793-CERTIFICATE-OF-ORGANIC-PRODUCTION-NOP.pdf`** | 🏛 🔴 **NOP 証書本体。**証書番号 `23-0793`／初回発効 `09/03/2011`／発行 `09/06/2023`／更新 `09/03/2024`／Product `100% Organic Wine Grapes`／**認証機関 `Organic Certifiers`（レターヘッド画像から実読）／署名 `Susan D. Siple, Executive Director`** |
| 🔴 **`/wp-content/uploads/2024/04/RIDGE-VINEYARDS-INC.-23-0793-SITE-ATTACHED-LIST-NOP.pdf`** | 🏛 🔴 **対象地一覧（住所・面積つき 12 区画）。**Monte Bello 系 6 区画（Jimsomare/Klein 57.60、Middle/Torre 34.80、Rousten/Ortmann 28.40、Upper/Perrone 26.50、Asiago 5.00、Jensen/Douglas Crest 1.25）、Geyserville 系 3 区画（Whitton 32.80、Fredson 14.60、Trentadue 3.74）、Lytton 系 2 区画（West 158.40、East 39.80）、Funsten Ranch 20.40 |
| 🔴 **公式ボトルショット画像** `22CMB-web.png` / `23CRE-web2.png` / `24ZGY-web2.png` | 🔴 **フロントラベル実読（拡大して逐語転記）。**Top Block と Bottom Block の全行 |
| ✅ **`/about/history/`** | **1885 Osea Perrone / 1892 初ヴィンテージ / 禁酒法 / 1940 年代 William Short / 1959・1962 の 4 人 / 1964 初ジンファンデル / 1966 初 Geyserville / 1969 Paul Draper / 1991 Lytton Springs** |
| ✅ **`/about/`** | **`single-vineyard` / `pre-industrial` / `transparency` / `Organic & Sustainable` の 4 本柱** |
| ✅ **`/about/winemaking/`** | **John Olney の経歴（1996 入社 / 2021 Head Winemaker & COO / 2026 CEO）、醸造チーム、pre-industrial の 4 原則、Paul Draper の「the wine glass」** |
| ✅ **`/about/explore/paul-draper/`** | **`Paul Draper - Winemaker Emeritus / Joined Ridge in 1969`。退任年の記載は無い** |
| ✅ **`/about/sustainability/our-farming-philosophy/`** | **2008 年からの有機移行、投入資材の抑制、隔畝耕耘、自家堆肥、pre-industrial との接続** |
| ✅ **`/about/explore/ingredient-labeling/` ＋ `/whats-in-a-wine/`** | **成分表を載せる理由、TTB 承認添加物・工程への造り手の立場、10 項目の成分の定義、Paul Draper 署名のエッセイ** |
| ✅ **`/vineyards/monte-bello/`** | **標高 1300′–2700′、石灰岩とグリーンストーン、太平洋から 15 マイル、収量 2 t/acre 未満、`100% of our Monte Bello Vineyard has been certified organic since harvest 2022`、Bordeaux blend の品種寄与** |
| ✅ **`/vineyards/geyserville/`** | **Alexander Valley Estate、`Old Patch` の 130 年超の樹、field blend、砂礫ローム＋川石、Geyserville の南 3 マイル、Trentadue 家との関係** |
| ✅ **`/policies/` / `/policies/privacy-policy/` / `/contact/`** | **真正性の検証。運営法人名・郵送先・ワイナリー住所・電話・FAX** |
| ✅ **`/about/critical-acclaim/`** | ⚠️ **第三者引用集。事実の典拠としては採用していない**（`America's First Growth` 等の表現はすべて第三者の言葉である） |
| ✅ **サイト内検索 `/?s=Otsuka`** | ✅ **`Otsuka Employee Gift` 頁と `Otsuka Group Business Partner Code of Ethics`。企業グループ帰属の唯一の生産者側証拠** |

### 🏛 公的登録簿・規制一次資料

| 資料 | 取得した情報 |
|---|---|
| 🏛 **eCFR 27 CFR § 9.31（`Santa Cruz Mountains`）** | **AVA の名称規定、承認地形図 24 葉（`Cupertino Quadrangle` を含む）** |
| 🏛 **eCFR 27 CFR § 9.53（`Alexander Valley`）** | **AVA の名称規定、「located in northeastern Sonoma County, California」、承認地形図 7 葉（`Geyserville Quadrangle` を含む）、境界の全記述** |
| 🔴 🏛 **eCFR 27 CFR § 4.23（`Varietal (grape type) labeling`）** | 🔴 **(b) 単一品種表示の 75% 要件の全文、(a) appellation of origin の併記義務、(d) 複数品種表示の要件** |
| 🔴 🏛 **eCFR 27 CFR § 4.26（`Estate bottled`）** | 🔴 **(a) 3 要件の全文、(c) `Controlled by` の定義（3 年以上のリース等）、(d)「No term other than Estate bottled may be used on a label to indicate combined growing and bottling conditions」** |
| 🏛 **eCFR title-27 structure API** | **`Santa Cruz Mountains` = § 9.31、`Alexander Valley` = § 9.53 の同定（節番号を推測せず機械的に確定した）** |
| 🔴 🏛 **USDA NOP 証書 `23-0793` ＋ 対象地一覧** | **上記（生産者ドメイン配信）** |

### 取得できなかったもの / 読めなかったもの

- 🔴 ⚠️ **🏛 TTB Public COLA Registry が CAPTCHA でゲートされていた。**
  **`https://ttbonline.gov/colasonline/publicSearchColasBasic.do` は F5/Shape 系 bot 防御（`bobcmn` / `TSPD_101`）を返し、
  ページ内に `captcha_audio` が実在した。突破は試みていない。**
  → **本書は TTB 承認ラベルの記録（brand name / fanciful name / class-type / 表示産地 / 承認日）を 1 件も持たない。**
  → **⚠️ ゲートは「ラベルが存在しない」ことの証拠ではない。**
- 🔴 **裏ラベル画像を 1 枚も取得できていない。**成分表の実文言、`ESTATE BOTTLED` の有無、
  政府警告文、Monte Bello の選抜量（トン数・エーカー数）が未確認。
- ⚠️ **🏛 USDA Organic INTEGRITY データベースは読めなかった。**
  `https://organic.ams.usda.gov/integrity/` は Blazor の JS シェルのみを返し、
  `POST /integrity/api/OperationSearch` は `400`。**（Batch 9・Montelena と同じ所見が再現した。）**
  → 🔴 **ただし本生産者では、認証機関発行の証書そのものが生産者ドメインで読めたため、実害は無い。**
- ⚠️ **認証機関 `Organic Certifiers` 側の顧客名簿（`organiccertifiers.com/clients/`）は `404`。**独立照合はできていない。
- ⚠️ **蔵出し価格を取得できなかった。**EC の価格が静的 HTML に出ず、JS 描画である。
  → **本書は蔵出し価格・倍率を一切主張しない。**
- ⚠️ **`Otsuka Group` の出資比率・取得年が公式サイトに書かれていない。**
- ⚠️ **1976 年の試飲会・2006 年の再戦について、造り手自身の記述を見つけられなかった。**
  **`/about/news/` の該当項目はいずれも第三者媒体の引用である。**
  ⚠️ **サイトは 559 頁あり全頁は読んでいない。「読んだ範囲に無い」であって「存在しない」ではない。**
- ⚠️ **`Monte Bello` 商標を Ridge が取得した年が書かれていない。**
- ⚠️ **Monte Bello 畑の総エーカー数を造り手が述べた記述が無い。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical: `migration/out/export/db_wine_canonical.json`（928 レコード）を機械走査。
`producer == 'Ridge Vineyards'` は `ridge-monte-bello` の 1 件のみ。**
🔍 **⚠️ 部分一致は使っていない（`D-2026-08-05-08` / `CDX-9`）。文字列 `Ridge` を含むレコードには
`switchback-ridge-peterson`（別生産者 `Switchback Ridge`）、`mt-eden-estate-cab`（説明文中の言及）、
`dehlinger-goldridge`（`Goldridge` 土壌）などが含まれる。**
🔍 **OBP: `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）に 3 行。
`source_row_id` = `obp-beverage-2026-08:43436ec6c8` / `:f70b019945` / `:717413779c`。
3 行すべて `match_state = unresolved`・`confidence = 0.0`・`producer_state = exact`・`source_quality_flags = []`。**
🔍 **⚠️ 同ファイル内で `Ridge` を含む別生産者の行が 1 件ある：`Turley` の
`'Rattlesnake Ridge,' Howell Mountain Zinfandel`（`obp-beverage-2026-08:4c8a44755d`）。本書とは無関係である。**
⚠️ **本書の「解決済み件数」はすべて `obp_intake_normalized_20260804.json` から取ったものであり、
`research/out/t-01/mapping.json` は参照していない**（両者が食い違うことは既知のため、出所を明記する。`CDX-4`）。
🔒 **canonical・`REGISTER.md`・intake のいずれも編集していない。**

---

## Confidence

```
reached_70: YES (~85%)
confidence: High
```

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | 🔴 **法人名が Privacy Policy と 🏛 NOP 証書の双方で `Ridge Vineyards, Inc.` と一致。郵送先も完全一致。ワイナリー住所がラベル現物・Contact 頁・NOP 対象地一覧の 3 経路で一致。CEO・Winemaker Emeritus・醸造チームの氏名と就任年が公式で確定**<br>⚠️ **Otsuka Group の出資構造のみ不明** |
| **Overview** | **High** | **蔵の自己規定（single-vineyard / pre-industrial / transparency / organic）がすべて公式の言葉で取れた** |
| 🔴 **History** | 🔴 **High** | 🔴 **1885 / 1892 / 禁酒法 / 1940 年代 / 1959 / 1962 / 1964 / 1966 / 1969 / 1991 / 2008 / 2011 / 2021 / 2023 / 2024 / 2026 がすべて公式頁で確定。**⚠️ **`Monte Bello` 商標取得年のみ不明** |
| 🔴 **Location** | 🔴 **High** | 🏛 **2 つの AVA が 27 CFR § 9.31 / § 9.53 で確定。**🔴 **Monte Bello の標高・土壌・海からの距離・収量、Geyserville の構成・土壌・樹齢・起源がすべて公式で確定。**🏛 **区画名と面積が NOP 対象地一覧で裏づけられた**<br>❓ **畑の総面積・植樹年・台木は不明** |
| 🔴 **Farming** | 🔴 **High —— 本ドシエ最大の強み** | 🔴 **認証書そのもの（証書番号・初回発効日・認証機関・署名者・対象地・面積）が読めている。年表で「どの畑がいつから」まで確定し、OBP 3 ヴィンテージすべてが射程内であることを 1 本ずつ確認した。**⚠️ **有機以外の 4 つの枠組みは一次文書未取得のため封じた** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **OBP 3 本すべてでセパージュ・アルコール・収穫日・Brix / TA / pH・発酵方式・樽（材・新樽率・樽齢構成）・熟成月数・選抜方法・成分表が確定。**⚠️ **裏ラベル現物の文言のみ未確認** |
| 🔴 **Style** | 🔴 **High** | 🔴 **3 本すべてに醸造家署名つき公式ノート。3 年分のヴィンテージノートと Growing Season 欄（雨量・開花期・天候）も取得。**⚠️ **2024 の収穫日に頁内矛盾があり、そこだけ封じた** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **3 行すべてについて、公式製品名・フロントラベル逐語・技術仕様が確定。さらに造り手自身のラベル文法文書により、`Estate` / `Monte Bello` / `Geyserville Vineyard` / `Proprietary Blend` の 4 語それぞれの身分を判定できた。行 1 の取り違え先（2023 Santa Cruz Mountains Cabernet）も実体確認済み**<br>⚠️ **蔵出し価格のみ取得できず** |
| **Canonical Conflict** | 🔴 **High** | 🔴 **gap は 928 レコードの機械走査で確定。記述の矛盾 5 点のうち 4 点は公式一次資料との直接照合。**⚠️ **②-1（1976 / 2006 の順位）のみ「読んだ範囲に無い」という消極的証拠** |
| **Staff Notes** | 🔴 **High** | ⚠️ **16 項目。🔴「Geyserville Vineyard は表記ゆれ」「Estate と Santa Cruz Mountains の取り違え」「Monte Bello のラベルにカベルネと書いてある」「オーガニックワイン」「1976 年 5 位・2006 年 1 位」「Draper 2016 年退任」「Estate Bottled」「ほぼ全部カベルネ」の 8 つの誤りを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を大きく超過。実感としては 85% 前後）。** | **OBP 3 本すべてについて、公式製品名・ラベルの全文・セパージュ・分析値・樽・熟成・造り手のノート・年の性格・畑・有機認証の射程を言える。産地は連邦規則まで、栽培は認証書まで遡って言える。**<br>🔴 **欠けているのは ① 裏ラベル現物 ② TTB COLA 記録 ③ 蔵出し価格 ④ 1976/2006 の造り手による記述 ⑤ Otsuka の出資構造。**<br>**いずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。** |

---

## Open Questions

1. 🔴 **OBP 3 本の裏ラベル現物（実ボトル案件）。**
   🔴 **Ridge の裏ラベルは 2011 年以降、成分表・生産量（Monte Bello は選抜のトン数とエーカー数）・
   醸造家の記述を載せる。この蔵を語る最大の武器であり、本書はそれを 1 枚も読めていない。**
   **確認すべき点：① 成分表の実際の文言（`minimum effective` が現在も使われているか）
   ② `ESTATE BOTTLED` の 2 語の有無 ③ Monte Bello の選抜量 ④ アレルゲン表示（`Contains Egg` の有無）。**
2. 🔴 **🏛 TTB COLA の再試行。**
   **本調査では CAPTCHA でゲートされた。開けば brand name / fanciful name / class-type / 表示産地 /
   承認日が確定し、Open Question 1 と行 2・3 の class/type 問題に直接の答えが出る。**
   **⚠️ 同一バッチ内でも生産者によって開閉が変わるため、日を改めた再試行に価値がある。**
3. 🔴 **1976 年の試飲会と 2006 年の再戦について、造り手自身の記述が存在するか。**
   **canonical は具体的な順位（5 位／1 位）を主張しているが、本調査で読んだ生産者著作の頁には無かった。**
   ⚠️ **`page-sitemap.xml` は 559 URL あり、全頁は読んでいない。「無い」と断定してはならない。**
   → **蔵への直接照会、または残りの公式頁の網羅的走査が要る。**
4. ⚠️ **蔵出し価格。**
   **EC の価格が JS 描画で静的取得できなかった。$300 / $990 / $175 の位置づけを語る材料が無い。**
5. ⚠️ **`Monte Bello` 商標を Ridge が取得した年。**
   **公式は「1962 年当時は Perrone の Montebello Wine Company の法人上の後継者が握っていた」「数年後に Ridge が取得した」
   とだけ書き、年を書いていない。**
6. ⚠️ **`Otsuka Group` との資本関係。**
   **生産者ドメイン上で確認できるのは帰属の事実のみ。出資比率・取得年・意思決定への関与は公表されていない。**
7. ⚠️ **`Geyserville` の「three adjoining vineyards」と NOP 対象地一覧の 3 区画（Fredson / Whitton / Trentadue）の対応。**
   **住所（Geyserville Avenue）の一致から本書は「対応する」と観察したが、造り手が明示的に対応づけた記述は無い。**
8. ⚠️ **2024 Geyserville の収穫日の頁内矛盾。**
   **ヴィンテージノート（8/30–9/14）と Winemaking 欄（9/2–10/9）が食い違う。造り手への照会案件。**
9. ⚠️ **canonical に載せるときの `name` をどれにするか。**
   **行 1 は公式製品名 `Estate Cabernet Sauvignon` だが、2008 年より前の同じワインは `Santa Cruz Mountains` を名乗り、
   2023 年からは別のワインがその名を取り戻している。行 3 は 2023 年まで `Geyserville`、2024 年から `Geyserville Vineyard`。**
   🔴 **すなわち本生産者では「キュヴェ名がヴィンテージによって変わる」。`cuvée × vintage` の粒度が要る。**
   → 🔒 **設計判断であり本書では決めない。**
10. ⚠️ **canonical `ridge-monte-bello` の `vintage = '—'` の扱い。**
    🔴 **Ridge は Monte Bello だけで 1962 年以降 60 を超えるヴィンテージを公式頁に持つ。
    粒度が無ければ OBP の 2022 を永久に解決できない。**
    → 🔒 **canonical への書き込みは本書では行っていない。昇格可否は Akio / CTO 判断。**
