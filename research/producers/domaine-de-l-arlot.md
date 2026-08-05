# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にはこの生産者のレコードが 1 件しか無い**（`arlot-clos-des-forets-2021`）。
> 本書は昇格前の研究記録であり、**canonical には何も書き込んでいない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト arlot.com ／ 造り手署名入りテクニカルシート PDF で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では事実源として使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.arlot.com/`（EN / FR）**
> 走査元: 🔴 **`robots.txt` が指す `http://www.arlot.com/sitemap.php`**
> （`/sitemap.xml` は 404。**Pol Roger と同じ Vinium 製 CMS で、`sitemap.php` に切り替えて初めて 72 URL が列挙できる**）
> 認証の確認元: **Agence Bio 公開登録（opendata API）→ Ecocert France 証明書ページ**
>
> 🔴 **本ドシエ最大の収穫は 3 点。**
> **① OBP 掲載 5 本すべてが、公式サイトの該当ヴィンテージに実在すると確認できた。**
> **② $3,700 の `Romanée-Saint-Vivant Grand Cru 2023` は公式に実在する。**
> **さらに「Arlot がこのワインを造り始めたのは 1991 年から」という公式の限定まで取れた。**
> **③ OBP に載っていない `Clos de l'Arlot` を含め、モノポールが 4 ラベル確定した。**
> **`Clos du Chapeau` も公式にモノポールである**（これは事前想定と逆の可能性があった箇所）。
>
> 🔴 **もう 1 点、canonical に直結する発見。**
> **造り手自身が 2 通りの綴りを併用している。**
> **ウェブページは `Clos des Forêts Saint Georges`（ハイフン無し）、
> 同じワインの造り手署名入り PDF は `Clos des Forêts Saint-Georges Monopole`（ハイフン有り）。**
> → §Canonical Conflict `S-2`
>
> ⚠️ **調査上の制約 3 点**
> **① INAO extranet の 3 本（`PNOCDC-Nuits-Saint-Georges` / `-Romanee-Saint-Vivant` / `-Cote-de-Nuits-Villages`）は
> 事前警告どおり HTTP 200 で HTML を返し、PDF ではなかった。** 取得物は
> `_sources/domaine-de-l-arlot/NOT_A_PDF_inao_*.html` として保存。**本書に appellation 団体の一次資料は無い。**
> **② 親会社 AXA Millésimes のコーポレートサイト（`axamillesimes.com` トップ）は本セッションの環境から名前解決できなかった。**
> ただし **`wines.axamillesimes.com` のテクニカルシート配信は生きており、そこから取得している。**
> **③ `arlot.fr`（メールのドメイン）は HTTPS で応答しない。稼働している公式サイトは `arlot.com` である。**

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`L’Arlot`**（producer_heading。**アポストロフィは U+2019**） |
| **canonical 表記** | 🔍 **`Domaine de L'Arlot`**（大文字 `L`） |
| **公式表記** | ✅ 🔴 **`Domaine de l'Arlot`**（**小文字 `l`**。全ページの `<title>` が `… - Domaine de l'Arlot`） |
| 🔴 **法人** | ✅ **`SOCIETE CIVILE D'EXPLOITATION DU DOMAINE DE L'ARLOT`**（`/fr/mentions-legales`）。**RCS DIJON 341 179 430 ／ TVA FR 25 341 179 430** |
| **公的登録** | ✅ **SIRET `34117943000010`**（Agence Bio 公開登録。`raisonSociale` = `SOC CIVILE EXPLOITATION DOMAINE L'ARLOT`、`denominationcourante` = `DOMAINE DE L'ARLOT`） |
| **所在** | ✅ **21700 Prémeaux-Prissey（Côte-d'Or）。Nuits-Saint-Georges の南 2 km。** 登録上の本店は **`14 RD 974, 21700 PREMEAUX-PRISSEY`** |
| **連絡先** | ✅ **Tel +33 3 80 61 01 92 ／ contact@arlot.fr** |
| 🔴 **所有** | ✅ 🔴 **`AXA Millésimes`。1987 年初頭に Jules Belin の相続人から建物と畑が譲渡された。**（`/en/history`）**家族ドメーヌではない。** |
| **Managing Director** | ✅ **Christian Seely**（`/en/team`）。**2007 年 1 月に Jean-Pierre de Smet からドメーヌの指揮を引き継いだ** |
| 🔴 **Technical Director** | ✅ 🔴 **Géraldine Godot。2014 年 9 月から。** 公式が「**微生物学者にしてエノログ。ブルゴーニュ出身で、学業もキャリアの大半もこの地方**」と記す。**Dijon の Institut Jules Guyot で細胞生物学＋醸造学の修士**、**Beaune の Alex Gambal でマネージャー兼エノログ**、**チリ Bodega Las Niñas 滞在**。**全キュヴェの公式テイスティングノートに彼女の署名が入る** |
| **前任者** | ✅ **Jean-Pierre de Smet（約 20 年）→ Olivier Leriche → Jacques Devauges（2011 年 8 月）→ Géraldine Godot（2014 年 9 月）** |
| **公式サイト** | ✅ **`https://www.arlot.com/`**（EN / FR。`sitemap.php` に 72 URL） |
| 🔴 **有機認証** | ✅ **Ecocert France（`FR-BIO-01`）。Agence Bio 公開登録で `numeroBio 108745`、状態 `ENGAGEE`、`datePremierEngagement 2010-07-16`、直近の管理参照年 2026。**→ §Farming |
| canonical id | 🔍 🔴 **`arlot-clos-des-forets-2021` の 1 件のみ**（`producer = "Domaine de L'Arlot"`） |

---

## Overview

✅ **Nuits-Saint-Georges の南 2 km、Prémeaux-Prissey にある Côte de Nuits の古典的なブルゴーニュ所有地。**
公式トップの自己紹介 —「**コート・ド・ニュイの中心に位置する Domaine de l'Arlot は、
テロワールのニュアンスに敏感で、それをワインの純粋さを通して伝え、
例外的なブドウ栽培の遺産の守り手である。**」

🔴 ✅ **公式が掲げる哲学の一文は 1 つに集約される。**
「**テロワールを表現するブドウを育て、そこから生まれるワインを造ること。**
**自然を尊重して偉大なテロワールの真実を明らかにするこの視座が、Domaine de l'Arlot の哲学を定義する。
それは、醸造から élevage に至るまで、われわれが完全に引き受ける要求の厳しい選択を課す、
意志的で断固とした取り組みである。細部への周到な注意と、例外的なものを肯定しようとする強い意志を要求する、長期の視座である。**」

🔴 ✅ **THÉSEUS 的にいちばん重要な事実 —— これは家族ドメーヌではない。**
**1987 年初頭に `AXA Millésimes` へ譲渡され、現在まで同社の所有下にある。**
**Managing Director は Christian Seely、Technical Director は Géraldine Godot。**
→ §Staff Notes ⚠️ ①

🔴 ✅ **公式が繰り返す 3 つの醸造上の署名。**
**① 手摘み＋二重選果**（畑で 1 回、cuverie 到着時にもう 1 回）
**② 自然発酵**（「**ブドウを槽に入れれば、発酵は自然に始まる。すべては ressenti（感覚）に従って動く**」）
**③ ピジャージュは手作業、ルモンタージュは常に極めて限定的**

🔴 ✅ **有機栽培は marketing ではなく、認証機関の登録で裏が取れる数少ない例。**
**Ecocert France（`FR-BIO-01`）の登録が Agence Bio の公開データに存在し、
`raisin de cuve`（ワイン用ブドウ）と `vins de raisin`（ブドウ酒）の双方が `AB`（＝転換中ではなく認証済）状態にある。**
→ §Farming

🔍 **THÉSEUS における状態は悪い。canonical レコードは 1 件しかなく、
OBP 掲載 5 本のうち 4 本がキュヴェまたはヴィンテージのレベルで未解決。
その中に $3,700 の最高価格行が含まれる。**

---

## History

✅ **公式 `/en/history` から確定できる系譜。年表ページは静的取得できた**（Pol Roger と違い JS 描画ではない）。

| 年 | 出来事 ✅ |
|---|---|
| **18 世紀末** | 🔴 **`Jean-Charles Vienot`。**「**古い記録は、ブルゴーニュの長い家系の相続人であり、18 世紀末に Prémeaux 村に家と畑を所有していた Jean-Charles Vienot の存在を伝えている。彼は進取の人で、ドメーヌの周りに壁を築き、こうして `Clos de l'Arlot` を創り出した。それは今日 Nuits Saint Georges 1er Cru である。**」 |
| **19 世紀** | ✅ **息子 `François Vienot` が、古い採石場の窪地に「並外れた公園」を夢見た。**「**今日、百年を経た木々と、Jules Belin の依頼で多くの芸術家が彫った石が、この場所を寓話的な劇場とし、ブドウの畝の厳格さに対する心地よい対比を作り出している。**」 |
| 🔴 **1891** | 🔴 ✅ **ワイン商 `Jules Belin` に売却。**「**Belin は `Clos des Forêts Saint Georges` と `Clos du Chapeau` を購入して所有地を拡大し、その全体が Domaine de l'Arlot を形づくった。**」 |
| 🔴 **1987 年初頭** | 🔴 ✅ **Belin の相続人が建物と畑を `AXA Millésimes` に譲渡。**「**ほぼ 1 世紀の後、1987 年初頭に。**」 |
| **1987 以降** | 🔴 ✅ **AXA Millésimes が Vosne-Romanée に 2 区画を取得 —— `Vosne Romanée 1er Cru Les Suchots` と `Romanée Saint Vivant Grand Cru`。** |
| 🔴 **1990 / 1991** | 🔴 ✅ **RSV の由来。**「**1990 年まで、この畑は Aloxe-Corton 村のただ一人の造り手の手にあった。Domaine de l'Arlot がこのワインを造った最初のヴィンテージは 1991 年である。**」 |
| **2007 年 1 月** | ✅ **Jean-Pierre de Smet（約 20 年間ドメーヌを率いた）が `Christian Seely` に指揮を引き継ぐ。** |
| **2011 年 8 月** | ✅ **技術管理が Olivier Leriche から `Jacques Devauges` へ。** |
| 🔴 **2014 年 9 月** | 🔴 ✅ **技術管理が `Géraldine Godot` へ。現任。** |

✅ **公式の自己規定** —「**Domaine de l'Arlot はまず何よりも、ある生き方の影響力を象徴する場所である。
その強い identity は、ワインの長い歴史と、その悦びを分かち合いたいという明白な願いを映している。**」

⚠️ **ドメーヌの総面積、Vienot 家・Belin 家の詳細、AXA Millésimes の取得価格や経緯は公式に無い。**

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Bourgogne / Côte de Nuits** ✅ |
| **本拠** | ✅ **Prémeaux-Prissey、Nuits-Saint-Georges の南 2 km** |
| **総面積** | ❓ 🔴 **公式に記載が無い。本書では言わない。** |

### ✅ 区画ごとの公式記述（**面積が明記されているものだけを載せる**）

| 畑 | アペラシオン | 面積 ✅ | 公式の記述 |
|---|---|---|---|
| 🔴 **Clos des Forêts Saint Georges**（モノポール） | **Nuits-Saint-Georges 1er Cru** | 🔴 **7.2 ha、一枚地** | 🔴 「**ブルゴーニュにおいて monopole とは、何世紀にもわたって完全に画定され、ただ一人の所有者に属する土地の単位、テロワールを指す。**」「**Nuits Saint Georges の斜面の地質のレンジ全体を覆う —— 下部は Ladoix 石灰岩、中部は Premeaux 石灰岩、上部は白色魚卵状石灰岩。所によりオークルのシルトが顕著。この Clos は全面がピノ・ノワール。**」 |
| 🔴 **Clos de l'Arlot**（モノポール・赤） | **Nuits-Saint-Georges 1er Cru** | 🔴 **2 ha（赤）** | 🔴 「**Clos de l'Arlot は旧採石場の跡地に植えられている点で異例で、円形劇場の形をしている。名は区画の底から湧き、少し下で Courtavaux に注ぐ泉に由来する。**」「**上部は白色魚卵状石灰岩で若木、下部は `ostrea acuminata` を含むマルヌで古木の一部。**」🔴 「**Clos de l'Arlot 赤のキュヴェには最も古い木のブドウだけが入る。若木のワインは Nuits Saint Georges 1er Cru 名の `Cuvée Mont des Oiseaux` を成す。**」 |
| **Clos de l'Arlot**（モノポール・白） | **Nuits-Saint-Georges 1er Cru** | ⚠️ **面積の記載なし** | 「**Clos de l'Arlot blanc のテロワールは荒く岩がちである。斜面が急なため、通常は機械の助けを借りて行う作業がすべて手で行われる。**」 |
| 🔴 **Clos du Chapeau**（モノポール） | **Côte de Nuits-Villages** | 🔴 **1.6 ha** | 🔴 「**Comblanchien 村に位置する、帽子の形をした区画で、それが名の由来である。**」「**粘土と石灰の混じった土壌。**」🔴 「**アペラシオン Côte de Nuits Villages は 5 つの村 —— Fixin、Brochon、Prémeaux、Comblanchien、Corgoloin —— のブドウに関わる。この産地は 170 ha に及ぶ。**」 |
| **Les Suchots** | **Vosne-Romanée 1er Cru** | ⚠️ **記載なし** | 「**Romanée Saint Vivant、Echézeaux、Richebourg の間 …… この畑は世界最高のワインのいくつかと隣り合う。多くの尊敬される専門家が Les Suchots を Vosne Romanée の 1er Cru の中でも最上級と見なしている。**」 |
| 🔴 **Romanée Saint Vivant** | **Grand Cru** | ⚠️ 🔴 **記載なし** | 🔴 「**Romanée Saint Vivant の畑は見事な位置にあり、Romanée-Conti とは道 1 本で隔てられているにすぎない。粘土と石灰の混合が世界最高の赤の一つを生む、崇高な土地の上の途方もなく寛大な土。**」「**1098 年に創建された Cîteaux 修道院はブルゴーニュのブドウ畑の拡大に長く寄与した。Saint-Vivant de Vergy の修道士たちが深く関わり、Côte de Nuits の一つの畑が彼らの名を冠するに至った。**」 |
| **Mont des Oiseaux** | **Nuits-Saint-Georges 1er Cru** | ⚠️ **記載なし** | 「**Clos de l'Arlot —— ドメーヌのモノポール —— の最も若い木から少量だけ造られるキュヴェ。**」 |
| **Au Leurey**（白） | **Côte de Nuits-Villages** | **0.24 ha** | 「**Clos de l'Arlot の向かい。北／西という異例の向き。2006 年にシャルドネで植え替え。石灰岩の崖錐の上のシルト質土壌。**」 |
| **Le Mont / Le Mont（白）** | **Bourgogne Hautes-Côtes de Nuits** | **一枚地 1 ha**（うち **Chardonnay 0.66 ha・2012 年植栽**、**Pinot Noir 0.33 ha・2007 年植栽**） | 「**Prémeaux-Prissey 村の上、標高 400 m、南東向きの一枚地。われわれの Clos des Forêts Saint Georges のすぐ上、東向きの位置。**」**混植（co-planted）。** |
| **La Gerbotte**（白） | **Nuits-Saint-Georges** | ⚠️ **記載なし** | — |
| **Cuvée Le Petit Arlot** | **Nuits-Saint-Georges** | ⚠️ **記載なし** | — |
| **Cuvée Les Petits Plets** | **Nuits-Saint-Georges 1er Cru** | ⚠️ **記載なし** | — |

🔴 **モノポールは 4 ラベル（実質 3 つの clos）。**
**`Clos des Forêts Saint Georges` / `Clos de l'Arlot`（赤・白の 2 ラベル）/ `Clos du Chapeau`。**
🔴 **`Les Suchots` と `Romanée Saint Vivant` はモノポールではない。** → §Staff Notes ⚠️ ②

---

## Farming

🔴 ✅ **本ドシエで最も強く裏の取れた節。公式の主張と、認証機関側の登録の双方がある。**

### 公式サイトの記述（`/en/terroir` ／ `/fr/terroir`）✅

**「2000 年から有機的な実践、2014 年に AB 認証。ドメーヌは 2003 年に有機農法を開始し、
現在はすべての畑に拡大している。**
**目的はブドウ栽培への眼差しを変えること —— リズム、観察、感覚に基づく古い実践を適用することによって。**
**化学肥料と合成物質を捨てること。生命はふたたび動き出しうる。**
**ブドウの株は自然の均衡の中心にある。それは、区画固有の味と性格を帯びたブドウを実らせることを可能にする環境の中で育つ。**
**結果は明白である —— それがテロワールの真実を表現する最良の道だ。**」

⚠️ 🔴 **この一文は公式自身の中で微妙にずれている。**
**「2000 年から有機的実践」「2003 年に有機農法を開始」「2014 年に AB 認証」の 3 つの年が並ぶ。**
**FR 版も同文（`Avec des pratiques bio depuis 2000 et une certification AB en 2014, le domaine a initié l'agriculture biologique en 2003`）。**
→ **どれか 1 つを単独で「有機に転換した年」として言ってはならない。** → §Staff Notes ⚠️ ④

### 🔴 認証機関側の記録（**marketing ではなく公的登録**）✅

| 項目 | 値 |
|---|---|
| 登録 | 🔴 **Agence Bio 公開登録（`opendata.agencebio.org`）** |
| `numeroBio` | **108745** |
| SIRET | **34117943000010** |
| 🔴 **認証機関** | 🔴 **`Ecocert France`（EU 管理番号 `FR-BIO-01`）** |
| 🔴 **状態** | 🔴 **`ENGAGEE`（有効）。`dateSuspension` / `dateArret` はいずれも null** |
| 🔴 **最初の engagement** | 🔴 **`2010-07-16`**（`datePremierEngagement` ＝ `dateEngagement`。notification は `2010-07-29`） |
| 管理参照年 | **2026**（直近更新 `dateMaj 2025-02-04`） |
| 生産区分の状態 | 🔴 **`Raisin de cuve`（ワイン用ブドウ）= `AB` ／ `Vins de raisin`（ブドウ酒）= `AB` ／ 休閑地 = `AB`。すべて `AB` であり、転換中（C1/C2）ではない** |
| 活動 | **Production ＋ Préparation**（＝栽培だけでなく醸造も認証範囲） |
| 証明書 | ✅ **Ecocert 証明書ページが実在。`Certification Agriculture biologique Europe (EU) 2018/848`。住所は `14 RD 974, 21700 PREMEAUX PRISSEY`** |

⚠️ 🔴 **公式サイトの「2014 年に AB 認証」と、登録上の `datePremierEngagement 2010-07-16` は同じ数字ではない。**
🔍 **フランスの有機転換は通常 3 年を要するため「2010 年に engagement → 2013/2014 に認証取得」という読み方は整合的だが、
それは推論であり、どちらの出典もそう書いてはいない。** → **本書では両方を並記し、断定しない。** → Open Questions 4

### ⚠️ ビオディナミについて（**ここを間違えると事故になる**）

🔴 ⚠️ **Domaine de l'Arlot はビオディナミの認証を受けていない。**

- ⚠️ **公式サイト全体で `biodynamic` の語は 1 か所にしか出てこない。** 該当は **2013 年 5 月 2 日のニュース `Compost`** の中の一節 —
  「**われわれの堆肥は牛糞で作り、発酵させたうえで**、**いくつかのビオディナミの材料（ノコギリソウ、カモミール、イラクサ、樫の樹皮、タンポポ、バレリアンを用いた調合剤）で強化する。**
  **まだ「新しい」状態、すなわち発酵がわずかしか進んでいない段階で撒き、動的な過程が土の中で続くようにする。**
  **毎年ブドウ畑の 3 分の 1 に撒き、施す区画を年ごとに回す。**」
- 🔴 ⚠️ **`Biodyvin` の公式会員リスト（`biodyvin.com/fr/liste-des-membres-biodyvin.html`）を取得して走査 → `Arlot` は 0 件。**
- 🔴 ⚠️ **`Demeter France` の adhérents サイトマップ（993 件）を走査 → `Arlot` は 0 件**（`de-sousa-charlotte` と `charlot-tanneux` の 2 件が誤ヒットしただけ）。
- ⚠️ **したがって「ビオディナミのドメーヌです」とは言えない。** 言えるのは
  **「有機認証（Ecocert）で、堆肥にビオディナミの調合剤を使っている」**まで。 → §Staff Notes ⚠️ ③

### ✅ 畑仕事について公式が書いていること

- 🔴 **馬耕（2013 年 5 月 3 日のニュース `Working the soil with horse-drawn tools`）** —
  「**Clos de l'Arlot のこの区画は斜度 30 度から 50 度あり、現代的な機械を入れることが絶対に不可能である。**
  **一年を通して、丘の上に据えたケーブルウインチで犂を引いて草を抑えている。**
  **しかし年に一度、春にブドウが生育を始める前に、冬のあいだに締まった土をほぐすために、古き良き動物の力を使う。**」
  ⚠️ 🔴 **これは Clos de l'Arlot の急斜面区画についての記述であり、「ドメーヌ全体を馬で耕している」とは書かれていない。**
- **収穫は手摘み。選果は畑と cuverie の 2 回。**✅
- **収量は区画ごとに抑える方針。**「**とりわけ収量が制限されるようにしている —— Clos du Chapeau については 1 ha あたり 35 hl に。**」✅
  ⚠️ 🔴 **ただし同じ Clos du Chapeau の 2023 年の fiche には `Yield = 53 hl/ha` と書かれている。**
  **35 hl/ha は方針の記述、53 hl/ha はその年の実測とみられるが、公式はその区別を説明していない。** → Open Questions 5

---

## Winemaking

### ✅ 公式が全体方針として書いていること（`/en/terroir`）

「**ワインの誕生に、適切な時にだけ、そしてできる限り少なく介入する —— それが Domaine de l'Arlot の醸造の基本規則である。**
**収穫の時、房は手で摘まれ、ブドウは 2 回選果される —— 畑で、そして cuverie に着いた時に —— 最良のブドウだけを残すために。**
**ブドウが槽に移されると発酵は自然に始まり、すべては ressenti（感覚）に従って進む。**
**赤ワインについては、ヴィンテージが許すときに収穫の一部が全房で仕込まれ、それがワインの優雅さに寄与する。**
**マセラシオンの間に採る方法は、テロワールに自らを語らせ、繊細に抽出すること。**
**ピジャージュは手で行い、ルモンタージュの回数は常に極めて限定的である。**」

「**赤ワインは醸造が終わった段階で樽に移され、白ワインについてはアルコール発酵の前に樽へ移される。**
**選ばれる木はフランスの樫の森に由来し、樽は élevage の間に味わいを保つために、軽いから極めて軽いトーストを受ける。**
**その élevage の間に、マロラクティック発酵が自発的に、季節のリズムに従って起こる。**
**このゆっくりとした熟成の段階は、細部に至る点検と監視を伴い、そこでは瓶詰めの正しい時を決めるために試飲が最も重要である。**」

### 🔴 OBP 掲載 5 本のヴィンテージ別の実データ（**造り手署名入り fiche technique PDF ＋公式ページ**）✅

| ワイン / VT | 醸造 | 熟成 | 収量・瓶詰め |
|---|---|---|---|
| 🔴 **Clos des Forêts Saint-Georges 2023** | 🔴 **除梗 100%／約 14 °C の低温プレファーメンテーション・マセラシオン 約 5 日／ステンレス槽で自生酵母による自然発酵 17 日、毎日ルモンタージュ** | 🔴 **フレンチオーク 228 L で 16 か月、うち新樽 40%／その後タンクで 1 か月半** | 🔴 **収量 40 hl/ha。2025 年 3 月 24–27 日に瓶詰め。**収穫 9/6–9/12、**ドメーヌ全体の収量 43 hl/ha** |
| 🔴 **Clos des Forêts Saint-Georges 2021** | ⚠️ **年別の詳細が無く、総称的な記述のみ** —「**伝統的な醸造 —— 手摘み、最小限の醸し、行き過ぎないルモンタージュとピジャージュ**」 | ⚠️ **「平均して樽で 15 か月、新樽は最大 50%、瓶詰め前にタンクで 3 か月」** | ⚠️ **収量・瓶詰め日の記載なし。**収穫 9/20–9/25 |
| 🔴 **Clos des Forêts Saint-Georges 2019** | ⚠️ **2021 と同じ総称記述** | ⚠️ **2021 と同じ（15 か月・新樽最大 50%・タンク 3 か月）** | ⚠️ **記載なし。**収穫 9/12–9/17 |
| 🔴 **Clos du Chapeau 2023** | 🔴 **除梗 100%／約 14 °C の低温マセラシオン 7 日／ステンレス槽で自生酵母 18 日、毎日ルモンタージュ** | 🔴 **228 L フレンチオークで 11 か月、うち新樽 30%／タンクで 1 か月半** | 🔴 **収量 53 hl/ha。2024 年 9 月 5–6 日に瓶詰め** |
| 🔴 **Romanée-Saint-Vivant 2023** | 🔴 **除梗 100%／🔴 木桶（wooden vats）で自生酵母による自然発酵 17 日、毎日ルモンタージュ**（**これだけがステンレスでなく木桶**） | 🔴 **228 L フレンチオークで 15 か月、うち新樽 40%／タンクで 1 か月半** | 🔴 **収量 45 hl/ha。2025 年 2 月 12 日に瓶詰め** |

🔴 ⚠️ **2023 年の 3 本はいずれも「除梗 100%」と明記されている。**
**全房を使ったとは書かれていない。** → §Staff Notes ⚠️ ⑤

⚠️ 🔴 **2021 と 2019 の fiche には、その年固有の醸造・熟成データが無い。**
**公式が載せているのは総称的な定型文であり、「新樽 40%」「16 か月」といった 2023 年の数字を
2021 / 2019 に当てはめてはならない。** → §Staff Notes ⚠️ ⑥

⚠️ 🔴 **アルコール度数（% vol）は 5 本のどの fiche にも記載が無い。生産本数も無い。**

### ✅ 参考（白の造り。OBP には無いが同じ蔵の対照として）

**Clos de l'Arlot blanc 2023** — 「**全房のダイレクトプレス／12 °C で 48 時間の低温デブルバージュ／
228 L フレンチオーク（新樽 20%）で自生酵母によるアルコール発酵**」「**バトナージュを行わずに 228 L 樽で 12 か月、
新樽 20%／タンクで 3 か月／2024 年 12 月 16 日瓶詰め／収量 36 hl/ha**」

---

## Style

### ✅ 造り手のワイン規定文（ヴィンテージ非依存）

| ワイン | 公式 |
|---|---|
| 🔴 **Clos des Forêts Saint Georges** | 「**明確に画定された性格をもつこのワインは、Nuits Saint Georges の畑の identity を完璧に体現する。カシスに香辛料のきいたブラックベリーが混じる複雑な香りが立ち上り、ヴィンテージによってはリコリス、レザー、ブラッドオレンジのより暗い調子を伴う。よく構築された口中は、豊かでよく包まれたタンニンによる緊密な骨格のまわりに、密度と力をもって自己を主張する。果実の優雅さ・強度・純度から来る魅力が、時とともに増していく。**」 |
| 🔴 **Clos du Chapeau** | 「**このワインはアペラシオン Côte de Nuits Villages を優美に擁護する。静かな野心をもつ —— ピノ・ノワールの繊細さを表現するという野心を。サワーチェリーと核果の調子を風に通すような颯爽とした香りを開き、しばしばクローヴ、白檀、時にカカオへと流れていく。機敏で軽快なこのワインは、胡椒とヴァニラの筆致を伴う赤い果実の実質を通して自己を肯定しながら、しなやかさと優雅さを引き出す。その性格ゆえにかなり若いうちから「果実の上で」楽しめるが、10 年ほどまでは熟成で良くなりうる。**」 |
| 🔴 **Romanée Saint Vivant** | 🔴 「**Romanée Saint Vivant を味わうことは常に特権である。それは自然と人間の傑作のそばにいることから生まれる稀な感情である。豪奢で堂々とした佇まいと、明るいルビーの色。ブケは、黒いチェリーからラズベリーのゼリー、そしてスミレを伴うブラックベリーのコーディアルへと移りゆく輝かしい豊かさをもつ。年を経ると下生えとレザーの調子が現れる。この巨大なワインは表現的な強度と深さをもつ。滑らかだが弛緩せず、絹のようだが構築があり、密だが優雅である。すべてが混じり合い結びついて、崇高な複雑さを作り出す。**」 |
| **Clos de l'Arlot（赤）** | 「**このワインの繊細さと優雅さは、抗いがたい即時の悦びの印象を伝える。ラズベリー、赤スグリ、チェリー、イチゴの調子が花のニュアンスと組み合わさった、輝かしく複雑なブケから始まる。**」 |
| **Les Suchots** | 「**繊細さ、豊かさ、複雑さ、調和がすべて集まり結びついて、この例外的なワインの完全さを示す。ビロードの手袋に包まれた鉄の手。**」 |

### 🔴 ✅ OBP 掲載 5 本の公式テイスティングノート（**すべて Géraldine Godot 署名**）

| ワイン / VT | ノート ✅ | 署名 |
|---|---|---|
| 🔴 **Clos des Forêts Saint-Georges 2023** | 「**香りは野性的で複雑な果実のアロマを、香辛料の調子とともに表現する。より筋肉質なワインという評判に忠実に、口中は密で、白胡椒と唐辛子の調子をもち、長く尾を引く余韻を残す。**」 | **Géraldine Godot, Technical Director（2025 年 2 月）** |
| 🔴 **Clos des Forêts Saint-Georges 2021** | 「**色は深く、香りは熟した果実のアロマを開く。複雑なブケは口中まで運ばれる —— 香辛料、花、果実の心地よい混淆。タンニンは絹のようで、繊細で、精確。余韻は優雅で清涼感がある。**」 | **Géraldine Godot, Technical Director（2023 年 4 月）** |
| 🔴 **Clos des Forêts Saint-Georges 2019** | 「**2018 年と同じく、このワインは美味な複雑さをもつ。最初のブケはフレッシュな果実、ブラッドオレンジ、マンゴー、イチゴ、チェリー、そして薔薇の爆発をもたらす。それから花と繊細に香辛料のきいたブケへ移る。口中は豊かで、アロマの後に柔らかく清涼なテクスチャーを保つタンニンが微かに続く。このワインの複雑さは、その豊かさと美しさをすべて引き出すために忍耐を要求する。余韻は寛大で gourmand。**」 | **Géraldine Godot, Technical Director（2021 年 6 月）** |
| 🔴 **Clos du Chapeau 2023** | 「**香りは純粋で、精確で、フレッシュ。カシス、赤いチェリー、イチゴのブケ。口中はジューシーで、エネルギッシュで、キレがある。表現的で、密で、肉付きがよく、その親しみやすさで人を惹きつけるワイン。**」 | **Géraldine Godot, Technical Director（2025 年 2 月）** |
| 🔴 **Romanée-Saint-Vivant 2023** | 🔴 「**壮麗なブケがグラスの中で開く —— 黒いチェリー、ヨードとスミレの気配、薔薇と芍薬。豊かで調和のとれたブケが、口中では精確で繊細なタンニンと並び立つ。長く、繊細で、力強い、魅力に満ちたワイン。**」 | **Géraldine Godot, Directrice Technique（2025 年 2 月）** |

### ✅ 公式の料理との合わせ方（**Clos du Chapeau と RSV にのみ記載がある**）

- 🔴 **Romanée-Saint-Vivant** — 「**このようなワインには、狙いを高く定めることを躊躇すべきではない —— トリュフソースの牛フィレ、canard à la presse、セップ茸の鶏。そして秋には lièvre à la royale がこの伝説的な赤に完璧に合うだろう。**」
- **Clos du Chapeau** — 「**この寛大で優雅な赤は jambon persillé やリヨンのソシソンによく合う。それ以上のこともでき、セップ茸を添えた肥育鶏、エシャロットのホロホロ鳥、仔牛の腎臓のグリルの素晴らしい相手になる。**」
- ⚠️ **Clos des Forêts Saint Georges の各ヴィンテージには料理の提案が付いていない。**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake、`beverage_menu_bottles.doc` 929–933 行。**全 5 本、`FRANCE | RED > BURGUNDY`、`producer_state = exact`**）

| # | OBP 印字 | VT | 価格 | ✅ **公式での確認結果** | 🔍 canonical |
|---|---|---|---|---|---|
| 1 | **'Clos du Chapeau,' Côte de Nuits Villages** | 2023 | **$210** | ✅ 🔴 **実在。公式名は `Clos du Chapeau Monopole`。**アペラシオンは造り手 PDF で **`AOC Côte de Nuits-Villages`**。**1.6 ha、Comblanchien、Pinot Noir 100%** | 🔴 **未登録**（canonical にキュヴェ自体が無い） |
| 2 | **'Clos des Forets Saint Georges,'** NSG 1er Cru | 2023 | **$515** | ✅ **実在。**公式のヴィンテージ一覧に 2023 あり。**16 か月・新樽 40%・収量 40 hl/ha** | 🔴 **未登録**（2021 のみ存在） |
| 3 | **'Clos des Forets Saint Georges,'** NSG 1er Cru | 2021 | **$515** | ✅ **実在。**⚠️ **年別の醸造データは公式に無く、総称記述のみ** | 🔍 ✅ **`arlot-clos-des-forets-2021` に一致（唯一の exact）** |
| 4 | **'Clos des Forets Saint Georges,'** NSG 1er Cru | 2019 | **$550** | ✅ **実在。**⚠️ **2021 と同じく総称記述のみ** | 🔴 **未登録** |
| 5 | 🔴 **Romanée-Saint-Vivant Grand Cru** | 2023 | 🔴 **$3,700** | 🔴 ✅ **実在を確認。公式ページ `/en/vin/9/romanee-saint-vivant` に 2023 があり、造り手署名入り fiche PDF のタイトルは `Romanée-Saint-Vivant Grand Cru, 2023` / `AOC Romanée-Saint-Vivant Grand Cru`。木桶発酵 17 日・新樽 40%・15 か月・収量 45 hl/ha・2025 年 2 月 12 日瓶詰め** | 🔴 **未登録** |

🔴 **5 本すべてについて、公式サイトに該当ヴィンテージが実在することを確認した。存在しない年を載せている行は無い。**
🔴 **バッチ 8 最大のリスク行だった $3,700 の RSV 2023 は、公式に裏が取れた。**

### ✅ 公式の全 13 ワイン（`sitemap.php` ＋ `/en/our-wines`）

| # | 公式名 | アペラシオン（公式サイト表記） | モノポール | 公式一覧の最新 VT |
|---|---|---|---|---|
| 1 | 🔴 **Clos des Forêts Saint Georges Monopole** ⭐OBP×3 | **Nuits Saint Georges 1er Cru** | 🔴 **○** | **2024**（1998–2024） |
| 2 | 🔴 **Clos du Chapeau Monopole** ⭐OBP | **Côte de Nuits Villages** | 🔴 **○** | **2024** |
| 3 | **Clos de l'Arlot (blanc) Monopole** | **Nuits Saint Georges 1er Cru** | 🔴 **○** | **2024** |
| 4 | **La Gerbotte (blanc)** | **Nuits Saint Georges** | — | ⚠️ **2020**（それ以降が無い） |
| 5 | **Cuvée Le Petit Arlot** | **Nuits Saint Georges** | — | ⚠️ **2014** |
| 6 | **Cuvée Les Petits Plets** | **Nuits Saint Georges 1er Cru** | — | ⚠️ **2014** |
| 7 | 🔴 **Clos de l'Arlot Monopole**（赤） | **Nuits Saint Georges 1er Cru** | 🔴 **○** | **2024** |
| 8 | **Les Suchots** | **Vosne Romanée 1er Cru** | ✕ | **2024** |
| 9 | 🔴 **Romanée Saint Vivant** ⭐OBP | **Grand Cru** | ✕ | **2024** |
| 10 | **Au Leurey (blanc)** | **Côte de Nuits Villages** | ✕ | **2024**（2015–） |
| 11 | **Le Mont (blanc)** | **Bourgogne Hautes-Côtes de Nuits** | ✕ | **2024**（2016–） |
| 12 | **Le Mont**（赤） | **Bourgogne Hautes-Côtes de Nuits** | ✕ | ⚠️ **2023** |
| 13 | **Mont des Oiseaux** | **Nuits Saint Georges 1er Cru** | ✕（**モノポールの若木から造るが、ラベルにモノポール表記なし**） | ⚠️ **2023** |

⚠️ 🔴 **`La Gerbotte` / `Cuvée Le Petit Arlot` / `Cuvée Les Petits Plets` は公式のヴィンテージ一覧が
それぞれ 2020 / 2014 / 2014 で止まっている。**
**ただし公式は「生産をやめた」とはどこにも書いていない。** → **「廃止された」と言ってはならない。** → Open Questions 6

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① Nuits-Saint-Georges の南 2 km、Prémeaux-Prissey。1987 年から AXA Millésimes が所有し、
2014 年 9 月から Géraldine Godot が技術責任者。**
「**ニュイ・サン・ジョルジュの南 2 km、プレモー・プリセにあるドメーヌです。**
**18 世紀末に Jean-Charles Vienot が畑の周りに壁を築いて `Clos de l'Arlot` を作り、
1891 年にワイン商の Jules Belin が買って `Clos des Forêts Saint Georges` と `Clos du Chapeau` を加え、
その全体が今の Domaine de l'Arlot になりました。**
**1987 年初頭に Belin の相続人から AXA Millésimes に渡り、現在も同社の所有です。**
**代表は Christian Seely、技術責任者は 2014 年 9 月からジェラルディーヌ・ゴド。**
**リストにあるワインのテイスティングノートは、すべて彼女自身の署名入りのものです。**」

**② モノポールは 3 つの clos。リストの `Clos du Chapeau` もモノポールです。**
「**このドメーヌはモノポール（単独所有畑）で知られています。**
**`Clos des Forêts Saint Georges`（7.2 ha、一枚地、ニュイ・サン・ジョルジュ 1er Cru、全面ピノ・ノワール）、**
**`Clos de l'Arlot`（旧採石場の跡地で円形劇場のような形。赤 2 ha と白があり、名は区画の底から湧く泉に由来します）、**
**そして `Clos du Chapeau`（コンブランシアンの 1.6 ha、帽子の形をした区画で、それが名の由来）。**
**リストの 210 ドルのコート・ド・ニュイ・ヴィラージュが、その 3 つ目のモノポールです。**
**一方で `Romanée-Saint-Vivant` はモノポールではありません。**」

**③ 3,700 ドルのロマネ・サン・ヴィヴァンは、造り手が 1991 年から造っている畑です。**
「**このドメーヌのロマネ・サン・ヴィヴァンは、造り手自身が『**1990 年までこの畑はアロース・コルトン村のただ一人の造り手の手にあり、
Domaine de l'Arlot が造った最初のヴィンテージは 1991 年である**』と書いています。**
**畑については『**ロマネ・コンティとは道 1 本で隔てられているにすぎない**』と。**
**2023 年は、このドメーヌで唯一、**ステンレスではなく木桶**で 17 日間、自生酵母で発酵させています。**
**新樽 40% で 15 か月、2025 年 2 月 12 日に瓶詰め。**」

### 追加で使える一手

- **Clos des Forêts Saint Georges（$515 / $550）**: 「**7.2 ha の一枚地で、ニュイ・サン・ジョルジュの斜面の地質のレンジ全体を覆います —— 下部が Ladoix 石灰岩、中部が Premeaux 石灰岩、上部が白色魚卵状石灰岩。全面ピノ・ノワールです。**
  **造り手の言葉では『明確に画定された性格をもち、ニュイ・サン・ジョルジュの identity を完璧に体現する』ワイン。**
  **2023 年は新樽 40% で 16 か月、収量 40 hl/ha。ゴド女史のノートは『より筋肉質なワインという評判に忠実に、白胡椒と唐辛子の調子』。**
  **2019 年は『2018 年と同じく美味な複雑さ』『ブラッドオレンジ、マンゴー、イチゴ、薔薇の爆発』と書かれています。**」
- **Clos du Chapeau（$210）**: 「**コンブランシアンの 1.6 ha のモノポール。造り手は『アペラシオン Côte de Nuits-Villages を優美に擁護する』ワインと表現しています。**
  **2023 年は樽 11 か月・新樽 30%。『若いうちから果実の上で楽しめるが、10 年ほどまでは熟成で良くなりうる』とのこと。**
  **jambon persillé やリヨンのソシソンを公式が薦めています。**」
- **栽培**: 「**有機です。Ecocert フランスの認証で、Agence Bio の公開登録にも載っています。**
  **造り手は『化学肥料と合成物質を捨てること。生命はふたたび動き出しうる』と書いています。**
  **堆肥は牛糞を発酵させ、ビオディナミの調合剤 —— ノコギリソウ、カモミール、イラクサ、樫の樹皮、タンポポ、バレリアン —— で強化し、毎年畑の 3 分の 1 に回して撒きます。**
  **クロ・ド・ラルロの斜度 30〜50 度の区画は機械が入らないので、年に一度、馬で耕します。**」
- **醸造の考え方**: 「**『ワインの誕生に、適切な時にだけ、できる限り少なく介入する』が基本規則。手摘み、畑と蔵で 2 回の選果、自生酵母の自然発酵、ピジャージュは手作業、ルモンタージュは常に極めて限定的。マロラクティックは季節のリズムに従って自発的に起こります。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／誤りやすい**）

1. 🔴 ⚠️ **「家族経営のドメーヌ」と言わない。** **1987 年初頭から `AXA Millésimes` の所有である。**
   **公式の history にそう書かれている。** 言うなら「**AXA Millésimes 所有のドメーヌ**」。
2. 🔴 ⚠️ **`Romanée-Saint-Vivant` と `Les Suchots` をモノポールと言わない。**
   **モノポールは `Clos des Forêts Saint Georges` / `Clos de l'Arlot`（赤・白）/ `Clos du Chapeau` の 3 つの clos だけ。**
   **逆に、$210 の `Clos du Chapeau` を「ただの村名格」と言うのも誤り —— 公式名は `Clos du Chapeau Monopole` である。**
3. 🔴 ⚠️ **「ビオディナミのドメーヌ」と言わない。**
   **`Biodyvin` の会員リストにも `Demeter France` の adhérents にも Arlot は無い**（双方の公式リストを走査して確認）。
   **公式サイトで `biodynamic` の語が出るのは、堆肥の調合剤についての 1 か所だけである。**
   言えるのは「**有機認証で、堆肥にビオディナミの調合剤を使っている**」まで。
4. 🔴 ⚠️ **有機転換の「年」を 1 つに絞って断定しない。**
   **公式は同じ一文の中で「2000 年から有機的実践」「2003 年に有機農法を開始」「2014 年に AB 認証」と 3 つの年を並べている。**
   **一方 Agence Bio の登録上の最初の engagement は `2010-07-16` である。**
   安全な言い方は「**Ecocert フランスの有機認証を受けている**」。年を言うなら**公式の 3 つを並べて引用する**。
5. 🔴 ⚠️ **2023 年のワインを「全房」と言わない。**
   **2023 年の 3 本（Clos des Forêts / Clos du Chapeau / RSV）の fiche はいずれも `100% destemming`（除梗 100%）と明記している。**
   **公式の総論には「ヴィンテージが許すときに収穫の一部を全房で」とあるが、それは方針であって 2023 年の実際ではない。**
6. 🔴 ⚠️ **2023 年の数字を 2021 / 2019 に流用しない。**
   **2021 と 2019 の fiche には年固有のデータが無く、「平均して樽で 15 か月、新樽は最大 50%、タンクで 3 か月」という総称記述しかない。**
   **「新樽 40%」「16 か月」「収量 40 hl/ha」は 2023 年の Clos des Forêts の数字である。**
7. 🔴 ⚠️ **アルコール度数を言わない。** **5 本のどの fiche にも `% vol` の記載が無い。**
8. ⚠️ **生産本数・希少性の数字を言わない。** **公式に一切記載が無い。**
9. ⚠️ **ドメーヌの総面積（「◯◯ ha のドメーヌ」）を言わない。**
   **公式に総面積の記載が無い。** 言えるのは**区画ごとの面積**（Clos des Forêts 7.2 ha、Clos de l'Arlot 赤 2 ha、Clos du Chapeau 1.6 ha、Au Leurey 0.24 ha、Le Mont 1 ha）だけ。
10. ⚠️ **`Clos du Chapeau` の収量を「35 hl/ha」と単独で言わない。**
    **35 hl/ha は公式の方針の記述だが、2023 年の fiche には `Yield = 53 hl/ha` とある。**
    **公式はこの差を説明していない。**
11. ⚠️ **「馬で耕しています」を全体に一般化しない。**
    **公式が馬耕を書いているのは `Clos de l'Arlot` の斜度 30〜50 度の区画についてであり、しかも「年に一度」である。**
    **通常はケーブルウインチで犂を引いている、と同じ記事に書かれている。**
12. ⚠️ **`La Gerbotte` / `Le Petit Arlot` / `Les Petits Plets` を「廃止された」と言わない。**
    **公式のヴィンテージ一覧が 2020 / 2014 / 2014 で止まっているだけで、公式は生産終了とは書いていない。**
13. ⚠️ **第三者点数を言わない。** **本調査で取得したどのページにも点数の掲載が無い。**
14. ⚠️ **Jean-Pierre de Smet 時代の逸話を語らない。**
    **公式が書いているのは「約 20 年間ドメーヌを率い、2007 年 1 月に Christian Seely へ引き継いだ」の一文だけである。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **新規の番号は開かない。既存の `S-2` / `C-1` の族に属する 2 件と、**
🔍 **「衝突ではなく欠落」が 1 件。**

---

### 【1】`S-2` — canonical キュヴェ名に二重引用符が埋め込まれている（**既知の族**）

1. **衝突する canonical ID**: `arlot-clos-des-forets-2021`
2. **なぜ問題か**: `name` フィールドの実値が **`"Clos des Forêts Saint Georges"`**（**先頭と末尾に `"` が literal で入っている**）。
   Batch 5–7 で 9 件見つかった **`S-2` 族と同型**。
3. **証拠**: 🔍 `migration/out/export/db_wine_canonical.json` の当該レコード —
   `"name": "\"Clos des Forêts Saint Georges\""`。
   ✅ 公式サイトの表記は **`Clos des Forêts Saint Georges Monopole`**（引用符なし）。
4. **OBP への影響**: OBP 側の印字は `'Clos des Forets Saint Georges,'` で、**シングルクォート＋カンマ**である。
   **引用符の種類が canonical と OBP で異なるため、文字列一致に頼る照合は破綻する。**
   現に 2023 / 2019 は `unresolved` のまま。
5. **推奨対応（DO NOT EXECUTE）**: `S-2` 族の一括正規化（引用符の剥離）と同時に処理する。**単独で修正しない。**
6. **Confidence**: **High**（実データを読んで確認した）。

---

### 【2】`S-2` 付随 — 🔴 **造り手自身が 2 通りの綴りを併用している（ハイフンの有無）**

1. **関係する canonical ID**: `arlot-clos-des-forets-2021`（`name` / `subregion` / `classification`）
2. **なぜ問題か**: 🔴 **同じワインについて、公式が 2 つの綴りを出している。**

   | 出典 | キュヴェ名 | アペラシオン |
   |---|---|---|
   | ✅ **公式ウェブページ** `/en/vin/1/…` | **`Clos des Forêts Saint Georges Monopole`**（**ハイフン無し**） | **`Nuits Saint Georges 1er Cru`**（**ハイフン無し**） |
   | ✅ 🔴 **造り手署名入り fiche PDF**（`wines.axamillesimes.com/N2UGUE/get/tech-sheet` 他） | 🔴 **`Clos des Forêts Saint-Georges Monopole`**（**ハイフン有り**） | 🔴 **`AOC Nuits-Saint-Georges Premier Cru`**（**ハイフン有り**） |
   | 🔍 **canonical** | `"Clos des Forêts Saint Georges"`（**ハイフン無し・`Monopole` 欠落**） | `Nuits-Saint-Georges Premier Cru`（**ハイフン有り**） |
   | 🔍 **OBP 印字** | `Clos des Forets Saint Georges`（**ハイフン無し・`ê` が `e`**） | `Nuits-Saint-Georges Premier Cru`（**ハイフン有り**） |

   **同じ現象が `Côte de Nuits-Villages` にもある** —— 公式ウェブは `Côte de Nuits Villages`、
   **造り手 PDF は `AOC Côte de Nuits-Villages`**、**OBP 印字は `Côte de Nuits Villages`**。
   **RSV も同様** —— 公式ウェブ `Romanée Saint Vivant`、**PDF `Romanée-Saint-Vivant Grand Cru`**、
   **OBP `Romanée-Saint-Vivant Grand Cru`**。
3. **証拠**: 上表のとおり。PDF は `_sources/domaine-de-l-arlot/tech_*.pdf` に保存済み。
4. **OBP への影響**: **アペラシオン文字列の正規化を「ハイフン無し」に寄せると INAO 表記から外れ、
   「ハイフン有り」に寄せると造り手のウェブ表記から外れる。**
   🔴 **OBP のアペラシオン印字は 2 種類が混在している**（`Côte de Nuits Villages` はハイフン無し、
   `Nuits-Saint-Georges Premier Cru` と `Romanée-Saint-Vivant Grand Cru` はハイフン有り）。
   **したがって OBP 側だけを見ても一貫した規則は導けない。**
5. **推奨対応（DO NOT EXECUTE）**:
   **アペラシオンは造り手 PDF が採用しているハイフン有りの AOC 正式形を canonical の正とし、
   ウェブ表記は alias として保持する。**
   **キュヴェ名の `Monopole` は名称の一部として扱うか属性として持つかを別途決める必要がある。**
   ⚠️ **appellation 団体（INAO）の一次資料は本調査で取得できなかったため、この推奨は「造り手 PDF に依拠した」ものである。**
6. **Confidence**: **High**（綴りの差は実物で確認）／**推奨の妥当性は Medium**（INAO 未確認のため）。

---

### 【3】🔴 **欠落 — canonical に 4 本分のレコードが無い（衝突ではない）**

1. **関係する canonical ID**: **無い。それが問題である。**
2. **なぜ問題か**: 🔍 **canonical の Arlot レコードは `arlot-clos-des-forets-2021` の 1 件のみ。**
   OBP に載る 5 本のうち **4 本が canonical に存在しない**。

   | OBP 行 | 状態 |
   |---|---|
   | `Clos du Chapeau` 2023（$210） | 🔴 **キュヴェ自体が canonical に無い** |
   | `Clos des Forêts Saint Georges` 2023（$515） | **キュヴェはあるがヴィンテージが無い** |
   | `Clos des Forêts Saint Georges` 2021（$515） | ✅ **唯一の一致** |
   | `Clos des Forêts Saint Georges` 2019（$550） | **ヴィンテージが無い** |
   | 🔴 `Romanée-Saint-Vivant Grand Cru` 2023（**$3,700**） | 🔴 **キュヴェ自体が canonical に無い。バッチ 8 最高額の行** |

3. **証拠**: 🔍 `db_wine_canonical.json`（928 件）を `arlot` で走査 → **Arlot 名義は 1 件**。
   🔍 `research/out/t-01/inventory.json` 929–933 行が OBP の 5 行。
4. **OBP への影響**: 🔴 **金額ベースで見ると、$4,890 のうち $515 分（10.5%）しか canonical に紐づいていない。**
5. **推奨対応（DO NOT EXECUTE）**: 本ドシエの §Important Cuvées にある**公式 13 ワインの一覧と、
   1998–2024 の公式ヴィンテージ一覧**をそのまま登録原簿として使える。
   **ただし登録は Akio / CTO 判断。本書では実行しない。**
6. **Confidence**: **High**。

---

### 【4】既存レコードの内容欠落（**参考。新規番号は開かない**）

🔍 **`arlot-clos-des-forets-2021` は `grapes` が空である。**
✅ **公式は全ヴィンテージで `Pinot Noir 100%` と明記しており、Clos des Forêts は「全面がピノ・ノワール」と書かれている。**
🔍 **`appellation_id` も `None`。**`subregion` と `classification` はともに文字列 `Nuits-Saint-Georges Premier Cru` で重複している。
🔍 **`description` / `obp_note` / `tasting` も無い**（同じ DB の `fornerol-*` レコードには存在する）。
→ **本書の §Style に公式ノート、§Winemaking に醸造データが揃っているので、埋める材料はある。**
→ **DO NOT EXECUTE。**

---

## Sources

**一次資料（公式サイト `https://www.arlot.com/` と、そこからリンクされた造り手署名入り fiche technique PDF）**

### 🔴 サイト真正性の検証（**必須手順**）

**`arlot.com` を公式と判定した根拠は 4 つ。**

| 検証 | 結果 |
|---|---|
| **(a) mentions légales に実在の法人名** | ✅ 🔴 **`/fr/mentions-legales` に `Propriétaire du Site Internet: SOCIETE CIVILE D'EXPLOITATION DU DOMAINE DE L'ARLOT`、`N° immatriculation RCS: 341 179 430 - DIJON`、`TVA: FR 25 341 179 430`。**ファンページ的な免責文言は一切無い |
| **(c) 公的登録との住所・識別子の一致** | ✅ 🔴 **Agence Bio 公開登録の `siret 34117943000010` は、mentions légales の RCS `341 179 430` と一致する**（SIRET ＝ SIREN 9 桁＋NIC 5 桁）。**登録上の本店 `14 RD 974, 21700 PREMEAUX-PRISSEY` は Ecocert 証明書ページの住所とも一致** |
| **(d) 商業・法的フッターの整合** | ✅ **全ページに酒類警告文、Cookie ポリシー、Axeptio 同意管理、制作会社 Vinium Luxury Webdesign（Aloxe-Corton）のクレジットがある** |
| **(補) 造り手ドメインからの配信** | ✅ 🔴 **各ワインページの fiche technique PDF は `wines.axamillesimes.com/<vincod>/get/tech-sheet` から配信されており、PDF のフッターは `Domaine de l'Arlot, 21700 Premeaux-Prissey / Tel. 03 80 61 01 92 / contact@arlot.fr / www.arlot.com`。** **所有者 AXA Millésimes のドメインとドメーヌのサイトが相互に噛み合っている** |

🔴 **なりすまし・偽サイトの却下は 0 件。**
**`domainedelarlot.com` / `domaine-de-larlot.com` / `domainedelarlot.fr` / `larlot.com` / `domaine-arlot.com` は
いずれも名前解決しなかった（`000`）ため、そもそも取得物が無い。保存すべき `NOT_THE_PRODUCER_*` ファイルは生じていない。**

⚠️ **`arlot.fr` は contact@arlot.fr のメールドメインとして公式に使われているが、
HTTPS では本セッションから応答しなかった。稼働している公式サイトは `arlot.com` である。**

### 取得した資料

| 資料 | 取得した情報 |
|---|---|
| 🔴 **`robots.txt` → `http://www.arlot.com/sitemap.php`** | 走査の起点。**`/sitemap.xml` は 404。** `sitemap.php` に **EN / FR 各 36、計 72 URL**（13 ワイン・11 ニュース・主要ページ） |
| 🔴 **`/en/history`** | 🔴 **Jean-Charles Vienot（18 世紀末・壁と Clos de l'Arlot の創出）、François Vienot（公園）、1891 年 Jules Belin（Clos des Forêts と Clos du Chapeau の追加）、1987 年初頭の AXA Millésimes への譲渡、Les Suchots と RSV の取得、de Smet → Seely（2007/1）→ Leriche → Devauges（2011/8）→ Godot（2014/9）** |
| 🔴 **`/en/terroir` ＋ `/fr/terroir`** | 🔴 **有機の記述（2000 / 2003 / 2014 の 3 年）、醸造の総論（二重選果・自然発酵・部分全房・手ピジャージュ・限定ルモンタージュ）、élevage の総論（赤は醸造後・白は AF 前に樽へ、フレンチオーク、軽〜極軽トースト、自発的マロラクティック）**。**EN / FR を突き合わせて同文であることを確認** |
| **`/en/team`** | **Christian Seely（Managing Director）と Géraldine Godot（Technical Director）の経歴** |
| **`/en/contact` / `/fr/mentions-legales`** | **所在・電話・メール・法人名・RCS・TVA** |
| 🔴 **`/en/vin/1/clos-des-forets-saint-georges-monopole`** | 🔴 **1998–2024 の 27 ヴィンテージ。**7.2 ha・monopole の定義・地質・2023 / 2021 / 2019 の醸造と Godot 署名ノート |
| 🔴 **`/en/vin/2/clos-du-chapeau-monopole`** | 🔴 **`Monopole` であることの確認。**1.6 ha・Comblanchien・帽子形・CdN-Villages 5 村 170 ha・35 hl/ha 方針・2023 のデータ |
| 🔴 **`/en/vin/9/romanee-saint-vivant`** | 🔴 **2023 の実在確認。**1098 年 Cîteaux・Romanée-Conti と道 1 本・**1990 年まで Aloxe-Corton の一人の造り手・Arlot の初ヴィンテージは 1991 年**・木桶発酵・料理の合わせ |
| **`/en/vin/3` `/7` `/8` `/10`–`/13`** | **Clos de l'Arlot 赤（2 ha・旧採石場・泉）と白（急斜面・手作業）、Les Suchots、Au Leurey 0.24 ha、Le Mont 1 ha（Ch 0.66 / PN 0.33）、Mont des Oiseaux（Clos de l'Arlot の若木）** |
| 🔴 **`wines.axamillesimes.com/{H71D2E,N2UGUE,P2UG0E,1CA27E,I27I1E}/get/tech-sheet`** | 🔴 **OBP 掲載 5 本の造り手署名入り fiche technique PDF（各 2 頁）。**🔴 **PDF タイトルがハイフン有りの `Clos des Forêts Saint-Georges Monopole` / `AOC Nuits-Saint-Georges Premier Cru` / `AOC Côte de Nuits-Villages` / `Romanée-Saint-Vivant Grand Cru` である点が重要** |
| **`/en/news/8` `/9`** | **馬耕（斜度 30–50 度・年 1 回・通常はケーブルウインチ）と堆肥（牛糞＋ビオディナミ調合剤・畑の 1/3 を毎年輪番）** |
| 🔴 **`opendata.agencebio.org/api/gouv/operateurs/?siret=34117943000010`** | 🔴 **`numeroBio 108745` / 認証機関 `Ecocert France` `FR-BIO-01` / `ENGAGEE` / `datePremierEngagement 2010-07-16` / 管理参照年 2026 / `Raisin de cuve` と `Vins de raisin` がともに `AB` / 活動は Production ＋ Préparation** |
| ✅ **`certificat.ecocert.com/entreprise/A7873588-…`** | **証明書ページが実在。`Certification Agriculture biologique Europe (EU) 2018/848`、住所 `14 RD 974, 21700 PREMEAUX PRISSEY`** |
| 🔴 **`biodyvin.com/fr/liste-des-membres-biodyvin.html`** | 🔴 **会員リストを走査 → `Arlot` は 0 件（＝非会員）** |
| 🔴 **`demeter.fr/adherents-sitemap.xml`（993 件）** | 🔴 **走査 → `Arlot` は 0 件（`de-sousa-charlotte` / `charlot-tanneux` の誤ヒットのみ）** |

**取得できなかったもの / 存在しなかったもの**

- 🔴 ⚠️ **INAO extranet の 3 本は HTTP 200 で HTML を返し、PDF ではなかった**
  （`PNOCDC-Nuits-Saint-Georges` / `PNOCDC-Romanee-Saint-Vivant` / `PNOCDC-Cote-de-Nuits-Villages`。各 6.9 KB の `text/html`）。
  **`_sources/domaine-de-l-arlot/NOT_A_PDF_inao_*.html` として保存。本書に appellation 団体の一次資料は無い。**
- 🔴 ⚠️ **親会社 `AXA Millésimes` のコーポレートサイト（`axamillesimes.com` / `axa-millesimes.com` トップ）は
  本セッションの環境から名前解決できなかった。** **所有関係の corroboration は
  「ドメーヌ自身の history ページの記述」と「`wines.axamillesimes.com` からの fiche 配信」に依っている。**
- ⚠️ **`arlot.fr` は HTTPS で応答しない。**
- 🔴 ⚠️ **ドメーヌの総面積が公式に無い。**
- 🔴 ⚠️ **アルコール度数（% vol）・生産本数が 5 本のどの fiche にも無い。**
- ⚠️ **2021 / 2019 の年固有の醸造・熟成データが無い**（総称記述のみ）。
- ⚠️ **RSV と Les Suchots の所有面積が無い。**
- ⚠️ **`/en/news`（11 記事）のうち 4 記事のみ精読。残り 7 記事は未読。**
- ⚠️ **`/en/gallery`（472 KB）と `The movie of Domaine de l'Arlot` は未確認。**

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔍 **canonical: `migration/out/export/db_wine_canonical.json`（928 件）→ Arlot 名義 1 件（`arlot-clos-des-forets-2021`）**／
🔍 **OBP: `research/out/t-01/inventory.json` 929–933 行の 5 本。**
**`producer_heading` は 5 行とも `L’Arlot`、`section_path` は `["FRANCE | RED", "BURGUNDY"]`、`section_start_page` は 12。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | **法人名・RCS・TVA・SIRET・所在・所有者・両責任者がすべて一次で取れた。**公的登録と mentions légales が相互に一致 |
| **Overview** | **High** | 哲学の原文、所有構造、醸造の署名がすべて公式 |
| **History** | 🔴 **High** | 🔴 **18 世紀末から現在まで、年つきの系譜が公式の history ページから連続して取れた。**⚠️ 総面積と取得経緯の詳細のみ不在 |
| **Location** | **Medium-High** | 🔴 **主要区画の面積・地質・モノポール status が確定。**⚠️ **総面積と RSV / Les Suchots の面積が不在** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **公式の主張だけでなく、`Agence Bio` 公開登録 → `Ecocert France FR-BIO-01`・`ENGAGEE`・`2010-07-16` という認証機関側の記録まで取れた。**さらに **`Biodyvin` / `Demeter` 非会員という negative evidence も両者の公式リストから確認。**⚠️ **認証年の 2014 と 2010-07-16 の差だけが未解消** |
| **Winemaking** | **Medium-High** | 🔴 **2023 年の 3 本は除梗率・マセラシオン温度と日数・発酵容器・樽の新樽比率と月数・収量・瓶詰め日まで取れた。**⚠️ 🔴 **2021 / 2019 は総称記述のみ。アルコール度数はゼロ** |
| **Style** | 🔴 **High** | 🔴 **OBP 掲載 5 本すべてに Géraldine Godot 署名入りの公式テイスティングノートがある** |
| **Important Cuvées** | 🔴 **High** | 🔴 **5 本すべての公式ヴィンテージ実在を確認。**公式 13 ワインとモノポール 4 ラベルを確定。**$3,700 の RSV 2023 が公式に裏付けられた** |
| **Staff Notes** | **High** | ⚠️ **14 項目。**🔴 **「家族経営」「RSV がモノポール」「ビオディナミ」「2023 が全房」「2023 の数字を 2021/2019 に流用」という 5 つの事故を塞いだ** |
| **Canonical Conflict** | **High** | 実データを読んで 3 件（＋参考 1 件）を特定。`S-2` / `C-1` の族に収めた |
| 🔴 **総合** | 🔴 **High — staff-usable。70% を明確に超過（体感 88%）。** | **OBP 掲載 5 本すべてについて、公式の正式名・アペラシオン・畑・面積（該当分）・栽培・醸造（2023 は全数値）・造り手のテイスティングノートを言える。**欠けているのは**アルコール度数・総面積・2021/2019 の年別数値**で、いずれも「言わなければ嘘にならない」種類の欠落である |

**reached_70: YES.**

---

## Open Questions

1. 🔴 **canonical に 4 本分のレコードが無い。**
   **`Clos du Chapeau`（キュヴェごと）、`Romanée-Saint-Vivant`（キュヴェごと・$3,700）、
   `Clos des Forêts Saint Georges` の 2023 と 2019。**
   → **本書の §Important Cuvées に公式 13 ワインと 1998–2024 のヴィンテージ一覧があり、そのまま登録原簿になる。**
   **登録可否は Akio / CTO 判断。本書では実行していない。**
2. 🔴 **`S-2`（埋め込み二重引用符）と、ハイフンの揺れをどう正規化するか。**
   🔴 **造り手自身がウェブと PDF で 2 通りの綴りを使っている**という事実が新しい。
   **`Monopole` を名称の一部にするか属性にするかも同時に決める必要がある。**
3. 🔴 **appellation 団体の一次資料が無い。**
   **INAO extranet の 3 本が PDF を返さなかった。**
   → **`Nuits-Saint-Georges` / `Romanée-Saint-Vivant` / `Côte de Nuits-Villages` の
   cahier des charges を別ルート（INAO 本体サイトの検索、または EU eAmbrosia）で取り直す必要がある。**
4. 🔴 **有機認証の年が 2 つある。**
   **公式サイト「2014 年に AB 認証」／ Agence Bio 登録「`datePremierEngagement 2010-07-16`」。**
   → **Ecocert 証明書ページから「現行証明書 PDF」をダウンロードすれば発行日で決着する可能性が高い**
   （ページ上にダウンロード UI があるが、日付・言語の選択が JS 制御で、本調査では取得しなかった）。
5. **`Clos du Chapeau` の収量 35 hl/ha（方針）と 53 hl/ha（2023 実測）の関係。**
   **公式が説明していない。**
6. **`La Gerbotte`（最新 2020）/ `Cuvée Le Petit Arlot`（2014）/ `Cuvée Les Petits Plets`（2014）の現況。**
   **生産終了なのか、単にページが更新されていないのか、公式に記載が無い。**
   ⚠️ **他のワインは 2024 まで更新されているため「更新漏れ」では説明しづらい。**
7. **アルコール度数（% vol）と生産本数。** **公式 fiche に一切無い。**
   → **輸入元向けのテクニカルシート、またはラベル実物が要る。**
8. **ドメーヌの総面積。** **公式が一度も書いていない。**
9. **`Romanée-Saint-Vivant` と `Les Suchots` の所有面積。**
   **RSV は $3,700 という価格に対して、公式が面積を一切書いていない。**
10. **親会社 `AXA Millésimes` のコーポレートサイトが本セッションで到達できなかった。**
    → **所有関係の二次確認（グループの公式ポートフォリオ頁）が未取得。**
    **ただしドメーヌ自身の history ページに明記されているため、事実自体は確定している。**
11. **`/en/news` の未読 7 記事と `/en/gallery`、公式ムービー。**
    **収穫や畑仕事の追加情報が含まれる可能性がある。**
