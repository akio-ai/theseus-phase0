# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは存在しない。** 本書は昇格前の研究記録であり、**何も作成していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公的一次資料で確認**（下記 §Sources の 4 系統。**生産者自身のサイトは存在しない** → 後述）
> `📄` 単一の非公式資料のみ（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05
>
> ## 🔴🔴 このドシエは他と成り立ちが違う。先にこれを読むこと
>
> **生産者の公式サイトは、本調査時点で機能していない。**
> `https://ganevat.fr/` および `https://www.ganevat.fr/` は **HTTP 200 を返すが、内容は
> 「Site en maintenance / Nous effectuons des opérations de maintenance. Revenez bientôt!」の
> メンテナンス画面のみ**（1,539 bytes）。`sitemap.xml` は **404**、`robots.txt` は `User-agent: *` の 1 行のみ。
> **`domaine-ganevat.com` / `.fr` / `jfganevat.com` などの候補ドメインはいずれも名前解決しない。**
>
> 🔴 **したがって本ドシエには「造り手が自分で語った言葉」が一行も無い。**
> **代わりに、公的機関と認証機関という一次資料 4 系統だけで構成した。**
>
> | 系統 | 何を確定できたか |
> |---|---|
> | **Agence Bio**（仏・公的機関）の事業者オープンデータ | 🔴 **法人が 2 つ存在し、活動範囲が違う** |
> | **Ecocert France**（認証機関）の証明書レジストリ | 🔴 **2 法人それぞれの EU 有機認証と活動区分** |
> | **Demeter France**（認証機関）の加盟者ページ | 🔴 **ビオディナミ認証と、認証済みキュヴェ 20 件の名前とヴィンテージ** |
> | **INAO 認証の cahier des charges**（CIVJ 公式配布 PDF）＋ **CIVJ** | **AOC Côtes du Jura の法的定義** |
>
> ✅ **この構成の利点**: 認証は**造り手の自己申告ではなく認証機関の記録**であり、自己申告より強い。
> ⚠️ **この構成の限界**: **歴史・栽培の実践・醸造は一行も裏が取れていない。** → §Confidence / §Open Questions

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Ganevat** |
| 🔴 **公的登録名（2 法人）** | ✅ **① `DOMAINE GANEVAT`**（Agence Bio raison sociale。Ecocert 表示は `DU DOMAINE GANEVAT`、Demeter 表示は `EARL DU DOMAINE GANEVAT`）<br>✅ **② `ANNE ET JEAN-FRANÇOIS GANEVAT`**（Ecocert 表示は `ANNE ET JEAN FRANCOIS GANEVAT`） |
| **SIRET ①** | ✅ **42169462100010** |
| **SIRET ②** | ✅ **79961576000011** |
| 🔴 **活動区分 ①** | ✅ **`Production` ＋ `Préparation`**（Agence Bio）／ **`Agriculteur (production végétale), Fabricant & Transformateur`**（Ecocert）<br>= **自ら栽培し、自ら醸造する** |
| 🔴 **活動区分 ②** | ✅ **`Préparation` のみ**（Agence Bio）／ **`Fabricant & Transformateur`** のみ（Ecocert）<br>= 🔴 **栽培をしない。醸造・仕立てのみ** |
| **生産物 ①** | ✅ **`Vins de raisin` / `Raisin de cuve` / `Prairie permanente`**（＝ワイン・醸造用ブドウ・恒久草地） |
| **生産物 ②** | ✅ **`Vins de raisin` のみ** |
| **所在（共通）** | ✅ **La Combe, 39190 Rotalier**（Jura 県）<br>Agence Bio は 2 法人とも **`2 La Serpentine, Lieu-dit La Combe, 39190 ROTALIER`** と **`351 Rue/Route de Conliège, 39570 Perrigny`** の 2 住所を登録 |
| **連絡先** | ✅ **+33 (0)6 70 19 11 37**（Demeter 掲載）／ **03 84 25 02 69・anne.ganevat@orange.fr**（CIVJ 掲載。担当 `Mme GANEVAT`） |
| **公式サイト** | 🔴 ⚠️ **`ganevat.fr` は存在するがメンテナンス中で内容ゼロ。** 本調査では一行も取得できなかった |
| **AOC** | ✅ **Côtes du Jura**（OBP 掲載 7 本すべて。**Rotalier は AOC の指定コミューン**） |
| canonical id | 🔴 **無し**（canonical 生産者 384 件を `ganevat` で走査 → **0 件**） |

---

## Overview

🔴 ✅ **本ドシエで最も重要な確定事実は「Ganevat という名の下に、活動範囲の違う法人が 2 つある」ことである。**

公的レジスタ（Agence Bio）と認証機関（Ecocert）が、**独立に同じ構造を記録している**。

- **`DOMAINE GANEVAT`** は **栽培＋醸造**。生産物に **`Raisin de cuve`（醸造用ブドウ）** と
  **`Prairie permanente`（恒久草地）** が含まれる ＝ **畑と土地を持つ実体。**
- **`ANNE ET JEAN-FRANÇOIS GANEVAT`** は **醸造・仕立てのみ。** 生産物は **`Vins de raisin` だけ** で、
  **`Raisin de cuve` が無い ＝ 自らブドウを育てていない。**

🔴 **これは THÉSEUS にとって設計上の分岐である。**
canonical に登録する際、**1 生産者にまとめるか 2 生産者に分けるか**を決めなければならない。
**既登録の `P-7`（Chave / Chave Sélections。「ブランド軸の実体化。統合禁止」）と同型**である。
→ §Canonical Conflict

✅ **認証は 2 系統とも確定している。**
**2 法人とも EU 有機規則 (EU) 2018/848 に基づく `Certification Agriculture biologique Europe` を
Ecocert France から受けており、Agence Bio 上の状態は 2 法人とも `ENGAGEE`。**
加えて **`EARL DU DOMAINE GANEVAT` は Demeter France の加盟者として掲載され、
ビオディナミ認証キュヴェが 20 件公表されている。**

🔍 **THÉSEUS における状態は最悪の部類。canonical に生産者レコードが無く、OBP 掲載 7 本すべてが
`producer_state = unresolved`。** ジュラのセクション自体が canonical で薄い可能性がある。

---

## History

🔴 ⚠️ **本調査では歴史を一件も確定できなかった。**

**公式サイトがメンテナンス中であり、公的レジスタと認証機関のデータには沿革が含まれない。**
INAO の cahier des charges はアペラシオンの歴史を書くが、**この生産者の歴史ではない。**

✅ **唯一、アペラシオン側の年号だけが公的資料で確定する** —
**AOC `Côtes du Jura` は 1937 年 7 月 31 日のデクレで初めて認められ、
現行の cahier des charges は 2011 年 9 月 23 日のデクレ n°2011-1189（JORF 2011 年 9 月 27 日）で承認された。**

🔴 **「創業年」「何代目」「いつ有機に転換したか」「いつビオディナミを始めたか」は、
本ドシエでは一切主張しない。** 巷間よく流布している数字（1650 年創業・14 代目・1998 年就任・
2006 年からビオディナミ・SO2 全廃 など）は、**本調査で一次資料に当たらなかった。**
→ **`awaiting material from the team`。** → §Staff Notes ⚠️ ① / Open Questions 2

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Jura**（Jura 県 39） ✅ |
| **コミューン** | ✅ **Rotalier（39190）**、lieu-dit **La Combe** |
| **AOC** | ✅ **Côtes du Jura** |
| **第 2 住所** | ✅ **351 Rue/Route de Conliège, 39570 Perrigny**（2 法人とも Agence Bio に登録。用途は ❓） |

### ✅ AOC Côtes du Jura の公的定義（INAO 認証 cahier des charges ／ CIVJ）

| | |
|---|---|
| 初認定 | **1937 年 7 月 31 日のデクレ** |
| 現行 cahier des charges | **デクレ n°2011-1189（2011 年 9 月 23 日）** |
| 対象 | **白・赤・ロゼの tranquille（スティル）ワイン** |
| 補足呼称 | **`vin de paille`** と **`vin jaune`** を名称に付加できる |
| 面積 | **551 ha**（CIVJ）。**105 コミューン**にまたがり、**Rotalier を含む** |
| 位置づけ | **ジュラで生産量第 2 位の AOC**（CIVJ） |

**✅ 認可品種（cahier des charges V. Encépagement）**

| 種別 | 主要品種 | 補助品種 |
|---|---|---|
| **白** | **chardonnay B, savagnin B** | pinot noir N, poulsard N（**現地名 ploussard**）, trousseau N |
| **赤・ロゼ** | **pinot noir N, poulsard N, trousseau N** | chardonnay B, savagnin B |
| `vin de paille` | chardonnay B, poulsard N, savagnin B, trousseau N | — |
| `vin jaune` | 🔴 **savagnin B のみ** | — |

**✅ 栽培規定（同 VI.）**
- **植密度は最低 5,000 本/ha**（テラス植えを除く）。**1 本あたり最大 2 m²、畝間 2 m 以下**
- **剪定は Guyot simple / Guyot double / taille courte（cordon de Royat）のみ**
- 芽数上限: **chardonnay・poulsard・savagnin・trousseau は 20 眼/株かつ 120,000 眼/ha。
  pinot noir は 80,000 眼/ha**

**✅ 収量（同 VIII.）**
| | 基準収量 | butoir（上限） |
|---|---|---|
| **白** | **60 hl/ha** | **72 hl/ha** |
| **赤・ロゼ** | **55 hl/ha** | ❓ 本抜粋では未取得 |
| `vin de paille` | **20 hl/ha** | — |

⚠️ **これはアペラシオンの法定上限であり、この生産者の実収量ではない。**

---

## Farming

🔴 ✅ **認証は確定している。実践は確定していない。この区別が本節の全てである。**

| 認証 | 対象 | 記録者 | 内容 |
|---|---|---|---|
| **EU 有機 (EU) 2018/848** | **`DU DOMAINE GANEVAT`** | **Ecocert France** | `Certification Agriculture biologique Europe`。活動区分 **`Agriculteur (production végétale), Fabricant & Transformateur`** |
| **EU 有機 (EU) 2018/848** | **`ANNE ET JEAN FRANCOIS GANEVAT`** | **Ecocert France** | 同上。活動区分 **`Fabricant & Transformateur`**（**栽培なし**） |
| **有機事業者登録** | **2 法人とも** | **Agence Bio**（公的機関） | 状態 **`ENGAGEE`**、認証機関はいずれも **Ecocert France** |
| 🔴 **Demeter（ビオディナミ）** | **`EARL DU DOMAINE GANEVAT`** | **Demeter France** | **加盟者として掲載。製品カテゴリ `Vins, bières et spiritueux`。認証キュヴェ 20 件を公表**（→ §Important Cuvées） |

🔴 **`Prairie permanente`（恒久草地）が Agence Bio の生産物として登録されている点は、
栽培のあり方を示唆する数少ない公的手がかりである。**
⚠️ **ただし「草生栽培をしている」と言うのは踏み込みすぎである。**
**登録されているのは「恒久草地という生産物カテゴリ」であって、畑の管理方法ではない。**

### ⚠️ 本節で確定できなかったこと（**すべて `awaiting material from the team`**）

- **有機・ビオディナミへの転換年**（Ecocert / Demeter のページに掲載日・取得日が無い）
- **面積**（**公的資料のどこにも ha が無い。「13 ha」という数字は一次資料で確認できなかった**）
- **樹齢・植密度・剪定・実収量・被覆作物・馬耕・SO2 の扱い**
- **区画名と品種の対応**（キュヴェ名からの推測はしていない）

---

## Winemaking

🔴 ⚠️ **本調査では醸造について一件も確定できなかった。**

**確定しているのは「法人 ① は栽培から醸造まで行い、法人 ② は醸造・仕立てのみを行う」という
活動区分だけである。** これは Agence Bio と Ecocert が独立に記録している。

⚠️ **「SO2 無添加」「マセラシオン期間」「熟成容器」「フードル / 樽 / アンフォラ」「ウイヤージュの有無」
「vin jaune を造るか」は、いずれも本ドシエでは主張しない。**

🔍 **一点だけ、認証データから機械的に言えること** —
**Demeter が公表する 20 キュヴェに `vin jaune` も `vin de paille` も含まれていない。**
⚠️ **ただしこれは「造っていない」ことの証明ではない。**
**Demeter のリストは「ビオディナミ認証を受けた製品」のリストであり、生産品目の全量ではない。**
→ §Staff Notes ⚠️ ⑤

---

## Style

⚠️ **公式のテイスティングノートが存在しない**（サイトがメンテナンス中）。
**本ドシエはスタイルについて一切主張しない。**

🔍 **色と品種について、Demeter の製品名から機械的に言えることのみ**（→ §Important Cuvées の表）。
**`Les Grands Teppes` は白（Chardonnay 系）と赤（Pinot Noir）の両方が存在する。**
**`Julien en Billat : enfant terrible du sud` は Poulsard である。**
**これは色と品種の対応であって、味わいの記述ではない。**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 7 本。すべて `unresolved`**）

| # | OBP 印字 | 色 | VT | 価格 | ✅ **Demeter 認証リストとの突合** |
|---|---|---|---|---|---|
| 1 | **'Les Grands Teppes,'** Côtes du Jura | **白** | 2018 | $600 | ✅ 🔴 **完全一致** — `Vin blanc Côtes du Jura "Les Grands Teppes" 2018 - 2019 - 2020`。**2018 は認証年に含まれる** |
| 2 | **'Les Varrons'** Côtes du Jura | **白** | 2020 | $560 | 🔴 ⚠️ **Demeter の 20 件に該当なし。** → Open Questions 4 |
| 3 | **'Les Survivants,'** Côtes du Jura | **白** | 2021 | $480 | ✅ 🔴 **完全一致** — `Vin blanc Côtes du Jura "Les Survivants" 2021`。**ヴィンテージまで一致** |
| 4 | **'Cuvée de l'Enfant Terrible,'** Côtes du Jura | **赤** | 2023 | $360 | ⚠️ **その名では該当なし。** 近いのは `poulsard "julien en billat : enfant terrible du sud"` → Open Questions 5 |
| 5 | **'Cuvée de l'Enfant Terrible,'** Côtes du Jura | **赤** | 2022 | $360 | ⚠️ 同上 |
| 6 | **'Julien en Billat - L'Enfant Terrible du Sud,'** Côtes du Jura | **赤** | 2024 | $440 | ✅ 🔴 **一致** — `Vin rouge côtes du jura poulsard "julien en billat : enfant terrible du sud" 2020 - à 2024`。**品種は Poulsard。2024 は範囲に含まれる** |
| 7 | **'Les Grands Teppes,'** Côtes du Jura | **赤** | 2023 | $440 | ✅ 🔴 **一致** — `Vin rouge côtes du jura " pinot les grands teppes" 2020 - 2022 - 2023`。**品種は Pinot Noir。2023 は含まれる** |

🔴🔴 **`Les Grands Teppes` は白と赤の両方に存在する。これがこの生産者最大の実務的な罠である。**
**OBP は白 2018（$600・WHITE セクション）と赤 2023（$440・RED セクション）の 2 本を載せており、
Demeter のリストも `Vin blanc … "Les Grands Teppes"` と `Vin rouge … "pinot les grands teppes"` の
2 系統を別に記載している。**
**赤は Pinot Noir。白の品種は Demeter の記載からは確定しない**（`chardonnay` の語が付いていない）→ Open Questions 3

### ✅ Demeter France が公表する認証キュヴェ 20 件（**全件・原文のまま**）

**白**
| キュヴェ | 品種表記 | 認証ヴィンテージ |
|---|---|---|
| **Les Grands Teppes** | （記載なし） | **2018 - 2019 - 2020** |
| Les rescapés | （記載なし） | 2021 |
| **Les Survivants** | （記載なし） | **2021** |
| Chalasses | chardonnay | 2018 - 2019 |
| Chamois du Paradis | chardonnay | 2018 à 2020 |
| En Billat | chardonnay | 2018 - 2019 |
| Florine | chardonnay | 2018 - 2019 - 2020 |
| Grusse en Billot | chardonnay | 2018 |
| Marguerite | chardonnay | 2018 - 2019 |
| Orégane | chardonnay | 2018 - 2019 |
| Antide | savagnin | 2018 - 2020 |
| Billat | savagnin | 2019 - 2020 |
| Les Dévoilés | savagnin | 2020 |
| Sous la Roche | savagnin | 2019 |

**赤**
| キュヴェ | 品種表記 | 認証ヴィンテージ |
|---|---|---|
| **Les Grands Teppes** | **pinot** | **2020 - 2022 - 2023** |
| En Billat | pinot | 2020 - 2022 - 2023 |
| Julien | pinot | 2020 - 2022 - 2023 |
| Chalasses Vieilles Vignes | poulsard | 2018 - 2020 - 2022 - 2023 |
| **Julien en Billat : enfant terrible du sud** | **poulsard** | **2020 - à 2024** |
| Plein Sud | trousseau | 2020 - 2022 - 2023 |

🔍 **`En Billat` も `Julien` も、白（chardonnay / savagnin）と赤（pinot / poulsard）に重複して現れる。**
**この生産者は区画名を色と品種をまたいで使う。** → §Staff Notes ⚠️ ④

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① ジュラ・ロタリエのビオディナミの造り手。認証は認証機関の記録で確認できている。**
「**ジュラ県ロタリエ村、リュー・ディ『ラ・コンブ』**の造り手です。
**EU の有機認証を Ecocert France から受けており、さらに Demeter のビオディナミ認証も持っています。**
これは造り手の自己申告ではなく、**認証機関自身が公表している記録**です。
アペラシオンは **コート・デュ・ジュラ**、ロタリエはその指定コミューンのひとつです。」

**② `Les Grands Teppes` は白と赤の 2 つがある。これを取り違えない。**
「**同じ『レ・グラン・テップ』という区画名で、白と赤の両方が造られています。**
**赤はピノ・ノワール**であることが認証記録で確認できます。
リストの **2018 年は白、2023 年は赤**です。**同じ名前ですが別のワインです。**」

**③ 造り手側の資料が今は取れない。だから畑や醸造の話は「していない」。**
「**この造り手は現在、公式サイトがメンテナンス中で、造り手自身の説明が公開されていません。**
ですので**面積・樹齢・醸造の詳細は、こちらから確かなことを申し上げられません。**
確かなのは **産地・アペラシオン・認証・品種**までです。」

### 追加で使える一手

- **`Julien en Billat - L'Enfant Terrible du Sud`（2024・$440）**: 「**プールサール（現地では ploussard とも）**です。
  **認証記録で 2020 年から 2024 年までのヴィンテージがビオディナミ認証を受けている**ことが確認できます。」
- **アペラシオンの話に逃がすなら**: 「**コート・デュ・ジュラは 1937 年認定、105 のコミューンにまたがる 551 ヘクタール。
  白の主要品種はシャルドネとサヴァニャン、赤はピノ・ノワール、プールサール、トゥルソー**です。
  **ヴァン・ジョーヌを名乗れるのはサヴァニャン 100% だけ**と法令で決まっています。」
- **数字で語るなら（アペラシオンの法定値として）**: 「**白は 60 hl/ha、赤とロゼは 55 hl/ha が基準収量、
  植密度は最低 5,000 本/ha、剪定はギヨ単／双またはコルドン・ド・ロワイヤのみ**が認められています。」

### ⚠️ 言ってはいけないこと（**一次資料の裏が無い／出典が沈黙している**）

1. 🔴 ⚠️ **創業年・世代数・当主の就任年を言わない。**
   「1650 年創業」「14 代目」「1998 年に継承」「2006 年からビオディナミ」といった数字は
   **本調査でどの公的資料にも当たらなかった。** **公式サイトはメンテナンス中で読めない。**
2. 🔴 ⚠️ **「SO2 無添加」と言わない。** **どの一次資料にも記載が無い。**
   有機・ビオディナミ認証は **SO2 の上限を定めるが、無添加を意味しない。**
3. ⚠️ **面積を「13 ヘクタール」と言わない。** **Agence Bio にも Ecocert にも Demeter にも
   面積の記載が無い。** 本調査で一次資料に当たらなかった。
4. 🔴 ⚠️ **区画名を色や品種と結びつけて一般化しない。**
   **`Les Grands Teppes` `En Billat` `Julien` は白にも赤にも存在する。**
   **「ビラの畑はシャルドネです」と言うと外す。**（`En Billat` は chardonnay の白・savagnin の白・
   pinot の赤・poulsard の赤の 4 通りが認証リストに並んでいる。）
5. ⚠️ **「ヴァン・ジョーヌは造っていない」と言わない。**
   **Demeter の認証リストに無いだけであり、リストは生産品目の全量ではない。**
6. 🔴 ⚠️ **`Ganevat` を一つの造り手として断定的に語らない。**
   **公的レジスタ上、`DOMAINE GANEVAT`（栽培＋醸造）と
   `ANNE ET JEAN-FRANÇOIS GANEVAT`（醸造のみ・栽培なし）の 2 法人が併存する。**
   **リストのどの 1 本がどちらの法人のものかは、本調査では特定できていない。**
   言うなら「**ガヌヴァの名で出ているワインには、自社畑のものと、そうでないものがある可能性があります**」まで。
7. ⚠️ **`Les Varrons` について認証を語らない。** **Demeter の 20 件に含まれていない。**
   **「ビオディナミです」と言えるのは、認証リストに載っているキュヴェだけ。**
8. ⚠️ **`Cuvée de l'Enfant Terrible`（2022 / 2023）と
   `Julien en Billat - L'Enfant Terrible du Sud`（2024）を同じワインとして語らない。**
   **メニューが別の行として印字しており、認証リストにあるのは後者だけである。**
9. ⚠️ **テイスティングノートを造り手の言葉として語らない。** **公式の記述が一行も無い。**
10. ⚠️ **アペラシオンの法定収量を「この造り手の収量」として言わない。**
    **60 / 55 hl/ha は AOC の上限であって実績値ではない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

**新規の登録なし。**

🔍 **理由は「衝突が無い」ではなく「レコードが存在しない」。**
canonical `wine_makers.json`（全 384 生産者）を `ganevat` で走査 → **0 件。**
**この生産者は THÉSEUS に一切登録されていない。** キュヴェ 0 件・ヴィンテージ 0 件。

🔴 **ただし登録時に必ず踏む分岐がある。既存の `P-7` と同型なので、新しい番号は開かない。**

**`P-7`（ブランド軸の実体化・統合禁止）と同型の構造** —
公的レジスタ上、**`DOMAINE GANEVAT`（Production ＋ Préparation）** と
**`ANNE ET JEAN-FRANÇOIS GANEVAT`（Préparation のみ）** は **SIRET の異なる別法人**であり、
**活動区分が違う。** `Chave` / `Chave Sélections` と同じく **統合してはならない**可能性が高い。

⚠️ **ただし決定的な差がある。** Chave の場合は **OBP 側が 2 つを別に印字していた**ため分離が保てた。
**Ganevat の場合、OBP は 7 本すべてを `Ganevat` の 1 語で印字している。**
🔴 **したがって「どの 1 本がどちらの法人か」をメニューの印字から決めることはできない。**
**分離して登録すると、7 本すべてが振り分け不能になる。**
→ **これは research では解けない。設計判断。** → Open Questions 1

---

## Sources

🔴 **生産者自身の一次資料は存在しない（サイトがメンテナンス中）。以下はすべて公的機関・認証機関の一次資料。**

| 資料 | 発行者 | 取得した情報 |
|---|---|---|
| 🔴 **`opendata.agencebio.org/api/gouv/operateurs/?q=ganevat`** | **Agence Bio**（仏・農業省が設立した公的機関） | 🔴 **2 法人の SIRET・raison sociale・住所 2 件ずつ・活動区分（`Production` / `Préparation`）・生産物カテゴリ・認証機関（Ecocert France）・状態 `ENGAGEE`** |
| 🔴 **`certificat.ecocert.com/entreprise/80D2CB5F-…`** | **Ecocert France**（認証機関） | **`DU DOMAINE GANEVAT`** — La Combe 39190 ROTALIER。活動 **`Agriculteur (production végétale), Fabricant & Transformateur`**。**`Certification Agriculture biologique Europe (EU) 2018/848`** |
| 🔴 **`certificat.ecocert.com/entreprise/86189421-…`** | **Ecocert France** | **`ANNE ET JEAN FRANCOIS GANEVAT`** — GANEVAT, LA COMBE 39190 Rotalier。活動 **`Fabricant & Transformateur`** のみ。同認証 |
| 🔴 **`demeter.fr/adherents/e-a-r-l-du-domaine-ganevat/`** | **Demeter France**（ビオディナミ認証機関） | 🔴 **`EARL DU DOMAINE GANEVAT` の加盟者掲載。認証キュヴェ 20 件の名称・色・品種表記・ヴィンテージ範囲**（本ドシエ §Important Cuvées に全件転記）。連絡先 +33 (0)6 70 19 11 37 |
| **`Cahier_des_charges_Cotes_du_Jura.pdf`**（CIVJ 公式配布・INAO 承認文書） | **INAO / 農業省**（デクレ n°2011-1189、JORF 2011-09-27） | **AOC の法的定義・初認定 1937-07-31・対象は白赤ロゼの tranquille・`vin jaune` / `vin de paille` の付加・認可品種・植密度 5,000 本/ha・剪定 3 方式・芽数上限・収量 60 / 55 / 20 hl/ha・butoir 72 hl/ha・コミューン一覧（Rotalier を含む）** |
| **`jura-vins.com/aoc-cotes-du-jura.htm`** | **Comité Interprofessionnel des Vins du Jura**（Château Pécauld, Arbois） | **551 ha・105 コミューン・ジュラ第 2 位の AOC** |
| **`jura-vins.com/details-domaine-ganevat-…,337.htm`** | **CIVJ** | **`GANEVAT Anne et Jean-François` / La Combe 39190 ROTALIER / 03 84 25 02 69 / anne.ganevat@orange.fr / 担当 `Mme GANEVAT`** |

**取得を試みて取得できなかったもの**
- 🔴 **`https://ganevat.fr/` `https://www.ganevat.fr/`** — **HTTP 200。内容は「Site en maintenance」のみ**（1,539 bytes）。
  **`/sitemap.xml` は 404。`/robots.txt` は `User-agent: *` の 1 行のみ。**
  ⚠️ **`ganevat.fr` は TLS 証明書のホスト名が一致しない**（`--insecure` でのみ取得できた）。
- **`domaine-ganevat.com` / `domaine-ganevat.fr` / `ganevat.com` / `jfganevat.com` /
  `anne-et-jean-francois-ganevat.fr`** — **いずれも名前解決しない。**
- **Ecocert の証明書 PDF 本体** — ダウンロードが日付・言語選択の JS フォームを経由するため、**未取得。**
  → **取得できれば認証の発効日と製品スコープが確定する。** → Open Questions 6
- **`extranet.inao.gouv.fr` の同 PDF** — タイムアウト。**CIVJ 配布の同一文書で代替した。**

**canonical / OBP（🔍 THÉSEUS DB。読み取りのみ・無変更）**
🔴 **canonical 生産者レコード: 存在しない**（384 件走査 → 0）／canonical キュヴェ **0 件**／
OBP **7 本**（すべて `match_state = unresolved`、`producer_state` も `unresolved`。
セクションは `FRANCE | WHITE > JURA` 3 本 ＋ `FRANCE | RED > JURA` 4 本）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | **High** | 🔴 **SIRET 2 件・登録名・住所・活動区分が、公的機関と認証機関の 2 系統で独立に一致** |
| Overview | **Medium-High** | 2 法人構造は確定。ただし**両者の関係の説明はどこにも無い** |
| **History** | 🔴 **None** | **一件も確定できなかった。** 公式サイトがメンテナンス中 |
| Location | **Medium-High** | コミューン・lieu-dit・AOC は確定。**面積は不明。第 2 住所（Perrigny）の用途も不明** |
| **Farming** | **Medium** | 🔴 **認証は確定（Ecocert の EU 有機 ＋ Demeter）。実践は一切不明。** 認証は自己申告より強い一方、実践の記述はゼロ |
| **Winemaking** | 🔴 **None** | **活動区分（栽培する / しない）以外は一件も確定できなかった** |
| Style | 🔴 **None** | **公式のテイスティングノートが存在しない** |
| **Important Cuvées** | **Medium-High** | 🔴 **OBP 7 本中 4 本を認証機関のキュヴェ名・ヴィンテージと突合できた**（うち 2 本は品種まで確定）。**1 本は該当なし、2 本は名称が一致しない** |
| Staff Notes | **High** | ⚠️ 10 項目。🔴 **「言えないこと」が多い生産者であり、⚠️ リストこそが本ドシエの価値である** |
| **総合** | 🔴 **Medium — 条件つきで staff-usable。** | **産地・アペラシオン・認証・一部の品種は嘘なく語れる。歴史・栽培の実践・醸造・味わいは語れない。** ⚠️ リストがその境界を明示している |

**reached_70: NO（暫定 ~55%）。**

🔴 **意図的に 70% に届かせていない。** 70% の定義は
「**ソムリエがフロアで、何も嘘を言わずにこの生産者について語れる**」だが、
**この生産者については History / Winemaking / Style を語る材料が一次資料に存在しない。**
**推測で埋めれば 70% に見せられるが、それは規約違反である。**
→ **`ganevat.fr` の復旧、または輸入元のテクニカルシートの提供を待つ。**
**この 1 件は `awaiting material from the team` として扱うべきである。**

---

## Open Questions

1. 🔴 **canonical に 1 生産者として登録するか、2 生産者に分けるか。**
   公的レジスタ上 **`DOMAINE GANEVAT`（栽培＋醸造）** と
   **`ANNE ET JEAN-FRANÇOIS GANEVAT`（醸造のみ）** は別法人・別 SIRET・別活動区分。
   **`P-7`（Chave / Chave Sélections）と同型だが、OBP が 7 本すべてを `Ganevat` の 1 語で印字するため、
   分離すると振り分け不能になる。** → **設計判断。research では解けない。**
2. 🔴 **`ganevat.fr` の復旧待ち。** 本ドシエの History / Farming の実践 / Winemaking / Style は
   **すべてこのサイトの復旧に依存している。** **定期的な再訪が要る。**
3. **白の `Les Grands Teppes` の品種。** Demeter の記載は `Vin blanc Côtes du Jura "Les Grands Teppes"` で
   **品種名が付いていない**（他の白は `chardonnay` / `savagnin` と明記されている）。
   **Chardonnay か Savagnin かアッサンブラージュかは確定しない。**
4. 🔴 **`Les Varrons`（OBP $560・2020）が Demeter の 20 件に無い。**
   **考えられる理由は複数ある**（ネゴス法人の製品／認証範囲外／リストが網羅的でない）が、
   **一次資料からは判定できない。** **「ビオディナミです」と言えない 1 本である。**
5. **`Cuvée de l'Enfant Terrible`（2022 / 2023）と
   `Julien en Billat : enfant terrible du sud`（2020–2024）の関係。**
   **同一ワインの表記揺れか、別キュヴェか。** OBP は**別の行として両方を載せている。**
6. **Ecocert の証明書 PDF が未取得。** ダウンロードが JS フォーム経由。
   **取得できれば認証の発効日・製品スコープ・失効の有無が確定する。**
   → **ブラウザ描画で取得すれば埋まる。**
7. **`351 Rue/Route de Conliège, 39570 Perrigny` の用途。**
   **2 法人とも Agence Bio に登録している第 2 住所。** 醸造所か事務所か倉庫か不明。
   ⚠️ **Agence Bio 内でも `Rue` と `Route` で表記が揺れている。**
8. **面積。** 公的資料のどこにも記載が無い。
9. **赤・ロゼの収量 butoir。** 本抜粋では白の 72 hl/ha しか取得していない。
   **cahier des charges の該当箇所を読めば確定する。**
10. **OBP の 7 本すべてが `unresolved`。** canonical 生産者レコードが無いことが直接の原因。
    → **登録は canonical への書き込みであり、本書では行っていない。** 昇格可否は Akio / CTO 判断。
