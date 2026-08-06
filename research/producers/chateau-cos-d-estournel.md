# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 2 件存在する**（`cos-destournel-1855` / `cos-destournel-parker-profile`）。
> **本書は昇格前の研究記録であり、canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト `www.estournel.com` で確認**（一次資料。§2a 認証済み）
> `🏛` **公的登録簿 / 法定文書**（`recherche-entreprises.api.gouv.fr` ／ Agence Bio ／ INAO *cahier des charges*）
> `📄` 生産者自身の旧ページの Internet Archive 復元（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://www.estournel.com/`（FR 原本 / EN / CN）**
> 走査元: **`robots.txt` が `Sitemap: https://www.estournel.com/fr/sitemap_aio.xml` を明示**
> → index → `post` 221 / `page` 66 / `hub` 64 = **351 URL を全数取得**（3 言語混在）
> 併用: 🏛 **INAO *cahier des charges* AOC「Saint-Estèphe」**（`extranet.inao.gouv.fr`。PDF 実体検証済）
> 併用: 🏛 **Agence Bio opendata（exact-SIRET 照会）**／🏛 **`recherche-entreprises.api.gouv.fr`**
> 併用: ✅ **公式 WooCommerce REST（`/wp-json/wp/v2/product`、100 件）**——公式が現に販売している商品名の一次証拠
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ① —— OBP の WHITE 2 行は「メニューが間違っている」とは言えない。間違っているのは
> *どの列か* である。**
> 🏛 **AOC「Saint-Estèphe」の *cahier des charges* は「L'appellation d'origine contrôlée « Saint-Estèphe »
> est réservée aux vins tranquilles rouges.」と明記し、認可品種は cabernet franc N / cabernet-sauvignon N /
> carmenère N / cot N / merlot N / petit verdot N ——白品種は 1 つも無い。**
> ✅ 一方で **`Cos d'Estournel Blanc`（初ヴィンテージ 2005）と `Pagodes de Cos Blanc`（初ヴィンテージ 2018）は
> 実在し、2018 も 2019 も公式ページに掲載されている。**
> → **すなわち「色セクション」は正しく、誤っているのは *ワイン名列に印字された `Saint-Estèphe`* である。**
> **メニューは「アペラシオン列」に AOC でありえない文字列を入れている。** → §Canonical Conflict `C-6` ①
>
> 🔴 **本ドシエ最大の収穫 ② —— `C-6` の前提分割（Batch 10 の指摘）に、決定的な実測が出た。
> 欠陥は「検知の失敗」ではなく「層をまたぐ伝播の喪失」である。**
> 🔴 **intake 層は正しく検知している。** 🔍 `obp_intake_normalized_20260804.json`（全 **704 行**）の
> `source_quality_flags` は、WHITE 2019 に `section_colour_conflict`、WHITE 2018 に
> `cross_section_duplicate` + `section_colour_conflict`、RED 2018 に `cross_section_duplicate` を立てている。
> 🔴 **`section_colour_conflict` は 704 行中わずか 3 回。うち 2 回が本件である
> ——メニュー全体で最も稀な欠陥型の 3 分の 2 を、この 1 生産者が単独で占めている。**
> 🔴 **しかしこのフラグは store 層に渡っていない。** `shells.json` / `inventory.json` の該当行は
> すべて `flags: []`、`mapping.json` には色の軸自体が無い。
> 🔍 store 層で「`RED`/`WHITE` を厳密にまたいで 1 shell に集約された」shell は 20 件。
> うち 11 件は `producer` レベル（＝正しい挙動。生産者は両色を造る）、
> `product` レベルが 5 件、`release` レベルが 4 件（＝欠陥）。Bordeaux の release 級はこの Cos の 1 件のみ。
> 🔴 **本件の release shell `rs:rel:1354e538b20bd449` は、
> WHITE 2018（$680）と RED 2018（$900）を 1 つに畳み、代表 `source_transcription` に WHITE 側だけを残し、
> `$900` を捨てている。**
> → **`C-6` は「canonical の構造」と「matcher の入力」の 2 欠陥ではなく、
> 「intake 層が検知した色の衝突が store 層の release 識別キーに伝播しない」という
> 第 3 の、より具体的な形を持つ。** → §Canonical Conflict `C-6` ②
>
> 🔴 **本ドシエ最大の収穫 ③ —— canonical には「批評家の参考書の項目」がワインレコードとして
> 37 件入っている。ブリーフが指摘した 1 件は氷山の一角だった。**
> 🔍 `classification` または `name` が Parker を名指すレコードは **928 件中 37 件（4.0%）**。内訳は
> **`Vintage Reference — Parker's Bordeaux` 34 件**（`producer = "Bordeaux"`、`vintage` に 1970 等の
> **実在する年号が入る**）／**`Château Profile — Parker's Bordeaux` 2 件**（Cos と Calon-Ségur）／
> **`Appellation Reference — Parker's Bordeaux` 1 件**（`producer = "Saint-Estèphe"`）。
> 🔴 **34 件は `color: "Rouge"`・`obp_format: "By the bottle"`・`food_pairings`・`glassware`・`serving_temp` を
> 完備しており、スキーマ上「売れるボトル」と区別がつかない。**
> → **unnumbered — CTO's call**（§Canonical Conflict ④）
>
> 🔴 **本ドシエ最大の収穫 ④ —— `Château Cos Labory` はもはや「別の生産者」ではない。**
> ✅ 公式サイトが「**Château Cos Labory, dernière acquisition de Michel Reybier au cœur de l'appellation
> Saint-Estèphe**」と記し、🏛 登録簿では旧運営会社（SIREN 334353885）が **2024-12-31 に閉鎖**、
> **DOMAINES REYBIER（SIREN 331321109）の établissement `33132110900042` が「CHATEAU COS LABORY」住所に
> 活動中**、かつ本体 siège の `date_debut_activite` が **2025-01-01**。
> → canonical `cos-labory-1855` の「オードワ家が現在まで所有」は **stale**。→ §Canonical Conflict ⑤
>
> ⚠️ **調査上の到達できなかった点 2 件（Open Questions 参照）**
> **① `Cos d'Estournel Blanc` / `Pagodes de Cos Blanc` の AOC 名を、公式は一度も書いていない。**
>    公式サイト 351 URL、公式 WooCommerce 商品 100 件、公式ボトルショット、公式 PDF —— どこにも
>    アペラシオン欄が存在しない。**INAO 側から「Saint-Estèphe ではありえない」ことは確定できるが、
>    「では何か」は公式から取れない。** 実ラベル確認が要る。
> **② `www.inao.gouv.fr/produit/saint-estephe-16807` は `HTTP 403`（WAF）。**
>    **gated — not evidence of absence.** *cahier des charges* 本体は extranet から PDF 実体で取得済。

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`Cos d’Estournel`**（`producer_heading`。**U+2019**、`Château` 無し）<br>ワイン名列は 4 行とも **`Saint-Estèphe`**（＝キュヴェ名ではなくアペラシオン） |
| **公式表記（本文）** | ✅ **`Cos d’Estournel`**。**`Château` を付けない形が圧倒的**<br>🔍 実測（公式 6 ページの生 HTML）: `Château` 前置 **14 回** / 無し **444 回**。アポストロフィは **U+2019 が 284 回・U+0027 が 174 回**——**公式サイト自身が両方を混用している**（同一ナビ内で `Cos d’Estournel` と `Cos d'Estournel Blanc` が並ぶ） |
| **公式表記（法定・フッター）** | ✅ **`Château Cos d’Estournel, 33180 Saint-Estèphe, France`**（*mentions légales* の siège social／全ページのフッター） |
| 🔴 **登録法人名** | 🏛 **`DOMAINES REYBIER`** ——**「Château Cos d'Estournel」という法人は存在しない**<br>✅ *mentions légales*: 「**DOMAINES REYBIER / Société Anonyme au capital de 121 000 euros / RCS Bordeaux n° 331 321 109**」 |
| **SIREN / SIRET** | 🏛 **SIREN `331321109`** ／ **siège SIRET `33132110900018`** |
| **NAF** | 🏛 **`01.21Z`**（Culture de la vigne）。`activite_principale_naf25` = `01.21Y` |
| **法形態 / 設立** | 🏛 nature juridique **`5699`**（SA à directoire）／ `date_creation` **1972-01-01**／ état **`A`（活動中）** |
| **規模** | 🏛 effectif tranche **`21`**（2023 年基準）／ établissements **4 件・全て開設中** |
| **住所（登録簿の綴り）** | 🏛 **`COS D ESTOURNEL 33180 SAINT-ESTEPHE`**（**アポストロフィ無し・`Château` 無し**）<br>座標 `45.23115424, -0.776566953` |
| 🔴 **4 事業所** | 🏛 `33132110900018` COS D ESTOURNEL ／ `01.21Z` ／ **bio id `32168`**<br>🏛 `33132110900026` LEYSSAC ROUTE DE POUMEYS ／ `55.10Z`（ホテル業＝La Maison d'Estournel）<br>🏛 `33132110900034` 1 ETAGE CHT COS D ESTOURNEL ／ `68.20A`<br>🔴 🏛 `33132110900042` **CHATEAU COS LABORY** ／ `01.21Z` ／ état `A` |
| **経営陣** | 🏛 **Aude AUGENBLICK（旧姓 REYBIER、1973 年生）— Présidente du directoire**（＝*mentions légales* の représentant légal と一致）<br>🏛 **Michel REYBIER（1945 年生）— Président du conseil de surveillance**<br>🏛 **Raphaël REYBIER（1974 年生）— Membre du directoire**<br>🏛 **Anne-Flore CARPENTIER ALTING（旧姓 REYBIER、1976 年生）— Vice-Président**<br>🏛 **CMJ HOLDINGS S.A. — Membre du conseil de surveillance**／CAC: PwC Entrepreneurs |
| **技術責任者** | ✅ **Dominique Arangoïts（Directeur technique / Technical Director）** |
| **白の醸造担当** | ✅ **Angélique Meynieu**（「responsable de la vinification de Cos d'Estournel Blanc」。2015 年の公式記述） |
| **所有** | ✅ **Michel Reybier、2000 年より所有**（「Owner of Cos d'Estournel since 2000」） |
| **連絡先** | ✅ `estournel@estournel.com` ／ `+33 (0)5 56 73 15 50`（*mentions légales*） |
| **canonical id** | 🔍 **`cos-destournel-1855`** と **`cos-destournel-parker-profile`** の 2 件。**どちらも `vintage = "—"`** |

### ⚠️ 同名・近似名の罠（`D-2026-08-05-08`）

**Bordeaux は本 register で最悪の条件だった。実際に踏んだ・回避した 4 件を全て記す。**

| # | 名前 | 実体 | 判定 |
|---|---|---|---|
| 1 | 🔴 **`LE COS D 'ESTOURNEL`** — SIREN `521310367` | 🏛 **Doubs 県 Vuillafans の不動産会社（NAF `68.20B`）。2023-12-30 閉鎖。ワインと無関係** | 🔴 **`recherche-entreprises` に `q=COS D'ESTOURNEL` を投げると *これが 1 位で返る*。**郵便番号 `33180` で絞らないと確実に誤認する |
| 2 | 🔴 **`Château Cos Labory`** — 別の Saint-Estèphe シャトー（1855 年 5 級） | 🏛 旧運営 `CECILE AUDOY (WEBER)` SIREN `412755134`（2006-08-31 閉鎖）→ `SOCIETE CIVILE D'EXPLOITATION DES DOMAINES REYBIER` SIREN `334353885`（**2024-12-31 閉鎖**）→ **現在は DOMAINES REYBIER の établissement `33132110900042`** | 🔴 **「Cos」トークンを共有する別シャトーだが、2025-01-01 以降は同一の法人が運営している。**「別の生産者だから無関係」という切り分けが *今は成立しない* |
| 3 | **`SAS GOULEE`** — SIREN `482243698` | 🏛 CHATEAU COS D'ESTOURNEL 住所。2005-05-10 設立、**2011-06-30 閉鎖**（siège は 2007-09-24 に閉鎖済） | Goulée 専用法人は既に消滅。ワインは 2018 まで継続（✅） |
| 4 | **`MJ FRANCE`** `433918182` / **`BEMER (LA CHARTREUSE)`** `841622145` / **`CHAPON FIN`** `428928667` | 🏛 いずれも `COS D'ESTOURNEL` 住所に登記されているが NAF は `70.10Z` / `55.10Z` / `70.2C`（＝持株・ホテル・経営コンサル）。**ブドウ栽培ではない** | 住所一致だけでは生産者と断定できない例 |

🔍 **canonical 928 件の全数走査（`D-2026-08-05-08`）**:
`Estournel` / `Cos Labory` を **identity フィールド（`producer` + `name`）に持つのは 3 件**
（`cos-destournel-1855` / `cos-destournel-parker-profile` / `cos-labory-1855`）。
🔴 **一方、散文（`description` / `obp_note` / `tasting`）にだけ現れるのは 7 件。**
`bordeaux-vintage-1970-guide` / `-1991-` / `-1993-` / `-1995-` / `saint-estephe-appellation-parker` /
`lafon-rochet-1855` / 🔴 **`leroux-auxey-duresses`（ブルゴーニュの Auxey-Duresses Rouge。
「Benjamin Leroux が Cos d'Estournel で研修した」という *経歴文* にヒットする）**。
→ **`"Cos d'Estournel"` の素朴な部分一致は 10 件を返し、そのうち 8 件が偽陽性（80%）。**

---

## Overview

✅ **サン=テステフ村の入口、メドック北部の起伏地に建つ 1855 年格付 2 級。**
✅ 「**cos**」は **古いガスコーニュ方言の「小石の丘」**に由来する、と公式が明記している。
✅ **東洋風パゴダを戴く château は、創設者 Louis Gaspard d'Estournel の異国趣味の産物**であり、
公式自身が彼を「**Maharajah of Saint-Estèphe**」と呼んでいる。

✅ **現在の畑は 100 ヘクタール。** カベルネ・ソーヴィニヨンが「この貴重なモザイクの 3 分の 2」を占め、
メルロがそれに次ぎ、カベルネ・フランとプティ・ヴェルドが少量。
**樹齢は平均 45 年**、うち **グラン・ヴァンに使われる樹の平均樹齢は 55 年**。
**最古の樹は 20 世紀初頭に遡る**と公式は書く。

🔴 ✅ **公式が現に掲げるレンジは 6 つであり、「グラン・ヴァン＋セカンド」の 2 本立てではない。**
`Cos d'Estournel` ／ `Cos d'Estournel Blanc` ／ `Pagodes de Cos` ／ `Pagodes de Cos Blanc` ／
`G d'Estournel` ／ `Goulée by Cos d'Estournel`。
**このうち 2 つが白**である——これが OBP の 4 行を読むための唯一の鍵である。

⚠️ **公式サイト自身に内部矛盾がある。** Michel Reybier のページは「**5 つの畑が Domaines Reybier を成す**」
（Cos d'Estournel / Hétszőlő ハンガリー 2009 / シャンパーニュのキュヴェ 2013 / La Mascaronne プロヴァンス
2020 / Lauzade 2021）と書くが、**同じサイトの別ページが Château Cos Labory を「Michel Reybier の最新の
買収」と告知している**。**片方が更新されていない。両論を残す。**

---

## History

✅ 公式の記述は人物ページに分散しており、年表ページは存在しない。以下は公式が明示的に書いた事項のみ。

| 年 | 出来事 |
|---|---|
| **1791** | 🔴 ✅ **Louis Gaspard d'Estournel が Cos と Pomys を *相続* する**（「inherited Cos and Pomys in 1791」）。<br>🔴 **canonical の「19 世紀初頭に創設」は、この公式記述と噛み合わない** |
| **（時期記載なし）** | ✅ **畑を 14 ha から 45 ha に拡張。**ガラス栓の使用など技術革新を導入し、新品種を試した |
| **1838** | ✅ **インド駐留の英国士官が彼のワインを飲み始める。**「新市場の追求が彼をアジアへ向かわせた」 |
| **（時期記載なし）** | ✅ **債務返済のため一度売却し、後に買い戻している**（公式が自ら書いている）<br>⚠️ **売却先の名は公式に無い。** canonical の「1853 年エルランジェ銀行に売却」は公式では裏が取れない |
| **1853** | ✅ **Louis Gaspard d'Estournel 死去**（公式は「1855 年格付の 2 年前に亡くなった」と記す。年号そのものは書いていない） |
| **1855** | ✅ **1855 年ボルドー格付が Cos d'Estournel を Second Growth として公式に認定。**<br>✅ なお彼は生前に「**Deuxième Grand Cru du Médoc**」の呼称をボルドーのネゴシアンから得ていた |
| **2000** | ✅ **Michel Reybier が取得。**「Cos and only Cos」 |
| **2001** | ✅ **畑の土壌調査を実施し、精密な土壌地図を作成。「20 に近い変異」の存在が明らかになる** |
| **2005** | 🔴 ✅ **`Cos d'Estournel Blanc` 初ヴィンテージ。**「Cos d'Estournel produced its first ever white wine」 |
| **2008** | ✅ **重力式の新セラーが稼働**（「Made using gravity flow in the new cellar」= 2008 年の白の記述） |
| **2009 / 2013 / 2020 / 2021** | ✅ Reybier の畑の拡大: Hétszőlő（ハンガリー）／シャンパーニュのキュヴェ／La Mascaronne（プロヴァンス）／Lauzade |
| **2018** | 🔴 ✅ **`Pagodes de Cos Blanc` 初ヴィンテージ**（「the first vintage of Pagodes de Cos Blanc」） |
| **2018** | ✅ **`Goulée by Cos d'Estournel` の最終掲載ヴィンテージ** |
| **2019** | ✅ **`G d'Estournel` の初掲載ヴィンテージ**（メドック北部） |
| **2024 / 2025** | 🏛 **Château Cos Labory の運営が DOMAINES REYBIER に統合**（旧法人 2024-12-31 閉鎖／本体 siège の活動開始日 2025-01-01） |

---

## Location

✅ **サン=テステフ村（メドック最北の村アペラシオン）の入口。ジロンド河口と大西洋のあいだ。**
✅ 公式は「**より顕著な海洋性気候が極端な天候を和らげる。冬は厳しくなく、夏の熱波も弱い。
熟成は穏やかに進み、複雑さと香りの鮮度に有利。頻繁に吹く風は過剰な湿気を乾かし空気を浄化する**」と書く。

✅ **土壌**: 中心は「**深い砂利の台地**」。そこから東向きと南南西向きに 2 つの丘が下る。
**粘土の脈が畑を斜めに走る。** メルロは東側の**粘土石灰質**に、カベルネ・ソーヴィニヨンは**排水が最良の
台地最高部**に植えられている。
✅ **2001 年の土壌調査で「20 に近い変異（nearly twenty variants）」が確認された。**

### 🏛 AOC「Saint-Estèphe」の *cahier des charges*

| 項目 | 法定文 |
|---|---|
| **初認定** | **décret du 14 novembre 1936** |
| 🔴 **色・製品種別** | 🔴 **「L'appellation d'origine contrôlée « Saint-Estèphe » est réservée aux vins tranquilles rouges.」**<br>**＝赤の静止ワインのみ。白もロゼも泡も存在しない。** |
| **地理的範囲** | 「la commune de Saint-Estèphe du département de la Gironde」——**収穫・醸造・仕上げ・熟成の全てが同村内** |
| **区画範囲** | 1994-09-08 の comité national 承認による parcellaire |
| 🔴 **認可品種** | **cabernet franc N / cabernet-sauvignon N / carmenère N / cot N / merlot N / petit verdot N**<br>🔴 **全て黒ブドウ（`N`）。白品種は 1 つも列挙されていない。**「色は赤のみ」は品種表からも独立に裏付けられる |
| **収量** | rendement `57 hl/ha` ／ rendement butoir `63 hl/ha`（特定条件下 `60 hl/ha`） |

⚠️ **出典レイヤーの正直な注記（§2c）**: この PDF は **`extranet.inao.gouv.fr/fichier/PNOCDCSaint-Estephe.pdf`**
（2010-10-21 の常設委員会意見に続く **procédure nationale d'opposition（PNO）文書**）である。
**先頭に `%PDF` を確認済**（ファイル名の罠は回避した）。**PNO 文書は変更点を太字、削除予定を打ち消し線で示す**が、
上記「réservée aux vins tranquilles rouges」の一文は**変更・削除のマーキングを受けていない本文**である。
🔴 **とはいえ厳密には consolidated 版ではない。** `www.inao.gouv.fr/produit/saint-estephe-16807` は
**`HTTP 403`（WAF）で取得できなかった —— gated, not evidence of absence。**
**「1936 年以来赤のみ」という結論は、品種表という独立の内部証拠と整合しており、本書はこれを採る。**

⚠️ **公式サイトはアペラシオン名を一度も印字していない。** 351 URL・商品 100 件・PDF・ボトルショットを
走査したが、`AOC` / `Appellation` / `Saint-Estèphe contrôlée` を製品に紐づける記述は皆無。
公式が Saint-Estèphe に言及するのは**村名・「メドック最北の村アペラシオン」という一般記述としてのみ**。

---

## Farming

### 🏛 Agence Bio —— **exact-SIRET `33132110900018` 照会**（名前検索ではない）

| 項目 | 登録値 |
|---|---|
| `numeroBio` | **`32168`** |
| `raisonSociale` | **`DOMAINES REYBIER`** |
| 🔴 `denominationcourante` | 🔴 **`DOMAINES PRATS`** ——**登録簿が旧商号を今も保持している** |
| `gerant` | `MICHEL REYBIER` ／ `codeNAF` `01.21Z` ／ `dateMaj` **2024-04-10** |
| **認証機関** | 🔴 **`Ecocert France`（`FR-BIO-01`）** |
| 🔴 **`etatCertification`** | 🔴 **`ENGAGEE`**（＝**転換に関与中。「認証済（certifié）」ではない**） |
| 🔴 **`dateEngagement` / `datePremierEngagement`** | 🔴 **`2021-08-16`** |
| `activites` | **`Production` / `Préparation` / `Distribution`** |
| 🔴 `mixite` | 🔴 **`Oui`** ——**bio と非 bio が同一経営内に併存している** |
| **`productions`（2026 管理年度）** | `Raisin de cuve` → **`C1` / `C2` / `C3` / `CS` / `AB` が同時に立つ**（＝区画ごとに転換段階が異なる）<br>`Vins de raisin` → **`CNS` / `AB`**<br>`Prairie permanente` → `AB`／`Jachère` → `CS`・`AB`／`Commerce de gros de boissons alcoolisées` → `AB` |
| **活動場所** | `Château Cos d'Estournel, 33180 Saint-Estèphe`（siège social 兼）／`ZAC Saint Laurent Médoc, 33112` |

### 🔴 温度差の罠（`D-2026-08-05` 系。Moussé・Giraud・Dauvissat に次ぐ 4 例目）

🔴 **OBP の 4 本は 2015 / 2018 / 2018 / 2019。転換開始 `2021-08-16` を 2〜6 年 *遡る*。**
🔴 **したがってこの 4 本について「オーガニック」とも「オーガニックではない」とも言ってはならない。**
**さらに `mixite = Oui` かつ `Raisin de cuve` に `C1`〜`CS` が並存している以上、
「2026 年の Cos は bio である」という現在形の断定すら、畑全体には成立しない。**

⚠️ **HVE / Demeter / その他の認証**: 公式サイト 351 URL に記載は無く、本調査では公的登録簿からも確認できなかった。
**「取得していない」ではなく「確認できていない」。** → Open Questions 4

✅ **公式が語る栽培（認証とは別）**: 「生垣を植える」「最も適した道具を選ぶ」「治療的ではなく予防的に取り組む」
「可能な限り自然で生態学的な栽培技術に向けて何も惜しまない」。**マッサル・セレクション**（最も畑の個性を体現する
株を選び、その穂木で若木を育てる）を「畑の継承の担保」として明示している。

---

## Winemaking

✅ **重力式（gravity-flow）の醸造棟。** 公式は「重力の法則に完全に基づく最先端の醸造設備の設計と設置」を
Reybier 期の主要投資として挙げ、白の 2008 年の記述にも「Made using gravity flow in the new cellar」と書く。

✅ **グラン・ヴァンの品種構成はヴィンテージごとに変動する（固定比率ではない）。** 公式掲載値:

| ヴィンテージ | Cos d'Estournel（赤） |
|---|---|
| **2015** | **CS 75% / Merlot 23,5% / Cabernet Franc 1,5%** |
| **2018** | **CS 74% / Merlot 23% / Cabernet Franc 2% / Petit Verdot 1%** |
| **2019** | **CS 65% / Merlot 35%** |
| 2024 | CS 60% / Merlot 38% / CF 1,5% / PV 0,5% |
| 2025 | CS 60% / Merlot 39% / PV 1% |

⚠️ **公式は醸造の数値（新樽比率・熟成月数・発酵日数・MLF の場所・清澄/濾過）を一切公開していない。**
canonical はこれらを数値で持っているが、**その出所は公式ではない。** → §Canonical Conflict

---

## Style

**以下はすべて公式（生産者自身）の語彙のみ。第三者の評価語は含めない。**

✅ **Cos d'Estournel（赤）— 「FASCINATING, OPULENT, VOLUPTUOUS」／「遠い土地の呼び声」**
「孤独な航海から戻った冒険者のように謎めき、Cos d'Estournel はゆっくりとしか自らを明かさない。
少しずつ、見慣れぬ果実と香辛料と品々に溢れた market stall、宴の熱と沈む陽、
豊麗な曲線を持つ婦人たちの姿を語りはじめる。無数の香り、色、味が感覚に訴える。
慎み深くありながら、意図された官能。」

✅ **Cos d'Estournel Blanc — 「KEEN, POWERFUL, IMPETUOUS」／「元素の力」**
「他に類のない性格を持ち、Cos d'Estournel Blanc は海水の飛沫の冷たさと顔を打つ塩気の風を喚起しながら、
同時に大地の温かさと豊かさを呼び起こす。寛大で生命力のあるワインで、
マルメロのジャムを厚く塗ったパン、陽を浴びた秋の果実の露店、
最も甘美な夏の瞬間の不意の記憶を思わせる。」

✅ **Pagodes de Cos — 「VIBRANT, SILKY, SEDUCTIVE」**／✅ **Pagodes de Cos Blanc — 「INTENSE, DELICATE, INTIMATE」**
✅ **G d'Estournel — 「EXQUISITE, ALLURING, ELEGANT」**／✅ **Goulée — 「ETHEREAL, DELECTABLE, GENEROUS」**

✅ **白の供出（公式）**: 「**開栓してすぐ供する。デカンタージュはしない。10〜11°C に保つ。**
収穫後 3 年は果実と花の強い香り。4〜5 年でトースト香と丸みが出て、香りの表現の頂点に向かって深みを増す。」

---

## Important Cuvées

### ✅ 公式の現行レンジ（全 6 種。ナビゲーション＋ `hub` サイトマップで全数確認）

| # | 名称（公式表記） | 公式掲載ヴィンテージ範囲 | 公式が明示する事項 |
|---|---|---|---|
| 1 | **Cos d'Estournel** | **1928 → 2025**（1928/1929/1933/1947/1948/1949/1959/1961/1971/1975/1976/1982/1985/1986/1988/1989/1990/1991/1995/1996/1998〜2025） | ✅ グラン・ヴァン。平均樹齢 55 年の古樹 |
| 2 | 🔴 **Cos d'Estournel Blanc** | 🔴 **2005 → 2025（欠年なし）** | 🔴 ✅ **初ヴィンテージ 2005。**「Cos d'Estournel produced its first ever white wine」<br>**Sauvignon Blanc + Sémillon。2019 = SB 65 / Sém 35。2018 = SB 67 / Sém 33** |
| 3 | **Pagodes de Cos** | **2000 → 2025** | ✅ 「Cos d'Estournel's **"Other Grand Vin"**」。平均樹齢 40 年の専用テロワール<br>⚠️ **公式の掲載は 2000 年からで、canonical の「1994 年〜」は公式では確認できない** |
| 4 | 🔴 **Pagodes de Cos Blanc** | 🔴 **2018 → 2025** | 🔴 ✅ **初ヴィンテージ 2018**（「the first vintage of Pagodes de Cos Blanc」）<br>**2019 = SB 88 / Sém 12。2018 = SB 93 / Sém 7**<br>🔴 **canonical はこのワインの存在を知らない** |
| 5 | **G d'Estournel** | **2019 → 2025** | ✅ メドック北部。2012 年に高密植した CS が骨格を与える<br>🔴 **canonical はこのワインの存在を知らない** |
| 6 | **Goulée by Cos d'Estournel** | **2005 → 2018** | ✅ 「**northernmost reaches of the Médoc**」——**サン=テステフではない**。Merlot 主体（2018 = Me 73 / CS 21 / CF 6）<br>🏛 専用法人 `SAS GOULEE` は 2011-06-30 に閉鎖済 |

⚠️ **公式レンジに `Gris de Cos` も `Cos Blanc` も無い。** canonical `cos-destournel-1855` はこの 2 語を挙げるが、
公式の現行ラインナップには存在しない。**（`Cos Blanc` は `Cos d'Estournel Blanc` の誤記と *思われる* が、
本書は推測しない。両論を残す。）**

---

### 🔍 OBP の 4 行 —— 1 行ずつ

**全 4 行に共通**（store 層 `research/out/t-01/inventory.json`）:
`document = beverage_menu_bottles.doc` ／ `section_start_page = 17` ／
`producer_heading = producer_or_brand = "Cos d’Estournel"`（U+2019）／
`product_name = ""` ／ `classification_text = "Saint-Estèphe"` ／ `layout = producer_heading` ／
`resolved_to = research_shell` ／ `canonical.producer = producer:chateau-cos-d-estournel`。
**4 行すべてが 1 つの product shell `rs:pro:29cab5c232001817` に集約されている。**

🔴 **品質フラグは層によって異なる。必ず層を名指すこと。**
**intake 層**（`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`）の
`source_quality_flags` は 3 行に立っている（下記の各行に記載）。
**store 層**（`inventory.json` の `flags` / `shells.json` の `flags`）は **4 行・4 shell とも `[]`**
——**intake 層で立ったフラグが store 層に伝播していない。** → §Canonical Conflict `C-6` ②

#### 行 1 — `source_line_no 702` ／ **`FRANCE | WHITE > BORDEAUX`** ／ 2019 ／ **$520**
`original_raw_line`: `2019\t\tSaint-Estèphe\t\t\t\t\t\t\t\t520` ／ release shell `rs:rel:766c6231144b8d0c`（単独）
🔴 **intake 層 `source_quality_flags` = `['section_colour_conflict']`**

🔴 **AOC Saint-Estèphe の白は法的に存在しない**（🏛 CDC）。**したがってこの行は AOC Saint-Estèphe ではない。**
✅ **2019 の白として公式に実在するのは 2 つ**: `Cos d'Estournel Blanc 2019`（SB 65 / Sém 35）と
`Pagodes de Cos Blanc 2019`（SB 88 / Sém 12）。
🔴 **どちらであるかは公式資料からは決定できない。** メニューはキュヴェ名を印字せず、
生産者見出しは両者で同一（`Cos d'Estournel`）だからである。
⚠️ ✅ **公式ショップは `Cos d'Estournel Blanc 2019` を現に商品として持っている**（product id `105260`、
在庫あり、`/fr/produit/cos-destournel-blanc-2019/`）——**存在の証明にはなるが、この行の同定にはならない。**
→ 実ラベル確認タスク 1

#### 行 2 — `source_line_no 703` ／ **`FRANCE | WHITE > BORDEAUX`** ／ 2018 ／ **$680**
`original_raw_line`: `2018\t\tSaint-Estèphe\t\t\t\t\t\t\t\t680`
🔴 **intake 層 `source_quality_flags` = `['cross_section_duplicate', 'section_colour_conflict']`**

🔴 同上。**2018 は `Cos d'Estournel Blanc 2018`（SB 67 / Sém 33、公式ショップ product id `81136`、
現在は `outofstock`）と `Pagodes de Cos Blanc 2018`（SB 93 / Sém 7、＝Pagodes 白の *初* ヴィンテージ）の
両方が実在する。**
→ 実ラベル確認タスク 2

#### 行 3 — `source_line_no 1014` ／ `FRANCE | RED > BORDEAUX` ／ 2018 ／ **$900**
`original_raw_line`: `2018\t\tSaint-Estèphe\t\t\t\t\t\t\t\t900`
🔴 **intake 層 `source_quality_flags` = `['cross_section_duplicate']`**

✅ **AOC Saint-Estèphe の赤として整合。** 公式の 2018 赤は
`Cos d'Estournel 2018`（CS 74 / Me 23 / CF 2 / PV 1）と `Pagodes de Cos 2018`（CS 54 / Me 37 / CF 6 / PV 3）。
⚠️ **どちらかは決定できない**（メニューはセカンドの名を一度も印字していない）。
→ 実ラベル確認タスク 3

🔴 **行 2 と行 3 は「重複」ではない。** 🏛 の色制約により **行 2 は AOC Saint-Estèphe ではありえず、
行 3 はありうる。したがって両者は必ず別のワインである。** 価格差（$680 / $900）はこれと矛盾しない。
🔴 **しかし intake はこの 2 行を 1 つの release shell `rs:rel:1354e538b20bd449` に畳んでいる。** → §Canonical Conflict `C-6` ②

#### 行 4 — `source_line_no 1015` ／ `FRANCE | RED > BORDEAUX` ／ 2015 ／ **$800**
`original_raw_line`: `2015\t\tSaint-Estèphe\t\t\t\t\t\t\t\t800` ／ release shell `rs:rel:63efc4f18ef1d3c5`（単独）
**intake 層 `source_quality_flags` = `[]`**（この行だけフラグなし）

✅ 公式の 2015 赤は `Cos d'Estournel 2015`（CS 75 / Me 23,5 / CF 1,5）と
`Pagodes de Cos 2015`（CS 44 / Me 46,2 / CF 5,8 / PV 4）。⚠️ 決定不能。
→ 実ラベル確認タスク 4

🔍 **メニュー全体の走査結果**（store 層 `research/out/t-01/inventory.json` = 全 768 行・うち WINE 677 行）:
**`Pagodes` / `Goulée` / `Labory` の文字列は 1 度も現れない。**
→ **「セカンドなら名前が出ているはずだから、これはグラン・ヴァンだ」という消去法は使えない。**

### ⚠️ 行数は成果物によって異なる —— intake↔store 乖離の 5 例目

🔴 **どの数字がどの成果物のものかを必ず名指すこと。両者は別の成果物であり、比較してはならない。**

| 層 | 成果物 | 行数 |
|---|---|---|
| **intake 層** | `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` | 🔴 **704 行**（＝**検証済みの intake 行数**。OBP 本数の分母はこちら） |
| **store 層** | `research/out/t-01/inventory.json` | **768 行**（うち `menu = WINE` は **677 行**） |

⚠️ **この食い違いは本件で新たに見つかったものではない。**
**Batch 8–9 で Bachelet-Monnot・Clos de Tart・Armand Heitz・Hundred Acre の 4 例が記録済みの
既知の intake↔store 乖離であり、本件はその 5 例目にあたる。**
→ **704 を「訂正」してはならない。704 は intake 層の正しい値である。**
**本ドシエの生産者側の走査結果（`Pagodes`/`Goulée`/`Labory` が 0 件）は store 層で取ったものであり、
上記乖離の影響を受けうる。** → Open Questions 15

---

## Staff Notes

### 🔴 芯 3 点（これだけ言えば、嘘をつかずに接客できる）

**① 「Cos は 1855 年格付の 2 級。サン=テステフの入口の丘に建ち、パゴダの屋根で知られます。
創設者 Louis Gaspard d'Estournel は 1791 年に Cos と Pomys を受け継ぎ、畑を 14 ha から 45 ha に広げました。
現在の畑は 100 ha、樹齢は平均 45 年、グラン・ヴァンに使う樹は平均 55 年。2000 年から Michel Reybier の
所有です。」**
→ 全て ✅ 公式。**「東インド会社で財を成した」は言わない**（公式に無い）。

**② 「Cos は白も造っています。`Cos d'Estournel Blanc` は 2005 年が初ヴィンテージ、
ソーヴィニヨン・ブランとセミヨン。2018 年からは `Pagodes de Cos Blanc` も加わりました。
ただしサン=テステフの AOC は法律上 *赤だけ* なので、白はサン=テステフを名乗れません。」**
→ ✅ + 🏛。**これがこのテーブルで最も価値のある一文である。**
**白のアペラシオン名が何かは、ラベルを見て答えてください（後述）。**

**③ 「グラン・ヴァンのブレンドは毎年変わります。2015 はカベルネ 75%、2018 は 74%、2019 は 65%。
『Cos はメルロが多い』という一般論は年によって当たりません。」**
→ ✅ 公式の年次数値。**canonical の固定比率をそのまま口にしないための予防線。**

---

### ⚠️ 言ってはいけないこと（must-not-say）

🔴 **本ドシエは公式資料が豊富な部類だが、canonical 側の誤りが多いため、このリストは長い。**

1. 🔴 **「オーガニック（ビオ）です」と言ってはならない。**
   Ecocert への `dateEngagement` は **2021-08-16**、`etatCertification` は **`ENGAGEE`（転換関与中、認証済ではない）**。
   **OBP の 4 本（2015 / 2018 / 2018 / 2019）はすべてこれより前。**
2. 🔴 **同時に「オーガニックではありません」とも言ってはならない。** 上と同じ理由。
   聞かれたら「**2021 年から Ecocert のもとで有機への転換に入っています。お出ししているヴィンテージは
   それ以前のものです**」——これだけが言える。
3. 🔴 **「白もサン=テステフです」は絶対に言ってはならない。** 🏛 CDC が赤のみと定める。
   **メニューの印字がそうなっていても、である。**
4. 🔴 **「白のアペラシオンは Bordeaux Blanc です」も言ってはならない。**
   **公式は白のアペラシオンを一度も書いていない。**「サン=テステフではありえない」までが確定事項。
5. 🔴 **「ブレンドは CS 65 / Merlot 34 / PV 1 です」と言ってはならない**（canonical の値）。
   **公式の年次値と 3 ヴィンテージすべてで一致しない。**
6. 🔴 **「畑は 91 ha」「64 ha」と言ってはならない**（canonical の 2 レコードの値）。**公式は 100 ha。**
7. 🔴 **「オーナーは Domaines Prats、Bruno Prats が経営」と言ってはならない。**
   **2000 年から Michel Reybier / DOMAINES REYBIER。**
   （⚠️ ただし Agence Bio の登録簿は今も `denominationcourante: DOMAINES PRATS` を保持している。
   canonical のこの文字列は *捏造ではなく古い実在値* である。）
8. 🔴 **「グラン・ヴァンは新樽 100%」「新樽 60〜100%」と言ってはならない。**
   **公式サイトのどこにも新樽比率は書かれていない。** canonical の 2 レコードは互いに矛盾している。
9. 🔴 **「熟成 22〜24 ヶ月」「MLF は 1997 年以降 100% 小樽」「1989 年以降 2 度目の濾過を廃止」
   「年産 30 万本」「植密度 9,000 本/ha」を言ってはならない。** すべて公式に出典が無い。
10. 🔴 **「1982 年以降は第一級相当（パーカー）」を店の説明として言ってはならない。**
    これは canonical に入っている**第三者批評家の評点であって生産者の言葉ではない**。
11. 🔴 **「1853 年にエルランジェ銀行に売却された」を断定してはならない。**
    公式は「債務のため一度売却し、買い戻した」とだけ書き、相手先を書いていない。
12. 🔴 **「セカンドの Pagodes de Cos は 1994 年から」を断定してはならない。**
    **公式の掲載は 2000 年から。**
13. 🔴 **「ザンジバルのスルタンの扉」と言い切ってはならない。**
    公式が書くのは「**la porte de Zanzibar（ザンジバルの扉）**」まで。**「スルタンの」は公式に無い。**
14. 🔴 **`Goulée by Cos d'Estournel` を「サン=テステフのワイン」と言ってはならない。**
    ✅ 公式は「**メドック最北**」と書く。**別のアペラシオンである。**
15. 🔴 **`Château Cos Labory` を「うちのラインナップ」と言ってはならず、
    同時に「まったく別の会社」とも言ってはならない。** ✅ 公式が「Michel Reybier の最新の買収」と告知し、
    🏛 2025-01-01 から DOMAINES REYBIER の事業所になっている。**別のシャトー・同じ経営者。**
16. ⚠️ **「サン=テステフには格付シャトーが 5 つ」を公式情報として言ってはならない。**
    本調査では公式・法定資料でこの数字を確認していない。
17. ⚠️ **`Gris de Cos` を現行商品として案内してはならない。** 公式レンジに存在しない。
18. 🔴 **どのヴィンテージについても「グラン・ヴァンです」と断定してはならない。**
    **メニューはキュヴェ名を印字していない。4 行すべてがセカンドでありうる。**
    実ラベルを見るまでは「**サン=テステフのコス・デストゥルネルのワイン**」までが言える範囲。

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

**canonical export `migration/out/export/db_wine_canonical.json`（928 件）は読み取り専用として扱った。
1 バイトも書き換えていない。`research/canonical_conflicts/REGISTER.md` も開いていない。**

**検証したレコード: 3 件**（`cos-destournel-1855` / `cos-destournel-parker-profile` / `cos-labory-1855`）
**＋ 走査で触れた 8 件**（prose-only 7 件 + `saint-estephe-appellation-parker`）。
**検証した個別主張: 33 件。うち公式・法定資料に照らして失敗: 21 件（63.6%）。**
内訳 —— **contradicted 10 件 / unsourced 9 件 / absent as key 2 件**。
🔴 **「14 生産者中 13 件で canonical の格納値が公式と矛盾した」という standing base rate を、
本件も *追認する* 側に立つ。**

---

### ① `C-6` に証拠を追加 —— **欠陥はメニューの「色」ではなく「アペラシオン列」にある**

| | |
|---|---|
| **対象** | OBP 行 1（line 702, WHITE, 2019, $520）／行 2（line 703, WHITE, 2018, $680） |
| **canonical 側** | `cos-destournel-1855` / `cos-destournel-parker-profile` **ともに `color: "Rouge"` 単一**。<br>🔴 **canonical はこの生産者が白を造ることを、typed な `color` フィールドの水準では知らない**（`obp_note` の散文中にだけ「Cos Blanc」の 5 文字がある） |
| **一次証拠** | 🏛 CDC:「L'AOC « Saint-Estèphe » est réservée aux vins tranquilles rouges」／認可品種 6 種すべて黒<br>✅ `Cos d'Estournel Blanc` 2018・2019 実在（公式ページ＋公式ショップ product `81136` / `105260`）<br>✅ `Pagodes de Cos Blanc` 2018・2019 実在 |
| 🔴 **どちら側の欠陥か** | 🔴 **メニューの *色セクション* は正しい。誤っているのはメニューの *ワイン名列* に印字された `Saint-Estèphe` である。**<br>**Batch 10・11 が示した「メニューが正しい場合もある」の第 5 例だが、より細かい形をしている ——<br>同じ 1 行のなかで、一方の列は正しく、他方の列が誤っている。** |
| **OBP 影響** | **2 本**（行 1・行 2）。両行とも `unresolved` のまま |
| **推奨（未実行）** | canonical に `color` 軸を持つ製品同一性を導入し、`Cos d'Estournel Blanc` / `Pagodes de Cos Blanc` を独立レコードとして起こす。**メニューの `Saint-Estèphe` 印字は白 2 行については採用しない。** |
| **確信度** | **High**（法定文＋公式の 2 面から独立に裏付け） |

---

### ② `C-6` の**前提分割**に対する実測 —— **欠陥は release 識別キーに色が無いこと**

🔍 **`research/out/t-01/duplicates.json`（141 件）の全数走査:**

| 区分 | 件数 |
|---|---|
| 2 つ以上の section にまたがって 1 shell に集約された shell | **34** |
| うち section 第 2 トークンが割れるもの（色＋日本酒の分類軸＋Champagne のスタイル軸を含む） | **33** |
| 🔴 うち **`RED` / `WHITE` を厳密にまたぐもの** | 🔴 **20**（残り 13 件は `NAMA \| RESERVE` 等の**酒質分類**と `CHAMPAGNE \| BLANC DE BLANCS/ROSÉ/BLENDS` の**スタイル軸**であり、色軸ではない。**「色跨ぎ」を section 文字列だけで数えると 33 と過大に出る**） |
| うち `producer` レベル | **11**（🟢 **正しい挙動**。1 生産者が両色を造るのは当然） |
| うち `product` レベル | 🔴 **5**（欠陥。うち Bordeaux は `rs:pro:29cab5c232001817` ＝本件のみ） |
| うち **`release` レベル** | 🔴 **4 件のみ**: `rs:rel:a1e9d1d17d351bdf`（Burgundy）／**`rs:rel:1354e538b20bd449`（Bordeaux＝本件）**／`rs:rel:553ebd516975cafc`・`rs:rel:39cbe0a8e191c75d`（Rhône） |

🔴 **本件 `rs:rel:1354e538b20bd449` の中身:**
- `source_lines` = line 703（**WHITE**, $680）+ line 1014（**RED**, $900）
- `source_transcription`（代表値）= **WHITE 側のみ**。`ignored_trailing_numeric = "680"`
- 🔴 **`$900` という価格は release shell からは消えている。**
- `duplicates.json` の `reason` = 「printed identity（と必要なら section）が一致したため 1 shell に集約」
  —— 🔴 **色を区別しない同一の理由文が、正しい 11 件（producer レベル）と
  誤った 9 件（product 5 + release 4）の *両方* に付いている。**

🔴 **したがって `C-6` の前提は「canonical 構造 vs matcher 入力」の 2 分割では足りない。**
**少なくとも 3 つ目 ——「release 識別キーが `(producer, classification_text, vintage)` で、
色を含まない」という *キー設計* の欠陥 —— が独立に存在する。**
**producer レベルの色跨ぎを欠陥として数えると 11 件の偽陽性が出る。
さらに section 文字列の第 2 トークンだけで機械的に数えると、日本酒の酒質分類と Champagne のスタイル軸
13 件を色跨ぎと誤認する（33 vs 20）。**

### 🔴 これは **検知の失敗ではなく、層をまたぐ伝播の喪失（propagation loss）** である

🔴 **intake 層はこの衝突を正しく検知している。**
🔍 実測（`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`、**全 704 行**）——
**フラグは `source_quality_flags` フィールドに載っている**（`_parts.flags` ではない。そちらは全行 `[]`）:

| OBP 行 | `source_quality_flags`（intake 層） |
|---|---|
| **WHITE 2019 $520** | 🔴 **`['section_colour_conflict']`** |
| **WHITE 2018 $680** | 🔴 **`['cross_section_duplicate', 'section_colour_conflict']`** |
| **RED 2018 $900** | **`['cross_section_duplicate']`** |
| RED 2015 $800 | `[]` |

🔴 **そして `section_colour_conflict` は 704 行中わずか 3 回しか立たない。うち 2 回が本件である。**
🔍 corpus 全体の語彙と頻度（intake 層、704 行）:
`missing_price` 28 ／ `producer_spelling` 13 ／ `cross_section_duplicate` 8 ／ `cuvee_spelling` 7 ／
`canonical_model_note` 6 ／ `format_in_name` 6 ／ `disgorgement_in_name` 4 ／
🔴 **`section_colour_conflict` 3** ／ `section_region_conflict` 2 ／ `malformed_vintage` 2 ／
`disgorgement_unknown` 1。
→ **Cos d'Estournel は、メニュー全体でも最も稀な欠陥型の 3 分の 2 を単独で占めている。**

🔴 **失われるのは、その先である。**

| 層 | 成果物 | 色の衝突は残っているか |
|---|---|---|
| **intake 層** | `obp_intake_normalized_20260804.json` | 🟢 **残っている**（`source_quality_flags` に 3 行分） |
| **store 層** | `research/store/t-01/shells.json` | 🔴 **消えている**（shell 4 件すべて `flags: []`） |
| **store 層** | `research/out/t-01/inventory.json` | 🔴 **消えている**（4 行すべて `flags: []`） |
| **store 層** | `research/out/t-01/mapping.json` | 🔴 **色の軸自体が出力スキーマに存在しない** |

🔴 **したがって `C-6` の前提分割は「canonical 構造 vs matcher 入力」の 2 分割では足りず、
「検知はできているのに次の層へ渡らない」という第 3 の形を持つ。**
**具体的には —— store 層の release 識別キーが `(producer, classification_text, vintage)` であり
色トークンを含まないため、intake 層が `section_colour_conflict` を立てた *まさにその 2 行* が、
store 層で 1 つの release shell `rs:rel:1354e538b20bd449` に畳まれ、$900 が捨てられる。**

⚠️ **本書の初稿はこれを「パイプラインが検知していない」と誤って記述していた。
原因は store 層の `inventory.json` の `flags` フィールドだけを見て、
intake 層の `source_quality_flags` を見ていなかったことにある。
—— 層を名指さずに「フラグが無い」と書いてはならない、という教訓そのものである。**

| | |
|---|---|
| **OBP 影響** | **2 本が 1 本に潰れている**（行 2・行 3）。**うち $900 の価格情報が失われる** |
| **推奨（未実行）** | ① store 層の release 識別キーに `section_path` の色トークンを含める<br>② **intake 層の `source_quality_flags` を store 層の `shells.json` / `inventory.json` に伝播させる**（現在は落ちている）<br>③ `duplicates.json` の `reason` をレベル別に分ける |
| **確信度** | **High**（intake 層・store 層の両成果物からの機械的導出。両者を突き合わせて確認済） |

---

### ③ `cos-destournel-1855` の逐条検証 —— **19 主張中 11 件が失敗**

| # | canonical の格納値 | 公式・法定側 | 判定 |
|---|---|---|---|
| 1 | `producer` = `Château Cos d'Estournel`（**U+0027**） | ✅ 公式本文は **U+2019 が優勢**（284 : 174）かつ **`Château` 無しが 444 : 14**<br>🏛 登録簿住所は **`COS D ESTOURNEL`（アポストロフィ無し）**<br>🔍 OBP は **`Cos d’Estournel`（U+2019）** | 🔴 **`S-2` / `C-1`。canonical と OBP でコードポイントが異なる**（U+0027 vs U+2019）＝素朴な文字列一致は必ず外れる |
| 2 | `vintage` = `—`（U+2014） | — | 🔴 **ボトルではない。328 件の同型が canonical 全体に存在** |
| 3 | `subregion` = `Saint-Estèphe` | ✅🏛 一致 | 🟢 PASS |
| 4 | `classification` = `1855 Médoc Classification · 2ème Grand Cru Classé` | ✅「the 1855 Bordeaux Classification officially recognized Cos d'Estournel as a **Second Growth Estate**」／「**Deuxième Grand Cru du Médoc**」 | 🟢 PASS（実質） |
| 5 | `color` = `Rouge` のみ | ✅ 白 2 種・ロゼの言及あり | 🔴 **absent as key**（§① 参照） |
| 6 | **91 ha** | ✅ **「Today the vineyard occupies 100 hectares」** | 🔴 **contradicted（typed 相当）** |
| 7 | **20 種類の土壌タイプ** | ✅ 2001 年の調査が「**nearly twenty variants**」を明らかにした | ⚠️ 近いが**文言が違う**（「20 種類の土壌」ではなく「20 に近い変異」）。数値の断定は不可 |
| 8 | **CS 65% / Merlot 34% / PV 1%** を固定値として格納 | ✅ **2015 = 75/23,5/CF1,5**・**2018 = 74/23/CF2/PV1**・**2019 = 65/35** | 🔴 **contradicted。OBP の 3 赤ヴィンテージのいずれとも一致しない。しかも比率は毎年変わる** |
| 9 | **グラン・ヴァンに新樽 100%** | ✅ 公式に記載なし | 🔴 **unsourced** |
| 10 | **熟成 約 22〜24 ヶ月** | ✅ 公式に記載なし | 🔴 **unsourced** |
| 11 | **19 世紀初頭に創設** | ✅ **「inherited Cos and Pomys in 1791」** | 🔴 **contradicted** |
| 12 | **東インド会社の貿易で財を成した** | ✅ 「新市場の追求がアジアへ向かわせた」「1838 年からインド駐留の英国士官が飲み始めた」。**"East India Company" は公式に一度も出ない** | 🔴 **unsourced** |
| 13 | **1853 年エルランジェ銀行に売却** | ✅ 「債務返済のため売却し、後に買い戻した」（相手先の記載なし） | 🔴 **unsourced** |
| 14 | **2000 年 Michel Reybier 取得** | ✅ 「Owner of Cos d'Estournel since 2000」 | 🟢 PASS |
| 15 | **ザンジバルのスルタンの扉** | ✅ 公式は「**la porte de Zanzibar**」とだけ書く | ⚠️ **部分的に裏付け。「スルタンの」は unsourced** |
| 16 | **Pagodes de Cos（セカンド、1994 年〜、新樽 45〜50%）** | ✅ 公式の掲載は **2000 年から**。新樽比率の記載なし | 🔴 **contradicted（1994）＋ unsourced（45〜50%）** |
| 17 | **Gris de Cos（グリ、ロゼ）** | ✅ 現行レンジに存在しない | 🔴 **unsourced** |
| 18 | **Cos Blanc（白、SB/Sém、2005 年〜）** | ✅ **ワインは実在し 2005 年も正しいが、公式名は `Cos d'Estournel Blanc`** | ⚠️ **名称形の誤り。中身は正しい** |
| 19 | ラインナップに **`Pagodes de Cos Blanc` と `G d'Estournel` が無い** | ✅ 両方が公式の現行レンジ | 🔴 **absent as key** |

**→ 19 主張中: PASS 3 / contradicted 5 / unsourced 6 / absent as key 2 / 部分裏付け・要注意 3。**

---

### ④ `cos-destournel-parker-profile` —— **unnumbered shape。しかも 1 件ではなく 37 件**

**このレコードの全フィールドを以下に転記する（要求どおり）。**

```
id                 = cos-destournel-parker-profile
producer           = Château Cos d'Estournel
name               = Cos d'Estournel — Parker's Château Profile
vintage            = —                       (U+2014)
country            = France
region             = Bordeaux
subregion          = Saint-Estèphe
type               = Wine                    ← 🔴 参考書の項目が「ワイン」型を名乗る
color              = Rouge
classification     = Château Profile — Parker's Bordeaux · 2ème Grand Cru Classé 1855
drinking_window    = 8〜30年（ヴィンテージによる）
food_pairings      = [Lamb · 仔羊, Beef Rib · 牛リブ, Truffle · トリュフ, Duck Confit · 鴨のコンフィ]
glassware          = Bordeaux
indicator          = #8b1a1a
obp_format         = By the bottle           ← 🔴 「ボトルで販売」を名乗る
serving_temp       = 17–19°C
tags               = [Château Profile, Cos d'Estournel, Saint-Estèphe, 2ème Cru Classé,
                      Parker, Reference, Super Second]
description        / description_en          … パーカーの評価を要約した散文
tasting            / tasting_en              … 同上（生産者の言葉ではない）
obp_note           / obp_note_en             … 下表の数値群を HTML で保持
```

**`obp_note` が保持する数値の逐条検証（14 主張中 10 件が失敗）:**

| canonical | 公式・法定側 | 判定 |
|---|---|---|
| **所有：Domaines Prats S.A.（経営 Bruno Prats・補佐 Jean-Guillaume Prats）** | 🏛 現在は **DOMAINES REYBIER SA**（SIREN 331321109）／✅ 2000 年から Reybier<br>🔴 **ただし Agence Bio は同一 SIREN に対し `denominationcourante: "DOMAINES PRATS"` を今も保持している** | 🔴 **contradicted（現在形として）／ 実在した旧商号（歴史値として）。捏造ではない** |
| **面積 64 ha** | ✅ **100 ha** | 🔴 contradicted |
| **平均樹齢 35 年** | ✅ **畑全体 45 年 / グラン・ヴァン 55 年** | 🔴 contradicted |
| **植密度 9,000 本/ha** | ✅ 記載なし | 🔴 unsourced |
| **CS 60% / Merlot 40%** | ✅ 年次値と全て不一致。🔴 **かつ `cos-destournel-1855` の CS65/Me34/PV1 とも矛盾** | 🔴 **contradicted ＋ canonical 内部矛盾** |
| **年産 グラン・ヴァン 30 万本 / セカンド 10 万本** | ✅ 記載なし | 🔴 unsourced |
| **3 週間醸造** | ✅ 記載なし | 🔴 unsourced |
| **1997 年以降 MLF を 100% 小樽で** | ✅ 記載なし | 🔴 unsourced |
| **新樽 60〜100%** | ✅ 記載なし。🔴 **`cos-destournel-1855` の「100%」と矛盾** | 🔴 **unsourced ＋ 内部矛盾** |
| **1989 年以降 2 度目の濾過を省略** | ✅ 記載なし | 🔴 unsourced |
| **1982 年以降は第一級相当（Parker）** | — | 🔴 **第三者批評家の評点が canonical の属性として格納されている** |
| **難ヴィンテージ成功例 1991 / 1992 / 1993** | ✅ 公式のヴィンテージ一覧に **1992・1993 は存在しない**（1991 はある） | 🔴 **contradicted** |
| **「Cos」の s は発音する [kos]** | ✅ 公式は語源（古ガスコーニュ語「小石の丘」）は書くが**発音は書かない** | 🔴 unsourced |
| subregion / classification / パゴダ / ラフィットを見下ろす立地 | ✅ 整合 | 🟢 PASS |

#### 🔴 shape の記述（**unnumbered — CTO's call**）

**canonical レコードの *provenance* が、生産者でも公的登録簿でもなく「第三者批評家の参考書」であるもの。**

🔍 **これは 1 件の異常値ではない。928 件中 37 件（4.0%）が同じ provenance を持つ。**

| sub-shape | 件数 | 例 | `producer` フィールドの中身 | `vintage` |
|---|---|---|---|---|
| `Vintage Reference — Parker's Bordeaux` | 🔴 **34** | `bordeaux-vintage-1970-guide` | 🔴 **`"Bordeaux"`（＝地方名。生産者ではない）** | 🔴 **`1970` 等、実在する年号** |
| `Château Profile — Parker's Bordeaux` | **2** | `cos-destournel-parker-profile`, `calon-segur-parker-profile` | シャトー名 | `—` |
| `Appellation Reference — Parker's Bordeaux` | **1** | `saint-estephe-appellation-parker` | 🔴 **`"Saint-Estèphe"`（＝アペラシオン名）** | `—` |

🔴 **危険性の核心 ——「参考書」と「売り物のボトル」がスキーマ上まったく区別できない。**
`bordeaux-vintage-1970-guide` は `type: "Wine"` / `color: "Rouge"` / `obp_format: "By the bottle"` /
`glassware: "Bordeaux"` / `serving_temp` / `drinking_window` / `food_pairings` を**完備している**。
🔴 **`vintage: "—"` センチネルすら持たない 34 件は、`(producer, vintage)` を鍵にする matcher に対して
「Bordeaux の 1970 年赤」として *正当に見える*。**
🔴 **さらに `producer` フィールドが地方名・アペラシオン名を保持する例が 35 件ある**
（`Bordeaux` 34 / `Saint-Estèphe` 1）——**`producer` は「生産者」を意味しない場合がある。**

**関連**: Batch 11 の `allemand-chaillot-nv`「template-derived」／ Batch 9 の attribute-provenance。
**これらはいずれも「値が誰の発言か」を記録する場所が canonical に無いことの別々の症状である。**

| | |
|---|---|
| **OBP 影響（本件分）** | 🔴 **4 本すべて。** `cos-destournel-parker-profile` は `producer` フィールドが
`cos-destournel-1855` と**バイト同一**であるため、生産者名で当てにいく matcher に対して**両者が等しく当たる**。<br>🔍 現に intake は 4 行すべてを producer レベルで止め、**cuvée / vintage レベルには 1 件も解決していない** |
| **推奨（未実行）** | canonical に `provenance` / `record_kind`（`bottle` / `reference` / `profile`）を導入し、
`reference` 系 37 件を製品名前空間から分離する。**分離するまでは 37 件を matcher の候補から除外する。** |
| **確信度** | **High**（レコード実体からの機械的導出。判断を要しない） |

---

### ⑤ `cos-labory-1855` —— 所有情報が stale（**近似名の罠の副産物**）

| | |
|---|---|
| **対象** | `cos-labory-1855`（`Château Cos Labory` / `1855 Médoc Classification · 5ème Grand Cru Classé`） |
| **canonical の主張** | 「1959 年：娘と娘婿のフランソワ・オードワ氏に引き継ぎ、**オードワ家が現在まで所有**」<br>「2000 年：長男ベルナール・オードワがシャトー運営を担当」 |
| **一次証拠** | ✅ `estournel.com`:「**Château Cos Labory, dernière acquisition de Michel Reybier au cœur de l'appellation Saint-Estèphe**」<br>🏛 `SOCIETE CIVILE D'EXPLOITATION DES DOMAINES REYBIER`（SIREN 334353885, 住所 `CHATEAU COS LABORY`）**état `C`、2024-12-31 閉鎖**<br>🏛 `DOMAINES REYBIER` の établissement **`33132110900042`（住所 `CHATEAU COS LABORY`、NAF `01.21Z`、état `A`）**<br>🏛 `DOMAINES REYBIER` siège の `date_debut_activite` = **`2025-01-01`** |
| **判定** | 🔴 **contradicted（stale）。** 「現在まで所有」は成立しない |
| **OBP 影響** | **0 本**（🔍 メニューに `Labory` の印字は 1 度も無い）。**ただし本件の生産者の識別に直接影響する** ——<br>🔴 **`Cos` トークンで生産者を寄せる処理は、2025 年以降「同じ経営者の 2 つのシャトー」を扱わねばならない** |
| **推奨（未実行）** | `cos-labory-1855` の所有記述を更新し、`cos-destournel-*` との**運営主体の同一性**を関係として持つ |
| **確信度** | **Medium-High**（公式の告知＋登録簿の 3 点で一致。ただし買収の *日付* を明示する法定文書は未取得） |

---

### ⑥ `S-2` / `C-1` —— アポストロフィと `Château` 前置

🔍 **同一実体に対して、システム内に 5 つの異なる書式が同時に存在する:**

| 出所 | 文字列 | アポストロフィ |
|---|---|---|
| 🏛 INSEE 登録簿（住所） | `COS D ESTOURNEL` | **無し** |
| 🏛 登録法人名 | `DOMAINES REYBIER` | — |
| ✅ 公式サイト本文（優勢） | `Cos d’Estournel` | **U+2019** |
| ✅ 公式サイト（同一ナビ内の別項目） | `Cos d'Estournel Blanc` | **U+0027** |
| ✅ 公式フッター / *mentions légales* | `Château Cos d’Estournel` | U+2019 |
| 🔍 OBP メニュー | `Cos d’Estournel` | **U+2019** |
| 🔍 canonical（2 件とも） | `Château Cos d'Estournel` | **U+0027** |

🔴 **canonical と OBP はアポストロフィのコードポイントが異なり、かつ canonical だけが `Château` を前置している。**
🔴 **Batch 11 の教訓（`La Forest` を一括正規化すると別の畑に着地する）に照らすと、
本件は「一括正規化してよい側」に見えるが、そう見えること自体が罠である ——
🏛 登録簿はアポストロフィを *持たない* 書式を採り、公式サイトは *両方* を使っている。
「正しい 1 つ」は存在しない。**
→ **推奨（未実行）: 正規化ではなく、`display_name` / `legal_name` / `match_keys[]` の 3 層に分離する。**

---

## Sources

### ✅ 採用した公式ドメイン

| URL | レイヤー | 内容 |
|---|---|---|
| `https://www.estournel.com/` | ✅ | 公式サイト（FR / EN / CN） |
| `https://www.estournel.com/fr/mentions-legales/` ／ `/en/terms-conditions/` | ✅ | **§2a の認証根拠。DOMAINES REYBIER / SA / capital 121 000 € / RCS Bordeaux n° 331 321 109 / siège Château Cos d'Estournel 33180 Saint-Estèphe / représentant légal Aude AUGENBLICK** |
| `https://www.estournel.com/robots.txt` | ✅ | `Sitemap: /fr/sitemap_aio.xml` を明示 |
| `https://www.estournel.com/fr/sitemap_aio.xml` → `post-` / `page-` / `hub-sitemap_aio.xml` | ✅ | **351 URL 全数** |
| `/en/cos/wines-cos-destournel/` | ✅ | グラン・ヴァン。1928–2025 のヴィンテージ別ブレンド |
| `/en/cos/wines-cos-destournel-blanc/` | ✅ | **白。2005–2025。初ヴィンテージ 2005 の明記** |
| `/en/cos/wines-pagodes-de-cos/` | ✅ | 「Other Grand Vin」。2000–2025 |
| `/en/cos/wines-pagodes-de-cos-blanc/` | ✅ | **2018–2025。「the first vintage」の明記** |
| `/en/cos/wines-gdestournel/` | ✅ | 2019–2025。メドック北部 |
| `/en/cos/wines-goulee-by-cos-destournel/` | ✅ | 2005–2018。「northernmost reaches of the Médoc」 |
| `/en/cos/terroir-remarkable-vineyard/` | ✅ | **100 ha / 樹齢 45 年 / グラン・ヴァン 55 年 / マッサル・セレクション** |
| `/en/cos/terroir-diversity/` | ✅ | 土壌構成 / 2001 年の調査 /「nearly twenty variants」/ 語源 |
| `/en/cos/commitment-louis-gaspard-destournel/` | ✅ | **1791 年相続 / 14→45 ha / 1838 年インド / 1855 年格付の 2 年前に死去** |
| `/en/cos/commitment-michel-reybier/` | ✅ | **2000 年取得 / Domaines Reybier の 5 つの畑 / Dominique Arangoïts** |
| `https://www.estournel.com/wp-json/wp/v2/product?per_page=100` | ✅ | **公式 WooCommerce。`Cos d'Estournel Blanc 2018`（id 81136）・`2019`（id 105260）の実在証明**／`Château Cos Labory, dernière acquisition de Michel Reybier` |
| `https://www.estournel.com/wp-content/uploads/2024/09/Cos-dEstournel-Blanc-neutre-0.75l.png` | ✅ | 公式ボトルショット（246×380px）。**ラベルに `COS D'ESTOURNEL` は読めるが、アペラシオン行は解像度不足で読めない** |
| `https://www.estournel.com/wp-content/uploads/2024/10/PDF-COS-DESTOURNEL-2010-EN.pdf` | ✅ | 公式 PDF（2010 年 14 周年リリース資料）。**アペラシオン記載なし** |

### 🏛 公的登録簿・法定文書

| URL | 内容 |
|---|---|
| `https://recherche-entreprises.api.gouv.fr/search?q=ESTOURNEL&code_postal=33180` | SIREN/SIRET/NAF/dirigeants/établissements |
| `https://recherche-entreprises.api.gouv.fr/search?q=COS&code_postal=33180` | Cos Labory / Goulée / 同住所の非ワイン法人の切り分け |
| `https://opendata.agencebio.org/api/gouv/operateurs/?siret=33132110900018` | 🔴 **exact-SIRET 照会。numeroBio 32168 / Ecocert FR-BIO-01 / ENGAGEE / 2021-08-16 / mixité Oui** |
| `https://extranet.inao.gouv.fr/fichier/PNOCDCSaint-Estephe.pdf` | 🔴 **AOC Saint-Estèphe CDC。`%PDF` 実体検証済（131,753 bytes）。「réservée aux vins tranquilles rouges」／décret du 14 novembre 1936 ／認可品種 6 種すべて黒**<br>⚠️ **PNO（2010 年異議申立手続）文書であり consolidated 版ではない（§2c）** |

### ❌ §2a により **却下**したドメイン / 到達できなかった資料

| ドメイン・URL | 却下・失敗の理由 |
|---|---|
| `cos-estournel.com` | **DNS 解決せず**（`curl` exit 000）。存在しない |
| `chateau-cos-destournel.com` | **DNS 解決せず**。存在しない |
| `cosdestournel.com` | **DNS 解決せず**。存在しない |
| `crus-classes.com` / `www.crus-classes.com` | **DNS 解決せず。**1855 年格付の公式団体サイトとして探したが到達不能。**1855 年格付の *法定原文* は本調査では取得できていない**（公式サイトの自己記述で代替した） |
| `https://www.inao.gouv.fr/produit/saint-estephe-16807` | 🔴 **`HTTP 403`（WAF）。gated — not evidence of absence** |
| `https://www.inao.gouv.fr/fichier/PNOCDCSaint-Estephe.pdf` ほか 3 綴り | **`HTTP 404` かつ本文が `<!DOCTYPE` — §2c のファイル名の罠を実際に踏んだ。`extranet.` サブドメインが正解だった** |
| `https://ec.europa.eu/agriculture/eambrosia/...` | JS レンダリング。API エンドポイントが `404`。**eAmbrosia からの裏取りは未達** |
| `https://www.estournel.com/en/shop/` | `HTTP 404`（ショップは `/fr/produit/` 配下。REST API で代替） |
| **Wikipedia / Wine-Searcher / Vivino / Decanter / Wine Advocate / Vinous / Millesima / Hachette / societe.com / verif.com / vin-vigne.com / lacaveduchateau.com / delicieuxsecret.com / vinatis.com / vinotheque-bordeaux.com / vins-fins.com / saint-estephe.fr** | 🔴 **§2.6 により事実源として使用禁止。検索結果に出現したが 1 語も採用していない。**<br>（`saint-estephe.fr` = La Maison du Vin de Saint-Estèphe は appellation body に近いが、§2a の認証を行っていないため不採用） |

---

## Open Questions

### 実ラベル確認タスク（現物が要る。番号は接客上の優先度順）

1. 🔴 **`FRANCE | WHITE > BORDEAUX` / 2019 / $520 のボトルを見て、
   ラベルの (a) キュヴェ名が `Cos d'Estournel Blanc` か `Pagodes de Cos Blanc` か、
   (b) **アペラシオン行の正確な文字列**を書き写す。**
   → **これ 1 本で「白の AOC は何か」という本ドシエ最大の未解決点が閉じる。**
2. 🔴 **同 / 2018 / $680 のボトルで同じ 2 点。**
   （**`Pagodes de Cos Blanc` の初ヴィンテージがまさに 2018 である**ため、この 1 本は特に判別価値が高い）
3. **`FRANCE | RED > BORDEAUX` / 2018 / $900 のラベルが
   `Château Cos d'Estournel` か `Pagodes de Cos` かを確認する。**
4. **同 / 2015 / $800 で同じ確認。**
5. **4 本すべてについて、ラベル上の生産者名が
   `Château` を前置しているか／アポストロフィが `’`（U+2019）か `'`（U+0027）か
   を *文字単位で* 記録する。** → `S-2` / `C-1` の一次証拠になる。
6. **赤 2 本の背ラベルに「MIS EN BOUTEILLE AU CHÂTEAU」および
   `DOMAINES REYBIER`（または別の法人名）が印字されているかを確認する。**
   → 法人名と表示名の対応が確定する。
7. **白のボトルに有機認証のロゴ（EU リーフ / AB / Ecocert）が
   *無い* ことを確認する**（2018・2019 は転換開始前。あった場合はそれ自体が重大な発見）。

### 資料・照会の未解決

8. 🔴 **`Cos d'Estournel Blanc` / `Pagodes de Cos Blanc` の AOC を、生産者に直接照会する。**
   `estournel@estournel.com`。公式サイトはアペラシオンを構造的に持っていない
   （＝「公表を止めた」型でも「サイトが古い」型でもなく、**「そもそも一度も公表していない」型**）。
9. **1855 年格付の *法定原文* を取得する。** `crus-classes.com` は DNS 解決せず、
   INAO 側も 403。**現状、格付の根拠は公式サイトの自己記述のみ。**
10. **AOC Saint-Estèphe の *consolidated* CDC（2021-10-26 arrêté 版）を
    `info.agriculture.gouv.fr/gedei/site/bo-agri/` から取得する。**
    本書が使ったのは 2010 年の PNO 版である（§2c）。
11. **HVE / Demeter / Terra Vitis 等の取得有無を、公的登録簿で SIRET `33132110900018` により照会する。**
    公式サイトは沈黙している。
12. **`Château Cos Labory` の取得日を法定文書で確定する。**
    登録簿の傍証（旧法人 2024-12-31 閉鎖／新事業所の開設）はあるが、日付を明示する一次文書は未取得。
13. 🔍 **`beverage_menu_bottles.doc` の 17 ページ目そのものを見る。**
    WHITE と RED の両セクションが `section_start_page = "17"` を共有しているのは、
    **transcription 側でページ番号が引き継がれた可能性**がある。
    **メニュー現物で、白の Cos が本当に「WHITE > BORDEAUX」の見出しの下に印字されているかを確認する。**
    → これが否なら、§Canonical Conflict ① の結論（＝色は正しい）が変わる。
14. ⚠️ **`Gris de Cos`（canonical が挙げるロゼ）が過去に存在したかを、
    Internet Archive の公式サイト旧版で確認する。** 本書では未実施。
15. ✅ **【解決済 · CLOSED】** **セカンド／白の名称走査を intake 層でやり直す件。**
    🔍 **orchestrator が intake 層で実施済（2026-08-06）。**
    成果物 **`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`、全 704 行**。
    走査対象フィールドは **`source_producer_raw` + `source_wine_raw`**、大文字小文字を無視した正規表現で
    本バッチの Bordeaux のセカンド／サード／白の名称を網羅
    （`pagode` / `goulée|goulee` / `labory` / `alter ego` / `sirène|sirene` / `petit mouton` / `aile d` /
    `clarence` / `clarté|clarte` / `forts de` / `pavillon` / `ygrec` / `carruades` ＋ `blanc` の総当たり）。
    **結果: 704 行中 16 ヒット。うち Bordeaux のセカンドワインは 1 件も無い。**
    16 件はすべて無関係な行の `Blanc` / `Blancs` の語である
    —— Champagne の Blanc de Blancs（Robert Moncuit・Vilmart）、ブルゴーニュの白
    （Eric Forest・Laroche・Louis Liger Leblanc）、Anne-Claude Leflaive の Clau de Nell、
    Ultramarine（Sonoma）のスパークリング 3 件、Grgich・Kazumi・Hundred Acre の Sauvignon Blanc、
    ＋ `Cheval Blanc` 2 件（**これは生産者名**）。
    → 🔴 **`Pagodes de Cos` / `Goulée` / `G d'Estournel` / `Cos Labory` は
    intake 層でも store 層でも出現回数 0。本書の当初の結論は正しく、
    誤っていたのは *それを測った成果物* だけだった。**
    → **消去法は依然として使えない。行 3・行 4 は実ラベルが要る**（実ラベル確認タスク 3・4 は存置）。

    🔴 **さらに重要な scope —— これは Cos に固有の欠落ではない。**
    **OBP の Bordeaux セクションは、どの生産者についても、どちらの層でも、
    セカンドワインの名称を一度も印字していない。**
    → **だからこそ「アペラシオンだけが印字された列」が Bordeaux ブロック全体の拘束条件になる。**
    **本ブロックの他の 7 生産者にも同じ制約が等しくかかる**（Pavillon Rouge/Blanc・Les Forts de Latour・
    Le Petit Mouton・Aile d'Argent・Le Clarence・Alter Ego・La Sirène・Ygrec 等はいずれも
    メニュー上に存在しない）。**個別ドシエごとに再走査する必要は無い。**
