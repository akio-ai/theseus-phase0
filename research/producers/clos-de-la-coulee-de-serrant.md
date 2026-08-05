# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical には 2021 年の 2 レコードのみ存在する。本書は昇格前の研究記録であり、canonical を一切変更していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者公式サイト `coulee-de-serrant.com` で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05
> 一次資料: **`https://coulee-de-serrant.com/`（FR / EN）**
> 走査元: **`robots.txt` → `sitemap_index.xml` → `page-sitemap.xml`（36 URL）/ `post-sitemap.xml`（44 URL）**
> 公的登録: **Agence Bio 公開登録（フランス国）／Certipaq Bio 証明書／Demeter France 会員登録**
> 原産地: **INAO `extranet.inao.gouv.fr` の cahier des charges 実 PDF 3 本**
>
> 🔴 **本ドシエ最大の収穫は 2 つ。**
> **① OBP が 5 行すべてに印字している `Savennières` は、うち 3 行で誤りである。**
> **`Clos de la Coulée de Serrant` の 3 本は AOC `Savennières` ではなく、独立した AOC
> `Coulée de Serrant`（2011 年 11 月に `Savennières Coulée de Serrant` として homologué、
> のち `Coulée de Serrant` に改称）である。INAO の cahier des charges 本文で確認した。**
> **② 栽培の認証は公式サイトからは一切取れない。** 公式は「**avec contrôle**（管理下で）」としか書かず、
> 認証機関名を一度も出さない。**認証は国の登録簿と認証機関側でしか確定できなかった。**
>
> ⚠️ **調査上の制約 3 点**
> **① INAO の製品ページ `www.inao.gouv.fr/produit/coulee-de-serrant-13353` は HTTP 403 を返し続けた**
>    （`savennieres-roche-aux-moines-16953` は 200 で取得できた）。→ Open Questions 5
> **② 取得できた Coulée de Serrant の cahier des charges は 2014 年 9 月 11 日の
>    「procédure nationale d'opposition」版である。** 現行homologué版そのものではない。
>    ただし**太字＝修正箇所の判定をフォント単位で行い、収量値が修正対象でないことは確認した。**
> **③ 公式サイトの英語版は機械翻訳の劣化が著しい**（`Coulée`→`Casting`、`rendement`→`output`、
>    `âge moyen`→`Middle Age`）。**本ドシエの数値はすべてフランス語版を採った。**

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Famille Joly** |
| **公式サイト上の呼称** | ✅ **`La Coulée de Serrant`**（全ページのフッタが `Copyright 2026 © La Coulée de Serrant`、`<title>` は `… - La Coulée de Serrant`、サイトのタグラインは **`LA COULÉE DE SERRANT, UN VIGNOBLE D'EXCEPTION`**） |
| 🔴 **法人** | ✅ **`SAS Famille JOLY`** — 公式 `mentions-legales` に明記。「**Propriétaire : Famille JOLY – SAS Famille Joly（Siret 40371449600011）– CHATEAU ROCHE AUX MOINES 49170 SAVENNIERES**」 |
| 🔴 **OBP 印字との関係** | ✅ **`Famille Joly` は空想の呼称ではなく、法人名そのものである。** Agence Bio 登録簿の `raisonSociale` も **`FAMILLE JOLY`**、`denominationcourante` も **`SAS FAMILLE JOLY`** |
| **所在** | ✅ **Château de la Roche aux Moines / 7 Chemin de la Roche aux Moines、49170 Savennières（Maine-et-Loire）** |
| 🔴 **サイト運営者** | ✅ **Virginie Joly**（`Créateur` / `Responsable publication` / `Webmaster` の 3 役すべて。公式 `mentions-legales`） |
| **Nicolas Joly** | ⚠️ 🔴 **公式サイトは Nicolas Joly を「著者」として扱っており、「当主」「醸造責任者」といった役職を一度も書いていない。** メニュー `Livres de N.Joly` があり、著書 10 言語版のページ群が存在する。→ §Staff Notes ⚠️ ⑧ |
| **公的登録** | ✅ **Agence Bio 事業者番号 `148071`／SIRET `40371449600011`／NAF `01.21Z`（ブドウ栽培）** |
| **有機認証** | ✅ **`Certipaq Bio`（EU 管理番号 `FR-BIO-09`）。状態 `ENGAGEE`。** 🔴 **`datePremierEngagement` = 1995-03-15** |
| **ビオディナミ認証** | ✅ **Demeter France 会員（`SAS FAMILLE JOLY`）。** ❓ **開始年は Demeter 側に記載が無い** |
| **生産する AOC** | 🔴 ✅ **3 つ**（`Coulée de Serrant` / `Savennières Roche aux Moines` / `Savennières`） |
| canonical producer id | 🔍 **`producer:clos-de-la-coulee-de-serrant-nicolas-joly`**（表示名 `Clos de la Coulée de Serrant (Nicolas Joly)`）。⚠️ **この文字列は公式サイトのどこにも存在しない** |

🔴 ⚠️ **`Clos de la Coulée de Serrant` という文字列は、生産者自身のサイト全 20 ページを走査して一度も出てこない。**
**唯一これを使っているのは Demeter France の会員登録の「所在」欄
（`Clos De La Coulée De Serrant / 7 Chemin De La Roche Aux Moines / 49170 SAVENNIERES`）である。**
**つまりこれは屋号・所在地名であって、ワイン名でも法人名でもない。** → §Canonical Conflict ①

---

## Overview

✅ **ロワール右岸、Angers の西 12 km ほどの Savennières 村。7 ヘクタールの単一の畑が、
それ自体でひとつの AOC を構成している。所有するのは Joly 家ただ一家である。**

🔴 ✅ **公式の一文がすべてを言い切っている** —
「**Le vignoble produit 3 vins d'appellations différentes（この畑は、appellation の異なる 3 つのワインを生む）**」
> **「La COULÉE de SERRANT」、appellation Coulée de Serrant、monopole de la famille Joly**
> **「Le CLOS de la BERGERIE」、appellation Savennières-Roche aux Moines**
> **「Les VIEUX CLOS」、appellation Savennières**

🔴 **この 1 行が、OBP メニューの 5 行のうち 3 行を否定する。** → §Important Cuvées / §Staff Notes ⚠️ ①

✅ **INAO の cahier des charges が独立 AOC であることを裏づける。**
「**Seuls peuvent prétendre à l'appellation d'origine contrôlée « Savennières Coulée de Serrant »,
les vins répondant aux dispositions particulières fixées ci-après.**」
🔴 そして同じ文書の歴史記述が改称の経緯を明記している —
「**（生産者たちは）この lieu-dit の appellation d'origine contrôlée としての認定を求めた。
豊かな歴史から生まれた彼らの実践は、2011 年 11 月に homologué された cahier des charges に
成文化され、独立した appellation d'origine « Savennières Coulée de Serrant » を認定した。
これはのちに « Coulée de Serrant » となる。**」

🔴 ✅ **農法こそがこの生産者の中身である。公式の記述は徹底している。**
「**une AOC は土壌と微気候によって刻印される。ブドウ樹がこの独自性を完璧に捉えるためには、
きわめて厳格な行動規範が要る。われわれはそれを早くから採用した（1984 年以来、畑の全体がビオディナミである）。**」

🔴 ✅ **公式が自ら掲げる立場** — 「**cellier（醸造小屋）は、われわれの目には産院でしかありえず、
決して工場ではない。**」

🔍 **THÉSEUS における状態は悪い。canonical は 2021 年の 2 本しか持たず、OBP 掲載 5 本の
ヴィンテージはそのどれとも一致しない。5 本すべてが `match_state = unresolved`。**

---

## History

✅ **公式サイトと INAO の cahier des charges が、同じ年号で一致している。**

| 年 | 出来事 | 層 |
|---|---|---|
| **1130** | 🔴 **シトー会修道士がブドウを植える。以来ブドウ畑であり続けている。** 公式:「**Plantés en 1130 par les moines Cisterciens et toujours resté en vigne depuis**」／INAO:「**Le vignoble de la « Coulée de Serrant » a été planté en 1130 par des moines cisterciens et, depuis cette date, le vin produit à partir de ces vignes a toujours été commercialisé sous cette dénomination**」 | ✅✅ **公式＋INAO の二重確認** |
| **1214** | **Roche aux Moines の戦い。** Philippe Auguste の子 Louis が Jean sans Terre を破る。**Bouvines の勝利の数週間前。** 公式・INAO 双方が触れる（INAO は Roche aux Moines の製品ページ） | ✅ |
| **1809** | INAO 引用 — 『Nouveau cours complet d'agriculture』（Institut de France）:「**… la coulée de Serrant, petit clos sur le penchant d'une colline escarpée, qui donne le meilleur vin de Maine et Loire …**」 | ✅ INAO |
| **1823** | INAO 引用 — JF BODIN:「**La Coulée de Serrant は名高く、それを生む clos はあまりに小さいので、手に入れるのがひどく難しい。**」 | ✅ INAO |
| **1887 / 1894** | ✅ INAO — **フィロキセラで畑が部分的に破壊され、1894 年に再植された。** | ✅ INAO |
| **1925** | ✅ INAO — MAISONNEUVE『L'Anjou, ses vignes, ses vins』が **Coulée de Serrant に丸ごと一章を割く。** | ✅ INAO |
| **1952-12-08** | 🔴 ✅ **AOC `Savennières` 認定の décret。この時点ですでに、`Coulée de Serrant` に区画指定された畑のワインは、AOC 名に この lieu-dit 名を付け加えてよいと定められていた。** | ✅ INAO |
| **1980** | ✅ 公式（EN 技術シート）—「**The domaine started biodynamic farming in 1980.**」／FR —「**La biodynamie a été implantée en 1980**」 | ✅ |
| **1984** | 🔴 ✅ **畑の全体がビオディナミに。** 「**depuis 1984 la totalité du vignoble en bénéficie. Aucun produit chimique de synthèse, acaricide, pesticide, systémique, désherbant, nitrate n'est utilisé depuis cette date.**」 | ✅ |
| **1985-09-11/12** | ✅ INAO — **`Coulée de Serrant` および `Roche aux Moines` の aire parcellaire（区画境界）が全国委員会で承認される。** | ✅ INAO |
| **1995-03-15** | 🔴 ✅ **有機認証への最初の登録（`datePremierEngagement`）。** フランス国 Agence Bio 登録簿 | ✅ 公的登録 |
| **2011-11** | 🔴 ✅ **cahier des charges が homologué され、`Savennières Coulée de Serrant` が独立 AOC として認定される。** 同年 `Savennières Roche aux Moines` も認定（INAO 製品ページ:「**ce site remarquable a conduit, en 2011, à la reconnaissance de l'AOC Savennières Roche aux Moines**」） | ✅ INAO |
| **2014-09-11** | 🔴 ✅ **AOC 名を `Coulée de Serrant` に改める cahier des charges 修正が国内異議申立手続に付される。** 表紙が **`« COULÉE DE SERRANT »`**、本文の見出しがまだ **`« SAVENNIÈRES COULÉE DE SERRANT »`** という過渡的な体裁 | ✅ INAO |
| **2015 / 2017** | ✅ 公式 — **2015 年が 885 回目、2017 年が 887 回目の連続収穫**（1130 年から途切れていない） | ✅ |

⚠️ **公式サイトは Joly 家がいつこの畑を取得したかを書いていない。** 取得年・世代数・当主の交代はすべて空白。
**INAO は「petit vignoble lieu-dit は数世紀にわたり Château de Serrant（隣接する Saint-Georges-sur-Loire 村）の
所有だった」「1894 年の再植後、歴代の所有者が耕作を続けた」としか書かない。** → Open Questions 3

⚠️ 🔴 **ビオディナミ開始年に、公式サイト内部で食い違いがある。**
**FR 技術シートの Coulée de Serrant の節だけが「Agriculture biodynamique depuis 1981 avec contrôle」と書き、
同じページの Clos de la Bergerie は「depuis 84」、Les Vieux Clos は「depuis 1984」、
そして同ページ末尾の総括は「1980 に導入、1984 から全体」と書いている。**
→ **言うなら「1980 年に導入、1984 年以来 畑の全体」。** → §Staff Notes ⚠️ ④

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Loire（Val de Loire）** ✅ — 🔴 **3 つの AOC いずれも、名称に地理的呼称 `Val de Loire` を付加できると cahier des charges に明記** |
| **Commune** | ✅ **Savennières（Maine-et-Loire、コード 49329）。** 🔴 **INAO: 収穫・醸造・熟成・（Savennières では）瓶詰めまで、すべてこの 1 村の領域で行われる** |
| **位置** | ✅ INAO — **ロワール右岸、Angers から 12 km ほど。南／南東向きの谷（talweg）を見下ろす斜面。北側は風の当たる、より寒冷な台地で、主に牧畜と穀作に充てられる** |
| 🔴 **`Coulée de Serrant` の構成** | ✅ INAO — **3 つの区画からなる。`grand clos de la coulée`（3 ha 98 a 50 ca、Chamboureau の丘の西斜面、強い傾斜）／`clos du Château`（85 a 50 ca、旧 Roche de Serrant 城の壁の下）／`Les Plantes`（2 ha 03 a、一部は東向きの急斜面、残りは Roche aux Moines の丘の南向き緩斜面）** |
| 🔴 **公式面積 vs INAO** | ⚠️ **公式は「7 hectares」。INAO は「6 ha 87 a」。** 上記 3 区画の合計は **6 ha 87 a** で INAO と一致する。**「7 ヘクタール」は生産者側の丸めである** |
| **地質** | ✅ INAO — **アルモリカ地塊。上部オルドヴィス紀〜下部デヴォン紀の片岩・片岩質砂岩。母岩が表層に極めて近く、土壌は浅く、痩せ、石が多い。排水能力が高く保水力は低い** |
| **土壌（生産者）** | ✅ **「赤い斜行片岩の上に載る、ごく薄い土壌（平均 20〜40 cm）」**（`Coulée de Serrant`）。**INAO は「0,15 メートル」と、さらに薄い数字を挙げている** ⚠️ |
| **気候** | ✅ INAO — **海洋性。西の Mauges 山塊がフェーン効果で緩和する。年間降水量は平均 600 mm（Mauges の丘では 800 mm 超）。年平均気温 約 12 ℃。ロワール川が温度調節器として働き、収穫期の朝霧を生んで botrytis cinerea の発生を促す** |
| **馬** | ✅ **馬で耕す区画は 1 ヘクタール半。「この部分の樹はほぼ樹齢 100 年で、土は完全に耕される」** |

### ✅ 3 つのワインの畑データ（公式 FR `fiche-technique` より。**EN 版は数値が古く一致しない**）

| | **Coulée de Serrant** | **Clos de la Bergerie** | **Les Vieux Clos** |
|---|---|---|---|
| **AOC** | 🔴 **Coulée de Serrant** | **Savennières Roche aux Moines** | **Savennières** |
| **面積** | **7 ha**（INAO は 6 ha 87 a）| **3,2 ha** | **5,5 ha** |
| **斜面** | **強い傾斜、南寄り** | **東寄り** | **東寄り、時に急** |
| **平均樹齢** | **35〜40 年**（最古 80 年）| **30 年** | **18〜20 年** |
| **植栽密度** | **4800〜6700 本/ha** | **4800 本/ha** | ⚠️ 記載なし |
| **土壌** | **片岩、石英** | **片岩、石英** | **片岩、石英、砂** |
| **収量（実績）** | **20〜25 hl/ha** | **28〜30 hl/ha** | **30〜35 hl/ha** |
| **生産本数** | **20,000〜25,000 本** | **8,000〜10,000 本** | **20,000 本前後** |
| **ビオディナミ** | **1981〜**（⚠️ 他所は 1984）| **1984〜** | **1984〜** |

⚠️ 🔴 **`Les Vieux Clos` の面積と生産本数は、公式サイト内部で一致しない。**
**`fiche-technique`（FR）は「5,5 ha / 20 000 本前後」、`presentation`（FR）は「15 000 本 / 年」、
EN 技術シートは「Savennières 3 hectares」。** → §Staff Notes ⚠️ ⑦

---

## Farming

🔴 **この生産者において、栽培は付随情報ではなく本体である。以下はすべて公式サイトの記述。**

### ✅ 認証（🔴 **公式サイトからは一件も取れない。すべて公的登録簿と認証機関側で確定した**）

| | |
|---|---|
| 🔴 **公式サイトの記述** | ✅ **「Agriculture en biodynamie depuis 1984 **avec contrôle**」。** **認証機関名は 3 ワインいずれについても書かれていない。** サイト全 20 ページに `Demeter` / `Biodyvin` / `Certipaq` / `Ecocert` の語は**一度も出てこない** |
| **有機（AB / EU）** | ✅ **Agence Bio 公開登録簿（フランス国）** — 事業者 `FAMILLE JOLY` / `SAS FAMILLE JOLY`、`numeroBio 148071`、SIRET `40371449600011`。**`datePremierEngagement` = `1995-03-15`** |
| 🔴 **認証機関** | ✅ **`Certipaq Bio`（EU 管理番号 `FR-BIO-09`）。** `etatCertification` = **`ENGAGEE`**、`dateNotification` = 2004-05-14、`dateEngagement` = 2022-05-04。**`dateSuspension` / `dateArret` はいずれも null** |
| **証明書** | ✅ **Certipaq 側の事業者ページ（事業者番号 58522）に証明書 `FR-BIO-09.250-0084025.2025.002` があり、有効期間 `10/12/2025 – 31/03/2027`。** 2021 / 2022 / 2023 / 2024 / 2025 の旧証明書も残っている |
| **AB 認定の対象** | ✅ **`Raisin de cuve`（醸造用ブドウ）と `Vins de raisin`（ブドウ酒）がいずれも 2025 管理年で `AB`。** 併せて `Prairie permanente`、`Vaches allaitantes`、`Veaux`、`Pommes de table` も `AB`（**牛と果樹まで含めて有機である**） |
| 🔴 **ビオディナミ** | ✅ **`Demeter France` の会員登録に `SAS FAMILLE JOLY` が存在する。** 所在は **`Clos De La Coulée De Serrant / 7 Chemin De La Roche Aux Moines / 49170 SAVENNIERES`** |
| **Demeter 開始年** | ❓ **Demeter France の会員ページに開始年の記載が無い。** → Open Questions 2 |
| **Biodyvin** | ⚠️ **`biodyvin.com` の `sitemap.xml` は 19 URL しか列挙せず、会員一覧が含まれない。加盟の有無を判定できなかった。** **「Biodyvin である／でない」とは言わない** |
| **`mixite`** | ✅ **Agence Bio 登録簿の `mixite` は `Non`。すなわち有機と慣行の混在経営ではない** |

### 🔴 ✅ 公式が挙げる栽培の実務（`actes-agricoles`／`en/statutes-…`。**「3 つのワイン、3 つの AOC すべてに関わる」と明記**）

| 項目 | 公式の記述 |
|---|---|
| 🔴 **堆肥** | **自家の牛 10 頭（`Nantaise`＝消滅危惧種 と `Highland`＝湿地に適応）と 雄牛 2 頭。「長期的に不均衡を生む人工授精を避けるため」。** 牛は**穀物・ビート・干し草で古いやり方で飼われ、その飼料はほぼすべて敷地内で作られる。**「**この土地に刻印された飼料が、この土地に適した堆肥をつくる**」。**この堆肥がビオディナミの調剤を受ける** |
| **草生** | **自然の草生。時とともに畑の周囲に数十種の植物が育った。「単一栽培の負の効果を抑える」** |
| 🔴 **除草剤** | **「20 年以上前から、畝間も含めて systématiquement 禁止」。** その不在ゆえに「**各々の根が異なる微生物（菌根）を生み、ブドウが土壌の subtilité をすべて捉えられるようになる**」 |
| 🔴 **耕耘** | **最小限（畝の chaussage / déchaussage）。「土壌の生命の層を混ぜないため」。馬で行う部分（1 ha 半、ほぼ樹齢 100 年）は完全に耕す** |
| 🔴 **動物** | **冬、ほとんどの区画に `Ouessant` 種の羊の群れを入れる。「この素朴な品種は草生を食べ、それを厩肥に変える」。春、カタツムリのいる区画に移動式の鶏小屋を置く。10 ほどの巣箱を敷地に配して受粉を確保する** |
| 🔴 **防除** | **ビオディナミ調剤（「病気とは健康の欠如でしかない」）と、植物のティザーヌ（セージ、スイバ、ヤナギ、イラクサ、ツヤ、ニレ、樫の樹皮、海藻、アルニカ、スピノサスモモ、コンフリー等）。「大半は敷地内の薬草、あるいは吉日に山で採取したもの」** |
| 🔴 **銅** | **ボルドー液で純銅 3〜5 kg/ha/年。「ある区画は 3 年間まったく使っていない」。「銅は生命に有用な微量元素だが、土壌の生命を抑えるので制限する」** ⚠️ **同じサイトの `fiche-technique` は「2/3 kg/ha/an」と書いており、数値が一致しない** |
| **硫黄** | **使用する。「開花期の光の供給として有益」。ただし「乳または乳清（5〜10 L/ha/回）に少しずつ置き換えつつある。うどんこ病に非常に有効で、樹に健全」** |
| 🔴 **生物多様性** | **「AOC 内で植栽可能な数ヘクタールを、荒地または草地のまま残している」。「そこから生じる動植物の多様性が、この土地の均衡の源であり、土壌の有機的生命の豊かさ＝テロワール効果の表現につながる」** |
| 🔴 **選抜** | **最も古い樹（1920 年前後）の枝木でしか苗を作らない。「畑は千年近く存在してきた。われわれ自身の AOC＝Coulée de Serrant に完璧に適応したシュナンの typicité を保たねばならない」。「クローンと違い、意味のある収穫まで 6 年かかる」** |
| 🔴 **剪定と収量** | **「年平均 20〜25 hl/ha に抑えるための厳しい剪定 —— 認可量のほぼ半分」。「これにより全ミレジムが非常に高い水準に達し、補糖も避けられる（Coulée では過去 15 年間 一度も無い）」** |
| **収穫** | **手摘み。3〜5 回の tri（選果通過）。9 月末〜11 月初の 5 週間ほど。「各房が最適な成熟に達したことを確かめるため」** |

### ✅ 品質憲章（`charte`。**生産者が自ら定め、公開している 3 段階の規範**）

**「Tous nos vins respectent les 3 stades de cette charte（われわれのワインはすべてこの憲章の 3 段階を守る）」**

- **第 1 段階（不可欠な基礎）**: 除草剤の全面排除／堆肥または有機質肥料／化学肥料の排除／有機農業の基準に沿った自然物のみでの防除、合成化学品（接触型・浸透型・浸達型を問わず）の全面排除／GMO 酵母・アロマ酵母の排除／遺伝子組換え苗の排除
- **第 2 段階（さらに進む）**: 手摘み／自然発酵の尊重（酵素添加・細菌添加・発酵活性剤〈窒素・ビタミン・チアミン・酵母皮〉・香味添加物の排除）／クリオエクストラクションおよびあらゆる濃縮法（減圧蒸発、逆浸透など）の排除／クローンを排したセレクション・マサル／**畑の土着酵母のみの使用**
- **第 3 段階（条件が許すとき）**: 補酸・除酸・補糖のいかなる形も禁止／**清澄（collage）なし**／**2 ミクロン未満または無菌の濾過なし**／**灌漑なし**

---

## Winemaking

🔴 **公式は「醸造では何をするか」ではなく「何をしないか」で語る。**
「**Le cellier ne doit être à nos yeux qu'une maternité et jamais une usine.**」

### ✅ 3 ワイン共通の実務（`au-cellier`）

| 工程 | 公式の記述 |
|---|---|
| 🔴 **デブルバージュ** | **行わない。**「なぜ澱を取るのか。ビオディナミ農法では悪い腐敗は非常に稀である。澱には発酵の良好な進行に必要な生きた要素が多く含まれる」 |
| 🔴 **冷却処理** | **行わない。**「冷は死の力であり、生の対極である。酒石を除き酸度を下げるこの技術は、われわれの考えでは望ましくない」 |
| 🔴 **酵母** | **土着酵母のみ。**「ビオディナミ農法では酵母は非常に多様で毎年異なり、各ミレジムの typicité を強める」。**「過去に中性酵母を 2〜3 回試したが満足のいくものではなかった」** |
| 🔴 **清澄（collage）** | **行わない。**「われわれの生産する少量のワインに、魚膠やアルブミンを入れる必要があるとは思えない。清澄はバリックの中で沈殿により自然に進む」 |
| 🔴 **温度管理** | **行わない。**「発酵を一定温度で強いることは、発酵という一種の熱＝新しい状態の出現を許す現象の、深い本性に反するのかもしれない。発酵は直線ではなく曲線を描いて進むべきである」。**発酵中に数日 25〜30 ℃まで上がることを害と見なさない。発酵は 2〜4 か月、時にそれ以上に及ぶ** |
| 🔴 **新樽** | **「毎年バリックの 3〜4 % を更新」。**「木はワインの良い呼吸に重要だが、新樽の味はワインにとって異物である。たとえ人好きのする味でも制限する。ワインはそれ自体で足りていなければならない」。**「バリックの球形は生の力を集める」** ⚠️ `fiche-technique` と `presentation` は「**5 % を超えない**」と書く |
| **樽の容量** | ✅ **`Coulée de Serrant` は 500 リットルのバリック** |
| 🔴 **熟成期間** | ✅ **`Coulée de Serrant` は オーク樽で 6〜8 か月。**`Clos de la Bergerie` と `Les Vieux Clos` は**新樽でない樽**（Vieux Clos はタンク醸造の年もある） |
| 🔴 **ソーティラージュ（澱引き）** | ⚠️ **記述が食い違う。** `au-cellier` は「**われわれはこれを増やす。酸素の供給だから**」、`fiche-technique` は「**1 à 2 soutirages**」。→ §Staff Notes ⚠️ ⑥ |
| **バトナージュ** | ✅ **行う**（`fiche-technique`） |
| 🔴 **SO₂** | ✅ **「各 soutirage のたびに 2 g ほどの軽い sulfitage を行う。これはまったく有害ではない。硫黄は光の一形態である」。** 加えて **`fiche-technique` は「瓶詰め前に軽い sulfitage」**。⚠️ **「2 g」の単位（g/hL と推定される）が公式に書かれていない。数値としては引用できない** |
| **無亜硫酸について** | ✅ **「硫黄を使わずにワインを造ることは可能だが、他の処理（アスコルビン酸、ソルビン酸カリウム等）を受けていない限り、輸送に耐えないおそれがある。われわれの考えではそれらのほうが有害である」** |
| 🔴 **濾過** | ✅ **「ワインが辛口のとき、濾過は非常に緩い（プレフィルトレーション）」。** 憲章の第 3 段階により **2 ミクロン未満・無菌濾過は行わない** |
| **補糖** | ✅ **行わない。**「Coulée では過去 15 年間 一度も無い」 |
| **禁じている操作** | ✅ **relevurage（再酵母添加）、香味添加、逆浸透（osmose）等は「bannis（禁じられている）」** |

### 🔴 ✅ 公式が挙げる分析値の目安

| 項目 | 記述 |
|---|---|
| **残糖** | **「一般に 2 g 未満」。** ⚠️ **「アルコールが 14,5 度を超える年には、酵母が転換しきらなかった残糖が 4〜5 g 残ることがある」** |
| **酸度** | **「4 と 5 のあいだ」。** ⚠️ **単位が書かれていない** |
| 🔴 **マロラクティック** | **「les malos ne se font pas toujours（マロは必ずしも起きない）」。** → **「マロを通す／通さない」と断定してはならない** |

---

## Style

### ✅ 生産者自身が語るスタイル（`presentation` / `au-cellier`）

🔴 ✅ **公式の中心命題は「成熟であって酸化ではない」である。**
「**シュナンは完全に熟したとき —— 深い黄色になったとき —— にしか複雑さを得ない。
そして健全で持続的な農業だけが、灰色カビを招かずにそれを保証できる。
そのため われわれのブドウはすべて、各区画が干しぶどう化し botrytis を形成しはじめるのに合わせて
4 回ないし 5 回に分けて摘まれる —— それによってシュナンのミネラルな風味が最大の強度に達する。
このように造られたワインは、開栓後もなお良くなり続け、けっして酸化していない。**」

✅ **生産者が提案する検証法** —
「**この色が酸化でないことを確かめるには、ご自身で試せばよい。冷蔵庫に戻さず、栓をし直すだけで、
数日にわたり毎日 1 杯ずつ味わってみてほしい。最初の数日、ときには 1 週間以上、
ワインが良くなっていくのが分かるだろう。もし酸化していたなら、飲めたものではないはずだ。**」

✅ **サービス（🔴 FR と EN で食い違う）**
- **FR（`au-cellier`）**: 「**できれば数回カラフェに移すか、24 時間前に開栓すること。カーヴの温度、すなわち最低 13 ℃で供する（14/15 ℃を推奨）。**」
- ⚠️ **EN（`presentation-wines`）**: 「**Open few hours in advance or carafe the wine. Serve at 14°C / 57°F.**」
→ **抜栓時間が「24 時間」と「数時間」で一致しない。** → §Staff Notes ⚠️ ⑨

✅ **料理（公式 `les-plats`。標語は「Plus les plats sont puissants plus nos vins s'expriment」＝料理が力強いほど、われわれのワインは表現する）**
**Poulet à l'Angevine（クリームとキノコ）／ロブスターのソース仕立て／仔牛のブランケット／
帆立のソース仕立て／サンドル（川カマス）のブール・ブラン／
非常に良いチーズ数種（Cantal、Salers、乾いたシェーヴル）**

### ✅ AOC の公式官能記述（INAO cahier des charges。**生産者ではなく appellation の記述である**）

| AOC | 記述 |
|---|---|
| 🔴 **Coulée de Serrant** | 「**ワインは白で、多くは辛口。麦わら色から黄金色の色調は ある種の優雅さを示す。香りは強く複雑な芳香のブーケを開く。マルメロ、杏、桃、あるいは乾果を思わせる果実の調子が、スパイシーあるいはスモーキーな香りと混じり合う。だがこのワインが何より魅了するのは 口中の見事な表現である。大きな凝縮、果実の芳香の豊かさ、味わいの美しい均衡、そして gras の存在が、ワインに美しい volume を与える。ミネラリティと清涼感に刻まれた例外的な長さの余韻が、ワインに信じがたい存在感を与える。**」 |
| **Savennières**（＝`Les Vieux Clos` の AOC） | 「**白、多くは辛口。ときに発酵性の糖を残すことがある。淡い黄色から黄金色。香りは一般に 花（アカシア、菩提樹…）の香りに、洋梨・桃・マルメロ・焼いたアーモンド・干しぶどう・蜂蜜を思わせる果実の調子が混じり、ミネラリティの一筆が加わる。口中のアタックは ample で gras、芳香の複雑さのすべてを明かす。余韻は清涼感、ミネラリティ、わずかな苦みの混合で、調和と均衡をもたらす。これらのワインは瓶熟数年を経て完全に開花する。**」 |
| **Savennières Roche aux Moines**（＝`Clos de la Bergerie` の AOC） | 「**黄金色の装いをまとい、花の香り、果実の調子、ミネラリティの一筆が絡み合う複雑な香り。口中は ample で suave、豊かさを釣り合わせる清涼感を備える。**」（INAO 製品ページ） |

⚠️ 🔴 **生産者は、キュヴェ別・ヴィンテージ別のテイスティングノートを一切公開していない。**
**公式サイトにヴィンテージ一覧のページも無い。** → §Staff Notes ⚠️ ⑩

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本、すべて `match_state = unresolved`**）

| # | OBP 印字 | VT | 価格 | ✅ **生産者自身の正式名** | 🔴 **真の AOC** | 判定 |
|---|---|---|---|---|---|---|
| 1 | **'Les Vieux Clos,' Savennières** | 2023 | $240 | ✅ **« Les VIEUX CLOS »** | ✅ **AOC Savennières** | ✅ **メニューの appellation は正しい** |
| 2 | **'Les Vieux Clos,' Savennières** | 2020 | $200 | ✅ **« Les VIEUX CLOS »** | ✅ **AOC Savennières** | ✅ **正しい** |
| 3 | **'Clos de la Coulée de Serrant,' Savennières** | 2023 | $500 | 🔴 ✅ **« La COULÉE de SERRANT »**（`Clos de la` は公式サイトに存在しない） | 🔴 **AOC Coulée de Serrant** | 🔴 ⚠️ **メニューの `Savennières` は誤り** |
| 4 | **'Clos de la Coulée de Serrant,' Savennières** | 2019 | $400 | 同上 | 🔴 **AOC Coulée de Serrant** | 🔴 ⚠️ **誤り** |
| 5 | **'Clos de la Coulée de Serrant,' Savennières** | 2012 | $600 | 同上 | 🔴 **AOC Coulée de Serrant** | 🔴 ⚠️ **誤り** |

🔴 **appellation を裏づける一次資料は 2 つある。**
**① 生産者の `presentation`:「Le vignoble produit 3 vins d'appellations différentes」に続く 3 行。**
**② INAO の cahier des charges:「Seuls peuvent prétendre à l'appellation d'origine contrôlée
« Savennières Coulée de Serrant » …」および 2014 年改称。**
**加えて Demeter France の会員登録が、生産者の 3 ワインを AOP 別に列挙している
（`AOP Coulée de Serrant` ／ `AOP Savennières - Roche aux Moines "Clos de la Bergerie"` ／
`AOP Savennières "Les Vieux Clos"`）。三者が完全に一致する。**

### 🔴 ✅ 5 本のヴィンテージ実在確認（**Demeter France の会員登録が公開している、Demeter 表示のヴィンテージ一覧**）

| ワイン | Demeter が列挙するヴィンテージ | OBP 掲載年の所在 |
|---|---|---|
| **AOP Coulée de Serrant** | **2010 / 2011 / 2012 / 2013 / 2015 / 2018〜2021 / 2023 / 2024** | ✅ **2023 実在・2019 実在（2018〜2021 に含まれる）・2012 実在** |
| **AOP Savennières «Les Vieux Clos»** | **2011 / 2012 / 2015 / 2018〜2021 / 2023 / 2024** | ✅ **2023 実在・2020 実在（2018〜2021 に含まれる）** |
| **AOP Savennières-Roche aux Moines «Clos de la Bergerie»** | **2010 / 2011 / 2015 / 2018 / 2020 / 2021 / 2023 / 2024** | 🔍 **OBP に該当行なし** |

🔴 **OBP 掲載 5 本すべてについて、そのヴィンテージが実在することを認証機関側の記録で確認した。**
⚠️ **ただしこれは「Demeter 表示で流通したヴィンテージ」の一覧であり、生産の全一覧ではない。**
**ここに無い年（例: Coulée の 2014 / 2016 / 2017 / 2022）を「造られなかった」と読んではならない。**

### ✅ 生産者の全キュヴェ（**3 つ。これがすべてである**）

| # | 公式表記 | AOC | canonical | OBP |
|---|---|---|---|---|
| 1 | **« La COULÉE de SERRANT »** | 🔴 **Coulée de Serrant**（モノポール） | ✅ `cuvee:clos-de-la-coulee-de-serrant-nicolas-joly-coulee-de-serrant`（name = `Coulée de Serrant`） | ⭐ **3 本** |
| 2 | **« Le CLOS de la BERGERIE »** | **Savennières Roche aux Moines** | ✅ canonical に 2021 が存在 | **0 本** |
| 3 | **« Les VIEUX CLOS »** | **Savennières** | 🔴 **canonical に存在しない** | ⭐ **2 本** |

🔴 🔍 **被覆の欠落 —— canonical が持つ 2 キュヴェのうち `Clos de la Bergerie` は OBP に無く、
OBP が持つ 2 キュヴェのうち `Les Vieux Clos` は canonical に無い。重なっているのは 1 キュヴェだけである。**
**そのうえ canonical のヴィンテージは両方とも 2021 で、OBP の 5 年（2023 / 2020 / 2023 / 2019 / 2012）
のいずれとも一致しない。** → §Canonical Conflict ③④

### ✅ AOC の法的規定（INAO cahier des charges。**canonical 登録時にそのまま使える**）

| | **Coulée de Serrant** | **Savennières** |
|---|---|---|
| **品種** | **chenin B のみ** | **chenin B のみ** |
| **色・タイプ** | **白のスティルワインのみ** | **白のスティルワイン** |
| **地理的呼称の付加** | **`Val de Loire` 可** | **`Val de Loire` 可** |
| **最低植栽密度** | **5 000 本/ha**（畝間 2 m 以下、株間 1 m 以上） | — |
| 🔴 **認可収量** | **辛口 30 hl/ha（butoir 35）／moelleux・doux 25（butoir 30）** | **secs・demi-secs 50 hl/ha（butoir 50）／その他 35（butoir 35）** |
| **区画あたり最大平均負荷** | **5 000 kg/ha** | — |
| **最低アルコール** | **11,5 %** | — |
| **区画境界の承認** | **1985 年 9 月 11・12 日の全国委員会** | — |

🔴 ⚠️ **収量の認可値について、公式サイトと INAO が一致しない。**
**公式は Coulée de Serrant について「(40 autorisés)」と書くが、INAO の cahier des charges は
辛口 30 hl/ha（butoir 35）である。** **PDF のフォントを走査して太字＝2014 年修正箇所を特定したところ、
収量の数値は太字ではなく、この改正で触られていないことを確認した。**
⚠️ **したがって「40 hl/ha まで認可されている」というのは、生産者側の記述としてしか引用できない。**
**なお `Savennières` の「50 autorisés」は INAO と一致する。** → §Staff Notes ⚠️ ②

### ✅ INAO による市場の記述（**2014 年改正で追加された太字部分**）

「**今日このワインは、心得た消費者のあいだで確立された名声を享受している。
フランス語圏・英語圏の報道にとどまらず、`Coulée de Serrant` の appellation は今日、
とりわけ日本とブラジルといった他の消費国で頻繁に言及される。
`Coulée de Serrant` のワインの総生産の 3 分の 2 以上が、現在 国外に輸出されている。**」

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① リストに載っている 2 つの名前は、appellation が違う。`Savennières` は片方だけの話。**
「**造り手は自分のサイトの冒頭でこう書いています —— 『この畑は、appellation の異なる 3 つのワインを生む』。**
**『レ・ヴュー・クロ』は AOC サヴニエール。**
**『クーレ・ド・セラン』は AOC クーレ・ド・セラン —— それ自体が独立したひとつの appellation です。**
**7 ヘクタールの畑がまるごと一個の AOC で、それをジョリー家が単独で所有している。**
**造り手自身が『monopole de la famille Joly』と書いています。**
**2011 年 11 月に『サヴニエール・クーレ・ド・セラン』として独立 AOC に認定され、
のちに『クーレ・ド・セラン』へ改称されました。**」

**② 1130 年にシトー会修道士が植え、以来ずっとブドウ畑。2017 年で 887 回目の連続収穫。**
「**シトー会の修道士が 1130 年に植えました。これは造り手の主張ではなく、
INAO の cahier des charges にそう書かれています —— 『1130 年にシトー会修道士によって植えられ、
その日以来、この樹から造られるワインは常にこの名で販売されてきた』。**
**造り手の側は『2015 年が 885 回目、2017 年が 887 回目の連続収穫』と数えています。**
**畑は 3 区画 —— グラン・クロ・ド・ラ・クーレ、クロ・デュ・シャトー、レ・プラント。合計 6 ヘクタール 87 アール。
造り手は 7 ヘクタールと丸めています。土は片岩で、深さ 20〜40 センチしかありません。**」

**③ 1984 年以来、畑の全体がビオディナミ。認証は Demeter と、有機は Certipaq Bio。**
「**1980 年に導入し、1984 年から畑の全体がビオディナミです。造り手はこう書いています ——
『その日以来、合成化学品、殺ダニ剤、殺虫剤、浸透性製剤、除草剤、硝酸塩は一切使っていない』。**
**堆肥は自家の牛 10 頭 —— ナンテーズ種とハイランド種、それに人工授精を避けるための雄牛 2 頭 ——
から作り、飼料もほぼ敷地内で賄っています。**
**冬にはウェサン種の羊を畑に入れ、春にはカタツムリのいる区画に移動式の鶏小屋を置く。
1 ヘクタール半は馬で耕していて、その区画の樹はほぼ樹齢 100 年です。**
**認証は、有機がセルティパック・ビオ（FR-BIO-09）で、フランス国の登録では最初の登録が 1995 年 3 月。
ビオディナミはドゥメテール・フランスの会員です。**」

### 追加で使える一手

- **クーレ・ド・セラン（$500 / $400 / $600）**: 「**7 ヘクタール、樹齢平均 35〜40 年、最古は 80 年。
  実収量 20〜25 hl/ha —— 造り手は『認可量のほぼ半分』と書いています。
  醸造は 500 リットルのバリック、新樽は 5 % を超えない。樽で 6〜8 か月。年産 2 万〜2 万 5 千本。**」
- **レ・ヴュー・クロ（$240 / $200）**: 「**クローンではなくセレクション・マサル —— 造り手いわく
  『香りの複雑さを増すため』。樹齢は 18〜20 年と 3 つのうち最も若い。土は片岩に石英、時に砂。
  木樽か、年によってはタンクで醸造します。**」
- **醸造で何をしないか**: 「**デブルバージュをしない。冷却処理をしない。清澄をしない。温度管理をしない。
  酵母は畑の土着のものだけ。新樽は毎年 3〜4 % しか更新しない。
  造り手の言葉では『cellier は産院であるべきで、決して工場ではない』。**」
- **サービス**: 「**カーヴの温度 —— 最低 13 度、造り手は 14〜15 度を勧めています。
  数回カラフェに移すか、事前に開けておいてください。**」
- **色について客に聞かれたら**: 「**深い黄金色は酸化ではなく成熟です。造り手はこう書いています ——
  『シュナンは完全に熟したときにしか複雑さを得ない』。
  そのためブドウは 4〜5 回に分けて、区画ごとに干しぶどう化とボトリティスが始まるのを待って摘まれます。
  造り手自身が確かめ方まで書いていて、栓をし直して冷蔵庫に入れず数日置くと良くなっていく、と。**」
- **料理**: 「**造り手が挙げているのは アンジュー風の鶏のクリーム煮、ロブスターのソース仕立て、
  仔牛のブランケット、帆立のソース仕立て、サンドルのブール・ブラン、
  そしてカンタルやサレール、乾いたシェーヴル。標語は『料理が力強いほど、われわれのワインは表現する』です。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が食い違う／出典が沈黙している**）

1. 🔴 ⚠️ **『クーレ・ド・セラン』を「サヴニエールのワイン」と言わない。**
   **AOC は `Coulée de Serrant` であり `Savennières` ではない。**
   **メニューの 3 行が印字している `Savennières` は誤りである。**
   村としての Savennières に在ることは正しいので、言うなら「**サヴニエール村にある、独立した AOC**」。
2. 🔴 ⚠️ **収量の「認可 40 hl/ha」を口にしない。**
   **これは公式サイトの記述であって、INAO の cahier des charges は辛口 30 hl/ha（butoir 35）である。**
   **言ってよいのは実収量のほう —— 「20〜25 hl/ha」（これは公式・複数ページで一致する）。**
3. 🔴 ⚠️ **「クロ・ド・ラ・クーレ・ド・セラン」を公式のワイン名として復唱しない。**
   **生産者のサイトにこの文字列は 1 度も出てこない。公式は « La COULÉE de SERRANT »。**
   **`Clos de la …` は Demeter の会員登録における所在地名（屋号）としてのみ確認できる。**
4. 🔴 ⚠️ **ビオディナミの開始年を「1981 年」と言わない。**
   **公式サイト内で 1980 / 1981 / 1984 の 3 つが混在している。**
   **安全なのは「1980 年に導入、1984 年以来 畑の全体」。**
5. ⚠️ **認証について「ビオディナミ認証を 1984 年に取得」と言わない。**
   **公式サイトは認証機関を一度も名指しせず「avec contrôle」としか書かない。**
   **確認できたのは Certipaq Bio（有機）と Demeter France（会員）で、**
   🔴 **Demeter の開始年は不明である。** **有機の最初の登録は 1995 年 3 月（フランス国の登録簿）。**
6. ⚠️ **ソーティラージュ（澱引き）の回数を数字で言わない。**
   **`au-cellier` は「増やす」、`fiche-technique` は「1〜2 回」と書いており、公式内部で矛盾している。**
7. ⚠️ **`Les Vieux Clos` の面積・生産本数を断定しない。**
   **`fiche-technique` は 5,5 ha / 約 20 000 本、`presentation` は約 15 000 本、
   英語版技術シートは 3 ha。3 つとも一致しない。**
8. ⚠️ **ニコラ・ジョリーの肩書きを名乗らせない。**
   **公式サイトは彼を「著者」としてしか扱わず、当主・醸造責任者といった役職を書いていない。**
   **サイトの `mentions légales` に名前があるのは Virginie Joly（作成者・公開責任者・ウェブマスター）である。**
   🔴 **彼の著書・講演・第三者インタビューは公式サイトの記述ではない。本ドシエはそれらを一切使っていない。**
9. ⚠️ **抜栓時間を「24 時間前」と断定しない。**
   **フランス語ページは「24 時間前」、英語ページは「数時間前」と書いている。**
   **言うなら「早めに開けるか、数回カラフェに移す」。**
10. 🔴 ⚠️ **ヴィンテージ別のテイスティングノートを「造り手いわく」と言わない。**
    **生産者はキュヴェ別・年別の官能記述を一切公開していない。**
    **官能記述として引用できるのは INAO の cahier des charges の appellation 記述だけで、
    それは「この AOC のワイン一般」の話である。**
11. ⚠️ **マロラクティック発酵を「する」とも「しない」とも言わない。**
    **公式は「les malos ne se font pas toujours（必ずしも起きない）」と書いている。**
12. ⚠️ **SO₂ の数値を言わない。** **「各 soutirage ごとに 2 g ほど」とあるが単位が書かれていない。**
13. ⚠️ **第三者点数・評価を言わない。** **本調査が取得したどの一次資料にも点数の掲載が無い。**
14. 🔴 ⚠️ **canonical の英文ノートにある「extended aging（長期熟成）」を復唱しない。**
    **公式は `Coulée de Serrant` について「オーク樽で 6〜8 か月」と明記しており、長期樽熟ではない。**
    →§Canonical Conflict ⑤

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

**新規の登録なし。**

🔍 **走査結果**: canonical（`migration/out/export/db_wine_canonical.json`、928 レコード）を
`Serrant` / `Joly` / `Bergerie` / `Vieux Clos` で走査 → **2 レコードのみ。**
生産者文字列は **`Clos de la Coulée de Serrant (Nicolas Joly)` の 1 種のみで、実体分裂も正規化キー衝突も無い。**

🔴 **本調査は既存カテゴリに該当する事象を 5 件観測した。新しい番号は開かない。**

---

### ① 冠詞・接頭辞の正規化（`NEXT_ACTIONS.md` §3b-2 / §3c-3 と同系統）

1. **衝突する canonical ID**: `cuvee:clos-de-la-coulee-de-serrant-nicolas-joly-coulee-de-serrant`
   （name = `Coulée de Serrant`）／`producer:clos-de-la-coulee-de-serrant-nicolas-joly`
2. **なぜミスマッチに見えるか**: OBP が印字するのは **`Clos de la Coulée de Serrant`**、
   canonical の cuvée 名は **`Coulée de Serrant`**。**先頭に `Clos de la ` が付くかどうかだけの差**である。
3. **Evidence**: 🔍 `research/out/t-01/review.json` の 3 行が
   **`fuzzy_candidate` / score `0.7556` / why `"fuzzy name, producer unknown"`** で滞留。
   `detail.cuvee` は「**生産者が未確定のため、銘柄が一致しても確定しない**」。
   ✅ **公式の正式名は `« La COULÉE de SERRANT »` であり、`Clos de la` を含まない。**
   ✅ **`Clos de la Coulée de Serrant` は Demeter France の会員登録における所在地名として実在する。**
   🔴 **Batch 4（de Montille `Clos de Roi` / `Clos du Roi`）および Batch 6（Ramonet `Le Montrachet` /
   `Montrachet`）と同じ「冠詞・前置詞句の正規化」問題の第 3 形である。**
4. **OBP への影響**: 🔴 **3 本（$500 / $400 / $600、計 $1,500）が `unresolved`。**
5. **推奨（DO NOT EXECUTE）**: **matcher 側の正規化規則の拡張**（先頭 `Le`/`La`、`de`/`du`/`des`、
   そして `Clos de la ` のような接頭辞句の除去後に再照合）。**canonical のリネームではない。**
6. **Confidence: High**

---

### ② 生産者名 3 種の不一致（P 系。**ただし実体分裂ではない**）

1. **衝突する canonical ID**: `producer:clos-de-la-coulee-de-serrant-nicolas-joly`
2. **なぜミスマッチに見えるか**: canonical の表示名 **`Clos de la Coulée de Serrant (Nicolas Joly)`** は、
   **公式サイトのどこにも存在しない合成文字列**である。
3. **Evidence**:
   - ✅ **法人名は `SAS Famille JOLY`**（公式 `mentions-legales`、Agence Bio 登録簿ともに一致）
   - ✅ **サイト上の自称は `La Coulée de Serrant`**
   - ✅ **`Clos de la Coulée de Serrant` は Demeter の所在地名としてのみ実在**
   - 🔍 **OBP 印字は `Famille Joly`** で、**これは法人名そのもの**である
   - 🔍 intake の `producer_state` は **`alias`** で、evidence は
     「**『Famille Joly』は Nicolas Joly / Virginie Joly の現行呼称**」
   - 🔴 🔍 **ただし `research/store/t-01/shells.json` の生産者シェル
     `rs:pro:fc888e1c58211837` は `canonical: {}` を持つ。**
     **すなわちワークスペース側では生産者が canonical に束ねられていない。**
     `obp_intake_normalized_20260804.json` の `producer_state = alias` と**状態が一致していない。**
4. **OBP への影響**: **5 本すべて**（cuvée 判定が「生産者未確定」で止まる直接原因）。
5. **推奨（DO NOT EXECUTE）**: **canonical の表示名を法人名（`Famille Joly`）に寄せるか、
   `Clos de la Coulée de Serrant` を alias として保持するかの設計判断。**
   **`Nicolas Joly` を表示名に含める根拠は公式に無い**（公式は彼を著者としてしか扱わない）。
   🔴 **加えて、intake と research workspace の生産者解決状態の不一致そのものを点検すべきである。**
6. **Confidence: High**（名称）／**Medium**（状態不一致の原因は本調査では特定していない）

---

### ③ `Les Vieux Clos` が canonical に存在しない（**衝突ではなく被覆の欠落**）

1. **衝突する canonical ID**: 該当なし。**`Clos de la Coulée de Serrant (Nicolas Joly)` 配下の
   キュヴェは `Coulée de Serrant` と `Clos de la Bergerie` の 2 件のみ。**
2. **なぜ問題か**: 🔴 **OBP に 2 本ある `Les Vieux Clos` に対応する canonical キュヴェが無い。**
   逆に **canonical が持つ `Clos de la Bergerie` は OBP に 1 本も無い。**
   **重なっているキュヴェは 3 つ中 1 つだけである。**
3. **Evidence**: ✅ 公式 `presentation` が生産する 3 ワインを明示。
   🔍 intake evidence:「**'Clos de la Coulée de Serrant (Nicolas Joly)' の canonical キュヴェ 2 件に
   一致無し: 'Les Vieux Clos'**」。
   🔍 `mapping.json` の 2 行は `research_shell`（`rs:pro:fc1686e9012e8c26`）で `canonical: {}`。
4. **OBP への影響**: **2 本（$240 / $200）が `unresolved`。**
5. **推奨（DO NOT EXECUTE）**: **`Les Vieux Clos`（AOC Savennières、5,5 ha、年産 15 000〜20 000 本）の
   canonical 追加。** 本書は追加していない。
6. **Confidence: High**

---

### ④ ヴィンテージの完全な非交差

1. **canonical ID**: `clos-de-la-coulee-de-serrant-coulee-de-serrant-2021` ／
   `clos-de-la-coulee-de-serrant-clos-de-la-bergerie-2021`
2. **なぜ問題か**: 🔴 **canonical に存在するヴィンテージは 2021 の 2 件だけ。
   OBP の 5 本は 2023 / 2020 / 2023 / 2019 / 2012 で、1 年も重ならない。**
   **`vintage_state` は 5 行すべて `unresolved`。**
3. **Evidence**: 🔍 上記 2 レコードのみ。
   ✅ **Demeter France の会員登録により、OBP の 5 ヴィンテージがいずれも実在することは確認済み**
   （§Important Cuvées）。**したがってこれは「存在しない年を載せている」問題ではなく、
   純粋に canonical のヴィンテージ被覆の問題である。**
4. **OBP への影響**: **5 本すべて。**
5. **推奨（DO NOT EXECUTE）**: **ヴィンテージ行の追加。** 本書は追加していない。
6. **Confidence: High**

---

### ⑤ canonical の散文が保持している未検証の主張（**`facts.subregion` の罠と同型**）

1. **canonical ID**: `clos-de-la-coulee-de-serrant-coulee-de-serrant-2021`
2. **なぜ問題か**: 🔴 **canonical の `description` / `obp_note` は出典の無い散文を製品側へ運んでいる。
   本調査で照合した結果、確認できたもの・できなかったもの・誤っているものが混在する。**
3. **Evidence（照合結果）**:

| canonical の主張 | 判定 |
|---|---|
| 7 ha のモノポール、自前の appellation を持つ | ✅ **確認**（公式「monopole de la famille Joly」＋INAO の独立 AOC）。⚠️ **面積の INAO 値は 6 ha 87 a** |
| Joly 家の単独所有 | ✅ **生産者が明言**。⚠️ **INAO の cahier des charges は所有者に言及しない**（appellation 規定は所有と無関係） |
| 1130 年、シトー会修道士が植えた急斜面 | ✅✅ **公式と INAO の双方で確認** |
| 1984 年以来ビオディナミ | ✅ **確認**。⚠️ **ただし公式内部に 1980 / 1981 / 1984 の揺れ** |
| 馬と手作業による耕作 | ✅ **確認**（**馬は 1 ha 半。全面ではない**） |
| 天然酵母 | ✅ **確認**（`levure indigène`） |
| 清澄・濾過は最小限 | ✅ **確認**（`Pas de collage`／`pré-filtration`） |
| 🔴 **「樽での緩やかな発酵と長期熟成」／`extended aging`** | 🔴 ⚠️ **誤り。公式は樽熟 6〜8 か月と明記。長期樽熟ではない。**（発酵が 2〜4 か月に及ぶのは事実） |
| `classification = "Savennières Coulée de Serrant AOC"` | 🔴 ⚠️ **旧称。** **INAO の 2014 年改正で `Coulée de Serrant` へ改称されている** |
| `subregion = "Savennières"` | ⚠️ 🔴 **村としては正しいが、appellation としては誤りを誘発する。**`Clos de la Bergerie`（Roche aux Moines）も同じ `subregion` を持つため、**3 つの異なる AOC が 1 つの文字列に潰れている。** 🔴 **Pride Mountain（`NEXT_ACTIONS.md` §3b-1）および Bordeaux の `facts.subregion` の罠と同じ形。** OBP intake 側の `_parts.appellation` も 5 行すべて `savennieres` に潰れている |
| `serving_temp = "12–14°C"` | ⚠️ **公式は「最低 13 ℃、14/15 ℃を推奨」。canonical のほうが低い** |
| `drinking_window` / テイスティングノート / `Market price from $100` | ❓ **公式に典拠が無い。生産者は官能記述も価格も公開していない** |

4. **OBP への影響**: **直接の解決阻害はない。** 🔴 **ただし `classification` の旧称と
   `subregion` の平坦化は、そのまま製品面に出れば誤情報になる。**
5. **推奨（DO NOT EXECUTE）**: **① `classification` を `Coulée de Serrant AOC` に更新するか否か
   （旧称を alias として残すか）の判断。② `extended aging` の記述の撤回。
   ③ appellation を `subregion` とは別のフィールドで持つかというモデル判断
   —— これは Pride Mountain と同じ議題であり、本書では開かない。**
6. **Confidence: High**（①②）／**Medium**（③はモデル判断）

---

## Sources

### 🔴 サイト真正性の事前確認（**Batch 6–7 の 4 件の偽サイト事故を受けた必須手順**）

**`https://coulee-de-serrant.com/` を公式と判定した根拠は 4 つで、要求される 4 条件すべてを満たす。**

| 条件 | 確認内容 |
|---|---|
| **(a) 法的告知** | ✅ **`/mentions-legales/` が実在し、事業者を名指ししている** ——「**Propriétaire : Famille JOLY – SAS Famille Joly（Siret 40371449600011）– CHATEAU ROCHE AUX MOINES 49170 SAVENNIERES**」。**知的財産・責任制限・個人情報の各条項が完備し、ファンページの免責文言は一切ない** |
| **(b) 認証機関からの相互リンク** | ✅ **Demeter France の会員ページ `demeter.fr/adherents/s-a-s-famille-joly/` が `http://www.coulee-de-serrant.com` を掲出している。** ✅ **Agence Bio 登録簿の `siteWebs` にも同 URL が `typeSiteWeb = "Site Officiel"` として登録されている** |
| **(c) 公的登録簿と一致する住所** | ✅ **Agence Bio: `JOLY VIRGINIE CHÂTEAU DE LA ROCHE AUX MOINES / 49170 SAVENNIERES` および `7 CHEMIN DE LA ROCHE AUX MOINES`。** **mentions légales の住所、Demeter の住所と一致。SIRET も一致** |
| **(d) 商用・法務フッタの整合** | ✅ **全ページのフッタが `Mentions légales` / `Politique de cookies (EU)` / `Copyright 2026 © La Coulée de Serrant`。** **Hébergeur は OVH（Roubaix）。カーヴ営業時間・訪問案内・メールアドレス `info@coulee-de-serrant.com`（Agence Bio 登録の email と一致）** |

🔴 **真正性で却下したサイト: なし。**
⚠️ ただし **`renaissance-des-appellations.com`（フッタの「Partenaires」リンク先）は
Nicolas Joly が率いる国際的な団体のサイトであり、ドメーヌのサイトではない。
本ドシエはこのサイトを一切参照していない。団体側の事実を語る必要が生じた場合にのみ、
「団体の資料」として明示的に区別して引用すべきである。**
⚠️ **同様に、`/les-livres-de-nicolas-joly/`（10 言語 44 ページ）は著書の紹介であり、
著書の内容は公式サイトの記述ではない。本ドシエは著書からの主張を一切取り込んでいない。**

### 一次資料 ①：生産者公式サイト `https://coulee-de-serrant.com/`

| ページ | 取得した情報 |
|---|---|
| `robots.txt` → `sitemap_index.xml` → `page-sitemap.xml`（36 URL）/ `post-sitemap.xml`（44 URL）/ `featured_item-sitemap.xml`（44 URL） | 走査の起点。**WordPress + Yoast。ページ全体の列挙** |
| 🔴 **`/presentation/`（FR）** | 🔴 **「3 つの異なる appellation の 3 ワイン」の定義。** 各ワインの畑・収量・生産本数・醸造の概要。**「成熟と酸化を区別せよ」。料理との合わせ方。** ⚠️ **EN 版 `/en/presentation-wines/` は機械翻訳が劣化しており数値も一部食い違う** |
| 🔴 **`/fiche-technique/`（FR）** | 🔴 **3 ワインの完全なデータ**（面積・傾斜・樹齢・密度・品種・土壌・収量・生産本数・ビオディナミ開始年・樽・酵母・補糖・soutirage・バトナージュ・濾過・sulfitage）**。銅・硫黄の使用量。収穫の tri 回数と時期。1130 年シトー会。** ⚠️ **EN 版 `/en/technical-sheet/` は内容が大幅に少なく、面積も一致しない** |
| 🔴 **`/actes-agricoles/`（FR）／`/en/statutes-of-the-vineyards-of-coulee-de-serrant/`** | 🔴 **栽培実務の全項目**（牛 10 頭＋雄牛 2 頭の堆肥、草生、除草剤 20 年不使用、最小耕耘、ウェサン羊、移動式鶏小屋、巣箱、ティザーヌ 11 種、銅 3〜5 kg、乳清、荒地の保全、セレクション・マサル、剪定、収穫）。**「1984 年以来 全体がビオディナミ」「3 つのワインと 3 つの AOC すべてに関わる」** |
| 🔴 **`/au-cellier/`（FR）** | 🔴 **醸造で行わないことの全リスト**（デブルバージュ、冷却、relevurage、清澄、温度管理）。**新樽 3〜4 %。soutirage と酸素。SO₂ の考え方。残糖 2 g 未満・14,5 度超で 4〜5 g。酸度 4〜5。マロは必ずしも起きない。サービス温度と抜栓** |
| **`/charte/`（FR）／`/en/charter/`** | **品質憲章の 3 段階（全 15 項目）。「われわれのワインはすべて 3 段階を守る」** |
| **`/histoire-de-la-coulee-de-serrant/`（FR）** | **1130 年の植樹、887 回目の連続収穫（2017）、旧修道院が歴史記念物目録に登録、1214 年の戦い、「英国人の墓地」と呼ばれる 300 m の城壁道、Louis XI「la goutte d'or」、Curnonsky** |
| **`/mentions-legales/`** | 🔴 **法人名・SIRET・住所・Virginie Joly の 3 役・ホスティング（OVH）** |
| **`/contact/`** | **営業時間（日曜・仏祝日を除く毎日 9:00-12:00 / 14:00-17:30）、試飲カーヴ、畑と庭の自由散策路、10 名超は要連絡** |
| **`/les-plats/`** | **公式の料理 6 種と標語** |
| **`/le-cheval/`** | **馬を入れることの理由（生産者の農学哲学。数値情報は無い）** |

### 一次資料 ②：公的登録簿・認証機関

| 資料 | 取得した情報 |
|---|---|
| 🔴 **Agence Bio 公開 API（フランス国）`opendata.agencebio.org/api/gouv/operateurs/?siret=40371449600011`** | 🔴 **`SAS FAMILLE JOLY` / `numeroBio 148071` / NAF `01.21Z` / 住所 2 件 / `datePremierEngagement = 1995-03-15` / 認証機関 `Certipaq Bio`（`FR-BIO-09`）/ `etatCertification = ENGAGEE` / `dateNotification 2004-05-14` / `dateEngagement 2022-05-04` / `mixite = Non` / 生産項目ごとの AB 状態（2025 管理年）** |
| **Certipaq Bio 事業者ページ（事業者番号 58522）** | **証明書 `FR-BIO-09.250-0084025.2025.002`、有効期間 `10/12/2025 – 31/03/2027`。2021〜2025 の旧証明書** |
| 🔴 **Demeter France `demeter.fr/adherents/s-a-s-famille-joly/`**（`adherents-sitemap.xml` 993 URL から特定） | 🔴 **会員登録。3 ワインを AOP 別に列挙し、Demeter 表示のヴィンテージ一覧を公開している。所在は `Clos De La Coulée De Serrant`** |
| ⚠️ **Biodyvin `biodyvin.com/sitemap.xml`** | **19 URL のみで会員一覧を含まない。加盟の有無は判定できなかった** |

### 一次資料 ③：INAO（原産地呼称の法定文書）

| 資料 | 取得した情報 |
|---|---|
| 🔴 **`extranet.inao.gouv.fr/fichier/CDCSAVENNIERESCOULEEDESERRANT.pdf`（12 頁・真正な PDF）** | 🔴 **AOC `Coulée de Serrant` の cahier des charges（2014-09-11 PNO 版）。** 名称・品種・区画（3 区画の実面積）・密度・剪定・収量（30 / butoir 35）・最低アルコール・地理と地質・**1130 年シトー会・1809/1823/1845/1861 の引用・1887 フィロキセラ・1952 décret・2011 年 11 月 homologation と `Coulée de Serrant` への改称**・官能記述・輸出比率 |
| **`extranet.inao.gouv.fr/fichier/3.15-CDC-Savennières-modifié.pdf`（13 頁）** | **AOC `Savennières` の cahier des charges（2018-09-06 PNO 版）。1952-12-08 の décret による認定。品種 chenin B のみ。収量 secs/demi-secs 50 hl/ha。官能記述** |
| **`extranet.inao.gouv.fr/fichier/PNOCDCSavennieresCouleeDeSerrant.pdf` / `PNOCDCSavennieresRocheAuxMoines.pdf`** | **各 1 頁の表紙（「fédération viticole de l'Anjou et de Saumur による認定提案」）** |
| **`www.inao.gouv.fr/produit/savennieres-roche-aux-moines-16953`** | **AOC 認定 2011 年、lieu-dit は約 35 ha、12 世紀に Saint-Nicolas d'Angers 修道院の修道士が拓いた clos、1214 年の戦い、官能記述** |

**取得できなかったもの / 存在しなかったもの**
- 🔴 **`www.inao.gouv.fr/produit/coulee-de-serrant-13353` が HTTP 403 を返し続けた**（`/produit/13353` は 404）。
- 🔴 **INAO extranet は存在しないファイル名に対しても HTTP 200 で HTML を返す。**
  `PNOCDC-Savennieres-Coulee-de-Serrant.pdf` など**ハイフン付きの 5 変種はすべて「Fichier non trouvé」の HTML** だった。
  **ハイフンを持たない `PNOCDCSavennieresCouleeDeSerrant.pdf` / `CDCSAVENNIERESCOULEEDESERRANT.pdf` が正しい。**
- 🔴 **`CDCSAVENNIERESROCHEAUXMOINES.pdf` は存在しない**（Roche aux Moines の完全な cahier des charges は未取得）。
- **EU の `eAmbrosia` 登録簿は SPA で、静的取得では中身が返らない。**
- **公式サイトにヴィンテージ一覧・キュヴェ別ページ・テイスティングノート・PDF テクニカルシートは存在しない。**
- **Joly 家がこの畑を取得した年、世代数、当主の交代の記録はどの一次資料にも無い。**

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔴 **canonical レコード 2 件**（`…-coulee-de-serrant-2021` / `…-clos-de-la-bergerie-2021`）／
**OBP 5 本**（すべて `match_state = unresolved`、`producer_state = alias`、
`cuvee_state` / `vintage_state` ともに `unresolved`。セクションは全て `FRANCE | WHITE > LOIRE`、
`beverage_menu_bottles.doc` の 729〜733 行）／
`research/out/t-01/mapping.json`: **2 行が `research_shell`、3 行が `review_item`**／
`research/store/t-01/shells.json`: **生産者シェル `rs:pro:fc888e1c58211837` は `canonical: {}`**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | **High** | 🔴 **法人名・SIRET・住所・サイト運営者・公的登録番号・認証機関がすべて一次で確定。** ⚠️ **Nicolas Joly の役職だけが空白** |
| **Overview** | **High** | 🔴 **3 ワイン＝3 appellation の構造を、生産者・INAO・Demeter の三者一致で確定した** |
| **History** | **Medium-High** | 🔴 **1130 / 1214 / 1887 / 1894 / 1952 / 1980 / 1984 / 1985 / 1995 / 2011 / 2014 が一次で取れた。** ⚠️ **Joly 家の取得年・世代が完全に空白** |
| **Location** | **High** | 🔴 **INAO が 3 区画の実面積・地質・気候を、生産者が土壌深さ・傾斜・樹齢・密度を与えている。**⚠️ 面積は 7 ha（生産者）と 6 ha 87 a（INAO）で食い違う |
| **Farming** | 🔴 **High** | 🔴 **本ドシエで最も厚い節。** 実務は全項目が公式。**認証は国の登録簿＋Certipaq＋Demeter の 3 経路で確定した。** ❓ **Demeter 開始年のみ不明** |
| **Winemaking** | **High** | 🔴 **「行わないこと」の全リストと、樽・酵母・熟成期間・残糖・酸度が公式。**⚠️ **soutirage 回数と新樽比率で公式内部が矛盾。SO₂ は単位不明** |
| **Style** | **Medium** | ✅ **生産者の「成熟 vs 酸化」の立場、サービス、料理は一次。**🔴 ⚠️ **キュヴェ別・年別の官能記述は生産者が一切公開していない。**代わりに **INAO の appellation 官能記述**を置いた |
| **Important Cuvées** | 🔴 **High** | 🔴 **5 本すべてについて、生産者の正式名・真の AOC・ヴィンテージの実在を確定した。**🔴 **3 本の appellation 誤記を検出した** |
| **Staff Notes** | **High** | ⚠️ **14 項目。** 🔴 **「サヴニエールと言ってしまう」「40 hl/ha」「Clos de la を復唱する」「長期熟成」という 4 つの実害ある誤りを塞いだ** |
| **Canonical Conflict** | **High** | 🔴 **5 件を、既存カテゴリに紐づけて escalate。新規番号は開いていない** |
| **総合** | 🔴 **High — staff-usable（70% を大きく超過。実質 88% 程度）。** | **OBP 掲載 5 本すべてについて、正式名・真の appellation・畑データ・収量・醸造・農法・認証・ヴィンテージ実在を言える。** 欠けているのは **① Joly 家の取得史 ② Demeter 認証の開始年 ③ 年別の官能記述** の 3 点で、**いずれもソムリエが嘘をつく原因にはならない。** |

**reached_70: YES.**

---

## Open Questions

1. 🔴 **`Clos de la Coulée de Serrant` はラベルにどう印字されているのか。**
   **生産者のサイトは `« La COULÉE de SERRANT »` としか書かず、`Clos de la` を含まない。**
   **一方 Demeter の会員登録は所在地名として `Clos De La Coulée De Serrant` を使い、
   OBP メニューもこの形で印字している。**
   → **実ボトルのラベル、または輸入元のテクニカルシートでの確認が要る。**
   🔍 **これは matcher の正規化規則を決める前提になる。** → §Canonical Conflict ①
2. 🔴 **Demeter 認証の開始年が不明。**
   **Demeter France の会員ページに年の記載が無く、生産者サイトは認証機関名すら書かない。**
   **有機側は Agence Bio の `datePremierEngagement = 1995-03-15` が取れている。**
   → **Demeter France への照会、または証明書の実物が要る。**
3. ⚠️ **Joly 家がこの畑を取得した年、および世代数。**
   **公式サイトにも INAO にも記載が無い。** INAO は「数世紀にわたり Château de Serrant の所有」
   「1894 年の再植後、歴代の所有者が耕作を続けた」としか書かない。
   → **生産者への直接照会が要る。**
4. ⚠️ **収量の認可値が公式（40 hl/ha）と INAO（30 hl/ha、butoir 35）で食い違う。**
   🔍 **PDF のフォント走査により、収量値が 2014 年改正の対象でないことは確認した。**
   **したがって公式サイトの記述のほうが古い可能性が高いが、断定していない。**
   → **現行 homologué 版（Legifrance または BO-Agri の consolidated 版）での確認が要る。**
5. ⚠️ **INAO 製品ページ `www.inao.gouv.fr/produit/coulee-de-serrant-13353` が HTTP 403。**
   **AOC の現行の正式名称表記・面積統計・ODG 情報が未取得。**
   → **ブラウザ描画で取得できる可能性がある。**
6. ⚠️ **`Les Vieux Clos` の面積と生産本数が公式内部で 3 通り**（5,5 ha / 20 000 本、15 000 本、3 ha）。
   → **どれが現行かの確認が要る。**
7. ⚠️ **soutirage の回数と新樽比率が公式内部で矛盾**（「増やす」対「1〜2 回」、「3〜4 %」対「5 % 以内」）。
8. ⚠️ **SO₂「各 soutirage ごとに約 2 g」の単位が書かれていない**（g/hL と推定されるが断定しない）。
9. ⚠️ **`Clos de la Bergerie`（AOC Savennières Roche aux Moines）の cahier des charges 全文が未取得。**
   **`CDCSAVENNIERESROCHEAUXMOINES.pdf` は存在せず、正しいファイル名が分かっていない。**
   🔍 **OBP に該当行が無いため優先度は低い。**
10. 🔴 🔍 **intake（`producer_state = alias`）と research workspace（生産者シェルの `canonical: {}`）で
    生産者の解決状態が一致していない。** **どちらが正なのか、なぜ分岐したのかは本調査では特定していない。**
    → §Canonical Conflict ②
11. ⚠️ **Nicolas Joly の現在の役割。**
    **公式サイトは彼を著者としてしか扱わず、`mentions légales` に現れる個人名は Virginie Joly のみである。**
    🔴 **第三者記事・著書・講演からこれを補うことは、本 workflow では禁じられている。**
