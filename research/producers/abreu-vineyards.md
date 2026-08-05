# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件も存在しない。**
> 🔍 **本調査で実測**: `migration/out/export/db_wine_canonical.json` = **928 レコード / 383 の distinct producer 値**。
> **`Abreu` / `abreu` を含む producer は 0 件。**アルファベット順の隣接は `A. Bergère` … `Alban Vineyards` で、
> **`Abreu` が入るべき位置は空である。**畑名（`Madrona` / `Thorevilos` / `Las Posadas` / `Cappella` /
> `Rothwell` / `Tilting`）も **DB 全体で 0 ヒット。**
> **したがって本書は、この生産者に関する THÉSEUS 最初の記録である。**
> 本書は昇格前の研究記録であり、**canonical も OBP も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者の公式サイトで確認**（一次資料）—— 本ドシエでは **`abreuvineyards.com`**
>    （`home` / `about` 5 頁 / `wines` 7 頁 / `stories` 13 頁 / `credits` / `acquire.abreuvineyards.com`）
> `📄` 単一の非公式資料のみ（**本書では事実の根拠に用いていない。§Sources に列挙のみ**）
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `🏛` **公的レジストリ / 認証団体 / 産地規制当局**（本書では **eCFR 27 CFR Part 9・Part 4**、
>    および **照会したが取得できなかった TTB COLA・California Secretary of State**）
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: **2026-08-05** ／ 一次資料: **`http://abreuvineyards.com/`（EN のみ）**
>
> 🔴 **本ドシエ最大の収穫 ①** —— **メニューが印字した 3 つのキュヴェ名は、いずれも公式名の短縮形である。**
> **公式サイト `/wines` が列挙する 6 つのワインの正式表記は**
> **`Thorevilos` / `Cappella` / `Las Posadas Howell Mountain` / `Madrona Ranch` / `Rothwell Hyde` / `Tilting Rock`。**
> → **`'Las Posadas,'` の正式名は `Las Posadas Howell Mountain`（産地名がキュヴェ名の一部）。**
> → **`'Madrona,'` の正式名は `Madrona Ranch`。**
> → **`'Thorevilos,'` のみ公式名と完全一致。** → §Important Cuvées / §Canonical Conflict ②
>
> 🔴 **本ドシエ最大の収穫 ②** —— **`Thorevilos` の `Napa Valley` 表記は、メニュー側の手抜きではない。**
> ✅ **生産者自身が公式ページで明言している ——**
> 「**Thorevilos はどの sub-appellation にも属さない。外れ者（an outlier）だ。
> だがそれは畑にとってもワインにとっても何の違いももたらさない。**」（David Abreu）
> ✅ **同ページは畑を「St. Helena AVA と Howell Mountain AVA の間に挟まっている」と説明する。**
> → 🔴 **したがって `Napa Valley` は、この畑に使える唯一の AVA である。**
>   **ここに canonical conflict を作ってはならない。** → §Location / §Canonical Conflict ③
>
> 🔴 **本ドシエ最大の収穫 ③** —— **生産者は自分のワインを一度も「Cabernet Sauvignon」と呼んでいない。**
> ✅ **公式の自己記述は `single-site Cabernet blends`（単一畑のカベルネ系ブレンド）であり、**
> ✅ **公式 meta description は `Cabernet-driven blends`（カベルネ主体のブレンド）である。**
> ✅ **7 つのワインページのどこにも `Cabernet` の語が出てこない。**
> ✅ **醸造家 Brad Grimes は「われわれのワインをこの品種が何%という形で理解しようとしても、うまくいかない」と明記している。**
> → 🔴 **メニューの `Cabernet Sauvignon` はメニュー側が付けた分類語であり、ラベル表記は未確認である。**
>   **Batch 9 の Harlan（`Proprietary Blend`）、Batch 7 の Mayacamas（`Red Wine`）と同型の構造。** → §Canonical Conflict ④
>
> ⚠️ **調査上の制約 3 点**
> **① 🏛 `TTB COLA` 公開レジストリ（`ttbonline.gov/colasonline/`）が bot 対策のチャレンジを返し、**
>    **画像 CAPTCHA（`What code is in the image?` / support ID `5964387807068716666`）を要求した。**
>    **方針によりこれを回避していない。代替として小売・オークションのラベル画像を使うこともしていない。**
>    **したがってラベル上の brand name / 表示産地 / 品種表示 / アルコール度数 / `Estate Bottled` 表記は本書では未確認。**
>    → Open Questions 2
> **② 🏛 `California Secretary of State` の事業体検索が Imperva/Incapsula にブロックされた**
>    （`Request unsuccessful. Incapsula incident ID: 358000930005291589-11440774992762698`）。
>    **法人格（LLC / Inc. / bonded winery 名）は未確認。** → Open Questions 3
> **③ 🔴 公式サイトは全 6 ワインについて `2019 Vintage` という見出ししか置いていない。**
>    **テイスティングノートもセパージュもアルコール度数も一切無い。**
>    **OBP 掲載の 2021 に対応する公式記述は存在しない。** → Open Questions 1

---

## Identity

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Abreu`**（`producer_or_brand` も `Abreu`。OBP 5 行すべて同一） |
| 🔴 **公式表記** | ✅ 🔴 **`Abreu Vineyards`**。`<title>Abreu Vineyards</title>`（全ページ）／`og:description`「**Abreu Vineyards. Passion beyond reason.**」／`/wines` の `Rothwell Hyde` 解説の本文中に「**Rothwell Hyde may be the wine that most closely defines Abreu Vineyards**」／会員登録ページの見出し「**Welcome to Abreu Vineyards**」「**Thank you for your interest in Abreu Vineyards.**」 |
| 🔴 **canonical 推奨名** | 🔴 **`Abreu Vineyards`**（複数形。`Abreu Vineyard` 単数形は公式ソースに 1 件も存在しない）。**`Abreu` は menu-printed alias として保持する** → §Canonical Conflict ① |
| **公式が掲げる所在** | ✅ **`P.O. Box 89, Rutherford, CA 94573`**（全ページのフッター）<br>🔴 ⚠️ **これは私書箱であり、ワイナリーや畑の所在地ではない。**⚠️ **4 つの畑はいずれも Rutherford ではなく St. Helena 周辺と Howell Mountain にある** → §Location |
| **公式の連絡先** | ✅ **`707-963-3465`** ／ **`info@abreuvineyards.com`**（全ページのフッター） |
| **タグライン** | ✅ **`Passion beyond reason.`**（`og:description`。本文でも「You could call it passion beyond reason. And you may be right.」） |
| **公式の自己規定** | ✅ **`Cabernet-driven blends from the meticulous properties of famed vineyard manager, David Abreu.`**（`meta name="description"`）<br>🔴 **創業者の肩書は winemaker ではなく `vineyard manager`（畑の管理者）である** |
| 🔴 **創業者 / 畑** | ✅ 🔴 **David Abreu**。**Napa Valley 生まれ、牧場主（ranchers）の家系。**「**Napa Valley は David Abreu の遊び場であり、同時に教室でもあった**」。少年期の大半を **Napa の原初の畑（Napa's original vineyards）** で働いて過ごした |
| 🔴 **醸造家** | ✅ 🔴 **Brad Grimes**。✅ **`a chef turned winemaker`（シェフから転じた醸造家）**。公式ページで一人称の長文を多数署名している |
| **畑のクルー（実名で公式に登場）** | ✅ **Jorge Delgado / Francisco Delgado**（vineyard foreman 兄弟。Michoacán 出身。収穫期は毎日ワイナリーに温かい食事を運ぶ）<br>✅ **Jesus Salcedo**（石工。Michoacán から 15 歳で渡米。**1998 年から David と仕事をしている**。畑のアーチと石壁をすべて一人で作る） |
| **ラベルの彫版師** | ✅ **Bob Swartley（Master Engraver）。2016 年 7 月 23 日没。**元は銃器の彫金師 |
| **公式が名指しする外部の協力者** | ✅ **Jake Wheeler**（畑に入れる麦稈の供給者）／✅ **Alta**（ブランド戦略・デザイン）／**Matt Morris**（写真）／**Lab 43**（開発）／**Mora Cronin**（コピーライティング）（`/credits`） |
| 🔴 **認証** | 🔴 ⚠️ **公式サイト全 24 ページに `organic` / `biodynamic` / `certified` / `sustainable` / `Demeter` / `CCOF` / `Napa Green` / `regenerative` の語が 1 件も無い（実測 0 ヒット）。**<br>🔴 **すなわち「生産者は認証を一切自称していない」ことは確定した。**<br>⚠️ **ただし CCOF・Demeter USA・Napa County の各レジストリは本調査で照会していない。**<br>**「認証を保持していない」という断定はできない。**→ §Farming / Open Questions 4 |
| **法人格** | ❓ **未確認。**公式サイトに `LLC` / `Inc.` の表示が無く、🏛 California Secretary of State の検索が Incapsula にブロックされた |
| **販売形態** | ✅ **メーリングリスト制。**「**当会の members list は現在満員です。waitlist へのご登録を…優先順位は登録日に基づきます**」（`acquire.abreuvineyards.com/mailinglist/`）。**国際発送は state ドロップダウンで `IT International` を選ぶ運用** |
| 🔴 **canonical id** | 🔴 **存在しない。**🔍 **canonical 383 生産者に一致・別名・近似いずれも無し** → §Canonical Conflict ① |

⚠️ **`Abreu` と `Abreu Vineyards` のどちらを canonical 名にするか —— 本書の判断根拠**

1. ✅ **公式サイトが自らを名乗る形は例外なく `Abreu Vineyards`**（title / og / 会員ページ / 本文）。
2. ✅ **`Abreu` 単体はナビゲーションのロゴ位置とドメイン名にのみ現れる**（`abreuvineyards.com` の `Abreu` メニュー項目）。
3. 🔴 **canonical の既存 Napa 生産者は `Beringer Vineyards` / `Caymus Vineyards` / `Dalla Valle Vineyards` /
   `Diamond Creek Vineyards` / `Shafer Vineyards` のように、`Vineyards` を含む正式形で登録されている。**
   → 🔍 **既存の命名規約とも `Abreu Vineyards` が整合する。**
4. ⚠️ **ラベル上の brand name は TTB COLA が取得できていないため未確認である。**
   **ラベルが `ABREU` 単体である可能性は排除できない。** → Open Questions 2

---

## Overview

✅ **Napa Valley。David Abreu が自ら計画し、自ら植えた 4 つの畑（Madrona Ranch / Cappella / Las Posadas /
Thorevilos）から、単一畑のカベルネ系ブレンドを造る。**

🔴 ✅ **公式の自己記述の全文（`/about/roots`）は、この生産者の構造をほぼ一文で説明している** ——
「**やがて直感と経験が、彼を 4 つの例外的な畑 —— Madrona Ranch、Cappella、Las Posadas、Thorevilos —— へと導いた。
彼はそのひとつひとつを計画し、植えた。そして妥協なき —— 人によっては狂気じみたと言うだろう —— 品質への献身をもって、
彼と彼のクルーはそれらを完璧に耕す。シェフから転じた醸造家 Brad Grimes とともに、
彼は 100 樽をわずか 12,000 本の単一畑カベルネ・ブレンドへと削り出す。**」

🔴 ✅ **生産量の唯一の公式数字** —— **`100 barrels` → `12,000 bottles`。**
⚠️ **これがどのワインの、どの年の数字なのかは公式に書かれていない。**
🔍 **算術的には 100 樽（1 樽 ≒ 300 本）＝ 約 30,000 本相当から 12,000 本を選び取る、
すなわち約 40% しか瓶詰めしない、という趣旨と読める。**⚠️ **ただし生産者はそう明示していない。断定しないこと。**

🔴 ✅ **哲学の核は「品種ではなく場所」** ——
「**共発酵は、風味を組み立てる方法であり、品種ではなく site を語るワインを造る方法である。**」（David Abreu）

🔴 ✅ **David Abreu 自身の比喩** ——
「**私はこれを、coq au vin のような料理を作ることに喩える。玉ねぎ、人参、マッシュルームを別々に火入れしてから
料理を組み立てたりはしないだろう。素材を一緒に煮込んで、進みながら味を組み立てていく。
品種を別々に発酵させていたら、われわれはこれと同じワインには決して近づけないと思う。**」

🔴 ✅ **David の仕事の姿勢を Brad Grimes が説明した一文** ——
「**彼が実行できないレベルの仕事があった。その支配権を持っていなかったからだ。彼は自分の名前をそこに載せたくなかった。
それが David だ。極端に几帳面なシェフが厨房にいるのと何も変わらない。
自分が納得していない料理は出さない。ゴミ箱に放り込んで、最初からやり直す。**」

🔍 **THÉSEUS における状態** —— 🔴 **canonical に生産者レコードもキュヴェレコードも 0 件。
OBP 掲載 5 本すべてが `producer_state: unresolved`。この生産者は THÉSEUS DB にまだ存在していない。**

---

## History

✅ **公式に年表ページは存在しない。以下は `/about/30-years`・`/about/roots`・`/stories/*`・`/wines/*` の
一人称の記述から復元したものである。**

| 年 | 出来事 |
|---|---|
| **少年期（〜1970s）** | ✅ **牧場主の家系に生まれ、Napa Valley の原初の畑で働いて育つ。**「**1970 年代に Cappella の果実を味わっていた。どんなワインができるか知っていた**」 |
| **1970s–80s（当時の Napa）** | ✅ **David の証言**「**あの頃、農家は仕事のあとにワインではなくマティーニを飲んでいた。農業はもっとビジネス、市場の話だった。4 つの作物のうち 2 つの価格が上がって 2 つが下がれば、たぶん大丈夫、という具合だ。私が近くで追っていたのは Laurie Wood と Chuck Carpy。彼らは畑だけを耕していた。牛も何も飼っていなかった。それに強く惹かれた**」 |
| 🔴 **1980 年代** | 🔴 ✅ **Madrona Ranch —— David が最初に惚れ込み、開発した畑。**「**Abreu に核があるとすれば、それは疑いなく Madrona Ranch である**」 |
| **1980 年代** | ✅ **Newton でプレスから流れ出る Cabernet Franc の果汁を見て衝撃を受ける**（「潰したブルーベリーがステンレスを流れ落ちているようだった」）。**機会を得次第 Madrona Ranch に植え、以後ほとんどの畑に植えるようになる** |
| **1980 年代** | ✅ **教会（カトリック）から依頼され、Cappella の古樹を引き抜く。**以後約 20 年、土地は休閑のまま置かれる |
| 🔴 **1986** | 🔴 ✅ **最初の醸造。Madrona Ranch のカベルネを数樽。**「**彼はこのワインを一度もリリースしなかった。最初のリリースが人を作りも壊しもする、と常々聞かされていた。そして '86 は十分でなかった**」 |
| 🔴 **1987** | 🔴 ✅ **David が最初に販売した Abreu のワイン。**「**私はヴァレー中のレストランにボトルを置いて回って、スタッフと飲んでくれと言った。『気に入ったら電話をくれ』とね**」 |
| **1990s** | ✅ **「このヴァレーで革命が丸ごと起きるのを見た…90 年代に本当に物事が変わった。畑についての考え方が変わり、特別な土地の区画について理解を得た。自転車を漕いでいて、ギアを一段上げたようなものだった」** |
| 🔴 **1986 / 1988 / 1990 / 1998** | 🔴 ✅ **Madrona Ranch の 4 ヴィンテージがすべて declassify された。**「**理由は毎回違ったが、すべて人為的なミスだった**」 |
| **1998** | ✅ **石工 Jesus Salcedo が David と仕事を始める**（畑のアーチと石壁） |
| 🔴 **2000** | 🔴 ✅ **Howell Mountain の Cold Springs Road の物件が競売に出て、David が落札。のちに丘のさらに上、空港の向かいの区画も取得。＝ Las Posadas。**<br>🔴 ✅ **同年、Thorevilos から初めて果実を収穫。**<br>✅ **同年、David は Stuart Sloan の施設でワインを造っていた。選果（sorting）の効果をめぐる Stuart との議論があった年** |
| 🔴 **2006** | 🔴 ✅ **4 つの estate 畑すべてから収穫するようになる**（Brad Grimes） |
| **2015 頃** | ✅ **Las Posadas の開発に 15 年を要した**（「It took him 15 years to develop the property」＝ 2000 年取得から逆算して 2015 年前後） |
| **2016-07-23** | ✅ **彫版師 Bob Swartley 逝去** |
| 🔴 **2020** | 🔴 ✅ **Napa Valley の山火事が Thorevilos 周囲の森（second growth redwood・sequoia・oak・madrone）をほぼ焼き尽くす。**復元作業が始まる |
| **公式サイト取得時点** | 🔴 ⚠️ **全 6 ワインの現行表示が `2019 Vintage` である** |

⚠️ **公式に無い**: 各畑の取得年（Las Posadas の 2000 年以外）、Madrona Ranch と Cappella の植栽年、
ワイナリー施設の取得・建設年、Brad Grimes の着任年、生産者の設立年（法人設立年）。
**「30 Years」というページ名から逆算した創業年を書かないこと** —— ページに年号が入っていない。

---

## Location

| | |
|---|---|
| **Country** | **United States** ✅ |
| **State / County** | **California / Napa County** ✅ |
| **公式の掲出住所** | ✅ **`P.O. Box 89, Rutherford, CA 94573`**（🔴 私書箱であり畑の所在ではない） |
| 🔴 **畑の数** | ✅ 🔴 **4 つ**（Madrona Ranch / Cappella / Las Posadas / Thorevilos）。**すべて David Abreu が自ら計画し植えた** |
| **ワインの数** | ✅ **6 つ**（上記 4 つの単一畑 ＋ 2 つの畑間ブレンド `Rothwell Hyde` と `Tilting Rock`） |

### ✅ 畑ごとの公式記述

| 畑 | 位置 ✅ | 土壌・地形 ✅ | 来歴 ✅ |
|---|---|---|---|
| 🔴 **Madrona Ranch** | ✅ **St. Helena の町の西縁**（`sites hovering on the western edge of the town of St. Helena`） | 🔴 ✅ **赤い Aiken、白い tufa、暗色の粘土、そして岩 —— この幅を一つの畑が持つ。**峡谷とカーブが敷地を蛇行する。**Spring Mountain から下りてくる ephemeral creek（季節性の小川）が走る** | ✅ **David が最初に惚れ込み、1980 年代に開発した最初の物件。**「**Abreu に核があるとすれば、それは疑いなく Madrona Ranch**」。🔴 **現役の ranch でもある —— 牛・山羊・豚・鶏、そして古い納屋に住む蜜蜂。**「動物は世話をするが、蜂には手を出さない。蜂蜜は採るがね。あれは正当な家賃だと思っている」 |
| **Cappella** | ✅ **St. Helena の町の西側、カトリック墓地の隣** | ✅ **6 エーカー** | ✅ **St. Helena で最も古い畑の一つ。初植栽 1869 年。**1980 年代に教会の依頼で古樹を抜根 → 約 20 年休閑 → 再植 → **病気に冒された台木のため再び抜根** →「**収穫を得るまでに 6 年かかった。無視して、倒れた樹から 1 本ずつ抜いていくこともできた。だがそうすると熟期がばらばらになり、一貫性に響く。簡単な判断だった**」 |
| 🔴 **Las Posadas** | ✅ 🔴 **Howell Mountain。標高およそ 2,000 フィート。**✅ **霧の層より上（above the fog line）。**モミと松の保護林に囲まれる | ✅ **赤い Aiken 土壌が白い tufa の上に層をなす。**敷地に散乱していた岩は、いまや境界を画す石壁になっている | ✅ **2000 年、Cold Springs Road の物件が競売に出て落札。**のちに丘の上、空港の向かいの区画も。**取得時に思わぬ副産物 —— 一世紀以上前の first growth redwood の支柱。**「**大学がこの敷地を持っていた頃は、下草を支柱ごと全部焼いて清潔に保っていた。私が入ったとき、それらを見つけて全部脇に取り分けた**」。**1800 年代にここには畑があった**（Krug・Keyes・Hastings ら開拓者の名が歴史書にある） |
| 🔴 **Thorevilos** | 🔴 ✅ **谷底より上、`St. Helena AVA と Howell Mountain AVA の間に挟まっている`。**✅ **mid-mountain climate**（中腹の気候）。**St. Helena の東斜面** | ✅ **Boomer および Forward series の土壌。小石まじりで、一貫して水はけがよい。**✅ **剃刀のように鋭い北向きの畝** | ✅ **200 エーカーの土地から、David が 40 vine acres を刻み出した。**✅ **David の少年期の遊び場だった**（「当時は樹が無かった。松、レッドウッド、古いオリーヴ林だけ」）。🔴 **2020 年の山火事が周囲の森をほぼ破壊した** |

### ✅ 追加の地名

- ✅ **`Tilting Rock` は畑ではなく地名（ランドマーク）である。**
  「**Thorevilos の最も奥、eastern St. Helena の Howell Mountain Road の下に隠れている。
  何十年もの間、地元の人々は未舗装路と踏み分け道をたどってこの象徴的な自然のモニュメントを見に来た。**」
- ✅ **Madrona Ranch と Cappella は「わずか 1/4 マイルしか離れていないのに、まったく別物」。**
  **David はこの 2 つのちょうど中間に住んでいる。**
- ✅ **かつて St. Helena の西側はクルミとプルーンの果樹園だったが、いまは学校・教会・住宅地になっている。**
  「**それらはたまたま、Napa Valley で最も望ましい土壌の上に建っている。**」
  **Cappella と Madrona Ranch は、その開発に囲まれながら手つかずで残った小さな畑のパッチワークの一部である。**

### 🏛 AVA の法的関係 —— **メニューの 3 つの産地表記を規制一次資料に照らす**

**［規制一次資料］27 CFR Part 9（AVA 定義）および Part 4（表示規則）。
これは規制の一次資料であって、生産者の証言ではない。**

| 🏛 条 | AVA の法定名 | 本件に効く定義 |
|---|---|---|
| **§ 9.23** | **`Napa Valley`** | 🏛 **Napa County 内に所在。境界は Napa–Lake 郡界、Putah Creek と Lake Berryessa の西岸・南岸、Napa–Solano 郡界、Napa–Sonoma 郡界。**［T.D. ATF-79, 46 FR 9063, 1981-01-28；T.D. ATF-201, 50 FR 12533, 1985-03-29 により改正］ |
| **§ 9.94** | **`Howell Mountain`** | 🔴 🏛 **「Howell Mountain viticultural area は California 州 Napa County に所在し、`Napa Valley viticultural area の一部である`」と条文が明記している。**🔴 **境界は全周が `1,400 フィート等高線`。**［T.D. ATF-163, 48 FR 57487, 1983-12-30；T.D. ATF-249, 52 FR 5960, 1987-02-27 により改正］ |
| **§ 9.149** | 🔴 **`St. Helena`**（**法定名は `St. Helena` であり `Saint Helena` ではない**） | 🏛 **Napa County 内に所在。境界は Zinfandel Lane、Bale Slough、Inglewood Avenue の延長線、`500 フィート等高線`、Sulphur Creek、`400 フィート等高線`、Bale Lane、Silverado Trail、`380 フィート等高線`、St. Helena 市境、Howell Mountain Road、Conn Valley Road。**⚠️ **条文中に「Napa Valley の一部である」という Howell Mountain 型の明示句は無い**（ただし境界は Napa County 内に完結し、§9.23 の Napa Valley 境界に内包される） |

| 🏛 条 | 規則 | 本件への含意 |
|---|---|---|
| **§ 4.25(e)(3)(ii)** | 🏛 **AVA をラベルに名乗るには、ワインの `85%` 以上がその AVA の境界内で育った葡萄由来であること** | **`Howell Mountain` を名乗る Las Posadas は、法的に Napa Valley を名乗ることもできる（入れ子だから）。逆は成り立たない** |
| **§ 4.25(e)(4)** | 🏛 **重なり合う AVA を複数併記する場合、重複域産が `85%` 以上必要** | — |
| **§ 4.27(a)(1)** | 🏛 **AVA を表示するヴィンテージワインは、`95%` 以上が表示年の収穫であること** | **`2019` `2021` の表示は 95% ルール下にある** |
| **§ 4.23(b)** | 🔴 🏛 **単一品種名を type designation に使えるのは、その品種由来が `75%` 以上のときのみ** | 🔴 **メニューの `Cabernet Sauvignon` が正しければ、各ワインは毎年カベルネ・ソーヴィニヨン 75% 以上でなければならない。**⚠️ **生産者は「品種比率は毎年必ず変わる」と明言している。ラベルが実際に何と書いてあるかは COLA 未確認** → §Canonical Conflict ④ |
| **§ 4.26(a)** | 🏛 **`Estate bottled` は、AVA 表示があり、瓶詰めワイナリーがその AVA 内に所在し、葡萄を自社所有／管理地で全量栽培し、破砕から瓶詰めまで連続工程である場合のみ使える** | ❓ **Abreu のラベルがこの語を使っているかは未確認** |

🔴 **結論 —— メニューの 3 つの産地表記の判定**

| メニュー印字 | 判定 | 根拠 |
|---|---|---|
| **`Howell Mountain`**（Las Posadas） | 🔴 ✅ **公式と一致。むしろメニューの方が控えめ。** | ✅ **生産者自身がワイン名を `Las Posadas Howell Mountain` としている**（`/wines`）。✅ **公式ページは畑を「Howell Mountain の物件」「標高およそ 2,000 フィート」と書く。**🏛 **§9.94 の境界は 1,400 フィート等高線であり、2,000 フィートはその内側にある。**🔍 **生産者証言と規制幾何が独立に一致する。** |
| **`Saint Helena`**（Madrona Ranch） | ⚠️ **産地としては未確認。表記としては法定名と不一致。** | ⚠️ **生産者は Madrona Ranch に AVA を一度も付していない。**公式の言い方は「**St. Helena の町の西縁**」であり、これは **町（town）** の言及であって AVA の主張ではない。🏛 **§9.149 は St. Helena AVA の西側境界を 500 フィート／400 フィート等高線で定めており、町の西縁の畑がその内側か外側かは、標高が公表されていない以上、本書では判定できない。**🔴 🏛 **加えて法定 AVA 名は `St. Helena` であって `Saint Helena` ではない。** → §Canonical Conflict ③ |
| **`Napa Valley`**（Thorevilos） | 🔴 ✅ **正しい。メニューの不備ではない。** | 🔴 ✅ **David Abreu 自身が「Thorevilos はどの sub-appellation にも属さない。外れ者だ」と公式ページで明言。**✅ **同ページは「St. Helena AVA と Howell Mountain AVA の間に挟まっている」と説明する。**🔍 **両 AVA の間の谷／斜面は、どちらの等高線条件も満たさない領域であり、使える AVA は上位の `Napa Valley` のみになる。**🔴 **ここに conflict を立ててはならない。** |

🔴 **入れ子は矛盾ではない。** 🏛 **§9.94 が明文で「Howell Mountain は Napa Valley の一部」と書いている以上、
`Howell Mountain` と `Napa Valley` が同じ生産者の隣り合う行に並ぶことは、何ら不整合ではない。**
**同様に St. Helena も Napa County 内に完結する。**

❓ **公式に無い**: 各畑の面積（Thorevilos の 40 vine acres と Cappella の 6 エーカー以外）、標高
（Las Posadas の「約 2,000 フィート」以外）、植栽密度、台木、クローン、樹齢、方位（Thorevilos の北向き以外）、
畝間、年間生産本数の内訳。

---

## Farming

🔴 **本節は §Winemaking と並んで本ドシエで最も強い部分である。**
**生産者は「畑が主で、醸造は従」という順序を公式に明言しており、畑の記述の方が厚い。**

### 🔴 ✅ 畑ごとの専属クルー —— **Abreu の最も特徴的な仕組み**

✅ **公式の原文（`/about/winegrowing`）** ——
「**うちの連中は自分の畑を手の甲のように知っている。それぞれの畑には、一年中、毎年、それを世話する
一つのクルーがつく。彼らが剪定し、枝を配置し、間引く。シーズンの終わりに近づくと、
房から未熟な粒を親指で落としていく。そして彼らが収穫する。収穫のあとは、
ワイナリーの選果台に立つのも彼らだ。彼らがその果実に所有権（ownership）を持つ、ということだ。
彼らが育てた。彼らが知っている。彼らはそれを誇りに思っている。**」
✅ **Brad Grimes の付け足し** ——「**実のところ、彼らはそれについてかなり競争的なんだ。**」

🔴 **すなわち作業の単位が「作業ごとの班」ではなく「畑ごとの通年の班」である。**
**これは剪定・枝配置・摘葉・粒単位の摘果・収穫・選果台までを同一チームが担うということであり、
Napa の大規模生産者で一般的な作業別外注とは構造が異なる。**

✅ **David Abreu 自身の言葉（`/about/people`）** ——
「**私はチームなしでは何者でもない。彼らが私の事業の背骨だ。何がわれわれを分けるか？
われわれは決して `no más`（もう無理だ）と言わない。**」

### ✅ 畑に入れる資材

- 🔴 ✅ **麦稈（wheat straw）** —— **供給者は Jake Wheeler。**
  **穀物を収穫したあとの刈り株を、Sacramento Valley の小麦農家から買い、自分で畑を歩いて検分してから
  刈り、梱包する。**「**清潔で、雑草の混じらない麦稈でなければいけない。`trashy` なものはだめだ。
  畑に望まない雑草を持ち込むようなものは。基準に満たなければ積み込まれない。**」
  「**David が何を望んでいるかは分かる。届けられないなら、はじめから関わらないことだ。**」
  🔍 **用途は明示されていないが、文脈（畑に入れる／雑草を持ち込まない）から
  マルチまたは土壌被覆材と読める。**⚠️ **公式は用途を書いていない。断定しないこと。**
- ✅ **オリーヴ** —— **各畑にオリーヴが植わっており、葡萄と同じくらい畑ごとに個性の違うオイルを産む**
  （`Extra Virgin Olive Oil`）。**David に olive oil の話を振ると、必ず Rutherford で育った話から始まる。**
- ✅ **ブラックベリー** —— **Madrona Ranch のブラックベリーは、Spring Mountain から下りてくる
  ephemeral creek に沿って生える。季節は早く、そして短い。7 月 4 日には最初の実が熟している。**

### 🔴 ✅ 2020 年火災後の森の再生（**Thorevilos。生産者の一人称**）

「**われわれは 1,000 本の樹を植え、一年以上にわたって手で水をやった。侵食を防ぐために麦稈のベールと
ネットを敷いた。そして私は、健康な地下の oak と madrone の root ball から出てくる sucker を
仕立て上げている。そうすれば大きく先行できるからだ。いずれこの場所は公園のように見えるようになる。
だが開けた形にしておく —— また火が来たとき、あの下草を、あの燃料を抱えていないように。
その可能性に備えて管理しなければならない。**」（David Abreu）

🔴 **これは「畑」ではなく「畑を囲む森」に対する作業である。**
**Abreu は林床の燃料管理を明示的に自分の仕事の範囲に入れている。**

### ✅ 石積み（**畑の景観そのものが手仕事である**）

「**畑によっては看板があるが、うちにはアーチがある。すべて同じ人物 —— Jesus Salcedo —— が作っている。
壁もそうだ。**」**彼は石灰岩を使い、大きな岩の外側の「皮」を剥ぎ、ジグソーパズルのように合わせる ——
目地は一切見えない。刃を選び、切り、切り口を鑿で叩いて自然に見えるようにする。一つ一つ手で。
欠けさせてはいけない、簡単に割れてしまうから。**
**1998 年から David と組んでいて、常に一人で働く。一度だけ助手を入れたが、
David が仕上がりを見て、どの石が Jesus の手で、どの石が助手の手かを言い当てた。**

### ⚠️ 認証について —— **「自称ゼロ」は確定、「不在」は未確定**

🔴 ⚠️ **公式サイト全 24 ページを機械的に走査した結果、
`organic` / `biodynamic` / `certified` / `sustainable` / `Demeter` / `CCOF` / `Napa Green` /
`regenerative` / `fish friendly` のいずれの語も 1 件も出現しなかった（実測 0 ヒット）。**

- 🔴 **確定したこと** —— **Abreu Vineyards は、いかなる有機・ビオディナミ・サステナビリティ認証も自称していない。**
  **公式の語彙は `meticulous`（几帳面）、`uncompromising`（妥協なき）、`farm them to perfection`（完璧に耕す）であって、
  認証や体系名ではない。**
- ⚠️ **確定していないこと** —— 🏛 **CCOF・Demeter USA・Napa County / Napa Green の各レジストリは
  本調査で照会していない。**（照会を試みた 🏛 レジストリは TTB COLA と California Secretary of State の 2 つのみで、
  いずれも bot 対策にブロックされた。）
  **したがって「認証を保持していない」と断定してはならない。** → Open Questions 4

❓ **公式に無い**: 農薬・除草剤・肥料の方針、耕起の有無、カバークロップの草種、灌漑の有無と方式、
収量（t/acre、hl/ha いずれも）、収穫日、収穫方法（手摘みか機械か —— ただし「選果台に立つ」記述から手摘みと推測できるが、
生産者は明示していない）。

---

## Winemaking

🔴 ✅ **Abreu の醸造は一語で要約できる —— `co-fermentation`（共発酵）。
そしてそれは思想ではなく、設備の制約から偶然生まれた。**

### 🔴 ✅ 起源 —— **2 つのタンクしか無かったこと**

✅ **Brad Grimes の原文（`/about/winemaking`）** ——
「**最良の実験というのは、ときに、ただ起きてしまうものだ。David が 80 年代にワインを造り始めたとき、
彼は自分のワイナリーを持っていなかった。使えるタンクが 2 つしかなかったので、
果実を全部 1 日で持ち込まなければならなかった。全部を一度に摘まなければならなかった。
まず Cab と Cab Franc が一緒に来て同じタンクに入り、次に Merlot が来て、最後に Petit Verdot。
摘んだものが何であれ、タンク 2 つ分。それがブレンドの作られ方だった。
いまは違う。必要なだけのタンクと時間がある。もっと意図的だ。だがわれわれは今も共発酵する。
われわれがやろうとしていることに、それが効くからだ。**」

🔴 **ここで公式に名が出る 4 品種** —— ✅ **Cabernet Sauvignon / Cabernet Franc / Merlot / Petit Verdot。**
⚠️ **ただしこれは 1980 年代の逸話の中の記述であり、現在の各ワインのセパージュではない。**

### 🔴 ✅ 摘み方 —— **品種ではなく「その日に仕上がっている粒」を摘む**

✅ **Brad Grimes** ——
「**われわれは、ある一日に仕上がるであろう葡萄を見極める。そしてそれを摘む。品種にかかわらず。
ブロックごとに摘むという specificity の考え方は理解している。だがブロックの中にもこれだけの差がある。
2 週間前に摘めたはずの樹や、房さえあるかもしれない。だから収穫の数週間を通じて、
私は果実を味わい、いま満たしつつあるタンクのことを考え、この pick をどう組み立てるかで頭を回している。
そしてそこが、私がやれる仕事の本当に面白いところだ。
`ブロック 7 のカベルネが毎年最初に来る` というような反復が無い。
一つ一つの発酵がすべて違う。決して繰り返せない。**」

### 🔴 ✅ ブレンドの手順（**Brad Grimes が段階として明記している唯一の公式手順**）

| 段階 | 内容 ✅ |
|---|---|
| **① 畑での選択** | **単一の畑から、複数のブロックにまたがり、品種をまたいで選択的に摘み、それらを一緒に発酵させる。**「**これがブレンドの第一歩 —— 畑での選択だ**」 |
| **② 複数の発酵** | **単一畑の site が、複数の発酵を生む** |
| **③ 個別に樽へ・1 年** | **それらのロットは別々に樽に入れられ、`1 年` 熟成してからブレンド試験が始まる** |
| **④ 評価** | **各ロットの代表サンプルを樽から抜き、その「兄弟たち」と相対的に評価する** |
| **⑤ core blend** | **通常、`2 〜 3 の発酵` から core blend が組まれる。その site の残りの樽は、より小さな比率でワインを完成させるのに使われる** |
| **⑥ 再結合・さらに 1 年** | 🔴 **ブレンドが確定すると、樽が一つに合わされ、瓶詰め前に `さらに 1 年` 一緒に熟成する** |

🔍 **③ と ⑥ を合わせると樽熟期間は約 2 年になる。**
⚠️ **ただし生産者は「合計 24 ヶ月」とは書いていない。新樽比率・樽のメーカー・産地・トースト・容量も一切書いていない。**

### 🔴 ✅ 歴史的な変遷（Brad Grimes）

「**ブレンドはかつてもっと単純だった。80 年代と 90 年代、David は Madrona Ranch の葡萄を全部同じ日に持ち込み、
2 つのタンクで並べて発酵させ、樽へ移すときに両方を一つにした。それがブレンドであり、それがワインだった。**
**2000 年に物事が変わり始めた。Thorevilos から初めて果実を採った年だ。
同じ年、Madrona Ranch を 3 回に分けて収穫し、発酵後もそれらのロットを分けて保った。
2006 年までに、4 つの estate 畑すべてから収穫するようになっていた。**」

### 🔴 ✅ 品種比率について —— **生産者自身の警告**

🔴 **Brad Grimes の原文** ——
「**私は人にこう言う。われわれのワインを、この品種が何%、あの品種が何%という形で理解しようとしても、
うまくいかない、と。これはわれわれの properties から来るワインだ。
そして一つ一つの発酵がすべて違うのだから、品種の比率は常に違うことになる。
この造り方をするということは、農業と摘みのあらゆる側面を支配下に置くということであり、
それが Abreu のやり方だ。**」

### ✅ Cabernet Franc の位置づけ（David Abreu）

「**Cabernet Franc はブレンドを別の次元へ引き上げる。それは味わいの中央にまっすぐ入り込み、
穴を埋める。偉大な一本のワインの sweet spot だ。**」
✅ **Madrona Ranch の古い Franc は、毎年 Madrona のブレンドにかなりの量を供給している。**

### 🔴 ✅ ボトル —— **1896 年の第一級ワインの型を復刻したもの**

✅ **Brad Grimes の原文（`/stories/the-bottle`）** ——
**David がボトルの原型を探していたとき、Marin Wine Cellar（2006 年閉店）の Paul と Harvey が、
1800 年代後半から 1900 年代初頭の何百本ものボトルを並べた。すべて手吹きだった。
「様式化され、華美で、極端で、それでいて非常に軽かった。パントは巨大だった。」**
🔴 **David は `1896 年の first-growth` のボトルに絞り込んだ。手に持った感触が気に入ったからだ。**
**それを買い、中身を友人と飲み、ガラス職人に見せたが、誰も複製できなかった。
そこで病院に頼んで CAT スキャンにかけ、密度の構造を明らかにした。
最終的にフランスの調香師（perfumer）に繋がり、その人物が型を作ることができた。**
「**David がこのボトルを作らせるまで、ガラス会社は標準ボトルの既製版しか作っていなかった。
誰も古いボトルを再現していなかった。David は彼らに、後ろを振り返ることは前を見ることと同じくらい
大切だと示したのだ。**」

### 🔴 ✅ ラベル —— **紙幣用の凹版印刷機で、1 回 100 枚ずつ**

✅ **原文（`/stories/labelling`）** ——
「**われわれのラベルは Cronite の intaglio press（凹版印刷機）で刷られている。
Cronite は 1900 年代初頭から、あるいはもっと前からある。米国造幣局が紙幣を刷るのに使っていた ——
再現できるディテールの水準が高いからだ。うちの印刷業者は主に高級文具や結婚式の招待状にこの機械を使う。
他のワインラベルは一切刷っていない。手間がかかりすぎるからだ ——
弱っているところに付け込んだのかもしれない。
ラベルの絵は金属板に彫刻されている。1 枚のラベルを完成させるのに `4 回` 通す。
プレスは手動で、完全に非電動。ロットは小さく、`一度に約 100 枚`。遅々としているが、
そのディテールが気に入っている。**」

✅ **彫版は Bob Swartley（Master Engraver）。**古式銃の彫金から出発し、19 歳で夜 7 時から深夜まで
週 6 日、指の感覚が無くなるまで独学した。1960 年代初頭に New York の Griffin & Howe で Josef Fugger の
弟子となる。**半引退後も Abreu の畑に何度も通い、鉛筆でスケッチし、ほぼ仕上がると David に見せた。
彫刻は Napa のスタジオで、拡大鏡と低倍率顕微鏡と針より鋭い道具を使い、一人で行った。
一つの図版に数週間かかることもあった。板は必ず Cronite（同じ印刷機のメーカー）から買った鋼板 ——
「非常に細かい木目」で、他に同等のものを見つけられなかったから。**
**2016 年 7 月 23 日逝去。**

❓ **公式に無い**: 酵母（天然か培養か）、マロラクティック発酵、発酵温度、浸漬期間、
パンプオーバー／パンチダウンの別、プレスの種類、清澄・濾過の有無、亜硫酸、
新樽比率、樽の産地とメーカー、アルコール度数、pH、酸度、瓶詰め日、生産本数の内訳。

---

## Style

🔴 ⚠️ **公式サイトには、どのワインについても、いかなるテイスティングノートも存在しない。**
**`2019 Vintage` という見出しが置かれているだけである。**
**したがって本節で書けるのは、生産者が質的に述べた性格の言葉に限られる。**

| ワイン | 生産者自身の言葉 ✅ |
|---|---|
| 🔴 **Thorevilos** | ✅ **Brad Grimes** ——「**St. Helena の上の東斜面から来るワインには、紛れもない野生（wildness）がある。Thorevilos はその基準点だ。露出した岩の不毛な景観は、多くのものが育つのを困難にする。ここは badlands、見つけられたくないものが見つかる場所だ。**」 |
| 🔴 **Tilting Rock** | ✅ **「St. Helena の上の東斜面から来るワインには野生がある —— 真夜中のコヨーテの遠吠えのように手に取れる獰猛さが。」**✅ **Brad Grimes** ——「**収穫時、両方の site から選んだ果実を発酵させ、畑と品種の間の共通の絆を見つける。果実の融合がワインを変質させる。私はそれを錬金術に喩える。結果として得られるのは、トランポリンの上や、ブランコの最高点で得られる、あのスリリングな無重力感だ。**」<br>✅ **「これを `mountain wine` と呼ぶのは、誘惑的ではあるが、単純にすぎ、広すぎる。これは山の心臓を貫くワインであり、その荒々しい景観を反響させながら、二つの消せない site の specificity を語るワインだ。**」 |
| 🔴 **Rothwell Hyde** | ✅ **Brad Grimes** ——「**Rothwell Hyde は最高水準のブレンドだ。私は収穫時にブレンドする —— Cappella と Madrona の葡萄を、熟度の essence において共発酵させる。ワイナリーでもブレンドする —— ワインが熟成を続ける間、風味・テクスチャー・構造を引き上げていく。このワインを造ることには自由がある。`Rothwell Hyde は Abreu の表現であって、必ずしも単一畑ではない`。**」<br>✅ **David Abreu** ——「**Rothwell Hyde は、われわれがやっていることのすべてを一本のワインに入れたものだ。**」 |
| **Madrona Ranch** | ✅ **「収穫の摘みは綿密で、しばしば数週間にわたる。だがその多様性が信じがたい複雑さと、豊富なブレンドの選択肢を生む。**」 |
| **Las Posadas** | ⚠️ **ワインの性格についての記述は公式に無い。**（記述は畑・土壌・レッドウッドの支柱に限られる） |
| **Cappella** | ⚠️ **ワインの性格についての記述は公式に無い。**（記述は畑の来歴に限られる） |

⚠️ **`Abreu` のスタイルを一般論として語らないこと。**
**生産者自身が「一つ一つの発酵がすべて違う。決して繰り返せない」と書いている。**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本。すべて `unresolved`。
セクションは全て `UNITED STATES | RED > NAPA`、`section_start_page` = `25`、producer heading は `Abreu`**）

| # | source_row_id | 行 | OBP 印字 | VT | 価格 | ✅ **公式の正式名 / 確認結果** |
|---|---|---|---|---|---|---|
| 1 | `obp-beverage-2026-08:7be8872fe2` | `1216` | **`'Las Posadas,'` Howell Mountain Cabernet Sauvignon** | **2021** | **$2,640** | 🔴 **正式名は `Las Posadas Howell Mountain`**（`/wines` の一覧表記）。**産地名がキュヴェ名の一部である。**✅ **産地 `Howell Mountain` は生産者自身の表記と一致。**⚠️ **2021 の公式記述は存在しない**（公式は `2019 Vintage`）。⚠️ **`Cabernet Sauvignon` はメニュー側の分類語** |
| 2 | `obp-beverage-2026-08:3a2698f611` | `1217` | **`'Las Posadas,'` Howell Mountain Cabernet Sauvignon** | **2019** | **$2,505** | 🔴 **同上。**🔴 ✅ **2019 は公式が現行として掲げているヴィンテージであり、存在が確認できる唯一の年である。**⚠️ **ただしテイスティングノートは無い** |
| 3 | `obp-beverage-2026-08:6b5f2f64f5` | `1218` | **`'Madrona,'` Saint Helena Cabernet Sauvignon** | **2021** | **$2,640** | 🔴 **正式名は `Madrona Ranch`。**`Madrona` 単体は公式の表記ではない。⚠️ **産地 `Saint Helena` は生産者が付していない**（公式は「St. Helena の町の西縁」という位置の説明のみ）。🏛 **法定 AVA 名は `St. Helena`。**⚠️ **2021 の公式記述なし** |
| 4 | `obp-beverage-2026-08:33560f82d0` | `1219` | **`'Madrona,'` Saint Helena Cabernet Sauvignon** | **2019** | **$2,505** | 🔴 **同上。**✅ **2019 は公式の現行ヴィンテージ** |
| 5 | `obp-beverage-2026-08:d792fe681b` | `1220` | **`'Thorevilos,'` Napa Valley Cabernet Sauvignon** | **2021** | **$2,640** | 🔴 ✅ **キュヴェ名が公式と完全一致する唯一の行（`Thorevilos`）。**🔴 ✅ **産地 `Napa Valley` も正しい —— 生産者自身が「どの sub-appellation にも属さない」と明言している。**⚠️ **2021 の公式記述なし** |

🔍 **intake の格納形** —— **5 行すべて `layout: producer_heading`、`flags: []`（例外なし）、
`unparsed_segment` は空。`product_name` にキュヴェ名（`Las Posadas` / `Madrona` / `Thorevilos`）、
`classification_text` に「産地 ＋ Cabernet Sauvignon」が入る。**
🔴 **すなわちパースは正常であり、問題は canonical 側に生産者が存在しないことだけである。**

### 🔴 ✅ 公式サイトが提示するワインの全数（`abreuvineyards.com/wines`。**6 つ**）

| # | 🔴 **公式の正式表記** | 種別 ✅ | 構成 ✅ | OBP |
|---|---|---|---|---|
| 1 | **`Thorevilos`** | **単一畑** | **Thorevilos** | ⭐ **×1（2021）** |
| 2 | **`Cappella`** | **単一畑** | **Cappella**（6 エーカー、1869 年初植） | — |
| 3 | 🔴 **`Las Posadas Howell Mountain`** | **単一畑** | **Las Posadas**（Howell Mountain、約 2,000 ft） | ⭐ **×2（2021 / 2019）** |
| 4 | 🔴 **`Madrona Ranch`** | **単一畑** | **Madrona Ranch** | ⭐ **×2（2021 / 2019）** |
| 5 | **`Rothwell Hyde`** | 🔴 **畑間ブレンド** | 🔴 **Madrona Ranch ＋ Cappella**（収穫時の共発酵＋ワイナリーでのブレンド）。**「Abreu Vineyards を最もよく定義するワインかもしれない」** | — |
| 6 | **`Tilting Rock`** | 🔴 **畑間ブレンド** | 🔴 **Thorevilos ＋ Las Posadas**（「標高が大きく異なる、St. Helena 東斜面の 2 畑」） | — |

🔴 **重要 —— `Rothwell Hyde` と `Tilting Rock` は「セカンドワイン」ではない。**
**公式はこれらを単一畑ワインの格下として扱っていない。**
**`Rothwell Hyde` については「Abreu Vineyards を最もよく定義するワインかもしれない」とまで書いている。**
**OBP には登場しないが、canonical に登録する際は 6 本を対等に扱うのが公式の構造と整合する。**

### ⚠️ 公式に確認できたヴィンテージ

| ワイン | 公式が掲げている年 |
|---|---|
| **全 6 ワイン** | 🔴 ⚠️ **`2019` のみ。**`<h4>2019 Vintage</h4>` という見出しが各ワインページに 1 つ置かれているだけで、**本文もリンクも PDF も無い。** |
| 🔴 **OBP の `2021`** | 🔴 ⚠️ **公式ソースに一切の記述が存在しない。**存在を否定する材料も無い。**単に公式サイトが更新されていないだけの可能性が高い**（同サイトは 2020 年の山火事に言及しており、2020 年以降に更新されている）。**しかし本書はこれを推測として扱い、2021 の存在を公式に確認したとは主張しない。** → Open Questions 1 |
| **過去に declassify された年** | 🔴 ✅ **Madrona Ranch の `1986` `1988` `1990` `1998`**（すべて人為的ミスによる）。**`1986` は最初の醸造そのもの。**✅ **`1987` が最初に販売されたヴィンテージ** |

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 造り手は醸造家ではなく「畑の人」です。ワインは畑の名前そのものです。**
「**Abreu Vineyards は、David Abreu という、Napa で最も名を知られた `vineyard manager`（畑の管理者）の
生産者です。彼は牧場主の家系に生まれ、少年時代を Napa の古い畑で働いて過ごしました。**
**公式サイトの自己紹介も『**名高い vineyard manager, David Abreu の几帳面な properties から来る、
カベルネ主体のブレンド**』という一行です。**
**彼が自分で計画し、自分で植えた畑が 4 つあります —— Madrona Ranch、Cappella、
Las Posadas（Howell Mountain）、Thorevilos。ワインの名前は、そのまま畑の名前です。**
**醸造はシェフから転じた Brad Grimes が担当し、100 樽をわずか 12,000 本に削り出します。**」

**② リストの `'Las Posadas,'` と `'Madrona,'` は短縮形です。正式名は `Las Posadas Howell Mountain` と `Madrona Ranch`。**
「**造り手のワインリストでは、`Las Posadas` には `Howell Mountain` まで含めて一つの名前になっています。
産地名がキュヴェ名の一部なんです。**
**`Madrona` の正式名は `Madrona Ranch` —— これは比喩ではなく、本当に稼働している ranch です。
牛、山羊、豚、鶏、そして古い納屋には蜜蜂が住んでいます。造り手はこう言っています ——
『動物は世話をするが、蜂には手を出さない。蜂蜜は採るがね。あれは正当な家賃だと思っている』。**
**`Thorevilos` だけがリストの印字と正式名が完全に一致しています。**」

**③ `Thorevilos` の `Napa Valley` は、手抜きではなく造り手自身の言葉です。**
「**Thorevilos は St. Helena AVA と Howell Mountain AVA の`間に挟まって`いて、
David Abreu 自身が公式にこう言っています ——
『**Thorevilos はどの sub-appellation にも属さない。外れ者だ。
だがそれは畑にとってもワインにとっても何の違いももたらさない**』。**
**だから `Napa Valley` としか名乗れないし、それが正しい表記です。**
**200 エーカーの土地から 40 エーカーだけを畑として刻み出した場所で、土壌は Boomer と Forward series、
小石まじりで水はけがよい。畝は剃刀のように鋭い北向きです。**
**醸造家はこう表現します ——『ここは badlands、見つけられたくないものが見つかる場所だ』。**」

### 追加で使える一手

- 🔴 **共発酵（co-fermentation）の由来**：「**始まりは思想ではなく、設備の制約でした。
  80 年代、David は自分のワイナリーを持たず、使えるタンクが 2 つしかなかった。だから果実を全部 1 日で摘んで
  持ち込むしかなかった。カベルネとカベルネ・フランが一緒に来て同じタンクへ、次にメルロ、最後にプティ・ヴェルド。
  摘んだものが何であれタンク 2 つ分 —— それがブレンドでした。
  いまはタンクも時間もありますが、それでも共発酵を続けています。**
  **David の比喩がわかりやすい ——『coq au vin を作るのに、玉ねぎと人参とマッシュルームを別々に火入れして
  あとから組み立てたりはしないだろう』。**」
- 🔴 **畑ごとの通年クルー**：「**それぞれの畑に、一年中・毎年その畑だけを世話する一つのクルーがつきます。
  剪定、枝の配置、間引き、シーズン終盤には房から未熟な粒を親指で落とす作業、そして収穫。
  収穫後にワイナリーの選果台に立つのも同じ人たちです。
  造り手の言葉では『彼らがその果実に ownership を持つ』。醸造家は
  『実のところ、彼らはそれについてかなり競争的だ』と付け足しています。**」
- 🔴 **ボトルそのものの話**：「**このボトルは 1896 年の第一級ワインのボトルの復刻です。
  David は 1800 年代後半の手吹きボトルを何百本も並べてもらって一本に絞り、
  手の中の感触で決めました。ガラス職人が誰も複製できなかったので、
  病院で CAT スキャンにかけて密度の構造を明らかにし、最後はフランスの調香師が型を作りました。**」
- 🔴 **ラベルの話**：「**ラベルは Cronite の凹版印刷機で刷られています。
  かつて米国造幣局が紙幣を刷るのに使っていた機械です。手動、完全非電動、1 枚のラベルに 4 回通し、
  一度に刷るのは約 100 枚。図版は Bob Swartley という彫版師が畑に通って鉛筆で描き、
  鋼板に彫ったものです。彼は 2016 年に亡くなりました。**」
- **Cappella の来歴（OBP には無いが会話に効く）**：「**St. Helena で最も古い畑の一つで、初植栽は 1869 年。
  カトリック墓地の隣、わずか 6 エーカーです。1980 年代に教会の依頼で David 自身が古樹を抜き、
  約 20 年放置されるのを見ていた。再植の機会が来たとき飛びついたが、その最初の再植は台木が病気で失敗し、
  また抜くことになった。収穫を得るまで 6 年かかっています。**」
- 🔴 **2020 年の火災のあと**：「**Thorevilos の周りの森は 2020 年の山火事でほぼ焼けました。
  彼らは 1,000 本の樹を植え、一年以上手で水をやり、侵食防止に麦稈のベールとネットを敷き、
  焼け残ったオークとマドローネの地下の根株から出る芽を仕立てています。
  『いずれ公園のようになる。だが開けた形にしておく —— また火が来たとき、燃料を抱えていないように』。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している**）

1. 🔴 ⚠️ **「品種構成はカベルネ・ソーヴィニヨン ◯%、メルロ ◯% です」と言わない。**
   **醸造家 Brad Grimes が明確に否定している ——
   『われわれのワインを、この品種が何%という形で理解しようとしてもうまくいかない。
   一つ一つの発酵がすべて違うのだから、品種の比率は常に違う』。**
   **公式に品種比率の数字は一つも無い。**
2. 🔴 ⚠️ **「100% カベルネ・ソーヴィニヨンです」と言わない。**
   **生産者は自分のワインを一度も単一品種として呼んでおらず、公式の語は `Cabernet-driven blends`
   （カベルネ主体のブレンド）と `single-site Cabernet blends`（単一畑のカベルネ系ブレンド）である。**
   **リストの `Cabernet Sauvignon` はメニュー側の分類語であり、ラベル表記は本調査で確認できていない。**
3. 🔴 ⚠️ **`'Madrona,'` を「Saint Helena AVA の畑です」と断定しない。**
   **生産者は Madrona Ranch に AVA を一度も付しておらず、公式の言い方は
   「St. Helena の`町`の西縁」である（町の言及であって AVA の主張ではない）。**
   🏛 **さらに法定 AVA 名は `St. Helena` であって `Saint Helena` ではない**（27 CFR §9.149(a)）。
   **言うなら「St. Helena の町の西側にある畑」まで。**
4. 🔴 ⚠️ **逆に、`'Thorevilos,'` の `Napa Valley` を「大雑把な表記ですね」と言わない。**
   **これは造り手自身の判断である ——『Thorevilos はどの sub-appellation にも属さない。外れ者だ』。**
   **メニューが正しい。**
5. 🔴 ⚠️ **`2021` について造り手のヴィンテージ描写を語らない。**
   **公式サイトは全 6 ワインについて `2019 Vintage` としか書いておらず、2021 の記述は一行も無い。
   他の年の話を流用しないこと。**
6. 🔴 ⚠️ **テイスティングノートを「造り手によれば」と言って語らない。**
   **公式にテイスティングノートは 1 件も存在しない。**
   **言えるのは Brad Grimes の質的な言葉（Thorevilos＝`badlands`、Tilting Rock＝`無重力感`、
   Rothwell Hyde＝`Abreu の表現であって必ずしも単一畑ではない`）までである。**
7. 🔴 ⚠️ **「有機栽培」「ビオディナミ」「◯◯認証」と言わない。**
   **公式サイト全 24 ページに認証語が 1 件も無い（実測 0 ヒット）。**
   **言えるのは「畑ごとに通年の専属クルーがつく」「雑草の無い麦稈しか入れない」
   「火災後に 1,000 本を植えて手で水をやった」といった、生産者が実際に書いた作業の内容まで。**
8. ⚠️ **`Rothwell Hyde` / `Tilting Rock` を「セカンドワイン」と言わない。**
   **公式はこれらを格下として扱っておらず、`Rothwell Hyde` については
   「Abreu Vineyards を最もよく定義するワインかもしれない」と書いている。**
9. ⚠️ **アルコール度数・新樽比率・樽熟期間・生産本数（各ワイン別）を言わない。**
   **公式に一切の記載が無い。**
   **言えるのは「ロットを個別に樽で 1 年 → ブレンド確定後さらに 1 年」という手順と、
   「100 樽から 12,000 本」という全体の数字だけである。**
10. ⚠️ **`P.O. Box 89, Rutherford` を「ワイナリーの住所」「畑の所在地」と言わない。**
    **これは私書箱である。4 つの畑はいずれも Rutherford ではなく、
    St. Helena 周辺（Madrona Ranch / Cappella / Thorevilos）と Howell Mountain（Las Posadas）にある。**
11. ⚠️ **点数・評価を語らない。**
    **公式 `/about/roots` に批評家の引用が 3 か所あるが（Antonio Galloni 2014-12 ×2、
    Robert Parker / The Wine Advocate 2014-10 ×1）、いずれも点数ではなく、
    しかも 2014 年の言及であって OBP 掲載の 2019 / 2021 とは無関係である。**
    **本ドシエはこれらを事実の根拠に用いていない。**
12. ⚠️ **創業年・設立年を言わない。**
    **`30 Years` というページ名はあるが、そのページに年号が書かれていない。**
    **確実に言えるのは「最初の醸造が 1986 年（未発売）、最初に販売したのが 1987 年」だけである。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **新規の登録は行っていない。以下は escalation であり、実行していない。**

### ① 🔴 **これは conflict ではない —— canonical の `gap`（欠落）である**

1. **ID**
   - canonical 生産者: 🔴 **存在しない。**（衝突している ID が無い。）
   - OBP 行: `source_line_no 1216`–`1220`（5 行）
   - source_row_id: `7be8872fe2` / `3a2698f611` / `6b5f2f64f5` / `33560f82d0` / `d792fe681b`
2. **なぜ「重複に見えるか」ではなく「欠落か」**
   🔴 **`P-1`〜`P-7`（実体分裂・キー衝突）、`C-1`〜`C-5`（キュヴェ名の形）、`V-1`〜`V-4`（層のずれ）、
   `S-1`〜`S-4`（スキーマ）—— REGISTER のどのクラスも、
   「生産者が canonical に一件も存在しない」状態を扱っていない。**
   **これは重複でも分裂でも符号化破損でもなく、単純な未収録である。**
   🔴 **したがって本書は新しい conflict 番号を開かない。**
3. **証拠**
   - 🔍 **`migration/out/export/db_wine_canonical.json` の実測**: **928 レコード / distinct producer 383 件 /
     producer 値が空のレコード 0 件。**
   - 🔍 **`Abreu` / `abreu` / `breu` を含む producer: 0 件。**
     アルファベット順で `Abreu` が入る位置の隣接は `A. Bergère`（前）と `Adrien Renoir` / `Agrapart & Fils` /
     `Alain Burguet` / `Alban Vineyards`（後）。
   - 🔍 **畑名・キュヴェ名の全文検索**: `Madrona` 0 件 / `Thorevilos` 0 件 / `Posadas` 0 件 /
     `Cappella` 0 件 / `Rothwell` 0 件 / `Tilting` 0 件。**別名で紛れ込んでいる可能性も無い。**
   - 🔍 **`research/out/t-01/mapping.json` および `review.json` にも `Abreu` は 1 件も現れない**
     （＝ matcher が候補すら立てていない）。
   - ⚠️ **オーケストレータの記録は「canonical 384 生産者」だが、本調査の実測は 383 である。**
     **1 件の差の原因は特定していない（数え方の差の可能性が高い）。この差は本件の結論に影響しない。**
4. **OBP への影響**
   🔴 **5 行 —— 合計 $12,930 相当 —— が丸ごと `unresolved` のまま。**
   **canonical に生産者が無いため、キュヴェ 6 本も当然すべて存在しない。**
   **ソムリエ画面はこの生産者について何も出せない。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - **新規 producer レコード `abreu-vineyards`（`producer = 'Abreu Vineyards'`）を立てる。**
     **`Abreu` は menu-printed alias として保持する。**
   - **`country = 'United States'` / `region = 'Napa Valley'`。**
     🔴 **`subregion` は畑ごとに異なるため producer 単位で固定しない**
     （Las Posadas＝`Napa Valley — Howell Mountain`、Madrona Ranch と Cappella＝`Napa Valley — St. Helena`（未確認）、
     Thorevilos＝`Napa Valley`（sub-appellation 無し、生産者明言））。
     🔍 **canonical の既存表記は `Napa Valley — Howell Mountain` / `Napa Valley — St. Helena` であり、
     この形に揃うのが自然。**
   - **キュヴェは 6 本を対等に登録する** ——
     `Thorevilos` / `Cappella` / `Las Posadas Howell Mountain` / `Madrona Ranch` / `Rothwell Hyde` / `Tilting Rock`。
     **OBP に無い 3 本（Cappella / Rothwell Hyde / Tilting Rock）も、公式が対等に扱っているため省かない。**
   - 🔴 **`grapes` は空のままにする。**
     **生産者が「品種比率は常に違う」と明示的に書いているため、固定値を入れるのは不適切である。**
6. **Confidence**: 🔴 **High**（欠落の事実は DB の実測で確定。推奨名の根拠は公式サイトの自称表記そのもの）。
   ⚠️ **ただし `subregion` の St. Helena 部分だけは Low**（§③ 参照）。

### ② 🔴 メニュー印字と公式名の乖離 —— **登録時にどちらを canonical 名にするか**

1. **ID**
   - canonical キュヴェ: **存在しない**（①のため）
   - OBP 行: `1216` `1217`（`Las Posadas`）／`1218` `1219`（`Madrona`）
2. **なぜ問題か**
   🔴 **OBP の `product_name` は `Las Posadas` と `Madrona` だが、公式の正式表記は
   `Las Posadas Howell Mountain` と `Madrona Ranch` である。**
   **前者は産地名をキュヴェ名に含み、後者は `Ranch` を含む。**
   **短縮形をそのまま canonical キュヴェ名として登録すると、公式表記との突き合わせが将来できなくなる。**
   ⚠️ **既存の `C-4`（識別語なしキュヴェ名）とは異なる** —— `Las Posadas` も `Madrona` も
   固有名として十分に識別的であり、スタイル語のみの名前ではない。**新番号は開かない。**
3. **証拠**
   ✅ **`abreuvineyards.com/wines` の一覧が 6 ワインを
   `Thorevilos` / `Cappella` / `Las Posadas Howell Mountain` / `Madrona Ranch` / `Rothwell Hyde` / `Tilting Rock`
   と表記している。**（各ワインの個別ページのフッターにも同じ 6 件の一覧が繰り返される。）
   ✅ **`Madrona Ranch` は本文でも一貫して `Madrona Ranch` と書かれる**（`/wines/madrona`、`/stories/legacy`、
   `/stories/blending`、`/about/30-years` のすべて）。
4. **OBP への影響**
   **4 行（$2,640 ×1・$2,505 ×1 ×2 組）。**
   **短縮形のまま登録すると、公式ソースやインポーター資料との将来の突き合わせで一致しない。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - **canonical キュヴェ名は公式表記（`Las Posadas Howell Mountain` / `Madrona Ranch`）を採り、
     OBP の印字（`Las Posadas` / `Madrona`）は menu-printed alias として保持する。**
   - 🔴 **`Las Posadas Howell Mountain` については、`Howell Mountain` が
     `キュヴェ名の一部`であると同時に `AVA 表示`でもあるという二重性を注記する。**
     **canonical の `subregion` にも `Napa Valley — Howell Mountain` を入れてよいが、
     キュヴェ名からは削らない。**
6. **Confidence**: 🔴 **High**（公式一覧の表記そのもの）

### ③ ⚠️ `Saint Helena` —— **表記と、産地主張そのものの二重の未確認**

1. **ID**
   - OBP 行: `1218` `1219`（`'Madrona,' Saint Helena Cabernet Sauvignon`）
   - `classification_text` = `"Saint Helena Cabernet Sauvignon"`
2. **なぜ問題か**
   - 🔴 🏛 **法定 AVA 名は `St. Helena` であって `Saint Helena` ではない**（27 CFR §9.149(a)：
     「the name of the viticultural area described in this section is `St. Helena`」）。
     🔍 **canonical の既存表記も `Napa Valley — St. Helena` である**（`corison-st-helena`、
     `spottswoode-estate`、`hundred-acre-kayli-morgan` ほか）。**綴りが揃わない。**
   - 🔴 ⚠️ **より重い問題は表記ではなく、産地主張そのものが未確認であること。**
     **生産者は Madrona Ranch に AVA を一度も付していない。**
     🏛 **§9.149 は St. Helena AVA の西側境界を 500 フィート／400 フィート等高線で定義しており、
     「町の西縁」の畑がその内側か外側かは、標高が公表されていない以上、判定できない。**
3. **証拠**
   - 🏛 **27 CFR §9.149(a) および (c)(3)(4)(6)(7)（500 ft / 400 ft 等高線）**
   - ✅ **`abreuvineyards.com/wines/rothwell`：「Madrona Ranch と Cappella は
     `the western edge of the town of St. Helena` に漂う site」** —— **`town`（町）であり `AVA` ではない**
   - ✅ **`/wines/madrona` は AVA に一切言及しない**
   - ❌ 🏛 **TTB COLA が CAPTCHA で取得できず、ラベルの表示産地は未確認**
4. **OBP への影響**
   **2 行（$2,640 / $2,505）。**
   **`Saint Helena` をそのまま `appellation` として書き込むと、綴りが法定名と異なるうえ、
   生産者の裏づけの無い産地主張を画面に出すことになる。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - **綴りは `St. Helena` に正規化し、`Saint Helena` は menu-printed alias とする。**
   - 🔴 **ただし `appellation` フィールドへの書き込みは保留する。**
     **TTB COLA でラベルを確認するか、生産者が公式に AVA を明示するまで、
     `subregion` は `Napa Valley`（上位）にとどめるのが安全である。**
   - **Cappella も同じ扱い**（OBP には無いが、公式は同じく「St. Helena の町の西側」としか書いていない）。
6. **Confidence**: **綴りの正規化 = High ／ 産地主張の当否 = 🔴 Low**（COLA 未取得）

### ④ 🔴 `Cabernet Sauvignon` —— **品種表示がメニュー側の分類語である可能性**

1. **ID**
   - OBP 行: `1216`–`1220`（5 行すべて）
   - `classification_text` の末尾が全行 `Cabernet Sauvignon`
2. **なぜ問題か**
   🔴 **生産者は 7 つのワインページのどこでも `Cabernet` の語を使っていない。**
   **公式の自己記述は `Cabernet-driven blends` および `single-site Cabernet blends` であり、
   いずれも `blend`（ブレンド）である。**
   **醸造家は品種比率での理解を明示的に否定している。**
   🏛 **27 CFR §4.23(b) により、`Cabernet Sauvignon` を type designation としてラベルに使うには
   その品種由来が 75% 以上でなければならない。**
   **生産者が「比率は常に違う」と言っている以上、この 75% 要件を毎年満たしているかは自明でない。**
   🔴 **すなわちラベルの type designation は `Cabernet Sauvignon` ではなく
   `Red Wine` / `Napa Valley Red Wine` などである可能性がある。**
   **これは Batch 9 の Harlan（`Proprietary Blend` はキュヴェ名ではない）、
   Batch 7 の Mayacamas（`Mount Veeder Proprietary Blend` → 実名 `Red Wine`）と同型の構造である。**
3. **証拠**
   - ✅ **`/wines/*` 7 頁に `Cabernet` の出現 0 件**（実測）
   - ✅ **`meta name="description"`：`Cabernet-driven blends …`**
   - ✅ **`/about/roots`：`12,000 bottles of single-site Cabernet blends`**
   - ✅ **`/stories/cofermentation`（Brad Grimes）：「品種が何%という形で理解しようとしてもうまくいかない…
     品種の比率は常に違うことになる」**
   - 🏛 **27 CFR §4.23(b)（75% 規則）**
   - ❌ 🏛 **TTB COLA 未取得 —— ラベルの type designation は未確認**
4. **OBP への影響**
   🔴 **5 行すべて。**
   **canonical の `type` / `grapes` に `Cabernet Sauvignon` を書き込むと、
   生産者が明示的に否定している表現を DB に固定することになる。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - 🔴 **`grapes` は空のままにする。**（生産者の明言により、固定値は不適切。）
   - **`Cabernet Sauvignon` は menu-printed classification として `classification_text` のまま保持し、
     canonical の品種フィールドへは昇格させない。**
   - **ラベルの type designation は 🏛 TTB COLA または実ボトルで確認してから決める。** → Open Questions 2 / 5
6. **Confidence**: **「生産者が単一品種として名乗っていない」= 🔴 High ／
   「ラベルが実際に何と書いているか」= 🔴 Unknown**

### ⑤ 既存の系に属するもの —— **新しい番号を開かない**

| 事象 | 扱い |
|---|---|
| **producer heading `Abreu` ↔ 公式 `Abreu Vineyards`** | 🔍 **メニュー側の短縮形。**①の解決（alias 保持）に含めれば足りる。**新番号は開かない。** |
| 🔴 **`vintage='—'`（em-dash sentinel）** | 🔍 **Batch 9 の実測で DB 全体 328 レコードに及ぶ systemic な形であることが既に判明している。**`abreu-vineyards` にはまだレコードが無いため該当しない。**新規登録時に同じ形を再生産しないこと。** |
| **`color=Rouge`（仏語の色名が米国産赤に付く）** | 🔍 **既存 Napa 生産者に見られる語彙の不統一。**⚠️ **本書では観察の記録にとどめ、新番号を開かない。** |

---

## Sources

**一次資料 —— 生産者の公式サイトと、規制の一次資料（eCFR）のみ。
retailer / critic / auction / blog / Wikipedia は事実の根拠に一切使用していない。**

### 🔴 サイト真正性の事前確認（**どうやって確かめたか**）

| 判定 | サイト | 確認方法 |
|---|---|---|
| ✅ **真正** | 🔴 **`http://abreuvineyards.com/`** | **(a) 一貫した法的フッター** —— 取得した全 24 ページのフッターに同一の実住所 `P.O. Box 89, Rutherford, CA 94573`、電話 `707-963-3465`、`info@abreuvineyards.com` が入る。<br>**(b) 自前の会員基盤** —— `acquire.abreuvineyards.com/shopping3/account/shopping_login.cfm`（会員ログイン）と `acquire.abreuvineyards.com/mailinglist/`（waitlist 登録）が同一ドメイン配下に存在し、実際に稼働するフォーム（州ドロップダウン・請求先情報）を持つ。**パーキングページや汎用テンプレートではない。**<br>**(c) 制作者の明示** —— `/credits` が 4 者（Alta / Matt Morris / Lab 43 / Mora Cronin）を実名で挙げ、それぞれの独立したサイトが `Abreu` を顧客として掲げている。<br>**(d) 内容の固有性** —— 石工・彫版師・麦稈供給者・料理番の実名と個人史を含む 13 本の長文が、他所から複製できない一人称で書かれている。 |
| 📄 **第三者（傍証のみ・事実の根拠には未使用）** | **`http://www.alta.co`（Alta Creative）** | `/credits` が `Brand strategy, creative direction & design` として名指し。**制作者側のサイトであって生産者の publication ではない。** |
| 📄 **第三者（同上）** | **`http://www.mattmorrisphotos.com`（MATT MORRIS）** | `/credits` が `Photography` として名指し。 |
| 📄 **第三者（同上）** | **`Lab 43`（`lab43.html`。`<title>Lab 43 \| Web Design and Development`）** | `/credits` が `Development` として名指し。 |
| ❌ **取得不能** | 🏛 **`TTB COLA Public Registry`（`ttbonline.gov/colasonline/`）** | 🔴 **bot 対策のチャレンジが返り、画像 CAPTCHA を要求された。**（`This question is for testing whether you are a human visitor and to prevent automated spam submission.` / `What code is in the image?` / `Your support ID is: 5964387807068716666.`）<br>🔴 **方針によりこれを回避していない。代替として小売・オークションのラベル画像で置き換えることもしていない。**<br>**したがってラベル情報は「未確認」として記録する。** |
| ❌ **取得不能** | 🏛 **`California Secretary of State` 事業体検索** | 🔴 **Imperva / Incapsula にブロックされた。**（`Request unsuccessful. Incapsula incident ID: 358000930005291589-11440774992762698`）**法人格は未確認。** |

### ✅ 取得した公式資料（`abreuvineyards.com`。**全 24 ページ**）

| 資料 | 取得した情報 |
|---|---|
| ✅ **`/`（home）** | 🔴 **`<title>Abreu Vineyards`・`og:description`「Abreu Vineyards. Passion beyond reason.」・`meta description`「Cabernet-driven blends from the meticulous properties of famed vineyard manager, David Abreu.」**・フッターの実住所と連絡先・8 本のストーリー導入文 |
| ✅ **`/about`** | **About の 5 節構成（30 Years / Winegrowing / Winemaking / People / Roots）** |
| 🔴 **`/about/roots`** | 🔴 **本ドシエ §Overview の骨格。**David の出自（牧場主の家系）・4 つの畑の名前・「100 樽 → 12,000 本の single-site Cabernet blends」・Brad Grimes＝`a chef turned winemaker`。⚠️ **末尾に批評家の引用 3 件**（Galloni 2014-12 ×2、Parker/TWA 2014-10 ×1。**本書では事実の根拠に用いていない**） |
| 🔴 **`/about/30-years`** | 🔴 **本ドシエ §History の骨格。**1986 最初の醸造（未発売）・1987 初販売・Madrona Ranch の 1986/1988/1990/1998 の declassify・Laurie Wood と Chuck Carpy・ボルドー訪問の姿勢・2000 年 Stuart Sloan の施設での選果論争 |
| ✅ **`/about/winegrowing`** | 🔴 **畑ごとの通年専属クルー。**剪定・枝配置・間引き・未熟粒の摘除・収穫・選果台までを同一チームが担う |
| ✅ **`/about/winemaking`** | 🔴 **共発酵の起源（タンク 2 つ）。**1980 年代に使われた 4 品種の名（CS / CF / Merlot / PV） |
| ✅ **`/about/people`** | **David Abreu の一人称「私はチームなしでは何者でもない…われわれは決して `no más` と言わない」** |
| 🔴 **`/wines`** | 🔴 **本ドシエで最も重要な 1 ページ。公式の 6 ワインの正式表記** —— `Thorevilos` / `Cappella` / `Las Posadas Howell Mountain` / `Madrona Ranch` / `Rothwell Hyde` / `Tilting Rock` |
| 🔴 **`/wines/thorevilos`** | 🔴 **「Thorevilos はどの sub-appellation にも属さない。外れ者だ」（David Abreu）・St. Helena と Howell Mountain AVA の間・200 エーカーから 40 vine acres・Boomer / Forward series 土壌・北向きの畝・mid-mountain climate・2020 年山火事と復元作業・Brad Grimes の `badlands` 発言・`2019 Vintage`** |
| 🔴 **`/wines/madrona`** | 🔴 **Madrona Ranch＝「Abreu の核」・1980 年代に最初に開発・赤い Aiken／白い tufa／暗色の粘土と岩・数週間にわたる摘み・現役の ranch（牛・山羊・豚・鶏・蜜蜂）・`2019 Vintage`** |
| 🔴 **`/wines/howell`（Las Posadas）** | 🔴 **2000 年取得・一世紀以上前の first growth redwood 支柱・標高約 2,000 ft・霧の層より上・モミと松の保護林・赤い Aiken が白い tufa の上に層をなす・岩を石壁に転用・`2019 Vintage`** |
| ✅ **`/wines/cappella`** | **St. Helena 最古級・6 エーカー・カトリック墓地の隣・初植栽 1869 年・1980 年代の抜根と約 20 年の休閑・病気台木による再度の抜根・収穫まで 6 年・`2019 Vintage`** |
| 🔴 **`/wines/rothwell`（Rothwell Hyde）** | 🔴 **Madrona Ranch ＋ Cappella のブレンド・「Abreu Vineyards を最もよく定義するワインかもしれない」・2 畑は 1/4 マイルしか離れていない・David は両者の中間に住む・St. Helena 西側の歴史（クルミとプルーンの果樹園 → 住宅地）・Brad Grimes の「Rothwell Hyde は Abreu の表現であって必ずしも単一畑ではない」・`2019 Vintage`** |
| 🔴 **`/wines/tilting-rock`** | 🔴 **Thorevilos ＋ Las Posadas のブレンド・「標高が大きく異なる St. Helena 東斜面の 2 畑」・`mountain wine` と呼ぶことへの拒否・Brad Grimes の「錬金術」「無重力感」・Tilting Rock は Thorevilos の最奥、Howell Mountain Road の下にある実在のランドマーク・`2019 Vintage`** |
| ✅ **`/stories`・`/stories-2`** | **全 13 本のストーリーの一覧**（Cofermentation / Blending / Extra Virgin Olive Oil / Blackberries / Saturday Thanksgiving / Purple Juice / Wheat Straw / The Bottle / Legacy / La Parrilla / Master Engraver / The Stonemason / Labelling） |
| 🔴 **`/stories/cofermentation`** | 🔴 **§Winemaking の中核。**David の coq au vin の比喩・「品種ではなく site を語るワイン」・Brad Grimes の摘み方・**品種比率での理解への明示的な否定** |
| 🔴 **`/stories/blending`** | 🔴 **ブレンド 6 段階の唯一の公式手順。**個別樽 1 年 → ブレンド試験 → core blend（2〜3 発酵）→ 再結合してさらに 1 年 → 瓶詰め。**2000 年 Thorevilos 初収穫、2006 年に 4 畑すべて** |
| 🔴 **`/stories/legacy`** | 🔴 **Las Posadas の取得（2000 年、Cold Springs Road の競売）・のちに丘の上の区画・15 年かけた開発・1800 年代の畑の痕跡（Krug / Keyes / Hastings）** |
| 🔴 **`/stories/the-bottle`（`p_stories_bottle.html`）** | 🔴 **1896 年 first-growth ボトルの復刻・Marin Wine Cellar・CAT スキャン・フランスの調香師が型を作った** |
| 🔴 **`/stories/labelling`** | 🔴 **Cronite intaglio press・米国造幣局・4 回通し・手動非電動・一度に約 100 枚** |
| 🔴 **`/stories/master-engraver`（`p_stories_engraver.html`）** | 🔴 **Bob Swartley の経歴と 2016-07-23 の逝去・Griffin & Howe / Josef Fugger・Cronite の鋼板** |
| ✅ **`/stories/the-stonemason`（`p_stories_mason.html`）** | **Jesus Salcedo・Michoacán・1998 年から・石灰岩・目地の見えない積み方・常に一人** |
| ✅ **`/stories/wheat-straw`** | **Jake Wheeler・Sacramento Valley の小麦農家・雑草の無い麦稈・自分で検分して刈り梱包する** |
| ✅ **`/stories/purple-juice`** | **Newton での Cabernet Franc との出会い・Madrona Ranch への植栽・「ブレンドを別の次元へ引き上げる」** |
| ✅ **`/stories/la-parrilla`（`p_stories_parrilla.html`）** | **Jorge / Francisco Delgado 兄弟・収穫期の毎日の食事・Las Posadas での Thanksgiving、Madrona Ranch での誕生日** |
| ✅ **`/credits`** | **Alta / Matt Morris / Lab 43 / Mora Cronin** |
| ✅ **`acquire.abreuvineyards.com/mailinglist/`** | **members list は満員・waitlist 制・優先順位は登録日順・国際発送は `IT International`** |

⚠️ **キャッシュ内で 404 を返した URL 2 件** —— `/wines/las-posadas` と `/wines/howell-mountain`。
**いずれも「推測した URL」であり、正しい実体は `/wines/howell` である。**
**この 2 件は本書の根拠に用いていない。**

### 🏛 ［規制一次資料］

| 資料 | 取得した情報 |
|---|---|
| 🏛 **27 CFR § 9.23 `Napa Valley`** | **AVA の法定名と境界（Napa 郡界に沿う）。**［T.D. ATF-79, 46 FR 9063, 1981-01-28；T.D. ATF-201, 50 FR 12533, 1985-03-29］ |
| 🔴 🏛 **27 CFR § 9.94 `Howell Mountain`** | 🔴 **「Napa County に所在し、`Napa Valley viticultural area の一部である`」と明文。境界は全周 `1,400 フィート等高線`。**［T.D. ATF-163, 48 FR 57487, 1983-12-30；T.D. ATF-249, 52 FR 5960, 1987-02-27］ |
| 🔴 🏛 **27 CFR § 9.149 `St. Helena`** | 🔴 **法定名は `St. Helena`（`Saint Helena` ではない）。境界に `500 ft` / `400 ft` / `380 ft` の等高線と St. Helena 市境、Howell Mountain Road、Conn Valley Road を含む。** |
| 🏛 **27 CFR § 4.25(e)** | **AVA 表示の 85% 規則。重複 AVA の 85% 規則。**［T.D. ATF-53, 43 FR 37675, 1978-08-23］ |
| 🏛 **27 CFR § 4.27(a)(1)** | **AVA 表示のヴィンテージワインは 95% が表示年の収穫。** |
| 🔴 🏛 **27 CFR § 4.23(b)** | 🔴 **単一品種名を type designation に使うには 75% 以上。**→ §Canonical Conflict ④ |
| 🏛 **27 CFR § 4.26** | **`Estate bottled` の 3 条件（AVA 表示・ワイナリーが AVA 内・自社所有／管理地で全量栽培・連続工程）。** |

**取得できなかったもの / 存在しなかったもの**
- 🔴 **`2021` のヴィンテージ記述** —— 公式サイトは全 6 ワインについて `2019 Vintage` としか書いていない。
- 🔴 **テイスティングノート** —— **どのワインについても 1 件も存在しない。**
- 🔴 **セパージュ・アルコール度数・新樽比率・樽のメーカー・生産本数の内訳** —— 公式に一切無い。
- 🔴 **各畑の面積・標高・植栽密度・台木・クローン・樹齢** —— Thorevilos の 40 vine acres、
  Cappella の 6 エーカー、Las Posadas の「約 2,000 フィート」以外は無い。
- 🔴 **法人格（LLC / Inc.）と bonded winery 名** —— 公式サイトに表示が無く、🏛 CA SoS が取得できなかった。
- 🔴 **ラベルの brand name / type designation / 表示産地** —— 🏛 TTB COLA が CAPTCHA で取得できなかった。
- ⚠️ **`/members`（会員ページ）はログインが要る。**本調査では未取得。
- ⚠️ **`robots.txt` / `sitemap.xml` はキャッシュに含まれていない。**
  **本書の 24 ページはナビゲーションからの網羅であり、サイトマップによる全数確認ではない。**
  **未取得のページが残っている可能性は排除できない。**
- ⚠️ **`/stories/extra-virgin-olive-oil`・`/stories/blackberries`・`/stories/saturday-thanksgiving`**
  —— **一覧には存在するが、本文ページはキャッシュに無い。**導入文のみを用いた。

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔴 **canonical 生産者レコード `0` 件 ／ canonical キュヴェ `0` 件 ／
OBP 5 本（`producer_state = unresolved`、セクション `UNITED STATES | RED > NAPA`、
`section_start_page = 25`、`source_line_no 1216`–`1220`、producer heading は `Abreu`、
`layout = producer_heading`、`flags = []`）。**
🔍 **参照した DB ファイル: `migration/out/export/db_wine_canonical.json`（928 レコード）、
`research/out/t-01/inventory.json`、`research/out/t-01/mapping.json`、`research/out/t-01/review.json`、
`research/canonical_conflicts/REGISTER.md`。いずれも読み取りのみ。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | **公式名 `Abreu Vineyards`・創業者・醸造家・実住所・連絡先・タグライン・自己記述がすべて公式で確定。**⚠️ **法人格のみ未確認**（CA SoS ブロック） |
| **Overview** | **High** | **公式の自己記述の全文・生産量（100 樽 → 12,000 本）・哲学の一次引用が取れた** |
| **History** | **Medium** | 🔴 **1986 / 1987 / 2000 / 2006 / 2016 / 2020 という節目は一人称で確定。**⚠️ **創業年・法人設立年・各畑の取得年（Las Posadas 以外）・植栽年が公式に無い** |
| 🔴 **Location** | 🔴 **High** | 🔴 **4 畑すべてに固有の公式記述があり、土壌名（Aiken / tufa / Boomer / Forward）まで出ている。**🏛 **3 つの AVA を規制一次資料で照合し、メニューの 3 表記の当否を個別に判定できた。**⚠️ **面積・標高の数字は大半が欠ける。Madrona の AVA は未確認** |
| **Farming** | **Medium-High** | 🔴 **「畑ごとの通年専属クルー」という構造と、火災後の森林復元の具体作業が公式で厚い。**🔴 **認証の自称ゼロを実測で確定。**⚠️ **収量・栽培資材・灌漑・カバークロップの数字はゼロ。**⚠️ **認証レジストリの照会は未実施** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **共発酵の起源・摘み方・ブレンド 6 段階の手順・樽での 1 年 ＋ 1 年・ボトルとラベルの製法が、すべて醸造家の一人称で取れた。**⚠️ **分析値・新樽比率・酵母は皆無** |
| **Style** | 🔴 ⚠️ **Low** | 🔴 **公式にテイスティングノートが 1 件も存在しない。**使えるのは Brad Grimes の質的な言葉のみ。**OBP 5 本のいずれについても、造り手の味の描写は無い** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **公式サイトが 6 ワインすべてに専用ページを持ち、OBP の 3 キュヴェすべてについて正式表記を確定できた。**⚠️ **ヴィンテージは 2019 のみ確認、2021 は未確認** |
| **Staff Notes** | **High** | ⚠️ **12 項目。**🔴 **「品種比率」「単一品種」「Saint Helena＝AVA」「2021 のヴィンテージ描写」「有機栽培」「セカンドワイン」という 6 つの誤りを塞いだ** |
| 🔴 **総合** | 🔴 **High — staff-usable（70% を明確に超過。到達度およそ 82%）。** | **必須 7 項目すべてを満たす。**Identity ✅／Overview ✅／Location ✅（AVA 照合込み）／Farming ✅／**Important Cuvées（OBP 5 本すべての正式名を確定 ＋ 公式 6 ワインの全数）✅**／Staff Notes 芯 3 点 ✅／⚠️ Must-Not-Say 12 項目 ✅。<br>**欠けているのは ① 2021 のヴィンテージ記述、② テイスティングノート（公式に存在しない）、③ ラベル由来の情報（TTB COLA が CAPTCHA）、④ 法人格（CA SoS がブロック）、⑤ 栽培・醸造の数値。**<br>🔴 **①②は生産者が公開していない。③④は別経路が要る。** |

**reached_70: YES.**（**約 82%**）

---

## Open Questions

1. 🔴 **OBP 掲載の `2021` に対応する公式記述が一切存在しない。**
   **公式サイトは全 6 ワインについて `<h4>2019 Vintage</h4>` という見出しを置くだけで、
   本文もリンクも PDF も無い。**
   **OBP の 5 行のうち 3 行（$2,640 ×3）が 2021 である。**
   ⚠️ **サイトは 2020 年の山火事に言及しているため 2020 年以降に更新されているが、
   それでも現行表示が 2019 である。単にサイトが古いだけの可能性が高い。**
   🔴 **ただし本書はこれを推測として扱い、2021 の存在をソムリエに保証しない。**
   → **会員ページ（`acquire.abreuvineyards.com` のログイン後）、インポーターのリリース案内、
     または実ボトルが要る。**

2. 🔴 🏛 **TTB COLA 公開レジストリが取得できていない。**
   **`ttbonline.gov/colasonline/` が bot 対策のチャレンジを返し、画像 CAPTCHA を要求した
   （`What code is in the image?` / support ID `5964387807068716666`）。方針によりこれを回避していない。**
   **結果として、ラベル上の brand name（`ABREU` か `ABREU VINEYARDS` か）、
   type designation（`Cabernet Sauvignon` か `Red Wine` か）、表示産地
   （Madrona は `St. Helena` か `Napa Valley` か）、アルコール度数、`Estate Bottled` 表記、
   bottler 名がすべて未確認である。**
   🔴 **これが埋まれば §Canonical Conflict ②③④ の 3 件が同時に解決する。**
   → **別の経路（ブラウザ描画での手動確認）が要る。**

3. 🔴 🏛 **法人格が未確認。**
   **California Secretary of State の事業体検索が Imperva/Incapsula にブロックされた
   （incident ID `358000930005291589-11440774992762698`）。**
   **公式サイトにも `LLC` / `Inc.` の表示が無い。**
   ❓ **`Abreu Vineyards` が法人名なのか、ブランド名なのかが確定していない。**
   → **別の経路での 🏛 レジストリ照会が要る。**

4. ⚠️ 🏛 **認証の「不在」が証明されていない。**
   🔴 **確定したのは「生産者が認証を一切自称していない」ことだけである**（公式 24 ページで認証語 0 ヒット）。
   ❓ **CCOF・Demeter USA・Napa Green / Napa County の各レジストリは本調査で照会していない。**
   → **これらを照会して初めて「認証を保持していない」と言える。**
     **Batch 8 の基準（proved absence は findings、assumed absence は findings ではない）に従い、
     本書は proved absence を主張しない。**

5. 🔴 📦 **【実ボトルが要る】ラベルの表記そのもの。**
   **以下は公式サイトでも規制文書でも解決できず、`物理的にボトルを見る`以外に確定手段が無い。**
   - ❓ **ラベルのブランド表記は `ABREU` か `ABREU VINEYARDS` か。**
   - ❓ **キュヴェ名は `LAS POSADAS` か `LAS POSADAS HOWELL MOUNTAIN` か。`MADRONA` か `MADRONA RANCH` か。**
   - ❓ **type designation は `Cabernet Sauvignon` か、それとも `Red Wine` などか。**
   - ❓ **Madrona Ranch の表示産地は `St. Helena` か `Napa Valley` か。**
   - ❓ **アルコール度数と、`Estate Bottled` 表記の有無。**
   → 🔴 **フロア・タスク**: **在庫の Abreu を 1 本、ラベル正面と裏を撮影する（2019 と 2021 の両方）。**
     **これで Open Questions 2 と §Canonical Conflict ②③④ が一度に解決する。**

6. ⚠️ **公式サイトの網羅性が保証されていない。**
   **`robots.txt` / `sitemap.xml` を取得していないため、本書の 24 ページはナビゲーション経由の網羅にとどまる。**
   ⚠️ **`/stories/extra-virgin-olive-oil`・`/stories/blackberries`・`/stories/saturday-thanksgiving`
   の 3 本は一覧に存在するが本文が未取得である。**
   → **サイトマップを取れば、未取得ページの有無が確定する。**

7. ⚠️ **`100 barrels → 12,000 bottles` がどの単位の数字か不明。**
   **年間総量なのか、1 ワインあたりなのか、ある年の実績なのかが公式に書かれていない。**
   🔍 **算術的には「約 30,000 本相当から 12,000 本を選ぶ」と読めるが、生産者はそう書いていない。**
   → **ソムリエ向けには「100 樽を 12,000 本に削り出す、と造り手が言っている」という引用の形でのみ使うこと。**

8. ⚠️ **Madrona Ranch と Cappella の標高が不明で、St. Helena AVA の境界内かを判定できない。**
   🏛 **§9.149 は西側境界を 500 フィート／400 フィート等高線で定める。**
   **生産者は両畑を「St. Helena の`町`の西縁」としか書いていない。**
   → **Open Questions 2 または 5 が解ければ、ラベルの表示産地から逆に確定する。**

9. ⚠️ **`Rothwell Hyde` という名の由来が公式に説明されていない。**
   **`Tilting Rock` は地元のランドマーク名だと明記されているが、`Rothwell Hyde` は
   Madrona Ranch ＋ Cappella のブレンドであること以外、名の来歴が書かれていない。**
   🔍 **St. Helena 西側の地名または通り名である可能性があるが、本書は推測しない。**

10. ⚠️ **canonical の生産者数が 383（本調査の実測）か 384（オーケストレータの記録）か。**
    🔍 **`db_wine_canonical.json` の 928 レコードから distinct な `producer` 値を数えると 383 件で、
    空値は 0 件だった。**
    **1 件の差の原因は特定していない。本件（`Abreu` の完全な不在）の結論には影響しない。**
    → **数え方の定義を揃える必要がある場合は、S 系（スキーマ）の課題として別途扱う。**
