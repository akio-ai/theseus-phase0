# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件しか存在しない**（`chateau-montelena-estate`）。
> **928 レコードの export 全体を機械走査し、文字列 `Montelena` を含むレコードが 1 件であることを実測した。**
> **OBP は 4 行。すなわち本生産者はほぼ全面的に canonical の「欠落（gap）」である。**
> 🔒 **gap は conflict ではない。「レコードが存在しない」を扱う登録票クラスは存在しないため、
> 本書は無理に既存の族へ押し込まず、事実として記述するにとどめる。**
> **canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式資料で確認**（`montelena.com` 本体・同ドメイン配信の公式 PDF・公式ボトルショット画像）
> `🏛` **公的登録簿／規制一次資料** —— **27 CFR Part 9 / Part 4（eCFR 現行版）**、
>    **Federal Register 最終規則 `T.D. TTB-83`（`74 FR 64612`）**、**Napa Green 参加者名簿**
> `📄` **生産者著作だが生産者ドメイン外で配信されている資料**（本書では press release 1 点のみ。出所を明記して使用）
> `⚠️` **出典間で食い違い／出典が沈黙している／第三者の主張であって未確認**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://montelena.com/`**
> 走査元: **`robots.txt` → `sitemap_index.xml` → `page-sitemap.xml`（42 URL）/ `product-sitemap.xml`（54 URL）/
> `product_cat-sitemap.xml`（14 URL）**、および **WordPress REST API（`/wp-json/wp/v2/pages` = 46 頁が開いている）**、
> **WooCommerce Store API（`/wp-json/wc/store/v1/products`）**
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ① —— メニューの `"The Montelena Estate,"` は組版の産物ではない。ラベルに実在する文字列である。**
> **生産者自身が配信しているボトルショット画像（trade 用 `Straight On` 素材）を実読した結果、
> `Estate Cabernet Sauvignon` のラベルには最上部に金地の帯があり、そこに
> `THE MONTELENA ESTATE` と印字されている。2011 年ヴィンテージと 2021 年ヴィンテージの双方で同一。**
> 🔴 **一方、生産者自身の EC サイトは同じワインを `Estate Cabernet Sauvignon` と呼び、
> WooCommerce の商品名は `2011 Montelena Estate Cabernet Sauvignon`、
> テクニカルシートの見出しは `estate cabernet sauvignon` である。**
> → 🔴 **すなわち「メニューがカテゴリー語をキュヴェ名として印字してしまった」型ではない。
> むしろ OBP のほうがラベル表記に忠実であり、生産者自身の呼称のほうが 3 通りに揺れている。**
> **→ 依頼時に想定されていた反復パターン (a) は、本生産者では成立しない。§Important Cuvées で反証を示す。**
>
> 🔴 **本ドシエ最大の収穫 ② —— OBP 1・2 行目の `Napa Valley Chardonnay` / `Napa Valley Cabernet Sauvignon` も、
> 生産者の公式製品名そのものである。**
> **公式製品ページのタイトルが `2023 Napa Valley Chardonnay` / `2022 Napa Valley Cabernet Sauvignon`。
> ラベルは `2023 / Chardonnay / NAPA VALLEY`、`2022 / Cabernet Sauvignon / NAPA VALLEY`。**
> → **これも「産地＋品種を勝手にキュヴェ名にした」のではなく、造り手がその形で売っている。**
>
> 🔴 **本ドシエ最大の収穫 ③ —— canonical の `subregion = "Napa Valley — Calistoga"` は一次資料で裏づけが取れる。**
> **ラベル現物（公式画像）に `CALISTOGA · NAPA VALLEY` と 2 段で印字されている。**
> **Batch 9 で escalate された「属性の出所（attribute provenance）」の未採番シェイプは、本生産者では再発していない。**
> **裏づけが取れたことを明示的に記録する。**
>
> 🔴 **本ドシエ最大の収穫 ④ —— canonical の説明文は公式テクニカルシートと矛盾している。**
> **canonical: 「Calistoga自家畑から100% CS、新樽率を抑えた長熟型」**
> **公式: 2011 = `99% Cabernet Sauvignon, 1% Cabernet Franc`、2019 = `99% / 0.5% PV / 0.5% CF`、
> 2021 = `94.1% Cabernet Sauvignon, 4.9% Cabernet Franc, 1% Petit Verdot`。
> 2021 の樽は `22 Months, 100% French Oak, 45% New`。**
> → **「100% CS」も「新樽率を抑えた」も、3 ヴィンテージの公式シートに反する。** → §Canonical Conflict
>
> ⚠️ **調査上の制約 ① —— 🏛 TTB Public COLA Registry は本調査では CAPTCHA でゲートされていた。**
> **`publicSearchColasBasic.do` は F5/Shape 系の bot 防御 JS（`bobcmn` / TSPD）を返し、
> ページ内に captcha 画像・音声・`name="answer"` の入力欄が実在した。ルールに従い突破は試みていない。**
> **したがって本書は TTB 承認ラベルの記録（brand name / fanciful name / class-type / alcohol）を一件も持たない。**
> **⚠️ ゲートされたことは「ラベルが存在しない」ことの証拠ではない。**
> **代替として、生産者自身が trade 向けに配信しているボトルショット画像を label evidence として用いた。**
> **これは生産者の公表物であって連邦承認記録ではない。両者を混同しない。**
>
> ⚠️ **調査上の制約 ② —— `montelena.com` には沿革・畑・栽培・持続可能性のページが 1 枚も存在しない。**
> **WordPress の全 46 頁を REST API で列挙して確認した。存在するのは EC（Shop）、Visit、Membership、
> In the News（第三者記事の引用集）、Resources（trade downloads）、および法務ページだけである。**
> → 🔴 **したがって本ドシエの History と Farming は構造的に薄い。造り手自身の言葉が存在しないためである。**
> **これは調査の失敗ではなく、公式サイトの構成そのものである。**

---

## Identity

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Chateau Montelena`** |
| **公式表記** | ✅ **`Chateau Montelena`**（全ページのタイトル・ロゴ）／**ラベル上は `CHATEAU MONTELENA`** |
| 🔴 **法人／サイト運営者** | ✅ 🔴 **`Chateau Montelena Winery`**。<br>**Terms of Service 冒頭に「The website located at www.montelena.com (“Site”) is **owned by and operated by Chateau Montelena Winery**」と明記。**<br>**Copyright Agent 宛先も `Chateau Montelena Winery, 1429 Tubbs Lane, Calistoga, CA, 94515`。**<br>**全ページ末尾は `© 2026 Chateau Montelena Winery`** |
| 🔴 **所在** | ✅ 🔴 **`1429 Tubbs Lane, Calistoga, CA 94515`**／**`707.942.5105`**（**Fax `707.942.4221`**）<br>**サイトのフッター、全テクニカルシートの版面下部、全 bio PDF の下部で完全に一致している** |
| 🔴 **設立年** | ✅ 🔴 **1882 年。**ラベルに **`ESTABLISHED 1882`** と印字。**公式商品説明も「Founded in 1882, Chateau Montelena…」** |
| 🔴 **創業者** | 📄 🔴 **`Alfred L. Tubbs`**（**A.L. Tubbs**）。**生産者 press release（2025-03-18）**: 「**Since its founding in 1882 by Alfred L. Tubbs**」<br>⚠️ **`montelena.com` 本体にはこの名前が一度も出てこない。**（**所在地の `Tubbs Lane` がその名を留めている**） |
| 🔴 **現オーナー** | 📄 🔴 **Bo Barrett。**生産者 press release の会社紹介欄が「**Bo Barrett stands as current CEO & Owner**」と明記。**同文書は「reaffirms the winery's dedication to staying family-owned」とも書く**<br>✅ **公式 bio: 「Bo has been involved in every vintage at Montelena since his family assumed ownership in 1972」** |
| 🔴 **CEO** | ✅ 🔴 **`Bo Barrett`（Chief Executive Officer）。**公式 bio PDF：**Fresno State で Viticulture and Enology を修めながら毎秋 Montelena で収穫に従事、1982 年に winemaker に就任、2013 年に CEO に就任。** |
| 🔴 **President & Winemaker** | ✅ 🔴 **`Matthew Crafton`（Matt Crafton）。**公式 bio PDF：**ヴァージニア出身、2003 年に University of Virginia で経済学の学位、2008 年に UC Davis で Viticulture and Enology を修了。**<br>🔴 **同 2008 年に Montelena に Enologist として入社、2014 年に winemaker、2025 年 12 月に President に就任（役職は現在 2 つ兼任）** |
| **Director of National Sales** | ✅ **`Tucker Spear`**（`/resources/` に bio PDF あり） |
| 🔴 **創業家（前世代）** | ✅ 🔴 **`Jim Barrett`。**公式 bio が「**his father, and winery founder, Jim Barrett**」と記す（**「winery founder」は 1972 年の再興を指す表現であり、1882 年の設立者ではない。混同しないこと**） |
| 🔴 **認証（栽培）** | 🔴 ⚠️ **本調査で取得した公式ページ全 46 頁・テクニカルシート・bio・press release のどこにも
`organic` / `biodynamic` / `certified` / `CCOF` / `Demeter` / `Napa Green` / `Fish Friendly Farming` の語が一件も無い。**<br>🏛 **Napa Green の参加者名簿（server-rendered、社名 73 件を機械抽出）にも `Montelena` は現れない。** → §Farming |
| **canonical id** | 🔍 🔴 **`chateau-montelena-estate` の 1 件のみ**（`producer='Chateau Montelena'` / `name='Estate Cabernet Sauvignon'` / `vintage='—'` / `subregion='Napa Valley — Calistoga'` / `color='Rouge'` / `classification='Calistoga Cabernet Sauvignon'`） |
| 🔴 **米国内流通** | ✅ **州ごとの卸を `/resources/us-distributors/` に自ら掲出**（RNDC / Breakthru Beverage / Wilson Daniels Wholesale ほか）。**メーリングリスト専売ではなく、通常流通のある生産者である** |
| **直販** | ✅ **自社 EC＋会員制（`Estate` / `Friends of Montelena` / 単一品種会員）。San Francisco の Westin St. Francis 内に直営テイスティングルーム** |

---

## Overview

✅ **ナパ・ヴァレー最北、カリストガ。1882 年設立の石造りのシャトーを構える蔵で、
1972 年に Barrett 家が取得して現在の姿になった。**
🔴 ✅ **1976 年のパリの試飲会で 1973 年のシャルドネが勝ったことで世界に知られる。**
公式の言葉：「**Founded in 1882, Chateau Montelena reflects a distinctly American idea:
that legitimacy is earned through conviction, not inheritance.
That belief reached a global audience in 1976, when Montelena's 1973 Chardonnay prevailed at the Judgment of Paris,
a blind tasting that challenged centuries of convention and altered the course of fine wine history.**」

🔴 ✅ **公式が「flagship（旗艦）」と明示するのは、シャルドネではなく `Estate Cabernet Sauvignon` である。**
「**The flagship wine of the Montelena Estate**」（複数の商品カードの定型文）、
「**Membership in this program is the only way to guarantee access to our flagship wine, the Estate Cabernet Sauvignon.**」
→ 🔴 **卓上でよくある誤解（＝「シャルドネの蔵」）を、造り手自身の言葉で正せる。** → §Staff Notes

🔴 ✅ **蔵の自己規定は「畑と年」に置かれている。**
Matt Crafton の公式 bio：「**each vintage as raw material shaped by the specific site and season,
coaxing wines that express the Calistoga Estate's gravelly benches, volcanic soils and the unique characteristics
of the growing season — true wines of place that can't be replicated anywhere else in the world.**」

🔴 ✅ **2025 年 3 月、シャルドネの将来の本拠として Carneros に 73 エーカーの畑を取得した。**
📄 **「The newly acquired 73 acre vineyard, situated at the base of Mount Veeder in the Carneros AVA」「plans to begin planting in 2026」**
→ ⚠️ **OBP 1 行目（2023 Napa Valley Chardonnay）は、この新しい畑のワインではない。植樹は 2026 年開始である。**

🔍 **THÉSEUS における状態は「4 行に対して 1 レコード」であり、
しかもその 1 レコードは `vintage='—'` の Estate Cabernet 1 本のみ。
Chardonnay も Napa Valley Cabernet も canonical に存在しない。**

---

## History

⚠️ 🔴 **`montelena.com` に沿革ページは存在しない。**（WP の全 46 頁を列挙して確認済み。）
**以下は、公式の商品説明・bio PDF・体験商品の説明文・生産者 press release、および
🏛 連邦官報の最終規則から拾い上げたものであり、蔵が編んだ年表ではない。**

| 年 | 出来事 | 典拠 |
|---|---|---|
| **1882** | 🔴 **Chateau Montelena 設立。** | ✅ **ラベル `ESTABLISHED 1882`／公式商品説明「Founded in 1882」** |
| **1882（同）** | 🔴 **設立者は `Alfred L. Tubbs`。** | 📄 **生産者 press release「Since its founding in 1882 by Alfred L. Tubbs」**。⚠️ **公式サイト本体には出てこない** |
| **1972** | 🔴 **Barrett 家が取得。「modern era」の起点。** | ✅ **公式 bio「since his family assumed ownership in 1972」**／📄 **press release「its revival in 1972 by the Barrett family」** |
| **1972（ヴィンテージ）** | 🔴 ✅ **「**Insufficient winter rains. Bad spring frosts. Record heat in July caused considerable damage. Rainfall at crush. One of the worst years in memory. **All Cabernet Sauvignon was declassified.**」** | ✅ **公式 Estate Weather Summaries** |
| **1973（ヴィンテージ）** | 🔴 ✅ **「**Normal winter, warm spring. Long, cool growing season. Record crop. Excellent maturity. Clean fruit.**」（公式の分類は `Cool`）** | ✅ **同上。これがパリで勝ったシャルドネの年である** |
| 🔴 **1976** | 🔴 ✅ **「Judgment of Paris」で 1973 年のシャルドネが勝つ。** | ✅ **公式：「Montelena's 1973 Chardonnay prevailed at the Judgment of Paris」**／📄 **press release：「The winery's 1973 Chardonnay, which triumphed over the finest French white Burgundies in Paris」** |
| **1976（ヴィンテージ）** | ✅ **「First drought year. Fruit had high sugars, low acids. Vineyards stressed.」** | ✅ **公式 Weather Summaries。**（**試飲会の年であって、勝ったワインの年ではない**） |
| **1982** | ✅ **Bo Barrett が winemaker に就任。** | ✅ **公式 bio** |
| **2003〜** | 🔴 🏛 **Bo Barrett が `Calistoga` の AVA 申請を TTB に提出。** | 🏛 **連邦官報最終規則（案件番号 `2003R-496P`）：「**On behalf of interested parties in the Calistoga viticultural community, **James P. “Bo” Barrett of Chateau Montelena**, a Calistoga, California, winery and vineyard, petitioned TTB to establish “Calistoga” as an American viticultural area.**」** |
| **2008** | ✅ **Matt Crafton が Enologist として入社。** | ✅ **公式 bio** |
| 🔴 **2009-12-08 / 2010-01-07** | 🔴 🏛 **`Calistoga` AVA 制定（公布 2009-12-08、施行 2010-01-07）。** | 🏛 **`T.D. TTB-83`, `74 FR 64612`／27 CFR § 9.209** |
| **2013** | ✅ **Bo Barrett が CEO に就任。** | ✅ **公式 bio** |
| **2014** | ✅ **Matt Crafton が winemaker に就任。** | ✅ **公式 bio** |
| **近年** | 🔴 ✅ **「the largest replant of the Montelena Estate in five decades」を完了。** | ✅ **公式 bio（Crafton）。**⚠️ **年は書かれていない** |
| 🔴 **2025-03-18** | 🔴 📄 **Carneros AVA・Mount Veeder 山麓に 73 エーカーの畑を取得。植樹は 2026 年開始予定。** | 📄 **生産者 press release** |
| **2025-12** | ✅ **Matt Crafton が President に就任（winemaker と兼務）。** | ✅ **公式 bio** |
| **2026** | ✅ 🔴 **「Judgment of Paris 50 周年」の記念年として、記念ロゴ入り 2023 Napa Valley Chardonnay の 3 本組、記念体験（`Judgment of Paris Commemorative Experience`）、番号入りサーベルなどを展開。** | ✅ **公式商品ページ／会員特典ページ** |

⚠️ 🔴 **1882 年から 1972 年までの 90 年間について、公式サイトは一切書いていない。**
**禁酒法期の休止、その後の所有者、1968–1972 年の再建については、造り手の言葉が本調査で 1 件も見つからなかった。**
→ **したがって本書は Tubbs 以後・Barrett 以前の歴史を一切主張しない。** → Open Questions 3

---

## Location

| | |
|---|---|
| **Country** | **USA**（California） |
| **Region** | **Napa Valley** 🏛（27 CFR § 9.23） |
| 🔴 **Sub-AVA** | 🔴 🏛 **`Calistoga`（27 CFR § 9.209）。**「**The name of the viticultural area described in this section is “Calistoga”. For purposes of part 4 of this chapter, “Calistoga” is a term of viticultural significance.**」 |
| 🔴 **Calistoga と Napa Valley の関係** | 🔴 🏛 **入れ子である。**最終規則 SUMMARY：「**This Treasury decision establishes the Calistoga viticultural area in Napa County, California. The viticultural area is **entirely within the existing Napa Valley viticultural area**.**」<br>**規則本文：「the proposed area surrounds the town of Calistoga and is entirely within the existing Napa Valley viticultural area described in 27 CFR 9.23」** |
| 🔴 **制定** | 🔴 🏛 **`T.D. TTB-83`／`74 FR 64612`／公布 2009-12-08／施行 2010-01-07**（**2024-10-16 の `T.D. TTB-196`（`89 FR 83434`）で一部改正**） |
| 🔴 **申請者** | 🔴 🏛 **`James P. “Bo” Barrett of Chateau Montelena`。**→ **この AVA は本生産者の CEO が申請して生まれたものである** |
| **境界の骨格** | 🏛 **東は標高 880 フィート等高線（「beyond which lies rugged, unplantable terrain」）、西と北は Napa–Sonoma 郡界、南東は St. Helena AVA（§ 9.149）、南西は Diamond Mountain District AVA（§ 9.166）の境界がそれぞれ画定する** |
| 🔴 **経過措置** | 🔴 🏛 **§ 9.209(d)：「**A label containing the word “Calistoga” in the brand name approved prior to December 8, 2009 may not be used on wine bottled on or after December 10, 2012**」**（**ブランド名に `Calistoga` を含む既存ラベルの猶予規定。本生産者のラベルは brand name が `CHATEAU MONTELENA` なのでこの規定の対象外**） |
| **蔵の所在** | ✅ **`1429 Tubbs Lane, Calistoga, CA 94515`** |

### 🔴 ✅ The Montelena Estate Vineyard（公式ヴィンヤードマップ PDF より）

🔴 ✅ **公式マップの表題は `The Montelena Estate Vineyard / CALISTOGA · NAPA VALLEY` である。**
→ 🔴 **`The Montelena Estate` は、まず「畑（estate）の名」として公式に使われている。** → §Important Cuvées

✅ **マップは畑を 3 つの土壌帯に色分けし、造り手自身の言葉で特徴を与えている。**

| 土壌帯 | 公式の記述 | 公式が挙げるワインの特徴 |
|---|---|---|
| 🔴 **ALLUVIAL（沖積）** | 「**Deposited by ancient river flows, cobbly, stony, gravelly, excessively drained, moderate to low nutrient content.**」 | **Earthy / Aromatic / Complex / Concentrated** |
| 🔴 **VOLCANIC（火山性）** | 「**Formed by local volcanic flows. Mainly rhyolite and tuff, poor in nutrient and organic material, excessively to well-drained.**」 | **Spicy / Cedary / Often minty** |
| 🔴 **SEDIMENTARY（堆積）** | 「**Richer loamy soils formed by the settling of an ancient sea or lake. Can be poorly drained and have good nutrient and organic composition.**」 | **Ripe berry / Fruit / Herbal** |

✅ **マップ上の区画は `区画記号 / 品種 / 植樹年` の三点で示される。**
本調査で読み取れたもの（**網羅ではない**）:
**`89-A`〜`89-E` = CS・1989／`1-F` = CS・1974／`1-Fa` = CS・2017／`1-G` = CS・2023／`1-H` = CS・2014／
`1-J` = CS・2007／`1-L` = CF・2008／`1-M` = CS・2020／`1-N` = CS・2020／`1-1` = CS・2020／
`1-90A` = CS・1990／`2-A` = ZN・2023（Replant）／`2-B` = ZN・1972／`2-E` = ZN・1994／
`3-D` = PV・2015／`4-A` = CF・2015／`4-B` = CF・2023／`5-A` = PS・2023／`Apollo` = CS・2022**
✅ **固有名の付いた場所として `JADE LAKE`、`BEE HILL`、`APOLLO`、`RESERVOIR`、`WINERY` がマップに記載されている。**

🔴 **区画の植樹年に 1972・1974・1989・1990 と 2014〜2023 が混在しており、
公式 bio のいう「five decades ぶりの大規模な植え替え」が実際にマップ上で確認できる。**

🏛 **Calistoga AVA の地質（最終規則が採用した Jonathan Swinchatt 博士の報告より）** ——
「**The entirety of the proposed viticultural area is underlain by volcanic bedrock, part of the more widespread
Sonoma Volcanics… These rocks comprise lava flows, ash-fall tuffs, welded tuffs, pyroclastic flows, mudflows,
and ignimbrites. Their composition is largely andesitic with some rhyolitic rocks admixed.**」
「**Soils throughout the proposed viticultural area are loams, gravelly loams, cobbly loams, often with boulders…
clay-rich soils are of limited distribution.**」
🔴 **同報告は南の St. Helena / Rutherford / Oakville との差を「**topographically more diverse but geologically more uniform**」
（地形はより多様だが、地質はより均質）と要約している。**

### 🔴 Carneros の新しい畑（2025 年取得）

📄 🔴 **「The newly acquired 73 acre vineyard, situated at the base of Mount Veeder in the Carneros AVA…
Composed of well-drained loam and red volcanic soils」「plans to begin planting in 2026」**
⚠️ **press release 本文に畑の固有名は書かれていない**（PDF のファイル名にのみ `Vandal` の語がある）。
**したがって本書は畑の名前を主張しない。** → Open Questions 5

❓ **公式に無い**: 畑の総面積（エーカー数）、区画ごとの面積、樹齢構成の全体、台木、収量。

---

## Farming

🔴 **本節は本ドシエで最も薄い。理由は明確で、公式サイトに栽培のページが 1 枚も存在しないからである。**
**「情報が見つからなかった」のではなく、「造り手が公開していない」。**

### ✅ 生産者自身が述べていること（これだけ）

- ✅ **「Under his watch, the winery has completed the largest replant of the Montelena Estate in five decades,
  **deepened its sustainability initiatives**, and developed a new home for their iconic Chardonnay —
  a world-class estate vineyard in Carneros」**（Matt Crafton 公式 bio）
- ✅ **「we've endeavored to improve our offerings from the **systematic replanting of our Estate vineyard**,
  to modernizing the cellar, to **becoming an industry leader in sustainability**」**
  （2015 Estate Cabernet の Winemaker's Note）
- ✅ **「the **Calistoga Estate's gravelly benches, volcanic soils**」**（Crafton bio）
- ✅ **公式ヴィンヤードマップの 3 土壌帯の記述**（上記 §Location）
- ✅ **「For the safety of our guests and grapes, we do not allow anyone to walk through the vineyard.」**（FAQ）

🔴 ⚠️ **「sustainability」という語は 2 回出るが、**
**どの制度・どの認証・どの基準を指すのかは一度も書かれていない。**

### 🏛 認証登録簿の照会結果（**読めたものと読めなかったものを分けて記す**）

| 登録簿 | 読めたか | 結果 |
|---|---|---|
| 🔴 🏛 **Napa Green（`napagreen.org/participating-members/`）** | 🔴 ✅ **読めた。**HTML に社名が server-rendered されており、`Winery` / `Vineyards` / `Cellars` / `Estate` を含む社名 73 件を機械抽出できた（`Charles Krug Winery` → `Chimney Rock Winery` の順に並ぶ） | 🔴 **`Montelena` は 0 件。`Barrett` も 0 件。**<br>→ **2026-08-05 時点の同名簿に本生産者は載っていない** |
| ⚠️ **CCOF 会員名簿（`ccof.org/resources/member-directory/`）** | ⚠️ 🔴 **読めなかった。**`?search_api_fulltext=Montelena` は 200 を返すが結果が本文に出ない。**対照実験として既知の有機認証生産者名（`Grgich` / `Frog`）で検索しても同様に 0 件**であり、検索結果が JS 描画であることが確定した | ⚠️ **判定不能。有無いずれも主張しない** |
| ⚠️ **USDA Organic INTEGRITY（`organic.ams.usda.gov/integrity/`）** | ⚠️ 🔴 **読めなかった。**Blazor の JS シェルが返るのみ。`POST /integrity/api/OperationSearch` は `400` | ⚠️ **判定不能。**（**Batch 9 の所見が本バッチでも再現した**） |
| ⚠️ **Demeter USA / Fish Friendly Farming** | ⚠️ **参加者名簿の機械可読な一覧を本調査で特定できなかった** | ⚠️ **判定不能** |

### 🔴 結論（**この形でしか言えない**）

🔴 **① 生産者は有機・ビオディナミ・いかなる認証も主張していない。**
🔴 **② Napa Green の名簿には載っていない（読める登録簿での実測）。**
🔴 **③ CCOF・USDA INTEGRITY・Demeter・FFF は本調査では読めなかったため、何も主張しない。**
🔴 **④ 「実践している（practised）」と「認証されている（certified）」を分ける以前に、
本生産者は実践の中身すら公開していない。**
→ **卓上で言えるのは「造り手は自分の栽培について公表していない」までである。** → §Staff Notes ⚠️ ③

⚠️ 🔴 **第三者（米国の全国卸 Wilson Daniels）の 2025-11-04 付リリースは、
「water conservation, embracing conscious farming, piloting modern technology, and
converting the entire estate to solar power」と書いている。**
⚠️ **これは生産者ドメインの資料ではなく、本調査ではいずれも生産者の言葉として裏づけられなかった。**
→ 🔴 **「全量ソーラー」「conscious farming」は卓上で言わない。** → §Staff Notes ⚠️ ④

---

## Winemaking

🔴 ✅ **公式テクニカルシート（`Winemaker's Notes`）は OBP 4 ヴィンテージすべてについて存在し、
`BLEND` / `HARVESTED` / `ALCOHOL` / `BOTTLED` / `AGING` / `RELEASE DATE` / `CELLARING` / `SERVING` を
定型で開示している。本節はすべてこの一次資料に基づく。**

| 項目 | **2023 Napa Valley Chardonnay** | **2022 Napa Valley Cabernet Sauvignon** | **2021 Estate Cabernet Sauvignon** | **2011 Montelena Estate Cabernet Sauvignon** |
|---|---|---|---|---|
| **シート上の表題** | `CHARDONNAY / NAPA VALLEY, 2023` | `cabernet sauvignon / NAPA VALLEY, 2022` | `estate cabernet sauvignon / CALISTOGA, 2021` | `2011 Montelena Estate Cabernet Sauvignon` |
| 🔴 **ブレンド** | **100% Chardonnay** | 🔴 **85% Cabernet Sauvignon / 14% Merlot / 0.5% Petit Verdot / 0.5% Cabernet Franc** | 🔴 **94.1% Cabernet Sauvignon / 4.9% Cabernet Franc / 1% Petit Verdot** | 🔴 **99% Cabernet Sauvignon / 1% Cabernet Franc** |
| **収穫** | **September 8 – October 10, 2023** | **September 8 – 24, 2022** | **September 4 – October 8, 2021** | **September 29 – October 29, 2011** |
| **アルコール** | **13.9%** | **14.2%** | **14.1%** | **13.5%** |
| **瓶詰** | **July 23 – August 1, 2024** | **April 1 – 9, 2024** | **July 27 – 28, 2023** | **December 2013** |
| 🔴 **樽** | 🔴 **10 か月、100% French Oak、新樽 25%** | 🔴 **16 か月、French and Eastern European Oak、新樽 30%** | 🔴 **22 か月、100% French Oak、新樽 45%** | 🔴 **22 か月、100% French、新樽 33%** |
| **リリース** | **November 2025** | **April 2025** | **March 2025** | **Spring 2015** |
| **醸造責任者** | **Matthew Crafton** | **Matthew Crafton** | **Matthew Crafton** | **Matt Crafton** |

🔴 **参考（1 世代前）— 2019 Estate Cabernet Sauvignon: `99% Cabernet Sauvignon / 0.5% Petit Verdot / 0.5% Cabernet Franc`。**
→ 🔴 **Estate Cabernet のセパージュは年によって 94.1%〜99% の幅で動く。「100% カベルネ」ではない。**

🔴 ✅ **熟成推奨（公式の言葉）**
- **2023 Chardonnay**：「**Expect bright fruit and vineyard flavors for 3〜5 years post release.
  Complexity builds as it reaches maturity after 15〜20 years, although further aging is achievable.**」
  🔴 **サーヴィス指定：「No decant is required for this wine, as the aromas can be quite delicate and sensitive to aeration.
  Serve slightly chilled at cellar temperature or around 55°F.**」
- **2022 Napa Valley Cabernet**：「**This wine is ready to be enjoyed. Drink now or cellar for added complexity
  over the next 10 years.**」
- 🔴 **2021 Estate Cabernet**：「**This vintage will reward time in cellar. It will take up to 10 years to build
  complexity with aging potential of 30+ years.**」

⚠️ 🔴 **公式シートに記載が無い項目（4 点とも全ヴィンテージで空白）:**
**発酵容器・発酵温度、マロラクティック発酵の有無、酵母、pH / TA / Brix などの分析値、生産本数。**
→ 🔴 **したがって本書はこれらを一切主張しない。** → §Staff Notes ⚠️ ⑦

---

## Style

### ✅ 公式テイスティングノート（OBP 該当 4 本すべて。造り手 Matt Crafton の署名つき）

| ワイン | 公式ノート（抜粋） |
|---|---|
| 🔴 **2023 Napa Valley Chardonnay** | 「**Cool vintages are something special. While there's certainly California luster and opulence in the margins,
both are tucked away right now, overshadowed by lush pear, lime leaf and orange blossom.
The minerality and tension on the palate are simply awesome and the acidity is bright and racy.**
… the mouthfeel is just gorgeous with **more gravitas and weight than I would have expected at this time**; a very pleasant surprise.」<br>**（洋梨、ライムの葉、オレンジの花／ミネラルと張り／柑橘・青リンゴ・火打石が今後数年支配する、と造り手が明言）** |
| 🔴 **2022 Napa Valley Cabernet Sauvignon** | 「**Driven by dark fruit, predominantly blackberry and cassis, the aromas are rich and intense.
They are closely followed by spicy clove and vanilla before yielding to pipe tobacco and a touch of caramel.**
On the palate, the tannins are quite supple… **Strawberry and cranberry sauce highlight the transition to the finish**…
Here the tannins are more sandy… **expressing now as cola, graphite and black cherry.**」 |
| 🔴 **2021 Estate Cabernet Sauvignon** | 「**On the nose, there's an elegant introduction of perfectly ripe blackberry and cranberry sauce notes…
punctuated by hints of black pepper and cedar, with additional layers of mint, cassis and black cherry revealed with a swirl.
The palate is intense as the tight, angular tannins vie with silky, bright fruit for dominance.
The finish on this wine doesn't quit. It keeps evolving through coffee bean, then vanilla and finally dried blackberry.
These slowly morph both texturally and in flavor into fresh walnut and dark chocolate.**」 |
| 🔴 **2011 Montelena Estate Cabernet Sauvignon** | 🔴 「**Aromatically, this is one of the most elegant Estate Cabernets that we have released in the last decade.
Notes of strawberry, rhubarb, and vanilla jump out of the glass, closely followed by lavender, bay laurel, and allspice…
On the palate, the rich minerality is balanced by ripe raspberry and earth, all of which are tied together by
silky, fine tannins that frame and enhance the soft texture, rather than overwhelm it…
As would be expected, the finish is almost Bordelaise in its subtlety and grace, with hints of cranberry, mint, and cocoa.**」 |

### 🔴 ✅ 公式 Estate Weather Summaries（**1972〜2025 の 54 年分。造り手自身の分類つき**）

🔴 **`/resources/` に、Estate の年ごとの気候要約が `Cool` / `Temperate` / `Warm` の三分類つきで掲出されている。
これは他の生産者ではまず得られない一次資料であり、卓上での「年の説明」に直接使える。**

| 年 | 分類 | 公式の要約（抜粋） |
|---|---|---|
| **1972** | **Cool** | 🔴 「Insufficient winter rains. Bad spring frosts. Record heat in July… One of the worst years in memory. **All Cabernet Sauvignon was declassified.**」**（Barrett 家最初の年）** |
| 🔴 **1973** | **Cool** | 「**Normal winter, warm spring. Long, cool growing season. Record crop. Excellent maturity. Clean fruit.**」**（パリで勝ったシャルドネの年）** |
| **1976** | **Warm** | 「First drought year. Fruit had high sugars, low acids. Vineyards stressed.」**（試飲会の年であって、勝ったワインの年ではない）** |
| 🔴 **2011** | **Cool** | 「Warm weather teased us for much of the season but never permanently settled in… **the cold nights continued to persist, the fog lingered, and the heat from the Nevada desert stayed far, far away.** With harvest approaching, we recognized the **textbook Bordelaise flavor profile**… and embraced the **bright acid profile and soft textures** that would come to be hallmarks of this vintage.」 |
| 🔴 **2021** | **Temperate** | 「A warm spring initiated early budbreak… **Bloom was punctuated by very warm temperatures, which reduced fruit set and the overall size of the crop. Despite the low yields, what remained was excellent.** Harvest was methodical and predictable.」 |
| 🔴 **2022** | **Warm** | 「The dry, mild winter triggered early budbreak… **While there was significant heat over Labor Day weekend that accelerated ripening and reduced the crop size**, the growing season was already leaning early so the lasting effect was mostly **increased concentration and flavor in the berries.**」 |
| 🔴 **2023** | **Cool** | 「**2023 was one of the finest vintages of the past decade**, thanks to heavy winter rains… A long, cool spring pushed budbreak back by **two to three weeks**… delivering a **textbook, exceptional year.**」 |

🔴 ✅ **2011 と 2021 の対比は、造り手自身の言葉でそのまま作れる。**
**2011 = 「過去 10 年で最もエレガントな Estate Cabernet の 1 本」「ほとんどボルドー的な余韻」（13.5%、新樽 33%）。**
**2021 = 「10 年かけて複雑さを築き、30 年以上の熟成能力」「タンニンが角張り、果実と競り合う」（14.1%、新樽 45%）。**
→ 🔴 **同じ畑・同じ醸造家の、正反対の年である。$625 と $800 の差を説明する軸になる。**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 4 行。4 行すべて `match_state = unresolved`**）

| # | メニュー印字 | VT | 価格 | セクション | ✅ **公式での確認結果** |
|---|---|---|---|---|---|
| **1** | **`Napa Valley Chardonnay`** | **2023** | **$235** | `UNITED STATES \| WHITE > NAPA` | ✅ 🔴 **実在。しかも公式の製品名がそのまま `2023 Napa Valley Chardonnay` である。**<br>**ラベル：`CHATEAU MONTELENA / ESTABLISHED 1882 / 2023 / Chardonnay / NAPA VALLEY`。**<br>**公式テクニカルシート `2023-Napa-Valley-Chardonnay.pdf` あり（100% Chardonnay・13.9%・10 か月 100% French Oak 新樽 25%・2025 年 11 月リリース）。**<br>**蔵出し価格 $75（750ml）→ OBP は約 3.1 倍** |
| **2** | **`Napa Valley Cabernet Sauvignon`** | **2022** | **$255** | `UNITED STATES \| RED > NAPA` | ✅ 🔴 **実在。公式の製品名がそのまま `2022 Napa Valley Cabernet Sauvignon`。**<br>**ラベル：`CHATEAU MONTELENA / ESTABLISHED 1882 / 2022 / Cabernet Sauvignon / NAPA VALLEY`（金帯は無い）。**<br>**公式テクニカルシート `2022-Napa-Valley-Cabernet-Sauvignon.pdf` あり（85% CS / 14% Merlot / 0.5% PV / 0.5% CF・14.2%・16 か月 French and Eastern European Oak 新樽 30%）。**<br>**蔵出し価格 $85 → OBP は 3.0 倍** |
| **3** | **`"The Montelena Estate," Calistoga Cabernet Sauvignon`** | **2021** | **$625** | `UNITED STATES \| RED > NAPA` | ✅ 🔴 **実在。しかも印字はラベルの逐語である。**<br>🔴 **ラベル：金地の帯に `THE MONTELENA ESTATE`、その下に `CHATEAU MONTELENA / ESTABLISHED 1882 / [シャトーの銅版画] / 2021 / CABERNET SAUVIGNON / CALISTOGA · NAPA VALLEY`。**<br>**公式サイトでの呼称は `2021 Estate Cabernet Sauvignon`、テクニカルシートは `estate cabernet sauvignon / CALISTOGA, 2021`。**<br>**蔵出し価格 $200 → OBP は約 3.1 倍** |
| **4** | **`"The Montelena Estate," Calistoga Cabernet Sauvignon`** | **2011** | **$800** | `UNITED STATES \| RED > NAPA` | ✅ 🔴 **実在。ラベル構成は 2021 と同一（金帯 `THE MONTELENA ESTATE` ＋ `CALISTOGA · NAPA VALLEY`）。**<br>🔴 **14 年前のヴィンテージだが公式テクニカルシートが現在も生きている**（`CHM_WN_ME-CS-2011_Trade.pdf`。**Notes from the Winemaker, Matt Crafton, December 2014**）。<br>🔴 **さらに蔵が現在も `Library Wines` として 750ml を $250 で直販している**（WooCommerce 商品 `2011 Montelena Estate Cabernet Sauvignon`）。**3.0L も商品として存在。**<br>**OBP は蔵出しの約 3.2 倍** |

🔴 **4 行すべてについて、公式の製品名・ラベル表記・セパージュ・アルコール・樽・収穫日・瓶詰日まで言える。**
🔴 **OBP の印字と公式の間に「別物を指している」ズレは 1 件も無い。**

### 🔴 反復パターン (a) の検証 —— **本生産者では成立しない**

**依頼時の想定は「メニューが産地語や品種語をキュヴェ名として印字している」（Harlan / Mayacamas / Grgich / Abreu と同型）だった。
本調査の結論はこれを支持しない。**

| 検証 | 結果 |
|---|---|
| **1・2 行目 `Napa Valley Chardonnay` / `Napa Valley Cabernet Sauvignon`** | 🔴 **生産者自身の製品名と完全一致。**EC の商品名・テクニカルシートの表題・ラベルのいずれもこの形。**キュヴェ名が別に存在してそれが落ちている、という事実は無い** |
| **3・4 行目 `"The Montelena Estate,"`** | 🔴 **ラベル最上部の金帯に実在する文字列。**<br>**メニューの二重引用符と内側のカンマはメニュー側の組版慣行だが、`The Montelena Estate` という語そのものは造り手の印刷物にある** |
| **3・4 行目 `Calistoga Cabernet Sauvignon`** | 🔴 **ラベルの `CABERNET SAUVIGNON` ＋ `CALISTOGA · NAPA VALLEY` の圧縮。**<br>⚠️ **ラベルは `CALISTOGA · NAPA VALLEY` と 2 段で書くが、メニューは `Napa Valley` を落としている。これは軽微な情報落ち** |

🔴 **むしろ揺れているのは生産者の側である。同一のワインに対して 3 つの呼称が公式に並存する:**
- **ラベル** = `THE MONTELENA ESTATE`（金帯）＋ `CABERNET SAUVIGNON`
- **EC の商品タイトル / テクニカルシートの表題** = `Estate Cabernet Sauvignon`
- **WooCommerce の内部商品名・旧テクニカルシートの表題** = `Montelena Estate Cabernet Sauvignon`
  （**例：カード表示は `2011 Estate Cabernet Sauvignon`、同じ商品のカートボタンは `2011 Montelena Estate Cabernet Sauvignon`。
  同一ページ内で 2 通りが同時に出る**）

🔴 **したがって「正式名は 1 つである」という前提自体が、この生産者では成立しない。**
→ **canonical に載せる際の `name` をどれにするかは設計判断であり、本書では決めない。** → Open Questions 2

### 🔴 `The Montelena Estate` とは何か（**追加調査目標 ①の回答**）

🔴 ✅ **① まず「畑の名」である。**
**公式ヴィンヤードマップ PDF の表題が `The Montelena Estate Vineyard / CALISTOGA · NAPA VALLEY`。**
🔴 ✅ **② 次に「ラベル上の呼称」である。**
**Estate Cabernet のラベル最上部の金帯に `THE MONTELENA ESTATE`。**
🔴 ✅ **③ 蔵は自社の体験商品名にも使う。**
**`The Montelena Estate Collection`（4 ヴィンテージの Estate Cabernet 比較試飲、$125／人）。**
🔴 ✅ **④ ただし「キュヴェ名」としては使っていない。**
**キュヴェ名にあたるのは `Estate Cabernet Sauvignon`（公式の呼称）であり、
`The Montelena Estate` はその上に載る「畑／シリーズの冠」である。**

🔴 ⚠️ **⑤ `Estate` が 27 CFR § 4.26 の法定用語 `Estate bottled` を意味するかどうかは、本調査では確定できない。**
🏛 **§ 4.26(a) の要件は「(1) 瓶詰め蔵が表示 AVA 内にあること、(2) 使用ブドウの全量を、
表示 AVA 内の、蔵が所有または支配する土地で栽培したこと、(3) 破砕・発酵・仕上げ・熟成・瓶詰めを
連続工程で、ワインが一度も蔵の敷地を離れずに行ったこと」の 3 点すべてである。**
🏛 **同(d)：「No term other than `Estate bottled` may be used on a label to indicate combined growing and bottling conditions.」**
⚠️ 🔴 **本調査で取得できたのは表ラベルの画像のみであり、そこに `ESTATE BOTTLED` の 2 語は現れない。
裏ラベルの瓶詰者表示は未取得。TTB COLA は CAPTCHA でゲートされていた。**
→ 🔴 **したがって本書は「Estate bottled である」とも「ではない」とも言わない。** → Open Questions 1（実ボトル案件）

### ✅ 生産者の現行ラインナップ（**canonical には 1 件も無い**）

🔍 **WooCommerce Store API と product-sitemap から機械的に確定した現行／近年の銘柄:**
🔴 **`Estate Cabernet Sauvignon`（Calistoga・flagship）**⭐OBP／
🔴 **`Napa Valley Cabernet Sauvignon`**⭐OBP／🔴 **`Napa Valley Chardonnay`**⭐OBP／
**`Estate Zinfandel`（Calistoga）／`Calistoga Petite Sirah`／`Napa Valley Sauvignon Blanc`／
`Potter Valley Riesling`／`Sonoma County Chardonnay`／`Russian River Valley Chardonnay`／
`Dry Creek Sauvignon Gris`／`Blanc de Blanc Sparkling Wine`（2023）**

🔴 **すなわち Calistoga／Napa Valley 以外の産地（Sonoma County、Russian River Valley、Dry Creek、Potter Valley）の
ワインも同一ブランドで出している。OBP の 4 行はいずれも Napa 系だが、この事実は知っておく価値がある。**

### 🔴 ✅ 公式が保有するヴィンテージ資料の範囲（**Estate Cabernet の「2020 年の不在」**）

✅ **`/resources/` の Tasting Notes 一覧が挙げる Estate Cabernet Sauvignon のヴィンテージ:**
**2006 / 2007 / 2008 / 2009 / 2010 / 2011 / 2012 / 2013 / 2014 / 2015 / 2016 / 2017 / 2018 / 2019 / **2021**。**
🔴 ⚠️ **`2020` だけが飛んでいる。Bottle Shots の一覧でも同じく 2020 が無い。**
⚠️ **公式は理由を一切書いていない。**
→ 🔴 **「2020 は造らなかった」と断定しない。「造り手の公開資料に 2020 が無い」という事実だけを記録する。** → Open Questions 4

✅ **Napa Valley Chardonnay の Tasting Notes は 2012〜2023 が連続。**
✅ **Napa Valley Cabernet Sauvignon は 2017 / 2018 / 2019 / 2021 / 2022 / 2023（**ここでも 2020 が無い**）。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① ナパの最北・カリストガ。1882 年創業、1972 年から Barrett 家。1976 年のパリで勝ったのは 1973 年のシャルドネ。**
「**ナパ・ヴァレーのいちばん北、カリストガ**にある**1882 年創業**の蔵です。
石造りのシャトーがそのままラベルの絵になっていて、ラベルにも **`ESTABLISHED 1882`** と入っています。
**いまの姿は 1972 年に Barrett 家が取得してから**で、**現 CEO のボー・バレットは 1972 年以降のすべてのヴィンテージに関わり、
1982 年に醸造長、2013 年に CEO**になりました。
**1976 年のいわゆる『パリの審判』で勝ったのは、この蔵の 1973 年のシャルドネ**です。
**造り手の言葉では『prevailed（勝った）』、公式のプレスリリースでは
『triumphed over the finest French white Burgundies（最良のフランス白ブルゴーニュを破った）』**と書かれています。」

**② カリストガはナパ・ヴァレーの中の AVA で、この蔵の CEO が申請して 2010 年にできた。**
「🔴 **カリストガは『ナパ・ヴァレーとは別の産地』ではありません。ナパ・ヴァレー AVA の内側にすっぽり入る sub-AVA** です。
**連邦官報の制定文書がはっきり『entirely within the existing Napa Valley viticultural area』と書いています。
公布が 2009 年 12 月 8 日、施行が 2010 年 1 月 7 日**です。
🔴 **そしてその申請者が、まさにこの蔵の CEO、ジェームズ・P・"ボー"・バレット**でした。
だから **Estate のラベルには `CALISTOGA · NAPA VALLEY` と 2 段で入っています。**」

**③ メニューの『The Montelena Estate』はラベルに実在する。旗艦は白ではなく Estate カベルネ。**
「🔴 **メニューの `"The Montelena Estate,"` は、ラベルの一番上の金色の帯にそのまま印刷されている文字です。**
**その下が `CHATEAU MONTELENA` で、さらに下に `CABERNET SAUVIGNON` と `CALISTOGA · NAPA VALLEY`。**
**同じワインを蔵の通販サイトは `Estate Cabernet Sauvignon` と呼んでいて、呼び名が複数あります。**
🔴 **そして造り手が『flagship（旗艦）』と呼んでいるのは、有名なシャルドネではなくこの Estate カベルネ**です。
公式に『**Membership in this program is the only way to guarantee access to our flagship wine,
the Estate Cabernet Sauvignon**』と書かれています。」

### 追加で使える一手（**すべて公式一次資料**）

- 🔴 **2011（$800）と 2021（$625）の対比**：「**同じ畑・同じ醸造家（マット・クラフトン）の、正反対の年**です。
  **2011 は造り手の分類で `Cool`。『ネヴァダの熱気は遠いまま、霧が居座り、冷たい夜が続いた』年で、
  造り手自身が『過去 10 年で最もエレガントな Estate カベルネの 1 本』『余韻はほとんどボルドー的』と書いています。
  アルコール 13.5%、フレンチオーク 22 か月・新樽 33%。**
  **2021 は `Temperate`。開花期の高温で結実が減り、収量は少ないが質は高かった年。
  アルコール 14.1%、新樽 45%。造り手は『複雑さが出るまで 10 年、熟成能力は 30 年以上』と書いています。**」
- 🔴 **2023 シャルドネ（$235）**：「**造り手が『過去 10 年で最良のひとつ』と呼ぶ年**です。
  **100% シャルドネ、10 か月フレンチオーク・新樽 25%、アルコール 13.9%。**
  **洋梨、ライムの葉、オレンジの花。造り手は『ミネラルと緊張感が素晴らしく、酸は明るく鋭い』と。**
  🔴 **公式が『デカンタは不要。香りが繊細で通気に敏感なので、**セラー温度（約 13℃／55°F）でやや冷やして**』と
  はっきり指定しています。**」
- 🔴 **2022 ナパ・ヴァレー・カベルネ（$255）**：「**これは Estate ではないほうのカベルネで、
  ラベルに金の帯がありません。産地表記も `NAPA VALLEY` だけです。**
  **セパージュも違って、85% カベルネ・ソーヴィニヨン、14% メルロ、プティ・ヴェルドとカベルネ・フランが各 0.5%。**
  **造り手は『収穫直前の 7 日間がこのヴィンテージすべてを決めた』——
  レイバー・デイの熱波で、赤い果実が黒い果実に変わった年だと書いています。**」
- 🔴 **畑の土壌**：「**造り手は自分の畑を 3 つの土壌帯に分けて公表しています。**
  **沖積（古い川が運んだ礫と石。earthy・aromatic・complex・concentrated）、
  火山性（流紋岩と凝灰岩。spicy・cedary・often minty）、
  堆積（古い海か湖の沈殿による豊かなローム。ripe berry・fruit・herbal）。**」
- 🔴 **1972 年**：「**Barrett 家の最初の年である 1972 年について、蔵は自分で
  『記憶にある限り最悪の年のひとつ。カベルネ・ソーヴィニヨンは全量格下げした』と書き残しています。**
  そういう年から始まった蔵です。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／第三者の主張にすぎない**）

1. 🔴 ⚠️ **『メニューの "The Montelena Estate" は店の表記ゆれです』と言わない。**
   **ラベル最上部の金帯にその通り印刷されている。むしろ蔵の通販サイトのほうが `Estate Cabernet Sauvignon` と省略している。**
2. 🔴 ⚠️ **『Estate Cabernet は 100% カベルネ・ソーヴィニヨンです』と言わない。**
   **公式テクニカルシート実測：2021 = 94.1% CS / 4.9% CF / 1% PV、2019 = 99% / 0.5% / 0.5%、2011 = 99% CS / 1% CF。
   年によって動く。**（**THÉSEUS の DB は「100% CS」と書いているが、これは公式と矛盾している。**）
3. 🔴 ⚠️ **『オーガニック』『ビオディナミ』『サステナブル認証』と言わない。**
   **公式サイト全 46 頁・テクニカルシート・bio・プレスリリースのどこにも認証名が 1 つも無い。**
   🏛 **Napa Green の参加者名簿にも載っていない。CCOF・USDA INTEGRITY は本調査では読めなかったので何も言えない。**
   **言えるのは「造り手は栽培について公表していない」まで。**
4. 🔴 ⚠️ **『畑全体をソーラーでまかなっている』『conscious farming』と言わない。**
   **これは米国の全国卸（Wilson Daniels）の 2025-11-04 付リリースの記述で、生産者自身の資料では裏づけられなかった。**
5. 🔴 ⚠️ **『Estate Bottled（エステート・ボトルド）です』と言わない。**
   🏛 **`Estate bottled` は 27 CFR § 4.26 の法定用語で、産地内立地・全量自社栽培・連続工程の 3 要件を満たす場合にのみ使える。**
   **本調査で読めたのは表ラベルのみで、そこにこの 2 語は無い。TTB COLA は CAPTCHA でゲートされ確認できていない。**
   **`Estate` という語が入っていることは、法定の `Estate bottled` の主張とは別である。**
6. 🔴 ⚠️ **映画『Bottle Shock』（2008）を蔵の説明として使わない。**
   **公式サイト・公式 PDF・公式プレスリリースのいずれにも映画への言及が 1 件も無い。**
   **THÉSEUS の DB は「映画『Bottle Shock（2008）』で描かれた蔵として認知度高い」と書いているが、これは造り手の言葉ではない。**
   **1976 年の出来事は、映画の筋書きではなく造り手の記述で語ること。**
7. 🔴 ⚠️ **マロラクティック発酵の有無、発酵温度、酵母、pH / TA / Brix、生産本数を語らない。**
   **公式テクニカルシートは `BLEND` / `HARVESTED` / `ALCOHOL` / `BOTTLED` / `AGING` / `RELEASE DATE` しか開示しておらず、
   上記は 4 ヴィンテージすべてで完全に空白である。**
8. 🔴 ⚠️ **『1882 年から Barrett 家が』と言わない。**
   **1882 年は設立年で、設立者は Alfred L. Tubbs。Barrett 家の取得は 1972 年である。**
   ⚠️ **さらに、公式 bio が Jim Barrett を「winery founder」と呼んでいるが、これは 1972 年の再興を指す表現であり、
   1882 年の設立者という意味ではない。ここを混ぜない。**
9. 🔴 ⚠️ **1882 年から 1972 年までの 90 年間について何も語らない。**
   **公式サイトにこの期間の記述が 1 行も無い。禁酒法・中間の所有者・再建の経緯を推測で埋めない。**
10. 🔴 ⚠️ **『2020 年は造らなかった』と言わない。**
    **公式の Tasting Notes / Bottle Shots の一覧に Estate Cabernet と Napa Valley Cabernet の 2020 が無い、というだけである。
    理由は書かれていない。**
11. ⚠️ **『カリストガはナパとは別の産地です』と言わない。**
    🏛 **連邦規則上、カリストガはナパ・ヴァレー AVA の完全な内側にある。ラベルも `CALISTOGA · NAPA VALLEY` と併記している。**
12. ⚠️ **1976 年の試飲会について、造り手が書いていないことを足さない。**
    **公式が書くのは「1973 年のシャルドネが Judgment of Paris で prevailed した」「フランスの最良の白ブルゴーニュを triumph した」まで。
    出品銘柄・順位・点数・審査員・その後の再現試飲は、いずれも本調査の公式資料に一切現れない。**
13. ⚠️ **第三者点数・受賞歴を語らない。**
    **`/in-the-news/` は第三者媒体の引用集であり、本書は事実の典拠として一切採用していない。**
14. ⚠️ **2025 年に取得した Carneros の畑を「いまのシャルドネの畑」と言わない。**
    **植樹は 2026 年開始予定。OBP の 2023 シャルドネはこの畑のワインではない。畑の固有名も公式には書かれていない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **本生産者について報告すべきことは 2 種類ある。①「gap」（レコードが存在しない）と、②「canonical 記述の誤り」である。**
🔒 **`research/canonical_conflicts/REGISTER.md` は本バッチでは編集禁止のため、一切触れていない。**
🔒 **canonical も `mapping.json` も一切変更していない。**

---

### 🔴 ① **gap —— 4 行に対して canonical レコードは 1 件。既存の登録票クラスに該当が無い。**

🔍 **canonical 全 928 レコードを機械走査し、文字列 `Montelena` を含むレコードが以下 1 件のみであることを実測した。**

```
id          : chateau-montelena-estate
producer    : Chateau Montelena
name        : Estate Cabernet Sauvignon
vintage     : —
country     : USA
region      : California
subregion   : Napa Valley — Calistoga
color       : Rouge
classification : Calistoga Cabernet Sauvignon
```

🔍 **OBP は 4 行。intake（`obp_intake_normalized_20260804.json`）上の状態:**
- **4 行すべて `match_state = unresolved` / `cuvee_state = unresolved` / `vintage_state = unresolved` / `confidence = 0.0`**
- **4 行すべて `producer_state = exact`（`proposed_canonical_producer_id = producer:chateau-montelena`）**
- **evidence 欄はいずれも「`'Chateau Montelena'` の canonical キュヴェ 1 件に一致無し」と記録している**

🔴 **したがって欠落は以下のとおり:**

| OBP 行 | canonical に対応するキュヴェ・レコードが | 
|---|---|
| **1. Napa Valley Chardonnay 2023** | 🔴 **存在しない**（Chardonnay のレコードが 0 件） |
| **2. Napa Valley Cabernet Sauvignon 2022** | 🔴 **存在しない**（Estate ではないほうの Cabernet が 0 件） |
| **3. The Montelena Estate / Calistoga Cabernet Sauvignon 2021** | ⚠️ **キュヴェとしては 1 件あるが `vintage='—'` のため 2021 に解決できない** |
| **4. 同 2011** | ⚠️ **同上。同じ 1 件に 2 本のヴィンテージを当てることはできない** |

🔴 **これは「別のレコードに誤って当たっている」という衝突ではない。「当てる先が存在しない」である。**
🔒 **既存の登録票クラス（`C-*` = キュヴェ誤割当、`S-*` = 文字列正規化、`P-*` = 生産者属性）はいずれも
「レコードの不在」を扱わない。したがって本件は既存 ID に紐づけない。**
🔒 **番号を開くかどうか、また `gap` という新クラスを設けるかどうかは CTO の判断であり、
本書は「未採番のまま、形だけを記述する」にとどめる。**

---

### 🔴 ② **canonical の `description` / `obp_note` が公式一次資料と矛盾する（4 点）**

🔴 **本バッチの標準的所見（「canonical の散文は信頼できない」）が、本生産者でも再現した。**

| # | canonical の記述 | ✅ 公式一次資料 | 判定 |
|---|---|---|---|
| **②-1** | 「**Calistoga自家畑から100% CS**」<br>（`description_en`: 「100% CS from Calistoga estate vineyards」） | 🔴 **2021 = `94.1% Cabernet Sauvignon, 4.9% Cabernet Franc, 1% Petit Verdot`**<br>**2019 = `99% CS, 0.5% Petit Verdot, 0.5% Cabernet Franc`**<br>**2011 = `99% Cabernet Sauvignon, 1% Cabernet Franc`** | 🔴 **誤り。3 ヴィンテージすべてで単一品種ではない** |
| **②-2** | 「**新樽率を抑えた長熟型クラシック・スタイル**」<br>（`description_en`: 「restrained-oak」） | 🔴 **2021 = `22 Months, 100% French Oak, **45% New**`**<br>**2011 = `22 months, 100% French, 33% new`** | 🔴 **少なくとも 2021 について「抑えた」とは言えない。単一の形容で固定できない** |
| **②-3** | 「**映画『Bottle Shock（2008）』で描かれた蔵として認知度高い**」 | ⚠️ 🔴 **公式サイト全 46 頁・テクニカルシート・bio・press release のいずれにも `Bottle Shock` の語が 1 件も無い** | 🔴 **生産者の言葉ではない。canonical から staff 向け表示に流れると、造り手が語っていない物語を卓上で語ることになる** |
| **②-4** | `obp_note`「**市場価格 $150〜$200/btl**」／`tags` に `$150-200` | 🔴 **蔵出し（750ml）: 2021 Estate = `$200`、2022 Estate = `$200`。2023 Estate は会員向け先行 6 本 `$990`／通常価格 `$1,350`（＝ 1 本あたり `$225`）と公式が明記** | ⚠️ **帯の上限に接しており、次のヴィンテージで外れる。市場価格を canonical に静的に持つこと自体の是非を含めた設計問題** |

🔴 **①（gap）と ②（記述の誤り）は独立している。gap を埋めるだけでは ② は残る。**

---

### 🔴 ③ **Batch 9 の未採番シェイプ（attribute provenance）は本生産者では再発していない —— 明示的に記録する**

🔴 **Batch 9 では、canonical が `subregion = "Napa Valley — Howell Mountain"` と主張する一方、
ラベルにも 2 件の COLA にも `NAPA VALLEY` としか無い、という事例が
「属性の出所」の未採番シェイプとして escalate された。**

🔴 **本生産者では、同じ形の属性（`subregion = "Napa Valley — Calistoga"`）に一次資料の裏づけがある。**
- ✅ 🔴 **生産者公表のラベル画像（2011・2021 とも）に `CALISTOGA · NAPA VALLEY` と 2 段で印字されている。**
- ✅ **公式テクニカルシートの表題が `estate cabernet sauvignon / CALISTOGA, 2021`。**
- ✅ **公式ヴィンヤードマップの表題が `The Montelena Estate Vineyard / CALISTOGA · NAPA VALLEY`。**
- 🏛 **`Calistoga` は 27 CFR § 9.209 の AVA であり、`Napa Valley`（§ 9.23）の完全な内側にある。
  したがって `Napa Valley — Calistoga` という 2 段表記は規制上の階層とも整合する。**

🔴 **よって本件では当該シェイプに新たな証拠を足す必要は無く、
「同型の属性でも裏づけが取れる場合がある」という反例として記録する。**
🔒 **番号は開かない。**

---

### 既存の族に該当するもの（**新しい番号は開かない**）

- **`S-2`（引用符の埋め込み）** — 🔍 **OBP 3・4 行目の生印字は `"The Montelena Estate," Calistoga Cabernet Sauvignon` で、
  **二重引用符とカンマがキュヴェ名の内側に入っている**（intake の `source_wine_raw` で確認）。
  **intake の `_parts.label` は `The Montelena Estate` と正しく剥がせている**が、
  **`_parts.printed_rest` が `Calistoga Cabernet Sauvignon` となり、`appellation` が `calistoga`、
  `varietal` が `cabernet sauvignon` に分解されている。`S-2` と同種である。**
- 🔴 ⚠️ **1・2 行目について、intake は `_parts.label = null` / `appellation = "napa valley"` と分解し、
  evidence に「`'Chateau Montelena'` の canonical キュヴェ 1 件に一致無し: `'napa valley'`」と記録している。**
  🔴 **すなわち matcher は `Napa Valley Chardonnay` を「産地＋品種」と読んで label を空にしたが、
  実際には `Napa Valley Chardonnay` が生産者の製品名そのものである。**
  **これは「産地語を含む製品名」を分解しすぎる、という構造であり、
  既存の `C-4`（識別語を持たないキュヴェ名）とは向きが逆である。**
  🔒 **新しい族に見えるが、番号は開かない。形だけ記述して CTO の判断に委ねる。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY**）

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の運営者名** | ✅ 🔴 **合格。**`https://montelena.com/terms-of-service/` に「**The website located at www.montelena.com (“Site”) is owned by and operated by Chateau Montelena Winery**」と明記。**Copyright Agent 宛先も `Chateau Montelena Winery, 1429 Tubbs Lane, Calistoga, CA, 94515, Attn: Copyright Agent and General Counsel`** |
| **(b) 非関連の免責表示が無い** | ✅ **合格。**「ファンサイト」「非公式」の類の表記は全ページに無い。**全ページ末尾は `© 2026 Chateau Montelena Winery`** |
| **(c) 公的資料と一致する所在** | ✅ 🔴 **合格。**サイト掲出の **`1429 Tubbs Lane, Calistoga, CA 94515`** が、**公式テクニカルシート 7 点の版面下部、bio PDF 3 点の版面下部、生産者 press release の dateline（`Calistoga, CA`）と完全一致。**<br>🏛 **さらに連邦官報の最終規則が「James P. “Bo” Barrett of Chateau Montelena, **a Calistoga, California, winery and vineyard**」と記述しており、公的文書側からも所在が裏づけられる** |
| **(d) 商業・法務フッターの整合** | ✅ **合格。**California Prop 65 警告、CCPA、GDPR、Privacy Policy、Accessibility Statement、Shipping、Terms and Conditions、`Do Not Sell My Personal Information`、21 歳未満の入店不可の明示、WooCommerce の実在する決済導線まで完備 |
| **年齢ゲート** | ✅ **本ドメインでは静的取得に年齢ゲートは掛からなかった**（robots.txt / sitemap / 商品ページ / PDF いずれも直接取得できた） |
| **bot 検出の兆候** | **無し。**`montelena.com` 側の CAPTCHA・チャレンジには一度も遭遇していない |

🔴 **本調査で `NOT_THE_PRODUCER_*` として退けたサイトは無い。ドメインの取り違え候補にも遭遇しなかった。**
（**WebSearch は URL の発見にのみ用い、検索結果の要約文は事実として一切採用していない。**）

**公式ドメイン外の資料 2 点の扱い（明示する）**

| 資料 | ドメイン | 判定 |
|---|---|---|
| 📄 **`Montelena-Vandal-Vineyard-Press-Release.pdf`**（2025-03-18） | **`vintus.com`**（米国の輸入・マーケティング会社） | 🔴 **生産者著作として使用。**根拠：**dateline が `Calistoga, CA`、本文が「Chateau Montelena … **proudly announces**」の一人称、CEO と winemaker の直接引用、末尾に `About Chateau Montelena` の会社紹介欄。**<br>⚠️ **ただし生産者ドメインでは配信されていない。本書では `Alfred L. Tubbs` / `CEO & Owner` / Carneros 取得の 3 点にのみ用い、`📄` を付して区別した** |
| ⚠️ **Wilson Daniels のポートフォリオ追加リリース**（2025-11-04） | **`wilsondaniels.com`**（米国の全国卸） | ⚠️ 🔴 **事実の典拠として採用しない。**「solar power」「conscious farming」等の記述は生産者資料で裏づけられなかったため、**§Staff Notes ⚠️ ④ で「言ってはいけないこと」に回した** |

### 一次資料（**`montelena.com` および同ドメイン配信の公式 PDF・公式画像**）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt` → `sitemap_index.xml`** | **`page-sitemap.xml`（42 URL）/ `product-sitemap.xml`（54 URL）/ `product_cat-sitemap.xml`（14 URL）。Yoast SEO + WooCommerce の WordPress サイト** |
| 🔴 **`/wp-json/wp/v2/pages?per_page=100`** | 🔴 **全 46 頁を列挙。**→ **沿革・畑・栽培・持続可能性のページが 1 枚も存在しないことの機械的な証明。**存在するのは Shop / Visit / Membership / In the News / Resources / Style（trade 素材）/ 法務ページのみ |
| **`/wp-json/wc/store/v1/products?per_page=100`** | **商品名・価格・パーマリンクを機械取得。**Estate Cabernet 2021・2022 = **$200**、Napa Valley Cabernet 2022 = **$85**、Napa Valley Chardonnay 2023 = **$75**、**2011 Montelena Estate Cabernet Sauvignon = $250（library 再リリース）** |
| 🔴 **`/resources/`（Trade Downloads）** | 🔴 **本ドシエの中核。**bio 3 点（Bo Barrett / Matthew Crafton / Tucker Spear）、Tasting Notes 一覧（Estate Cabernet 2006–2019・2021／Chardonnay 2012–2023／Napa Valley Cabernet 2017–2019・2021–2023）、Bottle Shots 一覧、Estate Vineyard Maps、**Estate Weather Summaries 1972–2025（54 年分）**、PDF リンク 58 本 |
| 🔴 **`2023-Napa-Valley-Chardonnay.pdf`** | 🔴 **OBP 1 行目の技術仕様。**100% Chardonnay／13.9%／収穫 9/8–10/10 2023／瓶詰 2024/7/23–8/1／**10 か月 100% French Oak 新樽 25%**／リリース 2025 年 11 月／**サーヴィス 55°F 指定・デカンタ不要** |
| 🔴 **`2022-Napa-Valley-Cabernet-Sauvignon.pdf`** | 🔴 **OBP 2 行目。**85% CS / 14% Merlot / 0.5% PV / 0.5% CF／14.2%／収穫 9/8–24 2022／瓶詰 2024/4/1–9／**16 か月 French and Eastern European Oak 新樽 30%**／リリース 2025 年 4 月 |
| 🔴 **`CS21-Notes.pdf`** | 🔴 **OBP 3 行目。**表題 `estate cabernet sauvignon / CALISTOGA, 2021`／94.1% CS / 4.9% CF / 1% PV／14.1%／収穫 9/4–10/8 2021／瓶詰 2023/7/27–28／**22 か月 100% French Oak 新樽 45%**／リリース 2025 年 3 月／**熟成能力 30 年以上** |
| 🔴 **`CHM_WN_ME-CS-2011_Trade.pdf`** | 🔴 **OBP 4 行目。**表題 `2011 Montelena Estate Cabernet Sauvignon`／`Notes from the Winemaker, Matt Crafton, December 2014`／99% CS / 1% CF／13.5%／収穫 9/29–10/29 2011／瓶詰 2013 年 12 月／**22 か月 100% French 新樽 33%**／リリース 2015 年春 |
| **`2019-Estate-Cabernet-Sauvignon.pdf`** | **99% CS / 0.5% PV / 0.5% CF。**→ **「100% CS ではない」ことの 3 例目** |
| 🔴 **`CHM_SH_VydMap_2024-04-ADA-3.pdf`** | 🔴 **表題 `The Montelena Estate Vineyard / CALISTOGA · NAPA VALLEY`。**3 土壌帯（ALLUVIAL / VOLCANIC / SEDIMENTARY）の定義と各々のワイン特徴、区画記号・品種・植樹年、`JADE LAKE` / `BEE HILL` / `APOLLO` / `RESERVOIR` |
| 🔴 **`CHM_Bio_BoBarrett-4.pdf`** | 🔴 **1972 年の家族取得、Fresno State、1982 年 winemaker、2013 年 CEO、`his father, and winery founder, Jim Barrett`** |
| 🔴 **`Matthew-Crafton-President-Winemaker-Bio.pdf`** | 🔴 **2003 年 UVA 経済学、2008 年 UC Davis、同年 Enologist として入社、2014 年 winemaker、2025 年 12 月 President。「largest replant of the Montelena Estate in five decades」「deepened its sustainability initiatives」「a world-class estate vineyard in Carneros」「Calistoga Estate's gravelly benches, volcanic soils」** |
| 🔴 **公式ボトルショット画像**（`CHM_BTL_CS-Estate-2011.jpg` / `CHM_EstateCab_Straight_2021-scaled.jpg` / `2022_CHM_NapaCab_Straight-scaled.jpg` / `2023_CHM_Chardonnay_Straight-scaled.jpg`） | 🔴 **ラベル実読。**<br>**Estate Cabernet（2011・2021 とも）= 金帯 `THE MONTELENA ESTATE` ＋ `CHATEAU MONTELENA` ＋ `ESTABLISHED 1882` ＋ 銅版画 ＋ `2011`/`2021` ＋ `CABERNET SAUVIGNON` ＋ `CALISTOGA · NAPA VALLEY`**<br>**Napa Valley Cabernet 2022 = 金帯なし ＋ `2022` ＋ `Cabernet Sauvignon`（イタリック体）＋ `NAPA VALLEY`**<br>**Napa Valley Chardonnay 2023 = 金帯なし ＋ `2023` ＋ `Chardonnay` ＋ `NAPA VALLEY`** |
| ✅ **`/wine/judgment-of-paris-chardonnay-gift-set/`** | 🔴 **`Judgment of Paris` に関する唯一のまとまった公式記述。**「Founded in 1882…」「Montelena's 1973 Chardonnay prevailed at the Judgment of Paris」「50th Anniversary logo」 |
| ✅ **`/membership/estate/`** | 🔴 **「our flagship wine, the Estate Cabernet Sauvignon」。2023 Estate は 2026 年 11 月リリース予定、会員先行 6 本 $990／通常 $1,350** |
| ✅ **`/visit/visitor-experiences/`** | **`The Montelena Estate Collection`（Estate Cabernet 4 ヴィンテージ比較・$125）、`Story Behind the Bottle`（「140+ year legacy」）、`Legacy in the Glass`、`Vineyard Tour & Tasting`** |
| ✅ **`/terms-of-service/` / `/privacy-policy/`** | **真正性の検証。運営者名・所在・Copyright Agent** |
| ✅ **`/resources/us-distributors/`** | **州別の卸一覧。通常流通のある生産者であることの確認** |

### 🏛 公的登録簿・規制一次資料

| 資料 | 取得した情報 |
|---|---|
| 🔴 🏛 **eCFR 27 CFR § 9.209（`Calistoga`）** | 🔴 **AVA の定義、`term of viticultural significance` 指定、承認地形図 4 葉、境界の全記述、経過措置(d)、出典注記 `[T.D. TTB-83, 74 FR 64612, Dec. 8, 2009, as amended by T.D. TTB-196, 89 FR 83434, Oct. 16, 2024]`** |
| 🔴 🏛 **Federal Register `E9-29217`（`74 FR 64602`〜、2009-12-08 公布 / 2010-01-07 施行）** | 🔴 **「entirely within the existing Napa Valley viticultural area described in 27 CFR 9.23」／申請者が `James P. “Bo” Barrett of Chateau Montelena` であること／Swinchatt 報告による地質・土壌・気候の記述／隣接 AVA（St. Helena § 9.149、Diamond Mountain District § 9.166）との境界関係** |
| 🔴 🏛 **eCFR 27 CFR § 4.26（`Estate bottled`）** | 🔴 **3 要件の全文、`Controlled by` の定義（3 年以上のリース等）、(d)「No term other than `Estate bottled` may be used…」** |
| 🏛 **Napa Green `participating-members`** | 🔴 **server-rendered の社名 73 件を機械抽出。`Montelena` = 0 件、`Barrett` = 0 件** |

### 取得できなかったもの / 存在しなかったもの

- 🔴 ⚠️ **🏛 TTB Public COLA Registry が CAPTCHA でゲートされていた。**
  **`publicSearchColasBasic.do` は F5/Shape 系の bot 防御（`bobcmn` / TSPD）を返し、
  ページ内に captcha 画像・音声・`name="answer"` 入力欄が実在した。突破は試みていない。**
  → **本書は TTB 承認ラベルの記録（brand name / fanciful name / class-type / alcohol / 承認日）を 1 件も持たない。**
  → **⚠️ ゲートは「ラベルが存在しない」ことの証拠ではない。**
- 🔴 **`montelena.com` に沿革・畑・栽培・持続可能性・スタッフ紹介のページが存在しない**（WP 全 46 頁で確認）。
- 🔴 **1882〜1972 年の 90 年間について、公式の記述が 1 行も無い。**
- 🔴 **Estate Cabernet と Napa Valley Cabernet の `2020` が、公式の Tasting Notes / Bottle Shots のいずれの一覧にも無い。理由の記述も無い。**
- 🔴 **裏ラベル画像を取得できていない。`ESTATE BOTTLED` の有無・瓶詰者表示・政府警告文が未確認。**
- ⚠️ **CCOF 会員名簿は JS 描画で読めなかった**（既知の認証生産者名での対照実験でも 0 件）。
- ⚠️ **USDA Organic INTEGRITY は Blazor の JS シェル。`POST /integrity/api/OperationSearch` は `400`。**
- ⚠️ **Demeter USA / Fish Friendly Farming の機械可読な参加者名簿を特定できなかった。**
- ⚠️ **公式テクニカルシートに、発酵容器・発酵温度・マロラクティック・酵母・pH / TA / Brix・生産本数が一切無い。**
- ⚠️ **2025 年取得の Carneros の畑の固有名が press release 本文に書かれていない**（PDF のファイル名にのみ `Vandal` の語）。
- ⚠️ **畑の総面積（エーカー数）が公式のどこにも書かれていない。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical: `migration/out/export/db_wine_canonical.json`（928 レコード）を機械走査。
文字列 `Montelena` を含むレコードは `chateau-montelena-estate` の 1 件のみ。**
🔍 **OBP: `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` に 4 行。
`source_row_id` = `obp-beverage-2026-08:955849bb52` / `:0864372f37` / `:3043afedd5` / `:2cfe4fe0bf`。
4 行すべて `match_state = unresolved`・`confidence = 0.0`・`producer_state = exact`。**
⚠️ **本書の「解決済み件数」はすべて `obp_intake_normalized_20260804.json` から取ったものであり、
`research/out/t-01/mapping.json` は参照していない**（両者が食い違うことは既知のため、出所を明記する）。
🔒 **canonical・`REGISTER.md`・intake のいずれも編集していない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | **High** | 🔴 **運営法人名・所在・電話・FAX が法務ページと全 PDF で一致。CEO・President&Winemaker・営業責任者の氏名と就任年がすべて公式 bio で確定。**⚠️ **創業者名のみ生産者ドメイン外の press release 由来** |
| **Overview** | **High** | **設立年・1976 年の位置づけ・flagship がどれか・畑の自己規定が公式で取れた** |
| 🔴 **History** | 🔴 **Low-Medium** | 🔴 **公式サイトに沿革ページが存在しない。**1882 / 1972 / 1982 / 2008 / 2013 / 2014 / 2025-12 は公式 bio で確定し、2003〜2010 の AVA 申請は 🏛 連邦官報で確定したが、**1882〜1972 の 90 年間が完全な空白** |
| 🔴 **Location** | 🔴 **High** | 🔴 **AVA の法的定義・制定日・Napa Valley との入れ子関係・申請者が 🏛 で確定。畑の土壌 3 帯と区画・植樹年が公式マップで確定。**⚠️ **畑の面積のみ不明** |
| 🔴 **Farming** | 🔴 **Low** | 🔴 **本ドシエ最大の弱点。造り手が栽培について何も公表していない。**🏛 **Napa Green 名簿には不在（読めた登録簿）だが、CCOF・USDA INTEGRITY は読めず判定不能。**→ **⚠️ で全面的に塞いだ** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **OBP 4 ヴィンテージすべての公式テクニカルシートを取得。セパージュ・アルコール・収穫日・瓶詰日・樽（月数／産地／新樽率）・リリース時期が確定。**⚠️ **発酵・MLF・分析値は完全に不在** |
| 🔴 **Style** | 🔴 **High** | 🔴 **OBP 4 本すべてに醸造家署名つきの公式ノート。さらに 1972–2025 の 54 年分の公式 Estate Weather Summaries を取得** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **4 行すべての実体・公式名・ラベル表記・技術仕様・蔵出し価格を確定。ラベル画像で `The Montelena Estate` の実在を実証** |
| **Canonical Conflict** | **High** | 🔴 **gap は 928 レコードの機械走査で確定。記述の矛盾 4 点はいずれも公式 PDF との直接照合** |
| **Staff Notes** | **High** | ⚠️ **14 項目。🔴「The Montelena Estate は店の表記ゆれ」「100% CS」「オーガニック」「Estate bottled」「Bottle Shock」「1882 年から Barrett 家」「2020 は造らなかった」「カリストガはナパとは別」の 8 つの誤りを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を超過。実感としては 80% 前後）。** | **OBP 4 本すべてについて、公式名・ラベル表記・セパージュ・樽・アルコール・造り手のノート・蔵出し価格・年の性格を言える。産地は連邦規則まで遡って言える。**<br>🔴 **欠けているのは ① 栽培（造り手が公開していない）、② 1882–1972 の歴史、③ 醸造工程の分析値、④ TTB ラベル記録。**<br>**いずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。** |

**reached_70: YES（~80%）。**

---

## Open Questions

1. 🔴 **OBP 3・4 行目の裏ラベルに `ESTATE BOTTLED` の表示があるか（実ボトル案件）。**
   🏛 **27 CFR § 4.26 の法定用語であり、表ラベルの `THE MONTELENA ESTATE` は
   同条(d)がいう「combined growing and bottling conditions を示す語」に当たるのか否かで解釈が分かれうる。**
   → **裏ラベルの瓶詰者表示（`Produced and Bottled by` / `Grown, Produced and Bottled by` / `Estate Bottled by` のいずれか）を
   実物で確認する。**
   → 🔴 **確認できるまで、staff は Estate bottled を主張しない。**
2. 🔴 **canonical に載せるときの `name` をどれにするか。**
   **公式が同時に 3 通り使っている：ラベル `THE MONTELENA ESTATE` + `CABERNET SAUVIGNON`、
   EC/テクニカルシート `Estate Cabernet Sauvignon`、WooCommerce 内部名 `Montelena Estate Cabernet Sauvignon`。**
   🔴 **さらに OBP の印字は 4 番目の形（`"The Montelena Estate," Calistoga Cabernet Sauvignon`）である。**
   → 🔒 **どれを canonical 名にし、残りを alias にするかは設計判断。本書では決めていない。**
3. 🔴 **1882 年から 1972 年までの 90 年間。**
   **公式サイトに記述が皆無。禁酒法期の扱い、中間の所有者、1968–1972 年の再建、
   1973 年のシャルドネを造った醸造家が誰であったか —— いずれも本調査では造り手の言葉が取れなかった。**
   → **蔵への直接照会、または蔵が過去に公開していた沿革ページの提供が要る。**
4. 🔴 **Estate Cabernet と Napa Valley Cabernet の `2020` が公式資料一覧に無い理由。**
   **Tasting Notes・Bottle Shots のいずれも 2019 の次が 2021。公式は理由を書いていない。**
   → **「造らなかった」と断定してはならない。蔵への照会案件。**
5. ⚠️ **2025 年に取得した Carneros の畑の正式名。**
   **press release 本文に名前が無く、PDF のファイル名にのみ `Vandal` の語がある。ファイル名は根拠にならない。**
6. 🔴 **🏛 TTB COLA の再試行。**
   **本調査では CAPTCHA でゲートされた。開けば brand name / fanciful name / 表示産地 / class-type /
   alcohol / 承認日が確定し、Open Question 1 と 2 の双方に直接の答えが出る。**
   **⚠️ 同一バッチ内でも生産者によって開いたり閉じたりするため、日を改めた再試行に価値がある。**
7. ⚠️ **栽培の実態。**
   **造り手は「sustainability」を 2 回口にするだけで、制度名も実務も公開していない。**
   🏛 **Napa Green 名簿には不在。CCOF・USDA INTEGRITY・Demeter・FFF は読めなかった。**
   → **蔵への直接照会、または読める形の登録簿を特定することが要る。**
8. ⚠️ **醸造工程の空白 —— 発酵容器・発酵温度・マロラクティック発酵の有無・酵母・pH / TA / Brix・生産本数。**
   **4 ヴィンテージの公式シートすべてで完全に空白。**
9. ⚠️ **畑の総面積。**
   **`The Montelena Estate Vineyard` のエーカー数が公式のどこにも書かれていない。**
   **（比較のため：2025 年に取得した Carneros の畑だけは `73 acre` と明記されている。）**
10. ⚠️ **canonical の `vintage = '—'` をどう扱うか。**
    🔴 **本生産者は Estate Cabernet だけで 1992〜2023 の 20 ヴィンテージ超を自社 EC で現に販売しており、
    `cuvée × vintage` の粒度が無ければ OBP の 2021 と 2011 を永久に分離できない。**
    → 🔒 **canonical への書き込みは本書では行っていない。昇格可否は Akio / CTO 判断。**
11. ⚠️ **`Judgment of Paris` の詳細。**
    **造り手が公式に書くのは「1973 年のシャルドネが prevailed / triumphed した」までで、
    出品銘柄・順位・審査員・その後の再現試飲について公式の記述が一切無い。**
    → **2026 年が 50 周年であり、記念関連の公式資料が今後出る可能性が高い。再訪の価値がある。**
