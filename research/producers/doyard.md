# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:doyard` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagnedoyard.fr（HTML ＋ 公式 fiche technique PDF）で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書で事実の根拠に使ったのはゼロ。1 箇所だけ Comité Champagne ディレクトリを明示注記つきで参照**）
> `⚠️` **公式内で食い違い。どちらも消さず両方残す** ／ `🔍` THÉSEUS DB・OBP intake・公式値からの機械的導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 一次資料: **`https://champagnedoyard.fr/`**（FR 原文。一部 EN ページあり）
> 参照した公式ページ **全 22 件**（サイトの全ページ。`wp-json/wp/v2/pages` で網羅を確認済み）:
> `/`（La Maison）・`/the-house-2/`（EN）・`/vignoble/`・`/vineyard/`（EN）・`/gamme/`・`/gamme-mobile/`・
> `/gamme/cuvee-vendemiaire/`・`/gamme/revolution/`・`/gamme/clos-de-labbaye/`・`/gamme/blanc-de-blancs/`・
> `/gamme/oeil-de-perdrix/`・`/gamme/les-lumieres/`・`/gamme/la-libertine/`・`/gamme/vieux-fombres/`・`/gamme/la-ratafia/`・
> `/cuvee-eng/`（旧 EN 版 Vendémiaire）・`/contact/`・`/actualites/`・`/news/`・`/galerie/`・`/mentions-legales-2/`・`/charte-de-confidentialite/`
> 公式 fiche technique PDF **8 件を取得済み** → `_sources/doyard/pdf/`
>
> 🔴 **本書の 4 つの前提。読まずに下へ行かないこと。**
> 1. 🔴 **タスク指示にあった `https://doyard.com/` は Champagne Doyard のサイトではない。** 200 は返すが中身は
>    `window.location.href="/lander"` だけのパーキング（ドメイン売り出し）ページである。**本書は一切使っていない。**
>    **本物の公式ドメインは `champagnedoyard.fr`**（`mentions légales` に自社サイトとして明記、`contact@champagnedoyard.fr`、全 fiche PDF のフッターに `www.champagnedoyard.fr`）。
> 2. ⚠️ **公式サイトは事実上 2021 年で更新が止まっている。** キュヴェ 9 ページの最終更新は全て **2021-06**、`/vignoble/` は **2018-02**、
>    `/the-house-2/` `/vineyard/` `/cuvee-eng/` は **2017-08**。fiche PDF も全 8 件が **2021/06 アップロード**。
>    `/actualites/` `/news/` `/galerie/` は Facebook / Instagram の埋め込みショートコードのみで**本文ゼロ**。
>    **したがって公式記述はすべて「2021 年時点」であり、「現在」として語れない。** 当主・醸造責任者の現況は確認できない（→ §History）。
> 3. ✅ **キュヴェ別 fiche technique PDF は存在し、全部取れた。** 各 `/gamme/*` ページ末尾の「Fiche technique」リンク（FR/EN 併記 1 枚もの）。
>    **HTML ページより PDF の方が情報が多い**（ベース年比率・瓶詰め年・実生産本数・熟成ポテンシャル）。**ただし OBP 掲載 3 本のうち PDF が存在するのは 1 本だけ。**
> 4. 🔴 **OBP 3 本のうち、公式で完全に裏が取れるのは Vendémiaire の 1 本だけ。** `Grand Cru Extra Brut 2015` は**公式に 2015 の fiche が無く**、
>    `'Voie d'Oger'` に至っては**公式サイトに一語も存在しない**。**§Important Cuvées と §Staff Notes を必ず読むこと。**

---

## Identity

| | |
|---|---|
| **Canonical Name** | Doyard（canonical `producer:doyard` / `aliases: []` / `confidence: 0.2` / `source: legacy_app`） |
| **公式のブランド表記** | **Champagne Doyard** ✅（全 fiche PDF の署名が «CHAMPAGNE DOYARD»、住所ブロックが «Champagne DOYARD»） |
| **サイト上の名乗り** | ⚠️ **«Domaine Doyard»**（`<title>` およびページタイトル）／ **«LE DOMAINE DOYARD»**（トップ本文）／ **«THE DOYARD HOUSE»**（EN 版）。**ラベル表記は «Champagne Doyard»、サイト表記は «Domaine Doyard»。両方公式。** |
| **Aliases（実務上）** | 🔍 「Champagne Doyard」「Domaine Doyard」「Doyard」。**canonical の `aliases` は空** → 昇格時に要追加 |
| **業態** | ✅ **Récoltant-Manipulant（RM）**。公式の言い回しは «Récoltant-Manipulant depuis quatre générations et Vigneron depuis douze générations»。**RM の matricule 番号は公式非掲載** ❓ |
| **法人** | ✅ **DOYARD, société civile** / 資本金 **155,310.00 €** / **RCS Châlons-en-Champagne n° 324 128 313**（`charte-de-confidentialité` に自己申告） |
| **住所** | ⚠️ **39, avenue du Général Leclerc, 51130 Vertus** ✅（`/contact/`・全 fiche PDF）／ **39 AV du Général Leclerc, 51130 Blancs-Coteaux** ✅（`charte-de-confidentialité`）。**同一地番。Vertus は 2019 年に新設コミューン Blancs-Coteaux に統合されたため、法定表記が Blancs-Coteaux、慣用・ラベル表記が Vertus。両方が公式に併存している。** |
| **連絡先** | ✅ Tél +33 3 26 52 14 74 / Fax +33 3 26 52 24 02 / contact@champagnedoyard.fr |
| **公式サイト** | ✅ **https://champagnedoyard.fr**（🔴 `doyard.com` はパーキングページ。公式ではない） |
| **所属** | ✅ **«Les Artisans du Champagne»（2010 年〜、16 の artisans-vignerons の団体）** |
| **関連事業** | ✅ **シャンブル・ドット «Clos Margot»**（`www.closmargot.fr`。`/contact/` からリンク） |

---

## Overview

コート・デ・ブラン南端、**ヴェルテュ（Vertus, 1er Cru）**に本拠を置く**レコルタン・マニピュラン**。✅
自社畑 **11 ヘクタール**、**54 の lieu-dit に分散**（1 区画平均 **0.20 ha**）。**シャルドネ 10 ha／ピノ・ノワール 1 ha** という構成で、
シャルドネは **1er Cru ヴェルテュ ＋ グラン・クリュ 4 村（ル・メニル・シュル・オジェ／オジェ／アヴィズ／クラマン）**、
ピノ・ノワールは **1er Cru ヴェルテュ ＋ グラン・クリュ アイ（Aÿ）** に置く。✅

醸造の骨格は全キュヴェで一貫している — **ブルゴーニュ産のピエス（228L 級）を「5 vins 以上を経た樽」だけで使う（＝新樽ゼロ）**、
**補糖（chaptalisation）を一切しない**、**マロラクティック発酵は原則ブロック**、**ドザージュは 0〜4 g/L**。✅
アッサンブラージュ系 2 本（Vendémiaire / Révolution）だけが例外的に **MLF を 20% だけ通し**、**キュヴェ（一番搾り）のみ**を使う。✅

栽培は 🔴 **公式には «viticulture raisonnée»（減農薬・合理的防除）**と書かれている。**オーガニックでもビオディナミでもない。** ✅
「化学的資材を一切入れない」と公式が書いているのは、**Clos de l'Abbaye という 0.5 ha の単一区画についてだけ**である。✅

---

## History

🔴 **この生産者は、公式サイトに沿革が一行も無い。** 年号・創業年・人名・世代交代の記述はゼロ。
**公式が語る「歴史」は次の一文に集約される 2 つの数字だけである。**

| | 公式の記述 | レイヤー |
|---|---|---|
| **レコルタン・マニピュランとして** | **4 世代** «Récoltant-Manipulant depuis quatre générations» | ✅ |
| **ヴィニュロン（葡萄栽培者）として** | **12 世代** «Vigneron depuis douze générations» | ✅ |

⚠️ **この 2 つの数字にも日付が無い。** 初出ページ `/the-house-2/` は **2017 年 8 月**、トップページは **2018 年 2 月**が最終更新である。
**「今何世代目か」は公式から言えない。**

### 公式から取れる確定年号（3 つだけ）✅

| 年 | 事実 | 出典 |
|---|---|---|
| **1956** | **Clos de l'Abbaye の 0.5 ha 区画を植樹** | `/gamme/clos-de-labbaye/` ＋ Clos fiche PDF |
| **2010** | **«Les Artisans du Champagne»（16 の artisans-vignerons）に加盟** | `/the-house-2/` |
| **2019** | 🔍 Vertus が新設コミューン **Blancs-Coteaux** に統合（公式は住所表記の差としてのみ現れる） | `charte-de-confidentialité` |

### 🔴 当主・技術陣 — **現況は確認できない** ❓

**公式サイトに個人名は一つも書かれていない。** 唯一の手掛かりは `mentions légales` の 2 行で、そこにも姓しか無い:

- **責任者（responsable publication）: «M. Doyard» — `charlesdoyard@gmail.com`** ✅
- **ウェブマスター: «M. Doyard» — `g.doyard@gmail.com`** ✅

🔍 **メールアドレスから読めるのは「Charles」と「G.」という 2 人の Doyard が運営に関わっている**ということだけであり、
**どちらが当主か、役割は何か、就任時期はいつかは公式に一切書かれていない。**
⚠️ **canonical の legacy テキストは「現在はギヨーム・ドワイヤールが管理」「1927 年にモーリス・ドワイヤールが初めてドワイヤールの名で生産」「1677 年から」と書いているが、**
**これらは公式サイトに一切根拠が無い。**（→ §Important Cuvées の canonical 突合表、§Staff Notes の ⚠️ リスト、Open Questions #4）

### 受賞 ❓

📄 **Comité Champagne（champagne.fr）の生産者ディレクトリに «Prix du Jury Jeune Talent du Champagne» 受賞と記載がある。**
**これは生産者一次資料ではなく、また受賞年も書かれていない。** 生産者自身の公式サイトには受賞の記述が皆無。→ **現場で言わない。** Open Questions #5。

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Champagne ✅ |
| **Village（本拠）** | **Vertus**（Côte des Blancs, **Premier Cru**）✅ |
| **総面積** | ⚠️ **11 ヘクタール** ✅（`/vignoble/` 2018-02）／ **«plus de dix hectares»＝10 ha 超** ✅（トップ・`/the-house-2/` 2017-08）。**採用: 11 ha**（新しい方かつ具体的） |
| **品種構成** | ✅ **シャルドネ 10 ha ／ ピノ・ノワール 1 ha**（⚠️ EN 版 `/vineyard/` は «Le Pinot Noir ( hectare)» と数字が脱落。FR を採用） |
| **区画数** | ✅ **54 lieux-dits、平均 0.20 ha/区画**（«Morcellement : 54 lieux-dits, soit une moyenne parcellaire de 0.20 ha»） |
| **平均樹齢** | ⚠️ **40 年** ✅（FR `/vignoble/` 2018-02）／ **39 年** ✅（EN `/vineyard/` 2017-08）。**同一記述の更新差。採用: 40 年。ただし «2018 年時点の 40 年»** |

### 村ごとの格付け ✅

| 品種 | 村 | 格付け |
|---|---|---|
| **Chardonnay（10 ha）** | **Vertus** | **Premier Cru** |
| | **Le Mesnil-sur-Oger / Oger / Avize / Cramant** | **Grand Cru（4 村）** |
| **Pinot Noir（1 ha）** | **Vertus** | **Premier Cru** |
| | **Aÿ** | **Grand Cru** |

🔍 **この 6 村の構成が、キュヴェの格付け表記を全部決めている** — Grand Cru を名乗れるのは Mesnil / Oger / Avize / Cramant / Aÿ 由来のもの、
ヴェルテュ由来のものは 1er Cru。**Clos de l'Abbaye が «Premier Cru» なのはヴェルテュだから**（→ §Important Cuvées。ここが OBP 照合の要）。

### 名前のある畑 ✅

- **Clos de l'Abbaye** — **ヴェルテュ**。**0.5 ha の完全に独立した単一区画（clos）**、**1956 年植樹**、**シャルドネ 100%**。
  «Sa situation et son sol très calcaire lui confèrent une très grande précocité»＝**強い石灰質土壌ゆえ非常に早熟**。
  **収量目標 35〜40 hl/ha**、**土壌は馬で耕す（travaillés au cheval）**、**化学的資材を一切入れない**。
  ⚠️ EN 訳は «its chalky soil give to the grape an atypical taste»（＝特異な味わい）と書いており、FR の «précocité»（早熟）と内容が違う。**FR を採用。**
- **En Vieux Fombrés** — **ヴェルテュの中腹（mi-coteau）の lieu-dit**。ここだけ Coteaux Champenois（スティル白）を造る。✅

---

## Farming

🔴 **ここが Doyard で最も間違えやすい節である。公式の表現を一語も変えずに読むこと。**

### 公式の宣言（`/vignoble/` ✅）

> **«Viticulture raisonnée, le moins d'intrants possible afin de laisser s'exprimer au mieux le terroir (travail mécanique du sol notamment).»**

- ✅ **「viticulture raisonnée」＝減農薬・合理的防除。** 公式はこの語しか使っていない。
- 🔴 **«bio» «biologique» «biodynamie» «organique» という語は、サイト全 22 ページ・PDF 8 件のどこにも一度も出てこない。**（全文検索で確認）
- 🔴 **認証名（AB / Ecocert / Demeter / Biodyvin / HVE / Viticulture Durable en Champagne）への言及もゼロ。** ❓

### 具体策 ✅

| 項目 | 公式の記述 |
|---|---|
| **除草** | **«travail mécanique du sol»＝機械的な土壌耕耘**（除草剤の可否は明言なし ❓） |
| **投入資材** | **«le moins d'intrants possible»＝可能な限り少なく**（ゼロとは書いていない） |
| **植え替え方針** | 🔴 **«Aucune nouvelle plantation, remplacement uniquement des pieds morts de façon annuelle»＝新規植樹はせず、枯死株のみ毎年補植。** 目的は明記されていて **«dans le but d'augmenter l'âge moyen du vignoble»＝平均樹齢を上げるため** |
| **剪定** | **«Taille cordon de Royat monté permanent»** |
| **狙い** | **«faire plonger les racines en profondeur»＝根を深く潜らせる ＋ «en maîtrisant fortement les rendements»＝収量を強く抑える** |

### 例外区画: Clos de l'Abbaye ✅

**この 0.5 ha についてだけ、公式はより強い言葉を使う。**

- **«Le mode de conduite très respectueux de l'environnement exclut tout apport de produit chimique»＝化学的資材の投入を一切排除**
- **«Les sols sont notamment travaillés au cheval»＝土壌は馬で耕す**
- **«vise un faible rendement (35 à 40 Hl/Hectare)»**
- fiche PDF（Millésime 2015）も見出しで **«Sans apport de produit chimique / Without chemical product»** と再掲 ✅

🔴 **「馬で耕す」「化学的資材ゼロ」は Clos de l'Abbaye の記述である。ドメーヌ全体の話として広げてはならない。**
（canonical の legacy テキストは «horse-drawn cultivation in most parcels» と全体に広げているが、**公式に根拠が無い**）

---

## Winemaking

### 全キュヴェを貫く 4 原則 ✅

| 原則 | 公式の記述 | 例外 |
|---|---|---|
| **1. 新樽を使わない** | **«pièces bourguignonnes de 5 vins minimums»＝最低 5 回ワインを仕込んだブルゴーニュのピエス** | ⚠️ **Blanc de Blancs の fiche（2009 / 2012）だけ «4 vins minimums»**。ページ側は «5 vins minimums»。**両方公式。両方残す** |
| **2. 補糖しない** | **«Pas de chaptalisation (degré alcoolique naturel)»** — 全キュヴェ・全 fiche に明記 | なし |
| **3. MLF は原則ブロック** | **«Fermentation malolactique non effectuée»** — Clos / Blanc de Blancs / Œil de Perdrix / Les Lumières | **Vendémiaire・Révolution のみ «effectuée à 20 %»＝20% だけ実施** |
| **4. 低ドザージュ** | **0 〜 4 g/L** | **La Libertine のみ 65 g/L（意図的な例外）** |

### 圧搾の使い分け ✅（Doyard の核心の一つ）

| 使う果汁 | キュヴェ |
|---|---|
| **キュヴェ（一番搾り）のみ «Moût de cuvée uniquement»** | **Vendémiaire・Révolution** |
| **1ère presse のみ** | **Clos de l'Abbaye・Les Lumières**、Œil de Perdrix のシャルドネ |
| **1ère ＋ 2ème presse** | **Blanc de Blancs**、Œil de Perdrix のピノ・ノワール |

### 樽比率 ✅

| キュヴェ | 木樽 | ステンレス |
|---|---|---|
| **Vendémiaire** | **40%** | **60%** |
| **Révolution** | **50%** | **50%** |
| **Clos de l'Abbaye / Blanc de Blancs / Les Lumières / En Vieux Fombrés** | **100%** | — |
| **Œil de Perdrix** | ピノ・ノワールのみ樽 | シャルドネはステンレス |

### 熟成・サービス ✅

- **全 fiche が «Servir entre 12 et 13 °»＝提供温度 12〜13 ℃を指定。**
  🔴 **canonical は «serving_temp: 8–10°C» と登録している。公式と食い違う。**（→ Open Questions #4）
- **熟成ポテンシャル: «Potentiel de garde de 5 ans minimum après dégorgement»＝デゴルジュマン後 5 年以上**（Clos / Blanc de Blancs / Œil de Perdrix）。
  **Les Lumières のみ «8 ans minimum»。**
- **Les Lumières は «temps sur latte» 約 10 年以上**と明記 ✅。

### ❓ 公式が語っていないこと（＝現場で言えないこと）

**酵母（自生か培養か）／ SO2 の使用量・タイミング／濾過・清澄の有無／デゴルジュマンの時期／
Vendémiaire 以外の瓶内熟成期間／リザーヴワインのソレラの有無／樽の産地・トヌリエ名 — すべて非開示。**
（唯一の熟成期間の言及は旧 EN ページ `/cuvee-eng/` の Vendémiaire «Quatre années de gestation»＝**4 年**。⚠️ **ただしこれは 2007-2008-2009 ベースの古いリリースの記述である。**）

---

## Style

🔴 **公式サイトは味わいをほとんど語らない。テイスティングノートは 1 キュヴェ分しか存在しない。**

- ✅ **Œil de Perdrix のみ**: «un champagne authentique, alliant **fraîcheur, élégance, vinosité, longueur**, avec un **nez complexe, aimablement empreint d'arômes de fruits rouges**»
- ✅ **La Libertine のみ**（性格の説明）: 18 世紀初頭の発泡ワインの味わいを再現。**«n'a pas d'équivalent et ne se rapproche d'aucun Champagne actuel»**。**気圧が通常より低い約 4 bar**。
- ✅ **Les Lumières のみ**（狙い）: **«obtenir de grandes émotions gustatives après un temps sur latte plus long»**

### 🔍 したがってハウススタイルは「造りからの導出」として語るしかない

**新樽ゼロの古樽発酵（酸化的な樽香が乗らない）＋ 補糖なし ＋ MLF ブロック（リンゴ酸を残す）＋ ドザージュ 0〜4 g/L**
— この 4 つが同時に成立している造りは、**樽の風味ではなく樽の質感だけを取り、酸を落とさず、糖で丸めない**という一点に向かっている。
**アッサンブラージュ系 2 本（Vendémiaire / Révolution）だけ MLF を 20% 通す**のは、**3 年ブレンドで飲み口を整えるための微調整**と読める。🔍

⚠️ **これは THÉSEUS による構造からの導出であって、生産者の自己申告ではない。「Doyard 曰く」と言ってはならない。**

---

## Important Cuvées

### A. 公式サイトに存在する全キュヴェ（9 本）✅

**各行の数値はすべて公式ページ ＋ 公式 fiche technique PDF から。⚠️ は公式内の食い違い。**

| # | キュヴェ | 格付け | 構成 | 樽 | MLF | 圧搾 | ドザージュ | 生産量 | fiche PDF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Vendémiaire** | **Blanc de Blancs 1er Cru Brut** | CH 100%・**3 年のアッサンブラージュ** | 40% 樽 / 60% inox | **20%** | cuvée のみ | **4 g/L** ⚠️ | **約 30,000 本 ＋ 1,500 マグナム/年** | ✅ **2015(50%)/2014(30%)/2013(20%)、2016 年瓶詰め、«principalement Vertus»** |
| 2 | **Révolution** | **Blanc de Blancs Grand Cru・Non dosé** | CH 100%・**3 年のアッサンブラージュ** | 50% 樽 / 50% inox | **20%** | cuvée のみ | **0 g/L** | 約 3,000 本 ＋ 500 マグナム | ✅ **2014(50%)/2013(30%)/2012(20%)、2015 年 6 月瓶詰め** ⚠️ ページは «Mise en bouteille en 2012» |
| 3 | **Clos de l'Abbaye** | **Extra-Brut・Premier Cru・Millésimé** | CH 100%・**ヴェルテュの 0.5 ha 単一クロ（1956 植樹）** | **100%** | なし | **1ère presse のみ** | **2 g/L** | ⚠️ 約 1,500 本 ＋ 150 マグナム（ページ）／ **1,915 本**（2015 fiche） | ✅ **Millésime 2015、2016 年瓶詰め、35〜40 hl/ha、化学資材ゼロ** |
| 4 | **Blanc de Blancs** | **Grand Cru・Millésimé** | CH 100%・**Mesnil / Oger / Avize / Cramant** | **100%** ⚠️（ページ «5 vins» / fiche «4 vins»） | なし | **1ère ＋ 2ème** | ⚠️ **3 g/L**（ページ）／ **2 g/L**（2012）／ **0.6 g/L**（2009） | 約 3,500 本・**«uniquement les grands millésimes»** | ✅ **2012（2013 瓶詰め）** ＋ **2009（2010 年 5 月瓶詰め）**。🔴 **2015 の fiche は存在しない** |
| 5 | **Œil de Perdrix** | **Extra-Brut・Grand Cru・Millésimé（ロゼ・ド・プレッセ）** | **PN 75%（Aÿ）／ CH 25%（Avize）** | PN のみ樽 | なし | CH=1ère / PN=1ère+2ème | **3 g/L** | ⚠️ 約 3,000 本（ページ）／ **3,500 本**（2015 fiche） | ✅ **Millésime 2015、2016 年瓶詰め** |
| 6 | **Les Lumières** | **Grand Cru** | ⚠️ **CH 66% / PN 34%**（ページ）／ **CH 65% / PN 35%**（2008 fiche）。CH＝Mesnil ＋ Avize、PN＝Aÿ | **100%** | なし | **1ère presse のみ** | **0.8 g/L** | **年約 700 本のみ** | ✅ **Millésime 2008、2009 年 9 月瓶詰め、sur latte 約 10 年以上、デゴルジュ後 8 年以上のポテンシャル** |
| 7 | **La Libertine** | （格付け表記なし） | **4〜5 ミレジムのアッサンブラージュ** | ❓ | ❓ | ❓ | **65 g/L** | ❓ | ✅ **セラー熟成 12 年超、気圧 約 4 bar、リキュールは 20 年超の古酒（マグナム／ジェロボアム保存）** |
| 8 | **En Vieux Fombrés** | **Coteaux Champenois blanc**（発泡ではない） | ヴェルテュ mi-coteau の lieu-dit・**単一区画** | **100% pièces bourguignonnes** | ❓ | ❓ | — | ❓ | ⚠️ **ページの「Fiche technique」リンクが Ratafia の PDF を指している（公式サイト側のリンクミス）。En Vieux Fombrés 専用の fiche は公開されていない** |
| 9 | **Ratafia Champenois** | （リキュール） | ✅ **fiche は «100% Pinot Noir»**。ページは «moût ＋ fine de Champagne» とだけ | **18 ヶ月 樽熟成** | — | — | — | ❓ | ✅ **提供 10〜12 ℃** |

---

### B. 🔴 OBP 掲載分（3 本）— 印字そのまま ／ canonical 突合 🔍

**全 3 本が `FRANCE | SPARKLING > CHAMPAGNE | BLANC DE BLANCS` セクション。価格は OBP 印字値（通貨単位は intake に記録なし ❓）。**

| # | OBP 印字 | VT | 価格 | intake state | canonical 登録 | 公式との照合 |
|---|---|---|---|---|---|---|
| 1 | `'Cuveé Vendémiaire,' Premier Cru Brut` | NV | **200** | `alias` | ✅ **登録済** `cuvee:doyard-cuvee-vendemiaire-blanc-de-blancs-premier-cru`（VT: NV） | ✅ **公式 «Vendémiaire — Blanc de Blancs 1er cru» と一致。3 本で唯一クリーン。** ⚠️ 印字の «Cuveé» は **«Cuvée» の綴り誤り**（メニュー側） |
| 2 | `Grand Cru Extra Brut` | **2015** | **455** | 🔴 `unresolved` | ✅ **登録済** `cuvee:doyard-blanc-de-blancs-grand-cru-extra-brut`（VT: **2015** 保有） | ⚠️ **canonical には既にある。印字が «Blanc de Blancs» を落としているため intake が解決できていないだけ。**ただし 🔴 **公式には 2015 の fiche が存在しない**（公開は 2009 と 2012 のみ）→ 下記 B-1 |
| 3 | `'Voie d'Oger,' Grand Cru Extra Brut` | **2016** | **700** | 🔴 `unresolved` | 🔴 **canonical 未登録** | 🔴 **公式サイトに «Voie d'Oger» という語は一語も存在しない**（全 22 ページ ＋ PDF 8 件を全文検索）→ 下記 B-2 |

**🔍 canonical 側の保有キュヴェは 2 件のみ**（`Blanc de Blancs Grand Cru Extra Brut` / `Cuvée Vendémiaire Blanc de Blancs Premier Cru`）。
**公式には 9 キュヴェあるので、Révolution・Clos de l'Abbaye・Œil de Perdrix・Les Lumières・La Libertine・En Vieux Fombrés・Ratafia の 7 本が canonical 未登録。**
→ **昇格時に追加すべきキュヴェ 7 件**（本書 §A の表がそのまま原資になる）。

---

### B-1 🔴 `Grand Cru Extra Brut 2015` の正体 ⚠️

**結論: 公式の «Blanc de Blancs Grand Cru Millésimé» の 2015 年ものである蓋然性が高い。ただし公式に 2015 の裏付けは無い。**

**根拠（○＝支持 / ×＝反証）**

| 候補 | 判定 |
|---|---|
| **Blanc de Blancs Grand Cru Millésimé** | ○ **格付け（Grand Cru）・色（Blanc de Blancs 節）・ミレジム表記・低ドザージュ（2 g/L〜3 g/L ＝ Extra Brut 域）がすべて合う。** ○ **canonical にも 2015 が登録済み。** ○ 🔍 **Doyard は 2015 年産を実際に瓶詰めしている**（Clos de l'Abbaye 2015・Œil de Perdrix 2015 の fiche がどちらも «2016 年瓶詰め» で存在）。× **2015 の fiche だけが公開されていない** |
| **Révolution（Blanc de Blancs Grand Cru, 0 g/L）** | × **Révolution は NV（3 年アッサンブラージュ）でミレジムを名乗らない。** × 公式表記は «Non dosé» であって «Extra Brut» ではない。**⚠️ ただし fiche の «2015 年 6 月瓶詰め» をメニュー側が年号として拾った可能性は完全には否定できない** |
| **Clos de l'Abbaye 2015** | × 🔴 **Clos de l'Abbaye はヴェルテュ産＝ Premier Cru である。Grand Cru ではない。**（公式 fiche の見出しが «Extra-Brut, Premier Cru Millésimé 2015»）**除外。** |
| **Œil de Perdrix 2015**（Extra-Brut / Grand Cru / Millésimé 2015 で表記は完全一致） | × 🔴 **ロゼであり PN 75%。OBP の掲載節は BLANC DE BLANCS。除外。** ⚠️ **ただし「Extra-Brut, Grand Cru, Millésimée 2015」という文字列だけなら Œil de Perdrix と完全一致する。名寄せを文字列だけでやると必ず誤爆する。** |

⚠️ **したがって現場では「2015 年のグラン・クリュのブラン・ド・ブラン」として扱ってよいが、
造りの数値（ドザージュ 3 g/L・2 g/L・0.6 g/L のいずれか）を断定してはいけない。公式の 2015 fiche が無い。**

### B-2 🔴 `'Voie d'Oger,' Grand Cru Extra Brut 2016` — **公式にゼロ** ❓

- 🔴 **公式サイトの全 22 ページ、fiche technique PDF 全 8 件を全文検索して «Voie» «Voie d'Oger» のヒットはゼロ。**
- 🔴 **公式のキュヴェは 9 本で、その中に単一区画ものは Clos de l'Abbaye（ヴェルテュ・1er Cru）と En Vieux Fombrés（ヴェルテュ・スティル）の 2 つだけ。**
- ⚠️ **公式サイトのキュヴェページは 2021 年 6 月で更新が止まっている。** 🔍 **したがって「2021 年以降にリリースされた新しい区画キュヴェで、サイトが追いついていない」という説明は構造的に成り立つ。**
  **Doyard はオジェにグラン・クリュのシャルドネを持っており（✅）、区画は 54 lieu-dit・平均 0.20 ha（✅）なので、単一 lieu-dit のキュヴェを出す素地はある。**
- ❓ **しかしそれは推論であって確認ではない。** «Voie d'Oger» が
  (a) オジェ／ル・メニル側のグラン・クリュ lieu-dit 名なのか、
  (b) ヴェルテュ側の「オジェへ抜ける道」の lieu-dit 名（＝その場合 1er Cru であり «Grand Cru» 表記が誤りになる）なのか、
  **THÉSEUS は公式に確定できない。** → Open Questions #1（最優先）。

---

## Staff Notes

> **この節は上の ✅ からのみ構成している。裏の取れていない事柄は一つも書いていない。**
> 🔴 **Doyard は「造りは公式で厚く取れるが、人と歴史が公式にゼロ」というタイプ。**
> **だから話す場所は畑と造りに寄せ、歴史と当主の話には踏み込まない。**

### 一行で言うと

「**ヴェルテュのレコルタン・マニピュラン。11 ヘクタールが 54 枚の畑に割れていて、平均 1 枚 0.2 ヘクタール。
新しい樽は 1 つも使わず、補糖もせず、マロラクティックも止める。ドザージュは 0 から 4 グラム。**」

### ゲストへの説明の芯（3 点）

**1. コート・デ・ブランを、ヴェルテュから 1 級と特級の両方で持っている。**
本拠は **ヴェルテュ（Premier Cru）**。そこに加えて **シャルドネの特級 4 村 — ル・メニル・シュル・オジェ、オジェ、アヴィズ、クラマン**、
そして **ピノ・ノワールは特級のアイ**。**シャルドネ 10 ヘクタール、ピノ・ノワール 1 ヘクタール。**
畑は **54 の区画に分かれていて、1 枚あたり平均 0.2 ヘクタール**しかありません。
**新しく植えることはせず、枯れた株だけを毎年入れ替えています。畑の平均樹齢を上げるためです。**（公式表記。2018 年時点で平均 40 年）

**2. 新樽をひとつも使わない。**
使うのは **ブルゴーニュのピエス（樽）で、しかも「5 回以上ワインを仕込んだ樽」だけ**。**新樽はゼロです。**
樽の香りを付けるためではなく、**質感のためだけに木を使っている**、という設計です。
比率はキュヴェごとに決まっていて、**ヴァンデミエールは 40% が樽・60% がステンレス**、
**クロ・ド・ラベイやブラン・ド・ブランは 100% 樽**です。

**3. 補糖しない、マロラクティックを止める、ドザージュを 0〜4 グラムに置く。**
**補糖（シャプタリザシオン）は全キュヴェで一切なし。アルコールは自然発酵の度数のまま。**
**マロラクティック発酵は原則やりません**（＝リンゴ酸を残す）。
例外は **ヴァンデミエールとレヴォリュシオンの 2 本だけで、そこも 20% しか通しません。**
**ドザージュは 0 から 4 グラム。** レヴォリュシオンに至っては **0 グラム（ノン・ドゼ）**です。
**提供温度は生産者自身が 12〜13 ℃と指定しています**（→ 冷やしすぎない）。

### 「オーガニックですか？」と訊かれたら（Doyard で最も高頻度・最も危険）

🔴 **ここだけは台詞を決めておく。**

> 「**公式には «viticulture raisonnée»、日本語だと「減農薬・合理的防除」という言い方をしています。
> 資材の投入を可能な限り減らし、除草は機械で土を耕して行う、という書き方です。
> オーガニック認証やビオディナミではありません。**
> ただ、**クロ・ド・ラベイという 0.5 ヘクタールの単一区画についてだけは、化学的な資材を一切入れず、
> 土は馬で耕し、収量を 35〜40 hl/ha に抑えると明記されています。**」

**これで止める。** 「実質オーガニック」「認証を取っていないだけ」は**言わない**（公式に根拠が無い）。

### 🔴 リストで気をつけること — Doyard は 3 本中 2 本が要注意

| リストの印字 | 現場での扱い |
|---|---|
| `'Cuveé Vendémiaire,' Premier Cru Brut` NV / **200** | ✅ **公式キュヴェと確実に一致。安心して語ってよい唯一の 1 本。** 語れる中身: **シャルドネ 100%・3 年のアッサンブラージュ・樽 40%／ステンレス 60%・MLF 20%・一番搾りのみ・4 g/L・年約 30,000 本。** ⚠️ **メニューの «Cuveé» は綴り誤り（正しくは Cuvée）。** |
| `Grand Cru Extra Brut` **2015** / **455** | ⚠️ **「2015 年のグラン・クリュのブラン・ド・ブラン」までは言ってよい。**（畑＝ル・メニル／オジェ／アヴィズ／クラマン、樽 100%、MLF なし、一番＋二番搾り、グラン・ミレジムのみ生産・年約 3,500 本 — ここまでは公式）🔴 **ドザージュの具体値を言わない。** 公式の 2015 のシートが存在せず、公表値は年により **0.6 g/L（2009）／ 2 g/L（2012）／ 3 g/L（一般記述）**とばらついている。 |
| `'Voie d'Oger,' Grand Cru Extra Brut` **2016** / **700** | 🔴 **「ヴォワ・ドジェ」というキュヴェについて、THÉSEUS は公式の裏を一切持っていない。中身を語らない。** 語ってよいのは **生産者そのものの話（芯 1・2・3）だけ。** 「オジェのグラン・クリュの単一畑です」も**言ってはいけない**（区画がヴェルテュ側の可能性が残る）。**3 本中で最も高価（700）な一本なので、質問される確率が最も高い。マネージャーに確認を上げる案件。** |

### ⚠️ 現時点で言ってはいけないこと

- 🔴 **「オーガニック」「ビオ」「ビオディナミ」「ビオロジック」「実質オーガニック」「認証を取っていないだけ」**
  — **公式の語は «viticulture raisonnée» ただ一つ。** 全 22 ページ・PDF 8 件に «bio» 系の語はゼロ。**一語でも出したら誤りになる。**
- 🔴 **認証名（AB / Ecocert / Demeter / Biodyvin / HVE / Viticulture Durable en Champagne）** — **公式に言及ゼロ。**
- 🔴 **「畑を馬で耕しています」（ドメーヌ全体として）** — **公式に馬耕が書かれているのは Clos de l'Abbaye だけ。**
- 🔴 **「化学的なものは一切使いません」（ドメーヌ全体として）** — 同上。**全体の表記は «le moins d'intrants possible»＝「可能な限り少なく」であってゼロではない。**
- 🔴 **「除草剤は使いません」** — **公式は «travail mécanique du sol»（機械的耕耘）としか書いていない。除草剤の可否は明言されていない。**
- 🔴 **創業年・人名（「1677 年から」「1927 年にモーリス・ドワイヤールが」「現当主はギヨーム・ドワイヤール」）**
  — 🔴 **すべて公式に根拠ゼロ。** 公式が書いているのは **«レコルタン・マニピュランとして 4 世代、ヴィニュロンとして 12 世代»** だけ。
  **しかもその記述自体が 2017–2018 年更新のページのもので、「今何世代目か」も言えない。**（→ Open Questions #4）
- 🔴 **「〇代目当主の〇〇さんが造っています」** — **公式に個人名が一つも無い。** 法定表記に «M. Doyard» が 2 名（`charlesdoyard@` / `g.doyard@`）あるだけ。**現況未確認。**
- 🔴 **「ヴァンデミエールは 47〜60 ヶ月シュール・リー」「マロは 15%」「ヴェルテュ 65%」「樹齢 45 年以上」**
  — 🔴 **canonical の legacy テキストにある数値だが、公式と食い違うか、公式に存在しない。**
  **公式は MLF «20 %»、ベースは «principalement Vertus»（比率なし）、平均樹齢は畑全体で «40 年»、熟成期間は非開示**（旧 EN ページの «4 年» のみ、しかも 2007-2009 ベースの旧リリース）。
- 🔴 **「93 点」「94 点」などの点数** — **canonical に Wine Spectator の点数が入っているが、公式にも本書にも裏付けが無い。口に出さない。**
- 🔴 **「クロ・ド・ラベイはグラン・クリュ」** — 🔴 **ヴェルテュ産＝ Premier Cru。公式 fiche の見出しが «Extra-Brut, Premier Cru Millésimé 2015»。**
- 🔴 **「レヴォリュシオンは 2012 年のシャンパーニュ」** — **レヴォリュシオンは NV（3 年アッサンブラージュ）。** ページの «Mise en bouteille en 2012» は**瓶詰め年**であり、しかも ⚠️ fiche は «2015 年 6 月瓶詰め»。**別リリース。年号として語らない。**
- 🔴 **「ラタフィアはシャルドネ」** — **公式 fiche は «100% Pinot Noir»。**
- ⚠️ **「畑は 10 ヘクタール」／「11 ヘクタール」の断定** — **公式に両方ある。**言うなら「**10 ヘクタール強**」。
- ⚠️ **「平均樹齢 40 年」を「現在」として言わない** — **2018 年 2 月更新のページの数字。**言うなら「公式には平均 40 年と出ています」。
- ⚠️ **「特級 4 村のブレンドだから複雑」といった味の断定** — **公式にテイスティングノートは Œil de Perdrix の 1 本分しか無い。** 味は造りの構造から説明する。
- ⚠️ **`doyard.com` を公式サイトとして案内しない** — 🔴 **パーキングページ。公式は `champagnedoyard.fr`。**

---

## Akio's Insight

*（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）*

---

## Canonical Conflict

**なし。** `wine_makers.json`（384 生産者）を走査したが **`producer:doyard` は 1 件のみ**で、Doyard 姓・Vertus 近縁（Doyard-Mahé 等）の重複レコードは canonical に存在しない。`REGISTER.md` の真の衝突 9 件（P-1〜P-7 / C-1〜C-3）にも Doyard は含まれず、誤検出 54 件にも該当なし。**REGISTER.md への追記は不要。**

⚠️ **ただし「衝突ではないがデータ品質の問題」が 1 件ある** — canonical の `vintage:doyard-*` に格納された `description` / `winemaking` / `obp_note` の本文が、**公式サイトと複数箇所で食い違っている**（創業年・当主名・MLF 比率・栽培方式・提供温度・第三者点数）。**これは重複の問題ではないので Canonical Conflict には立てない。** → **Open Questions #4** として扱う。

---

## Sources

### 一次資料（公式サイト・2026-08-04 参照）✅

**`https://champagnedoyard.fr/`** — WordPress。**FR が原文、EN ページは 3 枚だけ**（`/the-house-2/` `/vineyard/` `/cuvee-eng/`、いずれも 2017-08 更新）。**食い違い時は FR を採用した。**

| ページ | 得た主な事実 |
|---|---|
| `/`（La Maison）・`/the-house-2/`（EN） | **RM 4 世代 / vigneron 12 世代**、**10 ha 超**、**6 村**、**Les Artisans du Champagne（2010・16 名）** |
| `/vignoble/`（FR, 2018-02）・`/vineyard/`（EN, 2017-08） | 🔴 **本書の栽培情報の中核。** **11 ha**・**CH 10 ha / PN 1 ha**・**村ごとの格付け**・**54 lieux-dits / 平均 0.20 ha**・**平均樹齢 40 年（EN は 39 年 ⚠️）**・**新規植樹なし／枯死株のみ補植**・**viticulture raisonnée**・**travail mécanique du sol**・**cordon de Royat monté permanent** |
| `/gamme/` ＋ `/gamme-mobile/` | **公式キュヴェは 9 本**（`/gamme-mobile/` は 9 本の全文を 1 ページに集約しており、個別ページの内容と一致） |
| `/gamme/cuvee-vendemiaire/` | 40%樽/60%inox・MLF 20%・cuvée のみ・**4 g/L**・**約 30,000 本 + 1,500 マグナム** |
| `/gamme/revolution/` | **Grand Cru・0 g/L**・50%樽/50%inox・MLF 20%・**«Mise en bouteille en 2012»** ⚠️ |
| `/gamme/clos-de-labbaye/` | **0.5 ha・1956 植樹・35〜40 hl/ha・馬耕・化学資材ゼロ・2 g/L・約 1,500 本 + 150 マグナム** |
| `/gamme/blanc-de-blancs/` | **GC 4 村・1ère+2ème presse・100% 樽・MLF なし・3 g/L・約 3,500 本・«uniquement les grands millésimes»** |
| `/gamme/oeil-de-perdrix/` | **PN 75%（Aÿ）/ CH 25%（Avize）・rosé de pressée・3 g/L・約 3,000 本** ＋ **唯一のテイスティングノート** |
| `/gamme/les-lumieres/` | **CH 66% / PN 34%**・**sur latte 約 10 年以上**・**0.8 g/L**・**年約 700 本**・**«2008 actuellement, puis 2012, 2018, 2019 à l'avenir»** |
| `/gamme/la-libertine/` | **4〜5 ミレジム・セラー 12 年超・約 4 bar・65 g/L・20 年超の古酒リキュール** |
| `/gamme/vieux-fombres/` | **Coteaux Champenois blanc・ヴェルテュ mi-coteau の lieu-dit・100% pièces bourguignonnes** ⚠️ fiche リンクが Ratafia を指す |
| `/gamme/la-ratafia/` | moût ＋ fine de Champagne・**樽 18 ヶ月**・提供 10〜12 ℃ |
| `/cuvee-eng/`（旧 EN 版 Vendémiaire, 2017-08） | ⚠️ **古いリリースの記述。** **«Quatre années de gestation»＝ 4 年**・**瓶重量 1kg800**・**2007-2008-2009 のアッサンブラージュ**・**5 g/L**（現行ページは 4 g/L） |
| `/contact/` | 住所 **51130 Vertus**・電話・FAX・**Clos Margot（closmargot.fr）** |
| `/mentions-legales-2/`（2026-03 更新） | **«M. Doyard» × 2（charlesdoyard@ / g.doyard@）**・制作 Equinoxes（Reims）・ホスティング PlanetHoster |
| `/charte-de-confidentialite/` | **DOYARD, société civile・資本金 155,310 €・RCS Châlons-en-Champagne 324 128 313・住所 51130 Blancs-Coteaux** ⚠️ |
| `/actualites/` `/news/` `/galerie/` | **本文ゼロ。** Facebook（`champagne.doyard.1`）と Instagram のフィード埋め込みショートコードのみ → **公式の「近況」は取得できない** |

### 公式 fiche technique PDF（8 件・全取得済み）✅

**取得場所** — `/Users/akiomatsumoto/Theseus_Phase0/research/producers/_sources/doyard/pdf/`
**発見方法** — 各 `/gamme/*` ページ末尾の「Fiche technique」リンク。**全 8 件が `wp-content/uploads/2021/06/` 配下。FR/EN 併記の 1 枚もの。**

| ファイル | 実際の中身 | HTML に無い情報 |
|---|---|---|
| `Vendémiaire-Brut.pdf` | Cuvée «Vendémiaire» Brut, Blanc de Blancs 1er Cru | **2015(50%)/2014(30%)/2013(20%)**、**2016 年瓶詰め**、**«principalement Vertus»** |
| `REVOLUTION.pdf` | Cuvée «Révolution» Non dosé, BdB Grand Cru | **2014(50%)/2013(30%)/2012(20%)**、**2015 年 6 月瓶詰め** ⚠️ |
| `clos_2012_new.pdf` | ⚠️ **ファイル名は 2012 だが中身は «Clos de l'Abbaye» Extra-Brut, Premier Cru Millésimé 2015** | **2016 年瓶詰め**、**2 g/L**、**生産 1,915 本**、**«Sans apport de produit chimique»**、**35〜40 hl/ha**、**1956 植樹・0.5 ha** |
| `cuvee-Blanc-de-Blancs-2012.pdf` | «Blanc de Blancs Grand Cru Millésime 2012» | **2013 年瓶詰め**、**2 g/L**、**«4 vins minimums»** ⚠️ |
| `cuvee-Blanc-de-Blancs-2009.pdf` | Cuvée «Blanc de Blancs» Grand Cru Millésimée 2009 | **2010 年 5 月瓶詰め**、**0.6 g/L**、**«4 vins minimums»** ⚠️ |
| `OEIL-DE-PERDRIX-2015.pdf` | Cuvée «Œil de Perdrix» Extra-Brut, Grand Cru Millésimée 2015 | **2016 年瓶詰め**、**3 g/L**、**生産 3,500 本** ⚠️ |
| `LES-LUMIERES-2008.pdf` | «Les Lumières» Grand Cru 2008 | **2009 年 9 月瓶詰め**、**0.8 g/L**、**CH 65% / PN 35%** ⚠️、**デゴルジュ後 8 年以上** |
| `LIBERTINE.pdf` | Cuvée «La Libertine» & son écrin | 18 世紀は 50〜200 g/L だったが **65 g/L で止めた**という設計意図 |
| `Ratafia-champenois.pdf` | Ratafia Champenois | **«100% Pinot Noir»**（HTML には品種の記載なし） |

🔴 **OBP 掲載 3 本のうち fiche PDF が存在するのは Vendémiaire の 1 本だけ。** **Blanc de Blancs は 2009 と 2012 のみで 2015 が無く、Voie d'Oger は PDF も HTML も存在しない。**

### 二次資料

**事実の根拠としては使用ゼロ。** 小売・EC・インポーター・レビュー集約（wine-searcher / vivino 等）・まとめブログ・Wikipedia は**一切参照していない**（検索は公式ドメインの特定と `doyard.com` の性質確認にのみ使用）。
📄 **1 箇所だけ例外的に注記** — **Comité Champagne（champagne.fr）の生産者ディレクトリ**。**生産者一次資料ではない**ため、そこにしか無い «Prix du Jury Jeune Talent du Champagne»（受賞年の記載なし）は **§History で ❓ 扱いにし、§Staff Notes には入れていない。** なお同ディレクトリの住所・電話・「10 ha 超」「6 村」「4 世代 / 12 世代」は**すべて公式サイトと一致**しており、公式記述の裏取りとしては機能した。

### THÉSEUS 内部データ 🔍

- `batch2.json`（canonical レコード概要 / canonical キュヴェ 2 件 / OBP intake 3 本）
- `theseus-phase0@main` `4a4934d` — `migration/out/resolved/wine_makers.json`・`cuvees.json`・`vintages.json`（**読み取りのみ。canonical 無変更**）
- `research/canonical_conflicts/REGISTER.md`（既出衝突の確認。Doyard は非該当）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | **High** | 住所・法人格・資本金・RCS 番号・連絡先・業態（RM）まで公式。⚠️ Vertus / Blancs-Coteaux の二重表記も両方公式で説明がつく |
| **Overview** | **High** | 面積・品種・村・造りの 4 原則がすべて公式 |
| **History** | 🔴 **Low** | **公式に沿革が存在しない。**確定年号は 1956 / 2010 の 2 つだけ。**当主名・創業年・世代の現況はすべて未確認。**canonical の記述は公式と無関係 |
| **Location** | **High** | 面積・品種別 ha・6 村の格付け・54 lieux-dits・平均区画面積・平均樹齢まで公開。⚠️ は 10/11 ha と 39/40 年の 2 点のみで、どちらも実害が小さい |
| **Farming** | **High** | 🔴 **「viticulture raisonnée」と公式が明言している**のが決定的に強い。**認証の不在も、Clos de l'Abbaye だけが例外であることも公式で確定できる。**「客が必ず訊く」層を誤りなく塞げる |
| **Winemaking** | **High**（工程・比率）／ **Low**（非開示部分） | **樽比率・樽の使用歴・MLF 比率・圧搾の使い分け・補糖の有無・ドザージュ・瓶詰め年・提供温度・熟成ポテンシャルまで全キュヴェ分が公式。**シャンパーニュの RM としては開示が厚い。**一方で酵母・SO2・濾過・デゴルジュマン時期・瓶熟期間は全面非開示** |
| **Style** | 🔴 **Low** | **公式のテイスティングノートは Œil de Perdrix の 1 本分のみ。**ハウススタイルは造りからの導出に留まる |
| **Important Cuvées** | **Medium** | **公式 9 キュヴェは High**（fiche PDF 8 件で数値まで確定）。**減点は OBP 側** — 3 本中 1 本しか公式に完全一致せず、1 本は 2015 の fiche が無く、1 本は公式に存在しない |
| **Staff Notes** | **High** | すべて上記 ✅ から構成。**特に「オーガニックか」への回答が公式語で固定できている**のがこの生産者では最大の価値 |
| **Canonical Conflict** | **High** | 384 生産者の全走査で重複ゼロを確認。REGISTER.md とも非重複 |
| **総合** | **Medium-High — staff-usable。70% 到達済み。** | **「客が必ず訊く」3 層（畑・栽培・造り）が公式で厚く取れており、しかも最も誤りやすい「オーガニックか」を公式語で封じられている。** Identity / Location / Farming / Winemaking / Important Cuvées(A) / Staff Notes / ⚠️ リストがすべて揃っている。**減点は History のほぼ全面欠落と、OBP 3 本中 2 本のキュヴェ未確定。ただしその 2 本は ⚠️ リストで「語らない範囲」を明示したので、現場で間違ったことを言わずに済む状態は満たしている。** |

---

## Open Questions

1. 🔴 **`'Voie d'Oger,' Grand Cru Extra Brut 2016`（OBP $700）とは何か。最優先。**
   公式サイト全 22 ページ ＋ fiche PDF 8 件に**一語も存在しない**。公式のキュヴェページは 2021 年 6 月で更新が止まっているため、
   **2021 年以降の新キュヴェである可能性が高いが確認手段が無い。**
   特に **«Grand Cru» 表記の真偽**が問題 — «Voie d'Oger» がオジェ／ル・メニル側の lieu-dit なら Grand Cru で正しいが、
   **ヴェルテュ側の「オジェへ抜ける道」の lieu-dit なら Premier Cru であり、メニュー表記が誤りになる。**
   → **確定には実ボトルの表・裏ラベル、またはインポーター（`/contact/` に «MAP Importateur Champagne DOYARD» とあるがリンク先未取得）の技術資料が要る。**
2. 🔴 **`Grand Cru Extra Brut 2015`（OBP $455）のドザージュ。**
   Blanc de Blancs Grand Cru Millésimé 2015 と見て蓋然性が高いが、**公式の 2015 fiche が公開されていない。**
   公表値は **0.6 g/L（2009）／ 2 g/L（2012）／ 3 g/L（ページの一般記述）**とばらつく。**現場では数値を言わない運用にしてあるが、確定できれば価値が高い。**
3. 🔴 **`Grand Cru Extra Brut 2015` は intake で `unresolved` だが、canonical には該当キュヴェ（VT 2015 付き）が既に存在する。**
   **印字が «Blanc de Blancs» を落としているために解決できていないだけと見える。**
   ⚠️ ただし機械的に alias を足すのは危険 — **«Extra-Brut, Grand Cru, Millésimée 2015» という文字列は Œil de Perdrix 2015（ロゼ）と完全一致する。**
   **掲載節（BLANC DE BLANCS）を条件に含めない限り誤爆する。** → **matcher の課題として起票が要る（research 側では触らない）。**
4. 🔴 **canonical `vintage:doyard-*` の本文が公式と食い違っている。昇格前に是正が要る。**
   | canonical の記述 | 公式 |
   |---|---|
   | 「1677 年から」「1927 年 モーリス・ドワイヤール」「現在はギヨーム・ドワイヤール」 | 🔴 **根拠ゼロ。**公式は «RM 4 世代 / vigneron 12 世代» のみ、個人名なし |
   | 「非教条主義的ビオディナミ」「Practicing organic viticulture」「biodynamic-leaning」「馬耕（ほぼ全区画）」 | 🔴 **公式は «viticulture raisonnée»。**馬耕は Clos de l'Abbaye のみ |
   | 「マロラクティック 15%」 | **公式は 20%** |
   | 「ヴェルテュ 65%」「樹齢 45 年以上」 | **公式は «principalement Vertus»（比率なし）／畑全体の平均 40 年** |
   | 「最低 47〜60 ヶ月シュール・リー」 | **公式は非開示**（旧 EN ページの «4 年» のみ、しかも旧リリース） |
   | `serving_temp: 8–10°C` | 🔴 **公式 fiche は全キュヴェ «12〜13 ℃»** |
   | 「Wine Spectator 93 点 / 94 点」 | **公式・本書ともに裏付けなし** |
5. ❓ **«Prix du Jury Jeune Talent du Champagne» の受賞年と受賞者。**
   Comité Champagne ディレクトリにのみ記載があり、**生産者自身の公式サイトには受賞の記述が皆無**。受賞年も不明。→ **現場では言わない。**
6. ❓ **canonical 未登録の公式キュヴェ 7 本**（Révolution / Clos de l'Abbaye / Œil de Perdrix / Les Lumières / La Libertine / En Vieux Fombrés / Ratafia）。
   **本書 §Important Cuvées A の表が数値まで揃った原資になる。** ただし **OBP には現状 1 本も載っていない**ため、昇格の優先度判断は Akio 案件。
7. ❓ **公式サイトの更新停止（キュヴェページ 2021-06 / `/vignoble/` 2018-02）の意味。**
   Facebook（`champagne.doyard.1`）と Instagram が実質的な現行チャネルになっている可能性が高いが、**本書では未取得。**
   → **Voie d'Oger の確認にも直結するため、生産者 SNS を一次資料として扱ってよいかは運用判断が要る（Akio 案件）。**
8. ❓ **`/contact/` の «MAP Importateur Champagne DOYARD» の実体。** リンク先を辿っていない。**インポーター資料は非公式ソースだが、Voie d'Oger 確定の現実的な唯一の経路になりうる。**
