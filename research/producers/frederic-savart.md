# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:frederic-savart` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagne-savart.com で確認**（一次資料）
> `📄` 提供資料のみに基づく（公式未確認）／ `⚠️` 食い違い。両方を残す
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04（EDT）／ 2026-08-05 JST・**公式サイトを再検証済み**
> 一次資料: `https://champagne-savart.com/` — **実質全 17 ページ（＝公式の全量）**
> `/`（index） `/philosophie` `/vins` `/photos` `/actualites` `/partenaires` `/contact` `/mentions-legales`
> `/vins/l-annee-2013` `/vins/expression-nature` `/vins/expression-rose-nature` `/vins/l-accomplie`
> `/vins/le-mont-benoit` `/vins/le-mont-des-chretiens` `/vins/les-noues` `/vins/l-ouverture` `/vins/bulle-de-rose`
> ※ `sitemap.xml` は **26 URL** を列挙するが、うち **9 件は `/vins/*` の重複エイリアス**
> （`/bulle-de-rose` = `/vins/bulle-de-rose`。**本文テキスト完全一致を実測**）。**固有ページは 17。**
>
> 🔴 **本生産者は「公式情報が構造的に薄い」ケース。** 公式サイトには
> **沿革ページが存在しない・畑面積の記載が無い・当主の氏名すら本文に出てこない。**
> Louis Latour のようなキュヴェ別テクニカルシート PDF は**存在しない**（site.js / 全 HTML を grep して
> `.pdf` 参照ゼロを実測）。EN 切替は**表示だけで機能しない**
> （`site.js` に言語処理が無く、`/en` は **HTTP 200 を返すがナビゲーション枠だけで本文が空**の soft-404）。
> フッタは **© 2017**。**サイト全体が 2017 年前後で更新停止している可能性が高い。**
> → **薄いまま出している。埋めるために非公式ソースを使っていない。**
> → **その分 §Staff Notes の ⚠️ リストが本書の主成果物である。**

---

## 🔴 統合禁止境界（intake の保護境界。canonical 昇格時に必ず参照）

| これ | ≠ | あれ |
|---|---|---|
| **Champagne Savart / Frédéric Savart**（本書。Écueil、1 chemin de Sacy） | ≠ | **Sacy 村の生産者**。「Sacy」は**Écueil にある道路名**（`1 chemin de Sacy`）であり、住所は **51500 ÉCUEIL**。→ canonical の subregion「Écueil & Sacy」の出所を Open Questions 3 で疑う |
| **Frédéric Savart**（生産者） | ≠ | **「Frédéric Savart France」**（`/partenaires` の**フランス国内取引先セクションの見出し**。取引先企業名ではない） |
| **Le Mont Benoît**（Villers-aux-Nœuds のリュー・ディ由来キュヴェ） | ≠ | **L'Année 2013 の構成畑としての "Le Mont Benoit"**（L'Année 2013 は Les Rosets と Le Mont Benoit の 2 リュー・ディから成る）。**同じ畑名が単独キュヴェとブレンドの両方に出る** |

---

## Identity

| | |
|---|---|
| **Canonical Name** | Frédéric Savart |
| **公式サイト上の表記** | **Champagne Savart**（`title` / mentions légales / footer はすべて "Champagne Savart"。**"Frédéric Savart" は本文中では `/partenaires` の見出しにしか現れない**）✅ |
| **Aliases** | 🔍 canonical `aliases` 未確認。実務上 **Savart / Champagne Savart / Frédéric Savart** は同一 |
| **業態** | レコルタン（栽培家元詰め）と読めるが、**公式サイトに RM/NM の記載も CIVC 登録番号の記載も無い** ❓ |
| **所在** | **1 chemin de Sacy, 51500 ÉCUEIL** ✅ |
| **連絡先** | `fred@champagne-savart.com` / `+33 (0)3 26 84 91 60` ✅ |
| **現当主** | ❓ **公式サイトに当主・醸造責任者の氏名・就任年の記載が一切ない。**メールのローカル部が `fred@` であることのみ ✅。**「現在 Frédéric Savart が当主」と公式で裏が取れていない**（現在性未確認） |
| canonical id | `producer:frederic-savart` |
| canonical entity confidence | 0.2 — エンティティ同定の確度。本書の充実度とは別軸 |

---

## Overview

✅ **モンターニュ・ド・ランス、Écueil の造り手。**公式サイトの `title` タグが自らを
「**La maison de champagne Savart se situe à Ecueil, village classé 1er cru**」
（シャンパーニュ・サヴァールは Écueil、プルミエ・クリュ格付けの村にある）と規定している。
**Écueil が 1er cru であることは公式の言明**であり、全キュヴェが `PREMIER CRU` を冠する根拠。

✅ **ピノ・ノワールの村の造り手。**公式の 9 キュヴェのうち、**セパージュ記載のある 8 つすべてでピノ・ノワールが主体か 100%**。
唯一の例外が Chardonnay 100% の **Le Mont des Chrétiens**。
**Blanc de Blancs 単独のキュヴェは公式サイトに存在しない**（→ §Important Cuvées の 🔴）。

✅ **ドザージュが一貫して低い。**公式記載のある 8 キュヴェで **0〜7 g/L**、うち 5 つが **0〜3 g/L**。
Brut Nature（0 g/L）を 2 つ持つ。

✅ **自己規定は「テロワールの実験室」。**
> 「Le champagne Savart est **un laboratoire de terroirs et un créateur de cuvées**.」
> （シャンパーニュ・サヴァールはテロワールの実験室であり、キュヴェの創造者である）

リュー・ディ単位（Le Mont Benoît / Le Mont des Chrétiens / Les Noues）と、
ブレンド（L'Accomplie / L'Ouverture / Bulle de Rosé）と、
ヴィエイユ・ヴィーニュの樽仕込み（Expression Nature / Expression Rosé Nature）が並走する構成。

---

## History

🔴 **公式サイトに沿革ページが存在しない。**`sitemap.xml` の全 17 URL を実測したが、
`histoire` / `domaine` / `famille` / `about` に相当するページは**無い**。
創業年・世代・取得畑の履歴・当主交代について、**公式の記述はゼロ**。

| 事実 | 出典 |
|---|---|
| サイトのフッタ著作権表示が **© 2017** | ✅ |
| サイト制作は **MKB Prod（8 rue Clovis, 51100 Reims）** | ✅ `/mentions-legales` |
| ギャラリー画像のファイル名に **`20141209_...`**（2014 年 12 月）を含むものがある | ✅ `/photos` |
| 法人名義の表記は **「Champagne Savart」**（mentions légales） | ✅ |

❓ **創業年・世代数・現当主の就任年、いずれも未確認。** → Open Questions 1

⚠️ **現場で流通している「サヴァール像」は、本書では一切採用していない。**
創業年、何代目か、当主が家業を継いだ年、当主の前職——これらは業界で語られているが、
**公式サイトに一行も無い**。§Staff Notes の ⚠️ リストで**明示的に発話禁止**にしてある。

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Champagne — **Montagne de Reims** 🔍（canonical・OBP セクション由来。公式サイトは「Montagne de Reims」の語を使っていない） |
| **本拠地 / 村** | **Écueil**（51500）。公式が **village classé 1er cru** と明記 ✅ |
| **住所** | **1 chemin de Sacy, 51500 Écueil** ✅ |
| **もう一つの村** | **Villers-aux-Nœuds** ✅（L'Accomplie / Le Mont Benoît / L'Année 2013 に登場） |
| **土壌** | **argilo-calcaire（粘土石灰質）** ✅ — Écueil・Villers-aux-Nœuds の両方で明記 |
| **総面積** | ❓ **公式に一切記載が無い。**ha 数を言ってはいけない → Open Questions 2 |

### Key Vineyards（公式のキュヴェページから抽出した**リュー・ディの全量**）✅

| リュー・ディ | 村 | 土壌 | どのキュヴェに使われるか |
|---|---|---|---|
| **Aillys** | Écueil | argilo-calcaire | Expression Nature / Expression Rosé Nature |
| **Chaillots derrière Moutier** | Écueil | argilo-calcaire | Expression Nature / Expression Rosé Nature |
| **Gillys** | Écueil | argilo-calcaire | Expression Nature / Expression Rosé Nature |
| **Le Mont des Chrétiens** | Écueil | — | Le Mont des Chrétiens（単一リュー・ディ・Chardonnay 100%） |
| **Les Noues** | Écueil 🔍 | — | Les Noues（公式ページは **「À venir...」＝準備中**で中身なし） |
| **Le Mont Benoit** | **Villers-aux-Nœuds** | argilo-calcaire | Le Mont Benoît（単独）／ L'Année 2013（構成畑） |
| **Les Rosets** | Écueil または Villers-aux-Nœuds ❓ | — | L'Année 2013（構成畑） |

⚠️ **Villers-aux-Nœuds の格付けを公式は明言していない。** Écueil については
`title` で「village classé 1er cru」と明記があるが、**Villers-aux-Nœuds には同種の記述が無い。**
ただし Villers-aux-Nœuds 単独畑の **Le Mont Benoît が `PREMIER CRU` を名乗っている**ため、
1er cru であることは実質的に導けるが、**公式の直接言明ではない。** → Open Questions 4

⚠️ **canonical は Bulle de Rosé と L'Ouverture の subregion を「Écueil & Sacy」としているが、
公式サイトに「Sacy 村」の言及は無い。**サイト上で "Sacy" が出るのは**住所の道路名 `1 chemin de Sacy` だけ**。
両キュヴェの公式ページはそもそも **Terroir 欄自体を持たない**。→ Open Questions 3（**両方の値を消さずに残す**）

---

## Farming

✅ **公式の言明は、全キュヴェページに繰り返される次の一文に集約される。**

> 「**Vignes cultivées dans le respect des équilibres naturels.**」
> （自然の均衡を尊重して栽培された葡萄）

✅ **`/philosophie` が方法論を述べている（サイト上で最も情報量のあるページ）。**

> 「Nous cherchons à préserver **une expression de la nature la plus pure possible**.
> Nous privilégions **le travail à la main** et **les méthodes préventives ne cherchant pas à
> éradiquer les maladies mais à préserver un écosystème vivant et divers**.」

| 公式が言っていること | 内容 |
|---|---|
| **手作業を優先する** | 「le travail à la main」 |
| **予防的手法** | 病害を**根絶しに行かない**。**生きた多様な生態系を保つ**ことを目的とする |
| **自然の均衡への敬意** | 全キュヴェページの定型文 |

🔴 **公式サイトには、オーガニック認証・ビオディナミ認証・HVE・VDC（Viticulture Durable en Champagne）の
記載が一切ない。認証機関名も、転換年も、「bio」「biologique」「biodynamie」の語すら出てこない。**
「病害を根絶しに行かない予防的手法」という**書きぶりそのものが、認証を主張しない造り手の書きぶり**である。
→ **§Staff Notes で最優先の発話禁止項目。** → Open Questions 5

⚠️ **定型文が付いていないキュヴェが 1 つある。** `L'Année 2013` のページだけは
「Vignes cultivées dans le respect des équilibres naturels.」の代わりに
「**Raisins préssurées ensembles**（葡萄をまとめて圧搾）」と書かれている。**意味のある差か、単なる差し替え漏れかは不明** ❓

---

## Winemaking

🔴 **醸造の記述は、公式サイト全体で「Expression」2 キュヴェにしか存在しない。**

| 項目 | 公式記述 | 対象 |
|---|---|---|
| **発酵・熟成容器** | **Fût de 500 L**（500 リットル樽） | Expression Nature / Expression Rosé Nature のみ ✅ |
| **シュール・リー** | **10 mois sur lie**（澱と共に 10 ヶ月） | 同上 ✅ |
| **葡萄樹齢** | **100% très vieilles vignes de Pinot Noir**（極めて古い樹のピノ・ノワール 100%） | 同上 ✅ |
| **圧搾** | **Raisins pressurés ensemble**（まとめて圧搾＝混醸） | L'Année 2013 のみ ✅ |
| **ドザージュ** | 0 / 3 / 5 / 6 / 7 g/L（キュヴェ別に明記） | 8 キュヴェ ✅ |

✅ **醸造哲学（`/philosophie`）— これは明快に書かれている。**

> 「Dès lors, **la vinification et l'élevage consistent non pas à façonner les vins selon nos désirs
> mais de conserver et de protéger une création unique et fragile de Dame nature**.
> Ainsi, cette logique permet de découvrir tous les aspects, les nuances et les subtilités
> d'une même appellation.」
> （醸造と熟成とは、**我々の望むままにワインを形づくることではなく**、自然という婦人の唯一無二で
> 壊れやすい創造物を保存し守ることである。この論理によってこそ、同一のアペラシオンの
> あらゆる相・ニュアンス・機微を発見できる。）

✅ **ハッシュタグとして掲げる自己規定: `#vinsidentitaires`**

> 「Faire des vins singuliers, identitaires, **bien loin de la standardisation du goût**.
> C'est le vin dans lequel le vigneron s'implique, un vin où **la technique et le savoir-faire
> se placent au service d'une intention, d'une émotion et d'un ressenti**.」
> （味の標準化から遠く離れた、固有の・アイデンティティを持つワインを造る。造り手が身を投じるワイン、
> **技術と know-how が意図・情動・感覚に奉仕する**ワイン。）

❓ **公式記述が完全に無い項目**（→ Open Questions 6）:
**MLF の有無・天然酵母・新樽比率・樽の産地/樽元・リザーヴワイン/ソレラの有無・
瓶熟期間・デゴルジュマン時期・ドザージュ用リキュールの内容・SO2 の方針・
Le Mont Benoît / Le Mont des Chrétiens / L'Accomplie / L'Ouverture / Bulle de Rosé の容器と熟成。**

---

## Style

✅ 公式から**事実として言えるスタイルの規定要因**:

1. **ピノ・ノワール主体。** セパージュ記載のある 8 キュヴェのうち、**PN 100% が 3 つ**
   （L'Ouverture / Expression Nature / Expression Rosé Nature）、**PN 主体が 4 つ**
   （Le Mont Benoît 95%、L'Accomplie 80%、Bulle de Rosé 70%＋赤 8%、L'Année 2013 60%）。
   **Chardonnay 100% は Le Mont des Chrétiens ただ 1 つ。**
2. **低ドザージュが構造的な署名。** Brut Nature 0 g/L × 2、Extra Brut 3 g/L × 3、
   Extra Brut 5 g/L × 1、Brut 6 g/L × 1、Brut 7 g/L × 1。**最も甘いキュヴェで 7 g/L。**
3. **リュー・ディ単位の分割。** Écueil の Aillys / Chaillots derrière Moutier / Gillys /
   Le Mont des Chrétiens / Les Noues、Villers-aux-Nœuds の Le Mont Benoit、Les Rosets —
   **区画名をラベルとキュヴェ設計に持ち込む**。公式の自己規定「**laboratoire de terroirs**」がこれを言う。
4. **介入を最小にするという明示的な立場。**「我々の望むままにワインを形づくることではない」。
5. **樽と古樹を使う枠が別立てで存在する。** Expression 2 種のみ 500L 樽・10 ヶ月シュール・リー・
   très vieilles vignes。**サヴァールの「樽の顔」はこの 2 本に集中している。**

❓ **公式サイトに第三者評価・点数・プレス欄は無い。**（`/actualites` は SNS フィード用の枠のみで、
サーバ側 HTML には記事本文が 1 件も入っていない。）→ Open Questions 7

---

## Important Cuvées

### A. 公式サイトが掲載する全 9 キュヴェ ✅（これが公式の全量）

| # | キュヴェ | 表示 | 村 / リュー・ディ | セパージュ | ドザージュ | 醸造 |
|---|---|---|---|---|---|---|
| 1 | **L'Année 2013** | EXTRA BRUT | Écueil, Villers-aux-Nœuds ／ **Les Rosets, Le Mont Benoit** | Chardonnay 40% / Pinot Noir 60% | **3 g/L** | **葡萄をまとめて圧搾** |
| 2 | **Expression Rosé Nature** | **BRUT NATURE** | Écueil（argilo-calcaire）／ Aillys, Chaillots derrière Moutier, Gillys | **100% très vieilles vignes de Pinot Noir** | **0 g/L** | **500L 樽・10 ヶ月シュール・リー** |
| 3 | **Le Mont Benoît** | EXTRA BRUT | **Villers-aux-Nœuds**（argilo-calcaire） | Pinot Noir 95% / Chardonnay 5% | **3 g/L** | — |
| 4 | **Le Mont des Chrétiens** | EXTRA BRUT | Écueil ／ **Le Mont des Chrétiens** | **Chardonnay 100%** | **3 g/L** | — |
| 5 | **L'Accomplie** | EXTRA-BRUT | Écueil, Villers-aux-Nœuds | Pinot Noir 80% / Chardonnay 20% | **5 g/L** | — |
| 6 | **Les Noues** | ❓ | ❓ | ❓ | ❓ | 🔴 **公式ページは「À venir...（近日公開）」のみ。中身ゼロ** |
| 7 | **Expression Nature** | **BRUT NATURE** | Écueil（argilo-calcaire）／ Aillys, Chaillots derrière Moutier, Gillys | **100% très vieilles vignes de Pinot Noir** | **0 g/L** | **500L 樽・10 ヶ月シュール・リー** |
| 8 | **L'Ouverture** | BRUT | ❓（Terroir 欄なし） | **Pinot Noir 100%** | **7 g/L** | — |
| 9 | **Bulle de Rosé** | **BRUT** | ❓（Terroir 欄なし） | Pinot Noir 70% / Chardonnay 22% / **赤ワインのピノ・ノワール 8%** | **6 g/L** | 🔍 **赤を混ぜるロゼ・ダサンブラージュ** |

⚠️ **Expression Nature と Expression Rosé Nature の公式スペックは、名称以外まったく同一である。**
Terroir・リュー・ディ・セパージュ・醸造・ドザージュのすべてが 1 文字違わない。
**ロゼ側に赤ワインを加えるのか、セニエなのか、公式は何も書いていない。**
サイトのコピー流用の可能性が高いが、**どちらとも判定できない。両方残す。** → Open Questions 8

### B. canonical 登録キュヴェ 8 件 × 公式サイト 🔍

| canonical キュヴェ | canonical VT | 公式サイトでの確認 |
|---|---|---|
| **Le Mont Benoît Extra Brut Premier Cru** | 2020 | ✅ 一致（公式は **Benoît** とトレマ付き） |
| **Mont des Chrétiens** | 2020 | ✅ 一致（公式名は **Le Mont des Chrétiens**、定冠詞つき） |
| **L'Accomplie Extra Brut Premier Cru** | NV | ✅ 一致 |
| **Bulle de Rosé Premier Cru Brut** | NV | ✅ 一致（**Brut** で正しい。§C の 🔴 を見よ） |
| **L'Ouverture Blanc de Noirs Premier Cru Brut** | NV | ⚠️ **公式に「Blanc de Noirs」の表記は無い。**公式は「PREMIER CRU - L'OUVERTURE / BRUT / Cépage : Pinot Noir 100%」。**中身は Blanc de Noirs だが、ラベル文言としては公式未確認** |
| **Les Noues** | 2020 | ⚠️ **公式ページは存在するが「À venir...」で中身ゼロ。**実在は確認できるが**スペックは一切不明** |
| **Le Millésime — Premier Cru Extra Brut** | 2008 | ❓ **公式に「Le Millésime」という名のキュヴェは無い。**公式のヴィンテージ枠は **「L'Année 2013」**。→ §C-1 |
| **Blanc de Blancs Extra Brut Premier Cru** | NV | 🔴 **公式サイトに Blanc de Blancs キュヴェは存在しない。**Chardonnay 100% は **Le Mont des Chrétiens** ただ 1 つ。→ §C-2 |

🔍 **公式にあって canonical に無いキュヴェ 3 件**: **L'Année 2013 / Expression Nature / Expression Rosé Nature**。
（**OBP には 1 本も載っていないため、Packet 優先度は低い。**ただし canonical 昇格時には登録候補。）

### C. OBP 掲載 5 本 🔍（うち**未解決 2 本**）

| # | OBP 印字（そのまま） | VT | 価格 | OBP セクション | state | canonical | 公式サイトとの照合 |
|---|---|---|---|---|---|---|---|
| 1 | **Premier Cru Extra Brut** | **2008** | **$500** | CHAMPAGNE \| **BLENDS** | 🔴 **unresolved** | `Le Millésime — Premier Cru Extra Brut` 2008 が候補 | ❓ **公式に 2008 のページ無し** |
| 2 | **'Le Mont Benoit,' Premier Cru Extra Brut** | 2020 | $580 | CHAMPAGNE \| **BLENDS** | alias | ✅ 登録済（2020） | ✅ 公式 **Le Mont Benoît**。PN 95%/Ch 5% ＝ **BLENDS 分類は正しい** |
| 3 | **Premier Cru Extra Brut** | **NV** | **$380** | CHAMPAGNE \| **BLANC DE BLANCS** | 🔴 **unresolved** | `Blanc de Blancs Extra Brut Premier Cru` NV が候補 | 🔴 **公式に該当キュヴェ無し** |
| 4 | **'L'Ouverture,' Premier Cru Brut** | NV | $280 | CHAMPAGNE \| **BLANC DE NOIRS** | alias | ✅ 登録済（NV） | ✅ 公式 L'Ouverture、**PN 100%・Brut・7 g/L** ＝ BLANC DE NOIRS 分類は正しい |
| 5 | **'Bulle de Rosé,' Premier Cru Extra Brut** | NV | $360 | CHAMPAGNE \| **ROSÉ** | alias | ✅ 登録済（**Brut**） | 🔴 **⚠️ 表示の食い違い。**公式は **BRUT・6 g/L**。**OBP メニューの「Extra Brut」印字は公式と一致しない** |

#### C-1. 🔴 未解決①「2008 Premier Cru Extra Brut」（$500）

- canonical 側に **`Le Millésime — Premier Cru Extra Brut` / vintage 2008 / subregion「Écueil & Villers-aux-Nœuds」** が既にあり、
  **年・Extra Brut・BLENDS（＝単一品種ではない）・村構成のすべてが整合する。**
- **公式サイトのヴィンテージ枠は `L'Année 2013`（Écueil＋Villers-aux-Nœuds、Ch 40/PN 60、Extra Brut 3 g/L、混醸）** であり、
  **年号がキュヴェ名になる系列**であることが確認できる。この系列の 2008 版であれば整合する。
- ⚠️ **だが公式サイトに 2008 のページは無く、「Le Millésime」という名称も公式に存在しない。**
  **状況証拠は強いが、公式で確定できない。unresolved のまま据え置く。** → Open Questions 9

#### C-2. 🔴 未解決②「NV Premier Cru Extra Brut」（$380・BLANC DE BLANCS 欄）

- canonical に **`Blanc de Blancs Extra Brut Premier Cru` / NV / Écueil** があり、OBP のセクション（BLANC DE BLANCS）と一致する。
- 🔴 **しかし公式サイトには Blanc de Blancs のキュヴェページが無い。**sitemap 全 17 URL を実測済み。
  公式の Chardonnay 100% は **`Le Mont des Chrétiens`（Extra Brut・3 g/L・Écueil の単一リュー・ディ）だけ**。
- ⚠️ **したがって 2 つの相反する解釈が立ち、公式では決着しない。両方を残す:**
  1. **公式サイトが 2017 年以降更新されておらず、その後リリースされた NV Blanc de Blancs が未掲載**
  2. **OBP の印字が Le Mont des Chrétiens を指しており、NV 表記・キュヴェ名欠落はメニュー側の欠陥**
     （ただし canonical の Mont des Chrétiens は **2020 ヴィンテージ**であり NV ではない → 解釈 2 は弱い）
- **unresolved のまま据え置く。** → Open Questions 10

### D. 流通 ✅（`/partenaires`）

- **「Savart dans le monde」に 31 の海外取引先を掲載。**
- 🔴 **米国は 2 社: `Grand Cru Selections（New York）` と `Galaxy Wine Company（Oregon）`。**
  **ニューヨークの店舗にとって、公式サイトが名指しする輸入元は Grand Cru Selections である。**
- 日本は **Firadis Sarl le Bourgeon** ✅
- フランス国内（見出し「Frédéric Savart France」）に **L'Assiette Champenoise・Les Crayères・Le Cercle Champenois・
  Caves du Forum（Reims）、Le 520（Épernay）、Les Grandes Caves（Paris）、Chez Odette、La Maye、
  Les Cocottes du Cul de Poule、CPH - Perardel、Balourdet** を掲載 ✅
  → **ランスの二大レストラン（L'Assiette Champenoise / Les Crayères）に入っていることを公式が明示している。**
  **これは「現地での評価」を、非公式ソースに頼らず語れる唯一の公式材料である。**

---

## Staff Notes

> この節は上記の ✅ からのみ構成している。裏の取れていない事柄は書いていない。
> 🔴 **本生産者は公式情報が薄い。**だからこそ**⚠️ リストを先に読むこと。**

**一行で言うと** — 「モンターニュ・ド・ランスの **Écueil**、プルミエ・クリュの村の造り手。
**ピノ・ノワールの村で、区画ごとにキュヴェを分ける**。**ドザージュは最大でも 7 g/L**」。

**ゲストへの説明の芯（3 点）**

1. **Écueil という村。** モンターニュ・ド・ランスのプルミエ・クリュ村で、**ピノ・ノワールの村**です。
   土壌は**粘土石灰質（argilo-calcaire）**。サヴァールはここと隣の **Villers-aux-Nœuds** の畑を持ちます。
   造り手自身が「**テロワールの実験室（laboratoire de terroirs）**」と名乗っていて、
   **Le Mont Benoît / Le Mont des Chrétiens / Les Noues** のように**区画名がそのままキュヴェ名になる**。

2. **ドザージュが低い。**リストに載っている 5 本のうち、**Le Mont Benoît が 3 g/L、L'Accomplie が 5 g/L、
   Bulle de Rosé が 6 g/L、L'Ouverture が 7 g/L。**最も甘いもので 7 g/L です。
   ノン・ドゼ（0 g/L）のキュヴェも造っていますが、こちらのリストには入っていません。

3. **リストの並び方に意味がある。**
   - **`L'Ouverture`（$280）＝ ピノ・ノワール 100%**。名前どおり「開幕」の 1 本で、**ドザージュ 7 g/L と、ラインで最も高い**。入り口。
   - **`Le Mont Benoît`（2020, $580）＝ Villers-aux-Nœuds の単一リュー・ディ**。ピノ・ノワール 95%・シャルドネ 5%。**3 g/L**。
     少量のシャルドネが入るので、リスト上は BLENDS に置かれています。
   - **`Bulle de Rosé`（$360）＝ 赤ワインを 8% 加えるロゼ**（ピノ 70 / シャルドネ 22 / 赤のピノ 8）。**6 g/L**。
   - **2008（$500）とNV のブラン・ド・ブラン（$380）は、キュヴェ名がメニューに印字されていません**（下記 ⚠️）。

**ランスでの立ち位置を言いたいとき**（公式で裏が取れる唯一の材料）
公式サイトの取引先一覧に、**L'Assiette Champenoise と Les Crayères（いずれもランス）**が載っています。
「ランスの店では扱われています」までは公式で言えます。**それ以上（評価・点数・希少性）は言わない。**

---

**🔴🔴 現時点で言ってはいけないこと（本書で最も重要な節）**

> 公式サイトは**沿革ページを持たず、当主名も面積も認証も書いていない。**
> **薄い生産者ほど現場で即興が起きる。**以下は**すべて発話禁止**。

**① 栽培・認証について**
- ❌ **「ビオ」「オーガニック」「有機認証」「ビオディナミ」と言わない。** **公式サイトに認証の記載も、
  bio / biologique / biodynamie の語も一切ない。**公式が言っているのは
  「**自然の均衡を尊重して栽培**」「**手作業を優先**」「**病害を根絶しようとせず、生きた多様な生態系を保つ予防的手法**」だけ。
  → **言ってよいのはこの 3 つの日本語訳まで。**「認証を取っている」は誤り。**「認証は謳っていません」が正しい答え方。**
- ❌ **HVE / VDC（Viticulture Durable en Champagne）などの認証名を出さない。**公式に記載なし。

**② 造り手・沿革について**
- ❌ **「〇代目」「〇年に継いだ」「創業〇年」と言わない。** **公式サイトに沿革が存在しない。**
- ❌ **当主の前職（サッカー選手だった等）の逸話を語らない。** 業界で流通しているが**公式に一行も無い**。
  裏が取れていない人物譚を客に語るのは、この生産者では特に危険。
- ❌ **「現在の当主は Frédéric Savart です」と断定しない。** 公式サイト本文に当主名の記載がなく、
  **現況が確認できていない**（サイトは **© 2017** で更新停止の可能性）。
  → **「Savart 家の造り手です」までにとどめる。**

**③ 規模・畑について**
- ❌ **ha 数を言わない。** **公式に面積の記載がゼロ。**「4 ヘクタール」等の数字を出さない。
- ❌ **年間生産本数を言わない。** 公式に記載なし。
- ❌ **「Sacy 村の畑」と言わない。** **Sacy は住所の道路名（1 chemin de Sacy）**で、**所在地は Écueil**。
  canonical の subregion に「Écueil & Sacy」とあるが、**公式に Sacy 村の言及は無い**。
- ⚠️ **Villers-aux-Nœuds を「プルミエ・クリュの村」と断定しない。** 公式が 1er cru と明記しているのは **Écueil** のみ。

**④ 醸造について**
- ❌ **新樽比率・MLF・天然酵母・瓶熟期間・デゴルジュマン時期を言わない。** **公式に一切記載が無い。**
- ⚠️ **「樽で造る造り手」と一般化しない。** 公式が樽（**500L・10 ヶ月シュール・リー**）を明記しているのは
  **`Expression Nature` と `Expression Rosé Nature` の 2 本だけ**で、**この 2 本はどちらも当店のリストに無い**。
  **リスト上の 5 本については、容器・熟成に関する公式情報はゼロ。**

**⑤ 🔴 メニューの印字そのものに問題がある 3 点（現場で必ず当たる）**

| メニュー印字 | 実際 | 現場での言い方 |
|---|---|---|
| **`'Bulle de Rosé,' Premier Cru Extra Brut`** | 🔴 **公式は BRUT（6 g/L）。Extra Brut ではない** | **「エクストラ・ブリュットですか？」と訊かれたら「造り手の表記はブリュットで、ドザージュは 6g です」と答える。**メニューの印字を根拠に Extra Brut と説明しない |
| **`2008 Premier Cru Extra Brut`（$500）** | ⚠️ **キュヴェ名がメニューに無い。**ヴィンテージ・キュヴェであることまでは言えるが、**キュヴェ名は未確定** | **「2008 のヴィンテージものです」までにとどめ、キュヴェ名を口にしない。**ボトルのラベルを持って行って確認するのが正解 |
| **`NV Premier Cru Extra Brut`（$380・ブラン・ド・ブラン欄）** | 🔴 **キュヴェ名がメニューに無く、公式サイトにブラン・ド・ブランのキュヴェが存在しない** | **「シャルドネ 100% のキュヴェです」までにとどめる。**キュヴェ名も、単一区画かどうかも言わない。**必ずラベルを確認する** |

**⑥ リスト内で混同しやすい点**
- **`Le Mont Benoît`（単独キュヴェ）** と、**L'Année 2013 の構成畑としての `Le Mont Benoit`** は別物。
  ただし**リストに載っているのは単独キュヴェの 2020 だけ**なので、実務上は混乱しない。
- **`Le Mont Benoît`（Villers-aux-Nœuds・ピノ主体）** と **`Le Mont des Chrétiens`（Écueil・シャルドネ 100%）** は
  **名前が似ているが別の村・別の品種。** **Le Mont des Chrétiens は当店リストに無い。**

**⑦ 🔴 市中に流通している「サヴァール像」— 全部言わない**

> 公式ドメインを特定するための検索で、小売・EC・インポーター・イベントの各ページが返ってきた。
> **そこに載っていた事実主張は本書では一切採用していない。**以下は**すべて「公式未確認」であり、発話禁止**。
> ゲストやスタッフが口にした場合も、**同意も否定もせず「造り手の公式サイトには記載がありません」と返す。**

| 市中で流通している主張 | 公式サイトでの裏 | 現場での扱い |
|---|---|---|
| **「4 ヘクタール」等の畑面積** | ❌ **公式に面積の記載ゼロ** | 数字を出さない |
| **「20XX 年に家業を継いだ」「〇代目」** | ❌ **公式に沿革ページが存在しない** | 継承年・世代を言わない |
| **当主の前職の逸話（元アスリート等）** | ❌ **公式に一行も無い** | **人物譚を客に語らない** |
| **「Écueil / Trepail」など Écueil 以外の村を並べる表記** | ❌ **公式が挙げる村は Écueil と Villers-aux-Nœuds の 2 つだけ** | 他村を足さない |
| **`L'Ouverture` を「ブラン・ド・ブラン」と記載する売り手表記** | 🔴 **公式は `L'Ouverture` = ピノ・ノワール 100%**（＝ブラン・ド・**ノワール**の中身） | **売り手の表記に引きずられない。**当店メニューの BLANC DE NOIRS 欄が正しい |

**この生産者は「語れることが少ない」のではなく、「語ってよいことの境界が異常に鮮明」な生産者である。**
**公式が書いた範囲＝上の §Staff Notes 芯 3 点。その外は全部沈黙が正解。**

---

## Akio's Insight

*（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）*

---

## Canonical Conflict

> 🔴 **本節は解決しない。エスカレーションのみ。canonical は 1 バイトも書き換えていない。**
> 既存の登録票 `/Users/akiomatsumoto/Theseus_Phase0/research/canonical_conflicts/REGISTER.md`（P-1〜P-7 / C-1〜C-3、
> 誤検出 54 組の §C を含む）を**先に全読した。Savart は producer 側・cuvée 側とも一切登場しない**（未登録）。
> **producer レベルの衝突は無い。**`producer:frederic-savart` は 1 件のみで、`Savart` を含む別 producer レコードは存在しない。
> 下記は **cuvée レベルの新規候補 1 件**。**REGISTER.md への追記が必要**（当方は REGISTER.md を編集していない）。

### CS-1（新規候補・cuvée）— `Blanc de Blancs Extra Brut Premier Cru` / `Mont des Chrétiens`

**① 衝突している canonical ID**
`producer:frederic-savart` 配下の 2 キュヴェ:
- **`Blanc de Blancs Extra Brut Premier Cru`** — subregion「Montagne de Reims — Écueil Premier Cru」／ vintages: **NV**
- **`Mont des Chrétiens`** — subregion「Montagne de Reims — Écueil Premier Cru」／ vintages: **2020**

**② なぜ重複に見えるか**
**同一生産者・同一 subregion（Écueil 1er cru）・同一品種構成（シャルドネ 100%）・同一表示（Extra Brut）**の 2 レコードでありながら、
**公式サイトにシャルドネ 100% のキュヴェは `Le Mont des Chrétiens` ただ 1 つしか存在しない。**
片方が**一般記述子（"Blanc de Blancs"）**、片方が**リュー・ディ名**という、
REGISTER.md **C-3（Denis Mortet／命名規約の二重化）と同型のパターン**である。

**③ Evidence**
| | `Blanc de Blancs Extra Brut Premier Cru` | `Mont des Chrétiens` |
|---|---|---|
| canonical subregion | Écueil 1er cru | Écueil 1er cru（**同一**） |
| canonical vintage | **NV** | **2020**（⚠️ **ここだけ食い違う**） |
| 公式サイトに該当ページ | 🔴 **無い**（固有 17 ページ実測。BdB キュヴェは存在しない） | ✅ `/vins/le-mont-des-chretiens` |
| 公式スペック | ❓ | **Écueil / リュー・ディ Le Mont des Chrétiens / Chardonnay 100% / EXTRA BRUT / 3 g/L** |
| 命名の水準 | 一般記述子（品種カテゴリ） | リュー・ディ固有名 |

- 公式の全 9 キュヴェのうち **Chardonnay 100% は 1 つだけ**。「Écueil の 1er cru・シャルドネ 100%・Extra Brut」を
  満たす公式キュヴェは **`Le Mont des Chrétiens` 以外に存在しない。**
- **反証**: 公式サイトは **© 2017 で更新停止の疑いが強く**、2017 年以降にリリースされた
  **NV Blanc de Blancs が単に未掲載である可能性を排除できない。**（canonical が持つ 2020 ヴィンテージ 3 件
  ＝ Le Mont Benoît / Mont des Chrétiens / Les Noues も公式サイトには年号として出てこない。
  **canonical のほうが公式サイトより新しい情報を持っている。**）
- **NV と 2020 という vintage の違いは、同一ワインの別リリースでも説明でき、別ワインの証明にもならない。**

**④ OBP への影響**
🔴 **直接の実害あり。** OBP の **`NV Premier Cru Extra Brut` $380（CHAMPAGNE | BLANC DE BLANCS 欄・キュヴェ名の印字なし）**が
**unresolved のまま滞留している。**
- CS-1 が「同一キュヴェの二重登録」だった場合 → **canonical のキュヴェ数が 1 件過大**であり、
  この $380 は `Mont des Chrétiens` 系列に解決すべきボトルになる。
- CS-1 が「別キュヴェ」だった場合 → **$380 は `Blanc de Blancs Extra Brut Premier Cru` NV に解決すべき**であり、
  **同時に「公式サイトに存在しないキュヴェが canonical に実在する」＝ canonical の出所が公式外である**ことを意味する。
- **どちらに転んでも、この 1 本の解決とキュヴェ台帳の正しさが同時に決まる。**現状はどちらでもない中ぶらりん。

**⑤ 推奨される解決策（実行しない）**
1. **自動統合を禁止する。**名前の包含関係（"Blanc de Blancs" ⊂ シャルドネ 100%）で matcher に判定させない。
2. **決着は公式サイトでは付かない**（公式が古い）。取るべき一次情報は
   **①店の在庫ボトルのラベル実物**、**②生産者本人 `fred@champagne-savart.com`**、
   **③公式サイトが名指しする米国インポーター Grand Cru Selections（NY）**。
   **NY のインポーターであることは公式サイトの記載なので、照会先として正当。**
3. **`Blanc de Blancs Extra Brut Premier Cru` の canonical 登録がどの legacy ソースから来たかを遡る**
   （公式に存在しないキュヴェが入っている以上、出所の監査が先）。
4. **判定が付くまで OBP $380 は unresolved に据え置く。**fuzzy 一致で自動確定させない。

**⑥ Confidence: Medium**
同一生産者・同一村・同一品種・同一表示の一致は強い。
一方で **公式サイトが古く、canonical のほうが新しい情報を持っている**という構図が反証として効いており、
**「別キュヴェである」可能性を排除できない。誤検出の可能性を残したまま登録票に上げる。**

### 衝突ではないもの（誤検出として明示的に除外）

- **`Le Mont Benoît`（単独キュヴェ・Villers-aux-Nœuds）** と **`L'Année 2013` の構成畑 "Le Mont Benoit"**
  → **同一畑名がキュヴェ名とブレンド構成要素の両方に出るだけ。**`L'Année 2013` は canonical 未登録でもあり、**衝突ではない。**
- **`Le Mont Benoît`** と **`Le Mont des Chrétiens`** → **別の村・別の品種。名前が似ているだけ。衝突ではない。**
- **`Expression Nature`** と **`Expression Rosé Nature`** → **色違い（Blanc / Rosé）。衝突ではない**（両者とも canonical 未登録）。
- **`Le Millésime — Premier Cru Extra Brut`(2008)** と **`L'Année 2013`** → **`L'Année 2013` は canonical に存在しない。**
  canonical レコード同士の衝突ではないため、**§Important Cuvées C-1 の「未解決ボトルの同定問題」として扱い、
  canonical conflict には計上しない。**

---

## Sources

### 一次資料（公式サイト・2026-08-04 参照）✅

`https://champagne-savart.com/` — **`sitemap.xml` を実測（26 URL、うち 9 件は `/vins/*` の重複エイリアスで本文完全一致）。
固有 17 ページを全件取得・実測した。**（2026-08-05 JST に sitemap・HTTP ヘッダ・`/en`・エイリアスを再検証済み）

| ページ | 得た主な事実 |
|---|---|
| `/`（index） | サイト title＝**「Écueil, village classé 1er cru」**（Écueil の 1er cru 格付けの公式言明）。引用「Faire ce que tu aimes, c'est la liberté / Aimer ce que tu fais, c'est le bonheur.」— Pierre Champsaur |
| `/philosophie` | **栽培哲学（手作業・予防的手法・生態系）／醸造哲学（形づくらない）／「laboratoire de terroirs」／`#vinsidentitaires`** |
| `/vins` | **キュヴェ全 9 種の一覧**（＝公式の全量） |
| `/vins/l-annee-2013` | Écueil＋Villers-aux-Nœuds、**Les Rosets / Le Mont Benoit**、Ch40/PN60、**3 g/L**、**混醸** |
| `/vins/expression-nature` | Écueil **argilo-calcaire**、**Aillys / Chaillots derrière Moutier / Gillys**、**très vieilles vignes PN 100%**、**500L 樽・10 ヶ月シュール・リー**、**0 g/L** |
| `/vins/expression-rose-nature` | ⚠️ **上と完全同一のスペック** |
| `/vins/le-mont-benoit` | **Villers-aux-Nœuds** argilo-calcaire、PN95/Ch5、**3 g/L** |
| `/vins/le-mont-des-chretiens` | Écueil、リュー・ディ Le Mont des Chrétiens、**Chardonnay 100%**、**3 g/L** |
| `/vins/l-accomplie` | Écueil＋Villers-aux-Nœuds、PN80/Ch20、**5 g/L** |
| `/vins/l-ouverture` | **PN 100%**、**BRUT**、**7 g/L**（Terroir 欄なし） |
| `/vins/bulle-de-rose` | PN70/Ch22/**赤の PN 8%**、**BRUT**、**6 g/L**（Terroir 欄なし） |
| `/vins/les-noues` | 🔴 **「À venir...」のみ。中身ゼロ** |
| `/partenaires` | **海外 31 社**（米国＝**Grand Cru Selections（NY）** / Galaxy Wine（Oregon）、日本＝Firadis）＋**フランス国内取引先**（L'Assiette Champenoise、Les Crayères ほか） |
| `/contact` | **1 chemin de Sacy, 51500 ÉCUEIL** / `fred@champagne-savart.com` / +33 (0)3 26 84 91 60 |
| `/mentions-legales` | 法人表記「**Champagne Savart**」、制作 MKB Prod（Reims）、ホスティング PlanetHoster |
| `/photos` | サーバ側 HTML に本文なし。ギャラリー画像のみ（ファイル名に `20141209_` を含む） |
| `/actualites` | 🔴 **サーバ側 HTML に記事本文が 1 件も無い**（SNS フィード枠のみ） |

### 取得手法上の確認（教訓 2 への対応）

- ⚠️ **キュヴェ別テクニカルシート PDF は存在しない。**全 17 ページの HTML と `site.js`（実 JS・8,979 bytes）を
  grep し、**`.pdf` への参照が 1 件も無い**ことを実測。Louis Latour で使えた `/pdf/en/*.pdf` 方式は**適用不可**。
- ⚠️ **EN 版は存在しない。**ヘッダの `FR / EN` は `<span>` であって**リンクではなく**、`site.js` に言語切替処理が無い。
  `/en` は **HTTP 200 を返すが、FR のナビゲーション枠だけで本文が空**（index とも別バイト列）＝ **soft-404**。
  **英語の公式情報はゼロ。**
- ⚠️ **公式ドメインの特定に検索を 1 回だけ使用した。**返ってきたのは小売店・EC・インポーター・イベントの各ページで、
  **champagne-savart.com 以外に公式ドメインは存在しない**ことを確認した。
  **これらのスニペットに含まれる事実主張（面積・継承年・村名など）は本文に一切採用していない**
  — むしろ **§Staff Notes ⑦ で発話禁止として列挙した。**
- ⚠️ **`/actualites` は `jquery.socialfeed.js` による SNS 埋め込み枠で、サーバ側に本文が無い。**
  SNS アカウント（Instagram 等）は本バッチの「公式サイト」の範囲外として**採用していない** → Open Questions 11。

### 二次資料
**なし。本書は全面的に公式サイト `champagne-savart.com` のみに基づく。**
小売店・EC・インポーター販促文・レビュー集約サイト・まとめ記事の記述は**一切使用していない。**
（公式ドメインを特定するための検索は行ったが、**検索結果スニペットの内容は本文に一切採用していない。**）

### 保存物
`/Users/akiomatsumoto/Theseus_Phase0/research/producers/_sources/frederic-savart/`
`raw_*.html`（全 17 ページの生 HTML）／ `txt_*.txt`（抽出テキスト）／ `site.js`

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **Medium-High** | 所在地・連絡先・法人表記は公式で確定。**当主名と業態（RM/NM）が公式に無い** |
| Overview | **Medium-High** | Écueil の 1er cru 格付け、品種構成、低ドザージュ、自己規定はすべて公式 |
| History | **Low** | 🔴 **公式に沿革ページが存在しない。創業年・世代・当主交代がすべて未確認** |
| Location | **Medium-High** | 村・土壌・リュー・ディ 7 件は公式。**面積が完全に不明**、Villers-aux-Nœuds の格付けが未明言 |
| Farming | **Medium** | 公式の言明は明確だが短い。**認証の有無が「記載なし」という形でしか分からない**（＝「認証を謳っていない」ことは確度高く言える） |
| Winemaking | **Low-Medium** | **9 キュヴェ中 2 つにしか醸造記述が無い。**哲学は明快、実務数値はほぼ皆無 |
| Style | **Medium** | セパージュとドザージュの全数値から構造的に導出可能。第三者評価は無し |
| Important Cuvées | **Medium-High** | **公式 9 キュヴェのスペックを全取得。**ただし Les Noues は公式が空、OBP 未解決 2 本は公式で決着せず |
| Staff Notes | **High** | すべて上記 ✅ から構成。**⚠️ リストが本書の主成果物** |
| Canonical Conflict | **Medium** | producer 衝突は無しと確定（REGISTER.md 全読・Savart 未登場）。cuvée 候補 **CS-1 は 1 件、Medium で登録票へ**（誤検出可能性を残す） |
| **総合** | **Medium — ただし staff-usable（70% 到達）** | 現場で必要な Identity / Location / Farming / Cuvée スペック / OBP 紐付け / ⚠️ リストは揃った。**薄さの所在（沿革・面積・醸造数値）を明示し、そこを発話禁止で塞いだ**ことで、**「間違ったことを言わずに語れる」状態には到達している** |

---

## Open Questions

1. 🔴 **沿革が丸ごと空白。** 創業年・世代数・現当主の氏名と就任年・畑取得の履歴。**公式サイトに沿革ページが無い。**
   → **生産者本人（`fred@champagne-savart.com`）かインポーター Grand Cru Selections（NY）からの一次資料が要る。**
   **NY のインポーターであることは公式サイトが名指ししているので、照会先として正当。**
2. 🔴 **総面積・区画別面積・年間生産本数。** 公式に一切記載が無い。**現場で最も訊かれる数字の一つが空白。**
3. ⚠️ **canonical の subregion「Écueil & Sacy」の出所。** 公式サイトに **Sacy 村の言及は無く**、
   "Sacy" は住所の道路名（`1 chemin de Sacy`）としてのみ現れる。**Sacy に畑があるのか、住所からの誤導出か。**
   → **両方の値を消さずに残してある。**
4. **Villers-aux-Nœuds の格付け。** 公式が 1er cru と明記するのは Écueil のみ。
   Villers-aux-Nœuds 単独畑の Le Mont Benoît が Premier Cru を名乗るため実質 1er cru と導けるが、**公式の直接言明が無い。**
5. 🔴 **栽培の認証。** オーガニック / ビオディナミ / HVE / VDC のいずれについても**公式に記載も否定も無い。**
   「認証を謳っていない」ことまでは確度高く言えるが、**実際に認証を保有していないかは未確認。**
6. 🔴 **醸造の実務数値が 7 キュヴェ分欠落。** MLF・天然酵母・新樽比率・樽元・リザーヴワイン/ソレラ・
   瓶熟期間・デゴルジュマン時期・ドザージュ用リキュール・SO2 方針。
   **リストに載る 5 本すべてについて、容器と熟成の公式情報がゼロ。**
7. **第三者評価。** 公式にプレス欄・点数の掲載が無い。
8. ⚠️ **Expression Nature と Expression Rosé Nature の公式スペックが完全同一。**
   ロゼ側の造り（赤の添加かセニエか）が不明。**サイトのコピー流用の可能性が高いが判定不能。**
9. 🔴 **OBP「2008 Premier Cru Extra Brut」（$500）のキュヴェ同定。**
   canonical の `Le Millésime` 2008 と**年・表示・村構成・BLENDS 分類がすべて整合する強い候補**だが、
   **公式サイトに 2008 のページも「Le Millésime」の名称も無い**ため確定できない。
   → **fuzzy 一致で自動確定させず、review queue に残す。**
   → **決着手段: 店の在庫ボトルのラベル実物確認**が最短。
10. 🔴 **OBP「NV Premier Cru Extra Brut」（$380・BLANC DE BLANCS 欄）のキュヴェ同定。**
    **公式サイトに Blanc de Blancs キュヴェが存在しない。**公式の Chardonnay 100% は
    `Le Mont des Chrétiens`（ただし canonical では 2020 ヴィンテージで NV ではない）のみ。
    → **公式サイトが 2017 年以降未更新である可能性が、この空白の最有力説明。**
    → **決着手段: ラベル実物確認、または Grand Cru Selections（NY）への照会。**
    → 🔴 **これは同時に canonical の構造問題でもある。§Canonical Conflict CS-1 を見よ。
      `Blanc de Blancs Extra Brut Premier Cru` と `Mont des Chrétiens` が同一キュヴェの二重登録である可能性があり、
      REGISTER.md への追記が必要（当方は REGISTER.md を編集していない）。**
11. **公式 SNS を一次資料として採用するか。** `/actualites` は SNS フィード枠のみで、
    **サイト本体は 2017 年で止まっている疑いが強い。**現況（当主・新キュヴェ・認証）を取るには
    SNS か本人照会が必要だが、**本バッチのソース規律では未採用とした。Akio の判断が要る。**
12. **canonical に未登録の公式キュヴェ 3 件**（`L'Année 2013` / `Expression Nature` / `Expression Rosé Nature`）を
    登録するか。**OBP には 1 本も載っていないため優先度は低い。**
