# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:domaine-jean-louis-chave` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式で確認**（一次資料）。本書では出典を 3 系統に分けて明示する —
>   `✅生` = 生産者自身の公式サイト `domainejlchave.fr` ／
>   `✅公` = 公的機関の一次資料（INAO 公式 cahier des charges・Agence Bio／EU TRACES 有機認証・INSEE 企業登記）
> `📄` 非公式資料のみ（**本書では 1 件も採用していない**）／ `⚠️` 食い違い・注意。両方を残す
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04（JST 2026-08-05）
>
> 🔴 **この生産者は「公式サイトが実質存在しない」ケースである。**
> `http://www.domainejlchave.fr/` は **画像 2 枚と 1 行のフッターだけの 1 ページ**で、
> 履歴・畑・醸造・ワイン一覧・連絡先の**いずれのページも存在しない**（本日 HTTP で再取得して確認）。
> ナビゲーションリンクは 0 本、**テクニカルシート PDF も 0 件**（Louis Latour で使えた `/pdf/en/*.pdf` 方式は存在しない）。
> `http://www.jlchaveselection.com/` は本文が **「En cours de réalisation.」の 1 行のみ**。
> → **生産者由来の一次情報は「1481 年からの父子継承」「Mauves en Ardèche」だけ**である。
> 本書はその穴を**埋めない**。代わりに、**公的機関の一次資料**（AOC 法定要件・有機認証・企業登記）で
> 「間違ったことを言わずに語れる」範囲を最大化し、**言ってはいけないことを列挙する**方針をとる。
>
> 🔴 **`jeanlouischave.com` は公式ではない。Amazon アフィリエイトサイトである。**
> 検索上位に出るが、`tag=jeanlouischave` のアフィリエイトタグと "Check Price" ボタンを持つ商用ページ。
> 生産者名を冠した第三者サイト。**参照禁止**。取得物は `_sources/.../REJECTED_jeanlouischave-com_amazon-affiliate.html` に
> 「棄却済み」として保存してある（次の担当者が同じ罠を踏まないため）。詳細は §Sources。

---

## Identity

| | |
|---|---|
| **Canonical Name** | Domaine Jean-Louis Chave |
| **公式サイトの自称** | **Domaine Jean-Louis CHAVE** ✅生 |
| **公式タグライン** | **「Vignerons de père en fils depuis 1481」**（父子相伝の造り手、1481 年より）✅生 |
| **Aliases** | canonical `aliases` は **空**。🔍 **OBP メニューの印字は `Jean Louis Chave`**（ハイフン無し・Domaine 無し）→ alias 登録候補 |
| **法人名（登記）** | **DOMAINE JEAN LOUIS CHAVE** — SIREN `379077795` / SIRET `37907779500019` ✅公 |
| **法人設立** | **1990-07-01**（登記上の法人設立日。**家系の歴史とは別物**）✅公 |
| **主たる活動 (NAF)** | `01.21Z` ブドウ栽培 ✅公 |
| **法定代表者** | **CHAVE, Jean-Louis Paul Bernard Marie（1968 年 8 月生）— gérant 兼 無限責任社員** ✅公 |
| **もう一方の無限責任社員** | **CHAVE 1481**（法人。SIREN `890534431`）✅公 |
| **雇用規模** | INSEE `tranche_effectif_salarié = 12`（2023 年）🔍 INSEE 区分表では 20〜49 人に相当 |
| **有機認証番号** | **FR-BIO-15.250-0061897.2025.001**（Bureau Alpes Contrôles）✅公 |
| **業態** | **ドメーヌ（自社畑）**。ネゴシアン部門は**別法人**（§Canonical Conflict） |
| canonical id | `producer:domaine-jean-louis-chave` |
| canonical entity confidence | 0.2（source: `legacy_app`）— エンティティ同定の確度であり、本書の充実度とは別軸 |

⚠️ **公式サイト内部に軽微な表記揺れがある。** ヘッダ画像は **「Vignerons」（複数形）**、
`alt` 属性とフッターは **「Vigneron」（単数形）**。メニューや POP に引用する場合は
**画像側の «Vignerons de père en fils depuis 1481» を採る**（画像がブランドの提示形だから）。

---

## Overview

✅生 フランス・**アルデッシュ県 Mauves**（ローヌ右岸）に本拠を置くドメーヌ。公式サイトが掲げる自己規定は
**「Vignerons de père en fils depuis 1481」— 1481 年からの父子相伝**、ただ 1 行。
公式サイトには**これ以外の説明文が一切無い**（§Sources）。

✅公 家族の持株会社の登記名が **「CHAVE 1481」**（2020-11-02 設立、SAS、NAF `64.20Z` 持株会社、
所在地はドメーヌと同一の 37 avenue Saint-Joseph）である。**1481 という年号は家族自身が法人名に使っている。**
→ 「1481」は第三者の伝承ではなく、**家族自身の自己申告として二重に確認できる**（公式サイト＋登記名）。

🔍 THÉSEUS canonical 上の保有キュヴェは **Hermitage** と **Saint-Joseph** の 2 件のみ。
**OBP 掲載 11 本はすべてこの 2 アペラシオンで、うち 6 本が Hermitage の白である**（§Important Cuvées）。

✅公 **有機認証を取得している。** 認証機関 **Bureau Alpes Contrôles（FR-BIO-15）**、
**2016-02-04 に engagement**、2025 年管理年度で **Hermitage・Saint Joseph の両方が「Biologique」**。
一部区画は依然 **転換中（C2 / C3）**。→ §Farming。**これが本ドシエで最も実用価値の高い確定事実である。**

---

## History

🔴 **生産者由来の歴史記述は「1481」の 1 語しか存在しない。** 世代数・当主の代替わり・畑の取得年・
フィロキセラ時の移転——**いずれも公式サイトに記載が無い。** 本節は薄いまま出す。

### 家族・法人について公式に言えること

| 事項 | 内容 | 出典 |
|---|---|---|
| **1481** | 「父子相伝の造り手、1481 年より」— **公式サイトの自称**。1481 年に何が起きたかの説明は無い | ✅生 |
| **1481（傍証）** | 家族の持株会社が **「CHAVE 1481」**（2020-11-02 設立） | ✅公 |
| **1990-07-01** | **法人 DOMAINE JEAN LOUIS CHAVE の登記設立日** | ✅公 |
| **1996-08-01** | **JL CHAVE SELECTION の法人設立日**（別法人・ネゴシアン。§Canonical Conflict） | ✅公 |
| **2016-02-04** | **有機認証機関への engagement 日**（＝転換の起点） | ✅公 |
| **2020-11-02** | 持株会社 **CHAVE 1481** 設立 | ✅公 |
| **2025-01-23** | 同一住所に **POISSON ROUGE**（SIREN `941000234`、NAF `68.20B` 不動産賃貸）設立。gérant は Jean-Louis Chave、無限責任社員に CHAVE 1481 | ✅公 |
| **現在の代表** | **Jean-Louis Chave（1968 年 8 月生）**。登記の最終更新は RNE 2026-07-17 / INSEE 2025-12-06 → **現況として使える** | ✅公 |

❓ **Gérard Chave の現況は公式に確認できない。** 公式サイトの meta keywords に `Gérard Chave` の語は
残っているが、**現在の役割・存否を示す公式記述は無い。** 登記上の代表者は Jean-Louis Chave のみ。
🔴 **前回の教訓（Louis-Fabrice Latour 事件）を適用する。日付の無い情報を「現在」として語らない。**
→ §Staff Notes の禁止リスト。

❓ **世代数は公式に確認できない。** 「16 代目」等の数字は**商用サイトにしか出てこない**（§Sources の棄却記録）。**使用禁止。**

### アペラシオン側の歴史（✅公 INAO 公式 cahier des charges より。**Chave 家の話ではない**）

**Hermitage**
- **1936-06-25** ヴァランス地裁判決で原産地として認定 → **1937-03-04 の décret で AOC 認定**
- 現行 CDC は **décret n° 2011-1806（2011-12-06）**、**décret n° 2013-1095（2013-11-29、JORF 2013-12-03）**で改正。
  さらに **2024-06-25 の全国委員会**で改正案が審議されている
- ⚠️ **エルミット伝説は INAO 自身が「apocryphe（真偽不確か）」と明記している。**
  1836 年の『album du Dauphiné』（ALBERT du BOY）が、アルビジョワ十字軍帰りの騎士
  **Henri Gaspard de Stérimberg** が **1224 年頃**に隠者として住み着いたと伝えるが、INAO は
  「**Ce récit reste apocryphe**」とした上で、**Tain-l'Hermitage 市の文書で実証できるのは
  「1598 年以降、複数の隠者が丘に住んだ」ことだ**と書いている。丘の名は
  **「Saint-Christophe の丘」→「l'Ermitage の丘」**と変わり、それが AOC 名になった
- **1890** Tain-l'Hermitage 農業組合 → **1930** 「Hermitage」保護組合（境界画定が第一の目的）→ AOC 認定へ
- **2009 年時点で 137 ha**（生産・申告面積）。**協同組合 1・ネゴシアン 7・自家蔵 17**。**赤が生産の 70%**

**Saint-Joseph**
- **1956-06-15 の décret** で **Tournon 周辺 6 コミューン**が AOC 認定 → **1969 年に 20 コミューン追加**、北は Condrieu の territoire まで拡大
- 現行 CDC は **décret n° 2011-1375（2011-10-25）**、**arrêté 2018-12-21（JORF 2018-12-27）**改正。CDC 承認は **2023-11-30 の全国委員会**
- ⚠️ **「Saint-Joseph」は Tournon の一地籍リュー・ディ（quartier cadastré）の名である。**
  この名が選ばれたのは、**その畑の評判が確立していたこと**と、**隣村 Mauves の栽培家が一部を耕作していたから**。
  さらに **17 世紀に Tournon のイエズス会が、Mauves と Tournon のワインを指す語として既に用いていた**
- 中世、Saint-Joseph のワインは **「vins de l'Hermitage」および「vins de Mauves」**と呼ばれていた
- **1312 年**、右岸（現アルデッシュ）はフランス王国に、左岸（現ドローム）は帝国に属したままとなり、
  **右岸のワインは Dauphiné 市場への出口を失った。**さらに **1446 年のブルゴーニュ公の禁令**が
  Tournon を含む「bas pais」の"外来"ワインを締め出した。**同緯度・対岸の Hermitage はその間に評判を広げた**
- **1533 年**、ローマ滞在中の Tournon 枢機卿が「vin de Tournon」を送らせた。**フランソワ 1 世の宮廷も「vins de Tournon」を購入**
- **1560 年頃**の J. PELISSON（Tournon 学寮長）の手稿は「**Medves（Mauves）と Tournon の土地ほど繊細で美味なワインの穫れる所はない**」と記す
- **1776 年の勅令**で王国内のワイン自由流通が実現 → **ヴィクトル・ユゴー『レ・ミゼラブル』（1862）に「vins de Mauves」への言及がある**（INAO が明記）
- **1980 年代**、区画境界の大改訂で **6,800 ha → 3,400 ha へ半減**。斜面畑の再征服が目的
- **2009 年時点で約 1,000 ha 植栽・平均年産 35,000 hl**。**2010 年時点で赤が 90%、白が 10%**

---

## Location

| | |
|---|---|
| **Country** | France ✅生✅公 |
| **Region** | Vallée du Rhône septentrionale（北ローヌ）🔍 canonical `region = Rhône` |
| **Village** | **Mauves（アルデッシュ県、07300）— ローヌ右岸** ✅生✅公 |
| **登記住所** | **37 avenue Saint-Joseph, 07300 Mauves**（siège social・活動地・販売地）✅公 |
| **座標（Agence Bio 登録）** | 45.0400, 4.8301 ✅公 |
| **別法人の所在** | **JL CHAVE SELECTION は 1 rue des Mûres, 07300 Mauves**（同じ村の**別住所**）✅公 |

### 🔴 ここが staff にとって最重要の地理事実（✅公 INAO）

**ドメーヌは「エルミタージュの丘の上」には無い。丘は川の向こう側である。**

| | Hermitage AOC | Domaine J-L Chave |
|---|---|---|
| 岸 | **ローヌ左岸** | **右岸** |
| 県 | **ドローム県** | **アルデッシュ県** |
| コミューン | **Tain-l'Hermitage / Crozes-Hermitage / Larnage の 3 つのみ** | **Mauves** |

→ ✅公 **これは違反ではない。** Hermitage AOC の **aire de proximité immédiate（醸造・仕上げの例外区域）**に
**Mauves が明記されている**（アルデッシュ県分のリストに `Mauves`）。つまり
**「Mauves で仕込む Hermitage」は AOC が法的に認めた形**である。
逆向きも同じで、**Saint-Joseph AOC の aire de proximité immédiate には Tain-l'Hermitage が入っている。**

### Key Vineyards

🔴 **公式に確認できる畑名は「ゼロ」である。** 公式サイトに畑のページが無い。

⚠️ **リューディ名を Chave のものとして挙げてはならない。**
`Les Bessards` `Le Méal` `Péléat` `Clos Florentin` `Bachasson` などの名は
**棄却した商用サイト（jeanlouischave.com＝Amazon アフィリエイト）に載っているだけ**で、
**公式にも公的資料にも Chave との結びつきの記載が無い。**（同サイトは "Péléat monopole" とまで書いているが、
**モノポールであることを示す一次資料は存在しない**。）→ §Staff Notes の禁止リスト。

### アペラシオンの地質（✅公 INAO。**staff が語ってよい範囲**）

**Hermitage の丘** — ローヌが**トゥルノンの山塊から切り離した花崗岩の断片**であり、ドローム県の中で孤立した島をなす。
南端の **Pierreaiguille の岩（標高 335 m）**が西の境。
- **西側**＝一次生成の花崗岩、その上に**雲母片岩と片麻岩**。風化して**砂質粘土質の脆い «arène granitique»** に
- **東側**＝第四紀の**古い河岸段丘**（アルプス由来の diluvium）が重なり、末期に**北からの強風が石灰質のレスを堆積**させた。レスは侵食を免れた丘上の平坦部にのみ残る
- 丘は**谷軸に対して直角**を向き、切り立った斜面が北風を遮って**非常に暑いメゾクリマ**を生む。
  **«Les Beaumes» 地区にはオリーヴの遺存木**があるほど。**春の霜害リスクは排除される**
- 🔍✅公 **シラーは主に西側の花崗岩部分に、白品種（主にマルサンヌ）はより石灰質の土壌に**植えられる

**Saint-Joseph** — 気候は現地で「Lyonnais」と呼ばれる大陸性で、ローヌ谷を遡る地中海の影響が末端で届く。
支配的な北風 **«Bise»** は冷たく乾き、**葉を乾かして病害を抑える一方、成熟には不利**。
だから**風から守られた日照の良いニッチ**が選ばれる。
- ✅公 **Mauves と Glun の «granites porphyroïdes» 由来の土壌がシラーの一等地として名指しされている。**
  これは **Chave の本拠地そのもの**である
- 石垣は現地で **«Cheys»** と呼ばれる

---

## Farming

### 🔴 有機認証 — **公的一次資料で確定した。本ドシエ最大の成果。**

✅公 **Domaine Jean-Louis Chave は有機（AB / Biologique）認証を取得している。**

| 項目 | 内容 |
|---|---|
| **認証機関** | **BUREAU ALPES CONTRÔLES（コード FR-BIO-15）**、3 impasse des Prairies, 74940 Annecy-le-Vieux |
| **証明書番号** | **FR-BIO-15.250-0061897.2025.001**（EU 規則 2018/848 第 35 条 1 項に基づく証明書） |
| **有効期間** | **2025-05-15 〜 2026-09-30**（発行 2025-08-07） |
| **engagement 日** | **2016-02-04**（Agence Bio 登録の `datePremierEngagement`。**＝転換の起点**） |
| **認証状態** | `ENGAGEE`（停止・中止の日付なし） |
| **活動区分** | **Production（生産）＋ Préparation（醸造・仕込み）** |
| **認証製品** | **`Hermitage` = Biologique** ／ **`Saint Joseph` = Biologique** ／ `Raisin de cuve` = Biologique **および 転換中** ／ `Jachère`（休閑地）= Biologique |
| **Agence Bio 番号** | `numeroBio` 129760 |
| **認定** | 認証機関は **COFRAC** 認定（5-0539） |

🔴 **一部の区画は今も転換中である。** Agence Bio の生産区分に
**`Raisin de cuve` が AB（認証済）と同時に C2・C3（転換 2 年目・3 年目）でも登録されている**（管理年度 2025）。
証明書側も「production biologique, sauf durant la période de conversion」と
「production durant la période de conversion」の**両方**を記載している。
→ **「全区画が認証済み」とは言えない。「認証済みの区画と転換中の区画が併存する」が正しい。**

❓ **未確認**: ①どのヴィンテージからラベルに AB／ユーロリーフを表示しているか
②転換中の区画がどの畑・どのアペラシオンか ③2016 年以前の栽培方針。

⚠️ **ビオディナミではない。** Demeter・Biodyvin いずれの認証も、公的登録にも公式サイトにも**記載が無い。**
「ビオディナミ」と言ってはならない。**言ってよいのは「有機（AB）認証」まで。**

### 法定要件として確実に言えること（✅公 INAO。**Chave 固有の実践ではなく、守る義務のあるルール**）

| | **Hermitage** | **Saint-Joseph** |
|---|---|---|
| **収穫** | **手摘みが義務**。**房を丸ごとの状態で醸造所へ運ぶことが義務** | **手摘みが義務** |
| **植密度** | **最低 6,000 本/ha**。畝間 2.0 m 以下、株間 0.8 m 以上 | **植付時最低 4,500 本/ha**、1 株あたり最大 2.30 m² |
| **仕立** | **échalas（棒仕立て、高さ 1.50 m 以上）または「palissage plan relevé」** | — |
| **剪定** | **1 株最大 9 芽**。短梢（gobelet / cordon de Royat）または Guyot 単・双 | — |
| **収量** | **赤 40 hl/ha ／ 白 45 hl/ha**（butoir はいずれも 46） | **40 hl/ha**（butoir 46、**50 超で全収穫が AOC 権利喪失**） |
| **最低自然アルコール** | 赤 10.5% ／ 白 11%（vin de paille 19.5%） | **10.5%** |
| **除草** | **9/1〜2/1 は、耕耘か、薬剤を精密に局所散布できる機材のみ** | — |
| **灌漑** | 条件付き許可。**固定灌漑設備・スプリンクラー・点滴はすべて禁止** | — |
| **土壌保全** | **石垣・段々畑・法面（murets, terrasses, banquettes）の維持が義務**。構造を実質的に変える工事は禁止 | 同種の段々畑（«Cheys»）を前提 |
| **品種制限** | — | 🔴 **シラーのクローン 73 / 99 / 301 / 381 / 382 / 383 と台木 110 Richter の植栽が禁止**（2011-08-01 以降の植栽に適用） |

---

## Winemaking

🔴 **Chave 固有の醸造情報は、公式・公的いずれの一次資料にも存在しない。**
発酵容器・全房比率・酵母・新樽比率・熟成期間・樽材・SO2 — **すべて ❓。**
公式サイトにワインのページが無く、**テクニカルシート PDF も存在しない**（本日確認）。

⚠️ **「複数のリューディをアッサンブラージュする」という説明は、Chave について公式に裏が取れていない。**
INAO が書いているのは**アペラシオン一般の話**であって、Chave 個別の話ではない:

> ✅公 「エルミタージュの畑は、区画が画定区域全体に散在する多数の所有者によって耕作されている。
> このため造り手たちは、土壌の**多様性よりも相補性**を重視するようになる。」（INAO, Hermitage CDC）

→ **語ってよい形**: 「エルミタージュでは畑が細かく散らばっているので、**造り手は複数の土壌を組み合わせるのが常道**です」
→ **語ってはいけない形**: 「Chave は Bessards と Méal と Péléat をブレンドしています」（❓ 一次資料なし）

### 法定要件として確実に言えること（✅公 INAO。**この 2 アペラシオンのワインすべてに適用される**）

**Hermitage**
- **赤はシラー 85% 以上**。マルサンヌ・ルーサンヌが補助品種で、**シラー畑への混植は株数の 15% まで**。
  **赤白を混ぜて造る場合もこの比率を守った「ブドウの段階でのアッサンブラージュ」**として行う
- **白はマルサンヌとルーサンヌのみ**
- 🔴 **赤は瓶詰時点でリンゴ酸 0.4 g/L 以下**が義務 → **実質的にマロラクティック発酵を通すことが法定**
- **残糖は 3 g/L 以下**（自然アルコール 14% 超なら 4 g/L 以下）→ **辛口であることが法定**
- 🔴 **木片（オークチップ）の使用は禁止**
- 🔴 **連続式プレスは禁止**
- 補糖後の総アルコールは**白 14% / 赤 13.5% を超えられない**
- 醸造タンク容量は「収量 × 面積」の **0.8 倍以上**を保有する義務
- **コルクは長さ 44 mm 以上**。⚠️ 2010 年の改正案では**「凝集コルク禁止」「ヴィンテージの刻印」**も提示されたが、
  2024 年版の本文では**長さ 44 mm 以上のみが残っている**。**両方の版を保存してある**（§Sources）
- **`vin de paille`（藁ワイン）が認められている**唯一の北ローヌ AOC。白のみ。**最低 45 日の陰干し**、
  圧搾時**糖度 350 g/L 超**、収量 **15 hl/ha**、取得アルコール 12.5% 以上。生産量は「confidentielle」
  ❓ **Chave が vin de paille を造っているかは未確認。**

**Saint-Joseph**
- **赤はシラー 90% 以上**（Hermitage より 5 ポイント厳しい）。補助品種の混植は **10% まで**
- **白はマルサンヌとルーサンヌ**
- ✅公 **ラベルに地籍リューディ名を表示してよい**（収穫申告に記載があることが条件）。
  **「Cru des Côtes du Rhône」「Vignobles de la Vallée du Rhône」の上位地理表示も可**

---

## Style

🔴 **Chave のハウススタイルを記述した公式・公的資料は存在しない。**
第三者評価・点数も、**公式ソース規律により本書では一切採用しない。**

以下は **✅公 INAO がアペラシオン単位で公式に記述している味わい**である。
**「この造り手はこうだ」ではなく「このアペラシオンはこう定義されている」として語ること。**

| ワイン | INAO の公式記述 |
|---|---|
| **Hermitage 赤** | シラー主体。**濃い色調**、豊かで表現力に富む複雑な香り（**完熟果実・スパイス・下草**）。口中は**力強くタンニックで、それが良い熟成能力を与える** |
| **Hermitage 白** | **強大な香りの力**（**白い花・スパイス・蜂蜜**）。**酸とある種の «moelleux»（まろやかさ）の繊細な均衡**。ただし**発酵性糖は残さない** |
| **Hermitage vin de paille** | **琥珀色**、甘味、高いアルコール、複雑で強い香り。**砂糖漬け果実**が支配し、**燻香・エキゾチックフルーツ・ヴァニラ・蜂蜜**を伴う |
| **Saint-Joseph 赤** | **エレガンスとフィネス**に強く刻印された芳香（**果実・スパイス・リコリス・下草**）。口中は**タンニンのビロード感が追求される**。石灰質土壌由来のものは**タンニンがより素朴で、時間をかけて洗練される** |
| **Saint-Joseph 白** | 辛口で非常に香り高い。**蜜を思わせる白い花**が広く現れ、口中は**«gras»（豊満さ）が支える独特の均衡** |

🔍 構造上ほぼ確実に言える 3 点（法定要件からの機械的帰結。**推測ではない**）
1. **Hermitage 赤も Saint-Joseph 赤も、法定でシラーが 85%／90% 以上**。「シラーのワイン」と言い切ってよい
2. **Hermitage 白はマルサンヌとルーサンヌのみ**。「シャルドネ」等は法的にあり得ない
3. **Hermitage 赤は法定で辛口かつマロ通過**（リンゴ酸 0.4 g/L 以下・残糖 3 g/L 以下）

---

## Important Cuvées

### 🔴 OBP 掲載 11 本 — **色の内訳を確定した**（🔍 OBP メニュー行データより）

**メニューは「Hermitage」としか印字しない。赤か白かは、載っている節でしか分からない。**

| # | 色 | ワイン | OBP 印字 | 節 | ヴィンテージ | 価格 | canonical |
|---|---|---|---|---|---|---|---|
| 1 | **白** | **Hermitage Blanc** | `Hermitage` | **FRANCE \| WHITE > RHÔNE** | **2023** | **$1,400** | ⚠️ 白の専用レコード無し |
| 2 | **白** | Hermitage Blanc | `Hermitage` | WHITE > RHÔNE | **2022** | $1,400 | ⚠️ 同上 |
| 3 | **白** | Hermitage Blanc | `Hermitage` | WHITE > RHÔNE | **2021** | $1,400 | ⚠️ 同上 |
| 4 | **白** | Hermitage Blanc | `Hermitage` | WHITE > RHÔNE | **2020** | $1,400 | ⚠️ 同上＋**VT 未登録** |
| 5 | **白** | Hermitage Blanc | `Hermitage` | WHITE > RHÔNE | **2019** | **$960**（最安の Hermitage） | ⚠️ 同上＋**VT 未登録** |
| 6 | **白** | Hermitage Blanc | `Hermitage` | WHITE > RHÔNE | **2013** | **$1,480**（**最高価格**） | ⚠️ 同上＋**VT 未登録** |
| 7 | **赤** | **Hermitage Rouge** | `Hermitage` | **FRANCE \| RED > RHÔNE** | **2023** | $1,400 | **登録済** `cuvee:domaine-jean-louis-chave-hermitage` |
| 8 | **赤** | Hermitage Rouge | `Hermitage` | RED > RHÔNE | **2022** | $1,400 | **登録済** |
| 9 | **赤** | **Saint-Joseph** | `Saint-Joseph` | RED > RHÔNE | **2023** | **$440** | **登録済** `cuvee:domaine-jean-louis-chave-saint-joseph` |
| 10 | **赤** | Saint-Joseph | `Saint-Joseph` | RED > RHÔNE | **2022** | $400 | **登録済** |
| 11 | **赤** | Saint-Joseph | `Saint-Joseph` | RED > RHÔNE | **2021** | $400 | **登録済** |

**内訳: Hermitage 白 6 本 ／ Hermitage 赤 2 本 ／ Saint-Joseph 赤 3 本 = 11 本。**
**生産者の印字はすべて `Jean Louis Chave`**（`Domaine` 無し・ハイフン無し）。

🔴 **2022 と 2023 は、白と赤が同じ「Hermitage」・同じ $1,400 で、両方の節に載っている。**
つまり **印字・ヴィンテージ・価格がすべて一致し、節だけが違う 2 本ずつ**が存在する。
**現場で取り違えが起きうる構造。** → §Staff Notes。

🔍 **canonical との差分**
- canonical のキュヴェは **`Hermitage`（1 件）と `Saint-Joseph`（1 件）だけ**で、
  **`Hermitage` レコードの `facts.color` は `"Rouge"`**。**白のためのレコードは存在しない。**
  → **OBP の白 6 本が、色が「Rouge」と記録されたキュヴェにぶら下がっている**（intake は `cuvee_state=exact`）
- canonical のヴィンテージは Hermitage / Saint-Joseph とも **2021・2022・2023 のみ**。
  → **Hermitage の 2020・2019・2013（すべて白）は canonical に存在しない**（3 本）
- Saint-Joseph は **3 本すべてが canonical と一致**（色も Rouge で正しい）

### 公式サイトのメタデータが名を挙げているもの（✅生 だが**編集文ではなく SEO メタ情報**）

公式サイトの `<title>` と meta には次の語が並ぶ:
`Hermitage` / `Côtes du rhône` / `Saint Joseph` / `Mauves` / `Hermite` / `Ermite` / **`Cuvée Cathelin`** / `Gérard Chave`

- **`Cuvée Cathelin`** — **生産者自身のドメインのメタデータに現れる**ので、**名称の実在は確認できる**。
  ❓ **それ以外は一切不明**（造られる年の条件・生産量・命名の由来・現行有無）。OBP には無い。
  🔴 **由来や生産条件を語ってはいけない。**
- **`Hermite` / `Ermite`** — 🔍 これは**キュヴェ名ではなく AOC 名の綴り違いである可能性が高い**。
  ✅公 INAO の CDC 正式名称は「**Hermitage ou l'Hermitage ou Ermitage ou l'Ermitage**」で、
  **H の有無を含む 4 綴りが公式に等価**とされている。**「Chave が Ermite というワインを造っている」と言ってはならない。**
- **`Côtes du rhône`** — ❓ **公式サイトのメタに載っているが、ドメーヌの CDR なのか、
  別法人 JL Chave Sélection の CDR «Mon Coeur» を指しているのか判別できない。**（後者は canonical に登録済み）
  🔴 **「ドメーヌはコート・デュ・ローヌも造っている」と断定しない。**

---

## Staff Notes

> この節は上記の ✅生 / ✅公 / 🔍 からのみ構成している。**裏の取れていない事柄は一切書いていない。**
> **この生産者は記述が薄い。だから「言ってよいこと」より「言ってはいけないこと」の方が重要である。**

**一行で言うと** — 「**1481 年から父から子へ**と続く、アルデッシュ県マーヴの家。
**エルミタージュの丘の対岸**に蔵があり、**有機認証を取得している**」。

### ゲストへの説明の芯（3 点）

**1. 「1481 年から、父から子へ」。これは造り手自身の言葉である。**
公式サイトに書かれているのは、実質この 1 行だけ —
**«Vignerons de père en fils depuis 1481»**。家族の持株会社の登記名も **「CHAVE 1481」**。
**1481 という年号は、家族自身が今も使っている。**
🔴 **ただし「◯代目」という数字は絶対に言わない**（次項参照）。

**2. 蔵は丘の上ではなく、川の向こう側にある。それが由緒でもある。**
エルミタージュの丘は**ローヌ左岸・ドローム県**の Tain-l'Hermitage など 3 コミューンだけ。
Chave の蔵は**右岸・アルデッシュ県の Mauves**。
これは AOC が認めた形で、**Hermitage AOC の「醸造の例外区域」に Mauves が名指しで入っている**。
そして **Mauves は Saint-Joseph の歴史の中心**でもある —
- **「Saint-Joseph」という名前自体が、対岸トゥルノンの一区画の地名**で、
  **その畑を隣村マーヴの栽培家が耕していた**ことが命名理由の一つ
- **17 世紀、トゥルノンのイエズス会が「マーヴとトゥルノンのワイン」を指してこの名を使っていた**
- **1560 年頃の記録**に「**マーヴとトゥルノンの土地ほど繊細で美味なワインが穫れる所はない**」とある
- **ヴィクトル・ユゴーの『レ・ミゼラブル』（1862）に「vins de Mauves」が出てくる**（INAO が公式に記載）
- 中世、この地のワインは「**vins de l'Hermitage**」とも「**vins de Mauves**」とも呼ばれていた
→ **「対岸だから格下」ではない。両岸は同じ歴史の表と裏である。**

**3. 有機認証を取得している。ここは自信を持って答えてよい。**
- 認証機関 **Bureau Alpes Contrôles（FR-BIO-15）**、証明書 **2025 年 5 月 15 日〜2026 年 9 月 30 日** 有効
- **2016 年 2 月**に有機への取り組みを登録
- **エルミタージュとサン＝ジョゼフの両方が「Biologique」として認証製品に載っている**
- 🔴 **ただし「全部の畑が認証済み」とは言わない。転換中の区画が併存している**（公的登録に C2・C3 の記載あり）
- 🔴 **「ビオディナミ」とは絶対に言わない。**その認証は無い

### 🔴 リストで最も気をつけること — **エルミタージュが白と赤で「まったく同じ表記」で並んでいる**

| 節 | 印字 | VT | 価格 |
|---|---|---|---|
| **WHITE > RHÔNE** | `Hermitage` | **2023** | **$1,400** |
| **RED > RHÔNE** | `Hermitage` | **2023** | **$1,400** |
| **WHITE > RHÔNE** | `Hermitage` | **2022** | **$1,400** |
| **RED > RHÔNE** | `Hermitage` | **2022** | **$1,400** |

**印字・ヴィンテージ・価格がすべて同一。違うのは載っている節だけ。**
→ **オーダーを受けたら、必ず「白のエルミタージュでよろしいですか／赤でよろしいですか」と口頭で確認する。**
→ **セラーから出すときも、ゲストに見せる前にボトルの色を確認する。**

**リストの構成として言えること（🔍）**
- **Chave のエルミタージュは白が 6 本、赤が 2 本。白の方が厚い。** 白は 2013 まで縦に揃っている
- **最高価格は 2013 の白 $1,480**、**最安は 2019 の白 $960**
- **サン＝ジョゼフは赤 3 本のみ**（$400〜$440）。**エルミタージュとは 3 倍以上の価格差**
- **白のエルミタージュを勧めやすい店である。**「白のエルミタージュはマルサンヌとルーサンヌだけで造られ、
  法律上シャルドネなどは一切入りません」と言い切れる

### 品種・造りを聞かれたら（法定要件だけで答える）

- **「エルミタージュの赤は法律でシラーが 85% 以上。サン＝ジョゼフはさらに厳しく 90% 以上です」** ✅公
- **「エルミタージュの白はマルサンヌとルーサンヌのみです」** ✅公
- **「エルミタージュもサン＝ジョゼフも、収穫は手摘みが法律で義務づけられています」** ✅公
- **「エルミタージュは房を丸ごと醸造所へ運ぶことまで規定されていて、連続式プレスも木片の使用も禁止です」** ✅公
- **「エルミタージュの赤は瓶詰時のリンゴ酸が 0.4 g/L 以下と決まっていて、実質マロを通すことが法定です」** ✅公
- **「収量は赤 40、白 45 hl/ha が上限です」** ✅公
- 🔴 **これらは「AOC の決まり」として言うこと。「Chave はこうしている」と言い換えない。**

### 畑・丘の話が要るとき（アペラシオンの話としてなら安全）

- **エルミタージュの丘は、ローヌがトゥルノンの山塊から削り取った花崗岩の断片**。ドローム県の中の孤島 ✅公
- **西側は花崗岩＋雲母片岩・片麻岩が風化した砂質粘土（arène）、東側は古い河岸段丘＋北風が運んだレス** ✅公
- **谷に直角を向いた急斜面が北風を遮り、非常に暑いメゾクリマを生む。«Les Beaumes» にはオリーヴの遺存木が残る。春霜のリスクは無い** ✅公
- **エルミタージュは 2009 年時点で全部で 137 ha しかない**（協同組合 1・ネゴシアン 7・自家蔵 17）✅公
- **サン＝ジョゼフでは、マーヴとグランの «granites porphyroïdes» がシラーの一等地として INAO に名指しされている**（＝Chave の地元）✅公
- **サン＝ジョゼフは 1980 年代に区画を 6,800 ha から 3,400 ha へ半減させて、斜面畑を取り戻した** ✅公

### ⚠️🔴 現時点で言ってはいけないこと（**この生産者では、ここが本体である**）

**A. 人物・世代について**
1. 🔴 **「◯代目」と言わない。**「16 代目」等の数字は**商用サイトにしか無い**。公式は世代数を示していない
2. 🔴 **「ジェラール・シャーヴが今も造っている」と言わない。**公式に現況の記載が無い。
   **逆に「亡くなった」とも言わない。**登記上の代表者は **Jean-Louis Chave（1968 年生）**とだけ言う
3. **「1992 年に当主が就任した」等の年号を言わない。**公式に無い

**B. 畑・キュヴェについて**
4. 🔴 **`Les Bessards` `Le Méal` `Péléat` `Clos Florentin` `Bachasson` を Chave の畑として挙げない。**
   一次資料が無い。**「Péléat はモノポール」は特に危険**（出典は Amazon アフィリエイトサイトのみ）
5. 🔴 **「Chave は複数のリューディをブレンドしている」と断定しない。**
   言ってよいのは **「エルミタージュでは区画が散在するので、造り手は土壌を組み合わせるのが常道」**まで（INAO の一般記述）
6. 🔴 **「Cuvée Cathelin」の由来・生産される年の条件・生産量を語らない。**
   名称が公式サイトのメタ情報にある、という以上のことは分かっていない
7. 🔴 **「Chave は Ermite というワインを造っている」と言わない。**
   `Ermite`/`Hermite` は **AOC の公式綴り違い**（Hermitage / l'Hermitage / Ermitage / l'Ermitage）である可能性が高い
8. **「ドメーヌはコート・デュ・ローヌも造っている」と断定しない。**別法人の可能性がある（下記 D）

**C. 栽培・醸造について**
9. 🔴 **「ビオディナミ」と言わない。**認証が無い
10. 🔴 **「昔から有機」と言わない。**公的登録上の起点は **2016 年 2 月**
11. 🔴 **「全区画が有機認証済み」と言わない。**転換中（C2・C3）の区画が併存している
12. **新樽比率・熟成期間・全房比率・酵母・発酵容器を言わない。**一次資料が 1 件も無い
13. **「◯年は造られなかった」等のヴィンテージ判断を言わない**

**D. 別法人との混同**
14. 🔴 **`Jean-Louis Chave Sélections` は別法人である。**
    **JL CHAVE SELECTION**（SIREN `408501450`、**SAS**、NAF `46.34Z` 飲料卸、
    所在地 **1 rue des Mûres**、代表 **Erin Chave（1971 年生）**）。
    ドメーヌ（SIREN `379077795`、NAF `01.21Z` ブドウ栽培、37 avenue Saint-Joseph、代表 Jean-Louis Chave）とは
    **住所も業種も代表者も違う。** **同じワインの別ラベルではない。**
15. ⚠️ **THÉSEUS のアプリ側に、Chave Sélections についての未検証の記述が入っている。**
    canonical の `obp_note` / `description` に「**1995 年創業の négoce アーム**」「**Offerus は洗礼前の聖クリストフォロスの名**」
    「リュット・レゾネ」「自然酵母」「12〜14 ヶ月熟成」等が書かれているが、
    **これらは legacy_app 由来（confidence 0.2）で、公式に裏が取れていない。**
    ⚠️ **公的登記上、JL CHAVE SELECTION の法人設立は 1996-08-01 であり、DB の「1995 年創業」とは一致しない。**
    🔴 **アプリの記述をそのまま読み上げない。**

---

## Akio's Insight

*（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）*

---

## Canonical Conflict

**2 件。うち 1 件は登録済み（P-7）、1 件は新規。**

### ① `producer:domaine-jean-louis-chave` / `producer:jean-louis-chave-selections` → **既出。REGISTER.md `P-7` を参照**

**重複して書かない。** `research/canonical_conflicts/REGISTER.md` の **P-7** に登録済みで、
判断は「**統合禁止。ただし『同一家族の複数ブランドをどうモデル化するか』という共通課題（同 §「この登録票の扱い」1）として一括処理すべき**」。

🔴 **本ドシエは P-7 の「重複ではない」という判断を、公的登記で補強する新証拠を得た。**
両者は **別の法人**である:

| | Domaine | Sélections |
|---|---|---|
| 登記名 | DOMAINE JEAN LOUIS CHAVE | JL CHAVE SELECTION |
| SIREN | `379077795` | `408501450` |
| 法人設立 | **1990-07-01** | **1996-08-01** |
| NAF | **`01.21Z` ブドウ栽培** | **`46.34Z` 飲料卸** |
| 住所 | 37 avenue Saint-Joseph, Mauves | **1 rue des Mûres, Mauves** |
| 代表 | **Jean-Louis Chave**（gérant） | **Erin Chave**（président de SAS） |
| 有機活動区分 | **Production ＋ Préparation** | **Préparation のみ** |
| 有機証明書 | FR-BIO-15.250-**0061897**.2025.001 | FR-BIO-15.250-**0100237**.2025.001 |

→ **統合してはならない。** この証拠を **P-7 に追記することを推奨する**（REGISTER.md は編集していない）。

### ② 🆕 **`cuvee:domaine-jean-louis-chave-hermitage` が、赤と白の 2 製品を 1 レコードで表している**

🔴 **これは「重複レコード」ではない。逆に「1 レコードが 2 つの製品を吸収している」過少特定である。**
（色違いを別レコードとして誤検出する類型 — REGISTER.md §C — とは**向きが逆**であることに注意。）

**① 衝突している canonical ID**
- `cuvee:domaine-jean-louis-chave-hermitage`（`producer_id = producer:domaine-jean-louis-chave`、
  `facts.subregion = "Hermitage"`、**`facts.color = "Rouge"`**、`facts.serving_temp = "16–18°C"`、
  `facts.glassware = "Burgundy"`、vintages = 2021 / 2022 / 2023）
- **対応する白のレコードは存在しない。**

**② なぜ衝突か**
✅公 INAO の cahier des charges により、AOC「Hermitage」は **白と赤の両方**に与えられる
（赤＝シラー 85% 以上、白＝マルサンヌ＋ルーサンヌ）。**まったく別の製品**である。
canonical はこれを **`color: "Rouge"` を持つ単一レコード**で表しており、**白を表現する手段が無い。**

**③ Evidence**
🔍 OBP メニュー行データに、**同一生産者・同一印字 `Hermitage` が 2 つの節に分かれて存在する**:
- `FRANCE | WHITE > RHÔNE` — 2023 / 2022 / 2021 / 2020 / 2019 / 2013（**6 本**）
- `FRANCE | RED > RHÔNE` — 2023 / 2022（**2 本**）

**2022 と 2023 は白・赤とも $1,400 で同額**、印字も同一。
intake は 8 本すべてを `cuvee_state=exact` として**この 1 レコードに解決している**
（batch1 の `flags` に `cross_section_duplicate` が立っているのが唯一の痕跡）。
→ **色が「Rouge」と記録されたキュヴェに、白 6 本がぶら下がっている。**

**④ OBP への影響**
🔴 **11 本中 6 本（55%）が、色の誤った実体に紐づいている。**
さらに **白の 2020・2019・2013 の 3 ヴィンテージは canonical に一切存在しない**
（canonical の vintage は 2021/2022/2023 のみ）。
実害の質が P-1 と異なり、**現場のサービスに直結する** — アプリが「Rouge / 16–18°C / Burgundy グラス」を
返すため、**白を注文したゲストに赤の供出温度とグラスが案内されうる。**
Saint-Joseph 側（3 本）は色が Rouge で正しく、実害は無い。

**⑤ 推奨される解決策（実行しない）**
以下は**どれも architecture の判断**であり、research では動かさない。
- (a) `cuvee:domaine-jean-louis-chave-hermitage-blanc` を新設し、白 6 本を移す
- (b) キュヴェ名に色を含めるか（`Hermitage Blanc`）、`facts.color` を必須の識別軸に昇格させるか
  → **REGISTER.md の共通課題 2「キュヴェ名に格付け語・アペラシオンを含めるか」と同じ命名規約の問題**
- (c) matcher 側で、**OBP の節（WHITE/RED）を照合キーに含める**。現状は節が捨てられており、
  `cross_section_duplicate` フラグを立てるだけで解決先を分けていない
🔴 **同種の問題は Chave 固有ではない。** 赤白双方を持つ AOC（Hermitage / Crozes-Hermitage /
Saint-Joseph / Châteauneuf-du-Pape 等）で**同型の衝突が横断的に存在する可能性が高い**ため、
個別修正ではなく**規約として一括で決めるべき**。

**⑥ Confidence: High**
（INAO CDC で赤白両方の存在を確認済み・canonical の `color: "Rouge"` を実読・
OBP の節分岐 6/2 を行データで実測。）

🔴 **`research/canonical_conflicts/REGISTER.md` への追記が必要**（新規 `C-4` 相当）。
**REGISTER.md 自体は本作業で編集していない。**

---

## Sources

### 一次資料 A — 生産者公式サイト ✅生（2026-08-04 に再取得して現況確認）

`http://www.domainejlchave.fr/` — **全 1 ページ。これがサイトの全部である。**

| 取得物 | 得られた事実 |
|---|---|
| `official_domainejlchave-fr_home_20260804.html` | **«Vignerons de père en fils depuis 1481»**、**«Mauves en Ardèche - France»**、meta に `Hermitage` `Côtes du rhône` `Saint Joseph` `Mauves` `Hermite` `Ermite` `Cuvée Cathelin` `Gérard Chave` |
| `Exe_site-Chave.png` | ヘッダ画像。**«DOMAINE JEAN-LOUIS CHAVE / Vignerons de père en fils depuis 1481»** |
| `Exe_site-Chave2.png` | 2 枚目。**«MAUVES EN ARDÈCHE - FRANCE»** |
| `official_jlchaveselection-com_20260804.html` | `http://www.jlchaveselection.com/` — 本文は **«En cours de réalisation.» のみ** |

🔴 **確認済みの「無いもの」**（次の担当者が再調査しなくてよいように明記する）
- ナビゲーション・内部リンク: **0 本**（HTML に `<a>` が 1 つも無い）
- history / vineyards / winemaking / sustainability / wines / the estate / press / contact の各ページ: **存在しない**
- **テクニカルシート PDF・fiche technique: 0 件**。Louis Latour の `/pdf/en/*.pdf` に相当するものは無い
- サイトは **HTTP のみ**（HTTPS は TLS エラーで到達不能。ツールが HTTPS に昇格すると取得できない）

### 一次資料 B — 公的機関 ✅公（2026-08-04 取得）

| 取得物 | 発行元 | 得られた事実 |
|---|---|---|
| `attestation_bio_domaine_A03M160E.pdf` / `attestation_bio_domaine.txt` | **Bureau Alpes Contrôles**（EU TRACES 公開） | 証明書 **FR-BIO-15.250-0061897.2025.001**、有効 **2025-05-15〜2026-09-30**、活動 Production＋Préparation、**認証製品に `Hermitage` `Saint Joseph` = Biologique**、`Raisin de cuve` は Biologique と 転換中の両方、COFRAC 認定 5-0539 |
| `attestation_bio_selection_A03M247H.pdf` / `attestation_bio_selection.txt` | 同上 | **JL CHAVE SELECTION** の証明書 **FR-BIO-15.250-0100237.2025.001**、活動 **Préparation のみ**、住所 **LE VILLAGE, 07300 Mauves** |
| `agencebio_chave_20260804.json` | **Agence Bio**（公的登録） | `numeroBio` 129760、**`datePremierEngagement` 2016-02-04**、状態 `ENGAGEE`、生産区分に **AB / C3 / C2 が併存**、住所 37 avenue St Joseph、座標 45.0400/4.8301。**JL CHAVE SELECTION は `numeroBio` 62920・区分 Grossistes・gérant `CHAVE Erin`** |
| `sirene_chave_20260804.json` | **INSEE / recherche-entreprises（data.gouv）** | SIREN 379077795、法人設立 **1990-07-01**、NAF `01.21Z`、代表 **Jean-Louis Chave（1968-08 生）**、無限責任社員に **CHAVE 1481**、`tranche_effectif_salarié` 12（2023） |
| `sirene_jlchaveselection_20260804.json` | 同上 | SIREN 408501450、法人設立 **1996-08-01**、NAF `46.34Z`、**SAS**、代表 **Erin Chave（1971-01 生）**、住所 1 rue des Mûres |
| `sirene_chave1481_poissonrouge_20260804.json` | 同上 | **CHAVE 1481**（SIREN 890534431、**2020-11-02** 設立、NAF `64.20Z` 持株会社、président Jean-Louis Chave）／ **POISSON ROUGE**（SIREN 941000234、**2025-01-23** 設立、NAF `68.20B`、同一住所） |
| `PNO2024AOPHermitage.pdf` / `herm.txt` | **INAO**（2024-06-25 全国委員会） | Hermitage CDC 全文 — 品種・比率・収量・仕立・収穫・醸造禁止事項・vin de paille・**地質と歴史（Stérimberg 伝説の «apocryphe» 認定を含む）**・137 ha |
| `PNOCDCAOC-Hermitage.pdf` / `herm_extrait.txt` | **INAO**（2010-09-09 常任委員会） | ⚠️ **旧改正案**。「凝集コルク禁止」「**ヴィンテージの刻印**」「ガラス瓶のみ」の条項を含む。**2024 年版には残っていない**ため、**両版を保存**して食い違いを可視化 |
| `PNO2023SaintJoseph.pdf` / `sj.txt` | **INAO**（2023-11-30 全国委員会） | Saint-Joseph CDC 全文 — シラー 90%、**禁止クローン 73/99/301/381/382/383・台木 110R**、収量、**命名史（Tournon の地籍名・イエズス会・1312 年の分断・レ・ミゼラブル）**、1980 年代の区画半減、約 1,000 ha |

### 一次資料 C — THÉSEUS 内部 🔍（読み取りのみ・**canonical 無変更**）

- `theseus-phase0@main:migration/out/resolved/wine_makers.json` / `cuvees.json` / `vintages.json`
  → canonical ID・`facts.color`・legacy_ids・保有ヴィンテージを実読
- OBP メニュー行データ（`menu_rows.json`）→ **11 本の色・節・価格・印字を確定**
- `research/canonical_conflicts/REGISTER.md` → **P-7 を先に確認済み。重複記載していない**

### 🔴 棄却したソース（**再発見を防ぐために記録する**）

| ソース | 判定 |
|---|---|
| **`jeanlouischave.com`** | 🔴 **公式ではない。Amazon アフィリエイトサイト。** ページ内に `tag=jeanlouischave` のアフィリエイトタグと "Check Price" ボタン。生産者名を冠した第三者商用ページ。**検索結果では公式サイトのすぐ下に並ぶ。** 取得物を `REJECTED_jeanlouischave-com_amazon-affiliate.html` として保存。**ここに書かれている「16 代目」「Péléat monopole」「Les Bessards」「Clos Florentin」「Bachasson」はすべて出典不明であり、本書では 1 語も採用していない。** |
| 小売店・インポーター・レビュー集約・まとめブログ | **不使用**（ソース規律） |
| 検索結果のスニペット | **不使用。**「16 代目」「1992 年に参画」「フィロキセラ時に Mauves へ移転」等はスニペットにあるが、**いずれも一次資料で確認できなかったため採用していない** |

### 二次資料
**なし。本書は公式サイトと公的機関の一次資料のみに基づく。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **High** | 公式サイト・INSEE・Agence Bio の 3 系統で一致 |
| Overview | **Medium-High** | 事実は確実だが、生産者由来の情報が 1 行しかない |
| History | **Low**（家族）／ **High**（アペラシオン） | 家族史は「1481」以外に一次資料が皆無。アペラシオン史は INAO 全文 |
| Location | **High** | 登記住所・座標・AOC 地理区分がすべて公的資料で確定。**Mauves が Hermitage の aire de proximité immédiate に含まれることも確認済み** |
| **Farming** | **High** | **有機認証を証明書番号・機関・有効期間・engagement 日・転換中区画まで確定。必須項目を満たす** |
| Winemaking | **Low**（Chave 固有）／ **High**（AOC 法定要件） | 固有情報は一次資料が 0 件。法定要件は CDC 全文で確定 |
| Style | **Medium** | INAO のアペラシオン記述のみ。ハウススタイル・第三者評価は無し |
| **Important Cuvées** | **High** | **11 本すべての色・節・VT・価格・canonical 対応を確定。色の取り違えリスクを特定** |
| Canonical Conflict | **High** | P-7 を公的登記で補強、新規衝突をレコード実読で確定 |
| Staff Notes | **High** | すべて上記から構成。**禁止リストが本体** |
| **総合** | 🟡 **Medium — ただし「70% = 現場で間違ったことを言わずに語れる」基準は満たす。** | 必須項目（Identity / Overview / Location / **Farming** / Important Cuvées ＋ OBP 紐付け / Staff Notes 芯 3 点 / **⚠️ 禁止リスト**）はすべて充足。**充足の仕方が Louis Latour と逆で、「語れること」ではなく「語ってはいけないこと」を確定することで達成している。** |

🔴 **canonical 昇格の候補としては不十分。** 生産者固有の Winemaking・History が空であり、
**昇格させても canonical にほとんど書き込む中身が無い。**
昇格より先に、**§Canonical Conflict ② の色分離を architecture 側で決めるべき**である。

---

## Open Questions

**残り 12 件。1・2・3 は staff 運用に直結する。**

1. 🔴 **OBP の Hermitage 白 6 本を canonical 上どう表現するか。**
   現状 `facts.color = "Rouge"` の単一レコードに吸収されており、**白を注文したゲストに赤の供出温度・グラスが案内されうる。**
   → §Canonical Conflict ②。**architecture の判断が要る。**
2. 🔴 **`Cuvée Cathelin` の実体。** 公式サイトのメタ情報に名前があるだけで、他に何も分かっていない。
   OBP には無いが、**ゲストから名前を出される可能性が高い。**現状は「名前は存在する」以上のことを言えない。
3. 🔴 **Gérard Chave の現況。** 公式サイトの meta に名が残るのみ。**存否・役割ともに不明。**
   **Louis Latour で踏んだ地雷と同じ形**なので、確認できるまで語らない。
4. **世代数。** 「1481 年から父子相伝」は公式だが、**何代目かを示す公式記述が無い。**
5. **有機認証の適用ヴィンテージ。** engagement が 2016-02-04 なので、
   転換 3 年を機械的に当てれば 2019 年収穫以降が最初の認証年になるはずだが、**これは推定であり公式確認が要る。**
   **ラベルに AB／ユーロリーフを表示しているかも未確認**（OBP には 2013・2019 の白がある）。
6. **転換中（C2 / C3）の区画がどこか。** アペラシオン別・畑別の内訳が公的登録に出ていない。
7. **ドメーヌの総面積・アペラシオン別の面積。** 公式・公的いずれにも記載が無い。
8. **醸造の一切**（発酵容器・全房・酵母・新樽比率・熟成期間・SO2）。**一次資料が 1 件も無い。**
9. **公式サイトのメタにある `Côtes du rhône` の帰属。** ドメーヌ自身のワインか、
   別法人 JL Chave Sélection の «Mon Coeur» を指しているのか判別できない。
10. **`Hermite` / `Ermite`。** AOC の公式綴り違い（Hermitage / l'Hermitage / Ermitage / l'Ermitage）と解するのが
    最も整合的だが、**キュヴェ名である可能性を完全には排除できない。**
11. **Erin Chave と Jean-Louis Chave の関係。** 登記上は別法人の代表者という事実のみ。**推測しない。**
12. **`POISSON ROUGE`（2025-01-23 設立、NAF `68.20B` 不動産）の目的。**
    同一住所・同じ役員構成だが、**用途は公的登録から読み取れない。**

### 公式サイトが無いことによる構造的な限界

⚠️ **この生産者は、公式サイトが復活しない限り Louis Latour 水準には到達しない。**
残る現実的な一次資料の入手経路は 3 つしかない:
- **①ドメーヌへの直接照会**（ファクトシートの提供依頼）
- **②INAO の追加公式文書**（déclaration de récolte 等は非公開）
- **③生産者自身の刊行物**（存在するか未確認）

**②③は現時点で頭打ちである。** ①は Akio の判断が要る。
