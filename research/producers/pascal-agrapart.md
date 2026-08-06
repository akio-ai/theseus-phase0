# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:pascal-agrapart` および `producer:agrapart-and-fils` は**一切変更していない**。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagnepascalagrapart.com で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では事実の根拠として一切使っていない**）／ `⚠️` 食い違い。両方を残す
> `🔍` THÉSEUS DB / OBP intake / 公式値からの機械的導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 一次資料: `https://www.champagnepascalagrapart.com/`（FR 原文・`Default.aspx`）、
> `https://www.champagnepascalagrapart.com/default-en.aspx`（EN 訳）、`https://www.champagnepascalagrapart.com/mention.aspx`（法的表示）
>
> 🔴 **本書の 4 つの前提**
> 1. **公式サイトは HTML 3 枚しか存在しない。** Wayback CDX で全ドメインを走査した結果、`text/html` は
>    `Default.aspx` / `default-en.aspx` / `mention.aspx` の 3 本のみ。**下位ページは全て 404**
>    （旧サイトの `/en/AVIZOISE-44.aspx` `/en/Complantee-42.aspx` `/en/Venus-45.aspx` `/en/winery-31.aspx` は
>    現在 404 で、**Wayback にも 200 の捕獲が 1 件も無い**）。1 ページ完結のモーダル構成。
> 2. ⚠️ **テクニカルシート PDF は存在しない。** FR / EN / mentions の HTML 全文を走査して `.pdf` 参照はゼロ。
>    CDX 全 134 行にも PDF は 1 件も無い。**Louis Latour 型の PDF 収穫はこの生産者では不可能。**
> 3. 🔴 **公式サイトに沿革が一行も無い。** 創業年・世代・相続・「& Fils」の由来 — **すべて公式に存在しない。**
>    出てくる人名は連絡先ブロックの **«Pascal et Ambroise Agrapart»** の一箇所だけ。
> 4. 🔴 **canonical が 2 実体に割れている**（`pascal-agrapart` / `agrapart-and-fils`）。**§Canonical Conflict を必ず読むこと。**
>    公式サイトは**この重複を決着させる証拠を持っている。**
>
> **取得済みローカル素材** — `/Users/akiomatsumoto/Theseus_Phase0/research/producers/_sources/pascal-agrapart/`
> `home-fr-20260804.html` `home-en-20260804.html`（2026-08-04 実取得。既存の `home.html` `home-en.html` と**本文テキスト完全一致**を確認済み）
> `mention.html` ／ `plan.jpg`（**公式の手描き区画図。一次資料として使用**）／ `Fresque-1b.png` `Fresque-2b.png`（挿絵。文字情報なし）
> `cdx.txt` ／ Wayback 捕獲 16 本（`wayback-2022-07-03.html`〜`wb-20260511233230.html`。**公式記述の経年変化の追跡に使用**）

---

## Identity

| | |
|---|---|
| **Canonical Name** | Pascal Agrapart |
| **公式サイトの自称** | **«CHAMPAGNE PASCAL AGRAPART»** ✅（`<title>`・サイトロゴ・ドメイン名すべてこれ） |
| **法人名** | **SCEV Champagne Pascal Agrapart** ✅（`mention.aspx`。SCEV au capital de 1 000,00 euros） |
| **連絡先の名義** | **«Pascal et Ambroise Agrapart»** ✅（**2 名連名**。役割分担・当主の別は公式に無し ❓） |
| **Aliases** | 🔴 canonical `aliases` は**空**。実務上の別名は「Agrapart」「Agrapart & Fils」「アグラパール」 |
| **業態** | **Propriétaire Récoltant – Manipulant** ✅ ／ EN «Grape grower – winemaker» ／ **«pas d'achat de raisins»（葡萄を一切買わない）と明記** |
| **所在** | **57, Avenue Jean Jaurès, 51190 AVIZE** ✅ ／ Tel +33 (0)3 26 57 51 38 |
| **見学・直販** | 🔴 **«Pas de vente ni visite au domaine»＝ドメーヌでの販売も見学も無し** ✅（EN «Neither sales nor visit at the domain»） |
| **登記** | RCS **Reims 531 932 820** ✅ |
| canonical id | `producer:pascal-agrapart`（キュヴェ 2・OBP 2）／ 🔴 別レコード `producer:agrapart-and-fils`（キュヴェ 7・OBP 0）が併存 |
| canonical entity confidence | 0.2（source: `legacy_app`）— エンティティ同定の確度。本書の充実度とは別軸 |

🔴 **公式サイト全文（FR + EN + mentions）に «Fils» という語は 1 度も現れない。** grep で確認済み（ヒット 0）。
**公式の自称は一貫して «Champagne Pascal Agrapart» である。** → §Canonical Conflict の中心証拠。

⚠️ `mention.aspx` の ADEME 欄に **SIRET 78038582900012** が記載されるが、これは «Ressortissant du Comité Champagne»
（＝Comité Champagne の傘下として）という文脈で置かれており、**RCS Reims 531 932 820 と SIREN が一致しない。**
どちらが SCEV 自身の番号かは**公式の文面からは判定できない** ❓。**両方をそのまま残す。**

---

## Overview

✅ **コート・デ・ブラン、アヴィーズ（Avize）の Propriétaire Récoltant–Manipulant。** 公式サイトは業態の説明に
**«pas d'achat de raisins»（葡萄の買い付けを行わない）** をわざわざ括弧書きで添えている。**全量自社畑・自社収穫・自社圧搾。**

✅ **畑は 12 ヘクタール**（⚠️ 後述。2025 年春までは公式に 10ha）。**主にグラン・クリュ村に広がり、植えられているのはシャルドネ。**
公式の言い回しは «Des raisins blancs récoltés et pressés par nos soins»（白葡萄を自分たちの手で収穫し圧搾する）。

✅ **栽培の姿勢は «Notre approche vigneronne est naturelle»（我々の作り手としての姿勢は自然なものである）。**
土壌は**一貫して耕耘（labour）で維持**され、**毎年、地元産の材料でつくった堆肥を畑に入れる**。
**«La vie biologique des sols génère santé et productivité du vignoble»**（土壌の生物的活性が畑の健康と生産性を生む）。

✅ **醸造の公式記述は 3 点だけ** — **無清澄・無濾過（«ni collés ni filtrés»）／瓶詰めはドメーヌで行う／ルミュアージュ（動瓶）は手作業。**

✅ **公式ラインナップは 7 キュヴェ**: `7 Crus` `Terroirs` `Complantée` `Minéral` `Avizoise` `Vénus` `Expérience`。
**全キュヴェに共通して «Dégorgement 2 mois avant la vente»（販売の 2 ヶ月前にデゴルジュマン）。**

---

## History

### 🔴 公式サイトに沿革が存在しない

**創業年・世代交代・家族史・「& Fils」の由来 — すべて公式に一行も書かれていない。** ページ構成上、History に相当する
セクション自体が無い（旧サイトにあった `/en/winery-31.aspx` は現在 404、**Wayback にも 200 の捕獲が無い**）。

**公式から取れる「人」の情報は 1 箇所のみ** ✅ — 連絡先ブロックの見出し **«Pascal et Ambroise Agrapart»**。
**2 名の連名であること以上のことは書かれていない。** 続柄・役割・当主の別・就任年 — **すべて ❓。**

### ✅ ただし「公式記述の変化」は年月まで追える（Wayback 捕獲 16 本による）

**これは沿革の代用にはならないが、「いつ時点の話か」を確定できる唯一の材料である。**

| 項目 | 旧（確認できる最後） | 新（確認できる最初） | 変更が起きた窓 |
|---|---|---|---|
| **畑の面積** | **10 hectares**（〜**2025-02-16** 捕獲） | **12 hectares**（**2025-05-13** 捕獲〜現在） | **2025-02 〜 2025-05** |
| **7 Crus の格付け表示** | **Champagne Brut** | **Champagne Extra Brut** | **2024-04 〜 2025-01** |
| **7 Crus のドザージュ** | **7 g/L** | **5 g/L** | 同上 |
| **7 Crus の Premier Cru 村** | **COLIGNY** | **VAL DES MARAIS** | 同上 |
| **Terroirs の容量** | bouteille + magnum | **bouteille + magnum + jéroboam** | 2024-04 〜 2025-01 |
| **Avizoise / Vénus の容量** | «uniquement en bouteille» | **bouteille + magnum** | 同上 |
| **瓶詰めの表現** | «La mise en bouteille s'effectue **à la main** sur bouchons de liège et agrafes» | «La mise en bouteille s'effectue sur bouchons de liège et agrafes»（**«à la main» が削除**） | 同上 |

🔴 **したがって「12ha」「Extra Brut」「5 g/L」はすべて 2025 年以降の公式値である。**
**OBP に載っているのは 2015 ヴィンテージの 2 本であり、これらの数値を 2015 年のボトルに当てはめてはならない。**
⚠️ **COLIGNY → VAL DES MARAIS の書き換えが、村名（自治体）の変更なのか調達先の変更なのかは公式に説明が無い ❓。**
**「コリニーの畑をやめた」とも「同じ畑の名前が変わっただけ」とも言えない。**

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Champagne — **Côte des Blancs** ✅（公式が明記） |
| **Village（本拠）** | **AVIZE**（51190）✅ |
| **面積** | **12 ha** ✅（採用値）／ ⚠️ **10 ha**（2025 年 2 月まで公式）。**両方残す** |
| **主要品種** | **Chardonnay**（«principalement sur des Grands Crus plantés de cépage Chardonnay»）✅ |

### 調達している村（7 crus）✅

| 格付け | 村 |
|---|---|
| **Grand Cru（4）** | **AVIZE / CRAMANT / OIRY / OGER** |
| **Premier Cru** | **AVENAY VAL D'OR / VAL DES MARAIS / VAUCIENNES** |

⚠️ **公式は «2 Premiers Crus» と書きながら 3 村を列挙している。** FR / EN 両方で同じ。訳の誤りではない。
🔍 キュヴェ名「7 Crus」および «parcelles de 7 villages» と整合するのは **4 + 3 = 7**、すなわち「3 Premiers Crus」。
**しかし公式表記は «2» である。数字を勝手に直さない。現場で村数を数えて話さない。** → Open Questions。

❓ **各 Premier Cru 村がどのサブリージョンにあるか、どの品種が植わっているかは公式に記載が無い。**
7 Crus が «90% chardonnay et 10% pinot noir» であることは公式だが、**その pinot noir がどの村由来かは公式に書かれていない。**

### 公式が名指ししている畑（lieux-dits）✅

**5 つ。すべて公式サイト本文＋公式の手描き区画図 `plan.jpg` の両方で確認。**

| 畑名 | 村 | 使われるキュヴェ | 公式の地質記述 |
|---|---|---|---|
| **Le Champ Bouton** | AVIZE | **Minéral** | **«Un sol mince tout de suite sur la craie»＝薄い表土のすぐ下が白亜** |
| **Les Bionnes** | CRAMANT | **Minéral** | 同上（Champ Bouton と**同じ地質プロファイル**として選ばれている） |
| **Les Robarts** | AVIZE | **Avizoise** | **«Un sol avec des argiles plus profondes avant la craie»＝白亜の手前に、より深い粘土** |
| **Les Gros Yeux** | AVIZE | **Avizoise** | 同上 |
| **La Fosse aux Pourceaux** | AVIZE | **Vénus** | **60 ares（0.6 ha）の単一区画** |

✅ **公式区画図 `plan.jpg`** は AVIZE / CRAMANT / OIRY の位置関係、Bois de Saran・Bois d'Avize、
上記 5 つの lieu-dit、そして**アヴィーズ村内のドメーヌ位置（赤い ⊗ 印）**を手描きで示している。
**畑名の綴りは図でも本文と一致**（`LES BIONNES` `LE CHAMP BOUTON` `LA FOSSE AUX POURCEAUX` `LES GROS YEUX` `LES ROBARTS`）。

⚠️ **Minéral の 2 区画は、2022 年時点の公式では «Bionnes à CRAMANT et Champbouton à AVIZE» の順・綴りだった**
（現在は «Champ bouton à AVIZE et Bionnes à CRAMANT»）。**同じ 2 区画であり、順序と分かち書きだけの差。**

❓ **公式に無いもの**: 村ごとの面積内訳、区画数、樹齢、植栽密度、台木、仕立て、標高、向き、土壌分析値。
**Complantée と Expérience の区画名も公式には無い**（Complantée は «terroir d'AVIZE»、Expérience は «vieilles vignes d'Avize» とだけ）。

---

## Farming

### ✅ 公式が書いていること — 3 点だけ

1. **«Notre approche vigneronne est naturelle»** — 作り手としての姿勢は自然なもの。
2. **«Les sols de notre vignoble ont toujours été entretenus par le labour»** —
   **土壌は「常に」耕耘によって維持されてきた。**（EN «have always been maintained through ploughing»）
   🔍 **«toujours»（常に）という語が入っているのが要点。**「途中で除草剤をやめた」のではなく「一度も使わずに耕してきた」という主張。
   ⚠️ **ただし公式は除草剤・殺虫剤・銅・硫黄について一言も述べていない。**「耕してきた」から「無農薬」を導かないこと。
3. **«nous déposons, chaque année à la vigne, un compost d'ingrédients locaux»** —
   **毎年、地元産の材料でつくった堆肥を畑に入れる。** 目的は **«La vie biologique des sols génère santé et productivité du vignoble»**
   （土壌の生物的活性が、畑の健康と生産性を生む）。

### ✅ 区画単位の例外 — Vénus のみ

**«Aucun engin mécanique lourd n'est intervenu pour l'entretien de cette vigne, travaillée uniquement par l'homme et le cheval.»**
= **重い機械を一切入れず、人と馬だけで手入れした畑。** EN «which has solemnly been worked by man and by horse»。
**公式が「馬」に言及するのは Vénus の 60 ares のこの 1 箇所のみ。他の区画については何も書いていない。**

### 🔴 最重要 — 認証の記載がゼロである

**公式サイト全文（FR + EN + mentions）を grep した結果、以下の語のヒットは 0 である。**
`bio` / `biodynamie` / `biodynamic` / `Demeter` / `Biodyvin` / `Ecocert` / `HVE` /
`Viticulture Durable en Champagne (VDC)` / `certifié` / `certification` / `certified` / `conversion` / `durable`。

⚠️ **唯一の例外は `biologique` 1 件だが、これは認証の文脈ではない** —
**«La vie biologique des sols génère santé et productivité du vignoble»（土壌の“生物的”活性）** の一語であり、
**「ビオロジック（有機栽培）」の意味では使われていない。EN 訳も «The organic life of the soil» と訳している。**
🔴 **この 1 語を「オーガニックと公式に書いてある」と読み違えないこと。EN の «organic life» は特に誤読を誘う。**

🔴 **Prévost（«viticulture sans papier»）と違い、Agrapart は認証の不在を宣言してもいない。単に何も書いていない。**
**つまり「認証を持っている」とも「持っていない」とも公式からは言えない。**
→ **現場では認証の話に入らない。** §Staff Notes の禁止リスト参照。

---

## Winemaking

### ✅ 公式が書いていること（全部で 5 項目しかない）

| 項目 | 公式記述 | 適用範囲 |
|---|---|---|
| **清澄・濾過** | **«Nos vins de Champagne ne sont ni collés ni filtrés»＝清澄も濾過もしない** | **全キュヴェ** |
| **瓶詰め場所** | **«La mise en bouteille a lieu au domaine»＝瓶詰めはドメーヌで行う** | **全キュヴェ** |
| **ルミュアージュ** | **«le remuage est manuel»＝動瓶は手作業** | **全キュヴェ** |
| **打栓** | **«sur bouchons de liège et agrafes»＝コルク栓＋アグラフ（留め金）** | **Avizoise / Vénus / Expérience の 3 つのみ** |
| **デゴルジュマン** | **«Dégorgement 2 mois avant la vente»＝販売の 2 ヶ月前に澱抜き** | **全キュヴェ** |

⚠️ **«sur bouchons de liège et agrafes» は EN 訳では «Bottled under cork.» としか書かれておらず、«agrafes» が落ちている。**
**採用は FR 原文。** EN だけを読むと「コルク栓」で終わってしまう。
⚠️ **2022 年時点の公式は «La mise en bouteille s'effectue à la main sur bouchons…»（手作業で）だった。**
**現在の版から «à la main» が削除されている。**「瓶詰めも手作業」と言わないこと。**現在の公式は打栓方式しか言っていない。**

### ✅ アッサンブラージュの構造

- **`7 Crus` `Terroirs` `Complantée` の 3 つは «2 millésimes assemblés»＝2 つのミレジムのアッサンブラージュ。** ✅
  🔴 **公式が言っているのは「2 ミレジムの組み合わせ」だけである。**「リザーブワイン」「ソレラ」「réserve perpétuelle」
  「永久リザーブ」— **これらの語は公式に一切無い。**
- **`Minéral` `Avizoise` `Vénus` は «Toujours millésimée»＝常にミレジメ。** ✅
- **`Expérience` は公式に «Millésimé» と書かれていない。** ⚠️ 他 3 つと違い «Toujours millésimée» の一文が無い。
  **にもかかわらず OBP・canonical はヴィンテージ 2015 を持つ。**→ Open Questions。

### ✅ ドザージュ（現行リリース）

| キュヴェ | 表示 | ドザージュ |
|---|---|---|
| 7 Crus / Terroirs / Complantée | **Extra Brut** | **≤ 5 g/L**（«dosage limité à 5 grammes de sucre / litre»） |
| Minéral / Avizoise | **Extra Brut** | **≤ 3 g/L** |
| Vénus / Expérience | **Brut Nature** | **«sans dosage»＝ドザージュなし** |

⚠️ **7 Crus は 2024 年 4 月時点でまだ «Brut / 7 g/L» だった。**（§History の表）
**数値は現行リリースに対する記述であり、過去のボトルには適用できない。**

### 🔴 公式が一言も書いていないこと（＝語ってはいけない領域）

**圧搾（プレス機の型・キュヴェ／タイユの別）／ 発酵容器（樽・ステンレス・その別）／ 新樽比率 ／ トヌリエ名 ／
酵母（自生・培養の別）／ マロラクティック発酵（実施の有無・方針）／ 澱との接触期間 ／ 瓶熟期間 ／
デゴルジュマンの実施年月 ／ ドザージュのリキュール組成 ／ SO2 ／ 年間生産本数 ／ 収量。**

🔴 **Agrapart について世間で最もよく語られる「樽」の話は、公式サイトに 1 文字も無い。**
`fût` `barrique` `foudre` `chêne` `bois` `oak` `barrel` — **全て grep でヒット 0。**

---

## Style

### ✅ 公式が使っている味わいの語は、実質 4 つのキュヴェ分しかない

| キュヴェ | 公式の見出し | 公式の味わい記述 |
|---|---|---|
| **7 Crus** | **«Un champagne de gourmandise»**（美味しさ／食い気のシャンパーニュ） | それ以上の記述なし |
| **Terroirs** | **«Le terroir s'affirme»**（テロワールが自己主張する） | **«Rencontre de nos Grands Crus»**（我々のグラン・クリュたちの出会い） |
| **Complantée** | **«Un assemblage à la parcelle, un terroir omniprésent»**（区画そのものがアッサンブラージュ、遍在するテロワール） | 記述なし |
| **Minéral** | **«La valeur terroir prend effet»** | 🔴 **«Précise, sapide et saline»（精確・サピッド・塩味）／ «Minéral nous offre la dimension crayeuse de son terroir»（テロワールの白亜的次元を差し出す）** |
| **Avizoise** | **«Un terroir généreux»** | 🔴 **«densité et richesse, à la fois gastronome et élégante»（密度と豊かさ、ガストロノミックであり同時にエレガント）** |
| **Vénus** | **«Un terroir unique»** | **«l'emblème parcellaire du domaine»（ドメーヌの区画の象徴）** — 味わい記述ではない |
| **Expérience** | **«100 % raisins»（100% 葡萄）** | **«Défi ultime du champagne nature»（ナチュールなシャンパーニュの究極の挑戦）** — 味わい記述ではない |

### 🔍 構造から導けるハウススタイル（導出であり公式の主張ではない）

🔍 **① 選定軸が「村」ではなく「地質」である。** Minéral は **Avize と Cramant という別の村の 2 区画**を、
**«pour leur même profil géologique»（同じ地質プロファイルであるがゆえに）** 束ねている。
Avizoise は **Avize 内の 2 区画**を、やはり同じ理由で束ねる。**公式の選定基準は村の格ではなく土壌断面である。**

🔍 **② Minéral と Avizoise は、同じ造り手による対照実験として設計されている。**
**薄い表土 → すぐ白亜（Minéral: 精確・塩味・白亜的）** ⟷ **深い粘土 → その先に白亜（Avizoise: 密度・豊かさ）。**
**両者ともドザージュ ≤3 g/L、ともに常にミレジメ。醸造条件を揃えて土壌だけを変えている読み方ができる。**

🔍 **③ ドザージュが階段状に設計されている。** 5 g/L（アッサンブラージュ系 3 種）→ 3 g/L（区画系ミレジメ 2 種）
→ 0（Vénus / Expérience）。**キュヴェの階層とドザージュの減少が完全に一致する。**

🔍 **④ 無清澄・無濾過が全キュヴェに掛かる。** キュヴェごとの例外が公式に書かれていない。

⚠️ **第三者評価・点数・「◯◯年が当たり年」の類は公式に一切無い。Confidence: Low。**

---

## Important Cuvées

### 公式ラインナップ 7 キュヴェ ✅ ／ canonical・OBP との対応

| # | 公式キュヴェ | 公式の表示 | 品種・出所 | ドザージュ | 容量 | canonical | OBP |
|---|---|---|---|---|---|---|---|
| 1 | **7 Crus** | Champagne **Extra Brut** | **90% chardonnay / 10% pinot noir**、7 村（GC 4 + 1er Cru 3）、**2 ミレジム** | ≤ 5 g/L | **bouteille のみ** | ✅ `agrapart-and-fils` 側に登録 | ✗ |
| 2 | **Terroirs** | Extra Brut / **Blanc de Blancs Grand Cru** | Avize・Cramant・Oiry・Oger の選抜区画、全て chardonnay、**2 ミレジム** | ≤ 5 g/L | **bouteille / magnum / jéroboam** | ✅ `agrapart-and-fils` 側 | ✗ |
| 3 | **Complantée** | Extra Brut / **Grand Cru**（⚠️ **BdB とは書かれていない**） | **6 品種の混植** = chardonnay, pinot noir, pinot meunier + **arbane, petit meslier, pinot blanc**、AVIZE、**2 ミレジム** | ≤ 5 g/L | **bouteille のみ** | ✅ `agrapart-and-fils` 側 | ✗ |
| 4 | **Minéral** | Extra Brut / BdB **Grand Cru** / **Millésimé** | **Champ Bouton（Avize）＋ Bionnes（Cramant）**、薄い表土＝白亜直下 | **≤ 3 g/L** | bouteille / magnum | 🔴 **両実体に重複登録**（`pascal-agrapart` 2015 ／ `agrapart-and-fils` 2018） | ✅ **1 本** |
| 5 | **Avizoise** | Extra Brut / BdB **Grand Cru** / **Millésimé** | **Robarts ＋ Gros Yeux（ともに Avize）**、深い粘土の先に白亜 | **≤ 3 g/L** | bouteille / magnum | ✅ `agrapart-and-fils` 側 | ✗ |
| 6 | **Vénus** | **Brut Nature** / BdB **Grand Cru** / **Millésimé** | **Fosse aux Pourceaux（Avize）60 ares 単一区画**、**人と馬のみ** | **0（sans dosage）** | bouteille / magnum | ✅ `agrapart-and-fils` 側 | ✗ |
| 7 | **Expérience** | **Brut Nature** / BdB **Grand Cru**（⚠️ **Millésimé と書かれていない**） | **Avize の vieilles vignes**、**«sans aucun intrant exogène»＝外来の投入物を一切使わず** | **0（sans dosage）** | **bouteille のみ** | 🔴 **両実体に重複登録**（`pascal-agrapart` 2015 ／ `agrapart-and-fils` 2019） | ✅ **1 本** |

🔍 **7 キュヴェ全てが公式に実在し、canonical にも全て存在する。ただし 2 つの producer レコードに割れている。**
**`agrapart-and-fils`（7 キュヴェ）と `pascal-agrapart`（2 キュヴェ）の和集合が、ちょうど公式ラインナップ 7 と一致する。**

### OBP 掲載分（2 本）— 印字そのまま 🔍

| # | OBP 印字 | VT | 価格 | セクション | intake state | 公式との照合 |
|---|---|---|---|---|---|---|
| 1 | `'Minéral,' Grand Cru` | **2015** | 520 | FRANCE \| SPARKLING > CHAMPAGNE \| **BLANC DE BLANCS** | `alias` | ✅ **公式 «Minéral / Blanc de Blancs Grand Cru» と一致。セクション配置も正しい。** |
| 2 | `'Experience,' Grand Cru Brut Nature` | **2015** | 960 | 同上 | `alias` | ✅ **公式 «Expérience / Brut Nature / Blanc de Blancs Grand Cru» と一致。** |

**`source_quality_flags` は 2 本とも空。`obp_unresolved` = 0。🔍 通貨単位は intake に記録が無い ❓。**

🔴 **OBP の 2 本は「印字が公式と食い違っていない」という意味では THÉSEUS で最もクリーンな部類。**
**問題はキュヴェ側ではなく producer 側の重複にある。**

⚠️ **アクセントの揺れ**: 公式は **«Expérience»**（é）、OBP 印字も canonical 名も **«Experience»**（é なし）。
**Minéral は公式・OBP とも é が保たれている。**（C-1 Egly-Ouriet と同型のアクセント揺れ。ただし本件は OBP 側の 1 レコードのみ）

🔴 **2015 ヴィンテージに現行スペックを当てないこと。**
公式ページが述べる **≤3 g/L（Minéral）／ sans dosage（Expérience）／ 12ha** は、**いずれも 2025 年以降の公式記述である。**
**2015 年産のボトルの実ドザージュ・デゴルジュマン時期は、公式サイトからは確定できない ❓。**

---

## Staff Notes

> この節は上の ✅ からのみ構成している。裏の取れていない事柄は書いていない。
> 🔴 **公式サイトが極端に薄い生産者。だから ⚠️ 禁止リストが本体である。**
> **OBP に載っている 2 本は「キュヴェとしては安全」。危ないのは、造り手の背景を即興で埋めてしまうこと。**

**一行で言うと** — 「**コート・デ・ブラン、アヴィーズの造り手。葡萄は一切買わず、自社の 12 ヘクタールだけ。
畑を「村」ではなく「土の断面」で選び分けている造り手です。**」

### ゲストへの説明の芯（3 点）

**1. 葡萄を買わない。アヴィーズの自社畑 12 ヘクタールだけ。**
**Propriétaire Récoltant–Manipulant** で、公式に **«葡萄の買い付けはしない»** と書いています。
**畑は 12 ヘクタール、主にグラン・クリュ村で、植わっているのはシャルドネ。収穫も圧搾も自分たちの手で。**
グラン・クリュは **アヴィーズ、クラマン、オワリー、オジェ**。

**2. 畑を「村」ではなく「地質」で選んでいる。ここがこの造り手の設計思想です。**
**«Minéral» は、アヴィーズの «シャン・ブトン» とクラマンの «ビオンヌ» — 村は違うのに、
「同じ地質プロファイルだから」という理由で束ねられた 2 区画**から造られます。土は薄く、**すぐ下が白亜**。
公式の言葉で **«精確で、サピッドで、塩味がある»**、**«テロワールの白亜的な次元を差し出す»**。
対になるのが **«Avizoise»** で、こちらはアヴィーズの **«ロバール»** と **«グロ・ジュー»**。
**白亜の手前に、より深い粘土**があり、**«密度と豊かさ、ガストロノミックでありながらエレガント»** と書かれています。
**同じ造り手・同じドザージュ（3 g/L 以下）・同じミレジメで、土だけを変えてある。**

**3. 造りは、公式が言っていることだけで十分に強い。**
**清澄も濾過もしない。瓶詰めはドメーヌで。動瓶（ルミュアージュ）は手作業。**
**デゴルジュマンは販売の 2 ヶ月前**（＝出荷直前に澱を抜く）。畑は**一貫して耕耘で維持され、毎年、地元の材料でつくった堆肥**を入れます。
**«Expérience» は「外来の投入物を一切使わない」ブリュット・ナチュール**で、公式自身が **«ナチュールなシャンパーニュの究極の挑戦»** と呼んでいます。

### リストの 2 本 — そのまま使える説明

| リストの印字 | 現場で言えること |
|---|---|
| **`'Minéral,' Grand Cru` 2015 / 520** | ✅ 公式キュヴェと完全一致。**「アヴィーズのシャン・ブトンとクラマンのビオンヌ。薄い表土の、すぐ下が白亜。常にミレジメの、ブラン・ド・ブランのグラン・クリュです。」** 味わいは公式の語をそのまま — **「精確、サピッド、塩味」**。⚠️ **ドザージュの数字は言わない**（3 g/L は現行リリースの値）。 |
| **`'Experience,' Grand Cru Brut Nature` 2015 / 960** | ✅ 公式キュヴェと完全一致。**「アヴィーズの古樹から。外から何も加えずに造る、ドザージュ・ゼロのブリュット・ナチュール。コルク栓とアグラフで瓶詰めされます。造り手自身が『ナチュールなシャンパーニュの究極の挑戦』と呼んでいるキュヴェです。」** ⚠️ **「ミレジメ」と言わない**（公式は Expérience にだけ «Toujours millésimée» を付けていない）。⚠️ **「亜硫酸無添加」と言い換えない。** |

### 「オーガニックですか？」と訊かれたら（頻出・最重要）

🔴 **認証の話に入らない。公式が書いている事実だけを返す。**

> 「**土は昔から耕して管理していて、毎年、地元の材料でつくった堆肥を畑に入れている**、と造り手自身が書いています。
> **«Vénus» という区画は 60 アールしかなくて、重い機械を一切入れず、人と馬だけで手入れしている**そうです。
> **認証については公式に記載がないので、こちらでは確認が取れていません。**」

**これで止める。** «bio» «biodynamie» «Demeter» «HVE» — **公式サイトに 1 語も無い。**

### 「樽で造っているんですよね？」と訊かれたら

🔴 **「公式には書かれていません」で止める。**

> 「**造りについて公式が明かしているのは、清澄も濾過もしないこと、瓶詰めをドメーヌで行うこと、動瓶が手作業であること、
> デゴルジュマンが販売の 2 ヶ月前であること — この 4 点だけ**なんです。**発酵容器については公表されていません。**」

**`fût` `barrique` `foudre` `oak` — 公式サイトに 1 文字も無い。** grep でヒット 0 を確認済み。

### ⚠️ 現時点で言ってはいけないこと

- 🔴 **「オーガニック」「ビオ」「ビオロジック」「ビオディナミ」「Demeter」「Biodyvin」「AB」「HVE」「VDC」「認証取得」「転換中」**
  — **公式サイトに 1 語も無い。** 公式にあるのは «approche naturelle» / labour / compost / 馬（Vénus のみ）だけ。
- 🔴 **「無農薬」「除草剤不使用」「殺虫剤不使用」「銅を使わない」** — **公式は農薬・除草剤・銅・硫黄に一言も触れていない。**
  «toujours entretenus par le labour»（常に耕耘で維持）から農薬の不使用を導かない。
- 🔴 **「樽で発酵」「オーク熟成」「新樽◯%」「フードル」「◯◯社の樽」** — **公式に完全にゼロ。**
- 🔴 **「マロラクティックは通さない／通す」「自生酵母」「野生酵母」** — **公式に記載なし。**
- 🔴 **「リザーブワイン」「ソレラ」「réserve perpétuelle」「永久リザーブ」** — **公式は «2 millésimes assemblés»（2 ミレジムの組み合わせ）としか書いていない。**
- 🔴 **「◯年瓶熟」「デゴルジュマンは◯年◯月」** — 公式は **«販売の 2 ヶ月前にデゴルジュマン»** だけ。**熟成期間は非公開。**
- 🔴 **「亜硫酸無添加」「SO2 ゼロ」** — **Expérience の «sans aucun intrant exogène»（外来の投入物なし）を SO2 の話に翻訳しない。**
  **公式は SO2 という語を一度も使っていない。**
- 🔴 **「年間◯◯本」「◯◯ケースしか造らない」** — **生産量は完全に非公開。**
- 🔴 **創業年・「◯代目」・「祖父の代から」・「& Fils の由来は…」** — **公式サイトに沿革が一行も無い。**
  **年号を口にした時点で公式の裏が無い。**
- 🔴 **「現当主は Ambroise（あるいは Pascal）」「息子に代替わりした」** — **公式は «Pascal et Ambroise Agrapart» という連名だけ。**
  続柄も役割も就任年も書かれていない。**現在性未確認。**
- 🔴 **「Vénus は馬の名前」** — **公式が書いているのは「区画名は La Fosse aux Pourceaux」「人と馬だけで作業」の 2 点のみ。**
  **キュヴェ名 Vénus の由来は公式に一切説明が無い。**
- 🔴 **「ドメーヌで試飲できます」「訪問できます」** — **公式明記 «Pas de vente ni visite au domaine»＝販売も見学も無し。**
- ⚠️ **「畑は 12 ヘクタール」を 2015 年のボトルの説明として言わない。** **12ha は 2025 年春以降の公式値。それ以前は 10ha。**
- ⚠️ **「7 Crus はブリュット」「ドザージュ 7 グラム」** — **2024 年までの旧表記。現行は Extra Brut・5 g/L。**
  逆に**現行の数値を古いボトルに当てない。**
- ⚠️ **「4 つのグラン・クリュと 2 つのプルミエ・クリュ」と村数を数えない。** **公式は «2 Premiers Crus» と書きながら 3 村を列挙している。**
  安全な言い方は「**グラン・クリュ 4 村を中心に、7 つの村から**」。
- ⚠️ **Complantée を「ブラン・ド・ブラン」と言わない。** **公式表示は «Grand Cru» のみで、6 品種の混植。**
- ⚠️ **Expérience を「ミレジメ」と断定しない。** **«Toujours millésimée» が付くのは Minéral / Avizoise / Vénus の 3 つだけ。**
- ⚠️ **「Agrapart & Fils」と「Pascal Agrapart」を別の造り手として説明しない。** **同一生産者である蓋然性が極めて高い**（§Canonical Conflict）。
  ただし**「Agrapart & Fils が正式名称です」とも断定しない** — **公式サイトにその表記は存在しない。**

---

## Akio's Insight

*（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）*

---

## Canonical Conflict

🔴 **本件は既に登録済みである。** `/Users/akiomatsumoto/Theseus_Phase0/research/canonical_conflicts/REGISTER.md` の
**`P-3` Agrapart & Fils / Pascal Agrapart**（分類: 実体分裂／頻度 1 組／影響 2 本＋Packet C で衝突確定／Confidence High）。
**本節は重複記載ではなく、公式サイト調査で新たに得られた証拠の追加である。**
🔴 **REGISTER.md への追記が必要**（本節③の新 Evidence 2 点）。**REGISTER.md 自体は編集していない。**

### ① 衝突している canonical ID

- **`producer:agrapart-and-fils`** — "Agrapart & Fils"（Champagne, legacy_ids 7, キュヴェ **7**, OBP **0**）
- **`producer:pascal-agrapart`** — "Pascal Agrapart"（Champagne, legacy_ids 2, キュヴェ **2**, OBP **2**, confidence 0.2, aliases 空）

### ② なぜ重複に見えるか

姓 `agrapart` を共有し、**配下キュヴェ名が 2 件完全一致**する
（`Minéral Blanc de Blancs Grand Cru Extra Brut` ／ `Experience Blanc de Blancs Grand Cru Brut Nature`）。
同名キュヴェが**別ヴィンテージで 2 実体に分散**している（and-fils: 2018 / 2019、pascal: 2015 / 2015）。**取り込み時の分割痕。**

### ③ Evidence

**（既知・REGISTER.md 記載済み）**
- キュヴェ名 2 件が完全一致し、ヴィンテージが 2 実体に分かれている。
- `agrapart-and-fils` 側の 7 キュヴェが Avize の実ラインナップと整合。

**🔴（本調査で新たに得た証拠 — 追記が必要）**

**新 Evidence 1: 公式ラインナップと canonical の和集合が完全一致する。**
公式サイトが掲げるキュヴェは **`7 Crus` `Terroirs` `Complantée` `Minéral` `Avizoise` `Vénus` `Expérience` の 7 つで確定**
（1 ページ完結・他ページ無しを CDX で確認済み）。
**`agrapart-and-fils` の 7 キュヴェ ∪ `pascal-agrapart` の 2 キュヴェ = 7 種類**であり、
**公式ラインナップと過不足なく一致する。** 🔴 **2 実体が「別の生産者」であれば、この一致は起こり得ない。**
**同一生産者であることは、キュヴェ名の一致だけでなくラインナップ全体の同型性からも裏づけられる。**

**新 Evidence 2: 公式サイトに «Fils» が 1 文字も存在しない。**
FR 原文 `Default.aspx`・EN 訳 `default-en.aspx`・法的表示 `mention.aspx` の全文を grep して **`fils` のヒットは 0**。
**公式の自称は一貫して «CHAMPAGNE PASCAL AGRAPART»**（`<title>`／ロゴ／`meta description` は «CHAMPAGNE AGRAPART»）、
**法人名は «SCEV Champagne Pascal Agrapart»**、**ドメインは `champagnepascalagrapart.com`**。
**別ドメインの公式サイトも確認できない** — `agrapart.com` / `champagne-agrapart.com` / `champagneagrapart.com` /
`agrapartetfils.com` / `champagne-agrapart.fr` はいずれも**接続不能**、`agrapart.fr` は **OVH の «Site en construction» プレースホルダ**（無関係）。
⚠️ **ただし「ラベル上の表記が何か」は本調査では確認できていない** ❓ — 公式サイトはボトル画像を 1 枚も掲載していない。
**«Agrapart & Fils» が実在の label 表記である可能性を、この証拠は否定しない。否定しているのは「公式サイトがそう名乗っている」という前提だけである。**

### ④ OBP への影響

- OBP 2 本（`'Minéral,' Grand Cru` 2015 $520 ／ `'Experience,' Grand Cru Brut Nature` 2015 $960）は
  **`pascal-agrapart` 側に `alias` で解決済み。現時点で誤りは出ていない。**
- 🔴 **ただし「同じワインの別年」が別系列として扱われている。**
  Minéral は 2015（pascal）と 2018（and-fils）、Expérience は 2015（pascal）と 2019（and-fils）。
  **Packet C（ヴィンテージ追加）で必ず衝突する。**
- 🔴 **さらに、OBP に載っていない 5 キュヴェ（7 Crus / Terroirs / Complantée / Avizoise / Vénus）は
  `agrapart-and-fils` 側にしか存在しない。** 将来 OBP にこれらが載った場合、**印字が «Agrapart» で始まれば
  どちらの実体に付くかは matcher の到達順に依存する** — **P-1 Domaine Leroy / Maison Leroy と同じ壊れ方をする。**

### ⑤ 推奨される解決策（**実行しない**）

- **統合するのが妥当な蓋然性は極めて高い**（新 Evidence 1）。**ただし実行しない。**
- **どちらを canonical 名にするかは architecture の判断。** 判断材料は非対称である —
  **公式サイトの自称と法人名は «Pascal Agrapart» を支持**するが、
  **キュヴェの網羅性（7 件）とラインナップの完全性は `agrapart-and-fils` 側にある。**
  **どちらを残しても、もう一方のキュヴェとヴィンテージを漏らさず引き継ぐ必要がある。**
- ⚠️ **ラベル表記の確認が先。** 実ボトル（表・裏ラベル）または CIVC 登録番号での確認が取れるまで、
  **«Agrapart & Fils» を「誤った表記」として扱わないこと。** alias として保持するのが安全側。
- 🔴 **P-1 と同じく、`decisions` に機械可読な制約（統合可 / keep_separate）を置ける仕組みが無い限り、
  統合しても matcher 側の再発を防げない。** 本件は **S-2（裁定スキーマの不統一）と同じ根**を持つ。

### ⑥ Confidence

**High** — 同一生産者であることについて。根拠は
**(a) キュヴェ名 2 件の完全一致、(b) ヴィンテージの分散、(c) 🔴 公式ラインナップ 7 件と 2 実体の和集合の完全一致。**
**canonical 名の選択（どちらを残すか）については Confidence 判定の対象外 — これは research ではなく architecture の決定である。**

⚠️ **誤検出ではないことの確認**: 本件は「色違い」「別アペラシオン」「上位／下位」「別シャトー」のいずれにも該当しない。
**同一村・同一業態・同一キュヴェ名・同一ラインナップである。**

---

## Sources

### 一次資料（公式サイト・2026-08-04 参照）✅

**`https://www.champagnepascalagrapart.com/`（FR 原文＝`Default.aspx`）**
**`https://www.champagnepascalagrapart.com/default-en.aspx`（EN 訳）**
**`https://www.champagnepascalagrapart.com/mention.aspx`（法的表示・取扱店リスト・連絡先）**

**サイト構造: 1 ページ完結。モーダル 4 つ（`#liens`＝Où déguster ／ `#contact` ／ `#mentions` ／ 各キュヴェ）。**
**Wayback CDX（全 134 行）で `text/html` は上記 3 本のみ。`robots.txt` は 404。sitemap 無し。**
**旧サイトの下位ページ（`/en/AVIZOISE-44.aspx` `/en/Complantee-42.aspx` `/en/Venus-45.aspx` `/en/winery-31.aspx`）は
現在 404、かつ Wayback に 200 の捕獲が 1 件も存在しない。**

| 公式セクション | 得た主な事実 |
|---|---|
| **トップ（イントロ）** | **Propriétaire Récoltant–Manipulant / «pas d'achat de raisins» / 12 ha / 主にグラン・クリュ / chardonnay / 自社収穫・自社圧搾 / «approche naturelle» / labour / 毎年の地元堆肥 / 無清澄・無濾過 / ドメーヌ瓶詰め / 手作業ルミュアージュ** |
| **7 Crus** | Extra Brut / «notre premier vin» / 2 ミレジム / 7 村 / **GC 4（Avize, Cramant, Oiry, Oger）+ «2 Premiers Crus» と書いて 3 村列挙（AVENAY VAL D'OR, VAL DES MARAIS, VAUCIENNES）** / **90% chardonnay + 10% pinot noir** / **≤5 g/L** / bouteille のみ |
| **Terroirs** | Extra Brut / BdB Grand Cru / 4 GC の選抜区画・全て chardonnay / 2 ミレジム / ≤5 g/L / **bouteille・magnum・jéroboam** |
| **Complantée** | Extra Brut / **Grand Cru（BdB 表記なし）** / **6 品種混植（chardonnay, pinot noir, pinot meunier + arbane, petit meslier, pinot blanc）** / AVIZE / 2 ミレジム / ≤5 g/L / bouteille のみ |
| **Minéral** | Extra Brut / BdB GC / **Toujours millésimée** / **Champ bouton（AVIZE）+ Bionnes（CRAMANT）**、**同一の地質プロファイル**、**«sol mince tout de suite sur la craie»** / **«Précise, sapide et saline»**、«dimension crayeuse» / **≤3 g/L** / bouteille・magnum |
| **Avizoise** | Extra Brut / BdB GC / **Toujours millésimée** / **Robarts + Gros Yeux（AVIZE）**、**«argiles plus profondes avant la craie»** / **«densité et richesse, gastronome et élégante»** / **liège et agrafes** / ≤3 g/L / bouteille・magnum |
| **Vénus** | **Brut Nature** / BdB GC / Toujours millésimée / **Fosse aux pourceaux（AVIZE）60 ares** / **重機なし・人と馬のみ** / «l'emblème parcellaire du domaine» / liège et agrafes / **sans dosage** / bouteille・magnum |
| **Expérience** | **Brut Nature** / BdB GC / **«Millésimé» の記載なし** / **vieilles vignes d'Avize** / **«sans aucun intrant exogène»** / «Défi ultime du champagne nature» / liège et agrafes / **sans dosage** / **bouteille のみ** |
| **Où déguster**（`#liens`） | **地元（シャンパーニュ地方）の restaurants / hôtels-restaurants / cavistes のリストのみ。** L'Assiette Champenoise・Les Crayères・Royal Champagne・Les Avisés（Avize）等。🔴 **輸出先・インポーターの情報は公式に一切無い。** |
| **Contact**（`#contact`） | 🔴 **«Pas de vente ni visite au domaine»** / **«Pascal et Ambroise Agrapart»** / 57 Avenue Jean Jaurès 51190 AVIZE / Tel |
| **Mentions légales** | **SCEV Champagne Pascal Agrapart** / capital 1 000,00 € / **RCS Reims 531 932 820** / ADEME **FR246127_01QEKR** / ⚠️ **SIRET 78038582900012（«Ressortissant du Comité Champagne» の文脈）** / 制作 CELUGA（Paris） |
| **`plan.jpg`（公式手描き区画図）** | 🔴 **AVIZE / CRAMANT / OIRY の位置関係、Bois de Saran・Bois d'Avize、5 つの lieu-dit（LES BIONNES / LE CHAMP BOUTON / LA FOSSE AUX POURCEAUX / LES GROS YEUX / LES ROBARTS）、ドメーヌ位置。本文の畑名を図で裏づける。** |
| `Fresque-1b.png` `Fresque-2b.png` | 馬鍬（labour）の線画挿絵。**文字情報なし。事実の根拠には使っていない。** |

### 公式記述の経年変化（Wayback 捕獲 16 本・**公式ドメインの過去版のみ**）⚠️

`wayback-2022-07-03.html` ／ `wb-2022-12` `wb-2023-06` `wb-2023-09` `wb-2024-04` `wb-2025-01` `wb-2025-02`
`wb-2025-05` `wb-2025-08` `wb-2025-11` `wb-2026-02` `wb-2026-05`（ほか捕獲失敗 4 本）
→ **§History の変化表の根拠。10ha→12ha / Brut→Extra Brut / 7→5 g/L / COLIGNY→VAL DES MARAIS / «à la main» の削除。**
🔴 **これは第三者の記述ではなく、公式サイト自身の過去版である。**

### 現行性の確認 ✅

**2026-08-04 に FR / EN を実取得し、既存の `home.html` `home-en.html` と本文テキストの完全一致を確認済み**
（差分は ASP.NET の ViewState トークンのみ）。**本書の「現在」は 2026-08-04 時点の公式記述を指す。**

### 二次資料

**なし。本書の事実は全面的に公式サイトのみに基づく。**
小売店・EC・インポーター・レビュー集約サイト（wine-searcher / vivino 等）・Wikipedia の記述は**一切使用していない**
（検索は公式ドメインの特定と、別ドメイン公式サイトの不存在確認にのみ使用）。

### THÉSEUS 内部データ 🔍

`batch2.json`（canonical レコード概要 / canonical キュヴェ 2 件 / OBP intake 2 本）
`/Users/akiomatsumoto/Theseus_Phase0/research/canonical_conflicts/REGISTER.md`（**P-3**。読み取りのみ）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **High** | 法人名・住所・電話・登記番号・業態・見学方針まで公式。⚠️ SIRET と RCS の不整合、❓ ラベル表記 |
| Overview | **High** | 業態・面積・品種・栽培姿勢・醸造 3 原則すべて公式の一次記述 |
| History | 🔴 **Low** | **公式に沿革が一行も無い。**代替として得たのは「公式記述がいつ変わったか」だけ（これは High だが沿革ではない） |
| Location | **Medium-High** | 村・格付け・**5 つの lieu-dit（本文＋公式区画図の二重確認）**・地質の対比は High。⚠️ 面積が 10→12 で振れる、❓ 内訳・樹齢・密度・台木が全て非公開、⚠️ «2 Premiers Crus» で 3 村 |
| Farming | **Medium-High** | **方針（labour / 毎年の地元堆肥 / Vénus の馬）は公式で明確。**🔴 **認証・農薬・除草剤は公式に完全な沈黙** — 「書かれていない」ことを確定させた点で使える |
| Winemaking | **Medium** | **無清澄・無濾過／ドメーヌ瓶詰め／手作業ルミュアージュ／販売 2 ヶ月前デゴルジュマン／打栓方式／ドザージュ 3 段階**は公式。🔴 **発酵容器・樽・MLF・酵母・熟成期間・生産量は全面非開示** |
| Style | **Medium-Low** | **公式の味わい語は Minéral（«précise, sapide, saline»）と Avizoise（«densité et richesse…»）の 2 キュヴェ分のみ。**残りは見出しの一言。第三者評価・点数はゼロ |
| Important Cuvées | **High** | **公式 7 キュヴェの仕様（品種・区画・ドザージュ・容量・ミレジメの別）が全て取れている。OBP 2 本とも公式と印字が一致し、セクション配置も正しい。**THÉSEUS の中では例外的にクリーン |
| Canonical Conflict | **High** | REGISTER.md P-3 に加え、**ラインナップ和集合の完全一致**という新証拠を得た |
| Staff Notes | **High** | すべて上記 ✅ から構成。**⚠️ 禁止リストがこの生産者では本体** |
| **総合** | **Medium-High — staff-usable。70% 到達。** | **客が必ず訊く層（畑・栽培・キュヴェの中身）は公式で厚く取れており、OBP 2 本はキュヴェとして完全に一致する。**減点は **History の完全な不在**と **Winemaking 数値の全面非開示**。ただし**その 2 つを ⚠️ 禁止リストで明示的に封じたため、現場で間違ったことを言わずに語れる状態**は満たしている |

---

## Open Questions

1. 🔴 **canonical の重複統合が必要（最優先）。** `producer:agrapart-and-fils`（7 キュヴェ・OBP 0）と
   `producer:pascal-agrapart`（2 キュヴェ・OBP 2）は**同一生産者である蓋然性が極めて高い**
   — **公式ラインナップ 7 件と 2 実体の和集合が完全一致する**（新 Evidence）。
   **REGISTER.md `P-3` への追記が必要。統合の実行と canonical 名の選択は architecture の判断であり、research では動かさない。**
2. 🔴 **ラベル上の正式表記。** 公式サイトは «Champagne Pascal Agrapart» のみを名乗り、**«Fils» の語が全文にゼロ**。
   だが**公式サイトにボトル画像が 1 枚も無く、ラベル表記は確認できていない。**
   **実ボトルの表／裏ラベル、または CIVC 登録番号での確認が要る。**これが取れるまで «Agrapart & Fils» を誤記扱いしない。
3. 🔴 **沿革が公式に完全に欠落している。** 創業年・世代・相続・「& Fils」の由来 — 一行も無い。
   **旧サイトの `/en/winery-31.aspx` は 404 で、Wayback にも 200 の捕獲が無い。**
   **生産者提供の資料が来ない限り、History は埋まらない。**
4. 🔴 **Pascal と Ambroise の続柄・役割・現況。** 公式は連名 «Pascal et Ambroise Agrapart» のみ。
   **当主・醸造責任者が誰かは公式で確認できない。現在性未確認。**
5. **10 ha → 12 ha（2025 年 2–5 月の間に公式が変更）の内訳。** 買増か、賃借か、記載の是正か — 公式に説明なし。
   **どの村・どの区画が増えたかも不明。**
6. 🔴 **OBP の 2 本（2015 VT）の実スペック。** 公式の ≤3 g/L / sans dosage / 12 ha は**すべて 2025 年以降の記述**。
   **2015 年産の実ドザージュとデゴルジュマン時期は公式サイトから確定できない。**
   （公式は «販売の 2 ヶ月前» としか言わないため、**逆に「デゴルジュマン年 ≒ 販売年」という読みは公式に根拠がある**が、
   2015 VT がいつ販売されたかは不明。）
7. **`7 Crus` の «2 Premiers Crus» と 3 村の不整合。** FR / EN 同一。訳の誤りではない。**公式の記載側の問題。**
8. **`Expérience` はミレジメか。** 公式は Minéral / Avizoise / Vénus にだけ «Toujours millésimée» を付け、
   **Expérience には付けていない。**にもかかわらず canonical・OBP ともヴィンテージ（2015 / 2019）を持つ。
9. **COLIGNY → VAL DES MARAIS の書き換えの意味。** 自治体名の変更か、調達先の変更か。公式に説明なし。
10. **醸造の非開示項目一式。** 圧搾方式 / 発酵容器（樽の有無） / 新樽比率 / MLF / 酵母 / 澱接触・瓶熟期間 /
    リキュール組成 / SO2 / 年間生産量 / 収量。**生産者提供資料でしか埋まらない。**
11. **認証の有無そのもの。** 公式に記載なし。**「持っていない」も公式には言えない。**
12. **`mention.aspx` の SIRET 78038582900012 と RCS Reims 531 932 820 の関係。**
    SIREN が一致せず、前者は «Ressortissant du Comité Champagne» の文脈に置かれている。**どちらが SCEV 自身の番号か公式から判定不能。**
13. **OBP 価格の通貨単位。** 520 / 960 の通貨が intake に記録されていない（他生産者と共通の課題）。
