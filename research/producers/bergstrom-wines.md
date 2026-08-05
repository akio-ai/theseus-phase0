# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件も存在しない。**
> 本書は昇格前の研究記録であり、**canonical も OBP も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者の公式サイトで確認**（一次資料）——
>    本ドシエでは **`bergstromwines.com`（WordPress / Avada）**、
>    および **同社の Commerce7 ストアフロント API `api.commerce7.com/v1/…/bergstrom-wines`（＝生産者自身の商品台帳）**、
>    および **生産者が自ら公開する `Vintage Guide`（PDF・Updated 02/2025）**
> `📄` 単一の非公式資料のみ（**本書では `dundeehills.org`（同業組合）の 1 点のみ。事実の典拠には使っていない**）
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `🏛` **公的登記・認証機関・産地規制**（本書では **TTB COLA 公開レジストリ**／**Demeter U.S.A. Biodynamic Directory**／
>    **LIVE Certified**／**USDA Organic INTEGRITY Database**／**eCFR 27 CFR Part 9**）
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://bergstromwines.com/`（EN のみ）**
> 走査元: ✅ **`robots.txt` が指す `https://bergstromwines.com/sitemap_index.xml`**（Yoast 生成・10 サイトマップ）
>
> 🔴 **本ドシエ最大の収穫 ①** —— **認証の問題に、生産者自身の言葉で決着がついた。**
> **5 つの自社畑ページすべてが、`Farming Style` 欄に**
> 「**0% conventional, non-certified BD/regenerative-ecological**」——
> **すなわち「慣行栽培ゼロ、ただし *非認証* のビオディナミ／再生型」と明記している。**
> 🏛 **これは登記側でも裏が取れた。Demeter U.S.A. の Biodynamic Directory の `B` 一覧に Bergström は無い**
> （**同じ一覧に Willamette の Brick House Vineyards・Brooks Wine・Anacreon・Montinore Estate は載っている＝
> オレゴンのワイナリーが対象外なのではなく、Bergström が居ないということ**）。
> 🔴 **一方で `family.html` は「70 acres of biodynamic, estate monopole」と書き、
> Josh 本人のブログは「We are Biodynamic farmers」と一人称で書いている。**
> → **「ビオディナミで農をやっている」は公式。「ビオディナミ認証を受けている」は公式に否定されている。この 2 つを混ぜないこと。**
>
> 🔴 **本ドシエ最大の収穫 ②** —— 🏛 **TTB COLA 公開レジストリが今回は素通しで取れた。**
> **法人格は `BERGSTROM WINES, LLC`、TTB Basic Permit は `BW-OR-260`。**
> **同 permit で 108 件の COLA が登録されており、うち 88 件を本調査で復元した。**
> **キュヴェの `Fanciful Name` はここで一次的に確定できる —— `SILICE` / `CUMBERLAND RESERVE` /
> `BERGSTROM VINEYARD` / `LE PRE DU COL VINEYARD` / `LA SPIRALE (VINEYARD)` / `WINERY BLOCK` ほか。**
> 🔴 **そして `DUNDEE HILLS` という Fanciful Name は 88 件中 1 件も無い。**
>
> 🔴 **本ドシエ最大の収穫 ③** —— **OBP 5 行目「Dundee Hills Pinot Noir / 2023 / $440」の正体。**
> ✅ **生産者の 5 つの自社畑のうち、Dundee Hills AVA にあるのは `Bergström Vineyard` ただ 1 つ。**
> ✅ **商品台帳で `appellation: "Dundee Hills"` を持つ 2023 年の赤は `2023 Bergström Vineyard Pinot Noir` ただ 1 つ。**
> 🔍 **小売 $150 に対し OBP $440 ＝ 2.93 倍。同じ倍率は Cumberland Reserve 2023（$55 → $160 ＝ 2.91 倍）と一致する。**
> → 🔴 **`2023 Bergström Vineyard Pinot Noir` である蓋然性が非常に高い。**
>   **ただしメニューはキュヴェ名を印字しておらず、本書は断定しない。** → §Open Questions 1（**実ボトル確認事項**）

---

## Identity

### 🔴 生産者名 —— canonical に何と書くべきか

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Bergström`**（ウムラウトあり・`Wines` は付かない） |
| **公式サイトの自己表記** | ✅ **`Bergström Wines`**。WordPress の site `name` フィールドが **`Bergström Wines`**、`description` が **`Exquisite wines in the Willamette Valley of Oregon`**（`/wp-json/` ルート） |
| **全ページの `<title>` 接尾** | ✅ **`… - Bergström Wines`** |
| ⚠️ **全ページのフッター著作権表示** | ⚠️ **`© Copyright - Bergstrom Wines`（ウムラウト無し）**。**公式サイト内部で表記が割れている** |
| 🔴 **法人名** | 🏛 **`BERGSTROM WINES, LLC`**（TTB COLA 公開レジストリ・`Brand Name` 欄／`Permit No. BW-OR-260`）。**ウムラウト無し** |
| 🏛 **TTB Basic Permit** | 🏛 **`BW-OR-260`**（`BW` ＝ Bonded Winery、`OR` ＝ Oregon）。**1 permit ＝ 1 事業体。分社構造は本調査では確認されなかった** |
| **Commerce7 テナント slug** | ✅ **`bergstrom-wines`**（商品画像 CDN・API パス） |
| **ドメイン** | ✅ **`bergstromwines.com`** |
| **canonical id** | 🔍 **存在しない。**`producer` に `Bergström` / `Bergstrom` のいずれも 0 件（ASCII 畳み込み一致でも 0 件） |

🔴 **本ドシエの推奨（🔴 DO NOT EXECUTE）**

- canonical の `producer` は **`Bergström Wines`**（**ウムラウト付き・`Wines` 込み**）。
  **根拠は WordPress の site name と全ページの `<title>` であり、これが生産者自身の一次表記である。**
- **エイリアスとして `Bergström` / `Bergstrom Wines` / `Bergstrom` の 3 形を保持する。**
  **OBP の印字は `Bergström` 単体、自社フッターと TTB 法人名は `Bergstrom`。どちらも実在する形である。**
- **id（slug）は ASCII 畳み込みで `bergstrom-wines`。**
  🔍 **OBP intake も `ö → o` に正規化している。したがって「id は ASCII、表示名はウムラウト」という
  既存の運用（`C-1` アクセント系）と同じ扱いで足りる。新しい番号は開かない。**

⚠️ 🏛 **ウムラウトについて、TTB を根拠に「公式はウムラウトを使わない」と結論してはいけない。**
**TTB のレジストリは diacritic を保持できる —— 同じ `BW-OR-260` の登録に
`BERGHÖUSE`（ö あり）と `SALUD CUVÉE`（É あり）が実在する。**
**にもかかわらず Brand Name 欄は 88 件すべて `BERGSTROM` である。**
**しかしこれは「登録上の法人／ブランド名の欄」であって「ラベルの意匠」ではない。**
**ラベルに ö が刻まれているかは、実ボトルを見ないと確定しない。** → §Open Questions 3

### 人・体制

| | |
|---|---|
| 🔴 **創業者** | ✅ **John Bergström（M.D.）と Karen Bergström。**公式の肩書は **`Founders`** |
| **John** | ✅ **スウェーデンの辺境の伐採村の生まれ。10 代でスウェーデンを離れ渡米。Portland で学び、産婦人科の外科医となる** |
| **Karen** | ✅ **カリフォルニア生まれ。アイリッシュ系アメリカ人の家庭で育ち、正看護師（registered nurse）となる** |
| 🔴 **現当主** | ✅ **Josh Bergström —— `Owner, CEO, & Director of Winemaking`**。**Portland 生まれ** |
| **Josh の学歴** | ✅ **大学ではフランス語・経営・商法・人文学。のち **Beaune の CFPPA** でブドウ栽培・醸造の postgraduate degree** |
| **Josh の実績（公式の自己記述）** | ✅ **これまでに Willamette 域内 125 以上の畑からワインを造ってきた／Willamette Valley Wineries Association の board member を務めた／`Willamette: The Pinot Noir Auction` の創設を主導した／2023 年に **Académie Internationale du Vin** に選出された** |
| 🔴 **共同オーナー** | ✅ **Caroline Bergström —— `Owner, Director of Sales`。ブルゴーニュ Beaune 出身** |
| **Caroline の経歴** | ✅ **Beaune 生まれ。Hospice de Beaune で働き始め、数度の収穫を経て Lycée Viticole でワイン・スピリッツのマーケティングを学ぶ。そこで Josh と出会う。**養蜂家・ハーブティー職人・ジャム作りの手仕事も公式に紹介されている |
| **畑チーム（実名）** | ✅ **Sarah / Nick / Mayo / Félipe / Leo**（2020 年 3 月のブログ `Spring in the Vineyard` で Josh が名指し） |
| **米国の販売代理** | ✅ **`Wilson Daniels` の National Portfolio**（`/trade`・`/contact` の双方に明記） |
| **連絡先（公式に掲出）** | ✅ **Private Tastings `503-554-0468` ／ Wine Club・Business Office `503-554-0463`** |
| ⚠️ **所在地（番地）** | ⚠️ **公式サイト側では取得できていない。**`Map & Directions` ページは JS 埋め込みの空シェルで、本文に住所が無い。<br>📄 **`dundeehills.org`（Dundee Hills Winegrowers Association ＝ 同業組合。生産者公式ではない）は `8115 NE Worden Hill Road, Dundee, Oregon 97115` を掲げている。**<br>🔴 **本書はこれを事実として採用しない。** → §Open Questions 4 |
| **認証** | 🔴 **公式に「非認証」と明記。** → §Farming |

---

## Overview

✅ **オレゴン州 Willamette Valley。1999 年、John Bergström と息子 Josh が創業した一家族の生産者。**
**Pinot Noir と Chardonnay を、Dundee Hills・Chehalem Mountains・Ribbon Ridge の 3 つの AVA にまたがる
5 つの自社畑・計 70 エーカーで栽培する。**

🔴 ✅ **公式が掲げる合言葉は「`1000 Days of Effort`（1000 日の労力）」である。**
「**Bergström Wines の労働倫理は、この家族とチームのマントラに根ざしている。
1 本のボトルを市場に出すまでに、farm・ferment・age・finish で 3 年を要する。**」

🔴 ✅ **農の自己規定（`/farm`、原文）** ——
「**1999 年の畑の開設以来、われわれの estate は 除草剤・農薬・殺虫剤・浸透性化学物質を使わずに farm されてきた。
合成肥料ではなく、堆肥づくりと、ホメオパシー的な薬草・鉱物のお茶による処置を選ぶ。**」

🔴 ✅ **Josh の目標（`/family`、原文）** ——
「**Bergström Wines の始まりから、Josh のヴィジョンは明確だった ——
アメリカ最高の Pinot Noir、Chardonnay、Syrah を造ること、
そして 100% estate-farmed へ 漸進的に 進んでいくこと。**」
→ 🔴 **「100% estate」はまだ達成されていない、と生産者自身が書いている。**
  **実際、買いブドウの畑名キュヴェ（Gregory Ranch / Shea / Temperance Hill / Koosah / Hope Well）が併存する。**
  → §Staff Notes ⚠️ ⑦

🔴 ✅ **ワインの性格を生産者が一文で要約している（`/farm`）** ——
「**われわれのワインは、Pinot Noir と Chardonnay を育てている、海性堆積土と火山性の丘のちがいを辿る
ヴィナスな road map である。地域としての表現は、みずみずしい自然な酸、フレッシュな果実の香りと味わい、
張りのある塩気を帯びたミネラルの芯、そして古く風化した土壌と基盤岩から来る豊かな土と香辛料の性格を持つ。**」

🔍 **THÉSEUS における状態** —— 🔴 **canonical に生産者レコード 0 件・キュヴェ 0 件。**
**OBP 掲載 5 本すべてが `producer_state: unresolved`。本書がこの生産者の最初の記録である。**

---

## History

✅ **公式に専用の年表ページは無い。以下は `/family`・`/farm`・各畑ページ・Vintage Guide・ブログから復元した。**

| 年 | 出来事 |
|---|---|
| **1950**（写真） | ✅ **`John (17), and his mother, Sigrid, 1950`** —— **公式 `/family` の写真キャプション。**🔴 **この `Sigrid` が後年のフラッグシップ Chardonnay の名の由来である** |
| **—** | ✅ **John、スウェーデンの伐採村を出て渡米。Portland で学び、産婦人科の外科医となる** |
| 🔴 **1999** | 🔴 ✅ **Bergström Wines 創業。Josh と Caroline がオレゴンに戻り、最初のヴィンテージを仕込む。**<br>🔴 **同年 `Bergström Vineyard` を植える（Dundee Hills AVA）＝ `The Birthplace of Bergström Wines`**<br>✅ **Vintage Guide の記述は「`First vintage.` 長く冷涼な年で、夏と秋が長引いた。優雅で高酸の Pinot Noir に理想的な条件」** |
| **2001** | ✅ **`Silice Vineyard` 植栽開始（Chehalem Mountains AVA）**<br>⚠️ **畑ページは `Years planted: 2001-2006`、`/place` と商品ページは `Planted 2001` と書く** |
| **2002** | ✅ **`Winery Block` 植栽開始（Chehalem Mountains AVA）**<br>⚠️ **畑ページは `2002-2005`、`/place` は `Planted 2002`** |
| **2005** | ✅ **`La Spirale` 植栽（Ribbon Ridge AVA）** |
| **2006** | ✅ **`Le Pré du Col Vineyard` 植栽（Ribbon Ridge AVA）** |
| 🔴 **2018** | 🔴 ✅ **`La Spirale` を取得。**「**2018 年に取得したこの畑は、Bergström Wines が 100% estate-grown のワイナリーになるという
—— 創業ヴィンテージ以来の野心 —— に向けた転回点となった**」 |
| **2019** | ✅ **`La Spirale` の農法を「0% conventional, non-certified BD/regenerative-ecological」に切り替え（`since 2019`）**<br>🔴 **他の 4 畑は `since inception`。La Spirale だけが取得後の転換である** |
| 🔴 **2020** | 🔴 ✅ **畑に羊を導入。**「**`The Vine Ewes` と呼ばれる群れが、地元の羊飼いに率いられて数週間わが畑に住んだ。
春のカバークロップを食み、食みながら土を肥やした**」（Josh 署名・2020 年 4 月 10 日）<br>✅ **Vintage Guide：2020 は「9 月下旬の森林火災の影響で谷の大半にとって complicated な年。早摘みと蔵での厳格な declassification のおかげで、われわれの蔵は生き生きとした明るいワインを生んだ」** |
| 🔴 **2021** | 🔴 ✅ **Josh の 25 回目のオレゴン収穫。**`heat dome` で華氏 115 度が 3 日間（**前の記録は 2003 年の 106 度**）。**ヴェレゾン中の 2 度目の熱波で「西側キャノピーの果実の 10〜15% を失ったと見積もる」** |
| **2023** | ✅ **Josh が `Académie Internationale du Vin` に選出される** |
| **2024–2025** | ✅ **新しい畑名 `Koosah Vineyard`（Eola-Amity Hills）が商品台帳と COLA に登場。`Ekollon`（スウェーデン語で「どんぐり」）も 2024 年に COLA 登録・上市**<br>✅ **2024 年、Josh と Caroline の 25 周年を記念して `Cuvée Caroline` を一度きりのボトリングとして発売** |

---

## Location

| | |
|---|---|
| **Country** | ✅ **United States** |
| **State** | ✅ **Oregon** |
| **Region** | ✅ **Willamette Valley**（🏛 **27 CFR § 9.90 `Willamette Valley` として連邦法典に AVA が定義されている**） |
| 🔴 **自社畑の総面積** | ✅ **70 acres**（`/farm`・`/family` とも「70 acres」）<br>⚠️ **各畑ページの数字を足すと 13＋2＋22＋16＋14 ＝ 67 acres。3 acres 合わない** → §Staff Notes ⚠️ ⑥ |
| 🔴 **自社畑の数** | ✅ **5**（`Bergström Vineyard` / `Winery Block` / `Silice` / `Le Pré du Col` / `La Spirale`） |
| 🔴 **またがる AVA** | ✅ **Dundee Hills / Chehalem Mountains / Ribbon Ridge**（**いずれも Willamette Valley の中**） |
| **買いブドウの畑（公式商品台帳より）** | 🔍 **Gregory Ranch（Yamhill-Carlton）／Shea Vineyard（Yamhill-Carlton）／Temperance Hill（Eola-Amity Hills）／Koosah Vineyard（Eola-Amity Hills）／Hope Well／Croft Vineyard／Wren Vineyard／Nysa Vineyard（Dundee Hills・2004）／Arcus Vineyard（2000）** |

### 🔴 ✅ 自社畑 5 つ —— 公式の畑ページが数値で開示している

| 畑 | AVA | 植栽年 | 面積 | 標高 | 土壌 | 密度 | 品種 |
|---|---|---|---|---|---|---|---|
| 🔴 **Bergström Vineyard** ⭐OBP5 | **Dundee Hills** | **1999** | **13 acres** | **350–380 ft** | **玄武岩の上の火山性粘土（volcanic clay on Basalt）** | **2,200–5,000 vines/acre** | **Pinot Noir, Chardonnay** |
| **Winery Block** | **Chehalem Mountains** | **2002–2005** | **2 acres** | **400 ft** | **砂岩基盤の上の深い海成堆積砂** | 🔴 **5,000 vines/acre** | **Pinot Noir, Chardonnay** |
| 🔴 **Silice** ⭐OBP2·3·4 | **Chehalem Mountains** | **2001–2006** | ⚠️ **14 acres** | **400 ft** | 🔴 **砂 70%。砂岩基盤まで 15–20 ft の深さ** | **2,200–5,000 vines/acre** | **Pinot Noir, Chardonnay** |
| **Le Pré du Col** | **Ribbon Ridge** | **2006** | **16 acres** | **385–400 ft** | **頁岩・シルト岩の上の海成堆積土** | ⚠️ 記載無し | **Pinot Noir, Chardonnay** |
| **La Spirale** | **Ribbon Ridge** | **2005**（取得 2018） | **22 acres** | **400–450 ft** | 🔴 **頁岩・シルト岩の上に、識別可能な 14 種類の海成堆積土** | ⚠️ 記載無し | **Pinot Noir, Chardonnay, Syrah** |

⚠️ **`Silice` の面積は公式内部で食い違う。**
**畑ページ（`/farm/silice-vineyard`）は `Acres: 14`。
一方、同社の商品ページの畑解説は「この `20-acre` の畑は 4 つの起伏する砂の丘に広がる」と書く。**
→ **どちらも生産者公開の資料であり、本書は優劣を決めない。** → §Staff Notes ⚠️ ⑥

### ✅ 畑ごとの土地の性格（公式の言葉）

- 🔴 **`Bergström Vineyard`** ——「**テラコッタの、焼けた大地の円形劇場を思わせる、このボウル型の畑は、
  冷涼気候 Pinot Noir にとってアメリカで最も名高い appellation のただ中に理想的に据えられている。
  真南を向き、オレゴンの夏の陽を浴び、南西の Van Duzer 海岸風の隙間から吹き込む冷たい海風から守られている。**」
- 🔴 **`Silice`** ——「**フランス語の `Silica`（シリカ）に因む。Chehalem Mountains AVA でわれわれの最も砂の多い畑。
  6000 万年前に遡る砂質土は、先史時代には巨大な砂丘か浜辺だったのだろう。
  砂の含有率は驚くべき 70%、それが圧密された砂岩の基盤まで 15〜20 フィート続く。
  Calkins Lane の上に位置し、終日の陽光と一年中の風を受ける。**」
- **`Winery Block`** ——「**わずか 2 エーカー。オレゴンの多くの区画の 2 倍以上の 5,000 樹/エーカーで植えられている。
  この畑の密な隊形は、Caroline の故郷と Josh の学びへの敬意である。**」**大きさと密度ゆえ、完全に手作業でのみ farm される。**
- **`Le Pré du Col`** ——「**Ribbon Ridge AVA の玄関口。この細く、古い、海性の丘は
  6000 万年前の砂の海底からオレゴン屈指のワインを生んできた。北と南の 2 つの区画を、
  ダグラスファーの老木の並木が分けている。**」
- **`La Spirale`** ——「**`渦（the vortex）`の意。創造と生命のエネルギーという普遍の力を象徴する。
  南向きにゆるく西へ傾く、長くうねる砂の斜面で、三方を森に囲まれている。**」

### 🏛 AVA の入れ子関係 —— **これは矛盾ではない**

🏛 **eCFR で確認できた 27 CFR Part 9 Subpart C の該当条項（条名の実在のみ）**

| 条 | AVA |
|---|---|
| **§ 9.90** | **Willamette Valley** |
| **§ 9.180** | **Dundee Hills** |
| **§ 9.182** | **Ribbon Ridge** |
| **§ 9.205** | **Chehalem Mountains** |

✅ **生産者自身が `/farm` で明示している** ——
「**Oregon's Willamette Valley の中の Dundee Hills、Chehalem Mountains、Ribbon Ridge という
American Viticultural Areas (AVAs)**」

🔴 **したがって OBP の「Willamette Valley Pinot Noir」（Cumberland Reserve）と
「Chehalem Mountains Pinot Noir」（Silice）と「Dundee Hills Pinot Noir」が
同じ `WILLAMETTE` セクションに並んでいるのは、正常である。**
**Chehalem Mountains も Dundee Hills も Ribbon Ridge も、Willamette Valley AVA の *内側* にある。**
**広い AVA を名乗るか狭い AVA を名乗るかは、ワインごとの選択であって、矛盾ではない。**
→ 🔴 **ここから canonical conflict を作らないこと。** → §Canonical Conflict ③

⚠️ **ただし本調査は、境界の条文そのものを取得できていない。**
**`cfr-9.90.html` / `cfr-9.180.html` / `cfr-9.182.html` / `cfr-9.205.html` はいずれも 0 バイトで、
取得できたのは eCFR の目次構造（条名の実在）のみである。**
**入れ子関係の主張は「生産者自身の記述 ✅ ＋ 条名が連邦法典に実在すること 🏛」までで支えており、
条文の境界記述で検証したわけではない。** → §Open Questions 5

---

## Farming

🔴 **本節は本ドシエで最も強い部分である。生産者は 5 つの畑すべてについて `Farming Style` を 1 行で公表している。**

### 🔴 🏛 認証 —— **「非認証のビオディナミ」で確定**

🔴 ✅ **5 つの畑ページすべてに、同一の書式で次の 1 行がある。**

| 畑 | `Farming Style`（原文ママ） |
|---|---|
| **Bergström Vineyard** | **`0% conventional, non-certified BD/regenerative-ecological since inception`** |
| **Winery Block** | **`0% conventional, non-certified BD/regenerative-ecological since inception.`** |
| **Silice** | **`0% conventional, non-certified BD/regenerative-ecological since inception.`** |
| **Le Pré du Col** | **`0% conventional, non-certified BD/regenerative-ecological since inception`** |
| 🔴 **La Spirale** | 🔴 **`0% conventional, non-certified BD/regenerative-ecological since 2019`** |

🔴 **`BD` は biodynamic の略。すなわち生産者は自ら「認証を受けていないビオディナミ」と書いている。**
🔴 **`La Spirale` だけが `since 2019` であり、他の 4 畑の `since inception` と違う。**
**取得が 2018 年だから、転換はその翌年からである。**
→ 🔴 **「全畑が創業以来ずっと同じ農法」と言わないこと。** → §Staff Notes ⚠️ ④

### 🏛 登記側での検証 —— **問い合わせた先と、返ってきたもの**

| 🏛 レジストリ | 何を照会したか | 返ってきたもの | 判定 |
|---|---|---|---|
| 🔴 **Demeter U.S.A. — Biodynamic Farm and Product Directory**（`Browse by Member Name`） | **`A` / `B` / `C` の会員名一覧** | 🔴 **`B` の一覧は完全に取得できた。掲載は Bar Agricole / Baron Longo / BD Bees / Beaver Creek Vineyards / Beckmen Vineyards / Belle Colline Vineyard LLC dba Anacreon Winery（Newberg, OR）/ Benziger Family Winery / Black Lamb Wine / Bodegas Parra Jimenez / Bodegas Peñalba Lopez / Bonterra Vineyards / Brick House Vineyards（Newberg, OR）/ Brooks Wine（Amity, OR）の 13 件。**🔴 **`Bergström` は無い。** | 🔴 **不掲載＝証明された不在。**<br>**同じ `B` に Willamette の生産者が 3 軒、`A` に Montinore Estate（Forest Grove, OR）が載っており、
「オレゴンが対象外」ではないことが同時に確認できる** |
| **Demeter U.S.A. — 会員個別検索 URL** | **会員検索の直接 URL** | ⚠️ **`404 – File or directory not found`（`demeter-usa.org` のサイト刷新による）** | ⚠️ **取得できず。**上の Directory 一覧で代替した |
| 🔴 **LIVE Certified**（`Low Input Viticulture and Enology`。オレゴンの持続可能認証） | **`/visit` の `certified_members` ビュー** | 🔴 **地図レイヤに会員 288 地点が埋め込まれており、その中に `Bergström` は 1 件も無い。**（同レイヤには 12th and Maple、A to Z Wineworks–REX HILL、Adelsheim の 3 畑、Ponzi/Abetina などが実在する） | 🔴 **不掲載。**⚠️ **ただし表形式の会員一覧は `A` 行で切れており、地図レイヤ 288 件が全会員かは確証が無い** |
| **USDA Organic INTEGRITY Database**（`apps.ams.usda.gov/integrity`） | **有機認証事業者の照会** | ⚠️ **Blazor の SPA シェルのみが返り、データが返らない**（クライアント描画） | ⚠️ **未検証。有機認証の有無は本書では主張しない** |
| **Oregon Wine Board** | **—** | ⚠️ **Cloudflare の bot チャレンジ（`Just a moment...`）。方針によりこれを回避していない** | ⚠️ **未取得** |

### 🔴 ⚠️ 公式内部の緊張 —— **「ビオディナミである」と「認証は無い」が同居している**

- 🔴 ✅ **`/family`** ——「**Josh と彼の献身的な farming team は、Dundee Hills・Ribbon Ridge・Chehalem Mountains の
  5 つの畑にまたがる、**`70 acres of biodynamic, estate monopole`** の Pinot Noir と Chardonnay の世話人である。**」
- 🔴 ✅ **`/family`** ——「**Josh は biodynamic と regenerative の農法を擁護しており、
  それを自らのテロワールとワインの地域的性格を保つ道具と見なしている。**」
- 🔴 ✅ **Josh 一人称・ブログ `1,000 Days of Effort`（2020 年 4 月 10 日）** ——
  「**われわれは除草剤も農薬も殺虫剤も使わない。**`We are Biodynamic farmers.`**
  `Bio ＝ 生`、`Cide ＝ 死` であることを思い出してほしい。われわれは生を肯定し、生を築く工程を選ぶ。**」
- 🔴 **対して 5 つの畑ページはすべて `non-certified`。**

→ 🔴 **これは矛盾ではなく、「実践」と「第三者認証」の別である。**
  **フロアでは「認証は取っていないが、ビオディナミで農をやっている造り手」と言うのが正確。** → §Staff Notes ⚠️ ①

### ✅ 実際にやっていること（公式・Josh 一人称）

**堆肥（`/farm` と `1,000 Days of Effort` の両方に記述がある）**
🔴 「**毎年、われわれは自前の堆肥の山を数百トン築く —— 地元の有機の牛糞、地元の有機の藁と草、
前の収穫の発酵済みの果皮・種・梗、冬の剪定枝、
そして `chamomile（カモミール）`、`yarrow（ヤロウ）`、`valerian（バレリアン）`、
`dandelion（タンポポ）`、`stinging nettle（イラクサ）` といった薬草を混ぜる。
春にこれを畑へ返すと、より豊かで肥沃な複雑な土をつくり、構造・保水力・活力を高める。**」
🔴 「**堆肥は 5 つの estate すべての上で築く。牛糞は地元の Bansen 家の酪農場の有機のもの、
藁は友人の Boyer 家の有機のものを使う。**」
🔴 「**10 フィートの高さの山はすぐに発酵を始め、冷たい朝には湯気が立ち上るのが見えるほどの熱を出す。**」

**やらないこと**
🔴 ✅ 「**1999 年の畑の開設以来、`herbicides, pesticides, insecticides, systemic chemicals` を使わずに farm してきた。**」
🔴 ✅ 「**合成肥料ではなく、堆肥づくりと、ホメオパシー的な薬草・鉱物のお茶（`homeopathic herbal and mineral teas`）
による処置を選ぶ。**」
🔴 ✅ 「**カビやうどんこ病の防除に他者が強い合成殺菌剤に頼るところを、
われわれは植物性・ホメオパシー的なお茶を集中的に使う。**」

**生態系**
- ✅ **カバークロップの多様性と、捕食性昆虫・ミツバチ・多様な鳥のための生息地づくり**
- 🔴 ✅ **2020 年から羊（`The Vine Ewes`）を導入。地元の羊飼いが率いる群れが春のカバークロップを食み、食みながら施肥する**
- ✅ **カバークロップの内訳（春の記述）——「**背の高いライ麦草、マスタード、クローバー**」、
  「**小さなヒナギクがカバークロップに点在して咲き、ラッパズイセンとタンポポが陽を浴び、次はカモミールが咲く番だ**」**
- 🔴 ✅ **機械の置き換え** ——「**機械的で炭素を排出する機械類を、可能なかぎり人の手作業に置き換えてきた。**」

**Josh 自身の労働の実感（2021 harvest report）**
🔴 「**自社畑で果実をサンプリングして 1 日 13 マイル以上歩いた結果の筋肉の痛み**」

❓ **公式に無い**: 台木の品種名・クローン番号・区画名の一覧・年間生産本数・仕立ての様式・
灌漑の有無・収量（t/acre または hL/ha）。

---

## Winemaking

⚠️ **醸造については、公式は畑ほど数値を開示していない。以下は商品台帳の解説文から取れた範囲である。**

| 事項 | 記述 |
|---|---|
| 🔴 **リリースまでの時間** | ✅ **「farm・ferment・age・finish に 3 年 ＝ `1000 days of effort`」**（`/farm`） |
| 🔴 **収穫** | ✅ **手摘み（`hand-picked` / `harvesting each of our estate vineyards by hand`）** |
| **瓶詰** | ✅ **「`hand-bottled`」**（`/farm`） |
| 🔴 **全房発酵** | ✅ **`Winery Block` は「`100% whole cluster` の Pinot Noir」。**<br>✅ **2019 Winery Block の醸造家ノートは「`carbonic, whole-cluster Pinot Noir at its best`」**<br>⚠️ **他のキュヴェの全房比率は公式に数字が無い** |
| 🔴 **Chardonnay（Sigrid）** | 🔴 ✅ **「各自社畑を手で収穫したのち、果実を別々に `小さなフレンチオーク樽` で発酵させ、
`完全なマロラクティック発酵` と `18 か月の sur lie 熟成` を経る。そのうえで最良の樽だけを Sigrid のために選ぶ」** |
| **ロゼ** | 🔴 ✅ **「われわれのロゼは、アメリカ屈指の Pinot Noir の appellation である `Ribbon Ridge AVA` の
Pinot Noir を `全房プレス（whole-cluster-pressed）` した意図的なピンクのワインである。
`Le Pré du Col` と `La Spirale` の 2 つの畑が選ばれる」**（2021 harvest report） |
| **Syrah（gargantua）** | ✅ **「全房発酵と `neutral oak` 熟成」** |
| **醸造の姿勢** | 🔴 ✅ **Cuvée Caroline の解説より** ——「**筋肉・膂力・樽の誇示に寄る抽出的なスタイルではなく、
むしろ茶に近い、`infusion style` の醸造の、可憐さへの丁寧な注意を示している**」 |
| ⚠️ **新樽比率／樽熟期間（赤）／樽メーカー／酵母** | ⚠️ **公式に一切記載が無い** |
| 🔍 **アルコール度数（公表されている年のみ）** | 🔍 **公式商品ページに `Alcohol:` が併記されるのは一部のヴィンテージのみ。確認できた値は 12.9% / 13.0% / 13% / 13.2% / 13.3% / 13.4% / 13.5% / 13.6% / 13.8% / 13.9% / 14.1%**<br>🔴 **OBP 掲載 5 本のうち度数が公表されているのは 2019 年産のみ。2018 / 2021 / 2023 は無い** |

---

## Style

### ✅ Vintage Guide（生産者公式 PDF・`Updated 02/2025`・1999〜2023 の全 25 年）

🔴 **これは「その年の Willamette Valley と自社の作柄」の記述であり、キュヴェごとの記述ではない。**

| VT | 公式の記述（要旨・原文からの訳） | 飲み頃の指示 |
|---|---|---|
| ⭐ **2018** | 「**暖かく早い年から、また古典的に冷涼な秋へと入り、完璧な成熟の条件になった。
ワインは、果実味・ミネラル・ジューシーな味わいと均衡した見事な酸を示す。**」 | **DRINK NOW – 2035+. HOLD LARGE FORMATS.** |
| ⭐ **2019** | 「**早熟なほど暖かい春と夏から、冷涼で気まぐれな秋へ。
Pinot Noir と Chardonnay を低い糖度で、ジューシーな自然の酸とともに摘んだ。
ワインは花の香りを帯び、優雅で、テクスチャーがあり、品があり、`crunchy`。中長期にわたって良く飲める。**」 | **DRINK NOW – 2033+. HOLD LARGE FORMATS.** |
| ⭐ **2021** | 🔴 「**近年でもっとも溢れるように美味な（あえて `perfect` と言おうか）ヴィンテージのひとつ。
この年の Pinot Noir と Chardonnay は、今すでに美味で抗いがたく、優雅に熟成していく。
機会があれば買い置きを。大瓶は将来の特別な場で強い印象を残すだろう。**」 | **DRINK NOW – 2035+.** |
| ⭐ **2023** | 🔴 「**オレゴン史上 3 番目に暖かいヴィンテージ（2014、2015 に次ぐ）。
2023 年のリリースは赤白ともに等しくスリリング。…… Pinot Noir は溢れるように花と果実を帯び、
明るいマゼンタとルビーの色調と優れた口中の重み、果実・セイヴォリー・スパイス・ミネラルの
卓越した均衡を示す。このヴィンテージはきわめて快く、遊び心と真剣さが同時に成り立つ美味しさの典型である。
若くして良く、蔵での熟成にも耐える。**」 | **DRINK UPON RELEASE – 2035.** |

🔍 **参考（OBP に無い年で、フロアで対比に使えるもの）**
- **2020** ——「**9 月下旬の森林火災の影響で谷の大半にとって complicated な年。
  早摘みと蔵での厳格な declassification のおかげで、われわれの蔵は生き生きとした明るいワインを生んだ。
  Chardonnay にとっては熟成能力のある一級のヴィンテージ。
  Pinot Noir は当社史上もっとも低い生産量とアルコール度数で、途方もない複雑さと熟成能力を示す。**」
- **2022** ——「**春の霜の困難で収量が大きく減ったあと、Willamette Valley の回復力の証しとなるヴィンテージ。**」
- **2013** ——「**リリース当時は難しいヴィンテージとされたが、いまや過去 10 年でもっとも求められる年のひとつ。**」

### ✅ 畑ごとのスタイル（生産者の言葉。**畑ページと商品ページで一貫している**）

| 畑 | Pinot Noir の性格 ✅ |
|---|---|
| 🔴 **Bergström Vineyard**（Dundee Hills） | 🔴 「**`鉄の拳をビロードの手袋で包んだ（the iron fist in a velvet glove）`。
燻した肉や焚き火で焼いたジビエを思わせる強い鉄のミネラリティ。土の香り、タラゴン・タイム・ミントのような
セイヴォリーで甘い香草の調子、バラとスミレの繊細な花。絹のようにしなやかなタンニンで名高い。**」 |
| 🔴 **Silice**（Chehalem Mountains） | 🔴 「**鮮烈な香辛料と花の魅力、そこに生と乾のガーデンハーブのセイヴォリーな含み。
豊富な光と風のおかげで、この畑は当社でもっとも果実前面で熟した感じの Pinot Noir を一貫して生む。
どのヴィンテージでも、シナモン、カルダモン、八角、胡椒、ナツメグ、サッサフラス、コーラが一口ごとにある。**」 |
| **Winery Block**（Chehalem Mountains） | 「**甘いベーキングスパイス、五香粉、稀少材、香。黒いリコリスとジンジャーブレッドが長く残る。
頑健な構造と十分に熟したタンニン。**」 |
| **Le Pré du Col**（Ribbon Ridge） | 「**松茸と森の下草を思わせる旨味の含み。五香粉、稀少材、香、赤と青の果実。絹の質感と熟成に耐える構造。**」 |
| **La Spirale**（Ribbon Ridge） | 「**Willamette Valley でもっとも花に寄った表現のひとつ。
シャクヤク、バラ、スミレ、砂糖漬けの赤い果実。ジューシーで多汁な酸が長く尾を引く。**」 |

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本・すべて `unresolved`。
セクションは全て `UNITED STATES | RED > WILLAMETTE`（p.26）、producer heading は `Bergström`**）

| # | OBP 印字 | VT | 価格 | ✅ 🏛 **公式の正式名と、確認できたこと** |
|---|---|---|---|---|
| 1 | **'Cumberland Reserve,'** Willamette Valley Pinot Noir | **2023** | **$160** | ✅ **正式名 `Cumberland Reserve Pinot Noir`。**商品台帳の `appellation` は **`Willamette Valley`** ＝ **メニュー印字と一致**。<br>🏛 **COLA の Fanciful Name も `CUMBERLAND RESERVE`。**<br>✅ **2023 の存在は公式の商品台帳（SKU `23CUMBPN`・小売 $55）と Accolades ページの双方で確認** |
| 2 | **'Silice,'** Chehalem Mountains Pinot Noir | **2021** | **$305** | ✅ **正式名 `Silice Vineyard Pinot Noir`。**`appellation` は **`Chehalem Mountains`** ＝ **一致**。<br>🔴 **`Silice` にアクセント記号は付かない**（公式サイト・商品台帳・COLA すべて `Silice` / `SILICE`）。<br>✅ **2021 の存在は Accolades ページで確認。**⚠️ **現行ストアフロントには 2021 の 750ml が無い（完売）** |
| 3 | **'Silice,'** Chehalem Mountains Pinot Noir | **2019** | **$305** | ✅ **同上。2019 は Accolades で確認、かつ 2019 の 1.5L/3L/5L が商品台帳に現存。**🔍 **2019 の公表アルコールは 13.0%** |
| 4 | **'Silice,'** Chehalem Mountains Pinot Noir | **2018** | **$280** | ✅ **同上。2018 の公式醸造家ノート（`updated January 2025`）が 3L の商品ページに現存する** |
| 5 | 🔴 **（キュヴェ名の印字なし）** Dundee Hills Pinot Noir | **2023** | **$440** | 🔴 ⚠️ **メニューにキュヴェ名が無い。**`original_raw_line` は **`2023\t\tDundee Hills Pinot Noir\t\t\t\t\t\t440`**。<br>🔴 **`DUNDEE HILLS` は 🏛 COLA の Fanciful Name 88 件中 1 件も存在しない ＝ キュヴェ名ではない。**<br>🔴 **`Dundee Hills` は AVA 名である。** → 下記 |

### 🔴 OBP 5 行目「Dundee Hills Pinot Noir」は何か —— 突き合わせた 4 つの事実

1. ✅ **自社 5 畑のうち Dundee Hills AVA にあるのは `Bergström Vineyard` ただ 1 つ。**
   （Winery Block と Silice は Chehalem Mountains、Le Pré du Col と La Spirale は Ribbon Ridge）
2. ✅ **同社の商品台帳で `wine.appellation == "Dundee Hills"` かつ 2023 年産の赤は
   `2023 Bergström Vineyard Pinot Noir`（SKU `23BERGPN` / `23BERGPN3L`）ただ 1 つ。**
3. 🔍 **価格の倍率が一致する。**
   **Cumberland Reserve 2023：小売 $55 → OBP $160 ＝ 2.91 倍。
   Bergström Vineyard 2023：小売 $150 → 2.91 倍なら $437。OBP は $440。**
4. 🔍 **メニュー組版の説明がつく。**
   **producer heading がすでに `Bergström` なので、キュヴェ名 `Bergström Vineyard` を並べると
   `Bergström / 'Bergström Vineyard,' Dundee Hills Pinot Noir` と重複する。**
   **`original_raw_line` の末尾タブ数（6 個）は、この行が他の 4 行より短いこと（他は 2〜4 個）と整合しており、
   「印字段階でキュヴェ名が落ちている」ことが intake の parse ミスではないと確認できる。**

⚠️ **唯一の対抗候補は `Ekollon`（スウェーデン語で「どんぐり」）である。**
**商品台帳で `appellation: "Dundee Hills"` を持つもう 1 本だが、確認できるのは `2024 Ekollon Pinot` のみ。**
**🏛 COLA の `EKOLLON` は 2024 年 6 月 17 日の 2 件のみで、Accolades ページにも Ekollon の項目が無い。**
**本調査の資料に `2023 Ekollon` は 1 件も存在しない。**

🔴 **したがって本書の判断：`2023 Bergström Vineyard Pinot Noir` である蓋然性がきわめて高い。
ただし、メニューがキュヴェ名を印字していない以上、断定はしない。**
→ 🔴 **確定にはラベルの実見が要る。** → §Open Questions 1（**フロア作業**）

### ✅ 生産者が現在造っているワイン（🏛 COLA と ✅ 商品台帳の突き合わせ）

**自社畑・畑名キュヴェ（Pinot Noir）**

| 公式名 | AVA ✅ | 備考 |
|---|---|---|
| 🔴 **`Bergström Vineyard Pinot Noir`** ⭐OBP5? | **Dundee Hills** | ✅ **Accolades に 2013–2024 の連続した記載** |
| 🔴 **`Silice Vineyard Pinot Noir`** ⭐OBP2·3·4 | **Chehalem Mountains** | ✅ **Accolades に 2013–2024 の連続した記載** |
| **`Winery Block Pinot Noir`** | **Chehalem Mountains** | ✅ **2014–2024。100% 全房** |
| **`Le Pré du Col Vineyard Pinot Noir`** | **Ribbon Ridge** | ✅ **2018–2024**（⚠️ Accolades に 2020 が無い） |
| **`La Spirale Vineyard Pinot Noir`** | **Ribbon Ridge** | ✅ **2019–2024**。⚠️ **Accolades の見出しは `La Spirale Pinot Noir`、ストアは `La Spirale Vineyard Pinot Noir`。`Vineyard` の有無が公式内部で揺れる** |

**ブレンド・その他**

| 公式名 | AVA ✅ | 定義（公式の言葉） |
|---|---|---|
| 🔴 **`Cumberland Reserve Pinot Noir`** ⭐OBP1 | **Willamette Valley** | 🔴 「**Portland でわが家族が育った通りの名に因む。5 つの自社畑の最良の樽のいくつかをブレンドし、
オレゴンの Pinot Noir を最良の姿で示す。Bergström のスタイルの典型 —— そのヴィンテージ固有の性格と、
香辛料・ミネラル・フレッシュな果実の完璧な結婚。**」 |
| 🔴 **`Sigrid Chardonnay`** | **Willamette Valley** | 🔴 「**旗艦の白。スウェーデン人の祖母への homage であり、その `spirit, grace, and strength` が
3 世代の Bergström の子らを鼓舞した。**」🔴 **`Silice` と `Winery Block` の Chardonnay が毎年その土台になる** |
| **`Old Stones Chardonnay`** | **Willamette Valley** | 「**Sigrid の妹分（`the baby sister to our Sigrid Chardonnay`）**」 |
| **`Homage Pinot Noir`** | **Willamette Valley** | 🏛 COLA・商品台帳の双方に実在 |
| **`Ekollon Pinot`** | **Dundee Hills** | 🏛 **COLA 2024/06/17。**⚠️ 2024 年産のみ確認 |
| **`Cuvée Caroline Pinot Noir`** | **Willamette Valley** | ✅ **2024 年、Josh と Caroline の 25 周年を記念した一度きりのボトリング。
`Bergström Vineyard` の火山性土と `La Spirale` の海成砂質土から** |
| **`gargantua Syrah`（Oregon / Washington / California）／`pantagruel Syrah`** | 州名表示 | ✅ **全房発酵・ニュートラルオーク** |
| **`Ribbon Ridge Rosé of Pinot Noir`** | **Ribbon Ridge** | ✅ **`Le Pré du Col` と `La Spirale` から全房プレス** |

**買いブドウの畑名キュヴェ（🔍 商品台帳と 🏛 COLA より。過去〜現在）**
🔍 **`Gregory Ranch`（Yamhill-Carlton）／`Shea Vineyard`（Yamhill-Carlton）／
`Temperance Hill Vineyard`（Eola-Amity Hills）／`Koosah Vineyard`（Eola-Amity Hills）／
`Hope Well`／`Croft Vineyard`／`Wren Vineyard`／`Nysa Vineyard`（Dundee Hills・2004）／`Arcus Vineyard`（2000）**

**🏛 COLA にのみ現れ、現行ストアには無い名（＝過去または限定のボトリング）**
🏛 **`Paley's Place Cuvee` / `Salud Cuvée` / `Berghöuse` / `Les Griottes` / `La Voluptueuse` /
`Cuvee T.W.O.` / `Cuvee Solidarite` / `Houstonian Strong` / `Opportunity` / `The Two Pillars` /
`The Pioneer and the Punk` / `The Little Giant` / `White Gold` / `Single Barrel Selection` / `Rose'`**
⚠️ **これらは COLA の Fanciful Name であり、フロアで語る材料には使わない。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① ビオディナミです。ただし「認証」ではありません。ここを混ぜないでください。**
「**オレゴン、Willamette Valley の家族経営です。1999 年、スウェーデン出身の外科医だったお父さんの John と
息子の Josh が始めました。Josh の奥さんの Caroline はブルゴーニュ、ボーヌの出身で、二人は Beaune の
栽培醸造学校で出会っています。**
**畑は 5 つ、合わせて 70 エーカー。造り手はこの 5 つすべてについて、こう公表しています ——
『慣行栽培ゼロ、**認証は受けていない**ビオディナミ／再生型農法』。**
**除草剤・農薬・殺虫剤・浸透性化学物質は 1999 年の開設以来ひとつも使っていません。
合成肥料の代わりに、自前の堆肥を毎年数百トン。地元の有機の牛糞と藁、前年の果皮・種・梗・剪定枝、
そしてカモミール、ヤロウ、バレリアン、タンポポ、イラクサといった薬草を混ぜて仕込みます。
2020 年からは羊も畑に入れています。**
**ただし Demeter などの認証は取っていません。造り手自身が『non-certified』と書いています。**」

**② リストの 3 つの産地名は、入れ子です。矛盾ではありません。**
「**`Willamette Valley`（Cumberland Reserve）、`Chehalem Mountains`（Silice）、`Dundee Hills` ——
この 3 つはケンカしていません。Chehalem Mountains も Dundee Hills も Ribbon Ridge も、
すべて Willamette Valley の **中に** ある、より小さな AVA です。
造り手は広い名前を名乗るワインと、狭い名前を名乗るワインを、意図して造り分けています。**
**`Cumberland Reserve` は 5 つの自社畑の最良の樽を集めたブレンドなので、広い `Willamette Valley` を名乗ります。
名前の由来は、Bergström 家が Portland で育った通りの名前です。**
**`Silice` は Chehalem Mountains にある単一畑の名前です。フランス語の『シリカ（石英）』。
砂の含有率が 70%、砂岩の岩盤まで 15〜20 フィート。6000 万年前は砂丘か浜辺だっただろう、と造り手は書いています。
終日の日照と一年中の風があって、5 つの畑のなかでいちばん果実が前に出る Pinot になります。
シナモン、カルダモン、八角、胡椒、ナツメグ、サッサフラス、コーラ —— これがどの年にも出る、と。**」

**③ $440 の「Dundee Hills」は、リストにワイン名が印字されていません。**
「**このお値段の 1 本だけ、リストにキュヴェ名が入っていません。`Dundee Hills` は畑の名前ではなく、産地の名前です。**
**造り手の 5 つの自社畑のうち、Dundee Hills にあるのは `Bergström Vineyard` という 1 つだけです。
1999 年に植えた、この家の最初の畑 ——『Bergström Wines の生誕地』と造り手が呼ぶ畑で、
玄武岩の上に鉄分の多い火山性の粘土、真南向きのすり鉢型。
造り手はここの Pinot を『ビロードの手袋に包んだ鉄の拳』と表現します。
燻した肉、焚き火、鉄のミネラル、タラゴンやタイム、バラとスミレ。**
**ただし、ラベルを実際に見て確認するまでは『Bergström Vineyard です』と断定しないでください。**」

### 追加で使える一手

- **`1000 日`**：「**1 本を farm し、発酵させ、熟成させ、仕上げるのに 3 年。造り手はこれを
  『1,000 Days of Effort』と呼んで、家族とチームの合言葉にしています。**」
- **`Sigrid` の由来**：「**旗艦の Chardonnay `Sigrid` は、Josh の祖母の名前です。
  公式サイトには 1950 年の写真があって、17 歳の John と母 Sigrid が写っています。
  『その spirit, grace, and strength が 3 世代の Bergström の子らを鼓舞した』と。
  各畑を手で摘んで小樽で別々に発酵、フル・マロラクティック、18 か月の sur lie。
  そのうえで最良の樽だけを選びます。**」
- **`Winery Block` の話**：「**わずか 2 エーカー、1 エーカーあたり 5,000 樹。
  オレゴンの標準の 2 倍以上の密植で、大きさと密度のせいで完全に手作業でしか farm できません。
  Caroline の故郷ブルゴーニュと、Josh がボーヌで学んだことへの敬意だ、と造り手は書いています。
  100% 全房の Pinot Noir です。**」
- **2021 年の話（OBP に 2021 の Silice があるとき）**：「**2021 はオレゴンにとって記録的に乾いて暑い年でした。
  『heat dome』で華氏 115 度が 3 日続いた —— それまでの記録は 2003 年の 106 度です。
  1 度目の熱波は果粒がまだ小さく緑だったので無傷でしたが、2 度目がヴェレゾンのど真ん中に来て、
  Josh は『西側キャノピーの果実の 10〜15% を失ったと見積もる』と書いています。
  ところが 9 月に入ると熱が引いて、涼しい夜が丸ひと月戻ってきた。
  それでゆっくり熟して、酸が高いまま糖が整った。造り手は Vintage Guide で
  『あえて perfect と言おうか』とまで書いている年です。**」
- **2023 年の話（Cumberland Reserve と Dundee Hills が 2023）**：「**オレゴン史上 3 番目に暖かい年
  （2014、2015 に次ぐ）。造り手は『遊び心と真剣さが同時に成り立つ美味しさの典型』と表現していて、
  『若くして良く、蔵でも保つ』と。DRINK UPON RELEASE から 2035 まで、が造り手の指示です。**」
- **輸入・流通**：「**アメリカ国内は Wilson Daniels の National Portfolio で扱われています。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／出典が否定している**）

1. 🔴 ⚠️ **「ビオディナミ認証（Demeter 認証）です」「オーガニック認証です」と言わない。**
   **造り手自身が 5 つの畑すべてについて `non-certified` と明記している。**
   🏛 **Demeter U.S.A. の Biodynamic Directory の `B` 一覧にも掲載が無い**
   （**同じ一覧に Willamette の Brick House・Brooks・Anacreon が載っており、オレゴンが対象外なのではない**）。
   🏛 **LIVE Certified の会員地図 288 件にも無い。**
   **USDA の Organic INTEGRITY Database は本調査では照会できていない（有機認証の有無は未確認）。**
   → **言えるのは「認証は取っていないが、ビオディナミの実践で農をやっている」まで。**

2. 🔴 ⚠️ **産地名から「矛盾」を作らない。**
   **`Chehalem Mountains` も `Dundee Hills` も `Ribbon Ridge` も、`Willamette Valley` の内側にある AVA である。**
   **リストの 3 つの産地表記は、造り手の意図した造り分けであって、誤記ではない。**

3. 🔴 ⚠️ **$440 の 1 本を「Bergström Vineyard です」と断定しない。**
   **メニューにキュヴェ名が印字されていない。**
   **状況証拠（Dundee Hills の自社畑は 1 つだけ／2023 年の Dundee Hills 表示の赤は 1 本だけ／
   価格倍率が Cumberland Reserve と一致）は強いが、確定にはボトルのラベルを見る必要がある。**

4. ⚠️ **「創業以来ずっと全畑同じ農法です」と言わない。**
   **`La Spirale` だけは `since 2019`。この畑は 2018 年に取得したもので、転換はその後である。**

5. ⚠️ **「100% 自社畑（estate）です」と言わない。**
   **造り手自身の言葉は「`progressively moving toward a 100% estate-farmed approach`」＝ 途上である。**
   **実際に Gregory Ranch、Shea、Temperance Hill、Koosah などの買いブドウ由来のキュヴェが併存する。**

6. ⚠️ **`Silice` の面積を数字で断定しない。**
   **畑ページは `14 acres`、商品ページの畑解説は `20-acre` と書いており、公式内部で食い違っている。**
   **同様に自社畑の合計も、`70 acres` と公表されている一方、各畑の数字の和は 67 acres である。**
   **植栽年も `Silice: 2001-2006` と `Planted 2001`、`Winery Block: 2002-2005` と `Planted 2002` で揺れる。**

7. ⚠️ **`Silice` にアクセントを付けない。**
   **公式サイト・商品台帳・🏛 TTB COLA のすべてで `Silice` / `SILICE`。`Silicé` でも `Sílice` でもない。**
   **フランス語の `silica`（シリカ）に由来する、と造り手が説明している。**

8. ⚠️ **点数・評価を言わない。**
   **公式サイトには `Accolades` ページがあり、多数の批評家スコアが列挙されている。
   本ドシエはそれをワインの事実として採用していない。**
   **同ページはヴィンテージの実在を確かめるためだけに使った。**

9. ⚠️ **新樽比率・樽熟期間・酵母・生産本数・収量を言わない。**
   **赤について公式に一切記載が無い。**
   **言えるのは「Sigrid は小さなフレンチオーク樽で発酵、フル MLF、18 か月 sur lie」
   「Winery Block は 100% 全房」「gargantua Syrah はニュートラルオーク」まで。**

10. ⚠️ **アルコール度数を、公表されていないヴィンテージについて言わない。**
    **OBP 5 本のうち度数が公式に出ているのは 2019 年産だけである。**

11. ⚠️ **ワイナリーの住所を断定しない。**
    **公式サイトの `Map & Directions` は JS 埋め込みで、本調査では本文に番地が取れていない。**
    **`8115 NE Worden Hill Road, Dundee, OR 97115` という住所は同業組合 `dundeehills.org` の掲載であり、
    生産者公式ではない。**

12. ⚠️ **ラベルにウムラウトが刻まれているとも、いないとも言わない。**
    🏛 **TTB の Brand Name 欄は 88 件すべて `BERGSTROM`（ウムラウト無し）だが、
    同じ permit の `BERGHÖUSE` や `SALUD CUVÉE` は diacritic を保持している。**
    **登録上の綴りと、ラベルの意匠は別問題である。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **新規の登録は行っていない。以下は escalation であり、実行していない。**

### ① 🔴 これは conflict ではない —— **canonical のギャップ（`Bergström` 不在／オレゴン州が丸ごと不在）**

1. **ID**
   - canonical 生産者: 🔴 **無し。**`db_wine_canonical.json` 全 928 レコード・383 生産者に
     `Bergström` / `Bergstrom` は 0 件（**ASCII 畳み込み・レコード全文検索でも 0 件**）
   - OBP research shell: 🔍 **producer 層 `rs:pro:f3777ffa589f76a9`**
     ／ product 層 `rs:pro:723c8a4b7649a21e`（Cumberland Reserve）・`rs:pro:7d377355793761f4`（Silice、3 release を束ねる）
     ・`rs:pro:528dcadaa99d591b`（Dundee Hills Pinot Noir）
     ／ release 層 `rs:rel:b8ff59627c22801f`・`rs:rel:d584abdbd80d6d77`・`rs:rel:743d2edbda6e56a8`
     ・`rs:rel:fbb0477e8a8d0ac7`・`rs:rel:fb41809af91a4874`
   - OBP 行: `source_line_no 1342`〜`1346`（`beverage_menu_bottles.doc` p.26）
2. **なぜ duplicate に見えないのか（＝ conflict ではない理由）**
   🔴 **重複候補が存在しない。近似も別名も無い。**
   🔴 **さらに構造的な事実として —— canonical の米国レコードは 79 件あるが、`region` はすべて `California` である。
   オレゴンの生産者は 1 軒も存在しない。**
   → **これは「Bergström という 1 軒が抜けている」のではなく、**
     **「canonical がまだオレゴンという産地圏を持っていない」という被覆のギャップである。**
3. **証拠**
   - 🔍 **`migration/out/export/db_wine_canonical.json`：928 レコード／`producer` の distinct は 383。
     `country` は `France` 845・`USA` 79・`Japan` 4。`USA` 79 件の `region` は 100% `California`**
   - 🔍 **`research/out/t-01/inventory.json`：`Bergström` の 5 行はいずれも `flags: []`（parse エラーではない）**
4. **OBP への影響**
   🔴 **$160 / $305 / $305 / $280 / $440 —— 計 5 本が canonical に着地できない。**
   **同じセクション `UNITED STATES | RED > WILLAMETTE` に属する他の生産者も、
   同じ理由で着地できていない可能性が高い（本書はそこまで掃引していない）。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - **生産者レコードを新設する：`producer = 'Bergström Wines'`、id `bergstrom-wines`、
     `country = 'USA'`、`region = 'Oregon'`、`subregion = 'Willamette Valley'`。**
   - **エイリアス `Bergström` / `Bergstrom Wines` / `Bergstrom` を保持する。**
   - 🔴 **`region` に `Oregon` を持ち込むのは canonical にとって初めての値である。
     `USA → California` しか無い現状の語彙にオレゴンを足す判断は、本書の権限外である。**
   - **キュヴェは 3 本を分けて登録する：`Cumberland Reserve Pinot Noir`（appellation: Willamette Valley）／
     `Silice Vineyard Pinot Noir`（appellation: Chehalem Mountains）／
     $440 の 1 本は **ラベル確認まで登録しない**（→ Open Questions 1）。**
6. **Confidence**: 🔴 **High**（不在は機械的に確認済み。オレゴン不在も同様）

### ② ⚠️ メニュー側の形 —— **キュヴェ名が印字されていない 1 行**

1. **ID**
   - OBP 行: `source_line_no 1346`（2023 / $440）
   - shell: 🔍 **`rs:pro:528dcadaa99d591b`（product 層）・`rs:rel:fb41809af91a4874`（release 層）**
   - intake の格納形: 🔴 **`product_name` キーが `source_transcription` に存在しない。
     `classification_text` に `"Dundee Hills Pinot Noir"` が入り、shell がこれを product 層の識別子として抱えている**
2. **なぜ誤って見えるか**
   🔴 **`Dundee Hills` は AVA 名であり、キュヴェ名ではない。**
   🏛 **TTB COLA の Fanciful Name 88 件に `DUNDEE HILLS` は 1 件も無い。**
   **他の 4 行が `'名前,' 産地 品種` という書式なのに対し、この 1 行だけが `産地 品種` になっている。**
   **producer heading がすでに `Bergström` であるため、キュヴェ名 `Bergström Vineyard` を並べると重複する ——
   組版側でこれが落ちた、というのが最も素直な説明である。**
3. **証拠**
   - 🔍 **`original_raw_line`：`2023\t\tDundee Hills Pinot Noir\t\t\t\t\t\t440`。
     末尾タブ 6 個は、他 4 行（2〜4 個）より本文が短いことと整合する ＝ 印字段階での欠落であって parse 事故ではない**
   - ✅ **自社 5 畑のうち Dundee Hills AVA は `Bergström Vineyard` のみ**
   - ✅ **商品台帳で `appellation == "Dundee Hills"` かつ 2023 年の赤は `2023 Bergström Vineyard Pinot Noir` のみ**
   - 🔍 **小売 $150 × 2.91（Cumberland Reserve 2023 の実測倍率）＝ $437 ≒ $440**
4. **OBP への影響**
   🔴 **$440 —— この生産者の 5 行中もっとも高価な 1 本が、キュヴェ不明のまま画面に出る。**
   **`Bergström Vineyard` として登録できれば、畑の地質・標高・植栽年・スタイル記述が即座に埋まる。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - 🔴 **ラベルを実見して確定するまで、キュヴェ名を canonical に書き込まない。**
   - **`Dundee Hills Pinot Noir` は **menu-printed alias** として保持し、
     `appellation = 'Dundee Hills'` だけは確定値として持てる（これはメニュー印字と AVA 名が一致しているため）。**
   - **確定後は `Bergström Vineyard Pinot Noir` として登録し、alias を残す。**
6. **Confidence**: ⚠️ **Medium-High**（産地は確定、キュヴェ名は状況証拠のみ）

### ③ 既存の系に属するもの／新しい番号を開かないもの

| 事象 | 扱い |
|---|---|
| 🔴 **`Chehalem Mountains` / `Dundee Hills` と `Willamette Valley` の併存** | 🔴 **conflict ではない。AVA の入れ子である。**✅ **生産者自身が 3 AVA を Willamette Valley の中と明記。**🏛 **27 CFR §9.90 / §9.180 / §9.182 / §9.205 が条名として実在する。**→ **番号を開かない。** |
| **`Bergström` のウムラウト（`ö`）** | 🔍 **既存の `C-1`（アクセント）系と同型。**`ö → o` の畳み込みは intake が既に行っている。**新番号は開かず、`C-1` の扱いに従う。** |
| **`La Spirale Pinot Noir` ↔ `La Spirale Vineyard Pinot Noir`** | ⚠️ **公式内部の表記ゆれ（Accolades ページ ↔ ストアフロント）。**⚠️ **OBP に該当行が無いため、本書は記録にとどめる。新番号は開かない。** |
| **`Silice` の面積（14 acres ↔ 20-acre）／自社畑合計（70 ↔ 67 acres）／植栽年の幅** | ⚠️ **公式内部の食い違い。**canonical への書き込み対象ではないため、**§Staff Notes と §Open Questions に落として番号は開かない。** |
| 🔍 **`vintage='—'`（em-dash sentinel）** | 🔍 **DB 全体で 182 生産者・328 レコードに及ぶ systemic な形として既に掃引済み。**本生産者は canonical に不在なので該当レコードも無い。**参照にとどめる。** |

---

## Sources

**一次資料 —— 生産者の公式サイト、生産者自身の商品台帳（Commerce7）、生産者公開の PDF、
および公的レジストリのみ。retailer / critic / auction / Wikipedia は事実の典拠に使用していない。**

### 🔴 サイト真正性の事前確認（**どうやって確かめたか**）

| 判定 | サイト | 確認方法 |
|---|---|---|
| ✅ **真正** | 🔴 **`https://bergstromwines.com/`** | **(a) 一貫した自己同定** —— `/wp-json/` ルートが `name: "Bergström Wines"`、`url`/`home` ともに `https://bergstromwines.com` を返す。<br>**(b) 商業インフラの自己保有** —— Commerce7 テナント slug が `bergstrom-wines`、商品画像 CDN が `images.commerce7.com/bergstrom-wines/…`。**第三者が偽造できる形ではない。**<br>**(c) 法人との一致** —— 🏛 **TTB COLA の Brand Name `BERGSTROM WINES, LLC`（permit `BW-OR-260`、オレゴンの Bonded Winery）と、サイトが名乗る事業内容・州が一致する。**<br>**(d) `robots.txt` が `Sitemap: https://bergstromwines.com/sitemap_index.xml` を宣言し、Yoast 生成の 10 サイトマップが実在する。**<br>**(e) 実在の電話番号 3 系統（`503-554-0468` / `503-554-0463`）が全ページのフッターに入る。** |
| ✅ **真正（生産者自身のデータ）** | 🔴 **`api.commerce7.com/v1/…/bergstrom-wines`（商品台帳・126 商品）** | **同社サイトが `cdn.commerce7.com` のバンドルを読み込んで自ら描画しているストアフロントのバックエンド。**<br>🔴 **`wine.appellation` / `wine.vintage` / `wine.varietal` / `variants[].sku` / `variants[].price` を機械可読で持つ。**<br>⚠️ **ただしこれは商取引の記録であって、編集された記述ではない。**本書はこれを「生産者が自ら記録した商品台帳」として扱い、味わいの断定には使っていない。 |
| 📄 **非公式（事実の典拠には使用せず）** | **`https://dundeehills.org/businesses/bergstrom-wines/`** | 🔴 **Dundee Hills Winegrowers Association ＝ 同業組合であって生産者ではない。**<br>**`<title>` は `Bergström Wines - Dundee Hills Winegrowers Association`、著者欄は `Vanessa Bazzani`（組合側の担当者）。**<br>**住所 `8115 NE Worden Hill Road, Dundee, OR 97115` と、「25 年以上 biodynamic growers」という記述を掲げるが、本書はこれを事実として採用していない。** |

### ✅ 取得した公式資料

| 資料 | 取得した情報 |
|---|---|
| ✅ **`robots.txt` → `sitemap_index.xml`** | 走査の起点。**post / page / avada_portfolio / category / post_tag / fusion_tb_category / portfolio_category / element_category / slide-page / author の 10 サイトマップ**<br>⚠️ **`robots.txt` の中身は `User-agent: * / Disallow:`（全許可）と Sitemap 宣言のみ。エージェント宛の指示文は含まれていなかった** |
| 🔴 **`/farm`（How We Farm）** | 🔴 **本ドシエ §Farming の骨格。**`1000 Days of Effort`／**70 acres・5 畑・3 AVA**／**1999 年以来 herbicide・pesticide・insecticide・systemic chemical を使わない**／**堆肥の材料（有機牛糞・有機藁・果皮種梗・剪定枝・カモミール/ヤロウ/バレリアン/タンポポ/イラクサ）**／**ホメオパシー的な薬草・鉱物のお茶**／ワインの地域的表現 |
| 🔴 **`/place`（Place）** | **自社畑 5 つの一覧と、それぞれの AVA・植栽年・キャッチフレーズ。**`Sigrid` が畑と並んで提示されている |
| 🔴 **`/farm/bergstrom-vineyard`** | 🔴 **Dundee Hills AVA・1999・13 acres・350–380 ft・玄武岩上の火山性粘土・2,200–5,000 vines/acre・`0% conventional, non-certified BD/regenerative-ecological since inception`・`iron fist in a velvet glove`** |
| 🔴 **`/farm/silice-vineyard`** | 🔴 **Chehalem Mountains AVA・2001–2006・14 acres・400 ft・砂 70%・砂岩まで 15–20 ft・2,200–5,000 vines/acre・`non-certified BD … since inception`・Calkins Lane の上・`Sigrid` の土台** |
| **`/farm/winery-block`** | **Chehalem Mountains AVA・2002–2005・2 acres・400 ft・5,000 vines/acre・完全手作業・`non-certified BD … since inception`** |
| **`/farm/le-pre-du-col`** | **Ribbon Ridge AVA・2006・16 acres・385–400 ft・頁岩/シルト岩上の海成堆積土・老木のダグラスファーが南北の区画を分ける・`non-certified BD … since inception`** |
| 🔴 **`/farm/la-spirale`** | 🔴 **Ribbon Ridge AVA・2005・22 acres・400–450 ft・14 種の海成堆積土・Pinot Noir/Chardonnay/Syrah・2018 年取得・`non-certified BD … since 2019`** |
| 🔴 **`/family`（Our Family）** | 🔴 **John（スウェーデンの伐採村→ Portland の産婦人科外科医）・Karen（California 出身の正看護師）＝ Founders／Josh ＝ Owner, CEO, Director of Winemaking／Caroline ＝ Owner, Director of Sales（Beaune 出身、Hospice de Beaune → Lycée Viticole）／Josh は CFPPA Beaune の postgraduate／125 以上の畑での経験／WVWA 理事／`Willamette: The Pinot Noir Auction` 創設／2023 年 Académie Internationale du Vin／「`70 acres of biodynamic, estate monopole`」／「`progressively moving toward a 100% estate-farmed approach`」／写真キャプション `John (17), and his mother, Sigrid, 1950`** |
| **`/trade`・`/contact`** | **米国流通は `Wilson Daniels` の National Portfolio。電話 3 系統** |
| 🔴 **`Vintage Guide`（PDF・4 頁・`Updated 02/2025`）** | 🔴 **1999〜2023 の全 25 ヴィンテージの生育年記述と飲み頃指示。**OBP の 2018 / 2019 / 2021 / 2023 すべてを含む |
| 🔴 **`Accolades` ページ** | 🔴 **本書では「どのキュヴェのどのヴィンテージが存在するか」の確認にのみ使用した。**<br>**Silice Vineyard PN：2013–2024／Bergström Vineyard PN：2013–2024／Cumberland Reserve PN：2018–2024／Winery Block PN：2014–2024／Le Pré du Col PN：2018–2024（2020 欠）／La Spirale PN：2019–2024／Sigrid Ch：2012–2023**<br>⚠️ **同ページの批評家スコアは本ドシエで一切採用していない** |
| 🔴 **ブログ `1,000 Days of Effort`（Josh 署名・2020-04-10）** | 🔴 **一人称の農の告白。**「20 年間、化学肥料でなく手作りの堆肥で」「除草剤・農薬・殺虫剤は使わない。`We are Biodynamic farmers`」「Bansen 家の有機牛糞と Boyer 家の有機藁」「機械を人の手に置き換えてきた」「2020 年に羊 `The Vine Ewes` を導入」 |
| 🔴 **ブログ `2021 Harvest Report`（Josh 署名・2021-10-28）** | 🔴 **OBP の 2021 に直結。**heat dome 華氏 115 度 ×3 日（前記録は 2003 年の 106 度）／2 度目の熱波で「果実の 10–15% を失ったと見積もる」／9 月に冷涼が戻り緩やかに熟した／Chardonnay は 12 日で摘み終えた／ロゼは Ribbon Ridge の `Le Pré du Col` と `La Spirale` から全房プレス／Josh の 25 回目の収穫 |
| **ブログ `Spring in the Vineyard`（Josh 署名・2020-03-27）** | **畑チームの実名（Sarah, Nick, Mayo, Félipe, Leo）／堆肥の作り方（10 フィートの山・湯気）／カバークロップ（ライ麦草・マスタード・クローバー）** |
| 🔴 **Commerce7 商品台帳（126 商品・うち Wine 119）** | 🔴 **キュヴェ名・ヴィンテージ・`appellation`・SKU・小売価格の一次確定。**<br>🔴 **`Cumberland Reserve → Willamette Valley` / `Silice Vineyard → Chehalem Mountains` / `Bergström Vineyard → Dundee Hills` / `Le Pré du Col`・`La Spirale` → `Ribbon Ridge` / `Shea`・`Gregory Ranch` → `Yamhill-Carlton` / `Temperance Hill`・`Koosah`・`Dr. Bergström Riesling` → `Eola-Amity Hills`**<br>🔴 **`2023 Bergström Vineyard Pinot Noir` SKU `23BERGPN` 小売 $150.00／`2023 Cumberland Reserve Pinot Noir` SKU `23CUMBPN` 小売 $55.00** |

### 🏛 ［公的レジストリ］

| 資料 | 取得した情報 |
|---|---|
| 🔴 🏛 **TTB COLA 公開レジストリ**（`ttbonline.gov/colasonline/`） | 🔴 **今回は bot チャレンジに当たらず、検索結果が取得できた。**<br>🔴 **Permit `BW-OR-260` / Brand Name `BERGSTROM WINES, LLC`。総ヒット 108 件、うち **88 件を復元**（2013-08 〜 2026-01）。**<br>🔴 **Fanciful Name の全数：SILICE / CUMBERLAND RESERVE / BERGSTROM VINEYARD / LE PRE DU COL VINEYARD / LA SPIRALE / LA SPIRALE VINEYARD / WINERY BLOCK / SIGRID / HOMAGE / OLD STONES / GREGORY RANCH / SHEA VINEYARD / TEMPERANCE HILL VINEYARD / CROFT VINEYARD / WREN VINEYARD / KOOSAH PINOT NOIR / KOOSAH VINEYARD / EKOLLON / CAROLINE / GARGANTUA / GARGANTUA PANTAGRUEL / PALEY'S PLACE CUVEE / SALUD CUVEE / SALUD CUVÉE / LES GRIOTTES / LA VOLUPTUEUSE / CUVEE T.W.O. / CUVEE SOLIDARITE / BERGHÖUSE / HOPE WELL / HOUSTONIAN STRONG / OPPORTUNITY / THE TWO PILLARS / THE PIONEER AND THE PUNK / THE LITTLE GIANT / WHITE GOLD / SINGLE BARREL SELECTION / ROSE'**<br>🔴 **`DUNDEE HILLS` という Fanciful Name は 1 件も無い。**<br>🔴 **`BERGHÖUSE`（ö）と `SALUD CUVÉE`（É）が実在する＝このレジストリは diacritic を保持できる。それでも Brand Name は全件 `BERGSTROM`。**<br>⚠️ **1〜20 件目のページは取得できていない（キャッシュは 21 件目から始まる）。したがって 2013 年 8 月より前の登録は本書に反映されていない。**<br>⚠️ **1 件だけ permit が異なる：`CA-I-22083 / 268802 / 2026-03-12 / BERGSTROM VINEYARD / BERGSTROM`。California の輸入・卸 permit と見られるが、事業体の関係は本調査では特定していない** |
| 🔴 🏛 **Demeter U.S.A. — Biodynamic Farm and Product Directory** | 🔴 **`Browse by Member Name` の `A` / `B` / `C` を取得。`B` の 13 件を全数確認したが `Bergström` は無い。**<br>🔴 **同じ `B` に Willamette の Brick House Vineyards（Newberg, OR）・Brooks Wine（Amity, OR）・Belle Colline Vineyard LLC dba Anacreon Winery（Newberg, OR）が、`A` に Montinore Estate（Forest Grove, OR）が載っている ＝ オレゴンのワイナリーが対象外なのではない。**<br>⚠️ **会員個別検索の URL は `404 – File or directory not found` を返した（`demeter-usa.org` のサイト刷新による）** |
| 🔴 🏛 **LIVE Certified**（`livecertified.org` の `/visit`） | 🔴 **`certified_members` ビューの地図レイヤに会員 288 地点が埋め込まれている。`Bergström` は 1 件も無い。**<br>⚠️ **表形式の会員一覧はページングされており `A` 行で切れている。288 地点が全会員かどうかまでは確証が無い** |
| ⚠️ 🏛 **USDA Organic INTEGRITY Database**（`apps.ams.usda.gov/integrity`） | ⚠️ **Blazor の SPA シェルのみが返り、照会結果が返らなかった（クライアント描画）。有機認証の有無は未検証** |
| ⚠️ 🏛 **Oregon Wine Board** | ⚠️ **Cloudflare の bot チャレンジ（`Just a moment...` ページ）。方針によりこれを回避していない** |
| 🔴 🏛 **eCFR 27 CFR Part 9（AVA）** | 🔴 **条名の実在を確認：`§ 9.90 Willamette Valley` / `§ 9.180 Dundee Hills` / `§ 9.182 Ribbon Ridge` / `§ 9.205 Chehalem Mountains`。**<br>⚠️ 🔴 **境界の条文そのものは取得できていない（個別条文の取得は 0 バイトで失敗）。したがって「入れ子である」ことの根拠は生産者の記述 ✅ ＋ 条名の実在 🏛 までであり、境界記述による検証ではない** |

### 取得できなかったもの / 存在しなかったもの

- ⚠️ **`/2022-vintage-catalogue` と `/map-and-directions` は JS 埋め込みの空シェルで、本文が返らなかった。**
  **前者は 2022 年の全ラインナップ、後者はワイナリーの番地を含むはずだった。**
- ⚠️ **`/product/`（商品インデックスの WordPress 側）も同様に空シェル。**
  **商品情報は Commerce7 API から取得した。**
- ⚠️ **TTB COLA の 1〜20 件目**（＝ 2013 年 8 月より前の登録）。
- ⚠️ **ラベル画像そのもの。**COLA の一覧は取れたが、個別の label image は取得していない。
- ❓ **公式に存在しない**: 赤の新樽比率・樽熟期間・酵母・収量・年間生産本数・台木・クローン・仕立て・灌漑の有無。
- ❓ **公式に存在しない**: OBP 掲載 4 ヴィンテージ（2018/2019/2021/2023）のうち 2019 年産以外のアルコール度数。
- ⚠️ **オレゴン州務長官（Oregon Secretary of State）の法人登記は本調査で照会していない。**
  **法人格の根拠は 🏛 TTB COLA の `BERGSTROM WINES, LLC` のみである。**

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔴 **canonical 生産者レコード 0 件／canonical キュヴェ 0 件／
OBP 5 本（`producer_state: unresolved`、セクションは全て `UNITED STATES | RED > WILLAMETTE`、p.26、
`source_line_no 1342–1346`、producer heading は `Bergström`、`flags: []`）／
research shell 9 件（producer 1・product 3・release 5）。**
🔍 **canonical 全体：928 レコード・383 生産者・`country` は France 845 / USA 79 / Japan 4。
`USA` 79 件の `region` は 100% `California`。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | **公式サイトの site name・全ページ title・Commerce7 テナント slug・🏛 TTB の法人名と permit まで揃った。**⚠️ **番地だけが公式側で取れていない** |
| **Overview** | **High** | **`1000 Days of Effort`・農の自己規定・「100% estate へ漸進中」という自己記述が、すべて公式の原文で取れた** |
| **History** | **Medium** | **創業 1999・畑の植栽年・2018 の La Spirale 取得・2020 の羊・2023 の Académie は公式。**⚠️ **専用の年表ページが無く、植栽年が公式内部で揺れる（`2001-2006` vs `2001` 等）** |
| 🔴 **Location** | 🔴 **High** | 🔴 **自社畑 5 つすべてについて AVA・植栽年・面積・標高・土壌・密度・品種が数値で公式。**⚠️ **合計面積と Silice の面積だけが内部で食い違う** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **本ドシエで最も強い。**5 畑すべての `Farming Style` が 1 行で公表され、**認証の有無が「非認証」で確定。**🏛 **Demeter USA と LIVE の両レジストリで不在を確認。**堆肥の材料・薬草名・羊・カバークロップの草種まで公式 |
| **Winemaking** | ⚠️ **Low-Medium** | **Sigrid の樽発酵/MLF/18 か月 sur lie、Winery Block の 100% 全房、ロゼの全房プレス、`infusion style` の姿勢は取れた。**⚠️ **赤の新樽比率・樽熟期間・酵母・収量が皆無** |
| **Style** | 🔴 **High** | 🔴 **OBP の 4 ヴィンテージすべて（2018 / 2019 / 2021 / 2023）に、生産者公式 Vintage Guide の記述と飲み頃指示がある。**加えて畑ごとのスタイル記述が畑ページと商品ページで一貫している |
| **Important Cuvées** | ⚠️ **Medium-High** | 🔴 **5 本中 4 本は正式名・産地・ヴィンテージの実在を公式＋🏛 COLA で確定。**⚠️ **5 本目（$440）はキュヴェ名がメニューに無く、状況証拠 4 点で `Bergström Vineyard` を強く示すが断定していない** |
| **Staff Notes** | **High** | **芯 3 点＋一手 6 点＋⚠️ Must-Not-Say 12 項目。**🔴 **「Demeter 認証」「AVA の矛盾」「$440 の断定」「100% estate」という 4 つの誤りを塞いだ** |
| 🔴 **総合** | 🔴 **High — staff-usable（70% を明確に超過。到達度およそ 85%）。** | **必須 7 項目すべてを満たす。**Identity ✅／Overview ✅／Location ✅（**5 畑の数値が全部ある**）／**Farming ✅（極めて厚い。認証は proved negative）**／Important Cuvées（OBP 5 本中 4 本を公式名で確定、1 本は根拠を積んで Open Questions へ）✅／Staff Notes 芯 3 点 ✅／⚠️ Must-Not-Say 12 項目 ✅。<br>**欠けているのは赤の醸造数値と、$440 のキュヴェ名の最終確認。前者は公式が公開していない。後者は実ボトルで埋まる。** |

**reached_70: YES.**（**約 85%**）

---

## Open Questions

1. 🔴 **【実ボトル確認事項・フロア作業】OBP 5 行目「2023 / Dundee Hills Pinot Noir / $440」のキュヴェ名。**
   **メニューにキュヴェ名が印字されていない（`original_raw_line` に引用符付きの名前が無い）。**
   **状況証拠は 4 点そろっている ——**
   **(a) 自社 5 畑のうち Dundee Hills AVA は `Bergström Vineyard` のみ、**
   **(b) 商品台帳で `appellation == "Dundee Hills"` の 2023 年の赤は `2023 Bergström Vineyard Pinot Noir` のみ、**
   **(c) 小売 $150 × 2.91（Cumberland Reserve 2023 の実測倍率）＝ $437 ≒ $440、**
   **(d) producer heading が `Bergström` なのでキュヴェ名 `Bergström Vineyard` が組版上落ちる理由がある。**
   ⚠️ **唯一の対抗候補 `Ekollon`（Dundee Hills）は、確認できるのが 2024 年産のみで、2023 年産の記録が無い。**
   → 🔴 **これは資料では詰め切れない。ボトルのラベルを見れば 1 秒で決まる。**
   → 🔴 **確定するまで canonical にキュヴェ名を書き込まない。**

2. 🔴 **【実ボトル確認事項・フロア作業】2021 年産 Silice の実在確認。**
   ✅ **Accolades ページには 2021 Silice Vineyard Pinot Noir の記載があり、存在は公式に裏づけられている。**
   ⚠️ **ただし現行ストアフロントに 2021 の 750ml が無く（完売）、
   Vintage Guide も年単位の記述しか持たないため、このボトルについての造り手の言葉は無い。**
   → **語れるのは Vintage Guide の 2021 年評（「あえて perfect と言おうか」）と、
     Silice という畑のスタイル記述までである。**

3. ⚠️ **【実ボトル確認事項】ラベル上の綴りにウムラウトがあるか。**
   🏛 **TTB の Brand Name 欄は 88 件すべて `BERGSTROM`。**
   **同じ permit の `BERGHÖUSE` / `SALUD CUVÉE` は diacritic を保持しているので、
   システム上の制約ではない。**
   **一方、公式サイトの site name・全 title・商品名はすべて `Bergström`（ö あり）で、
   フッターの著作権表示だけが `Bergstrom`（ö 無し）。**
   → **canonical の表示名を決める前に、ラベルの実物で確認するのが確実。**

4. ⚠️ **ワイナリーの所在地（番地）が公式側で取れていない。**
   **公式の `Map & Directions` ページは JS 埋め込みの空シェルだった。**
   📄 **同業組合 `dundeehills.org` は `8115 NE Worden Hill Road, Dundee, OR 97115` を掲げるが、
   本書はこれを事実として採用していない。**
   → **公式ページをブラウザ描画で取得すれば埋まる。**

5. ⚠️ **27 CFR Part 9 の境界条文が取れていない。**
   **eCFR で確認できたのは `§9.90 Willamette Valley` / `§9.180 Dundee Hills` /
   `§9.182 Ribbon Ridge` / `§9.205 Chehalem Mountains` という条名の実在まで。**
   **個別条文の取得は 0 バイトで失敗した。**
   → **入れ子関係の主張自体は生産者の記述で足りているが、
     規制一次資料で裏づけるならここを埋める必要がある。**

6. ⚠️ **公式内部の数値の食い違いが 4 件ある。どれも本書では優劣を決めない。**
   - **`Silice` の面積：畑ページ `14 acres` ↔ 商品ページの畑解説 `20-acre`**
   - **自社畑の合計：`/farm` と `/family` の `70 acres` ↔ 各畑ページの和 `67 acres`**
   - **`Silice` の植栽年：`2001-2006`（畑ページ）↔ `Planted 2001`（`/place`・商品ページ）**
   - **`Winery Block` の植栽年：`2002-2005`（畑ページ）↔ `Planted 2002`（`/place`）**

7. ⚠️ **`Bergström Vineyard` の標高が 2 通りある。**
   **畑ページは `350-380 ft`、商品ページの畑解説は `Elevation: 380ft`。**
   **矛盾というより「幅」と「代表値」の違いと思われるが、公式が明示していない。**

8. ⚠️ **`La Spirale Pinot Noir` か `La Spirale Vineyard Pinot Noir` か。**
   **Accolades ページの見出しは `La Spirale Pinot Noir`、ストアフロントの商品名は
   `La Spirale Vineyard Pinot Noir`。**
   **OBP に該当行が無いため急がないが、canonical に入れるときは決める必要がある。**

9. ⚠️ **`Ekollon` がいつ始まったのか。**
   🏛 **COLA は 2024-06-17 の 2 件のみ。商品台帳は `2024 Ekollon Pinot`（Dundee Hills）のみ。
   Accolades ページに項目が無い。**
   **COLA の承認日は必ずしもヴィンテージ年と一致しないため、2022 または 2023 年産の可能性は残る。**
   → 🔴 **これが解ければ Open Questions 1 の対抗候補が完全に消える。**

10. ⚠️ **TTB COLA の 1〜20 件目（2013 年 8 月より前）が取れていない。**
    **総数 108 件のうち 88 件しか復元していない。**
    **古いキュヴェ名がさらに出る可能性があるが、OBP 5 本の判定には影響しない。**

11. ⚠️ **`CA-I-22083` permit の COLA が 1 件ある。**
    🏛 **`26067001000106 / CA-I-22083 / 268802 / 2026-03-12 / BERGSTROM VINEYARD / BERGSTROM / OREGON / TABLE RED WINE`。**
    **`BW-OR-260` とは別の permit（California の輸入・卸と見られる）である。**
    ❓ **Bergström Wines, LLC との関係（自社の California 拠点か、第三者の卸か）は本調査では特定していない。**
    → **`The Mascot` の件（Batch 9・Harlan）のような事業体の取り違えを避けるため、
      canonical へ昇格する前に確認しておくのが安全。**

12. ⚠️ **USDA Organic INTEGRITY Database と Oregon Wine Board が照会できていない。**
    **前者は Blazor の SPA でデータが返らず、後者は Cloudflare の bot チャレンジで阻まれた。**
    **方針によりチャレンジを回避していない。**
    → **したがって「有機認証を受けていない」とは本書では断定していない。**
      **断定しているのは「ビオディナミ認証（Demeter）を受けていない」までである。**

13. 🔴 **canonical にオレゴン州の生産者が 1 軒も存在しない。**
    🔍 **`USA` 79 レコードの `region` は 100% `California`。**
    **本生産者を昇格させると、canonical にとって初めての `Oregon` になる。**
    → 🔴 **`region` 語彙にオレゴンを足す判断は本書の権限外。Akio / CTO の設計判断。**
    → **同じ `UNITED STATES | RED > WILLAMETTE` セクションの他の生産者も同じ状態にある可能性が高い
      （本書は掃引していない）。**
