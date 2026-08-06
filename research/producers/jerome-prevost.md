# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:jerome-prevost` および配下の cuvée / vintage レコードは**一切変更していない**。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagnelacloserie.fr で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では事実の根拠として一切使っていない**）／ `⚠️` 食い違い。両方を残す
> `🔍` THÉSEUS DB / OBP intake / 公式値からの機械的導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 一次資料: `https://champagnelacloserie.fr/`（FR 原文）と `https://champagnelacloserie.fr/en/`（EN 訳）
> **公式サイトは 1 ページ完結。** セクション 10 個 = `La pierre` `Les vaisseaux` `L'intime` `La peau` `La parcelle` `Underground` `Les Béguines` `Fac similé` `Le vigneron` `Les clefs`。**全 10 セクションを FR / EN 両方で取得済み**（`_sources/jerome-prevost/home_fr.txt` `home_en.txt`）。
>
> 🔴 **本書の 4 つの前提**
> 1. ⚠️ **公式サイトは «Réalisation octobre 2016»（2016 年 10 月制作）と自ら明記しており、以後の更新形跡が無い。** ニュース欄・プレス欄・更新日欄が存在しない。**したがって公式記述はすべて「2016 年時点」であり、「現在」として語れない。**
> 2. ⚠️ **キュヴェ別テクニカルシート PDF は存在しない。** HTML 全文を走査したが `.pdf` 参照はゼロ（外部リンクは EN 版と Google Fonts の 2 本のみ）。Louis Latour で使えた `/pdf/en/*.pdf` 方式は無い。**ただしその代わり、`Les Béguines` / `Fac similé` の 2 セクション自体がテクニカルシート相当の密度**（地質・台木・植樹年・密度・樽容量・ドザージュまで）を持つ。
> 3. 🔴 **公式に存在するキュヴェは 2 つだけ**（`La Closerie Les Béguines` と `Fac Similé`）。**OBP 掲載 5 本のうち 4 本は、この 2 つに公式上マッピングできない。** §Important Cuvées と §Staff Notes を必ず読むこと。
> 4. 🔴🆕 **canonical に「公式と矛盾する記述」が入っている。** cuvée `cuvee:jerome-prevost-la-closerie-les-beguines-extra-brut` の facts は **品種 100% ムニエ / 2 区画のブレンド / Blanc de Noirs** となっており、**公式（94+2+2%・単一区画）と正面から食い違う。** → **§Canonical Conflict PV-1 が本書で最も重要。** staff が現行 DB をそのまま読むと**誤ったことを言う。**

---

## Identity

| | |
|---|---|
| **Canonical Name** | Jérôme Prévost |
| **ラベル上のブランド名** | **Champagne La Closerie** ✅（ボトルの主表記は生産者名ではなく **La Closerie**） |
| **公式の名義** | **«Champagne La Closerie — Agnès et Jérôme Prévost»** ✅（**Agnès と連名**が公式表記） |
| **Aliases** | ❓ canonical `aliases` は **空配列**。実務上の別名は「La Closerie」「Jérôme Prévost」「Prévost」「LC」 |
| **業態** | 単一区画・自家栽培自家醸造の極小生産者（RM 相当）。**公式に CIVC 区分の記載は無し** ❓ |
| **所在** | **65 rue des Dames de France, 51390 Gueux** ✅ |
| **連絡先** | Tel (33) 03 26 03 48 60 ／ champagnelacloserie@orange.fr ✅ |
| **見学** | **メール予約制のみ。**①販売可能な在庫が残っていること ②**葡萄の生育最盛期（période de pousse active）を外れていること** ③蔵側に時間があること、の 3 条件付き。**収穫期は不可。** ✅ |
| **販売** | 個人・業者とも **メールでのアロカシオン制**（«proposition d'allocation»）。個人はプロプリエテでの購入かフランス本土への発送のみ ✅ |
| **ラベル** | **図案・表ラベル文・裏ラベル文すべて Jérôme Prévost 本人の作** ✅（«Graphisme, texte étiquettes et contre étiquettes : Jérôme Prévost»） |
| canonical id | `producer:jerome-prevost` |
| canonical legacy_ids | `prevost-la-closerie-2021` / `-2022` / `-2023` の 3 件 🔍 |
| canonical entity confidence | 0.2 — エンティティ同定の確度。本書の充実度とは別軸 |

⚠️ **「生産者名」と「ブランド名」がずれる造り手。** canonical は `Jérôme Prévost`、OBP の印字は全 5 本とも `'La Closerie, ...'` で始まる。**リスト上で «La Closerie» を見た staff が別の造り手だと思わないこと。**

⚠️ **canonical には «Fallet-Prévostat»（Avize の別生産者）という似た綴りの実体が存在する。🔍 別生産者であり衝突ではない**（村も品種も違う）。**再走査時に重複として拾わないこと。**

---

## Overview

✅ Champagne **Gueux** の **2ha の単一区画 «Les Béguines»** だけを耕し、そこから造る**極小生産者**。畑は分割されておらず（«d'un seul tenant»）、**シャンパーニュ原産地呼称の「境界」に位置する**（«bordure d'appellation d'origine Champagne»）。

✅ **ピノ・ムニエ 94%、セレクション・マサル、1964 年植樹。** 残りは 2000 年植樹のピノ・グリ 2%、シャルドネ 2%。**ムニエをシャンパーニュの主役に据えた造り手**であり、ブレンドの補助品種としてではなく単一区画の表現媒体として扱う。

✅ **初収穫 1987 年、最初の自家醸造ワインは 1998 年。** 以来 **1998 年から一貫して extra brut のみ**。

✅ 醸造は **発酵から 10 ヶ月の熟成まで全量木樽・全澱（sur lie entière）**、**自然発酵**、**マロラクティック発酵は「義務づけない」**、**機械も電気も使わない**、**瓶詰めは重力による緩慢な充填**。ドザージュは **1 本あたり 2.5g**。

✅ 栽培は **1994 年に殺虫剤を停止（テュフロドロムスの先駆的再導入）、1996 年に除草剤を停止**。ただし**公式表現は «Viticulture sans papier»（＝紙／認証を持たない栽培）であり、有機・ビオディナミの認証を名乗っていない。**

---

## History

⚠️ **公式サイトに沿革の年表は存在しない。** 以下は `Les Béguines` セクションの技術記述と `Le vigneron` セクションの散文から拾える年号のみ。**世代・相続・設立の経緯は公式に書かれていない。**

| 年 | 出来事 | |
|---|---|---|
| **1964** | **Les Béguines にピノ・ムニエをセレクション・マサルで植樹**（台木 3309 / 5BB Teleki）。現在の樹齢の起点 | ✅ |
| **1987** | **初収穫**（«Première récolte : 1987»） | ✅ |
| **1994** | **殺虫剤の使用を停止。テュフロドロムス（捕食性ダニ）の先駆的再導入** | ✅ |
| **1996** | **除草剤の使用を停止。**以後、全域で **griffage（爪掻き）と sarclage（除草）による土壌作業** | ✅ |
| **1998** | **最初の自家醸造ワインを産出**（«Premier vin produit : 1998»）。**同年より一貫して extra brut のみ** | ✅ |
| **2000** | **ピノ・グリとシャルドネを植樹**（台木 riparia / 41B）。同年 **菌根（mycorhization）への取り組みを開始** | ✅ |
| **2007** | **Fac Similé の最初のワインを産出** | ✅ |
| 2016/10 | 公式サイト制作（«Réalisation octobre 2016»）。**以後の更新記録なし** | ✅ |

### 🔴 «L'ami Anselme» — 公式が書いていることと、書いていないこと

✅ `Le vigneron` セクションに、Jérôme Prévost 自身の言葉で次の一節がある — **«L'ami Anselme me dévoila le sens du geste patiemment durant 24 saisons.»**（友人 Anselme が 24 シーズンにわたり、辛抱強く「所作の意味」を私に明かしてくれた）。同じ段落で母方の祖母・母・父が並置され、**«Ils furent mon écosystème.»**（彼らが私の生態系だった）と結ばれる。

⚠️ **公式が書いていないこと（＝現場で言ってはいけないこと）**
- **姓「Selosse」は公式サイトに一文字も出てこない。** 出てくるのはファーストネーム «Anselme» のみ。
- 「**Selosse の下で修業した**」「**Selosse の弟子**」「**Avize のセラーを借りて最初の数年を醸造した**」— **いずれも公式に記述が無い。**
- 公式が主張しているのは **「友人」であり「24 シーズンにわたって所作の意味を明かしてくれた人」** という関係性だけである。師弟関係とも雇用関係とも書いていない。

🔴 **この生産者について世間で最も多く語られる話が、公式では最も慎重に書かれている。** 語るなら公式の言い回しに寄せること（§Staff Notes に台詞を用意した）。
🔴 **そして THÉSEUS の canonical レコード（`prevost-la-closerie-2022`）は «セロスに師事した» «A student of Selosse» と断定的に書いている。→ §Canonical Conflict PV-1。**

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Champagne ✅ |
| **Village** | **Gueux**（郵便番号 51390）✅ |
| **Subregion** | Montagne de Reims 🔍 — **canonical `subregion` の値。公式サイトには «Montagne de Reims» の記載は無い** ❓ |
| **Key Vineyard** | **Les Béguines — 唯一の畑** ✅ |

⚠️ **canonical 内で subregion 表記が 3 通りに割れている** 🔍 — `Gueux — Montagne de Reims`（2022）／ `Gueux — Petite Montagne de Reims（モンターニュ・ド・ランス）`（2021）／ `Gueux — Montagne de Reims（Petite Montagne、ランス西方 約10km）`（2023）。**いずれも公式の記述ではない。**

### Les Béguines（公式の全項目）✅

| 項目 | 公式値 |
|---|---|
| **地籍** | **lieu-dit «Les Béguines»**（一区画の地名） |
| **«Closerie» の語義** | **«parcelle de vigne de deux à trois hectares entretenue par un closier»**＝**closier（小作の耕作者）ひとりが世話をする 2〜3ha の葡萄区画** |
| **«Les Béguines» の語義** | **«Javelle de sarments. Plusieurs béguines composent un fagot»**＝**剪定した蔓の束（ジャヴェル）。béguine がいくつか集まって fagot（薪束）になる** |
| **面積** | **2ha、d'un seul tenant（一続き・分割なし）** |
| **appellation 上の位置** | **«bordure d'appellation d'origine Champagne»＝シャンパーニュ原産地呼称の境界部** |
| **地質** | **Paléocène 5,900 万〜5,500 万年前 — Thanétien 期の石灰質砂（sable calcaire du Thanétien）** |
| **標高** | **120m** |
| **向き** | **南北軸（axe nord-sud）** |
| **植栽密度** | **8,333〜10,000 本/ha** |
| **仕立て** | **cordon permanent（永久コルドン）および cordon de Royat** |
| **品種構成** | **94% ピノ・ムニエ** — セレクション・マサル、台木 3309 / 5BB Teleki、**1964 年植樹**<br>**2% ピノ・グリ** — セレクション・マサル、台木 riparia / 41B、**2000 年植樹**<br>**2% シャルドネ** — セレクション・マサル、台木 riparia / 41B、**2000 年植樹** |

🔴 **«Les Béguines» は「修道女」の意味ではない。公式が語義を明示している — 「剪定した蔓の束」である。**
（フランス語の béguine には確かに «ベギン会修道女» の語義もあるが、**公式サイトはこの畑名について「蔓の束」と定義している。**）**canonical `terroir` は «レ・ベギーヌ（修道女の意）» と書いており、これは公式と食い違う。→ §Canonical Conflict PV-1。**

🔴 **«La Closerie» と «Les Béguines» は 2 つの別区画ではない。** 公式では **«La Closerie Les Béguines | Lieu dit "Les Béguines" |»** と一体で提示され、面積は **«2ha d'un seul tenant»（一続き）**。**canonical `terroir` の «2つの区画のブレンド» は公式と食い違う。→ §Canonical Conflict PV-1。**

⚠️ **公式の品種構成は 94 + 2 + 2 = 98% にしかならない。残り 2% が公式に説明されていない。** FR 原文・EN 訳とも同じ数字であり、訳の誤りではない。**数字を「勝手に 96% や 100% に直さない」。** ❓ Open Questions #5。

⚠️ **面積の単位に注意。** FR 原文は **«2ha»**、EN 訳は **«around 5 unsegmented acres»**。**5 acres ≒ 2.02ha で内容は一致**しており矛盾ではないが、**EN だけを読むと「5 ヘクタール」と誤読しうる。採用値は 2ha（FR 原文）。**
同様に «Closerie» の語義説明も FR **«parcelle de vigne de deux à trois hectares»**、EN «around 5 to 7.5 acres»。**採用は FR。**

### 区画内の呼び名 ✅

✅ Prévost は 2ha の中を自分の呼び名で細分している — **«Derrière le Golf»（ゴルフ場の裏）、«Le long du verger»（果樹園沿い）、«Les grands tours»、«Devant chez mamie»（おばあちゃんちの前）、«Du côté de chez Nono»、«Sur le chemin du haut»（上の道の上）、«Au dessus du puit»（井戸の上）、«Près des bassins»（溜池のそば）、«Les pinots gris»、«Au court noué»（フランクリーフ＝ウイルス病の出た所）**。

✅ 公式の言い回し — 畑は «un carré de 200 enjambées»（**200 歩四方**）で、畝は «本のページのように背で綴じられている»。そして «On s'y apprivoise, on s'y détaille, on s'y devine, on s'y donne — **depuis plus de 45 ans**»（そこで互いに手なずけ合い、細部を見合い、察し合い、与え合ってきた — **45 年以上**）。

⚠️ **«45 年以上» は 2016 年執筆時点の記述。** 2026 年の会話で「55 年」等に換算して語らないこと。**公式が言っているのは「45 年以上」だけ**である。

---

## Farming

### 🔴 最重要 — 認証は無い。公式は «Viticulture sans papier» と書いている ✅

✅ FR 原文の見出し語は **«Viticulture sans papier»** — 直訳すれば**「紙のない（＝書類・認証を持たない）栽培」**。EN 訳は «Undocumented viticulture»。続けて **«travail manuel engendré par l'observation, adapté aux conditions de milieu sans dogmatisme»**（**観察から生まれる手作業。環境条件に適応させ、教条主義によらない**）。

✅ `La Parcelle` セクションの詩句も同じ思想を反復する — **«Ignorer l'orthodoxie (Sourire quand ça ne pousse pas droit)»**（**正統を無視せよ。真っ直ぐ育たない時は微笑め**）、«Admettre la force du peu, la profondeur du pas beaucoup»（**僅かなものの強さ、大したことのないものの深さを認めよ**）、«Imaginer la vigne heureuse»（**葡萄樹が幸福であると想像せよ**）。

🔴 **したがって「オーガニック」「ビオディナミ」「ビオロジック」「Demeter」「Biodyvin」「AB」— これらの語を Prévost に使ってはならない。公式は認証の不在をむしろ積極的に宣言している。**

### 実施している具体策 ✅

| 施策 | 開始 | 内容 |
|---|---|---|
| **殺虫剤の全廃** | **1994** | **テュフロドロムス（typhlodromes、捕食性ダニ）の先駆的再導入**（«réintroduction pionnière»）— 天敵によるダニ制御 |
| **除草剤の全廃** | **1996** | 以後、**griffage（爪掻き）と sarclage（除草）による土壌作業を全域で** |
| **菌根への取り組み** | **2000** | «travail sur la mycorhization» — 根と菌類の共生 |
| **硫黄** | — | **soufre mouillable（水和硫黄）を使用** |
| **銅** | — | **«limitation absolue de l'usage de cuivre»＝銅の使用を絶対的に制限** |

⚠️ **銅は「制限」であって「不使用」ではない。**「銅を使っていません」と言わないこと。
⚠️ **水和硫黄は使っている。**「無農薬」「何も撒いていない」と言わないこと。

✅ `La pierre` セクションが栽培思想の根拠を述べる — 5,500 万年かけて堆積した石灰質の海洋化石層に、**«racines colonisées symbiotiques»（共生的にコロニー化された根）** が接触し、**カルシウム・カチオンの流れを解き放つ**。それが «fulgurance saline»（**塩味の閃光**）として試飲時に現れる、という筋書き。**菌根への取り組み（2000 年〜）はこの思想と直結している。**

---

## Winemaking

### La Closerie Les Béguines ✅

| 工程 | 公式記述 |
|---|---|
| **発酵** | **fermentation spontanée（自然発酵）— «vinification paresseuse»（怠惰な醸造）** |
| **発酵容器・熟成** | **«Fermentation élevage 10 mois en totalité sous bois sur lie entière»**＝**発酵と 10 ヶ月の熟成を全量木樽で、全澱とともに** |
| **樽** | **異なる木材、容量 225 / 228 / 400 / 500 / 600 L** の混成 |
| **MLF** | **«Fermentation malolactique sans obligation»＝マロラクティック発酵は義務づけない**（＝阻止も強制もしない） |
| **機械・電気** | **«Sans machine, sans électricité»＝機械なし・電気なし** |
| **瓶詰め** | **«Mise en bouteille lente par gravité»＝重力による緩慢な瓶詰め** |
| **ドザージュ** | **1998 年以降 exclusivement extra brut。Dosage : 2,5 g par bouteille** |

🔴 **ドザージュの単位に注意。公式は FR・EN とも «par bouteille / per bottle»＝「1 本あたり 2.5g」と書いている。「2.5 g/L」ではない。**
🔍 750ml 換算すると **約 3.3 g/L** になる（単純除算）。**この換算値は THÉSEUS 側の計算であって公式値ではない。** 客に言うなら「公式表記は 1 本あたり 2.5g」と言うのが安全。
🔴 **canonical の `prevost-la-closerie-2022` は «ドザージュ 4 g/L»「マロラクティック発酵なし」「2 年以上のシュール・リー」「手作業デゴルジュマン」と書いている。いずれも公式と食い違うか、公式に存在しない。→ §Canonical Conflict PV-1。**

### Fac Similé ✅

| 工程 | 公式記述 |
|---|---|
| **種別** | **champagne rosé d'assemblage（アッサンブラージュのロゼ）** — **セニエではない** |
| **語義** | «Fac-similé : reproduction identique à la source originale»（原本と同一の複製） |
| **構成** | **87% Les Béguines のヴァン・ド・バーズ ＋ 13% Les Béguines の赤の静止ワイン** |
| **赤の原料** | **区画内選抜（sélection intra-parcellaire）のピノ・ムニエ、房が緩く粒が小さいもの** |
| **赤の醸造** | **除梗した果房のアルコール発酵。cuve à chapeau flottant（浮き蓋タンク）** |
| **SO2** | **«fermentation spontanée sans SO2»＝自然発酵、SO2 なし**（**この記述は Fac Similé の赤の発酵についてのみ**） |
| **熟成** | **228L バリック で 10 ヶ月** |
| **瓶詰め** | **機械なし・電気なしの、穏やかで緩慢な tirage** |
| **初年** | **2007** |
| **年産** | **約 3,300 本** |
| **ドザージュ** | **extra brut rosé — 1 本あたり 2〜3g** |
| **ラベル** | **図案・表裏ラベル文とも Jérôme Prévost の創作** |

⚠️ **FR «cuve chapeau flottant»（浮き蓋タンク）が EN では «mobile roof tank» と訳されている。採用は FR の「浮き蓋」。**
🔴 **«sans SO2» は Fac Similé の赤ワイン部分の発酵についての記述であって、Les Béguines 全体・瓶詰め時・出荷時の SO2 について公式は何も言っていない。「亜硫酸無添加のシャンパーニュ」と言ってはいけない。**

### 公式が一切書いていない醸造情報 ❓

**新樽比率／樽の産地・トヌリエ名／培養酵母の有無／清澄・濾過／圧搾方法と歩留まり／ティラージュのリキュール／瓶熟期間／デゴルジュマン方式と時期／リザーヴワイン比率／収穫年構成／総生産本数（Fac Similé の 3,300 本を除く）** — **すべて非開示。** §Staff Notes の ⚠️ リスト参照。

✅ `Underground` セクションが熟成環境だけは描写する — セラーは **«puit intérieur»（内なる井戸）**、暗く・湿り・静かで・野生的。**meulière（ビュル石）を樽と同心円状に積んだヴォールト**の下に埋もれ、その隙間に «myriades de jardins minuscules»（**無数の微小な庭**＝微生物叢）が花開いて «grandissant le vin»（ワインを育てる）。

---

## Style

🔴 **公式サイトに味わいの記述（tasting note）は一文も無い。** 香り・味・骨格・熟成ポテンシャルについて公式は完全に沈黙している。**以下は上記 ✅ の技術事実からの構造的導出（🔍）であり、公式の味わい表現ではない。**

🔍 **① 単一区画・単一品種の表現。** 2ha 一続き・94% ムニエ・1964 年植樹の単一マサル選抜。**ブレンドによる平準化の余地が構造上ほぼ無い。**「シャンパーニュ」というより「Gueux の Les Béguines という場所のワイン」として構成されている。

🔍 **② 木樽由来のテクスチャーと、樽香の不在という設計。** 発酵から 10 ヶ月まで全量木樽・全澱。しかし**樽は 225〜600L の 5 サイズ・異なる木材の混成**であり、**大容量樽が混じる構成は新樽由来の香りを前に出す設計ではない**。狙いは酸化的取り扱いとテクスチャーであって樽香ではない。

🔍 **③ MLF を決めていないことの帰結。** «sans obligation» — 年により通る／通らない。**したがってヴィンテージ間で酸の質が揺れることが構造上織り込まれている。** 「毎年同じ味」を期待させる説明をしてはいけない。

🔍 **④ 塩味（salinité）は公式の自己申告がある唯一の風味語。** ただし味わい欄ではなく `La pierre` の思想セクションに **«la fulgurance saline opérera à la dégustation»（塩味の閃光が試飲時に作用する）** として現れる。**Thanétien 期の石灰質砂 → 菌根 → カルシウム・カチオン → 塩味**、という因果を Prévost 自身が主張している。**現場で塩味に言及する根拠はここにある。**

🔍 **⑤ 極低ドザージュ。** 1998 年以来 extra brut のみ、1 本あたり 2.5g。糖による丸めが構造的に無い。

⚠️ **第三者評価・点数・「◯◯年が当たり年」の類は公式に一切無い。** canonical には `points: 96 / 95 / 93` が入っているが **🔍 出典不明の内部値であり、公式でも第三者機関の公表値でもない。客に点数を言わない。** Confidence: **Low**。

---

## Important Cuvées

### 公式に存在するキュヴェは 2 つだけ ✅

| キュヴェ | 種別 | 公式 | canonical | OBP |
|---|---|---|---|---|
| **La Closerie «Les Béguines» Extra Brut** | 白・94% ムニエ | ✅ | ✅ 登録済 `cuvee:jerome-prevost-la-closerie-les-beguines-extra-brut`（保有 VT: `2022` / `NV (LC21)` / `NV (LC23)`） | ✅ 1 本 |
| **Fac Similé Extra Brut Rosé** | ロゼ・アッサンブラージュ | ✅ | 🔴 **canonical 未登録**（2021 / 2023 レコードの本文中に言及があるのみ） | 🔴 **OBP に掲載なし** |

🔴 **Fac Similé は canonical にキュヴェとして存在しない。** 公式に実在し、年産約 3,300 本、2007 年初出。**canonical 昇格時に追加すべきキュヴェ。**

### OBP 掲載分（5 本）— 印字そのまま 🔍

| # | OBP 印字（`source_wine_raw`） | VT | 価格 | `cuvee_state` | `match_state` / conf | 公式との照合 |
|---|---|---|---|---|---|---|
| 1 | `'La Closerie, Les Beguines,' Extra Brut` | 2023 | 920 | `alias` | `unresolved` / 0.0 | ✅ **公式 «La Closerie Les Béguines» と一致。唯一クリーンな 1 本。**（canonical に 2023 が無いため vintage は未解決） |
| 2 | `'La Closerie, &,' Extra Brut` | 2023 | 780 | `unresolved` | `unresolved` / 0.0 | ❓ **公式サイトに «&» というキュヴェは存在しない。** |
| 3 | `'La Closerie, &,' Extra Brut` | 2021 | 820 | `unresolved` | `unresolved` / 0.0 | ❓ 同上 |
| 4 | `'La Closerie,' Grand Cru Extra Brut` | 2023 | 1400 | `alias` | `unresolved` / 0.0 | 🔴 **公式に «Grand Cru» の記述は皆無。alias 解決が誤っている疑いが濃い。** |
| 5 | `'La Closerie,' Grand Cru Extra Brut` | 2022 | 1780 | `alias` | 🔴 **`alias` / 0.9** | 🔴 **同上。しかもこの 1 本だけ confidence 0.9 で `vintage:...-2022`（＝最も品質の低い canonical レコード）に確定的に紐付いている。** |

すべて `FRANCE | SPARKLING > CHAMPAGNE | BLENDS` セクション。価格は OBP 印字値（**通貨単位は intake に記録が無い** ❓）。5 本とも `source_quality_flags` は空、`_collision_risk` は LOW。

### 🔴 «&» について ❓

- **公式サイトに «&» の記載は一切ない。** 全 10 セクションの FR / EN 全文を確認済み。
- 🔍 **intake のパーサは «&» を「キュヴェ名」として解釈している** — `_parts.label = "La Closerie, &"`、`rank: null`、`normalized_cuvee: "La Closerie, &"`。このメニューの組版規約は `'ブランド, キュヴェ,' スタイル`（例: Krug `'Grande Cuvée, 173ème Édition,' Brut`）であり、**«&» は «Les Beguines» と同じスロットに入っている。**
- 🔍 **単なる組版事故である可能性は低い。** **2 ヴィンテージ（2023 / 2021）にわたり同一表記で反復**し、**Les Béguines（920）と別の価格帯（780 / 820）で別建て**されている。事故なら 2 回・別価格で揃わない。**「実在する別ボトリング」を第一候補として扱うのが妥当。**
- ⚠️ **ただし «Fac Similé» と同定してはならない。** 根拠 2 つ — ① Fac Similé は**ロゼ**だが «&» 2 本は `CHAMPAGNE | BLENDS` 節（ロゼ節ではない）に置かれている。② Fac Similé は年産約 3,300 本の希少ロゼで、**Les Béguines より安い 780 / 820 という価格付けは説明しにくい。**
- 🔍 残る候補は **(a) 2016 年（公式サイト制作年）以降に登場した新ボトリング**、**(b) ラベル上のロット記号や特殊文字がメニュー組版で «&» に潰れたもの**。canonical には **«LC21» «LC23» というロット表記**が実在する（公式ではなく THÉSEUS 側の記述）ため、(b) の系統は捨てきれない。
- ⚠️ **確認できたのはそこまで。** «&» の品種・造り・位置づけについて**公式の裏付けはゼロ**であり、現場で内容を語ることはできない。→ Open Questions #1。

### 🔴 «Grand Cru» について ⚠️

**これはメニュー側の誤りの可能性が高い。根拠は 3 つ。**

1. ✅ **公式サイトは «Grand Cru» という語を一度も使っていない。**
2. ✅ **公式はむしろ逆を書いている** — Les Béguines は **«bordure d'appellation d'origine Champagne»＝シャンパーニュ呼称の境界部**。**「境界にある畑」と「Grand Cru」は両立しない。**
3. ✅ **Prévost の畑は Gueux の Les Béguines 2ha ただ 1 つ。**他村の畑を公式に一切持っていない以上、**Grand Cru 村の葡萄を仕入れる余地が構造上ない。**

🔴 **さらに intake 側の問題** — #4 / #5 は `cuvee_state: alias` で **canonical の «La Closerie Les Béguines» に解決されている**。しかし印字は «Les Beguines» ではなく «Grand Cru» である。**Les Béguines とは別物である可能性が高いものが、Les Béguines として紐付いている。** #2 / #3 の «&» が `unresolved` で正しく止まっているのと対照的に、**#4 / #5 は「誤って解決された」疑いがある。**
🔴 **とくに #5（2022 / 1780）は `match_state: alias`・confidence 0.9・`vintage_state: exact` で確定扱いになっている。** intake の evidence は «canonical に vintage 2022 実在» だが、**その «vintage 2022» こそが §Canonical Conflict PV-1 で問題にしている低品質レコードである。**⚠️ **`unresolved` より `alias` の方が危険という実例。** → Open Questions #3。

⚠️ 価格の異常も傍証になる — Les Béguines 2023 が **920** に対し «Grand Cru» は **2023 が 1400、2022 が 1780**。**同一キュヴェの隣接ヴィンテージでこの開きは説明できない。**

---

## Staff Notes

> この節は上記の ✅ からのみ構成している。裏の取れていない事柄は書いていない。
> 🔴 **この生産者は記述が薄いのではなく「公式が語らないことが多い」タイプ。だから ⚠️ リストが本体である。**
> 🔴🆕 **加えてこの生産者は「社内 DB の記述が公式と食い違っている」タイプでもある。DB の説明文をそのまま読み上げないこと。**

**一行で言うと** — 「**Gueux の 2 ヘクタール、たった一枚の畑だけ**。**1964 年植えのピノ・ムニエが 94%**。**全量木樽で発酵させ、機械も電気も使わずに瓶に詰める。**」

### ゲストへの説明の芯（3 点）

**1. 畑は一枚、2 ヘクタール。それが全部です。**
Gueux という村の **«Les Béguines» という一続きの 2ha**。区画は分割されていません。**シャンパーニュという原産地呼称の、ちょうど境界にある畑**です。地質は **5,500 万年前・タネシアン期の石灰質の砂**。標高 120m、南北の畝。**Prévost はこの中を「ゴルフ場の裏」「おばあちゃんちの前」「井戸の上」と自分の呼び名で刻んで、45 年以上その畑と付き合っている**、と本人が書いています。

**2. ピノ・ムニエが 94%。1964 年の、セレクション・マサル。**
シャンパーニュでムニエは普通ブレンドの補助役ですが、**ここではムニエが単独の主役**です。**1964 年植樹**、クローンではなく**セレクション・マサル**。残りは 2000 年に植えたピノ・グリとシャルドネが少しずつ。**単一区画・単一品種なので、ブレンドで味を均す余地が構造的にありません。**

**3. 発酵から熟成まで全部木樽、機械も電気も使わない。**
**自然発酵**を本人は **«vinification paresseuse»＝「怠惰な醸造」**と呼びます。**発酵と 10 ヶ月の熟成を全量木樽で、澱をまるごと抱えたまま。** 樽は **225L から 600L まで 5 サイズ、木も揃えていない混成**です。**マロラクティックは「義務づけない」**— 年によって通ったり通らなかったり。**瓶詰めは重力だけで、ゆっくり。1998 年からずっと extra brut のみで、ドザージュは 1 本あたり 2.5g** です。

### 名前の由来（公式にある。使うと強い）✅

> 「**«クロズリー» というのは、耕作人がひとりで面倒を見られるくらいの、2〜3 ヘクタールの葡萄畑**を指す古い言葉です。**«ベギーヌ» は剪定した蔓を束ねたもの** — それがいくつか集まると薪の束になる。**畑の名前も、蔵の名前も、畑仕事の言葉から来ています。**」

🔴 **«ベギーヌ＝修道女» と説明しない。公式は「蔓の束」と定義している。**（社内 DB の旧記述にこの誤りが入っている。）

### 「Selosse との関係は？」と訊かれたら（頻出）

🔴 **公式に書いてあるのはここまで、という線を守る。**

> 「ご本人が公式に書いているのは、**«友人 Anselme が、24 シーズンにわたって辛抱強く《所作の意味》を自分に明かしてくれた»** という一節です。母方の祖母、母、父と並べて **«彼らが自分の生態系だった»** と締めています。**それ以上のこと — 修業したとか、どこで醸造していたとかは、ご本人は公式には書いていません。**」

**これで止める。** «Anselme» の姓、師弟関係、Avize のセラー — **すべて公式の裏が取れていない。**

### 🔴 リストで気をつけること — Prévost は 5 本中 4 本が要注意

| リストの印字 | 現場での扱い |
|---|---|
| `'La Closerie, Les Beguines,'` 2023 / 920 | ✅ **これだけが公式のキュヴェと確実に一致。安心して上記 3 点を語ってよい。** |
| `'La Closerie, &,'` 2023 / 780 ・ 2021 / 820 | ⚠️ **«&» が何かを THÉSEUS は確認できていない。**「Les Béguines と同じもの」とも「ロゼのファクシミレです」とも言わない。**生産者・畑・品種の話（芯 1・2）は共通なので、そこまでで止める。**キュヴェ固有の造りには踏み込まない。 |
| `'La Closerie,' Grand Cru` 2023 / 1400 ・ 2022 / 1780 | 🔴 **«Grand Cru» と口に出さない。**「グラン・クリュのシャンパーニュです」と言った瞬間に誤りになる。**Prévost の畑は Gueux の 1 枚だけで、呼称の境界にある**とご本人が公式に書いている。**リスト表記について確認が要る旨をマネージャーに上げる。** |

### ⚠️ 現時点で言ってはいけないこと

- 🔴 **「グラン・クリュ」** — 公式に記述ゼロ。**公式はむしろ「呼称の境界にある畑」と書いている。**メニュー印字を鵜呑みにしない。
- 🔴 **「ピノ・ムニエ 100%」** — **公式は 94%。**（社内 DB の cuvée facts が «Pinot Meunier 100%» になっている。**DB が間違っている。**）
- 🔴 **「ラ・クロズリーとレ・ベギーヌ、2 つの畑のブレンド」** — **公式は「一続きの 2ha、単一区画」。**（これも社内 DB の旧記述の誤り。）
- 🔴 **「ベギーヌは修道女の意味」** — **公式は「剪定した蔓の束」と定義している。**
- 🔴 **「オーガニック」「ビオディナミ」「ビオ認証」「デメテール」「Biodyvin」** — **公式表現は «Viticulture sans papier»＝紙（認証）を持たない栽培**。認証の不在を本人が宣言している。**認証名を一つでも出したら誤り。**
- 🔴 **「亜硫酸無添加」「SO2 ゼロ」** — 公式の «sans SO2» は **Fac Similé の赤ワイン部分の発酵** についての記述のみ。**Les Béguines 全体・瓶詰め時については公式は何も言っていない。**
- 🔴 **「銅を使っていない」「農薬を一切使っていない」** — 公式は **«水和硫黄を使用»**、**銅は «絶対的に制限»（＝不使用ではない）**。
- 🔴 **「Selosse の弟子」「Selosse のところで修業した」「Avize のセラーを借りていた」** — **公式に一切無い。**公式は «友人 Anselme»・«24 シーズン» のみ。
- 🔴 **「祖母から畑を継いだ」** — 公式に相続の記述は無い。祖母は `Le vigneron` に「庭に立っていた」人として、区画の呼び名に «おばあちゃんちの前» として出るだけ。
- 🔴 **「1998 年創業」** — 公式は **«最初の自家醸造ワインが 1998 年»**、**«初収穫は 1987 年»**。設立年としては書かれていない。
- 🔴 **「ドザージュ 2.5 g/L」「4 g/L」** — 公式は **«1 本あたり 2.5g»**。単位が違う。**言うなら「1 本あたり 2.5 グラム」。**（DB の 4 g/L は誤り。）
- 🔴 **「マロラクティックはやりません」** — 公式は **«義務づけない»**。**「やらない」と断定しない。**（DB の «マロラクティック発酵なし» は誤り。）
- 🔴 **「年産 5,000 本」「◯◯本しか造らない」** — 公式にあるのは **Fac Similé の約 3,300 本だけ**。**Les Béguines の本数も総生産量も非公開。**
- 🔴 **「96 点」「95 点」などの点数** — **公式にも第三者公表にも根拠が無い社内値。客に言わない。**
- 🔴 **新樽比率／トヌリエ名／培養酵母／濾過・清澄／瓶熟期間／デゴルジュマン時期／リザーヴワイン比率** — **全部非開示。**「新樽は使いません」も「ノンフィルターです」も**推測であり言ってはいけない。**
- ⚠️ **「2023 ヴィンテージのシャンパーニュ」と断定しない** — **公式サイトはヴィンテージ表記・NV の別について一切説明していない。** canonical 側も `2022`（vintage 宣言）と `NV (LC21)` `NV (LC23)` が混在している。**年号は「リスト上の表記」として扱う。**
- ⚠️ **「畑は 5 ヘクタール」** — **EN 訳の «5 acres» の誤読。正しくは 2ha。**
- ⚠️ **「ムニエ 94%、ピノ・グリ 2%、シャルドネ 2%、あと 2% は◯◯」** — **残り 2% は公式に書かれていない。**埋めて話さない。

---

## Akio's Insight

*（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）*

---

## Canonical Conflict

> 🔴 **解決していない。canonical は一切書き換えていない。エスカレーション用の記述である。**
> 既存の `research/canonical_conflicts/REGISTER.md` を先に確認した — **Jérôme Prévost / La Closerie は同登録票に未記載**（P-1〜P-7 / C-1〜C-3 / §C 誤検出 54 件のいずれにも含まれない）。
> **したがって以下は新規。REGISTER.md への追記が必要**（本 research からは REGISTER.md を編集しない）。

### PV-1 🔴 `La Closerie Les Béguines Extra Brut` — 3 legacy レコードが 1 キュヴェに統合された際、**公式と矛盾する側の facts が採用された**

**① 衝突している canonical ID**
- `producer:jerome-prevost` — legacy_ids = `prevost-la-closerie-2021` / `prevost-la-closerie-2022` / `prevost-la-closerie-2023`
- `cuvee:jerome-prevost-la-closerie-les-beguines-extra-brut` — **上記 3 件すべてを legacy_ids に持つ単一キュヴェ**
- 配下 vintage 3 件 — `vintage:...-2022`（`nv:false`, `vintage_year:2022`）／ `vintage:...-nv-lc21`（`nv:true`）／ `vintage:...-nv-lc23`（`nv:true`）

**② なぜ重複／衝突に見えるか**
3 レコードは同一キュヴェの別ボトリングとして 1 つの cuvée に畳まれている。**畳んだこと自体は妥当**だが、**2 つの相容れない同定規約が同居している** —
- `2022` 系 = **ミレジム宣言のヴィンテージ champagne**（`nv:false`）、名称は素の `La Closerie Les Béguines Extra Brut`
- `LC21` / `LC23` 系 = **NV ＋ ロット記号**（`nv:true`）、名称は `... Extra Brut (LC21)` / `(LC23)`
そして **`LC23` レコード自身の本文が «法定のミレジムは名乗らずノン・ヴィンテージとして販売される» と書いている。** つまり **同一キュヴェ内で、あるレコードが他のレコードの同定規約を否定している。** これは REGISTER.md の **C-3（Denis Mortet — 命名規約の二重化）と同型**。

**③ Evidence**
cuvée レベルの `facts` は **`prevost-la-closerie-2022` 側から採られている**（`resolved_bottles.json` で 3 本とも同一の cuvée facts を持つ）:

| cuvée `facts` の値 | 公式（champagnelacloserie.fr）| 判定 |
|---|---|---|
| `grapes: ["Pinot Meunier 100%"]` | **94% meunier + 2% pinot gris + 2% chardonnay** | 🔴 **矛盾** |
| `color: "Blanc de Noirs"` | 記載なし（`LC21`/`LC23` レコードは `Blanc`） | ⚠️ **内部不一致** |
| `terroir:` «「ラ・クロズリー」と「レ・ベギーヌ」の**2 つの区画のブレンド**» | **«2ha d'un seul tenant»＝一続きの単一区画** | 🔴 **矛盾** |
| `terroir:` «レ・ベギーヌ（**修道女**の意）» | **«Javelle de sarments»＝剪定した蔓の束** | 🔴 **矛盾**（公式が語義を明示している） |
| `terroir:` «**サンディなシルト**土壌» | **«sable calcaire du Thanétien»＝タネシアン期の石灰質砂** | ⚠️ **食い違い** |
| `tags: [... "Vintage" ...]` | ミレジムの言及なし | ⚠️ |

vintage `2022` レベルの `facts` にはさらに:

| 値 | 公式 | 判定 |
|---|---|---|
| `dosage: "Extra Brut — 4 g/L"` | **«2,5 g par bouteille»（1 本あたり 2.5g）** | 🔴 **矛盾** |
| `winemaking:` «マロラクティック発酵**なし**» | **«sans obligation»＝義務づけない** | 🔴 **矛盾** |
| `winemaking:` «**2 年以上**のシュール・リー» / `aging: "2+ years sur lie"` | **«10 mois sous bois sur lie entière»**、瓶熟期間は**非公表** | 🔴 **矛盾** |
| `winemaking:` «**旧バーガンディ樽**（セロス哲学）» / «手作業デゴルジュマン» | 樽は «différents bois» 225–600L。デゴルジュマンの記載なし | 🔴 **公式に無い** |
| `description:` «**セロスに師事**した» / «A student of Selosse» | 公式は «**L'ami** Anselme»（姓なし・24 saisons）のみ | 🔴 **公式に無い** |
| `description:` «年産約 **5,000 本**» | **非公表**（公式の本数は Fac Similé の 3,300 本のみ） | 🔴 **公式に無い** |
| `points: 96` | 公式にも第三者公表にも根拠なし | ⚠️ |

対して `LC21` / `LC23` の 2 レコードは **公式値（94/2/2・2.5 g/瓶・10 ヶ月木樽・MLF 義務なし・98% の残余は非公表）を正しく写しており、非公表項目を明示的に «記載しない» と断っている。** **品質が明確に非対称である。**

**④ OBP への影響** 🔴
- OBP 5 本のうち **#5 `'La Closerie,' Grand Cru Extra Brut` 2022 / 1780** が、`match_state: alias`・**confidence 0.9**・`vintage_state: exact` で **`vintage:...-2022`（＝上表の低品質レコード）に確定的に紐付いている。** intake の evidence は «canonical に vintage 2022 実在» のみ。**リスト最高価格帯の 1 本が、公式と矛盾する記述に接続されている。**
- **cuvée レベルの誤り（100% ムニエ / 2 区画ブレンド / 修道女）は cuvée 経由で 5 本すべてに波及する。**
- #4（2023 / 1400）も同 cuvée に `alias` 解決済み。
- 結果として **「Grand Cru」というメニュー側の誤りと、「100% ムニエ・セロスの弟子・年産 5,000 本」という DB 側の誤りが、同じボトルの上で重なっている。**

**⑤ 推奨される解決策（実行しない）**
1. **3 レコードを統合したまま、cuvée `facts` の供給元を `prevost-la-closerie-2022` から `LC23`（最新かつ公式準拠）に差し替える**か、あるいは **cuvée facts から公式で裏が取れない項目（grapes / color / terroir）を落とす。**
2. **`vintage:...-2022` の同定を再検討する。** `2022` を「ミレジム宣言のヴィンテージ」として持つ根拠が公式にない。**`NV (LC22)` として他 2 件と規約を揃えるべきか**は architecture の判断。
3. **`points` / 年産本数 / 「セロスに師事」等、出典を持たない断定を canonical から分離する**（Research Layer 側に降ろす）ルールの検討。
4. **`Fac Similé` を cuvée として新規登録**するかの判断（公式に実在・canonical 未登録）。
→ **Akio と CTO の判断が要る。research 側では動かさない。**

**⑥ Confidence: High**
（3 レコードの生データを `migration/out/export/db_wine_canonical.json` と `resolved_bottles.json` で直接確認。矛盾は公式サイト原文と 1 対 1 で対照済み。OBP 実害は `obp_intake_normalized_20260804.json` の `match_state`/`confidence` で確認済み。）

### 誤検出として除外したもの（再走査時に拾わないこと）
- **`Fallet-Prévostat`（Avize, Champagne）と `Jérôme Prévost`** — 姓の綴りが近いだけの**別生産者**。村・品種・キュヴェとも一致しない。**衝突ではない。**
- **`La Closerie Les Béguines` と `Fac Similé`** — 同一生産者の**別キュヴェ**（白とロゼ）。**衝突ではない。**

---

## Sources

### 一次資料（公式サイト・2026-08-04 参照）✅

**`https://champagnelacloserie.fr/`（FR 原文）／ `https://champagnelacloserie.fr/en/`（EN 訳）**

**サイト構造: 1 ページ完結のパララックス・サイト。下位ページは存在しない**（`/fr/` は 404、`robots.txt` `sitemap.xml` とも 404）。HTML 内の `href` は `#`・`css/style.css`・`css/stylesheet.css`・`https://champagnelacloserie.fr/en`・Google Fonts の 5 種のみ。**FR 版が原文、EN 版が訳。本書は食い違い時に FR を採用した。**

| セクション（FR / EN） | 得た主な事実 |
|---|---|
| `La pierre` / The Stone | **Thanétien 期石灰質砂**、5,500 万年、**共生根 → カルシウム・カチオン → «fulgurance saline»**（塩味の唯一の公式言及） |
| `Les vaisseaux` / The vessels | 樽の思想（futaille / flottille）。**樽 = 記憶・呼吸・航海** |
| `La peau` / The skin | 収穫の時機（Kairos）、リグニン → 腐植と樽、HUMUS-HOMME-HUMBLE |
| `L'intime` / The intimate | **区画内 10 個の呼び名**、**«200 歩四方»**、**«45 年以上»**（⚠️ 2016 年時点） |
| `La parcelle` / The plot | 栽培思想 — **«正統を無視せよ»**、«僅かなものの強さ»、«葡萄樹が幸福であると想像せよ» |
| `Underground` | **セラー描写 — meulière のヴォールト、微生物叢（«無数の微小な庭»）** |
| **`Les Béguines`** | 🔴 **本書の技術情報の中核。«Closerie» と «Les Béguines» の語義**・面積 2ha・**呼称の境界**・地質・標高 120m・**品種と台木と植樹年**・密度 8333–10000・南北軸・コルドン・**«viticulture sans papier»**・**1994 殺虫剤／1996 除草剤／2000 菌根**・水和硫黄・銅制限・**初収穫 1987／初醸造 1998**・自然発酵・**全量木樽 10 ヶ月 sur lie entière**・**MLF 義務なし**・**機械電気なし**・**樽 225/228/400/500/600L**・重力瓶詰め・**extra brut 2.5g/本**・**ラベル文は本人執筆** |
| **`Fac similé`** | 🔴 **第 2 キュヴェの全仕様。**ロゼ・**アッサンブラージュ**・**87% + 13%**・区画内選抜・**浮き蓋タンク**・**SO2 なし発酵**・**228L で 10 ヶ月**・**初年 2007**・**年産約 3,300 本**・**2〜3g/本** |
| `Le vigneron` / The wine-grower | 🔴 **«L'ami Anselme... 24 saisons»**、祖母・母・父、«Ils furent mon écosystème» |
| `Les clefs` / The Keys | **住所 65 rue des Dames de France 51390 Gueux**、電話、メール、**«Agnès et Jérôme Prévost»**、**予約制見学（生育最盛期・収穫期は不可）**、**アロカシオン制販売** |
| （フッター） | **«Textes : Jérôme Prévost»**（本文は本人執筆）、**«Réalisation octobre 2016»** |

**取得済みローカル素材** — `/Users/akiomatsumoto/Theseus_Phase0/research/producers/_sources/jerome-prevost/`
`home_fr.html` `home_fr.txt`（FR 原文全文）／ `home_en.html` `home_en.txt`（EN 訳全文）

⚠️ **テクニカルシート PDF は存在しない。** HTML 全文を走査して `.pdf` / `.doc` 参照はゼロ。JS 注入リンクも無し。**Louis Latour 型の PDF 収穫はこの生産者では不可能。**

### 二次資料

**なし。本書の「生産者に関する事実」は全面的に公式サイトのみに基づく。** 小売店・EC・インポーター・レビュー集約サイト・Wikipedia の記述は**一切使用していない**（公式ドメインの特定にのみ検索を用いた）。

### THÉSEUS 内部データ 🔍

| ファイル | 用途 |
|---|---|
| `batch3.json`（scratchpad） | canonical レコード概要 / canonical キュヴェ / OBP intake 5 本 |
| `/Users/akiomatsumoto/Theseus_Phase0/migration/out/export/db_wine_canonical.json` | legacy 3 レコード全文（§Canonical Conflict の一次証拠） |
| `/Users/akiomatsumoto/Theseus_Phase0/migration/out/export/resolved_bottles.json` | producer / cuvée / vintage の解決結果と `facts` の継承元 |
| `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` | OBP 5 行の `_parts` / `match_state` / `confidence` / `evidence` |
| `/Users/akiomatsumoto/Theseus_Phase0/research/canonical_conflicts/REGISTER.md` | 既出衝突の確認（**Prévost は未記載＝新規**）。**読み取りのみ** |

**🔒 canonical ファイルは読み取りのみ。一切書き換えていない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **High** | 住所・連絡先・名義・ブランド名・見学条件まで公式。canonical alias が空なのは別問題 |
| Overview | **High** | すべて公式の技術記述から |
| History | **Medium** | **年号は公式で確実（1964/1987/1994/1996/1998/2000/2007）だが、沿革の物語（相続・設立経緯・世代）は公式に存在しない** |
| Location | **High** | 面積・地質・標高・向き・密度・台木・植樹年・**畑名と蔵名の語義**まで公開。⚠️ 品種構成が 98% にしかならない |
| Farming | **High** | 転換年と具体策が公式。**「認証なし」を公式が明言しているのが強い** |
| Winemaking | **High**（工程）／ **Low**（数値の一部） | 発酵容器・熟成期間・樽容量・MLF 方針・ドザージュまで公式。**新樽比率・酵母・濾過・瓶熟・デゴルジュマンは全面非開示** |
| Style | **Low** | **公式に味わいの記述が一文も無い。**構造からの導出と «salinité» の一語のみ |
| Important Cuvées | **Medium-Low** | **公式キュヴェ 2 つは High。しかし OBP 5 本中 4 本が公式に照合できない** |
| Staff Notes | **High** | すべて上記 ✅ から構成。**⚠️ リストがこの生産者では本体** |
| **Canonical Conflict** | **High** | **3 レコードの生データを直接確認し、公式原文と 1 対 1 で対照。OBP 実害も intake の `confidence` で確認済み** |
| **総合** | **Medium-High — staff-usable。70% 到達済み。** | **畑・栽培・醸造という「客が必ず訊く」層は公式で厚く取れている**（むしろ Leflaive より技術数値は細かい）。**減点は Style の完全な不在と、OBP 4 本のキュヴェ未確定。**ただし**⚠️ リストで誤りを封じているため、現場で間違ったことを言わずに語れる状態**は満たしている。**なお本書の最大の価値は §Canonical Conflict — 既存 DB の記述をそのまま使うと誤りになることを特定した点にある。** |

---

## Open Questions

1. 🔴 **«&» とは何か。** OBP に 2 ヴィンテージ（2023 / 2021）・独自価格帯（780 / 820）で反復掲載されているが、**公式サイトに記載が無い。** 組版事故ではなく実在の別ボトリングである可能性が高い。**Fac Similé とは同定できない**（BLENDS 節・価格が Les Béguines より安い）。**確定にはインポーター資料か実ボトルのラベル／裏ラベルが要る（裏ラベル文は Prévost 本人の執筆と公式にある）。→ 最優先。**
2. 🔴 **«Grand Cru» 表記 2 本（2023 / 1400、2022 / 1780）の正体。** 公式に Grand Cru は存在せず、Prévost は Gueux の 1 区画しか持たない。**かつ intake が誤って canonical «Les Béguines» に alias 解決している疑いが濃い。メニュー印字の誤りか、別キュヴェの誤記か。マネージャー確認事項。**
3. 🔴 **intake の alias 解決ロジック。** #4 / #5 が `alias` で解決され、#2 / #3 が `unresolved` で止まった。**「Grand Cru」という明らかに異質な語を含む印字が「canonical 側がスタイル語を名称に含むだけの表記差」として通ってしまう**のは、canonical キュヴェが 1 件しかない生産者で起きる典型的な誤マッチ。**さらに #5 は confidence 0.9 で確定している。`unresolved` より `alias` の方が危険という実例として横展開すべき。**
4. 🔴 **PV-1 の裁定（§Canonical Conflict）。** cuvée facts の供給元差し替え／`vintage 2022` の NV 化／出典なき断定の分離／`Fac Similé` の新規登録 — **4 点とも architecture の判断待ち。REGISTER.md への追記が必要。**
5. **品種構成の残り 2%。** 公式が 94 + 2 + 2 = 98% で止まっている。FR / EN とも同一のため訳出誤りではない。**公式の記載漏れ。**
6. **ヴィンテージ表記の意味。** 公式はヴィンテージ／NV について何も説明していない。canonical は `2022`（ミレジム宣言扱い）と `NV (LC21)` `NV (LC23)` が混在。**OBP は全 5 本に年号がある。この年号がベース年なのか収穫年なのか呼称上のミレジムなのか、公式では判定不能。**
7. **«Anselme» の姓と関係の性質。** 公式はファーストネームと «24 saisons» のみ。**公式で確定できるのはここまで。**
8. **公式サイトが 2016 年以降更新されていない。** 現況（当主・後継・畑の増減・新キュヴェ・セラー移転の有無）は**すべて現在性未確認**。**Prévost は単独の生産者であり当主交代の論点は現時点で無いが、「2016 年時点の記述である」ことは全項目に掛かる。**
9. **CIVC 上の区分（RM / NM 等）。** 公式に記載なし。ラベルの登録番号でのみ判定可能。
10. **通貨単位。** OBP 価格（780 / 820 / 920 / 1400 / 1780）の通貨が intake に記録されていない。
