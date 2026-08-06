# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件も存在しない。**
> **928 レコードの export 全体を機械走査し、`producer` 完全一致（`Chappellet`）0 件、
> 文字列 `Chappellet` / `chappellet` の部分一致も 0 件であることを実測した。OBP は 3 行。
> すなわち 3 行すべてが canonical の「欠落（gap）」である。**
> 🔒 **gap は conflict ではない（`CDX-23`・Abreu 先例）。canonical も `REGISTER.md` も一切書き換えていない。**
> 🔒 **「不在（absent）」と「存在するが到達できない（unreachable）」は別物である。本件は純粋な不在である。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式資料で確認**（`chappellet.com` 本体・同ドメイン配信の公式 PDF（技術資料・プレスキット）・公式ボトルショット画像、
>    および生産者自身の EC バックエンド（Commerce7 テナント `chappellet-winery`）が返す自社カタログ本文）
> `🏛` **公的登録簿／規制一次資料** —— **27 CFR Part 9 / Part 4（eCFR 現行版）**、**eCFR title-27 構造 API**、**Verisign RDAP**
> `📄` **生産者著作だが生産者ドメイン外で配信されている資料**（**本書では 0 件。使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している／第三者の主張であって未確認**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://chappellet.com/`**
> 走査元: **`robots.txt` → `sitemap_index.xml`（子サイトマップ 6 本）**、
> **`page-sitemap.xml`（108 URL）/ `assets-sitemap.xml`（62）/ `press-sitemap.xml`（25）/ `trades-sitemap.xml`（69）/
> `wines-sitemap.xml`（2 —— 実質空）**、および**生産者自身の EC カタログ全 384 プロダクト**（8 頁を機械取得）
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ① —— `Pritchard Hill` は AVA ではない。推測ではなく機械走査で確定した。**
> 🏛 **eCFR の 27 CFR title-27 構造 API を取得し、Part 9（AVA）の全 288 セクションを列挙した。
> 文字列 `Pritchard` は title-27 の構造全体に 1 件も存在しない。Napa Valley は `§ 9.23` である。**
> 🔴 **したがって `Pritchard Hill` は「行 3 のキュヴェ名」であり、かつ「地名」でもある —— (c) 両方が正解である。**
> **フロントラベルには `CHAPPELLET` の下に `Pritchard Hill`（赤い筆記体）、その隣に `NAPA VALLEY` と `CABERNET SAUVIGNON` が並ぶ。
> 産地表示（appellation of origin）はあくまで `NAPA VALLEY` であって `Pritchard Hill` ではない。**
> ✅ **蔵自身も全公式資料を通じて `AVA` / `appellation` の語を一度も使っていない**（本調査で取得した生産者資料 40 点超を機械検索して 0 件）。
> → §Location・§Important Cuvées 行 3
>
> 🔴 **本ドシエ最大の収穫 ② —— `Signature` は蔵が自分で定義した designation である。カテゴリー語ではない。**
> ✅ **蔵の公式年表（1980 年の項）：「Donn Chappellet wanted a way to distinguish this great vintage and decided that
> the best way to highlight it would be to give it his stamp of approval by signing the bottle. Chappellet did not
> designate another “Signature” Cabernet Sauvignon until 1984, at which time they made the decision to make the
> “Signature” an ongoing part of the portfolio by selecting the best overall lots to be blended into this wine.」**
> → 🔴 **`CDX-15`（メニューがカテゴリー語をキュヴェ名として印字する型）は本行では成立しない。**
> **Ridge の `ESTATE` と同じ結論に、まったく別の証拠経路で到達した（`3f-10`：パターンの存在は個々の行の証拠ではない）。**
>
> 🔴 **本ドシエ最大の収穫 ③ —— それでも「`Signature` はフロントラベルに印字されていない」。**
> 🔴 **蔵が配信するボトルショットのフロントラベルは `CHAPPELLET` ／ **Donn Chappellet の金色の直筆サイン** ／
> `Napa Valley` ／ `Cabernet Sauvignon` ／ `PRODUCED AND BOTTLED BY CHAPPELLET VINEYARD, ST. HELENA, CA U.S.A. / B.W. 4337`。**
> 🔴 **`Signature` という「語」はどこにも無い。ラベルにあるのは「署名そのもの」である。**
> → **メニューの `"Signature,"` は蔵の公式製品名として正しい。しかし「ラベルに Signature と書いてある」は言えない。** → §Staff Notes ⚠️ ③
>
> 🔴 **本ドシエ最大の収穫 ④ —— 3 本すべての per-vintage 技術資料（公式 PDF）が取得できた。**
> **セパージュ・アルコール・Brix・TA・pH・収穫期間・瓶詰月が 2021 / 2022 の両年で確定している。**
> 🏛 **27 CFR § 4.23(b) の 75% 要件は 3 本とも充足**（2021 Signature 79% / 2022 Signature 82% / 2022 Pritchard Hill 94%）。
>
> ⚠️ **調査上の制約 ① —— 蔵の EC 商品ページのメタデータがヴィンテージ的に腐っている。**
> 🔴 **2022 Signature の商品ページの `Growing Season` 欄は **2020 年**の生育期を説明しており、
> 2022 Pritchard Hill の同欄は **2019 年**を説明し、引用レビューも 2019 年ヴィンテージのものである。**
> → 🔴 **本書は per-vintage の事実をすべて公式 PDF（wine notes）から取り、商品ページ本文は使っていない。** → §Canonical Conflict ③
>
> ⚠️ **調査上の制約 ② —— ボトルショットは「型番なし」の汎用画像である。**
> **Signature・Pritchard Hill とも、蔵が配信する画像にヴィンテージ表示が無く、Signature の画像の `ALC. 14.5% BY VOL` は
> 2021（14.7%）とも 2022（14.9%）とも一致しない。しかも蔵はこの同じ画像を 2022 年のトレード資料にも使っている。**
> → 🔴 **ラベルの「構造」の証拠にはなるが、2021 / 2022 の現物ラベルの証拠にはならない。** → Open Questions 1（実ボトル案件）
>
> ⚠️ **調査上の制約 ③ —— 🏛 TTB COLA・🏛 California SOS・🏛 USDA Organic INTEGRITY の 3 つがすべてゲートされていた。**
> **TTB は F5/Shape 系 bot 防御（`bobcmn` / `TSPD_101` / `captcha_audio`）、California SOS bizfile は Incapsula で `403`、
> USDA INTEGRITY は Blazor の JS シェルのみ（API は `400`）。ルールに従い突破は一切試みていない。**
> **⚠️ ゲートは「記録が存在しない」ことの証拠ではない。**

---

## Identity

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Chappellet`** |
| **Canonical Name** | ✅ **`Chappellet`**（蔵自身がブランド名として単独で用いる。ラベル最上部も `CHAPPELLET` の 1 語） |
| 🔴 **法人名** | ✅ 🔴 **`Chappellet Winery, Inc.`**<br>✅ **Terms of Use 冒頭：「Welcome to the Chappellet Winery website (the “Site”). **The Site is owned by Chappellet Winery, Inc.**」**<br>⚠️ 🔴 **ただし蔵は自分を 3 通りに名乗る。①法務表示 `Chappellet Winery, Inc.` ②ラベルの生産表示 `CHAPPELLET VINEYARD` ③公式アクセス案内 `Chappellet Vineyard and Winery`。**<br>🏛 ⚠️ **California SOS（`bizfileonline.sos.ca.gov`）が Incapsula で `403` のため、登記上どれが正式名かは独立照合できていない** → Open Questions 5 |
| 🔴 **ラベル上のブランド名** | ✅ 🔴 **`CHAPPELLET`（単独）＋赤い三角のロゴマーク。**2 本のフロントラベルとも最上部（Pritchard Hill は縦組み）にこの 1 語が入る |
| 🔴 **ラベルの生産表示** | ✅ 🔴 **`PRODUCED AND BOTTLED BY CHAPPELLET VINEYARD, ST. HELENA, CA U.S.A.` ／ `B.W. 4337`**（Signature のボトルショットから実読）<br>🔴 **`GROWN, PRODUCED AND BOTTLED BY` でも `ESTATE BOTTLED` でもない。** → §Staff Notes ⚠️ ⑥ |
| **Aliases** | 🔍 **`Chappellet`**（OBP 印字）／✅ **`CHAPPELLET`**（ラベル）／✅ **`Chappellet Winery, Inc.`**（法務）／✅ **`Chappellet Vineyard`**（ラベル生産表示）／✅ **`Chappellet Vineyard and Winery`**（アクセス案内） |
| 🔴 **所在** | ✅ 🔴 **`1581 Sage Canyon Road, St. Helena, CA 94574` ／ `(707) 286-4219`**<br>**生産者自身のアクセス案内 PDF/画像（`WineryDirections2026`）とサイト内の予約頁の双方に同一表記。**<br>🔴 **同案内はこう書く：「the third driveway (#1581), marked by a post with addresses on the right and **a row of silver mailboxes on the left labeled “Pritchard Hill.”**」** |
| **旧・現の電話番号** | ✅ **2021 年の技術資料は `707-963-7136`、2022 年の技術資料は `707-286-4219`。**現行は後者 |
| 🔴 **創業** | ✅ 🔴 **1967 年、`Donn Chappellet` と `Molly Chappellet` による。**公式：「Founded by Molly and Donn Chappellet in 1967」<br>⚠️ **「初ヴィンテージ 1968 年」「初の商業リリース Cabernet Sauvignon 1969 年」は別の年である。混ぜない** |
| 🔴 **所有** | ✅ 🔴 **Chappellet 家（第 2 世代）。**公式：「one of the great Napa Valley wineries, and one of the few which remains family owned」<br>**`Cyril Chappellet` = CEO & Chairman of the Board／`Dominic Chappellet` = Co-owner & COO／`Carissa Chappellet` = Owner, Board Member／`Lygia Chappellet` = Owner, Board Member／`Alexa Chappellet` = Board Member, Shareholder／`Molly Chappellet` = Founder** |
| 🔴 **経営** | ✅ **`David Francke` = President（前職 Robert Mondavi の GM/VP、Folio Fine Wine Partners の managing director）／`Christine Ha` = CFO／`Mitch Boyd` = VP, Global Sales／`Brennan Anderson` = VP of Marketing。**<br>**取締役に `Tony Tjan`、`Jack Daniels`** |
| 🔴 **醸造責任者** | ✅ 🔴 **`Phillip Corallo-Titus` —— Vice President of Winemaking。**<br>**1981 年に assistant winemaker として入社 → 4 年後に Stratford・Cartlidge & Brown へ → **1990 年に Donn Chappellet の招きで winemaker として復帰**、以後現職。UC Davis で agronomy / viticulture / enology。**<br>🔴 **OBP 3 本の技術資料すべてに彼の名が印字されている** |
| 🔴 **醸造家** | ✅ 🔴 **`Ry Richards` —— Winemaker。**2006 年にセラーチームに入り、**2023 年に winemaker に昇格**。<br>🔴 **2022 Pritchard Hill の技術資料は `Vice President of Winemaking Phillip Corallo-Titus` ＋ `Winemaker Ry Richards` の連名。2021 年の 2 本は Phillip 単独名義である** |
| **栽培責任者** | ✅ **`Andrew Opatz` —— Director of Vineyard Operations。**2008 年入社。**前任の長年の vineyard manager `Dave Pirio` は 2023 年に退任。**Andrew は Dave の甥。**「manages our organic certification program」** |
| 🔴 **canonical id** | 🔍 🔴 **無し（0 件）。** `producer` 完全一致・部分一致とも 0 |
| 🏛 **ドメイン** | 🏛 **`chappellet.com` —— Verisign RDAP で `registration 1995-12-14`／`expiration 2027-12-13`／`last changed 2025-12-14`。NS は `PDNS07/08.DOMAINCONTROL.COM`** |

---

## Overview

✅ **カリフォルニア、ナパヴァレー東側の山、Pritchard Hill。1967 年に Donn と Molly Chappellet が創業した、
ナパで数少ない家族所有のまま残る名門である。**
公式の言葉：「**For almost 60 years, the Chappellet family has been crafting globally renowned wines made from fruit
cultivated on the steep, rocky slopes of Napa Valley's renowned Pritchard Hill. As one of the first wineries to pioneer
high-elevation hillside planting, and one of the few remaining great family-owned Napa Valley wineries, Chappellet has
influenced generations of vintners.**」

🔴 ✅ **蔵の自己規定は 3 つに集約される —— `mountain-grown`（山で穫る）、`hillside Cabernet Sauvignon`（丘のカベルネ）、
`Pritchard Hill`（場所そのもの）。**
「**Unlike the other great emerging Napa Valley wineries of the day, Chappellet chose a different path from its
contemporaries, looking beyond the valley floor towards the steep, rugged hillsides of Pritchard Hill.**」
🔴 **創業の動機はボルドーである：「**When Donn and Molly Chappellet founded Chappellet in 1967, their goal was to create
world-class wines with the depth, complexity and character of the finest first growths of Bordeaux.**」**

🔴 ✅ **そして蔵は、自分たちが Pritchard Hill という「場所の名」を確立した側だと明言している。**
「**Chappellet helped to establish Pritchard Hill as perhaps California's most revered winegrowing region.**」
→ 🔴 **この 1 文が本ドシエの中心線である。`Pritchard Hill` はキュヴェ名でもあり地名でもあり、
しかも法的な産地名（AVA）ではない。** → §Location

🔍 **THÉSEUS における状態は「3 行に対して 0 レコード」。canonical はこの蔵をまったく知らない。**
🔍 ⚠️ **ただし canonical は `Pritchard Hill` という文字列を 1 件だけ持っている —— 別の生産者 `Continuum Estate` の
`subregion` 値 `Napa Valley — Pritchard Hill` である。** → §Canonical Conflict ②

---

## History

### Foundation（創業）

| 年 | 出来事 | 典拠 |
|---|---|---|
| **1931** | **`Donn Chappellet` ロサンゼルス生まれ。1954 年に Pomona College を経済学で卒業。大学時代からボルドーを蒐集。** | ✅ **公式 Donn Chappellet 略歴** |
| **1950 年代半ば** | **コーヒー自動販売の `Interstate United Corporation` を共同創業。従業員 7,000 人超、NYSE 上場、業界全米 3 位まで育てる。** | ✅ **同上** |
| 🔴 **1966** | 🔴 **Interstate United の持株を売却し、**伝説的醸造家 `André Tchelistcheff`（Beaulieu Vineyards）の助言に導かれて**ナパヴァレー東端の岩がちな山地 320 エーカーを購入。** | ✅ **公式：「In 1966 he sold his shares in Interstate United and guided by the legendary winemaker Andre Tchelistcheff of Beaulieu Vineyards bought 320 acres of rocky mountain terrain at the eastern edge of the Napa Valley.」** |
| 🔴 **1967** | 🔴 **創業。**⚠️ **蔵は「**established the second new winery there after the repeal of Prohibition and became the 18th registered member of the Napa Valley Vintners**」とも書く（禁酒法廃止後 2 番目の新設ワイナリー／Napa Valley Vintners の 18 番目の登録会員）。**本書はこれを**生産者の主張として**記録し、独立の裏づけは取っていない | ✅ **公式 A Family Story** |
| **1968** | **ワイナリー着工。抽象画家 `Ed Moses` の設計、エジプトのピラミッドに範を取った建築。**後に英国のワインライター Hugh Johnson が「the most remarkable wine cathedral of the modern world」と呼ぶ。**同年が初収穫だが蔵が未完成のため、Mondavi 家が初ヴィンテージの破砕を引き受けた。** | ✅ **公式 A Family Story**<br>⚠️ **Hugh Johnson の評は第三者の言葉である。蔵はそれを引用しているにすぎない** |
| 🔴 **1969** | 🔴 **Donn Chappellet が最初の商業リリースのカベルネ・ソーヴィニヨンを出す。** | ✅ **公式 A Family Story**<br>⚠️ **蔵は同じ文で「It receives 100 points by Robert Parker's Wine Advocate」と書くが、これは第三者媒体の評価であり本書は事実の典拠として採らない** |

### Generations（designation の誕生と現体制）

| 年 | 出来事 | 典拠 |
|---|---|---|
| 🔴 **1980** | 🔴 **`Signature` の誕生。**「**Donn Chappellet wanted a way to distinguish this great vintage and decided that the best way to highlight it would be to give it his stamp of approval by signing the bottle.**」 | ✅ **公式 A Family Story（1980 の項）** |
| 🔴 **1984** | 🔴 **`Signature` が常設ラインに。**「**Chappellet did not designate another “Signature” Cabernet Sauvignon until 1984, at which time they made the decision to make the “Signature” an ongoing part of the portfolio by **selecting the best overall lots to be blended into this wine**.**」 | ✅ **同上。**🔴 **これが `Signature` の蔵自身による定義である** |
| **1988** | **`Cyril Chappellet`（長男）が Cal Poly（farm management）→ Pepperdine（経営）→ 企業の経営企画・M&A を経て蔵に復帰。** | ✅ **公式 Cyril Chappellet 略歴** |
| 🔴 **1997** | 🔴 **`Pritchard Hill Cabernet Sauvignon` の誕生。**「**In 1997, with the emergence of “Cult Wines,” the family felt the need to take one more step toward highlighting the magnificence of Pritchard Hill by **designating a small lot bottling of the best wine the property could produce**.**」 | ✅ **公式 A Family Story（1997 の項）**<br>🔴 **これが `Pritchard Hill` というキュヴェ名の蔵自身による定義である** |
| **1999** | **`Dominic Chappellet` が蔵に復帰。** | ✅ **公式 Dominic Chappellet 略歴** |
| **1980 年代前半** | **「sustainable」という語が使われるよりずっと前に、土壌保全と浸食防止のためカバークロップを導入。** | ✅ **公式 Green Practices** |
| **2008** | **960 枚・20,000 平方フィートの太陽光発電を導入（年間約 280,000 kWh、蔵の PG&E 請求を 100% 相殺）。** | ✅ **同上** |
| **2011** | **醸造用水を生物学的に浄化する処理設備を導入（年間約 100 万ガロンを畑の灌漑に戻す）。** | ✅ **同上** |
| 🔴 **2012** | 🔴 **`California Certified Organic Farmers (CCOF)` による 3 年の認証プロセスを完了し、畑全体（104 エーカー）が有機認証を取得。**同年、ピラミッドの隣に barrel chai（樽庫）を建設、太陽光を載せる。 | ✅ **公式 Land Stewardship / Green Practices / Estate Vineyard** → §Farming |
| **2016** | **`Donn Chappellet` 逝去。**同年、Pritchard Hill の `Hideaway` 区画から単一区画・カベルネ 100% のワインをリリース。 | ✅ **公式 Donn Chappellet 略歴 / A Family Story** |
| **2019** | **`Grower Collection`（ソノマの契約畑のシャルドネ／ピノ・ノワール）を発表。** | ✅ **公式 The Chappellet Story** |
| 🔴 **2023** | 🔴 **`Dominic Chappellet` が COO に就任（それ以前は vice president）。`Ry Richards` が winemaker に昇格。長年の vineyard manager `Dave Pirio` が退任。** | ✅ **公式 Dominic / Ry / Andrew 各略歴** |

⚠️ 🔴 **蔵の資料の中で「Signature は何十年の看板か」の記述が 3 通りに割れている。**
✅ 2021 年の技術資料「**our foundational wine for more than three decades**」／
✅ 2022 年の技術資料「**our foundational wine for well over three decades**」／
✅ EC 商品ページ「**our foundational wine for more than five decades**」。
🔴 **蔵自身の年表では最初の `Signature` は 1980 年（2022 年時点で 42 年）である。**
→ **卓上で「◯十年」という言い方をしない。「1980 年に始まった」と年で言う。** → §Staff Notes ⚠️ ⑦

---

## Location

| | |
|---|---|
| **Country** | **USA**（California, Napa County） |
| 🔴 **Region（法定産地）** | 🏛 🔴 **`Napa Valley`（27 CFR § 9.23）。**「**The name of the viticultural area described in this section is “Napa Valley.”**」／「**The Napa Valley viticultural area is located within Napa County, California.**」<br>🏛 **承認地形図 8 葉＋Napa 郡の税務評価図（`Mt. St. Helena`, `Detert Reservoir`, `St. Helena`, `Jericho Valley`, `Lake Berryessa`, `Mt. Vaca`, `Cordelia`, `Cuttings Wharf`）**<br>🔴 **OBP 3 行すべてがこの 1 つの AVA に属する。`_parts.appellation = "napa valley"` は正しい** |
| 🔴 **`Pritchard Hill` の法的身分** | 🏛 🔴 **AVA ではない。**<br>🏛 **eCFR の title-27 構造 API を取得し、Part 9 の全 **288 セクション**を機械列挙した。`Pritchard` を含むセクションは **0 件**。title-27 の構造全体にも文字列 `Pritchard` は **0 件**。**<br>🏛 **（比較：`Napa` を含むのは `§ 9.23 Napa Valley` / `§ 9.161 Oak Knoll District of Napa Valley` / `§ 9.296 Crystal Springs of Napa Valley` の 3 件のみ）**<br>✅ 🔴 **蔵自身も `AVA` / `appellation` の語を一度も使っていない。**本調査で取得した生産者資料（HTML 30 点超・PDF 15 点）を機械検索して 0 件。蔵が使うのは `region` / `terroir` / `mountain` / `property` である |
| **所在（蔵）** | ✅ **`1581 Sage Canyon Road, St. Helena, CA 94574`。**州道 128 号（Sage Canyon Road）を Silverado Trail から東へ約 3.5 マイル、Lake Hennessey のボートランプ向かい、そこから山道を 1.5 マイル登る |

### 🔴 ✅ Key Vineyard —— `Chappellet Estate Vineyard`（Pritchard Hill。OBP 3 行すべての産地）

| | ✅ 公式の記述 |
|---|---|
| 🔴 **標高** | 🔴 **`800 〜 1,800 フィート`（約 244〜549 m）。**「**Rising from 800 to 1,800 feet above sea level, the Chappellet Estate Vineyard on Pritchard Hill has earned global acclaim…**」 |
| 🔴 **面積** | 🔴 **総地積 `640` エーカー、うち植栽 `104` エーカー（16%）。**「**only 104 of the property's 640 total acres are planted as vineyards**」／「**Only a modest 16% of the 640-acre property is under vine; the rest remains uncultivated.**」<br>🔴 **品種内訳：「**Of the vineyard's 104 planted acres, **85 acres are Cabernet Sauvignon**, with the remainder consisting of small blocks of **Malbec, Cabernet Franc, Petit Verdot and Chenin Blanc**.**」 |
| 🔴 **区画** | ⚠️ 🔴 **公式資料の中で数が割れている。**プレスキット（2024-09 更新）は「**47 distinctive blocks—including 40 blocks of Cabernet Sauvignon**」、ウェブの Pritchard Hill 頁と Winemaking Philosophy PDF は「**48 individual blocks**」。<br>**本書は両方を記録し、どちらも断定しない** |
| ⚠️ **カベルネのクローン数** | ⚠️ 🔴 **これも割れている。**Estate Vineyard PDF は「**ten different Cabernet clones**」、ウェブの Phillip Corallo-Titus 紹介は「**40 blocks and nine clones of Cabernet Sauvignon**」。**卓上で数を言わない** |
| 🔴 **地質・土壌** | 🔴 **「**the roots of Pritchard Hill's greatness date back four million years, when a 14,000-foot volcano dominated what is now the eastern range of the Napa Valley. Erosion, water, wind and sun have combined to sculpt this area over the millennia, leaving Pritchard Hill with its **array of dramatic slopes and thin, volcanic soils**.**」<br>🔴 **土壌名まで公表している：「**varying depths of **Sobrante loam** and **Hambright rock outcrop****」**<br>✅ **Donn の見立て：「**the volcanic soil and warm, dry temperatures of Pritchard Hill contributed strength and character**」** |
| **区画名（判明分）** | ✅ **`Wells Ranch`、`Hideaway`（2016 年から単一区画としてリリース）** |
| 🔴 **既知の区画・ワインの対応** | ✅ 🔴 **`Signature` は「**Sourced from many of the lower elevation plots on Pritchard Hill starting at 800 feet**」**（蔵のトレード資料）<br>⚠️ **`Pritchard Hill` キュヴェの区画は公表されていない。「the best wine the property could produce」までしか書かれていない** |

⚠️ 🔴 **`Pritchard Hill` は蔵の私有地ではない。**蔵の所有地は 640 エーカーであり、
✅ 蔵自身が公式アクセス案内で「a row of silver mailboxes labeled **“Pritchard Hill”**」と書くとおり、
**Pritchard Hill は複数の地所が並ぶ山の名である。**
🔍 ⚠️ **THÉSEUS の canonical 自身が別の生産者（`Continuum Estate`）の `subregion` に
`Napa Valley — Pritchard Hill` を持っている。** → §Canonical Conflict ②
🔴 **本書は「Chappellet が Pritchard Hill の唯一の生産者である」とは書かない。蔵もそう書いていない。**

❓ **公式に無い**: 区画ごとの面積・植樹年・台木・樹齢構成、`Pritchard Hill` キュヴェの由来区画、
畑の総生産量、`Signature` に使う Merlot の出所（→ §Farming の注記）。

---

## Farming

### 🔴 Organic —— **認証は「蔵の記述」までで、証書は取れていない**

✅ 🔴 **蔵の公式記述（3 つの独立した公式資料で一致）**

| 資料 | 記述 |
|---|---|
| ✅ **`/land-stewardship/`** | 「**In 2012, the entire vineyard, totaling 104 acres, finished an extensive three-year certification process with the California Certified Organic Farmers (CCOF) and is now certified organic.**」／「**100% of the grapes grown on the estate vineyard come from blocks that are farmed using organic methods.**」 |
| ✅ **`Chappellet Estate Vineyard`（プレスキット PDF, 2024-09）** | 「**the Chappellet vineyard achieved organic certification from California Certified Organic Farmers (CCOF) in 2012**」 |
| ✅ **`Chappellet Green Practices`（プレスキット PDF, 2024-09）** | 「**In 2012, the vineyard finished an extensive three-year certification process with the California Certified Organic Farmers (CCOF) and is now certified organic and certified Fish Friendly Farming.**」 |
| ✅ **`The Chappellet Story`（プレスキット PDF, 2024-09）** | 「**the Chappellet family meticulously cultivates their estate vineyard using hands-on organic farming techniques**」 |
| ✅ **`Andrew Opatz` 略歴（2024-09）** | **栽培責任者が「**manages our organic certification program**」を職責として持つ** |

⚠️ 🔴 **しかし本調査は認証書・証書番号・有効期間を 1 件も取得できていない。**

| 照合先 | 結果 |
|---|---|
| ✅ **生産者ドメイン** | 🔴 **証書 PDF も証書番号も掲載されていない**（`assets-sitemap.xml` の 62 URL、`page-sitemap.xml` の 108 URL を機械走査済み） |
| 🏛 **USDA Organic INTEGRITY** | ⚠️ **ゲート。**`https://organic.ams.usda.gov/integrity/` は Blazor の JS シェルのみを返し、`POST /integrity/api/OperationSearch` は `400`、`api/Operations/Search` も `400`。**（Batch 9・10・Ridge と同じ所見が再現）** |
| 🏛 **CCOF 会員ディレクトリ** | ⚠️ **`https://www.ccof.org/members/` および `/directory/` はいずれも `404`。**独立照合の経路を確立できていない |

🔴 **したがって本書の立場：**
🔴 **「2012 年に CCOF の有機認証を取得したと蔵が公表している」は言ってよい。**
⚠️ 🔴 **「2021 年産・2022 年産のブドウが認証の射程にあった」は言えない。**
**認証は年次更新制であり、本調査は 2021 / 2022 収穫時点の有効性を示す一次文書を持たない。
蔵の記述は「is now certified organic」という現在形であって、収穫年ごとの言明ではない。** → §Staff Notes ⚠️ ④

⚠️ 🔴 **もうひとつ塞いでおくべき穴。**
✅ **蔵が公表する 104 エーカーの品種内訳は「Cabernet Sauvignon 85 エーカー＋ Malbec / Cabernet Franc / Petit Verdot / Chenin Blanc」で、
`Merlot` が入っていない。**
🔴 **一方 `Signature` のセパージュには Merlot が 2021 年 6%、2022 年 2% 含まれる。**
→ ⚠️ **すなわち `Signature` が 100% 自社畑であるという証拠は無い。蔵もそう書いていない。**
→ 🔴 **「Signature は 100% エステートです」と言わない。** → §Staff Notes ⚠️ ⑤

### Biodynamic

🔴 ⚠️ **本調査で取得した公式資料のいずれにも `biodynamic` / `Demeter` の語は 1 件も現れなかった。**
→ **ビオディナミは主張しない。**

### Sustainable

✅ **蔵が自ら挙げる取り組み（`Green Practices` PDF・`/land-stewardship/`）:**
- **1980 年代前半からのカバークロップ**（「long before the term sustainable was ever used」）、no-till farming
- **`Fish Friendly Farming` 認証**（2012 年の項に併記）⚠️ **認証番号・発効日は未取得**
- **年間 100 トンのポマース（梗・果皮・種）を自家堆肥に**
- **2008 年の太陽光（960 モジュール／20,000 sq ft／年 280,000 kWh／PG&E 請求の 100% 相殺／30 年で温室効果ガス 4,513,275 lbs 削減）**
- **2011 年の醸造用水浄化設備（年約 100 万ガロンを灌漑に還元）＋圃場センサー・自動バルブによる遠隔灌漑管理**
- **巣箱 30 個**（メンフクロウ・チョウゲンボウ・ハイタカ・ルリツグミ）。⚠️ **ウェブの `/land-stewardship/` は「ten bird boxes」と書き、PDF は「30 bird boxes」と書く。数が割れている**
- **UC Davis・Cal Poly Humboldt と共同でルリツグミの在来個体群を研究**
- **羊と山羊を使ってオークの下層植生を間引き、15 エーカー超の shaded fuel break（延焼帯）を造成**

### Other（栽培哲学）

✅ **「**This early adoption of practices such as no-till farming has evolved into a comprehensive program of sustainable
techniques used to eliminate the use of synthetic chemicals. These techniques include the use of cover crops, bird boxes,
on-site composting, beneficial insect releases, and organic fertilizers.**」**
✅ **「**only 104 of the property's 640 total acres are planted as vineyards, meaning a large expanse of uncultivated land
surrounds the vineyards with a natural buffer of beautiful forests and meadows that protect the plants from unwanted
pests and chemicals.**」**（未耕作地を病虫害の緩衝帯として位置づけている）
✅ **「**the vineyard team's commitment to low yields and meticulous canopy management**」／「**the family's belief in
regular replanting to augment quality**」**
✅ **2022 年の熱波対応（技術資料）：「**with extensive irrigation and careful canopy management to protect the fruit from
the sun, we were able to respond to the heat on a **block-by-block basis**.**」**

---

## Winemaking

### ✅ 造り手の原則

✅ **区画別醸造：「**To honor and maintain the natural diversity of Pritchard Hill, the Chappellet team cultivates the
estate as 48 individual vineyard blocks… Because Chappellet's experienced team knows each block intimately, they are
able to approach the winemaking with a greater degree of intuitiveness and artistry.**」**
✅ **「**In the winery, renowned Winemaker Phillip Corallo-Titus… gently ferments and ages most blocks individually to
maintain their distinctive character throughout the winemaking process. To further ensure individuality, different lots
benefit from an array of maceration and fermentation practices of varying lengths and temperatures.**」**
🔴 ✅ **樽：「**Phillip has established an extensive barrel program utilizing the very best barrels from a number of
different **elite French coopers and forests**.**」**
✅ **2020 年に小型発酵槽を導入：「**Small fermentation tanks were installed to match small blocks and manage separate
fermentations.**」**
✅ **ブレンドの思想（2022 年技術資料）：「**with our Red Bordeaux grapes picked at a range of ripeness levels to ensure
abundant options at the blending table**」**

### 🔴 ✅ OBP 3 本の技術仕様（**蔵の公式 wine notes PDF をそのまま実測**）

| 項目 | **2021 Signature Cabernet Sauvignon**<br>（OBP 行 2） | **2022 Signature Cabernet Sauvignon**<br>（OBP 行 1） | **2022 Pritchard Hill Cabernet Sauvignon**<br>（OBP 行 3） |
|---|---|---|---|
| 🔴 **公式製品名** | **`2021 Signature Cabernet Sauvignon` / `Napa Valley`** | **`2022 Signature Cabernet Sauvignon` / `Napa Valley`** | **`2022 Pritchard Hill Cabernet Sauvignon`** |
| 🔴 **セパージュ** | 🔴 **79% Cabernet Sauvignon / 8% Petit Verdot / 7% Malbec / 6% Merlot** | 🔴 **82% Cabernet Sauvignon / 9% Petit Verdot / 7% Malbec / 2% Merlot** | 🔴 **94% Cabernet Sauvignon / 6% Petit Verdot** |
| 🏛 **§ 4.23(b) 75% 要件** | 🔴 **充足（79%）。下限に最も近い** | 🔴 **充足（82%）** | 🔴 **充足（94%）** |
| **アルコール** | **14.7%** | 🔴 **14.9%** | **14.8%** |
| **収穫時 Brix** | **24.5 – 27.0°** | **24.5 – 27.0°** | **25.0 – 27.0°** |
| **TA** | **0.57 g/100 ml** | **0.57 g/100 ml** | **0.60 g/100 ml** |
| **pH** | **3.69** | **3.72** | **3.71** |
| 🔴 **収穫期間** | **9 月 9 日 – 10 月 20 日, 2021** | ⚠️ 🔴 **同一 PDF 内で矛盾。**統計欄「**Sept. 7 – Oct. 20, 2022**」／本文「**Harvest began in early September and concluded on October 17**」 | **9 月 7 日 – 10 月 18 日, 2022**（統計欄と本文が一致） |
| **瓶詰** | **2023 年 6 月** | **2024 年 6 月** | **2024 年 7 月** |
| 🔴 **樽・熟成** | ⚠️ 🔴 **公表されていない** | ⚠️ 🔴 **公表されていない** | 🔴 **22 か月・100% 新樽フレンチオーク**（「**The wine was aged for 22 months in 100 percent new French oak.**」） |
| **醸造者名義** | **Winemaker `Phillip Corallo-Titus`** | **Winemaker `Phillip Corallo-Titus`**<br>⚠️ **同年のトレード資料は `VP of Winemaking Phillip Corallo-Titus` ＋ `Winemaker Ry Richards` の連名。名義が資料間で割れている** | 🔴 **`Vice President of Winemaking Phillip Corallo-Titus` ＋ `Winemaker Ry Richards`** |
| **蔵出し価格（750 ml）** | ✅ **$95.00** | ✅ **$95.00** | ✅ **$325.00** |
| 🔍 **OBP 価格** | 🔍 **$280**（約 2.95 倍） | 🔍 **$280**（約 2.95 倍） | 🔍 **$940**（約 2.89 倍） |

⚠️ 🔴 **`Signature` の樽情報が 2 ヴィンテージとも公表されていないのは、本ドシエの実質的な最大の欠落である。**
**EC 商品ページの古いテイスティングノートに「hints of toasted oak, cardamom, clove and vanilla **from French oak aging**」
とあるが、これは 2020 年ヴィンテージの記述であり、2021 / 2022 の樽構成の根拠にはならない。**
→ **卓上で `Signature` の新樽比率・熟成月数を言わない。** → §Staff Notes ⚠️ ⑧

⚠️ 🔴 **2021 Pritchard Hill（OBP には無いが、比較の実体確認として取得）：95% CS / 5% PV・14.8%・TA 0.56・pH 3.74・
収穫 9/10–10/11・瓶詰 2023 年 7 月・22 か月 100% 新樽フレンチオーク。**
→ **`Pritchard Hill` の 22 か月・新樽 100% は年をまたいで一定の造りである。**

---

## Style

### ✅ 公式テイスティングノート（**蔵の wine notes PDF の逐語**）

| ワイン | 公式ノート（逐語） |
|---|---|
| 🔴 **2021 Signature** | 「**Luxuriously dark and concentrated, this wine displays aromas of cassis, black cherry and boysenberry, as well as notes of fresh herbs and French oak-inspired hints of vanilla, cardamom and clove. On the palate it is beautifully full-bodied with supple, polished tannins and alluring layers of dark berries and spice, with notions of dark chocolate, espresso, sage and anise emerging on the long, dramatic finish.**」 |
| 🔴 **2022 Signature** | 「**Beautifully dark, complex and concentrated, this wine offers luxurious aromas of blackcurrant, dark cherry and plum, layered with hints of cedar, mountain sage, aged tobacco, thyme and toasted oak. The structure is seamless and silky, with a glowing richness that permeates the palate, adding depth and generosity to flavors of black cherry, currant, chocolate and espresso bean, with notions of fresh herbs and barrel spice providing a lovely counterpoint throughout the long, resonating finish.**」 |
| 🔴 **2022 Pritchard Hill** | 「**With captivating complexity and deep and resonant aromas, this stunning wine embodies the essence of the very finest mountain fruit from Pritchard Hill, offering an impressive display of fragrant liqueur-like aromas of black currant, cassis and ripe blackberry. As it gracefully unfurls, notes of violet, sweet oak, cedar and black tea emerge, as well as hints of roasted coffee, graphite, cinnamon stick and vanilla bean. On the weighty palate it is pure and concentrated with polished, mouthcoating tannin framing luxurious layers of berry compote, dark chocolate, anise, wood smoke and sage as they flow to a long, radiant finish.**」 |

### ✅ 公式ヴィンテージノート（**年の性格を造り手の言葉で言える**）

| 年 | 公式の記述（Growing Season & Harvest 欄の逐語） |
|---|---|
| 🔴 **2021** | 🔴 **「**The 2021 growing season began with one of the driest winters on record, followed by a mild spring and summer with **no adverse heat events**. Due to the lack of precipitation, canopy growth was limited and the vines produced **very small berries and clusters**. To ensure ideal ripening and flavor development we closely monitored vine water stress and applied a highly targeted irrigation strategy. While the drought yielded a small crop, the long, temperate growing season combined with ideal harvest weather produced dark and powerful wines with concentrated aromas and flavors, excellent structure and lush, mouthcoating tannins.**」**<br>**（Signature・Pritchard Hill の両 PDF に同文で載る）** |
| 🔴 **2022** | 🔴 **「**2022 began with **generous winter rains** that filled our reservoirs and saturated our soils. A cool, dry spring was followed by ideal summer weather with **no days above 100º F until a significant heat event beginning near Labor Day**. Thankfully, with extensive irrigation and careful canopy management to protect the fruit from the sun, we were able to respond to the heat on a **block-by-block basis**.**」**<br>**（Signature・Pritchard Hill の両 PDF に同文で載る。末尾の収穫終了日だけが 2 本で異なる）** |

🔴 **2 年の対比は明快である ——**
**2021 = 記録的に乾いた冬・熱波なし・小粒小房・少量。2022 = 潤沢な冬雨・レイバーデー前後の熱波を区画単位でしのいだ年。**

### 🔴 ✅ スタイルの骨格（造り手の自己記述）

- 🔴 **`Signature` = 「foundational wine」であり「flagship wine」。**
  「**It is a benchmark for the long-lived hillside wines of the Napa Valley; full of structure and aging potential,
  yet seductively forward in its concentrated varietal character. The dry, rocky soils of Pritchard Hill produce small,
  intensely flavorful grapes. Crop thinning allows for full, even ripening and elevates flavor complexity.**」
  ✅ **蔵の体験プログラム頁も「**our flagship wine, the Signature Cabernet Sauvignon**」と呼ぶ。**
- 🔴 **`Pritchard Hill` = 「the pinnacle of Chappellet winemaking」。**
  「**The most sought-after wine in our portfolio, this limited-production Cabernet Sauvignon represents the pinnacle of
  Chappellet winemaking and embodies the elegant power and complexity of Pritchard Hill winegrowing. **Like the great
  Bordeaux wines that first inspired Donn Chappellet, this wine is crafted by blending Cabernet Sauvignon with other
  classic Bordeaux varietals.** … Grown on our rocky, mountainside vineyard, our Cabernets have consistently displayed
  an ability to age for several decades.**」
- ✅ **蔵全体のスタイル記述：「**wines defined by their strength, finesse and age-worthiness**」／
  「**Recognized for their signature mix of grandeur, power and purity**」。**
  ⚠️ **後者の `signature` は普通名詞であってキュヴェ名ではない。混同しない。**

---

## Important Cuvées

### 🔴 まず本節の 2 つの論点を先に決着させる

#### 🔴 論点 A —— `Signature` はカテゴリー語か、蔵の designation か

| 検証 | 結果 |
|---|---|
| ✅ **蔵自身の定義があるか** | 🔴 **ある。**公式年表 1980 年の項と 1984 年の項が、designation の起源と選抜基準（「**selecting the best overall lots to be blended into this wine**」）を明記している |
| ✅ **公式製品名に入っているか** | 🔴 **入っている。**EC カタログ全 384 プロダクトの機械走査で、`Signature Cabernet Sauvignon` は 1980 年代から現行まで連続して存在する製品系列である |
| ✅ **技術資料の表題か** | 🔴 **そう。**wine notes PDF の表題が `2021 Signature Cabernet Sauvignon / Napa Valley`、`2022 Signature Cabernet Sauvignon / Napa Valley` |
| 🔴 **フロントラベルに「語」として印字されているか** | 🔴 **されていない。**ラベルにあるのは **Donn Chappellet の金色の直筆サインそのもの**であって、`Signature` という単語ではない |
| **判定** | 🔴 **カテゴリー語ではない。`CDX-15` は本行では成立しない。**<br>🔴 **メニューの `"Signature,"` は蔵の公式製品名として正確である。**<br>⚠️ **ただし「ラベルに Signature と書いてある」は誤りである** |

#### 🔴 論点 B —— `Pritchard Hill` は (a) キュヴェ名 / (b) 固有designation としての地名 / (c) 両方か

| 検証 | 結果 |
|---|---|
| ✅ **キュヴェ名として実在するか** | 🔴 **する。**公式製品名 `2022 Pritchard Hill Cabernet Sauvignon`。蔵の年表 1997 年の項が命名の経緯を明記（「designating a small lot bottling of the best wine the property could produce」） |
| 🔴 **フロントラベルに印字されているか** | 🔴 **されている。**縦組みの `CHAPPELLET` の右に **`Pritchard Hill`（赤い筆記体）**、その右に `NAPA VALLEY` と `CABERNET SAUVIGNON`、下に赤い三角ロゴ |
| 🏛 **AVA か** | 🔴 **違う。**27 CFR Part 9 の全 288 セクションに `Pritchard` は 0 件。title-27 構造全体でも 0 件 |
| 🔴 **ラベル上の産地表示は何か** | 🔴 **`NAPA VALLEY`（= 🏛 § 9.23）。**`Pritchard Hill` は産地表示の位置にはない |
| 🔴 **地名として実在するか** | 🔴 **する。**蔵自身の公式アクセス案内が、山の入口に「**a row of silver mailboxes … labeled “Pritchard Hill”**」があると書いている。蔵は自分たちが「Pritchard Hill を winegrowing region として確立するのを助けた」とも書く |
| **判定** | 🔴 **(c) 両方である。**<br>🔴 **`Pritchard Hill` は ①この蔵の $940 のワインのキュヴェ名であり ②地名でもあり ③AVA ではない。**<br>🏛 **参考条文：27 CFR § 4.39(i)(3)「A name has viticultural significance when it is the name of a state or county…, **when approved as a viticultural area in part 9 of this chapter**, or by a foreign government, or **when found to have viticultural significance by the appropriate TTB officer**.」**<br>⚠️ 🔴 **末尾の「TTB officer が viticultural significance を認めた場合」に当たるか否かは CFR には現れない行政判断であり、TTB COLA がゲートされている本調査では確認できない。本書は断定しない** |

⚠️ 🔴 **他生産者による `Pritchard Hill` の使用について。**
🔍 **THÉSEUS の canonical 自身が、別の生産者 `Continuum Estate` の `subregion` に `Napa Valley — Pritchard Hill` を持っている。**
🔴 **すなわち「Pritchard Hill を名乗る（あるいは所在地とする）生産者は Chappellet だけではない」ことは THÉSEUS の DB 内でも確認できる。**
⚠️ 🔴 **命名をめぐる争いについて、公的に文書化された記録は本調査で 1 件も取得できていない。**
**🏛 USPTO の商標検索（`tmsearch.uspto.gov`）は Angular の SPA で、API 経路（`api-v1-0-0/tmsearch` ほか 3 経路）はいずれも `405` を返した。**
**蔵の公式サイトにも商標・係争に触れる記述は 1 件も無い（`trademark` の語は Terms of Use の定型文にしか現れない）。**
→ 🔴 **本書は命名の争いについて何も述べない。「Chappellet が Pritchard Hill を代表する蔵のひとつである」までにとどめる。** → §Staff Notes ⚠️ ⑨

---

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 3 行。3 行とも `match_state` / `producer_state` / `cuvee_state` / `vintage_state` すべて `unresolved`・`confidence 0.0`**）

#### 🔴 行 1 —— `obp-beverage-2026-08:21beac6c98`
**印字 `"Signature," Napa Valley Cabernet Sauvignon` / VT 2022 / $280 / `UNITED STATES | RED > NAPA`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。公式製品名は `2022 Signature Cabernet Sauvignon`（Napa Valley）。**蔵出し $95.00 |
| 🔴 **`"Signature,"` の身分** | 🔴 **蔵が 1980 年に始め 1984 年に常設化した designation。カテゴリー語ではない**（→ 論点 A） |
| 🔴 **ラベル実読**（公式ボトルショット `sig_cab-bottle-scaled.jpg`） | 🔴 **上から `CHAPPELLET`（＋赤い三角ロゴ）／**金色の直筆サイン**／`Napa Valley`／`Cabernet Sauvignon`。**<br>🔴 **右下に `PRODUCED AND BOTTLED BY CHAPPELLET VINEYARD, ST. HELENA, CA U.S.A. / B.W. 4337 / ALC. 14.5% BY VOL`**<br>⚠️ **この画像は汎用のストック画像である。ヴィンテージ表示が無く、`14.5%` は 2022 年の公表値 `14.9%` と一致しない。蔵はこの同じ画像を 2022 年のトレード資料にも使っている。ラベルの「構造」の証拠であって 2022 年現物の証拠ではない** |
| 🏛 **`Cabernet Sauvignon` の表示は適法か** | 🔴 **適法。82%。**🏛 **27 CFR § 4.23(b)：「the name of a single grape variety may be used as the type designation if **not less than 75 percent** of the wine is derived from grapes of that variety, the entire 75 percent of which was grown in the labeled appellation of origin area」**<br>⚠️ **残り 18% は Petit Verdot 9%・Malbec 7%・Merlot 2%。「ほぼ全部カベルネ」ではない** |
| 🔴 **`Napa Valley` は正しいか** | 🔴 **正しい。**ラベル・技術資料・🏛 § 9.23 の 3 経路で一致。`_parts.appellation = "napa valley"` も正しい |
| ⚠️ **取り違えリスク** | ⚠️ 🔴 **同じ OBP ファイル内に `Darioush` の `'Signature,'` が 3 行ある**（Napa Valley Cabernet Sauvignon 2022 / Chardonnay 2023 / Merlot 2023）。**`Signature` は 2 つの蔵がそれぞれ自分の designation として使う語である。生産者を外して語らない** |
| 🔍 **canonical** | 🔴 **対応レコード無し（gap）** |

#### 🔴 行 2 —— `obp-beverage-2026-08:34ffe95190`
**印字 `"Signature," Napa Valley Cabernet Sauvignon` / VT 2021 / $280 / `UNITED STATES | RED > NAPA`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。公式製品名は `2021 Signature Cabernet Sauvignon`（Napa Valley）。**蔵出し $95.00 |
| 🔴 **2022 年との違い（ここが行 1 と行 2 を分ける唯一の実質）** | 🔴 **セパージュ：79/8/7/6（CS/PV/Malbec/Merlot）—— 2022 の 82/9/7/2 より Merlot が 3 倍。**<br>🔴 **アルコール 14.7%（2022 は 14.9%）／pH 3.69（同 3.72）／TA は両年とも 0.57。**<br>🔴 **年の性格が正反対：2021 は記録的な乾いた冬・熱波なし・小粒小房の少量年。2022 は潤沢な冬雨＋レイバーデーの熱波。**<br>🔴 **瓶詰 2023 年 6 月（2022 は 2024 年 6 月）** |
| 🏛 **§ 4.23(b)** | 🔴 **適法。79%。**⚠️ **3 本の中で 75% の下限に最も近い。「ほぼ全部カベルネ」は 2021 年について特に言えない** |
| 🔴 **ラベル** | ⚠️ **行 1 と同じ汎用ボトルショットしか存在しない。2021 年現物のラベルは未取得** |
| 🔍 **canonical** | 🔴 **対応レコード無し（gap）** |

#### 🔴 行 3 —— `obp-beverage-2026-08:e727ecdf8d`
**印字 `"Pritchard Hill," Napa Valley Cabernet Sauvignon` / VT 2022 / $940 / `UNITED STATES | RED > NAPA`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。公式製品名は `2022 Pritchard Hill Cabernet Sauvignon`。**蔵出し $325.00 |
| 🔴 **`"Pritchard Hill,"` の身分** | 🔴 **キュヴェ名であり地名でもある（両方）。AVA ではない**（→ 論点 B） |
| 🔴 **ラベル実読**（公式ボトルショット `pritchard_hill-bottle-scaled.jpg`） | 🔴 **縦組みで `CHAPPELLET` ／ **`Pritchard Hill`（赤い筆記体）** ／ `NAPA VALLEY` ／ `CABERNET SAUVIGNON` ／ 赤い三角ロゴ**<br>⚠️ **ヴィンテージ表示・アルコール表示・生産表示は本画像では読めない。汎用画像である** |
| 🏛 **`Cabernet Sauvignon` の表示は適法か** | 🔴 **適法。94%。**残り 6% は Petit Verdot のみ。**3 本の中で最もカベルネ純度が高い** |
| 🔴 **造り** | 🔴 **22 か月・100% 新樽フレンチオーク。**収穫 9/7–10/18/2022、瓶詰 2024 年 7 月、14.8%、Brix 25.0–27.0°、TA 0.60、pH 3.71 |
| 🔴 **蔵の位置づけ** | 🔴 **「the pinnacle of Chappellet winemaking」「The most sought-after wine in our portfolio」「limited-production」。**1997 年に「the best wine the property could produce」を designating する目的で始まった |
| ⚠️ **入手経路** | ✅ **蔵の公式頁：「otherwise only available by allocation」「Pritchard Hill Estate Allocation」（3 / 6 / 12 本の年次配分）。**同じ配分に `Hideaway` Cabernet Sauvignon が併存する |
| 🏛 **参考条文** | 🏛 **27 CFR § 4.39(m)：「the name of a vineyard, orchard, farm or ranch shall not be used on a wine label, unless **95 percent** of the wine in the container was produced from primary winemaking material grown on the named vineyard…」**<br>⚠️ **`Pritchard Hill` が「畑の名」として扱われているのか「fanciful name」として扱われているのかは、TTB COLA がゲートされている本調査では確認できない。断定しない** |
| 🔍 **canonical** | 🔴 **対応レコード無し（gap）。**⚠️ **文字列 `Pritchard Hill` は canonical に 1 件だけあるが、それは `Continuum Estate` の `subregion` 値である** |

### ✅ 生産者の主要ラインナップ（**canonical には 1 件も無い。参考**）

🔍 **蔵自身の EC カタログ全 384 プロダクトを機械走査して確認できた系列:**
🔴 **`Pritchard Hill Cabernet Sauvignon`（1997〜）**⭐OBP／🔴 **`Signature Cabernet Sauvignon`（1980・1984〜）**⭐OBP／
**`Hideaway Cabernet Sauvignon`（2016〜。Hideaway 区画の単一区画）／`Cabernet Franc`／`Merlot`／`Malbec`／
`Las Piedras`／`Cultivation`／`Chenin Blanc`（`Signature Chenin Blanc` とも）／`Mountain Cuvee`／`Zinfandel`（Sonoma Valley）／
`Grower Collection`（2019〜。Sonoma の Chardonnay `Sangiacomo` / `El Novillero` / `Calesa`、Pinot Noir `Dutton Ranch` /
`Apple Lane` / `Fedrick Ranch`、Viognier `Eagle View`）／`Sonoma-Loeb`（Phillip Corallo-Titus が兼務）／
過去の実験的ボトリング（`Clone 337`、`Clone 4`、`Cultivation`）**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① ナパの谷底ではなく「山」を選んだ蔵。1967 年創業、いまも家族所有。**
「**ナパヴァレーの東側、Lake Hennessey の上にそびえる Pritchard Hill という山の上**にある蔵です。
**創業は 1967 年、Donn と Molly Chappellet 夫妻。**Donn はもともとコーヒー自販機の会社を
ニューヨーク証券取引所に上場させた実業家で、**1966 年にその持株を売り、Beaulieu の André Tchelistcheff の助言で
この岩山 320 エーカーを買いました。**
**当時のナパの新興ワイナリーが谷底を選ぶなか、ここだけが山の斜面を選んだ。**
造り手の言葉で『**looking beyond the valley floor towards the steep, rugged hillsides of Pritchard Hill**』です。
**1968 年に建った蔵は抽象画家 Ed Moses の設計でピラミッド型。**
**いまも Chappellet 家の所有で、CEO は長男の Cyril、COO は弟の Dominic。
醸造は 1990 年から Phillip Corallo-Titus が率いています。**」

**② `Signature` も `Pritchard Hill` も、蔵が自分で意味を決めた「designation」である。**
「🔴 **`Signature` は 1980 年に生まれました。Donn Chappellet がその年のできが良すぎたので、
"自分の保証" として**ボトルに直筆でサインした**んです。次に Signature を名乗らせたのは 1984 年で、
このとき『**最も良いロットを選んで組み立てる**』常設のワインにすると決めた。以来これが蔵の看板（flagship）です。**
🔴 **`Pritchard Hill` のほうは 1997 年。カルトワインの時代に、"この土地が出せる最高のもの" を
小ロットで別に瓶詰めすると決めて生まれたワインです。**
**つまり片方は "選抜の思想" の名前、もう片方は "場所そのもの" の名前です。**」

**③ 3 本の中身は、数字ではっきり違う。**
「🔴 **2021 の Signature（$280）は 79% カベルネ・ソーヴィニヨンに、プティ・ヴェルド 8%、マルベック 7%、メルロー 6%。
アルコール 14.7%、2023 年 6 月瓶詰め。年は記録的に乾いた冬で、熱波が一度も来ず、粒も房も非常に小さかった少量の年です。**
🔴 **2022 の Signature（同じ $280）は 82% カベルネに、プティ・ヴェルド 9%、マルベック 7%、メルロー 2%。
14.9%、2024 年 6 月瓶詰め。冬は雨が多く貯水池が満ちた年で、レイバーデーの頃に熱波が来たのを区画ごとに凌いだ年。**
🔴 **2022 の Pritchard Hill（$940）は 94% カベルネと 6% プティ・ヴェルドだけ。14.8%。
**22 か月、100% 新樽のフレンチオーク**で寝かせて 2024 年 7 月に瓶詰め。造り手は『ポートフォリオの頂点』と呼びます。**」

### 追加で使える一手（**すべて公式一次資料**）

- 🔴 **畑の数字**：「**山の地所は 640 エーカーありますが、植えてあるのは 104 エーカー、16% だけです。
  残りは森と草地のまま残していて、造り手はそれを『畑を守る自然の緩衝帯』と説明しています。
  104 エーカーのうち 85 エーカーがカベルネ・ソーヴィニヨン。標高は 800 から 1,800 フィート。
  区画は 47 とも 48 とも書かれていて、そのうち 40 区画がカベルネです。**」
- 🔴 **土壌**：「**4 百万年前、いまのナパ東側の山地に標高 14,000 フィートの火山があった。
  その火山灰が浸食されて残ったのが Pritchard Hill の薄い火山性土壌です。
  造り手は土壌名まで公表していて、`Sobrante loam` と `Hambright rock outcrop` が深さを変えて分布しています。**」
- 🔴 **2 年の対比**：「**2021 は "one of the driest winters on record"。熱波がゼロで、乾きのせいで
  粒も房も小さく、収量は少ないが凝縮した年。2022 は逆に冬の雨が潤沢で貯水池が満ちた年で、
  100°F を超える日が一度も無いまま来て、レイバーデー近くに一度だけ大きな熱波が来た。
  造り手はそれを『区画ごとに（block-by-block）』灌漑とキャノピー管理で凌いだと書いています。**」
- 🔴 **建築**：「**1968 年に建ったピラミッド型の蔵は抽象画家 Ed Moses の設計です。
  Hugh Johnson が『the most remarkable wine cathedral of the modern world』と呼びました
  —— これは第三者の評ですが、蔵自身が引用しています。2012 年にその隣に barrel chai を建て、
  太陽光パネルを載せました。**」
- ⚠️ **蔵出しとの差**：「**蔵の直販価格は Signature が $95、Pritchard Hill が $325 です。**」
  （**数字を出す必要がある場面だけ。倍率は言わない**）

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／第三者の主張にすぎない**）

1. 🔴 ⚠️ **『Pritchard Hill は AVA です』『ナパのサブアペラシオンです』と言わない。**
   🏛 **27 CFR Part 9 の全 288 セクションに `Pritchard` は 1 件も存在しない。**
   **ラベルの産地表示は `NAPA VALLEY`（§ 9.23）である。造り手自身も `AVA` / `appellation` の語を一度も使っていない。**
   **言ってよいのは「Pritchard Hill という山の名で、法定の産地区分ではありません」まで。**
2. 🔴 ⚠️ **逆に『Pritchard Hill は単なるキュヴェ名です』とも言わない。**
   **実在の地名であり、蔵の公式アクセス案内が山の入口の郵便受けに『Pritchard Hill』と書いてあると明記している。
   キュヴェ名でもあり地名でもある、が正解である。**
3. 🔴 ⚠️ **『ラベルに Signature と書いてあります』と言わない。**
   **フロントラベルにあるのは Donn Chappellet の金色の直筆サインそのもので、`Signature` という語ではない。
   「造り手の公式な製品名が Signature Cabernet Sauvignon で、ラベルには創業者の署名が入っています」が正しい言い方。**
4. 🔴 ⚠️ **『2021 年産・2022 年産は有機認証のブドウです』と言わない。**
   **蔵は「2012 年に CCOF の 3 年の認証プロセスを終え、いま有機認証を受けている」と現在形で書いているだけで、
   証書も証書番号も公開していない。🏛 USDA Organic INTEGRITY は JS シェルでゲート、CCOF の会員名簿は `404`。
   本調査は 2021 / 2022 収穫時点の有効性を示す一次文書を 1 件も持っていない。
   言ってよいのは「造り手は 2012 年に CCOF の有機認証を取得したと公表しています」まで。**
5. 🔴 ⚠️ **『Signature は 100% 自社畑（エステート）です』と言わない。**
   **蔵が公表する 104 エーカーの品種内訳には Merlot が入っていない。しかし Signature には
   2021 年で 6%、2022 年で 2% の Merlot が入る。ラベルの生産表示も
   `PRODUCED AND BOTTLED BY`（＝ `GROWN, PRODUCED AND BOTTLED BY` ではない）である。**
6. 🔴 ⚠️ **『Estate Bottled（エステート・ボトルド）です』と言わない。**
   🏛 **`Estate bottled` は 27 CFR § 4.26 の法定用語である。**
   **本調査で読めたフロントラベルにあるのは `PRODUCED AND BOTTLED BY CHAPPELLET VINEYARD` のみで、
   `ESTATE BOTTLED` の 2 語は無い。裏ラベルは未取得、TTB COLA は CAPTCHA でゲートされていた。どちらとも言わない。**
7. 🔴 ⚠️ **『Signature は◯十年続く看板です』と年数で言わない。**
   **蔵の資料が 3 通りに割れている（`more than three decades` / `well over three decades` / `more than five decades`）。
   蔵自身の年表では最初の Signature は 1980 年である。「1980 年に始まりました」と年で言う。**
8. 🔴 ⚠️ **`Signature` の新樽比率・熟成月数を言わない。**
   **2021・2022 とも蔵は公表していない。`22 か月・100% 新樽フレンチオーク` は `Pritchard Hill` の数字であって
   `Signature` の数字ではない。3 本を一括りにしない。**
9. 🔴 ⚠️ **Pritchard Hill の名前をめぐる争いの話をしない。**
   **公的に文書化された記録を本調査は 1 件も持っていない（🏛 USPTO の検索は SPA で API が `405`）。
   蔵の公式サイトにも商標・係争の記述は無い。「Chappellet は Pritchard Hill を代表する蔵のひとつです」までにとどめる。**
10. 🔴 ⚠️ **『ほぼ全部カベルネ・ソーヴィニヨンです』と Signature について言わない。**
    **2021 年は 79%、2022 年は 82%。🏛 27 CFR § 4.23(b) の下限 75% に近い。残りはプティ・ヴェルド、マルベック、メルロー。**
    **94% のカベルネは `Pritchard Hill` のほうである。**
11. 🔴 ⚠️ **2022 Signature の収穫終了日を具体的に言わない。**
    **同じ公式 PDF の中で統計欄が `Oct. 20`、本文が `concluded on October 17` と食い違っている。
    「9 月に始まり 10 月まで続いた」までにとどめる。**
12. ⚠️ **EC 商品ページに載っている「Growing Season」の説明を 2021 / 2022 の話として引用しない。**
    **2022 Signature の商品ページの同欄は 2020 年を、2022 Pritchard Hill の同欄は 2019 年を説明している。
    per-vintage の事実は wine notes PDF から取る。**
13. ⚠️ **第三者の点数・評語を蔵の説明として使わない。**
    **『100 points from Robert Parker』『Napa's Grand Cru』『Napa Valley's Rodeo Drive』
    『the most remarkable wine cathedral of the modern world』はいずれも第三者の言葉である。
    蔵はそれを引用しているだけで、本書は事実の典拠として採用していない。**
14. ⚠️ **区画数・クローン数・巣箱の数を断定しない。**
    **区画は 47 とも 48 とも、カベルネのクローンは 9 とも 10 とも、巣箱は 10 とも 30 とも、
    公式資料の中で割れている。**
15. ⚠️ **『Chappellet が Pritchard Hill で唯一の生産者です』と言わない。**
    **蔵もそうは書いていない（「helped to establish Pritchard Hill as… region」）。
    THÉSEUS の canonical 自身が別の生産者に `Napa Valley — Pritchard Hill` を持っている。**
16. ⚠️ **`Signature` を生産者抜きで語らない。**
    **同じメニューの中に `Darioush` の `'Signature,'` が 3 行ある。`Signature` は複数の蔵がそれぞれ
    自分の designation として使う語である。**

---

## Akio's Insight

🖋 （この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **canonical（`migration/`）も `research/canonical_conflicts/REGISTER.md` も一切変更していない。**
🔒 **以下はすべて escalate であり、実行はしていない。新しい番号も開いていない。**

---

### 🔴 ① **gap —— 3 行に対して canonical レコードは 0 件（`CDX-23`・Abreu 先例）**

1. **衝突する canonical ID**: 🔴 **無い（これは衝突ではなく不在である）。**
2. **証拠**: 🔍 **canonical 全 928 レコードを機械走査した。**
   - **`producer` フィールドが `Chappellet`（および `Chappellet` を含む任意の値）のレコード: **0 件****
   - **レコード全体（全フィールドを JSON 化して）に文字列 `Chappellet` / `chappellet` を含むレコード: **0 件****
   - **文字列 `Pritchard Hill` / `Pritchard`: **1 件**（`continuum` —— 生産者 `Continuum Estate`、`subregion = 'Napa Valley — Pritchard Hill'`）**
   - **文字列 `Signature`: **10 件**（Lafite / Margaux / La Lagune / Graillot / Chavost / Caymus / Shafer / Frog's Leap / Trimbach / Jean Velut）。**
     🔴 **いずれも本生産者とは無関係で、`Signature` は説明文中の普通名詞として現れているにすぎない。キュヴェ名としての `Signature` は canonical に 0 件**
3. **intake 側の記録は正しい**: 🔍 **3 行とも `producer_state: unresolved`、evidence は
   `canonical 384 生産者に一致・別名・近似いずれも無し: 'Chappellet'`。**
   🔴 **matcher は正しく「無い」と言っている。ここに defect は無い。**
4. **OBP への影響**: 🔴 **$280 × 2 ＋ $940 ＝ $1,500 分の 3 行が canonical から完全に見えない。**
5. **推奨する解決（実行しない）**: 🔒 **`CDX-23` の扱いに従う。純粋な gap であり `unreachable` ではない。
   生産者側には公式製品頁・ラベル画像・per-vintage 技術資料が完備しており、到達不能な要素は無い。**
6. **Confidence**: 🔴 **High**（機械走査＋公式一次資料の両方向で確定）

---

### ⚠️ ② **canonical は `Pritchard Hill` を `subregion`（＝産地の階層）として保持している**

1. **該当 canonical ID**: 🔍 **`continuum`**（生産者 `Continuum Estate`、`subregion = 'Napa Valley — Pritchard Hill'`）
2. **問題**: 🏛 🔴 **`Pritchard Hill` は 27 CFR Part 9 に存在しない。AVA ではない。**
   **canonical の `subregion` が AVA 階層を表す想定であるなら、この値は法定の産地区分ではないものを
   産地階層に置いていることになる。**
   ⚠️ **もし `subregion` が「通称を含む地理的表示」を許す設計であるなら問題ではない。設計意図が本書からは判別できない。**
3. **本生産者への波及**: 🔴 **Chappellet を canonical に昇格させるとき、行 3 の `Pritchard Hill` を
   `name`（キュヴェ名）に置くのか `subregion`（産地）に置くのかで、既存の `continuum` と整合が取れなくなる。**
   🔴 **本生産者では `Pritchard Hill` は同時に両方である。**
4. **族**: ⚠️ **`CDX-16`（属性の出所／属性の意味づけ）と同型。新番号は開かない。**
5. **Confidence**: 🔴 **High**（canonical の実値と 🏛 CFR の双方を実測）

---

### ⚠️ ③ **既存の族に該当するもの・および本バッチの新規観察（各 1 行。深追いしない）**

- ⚠️ **`CDX-15` は成立しない** —— 🔴 **行 1・2 の `_parts.label = "Signature"` は、蔵が 1980 年に始め 1984 年に
  常設化した designation であって、メニュー側のカテゴリー語ではない。**
  🔴 **`NEXT_ACTIONS.md` §3f-10（パターンの存在は個々の行の証拠ではない）が Ridge に続いて再び当たった事例として記録する。**
- ⚠️ **`CDX-5` の逆** —— 🔍 **本生産者では canonical に値そのものが無いため、格納値と公式の矛盾は発生しない。
  `CDX-5` が base rate であることの裏返しとして、gap のほうがむしろ「嘘をつかない」状態である。**
- 🔴 **新規観察 A（生産者側のデータ品質）** —— ✅ **蔵の EC 商品ページのメタデータがヴィンテージ的に腐っている。
  2022 Signature の `Growing Season` 欄は 2020 年を、2022 Pritchard Hill の同欄は 2019 年を説明し、
  引用レビューも 2019 年のものである。商品ページを scrape するパイプラインは誤ヴィンテージの記述を取り込む。
  per-vintage の真値は wine notes PDF 側にある。**
- 🔴 **新規観察 B（matcher 設計）** —— 🔍 **`Signature` は同一 OBP ファイル内で 2 生産者（`Chappellet` 3 行のうち 2 行、
  `Darioush` 3 行）が front-label designation として使う語である。
  label token の一致は必ず producer scope 内で評価する必要がある。**
- ⚠️ **`CDX-9`（生産者名の部分一致）は本件では発火しない** —— 🔍 **canonical・OBP のいずれでも
  文字列 `Chappellet` は本生産者以外に 1 件も現れない。**
  🔴 **本書は `producer` フィールドの完全一致で判定し、`D-2026-08-05-08` に従って
  家族名の部分一致による同定は一切行っていない。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY / `D-2026-08-05-09`**）

🔴 **本ブリーフは候補ドメインを名指ししていない。以下は本調査が自力で特定し、検証した結果である。**

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の運営者名** | ✅ 🔴 **合格。**`https://chappellet.com/terms-of-use/` 冒頭に「**Welcome to the Chappellet Winery website (the “Site”). The Site is owned by Chappellet Winery, Inc.**」と明記 |
| **(b) 非関連の免責表示が無い** | ✅ **合格。**「ファンサイト」「非公式」の類の表記は無い。**全ページ末尾は `© Chappellet 2026`**。制作者クレジット `An Affinity Site`（`affinitycreative.com`）が付くが、これは制作会社であって運営者ではない |
| **(c) 公的資料と一致する所在** | ⚠️ 🔴 **部分合格。**<br>✅ **生産者自身の 3 経路が一致する：①ラベルの生産表示 `CHAPPELLET VINEYARD, ST. HELENA, CA U.S.A.` ②公式アクセス案内 `Chappellet Vineyard and Winery, 1581 Sage Canyon Road, St. Helena, CA 94574` ③サイト内予約頁 `1581 Sage Canyon Rd, St Helena, CA 94574`。**<br>🏛 ⚠️ **公的登録簿との突合は取れていない。California SOS bizfile が Incapsula で `403`、TTB COLA が CAPTCHA。ラベル上の連邦醸造所番号 `B.W. 4337` は読めているが、これを照合できる公開登録簿には本調査で到達していない** |
| **(d) 商業・法務フッターの整合** | ✅ **合格。**`Terms of Use` / `Privacy Policy` / `Shipping Compliance`（発行可能 40 州超の一覧つき）/ `Careers` / `Reservations` / `Trade & Media` が揃う。**実在する EC（Commerce7 テナント `chappellet-winery`、384 プロダクト）、会員ログイン、責任飲酒団体 `responsibility.org` へのリンクあり**<br>⚠️ **`Terms of Use` の `Last Updated` が `October 1, 2012` と古い。`Privacy Policy` には制定日が無い** |
| 🏛 **ドメイン登録** | 🏛 **合格。**Verisign RDAP：`CHAPPELLET.COM` / 登録 `1995-12-14` / 満了 `2027-12-13` / 最終更新 `2025-12-14`。**30 年超の継続登録であり、なりすまし用の新規ドメインではない** |
| **年齢ゲート** | ✅ **サイト全体に「Are you over 21 years old?」の自己申告ゲートがあるが、静的取得は妨げられなかった**（`robots.txt` / sitemap / 頁 / PDF / 画像すべて直接取得できた）。**これは bot チャレンジではない** |
| **bot 検出の兆候** | **`chappellet.com` 側では無し。**CAPTCHA・チャレンジには一度も遭遇していない<br>⚠️ **ただし断続的に TLS ハンドシェイク失敗（`tlsv1 alert internal error`）が起きたため、全取得にリトライを入れている。これは bot 防御ではなくネットワーク／TLS 側の事象である** |

🔴 **本調査で `NOT_THE_PRODUCER_*` として退けたサイトは無い。**
（**WebSearch は一切使用していない。ドメインは `robots.txt` → `sitemap_index.xml` から自力で構造を確定した。**
**Wikipedia・メディア・小売・オークション・評論家サイトは 1 件も開いていない。**）
🔴 **生産者ドメイン外の資料は本書では 1 件も事実の典拠に使っていない（`📄` 0 件、`IMPORTER_*` 0 件）。**
⚠️ 🔴 **1 点だけ transport の断りを入れる：EC カタログ本文は `api.commerce7.com`（テナント `chappellet-winery`）から
取得している。配信元は生産者ドメイン外だが、内容は生産者が自社ストアに入稿した自社カタログであり、
`chappellet.com/shop/` が同じテナント設定でこれを描画している（`c7wp_settings.tenant = "chappellet-winery"` を実読）。**
🔴 **本書は EC カタログを ①製品系列の網羅 ②公式製品名 ③蔵出し価格 ④技術資料 PDF の所在 の 4 点にのみ使い、
per-vintage の技術データはすべて公式 PDF 側から取っている。**

### 一次資料（**`chappellet.com` および同ドメイン配信の公式 PDF・公式画像**）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt` → `sitemap_index.xml`** | **子サイトマップ 6 本。WordPress + Yoast SEO 構成。**⚠️ **`wines-sitemap.xml` は `lastmod 2022-06-15` で URL 2 本（`/wine/` と `/wine/test/`）しか無く、実質空。ワインの実体は EC 側にある** |
| **`page-sitemap.xml`（108 URL）/ `assets-sitemap.xml`（62）/ `press-sitemap.xml`（25）/ `trades-sitemap.xml`（69）** | **サイト全体の構造、プレスキットの所在、資産（tech sheet / bottle shot / shelf talker）の所在を機械的に確定** |
| 🔴 **公式 wine notes PDF `2022-Signature-Cabernet-Sauvignon-Wine-Notes.pdf`** | 🔴 **OBP 行 1。**82/9/7/2・14.9%・Brix 24.5–27.0°・TA 0.57・pH 3.72・収穫 9/7–10/20（本文は 10/17）・瓶詰 2024/6・Winemaker `Phillip Corallo-Titus`・住所 `PRITCHARD HILL, ST. HELENA, CA 94574` |
| 🔴 **公式 wine notes PDF `2021-Signature-Cabernet-Sauvignon-Wine-Notes.pdf`** | 🔴 **OBP 行 2。**79/8/7/6・14.7%・Brix 24.5–27.0°・TA 0.57・pH 3.69・収穫 9/9–10/20・瓶詰 2023/6・電話 `707-963-7136`（旧番号） |
| 🔴 **公式 wine notes PDF `2022-Pritchard-Hill-Cabernet-Sauvignon.pdf`** | 🔴 **OBP 行 3。**94/6・14.8%・Brix 25.0–27.0°・TA 0.60・pH 3.71・収穫 9/7–10/18・瓶詰 2024/7・**22 か月 100% 新樽フレンチオーク**・`VP of Winemaking Phillip Corallo-Titus` ＋ `Winemaker Ry Richards` |
| 🔴 **公式 PDF `2021-Pritchard-Hill-Cabernet-Sauvignon-Tasting-Notes-1.pdf`** | **比較用（OBP 外）。**95/5・14.8%・TA 0.56・pH 3.74・収穫 9/10–10/11・瓶詰 2023/7・**22 か月 100% 新樽フレンチオーク** |
| 🔴 **公式トレード資料 `Signature-Cabernet-Sauvignon-Trade-Sales-Sheet-V-97pts.pdf`（2026-02 掲載）** | 🔴 **`Signature` designation の由来：「**Donn Chappellet signed the bottle of the 1980 vintage, as a promise of quality, creating the first “Signature” Cabernet Sauvignon.**」**／🔴 **「**Sourced from many of the lower elevation plots on Pritchard Hill starting at 800 feet**」**／`VP of Winemaking Phillip Corallo-Titus` ＋ `Winemaker Ry Richards`<br>⚠️ **同資料に並ぶ点数はすべて第三者媒体のもの。本書は採用していない** |
| 🔴 **公式ボトルショット `sig_cab-bottle-scaled.jpg`** | 🔴 **フロントラベル実読。**`CHAPPELLET` ＋三角ロゴ／**Donn Chappellet の金色の直筆サイン**／`Napa Valley`／`Cabernet Sauvignon`／`PRODUCED AND BOTTLED BY CHAPPELLET VINEYARD, ST. HELENA, CA U.S.A.`／`B.W. 4337`／`ALC. 14.5% BY VOL`<br>⚠️ **ヴィンテージ表示なし。汎用画像である** |
| 🔴 **公式ボトルショット `pritchard_hill-bottle-scaled.jpg`** | 🔴 **フロントラベル実読。**縦組み `CHAPPELLET`／**`Pritchard Hill`（赤い筆記体）**／`NAPA VALLEY`／`CABERNET SAUVIGNON`／三角ロゴ<br>⚠️ **ヴィンテージ・アルコール・生産表示は読めない。汎用画像である** |
| ✅ **`/our-story/`（A Family Story）** | **1967 創業／1968 ピラミッド着工・Mondavi が初破砕／1969 初商業カベルネ／🔴 **1980・1984 の `Signature` 定義**／🔴 **1997 の `Pritchard Hill` 定義**／2012 barrel chai／2016 Hideaway／役員・チーム一覧（21 名）／Donn・Molly の詳細略歴 |
| ✅ **`/pritchard-hill/`** | **標高 800–1,800 ft／48 区画／Cyril の言葉／2000–2021 の replanting（`Wells Ranch`・`Hideaway` 区画）／2012 CCOF／2012 barrel chai／2020 小型タンク／Phillip・Ry・Andrew の紹介** |
| ✅ **`/land-stewardship/`** | 🔴 **有機（2012 CCOF・104 エーカー・3 年プロセス）／太陽光（2008・960 モジュール）／水処理（2011）／640 エーカーの 16% のみ植栽／堆肥 100 トン／巣箱／カバークロップ** |
| ✅ **プレスキット PDF `The-Chappellet-Story-9-23-2024.pdf`** | **蔵の自己紹介の正典。第 2 世代（Cyril / Carissa / Dominic ＋ Lygia / Alexa）、47 区画、Grower Collection（2019〜）** |
| ✅ **プレスキット PDF `Chappellet-Estate-Vineyard-9-23-2024.pdf`** | 🔴 **畑の正典。**標高 800–1,800 ft／4 百万年前の 14,000 ft の火山／**`Sobrante loam` と `Hambright rock outcrop`**／47 区画（うちカベルネ 40）／10 クローン／**104 / 640 エーカー、カベルネ 85 エーカー、残りは Malbec・Cabernet Franc・Petit Verdot・Chenin Blanc**／2012 CCOF |
| ✅ **プレスキット PDF `Chappellet-Green-Practices-9-19-2024.pdf`** | **2012 CCOF ＋ `Fish Friendly Farming`／太陽光の詳細数値／水処理／巣箱 30／羊と山羊による shaded fuel break 15 エーカー超／UC Davis・Cal Poly Humboldt との共同研究** |
| ✅ **プレスキット PDF `3-Chappellet-Winemaking-Philosophy.pdf`** | **1967 の目的（ボルドー第一級）／谷底ではなく丘を選んだこと／48 区画／区画別発酵・熟成／**elite French coopers and forests**** |
| ✅ **プレスキット PDF（略歴 6 点）** | **`Cyril`（CEO & Chairman、1988 復帰）／`Dominic`（Co-owner & COO、2023 就任、1999 復帰）／`Phillip Corallo-Titus`（VP of Winemaking、1981 入社・1990 復帰）／`Ry Richards`（Winemaker、2006 入社・2023 昇格）／`Andrew Opatz`（Director of Vineyard Operations、2008 入社、有機認証プログラム担当、Dave Pirio は 2023 退任）／`David Francke`（President）** |
| 🔴 **公式アクセス案内 `WineryDirections2026-scaled.jpg`** | 🔴 **`Chappellet Vineyard and Winery, 1581 Sage Canyon Road, St. Helena, CA 94574 / 707-286-4219`**／🔴 **「a row of silver mailboxes on the left labeled **“Pritchard Hill”**」**／Lake Hennessey・Hwy 128 からの経路 |
| ✅ **`/terms-of-use/` / `/privacy-policy/` / `/contact/` / `/shipping/`** | **真正性の検証。運営法人名 `Chappellet Winery, Inc.`、連絡先 5 系統、発送可能州の一覧** |
| ✅ **`/pritchard-hill-estate-allocation/` / `/signature-retrospecitve/` / `/collectors-library/`** | **`Pritchard Hill` と `Hideaway` の配分制／`Signature` を「our flagship wine」と呼ぶ／Collector's Library の 4 系列（PRITCHARD HILL / hideaway / signature / cab franc）** |
| 🔴 **EC カタログ（Commerce7、テナント `chappellet-winery`、8 頁・384 プロダクト）** | 🔴 **公式製品名・蔵出し価格（Signature $95.00 / Pritchard Hill $325.00）・技術資料 PDF の URL・製品系列の網羅**<br>⚠️ **商品本文のメタデータはヴィンテージ的に腐っている（→ §Canonical Conflict ③）。本書は per-vintage の事実に使っていない** |

### 🏛 公的登録簿・規制一次資料

| 資料 | 取得した情報 |
|---|---|
| 🔴 🏛 **eCFR title-27 構造 API（`/api/versioner/v1/structure/2026-08-01/title-27.json`）** | 🔴 **Part 9 の全 288 セクションを機械列挙。`Pritchard` は 0 件。`Napa` を含むのは `§ 9.23` / `§ 9.161` / `§ 9.296` の 3 件のみ。**<br>🔴 **これが「Pritchard Hill は AVA ではない」の根拠であり、節番号を推測せず機械的に確定している** |
| 🏛 **eCFR 27 CFR § 9.23（`Napa Valley`）** | **AVA の名称規定、承認地形図 8 葉＋Napa 郡税務評価図、境界の全記述、「located within Napa County, California」、制定 `T.D. ATF-79, 46 FR 9063, Jan. 28, 1981`（1985 改正）** |
| 🔴 🏛 **eCFR 27 CFR § 4.23（`Varietal (grape type) labeling`）** | 🔴 **(b) 単一品種表示の 75% 要件の全文、(a) appellation of origin の併記義務、(d) 複数品種表示の要件** |
| 🔴 🏛 **eCFR 27 CFR § 4.39（`Prohibited practices`）** | 🔴 **(i) Geographic brand names の全文、(i)(3) `viticultural significance` の定義、(j) Product names of geographical significance、(m) 畑・農場名を使う場合の 95% 要件** |
| 🏛 **eCFR 27 CFR § 4.25（`Appellations of origin`）** | **appellation of origin の定義（(a)(1)(vi) に viticultural area）、(b)(1) の 75% 要件、(e) AVA の petition 手続への参照** |
| 🏛 **Verisign RDAP（`rdap.verisign.com/com/v1/domain/CHAPPELLET.COM`）** | **登録 1995-12-14 / 満了 2027-12-13 / 最終更新 2025-12-14 / NS `PDNS07-08.DOMAINCONTROL.COM`** |

### 取得できなかったもの / 読めなかったもの

- 🔴 ⚠️ **🏛 TTB Public COLA Registry が CAPTCHA でゲートされていた。**
  **`https://ttbonline.gov/colasonline/publicSearchColasBasic.do` は F5/Shape 系 bot 防御（`bobcmn` / `TSPD_101`）を返し、
  ページ内に `captcha_audio` が実在した。突破は試みていない。**
  → **本書は TTB 承認ラベルの記録（brand name / fanciful name / class-type / 表示産地 / 承認日）を 1 件も持たない。**
  → 🔴 **これが本ドシエで最も惜しい欠落である。COLA が開けば `Pritchard Hill` が TTB 上どう分類されているか
  （fanciful name か / viticultural significance を認められているか）に直接の答えが出る。**
  → **⚠️ ゲートは「記録が存在しない」ことの証拠ではない。**
- 🔴 ⚠️ **🏛 California Secretary of State（`bizfileonline.sos.ca.gov`）が Incapsula で `403`。**
  **`Chappellet Winery, Inc.` の登記番号・登記日・現況・登記住所を確認できていない。**
  → **蔵が自分を 3 通りに名乗る（`Chappellet Winery, Inc.` / `Chappellet Vineyard` / `Chappellet Vineyard and Winery`）
  問題を解けていない。**
- 🔴 ⚠️ **🏛 USDA Organic INTEGRITY データベースは読めなかった。**
  `https://organic.ams.usda.gov/integrity/` は Blazor の JS シェルのみを返し、
  `POST /integrity/api/OperationSearch` と `POST /integrity/api/Operations/Search` はいずれも `400`。
  **（Batch 9・10・Ridge と同じ所見が再現した。）**
  → 🔴 **本生産者では、Ridge と違って蔵が証書を配信していないため、これが実害になっている。**
- ⚠️ **認証機関 `CCOF` 側の会員ディレクトリに到達できなかった。**`/members/` も `/directory/` も `404`。
- ⚠️ **🏛 USPTO の商標登録簿を機械的に読めなかった。**
  `tmsearch.uspto.gov` は Angular の SPA で、試した 4 つの API 経路（`api-v1-0-0/tmsearch`、`api/v1/tmsearch`、
  `api-v1-0-0/tmsearch/select`、`api/search`）はすべて S3 の `405 MethodNotAllowed` を返した。
  `assignment-api.uspto.gov` は DNS 解決不能。
  → 🔴 **`Pritchard Hill` の商標上の身分を確認できていない。本書は命名の争いについて何も述べない。**
- 🔴 **裏ラベル画像を 1 枚も取得できていない。**
  **政府警告文、`ESTATE BOTTLED` の有無、亜硫酸表示、生産量、ヴィンテージ表示の位置が未確認。**
- 🔴 **2021 / 2022 の現物ラベル画像が無い。**
  **蔵が配信するボトルショットは 2 本ともヴィンテージ表示のない汎用画像で、Signature の `ALC. 14.5%` は
  2021（14.7%）とも 2022（14.9%）とも一致しない。**
- ⚠️ **`Signature` の樽構成・熟成月数が 2021・2022 とも公表されていない。**
- ⚠️ **`Signature` の Merlot の出所が公表されていない**（蔵の 104 エーカーの品種内訳に Merlot が無い）。
- ⚠️ **`Pritchard Hill` キュヴェの由来区画・生産本数が公表されていない。**
- ⚠️ **`Fish Friendly Farming` の認証番号・発効日・対象範囲を示す一次文書を取得していない。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical: `migration/out/export/db_wine_canonical.json`（928 レコード）を機械走査。
`producer == 'Chappellet'` は 0 件。レコード全文への部分一致でも `Chappellet` は 0 件。**
🔍 **`Pritchard Hill` / `Pritchard` は 1 件（`continuum` の `subregion`）。`Signature` は 10 件だがすべて無関係の普通名詞。**
🔍 **⚠️ 家族名の部分一致は使っていない（`D-2026-08-05-08` / `CDX-9`）。**
🔍 **OBP: `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）に 3 行。
`source_row_id` = `obp-beverage-2026-08:21beac6c98` / `:34ffe95190` / `:e727ecdf8d`。
3 行すべて `match_state` / `producer_state` / `cuvee_state` / `vintage_state` が `unresolved`・`confidence = 0.0`・
`source_quality_flags = []`・`_collision_risk = LOW`・`proposed_canonical_*` はすべて `null`。**
🔍 **⚠️ 同ファイル内で `Signature` を含む別生産者の行が 3 件ある：`Darioush` の
`'Signature,' Napa Valley Cabernet Sauvignon`（2022）/ `Chardonnay`（2023）/ `Merlot`（2023）。本書とは無関係である。**
🔍 **⚠️ `Pritchard` を含む OBP 行は本生産者の 1 行のみである。**
⚠️ **本書の件数はすべて `obp_intake_normalized_20260804.json` から取ったものであり、
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
| **Identity** | 🔴 **Medium-High** | ✅ **法人名が Terms of Use で明示（`Chappellet Winery, Inc.`）。所在が公式アクセス案内・予約頁・ラベル生産表示の 3 経路で一致。役員・醸造チームの氏名と就任年がプレスキット PDF で確定**<br>⚠️ 🔴 **公的登録簿との突合が 0 件（California SOS が `403`）。蔵が 3 通りに名乗る問題が未解決のため High には上げない** |
| **Overview** | **High** | **蔵の自己規定（mountain-grown / hillside Cabernet / Pritchard Hill）がすべて公式の言葉で取れた** |
| 🔴 **History** | 🔴 **High** | 🔴 **1931 / 1966 / 1967 / 1968 / 1969 / **1980・1984（Signature の定義）** / **1997（Pritchard Hill の定義）** / 2008 / 2011 / 2012 / 2016 / 2019 / 2023 がすべて公式頁または公式 PDF で確定**<br>⚠️ **「禁酒法廃止後 2 番目の新設ワイナリー」「NVV の 18 番目の会員」は生産者の主張として記録したのみ。「◯十年の看板」の記述割れも封じた** |
| 🔴 **Location** | 🔴 **High** | 🏛 **`Napa Valley` = 27 CFR § 9.23 で確定。**🔴 **`Pritchard Hill` が AVA でないことを Part 9 全 288 セクションの機械列挙で確定した（本ドシエ最強の検証）。**✅ **標高・面積・品種面積・土壌名・地質史がすべて公式で確定**<br>⚠️ **区画数（47/48）とクローン数（9/10）は公式資料内で割れており封じた。区画ごとの面積・植樹年・台木は不明** |
| ⚠️ **Farming** | ⚠️ **Medium** | ✅ **CCOF 有機認証（2012・104 エーカー・3 年プロセス）が 4 つの公式資料で一致し、栽培責任者の職責としても記述されている**<br>🔴 ⚠️ **しかし証書・証書番号・有効期間を 1 件も取得できていない。🏛 USDA INTEGRITY はゲート、CCOF 名簿は `404`、蔵は証書を出していない。**🔴 **2021 / 2022 収穫時点の有効性は言えない。**⚠️ **Signature の Merlot の出所も不明。本節が本ドシエで最も弱い** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **OBP 3 本すべてでセパージュ・アルコール・Brix・TA・pH・収穫期間・瓶詰月が公式 PDF で確定。🏛 § 4.23(b) の 75% 要件を 3 本とも個別に検証した。Pritchard Hill は樽（22 か月・100% 新樽フレンチ）も確定**<br>⚠️ 🔴 **`Signature` の樽が 2 年とも未公表。2022 Signature の収穫終了日に PDF 内矛盾があり封じた** |
| 🔴 **Style** | 🔴 **High** | 🔴 **3 本すべてに公式テイスティングノート。2021・2022 のヴィンテージノート（Growing Season & Harvest）も逐語で取得し、2 年の対比が造り手の言葉で言える**<br>⚠️ **EC 商品ページのノートは腐っており、使用していない** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **3 行すべてについて公式製品名・フロントラベル逐語・per-vintage 技術仕様・蔵出し価格が確定。**🔴 **さらに本節最大の論点 2 つ（`Signature` の身分、`Pritchard Hill` の身分）を、蔵自身の定義と 🏛 CFR の双方で決着させた**<br>⚠️ **ボトルショットが汎用画像であること、TTB COLA が未取得であることが残る** |
| **Canonical Conflict** | 🔴 **High** | 🔴 **gap は 928 レコードの機械走査で確定（`producer` 完全一致 0・部分一致 0）。`Pritchard Hill` が `continuum` の `subregion` にあることも実測** |
| **Staff Notes** | 🔴 **High** | ⚠️ **16 項目。🔴「Pritchard Hill は AVA」「Pritchard Hill は単なるキュヴェ名」「ラベルに Signature と書いてある」「2021/2022 は有機認証」「Signature は 100% エステート」「Estate Bottled」「Signature の樽」「ほぼ全部カベルネ」「命名の争い」の 9 つの誤りを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を明確に超過。実感としては 85% 前後）。** | **OBP 3 本すべてについて、公式製品名・ラベルの構造・セパージュ・分析値・収穫期間・瓶詰時期・造り手のノート・年の性格・畑・キュヴェ名の由来を言える。産地は連邦規則まで遡って言える。**<br>🔴 **`Pritchard Hill` の法的身分という本ドシエの中心問題は、推測ではなく 🏛 CFR の機械走査で決着した。**<br>🔴 **欠けているのは ① TTB COLA 記録 ② 有機認証の証書と 2021/2022 の射程 ③ 現物ラベル（表裏）④ Signature の樽 ⑤ 法人登記の照合。**<br>**②以外はいずれも「言わない」で回避でき、②も「造り手はこう公表しています」という言い方に落とせば卓上で嘘をつく経路は無い。** |

---

## Open Questions

1. 🔴 **OBP 3 本の現物ラベル（実ボトル案件）。**
   🔴 **蔵が配信するボトルショットは 2 本ともヴィンテージ表示のない汎用画像であり、Signature の画像の
   `ALC. 14.5%` は 2021（14.7%）とも 2022（14.9%）とも一致しない。**
   **確認すべき点：① ヴィンテージ表示の位置（表ラベルか、ネックラベルか）② `Signature` の語が実際にどこかに印字されているか
   ③ `ESTATE BOTTLED` の 2 語の有無 ④ Pritchard Hill の生産表示（`PRODUCED AND BOTTLED BY` か `GROWN, PRODUCED…` か）
   ⑤ 裏ラベルの記載事項一式。**
2. 🔴 **🏛 TTB COLA の再試行。**
   **本調査では CAPTCHA でゲートされた。開けば brand name / fanciful name / class-type / 表示産地 / 承認日が確定し、
   🔴 **`Pritchard Hill` が TTB 上どう扱われているか（fanciful name か、viticultural significance を認められた地名か）**
   に直接の答えが出る。本ドシエの中心問題の残り半分がここにある。**
   **⚠️ 同一バッチ内でも生産者によって開閉が変わるため、日を改めた再試行に価値がある。**
3. 🔴 **有機認証の証書と、2021 / 2022 収穫の射程。**
   **蔵は「2012 年に CCOF の認証を取得」と書くのみで、証書・番号・有効期間を出していない。
   🏛 USDA Organic INTEGRITY は Blazor シェル、CCOF 名簿は `404`。**
   → **蔵への直接照会（証書 PDF の提供依頼）が最短。**
4. 🔴 **`Signature` の樽構成と熟成期間（2021 / 2022）。**
   **蔵は `Pritchard Hill` については「22 か月・100% 新樽フレンチオーク」と公表しているのに、
   `Signature` については 2 年とも一切公表していない。造り手への照会案件。**
5. ⚠️ **法人の正式名称と登記。**
   **`Chappellet Winery, Inc.`（Terms of Use）／`Chappellet Vineyard`（ラベル生産表示）／
   `Chappellet Vineyard and Winery`（アクセス案内）の 3 つが並立する。
   🏛 California SOS が Incapsula で `403`、TTB の醸造所番号 `B.W. 4337` を照合できる公開登録簿にも到達していない。**
6. ⚠️ **`Signature` に使う Merlot の出所。**
   **蔵が公表する 104 エーカーの品種内訳（カベルネ 85、残りは Malbec / Cabernet Franc / Petit Verdot / Chenin Blanc）に
   Merlot が無いが、Signature には 2021 年 6%・2022 年 2% の Merlot が入る。買いブドウか、内訳の記載漏れか。**
7. ⚠️ **区画数・クローン数の公式値。**
   **47（プレスキット 2024-09）と 48（ウェブ・Winemaking Philosophy PDF）、
   カベルネ 9 クローン（ウェブ）と 10 クローン（Estate Vineyard PDF）が並立する。造り手への照会案件。**
8. ⚠️ **2022 Signature の収穫終了日の PDF 内矛盾。**
   **統計欄 `Oct. 20` と本文 `concluded on October 17` が食い違う。造り手への照会案件。**
9. 🔴 ⚠️ **canonical に載せるときの `Pritchard Hill` の置き場所。**
   🔴 **本生産者では `Pritchard Hill` は同時に ①キュヴェ名（`name`）②地名（`subregion`）である。
   canonical はすでに別生産者（`Continuum Estate`）で `subregion = 'Napa Valley — Pritchard Hill'` を採っている。
   同じ文字列が 2 つの階層に現れることをスキーマがどう扱うかを決めないと、行 3 は正しく昇格できない。**
   → 🔒 **設計判断であり本書では決めない。**
10. ⚠️ **`Signature` の producer scope 問題。**
    **同じメニューに `Darioush` の `'Signature,'` が 3 行ある。label token の一致を producer scope 内で
    評価する仕組みが無いと、2 蔵の designation が混線する。**
    → 🔒 **matcher の設計判断であり本書では決めない。**
