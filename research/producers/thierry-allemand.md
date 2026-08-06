# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 登録済（5 件）**
> 🔴 **本書は昇格前の研究記録であり、canonical を一切変更していない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式資料**（**本書には 1 件も無い。§Sources 参照**）
> `🏛` **公的登記・規制一次資料**（INAO cahier des charges／INSEE-Sirene 企業登記／Agence Bio／
>   DGFiP 地籍オープンデータ／Demeter France 認証規格／Biodyvin 会員名簿）
> `📄` 生産者作成だが自社ドメイン外（**本書では 0 件。取得した輸入元資料は authorship で棄却**）
> `⚠️` **出典間で食い違い／出典が沈黙している／第三者未検証**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
> `🔴` load-bearing finding
>
> 更新: 2026-08-06（JST）
>
> ---
>
> ## 🔴🔴 本ドシエ最大の結論 —— **メニューが誤っている側である。今回は明確にそうだ。**
>
> 🔍 **OBP メニューは 4 行すべてで生産者名を `Theirry Allemand` と印字している。**
> **`Thierry` の `i` と `r` が転置している。正しい綴りは `Thierry` である。**
> 🏛 **フランス国家企業登記（INSEE / Sirene）における法人名は `THIERRY ALLEMAND`
> （SIREN `432434637`）であり、代表者は `ALLEMAND THIERRY`（1963 年 3 月生）。**
> **公的登記が `Thierry` を確定させるので、これは推測ではなく確認である。**
>
> 🔴 **Batch 10 は「メニューが defective な側とは限らない」という常設の警告を立て、
> 反例を 3 件出した。本バッチでも Alvina Pernot で 4 件目の反例が出ている。
> 本行はその逆のケース —— メニュー側の純粋な誤植である。**
> **警告そのものと同じくらい、「今回は違う」と明言することに価値がある。**
> **パターンの存在は個別行の証拠にならない、という原則は両方向に効く。**
>
> ---
>
> ## 🔴🔴 第 2 の結論 —— **`allemand-chaillot-nv` は Cornas ではありえない**
>
> 🏛 **INAO『Cornas』cahier des charges 第 I 章 III は
> 「L'appellation d'origine contrôlée « Cornas » est réservée aux vins tranquilles rouges」
> —— スティルの赤ワインに限る、と定める。**
> 🏛 **同 II は「Dénominations géographiques et mentions complémentaires : Pas de disposition
> particulière」—— 補完的表示の規定を一切持たない。**
> 🏛 **さらに申告制度（第 II 章 I）は `déclaration de récolte` を軸に構築されており、
> 収穫年をまたぐブレンドを想定した条項は cahier des charges のどこにも存在しない。**
> 🔴 **すなわち AOC Cornas に non-vintage という概念は無い。`vintage: "NV"` は成立しない値である。**
>
> 🔴 **そして `D-2026-08-05-12` は canonical 全体で `'NV'` を 88 件と実測し、
> 「non-vintage Champagne については正当な値である」と読んだ。**
> 🔴 **本件はその読みへの反例である。`'NV'` の 88 件が全部 Champagne だとは限らない。
> 少なくとも 1 件は、NV がありえない静止赤ワイン AOC に付いている。**
> **`D-2026-08-05-12` の「NV は正当」という判断は、appellation 単位で再検証が要る。**
>
> ---
>
> ## 🔴🔴 第 3 の結論 —— **`Chaillot` と `Reynard` は実在する地籍リュー・ディである**
>
> 🏛 **DGFiP／Etalab 地籍オープンデータ（コミューン `07070` = Cornas）の
> リュー・ディ層は 39 の固有名を持ち、その中に `CHAILLOT` と `REYNARD` の両方が実在する。**
> 🏛 **かつ cahier des charges 第 XII 章 2°a) は
> 「より小さい地理的単位の名称をラベルに記載してよい。ただし ① 地籍上のリュー・ディであること
> ② 収穫申告に記載されていること」を条件として明示的に許可している。**
> 🔴 **したがって `Chaillot` / `Reynard` は空想的なキュヴェ名ではなく、
> AOC が法的経路を用意している地籍名である。これは floor で使える確定事実である。**
> ⚠️ **ただし cahier des charges の本文に `Chaillot` / `Reynard` の語は 0 回しか現れない
> （＝ appellation が個別に列挙・格付けしているのではない）。Batch 8 の Niellon `Truffière` と
> 同じ「呼称の法的粒度より下」の形だが、Cornas には一般条項としての経路がある点が異なる。**
>
> ---
>
> ## 🔴 生産者自身の資料は 1 行も無い —— **不在を証明した**
>
> 🏛 **`thierryallemand.com` / `thierry-allemand.com` / `domainethierryallemand.com` は
> Verisign RDAP で `404`（＝未登録）。`thierryallemand.fr` / `thierry-allemand.fr` は
> AFNIC RDAP で `NOT_FOUND_DOMAIN_NAME_WITH_NAME`。DNS も A/AAAA/MX すべて空。**
> 🏛 **Internet Archive の availability API は 4 ドメインすべてで
> `{"archived_snapshots": {}}` を `HTTP 200` で返した（＝ゲートではなく、確定した空）。**
> 🏛 **Agence Bio に事業者レコードそのものが存在しないため `siteWebs` 欄も存在しない。**
> 🔴 **本バッチはこれで 4 つ目の「不在の形」を得た ——
> ① OVH プレースホルダー（Roulot）② NXDOMAIN（Niellon）
> ③ 保有しているが未公開・9 バイト応答（Alvina Pernot）
> ④ 🔴 **本件 = ドメインが一度も登記されたことがない（RDAP 404 + Wayback 0 件）**。**
>
> 🔴 **したがって `## History` / `## Winemaking` / `## Style` は空白である。埋めていない。**
> 🔴 **とりわけ「無亜硫酸（sans soufre）」——この生産者について最も広く流布し、
> 最も頻繁に誤って語られる属性——について、本ドシエは一切の記述を拒否する。** → §Staff Notes ⚠️ ⑥

---

## Identity

| | |
|---|---|
| 🔴 **OBP 印字** | 🔍 **`Theirry Allemand`** —— **誤植。`i`/`r` 転置。4 行すべて同じ誤り** |
| **canonical 表記** | 🔍 **`Thierry Allemand`**（canonical レコード 5 件すべてこの表記・正しい） |
| 🔴 **公的登記上の法人名** | 🏛 **`THIERRY ALLEMAND`** — SIREN **`432434637`** / SIRET **`43243463700018`** |
| **法定形態** | 🏛 **SAS**（nature juridique `5710`）。**état `A`（活動中）** |
| **法人設立** | 🏛 **2000-07-01**。`date_debut_activite` = **2008-01-01** |
| 🔴 **登記上の代表者** | 🏛 **`ALLEMAND THIERRY`（1963 年 3 月生）= Président de SAS** |
| **NAF** | 🏛 **`01.21Z`（ブドウ栽培）**。IDCC `7024`（農業系協約） |
| **所在** | 🏛 **`22 impasse des Granges, 07130 Cornas, France`** |
| **座標** | 🏛 🔍 **lat 44.962225 / lon 4.848794**（Sirene） |
| **従業員規模** | 🏛 **INSEE 区分コード `02`（2023 年基準）** |
| **TVA** | 🏛 **`FR24432434637`** |
| **公表財務（2024）** | 🏛 **`résultat_net` = 217,979。`ca` = 0（申告値）** ⚠️ **CA 0 は非開示を意味しうる。額面で読まない** |
| 🔴 **同一住所の関連法人①** | 🏛 **`TA COMMERCIALISATION`** — SIREN `499357234` / SAS / **設立 2007-07-01** / NAF **`47.25Z`（飲料の専門店小売）** / Président = **`ALLEMAND THIERRY CHRISTIAN HENRI`（1963-03 生）** / TVA `FR28499357234` |
| 🔴 **同一住所の関連法人②** | 🏛 **`PETITE CERISE`** — SIREN `504587890` / **設立 2008-05-27** / NAF `68.20B` / Gérant = `ALLEMAND THIERRY CHRISTIAN HENRI` / **法人役員に `TA COMMERCIALISATION`** |
| 🔴 **同一住所の関連法人③** | 🏛 **`LA LOUBIE`** — SIREN `813919446` / **設立 2015-10-05** / NAF `68.32A` / Gérant = `ALLEMAND THIERRY CHRISTIAN HENRI` / 他に `HERENT EMMANUELLE JANIQUE` |
| 🔴 **同一住所の関連法人④** | 🏛 **`GFA LE GRAND CADE`** — SIREN `901621185` / **設立 2021-07-08** / NAF `68.20B` / **Gérant = `ALLEMAND THIERRY CHRISTIAN HENRI`／Associé = `ALLEMAND THEO RENE-PAUL`** |
| 🔴 **同一住所の別事業者** | 🏛 **`THEO ALLEMAND`** — SIREN `909883225` / SIRET `90988322500015` / **個人事業主（NJ `1000`）** / **設立 2022-01-26** / NAF **`01.21Z`（ブドウ栽培）** / **état `A`** / 事業主 = **`ALLEMAND THEO RENE PAUL`** |
| 🔴 **有機認証** | 🏛 **無し。** Agence Bio を **SIRET 完全一致**で 3 事業者すべて照会 → **`nbTotal: 0`** |
| 🔴 **ビオディナミ認証** | 🏛 **無し。** Biodyvin 会員名簿（2025 年 224 名）に `ALLEMAND` も `CORNAS` も**現れない** |
| **公式サイト** | 🔴 🏛 **存在しない。ドメインが一度も登記されたことがない**（RDAP 404 / Wayback 0 件） |
| **canonical id** | 🔍 `allemand-chaillot-nv` / `allemand-chaillot-2001` / `allemand-chaillot-1999` / `allemand-reynard-2006` / `allemand-reynard-1998` |

### 🔴 ⚠️ 姓の部分一致は本件でも誤爆した（`D-2026-08-05-08`）

**同じ defect が本バッチ内で 3 度目、そして本ドシエ内で 2 経路同時に発火した。**

| 誤爆先 | どこで | 実体 |
|---|---|---|
| 🏛 **`ALLEMAND INVEST`**（SIREN `934432261`） | 企業登記を `Allemand` + 郵便番号 `07130` 近傍で検索 | **Saint-Péray 所在・2024-10-15 設立・NAF `68.20B`・役員は `MAUREAU (ALLEMAND) LUCIE` と `MAUREAU MAXIME`。** ⚠️ **Cornas の造り手ではない** |
| 🏛 **`GARAGE ALLEMAND`**（SIREN `480471903`） | 同上 | **Toulaud の自動車整備業（NAF `45.20A`）** |
| 🔴 🏛 **`LALLEMAND` 系 7 件** | **Agence Bio 公開 API の `?nom=allemand` 検索** | **`J P LALLEMAND` / `LALLEMAND BENJAMIN` / `LALLEMAND JEAN` / `INDIVISION LALLEMAND` 等が `allemand` クエリで返る。** 🔴 **国家有機登録簿自身の検索 API が同じ部分一致 defect を持っている。** **だから「名前で照会して 0 件」は証明にならず、`siret=` 完全一致でしか証明できない** |

🔴 **`THEO ALLEMAND` は誤爆ではない。同一住所（`22 impasse des Granges`）・同一 NAF（`01.21Z`）で
2022-01-26 に登記された、実在する別事業者である。**
⚠️ 🔴 **これは登記事実であって、事業承継の物語ではない。**
**Batch 8 は Roulot の 2 法人を物語として読むことを明示的に拒否した。本書も同じ扱いをする。**
**「息子に代替わりした」「引退した」等は本書からは一切導けない。** → §Staff Notes ⚠️ ②、Open Questions 4

---

## Overview

🔴 ⚠️ **この節は通常、生産者自身の自己規定で書かれる。本件にはそれが一行も無い。**
**以下はすべてフランス国家の公的登記と INAO・地籍から取れた事実だけである。**

🏛 **フランス・アルデッシュ県 Cornas 村、`22 impasse des Granges` に本拠を置く
ブドウ栽培事業体（NAF `01.21Z`）。法人形態は SAS、SIREN `432434637`、2000 年 7 月 1 日設立、
現在も活動中。代表者は 1963 年 3 月生まれの `Thierry Allemand`。従業員規模は INSEE 区分 `02`。**

🔴 🏛 **同一住所に、Thierry Allemand 本人が役員を務める法人が計 4 つ登記されている ——
飲料小売の `TA COMMERCIALISATION`（2007）、不動産系の `PETITE CERISE`（2008）と
`LA LOUBIE`（2015）、そして農地保有体 `GFA LE GRAND CADE`（2021）。**
🔴 **加えて、同一住所・同一 NAF で `THEO ALLEMAND` が 2022 年に個人事業主として登記されている。**
⚠️ **これらは登記上の構造であり、役割分担・実務・承継を意味しない。本書は解釈しない。**

🔴 🏛 **有機認証は無い。** **Agence Bio（フランス国家有機登録簿）に、
`43243463700018` / `90988322500015` / `49935723400016` の 3 SIRET を
完全一致で照会したところ、いずれも `nbTotal: 0` を返した。**
**INSEE 企業登記側の `est_bio` フラグも `false`、`liste_id_bio` も `null` である。**
🔴 🏛 **ビオディナミ認証も無い。** **Biodyvin の会員名簿（2025 年・224 名・全文取得）に
`ALLEMAND` は現れず、`CORNAS` の語も現れない。**
🔴 🏛 **Demeter も構造的に不可能である。** **Demeter France cahier des charges（2024 年 1 月版）は
「La certification biologique est une condition préalable pour être en conformité avec le présent
cahier des charges」——有機認証が前提条件であると明記する。有機認証が存在しない以上、
Demeter 認証は成立しえない。**

🔴 ⚠️ **したがって canonical の 5 レコードすべてが述べる「バイオダイナミック農法」および
`Biodynamic` タグは、いかなる認証によっても裏づけられない。** → §Canonical Conflict

🔍 **THÉSEUS における状態: canonical に `producer` フィールドが `Thierry Allemand` の
レコードが 5 件存在する（prose-only ヒットは 0 件）。OBP 掲載は 4 本。
4 本すべて `match_state: alias`（生産者名の誤植による）、`cuvee_state` と `vintage_state` は
4 本とも `exact`。** → §Important Cuvées

---

## History

🔴 ⚠️ **本ドシエは沿革を持たない。**

**公式サイトが存在せず（それどころかドメインが一度も登記されていない）、
生産者が公表した沿革文書が一件も存在しないためである。**
**創業年・畑の取得経緯・師事関係・世代交代は、一次資料が無いため本書では一切主張しない。**

🏛 **公的登記から機械的に読める「日付」だけを並べる。これは沿革ではなく登記事象である。**

| 日付 | 登記事象 🏛 | 出典 |
|---|---|---|
| **1938-08-05** | 🏛 **AOC「Cornas」が décret により初めて認定される**（*appellation の歴史であって Allemand の歴史ではない*） | INAO CDC |
| **1971-05-12** | 🏛 **INAO 全国委員会が Cornas の区画境界（aire parcellaire）を承認** | INAO CDC |
| **1981-11-10** | 🏛 **`NOEL VERSET`（SIREN `323099473`・NAF `01.21Z`・Cornas）が登記される** | INSEE / Sirene |
| **2000-07-01** | 🔴 🏛 **`THIERRY ALLEMAND`（SAS・SIREN `432434637`）設立** | INSEE / Sirene |
| **2007-07-01** | 🏛 **`TA COMMERCIALISATION`（SAS・飲料小売）設立** | INSEE / Sirene |
| **2008-01-01** | 🏛 **`THIERRY ALLEMAND` の本店事業所の活動開始日（`date_debut_activite`）** | INSEE / Sirene |
| **2008-05-27** | 🏛 **`PETITE CERISE` 設立** | INSEE / Sirene |
| **2008-10-31** | 🔴 🏛 **`NOEL VERSET` が `état C`（廃止）となる** | INSEE / Sirene |
| **2015-10-05** | 🏛 **`LA LOUBIE` 設立** | INSEE / Sirene |
| **2019-12-06** | 🏛 **現行 Cornas CDC の homologation（arrêté、JORF 2019-12-08 公示）** | INAO CDC |
| **2021-07-08** | 🏛 **`GFA LE GRAND CADE`（農地保有体）設立** | INSEE / Sirene |
| **2022-01-26** | 🔴 🏛 **`THEO ALLEMAND`（個人事業主・NAF `01.21Z`・同一住所）登記** | INSEE / Sirene |
| **2023-11-30** | 🏛 **CDC 改正案が INAO 全国委員会で承認（国内異議申立手続中）** | INAO CDC |

🔴 ⚠️ **上表を「沿革」として客に語ってはならない。**
**法人設立日 2000-07-01 は創業年ではない。**
🔴 **OBP の 1998 年と 1999 年のボトルは、この法人の登記より前である。** → §Staff Notes ⚠️ ①

### 🔴 canonical の `Noël Verset` 記述について —— **登記で「支持できない」と言える**

🔍 **canonical 5 レコードすべての `description` が
「かつてノエル・ヴェルセが所有していた畑を引き継ぎ」と書いている。**

🏛 **登記から言える事実:**
- **`NOEL VERSET`（SIREN `323099473`・NAF `01.21Z`・Cornas）は 1981-11-10 に登記され、
  🔴 2008-10-31 に廃止されている。**
- **Cornas には現在も Verset 名の事業体が複数、活動中で存在する ——
  `ALAIN VERSET`（SIREN `444780415`・2003 年）、
  `EARL DOMAINE VERSET A ET E`（SIREN `822442026`・NAF `01.21Z`・2016 年）、
  `GFV VERSET MOUTON`（SIREN `914114574`・2022 年）。**

🔴 **したがって: ① 畑の移転を示す一次資料は無い（地籍は所有者を公開しない）。
② Verset 名の栽培事業体は Cornas に今も存在する。
③ 仮に移転があったとしても `NOEL VERSET` の廃止は 2008 年であり、
OBP の 4 ヴィンテージ（1998 / 1999 / 2001 / 2006）はすべてそれより前である。**
🔴 **どの読み方をしても、この記述を OBP の 4 本の説明として使うことはできない。**
→ §Canonical Conflict、§Staff Notes ⚠️ ③

---

## Location

| | |
|---|---|
| **Country** | France 🏛 |
| **Region** | 🏛 **Vallée du Rhône septentrionale（北ローヌ）。** CDC は Cornas を **「Crus des Côtes du Rhône」**の一つと位置づける |
| **Commune** | 🏛 **Cornas（Ardèche 07）。INSEE コミューン番号 `07070`。郵便番号 `07130`** |
| **住所** | 🏛 **`22 impasse des Granges, 07130 Cornas`** |
| **座標** | 🏛 🔍 **44.962225 N, 4.848794 E** |
| 🔴 **畑の所在** | ❓ **不明。Allemand の所有区画リスト・面積を示す一次資料は存在しない**（→ ただし `Chaillot` / `Reynard` の**地籍上の位置**は下記で確定した） |

### 🏛 AOC『Cornas』の法的枠組み —— **appellation レベルの公的事実**

⚠️ **以下は AOC「Cornas」全体に対する INAO の規定であり、Thierry Allemand 固有の情報ではない。**
**この区別は絶対に崩さないこと。**

⚠️ **出典注記: 取得した cahier des charges は 2023-11-30 の全国委員会で承認された
「国内異議申立手続（PNO）」版であり、冒頭に「Cette modification du cahier des charges ne saurait
préjuger de la rédaction finale」と明記されている。現行の homologation は
`arrêté du 6 décembre 2019`（JORF 2019-12-08）である。**
🔴 ⚠️ **さらに PNO 版は改正部分を「旧値と新値の併記」で出力するため、
数値が連結して見える箇所がある**（例: `En 20092021 … environ 115160 hectares … 36005000 hectolitres`
＝ **2009 年: 約 115 ha / 3600 hl → 2021 年: 約 160 ha / 5000 hl** と読める）。
**Roulot の rendement で踏んだのと同じ罠である。本書では連結値をそのまま引用しない。**

| 項目 | 規定 🏛 |
|---|---|
| **初認定** | 🔴 **`décret du 5 août 1938`** |
| **色・種別** | 🔴 **「vins tranquilles rouges」—— スティルの赤のみ。白もロゼも泡も無い** |
| **補完的地理表示** | 🔴 **「Pas de disposition particulière」—— 規定を持たない** |
| **地理的範囲** | 🔴 **Cornas 村 1 コミューンのみ**（収穫・醸造・熟成すべて） |
| **区画境界** | 🏛 **1971-05-12 の全国委員会で承認。図面は Cornas 市役所に寄託** |
| 🔴 **品種** | 🔴 **`syrah N` のみ。** CDC 自身が「北ローヌの全 AOC の中で唯一、Syrah のみから造られる」と明記 |
| **植密度** | **最低 4,400 本/ha。1 本あたり最大 2.30 m²。畝間 2.50 m 以下** |
| **剪定** | **1 株あたり最大 8 芽。gobelet / cordon de Royat / Guyot 単・複。コルドン高さ最大 0.60 m** |
| 🔴 **仕立て** | 🔴 **`échalas`（棒仕立て）か「palissage plan relevé」のいずれか。échalas は最低 1.50 m** |
| **最大負荷** | **7,000 kg/ha。欠株率上限 20%** |
| **糖度** | **最低 171 g/L（果汁）** |
| **自然アルコール** | **最低 10.5 %vol** |
| 🔴 **収量** | 🔴 **rendement `40 hl/ha` / rendement butoir `46 hl/ha` / `50 hl/ha` を超えると収穫全量が AOC を失う** |
| 🔴 **収穫** | 🔴 **手摘み義務（`récoltés manuellement`）。房は「entières」＝丸ごと醸造所へ運ぶ義務** |
| **マロラクティック** | **瓶詰時点でリンゴ酸 0.4 g/L 以下** |
| **残糖** | **3 g/L 以下（自然アルコール 13.5% 以下）／4 g/L 以下（13.5% 超）** |
| 🔴 **禁止事項** | 🔴 **40°C 超の加熱処理禁止／木片（copeaux）の使用禁止／連続式圧搾機禁止** |
| **上限アルコール** | **補糖後の総アルコール 13.5% を超えない** |
| **容器** | **消費者向けはガラス瓶のみ（2016-08-01 から適用）** |
| 🔴 **熟成期間** | 🔴 **規定なし。** CDC は最低熟成期間も出荷解禁日も定めていない |
| **より大きい単位** | **`Cru des Côtes du Rhône` / `Vignobles de la Vallée du Rhône` を併記可。呼称名の 2/3 以下の寸法で** |

### 🏛 Cornas の自然条件（CDC 第 X 章より）

🏛 **ローヌ右岸、Valence 市の対岸。北を `massif des Arlettes` に守られ、南に大きく開いた
「amphithéâtre（円形劇場）」状の地形。「Lyonnais 型」の温暖な気候が、南向きと北風からの
自然の遮蔽によって強く性格づけられる。**
🔴 🏛 **土壌の大部分は一次火成岩の風化物 —— `granites porphyroïdes de Tournon`（花崗岩）。**
🏛 **村の北部、`massif des Arlettes` だけが二次代の堆積岩（緻密な石灰岩）で、
その南斜面に崩積土（éboulis calcaires）を落としている。これは `Pied-la-Vigne` 地区に見られ、
🔴 「zone géographique のごく一部（infime partie）」にすぎない。**
🏛 **急斜面では花崗岩の砂（arènes granitiques）を留めるため、
伝統的な空石積みの擁壁（murets de pierres sèches）で小さなテラスを組む。**
🏛 **Hermitage は北へ 12 km。Cornas の収穫はしばしば 1 週間早く始まる。**
🏛 **`Cornas` はケルト語で「terre brûlée（焼けた土地）」を意味する、と CDC は記す。**

⚠️ **これらは AOC 全域の記述であり、Allemand の畑の説明ではない。**

---

## Farming

🔴 ⚠️ **本節は「認証は無い」という否定的事実だけが確定している。**
**実際に何をしているかを示す一次資料は一件も無い。**

### 🔴 🏛 認証の有無 —— **3 経路すべてで確認した**

| 経路 | 照会方法 | 結果 🏛 |
|---|---|---|
| 🔴 **Agence Bio（国家有機登録簿）** | **SIRET 完全一致で 3 回**: `43243463700018`（THIERRY ALLEMAND）／`90988322500015`（THEO ALLEMAND）／`49935723400016`（TA COMMERCIALISATION） | 🔴 **3 件とも `nbTotal: 0`。** **有機認証事業者として登録されていない** |
| **INSEE / Sirene** | 企業登記レコードの bio フラグ | 🏛 **`est_bio: false` / `liste_id_bio: null`** |
| 🔴 **Biodyvin** | **会員名簿ページ全文取得**（`liste-des-membres-biodyvin.html`、**2025 年 224 名**、`Vallée du Rhône` 節を含む完全に解決するページ） | 🔴 **`ALLEMAND` は 0 件。`CORNAS` の語も 0 件。会員ではない** |
| 🔴 **Demeter France** | **cahier des charges 2024 年 1 月版 PDF（実物取得）** | 🔴 **「La certification biologique est une condition préalable pour être en conformité avec le présent cahier des charges relatif aux produits alimentaires et matières premières d'origine agricole」（p.16）。** **有機認証が前提条件である以上、上記の Agence Bio 陰性により Demeter は成立しえない** |

⚠️ **Demeter France の会員検索ページ（`demeter.fr/?s=…`）は JS シェルで、
存在する会員名で検索しても同一の HTML を返した。したがって同ページ単独では proved negative に
ならない。** **本書の Demeter 判断は「会員検索が空だった」ではなく
「規格自身が前提条件を課しており、その前提が満たされていない」という構造的論拠に依っている。**

### 🔴 ⚠️ **時間的な罠 —— 認証の話は OBP の 4 本には届かない**

🔴 **OBP のヴィンテージは 1998 / 1999 / 2001 / 2006 である。**
🔴 **Agence Bio の登録簿はそもそもこの時期まで遡らない。**
**仮に将来この事業者が有機認証を取得したとしても、それは 1998〜2006 年のボトルについて
何も語らない。逆も同様である。**
🔴 **Batch 10 の Famille Moussé がこの先例である —— 3 本の OBP ヴィンテージがすべて転換開始前で、
したがってそのボトルを「オーガニック」と呼んではならないと結論した。**
**本件はさらに強い形である: そもそも認証が一度も存在しない。**
→ §Staff Notes ⚠️ ④

### ❓ 公的資料が沈黙している栽培項目

❓ **自社畑の総面積・区画ごとの面積・樹齢・植密度・仕立ての実態・馬耕の有無・
収量の実績値・除草の方法・被覆作物。**
**これらを示す一次資料は存在しない。本ドシエでは一切主張しない。**

⚠️ 🔴 **canonical の `terroir` フィールドは「「シャイヨ」は樹齢20〜40年の区画」と書き、
`description` は「シャイヨ（若い木）」「ルナール（古い木）」と書く。**
🔴 **樹齢の数値も、二区画の樹齢の上下関係も、本調査ではいかなる一次資料からも確認できなかった。**
→ §Canonical Conflict、§Staff Notes ⚠️ ⑤

⚠️ **CDC には「échalas は最低 1.50 m」「植密度は最低 4,400 本/ha」等の栽培規定があるが、
これは AOC Cornas を名乗る全生産者に課される最低基準であって、
Thierry Allemand が何をしているかの説明ではない。**

---

## Winemaking

🔴 ⚠️ **本ドシエは、この生産者の醸造について一件も確定できなかった。**

**理由は明快である —— 公式サイトが存在せず（ドメインが一度も登記されていない）、
生産者が公表した醸造記述が一件も無いからである。**

### 🔴🔴 **無亜硫酸（sans soufre）について —— 本書は記述を拒否する**

🔴 **これはこの生産者について最も広く流布し、最も頻繁に誤って語られる属性である。**
🔴 **本調査は、亜硫酸の使用・不使用について、生産者自身に由来する記述を一件も入手できなかった。**

**確認できたのは以下だけである:**
- 🏛 **INAO の cahier des charges は SO₂ について何も定めていない**
  （定めているのはリンゴ酸・残糖・アルコール・加熱温度・木片・連続式圧搾機である）。
- ⚠️ **第三者（輸入元・小売店・評論）の記述は本調査規約により事実の根拠として使用できない。**
  **本調査で目にした第三者記述は互いに一致していない**
  （「ごく少量の SO₂」「特定ヴィンテージのみ無亜硫酸のキュヴェ」「無亜硫酸の Reynard」等）。
  🔴 **一致していないという事実自体が、断定を禁じる根拠である。**

🔴 **したがって本書は次の 3 つをいずれも主張しない:**
1. 🔴 **「無亜硫酸である」と言わない。**
2. 🔴 **「亜硫酸を使っている」とも言わない。**
3. 🔴 **「昔は使っていなかったが今は使う」等の**変遷**を語らない。**

🔴 **とりわけ OBP の 4 本（1998 / 1999 / 2001 / 2006）について、
当該年の亜硫酸の扱いを示す生産者資料は一件も存在しない。**
🔴 **本書はこの 4 本の醸造を性格づけることを明示的に拒否する。**
→ §Staff Notes ⚠️ ⑥、Open Questions 2

### ❓ その他、公的資料が沈黙している醸造項目

❓ **除梗の有無と比率・全房発酵の有無・マセラシオンの日数と温度・酵母・
樽の種類とサイズと新樽比率・熟成期間・ラッキングの有無と回数・
清澄と濾過・瓶詰時期。**

🔴 **これらについて、一般的な北ローヌの慣行や他の Cornas 生産者の手法を援用して
埋めることはしていない。**
🔴 ⚠️ **canonical の `allemand-chaillot-nv` はこれらを具体的に記述している
（「全房発酵（部分的）」「古樽で18ヶ月以上熟成」「無清澄・無濾過」）が、
本調査ではその出典を一件も確認できなかった。** → §Canonical Conflict

🏛 **appellation レベルで確実に言えるのは、CDC が全生産者に課す以下だけである ——
手摘み義務・房を丸ごと運ぶ義務・連続式圧搾機の禁止・40°C 超の加熱処理の禁止・
木片の使用禁止・補糖後 13.5% 上限・瓶詰時リンゴ酸 0.4 g/L 以下・ガラス瓶のみ。**
🔴 **熟成期間の規定は存在しない。したがって canonical の `aging: "18+ months old barrel"` は
appellation 側からも支持されない。**

---

## Style

🔴 ⚠️ **本ドシエは、この生産者のテイスティングノートを持たない。**

**生産者による公式のテイスティングノートが存在しない（サイトが存在しない）。**
**輸入元・小売店・評論家によるノートは本調査規約により事実の根拠として使用できない。**

❓ **香り・味わい・骨格・熟成能力・飲み頃について、本ドシエは何も主張しない。**
🔴 **とりわけ 1998 / 1999 / 2001 / 2006 という 20〜28 年を経たボトルの現在の状態は、
いかなる資料からも導けない。**

### 🏛 appellation レベルで言えること —— **AOC Cornas 全体の性格**

⚠️ **以下は CDC 第 X 章 2° が「AOC Cornas のワイン」全体について記す公的記述であり、
Thierry Allemand のワインの説明ではない。この区別を崩さないこと。**

🏛 **「Les vins présentent toujours une robe très foncée, grenat, voire presque noire,
caractéristique, évoluant vers des tonalités ambrées avec le vieillissement.
Ils sont puissants et charpentés et atteignent leur apogée après une longue garde.」**
—— **常に非常に濃い、ガーネットからほとんど黒に近い色調を持ち、熟成とともに琥珀色の
トーンへ向かう。力強く骨格があり、長い熟成の後に頂点に達する。**
🏛 **CDC はこれを受けて、Cornas がしばしば **「virils」**（男性的）と形容されると記す。**

🏛 **CDC が引く 1819 年 P. MAIGNE『Le nouveau manuel complet du sommelier et du marchand de vin』
の記述: 「ils sont riches en couleur, ont beaucoup de corps, de moelle, de velouté, de solidité」。**

🔴 ⚠️ **これは AOC の公的記述であって、この 4 本のグラスの中身の描写ではない。**
**「Cornas という呼称はこういうワインです」とは言えるが、
「このアルマンはこういう味です」とは本書からは言えない。** → §Staff Notes ⚠️ ⑦

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 4 本。全行 `producer_state = alias`**）

**セクションはすべて `FRANCE | RED > RHÔNE`。合計 $8,600 —— 本バッチ最高価格帯。**

| # | OBP 印字（生産者） | OBP 印字（ワイン） | VT | 価格 | canonical 照合 🔍 | 🏛 **確定したこと** |
|---|---|---|---|---|---|---|
| 1 | 🔴 **`Theirry Allemand`**（誤植） | **`'Chaillot,' Cornas`** | **2001** | **$2,000** | `allemand-chaillot-2001` / `cuvee_state: exact` / `vintage_state: exact` | 🏛 **`CHAILLOT` は Cornas の地籍リュー・ディとして実在（後述 ★）** |
| 2 | 🔴 **`Theirry Allemand`**（誤植） | **`'Chaillot,' Cornas`** | **1999** | **$2,400** | `allemand-chaillot-1999` / 同上 | 同上 |
| 3 | 🔴 **`Theirry Allemand`**（誤植） | **`'Reynard,' Cornas`** | **2006** | **$1,600** | `allemand-reynard-2006` / 同上 | 🏛 **`REYNARD` も地籍リュー・ディとして実在（後述 ★）** |
| 4 | 🔴 **`Theirry Allemand`**（誤植） | **`'Reynard,' Cornas`** | **1998** | **$2,600** | `allemand-reynard-1998` / 同上 | 同上 |

🔍 **4 行とも `match_state: alias`、`confidence: 0.95`、`source_quality_flags: ["producer_spelling"]`、
`_collision_risk: LOW`。**
🔍 **intake の evidence 第 1 行は 4 行とも同一 ——
「『Theirry』は i/r 転置。行の 'Chaillot' / 'Reynard' は Allemand の 2 大 Cornas キュヴェ。」**

---

### 🔴 ★ `Chaillot` と `Reynard` —— **両方とも地籍リュー・ディである。二重に確定した。**

**① 🏛 DGFiP / Etalab 地籍による肯定的証明**

**フランス国家地籍オープンデータ（コミューン `07070` Cornas）のリュー・ディ層を全件取得した。
Cornas には固有のリュー・ディが 39 件（ポリゴン 46）あり、その中に
`CHAILLOT` と `REYNARD` の両方が実在する。**

| リュー・ディ 🏛 | ポリゴン数 | **地籍上の広がり**（🔍 THÉSEUS 側の機械計算） | 中心座標（🔍 算術重心） |
|---|---|---|---|
| 🔴 **`CHAILLOT`** | **1** | **約 17.8 ha** | **44.96945 N / 4.84540 E** |
| 🔴 **`REYNARD`** | **2** | **約 23.7 ha（合計）** | **44.96687 N / 4.83706 E ＋ 44.96590 N / 4.84105 E** |
| **`PIED LA VIGNE`**（参考・CDC 本文が名指しする石灰崩積土の地区） | 2 | 約 33.2 ha | 44.97271 / 4.84775 ほか |
| **`LES ARLETTES`**（参考・CDC 本文が名指しする北の石灰岩塊） | 1 | 約 74.8 ha | 44.97557 / 4.84382 |

🔴 ⚠️ **上の「ha」は地籍リュー・ディの外形面積であり、ブドウ畑の面積ではなく、
まして Thierry Allemand の所有面積ではない。**
**リュー・ディには道・宅地・林地も含まれる。この数字を「畑の広さ」として語ってはならない。**
→ §Staff Notes ⚠️ ⑧

🔴 🔍 **位置関係（座標から機械的に導けること）:**
**`REYNARD` は経度 4.83434〜4.84349・緯度 44.96301〜44.96848。
`CHAILLOT` は経度 4.83946〜4.84944・緯度 44.96826〜44.97202。**
🔴 **すなわち `Reynard` が南・やや西、`Chaillot` が北・やや東で、両者は緯度 44.9683 付近で境を接する。**
**ドメーヌの登記住所（44.96222 / 4.84879）はその南東、村側にある。**
⚠️ **これは地籍ポリゴンの座標から機械的に読める相対位置であって、
標高・傾斜・日照・土壌についての主張ではない。地籍データはそれらを持たない。**

**② 🏛 CDC による法的経路の確認**

🔴 🏛 **cahier des charges 第 XII 章 2°a):**
**「L'étiquetage des vins bénéficiant de l'appellation d'origine contrôlée peut préciser
le nom d'une unité géographique plus petite, sous réserve : - qu'il s'agisse d'un lieu-dit cadastré ;
- que celui-ci figure sur la déclaration de récolte.」**
🔴 **＝ より小さい地理的単位の名称をラベルに記載してよい。ただし ①地籍上のリュー・ディであること
②収穫申告に記載されていること。**
🔴 **`Chaillot` も `Reynard` も条件①を満たす（上記①で実証）。**
**したがってこれらはラベル上で合法に名乗れる地籍名である。**

**③ 🏛 ただし CDC 本文には一度も現れない**

🔴 **`Chaillot` / `Reynard` の語は cahier des charges 全 13 ページのどこにも 0 回である。**
🔴 🏛 **かつ第 I 章 II は「Dénominations géographiques et mentions complémentaires :
Pas de disposition particulière」——補完的地理表示の規定を持たない。**
🔴 **つまり Cornas には premier cru も climat 格付けも一切存在しない。**

⚠️ **これは Batch 8 の Niellon `Truffière` と同じ「呼称の法的粒度より下の名前」の形である。**
🔴 **ただし決定的に異なる点がある —— Truffière と違い、Cornas の CDC は
「地籍リュー・ディなら記載してよい」という一般条項を明示的に持っている。**
🔴 **したがって「これは 1er Cru ではない」と言いつつ、
「地籍に実在し、AOC が名乗ることを明示的に認めた区画名である」と言える。**
**これは floor で使える、appellation レベルの確実な説明である。**

**④ 🔴 二区画の違いについて —— 言えることと言えないこと**

✅ **言えない:** ❓ **どちらが古木でどちらが若木か。樹齢。傾斜。標高。土壌の差。**
**Allemand 自身の資料が無いため、これらの区別を示す一次資料は一件も無い。**
🔴 **「Chaillot は若木、Reynard は古木」という区別は canonical の `description` にあるが、
出典を確認できなかった。第三者資料にも同旨の記述は流通しているが、
本調査規約により事実の根拠として採用できない。** → §Staff Notes ⚠️ ⑤

🔴 **言える:** 🏛 **両方とも Cornas 村の地籍リュー・ディであり、
Reynard が南西・Chaillot が北東で隣接すること。**
🏛 **AOC Cornas の土壌の大部分は花崗岩（granites porphyroïdes de Tournon）で、
石灰崩積土は北端の `Pied-la-Vigne` 地区に限られ「ごく一部」であること。**
🔍 🏛 **`CHAILLOT` も `REYNARD` も `PIED LA VIGNE` とは別のリュー・ディであり、
地籍上、両者は `PIED LA VIGNE` の西〜南西側にある。**
⚠️ **ただし「だから両区画は花崗岩である」と断定はしない。
CDC は土壌の分布を地籍リュー・ディ単位では示していない。** → Open Questions 5

---

### 🔴 ★★ ヴィンテージの裏づけ —— **沈黙であって、誤りではない**

🔍 **intake は 4 行とも `vintage_state: exact` とし、
「canonical に vintage 2001 実在（保有: 1999, 2001, NV）」等を evidence とする。**
🔴 **これは canonical の自己参照であって、外部からの裏づけではない。**

🏛 **1998 / 1999 / 2001 / 2006 の各年に `Chaillot` / `Reynard` が実際に生産されたことを
示す公的または生産者一次資料は、本調査では一件も入手できなかった。**
- **生産者の公式資料が存在しない。**
- **INAO の cahier des charges は appellation の規定であって生産実績を持たない。**
- **収穫申告（déclaration de récolte）は公開されない。**

🔴 **Batch 9 の Abreu 先例を適用する —— 古いヴィンテージについて公的な裏づけが無いことは
「沈黙」であって「誤り」ではない。**
🔴 **したがって本書はこの 4 ヴィンテージを「確認できた」とも「存在しない」とも記録しない。
`silence` として記録する。**
→ §Canonical Conflict の gap 表、Open Questions 3、**物理ラベル照合タスク**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 「コルナス」という呼称そのものが、この 4 本の一番確かな話である。**
「**コルナスは、ローヌ川の右岸、ヴァランスの街の対岸にある、たった一つの村だけの呼称**です。
**1938 年 8 月 5 日の政令で認められました。**
**北ローヌの呼称の中で、シラー 1 品種だけで造られる唯一の呼称**で、
**赤のスティルワインしか認められていません。**
**ブドウは手摘みが義務**で、**房は丸ごと醸造所へ運ぶことが定められています。**
**大部分は花崗岩の斜面**で、**急斜面には空石積みの擁壁で組んだ小さなテラス**が並びます。
**エルミタージュは北へ 12 キロですが、コルナスのほうが 1 週間ほど収穫が早い**——
呼称明細書にそう書かれています。
ちなみに **『コルナス』はケルト語で『焼けた土地』**という意味だそうです。」

**② 『シャイヨ』も『ルナール』も、地籍に実在する区画名です。プルミエ・クリュではありません。**
「**コルナスにはプルミエ・クリュも climat の格付けも存在しません。**
**呼称明細書の『補完的な地理的表示』の欄は『規定なし』**とだけ書かれています。
では『シャイヨ』『ルナール』は何かというと、
**フランス国の地籍に実在する、コルナス村のリュー・ディ（小地名）**です。
**コルナス村には 39 のリュー・ディがあり、その両方が入っています。**
**呼称明細書は『地籍上のリュー・ディであり、収穫申告に記載されていれば、
ラベルに記載してよい』と明示的に認めています。**
**位置関係も地籍で分かります —— ルナールが南西、シャイヨが北東で、両者は隣り合っています。**」

**③ 造り手自身は何も公表していません。だから『造り手によれば』は使えません。**
「**この造り手は公式サイトを持っていません。**
**それどころか、それらしいドメイン名が一度も登録された記録がなく、
インターネット・アーカイブにも過去のページが一件も残っていません。**
ですので **『造り手はこう言っています』という形でお伝えできることは、私どもには一つもありません。**
**フランス国の企業登記で確認できるのは、コルナス村の `22 impasse des Granges` に本拠を置く
2000 年設立の会社で、代表は 1963 年 3 月生まれの Thierry Allemand 氏である、ということまで**です。」

### 追加で使える一手

- **メニューの綴りについて（聞かれた場合のみ・こちらから訂正に行かない）**:
  「**メニューの綴りは `Theirry` になっていますが、正しくは `Thierry` です。**
  **フランス国の企業登記でも法人名は `THIERRY ALLEMAND` です。**」
- **お値段について（$1,600〜$2,600）**:
  「**1998年から2006年、20年から28年を経たボトル**です。
  **呼称明細書は『力強く骨格があり、長い熟成の後に頂点に達する』と、
  コルナスというワイン全体についてそう記しています。**
  **色は非常に濃いガーネット、ほとんど黒に近く、熟成とともに琥珀のトーンへ向かう**、とも。
  ⚠️ **ただしこれは呼称全体の公的な記述で、この 1 本の今の状態のお話ではありません。**」
- **収量について**:
  「**基準収量は 40 hl/ha、上限が 46 hl/ha。50 hl/ha を超えると、
  その年の収穫は全量が呼称を失います。**」
- **仕立てについて**:
  「**呼称明細書は『échalas（棒仕立て）』か『引き上げ式の垣根』のどちらかと定めています。
  棒仕立ての場合、棒の高さは最低 1.5 メートル**です。」
- **『黒に近い色』の由来**:
  「**1819 年の『ソムリエと葡萄酒商のための新完全便覧』が既に
  『色が豊かで、ボディがあり、まろやかで、ビロードのようで、堅固だ』と書いている**——
  これは呼称明細書自身が引用している一節です。」

### ⚠️ 言ってはいけないこと（**根拠が無い／出典が沈黙している／第三者情報しかない**）

🔴 **本ドシエは生産者由来の情報が「ゼロ」である。したがってこの一覧が本書で最も重要な成果物である。**
🔴 **この生産者は評論家と商業サイトに極めて多く書かれており、
流通している「常識」のほとんどに一次資料が無い。だからこの一覧は長い。**

1. 🔴 ⚠️ **創業年を言わない。**
   **法人 `THIERRY ALLEMAND` の登記設立日 2000-07-01 は法人の設立日であって創業年ではない。**
   🔴 **OBP の 1998 年・1999 年のボトルは、この法人の登記より前である。**
   **「1980 年代に始めた」「最初の区画は 19XX 年」等の年号は、本調査では一件も確認できていない。**
2. 🔴 ⚠️ **世代交代・引退・承継の物語を語らない。**
   🏛 **本書が持つのは「同一住所・同一業種で `THEO ALLEMAND` が 2022-01-26 に
   個人事業主として登記された」という登記事実だけである。**
   **これは役割分担も承継も意味しない。Batch 8 は Roulot の 2 法人を同じ理由で物語として読むことを
   拒否した。同じ扱いをする。**
3. 🔴 ⚠️ **『ノエル・ヴェルセの畑を引き継いだ』と言わない。**
   **canonical の記述にはあるが、出典を確認できなかった。**
   🏛 **登記上、`NOEL VERSET` は 2008-10-31 に廃止されており、
   OBP の 4 ヴィンテージ（1998/1999/2001/2006）はすべてそれより前である。**
   🏛 **かつ Cornas には `ALAIN VERSET`・`EARL DOMAINE VERSET A ET E`・`GFV VERSET MOUTON` が
   今も活動中で存在する。** **どう読んでもこの 4 本の説明には使えない。**
4. 🔴 ⚠️ **『ビオディナミ』『オーガニック』『ビオ』と言わない。**
   🔴 🏛 **Agence Bio に SIRET 完全一致で 3 事業者を照会し、3 件とも `nbTotal: 0`。有機認証は無い。**
   🔴 🏛 **Biodyvin の 2025 年会員名簿（224 名・全文取得）に `ALLEMAND` は無い。**
   🔴 🏛 **Demeter France の規格は有機認証を前提条件と明記しており、前提が満たされていない。**
   🔴 ⚠️ **さらに決定的に —— OBP のヴィンテージは 1998〜2006 年である。
   Agence Bio の登録簿はそこまで遡らない。仮に現在何らかの認証があったとしても、
   このボトルについては何も語らない**（Batch 10 の Famille Moussé と同じ理由）。
   🔴 **canonical の `Biodynamic` タグと「バイオダイナミック農法」記述は、本書では採用しない。**
5. 🔴 ⚠️ **『シャイヨは若木、ルナールは古木』と言わない。樹齢の数字を出さない。**
   **canonical は「樹齢20〜40年」と具体的に書くが、出典を確認できなかった。**
   **どちらの区画がより古いかを示す一次資料は一件も無い。**
6. 🔴🔴 ⚠️ **亜硫酸について何も言わない。「無亜硫酸」も「少量」も「昔は」も、すべて言わない。**
   🔴 **この生産者について最も広く流布し、最も誤って語られる属性である。**
   **生産者自身の記述は一件も入手できていない。**
   **本調査で目にした第三者記述は互いに一致していなかった。**
   🔴 **とりわけ 1998 / 1999 / 2001 / 2006 の各年に何をしていたかは、完全な空白である。**
   **聞かれたら「造り手が公表していないので、私どもからは申し上げられません」と答えるのが正しい。**
7. 🔴 ⚠️ **味のノートを『造り手によれば』と言わない。**
   **公式のテイスティングノートは存在しない。**
   **呼称明細書の「濃いガーネット／力強く骨格がある／長期熟成」は AOC コルナス全体の公的記述であって、
   この 1 本の描写ではない。この 2 つを混ぜない。**
   **自分で試飲した感想を述べるのは構わないが、それを『造り手によれば』と言ってはならない。**
8. 🔴 ⚠️ **『シャイヨは約 18 ヘクタール』等と言わない。**
   **本書の面積は地籍リュー・ディの外形面積であり、ブドウ畑の面積でも所有面積でもない。**
   **道・宅地・林地を含む。**
   🔴 **Allemand の所有面積を示す一次資料は一件も無い。数字を出してはならない。**
9. ⚠️ **『プルミエ・クリュ』と言わない。**
   🏛 **コルナスにはプルミエ・クリュも climat 格付けも存在しない。
   呼称明細書の補完的地理表示の欄は「規定なし」である。**
   **メニューが `'Chaillot,' Cornas` とだけ書いているのは正しい表記である。**
10. 🔴 ⚠️ **醸造を一切語らない。**
    **除梗・全房・マセラシオン日数・酵母・樽の種類と新樽比率・熟成期間・
    ラッキング・清澄・濾過 —— 本ドシエは根拠を一つも持たない。**
    🏛 **呼称明細書には熟成期間の規定すら存在しない。**
    **『北ローヌでは普通こうです』で埋めてはならない。**
11. ⚠️ **第三者点数・評論家評を言わない。**
    🔍 **canonical は `points: 95` を持つが、これは NV レコードにのみ付いており、
    出典が記録されていない。**
12. 🔴 ⚠️ **輸入元・小売店の資料に書かれている内容を、造り手の説明として語らない。**
    🔴 **本調査は米国の輸入元・小売のページを取得したが、いずれも三人称の自社販促文で、
    生産者の署名も「notes from the domaine」の表記も無いため、authorship を理由に棄却した。**
    ⚠️ **同種の資料には畑の面積・樹齢・師事関係・醸造・亜硫酸の記述があるが、
    本ドシエはそれを一切採用していない。**
    ⚠️ 🔴 **付言すると、取得した輸入元ページは生産者名を `Thiérry Allemand` と表記していた
    （`e` にアクセント）。メニューは `Theirry`。canonical と登記は `Thierry`。
    この生産者の名は、三者三様に間違えられている。**
13. ⚠️ **『Cornas AOC には熟成義務がある』等と言わない。**
    🏛 **cahier des charges は最低熟成期間も出荷解禁日も定めていない。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **本生産者について escalate すべき事項は 6 件ある。**
🔴 **いずれも DO NOT EXECUTE。canonical は読み取りのみで、一切変更していない。**
🔴 **既存ファミリーに当たるものは既存番号を引用し、新番号は一つも開いていない。**

🔍 **走査結果の前提: canonical 928 件中、文字列 `allemand` にヒットするのは 5 件。
🔴 5 件すべてが `producer` フィールドでのヒットであり、prose-only ヒットは 0 件である
（`D-2026-08-05-08` の部分一致誤爆は canonical 側では発生していない）。**

---

### 🔴🔴 `V-*` 系／`D-2026-08-05-12` への反例 —— `allemand-chaillot-nv` の `vintage: "NV"`

1. **衝突する canonical ID**
   - 🔴 **`allemand-chaillot-nv` … `vintage = "NV"`**
2. **なぜ問題か**
   🔴 🏛 **AOC Cornas は「vins tranquilles rouges」に限られ（CDC 第 I 章 III）、
   補完的表示の規定を持たず（同 II）、収穫年をまたぐブレンドを許す条項を一切持たない。
   申告制度は `déclaration de récolte` を軸に構築されている。**
   🔴 **すなわち non-vintage の Cornas は成立しない。この値は不可能な値である。**
3. 🔴 **既知の読みへの反例であること（これが本項の要点）**
   🔴 **`D-2026-08-05-12` は canonical 全体で `'NV'` を **88 件**と実測し、
   「non-vintage Champagne については legitimate である」と読んだ。**
   🔴 **本件はその読みへの反例である。88 件のうち少なくとも 1 件は、
   NV がありえない静止赤ワイン AOC に付いている。**
   🔴 **「`'NV'` は正当」という判断は、appellation 単位で再検証しなければならない。
   `S-2` に対する『restate が要る』のと同じ扱いが `D-2026-08-05-12` にも要る。**
   **本書は再走査を行っていない（指示範囲外）。** → Open Questions 1
4. 🔴 **phantom か distinct か —— distinct であり、テンプレート由来と読める**
   🔍 **`allemand-chaillot-nv` は 4 兄弟と **3 点同時に**異なる:**
   - **`name` に呼称が埋め込まれている: `"Chaillot" Cornas` vs 4 件は `"Chaillot"` / `"Reynard"`**
   - **`subregion`: `Cornas — Northern Rhône` vs 4 件は `Cornas`**
   - **`classification`: `Cornas AOC` vs 4 件は `Cornas`**
   🔴 **さらに決定的な 2 点:**
   - 🔴 **`dosage: "N/A — Still Wine"` というキーを持つ。`dosage` は Champagne のフィールドである。**
   - 🔴 **`tags` に `Vintage` を含まない**（4 兄弟の `tags` は `["Vintage"]` のみ）。
   🔴 **`vintage: "NV"` と `dosage` キーが同一レコードに同居している。
   これは「Champagne 用テンプレートから生成されたレコード」と読むのが最も整合的である。**
   🔴 **したがって単純な重複（phantom）ではなく、別スキーマ由来の distinct なレコードである。
   ただし内容は `allemand-chaillot-2001` / `-1999` と同じキュヴェを指しており、
   `Chaillot` について canonical が 3 レコードを持つ状態になっている。**
5. 🔴 **`name` への呼称埋め込みは `C-4` の逆形である**
   🔴 **Batch 10 は Montelena で「`name` が `Napa Valley Chardonnay` のように
   呼称＋品種を含む」形を `C-4` として扱った。**
   🔴 **本件 `"Chaillot" Cornas` は同じ層のずれの**逆向き**である ——
   キュヴェ名フィールドに呼称が後置されている。**
   **`C-4` の一括方針を決める際、この向きも射程に入れる必要がある。新番号は開かない。**
6. **OBP への影響**
   🔍 **直接の影響は無い。OBP の 4 行はいずれも `allemand-chaillot-nv` に解決していない。**
   🔴 **ただし intake の evidence は「canonical に vintage 2001 実在（**保有: 1999, 2001, NV**）」と、
   `NV` を保有ヴィンテージの一つとして列挙している。
   マッチャは `NV` を年と同格に扱っている。** → 潜在的な誤解決の温床
7. **推奨する解決（DO NOT EXECUTE）**
   🔴 **`allemand-chaillot-nv` を Chaillot の 2001/1999 に統合するのか、
   別の実在ボトリングを指すレコードとして残すのかは、**中身の出所が不明なため本書では決められない**。**
   🔴 **先に `D-2026-08-05-12` の `'NV'` 88 件を appellation 別に再分類することを推奨する。**
8. **Confidence: High**（CDC と値の両方を直接確認済み）

---

### 🔴 `S-2`（既存ファミリー・175 件 / 18.9%） —— canonical キュヴェ名に二重引用符

1. **衝突する canonical ID**
   - **`allemand-chaillot-nv` … `name = "\"Chaillot\" Cornas"`**
   - **`allemand-chaillot-2001` / `allemand-chaillot-1999` … `name = "\"Chaillot\""`**
   - **`allemand-reynard-2006` / `allemand-reynard-1998` … `name = "\"Reynard\""`**
   🔴 **5 件すべて。100%。**
2. **なぜ問題か**
   **キュヴェ名の値に引用符そのものが含まれている。
   文字列一致による OBP 照合、表示、ソート、URL slug 生成のすべてに影響する。**
   🔴 **`D-2026-08-05-12` で 175 件 / canonical の 18.9% と実測済みの既知ファミリーと同一の形である。
   新番号は開かない。証拠を足すだけである。**
3. 🔴 **Alvina Pernot の指摘が本件でも成立する —— かつ、より強い形で**
   🔴 **Alvina Pernot は「マッチャの evidence 文字列自身が `'Reynard' ≡ '"Reynard"'` の形で
   高信頼一致を宣言しており、破損がマッチングからは不可視である」ことを指摘した。**
   🔴 **本件の evidence はまさにその文字列である ——
   行 3・4 の evidence 第 2 行は `名称トークン集合一致: 'Reynard' ≡ '"Reynard"'`、`confidence: 0.95`。**
   🔴 **さらに本件は同じ生産者の 4 行の中に**2 つの異なる挙動**が同居している:**
   - **行 3・4（Reynard）: evidence は `'Reynard' ≡ '"Reynard"'`、
     `proposed_canonical_cuvee` も **`"Reynard"`（引用符つき）**。**
   - **行 1・2（Chaillot）: evidence は `'Chaillot' ≡ 'Chaillot'`（引用符が消えている）、
     `proposed_canonical_cuvee` も **`Chaillot`（引用符なし）**。**
   🔴 **canonical 側は 5 件とも引用符つきなのに、マッチャの出力は
   同一生産者・同一破損に対して 2 通りの表現を返している。**
   🔴 **すなわち `S-2` は「マッチングを壊す」だけでなく、
   `proposed_canonical_cuvee` を経由して**破損を下流へ伝播させている**。
   Chaillot 側は正規化され、Reynard 側は正規化されない。この非一貫性は
   `S-2` の一括修正の設計に直接効く。**
4. **正規化の注意**
   🔴 **剥がすべきは ASCII の二重引用符 `"` であって、フランス語のエリジオン（`d'`, `l'`）や
   OBP 印字の単一引用符 `'Chaillot,'` ではない。**
   **本件のキュヴェ名にはエリジオンが含まれないため衝突しないが、
   一括処理を Burgundy / Rhône 全体に流す際は必ず区別すること。**
5. **OBP への影響**
   🔍 **4 行すべてがこの 2 キュヴェ名に依存する（$8,600）。
   `cuvee_state` は 4 行とも `exact` なので実害は現時点で出ていないが、
   それはマッチャが正規化で吸収しているためであって、値が正しいからではない。**
6. **推奨する解決（DO NOT EXECUTE）** **`S-2` の一括処理に合流させる。単独で修正しない。**
7. **Confidence: High**

---

### 🔴 `C-*` 系（既知の「prose が複製される」形） —— **`description` が 5 件で byte 同一**

⚠️ **Batch 10 の Roederer で「同一の `house_style` が 16 レコードに複製され、うち 2 件が虚偽」
という形が出ている。本件は同型で、より小規模だが、より明確に誤っている。**

1. **衝突する canonical ID** — **5 件すべて。**
2. 🔴 **何が起きているか**
   🔍 **`description` と `description_en` が 5 レコードで完全に同一の文字列である。**
   🔴 **その本文は Chaillot について書かれている ——
   「「シャイヨ（若い木）」は若い樹齢（樹齢20〜40年）の区画から造るコルナス。
   「ルナール（古い木）」と並ぶドメーヌの中核キュヴェ」。**
   🔴 **この文が `allemand-reynard-2006` と `allemand-reynard-1998` にもそのまま入っている。**
   🔴 **すなわち Reynard のレコードの説明文が、Chaillot を主語として語っている。**
3. **なぜ問題か**
   🔴 **表示層がこの `description` を出すと、Reynard の 2 本（$1,600 / $2,600）に
   Chaillot の説明が表示される。**
   **これは「値が古い」のではなく「レコードの主語が違う」という誤りである。**
4. 🔴 **加えて、その本文の内容自体が本調査で支持できない**
   - **「バイオダイナミック農法で単独管理する」** → 🏛 **認証は 3 経路すべてで否定。実践を示す
     生産者資料も無い。**
   - **「ノエル・ヴェルセが所有していた畑を引き継ぎ」** → 🏛 **一次資料なし。かつ `NOEL VERSET` の
     廃止は 2008 年で、OBP の 4 ヴィンテージより後。**
   - **「樹齢20〜40年」** → ⚠️ **出典なし。**
   - **「非常に少量で入手困難」** → ⚠️ **出典なし（かつ商業的評価語である）。**
5. **推奨する解決（DO NOT EXECUTE）**
   🔴 **prose の複製検出は producer 単位の一括問題である。単独で書き換えない。**
   🔴 **少なくとも「Reynard レコードから Chaillot 主語の本文を外す」ことは、
   出典の議論と独立に成立する。だが実行は CTO 判断である。**
6. **Confidence: High**（値そのものを確認済み）

---

### 🔴 canonical の格納値が公的資料と矛盾する／出典が無い —— **フィールド単位の突合表**

🔴 **Batch 10 は「canonical の格納値が 10/10 の生産者で公式と矛盾する」を base rate として立てた。
本件は 11 例目であり、base rate を維持する。**
🔴 **ただし Alvina Pernot が「レコードが空の殻である」形を初めて出したので、
本書は **contradicted / unsourced / absent-as-key** を明示的に区別する。**
🔴 **本件はその 3 つが同一生産者の 5 レコードに**同居**している。**

| フィールド | 格納値 | 判定 | 根拠 |
|---|---|---|---|
| 🔴 **`grapes`**（chaillot-nv / -2001 / -1999） | `["Syrah 100%"]` | ✅ **正しい（本書で唯一、公的に裏づけられた typed field）** | 🏛 **CDC 第 V 章「Les vins sont issus du cépage syrah N」** |
| 🔴 **`grapes`**（reynard-2006 / -1998） | 🔴 **キー自体が存在しない** | **absent as key** | 🏛 **同じ AOC・同じ生産者なのに 2 件だけ欠落。値の誤りではなく欠落である** |
| 🔴 **`vintage`**（chaillot-nv） | 🔴 **`"NV"`** | 🔴 **contradicted** | 🏛 **CDC: Cornas は静止赤のみ。NV 条項なし** |
| 🔴 **`aging`**（chaillot-nv のみ） | `"18+ months old barrel"` | 🔴 **unsourced**（かつ appellation からも支持されない） | 🏛 **CDC は最低熟成期間を定めていない。生産者資料は存在しない** |
| **`aging`**（他 4 件） | **キーなし** | **absent as key** | — |
| **`founded_year`** | 🔴 **5 件すべてキーなし** | **absent as key** | 🏛 **むしろ正しい。登記設立日 2000-07-01 を創業年として入れられていない点は安全側** |
| **`subregion`** | `Cornas`（4 件）／🔴 `Cornas — Northern Rhône`（nv） | ⚠️ **不整合**（内容はいずれも正しい） | 🏛 **CDC は Cornas を Côtes du Rhône septentrionales の一つとする。両表記とも誤りではないが 5 件で揃っていない** |
| **`classification`** | `Cornas`（4 件）／🔴 `Cornas AOC`（nv） | ⚠️ **不整合** | 🏛 **INAO の正式表記は `appellation d'origine contrôlée « Cornas »`。`Cornas AOC` のほうが近いが、揃っていない** |
| 🔴 **`description` / `description_en`** | **5 件 byte 同一・Chaillot 主語** | 🔴 **contradicted（Reynard 2 件）＋ unsourced（内容）** | **上記 `C-*` 系の項参照** |
| 🔴 **`obp_note` / `obp_note_en`**（nv のみ） | 「バイオダイナミック農法のシラー100%」「樹齢20〜40年の若い木」「ブラックベリー、スモーク、鉄のミネラリティ」 | 🔴 **contradicted（ビオディナミ）＋ unsourced（樹齢・香味）** | 🏛 **Agence Bio `nbTotal:0` ×3／Biodyvin 名簿に不在／Demeter は前提条件不成立** |
| **`obp_note`**（他 4 件） | **キーなし** | **absent as key** | 🔴 **OBP に載っている 4 本のほうが `obp_note` を持たず、OBP に載っていない NV だけが持つ** |
| 🔴 **`winemaking`**（nv のみ） | 「全房発酵（部分的）。古樽で18ヶ月以上熟成。無清澄・無濾過。」 | 🔴 **unsourced** | **生産者資料が存在しない。CDC も定めていない** |
| 🔴 **`tasting`**（nv のみ） | 「ブラックベリー、ブラックチェリー、スモーク、鉄、ラベンダー、胡椒、タール…」 | 🔴 **unsourced** | **公式テイスティングノートは存在しない** |
| 🔴 **`points`**（nv のみ） | **`95`** | 🔴 **unsourced** | **出典が記録されていない。かつ実在しえないレコードに付いている** |
| **`terroir`**（chaillot 3 件） | 「花崗岩土壌の急斜面。バイオダイナミック農法。「シャイヨ」は樹齢20〜40年の区画。」 | ⚠️ **partly supported / partly contradicted** | 🏛 **花崗岩・急斜面は CDC が支持する。ビオディナミは否定。樹齢は unsourced** |
| **`drinking_window`**（nv のみ） | `2024–2040` | 🔴 **unsourced**（かつ OBP の 1998–2006 には適用できない） | — |
| **`dosage`**（nv のみ） | `N/A — Still Wine` | 🔴 **スキーマ由来の異物** | **`dosage` は Champagne のフィールド。上記 NV 項参照** |
| **`indicator`** | `#800020`（nv）／`#c9a84c`（4 件） | ⚠️ **不整合** | 🔍 **5 件とも `color: Rouge` だが、実 OBP に対応する 4 件のほうが金色系の値を持つ** |
| **`tags`** | 6 タグ（nv・`Biodynamic` 含む）／`["Vintage"]`（4 件） | 🔴 **contradicted（`Biodynamic`）** | 🏛 **認証 3 経路すべてで否定** |

**Confidence: High**（各値と各公的資料を直接突合済み）

---

### 🔴 メニュー側の欠陥 —— **`Theirry` 誤植（4 行）**

⚠️ **これは canonical conflict ではない。OBP メニュー側の欠陥である。分けて記録する。**

1. **対象** — 🔍 **OBP 4 行すべての `source_producer_raw` = `Theirry Allemand`。**
2. **根拠** — 🏛 **INSEE / Sirene の法人名 `THIERRY ALLEMAND`、代表者 `ALLEMAND THIERRY`。
   canonical も 5 件すべて `Thierry Allemand`。**
3. 🔴 **Batch 10 の常設警告との関係**
   🔴 **「メニューは defective な側とは限らない」は正しい警告であり、
   本バッチでも Alvina Pernot で 4 件目の反例が出ている。**
   🔴 **本行はその**逆のケース**である。メニューが単純に誤っている。**
   🔴 **警告は「メニューを疑うな」ではなく「パターンの存在を個別行の証拠にするな」である。
   個別に検証した結果、今回はメニュー側だった —— そう明言できることに、警告と同じ価値がある。**
4. **影響** — 🔍 **`producer_state` が 4 行とも `alias` に落ちている。
   `alias` 登録（`Theirry Allemand` → `Thierry Allemand`）で解決可能。**
   ⚠️ **ただし alias として固定すると誤植が正規の別名として定着する。
   「メニュー印字の誤り」として扱うほうが正しい可能性がある。** → Open Questions 6
5. **Confidence: High**

---

### 🔍 参考: 衝突ではないが記録しておくべきこと

| 事項 | 状態 | 備考 |
|---|---|---|
| **生産者そのもの** | 🔍 **gap ではない** | **canonical に `producer` = `Thierry Allemand` のレコードが 5 件実在する** |
| **OBP 4 本のキュヴェ・ヴィンテージ** | 🔍 **4 本とも canonical に対応レコードあり** | **`cuvee_state` / `vintage_state` とも 4 行すべて `exact`** |
| 🔴 **4 ヴィンテージの外部裏づけ** | 🔴 **silence** | 🏛 **1998/1999/2001/2006 の生産を示す公的・生産者一次資料は 0 件。Batch 9 Abreu 先例により「沈黙」であって「誤り」ではない** |
| **`allemand-chaillot-nv`** | 🔴 **OBP に対応行を持たない canonical レコード** | **在庫に無いものが canonical にある状態。上記 NV 項参照** |
| **`THEO ALLEMAND`（SIREN 909883225）** | 🔍 **canonical に不在** | 🏛 **同一住所・同一 NAF の別事業者。canonical にも OBP にも現れない。gap ではあるが、この事業者のワインが OBP に無いので起票対象ではない** |

---

## Sources

### 🔴 サイト真正性の事前確認（`D-2026-08-05-09`） —— **実施結果**

🔴 **本件は「look-alike を掴んだ」ケースではなく「候補ドメインが一つも存在しない」ケースである。**

| 候補 | 判定 | **どう検証したか** |
|---|---|---|
| 🔴 **`thierryallemand.com`** | 🔴 **未登録** | **Verisign RDAP (`rdap.verisign.com/com/v1/domain/…`) → `HTTP 404`。DNS A/MX とも空** |
| 🔴 **`thierry-allemand.com`** | 🔴 **未登録** | **同上 `HTTP 404`** |
| 🔴 **`domainethierryallemand.com`** | 🔴 **未登録** | **同上 `HTTP 404`** |
| 🔴 **`thierryallemand.fr`** | 🔴 **未登録** | **AFNIC RDAP (`rdap.nic.fr`) → `NOT_FOUND_DOMAIN_NAME_WITH_NAME`** |
| 🔴 **`thierry-allemand.fr`** | 🔴 **未登録** | **同上** |
| **`domaine-thierry-allemand.fr` / `allemand-cornas.fr` / `allemandcornas.com`** | **存在しない** | **DNS A/AAAA/MX すべて空** |
| ⚠️ **`allemand.fr`** | 🔴 **別人のサイト。使用せず。** | **DNS は解決する（A: `185.230.63.107` 他 ＝ Wix のホスティング IP 帯、MX: `lerelaisinternet.com`）が、`https://allemand.fr` は `HTTP 404` を `server: Pepyaka`（Wix）で返す。Cornas とも Allemand 家とも結びつかない。** **1 文字も使用していない** |
| 🔴 **Internet Archive** | 🔴 **過去の公式サイトも存在しない** | **`archive.org/wayback/available` に 4 ドメインを照会 → 4 件とも `HTTP 200` で `{"archived_snapshots": {}}`。** ⚠️ **本バッチで Wayback が `HTTP 429` を返した事例があるが、本件は 200 で完全に解決しており、ゲートではない** |
| 🔴 **Agence Bio の `siteWebs`** | 🔴 **フィールド以前にレコードが無い** | **SIRET 完全一致で `nbTotal: 0`** |

🔴 🏛 **結論: Thierry Allemand に公式ウェブサイトは存在しない。**
**しかも「ドメインを持っているが空」（Roulot / Alvina Pernot）でも「NXDOMAIN」（Niellon）でもなく、
🔴 「ドメインが一度も登記されたことがない ＋ Wayback にも一件も無い」という形である。**
🔴 **本バッチで確認された 4 つ目の不在の形である。**

🔴 **したがって本ドシエは、指示された fallback ルート
（企業登記 → Agence Bio / 認証機関 → INAO cahier des charges → 地籍）を全面的に採用した。**

---

### 一次資料（**実際に取得し `_sources/thierry-allemand/` に保存したもの**）

| 資料 | 種別 | 取得した情報 |
|---|---|---|
| 🔴 🏛 **INSEE / Sirene 企業登記** `recherche-entreprises.api.gouv.fr` → `annuaire_432434637.json` / `annuaire_909883225.json` / `annuaire_499357234.json` / `annuaire_allemand_07130.json` / `annuaire_q1.json` | **フランス国家企業登記** | 🔴 **`THIERRY ALLEMAND` SAS SIREN 432434637 / SIRET 43243463700018 / 2000-07-01 設立 / NAF 01.21Z / NJ 5710 / état A / 22 impasse des Granges 07130 Cornas / 座標 44.962225,4.848794 / Président `ALLEMAND THIERRY`(1963-03) / effectif `02`(2023) / IDCC 7024 / TVA FR24432434637 / `est_bio:false` / `liste_id_bio:null` / 2024 `résultat_net` 217,979・`ca` 0。`TA COMMERCIALISATION` SAS 499357234・2007-07-01・NAF 47.25Z。`THEO ALLEMAND` 個人事業主 909883225・2022-01-26・NAF 01.21Z・同住所。`PETITE CERISE` 504587890・2008-05-27。`LA LOUBIE` 813919446・2015-10-05。`GFA LE GRAND CADE` 901621185・2021-07-08。`NOEL VERSET` 323099473・1981-11-10 設立 / 2008-10-31 廃止(état C)。`ALAIN VERSET` 444780415。`EARL DOMAINE VERSET A ET E` 822442026。`GFV VERSET MOUTON` 914114574** |
| 🔴 🏛 **INAO cahier des charges「Cornas」** `extranet.inao.gouv.fr/fichier/PNO2023AOPCornas.pdf` → `cdc_cornas.pdf`（**13 頁・`%PDF-1.5` 検証済**）/ `cdc_cornas.txt` | **原産地呼称明細書** | 🔴 **1938-08-05 décret / 現行 homologation arrêté 2019-12-06 (JORF 2019-12-08) / 本 PDF は 2023-11-30 承認の PNO 版 / 静止赤のみ / 補完的表示「規定なし」/ Cornas 1 コミューンのみ / 区画境界 1971-05-12 承認 / syrah N のみ / 密度 4400・2.30 m²・畝間 2.50 m / 8 芽・コルドン 0.60 m / échalas 1.50 m / 7000 kg/ha / 欠株 20% / 糖 171 g/L / 自然アルコール 10.5% / 収量 40・butoir 46・失効 50 hl/ha / 手摘み義務 / 房丸ごと運搬義務 / リンゴ酸 0.4 g/L / 残糖 3・4 g/L / 40°C 超禁止・木片禁止・連続式圧搾機禁止 / 総アルコール 13.5% 上限 / ガラス瓶のみ(2016-08-01〜) / 熟成規定なし / 🔴 第 XII 章 2°a) 地籍リュー・ディ＋収穫申告記載でラベル記載可 / 花崗岩(granites porphyroïdes de Tournon)・Arlettes の石灰岩・Pied-la-Vigne の崩積土 / Hermitage の 12 km 南・収穫 1 週間早い / celte「terre brûlée」/ 1952 年に初の自家瓶詰 / 約 60 の caves particulières / 官能記述「robe très foncée…virils」/ 1819 P. MAIGNE 引用。🔴 `Chaillot` `Reynard` は全文 0 回** |
| 🔴 🏛 **DGFiP / Etalab 地籍オープンデータ** `cadastre.data.gouv.fr/.../07/07070/cadastre-07070-lieux_dits.json.gz` → `cadastre_07070_lieux_dits.json` | **フランス国家地籍** | 🔴 **Cornas の全リュー・ディ 39 名・46 ポリゴン。`CHAILLOT`（1 ポリゴン）と `REYNARD`（2 ポリゴン）の実在を確認。`PIED LA VIGNE` `LES ARLETTES` も実在（CDC 本文と一致）。** 🔍 **外形面積と重心は THÉSEUS 側の機械計算（等長方形近似）** |
| 🔴 🏛 **Agence Bio 公開 API** `opendata.agencebio.org/api/gouv/operateurs/?siret=…` → `agencebio_siret_43243463700018.json` / `…_90988322500015.json` / `…_49935723400016.json` / `agencebio_nom_allemand07.json` | **フランス国家有機登録簿** | 🔴 **SIRET 完全一致 3 件すべて `nbTotal: 0`（proved negative）。** 🔴 **`?nom=allemand` は 25 件を返すが `LALLEMAND` 系の部分一致誤爆を含み、Ardèche / Cornas の該当は 0 件** |
| 🔴 🏛 **Biodyvin 会員名簿** `biodyvin.com/fr/liste-des-membres-biodyvin.html` → `biodyvin_membres.html` | **ビオディナミ認証団体の会員名簿** | 🔴 **2025 年 224 名。`Vallée du Rhône` 節を含み完全に解決する。`ALLEMAND` 0 件・`CORNAS` 0 件（proved negative）** |
| 🔴 🏛 **Demeter France cahier des charges 2024 年 1 月版** `demeter.fr/wp-content/uploads/2024/03/Cahier-des-charges-Demeter-France-2024.pdf` → `demeter_cdc_2024.pdf` / `.txt` | **認証規格の一次文書** | 🔴 **p.16「La certification biologique est une condition préalable pour être en conformité avec le présent cahier des charges relatif aux produits alimentaires et matières premières d'origine agricole」** |
| 🏛 **Verisign RDAP / AFNIC RDAP / dig / Internet Archive availability API** → `dns_checks.txt` ほか | **ドメイン登記・DNS・アーカイブ** | 🔴 **`.com` 3 件 RDAP 404 / `.fr` 2 件 AFNIC NOT_FOUND / DNS 全滅 / Wayback 4 件とも `archived_snapshots: {}`** |

### 🔴 取得したが **事実の根拠として採用しなかった** もの

| 資料 | 理由 |
|---|---|
| 🔴 **`IMPORTER_rarewineco_allemand.html`** | 🔴 **米国の輸入元兼小売業者が自ら書いた生産者紹介ページである（サイト自身が "Wine Importer and Merchant since 1989" と名乗る）。全文が三人称の紹介文で、生産者の署名も「notes from the domaine」の表記も無い。** **`D-2026-08-05` の authorship 規約により、事実の根拠として一切使用していない。** ⚠️ **同ページには師事関係・畑の来歴・醸造哲学の記述があるが、本ドシエはそれを一切採用していない。** ⚠️ 🔴 **なお同ページは生産者名を `Thiérry Allemand` と表記している（`e` にアクセント）** |
| ⚠️ **`demeter_search_allemand.html`** | ⚠️ **Demeter France の会員検索。既知の会員名で検索しても同一 HTML を返す JS シェルであり、proved negative にならない。** **本書の Demeter 判断はこのページではなく、規格本文の前提条件に依拠している** |
| ⚠️ **検索結果に現れた小売・輸入元・評論・ワイン検索サイト・Vivino・CellarTracker・Wine-Searcher** | **本調査規約により全面禁止。内容を一切参照・引用していない。** 🔴 **この生産者は第三者記述が極めて多く、とりわけ亜硫酸と畑の来歴について互いに一致しない記述が流通している。それが `## Staff Notes` の禁止一覧が長い理由である** |

### 取得できなかったもの / 存在しなかったもの

- 🔴 **生産者の公式サイト —— 存在しない**（ドメインが一度も登記されていない）。
- 🔴 **生産者による醸造記述・テイスティングノート・沿革・畑の面積・樹齢 —— 一件も存在しない。**
- 🔴🔴 **亜硫酸の使用・不使用に関する生産者自身の記述 —— 一件も存在しない。**
  **とりわけ 1998 / 1999 / 2001 / 2006 の各年については完全な空白である。**
- 🔴 **1998 / 1999 / 2001 / 2006 の生産を裏づける公的資料 —— 存在しない（収穫申告は非公開）。**
- ⚠️ **`allemand-chaillot-nv` の `points: 95`・`winemaking`・`tasting`・`drinking_window` の出典 ——
  canonical 内にも記録されていない。**
- ⚠️ **現行 homologation 版（arrêté 2019-12-06）の cahier des charges PDF 実物。**
  🔴 **取得できたのは 2023-11-30 承認の PNO（異議申立手続）版である。**
  **INAO extranet のファイル名は appellation ごとに一貫せず、本件で通ったのは
  `PNO2023AOPCornas.pdf` という新しい形であった。** → 下記トラップ記録
- ⚠️ **Demeter France の会員一覧（JS シェルのため確定できず）。**

### 🔴 ⚠️ INAO ファイル名トラップ —— **本バッチ 4 度目。次の担当者へ**

🔴 **以下 9 通りをすべて試し、9 通りとも `HTTP 200` を返したが本文は HTML だった（PDF ではない）:**
`PNOCDCCornas.pdf` / `pnocdccornas.pdf` / `PNOCDC-Cornas.pdf` / `CDCCornas.pdf` /
`PNOCDCcornas.pdf` / `PNOCDCCORNAS.pdf` / `pnocdc-cornas.pdf` / `cdccornas.pdf` /
`PNOCDCCornas1.pdf`（`extranet.inao.gouv.fr/fichier/` と
`info.agriculture.gouv.fr/gedei/site/bo-agri/document_administratif-` の両方で）。
🔴 **実際に通ったのは `https://extranet.inao.gouv.fr/fichier/PNO2023AOPCornas.pdf`
—— `PNO` + **承認年** + `AOP` + 呼称名 という、既知のどの形とも違う第 3 の命名規則である。**
🔴 **`PNO<年>AOP<Name>.pdf` を候補リストに追加すること。**
**Crozes-Hermitage が `PNO2024AOPCrozesHermitage.pdf` と `PNO2020CDCCrozesHermitage.pdf` の
両方を持つことも確認しており、年と `AOP`/`CDC` の両方が変動する。**
🔴 **必ず本文先頭 4 バイトが `%PDF` であることを確認すること。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical 928 件を走査。文字列 `allemand` のヒットは 5 件で、
🔴 5 件すべてが `producer` フィールドのヒット。prose-only ヒットは 0 件。**
🔍 **OBP 掲載 4 本（`obp_intake_normalized_20260804.json` より）。
`match_state` は 4 行とも `alias`、`producer_state` も `alias`、
`cuvee_state` / `vintage_state` は 4 行とも `exact`、`confidence` は 4 行とも `0.95`。**
🔍 **本書が引用する「4 本」「5 レコード」の計数は
`obp_intake_normalized_20260804.json` と `migration/out/export/db_wine_canonical.json` から直接取得したものであり、
`research/out/t-01/mapping.json` は参照していない**（両者が resolved 判定で食い違う既知の問題があるため）。
🔍 **canonical / REGISTER.md の SHA-256 は着手前後で不変であることを確認済み。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | 🏛 **国家企業登記で法人名・SIREN/SIRET・設立日・法定形態・NAF・住所・座標・代表者と生年まで確定。同一住所の関連 5 法人も列挙できた。認証の不在も 3 経路で確定。**⚠️ **生産者自身の自称表記だけが不明** |
| **Overview** | ⚠️ **Medium-Low** | 🔴 **生産者の自己規定が一行も無い。**登記と認証の否定的事実は堅いが、**造り手が何を目指しているかは完全な空白** |
| **History** | 🔴 **None** | 🔴 **沿革は一件も確定していない。**表にあるのは登記事象と appellation の日付だけ |
| **Location** | 🔴 **Medium-High** | 🏛 **住所・コミューン・座標は確定。appellation の法的枠組みと自然条件は CDC から高密度に取れた。**🔴 **加えて `Chaillot` / `Reynard` の地籍上の実在・広がり・相対位置を確定できたのが本書最大の実務価値。**⚠️ **ただし Allemand の所有区画は完全に不明** |
| 🔴 **Farming** | ⚠️ **Low（否定側のみ High）** | 🔴 **「認証は無い」は 3 経路（Agence Bio SIRET 完全一致 ×3・Biodyvin 名簿・Demeter 規格の前提条件）で確定 = High。**🔴 **しかし実際に何をしているかは完全な空白。**🔴 **さらに OBP のヴィンテージが 1998–2006 で、認証の議論がそもそも届かない** |
| 🔴 **Winemaking** | 🔴 **None** | 🔴 **一件も確定していない。**🔴 **とりわけ亜硫酸について、本書は意図的に記述を拒否した** |
| 🔴 **Style** | 🔴 **None（appellation 側のみ Medium）** | 🔴 **生産者の公式テイスティングノートは存在しない。**🏛 **AOC Cornas 全体の公的官能記述は CDC から引けるが、この 4 本の描写ではない** |
| **Important Cuvées** | 🔴 **Medium-High** | 🔴 **`Chaillot` / `Reynard` が地籍リュー・ディとして実在し、CDC 第 XII 章がラベル記載を明示的に認めていることを二重に確定。プルミエ・クリュ不在も確定。**⚠️ **しかし二区画の違い（樹齢・土壌・傾斜）は一次資料が無く、4 ヴィンテージの外部裏づけも silence** |
| 🔴 **Staff Notes** | 🔴 **High** | ⚠️ **13 項目。**🔴 **「創業年」「承継の物語」「ヴェルセ」「ビオディナミ/オーガニック」「樹齢」「亜硫酸」「味のノート」「面積」「プルミエ・クリュ」「醸造」という、この生産者で最も踏みやすい誤りを塞いだ。**🔴 **亜硫酸の項が最重要** |
| **Canonical Conflict** | 🔴 **High** | 🔴 **`NV` の不可能性を CDC で証明し、`D-2026-08-05-12` への反例として提示。`S-2` に「マッチャ出力が同一破損に 2 通りの表現を返す」という新しい証拠を追加。`C-4` の逆形を指摘。フィールド単位で contradicted / unsourced / absent-as-key を分離。**🔴 **新番号は一つも開いていない** |
| 🔴 **総合** | 🔴 **Low-Medium —— staff-usable ではない。約 62%。** | **必須項目は形式上すべて埋まっている（Identity / Overview / Location / **Farming** / Important Cuvées の OBP 連結 / Staff Notes 芯 3 点 / Must-Not-Say / Sources / Open Questions）。**🔴 **しかし History・Winemaking・Style が三つとも完全な空白で、生産者自身の言葉が一行も無い。**🔴 **スタッフは「コルナスという呼称」「シャイヨとルナールが地籍リュー・ディであること」「造り手が何も公表していないこと」しか語れず、$1,600〜$2,600 の 20〜28 年熟成のボトルについて、味も造りも亜硫酸も一切語れない。**🔴 **公式サイトが原理的に存在しないため、この空白は追加のウェブ調査では埋まらない。** |

🔴 **reached_70: NO（約 62%）。**

🔴 **ステータス: `awaiting material from the team`.**

🔴 **ブロッカー（正確に）:**
**Thierry Allemand には公式ウェブサイトが存在せず、それらしいドメイン名が
一度も登記されたことがなく（`.com` は Verisign RDAP で 404、`.fr` は AFNIC RDAP で NOT_FOUND）、
Internet Archive にも過去のページが一件も無い。
そのため生産者が公表した醸造記述・テイスティングノート・沿革・畑の面積・樹齢が一件も存在せず、
`## History` / `## Winemaking` / `## Style` の 3 節が公的資料の代替では原理的に埋められない。**
🔴 **とりわけこの生産者で最も頻繁に問われる「無亜硫酸か否か」は、
生産者由来の資料が無い以上、本調査では答えられない。第三者記述は互いに一致していない。**
**INSEE/Sirene・Agence Bio・Biodyvin・Demeter 規格・INAO cahier des charges・DGFiP 地籍・
RDAP・Wayback という利用可能な公的経路はすべて使い切っており、追加のウェブ調査では改善しない。**

🔴 **必要なもの:**
1. 🔴 **ドメーヌ作成の technical sheet**（生産者の署名または `notes from the domaine` の明示があるもの）
   **または蔵からの直接回答。**
   **必須項目: `Chaillot` / `Reynard` の樹齢・面積・土壌・向き、両区画の違い、
   🔴 各ヴィンテージにおける亜硫酸の扱い、熟成、1998/1999/2001/2006 の生産有無。**
   ⚠️ **輸入元が自ら書いた三人称の販促シートでは要件を満たさない。**
2. 🔴 **物理ラベルの照合（下記）。**

### 🔴 物理ラベル照合タスク（**オンラインでは決着しない行**）

| # | 対象 | 確認事項 |
|---|---|---|
| **PL-1** | 🔴 **OBP 4 本すべてのボトル実物** | **ラベル上の生産者名の綴り。`Thierry` であることの実地確認（メニュー `Theirry`・輸入元 `Thiérry`・登記 `THIERRY` の三者が食い違っている）** |
| **PL-2** | 🔴 **`Chaillot` 2001 / 1999、`Reynard` 2006 / 1998** | **ラベルが区画名をどう綴っているか（`Chaillot` / `Reynard` そのままか、頭文字 `C` / `R` か、定冠詞を伴うか）。canonical の `"Chaillot"` / `"Reynard"` の正規形を決めるのに要る** |
| **PL-3** | 🔴 **同 4 本** | **裏ラベル／表ラベルの亜硫酸表示（`contient des sulfites` の有無）。** ⚠️ **EU 規則上、10 mg/L 超で表示義務がある。表示が無ければ 10 mg/L 以下であることの強い示唆になる。**🔴 **これはオンラインでは絶対に決着しない、この生産者で最も価値の高い実地確認である** |
| **PL-4** | **同 4 本** | **アルコール度数の実測表示。CDC の上限 13.5% と突き合わせる** |
| **PL-5** | 🔴 **`allemand-chaillot-nv` に対応する実物があるか** | **在庫棚に「ヴィンテージ表記の無い Chaillot」が実在するか。実在しなければこのレコードは統合対象である** |

---

## Open Questions

1. 🔴 **`D-2026-08-05-12` の `'NV'` 88 件は、本当に全部 Champagne なのか。**
   🔴 **本件で少なくとも 1 件、NV がありえない静止赤 AOC（Cornas）に `'NV'` が付いていることが
   確定した。「NV は non-vintage Champagne について legitimate」という読みは反例を持つ。**
   🔴 **88 件を appellation 別に再分類する横断走査が要る。本書では走査していない（指示範囲外）。**
   → **採番・再 restate は CTO / Akio の権限。**

2. 🔴🔴 **亜硫酸 —— 1998 / 1999 / 2001 / 2006 の各年に何が行われたか。**
   🔴 **本調査では生産者由来の資料が一件も存在せず、答えられなかった。**
   ⚠️ **第三者記述は互いに一致していない（「ごく少量」「特定年のみ無亜硫酸のキュヴェ」等）。**
   🔴 **本書はこの 4 本の醸造を性格づけることを明示的に拒否した。**
   → 🔴 **蔵からの直接回答か、`PL-3`（ラベルの sulfites 表示）でしか決着しない。**

3. ⚠️ **1998 / 1999 / 2001 / 2006 の各ヴィンテージが実際に生産されたか。**
   🔴 **公的・生産者一次資料は 0 件。収穫申告は非公開。**
   🔴 **Batch 9 Abreu 先例により、これは「沈黙」であって「誤り」ではない。**
   **canonical にレコードは存在するので unresolved ではないが、外部裏づけは無い。**

4. ⚠️ **`THEO ALLEMAND`（SIREN 909883225・2022-01-26・同一住所・同一 NAF）をどう扱うか。**
   🏛 **これは登記事実である。**
   🔴 **本書は承継・世代交代・役割分担を一切推論していない**（Batch 8 の Roulot 先例）。
   ❓ **別ブランドとして OBP / canonical に現れる可能性があるか、
   それとも同一ドメーヌの別法人にすぎないかは、蔵への確認が要る。**
   🔴 **`GFA LE GRAND CADE`（2021・農地保有体）に両名が名を連ねている点も同様に、
   登記事実として記録するにとどめる。**

5. ⚠️ **`CHAILLOT` / `REYNARD` の土壌。**
   🏛 **CDC は Cornas の大部分を花崗岩、北端 `Pied-la-Vigne` を石灰崩積土（「ごく一部」）とするが、
   土壌分布をリュー・ディ単位では示していない。**
   🔍 **地籍上、`CHAILLOT` も `REYNARD` も `PIED LA VIGNE` とは別のリュー・ディで、その西〜南西にある。**
   🔴 **しかし「だから両区画は花崗岩である」と断定はしていない。**
   ❓ **BRGM の地質図など、より細かい公的経路がありうるが本調査では未着手。**

6. ⚠️ **`Theirry Allemand` を alias として登録すべきか。**
   🔍 **4 行とも `producer_state: alias` に落ちており、alias 登録で機械的には解決する。**
   🔴 **しかしこれは単純な誤植であり、alias として固定すると誤りが正規の別名として定着する。**
   ❓ **「メニュー印字の誤り」として intake 側で訂正する経路のほうが正しい可能性がある。**
   → **設計判断であり、本書では実行していない。**

7. ⚠️ **`allemand-chaillot-nv` の内容（`points: 95` / `winemaking` / `tasting` / `drinking_window` /
   `aging` / `obp_note`）はどこから来たのか。**
   🔴 **canonical 内に出典が記録されていない。**
   🔴 **かつ OBP に載っている 4 本のほうがこれらのフィールドを一切持たず、
   OBP に載っていない NV レコードだけが持っている。**
   ❓ **この非対称は「NV が表示用の代表レコードとして作られた」ことを示唆するが、
   本書では確認できていない。**

8. ⚠️ **現行 homologation 版（arrêté 2019-12-06）の cahier des charges 実物。**
   🔴 **取得できたのは 2023-11-30 承認の PNO 版で、冒頭に「最終稿を予断しない」と明記されている。**
   ⚠️ **PNO 版は改正部分を旧値・新値の併記で出力するため、数値が連結して読める箇所がある
   （`20092021` / `115160 hectares` / `36005000 hectolitres`）。**
   🔴 **本書が引用した規定値（収量 40/46/50、糖 171 g/L、アルコール 10.5%/13.5%、
   密度 4400、échalas 1.50 m 等）は連結が生じていない単一値の箇所のみである。**
   ❓ **確実を期すなら Légifrance で arrêté 2019-12-06 の別添を取るべきだが、本調査では未取得。**
