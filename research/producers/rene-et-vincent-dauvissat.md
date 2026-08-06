# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件も存在しない。**
> 🔍 **本調査で実測**: `migration/out/export/db_wine_canonical.json` = **928 レコード / 383 の distinct producer 値**。
> **`Dauvissat` を含む producer フィールドは 0 件。散文（prose）中の出現も 0 件。**
> **すなわち producer-field ヒット 0 ／ prose-only ヒット 0 の完全な不在である。**
> **したがって本書は、この生産者に関する THÉSEUS 最初の記録である。**
> 🔒 **これは gap（不在）であって conflict ではない。**（Batch 9 の Abreu が確立した扱い。）
> **REGISTER.md には一切触れていない。新しい番号も開いていない。**
> 本書は昇格前の研究記録であり、**canonical も OBP も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式資料**（一次資料）—— 🔴 **本ドシエには 1 件も存在しない。**
> `🏛` **公的レジストリ / 規制一次資料**
>    —— INAO cahier des charges（Chablis / Chablis Grand Cru）、フランス国家企業登記
>    （`recherche-entreprises.api.gouv.fr`）、Agence Bio、Ecocert 発行証書、Demeter France
> `🏛⚠️` **業界団体（interprofession）のディレクトリ** —— BIVB / Chablis-wines。
>    **公的登記でも規制文書でもなく、生産者自身の publication でもない。申告ベースの名簿である。**
>    **本書では「識別情報（住所・電話・ウェブサイト欄の有無・申告された生産 AOC）」に限って用い、**
>    **味・醸造・沿革の根拠には一切用いていない。**
> `📄` 生産者が書いた off-domain 資料 —— 🔴 **本ドシエには 1 件も存在しない。**
> `⚠️` **出典間で食い違っている／出典が沈黙している／第三者の未検証情報**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出 ／ `❓` 未解決
> `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: **2026-08-06（JST 実時刻取得）**
>
> ---
>
> ## 🔴🔴 本ドシエ最大の結論 ① —— **`La Forest` は INAO の climat 一覧に存在しない**
>
> 🏛 **Chablis の cahier des charges 全文（20 頁）を機械的に走査した結果、
> `Forest` という綴りは大文字小文字を問わず `0 回` しか出現しない。すなわち一度も出現しない。**
> 🏛 **Chablis Grand Cru の cahier des charges でも同じく `0 回`である。**
>
> 🔴 **INAO が premier cru の `NOM DE CLIMAT` として掲げる該当形は 2 つで、いずれも複数形である ——
> `Forêts`（冠詞なし）と `Les Forêts`（冠詞あり）。どちらも lieudit `Les Forêts` に対応し、
> 傘となる climat は `Montmains` である。**
> ⚠️ 🔴 **さらに罠がある —— INAO には `La Forêt`（単数・冠詞あり）と `Sur la Forêt` も実在するが、
> これらは `Montmains` ではなく `Vau Ligneau` の傘に属する別の climat である。**
> 🔴 **メニューの `La Forest` は「単数＋冠詞」であり、字面としては
> `Les Forêts`（Montmains）よりも `La Forêt`（Vau Ligneau）に近い。**
> 🔴 **したがって素朴な正規化規則（アクセント除去・冠詞処理・綴り揺れ吸収）を当てると、
> 別の climat に誤って着地しうる。**
> 🔴 **これは正規化規則で橋渡ししてはならない。明示的な alias が要る。**
> **Batch 8 の `Les Champs Gains` / `Les Champs gain` と同型である。** → §Important Cuvées / §Canonical Conflict ①
>
> 🏛⚠️ **加えて、appellation 側の名簿（BIVB）はこの生産者の当該ワインを `Chablis 1er Cru - Forêt`
> （単数・冠詞なし）と記載している。**
> 🔴 **すなわち同一のワインに対して 3 つの異なる表記が並存する ——
> `La Forest`（メニュー） / `Forêt`（業界団体名簿） / `Forêts`・`Les Forêts`（INAO 法定）。
> 3 つのどれ 2 つも一致しない。**
>
> ---
>
> ## 🔴🔴 本ドシエ最大の結論 ② —— **公式サイトは存在しない（実測で証明した）**
>
> **単に「無い」と報告するのではなく、5 通りの独立な経路で不在を測定した。**
> 1. 🔍 **候補ドメイン 8 件が DNS で NXDOMAIN**
>    （`vincentdauvissat.com` / `.fr`、`domaine-dauvissat.com`、`rene-et-vincent-dauvissat.com`、
>    `renedauvissat.fr`、`dauvissat-camus.fr`、`dauvissatchablis.com`、`dauvissat-chablis.fr`）。
> 2. ❌ **`dauvissat.fr` は解決するが、`Dovendi - Domain for sale` の売却ページである。**
>    🏛 **AFNIC WHOIS の holder は組織 `Nomio24`、レジストラ `XNS Registrar B.V.`、登録 2023-07-23。**
>    🔴 **これは本 Batch の Vilmart で既に掴んだのと同じ Dovendi の売却基盤である（look-alike 再犯）。**
> 3. ❌ **`dauvissat.com` は `https://www.linkedin.com/in/nicolas-dauvissat` へリダイレクトする個人プロフィールで、
>    生産者とは無関係。**（A レコードは OVH、MX は ProtonMail。）
> 4. ❌ **`domaine-dauvissat.fr` は実在し中身もあるが、`Beine` の
>    **`Domaine Dauvissat Agnès, Didier et Florent`** という**別の蔵**である。→ §Identity の entity separation
> 5. 🏛 **Agence Bio の当該事業者レコードの `siteWebs` は空配列ではない ——
>    `typeSiteWeb: Site Officiel` のレコードが 1 件存在し、その `url` が空文字列 `''` である。**
>    🔴 **これは Batch 8 の Roulot（`siteWebs: []`）とも、本 Batch の Alvina Pernot
>    （ドメインは保有・本文 9 バイト）とも異なる、第 3 の形である ——
>    「公式サイト欄が登録されているのに URL が空」。**
> 6. 🏛⚠️ **BIVB の生産者名簿にも `website` 欄そのものが無い。**
> 7. 🔍 **Internet Archive の CDX に、上記候補ドメインの生産者サイトは 1 件も無い**
>    （`dauvissat.com` に 2 行あるが上記リダイレクト先、`domaine-dauvissat.fr` の 5 行は別蔵）。
>
> 🔴 **したがって本ドシエには、生産者自身の言葉が一行も無い。**
> **醸造・スタイル・沿革・畑の面積・樹齢・キュヴェの全数は、公式資料が存在しないため全面的に空白である。**
> **それらを一般的なブルゴーニュ知識や第三者評論で埋めることはしていない。**
>
> ---
>
> ## 🔴🔴 本ドシエ最大の結論 ③ —— **OBP の 2 ヴィンテージはいずれも有機認証の対象外である**
>
> 🏛 **Agence Bio（exact SIRET 照会）——
> `numeroBio 26543` / `SCEV VINCENT DAUVISSAT` / 認証機関 `Ecocert France`（`FR-BIO-01`）/
> `etatCertification: ENGAGEE` / 🔴 `datePremierEngagement: 2021-04-27` /
> `mixité: Non`（有機と慣行の併存なし）/ `dateSuspension: null` / `dateArret: null`。**
> 🔴 **OBP の `2019` は engagement の 2 年以上前であり、完全に対象外。**
> 🔴 **OBP の `2021` は engagement（2021-04-27）の直後の収穫であり、転換期間の初年度にあたる。**
> 🔴 **したがって OBP 掲載の 4 本はいずれも「有機認証ワイン」ではない。**
> ⚠️ **「有機栽培」「ビオディナミ」とフロアで言わないこと。** → §Farming / §Staff Notes
>
> 🏛 **Ecocert 発行証書の scope は `Agriculteur (production végétale)`（植物生産＝栽培）であり、
> 醸造・加工（transformation）は掲げられた scope に入っていない。**
> 🔴 **すなわち仮に将来認証が成立しても、それは「畑の認証」であって「ワインの認証」ではない。**
>
> 🏛 **Demeter France のディレクトリ検索は完全に解決し、
> `Il semblerait qu'il n'y ait pas de résultats pour cette recherche`（該当なし）を返した。
> → Demeter 認証は proved negative。**
> ⚠️ **Biodyvin は検索エンドポイントが検索結果ページを返さずトップページに落ちたため、
> proved negative として扱わない。** → Open Questions 6
>
> ---
>
> ## 🔴 本ドシエ最大の結論 ④ —— **`Dauvissat` は Chablis で 9 つの別法人に分かれている**
>
> 🔴 **`D-2026-08-05-08`（同名別主体）の最も濃い実例。本 Batch で 3 度目の発火。**
> 🏛 **国家企業登記で `Dauvissat` を照会すると、Chablis（89800）だけで 8 法人、
> 加えて別村 Beine に 1 蔵が存在する。うち NAF `01.21Z`（ブドウ栽培）は 4 法人。**
> 🔴 **本件の対象は `8 RUE EMILE ZOLA 89800 CHABLIS` に同居する 3 法人だけであり、
> 他は一切混ぜてはならない。** → §Identity

---

## Identity

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`René & Vincent Dauvissat`**（OBP 4 行すべて同一） |
| 🔴 **公式表記** | 🔴 ⚠️ **確認不能。公式サイトが存在せず、生産者自身による表記が 1 件も取得できていない。** |
| 🔴 **経営体（operating entity）** | 🏛 🔴 **`SCEV VINCENT DAUVISSAT`** — SIREN **`317577849`** / SIRET **`31757784900019`**。**設立 `1979-01-01`**。NAF **`01.21Z`（ブドウ栽培）**。法定形態コード **`6597`**（SCEV＝Société Civile d'Exploitation Viticole）。状態 **`A`（活動中）**。`est_bio: true` |
| 🔴 **土地保有体** | 🏛 🔴 **`GFA DAUVISSAT - CAMUS`** — SIREN **`520830076`**。**設立 `2010-01-30`**。NAF `00.00Z`。法定形態コード **`6534`**（GFA＝Groupement Foncier Agricole）。**同一住所。**状態 `A`<br>🔴 **メニュー等で流通する `Dauvissat-Camus` という形は、法的にはこの土地保有 GFA の名称である。ワインのブランド名としては確認できていない。** |
| 🔴 **歴史的な個人事業体** | 🏛 🔴 **`RENE DAUVISSAT`** — SIREN **`778655506`** / SIRET `77865550600013`。**`entrepreneur individuel`（個人事業主）。同一住所。状態 `A`（現在も登記が生きている）。**NAF は旧コード `01.1G`<br>⚠️ **`date_creation: 1900-01-01` は登記側の sentinel 値であり、実際の創業年ではない。**`date_debut_activite` は `1994-12-25`。**この 2 つのどちらも創業年として引用してはならない。** |
| **持株会社（2025 新設）** | 🏛 **`SC LE NOYAU`** — SIREN `988486353`。**設立 `2025-06-17`**。NAF `64.20Z`（持株会社）。法定形態コード `6599`。**同一住所。**SCEV の無限責任社員（法人）として登記されている |
| 🔴 **SCEV の登記上の役員** | 🏛 🔴 **`DAUVISSAT ETIENNETTE`（1989 年生）= Gérant et associé indéfiniment responsable**<br>🏛 🔴 **`DAUVISSAT GHISLAIN`（1984 年生）= Gérant et associé indéfiniment responsable**<br>🏛 `DAUVISSAT SOLENNE`（1985 年生）= 無限責任社員<br>🏛 `SC LE NOYAU`（SIREN 988486353）= 無限責任社員（法人） |
| 🔴 **GFA の登記上の役員** | 🏛 🔴 **`DAUVISSAT VINCENT`（1957 年生）= Gérant et associé indéfiniment responsable**<br>🏛 他に 9 名の無限責任社員 —— `VALLE (DAUVISSAT) MARIE-ELISABETH`（1954 年生）／`DAUVISSAT ETIENNETTE`（1989）／`DAUVISSAT GHISLAIN`（1984）／`DAUVISSAT SOLENNE`（1985）／`FROCRAIN LOÏC NOËL VINCENT`（1988）／`FROCRAIN MARC LOUIS RENE`（1983）／`MOREAU FROCRAIN (FROCRAIN) SANDRINE MARIE PAULE`（1984）／`VALLE ANTOINE VINCENT`（1992）／`VALLE THIBAULT RENE PRIMO`（1991） |
| 🔴 **世代交代の登記上の形** | 🏛 🔴 **`Vincent Dauvissat`（1957 年生）は SCEV（経営体）の役員として登記されていない。**<br>🔴 **SCEV の業務執行社員は 1984 年生と 1989 年生の 2 名である。**<br>🔴 **Vincent は GFA（土地保有体）の Gérant である。**<br>⚠️ **これは Batch 8 の Roulot と同型の構造（旧世代が GFA、新世代が経営体）だが、
これは登記上の記載であって、実務上の役割分担を意味するとは限らない。** → Open Questions 3 |
| 🔴 **`Vincent` のフルネーム** | 🏛 🔴 **`DAUVISSAT VINCENT ROBERT`**（SC LE NOYAU の登記。1957 年生）。**ミドルネームは `Robert`** |
| **所在** | 🏛 ✅ **`8 rue Emile Zola, 89800 Chablis, France`**<br>🔴 **国家企業登記・Ecocert 発行証書・Agence Bio・BIVB 名簿の 4 者が完全一致する。** |
| **座標** | 🏛 🔍 **lat `47.8115890525709` / long `3.79990858157804`**（Sirene）。🏛⚠️ BIVB は `47.8114920 / 3.7999985` |
| **電話 / FAX** | 🏛⚠️ **`03 86 42 11 58` / FAX `03 86 42 85 32`**（BIVB 名簿。**生産者自身の掲出ではない**） |
| **従業員規模** | 🏛 **INSEE 区分コード `02`（2023 年基準）** |
| **本店の活動開始日** | 🏛 **`2008-01-01`**（SCEV の siege）。⚠️ **これは事業所レコードの開始日であって創業年ではない** |
| 🔴 **有機認証** | 🏛 🔴 **`Ecocert France` / `FR-BIO-01` / `etatCertification: ENGAGEE` / `datePremierEngagement: 2021-04-27` / `mixité: Non` / 停止日・終了日ともに `null`**<br>🏛 **証書上の被認証者名は `Vincent Dauvissat`、scope は `Agriculteur (production végétale)`、規則は `(EU) 2018/848`**<br>🔴 **OBP の 2019・2021 はいずれも認証済ワインではない** → §Farming |
| **Bio 番号** | 🏛 **`numeroBio: 26543`**（Agence Bio） |
| 🔴 **公式サイト** | 🔴 **存在しない（5 経路で実測）。**Agence Bio の `siteWebs` は **`Site Officiel` レコードが 1 件あるが `url` が空文字列 `''`**。BIVB 名簿には website 欄が無い。候補ドメイン 8 件は NXDOMAIN。`dauvissat.fr` は Dovendi 売却ページ、`dauvissat.com` は LinkedIn 個人ページ、`domaine-dauvissat.fr` は別蔵 |
| 🔴 **canonical id** | 🔴 **存在しない。**🔍 **canonical 383 生産者に一致・別名・近似いずれも無し。producer-field 0 件 / prose-only 0 件** → §Canonical Conflict ⑤ |

### 🔴 🏛 Entity separation —— **`Dauvissat` を名乗る Chablis の別法人（混ぜてはならない）**

**`D-2026-08-05-08`。国家企業登記の照会結果をそのまま置く。**
🔴 **本件の対象は No.1〜3（`8 rue Emile Zola` に同居する 3 法人）だけである。**

| # | 🏛 登記名 | SIREN | 住所 | 設立 | NAF | 状態 | 本件との関係 |
|---|---|---|---|---|---|---|---|
| **1** | 🔴 **`SCEV VINCENT DAUVISSAT`** | **`317577849`** | 🔴 **8 rue Emile Zola, Chablis** | 1979-01-01 | `01.21Z` | A | 🔴 **本件の経営体。OBP 4 行はこれに帰属する** |
| **2** | 🔴 **`GFA DAUVISSAT - CAMUS`** | `520830076` | 🔴 **8 rue Emile Zola, Chablis** | 2010-01-30 | `00.00Z` | A | 🔴 **本件の土地保有体。`Dauvissat-Camus` という呼称の法的な出どころ** |
| **3** | **`RENE DAUVISSAT`** | `778655506` | 🔴 **8 rue Emile Zola, Chablis** | ⚠️ sentinel | `01.1G` | A | **本件の歴史的な個人事業体。現在も登記が生きている** |
| **3b** | `SC LE NOYAU` | `988486353` | 8 rue Emile Zola, Chablis | 2025-06-17 | `64.20Z` | A | 本件の持株会社（2025 新設）。ワイン生産体ではない |
| ❌ **4** | **`EARL DOMAINE JEAN DAUVISSAT PERE ET FILS`** | `317145456` | **11-13 rue de Léchet, Chablis** | 1979-01-01 | `01.21Z` | A | 🔴 **別蔵。**Gérant は `DAUVISSAT FABIEN`（1985 年生）。🏛 **Agence Bio では `numeroBio 91`、`siteWebs: []`** |
| ❌ **5** | **`JEAN ET SEBASTIEN DAUVISSAT`** | `392822821` | **3 rue de Chichée, Chablis** | 1994-11-01 | `01.21Z` | A | 🔴 **別蔵。**役員は `BOISSET NATHALIE` / `DEPUYDT LUCIE` |
| ❌ **6** | **`BENOIT DAUVISSAT`** | `819696295` | **15 av. de la République, Chablis** | 2016-04-01 | `01.21Z` | A | 🔴 **別蔵** |
| ❌ **7** | **`EARL TRIBUT DAUVISSAT`** | `388433138` | **Poinchy, 15 rue de Poinchy, Chablis** | 1992-07-07 | `01.21Z` | A | 🔴 **別蔵**（Tribut 家） |
| ❌ **8** | **`GFR RAVENEAU-DAUVISSAT`** | `539999037` | **18 rue du Panonceau, Chablis** | 2011-12-31 | `68.20B` | A | 🔴 **Raveneau 側の土地保有体。**⚠️ **canonical には `Domaine François Raveneau` が既に 1 件存在する。混同しないこと** |
| ❌ **9** | **`MICHEL DAUVISSAT`** | `333016830` | **7 rue de Fye, Chablis** | 1984-05-02 | `01.1G` | 🔴 **`C`（停止）** | **別主体。既に活動停止** |
| ❌ **10** | **`CABINET DAUVISSAT`** | `949273817` | Milly, 14 rue de Charlevaux, Chablis | 2023-02-20 | `68.20B` | A | **不動産業。ワインとは無関係** |
| ❌ **11** | **`Domaine Dauvissat Agnès, Didier et Florent`** | ❓ 未照会 | 🔴 **`Beine`（別村）** | ❓ | ❓ | ❓ | 🔴 **別蔵。**`domaine-dauvissat.fr` を運営しているのはこの蔵であって本件ではない |
| ❌ | **`ISABELLE DAUVISSAT (POITRAT)`** | `442321576` | Auxerre | 2002-07-01 | `86.90D` | A | **医療系。ワインとは無関係** |

⚠️ 🔴 **`René & Vincent Dauvissat` / `René Dauvissat` / `Vincent Dauvissat` / `Dauvissat-Camus` の 4 形について**

1. 🏛 **国家登記に存在するのは `SCEV VINCENT DAUVISSAT`（経営体）、`RENE DAUVISSAT`（個人事業体）、
   `GFA DAUVISSAT - CAMUS`（土地保有体）の 3 つで、いずれも同一住所である。**
2. 🏛 **Ecocert 発行証書の被認証者名は `Vincent Dauvissat`。**
3. 🏛⚠️ **BIVB 名簿の掲載名は `Domaine Dauvissat Vincent`。**
4. 🔴 ⚠️ **`René & Vincent Dauvissat`（OBP 印字）という結合形は、
   照会したいずれの 🏛 レジストリにも現れない。**
   **ラベル上の表記としては十分ありうるが、本書は確認していない。**
5. 🔴 **したがって canonical 名を本書では決定しない。**
   **`René & Vincent Dauvissat` は menu-printed form として保持し、
   ラベル実物を見るまで正規名を確定させない。** → §Canonical Conflict ⑤ / Open Questions 1

---

## Overview

🔴 ⚠️ **この節は、通常なら生産者自身の自己規定で書かれる。本件にはそれが 1 行も無い。**
**以下はすべてフランス国家の公的登記・認証機関・appellation 名簿から取れた事実だけである。**

🏛 **Chablis 村の中心部、`8 rue Emile Zola` に本拠を置く家族経営のブドウ栽培・醸造事業体。**
**経営体 `SCEV VINCENT DAUVISSAT`（1979 年設立、NAF `01.21Z`）、
土地保有体 `GFA DAUVISSAT - CAMUS`（2010 年設立）、
および現在も登記の生きた個人事業体 `RENE DAUVISSAT` が同一住所に同居する。**
🏛 **従業員規模は INSEE 区分 `02`（2023 年基準）—— 小規模である。**

🏛⚠️ **BIVB（ブルゴーニュ業界団体）の名簿が申告として掲げる生産 AOC は 9 つ ——
`Petit Chablis` / `Chablis` / `Chablis 1er Cru - Forêt` / `Chablis 1er Cru - Montée de Tonnerre` /
`Chablis 1er Cru - Sécher` / `Chablis 1er Cru - Vaillons` / `Chablis Grand Cru - Les Clos` /
`Chablis Grand Cru - Preuses` / 🔴 `Irancy`（赤）。**
🔴 **`Irancy` は Chablis ではなく、Yonne 県の別 AOC の赤ワインである。**
🔴 ⚠️ **ただしこれは「AOC の申告」であって「キュヴェの一覧」ではない。**
**同一 AOC で複数のキュヴェを瓶詰めしているかどうかは、この名簿からは分からない。** → §Important Cuvées 行 1

🏛⚠️ **BIVB 名簿の輸出先申告: ドイツ・ベルギー・アメリカ・日本・オランダ・イギリス。**

🔍 **THÉSEUS における状態** —— 🔴 **canonical に生産者レコードもキュヴェレコードも 0 件。
OBP 掲載 4 本すべてが `producer_state` / `cuvee_state` / `vintage_state` ともに `unresolved`、
`confidence 0.0`、`proposed_canonical_producer` は `null`。
この生産者は THÉSEUS DB にまだ存在していない。**

---

## History

🔴 ⚠️ **公式資料が存在しないため、沿革は本ドシエでは書けない。**
🔒 **第三者（評論家サイト・輸入元・小売）が流布している創業年・世代数・当主交代の年は、
方針により一切採用していない。それらをここに書くことは捏造と同じである。**

**🏛 国家登記から言える「登記上の事実」だけを置く。**

| 🏛 登記上の日付 | 事象 | ⚠️ 注意 |
|---|---|---|
| ⚠️ **`1900-01-01`** | `RENE DAUVISSAT`（個人事業体）の `date_creation` | 🔴 **これは登記側の sentinel 値である。創業年として引用してはならない** |
| **`1979-01-01`** | 🔴 **`SCEV VINCENT DAUVISSAT` の設立** | ⚠️ **法人設立日であって、ブドウ栽培の開始年ではない** |
| **`1994-12-25`** | `RENE DAUVISSAT` の `date_debut_activite` | ⚠️ **事業所レコードの開始日。実態を意味しない** |
| **`2008-01-01`** | SCEV の本店（siege）の活動開始日 | ⚠️ **同上** |
| **`2010-01-30`** | 🔴 **`GFA DAUVISSAT - CAMUS` の設立** | **土地保有体の分離。`Camus` の名がここで法的に現れる** |
| 🔴 **`2021-04-27`** | 🔴 **Ecocert への有機初回コミット（`datePremierEngagement`）** | 🔴 **OBP の両ヴィンテージとの関係で決定的** → §Farming |
| **`2025-06-17`** | `SC LE NOYAU`（持株会社）の設立 | **直近の資本構成の変化** |

❓ **公式に無い（したがって本書に無い）**: 創業年、世代数、当主の交代時期、
`René Dauvissat` と `Vincent Dauvissat` の続柄、`Camus` 家との関係の由来、
畑の取得年、醸造所の建設年、栽培方式を変更した年。
🔴 **`Camus` は 🏛 GFA の名称に現れるだけで、その由来は本書では確認できていない。** → Open Questions 2

---

## Location

| | |
|---|---|
| **Country** | **France** 🏛 |
| **Region / Département** | **Bourgogne / Yonne（89）** 🏛 |
| **Commune** | 🏛 **`Chablis`（INSEE 89800）** |
| **住所** | 🏛 **`8 rue Emile Zola, 89800 Chablis`**（登記・Ecocert・Agence Bio・BIVB の 4 者一致） |
| **座標** | 🏛 **lat `47.81159` / long `3.79991`**（Sirene） |
| ❓ **畑の所在・面積・区画** | 🔴 **一切不明。**生産者が公表しておらず、🏛 DGFiP 地籍からは「どの区画を誰が耕作しているか」は分からない |

### 🏛 AOC の法的構造 —— **OBP 4 行を規制一次資料に照らす**

**［規制一次資料］INAO cahier des charges
`AOC « Chablis »`（v2.2 du 16/09/2010、20 頁）および
`AOC « Chablis Grand Cru »`（v2.2 du 16/09/2010）。**
⚠️ 🔴 **重要な但し書き —— 取得した 2 つの PDF はいずれも
`Procédure nationale d'opposition`（全国異議申立手続）版であり、
「削除が提案された規定は取消線 XXX で表示される」と明記されている。**
**したがって数値が `153 161` のように 2 つ並ぶ箇所は、`153` が旧値（取消線）、`161` が新値である。**
**本書は新値を採り、その旨をここに明記する。最終確定版との異同は未検証である。** → Open Questions 5

| 🏛 事項 | AOC « Chablis » | AOC « Chablis Grand Cru » |
|---|---|---|
| **初認定** | **1938 年 1 月 13 日のデクレ** | **同じく 1938 年 1 月 13 日のデクレ** |
| **色 / タイプ** | **白のスティルワインのみ**（`vins tranquilles blancs`） | **同じ** |
| **地理的範囲** | Yonne 県の複数コミューン | 🔴 **`Chablis` コミューンの territory のみ** |
| **区画画定** | 🔴 **1978 年 1 月 31 日の comité national による承認** | 🔴 **同じく 1978 年 1 月 31 日** |
| **品種** | 🔴 **`chardonnay B` のみ** | 🔴 **`chardonnay B` のみ** |
| **植栽密度** | **最低 5,500 本/ha** | **最低 5,500 本/ha** |
| **灌漑** | 🔴 **禁止（`L'irrigation est interdite`）** | 🔴 **禁止** |
| **糖分最低 / 自然アルコール最低** | **Chablis: 161 g/l ・ 10%**<br>**1er cru: 170 g/l ・ 10.5%** | 🔴 **178 g/l ・ 11%** |
| **収量（rendement）** | **Chablis: 60 hl/ha**<br>**1er cru: 58 hl/ha** | 🔴 **54 hl/ha** |
| **上限収量（butoir）** | **Chablis: 70 hl/ha ／ 1er cru: 68 hl/ha** | 🔴 **64 hl/ha** |
| **補糖後の総アルコール上限** | **Chablis: 13% ／ 1er cru: 13.5%** | ⚠️ 本書未抽出 |
| **禁止設備** | 🔴 **連続式プレス（`pressoirs continus`）禁止／木片（`morceaux de bois`）の使用禁止** | ⚠️ 本書未抽出 |

### 🔴 🏛 premier cru の「傘 climat / 個別 climat」構造 —— **本ドシエの中核**

🏛 **Chablis の cahier des charges 第 I 章 II 節の原文 ——
「L'appellation d'origine contrôlée peut être complété de la mention « premier cru »,
`suivie éventuellement d'un nom de climat d'origine`」。**
🔴 **`éventuellement`（任意で）が効いている —— climat 名は付けても付けなくてもよい。**

🏛 **同 IV 節 2° b) は「premier cru に格付けされた climat の一覧」を
`COMMUNE / NOM DE CLIMAT / LIEUDIT` の 3 列表として掲げる。**
🔴 **この表の構造そのものが、傘と個別の法的関係を表現している ——
`同じ lieudit が、傘の NOM DE CLIMAT の下にも、それ自身の NOM DE CLIMAT としても、二重に現れる`。**

🔴 **`Montmains` の実例（本件の行 2 に直結）**

| 🏛 NOM DE CLIMAT | 🏛 対応する LIEUDIT |
|---|---|
| 🔴 **`Montmains`（傘）** | **`Les Monts Mains` / 🔴 `Les Forêts` / `Les Bouts des Butteaux` / `Vaux Miolot` / `Le Milieu des Butteaux` / `Les Ecueillis` / `Vaugerlains`** |
| **`Les Monts Mains`** | `Les Monts Mains` |
| 🔴 **`Forêts`** | 🔴 **`Les Forêts`** |
| 🔴 **`Les Forêts`** | 🔴 **`Les Forêts`** |
| **`Butteaux`** | `Les Bouts des Butteaux` / `Vaux Miolot` / `Le Milieu des Butteaux` / `Les Ecueillis` / `Vaugerlains` |
| **`Les Bouts des Butteaux`** ほか | それぞれ同名の lieudit |

🔴 **したがって lieudit `Les Forêts` のブドウから造ったワインは、法的に
`Chablis Premier Cru Montmains`（傘）とも `Chablis Premier Cru Forêts` とも
`Chablis Premier Cru Les Forêts` とも名乗れる。これが「傘か個別か」の法的な中身である。**

🔴 **`Vaillons` も同じ構造**（傘 `Vaillons` の下に `Les Vaillons` / `Sur les Vaillons` /
`Les Grands Chaumes` / `Les Chatains` / `Chatains` / 🔴 `Sécher` / `Les Beugnons` / `Les Lys` /
`Champlain` / `Les Minos` / `Les Roncières` / `Les Epinottes` の 12 lieudit があり、
それぞれが個別の NOM DE CLIMAT としても掲げられる）。
🔴 **INAO の法定綴りは `Sécher` である。**（BIVB 名簿も `Sécher`。）

🔴 **`Montée de Tonnerre` も傘である**（commune `Chablis (Fyé)`。
lieudit `Montée de Tonnerre` / `Les Chapelots` / `Pied d'Aloup` / `Sous Pied d'Aloup` /
`Côte de Bréchain` を擁し、`Chapelot` / `Les Chapelots` / `Pied d'Aloup` /
`Sous Pied d'Aloup` / `Côte de Bréchain` がそれぞれ個別 climat としても掲げられる）。

### 🔴 🏛 Grand Cru の climat 命名 —— **冠詞は一律ではない**

🏛 **Chablis Grand Cru の cahier des charges 第 I 章 II 節の原文（列挙は逐語）——
「Le nom de l'appellation d'origine contrôlée « Chablis Grand Cru » peut être complété
d'un des noms de climat d'origine
« Blanchot », « Bougros », 🔴 « Les Clos », « Grenouilles », « Preuses », « Valmur » et « Vaudésir »」。**

🔴 **7 つの Grand Cru climat のうち、冠詞 `Les` を伴うのは `Les Clos` ただ 1 つである。**
**他の 6 つは無冠詞（`Blanchot` は単数、`Preuses` は複数無冠詞）。**
🔴 ⚠️ **したがって「Chablis の Grand Cru には一律で冠詞を付ける／外す」という正規化規則を書いてはならない。**
**Batch 8 の Meursault（`Les Bouchères` は冠詞あり、`Perrières` は冠詞なし）と同じ性質である。**

🏛 **Grand Cru の `NOM DE CLIMAT / LIEUDIT` 対応（commune はすべて `Chablis`、Blanchot のみ `Chablis (Fyé)`）**

| 🏛 NOM DE CLIMAT | 🏛 LIEUDIT |
|---|---|
| `Blanchot` | `Côte de Blanchot` |
| `Bougros` | `Les Bouguerots` |
| 🔴 **`Les Clos`** | 🔴 **`Les Clos`**（1 対 1。下位 lieudit を持たない） |
| `Grenouilles` | `Les Grenouilles` |
| `Preuses` | `Les Preuses` |
| `Valmur` | `Côte de Valmur` / `Envers de Valmur` |
| `Vaudésir` | `Envers des Vaudésirs` / `Les Vaudésirs` |

🔴 **`Les Clos` は NOM DE CLIMAT と LIEUDIT が完全に同一で、下位区画を持たない。**
**すなわち OBP 行 4 の `'Les Clos,' Chablis Grand Cru` は、法定名と完全一致する。**

### 🏛 格下げ（declassification）の法的経路 —— **行 1 の解釈に効く**

🔴 🏛 **両 cahier des charges の IV 節 2° c) が同一の規定を置いている ——
「`Chablis Grand Cru` の画定区画のブドウから造られたワインは、
`Chablis` に `premier cru` の表示を付した（ただし climat 名は付さない）appellation を名乗ることもできる」。**
🔴 **すなわち Grand Cru → 「Chablis Premier Cru（climat 名なし）」への格下げが法的に用意されている。**
🔍 **同様に premier cru の果実を村名 `Chablis` として申告することも一般に妨げられない。**
🔴 **したがって「村名 Chablis の中身は村名区画のみである」と断定してはならない。** → §Important Cuvées 行 1

### 🏛 ラベル表示規則（premier cru）

🏛 **原文 ——「premier cru に格付けされた区画由来のワインについて、
`« Chablis »` に `« premier cru »` を付し、さらに climat 名を続ける場合、
その climat 名は `appellation の後ろに置かれ`、
`高さ・幅ともに appellation の文字寸法を超えてはならない`」。**
🔍 **これは配置と文字寸法の規則であって、綴りを定める規則ではない。**
🔴 **INAO が綴りを定めているのは、あくまで IV 節 2° b) の climat 一覧の方である。**

---

## Farming

🔴 **本節は §Location（appellation 法）と並んで、本ドシエで最も硬い部分である。**
**生産者が何も語らない代わりに、認証の側が異例に精密な日付を持っている。**

### 🔴 🏛 有機認証 —— **「転換中」であって「有機」ではない**

🏛 **Agence Bio（`opendata.agencebio.org`、`siret=31757784900019` の exact 照会。`nbTotal: 1`）**

| 🏛 フィールド | 値 |
|---|---|
| `numeroBio` | **`26543`** |
| `raisonSociale` | **`SCEV VINCENT DAUVISSAT`** |
| `siret` | **`31757784900019`** |
| **認証機関** | **`Ecocert France`** |
| **EU 管理番号** | **`FR-BIO-01`** |
| 🔴 `etatCertification` | 🔴 **`ENGAGEE`** |
| 🔴 `datePremierEngagement` | 🔴 **`2021-04-27`** |
| `dateNotification` | `2021-04-27T12:35:45.976Z` |
| `dateSuspension` / `dateArret` | **ともに `null`**（停止も終了もしていない） |
| 🔴 `mixité` | 🔴 **`Non`** —— **有機と慣行の併存なし＝全園が同一の体系にある** |
| `siteWebs` | 🔴 **`Site Officiel` レコード 1 件、`url` は空文字列 `''`** |

🏛 **Ecocert 発行証書（`certificat.ecocert.com`）**

| 🏛 項目 | 値 |
|---|---|
| **被認証者名** | **`Vincent Dauvissat`** |
| **住所** | **`8 rue Emile Zola, 89800 Chablis, France`**（登記と完全一致） |
| **規則** | **`Certification Agriculture biologique Europe (EU) 2018/848`** |
| 🔴 **scope** | 🔴 **`Agriculteur (production végétale)`** —— **栽培のみ。醸造・加工は掲げられていない** |
| **製品カテゴリ** | **`Fruits, noix, légumes et dérivés` / `Surface de biodiversité`** |
| ⚠️ **証書番号・有効期限** | ⚠️ **ウェブ表示上には出ていない**（別途 PDF のダウンロードが要る） → Open Questions 6 |

🔴 **OBP の 2 ヴィンテージとの関係 —— 本節で最も重要な一点**

| OBP ヴィンテージ | 🔴 判定 | 根拠 |
|---|---|---|
| 🔴 **`2019`**（行 1） | 🔴 **有機認証と一切無関係。**engagement の **約 2 年 5 か月前**の収穫 | 🏛 `datePremierEngagement: 2021-04-27` |
| 🔴 **`2021`**（行 2・3・4） | 🔴 **engagement の直後の収穫であり、転換期間の初年度にあたる。認証済ワインではない** | 🏛 同上。engagement は 2021 年 4 月、収穫は同年秋 |

🔴 **したがって OBP 掲載 4 本のいずれについても、「有機（bio / organic）」とフロアで言ってはならない。**
🔴 **`etatCertification: ENGAGEE` は「認証を取得済み」ではなく「有機の体系にコミットしている」状態を指す。**
✅ **言ってよい形は ——「2021 年 4 月に Ecocert に有機の登録をした造り手で、
リストの 2019 と 2021 はその登録の前後にあたるため、有機認証ワインではありません」。**

### 🔴 🏛 他の認証 —— **測った結果**

| 🏛 認証 | 結果 | 証明の質 |
|---|---|---|
| **Ecocert（AB / EU 有機）** | 🔴 **`ENGAGEE`、2021-04-27 から** | 🏛 **exact SIRET 照会 + 証書実物。確定** |
| 🔴 **Demeter（ビオディナミ）** | 🔴 **該当なし** | 🔴 **`demeter.fr` の検索が完全に解決し、`Il semblerait qu'il n'y ait pas de résultats pour cette recherche` を返した。→ proved negative** |
| ⚠️ **Biodyvin（ビオディナミ）** | ⚠️ **未確定** | ⚠️ 🔴 **検索エンドポイントが検索結果ページを返さずトップページ（`<title>Accueil`）に落ちた。JS シェルと同じ扱いとし、proved negative としない** → Open Questions 6 |
| 🏛⚠️ **BIVB 名簿の環境ラベル欄** | **何も記載なし**（`None listed`） | 🏛⚠️ **申告ベースの名簿。更新遅れの可能性があり、単独では proved negative にしない** |
| **HVE / Terra Vitis** | ❓ **未照会** | ❓ |

⚠️ 🔴 **第三者（評論家サイト等）は「2002 年にビオディナミへ転換した」という趣旨の記述を流布している。**
🔒 **これらは方針上の禁止ソースであり、本書は事実として採用しない。**
🔴 **そして 🏛 Demeter は proved negative、🏛 Agence Bio の初回コミットは 2021-04-27 である。**
🔴 **「ビオディナミの造り手です」とフロアで言ってはならない。** → §Staff Notes

### 🏛 appellation が課す栽培規則（**生産者固有ではないが、必ず効いている**）

- 🔴 **品種は `chardonnay B` のみ**（Chablis / Chablis Grand Cru とも）。
  🔴 **したがって OBP 4 本はすべて 100% シャルドネである。これは生産者の選択ではなく法的要件である。**
- **植栽密度は最低 `5,500 本/ha`。**
- 🔴 **灌漑は禁止（`L'irrigation est interdite`）。**
- **収量上限は村名 60（butoir 70）／ 1er cru 58（butoir 68）／ Grand Cru 54（butoir 64）hl/ha。**
- **欠株率の上限は 20%。**
- **垣根仕立て（palissage）が義務で、その維持も義務。**

❓ **公式に無い（したがって本書に無い）**: 所有面積、区画ごとの面積、樹齢、台木、クローン、
仕立ての詳細、カバークロップ、耕起の方針、収穫方法（手摘みか機械か）、収穫日、実収量。

---

## Winemaking

🔴 ⚠️ **生産者による醸造の記述は 1 行も存在しない。**
**公式サイトが無く、`📄` 生産者署名の off-domain 資料も発見できなかった。**
🔒 **輸入元の資料は authorship の理由で棄却した（三人称の marketing 文）。** → §Sources

**したがって本節に書けるのは 🏛 appellation の法的枠だけである。**

| 🏛 規則 | AOC « Chablis » | AOC « Chablis Grand Cru » |
|---|---|---|
| **糖分最低（g/l 果汁）** | **161**（村名）／ **170**（1er cru） | 🔴 **178** |
| **自然アルコール最低** | **10%**（村名）／ **10.5%**（1er cru） | 🔴 **11%** |
| **補糖後の総アルコール上限** | **13%**（村名）／ **13.5%**（1er cru） | ⚠️ 本書未抽出 |
| 🔴 **連続式プレス** | 🔴 **禁止** | ⚠️ 本書未抽出 |
| 🔴 **木片（オークチップ等）の使用** | 🔴 **禁止** | ⚠️ 本書未抽出 |
| **収穫の輸送** | **雨から保護すること（Grand Cru に明文）** | 🏛 **明文あり** |

❓ **一切不明（生産者が公表していない）**: 圧搾の方式と圧力、デブルバージュ、
発酵容器（ステンレス / 木樽 / フードル）の別と比率、酵母（天然か培養か）、
マロラクティック発酵の有無、熟成期間、樽の産地・容量・新樽比率、
澱との接触、清澄・濾過の有無、亜硫酸の量とタイミング、瓶詰め時期、生産本数。

🔴 **これらをフロアで「たぶんこうでしょう」と補ってはならない。**
**Chablis の一般論（「ステンレスで、樽は使わない」等）を、この造り手の説明として語ってはならない。**

---

## Style

🔴 ⚠️ **本節は空である。**

**生産者によるテイスティングノートは、どのワインについても、どのヴィンテージについても存在しない。**
**公式サイトが無いため、`✅` 一次資料はゼロ件である。**
🔒 **評論家・小売・オークション・輸入元の記述は方針上の禁止ソースであり、
それらで本節を埋めることはしていない。**

🔴 **したがって OBP 掲載の 4 本について、造り手由来の味の描写は 1 文字も無い。**

🏛 **言える範囲の唯一の客観的事実 ——
4 本はすべて `chardonnay B` 100% の辛口白であり（appellation の要件）、
村名 → 1er Cru → Grand Cru の順に、法定の最低成熟度が上がり（161 → 170 → 178 g/l）、
法定の最大収量が下がる（60 → 58 → 54 hl/ha）。**
🔍 **これは「凝縮度の階段」を法が用意しているという意味であって、
個々のワインの味を保証するものではない。**

⚠️ **フロアでは「造り手が味について公表しているものは無い」と正直に言い、
自分のテイスティング所見として語ること。** → §Staff Notes

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 4 本。すべて `unresolved`**）

🔍 **4 行すべてに共通する intake evidence（逐語・完全同一）——
`canonical 384 生産者に一致・別名・近似いずれも無し: 'René & Vincent Dauvissat'`。
`producer_state` / `cuvee_state` / `vintage_state` はいずれも `unresolved`、
`confidence 0.0`、`proposed_canonical_producer` は `null`。
セクションは全行 `FRANCE | WHITE > BURGUNDY`。**

| # | OBP 印字 | VT | 価格 | match_state | 🏛 **INAO 照合の結果** |
|---|---|---|---|---|---|
| **1** | **`Chablis`** | **2019** | **$400** | `unresolved` | 🔴 ⚠️ **キュヴェ名が無い。**村名 AOC としては正しい表記だが、**この造り手が村名 Chablis を 1 種類しか瓶詰めしていないかは確認できない。**→ 下記「行 1」 |
| **2** | 🔴 **`'La Forest,' Chablis Premier Cru`** | **2021** | **$700** | `unresolved` | 🔴 **`La Forest` は INAO の climat 一覧に存在しない（`Forest` の出現 0 回）。**→ 下記「行 2」 |
| **3** | **`'Montée de Tonnerre' Chablis Premier Cru`** | **2021** | **$780** | `unresolved` | 🔴 ✅ **INAO の法定 NOM DE CLIMAT と完全一致**（commune `Chablis (Fyé)`）。**アクセント・冠詞・綴りすべて一致。本 4 行で唯一、綴りに問題が無い行** |
| **4** | **`'Les Clos,' Chablis Grand Cru`** | **2021** | **$1,560** | `unresolved` | 🔴 ✅ **INAO の法定 NOM DE CLIMAT と完全一致（冠詞 `Les` を含めて）。**🔴 **冠詞を外してはならない** |

---

### 🔴 行 1 —— **`Chablis` 2019 / $400。候補集合を閉じられないので、名を決めない**

**① 何が確定しているか**
- 🏛⚠️ **BIVB 名簿は、この造り手が `Chablis`（村名）を生産すると申告している。**
  **→ 村名 Chablis を造っていること自体は確からしい。**
- 🏛⚠️ **同名簿は `Petit Chablis` も別項目として掲げている。**
  🔴 **したがってメニューの `Chablis` が `Petit Chablis` の誤記である可能性は、名簿上は否定できない。**
  🔍 ⚠️ **ただしメニューは `Petit Chablis` を別の行として持っておらず、
  価格帯も村名として読むのが自然である。断定はしない。**

**② 何が確定していないか（🔴 ここが本質）**
- 🔴 **この造り手が村名 `Chablis` を「1 種類だけ」瓶詰めしているのか、
  複数のキュヴェ（区画別・樹齢別・容器別など）に分けているのかが、
  いかなる 🏛 一次資料からも確定できない。**
- 🔴 **BIVB 名簿が掲げるのは `AOC の申告`であって `キュヴェの一覧`ではない。**
  **同一 AOC で 2 本瓶詰めしていても、名簿上は `Chablis` の 1 項目にしかならない。**
- 🔴 🏛 **加えて、cahier des charges の IV 節 2° c) により、
  Grand Cru 区画のワインは `Chablis premier cru`（climat 名なし）を名乗れる。
  格下げの経路が法的に存在する以上、村名 `Chablis` の中身を区画から逆算することもできない。**

**③ 🔴 判断 —— Batch 9 の Armand Heitz 先例に従う**
🔴 **候補集合の「天井」だけを言い、キュヴェ名は決めない。**
- ✅ **言える上限**: 「🏛 appellation 側の名簿では、この造り手は
  `Petit Chablis` / `Chablis` / 1er Cru 4 つ / Grand Cru 2 つ / `Irancy` を申告している。
  リストの `Chablis` は、そのうちの村名 AOC にあたる。」
- 🔴 **言えないこと**: 「この造り手の村名 Chablis はこれ 1 本です」
  「この Chablis は◯◯という名前です」「◯◯の区画から来ています」。
- 🔴 **canonical への昇格時、`name` に `Chablis` 以外の何かを補ってはならない。**

**④ 🔴 ルーティング**
🔴 **【実ボトルが要る】この行はオンラインの一次資料では閉じない。**
**在庫の該当ボトルのラベル正面・背面を撮影すれば、キュヴェ名の有無が一度に確定する。** → Open Questions 1

---

### 🔴🔴 行 2 —— **`'La Forest,'` —— 本ドシエ最大の発見**

**① 🏛 INAO は何と書いているか（実測）**

| 綴り | 🏛 Chablis CDC での出現 | 位置づけ |
|---|---|---|
| 🔴 **`Forest`（英語綴り）** | 🔴 **`0 回`**（大文字小文字を問わず。Grand Cru CDC でも `0 回`） | 🔴 **法定名として存在しない** |
| **`Forêts`** | **NOM DE CLIMAT として掲載** | **傘 `Montmains` 配下。lieudit は `Les Forêts`** |
| **`Les Forêts`** | **NOM DE CLIMAT として掲載** | **同上** |
| ⚠️ **`La Forêt`（単数・冠詞あり）** | **NOM DE CLIMAT として掲載** | 🔴 ⚠️ **傘は `Montmains` ではなく `Vau Ligneau`。別の climat である** |
| ⚠️ **`Sur la Forêt`** | **NOM DE CLIMAT として掲載** | 🔴 ⚠️ **同じく `Vau Ligneau` 配下** |

**② 🏛⚠️ appellation 側の名簿は何と書いているか**
🏛⚠️ **BIVB は `Chablis 1er Cru - Forêt`（単数・冠詞なし）と記載している。**
🔴 **これは INAO の法定 4 形（`Forêts` / `Les Forêts` / `La Forêt` / `Sur la Forêt`）の
どれとも一致しない第 5 の形である。**

**③ 🔴 3 つの表記が並存し、どの 2 つも一致しない**

| 出典 | 表記 | レイヤー |
|---|---|---|
| **OBP メニュー** | 🔴 **`La Forest`** | 🔍 |
| **BIVB 名簿** | 🔴 **`Forêt`** | 🏛⚠️ |
| **INAO 法定一覧** | 🔴 **`Forêts` / `Les Forêts`**（Montmains 配下） | 🏛 |

**④ 🔴 なぜ正規化規則で処理してはならないか**
🔴 **`La Forest` は「単数 ＋ 冠詞 `La`」である。**
🔴 **アクセント除去・冠詞正規化・綴り揺れ吸収という素朴な規則を当てると、
`La Forest` → `La Forêt` に着地する。**
🔴 **しかし `La Forêt` は `Vau Ligneau` の climat であり、`Montmains` の `Les Forêts` とは
`別の畑`である。**
🔴 **すなわち正規化規則は、この行を「静かに間違った climat に結び付ける」。**
🔴 **これは Batch 8 の `Les Champs Gains` / `Les Champs gain` と同型 ——
`いかなる正規化規則でも橋渡しできない差は、明示的な alias で解決しなければならない`。**

**⑤ 🔴 推奨する解決（🔴 DO NOT EXECUTE）**
- 🔴 **`La Forest` を、この生産者に限定した明示的 alias として登録する。**
  **正規化規則を書かない。他の生産者に波及させない。**
- 🔴 **alias の宛先（`Forêts` か `Les Forêts` か、あるいは傘の `Montmains` か）は、
  本書では決定しない。**
  ⚠️ **BIVB が `Forêt` と書いていることは `Montmains` 系（`Forêts`）を示唆するが、
  `Vau Ligneau` 系（`La Forêt`）を排除する 🏛 証拠を本書は持っていない。**
- 🔴 **ラベル実物を見るまで宛先を確定させない。** → Open Questions 1

**⑥ Confidence**: 🔴 **「`La Forest` が INAO 法定名でないこと」= High（実測 0 回）**
／ 🔴 **「どの climat を指すか」= Low**

---

### 行 3 —— **`'Montée de Tonnerre'` 2021。問題なし**

🏛 ✅ **INAO の premier cru 一覧に `COMMUNE: Chablis (Fyé)` / `NOM DE CLIMAT: Montée de Tonnerre` /
`LIEUDIT: Montée de Tonnerre` として掲載。メニューの印字と、アクセント・冠詞・語順まで完全一致。**
🏛 **`Montée de Tonnerre` は傘でもあり、`Les Chapelots` / `Pied d'Aloup` / `Sous Pied d'Aloup` /
`Côte de Bréchain` を配下に持つ。**
🔍 **したがって「Montée de Tonnerre」と名乗るワインには、
傘の下の複数 lieudit の果実が含まれうる。⚠️ ただしこの造り手がどうしているかは不明。**
🏛⚠️ **BIVB 名簿も `Chablis 1er Cru - Montée de Tonnerre` と記載しており、INAO と一致する。**
🔴 **本 4 行で唯一、3 つの出典（メニュー・BIVB・INAO）が完全に一致する行である。**

🔴 🔍 **canonical に前例がある** ——
**`raveneau-montee-de-tonnerre-2021`（`Domaine François Raveneau` / `name: "Montée de Tonnerre"` /
`vintage: 2021` / `subregion: Chablis Premier Cru`）。**
🔴 **同じ climat・同じヴィンテージのレコードが、別の生産者の下に既に存在する。**
🔴 **したがってこの行の「不在」は cuvée レベルの gap ではなく、`生産者レベルの gap` である。**
🔴 **昇格時は Raveneau レコードの格納形（`name` に climat 名のみを引用符付きで格納し、
`subregion` に `Chablis Premier Cru` を置く）に揃えるのが、canonical 内で最も整合する。**

---

### 行 4 —— **`'Les Clos,' Chablis Grand Cru` 2021。冠詞を外してはならない**

🏛 ✅ **Chablis Grand Cru の cahier des charges 第 I 章 II 節が列挙する 7 climat のひとつ。
逐語で `« Les Clos »` —— 冠詞込みが法定名である。**
🏛 ✅ **一覧表でも `COMMUNE: Chablis` / `NOM DE CLIMAT: Les Clos` / `LIEUDIT: Les Clos` の 1 対 1 対応。
下位 lieudit を持たない。**
🏛⚠️ **BIVB 名簿も `Chablis Grand Cru - Les Clos` と記載。**
🔴 **メニュー・BIVB・INAO の 3 者が一致する（行 3 と並ぶ 2 つ目の完全一致行）。**

🔴 ⚠️ **冠詞について ——「Chablis の Grand Cru は冠詞を外す」という規則を書いてはならない。**
🏛 **INAO 自身の 7 climat 一覧が内部で不統一である ——
`Les Clos` だけが冠詞を持ち、`Blanchot` `Bougros` `Grenouilles` `Preuses` `Valmur` `Vaudésir`
の 6 つは無冠詞である。**
🔴 **Batch 8 の Meursault（`Les Bouchères` は冠詞あり、`Perrières` は冠詞なし）と同じ性質。**
🔴 **climat 名は「規則」ではなく「一覧」で扱うこと。**

🔍 **canonical に Chablis Grand Cru `Les Clos` のレコードは 0 件。**
⚠️ **`Les Clos` という文字列は canonical に 1 件あるが、
それは `Domaine Le Petit Saint Vincent` の Saumur-Champigny `"Les Clos Lyzières"` であり、
Chablis とは無関係である。**
🔴 **これは `D-2026-08-05-08`（部分一致による偽陽性）の実例そのものである。** → §Canonical Conflict ⑥

---

### 🏛⚠️ appellation 名簿が掲げる生産 AOC（**キュヴェ一覧ではない**）

| 🏛⚠️ BIVB 記載 | 色 | OBP |
|---|---|---|
| **`Petit Chablis`** | 白 | — |
| **`Chablis`** | 白 | ⭐ **行 1（2019）** |
| 🔴 **`Chablis 1er Cru - Forêt`** | 白 | ⭐ **行 2（2021。メニューは `La Forest`）** |
| **`Chablis 1er Cru - Montée de Tonnerre`** | 白 | ⭐ **行 3（2021）** |
| **`Chablis 1er Cru - Sécher`** | 白 | — |
| **`Chablis 1er Cru - Vaillons`** | 白 | — |
| 🔴 **`Chablis Grand Cru - Les Clos`** | 白 | ⭐ **行 4（2021）** |
| **`Chablis Grand Cru - Preuses`** | 白 | — |
| 🔴 **`Irancy`** | 🔴 **赤** | — |

🔴 ⚠️ **この表を「この造り手のワイン一覧」として読んではならない。**
**AOC の申告であり、① 同一 AOC 内の複数キュヴェを区別しない
② 申告と実際の瓶詰めは別物 ③ 名簿の更新時点が不明、という 3 つの限界がある。**
🔴 **とくに `Irancy`（赤）は Chablis と全く別の AOC であり、
「Chablis の造り手が赤も申告している」という事実にとどめること。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① この造り手は何も公表していません。だから「造り手が言っていること」は一つもありません。**
「**Chablis 村の中心、`8 rue Emile Zola` にある小さな家族経営の造り手です。
公式サイトがありません —— 探して無かったのではなく、実際に存在しないことを確認しました。
ドメインは売りに出されているか、別人のものか、そもそも存在しません。
フランスの有機登録簿の『公式サイト』欄も、登録はあるのに URL が空でした。
appellation の名簿にもウェブサイト欄がありません。**
**ですので、醸造の方法も、樽の使い方も、畑の広さも、味の説明も、
`造り手からは一切公表されていません`。私がご説明できるのは、
`フランスの公的な登記と、Chablis の法令に書いてあること`だけです。**
**逆に言えば、そこは非常にはっきりしています。**」

**② リストの `La Forest` という綴りは、法令上の畑の名前ではありません。**
「**Chablis のプルミエ・クリュには、INAO が定めた畑（climat）の正式名の一覧があります。
`La Forest` というこの綴りは、その一覧に `一度も出てきません`。**
**法令が定めているのは `Forêts` または `Les Forêts` という複数形で、
これは `Montmains` という大きな畑の傘の下にあります。**
**Chablis のプルミエ・クリュは、`傘の名前で名乗ってもいいし、その中の個別の畑の名前で名乗ってもいい`
という仕組みになっていて、同じ畑が両方の名前を持てるんです。**
**さらにややこしいことに、`La Forêt` という単数形も法令に実在しますが、
それは `Vau Ligneau` という`別の傘`の下の`別の畑`です。**
**ですので『La Forest は La Forêt のことでしょう』と言ってはいけません。違う畑になってしまいます。**
**appellation 側の名簿はこのワインを `Forêt` と書いていて、これはまた別の綴りです。**
**要するに `3 つの出典が 3 通りの綴りをしていて、どの 2 つも一致していません`。
どれが正しいかは、ボトルの実物を見ないと決められません。**」

**③ 有機認証は 2021 年 4 月からで、リストの 2 本はどちらもその対象外です。**
「**フランスの国家有機登録簿で確認しました。認証機関は Ecocert、
`最初の登録が 2021 年 4 月 27 日`です。状態は『コミット済（ENGAGEE）』。**
**リストの `2019` はその 2 年以上前の収穫、`2021` は登録した年の秋の収穫で、
ブドウの木は転換に 3 年かかりますから、`どちらも有機認証のワインではありません`。**
**それと、Ecocert の証書に書かれている対象は `栽培（production végétale）`であって、
醸造は入っていません。**
**ビオディナミについては、Demeter のディレクトリを検索して `該当なしと確認`しています。**」

### ⚠️ 言ってはいけないこと（**must-not-say。本ドシエは記録が薄いので、この一覧が最も重要**）

🔴 **薄い記録ほどフロアで即興されやすい。以下は全て「言えない」。**

| # | ⚠️ 言ってはいけない | 🔴 なぜ |
|---|---|---|
| **1** | 🔴 **「`La Forest` は `La Forêt` のことです」** | 🔴 **`La Forêt` は `Vau Ligneau` 配下の別 climat。`Les Forêts` は `Montmains` 配下。別の畑になってしまう** |
| **2** | 🔴 **「`La Forest` は正式には `Les Forêts` です」** | 🔴 **そう`推定`はできるが、🏛 で確定していない。BIVB は `Forêt`（単数）と書いている。断定するとラベルと食い違いうる** |
| **3** | 🔴 **「有機栽培の造り手です」／「オーガニックです」** | 🔴 **`etatCertification: ENGAGEE`（コミット済）であって認証取得済ではなく、初回コミットは 2021-04-27。OBP の 2019・2021 はいずれも対象外** |
| **4** | 🔴 **「ビオディナミです」** | 🔴 **🏛 Demeter は proved negative（該当なし）。Biodyvin は未確定。第三者の記述は禁止ソース** |
| **5** | 🔴 **「有機のワインです」（仮に将来認証されても）** | 🔴 **Ecocert 証書の scope は `Agriculteur (production végétale)` ＝ 栽培のみ。醸造は scope に無い** |
| **6** | 🔴 **醸造の説明全般（樽か否か、新樽比率、天然酵母、MLF、熟成期間、澱、濾過、亜硫酸）** | 🔴 **一次資料が 1 行も無い。Chablis の一般論をこの造り手の説明として語らない** |
| **7** | 🔴 **味の描写を「造り手によれば」と付けて語ること** | 🔴 **造り手のテイスティングノートは 1 件も存在しない。自分の所見として語ること** |
| **8** | 🔴 **創業年・世代数・当主の交代時期** | 🔴 **🏛 登記の `1900-01-01` は sentinel、`1979-01-01` は法人設立日。どちらも創業年ではない。第三者の「◯代目」「創業◯年」は禁止ソース由来** |
| **9** | 🔴 **「Vincent さんが今の当主です」** | 🔴 **🏛 登記上、Vincent（1957 年生）は経営体 SCEV の役員ではなく、土地保有体 GFA の Gérant。SCEV の業務執行社員は 1984 年生と 1989 年生の 2 名。ただし登記＝実務とは限らないので、どちらの断定もしない** |
| **10** | 🔴 **「この造り手の村名 Chablis はこの 1 本です」** | 🔴 **BIVB 名簿は AOC の申告であってキュヴェ一覧ではない。複数瓶詰めの可能性を排除できない** |
| **11** | 🔴 **「村名 Chablis は村名の区画から来ています」** | 🔴 🏛 **cahier des charges に格下げの経路が明文である（Grand Cru → premier cru（climat 名なし））。中身を区画から逆算できない** |
| **12** | 🔴 **`Les Clos` を「Clos」と冠詞を外して呼ぶこと／他の Grand Cru に冠詞を足すこと** | 🔴 🏛 **INAO の 7 climat 一覧は内部で不統一。`Les Clos` だけが冠詞付き、他 6 つは無冠詞。一律規則は誤り** |
| **13** | 🔴 **`Dauvissat` を名乗る他の Chablis の蔵の話を混ぜること** | 🔴 **Chablis だけで `Jean et Sébastien` / `Jean Père et Fils` / `Benoît` / `Tribut` / `Michel`（停止）、さらに Beine に `Agnès, Didier et Florent` がある。**⚠️ **`GFR RAVENEAU-DAUVISSAT` は Raveneau 側の法人** |
| **14** | 🔴 **「Dauvissat-Camus という名前でも出しています」** | 🔴 **`Dauvissat - Camus` は 🏛 土地保有 GFA の登記名。ワインのブランド名としては未確認** |
| **15** | 🔴 **「公式サイトはこちらです」と `dauvissat.fr` / `dauvissat.com` / `domaine-dauvissat.fr` を案内すること** | 🔴 **順に、Dovendi の売却ページ／LinkedIn の個人ページ／`Beine` の別蔵。3 件とも生産者ではない** |
| **16** | ⚠️ **畑の面積・樹齢・所有区画** | 🔴 **一次資料が無い。🏛 地籍からも耕作者は分からない** |
| **17** | ⚠️ **「2021 年は◯◯な年でした」とヴィンテージを語ること** | 🔴 **造り手のヴィンテージコメントが存在しない。一般論を造り手の言葉として語らない** |
| **18** | 🔴 **`Sécher` を `Séchet` と綴ること** | 🏛 **INAO 法定綴りも BIVB も `Sécher`。**⚠️ **棄却した輸入元資料は `Séchet` と綴っており、そちらに引きずられないこと** |

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **本節は escalation のみである。`REGISTER.md` には一切触れていない。新しい番号も開いていない。**
🔒 **既存の系（`P-*` / `C-*` / `V-*` / `S-*` / `CAT-*`）が明らかに当てはまる場合はそれを引き、
当てはまらない場合は「未採番の形」として記述する。採番は CTO の判断である。**

### ① 🔴 `La Forest` —— **正規化規則で橋渡しできない綴り差（`C-*` 系）**

1. **ID**: OBP 行 2 `'La Forest,' Chablis Premier Cru` 2021 / $700
2. **なぜ問題か**
   🔴 🏛 **`Forest` は Chablis / Chablis Grand Cru 両 cahier des charges に `0 回`しか出現しない
   （＝一度も出現しない）。法定 climat 名ではない。**
   🔴 **法定の該当形は `Forêts` / `Les Forêts`（傘 `Montmains`）である。**
   🔴 **一方 `La Forêt` / `Sur la Forêt` は実在するが傘 `Vau Ligneau` の別 climat であり、
   `La Forest` は字面としてこちらに近い。**
   🔴 **したがってアクセント除去・冠詞正規化の類の規則を当てると、別の畑に誤着地する。**
3. **証拠**
   - 🏛 **INAO `PNOCDCChablis.pdf`（v2.2 du 16/09/2010）IV 節 2° b) の climat 一覧（実測）**
   - 🏛 **同 PDF の全文走査で `forest` の出現 0 件（大文字小文字無視）**
   - 🏛⚠️ **BIVB 名簿の記載は `Chablis 1er Cru - Forêt`（第 3 の綴り）**
4. **OBP への影響**: **1 行（行 2）。**
5. **推奨する解決（🔴 DO NOT EXECUTE）**
   - 🔴 **この生産者に限定した明示的 alias を置く。正規化規則を書かない。**
   - 🔴 **alias の宛先はラベル実物を見るまで確定させない。**
6. **既存の系**: 🔴 **Batch 8 の `Les Champs Gains` / `Les Champs gain` と同型。
   「いかなる正規化規則でも橋渡しできない差は explicit alias を要する」という同じ形。**
   ⚠️ **ただし本件は「別の実在 climat に誤着地しうる」点でより危険であり、
   同一視してよいかは CTO の判断。**
7. **Confidence**: **「法定名でないこと」= High ／「宛先」= Low**

### ② 🔴 canonical の Chablis Grand Cru 名が INAO 法定 climat 名と食い違う（`C-*` 系）

🔴 **本件の生産者のレコードではないが、`Les Clos` を昇格させる前に必ず効く。**

| 🔍 canonical レコード | canonical の `name` | 🏛 INAO 法定 NOM DE CLIMAT | 判定 |
|---|---|---|---|
| `laroche-blanchots-2019` | 🔴 **`"Les Blanchots"`** | 🔴 **`Blanchot`**（単数・無冠詞） | 🔴 **不一致。**`Les Blanchots` は lieudit ですらない（法定 lieudit は `Côte de Blanchot`） |
| `billaud-simon-preuses-2022` | 🔴 **`"Les Preuses"`** | 🔴 **`Preuses`**（無冠詞） | ⚠️ **不一致だが `Les Preuses` は法定 `LIEUDIT` である。**「climat 名の欄に lieudit を入れている」形 |
| `laroche-fourchaumes-2021` | 🔴 **`"Les Fourchaumes"`** | 🔴 **`Fourchaume`**（単数・無冠詞） | 🔴 **不一致**（複数形＋冠詞） |
| `bessin-tremblay-valmur-2023` | `Chablis Grand Cru Valmur` | `Valmur` | ✅ **climat 名は一致**（格納形は下記③） |

🔴 **すなわち canonical の Chablis 系 4 レコードのうち 3 件が、INAO 法定 climat 名と食い違っている。**
🔴 **Batch 8–10 で確立した「canonical の格納値は生産者公式／規制一次資料と矛盾する（base rate）」の
Chablis における実例。**
**推奨（🔴 DO NOT EXECUTE）: `Les Clos` を昇格させる際は 🏛 INAO 一覧を正とし、
既存 3 件の是正は別タスクとして CTO に上げる。**
**Confidence: High**（🏛 一次資料と canonical の直接照合）

### ③ ⚠️ Chablis レコードの `name` 格納形が 2 通りある（`S-*` 系）

| 形 | レコード | `name` の中身 |
|---|---|---|
| **A: climat 名のみを引用符付きで格納** | `laroche-fourchaumes-2021` / `billaud-simon-mont-de-milieu-2022` / `billaud-simon-preuses-2022` / `laroche-blanchots-2019` / **`raveneau-montee-de-tonnerre-2021`** | **`"Montée de Tonnerre"` のように climat 名だけ**（appellation は `subregion` 側） |
| **B: appellation を含めてインラインで格納** | `drouhin-vaudon-chablis-pc-2022` / `bessin-tremblay-valmur-2023` | **`Chablis Premier Cru Montmains` / `Chablis Grand Cru Valmur`** |

🔴 **同じクラス（Chablis の cru ワイン）に 2 つの非互換な格納形が並存している。**
🔴 **OBP 4 行を昇格させる際、どちらに揃えるかを決めないと 3 つ目の形が生まれる。**
🔍 **形 A が 5 件、形 B が 2 件。かつ行 3 と同一 climat・同一ヴィンテージの前例（Raveneau）が形 A である。**
**推奨（🔴 DO NOT EXECUTE）: 形 A に揃える。**
**⚠️ 未採番の形。`S-*`（スキーマ）に属すると思われるが、採番は CTO の判断。**

### ④ ⚠️ Chablis レコードの `grapes` が半分欠けている（`S-*` 系）

🔍 **`bessin-tremblay-*`（2 件）と `drouhin-vaudon-*`（1 件）は `grapes: ["Chardonnay 100%"]` を持つが、
`laroche-*`（2 件）・`billaud-simon-*`（2 件）・`raveneau-*`（1 件）には `grapes` フィールドが無い。**
🔴 🏛 **Chablis / Chablis Grand Cru の cahier des charges は
`Les vins sont issus exclusivement du cépage chardonnay B` と定めており、
欠けている 4 件は規制一次資料から機械的に復元できる。**
**推奨（🔴 DO NOT EXECUTE）: 復元は可能だが、本件の範囲外。CTO に上げるのみ。**
**⚠️ 未採番の形。**

### ⑤ 🔴 生産者そのものが canonical に不在 —— **gap であって conflict ではない**

🔴 **🔍 実測: `db_wine_canonical.json` 928 レコード / 383 distinct producer。
`Dauvissat` を含む `producer` フィールド = `0 件`。散文中の出現 = `0 件`。**
🔴 **すなわち producer-field ヒット 0 ／ prose-only ヒット 0 の完全な不在。**

🔒 **これは gap である。**
- 🔴 **「レコードが存在するが識別子の綴りが違って一致しない」（＝ unreachable）ではない。**
  **`Dauvissat` という文字列自体が DB のどこにも無いため、綴り違いの候補すら存在しない。**
  **Batch 10 で unreachable を gap と誤認して重複を作りかけた事例とは、状況が異なる。**
- 🔒 **「生産者が存在しない」を表現する register クラスは無く、無理に当てはめるのは誤りである。**
  **Batch 9 の Abreu がこの扱いを確立した。**
- 🔴 **番号を開かない。`REGISTER.md` に触れない。**

⚠️ **canonical 名の候補が 🏛 レジストリ間で分かれている（未採番の形）**
| 出典 | 表記 |
|---|---|
| **OBP 印字** | 🔴 **`René & Vincent Dauvissat`** |
| 🏛 **国家企業登記（経営体）** | **`SCEV VINCENT DAUVISSAT`** |
| 🏛 **Ecocert 証書** | **`Vincent Dauvissat`** |
| 🏛⚠️ **BIVB 名簿** | **`Domaine Dauvissat Vincent`** |
| 🏛 **国家企業登記（土地保有体）** | **`GFA DAUVISSAT - CAMUS`** |
| 🏛 **国家企業登記（個人事業体）** | **`RENE DAUVISSAT`** |

🔴 **`René & Vincent Dauvissat` という結合形は、照会したどの 🏛 レジストリにも現れない。**
🔴 **本書は canonical 名を決定しない。ラベル実物が要る。** → Open Questions 1

### ⑥ ⚠️ `D-2026-08-05-08`（部分一致による偽陽性）の再確認 —— **本件で 3 度発火した**

🔍 **canonical を climat 名で走査した際の producer-field / prose-only の内訳（実測）**

| 走査語 | producer-field | prose-only | 🔴 prose-only の中身 |
|---|---|---|---|
| **`Dauvissat`** | **0** | **0** | — |
| 🔴 **`Forest`** | **0** | **33** | 🔴 **ほぼ全件が英語のテイスティングノートの `forest floor`（下草／腐葉土）。Chablis とは無関係。**加えて Henri Giraud の `Argonne forest`（樽材の産地）が多数 |
| 🔴 **`Forêts`** | **0** | **1** | 🔴 **`Domaine de L'Arlot` の `"Clos des Forêts Saint Georges"` —— `Nuits-Saint-Georges` の 1er Cru。Chablis ではない** |
| 🔴 **`Les Clos`** | **0** | **1** | 🔴 **`Domaine Le Petit Saint Vincent` の Saumur-Champigny `"Les Clos Lyzières"` —— Loire。Chablis Grand Cru ではない** |
| **`Montée de Tonnerre`** | **0** | **1** | ✅ **`raveneau-montee-de-tonnerre-2021`。これは真の一致**（別生産者の同 climat） |
| **`Montmains`** | **0** | **1** | ✅ **`drouhin-vaudon-chablis-pc-2022`。真の一致**（別生産者） |
| **`Vaillons`** | **0** | **0** | — |
| **`Chablis`** | **0** | **19** | ✅ **8 レコード（5 生産者）が実際の Chablis。残りは他産地の散文中の言及** |

🔴 **`Forest` / `Forêts` / `Les Clos` の 3 語すべてで、
`部分一致は当たるが実体は別産地`という偽陽性が出た。**
🔴 **climat 名での canonical 照合は、必ず `producer` フィールドと
`region` / `subregion` を併せて絞ること。文字列だけで判定してはならない。**

---

## Sources

**一次資料 —— 🏛 公的登記・認証機関・INAO 規制文書のみ。**
🔒 **生産者の公式資料は存在しないため `✅` は 1 件も無い。**
🔒 **retailer / critic / auction / blog / Wikipedia / 輸入元は事実の根拠に一切使用していない。**

### 🔴 サイト真正性の事前確認（`D-2026-08-05-09`。**どうやって確かめたか**）

🔴 **本件では「真正な生産者サイト」は 1 件も見つからず、代わりに look-alike を 3 件掴んだ。**

| 判定 | サイト | 確認方法と結果 |
|---|---|---|
| ❌ 🔴 **look-alike（売却ページ）** | **`dauvissat.fr`** | 🔴 **本文が `Dovendi - Domain for sale`。**`<meta description>` は `This domain is available for sale…`。<br>🏛 **AFNIC WHOIS: holder コンタクトは組織 `Nomio24`（`type: ORGANIZATION`）、レジストラ `XNS Registrar B.V.`、登録 `2023-07-23`。**<br>🔴 **DNS の NS は `ns1.dovendi.nl` / `ns2.dovendi.eu` / `ns3.dovendi.eu`。**<br>🔴 **本 Batch の Vilmart で掴んだのと同じ Dovendi の基盤である（同一手口の再犯）。一語も使用していない。** |
| ❌ 🔴 **look-alike（別人）** | **`dauvissat.com`** | 🔴 **`https://www.linkedin.com/in/nicolas-dauvissat` へリダイレクトする個人の LinkedIn プロフィール。**<br>**A レコードは `213.186.33.5`（OVH）、MX は `mail.protonmail.ch`、NS は OVH。**<br>🔴 **生産者とは無関係。一語も使用していない。** |
| ❌ 🔴 **look-alike（同名の別蔵）** | **`domaine-dauvissat.fr`** | 🔴 **実在し中身もあるが、`<meta description>` が
`Le Domaine Dauvissat Agnès, Didier et Florent se situe à Beine…` —— `Beine` 村の別の蔵である。**<br>🔴 **本件（`Chablis` の `8 rue Emile Zola`）とは別法人。一語も使用していない。**<br>🔴 **`D-2026-08-05-08` の典型例。** |
| 🔴 **不在の証明** | **生産者の公式サイト** | 🔴 **上記 3 件に加え、`vincentdauvissat.com` / `vincentdauvissat.fr` / `domaine-dauvissat.com` / `rene-et-vincent-dauvissat.com` / `renedauvissat.fr` / `dauvissat-camus.fr` / `dauvissatchablis.com` / `dauvissat-chablis.fr` の 8 件が DNS で `NXDOMAIN`。**<br>🔴 **🏛 Agence Bio の `siteWebs` は `Site Officiel` レコードが 1 件あるが `url` が空文字列 `''`。**<br>🔴 **🏛⚠️ BIVB 名簿に website 欄が無い。**<br>🔴 **Internet Archive CDX に生産者サイトの痕跡なし。**<br>→ **5 経路すべてが一致して「存在しない」を示す。** |

### 🔴 棄却したソース（**authorship を理由に。内容の当否ではない**）

| 棄却 | ソース | 理由 |
|---|---|---|
| ❌ 🔴 **`IMPORTER_vineyardbrands_dauvissat.html`** | **米国輸入元 `vineyardbrands.com` の生産者ページ** | 🔴 **全文が三人称の marketing 文（`Domaine Vincent Dauvissat is arguably the finest Domaine in Chablis…`）。生産者の署名も一人称も無い。**<br>🔒 **方針により authorship を理由に棄却。キャッシュのみ保持。**<br>⚠️ **同ページは front / back のラベル画像インデックスを持ち、そのキャプションに `La Forest` と `Séchet` の綴りが現れる。**<br>🔴 **これは本書の根拠に用いていない。**行 2 の宛先確定にも用いない。**ラベル実物が要る理由がまさにこれである。** |
| ❌ 🔒 **評論家サイト各種** | `burgundy-report.com` / `falstaff.com` / `insideburgundy.com` ほか | 🔒 **方針上の禁止ソース。取得も引用もしていない。**⚠️ **これらが流布する「創業◯年」「2002 年ビオディナミ転換」「◯代目」は本書に一切採用していない。** |

### 🏛 ［公的登記・認証機関］

| 資料 | 取得した情報 |
|---|---|
| 🏛 🔴 **`recherche-entreprises.api.gouv.fr`（フランス国家企業登記）— `q=dauvissat chablis`** | 🔴 **`Dauvissat` 名の全法人。Chablis だけで 8 法人。**→ §Identity の entity separation 表 |
| 🏛 🔴 **同 — `q=317577849`** | 🔴 **`SCEV VINCENT DAUVISSAT`。SIRET `31757784900019`、設立 `1979-01-01`、NAF `01.21Z`、法定形態 `6597`、状態 `A`、`est_bio: true`、従業員区分 `02`（2023）、siege 活動開始 `2008-01-01`、座標 `47.81159 / 3.79991`。役員 4 名（Etiennette 1989 / Ghislain 1984 が Gérant、Solenne 1985、法人 `SC LE NOYAU`）** |
| 🏛 🔴 **同 — `q=520830076`** | 🔴 **`GFA DAUVISSAT - CAMUS`。設立 `2010-01-30`、法定形態 `6534`、同一住所。Gérant は `DAUVISSAT VINCENT`（1957 年生）。無限責任社員 10 名（Vallé 家・Frocrain 家を含む）** |
| 🏛 **同 — `q=778655506`** | **`RENE DAUVISSAT`。`entrepreneur individuel`、同一住所、状態 `A`、NAF 旧コード `01.1G`、`date_creation` は sentinel `1900-01-01`、`date_debut_activite` `1994-12-25`** |
| 🏛 **同 — `q=988486353`** | **`SC LE NOYAU`。設立 `2025-06-17`、NAF `64.20Z`、同一住所。Gérant `DAUVISSAT ETIENNETTE`（1989）、社員 `DAUVISSAT VINCENT ROBERT`（1957）** |
| 🏛 **同 — `q=31714545600024`** | **`EARL DOMAINE JEAN DAUVISSAT PERE ET FILS`（SIREN `317145456`、11-13 rue de Léchet）。**🔴 **別蔵であることの確認** |
| 🏛 🔴 **`opendata.agencebio.org` — `?siret=31757784900019`** | 🔴 **`nbTotal: 1`。`numeroBio 26543`、`Ecocert France` / `FR-BIO-01`、`etatCertification: ENGAGEE`、`datePremierEngagement: 2021-04-27`、`mixité: Non`、停止・終了とも `null`、`siteWebs` の `url` が空文字列** |
| 🏛 🔴 **同 — `?siret=77865550600013`（`RENE DAUVISSAT`）** | 🔴 **`nbTotal: 0` —— exact SIRET 照会による proved negative。個人事業体は有機登録されていない** |
| 🏛 🔴 **同 — `?siret=52083007600011`（`GFA DAUVISSAT - CAMUS`）** | 🔴 **`nbTotal: 0` —— 同じく proved negative** |
| 🏛⚠️ **同 — `?nom=dauvissat`（名前照会。proved negative には使えない）** | ⚠️ **`nbTotal: 2`。本件（`26543`）と `EARL DOMAINE JEAN DAUVISSAT PERE ET FILS`（`numeroBio 91`、`siteWebs: []`）** |
| 🏛 🔴 **`certificat.ecocert.com/entreprise/6CF06E29-…`** | 🔴 **被認証者 `Vincent Dauvissat`、住所 `8 rue Emile Zola, 89800 Chablis`、規則 `(EU) 2018/848`、scope `Agriculteur (production végétale)`、カテゴリ `Fruits, noix, légumes et dérivés` / `Surface de biodiversité`。**⚠️ **証書番号と有効期限はウェブ表示に出ていない** |
| 🏛 🔴 **`demeter.fr/?s=dauvissat`** | 🔴 **ページが完全に解決し `Il semblerait qu'il n'y ait pas de résultats pour cette recherche` を返した。→ proved negative** |
| ⚠️ **`biodyvin.com/?s=dauvissat`** | ⚠️ 🔴 **検索結果ページではなくトップページ（`<title>Accueil`）が返った。→ proved negative として扱わない** |
| 🏛⚠️ **`bourgogne-wines.com`（BIVB 生産者名簿）** | 🏛⚠️ **`Domaine Dauvissat Vincent` / `8, rue Emile Zola, 89800 CHABLIS` / Tel `03 86 42 11 58` / Fax `03 86 42 85 32` / GPS `47.8114920 / 3.7999985` / 🔴 **website 欄なし** / 生産 AOC 9 件 / 輸出先 6 か国 / 環境ラベル記載なし**<br>⚠️ **申告ベースの業界団体名簿。識別情報のみに使用** |
| ⚠️ **`chablis-wines.com`（Chablis 名簿）** | ⚠️ **個票が展開されず検索インターフェースのみ取得。本書の根拠に用いていない** |
| ❌ 🏛 **AFNIC WHOIS（`dauvissat.fr`）** | 🔴 **holder 組織 `Nomio24`、レジストラ `XNS Registrar B.V.`、登録 `2023-07-23`。→ 売却ドメインであることの裏付け** |

### 🏛 ［規制一次資料 —— INAO cahier des charges］

⚠️ 🔴 **取得した 2 つの PDF はいずれも `Procédure nationale d'opposition`（全国異議申立手続）版であり、
「削除提案の規定は取消線で表示される」と明記されている。**
**数値が 2 つ並ぶ箇所（`153 161` 等）は旧値・新値の順。本書は新値を採った。**
**最終確定版との異同は未検証。** → Open Questions 5

| 資料 | 取得した情報 |
|---|---|
| 🏛 🔴 **`https://extranet.inao.gouv.fr/fichier/PNOCDCChablis.pdf`**<br>（**`Version n° 2.2 du 16/09/2010`、20 頁、545,536 バイト、先頭 `%PDF` を確認**） | 🔴 **premier cru の `COMMUNE / NOM DE CLIMAT / LIEUDIT` 一覧（傘と個別の二重掲載構造）。`Montmains` / `Vaillons` / `Montée de Tonnerre` / `Vau Ligneau` の各ブロック。**🔴 **`forest` の出現 0 件。**<br>**1938-01-13 のデクレによる初認定、1978-01-31 の区画画定、`chardonnay B` 単一品種、5,500 本/ha、灌漑禁止、糖分 161/170 g/l、自然アルコール 10 / 10.5%、収量 60 / 58（butoir 70 / 68）hl/ha、補糖後上限 13 / 13.5%、連続式プレス禁止、木片使用禁止、欠株率 20%、垣根仕立て義務。**<br>**IV 節 2° c)（Grand Cru → premier cru（climat 名なし）への格下げ）、XII 節（climat 名は appellation の後ろ・文字寸法は appellation 以下）** |
| 🏛 🔴 **`https://extranet.inao.gouv.fr/fichier/PNOCDCChablisGrandCru.pdf`**<br>（**`Version n° 2.2 du 16/09/2010`、142,745 バイト、先頭 `%PDF` を確認**） | 🔴 **第 I 章 II 節の 7 climat の逐語列挙 —— `« Blanchot », « Bougros », « Les Clos », « Grenouilles », « Preuses », « Valmur » et « Vaudésir »`（🔴 冠詞を持つのは `Les Clos` のみ）。**<br>🔴 **`NOM DE CLIMAT / LIEUDIT` 一覧（`Les Clos` は 1 対 1、下位 lieudit なし）。**<br>**commune は `Chablis` のみ、`chardonnay B` 単一品種、5,500 本/ha、灌漑禁止、糖分 178 g/l、自然アルコール 11%、収量 54（butoir 64）hl/ha。**🔴 **`forest` の出現 0 件** |

⚠️ 🔴 **INAO ファイル名の罠 —— 本件で 9 候補中 7 件が「HTTP 200 ＋ HTML」を返した**

| 試した URL | 結果 |
|---|---|
| ✅ **`PNOCDCChablis.pdf`** | 🔴 **`%PDF` / 545,536 バイト —— 本物** |
| ✅ **`pnocdcchablis.pdf`**（全小文字） | 🔴 **同一ファイル（`%PDF` / 545,536 バイト）。大文字小文字は無関係だった** |
| ✅ **`PNOCDCChablisGrandCru.pdf`** | 🔴 **`%PDF` / 142,745 バイト —— 本物** |
| ❌ `PNOCDC-Chablis.pdf` | **HTTP 200 だが `<!DO`（HTML）／6,891 バイト** |
| ❌ `CDCChablis.pdf` | **HTTP 200 だが HTML ／6,887 バイト** |
| ❌ `PNOCDC-Chablis-Grand-Cru.pdf` | **HTTP 200 だが HTML ／6,901 バイト** |
| ❌ `PNOCDCChablis-Grand-Cru.pdf` | **HTTP 200 だが HTML ／6,900 バイト** |
| ❌ `pnocdcchablis-grand-cru.pdf` | **HTTP 200 だが HTML ／6,900 バイト** |
| ❌ `PNOCDCChablisGrand-Cru.pdf` | **HTTP 200 だが HTML ／6,899 バイト** |

🔴 **Chablis 系で効いた形は「`PNOCDC` ＋ ハイフン無しの appellation 名」。
Grand Cru は語間のハイフンも空白も入れずに `ChablisGrandCru` と連結する形だけが通った。**
🔴 **HTTP ステータスは判定に使えない。本文先頭が `%PDF` かどうかだけが判定基準である。**

### 🔍 canonical / OBP（**THÉSEUS DB。読み取りのみ・無変更**）

🔴 **`migration/out/export/db_wine_canonical.json` = 928 レコード / 383 distinct producer。**
🔴 **`Dauvissat`: producer-field `0` 件 / prose-only `0` 件 —— 完全な不在（gap）。**
🔍 **canonical に実在する Chablis レコードは 8 件 / 5 生産者 ——
`Bessin-Tremblay`（2）／`Domaine Drouhin-Vaudon`（1）／`Domaine Laroche`（2）／
`Domaine Billaud-Simon`（2）／`Domaine François Raveneau`（1）。**
🔴 **うち `raveneau-montee-de-tonnerre-2021` は OBP 行 3 と同一 climat・同一ヴィンテージである。**
🔍 **OBP 4 行（`FRANCE | WHITE > BURGUNDY`、producer heading `René & Vincent Dauvissat`、
`producer_state` / `cuvee_state` / `vintage_state` すべて `unresolved`、`confidence 0.0`、
`proposed_canonical_producer: null`）。**
🔍 **参照ファイル: `migration/out/export/db_wine_canonical.json`、
`obp_intake_normalized_20260804.json`（オーケストレータ提供の行情報）。いずれも読み取りのみ。**

⚠️ **オーケストレータの記録および intake evidence の文言は `canonical 384 生産者` であるが、
本書が `db_wine_canonical.json` から distinct `producer` を数えると `383` である
（空値 0 件）。**
🔍 **Batch 9 の Abreu ドシエでも同じ 383 / 384 の 1 件差が記録されている。**
**数え方の定義の差と思われる。本件（`Dauvissat` の完全な不在）の結論には影響しない。** → Open Questions 7

### **取得できなかったもの / 存在しなかったもの**

- 🔴 **生産者の公式サイト —— 存在しない（5 経路で実測）。**
- 🔴 **生産者によるテイスティングノート・醸造の記述・沿革・畑の情報 —— 1 件も存在しない。**
- 🔴 **キュヴェの正式な全数と正式表記 —— 一次資料が無い。**
- 🔴 **ラベル上の生産者表記（`René & Vincent Dauvissat` か否か）—— 未確認。**
- ⚠️ **Ecocert 証書の証書番号と有効期限 —— ウェブ表示に出ておらず、PDF 未取得。**
- ⚠️ **Biodyvin 認証の有無 —— 検索が解決せず未確定。**
- ⚠️ **HVE / Terra Vitis —— 未照会。**
- ⚠️ **`Domaine Dauvissat Agnès, Didier et Florent`（Beine）の SIREN —— 未照会**
  （本件と無関係であることの確認には不要と判断）。
- ⚠️ **INAO cahier des charges の最終確定版 —— 取得したのは異議申立手続版のみ。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🏛 **4 つの独立な公的ソース（国家登記・Ecocert・Agence Bio・BIVB）が住所で完全一致。**🔴 **3 法人の分離、役員、設立日、SIREN/SIRET まで確定。**🔴 **同名別法人 11 件を明示的に分離した。**⚠️ **公式表記だけが未確認**（生産者が何も出していないため） |
| **Overview** | ⚠️ **Low-Medium** | 🏛 **登記由来の事実だけで構成。**🔴 **生産者の自己規定が 1 行も無い。**🏛⚠️ **BIVB の AOC 申告 9 件が唯一の「何を造っているか」の手がかりだが、キュヴェ一覧ではない** |
| **History** | 🔴 ⚠️ **Very Low** | 🔴 **公式資料ゼロ。**🏛 **書けたのは登記上の日付 7 件のみで、うち 2 件は sentinel / 事業所レコード日付であり創業年として使えない。**🔒 **第三者の沿革は方針上不採用** |
| 🔴 **Location** | 🔴 **High** | 🏛 **住所・座標が 4 ソース一致。**🔴 **INAO 両 cahier des charges から appellation の法的構造（傘 climat / 個別 climat の二重掲載、Grand Cru 7 climat、格下げ経路、ラベル規則、収量・成熟度）を全面的に取れた。**❓ **ただし畑の所在・面積は完全に不明** |
| 🔴 **Farming** | 🔴 **High**（認証について）／⚠️ **Very Low**（栽培実務について） | 🔴 **認証は exact SIRET 照会と証書実物で日付まで確定 —— `2021-04-27`、`ENGAGEE`、`mixité: Non`、scope は栽培のみ。**🔴 **Demeter は proved negative。**🔴 **OBP 両ヴィンテージが対象外であることを確定できた。**🔴 **一方、実際の栽培作業（耕起・カバークロップ・収穫方法・収量）は一切不明** |
| 🔴 **Winemaking** | 🔴 ⚠️ **Very Low** | 🔴 **生産者由来の記述ゼロ。**🏛 **appellation の法的枠（成熟度・アルコール上限・連続式プレス禁止・木片禁止）のみ。**🔴 **この造り手が実際に何をしているかは 1 行も書けない** |
| 🔴 **Style** | 🔴 ⚠️ **Zero** | 🔴 **本節は実質的に空である。テイスティングノートが 1 件も存在せず、禁止ソース以外に代替が無い。**🔴 **OBP 4 本のいずれについても味の描写は書けない** |
| 🔴 **Important Cuvées** | 🔴 **High**（法定名の照合）／⚠️ **Low**（キュヴェの実体） | 🔴 **OBP 4 行すべてを INAO 一次資料に照合し、行 3・行 4 は完全一致、行 2 は法定名に存在しないことを実測で確定した。**🔴 **行 1 は候補集合を閉じられないことを明示し、名を決めなかった。**⚠️ **キュヴェの全数・正式表記は未確認** |
| **Staff Notes** | 🔴 **High** | 🔴 **芯 3 点は全て 🏛 一次資料に紐づく。**🔴 **must-not-say は 18 項目 —— 記録が薄いぶん、塞ぐべき穴を最大限に列挙した** |
| 🔴 **総合** | 🔴 **Low-Medium — `awaiting material from the team`** | **下記参照** |

🔴 **reached_70: NO（およそ 64%）。**
🔴 **`awaiting material from the team`。**

**満たした必須項目**: Identity ✅ ／ Location ✅ ／ **Farming ✅（認証の日付まで確定）** ／
**Important Cuvées（OBP 4 行すべての法定名照合）✅** ／ Staff Notes 芯 3 点 ✅ ／
⚠️ **must-not-say 18 項目 ✅** ／ `## Sources` ✅ ／ `## Open Questions` ✅

🔴 **満たせなかった必須項目**:
- 🔴 **`## Style` が実質的に空**（生産者のテイスティングノートが存在しない）
- 🔴 **`## Winemaking` に生産者固有の情報がゼロ**
- 🔴 **`## History` がほぼ空**
- 🔴 **`## Overview` が生産者の自己規定を持たない**

🔴 **70% に届かない理由は明快である —— この生産者は何も公表していない。**
**公式サイトが無いことを 5 経路で証明し、輸入元資料は authorship で棄却したため、
`✅` レイヤーの資料が 1 件も存在しない。**
🔴 **ブリーフの指示に従い、🏛 appellation 法と公的登記の側を最大限まで深掘りして補償した ——
INAO 両 cahier des charges の全文走査、climat の傘構造の解明、
同名 11 法人の分離、認証日付の確定。**
🔴 **しかし「ワインそのものについて造り手が何を言っているか」は、
どれだけ登記を掘っても代替できない。**
🔴 **したがって水増しせず、バーの下で出す。**

---

## Open Questions

1. 🔴 📦 **【実ボトルが要る】ラベルの表記そのもの —— 本ドシエで最も価値の高い 1 タスク。**
   **以下は 🏛 レジストリでも INAO 文書でも解決できず、`物理的にボトルを見る`以外に確定手段が無い。**
   - ❓ 🔴 **行 2 の climat 表記は `La Forest` か。ラベルの実際の綴りは何か。**
     **そしてそれは `Montmains` 系（`Forêts` / `Les Forêts`）なのか、
     `Vau Ligneau` 系（`La Forêt`）なのか。**
   - ❓ 🔴 **行 1 の `Chablis` にキュヴェ名が付いているか。付いていないか。**
   - ❓ 🔴 **生産者表記は `René & Vincent Dauvissat` か、`Vincent Dauvissat` か、
     `Dauvissat-Camus` か。**
   - ❓ **行 3・行 4 のラベルが INAO 法定綴りどおりか（`Montée de Tonnerre` / `Les Clos`）。**
   - ❓ **アルコール度数、瓶詰者表記。**
   → 🔴 **フロア・タスク**: **在庫の該当ボトル 4 本のラベル正面と背面を撮影する。**
     **これで §Canonical Conflict ① と ⑤、および行 1 の未解決が一度に片づく。**

2. ⚠️ **`Camus` の由来が不明。**
   🏛 **`GFA DAUVISSAT - CAMUS`（2010 年設立）という土地保有体の名にのみ現れる。**
   ❓ **`Camus` が姻族名なのか、取得した畑の旧所有者名なのか、確認できていない。**
   ⚠️ **GFA の無限責任社員 10 名に `Camus` 姓は 1 人もいない**
   （Dauvissat / Vallé / Frocrain の 3 姓のみ）。
   → **公式資料か、GFA の設立時の登記全文が要る。**

3. ⚠️ **経営体の実務上の当主が誰か確定できない。**
   🏛 **登記上、SCEV の Gérant は `DAUVISSAT ETIENNETTE`（1989 年生）と
   `DAUVISSAT GHISLAIN`（1984 年生）の 2 名で、
   `DAUVISSAT VINCENT`（1957 年生）は GFA の Gérant である。**
   ⚠️ **これは Batch 8 の Roulot と同型だが、登記＝実務とは限らない。**
   🔴 **フロアでは「誰が当主か」を断定しないこと。**

4. 🔴 **行 1（村名 `Chablis` 2019）のキュヴェ候補集合が閉じない。**
   🏛⚠️ **BIVB 名簿は AOC の申告であってキュヴェ一覧ではないため、
   村名 Chablis が 1 種類か複数かを判定できない。**
   🏛 **さらに cahier des charges には格下げの経路が明文であり、中身を区画から逆算もできない。**
   → **Open Questions 1 が解ければ同時に片づく。**

5. ⚠️ **取得した INAO cahier des charges が最終確定版でない。**
   🔴 **2 つとも `Procédure nationale d'opposition` 版（v2.2 du 16/09/2010）で、
   取消線付きの旧値と新値が併記されている。**
   **本書は新値（`Chablis` 161 g/l、`1er cru` 170 g/l、`Grand Cru` 178 g/l 等）を採った。**
   ❓ **最終確定版で数値や climat 一覧が変わっていないかは未検証。**
   🔴 **ただし climat 名の一覧そのものは取消線の対象ではなく、
   `La Forest` が存在しないという本ドシエの中核結論は影響を受けない。**
   → **INAO の確定版 PDF、または EU の e-Ambrosia 登録原簿が要る。**

6. ⚠️ **認証の「不在」の証明が 2 件だけ不完全。**
   🔴 **確定したのは Ecocert（`ENGAGEE`、2021-04-27）と Demeter（proved negative）。**
   ⚠️ **Biodyvin は検索エンドポイントがトップページに落ちたため未確定。**
   ⚠️ **HVE / Terra Vitis は未照会。**
   ⚠️ **Ecocert 証書の証書番号と有効期限は、ウェブ表示に出ておらず PDF を取得していない。**
   → **これらを埋めれば §Farming が完全になる。**

7. ⚠️ **canonical の生産者数が 383（本調査の実測）か 384（intake evidence の文言）か。**
   🔍 **`db_wine_canonical.json` の 928 レコードから distinct な `producer` 値を数えると
   383 件で、空値は 0 件だった。**
   🔍 **Batch 9 の Abreu ドシエでも同じ 1 件差が記録されている。再現性のある差である。**
   **本件（`Dauvissat` の完全な不在）の結論には影響しない。**
   → **数え方の定義を揃える必要がある場合は、`S-*`（スキーマ）の課題として別途扱う。**

8. ⚠️ **`Irancy`（赤）の位置づけが不明。**
   🏛⚠️ **BIVB 名簿はこの造り手が `Irancy`（Yonne の赤 AOC）を申告していると記載する。**
   ❓ **実際に瓶詰めしているか、どのキュヴェ名か、OBP に載る可能性があるかは未確認。**
   ⚠️ **OBP 4 行はすべて白であり、本件の範囲外。記録のみ。**
