# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical にこの生産者のレコードは 16 件存在する**（すべて `Cristal` 系。`Collection` は 0 件）。
> 本書は昇格前の研究記録であり、**canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト louis-roederer.com ／ 公式フィッシュ・テクニック PDF で確認**（一次資料）
> `🏛` **公的登録（recherche-entreprises.api.gouv.fr ／ Agence Bio ／ Ecocert ／ Demeter France）**
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出（読み取りのみ）
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://www.louis-roederer.com/`（FR 原本。EN は裏取りのみ）**
> 併用: ✅ **公式テクニカルシート PDF 14 点**（`/sites/default/files/pdf/`。Cristal 2013–2016 /
> Cristal Rosé 2012–2015 / Collection 241–246）
> 併用: 🏛 **フランス企業登録・Agence Bio・Ecocert・Demeter France**
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ①（タスク前提への push back）——
> `Cristal` の「色の軸」は canonical に既に存在する。壊れているのは matcher の側だけである。**
> **canonical は `Cristal Brut`（`color='Blanc'`）と `Cristal Rosé Brut`（`color='Rosé'`）を
> 別キュヴェとして持ち、`cristal-rose-2014` は OBP 4 行目の正しい着地点として実在する。**
> **すなわち本件は Taittinger の `C-6`（=「識別に必要な軸が canonical に無い」）**の同型ではない。**
> **むしろ `C-6` の対偶事例であり、`C-6` の推奨のうち「色を cuvée の識別属性にする」側は
> Roederer では既に満たされている。残っているのは
> **「メニューのセクション見出しを matcher の入力信号にする」側だけ**である。
> → §Canonical Conflict `C-6`（証拠追加）／ 直接の族は **`C-4`**
>
> 🔴 **本ドシエ最大の収穫 ②（タスク前提への push back）——
> Roederer の認証は「ビオディナミ認証」ではなく「有機（agriculture biologique）認証」である。**
> **公式の数字は「シャンパーニュで最も広い有機栽培の畑、135 ヘクタール認証済み」。**
> **🏛 Agence Bio の認証機関は `Ecocert France`（`FR-BIO-01`）、
> 認証枠組みは `Agriculture biologique Europe (EU) 2018/848`、engagement `2018-03-12`。**
> **🏛 Demeter France のサイト内検索「roederer」は 0 件。Biodyvin にも該当なし。**
> **公式がビオディナミについて語るのは「原理（principes）」「ビオディナミ堆肥（composts biodynamiques）」まで、
> すなわち "実践" であって "認証" ではない。**
> → 🔴 **canonical の `house_style` は「since 2012 all Cristal vintages produced from
> **Demeter-certified** biodynamically farmed fruit」と書いており、これは公的登録に反する。**
> → §Canonical Conflict【B】
>
> 🔴 **本ドシエ最大の収穫 ③ —— `Collection 246` の `246` は「ベース年の符号化」ではない。
> Roederer 家の「246 回目の収穫／246 番目のアッサンブラージュ」という序数である。
> ベース年（2021）は別の値として存在し、しかも 55% という比率つきである。**
> → §Canonical Conflict `V-1`（証拠追加）
>
> 🔴 **本ドシエ最大の収穫 ④ —— Cristal Rosé の色づけは `saignée` ではない。
> 公式の呼称は「`infusion` ／ `infusion douce`（ゆるやかな infusion）」であり、
> 公式テクニカルシートは「シャルドネの果汁の一部をピノ・ノワールのマセラシオンに流し込み、
> 一緒に発酵させる」と書いている。赤ワインの添加ではない。**
> **canonical の `house_style` は「rosé colored via saignée method with red wine」と書いており、誤り。**
> → §Winemaking ／ §Staff Notes ⚠️ ④
>
> ⚠️ **調査上の制約 3 点**
> **① サイト全体が年齢確認ゲート（Drupal、`/{lang}/prehome/enter`）の背後にある。**
>    **これは CAPTCHA / bot チャレンジではなく、酒類サイトの年齢自己申告ゲートである。
>    サイト自身が公開している導線を通っただけで、迂回・突破は行っていない。**
> **② `/sitemap.xml` は `lastmod 2014-01-21` で腐っており、`<loc>` は
>    ステージング用ドメイン `roederer-site.pp.mzrn.net` を指している（148 URL）。**
>    **本番の URL 構造はここからは取れない。フッターのナビゲーションから読み取った。**
>    **⚠️ このステージング URL は本番の一次資料ではない。事実の根拠に一切使っていない。**
> **③ `lr_tech_sheet_collection_245_fr.pdf` はフォント埋め込みが壊れており、
>    テキスト抽出が文字化けする（cid 写像の欠落）。245 のセパージュとドザージュは本書では確定していない。**

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Louis Roederer** |
| **公式表記** | ✅ **Champagne Louis Roederer** ／ **Maison Louis Roederer**（公式サイト上で併用） |
| 🔴 **法人** | ✅ **Champagne Louis Roederer (CLR)**。**Société anonyme au capital de 3 672 000 €**<br>**N.M. 291-001**（シャンパーニュのマーク番号）／**RCS Reims B 335 681 169 00017**<br>🏛 **`recherche-entreprises.api.gouv.fr` で一致確認: SIREN `335681169` / SIRET `33568116900017` / NAF `11.02A`** |
| **本社所在** | ✅ **CS 40014 – 21 boulevard Lundy – 51722 REIMS Cedex – France**<br>🏛 **登録上の siège も `21 BOULEVARD LUNDY 51100 REIMS`。一致。** |
| **連絡先（公式表示）** | ✅ Tél. `+33 (0)3 26 40 42 11` ／ `com@champagne-roederer.com` |
| **AGEC 法の一意識別子** | ✅ 🏛 **`FR246127_01QEKR`**（ADEME 登録。Comité Champagne 経由）<br>⚠️ **同じ行に併記される SIRET `78038582900012` は Comité Champagne 側のもので、Roederer のものではない。読み違えに注意。** |
| 🔴 **社長** | ✅ **Frédéric Rouzaud（Président Directeur Général）。一族の第 7 世代。** |
| 🔴 **醸造長・畑統括** | ✅ **Jean-Baptiste Lécaillon（Chef de Caves et du vignoble）。1999 年より。** |
| **畑の管理責任者** | ✅ **Johann Merle（Régisseur des Vignobles）**（2016 年の公式インタビュー時点） |
| 🔴 **創業** | ✅ **1776 年、ランス。**「**Fondée à Reims en 1776**」（250 周年ページ）。**2026 年が創業 250 年。**<br>🏛 ⚠️ **企業登録上の `date_creation` は `1956-01-01`。これは法人登記の日付であって、家の起点ではない。**<br>🔍 **canonical の `founded_year = 1776` は公式と一致する（Taittinger の `P-8` のような矛盾は無い）。** |
| **家族性・独立性** | ✅ 「**l'une des très rares grandes maisons de Champagne demeurées familiales et indépendantes**」 |
| **年間出荷** | ✅ **約 300 万本**（「trois millions de bouteilles à travers le monde」） |
| **認証（🏛 で裏を取ったもの）** | 🏛 **Ecocert France `FR-BIO-01` / `Agriculture biologique Europe (EU) 2018/848` / 状態 `ENGAGEE` / engagement `2018-03-12`**<br>🏛 **Agence Bio 番号 `133856`。`mixité: Oui`（＝有機と非有機が併存する経営体）**<br>✅ **HVE（Haute Valeur Environnementale）＋ Comité Champagne の持続可能栽培（VDC）、2014 年から取得手続き、2016 年 7 月に更新監査** |
| 🔴 **認証されて「いない」もの** | 🏛 ⚠️ **Demeter 認証は確認できない。**`demeter.fr` のサイト内検索「roederer」は **0 件**。<br>⚠️ **Biodyvin の記載も無い。** → §Farming / §Staff Notes ⚠️ ③ |
| **canonical id** | 🔍 **16 件、すべて `Cristal` 系**（下表）。**`Collection` / `Brut Premier` / `Vintage` / `Blanc de Blancs` / `Brut Nature` / `Hommage à Camille` は 1 件も無い。** |

---

## Overview

✅ **ランス、21 boulevard Lundy。1776 年創業、第 7 世代の Frédéric Rouzaud が率いる、
シャンパーニュでは稀な「完全に家族所有かつ独立」のグランド・メゾン。2026 年が創業 250 年。**

🔴 ✅ **このメゾンの構造的な特異点は「畑を持っていること」そのものである。**
公式の自己記述は明快で、19 世紀に「他が葡萄を買っていたとき、Louis Roederer は畑を慈しんだ」と書く。
「**1845 年、Louis Roederer はグラン・クリュ Verzenay に 15 ヘクタールを買うことを決める。
葡萄にほとんど価値が無かった時代に、自らのミレジムの醸造をよりよく制御するために vigneron になるという、
奇妙な発想だった。**」

🔴 ✅ **その帰結が、公式が自ら「シャンパーニュでは唯一（unique en Champagne）」と呼ぶ状態である。**
「**それ以来、Louis Roederer のミレジム（vintage 表示のワイン）はすべて、
例外なく自社の畑から生まれている。これはシャンパーニュにおいて唯一の例である。**」
→ 🔴 **重要な限定に注意。「すべてのワイン」ではなく「すべての millésime（ミレジム表示のワイン）」である。**
**非ミレジムの `Collection` は、自社畑に加えて協働栽培者の「Cœur de Terroir」区画の葡萄を使う。**
→ §Staff Notes ⚠️ ①

✅ **畑の規模は 250 ヘクタール、420 を超える区画。**
（`/fr/house`: 「**En 2024, la surface du vignoble Louis Roederer s'étend sur 250 ha composés de 420 parcelles**」）

🔴 ✅ **そして本ドシエの中心的な発見のひとつ ——
「Depuis plus de vingt ans, sous la houlette de son Chef de Caves Jean-Baptiste Lécaillon,
Louis Roederer déploie une viticulture attentive, précise et en constante évolution,
jusqu'à devenir **le plus vaste vignoble de Champagne en agriculture biologique
avec 135 hectares certifiés**.」**
→ 🔴 **公式の主張は「有機（agriculture biologique）で 135 ha 認証済み、シャンパーニュ最大」である。
「ビオディナミ認証」ではない。** → §Farming

🔍 **THÉSEUS における状態は、Taittinger と正反対の形をしている。
canonical は `Cristal` 系を 16 件持ち、白・ロゼ・Vinothèque・Vinothèque Rosé の 4 キュヴェを
きちんと分けて登録している。にもかかわらず OBP 4 行のうち 3 行が `candidate` 止まりであり、
残る 1 行（`Collection 246`）は canonical にキュヴェ自体が無いため `unresolved` である。**

---

## History

✅ **公式の沿革は `/fr/house`（La Maison）と `/fr/250ans`（250 周年ページ）の 2 か所にあり、
両者は互いに整合している。**

| 年 | 出来事 ✅ |
|---|---|
| 🔴 **1776** | 🔴 **ランスでメゾン創業。**「**Fondée à Reims en 1776**」。**2026 年が 250 周年。** |
| 🔴 **1833** | 🔴 **Louis Roederer がメゾンを相続し、自らの名を与える。**「**Un tournant décisif intervient en 1833, lorsque Louis Roederer hérite de la Maison et lui donne son nom.**」 |
| 🔴 **1845** | 🔴 **Verzenay グラン・クリュに 15 ha を購入。自社畑戦略の起点。** |
| **19 世紀後半** | **国際展開、とくにロシア。1870 年代には米国とロシア皇帝の食卓へ** |
| 🔴 **1876** | 🔴 **Louis Roederer II が皇帝アレクサンドル 2 世のために `Cristal` を創出。**<br>✅ 「**première cuvée de prestige de l'histoire du Champagne**」（シャンパーニュ史上最初のプレステージ・キュヴェ）。**2026 年が Cristal 150 年。** |
| **1920 年代** | **Léon Olry Roederer が、複数ミレジムの恒常的なアッサンブラージュという発想を打ち出す。**「**Il dessine ainsi les contours du futur Brut Premier**」（＝のちの `Brut Premier` の輪郭） |
| **1933–** | **Léon の死後、妻 Camille Olry-Roederer がメゾンを率いる。**✅ **在任 43 年。**「**la force et la vision ont permis de préserver l'indépendance de la Maison dans la période la plus délicate de son histoire**」 |
| **20 世紀後半** | **Jean-Claude Rouzaud（œnologue・ingénieur agronome、Camille の孫）が畑の remembrement（再編）を進める** |
| 🔴 **1974** | 🔴 **Jean-Claude Rouzaud が `Cristal Rosé` を創出。**「**Il repéra et sélectionna des parcelles iconiques de pinot noir à Aÿ et de chardonnay sur Avize et Le Mesnil-sur-Oger, créant ainsi le premier assemblage de Cristal Rosé à partir de la vendange 1974.**」<br>**同時に「infusion」と名づけられた手法を導入。**（**50 周年は 2024 年**として公式が記念） |
| 🔴 **1998** | 🔴 **Aÿ の斜面のより高所にある遅熟の区画 `La Villers` を、数年の jachère（休閑）を経て、
sélection massale 由来の若木で植え替え。**「**C'est le début d'une redéfinition continue du parcellaire de Cristal Rosé.**」 |
| **1990 年代末** | ✅ **Rouzaud 家と Lécaillon の主導で栽培の見直しが始まる。「l'arrêt des intrants et la régénération des sols」（投入資材の停止と土壌の再生）** |
| 🔴 **1999** | 🔴 **Jean-Baptiste Lécaillon が Chef de Caves et du vignoble に就任（現職）** |
| 🔴 **2006** | 🔴 **「culture biologique régénérative」への転換を開始。**🔴 **起点は `Domaine Cristal Rosé` の区画。**「**la transition vers une culture biologique régénérative est engagée dès 2006, en commençant par les parcelles du Domaine Cristal Rosé**」 |
| **2008** | ✅ **Cristal Rosé にとって二重の転換点。「un changement de nature de l'infusion et de paradigme」** |
| **2014** | ✅ **Comité Champagne（CIVC）基準と HVE の持続可能栽培認証の取得手続きに着手** |
| 🔴 **2018-03-12** | 🏛 🔴 **Agence Bio における有機認証の engagement 日（認証機関 Ecocert France）** |
| **2016 年 7 月** | ✅ **環境認証の更新監査**（Johann Merle 談） |
| 🔴 **2021 頃** | 🔴 **`Brut Premier` に代わる新しい多年アッサンブラージュ `Collection` を開始**（`Collection 241` = 2016 収穫がベース） |
| **2024** | ✅ **`Cristal Rosé` 創出 50 周年** ／ ✅ **畑 250 ha・420 区画の公式数値の基準年** |
| **2026** | ✅ **メゾン 250 周年 ＋ Cristal 150 周年 ＋ Fondation Louis Roederer 15 周年** |

⚠️ 🔴 **Cristal の lieux-dits の形成開始年が公式内で食い違っている。**
- `/fr/cristal2015`: 「**des lieux-dits patiemment constitués depuis 1845**」
- `/fr/cristal2016`（同一ページ内の英文段落）: 「**carefully and patiently built up by successive generations
  at the helm of the Louis Roederer Champagne House since 1841**」
→ **1845 と 1841 で 4 年ずれる。どちらが正しいかは公式からは決められない。** → §Staff Notes ⚠️ ⑦

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| **本拠** | ✅ **Reims、`21 boulevard Lundy`**（🏛 企業登録と一致） |
| 🔴 **畑の規模** | ✅ **250 ヘクタール、420 を超える区画**（2024 年時点） |
| ⚠️ 🔴 **畑の格付け表記** | ⚠️ **公式内で食い違っている。**<br>`/fr/house`: 「**250 hectares situés exclusivement dans les Grands et Premiers Crus de la Marne**」（**exclusivement**）<br>`/fr/250ans`: 「**la propriété couvre 250 hectares situés sur les meilleurs terroirs de Champagne, essentiellement en Premiers et Grands Crus**」（**essentiellement**）<br>→ 🔴 **「排他的に」と「主として」は同じことを言っていない。** → §Staff Notes ⚠️ ⑥ |
| **畑の広がり** | ✅ **Montagne de Reims ／ Vallée de la Marne ／ Côte des Blancs の 3 地区** |
| **品種** | ✅ **Chardonnay / Pinot noir / Pinot Meunier の 3 品種が自社畑に共存** |
| 🔴 **社内の畑区分** | 🔴 ✅ **テクニカルシートが一貫して使う 3 区分 —— 「**la Rivière**」「**la Montagne**」「**la Côte**」**<br>**`Collection` は 1/3 ずつ、`Cristal` も 1/3 ずつ、`Cristal Rosé` は 1/2 Rivière ＋ 1/2 Côte（Montagne を含まない）** |

### 🔴 ✅ キュヴェ別の産地構成（**公式テクニカルシート PDF より。canonical には無い情報**）

| キュヴェ | 社内区分 | 主要クリュ（`CRUS PRINCIPAUX`） |
|---|---|---|
| 🔴 **Cristal**（白） | **1/3 la Rivière ／ 1/3 la Montagne ／ 1/3 la Côte** | 🔴 **Verzenay, Verzy, Beaumont-sur-Vesle, Aÿ, Avize, Mesnil-sur-Oger, Cramant（7 クリュ）** |
| 🔴 **Cristal Rosé** | 🔴 **1/2 la Rivière ／ 1/2 la Côte（Montagne は入らない）** | 🔴 **Aÿ, Avize, Mesnil-sur-Oger（3 クリュのみ）** |
| **Collection** | **1/3 ／ 1/3 ／ 1/3** | ✅ **自社畑に加え、協働栽培者の「Cœur de Terroir」選抜区画の葡萄で補う** |

🔴 ✅ **`Cristal` の畑は「Domaine Cristal」と呼ばれる独立した区画群である。**
「**Cristal est un champagne de terroir et d'artisan, issu exclusivement du domaine éponyme
cultivé en agriculture biologique.**」（`/fr/cristal2016`）
→ 🔴 **「同名のドメーヌから排他的に、有機栽培で」。**

### 🔴 ✅ Cristal の区画数（**年によって変わる。固定値ではない**）

| 出典 | 数字 |
|---|---|
| ✅ `/fr/cristal2015` | 🔴 「**Pour la première fois depuis 2002, ce millésime 2015 est issu de l'ensemble des
**45 parcelles de plus de vingt ans d'âge**, éligibles ainsi à entrer dans l'assemblage Cristal.**」<br>→ **Cristal に入る資格を持つ区画は「樹齢 20 年超の 45 区画」。2015 はその全部を使った。** |
| ✅ **`ft_cristal_2016_fr.pdf`** | 🔴 **`32 PARCELLES`** |
| ✅ **`lr_tech_sheet_cristal_blanc_2015_fr.pdf` / `..._2014_fr.pdf`** | ⚠️ **区画数の記載が無い** |

→ 🔴 ⚠️ **したがって「Cristal は 45 区画から造られる」と固定的に言ってはならない。
45 は「資格のある区画の総数」であり、実際に使う数は年ごとに違う（2016 は 32）。**
→ §Staff Notes ⚠️ ② ／ §Canonical Conflict【B】

❓ **公式に無い**: クリュごとのヘクタール数、区画名の一覧、協働栽培者の名前、
`Collection` の「Cœur de Terroir」区画の所在。

---

## Farming

🔴 **本節は本ドシエで最も慎重に書かれた節である。タスク側の前提（「認証ビオディナミ」）は
公式および公的登録の双方によって否定された。**

### 🔴 ✅ 公式が主張していること —— **有機（agriculture biologique）で 135 ha 認証済み**

✅ **`/fr/250ans` の一文（verbatim）:**
「**Depuis plus de vingt ans, sous la houlette de son Chef de Caves Jean-Baptiste Lécaillon,
Louis Roederer déploie une viticulture attentive, précise et en constante évolution,
jusqu'à devenir le plus vaste vignoble de Champagne en agriculture biologique
avec 135 hectares certifiés.**」

→ 🔴 **250 ha のうち 135 ha が有機認証。すなわち約 54%。残りは認証されていない。**
→ 🏛 **Agence Bio の `mixité: Oui`（有機と非有機の併存）がこれと完全に整合する。**

### 🏛 認証の裏取り（**公的登録での照合**）

| 照合先 | 結果 |
|---|---|
| 🏛 **Agence Bio（`opendata.agencebio.org`）** | ✅ **`CHAMPAGNE LOUIS ROEDERER` / SIRET `33568116900017` / numéro bio `133856` の 1 件がヒット。**<br>**認証機関: `Ecocert France`（`FR-BIO-01`）／ 状態 `ENGAGEE` ／ `dateEngagement` `2018-03-12` ／ `datePremierEngagement` `2018-03-12`**<br>**`productions`: `Raisin de cuve`（状態 `AB` / `C1` / `C2` / `C3` / `CS` / `EAC`、基準年 2026）、`Vins de raisin`（`AB` / `EAC`）ほか**<br>🔴 **`C1`〜`C3`（転換期 1〜3 年目）が同時に立っている ＝ 現在も転換中の区画がある。**<br>**活動地: `21 boulevard Lundy, Reims`（本社・活動地）＋ `15 Rue Henry Henrion, 51160 AY`（活動地）** |
| 🏛 **Ecocert 証明書ページ** | ✅ **`CHAMPAGNE LOUIS ROEDERER`、`21 boulevard Lundy, CS 40014, 51722 REIMS`。**<br>**認証名は「`Certification Agriculture biologique Europe (EU) 2018/848`」の 1 件のみ。**<br>**活動: `Agriculteur (production végétale)` / `Fabricant & Transformateur` / `Grossiste spécialisé`。**<br>🔴 **ビオディナミの認証は一切掲載されていない。** |
| 🏛 **Demeter France** | 🔴 ⚠️ **`demeter.fr` のサイト内検索「roederer」→「Il semblerait qu'il n'y ait pas de résultats pour cette recherche」（0 件）。**<br>**`/adherents/champagne-louis-roederer/` は HTTP 404。** |
| 🏛 **Biodyvin** | ⚠️ **該当なし（検索で発見できず）。** |

### 🔴 ⚠️ ビオディナミについて公式が実際に書いていること —— **「実践」であって「認証」ではない**

| 出典 | 記述（verbatim） | 読み |
|---|---|---|
| ✅ `/fr/house`・`/fr/homepage` | 「**Ce travail de précision s'effectue dans le respect de la biodiversité et accorde une place grandissante aux principes de la biodynamie.**」 | **「ビオディナミの原理に、増しつつある場所を与えている」。認証の主張ではない。** |
| ✅ `/en/house`（英語版） | 「**with great respect for biodiversity and, increasingly, the principles of biodynamic cultivation**」 | **⚠️ FR と EN で数字・主張の食い違いは無い。** |
| ✅ `/fr/cristal2015` | 「**des pratiques vertueuses comme la sélection massale, la taille douce, des jachères longues, des composts biodynamiques et des méthodes inspirées du modèle de la permaculture**」 | 🔴 **「ビオディナミ堆肥」という具体的な実務。これは実践の記述である。** |
| ✅ `/fr/cristal-rose-50` | 「**la transition vers une culture biologique régénérative est engagée dès 2006, en commençant par les parcelles du Domaine Cristal Rosé**」 | 🔴 **転換の語は `biologique régénérative`（再生型有機）。`biodynamique` ではない。** |

→ 🔴 **結論: `practised`（ビオディナミ的実務あり） vs `certified`（有機のみ、Ecocert）。
Bergström（Batch 9）と同じ区別が、ここでは逆向きに効いている ——
プロンプトが「認証ビオディナミ」と述べていた点は、公式・公的登録の双方で支持されない。**

### ✅ 具体的な栽培実務（公式が名指しするもの）

- 🔴 **`sélection massale`（マサル・セレクション）** — 「**une sélection de pieds de vignes aux potentiels
  génétiques variés parmi une population diversifiée, dont on prélèvera un sarment, le "greffon",
  pour le greffer sur un porte-greffe**」。**20 年以上にわたる植物遺産保存プログラム。**
  🔴 「**Dans trente ans, l'ensemble du vignoble Louis Roederer sera ainsi planté d'individus
  entièrement sélectionnés par nos soins, issus de notre propre pépinière. Un cas unique en Champagne.**」
- ✅ **台木（porte-greffes）を自社ドメーヌで直接栽培**
- ✅ **`taille douce`（樹液の流れを尊重する剪定）**
- ✅ **`jachères longues`（長期の休閑）／ jachère の輪作**
- ✅ **生垣（haies）と石垣（murets）の維持、蜜蜂の巣箱の設置、果樹の存在、果樹園の再生**
- ✅ **パーマカルチャーの発想に着想を得た手法**
- ✅ **手摘み収穫。区画ごとの分別醸造（vinification parcellaire）。収穫地でそのまま圧搾**
- ✅ **1990 年代末からの「l'arrêt des intrants et la régénération des sols」（投入資材の停止と土壌再生）**
- ✅ **HVE（農業省）と Comité Champagne 基準の持続可能栽培 —— 2014 年から着手、2016 年 7 月に更新監査で確認**
- ✅ **列の長さ、草生面積、景観整備を「set ratios」に合わせて計測**（Johann Merle 談）

✅ **畑責任者の言葉（2016 年、Johann Merle）** —
「**生垣はとりわけ重要です。見渡す限り葡萄しか無ければ、鳥は止まる場所も巣を作る場所もありません。
ところが鳥は昆虫の捕食者です。鳥がいなければ昆虫は増え、広がります。**」

✅ **醸造長の言葉（`/fr/expression-of-biodiversity`）** —
「**21 世紀において、戦いは自然のそれである。大地への敬意がこれほど切実であったことはない。
葡萄樹によりいっそうの回復力を与え、最大限の多様性を再創造し、
異なる感受性で生態系を豊かにし、自分たち自身の道を描くことである。**」—— Jean-Baptiste Lécaillon

---

## Winemaking

### 🔴 Cristal（白）—— **公式テクニカルシート PDF より** ✅

| 項目 | 2016 | 2015 | 2014 | 2013 |
|---|---|---|---|---|
| **セパージュ** | 🔴 **Pinot noir 58% / Chardonnay 42%** | **Pinot noir 60% / Chardonnay 40%** | **Pinot noir 60% / Chardonnay 40%** | （fiche あり・未転記） |
| 🔴 **木樽仕込み（`VINS SOUS BOIS`）** | 🔴 **31%** | **25%** | **32%** | — |
| 🔴 **マロラクティック発酵** | 🔴 **0%** | 🔴 **0%** | 🔴 **0%** | — |
| 🔴 **ドザージュ** | **7 g/L** | **7 g/L** | **7 g/L** | — |
| **区画数** | 🔴 **32 PARCELLES** | ⚠️ **記載なし**（landing は「45 区画すべて」） | ⚠️ **記載なし** | — |
| **収穫期間** | **2016-09-15 〜 10-01** | **2015-09-07 〜 09-20** | **2014-09-11 〜 09-21** | — |
| **社内区分** | （記載なし） | **1/3 ／ 1/3 ／ 1/3** | **1/3 ／ 1/3 ／ 1/3** | — |

✅ **熟成（製品ページ、全ミレジム共通の記述）** —
「**Elaboré uniquement lors des « grandes années », quand la maturité du Chardonnay (environ 40%)
et du Pinot noir (environ 60%) qui le composent est parfaite,
Cristal vieillit 6 années en cave et se repose 8 mois après dégorgement.**」
→ 🔴 **蔵で 6 年、デゴルジュマン後さらに 8 か月。**（🔍 canonical の `aging = '6 years on lees'` と整合）

✅ **熟成能力（公式）** —「**Cristal est un vin de garde. Il peut être conservé plus de vingt ans
sans perdre sa fraîcheur et son caractère.**」

### 🔴 Cristal Rosé —— **`infusion` / `infusion douce`。`saignée` ではない** ✅

🔴 ✅ **公式テクニカルシート `lr_tech_sheet_cristal_rose_2013_fr.pdf` の `Vinification` 欄（verbatim）:**
> **「Vinification : longue et douce «infusion», technique propre à la Maison.
> Quelques jus de Chardonnays sont coulés dans une macération de Pinots noirs,
> pour fermenter ensemble et s'intégrer parfaitement.」**

（訳: **「長く、ゆるやかな『infusion』。メゾン固有の技法。
シャルドネの果汁の幾ばくかを、ピノ・ノワールのマセラシオンのなかへ流し込み、
一緒に発酵させて完全に統合させる。」**）

🔴 ✅ **`/fr/wine/cristal-rose` の解説（verbatim、要点）:**
> 「**L'expression des arômes de Cristal Rosé était déjà magnifiée à travers la technique de
> l'infusion, mise en place dès les origines de la cuvée, mais il fallait aller plus loin,
> en distinguant avec encore plus de précision les deux phases d'infusion et de fermentation.
> Jean-Baptiste Lécaillon […] va faire progresser la technique, s'inspirant notamment du travail
> des grands Maîtres de thé japonais, qui maîtrisent l'art de la préparation et de l'infusion
> des feuilles de thé afin d'extraire des jus encore plus frais, précis et brillants.
> Depuis près de 25 ans, ce travail en perpétuelle réflexion se poursuit pour toujours garantir
> une plus grande pureté de l'infusion.**」

🔴 ✅ **`/fr/250ans`:**「**il s'appuie sur un savoir-faire pionnier, l'infusion douce,
qui lui confère son style singulier : une texture poudrée, une intensité soyeuse,
une fraîcheur saline et une finesse presque tactile.**」

→ 🔴 **公式サイト・公式テクニカルシートのいずれにも `saignée` の語は現れない。
また「赤ワインを加える」という記述も無い。行われているのは
「ピノ・ノワールのマセラシオンにシャルドネ果汁を注ぎ、共発酵させる」ことである。**
→ §Canonical Conflict【B】／ §Staff Notes ⚠️ ④

### 🔴 Cristal Rosé —— 公式テクニカルシートの数値 ✅

| 項目 | 2015 | 2014 | 2013 | 2012 |
|---|---|---|---|---|
| **セパージュ** | **Pinot noir 56% / Chardonnay 44%** | 🔴 **Pinot noir 55% / Chardonnay 45%** | （比率の記載を確認せず） | （fiche あり・未転記） |
| **木樽仕込み** | **15%** | 🔴 **19%** | **20%** | — |
| 🔴 **マロラクティック発酵** | 🔴 **0%** | 🔴 **0%** | 🔴 **0%** | — |
| 🔴 **ドザージュ** | **7 g/L** | 🔴 **8 g/L** | **7 g/L** | — |
| **主要クリュ** | **Aÿ, Avize, Mesnil-sur-Oger** | **Aÿ, Avize, Mesnil-sur-Oger** | **Aÿ, Avize, Mesnil-sur-Oger** | — |
| **社内区分** | **1/2 Rivière ／ 1/2 Côte** | **1/2 Rivière ／ 1/2 Côte** | **50% Rivière ／ 50% Côte** | — |
| **収穫期間** | **2015-09-07 〜 09-20** | **2014-09-11 〜 09-21** | — | — |

### 🔴 Collection 246 —— 公式テクニカルシート `lr_ft_collection_246_fr.pdf` ✅

| 項目 | 記述 |
|---|---|
| 🔴 **ベース収穫年** | 🔴 **2021**。「**Cette 246ème vendange chez Louis Roederer…**」／「**Les vendanges se sont déroulées du 13 au 30 septembre 2021.**」 |
| **産地** | **1/3 la Rivière ／ 1/3 la Montagne ／ 1/3 la Côte。**✅ **「Les raisins de nos domaines sont complétés avec des raisins provenant de parcelles sélectionnées "Cœur de Terroir" auprès de vignerons partenaires.」** |
| 🔴 **セパージュ** | 🔴 **Chardonnay 54% / Pinot noir 35% / Meunier 11%**（**シャルドネ比率が異例に高い年**） |
| 🔴 **246ème ASSEMBLAGE の内訳** | 🔴 **RÉSERVE PERPÉTUELLE 35%（2012–2020 の 9 年）**<br>🔴 **VINS DE RÉSERVE ÉLEVÉS SOUS BOIS 10%（2012–2017）**<br>🔴 **VINS SOUS BOIS 24%**<br>🔴 **VENDANGE 2021 55%** |
| 🔴 **マロラクティック発酵** | 🔴 **30%**（→ **Cristal の 0% と対照的。混同しないこと**） |
| **ドザージュ** | **7 g/L** |
| **熟成** | ✅ **「Élevé près de 4 ans dans nos caves」（蔵で約 4 年）** |
| **樽** | ✅ **「foudres de chêne français」（フランス産オークの大樽）。**🔴 **「des jeunes parcelles du domaine Cristal」由来のリザーヴワインも含む** |

### ✅ Collection 番号のシリーズ（**公式テクニカルシートで機械的に確定**）

| 番号 | ベース収穫年 | セパージュ | Réserve Perpétuelle | MLF | ドザージュ |
|---|---|---|---|---|---|
| **241** | **2016** | （記載形式が異なる） | — | — | — |
| **242** | **2017** | **Ch 42 / PN 36 / Me 22** | **34%（2012–2016）** | **34%** | **8 g/L** |
| **243** | **2018** | **Ch 42 / PN 40 / Me 18** | **31%（2012–2017）** | **26%** | **8 g/L** |
| **244** | **2019** | **Ch 41 / PN 33 / Me 26** | **36%（2012–2018）** | **35%** | **7 g/L** |
| **245** | **2020** | ⚠️ **PDF のフォント破損で抽出不能**（`35% Pinot noir` のみ読める） | **35%** | ⚠️ **抽出不能** | ⚠️ **抽出不能** |
| 🔴 **246** ⭐OBP | 🔴 **2021** | **Ch 54 / PN 35 / Me 11** | **35%（2012–2020）** | **30%** | **7 g/L** |

→ 🔴 **番号は連続する整数で、収穫年と 1 対 1 に対応する。`241 → 2016` から `246 → 2021`。**
**1776 年創業とすると `1776 + 245 = 2021` で整合する。**

⚠️ 🔴 **公式の「番号が何であるか」の言い方は 2 通りあり、どちらも同じページ群に出る:**
- ✅ **fiche `246`**: 「**Cette 246ème vendange chez Louis Roederer**」（**246 回目の収穫**）
- ✅ **`/fr/collection246`**: 「**Ce 246e assemblage de la Maison Louis Roederer**」（**246 番目のアッサンブラージュ**）
→ **どちらも「メゾンの歴史における序数」であって、「ベース年の符号」ではない。**
**ベース年 2021 は別に、しかも「55%」という比率つきで存在する。** → §Canonical Conflict `V-1`

⚠️ **公式は `Brut Premier` のページを残しているが、`Collection` を
「Brut Premier の後継」と明示する文は本調査では見つけられなかった。**
**公式が書くのは「創造の自由」「新しい章」という語だけである。** → Open Questions 3

---

## Style

### ✅ 公式テイスティングノート（**OBP 関連分。すべて公式 fiche / 製品ページ**）

| キュヴェ / VT | 醸造長の一言 ✅（Jean-Baptiste Lécaillon） |
|---|---|
| 🔴 **Cristal 2016** ⭐OBP | 🔴 「**Cristal 2016 est tout simplement « phénoménal » ! Issu d'une année fraîche et tardive,
il révèle cet équilibre rare et magique entre intensité des parfums purs, vibration énergique,
bouche juteuse et finale saline et crayeuse. L'équilibre parfait d'un Cristal 50% sol / 50% soleil.**」 |
| 🔴 **Cristal 2015** ⭐OBP | 🔴 「**Cristal 2015 se présente avec un tempérament calcaire, plus « sol » que solaire…
ce qui est incroyable pour un millésime si solaire. Grand potentiel de garde !**」 |
| **Cristal 2014** | 「**Délicieux, salin et raffiné… définitivement Cristal.**」 |
| 🔴 **Cristal Rosé 2014** ⭐OBP | 🔴 「**Cristal Rosé 2014 au fruit mûr, élancé et à la texture délicieuse est d'une incroyable précision.
Un délice, presque électrique, de haute intensité de goût.**」 |
| **Cristal Rosé 2015** | 「**Cristal Rosé 2015 signe une sorte de contre-pied avec son année de naissance :
à l'opposé de la puissance et de la richesse d'un millésime chaud et sec,
il livre toute la délicatesse et la fraîcheur des grands sols blancs crayeux de son domaine.**」 |
| **Cristal Rosé 2013** | 「**Cristal rosé 2013 est une essence, une fragrance aux parfums délicats, denses et concentrés.
La perfection ?**」 |
| 🔴 **Collection（全番号共通）** ⭐OBP | 🔴 「**Chaque Collection est un « pas de côté », un nouveau chapitre dans l'univers du goût de la Maison.
À chaque fois singulier mais toujours résolument Roederer !**」 |

### ✅ Cristal 2016 の公式テイスティングノート（fiche、抜粋）

「**輝く明るい黄色。壮麗で、ゆるやかで、細かい泡立ち。白い花（アカシア）、凝縮して焼けた柑橘（レモン）、
熟した黄色い果実（桃、ミラベル）の香りが混ざり合う、強く、深く、精確な bouquet。
数分後、控えめにヨードを帯び、粉を帯び、焙煎された色調が、
« sur lattes » の熟成中の酵母自己消化を証している。口中の印象は「即時的」で、
やわらかく繊細、かつてないほど近づきやすい。［…］
Cristal 2016 は純粋で、繊細でありかつ凝縮している。それは偉大な Cristal の、完全で自明な姿である ——
50% は太陽（熟して果汁の乗った猛暑のピノ・ノワール）、50% は土（白亜的で塩気のあるシャルドネ）。
2002、2008、2012 に近いが、さらに引き伸ばされ、精確で、凝縮した姿を持つ。**」

### ✅ Cristal Rosé 2014 の公式テイスティングノート（fiche、抜粋）

「**わずかに銅色を帯びた反射のあるピンク。持続する cordon をつくる、動的な泡立ち。
純粋で、精確で、輝かしい bouquet。ピノ・ノワールの強い香りが、収穫を、純粋で熟し凝縮した果実を思わせる ——
森の赤い果実（すぐり、野いちご、カシス）と、酸を帯びたもの、フランボワーズのリキュール。
次いで甘い香辛料、燻した調子、ピノ・ノワールの還元の一点（燻香、香辛料）が下生えの調子とともに現れる。
口中は凝縮し、豊かで、赤い果実（いちご、ラズベリー）が引き締まった強い質感のなかに凝集する。
その年の両極を映して 2 段階で開く —— まず絹のように豊かなアタック（最終的な成熟）、
続いて引き締まった強いフレッシュさ（涼しい夏）。［…］
塩気とヨードの印象が燻香と酸に結びつき、umami と、限りなく美味な余韻を与える。**」

### ✅ Collection 246 の公式テイスティングノート（fiche、抜粋）

「**輝かしく明るい反射を持つシャンパーニュ色。極めて細かく規則的な泡立ち。
黄色い果実（ミラベル、ネクタリン）と砂糖漬けの柑橘（レモン）の bouquet に、
われわれのフランス産オークの大樽で醸造された 24% のワインに由来する木の調子（焼け、ヴァニラ）が加わる。［…］
Collection 246 は、精確で、優しく、同時に振動している。
finesse と élégance、白亜的な質と塩気をもたらすシャルドネの例外的な比率のおかげで、
渇きを癒す軽やかさを解き放つ。ある種のブラン・ド・ブランの性格を思わせなくもない。**」

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 4 本。0 本が `exact`、3 本が `candidate`、1 本が `unresolved`**）

| # | OBP 印字 | VT | 価格 | メニューのセクション | ✅ **公式での確認結果** |
|---|---|---|---|---|---|
| 1 | **'Collection 246,'** Brut | — | $250 | `… \| BLENDS` | ✅ 🔴 **`Collection 246` として実在。公式テクニカルシート `lr_ft_collection_246_fr.pdf` あり。**<br>🔴 **`246` は「Louis Roederer における 246 回目の収穫／246 番目のアッサンブラージュ」。ベース収穫年は 2021（アッサンブラージュの 55%）。**<br>**Ch 54 / PN 35 / Me 11、Réserve Perpétuelle 35%（2012–2020）、MLF 30%、ドザージュ 7 g/L、蔵で約 4 年。**<br>🔍 **canonical に `Collection` のレコードは 1 件も存在しない ＝ gap。** |
| 2 | **'Cristal,'** Brut | **2016** | $1,120 | `… \| BLENDS` | ✅ 🔴 **`Cristal 2016` として実在。現行リリース。**公式 fiche `ft_cristal_2016_fr.pdf`。<br>**PN 58 / Ch 42、32 区画、木樽 31%、MLF 0%、ドザージュ 7 g/L、収穫 2016-09-15〜10-01。**<br>🔍 🔴 **canonical に `cristal-2016` は存在しない ＝ vintage 層の gap。**（2015 / 2014 / 2013 / 2012 / 2006 / 2002 はある） |
| 3 | **'Cristal,'** Brut | **2015** | $1,200 | `… \| BLENDS` | ✅ 🔴 **`Cristal 2015` として実在。**公式 fiche `lr_tech_sheet_cristal_blanc_2015_fr.pdf`。<br>**PN 60 / Ch 40、木樽 25%、MLF 0%、ドザージュ 7 g/L、収穫 2015-09-07〜09-20。**<br>🔴 **「2002 年以来はじめて、樹齢 20 年超の 45 区画すべてから造られた」**（公式）。<br>🔍 ✅ **canonical `cristal-2015` の `grapes = ['Pinot Noir 60%','Chardonnay 40%']` と `dosage = '7 g/L'` は公式 fiche と完全一致。** |
| 4 | **'Cristal,'** Brut | **2014** | $1,985 | 🔴 `… \| **ROSÉ**` | ✅ 🔴 **メニューのセクションが `ROSÉ` である以上、これは `Cristal Rosé 2014`。**<br>**公式 fiche `lr_tech_sheet_cristal_rose_2014_fr.pdf`: PN 55 / Ch 45、木樽 19%、MLF 0%、ドザージュ 8 g/L、クリュは Aÿ / Avize / Mesnil-sur-Oger の 3 つのみ、収穫 2014-09-11〜09-21。**<br>⚠️ **`Cristal 2014`（白）も公式に実在する。両者は別物で、木樽比率もドザージュもクリュ構成も違う。**<br>🔍 🔴 **canonical `cristal-rose-2014` が実在し、`grapes = ['Pinot Noir 55%','Chardonnay 45%']` / `dosage = '8 g/L'` は公式 fiche と完全一致。**<br>🔴 **すなわち「正しい着地点はすでに canonical にある」。matcher が届いていないだけである。** |

🔴 **4 本すべてが、公式に実在するキュヴェ／ミレジムであることを確認した。**
🔴 **価格の順序も裏づけになる。ROSÉ セクションの 2014 が $1,985 で、BLENDS の 2015（$1,200）・2016（$1,120）より
はるかに高い。Cristal Rosé は Cristal（白）より高価な位置づけであり、これは色の読みと整合する。**
⚠️ **ただし価格は OBP 側のデータであって公式の裏づけではない。補強材料にとどめる。**

### 🔍 OBP intake の実データ（**読み取りのみ・無変更**）

| index | source_row_id | section | match_state | cuvee_state | evidence（要約） |
|---|---|---|---|---|---|
| **47** | `…6851d1f53e` | **BLENDS** | **unresolved** | **unresolved** | 🔴 「**'Louis Roederer' の canonical キュヴェ 4 件に一致無し: 'Collection 246'**」 |
| **48** | `…55508bbc99` | **BLENDS** | **candidate** | **candidate** | 🔴 「**ラベル 'Cristal' が canonical の 4 キュヴェに同程度に該当し一意に決まらない: Cristal Brut, Cristal Rosé Brut, Cristal Vinotheque, Cristal Vinotheque Rosé**」 |
| **49** | `…9969ee716e` | **BLENDS** | **candidate** | **candidate** | 同上 |
| **142** | `…4af758cbdd` | 🔴 **ROSÉ** | **candidate** | **candidate** | 同上。🔴 **evidence の文言は 47・48・49 と完全に同一 —— すなわち matcher は `ROSÉ` というセクション見出しを一切見ていない。** |

🔴 **これが本ドシエの構造的な核心である。**
**canonical は 4 キュヴェを正しく分けて持っている。intake の evidence 文字列自体が 4 件を列挙している。
にもかかわらず 4 行目が解決しないのは、`'Cristal,' Brut` という印字文字列に
白／ロゼ／Vinothèque を選ぶ語が一つも無く（→ `C-4`）、
かつ唯一それを決められる情報（セクション見出し `ROSÉ`）を matcher が入力に取っていないためである。**

### ✅ 公式の全キュヴェ（`/fr/wine/*` のフッター・ナビゲーション。**canonical には Cristal 系以外 1 件も無い**）

| 区分 | 公式キュヴェ | canonical |
|---|---|---|
| **Multi-millésimés** | 🔴 **Collection** ⭐OBP | 🔍 **無し** |
| | **Brut Premier** | 🔍 無し |
| | **Carte Blanche** | 🔍 無し |
| **Millésimés** | **Vintage** ／ **Rosé Vintage** ／ **Blanc de Blancs Vintage** | 🔍 無し |
| | **Vintage Late Release** ／ **Rosé Late Release** | 🔍 無し |
| 🔴 **Cristal** | 🔴 **Cristal** ⭐OBP | 🔍 **`Cristal Brut` — 2015/2014/2013/2012/2006/2002 ＋ 2013 Magnum** |
| | 🔴 **Cristal Rosé** ⭐OBP | 🔍 **`Cristal Rosé Brut` — 2015/2014 ＋ 2013/2008/1996 Magnum** |
| | **Cristal Vinothèque** ／ **Cristal Rosé Vinothèque** | 🔍 **`Cristal Vinotheque` 2004/2002、`Cristal Vinotheque Rosé` 2004/2002**<br>⚠️ **canonical の綴りは `Vinotheque`（アクセント無し）。公式は `Vinothèque`** |
| | **Flacon Médaillon**（`/fr/wine/jeroboam-2002-cristal`） | 🔍 無し |
| **Des vins singuliers** | **Brut Nature 2018 / 2015 / 2012 / 2009 / 2006** | 🔍 無し |
| **静止ワイン** | **Hommage à Camille** | 🔍 無し |

### 🔴 ✅ 公式サイトが掲示するミレジム一覧（「Trouver un millésime」）

| キュヴェ | 公式が並べるヴィンテージ |
|---|---|
| 🔴 **Cristal**（白） | 🔴 **2016 ⭐ / 2015 ⭐ / 2014 / 2013 / 2012 / 2009 / 2008 / 2007 / 2006 / 2005 / 2004 / 2002 / 2000** |
| 🔴 **Cristal Rosé** | 🔴 **2015 / 2014 ⭐ / 2013 / 2012 / 2009 / 2008 / 2007 / 2006 / 2005 / 2004 / 2002 / 2000** |
| **Collection** | **246 ⭐ / 245 / 244 / 243 / 242 / 241** |

🔴 **重要な非対称: `Cristal` は 2016 まで、`Cristal Rosé` は 2015 までしか無い。
すなわち公式の現行リリースは Cristal 2016 と Cristal Rosé 2015 である。**
🔴 **両者に 2010・2011 は無い（造られていない）。**
⚠️ **これは Taittinger と違って「公式が実際に一覧を掲示している」ケースである。
ただし過去に遡ってすべてのミレジムを網羅したものかは公式が明言していない。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 1776 年ランス創業。250 ヘクタール・420 区画を自分で持っている。ミレジムは全部その自社畑から。**
「**1776 年にランスで創業した、シャンパーニュでは数少ない『完全に家族所有で独立』のメゾンです。
いまは 7 代目の Frédéric Rouzaud。2026 年でちょうど 250 年になります。**
このメゾンの一番の特徴は**畑を持っていること**で、**250 ヘクタール、420 を超える区画**を所有しています。
1845 年に Verzenay に 15 ヘクタール買ったのが始まりで、
造り手自身が『**それ以来、うちのミレジムはすべて例外なく自社畑から生まれている。
これはシャンパーニュで唯一の例だ**』と書いています。」

**② Cristal は『白』と『ロゼ』の 2 本立て。別のワインです。色づけは saignée ではなく『infusion』。**
「🔴 **『Cristal』は 1 つのワインの名前ではありません。**
**Cristal（白）**は **Verzenay、Verzy、Beaumont-sur-Vesle、Aÿ、Avize、Mesnil-sur-Oger、Cramant の 7 クリュ**、
**ピノ・ノワールおよそ 60%・シャルドネおよそ 40%**、**蔵で 6 年、デゴルジュマン後さらに 8 か月**。
**Cristal Rosé** は **1974 年に Jean-Claude Rouzaud が創り出した別のキュヴェ**で、
**クリュは Aÿ、Avize、Mesnil-sur-Oger の 3 つだけ**。
🔴 **色づけの方法が独特で、造り手はこれを『infusion（インフュージョン）』と呼びます。**
**ピノ・ノワールのマセラシオンにシャルドネの果汁を流し込んで、一緒に発酵させる。**
**醸造長は日本の茶の作法から着想を得たと言っています。**
**どちらもマロラクティック発酵は 0% です。**」

**③ 有機認証は 135 ヘクタール。シャンパーニュ最大。ビオディナミは『実践』であって『認証』ではない。**
「**造り手の公式表記は『**シャンパーニュで最も広い有機栽培（agriculture biologique）の畑、
135 ヘクタールが認証済み**』です。畑全体が 250 ヘクタールなので、およそ半分強ですね。
**認証機関は Ecocert、2018 年から**です。
**転換は 2006 年に、Cristal Rosé の区画から始まりました。**
🔴 **ビオディナミについては『**その原理に増しつつある場所を与えている**』『**ビオディナミ堆肥を使う**』
という書き方で、**認証は取っていません**。
実際にやっているのは**マサル・セレクション、やさしい剪定、長い休閑、パーマカルチャー由来の手法**です。」

### 追加で使える一手

- 🔴 **Collection 246（$250）の説明**: 「**この 246 という数字はヴィンテージではありません。
  『Louis Roederer にとって 246 回目の収穫』という意味です。**
  1776 年創業なので、**246 回目の収穫は 2021 年**。実際にこのボトルは**2021 年の収穫が 55%**で、
  そこに**『Réserve Perpétuelle（永久リザーヴ）』が 35%（2012〜2020 年の 9 年分）**、
  **フランス産オークの大樽で熟成させたリザーヴワインが 10%** 入っています。
  **蔵で約 4 年。**造り手は『**それぞれの Collection は「横への一歩」、
  メゾンの味の宇宙における新しい一章だ**』と言っています。」
- 🔴 **Collection 246 が特殊な年である理由**: 「**2021 年は造り手自身が『1958 年以来、
  これほど難しく先の読めない年は無かった』と書いた年**です。**収量も低かった。**
  結果として**シャルドネが 54% という異例の比率**になり、
  造り手は『**ある種のブラン・ド・ブランの性格を思わせなくもない**』と書いています。」
- 🔴 **Cristal 2016（$1,120）**: 「**造り手は『単純に「phénoménal」だ』と言い切っています。**
  『**冷涼で遅い年から生まれ、純粋な香りの強さ、エネルギーの振動、果汁感のある口中、
  塩気と白亜の余韻という、稀で魔術的な均衡を明かす。50% が土、50% が太陽という、Cristal の完璧な均衡**』。
  **32 区画、ピノ・ノワール 58%・シャルドネ 42%、木樽仕込み 31%、ドザージュ 7 g/L。**
  造り手自身が**2002・2008・2012 に近いと位置づけています**。」
- 🔴 **Cristal 2015（$1,200）**: 「**2015 は特別な年で、造り手は『2002 年以来はじめて、
  樹齢 20 年を超える 45 区画すべてが Cristal のアッサンブラージュに入った』**と書いています。
  『**暑く乾いた年なのに、太陽よりも「土」の気質を持っている。長期熟成の大きな可能性**』。
  **ピノ・ノワール 60%・シャルドネ 40%、木樽 25%、ドザージュ 7 g/L。**」
- 🔴 **Cristal Rosé 2014（$1,985）**: 「**造り手の言葉は『熟した果実、しなやかで、
  délicieux な質感。信じがたい精確さ。ほとんど電気的な、高い味の強度の悦び』。**
  **ピノ・ノワール 55%・シャルドネ 45%、木樽 19%、ドザージュ 8 g/L。**
  クリュは**Aÿ、Avize、Mesnil-sur-Oger の 3 つだけ**で、白の Cristal より産地が絞られています。」
- **Cristal の由来**: 「**1876 年、皇帝アレクサンドル 2 世のために造られました。
  シャンパーニュ史上最初の『プレステージ・キュヴェ』です。**
  **2026 年でちょうど 150 年**になります。」
- **家族**: 「**20 世紀にメゾンの独立を守ったのが Camille Olry-Roederer で、43 年間トップにいました。**
  現社長の**Frédéric Rouzaud は 7 代目**です。」
- **マサル・セレクション**: 「**造り手は自前の苗床を持っていて、
  『30 年後には Louis Roederer の畑全体が、自分たちで選抜した個体で植えられていることになる。
  シャンパーニュで唯一の例だ』**と書いています。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／出典が矛盾している**）

1. 🔴 ⚠️ **メニューの 4 行目（2014・$1,985・`ROSÉ` セクション）を『白の Cristal』として説明しない。**
   **メニューのセクションは `ROSÉ` であり、`Cristal Rosé 2014` は公式に実在し、公式 fiche もある。**
   **⚠️ ただし `Cristal 2014`（白）も公式に実在するため、決め手はセクション見出しと価格だけである。
   注文を受けたら実ボトルの色とラベルを必ず確認すること。** → §Canonical Conflict `C-6`
2. 🔴 ⚠️ **「Cristal は 45 区画から造られる」と固定的に言わない。**
   **45 は『樹齢 20 年超で Cristal に入る資格を持つ区画の総数』であり、
   2015 は例外的にその全部を使ったが、2016 の公式 fiche は `32 PARCELLES` と書いている。**
   **年によって違う。** 言うなら「**資格を持つ区画は 45 で、年によって使う数が変わる**」まで。
3. 🔴 ⚠️ **「ビオディナミ認証」「Demeter 認証」と言わない。**
   **公式が主張しているのは『**agriculture biologique（有機）で 135 ヘクタール認証済み**』である。**
   🏛 **Agence Bio の認証機関は Ecocert France（FR-BIO-01）、枠組みは EU 2018/848 の有機。**
   🏛 **Demeter France のサイト内検索は 0 件。**
   **公式がビオディナミについて書くのは『原理に場所を与えている』『ビオディナミ堆肥』まで。**
   言えるのは「**有機認証 135 ヘクタール、Ecocert、2018 年から。
   ビオディナミの手法も取り入れているが認証は取っていない**」まで。
4. 🔴 ⚠️ **「Cristal Rosé は saignée（セニエ）で造る」「赤ワインを加える」と言わない。**
   **公式サイト・公式テクニカルシートのどこにも `saignée` の語は無い。**
   **公式の記述は『長く、ゆるやかな「infusion」。メゾン固有の技法。
   シャルドネの果汁の幾ばくかをピノ・ノワールのマセラシオンに流し込み、一緒に発酵させる』である。**
   🔴 **THÉSEUS の DB は現在『saignée method with red wine』と書いているが、これは公式に反する。**
5. 🔴 ⚠️ **「Louis Roederer は全部自社畑」と言わない。**
   **公式が『例外なく自社畑』と限定しているのは `millésime`（ミレジム表示のワイン）だけである。**
   **`Collection` は公式テクニカルシート自身が
   『自社ドメーヌの葡萄は、協働栽培者の「Cœur de Terroir」選抜区画の葡萄で補われる』と明記している。**
   → **OBP 1 行目（Collection 246）の説明で特に危険。**
6. 🔴 ⚠️ **「250 ヘクタールはすべてグラン・クリュとプルミエ・クリュ」と断定しない。**
   **`/fr/house` は `exclusivement`、`/fr/250ans` は `essentiellement` と書いており、公式内で揺れている。**
   言うなら「**250 ヘクタール、主にプルミエ・クリュとグラン・クリュ**」まで。
7. ⚠️ **Cristal の lieux-dits の形成開始年を断定しない。**
   **公式内に `1845`（`/fr/cristal2015`）と `1841`（`/fr/cristal2016` の英文段落）の 2 つがある。**
   言うなら「**1840 年代から代々築かれてきた区画群**」まで。
8. 🔴 ⚠️ **Collection の `246` を「ベースヴィンテージ」「2046 年」「シリーズ番号」などと言わない。**
   **公式の語は『246ème vendange』（246 回目の収穫）と『246e assemblage』（246 番目のアッサンブラージュ）。**
   **ベース年は 2021 で、アッサンブラージュの 55% を占める。この 2 つは別の数字である。**
9. 🔴 ⚠️ **Cristal と Collection の醸造条件を混ぜない。**
   **Cristal はマロラクティック発酵 0%。Collection 246 は 30%。**
   **「Roederer はマロをやらない」は誤り。「Cristal はやらない」が正しい。**
10. ⚠️ **第三者点数を言わない。**
    **公式サイト・全テクニカルシートに点数の掲載は一切無い。**
    🔴 **THÉSEUS の DB に入っている「98 points」「96–97 pts」「97 points」は公式起源ではない。**
11. ⚠️ **アルコール度数・デゴルジュマン日・生産本数・出荷価格を言わない。**
    **公式に一切記載が無い。**（メゾン全体の「年間約 300 万本」だけが唯一の量的記述。）
12. 🔴 ⚠️ **「2014 が jetting を導入した最初の Cristal」と言わない。**
    **公式サイト・全テクニカルシートに `jetting` の語は一度も出てこない。**
    **THÉSEUS の DB にはこの記述があるが、本調査では公式の裏づけを取れなかった。**
13. 🔴 ⚠️ **Deutz / Delas / Domaines Ott / Château Pichon Comtesse / Merry Edwards / Diamond Creek /
    Scharffenberger / Roederer Estate（Anderson Valley）の話を、
    「Champagne Louis Roederer の話」として混ぜない。**
    🔴 **`louis-roederer.com` の全取得ページを機械走査したが、これらの姉妹ドメーヌへの言及は 1 件も無い。**
    **したがって本ドシエは、グループ構造について公式の裏づけを一切持っていない。**
    **OBP の他の行でこれらに当たるものがあれば、それは `CAT-3`（brand_axis）の話であって本件ではない。**
14. ⚠️ **`Cristal Rosé 2016` は存在しない前提で話さない／存在する前提でも話さない。**
    **公式の一覧は Rosé が 2015 止まり、白が 2016 まで。**
    **「まだ出ていない」とは公式に書かれていないので、「公式の現行は Rosé が 2015」までにとどめる。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **REGISTER.md も canonical も本書では一切編集していない。**
🔴 **新しい番号は開かない。既存の登録 ID に証拠を足す形で書く。**
🔴 **既存のどの族にも当たらないものが 1 つあり、それは「番号なし」と明記する。**

---

### 🔴 【A】`C-6`（Taittinger ドシエの提案 ID）—— **証拠追加。ただし Roederer は「対偶事例」である**

🔴 **タスク側の前提に対する push back を先に書く。**

**タスクは「canonical が `Cristal` を 1 キュヴェしか持っていなければ `C-6` と同じ欠陥」と述べていた。
実測の結果、canonical は `Cristal` を 4 キュヴェ持っている。したがって前提は成立しない。**

🔍 **canonical の実データ（読み取りのみ）:**

| cuvée | color | canonical レコード |
|---|---|---|
| **`Cristal Brut`** | **`Blanc`** | `cristal-2015` `cristal-2014` `cristal-2013` `cristal-2012` `cristal-2006` `cristal-2002` `cristal-2013-magnum` |
| 🔴 **`Cristal Rosé Brut`** | 🔴 **`Rosé`** | 🔴 **`cristal-rose-2015` `cristal-rose-2014` `cristal-rose-2013-magnum` `cristal-rose-2008-magnum` `cristal-rose-1996-magnum`** |
| **`Cristal Vinotheque`** | `Blanc` | `cristal-vinotheque-2004` `cristal-vinotheque-2002` |
| **`Cristal Vinotheque Rosé`** | `Rosé` | `cristal-vinotheque-rose-2004` `cristal-vinotheque-rose-2002` |

🔴 **すなわち `C-6` の推奨のうち「色を cuvée の識別属性として持たせる」側は、Roederer では既に実装されている。**
🔴 **そして OBP 4 行目（2014・ROSÉ・$1,985）の正しい着地点である `cristal-rose-2014` は
canonical に実在し、その `grapes = ['Pinot Noir 55%','Chardonnay 45%']` と `dosage = '8 g/L'` は
✅ 公式テクニカルシート `lr_tech_sheet_cristal_rose_2014_fr.pdf` と完全に一致する。**

🔴 **それでも 4 行目は `candidate` 止まりである。理由は 1 つしかない。**
🔍 **intake の evidence 文字列が、4 行すべてで完全に同一だからである:**
> 「**ラベル 'Cristal' が canonical の 4 キュヴェに同程度に該当し一意に決まらない:
> Cristal Brut, Cristal Rosé Brut, Cristal Vinotheque, Cristal Vinotheque Rosé**」

**BLENDS セクションの 3 行と ROSÉ セクションの 1 行が、同じ evidence を返している。
＝ matcher はセクション見出しを入力に取っていない。**

🔴 **したがって Roederer は `C-6` に対する最も強い形の証拠である ——
「canonical 側を完璧にしてもなお解けない」ことを示す統制群だからである。**
**`C-6` の 2 つの推奨のうち、有効なのは第 2 の推奨
（**メニューのセクション見出しを matcher の入力信号にする**）だけであり、
Roederer ではそれ「だけ」で 4 行目が確定する。**

**Confidence: High**（canonical の実データ、intake の evidence 文字列、公式 fiche の 3 点で裏づけ）

---

### 🔴 【B】`C-4`（識別語を持たないキュヴェ名）—— **本件の直接の族。証拠追加**

🔴 **OBP の印字は `'Cristal,' Brut`。この文字列には
`Rosé` か否か、`Vinothèque` か否かを決める語が一つも無い。**
**`Brut` は 4 キュヴェすべてに当てはまるため、識別に寄与しない。**
**これは `C-4`（38 件の族）の教科書的な事例である。**
🔴 **`C-6` の根本原因が `C-4` であるという Taittinger ドシエの指摘は、Roederer でもそのまま成り立つ。**

⚠️ **付随して、canonical の名前と公式の正式名にも差がある（新規の衝突としては開かない）:**
- **canonical `Cristal Brut` / `Cristal Rosé Brut`** ↔ **公式のキュヴェ名は `Cristal` / `Cristal Rosé`**
  （`Brut` は公式のキュヴェ名の一部ではない）
- 🔴 **canonical `Cristal Vinotheque` / `Cristal Vinotheque Rosé`** ↔
  **公式は `Cristal Vinothèque` / `Cristal Rosé Vinothèque`**
  → ⚠️ **アクセントが落ちている（`S-1` 符号化破損の族に近い）だけでなく、
  `Rosé` と `Vinothèque` の語順が公式と逆である。**

---

### 🔴 【C】`V-1`（Krug Grande Cuvée — édition が層をまたぐ）—— **証拠追加。Roederer `Collection` は同型**

**1. 該当する OBP 行**
🔍 **intake index 47** — `'Collection 246,' Brut` / vintage `null` / $250 /
`match_state = unresolved` / `cuvee_state = unresolved` /
evidence 「**'Louis Roederer' の canonical キュヴェ 4 件に一致無し: 'Collection 246'**」
🔍 **`normalized_cuvee = "Collection 246"` / `normalized_vintage = "NV"`**
→ 🔴 **正規化の時点で `246` はキュヴェ名の一部として扱われ、`vintage` は `NV` に潰されている。
`246 → 2021` という写像はどこにも保持されていない。**

**2. 公式が何と言っているか（✅ 一次資料）**
- ✅ **`lr_ft_collection_246_fr.pdf`**: 「**Cette 246ème vendange chez Louis Roederer…**」
  「**Les vendanges se sont déroulées du 13 au 30 septembre 2021.**」
  「**246ème ASSEMBLAGE : […] VENDANGE 2021 : 55%**」
- ✅ **`/fr/collection246`**: 「**Ce 246e assemblage de la Maison Louis Roederer…**」
- ✅ **番号とベース年の対応が 6 件連続で確定**: `241→2016` `242→2017` `243→2018` `244→2019` `245→2020` `246→2021`

🔴 **したがって `246` は「ベース年の別表記」ではなく、
メゾンの収穫／アッサンブラージュの序数である。ベース年 2021 は独立した値であり、
しかも「アッサンブラージュの 55%」という比率を伴う。**
🔴 **さらに `Réserve Perpétuelle 35%（2012–2020 の 9 年）` と
`vins de réserve élevés sous bois 10%（2012–2017）` という 2 つの多年成分がある。
すなわち「単一のベース年」でこのワインを表現することは、そもそも原理的に不完全である。**

**3. canonical 側の状態（🔍 読み取りのみ）**
🔴 **canonical に `Collection` のレコードは 1 件も存在しない。**（→ これは conflict ではなく **gap**）
🔍 **既存の同型 2 例を実測した:**

| 生産者 | canonical `name` | canonical `vintage` |
|---|---|---|
| **Krug** | **`Grande Cuvée 173ème Édition`** | **`NV · based on 2017`** |
| **Jacquesson** | **`Cuvée 747 Extra Brut`** | **`MV (Base: 2019)`** |

🔴 **どちらも「序数を `name` に入れ、ベース年を `vintage` 文字列に埋める」という同じ設計をしており、
しかも `vintage` の書式が互いに違う（`NV · based on YYYY` と `MV (Base: YYYY)`）。**
**`Collection` を追加すれば 3 つ目の同型・3 つ目の書式候補になる。**

**4. 🔍 本調査で実測した `vintage` 文字列の異表記（`db_wine_canonical.json` 928 件を機械走査）**

| 書式 | 件数 | 例 |
|---|---|---|
| `NV`（素の NV） | **88** | `gosset-excellence-brut` |
| `NV · based on YYYY` | **12** | `krug-grande-cuvee-162`〜`173` |
| `NV · 2022 Base` | **4** | `remi-leroy-reserve-blanc-de-noirs-nv` |
| `NV (Base: YYYY)` | **3** | `egly-ouriet-grand-cru-brut-nv` / `bollinger-pn-vz19` / `drappier-pere-pinot` |
| `MV (Base: YYYY)` | **2** | `jacquesson-cuvee-746` / `747` |
| `NV (LCnn)`（lot） | **2** | `prevost-la-closerie-2021` / `2023` |
| `NV（2022）`（**全角括弧**） | **1** | `bougy-chetillon-de-haut-nv2022` |
| `NV · blend 2005–2015` | **1** | `krug-rose-27` |

🔴 **素の `NV` を除くと 26 レコード・7 書式。**
⚠️ **登録票の記述（「24 件・5 書式」）とは数が合わない。
本書の数字は 2026-08-06 時点の `migration/out/export/db_wine_canonical.json` に対する実測である。
どちらが正しいかは判定しない（走査条件の違いの可能性が高い）。**

**5. 推奨（🔒 実行していない）**
- **`Collection` は canonical にまだ存在しないので、「壊す前に決められる」唯一の機会である。**
- 🔴 **Roederer の場合、最低でも 3 つの値が必要になる: `release_ordinal = 246`、
  `base_year = 2021`、`base_year_share = 55%`。** これに `perpetual_reserve_share = 35%` が続く。
- 🔒 **どの層に置くかは設計判断であり、本書では実行していない。**

**Confidence: High**（公式 fiche 6 点で番号→年の写像を確定。canonical 側は機械走査）

---

### 🔴 【D】`V-2`（Louis Roederer Cristal 2013 — 容量が vintage 行を分ける）—— **証拠追加。登録票の「1 組」は過小である**

🔍 **実測: Roederer の 16 レコードのうち、フォーマットが identity に入っているものは 4 件ある。**

| id | `name` | `obp_format` | 標準ボトルの対応行 |
|---|---|---|---|
| `cristal-2013-magnum` | **`Cristal Brut Magnum`** | `By the bottle (Magnum)` | ✅ **`cristal-2013` がある**（＝登録票が指す「1 組」） |
| 🔴 `cristal-rose-2013-magnum` | **`Cristal Rosé Brut Magnum`** | `By the bottle (Magnum)` | 🔴 **無い** |
| 🔴 `cristal-rose-2008-magnum` | **`Cristal Rosé Brut Magnum`** | `By the bottle (Magnum)` | 🔴 **無い** |
| 🔴 `cristal-rose-1996-magnum` | **`Cristal Rosé Brut Magnum`** | `By the bottle (Magnum)` | 🔴 **無い** |

🔴 **登録票 `V-2` は「1 組 / 影響 0 本 / Confidence Medium」と記録しているが、
実際にはマグナム行は 4 件あり、うち 3 件は標準ボトルの対応行を持たない「マグナム単独行」である。**
🔴 **さらに重要な点: フォーマットは 2 か所に二重符号化されている ——
`name` の末尾（`… Magnum`）と、専用フィールド `obp_format`（`By the bottle (Magnum)`）である。**
**専用フィールドが既にあるのに `name` にも入れている、というのが defect の実体であり、
「容量が identity に紛れ込んでいる」という登録票の分類自体は正しい。**

⚠️ **本ドシエの OBP 4 行はいずれもフォーマットを印字していない（暗黙に標準ボトル）。
したがって `V-2` の「影響 0 本」は本調査でも変わらない。**

**Confidence: High**（canonical の機械走査。分類は既存 `V-2` のまま）

---

### 🔴 【E】**canonical の説明文（`house_style` / `description` / `obp_note`）が公式一次資料と矛盾する**
### —— **既存のどの登録 ID にも当たらない。番号は開かない（採番は CTO 判断）**

🔴 **これはマッチングの衝突ではなく、「canonical に入っている散文が事実として誤っている」という別種の問題である。
登録票の `P-` `C-` `V-` `S-` のいずれの族にも当たらないため、
本書は形だけを記述し、番号を付けない。**

**1. `house_style`（🔴 Roederer の 16 レコード**すべて**に同一文字列で入っている）**

> 「**Prestige cuvée Cristal uses approximately equal blend of Chardonnay and Pinot noir;
> rosé colored via saignée method with red wine; 2000 vintage had dosage of 10 g/L;
> since 2012 all Cristal vintages produced from Demeter-certified biodynamically farmed fruit**」

| 主張 | 公式／公的登録での検証 | 判定 |
|---|---|---|
| 「approximately equal blend of Chardonnay and Pinot noir」 | ✅ 製品ページ「**Chardonnay (environ 40%) と Pinot noir (environ 60%)**」。fiche は PN 58–60%。 | 🔴 **不正確**（equal ではない） |
| 🔴 「rosé colored via **saignée** method **with red wine**」 | ✅ fiche `…rose_2013`「**longue et douce «infusion», technique propre à la Maison. Quelques jus de Chardonnays sont coulés dans une macération de Pinots noirs, pour fermenter ensemble**」。**`saignée` の語は公式に一度も出ない。赤ワイン添加の記述も無い。** | 🔴 **誤り** |
| 「2000 vintage had dosage of 10 g/L」 | ⚠️ **2000 の公式 fiche を本調査で取得できていない。**（公式サイトの PDF リンクは 2008 以降のみ） | ⚠️ **未検証（否定もできない）** |
| 🔴 「since 2012 all Cristal vintages produced from **Demeter-certified** biodynamically farmed fruit」 | 🏛 **Agence Bio: 認証機関 `Ecocert France`（`FR-BIO-01`）、枠組み `Agriculture biologique Europe (EU) 2018/848`、engagement `2018-03-12`。**<br>🏛 **Ecocert 証明書ページに掲載される認証は有機の 1 件のみ。**<br>🏛 **Demeter France のサイト内検索「roederer」→ 0 件。**<br>✅ **公式の主張は「agriculture biologique で 135 ha 認証済み」。** | 🔴 **誤り。しかも公的登録で反証できる種類の誤り。** |

**2. `cristal-2015` の `description_en` / `obp_note`**
- 「**Cristal 2015 comes from exclusively Roederer-owned Grand Cru vineyards (principally Verzenay and Avize)**」
  → ⚠️ **公式 fiche の `CRUS PRINCIPAUX` は 7 つ（Verzenay, Verzy, Beaumont-sur-Vesle, Aÿ, Avize,
  Mesnil-sur-Oger, Cramant）。「principally Verzenay and Avize」は公式に無い切り取りである。**
- 「**farmed biodynamically since 2013**」／ `obp_note`「**The biodynamic conversion that began in 2013**」
  → 🔴 **公式は「2006 年から `culture biologique régénérative` への転換、起点は Domaine Cristal Rosé の区画」。
  `2013` という年も `biodynamic` という語も公式に無い。**
- 「**Like Krug and Salon, Cristal practices no malolactic fermentation**」
  → ✅ **MLF 0% 自体は公式 fiche（2014/2015/2016 とも `FERMENTATION MALOLACTIQUE : 0%`）で正しい。
  ただし他メゾンとの比較は Roederer 公式の記述ではない。**
- ✅ 「**This bottle lived 6 years underground before it met you**」
  → ✅ **公式「Cristal vieillit 6 années en cave」と整合。**

**3. `cristal-2014` の `description` / `obp_note`**
- 「**45 parcelles Grand Cru dans 7 villages**」
  → 🔴 **公式が `45 parcelles` を結びつけているのは 2014 ではなく 2015 である
  （「Pour la première fois depuis 2002, ce millésime **2015** est issu de l'ensemble des 45 parcelles…」）。
  そして 2016 の fiche は `32 PARCELLES` と書いている。区画数は年ごとに変わる定数ではない。**
  ⚠️ **7 クリュという数字自体は公式と一致する。**
- 「**Chef de Cave Jean-Baptiste Lécaillon (since 1999) began biodynamic conversion in 2000**」
  → ✅ **`since 1999` は公式と一致。**🔴 **`biodynamic conversion in 2000` は公式に無い。**
- 🔴 「**2014 : premier Cristal avec le jetting**」「**39/45 parcelles**」「**96–97 pts**」
  → 🔴 **`jetting` の語は公式サイト・全 fiche に一度も現れない。`39/45` も無い。点数は公式に一切無い。**

**4. `cristal-rose-2014` / `cristal-rose-2015` の `description` / `obp_note`**
- 「**macération à basse température et co-fermentation — méthode unique à Roederer**」
  → ⚠️ **`co-fermentation` は公式（「pour fermenter ensemble」）と整合する。**
  🔴 **しかし `à basse température`（低温）は公式に記述が無い。**
  🔴 **そして公式が用いる呼称 `infusion` / `infusion douce` を canonical は一度も使っていない。**
- 🔴 ⚠️ **同一レコード内で `house_style` が「saignée with red wine」、
  `description` が「macération et co-fermentation」と述べており、canonical が自分自身と矛盾している。**
- 🔴 「**98 points**」「**97 points**」 → **公式に点数の掲載は一切無い。**

**5. 影響**
🔴 **照合（matching）への影響はゼロ。これらのフィールドはマッチングに使われていない。**
🔴 **だが staff 向け表示や生成テキストに使われれば、卓上で
「Demeter 認証のビオディナミです」「ロゼはセニエで赤ワインを加えます」「45 区画です」
「98 点です」という、公式に反する／公式に根拠の無い発言を生む。**
→ **§Staff Notes ⚠️ ②③④⑩⑫ で塞いだ。**

**6. 推奨（🔒 実行していない）**
- **`house_style` が 16 レコードすべてに同一文字列で複製されている構造そのものが、
  1 か所の誤りを 16 倍に増幅している。生産者層に 1 つ持つべき値である。**
- 🔒 **本書では canonical を一切変更していない。採番も分類も CTO 判断。**

**Confidence: High**（公式一次資料＋公的登録で個別に反証済み。ただし「2000 のドザージュ 10 g/L」だけは未検証）

---

### 🔴 【F】**gap（conflict ではない）—— canonical に存在しないもの**

🔴 **登録票のどのクラスもカバーしないため、「gap」として記録する。**

| 欠落 | 影響 |
|---|---|
| 🔴 **`Collection` キュヴェが canonical に 1 件も無い** | 🔴 **OBP 1 行（$250）が `unresolved`。着地点そのものが存在しない。** |
| 🔴 **`cristal-2016` が canonical に無い** | 🔴 **OBP 1 行（$1,120、現行リリース）が仮にキュヴェを解決できても、vintage 層で着地できない。** |
| **`Brut Premier` / `Carte Blanche` / `Vintage` / `Rosé Vintage` / `Blanc de Blancs Vintage` /
`Vintage Late Release` / `Rosé Late Release` / `Brut Nature`（5 年分） / `Hommage à Camille` /
`Flacon Médaillon` が canonical に無い** | **本 OBP には無いが、公式の主要ラインナップの大半が未登録である。** |

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY / 標準ルール `D-2026-08-05-09`**）

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の会社名** | ✅ **合格。** `https://www.louis-roederer.com/fr/roederer_layout/legal_terms_popup`（Mentions légales、**最終更新 13/05/2026**）に **`Champagne Louis Roederer (CLR)` / `Société anonyme au capital de 3 672 000 €` / `N.M. 291-001` / `RCS Reims B 335 681 169 00017`** を明記 |
| **(c) 公的登録と一致する住所** | ✅ 🏛 **合格。** 公式表示 `CS 40014 - 21 boulevard Lundy - 51722 REIMS Cedex` に対し、**`recherche-entreprises.api.gouv.fr` の `SIREN 335681169` / `SIRET 33568116900017` / siège `21 BOULEVARD LUNDY 51100 REIMS` / NAF `11.02A` が一致。** |
| **(d) 整合した商業・法務フッター** | ✅ **合格。** 年齢確認ゲート、`L'abus d'alcool est dangereux pour la santé` の法定表示、Mentions légales、Politique de confidentialité、`QUALITÉ & CARACTÉRISTIQUES ENVIRONNEMENTALES`、AGEC 法の一意識別子（`FR246127_01QEKR`）、`Tribunal de Commerce de REIMS` の管轄条項、**Index égalité femmes-hommes 67/100（2026 年、2025 年データ）** まで完備。**免責的な「ファンサイト」表記は無い** |
| **一人称の告白的記述** | **無し。** 過去バッチで掴んだファンページの兆候は一切無い |
| **ドメイン売却ページの兆候** | **無し** |
| 🏛 **独立系登録による裏取り** | ✅ **Agence Bio と Ecocert の双方が、同じ SIRET・同じ住所で `CHAMPAGNE LOUIS ROEDERER` を掲載している。** |

🔴 **本調査で `NOT_THE_PRODUCER_*` / `FANPAGE_*` として退けたサイトは無い。**
（**WebSearch は Demeter France の所在確認にのみ用い、検索結果の要約文は事実として一切採用していない。
Demeter の判定は `demeter.fr` 上で直接検索して確認した。**）

⚠️ 🔴 **ただし 1 件、注意すべき発見がある。**
**`https://www.louis-roederer.com/sitemap.xml` → `/fr/sitemap.xml` の 148 件の `<loc>` は、
すべて `http://roederer-site.pp.mzrn.net/...` というステージング用ドメインを指している
（`lastmod` はすべて `2014-01-21T13:46:00`）。**
🔴 **これは公式サイトの設定漏れであって別人のサイトではないが、
「公式ドメインから配信された XML の中に、公式でないホスト名が入っている」という状態である。**
**本書はこのドメインから 1 バイトも取得しておらず、事実の根拠に一切使っていない。**
**URL 構造は `www.louis-roederer.com` のフッター・ナビゲーションから読み取った。** → Open Questions 5

### 一次資料（**`louis-roederer.com` および公的登録のみ。非公式ソースは事実の根拠に使っていない**）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt`** | **Drupal 標準。`Crawl-delay: 10`。sitemap の指定なし。** |
| ⚠️ **`/sitemap.xml` → `/fr/sitemap.xml`** | ⚠️ **148 URL。すべてステージングドメイン。`lastmod 2014`。**`brut-premier` が現役として載っているなど内容も古い。**事実には使用せず。** |
| **`/fr/prehome`（年齢確認ゲート）** | **サイト全体のナビゲーション構造（全キュヴェ URL、全 Cristal ミレジムページ URL）。JS から入場導線 `/{lang}/prehome/enter` を特定。** |
| 🔴 **`/fr/wine/cristal`** | 🔴 **Cristal の中核。**「1876 年、皇帝アレクサンドル 2 世」「Chardonnay 環境 40% / Pinot noir 環境 60%」「**蔵で 6 年 ＋ デゴルジュマン後 8 か月**」「20 年以上の熟成能力」「**ミレジム一覧 2016〜2000（13 年）**」「各年の醸造長コメント」。**テクニカルシート 7 点へのリンク** |
| 🔴 **`/fr/wine/cristal-rose`** | 🔴 **Rosé が独立キュヴェであることの決定的証拠。**「**l'infusion douce**」「日本の茶の師匠に着想」「1998 年 La Villers の植え替え」「**ミレジム一覧 2015〜2000（12 年）**」。**テクニカルシート 6 点へのリンク** |
| 🔴 **`/fr/wine/collection` ／ `/fr/collection246`** | 🔴 **`V-1` の根拠。**「**Ce 246e assemblage de la Maison Louis Roederer**」「2021 は 1958 年以来最も困難な年」「Réserve Perpétuelle 35%」「蔵で約 4 年」「Cœur de Terroir」「Frédéric Rouzaud の言」。**テクニカルシート 6 点へのリンク** |
| 🔴 **公式テクニカルシート PDF 14 点**（`/sites/default/files/pdf/`、全点 `application/pdf`・テキストレイヤーあり） | 🔴 **`ft_cristal_2016_fr` / `lr_tech_sheet_cristal_blanc_2015_fr` / `..._2014_fr` / `..._2013_fr` / `lr_tech_sheet_cristal_rose_2014_fr` / `..._2013_fr` / `ft_cristal_rose_2015_fr` / `cristal_rose_2012_tech_sheet_fr` / `lr_ft_collection_246_fr` / `lr_tech_sheet_collection_241`〜`245_fr`。**<br>🔴 **セパージュ・木樽比率・MLF %・ドザージュ・主要クリュ・区画数・収穫期間・社内 3 区分・Réserve Perpétuelle の内訳** |
| 🔴 **`/fr/250ans`（＝ `/fr` 実体）** | 🔴 **本ドシエで最も情報密度の高いページ。**「**Fondée à Reims en 1776**」「1833 年に Louis Roederer が相続し名を与える」「1876 年 Cristal ＝史上最初のプレステージ・キュヴェ」「**1974 年 Cristal Rosé、Jean-Claude Rouzaud**」「Camille Olry-Roederer 在任 43 年」「Frédéric Rouzaud 第 7 世代」「**250 ha / 420 区画超**」「🔴 **le plus vaste vignoble de Champagne en agriculture biologique avec 135 hectares certifiés**」「**l'infusion douce**」 |
| 🔴 **`/fr/house`（＝`/fr/homepage`）** | 🔴 **「250 hectares situés exclusivement dans les Grands et Premiers Crus de la Marne」「En 2024 … 250 ha composés de 420 parcelles」「1845 年 Verzenay 15 ha」「**tous les millésimes … issus exclusivement de nos propres vignes, ce qui est unique en Champagne**」「約 300 万本」「**une place grandissante aux principes de la biodynamie**」「vinification parcellaire」「手摘み・収穫地で圧搾」** |
| 🔴 **`/fr/expression-of-biodiversity`** | 🔴 **§Farming の中核。**「1990 年代末からの `l'arrêt des intrants et la régénération des sols`」「sélection massale の詳細な定義」「自社の苗床、30 年後には全畑が自家選抜個体に」「台木の自社栽培」「taille douce」「生垣・石垣・蜜蜂・果樹・jachère の輪作」「Lécaillon の言」 |
| 🔴 **`/fr/cristal2016`** | 🔴 **「**Cristal est un champagne de terroir et d'artisan, issu exclusivement du domaine éponyme cultivé en agriculture biologique**」。**⚠️ FR ページ内に未翻訳の英文段落が混在し、そこに「since 1841」とある** |
| 🔴 **`/fr/cristal2015`** | 🔴 **「**Pour la première fois depuis 2002, ce millésime 2015 est issu de l'ensemble des 45 parcelles de plus de vingt ans d'âge**」「lieux-dits patiemment constitués **depuis 1845**」「**composts biodynamiques**」「permaculture」 |
| 🔴 **`/fr/cristal-rose-50`** | 🔴 **Cristal Rosé の 50 年史。**「1974 年、Aÿ のピノ・ノワールと Avize / Le Mesnil-sur-Oger のシャルドネ」「**infusion douce**」「**la transition vers une culture biologique régénérative est engagée dès 2006, en commençant par les parcelles du Domaine Cristal Rosé**」「2008 年が転換点」 |
| **`/fr/news/certification-viticulture-durable`（2016-07-22）** | **「Depuis 2014 … certification viticulture durable selon le référentiel du Comité Champagne et HVE」。Johann Merle（Régisseur des Vignobles）。生垣・景観・列長・草生面積・蜜蜂・果樹園再生。2016 年 7 月に更新監査** |
| **`/fr/news/certification-sustainable-winegrowing`（英語版）** | **⚠️ FR 版と数字・主張の食い違いなし（既知の罠のチェック用に取得）** |
| **`/en/house` ／ `/en/wine/cristal`** | **⚠️ FR/EN の数値差の検証用。「250 hectares」「three million bottles」「6 years … 8 months after dégorgement」「increasingly, the principles of biodynamic cultivation」——** ✅ **FR と一致。翻訳による数値の乖離は検出されなかった。** |
| **`/fr/roederer_layout/legal_terms_popup`** | **真正性の検証。法人名・資本金・NM 番号・RCS・住所・AGEC 識別子・管轄・Index égalité** |

### 🏛 公的登録（**すべて読み取りのみ**）

| 登録 | 取得した情報 |
|---|---|
| 🏛 **`recherche-entreprises.api.gouv.fr`** | **`CHAMPAGNE LOUIS ROEDERER` / SIREN `335681169` / SIRET `33568116900017` / NAF `11.02A` / siège `21 BOULEVARD LUNDY 51100 REIMS`。**⚠️ **`date_creation = 1956-01-01` は法人登記の日付であり、公式の創業年 1776 とは別の概念。** |
| 🏛 **Agence Bio（`opendata.agencebio.org/api/gouv/operateurs`）** | 🔴 **numéro bio `133856`。認証機関 `Ecocert France`（`FR-BIO-01`）。`etatCertification: ENGAGEE`、`dateEngagement: 2018-03-12`、`dateSuspension: null`、`dateArret: null`。`mixite: "Oui"`。`productions` に `Raisin de cuve`（`AB`/`C1`/`C2`/`C3`/`CS`/`EAC`、基準年 2026）と `Vins de raisin`（`AB`/`EAC`）。活動地に `15 Rue Henry Henrion, 51160 AY` を含む。** |
| 🏛 **Ecocert 証明書（`certificat.ecocert.com`）** | 🔴 **掲載認証は「`Certification Agriculture biologique Europe (EU) 2018/848`」の 1 件のみ。活動は `Agriculteur (production végétale)` / `Fabricant & Transformateur` / `Grossiste spécialisé`。ビオディナミ認証の記載なし。** |
| 🏛 **Demeter France（`demeter.fr`）** | 🔴 **サイト内検索「roederer」→「Il semblerait qu'il n'y ait pas de résultats pour cette recherche」（0 件）。`/adherents/champagne-louis-roederer/` は HTTP 404。** |

### 取得できなかったもの / 存在しなかったもの

- 🔴 **`lr_tech_sheet_collection_245_fr.pdf` はフォント埋め込みが壊れており（cid 写像欠落）、
  テキスト抽出が文字化けする。245 のセパージュ・MLF・ドザージュは確定していない。**
  **（`35% Pinot noir` と `RÉSERVE PERPÉTUELLE : 35%` だけが読める。）**
- 🔴 **`Cristal 2000` / `2002` などの古いミレジムのテクニカルシートは公式サイトにリンクが無い。**
  **PDF リンクは Cristal 白が 2008 以降、Rosé が 2008 以降のみ。**
  → **canonical の「2000 vintage had dosage of 10 g/L」を検証できなかった理由。**
- 🔴 **`Collection 241` の fiche はセパージュ・アッサンブラージュ内訳の記載形式が他の 5 点と異なり、
  数値ブロックが取得できていない。**
- 🔴 **公式は Cristal / Cristal Rosé の「熟成年数」を fiche に書いていない。**
  **6 年＋8 か月は製品ページ側の記述であり、ミレジム別ではない。**
- ⚠️ **アルコール度数・デゴルジュマン日・生産本数・希望小売価格が、どのキュヴェにも公式に無い。**
- ⚠️ **クリュごと／区画ごとのヘクタール数が公式に無い。**
- ⚠️ **`Collection` の「Cœur de Terroir」協働栽培者の名前・所在が公式に無い。**
- ⚠️ **`Brut Premier` から `Collection` への移行を「後継」と明示する公式の文が見つからなかった。**
- 🔴 **`louis-roederer.com` の全取得ページを機械走査したが、
  Deutz / Delas / Domaines Ott / Pichon Comtesse / Merry Edwards / Diamond Creek /
  Scharffenberger / Roederer Estate（Anderson Valley）への言及は 1 件も無い。**
  → **本ドシエはグループ構造について公式の裏づけを持たない。事実として主張していない。**
- ⚠️ **`/fr/vintages`（Trouver un millésime）は JS 描画で、静的取得では中身が取れなかった。**
- ⚠️ **`/fr/news` は 148 件規模のアーカイブがあるが、本調査で読んだのは 4 件である。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical: `producer = 'Louis Roederer'` のレコード 16 件**
（`cristal-2015` `-2014` `-2013` `-2013-magnum` `-2012` `-2006` `-2002` /
`cristal-rose-2015` `-2014` `-2013-magnum` `-2008-magnum` `-1996-magnum` /
`cristal-vinotheque-2004` `-2002` / `cristal-vinotheque-rose-2004` `-2002`）
🔍 **全 16 件が `founded_year = 1776` / `region = Champagne` / `subregion = 'Reims'` /
`appellation_id = appellation:champagne` / `type = 'Champagne'`。**
🔍 **`Collection` / `Brut Premier` / `Vintage` / `Blanc de Blancs` / `Brut Nature` /
`Hommage à Camille` / `Carte Blanche` のレコードは 0 件。**
🔍 **`cristal-2016` は存在しない。**
🔍 **OBP: 4 本**（`obp_intake_normalized_20260804.json` index **47 / 48 / 49 / 142**）。
**全 4 本が `producer_state = exact`。`match_state` は 1 本が `unresolved`、3 本が `candidate`。
`confidence` は 4 本とも `0.0`。`proposed_canonical_cuvee_id` は 4 本とも `null`。**
🔒 **canonical・`REGISTER.md`・intake のいずれも編集していない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | 🔴 **法人名・資本金・NM 番号・RCS・住所が Mentions légales で確定し、🏛 企業登録・Agence Bio・Ecocert の 3 つの独立した登録と一致。創業年 1776 も公式が明記。** |
| **Overview** | **High** | 自社畑戦略、250 ha / 420 区画、有機 135 ha、家族独立性、300 万本がすべて一次で取れた |
| **History** | **High** | 🔴 **1776 / 1833 / 1845 / 1876 / 1920s / 1933 / 1974 / 1998 / 1999 / 2006 / 2014 / 2018 / 2024 / 2026 が公式で確定。**⚠️ **lieux-dits の起点だけが 1841 と 1845 で揺れる** |
| **Location** | **Medium-High** | 250 ha / 420 区画 / 3 地区 / キュヴェ別のクリュ構成と社内 3 区分まで確定。⚠️ **`exclusivement` と `essentiellement` の矛盾、区画数の年次変動** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **本ドシエで最も強い節。公式の主張（有機 135 ha）を、🏛 Agence Bio・Ecocert・Demeter France の 3 つの独立した登録で裏取りし、「practised vs certified」を確定させた。実務（massale・taille douce・jachère・permaculture・自社苗床）も一次で取れた** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **OBP 4 本すべてについて、公式 fiche からセパージュ・木樽比率・MLF%・ドザージュ・収穫期間が取れた。`infusion` の定義は fiche の verbatim。**⚠️ **デブルバージュ・発酵温度・ルミュアージュ・分析値は公式に不在** |
| **Style** | **High** | 🔴 **OBP 4 本すべてに醸造長の署名つき公式コメントがあり、うち 3 本は fiche の完全なテイスティングノートを取得** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **OBP 4 本すべてが公式に実在することを確認し、うち 4 本すべてに公式テクニカルシートがある。**⚠️ **4 行目の色の確定だけは、メニューのセクション見出しと価格が根拠である** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **`C-6`／`C-4`／`V-1`／`V-2` に実測データつきの証拠を追加し、【E】の 4 系統の誤りを公式・公的登録で個別に反証した。番号は 1 つも開いていない** |
| **Staff Notes** | **High** | ⚠️ **14 項目。🔴 「4 行目を白と説明する」「45 区画」「Demeter 認証」「saignée」「全部自社畑」「exclusivement Grand Cru」「246 = ベース年」「Roederer はマロをやらない」「点数」「jetting」「姉妹ドメーヌの混入」という 11 の誤りを塞いだ** |
| 🔴 **総合** | 🔴 **High — staff-usable（70% を大きく超過。実感としては 88% 前後）。** | **OBP 4 本すべてについて、公式の正式名・ベース年／ミレジム・セパージュ・木樽比率・MLF・ドザージュ・産地・造り手のコメントを言える。栽培は認証機関名・認証枠組み・認証面積・engagement 日まで言える。**<br>**欠けているのは ① 分析値（アルコール・デゴルジュマン日・生産量）、② Collection 245 の数値、③ 古いミレジムの fiche。**<br>**いずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。** |

**reached_70: YES（~88%）。**

---

## Open Questions

1. 🔴 ⚠️ **OBP 4 行目（2014・$1,985・`ROSÉ` セクション）が `Cristal Rosé 2014` であることの最終確定。**
   **`Cristal 2014`（白）も `Cristal Rosé 2014` も公式に実在する。**
   **判断根拠はメニューのセクション見出しと価格（$1,985 は BLENDS の 2015 = $1,200 より大きく高い）だけである。**
   → 🔴 **物理ラベル確認タスク: 実ボトルの色とラベル表記（`Cristal Rosé` の刻印の有無）を確認する。**
   → **確認できるまで、staff は色を断定しない。**
2. 🔴 **canonical に `Collection` を登録するかどうか、登録するならどの層に何を持たせるか。**
   **最低でも `release_ordinal = 246` / `base_year = 2021` / `base_year_share = 55%` の 3 値が要る。**
   **Krug（`NV · based on 2017`）と Jacquesson（`MV (Base: 2019)`）が既に 2 つの異なる書式で存在しており、
   `Collection` を足せば 3 つ目になる。**
   → 🔒 **canonical への書き込みは本書では行っていない。設計判断は Akio / CTO。** → §Canonical Conflict `V-1`
3. ⚠️ **`Brut Premier` と `Collection` の関係。**
   **公式サイトは両方のページを現役で持っており、`Collection` を「Brut Premier の後継」と
   明示する文は本調査では見つけられなかった。**
   **「置き換えた」と言ってよいかは公式からは決められない。**
   → **公式プレスリリースまたはメゾンへの照会が要る。**
4. 🔴 **canonical の `house_style`（16 レコードに同一文字列で複製）をどう扱うか。**
   **`Demeter-certified` は 🏛 公的登録で反証済み、`saignée with red wine` は ✅ 公式 fiche で反証済みである。**
   **1 か所の誤りが 16 レコードに複製されている構造そのものが問題である。**
   → 🔒 **本書では変更していない。** → §Canonical Conflict【E】
5. ⚠️ **`/fr/sitemap.xml` の 148 URL がすべてステージングドメイン
   `roederer-site.pp.mzrn.net` を指している（`lastmod 2014`）。**
   **公式ページの全数は本調査では確定していない。**
   → **`/fr/news` の 148 件規模のアーカイブに、追加のミレジム情報や
   `Collection` の位置づけに関する公式記述が埋まっている可能性がある。**
6. ⚠️ **`lr_tech_sheet_collection_245_fr.pdf` のフォント破損。**
   **245（ベース 2020）のセパージュ・MLF・ドザージュが未確定。**
   → **PDF を OCR にかけるか、メゾンに fiche を再請求する必要がある。**
7. ⚠️ **`Cristal 2000` の公式ドザージュ。**
   **canonical は 10 g/L と書いているが、公式サイトに 2000 年の fiche が無いため検証できていない。**
   **否定もできない。**
8. ⚠️ **Cristal の lieux-dits の形成開始年が公式内で 1841 / 1845 と揺れている。**
   **どちらが現行の公式見解かは未確定。**
9. ⚠️ **250 ha の格付け構成。**
   **`exclusivement` Grands et Premiers Crus（`/fr/house`）と
   `essentiellement` Premiers et Grands Crus（`/fr/250ans`）のどちらが正しいか未確定。**
   **プルミエ・クリュとグラン・クリュの内訳ヘクタール数も公式に無い。**
10. ⚠️ **有機認証 135 ha が、Cristal / Cristal Rosé / Collection のどの区画をどこまでカバーするか。**
    **`/fr/cristal2016` は「Cristal は同名ドメーヌから排他的に、有機栽培で」と書いているが、
    Domaine Cristal のヘクタール数は公式に無い。**
    🏛 **Agence Bio に `C1`/`C2`/`C3`（転換 1〜3 年目）が同時に立っており、
    現在も転換中の区画が存在することは分かる。**
11. ⚠️ **ビオディナミ実務の範囲。**
    **公式が名指しするのは「composts biodynamiques」（Cristal のページ）と
    「principes de la biodynamie」（La Maison）だけで、対象面積も期間も書かれていない。**
12. 🔴 ⚠️ **姉妹ドメーヌ（Deutz / Delas / Domaines Ott / Pichon Comtesse / Merry Edwards /
    Diamond Creek / Scharffenberger / Roederer Estate）は本調査の対象外とした。**
    **`louis-roederer.com` にはこれらへの言及が 1 件も無く、本ドシエはグループ構造の裏づけを持たない。**
    **OBP の他の行がこれらに触れるなら、それは `CAT-3`（brand_axis）の案件であって本件ではない。**
