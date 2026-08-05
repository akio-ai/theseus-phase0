# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは存在しない。** 本書は昇格前の研究記録であり、**何も作成していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト polroger.com で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.polroger.com/`（EN / FR）**
> 走査元: 🔴 **`robots.txt` が指す `http://www.polroger.com/sitemap.php`**
> （`/sitemap.xml` は存在しない。**`sitemap.php` に切り替えて初めてページが列挙できる**）
>
> 🔴 **本ドシエ最大の収穫は、OBP 掲載 6 本すべてが公式のヴィンテージ一覧に実在すると確認できたこと。**
> **`Brut Vintage` は 2018 / 2016 の両方、`Cuvée Sir Winston Churchill` は 2018、
> `Brut Vintage Édition Vinothèque` は 2004、`Cuvée SWC Édition Vinothèque` は 2002 が公式に存在する。**
>
> ⚠️ **調査上の制約 2 点**
> **① `/en/history/the-house` と `/en/history/the-family` は静的取得で本文が返らない**（JS 描画の年表 `uneFriseHistoire`）。
>    **本ドシエに沿革の年表は無い。創業年も本書では主張しない。** → Open Questions 2
> **② `/en/champagnes/11/…`（SWC Vinothèque）は一度 `error code: 520` を返した。**再試行で取得できた。

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Pol Roger** |
| **公式表記** | **Champagne Pol Roger** ✅（各ワインページの `<title>` は `… - Champagne Pol Roger`） |
| **法人** | ✅ **Pol Roger & Cie**（`/en/news-champagne/318/le-conseil-de-surveillance-de-pol-roger-cie-se-renforce`） |
| **所在** | ✅ 🔴 **Épernay の `Avenue de Champagne`**。「**ワイナリーとカーヴは、シャンパーニュの心臓が脈打つまさにその場所、
Épernay の名高く高貴な Avenue de Champagne にある**」 |
| 🔴 **カーヴの深さ** | ✅ 🔴 **地下 33 メートル。** 全キュヴェの記述に繰り返し現れる。**「非常に細かく持続するムースは、この深く冷たく湿ったカーヴに多くを負っている」** |
| **歴史の長さ** | ✅ **「175 years of history, six generations & Independence」**（`/en/philosophy/excellence-champagne` の見出し） |
| **創業年** | ❓ 🔴 **本ドシエでは主張しない。** 年表ページが JS 描画で取得できなかった → Open Questions 2 |
| **家族経営** | ✅ **6 世代。**「**家族が完全な独立のうちにアッサンブラージュを選ぶ**」 |
| 🔴 **醸造長** | ✅ **Damien Cambres**（`cellar master`。SWC Vinothèque 2002 の記述で名指し） |
| **前会長** | 🔍 ✅ **Patrice Noyelle** への tribute 記事が公式ニュースに存在（`/news-champagne/321/tribute-to-patrice-noyelle`）。**本調査では内容未読** |
| **認定** | 🔍 ✅ **`Entreprise du Patrimoine Vivant`（生きた遺産企業）** の公式ニュースあり（`/news-champagne/309/`）。**本調査では内容未読** |
| **加盟** | 🔍 ✅ **`Primum Familiae Vini`**（家族経営ワイン生産者の国際団体）の記事が複数 |
| canonical id | 🔴 **無し**（canonical 生産者 384 件を `pol roger` で走査 → **0 件**） |

---

## Overview

✅ **Épernay の Avenue de Champagne に本拠を置く、6 世代・175 年の家族経営メゾン。**

🔴 ✅ **公式が自らの核心として掲げる語は 2 つ —— `Excellence` と `Independence`。**
「**この評価は、メゾンが揺るぎなく捧げてきた 2 つの本質的な価値の果実である —— 卓越と独立。
われわれの名を帯びるワインは一つひとつが、われわれの歴史の完璧な大使として扱われる。
6 世代にわたり、後継者たちは等しく厳格であり、創業者が最初から始めた戦略に忠実であり続けた。**」

🔴 ✅ **公式は「ブドウを買っている」ことを隠していない。**
「**卓越とは、メゾンが仕事を共にするブドウ栽培者の厳格な選定を意味し、
また彼らから買うブドウの厳格な選別を意味する。
家族の一員が、醸造の細部を含むすべての作業に目を光らせる。
それはまた、家族が完全な独立のうちに、ワインを生むアッサンブラージュを選ぶということでもある。**」
→ 🔴 **したがって「全部自社畑」とは言えない。** → §Staff Notes ⚠️ ②

🔴 ✅ **醸造上の署名は 4 つあり、全キュヴェに共通する。**
**① デブルバージュを 2 回**（プレス場で 1 回、蔵で **6 °C・24 時間の冷却デブルバージュ**を 1 回）
**② 低温発酵**（**18 °C 以下**、ステンレス。**品種ごと・村ごとに分けて**アッサンブラージュまで保つ）
**③ 全ワインがマロラクティック発酵を通る**（「All our wines go through a malolactic fermentation」）
**④ 手作業のルミュアージュ**（「**今日のシャンパーニュでは稀（a rarity in Champagne nowadays）**」と公式が明記）

✅ **スタイルの自己規定** — 「**Pol Roger は紳士のシャンパーニュである**」（Jean-Paul Kauffmann の
『Voyage en Champagne』からの引用として公式が掲げる）。
「**したがって Winston Churchill、さらには英国王室が、年月をかけてこれをお気に入りにしたのも驚くにあたらない。**」

🔍 **THÉSEUS における状態は最悪の部類。canonical に生産者レコードが無く、OBP 掲載 6 本すべてが
`producer_state = unresolved`。**

---

## History

⚠️ 🔴 **公式サイトの沿革ページ（`/en/history/the-house` / `/en/history/the-family`）は
静的取得で本文が返らない**（HTML 内のクラス名 `uneFriseHistoire`＝「歴史の帯」から、
**JS 描画の年表**であることは確認できる）。
**したがって本ドシエは沿革の年表を持たない。**

✅ **他ページから確定できる歴史上の 3 点だけを記す。**

| 年 | 出来事 ✅ |
|---|---|
| — | **175 年の歴史、6 世代。**「**創業者が最初から始めた戦略に忠実であり続けた**」 |
| **1975** | 🔴 **`Cuvée Sir Winston Churchill` が「Old Lion（老いた獅子）」への tribute として創られる。** 公式の記述 —「**The Sir Winston Churchill Cuvée was created in 1975 as a tribute to the "Old Lion"**」 |
| **175 周年** | 🔴 **`Édition Vinothèque` の展開が始まる。**「**175 周年を機に、Pol Roger は象徴的なキュヴェの古いヴィンテージを、ごく限られた本数で提供することにした**」 |

✅ **Churchill との関係について公式が書いていること** —
**キュヴェは Churchill が「シャンパーニュに求めた資質」を反映して造られた。**
すなわち **`a firm structure`（堅固な骨格）、`a full-bodied character`（フルボディの性格）、
`relative maturity`（相応の熟成）**。
**引用される Churchill の言葉は「My tastes are simple, I am easily satisfied with the best.」**
🔴 **「正確なアッサンブラージュは家族が固く守る秘密である」と公式は明記している。**

🔴 ✅ **SWC の畑についての公式の限定** —
「**Churchill の存命中にすでに植わっていた（already under vine during Churchill's lifetime /
already in production during the Churchill era）Pinot Noir と Chardonnay のグラン・クリュのブドウだけで造られる。**」

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| **本拠** | ✅ **Épernay、`Avenue de Champagne`** |
| 🔴 **カーヴ** | ✅ **地下 33 m。** 二次発酵は **9 °C** で行われる |
| **ブドウの産地** | ✅ **Montagne de Reims ／ Vallée de la Marne ／ Épernay 周辺 ／ Côte des Blancs** |

### ✅ キュヴェ別の産地構成（公式）

| キュヴェ | 産地 |
|---|---|
| **Brut Réserve** | 🔴 **30 の異なるクリュ**。Pinot Noir は主に **Montagne de Reims の最良のクリュ**、Pinot Meunier は **Vallée de la Marne と Épernay 周辺の複数のクリュ**、Chardonnay は **Épernay と Côte des Blancs の最良のクリュ** |
| **Brut Vintage** | 🔴 **Montagne de Reims と Côte des Blancs の 20 のグラン・クリュおよびプルミエ・クリュ** |
| **Cuvée Sir Winston Churchill** | 🔴 **グラン・クリュのみ**（Pinot Noir と Chardonnay）。**Churchill の存命中にすでに生産していた畑に限る** |

❓ **公式に無い**: 自社畑の面積・所有クリュ名・購入比率・栽培方針・認証。

---

## Farming

🔴 ⚠️ **本調査では栽培について一件も確定できなかった。**

**公式サイトの栽培に関する記述は、`/en/philosophy/excellence-champagne` の
「メゾンが仕事を共にするブドウ栽培者の厳格な選定と、彼らから買うブドウの厳格な選別」という一文のみである。**

⚠️ **公式サイトに `organic` / `biodynamic` / `HVE` / `Viticulture Durable en Champagne` /
認証機関名は一切出てこない。**

🔍 **`/f/file/our-commitments.pdf`（「われわれのコミットメント」・1.1 MB）を取得したが、
テキストレイヤーが無く抽出できなかった。** **この PDF に栽培・環境方針が書かれている可能性が高い。**
→ **OCR すれば埋まる。** → Open Questions 3

⚠️ **したがって「Pol Roger は◯◯栽培です」という言い方は本ドシエでは一切しない。**

---

## Winemaking

### 🔴 全キュヴェに共通する工程（公式。**キュヴェページごとに同文が反復されている**）✅

| 工程 | 記述 |
|---|---|
| 圧搾 | **収穫後ただちに、繊細に圧搾** |
| **デブルバージュ①** | **プレス場で圧搾直後** |
| 🔴 **デブルバージュ②** | 🔴 **蔵のステンレスタンクで `à froid`（冷却）。6 °C・24 時間** |
| **アルコール発酵** | 🔴 **低温（18 °C 以下）。温度管理されたステンレス槽。品種ごと・村ごとに分けたまま最終アッサンブラージュまで保つ** |
| 🔴 **マロラクティック** | 🔴 **全ワインが通る**（`All our wines go through a malolactic fermentation` / `a full malolactic fermentation prior to final blending`） |
| **二次発酵（prise de mousse）** | 🔴 **瓶内・9 °C・地下 33 m のカーヴ** |
| 🔴 **ルミュアージュ** | 🔴 **1 本ずつ手作業。公式が「今日のシャンパーニュでは稀」と明記** |
| デゴルジュマン / ドザージュ | **ルミュアージュの後** |
| 出荷前の静置 | **Brut Réserve は最低 3 か月**（`the wines rest for a minimum of three months before being released`） |

✅ **公式の説明** — 「**Pol Roger が知られる非常に細かく持続するムースは、
この深く、冷たく、湿ったカーヴに多くを負っている。**」

### 🔴 キュヴェ別の構成と熟成（公式）

| キュヴェ | セパージュ | リザーヴワイン | 熟成 |
|---|---|---|---|
| **Brut Réserve** | 🔴 **Pinot Noir / Pinot Meunier / Chardonnay を等量**（30 クリュ） | 🔴 **25%** | 🔴 **カーヴで 4 年** |
| **Brut Vintage** | 🔴 **Pinot Noir 60% / Chardonnay 40%**（20 の GC・1er Cru） | — | **「深いカーヴで熟成」**（**2013 / 2012 は「7 年」と明記**） |
| **Brut Vintage Édition Vinothèque** | **同上（60 / 40）** | — | 🔴 **デゴルジュマン前に 10 年**（2006 は「約 10 年」）。**その後、初回デゴルジュマンを経て再びカーヴへ戻し、追加の長期熟成** |
| **Cuvée Sir Winston Churchill** | 🔴 **Pinot Noir 主体 ＋ Chardonnay。グラン・クリュのみ。比率は非公開** | — | 🔴 **カーヴで 10 年超。「他のヴィンテージ・シャンパーニュより常に遅くリリースされる」** |
| **Cuvée SWC Édition Vinothèque** | **同上** | — | 🔴 **デゴルジュマン前に 10 年 ＋ 追加の長期熟成** |

🔴 ✅ **`Édition Vinothèque` の定義（公式の原文）** —
「**175 周年を機に、Pol Roger は象徴的なキュヴェの古いヴィンテージを、ごく限られた本数で提供することにした。
最初のデゴルジュマンののち、これらのボトルは名高く深く冷たい Pol Roger のカーヴに戻され、
リリースまで手つかずのまま眠っていた。
これらのボトルは歴史的な Pol Roger のデザインに基づくラベル・キャップ・カラーを持つだけでなく、
手作業で仕立てられ、優雅な木箱に入って届く。**」

🔴 ⚠️ **ドザージュの g/L、アルコール度数、デゴルジュマン日、生産本数は公式に一切記載が無い。**
→ §Staff Notes ⚠️ ⑤

---

## Style

### ✅ 公式テイスティングノート（OBP 掲載 6 本すべて）

| キュヴェ / VT | 公式ノート（抜粋） |
|---|---|
| **Brut Réserve**（NV） | 「**美しい黄金の麦わら色**、豊かで細かい泡。**力強く魅力的な香り**は、まず**果実（洋梨、マンゴー…）**を、次いで**スイカズラと白いジャスミン**の軽やかな風味を放ち、**ヴァニラとブリオッシュ**の調子に落ち着く。率直で躍動的なアタックの奥に、良い調和と心地よい清涼感、そして骨格。口中では**煮た果実（マルメロのゼリー、杏のジャム）**が**蜜蝋とアカシアの蜂蜜**の香りと混じり合う。**砂糖漬けのオレンジピール、タンジェリン**といった果実の調子と、**カルダモン、アニス**の香辛料の調子からなる長い余韻が卓越している。」 |
| **Brut Vintage 2018** | 「**結晶のように淡い黄色**、極めて細かい泡が繊細で優雅な糸となって表れる。**第一香は控えめでやや閉じている。**次第に開き、**フレッシュな果実、エキゾチックフルーツ（とくにパイナップル）、白桃**の調子。空気に触れると**フレッシュバターとカスタードクリーム**の香りが立ち上る。口中は**丸みと volume** を特徴とし、同時に美しい芳香の清涼感を示す。**Pol Roger が知られる広がりと長さ**がある。余韻はややタンジーで、レモンと柑橘の気配が心地よい清涼感を残し、**有望な熟成能力を予告する**。」 |
| **Brut Vintage 2016** | 「**銀の照りを帯びた淡い黄色**、細かく持続する泡の糸から立ち上る魅惑的な発泡。**とりわけ開いて表現力のある香り**は、**乾果、カカオ、アーモンド、ココナッツ**の調子で始まる。空気に触れると**ミラベルや eau de vie といった黄色い果実**の調子が複雑さを加え、若いながら豊かで有望。**口中は極めてフレッシュ。切れのある酸**が強い背骨を与え、余韻まで貫く。第一香の乾果の香りが持続し、**柑橘、レモン、ビターオレンジ**の色合いが口中を完成させ、ワインの若さを裏づける。」 |
| **Cuvée Sir Winston Churchill 2018** | 「**輝く黄金色**と繊細な泡は、メゾンの最深部のカーヴでの長い熟成の証。**均衡のとれた香りはまだ内気だが、すでに美しい艶を見せる。白い花、柑橘、乾燥した杏**の調子が、**ブロンド・タバコと穏やかに胡椒の効いた甘い香辛料**の香りと混じる。口中は清潔で、**躍動的な清涼感**。**ミネラリティと張り**が、複雑さと優雅さを併せ持つ骨格の中で織り合わされる。口中の構築は**エネルギッシュかつ洗練**。**ブラッドオレンジとペストリー**の香りが**フレッシュなラズベリー**の気配に美しく補完される。余韻は長く、寛大で、将来性に満ちる。」 |
| **Brut Vintage Édition Vinothèque 2004** | 「**強い黄金色**に明るい照り、細かく繊細な泡。香りは**砂糖漬けの果実、カカオ、モカ**の凝縮した香りを放ち、空気に触れると**繊細なペストリーの調子、さらにはドゥルセ・デ・レチェ**の気配が加わる。口中は**その古い年齢を映す、著しい存在感と vinosité（ヴィノジテ）**を示す。**柑橘、オレンジ、砂糖漬けのレモン**の調子が**蜂蜜の一筆**に美しく引き立てられる。**大きく寛大な余韻**を持つ洗練されたシャンパーニュ。」 |
| **Cuvée SWC Édition Vinothèque 2002** | 🔴 「**銅の気配を帯びた美しい深い黄金色**と細かい泡。香りでは**砂糖漬けの黄色い果実**が**ヘーゼルナッツのリキュール、フルーツゼリー、熟成したコニャック**の繊細な調子と混じり合う。口中は香りと呼応する。**極めて滑らかでヴィノーなこのワインの骨格は、緊密でありながら豪奢。**歴史的なヴィンテージとして供されるこの Cuvée Sir Winston Churchill は、メゾンの深いカーヴでの熟成の恩恵を余すところなく受け、深みを増して、いま在る**フルボディで骨格の確かなワイン**となった。**醸造長 Damien Cambres はこれを『三次元的』——繊細さ・力・長さを併せ持つ——と評する。**」 |

✅ **Brut Réserve の食事との合わせ方（公式）** —
「**この Brut Réserve に捉えられた骨格とヴィノジテ、優雅さと清涼感は、力と繊細さの最適な均衡を与え、
アペリティフとしても、食事を通して供するのにも際立ったワインにしている。**」

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 6 本。すべて `unresolved`**）

| # | OBP 印字 | VT | 価格 | ✅ **公式の正式名 / 確認結果** |
|---|---|---|---|---|
| 1 | **'Réserve,'** Brut | NV | $230 | ✅ **`Brut Réserve`**（`/champagnes/2/brut-reserve`）。**NV。等量 3 品種・30 クリュ・リザーヴ 25%・4 年熟成** |
| 2 | **'Vintage,'** Brut | 2018 | $415 | ✅ **`Brut Vintage 2018`**（`/champagnes/3/brut-vintage`）。**公式のヴィンテージ一覧に 2018 が実在** |
| 3 | **'Cuvée de Réserve, Vinothéque,'** Brut | 2004 | $980 | ⚠️ 🔴 **`Brut Vintage Édition Vinothèque 2004`**（`/champagnes/8/…`）。**公式の一覧は 2006 / 2004 / 2002 / 2000。2004 は実在する。** ただし**公式の名称に `Cuvée de Réserve` は含まれない** → Open Questions 4 |
| 4 | **'Cuvée Sir Winston Churchill,'** Brut | 2018 | $1,155 | ✅ **`Cuvée Sir Winston Churchill 2018`**（`/champagnes/4/…`）。**公式の一覧に 2018 が実在** |
| 5 | **'Cuvée Sir Winston Churchill, Vinothéque,'** Brut | 2002 | $2,920 | ✅ **`Cuvée Sir Winston Churchill Édition Vinothèque 2002`**（`/champagnes/11/…`）。**公式の一覧は 2004 / 2002 / 1999 / 1998。2002 は実在する** |
| 6 | **Brut**（ラベル語なし） | 2016 | $505 | ⚠️ 🔴 **`Brut Vintage 2016` と読むのが最も整合する。** 公式の `Brut Vintage` 一覧に 2016 が実在し、**Pol Roger にヴィンテージ入りの「ただの Brut」は存在しない。** → Open Questions 5 |

🔴 **6 本すべてについて、公式のヴィンテージ一覧に該当する年が実在することを確認した。**
**存在しないヴィンテージを載せている行は 1 本も無い。**

### ✅ 公式の全 11 キュヴェ（`sitemap.php` より。**canonical には 1 件も無い**）

| # | 公式キュヴェ | URL |
|---|---|---|
| 1 | **Blanc de Blancs Vintage** | `/champagnes/1/blanc-de-blancs-vintage` |
| 2 | **Brut Réserve** ⭐OBP | `/champagnes/2/brut-reserve` |
| 3 | **Brut Vintage** ⭐OBP×2 | `/champagnes/3/brut-vintage` |
| 4 | **Cuvée Sir Winston Churchill** ⭐OBP | `/champagnes/4/cuvee-sir-winston-churchill` |
| 5 | **Pure Brut Nature** | `/champagnes/5/pure-brut-nature` |
| 6 | **Rich** | `/champagnes/6/rich` |
| 7 | **Rosé Vintage** | `/champagnes/7/rose-vintage` |
| 8 | **Brut Vintage Édition Vinothèque** ⭐OBP | `/champagnes/8/vinotheque-brut-vintage` |
| 9 | **Rosé Vintage Édition Vinothèque** | `/champagnes/9/vinotheque-rose-vintage` |
| 10 | **Blanc de Blancs Édition Vinothèque** | `/champagnes/10/vinotheque-blanc-de-blancs` |
| 11 | **Cuvée Sir Winston Churchill Édition Vinothèque** ⭐OBP | `/champagnes/11/vinotheque-cuvee-sir-winston-churchill` |

🔴 **`Édition Vinothèque` は 4 キュヴェに展開されている**（Brut Vintage / Rosé Vintage /
Blanc de Blancs / Cuvée Sir Winston Churchill）。
**これは独立したキュヴェではなく、既存キュヴェの「追加熟成版」という層である。**
→ 🔍 **canonical のモデルでは `V-3`（Dom Pérignon の P2 / P3 / Œnothèque）と同型の「層のずれ」になる。**
→ §Canonical Conflict

### ✅ 公式が公開しているヴィンテージ一覧（**canonical 登録時にそのまま使える**）

| キュヴェ | 公式サイト上のヴィンテージ |
|---|---|
| **Brut Vintage** | **2018 / 2016 / 2015 / 2013 / 2012 / 2009 / 2008 / 2006 / 2004 / 2002 / 2000 / 1999 / 1998** |
| **Cuvée Sir Winston Churchill** | **2018 / 2015 / 2013 / 2012 / 2009 / 2008 / 2006 / 2004 / 2002 / 2000 / 1999 / 1998 / 1996** |
| **Brut Vintage Édition Vinothèque** | **2006 / 2004 / 2002 / 2000** |
| **Cuvée SWC Édition Vinothèque** | **2004 / 2002 / 1999 / 1998** |

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① エペルネのアヴニュ・ド・シャンパーニュ、6 世代 175 年の家族経営。カーヴは地下 33 メートル。**
「**エペルネの『アヴニュ・ド・シャンパーニュ』**——造り手自身が『シャンパーニュの心臓が脈打つまさにその場所』と
書いている通りに本拠があります。**6 世代、175 年の家族経営**で、掲げる言葉は
**『卓越（Excellence）』と『独立（Independence）』**の 2 つ。
**カーヴは地下 33 メートル**にあり、**二次発酵は 9 度で行われます。**
造り手は『**Pol Roger の細かく持続する泡は、この深く冷たく湿ったカーヴに多くを負っている**』と説明しています。」

**② ルミュアージュは 1 本ずつ手作業。造り手自身が『今のシャンパーニュでは稀』と書いている。**
「醸造で一貫しているのは 4 点 ——
**デブルバージュを 2 回（うち 1 回は 6 度・24 時間の冷却）、発酵は 18 度以下で品種・村ごとに分けて、
全ワインがマロラクティックを通り、ルミュアージュは 1 本ずつ手作業。**
**手作業のルミュアージュについては、造り手自身が『今日のシャンパーニュでは稀（a rarity）』と書いています。**」

**③ 『ヴィノテーク』はキュヴェ名ではなく「追加熟成版」という層。**
「**リストにある『ヴィノテーク』の 2 本は、別のワインではありません。**
**175 周年を機に始まった企画で、いったんデゴルジュマンしたボトルを深いカーヴへ戻し、
リリースまで手つかずで寝かせたもの**です。
**ラベル・キャップ・カラーは歴史的な Pol Roger のデザインに基づき、手作業で仕立てて木箱入り**で届きます。
**2004 年のブリュット・ヴィンテージと、2002 年のサー・ウィンストン・チャーチル**が、その版にあたります。」

### 追加で使える一手

- **Cuvée Sir Winston Churchill**: 「**1975 年に『老いた獅子（Old Lion）』への tribute として創られた**キュヴェです。
  **Churchill がシャンパーニュに求めた資質 —— 堅固な骨格、フルボディ、相応の熟成 —— を反映**しています。
  **正確なアッサンブラージュは家族が固く守る秘密**と公式に書かれていますが、
  **ピノ・ノワール主体でシャルドネを加え、グラン・クリュのブドウのみ**、
  しかも **チャーチルの存命中にすでに植わっていた畑に限る**とされています。
  **カーヴで 10 年以上寝かせ、他のヴィンテージ物より常に遅くリリースされます。**
  引かれる Churchill の言葉は『**My tastes are simple, I am easily satisfied with the best.**』。」
- **Brut Réserve（$230）**: 「**3 品種を等量、30 のクリュから。リザーヴワインを 25% 使い、カーヴで 4 年。**
  出荷前にさらに最低 3 か月休ませます。」
- **Brut Vintage（2018 / 2016）**: 「**ピノ・ノワール 60%、シャルドネ 40%。
  モンターニュ・ド・ランスとコート・デ・ブランの 20 のグラン・クリュとプルミエ・クリュ**から。
  **2018 は『第一香は控えめでやや閉じている』、2016 は『とりわけ開いて表現力がある』**と、
  造り手自身がはっきり対照的に書いています。」
- **SWC ヴィノテーク 2002（$2,920）**: 「**醸造長のダミアン・カンブルがこれを『三次元的』——
  繊細さ・力・長さを併せ持つ——と評しています。**」
- **スタイルを一言で**: 「造り手は自らを『**紳士のシャンパーニュ**』と紹介しています
  （Jean-Paul Kauffmann『Voyage en Champagne』からの引用として）。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している**）

1. 🔴 ⚠️ **創業年を言わない。** **公式が書いているのは「175 年の歴史、6 世代」だけで、
   沿革の年表ページは JS 描画のため本調査で取得できなかった。**
   言うなら「**6 世代、175 年の家族経営**」まで。
2. 🔴 ⚠️ **「自社畑」と言わない。** 公式は
   「**メゾンが仕事を共にするブドウ栽培者の厳格な選定と、彼らから買うブドウの厳格な選別**」と
   明記している。**購入ブドウを使う造り手である。**
   **自社畑の面積・所有クリュは公式に一切記載が無い。**
3. 🔴 ⚠️ **栽培・農法・認証を語らない。** **公式サイトに `organic` / `biodynamic` / `HVE` /
   `Viticulture Durable en Champagne` の語が一つも出てこない。**
4. 🔴 ⚠️ **SWC のセパージュ比率を数字で言わない。**
   **公式は「Pinot Noir が優勢」としか書かず、「正確なアッサンブラージュは家族が固く守る秘密」と明記している。**
   **「60/40」などと言ってはならない**（それは `Brut Vintage` の比率である）。
5. 🔴 ⚠️ **ドザージュ（g/L）・アルコール度数・デゴルジュマン日・生産本数を言わない。**
   **公式サイトのどのキュヴェページにも記載が無い。**
6. ⚠️ **メニューの `'Cuvée de Réserve, Vinothéque,'` を公式名として復唱しない。**
   **公式の名称は `Brut Vintage Édition Vinothèque` である。**
   （`Vinothéque` の綴りも公式は `Vinothèque`。）
7. ⚠️ **`Vinothèque` を「別のワイン」と説明しない。**
   **同じキュヴェを追加熟成させた版であり、独立したキュヴェではない。**
8. ⚠️ **「Churchill が飲んでいたのはこのキュヴェです」と言わない。**
   **キュヴェが創られたのは 1975 年 —— Churchill の死後である。**
   言うなら「**Churchill への tribute として 1975 年に創られたキュヴェ**」。
9. ⚠️ **英国王室との関係を具体的に語らない。** **公式の記述は
   「Winston Churchill、さらには英国王室が年月をかけてこれをお気に入りにした」の一文だけである。**
10. ⚠️ **第三者点数を言わない。** **本調査で取得したどのページにも点数の掲載が無い。**
    （`/en/news/press-review` は未読。）
11. ⚠️ **`Brut Vintage 2013 / 2012` の「7 年熟成」を他のヴィンテージに一般化しない。**
    **熟成年数が明記されているのは 2013 と 2012 だけである。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

**新規の登録なし。**

🔍 **理由は「衝突が無い」ではなく「レコードが存在しない」。**
canonical `wine_makers.json`（全 384 生産者）を `pol roger` および `polroger` で走査 → **0 件。**
**この生産者は THÉSEUS に一切登録されていない。** キュヴェ 0 件・ヴィンテージ 0 件。

🔴 **ただし登録時に必ず踏む分岐がある。既存の `V-3` と同型なので、新しい番号は開かない。**

**`V-3`（層のずれ ── Dom Pérignon の P2 / P3 / Œnothèque）と同型の構造** —
Pol Roger の **`Édition Vinothèque`** は、**Brut Vintage / Rosé Vintage / Blanc de Blancs /
Cuvée Sir Winston Churchill の 4 キュヴェそれぞれに存在する「追加熟成版」**である。
**同じ年（例: `Cuvée Sir Winston Churchill 2002`）が、通常版と Vinothèque 版の両方に存在しうる。**

🔴 **したがって `cuvée × vintage_year` だけでは一意にならない。**
**`release_label`（＝ `Édition Vinothèque`）が要る。**
🔍 **canonical の `vintages` スキーマには `release_label` フィールドが既に存在する**
（`V-3` の Dom Pérignon Plénitude 対応で使われている想定）。
**Pol Roger を登録するなら、Vinothèque は `release_label` で表現するのが `V-3` と整合する。**
→ **ただしこれは設計判断であり、本書では実行していない。** → Open Questions 1

---

## Sources

**一次資料（公式サイト `https://www.polroger.com/` のみ。非公式ソースは一切使用していない）**

| 資料 | 取得した情報 |
|---|---|
| 🔴 **`robots.txt` → `http://www.polroger.com/sitemap.php`** | 走査の起点。**`/sitemap.xml` は存在しない。** `sitemap.php` に **11 のシャンパーニュページ**と全ニュース・ギャラリー URL が列挙されている |
| **`/en/champagnes/2/brut-reserve`** | **3 品種等量・30 クリュ・リザーヴ 25%・4 年熟成・各品種の役割・全醸造工程・テイスティングノート・食事との合わせ方** |
| 🔴 **`/en/champagnes/3/brut-vintage`** | 🔴 **2018 / 2016 を含む 13 ヴィンテージ。**セパージュ 60/40・20 の GC/1er Cru・**各年の公式テイスティングノート**（2013 / 2012 は「7 年熟成」と明記） |
| 🔴 **`/en/champagnes/4/cuvee-sir-winston-churchill`** | 🔴 **13 ヴィンテージ（2018 を含む）。**「1975 年創設」「Old Lion」「Churchill 存命中の畑に限る」「グラン・クリュのみ」「10 年超熟成」「常に他より遅くリリース」「正確な配合は家族の秘密」 |
| 🔴 **`/en/champagnes/8/vinotheque-brut-vintage`** | 🔴 **`Édition Vinothèque` の定義（175 周年・再カーヴ入れ・歴史的デザイン・手作業・木箱）。**2006 / 2004 / 2002 / 2000 の各テイスティングノート |
| 🔴 **`/en/champagnes/11/vinotheque-cuvee-sir-winston-churchill`** | 🔴 **2004 / 2002 / 1999 / 1998。**⚠️ **一度 `error code: 520` を返し、再試行で取得。** **醸造長 `Damien Cambres` の名と「三次元的」という評** |
| **`/en/philosophy/excellence-champagne`** | 🔴 **「175 years of history, six generations & Independence」・卓越と独立の定義・ブドウ栽培者の選定と購入ブドウの選別** |
| **`/en/philosophy/style-champagne`** | **「紳士のシャンパーニュ」（Jean-Paul Kauffmann『Voyage en Champagne』）・Churchill と英国王室・Avenue de Champagne** |
| `/en/`（トップ・194 KB） | ナビゲーション構造。⚠️ **年表は `uneFriseHistoire` クラスの JS 描画で、静的取得では中身が無い** |

**取得できなかったもの / 存在しなかったもの**
- 🔴 **`/en/history/the-house` と `/en/history/the-family` が静的取得で本文を返さない。**
  **創業年・世代ごとの当主・Churchill との交流史はすべて未取得。**
- 🔴 **`/f/file/our-commitments.pdf`（1.1 MB）にテキストレイヤーが無い。**
  **環境・栽培のコミットメントが書かれている可能性が高いが読めていない。** → **OCR が要る。**
- 🔴 **自社畑の面積・所有クリュ・購入比率が公式に無い。**
- 🔴 **ドザージュ（g/L）・アルコール度数・デゴルジュマン日・生産本数がどのキュヴェにも無い。**
- ⚠️ **`/en/news/press-review`（プレスレビュー）と `/en/news-champagne/321/tribute-to-patrice-noyelle`、
  `/en/news-champagne/309/entreprise-du-patrimoine-vivant` は本調査で未読。**
- ⚠️ **`/sitemap.xml` は存在しない**（`robots.txt` が `sitemap.php` を指す）。

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔴 **canonical 生産者レコード: 存在しない**（384 件走査 → 0）／canonical キュヴェ **0 件**／
OBP **6 本**（すべて `match_state = unresolved`、`producer_state` も `unresolved`。
セクションは全て `FRANCE | SPARKLING > CHAMPAGNE | BLENDS`）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **Medium-High** | 所在・法人名・醸造長・「175 年 6 世代」は確定。🔴 **創業年が取れていない** |
| Overview | **High** | 卓越と独立という自己規定、購入ブドウの明示、醸造の 4 つの署名がすべて一次で取れた |
| **History** | 🔴 **Low** | **年表ページが JS 描画で未取得。**確定できたのは **1975 年（SWC 創設）と 175 周年（Vinothèque 開始）**の 2 点のみ |
| Location | **Medium** | Épernay / Avenue de Champagne / 地下 33 m / キュヴェ別の産地は確定。🔴 **自社畑の情報がゼロ** |
| **Farming** | 🔴 **None** | **公式サイトに栽培の記述が実質的に無い。**認証への言及もゼロ。**`our-commitments.pdf` が読めていない** |
| **Winemaking** | **High** | 🔴 **全工程（2 回のデブルバージュ・6 °C 24 h・18 °C 以下・全 MLF・9 °C 瓶内・33 m・手ルミュアージュ）と、キュヴェ別のセパージュ・リザーヴ比率・熟成年数が公式。**⚠️ **ドザージュと分析値のみ不在** |
| **Style** | **High** | 🔴 **OBP 掲載 6 本すべての公式テイスティングノート。**メゾンのスタイル自己規定も |
| **Important Cuvées** | **High** | 🔴 **OBP 6 本すべてについて、公式のヴィンテージ一覧に該当年が実在することを確認。**全 11 キュヴェと 4 系統のヴィンテージ一覧を取得 |
| Staff Notes | **High** | ⚠️ 11 項目。🔴 **「自社畑」「創業年」「SWC のセパージュ」「Vinothèque は別ワイン」という 4 つの誤りを塞いだ** |
| **総合** | **Medium-High — staff-usable（70% を超過）。** | **OBP 掲載 6 本すべてについて、公式の正式名・セパージュ・熟成・造り手のテイスティングノートを言える。** 欠けているのは**沿革・栽培・分析値**で、**沿革と栽培は取得手段が残っている**（JS 描画ページと PDF の OCR）。 |

**reached_70: YES.**

---

## Open Questions

1. 🔴 **canonical に生産者レコードが無い。** OBP 6 本すべてが `producer_state = unresolved`。
   **登録するなら、`Édition Vinothèque` をどう表現するかを同時に決めねばならない。**
   🔍 **`V-3`（Dom Pérignon Plénitude）と同型であり、`vintages.release_label` を使うのが整合的。**
   → **canonical への書き込みは本書では行っていない。** 昇格可否は Akio / CTO 判断。
2. 🔴 **沿革ページ（`/en/history/the-house` / `/the-family`）が JS 描画で取得できていない。**
   **創業年・世代の系譜・Churchill との交流史がすべて空白。**
   → **ブラウザ描画で取得すれば埋まる。**（本調査では同意バナーの操作が必要となったため中止した。）
3. 🔴 **`/f/file/our-commitments.pdf` にテキストレイヤーが無い。**
   **栽培・環境方針が書かれている可能性が高い。** → **OCR すれば §Farming の空白が埋まる。**
4. ⚠️ **OBP の `'Cuvée de Réserve, Vinothéque,'` という印字。**
   **公式の名称は `Brut Vintage Édition Vinothèque` であり、`Cuvée de Réserve` を含まない。**
   🔍 **`Cuvée de Réserve` は Pol Roger のヴィンテージ物の歴史的な呼称である可能性があるが、
   現行の公式サイトでは確認できなかった。ラベル実物での確認が要る。**
5. ⚠️ **OBP の 6 本目 `Pol Roger | Brut | 2016`（ラベル語なし・$505）。**
   🔍 **公式の `Brut Vintage` に 2016 が実在し、Pol Roger にヴィンテージ入りの「ただの Brut」は無いため、
   `Brut Vintage 2016` と読むのが最も整合する。**
   ⚠️ **ただし 2 行目の `'Vintage,' Brut 2018` が $415 なのに対しこちらが $505 と高い。**
   **実リストでの確認が要る。**
6. **SWC のセパージュ比率。** 公式が「家族の秘密」と明言しており、**恒久的に不明である。**
7. **ドザージュ・アルコール度数・デゴルジュマン日・生産本数。** 公式に一切無い。
   → **輸入元のテクニカルシートが要る。**
8. **自社畑の有無と規模。** 公式は購入ブドウに言及するが、自社畑については沈黙している。
9. **`/en/news/press-review` が未読。** 第三者評価の掲出があるか未確認。
10. **`Entreprise du Patrimoine Vivant` 認定の年と内容が未読**（`/en/news-champagne/309/`）。
    **`Primum Familiae Vini` への加盟も記事から確認できるが、加盟年は未取得。**
