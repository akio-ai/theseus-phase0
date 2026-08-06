# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:michel-gonet` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト gonet.fr / en.gonet.fr で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では使用していない**）
> `⚠️` **出典間で食い違い。両方を残す**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.gonet.fr/`（FR）と `https://en.gonet.fr/`（EN）の二言語**
> 走査元: 公式 `sitemap.xml` → `pages-sitemap.xml`（**2026-08-05 に再取得。掲載 53 URL を全件確認**）。
> シャンパーニュ関連ページ（`/histoire-d-une-famille` `/terroirs` `/vinification` `/champagnes`
> `/anamnese` `/coeurdemesnil` `/millesimegrandcru` `/authentique` `/3terroirs` `/vindey-montgueux`
> `/fravaux` `/brut6g` `/rose` `/champagnerose` `/noel` `/prestige` `/ratafia` `/boutique`
> `/article-hve` `/revue-presse` `/downloads` `/find-us`）は**両言語で取得済み**。
>
> ⚠️ **キュヴェ別テクニカルシート PDF は「存在するが読めない」。** 公式 `/downloads` の
> 「FICHES TECHNIQUES」から 7 本（3 Terroirs / Authentique / Brut 6g / Cœur de Mesnil /
> Grand Cru Millésimé / Prestige / Vindey-Montgueux）を取得済みだが、**中身がアウトライン化された
> デザイン PDF でテキスト層が無く、機械抽出は 1 本を除き全て空**（`_sources/michel-gonet/ts_*.pdf`）。
> → **本書の技術数値は全てキュヴェページ HTML 由来。**PDF の数値との突合は未実施。→ Open Questions 6
>
> 🔴 **サイトの「現在性」は節ごとに違う。** blog / booking の sitemap lastmod は **2026 年**（サイトは生きている）
> 一方、**キュヴェページの内容は 2023–2024 年頃で止まっている**と読める
> （`3 Terroirs` = "currently 2020"、`Édition de Noël` = **2023**、フッター © 2017）。
> **人物・現行ヴィンテージ・在庫を現在形で断定していない。** → Open Questions 1

---

## Identity

| | |
|---|---|
| **Canonical Name** | Michel Gonet |
| **公式の法人名** | **SCEV Michel Gonet & Fils** ✅（全ページのフッター著作権表記） |
| **公式のブランド表記** | **Champagne Michel Gonet** / 総称として **Vignobles Michel Gonet**（シャンパーニュ＋ボルドーを束ねる呼称）✅ |
| **Aliases** | ❓ canonical `aliases` は**空**。実在する表記ゆれ（`Michel Gonet & Fils` / `SCEV Michel Gonet et Fils` / `Vignobles Michel Gonet`）が**未登録** → Open Questions 5 |
| **業態** | ✅ **自社栽培のシャンパーニュ生産者**。「38 ha の自社ブドウ畑」と公式が明記（EN `/terroirs`）。**加えてボルドーに複数のシャトーを所有する家族企業** |
| **カテゴリ記号（NM/RM/CM 等）** | ❓ **公式に一切記載なし。現場で RM とも NM とも言わない** |
| **シャンパーニュ本拠** | ✅ **196, Avenue Jean Jaurès, 51190 AVIZE** ／ +33 (0)3 26 57 50 56 ／ avize@gonet.fr |
| **ボルドー本拠** | ✅ **Château Lesparre, 33750 Beychac et Caillau** ／ +33 (0)5 57 24 51 23 ／ info@gonet.fr |
| **エペルネの受け入れ拠点** | ✅ **Villa Signolle — 37 avenue de Champagne, Épernay**（2011 年〜、Sophie が開設） |
| **創業** | ✅ **1802 年、Charles Gonet がシャンパーニュのメゾンを創業**。長く「**Gonet et Fils**」の名で発展 |
| **名祖** | ✅ **Michel Gonet（1935 年生）** — 現在のメゾンを Avize に築いた人物 |
| **現世代** | ✅ **Sophie（シャンパーニュ）/ Charles-Henri / Frédéric**。「今日、シャンパーニュとボルドーで松明を受け継いでいるのは彼らである」 |
| **世代数** | ✅ **「7 世代」**（FR `/champagne`: "depuis 7 générations"） |
| **品質責任者** | ✅ **Julie Jeanneau** — ただし出典は **HVE 記事（2019–2020 年頃）**。現況未確認 → Open Questions 1 |
| canonical id | `producer:michel-gonet` |
| canonical entity confidence | **0.2**（source: `legacy_app`、`facts` は**空**、`aliases` も**空**、legacy_id `michel-gonet-mesnil-gc-2015`）— エンティティ同定の確度であり、本書の充実度とは別軸 |

---

## Overview

✅ **Avize に本拠を置く、シャンパーニュ 38 ha の自社栽培生産者。**主役は圧倒的に**シャルドネ**で、
**コート・デ・ブランのグラン・クリュ 3 村（Le Mesnil-sur-Oger / Oger / Avize）を核に、
コトー・セザネ（Vindey）、モングー（Montgueux）、コート・デ・バール（Fravaux）という
性格の異なる 4 つのテロワールを持つ**。この「グラン・クリュだけの家ではない」という点が、
同じコート・デ・ブランの単一村生産者との決定的な違いである。

✅ **1802 年創業（Charles Gonet、当初は "Gonet et Fils"）。** ただし現在のメゾンは、
**長兄だった Michel Gonet が弟たちに家業を譲って数キロ離れた土地へ移り、新たにカーヴを築いた**
ところから始まっている（公式の家族史）。**Gonet 姓のシャンパーニュ生産者が複数存在するのは
この分岐が理由**であり、公式サイト自身がその分岐を明記している。→ §Staff Notes ⚠️ 最重要。

✅ **醸造の署名は「区画別 × 低温 × 極低ドザージュ」。** 全収穫を Avize の自社圧搾所で**区画ごとに個別圧搾**し、
**区画ごとに小型タンクで個別醸造**。発酵は **12–13°C の低温で 2–3 週間**。
**1973 年に白亜層を 12 m 掘って造った地下カーヴ**が年間を通じて **12°C** を保つ。
デゴルジュマンは自社で行い、**その年のシャルドネから作ったリキュール**を用いる。

✅ **マロラクティック発酵は「年による」。2016 年以降は温暖化への対応として意図的にブロックしている**
と公式が明言する（`/vinification`）。⚠️ **ただしキュヴェページの記述と矛盾する箇所がある** → §Winemaking。

🔍 **THÉSEUS における現状は極端に薄い。** canonical は **producer 1 件（confidence 0.2・facts 空）＋
キュヴェ 1 件（`Mesnil-sur-Oger Grand Cru Blanc de Blancs` / vintages `2015` のみ）**。
**OBP 掲載 3 本のうち、canonical で解決できるものは 0 本**（3 本すべて `match_state = unresolved`）。

---

## History

✅ **公式の家族史は `/histoire-d-une-famille`（EN: `en.gonet.fr/histoire-d-une-famille`）の 1 ページに集約されている。**
以下はその全内容である。**これ以上の年表・世代図は公式に無い。**

### Foundation

- ✅ **1802 年、Charles Gonet が自らのシャンパーニュ・メゾンを創業。** 以後長らく「**Gonet et Fils（Gonet and Sons）**」の名で発展。
- ⚠️ **1802 → 1935 の年数表現が EN と FR で食い違う。**

| | 記述 |
|---|---|
| **EN `/histoire-d-une-famille`** ✅ | "More than **half a century** later, in 1935, Michel Gonet was born." |
| **FR `/histoire-d-une-famille`** ✅ | "Plus d'un **siècle et demi** plus tard, en 1935, naît Michel Gonet." |

→ **実年数は 133 年**であり、**FR の「一世紀半以上」は過大、EN の「半世紀以上」は過小**。
**どちらも公式。どちらも消さない。現場ではどちらの表現も使わず「1802 年創業、1935 年に Michel 誕生」と数字で言う。**

### Michel Gonet（1935–）

- ✅ **出生時に食道閉塞（dysphagie）で何も飲み込めず、「奇跡的に助かった子」とされた。
  一口のシャンパーニュで息を吹き返したという。本人は後に「シャンパーニュが私を救った」と語った。**
  → **これがワインへの情熱の始まりだったと公式は位置づけている。**
- 🔴 ✅ **長兄であった Michel は、弟たちに場所を空けるため家業の土地を離れ、
  妻 Annie とともに数キロ先へ移って新しいカーヴを築いた。**
  → **これが「Gonet」姓の分岐点である。** §Staff Notes ⚠️ ①
- ✅ その後長年にわたり畑とカーヴの仕事の質を高め続けた。目標は「**純粋で、環境に配慮したシャンパーニュを作り直すこと**」。
- ❓ **Michel Gonet の没年・現況は公式に一切記載がない。現在形でも過去形でも断定していない。** → Open Questions 2

### ボルドーへの拡張

- ✅ **1986 年、Michel がボルドー地方に惚れ込み、3 人の子（Sophie / Charles-Henri / Frédéric）に支えられて
  シャンパーニュで培った savoir-faire を持ち込む。**
- ✅ **右岸のあと左岸へ。** まず **Charles-Henri が Château Haut-Bacalan**、続いて **Frédéric が Château d'Eck**。
- ✅ **Château Haut-Brana** が後に加わる。公式は「**Pessac-Léognan の小さな宝石で、Château Pape Clément の畑に囲まれている**」と記す。
- 🔍 公式 `pages-sitemap.xml` に専用ページを持つボルドーの資産（2026-08-05 時点）:
  **Château Lesparre / Château Haut-Bacalan / Château d'Eck / Château Haut-Brana /
  Château Durand-Bayle / Château Saint-Eugène / Château La Rose Videau / Château Haut-l'Évêque**。
  ❓ **各シャトーの取得年・面積・アペラシオンは本調査では未取得**（シャンパーニュ優先のため）→ Open Questions 7

### エペルネ

- ✅ **2011 年、Sophie が「迎え入れ、家族のシャンパーニュを分かち合いたい」という思いから
  エペルネの名高い avenue de Champagne 37 番地に進出。**
  婚姓を冠した **Villa Signolle** はシャンパーニュ愛好家の必訪地となった、と公式は述べる。
- ✅ 公式は **avenue de Champagne が 2015 年に UNESCO 世界遺産に登録された**ことを併記している。

### 環境認証の歩み

- ✅ **2019 年、VDC（Viticulture Durable en Champagne）認証取得に向けた転換を開始**（`/terroirs`）。
- ✅ **同じく 2019 年から HVE（Haute Valeur Environnementale）に着手し、「2020 年末までに niveau 3 到達を目指す」と表明**（`/article-hve`）。
- ❓ 🔴 **VDC も HVE も「取得した」という記述は公式サイト上に見当たらない。**
  取得の可否・時期は**未確認**。→ §Farming / Open Questions 3

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Champagne ✅（＋ Bordeaux に別事業）|
| **本拠村** | **Avize**（Côte des Blancs / Grand Cru 村）✅ — 196 Avenue Jean Jaurès |
| **自社畑面積** | ✅ **38 ha**（EN `/terroirs`: "With 38 hectares of vine in the best terroirs of the Champagne region"）。⚠️ **FR 版の対応文は本調査の抽出では回収できず、EN のみで確認**。→ Open Questions 4 |
| **畑の広がり** | ✅ **コート・デ・ブラン（Grand Cru）／コトー・セザネ／モングー／バール・シュル・オーボワ（Côte des Bar）の 4 圏** |

### Key Vineyards — **公式が区画名まで開示している**（FR `/terroirs`。EN 版には区画名リストが無い）

| テロワール | 村 | 土壌 ✅ | 品種 ✅ | **区画（lieux-dits）** ✅ |
|---|---|---|---|---|
| **Côte des Blancs — Grand Cru** | **Le Mesnil-sur-Oger / Oger / Avize** | **craie limoneuse（シルト質の白亜）+ 下層は白亜**。北の冷風はモンターニュ・ド・ランスに遮られ、マルヌ渓谷の雨も免れる | Chardonnay | 🔴 **Les Hautes Mottes** / Les Coullemets / Vaucherot / Les Moissonnières / Les Boulangères / Le Tilleul / **Chetillon** / Les Maladreries du Midi |
| **Coteaux du Sézannais（Vindey）** | Vindey | **argilo-calcaire**、区画により砂質 | Chardonnay（繊細・花・高い vivacité） | Les Sablons / Le Village / Les Macherets / La Justice / Les Chalmonts |
| **Montgueux**（トロワ近郊） | Montgueux | **craie marneuse ＋ 小さな珪石片**、**真南向き** | Chardonnay（**力強く、スパイシー**） | Les Jognelles / Beauregard / Voie Creuse / Bas du Fiat / Grate Pot / Les Chères Vignes / La Richasse / Vaux / Marivat |
| **Côte des Bar（Bar-sur-Aubois）** | **Fravaux**（＋ Spoy / Couvignon） | 小さな石灰片と珪石。全体に白亜質で気温変動を緩衝 | **Pinot Noir**（明るく果実的） | **Le Varlan** / Prele（Spoy）/ Terres de L'Ebveaux（Couvignon） |

### 🔴 **`Les Hautes Mottes` はキュヴェ名ではなく、Le Mesnil-sur-Oger の lieu-dit である**

✅ 公式は 3 か所で一致してこう書く —

| ページ | 記述 |
|---|---|
| `/terroirs` | Côte des Blancs Grand Cru の**区画リストの筆頭**が **Les Hautes Mottes** |
| `/coeurdemesnil` | Terroir: **"Le Mesnil-sur-Oger, vieilles vignes du lieu dit «les Hautes Mottes»"** |
| `/authentique` | Terroir: **同上（vieilles vignes du lieu dit «les Hautes Mottes»）** |
| `/millesimegrandcru` | Terroir: **"Le Mesnil-sur-Oger, lieu-dit «les Hautes Mottes»"** |

→ すなわち **Les Hautes Mottes は、このメゾンの最上級キュヴェ 3 本すべての供給源となっている
ル・メニル・シュル・オジェの老樹区画**である。
→ 🔴 **OBP が「'Les Hautes Mottes,' Brut Nature 2018」として売っている 1 本の正体は、この区画名である。**
**ただし「Les Hautes Mottes」という名のキュヴェは公式サイトに存在しない**（`pages-sitemap.xml` 53 URL・
`/boutique` の商品名一覧の**いずれにも無い**、2026-08-05 実測）。→ §Important Cuvées / Open Questions 8

---

## Farming

- ✅ **自社栽培。38 ha。**（買いブドウについての記述は公式に無い ❓）
- ✅ **公式の表現は「culture raisonnée（減農薬・理性的栽培）」であって、オーガニックでもビオディナミでもない。**
  「Sophie とチームは、**投入資材を減らし区画の生物多様性を守る**ことを目的に、
  **culture raisonnée・土壌の耕起（travail des sols）・草生栽培（enherbement）** の一貫した実践を進めている」。
- ✅ 具体的な実践として公式が挙げるもの: **森や生垣の保存／生態学的緩衝帯の維持／水資源の管理**。
- ✅ **2019 年に VDC（Viticulture Durable en Champagne）への転換を開始**（`/terroirs`）。
- ✅ **同 2019 年から HVE に着手**（`/article-hve`）。公式が挙げる取り組みの柱は 4 つ —
  **①廃棄物管理の最適化 ②投入資材の削減**（植物防疫製品の使用制限・施肥の均衡化・水資源使用の削減）
  **③自社敷地内の自然空間保全による生物多様性の保護 ④農業実践の負の影響の限定と便益の最適化**。
  公式は HVE を「**製品の品質ではなく、農場の環境品質を認証する制度**」と正しく説明している。
- ✅ 公式の自己申告: 「**30 年近く、テロワールとブドウ樹への敬意が Vignobles Michel Gonet の哲学の一部だった**」
  「**長年 agriculture raisonnée に取り組んできた**」。

### 🔴 ❓ **認証の「現在の到達点」が公式に無い**

- **VDC**: 「2019 年に転換を開始した」までしか書かれていない。**取得したとは書かれていない。**
- **HVE**: 「2020 年末までに niveau 3 到達を**目指す**」で記述が終わっている。**達成の告知が見当たらない。**
- → 🔴 **現場で「HVE 認証」「VDC 認証」を持っていると言ってはならない。** → §Staff Notes ⚠️ ⑤

### ❓ 公式に無い農業情報

**樹齢（「vieilles vignes」という語以外に数値なし）／各区画の面積内訳／植密度／収量（kg/ha）／
収穫日／手摘みか否か／台木・クローン／畑ごとの所有・借地の別。**

---

## Winemaking

✅ **`/vinification`（FR）のギャラリー解説が、このメゾンで最も情報密度の高い一次資料である。**
以下はその全 11 項目（EN 版 `/vinification` と突合済み。**FR 版の方が記述が厚い**）。

### 圧搾 ✅

- **収穫の全量を Avize の自社カーヴで自ら圧搾する。**
- 🔴 **区画ごとに個別に圧搾する（"Chaque parcelle est pressée séparément"）。**
- **果汁は抽出段階でも分ける。** より洗練され均衡した **cuvée（一番搾り）がシャンパーニュに使われる。**
- **tailles（圧搾後半の、より糖度が高く力強い果汁）のうち最も質の高いものだけがラタフィアに回される。**

### 発酵 ✅

- 🔴 **区画ごとに個別醸造（cuves parcellaires）。** 「小型タンクによって、それぞれ異なり唯一である
  テロワールのアロマと個性が育つのを見ることができる。**vins clairs の区画的多様性が最良のアッサンブラージュを可能にする**」。
- **全ての醸造を低温（12–13°C）・サーモレギュレーション付きステンレスタンクで行う。** 目的は「**大いなる繊細さを持つワイン**」。
- **発酵期間は 2〜3 週間。**

### ⚠️ マロラクティック発酵 — **公式内部で食い違う**

| 出典 | 記述 |
|---|---|
| **`/vinification`（FR）** ✅ | 「MLF は**体系的ではなく**、ミレジムの豊かさと、フレッシュさ／力強さの均衡によって決まる。**2016 年以降は温暖化の影響により、ミレジムのフレッシュさと酸を守るため MLF をブロックしている**」 |
| **`/millesimegrandcru`（Grand Cru millésimé、**Vintage: 2016**）** ✅ | Vinification: "Low temperature fermentation **& malolactic fermentation**" |
| **`/coeurdemesnil`（Cœur de Mesnil、Vintage: 2009）** ✅ | Vinification: "Low temperature fermentation **& malolactic fermentation**" |
| **`/anamnese`（Anamnèse）** ✅ | 「**fermentation malo-lactique partielle**、ミレジムに応じて」 |
| **`/3terroirs` `/vindey-montgueux` `/fravaux` `/brut6g` `/rose`** ✅ | いずれも "**Without malolactic fermentation**" |

→ 🔴 **「2016 年以降はブロック」と「2016 年ミレジムは MLF あり」が正面から矛盾する。**
**どちらも公式。どちらも消さない。**
→ **合理的な読みは「方針転換の初年であり、キュヴェページの更新が追いついていない」だが、これは推測である。**
→ **現場では「MLF はキュヴェと年によって変える家」と言うにとどめる。** → §Staff Notes ⚠️ ④

### 樽 ✅

- 「**一部のキュヴェは樽熟成の恩恵を受け、丸みと力強いアロマを得る。An "Authentique" pleasure（＝キュヴェ Authentique の名に掛けている）。**」
- 「**一部のバリックはアッサンブラージュを丸め、構築し、複雑にするためにも用いられる。**」
- ✅ **具体値が公式にあるのは Authentique のみ — 「オーク樽で 7 か月」。**
- ❓ **新樽比率・樽の産地・樽材・容量・バトナージュは一切非公開。**

### 熟成・デゴルジュマン ✅

- **地下カーヴは Avize。1973 年に建設、白亜層を 12 m 掘り下げ、年間を通じて 12°C。**
- **アッサンブラージュ・瓶詰め後、将来のシャンパーニュは 3〜15 年 sur latte で熟成**してから
  **mise sur pointe**（動瓶）、そしてデゴルジュマンへ。
- **各ロットのサンプルを保管し、継続性と品質を担保する。**
- 🔴 **デゴルジュマンは自社で行う。リキュール・デクスペディシオンには「その年のシャルドネから作ったワイン」を用い、
  最適なフレッシュさを保つ。「われわれのシャンパーニュは、ワインとテロワールを語らせるため、極めて低くしかドザージュしない」。**

### ❓ 公式に一切記述が無い項目（**現場で語ってはならない**）

**酵母（天然か培養か）／補糖（シャプタリザシオン）／清澄・濾過／ティラージュの詳細／
リザーブワインの管理方式（Anamnèse の "réserve perpétuelle" 以外）／生産本数／
デゴルジュマン日（ロット別）／各キュヴェの実分析値（pH・総酸・アルコール）。**

---

## Style

✅ **公式が掲げる核の一文** — 「**« La terre n'appartient pas à l'homme, c'est l'homme qui appartient à la terre »**
（土地が人に属するのではない、人が土地に属するのだ）。**7 世代にわたり、この格言から学びを引き出そうとしてきた**」（FR `/champagne`）。

✅ **テロワールを「国」として扱うという自己規定** — 「Sophie、Charles-Henri、Frédéric はそれぞれのやり方で、
フランスと世界の他の産地への旅と経験によって味覚を鍛え、好奇心を養ってきた。
**そうして彼らは大きな開かれた精神で、自分たちのテロワールをそれぞれ独立した「pays（国）」として捉える —
まず訪ね、次に研究し、そこに実践を適合させ、その典型性を価値づける**」（FR `/champagne`）。
→ **これが「4 つのテロワールを別々に瓶詰めする」という商品構成の思想的裏付けである。**

### テロワール別の公式スタイル記述 ✅

| テロワール | 公式が使う言葉 |
|---|---|
| **Côte des Blancs GC** | 白亜がもたらす **structure と minéralité**。「grand vin de Champagne の生産に適する」 |
| **Coteaux du Sézannais（Vindey）** | **fins, floraux（繊細・花的）**、**grande vivacité et fraîcheur** |
| **Montgueux** | **puissants et épicés（力強く、スパイシー）**。真南向きが「richesse aromatique」を養う |
| **Côte des Bar（Fravaux）** | ピノ・ノワールが **clairs et fruités（明るく果実的）** |

### 味わいの語彙（公式キュヴェページの Tasting 欄より）✅

- **共通して繰り返される語は "brioché"（ブリオッシュ）と "minéral" と "gourmand"。**
  Cœur de Mesnil / Authentique = 「gourmet wine, complex, **brioché** and **mineral**」。
- **Anamnèse の家族テイスティングノート（FR、最も詳細な公式ノート）** ✅
  「香りでは、**リンゴの花の優雅さ**が、**キャラメリゼした黄色い果実のタルト・タタンの甘さ**と
  **レモン・メレンゲの爽やかさ**に出会う。
  口中では、**フレッシュなアタック**が**キャラメルとクレーム・ブリュレの gourmandise** へ変わる。
  香りで予感された白い花は**アーモンドの花**として現れ、**蜂蜜と蜜蝋**へ進む。
  **澱熟成による gras（丸みのある厚み）とアロマの豊かさ**が苦味と柑橘の要素と釣り合い、
  ワインをゆっくりとした estompe（にじみ消え）へ運ぶ。
  **常に底流にあるミネラリティが、構造と複雑な塩気を与える。**」

✅ **公式が掲載する第三者評価**（「公式が引用している」という事実は一次情報。評価そのものは第三者）

| キュヴェ | 掲載されている評価 |
|---|---|
| **Grand Cru Millésimé 2016** | **Guide Hachette 2021 — 2 étoiles** |
| **Cœur de Mesnil 2009** | **Bettane et Desseauve — 16/20** |
| **Brut 6g** | **Gault & Millau — 16/20** |
| **Rosé de Saignée 2007** | **Gault & Millau — 16/20**（引用コメント: 「なんというロゼ、当惑するほどの果実の純度、森の苺と温めたフランボワーズ…」） |
| **Prestige（1996 / 1998）** | **Gault & Millau 15/20 ／ Le Figaro 16/20** |

⚠️ **これらは全て公式サイト上に文字で載っている。**ただし**掲載年が古い**（Hachette 2021 が最新）。
**「現在の評価」として語らない。**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 3 本。すべて BLANC DE BLANCS セクション**）

| # | OBP 印字 | VT | 価格 | match_state | cuvee_state | canonical | **公式サイトでの対応** |
|---|---|---|---|---|---|---|---|
| 1 | **'Vindey-Montgueux,' Extra Brut** | NV | **$160** | 🔴 unresolved | 🔴 unresolved | ❌ 未登録 | ✅ **存在する** — `Champagne Vindey - Montgueux, Blanc de Blancs, Extra Brut` |
| 2 | **'Mesnil-sur-Oger,' Grand Cru Extra Brut** | **2016** | **$220** | 🔴 unresolved | alias | ⚠️ **キュヴェは登録済み・年が無い**（`Mesnil-sur-Oger Grand Cru Blanc de Blancs` / 保有 vintage は **2015 のみ**） | ✅ **存在する** — `Champagne Grand Cru millésimé`（**Vintage 2016**） |
| 3 | **'Les Hautes Mottes,' Brut Nature** | **2018** | **$345** | 🔴 unresolved | 🔴 unresolved | ❌ 未登録 | 🔴 ❓ **同名のキュヴェは公式サイトに存在しない**（`Les Hautes Mottes` は**区画名**） |

🔍 **3 本すべて `producer_state = exact`（生産者名は完全一致）。詰まっているのは全てキュヴェ層である。**

#### ① Vindey-Montgueux — **canonical に無いだけで、公式には確実に存在する** ✅

| | 公式記述（`/vindey-montgueux`） |
|---|---|
| 品種 | **Chardonnay 100%**（Blanc de Blancs） |
| テロワール | **Vindey**（⚠️ 商品名は "Vindey - Montgueux" だが、キュヴェページの Terroirs 欄は **"Vindey" のみ**。`/boutique` の商品名は "Vindey - Montgueux, Blanc de Blancs, Extra Brut"） |
| 醸造 | 低温発酵・**MLF なし** |
| 熟成 | 「フレッシュな果実のアロマを保つための最小限の澱熟成」 |
| ヴィンテージ | **Non vintaged（NV）** — **OBP の NV と一致** ✅ |
| ドザージュ | **Extra-brut 2 g/L** |
| 味わい | 「果実的かつ gourmand。**2 つのテロワール双方の典型性**を示す — フレッシュな果実と白い花、そして心地よい丸み」 |

→ **canonical に追加すべき筆頭候補。ただし本書では追加していない。** → Open Questions 9

#### ② Mesnil-sur-Oger Grand Cru 2016 — 🔴 **ドザージュ表記が OBP と公式で食い違う** ⚠️

| | 公式記述（`/millesimegrandcru`） |
|---|---|
| 公式名 | **Champagne Grand Cru millésimé**（`/boutique` の商品名: **"Grand Cru, Mesnil-sur-Oger, Millésimé"**） |
| 品種 | **Chardonnay 100%** |
| テロワール | **Le Mesnil-sur-Oger, lieu-dit "les Hautes Mottes"** |
| 醸造 | 低温発酵 **＋ MLF あり**（⚠️ `/vinification` の「2016 以降ブロック」と矛盾。→ §Winemaking） |
| 熟成 | **最低 7 年 sur latte** |
| ヴィンテージ | **2016** — **OBP と一致** ✅ |
| ドザージュ | 🔴 **Zéro dosage 0 g/L** |
| 評価 | **Guide Hachette 2021 — 2 étoiles** |
| 味わい | 「美しい淡い黄金色、軽やかで、エレガントかつ爽やかな口中」／「refined wine, mineral with chalky notes」 |

→ ⚠️ **OBP は "Extra Brut" と印字しているが、公式は "Zéro dosage 0 g/L" である。**
**Extra Brut（0–6 g/L）の範囲内なので「誤り」ではないが、「エクストラ・ブリュットで 4〜5 g くらい」と補って語ると嘘になる。**
→ §Staff Notes ⚠️ ②
→ 🔍 **canonical はこのキュヴェを持っているが vintage は 2015 のみ。2016 が無いために `unresolved` になっている。**

#### ③ Les Hautes Mottes 2018 — 🔴 **本調査で最も重要な未解決事項**

- ✅ **`Les Hautes Mottes` は Le Mesnil-sur-Oger の lieu-dit** であり、
  **Cœur de Mesnil / Authentique / Grand Cru Millésimé の 3 本すべての供給区画**である（§Location に 4 出典）。
- 🔴 **しかし「Les Hautes Mottes」という名前のキュヴェは、公式サイトのどこにも存在しない。**
  **2026-08-05 に `pages-sitemap.xml`（53 URL）を再取得して確認**、加えて `/boutique` の商品名一覧
  （Anamnèse / 3 Terroirs / Authentique 2004 / Cœur de Mesnil / Fravaux / Grand Cru Mesnil-sur-Oger Millésimé /
  Vindey-Montgueux / Édition de Noël / Grande Cuvée d'Eck Blanc）にも**無い**。
- ❓ **考えられる読みは複数あり、公式情報では決着しない** —
  (a) **Grand Cru Millésimé（区画 = les Hautes Mottes）の後年ヴィンテージが、区画名ラベルで米国に出ている**
  (b) **`/cellarsale`（公式にページは存在する）または限定リリース**
  (c) **輸入元独自の呼称**
  → **どれも証拠が無い。現場で「これは Grand Cru Millésimé の 2018 年です」と言ってはならない。** → §Staff Notes ⚠️ ③
- ⚠️ **価格の跳ね方も傍証にならない**（$220 → **$345**、+57%）。**推測の材料にしない。**
- → **必要なのはボトル実物のラベル確認、または輸入元資料。** → Open Questions 8

### 公式サイトに載る全キュヴェ（**canonical 登録は 1 件のみ・OBP 掲載は 3 本のみ**）

| キュヴェ | 品種 | テロワール | 熟成 | ドザージュ | VT | canonical | OBP |
|---|---|---|---|---|---|---|---|
| **Anamnèse — Réserve Perpétuelle de Grand Cru** | Chardonnay | **Le Mesnil-sur-Oger / Oger / Avize（GC）** | **6 年 sur latte** | **Extra-Brut 4.5 g/L** | **2010 起点の永久リザーブ＋ 2014 以降の各ミレジム** | ❌ | ❌ |
| **Cœur de Mesnil, Grand Cru, Millésimé** | Chardonnay | **Le Mesnil-sur-Oger — vieilles vignes「les Hautes Mottes」** | **最低 10 年 sur latte** | **Extra-Brut 4.5 g/L** | **2009** | ❌ | ❌ |
| **Grand Cru Millésimé（= Mesnil-sur-Oger）** | Chardonnay | **Le Mesnil-sur-Oger, lieu-dit「les Hautes Mottes」** | **最低 7 年 sur latte** | 🔴 **Zéro dosage 0 g/L** | **2016** | ⚠️ **キュヴェのみ（vintage 2015）** | ✅ **$220** |
| **Authentique — Grand Cru en fût de chêne** | Chardonnay | **Le Mesnil-sur-Oger — vieilles vignes「les Hautes Mottes」** | **オーク樽 7 か月 ＋ 最低 10 年 sur latte** | **Extra Brut** | **2004** | ❌ | ❌ |
| **3 Terroirs, Blanc de Blancs** | Chardonnay | **Le Mesnil-sur-Oger ＋ Vindey ＋ Montgueux** | **最低 5 年 sur latte** | **Extra-Brut 4 g/L** | **2009 年から。「currently 2020」** | ❌ | ❌ |
| **Vindey-Montgueux, Blanc de Blancs** | Chardonnay | **Vindey** | 最小限（果実のフレッシュさ優先） | **Extra-Brut 2 g/L** | **NV** | ❌ | ✅ **$160** |
| **Fravaux「Le Varlan」, Blanc de Noirs** | **Pinot Noir** | **Fravaux（Côte des Bar）** | 最小限 | **Extra Brut 4 g/L** | 年により組成を変える | ❌ | ❌ |
| **Brut 6g** | **Pinot Noir** | **Fravaux** | **最低 2 年 sur latte** | **Brut 6 g/L** | 年によるアッサンブラージュ | ❌ | ❌ |
| **Rosé（Assemblage）** | **Pinot Noir + Chardonnay** | **Vindey / Montgueux** | 最小限 | **Extra-Brut 2 g/L** | **NV** | ❌ | ❌ |
| **Rosé de Saignée** | **Pinot Noir** | **Fravaux** | **最低 2 年 sur latte** | **Brut 8 g/L** | **2007** | ❌ | ❌ |
| **Édition de Noël, Grand Cru, Blanc de Blancs** | Chardonnay | **Le Mesnil-sur-Oger ＋ Oger（GC）** | **4 年 sur lies** | **Brut 2 g/L** | **2023 年版**（毎冬、蔵出しまたは実験的ロットから） | ❌ | ❌ |
| **Prestige（old vintages）** | Chardonnay | **Le Mesnil-sur-Oger** | **最低 10 年 sur latte** | ミレジムとデゴルジュマンによる | **1996 / 1998** | ❌ | ❌ |
| **Ratafia de Champagne** | **Pinot Noir** | **Fravaux** | 樽で数か月〜数年、瓶で長期 | —（**18% vol**） | **1996** | ❌ | ❌ |
| **Les Hautes Mottes, Brut Nature 2018** | ❓ | ❓ | ❓ | ❓ | **2018** | ❌ | ✅ **$345** |

🔴 **公式 13 キュヴェに対し canonical は 1 件（7.7%）。OBP 3 本のうち解決できるものは 0 本。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① Gonet は「1 軒」ではない。この家は Michel が弟たちに家業を譲って出た側である。**
「シャンパーニュには **Gonet の名を持つ造り手が複数あります**。この **Michel Gonet** は、
**1802 年創業の家（当時は Gonet et Fils）の長兄だった Michel が、弟たちのために家業の土地を離れ、
数キロ先の Avize で新しくカーヴを築いた**ところから始まる家です。**造り手自身がそう書いています。**」
→ 🔴 **これが最優先。リストに「Gonet」とだけ書かれた場合、別の家の可能性を必ず疑う。**

**② 4 つのテロワールを、別々の「国」として瓶詰めする家。**
「38 ヘクタール。**ル・メニル・シュル・オジェ／オジェ／アヴィズのグラン・クリュ**、
**セザネのヴァンデ**、**トロワ近くのモングー**、そして**ピノ・ノワールのコート・デ・バール（フラヴォー）**。
造り手は自分のテロワールを『**それぞれ独立した pays（国）**』と呼び、
**区画ごとに圧搾し、区画ごとに小さなタンクで醸します。**
だから **1 本ごとに産地の性格がまるで違う** — セザネは繊細で花、モングーは力強くスパイシー、
グラン・クリュは白亜の構造とミネラル。」

**③ 極低ドザージュ。OBP の 2016 グラン・クリュは「ゼロ・ドザージュ」である。**
「デゴルジュマンは自社で行い、リキュールには**その年のシャルドネから作ったワイン**を使います。
造り手は『**ワインとテロワールを語らせるため、ごく僅かしかドザージュしない**』と明言しています。
**2016 年のグラン・クリュ・ミレジメは、公式には 0 g/L —— ゼロ・ドザージュ。**
ル・メニル・シュル・オジェの **« Les Hautes Mottes » という単一区画**から来ていて、**最低 7 年**澱の上です。
**Guide Hachette 2021 で 2 つ星。**」

### 追加で使える一手

- **カーヴの話**: 「アヴィズのカーヴは **1973 年に白亜層を 12 メートル掘って造ったもので、年間を通じて 12°C** です。」
- **区画の話（この家の切り札）**: 「**Les Hautes Mottes** はル・メニル・シュル・オジェの**老樹の区画**で、
  この家の最上級 3 本 —— **Cœur de Mesnil、樽熟の Authentique、そしてグラン・クリュ・ミレジメ** ——
  **すべてがこの 1 区画から**来ています。」
- **名前の由来（Anamnèse）**: 「**アナムネーシス**は『**先祖が耕したテロワールへの回帰**』として造られた、
  **2010 年を起点とする永久リザーヴ**のキュヴェです。造り手は『**何年もかけて我々のミレジムを味わってきた人には、
  最も美しい記憶を呼び覚ますだろう**』と書いています。」
- **創業の逸話（使いどころを選ぶ）**: 「名祖の **Michel は 1935 年生まれ。生まれつき食道が塞がっていて
  何も飲み込めず、一口のシャンパーニュで息を吹き返した**と伝えられています。
  本人は後に『**シャンパーニュが私を救った**』と語りました。」
- **ボルドーの話（訊かれたら）**: 「**1986 年からボルドーにも進出**していて、
  **Château Haut-Bacalan** や **Château d'Eck** など複数のシャトーを家族で持っています。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／公式が食い違っている**）

> 🔴 **この家は「情報が薄い」のではなく「情報が多くて食い違っている」タイプである。危険の質が違う。**

1. 🔴 ⚠️ **他の Gonet と混同しない／「コート・デ・ブランの Gonet 家」と一括りにしない。**
   公式家族史が「**Michel は弟たちに場所を空けるため家業の土地を離れた**」と明記している以上、
   **同名の別メゾンが存在する前提で扱う。** **本社は Avize（196 Avenue Jean Jaurès）**である。
   🔍 **社内 DB には Gonet 姓の生産者が「Michel Gonet」1 件しか無い**（384 生産者を全走査して確認）。
   **つまり別の Gonet がリストに現れた場合、DB は必ずこの 1 件に吸い寄せる。DB の一致を信用しない。**
2. 🔴 ⚠️ **2016 グラン・クリュを「エクストラ・ブリュットで 4〜5 g くらい」と補足しない。**
   **公式は Zéro dosage 0 g/L。** メニューの印字（Extra Brut）は範囲としては誤りではないが、
   **具体的な g/L を補うと嘘になる。**「**ゼロ・ドザージュです**」と言う。
3. 🔴 ⚠️ **「Les Hautes Mottes 2018」を「グラン・クリュ・ミレジメの 2018 年」と言わない。**
   **公式サイトにこの名のキュヴェは存在しない**（2026-08-05 実測）。
   言ってよいのは事実だけ —— 「**Les Hautes Mottes はル・メニル・シュル・オジェの老樹の単一区画名**で、
   この家の最上級キュヴェの供給源です」。**そのうえで「この 2018 年については確認します」と引く。**
4. ⚠️ **「マロラクティックをしない家」とも「する家」とも言わない。**
   公式は「**2016 年以降はブロックしている**」と書く一方、**2016 年のグラン・クリュ自体は「MLF あり」**と書いている。
   **公式同士が矛盾している。**言うなら「**キュヴェと年によって使い分ける家**」まで。
5. 🔴 ⚠️ **「HVE 認証」「VDC 認証」を取得済みと言わない。**
   公式にあるのは「**2019 年に転換／着手した**」「**2020 年末までに HVE niveau 3 を目指す**」までで、
   **達成の記述が見当たらない。** 言うなら「**減農薬（culture raisonnée）と草生栽培に取り組み、
   2019 年から持続可能認証の取得に動いています**」。
6. ⚠️ **「オーガニック」「ビオディナミ」と言わない。** 公式の語は **culture raisonnée** である。
7. ⚠️ **創業から現在までを「一続きの家」として語らない。**
   **1802 年創業は「Gonet et Fils」であって、現在の Avize のメゾンは Michel が新たに築いたもの**である。
   「**1802 年に始まる一族で、現在の蔵は Michel が興したもの**」と分けて言う。
8. ⚠️ **1802 → 1935 を「一世紀半後」とも「半世紀後」とも言わない。**（FR / EN が食い違う。実際は **133 年**。）
9. ⚠️ **Michel Gonet を現在形で語らない。** **1935 年生まれ**で、**没年も現況も公式に記載が無い。**
   現在の担い手は **Sophie / Charles-Henri / Frédéric** である。
10. ⚠️ **Julie Jeanneau を「現在の品質責任者」と断定しない。** 出典は **2019–2020 年頃の HVE 記事**のみ。
11. ⚠️ **樽・新樽比率・酵母・生産本数・分析値（pH / 酸 / アルコール）を語らない。**
    公式に**一行も無い**。樽の具体値は **Authentique の「7 か月」だけ**である。
12. ⚠️ **評価を「現在の評価」として語らない。** 公式掲載の最新は **Guide Hachette 2021（2 étoiles）**。
    Gault & Millau や Bettane et Desseauve の点はさらに古い。**年号ごと言う。**
13. ⚠️ **「Vindey-Montgueux」の産地を断定しない。** **商品名は 2 つの村を並べるが、
    キュヴェページの Terroirs 欄は「Vindey」のみ**である。「**セザネのヴァンデを軸に、モングーを合わせた**」まで。
14. ⚠️ **「38 ha」以外の面積・区画面積・樹齢・収量を言わない。** 公式に数値が無い。
    **38 ha も EN 版でしか確認できていない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

**なし。**

🔍 **確認方法**: canonical `wine_makers.json`（**全 384 生産者**）を `gonet` で全文正規表現走査 →
**ヒットは `producer:michel-gonet` の 1 件のみ**。**同一生産者を指す重複レコードは存在しない。**

⚠️ **ただし「衝突が無い」ことは「安全である」ことを意味しない。**
公式家族史が Gonet 姓の分岐を明記しているにもかかわらず、
**canonical には Gonet 姓の生産者が 1 件しか存在せず、`aliases` も空**である。
→ **将来のリストに別の Gonet が現れた場合、producer 照合は高確率でこの 1 件に誤って解決する。**
→ これは**現在の衝突ではなく将来の誤解決リスク**であるため、本節ではなく **Open Questions 5 / 10** に置く。
**canonical は読み取りのみ。一切変更していない。**

---

## Sources

**一次資料（公式サイトのみ。非公式ソースは一切使用していない）**

| ページ | 言語 | 取得した情報 |
|---|---|---|
| `pages-sitemap.xml` | — | 🔴 **2026-08-05 に再取得。全 53 URL。**「Les Hautes Mottes」ページ**不在**の根拠 |
| `/histoire-d-une-famille` | **FR + EN** | 🔴 家族史の全て。1802 / Charles Gonet / Gonet et Fils / 1935 Michel 誕生・食道閉塞の逸話 / **弟たちに譲って離れた** / 妻 Annie / 1986 ボルドー / Sophie・Charles-Henri・Frédéric / Haut-Bacalan / d'Eck / Haut-Brana / 2011 Villa Signolle・37 avenue de Champagne / UNESCO 2015。⚠️ **EN「半世紀以上」/ FR「一世紀半以上」の食い違い** |
| `/terroirs` | **FR + EN** | 🔴 **最重要。EN のみに「38 ha」。FR のみに区画名リスト全 25 区画。** 4 テロワールの土壌・性格 / culture raisonnée・travail des sols・enherbement / **2019 年 VDC 転換開始** |
| `/vinification` | **FR + EN** | 🔴 **最重要。**ギャラリー解説 11 項目 — 区画別圧搾 / cuvée と taille の分離 / **1973 年建設・12 m・12°C のカーヴ** / **12–13°C・2–3 週間** / **2016 年以降 MLF ブロック** / 樽の用途 / **3–15 年 sur latte** / 自社デゴルジュマン・**当年シャルドネのリキュール** |
| `/champagne` | FR | **7 générations** / 「土地が人に属するのではない」/ **テロワール＝pays** の思想 / 現行 7 キュヴェの一覧 |
| `/anamnese` | FR | Anamnèse の全技術情報＋**家族による最詳細テイスティングノート**。**2010 起点の réserve perpétuelle ＋ 2014 以降の各ミレジム** / 部分 MLF / 6 年 / 4.5 g/L |
| `/millesimegrandcru` | EN | 🔴 **OBP #2 の一次情報。** Le Mesnil-sur-Oger, lieu-dit「les Hautes Mottes」/ **MLF あり** / **最低 7 年** / **Zéro dosage 0 g/L** / **VT 2016** / Hachette 2021 2 étoiles |
| `/coeurdemesnil` | EN | vieilles vignes「les Hautes Mottes」/ MLF あり / 最低 10 年 / Extra-Brut 4.5 g/L / VT 2009 / Bettane et Desseauve 16/20 |
| `/authentique` | EN | vieilles vignes「les Hautes Mottes」/ **オーク樽 7 か月** / 最低 10 年 / Extra Brut / VT 2004 |
| `/3terroirs` | EN | Le Mesnil sur Oger + Vindey + Montgueux / MLF なし / 最低 5 年 / Extra-brut 4 g/L / **2009 年から、currently 2020** |
| `/vindey-montgueux` | EN | 🔴 **OBP #1 の一次情報。** Terroirs 欄は **Vindey のみ** / MLF なし / **NV** / **Extra-brut 2 g/L** |
| `/fravaux` | EN | Pinot Noir / Fravaux / MLF なし / Extra Brut 4 g/L |
| `/brut6g` | EN | Pinot Noir / Fravaux / 最低 2 年 / Brut 6 g/L / Gault & Millau 16/20 |
| `/rose` | EN | PN + Chardonnay / Vindey・Montgueux / MLF なし / NV / Extra-Brut 2 g/L |
| `/champagnerose` | EN | Rosé de Saignée / PN / Fravaux / 最低 2 年 / Brut 8 g/L / VT 2007 / G&M 16/20 と引用コメント |
| `/noel` | EN | **Édition de Noël 2023** / Mesnil + Oger GC / 4 年 sur lies / Brut 2 g/L / Sophie Signolle-Gonet のテイスティングノート |
| `/prestige` | EN | Le Mesnil-sur-Oger / 最低 10 年 / **VT 1996・1998** / G&M 15/20・Le Figaro 16/20 |
| `/ratafia` | EN | PN / Fravaux / **18% vol** / VT 1996 / 樽熟成 |
| `/boutique` | EN | 🔴 **商品名の正式表記一覧**（"Grand Cru, Mesnil-sur-Oger, Millésimé" 等）。**Les Hautes Mottes 不在**の第 2 根拠 |
| `/article-hve` | FR | 🔴 **HVE の全経緯。2019 年着手・2020 年末に niveau 3 を目指す・4 つの取り組み・品質責任者 Julie Jeanneau・「30 年近く」** |
| `/revue-presse` | FR | 掲載記事一覧（2016 冬〜2018 秋）。Sommeliers International / Le Figaro Magazine |
| `/downloads` | FR | フィッシュ・テクニック 7 本の配布元（**PDF は取得済みだがテキスト層なし**） |
| `/find-us` | EN | Avize / Bordeaux / Épernay の 3 拠点と住所・電話 |

**取得したが使えなかったもの**
- ⚠️ **テクニカルシート PDF 7 本**（`ts_3terroirs` / `ts_authentique` / `ts_brut6g` / `ts_coeur_de_mesnil` /
  `ts_grandcru_millesime` / `ts_prestige` / `ts_vindey-montgueux`）: **アウトライン化されテキスト抽出不可**
  （`ts_3terroirs` から "Since 2009, currently 2020" のみ回収）。**OCR 未実施。** → Open Questions 6

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
`producer:michel-gonet`（region Champagne / confidence **0.2** / `aliases` 空 / `facts` 空 /
legacy_id `michel-gonet-mesnil-gc-2015` / source `legacy_app`）／
canonical キュヴェ **1 件** `Mesnil-sur-Oger Grand Cru Blanc de Blancs`
（subregion `Côte des Blancs — Le Mesnil-sur-Oger Grand Cru` / vintages **`2015`**）／
OBP **3 本**（`obp_intake_normalized_20260804.json` の 3 行、`batch2.json` の `Michel Gonet` エントリ）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **High** | 法人名・2 拠点の住所・電話・メール・創業年・世代数まで公式で確定。**NM/RM 記号のみ不在** |
| Overview | **High** | 面積・テロワール構成・醸造の署名がいずれも公式一次で裏取り済み |
| History | **Medium-High** | 🔴 **家族史ページが 1 枚あり、創業年・人物・拡張の経緯が揃う。**一方 **EN/FR の年数表現が矛盾**し、**Michel の没年・各シャトーの取得年が不在** |
| Location | **High** | 🔴 **4 テロワール × 全 25 区画名を公式が開示。**「Les Hautes Mottes = 区画名」を **4 出典で独立に確認** |
| **Farming** | **Medium** | 方針（culture raisonnée / travail des sols / enherbement）と認証への着手年は明確。🔴 **ただし認証の到達点が不明**。面積内訳・樹齢・収量は全面非公開 |
| Winemaking | **Medium-High** | 🔴 **圧搾から出荷までの全工程が公式ギャラリーで語られている**（区画別圧搾・12–13°C・カーヴ諸元・熟成年数・自社デゴルジュマン）。⚠️ **MLF で公式同士が矛盾。**酵母・分析値は非公開 |
| Style | **Medium-High** | テロワール別の公式語彙が揃い、Anamnèse には家族の詳細ノートがある。第三者評価は**掲載年が古い** |
| Important Cuvées | **High（ただし 1 本だけ ❓）** | 🔴 **公式 13 キュヴェを全て技術情報つきで確定。OBP 3 本のうち 2 本は公式と完全に接続できた。**残る **Les Hautes Mottes 2018 のみ未接続** |
| Staff Notes | **High** | 全て上記から構成。**矛盾と未確認を 14 項目の ⚠️ で封じた** |
| **総合** | **Medium-High — staff-usable（70% 到達）。** | **OBP の 3 本中 2 本について、産地村・区画・品種・MLF・熟成年数・ドザージュ実値・評価まで公式で埋まった。**3 本目は「区画名である」ところまで確定し、**それ以上を語らせない ⚠️ を置いた。**メゾンの歴史・栽培方針・醸造工程はいずれも一次で語れる。 |

**reached_70: YES.**
根拠 — ①OBP 掲載 3 本すべての公式対応関係を判定済み（2 本確定・1 本は「区画名」まで確定し断定を封じた）
②Farming・Winemaking・Location が公式一次で埋まっている（70% の必須欄）
③⚠️「言ってはいけないこと」14 項目のうち **5 項目が公式内部の矛盾に由来**しており、現場の即興を具体的に塞いでいる。
**不足しているのは分析値・生産本数・認証の到達点であり、いずれも「公式が公開していない」ことを確認済みである。**

---

## Open Questions

1. 🔴 **サイトの現在性が節ごとに違う。** blog / booking の sitemap lastmod は **2026 年**だが、
   キュヴェページは **3 Terroirs = "currently 2020"、Édition de Noël = 2023** で止まっている。
   → **現行ヴィンテージ・現行ドザージュ・Julie Jeanneau の在職が全て未確認。**
   前例（Louis Latour：資料が故人を現当主と記載）に倣い、**人物を現在形で断定していない。**
2. **Michel Gonet（1935 年生）の現況・没年。** 公式に一切記載なし。**現世代は Sophie / Charles-Henri / Frédéric。**
3. 🔴 **VDC と HVE の到達点。** 公式は「**2019 年に着手**」「**2020 年末までに HVE niveau 3 を目指す**」で記述が終わっている。
   **取得できたのか、いつなのか、現在も維持しているのかが不明。** → 現場では認証を名乗らせない運用中。
4. **自社畑 38 ha の裏取り。** **EN `/terroirs` のみ**で確認。FR 版の対応文は本調査の抽出では回収できなかった。
   **区画別の面積内訳は公式に無い。**
5. **canonical `aliases` が空。** `Michel Gonet & Fils` / `SCEV Michel Gonet et Fils` / `Vignobles Michel Gonet`
   が未登録。**`Gonet` 単独表記でのリスト印字が出た場合、確実に取りこぼすか誤解決する。**
6. **テクニカルシート PDF 7 本のテキスト化。** 取得済みだが**テキスト層が無い**。
   **OCR すれば分析値（pH・総酸・アルコール・デゴルジュマン日）が得られる可能性がある。** 未実施。
7. **ボルドー側 8 シャトーの内容。** 専用ページは公式に存在するが、**本調査ではシャンパーニュを優先して未取得。**
   OBP のボルドー欄に Gonet 系が載っている可能性は**未確認**。
8. 🔴 **最重要 — 「Les Hautes Mottes, Brut Nature 2018」（OBP $345）の正体。**
   **区画名であることは確定した**が、**同名キュヴェは公式サイトに存在しない**（53 URL ＋ boutique 商品名で実測）。
   → **必要なのはボトル実物のラベル、または輸入元のテクニカルシート。**
   **Grand Cru Millésimé の後年ヴィンテージと断定してはならない。**
9. **canonical への追加候補の扱い。** `Vindey-Montgueux Blanc de Blancs Extra Brut (NV)` は
   **公式に実在が確定**しており OBP にも載るが **canonical 未登録**。
   また `Mesnil-sur-Oger Grand Cru Blanc de Blancs` は**キュヴェは存在するが vintage 2016 が無い**。
   → **いずれも canonical への書き込みは行っていない。昇格の可否は Akio / CTO 判断。**
10. **Gonet 姓の名寄せ方針。** canonical には Gonet 姓が **1 件しか無い**（384 生産者を全走査）。
    公式家族史が分岐を明記している以上、**別の Gonet が将来のリストに現れる前提が要る。**
    → **producer 照合に「姓だけ一致では確定しない」ガードが必要かどうかは architecture 側の判断。**
    本書では**提起のみ。実装も canonical 変更も行っていない。**
