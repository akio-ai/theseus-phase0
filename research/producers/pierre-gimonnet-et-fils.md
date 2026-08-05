# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:pierre-gimonnet-and-fils` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagne-gimonnet.com ／公式 PDF で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本バッチでは不使用**）
> `⚠️` **公式内で食い違い。両方を残す**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 一次資料: `https://www.champagne-gimonnet.com/`
> 参照した公式ページ: `/un-domaine-familial-et-vignerons-avant-tout/` `/un-terroir-unique-chef-doeuvre-de-la-nature/`
> `/un-style-reflet-du-terroir-et-dun-savoir-faire/` `/une-viticulture-respectueuse-du-terroir/`
> `/lart-de-lassemblage/` `/notre-philosophie-du-champagne/` `/brochure-2025/` `/cuvees/` `/boutique/`
> 製品ページ 15 件（`/produit/cuis-1er-cru/` `/produit/cuis-1er-cru-special-club/` `/produit/chouilly-grand-cru/`
> `/produit/cramant-grand-cru/` `/produit/oger-grand-cru/` `/produit/oger-grand-cru-2/` `/produit/special-club/`
> `/produit/millesime-de-collection/` `/produit/oenophile-non-dose/` `/produit/fleuron/` `/produit/gastronome/`
> `/produit/rose-de-blancs/` `/produit/brut-extra/` `/produit/mono-terroir-grand-cru/` `/produit/grands-formats/`）
>
> ✅ **公式テクニカルシート（fiche technique）を発見・全件取得済み。** 公式サイトの WordPress メディアに
> **PDF 98 件**が存在する。**OBP 掲載 6 本すべてに対応するシートを取得し `pdftotext` で解析済み**（下記 §Sources）。
> ✅ **公式 Estate Book「BROCHURE 2025」（91 頁 PDF）を全文解析**。これが最新の一次資料であり、
> **サイト本文（2019 年更新のまま）より新しい。数値が食い違う箇所は 2025 ブローシャを採用し、旧値も残す。**
>
> ✅ **第二の一次資料**: Club Trésors de Champagne 公式サイト `clubtresorsdechampagne.com`
> （`/en/le-club-tresors-de-champagne/qui-sommes-nous-2/` `/en/le-club-tresors-de-champagne/les-vignerons-du-club/`）。
> Spécial Club は生産者の自称ではなく**協会の制度**であるため、協会公式を一次資料として併用した。

---

## Identity

| | |
|---|---|
| **Canonical Name** | Pierre Gimonnet & Fils |
| **Aliases** | `Champagne Pierre Gimonnet & Fils` ✅（公式サイト自称）／ `Champagne Pierre GIMONNET et Fils` ✅（**Club Trésors 公式会員一覧の表記。`&` ではなく `et`**）／ `Maison Gimonnet` ✅（2025 ブローシャ内の自称）／ `Pierre Gimonnet et Fils` ✅（公式ページ本文に併存） |
| **業態** | **vigneron（自社畑のみ・ブドウを買わない）** ✅ — 公式明言「**Nous ne sommes pas des négociants**」「**nous n'achetons pas de raisins**」「**Notre vignoble assure 100% de notre approvisionnement**」 |
| **所在** | **1 rue de la République, 51530 Cuis**（Marne / Côte des Blancs）✅ |
| **現経営** | **Olivier Gimonnet ／ Didier Gimonnet — 共同経営（3 代目）** ✅。Michel Gimonnet と Françoise Gimonnet-Larmandier の 4 人の子のうちの 2 人。1980 年代に就農、**「30 年以上」共同で畑と醸造を担当** ✅ |
| **次世代** | **Arnaud Gimonnet ／ Pierre-Guillaume Gimonnet（4 代目）** ✅ — **2025 年ブローシャに署名者として明記**。Arnaud は**醸造コンサルタントとして 10 年の経験**を経て参画 ✅ |
| canonical id | `producer:pierre-gimonnet-and-fils` |
| canonical entity confidence | 0.2（source: `legacy_app`、`legacy_ids` 2 件）— エンティティ同定の確度であり本書の充実度とは別軸 |
| **Club 会員資格** | ✅ **Club Trésors de Champagne 正会員**。協会公式の会員一覧（全 25 名）に `Champagne Pierre GIMONNET et Fils — Cuis` として掲載。Côte des Blancs / Côte de Sézanne 区分 |

**現況の確認について（前回の教訓 1 の適用）**
✅ 当主の現在性は**公式 2025 年ブローシャの署名**（「Didier et Olivier Gimonnet (3e génération) / Arnaud et
Pierre-Guillaume Gimonnet (4e génération)」）で確認済み。写真キャプションも `Effervescence 2024` `2025` と
年付きで、**2025 年時点の現況として断定してよい。**
❓ ただし **Olivier / Didier / Arnaud / Pierre-Guillaume の役職（醸造責任者・畑責任者など）は公式に肩書として
明記されていない。**公式は「役割を自然に分け合った（du vignoble à la cave, du chai au commerce）」としか書かない。
**「醸造責任者は◯◯」と名指ししてはならない。**

---

## Overview

✅ **コート・デ・ブラン Cuis 村に本拠を置く、シャルドネ専業のレコルタン**。ロゼを唯一の例外として、
**全キュヴェが 100% シャルドネのブラン・ド・ブラン**であり、**ブドウは 1 粒も買わない（自社畑 100%）**。
これは公式が「Champagne でほぼ唯一（*presque unique sur de tels volumes*）」と自認する規模での blanc de blancs 専業である。

✅ 畑は**すべてコート・デ・ブランの 1er Cru / Grand Cru 斜面**にあり、**30 ha 超**。うち **13 ha が Grand Cru**。
Cuis（発祥地）・Cramant・Chouilly の 3 村だけで **27 ha ＝ 全体の 90%** を占める。
**Cramant が全ミレジムの「背骨（colonne vertébrale）」**であり、**Cuis が「フレッシュさの署名」**という
二重構造がハウススタイルの核である。

✅ 醸造は**ステンレスの区画別ヴィニフィカシオン（1955 年に父 Michel が導入）＋ マロラクティック発酵実施 ＋
樽・バトナージュ一切なし**。**リザーブワインは 1982 年以来 100% 瓶で保管**（約 20 万本・約 10 ミレジム）という、
シャンパーニュでは極めて珍しい手法を持つ。年産**約 26 万本**、**輸出 75%・48 か国**。

✅ **Club Trésors de Champagne の正会員**であり、プレステージ・キュヴェ **Spécial Club** を 1971 年（協会創設年）から
造り続けている。**OBP 掲載 6 本はすべてこの Spécial Club 系列**である。

---

## History

### Foundation / 家系

- ✅ **1615** — Gimonnet 家が Cuis に定着。出典は公式ブローシャに引用された **Guy Gimonnet（1925–2023、系譜研究に没頭した叔父）** の言「On trouve des Gimonnet à Cuis depuis 1615…」。
  - ✅ 公式は同時に「先祖は**まず農民（agriculteurs）**であり、vigneron というより百姓だった」「金ぴかの伝説でも神話でもない（*Ni légende dorée, ni mythe*）」と明記する。**「1615 年創業のシャンパーニュ・メゾン」ではない。**
- ✅ **20 世紀初頭** — **既知の最初のラベルは Henri GIMONNET 名義**。
- ✅ **1920 年代** — 醸造活動が実質的に開始。1929 年の大恐慌でネゴスへのブドウ販売が価格的に成立しなくなったことが直接の契機。
- ✅ **1925** — **Pierre Gimonnet（当時 27 歳）が父から独立**。現在の母屋（maison d'exploitation）を建て、**最初の畑 7 ha（2 区画）を購入**。**公式はこの 1925 年を「メゾンの創設」と位置づける**（「Pierre, notre grand-père, le visionnaire qui a fondé la Maison en 1925」）。
  - ⚠️ **最初の価格表の年が公式内で食い違う。** サイト本文（2019 年）は「**début des années 1930**」、英語ブローシャは「**Around 1935**」、2025 年ブローシャは「**Cette tarification retrouvée en 1935**」。→ **「1930 年代に最初の価格表」**とだけ言うのが安全。
  - ✅ その価格表には「jus de raisin frais（生ブドウ果汁）」「vin tranquille originaire de la Champagne（スティルワイン）」「champagnes de cru」が並び、**Cuis の lieu-dit「Les Roualles」のワイン**が載っている。
- ✅ **1947** — **Gastronome 創設**（「Créée en 1947」）。レストラン用に構想された「petite mousse（弱発泡）」のキュヴェ。
- ✅ **1951** — **Chouilly の lieu-dit「Montaigu（Mont Aigu）」植樹**。現在の Chouilly Grand Cru キュヴェの唯一の供給源。
- ✅ **1955** — **Michel Gimonnet（Pierre の息子）が就農し、醸造を一変させる。** 科学的精神の持ち主で、**小型ステンレスタンクによる区画別ヴィニフィカシオンの先駆者**。各 lieu-dit のトレーサビリティと精密な把握を確立した。**「Pierre Gimonnet & Fils スタイル」の創始者は Pierre ではなく Michel である**（公式明言：「**C'est notre père, Michel Gimonnet qui fut l'initiateur du style Pierre Gimonnet & Fils**」）。
- ✅ **1958** — **Cramant Grand Cru を取得。「majoritairement de notre mère, née Larmandier」＝母 Françoise Gimonnet-Larmandier 由来**。
- ✅ **1971** — **Club Trésors de Champagne 創設。同年、Spécial Club キュヴェ誕生。** 公式「La cuvée « Special Club » est née en 1971, à l'occasion de la création du Club Trésors」。後年に「Grands Terroirs de Chardonnay」と命名された（**当初からこの名ではない**）。
  - 🔍 公式 PDF「Special Club 1973」に「**1973 was the 2nd "Special Club" cuvee of the Domaine**」とあり、**メゾンの初 Spécial Club が 1971 年であること**と整合する。
- ✅ **1970 年代の姿** — 1973 年の assemblage は **67% Cramant（Buissons、1913 年植）／33% Cuis 1er Cru**、**dosage 8 g/L**、生産 5,244 本。「当時 Cramant の畑は 1 ha 未満」。**現在の 4 g/L・extra-brut とはまったく別物**であり、ドザージュの歴史的変遷の証拠になる。
- ✅ **1980 年代** — **Olivier と Didier が就農。**
- ✅ **1982** — **リザーブワインの瓶保管を開始**（Michel による）。現在まで続くメゾン最大の差別化要素。
- ✅ **1985** — **Œnophile（非ドザージュ）誕生**。2025 ブローシャは「**elle fut la première cuvée de vigneron non dosée en Champagne, dès 1985**（シャンパーニュ初の vigneron による非ドザージュ・キュヴェ）」と主張する。
  - ⚠️ **公式内で矛盾。** Œnophile 2010 の公式シートは「Our first cuvée « non dosé » was created on **1985**」と書きながら、続けて「**after 1979, 1982, 1985, 1988, 1990, 1993, 1995, 1998, 1999, 2000, 2002, 2004, 2005 and 2008**」と **1979 年・1982 年を列挙**している。**1985 年が「最初」なのか、1979 年が最初なのかは公式内で解決しない。両方残す。**
- ✅ **2005** — **Oger Grand Cru に 1 ha 取得**（コート・デ・ブラン南部への初進出）。
- ✅ **2008** — **Vertus / Bergères-les-Vertus 1er Cru 取得。**
- ✅ **2005–2010** — Oger を 6 ミレジムにわたり控えめにアッサンブラージュへ組み込む試み。だが**「même à très faible dose, Oger imposait sa personnalité」＝極少量でも個性が出すぎた**。
- ✅ **2011** — **Oger Grand Cru を「ノンヴィンテージ（brut sans année）」で単独リリース**。これが mono-terroir 路線の最初の一歩。
- ✅ **2012** — **例外的なミレジムを機に、Spécial Club の mono-terroir 3 種（Chouilly / Cramant / Oger）を創設。**
- ✅ **2012** — **Rosé de Blancs 発売開始。**
- ✅ **2016** — Cuis に **50 ares 追加。**
- ✅ **2018** — **初の Spécial Club「Cuis 1er Cru」**（Grand Cru ではなく 1er Cru の mono-terroir）。以後**隔年**でリリース。
- ✅ **2021** — **Le Mesnil-sur-Oger Grand Cru に 7 ares 取得。**
- ✅ **2022** — **Villeneuve-Renneville 1er Cru に 35 ares 取得。**
- ✅ **2025** — 公式 Estate Book「BROCHURE 2025」刊行（91 頁）。3 代目と 4 代目の連名署名。

---

## Location

**Country / Region** ✅ France / Champagne — **100% Côte des Blancs**（例外なし）
**Village（本拠）** ✅ **Cuis**（1er Cru）。1 rue de la République, 51530 Cuis

### 畑の内訳 ⚠️ **公式内で 2 系統ある。2025 ブローシャを採用値とする。**

| 村 / 格付 | **✅ 採用値: 2025 ブローシャ** | 旧サイト本文（2019 更新）／旧英語ブローシャ |
|---|---|---|
| **Cuis 1er Cru**（発祥地） | **約 15 ha** | 「depuis toujours」（面積記載なし） |
| **Chouilly Grand Cru** | **6 ha**、うち **Montaigu 2.80 ha**（1951 年植） | 「Montaigu **3 ha**」⚠️ |
| **Cramant Grand Cru** | **約 6 ha**（母 Larmandier 家由来、1958〜） | （面積記載なし） |
| **Oger Grand Cru** | **97 ares**（2005〜） | 「**1 hectare**」⚠️（2025 ブローシャ §3.4 自身も「un hectare」と書く） |
| **Vertus & Bergères-les-Vertus 1er Cru** | **1.90 ha**（2008〜） | 「Vertus depuis 2008」 |
| **Le Mesnil-sur-Oger Grand Cru** | **7 ares**（2021〜） | **記載なし**（旧テキストには存在しない村） |
| **Villeneuve-Renneville 1er Cru** | **35 ares**（2022〜） | **記載なし** |
| **合計** | **「plus de 30 hectares」** | **「29,40 hectares」** ⚠️ |
| **うち Grand Cru** | **13 ha** | 「environ 13 ha de grands crus / 16 ha de 1ers crus」 |

🔍 **内部整合の検証（採用値の妥当性）**: 15 + 6 + 6 + 0.97 + 1.90 + 0.07 + 0.35 = **30.29 ha** →「plus de 30 ha」と一致。
Grand Cru 分 6 + 6 + 0.97 + 0.07 = **13.04 ha** →「13 ha classés Grand Cru」と一致。
**2025 ブローシャの数値は内部で閉じている。**したがってこれを採用値とする。

⚠️ **一方、テクニカルシート（2016・2017 ミレジム）は「12 hectares de Grand Cru」と書いている。**
これはシート執筆時点（2017–2018 年頃）の値であり、Le Mesnil（2021）取得前と整合する。**古い記述であって誤りではない。**
→ **現場では「Grand Cru は 12 ha か 13 ha」と数字を断定せず、「13 ha ほど」と言う。**

⚠️ **Chouilly Montaigu は 2.80 ha（2025）と 3 ha（旧サイト・現行製品ページ）の両方が生きている。**
製品ページ `/produit/chouilly-grand-cru/` は**現在も「nos 3 hectares de Montaigu」と書いており**、
サイトとブローシャで矛盾したまま公開されている。**両方残す。断定しない。**

### 主要 lieux-dits ✅（2025 ブローシャの列挙）

| 村 | lieux-dits |
|---|---|
| **Cramant GC** | **Les Terres des Buissons**（1913 年植・**樹齢 100 年超**）／ **Le Bateau**（1911 年植・**樹齢 100 年超**、旧表記 *Fond du Bateau*）／ **Le Gros Mont**（旧表記 *Gromonts*）／ **Les Bionnes** ／ **Les Bauves**（*Hautes Bauves*）／ *Briquettes* ／ *Champ du Prévot* ／ *Grande plante* |
| **Chouilly GC** | **Mont Aigu / Montaigu**（1951 年植・**北東向き**・チョークが露出）／ **Les Ronds Buissons** |
| **Oger GC** | **Terres de Noël** ／ **Champs Nérons** ／ **Brulis** ／ **Fondy** |
| **Vertus 1er** | **Justices** ／ **Faucherets** |
| **Cuis 1er** | **Croix-Blanche**（**4 ha 超の一枚畑、母屋の真裏**。⚠️ Cuis Spécial Club 製品ページは「**4.35 ha**」、2025 ブローシャは「**plus de 4 hectares**」）／ **Les Roualles** ／ **Les Basses Vignes** ／ *Les Bourgs*（1925 年の最初の 2 区画の一方） |

✅ **樹齢**: 「**Grand Cru の 80% は樹齢 50 年超**」（2025）。**Cramant の平均樹齢は 60 年**。
1911 年 Le Bateau と 1913 年 Terres des Buissons の 2 区画は**現在も年 50 hl を産する**。
⚠️ 旧英語ブローシャは「**vineyard の 50% が樹齢 35 年超／Grand Cru 区画の 80% が 45 年以上前に植樹**」。数値が更新されている。

✅ **カーヴ**: 白亜（craie）を掘った地下、**深さ 10–25 m、年間を通じ 9°C 一定**。
⚠️ Millésime de Collection の頁のみ「**15–25 m**」と書かれる。両方残す。

---

## Farming

### 認証 — **ここが現場で最も事故りやすい**

✅ **取得している認証は HVE3（Haute Valeur Environnementale レベル 3）ただ一つ。**
公式原文：「**Nous sommes certifiés HVE3 — non pas par goût des labels, mais parce qu'il faut bien une référence**」。

🔴 ✅ **オーガニック認証・ビオディナミ認証はない。公式が明示的に否定している。**
- 「**Pratiques biologiques sur plusieurs parcelles, sans certification**（複数区画で有機的実践、ただし**無認証**）」
- 「**Chez Gimonnet, nous ne faisons pas de viticulture militante. Nous faisons une viticulture de conviction**」
- 「**Nous ne sommes pas des idéologues, mais tout simplement des pragmatiques avec du bon sens**」（サイト本文）
- 🔴 決定的な一文：「**Trois fois en huit ans, nous avons dû choisir : continuer une pratique «idéale» (bio) sur certaines parcelles, ou sauver la récolte ? Nous avons choisi la vigne.**」
  ＝ **8 年で 3 回、有機的実践を貫くか収穫を守るかの選択を迫られ、収穫を選んだ**と公式が自ら書いている。
  理由も明快：「**Nous ne sommes pas des négociants. Pas de vendange = pas de vin.**」

### 実際の栽培 ✅（2025 ブローシャの箇条書き＝現行方針）

- **除草剤ゼロ（Zéro herbicide）** — 草生栽培（couverts végétaux）、土壌の耕起、**古樹区画では馬耕（traction au cheval）**
- **殺虫剤ゼロ（Aucun insecticide）** — **性フェロモン交信攪乱（confusion sexuelle）**で代替
- **施肥はほぼ行わない** — 「La fertilisation est quasi inexistante」。土壌分析に基づき最小限。**根系を白亜の深部へ潜らせるため**
- **介入は必要最小限**
- **狙いは「fruit より minéral を優先すること」** — 公式原文「**pour privilégier le minéral sur le fruit**」。樹勢を「飼い慣らし（dompter）」区画の個性を出す
- **収穫は全て手摘み** ✅（全テクニカルシート「Vendanges manuelles」）
- **収穫日の決定を最重要視** — 「La date de vendange est cruciale」。香りの成熟＋ミネラルを吸い上げる十分な生育期間
- **マッサル・セレクション（sélection massale）を優先** — 1990 年代に開始、現在は Arnaud と Pierre-Guillaume が継続。祖父母・曽祖父母が選んだ遺伝的多様性を保存する目的。台木も最良区画向けに厳選
- **試験的取り組み** — court-noué（ファンリーフ）対策、気候変動への適応

✅ **ブドウは買わない。100% 自社畑。**（複数箇所で明言）

---

## Winemaking

### 基本方針 ✅
「**La vinification accompagne le raisin, elle ne cherche pas à créer un style**（醸造はブドウに寄り添うのであって、スタイルを作りにいくのではない）」。
自己規定は「**デザイナーの倫理：épure を求め、余計を削ぎ、本質だけを残す**」。

### 工程（全テクニカルシートで共通・一貫）✅

| 工程 | 内容 |
|---|---|
| **収穫** | 手摘み、必要に応じ選果 |
| **圧搾** | **摘み取りから 6 時間以内**。**分割圧搾（pressurage fractionné）** — 果肉由来の「cuvée」と周縁部の「taille」を分離。果汁は**重力でキュヴリーへ** |
| **デブルバージュ** | **低温で自然に。⚠️ 2025 ブローシャ「18 時間」／旧サイト本文「24 時間」。両方残す** |
| **発酵開始** | **圧搾から 36 時間以内**（香りの純度を保つため） |
| **アルコール発酵** | **区画別（parcellaire）・温度管理・ステンレスタンク**。1955 年 Michel が導入した「cuves neutres」。⚠️ 1983 年シートには「18–21°C」の記載あり |
| **マロラクティック発酵** | 🔴 **全キュヴェで実施。**取得した公式シート全件に「Fermentation malolactique / Malolactic fermentation」が明記されている |
| **熟成（タンク）** | **細かい澱の上で、バトナージュなし（sans bâtonnage）**。**6 か月（mono-terroir 系）／ 8 か月（GTC・Œnophile）**。期間は試飲で調整 |
| **安定化** | **低温安定化 −4°C ＋ 粘土による清澄・濾過（filtration sur argile）** |
| **ティラージュ** | 翌年 4 月 |
| **瓶内熟成** | **澱の上で 4〜5 年以上**（Spécial Club）。**GTC は「7〜10 年」**（2025 ブローシャ）。Millésime de Collection は **10 年以上** |
| **デゴルジュマン** | **出荷の 3 か月前**（Oger 2017 のみ **6 か月前**） |

🔴 **樽（oak）は一切登場しない。** 取得した公式資料のいずれにも木樽・フードル・バリックの記述がない。
リザーブワインも「**jamais en cuve ni en foudre**（タンクでもフードルでもなく）」と明示的に否定されている。

### リザーブワイン — メゾン最大の差別化要素 ✅

- **1982 年以来、リザーブワインの 100% を「瓶」で保管**（クオート・ド・ムース ＝ 弱めのガス圧で瓶詰め）。
- **現在約 200,000 本、約 10 ミレジム分**。地下 10–25 m・9°C 一定のカーヴで**緩やかな自己消化（autolyse lente）**。
- 公式の位置づけ：「制約から生まれた決断が、メゾンの強い署名になった」。
- 2 系統に分かれる：
  - **pré-assemblages** — 過去の最良ブリュットの「生きた記憶」。**毎年、ブリュット SA の事前アッサンブラージュを丸ごと隔離保存する**
  - **vins identitaires** — アッサンブラージュの「**医者（médecins）**」。素材感・フレッシュさ・白亜のミネラル・塩味・テクスチャーで選ばれる
- 公式の比喩：リザーブワインは「**des guides、des vins médecins**」であり、**その年のワインを教育する**。

### アッサンブラージュ ✅

- **毎春、直近収穫の vins clairs を約 40 種試飲**（サイト本文は「une quarantaine」）。
- **最優先は毎年「Cuis 1er Cru」ブリュット SA**。「これがドメーヌの名刺（carte de visite）」であり、**他の何より先に造る**。
- **Cuis SA のアッサンブラージュには 60〜80 サンプルを供する**（当年の区画別 vins clairs ＋ **3 キュヴェ × 10 ミレジムのリザーブワイン**）。
- ⚠️ 本数の表現が公式内で揺れる：サイト本文「**pas moins d'une cinquantaine de vins**（50 種以上を assemblage）」、2025 ブローシャ「**60 à 80 échantillons**」。両方残す。
- **ブリュット SA は最低 5 年分の異なる年のワインで構成される**（＝ multi-vintage）✅。
- **基準に達しない vins clairs は容赦なく除外**。
- **アッサンブラージュの処方は代々「小さな手書きのノート（petits carnets）」に記録**。Pierre → Michel → Olivier/Didier の**3 世代**が書き継いでいる。
- 批評家からは「**adeptes de l'holisme**（ホリズムの信奉者）」「**les mixologistes**」と呼ばれてきた（公式が自ら引用。⚠️ サイト本文は綴りが «myxologistes»、ブローシャは «mixologistes»）。

### ドザージュの思想 ✅ — **現場で最重要**

公式原文（Brut Extra の頁）：
「**Personnellement, nous pensons que le dosage fait partie de la vinification champenoise, et nous préférons donc souvent les «extra-brut» au «brut nature». Le bon dosage, c'est «quand on n'en parle pas». Il y en a assez, mais pas trop. Question d'équilibre.**」
＝ **ドザージュは醸造の一部であり、しばしば brut nature より extra-brut を好む。良いドザージュとは「話題にならないドザージュ」。**

そして **Œnophile（唯一の brut nature）は「そういう主義のキュヴェ」ではない**：
「**Œnophile n'est pas une cuvée à part : c'est un Fleuron qui, certains millésimes, atteint un tel équilibre qu'il se passe naturellement de dosage.**」
＝ **Œnophile は Fleuron そのものであり、その年の均衡が完璧なときに「ドザージュを足さなかった」だけ。**
Œnophile 2010 の公式シートも「**So, this Oenophile 2010 is the cuvee Fleuron 2010, without dosage**」と明言する。

### 生産規模 ✅

- **年産 約 260,000 本**（30 ha から）— 2025 ブローシャ
- **輸出 75%、48 か国** ／ **フランス国内 25%（依然として最大単一市場）** — 2025 ブローシャ
  - ⚠️ 旧英語ブローシャ：「**約 70% を 42 か国へ輸出**」「年間 160,000〜180,000 本を輸出」。**古い数字。使わない。**
  - ⚠️ サイト本文（2019）：「**plus de 40 pays**」。**古い。**
- **ヨーロッパ最大市場はドイツ（数量ベース）**、**グラン・エクスポート筆頭は米国** ✅
- **ドメーヌ直販は年 5,000〜8,000 本のみ** ✅

---

## Style

✅ 公式が掲げる**3 本の柱**（サイト §「Notre philosophie du Champagne」＋ 2025 ブローシャ §3.5 で一致）：

1. **シャンパーニュはその出自を明かすべきである** — 「驚くべきミネラリティを通じて、ワインが白亜の土壌について語る」
2. **快楽のためのシャンパーニュ** — 「fraîcheur sapide（旨味のある鮮烈さ）、equilibre、complexité、élégance」
3. **シャンパーニュは偉大な熟成ワインでもある** — 「精密なアッサンブラージュがこの稀な熟成能力の鍵」。**ただし「均衡のとれたシャンパーニュは何年も待つ必要はない。だが何年も保てる」**

✅ **ハウススタイルの言語**（公式の自称語彙。そのまま使ってよい）
`fraîcheur minérale`（ミネラルな鮮烈さ）／ `élégance ciselée`（彫琢された優雅さ）／ `pureté cristalline` ／
`salivant`（唾液を誘う）／ `tension` ／ `texture soyeuse`（絹のような舌触り）／ `crayeux`（白亜的）／
`sans artifice`（作為がない）。**公式は「préférer l'harmonie à l'intensité, l'équilibre à l'ultra-concentration」＝
強度より調和、超凝縮より均衡**と明言する。

✅ **村ごとのキャラクター**（2025 ブローシャ §4.2 — 現場でそのまま使える）

| 村 | 公式の性格づけ |
|---|---|
| **Cramant** GC | 「notre fierté」。**究極の繊細さ、白亜の骨格、彫琢されたテクスチャー**。クリーミーで包み込む舌触り。**全ミレジムの背骨** |
| **Chouilly** GC | **より愛撫的、丸みのある果実感と即時的な優雅さ**。Mont Aigu は北東向きで成熟が遅く「**ultra-crayeuse（超白亜的）**」なテクスチャー |
| **Cuis** 1er | **本質的。複雑さは劣るが、鋭く、光に満ち、空気のよう。全体を持ち上げる** |
| **Oger** GC | **南部唯一の畑。より陽性（solaire）で骨格があり、密度が高く、ほぼリッチ。「fumée（燻し）」「graphite」のミネラル** ← **他と明確に別物** |
| **Vertus** 1er | 「éclats exotiques（エキゾチックな煌めき）」 |

✅ **ブラン・ド・ブランの位置づけ** — 「大手メゾンでは blanc de blancs は例外・高級ライン。**うちでは逆で、blanc de blancs は例外でも希少品でもなく、当たり前（une évidence）**」。

---

## Important Cuvées

### 🔴 OBP 掲載分（全 6 本）— **全て Spécial Club 系列**

🔍 canonical 状態は batch3.json（THÉSEUS 側実データ）より。
✅ 技術データは**公式テクニカルシート PDF から直接読み取った値**。

| # | **OBP 印字**（メニューそのまま） | VT | 価格 | **公式正式名** | **公式ドザージュ** | **生産本数** | canonical |
|---|---|---|---|---|---|---|---|
| 1 | `'Chouilly,' Grand Cru Brut` | **2016** | $415 | **Special Club — CHOUILLY GRAND CRU** | **EXTRA-BRUT 4,5 g/L** | **3,883 本** | ✅ **登録済** `cuvee:…-chouilly-grand-cru-special-club-brut` / vintage 2016 あり（state=`alias`） |
| 2 | `'Cramant' Grand Cru Brut` | **2017** | $465 | **Special Club — CRAMANT GRAND CRU 2017** | **EXTRA-BRUT 4 g/L** | **3,906 本** | 🔴 **未登録**（state=`unresolved`） |
| 3 | `'Cuis,' Premier Cru Brut` | **2019** | $360 | **Special Club — CUIS 1ER CRU 2019** | **EXTRA-BRUT 4,5 g/L** | **4,020 本** | 🔴 **未登録** |
| 4 | `'Grand Terriors de Chardonnay,' Premier Cru Brut` ⚠️**誤植** | **2016** | $350 | **SPECIAL CLUB « Grands Terroirs de Chardonnay » 2016** | **EXTRA BRUT 5 g/L** | **26,320 本** | 🔴 **未登録** |
| 5 | `'Grand Terriors de Chardonnay,' Premier Cru Brut` ⚠️**誤植** | **2014** | $435 | **SPECIAL CLUB « Grands Terroirs de Chardonnay » 2014** | **EXTRA BRUT 5 g/L** | **24,876 本 ＋ magnum 1,172 本** | 🔴 **未登録** |
| 6 | `'Oger,' Grand Cru Brut` | **2017** | $440 | **Special Club — OGER GRAND CRU 2017** | **EXTRA-BRUT 4 g/L** | **3,952 本** | 🔴 **未登録** |

🔴 **6 本中 5 本が canonical 未解決。本バッチ最多。**
🔴 **6 本すべてがメニュー上「Brut」と印字されているが、公式はすべて EXTRA-BRUT（4〜5 g/L）である。**

---

### 各キュヴェの公式データ（テクニカルシートより）

#### ① Special Club — CHOUILLY GRAND CRU 2016 ｜ OBP $415
> 公式キャッチ：「**Grand Blanc tout en finesse et élégance, à la texture ultra-crayeuse**」

- **セパージュ** 100% Chardonnay ✅
- **テロワール** **100% Chouilly Grand Cru — lieu-dit「Montaigu」のみ。1951 年植樹の畑** ✅
  → **メゾンで唯一「複数区画・単一 lieu-dit」から成るキュヴェ** ✅（製品ページ明言）
- **収穫** ⚠️ FR シート「**2016 年 9 月 27・28 日**」／ EN シート「**27th September 2016**」。自然アルコール度 **10°6**
- **醸造** 手摘み・分割圧搾／低温デブルバージュ／温度管理 AF／**MLF あり**／**タンク熟成 6 か月**／−4°C 安定化＋粘土濾過
- **ティラージュ** 2017 年 4 月（EN シートは「27th April 2017」）
- **瓶熟** ⚠️ **FR シート「plus de 4 ans」／ EN シート「more than 5 years」。公式内で食い違う。両方残す**
- **デゴルジュマン** 出荷 3 か月前 ／ **ドザージュ EXTRA-BRUT 4,5 g/L** ／ **生産 3,883 本**
- **スタイル** ✅「blanc de blancs の原型。繊細・デリケート・クリーミー。極めて Gimonnet 的」「白亜のささやき、塩の愛撫」

#### ② Special Club — CRAMANT GRAND CRU 2017 ｜ OBP $465
> 公式キャッチ：「**Notre Terroir préféré. Élégant, soyeux et profondeur**（我々の一番好きなテロワール）」

- **テロワール** **100% Cramant Grand Cru** ✅ — **区画構成まで公開されている**：
  - **65% 「Terres des Buissons」**（うち **1913 年植の古樹**を含む）
  - **21% 「Le Bateau」**（うち **1911 年植の古樹**を含む）
  - **14% 「Grande plante」「Bauves」「Bionnes」**
- **収穫** 2017 年 9 月 5–7 日、自然アルコール度 **11°5**
- **醸造** ステンレスタンク熟成 6 か月、**MLF あり**、−4°C 安定化＋粘土濾過
- **ティラージュ 2018 年 4 月 25 日** ／ **瓶熟 5 年以上** ／ デゴルジュマン 3 か月前
- **ドザージュ EXTRA BRUT 4 g/L** ／ **生産 3,906 本**
- **スタイル** ✅「絹のようなテクスチャー、優雅さ、深み — 模倣不能」「コート・デ・ブラン 2 大歴史的グラン・クリュの一つ」
- 🔴 **メゾンの「coup de cœur（一番の惚れ込み）」と公式が明言する。**

#### ③ Special Club — CUIS 1ER CRU 2019 ｜ OBP $360
> 公式キャッチ：「**Fine and elegant, a great "silky" and deep Blanc de blancs**」

- **テロワール** **Cuis 1er Cru — 90% 「Croix-Blanche」／ 10% 「Les Roualles」** ✅
- **瓶詰前の自然アルコールポテンシャル 11°95** ✅
- **ティラージュ 2020 年 4 月** ／ **瓶熟 4 年以上** ／ デゴルジュマン 3 か月前
- **ドザージュ EXTRA BRUT 4,5 g/L** ／ **生産 4,020 本**
- 🔴 **2018 年が初ヴィンテージ。2019 は第 2 ヴィンテージ。**公式シート冒頭が直球：
  「After the 1st Special Club "Cuis 1er cru" in 2018…. Let's go for 2019… **It seems so easy because 2019 is probably the best vintage of the decade…**」
  → **「作り手自身が 2019 を『おそらくこの 10 年で最良のミレジム』と書いている」は使える一言。**
- ✅ **なぜ 2018 年に初めて成立したか**：「**15 ha を Cuis に持ち、温暖化による新しい成熟が得られる文脈で、4,000 本を造ることが可能になった。そして何より、正当（légitime）になった**」
- ✅ 位置づけ：「**Special Club コレクションの独奏者（soliste virtuose）**」。GTC が交響曲、他 3 つが Grand Cru の中で、これだけが **mono-premier cru** で「より結晶的、より空気的」
- ✅ Cuis の性格：「**コート・デ・ブランで最も厳しい（austères）テロワールの一つ**」「空気的、レモン的、唾液を誘い、深くミネラル」

#### ④⑤ SPECIAL CLUB « Grands Terroirs de Chardonnay » 2016 / 2014 ｜ OBP $350 / $435
> **1971 年以来のプレステージ・キュヴェ。メゾンの旗艦アッサンブラージュ。**

| | **2016** | **2014** |
|---|---|---|
| **格付比率** | **85% Grands Crus – 15% 1er Cru** | **84% Grand Cru – 16% 1er Cru** |
| **Cramant GC** | **58%** — 33% Terres des Buissons / 7% Bauves / 9% Bateau & Gros Mont / 9% Champ du Prévot ほか | **59%** — ⚠️ **FR/EN で lieu-dit 表記が違う**：FR「Bateau, Gros Mont, Briquettes, Bauves, Bionnes」／ EN「**Fond du Bateau, Gromonts**, Briquettes, Bauves, Bionnes」 |
| **Chouilly GC** | **27%**（Mont Aigu） | **25%**（Montaigu） |
| **Cuis 1er** | **15%** — 5% Croix-Blanche / 10% Roualles | **16%** — Croix-Blanche, Roualles |
| **タンク熟成** | **8 か月**（澱の上） | **8 か月** |
| **ティラージュ** | **2017 年 4 月 27 日** | **2015 年 4 月** |
| **瓶熟** | **5 年以上** | **4 年以上** |
| **ドザージュ** | **EXTRA BRUT 5 g/L** | **EXTRA BRUT 5 g/L** |
| **生産** | **26,320 本** | **24,876 本 ＋ magnum 1,172 本** |

- ✅ **共通の構成原理**：「**樹齢 40 年超の古樹のみ。最古は 1911 年と 1913 年植**」「**Cramant の『テロワールの心臓部』を主体に、Chouilly Montaigu で補い、Cuis 1er Cru を『一点』加えて Gimonnet の署名たるフレッシュさを与える**」
- ✅ 2025 ブローシャの現行構成比：**Cramant 60% / Chouilly 25% / Cuis 15%**、**瓶熟は 7〜10 年**
- ✅ 生産量の基準：「**収穫の質に応じ 10,000〜25,000 本。偉大な年のみ**」（2012 年シート）
- ⚠️ **メニュー印字「Grand Terriors de Chardonnay」は誤植。正しくは「Grands Terroirs de Chardonnay」。**
- ❓ **ラベル上の格付表記（"Premier Cru" か否か）は公式に明記がない。** ただし **85%GC + 15%1er cru** の混成であり、
  メニューの「Premier Cru」表記は算術的に矛盾しない。**断定はしない。**

#### ⑥ Special Club — OGER GRAND CRU 2017 ｜ OBP $440
> 公式キャッチ：「**Puissance et minéralité d'un grand terroir**」

- **テロワール** **Oger Grand Cru — 4 区画 / 4 lieux-dits** ✅
  - **62% 「Terres de Noël」＋「Brulis」**（cœur de terroir）
  - **20% 「Fondy」**（Oger の粘土石灰質）
  - **18% 「Champs Néron」**（純白亜の上）
- **収穫** 2017 年 9 月 4 日、自然アルコール度 **11°6**
- **ティラージュ 2018 年 4 月 25 日** ／ **瓶熟 5 年以上**
- 🔴 **デゴルジュマン：出荷の 6 か月前**（他キュヴェは 3 か月前）— **このキュヴェだけ違う**
- **ドザージュ EXTRA-BRUT 4 g/L** ／ **生産 3,952 本**
- ✅ **位置づけが他と決定的に違う**：「**ドメーヌで唯一、コート・デ・ブラン南部から全量が来るキュヴェ**」
  「自然な力強さと、**通常のアッサンブラージュより『燻した』『グラファイト的』なミネラル表現**」
  「**通常のアッサンブラージュの白亜的フレッシュさから遠い、稀な表現**」
- ✅ 公式のユーモア（そのまま使える）：「**L'huître chuchote à Chouilly, Oger danse avec le homard**
  （牡蠣は Chouilly にささやき、Oger はオマールと踊る）」

---

### 🔴 Spécial Club とは何か — 現場説明用（Club Trésors 公式より）

| | |
|---|---|
| **主体** | **Club Trésors de Champagne**（1971 年創設）✅ |
| **会員数** | **現在 25 名の Clubmen / Clubwomen** ✅（Gimonnet はその 1 人・Cuis） |
| **性格** | **「シャンパーニュで唯一、妥協なき基準で造り手を選抜する組織」**（協会公式の自称）✅ |
| **Spécial Club の資格** | ✅ **会員だけが造れる。**造るには**有望なミレジムを厳格な仕様書（cahier des charges）に基づいて申請**し、**独立した醸造士パネルによる 2 回のブラインド・テイスティング**を通過しなければならない |
| **必ず** | **ミレジム（ヴィンテージ）である** ✅ |
| **見分け方** | ✅ **専用の独特なボトル形状（公式 PDF は「bouteille de style XVIIIème」＝ 18 世紀様式）と Club の紋章ラベル** |
| **流通** | ✅ 少量限定。Reims の La Boutique、会員本人、および**選ばれた酒販店・レストラン**（フランス国内外） |
| **4 つの価値** | Excellence / Passion / Conviviality / Commitment。入会時に **Clubman/woman Commitment Charter への署名が必要** ✅ |
| **最古** | ✅ 協会は **1971 年（協会最初のミレジム）に遡る Spécial Club のワインライブラリーを保有** |

🔴 **重要**：Spécial Club は **AOC の格付でも、公的な認証機関でもない。生産者団体の共通プレステージ・キュヴェである。**

---

### OBP 未掲載の主要キュヴェ（参考・アップセル用）✅

| キュヴェ | 種別 | 公式の要点 |
|---|---|---|
| **Cuis 1er Cru**（ブリュット SA） | NV Brut | **メゾンの名刺・最量販キュヴェ**。毎年**最優先**で造る。**最低 5 年分**のブレンド。瓶熟リザーブワインを多量に含む。「vif, aérien, salivant」 |
| **Brut Extra** | NV Extra-Brut | Cuis 1er Cru と**同じアッサンブラージュ**を、**より長く（約 4 年）ラット熟成**し **extra-brut ドザージュ**にしたもの。「より垂直的、よりミネラル」 |
| **Rosé de Blancs** | NV Rosé | **唯一の非 blanc de blancs**。**Chardonnay 94% ＋ Grand Cru Pinot Noir 6%** ⚠️（サイト製品ページは「92〜95% / 5〜8%」）。2012 年発売。**saignée ではなくアッサンブラージュ**。年約 20,000 本仕込み。**現在 Gastronome より売れている** |
| **Oger Grand Cru**（ブリュット SA） | NV Brut | 🔴 **Spécial Club の Oger とは別物。**メゾン唯一の「単一 Grand Cru のノンヴィンテージ」。**熟成 2〜3 年と短く、リザーブワインは 5〜10% のみ**で、実質は単一収穫年。2011 年開始 |
| **Gastronome** | Millésimé | **1947 年創設**。**「petite mousse / perlé」＝ 意図的に弱い発泡**でレストラン向け。Cramant・Oger（深み）＋ Chouilly・Vertus（果実）＋ Cuis（フレッシュさ） |
| **Fleuron** | Millésimé | **ドメーヌ最初のミレジム・キュヴェ。**祖父の時代、「リザーブワインを足さなくても均衡する年」に造られた。**リザーブワインを使わない**。「Cuis 1er Cru より構造的、Gastronome より複雑、Special Club GTC よりしばしば開いている」 |
| **Œnophile** | Millésimé Brut Nature | 🔴 **その年の Fleuron そのものを、ドザージュせずに出したもの。**専用のアッサンブラージュを組まない。**メゾン唯一の brut nature**。1985 年〜（⚠️ 1979/1982 の記載もあり） |
| **Millésime de Collection** | Millésimé（**magnum のみ**） | 🔴 **Special Club GTC と同一のアッサンブラージュ。**違いは **① マグナムでの瓶内二次発酵 ② 澱の上で 10 年以上 ③ 深さ 15–25 m・9°C のカーヴでの緩慢な熟成**。**8 年カーヴに置いて期待に届かなければこのラベルを付けない。**現行 2014・2015 |

✅ **Œnophile 2010 の実測アッサンブラージュ**（canonical 修正の根拠。§Open Questions 参照）：
**40.5% Cramant GC（Bateau, Buissons）／ 27% Chouilly GC（Montaigu, Ronds Buissons）／ 5.8% Oger GC（Champs Nérons, Terres de Noël）／ 10.5% Vertus 1er（Faucherets, Justices）／ 16.2% Cuis 1er（Croix-Blanche）**。
**73% Grand Cru – 27% 1er Cru。瓶熟 8 年以上。Fleuron 2010 の 33,680 本のうち 6,000 本が brut nature。**

---

## Staff Notes

### 芯 3 点（これだけ覚えれば現場で間違えない）

**① 「コート・デ・ブラン 100%、シャルドネ 100%、自社畑 100%」**
ロゼを唯一の例外に、**全てのキュヴェがブラン・ド・ブラン**。**ブドウは一切買わない。**
30 ha 超を全てコート・デ・ブランの 1er / Grand Cru 斜面に持つ。この規模での blanc de blancs 専業は
シャンパーニュで**ほぼ他にない**（公式自称：「presque unique sur de tels volumes」）。

**② 「Spécial Club は Gimonnet の商品名ではない」**
**Club Trésors de Champagne（1971 年創設、現在 25 名の造り手）の共通プレステージ・キュヴェ**であり、
**必ずミレジム**、**独立醸造士による 2 回のブラインド審査を通過**したものだけが名乗れる。
**専用の 18 世紀様式ボトル**が目印。**OBP の 6 本はすべてこれ。**

**③ 「背骨は Cramant、署名は Cuis」**
Gimonnet の全ミレジムの骨格は **Cramant Grand Cru**（樹齢平均 60 年、1911/1913 年の百年樹を含む）。
そこに **Cuis 1er Cru を一点加えてフレッシュさを与える**のが「Gimonnet の署名」。
だから **本流はアッサンブラージュの GTC**であり、**モノテロワール 4 種は「例外」**。
その例外は **年産 4,000 本前後**（GTC の 26,000 本に対して）で、**極めて希少**。

### そのまま使える一言（すべて公式表現）

- 「**Michel が 1955 年に始めた区画別ステンレス醸造。だから樽の香りは一切ありません。**」
- 「**リザーブワインを 1982 年から 100% 瓶で寝かせています。約 20 万本、10 ミレジム分。シャンパーニュでは極めて珍しい方法です。**」
- 「**ドザージュについて彼らはこう言います — 良いドザージュとは、話題にならないドザージュだ、と。**」
- 「**Cramant 2017 は蔵元自身が『我々の一番の惚れ込み（coup de cœur）』と書いているキュヴェです。3,906 本しか造られていません。**」
- 「**Cuis 2019 は蔵元が『おそらくこの 10 年で最良のミレジム』と書いています。Cuis 単独の Spécial Club は 2018 年が初めてで、これは 2 本目のヴィンテージです。**」
- 「**Oger だけ南部の畑で、他とまるで性格が違います。蔵元の言葉では『牡蠣は Chouilly にささやき、Oger はオマールと踊る』。**」
- 「**Chouilly は Montaigu という単一 lieu-dit だけ。1951 年に植えられた畑です。北東向きで成熟が遅く、極端に白亜的な質感になります。**」
- 「**Millésime de Collection は Special Club とまったく同じアッサンブラージュを、マグナムだけで 10 年以上寝かせたものです。**」

### 温度・グラス・ペアリング
✅ 公式に**サービス温度・グラスの指定はない**（canonical の `serving_temp` / `glassware` は公式由来ではない）。
✅ 公式が明示するペアリングのみ使うこと：
- **Œnophile** → **牡蠣 1 ダース**、料理しながら瞑想的に単体で
- **Oger（BSA）** → **アメリケーヌ・ソースのアンコウ**、**ケイジャン・スパイスのマグロのミキュイ**
- **Gastronome** → 繊細な料理、食前酒の延長。「食卓のためのシャンパーニュ」
- **Cuis 1er Cru** → **食前酒。時間を問わず**

### ⚠️ 言ってはいけないこと（現場で事故る順）

🔴 **1. 「オーガニックです」「ビオディナミです」「サステナブル認証を取っています」— 全部 NG。**
**取得認証は HVE3 ただ一つ。**公式は「複数区画で有機的実践、**ただし無認証**」と書き、さらに
**「8 年で 3 回、有機的実践を貫くか収穫を守るかを迫られ、収穫を選んだ」**と自ら書いている。
正しい言い方 →「**認証は HVE3。除草剤ゼロ、殺虫剤ゼロ、古樹区画では馬で耕します。有機は一部区画で実践していますが、認証は取っていません — 彼らは主義より収穫を守る方を選ぶと明言しています。**」

🔴 **2. 「ブリュットです」と言い切る — NG。OBP 掲載 6 本はすべて EXTRA-BRUT（4〜5 g/L）。**
メニュー印字が「Brut」なので**そのまま読むと間違える。**
正しい言い方 →「**メニューには Brut とありますが、蔵元の公式データではエクストラ・ブリュット、残糖 4〜5 g/L です。**」

🔴 **3. 「グラン・テリオール（Grand Terriors）」と読み上げる — NG。メニューの誤植。**
正しくは **「Grands Terroirs de Chardonnay」（グラン・テロワール・ド・シャルドネ）**。

🔴 **4. 「SGC 認定」— NG。そんな機関は存在しない。**
（canonical の既存テキストにこの表現が入っているが**公式ソースに存在しない**。）
正しくは **Club Trésors de Champagne**。審査は**独立醸造士パネルによる 2 回のブラインド・テイスティング**。

🔴 **5. 「樽で熟成しています」「バトナージュしています」— NG。両方とも一切ない。**
公式は樽・フードルを**明示的に否定**する（リザーブワインも「jamais en cuve ni en foudre」）。熟成はステンレス、澱の上で**バトナージュなし**。

🔴 **6. 「マロラクティック発酵はしていません」— NG。全キュヴェで実施している。**
取得した公式テクニカルシート全件に MLF が明記されている。

🔴 **7. 「Spécial Club はグラン・クリュだけのものです」— NG。**
**Cuis は 1er Cru の Spécial Club**（2018 年〜）。**GTC もメニュー上 Premier Cru 表記。**

🔴 **8. 「Oger が Gimonnet の中心的な畑です」— NG。逆。**
Oger は **97 ares（1 ha 弱）** しかなく、**南部唯一の「例外」**。中心は **Cramant と Cuis**。

🔴 **9. 現当主を「Pierre Gimonnet」と言う — NG。**
Pierre は**創業者（1925 年、27 歳）で故人**。現在は **Olivier と Didier（3 代目）**、次世代が **Arnaud と Pierre-Guillaume（4 代目）**。
🔴 **さらに「醸造責任者は◯◯さん」と名指ししてはならない。公式に肩書の記載がない。**

🔴 **10. 「1615 年創業の名門」— NG。**
1615 年は **Gimonnet 家が Cuis にいたことが確認できる年**であって創業年ではない。しかも公式自身が
「先祖はまず農民だった」「金ぴかの伝説でも神話でもない」と書いている。**メゾンの創設は 1925 年。**

🔴 **11. 面積の数字を断定する — 危険。公式内で食い違っている。**
「Grand Cru は 12 ha」（テクニカルシート）／「13 ha」（2025 ブローシャ）、
「Montaigu は 3 ha」（現行製品ページ）／「2.80 ha」（2025 ブローシャ）、
「総面積 29.40 ha」（旧）／「30 ha 超」（2025）。→ **「およそ 30 ha、うちグラン・クリュが 13 ha ほど」**でぼかす。

🔴 **12. 「40 か国に輸出」— 古い。**
現行（2025）は **48 か国・輸出比率 75%**。旧資料の「42 か国 / 70%」「40 か国」は使わない。

🔴 **13. 「Millésime de Collection は Special Club とは別のワイン」— NG。**
**アッサンブラージュは同一。**違うのは**マグナムでの二次発酵と 10 年以上の熟成**だけ。

🔴 **14. 点数・評価を語る — 公式に一切ない。**
canonical に「95 points」等が入っているが**出典不明で公式由来ではない**。**現場で点数を言わない。**
公式が唯一引用する第三者評は **Richard Juhlin（⚠️ 公式表記は「Richard Julhin」と綴り誤り）の「生涯に一度は試すべき 100 のシャンパーニュ」** における Millésime de Collection への言及のみ。

🔴 **15. 「非ドザージュのパイオニアで、主義としてドザージュを否定している」— NG。逆。**
公式は「**ドザージュは醸造の一部**」「**しばしば brut nature より extra-brut を好む**」と明言する。
Œnophile は主義ではなく「**その年の Fleuron がたまたま完璧に均衡したので何も足さなかった**」もの。

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

なし。

---

## Sources

### 一次資料 A — 生産者公式サイト `https://www.champagne-gimonnet.com`
**コンテンツページ（9）**
- `/un-domaine-familial-et-vignerons-avant-tout/`（沿革・家族）
- `/un-terroir-unique-chef-doeuvre-de-la-nature/`（畑・テロワール）
- `/un-style-reflet-du-terroir-et-dun-savoir-faire/`（醸造工程）
- `/une-viticulture-respectueuse-du-terroir/`（栽培）
- `/lart-de-lassemblage/`（アッサンブラージュ・リザーブワイン）
- `/notre-philosophie-du-champagne/`（3 本の柱）
- `/brochure-2025/` `/cuvees/` `/contact/`

**製品ページ（15）** — `/produit/` 配下（§ヘッダに列挙）

### 一次資料 B — 公式テクニカルシート PDF（全 98 件中、取得・解析したもの）
**OBP 掲載 6 本に対応（全件取得済み・`_sources/pierre-gimonnet-et-fils/` に保存）**

| ファイル | 公式 URL |
|---|---|
| `Special-Club-Chouilly-GC-2016-FR.pdf` | `/wp-content/uploads/2019/11/Special-Club-Chouilly-GC-2016-FR.pdf` |
| `Special-Club-Chouilly-GC-2016.pdf`（EN） | `/wp-content/uploads/2019/11/Special-Club-Chouilly-GC-2016.pdf` |
| `Special-Club-Cramant-GC-2017-FR.pdf` / `-EN.pdf` | `/wp-content/uploads/2019/11/Special-Club-Cramant-GC-2017-{FR,EN}.pdf` |
| `Special-Club-Cuis-1er-cru-2019-EN.pdf` | `/wp-content/uploads/2023/02/Special-Club-Cuis-1er-cru-2019-EN.pdf` |
| `Special-Club-GTC-2016-FR.pdf` / `-EN.pdf` | `/wp-content/uploads/2019/11/Special-Club-GTC-2016-{FR,EN}.pdf` |
| `Special-Club-GTC-2014-4.pdf`（FR）/ `-5.pdf`（EN） | `/wp-content/uploads/2019/11/Special-Club-GTC-2014-{4,5}.pdf` |
| `Special-Club-Oger-GC-2017-FR.pdf` / `-EN.pdf` | `/wp-content/uploads/2019/11/Special-Club-Oger-GC-2017-{FR,EN}.pdf` |

**補助的に解析した公式 PDF**
- `BROCHURE-GIMONNET-2025-FR.pdf`（91 頁 Estate Book。**最新の一次資料**。⚠️ 奥付の法定文言は「2026 -」表記）
- `brochure-gimonnet-fr.pdf` / `brochure-gimonnet-en.pdf`（**旧版 Estate Book。29.40 ha 等の旧数値の出典**）
- `Oenophile-brut-nature-2010-4.pdf`（canonical 登録済 vintage 2010 の実測アッサンブラージュ）
- `Special-Club-2012-Fiche-technique.pdf`（GTC 2012。生産基準「10〜30,000 本、偉大な年のみ」）
- `Special-club-1973-to-2010.pdf` / `Special-club-1983-to-2010.pdf`（Spécial Club 歴代ミレジムの assemblage 履歴）

### 一次資料 C — Club Trésors de Champagne 公式 `https://www.clubtresorsdechampagne.com`
- `/en/le-club-tresors-de-champagne/qui-sommes-nous-2/` — 協会の定義、Spécial Club の資格要件・審査手順
- `/en/le-club-tresors-de-champagne/les-vignerons-du-club/` — **会員 25 名の一覧。`Champagne Pierre GIMONNET et Fils — Cuis` を確認**
- `/la-boutique-du-club/qui-sommes-nous-2/`（FR）

### THÉSEUS 内部データ 🔍
- `batch3.json`（canonical レコード概要／canonical キュヴェ 2 件／OBP 掲載 6 本）
- `theseus-phase0@main:migration/out/resolved/{wine_makers,cuvees,vintages}.json`（**読み取りのみ・無変更**）
- `research/canonical_conflicts/REGISTER.md`（**Gimonnet の記載なし**を確認済み）

### 🚫 使用していないもの
Wikipedia、小売・EC サイト、インポーター販促文、wine-searcher / Vivino 等の集約サイト、まとめブログ。
**検索は公式ドメインの特定にのみ使用した。**

---

## Confidence

| 節 | 判定 | 根拠 |
|---|---|---|
| **Identity** | **High** | 公式サイト＋2025 ブローシャ署名＋Club Trésors 会員一覧の 3 点で一致。ただし**役職名は未確認（Medium）** |
| **Overview** | **High** | 全項目が公式一次資料に直接対応 |
| **History** | **Medium-High** | 主要年（1925/1955/1958/1971/1982/2005/2008/2012/2018/2021/2022）は公式明記。⚠️ 最初の価格表の年と非ドザージュ初年に公式内矛盾あり |
| **Location** | **Medium-High** | 2025 ブローシャの内訳は**内部整合が取れている**（合計 30.29 ha / GC 13.04 ha）ため信頼度高。ただし**旧値と併存**しており数値の断定はできない |
| **Farming** | **High** | 認証（HVE3 のみ・有機非認証）は公式が反復して明言。除草剤/殺虫剤ゼロ・馬耕・マッサル選抜まで具体 |
| **Winemaking** | **High** | **OBP 掲載 6 本すべてのテクニカルシートを取得済み。**圧搾〜デゴルジュマンまで数値付きで確認。MLF・樽なしも全件で一貫 |
| **Style** | **High** | 公式の 3 本柱と村別キャラクターがサイト・ブローシャで一致 |
| **Important Cuvées** | **High** | 6 本すべてに公式シートあり。区画構成・生産本数・ドザージュ・熟成期間まで数値確定 |
| **Spécial Club の制度説明** | **High** | 協会公式（一次資料）で確認。会員数 25・2 回ブラインド審査・1971 年創設 |
| **Staff Notes / ⚠️ リスト** | **High** | すべて公式記述に紐付く。推測を含まない |
| **総合** | **High** | 🔴 **70% 基準を大きく超過。**必須項目（Identity / Overview / Location / **Farming** / Important Cuvées（OBP 紐付け）/ Staff Notes 芯 3 点 / ⚠️ リスト）がすべて公式一次資料で埋まり、**さらに後回し可の領域（醸造数値・区画比率・生産本数）まで公式 PDF で確定している** |

---

## Open Questions

### 公式に記述が存在しない事項（＝これ自体が調査結果。埋めるために非公式ソースを使わない）
- ❓ **RM（Récoltant-Manipulant）番号・法人形態・登録番号**が公式サイトに記載されていない。「ブドウを買わない vigneron」であることは明言されているが、**ラベル記号「RM」を公式では確認できない。**
- ❓ **Olivier / Didier / Arnaud / Pierre-Guillaume の正式な役職**（醸造責任者・栽培責任者・輸出責任者など）が公式に一切明記されていない。**名指しの肩書は出せない。**
- ❓ **サービス温度・グラス指定**が公式に存在しない。canonical の `serving_temp`「8–10°C」「9–11°C」、`glassware`「White Burgundy」「Tulip」**は公式由来ではない。**
- ❓ **点数・第三者評価**が公式にほぼ存在しない。唯一 Richard Juhlin の言及（Millésime de Collection）のみ。canonical の `points: 95` は**出典不明。**
- ❓ **GTC の label 上の格付表記**（"Premier Cru" と印字されているか）が公式資料で確認できない。
- ❓ **Chouilly Grand Cru キュヴェの正確な区画数**。公式は「複数区画・単一 lieu-dit Montaigu」とするが区画数は非公開。

### 公式内で食い違い、解決できなかった事項 ⚠️（両方残してある）
- ⚠️ **Chouilly 2016 の瓶熟期間** — FR シート「4 年以上」／ EN シート「5 年以上」
- ⚠️ **Œnophile の初の非ドザージュ年** — 「1985 年が最初」と書きつつ、同一シートで 1979・1982 を列挙
- ⚠️ **Montaigu の面積** — 現行製品ページ「3 ha」／ 2025 ブローシャ「2.80 ha」
- ⚠️ **Grand Cru 総面積** — テクニカルシート「12 ha」／ 2025 ブローシャ「13 ha」（取得年の差で説明可能だが確証なし）
- ⚠️ **総面積** — 旧ブローシャ／旧サイト「29.40 ha」／ 2025 ブローシャ「30 ha 超」
- ⚠️ **Oger の取得面積** — 「97 ares」（2025 §1.1）／「un hectare」（2025 §3.4・旧サイト）
- ⚠️ **デブルバージュ時間** — 2025「18 時間」／旧サイト「24 時間」
- ⚠️ **GTC 2014 の Cramant lieux-dits 表記** — FR「Bateau / Gros Mont」／ EN「Fond du Bateau / Gromonts」
- ⚠️ **Rosé de Blancs の比率** — 製品ページ「Chardonnay 92–95% / Pinot Noir 5–8%」／ 2025 ブローシャ「94% / 6%」
- ⚠️ **Cuis SA アッサンブラージュのサンプル数** — サイト「50 種以上」／ 2025「60〜80」
- ⚠️ **カーヴの深さ** — 「10–25 m」（リザーブワインの頁）／「15–25 m」（Collection の頁）
- ⚠️ **2025 ブローシャの年次** — ページ更新日は 2025-10-31、タイトルは「Brochure 2025」だが、**PDF 奥付の法定文言は「2026 -」**。刊行年の断定は避けた。

### 🔴 canonical 側の要修正事項（**本書では修正していない。昇格時に必ず処理すること**）
1. 🔴 **`cuvee:pierre-gimonnet-and-fils-chouilly-grand-cru-special-club-brut` の `dosage: "Brut — 5 g/L"` は誤り。**
   公式シート＝ **EXTRA-BRUT 4,5 g/L**。キュヴェ名に含まれる `Brut` も**公式は `Extra-brut`**。
2. 🔴 **同レコードの `obp_note` / `description` にある「SGC が認定」「SGC 認定」は公式に存在しない表現。**
   正しくは **Club Trésors de Champagne**、審査は**独立醸造士による 2 回のブラインド・テイスティング**。
3. 🔴 **`cuvee:pierre-gimonnet-and-fils-oenophile-non-dose-premier-cru` の `subregion` 「Chouilly Grand Cru / Cuis Premier Cru」は不正確。**
   公式 2010 シートの実測は **Cramant 40.5% / Chouilly 27% / Oger 5.8% / Vertus 10.5% / Cuis 16.2%** であり、
   **最大構成要素の Cramant が欠落している。**
4. ⚠️ `vintage:…-chouilly-…-2016` の `aging: "5+ years sur lie"` は EN シート準拠。**FR シートは「4 年以上」。**
5. ⚠️ `points: 95` / `drinking_window` / `serving_temp` / `glassware` は**公式に典拠がない。**昇格時に出典を要求すべき。

### 🔴 OBP / intake 側の要処理事項 🔍
6. 🔴 **OBP 6 本中 5 本が canonical 未登録**（Cramant 2017 / Cuis 2019 / GTC 2016 / GTC 2014 / Oger 2017）。
   **本バッチ最多。**すべて**公式テクニカルシートが存在し、区画構成・生産本数・ドザージュまで確定済み**であるため、
   **Packet B（新規キュヴェ）として即座に登録可能な状態**にある。
7. 🔴 **メニュー印字「Grand Terriors de Chardonnay」は誤植**（正: `Grands Terroirs de Chardonnay`）。
   **同一誤植が 2 行（2016 / 2014）に存在する。**intake の alias 規則で吸収するか、メニュー修正を提案するかの判断が必要。
8. 🔴 **OBP は 6 本すべてを `Brut` と印字しているが、公式はすべて `Extra-Brut`。**
   canonical のキュヴェ命名規約（`… Special Club Brut`）が**公式と乖離している。**
   Chouilly の既存 canonical 名もこの誤りを含む。**命名規約レベルの判断が必要（architecture 案件）。**
9. ⚠️ **`'Oger,' Grand Cru` は 2 つの別キュヴェを指しうる** — Spécial Club の**ミレジム版**（OBP の 2017 はこちら）と、
   ノンヴィンテージの **`Oger Grand Cru` ブリュット SA**。公式サイトも製品ページを 2 つ持つ（`/produit/oger-grand-cru/` と
   `/produit/oger-grand-cru-2/`）。**canonical 登録時に両者を分離しないと将来必ず衝突する。**
10. ⚠️ **`Cuis 1er Cru` も同様に 2 つ存在する** — ブリュット SA（`/produit/cuis-1er-cru/`）と
    Spécial Club ミレジム（`/produit/cuis-1er-cru-special-club/`）。**OBP の 2019 は後者。**
    **公式サイト自身が両ページに同じタイトル「Cuis 1er Cru」を付けている**ため、機械照合は必ず誤る。
