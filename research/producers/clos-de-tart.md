# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にはこの生産者のレコードが 1 件しか無い**（`clos-de-tart-2018`）。
> 本書は昇格前の研究記録であり、**canonical には何も書き込んでいない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト clos-de-tart.com ／ INAO cahier des charges ／ 認証機関の公開登録で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では事実源として使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.clos-de-tart.com/`（FR / EN / CN）**
> 認証の確認元: **Agence Bio 公開登録（opendata API）→ Ecocert France 証明書ページ ／ Biodyvin 公式会員リスト**
> appellation の確認元: 🔴 **INAO extranet の cahier des charges 2 本（`Clos de Tart` と `Morey-Saint-Denis`）**
>
> 🔴 **本ドシエ最大の収穫は 4 点。**
> **① `Clos de Tart` は「Morey-Saint-Denis の中の畑」ではなく、`décret du 4 janvier 1939` で認められた
> 独立した AOC である。** INAO の cahier des charges を実物で取得して確認した。
> **② `La Forge de Tart` が Morey-Saint-Denis Premier Cru を名乗れる法的根拠を、INAO の条文で特定した。**
> **Morey-Saint-Denis の cahier des charges IV 章 2°c) が、Clos de Tart の区画から採れたブドウに
> 「Morey-Saint-Denis premier cru」を、`sans nom du climat d'origine`（climat 名を付けずに）認めている。**
> **したがって `La Forge de Tart` は 1er cru の climat 名ではなく、造り手が付けたキュヴェ名である。**
> **③ 3 つのワインはすべて同じ 7.53 ha の壁の中から採れる。** ただし
> **`Monopole` を名乗るのは `Clos de Tart` Grand Cru だけ**（公式 HTML が `<span class='monopole'>` を
> このワインにのみ付けている）。
> **④ 有機登録が所有権移転に合わせて綺麗に切り替わっている。**
> **Mommessin 期の登録（Bureau Veritas）が `2018-04-16` に `ARRETEE`、
> 同じ `2018-04-16` に新登録（Ecocert France）が `ENGAGEE` になっている。同一 SIRET。**
>
> 🔴 **INAO のファイル名規則について、Batch 8 の 3 形式に加えて 2 つの新形式を確認した。**
> **`PNOCDCClos-de-Tart.pdf`（接頭辞は非ハイフン・名称はハイフン有り・間に区切り無し）**
> **`PNOCDC-MoreySaintDenis.pdf`（接頭辞の後にハイフン・名称は完全非ハイフン）**
> **事前警告どおり、外した推測は HTTP 200 で HTML を返す**（`Le document demandé n'existe pas`）。
>
> ⚠️ **調査上の制約 3 点**
> **① `robots.txt` も `sitemap.php` も `sitemap.xml` も存在しない。**
> **未知の URL はすべて HTTP 200 で 183,062 バイトのソフト 404 を返す**（`404 - La page que vous avez demandée n'existe pas`）。
> **URL 構造はトップページのナビゲーションから抽出するしかなかった。**
> **② 🔴 公式サイトが古い。ワインページの最新ヴィンテージは 3 本とも 2019 で止まっている。**
> **ニュースの最新は 2022 年 7 月 11 日。**
> **OBP に載る 2021 / 2022 / 2023 は、公式サイトでは一件も確認できない。**
> **③ `/fr/revue-de-presse` と `/en/press-review` は HTTP 500 を返す**（本調査時点で公式側の障害）。

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`Clos de Tart`**（`producer_heading` / `producer_or_brand` とも同一） |
| **canonical 表記** | 🔍 **`Clos de Tart`**（`producer` と `name` が**同一文字列**。→ §Canonical Conflict【1】） |
| **公式表記** | ✅ **`Clos de Tart`**（全ページの `<title>` が `… - Clos de Tart`） |
| 🔴 **法人** | ✅ **`Société du Clos de Tart`**（`/fr/mentions`）。**RCS DIJON 686042409** |
| **公的登録** | ✅ **SIRET `68604240900041`**（Agence Bio 公開登録。`raisonSociale` = `SOCIETE DU CLOS DE TART`）。**SIREN 9 桁 `686042409` が mentions légales の RCS と一致** |
| **所在** | ✅ **`7, route des Grands Crus`、21220 Morey-Saint-Denis（Côte-d'Or）** |
| **連絡先** | ✅ **Tel +33 3 80 34 30 91 ／ contact@clos-de-tart.com** |
| 🔴 **現在の所有** | ✅ 🔴 **`Pinault 家` / `Artémis Domaines`。2018 年に取得。**（`/en/history`「**Clos de Tart was acquired by the Pinault family in 2018**」）**家族ドメーヌではない。** |
| **親会社側の記述** | ✅ **`artemis-domaines.com` が相互に記述** —「**1141 年に創設された Clos de Tart は、その長い歴史の中で 4 度しか手を変えておらず、最後は 2018 年、`Groupe Artémis` による取得である。**」 |
| ⚠️ **前所有者** | ✅ **`Mommessin` 家。1932 年〜2018 年。**「**The Mommessin family remained the sole owners until 2018.**」 |
| 🔴 **Artémis Domaines CEO** | ✅ **`Frédéric Engerer`**（`/en/location`） |
| 🔴 **Estate Director** | ✅ **`Alessandro Noli`**（`/en/location` ／ `/en/news/4` ／ `/en/news/5`）。**2019 年が Artémis Domaines と Noli にとって最初の `berry to bottle` ヴィンテージ** |
| **サイト発行責任者** | ✅ 🔴 **`Jean Garandeau`（`j.garandeau@chateau-latour.com`）**（`/fr/mentions`）。**Château Latour のドメインのメールが発行責任者として載っている** |
| **公式サイト** | ✅ **`https://www.clos-de-tart.com/`**（FR / EN / CN。⚠️ **sitemap 無し**） |
| 🔴 **有機認証** | ✅ **Ecocert France（`FR-BIO-01`）。Agence Bio 公開登録で `numeroBio 141317`、状態 `ENGAGEE`、`dateEngagement 2018-04-16`、直近更新 `2025-02-03`。**→ §Farming |
| 🔴 **ビオディナミ認証** | ✅ **`Biodyvin`。公式会員リストに `Clos de Tart / 21220 Morey-Saint-Denis / Bourgogne` として掲載。**公式サイトは「**2016 年にビオディナミの実践を導入、2019 年に Biodyvin 認証**」と記す。→ §Farming |
| **真贋対策** | ✅ **2024 年に `Prooftag` 認証システムを導入**（`/en/authenticity`） |
| canonical id | 🔍 🔴 **`clos-de-tart-2018` の 1 件のみ** |

---

## Overview

✅ **Côte de Nuits、Morey-Saint-Denis 村の中心にある、壁に囲まれた 7.53 ha の一枚地。**
🔴 ✅ **公式の自己規定は明快 —— 「**それは今日、ブルゴーニュで最大のグラン・クリュ・モノポールである
（It is indeed the largest Grand Cru Monopole in Burgundy today）**」。**

🔴 ✅ **公式が繰り返す構造上の事実は「分割されたことが一度も無い」こと。**
「**何百年にもわたる長い歴史にもかかわらず、Clos de Tart は一度も分割も細分化もされたことがない。
ブドウ畑も、熟成と醸造の施設も、常にまったく同じ場所にあった。**」
✅ **「**このドメーヌは歴史上 4 人の所有者しか持たなかった**」**（`/en/spirit`）。

🔴 ✅ **THÉSEUS 的にいちばん重要な事実 —— これは家族ドメーヌではない。**
**1932 年から 2018 年まで Mommessin 家の単独所有だったが、2018 年に Pinault 家 / Artémis Domaines が取得した。**
**Artémis Domaines の CEO は `Frédéric Engerer`、Estate Director は `Alessandro Noli`。**
→ §Staff Notes ⚠️ ①

🔴 ✅ **公式が「3 つのワイン」と明示している。そしてその 3 つはすべて同じ壁の中から採れる。**

| 公式名 | 格 | 公式の説明 |
|---|---|---|
| **Clos de Tart** | ✅ **Grand Cru Monopole** | **「ドメーヌの古木の本質そのものを表現する。その大半は平均でおよそ 60 年生」** |
| **La Forge de Tart** | ✅ **Premier Cru** | **「およそ 20 年生の樹が古木から分けられ、その果実で `La Forge de Tart` という別のワインが造られる。これは Morey-St-Denis Premier Cru に分類される」** |
| **Morey-Saint-Denis** | ✅ **Appellation Village** | 🔴 **「われわれは 2018 年に Morey-Saint-Denis をワインの家族に加えた。ブドウ畑全体で抜かれた古く生産性の落ちた樹を植え替えるために植えた若木の、最良の果実から来る村名ワインである」** |

🔴 ✅ **醸造上の署名は 4 つ。**
**① 選果台で 1 粒ずつ選別**
**② 商業酵母を一切使わない（`We do not use any commercial yeast` / `100% wild yeast`）**
**③ マロラクティックも乳酸菌を接種せず完全に自然**
**④ 区画ごとに木桶で個別醸造 → 収穫翌年 6 月にアッサンブラージュ → 樽で計 18 か月**

🔍 **THÉSEUS における状態は悪い。canonical レコードは `clos-de-tart-2018` の 1 件のみで、
OBP 掲載 5 本のうち 4 本がキュヴェまたはヴィンテージのレベルで未解決。**
🔴 **さらに、既存の 1 件にも公式と食い違う数値と、公式に裏付けの無い人名が入っている。**
→ §Canonical Conflict

---

## History

✅ **公式 `/en/history` は静的取得できた**（JS 描画ではない）。

| 年 | 出来事 ✅ |
|---|---|
| **12 世紀初頭** | 🔴 **この土地は `Climat de la Forge` と呼ばれていた。**「**At the beginning of the Twelfth Century Clos de Tart was called Climat de la Forge.**」→ 🔴 **`La Forge de Tart` の名はここに由来する** |
| 🔴 **1141** | 🔴 ✅ **`Tart 修道院`（Cîteaux 修道院の分院）のシトー会修道女によって創設。**「**フランス革命に至るまでこの修道会に属した。**」 |
| **1141–1789** | ✅ **650 年以上にわたり、`Tart のご婦人方（Tart Ladies）`と呼ばれたシトー会修道女が修道院的な生活様式をもたらした**（`/en/spirit`） |
| 🔴 **1791** | 🔴 ✅ **`Marey-Monge` 家が所有権を取得。** Nuits-Saint-Georges のワイン商 `Claude Marey` が、**植栽済み 18 `journaux`（約 15 acres）**とともに購入。**その後 `Joseph Marey` と `Ferdinand Marey-Monge`（数学者 Monge の娘と結婚）が変革を主導** |
| 🔴 **1855** | 🔴 ✅ **Lavalle 博士の Côte-d'Or 分類で `Tête de Cuvée` に格付け。**「**今日のグラン・クリュ分類よりも制限的な、格式ある区分**」。**Morey-Saint-Denis で唯一この栄誉を受けたドメーヌ** |
| 🔴 **1939 年 1 月 4 日** | 🔴 ✅ **AOC `Clos de Tart` が `décret du 4 janvier 1939` により最初に認められる**（INAO cahier des charges I 章） |
| 🔴 **1932** | 🔴 ✅ **Marey-Monge 家が競売で Mâcon のワイン商 `Henri Mommessin` に売却。**「**当時の経済危機のため、彼は最低競売価格で、唯一の入札者として落札した。**」 |
| **1965 年 7 月 24 日** | ✅ **INAO 全国委員会が `Clos de Tart` の `aire parcellaire` を承認**（INAO cahier des charges IV 章 2°） |
| 🔴 **1996** | ✅ **`Sylvain Pitiot` が運営に着任。**「**土壌と下層土のより精密なマッピング**」と「**新しい醸造設備の導入**」でドメーヌに新しい息吹をもたらした |
| **2006** | ✅ **壁（1.2 km）が修復される** |
| 🔴 **2016** | 🔴 ✅ **ビオディナミの実践を導入**（`/en/location`） |
| 🔴 **2018** | 🔴 ✅ **`Pinault` 家が取得。Mommessin 家は 2018 年まで単独所有者だった。**🔴 **同年、村名ワイン `Morey-Saint-Denis` が初リリース**（2018 ヴィンテージ） |
| 🔴 **2018 年 4 月 16 日** | 🔴 ✅ **有機登録が切り替わる。**Mommessin 名義（Bureau Veritas）が `ARRETEE`、同日 `Société du Clos de Tart` 名義（Ecocert France）が `ENGAGEE`（Agence Bio 公開登録） |
| 🔴 **2019** | 🔴 ✅ **`Biodyvin` 認証。**🔴 **新しい醸造場（cuverie）が 2019 ヴィンテージから稼働。**🔴 **Artémis Domaines と Alessandro Noli にとって最初の `berry to bottle` ヴィンテージ** |
| **2019 年末〜2022** | ✅ **建物の改修が 2019 年末に開始。**2022 年のニュースで「**今年で改修を終えたい —— 事務所、テイスティングルーム、中庭、象徴的な `Salle du Vieux Pressoir` を改修した**」 |
| **2024** | ✅ **`Prooftag` による真贋認証システムを導入**（「**数年の試験を経て**」） |

✅ **歴史上の物件 2 点**（`/en/spirit`）—
**14 世紀の小像 `Tart の聖母`** がドメーヌを見守る。
🔴 **`parrot press`（オウム型プレス）** —「**ロープと滑車の連なりで動かし、1570 年から 1924 年まで毎年使われた。
おそらく現存する唯一の型である。**」

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Bourgogne / Côte de Nuits** ✅ |
| **Commune** | ✅ **Morey-Saint-Denis（Côte-d'Or）** |
| 🔴 **面積** | ✅ 🔴 **7.53 ha、一枚地（`d'un seul tenant`）。**公式サイトと Artémis Domaines の双方が同じ数字 |
| 🔴 **壁** | ✅ 🔴 **空積み石の壁が全周を囲む。全長 1.2 km。2006 年に修復。**「**`Clos` は『壁に囲まれた畑』を意味し、それがドメーヌの名の由来である**」 |
| **形状・寸法** | ✅ **長さ 300 m × 幅 250 m の矩形。斜面の中腹** |
| **標高** | ✅ **269 m 〜 302 m** |
| **向き** | ✅ **区画全体が南東向き** |
| 🔴 **畝の向き** | 🔴 ✅ **北 — 南（斜面の等高線に対して垂直）。**「**Côte-d'Or のブドウ畑の大多数とは逆**」 |
| 🔴 **区画構成** | 🔴 ✅ **12 の `micro climats`。それぞれ個別に収穫される** |
| **土壌** | ✅ **粘土石灰質。複数の異なる石灰岩から成り、それが複数の明確に画定された `micro climats` を生む** |

### 🔴 ✅ 北 — 南植栽についての公式の説明（**このドメーヌ固有の話題**）

「**このように植えることは冬の雨のあいだ土がその場に留まるため、侵食を避ける助けになる。
また、ブドウが朝と午後の陽に両側から当たることを意味し、最適な成熟に達するのがずっと容易になる。
さらに、日射がこう交互になるおかげで、真夏でもブドウは日焼けを起こしにくい。
しかしながら、北から南へ畝を並べることはブルゴーニュの斜面では珍しい光景である。
急な勾配が畑仕事の機械化を非常に困難にするからである。
だからこそ Clos de Tart のほとんどの畑仕事は手で行われる。**」

### ✅ 樹齢と植栽材料

- 🔴 **「平均しておよそ 60 年生で、一部は 100 年を超える（some are centenary）」**
- ✅ **`Pinots Fins` と通称される最良のピノ・ノワール。最高品質の株の選抜による**
- 🔴 **植え替えは `massal selection`（マサル・セレクション）。ドメーヌは自前の苗床（nursery）を持つ**
- 🔴 **「**20 年にわたるマサル・セレクションの実践の結果として、50 の異なるピノ・ノワールの個体のプールを育ててきた。それぞれの樹が固有の美点（芽の稔性、樹勢、樹のバランス…）を持つ**」**（`/en/news/5`, 2022 年 7 月 11 日）

### 🔴 ✅ 3 つのワインの畑上の出どころ（**すべて同じ壁の中**）

| ワイン | 出どころ ✅ |
|---|---|
| **Clos de Tart** Grand Cru | **ドメーヌの古木。平均およそ 60 年生** |
| 🔴 **La Forge de Tart** 1er Cru | 🔴 **「**典型的には Clos de Tart の 25 年未満の樹**」。「**3 つの主要区画がこのワインの生産に入る**」。**2018 年のフィッシュは `Source: 3 plots of 0.68 ha`**、2019 年は `Source: Plantation 2011, Ballonge 2, La Forge` |
| 🔴 **Morey-Saint-Denis** Village | 🔴 **「**ブドウ畑全体で抜かれた古く生産性の落ちた樹を植え替えるために植えられた若木**」。フィッシュは `Source: Youngest vines on the Estate` |

🔴 ⚠️ **したがって「村名の Morey-Saint-Denis は Clos de Tart の外の畑から来る」というのは誤りである。**
**3 本とも同じ 7.53 ha の壁の中から来る。** → §Staff Notes ⚠️ ③

---

## Farming

🔴 ✅ **本ドシエで最も強く裏の取れた節。公式の主張と、認証機関側の登録の双方があり、しかも両者が噛み合っている。**

### 公式サイトの記述（`/en/location`）✅

「**われわれはこの貴重な宝石のようなブドウ畑の現在の管理人としての責任を強く自覚しており、
そのため、ブドウ畑を有機栽培に転換した前任者たちが始めた仕事を続けることに決めた。
Artémis Domaines の CEO である `Frédéric Engerer` と、Estate Director の `Alessandro Noli` は
同じ方向に進み続け、ブドウ畑全体をビオディナミ栽培に転換した。
その狙いは、われわれの類い稀な植物材料が、テロワールと、それを示すために倦まず働く人々への
最大限の敬意のもとに、その潜在能力のすべてを表現できるようにすることである。**」

🔴 ✅ **認証の年についての公式の一文（`/en/location` の `Biodynamics` 見出し）** —
「**2016 年にビオディナミの実践が導入され、2019 年に `Biodyvin` 認証が続いた。**」

### 🔴 認証機関側の記録（**marketing ではなく公的登録**）✅

🔴 **Agence Bio の公開登録には、同一 SIRET `68604240900041` で 2 件のレコードが存在する。**
**そしてその 2 件は、所有権の移転に合わせて同じ日に入れ替わっている。**

| 項目 | 🔴 **現行（Pinault / Artémis 期）** | ⚠️ **旧（Mommessin 期）** |
|---|---|---|
| `numeroBio` | 🔴 **141317** | **128822** |
| `denominationcourante` | 🔴 **`SOCIETE DU CLOS DE TART`** | 🔴 **`CLOS DE TART FAMILLE MOMMESSIN`** |
| `raisonSociale` | **`SOCIETE DU CLOS DE TART`** | **`SOCIETE DU CLOS DE TART`**（同一） |
| SIRET | **68604240900041** | **68604240900041**（同一） |
| 🔴 **認証機関** | 🔴 **`Ecocert France`（`FR-BIO-01`）** | 🔴 **`Bureau Veritas Certification France`（`FR-BIO-10`）** |
| 🔴 **状態** | 🔴 **`ENGAGEE`（有効）。`dateSuspension` / `dateArret` はいずれも null** | 🔴 **`ARRETEE`（終了）** |
| 🔴 **`dateEngagement`** | 🔴 **`2018-04-16`** | **`2015-03-25`** |
| 🔴 **`dateArret`** | **null** | 🔴 **`2018-04-16`** |
| 直近更新 | **`2025-02-03`** | `2023-09-26` |
| 活動 | **Production ＋ Préparation** | **Production ＋ Préparation** |
| 生産区分 | **`Raisin de cuve`（ワイン用ブドウ）／ `Vins de raisin`（ブドウ酒）** | — |

🔴 **旧登録の終了日と新登録の開始日が同じ `2018-04-16` である。**
**所有権の移転にあわせて、有機登録が断絶なく引き継がれたことを示している。**

✅ **Ecocert 証明書ページが実在する**（`certificat.ecocert.com/entreprise/E810A020-…`）—
**`CLOS DE TART` / `7, Route des Grands Crus, 21220 Morey Saint Denis` /
活動 `Agriculteur (production végétale), Fabricant & Transformateur` /
`Certification Agriculture biologique Europe (EU) 2018/848`。**
**住所は mentions légales と完全に一致する。**

### 🔴 ✅ ビオディナミ（**L'Arlot と逆で、ここは本当に認証がある**）

- 🔴 ✅ **`Biodyvin` の公式会員リスト（`biodyvin.com/fr/liste-des-membres-biodyvin.html`）を取得して走査 →
  `Clos de Tart / 21220 / Morey-Saint-Denis / Bourgogne` として掲載されている。**
  **住所が公式サイトの所在と一致する。**
- ⚠️ **`Demeter France` の adhérents サイトマップ（993 件）を走査 → `Tart` は 0 件。**
  **したがって認証は `Biodyvin` であって `Demeter` ではない。** → §Staff Notes ⚠️ ④
- ⚠️ 🔴 **`Biodyvin` 側の資料には認証取得年が載っていない。**
  **「2019 年」は公式サイトの自己申告である。**`Biodyvin` の会員リストは現在の会員である事実しか示さない。
  → Open Questions 4

### ✅ 気候変動への対応（`/en/news/5`、2022 年 7 月 11 日。**Alessandro Noli への聞き取り**）

- 🔴 **「**Clos の中心に 350 メートルの生垣を植えた。そこには十数種の植物（スピノサスモモ、野生の梨、桃、
  フユボダイジュ〔field maple〕、サント・リュシー桜…）が含まれる。同種の他の生垣と樹木が、
  ブドウ畑の他の場所にも既に計画されている。**」**
  公式が挙げる効果は **4 つ** —— **生物多様性（ブドウの益虫の生息地、開花期の延長、鳥類の通過）／
  菌根（mycorrhiza）の発達を促し、リンなどのミネラルをブドウにもたらす／ 日陰／ 景観の多様性**。
  **「ヘーゼルナッツの木はテントウムシのような益虫にとって理想的な生息地」「翌冬にはシジュウカラなどの鳥と
  コウモリのための巣箱を Clos に設置する」。**
- 🔴 **接ぎ木の実験** —「**Clos の 2 つの異なるテロワール —— `La Forge` と `Ballonge 2` —— の
  2 畝で、古い台木に新しい穂木を接ぐ実験を行ってきた。**」**穂木は自前の苗床で育てたもの。**
  **「接ぎ木は植物にとって非常にストレスが大きいので、80% という成功率にはとりわけ満足している。
  そこで 2022 年にはこの計画をこの 2 つの区域の 4 畝に拡大することにした。」**
  ⚠️ **「最初の果実は接ぎ木の 3 年後にしか得られない」と公式が明記している。**
- ✅ **`INRAE`（フランス国立農業・食料・環境研究所）Colmar とのプロジェクトを 2022 年に開始。
  ブドウ畑におけるウイルス、とりわけ `Grapevine Fanleaf Virus`（ブドウ扇葉病）の影響を調べる。**
- ✅ **急勾配のため機械化が困難で、「Clos de Tart のほとんどの畑仕事は手で行われる」。**

### ⚠️ 公式が沈黙していること

⚠️ **収量の方針値、施肥、調合剤（500 / 501 など）の具体、耕耘の方法（馬耕の有無）、
被覆作物、認証の証明書番号は公式サイトに一切記載が無い。**

---

## Winemaking

### 🔴 ✅ 醸造場（cuverie）

✅ **「**ドメーヌは 2019 ヴィンテージのために新しい醸造場を開設した。**」

⚠️ 🔴 **桶の本数について、公式サイト自身の中で数字が食い違っている。**

| 出典 | 記述 |
|---|---|
| ✅ **`/en/location`** | 🔴 「**桶の数を増やしたので（われわれは **7 基のステンレス槽**から、大きさの異なる **14 基の円錐台形の木桶**へ移った）、醸造をいっそう精密にすることが可能になった。**」 |
| ✅ 🔴 **`/en/news/4`（2021 年 4 月 8 日、Noli への聞き取り）** | 🔴 「**20 hL から 40 hL まで大きさの異なる **15 基の新しい木桶**が、**50 hL の古いステンレス槽**に取って代わり、区画ごとの醸造をより精密に行えるようになった。**」 |

→ 🔴 **「14」と「15」が公式の中で並立している。どちらか一方を断定してはならない。** → §Staff Notes ⚠️ ⑥

### ✅ 全体の工程（`/en/location`）

| 工程 | 記述 ✅ |
|---|---|
| 選果 | **「ドメーヌの異なる `micro climats` のブドウは、選果台の上で 1 粒ずつ注意深く選別され、最良のものだけが桶にたどり着く」** |
| 🔴 **全房** | 🔴 **区画によって比率が変わる。**「**茎の質と成熟度によって使う全房の比率は変わる**」 |
| 発酵容器 | **「異なる容量の木桶で個別に醸造される」。各桶が独立した温度管理系統を持つ** |
| 🔴 **酵母** | 🔴 **「われわれは醸造工程で商業酵母を一切使わない。アルコール発酵は 100% 野生酵母によって行われる」** |
| 🔴 **マロラクティック** | 🔴 **「乳酸菌を一切接種しないため、マロラクティック発酵もまた完全に自然である。ヴィンテージの性格によって、この発酵は速く（12 月／1 月ごろに終わる）進むことも、はるかに長くかかる（通常 5 月／6 月ごろに終わる）こともある」** |
| 樽熟成 | **「およそ 18 か月」** |
| 🔴 **アッサンブラージュ** | 🔴 **「最終アッサンブラージュは以前より早く行われるようになった。これは Clos de Tart Grand Cru の最終的な骨格を決める決定的な段階である。一般に、いまは収穫翌年の 6 月に行われる」** |
| 🔴 **熟成の 2 段階** | 🔴 **「最初の 9 か月はロットごとに個別に熟成させ、次の 9 か月はアッサンブラージュしたワインとして熟成させる。これはグラン・クリュにもプルミエ・クリュにも当てはまる」** |

### 🔴 ✅ 全房比率についての公式の記述（**このドメーヌで最も具体的な数字**）

「**大まかに言えば、Clos de Tart の下部の大半の区画では、土壌の石灰質が高いため
全房発酵は 3 分の 1 程度にとどまる。一方、マルヌの比率が高い畑の上半分の大半の区画では
およそ 3 分の 2 になる。**
**各 `micro climat` の面積を勘案すると、平均して `Clos de Tart Grand Cru` にはおよそ 55% の全房を用いる。**
**`La Forge de Tart Premier Cru` を造るときには全房を一切用いない。**」

🔴 ✅ **さらに、2019 年から Bordeaux 大学と共同研究が進行中** —
「**2019 年には Bordeaux 大学との研究も開始し、Clos の新しく画定された各区画における
全房の理想的な比率を determine しようとしている。これは今も継続中である。**」（`/en/news/4`）

### 🔴 ✅ ヴィンテージ別の実データ（**公式ワインページ。OBP 掲載 5 本のうち 2018 のみ該当**）

| ワイン / VT | 収穫 | 収量 | ABV | 全房 | 熟成 | 瓶詰め |
|---|---|---|---|---|---|---|
| 🔴 **Clos de Tart 2019** | **9/13–9/19** | 🔴 **30 hL/ha** | **14%** | 🔴 **60%** | 🔴 **18 か月、新樽 70%** | **2021/03/26** |
| 🔴 **Clos de Tart 2018** ⭐OBP | **8/30–9/3** | 🔴 **32 hL/ha** | **14.1%**（pH 3.62） | ⚠️ **記載なし** | 🔴 **18 か月、新樽 80%** | **2020 年 5 月** |
| **Clos de Tart 2017** | **9/6–9/10** | **32 hL/ha** | **13.5%**（pH 3.7） | ⚠️ **記載なし** | **樽 19 か月 ＋ タンク 1 か月** | **2019 年 5 月** |
| **Clos de Tart 2016** | **9/28–10/3** | **35 hL/ha** | **13.5%**（pH 3.7） | ⚠️ **記載なし** | **17 か月** | **2018 年 4 月** |
| 🔴 **La Forge de Tart 2019** | **9/13–9/19** | ⚠️ **記載なし** | **14%** | 🔴 **15%** | 🔴 **新樽 50%** | **2021/03/17** |
| 🔴 **La Forge de Tart 2018** | **8/30–9/3** | ⚠️ **記載なし** | **14.1%** | 🔴 **100% 除梗** | 🔴 **新樽 50%** | **2020 年 4 月** |
| 🔴 **Morey-Saint-Denis 2019** | **9/13–9/19** | ⚠️ **記載なし** | **13.5%** | 🔴 **100% 除梗** | 🔴 **18 か月、新樽 0%** | **2021/01/21** |
| 🔴 **Morey-Saint-Denis 2018** | **8/30–9/3** | ⚠️ **記載なし** | **13.5%** | 🔴 **100% 除梗** | 🔴 **新樽 0%** | **2020/01/27** |

⚠️ 🔴 **`La Forge de Tart 2019` は全房 15% とある。**
**しかし `/en/location` の総論は「La Forge de Tart には全房を一切用いない」と書いている。**
**2018 年は `100% destemmed`（＝全房 0）で総論と整合するが、2019 年は整合しない。**
→ 🔴 **総論の「0%」を年をまたいで断定してはならない。** → §Staff Notes ⚠️ ⑦

🔴 ✅ **新樽比率が下がっている。**2018 = 80% → 2019 = 70%（Clos de Tart）。
**公式の 2021 年インタビューも「**熟成における新樽の使用も減った（The use of new oak in the ageing process has also decreased）**」と明記している。**

⚠️ 🔴 **生産本数は 3 本のどのページにも記載が無い。**

---

## Style

### 🔴 ✅ 公式テイスティングノート

| ワイン / VT | ノート ✅ |
|---|---|
| 🔴 **Clos de Tart 2019** | 「**魅惑的な深紅の衣。素晴らしく複雑な香りは、野イチゴやローガンベリーといったフレッシュな赤い果実、さらにカシスとプラムのより暗い果実の風味を見せ、土と香辛料の調子、そして繊細な花の香りを伴う。口中でこのワインはその血統を示し、絶妙な均衡と精確さを発揮する。**」 |
| 🔴 **Clos de Tart 2018** ⭐OBP | 🔴 「**美しく深い色。寛大な赤いベリー、煮たプラム、チェリーの複雑な香りに、空気に触れるといくらか黒い果実、そして薔薇とスミレの花の調子が加わる。口中では温暖なヴィンテージ由来であることを示し、力強く、強度があり、肉感的でありながら、柔らかく絹のようなタンニンとともに信じがたいほど優雅であり続ける。**」 |
| **Clos de Tart 2017** | 「**凝縮した年の特徴をすべて示す 2016 年と比べ、2017 年の特質は優雅さと清涼感である。美しい深みと、果実的（空気に触れるとブラックベリーの気配をより見せる赤い果実）かつ花的（とりわけスミレと薔薇）な複雑な芳香のスペクトルを持つ。Clos de Tart の最良の年に特徴的な、極めて精確な骨格を伴う。**」 |
| **Clos de Tart 2016** | 「**深いルビー色の衣。極めて複雑な香りが広い芳香の幅を持つ —— 果実（野イチゴ）が花の気配（薔薇、ライラック）、香辛料（胡椒）、タバコとハーブティーのニュアンスと混じり合う。密で、豊かで、フルボディでありながら軽やかな口当たり。肉付きがよく絹のようなタンニンが口中を軽く覆い、長く愛撫するような余韻に至る。力強く、優雅で、美味で、蠱惑的なワイン。**」 |
| 🔴 **La Forge de Tart 2019** | 「**この紫の色合いを帯びた Forge de Tart は、香りに愛らしいフレッシュな赤い果実を、香辛料と花の調子とともに現す。深い味わいと見事な均衡を示す美味な口当たり。柔らかいタンニン、繊細な酸、そして長く精確な余韻。**」 |
| 🔴 **La Forge de Tart 2018** | 「**この Forge de Tart は香りに大きな凝縮感を示し、豊かな黒い果実（プラム、カシス、ブラックチェリー）、香辛料、そして滋味のある黒オリーヴの調子を見せる。滑らかでビロードのようなタンニンとともに見事な均衡を示し、長く尾を引くエネルギッシュな余韻。**」 |
| 🔴 **Morey-Saint-Denis 2019** | 🔴 「**深い紫の色。この村名ワインは、赤いベリー、ダークチェリー、カシスの葉の果実的なブケに、アニスの気配を伴う。口中は滑らかで優雅、優れた果実の凝縮感を示す。**」 |
| 🔴 **Morey-Saint-Denis 2018** | 🔴 「**深い紫の色。この村名ワインは、みずみずしいラズベリーとイチゴの果実のブケに、香辛料の気配と繊細な花の香りを伴う。口中には良い張りと強い風味。**」 |

### ⚠️ 第三者評価について

⚠️ 🔴 **公式サイトの `/en/signature` には第三者の評言が 2 つ掲げられている**
（`Guide Vert 2019` の 3 つ星昇格、`Neal Martin, The Wine Advocate, 29/12/17`）。
🔴 **本ドシエはこれらを事実源として使用しない。**
**公式が掲出している事実だけを記録する。** → §Staff Notes ⚠️ ⑨

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake、`beverage_menu_bottles.doc` 803–807 行。**全 5 本、`FRANCE | RED > BURGUNDY`、p.12、`producer_state = exact`**）

| # | OBP 印字 | VT | 価格 | ✅ **公式での確認結果** | 🔍 canonical / matcher |
|---|---|---|---|---|---|
| 1 | 🔴 **`Morey-Saint-Denis`**（キュヴェ名なし） | **2023** | **$600** | 🔴 ✅ **実在するキュヴェである。公式名はまさに `Morey-Saint-Denis`、格は `Appellation Village`。2018 ヴィンテージから生産。**⚠️ 🔴 **ただし公式の一覧は `2019 / 2018` のみで、2023 は確認できない**（サイトが古い） | 🔴 **canonical に無し。**matcher は**独自 shell** `rs:pro:197951b8afe2e608` を作成し、**生産者レベルのみ** `producer:clos-de-tart` に接続 |
| 2 | **`'La Forge de Tart,' Morey-Saint-Denis Premier Cru`** | **2022** | **$1,040** | ✅ 🔴 **キュヴェ名も格も公式と一致。**⚠️ **公式の一覧は `2019 2018 2017 2016 2014 2011 2008 2007 2006` で、2022 は確認できない** | 🔴 **`review_item`。**fuzzy 候補 `cuvee:clos-de-tart-clos-de-tart`（score **0.7143**） |
| 3 | **`'La Forge de Tart,' Morey-Saint-Denis Premier Cru`** | **2021** | **$1,020** | ✅ **同上。**⚠️ **2021 も公式一覧に無い** | 🔴 **`review_item`。**同じ候補・同じ score |
| 4 | **`Clos de Tart Grand Cru`** | **2022** | **$3,720** | ✅ **キュヴェは実在。**⚠️ 🔴 **公式一覧の最新は 2019。2022 は確認できない** | 🔴 **shell `rs:pro:8b62b9cf17ab172d`。**⚠️ **2018 行と同じ shell に集約されている** |
| 5 | **`Clos de Tart Grand Cru`** | **2018** | **$3,260** | ✅ 🔴 **完全に裏が取れた唯一の行。**公式の 2018 ページに **収量 32 hL/ha・ABV 14.1%・pH 3.62・18 か月／新樽 80%・2020 年 5 月瓶詰め・公式テイスティングノート**がある | 🔍 ✅ **canonical `clos-de-tart-2018` に対応。**⚠️ **ただし canonical の熟成値が公式と食い違う（→ §Canonical Conflict【3】）**。matcher は 2022 行と同一 shell |

🔴 ⚠️ **5 本のうち、公式サイトでヴィンテージの実在まで確認できたのは 2018 の 1 本だけである。**
**残り 4 本（2021 / 2022 ×2 / 2023）は「キュヴェは実在するが、その年は公式サイトに無い」状態。**
**原因は公式サイトが 2019 ヴィンテージ以降更新されていないことであり、
「その年は造られていない」という意味ではない。** → §Staff Notes ⚠️ ⑧

### ✅ 公式の全 3 ワインと、公式が掲げるヴィンテージ一覧

| # | 公式名 | 格（公式 HTML の `vin_class`） | 🔴 **`monopole` タグ** | 公式一覧のヴィンテージ |
|---|---|---|---|---|
| 1 | 🔴 **Clos de Tart** ⭐OBP×2 | **Grand Cru** | 🔴 **○ あり** | **2019 2018 2017 2016 2015 2014 2013 2012 2011 2010 2009 2008 2007 2006 2005 2004 2003 2002 2001 2000 1999 1996** |
| 2 | 🔴 **La Forge de Tart** ⭐OBP×2 | **Premier Cru** | 🔴 **✕ なし** | ⚠️ 🔴 **2019 2018 2017 2016 2014 2011 2008 2007 2006**（**毎年造られていない**） |
| 3 | 🔴 **Morey-Saint-Denis** ⭐OBP | **Appellation Village** | 🔴 **✕ なし** | 🔴 **2019 2018 のみ**（**2018 が初ヴィンテージ**） |

🔴 **公式 HTML は `<h1>` の中で `<span class='monopole'>Monopole</span>` を
`Clos de Tart` にのみ付けている。`La Forge de Tart` と `Morey-Saint-Denis` には付けていない。**
**FR 版・EN 版の双方で同じ。**

🔴 ⚠️ **`Clos de Tart` の公式一覧に `1998` と `1997` が無い。**
**公式は理由を書いていない。** → Open Questions 6

### 🔴 ✅ 3 つのワインの appellation 上の関係（**INAO の条文で確定**）

| ワイン | AOC | 🔴 根拠 |
|---|---|---|
| 🔴 **Clos de Tart** | 🔴 **AOC `Clos de Tart`（独立した AOC）** | ✅ **`décret du 4 janvier 1939` により最初に認められた。**cahier des charges I 章。**III 章「AOC `Clos de Tart` は赤の静止ワインに限る」** |
| 🔴 **La Forge de Tart** | 🔴 **AOC `Morey-Saint-Denis` ＋ `premier cru` の表示（climat 名なし）** | 🔴 ✅ **Morey-Saint-Denis の cahier des charges IV 章 2°c)** |
| **Morey-Saint-Denis** | **AOC `Morey-Saint-Denis`（村名）** | ⚠️ **条文上の経路は本調査で特定できていない**（下記） |

🔴 ✅ **決定的な条文（Morey-Saint-Denis の cahier des charges、IV 章 2°c)。原文の訳）** —

「**AOC `Clos de la Roche`、`Clos Saint-Denis`、`Bonnes-Mares`、`Clos des Lambrays` および `Clos de Tart` の
画定区画内にあるブドウ樹から生じたワインは、`premier cru` の表示を付した AOC `Morey-Saint-Denis` を、
**`sans nom du climat d'origine`（由来する climat の名を付けずに）**、
名乗ることもできる。**」

🔴 **したがって —— `La Forge de Tart` は 1er cru の climat 名ではない。**
**INAO が認めている表示は「Morey-Saint-Denis premier cru」までであり、climat 名を付けることは
この経路では明示的に認められていない。**
**`La Forge de Tart` は造り手が付けたキュヴェ名（ブランド名）であり、
`La Forge` はドメーヌ内部の区画名である**（12 世紀の旧称 `Climat de la Forge` に由来し、
2022 年のニュースでも `La Forge` と `Ballonge 2` が Clos 内の 2 つのテロワールとして名指しされている）。

✅ **参考: Morey-Saint-Denis の 1er cru 公式 climat 一覧（cahier des charges の表。20 climat）** —
**Les Genavrières / Monts Luisants / Les Chaffots / Clos Baulet / Les Blanchards / Les Gruenchers /
La Riotte / Les Millandes / Les Faconnières / Les Charrières / Clos des Ormes / Aux Charmes /
Aux Cheseaux / Les Chenevery / Le Village / Les Sorbès / Clos Sorbè / La Bussière / Les Ruchots / Côte Rotie。**
🔴 **`La Forge` はこの一覧に無い。**

⚠️ 🔴 **村名の `Morey-Saint-Denis` については、条文上の経路を本書では確定できなかった。**
**IV 章 2°c) は `premier cru` の経路しか定めておらず、村名についての明文が無い。**
**Clos de Tart の cahier des charges には `déclaration de repli`（より一般的な appellation への引き下げ）の
手続き規定はあるが、引き下げ先の appellation 名は書かれていない。**
**また Clos de Tart の cahier des charges VIII 章 4° は、若木は植栽の翌々年からしか AOC を名乗れないと定める。**
→ **推測で埋めない。** → Open Questions 3

✅ **AOC `Clos de Tart` の主な生産条件（cahier des charges）** —
**主要品種 `pinot noir N`／補助品種 `chardonnay B, pinot blanc B, pinot gris G`／
収量 `35 hL/ha`、butoir `49 hL/ha`／最低自然アルコール `11.5%`／
補糖後の総アルコールは `14.5%` を超えない／
栽培・醸造・熟成はすべて Morey-Saint-Denis 村の territory で行う。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① ブルゴーニュ最大のグラン・クリュ・モノポール。7.53 ha の壁の中。900 年で所有者は 4 人だけ。
2018 年からピノー家（Artémis Domaines）の所有です。**
「**モレ・サン・ドニ村の、壁にぐるりと囲まれた 7.53 ヘクタールの一枚地です。
造り手自身が『**今日ブルゴーニュで最大のグラン・クリュ・モノポール**』と書いています。
壁は空積みの石で全長 1.2 キロ、2006 年に修復されました。**
**1141 年にタール修道院のシトー会修道女が創設して以来、一度も分割されたことがなく、
所有者は 900 年で 4 人だけ —— 修道女、マレー・モンジュ家（1791 年〜）、モメサン家（1932 年〜）、
そして 2018 年からピノー家です。**
**現在は Artémis Domaines の傘下で、CEO はフレデリック・エンジェレール、
現地の責任者はアレッサンドロ・ノリ。2019 年が、この体制で最初の『ブドウから瓶まで』のヴィンテージでした。**」

**② リストの 3 本は、値段が 6 倍違っても、すべて同じ壁の中から採れています。違うのは樹齢です。**
「**このリストにある 3 種類は、別々の畑ではありません。すべて同じ 7.53 ヘクタールの中です。**
**分けているのは樹齢です —— **
**`クロ・ド・タール` グラン・クリュは平均 60 年生の古木、中には樹齢 100 年を超えるものもあります。**
**`ラ・フォルジュ・ド・タール` は 25 年未満の若い樹で、造り手は『3 区画、0.68 ヘクタール』と書いています。**
**そして 600 ドルの村名 `モレ・サン・ドニ` は、抜いた古木を植え替えた最も若い樹から。2018 年が最初の年です。**
**『クロ・ド・タールとまったく同じ手間をかけて造るが、より早く飲む楽しみを与えてくれる』
と造り手自身が説明しています。**」

**③ 醸造は商業酵母を一切使わず、区画ごとに木桶で。全房比率が畑の上下で違います。**
「**12 の『ミクロ・クリマ』に分けて別々に収穫し、選果台で 1 粒ずつ選びます。**
**商業酵母は一切使わず、アルコール発酵は 100% 野生酵母。マロラクティックも乳酸菌を接種しません。**
**全房の比率が面白くて、**石灰質の多い畑の下部では約 3 分の 1、マルヌの多い上部では約 3 分の 2**。
**面積で均すと `クロ・ド・タール` は平均でおよそ 55% です。**
**2019 年から新しい醸造場が稼働し、大型のステンレス槽から、20〜40 ヘクトリットルの
小さな円錐台形の木桶に替えて、区画ごとに仕込めるようになりました。**
**樽熟成は 18 か月。前半 9 か月はロットごと、収穫翌年の 6 月にアッサンブラージュして、後半 9 か月です。**」

### 追加で使える一手

- **栽培（ここは強い）**: 「**有機とビオディナミの両方です。**
  **有機は Ecocert フランスで、Agence Bio の公開登録にも載っています。**
  **ビオディナミは 2016 年に実践を始めて、2019 年に `Biodyvin` の認証を取得。**
  **Biodyvin の会員リストにも載っています。**
  **畝が北 — 南向きなのがこの畑の特徴で、これはブルゴーニュの斜面では珍しい。
  造り手は『冬の雨での土の流出を防ぎ、ブドウが朝と午後の陽を両側から受けられる』と説明しています。
  ただし勾配が急で機械が入りにくいので、畑仕事のほとんどは手作業です。**」
- **気候変動への取り組み**: 「**クロの中心に 350 メートルの生垣を植えています。
  スピノサスモモ、野生の梨、桃、サント・リュシー桜など十数種。
  益虫の住処になり、菌根の発達を促し、日陰も作る。翌年には鳥とコウモリの巣箱も設置すると。**
  **さらに、20 年のマサル・セレクションで選び抜いた 50 本のピノ・ノワールの個体を自前の苗床で育て、
  古い台木に接ぎ木する実験を進めています。成功率 80% だったそうです。**」
- **Clos de Tart 2018（$3,260）**: 「**収穫は 8 月 30 日から 9 月 3 日、収量 32 ヘクトリットル、
  アルコール 14.1%。18 か月の樽熟成で新樽は 80%、2020 年 5 月の瓶詰めです。**
  **造り手のノートは『美しく深い色、寛大な赤いベリー、煮たプラム、チェリー。
  温暖なヴィンテージ由来で力強く肉感的だが、柔らかく絹のようなタンニンとともに信じがたいほど優雅』。**」
- **歴史の小話**: 「**12 世紀の初め、この土地は `Climat de la Forge` と呼ばれていました。
  リストにある『ラ・フォルジュ・ド・タール』の名前はここから来ています。**
  **1855 年のラヴァル博士の分類では `Tête de Cuvée` —— 今のグラン・クリュより厳しい格付けで、
  モレ・サン・ドニでこれを受けたのはここだけでした。**
  **1570 年から 1924 年まで毎年使われた『オウム型プレス』が今も残っていて、
  造り手は『おそらく現存する唯一の型』と書いています。**」
- **真贋**: 「**2024 年から `Prooftag` という認証システムを導入していて、
  ボトルの参照番号から真贋と詳細情報を確認できます。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／誤りやすい**）

1. 🔴 ⚠️ **「モメサン家のドメーヌ」と言わない。**
   **2018 年に Pinault 家 / Artémis Domaines が取得している。**
   **公式の history が「The Mommessin family remained the sole owners until 2018」と明記。**
   ⚠️ **同時に「ケリング」「ピノー・プランタン」とも言わない。**
   **公式が書いているのは `Pinault family` と `Artémis Domaines`／`Groupe Artémis` であって、
   小売コングロマリットの名前ではない。**
2. 🔴 ⚠️ **`Clos de Tart` を「モレ・サン・ドニの中のグラン・クリュ畑」と言わない。**
   **`Clos de Tart` は `décret du 4 janvier 1939` で認められた独立した AOC である。**
   **INAO の cahier des charges が別立てで存在する。**
3. 🔴 ⚠️ **600 ドルの村名 `モレ・サン・ドニ` を「クロの外の畑」と言わない。**
   **公式は「ブドウ畑全体で抜かれた古く生産性の落ちた樹を植え替えるために植えた若木から」と書いており、
   フィッシュの `Source` は `Youngest vines on the Estate` である。**
   **3 本とも同じ壁の中から来る。**
4. 🔴 ⚠️ **「ドゥメテール（Demeter）認証」と言わない。**
   **認証は `Biodyvin` である。**`Demeter France` の adhérents 993 件を走査して 0 件を確認した。
5. 🔴 ⚠️ **`La Forge de Tart` を「1er cru の畑（climat）の名前」と言わない。**
   **Morey-Saint-Denis の 1er cru 公式 climat 一覧 20 件に `La Forge` は無い。**
   **INAO は Clos de Tart の区画から採れたブドウに
   「Morey-Saint-Denis premier cru」を `climat 名を付けずに` 名乗ることを認めているだけである。**
   **`La Forge de Tart` は造り手のキュヴェ名。**
6. 🔴 ⚠️ **木桶の本数を断定しない。**
   **公式サイト自身が `/en/location` で「7 基のステンレス → 14 基の木桶」、
   `/en/news/4` で「50 hL のステンレスを 15 基の新しい木桶（20–40 hL）が置き換えた」と書いている。**
   言うなら「**20 から 40 ヘクトリットルの小さな木桶に替えた**」まで。
7. 🔴 ⚠️ **「ラ・フォルジュは全房を使わない」と年をまたいで断定しない。**
   **総論はそう書いているが、`La Forge de Tart 2019` のフィッシュは `% Whole Bunch: 15%` である。**
   **2018 年は `100% destemmed` で総論と整合する。年ごとに違う。**
8. 🔴 ⚠️ **リストの 2021 / 2022 / 2023 について「公式で確認しました」と言わない。**
   **公式サイトのワインページは 3 本とも 2019 ヴィンテージで止まっている。**
   **確認できたのは `Clos de Tart 2018` だけである。**
   ⚠️ **同時に「その年は造っていない」とも言わない** —— サイトが古いだけの可能性が高い。
9. ⚠️ **第三者の点数・評言を復唱しない。**
   **公式が `/en/signature` に 2 件掲げているが、本ドシエは事実源として採用していない。**
   🔴 **canonical にある `points: 96` も出典不明である。**
10. 🔴 ⚠️ **醸造長・栽培長の名前を canonical から引かない。**
    **canonical の `description_en` にある 2 つの人名は、公式サイトのどこにも出てこない。**
    **公式が名指ししているのは `Frédéric Engerer`（Artémis Domaines CEO）と
    `Alessandro Noli`（Estate Director）、および歴史上の `Sylvain Pitiot`（1996 年着任）だけである。**
11. 🔴 ⚠️ **`Clos de Tart 2018` の新樽比率を「50%」と言わない。**
    **公式は `18 months, 80% new oak` と書いている。**
    **canonical の `18 months barrel (new oak 50%)` は公式と食い違う。**
12. ⚠️ **生産本数・希少性の数字を言わない。** **公式に一切記載が無い。**
13. ⚠️ **収量の方針値を語らない。**
    **公式サイトに方針としての収量の記述は無い。**
    **年ごとの実測（2019 = 30、2018 = 32、2017 = 32、2016 = 35 hL/ha）と、
    INAO の上限（35 hL/ha、butoir 49 hL/ha）は別物である。**
14. ⚠️ **`Clos de Tart` の 1997 / 1998 について「造られなかった」と言わない。**
    **公式一覧に無いというだけで、公式は理由を書いていない。**
15. ⚠️ **Sylvain Pitiot 時代の逸話を語らない。**
    **公式が書いているのは「1996 年に着任し、土壌のより精密なマッピングと新しい醸造設備で
    新しい息吹をもたらした」の一文だけである。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **実在する衝突が 4 件。**
🔴 **うち【1】は既存のどの族にも当てはまらない新しい形である。**
**指示どおり番号は開かない。形だけを記述し、採番は CTO に委ねる。**

---

### 【1】🔴 **新しい形 —— 生産者名とキュヴェ名が同一文字列であることによる照合の汚染**

1. **衝突する canonical ID**: `clos-de-tart-2018`
   **関係する OBP 行**: 803 / 804 / 805 / 806 / 807（**全 5 行**）
2. **なぜ問題か**:
   🔴 **canonical の当該レコードは `producer` と `name` がともに `Clos de Tart` である。**
   **その結果、matcher が導出したキュヴェ実体 ID は `cuvee:clos-de-tart-clos-de-tart` となっている**
   （🔍 `research/out/t-01/review.json` に実値で存在）。
   **生産者スラッグとキュヴェスラッグが同一であるため、
   「生産者名に由来するトークン」と「キュヴェを識別するトークン」が区別できない。**

   🔴 **実害が 2 つの形で観測されている。**

   **(i) 生産者名トークンによる fuzzy スコアの押し上げ。**
   **OBP 804 / 805 行の `La Forge de Tart`（$1,040 / $1,020、Premier Cru）に対し、
   matcher は `Clos de Tart`（Grand Cru、$3,260–$3,720）を
   `score 0.7143` / `why: "fuzzy within producer"` で唯一の候補として提示している。**
   **一致しているトークンは `de` と `Tart` —— どちらも生産者名の構成要素であり、
   キュヴェを識別する力を持たない。**
   ⚠️ **現状は `review_item` に落ちており自動確定はされていない。**
   **しかし自動確定の閾値が 0.71 以下であれば、
   Premier Cru が Grand Cru に自動一致していた。潜在的な事故である。**

   **(ii) キュヴェ名が空の行の扱い。**
   **OBP 803 行（村名 `Morey-Saint-Denis`、$600）は `product_name` が空文字列で、
   識別情報は `classification_text = "Morey-Saint-Denis"` にしかない。**
   🔴 **そしてこの文字列は canonical の `subregion` の値と同一である。**
   **すなわち「キュヴェ名 = 生産者名」の衝突に加えて、
   「キュヴェ名 = subregion 名」という二つ目の同名衝突がこの生産者には存在する。**

3. **証拠**:
   🔍 `migration/out/export/db_wine_canonical.json` — `"producer": "Clos de Tart"`, `"name": "Clos de Tart"`。
   🔍 `research/out/t-01/review.json` 803–807 行分 —
   `{"entity_id": "cuvee:clos-de-tart-clos-de-tart", "name": "Clos de Tart", "score": 0.7143, "why": "fuzzy within producer"}`。
   ✅ 公式サイトが 3 つの別々のワインを持つことは `/en/wines` と 3 つのワインページで確認済み。
4. **OBP への影響**:
   🔴 **金額ベースで $9,640 のうち、canonical に正しく紐づいているのは $3,260（33.8%）だけ。**
   **$600 の村名ワインと $2,060 の 1er Cru（2 本）は、
   生産者名と同綴りの Grand Cru キュヴェに引き寄せられる圧力を受け続ける。**
5. **推奨対応（DO NOT EXECUTE）**:
   **(a) fuzzy 照合の前に、キュヴェ候補文字列から生産者名トークンを除去する
   （`La Forge de Tart` vs `Clos de Tart` は、`Tart` を落とせば `La Forge` vs `Clos` となり一致しない）。**
   **(b) 生産者名と完全一致するキュヴェには「同名フラグ」を立て、
   fuzzy 経路での自動確定を禁止して常に人間裁定へ回す。**
   **(c) `classification_text` が canonical の `subregion` と一致する行を、
   キュヴェ照合の入力に使わない。**
   ⚠️ **これらはすべて matcher の設計変更であり、本書では実行していない。**
6. **Confidence**: 🔴 **High**（`score 0.7143` と `entity_id` は実データを読んで確認した）。

⚠️ 🔴 **なお、本タスクの前提には修正が要る。**
**「OBP 行 1（村名 Morey-Saint-Denis）が Grand Cru キュヴェ `Clos de Tart` に `exact` で一致している」
という記述は、本調査で読んだ成果物では裏付けられなかった。**
🔍 **`mapping.json` の 803 行のエントリは
`{"resolved_to": "research_shell", "shell_id": "rs:pro:197951b8afe2e608", "canonical": {"producer": "producer:clos-de-tart"}}`
であり、canonical への接続は生産者レベルのみ、キュヴェは付与されていない。
しかも 806 / 807 行とは別の shell が与えられている。**
**`exact` は `producer_state`（生産者名の一致）を指しており、それ自体は正しい。**
**ただし上記のとおり、同名衝突という欠陥そのものは実在し、
804 / 805 行の fuzzy 候補という形で現に観測できる。**

---

### 【2】🔴 **appellation の平板化 —— 独立した AOC が村名に潰されている**

1. **衝突する canonical ID**: `clos-de-tart-2018`
2. **なぜ問題か**:
   🔍 **`subregion` の値が `Morey-Saint-Denis` である。**
   ✅ 🔴 **しかし `Clos de Tart` は `décret du 4 janvier 1939` で認められた独立した AOC であり、
   INAO は Morey-Saint-Denis とは別の cahier des charges を持つ。**
   🔍 **`classification` フィールドには `Clos de Tart Grand Cru (Monopole)` と正しく入っているため、
   同一レコード内で appellation の情報が 2 つのフィールドに分裂し、
   `subregion` 側だけが誤っている状態にある。**
   🔴 **Batch 8 の Coulée de Serrant（モノポールのグラン・クリュが自身の AOC を村名に潰された）と同型。**
3. **証拠**:
   ✅ `extranet.inao.gouv.fr/fichier/PNOCDCClos-de-Tart.pdf` I 章 —
   「**Seuls peuvent prétendre à l'appellation d'origine contrôlée « Clos de Tart » initialement reconnue par le décret du 4 janvier 1939…**」
   ✅ `extranet.inao.gouv.fr/fichier/PNOCDC-MoreySaintDenis.pdf` I 章 —
   Morey-Saint-Denis は `décret du 8 décembre 1936` による別の AOC。
   **同 IV 章 2°c) が両者を明確に別物として扱っている。**
4. **OBP への影響**:
   🔴 **`subregion` で検索・集計すると、独立 AOC のグラン・クリュが村名ワインと同じ箱に入る。**
   **本件ではまさにその箱に $600 の村名ワインと $3,260 のグラン・クリュが同居する。**
   **`La Forge de Tart`（真に Morey-Saint-Denis 1er Cru）だけが正しく村名に属する。**
5. **推奨対応（DO NOT EXECUTE）**:
   **`appellation` を `subregion` から分離し、`AOC Clos de Tart` を正とする。**
   **`Morey-Saint-Denis` は commune（村）として別フィールドに持つ。**
   🔴 **Coulée de Serrant と同じ族として一括で扱うのが整合的。番号は CTO 判断。**
6. **Confidence**: 🔴 **High**（INAO の一次資料を実物で取得した）。

---

### 【3】🔴 **既存レコードの内容が公式と食い違う／公式に裏付けが無い**

1. **衝突する canonical ID**: `clos-de-tart-2018`
2. **なぜ問題か**: **4 点。**

   | フィールド | 🔍 canonical の値 | ✅ 公式の値 | 判定 |
   |---|---|---|---|
   | 🔴 `aging` | **`18 months barrel (new oak 50%)`** | 🔴 **`18 months, 80% new oak`**（2018 ページ） | 🔴 **数値の誤り** |
   | `terroir` | **`7.5ha`** | **`7.53 ha`**（公式サイトと Artémis Domaines の双方） | **精度の誤り** |
   | 🔴 `description_en` | 🔴 **`Since winemaker Jacques-Luc Aegerter and then Perrine Fenal (under the Pinault era)`** | 🔴 **公式サイトのどこにも出てこない人名。**公式が名指しするのは `Frédéric Engerer`（Artémis Domaines CEO）と `Alessandro Noli`（Estate Director） | 🔴 **裏付け無し** |
   | 🔴 `description` | 🔴 **`ピノー・プランタン財閥（フランソワ・ピノー）が所有`** | 🔴 **公式は `Pinault family` / `Artémis Domaines`、親会社側は `Groupe Artémis`** | 🔴 **主体の誤り**（小売コングロマリットと混同） |
   | `points` | **`96`** | ⚠️ **公式に記載が無い** | ⚠️ **出典不明** |

   🔴 **`description_en` の人名は `P-8`（裏付けの無い `founded_year`）と同種の
   「一次資料に存在しない属性が canonical に入っている」問題だが、対象が年ではなく人名である。**
   **既存族に入れるか新設かは CTO 判断。番号は開かない。**
3. **証拠**: 上表のとおり。✅ `/en/wines/1/clos-de-tart/2018`、`/en/location`、`artemis-domaines.com`。
4. **OBP への影響**:
   🔴 **`clos-de-tart-2018` は OBP 807 行（$3,260）に対応する唯一の完全一致レコードである。**
   **すなわち、5 本のうち最も信頼されるべき 1 本の記述に、
   数値の誤りと出典不明の人名が同居している。**
   **ソムリエがこのレコードをそのまま読み上げると、少なくとも 2 つの虚偽を述べることになる。**
5. **推奨対応（DO NOT EXECUTE）**:
   **`aging` を `18 months, 80% new oak` に、`terroir` の面積を `7.53 ha` に訂正。**
   **`description` / `description_en` から裏付けの無い人名と `ピノー・プランタン` を削除し、
   本書 §Identity / §History の公式記述で置き換える。**
   **`points` は出典を明示できないなら削除。**
   ⚠️ **canonical は READ-ONLY。本書では実行していない。**
6. **Confidence**: 🔴 **High**（canonical の実値と公式ページを突き合わせた）。

---

### 【4】⚠️ **shell が異なるヴィンテージを 1 つに集約している**

1. **関係する ID**: 🔍 shell `rs:pro:8b62b9cf17ab172d`（OBP 806 行と 807 行）
2. **なぜ問題か**:
   🔍 `duplicates.json` —
   `{"shell_id": "rs:pro:8b62b9cf17ab172d", "level": "product", "identity_basis": "source_exact", "appearances": 2, "lines": ["2022\t\tClos de Tart Grand Cru\t\t\t\t\t\t3720", "2018\t\tClos de Tart Grand Cru\t\t\t\t\t\t3260"], "reason": "printed identity (と必要なら section) が一致したため 1 shell に集約"}`
   🔴 **`identity_basis` が `source_exact` であるにもかかわらず、
   ヴィンテージが shell の identity に含まれていない。**
   **その結果、2022 年（$3,720）と 2018 年（$3,260）という異なる 2 つの商品が 1 つの shell に潰れている。**
   ⚠️ **一方 803 行（村名・2023）は独自の shell を得ており、挙動が一貫していない。**
3. **証拠**: 上記 `duplicates.json` の実エントリ。🔍 `mapping.json` で 806 / 807 の `shell_id` が同一。
4. **OBP への影響**:
   🔴 **合計 $6,980 の 2 行が 1 つの実体として扱われる。**
   **価格差 $460 とヴィンテージ差 4 年が失われる。**
   **canonical には 2018 しか無いため、昇格時に 2022 が 2018 に吸収される危険がある。**
5. **推奨対応（DO NOT EXECUTE）**:
   **`level: product` の shell identity に `vintage_text` を含める。**
   ⚠️ **ただしこれは intake 側の設計変更であり、本書では実行しない。**
6. **Confidence**: **High**（成果物の実エントリを読んで確認）。

---

### 【5】🔍 **欠落 —— canonical に 4 本分のレコードが無い（衝突ではない）**

🔍 **canonical の Clos de Tart レコードは `clos-de-tart-2018` の 1 件のみ。**

| OBP 行 | 状態 |
|---|---|
| 803 `Morey-Saint-Denis` 2023（$600） | 🔴 **キュヴェ自体が canonical に無い** |
| 804 `La Forge de Tart` 2022（$1,040） | 🔴 **キュヴェ自体が canonical に無い** |
| 805 `La Forge de Tart` 2021（$1,020） | 🔴 **キュヴェ自体が canonical に無い** |
| 806 `Clos de Tart Grand Cru` 2022（$3,720） | **キュヴェはあるがヴィンテージが無い** |
| 807 `Clos de Tart Grand Cru` 2018（$3,260） | ✅ **唯一の一致**（ただし【3】の内容誤りあり） |

🔴 **本書の §Important Cuvées にある公式 3 ワインと、各ワインの公式ヴィンテージ一覧が、
そのまま登録原簿として使える。**
**ただし登録は Akio / CTO 判断。本書では実行しない。**

---

## Sources

**一次資料（公式サイト `https://www.clos-de-tart.com/`、INAO cahier des charges、認証機関の公開登録）**

### 🔴 サイト真正性の検証（**必須手順**）

**`clos-de-tart.com` を公式と判定した根拠は 4 つ。指示の (a)(b)(c)(d) をすべて満たす。**

| 検証 | 結果 |
|---|---|
| **(a) mentions légales に実在の法人名** | ✅ 🔴 **`/fr/mentions` に `Le responsable du traitement est Société du Clos de Tart dont le siège social est sis 7 route des grands crus, 21 220 [Morey]-Saint-Denis, France, immatriculée au Registre du Commerce et des Sociétés de Dijon sous le numéro 686042409`。**ファンページ的な免責文言は一切無い |
| 🔴 **(b) 所有者からの相互リンク** | ✅ 🔴 **親会社 `artemis-domaines.com` のトップページが `Clos de Tart` を自社ドメーヌとして記載し、`href="https://www.clos-de-tart.com/fr/"` で本サイトへ直接リンクしている。**さらに **Clos de Tart 側のフッターが `Château Grillet` / `Eisele Vineyard` / `Château Latour` / `Domaine d'Eugénie` へリンクしており、双方向で噛み合う** |
| 🔴 **(c) 公的登録との識別子の一致** | ✅ 🔴 **Agence Bio 公開登録の `siret 68604240900041` の先頭 9 桁（SIREN）`686042409` が、mentions légales の RCS Dijon 番号 `686042409` と完全一致。**登録上の住所 `7 RTE DES GRANDS CRUS, 21220 MOREY-SAINT-DENIS` は公式サイトの所在および **Ecocert 証明書ページの住所とも一致** |
| **(d) 商法・法務フッターの整合** | ✅ **全ページに Cookie ポリシー、CNIL への言及、GDPR 上の権利、制作会社 `Vinium Luxury Web Design`（3 rue des Corton, 21420 Aloxe-Corton）のクレジット。**🔴 **発行責任者は `Jean Garandeau`（`j.garandeau@chateau-latour.com`）—— 同一グループの Château Latour のドメイン** |

🔴 **なりすまし・偽サイトの却下は 0 件。**
**`closdetart.com` / `clos-de-tart.fr` / `closdetart.fr` / `domaine-clos-de-tart.com` を試みたが、
いずれも名前解決しないか応答が無く、取得物が生じなかった。
したがって `_sources/clos-de-tart/NOT_THE_PRODUCER_*.html` は 1 件も作成していない。**

⚠️ 🔴 **公式サイト自身のタイポを記録しておく。**
**`/fr/mentions` と `/en/contact` の本文が、住所を 2 度とも `Moyer-Saint-Denis` と綴っている**
（正しくは `Morey-Saint-Denis`）。**同ページのヘッダー部と `/fr/contact` の住所表示は `Morey-Saint-Denis` で正しい。**
**これは真正性を損なうものではないが、文字列照合の材料に使ってはならない。**

### 取得した資料

| 資料 | 取得した情報 |
|---|---|
| ⚠️ 🔴 **`robots.txt` / `sitemap.php` / `sitemap.xml`** | 🔴 **3 つとも存在しない。すべて HTTP 200 で 183,062 バイトのソフト 404（`404 - La page que vous avez demandée n'existe pas`）を返す。**URL 構造はトップページ（186,093 バイト）のナビゲーションから抽出した |
| ✅ **`/fr/mentions`** | **法人名 `Société du Clos de Tart`、RCS Dijon 686042409、所在、発行責任者 `Jean Garandeau`、制作会社 Vinium** |
| 🔴 **`/en/history`** | 🔴 **1141 年創設（Tart 修道院シトー会修道女）、12 世紀初頭の旧称 `Climat de la Forge`、1791 年 Marey-Monge、1855 年 Lavalle の `Tête de Cuvée`、1932 年競売で Henri Mommessin、1996 年 Sylvain Pitiot、`Mommessin 家は 2018 年まで単独所有`、`2018 年 Pinault 家が取得`、7.53 ha** |
| 🔴 **`/en/location`** | 🔴 **7.53 ha・壁 1.2 km（2006 年修復）・300 m × 250 m・標高 269–302 m・南東向き・北 — 南植栽・12 micro climats・樹齢平均 60 年／一部 100 年超・Pinots Fins・マサル・セレクションと自前苗床・`Frédéric Engerer` と `Alessandro Noli` によるビオディナミ転換・`2016 年に実践導入、2019 年に Biodyvin 認証`・醸造場（7 → 14 桶）・全房比率（下部 1/3・上部 2/3・平均 55%・La Forge は 0）・野生酵母 100%・自然マロラクティック・18 か月（9 + 9）・6 月アッサンブラージュ・La Forge は 25 年未満の 3 区画・村名は 2018 年導入** |
| ✅ **`/en/wines`** | **公式 3 ワインの定義文と URL（`/en/wines/1/clos-de-tart`、`/2/la-forge-de-tart`、`/3/morey-saint-denis`）** |
| 🔴 **`/en/wines/{1,2,3}/…` ＋ `/…/{2018,2017,2016}`** | 🔴 **各ワインの公式ヴィンテージ一覧と、年ごとの収穫日・収量・ABV・pH・全房比率・熟成・瓶詰め日・公式テイスティングノート。**🔴 **ヴィンテージ切替は `/en/wines/<id>/<slug>/<year>` という URL で成立する**（`?millesime=` などのクエリ形は効かない） |
| 🔴 **`/en/wines/1/clos-de-tart` の `<h1>`** | 🔴 **`<span class='monopole'>Monopole</span>` が Clos de Tart にのみ付き、La Forge de Tart と Morey-Saint-Denis には付かない。**FR / EN 両方で確認 |
| **`/en/spirit`** | **650 年の修道女、`所有者は歴史上 4 人だけ`、14 世紀の `Tart の聖母`、1570–1924 年の `parrot press`、地下 2 層のカーヴ** |
| 🔴 **`/en/news/5`（2022/07/11）** | 🔴 **350 m の生垣（十数種）・生物多様性と菌根・巣箱・`La Forge` と `Ballonge 2` での接ぎ木実験（成功率 80%、2022 年に 4 畝へ拡大）・20 年のマサル・セレクションによる 50 個体のプール・INRAE Colmar とのウイルス研究・改修の完了予定** |
| 🔴 **`/en/news/4`（2021/04/08）** | 🔴 **2019 年が Artémis Domaines と Noli の最初の `berry to bottle`・新しい畑の区分（土壌／植物材料／剪定法／樹齢の 4 基準）・`15 基の木桶 20–40 hL が 50 hL のステンレスを置換`・新樽使用の減少・Bordeaux 大学との全房比率の共同研究** |
| ✅ **`/en/authenticity`** | **2024 年に `Prooftag` 認証システム導入** |
| ⚠️ **`/en/signature`** | **第三者評言 2 件。**🔴 **本書では事実源として不採用** |
| 🔴 **`extranet.inao.gouv.fr/fichier/PNOCDCClos-de-Tart.pdf`**（399 KB・真正の PDF） | 🔴 **AOC `Clos de Tart` の cahier des charges（v2.2、2010/09/16）。`décret du 4 janvier 1939`・赤の静止ワイン限定・Morey-Saint-Denis 村・aire parcellaire は 1965/07/24 承認・主要品種 pinot noir N／補助 chardonnay B, pinot blanc B, pinot gris G・収量 35 hL/ha、butoir 49 hL/ha・最低自然アルコール 11.5%・総アルコール上限 14.5%・若木の参入規定・repli と déclassement の手続き** |
| 🔴 **`extranet.inao.gouv.fr/fichier/PNOCDC-MoreySaintDenis.pdf`**（441 KB・真正の PDF） | 🔴 **AOC `Morey-Saint-Denis` の cahier des charges（v2.2、2010/09/14）。`décret du 8 décembre 1936`・1er cru の公式 climat 20 件の一覧・🔴 IV 章 2°c)（Clos de Tart 等の区画から `Morey-Saint-Denis premier cru` を climat 名なしで名乗れる規定）** |
| 🔴 **`opendata.agencebio.org/api/gouv/operateurs/?q=Clos de Tart`** | 🔴 **同一 SIRET `68604240900041` の 2 レコード。`141317 SOCIETE DU CLOS DE TART` = Ecocert France `FR-BIO-01`・`ENGAGEE`・`dateEngagement 2018-04-16`・`dateMaj 2025-02-03`。`128822 CLOS DE TART FAMILLE MOMMESSIN` = Bureau Veritas `FR-BIO-10`・`ARRETEE`・`dateEngagement 2015-03-25`・`dateArret 2018-04-16`** |
| ✅ **`certificat.ecocert.com/entreprise/E810A020-…`** | **証明書ページが実在。`CLOS DE TART`／`7, Route des Grands Crus, 21220 Morey Saint Denis`／`Agriculteur (production végétale), Fabricant & Transformateur`／`Certification Agriculture biologique Europe (EU) 2018/848`** |
| 🔴 **`biodyvin.com/fr/liste-des-membres-biodyvin.html`** | 🔴 **会員リストに `Clos de Tart / 21220 / Morey-Saint-Denis / Bourgogne` が掲載されている（＝現会員）** |
| 🔴 **`demeter.fr/adherents-sitemap.xml`（993 件）** | 🔴 **走査 → `Tart` は 0 件**（`Déplaude de Tartaras` 等の誤ヒットのみ）**＝ Demeter 非会員** |
| ✅ **`artemis-domaines.com`（トップ）** | ✅ 🔴 **`Clos de Tart` を自社ドメーヌとして記載し、`clos-de-tart.com` へリンク。**「**1141 年創設、長い歴史の中で 4 度しか手を変えていない、最後は 2018 年の `Groupe Artémis` による取得。7.53 ha 一枚地。ブルゴーニュで最大の Monopole classé en Grand cru**」 |

**取得できなかったもの / 存在しなかったもの**

- ⚠️ 🔴 **`robots.txt` / `sitemap.php` / `sitemap.xml` がいずれも存在しない**（すべてソフト 404）。
- ⚠️ 🔴 **`/fr/revue-de-presse` と `/en/press-review` が HTTP 500 を返す。**第三者評価の掲出内容は未確認。
- ⚠️ 🔴 **公式サイトが 2019 ヴィンテージ以降更新されていない。**
  **OBP の 2021 / 2022 / 2023 に対応する公式データが存在しない。**
- 🔴 ⚠️ **INAO のファイル名推測で外した 7 通りはすべて HTTP 200 で HTML を返した**
  （`info.agriculture.gouv.fr` 側の `Le document demandé n'existe pas`、8,354 バイト。
  および `extranet.inao.gouv.fr` 側の 6,901–6,903 バイト）。**いずれも保存せず破棄した。**
- ⚠️ **`/en/gallery`（260 KB）、`/en/cartography`（924 KB、地形図）、`/en/distributors`（307 KB）は未精読。**
  **`cartography` には 12 の micro climats の詳細が含まれる可能性が高い。**
- ⚠️ **`/en/news/1`（ラベル）、`/en/news/2`（改修）、`/en/news/3`（Bill Nanson）は未精読。**
- 🔴 ⚠️ **生産本数、収量の方針値、施肥・調合剤の具体、`fiche technique` PDF は存在しない。**
  **このドメーヌは造り手署名入りの技術シート PDF を配信していない**（Arlot と異なる点）。
- ⚠️ 🔴 **2026 年時点の現任者を確認する手段が無い。**
  **`Alessandro Noli` / `Frédéric Engerer` は公式サイト（〜2022 年更新）に基づく。**

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔍 **canonical: `migration/out/export/db_wine_canonical.json`（928 件）→ Clos de Tart 名義 1 件（`clos-de-tart-2018`）**／
🔍 **OBP: `research/out/t-01/inventory.json` 448–452 番（`source_line_no` 803–807）の 5 本。**
**`producer_heading` は 5 行とも `Clos de Tart`、`section_path` は `["FRANCE | RED", "BURGUNDY"]`、`section_start_page` は 12、`layout` は `producer_heading`、`flags` は全行空。**
🔍 **`research/out/t-01/mapping.json`（803 / 806 / 807）・`review.json`（804 / 805）・`duplicates.json`（shell `rs:pro:8b62b9cf17ab172d`）。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | **法人名・RCS・SIRET・所在・電話・現所有者・親会社・CEO・Estate Director がすべて一次で取れた。**公的登録と mentions légales が識別子レベルで一致し、親会社サイトと相互リンクもある |
| **Overview** | **High** | 「ブルゴーニュ最大のグラン・クリュ・モノポール」「一度も分割されていない」「所有者は 4 人」「3 つのワイン」がすべて公式 |
| **History** | 🔴 **High** | 🔴 **1141 年から 2024 年まで、年つきの系譜が公式の history ページと INAO の décret から連続して取れた。**⚠️ Mommessin 期 86 年間の詳細のみ薄い |
| **Location** | 🔴 **High** | 🔴 **面積・壁の長さと修復年・寸法・標高・向き・畝の向きとその理由・12 micro climats・樹齢・植栽材料がすべて公式。**さらに 3 つのワインの畑上の出どころまで確定 |
| 🔴 **Farming** | 🔴 **High** | 🔴 **公式の主張に加え、`Agence Bio` 公開登録で Ecocert `FR-BIO-01`・`ENGAGEE`・`dateEngagement 2018-04-16` を確認し、旧 Mommessin 登録の `ARRETEE 2018-04-16` まで取れた。**🔴 **ビオディナミは `Biodyvin` の公式会員リストに実在を確認、`Demeter` は 993 件走査で非会員を確認。**⚠️ **Biodyvin の認証年 2019 は自己申告のみ** |
| **Winemaking** | 🔴 **High** | 🔴 **酵母・マロラクティック・全房比率（区画別と平均）・熟成の 2 段階・アッサンブラージュ時期・年ごとの収量／ABV／pH／新樽率／瓶詰め日が公式。**⚠️ **桶の本数が公式内で 14 と 15 に割れている。生産本数はゼロ** |
| **Style** | 🔴 **High** | 🔴 **3 ワイン × 複数ヴィンテージの公式テイスティングノートを取得。OBP の 2018 を含む** |
| **Important Cuvées** | 🔴 **High** | 🔴 **公式 3 ワインの正式名・格・モノポール status・ヴィンテージ一覧を確定。**🔴 **`La Forge de Tart` の Premier Cru 資格を INAO の条文で確定したのが最大の成果。**⚠️ **OBP 5 本のうち公式でヴィンテージ実在まで確認できたのは 2018 の 1 本のみ**（サイトが古いため） |
| **Staff Notes** | **High** | ⚠️ **15 項目。**🔴 **「モメサン家の」「モレの中の畑」「村名は外の畑」「Demeter」「La Forge は climat 名」「新樽 50%」という 6 つの事故を塞いだ** |
| **Canonical Conflict** | 🔴 **High** | 実データを読んで 4 件（＋欠落 1 件）を特定。**同名衝突は `score 0.7143` と `entity_id` という実値で裏付けた。**⚠️ **タスク前提の「行 1 が Grand Cru キュヴェに exact 一致」は成果物では確認できず、その旨を明記した** |
| 🔴 **総合** | 🔴 **High — staff-usable。70% を明確に超過（体感 90%）。** | **OBP 掲載 5 本すべてについて、公式の正式名・appellation（INAO 条文つき）・畑・樹齢・栽培と認証（開始日つき）・醸造方針を言える。**欠けているのは **2021 / 2022 / 2023 の年別データ**（公式サイトが古い）と**生産本数**であり、いずれも「言わなければ嘘にならない」種類の欠落である |

**reached_70: YES.**

---

## Open Questions

1. 🔴 **canonical に 4 本分のレコードが無く、既存の 1 件にも誤りがある。**
   **`Morey-Saint-Denis`（村名・キュヴェごと）、`La Forge de Tart`（キュヴェごと・2 本）、
   `Clos de Tart` の 2022。**
   **加えて `clos-de-tart-2018` の `aging`（新樽 50% → 公式は 80%）と
   `description_en` の裏付けの無い人名。**
   → **登録・訂正の可否は Akio / CTO 判断。本書では実行していない。**
2. 🔴 **生産者名とキュヴェ名が同一文字列である問題を、どう一般化して解くか。**
   🔴 **`cuvee:clos-de-tart-clos-de-tart` という実体 ID が既に生成されている。**
   **同型の生産者（`Clos des Lambrays`、`Château Latour` など、生産者名＝旗艦キュヴェ名）が
   canonical にどれだけあるかの棚卸しが要る。**
   → **採番と設計判断は CTO。**
3. 🔴 **村名 `Morey-Saint-Denis` の条文上の経路が特定できていない。**
   **Morey-Saint-Denis の cahier des charges IV 章 2°c) は `premier cru` の経路しか定めていない。**
   **Clos de Tart の画定区画から採れたブドウが村名 AOC を名乗る根拠が、
   `repli`（引き下げ）なのか、Clos de Tart の区画が Morey-Saint-Denis の
   `aire parcellaire` にも含まれているからなのかが未確定。**
   → **1982 年 11 月 3–4 日承認の `documents graphiques`（Morey-Saint-Denis 村役場に寄託）が要る。**
   **PDF には図面が含まれていない。**
4. 🔴 **`Biodyvin` 認証の取得年。**
   **公式サイトは「2019 年」と書くが、`Biodyvin` 側の会員リストには年が載っていない。**
   **一方 Agence Bio の Ecocert 登録は `2018-04-16` 開始である（こちらは有機 AB であってビオディナミではない）。**
   → **`Biodyvin` に会員名簿の登録年を照会するか、認証書の実物が要る。**
5. 🔴 **公式サイトが 2019 ヴィンテージ以降更新されていない。**
   **OBP に載る `Clos de Tart 2022`（$3,720）、`La Forge de Tart 2022 / 2021`（$1,040 / $1,020）、
   `Morey-Saint-Denis 2023`（$600）—— 合計 $6,380 分の存在を公式で確認できない。**
   ⚠️ **とくに `La Forge de Tart` は公式一覧を見る限り毎年造られてはいない
   （2015 / 2013 / 2012 / 2010 / 2009 が欠けている）ため、2021 と 2022 の両方が存在するかは要確認。**
   → **輸入元の割当リスト、またはドメーヌへの直接照会が要る。**
6. **`Clos de Tart` の公式ヴィンテージ一覧に `1997` と `1998` が無い。**
   **公式は理由を書いていない。**（1996 はあり、1999 以降は連続している。）
7. 🔴 **木桶の本数が公式内で割れている。**
   **`/en/location` は「7 基のステンレス → 14 基の木桶」、`/en/news/4` は「15 基の木桶が 50 hL のステンレスを置換」。**
   → **どちらかが古い記述である可能性が高いが、公式は説明していない。**
8. **`La Forge de Tart` の全房比率。**
   **総論は「一切用いない」、2018 年は `100% destemmed` だが、2019 年は `15%`。**
   **公式はこの差を説明していない。**
9. **生産本数。** **3 ワインのどのページにも記載が無く、技術シート PDF も配信されていない。**
10. **2026 年時点の Estate Director。**
    **`Alessandro Noli` は 2022 年更新の公式サイトに基づく。現任かどうかは未確認。**
11. **`/en/cartography`（924 KB の地形図）が未精読。**
    **12 の `micro climats` の名称と面積が含まれている可能性が高く、
    `La Forge` / `Ballonge 2` / `Plantation 2011` の位置と規模が確定できるかもしれない。**
12. **`/en/press-review` が HTTP 500。**
    **公式がどの第三者評価を掲出しているか未確認**（本書では事実源に採用しないが、
    OBP の `points: 96` の出所を辿る手掛かりにはなりうる）。
