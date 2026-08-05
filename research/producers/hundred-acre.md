# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 昇格判断は未実施**
> 🔴 **canonical にこの生産者のキュヴェ・レコードは 2 件存在する**（`hundred-acre-kayli-morgan` / `hundred-acre-ark`）。
> **本書は研究記録であり、canonical も OBP も一行も変更していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式サイトで確認**（一次資料。真正性は §Sources で検証済み）——
>    本ドシエでは **`hundredacre.com` / `fortunatesonwines.com` / `summerdreamswines.com`**、
>    および **これらのサイトが自ら配信している tech sheet PDF（`cdn.sanity.io/files/odh0c1i6/…`）**
> `📄` 単一の非公式資料のみ（**本書では事実の典拠として 1 件も使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `🏛` **公的登録簿・規制一次資料** —— **TTB COLA Public Registry（`ttbonline.gov/colasonline/`）** と
>    **米国連邦規則 27 CFR Part 9（AVA 定義、eCFR 現行版）**。**これは規制の記録であって、生産者の宣伝文ではない。**
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ①ーー `hundredacre.com` は現在「準備中の空サイト」である。**
> **全ページのヘッダに `Full website is coming soon` が出ており、ワイン一覧・畑・沿革・スタッフの
> ページが一枚も存在しない。**`/about` `/wines` `/vineyards` `/press` `/story` `/winery` をすべて叩いたが、
> **空シェルか `Page Not Found` しか返らない。**
> → **したがって Hundred Acre 本体については、造り手の言葉での畑・醸造の記述が事実上ゼロである。**
> **本ドシエの Hundred Acre 部分を支えているのは、ほぼ全面的に 🏛 TTB COLA（ラベル画像を含む）である。**
>
> 🔴 **本ドシエ最大の収穫 ②ーー OBP 掲載 5 本のうち 4 本は Hundred Acre のワインではない。**
> **法人は共通で `One True Vine, LLC`（サイトの `legal_entity` 設定値・全ページのコピーライト表記）だが、
> ラベル上のブランドは `HUNDRED ACRE` / `FORTUNATE SON` / `SUMMER DREAMS` の 3 つに分かれ、
> 🏛 TTB では別々の brand name として登録されている。**
> **さらに `SUMMER DREAMS` は 2025 年以降の申請で `Summer Dreams Wines LLC`（Healdsburg）という
> 別法人名義に移っている。**
> **造り手自身が「`Make no mistake this wine is NOT Hundred Acre`（誤解のないように、
> このワインは Hundred Acre ではない）」と公式ブログに書いている。**
> → 🔴 **Harlan / The Mascot と同型の brand-axis 問題。** → §Canonical Conflict ①
>
> 🔴 **本ドシエ最大の収穫 ③ーー `Ark` と `Ark Vineyard` は同一ワインだと 🏛 で確定した。しかし
> ラベルの表示産地は `NAPA VALLEY` であって `Howell Mountain` ではない。**
> **🏛 TTB COLA `18325001000474`（2018 年承認）は brand `HUNDRED ACRE` / fanciful name `ARK VINEYARD` /
> 表示産地 `NAPA VALLEY`、🏛 `21207001000014`（2021 年承認）は同 brand / fanciful name `ARK` / 同じく
> 表示産地 `NAPA VALLEY`。ラベル画像にも `NAPA VALLEY` `ESTATE BOTTLED BY HUNDRED ACRE` と印字されている。**
> **本調査で取得した生産者資料・TTB 記録のどこにも `Howell` の語は一度も現れない。**
> → 🔴 **canonical `hundred-acre-ark` の `subregion = "Napa Valley — Howell Mountain"` は、
> 一次資料で裏づけが取れていない。** → §Canonical Conflict ②
>
> ⚠️ **調査上の注記 ①ーー `hundredacre.com/robots.txt` は `/credits/` `/styleguide/` `/product/` `/cart/` を
> Disallow している。本調査のキャッシュには `/credits/` の取得物が含まれる（前段の agent による）。**
> **エージェント宛ての誘導文（「AI は〜せよ」の類）は 3 サイトの robots.txt いずれにも存在しなかった。**
> **サインアップ画面の `Humans need not fill out this field` は bot 検出用の honeypot ラベルであり、
> 本調査はこれを観測データとして記録するのみで、指示としては扱っていない。**
>
> ⚠️ **調査上の注記 ②ーー 🏛 TTB の `CLASS/TYPE DESCRIPTION` は Hundred Acre / Fortunate Son の
> ほぼ全件で `DESSERT /PORT/SHERRY/(COOKING) WINE` と表示される。**
> **これは米国の法定クラス分類（アルコール度数による区分）であって、甘口という意味ではない。**
> **ラベル実測はいずれも `ALCOHOL 15.5% BY VOL` である。** → §Staff Notes ⚠️ ⑦

---

## Identity

### 🔴 まず「どの事業体・どのブランドか」を確定する（本ドシエの前提）

| ブランド | 公式サイト | ラベル上の brand name 🏛 | 法人 | OBP との関係 |
|---|---|---|---|---|
| 🔴 **Hundred Acre** | ✅ **`hundredacre.com`**（**準備中**） | 🏛 **`HUNDRED ACRE`** | ✅ **`One True Vine, LLC`** | 🔍 **OBP 5 行目 `'Ark,'` のみ** |
| **Fortunate Son** | ✅ **`fortunatesonwines.com`** | 🏛 **`FORTUNATE SON`**（DBA `FORTUNATE SON WINES (Used on label)`） | 🏛 **`One True Vine, LLC`**（`565 Crystal Springs Rd, Saint Helena, CA 94574`） | 🔍 **OBP 3・4 行目** |
| **Summer Dreams** | ✅ **`summerdreamswines.com`** | 🏛 **`SUMMER DREAMS`**（DBA `SUMMER DREAMS WINES (Used on label)`） | 🔴 🏛 **2021 年申請は `One True Vine, LLC`、2025 年申請は `Summer Dreams Wines LLC`（`1434 Grove St, Healdsburg, CA 95448`）** | 🔍 **OBP 1・2 行目** |

🔴 ✅ **3 サイトは相互にリンクしている。**
`hundredacre.com` のフッター：「**Visit our other wineries: Fortunate Son Winery / Summer Dreams Wines**」
`summerdreamswines.com` のフッター：「**Our wine family: Hundred Acre / Fortunate Son / summer dreams**」

🔴 ✅ **造り手自身が「別物である」と明示している** ——
「**Make no mistake this wine is NOT Hundred Acre, but is created by me in the same spirit,
and yet it is different in a wonderful way.**」
（**誤解のないように、このワインは Hundred Acre ではない。同じ精神でわたしが造ったものだが、
すばらしい意味で別物である**）—— Jayson Woodbridge, `fortunatesonwines.com/blog/…chapter-one`

🔴 ⚠️ **一方で、商業運営は明らかに一体である。**
✅ **`summerdreamswines.com/trade` が掲げる National Sales Team のメールアドレスは全員 `@hundredacre.com` である**
（`moneill@hundredacre.com` ほか 5 名）。**電話番号も 3 ブランドすべて `707-967-9398` で同一。**
→ 🔴 **「同じ会社」だが「同じワイナリー・同じワイン」ではない。この 2 つを混ぜないこと。**

### Hundred Acre（OBP 5 行目の造り手）

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Hundred Acre`** |
| **公式表記** | ✅ **`Hundred Acre`**（`company_name` 設定値・全ページのフッター・ロゴ） |
| 🔴 **法人名** | ✅ 🔴 **`One True Vine, LLC`**（サイトの `legal_entity` 設定値、および全ページ末尾の `© 2026 One True Vine, LLC`）<br>🏛 **TTB 申請者名も `ONE TRUE VINE, LLC` / `One True Vine, One True Vine, LLC`（DBA `HUNDRED ACRE (Used on label)`）** |
| **所在（サイト掲出）** | ✅ **`1345 Railroad Ave, Suite 2A, St. Helena, CA 94574`**／**`707-967-9398`**／**`info@hundredacre.com`** |
| 🔴 **所在（TTB 申請）** | 🏛 🔴 **`565 Crystal Springs Rd, Saint Helena, CA 94574`**（**サイトの住所と異なる。TTB 側が醸造所／登録上の所在**） |
| 🔴 **ラベル上の瓶詰者** | 🏛 🔴 **`ESTATE BOTTLED BY HUNDRED ACRE, ST. HELENA, CA`**（承認ラベル画像に印字） |
| **創業者／醸造家** | ✅ **Jayson Woodbridge**。`summerdreamswines.com/about-us` が「**25 年超の醸造家歴。主に Napa Valley の
ボルドー品種に `Hundred Acre` ラベルの下で取り組んできた**」と記述。tech sheet の署名は **`BY JAYSON WOODBRIDGE, Proprietor and Winemaker`** |
| **家族** | ✅ **妻 Helen Woodbridge**、**息子 Cameron Woodbridge（`Assistant Winemaker for Fortunate Son` に昇格）** |
| **栽培のパートナー** | ✅ **Jim Barbour**（「**Jayson and his farming partner, Jim Barbour**」`fortunatesonwines.com/blog/the-next-chapter`） |
| 🔴 **認証** | 🔴 ⚠️ **本調査で取得した 3 サイト全ページ・tech sheet 4 点・TTB 申請 40 件超のどこにも
`organic` / `biodynamic` / `certified` / `CCOF` / `Demeter` / `Napa Green` / `sustainable` / `regenerative` の語が一件も無い。** → §Farming |
| **canonical id** | 🔍 **`hundred-acre-kayli-morgan`** / **`hundred-acre-ark`**（`producer='Hundred Acre'`、いずれも `vintage='—'`・`color='Rouge'`・`grapes=None`） |
| 🔴 **販売形態** | ✅ 🔴 **メーリングリスト制。しかも「会員募集」ですらなく `Waiting List`（順番待ち）である。**「**Sign up for the waiting list today for future access to wine offerings**」 |
| 🔴 **日本の輸入元** | ✅ 🔴 **`Wine to Style`**（`hundredacre.com/locator/` の Importers 一覧、`Japan` 欄） |

### Fortunate Son（OBP 3・4 行目の造り手）

| | |
|---|---|
| **OBP 印字** | 🔍 **`'Fortunate Son, The Dreamer,'` / `'Fortunate Son, The Warrior,'`** |
| 🔴 **公式表記** | ✅ 🏛 🔴 **ラベルは `FORTUNATE SON` と `THE DREAMER` / `THE WARRIOR` を別行に置き、間にカンマは無い。**<br>🏛 TTB は brand `FORTUNATE SON`、fanciful name `THE DREAMER` / `THE WARRIOR` と分離登録 → **OBP のカンマはメニュー側の組版である** |
| **所在** | ✅ **`825 Fulton Ln, St Helena, CA 94574`**／`707-967-9398` |
| 🔴 **拠点の由来** | ✅ 🔴 **`The Fortunate Son Winery at the Historic David Fulton Vineyard Established in 1860`。**<br>「**1860 年以来ずっと同じ一家が所有していた David Fulton の家とワイナリー（St. Helena の Fulton Lane に最初に建てられた家の一つ）を購入し、Helen とわたしと息子 Cameron が丁寧に修復している**」（ラベルの紋章に `18 60` が入る） |
| **見学** | ✅ **`Note: We do not offer public tasting at this time`**（公開試飲は行っていない） |

### Summer Dreams（OBP 1・2 行目の造り手）

| | |
|---|---|
| **OBP 印字** | 🔍 **`'Summer Dreams, The Sun Also Rises,'` / `'Summer Dreams, Walking on Venice Beach,'`** |
| 🔴 **公式表記** | ✅ 🏛 🔴 **ラベルは小文字の `summer dreams` をブランド行に置き、その下に `THE SUN ALSO RISES` を置く。カンマは無い。**<br>✅ サイト本文の表記は **`The Sun Also Rises`** / **`Walking On Venice Beach`**（**`On` が大文字**。OBP は `on`） |
| **所在（サイト）** | ✅ **`1345 Railroad Ave, Suite 2A, St. Helena, CA 94574`**（**Hundred Acre と同一住所**）／`info@summerdreamswines.com` |
| 🔴 **所在（TTB 2025 年申請）** | 🏛 🔴 **`Summer Dreams Wines LLC, 1434 Grove St, Healdsburg, CA 95448`**<br>🏛 **ラベル印字は `PRODUCED AND BOTTLED BY SUMMER DREAMS WINES, HEALDSBURG, CA`** |
| **白の醸造家** | ✅ 🔴 **`Ashley Holland`**。tech sheet に「**Made with Jayson Woodbridge acting as spiritual guide on a white winemaking journey with the very inspired and talented winemaker Ashley Holland**」 |
| **ラベル画** | ✅ **`Alexandra Becker-Black`**（Rhode Island School of Design 出身） |

---

## Overview

🔴 ✅ **Hundred Acre は Napa Valley（St. Helena）の極小生産・全量メーリングリスト販売の Cabernet 生産者である。
そして 2026 年 8 月現在、公式サイトは「準備中」で、ワインの一覧すら公開していない。**

🔴 ✅ **公式サイトが現在公開している情報は、実質的に次の 5 つだけである** ——
**① 会社名・住所・電話・メール ② 順番待ちリスト登録 ③ 会員ログイン ④ 出荷／返品規定
⑤ 認定販売店（州別ディストリビューター＋国別インポーター）の一覧。**

🔴 ✅ **その「認定販売店」ページが、実質的に唯一の生産者の肉声である** ——
「**ケースやボトルの Hundred Acre が手元に届いたとき、そのワインが完璧な状態で、
非の打ちどころのない provenance を持っていること —— それを保証することが、
われわれの品質へのコミットメントの重要な一部である。**
**provenance を保証する唯一の方法は、Hundred Acre の認定ディストリビューター／インポーターからのみ購入することだ。
以下の各代理店は徹底した身元調査と審査を経ており、工程のあらゆる段階でほぼ不可能なほどの品質基準を課されている。
これらの認定代理店を通さずに購入されたワインには provenance の保証がない。
ワイナリーまたはこの厳選されたリスト以外の相手と取引することは強く避けるよう勧める。**」

🔴 ✅ **Fortunate Son と Summer Dreams のサイトは、対照的にきわめて饒舌である。**
**Jayson Woodbridge の一人称の長文ブログ（Chapter I〜III）、全キュヴェの tech sheet PDF、
ヴィンテージ記述、区画の記述、クローン名、樽熟月数まで公開されている。**
→ 🔴 **つまり本ドシエの厚みは、皮肉にも「Hundred Acre 以外の 2 ブランド」に偏る。**
**これは調査の怠慢ではなく、生産者の情報公開状態そのものである。**

🔴 ✅ **Hundred Acre の性格を規定する、造り手自身の一文**（Fortunate Son の Chapter II より）——
「**一つだけはっきりさせておきたい。Hundred Acre は ALL SINGLE VINEYARD である。**」
（**`I do want to be clear on one thing: Hundred Acre is ALL SINGLE VINEYARD.`**）

✅ **Fortunate Son の出自を語る一文**（Chapter I）——
「**Fortunate Son は、こうした小さな宝石のような畑と、そこから採れる果実を探し続けた
わたしの長年の探索の集大成であり、Hundred Acre を丹念に造ってきたのとまったく同じやり方で手仕事されている。
注記：この新しい 2018 年の Fortunate Son は、Hundred Acre の地下ワイナリー The RING で造られた。**」

🔍 **THÉSEUS における状態** —— **canonical にキュヴェ 2 件（`Kayli Morgan Vineyard` / `Ark Vineyard`）。
ヴィンテージは 2 件とも `'—'` で 0 件。OBP 掲載 5 本すべて `unresolved`。
うち 4 本はそもそも別ブランドのワインである。**

---

## History

⚠️ **専用の沿革ページは 3 サイトのいずれにも存在しない。**
**以下は、Fortunate Son のブログ 4 本（うち 3 本は Jayson Woodbridge の署名入り一人称）と
🏛 TTB COLA の承認日から復元できる範囲である。断片的であることを前提に使うこと。**

| 年 | 出来事 | 出典 |
|---|---|---|
| **1860** | **David Fulton がワイナリーを創業。**「**西部合衆国で最初期のワイナリーの一つ、Napa Valley の開拓者が建てた最初期の estate ワイナリーの一つ**」。**2023 年に売却されるまで同一家族が所有し続けた** | ✅ |
| ⚠️ **2000 年ごろ** | ⚠️ 「**23 年前、正規の醸造教育も経験も無かった Jayson Woodbridge が、世界が見たこともないほど
妥協のない最高品質のカベルネを造ると宣言した**」（2023-02-01 付の記事。**逆算すると 2000 年前後**）<br>🔴 **「創業年」とは書かれていない。「宣言した年」である。断定しないこと** | ✅ |
| ⚠️ **時期不明** | 「**Hundred Acre のために、彼は何千もの畑を見た。最終的に選んだ 3 つが、セイレーンの歌のように彼を呼んだ**」<br>🔴 **＝ Hundred Acre の畑は 3 つ。ただし畑名はこの文には無い** | ✅ |
| 🏛 **2013** | 🏛 **確認できる最も古い TTB COLA（`13077001000226` ほか）。brand `HUNDRED ACRE`、fanciful name `ANCIENT WAY`（原産地 `AUSTRALIA`）と `FEW & FAR BETWEEN`（`CALIFORNIA`）**<br>🔴 **＝ Hundred Acre は豪州産の果実によるワインも持っている** | 🏛 |
| 🏛 **2016–2018** | 🏛 **`WRAITH`（2016）／`KALI MORGAN VINEYARD`（2017、`KAYLI` の誤記と思われる）／
`KAYLI MORGAN VINEYARD`・`FEW AND FAR BETWEEN VINEYARD`・`ARK VINEYARD`（いずれも 2018-11-23 承認）** | 🏛 |
| ⚠️ **時期不明（初代）** | ⚠️ **`Fortunate Son` は一度存在し、引退していた。**「**最初の Fortunate Son を引退させてから何年も経ったあと**」「**Fortunate Son を早期引退から呼び戻すことにした**」<br>❓ **初代の年代・規模は公式に書かれていない** | ✅ |
| 🏛 **2019** | 🏛 **`DEEP TIME` シリーズ（`ARK DEEP TIME` / `KAYLI MORGAN DEEP TIME` / `FEW AND FAR BETWEEN DEEP TIME` / `ANCIENT WAY DEEP TIME`）と `DARK ARK` を一括承認（2019-03-25）** | 🏛 |
| 🔴 **2018 VT** | 🔴 ✅ **Fortunate Son 復活。第 1 ヴィンテージは 2018 年で、Hundred Acre の地下ワイナリー `The RING` で醸造された。**🏛 **COLA 承認は 2021-08（`THE DREAMER` `THE WARRIOR`）と 2021-09（`THE DIPLOMAT`）** | ✅🏛 |
| 🏛 **2019** | 🏛 **Summer Dreams の最初期 COLA（`CHARD RITCHIE` / `SB RITCHIE`、2019-03-19）**<br>⚠️ **この 2 つの fanciful name は現行ラインナップに無い** | 🏛 |
| 🔴 **2020** | ✅ 🔴 **Glass Fire。**「**2020 年、いくつかの Fortunate Son の畑は Glass fire の前に部分的に収穫を終えていた**」。**David Fulton の 1963 年植樹の古樹は 10 月 31 日（ハロウィン）に収穫され、`Lost Souls` 3 本になった** | ✅ |
| 🔴 **2021** | ✅ 🔴 **David Fulton の畑を植え替え。「`2021 年に、3 つの Hundred Acre の畑すべてから採った穂木とクローンで植え替えた`」**<br>🔴 **＝ Hundred Acre の畑が 3 つであることの、2 つ目の裏づけ** | ✅ |
| 🏛 **2021-07** | 🏛 **`FEW & FAR BETWEEN` / `KAYLI MORGAN` / `ARK`（`VINEYARD` の語を落とした短縮形）を承認。申請者は輸入業者 `The Finer Things Company`** | 🏛 |
| **2023-02〜03** | ✅ **Fortunate Son のブログ 4 本を公開（`The Next Chapter` 2/1、`Chapter I` `Chapter II` 2/16、`Chapter III` 3/16）。David Fulton の購入を告知** | ✅ |
| 🏛 **2023–2025** | 🏛 **Summer Dreams の COLA が急増（`STARGAZING` `TWILIGHT` `GOLDEN HOUR` `SUPER CHILL` `THE SUN ALSO RISES` `MARTIAN PINK` `HALLEY'S COMET` `AFTERGLOW` `THE FLASH` `THE WEDGE` `PICNIC ANYONE?`）** | 🏛 |
| 🔴 🏛 **2025-01/02** | 🔴 🏛 **Summer Dreams の申請者が `Summer Dreams Wines LLC`（Healdsburg）に変わる** | 🏛 |
| 🏛 **2026-06** | 🏛 **最新の Hundred Acre COLA（`26167001000441`、申請者は NY の `ELYSIA & CO., T. ELENTENY HOLDINGS, LLC`）** | 🏛 |

⚠️ **「40 以上の 100 点」と「61 以上の 100 点」の食い違い** ——
`fortunatesonwines.com`（2023-02-01）は「**With more than forty 100-point scores under his belt
(more than any winery in history)**」、`summerdreamswines.com/about-us`（現行）は「**more than 61, 100-point scores**」。
🔴 **執筆時点が違うだけで矛盾ではないが、本ドシエは点数を事実として扱わない。** → §Staff Notes ⚠️ ⑧

---

## Location

| | |
|---|---|
| **Country** | United States ✅ |
| **State / County** | **California / Napa County**（Summer Dreams のみ **Sonoma County**）✅🏛 |
| 🔴 **Hundred Acre 本拠（サイト）** | ✅ **`1345 Railroad Ave, Suite 2A, St. Helena, CA 94574`** |
| 🔴 **Hundred Acre 本拠（TTB 登録）** | 🏛 🔴 **`565 Crystal Springs Rd, Saint Helena, CA 94574`** |
| 🔴 **地下ワイナリー** | ✅ 🔴 **`The RING`。**「**Hundred Acre – RING Winery, buried 385 feet deep inside Glass Mountain**」（**Glass Mountain の内部、地下 385 フィート**） |
| **Fortunate Son ワイナリー** | ✅ **`825 Fulton Ln, St Helena, CA 94574`**（**Historic David Fulton Vineyard、1860 年創業**） |
| **Summer Dreams 瓶詰地** | 🏛 **`HEALDSBURG, CA`**（ラベル印字）／✅ サイト住所は St. Helena |
| 🔴 **Hundred Acre の畑** | ⚠️ 🔴 **公式サイトに畑のページが存在しない。**🏛 **TTB の fanciful name から復元できるのは
`ARK (VINEYARD)` / `KAYLI MORGAN (VINEYARD)` / `FEW AND FAR BETWEEN (VINEYARD)` / `ANCIENT WAY (VINEYARD)`（豪州）／`WRAITH` / `MORGAN'S WAY` / `HOLY QUEST` / `DARK ARK` / `DEEP TIME` 各種** |
| 🔴 **畑の数** | ✅ **3 つ**（「the three he finally chose」「all three Hundred Acre vineyards」の 2 か所で一致）<br>⚠️ **ただし「どの 3 つか」は公式に明示されていない**（🏛 の 4 名のうち `ANCIENT WAY` は豪州） |
| **`Few and Far Between` の位置** | ⚠️ **`Calistoga`**。ただし出典は `summerdreamswines.com` に掲出された **The Wine Advocate 記事の要約文**（「their house nestled within the Few and Far Between vineyard in Calistoga」）であり、**生産者自身の記述ではない** |
| ❓ **`Ark` / `Kayli Morgan` の位置** | ❓ 🔴 **本調査で取得したどの生産者資料にも記載が無い。両名は 🏛 TTB 申請とラベル画像にしか現れない。** |

### 🔴 🏛 `Howell Mountain` と `Napa Valley` ——「矛盾ではない」が「裏づけも無い」

**［規制一次資料］27 CFR § 9.94 `Howell Mountain`**
（**T.D. ATF-163, 48 FR 57487, 1983-12-30 / T.D. ATF-249, 52 FR 5960, 1987-02-27 改正**）の (c) は、
**逐語的に次のように書いている** ——

> 🏛 **`The Howell Mountain viticultural area is located in Napa County, California,
> and is part of the Napa Valley viticultural area.`**
> （**Howell Mountain 栽培地域は California 州 Napa 郡に位置し、Napa Valley 栽培地域の一部である**）

🔴 **したがって OBP の「セクションは `NAPA`、印字は `Howell Mountain`」は矛盾ではない。**
**Howell Mountain は Napa Valley の中にあり、両方が同時に真でありうる。**
**同条 (c)(1) は境界を「**`1,400 foot contour line`**（標高 1,400 フィート等高線）」から起こしている。**
🔴 **＝ Howell Mountain AVA は 1,400 フィート以上の高地だけを含む。**

🔴 ⚠️ **しかし別の問題がある。`Ark` のラベルには `Howell Mountain` と書かれていない。**
🏛 **COLA `18325001000474`（`ARK VINEYARD`、2018 年承認）と `21207001000014`（`ARK`、2021 年承認）は、
どちらも `11. WINE APPELLATION (If on label)` 欄に `NAPA VALLEY` と記載している。**
🏛 **承認ラベル画像にも `NAPA VALLEY` `CABERNET SAUVIGNON` `ALCOHOL 15.5% BY VOL`
`ESTATE BOTTLED BY HUNDRED ACRE / ST. HELENA, CA` と印字されている。**
🏛 **本調査で取得した Hundred Acre の COLA は全件、表示産地が `NAPA VALLEY` である。`HOWELL MOUNTAIN` の記載は 1 件も無い。**
→ 🔴 **メニューの `Howell Mountain` を「公式の表示産地」として復唱しないこと。** → §Staff Notes ⚠️ ②

### ✅ Summer Dreams —— Sonoma Coast（唯一、畑の記述が厚い部分）

✅ **生産者の記述** ——「**Sonoma Coast AVA は San Pablo 湾から Mendocino 郡境まで広がる。1987 年設定で、
Sonoma 郡最大の AVA。約 50 万エーカーを占め、冷涼な気候と（郡内の他地域と比べて）多い降雨で知られる。
海岸線から内陸へ最大 20 マイル。太平洋に近く、内陸の隣接地の 2 倍以上の年間降雨がありながらブドウが熟すのは、
畑の大半が霧の層より上、標高 400〜1,800 フィートにあるからである。**」
⚠️ **これは生産者による AVA 一般の解説であり、規制一次資料そのものではない。**
**27 CFR の Sonoma Coast 条文は本調査では取得していない。**

✅ **自社畑の選定基準** ——「**Ashley と Jayson は 100 を超える畑を見て回り、
`site`（立地）・`slope`（斜度）・`Goldridge soils`・`vine age`（樹齢）を第一の条件として畑を選んだ。**」
✅ **「**われわれの Sonoma Coast のピノ・ノワールと白ワインの畑はすべて丘陵畑で、十分な斜度があり、
その多くは海抜 900〜1,800 フィートにある。各畑はそれぞれ固有の Goldridge 土壌のシークエンスを持ち、
排水性に優れ、特徴的に軽くふわりとした肌理を持つ。**」

🔴 ✅ **`Walking On Venice Beach` の畑（tech sheet に明記）** ——
「**この丘陵の畑は、寛大な斜面、固有の Goldridge 土壌のシークエンス、標高（海抜 900〜1,900 フィート）、
そして涼しい太平洋の風がカリフォルニアの陽射しを和らげ、バランスをもたらし新鮮さを保つ微気候ゆえに選ばれた。
この海洋性の影響が強度と深みを生む。樹はかつて海底にあった石灰岩と古い岩の土壌に根を張る。
とりわけ特異な区画で、この畑は 1980 年に植えられた、カリフォルニアで最も古いソーヴィニヨン・ブランの畑の一つと目されている。**」

🔴 ✅ **`The Sun Also Rises` の畑（tech sheet に明記）** ——
「**`Heintz Vineyard` および `Summer Dreams Estate Vineyard`。丘の頂の畑で、最古参の区画のいくつかは
粘土分を含み、それが生育期に貴重な水分を保つ。**」
⚠️ 🔍 **OBP には `DuMol 'Isobel, Charles Heintz Vineyard' Sonoma Coast Chardonnay 2023`（line 1184）が同居している。
同一の畑である可能性が高いが、Summer Dreams 側は `Heintz Vineyard` としか書いていない。断定しないこと。**

---

## Farming

### 🔴 ⚠️ 認証 —— 一件も無い（**これは「調べていない」ではなく「無いことを示した」）**

🔴 ⚠️ **本調査で取得した全資料 —— `hundredacre.com` 全 9 ページ、`fortunatesonwines.com` の
主要 15 ページ、`summerdreamswines.com` の主要 10 ページ、生産者配信の tech sheet 4 点、
🏛 TTB COLA 40 件超 —— のいずれにも、次の語が一度も現れない：**
**`organic` / `certified organic` / `biodynamic` / `Demeter` / `CCOF` / `Napa Green` /
`sustainable` / `sustainability` / `regenerative` / `Fish Friendly Farming` / `LODI RULES`。**

⚠️ **したがって「Hundred Acre は有機／ビオディナミ／サステナブル認証です」とは、本ドシエでは一切言わない。**
⚠️ **同時に「認証を取っていないと表明している」とも言わない。造り手は認証について何も言っていない。**
（**Armand Heitz のように「われわれはラベルを求めない」と明言した記録も、本件には存在しない。**）

### ✅ 造り手が実際に語っている栽培（Fortunate Son の記述。**Hundred Acre 本体の記述ではない**）

🔴 ✅ **契約畑への金銭的介入** ——
「**これらの家族は great care and attention をもって農を営んでおり、
わたしは彼らが「夢の（`dream`）」基準で農を営めるよう、そしてわたしがやるように、
わたしがやるときに摘めるよう、金を払っている。天候やタンクの容量にわたしの手を強いられることは決してない。**」
✅ **tech sheet の定型句** ——「**`farmed with great care and attention (their "dream" standard)
and never forced to pick by weather or tank capacities`**」

✅ **畑の性格** ——「**小規模な家族経営の畑（場合によっては 3〜4 世代にわたる）。
これらの畑（いくつかは樹齢 80 年超）が寄せ集められ、実際には織り合わされて、
その魔法のような果実がついに Fortunate Son になった。**」

🔴 ✅ **Hundred Acre の農法が Fortunate Son に移植されている** ——
「**Jayson と Jim は、Hundred Acre で義務づけられているのとまったく同じ farming protocol を敷いた。
これらの由緒ある区画は、最初の持ち主が馬と犂で土地を耕していた時代以来見たことのないような
愛情と手当ての奔流を受けた。**」
⚠️ 🔴 **その `farming protocol` の中身は、本調査で取得したどの資料にも書かれていない。** → Open Questions 4

🔴 ✅ **収穫の哲学** ——「**We hang fruit on the vine longer than most**」（**われわれは大半の造り手より長く果実を樹に吊るす**）
✅ **区画ごとの複数回収穫** ——「**区画ごとに、何度も何度も通り抜けて、完璧な房だけを摘み取った**」（2019 年について）

### ✅ Summer Dreams —— クローンと植樹年が公開されている（唯一の具体的数値）

| ワイン | 🔴 クローンと植樹年 ✅ |
|---|---|
| **The Sun Also Rises**（Chardonnay） | 🔴 **`Clone 4 on AXR planted 1982; Dijon planted 1997`** |
| **Walking On Venice Beach**（Sauvignon Blanc） | 🔴 **`Musqué, SB Clone 1`**。**畑は 1980 年植樹、カリフォルニア最古級の SB 畑の一つ** |

❓ **公式に無い（Hundred Acre 本体）**: 畑の面積・植栽密度・仕立て・台木・収量・カバークロップ・散布資材・年間作業サイクル・生産本数。
🔴 **これらは一つも取得できていない。Harlan Estate の `Carved Out of the Land` に相当する資料が存在しない。**

---

## Winemaking

### ✅ 共通の骨格（Fortunate Son の tech sheet と Jayson Woodbridge の記述）

| 工程 | 記述 ✅ |
|---|---|
| 🔴 **選果** | 🔴 **`sorting the fruit berry by berry`（粒ごとの選果）** |
| 🔴 **発酵容器** | 🔴 **`fermenting in small, French oak fermenters`（小型のフレンチオーク発酵槽）。ステンレスではない** |
| 🔴 **樽** | 🔴 **`100% new French oak`。**「**最高のフレンチオーク barrique しか使わない。stave wood は超緻密な木目のものを手で選び、樽に仕立てる前に 3 年間 air dry する。**」 |
| 🔴 **熟成期間** | 🔴 **`The Warrior` 2022 / `The Dreamer` 2022 ＝ `35 months`**<br>**`Hell's Gate`（2019）＝ `44 months`**<br>**`Voyager` シリーズ（2018、`DEEP SPACE` プログラム）＝ `48 months`** |
| 🔴 **熟成場所** | 🔴 **`The RING`（Glass Mountain 内部、地下 385 フィート）。**「**樽は Hundred Acre の樽と並んで、地中の The Ring winery で眠る**」「**そこでは時間が止まる**」 |
| **リリースの遅さ** | ✅ **「ほとんどのワイナリーはこの伝説的なヴィンテージ（2018）をすでにリリースし、売り切れている。われわれは違う。必要なだけの時間を与える。」** |

🔴 ⚠️ **これらはすべて Fortunate Son についての記述である。**
**造り手は「Hundred Acre とまったく同じ樽・同じ森・同じ樽メーカー・同じトースト、
そして同程度の期間」と書いているが、Hundred Acre 本体の数値そのものは公開されていない。** → §Staff Notes ⚠️ ④

### ✅ Summer Dreams の白 —— 数値がすべて公開されている

| | **The Sun Also Rises 2024**（Chardonnay） | **Walking On Venice Beach 2024**（Sauvignon Blanc） |
|---|---|---|
| **表示産地** | ✅🏛 **Sonoma Coast** | ✅🏛 **Sonoma Coast** |
| 🔴 **セパージュ** | ✅ **100% Chardonnay** | 🔴 ✅ **58% Sauvignon Blanc, 42% Musqué**<br>⚠️ **`fortunatesonwines.com` の `The Blade`（別ブランドの SB）は `88% Sauvignon Blanc 12% Sauvignon Musqué`。混同しないこと** |
| 🔴 **発酵** | 🔴 **樽発酵。フレンチオークの各種サイズ —— `puncheons (500L)`、`barrels (228L)` と `(265L)`** | ⚠️ **tech sheet に発酵欄なし** |
| 🔴 **樽** | 🔴 **`16 months in French Oak (64% new) puncheons`。11 か月時点で全樽をテイスティングし、選抜した分をステンレスドラムに移して残りの élevage を行う** | 🔴 **`French Oak Puncheons` と `Cigar shaped barrels`、および `Acacia Puncheons` の組み合わせ（新樽 21%、うち半分がアカシア、半分がフレンチオーク）。残りは古樽、一部はステンレス** |
| **清澄・濾過** | 🔴 **`Crossflow filtered`（クロスフロー濾過）** | 🔴 **`Polished, minimal filtering`** |
| 🔴 **アルコール（ラベル実測）** | 🏛 **`14.5% ALC. BY VOL.`**（🏛 COLA `25022001000716` の 2023 年ラベル画像）<br>⚠️ **2024 年ヴィンテージのラベルは未確認** | ⚠️ **未確認** |
| 🔴 **蔵出し価格** | ✅ 🔴 **`$110`／本（6 本パック単位）** | ✅ 🔴 **`$85`／本（6 本パック単位）** |

🔴 ⚠️ **Fortunate Son と Hundred Acre の蔵出し価格は公式サイトに一切出ていない**（allocation のため）。

---

## Style

### 🔴 ✅ OBP 掲載 4 本には、造り手自身のテイスティングノートが存在する

| OBP # | ワイン | 造り手の公式ノート（抜粋・訳） |
|---|---|---|
| **1** | 🔴 **The Sun Also Rises 2024** | 「**メイヤーレモンのオイル、海辺のタイム、フレッシュジンジャー、イランイランが香りを先導する。
味わいはシトラス・コンフィ、ゴールデンアップル、キャラメリゼしたパイナップルを重ね、
ターメリックと核果の気配がミネラルの芯を包む。溌溂とした酸が豊かな口当たりを駆動し、
明るく、焦点が定まり、興味をそそる複雑さで終わる。**」 |
| **2** | 🔴 **Walking On Venice Beach 2024** | 「**明るく持ち上がった香り。白グレープフルーツ、マンダリンのオイル、ライムの花、
パッションフルーツ・クリーム、柚子、こぶみかん。味わいは結晶のように精緻で、
濡れた川石のミネラルがジャスミンと柑橘の花と層をなし、ごく軽いハーブの縁取りが枠を与える。
レモンシャーベット、チャービル、タラゴン、胡瓜の皮の気配が、遊び心と落ち着きを併せ持つ余韻へ運ばれる。**」 |
| **3** | 🔴 **Fortunate Son The Dreamer 2022** | 「**2022 年の Dreamer は、トーストしたアーモンド、プラム、熟したイチジクという幽玄な香りで開き、
砕いた花崗岩のミネラルの筋がすべてを貫く。ダークチョコレートの伏流が香りに豊かさと妖しさを加え、
乾いたハーブと革の気配がサヴォリーな次元を与える。味わいでは、豊満で細かく織られたタンニンが
熟した赤系果実の芯を包み、明るく爽やかな酸がその柔らかな縁をすべて研ぎ澄ます。
余韻は夜更けまで続き、それは結論というより、自らの夢景色の奥へさらに分け入れという誘いである。**」<br>🔴 **造り手のノート：「このワインは暗く、思い詰めていて、優雅さと精緻で構造的なタンニンを持つ。
嵐の夜のワーグナーが、思いがけず莫大な金を稼いだような、そういうワインだ。**」 |
| **4** | 🔴 **Fortunate Son The Warrior 2022** | 「**2022 年の Warrior は大胆で揺るぎない。白胡椒、ラズベリー・ジャム、乾燥した苺の層が
複雑な香りを構成し、土くれた粘土壺とタバコの葉の気配が均衡を与える。
アプリコット、熟成した甘いオーク、そして石灰岩の洞窟を思わせる冷たいミネラルの繊細な差し色が
深みと陰影をもたらす。味わいでは、生き生きとした酸が果実を際立たせ、
細かい粒子のタンニンが質感を豊かにする。中盤にはみごとに繊細な引っかかりがあり、
それが均衡のとれた、持続する筋肉質の余韻へつながる。**」<br>🔴 **造り手のノート：「純粋で総体的な力と暗さ。気に入りすぎて、
本当に思っていることを人に言いたくなる気分になるかもしれないから注意すること。
これはまたしても、気の弱い者のためのワインではない。鋼の意志と、それに見合う決意を持つ者のためのものだ。**」 |

### 🔴 ⚠️ OBP 5 行目 `'Ark'` 2022 —— **造り手のノートは存在しない**

🔴 **`hundredacre.com` にはワインのページが無く、`Ark` についての記述はどこにも公開されていない。**
🏛 **取得できたのは COLA 上の事実だけである** ——
**brand `HUNDRED ACRE` / fanciful name `ARK VINEYARD`（2018）→ `ARK`（2021）／
grape varietal `Cabernet Sauvignon` / 表示産地 `NAPA VALLEY` / `ALCOHOL 15.5% BY VOL` / `750ML` /
`ESTATE BOTTLED BY HUNDRED ACRE, ST. HELENA, CA`。**
🏛 **ラベル表面の一文：「`This wine is made exclusively from one hundred percent Cabernet Sauvignon
grown on our estate vineyard in Napa Valley.`」**
（**このワインは、われわれが Napa Valley に持つ estate vineyard で育った 100% カベルネ・ソーヴィニヨンのみから造られている**）
🏛 **裏ラベルは Odyssey 冒頭の英訳を薄い文字で全面に敷き、その下に大きくヴィンテージを置く意匠である。**

⚠️ 🔴 **したがって $2,400 のこの 1 本について、造り手の言葉で味わいを語ることはできない。** → §Staff Notes ⚠️ ①

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本。すべて `unresolved`**）

| # | source_row_id 🔍 | OBP 印字 | VT | 価格 | ✅🏛 **確認結果** |
|---|---|---|---|---|---|
| 1 | `obp-beverage-2026-08:277c364639` | **'Summer Dreams, The Sun Also Rises,'** Sonoma Coast Chardonnay | 2024 | **$325** | 🔴 **造り手は `Summer Dreams`。Hundred Acre ではない。**<br>✅🏛 **正式形は brand `summer dreams` ＋ 銘 `The Sun Also Rises`。カンマは無い**<br>✅ **100% Chardonnay / Heintz Vineyard ＋ Summer Dreams Estate Vineyard / 樽発酵 / 16 か月・新樽 64%**<br>🔴 **蔵出し $110。OBP は約 3.0 倍**<br>🔴 ⚠️ **セクションは `WHITE > NAPA` だが、🏛 の表示産地は `SONOMA COAST`。Sonoma Coast は Napa Valley の中に無い＝ `section_region_conflict` は妥当** |
| 2 | `obp-beverage-2026-08:baf656491f` | **'Summer Dreams, Walking on Venice Beach,'** Sonoma Coast Sauvignon Blanc | 2024 | **$260** | 🔴 **造り手は `Summer Dreams`。**<br>✅ **公式表記は `Walking On Venice Beach`（`On` が大文字）**<br>✅ **58% Sauvignon Blanc / 42% Musqué。1980 年植樹の古樹畑**<br>🔴 **蔵出し $85。OBP は約 3.1 倍**<br>✅ **セクション `WHITE > SONOMA` は正しい** |
| 3 | `obp-beverage-2026-08:8d7acfc7a0` | **'Fortunate Son, The Dreamer,'** Napa Valley Cabernet Sauvignon | 2022 | **$520** | 🔴 **造り手は `Fortunate Son`。Hundred Acre ではない**（造り手自身が明言）<br>✅🏛 **正式形は brand `FORTUNATE SON` ＋ 銘 `THE DREAMER`。カンマは無い**<br>✅ **100% Cabernet Sauvignon / 35 か月 100% 新フレンチオーク / 表示産地 `Napa Valley` ✅🏛 一致**<br>✅ **公式テイスティングノート実在** |
| 4 | `obp-beverage-2026-08:e4e295786c` | **'Fortunate Son, The Warrior,'** Napa Valley Cabernet Sauvignon | 2022 | **$1,200** | 🔴 **造り手は `Fortunate Son`**<br>✅ **100% Cabernet Sauvignon / 35 か月 100% 新フレンチオーク / 表示産地 `Napa Valley` ✅🏛 一致**<br>🔴 **`Warrior` は単一畑。**「**`Sourced from a single, small, family-owned vineyard`**」（Dreamer は複数畑）<br>✅ **公式テイスティングノート実在** |
| 5 | `obp-beverage-2026-08:530025170e` | **'Ark,'** Howell Mountain Cabernet Sauvignon | 2022 | **$2,400** | 🔴 **これだけが本物の Hundred Acre**<br>🔴 🏛 **`Ark` ＝ `Ark Vineyard`。同一ブランド・同一品種で、2018 年承認が `ARK VINEYARD`、2021 年承認が `ARK`。→ canonical `Ark Vineyard Cabernet Sauvignon` と同一ワイン。alias マッチは妥当**<br>🔴 ⚠️ **ただし 🏛 の表示産地は 2 件とも `NAPA VALLEY`。`Howell Mountain` の裏づけは一次資料に無い**<br>⚠️ **2022 年ヴィンテージに対応する COLA は本調査では未取得** |

🔴 **5 本のうち 4 本（1・2・3・4）は、canonical/intake が `producer:hundred-acre` に結びつけているが、
生産者自身は別ブランドとして提示し、🏛 も別 brand name で登録している。** → §Canonical Conflict ①

### ✅🏛 各ブランドの公式ラインナップ（**現時点で確認できる全数**）

| ブランド | ワイン | 出典 |
|---|---|---|
| 🔴 **Hundred Acre** | ⚠️ **公式サイトに一覧が無い。**🏛 TTB の fanciful name から確認できるのは<br>**`Ark Vineyard`／`Ark`・`Kayli Morgan Vineyard`／`Kayli Morgan`・`Few and Far Between Vineyard`／`Few & Far Between`・`Ancient Way (Vineyard)`（豪州）・`Wraith`・`Wraith Crypt`・`Morgan's Way`・`Holy Quest`（ラベルは `WRAITH / HOLY QUEST` の 2 段）・`Dark Ark`・`Ark Deep Time`／`Kayli Morgan Deep Time`／`Few and Far Between Deep Time`／`Ancient Way Deep Time`**<br>✅ **さらに `Hundred Acre Precious Cabernet Sauvignon` が Fortunate Son のサイト本文で名指しされている** | 🏛✅ |
| **Fortunate Son** | ✅ **`The Warrior`・`The Diplomat`・`The Dreamer`・`The Visionary`・`Hell's Gate`・`Voyager`（II / III / V / VII）・`Lost Souls`（`Ghost Vines of 1963`／`Power and Darkness`／`Pleasure and Light`）・`The Reader`・`The Blade`（SB）・`Chronos Complications`・`Precious`**（公式 sitemap の 11 URL＋本文） | ✅🏛 |
| **Summer Dreams** | ✅ **Pinot Noir: `Golden Hour`・`Halley's Comet`・`Stargazing`・`Super Chill`・`The Flash`・`The Wedge`・`Twilight` ／ Chardonnay: `Afterglow`・`The Sun Also Rises` ／ Sauvignon Blanc: `Walking On Venice Beach` ／ Rosé: `Martian Pink` ／ Blanc de Pinot Noir: `Picnic Anyone?`**（公式 sitemap の 12 URL） | ✅🏛 |

🔴 **canonical にある `Kayli Morgan Vineyard Cabernet Sauvignon` は OBP に無い。**
🏛 **ラベル実測は `HUNDRED ACRE / Kayli Morgan Vineyard / NAPA VALLEY / CABERNET SAUVIGNON /
ALCOHOL 15.5% BY VOL / ESTATE BOTTLED BY HUNDRED ACRE, ST. HELENA, CA` で、Ark と同一書式である。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① リストの 5 本のうち、Hundred Acre のワインは `'Ark'` 1 本だけです。残り 4 本は姉妹ブランドです。**
「**同じ会社（One True Vine, LLC）、同じ造り手（Jayson Woodbridge）、同じ電話番号ですが、ラベル上のブランドは 3 つに分かれています。**
**`Fortunate Son` は Hundred Acre とは別のワインです —— 造り手自身がブログで
『誤解のないように、このワインは Hundred Acre ではない』と書いています。**
**Hundred Acre は全量が自社の単一畑（`ALL SINGLE VINEYARD`）。それに対して Fortunate Son は、
何世代も家族が守ってきた小さな契約畑 —— 樹齢 80 年を超えるものもあります —— を織り合わせて造ります。**
**`Summer Dreams` はさらに別で、Sonoma Coast の冷涼な丘陵から白とピノ・ノワールを造る、白専門の醸造家
Ashley Holland との共同プロジェクトです。**」

**② `'Ark'` は Hundred Acre の自社畑名です。ラベルの表示産地は Napa Valley です。**
「**`Ark` は畑の名前で、正式には `Ark Vineyard` とも書かれます —— 造り手はラベルの銘を年代によって
`Ark Vineyard` から `Ark` へ短くしてきました。同じワインです。**
**ラベルには『このワインは、われわれが Napa Valley に持つ自社畑で育った 100% カベルネ・ソーヴィニヨンのみから造られている』
と書かれ、表示産地は `NAPA VALLEY`、`ESTATE BOTTLED`、アルコール 15.5% です。**
**裏ラベルは『オデュッセイア』の冒頭が薄い文字で全面に敷かれた意匠になっています。**
**Hundred Acre には畑が 3 つあり、そのすべてが単一畑としてボトリングされます。**」
🔴 **（`Howell Mountain` はメニューの印字です。造り手のラベルにはその語がありません。下記 ⚠️ ② を必ず読むこと。）**

**③ 造り手の設計思想は「時間」です。数字が出ているのは Fortunate Son の側です。**
「**粒ごとの選果、小さなフレンチオークの発酵槽、そして 100% 新樽のフレンチオーク barrique。
樽材は超緻密な木目のものを手で選び、樽にする前に 3 年間 air dry します。**
**2022 年の `The Warrior` と `The Dreamer` は 35 か月、`Hell's Gate` は 44 か月、
`Voyager` シリーズは『DEEP SPACE』という 48 か月のプログラムです。**
**熟成庫は Glass Mountain の内部、地下 385 フィートに掘られた `The RING` という地下ワイナリー。
造り手は『そこでは時間が止まる』と書いています。**
**リリースも遅い。『ほとんどのワイナリーは 2018 年をとうに売り切ったが、われわれは必要なだけの時間を与える』。**」

### 追加で使える一手

- 🔴 **`The Warrior` と `The Dreamer` の違い（造り手の記述で唯一はっきり分かれる点）**：
  「**`The Warrior` は単一の小さな家族経営の畑から。`The Dreamer` は複数の小さな家族畑から。
  セパージュはどちらも 100% カベルネ・ソーヴィニヨンで、樽も 35 か月 100% 新樽と同じです。
  違いは畑の数です。**」
- **`Fortunate Son` の拠点**：「**1860 年に建てられた `David Fulton` のワイナリー —— St. Helena の
  Fulton Lane にある、この街で最初期の家の一つです。2023 年まで 160 年以上同じ一家が持っていた土地を
  Woodbridge 一家が買い取り、修復しました。ラベルの紋章に `18 60` と入っているのはそのためです。**」
- **`Summer Dreams` の名前の由来（造り手の言葉）**：「**`Walking On Venice Beach` は、
  『わたしがカリフォルニアで最初に歩いたビーチ、Venice Beach にちなんだ。冷たくて、同時に野性的だった』。
  ソーヴィニヨン・ブランの畑は 1980 年植樹で、カリフォルニアで最も古い SB の畑の一つと言われています。**」
- **買い方**：「**Hundred Acre は順番待ちリスト（`Waiting List`）制です。会員募集ですらなく、
  順番を待つところから始まります。造り手は認定ディストリビューター以外からの購入を強く避けるよう
  公式に呼びかけています —— provenance を保証できないからです。日本の正規輸入元は `Wine to Style` です。**」
- 🔴 **Jayson Woodbridge の人物像（造り手側サイトの記述）**：「**カナダ出身。正規の醸造教育も経験も無いまま
  2000 年ごろに『世界が見たこともないほど妥協のないカベルネを造る』と宣言した人物です。
  ブログの文体は極端に率直で、罵り言葉も伏せずに載せています。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している**）

1. 🔴 ⚠️ **`'Ark'` 2022 の味わいを、造り手の言葉として語らない。**
   **`hundredacre.com` は現在「準備中」で、ワインのページが一枚も存在しない。**
   **`Ark` についての造り手のテイスティングノート・畑の記述・生育期の記述は、本調査で一件も見つからなかった。**
   **他のヴィンテージや他のワインのノートを流用しないこと。**
2. 🔴 ⚠️ **`Ark` を「Howell Mountain のワインです」と断定しない。**
   🏛 **TTB COLA 2 件（2018 年 `ARK VINEYARD` / 2021 年 `ARK`）はどちらも表示産地を `NAPA VALLEY` と記載し、
   承認ラベル画像にも `NAPA VALLEY` と印字されている。**
   **取得した生産者資料・TTB 記録のどこにも `Howell` の語が無い。**
   🔴 **ただし「Howell Mountain は Napa じゃない」も誤り。**
   🏛 **27 CFR §9.94 は逐語で「Howell Mountain 栽培地域は Napa 郡に位置し、Napa Valley 栽培地域の一部である」と定めている。**
   **言うなら「Napa Valley の、St. Helena に拠点を置く造り手の自社畑」まで。**
3. 🔴 ⚠️ **`Summer Dreams` と `Fortunate Son` を「Hundred Acre のセカンドラベル」と言わない。**
   **造り手は「このワインは Hundred Acre ではない」と明言している。**
   **`Summer Dreams` は Sonoma Coast、`Fortunate Son` は Napa Valley の契約畑で、産地も畑も別である。**
   **さらに `Summer Dreams` は 2025 年以降、🏛 TTB 上は `Summer Dreams Wines LLC` という別法人名義になっている。**
4. 🔴 ⚠️ **Fortunate Son の醸造数値（35 か月・100% 新樽など）を Hundred Acre の数値として語らない。**
   **これらはすべて Fortunate Son の tech sheet の記載である。**
   **造り手は「Hundred Acre と同じ樽・同じ森・同程度の期間」と書いているが、
   Hundred Acre 本体の月数・新樽比率は一切公開されていない。**
5. 🔴 ⚠️ **「有機栽培」「ビオディナミ」「サステナブル認証」と言わない。**
   **取得した全資料（3 サイト・tech sheet 4 点・TTB 40 件超）に認証語が一件も無い。**
   **同時に「認証を拒否している造り手です」とも言わない。造り手は認証について何も述べていない。**
   **言えるのは「契約農家が『夢の基準』で農を営めるよう造り手が費用を負担している」「天候やタンク容量に
   収穫を強いられない」「大半の造り手より長く果実を吊るす」まで。**
6. 🔴 ⚠️ **Hundred Acre の畑の面積・植栽密度・収量・樹齢・生産本数を言わない。**
   **一つも公開されていない。**「畑は 3 つ」だけが二重に裏づけられた数字である。
   **`Kayli Morgan` と `Ark` の所在地（何山・何 AVA か）も、造り手資料には一切書かれていない。**
7. ⚠️ **🏛 TTB の `CLASS/TYPE DESCRIPTION` を「デザートワイン」と読み替えない。**
   **Hundred Acre と Fortunate Son のほぼ全件が `DESSERT /PORT/SHERRY/(COOKING) WINE` と表示されるが、
   ラベル実測は `ALCOHOL 15.5% BY VOL` の辛口赤である。**
   **同じ Fortunate Son でも `The Diplomat` だけは `TABLE RED WINE` に分類されている。**
   ⚠️ **これはアルコール度数による米国の法定クラス区分と考えられるが、
   本調査では 27 CFR Part 4 の該当条文を取得していない。断定はしないこと。**
8. ⚠️ **点数を事実として語らない。**
   **`98 points` `99 points` `97+ points` `95pts` `97 POINTS` などは、いずれも生産者サイトに掲出された
   第三者評価の引用である。本ドシエはこれを事実の典拠として用いない。**
   **「100 点の数」も生産者サイト内で `more than forty`（2023 年）と `more than 61`（現行）で食い違う。**
9. ⚠️ **`Heintz Vineyard` を `Charles Heintz Vineyard` と言い換えない。**
   🔍 **OBP の line 1184 に `DuMol 'Isobel, Charles Heintz Vineyard'` があり同一畑の可能性が高いが、
   Summer Dreams 側は `Heintz Vineyard` としか書いていない。**
10. ⚠️ **`Precious` を 1 つのワインとして語らない。**
    ✅ **`Fortunate Son Precious`（2022、Napa Valley Cabernet）と `Hundred Acre Precious Cabernet Sauvignon` は
    別のワインである。造り手自身が「これは Hundred Acre Precious の輝かしい兄弟である」と書いて区別している。**
11. ⚠️ **`Summer Dreams` という名の他社ワインと混同しない。**
    🏛 **TTB には `SUMMER DREAMS` ブランドで、フランス産ロゼ（NY の輸入業者、2018・2019 年）と
    New Hampshire のフレーバー麦芽飲料の登録も存在する。これらは本生産者と無関係である。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **新規の登録は行っていない。以下は escalation であり、実行していない。**

### ① 🔴 OBP 5 行のうち 4 行が別ブランドのワイン —— **既存クラス `CAT-3 brand_axis` に該当**

1. **ID**
   - canonical 生産者: `producer:hundred-acre`（canonical キュヴェは `hundred-acre-kayli-morgan` / `hundred-acre-ark` の 2 件）
   - 🔍 **research shell（`research/store/t-01/shells.json`、2026-07-29 スナップショット）**
     - `rs:pro:00d8d28fbafaf9df`（line 1271 = Fortunate Son, The Dreamer）／`rs:rel:11e0d5e8182561d7`
     - `rs:pro:9e44159419126c5a`（line 1272 = Fortunate Son, The Warrior）／`rs:rel:255350600540eef3`
     - `rs:pro:a4dbf1e5e6190afe`（line 1273 = Ark）／`rs:rel:2336197f54536949`
     - **上記 3 件はすべて `canonical.producer_id = "producer:hundred-acre"` を保持**
   - 🔍 **白 2 行**: `rs:pro:cf8ae75795870905` / `rs:pro:e89b472b1464354f`（line 1165）、
     `rs:pro:ff227e82730ab00a` / `rs:pro:4f7b283083696177`（line 1189）
   - 🔍 **OBP 2026-08 intake（本 repo に未同梱）**: `obp-beverage-2026-08:277c364639` ほか 4 件、
     いずれも `producer_heading = "Hundred Acre"` / `producer_state = exact` / `match_state = unresolved`
2. **なぜ誤って見えるか**
   🔴 **`Fortunate Son` と `Summer Dreams` は Hundred Acre の別名でもセカンドラベルでもない。**
   **🏛 TTB では別々の brand name（`FORTUNATE SON` / `SUMMER DREAMS`）として登録され、
   `Summer Dreams` は 2025 年以降 `Summer Dreams Wines LLC` という別法人名義に移っている。**
   **産地も異なる（Fortunate Son ＝ Napa Valley の契約畑、Summer Dreams ＝ Sonoma Coast）。**
   **canonical の 2 キュヴェは `subregion` に `Napa Valley — St. Helena` / `Napa Valley — Howell Mountain` を持つため、
   このまま 4 行を同じ生産者に紐づけると、Sonoma Coast のシャルドネに Napa の産地情報が付く。**
3. **証拠**
   - ✅ **`fortunatesonwines.com/blog/…chapter-one`（Jayson Woodbridge 署名）：
     「`Make no mistake this wine is NOT Hundred Acre`」**
   - ✅ **同：「`I do want to be clear on one thing: Hundred Acre is ALL SINGLE VINEYARD.`」
     （Fortunate Son は契約畑のブレンド）**
   - 🏛 **COLA `22307001000816`：brand `FORTUNATE SON` / fanciful `THE WARRIOR` / 申請者 `One True Vine, LLC` /
     DBA `FORTUNATE SON WINES (Used on label)`**
   - 🏛 **COLA `25022001000716` / `25028001000996`：brand `SUMMER DREAMS` / 申請者
     `summer dreams wines, Summer Dreams Wines LLC`（`1434 Grove St, Healdsburg, CA 95448`）/
     表示産地 `SONOMA COAST`**
   - 🏛 **ラベル画像：`PRODUCED AND BOTTLED BY SUMMER DREAMS WINES, HEALDSBURG, CA`**
   - ✅ **`hundredacre.com` フッター：「Visit our **other wineries**: Fortunate Son Winery / Summer Dreams Wines」**
   - ⚠️ **逆方向の証拠：`summerdreamswines.com/trade` の営業チームのメールが全員 `@hundredacre.com`。
     電話番号も 3 ブランド共通。＝ 商業運営は一体である**
4. **OBP への影響**
   🔴 **5 行中 4 行（$325 / $260 / $520 / $1,200 ＝ 合計 $2,305）が誤った生産者に帰属している。**
   **この状態でソムリエ画面に Hundred Acre の産地情報を出すと、Sonoma Coast のワインに Napa の記述が付く。**
   **逆に正しいブランドへ紐づければ、4 行すべてに造り手自身の tech sheet とテイスティングノートが即座に付く。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - **`producer:fortunate-son`（`producer='Fortunate Son'`）と `producer:summer-dreams`（`producer='Summer Dreams'`）を
     新設し、4 行をそこへ移す。**
   - 🔴 **統合はしない。**`REGISTER.md` の **`P-7 Chave / Chave Sélections —— 統合禁止`** と同じ扱いが妥当。
   - **上位に `One True Vine, LLC` を group / parent として持てるかは canonical のスキーマ次第。
     持てないなら 3 ブランドを並列の生産者として登録し、注記で関係を残す。**
   - 🔴 **`Summer Dreams` の `region` に `Napa Valley` を入れない。`California — Sonoma Coast` が正しい。**
   - 🔴 **`producer_heading = "Hundred Acre"` は menu-printed alias として保持する（メニューの実際の印字だから）。**
6. **既存 ID との対応**: 🔴 **新番号を開かない。`REGISTER.md §D CAT-3 `brand_axis`（同一家族の複数ブランドをどう持つか）
   にそのまま該当する。**`P-6` `P-7` と同型であり、**Harlan Estate ドシエの `The Mascot` 帰属問題とも同型。**
7. **Confidence**: 🔴 **High**（ブランド名・法人名・表示産地・造り手自身の明言がすべて一次／規制資料で揃っている）

### ② 🔴 `hundred-acre-ark` の `subregion = "Napa Valley — Howell Mountain"` に一次資料の裏づけが無い —— **新規の形（proposed, unnumbered）**

1. **ID**
   - canonical: 🔍 **`hundred-acre-ark`**
     （`name='Ark Vineyard Cabernet Sauvignon'` / `subregion='Napa Valley — Howell Mountain'` /
     `classification='Howell Mountain Single Vineyard Cabernet Sauvignon'` /
     `tags` に `Howell Mountain` / `description` に「**Howell Mountain の山岳単一畑。火山性土壌・標高約 500m**」）
   - OBP: 🔍 `rs:pro:a4dbf1e5e6190afe`（line 1273、印字 `'Ark,' Howell Mountain Cabernet Sauvignon`、$2,400）
2. **なぜ問題に見えるか**
   🔴 **canonical は Ark を Howell Mountain の山岳畑と断定し、標高・土壌・スタイルまで記述しているが、
   本調査で取得した一次資料・規制資料のどこにも `Howell` の語が現れない。**
   🏛 **TTB COLA 2 件（`18325001000474` = `ARK VINEYARD`、`21207001000014` = `ARK`）は
   どちらも `11. WINE APPELLATION (If on label)` を `NAPA VALLEY` と記載している。**
   🏛 **承認ラベル画像にも `NAPA VALLEY` としか印字されていない。**
   🔴 **さらに canonical の「標高約 500m」（≒1,640 ft）という数値は、🏛 27 CFR §9.94(c)(1) が定める
   Howell Mountain AVA の下限 1,400 フィート等高線と整合はするが、出典が不明である。**
3. **証拠**
   - 🏛 **COLA `18325001000474`（2018-11-23 承認、申請者 `ADVENTURES IN WINE, BARSAC, INC.`、
     permit `CA-I-3223`）：brand `HUNDRED ACRE` / fanciful `ARK VINEYARD` /
     grape varietal `Cabernet Sauvignon` / wine appellation `NAPA VALLEY`**
   - 🏛 **COLA `21207001000014`（2021-07-27 承認、申請者 `The Finer Things Company`）：
     brand `HUNDRED ACRE` / fanciful `ARK` / wine appellation `NAPA VALLEY`**
   - 🏛 **承認ラベル画像（front）：`HUNDRED ACRE / Ark Vineyard /
     "This wine is made exclusively from one hundred percent Cabernet Sauvignon grown on
     our estate vineyard in Napa Valley." / NAPA VALLEY | CABERNET SAUVIGNON /
     750ML | ALCOHOL 15.5% BY VOL / ESTATE BOTTLED BY HUNDRED ACRE / ST. HELENA, CA / www.hundredacre.com`**
   - 🏛 **本調査で取得した Hundred Acre の COLA 全 41 件中、表示産地が `HOWELL MOUNTAIN` のものは 0 件。**
   - ⚠️ **`hundredacre.com` には Ark のページ自体が存在しない（`Full website is coming soon`）。**
   - 🏛 **27 CFR §9.94(c)：Howell Mountain は Napa Valley AVA の一部。**
     → **したがって「Napa Valley 表示」は「Howell Mountain 産でない」ことを意味しない。両立しうる。**
4. **OBP への影響**
   🔴 **$2,400 —— 本バッチで最も高価な 1 行。**
   **現状 canonical には `Ark Vineyard` のヴィンテージが 0 件で、`unresolved` のまま。**
   **さらにソムリエ画面に「Howell Mountain の火山性山岳畑、標高約 500m」を出すと、
   造り手のラベルにない産地をゲストに断定して伝えることになる。**
   🔴 **`Ark` ↔ `Ark Vineyard` の同一性そのものは 🏛 で確定しており、alias マッチは正しい。争点は産地だけである。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - **キュヴェ名は `Ark Vineyard Cabernet Sauvignon` のまま維持し、`Ark` を label alias として明示登録する
     （2021 年以降の🏛 承認ラベルの銘）。**
   - 🔴 **`subregion` を `Napa Valley` に後退させ、`Howell Mountain` は「未検証の主張」として
     別フィールド（または注記）に降格する。**
   - 🔴 **`classification` の `Howell Mountain Single Vineyard` と、`description` / `tasting` / `tags` の
     Howell Mountain 由来の記述（火山性土壌・標高約 500m・山岳のスパイス）も同時に見直す必要がある。
     これらは産地の断定に依存している。**
   - **確定には 2022 年ヴィンテージの実ボトル、または当該年の COLA が要る。** → Open Questions 1
6. **既存 ID との対応**: 🔴 **`REGISTER.md` の 20 件（`P-1`〜`P-7` / `C-1`〜`C-5` / `V-1`〜`V-4` / `S-1`〜`S-4`）および
   `CAT-1`〜`CAT-9` のいずれにも該当しない。**
   **既存分類はすべて「命名規約」「層の境界」「キー設計」「entity 境界」の問題であり、
   本件は「canonical の属性が一次資料と食い違う」＝ 事実の出所（provenance）の問題である。**
   🔴 **新しい形として提案する（`proposed, unnumbered`）。番号付与は Akio / CTO の判断。**
   **候補名: `unsourced_attribute` —— canonical の記述的属性が、規制／一次資料と照合できない。**
   ⚠️ **同型が他生産者にもあるかは、本ドシエでは走査していない（repo 全体の掃引は行わない方針のため）。**
7. **Confidence**: 🔴 **High（ラベル表示産地が `NAPA VALLEY` であること）／ Medium（Ark 畑の実際の所在）。**
   **「ラベルに Howell Mountain と書かれていない」は確定。「Ark 畑が Howell Mountain に無い」とは言っていない。**

### ③ 既存の系に属するもの —— **新しい番号を開かない**

| 事象 | 扱い |
|---|---|
| 🔴 **`vintage='—'`（em-dash sentinel）** | 🔍 **`hundred-acre-kayli-morgan` / `hundred-acre-ark` の 2 件とも該当。**<br>**DB 全体で 328 レコードに及ぶ既知の systemic な形であり、本生産者固有の欠陥ではない。既存の掃引結果を参照するにとどめる。** |
| 🔍 **line 1165 / 1189 に `level='producer'` と `level='product'` の shell が二重に立っている** | 🔍 **同一 `source_line_no` に 2 つの `rs:pro:*` が存在する（`cf8ae75795870905`＋`e89b472b1464354f`、`ff227e82730ab00a`＋`4f7b283083696177`）。**<br>⚠️ **同型は Grgich Hills・Hudson・Kazumi・Odette・Antica Terra・Composition でも観察でき、Hundred Acre 固有ではない。intake の生成規則の問題。新番号を開かない。** |
| 🔴 🔍 **line 1165 / 1189 の parse 破損** | 🔴 🔍 **`producer_or_brand` に `"2024\t\t'Summer Dreams, The Sun Also Rises,'"` という行全体が入り、`original_raw_line` は `"Sonoma Coast Chardonnay\t\t\t\t\t325"` だけになっている。`canonical` は空 `{}`。**<br>**＝ 2026-07-29 スナップショットでは、この 2 行に生産者が付いていない。**<br>⚠️ **2026-08 intake では `producer_heading = "Hundred Acre"` / `producer_state = exact` になっているとのことだが、その intake は本 repo に無く、本ドシエでは検証できていない。** → Open Questions 6 |
| 🔍 **`color='Rouge'`（仏語の色名が米国産赤に付く）** | 🔍 **Harlan Estate ドシエと同一の観察。語彙統一の問題であり matcher の誤割当ではない。観察の記録にとどめる。** |
| 🔍 **`grapes=None`** | 🏛 **ラベルは `Ark` / `Kayli Morgan` とも `100% Cabernet Sauvignon` と明記している。**<br>**＝ 本件については `grapes` を埋められる。ただし埋めるのは canonical 側の作業であり、本ドシエは実行しない。** |
| 🔍 **`section_region_conflict`（line 1165）** | 🔍 🔴 **実在の不整合。**🏛 **`SUMMER DREAMS / THE SUN ALSO RISES` の表示産地は `SONOMA COAST` で、`SONOMA COUNTY` にある。`NAPA` セクションは誤り。**<br>**同じブランド・同じ表示産地の line 1189 は `SONOMA` セクションにある＝ OBP 側の内部不整合。**<br>**これはメニュー原本の組版の問題であり、canonical の問題ではない。** |

---

## Sources

**一次資料は生産者自身の 3 サイトと、そこが配信する tech sheet PDF のみ。
規制資料は TTB COLA と eCFR。retailer / auction / critic aggregator / Wikipedia は
事実の典拠として一切使用していない。**

### 🔴 サイト真正性の事前確認（**どうやって確かめたか**）

| 判定 | サイト | 確認方法 |
|---|---|---|
| ✅ **真正** | 🔴 **`https://hundredacre.com/`** | 🔴 **(a) 規制一次資料との一致** —— 🏛 **TTB 承認ラベル画像に `www.hundredacre.com` が印字されている**（COLA `18325001000474` ほか）。**これが最強の裏づけ。**<br>**(b) 法人名の一致** —— サイトの `legal_entity` 設定値 `One True Vine, LLC` と、🏛 TTB 申請者名 `ONE TRUE VINE, LLC`（`565 Crystal Springs Rd, Saint Helena, CA`、DBA `HUNDRED ACRE (Used on label)`）が一致。<br>**(c) 一貫した法的フッター** —— 全ページに `1345 Railroad Ave, Suite 2A, St. Helena, CA 94574` / `707-967-9398` / `info@hundredacre.com` / `© 2026 One True Vine, LLC`。<br>**(d) 実運用の痕跡** —— live の Stripe 公開鍵、州別 shipping compliance 設定、実在のディストリビューター 50 州分＋インポーター 17 か国分。 |
| ✅ **真正** | **`https://fortunatesonwines.com/`** | 🏛 **COLA `22307001000816` の申請者 `One True Vine, LLC` に DBA `FORTUNATE SON WINES (Used on label)` が付き、電話 `(707) 967-9398` が一致。**<br>✅ **`hundredacre.com` フッターからの相互リンク。**`robots.txt` が `Host: https://fortunatesonwines.com/` を宣言。 |
| ✅ **真正** | **`https://summerdreamswines.com/`** | 🏛 **COLA `21232001000314` の申請者は `One True Vine, LLC`、`25022001000716` は `Summer Dreams Wines LLC`、いずれも DBA/brand が `SUMMER DREAMS`。**<br>✅ **`hundredacre.com` フッターからの相互リンク。営業チームのメールが `@hundredacre.com`。**`robots.txt` が `Host: https://summerdreamswines.com/` を宣言。 |
| 🔴 ❌ **却下** | 🔴 **`hundredacrewine.com`**（単数形） | 🔴 **ドメイン・パーキング。実体は 159 バイトの `<FRAMESET>` で、`http://www.searchvity.com/?dn=hundredacrewine.com&pid=9PO1MNIJ3` を読み込むだけ。ワインの内容は皆無。**<br>→ `_sources/hundred-acre/NOT_THE_PRODUCER_hundredacrewine_com_parking.html` にキャッシュ済み。 |
| 🔴 ❌ **却下** | 🔴 **`hundredacrewines.com`**（複数形） | 🔴 **同じくパーキング（160 バイト、`dn=hundredacrewines.com`、同一 `pid`）。**<br>→ `NOT_THE_PRODUCER_hundredacrewines_com_parking.html` にキャッシュ済み。 |
| 🔴 **取り違え注意** | —— | 🔴 **公式は `hundredacre.com`（`wine` も `wines` も付かない）。**<br>**`hundredacrewine.com` と `hundredacrewines.com` は同一のパーキング業者が押さえている。**<br>**なお公式サイトの `<title>` は `Hundred Acre Wines- Homepage` と `Wines` 付きで書かれており、ここでも取り違えやすい。** |

### ✅ 取得した公式資料

| 資料 | 取得した情報 |
|---|---|
| ✅ **`hundredacre.com/robots.txt` → `/sitemap.xml` 系** | ⚠️ **`sitemap.xml` は 0 バイト、`sitemap-0.xml` / `sitemap_index.xml` / `wp-sitemap.xml` はいずれも HTML の 404 ページを返す。**→ **走査の起点として使えなかったため、URL を推測で叩く方式（probe）に切り替えている。** |
| 🔴 **`hundredacre.com/`（home）** | 🔴 **`Full website is coming soon`。本文はヒーロー画像 1 枚のみ（alt: `A 3-pack of Hundred Acre Wraith Cabernet Sauvignon`）。**フッターに社名・住所・電話・メール・姉妹ブランド 2 件・`© 2026 One True Vine, LLC`。<br>🔴 **埋め込み設定 JSON に `legal_entity: "One True Vine, LLC"` / `company_name: "Hundred Acre"` / `company_email` / `company_phone`。** |
| 🔴 **`/locator/`（Our Distributors）** | 🔴 **provenance に関する造り手の声明（本ドシエ §Overview に全訳）。**米国 50 州＋DC のディストリビューター実名。<br>🔴 **インポーター 17 か国。`Japan` は `Wine to Style`。** |
| **`/terms/` `/privacy/` `/shipping/` `/accessibility/` `/credits/`** | **運営主体（`hundredacre.com` ＝ Hundred Acre）、準拠法（California / Napa County 裁判管轄）、出荷不可の州（UT, DE, NH, MS, ND, WV）、サイト制作 `Offset`。**<br>⚠️ **`/credits/` は `robots.txt` の Disallow 対象だが、前段の agent がキャッシュしていたためそのまま参照した。** |
| **`/signup/`（Waiting List）** | **順番待ちリスト制であることの確認。**⚠️ **honeypot ラベル `Humans need not fill out this field` を観測（指示としては扱っていない）。** |
| ⚠️ **`/about` `/our-wines` `/wines` `/story` `/vineyards` `/press` `/trade` `/winery` の probe** | 🔴 ⚠️ **`/story` と `/winery` は `Page Not Found`。他は空シェル（フッターのみ）。**<br>**`/trade` だけは `Logos / Wines / Images / Distributor List` の見出しがあるが、中身は空。**<br>→ 🔴 **「Hundred Acre 本体の情報が無い」ことの実証。** |
| 🔴 **`fortunatesonwines.com/blog/the-next-chapter`（2023-02-01）** | 🔴 **「23 年前の宣言」「40 超の 100 点」「Hundred Acre のために何千もの畑を見て 3 つを選んだ」「farming partner Jim Barbour」「Hundred Acre と同じ farming protocol」** |
| 🔴 **`/blog/…chapter-one`（Jayson Woodbridge 署名、2023-02-16）** | 🔴 **「NOT Hundred Acre」「2018 Fortunate Son は The RING で造られた」「David Fulton（1860）を Helen と Cameron と購入・修復」「契約農家に『夢の基準』の費用を払う」「樹齢 80 年超」「会員向けテイスティングルーム・ラウンジ・葉巻スペース」** |
| 🔴 **`/blog/…chapter-two`（同、2023-02-16）** | 🔴 **「`Hundred Acre is ALL SINGLE VINEYARD`」「初代 Fortunate Son を引退させていた」「20 年以上見てきた小さな畑の選抜区画」** |
| **`/blog/…chapter-three`（同、2023-03-16）** | **「Fortunate Son は最終的に 7 種になる。今は最初の 3 種」「Hundred Acre の樽と並んで The Ring の地中で熟成」「引用句は毎ヴィンテージ変わる」** |
| 🔴 **`/our-wines/warrior` `/our-wines/dreamer` ほか 11 URL（公式 sitemap 全数）** | 🔴 **全キュヴェの Vintage Notes / Vineyard Notes / Composition / Cooperage / Appellation / Tasting Notes。**35 か月・44 か月・48 か月、100% 新フレンチオーク、`The RING` 地下 385 ft。 |
| **`/contact` `/press` `/trade` `/napa-valley`** | **`825 Fulton Ln, St Helena`／公開試飲なし／press 一覧／Napa Valley の地質解説（生産者による一般解説）** |
| 🔴 **`summerdreamswines.com/about-us` `/location` `/our-wines/*`（公式 sitemap 全 12 ワイン）** | 🔴 **Jayson Woodbridge と Ashley Holland の経歴、Alexandra Becker-Black（ラベル画）、Sonoma Coast AVA の解説、区画の標高 900–1,800 ft と Goldridge 土壌、全ワインのクローンとスタイル、蔵出し価格** |
| **`/trade`** | 🔴 **National Sales Team 6 名の実名とメール（全員 `@hundredacre.com`）** |
| 🔴 **tech sheet PDF 4 点（生産者サイトが `cdn.sanity.io/files/odh0c1i6/…` から直接配信）** | 🔴 **`ts_fs_warrior_2022` / `ts_fs_dreamer_2022` / `ts_sd_sun-also-rises_2024` / `ts_sd_venice-beach_2024`。**<br>**OBP 掲載 4 本すべてに、造り手署名入りの tech sheet が存在した。**<br>⚠️ **PDF はフォントに ToUnicode を持たず、テキスト抽出では glyph ID しか出ない。ページ画像として読み取った。** |

### ［規制一次資料 🏛］

| 資料 | 取得した情報 |
|---|---|
| 🔴 🏛 **TTB COLA Public Registry（`ttbonline.gov/colasonline/`）** | 🔴 **取得に成功した。**（Harlan Estate 調査時は bot 対策に阻まれた箇所。）<br>**brand `HUNDRED ACRE` 41 件・`FORTUNATE SON` 20 件・`SUMMER DREAMS` 44 件の一覧、および detail 17 件。**<br>**取得できたフィールド: TTB ID / permit / serial / 承認日 / brand name / fanciful name / grape varietal / wine appellation / 申請者名と住所 / DBA / class-type description。**<br>🔴 **加えて承認ラベル画像 6 点（`Ark Vineyard` front・back、`Kayli Morgan Vineyard`、`Wraith / Holy Quest`、`Fortunate Son The Warrior 2019`、`summer dreams The Sun Also Rises 2023`）。** |
| 🔴 🏛 **27 CFR § 9.94 `Howell Mountain`**（eCFR 現行版 XML。**T.D. ATF-163, 48 FR 57487, 1983-12-30 / T.D. ATF-249, 52 FR 5960, 1987-02-27**） | 🔴 **(c) 逐語：「Howell Mountain 栽培地域は California 州 Napa 郡に位置し、Napa Valley 栽培地域の一部である」**<br>**(b) 承認地図：USGS 7.5 分図幅 `Detert Reservoir` / `Aetna Springs` / `Calistoga` / `St. Helena`**<br>**(c)(1)–(4) 境界は `1,400 foot contour line` から起こす** |
| ❌ 🏛 **27 CFR § 9.23 `Napa Valley`** | 🔴 **取得できなかった。**`ecfr_9.23.html` は 0 バイトである。<br>**したがって Napa Valley AVA の法定境界そのものは本ドシエでは参照していない。**<br>**Howell Mountain が Napa Valley の一部であることは §9.94(c) 側の記述で足りている。** |
| ❌ 🏛 **`Sonoma Coast` AVA の条文** | **取得していない。**Summer Dreams の Sonoma Coast 記述は生産者による解説であって規制一次資料ではない。 |
| ❌ 🏛 **27 CFR Part 4（class/type・`Estate Bottled` の定義）** | **取得していない。**<br>**そのため「class/type = DESSERT はアルコール度数による区分である」も
「`ESTATE BOTTLED` 表示が産地表示を拘束する」も、本ドシエでは断定していない。** |
| ❌ 🏛 **California Secretary of State（`One True Vine, LLC` / `Summer Dreams Wines LLC` の登記）** | **取得していない。**法人の存在は TTB 申請者名とサイト表記の一致でのみ確認している。 |

**取得できなかったもの / 存在しなかったもの**
- 🔴 **Hundred Acre のワイン一覧・畑・沿革・スタッフ・テイスティングノート** —— **公式サイトが未公開**（`Full website is coming soon`）。
- 🔴 **`Ark` / `Kayli Morgan` の所在地（AVA・標高・土壌）** —— **生産者資料に一件も無い。**
- 🔴 **`Ark` 2022 ヴィンテージの COLA** —— **取得した Hundred Acre の COLA に 2022 年物の `ARK` は無い。**
- 🔴 **Hundred Acre の樽熟月数・新樽比率・生産本数・蔵出し価格** —— 公式に一切無い。
- 🔴 **認証（有機／ビオディナミ／その他）** —— **語そのものが全資料に 0 件。**
- ⚠️ **`hundredacre.com/members`（会員ページ）と各ブランドの `Acquire` フロー** —— ログインが要る。未取得。
- ⚠️ **`fortunatesonwines.com` / `summerdreamswines.com` の価格（Fortunate Son 側）** —— 掲出されていない。
- ⚠️ **`ttb_search1.html`** —— **検索フォームのシェルのみで結果行を含まない。本ドシエでは使用していない。**
- ⚠️ **`cj*.txt`（curl の cookie jar）・`extract.py` / `flight.py` / `wd.py` / `wd2.py` / `ttbparse.py` / `__pycache__`** ——
  **前段 agent の作業補助であり、出典ではない。何を取得したかの証跡としてのみ扱った。**

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔴 **canonical キュヴェ 2 件（`hundred-acre-kayli-morgan` / `hundred-acre-ark`、`producer='Hundred Acre'`、
`vintage='—'`、`color='Rouge'`、`grapes=None`、`obp_format='By the bottle'`）／
research shell（`research/store/t-01/shells.json`、2026-07-29）は赤 3 行に
`canonical.producer_id='producer:hundred-acre'` を持ち、白 2 行は `canonical={}` かつ parse 破損／
OBP 2026-08 intake の 5 行（`producer_state=exact` / `match_state=unresolved`、うち行 5 のみ
`cuvee:hundred-acre-ark-vineyard-cabernet-sauvignon` に alias マッチ、ヴィンテージ 0 件）。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | **法人 `One True Vine, LLC` がサイト設定値と 🏛 TTB 申請者名の両方で一致。3 ブランドの分離が 🏛 の brand name と造り手自身の明言で確定。**⚠️ **CA 州の登記そのものは未確認** |
| **Overview** | **Medium** | 🔴 **Hundred Acre 側の一次情報が「provenance に関する声明」と「販売網」しか無い。**厚みは Fortunate Son / Summer Dreams 側に偏る |
| **History** | ⚠️ **Low-Medium** | **沿革ページが存在しない。**🏛 **COLA 承認日で年表の骨は作れたが、創業年は「23 年前に宣言した」からの逆算にすぎない。**⚠️ **初代 Fortunate Son の年代は完全に不明** |
| 🔴 **Location** | ⚠️ **Split** | 🔴 **Summer Dreams（Sonoma Coast）は High** —— 標高・土壌・クローン・植樹年まで公式。<br>🔴 **Hundred Acre は Low** —— **畑が 3 つであること以外、位置も面積も標高も一切不明。**<br>🏛 **Howell Mountain と Napa Valley の包含関係だけは規制一次資料で確定** |
| 🔴 **Farming** | ⚠️ **Low（ただし「認証ゼロ」の確定は High）** | 🔴 **Hundred Acre 本体の農法記述がゼロ。**`farming protocol` の存在は書かれているが中身が無い。<br>🔴 **認証語が全資料に 0 件であることは、網羅的に確認できた（＝「無い」ことは示せた）** |
| **Winemaking** | **Medium-High** | 🔴 **Fortunate Son / Summer Dreams は数値まで High**（35/44/48 か月、新樽比率、樽サイズ、濾過）。<br>⚠️ **Hundred Acre 本体の数値は皆無** |
| **Style** | ⚠️ **Split** | 🔴 **OBP 1〜4 行目は High** —— 4 本すべてに造り手の tech sheet とテイスティングノートがある。<br>🔴 **OBP 5 行目（$2,400 の `Ark`）は None** —— **造り手の記述が一行も存在しない** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **5 本すべてについて、正式なブランド名・銘・表示産地・品種を 🏛 と ✅ で確定できた。**`Ark` ↔ `Ark Vineyard` の同一性も確定 |
| **Staff Notes** | **High** | ⚠️ **11 項目。**🔴 **「Fortunate Son＝セカンド」「Ark＝Howell Mountain 断定」「Fortunate Son の樽数値＝Hundred Acre」「デザートワイン」という 4 つの誤りを塞いだ** |
| 🔴 **総合** | 🔴 **High — staff-usable（到達度およそ 78%）** | **必須 7 項目を満たす。**Identity ✅／Overview ✅／Location ✅（Hundred Acre 側の欠落を明示）／**Farming ✅（認証ゼロを実証）**／Important Cuvées（5 本すべて確定）✅／Staff Notes 芯 3 点 ✅／⚠️ Must-Not-Say 11 項目 ✅。<br>🔴 **欠けているのは Hundred Acre 本体の畑・農法・醸造数値と、`Ark` の味わい。いずれも生産者が公開していない。**<br>**公式サイトの本公開を待つか、実ボトル／2022 年 COLA を取るしかない。** |

**reached_70: YES.**（**約 78%**）

---

## Open Questions

1. 🔴 🍾 **`Ark` 2022 のラベルに何と書かれているか —— 実ボトルでしか解決できない。**
   🏛 **取得できた `ARK` の COLA は 2018 年と 2021 年の承認で、どちらも表示産地 `NAPA VALLEY`。**
   **2022 年ヴィンテージに対応する COLA は本調査で見つからなかった。**
   → 🔴 **床の作業（フロアタスク）：`'Ark'` 2022 の実ボトルを手に取り、
   ① 表示産地が `NAPA VALLEY` か `HOWELL MOUNTAIN` か
   ② 銘が `Ark` か `Ark Vineyard` か
   ③ アルコール度数
   ④ `ESTATE BOTTLED` 表記の有無
   を撮影して記録する。**
   → **これが埋まれば §Canonical Conflict ② が一発で決着する。**

2. 🔴 **`Ark` 畑と `Kayli Morgan` 畑は、どこにあるのか。**
   ❓ **生産者資料に一切の記載が無い。**
   **canonical は `Ark` を Howell Mountain、`Kayli Morgan` を St. Helena としているが、
   どちらも本調査では一次資料で確認できなかった。**
   → **`hundredacre.com` の本公開を待つか、公式のプレスキット／輸入元（`Wine to Style`）の
   テクニカルシートを取得する必要がある。**

3. 🔴 **Hundred Acre の 3 つの畑とは、どの 3 つか。**
   ✅ 「the three he finally chose」「all three Hundred Acre vineyards」で **3 つであることは二重に確定。**
   🏛 **TTB の fanciful name には `Ark` `Kayli Morgan` `Few and Far Between` `Ancient Way`（豪州）`Wraith` `Morgan's Way` `Holy Quest` が並ぶ。**
   ❓ **`Wraith` `Morgan's Way` `Holy Quest` `Dark Ark` が畑名なのかキュヴェ名なのかが判別できない。**
   （**`Holy Quest` のラベルは `WRAITH / HOLY QUEST` の 2 段で、`Wraith` の下位表記と読める。**）

4. 🔴 **Hundred Acre の `farming protocol` の中身。**
   ✅ **「Jayson と Jim Barbour は Hundred Acre で義務づけられているのとまったく同じ farming protocol を敷いた」
   とだけ書かれている。**
   ❓ **その protocol が何なのか（密植・収量・剪定・被覆作物・散布資材）は一行も書かれていない。**

5. ⚠️ **初代 `Fortunate Son` はいつ存在し、いつ引退したのか。**
   ✅ **「最初の Fortunate Son を引退させてから何年も経った」「早期引退から呼び戻した」とあるが、年代が無い。**
   🏛 **TTB の `FORTUNATE SON` 登録は 2021 年が最古で、初代の記録は見つからなかった。**

6. 🔴 🔍 **OBP intake の 2 つのスナップショットが食い違っている。**
   **本 repo の `research/store/t-01/shells.json`（2026-07-29）では、白 2 行（line 1165 / 1189）は
   `producer_or_brand` に行全体が入り込んだ parse 破損状態で、`canonical` は空である。**
   **一方 2026-08 の intake（`obp-beverage-2026-08:*`）では、同じ 2 行が
   `producer_heading = "Hundred Acre"` / `producer_state = exact` になっているとされる。**
   ❓ **どちらが現行か、そして 8 月の intake が「Hundred Acre」をどこから取ったのかが、本 repo では確認できない。**
   → **2026-08 intake のスナップショットを repo に入れるか、参照経路を明示する必要がある。**

7. ⚠️ **`Heintz Vineyard` ＝ `Charles Heintz Vineyard` か。**
   🔍 **OBP の line 1184 に `DuMol 'Isobel, Charles Heintz Vineyard' Sonoma Coast Chardonnay 2023` がある。**
   ✅ **Summer Dreams の tech sheet は `Heintz Vineyard` としか書いていない。**
   → **同一なら、同じリスト上の 2 本を畑で結べる強い接点になる。DuMol 側の資料で確認できる可能性が高い。**

8. ⚠️ **`Summer Dreams Wines LLC` と `One True Vine, LLC` の関係。**
   🏛 **2021 年の COLA は `One True Vine, LLC`、2025 年の COLA は `Summer Dreams Wines LLC`（Healdsburg）。**
   ✅ **一方でサイトの住所は St. Helena（Hundred Acre と同一）、営業チームのメールは `@hundredacre.com`。**
   ❓ **分社なのか、単に bonded winery の登録を移しただけなのかが不明。**
   → **California Secretary of State の法人検索で解決しうる。本調査では未実施。**

9. ⚠️ **`Hundred Acre Precious` の実体。**
   ✅ **Fortunate Son のサイトが「`Hundred Acre Precious Cabernet Sauvignon` はわれわれの最高のワインの一つ」と書いている。**
   🏛 **しかし TTB の `HUNDRED ACRE` 登録に `PRECIOUS` の fanciful name は見当たらない。**
   ❓ **別名で登録されているか、fanciful name 空欄の 8 件のいずれかである可能性がある。**

10. ⚠️ **🏛 の class/type `DESSERT /PORT/SHERRY/(COOKING) WINE` の正確な根拠。**
    **15.5% の辛口カベルネにこの分類が付き、`The Diplomat` だけ `TABLE RED WINE` になっている。**
    **アルコール度数による法定区分と考えるのが自然だが、27 CFR Part 4 の条文を本調査では取得していない。**
    → **条文を 1 本取れば確定する。ソムリエへの説明として必要になる場面がありうる。**

11. 🔍 **`vintage='—'`（em-dash sentinel）。**
    **canonical の Hundred Acre 2 件とも該当。DB 全体で 328 レコードに及ぶ systemic な形であり、
    本生産者固有の問題ではない。本書は新しい番号を開かず、既存の掃引結果を参照するにとどめた。**
    → **設計判断は Akio / CTO。**
