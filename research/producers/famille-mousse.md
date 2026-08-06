# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にはこの生産者のレコードが 3 件、しかも「2 つの別生産者」として存在する**
> （`Famille Mousse` 2 件 ／ `Mousse Fils` 1 件）。**本書は昇格前の研究記録であり、canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagnemousse.fr で確認**（一次資料）
> `🏛` **公的登録**（`recherche-entreprises.api.gouv.fr` ／ Agence Bio ／ Club Trésors de Champagne 公式）
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `⚠️` **出典が沈黙している／出典間で食い違っている** ／ `🔴` 高重要度
> `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://champagnemousse.fr/`（FR 原本 ＋ `/en/`）**
> 走査元: **`/sitemap_index.xml` → `page-sitemap.xml`（20 URL）**、および
> **WP REST API `/wp-json/wp/v2/pages`（FR 12 ページ / EN 11 ページ、本文全文）**
> ⚠️ **サイトは年齢確認ゲートで本文が隠れる。REST API 経由で本文を取得した。**
>
> ---
>
> 🔴 **本ドシエ最大の収穫 —— `P-2`（実体分裂）に決着をつける公的証拠が取れた。**
> **Agence Bio の事業者レコード（numeroBio `44958`）は、ただ 1 つの SIRET `449 670 702 00025` に対して**
> **`raisonSociale = "SARL CHAMPAGNE MOUSSE FILS"` と `denominationcourante = "SARL FAMILLE MOUSSE"` の**
> **両方を記載し、`gerant = "Cédric Moussé"` としている。**
> **すなわち `Moussé Fils` と `Famille Moussé` は 2 軒ではなく、単一法人の 2 つの名前である。**
> → §Canonical Conflict `P-2`（**評価は既存 ID に追記。新番号は開かない**）
>
> 🔴 **第二の収穫 —— canonical のキュヴェ名 `Les Fortes Terres Extra Brut Special Club` の**
> **`Special Club` を裏づける公式根拠が存在しない。**
> **① 公式サイト全文（12 ページ・69,221 文字）に `club` / `spécial` / `special` の出現は 0 件。**
> **② Club Trésors de Champagne の公式会員名簿（25 軒）に Moussé は無い（HTML 411KB 中 `mousse` 0 件）。**
> → §Canonical Conflict（**新形状・未採番**）
>
> 🔴 **第三の収穫 —— canonical の `Terre d'Illite` のセパージュが公式と矛盾している。**
> **canonical `Pinot Meunier 100%` ／ 公式 `80% MEUNIER 20% PINOT NOIR`。**
> → §Canonical Conflict（**新形状・未採番**）
>
> 🔴 **第四の収穫（P-2 の前提そのものへの反証）—— 統合しても消えるのは 3 本ではなく 1 本である。**
> **canonical の `Les Fortes Terres` は `mousse-fortes-terres-2018` の 1 ヴィンテージのみ。**
> **OBP は 2018 / 2019 / 2020 の 3 本。実体統合で解決するのは 2018 の 1 本だけで、**
> **2019 と 2020 は「canonical にヴィンテージが無い」＝ gap として残る。** → §Canonical Conflict `P-2` 追記 4

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔴 **2 通りに割れている。** `Famille Moussé`（BLANC DE NOIRS 節）／ `Moussé Famille`（SPÉCIAL CLUB 節） |
| 🔴 **公式の商号** | ✅ **`CHAMPAGNE MOUSSE FILS`**（mentions légales の「Directeur de la publication」。FR/EN 両版とも同一表記）<br>✅ 本文中の表記は **`Champagne Moussé`**（例: 沿革ページ見出し「**LA RENAISSANCE DU CHAMPAGNE MOUSSÉ**」、キュヴェ解説「**les nouvelles et les jeunes parcelles du Champagne Moussé**」） |
| 🔴 **法人（登記名）** | 🏛 **`SARL FAMILLE MOUSSE`** — **SIREN `449 670 702`** / **SIRET（siège）`449 670 702 00025`**<br>**設立 2003-08-01**／**NAF `01.21Z`（Culture de la vigne）**／**état `A`（活動中）**／**nature juridique `5499`** |
| 🔴 **同一法人が両名を持つ公的証拠** | 🏛 **Agence Bio 事業者 `numeroBio 44958`（id 123874）:**<br>**`raisonSociale`: `SARL CHAMPAGNE MOUSSE FILS`**<br>**`denominationcourante`: `SARL FAMILLE MOUSSE`**<br>**`siret`: `44967070200025`（＝上記 SIREN と同一）**／**`gerant`: `Cédric Moussé`**<br>🔴 **単一 SIREN が両名を担っている。これが `P-2` の決着証拠である。** |
| **代表者** | 🏛 **`MOUSSE, CEDRIC ROGER EDMOND`（Gérant、生年 1980-07）** |
| **所在（登記）** | 🏛 **`3 RUE DE JONQUERY, 51700`**（INSEE の siège は commune `CHATILLON-SUR-MARNE`、Agence Bio は同一住所を `Cuisles` としても登録）<br>⚠️ **Cuisles / Châtillon-sur-Marne の 2 通りで登録されている。同一住所の commune 表記揺れ** |
| **所在（サイト掲載）** | ✅ **`5 Rue de Jonquery, 51700 Cuisles`**（mentions légales）<br>⚠️ **登記の `3 rue de Jonquery` と番地が違う。同一通り。** |
| 🔴 **正しいアクセント** | ✅ **`Moussé`（é つき）。** 公式本文は人名・社名とも一貫して `Moussé`（Eugène Moussé / Edmond Moussé / Jean-Marc Moussé / Champagne Moussé）<br>⚠️ **ドメイン `champagnemousse.fr` と mentions légales の大文字表記 `CHAMPAGNE MOUSSE FILS` は無アクセント**（ドメインの技術制約／フランス語の大文字慣行） |
| **当主** | ✅ **Cédric Moussé**（2003 年〜）。CIVC の実験醸造所などで研鑽 |
| **先代** | ✅ **Jean-Marc Moussé**（1976 年初収穫。**Cuisles 村長を 25 年**。2013 年に事故） |
| **創業者** | ✅ **Eugène Moussé（1896 年生）。1923 年に最初の 1 本** |
| **代数** | ✅ **「父から子へ 1629 年以来 12 世代の vigneron、醸造家としては 4 世代」** |
| **canonical id** | 🔍 **3 件が 2 生産者に分裂**: `mousse-terre-dillite-2020` / `mousse-terre-dillite-2019`（`producer='Famille Mousse'`）／ `mousse-fortes-terres-2018`（`producer='Mousse Fils'`） |

### 🔴 ⚠️ Cuisles には別系統の Moussé 家法人が実在する（**混同禁止**）

🏛 **`recherche-entreprises.api.gouv.fr` を `mousse cuisles` で検索（22 件）した結果、
本生産者とは別の Moussé 名義の法人が同じ村に複数ある。**

| 法人 | SIREN | 住所 | NAF | 代表 |
|---|---|---|---|---|
| 🔴 **`MOUSSE`** | **534 379 938** | **2 rue du Four à Chaux, Cuisles** | **01.21Z** | 🔴 **`MOUSSE, MATHIEU EDMOND ROBERT` ／ `MOUSSÉ, NICOLAS`（Gérant 2 名）** |
| **`NICOLAS MOUSSE`** | 829 560 895 | Cuisles / Châtillon-sur-Marne | 01.21Z | — |
| **`ODILE THIEULLET (MOUSSE)`** | 841 334 576 | 3 rue de la Bochotte, Jonquery | 01.21Z | — |

🔴 **`MOUSSE`（SIREN 534379938）は別の番地・別の代表者を持つ、本生産者とは別の栽培法人である。**
**「Cuisles の Moussé」というだけでは一意にならない。** → §Staff Notes ⚠️ ⑧

### 🏛 本生産者を取り巻く付随法人（すべて Cédric Moussé 系。**ブランドではない**）

| 法人 | SIREN | 性格 |
|---|---|---|
| **`GROUPEMENT FONCIER VITICOLE CHAMPAGNE MOUSSE ET FILS`** | **521 983 254** | **土地保有 GFV（1 rue de Jonquery、2010 設立）。`MOUSSE, CEDRIC ROGER EDMOND` が Gérant。associés 約 32 名の出資組合** |
| `CEDRIC MOUSSE (CEDRIC MOUSSE ACCOMPAGNEMENT)` | 818 231 623 | **5 rue de Jonquery**（＝mentions légales の住所）。NAF 46.19B |
| `GROUPEMENT D'EMPLOYEURS MOUSSE & CIE` | 913 395 257 | 雇用組合 (78.30Z) |
| `GROUPEMENT FONCIER VITICOLE MOUSSE & CIE` | 948 905 799 | 土地保有 (68.20B) |
| `SCI LES FRERES MOUSSE` | 908 159 999 | 不動産 (68.20B) |
| `CUMA TERRES DE MEUNIER` | 978 274 348 | 機械共同利用組合 (01.61Z) |

🔴 **これらは「別ブランド」ではなく、フランスの農業経営に典型的な
「exploitation（SARL）＋ 土地 GFV ＋ 雇用 GE ＋ 機械 CUMA」という機能分割である。**
**`GFV CHAMPAGNE MOUSSE ET FILS` に `Champagne Moussé et Fils` の名が現れることは、
`Moussé Fils` が別の醸造元であることを意味しない。** → §Canonical Conflict `P-2`

---

## Overview

✅ **ヴァレ・ド・ラ・マルヌ右岸、Cuisles 村。マルヌ川に直交する小さな谷にある、
ピノ・ムニエに徹した家族経営の栽培醸造家。**

🔴 ✅ **公式が自らを規定する第一句は `profondément meunier…`（英語版 `Deeply Meunier...`）である。**
「**マルヌ川に直交する小さな谷、Cuisles 村に位置するわれわれのシャンパーニュ・メゾンは、
1923 年以来、緑色粘土のテロワールの上で identitaire な Meunier を手がけている。
畑は主に 3 つの村に分かれているが、同じ一つの南向き斜面の上にある。
われわれはこの品種とこの唯一のテロワールのために、自らを消すことに全力を尽くす。**」

🔴 ✅ **「父から子へ 1629 年以来 12 世代の栽培者、醸造家としては 4 世代。
われわれは環境への影響を抑えるために一つ一つの所作を考え直している。
自然はわれわれの道具であり、大切に扱わねばならない。
醸造は可能な限り介入を減らし、目標は明確 —— 純粋で、張りがあり、自然な Meunier である。**」

🔴 ✅ **公式の全キュヴェ 10 点のうち 8 点が Meunier 主体、うち 3 点が Meunier 100%。**
**Chardonnay 100% の `L'Anecdote` が唯一の例外で、公式自身が
「Cuisles にはそれまで 100% Chardonnay は存在しなかった」と書いている。**

🔍 **THÉSEUS における状態は「同一生産者が 2 生産者に割れている」形。
`Terre d'Illite` は `Famille Mousse` に、`Les Fortes Terres` は `Mousse Fils` に置かれ、
OBP 5 行はすべて `famille-mousse` に割り当てられた結果、
`Les Fortes Terres` 3 行が「canonical に実在するのに未解決」になっている。**
🔴 **ただし実際に実体統合で救われるのは 2018 の 1 本だけである。** → §Canonical Conflict

---

## History

✅ **公式沿革ページ（`/notre-histoire/` ／ `/en/our-history/`）は本文が完全に取得できた。**
🔴 **この生産者の沿革は、シャンパーニュの生産者としては異例に濃い戦争史を含む。**

| 年 | 出来事 ✅ |
|---|---|
| **1629** | **父から子へ vigneron の家系が始まる**（公式「vignerons de père en fils depuis 1629」、**12 世代**） |
| **17 世紀〜** | **Moussé 家は一貫してヴァレ・ド・ラ・マルヌ沿いに住む。**⚠️ **EN 版のみ「最初は Saint Eugène、その後 1880 年から Cuisles」と書く。FR 版は「À Cuisles depuis 1880」のみで前段が無い** |
| **1880** | **Cuisles に定着。**当時は**自家の畑を耕し、ブドウは Négoce に売っていた** |
| **1896** | **Eugène Moussé 生まれる** |
| **1922** | **ブドウ相場の暴落（crise de 1922）** |
| 🔴 **1923** | 🔴 **Eugène Moussé が最初の 1 本を生産。**1922 年の危機を受け、**canton で自らシャンパーニュを醸造すると決めた 2 人の vigneron の 1 人**。最初の圧搾機と数樽を購入 |
| **1926** | **初めての商業化。**Cuisles で最初の自動車（Citroën B14）の持ち主 **Evrard Thomas** にパリまで運んでもらい、**開業したばかりのアメリカ人ケータリング業者と出会う。数年後、この業者が Eugène の生産量を全量買い取るようになる**。ボトルは木箱で **Port-à-Binson 駅**へ運ばれ（Fresne 氏の黒馬 Mona が牽く荷車）、列車でパリ **Gare de l'Est** へ |
| **1939** | **第二次大戦により Eugène の努力が中断** |
| 🔴 **1943-06-24** | 🔴 **Eugène の息子 Edmond と友人 Jean Loé が、Cuisles のブドウ畑の真ん中の電柱を鋸で切り、ドイツ軍への送電を断つ** |
| **1943-08** | **落下傘降下した英米の飛行士を救出する `réseau Possum` が組織される**（ベルギー・ルクセンブルク州から Reims–Fismes–Soissons の三角地帯まで） |
| **1943-11-15** | **Eugène が降下した飛行士 2 名（英国人 Ian Robb、米軍中尉 Carlyle Darling）を 12 日間匿う** |
| **1943-12-28** | **Gestapo の急襲（Reims、161 rue Lesage）で réseau Possum が壊滅** |
| 🔴 **1944-06-21** | 🔴 **レジスタンスの Eugène と Edmond が Gestapo に逮捕される。**将校が食器棚の上に Sten 短機関銃を見つけたが家宅捜索はせず、寝室に隠れていたレジスタンスの Jacques Hodin が助かる。Reims（rue Jeanne d'Arc）→ Châlons-sur-Marne → Compiègne。**妻 Suzanne は自転車で Compiègne へ夫の消息を尋ねに行った**<br>**2 人は Neuengamme に送られ、次いで Bremen-Farge の Kommando で Valentin 掩体壕の建設に従事。Edmond はその後ハンブルクの瓦礫で不発弾処理に回された** |
| 🔴 **1945-04-12** | 🔴 **Eugène Moussé、Ravensbrück 強制収容所でチフスにより死去**（Watenstedt-Salzgitter の爆弾・弾薬工場に送られていた）。**妻 Suzanne が息子 Edmond の回復まで経営を代行** |
| **1947** | **`LA RENAISSANCE DU CHAMPAGNE MOUSSÉ`。** 戦後、Edmond が醸造への情熱で谷の多くの vigneron を指導・育成 |
| **1976** | 🔴 **Jean-Marc の初収穫。**「**畑とワインへの深い情熱をもって、Jean Marc はごく早い時期に生態的転換の舵を切る。着任間もなく畑の草生栽培（enherbement）を始め、生産全体を考え直した**」 |
| **1990** | **Jean-Marc が新しい圧搾設備を建設**（のちに現在のレセプション・ホールとなる）／**同年 Edmond 死去** |
| 🔴 **2003** | 🔴 **Cédric の時代が始まる。**CIVC の実験醸造所（cuverie expérimentale）などで研鑽ののち、家族の畑で実験を重ねる。「**極めて責任ある生産と深い持続可能性へ、とことん行くという意志が早くから形になった**」<br>🏛 **同年 `SARL FAMILLE MOUSSE` 設立（登記 2003-08-01）。**⚠️ **サイトはこの法人設立に触れていない**<br>🔴 **同年、perpétuelle（永久ブレンド）の起点。現行 4 キュヴェが `2003/…` と表記する** |
| **2009** | **Jean-Marc と Cédric が、完全にエコ設計された新しい醸造施設（chai）を建設** |
| **2013** | **Jean-Marc が事故で中断。Cédric が彼の始めた醸造を引き継いで仕上げる** |
| 🔴 **2014** | 🔴 **「合成農薬を完全に停止する賭けに成功した（le pari d'arrêter complètement les pesticides de synthèse est réussi）。以降、要求は極めて明快 —— よりよく、そして清潔に造る」** |
| 🔴 **2017** | 🔴 **醸造における断絶。**「**頭にあったのはただ一つ、すべての仮面を取り去ること —— 門出のリキュールの糖、醸造補助剤、石油由来の硫黄、新樽、酸化…。数年にわたる研究とワインの深い変質の号砲だった**」 |
| **2023** | **創業 100 周年。**「**centenaire の年がレンジの再編を画し、`Eugène` が登場した**」（旧称 `Carte Or` → `Or Tradition` → `L'Or d'Eugène`） |
| **現在** | ✅ **Pays Nantais の vigneron `Fred Niger` との出会いを受け、「ワインの振動レベルを上げること」に今後数年を充てる。「カーボン・ゼロと質的向上を常に念頭に、複数のプロジェクトが進行中」** |

⚠️ **公式に無い**: Eugène 以前の当主名、Edmond の生年、Jean-Marc の生没年、Cédric の就任の正式年（「2003」は見出しの年）。

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| **Village** | 🔴 ✅ **Cuisles（51700）。マルヌ川に直交する小さな谷**（Vallée de la Marne 右岸 / Petite Montagne） |
| 🔴 **畑の広がり** | 🔴 ✅ **3 村 —— `Cuisles` / `Jonquery` / `Châtillon-sur-Marne`。**「**畑は主に 3 つの村に分かれているが、すべての区画は同じ一つの斜面の上にあり、全面南向き（exposé plein sud）**」 |
| 🔴 **土壌** | 🔴 ✅ **「土壌の 90% が石灰質マルヌの上の緑色粘土（argiles vertes sur marne calcaire）」**（キュヴェ 4 点に同一表記）<br>🔴 **緑色粘土＝ペドロジーでいう `Illite`。**「**われわれの土壌は浅く、非常に水はけのよい石灰質マルヌがあり、そして必ず厚い緑色粘土の脈がある。ペドロジーで `Illite` と呼ばれるものだ**」 |
| 🔴 **土壌断面（公式）** | 🔴 ✅ **4 層** —— **① 表土の粘土質土 20 cm ② 非常に排水性の高い粘土質砂 40 cm（砂 80%）③ 緑色粘土（Illite）30 cm ＝ 土壌の水の備蓄 ④ 石灰質マルヌ（白亜＋粘土）** |
| 🔴 **緑色粘土の機能** | 🔴 ✅ 「**とくに夏の長い乾燥期には、緑色粘土だけが湿気の残る唯一の土壌である。この粘土の繊細さと純度がブドウへの給水を保証する**」 |
| **リュー・ディ（公式に名前が出るもの）** | ✅ **`Les Fortes Terres`（Cuisles、4 区画）**／✅ **`Les Varosses`（Cuisles）**／✅ **`Les Terres Rouges`（Jonquery）**／✅ **`Les Bouts de la Ville`（Cuisles、当家最古の区画）** |
| 🔴 **`Les Varosses` の逸話** | 🔴 ✅ 「**シャンパーニュの世界では `les Varosses` の名は、ブドウの質が高くない場所を指すのによく使われる。25 年前、われわれはこのリュー・ディが Cuisles の斜面の他の部分と違って非常に深い土壌を持つことに気づいた —— 他が 0.60 m なのに対し 1.60 m。だから深い土を好む Chardonnay を植えることにした**」 |
| ⚠️ **畑の面積** | ⚠️ 🔴 **公式サイトに ha の数字が一切無い。**本調査では**確定できなかった** → Open Questions 3 |
| **格付** | ⚠️ **公式サイトは Cuisles の échelle des crus 上の格付に触れていない** |

---

## Farming

🔴 **この生産者の栽培は「公的登録が公式サイトより多くを語る」という珍しい形をしている。
公式サイトは認証名を一つも出さないが、Agence Bio には登録がある。**

### ✅ 公式サイトが語る実務（**認証名は一つも出てこない**）

| 年 | 内容 ✅ |
|---|---|
| **1976 年〜** | **Jean-Marc が着任間もなく畑の草生栽培（enherbement）を開始し、生産全体を再設計** |
| **2009** | **完全にエコ設計された醸造施設（chai complètement éco-conçu）** |
| 🔴 **2014** | 🔴 **「合成農薬の完全停止に成功」** |
| 🔴 **2017** | 🔴 **醸造から「仮面」を除去 —— 門出のリキュールの糖 / 醸造補助剤 / 石油由来の硫黄 / 新樽 / 酸化** |
| **収穫** | ✅ **全キュヴェで手摘み、`caisse de maraichage`（市場向け野菜用の浅いコンテナ）** |
| 🔴 **硫黄** | 🔴 ✅ **`soufre de mine fabrication maison`（自家製の鉱山硫黄）を全キュヴェで使用。**公式はキュヴェごとに **mg/l 単位の実数**まで開示している（下表） |
| **現在** | ✅ **「カーボン・ゼロと質的向上」を目標に複数プロジェクト進行中** |

🔴 ✅ **公式が開示する硫黄の実測値（この開示の細かさ自体がこの生産者の性格を示す）**

| キュヴェ | 硫黄 |
|---|---|
| **Eugène** | **12 mg/l H2SO4** |
| **Eugène Longue Garde** | **SO2 total 29 mg/l** |
| **Eugène Rosé** | **< 10 mg/l H2SO4** |
| **Les Vignes de mon Village** | **< 10 mg/l H2SO4** |
| **Les Terres d'Illite 2019** | **11 mg/l H2SO4** |
| 🔴 **Les Fortes Terres 2018** | 🔴 **26 mg/l H2SO4** |
| **L'Anecdote 2019** | **23 mg/l H2SO4** |

### 🏛 認証の実態（**公的登録から。公式サイトは沈黙している**）

🔴 **Agence Bio 事業者レコード `numeroBio 44958`（`SARL CHAMPAGNE MOUSSE FILS` / `SARL FAMILLE MOUSSE`）**

| 項目 | 値 🏛 |
|---|---|
| 🔴 **認証機関** | 🔴 **`Ecocert France`（`FR-BIO-01`）** |
| 🔴 **状態** | 🔴 **`ENGAGEE`（有機認証に engagement 中）。`dateSuspension`・`dateArret` ともに `null`** |
| 🔴 **engagement 開始日** | 🔴 **`2022-09-01`**（`datePremierEngagement` も同日 ＝ **これが最初の engagement**） |
| **活動** | **`Production` / `Viticulture`** |
| 🔴 **生産の状態（参照年 2026）** | 🔴 **`Raisin de cuve` に `AB`（認証済）・`C1`（転換 1 年目）・`CS`（非有機）の 3 状態が併存**<br>**`Raisin de table` = `CS`／`Jachère` = `CS`／`Culture inconnue` = `AB`** |
| **証明書 URL** | 🏛 `https://certificat.ecocert.com/entreprise/FCED643D-C4B8-40F2-8907-7DFD6F170D76` |
| **`siteWebs`** | ⚠️ **空**（Agence Bio 側に URL 登録なし） |

🔴 ⚠️ **ここから導かれる、卓上で最も重要な帰結:**
**① 有機への engagement は `2022-09-01` 開始である。**
**したがって OBP に載る 2018 / 2019 / 2020 の収穫は、いずれも有機転換の開始より前である。**
**② 2026 年参照でも畑は `AB` / `C1` / `CS` が混在しており、全園が認証済ではない。**
→ 🔴 **これらのボトルを「オーガニック」と呼んではならない。** → §Staff Notes ⚠️ ②

### ⚠️ 公式サイトに存在しない語（**機械走査による確認**）

🔴 **FR 12 ページ・EN 11 ページの本文全文（FR 側 69,221 文字）を機械走査した結果:**

| 語 | 出現数 |
|---|---|
| `bio` / `Bio` | 🔴 **0** |
| `certifi…`（certifié / certification） | 🔴 **0** |
| `Ecocert` | 🔴 **0** |
| `HVE` | 🔴 **0** |
| `Demeter` / `biodynam…` | 🔴 **0** |
| `durable` | 🔴 **0** |
| `VDC` | 🔴 **0** |
| `récoltant` / `manipulant` / `matricul…` | 🔴 **0** |
| （対照）`meunier` | **27** |

🔴 **すなわち、この生産者は自分では一切「認証」を語らない。**
**Ecocert の engagement は Agence Bio 側にのみ存在する。**
⚠️ **`Demeter` / `Biodyvin` / `HVE` の登録は本調査では見つからなかった。**
**「無い」の証明ではなく、「Agence Bio に有機 engagement があり、他の認証は確認できなかった」である。**

---

## Winemaking

### 🔴 ✅ 全キュヴェに共通する公式の実務

| 項目 | 記述 ✅ |
|---|---|
| **収穫** | **手摘み、`caisse de maraichage`** |
| 🔴 **マロラクティック発酵** | 🔴 ✅ **公式の全キュヴェ解説に `Fermentation malolactique` が例外なく明記されている。**<br>**Meunier 生産者としては明確な選択であり、公式が沈黙していない稀な項目である** |
| **硫黄** | **自家製 `soufre de mine`。キュヴェごとに mg/l 開示（上表）** |
| 🔴 **perpétuelle（永久ブレンド）** | 🔴 ✅ **2003 年起点。**「**リザーヴワインは 2003 年から 2020 年のもので、毎年新しい収穫の 50% で更新する**」 |
| **微量仕込** | ✅ **`Micro vinification en réduction dans des petits contenants en inox`（還元状態の小型ステンレス）**（`Les Fortes Terres` / `Les Vignes de mon Village`） |
| 🔴 **2017 年以降の方針** | 🔴 ✅ **門出のリキュールの糖・醸造補助剤・石油由来硫黄・新樽・酸化をすべて排除** |

### 🔴 ✅ キュヴェ別スペック（**公式 `/nos-cuvees/` より。canonical には 3 件しか無い**）

| キュヴェ | セパージュ | 糖（dégorgement 添加） | 熟成 |
|---|---|---|---|
| **L'Esquisse** | **70% Meunier / 30% Pinot Noir**、base 70% 2020 + 30% 2021 | **未定と明記** | **平均 18 か月** |
| **Eugène** | **80% Meunier / 20% Pinot Noir**、perpétuelle 2003/2020 | **2.5 g/l**（残糖 2.5 g/l） | **平均 18 か月** |
| **Eugène Longue Garde** | **80% Meunier / 20% Pinot Noir**、perpétuelle 2003/2017 | 🔴 **0 g/l** | 🔴 **平均 60 か月 sur lattes** |
| **Eugène Rosé** | **82% Meunier / 18% Pinot Noir** | **2.5 g/l** | **平均 18 か月** |
| **L'Anecdote 2019** | 🔴 **100% Chardonnay** | **0 g/l** | **36 か月** |
| **Les Vignes de mon Village** | **100% Meunier、`tirée liège`（コルク打栓熟成）**、2014–2020 の assemblage | **0 g/l** | **平均 20 か月** |
| 🔴 ⭐ **Les Terres d'Illite 2019** | 🔴 **80% Meunier / 20% Pinot Noir** | **2.5 g/l** | 🔴 **36 か月** |
| 🔴 ⭐ **Les Fortes Terres 2018** | 🔴 **100% Meunier** | 🔴 **0.5 g/l** | 🔴 **48 か月** |
| **La Confiance de mon Père 2019** | **100% Meunier、`Rosé de Saignée`** | **未定と明記** | **36 か月** |
| **Edmond Ratafia T'en Penses Quoi?** | **Ratafia Champenois 100% Meunier、50 cl** | — | — |

### 🔴 ✅ 特筆すべき醸造（公式の記述）

- 🔴 **`Eugène Rosé` —— 2 つの perpétuelle の組み合わせ。**
  「**われわれのロゼは、2003 年以来の 2 つの perpétuelle の assemblage で特徴づけられる —— 一方は白ワインの、他方は赤ワインの。
  後者は同一の Meunier の区画から得られ、8 年以上の古樽で熟成される。古い樽を使うことで、われわれは酸化を促そうとしている。
  長い低温プレ・ファーメンタリー・マセラシオンで仕込まれた Meunier の赤の特異性が、これを identitaire なロゼにしている**」
- 🔴 **`La Confiance de mon Père` —— Rosé de Saignée の全工程が公開されている。**
  「**手摘み、手選果、除梗、CO2 で不活性化したステンレスタンクへ Meunier の果粒を重力で投入。
  168 時間の低温プレ・ファーメンタリー・アンフュージョン、その後にセニエ。
  バリックでアルコール発酵、次いで中和のためステンレスへ移す。マロラクティック発酵。
  コラージュ・冷却処理・濾過はいずれも行わない**」
- 🔴 **`Edmond Ratafia` —— 「Edmond Moussé のレシピに則り、その秘密は息子と孫だけが受け継いだ」。**
  **自家製の `alcool surfin`（Meunier のワイン由来）、rebêche の微量仕込、rebêche のワインと marc の二度蒸留、
  Meunier の果汁のミュタージュ、自然の冷却、無濾過。**

⚠️ **公式に一切記載が無い**: アルコール度数、デゴルジュマン日（**ただし「裏ラベルに記載」と公式が明言**）、生産本数、
圧搾比率（`taille` の割合は `L'Esquisse` で定性的に触れるのみ）、発酵温度、ルミュアージュの方式、酵母。

---

## Style

### ✅ 公式の性格描写と食事の合わせ（**OBP 関連分を優先**）

| キュヴェ | 公式の記述 ✅ |
|---|---|
| 🔴 ⭐ **Les Terres d'Illite 2019** | 「**このキュヴェの名は緑色粘土に由来する。**（…）**この地質的なワインの個性は、最も美しい緑色粘土を備えた区画の選抜にかかっている。**」<br>**2019 年**: 「**収穫開始は 9 月 13 日。かなり湿った冬ののち、早い春、そして窪地では全般的な霜**」<br>**合わせ**: 「**総じてオリーブ油で調理したタパス —— タコ、クロケッタ、パン・コン・トマテと生ハム、ピーマン、パタタス・ブラバス、ボケロネス、ガンバスとチョリソ…**」 |
| 🔴 ⭐ **Les Fortes Terres 2018** | 🔴 「**`Les Fortes Terres` は 2005 年、当家で最初の 100% Meunier のキュヴェだった。毎年のブラインド試飲で、このリュー・ディのワインの質が強く印象に残ったから、この一片のテロワールを選んだ。このワインの力強さと張りが、この唯一の土壌の identité を translate している。**」<br>**土壌**: 「**Cuisles、リュー・ディ `Les Fortes Terres` に由来する 4 区画。斜面中腹の大きな傾斜は、何百年もの浸食の影響で浅い土壌になっている。ここでは緑色粘土が数センチのところにあり、ブドウは凝縮し、白い果実、とりわけ白桃が前に出る。**」<br>**2018 年**: 「**収穫開始は 9 月 6 日**」<br>🔴 **飲み頃**: 「**裏ラベルに記載されたデゴルジュマン日の 6 か月後が理想**」／🔴 **`Garde: 20 ans`**<br>**合わせ**: 「**北京ダック、あるいは鴨のあらゆる変奏**」 |
| **Les Vignes de mon Village** | 🔴 「**この 100% Meunier は、まさに美食のシャンパーニュである。十全に表現されるには、カラフェに移してはならず、試飲の 5 分前に白ワイン用のグラスに注ぐこと。そうすれば酸素との接触はより穏やかになる**」／合わせ: **ソースをかけない白身肉、あるいは単にパイ菓子** |
| **L'Anecdote 2019** | 「**理想の合わせはホタテのカルパッチョ、あるいは新鮮な柑橘を添えた伊勢海老のグリル**」／**デゴルジュマンの 1 年後が理想**／**`Garde: 10 ans`** |
| **L'Esquisse** | 「**果実に寄り、若いうちに飲まれるよう考えられたキュヴェで、`taille` の比率が高く、それが大きな buvabilité を与える**」／合わせ: **よい友人、家族、日射し（あるいは無くとも）、アーモンド・ドライフルーツ・スイカのアペリティフ** |
| **Eugène** | 合わせ: 🔴 **「国際的なストリートフード —— ピッツァ、フォカッチャ、バーガー、ナゲット、小麦のタコス、ピタパン、ブリック、サモサ、チーズのフリット…」** |
| **Eugène Longue Garde** | 🔴 「**この Longue Garde 版は、Meunier がすべての清涼さと張りを保ったまま熟成しうることを示す**」／合わせ: **「素晴らしいヴォロヴァン！」** |
| **Eugène Rosé** | 合わせ: **パテ・アン・クルート、ニンニクのサラミ、日本の食パンのクロックムッシュ、コッパ、ランスのハム…** |
| **La Confiance de mon Père 2019** | 合わせ: **「包丁で刻んだステーク・タルタル」**／**`Garde: 10 ans`** |

🔴 ⚠️ **公式サイトには、いわゆる「テイスティングノート」（色・香り・味わいの記述）が存在しない。**
**あるのは土壌・醸造・食事の合わせ・熟成能力である。**
**Taittinger のような造り手署名のテイスティングノートは、この生産者には無い。** → §Staff Notes ⚠️ ⑥

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本。2 本が alias、3 本が `unresolved`**）

| # | メニュー印字（生産者 / ワイン） | VT | 価格 | メニュー節 | ✅ **公式での確認結果** |
|---|---|---|---|---|---|
| 1 | `Famille Moussé` — `'Terre d'Illite,' Extra Brut` | **2020** | **$275** | `… \| BLANC DE NOIRS` | ⚠️ 🔴 **キュヴェは実在するが、公式の名は `Les Terres d'Illite`（複数形＋定冠詞）。**<br>🔴 **公式サイトが掲示するのは `Les Terres d'Illite 2019` のみで、`2020` は公式に現れない。**（「存在しない」ではなく「公式が沈黙」）<br>🔴 **公式セパージュは `80% MEUNIER 20% PINOT NOIR`。canonical の `Pinot Meunier 100%` と矛盾** |
| 2 | `Famille Moussé` — `'Terre d'Illite,' Extra Brut` | **2019** | **$275** | `… \| BLANC DE NOIRS` | ✅ 🔴 **`Les Terres d'Illite 2019` として公式に実在。現行掲示。**<br>**公式スペック: 80% Meunier / 20% Pinot Noir、糖 2.5 g/l、熟成 36 か月、収穫開始 2019-09-13**<br>⚠️ **公式は `Extra Brut` の語も `Blanc de Noirs` の語もこのキュヴェに使っていない**（2.5 g/l は EU 規則上 Extra Brut の範囲内ではある） |
| 3 | `Moussé Famille` — `'Les Fortes Terres,' Extra Brut` | **2020** | **$400** | 🔴 `… \| **SPÉCIAL CLUB**` | ⚠️ 🔴 **キュヴェは実在するが、公式が掲示するのは `2018` のみ。`2020` は公式に現れない。**<br>🔴 **公式に `Special Club` の語は無く、生産者は Club Trésors de Champagne の会員名簿にも無い** |
| 4 | `Moussé Famille` — `'Les Fortes Terres,' Extra Brut` | **2019** | **$360** | 🔴 `… \| **SPÉCIAL CLUB**` | ⚠️ 🔴 **同上。`2019` は公式に現れない** |
| 5 | `Moussé Famille` — `'Les Fortes Terres,' Extra Brut` | **2018** | **$360** | 🔴 `… \| **SPÉCIAL CLUB**` | ✅ 🔴 **`Les Fortes Terres 2018` として公式に実在。現行掲示。**<br>**公式スペック: 100% Meunier、Cuisles のリュー・ディ `Les Fortes Terres` の 4 区画、糖 0.5 g/l、熟成 48 か月、収穫開始 2018-09-06、`Garde 20 ans`**<br>🔴 **公式に `Special Club` の語は無い** |

🔴 **5 本のうち公式で現物の年まで裏が取れたのは 2 本（`Les Terres d'Illite 2019` と `Les Fortes Terres 2018`）。**
🔴 **残る 3 本（Illite 2020 / Fortes Terres 2019・2020）は「キュヴェは実在するが、その年は公式サイトに掲示が無い」。**
⚠️ **公式サイトは各キュヴェについて現行リリース 1 年しか掲示せず、ヴィンテージ一覧を持たない。
したがって「2020 は存在しない」とは言えない。** → Open Questions 1

### 🔴 メニュー印字 × 公式名 × canonical 名 の三者対照

| | メニュー印字 | 🔴 公式の正式名 | canonical の名 |
|---|---|---|---|
| **生産者** | 🔴 **`Famille Moussé` と `Moussé Famille` の 2 通り** | ✅ **`Champagne Moussé Fils`**（法人 `SARL FAMILLE MOUSSE`） | 🔴 **`Famille Mousse` と `Mousse Fils` の 2 レコード** |
| **キュヴェ A** | `'Terre d'Illite,'`（単数・冠詞なし） | 🔴 **`Les Terres d'Illite`（複数・定冠詞つき）** | `Terre d'Illite Blanc de Noirs Extra Brut` |
| **キュヴェ B** | `'Les Fortes Terres,'` | ✅ **`Les Fortes Terres`**（一致） | 🔴 **`Les Fortes Terres Extra Brut Special Club`** |

🔴 **`Moussé Famille` はメニュー側の語順転倒である。公式にこの語順は存在しない。**
🔴 **`Terre d'Illite` → `Les Terres d'Illite` は「冠詞 ＋ 単複」の二重のずれで、`C-1` 族の形状。**
✅ **なお `Terre d'Illite` のアポストロフィはフランス語の正当なエリジオン（`de` + `Illite`）であり、
`S-2`（引用符の埋め込み）とは無関係。**
⚠️ **ただし OBP 印字 `'Terre d'Illite,'` の外側を囲む `'…,'` は `S-2` そのものである。
内側のエリジオンと外側の引用符を混同しないこと。**

### ✅ 公式の全キュヴェ 10 点（**canonical には 3 件しか無い**）

| # | 公式キュヴェ | canonical |
|---|---|---|
| 1 | **L'Esquisse** | ❌ 無し |
| 2 | **Eugène** | ❌ 無し |
| 3 | **Eugène - Longue Garde** | ❌ 無し |
| 4 | **Eugène Rosé** | ❌ 無し |
| 5 | **L'Anecdote 2019**（100% Chardonnay） | ❌ 無し |
| 6 | **Les Vignes de mon Village** | ❌ 無し |
| 7 | 🔴 ⭐ **Les Terres d'Illite 2019** | ✅ 2 件（2019 / 2020、`Famille Mousse` 名義） |
| 8 | 🔴 ⭐ **Les Fortes Terres 2018** | ✅ 1 件（2018 のみ、`Mousse Fils` 名義） |
| 9 | **La Confiance de mon Père 2019**（Rosé de Saignée） | ❌ 無し |
| 10 | **Edmond Ratafia T'en Penses Quoi?**（Ratafia Champenois） | ❌ 無し |

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① ヴァレ・ド・ラ・マルヌの Cuisles、「徹底的にムニエ」の造り手。1629 年から 12 世代。**
「**マルヌ川に直交する小さな谷、キュイスル村**の造り手です。
造り手が自分のサイトの一行目に掲げている言葉が **『profondément meunier —— 徹底的にムニエ』**。
**畑はキュイスル、ジョンクリ、シャティヨン＝シュル＝マルヌの 3 村**にありますが、
造り手いわく **『すべて同じ一つの斜面の上、全面南向き』**です。
**父から子へ 1629 年以来 12 世代のブドウ栽培者、醸造家としては 4 世代。
最初の 1 本は 1923 年、ウジェーヌ・ムセが造りました。**現当主は **セドリック・ムセ**で 2003 年からです。」

**② キュヴェ名の『イリット』は土壌の名前。緑色粘土のことです。**
「**イリット（Illite）は粘土鉱物の名前**で、造り手の土壌の **90% が『石灰質マルヌの上の緑色粘土』**。
造り手の説明では **『われわれの土壌は浅く、必ず厚い緑色粘土の脈がある。ペドロジーでイリットと呼ばれるものだ』**。
**夏の長い乾燥期に湿気が残る唯一の層がこの緑色粘土**で、
**その粘土がいちばん美しい区画を選んだのがこのキュヴェ**です。
土壌断面まで公開していて、**表土 20 cm / 粘土質砂 40 cm / 緑色粘土 30 cm / 石灰質マルヌ**の 4 層です。」

**③ 『レ・フォルト・テール』は 2005 年に始まった、当家最初のムニエ 100%。熟成 48 か月、糖 0.5 g/l。**
「**キュイスルのリュー・ディ『レ・フォルト・テール』の 4 区画**から。
造り手の言葉では **『毎年のブラインド試飲でこのリュー・ディのワインの質が強く印象に残ったから選んだ』**。
**斜面中腹の急斜面で、何百年もの浸食で土が浅く、緑色粘土が数センチ下にある。
だからブドウが凝縮して、白い果実、とくに白桃が前に出る**と造り手は書いています。
**2018 年は 9 月 6 日収穫開始、熟成 48 か月、門出の糖は 0.5 g/l、熟成能力 20 年。**
造り手は **『裏ラベルのデゴルジュマン日から 6 か月後が理想』**とし、**合わせは北京ダック**を挙げています。」

### 追加で使える一手

- 🔴 **戦争史**: 「**創業者ウジェーヌは対独レジスタンスでした。**
  1943 年 11 月に英米の落下傘飛行士 2 名を 12 日間匿い、**1944 年 6 月 21 日に息子エドモンとともにゲシュタポに逮捕**。
  ノイエンガンメへ送られ、**1945 年 4 月 12 日にラーフェンスブリュックでチフスにより亡くなっています。**
  **1947 年の『シャンパーニュ・ムセの再生』は、生還した息子エドモンによるものです。**」
  ⚠️ **重い話題なので、客が沿革を尋ねた時だけ。自分から持ち出さない。**
- 🔴 **ムニエ 100% の話法**: 「**現行 10 キュヴェのうち 8 つがムニエ主体、3 つがムニエ 100%。**
  唯一の例外がシャルドネ 100% の『**ラネクドット**』で、造り手自身が
  **『キュイスルにそれまで 100% シャルドネは存在しなかった』**と書いています。」
- 🔴 **硫黄の話**: 「**自家製の『鉱山硫黄』を使っていて、キュヴェごとに mg 単位で数字を公開しています。**
  **レ・フォルト・テールは 26 mg/l、レ・テール・ディリットは 11 mg/l。**
  **2017 年に『すべての仮面 —— 門出の糖、醸造補助剤、石油由来の硫黄、新樽、酸化 —— を取り去る』**と決めた造り手です。」
- 🔴 **ペルペチュエル**: 「**2003 年から続く永久ブレンドを持っていて、毎年新しい収穫の 50% で更新します。**
  **『ウジェーヌ』は 2003/2020、その長期熟成版は 2003/2017 で 60 か月寝かせ、糖はゼロです。**」
- **2014 年**: 「**2014 年に合成農薬を完全にやめています。**造り手の言葉で『**賭けに成功した**』と書かれています。」
- **サーヴィス**: 「**造り手が明示的に指定しています —— カラフェに移さず、白ワイン用のグラスに、
  飲む 5 分前に注ぐ。そのほうが酸素との接触が穏やかになる、と。**」（`Les Vignes de mon Village` の記述）

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／出典が矛盾している**）

1. 🔴 ⚠️ **『スペシャル・クラブ』と説明しない。**
   **公式サイト全文（12 ページ・69,221 文字）に `club` / `spécial` / `special` の出現が 0 件。**
   **さらに Club Trésors de Champagne の公式会員名簿（現行 25 軒、2026-08-05 取得・HTML 411KB）に Moussé は無い。**
   🔴 **`Spécial Club` は Club Trésors de Champagne の集合的呼称であり、会員でなければ名乗れない。**
   **THÉSEUS の DB はキュヴェ名に `Special Club` を含んでいるが、その裏づけは取れていない。**
   ⚠️ **メニュー自身が `SPÉCIAL CLUB` の節に置いているため、客から聞かれる可能性が高い。**
   **その場合は『造り手の公式にはその記載がありません』と答え、実ボトルのラベルを確認すること。**
2. 🔴 ⚠️ **『オーガニック』『ビオ』と言わない。とくに 2018 / 2019 / 2020 については言ってはならない。**
   **Agence Bio における有機 engagement の開始は `2022-09-01` であり、
   OBP に載る 3 ヴィンテージはいずれもそれ以前の収穫である。**
   **さらに 2026 年参照でも畑は `AB`（認証済）・`C1`（転換 1 年目）・`CS`（非有機）が混在している。**
   **言えるのは『**2014 年に合成農薬を完全にやめた**』『**2022 年から Ecocert で有機の手続きに入っている**』まで。**
3. 🔴 ⚠️ **『レ・テール・ディリットはムニエ 100%』と言わない。**
   **公式は `80% MEUNIER 20% PINOT NOIR` と明記している。**
   **THÉSEUS の DB は `Pinot Meunier 100%` としているが、これは公式と矛盾する。**
   **ムニエ 100% なのは `Les Fortes Terres`・`Les Vignes de mon Village`・`La Confiance de mon Père` の 3 つ。**
4. 🔴 ⚠️ **キュヴェ名を『テール・ディリット』（単数）と言い切らない。**
   **公式の表記は `Les Terres d'Illite`（定冠詞つき複数）である。**
   **メニューの印字は単数だが、造り手の表記は複数。**
5. 🔴 ⚠️ **メニューの 2020（イリット）・2019 / 2020（フォルト・テール）を『公式確認済み』として語らない。**
   **公式サイトが掲示しているのは `Les Terres d'Illite 2019` と `Les Fortes Terres 2018` だけである。**
   **公式はキュヴェごとに現行リリース 1 年しか出さないので、
   『存在しない』ではなく『裏が取れていない』。**
6. 🔴 ⚠️ **テイスティングノート（色・香り・味わい）を造り手の言葉として語らない。**
   **公式サイトにテイスティングノートは一切存在しない。**
   **あるのは土壌・醸造・食事の合わせ・熟成能力だけ。**
   **言えるのは『**造り手は白い果実、とくに白桃が前に出ると書いている**』（`Les Fortes Terres` の土壌解説）まで。**
7. 🔴 ⚠️ **畑の面積（ha）を言わない。** **公式サイトに数字が一切無い。**
8. 🔴 ⚠️ **『キュイスルのムセ』と言うだけで一意だと思わない。**
   🏛 **同じ Cuisles に別法人 `MOUSSE`（SIREN 534 379 938、2 rue du Four à Chaux、
   代表 Mathieu Moussé / Nicolas Moussé）が実在する。**
   **本生産者は `SARL FAMILLE MOUSSE`（SIREN 449 670 702、3 rue de Jonquery、代表 Cédric Moussé）。**
9. ⚠️ **アルコール度数・デゴルジュマン日・生産本数を言わない。**
   **公式に一切無い。**（**ただしデゴルジュマン日は「裏ラベルに記載」と公式が明言しているので、実ボトルで読める。**）
10. ⚠️ **『ブラン・ド・ノワール』を造り手の言葉として使わない。**
    **公式はこのキュヴェにその語を使っていない。**
    **メニューの節見出しであって、造り手の表記ではない。**
    （**80% Meunier + 20% Pinot Noir はいずれも黒ブドウなので事実としては誤りではないが、造り手の語ではない。**）
11. ⚠️ **第三者点数を言わない。** **本調査で取得した公式資料に点数の掲載は一切無い。**
    **canonical の `points`（94 / 95 / 94）の出所は不明である。**
12. ⚠️ **『RM（レコルタン・マニピュラン）』と断定しない。**
    **公式サイトに `récoltant` / `manipulant` / 資格記号の記載が 0 件で、本調査では確認できなかった。**
    **資格記号はラベルに必ず印字されるので、実ボトルで確認できる。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **本件は既存の登録票 `P-2` に該当する。新しい番号は開かない。**
🔒 **`research/canonical_conflicts/REGISTER.md` は本書では一切編集していない（読み取りのみ）。**
🔒 **canonical も編集していない。統合も行っていない。**

---

### 🔴 `P-2`（既存）—— **Famille Moussé / Moussé Fils。本調査で「公式確認」を供給する**

`P-2` は「**公式確認後に統合 or 親子明示。自動統合は禁止**」を推奨として保留していた。
**本ドシエはその公式確認を供給する。以下は `P-2` への追加証拠であり、裁定ではない。**

#### 追記 1 —— 🔴 **単一 SIREN が両名を担っていることの公的証拠**

🏛 **Agence Bio 事業者レコード `numeroBio 44958`（id 123874）は、
ただ 1 つの SIRET に対して 2 つの名前を並記している:**

| フィールド | 値 |
|---|---|
| **`raisonSociale`** | 🔴 **`SARL CHAMPAGNE MOUSSE FILS`** |
| **`denominationcourante`** | 🔴 **`SARL FAMILLE MOUSSE`** |
| **`siret`** | **`44967070200025`** |
| **`gerant`** | **`Cédric Moussé`** |
| **`codeNAF`** | `01.21Z` |

🏛 **`recherche-entreprises.api.gouv.fr` 側の同一 SIREN `449 670 702`:**
`nom_complet` = **`SARL FAMILLE MOUSSE`**、`dirigeants` = **`MOUSSE, CEDRIC ROGER EDMOND`（Gérant）**、
`date_creation` = `2003-08-01`、`siege` = `3 RUE DE JONQUERY 51700`、`liste_id_bio` = `[44958]`。

🔴 **したがって `Moussé Fils` と `Famille Moussé` は 2 軒ではない。単一法人の 2 つの名前である。**
**`Champagne Moussé Fils` が商号（サイトの mentions légales が掲げる名）、
`SARL Famille Moussé` が登記名。**

#### 追記 2 —— 🔴 **公式サイトが両キュヴェを同一の「Nos cuvées」ページに並べている**

✅ **`https://champagnemousse.fr/nos-cuvees/`（および `/en/our-wines/`）は、
`Les Terres d'Illite` と `Les Fortes Terres` を、他の 8 キュヴェとともに
同一ページ・同一書式で掲載している。**
🔴 **すなわち両者は同一の造り手の同一ラインナップであり、別ブランドではない。**

#### 追記 3 —— 🔴 **canonical の `description_en` が公式と正面から矛盾している**

🔍 **canonical `mousse-fortes-terres-2018` の `description_en`:**
「**Mousse Fils is a Pinot Meunier specialist grower in Cuisles (separate brand from Famille Mousse).**」
🔴 **`separate brand from Famille Mousse` は公的登録と公式サイトの双方に反する。**
**これは既知の罠「canonical の `obp_note` / `description` 散文は信用できない」の新しい実例である。**

#### 追記 4 —— 🔴 ⚠️ **`P-2` の影響見積り「3 本」への反証**

`P-2` は「**影響: OBP 3 本**」「**統合されれば Packet B から 3 件消える**」と記録している。
🔴 **本調査の実測では、統合で解決するのは 1 本だけである。**

🔍 **canonical に存在する `Les Fortes Terres` は `mousse-fortes-terres-2018` の 1 レコードのみ**
（`producer='Mousse Fils'`、`vintage='2018'`）。
🔍 **OBP 側は 2018 / 2019 / 2020 の 3 行。**

| OBP 行 | 実体統合後に解決するか |
|---|---|
| **2018**（$360） | ✅ **解決する** |
| **2019**（$360） | 🔴 **解決しない —— canonical にこのヴィンテージが無い** |
| **2020**（$400） | 🔴 **解決しない —— canonical にこのヴィンテージが無い** |

🔴 **したがって `P-2` の実体分裂が説明するのは 1 本であり、残る 2 本は
「実体分裂」ではなく「canonical にヴィンテージが無い」＝ gap である。**
⚠️ **この 2 本は統合を行っても `unresolved` のまま残る。**
**`P-2` の影響欄は、実体分裂 1 本 ＋ ヴィンテージ gap 2 本に分解されるべきである。**
🔒 **どう記録するかは CTO の判断。本書は REGISTER.md を書き換えていない。**

#### 追記 5 —— **推奨（🔒 実行していない。`P-2` の既存推奨を変更しない）**

- **公式確認は得られた。ただし「統合」と「親子明示」のどちらを採るかは設計判断であり、本書では決めない。**
- ⚠️ **統合する場合の表示名は、公式の商号 `Champagne Moussé Fils` を canonical name とし、
  `Famille Moussé` / `SARL Famille Moussé` / `Moussé Famille`（メニューの語順転倒）を alias に置くのが公式記述と整合する。**
- 🔒 **自動統合は禁止という `P-2` の但し書きを本書は解除しない。**

---

### 🔴 新しい形状（**既存のどの族にも当たらない。未採番 —— 番号は CTO の判断**）

#### 形状 A 🔴 —— **canonical のキュヴェ名に、裏づけの取れない団体呼称が埋め込まれている**

**対象**: `mousse-fortes-terres-2018` の `name` = **`Les Fortes Terres Extra Brut Special Club`**
（`classification` = `Extra Brut Special Club`、`tags` に `Special Club`）

**問題**:
🔴 **`Spécial Club` は Club Trésors de Champagne（1971 年創設）の集合的呼称であり、
キュヴェ名の一部ではなく、会員資格に紐づく団体の指定である。**

**証拠**:
- ✅ **公式サイト全 12 ページ本文（69,221 文字）を機械走査した結果、
  `club` / `spécial` / `special` の出現は 0 件**（対照: `meunier` は 27 件）。
  **`Les Fortes Terres 2018` の公式解説にもこの語は無い。**
- 🏛 **Club Trésors de Champagne の公式会員ページ
  （`clubtresorsdechampagne.com/le-club-tresors-de-champagne/les-vignerons-du-club/`）を直接取得（HTML 411,899 B）。
  掲載会員は 25 軒で、`mousse` の出現は 0 件。**
  会員は Paul Bara / Roland Champion / Charlier & Fils / Gaston Chiquet / Dumenil / Forget-Chemin /
  Fresnet-Juillet / Pierre Gimonnet et Fils / Henri Goutorbe / Grongnet / Marc Hébrart / Hervieux-Dumez /
  Vincent Joudart / Juillet-Lallement / J. Lassalle / Pertois-Moriset / Loriot-Pagel / A. Margaine /
  Rémy Massin et Fils / José Michel / Morel / Nominé-Renard / Salmon / Sanchez Le Guédard / Vazart-Coquart et Fils。
- 🔍 **canonical の `obp_note` は「**ムス・フィスがムニエの品質ポテンシャルを SGC に認めさせた証**」と書くが、
  この主張の出所は不明であり、上記 2 点と整合しない。**

⚠️ **保留すべき不確実性（消さない）**:
- **取得した名簿は「2026-08-05 時点の現会員」である。過去の会員履歴は公開されていない。**
  **したがって「過去に一度も会員でなかった」ことは証明されていない。**
- 🔴 **OBP のメニュー自身が 3 行を `SPÉCIAL CLUB` の節に置いている。
  すなわち矛盾は canonical だけでなくメニュー側にも存在する。**
  **どちらが誤りかは、実ボトルのラベル（Spécial Club はボトル形状も専用のものが定められている）でしか決まらない。**

**モデリング上の問い（🔒 決めない）**:
🔴 **仮に会員だったとしても、`Special Club` をキュヴェ名の文字列に含めるべきかは別問題である。**
**`Spécial Club` は生産者横断の団体指定であり、`Grand Cru` や `HVE` と同じく
「キュヴェ名」ではなく「キュヴェの属性」として持つほうが構造的に正しい可能性が高い。**
**現状のように名前の文字列に溶かし込むと、25 軒すべてのキュヴェ名に同じ語が入り、
かつ照合時に `Les Fortes Terres` という印字と一致しなくなる（実際に本件で 3 行が未解決になっている）。**
🔒 **これは設計判断であり、本書では実行も決定もしていない。**

**OBP への影響**: 🔴 **3 行が `unresolved`。うち 1 行（2018）はこの名前の不一致が直接の原因。**

---

#### 形状 B 🔴 —— **canonical のセパージュが公式と矛盾している（散文ではなく構造化フィールド）**

**対象**: `mousse-terre-dillite-2020` / `mousse-terre-dillite-2019` の **`grapes = ["Pinot Meunier 100%"]`**

**証拠**:
- 🔴 ✅ **公式 `/nos-cuvees/` の `Les Terres d'Illite 2019` の見出しは
  `80% MEUNIER 20% PINOT NOIR`。EN 版も同一。**
- 🔍 **canonical の `description` / `description_en` も
  「ピノ・ムニエ100%のブラン・ド・ノワール」「100% Pinot Meunier Blanc de Noirs」と書いており、
  構造化フィールドと散文の双方が同じ誤りを持つ。**

**あわせて食い違う値**:

| 項目 | 🔍 canonical | ✅ 公式（2019） |
|---|---|---|
| **セパージュ** | 🔴 `Pinot Meunier 100%` | 🔴 **`80% Meunier / 20% Pinot Noir`** |
| **dosage** | `Extra Brut — 3 g/L` | **`2,5 g/l`（dégorgement 添加）** |
| **aging** | `3+ years sur lie`（2020）/ `4+ years`（2019） | **`36 mois`（年による区別の記載なし）** |
| **color** | `Blanc de Noirs` | ⚠️ **公式はこの語を使っていない** |

🔴 **`Les Fortes Terres 2018` 側も dosage が食い違う: canonical `3 g/L` ／ 公式 `0,5 g/l`。**
（**熟成 `4+ years sur lie` ／ 公式 `48 mois` は整合。セパージュ `Pinot Meunier 100%` ／ 公式 `100% MEUNIER` も整合。**）

**なぜ重要か**:
🔴 **これは `obp_note` の散文の誤りではなく、`grapes` / `dosage` という構造化フィールドの誤りである。**
**既知の罠は「canonical の散文は信用できない」だったが、本件は
「構造化フィールドも公式と照合されていない」ことを示す。**

**OBP への影響**: ⚠️ **照合には影響しない（`grapes` はマッチングに使われていない）。
しかし staff 向け表示に出れば、卓上で『ムニエ 100%』という公式に反する説明を生む。** → §Staff Notes ⚠️ ③

---

#### 形状 C —— **既存の族に該当するもの（新しい番号は開かない）**

- **`C-1`（語順・アクセント揺れ）** — 🔴 **本件は 3 重にこの族である。**
  - **アクセント**: 公式は一貫して **`Moussé`**。canonical は表示名レベルで **`Famille Mousse` / `Mousse Fils`** と
    **アクセントを落としている**（id だけでなく `producer` フィールドそのもの）。
  - **語順**: メニューが **`Famille Moussé`** と **`Moussé Famille`** の 2 通りを印字している。
    **公式にはどちらの語順も無く、正しくは `Champagne Moussé Fils`。**
  - **冠詞・単複**: **`Terre d'Illite`（メニュー・canonical）** ／ **`Les Terres d'Illite`（公式）**。
- **`S-2`（引用符の埋め込み）** — **OBP 印字は `'Terre d'Illite,'` および `'Les Fortes Terres,'` で、
  アポストロフィとカンマがキュヴェ名の内側に入っている。**
  ⚠️ 🔴 **ただし `Terre d'Illite` の `d'` は正当なフランス語のエリジオンであり `S-2` ではない。
  外側を囲む `'…,'` だけが `S-2` である。両者を同一視しないこと。**
- **`C-4`（識別語を持たないキュヴェ名）** — ⚠️ **本件は当たらない。**
  `Les Fortes Terres` も `Les Terres d'Illite` も、それ自体で一意なリュー・ディ／土壌名である。

---

#### 🔴 gap（**conflict ではない。canonical に不在**）

- 🔴 **`Les Fortes Terres` の 2019・2020 が canonical に無い**（2018 のみ）。
- 🔴 **公式の全 10 キュヴェのうち 7 つが canonical に一切無い** ——
  `L'Esquisse` / `Eugène` / `Eugène Longue Garde` / `Eugène Rosé` / `L'Anecdote` /
  `Les Vignes de mon Village` / `La Confiance de mon Père` / `Edmond Ratafia`。
- ⚠️ **どの register class もこれを覆わない。gap であって conflict ではない。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY / `D-2026-08-05-09`**）

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の名を掲げているか** | ✅ **合格。** `https://champagnemousse.fr/mentions-legales/` が **「Directeur de la publication: `CHAMPAGNE MOUSSE FILS`, 5 Rue de Jonquery, 51700 Cuisles」** を明記。EN 版 `/en/legal-notices/` も同一 |
| 🔴 **(c) 公的登録と一致する住所** | 🔴 ✅ **合格。** 🏛 **`SARL FAMILLE MOUSSE`（SIREN 449 670 702）の登記住所は `3 rue de Jonquery, 51700`。** **同じ通り。** さらに 🏛 **Agence Bio が同一 SIRET に `SARL CHAMPAGNE MOUSSE FILS` の名を記録**しており、**サイトの掲げる名と公的登録が一致する**<br>⚠️ **番地は 5（サイト）と 3（登記）で異なる。`5 rue de Jonquery` は 🏛 `CEDRIC MOUSSE ACCOMPAGNEMENT`（SIREN 818 231 623）の登記住所でもある。同一集落内の関連番地と判断したが、この差自体は記録する** |
| **(d) 整合した商業・法務フッター** | ✅ **合格。** 年齢確認ゲート（`Je certifie avoir l'âge légal pour consommer de l'alcool dans mon pays de résidence.`）、mentions légales、charte de confidentialité、cookie 管理（tarteaucitron）、制作・ホスティング事業者（**Agence Équinoxes, Rue des Moines, 02200 Villeneuve-Saint-Germain**）を明示 |
| **免責的な「ファンサイト」表記** | **無し** |
| **ドメイン売却／パーキングの兆候** | **無し**（WordPress + Yoast SEO の実運用サイト。`page-sitemap.xml` の `lastmod` は **2026-07-17**） |
| 🔴 **`NOT_THE_PRODUCER_*` として退けたもの** | 🔴 **無し。** **本調査で事実の根拠に用いたのは `champagnemousse.fr` と公的登録のみ。**<br>⚠️ **WebSearch の結果には輸入業者・小売（`succul.fr` / `craftetcompagnie.com` / `vynluna.com` / `berkeleyandstuart.com` / `comptoirdesmillesimes.com` / `thehappyvine.net`）と批評媒体（`worldoffinewine.com`）、および `substack.com` のニュースレターが並んだが、**🔴 **いずれも一次資料として採用していない。**<br>🔴 **とくに「畑 5.5 ha」「12 代目」という数字が複数の非公式ソースに出るが、`ha` は公式に無いため本書は採用していない**（`12 世代` のみ公式に存在するので採用） |
| 🔴 **Wikipedia** | 🔴 **検索結果に `en.wikipedia.org/wiki/Club_Trésors_de_Champagne` が出たが、方針どおり一切開いていない・使用していない。**<br>**Club の会員名簿は Club 自身の公式サイトから直接取得した。** |

### 一次資料（**公式ドメイン ＋ 公的登録のみ**）

| 資料 | 取得した情報 |
|---|---|
| **`/robots.txt`** | `sitemap` の指定を確認。`/sitemap.xml` は `/sitemap_index.xml` へ 301 |
| **`/sitemap_index.xml` → `/page-sitemap.xml`** | **FR / EN 併せて 20 URL。**`lastmod 2026-07-17`。**`post-sitemap.xml` は空（投稿型コンテンツ無し）** |
| 🔴 **`/wp-json/wp/v2/pages`（FR 12 件・EN 11 件、`content` 全文）** | 🔴 **本ドシエの本体。**⚠️ **サイトは年齢確認ゲートで通常取得では本文が出ないため、REST API 経由で取得した。**<br>**`nos-cuvees` / `notre-histoire` / `philosophie` / `contact-visites` / `dans-le-monde` / `mentions-legales` ＋ EN 対応版** |
| 🔴 **`/nos-cuvees/` ＋ `/en/our-wines/`** | 🔴 **全 10 キュヴェのセパージュ・糖・熟成月数・リュー・ディ・土壌・硫黄 mg/l・食事の合わせ・熟成能力。**<br>🔴 **`Les Terres d'Illite 2019` = 80% Meunier / 20% Pinot Noir / 2.5 g/l / 36 mois。**<br>🔴 **`Les Fortes Terres 2018` = 100% Meunier / 0.5 g/l / 48 mois / 4 区画 / 2005 年に当家初のムニエ 100% / Garde 20 ans。**<br>🔴 **両者が同一ページに並ぶ ＝ `P-2` 追記 2** |
| 🔴 **`/notre-histoire/` ＋ `/en/our-history/`** | 🔴 **§History の全体。**1629 / 1880 / 1896 / 1922 / 1923 / 1926 / 1939 / 1943 / 1944 / 1945 / 1947 / 1976 / 1990 / 2003 / 2009 / 2013 / 2014 / 2017 / 100 周年。**レジスタンスと強制収容所の記述を含む** |
| **`/`（`/en/`）** | **`profondément meunier…` / `Deeply Meunier...`、Cuisles、1923 年以来、3 村・同一南向き斜面、12 世代 / 4 世代、緑色粘土** |
| 🔴 **`/mentions-legales/` ＋ `/en/legal-notices/`** | 🔴 **真正性の検証と商号の確定。`Directeur de la publication: CHAMPAGNE MOUSSE FILS, 5 Rue de Jonquery, 51700 Cuisles`** |
| **`/philosophie/`** | **Saint-Exupéry の引用 1 行のみ**（「われわれは大地を親から受け継ぐのではない、子から借りているのだ」）。⚠️ **栽培哲学の実質的な記述は無い** |
| 🔴 **`recherche-entreprises.api.gouv.fr`（`q=mousse cuisles`、22 件 ／ `q=mousse fils`、10 件 ／ SIREN 個別 4 件）** | 🔴 **`SARL FAMILLE MOUSSE` SIREN 449 670 702・gérant `MOUSSE, CEDRIC ROGER EDMOND`（1980-07 生）・2003-08-01 設立・NAF 01.21Z・`liste_id_bio [44958]`。**<br>🔴 **別系統の `MOUSSE` SIREN 534 379 938（Mathieu / Nicolas Moussé）の存在。**<br>**`GFV CHAMPAGNE MOUSSE ET FILS` SIREN 521 983 254（Cédric が Gérant、associés 約 32 名）ほか付随法人 6 件** |
| 🔴 **`opendata.agencebio.org/api/gouv/operateurs/?numeroBio=44958`** | 🔴 **`P-2` の決着証拠。`raisonSociale = SARL CHAMPAGNE MOUSSE FILS` ／ `denominationcourante = SARL FAMILLE MOUSSE` ／ 同一 SIRET `44967070200025` ／ `gerant = Cédric Moussé`。**<br>🔴 **Ecocert France `FR-BIO-01`、`ENGAGEE`、`dateEngagement 2022-09-01`（＝`datePremierEngagement`）、`Raisin de cuve` に `AB`+`C1`+`CS` 併存（参照年 2026）、`siteWebs` は空** |
| 🔴 **`clubtresorsdechampagne.com/le-club-tresors-de-champagne/les-vignerons-du-club/`（HTML 411,899 B 実取得）** | 🔴 **現行会員 25 軒の名簿。`mousse` の出現 0 件。**→ 形状 A の根拠 |
| **`clubtresorsdechampagne.com/en/members/`** | **英語版。`Champagne Morel` を「25 番目の会員」と記載。`Mousse` の言及なし。⚠️ 過去会員の記載は無い** |

### 取得できなかったもの / 存在しなかったもの

- 🔴 **公式サイトに `bio` / `certifi…` / `Ecocert` / `HVE` / `Demeter` / `biodynam…` / `durable` / `VDC` が
  1 件も出現しない**（FR 12 ページ 69,221 文字の機械走査）。**認証は生産者自身によって一切主張されていない。**
- 🔴 **公式サイトに `club` / `spécial` / `special` が 1 件も出現しない。**
- 🔴 **公式サイトに `récoltant` / `manipulant` / `matricul…` が 1 件も出現しない。**
  → **RM/NM/RC の資格記号と matriculation 番号は本調査では確定できなかった。** → Open Questions 2
- 🔴 **公式サイトに畑の面積（ha）の記載が一切無い。** → Open Questions 3
- 🔴 **公式サイトにテイスティングノート（色・香り・味わい）が一切無い。**
- 🔴 **公式サイトはキュヴェごとに現行リリース 1 年しか掲示せず、ヴィンテージ一覧を持たない。**
  **`Les Terres d'Illite` は 2019、`Les Fortes Terres` は 2018 のみ。**
  → **OBP の Illite 2020・Fortes Terres 2019/2020 は裏が取れない。** → Open Questions 1
- ⚠️ **公式のテクニカルシート（fiche technique）PDF が存在しない。**
  **`/nos-cuvees/` のページ本文がテクニカルシートの役割を果たしている。**
- ⚠️ **`/dans-le-monde/`（輸入元・取扱店の地図）は JS 埋め込みで、
  取扱業者の一覧は静的取得では読めなかった。**
- ⚠️ **`/contact-visites/` の予約ウィジェットは Base64 で埋め込まれた外部 iframe（`rosedesvins.co`）。
  訪問予約が可能であること以上の情報は得られない。**
- ⚠️ **Agence Bio の `siteWebs` が空。** 公式サイト URL は Agence Bio 側に登録されていない。
- ⚠️ **`Demeter` / `Biodyvin` / `HVE` の登録は本調査では確認できなかった。**
  **これは「登録が無い」の証明ではない。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical レコード 3 件（`migration/out/export/db_wine_canonical.json`、928 件中）:**

| id | producer | name | vintage |
|---|---|---|---|
| `mousse-terre-dillite-2020` | **`Famille Mousse`** | `Terre d'Illite Blanc de Noirs Extra Brut` | 2020 |
| `mousse-terre-dillite-2019` | **`Famille Mousse`** | `Terre d'Illite Blanc de Noirs Extra Brut` | 2019 |
| `mousse-fortes-terres-2018` | 🔴 **`Mousse Fils`** | 🔴 `Les Fortes Terres Extra Brut Special Club` | 2018 |

**共通**: `subregion='Cuisles — Vallée de la Marne'` / `region='Champagne'` / `dosage='Extra Brut — 3 g/L'` /
`grapes=['Pinot Meunier 100%']` / `serving_temp='9–11°C'` / `drinking_window='Now–2030'`。
`points` は 94 / 95 / 94。

🔍 **OBP 5 行**（`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`）:
**全 5 行が `producer_state = exact`、`proposed_canonical_producer_id = producer:famille-mousse` に割当。**
**`match_state` は Illite 2 行が `alias`（`confidence 0.9`）、Fortes Terres 3 行が `unresolved`（`confidence 0.0`）。**
🔍 **未解決 3 行の `evidence` は「`'Famille Mousse'` の canonical キュヴェ 1 件に一致無し: `'Les Fortes Terres'`」** ——
**すなわち matcher は `famille-mousse` 配下の 1 キュヴェしか見ておらず、
`mousse-fils` 配下の `Les Fortes Terres` に到達できていない。`P-2` の記述と整合する。**

⚠️ **`research/out/t-01/mapping.json` は本調査では参照していない。
上記の「解決/未解決」はすべて `obp_intake_normalized_20260804.json` から読んだものである。**
（既知の罠: 2 つの artifact は resolved 数が食い違う。**出典を明示する。**）

🔒 **canonical・`REGISTER.md`・intake JSON のいずれも編集していない。**

### 🔴 ソースキャッシュ

`research/producers/_sources/famille-mousse/`（gitignored）に 19 ファイルを保存:
`wpjson_pages_content.json`（FR 全文 121 KB）／ `wpjson_en.json`（EN 全文 108 KB）／
`sm_page-sitemap.xml` ／ `raw_home.txt` ／ `raw_robots.txt.txt` ／ `raw_sitemap.xml.txt` ／
`REGISTER_api_gouv_mousse_cuisles_full.json` ／ `REGISTER_api_gouv_mousse_fils.json` ／
`reg_449670702.json`（＋ `reg_famille_full.json`）／ `reg_521983254.json` ／ `reg_534379938.json` ／
`reg_818231623.json` ／ `agencebio_44958.json` ／ `clubtresors_vignerons.html`（411 KB）。
🔴 **`NOT_THE_PRODUCER_*` / `FANPAGE_*` / `IMPORTER_*` として保存したものは無い**（非公式ソースを一切採用しなかったため）。

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🔴 **商号・登記名・SIREN・SIRET・代表者名と生年・設立日・住所がすべて公的登録で確定。`P-2` の核心である「単一法人か否か」に決着がついた。**⚠️ **番地のみ 3/5 で揺れる** |
| **Overview** | **High** | 公式の自己規定（`profondément meunier`）、3 村・同一斜面、12 世代 / 4 世代、緑色粘土が一次で取れた |
| 🔴 **History** | 🔴 **High** | 🔴 **沿革ページが完全取得でき、1629 / 1880 / 1923 / 1926 / 1943 / 1944 / 1945 / 1947 / 1976 / 1990 / 2003 / 2009 / 2013 / 2014 / 2017 が確定。戦争史は日付レベルまで公式が記述している**<br>⚠️ **Eugène 以前の当主名と各世代の生没年は不明** |
| **Location** | **Medium-High** | 🔴 **村・3 村構成・斜面の向き・土壌組成・4 層の土壌断面・リュー・ディ 4 つが確定**<br>🔴 ⚠️ **面積（ha）と échelle des crus 上の格付が完全に不在。これが Medium-High に留める理由** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **公式の実務（1976 草生 / 2014 合成農薬全廃 / 2017 醸造の断絶 / 自家製鉱山硫黄の mg 単位開示）と、公的登録の認証実態（Ecocert `ENGAGEE`、engagement 2022-09-01、AB/C1/CS 併存）の双方が取れた。**<br>🔴 **「公式は認証を語らないが Agence Bio には登録がある」という食い違いを、両方記録したうえで卓上の誤りを塞いだ** |
| **Winemaking** | **Medium-High** | 🔴 **全 10 キュヴェのセパージュ・糖・熟成月数・硫黄値が公式で確定。マロラクティックが全キュヴェで明記されているのは稀な収穫**<br>⚠️ **アルコール度数・生産本数・発酵温度・ルミュアージュ・酵母・圧搾比率が不在** |
| ⚠️ **Style** | ⚠️ **Low-Medium** | 🔴 **公式にテイスティングノートが一切存在しない。**取れたのは土壌由来の性格描写（白桃）・食事の合わせ・熟成能力のみ。**本ドシエで最も弱い節であり、⚠️ ⑥ で卓上の経路を塞いだ** |
| ⚠️ **Important Cuvées** | ⚠️ **Medium** | 🔴 **OBP 5 本のうち公式で年まで裏が取れたのは 2 本のみ**（Illite 2019 / Fortes Terres 2018）。**残り 3 本はキュヴェの実在は確定、年は公式が沈黙。**<br>🔴 **一方で公式の正式名・セパージュ・糖・熟成は 2 本について完全に取れた** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **`P-2` は Agence Bio の単一 SIRET 二重名記載で決着。形状 A は公式全文走査 0 件 ＋ 会員名簿 411 KB 実取得 0 件。形状 B は公式の見出しと canonical の構造化フィールドの直接対照。**<br>⚠️ **形状 A のみ「過去の会員履歴が非公開」という限界を明示的に残している** |
| **Staff Notes** | **High** | ⚠️ **12 項目。🔴 「スペシャル・クラブ」「オーガニック」「イリットはムニエ 100%」「単数形のキュヴェ名」「未確認ヴィンテージ」「テイスティングノート」「別法人との混同」という 7 つの誤りを塞いだ** |
| 🔴 **総合** | 🔴 **High — staff-usable（70% を超過。実感としては 80% 前後）。** | **OBP 5 本すべてについて、公式の正式名・実在するヴィンテージか否か・セパージュ・糖・熟成を言える。栽培は年次まで、認証は公的登録の実態まで言える。**<br>**欠けているのは ① テイスティングノート、② 面積、③ 資格記号、④ 3 ヴィンテージの裏づけ。**<br>**いずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。** |

**reached_70: YES（~80%）.**

---

## Open Questions

1. 🔴 **OBP 3 行（`Les Terres d'Illite 2020`、`Les Fortes Terres 2019` / `2020`）が公式で裏づけられていない。**
   **公式サイトはキュヴェごとに現行リリース 1 年しか掲示せず、ヴィンテージ一覧を持たない。**
   **「存在しない」ではなく「公式が沈黙している」。**
   → **① 実ボトルのラベル、② 生産者への直接照会（`info@champagnemousse.fr`）のいずれかが要る。**
2. 🔴 **【物理ラベル確認タスク】資格記号（RM / NM / RC / CM）と matriculation 番号。**
   **公式サイトに `récoltant` / `manipulant` / `matricul…` の出現が 0 件。**
   🔴 **資格記号はシャンパーニュのラベルに法的に必須の印字なので、実ボトルの表／裏ラベルで必ず読める。**
   → **RM であれば「栽培から醸造まで自家」という語り方が公的に裏づけられる。現状は言えない。**
3. 🔴 **【物理ラベル確認タスク】`Spécial Club` の表示があるか。**
   🔴 **本調査で最も重要な物理確認。**
   **メニューは 3 行を `SPÉCIAL CLUB` 節に置き、canonical はキュヴェ名に `Special Club` を含むが、
   公式サイトにも Club の現行会員名簿にも根拠が無い。**
   → **`Spécial Club` は専用のボトル形状と、ラベルへの `Spécial Club` 表記が定められている。
   実ボトルを見れば一目で決着する。**
   → **決着するまで staff は `Spécial Club` として売らない。** → §Staff Notes ⚠️ ①
4. 🔴 **畑の面積（ha）が公式に無い。**
   ⚠️ **非公式ソースには数字が出るが、方針により採用していない。**
   → **生産者への直接照会、または CIVC / INAO の公開資料でしか埋まらない。**
5. 🔴 **`P-2` の解決方法 —— 統合か、親子明示か。**
   **公式確認は本書で供給した（単一法人）。だが canonical 上で
   `Champagne Moussé Fils` を単一 producer にまとめるのか、
   `Famille Moussé` を別名として保持するのかは設計判断である。**
   → 🔒 **`P-2` の「自動統合は禁止」は本書では解除していない。昇格可否は Akio / CTO 判断。**
6. 🔴 **`Special Club` をキュヴェ名の文字列に持つべきか、属性として持つべきか。**
   **`Grand Cru` / `HVE` と同種の「生産者横断の団体・格付指定」であり、
   名前に溶かし込むと照合が壊れる（実際に本件で壊れている）。**
   → 🔒 **設計判断。本書では決めていない。** → §Canonical Conflict 形状 A
7. 🔴 **canonical の `grapes` / `dosage` が公式と食い違う件を、どこまで遡って点検すべきか。**
   **本件では 3 レコード中 3 件すべてで `dosage` が、2 件で `grapes` が公式と違った。**
   **既知の罠は「散文が信用できない」だったが、本件は構造化フィールドの問題である。**
   → **他生産者の `grapes` / `dosage` も同様に未検証である可能性が高い。**
8. ⚠️ **公式にテイスティングノートが存在しない。**
   **色・香り・味わいを語る公的な根拠が無い。**
   → **蔵の資料、または実際の試飲でしか埋まらない。**
9. ⚠️ **`Demeter` / `Biodyvin` / `HVE` の登録の有無が未確認。**
   **Agence Bio の有機 engagement は確認できたが、他の認証機関の登録は照会していない。**
10. ⚠️ **`/dans-le-monde/` の輸入元・取扱店一覧が JS 埋め込みで読めなかった。**
    **米国輸入元が判明すれば、輸入元のテクニカルシートから
    アルコール度数・デゴルジュマン日・生産本数が得られる可能性がある。**
    ⚠️ **ただし輸入元資料は「生産者著作であること」が示せる場合のみ採用可。**
11. ⚠️ **Cuisles の échelle des crus 上の格付が未確認。**
12. ⚠️ **`SARL FAMILLE MOUSSE` の登記 commune が `Châtillon-sur-Marne` と `Cuisles` で揺れている**
    （INSEE は前者、Agence Bio は同一住所を両方で登録）。**実害は無いが記録する。**
