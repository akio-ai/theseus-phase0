# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> **`reached_70: YES (~88%)` ／ confidence: High**
> 🔴 **canonical にこの生産者のレコードは 1 件だけ存在する**（`ch-margaux-1855`、`vintage='—'`）。
> **本書は昇格前の研究記録であり、canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式サイト `chateau-margaux.com` で確認**（一次資料）
> `🏛` **公的登記・法定文書**（INAO cahier des charges ／ `recherche-entreprises.api.gouv.fr` ／ Agence Bio ／ Ecocert）
> `📄` 生産者自身の旧ページを Internet Archive から復元（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: ✅ **`https://chateau-margaux.com/`**
> 走査元: ✅ **`robots.txt` → `sitemap.xml`（sitemapindex）→ `sitemap_en.xml` = 358 URL / `sitemap_fr-FR.xml`**
> **うち `/vins/` 配下が 251 URL。グラン・ヴァンは 1900〜2025 の全年に個別ページを持つ（127 ページ）**
> 併用: 🏛 **INAO CDC「Margaux」PDF 2 版**（`PNOCDCMargaux.pdf` 2010 / `3-CDC-Margaux.pdf` 2022）
> 　　　🏛 **`recherche-entreprises.api.gouv.fr`（SIREN 321152993）** ／ 🏛 **Agence Bio（exact SIRET）** ／ 🏛 **Ecocert**
>
> ---
>
> 🔴 **① 本ドシエ最大の収穫 —— 農法。Agence Bio の exact-SIRET 照会が「有機転換中」を返した。
> 　　だが `datePremierEngagement` は **2023-07-18**。**OBP 8 本のヴィンテージは 1995〜2019 で、全部これより前である。**
> 　　しかも現在の状態は `ENGAGEE` / `C1`（転換 1 年目）であって認証取得済みですらない。
> 　　→ **8 本すべてについて「オーガニック」とも「オーガニックでない」とも言えない。** → §Farming / §Canonical Conflict
>
> 🔴 **② `Margaux` という文字列は、この生産者において 5 つの別のものを同時に指す。**
> 　　**AOC 名 ／ コミューン名（現 Margaux-Cantenac）／ シャトー名 ／ グラン・ヴァンの通称 ／
> 　　そしてサードワインの正式名 `Margaux du Château Margaux`（2009 年〜）。**
> 　　**OBP 8 行はすべて `source_wine_raw = "Margaux"` しか印字していない。**
> 　　→ **印字文字列だけでは、グラン・ヴァン／セカンド／サードのどれかを原理的に決められない。** → §Important Cuvées
>
> 🔴 **③ 白 `Pavillon Blanc du Château Margaux` は AOC Margaux ではない —— 法定文書で確定した。**
> 　　🏛 INAO CDC 第 I 章 III 節: 「**L'appellation d'origine contrôlée « Margaux » est réservée aux vins tranquilles rouges.**」
> 　　**2010 年版・2022 年版の両方が同一文言。この条項は取消線・太字のどちらでもない**（§2c の罠に該当しない）。
>
> 🔴 **④ 2015 年（OBP 3 行目・$6,890）は、公式に「紙ラベルが無い」ヴィンテージである。**
> 　　✅ 「**A unique case was designed and adorned with a magnificent screen print, specially conceived for this vintage,
> 　　and affixed directly to the glass in place of the usual labels.**」
> 　　→ **価格の説明はしない。だが「ラベルで同定する」という手順がこの 1 本だけ成立しない。** → §Open Questions 1
>
> 🔴 **⑤ canonical の格納値は、検証した 33 項目中 18 項目が公式と食い違った（contradicted 9 / unsourced 9）。**
> 　　**typed field にも及ぶ**（`serving_temp` / 栽培密度 / 作付面積）。→ §Canonical Conflict
>
> 🔴 **⑥ canonical にこの生産者のヴィンテージ・レコードは 0 件。OBP 8 本は全部 gap。**
> 　　**ただし「ボルドーの vintage 実体が canonical に構造的に無い」のではない —— Latour・Mouton・Haut-Brion には有る。**
> 　　**5 大シャトーのうち実体ボトルを 1 件も持たないのは Lafite と Château Margaux の 2 つだけである。** → §Canonical Conflict

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`source_producer_raw = "Margaux"` ／ `source_wine_raw = "Margaux"`**（8 行すべて。**アペラシオン名のみでキュヴェ名が無い**） |
| **公式表記** | ✅ **Château Margaux**。グラン・ヴァンの正式名は ✅ **`Grand Vin du Château Margaux`** |
| 🔴 **法人** | 🏛 ✅ **SCA Château Margaux — Société en Commandite par Actions**<br>**資本金 208,680 €／RCS Bordeaux `321 152 993`** |
| 🔴 **SIREN / SIRET** | 🏛 **SIREN `321152993` ／ SIRET（siège）`32115299300010`**<br>**公式 mentions légales の記載と `recherche-entreprises.api.gouv.fr` の返り値が完全一致** → §2a 認証成立 |
| **TVA** | ✅ **`FR 89 321 152 993`**（mentions légales） |
| **NAF / APE** | 🏛 **`01.21Z`（Culture de la vigne）**／ NAF2025 `01.21Y` |
| **法人設立** | 🏛 **1976-12-21**（`date_creation`。⚠️ **これは登記上の法人設立日であって、シャトーの創業年ではない**） |
| **所在** | 🏛 ✅ **Domaine de Château Margaux, 33460 Margaux — FRANCE**<br>🏛 登記上の commune 表記は **`MARGAUX-CANTENAC`**（INSEE code `33268`）。**公式サイトは旧表記 `33460 Margaux` のまま** |
| **電話** | ✅ 🏛 **+33 (0)5 57 88 83 83**（公式・Agence Bio 双方で一致） |
| 🔴 **代表者** | ✅ 🏛 **Alexis Leven-Mentzelopoulos** — **Co-owner & CEO**。**2023 年末に CEO 就任**<br>**mentions légales は「Co-owner and Managing Partner（gérant commandité）」として掲載責任者に指名**<br>**RNE の `dirigeants` も `Gérant: LEVEN-MENTZELOPOULOS ALEXIS JOSEPH`（1993 年生）で一致** |
| 🔴 **共同オーナー** | ✅ **Alexandra Petit-Mentzelopoulos** — **Co-owner & President of the Supervisory Board of the holding company** |
| **Managing Director** | ✅ **Philippe Bascaules** |
| **醸造・栽培統括** | ✅ **Benjamin Vimal（Director of Winemaking and Estate Operations）** |
| **副 MD** | ✅ **Aurélien Valance（Deputy Managing Director, Sales and Operations）** |
| **R&D** | ✅ **Blandine de Rouffignac（PhD in Oenology、2018 年 1 月入社）**。**R&D 部門は 2000 年設立**、**Jérôme Godineau（2011 年〜）が補佐** |
| **世代** | ✅ **Alexis は「祖父 André、母 Corinne に次ぐ、当主として第 3 世代」** |
| 🔴 **有機登録** | 🏛 **Agence Bio `numeroBio = 55044`／認証機関 Ecocert France（`FR-BIO-01`）／`etatCertification = ENGAGEE`／`datePremierEngagement = 2023-07-18`** → §Farming |
| **canonical id** | 🔍 **`ch-margaux-1855` 1 件のみ（`vintage='—'`）。ヴィンテージ実体は 0 件** |

### ⚠️ 同名の別物（**必ず SIREN で切ること**）

🔴 **`Margaux` は Bordeaux で最も危険な文字列の一つである。**

| 種別 | 実体 | 切り方 |
|---|---|---|
| **AOC** | 🏛 **AOC Margaux**（1954 年 8 月 10 日の décret で認定）。**Arsac / Cantenac / Labarde / Margaux-Cantenac / Soussans の 5 コミューン** | アペラシオンであってシャトーではない |
| **コミューン** | 🏛 **Margaux-Cantenac**（INSEE `33268`）。🔴 **2010 年版 CDC は `Margaux`、2022 年版 CDC は `Margaux-Cantenac` と書く —— 法定文書の側でコミューン名が変わっている** | 地名であってシャトーではない |
| **サードワイン** | ✅ 🔴 **`Margaux du Château Margaux`** —— **この生産者自身のサードワインの正式名が `Margaux` で始まる** | §Important Cuvées |
| **同一 NAF・同一県の別法人** | 🏛 **`nom` に `margaux` を含み NAF `01.21Z`・Gironde の企業は 48 件**（実測）。うち **`SCEA DOMAINE DE L'ÎLE MARGAUX`（SIREN 348150376）** は **同じ Margaux-Cantenac に所在する別の生産者** | 🔴 **exact SIREN `321152993` 以外は全部別物** |
| **同コミューンの格付シャトー群** | 🏛 **Palmer（781863428）／Rauzan-Ségla（392694881）／Lascombes（344388848）／d'Issan（318415023）／Desmirail（388034134）／Marquis de Terme（781937289）… すべて `MARGAUX-CANTENAC` 所在** | 🔴 **住所が「Margaux-Cantenac」であることは、Château Margaux であることを一切意味しない** |

---

## Overview

✅ **メドックの中心、AOC Margaux。敷地 265 ヘクタール。うち赤ブドウの生産樹が約 87 ヘクタール、
白ブドウが 12 ヘクタール。残りは牧草地・森・庭園・歴史的建造物である。**
✅ **ボルドーから約 30 キロ。**

🔴 ✅ **公式が「265 ヘクタール」を 17 世紀末から変えていないと明言している。**
「**By the end of the seventeenth century, the estate extended to 265 hectares,
a surface area it has retained to this day, with approximately one third devoted to vines.**」

🔴 ✅ **1855 年格付についての生産者自身の記述**（`/en/le-domaine/histoire`）—
「**A blind tasting was organised in Paris. It resulted in the 1855 Classification,
which distributed around sixty Médoc growths, together with one growth from Graves,
into five levels of quality. Four properties were classified as "Premier Grand Cru Classé".
Château Margaux was the only one to obtain the maximum mark of twenty out of twenty.**」
⚠️ **「20/20 を得た唯一のシャトー」は生産者自身の主張であり、
本調査では格付を管理する団体側の文書でこの数値を確認していない。** → §Staff Notes ⚠️ ⑨

🔴 ✅ **現在の製品構成は 5 本 ＋ バルク販売の第 4 選抜である。**
公式は **`Pavillon Blanc Second Vin` を「五世紀で 5 本目に launch されたワイン」** と明記している —
「**Pavillon Blanc Second Vin is only the fifth wine to be launched by the estate in five centuries.**」
→ 🔴 **canonical はこれを 4 本として記録している。** → §Canonical Conflict

🔍 **THÉSEUS における状態は、Batch 11 で分類された 3 つの failure mode のうち
「absent as key」が最も純粋な形で出ているケース。
canonical にはこの生産者の実体ボトルが 1 本も無く、あるのは格付を符号化した殻 1 件だけ。
OBP 8 本は全部 `unresolved`。**

---

## History

✅ **公式沿革ページ（`/en/le-domaine/histoire`）は静的取得で本文が返る。以下はすべてそこからの引用である。**

| 年 | 出来事 ✅ |
|---|---|
| **12 世紀** | **「La Mothe de Margaux」として記録される。この時点では畑を持たない。**「**The name refers to a slight elevation in the land, a valuable feature in the Médoc, where the finest vineyard soils benefit from good drainage.**」 |
| **1152–1453** | **アキテーヌがイングランド統治下に。**リチャード獅子心王がボルドーを食卓のワインに |
| 🔴 **1572–1582** | 🔴 **Pierre de Lestonnac が所領と畑を全面的に再構築。**メドックが穀作からブドウへ移行するのを先取り |
| **17 世紀初** | 🔴 **執事 Berlon が決定的な役割。赤と白の別々の醸造を導入**（それ以前は混植混醸）。**早摘みを拒否**（「**because the grapes are covered with dew and, if they are picked in the morning, their colour will be diluted and faded by excess moisture**」）。**区画ごとの品種適性を見極め、テロワールの根本的役割を確立** |
| **17 世紀末** | 🔴 **敷地が 265 ヘクタールに到達。以後今日まで同じ面積** |
| **1705** | **London Gazette がボルドー・グラン・クリュの最初の競売を告知 —— 「Margose」230 樽** |
| **1771** | **1771 年産が Christie's のカタログに載った最初の「claret」** |
| **1784** | 🔴 **在仏米国大使 Thomas Jefferson が 1784 年産を注文。**「**there could be no better bottle of Bordeaux**」。**ボルドー大ワインの序列で Château Margaux を第 1 位に置いた** |
| **1801** | **Bertrand Douat, Marquis de La Colonilla が取得。現在のシャトーの建設を決める** |
| 🔴 **1810–1815** | 🔴 **建築家 Louis Combes が現在のシャトーを建設。**「**Versailles of the Médoc**」と呼ばれ、**フランスでは稀な新パラディオ様式**。**Colonilla は 1816 年に、一度も住まないまま没した** |
| **1836 以前** | **銀行家 Alexandre Aguado が取得（ボルドー大シャトーを買った最初の銀行家）。Rossini の後援者となり、Rossini は「Château Margaux」というサルスエラを作曲** |
| 🔴 **1855** | 🔴 **パリ万博に際し Napoléon III が公式格付を要請。ブラインド・テイスティングの結果が 1855 年格付。4 つが `Premier Grand Cru Classé`** |
| **1879** | **Emily Macdonnel が Count Pillet-Will に売却。オイディウム・ベト病・フィロキセラの時代** |
| **1893** | **著名な当たり年。**「**so abundant that the harvest had to be interrupted for six days due to the lack of available vats**」 |
| 🔴 **（フィロキセラ後）** | 🔴 **植え替え後の若木が最適な品質に達しないため、生産の一部を「second wine」として販売。**「**which would later take the name Pavillon Rouge du Château Margaux**」 |
| 🔴 **1906** | 🔴 ✅ **セカンドワインが `Pavillon Rouge du Château Margaux` の名になる。**公式ワインページ: 「**first named "Château - Margaux 2me vin", before becoming Pavillon Rouge du Château Margaux in 1906**」 |
| **1908** | 🔴 **Pierre Moreau が取りまとめた株主シンジケートが Château Margaux を購入。**🔴 **これは「所有者が変わった年」であって、Pavillon Rouge の命名年ではない** → §Canonical Conflict |
| **1920** | ✅ **白ワインが `Pavillon Blanc du Château Margaux` の名になる**（旧称 `Château - Margaux vin blanc sauvignon`） |
| **1925** | 🔴 **Pierre Moreau の最重要の革新 —— シャトー元詰めの義務化。**「**the requirement of bottling at the château, adopted in 1925 as a guarantee of authenticity**」 |
| **〜1950** | **Ginestet 一族が全体を取得**（Fernand と息子 Pierre） |
| **1972・1973・1974** | **壊滅的で売れない年が続き、1970 年代の不況と重なって Ginestet 家が窮地に** |
| 🔴 **1977** | 🔴 **André Mentzelopoulos が取得。**1915 年ギリシャ・パトラ生まれ。グルノーブルで文学を学び、ビルマ・中国・インド・パキスタンで穀物の輸出入により財を成し、**1958 年に Félix Potin を取得して 1,600 店舗の近代流通グループに育てた** |
| **1989** | ✅ 🔴 **ボトルへのレーザー刻印を開始**（真贋対策の先駆） → §Open Questions |
| 🔴 **1989–2015** | 🔴 ✅ **Paul Pontallier が Managing Director。**公式 2015 年ページ: 「**the final vintage overseen by Paul Pontallier, Managing Director of Château Margaux from 1989 to 2015**」 → §Canonical Conflict |
| **1997** | ✅ **瓶底にシャトーのエンボスを導入** |
| **2000** | ✅ **R&D 部門を設置** |
| **2011** | ✅ **Prooftag の Bubble Code を全ボトルに導入** |
| 🔴 **2015** | 🔴 ✅ **建物の 200 周年（1815 年建造）と、Norman Foster 設計の新施設の落成が重なった年**。**Pontallier の最後のヴィンテージ** |
| **2019** | ✅ **サステナビリティ専任職と行動計画を新設。**「**our sustainable development efforts were stepped up in 2019 with the creation of a dedicated role and an action plan**」 |
| 🔴 **2020** | ✅ **Alexis Leven-Mentzelopoulos が Business Development Director として入社** |
| **2022** | ✅ **`Pavillon Blanc Second Vin` を 2022 年産から瓶詰め開始（5 本目のワイン）** |
| 🔴 **2023-07-18** | 🏛 🔴 **Agence Bio への最初の登録（`datePremierEngagement`）。有機転換の起点** |
| 🔴 **2023 年末** | 🔴 ✅ **Alexis Leven-Mentzelopoulos が CEO に就任** |
| **2026** | ✅ **QR コード付きシールによる真贋確認システムを開始** |

---

## Location

| | |
|---|---|
| **Country** | France ✅🏛 |
| **Region** | **Bordeaux** ✅ |
| 🔴 **Appellation** | 🏛 ✅ **AOC Margaux。**公式 terroir ページ: 「**Located in the prestigious Margaux appellation (AOC Margaux), in the heart of the Médoc**」 |
| 🔴 **AOC の法定範囲** | 🏛 **1954 年 8 月 10 日の décret で認定。**現行版は **2023 年 3 月 31 日の arrêté（JORF 2023-04-05 / BO n°15 2023-04-13）で homologué**<br>🔴 **`L'appellation d'origine contrôlée « Margaux » est réservée aux vins tranquilles rouges.`（＝赤のスティルワイン専用）** |
| **AOC のコミューン** | 🏛 **Arsac, Cantenac, Labarde, Margaux-Cantenac, Soussans**（2022 年版）<br>⚠️ **2010 年版は `Margaux`。法定文書の側でコミューン名が変わっている** |
| **AOC の近接区域** | 🏛 **Arcins, Avensan, Lamarque, Ludon-Médoc, Macau, Le Pian-Médoc**（醸造・熟成の例外承認地域） |
| 🔴 **AOC の認可品種** | 🏛 **主要品種: cabernet franc N, cabernet-sauvignon N, carmenère N, cot N (malbec), merlot N, petit verdot N**<br>**適応目的の関心品種: castets N（作付の 5% 以下、INAO・ODG との協定を条件とする）** |
| **AOC の植栽密度下限** | 🏛 **7,000 pieds/ha 以上、畝間 1.50 m 以下、株間 0.80 m 以上**（2022 年版） |
| 🔴 **敷地** | ✅ **265 ヘクタール**（17 世紀末から不変） |
| 🔴 **生産樹面積** | ✅ 🔴 **赤 約 87 ヘクタール ＋ 白 12 ヘクタール**（「**around 87 hectares of red vines and 12 hectares of white vines in production**」） → §Canonical Conflict |
| 🔴 **区画** | ✅ **126 区画を精査してマッピング。うち 72 区画が Cabernet Sauvignon** |
| 🔴 **植栽密度** | ✅ 🔴 **6,666 〜 10,000 本/ha（土壌型と、樹勢・凝縮・果実品質の狙う均衡に応じて変える）** → §Canonical Conflict |
| **樹齢** | ✅ **赤は平均 35 年、最古は 1951 年植え（"The Cuvier"）。白（sauvignon blanc）は平均 50 年、最古は 1970 年植え** |
| 🔴 **地質** | ✅ **2 つの主要層 —— ①第三紀の石灰岩・粘土（古い海進の名残）②第四紀のガロンヌ河成段丘由来の砂利・砂・粘土。**<br>🔴 **深い砂利が優越し、とくに Margaux を象徴する「Type 4」段丘。**「**Their composition ensures optimal drainage and deep vine rooting, providing naturally regulated water supply.**」 |
| **気候** | ✅ **大西洋とジロンド河口の間の温暖な海洋性気候。近接する水塊が極端な暑さと霜から畑を守り、緩やかで均一な成熟をもたらす** |
| 🔴 **気候変動への対応** | ✅ **改植時に畝の向きを 45°〜60° NE/SW にして日焼けを減らす。加えて有機栽培への完全転換** |

❓ **公式に無い**: 区画ごとのヘクタール数、区画名の全体（`L'Enclos`・`Haut-du-Jardin`・`The Cuvier` の 3 つだけが名指しされている）、
グラン・ヴァンに使う区画の特定。

---

## Farming

🔴 **本節が本ドシエで最も重要である。そして最も誤用されやすい。**

### 🏛 Agence Bio —— **exact SIRET `32115299300010` で照会した結果（`nbTotal: 1`）**

| 項目 | 登録値 |
|---|---|
| **raisonSociale** | **SCA CHATEAU MARGAUX** |
| **numeroBio** | **55044** |
| **SIRET** | **32115299300010**（完全一致） |
| **codeNAF** | **01.21Z** |
| 🔴 **認証機関** | 🔴 **Ecocert France ／ `numeroControleEu = FR-BIO-01`** |
| 🔴 **etatCertification** | 🔴 **`ENGAGEE`**（＝**関与中。認証取得済みではない**） |
| 🔴 **datePremierEngagement** | 🔴 **2023-07-18** |
| **dateNotification** | **2023-07-07** |
| 🔴 **activites** | 🔴 **`Production` のみ。**（`Préparation` は無い） |
| **annuaireActivites** | **Viticulture** |
| 🔴 **productions / etatProduction** | 🔴 **`Raisin de cuve`（醸造用ブドウ、code 01.21.12）= `C1` と `AB` の両方**（`anneeReferenceControle: 2026`）<br>**`Jachère`（休閑地）= `C1`** |
| 🔴 **mixite** | 🔴 **`Oui`（＝有機と非有機が混在する経営体）** |
| **公式サイト登録** | **`https://www.chateau-margaux.com`（`typeSiteWeb: Site Officiel`）** → §2a の相互確認に使用 |
| **登録住所** | **`DOM DOMAINE DE CHATEAU MARGAUX` 33460 MARGAUX-CANTENAC（siège）／`RTE RAUZAN` 同市（活動地）** |
| **dateMaj** | **2024-04-10** |

### 🔴 温度差のある事実 —— 生産者自身の言葉

✅ **公式 terroir ページ（現在形）**:
「**This natural approach supports the vineyard's conversion to organic farming**」
「**completing its full conversion to organic farming**」
→ 🔴 **公式も「転換中／転換の完了」と書いており、「認証取得済みの有機」とは書いていない。登記と整合している。**

🔴 ✅ **2012 年ヴィンテージのページ（生産者自身が当時書いた文章）**:
「**this year we intensified our organic programme with great success:
not only have we not used any insecticide on the estate for 10 years,
but in 2012 we only used one chemical treatment, as opposed to the usual 7 or 8 on the great wine plots.
We're almost there…**」
→ 🔴 **殺虫剤の不使用は「2012 年の時点で 10 年間」＝およそ 2002 年以降である。** → §Canonical Conflict

### ✅ 公式が名指しする具体的な実務

- ✅ **草生**: 「**grass cover is carefully managed according to each plot**」。**`L'Enclos` 周辺とシャトー前面は恒久草生**（土壌保護・踏圧軽減）。**他の区画は土壌の典型性と品種に応じて調整**
- ✅ **カバークロップ**: **テロワールごとに設計し、毎年春前に鋤き込む。**「**maintain soil vitality, structure the earth, reduce erosion, stimulate microbial life, and increase organic matter … provide habitat for many species, including pollinators**」
- ✅ **堆肥**: **地域のパートナーシップで有機残渣を堆肥化し、区画に還元**
- ✅ **森林**: **ONF（フランス国有林野庁）と協働で生態調査＋野生動物調査を実施し、行動計画を策定。専任パートナーと林地を持続的に管理**
- ✅ **エネルギー**: 🔴 **電力は 100% 再生可能。**建物は順次改修して効率化。**定期的なカーボンフットプリント評価**
- ✅ **水**: **醸造タンク準備時の水を再利用し、工程を最適化して使用量を抑制**
- ✅ **機械・人**: **トラクターに燃費節約キットを装着。反復動作の負担を減らすため作業を多様化する労務設計**

### 🔴 温度的トラップ（§2e）—— **本ドシエで最も強い禁止事項**

| OBP ヴィンテージ | 有機登録（2023-07-18）との関係 |
|---|---|
| **1995 / 2005 / 2006 / 2010 / 2012 / 2015 / 2016 / 2019** | 🔴 **8 本すべてが `datePremierEngagement` より前。1 本の例外も無い** |

🔴 **したがって、この 8 本について「オーガニック」と言ってはならない。
　同時に「オーガニックではない」とも言ってはならない —— 登記が語るのは 2023 年以降の状態だけである。**
🔴 **さらに現在の状態ですら `ENGAGEE` / `C1`（転換 1 年目）であり、`mixite = Oui`（混在経営）である。
　「いま有機認証を持っている」も、現時点では正確ではない。**

⚠️ **HVE / Demeter / Biodyvin / Terra Vitis の語は、公式サイトにも Agence Bio 登録にも一つも出てこない。
　これらの認証は主張されていない。**

---

## Winemaking

⚠️ 🔴 **本節は本ドシエで最も薄い。理由を明示する。**
**公式の醸造ページ `/en/savoir-faire/le-travail-des-chais` は、
バーチャルツアーと訪問への誘導だけで構成されており、醸造の技術的記述を一切含まない**
（取得した本文は 2 段落・約 380 字で、そのすべてが定性的な導入文である）。
🔴 **これは「サイトが古い」のでも「取得に失敗した」のでもなく、現行の公式ページがそう作られている。**

### ✅ 公式が実際に書いていること

| 項目 | 記述 |
|---|---|
| 🔴 **グラン・ヴァンの選抜率** | ✅ **平均で収穫の約 40%。**「**around 40% of the harvest is dedicated to the Grand Vin**」<br>**実測値（各年ページ）: 2006 = 36%（瓶詰め時には 1/3）／2012 = 34% 弱／2015 = 35%／2016 = 28%／2019 = 37%** |
| **グラン・ヴァンの生産量** | ✅ **平均およそ 120,000 本** |
| 🔴 **選抜の階層** | ✅ 🔴 **グラン・ヴァン → Pavillon Rouge → Margaux du Château Margaux → 第 4 選抜（バルク販売、瓶詰めしない）**<br>「**Volumes not retained for bottling are now grouped into a fourth selection, forming the estate's fourth wine, which is sold exclusively in bulk.**」 |
| **プレスワイン** | ✅ **2012 年ページ: 「Our best press wines, which are the result of a stringent selection, bring remarkable density and flesh to this year's blend, without sacrificing the slightest finesse.」** |
| **サードの熟成** | ✅ 🔴 **約 18 か月、うち約 25% を新フレンチオークで** → §Canonical Conflict |
| **`Pavillon Blanc Second Vin` の熟成** | ✅ **約 8 か月、うち約 20% を新フレンチオークで** |
| **元詰め** | ✅ **1925 年からシャトー元詰めが義務** |

🔴 ⚠️ **公式に記述が無い**: 発酵槽の材質・形状、発酵温度、マセラシオン期間、マロラクティック発酵の有無、
清澄の方法、グラン・ヴァンと Pavillon Rouge の樽熟期間・新樽比率、アルコール度数、デゴルジュ相当の工程。
→ 🔴 **本ドシエはこれらを一切主張しない。** → §Staff Notes ⚠️ ③④

---

## Style

### ✅ 生産者自身のヴィンテージ評（**OBP 8 本すべてに公式ページが存在する**）

| VT | ✅ 公式の言葉（抜粋） | ✅ セパージュ | ✅ 選抜率 |
|---|---|---|---|
| 🔴 **1995** | 「**1995 is a truly great vintage displaying all the hallmark characteristics: power, depth, richness, complexity, subtlety and harmony.** 今日、香りは閉じてはいないがなお控えめで、アロマはあるがいくらか覆われている。口中では明らかに力が支配し、**タンニンの構造は密で、締まっており、硬さを伴わずに堅固**。理想を言えば、この見事なワインはあと数年置いてから開けるべきである」（2025 年 10 月） | ⚠️ **公式に記載なし** | ⚠️ 記載なし |
| 🔴 **2005** | 「**2005 is a truly great, pure Château Margaux vintage!** まずそのクラス —— **繊細さと優美さと深さを備えた、そのテロワールと、いくつかの夢のような年にしか属さないあの香り**。そして力 —— **凝縮は例外的で、2000 年、さらには 2003 年をも上回る**。まず色に前例のない強度として現れ、口中では並外れた密度と長さとして現れる。**それでも最後に物を言うのは力ではなく、官能性と調和である**」 | 🔴 **Cabernet Sauvignon 85%**（**13% を超えないアルコールで完璧な熟度に達した**）／**Merlot 8%**（**14% に達しなかった唯一のロット**）<br>⚠️ **残り 7% の内訳は公式に記載なし** | ⚠️ 記載なし |
| 🔴 **2006** | 「**Cabernet sauvignon therefore dominates the blend: 90%!** それが 2006 年に**並外れた香りの繊細さ、2005 年に次ぐタンニンの豊かさ、そしてとりわけ密で目の詰まった質感**をもたらす。**余韻は非常に長く、フレッシュで生き生きとしており、わずかに堅いがすでに旨みがある**」<br>「**One single batch of merlot, though of remarkably high quality, finally went in the blend, but it only represents 4% … It is the first time we have had so little.**」 | 🔴 **CS 90% / Merlot 4% / Petit Verdot 4% / Cabernet Franc 2%** | **収穫の 36% 弱**（**瓶詰め時には 1/3**） |
| 🔴 **2010** | 「**As unbelievable as it may sound, 2010 is at least as great a vintage of Château Margaux as 2009!** … **Château Margaux 2010 is a giant, but it is not monstrous. It is sheer magic —— both classic and extraordinary.** 純粋さ、繊細さ、柔らかく爽やかな余韻において古典的であり、驚くべき香りの複雑さと例外的な力において並外れている」 | 🔴 **CS 90% / Merlot 7% / Cabernet Franc 1.5% / Petit Verdot 1.5%** | ⚠️ 記載なし |
| 🔴 **2012** | 「**Château Margaux 2012 is a perfect example of the softness, delicacy, charm, and balance that have been the hallmarks of our wines for centuries.** 最後に、偉大な年になるにはあと少しの深みと密度が要るというだけである。**タンニンの柔らかさゆえに今日でも美味だが、理性はもう少し待つよう告げる**」 | 🔴 **CS 87% / Merlot 10% / Cabernet Franc 2%**<br>**Petit Verdot は「唯一の古い区画が見事なワインを生んだ」と書かれるが比率の記載なし** | **収穫の 34% 弱**（**理由は 2012 年の不均質性。若木と敏感なテロワールの水ストレス**） |
| 🔴 **2015** ⭐ | 「**2015 was a historic year—literally—for Château Margaux.**（1815 年建造の建物の 200 周年と、Norman Foster 設計の新施設の落成）… **one can evoke a combination of the strength of 2005, the flesh of 2009, the subtlety of 2010, and the inimitable charm of Château Margaux.** … **Fittingly, the final vintage overseen by Paul Pontallier, Managing Director of Château Margaux from 1989 to 2015, expresses the estate's most beautiful qualities.**」 | 🔴 **CS 87%**（「**unusual vigour and strength this year**」）**/ Merlot 8% / Cabernet Franc 3% / Petit Verdot 2%** | 🔴 **収穫の 35% のみ。「a record level of strictness for a vintage of this quality」** |
| 🔴 **2016** | 「**How difficult it is to follow a vintage as extraordinary as 2015! And yet, Château Margaux 2016 clearly ranks among the greatest vintages of this early century!** 香りはとりわけ繊細で複雑で深い。口中では**信じがたい容積、柔らかさ、そしてなにより長さ**。… **乾いた陽光の夏にもかかわらず酸を保持しており、見事な熟成能力を約束する**」 | 🔴 **CS 94% / Cabernet Franc 3% / Merlot 2% / Petit Verdot 1%**（**PV は 1% でも「considerable density and volume」を加える**） | 🔴 **収穫の 28%** |
| 🔴 **2019** | 「**Château Margaux 2019 is one of the greatest vintages in our history and joins the list of exceptional wines we've been fortunate to produce this decade: 2015, 2016, 2018, and now 2019…**」<br>「**Château Margaux 2019 will be the first to fully benefit from the new facilities in the second-year cellar**（André Mentzelopoulos が 1970 年代末に着工した二年目蔵の全面改修）」 | 🔴 **CS 90% / Merlot 7%**（**"Haut-du-Jardin" 区画のメルロを新たに加えた**）**/ Cabernet Franc 2% / Petit Verdot 1%** | 🔴 **収穫の 37%** |

### ✅ 提供について（公式 `/en/mon-vin/service`）

- 🔴 **赤**: 「**Great red Bordeaux wines are traditionally served, at room temperature, around 18–19°C (64-66°F).**」
  **高すぎるとブーケが繊細さを失いアルコールが立ち、タンニンが乾いて硬く感じられる。低すぎるとアロマが閉じ、
  ワインは鈍く短く感じられる**
- **白（Pavillon Blanc）**: **10–13°C（50–55°F）、室温に応じて**
- **デカンタージュ**: **主目的は澱の分離。**「**For young wines, decanting is generally beneficial … a wide carafe is ideal.
  For older wines, a narrower carafe is preferable, as the aim is simply to remove the sediment while limiting exposure to oxygen.**」
  **澱があるなら年齢を問わずデカンタすべき。光源にかざしてゆっくり注ぐ。提供の直前が望ましい**

⚠️ **公式は個別ヴィンテージについて「スミレ」「バラの花びら」といった具体的なアロマ語をほとんど使わない。
本節の語はすべて公式原文の直訳であり、一般的なマルゴー像から補ったものは一つも無い。**

---

## Important Cuvées

### ✅ 公式の現行ラインナップ（`sitemap_en.xml` の `/vins/` 251 URL から機械的に確定）

| # | 公式名 | 種別 | ✅ 公式ページのヴィンテージ範囲 | 備考 |
|---|---|---|---|---|
| 1 | 🔴 **Grand Vin du Château Margaux** | **グラン・ヴァン（赤）** | 🔴 **1900〜2025 の全年（127 ページ）＋ 1771 / 1791 / 1847 / 1848 / 1855 / 1864 / 1865 / 1868 / 1870 / 1893 / 1898 / 1899 の歴史ヴィンテージ 12 本** | **収穫の約 40%、約 120,000 本** |
| 2 | **Pavillon Rouge du Château Margaux** | **セカンド（赤）** | **1978〜2025 の全年（49 ページ）** | **1906 年に命名** |
| 3 | 🔴 **Margaux du Château Margaux** | **サード（赤）** | 🔴 **2009〜2019。ただし 2016 のページだけが存在しない**（実測 404） | **約 18 か月熟成、新樽約 25%、年産およそ 60,000 本** |
| 4 | **Pavillon Blanc du Château Margaux** | **白** | **1978〜2025 の全年（49 ページ）** | 🔴 **Sauvignon Blanc 100%、12 ヘクタール。1920 年に命名** |
| 5 | **Pavillon Blanc Second Vin** | **白のセカンド** | **2023 / 2024**（**2022 年産から瓶詰め開始**） | **約 8 か月熟成、新樽約 20%、年産およそ 15,000 本。Place de Bordeaux 経由** |
| — | **第 4 選抜** | **バルク販売** | **瓶詰めされない** | **公式が「fourth wine」と呼ぶ** |

⚠️ **`Margaux du Château Margaux` は公式サイトのフッター・ナビゲーションの「OUR WINES」に載っていない**
（載っているのは Grand Vin / Pavillon Rouge / Pavillon Blanc / Pavillon Blanc Second Vin の 4 つ）。
**だが個別ページ群は存在し、2017 年のページは本文で「the 2016 vintage」に言及している。
したがって 2016 年産のサードは存在するが、ページが無い。** → §Open Questions 5

### 🔴 白の帰属 —— 法定文書で確定した

🏛 **INAO CDC「Margaux」第 I 章 III 節（2010 年版・2022 年版とも同一文言）**:
「**L'appellation d'origine contrôlée « Margaux » est réservée aux vins tranquilles rouges.**」

→ 🔴 **`Pavillon Blanc du Château Margaux` と `Pavillon Blanc Second Vin` は、
　法的に AOC Margaux ではありえない。**
→ 🔴 **公式 terroir ページも、AOC への帰属を赤の畑にだけ限定して書いている** —
　「**The red vineyard of Château Margaux, located in the heart of the Margaux AOC**」。
⚠️ 🔴 **ただし公式サイトは、白が実際にどのアペラシオンで出荷されているかを一度も明記していない。
　`Bordeaux Blanc` という語は公式サイトのどこにも現れなかった。
　本ドシエは「AOC Margaux ではない」までを確定とし、「AOC Bordeaux である」とは書かない。** → §Open Questions 2

### 🔴 OBP 掲載分 —— 8 行を 1 行ずつ

🔍 **8 行すべてが `FRANCE | RED > BORDEAUX`、`source_producer_raw = "Margaux"`、`source_wine_raw = "Margaux"`、
`match_state = unresolved`（producer は exact、vintage が unresolved）、提案は `cuvee:chateau-margaux-chateau-margaux`。**

🔴 **まず、8 行すべてに共通する構造的事実を確定する。**

**① 白は 2 つの独立した理由で除外される。**
　🏛 **AOC Margaux は法的に赤専用である。**
　🔍 **メニューのセクションが `RED > BORDEAUX` である。**
　→ **`Pavillon Blanc` 系の 2 本は、8 行のいずれでもない。**

**② 残る候補は 3 つ —— グラン・ヴァン／Pavillon Rouge／Margaux du Château Margaux。**
　🔴 **この 3 つはすべて AOC Margaux の赤であり、印字文字列 `Margaux` はどれとも両立する。**
　🔴 **とくに 3 番目は、正式名が文字通り `Margaux` で始まる。**
　→ **`source_wine_raw = "Margaux"` は「アペラシオンだけが印字されている」とも
　　「サードワインの名の頭が印字されている」とも読める。両方が文法的に成立する。**

**③ ヴィンテージの存否だけが、機械的に効く唯一の切り分けである。**

| # | VT | 価格 | ✅ グラン・ヴァン | ✅ Pavillon Rouge | ✅ Margaux du Ch. Margaux（サード） | 🔴 判定 |
|---|---|---|---|---|---|---|
| 1 | **2019** | $3,760 | ✅ **有**（CS 90/Me 7/CF 2/PV 1、収穫の 37%） | ✅ **有** | ✅ **有**（CS 60/Me 38/CF 1/PV 1） | ⚠️ **3 候補すべて実在。印字では決まらない** |
| 2 | **2016** | $3,380 | ✅ **有**（CS 94/CF 3/Me 2/PV 1、収穫の 28%） | ✅ **有** | ⚠️ **ページ無し（404）だが 2017 年ページが「the 2016 vintage」に言及**→存在する | ⚠️ **3 候補すべて実在** |
| 3 | **2015** ⭐ | $6,890 | ✅ **有**（CS 87/Me 8/CF 3/PV 2、収穫の 35%）<br>🔴 **紙ラベルが無い特別意匠**（後述） | ✅ **有** | ✅ **有**（**「最も厳しい選抜。生産のほぼ 1/4 を第 4 選抜に落とした」**） | 🔴 **卓上で一意に決まる唯一の行** → 後述 |
| 4 | **2012** | $2,440 | ✅ **有**（CS 87/Me 10/CF 2、収穫の 34% 弱） | ✅ **有** | ✅ **有** | ⚠️ **3 候補すべて実在** |
| 5 | **2010** | $5,120 | ✅ **有**（CS 90/Me 7/CF 1.5/PV 1.5） | ✅ **有** | ✅ **有** | ⚠️ **3 候補すべて実在** |
| 6 | **2006** | $3,375 | ✅ **有**（CS 90/Me 4/PV 4/CF 2、収穫の 36% 弱） | ✅ **有** | 🔴 **無 —— サードは 2009 年産から** | 🔴 **サードは除外。グラン・ヴァンか Pavillon Rouge の 2 択** |
| 7 | **2005** | $5,120 | ✅ **有**（CS 85/Me 8、残り 7% は非公表） | ✅ **有** | 🔴 **無** | 🔴 **2 択** |
| 8 | **1995** | $4,800 | ✅ **有**（セパージュは非公表） | ✅ **有** | 🔴 **無** | 🔴 **2 択** |

🔴 **結論 —— 8 行のうち 5 行（2019 / 2016 / 2015 / 2012 / 2010）は 3 候補、
　3 行（2006 / 2005 / 1995）は 2 候補まで絞れるが、印字文字列と公式資料だけでは 1 つに確定できない。**
🔴 **これは調査の不足ではなく、メニューが印字していない情報を要求されているということである。**
　**§3-4 の問い（どちらの側が defective か）への回答: この 8 行については OBP メニュー側である。**
　**canonical は「そもそも実体を 1 件も持っていない」ため、defective ですらなく不在（gap）である。**

### 🔴 3 行目（2015・$6,890）—— **識別に効く公式事実**

⚠️ **価格の説明はしない。** だが公式が、この 1 本の**同定手順**を他の 7 本と違うものにしている。

✅ 「**For all these reasons, Château Margaux chose to create a special design for its 2015 Grand Vin.
A unique case was designed and adorned with a magnificent screen print, specially conceived for this vintage,
and affixed directly to the glass in place of the usual labels.**」

🔴 **すなわち 2015 年のグラン・ヴァンには、通常のラベルが無い。ガラスに直接スクリーン印刷されている。**
🔴 **したがって 3 行目は、卓上で見れば一意に決まる —— 通常の紙ラベルが貼ってあれば、それは 2015 年のグラン・ヴァンではない。**
✅ **公式が挙げるこの意匠の理由は 2 つ**: **1815 年建造の建物の 200 周年 ＋ Norman Foster 設計の新施設の落成**、
そして **Paul Pontallier（MD 1989–2015）が手がけた最後のヴィンテージであること**。

⚠️ **`Pavillon Rouge 2015` と `Margaux du Château Margaux 2015` の意匠については公式に記述が無い。
　「特別意匠が無い＝グラン・ヴァンではない」とまでは言えるが、その先は現物で確認する必要がある。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① メドックの AOC マルゴー、1855 年格付第 1 級。敷地 265 ヘクタールは 17 世紀末から変わっていない。**
「**メドックのマルゴーというアペラシオンの、1855 年格付第 1 級**です。
**敷地は 265 ヘクタール**で、造り手自身が『**17 世紀末にこの面積に達して以来、今日まで同じ**』と書いています。
そのうち**ブドウは赤が約 87 ヘクタール、白が 12 ヘクタール**で、残りは牧草地と森と庭園です。
**区画は 126 に分けて管理**していて、**そのうち 72 区画がカベルネ・ソーヴィニヨン**。
土壌は**深い砂利**が中心で、造り手は**マルゴーを象徴する『タイプ 4』の段丘**と呼んでいます。
いまの当主は **2023 年末に CEO に就いたアレクシス・ルヴェン＝メンツェロプロス**、
**アンドレ、コリーヌに次ぐ第 3 世代**です。」

**② グラン・ヴァンは収穫の 4 割弱しか使わない。その下に 3 段階ある。**
「🔴 **『シャトー・マルゴー』を名乗るワインは、収穫の平均 4 割程度**しか使いません。
造り手が公表している実数で言うと、**2016 年は 28%、2012 年は 34% 弱、2015 年は 35%、2019 年は 37%**。
残りは**セカンドのパヴィヨン・ルージュ**、**サードのマルゴー・デュ・シャトー・マルゴー**（2009 年から）、
そして**瓶詰めせずバルクで売る第 4 選抜**へ下ろされます。
**グラン・ヴァンは年産およそ 12 万本**です。」

**③ 2015 年だけは、ボトルに紙のラベルが無い。**
「🔴 **2015 年のグラン・ヴァンは、通常のラベルの代わりに、ガラスに直接スクリーン印刷**されています。
造り手が『**このヴィンテージのためだけに考案した**』と書いている特別意匠です。
理由は 2 つで、**1815 年に建った建物の 200 周年**と、
**1989 年から 2015 年まで MD を務めたポール・ポンタリエが手がけた最後のヴィンテージ**であること。
**造り手がグラン・ヴァンのために一度きりの意匠を作ったのは、これが初めて**です。」

### 追加で使える一手（**すべて造り手自身の言葉**）

- **2010 について**: 「造り手自身が『**信じがたいことに、2010 は少なくとも 2009 と同じくらい偉大**』と書いています。
  **カベルネ・ソーヴィニヨンが 90%**。『**巨人だが怪物ではない。純粋さと繊細さと柔らかい余韻において古典的で、
  驚くべき香りの複雑さと例外的な力において並外れている**』。」
- **2016 について**: 「**カベルネ・ソーヴィニヨンが 94%** で、造り手の記録の中でも際立って高い年です。
  **収穫の 28% しか使っていない**。『**乾いた陽光の夏にもかかわらず酸を保っている**』と書いています。」
- **2005 について**: 「造り手は『**凝縮は例外的で、2000 年、さらには 2003 年をも上回る**』と。
  **カベルネ・ソーヴィニヨンが 85% で、アルコールは 13% を超えずに完璧な熟度に達した**そうです。
  『**それでも最後に物を言うのは力ではなく、官能性と調和である**』。」
- **1995 について**: 「造り手の現在の評は『**力、深み、豊かさ、複雑さ、繊細さ、調和 —— 偉大な年の特徴をすべて備える**』。
  ただし『**今日なお香りは控えめで、理想を言えばあと数年**』とも書いています（2025 年 10 月時点の記述）。」
- **提供温度**: 「造り手の指定は **18〜19 度**です。**高すぎるとブーケが繊細さを失い、タンニンが乾いて感じられる**、
  **低すぎるとアロマが閉じて短く感じられる**、と明記しています。」
- **デカンタ**: 「造り手は『**若いワインには広いカラフ、熟成したワインには細いカラフ**』と使い分けを書いています。
  熟成したものは**澱を除くのが目的で、酸素との接触は抑えたい**からです。」
- **真贋**: 「**1989 年からレーザー刻印、1997 年から瓶底のエンボス、2011 年からプルーフタグのバブルコード**。
  **2026 年からは QR コード付きのシール**です。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／出典が矛盾している**）

1. 🔴 ⚠️ **メニューの `Margaux` を「シャトー・マルゴー（グラン・ヴァン）です」と断定しない。**
   **`Margaux` という印字は、AOC 名でもあり、コミューン名でもあり、
   この造り手のサードワイン `Margaux du Château Margaux` の名の頭でもある。**
   **8 行のうち 5 行はグラン・ヴァン／セカンド／サードの 3 候補、3 行（1995/2005/2006）でも 2 候補が残る。**
   → **注文前に必ず現物のラベルを確認すること。**
2. 🔴 ⚠️ **8 本のどれについても「オーガニック」と言わない。同時に「オーガニックではない」とも言わない。**
   **Agence Bio の登録（exact SIRET 一致）は `datePremierEngagement = 2023-07-18`。
   OBP の 8 本は 1995〜2019 で、全部これより前である。**
   **さらに現在の状態は `ENGAGEE` / `C1`（転換 1 年目）であり、`mixite = Oui`（有機と非有機の混在経営）。
   「いま有機認証を持っている」も正確ではない。**
   言えるのは「**2023 年に Ecocert のもとで有機への転換を開始し、造り手自身も『転換中』と書いている**」まで。
3. 🔴 ⚠️ **発酵槽の材質・形状を語らない。とくに「木製の円錐台形発酵槽」と言ってはならない。**
   🔴 **公式の醸造ページにはバーチャルツアーへの誘導しか無く、
   発酵槽についても、発酵温度についても、マセラシオンについても記述が一切無い。**
   （THÉSEUS の DB にはこの記述があるが、本調査では公式に裏が取れなかった。）
4. 🔴 ⚠️ **「卵白 6 個で清澄」「自社樽工房で 1 日 3 個」「必要量の 3 分の 1 が自社製」を言わない。**
   **公式サイトのどこにも無い。**（歴史ページに建物としての `cooperage` が出てくるだけである。）
5. 🔴 ⚠️ **「収穫は 5 チーム 1,000 人」と言わない。公式に無い。**
6. 🔴 ⚠️ **「馬で耕している」「性フェロモン交信攪乱を導入」「1 年以上堆肥化した牛糞」を言わない。**
   **いずれも公式サイトにも Agence Bio 登録にも無い。**
   言えるのは「**地域のパートナーシップで有機残渣を堆肥化して区画に還元している**」まで。
7. 🔴 ⚠️ **「栽培密度は 1 ヘクタールあたり 10,000 本」と断定しない。**
   **公式は「6,666 から 10,000 本、土壌型と狙う均衡に応じて変える」と幅で書いている。**
8. 🔴 ⚠️ **「1990 年代から殺虫剤不使用」と言わない。**
   **造り手が 2012 年に書いた文章は「10 年間、この地所で殺虫剤を使っていない」であり、起点はおよそ 2002 年。**
   同じ文が「**2012 年には化学的処理を 1 回だけ、通常は 7〜8 回のところ**」とも書いている。
9. 🔴 ⚠️ **「1855 年に 20 点満点を取った唯一のシャトー」を第三者の事実として語らない。**
   **これは造り手自身の沿革ページの記述であり、格付を管理する団体側の文書では本調査で確認できていない。**
   言うなら「**造り手自身がそう書いている**」と帰属を明示すること。
10. 🔴 ⚠️ **`Pavillon Blanc` を「AOC マルゴーの白」と言ってはならない。**
    **AOC Margaux は法的に赤のスティルワイン専用である（INAO cahier des charges 第 I 章 III 節）。**
    ⚠️ **同時に「AOC ボルドー・ブランです」とも断定しない —— 公式サイトは白のアペラシオンを一度も明記していない。**
11. ⚠️ **ポール・ポンタリエの在任期間を「1983 年から 2016 年」と言わない。**
    **公式は「Managing Director of Château Margaux from 1989 to 2015」と書いている。**
12. ⚠️ **「オーナーはコリーヌ・メンツェロプロス」と現在形で言わない。**
    **公式の現在のチーム表は、Co-owner & CEO を Alexis Leven-Mentzelopoulos（2023 年末就任）、
    Co-owner & President of the Supervisory Board を Alexandra Petit-Mentzelopoulos としている。
    Corinne は沿革の中で「Alexis の母」として言及されるのみである。**
13. ⚠️ **1995 年と 2005 年のセパージュを完全な比率で言わない。**
    **1995 は公式に記載が無く、2005 は CS 85% と Merlot 8% までしか公表されていない（残り 7% は非公表）。**
14. ⚠️ **アルコール度数・生産本数（グラン・ヴァンの約 120,000 本、サードの約 60,000 本、
    白セカンドの約 15,000 本を除く）・樽熟成期間（サードの約 18 か月と白セカンドの約 8 か月を除く）を言わない。**
    **グラン・ヴァンと Pavillon Rouge の熟成期間・新樽比率は公式に一切記載が無い。**
15. ⚠️ **第三者点数を言わない。本調査で取得したどの公式ページにも点数の掲載が無い。**
16. ⚠️ **「マルゴーは女性的」「5 大シャトーで最もエレガント」といった比較的形容を、造り手の言葉として語らない。**
    **公式のヴィンテージ評にこの種の比較は出てこない。**（THÉSEUS の DB にはあるが、公式の裏付けが無い。）
17. ⚠️ **住所が Margaux-Cantenac であることを根拠に別のシャトーと混同しない。**
    **同コミューンには Palmer、Rauzan-Ségla、Lascombes、d'Issan、Desmirail、Marquis de Terme などが所在し、
    さらに `Domaine de l'Île Margaux` という別の生産者もいる。切るのは SIREN `321152993` である。**

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

🔒 **canonical も `research/canonical_conflicts/REGISTER.md` も本書では一切開いていない・編集していない。
以下はすべて本ドシエ内の escalation であり、ID は既存ファミリーへの帰属提案にすぎない。**

**検証対象**: `ch-margaux-1855`（全 23 キー）。**検証した個別主張 33 件のうち 18 件が公式と食い違った。**

| failure mode | 件数 |
|---|---|
| 🔴 **contradicted**（公式が別の値を明示している） | **9** |
| 🔴 **unsourced**（公式のどこにも根拠が無い。誤りとは言えないが典拠が無い） | **9** |
| ✅ **pass** | **15** |

---

### 🔴 ① `S-2` に証拠を追加 —— **格付の殻レコードはマッチングから不可視である**

**1. レコード**: `ch-margaux-1855`（`vintage = '—'`、U+2014）

**2. 実測**: 🔍 **canonical 928 件のうち `vintage == '—'` は 328 件**
（Batch 11 の実測 175 件から増えている。**同じ 928 件の母集団に対する再実測である**）。
**`classification` に `1855` を含むレコードは 68 件。**

**3. 🔴 新しい証拠 —— 「殻」と「実体」で `classification` の書式が違う**

| `classification` の文字列 | 件数 | `vintage` | 実体 |
|---|---|---|---|
| **`1855 Médoc Classification · 1er Grand Cru Classé`** | **5** | 🔴 **全件 `'—'`** | **Lafite / Latour / Margaux / Mouton / Haut-Brion —— 格付の殻** |
| **`Premier Grand Cru Classé (1855)`** | **5** | 🔴 **全件が実年（1987 / 1993 / 1996 / 1996 / 2001）** | **Haut-Brion ×2 / Mouton ×2 / Latour ×1 —— 実体ボトル** |

🔴 **これは重要な反例である。**
**ブリーフ §4 は「`vintage: '—'` ＋ `1855 Médoc Classification · Nème Grand Cru Classé` は
格付を符号化した殻である」と述べており、それは正しい。
だが同時に、canonical には第 2 の書式 `Premier Grand Cru Classé (1855)` が並存しており、
そちらは実体ボトルにだけ付いている。**
🔴 **つまり「ボルドー第 1 級の実体が canonical に構造的に無い」わけではない ——
Latour・Mouton・Haut-Brion には有る。5 大シャトーで実体を 1 本も持たないのは Lafite と Château Margaux だけである。**

**4. OBP への影響**: 🔴 **8 本すべて。**`vintage='—'` の殻は年で照合できないため、
`producer` が exact に当たっても `vintage` が `unresolved` のまま残る。

**5. 推奨（🔒 実行していない）**: **殻レコードを「格付エンティティ」として実体ボトルとは別の型に分離し、
`classification` の 2 書式を統一する。**
**⚠️ ただし 2 書式の並存が偶発なのか設計なのかは本調査では判断できない。CTO の判断領域である。**

**6. Confidence**: 🔴 **High**（全件を機械的に列挙して確認した）

---

### 🔴 ② `P-*` ファミリーに証拠を追加 —— **contradicted 9 件**

🔴 **Batch 10 の知見（「失敗は typed field にも及ぶ」）を、この生産者は 3 件で再現している
（`serving_temp` / 栽培密度 / 作付面積）。**

| # | canonical の格納値 | ✅🏛 公式の値 | 出典 |
|---|---|---|---|
| 1 | 🔴 **「現オーナーはコリーヌ・メンツェロプロス（2003 年から独占株主）」** | 🔴 **Alexis Leven-Mentzelopoulos = Co-owner & CEO（2023 年末就任）／Alexandra Petit-Mentzelopoulos = Co-owner & President of the Supervisory Board** | ✅ `/en/le-domaine/les-femmes-et-les-hommes` ＋ ✅ mentions légales ＋ 🏛 RNE `dirigeants` の**三者が一致** |
| 2 | 🔴 **「ポール・ポンタリエ MD（1983 年〜）、2016 年 3 月急逝」** | 🔴 **「Managing Director of Château Margaux from 1989 to 2015」** | ✅ `/en/vins/grand-vin-du-chateau-margaux-2015`。**始点・終点の両方が違う** |
| 3 | 🔴 **「265ha 所有のうち 80ha 超でブドウ栽培」** | 🔴 **「around 87 hectares of red vines and 12 hectares of white vines in production」（＝約 99 ha）** | ✅ `/en/le-domaine/le-terroir`。**白 12 ha が欠落している** |
| 4 | 🔴 **「栽培密度 10,000 本/ha」**（typed) | 🔴 **「Planting densities range from 6,666 to 10,000 vines per hectare」** | ✅ 同上。**単一値と幅** |
| 5 | 🔴 **「1990 年代以来殺虫剤不使用」** | 🔴 **「we have not used any insecticide on the estate for 10 years」（2012 年産についての記述＝起点はおよそ 2002 年）** | ✅ `/en/vins/grand-vin-du-chateau-margaux-2012` |
| 6 | 🔴 **「Pavillon Rouge（1908 年〜、1977 年再開）」** | 🔴 **「before becoming Pavillon Rouge du Château Margaux in 1906」** | ✅ `/en/vins/margaux-du-chateau-margaux`。<br>🔴 **1908 は「株主シンジケートがシャトーを購入した年」であり、公式沿革ページに別事実として載っている。所有年をキュヴェ命名年に取り違えた形である**（「1977 年再開」も公式に根拠が無い） |
| 7 | 🔴 **「サード：Margaux du Château Margaux（2009 年〜、15 ヶ月樽熟成）」** | 🔴 **「aged for around 18 months, with approximately 25% aged in new French oak barrels」**（**2009 年起点は正しい**） | ✅ 同上 |
| 8 | 🔴 **ラインナップを 4 本と記載**（グラン・ヴァン／セカンド／サード／白） | 🔴 **5 本 ＋ バルクの第 4 選抜。**「**Pavillon Blanc Second Vin is only the fifth wine to be launched by the estate in five centuries**」（2022 年産から） | ✅ `/en/vins/pavillon-blanc-second-vin` ＋ sitemap |
| 9 | 🔴 **`serving_temp = "17–19°C"`**（typed） | 🔴 **「around 18–19°C (64-66°F)」**（白は 10–13°C） | ✅ `/en/mon-vin/service` |

**OBP への影響**: 🔴 **8 本すべて。**`ch-margaux-1855` はこの生産者の全 OBP 行が参照する唯一のレコードであり、
`obp_note` はソムリエ向けの提供テキストとして設計されている。
🔴 **とくに ①②⑤⑧ は、卓上で客に語られると事実として誤る。**

**Confidence**: 🔴 **High**（9 件すべてについて公式原文を引用できる）

---

### 🔴 ③ `P-*` ファミリー —— **unsourced 9 件**（誤りとは断定しない）

**公式サイト全体（`sitemap_en.xml` 358 URL のうち関連 20 ページを取得）に根拠が見つからなかったもの:**

1. **「木製円錐台形ファーメンター」**（canonical が「醸造の最大の特徴」と位置づけている記述）
2. **「清澄：卵白 6 個/樽」**
3. **「自社樽工房：専属職人 1 名、1 日 3 個製作、必要量の 1/3 を自社製」**
4. **「収穫は 5 チーム計 1000 人体制」**
5. **「セクシャル・コンフュージョン導入」**
6. **「有機肥料（1 年以上堆肥化した牛の堆肥）」**
7. **「馬による耕作を試験的に実施」**
8. **「フィリップ・パスコール 2016 年 10 月就任」**（**現職であることは公式で確認できるが、就任年月は公式に無い**）
9. **`tasting_en` の「the most aromatic and feminine of the 1855 premiers crus」**（比較的評価。公式のヴィンテージ評にこの種の比較は現れない）

🔴 **①〜④ が特に重い。**
**canonical の `obp_note` はこれらを「【醸造の最大の特徴】」「【自社樽工房】」という見出しつきで提示しており、
ソムリエが最も語りたくなる部分でありながら、公式の裏付けが取れていない。**
⚠️ **「公式サイトが薄い」ことが原因の可能性が高い**（醸造ページはバーチャルツアーへの誘導のみ）。
**これらが「誤り」だとは言っていない —— 典拠が無い、と言っている。** → §Open Questions 3

**Confidence**: **Medium-High**（不在の証明は原理的に弱い。ただし 20 ページと sitemap 全 358 URL を走査した上での不在である）

---

### 🔴 ④ **gap（衝突ではない）** —— ヴィンテージ実体 0 件、他の 4 ワイン 0 件

🔍 **実測**:
- **`producer == 'Château Margaux'` のレコード: 1 件**（`ch-margaux-1855`、`vintage='—'`）
- 🔴 **ヴィンテージ実体: 0 件** → **OBP 8 行すべてが vintage gap**
- 🔴 **`Pavillon` の語を含むレコード: canonical 全体で 2 件のみ。**
  **うち 1 件は `ch-margaux-1855` の `obp_note` 内の散文、もう 1 件は `leoville-poyferre-1855`（別生産者）。**
  → 🔴 **`Pavillon Rouge` / `Pavillon Blanc` / `Margaux du Château Margaux` / `Pavillon Blanc Second Vin` は
  　canonical に独立レコードとして 1 件も存在しない。**

🔴 **`D-2026-08-05-14`（Abreu 先例）に従い、これは conflict ではなく gap として扱う。登録票には上げない。**

---

### ⚠️ ⑤ `D-2026-08-05-08` の実測 —— **`Margaux` の部分一致精度は 1/53**

🔍 **canonical 928 件に対し、レコード全体を JSON 化して `margaux` を部分一致させると 53 件がヒットする。
そのうち本当にこの生産者なのは 1 件だけである（精度 1.9%）。**

**内訳**:
- **31 件** = `bordeaux-vintage-YYYY-guide`（**1964〜1997 の年別ガイド**）。**`subregion` や `description_en` / `obp_note_en` の
  散文で `Margaux` に言及しているだけ**（例: `Saint-Estèphe ★★★★ Pauillac ★★★★★ … Margaux ★★★`）
- **21 件** = **Margaux コミューンの他の格付シャトー**（`palmer-1855` / `rauzan-segla-1855` / `lascombes-1855` /
  `dissan-1855` / `du-tertre-1855` …）。**`subregion = 'Margaux'` で一致する**
- **1 件** = `lagrange-sj-1855`（**Saint-Julien の Château Lagrange**）。**`obp_note_en` の散文
  「Southern Saint-Julien, near Margaux village」で一致する** 🔴 **これは Margaux ですらない**
- **1 件** = 🔴 **`ch-margaux-1855` —— 本命**

→ 🔴 **`D-2026-08-05-08` に対する新しい定量的証拠。**
**Bordeaux では `subregion` がアペラシオン名を持つため、部分一致は同アペラシオンの全シャトーを巻き込む。
さらに年別ガイドの散文が全アペラシオン名を列挙するため、母数がさらに膨らむ。**

---

### 🔴 ⑥ **unnumbered — CTO's call**: 生産者名・キュヴェ名・アペラシオン名・コミューン名の四重衝突

**ブリーフは Batch 9 の Clos de Tart 先例（producer/cuvée 同一文字列、未採番）を指している。
Château Margaux はその形を含むが、より重い。**

| 軸 | 値 |
|---|---|
| **producer** | `Château Margaux` |
| **提案 cuvée** | `chateau-margaux-chateau-margaux`（🔴 **producer と cuvée が同一文字列 = Clos de Tart 形**） |
| **`subregion`** | `Margaux`（🔴 **AOC 名。canonical 上、同アペラシオンの 21 シャトーと同値**） |
| **commune** | 🏛 `Margaux-Cantenac`（🔴 **法定名が 2010→2022 で変わっている**） |
| 🔴 **サードワインの正式名** | ✅ `Margaux du Château Margaux`（🔴 **Clos de Tart 形には無い、新しい軸**） |

🔴 **Clos de Tart 形との違い**:
**Clos de Tart では producer と cuvée が同名なので、衝突しても指す実体は 1 つだった。
Château Margaux では、`Margaux` という同じ文字列が指しうる実体が 3 つある
（グラン・ヴァン／セカンド／サード）。衝突が「冗長」ではなく「多義」である。**

🔴 **加えて `source_wine_raw = "Margaux"` は、
「アペラシオンだけを印字した」とも「サードワイン名の頭を印字した」とも読める。
どちらの解釈も文法的に成立し、印字からは決められない。**

**推奨（🔒 実行していない）**:
- **cuvée 層に `tier`（grand vin / second / third）を識別属性として持たせる**
- 🔴 **`source_wine_raw` がアペラシオン名と完全一致する行に「アペラシオン専用フラグ」を立て、
  自動確定させず review queue に送る**（Bordeaux ブロック 8 生産者に共通して効くはずである）
- ⚠️ **どちらも設計判断であり、本書では実行していない。**

**Confidence**: 🔴 **High**（サードワインの存在と名称は公式ページで確定。曖昧性は構造的なものである）

---

## Sources

### ✅ 生産者公式（**採用ドメイン: `chateau-margaux.com`**）

| URL | 用途 |
|---|---|
| `https://www.chateau-margaux.com/fr/mentions-legales` | 🔴 **§2a 認証の主証拠。**SCA Château Margaux / RCS 321 152 993 / SIRET 321 152 993 000 10 / TVA FR 89 321 152 993 / 掲載責任者 Alexis Mentzelopoulos |
| `https://www.chateau-margaux.com/robots.txt` | 走査起点（`Allow: /`、sitemap 指定あり） |
| `https://chateau-margaux.com/sitemap.xml` → `sitemap_en.xml`（**358 URL**）／`sitemap_fr-FR.xml` | 🔴 **ラインナップとヴィンテージ範囲の機械的確定** |
| `/en/le-domaine/histoire` | 沿革全般、1855 年格付、Pavillon Rouge の由来、1925 年元詰め |
| `/en/le-domaine/le-terroir` | 🔴 **265 ha / 87 ha 赤 / 12 ha 白 / 126 区画 / 密度 6,666–10,000 / 樹齢 / 地質 / 有機転換** |
| `/en/le-domaine/les-femmes-et-les-hommes` | 🔴 **現行チーム（Alexis CEO 2023 年末〜、Alexandra、Bascaules、Vimal、Valance、de Rouffignac）** |
| `/en/savoir-faire/nos-engagements` | 環境の取り組み（2019 年専任職、ONF 調査、再エネ 100%、堆肥、水） |
| `/en/savoir-faire/le-travail-des-chais` | ⚠️ **醸造の技術記述が無いことの確認**（不在の証拠として使用） |
| `/en/savoir-faire/le-travail-de-la-vigne` | ⚠️ 同上（定性的導入のみ） |
| `/en/vins/grand-vin-du-chateau-margaux` | 選抜率 約 40% / 約 120,000 本 / 「Classified First Growth since 1855」 |
| `/en/vins/pavillon-rouge-du-chateau-margaux` | セカンド |
| `/en/vins/margaux-du-chateau-margaux` | 🔴 **サードの由来・1906 年命名・18 か月/新樽 25%・約 60,000 本・第 4 選抜** |
| `/en/vins/pavillon-blanc-du-chateau-margaux` | 白（SB 100%、12 ha、1920 年命名） |
| `/en/vins/pavillon-blanc-second-vin` | 🔴 **「五世紀で 5 本目」・2022 年産から・8 か月/新樽 20%・約 15,000 本** |
| `/en/vins/grand-vin-du-chateau-margaux-{1995,2005,2006,2010,2012,2015,2016,2019}` | 🔴 **OBP 8 本の公式確認・セパージュ・選抜率・2015 の特別意匠** |
| `/en/mon-vin/service` | 🔴 **提供温度 18–19°C（白 10–13°C）・デカンタージュ** |
| `/en/mon-vin/authentification` ／ `/en/mon-vin/les-millesimes` | 🔴 **真贋機能とその導入年（1989 / 1997 / 2011 / 2026）** |
| `/en/500-ans` | ⚠️ **見出しのみで実質的な記述が無いことの確認** |

### 🏛 公的登記・法定文書

| URL / 識別子 | 用途 |
|---|---|
| `https://recherche-entreprises.api.gouv.fr/search?q=321152993` | 🔴 **SIREN/SIRET/NAF/住所/dirigeants/`liste_id_bio`。§2a 認証の対照側** |
| `https://recherche-entreprises.api.gouv.fr/search?q=margaux&activite_principale=01.21Z&departement=33` | 🔴 **同名他社の実測（48 件）。disambiguation の証拠** |
| `https://opendata.agencebio.org/api/gouv/operateurs/?siret=32115299300010` | 🔴 **exact-SIRET 照会（`nbTotal: 1`）。Ecocert / FR-BIO-01 / ENGAGEE / C1 / 2023-07-18 / mixite Oui** |
| `https://certificat.ecocert.com/entreprise/C503EC86-1ABA-44D2-AE04-5EA007617FE9` | 🏛 Agence Bio が返した Ecocert 証明書 URL（**登録値として記録。本文には未使用**） |
| `https://extranet.inao.gouv.fr/fichier/3-CDC-Margaux.pdf` | 🔴 **CDC「Margaux」2022 年 PNO 版。`%PDF` 検証済（162,062 bytes）。赤専用条項・5 コミューン・品種・密度** |
| `https://extranet.inao.gouv.fr/fichier/PNOCDCMargaux.pdf` | 🔴 **CDC「Margaux」2010 年 PNO 版。`%PDF` 検証済（147,554 bytes）。赤専用条項が同一であることの確認＋旧コミューン名** |
| `https://www.inao.gouv.fr/produit/margaux-17485` | 🏛 **認定日 1954-08-10／現行版は 2023-03-31 arrêté（JORF 2023-04-05・BO n°15 2023-04-13）** |
| `https://gcc-1855.fr/the-1855-grand-cru-classification/` | ⚠️ **Château Margaux が Premiers Crus に「Château MARGAUX」として掲載されていることのみ確認**（後述） |

### 🔴 §2c の罠 —— **実際に踏んだので記録する**

🔴 **`info.agriculture.gouv.fr/gedei/site/bo-agri/document_administratif-{PNOCDCMargaux, PNOCDC-Margaux, PNO2023AOPMargaux, CDCMargaux}.pdf`
の 4 通りすべてが `HTTP 200` を返したが、body の先頭は `<html`（8,354 bytes、全部同一サイズ）。
`%PDF` 検証をしていなければ、4 件とも「取得成功」と誤認していた。**
→ **正解は `extranet.inao.gouv.fr/fichier/` 配下だった。**

🔴 **さらに取得できた 2 つの PDF は**どちらも**「procédure nationale d'opposition」版**であり、
冒頭に **「取消線 XXX は削除提案、太字は変更提案」** の AVERTISSEMENT を持つ。
→ 🔴 **本ドシエは、この 2 つの PDF から数値を引用していない。
　引用したのは「赤専用」条項・コミューン名・認可品種のみで、
　いずれも取消線でも太字でもなく、2010 年版と 2022 年版で文言が一致するものに限った。**

### ⚠️ §2a で **保留**した（＝本文の事実根拠として使っていない）ドメイン

| ドメイン | 判定 | 理由 |
|---|---|---|
| **`gcc-1855.fr`**（Le Conseil des Grands Crus Classés en 1855） | ⚠️ **限定使用** | 🏛 **`CONSEIL DES GRANDS CRUS CLASSES EN 1855`（SIREN `484841663`、NAF `94.11Z`、1 cours du XXX Juillet 33000 Bordeaux）が登記に実在し、団体名は一致する。**<br>🔴 **だがサイト側の mentions légales は年齢確認ゲートと JS の背後にあり、SIREN の相互確認まで到達できなかった。**<br>→ **「Château MARGAUX が Premiers Crus に載っている」という一点のみ参照し、
格付の歴史・件数・20/20 の逸話などの事実根拠には使っていない。** |

🔴 **本調査では、ドメイン乗っ取り・パーキング・ファンサイト・同名他社の類は 1 件も遭遇しなかった。**
**`chateau-margaux.com` は mentions légales の SIREN/SIRET が登記と完全一致し、
かつ Agence Bio の登録が同ドメインを `Site Officiel` として相互に指している（二重確認）。**

### 🚫 使用していない（§2 の禁止に該当）

**Wikipedia（`en.wikipedia.org` / `fr.wikipedia.org`）／Decanter ／The Drinks Business ／Wine Spectator ／
Wine.com ／Bordeaux Index ／Lay & Wheeler ／Haute Living ／Vertdevin ／Big Hammer Wines ／
Comptoir des Millésimes ／winewithseth.com。**
🔴 **これらは検索結果に現れたが、事実根拠として一切参照していない。**
⚠️ **とくに 2015 年の特別ボトルについては複数の第三者媒体が報じているが、
本ドシエは生産者自身のヴィンテージページの記述のみを採用した（第三者側の記述は読んでいない）。**

---

## Open Questions

1. 🔴 **【物理ラベル】2015 年（OBP 3 行目・$6,890）の現物確認。**
   ✅ **公式は「通常のラベルの代わりに、ガラスに直接スクリーン印刷した特別意匠」と明記している。**
   → **現物に通常の紙ラベルがあれば、それは 2015 年のグラン・ヴァンではない。**
   **確認すべき: ①紙ラベルの有無 ②スクリーン印刷の有無 ③木箱の意匠。**
2. 🔴 **【要調査】`Pavillon Blanc du Château Margaux` の実際のアペラシオン。**
   🏛 **AOC Margaux でないことは法定文書で確定した。**
   ⚠️ **だが公式サイトは白のアペラシオンを一度も明記しておらず、`Bordeaux` という語も出てこない。**
   → **現物のラベル、または EU eAmbrosia / 出荷書類での確認が要る。**
   **（OBP 8 行はすべて `RED` セクションなので、8 行の同定には影響しない。）**
3. 🔴 **【チームへの依頼】醸造の技術情報が公式に存在しない。**
   **`/en/savoir-faire/le-travail-des-chais` はバーチャルツアーへの誘導のみである。**
   🔴 **「六つの形」のうち該当するのは「material exists but is gated」に近いが、正確には
   「site is live and actively maintained, but the winemaking section publishes no technical content」——
   これは 6 形のどれとも一致しない新しい形である。**
   **`archive recovery` が効く可能性はある（旧サイトが技術情報を載せていた可能性）が、本調査では試していない。**
   → **fiche technique があればチームから供給を受けたい。**
4. 🔴 **【物理ラベル】8 行それぞれについて、グラン・ヴァン／Pavillon Rouge／
   Margaux du Château Margaux のどれかを現物で確定する。**
   **印字文字列と公式資料だけでは、5 行が 3 候補、3 行（1995/2005/2006）が 2 候補までしか絞れない。**
   **確認すべきは正面ラベルの表示名である**（`GRAND VIN` / `PAVILLON ROUGE DU CHÂTEAU MARGAUX` /
   `MARGAUX DU CHÂTEAU MARGAUX`）。
5. ⚠️ **【要調査】`Margaux du Château Margaux 2016` のページが存在しない理由。**
   **sitemap にも無く、直接アクセスも 404。だが 2017 年のページ本文は「the 2016 vintage」に言及している。**
   → **製品として存在しないのか、ページが未作成なのか、公式からは判断できない。**
   **（同様に 2020 年以降のサードのページも存在しない。）**
6. ⚠️ **【要調査】1995 年と 2005 年のセパージュ完全比率。**
   **1995 は公式に記載が無く、2005 は CS 85% / Merlot 8% までで残り 7% が非公表である。**
7. 🔴 **【物理ラベル・真贋】OBP 8 本の真贋確認機能はヴィンテージによって異なる。**
   ✅ 公式の導入年に基づく期待値:
   - **1995**: **レーザー刻印**（1989 年開始、**1995 年産から全ボトルに体系適用**）。**瓶底エンボスは無いはず**（1997 年〜）
   - **2005 / 2006 / 2010**: **レーザー刻印 ＋ 瓶底エンボス。Prooftag は無いはず**（2011 年〜）
   - **2012 / 2015 / 2016 / 2019**: **レーザー刻印 ＋ 瓶底エンボス ＋ Prooftag Bubble Code**
   → 🔴 **期待値と現物が食い違ったら、真贋そのものを疑う理由になる。**
   ⚠️ **QR コード付きシールは「2026 年 1 月 1 日以降に蔵を出たボトル」に付く。
   古いヴィンテージでも 2026 年以降の出庫なら付きうる点に注意。**
8. ⚠️ **【要調査】canonical の unsourced 9 件（木製円錐台形発酵槽・卵白 6 個・自社樽工房・
   収穫 1,000 人体制など）の出所。**
   **公式サイトには無い。旧サイトか、印刷物か、第三者由来かを特定する必要がある。**
   → **`P-*` の解決には出所の特定が要る。**
9. ⚠️ **【要確認】1855 年格付の「20/20 満点は Château Margaux のみ」の一次的裏付け。**
   **生産者自身の沿革ページにしか見つからなかった。**
   **`gcc-1855.fr` は掲載一覧であって、採点の記録を公開していない。**
