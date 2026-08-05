# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:larmandier-bernier` および配下 3 キュヴェは一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト larmandier.fr で確認**（一次資料）
> `📄` 提供資料のみに基づく（公式未確認）／ `⚠️` 食い違い。両方を残す
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 一次資料: `https://larmandier.fr/` **en / fr 両言語で 14 ページ ＋ 公式 PDF 1 点**
> `/en/` `/en/our-domain/` `/en/our-know-how/` `/en/our-champagnes/`
> `/en/our-champagnes/latitude/` `/longitude/` `/vieille-vigne-du-levant/` `/terre-de-vertus/`
> `/chemins-avize/` `/rose-de-saignee/` `/cramant-nature/` `/vertus-rouge/`
> `/en/visits-contact/` `/fr/vinotheque/` ／ ブログ `Récolte 2025`（2025-10-07）・`Non, nous n'avons rien oublié !`（2024-09-13）
> 公式 PDF: `wp-content/uploads/2019/05/tour-Larmandier-Bernier-vineyards.pdf` → `_sources/larmandier-bernier/tour-vineyards.pdf`
>
> ⚠️ **キュヴェ別テクニカルシート PDF は存在しない。**`page-sitemap.xml` 全 40 URL と全 HTML の `href="*.pdf"` を
> 総当たりした結果、サイト内の PDF は上記の畑めぐり地図 1 点のみ。**ただし技術情報はテクニカルシートの代わりに
> 各キュヴェページ本文に直接埋め込まれている**（品種比率・リザーヴ比率・ドサージュ g/l・熟成年数・デゴルジュマン時期）。
> Louis Latour 型（PDF あり）でも Leflaive 型（技術情報なし）でもない**第三の型**。
>
> ⚠️ **FR 版と EN 版で内容が食い違う箇所がある。**EN は FR からの翻訳で、翻訳時に脱落した情報がある
> （§Location のグラン・クリュ村リスト）。**FR を一次、EN を二次として扱った。**

---

## 🔴 統合禁止境界（intake の保護境界。canonical 昇格時に必ず参照）

| これ | ≠ | あれ |
|---|---|---|
| **Larmandier-Bernier**（本書。Vertus。Pierre & Sophie Larmandier） | ≠ | **Guy Larmandier**（同じく Vertus の別 RM。canonical 未登録・OBP 掲載なし）🔍 |
| **Larmandier-Bernier** | ≠ | **Larmandier Frères**（Cramant の別 RM。canonical 未登録・OBP 掲載なし）🔍 |
| **Vieille Vigne du Levant**（Cramant GC・単一区画） | ≠ | **Les Chemins d'Avize**（Avize GC・単一区画）／ **Terre de Vertus**（Vertus 1er・単一区画） |
| **Cramant Nature**（Coteaux Champenois **白**・泡なし） | ≠ | **Vieille Vigne du Levant**（同じ Cramant のシャンパーニュ） |

⚠️ **`Larmandier` 姓は Côte des Blancs に複数の独立生産者がいる。**現時点で canonical に登録されているのは
`producer:larmandier-bernier` **1 件のみ**（下記 §Canonical Conflict で全 384 生産者を走査済み）。
**将来 `Guy Larmandier` / `Larmandier Frères` を intake する際、姓トークン `larmandier` だけで
本レコードに吸着させてはならない。**（REGISTER.md P-2 Famille Mousse / Mousse Fils と同型のリスク）

---

## Identity

| | |
|---|---|
| **Canonical Name** | Larmandier-Bernier |
| **公式表記** | **Champagne Larmandier-Bernier** ✅（ラベル・footer とも） |
| **Aliases** | ❓ canonical `aliases` は空。`legacy_ids` 3 件（`larmandier-latitude` / `larmandier-longitude` / `larmandier-levant-2014`） |
| **業態** | **RM（récoltant-manipulant／家族経営ドメーヌ）** — ✅ **「ブドウは一切買わない」と公式に明記** |
| **所在** | **19, avenue du Général de Gaulle, 51130 VERTUS** ✅ |
| **GPS** | 48°53′50″N / 4°00′40″E ✅（`/en/visits-contact/`。公式 PDF では 4°00′41″E ⚠️ 誤差レベル・無視可） |
| **現運営** | **Pierre Larmandier（1988〜）／ Sophie Larmandier（1988〜）／ Arthur Larmandier（2017〜）／ Georges Larmandier（2021〜）** の 4 名 ✅ |
| **現況の確認日** | ✅ **2025-10-07 付ブログ記事の署名が「Georges, Arthur, Pierre & Sophie」** — 4 名体制は 2025 年 10 月時点で現行と確認済み |
| **醸造責任者（chef de cave）** | ❓ **公式サイトに職名も個人名も存在しない。**4 名の家族が「vignerons」として記載されるのみ |
| canonical id | `producer:larmandier-bernier` |
| canonical entity confidence | 0.2（`legacy_app`）— エンティティ同定の確度。本書の充実度とは別軸 |

---

## Overview

✅ **コート・デ・ブランの Vertus に本拠を置く RM（栽培家兼醸造家）。**Larmandier 家は**フランス革命期からコート・デ・ブランのシャンパーニュの評価に寄与してきた 8 世代**の家系で、ブドウ栽培そのものは **Larmandier 家と Bernier 家双方で 1765 年から**記録されている。ただし **Larmandier-Bernier という名のシャンパーニュは 1971 年、Philippe Larmandier と Vertus に畑を持つ Elisabeth Bernier の結婚によって生まれた**。

✅ **自社畑 19 ha のみ。ブドウは一切買わない。**「醸造は、ブドウへの全幅の信頼なしには同じものにならない」という理由による。**シャルドネが 90% 超**、平均樹齢 35 年、**Larmandier 家と Bernier 家の祖父たちが行ったマサル・セレクション由来**。

✅ **ビオディナミの代表格。**1992 年に Pierre が除草剤を完全放棄、**1999 年に全所有畑をビオディナミへ移行し、同年から野生酵母（levures indigènes）と木樽での醸造を開始。オーガニック認証は 2003 年取得。**「20 年以上のビオディナミ」を公式に掲げる。

✅ **エクストラ・ブリュットの旗手。**「通常のブリュットのドサージュが 12 g/l 前後であるのに対し、当家のキュヴェは 3 g を超えない」と公式に宣言し、実際の公表値は **Latitude / Longitude / Vieille Vigne du Levant / Les Chemins d'Avize / Rosé de Saignée がすべて 2 g/l、Terre de Vertus は 0 g/l**。

✅ **Robert Parker Green Emblem（持続可能性に対する顕彰）の最初の 24 生産者の 1 つ。**

---

## History

### 公式年表（`/fr/maison-larmandier/`「Chronologie」＋「Philosophie」の 2 系統を統合）✅

| 年 | 出来事 | |
|---|---|---|
| **1765** | **Larmandier 家・Bernier 家双方の歴史に「ブドウを耕すこと」が記される起点** | ✅ |
| 1856 | **Louis Prosper Larmandier**（Pierre の高祖父／great-great-grandfather）が両親の記憶を語る:「1856 年の収穫は 1 エーカーあたり平均 10 樽。少なく見えるが、当時はアメリカ台木も肥料すら無かった。土と太陽だけがブドウを養っていた」 | ✅ |
| 1925 | **「呪われた年」。Jules Larmandier**（Pierre の曾祖父）が記者の取材に応じ、**Cramant の「美しい Côte de Saran」から「Vertus の側にまで」及んだブドウノメイガ（cochylis）の被害**を語る | ✅ |
| 1950 | **「パリの時代」。**Jules Larmandier、続いてその息子 **Philippe Allyre Larmandier** が**パリの名店（La Tour d'Argent / Taillevent / Charlot roi des coquillages 等）への供給者となる** | ✅ |
| **1971** | **LARMANDIER-BERNIER 創設。**Philippe Larmandier が、**Vertus に畑を所有する妻 Elisabeth Bernier** とともにブランドを立ち上げ、**Vertus にセラーを建設** | ✅ |
| **1988** | **Pierre**（Philippe と Elisabeth の息子）が**父の早すぎる死**を受けて家業に戻り、母を支える。同年 **Sophie と結婚**。土を耕し除草剤を捨て、各テロワールに息を吹き込む | ✅ |
| **1988** | **単一区画キュヴェの系譜が始まる — `Vieille Vigne de Cramant`（現 Vieille Vigne du Levant）誕生** | ✅ |
| **1992** | **除草剤を全面的かつ決定的に放棄** | ✅ |
| **1995** | **`Terre de Vertus` — Les Barillers 区画の単独醸造を開始** | ✅ |
| **1999** | **全所有畑でビオディナミを実践。発酵に野生酵母を使用。木樽での醸造を開始。** ステンレスでの古典的熟成では表現しきれなくなったため、Pierre は畑で始めた仕事を樽・フードルでの熟成へ延長する | ✅ |
| 1999 | **`Rosé de Saignée` 開始**（単一区画系譜の 3 つ目） | ✅ |
| **2002** | **Vertus に 4 ha（＝10 エーカー）を買い増し。**この畑は**耕され、除草剤も gadoues（都市ゴミ堆肥）も一度も使われたことがない** | ✅ |
| **2003** | **オーガニック認証（BIO）取得。**同年 `Classement des Meilleurs Vins de France` で 1 つ星 → 2 つ星、Revue du Vin de France「2002 年最も将来を嘱望されるワイン」、GaultMillau / Bernard Burtschy「2003 年の Winegrower of the year」、Bettane & Desseauve 4 BD | ✅ |
| **2009** | **小型プレス機の導入により、Avize の 2 区画を分離醸造できるようになる** → `Les Chemins d'Avize` へ | ✅ |
| **2010** | **Chai（醸造棟）建設。**収穫全量を木で熟成し、さらにセラーでの熟成を延長するため。樽・木製フードルの増設 | ✅ |
| **2017** | **Arthur Larmandier**（Rennes Business School 卒、国際経験を経て）が両親に合流 | ✅ |
| **2018** | **Avize に新たな畑を取得。**「収穫をコントロールし続けるためにブドウは決して買わない。最上のクリュで畑を買うことによって未来を書き続ける」 | ✅ |
| **2021** | **Georges Larmandier** が合流。Supélec 卒後、**航空エンジニアとして 3 年勤務**してから家業へ | ✅ |
| **2024/9** | **キャップシール（coiffe）を廃止。**EU 法の改正で無キャップシール販売が可能になったことを受けた選択 | ✅ |
| **2025** | **新しい Chai を建設 — 木樽でのより長い élevage を可能にするため** | ✅ |
| **2025/10** | 2025 年収穫を総括する記事を Georges・Arthur・Pierre・Sophie の 4 名連名で公開 | ✅ |

### 世代 ✅

| 代 | 人物 | |
|---|---|---|
| — | **Louis Prosper Larmandier** | Pierre の**高祖父**（great-great-grandfather）。1856 年の証言 |
| — | **Jules Larmandier** | Pierre の**曾祖父**。1925 年の証言／パリの名店への供給を開始 |
| — | **Philippe Allyre Larmandier** | Jules の息子。パリ供給を継承 |
| — | **Philippe Larmandier ＋ Elisabeth Bernier** | **1971 年に Larmandier-Bernier を創設。**Elisabeth が Vertus の畑をもたらした |
| 現 | **Pierre Larmandier**（Vertus 生まれ、Audencia ナント商科大学卒） | 1988〜。ビオディナミ転換の当事者 |
| 現 | **Sophie Larmandier**（**Avize 出身**、École Centrale de Lyon 卒） | 1988〜。「環境への敬意と健康な食」という生き方がビオディナミ転換のもう一つの起点 |
| 次 | **Arthur Larmandier** | 2017〜 |
| 次 | **Georges Larmandier** | 2021〜。元・航空エンジニア |

❓ **各人物の生没年は公式サイトに一切記載がない。**Philippe Larmandier の没年（1988 年の「父の早すぎる死」）も年としては明示されていない。
⚠️ 「Philippe Allyre Larmandier」と「1971 年の Philippe Larmandier」が**同一人物か父子かは公式からは断定できない。**年表の流れ（1950 年に Jules の息子として登場 → 1971 年に創設 → 1988 年に息子 Pierre が継承）からは**同一人物である蓋然性が高いが、公式は "Philippe Allyre" と "Philippe" を別表記のまま置いている。** ❓

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Champagne ✅ |
| **Sub-region** | **Côte des Blancs** ✅ |
| **Village（本拠）** | **Vertus**（Premier Cru）✅ — セラーは 1971 年に Vertus に建設 ✅ |
| **地質** | ✅ **カンパニアン期のチョーク（craie du campanien）が露出**。公式は「シャンパーニュの全生産地区のうち、**Montagne de Reims と Côte des Blancs だけがこのカンパニアン・チョークの上にある**」と明記し、これが自社ワインのミネラル感の根源だとする |
| **セラー** | **チョークを掘り抜いた地下蔵**（caves creusées dans la craie）✅ |
| **面積** | **19 ha**（FR）＝ **47 acres**（EN）✅ **両言語で一致** |
| **平均樹齢** | **35 年** ✅ |
| **品種構成** | **シャルドネ 90% 超** ✅／ **ピノ・ノワールは畑の 5%**（2025 年収穫記事）✅／ **ピノ・グリ**も少量 ✅ |

### ⚠️ グラン・クリュ村リスト — 公式内で 3 通りに食い違う。**消さずに全部残す**

| 出典（すべて公式） | 記載 |
|---|---|
| `/fr/savoir-faire-vigneron/`（**FR・最も網羅的**） | 「Vertus classé Premier Cru et **Cramant, Chouilly, Oger, Avize**, tous classés Grands Crus」＝ **GC 4 村** |
| `/en/our-know-how/`（EN 訳） | 「Vertus, classified Premier Cru and **Cramant, Chouilly and Avize**」＝ **GC 3 村（Oger が脱落）** |
| `/fr/maison-larmandier/` ＋ `/en/our-domain/` | 「Grands crus : **Cramant, Avize, Oger** et 1er cru Vertus」＝ **GC 3 村（Chouilly が脱落）** |
| `/en/our-champagnes/longitude/`（キュヴェページ） | Longitude の構成村として「**Vertus, Oger, Avize, Cramant**」（Chouilly なし） |

**採用: Vertus（1er Cru）＋ Cramant / Chouilly / Oger / Avize（すべて Grand Cru）** — FR 版 Know-How が**唯一 4 村すべてを含む上位集合**であり、他 3 つはその部分集合。EN 版は FR からの翻訳時の脱落と判断する。
🔍 **参考: canonical の Longitude `subregion` は「Vertus / Oger / Avize / Cramant」で、Chouilly を含まない。**上記の食い違いをそのまま継承している。
⚠️ **現場では村数を断定しない。**§Staff Notes 参照。

### Key Vineyards ✅

**Vertus（Premier Cru）— 公式 PDF「Tour the Larmandier-Bernier vineyards」に自社看板つきで実名表示される区画**

| 区画 | 備考 |
|---|---|
| **Croix Saint Ladre** | Vertus を出た右手。Know-How ページの写真キャプションにも登場 |
| **Grillettes** | Vertus 教会の眺望 |
| **Plisson（Plissons）** | Chemin Plisson を 800 m。徒歩コースの起点 |
| **Le Lièvre** | |
| **Grand Mont** | Mont Aimé とシャンパーニュ平野の眺望 |
| **Belval** | |
| **Les Barilliers**（地図番号 7・8・9） | ⚠️ **`Terre de Vertus` ページでは「Les Barillers」表記**（l が 1 つ）。**両方公式。両方残す** |
| **Les Faucherets**（10・11） | 自社看板あり |
| **La Justice**（12） | |
| **Les Mazaux**（13） | Le Mesnil-sur-Oger 方面 |

**Cramant（Grand Cru）**
- ✅ **`Bourron du Levant`** — 東〜南東向きの単一区画。**「Levant」は東を意味し、朝の最初の陽を受ける。**Cramant では**斜面の反対側（西向き）の畑とはまったく別物**で、東向き側は「特にリッチでパワフルな」ブドウを生む。樹齢 **60 年〜85 年超**。→ `Vieille Vigne du Levant`
- 🔴 **canonical の記述誤り**: `cuvee:larmandier-bernier-vieille-vigne-du-levant-grand-cru-extra-brut` の `terroir`（日本語）は区画名を**「ブロン・デュ・ルヴァン」**と書いているが、**公式の綴りは `Bourron`（ブーロン）**。canonical 側の転記誤り。**現場で「ブロン」と言わない。**（canonical は書き換えていない）

**Avize（Grand Cru）**
- ✅ **`Chemin de Plivot` と `Chemin de Flavigny`** の 2 区画。**Avize 村の中心部**。**土壌は非常に痩せ、チョークが露出。樹齢 65 年。**2009 年に小型プレス導入で分離可能になった → `Les Chemins d'Avize`

**Chouilly / Oger（Grand Cru）**
- ❓ **区画名は公式に記載なし。**Longitude のアッサンブラージュに入る村としてのみ言及される（Oger）／ Know-How FR の村リストにのみ登場（Chouilly）

---

## Farming

| 項目 | 内容 | |
|---|---|---|
| **ビオディナミ** | **1999 年から全所有畑。**「20 年以上」 | ✅ |
| **除草剤** | **1992 年に全面的・決定的に放棄** | ✅ |
| **農薬** | **「0% pesticides」と公式に明記** | ✅ |
| **オーガニック認証** | **「certifié BIO depuis 2003」＝ 2003 年からオーガニック認証** | ✅ |
| 🔴 **認証機関** | ❓ **公式サイトに認証機関名が一切出てこない。**`Demeter` `Biodyvin` `Ecocert` いずれの語も**全 14 ページ中 0 回**。**ビオディナミ「認証」を受けているかどうかも公式は述べていない**（述べているのは「ビオディナミを実践している」ことと「BIO 認証を持っている」ことの 2 点のみ） | ❓ |
| **耕耘** | **軽い犂耕（labour）。**深根化を促し土壌の生命を保つため。「そうすることで収量は自然に抑えられ、ワインは構造と成熟でそれを返す」 | ✅ |
| **収量** | 「rendements mesurés（節度ある収量）」— **数値は非公表** ❓ | ✅／❓ |
| **樹齢・遺伝資源** | 平均 35 年。**Larmandier 家と Bernier 家の祖父たちによるマサル・セレクション由来**。公式は「真の自然遺産（véritable patrimoine naturel）」と呼び、**vieilles vignes の保全**を明示的な方針とする | ✅ |
| **収穫** | **常に手摘み。「完全に熟した時＝味が良く複雑さを示す時」に摘む。**通常 9〜10 月だが、気候変動により 8 月末に鋏が入ることもある | ✅ |
| **ブドウの購入** | **一切なし** | ✅ |
| **持続可能性の外部評価** | **Robert Parker Green Emblem — 最初の 24 生産者の 1 つ** | ✅ |
| **包装** | **2024 年 9 月よりキャップシール（coiffe）を廃止。**EU 法改正を受け、「最良の廃棄物は存在しない廃棄物」「常に簡素さの中に瓶の優雅さを求めてきた」という理由。**瓶は「délicat tour de col（繊細な首まわり）」を露わにする** | ✅ |
| **その他** | 蔵に**EV 充電スタンド**を設置 | ✅ |

### 2025 年ヴィンテージの実況（現場で使える最新情報）✅
2025-10-07 付の公式記事より:
- **8 月に糖度が週 2 度超のペースで上昇（前例なし）**。コート・デ・ブランの ban des vendanges は **8 月 26 日**に解禁されたが、**Larmandier-Bernier は「果皮がまだ金色で透明になっておらず、香りの複雑さが来ていない」として 1 週間待ち、9 月初めに開始した。**
- **量は大幅な期待割れ。**2024 年 6 月の花芽分化不良で房数が少なく、加えて 5 月末の数日間の冷え込みで**房の重さが見込みを大きく下回った**。「房は美しいが、重さがない」。
- **春はシャンパーニュで特に乾燥。**公式は「**有機農法とビオディナミによる土壌への敬意**が、わずかな水を保持し干ばつの影響を抑えた」と自己評価。
- **ピノ・ノワールは開花条件が良好。**Rosé de Saignée 用に良い収穫。**Coteaux Champenois 赤用の古木ピノ・ノワールは 2025 年で樹齢 65 年。**
- 総括: **「degrés は高いが過剰でなく、健全度は完璧以上。忍耐は報われた」「大いなるミレジムへ向かって」**。野生酵母による発酵はフードルと樽で速やかに始動。

---

## Winemaking

| 工程 | 内容 | |
|---|---|---|
| **圧搾** | **空気圧プレスで穏やかに**。「最も純粋な果汁を取り出すため」。**クリュごと・品種ごと・区画ごとに別々に醸造** | ✅ |
| **デブルバージュ** | **ごく軽くしか清澄しない**（"clarified very slightly"） | ✅ |
| **アルコール発酵** | **野生酵母（levures indigènes）100%、1999 年から。**「収穫ごと、樽ごと、フードルごとに、それぞれの酵母で、それぞれの生を生きる」 | ✅ |
| **発酵容器** | **収穫全量が木**（fûts と foudres）。**Stockinger 社製**を選択 — 「**繊細なトースティングがワインを尊重する**」ため | ✅ |
| **MLF** | 🔴 **マロラクティック発酵は自然に開始する（"begin spontaneously"）。ブロックしない。**Latitude / Longitude / VVdL / Terre de Vertus / Les Chemins d'Avize の全キュヴェページに同一の記述 | ✅ |
| **シュール・リー熟成（1 次）** | **約 1 年／公式の別表記では 11 か月**。**澱引きなし（no racking）** | ✅ |
| **清澄・濾過** | **無濾過・無清澄（ni filtration ni collage）** | ✅ |
| **永久リザーヴ** | **2004 年開始。毎年新しいヴィンテージで補充される perpetual reserve。**Latitude と Longitude に **40%** 使用 | ✅ |
| **アッサンブラージュ** | **1 年後の家族試飲で決定。**単一区画で完結する場合は parcellaire（Terre de Vertus / Vieille Vigne du Levant / Les Chemins d'Avize）、調和する場合はブレンド（Latitude / Longitude） | ✅ |
| **ティラージュ・瓶詰** | **7 月末頃**。ただちにセラーへ降ろす | ✅ |
| **2 次発酵・セラー熟成** | **チョークを掘り抜いた地下蔵で、ゆっくり。「3 年から 10 年」が経過する** | ✅ |
| **ルミュアージュ** | **手動** | ✅ |
| **デゴルジュマン** | **手動（à la volée）** | ✅ |
| **ドサージュ** | **極小。**§下の ⚠️ 参照 | ✅ |
| **コンクリート・エッグ** | **Rosé de Saignée の 1 次発酵にタンクまたはコンクリート・エッグを使用** | ✅ |

### ⚠️ ドサージュ上限 — 公式内で 2 通り。**両方残す**

| 出典（両方公式） | 記載 |
|---|---|
| `/en/our-know-how/` ＋ `/fr/savoir-faire-vigneron/` | 「**never go above 3 g/l** / **les cuvées ne dépassent pas les 3 g**」 |
| 各キュヴェページ内「Dosage / Le Dosage」ボックス（VVdL・Terre de Vertus 等） | 「**we never go above 4 g/l** / **nous ne dépassons pas les 4 g**」 |

**採用: 「3 g/l を超えない」（Know-How ページ＝製法の正典セクション）。ただし現場では上限値を言わず、実測値を言え。**
✅ **公表されている実際のドサージュはすべて 2 g/l または 0 g/l**（下表）。この事実の方が強く、かつ食い違いを回避できる。
✅ 公式は「**一般的にはおよそ 1 g の天然残糖が残る**」とも述べる。
✅ 思想: 「**デゴルジュマン時に砂糖を足してシャンパーニュを重くし、テロワールから遠ざかるリスクを冒すより、ブドウの熟度とその天然糖を優先する**」。

### ❓ 公式に存在しない数値（**創作するな**）
- **新樽比率**（Stockinger の樽・フードルとしか書かれず、新樽比率も樽サイズも樽/フードルの比率も非公表）
- **収量（hl/ha）**・**圧搾歩留まり**
- **各村ごとの所有面積の内訳**（19 ha の内訳は一切非公表）
- **Latitude / Longitude のリザーヴワインの平均年齢**（40% という比率のみ）
- **各キュヴェの年産本数**

---

## Style

✅ **公式の自称（footer に常設・全ページ共通）**:
> 「Des grands crus cultivés en bio, un travail précis et patient, de beaux raisins mûrs pour des vins purs et minéraux, des vins vrais.」
> ＝ **有機で育てたグラン・クリュ、精緻で忍耐強い仕事、美しく熟した果実から、純粋でミネラルな、本物のワインを。**

✅ **ハウス・モットー（トップページの第一メッセージ）**:
> 「Good Champagnes conform to the rules. Really great Champagnes often break them.」
> 「Un bon champagne se conforme aux règles d'élaboration. C'est en brisant les règles que naît un grand champagne !」
> ＝ **良いシャンパーニュは規則に従う。本当に偉大なシャンパーニュは、しばしばそれを破る。**

✅ **公式が繰り返す 3 語**: **maturité（成熟）／ minéralité（ミネラリティ）／ pureté（純粋さ）**。「テロワールに最も近い」。

✅ **公式の哲学の中核（`/en/our-domain/` より）**:
> 「方法論を押しつけようという話ではない。Sophie、Pierre、Arthur、Georges はただ**正しく、良くやりたい**だけだ。彼らは**違っていてよい権利**を、**紋切り型ではないワインを作る権利**を主張する。**自分たちを差別化しようとしてではなく。**」
> 「ブドウは、**いかなる人間にも発明できない真正性のすべてを、自ずから内に宿している。**」
> ✅ テロワール＝楽譜、ブドウ樹＝楽器、栽培者＝演奏家という比喩を公式が用いる。「**楽譜だけでは足りない**」。

✅ **野生酵母についての公式の主張（これがこの蔵の立ち位置を最も鋭く表す）**:
> 「今日、シャンパーニュの **99% は市販酵母**で造られる。品質は非常に良いが、**味の均一化に寄与している**。」
> 「テロワールの野生酵母は、良いワインを造るのに絶対必要か？ **否。** 偉大なワインを造るのに絶対必要か？ **然り。**なぜなら偉大なワインは必然的に偉大なテロワールに結びついており、**酵母はその方程式の本質的要素だからだ。**」

📄 **第三者評価（公式サイトが自ら転載しているもののみ）** — 出典は公式サイト上の Revue de Presse
- ✅ Andrew Jefford, *The New France*（2003 年欄に引用）:「シャンパーニュにおいて、Larmandier-Bernier ほど一貫して傑出したレンジを持つ生産者は**ほとんどいない**」
- 📄 Bettane & Desseauve **4 BD**／`Classement des Meilleurs Vins de France` **2 つ星**（2003 年時点）
- 📄 `Les Meilleurs Vins – Le Guide 2026` **★★★★**:「**全地域を通じて、これほどの高水準での安定を誇れるドメーヌはほとんどない。レンジは驚くほど揃っており、しかも手頃な価格で提供されている**」
- 📄 Vinous / Antonio Galloni 2025:Latitude **94**、Rosé de Saignée **93**、Vieilles Vignes du Levant 2015 **96**
- 📄 Wine Advocate 2023-12:Longitude **92**

---

## Important Cuvées

### 🔴 OBP 掲載分（3 本。**すべて canonical 登録済・未解決 0**）🔍

| OBP 印字 | VT | 価格 | canonical cuvée id | 状態 |
|---|---|---|---|---|
| **'Latitude,' Premier Cru Extra Brut** | NV | **$220** | `cuvee:larmandier-bernier-latitude-extra-brut` | ✅ **登録済**（`state=alias`, flags なし） |
| **'Longitude,' Premier Cru Extra Brut** | NV | **$240** | `cuvee:larmandier-bernier-longitude-extra-brut-premier-cru` | ✅ **登録済**（`state=alias`, flags なし） |
| **'Vieille Vigne du Levant,' Grand Cru Extra Brut** | **2014** | **$535** | `cuvee:larmandier-bernier-vieille-vigne-du-levant-grand-cru-extra-brut` | ✅ **登録済**（`state=alias`, flags なし） |

🔍 いずれも OBP セクションは `FRANCE | SPARKLING > CHAMPAGNE | BLANC DE BLANCS`。
✅ **3 本すべて 100% シャルドネであり、Blanc de Blancs 分類は正しい。**

### ⚠️ OBP 印字と公式ラベルの食い違い — **Latitude の「Premier Cru」**

| | |
|---|---|
| **OBP 印字** | 「'Latitude,' **Premier Cru** Extra Brut」 |
| **canonical** | `subregion: Côte des Blancs — **Vertus Premier Cru**`／`tags` に **"Premier Cru"** |
| **公式ページ見出し** | 「**Champagne Extra Brut**」— **Premier Cru の表記なし** ✅ |
| **公式 FR URL slug** | `/fr/champagnes/**latitude-extra-brut**/` — cru 表記なし ✅ |
| **比較: Longitude** | 見出し「Champagne **Premier Cru** \| Extra Brut」／slug `longitude-**premier-cru**-extra-brut` ✅ |
| **比較: Terre de Vertus / Rosé de Saignée** | いずれも見出し・slug ともに **Premier Cru を明示** ✅ |
| **比較: VVdL / Les Chemins d'Avize / Cramant Nature** | いずれも **Grand Cru を明示** ✅ |

**判定: 公式は Latitude にだけ意図的に cru 表記を付けていない。**Vertus は Premier Cru なので**格として誤りではない**が、**ラベルにそう書かれている保証はない。**
（Vinous のレビューは「Latitude 1er Cru」と書いているが、これは第三者の記述であり公式ではない。📄）
→ **§Staff Notes ⚠️ リスト参照。**

### OBP 3 本の技術詳細 ✅

| | **Latitude** | **Longitude** | **Vieille Vigne du Levant** |
|---|---|---|---|
| 格付 | ⚠️ 公式は cru 表記なし（Vertus＝1er Cru） | **Premier Cru** | **Grand Cru** |
| 品種 | **Chardonnay 100%** | **Chardonnay 100%** | **Chardonnay 100%** |
| 産地 | **Vertus 南部のみ**（＝同じ「緯度」） | **Vertus / Oger / Avize / Cramant**（＝東経 4 度線付近＝同じ「経度」） | **Cramant 100%・単一区画 `Bourron du Levant`** |
| 樹齢 | ❓非公表 | ❓非公表 | **60 年〜85 年超** |
| ヴィンテージ | **NV**（リザーヴ 40%、2004 年開始の永久リザーヴ） | **NV**（リザーヴ 40%、同上） | **ミレジム（単一年）・単一区画。他年・他テロワールとの一切のブレンドなし** |
| 発酵 | 木（Stockinger の fût / foudre）・野生酵母・MLF 自然発動 | 同左 | 同左 |
| 1 次熟成 | シュール・リー 1 年、無濾過・無清澄 | 同左 | 同左 |
| ティラージュ | 7 月 | 7 月 | 7 月 |
| 2 次熟成 | **最低さらに 2 年** | **最低さらに 2 年** | 🔴 **さらに約 9 年** |
| デゴルジュマン | **手動。出荷の 9 か月前** | **手動。出荷の 9 か月前** | **手動。出荷の 1 年前** |
| ドサージュ | **2 g/l** | **2 g/l** | **2 g/l** |
| 旧名 | **`Tradition`**（1970 年代に Pierre の両親が命名） | **`Blanc de Blancs`**（20 世紀初頭から） | **`Vieille Vigne de Cramant`**（1988 年創設時）→ **Cramant と crémant の混同を避けるため改名** |
| 公式の飲み頃 | 「今飲めるが 2〜3 年置いてもよい」 | 「今飲めるが数年寝かせてもよい」 | 「**開くのに時間を要する。**2 年は置くべき（深みを増す）、もっと長くてもよい」 |
| 公式の性格 | **Harmony and roundness** — 「一日（あるいは一夜）のどの時間にも魅力的」。豊かで華やか、祝祭のシャンパーニュ | **Superbly fresh and mineral** — 「アペリティフに完璧。**まっすぐさとミネラル**が食欲を開く」 | **A deep, intense wine** — ヴォリューム・リッチネス・ミネラリティと**非常に長い余韻** |
| 公式のペアリング | （記載なし） | （記載なし） | **アペリティフ／モリーユ茸を添えた家禽／クリームを使った料理**に「堂々と拮抗する」 |
| 蔵元価格（参考・仏国内 TTC） | **58€/btl・122€/magnum・345€/Jeroboam** | **68€/btl・142€/magnum** | **148€/btl・302€/magnum（2015）** |
| **OBP 価格** | **$220** | **$240** | **$535** |

✅ **Latitude / Longitude の命名の由来（これが最強の説明材料）**
- **Latitude**＝「この**緯度**、Vertus の南では、テロワールが豊かで、とても丸いシャルドネが生まれる」
- **Longitude**＝「**Longitude は長さを意味し**、チョークがほぼ露出しているコート・デ・ブランの偉大なテロワール由来の、**非常にピュアでまっすぐなスタイル**を表す」。構成 4 村は「**第 4 子午線（4th meridian）の近くで一本の線をなす**」

### 公式レンジ全 8 種（OBP 非掲載分＝Packet A 候補）✅🔍

| キュヴェ | 格付 | 内容 | canonical |
|---|---|---|---|
| **Latitude** | ⚠️ cru 表記なし | Chardonnay 100%・Vertus 南部・2 g/l | ✅ 登録済（OBP） |
| **Longitude** | Premier Cru | Chardonnay 100%・4 村・2 g/l | ✅ 登録済（OBP） |
| **Vieille Vigne du Levant** | Grand Cru | Chardonnay 100%・Cramant 単一区画・ミレジム・2 g/l | ✅ 登録済（OBP） |
| **Les Chemins d'Avize** | Grand Cru | Chardonnay 100%・**Avize の 2 区画（Chemin de Plivot / Chemin de Flavigny）**・樹齢 65 年・**ティラージュ後 9 年以上**・出荷 1 年前に手動デゴルジュマン・**2 g/l**。**2009 年に小型プレス導入で分離**。Vinothèque で **2014 = 160€** | 🔍 **canonical 未登録** |
| **Terre de Vertus** | Premier Cru **Non Dosé** | Chardonnay 100%・**Vertus の区画 `Les Barillers`・1995 年から単独醸造**・ミレジム・**ティラージュ後 6 年以上**・出荷 1 年前に手動デゴルジュマン・**0 g/l**。Vinothèque で **2015 = 110€/btl、2014 = 205€/magnum** | 🔍 **canonical 未登録** |
| **Rosé de Saignée** | Premier Cru Extra Brut | **Pinot Noir 90% / Pinot Gris 10%**（Vertus の同一区画に**混植された古木**）・**選果台 → 部分除梗 → 2〜3 日のマセラシオン**・タンクまたは**コンクリート・エッグ**で発酵・シュール・リー約 1 年・7 月末ティラージュ・**さらに最低 2 年**・出荷 6 か月前デゴルジュマン・**2 g/l**。**1999 年開始** | 🔍 **canonical 未登録** |
| **Cramant Nature** | **Coteaux Champenois** Grand Cru（**泡なし白**） | 「Cramant のテロワールを、泡なしで」。公式評「**並外れた繊細さ／際立って成熟し繊細な、泡のないワイン**」 | 🔍 **canonical 未登録** |
| **Vertus Rouge** | **Coteaux Champenois** Premier Cru（**赤**） | Vertus の Pinot Noir。**2025 年で樹齢 65 年の古木**由来。蔵元 **90€/btl**。公式のペアリング提案は**釣り上げたスズキ／仔牛のすね肉**。公式は「Coteaux Champenois はシャンパーニュと同一の生産地区・栽培条件で、スティルワインとして醸造される。**最も名高い村はラベルに村名を記す（Bouzy Rouge, Vertus Rouge…）**」と説明 | 🔍 **canonical 未登録** |

✅ **Vinothèque（蔵出しバックヴィンテージ）にのみ存在する第 9 の顔**:
**`BLANC DE NOIRS Premier Cru Brut Nature`** — 「Vertus のピノ・ノワールが**7 年の熟成を経て**表現する、エレガントでヴァン的（vineux）で複雑なシャンパーニュ」。**2015 = 125€/btl**。
⚠️ **通常レンジの 8 種には含まれていない。**常時商品か Vinothèque 限定かは ❓。

✅ **単一区画（champagnes singuliers）の系譜 — 公式が明示する順序**
**1988 Vieille Vigne de Cramant（現 Vieille Vigne du Levant）→ 1995 Terre de Vertus → 1999 Rosé de Saignée → 2009〜 Les Chemins d'Avize（最新）**

---

## Staff Notes

### 芯 3 点（これだけ覚えれば OBP の 3 本は語れる）

**① 「Latitude と Longitude は、緯度と経度そのもの」— これが最強の一言。**
- **Latitude（緯度）＝ Vertus 南部という、東西に走る一本の線の上だけ**から。だから**豊かで丸い**。祝祭の一本。
- **Longitude（経度）＝ コート・デ・ブランを南北に貫く線（東経 4 度線付近）の上に並ぶ 4 村**から。だから**まっすぐで、長く、ミネラル**。アペリティフの一本。
- **地図を指で横に引くか、縦に引くか。**この 2 本を並べて売れるのが Larmandier-Bernier の最大の武器。$220 と $240、差は $20。**「同じ造り手が、同じシャルドネで、畑の取り方だけを変えた 2 本」**として並行提案せよ。

**② 「NV だが、ブレない理由がある」— 永久リザーヴ 40%。**
Latitude も Longitude も **2004 年に始まった永久リザーヴ（perpetual reserve）を 40% 含む。**毎年新しい年が注ぎ足され、20 年以上の年が層になっている。**「NV = 安い方」ではなく「NV = 積み重ね」**という語り口に転換できる。
さらに: **野生酵母 100%・木樽発酵・MLF は止めない・無濾過無清澄・手動デゴルジュマン・ドサージュ 2 g/l。**シャンパーニュの 99% が市販酵母を使う中で、この蔵は「**市販酵母は品質は良いが味の均一化に寄与している**」と公式に言い切っている。

**③ VVdL の $535 は「時間」の値段。**
- **クラマン・グラン・クリュの単一区画（`Bourron du Levant`）、単一年、樹齢 60〜85 年超。**
- **東向き。**「Levant」は東の意。**朝一番の陽が当たる。**同じクラマンでも斜面の反対（西向き）とは別物で、東向き側は特にリッチでパワフル。
- **ティラージュ後、セラーで約 9 年。デゴルジュマンは出荷の 1 年前、手作業。**
- **公式が「開くのに時間を要する」と明言している。**→ **抜栓後すぐに出さない。グラスは白ブルゴーニュ型。**canonical も VVdL のみ `glassware: White Burgundy Glass` を指定している（Latitude / Longitude はフルートも可）。🔍
- ペアリングは公式提案がある: **モリーユ茸を添えた家禽／クリーム系の料理。**「堂々と拮抗する」。

### 追加で効く話（訊かれたら出す）

- **「なぜキャップシールが無いの？」** → **2024 年 9 月からの意図的な廃止。**EU 法改正で可能になった。蔵の言葉は「**最良の廃棄物は、存在しない廃棄物**」。「常に簡素さの中に瓶の優雅さを求めてきた」。**欠品でもミスでもない。**これは自信を持って言える鉄板ネタ。
- **「オーガニックですか？」** → **「2003 年からオーガニック認証。1999 年から全所有畑でビオディナミ。除草剤は 1992 年に捨てました。」**（認証機関名は言わない。§⚠️）
- **「サステナビリティの評価は？」** → **Robert Parker Green Emblem の最初の 24 生産者の 1 つ。**
- **家族**: **Pierre と Sophie（ともに 1988 年から）、息子の Arthur（2017 年〜）と Georges（2021 年〜）の 4 人。**Georges は**元・航空エンジニア（3 年）**。Sophie は**École Centrale de Lyon 卒**で **Avize 出身**。この「理系の家族がシャンパーニュを造っている」という絵は刺さる。
- **歴史の一撃**: **1950 年代、Jules Larmandier と息子 Philippe Allyre は La Tour d'Argent と Taillevent に納めていた。**レストランの文脈で最も効く一行。
- **ブドウは一切買わない。**「収穫をコントロールし続けるため」。畑を買うことでしか拡大しない（2002 年 Vertus 4 ha、2018 年 Avize）。
- **モットー**: 「**良いシャンパーニュは規則に従う。本当に偉大なシャンパーニュは、しばしばそれを破る。**」

### ⚠️🔴 言ってはいけないこと（**公式に無い／公式内で食い違う**。この蔵は記述が濃いぶん、外す時は大きく外す）

1. **「デメテール認証」「ビオディナミ認証」「Biodyvin」と言わない。**
   公式は **`Demeter` `Biodyvin` `Ecocert` のいずれの語も全ページで一度も使っていない。**公式が書いているのは
   **①「biodynamie depuis 1999（1999 年からビオディナミ）」②「certifié BIO depuis 2003（2003 年からオーガニック認証）」の 2 点だけ**である。
   → **言ってよいのは「2003 年からオーガニック認証」「1999 年からビオディナミを実践」まで。「ビオディナミ認証を取得している」とは言わない。認証機関名は絶対に出さない。**
2. **Latitude を「プルミエ・クリュ」と言い切らない。**
   OBP は「'Latitude,' **Premier Cru** Extra Brut」と印字し canonical も Premier Cru タグを持つが、
   **公式のキュヴェページ見出しにも URL slug にも Premier Cru は無い**（Longitude・Terre de Vertus・Rosé には有る）。
   → **「ヴェルテュ（プルミエ・クリュ格の村）の南部から」と、村の格として言う。ワインの格付表記としては言わない。**
3. **「新樽 ◯%」「◯ヶ月樽熟成」と言わない。**
   公式は **Stockinger 社の fût（樽）と foudre（大樽）**としか書かない。**新樽比率・樽サイズ・樽とフードルの比率はすべて非公表。**
   → 言ってよいのは「**収穫全量が木で発酵・熟成される**」「**Stockinger 社製を、トーストが繊細でワインを尊重するという理由で選んでいる**」まで。
4. **「マロラクティックは止めています」と言わない。逆である。**
   全キュヴェページに「**the malolactic fermentation begin spontaneously**」と明記。**MLF は自然に起こる。**
   （ミネラル/シャープなスタイルから MLF ブロックを類推するのは典型的な事故。**この蔵はやっていない。**）
5. **「ドサージュ・ゼロの蔵」と一括りにしない。**
   **0 g/l は Terre de Vertus だけ。**OBP の 3 本はすべて **2 g/l**。
   さらに上限値そのものも**公式内で食い違う（Know-How ページ「3 g を超えない」／各キュヴェページ「4 g を超えない」）。**
   → **上限を語らず「このキュヴェは 2 g/l」と実測値を言う。**
6. **「醸造長は◯◯です」と言わない。**
   **公式に chef de cave の職名も個人名も存在しない。**4 名の家族が vignerons として並ぶだけ。
   → 「**家族 4 人で造っている**」と言う。
7. **「16 ヘクタール」と言わない。**
   16 ha は**公式サイトに転載された第三者ガイド（Les Meilleurs Vins Le Guide）の記述**であり、
   **蔵自身の公表値は 19 ha（＝ EN 版 47 acres）で FR/EN 一致している。** → **19 ha。**
8. **グラン・クリュの村数を断定しない。**
   公式内で **Cramant / Chouilly / Oger / Avize（FR 版 Know-How, 4 村）** ／ **Cramant / Chouilly / Avize（EN 版）** ／
   **Cramant / Avize / Oger（Domain ページ）** と 3 通りに割れている。
   → **「ヴェルテュのプルミエ・クリュに加えて、クラマン、アヴィズ、オジェといったグラン・クリュに畑を持っています」**
   と**例示で止める**。「グラン・クリュ 3 村」「4 村」と数を言わない。
9. **VVdL の区画名を「ブロン・デュ・ルヴァン」と言わない。**
   **公式の綴りは `Bourron du Levant`（ブーロン）。**canonical の日本語 `terroir` が「ブロン」と誤記している。
   → 迷うなら**「クラマンの東向きの単一区画」**とだけ言えば十分。
10. **キュヴェ名を複数形「Vieilles Vignes du Levant」と言わない。**
    **公式は単数 `Vieille Vigne du Levant`。**Vinous も Le Figaro も複数形で書いているが、**蔵の正式名は単数。**
    （なお **1988 年の創設時の名は `Vieille Vigne de Cramant`。Cramant と crémant の混同を避けて改名した。改名の年は公式に無い** ❓）
11. **「Longitude はグラン・クリュを含むから Latitude より格上」と言わない。**
    Longitude は GC 3 村を含むが**表記は Premier Cru** である。この理由を公式は説明していない 🔍。
    → **「格の上下」ではなく「取り方の違い（緯度＝1 村の横線／経度＝4 村の縦線）」として売る。**
12. **Latitude / Longitude の熟成年数を断定しない。**
    公式は「**at least two more years（最低さらに 2 年）**」としか言わない。**「3 年熟成」等の具体値は公式に無い。**
    → 「**最低 2 年、デゴルジュマンは出荷の 9 か月前**」と、公式の言い方のまま言う。
13. **「1971 年創業のドメーヌ」と言い切らない。**
    **1971 年は `Larmandier-Bernier` というラベルの誕生年**（Philippe Larmandier ＋ Elisabeth Bernier）。
    **家族のブドウ栽培は 1765 年から、コート・デ・ブランでは 8 世代。**
    → 「**ラベルは 1971 年、家族は 1765 年から、コート・デ・ブランで 8 世代**」と 3 点セットで言う。
14. **OBP の VVdL は 2014 である。2015 と言わない。**
    🔍 **蔵元が現在販売しているのは 2015**（Vinous 96 点も 2015）。**OBP は 1 つ前の 2014。**
    → **点数を引用するなら「2015 が 96 点」であって「この 2014 が 96 点」ではない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

**なし。**

（走査根拠 🔍: `theseus-phase0@main` の `migration/out/resolved/wine_makers.json`（384 件）および `cuvees.json`（781 件）を
文字列 `larmandier` で全走査した結果、**ヒットは `producer:larmandier-bernier` 1 件と、その配下の 3 キュヴェのみ。**
`Guy Larmandier` `Larmandier Frères` 等の同姓別生産者は canonical に存在せず、**衝突する相手が無い。**
また `research/canonical_conflicts/REGISTER.md` の全 10 件（P-1〜P-7 / C-1〜C-3）に Larmandier は**一度も登場しない。**
**REGISTER.md への追記は不要。**canonical は読み取りのみで一切変更していない。）

### 🔴 ただし canonical に**衝突ではない事実誤り／未検証記述**が 3 件ある（**別件としてエスカレーション**）

これらは重複ではないため上記の「衝突なし」は覆らないが、**canonical 昇格時に必ず修正が要る。research 側では修正していない。**

| # | 対象 | 内容 | Confidence |
|---|---|---|---|
| **E-1** | `cuvee:larmandier-bernier-vieille-vigne-du-levant-grand-cru-extra-brut` の `facts.terroir`（日本語） | 区画名を**「ブロン・デュ・ルヴァン」**と表記。**公式の綴りは `Bourron du Levant`。**単純な転記誤り | **High** |
| **E-2** | `cuvee:larmandier-bernier-latitude-extra-brut` の `facts.subregion` / `facts.tags` | **`Premier Cru` を付与している**が、**公式はこのキュヴェにのみ意図的に cru 表記を付けていない**（Longitude・Terre de Vertus・Rosé には付いている）。OBP 印字も同じ問題を持つ | Medium-High |
| **E-3** | `cuvee:larmandier-bernier-longitude-extra-brut-premier-cru` の `facts.terroir_en` | 「Avize's precision, Cramant's depth, **Oger's aromatic elegance**」という村ごとの性格付けは**公式サイトに一切根拠が無い編集上の創作**。また `subregion` が **Chouilly を含まない**（公式 FR 版 Know-How は 4 村目に Chouilly を挙げる） | Medium-High |

---

## Sources

### 一次資料（公式サイト `https://larmandier.fr/` のみ。ローカル保存: `_sources/larmandier-bernier/`）

| ページ | ローカル |
|---|---|
| `/en/`（Home） / `/fr/` | `home_en.html` / `home_fr.html` |
| `/en/our-domain/` / `/fr/maison-larmandier/`（Estate・Philosophy・Chronology・Winegrowers） | `domain_en.html` / `domain_fr.html` |
| `/en/our-know-how/` / `/fr/savoir-faire-vigneron/`（Vineyard・Vinification・Blending・Ageing・Dosage） | `knowhow_en.html` / `knowhow_fr.html` |
| `/en/our-champagnes/` / `/fr/champagnes/`（レンジ一覧・Authenticity・Green Emblem） | `champagnes_en.html` / `champagnes_fr.html` |
| `/en/our-champagnes/latitude/` / FR | `cuvee_latitude_en.html` / `cuvee_latitude_fr.html` |
| `/en/our-champagnes/longitude/` / FR | `cuvee_longitude_en.html` / `cuvee_longitude_fr.html` |
| `/en/our-champagnes/vieille-vigne-du-levant/` / FR | `cuvee_vvdl_en.html` / `cuvee_vvdl_fr.html` |
| `/en/our-champagnes/terre-de-vertus/` / FR | `cuvee_terredevertus_en.html` / `cuvee_terredevertus_fr.html` |
| `/en/our-champagnes/chemins-avize/` | `cuvee_cheminsavize_en.html` |
| `/en/our-champagnes/rose-de-saignee/` | `cuvee_rose_en.html` |
| `/en/our-champagnes/cramant-nature/` | `cuvee_cramantnature_en.html` |
| `/en/our-champagnes/vertus-rouge/` | `cuvee_vertusrouge_en.html` |
| `/en/visits-contact/` | `visits_en.html` |
| `/fr/vinotheque/` | `vinotheque_fr.html` |
| ブログ `Récolte 2025`（2025-10-07） | `post_recolte2025.html` |
| ブログ `Non, nous n'avons rien oublié !`（2024-09-13） | `post_rienoublie.html` |
| Revue de Presse（公式が転載する第三者評） | `presse.html` |
| **公式 PDF** `tour-Larmandier-Bernier-vineyards.pdf`（畑めぐり地図。Vertus の自社区画 13 か所を実名で列挙） | `tour-vineyards.pdf` / `tour-vineyards.txt` |
| `page-sitemap.xml` / `post-sitemap.xml`（**全 URL を列挙し、未読ページが無いことを確認**） | 同名 |

### THÉSEUS 内部（読み取りのみ）
- `theseus-phase0@main:migration/out/resolved/wine_makers.json`（384 件）／ `cuvees.json`（781 件）🔍
- `research/canonical_conflicts/REGISTER.md`（全 10 件を確認、Larmandier は不在）🔍
- OBP intake（掲載 3 本・価格・セクション・`cuvee_state=alias`・`source_quality_flags` なし）🔍

### 明示的に使わなかったもの
Wikipedia・小売/EC サイト・インポーターの販促文・レビュー集約サイト（wine-searcher / vivino 等）・まとめブログ。
Vinous / Wine Advocate / Le Figaro / Bettane & Desseauve の点数と評文は、**公式サイトが自ら転載しているもののみ**を `📄` として引いた。

---

## Confidence

| 節 | 評価 | 根拠 |
|---|---|---|
| Identity | **High** | 住所・GPS・4 名の体制すべて公式。**2025-10-07 の署名で現況を確認済み**（教訓 1 クリア）。chef de cave の不在は ❓ として明示 |
| Overview | **High** | 全項目が公式の直接記述 |
| History | **Medium-High** | 公式年表が 1765 年から 2025 年まで 18 点あり異例に厚い。**ただし各人物の生没年が皆無**、Philippe Allyre と Philippe の同一性が ❓ |
| Location | **Medium-High** | 面積 19 ha は FR/EN 一致。区画名は公式 PDF で 13 か所を実名確認。**⚠️ グラン・クリュ村リストが公式内で 3 通りに割れる**ため満点にならない。村ごとの面積内訳は皆無 |
| **Farming** | **High** | 年次（1992/1999/2002/2003）・手法・0% pesticide・手摘み・マサル選抜まで公式。**❓ は認証機関名のみ**（これは ⚠️ で防御済み） |
| **Winemaking** | **High** | 圧搾から手動デゴルジュマンまで全工程が公式。**MLF・野生酵母・無濾過無清澄・永久リザーヴ 40%・Stockinger まで一次確認。**⚠️ ドサージュ上限の 2 値のみ食い違い。新樽比率は ❓ |
| Style | **Medium-High** | 公式の自称・モットー・哲学は一次。第三者評価は**公式サイト転載分に限定**したため範囲が狭い |
| **Important Cuvées** | **High** | **OBP 3 本すべてに公式キュヴェページがあり、品種・ドサージュ・熟成年数・デゴルジュマン時期・リザーヴ比率・旧名まで揃った。**レンジ全 8 種＋Vinothèque も網羅。⚠️ Latitude の cru 表記のみ要注意 |
| Staff Notes | **High** | 芯 3 点が公式の一次情報のみで構成でき、**⚠️ リスト 14 項目すべてが「公式に無い／公式内で食い違う」ことの実証に基づく** |
| Canonical Conflict | **High** | 384 生産者・781 キュヴェを全走査。REGISTER.md 全件確認。**衝突は存在しない** |
| **総合** | **Medium-High** | **70% を明確に超えている。**必須 6 項目（Identity / Overview / Location / **Farming** / Important Cuvées（OBP 紐付け）／ Staff Notes 芯 3 点 ／ ⚠️ リスト）がすべて公式一次で埋まった。**後回し可の領域（新樽比率・収量・村別面積・各キュヴェ生産本数）のみが空白** |

---

## Open Questions

### 🔴 現場に影響する（優先）
1. ❓ **ビオディナミの認証の有無と機関名。**公式は「1999 年からビオディナミ」「2003 年から BIO 認証」としか書かず、**ビオディナミ認証（Demeter / Biodyvin）についてはその有無すら述べていない。**→ **蔵元に直接照会するのが唯一の解。** 現状は ⚠️ 2 番で防御。
2. ❓ **Latitude はラベル上 Premier Cru を名乗っているか。**公式サイトは付けず、OBP は付け、Vinous は「1er Cru」と書く。**実ボトルのラベル写真での確認が要る。**OBP 側の印字修正が必要になる可能性がある。
3. ❓ **グラン・クリュの村は 3 か 4 か（Chouilly と Oger）。**公式内 3 通り。**蔵元照会 or 現行ラベルの記載で解決。**
4. ❓ **OBP の VVdL 2014 の実際のデゴルジュマン日。**公式は「ティラージュ後 9 年、出荷 1 年前に手動デゴルジュマン」としか言わず、**2014 の個体の dégorgement date は不明。**（ボトル背面に記載がある可能性）

### 記述の穴（後回し可）
5. ❓ **新樽比率・樽とフードルの比率・樽の容量。**公式は「Stockinger」としか書かない。
6. ❓ **収量（hl/ha）。**「rendements mesurés」のみで数値なし。
7. ❓ **19 ha の村別内訳。**Vertus / Cramant / Chouilly / Oger / Avize それぞれの面積は完全に非公表。
8. ❓ **各キュヴェの年産本数。**公式に一切なし。
9. ❓ **`Vieille Vigne de Cramant` → `Vieille Vigne du Levant` の改名年。**公式は改名の理由（Cramant / crémant の混同）は書くが年を書かない。
10. ❓ **Philippe Allyre Larmandier と、1971 年に Larmandier-Bernier を創設した Philippe Larmandier は同一人物か。**年表上は同一人物と読めるが公式は表記を統一していない。
11. ❓ **`Blanc de Noirs Premier Cru Brut Nature` は通常レンジの商品か、Vinothèque 限定か。**レンジ一覧（8 種）には入っていない。
12. ❓ **各人物の生没年。**Louis Prosper / Jules / Philippe Allyre / Philippe / Elisabeth Bernier いずれも不明。Philippe の没年（1988 年前後の「早すぎる死」）も年が特定できない。
13. ❓ **Robert Parker Green Emblem の受賞年。**「最初の 24 生産者の 1 つ」とのみ。

### canonical へのエスカレーション（**research では実行しない**）
14. 🔴 **E-1 / E-2 / E-3**（§Canonical Conflict 末尾の表）— **canonical 側の転記誤り 1 件・格付表記の疑義 1 件・出典なき創作記述 1 件。**衝突ではないため REGISTER.md の対象外だが、**canonical 昇格の前に裁定が要る。**
15. 🔴 **Packet A 候補 5 件**: `Les Chemins d'Avize` / `Terre de Vertus` / `Rosé de Saignée` / `Cramant Nature` / `Vertus Rouge` は**公式レンジに実在するが canonical 未登録。**本書に公式一次の技術情報が揃っているため、**登録は即座に可能。**
16. 🔴 **将来の intake 防御**: `Guy Larmandier` / `Larmandier Frères` を姓トークンだけで `producer:larmandier-bernier` に吸着させない規則が要る（REGISTER.md P-2 と同型のリスク）。
