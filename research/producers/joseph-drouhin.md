# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:joseph-drouhin` / `producer:domaine-drouhin-vaudon` / `producer:domaine-drouhin-oregon`
> はいずれも一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト drouhin.com で確認**（一次資料。**公式配布の per-vintage テクニカルシート PDF を含む**）
> `📄` 単一の非公式資料のみ（**本書では使用していない**）
> `⚠️` **出典間で食い違い。両方を残す**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.drouhin.com/`（FR / EN 両ロケール）**
> 走査元: 公式 `sitemap.xml`（**全 438 URL。うち `en_US` 211 URL を全件確認**）
> **`/en_US/wine/<slug>/<millésime>` 形式のワインページが 163 件**存在し、
> **各ページに `/en_US/winepdf/<slug>/<millésime>` の公式 PDF が紐づく。**
>
> 🔴🔴 **このドシエは 1 生産者ではなく、canonical 上の 3 生産者・OBP 10 本をカバーする。**
> **`Joseph Drouhin`（7 本）＋ `Drouhin-Vaudon`（2 本）＋ `Drouhin`＝Oregon（1 本）。**
> **メニューは 3 つの名前で印字しているが、公式サイトはすべて `Maison Joseph Drouhin` の下にある。**
>
> 🔴 **本ドシエ最大の実務的価値は、公式が各ワインに `Supply:` 欄を設けて
> 「自社畑か、購入ブドウ・果汁か」を明記していることである。** → §Important Cuvées

---

## Identity

| | |
|---|---|
| **Canonical Name** | Joseph Drouhin |
| **公式表記** | **Maison Joseph Drouhin** ✅（サイト全体の `<title>` と法定表示） |
| **Aliases** | ❓ canonical `aliases` は**空**。**OBP が印字する `Joseph Drouhin` / `Drouhin-Vaudon` / `Drouhin` のいずれも未登録** |
| **創業** | ✅ **1880 年**。公式のメニュー項目は **`A Family since 1880`** |
| **世代** | ✅ **4 世代**（「A Heritage and Philosophy Inherited for 4 Generations」） |
| **アペラシオン数** | ✅ **約 90**（「This quest for excellence extends across nearly 90 appellations」） |
| **品種** | ✅ **Chardonnay と Pinot Noir のみ** |
| **所有面積** | ✅ 🔴 **Côte d'Or 53 ha ／ Chablis 40 ha ／ Oregon 100 ha**（`/presentation/pioneers-in-oregon`） |
| ⚠️ **面積の別記述** | ⚠️ **各ワインページの Viticulture 欄は「its 100-hectare (247 acres) estate」と書く。** Côte d'Or 53 ＋ Chablis 40 ＝ **93 ha** であり一致しない。**両方残す** → Open Questions 3 |
| **テイスティングノートの著者** | ✅ **Véronique Boss-Drouhin**（全ワインページの `Tasting by …`） |
| **Oregon 部門** | ✅ **Domaine Drouhin Oregon（DDO）** — **1987 年 7 月設立。モットー `French Soul, Oregon Soil`** |
| **Oregon 第 2 部門** | ✅ **Roserock Drouhin Oregon** — **2013 年取得。Eola-Amity Hills。112 ha（うち畑 54 ha）** |
| **法人** | ✅ **Maison Joseph Drouhin**（法定表示。サイトは Vinium との協働で制作） |
| canonical id | `producer:joseph-drouhin` ／ `producer:domaine-drouhin-vaudon` ／ `producer:domaine-drouhin-oregon` |
| canonical entity confidence | **すべて 0.2**（`aliases` 空。`domaine-drouhin-oregon` のみ `facts.subregion = Willamette Valley`） |

---

## Overview

✅ **1880 年創業、4 世代のボーヌのメゾン。ブルゴーニュの約 90 アペラシオンを、
シャルドネとピノ・ノワールの 2 品種だけで手がける。**

🔴 ✅ **公式が最も強く打ち出しているのは農法である。**
「**時とともに、経験と呼ぶものを通じて、Maison Joseph Drouhin は自然に
有機の、さらにはビオディナミのアプローチを選び取った —— 80 年代末から。**」
⚠️ **一方、各ワインページの定型文はこう書く** —
「**100 ヘクタールの自社畑全体で、Maison Joseph Drouhin は 1980 年代末から有機栽培を、
1990 年代からビオディナミ栽培を採用してきた。**」
→ 🔴 **ビオディナミの開始時期が「80 年代末」と「1990 年代」で食い違う。両方残す。** → §Farming

✅ **公式のモットーは「natural responses to natural challenges（自然の問いには自然の答えを）」。**

🔴 ✅ **もう一つの核心は「自社畑と購入ブドウの明示」である。**
**公式は各ワインの Winemaking 欄の冒頭に `Supply:` を置き、3 通りに書き分けている。**

| `Supply:` の記述 | 意味 |
|---|---|
| **（記載なし）** | 🔍 **自社畑のみ**と読める（Musigny / Montrachet Marquis de Laguiche / Chablis GC Vaudésir がこれ） |
| **`from grapes harvested on some parcels of the Drouhin Family Properties as well as from grapes and musts purchased from supply partners`** | **自社畑＋購入の混成** |
| **`from grapes and musts purchased from supply partners according to rigorous specifications`** | 🔴 **購入のみ**（Puligny-Montrachet / Folatières がこれ） |

→ 🔴 **OBP 掲載 10 本のうち、少なくとも 2 本は「購入ブドウのみ」と公式が明記している。**
**これはフロアで最も間違えやすい点である。** → §Staff Notes ⚠️ ①

✅ **スタイルの自己規定** —
「**エレガンスと調和がこのスタイルの指針である。**
**最初の取得が Chambolle-Musigny 村の近くだったのは偶然ではない —— いや、もはや偶然ではない。**」

🔍 **THÉSEUS における状態。canonical に 3 生産者・3 キュヴェ・3 ヴィンテージのみ。
OBP 掲載 10 本のうち解決済みは 2 本。**

---

## History

| 年 | 出来事 ✅ |
|---|---|
| **1880** | **Maison Joseph Drouhin 創業**（公式の自称は `A Family since 1880`） |
| **1776** | （関連）**Montrachet の Marquis de Laguiche 家所有が始まる。以後同家の手にある** |
| **1947** | 🔴 **Drouhin 家が Marquis de Laguiche の Montrachet の栽培と醸造を担うようになる。以後その名声を世界に広めた** |
| **1960 年代** | 🔴 **Robert Drouhin がシャブリの潜在力を見出す。** 「**60 年代、シャブリの畑がすべて見捨てられていたとき、Robert Drouhin はこの地域の潜在力を認めた。一世紀前にフィロキセラで荒廃していた。彼はこの地域の再生に取りかかった最初のブルゴーニュの propriétaire の一人であった。**」 |
| **1961** | ✅ **Robert Drouhin が「オレゴンで果たす役割がある」と確信し始める** |
| **1980 年代末** | ✅ **有機栽培の採用**（⚠️ ビオディナミも「80 年代末から」とする記述と「1990 年代から」とする記述が併存） |
| **1987 年 7 月** | 🔴 ✅ **Robert Drouhin と、醸造学を修めたばかりの娘 Véronique Drouhin が Dundee Hills（Willamette Valley）に土地を購入。`Domaine Drouhin Oregon（DDO）` 誕生。モットー `French Soul, Oregon Soil`** |
| **1988** | ✅ **DDO 最初のワイン = `Pinot Noir`（＝ OBP 掲載の Dundee Hills Pinot Noir の系譜）** |
| **1989** | ✅ **丘の頂に重力式（gravity-flow）ワイナリーが建つ** |
| **1992 頃** | ✅ **ピノ・ノワールの選抜キュヴェ `Laurène` をリリース**（Véronique の長女の名。公式は「3 年後」と記す） |
| **1996** | ✅ **自社畑シャルドネの初ヴィンテージ** |
| **1999 頃** | ✅ **ピノ・ノワールの新たな選抜に `Louise`（次女の名）**（公式は「3 ヴィンテージ後」と記す） |
| **2004** | ✅ **シャルドネのキュヴェに三男 `Arthur` の名** |
| **2013** | 🔴 ✅ **`Roserock Vineyards` 取得（Eola-Amity Hills）。112 ha、うち畑 54 ha。主にピノ・ノワール** |

🔴 ✅ **公式が語る 2 つのオレゴンのテロワールの対比** —
「**われわれを興奮させるのは、いずれも火山起源の 2 つの異なるテロワールを持ち、
Roserock のほうがやや冷涼な微気候であることだ。**」
「**Dundee Hills のワインは魅力的で絹のよう、Eola-Amity Hills のそれはより骨格があり躍動的である。
この差は、ブルゴーニュにおける Chambolle-Musigny と Gevrey-Chambertin の差になぞらえられる。**」

---

## Location

| | |
|---|---|
| **Country** | France ＋ **USA** ✅ |
| **本拠** | **Beaune**（Côte d'Or） ✅ |
| 🔴 **所有面積** | ✅ **Côte d'Or 53 ha ／ Chablis 40 ha ／ Oregon 100 ha** |
| **オレゴンの AVA** | ✅ **Dundee Hills**（DDO）と **Eola-Amity Hills**（Roserock）。いずれも Willamette Valley 内。**両者とも火山起源** |
| ⚠️ **面積の不一致** | ⚠️ **ワインページ定型文の「100-hectare estate」対 内訳合計 93 ha** |

### 🔴 公式が書く畑の性格（OBP 掲載分。**各ワインページの `Site` / `Soil` 欄**）

- **Musigny** — 「**Clos Vougeot を見下ろす白亜のテラスに位置する。Chambolle の combe と Orveaux の combe という
  2 つの小さな谷の間にある。**」土壌は「**緩やかな傾斜、真東向き。褐色で白亜質、いくらか小石が混じり、粘土は多くない。**」
  🔴 由来: 「**この地でブドウ栽培の真の先駆者だったのは、ガロ・ローマ時代にこの丘に畑を持っていた Mucius という人物である。
  Musigny が今の地位に上ったのは、実際には中世初期、修道士たちの助けによる。**」
- **Chambolle-Musigny 1er Cru** — 「**名高い Chambolle-Musigny の畑の中心、良好な東向き。**」
  基盤の石灰岩は**ジュラ紀起源**で「**ピノ・ノワールに理想的**」。
  由来: 「**村名 Chambolle はおそらくケルト語の `cambola`（小川の近くの肥沃な土地、良質な土壌）に由来する。**」
- **Montrachet（Marquis de Laguiche）** — 「**生産コミューンは Puligny-Montrachet と Chassagne-Montrachet。
  Marquis de Laguiche の所有地は全体が Puligny 側にある。極めて緩やかな傾斜と、見事な南東向き。**」
  土壌は「**赤褐色の土に、白く磨かれた石灰岩の小石が散らばる。Montrachet の `rachet` は、
  何も育たない不毛の土地を意味する。**」
- **Puligny-Montrachet** — 「**Puligny はローマ帝国期に Pullius なる人物のものであった可能性がある。
  その所領は `Pulliniacus` と呼ばれ、そこから Puligny の名が派生した。**」
  土壌は「**石灰岩。黄土色の土と小さな小石の混合。**」
- **Puligny-Montrachet 1er Cru Les Folatières** — 「**Premier Cru の中でも Les Folatières は最も名高いものの一つで、
  斜面中腹の中心的な位置を占める。**」
  由来: 「**`Folatières` の名はフランス語の `feu follet`（鬼火）に由来するかもしれない。
  民間の想像では、夏の暖かい夜に近くの森や下の谷から立ち上るのが見えたという。**」
  土壌は「**石灰岩。極めて白亜質で石が多く、大部分は実際には石灰岩の礫である。**」
- **Côte de Beaune（白・赤）** — 🔴 「**生産コミューンは Beaune。ボーヌ市を見下ろす丘の上。
  アペラシオン `Côte de Beaune` は、ボーヌ市を見下ろす丘の頂にある畑のワインに与えられる。**
  **`Côte de Beaune-Villages` と混同してはならない。後者は Côte de Beaune のいくつかの村（ただしボーヌ自身は除く）の
  ワインをブレンドしたものに与えられ、赤ワインにのみ用いられる。**」
  白の土壌は「**粘土と石灰岩。軽い土壌がワインに大きな繊細さを与える。**」
  赤の土壌は「**白亜質であまり深くない。傾斜は急になりうる。向きは南／南東。**」
- **Chablis（Vaudésir / Premier Cru）** — 「**キンメリジャンの石灰岩は、白っぽいモルタルのようなものに埋め込まれた
  無数の微小な海生化石を含む。それは数億年前、かつて海の底だったのかもしれない。
  この海の起源がシャブリのワインに固有の風味を与える。**」
  **Vaudésir** は 🔴「**その起伏はブルゴーニュに類例がない。円い形と急斜面は古代の円形劇場を思わせる。
  向きは 2 つ —— 北側区画は真南、南側区画は南西。シャブリの 7 つのグラン・クリュの中で最大級。**」
  由来は「**畑を真ん中で切る `chemin des vaudésirs`（ヴォデジールの道）から。**」

---

## Farming

| | 公式の記述 ✅ |
|---|---|
| **有機** | 🔴 **1980 年代末から** |
| **ビオディナミ** | ⚠️ 🔴 **「1990 年代から」（ワインページ定型文）／「80 年代末から」（`/presentation/in-pursuit-of-excellence`）。両方残す** |
| **モットー** | **「natural responses to natural challenges」（自然の問いには自然の答えを）** |
| 🔴 **具体的実践** | **馬による耕起（horse ploughing）／被覆作物（cover cropping）／自然堆肥（natural composting）** |
| 🔴 **ビオディナミの手当て** | **植物の浸出液由来の調剤と天敵（natural predators）を、専用のカレンダーに従って用いる** |
| 🔴 **植密度** | **最大 12,500 本 / ha**（「high-density planting – up to 12,500 vines per hectare」） |
| **収量** | **意図的に低収量**（「Our deliberately low production yields」） |
| **根** | **深い根系を優先する** |
| **収穫** | **手摘み。小さな有孔クレート（open-work / perforated crates）で果実の健全性を保つ** |

### ✅ 公式が公開する栽培の 1 年（`/passion-2/our-vines-a-constant-attention-to-details`）

| 時期 | 作業 |
|---|---|
| **11 月** | **土壌を活性化させる有機資材を散布** |
| **11 月〜2 月** | **丁寧に、穏やかに剪定** |
| **4 月** | **耕起。先に散布した有機資材を鋤き込む。萌芽の開始** |
| **初夏** | **誘引（tying-up and down）と摘芯（trimming）** |
| **7〜8 月** | **グリーンハーヴェストと除葉。必要なら植物由来の調剤で防除。** **定期的なサンプリングで収穫日を決定** |

🔴 ✅ **Oregon 側は別の認証を持つ** —
「**Domaine Drouhin Oregon は持続可能栽培の `Low Input Viticulture Environment`（LIVE）認証を受けている。**」

❓ **公式に無い農業情報**: 認証機関名（仏側。**有機 / ビオディナミの認証名が一切書かれていない**）／
区画ごとの ha ／ 実収量の数値 ／ 樹齢。

---

## Winemaking

### ✅ メゾン全体の方針（`/presentation/in-pursuit-of-excellence`）

「**蔵では、この誠実さへの傾倒が、各テロワールに応じた醸造の自然なリズムを優先することで保たれる ——
除梗、垂直または水平のプレス、重力による清澄、野生酵母、ステンレスまたはオーク樽…。**」
🔴 「**樽材の選定では、注意深く選ばれ 3 年間自然乾燥させた樫を用いてタンニンを洗練させる。**」

### 🔴 公式のワイン別テクニカル（**OBP 掲載 10 本。すべて公式ワインページ ＋ 公式 PDF より**）

| ワイン | VT | 🔴 `Supply` | 発酵・醸造 | **新樽 %** | **熟成** | 飲み頃 / 潜在 | 供出温度 |
|---|---|---|---|---|---|---|---|
| **Chablis 1er Cru**（Drouhin-Vaudon） | 2022 | **自社＋購入** | 全房を空圧式で緩慢に圧搾。**ステンレス槽で発酵** | — | 🔴 **ステンレス槽 8–10 か月** | 3–8 / 10 年 | 12–13 °C |
| **Chablis GC Vaudésir**（Drouhin-Vaudon） | 2023 | **記載なし（自社）** | 全房を空圧式で緩慢に圧搾。**使用済み樽へ移す** | 🔴 **0%** | 🔴 **500 L のオーク樽（新樽なし）で AF＋熟成 12–15 か月** | 4–10 / 15 年 | 13 °C |
| **Côte de Beaune 白** | 2023 | **自社＋購入** | 空圧式で緩慢に圧搾。澱下げ後、樽へ | **10–15%** | **樽で AF＋MLF＋熟成 12–14 か月** | 4–6 / 8 年 | 13 °C |
| **Côte de Beaune 赤** | 2023 | ❓ 本調査で未取得 | ❓ | ❓ | ❓ | 5–8 / 10 年 | 16 °C |
| **Puligny-Montrachet** | 2020 | 🔴 **購入のみ** | 同上 | **約 20%** | **樽で AF＋MLF＋熟成 14–16 か月** | 6–15 / 15 年 | 13 °C |
| **Puligny 1er Cru Les Folatières** | 2023 | 🔴 **購入のみ** | 同上 | **20–25%** | **樽で AF＋MLF＋熟成 16–18 か月** | 8–20 / 20 年 | 13 °C |
| **Montrachet Marquis de Laguiche GC** | 2021 | **記載なし（自社管理）** | 空圧式で緩慢に圧搾。最終プレス果汁をフリーランと分離 | **約 30%** | **樽で AF＋MLF＋熟成 18–21 か月** | 8–15 / 20 年 | 14–15 °C |
| **Chambolle-Musigny 1er Cru** | 2023 | **自社＋購入** | 🔴 **全房 20–50%（ヴィンテージによる）。小型開放槽で 2–3 週間の発酵と醸し。ピジャージュとルモンタージュ。野生酵母。垂直プレス** | **25%** | **樽 14–18 か月** | 10–20 / 25 年 | 16 °C |
| **Musigny GC** | 2021 | **記載なし（自社）** | 同上 | **30%** | **樽 16–20 か月** | 15–20 / 30 年 | 16–18 °C |
| **DDO Dundee Hills Pinot Noir** | ⚠️ 2021 で確認 | **自社畑のみ**（「harvested only on the estate's plots in the Dundee Hills」） | 🔴 **25 ポンドのクレートで手摘み、手選果、除梗。4 層の重力式ワイナリー。発酵は長く慎重に。11 月までに全量が樽に入る** | ❓ | ❓ | 1–6 / 10 年 | 16 °C |

✅ **樽材の産地**（仏側の全ワインに共通の記述）: **`oak grown in French high forest`（フランスの高林の樫）**。
✅ **DDO の樽**: **「ブルゴーニュで特注し、フランス最良の森の樫を用いる」**。

✅ **全ワインに共通する締めの定型文** —
「**熟成の全期間を通じて、決定は注意深いテイスティング評価の後にのみ下される。
得られたデータは技術分析によって補完される。他の全ての Joseph Drouhin のワインと同じく、
テロワールの真の表現とヴィンテージの性格に絶対の優先が置かれる。**」

🔴 ⚠️ **公式 PDF テクニカルシートを 3 本取得したが、内容は Web ページと同一であり、
アルコール度数・pH・総酸・収穫日・生産量はどのワインについても記載が無い。**
→ §Staff Notes ⚠️ ⑦

---

## Style

### ✅ メゾンのスタイル自己規定

「**エレガンスと調和がこのスタイルの指針である。若いうちに飲めば果実味豊かで美味しく、
さらに忍耐を重ねれば、豪奢で言葉にしがたいほど複雑な性格へと変化する。**」

### ✅ 公式テイスティングノート（**すべて Véronique Boss-Drouhin による**。OBP 掲載分）

| ワイン | 公式ノート（抜粋） |
|---|---|
| **Montrachet Marquis de Laguiche** | 🔴 「**真正の傑作！ このワインは、他のすべてのブルゴーニュを測るべき物差しと見なされるべきである。**色は見事な黄金の光沢。香りには無数のアロマ —— スズラン、桃の花、エキゾチックフルーツ、蜜、焼いたアーモンド、時にはエキゾチックな木の香りまで。口中では調和のとれた丸みが構造を支配し、決して重さを与えない。余韻は例外的に長く、全体の繊細さを高める。**感覚の輝かしい交響曲！**」 |
| **Musigny** | 🔴 「**例外的かつ唯一無二のテロワールの反映。Chambolle-Musigny のごく一部から生まれるグラン・クリュ。ピノ・ノワールのエレガンスの最も美しい表現としばしば言われる。**香りは強く複雑で、信じがたいほど調和している。タンニンは官能的で繊細、しかし極めて生き生きしている。若いうちから美味だが、優雅に熟成し、繊細で洗練された香りを開く。」 |
| **Chambolle-Musigny 1er Cru** | 「**繊細なレースと絹**——このワインに最もよく結びつけられる言葉。明るく強い色調、スミレ・ブラックチェリー・湿った土を思わせる複雑な香り。ヴィンテージによってはトリュフとジビエの調子も。洗練されたタンニンが口中を覆う。テクスチャーと酸の良好な均衡。余韻は長く、チェリーと砂糖漬けの果実の調子。」 |
| **Puligny 1er Cru Les Folatières** | 「見事な調和がこの貴重なワインを定義する。黄金で明るい色調。**Puligny の複雑で個性的な香り —— 蜜、スイカズラ、フレッシュなアーモンド。**熟成につれ乾果と香辛料へ変化する。口中は清涼感とビロードの質感の均衡が非常に良い。**強固な背骨**さえ感じられる。余韻は例外的に長く、洗練された花の調子が貫く。」 |
| **Puligny-Montrachet** | 「大きな繊細さを持つ、気品ある優雅なワイン。純粋で明るい色調、白金の微かな輝き。香りは**花咲く木々と白桃のような白い果肉の果実**。熟成につれアーモンドと軽く焼いた乾果へ。口中は**みずみずしい絹の感触**。」 |
| **Chablis GC Vaudésir** | 「**しばしば単独でアペリティフとして飲まれる絶妙なワイン。**純粋で澄んだ色調、微かな緑の気配。香りは花と果実（レモンの風味）、時にコリアンダーの香辛料の調子。口中は調和した香りが性格と優雅さをもたらす。**グラン・クリュの規模と、キンメリジャン土壌由来の軽い塩の調子**が明らか。」 |
| **Chablis 1er Cru** | 「**シャブリらしい、辛口で切れのあるワイン。**輝く黄緑の色調。香りはレモン、柑橘、アスパラガス…。口中は最初の一口が明晰でフレッシュ、良い質感。余韻は長く、果実とミネラルの風味。熟成が進むとやや蜜を帯びる。」 |
| **Côte de Beaune 白** | 「実に美味で調和のとれたワイン。淡い黄金色、非常に明るい。香りは**蜜、アーモンド、レモングラス**。熟成につれ**焼いたヘーゼルナッツとアーモンド**の強い風味。」 |
| **Côte de Beaune 赤** | 「真の喜びと大きな調和！ 美しい紫色。香りは**イチゴとレッドカラント**の繊細で果実的な調子。口中のタンニンは洗練され、良い丸みを与える。優雅な余韻。」 |
| **DDO Dundee Hills Pinot Noir** | 「若々しく明るい。香りは**ブラックチェリーと熟したサワーチェリー**が溢れ、**乾いたスミレと軽く焙煎したコーヒー豆**の気配。口中は**フレッシュなラズベリー、クランベリー、そして明らかに土のような感触**。愛らしく、躍動的で、優雅。」 |

### ✅ 公式ヴィンテージ評（OBP 該当分）

| VT | 公式の記述 |
|---|---|
| **2020**（白） | 「**非常に良い収穫。蜜と果実の香りに乾果の調子が混じる。酸のレベルが高く、清涼感の印象を高める。**」 |
| **2021** | 🔴 「**2021 の気まぐれは収量に大きく影響し、ブルゴーニュ史上最小級の収穫となった。**<br>**白**は以前のヴィンテージほど豊満ではないが、過度な華美なしに均衡がとれ美しい香りを持つ。<br>**赤**は調和がとれて優雅、アルコール濃度は以前より低い。**果実味と多くの清涼感を示す、むしろブルギニヨン的なスタイルのヴィンテージ。**」 |
| **2022**（白） | 「**良好な成熟。とりわけ香り高い白。柑橘と熟した果実に繊細な花の香り、しばしばやや香辛料的なペストリーの調子を伴う。口中は柔らかく肉厚で、強い質感に支えられる。心地よい丸みと豊かな余韻。均衡がとれ、優れた熟成能力を示す。**」 |
| **2023** | 🔴 「**2023 はブルゴーニュで最も暑い年の一つとして際立ち、2022 をも上回る。**<br>**白**: ブドウは完璧な成熟で収穫された。極めて香り高く、黄色い果実に花の気配。口中は豊満でフルボディ。寛大さ・清涼感・繊細さを併せ持ち、**気候がテロワールを圧倒せずに高めた**。<br>**赤**: **量と質の両面で寛大なヴィンテージ**で、ブルゴーニュ全域で安定した収量。熟した赤と黒のベリーの風味。**優れた成熟と、滑らかで長く複雑な口中。高品質のヴィンテージ。**」 |

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 10 本。解決済みは 2 本のみ**）

| # | OBP 印字 | セクション | VT | 価格 | ✅ **公式の正式名** | canonical 状態 🔍 |
|---|---|---|---|---|---|---|
| 1 | **Drouhin-Vaudon** \| Chablis Premier Cru | WHITE | 2022 | $175 | **Chablis Premier Cru**（**Roncières / Mont de Milieu / Montée de Tonnerre / Moireins の混成**） | 🔴 **キュヴェ不在**。canonical にあるのは **`Chablis Premier Cru Montmains`** で**別のワイン** |
| 2 | **Drouhin-Vaudon** \| 'Vaudésir,' Chablis Grand Cru | WHITE | 2023 | $400 | **Chablis Grand Cru Vaudésir** | 🔴 **キュヴェ不在** |
| 3 | Joseph Drouhin \| Côte de Beaune | **WHITE** | 2023 | $240 | 🔴 **Côte de Beaune Blanc** | 🔴 **キュヴェ不在** |
| 4 | Joseph Drouhin \| Puligny-Montrachet | WHITE | 2020 | $395 | **Puligny-Montrachet** | 🔴 **キュヴェ不在** |
| 5 | Joseph Drouhin \| 'Les Folatières,' Puligny-Montrachet 1er Cru | WHITE | 2023 | $665 | **Puligny-Montrachet Premier Cru Les Folatières** | 🔴 **キュヴェ不在** |
| 6 | Joseph Drouhin \| 'Marquis de Laguiche,' Montrachet Grand Cru | WHITE | 2021 | $4,000 | **Montrachet Marquis de Laguiche Grand Cru** | ✅ `exact` |
| 7 | Joseph Drouhin \| Côte de Beaune | **RED** | 2023 | $240 | 🔴 **Côte de Beaune Rouge** | 🔴 **キュヴェ不在** |
| 8 | Joseph Drouhin \| Chambolle-Musigny Premier Cru | RED | 2023 | $580 | **Chambolle-Musigny Premier Cru** | 🔴 **キュヴェ不在** |
| 9 | Joseph Drouhin \| Musigny Grand Cru | RED | 2021 | $5,865 | **Musigny Grand Cru** | ✅ `exact` |
| 10 | **Drouhin** \| Dundee Hills Pinot Noir | US / WILLAMETTE | 2024 | $175 | **Domaine Drouhin Oregon, Pinot Noir Dundee Hills** | 🔴 **`producer_state` すら `unresolved`**。canonical に `producer:domaine-drouhin-oregon` は**在る**が、**`Drouhin` という alias が無い** |

### 🔴🔴 `Côte de Beaune` が 2 行あるのは誤りではない。**白と赤の 2 本である**

**OBP は `Joseph Drouhin | Côte de Beaune | 2023 | $240` を 2 行印字している。**
**片方は `FRANCE | WHITE > BURGUNDY`、もう片方は `FRANCE | RED > BURGUNDY`。**
**公式にも `Côte de Beaune Blanc` と `Côte de Beaune Rouge` が別のワインとして存在する。**
🔴 **したがって重複行ではない。同名・同価格・同ヴィンテージの別ワインである。**

🔴 ✅ **さらに公式は両方について「格下げ」の事実を明記している。**
- **白**: 「**Côte de Beaune にある Joseph Drouhin の所有地と、
  名高い `Clos des Mouches` の若木から格下げされたワインから来る。**」
- **赤**: 「**Joseph Drouhin の所有地の樹と、`Clos des Mouches` およびボーヌの他の Premier Cru の
  若木を格下げしたものから来る**（ボーヌのワインは Côte de Beaune へ格下げできる）。」

### 🔴 `Chambolle-Musigny Premier Cru` の中身（公式が区画名を明記している）✅

「**Joseph Drouhin は複数の Premier Cru 区画を所有している。それらは小さすぎるため、
これらの Premier Cru の畑（`Noirots`, `Hauts Doix`, `Borniques`, `Plantes`, `Combottes`）は
まとめて収穫・醸造される。**
**したがってこのワインの名は `Chambolle-Musigny Premier Cru` である
（この "cuvée" の構成要素がすべて Premiers Crus であるため）。**」

### 🔴 `Montrachet Marquis de Laguiche` の権利関係（公式）✅

「**この所有地（2.06 ヘクタール ＝ 5.09 エーカー）は実際に Montrachet の畑の中で最大の区画であり、
1776 年以来 Laguiche 家の手にある。**
**Drouhin 家がその栽培と醸造を担い、1947 年以来その世界的な名声を広め、守ってきた。**」

### 🔴 canonical の `Chablis Premier Cru Montmains` は OBP と別物である（**マッチャは正しい**）

canonical には **`cuvee:domaine-drouhin-vaudon-chablis-premier-cru-montmains`（vintage 2022）** が在り、
**OBP の `Drouhin-Vaudon | Chablis Premier Cru | 2022` と年も生産者も一致する。**
**しかしマッチャはこれを `unresolved` にした。**
🔴 ✅ **これは正しい判断である。**
**公式には `Chablis Premier Cru`（Roncières / Mont de Milieu / Montée de Tonnerre / Moireins の混成）と
`Chablis Premier Cru Montmains` の 2 つが別のワインとして存在し、
しかも公式の混成キュヴェに Montmains は含まれていない。**
**「同じ生産者・同じ年・似た名前」を自動で結ばなかったことで、実体の取り違えを回避している。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 1880 年創業、4 世代のボーヌのメゾン。約 90 のアペラシオンを、シャルドネとピノ・ノワールだけで。**
「**1880 年創業、4 代続くボーヌのメゾン**です。**約 90 のアペラシオン**を手がけますが、
**品種はシャルドネとピノ・ノワールの 2 つだけ**。
**所有はコート・ドールに 53 ヘクタール、シャブリに 40 ヘクタール、そしてオレゴンに 100 ヘクタール**です。
**1980 年代末から有機、その後ビオディナミ**。**馬耕・被覆作物・自然堆肥**を公式に挙げ、
**植密度は最大 1 ヘクタールあたり 12,500 本**とのことです。」

**② 「自社畑か、買いブドウか」を造り手自身が 1 本ずつ公表している。**
「ドルーアンは**各ワインの技術情報に `Supply`（供給）という欄**を設けていて、
**『自社畑のみ』『自社畑＋購入』『購入のみ』を明記**しています。
たとえば**ムジニーとモンラッシェ、シャブリのヴォデジールには購入の記載がありません**が、
**ピュリニー・モンラッシェとフォラティエールは『パートナーから購入したブドウと果汁』と明記**されています。
**どちらが上ということではなく、造り手が正直に開示している**という点が特徴です。」

**③ リストの `Côte de Beaune` 2 本は白と赤。どちらもクロ・デ・ムーシュの若木を含む。**
「**同じ名前・同じ値段で 2 行ありますが、片方が白、片方が赤**です。
**どちらもボーヌ市を見下ろす丘の上のアペラシオン**で、
**造り手の畑に加えて、名高い `クロ・デ・ムーシュ` の若木を格下げしたものが入っている**と公式に書かれています。
**赤にはさらにボーヌの他のプルミエ・クリュの若木も**入ります。
なお **`コート・ド・ボーヌ・ヴィラージュ` とは別のアペラシオン**で、そちらは赤専用です。」

### 追加で使える一手

- **Montrachet Marquis de Laguiche（$4,000）**: 「**モンラッシェの中で最大の区画、2.06 ヘクタール**です。
  **1776 年からラギッシュ侯爵家の所有**で、**1947 年からドルーアン家が栽培と醸造を担っています。**
  区画は**全体がピュリニー側**。**新樽 30%、樽で 18〜21 か月**。
  造り手のテイスティングノートは『**他のすべてのブルゴーニュを測るべき物差し**』という言葉で始まります。」
- **Musigny（$5,865）**: 「**クロ・ヴジョを見下ろす白亜のテラス**、**シャンボールとオルヴォーという 2 つのコンブの間**です。
  **全房を 20〜50%、小型の開放槽で 2〜3 週間、野生酵母、垂直プレス。新樽 30%、16〜20 か月。**
  造り手は飲み頃を**収穫から 15〜20 年、ポテンシャル 30 年**としています。」
- **Chambolle-Musigny 1er Cru（$580）**: 「**単一の畑ではありません。**
  **ノワロ、オー・ドワ、ボルニック、プラント、コンボットという複数のプルミエ・クリュ区画**を、
  **小さすぎるので一緒に収穫・醸造している**と公式に明記されています。
  **構成要素が全てプルミエ・クリュなので、名前もプルミエ・クリュ**です。」
- **Chablis GC Vaudésir（$400）**: 🔴 「**新樽はゼロ**です。**500 リットルの使用済み樽で 12〜15 か月。**
  畑は『**古代の円形劇場を思わせる円い形と急斜面。ブルゴーニュに類例がない**』と造り手が書いています。」
- **Dundee Hills Pinot Noir（$175）**: 「**ドルーアン家がオレゴンに入ったのは 1987 年 7 月**、
  モットーは『**French Soul, Oregon Soil**』。**最初のピノ・ノワールが 1988 年。**
  **1989 年に丘の頂に重力式のワイナリー**を建てました。
  このワインは**ダンディー・ヒルズの自社畑のみ**で、**LIVE という持続可能栽培の認証**を受けています。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／公式が食い違っている**）

1. 🔴 ⚠️ **「すべて自社畑です」と言わない。**
   **公式は `Puligny-Montrachet` と `Puligny-Montrachet 1er Cru Les Folatières` について
   「パートナーから購入したブドウと果汁から造られる」と明記している。**
   **`Chablis 1er Cru` `Côte de Beaune 白` `Chambolle-Musigny 1er Cru` は「自社畑＋購入」。**
   **リスト 10 本のうち、公式に自社畑と読めるのは Montrachet / Musigny / Chablis GC Vaudésir /
   Dundee Hills の 4 本だけである。**
2. 🔴 ⚠️ **`Côte de Beaune` の 2 行を「メニューの重複」と言わない。白と赤の別ワインである。**
3. 🔴 ⚠️ **ビオディナミの開始年を断定しない。**
   **公式内で「1990 年代から」と「80 年代末から」が併存している。**
   言うなら「**1980 年代末から有機、ほどなくビオディナミへ**」まで。
4. ⚠️ **有機・ビオディナミの「認証」を言わない。**
   **公式は実践を詳しく書くが、仏側について認証機関名・認証名を一切書いていない。**
   **認証名を出せるのは Oregon の `LIVE` だけである。**
5. ⚠️ **総面積を「100 ヘクタール」と一言で言わない。**
   **公式は「Côte d'Or 53 ／ Chablis 40 ／ Oregon 100」と書く一方、
   ワインページの定型文は仏側を「100-hectare estate」と書く。53 ＋ 40 ＝ 93 で一致しない。**
6. ⚠️ **`Chablis Premier Cru` を `Montmains` と言わない。**
   **公式の `Chablis Premier Cru` は Roncières / Mont de Milieu / Montée de Tonnerre / Moireins の混成であり、
   `Montmains` は別に存在する別のワインである。**
7. 🔴 ⚠️ **分析値を言わない。** **公式の PDF テクニカルシートを 3 本取得したが、
   アルコール・pH・総酸・収穫日・生産量はどのワインにも記載が無い。**
   **公式が数値として出しているのは、供出温度・飲み頃年数・新樽比率・熟成月数だけ。**
8. ⚠️ **`Clos des Mouches` そのものを注いでいると言わない。**
   **Côte de Beaune に入るのは「若木からの格下げ分」である。**
9. ⚠️ **第三者点数を言わない。** **公式サイトにも PDF にも点数の掲載が無い。**
10. ⚠️ **`Drouhin-Vaudon` をシャブリの独立ドメーヌのように語らない。**
    **本調査では、公式サイト上に `Drouhin-Vaudon` という表記を一件も確認できなかった。**
    **公式のシャブリは `Maison Joseph Drouhin` の下にあり、ワイン名に `Domaine de Vaudon` が現れる。**
    → Open Questions 4
11. ⚠️ **Dundee Hills の 2024 年について公式の情報を語らない。**
    **公式サイトに 2024 のページが存在せず、本ドシエの記述は 2021 のページに基づく。**
    **ヴィンテージ固有の記述（天候・テイスティング）を 2024 に流用してはならない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

**新規の登録なし。**

🔍 **走査結果**: canonical 生産者 384 件を `drouhin` で走査 → **3 件**。
**`Joseph Drouhin` / `Domaine Drouhin-Vaudon` / `Domaine Drouhin Oregon`。**
🔴 **これは重複ではない。公式サイトの構造とも整合する分割であり、統合してはならない。**
**`P-7`（Chave / Chave Sélections。「ブランド軸の実体化・統合禁止」）と同型の、正しく分離された例である。**

🔴 **ただし本調査は既存カテゴリに該当する事象を 2 件観測した。新しい番号は開かない。**

1. 🔴 **`producer:domaine-drouhin-oregon` に alias が無いため、OBP 1 本が実体不明のまま落ちている。**
   **OBP の印字は `Drouhin` の 1 語**（セクションは `UNITED STATES | RED > WILLAMETTE`）。
   canonical には **`Domaine Drouhin Oregon`（`facts.subregion = Willamette Valley`）が存在するのに、
   `producer_state` すら `unresolved` になっている。**
   ⚠️ **これは衝突ではなく `aliases` 空の帰結**である。
   **ただし `Drouhin` を alias に足すと、`Joseph Drouhin` と `Drouhin-Vaudon` の 3 者に多義化する。**
   🔍 **セクションが `WILLAMETTE` である以上、地域で解ける。**
   → **正しい修正は「alias 追加」ではなく「セクション（産地）を使った曖昧性解消」であり、
   これはマッチャ側の設計判断である。** → Open Questions 2
2. **`C-4`（識別語を持たないキュヴェ名）に該当** —
   `cuvee:joseph-drouhin-musigny` の名称は **`Musigny`**、
   `cuvee:joseph-drouhin-marquis-de-laguiche` の名称は **`"Marquis de Laguiche"`**
   （🔴 **二重引用符込み。Batch 5 の Rousseau / Billaud-Simon と同じ形**）。
   **前者はアペラシオン名そのもの、後者は所有者名だけでワインの実体（Montrachet）が名称に無い。**

---

## Sources

**一次資料（公式サイト `https://www.drouhin.com/` のみ。非公式ソースは一切使用していない）**

| 資料 | 取得した情報 |
|---|---|
| `sitemap.xml`（**全 438 URL**） | 走査の起点。**`en_US` 211 URL を全件確認。`/en_US/wine/<slug>/<millésime>` 形式のワインページ 163 件を列挙** |
| 🔴 **`/en_US/wine/…` ワインページ ×10** | 🔴 **本ドシエの中核。** OBP 掲載 10 本の **Site / Soil / History & tradition / Tasting（Véronique Boss-Drouhin）/ Vintage / `Supply` / Vinification / Ageing（新樽 % と月数）/ Cellaring / 供出温度** |
| 🔴 **`/en_US/winepdf/…` PDF ×3** | **Montrachet Marquis de Laguiche 2021 / Musigny 2021 / Chambolle-Musigny 1er Cru 2023 の公式テクニカルシート**（307–319 KB）。⚠️ **内容は Web ページと同一で、分析値は含まれない** |
| **`/en_US/presentation/in-pursuit-of-excellence`** | 🔴 **4 世代・約 90 アペラシオン・有機とビオディナミ・馬耕・被覆作物・自然堆肥・植密度 12,500 本/ha・低収量・手摘み・除梗・垂直/水平プレス・重力清澄・野生酵母・樫の 3 年自然乾燥・スタイルの自己規定** |
| 🔴 **`/en_US/presentation/pioneers-in-oregon`** | 🔴 **`Côte d'Or 53 ha / Chablis 40 ha / Oregon 100 ha`・1961 年の着想・1987 年 7 月 DDO 設立・`French Soul, Oregon Soil`・1989 年重力式ワイナリー・Laurène / Louise / Arthur の由来・1996 年初シャルドネ・2013 年 Roserock 取得（112 ha / 畑 54 ha）・2 つのテロワールの対比** |
| **`/en_US/passion-2/our-vines-a-constant-attention-to-details`** | **栽培の 1 年**（11 月の有機資材 → 2 月までの剪定 → 4 月の耕起 → 誘引・摘芯 → 7–8 月のグリーンハーヴェストと除葉 → サンプリングによる収穫日決定） |
| **`/en_US/legal-mentions`** | 法定表示。サイトの編集主体は **Maison Joseph Drouhin**（Vinium との協働） |

**取得できなかったもの / 存在しなかったもの**
- 🔴 **分析値（アルコール・pH・総酸・収穫日・生産量）が公式に一切無い。** **PDF にも無い。**
- ⚠️ **`Côte de Beaune Rouge 2023` の Winemaking 欄（新樽 % と熟成月数）を本調査で取得できていない。**
  白と Cellaring / 供出温度は取得済み。
- ⚠️ **`/en_US/wine/domaine-drouhin-oregon-pinot-noir-dundee-hills/2024` が存在しない。**
  **OBP は 2024 を載せているが、公式の最新は 2021。**本ドシエの DDO 記述は **2021 ページ**に基づく。
- ⚠️ **`/en_US/wine/chablis-domaine-de-vaudon/<年>` は 2019 / 2020 / 2021 / 2022 のいずれも本文を返さなかった。**
- 🔴 **`Drouhin-Vaudon` という表記が公式サイト上に一件も見つからなかった**（取得済み全ページを走査）。
- ⚠️ **仏側の有機 / ビオディナミの認証機関名・認証名が公式に無い。**
- ⚠️ **区画ごとの ha・樹齢・実収量が公式に無い。**

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
canonical 生産者 **3 件**（すべて `confidence 0.2` / `aliases` 空）／
canonical キュヴェ **3 件**（`Chablis Premier Cru Montmains` / `"Marquis de Laguiche"` / `Musigny`）／
canonical ヴィンテージ **3 件**（Montmains 2022 / Laguiche 2021 / Musigny 2021）／
OBP **10 本**（`exact` 2・`unresolved` 8。**うち 7 件はキュヴェ不在、1 件は生産者 alias 不在が原因**）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **High** | 創業年・世代数・アペラシオン数・3 地域の所有面積・Oregon 2 部門まで公式で確定。**面積の内訳が定型文と合わない点のみ ⚠️** |
| Overview | **High** | 🔴 **`Supply` 欄という、この生産者を理解する最大の鍵が一次で取れた** |
| History | **High** | 🔴 **1776 / 1880 / 1947 / 1960 年代 / 1987 / 1988 / 1989 / 1996 / 2004 / 2013 と年が特定できる** |
| Location | **High** | 🔴 **OBP 掲載 10 本すべてについて Site と Soil の公式記述がある。** 区画ごとの ha のみ不明 |
| **Farming** | **High** | 🔴 **有機・ビオディナミ・馬耕・被覆作物・自然堆肥・植密度 12,500 本/ha・栽培の 1 年まで公式。** ⚠️ **ビオディナミ開始年の食い違いと、認証名の不在** |
| **Winemaking** | **High** | 🔴 **OBP 10 本中 9 本について、新樽比率・熟成月数・発酵容器・全房比率・酵母・プレス方式が公式。** ⚠️ **Côte de Beaune 赤の醸造欄のみ未取得** |
| **Style** | **High** | 🔴 **OBP 10 本すべての公式テイスティングノート（Véronique Boss-Drouhin）＋ 4 ヴィンテージの公式評** |
| **Important Cuvées** | **High** | 🔴 **OBP 10 本すべてを公式の正式名と突合。** `Côte de Beaune` 白赤の分離、`Chambolle 1er Cru` の構成区画、`Montrachet` の権利関係、`Chablis 1er Cru` と `Montmains` の別物性まで確定 |
| Staff Notes | **High** | ⚠️ 11 項目。🔴 **「全部自社畑」という最も出やすい誤りを塞いだ** |
| **総合** | **High — staff-usable（70% を明確に超過）。** | **OBP 掲載 10 本すべてについて、畑の性格・土壌・自社畑か否か・新樽比率・熟成期間・造り手自身のテイスティングノートと飲み頃を言える。** 欠けているのは分析値のみで、**これは公式が publish していない。** |

**reached_70: YES.**

---

## Open Questions

1. 🔴 **canonical にキュヴェが 7 件欠落している** —
   `Chablis Premier Cru`（混成）/ `Chablis Grand Cru Vaudésir` / `Côte de Beaune Blanc` /
   `Côte de Beaune Rouge` / `Puligny-Montrachet` / `Puligny-Montrachet 1er Cru Les Folatières` /
   `Chambolle-Musigny Premier Cru`。**OBP 7 本の未解決の直接原因。**
   → **追加は canonical への書き込みであり、本書では行っていない。** 昇格可否は Akio / CTO 判断。
2. 🔴 **`Drouhin` の 1 語をどう解決するか。**
   OBP の Dundee Hills 1 本は `producer_state = unresolved`。
   **`Drouhin` を alias に足すと 3 生産者に多義化する。**
   🔍 **セクションが `UNITED STATES | RED > WILLAMETTE` であり、
   canonical の `producer:domaine-drouhin-oregon` は `facts.subregion = Willamette Valley` を持つ。
   産地での曖昧性解消が可能である。** → **マッチャ側の設計判断。**
3. ⚠️ **所有面積の不一致。** 公式は「Côte d'Or 53 ha / Chablis 40 ha / Oregon 100 ha」と書くが、
   ワインページの定型文は仏側を「**its 100-hectare (247 acres) estate**」と書く。**53 ＋ 40 ＝ 93。**
   **どちらを canonical の `facts` に入れるかは決められない。**
4. 🔴 **`Drouhin-Vaudon` の出所。**
   **公式サイト上に一件も現れない**が、**OBP は 2 本をこの名で印字し、canonical にも
   `producer:domaine-drouhin-vaudon` が存在する。**
   **輸出市場のラベル表記と思われるが、公式で裏が取れていない。ラベル実物での確認が要る。**
5. **ビオディナミの開始年。** 「1990 年代から」（ワインページ）対「80 年代末から」（presentation）。
6. **仏側の有機 / ビオディナミの認証。** 公式に認証名・認証機関名が無い。
   🔍 **Ganevat のドシエで使った Agence Bio / Ecocert のレジストリで照会すれば確定できる**が、**本調査では未実施。**
7. **`Côte de Beaune Rouge 2023` の新樽比率と熟成月数。** ページは取得したが Winemaking 欄を読み切れていない。
   **再取得すれば埋まる。**
8. **DDO Dundee Hills の 2024 ページが公式に無い。** OBP は 2024 を載せている。
   **ヴィンテージ固有の記述は 2021 のものであり、2024 に流用してはならない。**
9. **公式にテクニカルシートはあるが分析値が無い。** アルコール・pH・総酸・収穫日・生産量は
   **どのワインについても取得できない。** → **輸入元資料が要る。**
10. **`Chablis Premier Cru Montmains`（canonical）が OBP に対応しないまま残っている。**
    **公式には実在するワインなので誤りではないが、`vintage 2022` を持つのに OBP と結ばれていない。**
    **「canonical に在るが OBP に無い」ケースとして正常。**
