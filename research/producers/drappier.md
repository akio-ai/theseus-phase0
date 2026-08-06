# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:drappier` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagne-drappier.com / 公式 PDF で確認**（一次資料）
> `📄` 単一の非公式資料のみ（本書では不使用）／ `⚠️` **公式内で食い違い。両方を残す**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 公式ドメイン: `https://www.champagne-drappier.com`
> 参照した公式ページ: `/en/`（home） `/en/house/` `/en/history-family/` `/en/vineyard/`
> `/en/work-cellar/` `/en/nature-environment-and-carbon-neutrality/` `/en/champagnes/`
> `/en/loenotheque/` `/en/ephemeral-qualities/` `/en/news/` `/en/clarevallis/`
> `/en/grande-sendree/` `/en/quattuor/` `/en/brut-nature-sans-soufre/`
> **＋ 仏語版** `/fr/le-vignoble` `/fr/histoire-de-famille` `/fr/le-travail-en-cave` `/fr/nature-...`
> （**仏語版と英語版で栽培面積・認証範囲・樽材の年代が食い違う。§Farming / §Winemaking 参照**）
>
> **公式テクニカルシート（FT）9 種を取得・解析済み**（`_sources/drappier/FT_*.pdf`）:
> Grande Sendrée 2015 ／ Œnothèque 2005 ／ Œnothèque 2007 ／ Père Pinot 2 ／ Clarevallis ／
> Carte d'Or ／ Brut Nature ／ Brut Nature Sans Soufre ／ Quattuor ／ Rosé de Saignée ／
> Millésime Exception 2019 ／ Charles de Gaulle
>
> **公式ニュースレター「La Lettre」66・67・68・69 を全文解析済み**（EN/FR、`_sources/drappier/lettre6*.pdf`）。
> 🔴 **Lettre 69（2026 春夏号、公式サイト掲載の最新号）が、公式サイト本文より新しい。
> 当主世代・技術陣の現況はニュースレター側が正しい。§Identity の警告を必ず読むこと。**

---

## Identity

| | |
|---|---|
| **Canonical Name** | Drappier |
| **公式の自称** | **Champagne Drappier** ／ **Maison Drappier** ／ **Domaine familial depuis 1808**（公式 home の `<title>`）✅ |
| **Aliases** | canonical `aliases` は空 🔍。OBP 印字は `Drappier` |
| **業態** | **récoltant-manipulant 系の家族経営メゾン**（自社畑＋契約栽培農家からの購入を併用）✅ |
| **所在** | **Rue des Vignes, 10200 Urville, France**（公式フッター）✅ |
| **地区** | Champagne — **Côte des Bar**（Aube 県 Bar-sur-Aube 郡）✅ |
| **創業** | **1808 年**、François Drappier が Urville に定住 ✅ |
| **世代** | **第 8 世代が現役**（2016 年に参画）✅ |
| canonical id | `producer:drappier` |
| canonical entity confidence | 0.2（`legacy_app`）— エンティティ同定の確度。本書の充実度とは別軸 |

### 🔴 現況（2026-08 時点）— 公式サイト本文は古い。ここを間違えると現場で事故る

| 人物 | 現況 | 出典 |
|---|---|---|
| **André Drappier** | 🔴 **1926–2025。2025 年に 99 歳で逝去。** | ✅ Lettre 69 マストヘッド「André DRAPPIER (1926-2025)」／本文「André Drappier, who passed away in 2025 at the age of 99」／Lettre 67 は Michel Drappier 署名の追悼文一本 |
| **Michel Drappier** | 現当主。**1979 年から醸造を統括**。Lettre 66 の巻頭論説に署名、2026 年 3 月も Éclose の試飲に登場 | ✅ 公式サイト＋Lettre 66 / 69 |
| **Sylvie Drappier** | Michel の妻 | ✅ |
| **Hugo Drappier**（1991 年生） | **第 8 世代。現在のハウス・ワインメーカー。** 元は「viticulture と œnologie の責任者」表記 | ⚠️ 下記参照 |
| **Charline Drappier**（1989 年生） | マーケティング／商業。ギフトボックスのデザインも担当 | ✅ |
| **Antoine Drappier**（1996 年生） | 馬（traction animale）による畑作業。動物・自然担当 | ✅ |
| **Elysé Brigandat** | 公式サイト `/en/work-cellar/` に **Cellar Master** として記載 | ⚠️ 下記参照 |

⚠️ **技術陣の呼称が公式内で二重化している。両方残す。**

| 出典 | 記述 |
|---|---|
| 公式サイト `/en/work-cellar/`（更新日不明・本文は André 存命前提） | 「the three Drappier generations, **André, Michel and Hugo** come together each year with **Cellar Master, Elysé Brigandat**」 |
| 公式 Lettre 69（2026 春夏、PRESS 欄に転載された 2025 年 11 月の記事） | 「**Hugo Drappier** … **is now the house winemaker. He is the 8th generation to hold the title.**」 |

→ **André が 2025 年に亡くなった以上、サイト本文の「三世代が毎年集まる」は既に成立しない。**
Elysé Brigandat が現任かどうかは公式に否定も更新もされていない → **❓ Open Questions 2**。
🔴 **現場では「Hugo が現在の造り手、Michel が統括、André は 2025 年に他界」までにとどめる。**

✅ **Hugo Drappier は The Drinks Business の "Top 100 Best Wine Makers in the World" で
2025 年の Best Winemaker に選出**（Lettre 67 の DISTINCTION 欄で公式が報告）。
受賞理由として挙げられたのは **minimal intervention・ワインの自然な色・fleshy elegance**。

---

## Overview

✅ **Côte des Bar の Urville に本拠を置く、1808 年創業・第 8 世代の家族経営シャンパーニュ・メゾン。**
畑は **Kimmeridgian（後期ジュラ紀）の石灰質**で、公式は**「シャブリ・グラン・クリュと同一の土壌」**と明言する。
**Pinot Noir が畑の 70%** を占め、公式表現では「Pinot Noir は我々の血に流れている（runs in our veins）」。

✅ **メゾンの核は「引き算」である。** 亜硫酸は業界最小水準（**30–45 mg/L、法定上限の 1/4 未満**）、
ドサージュは**約 40 年前からゼロ・ドサージュに特化**、**約 10 年前に第一発酵の補糖（加糖）を完全にやめた**。
濾過なし・脱色なし・動物由来の清澄剤なし。**2007 年に亜硫酸無添加の `Brut Nature Sans Soufre` を発売**し、
公式は自らを **「現代史上初の亜硫酸フリー・シャンパーニュを造ったメゾン」** と位置づける（Lettre 69）。

✅ **2016 年、Écoact により地域初の「カーボン・ニュートラル」認定を取得。**
公式サイトのロゴにも常時「Première Maison « Carbone Neutre »」と掲げている。

✅ 公式（Lettre 69）によれば、**2026 年の "world's most admired Champagne brands" で 2 つ順位を上げて 16 位**。
✅ **フランス国内が最大市場で売上の 40%**（Lettre 68）。

---

## History

### Cistercian の前史（メゾン以前）

| 年代 | 出来事 | |
|---|---|---|
| 約 2,000 年前 | ガロ・ローマ人が Urville となる villa の丘に最初のブドウを植える | ✅ |
| **1116** | **Saint Bernard**（Cîteaux 修道院の修道士、Clos Vougeot 近郊出身）がブドウ畑を再興。ブルゴーニュから **Morillon Noir**（Pinot の祖先）を導入 | ✅ |
| **1152** | Saint Bernard が **Urville に酒庫（cellier）を建造**。Bavin-Sainte Eulalie の付属施設。すべては **Clairvaux 大修道院**の所有 | ✅ |
| 1153 | Saint Bernard 没。当時の年間ワイン生産は**約 600,000 リットル**。ガラスが高価だったため大半は樽で出荷 | ✅ |
| — | これらは **Vins de Bar** と呼ばれ、Aube・Seine 川の商船でシャンパーニュ伯とパリに運ばれ愛飲された | ✅ |
| フランス革命後 | ナポレオンが Clairvaux 修道院を**監獄**に転用。19 世紀に Urville の酒庫は**村の司祭館**になる | ✅ |
| 第二次大戦後 | 酒庫の隣に住んでいた **Drappier 家がこれを買い取り、そこに蔵を構える**。現在はメゾン最良のヴィンテージと大瓶を収める | ✅ |

✅ **この 12 世紀の穹窿（vaulted）セラーは UNESCO のインベントリに登録されている**（Lettre 68）。

### Drappier 家（1808–）

| 年 | 出来事 | |
|---|---|---|
| 1604 | **Rémy Drappier** 誕生。家系図の起点。のちに Reims の**羅紗商（cloth merchant / marchand drapier）**となる — Nicolas Ruinart と同業 | ✅ |
| 1669–1724 | 孫の **Nicolas** はルイ 14 世の**国王代訴人（procureur au roi）** | ✅ |
| **1808** | **François Drappier が Urville に定住し、数 ha の畑の耕作を始める** ← **メゾンの起点** | ✅ |
| 1930 年代初 | **Georges Collot**（Michel の母方の祖父）が**この canton で最初に Pinot Noir を植え直す**決断。物議を醸し **「Père Pinot（ピノ親爺）」**の綽名を得る。Pinot Noir は現在 Drappier の畑の 70%、Aube 全体でも同比率 | ✅ |
| **1952** | **André と Micheline Drappier が `Carte d'Or` を創出**（黄色いラベル、マルメロのジャム＝coing の香り） | ✅ |
| **1957** | **歴史的な霜害。収穫の 95% が壊滅。** André は春霜に強い **Pinot Meunier** の導入を決断 | ✅ |
| **1965** | **Charles de Gaulle 将軍**が Colombey-les-Deux-Églises の私邸 **La Boisserie** で Drappier の Pinot Noir を愛飲。当時のメゾン最大の著名顧客 | ✅ |
| **1968** | **Micheline が「ロゼを造ろう」と提案し、100% Pinot Noir と決める** → 現在の `Rosé de Saignée`。50 年後にはエリゼ宮でも供された | ✅ |
| 1970 年代 | **`Grande Sendrée` 誕生。** Michel Drappier 自身が「Philipponnat が 1935 年に Clos des Goisses でテロワール・ワインの先鞭をつけ、**70 年代に Krug の Clos du Mesnil と Drappier の Grande Sendrée が生まれた**」と書いている | ✅ Lettre 66 |
| **1979** | **Michel Drappier が醸造を掌握**（以後現在まで） | ✅ |
| 1980 年代 | 亜硫酸を使わない醸造の**実験開始** | ✅ |
| **1988** | ナポレオン 3 世期に Reims の白亜に掘られた**深いカーヴが家業に加わる**。Grande Sendrée の最良ボトルはここで眠る | ✅ |
| **1990** | **6 月 18 日の呼びかけ 50 周年**を記念し、ヴィンテージ・キュヴェ **`Charles de Gaulle`** を創出 | ✅ |
| **2007** | **`Brut Nature Sans Soufre` 発売**（80 年代からの実験の到達点）／ **`Quattuor` 初リリース**（古代品種の復活） | ✅ |
| **2012** | 卵型フードル **`Ovum`（3,342 L）**がカーヴに到着。**シャンパーニュ地方初** | ✅ |
| **2013** | **Fromenteau（＝Pinot Gris）**が畑に加わる。最も新しい復活品種 | ✅ |
| **2016** | **第 8 世代（Charline / Hugo / Antoine）が参画**。同年 **Écoact による「カーボン・ニュートラル」認定**（地域初）。`Père Pinot` プロジェクト開始 | ✅ |
| **2019** | **`Trop m'en Faut`（100% Fromenteau）**リリース | ✅ |
| **2025** | 🔴 **André Drappier 逝去（99 歳）** | ✅ Lettre 67 / 69 |
| **2026 年春** | **`Éclose` を初試飲・発表**（Ovum 由来。2010 年開始の卵型フードル研究の結実） | ✅ Lettre 69 |

---

## Location

| | |
|---|---|
| **Country** | France |
| **Region** | Champagne — **Côte des Bar**（Aube 県、Bar-sur-Aube 郡）✅ |
| **Village（本拠）** | **Urville**（10200）。「Essentiellement situé sur la commune d'Urville」✅ |
| **第 2 拠点** | **Reims** — ナポレオン 3 世期の白亜の深いカーヴ（1988 年取得）。Grande Sendrée の長期熟成用 ✅ |
| **土壌** | **Kimméridgien Supérieur（後期ジュラ紀）の石灰質**。公式は繰り返し**「シャブリ・グラン・クリュと同一」**と書く。FT の表記は `Jurassic Kimmeridgian limestone (and chalk)` ✅ |
| **地形** | Urville を囲む coteaux（斜面）。FT `Œnothèque` は **south-facing slopes（南向き斜面）**と明記 ✅ |

### Key Vineyards / 区画

- **Grande Sendrée** ✅ — メゾンの看板単一区画。**1836 年の Urville 大火で灰（cendres）を被った区画群**に由来。
  地籍の新版で綴りを誤り "s" が入ったため、今日は **Sendrée** と綴る。
  FT 2015 は **"an archipelago of plots on Kimmeridgian chalk"**（Kimmeridgian 石灰上の**区画の群島**）と表現する。
  → 🔴 **単一の一枚畑ではなく、区画の集合体である。**「single vineyard」と言い切ると危うい
  （公式 Lettre 69 の press 引用は "A single vineyard wine" と書いているが、FT の記述が優先）⚠️
- **Cornellier** ✅ — 公式が名指しする畑。近隣に、建築学生がリサイクル材で建てた**ブドウ畑の小屋（cabanes）**が点在し、訪問者が中で試飲できる。
- **古代品種の畑 — 4 ha** ✅ — Arbanne / Petit Meslier / Blanc Vrai / Fromenteau。
- ❓ **`Les Riceys`** — Côte des Bar の村。**Drappier の公式サイトには一切記述が無い。** §Important Cuvées 参照。

### 品種構成（公式 `/en/vineyard/`・`/fr/le-vignoble`）✅

| 品種 | 比率 |
|---|---|
| **Pinot Noir** | **70%** |
| Pinot Meunier | 15% |
| Chardonnay | 9% |
| **古代品種（Arbanne / Petit Meslier / Blanc Vrai / Fromenteau）** | **6%** |

✅ **シャンパーニュの認可 7 品種すべてを栽培している**（`/en/nature-.../` に明記）。
これは現場で強い。**「7 品種すべてを持っている造り手」は多くない。**

---

## Farming

### 実践（公式内で一貫。ここは断定してよい）✅

- **除草剤・殺虫剤を一切使わない**（no herbicides, no insecticides）
- **手作業の除草（désherbage manuel / à la pioche ＝鍬）**
- **馬による耕作（labour à cheval）** — 末子 **Antoine Drappier** が自身の輓馬で担当。
  公式の理由づけは **①植物に最も近い作業ができる ②カーボン負荷の低減 ③土壌の踏み固めと侵食の回避**
- **enherbement maîtrisé（管理された草生栽培）** と **jachère（休閑）**。生物多様性のため
- **電動トラクター・電動商用車への段階的転換**（熱機関からの置換）
- 敷地内に **菜園・古い果樹園（パーマカルチャー）・鶏舎**

### 🔴 有機認証の範囲 — **公式内で 3 通りに割れている。統合するな**

| 出典 | 記述 |
|---|---|
| **仏語** `/fr/le-vignoble` | 「**Aujourd'hui, 100% du domaine est cultivé en agriculture biologique, certifié par le label Ecocert.**」＝ **ドメーヌの 100% が有機、Ecocert 認証** |
| **英語** `/en/vineyard/`（同一ページの英訳） | 「We apply these methods across **27 hectares** of land, which are now cultivated sustainably and **certified organic by Ecocert**」 |
| **英・仏** `/…/nature-environment-and-carbon-neutrality/` | 「over **110 ha** の畑、うち **60 ha が自社所有**、**17 ha が 2017 年から AB 認証**、**さらに 10 ha が転換中**。**畑全体は持続可能栽培**」 |
| **FT Grande Sendrée 2015** | 「Sustainable and organic farming, **certified organic since 2014**」（＝当該区画） |
| **公式サイトのグローバル注記** | 「***Wines certified organic**」の星印が付くのは **`Clarevallis` と `Quattuor` の 2 キュヴェのみ** |

⚠️ **17 + 10 = 27** なので、英語 vineyard ページの「27 ha が認証済み」は
**「17 認証済み＋10 転換中」を一括りにした表現**である可能性が高い（＝過大表現）。
一方で仏語 vineyard ページの「100%」は上の全部と矛盾する。
🔴 **どれも消さない。現場では「認証キュヴェは Clarevallis と Quattuor。畑全体は持続可能栽培で、
有機認証は区画ごとに段階的に進行中」とだけ言う。** → ⚠️ リスト 1・§Open Questions 1

### カーボン・ニュートラル ✅

- **2016 年、Écoact により地域初の「Carbon Neutral」認定。**
- **屋根の太陽光パネル約 2,000 m² が必要電力の 75% を賄う。**
- 電動車両群＋来訪者・スタッフ用の充電設備（汎用・Tesla）。
- **Michel Drappier 自身が設計したボトルは従来のシャンパーニュ瓶より 15% 軽い。**
- 瓶・ルミアージュ用ラック（pupitre）等のリサイクル。飲み終えた瓶は**植物性ワックスの蝋燭
  `Incandescence`** に転生させる。
- **天然コルクのみを使用。** WBCSD の算定で **コルク 1 個あたり CO2 を 390 g 削減**（コルク樫の炭素固定）✅ Lettre 69。
- 受賞: **Michel Drappier — Green Personality of the Year（The Drinks Business, 2017）** ／
  **Prix de l'innovation（La Revue du Vin de France, 2019）** ／
  **Trophée Champenois de la démarche éco-responsable（Bulles & Millésimes, 2018）** ✅

---

## Winemaking

### 全キュヴェ共通の骨格（FT 9 種すべてで反復。ここは強い）✅

| 工程 | 内容 |
|---|---|
| **圧搾** | **低圧に較正した機械式プレート／メンブレン・プレス。「キュヴェ」＝一番搾りのみ使用**（Only first press） |
| **移送** | **重力による移送（vinification by gravity / no pumping）** — 酸化を防ぎ、亜硫酸をさらに減らせる |
| **デブルバージュ** | **自然沈降（natural settling）**。遠心分離しない |
| **酵母** | **自社酵母 `Drappier Fermentum Meum`（DFM）** — 自社区画から選抜し、長年の実験の末に命名。**Drappier のワインにのみ使用**。発酵に使う酵母の一部がこれ ✅ |
| **MLF** | **マロラクティック発酵を実施**（全 FT で `Malolactic fermentation`）。Œnothèque は**澱引きと MLF を 18°C で即座に**行う |
| **清澄** | **冬季の低温（5–8°C）での自然清澄。動物由来の製品は一切使わない** |
| **濾過** | **無濾過・無脱色（not filtered, not discolored）** |
| **亜硫酸** | **30–45 mg/L、法定許容量の 1/4 未満**。`Brut Nature` FT は **less than 35 mg/l** と明記 |
| **prise de mousse** | **低温でゆっくり**行う（亜硫酸が少ないから可能）→ **細かく繊細な泡** |
| **補糖** | ✅ **約 10 年前に第一発酵での加糖を停止**。「ブドウ由来の糖のみで、自社酵母で発酵させる。結果として原酒は軽くなる」（Lettre 69） |

### 木（Le « Cercle »）✅

- カーヴの中心が **「Cercle」** — シャンパーニュ地方で**リザーブワインを寝かせる場所**の呼称。
  名の由来は箍（たが）を巻いた **foudres cerclés**。
- **muid（約 274 L）／ demi-muid（約 137 L）** は **Aube の地元オーク**製。
  ⚠️ **年代が公式内で食い違う**: 英語版「planted by the Templars in the **Eighteenth** Century」／
  仏語版「la forêt créée par les Templiers au **XIIIème** siècle」（**13 世紀**）。
  FT `Père Pinot 2` は樽の産地を **Temple Forest (Aube)** と書き、サイト本文は **Orient Forest** と書く。
  → **テンプル騎士団は 1312 年に解散しているため、仏語版（13 世紀）が整合的。**
  🔴 **現場では年代を言わず「Aube の地元オーク（Orient/Temple の森）」にとどめる。** → ⚠️ リスト 8
- **`Ovum`**（2012 年着荷、**シャンパーニュ地方初の卵型フードル**、**3,342 L**）
  ⚠️ 英語版は「holds 3.342 litres of **premium Grande Sendrée**」、仏語版は「**les plus beaux millésimes**（最良のヴィンテージ群）」。英語版の方が限定的。両方残す。
  → **この Ovum から生まれたのが `Éclose`。**§Important Cuvées 参照。

### Liqueur de dosage（ドサージュ用リキュール）✅

**リムーザン産オークの樽で熟成 → その後ダム・ジャンヌ（demijohn）で 15 年以上。**
濃縮と気品を得たものを、デゴルジュマン時に少量だけ加える。
FT `Grande Sendrée 2015` は「liqueur de dosage **matured in wood for 15 years**」、
FT `Œnothèque 2005` は「liqueur aged in oak barrels for **25 years**」と、キュヴェごとに年数が違う。
✅ **狙いは甘さではなく「口中の余韻を伸ばすこと、パレットを重くしないこと」。**

### 大瓶（現場で最も効く技術的事実）✅

🔴 **「Maison Drappier は、ハーフボトルから Melchizedek（30 L ＝ 40 本分）まで、
すべてのサイズで prise de mousse・ルミアージュ・デゴルジュマンを個別に行う唯一のシャンパーニュ・メゾンである」**
（＝大瓶に移し替えない）。公式はこれを**「その瓶の中で泡を起こす」**伝統技法とし、
結果として**大瓶でも例外的な新鮮さと泡の細かさ**が得られると説明する。
**`Primat`** は Drappier が唯一の製造者。名はガロ・ローマ由来のラテン語 `Primatus`（首位）。
大瓶を注ぐため、デザイナー **Carmelo de Giorgio** がスイス・ルツェルン製の精密器具 **`VCanter`** を設計。

### 「Immersion」海中熟成 ✅

**水深 30 m（ブルターニュ沖）で 1〜3 年**。木箱の `Immersion` セットには**同一キュヴェの 2 本**
（海で熟成したものと Urville のカーヴで熟成したもの）が入り、比較試飲ができる。
対象は `Brut Nature` と `Carte d'Or`。

---

## Style

✅ **ハウススタイルは「Pinot Noir の果肉と、Kimmeridgian の石灰のミネラル」の二軸。**
公式の言葉では「**エレガンスと、その正体である Kimmeridgian・ジュラ紀石灰のミネラル質を決して手放さない**」。

**外観**: 🔴 **亜硫酸が極端に少ないため、色が濃い。**公式は
「**より自然な、深い黄金色、しばしば銅色（cuivré）**」と自ら書く。
→ **現場で「色が濃い＝古い／酸化している」と誤解されるのは Drappier で最も起きやすい事故。
色は意図された結果である、と先回りして説明すること。**

**泡**: 低温・低速の prise de mousse に由来する **fine, subtle effervescence**（細かく穏やか）。

**味わい**: FT の頻出語は **quince jelly（マルメロのジャム、Carte d'Or の署名）／ vineyard peach（畑の白桃）／
spicy notes（スパイス）／ black grapes freshly pressed**。
Pinot Noir 主体ゆえ **vinous（ワイン的）で肉厚**、しかしドサージュが低いため輪郭は締まる。

**ドサージュ**: ✅ **約 40 年前からゼロ・ドサージュに特化。**
Lettre 69 は「**Charles de Gaulle（クラシックな Brut）と少数の Demi-Sec を除き、
全キュヴェが Brut Nature（ドサージュ 0）か、4 g/L 未満の Extra-Brut**」と書く。
⚠️ **しかし FT の実数はこれと合わない**（下表）。🔴 **この一文をそのまま客に言うな。** → ⚠️ リスト 3

| キュヴェ | FT のドサージュ | 表記 |
|---|---|---|
| Brut Nature ／ Brut Nature Sans Soufre | **0 g/L** | Brut Nature |
| Père Pinot 2 | **1.8 g/L** | Extra Brut |
| Clarevallis ／ Œnothèque 2005・2007 | **4 g/L** | Extra Brut |
| Quattuor ／ Grande Sendrée 2015 | **4.2 g/L** | — |
| **Carte d'Or ／ Charles de Gaulle ／ Millésime Exception 2019** | **5 g/L** | ← **4 g/L 超** |
| **Rosé de Saignée** | **5.5 g/L** | ← **4 g/L 超** |

**位置づけ**: ✅ Lettre 69 が引用する米国の批評（2026 年 1 月）は Drappier を
**Pol Roger / Bollinger / Jacquesson と並べて**推奨している（＝第三者評価。§⚠️ リスト 10）。

---

## Important Cuvées

### 🔍 OBP 掲載分（7 本）— canonical 登録状況つき

| # | OBP 印字 | VT | 価格 | OBP 節 | canonical | state | 公式 FT |
|---|---|---|---|---|---|---|---|
| 1 | `'Clarevallis,' Extra Brut` | NV | $230 | BLENDS | ✅ **登録済** `Clarevallis Extra Brut`（Urville — Côte des Bar / NV） | alias | ✅ あり |
| 2 | `'Grand Sendrée,' Brut` | **2012** | $400 | BLENDS | ✅ **登録済** `Grande Sendrée Brut`（2010, 2012） | alias | ⚠️ **2012 の FT は無し**（2015 のみ） |
| 3 | `'Grand Sendrée,' Brut` | **2010** | $395 | BLENDS | ✅ **登録済**（同上） | alias | ⚠️ **2010 の FT は無し** |
| 4 | `'Père Pinot 2,' Extra Brut` | NV | $455 | BLENDS | ✅ **登録済** `Père Pinot 2` | exact | ✅ あり |
| 5 | `'Réserve de L'Oenothèque,' Brut` | **2007** | $460 | BLENDS | ✅ **登録済** `Réserve de l'Oenothèque Brut`（2007） | alias | ✅ **あり（2007 専用）** |
| 6 | `'Éclose,' Extra Brut` | **2012** | **$1,520** | BLENDS | ✅ **登録済** `Éclose`（2012） | exact | ❌ **FT 無し** |
| 7 | 🔴 `'Les Riceys,' Brut Nature` | NV | $295 | **ROSÉ** | ❌ **canonical 未登録** | **unresolved** | ❌ **FT 無し・専用ページ無し** |

⚠️ **メニュー印字の綴りが 2 本で誤っている**: `Grand Sendrée` → 正しくは **`Grande Sendrée`**。
語源（1836 年の大火の灰＝cendres）を語るなら綴りは **Sendrée**。

---

### 1. Clarevallis — Extra Brut ✅ **有機認証キュヴェ**

| | |
|---|---|
| **セパージュ** | **Pinot Noir 75% / Pinot Meunier 10% / Chardonnay 10% / Blanc Vrai 5%** |
| **名の由来** | **`Clara Vallis`（明るき谷）— Saint Bernard が自ら創建した修道院に与えた名**。＝ **Clairvaux** |
| **畑** | **Urville の斜面。シトー会時代に植えられた区画。有機栽培。一部は馬で耕す** |
| **醸造** | Jurassic Kimmeridgian 石灰／一番搾りのみ／重力／MLF／**自社畑由来の有機の澱（organic lees from the estate）**／無濾過・無脱色／亜硫酸極少 |
| **ドサージュ** | **4 g/L** |
| **テイスティング（公式）** | **金色がかった灰色（golden grey）**、極めて細かく持続する泡。**ニワトコ（elderberry）とスミレ**。石灰のミネラルが Pinot の果肉で和らぐ。控えめなドサージュと美しい苦味の調和 |
| **サービス（公式）** | **7°C**。アペリティフまたは食中。**鯛のマリネとグレープフルーツ／夏のサラダ／手長海老と歯応えのある野菜** |

✅ **Lettre 69 が引用する 2026 年 2 月の評**: 熟したリンゴ、焼いたブドウ、カスタードクリーム、
ロースト・コーヒー、糖果した黄色い果実。フィニッシュは crisp・fresh・mineral で**微かなタンニン感**。
✅ クロアチア Korčula 島のミシュラン店 **LD Restaurant のシグネチャー・ワイン**（Lettre 69）。

---

### 2–3. Grande Sendrée — Brut（2012 / 2010）— **メゾンの看板**

| | |
|---|---|
| **名の由来** | ✅ **1836 年の Urville 大火で灰（cendres）を被った区画群。地籍の新版で綴り誤りが入り、今日は "s" 付きの `Sendrée`** |
| **畑** | ✅ **Kimmeridgian 石灰上の「区画の群島（an archipelago of plots）」**。FT 2015 は **2014 年から有機認証**と記載 ⚠️ |
| **瓶** | ✅ **Urville のカーヴで見つかった 18 世紀の瓶（Louis XV 型）の複製**。**ルミアージュは全量が完全な手作業** |
| **マグナム** | ✅ **1999 ヴィンテージから** |
| **誕生** | ✅ **1970 年代**（Michel Drappier 自身が Krug `Clos du Mesnil` と並べて言及） |
| **熟成（2015 FT）** | ✅ **ワインの 100% が樽で熟成**。亜硫酸極少。**瓶熟 9 年**（⚠️ 同じ FT のテイスティング欄は「eight years of maturation」と書く。両方残す） |
| **ドサージュ（2015 FT）** | **4.2 g/L**（**木樽で 15 年熟成させた liqueur de dosage**） |

🔴 **2010 / 2012 の公式 FT は入手できなかった。**公式サイトが掲載しているのは **2015 のみ**。
以下は**同じ 2015 の数値であり、2010 / 2012 の数値ではない**: セパージュ **Pinot Noir 55% / Chardonnay 45%**。
→ **OBP の 2 本について、セパージュ・熟成期間・ドサージュを断定してはならない。** → ⚠️ リスト 6・§Open Questions 3

✅ **公式が言及する 2010 / 2012 に関する事実（数値ではない）**:
- **Grande Sendrée 2010** — 2025 年 11 月、ホリデーシーズンの推奨として取り上げられた（Lettre 69）
- **Grande Sendrée 2012** — 2024 年に **94/100**、**The Drinks Business の金賞**（2015 と共に）を受賞（Lettre 67 / 68）
- **2012 は Juan-les-Pins の `La Passagère`（2008 と共に）、Chelles の `Cep & Malt` でオンリスト**（Lettre 67）
- ✅ **Grande Sendrée は Paris エッフェル塔 2 階の 2 つ星 `Le Jules Verne` で供されている**（Lettre 68）。**現場で効く**

---

### 4. Père Pinot 2 — Extra Brut 🔴 **亜硫酸無添加・1,764 本のみ**

| | |
|---|---|
| **名の由来** | ✅ **Georges（Père Pinot）— Aube で Pinot Noir の植え直しを唱えた曾祖父**。「彼は我々の曾祖父でもある」（＝ Charline / Hugo / Antoine から見て） |
| **企画** | ✅ **2016 年、第 8 世代の 3 人が家業に参画した年に始動。「家族のワイン」として自由に家系の醸造の過去を探る** |
| **セパージュ** | ✅ **「4 つの Pinot」を 25% ずつ**: **Pinot Noir 25% / Meunier 25% / Fromenteau（＝Pinot Gris）25% / Blanc Vrai（＝Pinot Blanc）25%** |
| **原料** | ✅ **2020 年収穫分から、4 つの Pinot はすべて自社の Urville 区画由来** |
| **醸造** | ✅ **収穫後に Pinot Blanc の果皮浸漬（skin maceration）**／**半量を Aube・Temple の森のオーク製 quarter-muid で発酵・熟成**／🔴 **亜硫酸無添加（without added sulfur）** |
| **生産量** | ✅ **1,764 本** |
| **熟成／デゴルジュマン** | ✅ **澱と 3 年 → 2024 年 3 月デゴルジュマン** |
| **ドサージュ** | ✅ **1.8 g/L**（熟成リキュール）⚠️ Lettre 66 の press 引用は「2 g/L」。FT を採る |
| **テイスティング（公式）** | 🔴 **銅がかったロゼ色（coppery rose）**。**野生の果実、とりわけブラックベリーとブルーベリー**、**サクランボの核**、**ヴァニラのアンフュージョン**、フレッシュなフィニッシュ |
| **サービス（公式）** | **7°C**。アペリティフ。**桃・ミント・アーモンドのサラダ／手長海老のタルタルとエスプレット** |

🔴 **色が「銅がかったロゼ」であることを必ず先に言うこと。** OBP は BLENDS（白）節に置いているため、
グラスに注いだ瞬間に客が驚く。**これは Drappier で最も起きやすいテーブル事故。** → ⚠️ リスト 11

---

### 5. Réserve de L'Œnothèque — Brut 2007

| | |
|---|---|
| **位置づけ** | ✅ **メゾンの「生きた記憶」＝家族のプライベート・コレクション。**12 世紀のシトー会の穹窿と Reims のカーヴで秘匿し、**その年の強度と個性を明かす準備が整ったと判断した時にだけ、少量ずつ — 時には 1 本だけ — デゴルジュマンする** |
| **公式のリリース** | ✅ 2003 / 2004 / 2005 / **2006（マグナム）** / **2007** |
| **セパージュ（2007 FT）** | ✅ **Pinot Noir 60% / Chardonnay 40%** |
| **醸造（2007 FT）** | ✅ 「キュヴェ」＝一番搾りのみ／**低圧メンブレン・プレス**／**ポンプを使わず重力でタンクへ**／自然沈降／**冬季の自然清澄・無濾過**／**澱引きと MLF を直ちに 18°C で**／**冬季 5–8°C の低温清澄**／**遠心分離なし・濾過なし** |
| **アルコール** | ✅ **12%** |
| **ドサージュ** | ✅ **4 g/L**（LOW DOSAGE） |
| 🔴 **澱との接触** | ✅ **14 年超（over 14 years on the lees）** |
| 🔴 **デゴルジュマン** | ✅ **2023 年 6 月** |
| **テイスティング（公式）** | ✅ **フレッシュさが際立った年。今は great subtlety で表現される。繊細な白い果実、オレンジの花、石灰テロワール由来のミネラリティ** |

✅ **参考: Œnothèque 2005**（OBP 未掲載）は **澱と 16 年超**・**同じく 2023 年 6 月デゴルジュマン**・
**オーク樽で 25 年熟成させたリキュール**で 4 g/L。テイスティングは**糖果した果実と乾いた花、
乾果、菩提樹とマルメロのジャムの爽やかさ**。→ **2007 と 2005 の対比は卓上で強い。**

🔴 **「2023 年 6 月にデゴルジュマンした 2007 年、澱と 14 年超」は、この 1 本で最も価値のある一文。
必ず言うこと。** 数字が具体的で、かつ公式一次資料で裏が取れている。

---

### 6. Éclose — Extra Brut 🔴 **公式 FT 無し。語れることが極端に少ない**

**公式（Lettre 69、2026 年春夏号）に書かれている全て**:
- ✅ **2010 年に始めた卵型フードル `Ovum` の開発研究の結実。**Ovum は**大きなワインを熟成させるのに
  理想的な形状**と考えられている
- ✅ **「Éclose」と名付けたのは 2026 年初春の試飲時**
- ✅ **たった一つのオーク樽（a single oak cask）から生まれた稀少な 1 本**。カーヴから
  **「一滴ずつ（drop by drop）」**放出される
- ✅ **Michel が始め、André が試飲し、Hugo Drappier が完成させた**
- ✅ **`Sendré` の最上のテロワール、Kimmeridgian 石灰**（＝**シャブリ・グラン・クリュと同型**）由来
- ✅ **専用に誂えたボトル（custom-made bottle）**
- ✅ 🔴 **「木とガラスとコルクしか知らない、極めて稀な純粋なシャンパーニュ」**
  （= **ステンレスに一度も触れていない**）
- ✅ 2026 年 3 月、作家 **Amélie Nothomb** が Hugo・Michel と共に試飲

🔴 **公式はヴィンテージを一切書いていない。** OBP と canonical は **2012** としているが、
**2012 は Ovum がカーヴに到着した年**でもある。**「2012 年産」と断定してはならない。** → ⚠️ リスト 7・§Open Questions 4

🖋 **語源の補助**（言語事実のみ、生産者情報ではない）: `Éclose` は仏語 `éclore`（孵る／花開く）の過去分詞。
**卵型のフードル `Ovum`（ラテン語で「卵」）から生まれたワインに「孵った」と名付けている。**
→ **$1,520 の 1 本に対して、これが最も強い一言である。**

---

### 7. 🔴 Les Riceys — Brut Nature（OBP 未解決）

**公式サイト全体で「Les Riceys」への言及は Lettre 66 の 1 箇所のみ。**
`/en/les-riceys` `/en/rose-des-riceys` は **404**。専用ページも FT も存在しない。

✅ **公式に書かれている全文（Lettre 66）**:
「Anne-Sophie Pic … **Our Brut Nature Rosé de Saignée** is now featured at her location in Valence,
while **Brut Nature Les Riceys** is served in her new establishment at the **Beau-Rivage Palace**.」

→ 分かるのは以下だけ:
- ✅ **`Brut Nature Les Riceys` という名の Drappier のワインは実在する**
- ✅ **Anne-Sophie Pic の Beau-Rivage Palace（Lausanne）でオンリスト**
- ❌ **色・セパージュ・畑・熟成・ドサージュ・ヴィンテージ — すべて公式に記述が無い**

🔴 **OBP はこれを `CHAMPAGNE | ROSÉ` 節に置いているが、公式にはロゼである根拠が一切無い。**
同じ Lettre 66 の一文は `Rosé de Saignée` を**明示的に「Rosé」と書いて区別している**のに、
Les Riceys には色の語が付いていない。
🔴 **さらに `Rosé des Riceys`（Les Riceys 村の別 AOC のスティル・ワイン）と混同してはならない。
Drappier の公式資料に `Rosé des Riceys` は一度も登場しない。** → ⚠️ リスト 5・§Open Questions 5

---

### OBP 未掲載だが会話に出やすい主要キュヴェ ✅

| キュヴェ | セパージュ | ドサージュ | 押さえどころ |
|---|---|---|---|
| **Carte d'Or** | PN 80 / Ch 15 / Meunier 5 | 5 g/L | **1952 年、André と Micheline が創出**。**リザーブワイン 40%**、**5% を樽熟**。「ほぼ Blanc de Noirs」。**マルメロのジャム**が署名 |
| **Brut Nature** | **PN 100%** | **0 g/L** | Michel Drappier が創出した「Nature」版の Blanc de Noirs。**亜硫酸 35 mg/L 未満**、**澱と 36 ヶ月**。公式が「メゾンの象徴的ワイン」と紹介する |
| **Brut Nature Sans Soufre** | **PN 100%** | **0 g/L** | 🔴 **2007 年発売。80 年代からの実験の到達点。亜硫酸「無添加」**、**澱と 24 ヶ月**。FT は**「硫黄アレルギーの方に推奨」**とまで書く |
| **Quattuor** ✅有機認証 | **Arbanne 25 / Petit Meslier 25 / Blanc Vrai 25 / Chardonnay 25** | 4.2 g/L | **2007 年初リリース。忘れられた品種の Blanc de Blancs**。名はラテン語の「4」。**澱と 36 ヶ月**。**The Drinks Business 金賞** |
| **Rosé de Saignée** | **PN 100%** | 5.5 g/L | **1968 年に Micheline の発案**。**除梗後の低温プレ発酵浸漬 → 2 日間のセニエ**。**5% を大樽熟成**。エリゼ宮でも供された |
| **Charles de Gaulle** | PN 80 / Ch 20 | 5 g/L | **1990 年、6/18 の呼びかけ 50 周年に創出**。**30% を大樽熟成**、**瓶熟 36 ヶ月**。公式が唯一「クラシックな Brut」と認める |
| **Millésime Exception 2019** | PN 60 / Ch 40 | 5 g/L | 「一年の四季をグラスに封じる」。**60% を瓶詰め前に樽熟**、**澱と 4 年** |
| **Trop m'en Faut** | **Fromenteau 100%** | — | **2019 年初リリース**。**Champagne AOC 版と Coteaux Champenois AOC 版の 2 種**がある |

---

## Staff Notes

### 芯 3 点（これだけで一皿分は持つ）

**① 「シャブリと同じ石灰の上で、Pinot Noir を 70%」**
Côte des Bar の Urville は **Kimmeridgian（後期ジュラ紀）石灰**で、**公式自身がシャブリ・グラン・クリュと
同一土壌だと明言している**。Côte des Blancs の Chardonnay 的シャンパーニュを期待している客に対し、
**「北のブルゴーニュの石灰の上で、赤ブドウを主役にしたシャンパーニュ」**という一文で位置を作れる。
1152 年に Saint Bernard が Clairvaux 修道院の付属として掘らせたセラーが、今もそのまま使われている
（**UNESCO インベントリ登録**）。**Clarevallis というキュヴェ名はその修道院の名（Clara Vallis）そのもの。**

**② 「引き算のメゾン — 亜硫酸・ドサージュ・補糖のすべてを削っている」**
- **亜硫酸 30–45 mg/L ＝ 法定上限の 1/4 未満。** 業界最小水準
- **約 40 年前からゼロ・ドサージュに特化**
- **約 10 年前に第一発酵の補糖を完全に停止**（ブドウ由来の糖のみ）
- **2007 年に亜硫酸無添加の `Brut Nature Sans Soufre` を発売**（80 年代からの実験の結実）
- **無濾過・無脱色・動物由来の清澄剤なし・自社酵母 DFM**

🔴 **その結果としてグラスの中の色が濃い。** 公式自身が「**より自然な深い黄金色、しばしば銅色**」と書く。
**「古いのでは」「酸化では」と聞かれる前に、こちらから色の理由を言う。**
これが Drappier のサービスにおける最重要ポイント。

**③ 「大瓶を移し替えない、唯一のメゾン」**
**ハーフから Melchizedek（30 L）まで、すべてのサイズで瓶内二次発酵・ルミアージュ・
デゴルジュマンを個別に行う。** 大瓶の注文が入った時、これは決定的な差別化になる。
（**Primat は Drappier が唯一の製造者。**）
加えて **2016 年に地域初のカーボン・ニュートラル認定**（Écoact）、
**ボトルは Michel Drappier 設計で従来比 15% 軽量**、**天然コルク 1 個で CO2 を 390 g 削減**。
サステナビリティを訊く客に対して、**認証と数字の両方で答えられる稀な造り手**。

### 追加の「効く」一言

- **Charles de Gaulle 将軍は Drappier の顧客だった。**Colombey-les-Deux-Églises の私邸 La Boisserie は
  Urville のすぐ近く。1990 年に記念キュヴェが生まれた。
  🔴 **ただし将軍が飲んでいたのは `Extra Dry`（18 g/L）である**と Michel Drappier 自身が書いている
  （Lettre 66）。**「将軍もこの Brut Nature を飲んでいた」は誤り。**
- **エッフェル塔 2 階の 2 つ星 `Le Jules Verne` で Grande Sendrée と Rosé de Saignée が供されている。**
- **Hugo Drappier は The Drinks Business の 2025 年 Best Winemaker。** 現在の造り手。
- **シャンパーニュの認可 7 品種すべてを栽培。**うち **Arbanne / Petit Meslier / Blanc Vrai / Fromenteau
  の 4 つの古代品種で 4 ha**。これを 1 本にしたのが `Quattuor`。
- **`Père Pinot 2` は 1,764 本のみ、亜硫酸無添加、2024 年 3 月デゴルジュマン、ドサージュ 1.8 g/L。**
  「4 つの Pinot」を 25% ずつ。
- **`Réserve de L'Œnothèque 2007` は澱と 14 年超、2023 年 6 月デゴルジュマン。**
  必要な時にだけ、時には 1 本だけ抜栓のためにデゴルジュマンする家族のコレクション。

---

### ⚠️ 言ってはいけないこと（記述が薄い分、ここが最重要）

1. 🔴 ❌ **「ドメーヌ全体が有機認証」と言わない。**
   公式内で **100%（仏語 vineyard）／ 27 ha（英語 vineyard）／ 17 ha 認証＋10 ha 転換中（nature 頁）**
   の 3 通りに割れている。**サイトが有機認証の星印を付けているのは `Clarevallis` と `Quattuor` の 2 つだけ。**
   ✅ 言ってよい: **「畑全体が持続可能栽培。有機認証は区画ごとに進行中で、Clarevallis と Quattuor が認証キュヴェ」**

2. 🔴 ❌ **「André Drappier が今も畑を見ている」と言わない。**
   **2025 年に 99 歳で逝去。**公式サイトの History 頁は今も現在形で「74 回の収穫を経た André が
   畑に目を配る」と書いており、**サイトが古い。**
   ✅ 言ってよい: **「Michel が統括、息子の Hugo が現在の造り手。André は 2025 年に亡くなった」**

3. ❌ **「Drappier のシャンパーニュは全てドサージュ 4 g/L 以下」と言わない。**
   Lettre 69 はそう書くが、**FT の実数は Carte d'Or 5 / Charles de Gaulle 5 /
   Millésime Exception 5 / Rosé de Saignée 5.5 g/L**。
   ✅ 言ってよい: **「大半がゼロ・ドサージュか Extra Brut。Carte d'Or や Rosé de Saignée は 5 g/L 前後」**

4. ❌ **`Brut Nature Sans Soufre` を「亜硫酸ゼロ」と言わない。**
   公式表記は **`No added sulphites`＝無添加**。発酵で自然生成される分はある。
   ✅ 言ってよい: **「亜硫酸無添加」**

5. 🔴 ❌ **`Les Riceys` を「ロゼ」と言わない。`Rosé des Riceys` と呼ばない。**
   OBP はロゼ節に置いているが、**公式には色の記述が一切無い**（公式の言及は Lettre 66 の 1 行のみ）。
   ✅ 言ってよい: **「Les Riceys 村のブドウによる Brut Nature。詳細は公表されていない。
   Anne-Sophie Pic の Beau-Rivage Palace でも供されている」**（＋**開ける前にグラスで色を確認する**）

6. ❌ **`Grande Sendrée` **2010 / 2012** のセパージュ・熟成期間・ドサージュを断定しない。**
   公式 FT は **2015 のみ**（PN 55 / Ch 45、樽熟 100%、瓶熟 9 年、4.2 g/L）。
   **これらは 2010 / 2012 の数値ではない。**
   ✅ 言ってよい: **「1836 年の大火で灰を被った Kimmeridgian の区画群。18 世紀の瓶の複製に詰め、
   ルミアージュは全量手作業。1970 年代生まれのメゾンの看板」**

7. ❌ **`Éclose` を「2012 年ヴィンテージ」と断定しない。**
   **公式はヴィンテージを書いていない。2012 は卵型フードル `Ovum` が到着した年。**
   ✅ 言ってよい: **「卵型フードル Ovum から生まれた単一樽の 1 本。木とガラスとコルクしか知らない。
   Michel が始め、Hugo が仕上げた」**

8. ❌ **樽材のテンプル騎士団の年代を「18 世紀」と言わない。**
   英語版はそう書くが、**仏語版は 13 世紀**であり、テンプル騎士団は 1312 年に解散している。
   ✅ 言ってよい: **「Aube の地元オーク（Orient／Temple の森）」**（年代を言わない）

9. ❌ **「カーボン・ニュートラルだから CO2 を出していない」と言わない。**
   **2016 年に Écoact が認定した枠組み**であり、排出ゼロではない。
   ✅ 言ってよい: **「2016 年に地域で最初にカーボン・ニュートラル認定を取得したメゾン」**

10. ❌ **点数（96/100・98/100 など）や「世界 16 位」を自分の言葉で断定しない。**
    すべて**第三者の評価を公式が転載したもの**。
    ✅ 言ってよい: **「〜という評価が出ています」**と出所を付ける

11. 🔴 ❌ **`Père Pinot 2` を白ワインとして注がない。**
    **公式の色は「銅がかったロゼ（coppery rose）」。** OBP は BLENDS 節に置いている。
    ✅ **注ぐ前に色を伝える。「4 つの Pinot を等分した、銅色を帯びた 1 本です」**

12. ❌ **畑の面積を単一の数字で断定しない。**
    公式内で **62 ha 自社＋50 ha 契約（History 頁）／ 110 ha 超・うち 60 ha 自社（Nature 頁）／
    70 ha（Œnothèque FT）** と割れている。
    ✅ 言ってよい: **「自社畑と契約畑を合わせて 100 ha 超の規模」**

13. ❌ **`Grande Sendrée` を「有機認証ワイン」と言わない。**
    FT 2015 は当該区画が「2014 年から有機認証」と書くが、**サイトが有機の星印を付けているのは
    Clarevallis と Quattuor だけ**である。⚠️ 公式内で不整合。

14. ❌ **`Grande Sendrée` を「単一畑（single vineyard）」と断言しない。**
    **FT は "an archipelago of plots"（区画の群島）**と書く。
    ✅ 言ってよい: **「大火の灰を被った、隣接する区画の集まり」**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

**なし。**

（補足・衝突ではない: `producer:drappier` と重複しうる canonical レコードは検出されなかった。
既存の `/Users/akiomatsumoto/Theseus_Phase0/research/canonical_conflicts/REGISTER.md`
（真の衝突 9 件）にも Drappier / Urville / Les Riceys の項目は存在しない。
OBP 7 本目 `'Les Riceys,' Brut Nature` が `unresolved` なのは**キュヴェの被覆漏れ（coverage gap）**であって
**重複ではない** — canonical 側に対応するレコードがそもそも存在しない。
`Grand Sendrée` → `Grande Sendrée` はメニュー印字の綴り誤りであり alias で解決済み。
**REGISTER.md への追記は不要。**）

---

## Sources

**すべて公式一次資料。非公式ソース（Wikipedia・小売・EC・インポーター・レビュー集約）は一切使用していない。**

### 公式サイト `https://www.champagne-drappier.com`（2026-08-04 取得）

| ページ | ローカル |
|---|---|
| `/en/`（home） | `_sources/drappier/home_en.{html,txt}` |
| `/en/house/` | `page_house.{html,txt}` |
| `/en/history-family/` ／ `/fr/histoire-de-famille` | `page_history-family.*` ／ `fr_histoire-de-famille.*` |
| `/en/vineyard/` ／ `/fr/le-vignoble` | `page_vineyard.*` ／ `fr_le-vignoble.*` |
| `/en/work-cellar/` ／ `/fr/le-travail-en-cave` | `page_work-cellar.*` ／ `fr_cave.html` |
| `/en/nature-environment-and-carbon-neutrality/` ／ 仏語版 | `page_nature-...*` ／ `fr_nature.*` |
| `/en/champagnes/` | `page_champagnes.*` |
| `/en/loenotheque/` | `cuvee_loenotheque.*` |
| `/en/ephemeral-qualities/` ／ 仏語版 | `page_ephemeral-qualities.*` ／ `fr_eph.html` |
| `/en/clarevallis/` `/en/grande-sendree/` `/en/quattuor/` `/en/brut-nature-sans-soufre/` | `cuvee_*.{html,txt}` |
| `/en/news/` | `page_news.*` |
| ❌ `/en/eclose` `/en/les-riceys` `/en/rose-des-riceys` | **すべて 404**（`x_eclose.html` 他が証跡） |

### 公式テクニカルシート PDF（`/sites/drappier/files/…`）

`FT_grande_sendree_2015_en.pdf` ／ `FT_oenotheque_2005_en.pdf` ／ `FT_oenotheque_2007_en.pdf` ／
`FT_pere_pinot_2_en.pdf` ／ `FT_clarevallis_en.pdf` ／ `FT_carte_dor_en.pdf` ／
`FT_brut_nature_en.pdf` ／ `FT_brut_nature_sans_soufre_en.pdf` ／ `FT_quattuor_en.pdf` ／
`FT_rose_de_saignee_en.pdf` ／ `FT_millesime_exception_2019_en.pdf` ／ `FT_charles_de_gaulle_en.pdf`

### 公式ニュースレター「La Lettre」（公式サイト `/en/news/` から配布）

| 号 | 時期 | 本書で使った内容 |
|---|---|---|
| **N°66** | 2025 春（`2025-05/`） | Michel Drappier 署名の論説（シャンパーニュのドサージュ史・**Grande Sendrée は 70 年代生まれ**・**de Gaulle は Extra Dry 18 g/L**・**Hugo が DFM を使う**）／**Brut Nature Les Riceys の唯一の言及** |
| **N°67** | 2025 春（`2025-05/`） | 🔴 **André Drappier 追悼号**（Michel 署名）／**Hugo が The Drinks Business の 2025 Best Winemaker**／Grande Sendrée 2015・2012 と Quattuor が金賞 |
| **N°68** | 2025 秋冬（`2025-10/`） | シャンパーニュ UNESCO 登録 10 周年／**Urville の穹窿セラーが UNESCO インベントリ登録**／**仏国内が売上の 40%**／Le Jules Verne |
| **N°69** | **2026 春夏（`2026-04/`、最新号）** | 🔴 **André（1926-2025）逝去の明記**／🔴 **Hugo が現ワインメーカー**／🔴 **Éclose の唯一の一次記述**／補糖停止・ゼロドサージュ 40 年／コルク 390 g CO2／**2026 年 16 位** |

（EN / FR 両版を取得済み。**仏英で内容が食い違う箇所は本文中に ⚠️ で明示した。**）

---

## Confidence

| 節 | 判定 | 根拠 |
|---|---|---|
| **Identity** | **High** | 公式フッター・自称・家族構成すべて一次資料。現況（André 逝去 / Hugo 就任）は Lettre 67・69 で二重に確認 |
| **Overview** | **High** | 公式の自己記述に完全に依拠 |
| **History** | **High** | 年表のほぼ全項目が公式 History 頁＋Lettre で裏取り済み。世代の生年も公式記載 |
| **Location** | **High** | 住所・地区・土壌・品種比率すべて公式。区画名は Grande Sendrée / Cornellier のみ確認 |
| **Farming（実践）** | **High** | 除草剤不使用・馬耕・電動化・草生栽培は英仏両版で一致 |
| **Farming（有機認証の範囲）** | 🔴 **Low** | **公式内で 3 通りに矛盾。確定不能。⚠️ リスト 1 で運用回避** |
| **Farming（カーボン）** | **High** | 2016 / Écoact / 2,000 m² / 75% / 15% 軽量 / 390 g、すべて公式数値 |
| **Winemaking（共通工程）** | **High** | FT 12 種で反復確認。相互に整合 |
| **Winemaking（木・大瓶・Immersion）** | **High**（樽材の年代のみ ⚠️） | 英仏で 13 世紀 / 18 世紀が食い違う一点を除き一致 |
| **Style** | **High** | 色・泡・香りの記述はすべて公式の自己記述と FT |
| **Important Cuvées — Clarevallis / Père Pinot 2 / Œnothèque 2007** | **High** | **専用 FT があり、セパージュ・醸造・ドサージュ・デゴルジュマン日まで確定** |
| **Important Cuvées — Grande Sendrée 2010 / 2012** | **Medium-Low** | **当該ヴィンテージの FT が入手できない。**2015 の数値で代替してはならない |
| **Important Cuvées — Éclose** | **Low** | **FT・専用ページ無し。Lettre 69 の 1 段落のみ。ヴィンテージ不明** |
| **Important Cuvées — Les Riceys** | 🔴 **Low** | **公式に 1 行のみ。色・セパージュ・畑すべて不明。canonical 未登録** |
| **Staff Notes / ⚠️ リスト** | **High** | 全項目が公式内の矛盾または公式記述の直接の帰結 |
| **Canonical Conflict** | **High** | REGISTER.md を精査。Drappier に該当項目なし |
| | | |
| 🔴 **総合** | **Medium-High** | **70% 基準は満たす。** Identity / Overview / Location / Farming（実践）/ Winemaking / Style / OBP 紐付け / ⚠️ リストがすべて揃っている。**欠けているのは Grande Sendrée の該当ヴィンテージ FT、Éclose のヴィンテージ、Les Riceys の実体の 3 点のみ**であり、⚠️ リストでいずれも運用上カバー済み |

**reached_70: true**

---

## Open Questions

1. ❓ 🔴 **有機認証の実際の範囲は何 ha か。**
   仏語 vineyard 頁「100%」／英語 vineyard 頁「27 ha」／nature 頁「17 ha 認証＋10 ha 転換中」が矛盾する。
   さらに Grande Sendrée FT は当該区画が「2014 年から認証」と書くが、サイトの有機星印は Clarevallis と
   Quattuor のみ。**Ecocert の認証書か、生産者への直接照会が要る。**

2. ❓ 🔴 **`Elysé Brigandat` は現在も Cellar Master か。**
   公式サイト `/en/work-cellar/` は Cellar Master として記載するが、同ページ本文は André 存命を前提としており
   更新されていない。Lettre 69 は Hugo Drappier を "the house winemaker" とする。
   **両者の職掌の関係（chef de cave と winemaker）が公式に整理されていない。**

3. ❓ 🔴 **`Grande Sendrée` **2010** および **2012** の公式テクニカルシートが存在するか。**
   公式サイトが掲載しているのは 2015 のみ。**OBP はこの 2 ヴィンテージを $395 / $400 で売っているのに、
   セパージュも熟成期間もドサージュも公式で裏が取れない。**生産者に FT を請求すべき最優先項目。

4. ❓ 🔴 **`Éclose` のヴィンテージは何年か。**
   公式 Lettre 69 はヴィンテージを書いていない。OBP / canonical は 2012 とするが、
   **2012 は Ovum が到着した年**であり、混同の可能性がある。
   併せて **Éclose は Grande Sendrée の区画から来ているのか**（Lettre 69 は "the finest terroir of the Sendré"、
   サイトは Ovum が "premium Grande Sendrée" を収めるとする）も未確定。**$1,520 の 1 本として要確認。**

5. ❓ 🔴 **`Brut Nature Les Riceys` とは何か。**
   公式の言及は Lettre 66 の 1 行のみ。**色（OBP はロゼ節に置く）・セパージュ・畑・ヴィンテージが全て不明。**
   canonical にレコードが無い。**このボトルは現状、ソムリエが語れる公式情報をほぼ持たない。**

6. ❓ **`Réserve de L'Œnothèque` の各ヴィンテージの生産本数。**
   公式は「小ロット、時には 1 本だけデゴルジュマンする」と書くのみで、2007 の本数は非公表。

7. ❓ **樽材の森の年代**（テンプル騎士団は 13 世紀か 18 世紀か）。仏語版が整合的だが、
   英語版は未訂正のまま。**公式に訂正を求めるべき軽微な誤訳。**

8. ❓ **`Ovum` の容量表記。** 公式は `3.342 litres` と書く（仏語版も同表記）。
   **3,342 L の桁区切りと解するのが自然だが、公式が明示的に単位を確認していない。**
