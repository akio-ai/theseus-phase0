# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> **reached_70: YES（~88%） / confidence: High**
> 🔍 **canonical に `producer` フィールド一致は 1 件のみ（`giscours-1855`）。ヴィンテージ・レコードは 0 件。**
> 🔍 **928 件全走査で `giscours` 部分文字列は 8 件ヒット。うち 7 件は prose のみの誤検出**（`D-2026-08-05-08` の実例）。
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト `giscours.com`／公式フィッシュ・テクニック（PDF）で確認**（一次資料）
> `🏛` **公的登録**（recherche-entreprises.api.gouv.fr / Agence Bio / INAO CDC / Légifrance / geo.api.gouv.fr / AFNIC whois）
> `📄` Internet Archive 経由の造り手自身の旧ページ ／ `⚠️` **出典間で食い違う／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出 ／ `❓` 未解決
> `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://giscours.com/fr/`（FR 原本）**
> 走査元: **`sitemap_index.xml` → `page-sitemap`（90 URL）＋ `wine-sitemap`（8 URL）＋ `post-sitemap`（34 URL）＋ `product-sitemap`（22 URL）**
> 併用: ✅ **公式フィッシュ・テクニック 6 点（OBP 該当 6 ヴィンテージ全て。全点 `%PDF` 実体・テキストレイヤーあり・FR/EN 併記）**
> 併用: 🏛 **INAO CDC「Margaux」2 版（PNO 2010 / PNO 2022）＋ Légifrance 施行文（décret n° 2009-1137）**
>
> ---
>
> 🔴 **① OBP 6 行は、造り手の 2 本のワインのどちらとも決着しない —— しかも欠陥は「アペラシオン列」ではなく `パイプラインの側` にある。**
> 🔴 **印字されたメニューの銘柄名の列は空である**（生ライン全 6 行が `2020\t\tMargaux\t\t…\t300`）。
> 🔴 **store 層（`research/out/t-01/inventory.json`）はそれを正しく保存している**（`product_name: ""` ／ `classification_text: "Margaux"`）。
> 🔴 **intake 層（`obp_intake_normalized_20260804.json`）もそれを知っている ——`_parts.label` は `null`、`_parts.appellation` は `"margaux"`。パーサは `Margaux` をラベルではなくアペラシオンとして正しく分類した。**
> 🔴 **それでもなお、同じ行が `cuvee_state: "exact"` と `proposed_canonical_cuvee: "Château Giscours"`（`cuvee:chateau-giscours-chateau-giscours`）を出力する。**
> 🔴 **すなわち欠陥は「アペラシオンが銘柄名の列に印字された」ことでも「パーサが騙された」ことでもない ——**
> 🔴 **`パーサはキュヴェ名の不在を検出しており、マッチャがそれを無視してキュヴェを提案している`。** → §Important Cuvées・§Canonical Conflict ⑥
> 🔴 **そして `Château Giscours`（グラン・ヴァン）と `La Sirène de Giscours`（セカンド）は `どちらも AOC Margaux` であり、**
> 🔴 **OBP の 6 ヴィンテージ（2010・2011・2017・2018・2019・2020）は `両方のレンジに 6 つとも実在する`。**
> → **アペラシオンでもヴィンテージでも切り分けられない。実物ラベルでしか決着しない。** → §Important Cuvées・§Open Questions 1
>
> 🔴 **② 兄弟ワインが別のアペラシオンにいる —— `Haut-Médoc Giscours` は AOC Margaux ではない。**
> ✅ **公式は「troisième vin」「1992 年創出」「appellation Haut-Médoc（60 ha）」と明記する。**
> 🔴 **メニューの列構造は「同一ブランドで AOC が分岐する」ことを表現できないが、**
> 🔴 **本件に限っては `Margaux` という文字列がその 3 本目を`正しく除外している`。この列は今回は効いている。**
>
> 🔴 **③ シャトーはマルゴー村ではなく `ラバルド村（Labarde）` にある。canonical の `subregion: Margaux` はアペラシオン名であって村名ではない。**
> 🏛 **登記上の本店 `10 ROUTE DE GISCOURS 33460 LABARDE`／INSEE コミューン `33211 Labarde`（人口 623）。**
> 🔴 🏛 **AOC Margaux の現行の地理的領域は `4 コミューン` —— `Arsac, Labarde, Margaux-Cantenac, Soussans`（統合版 CDC、2023-03-31 homologué／2023-04-05 JORF）。**
> 🔴 **本ドシエ初版は「5 コミューン」と書いたが、それは `PNO の取り消し線が pdftotext で生き残った抽出アーティファクト` だった。訂正済み。**
> 🔴 **`Cantenac` は 2017 年に `Margaux-Cantenac` へ合併して消滅している（🏛 `33268` の `anciensCodes: ["33091"]`／旧コード `33091` は HTTP 404）。**
> 🔴 **`Labarde` はどの版（1954／2009／2022 案／2023 現行）にも入っており、本ドシエの Labarde 判定は揺るがない。** → §Location
>
> 🔴 **④ 農法 —— 造り手は「畑の半分は有機農法」と自ら書き、公的登録は栽培法人について「有機登録なし」を返す。両立するが、混ぜると即座に嘘になる。**
> 🏛 **Agence Bio、栽培法人 SIRET `47220071600034` 完全一致 → `{"nbTotal":0,"items":[]}`（有効な陰性）。**
> 🔴 🏛 **一方で同一住所の `AJ DOMAINES`（SIRET `32052803700056`）は `numeroBio 10839` を持つ。**
> 🔴 **だがその scope は `Distribution / Grossistes`、`商業` カテゴリ（酒類卸・食用油脂卸）であり、`Production`（栽培）ではない。**
> 🔴 **状態は `ENGAGEE`、`datePremierEngagement 2020-02-25`。OBP の 6 本中 5 本はこの日付より前の収穫である。** → §Farming
>
> 🔴 **⑤ canonical の `giscours-1855` は、typed field を含めて造り手・公的登録と広範に食い違う。**
> **`94 ha` ⟷ ✅ 公式フィッシュ全 6 点が `95 ha en production`／**
> **`CS 60% / Merlot 32% / CF 5% / PV 3%` ⟷ ✅ 公式の実ヴィンテージ 6 つのどれとも一致せず、`6 つとも Cabernet Franc を含まない`／**
> **`発酵 18〜28 日` ⟷ ✅ 全 6 点が `Macération 35 jours à 28°C`／**
> 🔴 **`シャトー・テルトルも所有` ⟷ ✅ 公式 AJ Domaines ページは所有を `Giscours（Bordeaux）と Caiarossa（Toscane）` の 2 つと明記し、**
> 🔴 🏛 **du Tertre の現行操業法人（SIREN 894341353）の gérant は `HELFRICH Joseph`、社員は `LES GRANDS CHAIS DE FRANCE` と `TERRES BORDELAISES`。**
> → **公式・公的登録の両方から反証された。** → §Canonical Conflict
>
> 🔴 **⑥ 2000 年代半ばの規制・司法問題について。**
> ⚠️ **Légifrance 判例検索（`Giscours`、15 件）・Cour de cassation・造り手自身のサイト全走査のいずれからも、**
> ⚠️ **`醸造実務に関する 2000 年代半ばの公式記録は 1 件も見つからなかった`。**
> 🔴 **したがって本件は「広く流布した第三者言説であり、公式出典を特定できなかったもの」として扱い、`言ってはいけないことリスト`に置く。**
> **本ドシエはその内容を一切記述しない。** → §Staff Notes ⚠️ ①・§Open Questions 6
>
> ⚠️ **調査上の制約**
> **① 公式サイトの `<title>` は FR/EN とも `Grand Cru Classé en 1885` と誤記している（正しくは 1855）。**
>    **本文・沿革ページは `1855`／`3ème Grand Cru Classé` と正しい。造り手側のタイポである。** → §Identity
> **② INAO CDC は `§2c` の罠が実際に発生した。`3-CDC-Margaux.pdf` も `PNOCDCMargaux.pdf` も `どちらも PNO（異議申立手続）案`であり、**
>    **ファイル名から consolidated 版を見分けることはできなかった。数値は Légifrance 施行文と突き合わせた。**
> **③ `chateau-giscours.fr` は実在し、しかも `保有者は蔵自身`だが、内容を 1 バイトも配信していない。** → §Sources

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`Giscours`**（`producer_or_brand`。`product_name` は**空文字**） |
| **公式表記** | ✅ **`Château Giscours`**（全フィッシュ・テクニックの見出し／`/nos-vins`／沿革ページ）<br>✅ **短縮形 `Giscours` を造り手自身が多用する**（`les vins de Giscours`・`AJ Domaines` ページ） |
| **サイトのタイトル** | ⚠️ 🔴 **`Bienvenue à Giscours - Château Giscours Grand Cru Classé en 1885`**（FR）／**`… in 1885`**（EN）<br>🔴 **`1885` は誤記。本文・沿革は一貫して `1855`。** |
| 🔴 **法人（🏛 公的登録）** | 🏛 **SIREN `472200716`／`nom_complet: CHATEAU GISCOURS`／`nature_juridique 5710`（SAS）**<br>🏛 **本店 SIRET `47220071600034`／NAF `01.21Z`（ブドウ栽培）／`date_creation 1972-01-01`／`etat_administratif: A`**<br>🏛 **TVA `FR95472200716`／`nombre_etablissements 3`（開設中 2）／`tranche_effectif_salarie 21`（2023）**<br>🏛 **2024 年会計: `ca 17 082 903 €`／`resultat_net 1 752 732 €`** |
| 🔴 **法人（公式 mentions légales）** | ✅ **`Château Giscours / 10 route de Giscours / 33460 LABARDE`**（個人データ処理責任者として記載）<br>⚠️ **同じページの別行は `Château Giscours 10 route de Giscours ◆ Labarde ◆ 33460 MARGAUX` と書く。**<br>🔴 **公式サイト内で `33460 LABARDE` と `33460 MARGAUX` が同居している。**郵便番号 33460 は両コミューンに割り当てられており、どちらも郵便上は成立する。**登記上の commune は `LABARDE`（INSEE 33211）。** |
| 🔴 **住所（🏛 登録）** | 🏛 **`CHATEAU GISCOURS 10 ROUTE DE GISCOURS 33460 LABARDE`／`commune 33211`／`lat 45.00889, long -0.64563`**<br>🔴 **公式の mentions légales と登記の街路・番地が完全一致（真正性チェック合格）** |
| **電話 / メール** | ✅ **`+33 (0)5 57 97 09 09` / `contact@giscours.com`** |
| **サイトのホスティング** | ✅ **`SARL Kaizen Agency, 9 rue André Darbon, 33300 Bordeaux`**（mentions légales）／✅ **制作 `The Crowd`**（フッター） |
| 🔴 **親会社 / グループ** | 🏛 **`CHATEAU GISCOURS` の `Président de SAS` は法人 `A J DOMAINES`（SIREN `320528037`）**<br>🏛 **AJ DOMAINES: NAF `46.34Z`（飲料卸）／SAS／本店は同一住所／`date_creation 1970-10-30`／2024 年 `ca 2 115 661 €`**<br>🏛 **AJ DOMAINES の `Président de SAS` は `FONDATION BAENT`（外国法人、SIREN なし）** |
| 🔴 **現在の所有・経営** | 🏛 **AJ DOMAINES の `Directeur Général` 3 名 = `ALBADA JELGERSMA Dennis`（1972）／`Derk`（1974）／`Valérie`（1976）**<br>🏛 **`Directeur général délégué` = `VAN BEEK Alexander`（1971）**<br>✅ **公式チームページの肩書は「Dennis, Derk & Valérie ALBADA JELGERSMA — `Propriétaires du Château Giscours`」。公式と登録が一致する。** |
| 🔴 **創業者（公式の起点）** | ✅ **`Pierre de Lhomme`、1552–1571、「Le Fondateur」「ce riche drapier」**<br>⚠️ **公式沿革は 1552 年より前について何も述べない。** |
| **1855 格付（造り手）** | ✅ **「nommé `troisième Grand Cru Classé` en 1855」**（沿革ページ冒頭）／✅ **年表 1855「Château Giscours devient `3ème Grand Cru Classé`」** |
| 🔴 **1855 格付（🏛 格付団体）** | 🏛 **`Conseil des Grands Crus Classés en 1855 (Médoc & Sauternes)` の公式一覧は「Château GISCOURS ／ `Troisième Cru` ／ Appellation `Margaux`」**<br>🏛 **同団体は SIRET `48484166300012`（SIREN `484841663`、NAF `94.11Z`、association、`1 cours du XXX Juillet 33000 Bordeaux`）。mentions légales と登録が一致（真正性チェック合格）** |
| **有機登録（🏛）** | 🏛 🔴 **栽培法人 `47220071600034` は Agence Bio に登録なし（完全一致クエリで `nbTotal: 0`）。`complements.est_bio: false`／`liste_id_bio: null`** |
| **canonical id** | 🔍 **1 件のみ**（`giscours-1855`。`vintage: "—"`。下記 §Canonical Conflict） |

### ⚠️ 同名・近名の別事業者 —— **「Giscours」は蔵名であると同時に街路名である**

🏛 **企業登録を `giscours` で引くと 23 件返る。ラバルド村の `ROUTE DE GISCOURS` は公道であり、そこに住所を持つだけの無関係な事業者が多数含まれる。**

| 🏛 SIREN | 名称 | NAF | 備考 |
|---|---|---|---|
| 🔴 **472200716** | 🔴 **CHATEAU GISCOURS** | **01.21Z** | 🔴 **本ドシエの対象。OBP の `Giscours`** |
| ⚠️ **320528037** | **AJ DOMAINES** | **46.34Z** | **同一住所のグループ卸法人。`est_bio: true` はこちらに付く。**→ §Farming |
| ⚠️ **429716632** | **GFA CHATEAU GISCOURS** | **68.20B** | 🔴 **不動産 GFA。役員に `TARI` 家（Pierre・Guillaume・Louis-Antoine）と `HEETER-TARI Nicole` が残り、`Liquidateur` 資格が付く。1995 年以前の所有者系統の残存法人。ワインの生産主体ではない** |
| ⚠️ **480890177** | **GISCOURS**（Marcq-en-Barœul、ノール県） | **68.20B** | **完全な別事業者。地理も業種も無関係** |
| ⚠️ **511568057** | **SCI GISCOU** | 68.20B | **綴り違いの別事業者（Chalon-sur-Saône）** |
| ⚠️ **385181185** | **ASSOCIATION POLO CLUB DE BORDEAUX** | 92.6C | **住所が `CHATEAU GISCOUS 33460 LABARDE`。同敷地だが別団体** |
| ⚠️ **401984117 / 833360555 / 898512009 / 912904257 / 880042163 ほか** | 個人事業者・SCI 各種 | 各種 | **`n ROUTE DE GISCOURS` に住むだけ。蔵とは無関係** |

🔴 **⚠️ `Château du Tertre`（33460 Arsac）とは厳格に分離すること。**
🏛 **現行操業法人 `LES GRANDS CRUS DU CHATEAU DU TERTRE`（SIREN `894341353`、2021-02-15 設立、NAF 01.21Z）の gérant は `HELFRICH Joseph`、社員は `LES GRANDS CHAIS DE FRANCE`（SIREN 315999201）と `TERRES BORDELAISES`（SIREN 344303516）。**
🏛 **旧法人 `SOC EXPLOIT VITICOLE CHATEAU DU TERTRE`（SIREN 950360271）は `etat_administratif: C`（廃止）。**
→ 🔴 **Giscours グループとの資本関係は、公式・公的登録のいずれにも見当たらない。** → §Canonical Conflict ②

⚠️ **`Margaux` は同時に ①シャトー名（Château Margaux）②コミューン名（現 Margaux-Cantenac）③AOC 名 である。**
**OBP の `Margaux` は ③ である**（`classification_text` 列に入っているため）。**卓上で ① と混同してはならない。** → §Staff Notes ⚠️ ②

---

## Overview

✅ **Château Giscours は、ボルドー・メドックのラバルド村にある AOC Margaux の生産者で、1855 年格付の第 3 級（Troisième Grand Cru Classé）である。**
✅ **公式の起点は 1552 年、毛織物商 Pierre de Lhomme。以後 5 系統の所有者を経て、1995 年からオランダの Albada Jelgersma 家が所有する。**
✅ **2018 年に創業者 Eric Albada Jelgersma が没し、以後は子 3 名（Dennis・Derk・Valérie）が所有者、Alexander van Beek が経営を執る。**

🔴 ✅ **造り手が自らのワインを語るときの中心語は、はっきり 2 つである。**

🔴 ✅ **① `l'éclat aromatique`（芳香の輝き）と `la finesse des tannins`（タンニンの繊細さ）。**
**2019・2020 のフィッシュ、および `/vin/chateau-giscours/` の本文が、同じ 2 語をそのまま反復する。**
「**ミレジムごとに、Château Giscours の見事な独自性 —— 同時に `puissant`（力強く）かつ `charnu`（肉付きよく）—— を保つことに努めつつ、
われわれの心に近い 2 つの観念に取り組む: `l'éclat aromatique` と `la finesse des tannins`。**」

🔴 ✅ **② 抽出を「注入（infusion）」として捉え直したこと。**
「**Au chai, nous avons modifié notre approche d'extraction afin de mettre en valeur la délicatesse des tannins.
La macération est pensée sur la durée, `comme une infusion`, plus que sur l'intensité du travail des cuves.
`Seule la dégustation guide nos choix.`**」

🔴 ✅ **造り手自身がレンジを「家族」として語る。**
「**À Giscours, un vin ne vit pas tout seul. … Voilà pourquoi l'on parle des `vins de Giscours`,
comme d'une famille composée de diverses personnalités, `et appellations`.**」
🔴 **末尾の `et appellations`（そしてアペラシオン）は造り手自身の語である。すなわち「同一ブランドで AOC が分岐する」ことを、造り手は自覚的に売っている。**

🔍 **THÉSEUS における状態は「canonical が生産者を 1 行で知っているが、ボトルを 1 本も持っていない」形。
`giscours-1855` は `vintage: "—"` の格付レコードであり、OBP の 6 行はいずれも受け皿を欠く。
すなわち主たる問題は矛盾ではなく `不在`（vintage gap）である —— ただしその 1 行の中身自体は広範に矛盾している。**

---

## History

✅ **公式沿革ページ（`/decouvrez-giscours/lhistoire/`）は縦スクロールの年表構成。全文が静的 HTML に含まれる。**

| 年 | 出来事 ✅ |
|---|---|
| 🔴 **1552** | 🔴 **`Pierre de Lhomme` —— 「Le Fondateur」。1552 年から 1571 年。**「**ce riche drapier s'appliqua à accroître la surface du vignoble. C'est lui qui initia `la colonisation des terres sauvages par les vignes`.**」 |
| **1825** | **`Marc Promis` —— 「L'inlassable bâtisseur」。1825–1847。「Industriel et négociant, il eut pour ambition de remettre en état le vignoble」** |
| **1847** | **`Jean-Pierre Pescatore et ses héritiers` —— 「Le Financier esthète」。1847–1875。「多くの投資を重ねてワインの質を高め、所有地に強い名声を与えた」** |
| 🔴 **1855** | 🔴 **「Château Giscours devient `3ème Grand Cru Classé`」** |
| **1870** | **11 月 8 日、気球「La Gironde」。「普仏戦争のさなか、ボルドーの 2 人のネゴシアン Gambès と Barry が高度 2500 m で Château Giscours を 2 本試飲し、1 本を『美味しい食事、素晴らしい Château Giscours、召し上がれ！』のメモとともにゴンドラから投下した」。**⚠️ **公式は出典を地方紙 `La Gironde` の記事と明記し、`Anecdote` と自称する** |
| **1875** | **`Edouard Cruse` —— 「Le viticulteur visionnaire」。1875–1890。所有地を全面近代化し、シャトー周囲に公園を造成、模範農場 `Ferme Suzanne` を建設**<br>**同年、造園家 `Eugène Bühler`（ヴェルサイユ王立園芸学校卒）が `Parc de Giscours` を創出** |
| 🔴 **1900** | 🔴 **「Château Giscours のエチケットに `sirène`（人魚）が初めて登場」。**「**今日この人魚はグラン・ヴァン Château Giscours のエチケット上にあり、`セカンドワイン La Sirène de Giscours の名の由来となった`。**」 |
| 🔴 **1952** | 🔴 **`Nicolas Tari et ses héritiers` —— 「L'homme providentiel」。1952–1995。**「**第二次大戦後の Giscours を「立て直し」、`所有地の 300 ヘクタールを再編した`。**」<br>🔴 **canonical はこの所有者系統を完全に欠落させている。** → §Canonical Conflict |
| **1973** | **Ford Blanquefort 工場落成を Giscours で祝賀。Henry Ford II 臨席。Ferme Suzanne に巨大バーベキュー設置（現用）** |
| 🔴 **1992** | 🔴 **`Premier Haut-Médoc Giscours`。「Haut-Médoc の歴史的区画に由来する、Giscours 家 `3 本目のワイン` が登場」** |
| 🔴 **1995** | 🔴 **`Eric Albada Jelgersma` —— 「L'infatigable perfectionniste」。「ワイン愛好家にして美術収集家である彼は、`畑を再構築し、経営用建物を改修した`」**<br>✅ **AJ Domaines ページ:「Eric Albada は当時 `la Société d'Exploitation du Château Giscours` を引き継ぎ、オランダから自らの方法と大胆さを持ち込んだ」** |
| **2011** | **7 月 16 日、Giscours のクリケットチームが Windsor 城で Royal Household Cricket Club と対戦（エリザベス 2 世臨席）** |
| **2012** | **`Conservatoire des Races d'Aquitaine` との協働開始。ボルドー種の牛を Giscours の牧草地に受け入れ** |
| 🔴 **2018** | 🔴 **「Les enfants Albada Jelgersma reprennent les rênes」。**「**Dennis、Derk、Valérie が、`父 Eric Albada Jelgersma の逝去のあと`、Alexander van Beek を経営陣に擁して所有地の手綱を取る。**」 |
| 🔴 **2019** | 🔴 **`Rosé x Giscours` 創出（「Giscours は淡い色調のロゼで刷新し革新する。Cabernet Sauvignon の 1 区画をこのロゼのために年間通じて専用に管理し、`圧搾の一番搾りだけ`を用いる」）**<br>**同年 `Potager de Giscours`（菜園）創出、ランド種の羊 60 頭を受け入れ** |
| **2021** | **第 1 回 `Grand Prix de Giscours`（芝の障害飛越全国大会）。**🔴 **同年「`450e millésime à la propriété`」（所有地における 450 回目のミレジム）** |
| **2022** | **`Atelier Rose La Biche` 落成** |

⚠️ **公式沿革が沈黙している事項**: 1552 年より前の所有史（**canonical が主張する「14 世紀の防御塔」は公式に一切現れない**）／`Guyscoutz` という綴り／フィロキセラ／両大戦／1855 年格付の根拠文書／`La Sirène de Giscours` の初リリース年。 → Open Questions 3

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Bordeaux — Médoc** ✅ |
| 🔴 **Commune（村）** | 🔴 🏛 **`Labarde`。INSEE コード `33211`、郵便番号 `33460`、人口 623（geo.api.gouv.fr）。**<br>🔴 🏛 **登記本店 `10 ROUTE DE GISCOURS 33460 LABARDE`／`lat 45.00889, long -0.64563`**<br>🔴 **`Margaux` 村ではない。**⚠️ **ただし公式 mentions légales の 1 行は `Labarde ◆ 33460 MARGAUX` と書く（同一ページ内に `33460 LABARDE` も併記）** |
| 🔴 **Appellation** | 🔴 ✅ **`AOC Margaux`（グラン・ヴァンとセカンド）／✅ `AOC Haut-Médoc`（3 本目）**<br>🔴 **canonical の `subregion: "Margaux"` は`アペラシオン名`であって`村名`ではない。** |
| 🔴 **AOC の地理的領域 ①（🏛 現行・in force）** | 🔴 🏛 **統合版 cahier des charges、`2023 年 3 月 31 日 homologué`／`2023 年 4 月 5 日 JORF 公示`:**<br>🔴 **`Arsac, Labarde, Margaux-Cantenac et Soussans` —— `4 コミューン`。**<br>🔴 **これが現行の施行テキストである。**<br>⚠️ **本項は Batch 12 の別エージェントが in-force テキストに当たって確定させたもの（本ドシエは独自取得していない）。** |
| ⚠️ **AOC の地理的領域 ②（🏛 `superseded` — 旧施行文）** | 🏛 ⚠️ **Légifrance / `décret n° 2009-1137 du 18 septembre 2009`（annexe AOC MARGAUX、`LEGIARTI000021063626`）:**<br>「**… sur le territoire des communes suivantes du département de la Gironde : `Arsac, Cantenac, Labarde, Margaux et Soussans`.**」<br>⚠️ **2017 年のコミューン合併より前の綴り。上記 ① に置き換えられている。** |
| ⚠️ **AOC の地理的領域 ③（🏛 `draft` — PNO 案、確定文ではない）** | 🏛 ⚠️ **INAO `3-CDC-Margaux.pdf`（2022 年 9 月 8 日 委員会意見に伴う PNO）:**<br>「**… sur la base du `code officiel géographique en date du 1er janvier 2022` : `Arsac, Cantenac, Labarde, Margaux-Cantenac et Soussans`.**」<br>🔴 **抽出テキストは 5 つ並ぶが、これは `PNO の取り消し線が抽出で生き残った産物` である。下記参照。** |
| 🔴 **なぜ「5 コミューン」と読めてしまうのか（`§2c` の実例）** | 🔴 **PNO（異議申立手続）版の CDC は、削除予定の語を `取り消し線` で残したまま新しい語を併記する。`pdftotext` は取り消し線を落とせないため、`削除される Cantenac` と `新設の Margaux-Cantenac` が同一行に並んで抽出される。**<br>🔴 **すなわち「施行文は 5、PNO は 5」という本ドシエ初版の読みは、`出典間の実際の不一致ではなく抽出アーティファクト`だった。訂正する。**<br>🔴 🏛 **裏づけ（実測）: `geo.api.gouv.fr/communes/33268` は `{"nom":"Margaux-Cantenac","code":"33268","anciensCodes":["33091"]}` を返し、旧 Cantenac コード `33091` への直接照会は `HTTP 404`。**<br>🔴 **`Cantenac というコミューンはもはや存在しない`。したがって現行リストに `Cantenac` と `Margaux-Cantenac` が併存することはありえない。**<br>🔴 **`§2c` はこれまで `40 50 hl`・`115160 hectares` のような`数値の融合`として記録されてきたが、本件は同じ罠が `リスト` に対して発火した実例である。数値に限られた罠ではない。** |
| ⚠️ **AOC の歴史的根拠（🏛 CDC §XI）** | 🏛 **「Le `décret de l'AOC Margaux du 10 août 1954` reconnaît l'aire géographique … aux `cinq communes de Margaux, Cantenac, Soussans, Arsac et Labarde`.」**<br>→ ⚠️ **1954 年時点では確かに 5 コミューンだった（当時 Margaux と Cantenac は別のコミューン）。現行の 4 は、コミューン数の減少であってアペラシオンの縮小ではない。**<br>→ 🔴 **1954 年の原初リストにも、現行リストにも、`Labarde` は入っている。本ドシエの Labarde 判定はどの版でも揺るがない。** |
| 🔴 **aire parcellaire délimitée** | 🏛 **「INAO の当該全国委員会 `2007 年 3 月 16 日` および `2016 年 6 月 8 日` の会期に承認された区画境界。INAO は上記コミューンの各役場に図面を寄託する」**（PNO 2022 版） |
| **aire de proximité immédiate** | 🏛 **醸造・熟成に限る例外区域: `Arcins, Avensan, Lamarque, Ludon-Médoc, Macau, Le Pian-Médoc`**（Légifrance 施行文） |
| 🔴 **AOC の色（🏛）** | 🔴 🏛 **「L'appellation d'origine contrôlée « Margaux » est réservée aux `vins tranquilles rouges`.」**<br>🏛 **「Les vins de l'AOC « Margaux » sont `uniquement des vins tranquilles rouges`.」**<br>→ 🔴 **したがって `Rosé x Giscours` は AOC Margaux ではありえない。** → §Important Cuvées |
| 🔴 **面積（AOC Margaux、公式）** | 🔴 ✅ **`95 ha en production`。**🔴 **OBP 該当 6 ヴィンテージ（2010・2011・2017・2018・2019・2020）の公式フィッシュ 6 点すべてが同一値を記す。**<br>🔴 **canonical の `94ha` と一致しない。** → §Canonical Conflict |
| 🔴 **面積（AOC Haut-Médoc、公式）** | 🔴 ✅ **`nos vignes en appellation Haut-Médoc (`60 ha au total`)`**（`/vin/haut-medoc-giscours/`） |
| ⚠️ **面積（別の官報系数字）** | ⚠️ ✅ **2022 年 3 月 14 日の公式記事は被覆作物について「`Déjà 80 hectares sur les 160` sont concernés」と書く。**<br>🔴 **この `160` が何の総体を指すかを公式は定義していない。95 + 60 = 155 に近いが、`合算してよいとは公式のどこにも書かれていない`。両方を別々に記す。** |
| ⚠️ **所有地総面積** | ⚠️ ✅ **沿革 1952 年の項が「Nicolas Tari … `réorganisa les 300 hectares de la propriété`」と書くのみ。現在の総面積を公式は述べない。** |
| 🔴 **土壌（公式フィッシュ）** | 🔴 ✅ **`Graves d'origine garonnaise profondes`（2010・2011・2019・2020）／`Graves garonnaises profondes`（2017・2018）**<br>✅ EN 版はいずれも `Deep garonnais gravel` |

### 🔴 ✅ 3 つの croupe —— **公式が名指しする唯一の区画構造**

✅ **`/nos-vins/le-terroir-de-giscours/`** —
「**さまざまな地質研究が、われわれのテロワールの高度に質的な起源を明かした ——
`第四紀前期のガロンヌ由来の沖積グラーヴ堆積`が、われわれのブドウ畑の基盤をなしている。
ピレネーから第四紀に運ばれたこれらの痩せ、侵食された土地の上に、
メドックで `croupes graveleuses`（砂利の丘）と呼ばれる起伏が形成された。**」

| croupe | ✅ 公式の記述 |
|---|---|
| 🔴 **Le Grand & Petit Poujeau** | **所有地の西、標高 `21 m`。「ほぼ全面が `peyrosols`。ガロンヌとドルドーニュが運んだ、`大きさで際立つ`美しいグラーヴ。温かい土壌を形成し、Cabernet Sauvignon に特に適し、非常に完成した成熟を可能にする」** |
| 🔴 **Bel Air** | **標高 `12 m`。「`brunisols` の比率が高い（gravelo-sableux 〜 sablo-graveleux）。より冷たいとされるテロワールで、暑く乾いた年を好む」** |
| 🔴 **Le Plateau de Giscours（`Cantelaude`）** | **標高 `17 m`。「前 2 者の巧みな結合。Merlot に肉と深みを、Cabernet Sauvignon には美しい複雑さを与える」** |

✅ **「これらの croupe の上で、われわれのブドウの根系は `十数メートルの深さまで`潜り、乾燥期に必要な水分を地下層から汲む。」**
✅ **「最も古い区画は `1923 年`に植えられた」**（`/nos-vins/de-la-vigne-au-chai/`）
✅ **「われわれの 4 品種 —— Cabernet Sauvignon、Cabernet Franc、Merlot、Petit Verdot」**
✅ **公園と森は `Natura 2000` サイトに指定されている。**

🏛 **参考: AOC Margaux CDC の認可品種は `cabernet franc N, cabernet-sauvignon N, carmenère N, cot N (malbec), merlot N, petit verdot N`（主要品種）＋ 適応目的品種 `castets N`（栽培面積の 5% 以下、協定署名を条件）。植栽密度は `最低 7 000 pieds/ha`、畝間 1.50 m 以下、株間 0.80 m 以上。**
⚠️ **これは AOC の規則であって Giscours の実務ではない。Giscours 自身は植栽密度も仕立ても公表していない。**

❓ **公式に無い**: croupe ごとの ha 内訳、区画名の一覧、平均樹齢、仕立て（canonical の「ドゥーブル・ギュイヨ」は公式に現れない）、収量、標高以外の地質断面。

---

## Farming

🔴 **本節の要点は 1 つ —— 造り手は「畑の半分は有機農法で耕している」と自ら書き、公的登録は「栽培法人に有機登録なし」を返す。**
🔴 **両者は矛盾しない（`実践` と `認証` は別の主張である）。だが混ぜた瞬間に嘘になる。**

### ✅ 造り手自身が書いていること（**実践**）

| 主張 | ✅ 公式の原文と出所 |
|---|---|
| 🔴 **有機農法の面積比** | 🔴 **「`Actuellement, la moitié de la surface du vignoble est cultivée en agriculture biologique.`」**（`/nos-vins/la-philosophie-de-giscours/`＝「Préparer demain」）<br>🔴 **「`Plus de la moitié du vignoble est aujourd'hui conduite selon les méthodes de l'agriculture biologique` ; une part en augmentation chaque année.」**（`/nos-vins/de-la-vigne-au-chai/`）<br>⚠️ **同一サイト内で `la moitié`（半分）と `plus de la moitié`（半分超）が併存する。どちらも 2026-08-06 時点で生きているページである。** |
| 🔴 **除草剤・殺虫剤** | 🔴 **「`Depuis 10 ans, plus aucun herbicides, insecticides et produits nocifs pour la santé des vignerons ne sont utilisés sur ses terres.`」**（2022-03-14 の公式記事。**すなわち記事時点で「10 年来」＝概ね 2012 年以降**）<br>✅ **「À Giscours nous n'utilisons plus de produits herbicides depuis des années. Nous pratiquons un `désherbage mécanique`, que nous cherchons à réduire.」— `Jérôme Poisson, régisseur général du Château Giscours`** |
| **代替防除** | ✅ **`confusion sexuelle`（交信攪乱）を用いる** |
| 🔴 **被覆作物** | 🔴 **「céréales comme l'`avoine` et l'`orge` entre les rangs」「jachère avec `seigle, vesce, trèfle`」「`Déjà 80 hectares sur les 160` sont concernés」「3 つの異なるテロワール、約 `6 ha` で試験中」「3 年計画」** |
| **土壌** | ✅ **「l'entretien des sols par un `labour traditionnel` est redevenu la règle」／「nous raisonnons nos labours pour `préserver la matière organique du sol`」** |
| **剪定** | ✅ **「La taille a été également repensée pour faciliter la circulation de la sève d'année en année, diminuer les `risques de maladie du bois` et améliorer la longévité de la plante.」** |
| 🔴 **植え替え** | 🔴 **`sélection massale`。「70 年以上の古木（クローン選抜以前のもの）を見つけ、識別し、観察し、最も質の高いものを増殖して、この遺伝的資産と栽培の多様性を保つ」— `Didier Forêt, directeur technique`**<br>✅ **古い区画は `complantation`（補植）で維持する** |
| **生物多様性** | ✅ **公園と森は `Natura 2000` サイト。2020 年以降 `約 800 m の生垣`を植栽、`数百の巣箱`を設置。`Conservatoire des Races d'Aquitaine` と協働（ボルドー種の牛・ランド種の羊 60 頭）** |
| **収穫** | ✅ **`vendanges intra parcellaires`。「最も若い株を先に収穫（芳香の輝きと果実味のため）、その後 `複数回の passage` で最も古い株を完熟時に摘む」** |

### 🔴 🏛 認証 —— **登録を SIRET 完全一致で実測した**

| 照会 | 🏛 結果 |
|---|---|
| 🔴 **Agence Bio ／ 栽培法人 SIRET `47220071600034`（CHATEAU GISCOURS、NAF 01.21Z）** | 🔴 **`{"nbTotal":0,"items":[]}`**<br>🔴 **完全に解決するクエリがゼロ件を返した。`D-2026-08-05-08` の要件を満たす `有効な陰性`である。** |
| 🔴 **Agence Bio ／ グループ卸法人 SIRET `32052803700056`（AJ DOMAINES、NAF 46.34Z）** | 🔴 **`nbTotal: 1`。`numeroBio 10839`／`gerant: ALEXANDER VAN BEEK`／住所 `10 ROUTE DE GISCOURS 33460 LABARDE`**<br>🔴 **`categories: [{ "nom": "Grossistes" }]`／`activites: [{ "nom": "Distribution" }]`**<br>🔴 **`productions`: `46.33.13 Commerce de gros d'huiles et de matières grasses comestibles`（AB, 2026）／`46.34.12 Commerce de gros de boissons alcoolisées`（AB, 2026）**<br>🔴 **`certificats`: `FR-BIO-01` / `Ecocert France` / `etatCertification: ENGAGEE` / `dateEngagement: 2020-02-25` / `dateNotification: 2020-04-23` / `dateSuspension: null` / `dateArret: null`**<br>🔴 **`datePremierEngagement: 2020-02-25`** |
| **Agence Bio ／ GFA SIRET `42971663200014`** | **`{"nbTotal":0,"items":[]}`** |
| **企業登録の相互参照** | 🏛 **`CHATEAU GISCOURS`: `est_bio: false`／`liste_id_bio: null`**<br>🏛 **`AJ DOMAINES`: `est_bio: true`／`liste_id_bio: [10839]`** |

### 🔴 したがって、言えること・言えないこと

🔴 **① 「Giscours は有機認証を受けています」は言ってはならない。**
**有機登録を持つのは`卸の法人`（AJ DOMAINES）であって`栽培の法人`（CHATEAU GISCOURS）ではなく、**
**その登録の scope は `Distribution / Grossistes` と `酒類・食用油脂の卸売` であって、`Production`（ブドウ栽培）ではない。**
🔴 **同じ住所・同じ経営者（Alexander van Beek）に付いているため、極めて誤読しやすい。これは本ドシエ最大の落とし穴である。**

🔴 **② 「Giscours は有機農法をしていません」も言ってはならない。**
**造り手自身が「畑の半分（あるいは半分超）は有機農法で耕している」と公式に書いている。**

🔴 **③ 温度的トラップ（`§2e`）。`datePremierEngagement` は `2020-02-25`。**
**OBP の 6 本のうち `2010・2011・2017・2018・2019` の 5 本は、この日付より前に収穫・醸造されている。**
**`2020` のみ収穫（9 月 8 日〜10 月 2 日）がこの日付より後だが、それは`卸法人の認証`であってボトルの認証ではない。**
🔴 **よって 6 本のいずれについても、`bio` を含意する言葉を使ってはならない。**

⚠️ **`HVE`／`Haute Valeur Environnementale`／`Terra Vitis`／`Demeter`／`Biodyvin`／`Ecocert`（蔵自身として）の語は、
取得した公式 HTML 全ページ・全 6 フィッシュのいずれにも一度も現れない。**
🔴 ⚠️ **`biodynamique` の語は公式サイトに 1 回だけ現れるが、それは `Caiarossa`（トスカーナの姉妹蔵、2004 年取得）についての記述である。Giscours についてではない。**
🔴 **AJ Domaines ページを読んだ人がこの語を Giscours に持ち帰る事故が起きうる。** → §Staff Notes ⚠️ ⑤

⚠️ **公式は `Natura 2000` を「公園と森」について述べる。これは`環境保護区の指定`であって`農法の認証`ではない。** → Open Questions 5

---

## Winemaking

### ✅ 公式が記す工程（`/nos-vins/de-la-vigne-au-chai/`）

✅ **「収穫されたブドウは選果され、`éraflés en douceur`（穏やかに除梗）され、`tri optique`（光学選別）で再度選別されて最良のもののみが残る。」**
🔴 ✅ **「`macération pré-fermentaire à froid`（低温の前発酵浸漬）を、`très respectueuse` に行い、アルコール発酵前に果実の香りを昇華させる。」**
🔴 ✅ **「アルコール発酵もまた `plus basse température`（より低温）で、`extraction en douceur semblable à une infusion`（注入に似た穏やかな抽出）で、`à l'abri de l'air`（空気から遮って）行い、果実の新鮮さを守る。」**
🔴 ✅ **「次いで `fermentation malolactique`、これは `réalisée en cuve`（タンクで実施）。」**
✅ **「この段階は定期的な試飲に導かれ、固有のアッサンブラージュの構成に至る。」**
✅ **「ワインは `barriques de chênes français` での熟成で幅と密度を得る。木は `tannins nobles et doux` をもたらし、ごく微量の酸素を通して構造を磨く。」**
✅ **「アッサンブラージュは `dès le printemps`（春の時点で）畑で構想される。」**
✅ **「収穫は `sélection par âge`（樹齢別の選別）で、各区画を `plusieurs fois`（複数回）通る。」**

### 🔴 ✅ 公式フィッシュ・テクニックの全スペック（**OBP 該当 6 点。PDF から機械的に転記。FR 原本を採用**）

| ミレジム | ⭐OBP | SOL | SURFACE | 🔴 **ASSEMBLAGE** | VENDANGES | VINIFICATION | 🔴 **ELEVAGE** |
|---|---|---|---|---|---|---|---|
| 🔴 **2010** | ⭐**$460** | Graves d'origine garonnaise profondes | **95 ha en production** | 🔴 **71 % Cabernet Sauvignon – 29 % Merlot** | **Du 27 septembre au 14 octobre** | Tris manuel et optique／Cuves béton et inox／**Macération 35 jours à 28°C** | Barriques de chêne français／**50% bois neuf**／🔴 **17 mois** |
| 🔴 **2011** | ⭐**$335** | 同上 | **95 ha** | 🔴 **75 % CS – 20 % Merlot – 5 % Petit Verdot** | **Du 8 septembre au 1er octobre** | 同上／**35 jours à 28°C** | **50% bois neuf**／🔴 **17 mois** |
| 🔴 **2017** | ⭐**$300** | Graves garonnaises profondes | **95 ha** | 🔴 **71 % CS ／ 24 % Merlot ／ 5 % petit Verdot** | **Du 15 septembre au 5 octobre** | 同上／**35 jours à 28°C** | **50% bois neuf**／🔴 **17 mois** |
| 🔴 **2018** | ⭐**$335** | Graves garonnaises profondes | **95 ha** | 🔴 **55 % CS ／ 39 % Merlot ／ 6 % petit Verdot** | **Du 12 septembre au 12 octobre** | 同上／**35 jours à 28°C** | **50% bois neuf**／🔴 **17 mois** |
| 🔴 **2019** | ⭐**$280** | Graves d'origine garonnaise profondes | **95 ha** | 🔴 **65 % CS – 35 % Merlot** | **Du 11 septembre au 12 octobre** | 同上／**35 jours à 28°C** | **50% bois neuf**／🔴 **17 mois** |
| 🔴 **2020** | ⭐**$300** | Graves d'origine garonnaise profondes | **95 ha** | 🔴 **56 % CS – 44 % Merlot** | **Du 8 septembre au 2 octobre** | 同上／**35 jours à 28°C** | **50% bois neuf**／🔴 **17 mois** |

🔴 **観察 ① —— OBP の 6 ヴィンテージのうち、`Cabernet Franc を含むものは 1 つも無い`。**
**含まれるのは Cabernet Sauvignon・Merlot・Petit Verdot の 3 品種のみである。**
🔴 **canonical の固定比率 `CS 60% / Merlot 32% / CF 5% / PV 3%` は、この 6 つのどれとも一致しない。** → §Canonical Conflict

🔴 **観察 ② —— Cabernet Sauvignon の比率は 6 年間で `55%〜75%` と大きく振れる。**
**「Giscours は CS 60% です」という固定的な言い方は、6 本のどれについても正確ではない。**

🔴 **観察 ③ —— `Macération 35 jours à 28°C` と `17 mois d'élevage` と `50% bois neuf` は、6 点すべてで完全に一致する。**
**この 3 つは「このヴィンテージ群を通じて安定した造り」として言ってよい。**

### ✅ 醸造責任者の変遷（**フィッシュのクレジット欄から機械的に転記**）

| ミレジム | PRESIDENT | DIRECTEUR GENERAL | DIRECTEUR TECHNIQUE | ŒNOLOGUE CONSEIL |
|---|---|---|---|---|
| **2010** | **Eric Albada Jelgersma** | **Alexander van Beek** | **Didier Forêt** | 🔴 **Denis Dubourdieu** |
| **2011** | **Eric Albada Jelgersma** | Alexander van Beek | Didier Forêt | 🔴 **Denis Dubourdieu** |
| **2017** | ⚠️ **FR 版 `Eric Albada Jelgersma` ／ EN 版 `Albada Jelgersma Family`** | Alexander van Beek | Didier Forêt | 🔴 **Valérie Lavigne – Axel Marchal**（`CONSULTANTS`、複数形） |
| **2018** | **Famille Albada Jelgersma** | Alexander van Beek | Didier Forêt | ⚠️ **記載なし** |
| **2019** | **Famille Albada Jelgersma** | Alexander van Beek | Didier Forêt | 🔴 **Thomas Duclos** |
| **2020** | **Famille Albada Jelgersma** | Alexander van Beek | Didier Forêt | 🔴 **Thomas Duclos** |

🔴 **`Didier Forêt` は 6 点すべてで `Directeur Technique`。この 11 年間、技術責任者は変わっていない。**
⚠️ 🔴 **2017 年フィッシュは、`同一 PDF の中で` FR 欄が `Eric Albada Jelgersma`、EN 欄が `Albada Jelgersma Family` と食い違う。**
**造り手側の内部不一致であり、どちらが正かは公式に書かれていない。両論のまま残す。** → Open Questions 4

✅ **その他の役職（公式チームページ・記事より）**: `Jérôme Poisson`（régisseur général）／`Lionel Aznar`（chef de culture）／`Laure Bastard`（Directrice Commerciale、2002 年 4 月着任）。

⚠️ **アルコール度数、pH、総酸、生産本数、酵母、樽の産地・トヌリエ名、瓶詰め日、収量（hl/ha）は、公式のどこにも記載が無い。** → Open Questions 2

---

## Style

### ✅ 造り手自身のテイスティング言語（**OBP 該当 6 ヴィンテージのフィッシュ本文より。第三者の評言は一切含まない**）

| ミレジム | ✅ 公式の言葉 |
|---|---|
| 🔴 **2010** | 「**2010 は `un millésime de précision`、Giscours で成し遂げられた最も偉大なものの一つ。例外的で満場一致に称えられ、`précis et sensuel`（精密で官能的）。Château Giscours 2010 は `sa délicatesse et sa structure`（繊細さと構造）の両方で印象づける。`puissance と finesse` の、`tannins de grande garde と fraîcheur` の、稀な完全調和の表現である。**」<br>🔴 **「`De la beauté liquide !`（液体の美だ！）」—— 公式は `Denis Dubourdieu` の言葉として引く** |
| 🔴 **2011** | 「**2011 は早い年だった。降水の少ない暖かい春に、非常に日照の多い乾いた夏が続いた。生育期は早まったが、夏の終わりの降雨がブドウを理想的な条件で完熟させた。2011 は Château Giscours に求めるすべての資質を備える —— `un nez frais et vif`（新鮮で生き生きした香り）、`des tannins soyeux`（絹のようなタンニン）、`カベルネに支えられた、力強くも velouté な構造`。`belle énergie` を示し、`fraîcheur と vivacité` を保っている。**」 |
| 🔴 **2017** | 「**Château Giscours 2017 は `vin précis, d'une grande finesse`。2017 年は霜害の年として記憶に残る。しかし `打撃を受けたのは低標高のテロワールのみ`で、偉大なテロワールは無傷だった。完璧な開花、`適度な水分制限`のある日照豊かな夏がブドウに美しい凝縮を与えた。`冷涼で穏やかな収穫期`がタンニンの完全な成熟と香りの充溢をもたらした。醸造所では、霜が生んだ不均質さが、われわれに選別で最大限に厳格であることを強いた。**」 |
| 🔴 **2018** | 「**Château Giscours 2018 はグラン・ヴァンのすべての特徴を備える —— `la puissance, la finesse et la capacité à voyager dans le temps`（時を旅する能力）。このミレジムでは、最終アッサンブラージュにおける `Merlot の特に高い比率` が、`深いグラーヴの土壌に自然に備わる構造とタンニンを包み込む douceur と densité` をワインに与えている。カベルネは極めて好適な晩夏のおかげで完璧な成熟に達し、`vinification douce` を通じて構造・新鮮さ・長期熟成のポテンシャルを前面に出した。**」 |
| 🔴 **2019** | 「**この 2019 で、Château Giscours の `typicité`、その `puissance`、その `charnu` を保ちつつ、心に近い 2 つの観念に取り組んだ: `l'éclat aromatique` と `la finesse des tannins`。メルロはテロワールと収穫日に応じて異なる profil を見せた —— 「`fruit frais, juteux`」で摘まれたものは輝く新鮮さを、完成した成熟で摘まれたものは見事な丸みと極度の gourmandise を。カベルネは `皮の最も完成した成熟を待つため`に収穫日を後ろに倒す決断をした。醸造所では抽出の手法を変え、`浸漬をタンクの作業強度ではなく時間の観念に軸を置いた`。`Seule la dégustation a piloté nos choix`（試飲だけがわれわれの選択を操縦した）。目標はカベルネに `tridimensionnalité`（三次元性）—— 構造・新鮮さ・密度 —— を与えることだった。2019 の Giscours は `tout en précision et en équilibre`、その全き力量を示す。**」 |
| 🔴 **2020** | 「**2020 では 2019 と同じ路線を続け、Château Giscours の typicité を保つことを望んだ。技術チームは `一株ごとに sur-mesure な注意` を払った。われわれの vignerons と vigneronnes は担当する畝とテロワールの精緻な知識を持ち、`これらのブドウの畝を micro-jardins（小さな庭）として`考えている。2020 は誇れるミレジムである。テロワールの鋭い知識とチームの取ったリスクが `un vin voluptueux` を生んだ。`Gourmand`、大きな個性を持つ。Château Giscours の `puissance と charnu` のすべてを備え、`une texture de Taffetas`（タフタの質感）を思わせ、`tannins soyeux` を持つ。**」 |

### ✅ レンジ全体についての造り手の言葉

✅ **Château Giscours（総論）**: 「**`voluptueux`、`gourmand`、AOC Margaux のグラン・ヴァンに固有の強い個性を持つ。`tannins fins et soyeux` によって口中で魅惑的に現れる。`Puissant, envoûtant`、大きな魅力の vin。皺が寄るまでには多くの年月が流れるだろう。**」
✅ **テロワール総論**: 「**マルゴー的性格を語ることは `« une main de fer dans un gant de velours »`（ビロードの手袋の中の鉄の手）を思い描くことだ。**」
🔴 ⚠️ **これは造り手が `Margaux というアペラシオン全体` について述べた比喩であり、`Château Giscours という 1 本` の評ではない。** → §Staff Notes ⚠️ ⑦

⚠️ **点数・受賞・第三者評は公式サイトに掲載が無い（唯一の例外はロゼについての「`« meilleur rosé de Bordeaux »` という評判を既に得ている」という自称）。**

---

## Important Cuvées

### ✅ 公式の現行レンジ（**全 4 品目。`wine-sitemap.xml` の 4 URL と `/nos-vins/` が完全に一致**）

| # | 公式のキュヴェ名 | 位置づけ | 🔴 **アペラシオン** | 公式が持つミレジム一覧 | OBP |
|---|---|---|---|---|---|
| 1 | 🔴 **Château Giscours** | 🔴 **Grand Vin（1855 年 3 級）** | 🔴 ✅ **AOC Margaux** | 🔴 **2000〜2024（25 年連続）** | 🔴 ⭐**6 行の候補 A** |
| 2 | 🔴 **La Sirène de Giscours** | 🔴 **`second vin`（公式の語）** | 🔴 ✅ **AOC Margaux**（「issu de nos vignes en `appellation Margaux`」） | 🔴 **2010〜2021・2023・2024** | 🔴 ⭐**6 行の候補 B** |
| 3 | 🔴 **Haut-Médoc Giscours** | 🔴 **`troisième vin`（公式の語）。1992 年創出** | 🔴 ✅ **AOC Haut-Médoc**（`60 ha au total`） | **2019〜2024** | 🔴 **除外（AOC が違う）** |
| 4 | **Le Rosé x Giscours** | **「Dernier né de la gamme」。2019 年創出** | ⚠️ **公式はアペラシオンを明示しない。**🏛 **AOC Margaux は赤のみなので Margaux ではありえない** | **2021〜2025** | **除外（色・AOC・ヴィンテージのすべてで外れる）** |

🔴 **この 4 品目の外に、公式が現在紹介しているワインは無い。**

---

### 🔴 OBP 掲載分（🔍 THÉSEUS intake `research/out/t-01/inventory.json` より。**全 6 行**）

🔍 **2 つの層の生データ（6 行すべて同型）。層ごとに artifact 名を明示する。**

🔍 **① store 層 —— `/Users/akiomatsumoto/Theseus_Phase0/research/out/t-01/inventory.json`（および `research/store/t-01/shells.json`）**
`document: "beverage_menu_bottles.doc"` / `menu: "WINE"` / `section_path: ["FRANCE | RED", "BORDEAUX"]` / `section_start_page: "17"` /
`producer_heading: "Giscours"` / `producer_or_brand: "Giscours"` / 🔴 **`product_name: ""`** / 🔴 **`classification_text: "Margaux"`** /
`layout: "producer_heading"` / `flags: []` / `unparsed_segment: ""`
→ 🔴 **store 層は「印字された銘柄名が無い」という事実を正しく保存している。**

🔍 **② intake 層 —— `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行。**リポジトリ外**。ブリーフの値と `coverage.py` はこちら由来）**
`source_producer_raw: "Giscours"` / `source_wine_raw: "Margaux"` / `source_vintage_raw: "2010"…"2020"` /
🔴 **`_parts: { "label": null, "appellation": "margaux", "appellation_display": "Margaux", "printed_rest": "Margaux", "varietal": null, "style": null, "rank": null, "parens": [], "flags": [] }`**
🔴 **`normalized_cuvee: "Margaux"` / `proposed_canonical_cuvee: "Château Giscours"` / `proposed_canonical_cuvee_id: "cuvee:chateau-giscours-chateau-giscours"`**
🔴 **`cuvee_state: "exact"` / `vintage_state: "unresolved"`**

🔴 **したがって intake 層は `source_wine_raw` を持つ。**⚠️ **本ドシエの初版は「`source_wine_raw` は存在しない」と書いたが、それは誤りだった。**
**store 層だけを測って intake 層を測らなかったことによる。訂正する。**

🔴 **そして重要なのは、intake 層が `矛盾した 2 つのことを同時に言っている` ことである:**
🔴 **`_parts.label: null`（＝キュヴェ名は印字されていない、とパーサが正しく判定した）**
🔴 **`cuvee_state: "exact"` ＋ `proposed_canonical_cuvee: "Château Giscours"`（＝キュヴェは確定した、とマッチャが宣言した）**

🔴 **さらに `proposed_canonical_cuvee` が返した値は `Margaux`（アペラシオンのエコー）ではなく `Château Giscours`（グラン・ヴァン）である。**
🔴 **すなわちマッチャは、本ドシエが「公式資料からは決められない」と証明したまさにその二択を、`証拠ゼロでグラン・ヴァン側に黙って倒している`。**
🔴 **6 行が `unresolved` と表示されるのは `vintage_state` のせいであって、`cuvee_state` は 6 行とも `exact` である。**
→ ⚠️ **`match_state = exact` が「解決」ではなく「canonical との一致度」しか測っていないというブリーフ §4 の警告の、最も鮮明な実例。**

| # | source_line_no | 生ライン | VT | 価格 | intake | ✅ **公式での照合結果** |
|---|---|---|---|---|---|---|
| 1 | **1026** | `2020\t\tMargaux\t\t…\t300` | **2020** | **$300** | 🔴 `unresolved` | 🔴 ⚠️ **`Château Giscours 2020` と `La Sirène de Giscours 2020` の両方が公式に実在。決着せず** |
| 2 | **1027** | `2019\t\tMargaux\t\t…\t280` | **2019** | **$280** | 🔴 `unresolved` | 🔴 ⚠️ **両方実在。決着せず** |
| 3 | **1028** | `2018\t\tMargaux\t\t…\t335` | **2018** | **$335** | 🔴 `unresolved` | 🔴 ⚠️ **両方実在。決着せず** |
| 4 | **1029** | `2017\t\tMargaux\t\t…\t300` | **2017** | **$300** | 🔴 `unresolved` | 🔴 ⚠️ **両方実在。決着せず** |
| 5 | **1030** | `2011\t\tMargaux\t\t…\t335` | **2011** | **$335** | 🔴 `unresolved` | 🔴 ⚠️ **両方実在。決着せず** |
| 6 | **1031** | `2010\t\tMargaux\t\t…\t460` | **2010** | **$460** | 🔴 `unresolved` | 🔴 ⚠️ **両方実在。決着せず** |

---

### 🔴 6 行すべてに共通する問題 —— **「どのワインか」がメニュー側に書かれていない**

#### 🔴 ① 「アペラシオンが銘柄名の列に入っている」のではない。**銘柄名の列が空である。**

🔴 **store 層の `product_name` は空文字であり、`Margaux` は `classification_text` に入っている。**
🔴 **intake 層の `_parts.label` も `null` であり、`Margaux` は `_parts.appellation` に入っている。**
🔴 **すなわち本行群は「アペラシオンで銘柄名を代用した」形ではなく、`銘柄名がそもそも印字されていない` 形である。**
🔴 **メニューはプロデューサー見出し `Giscours` の下に `ヴィンテージ / 格付 / 価格` の 3 列だけを並べている（`layout: "producer_heading"`）。**
→ ⚠️ **Batch 12 のブリーフはこの列を「wine-name 列にアペラシオンが印字されている」と述べたが、実データは `列が空` である。**
→ 🔴 **ただしブリーフの言う `source_wine_raw` は intake 層に実在する（値は `"Margaux"`）。本ドシエ初版の「存在しない」は誤りで、訂正済み。**
→ 🔴 **そして真の欠陥は列の中身ではなく、`ラベル不在を検出済みのままキュヴェを提案するマッチャ`にある。** → §Canonical Conflict ⑥ 新形 A

#### 🔴 ② そして `Margaux` という 1 語では、グラン・ヴァンとセカンドを切り分けられない。

🔴 ✅ **`Château Giscours` は AOC Margaux である**（「un vin en `appellation Margaux`」）。
🔴 ✅ **`La Sirène de Giscours` も AOC Margaux である**（「Notre second vin, `issu de nos vignes en appellation Margaux`」）。
🔴 ✅ **そして OBP の 6 ヴィンテージ（2010・2011・2017・2018・2019・2020）は、`公式のミレジム一覧上、両方のレンジに 6 つとも存在する`。**

| VT | Château Giscours | La Sirène de Giscours | Haut-Médoc Giscours | Rosé x Giscours |
|---|---|---|---|---|
| **2010** | ✅ 実在 | ✅ 実在 | ✗ | ✗ |
| **2011** | ✅ 実在 | ✅ 実在 | ✗ | ✗ |
| **2017** | ✅ 実在 | ✅ 実在 | ✗ | ✗ |
| **2018** | ✅ 実在 | ✅ 実在 | ✗ | ✗ |
| **2019** | ✅ 実在 | ✅ 実在 | ✅ 実在（**別 AOC**） | ✗ |
| **2020** | ✅ 実在 | ✅ 実在 | ✅ 実在（**別 AOC**） | ✗ |

→ 🔴 **アペラシオンでも、ヴィンテージでも、切り分けは不可能である。**
→ 🔴 **決着させられるのは `実物ラベル` だけである。** → §Open Questions 1

#### 🔴 ③ **それでも本ドシエは「メニューが誤っている」と断定しない。**

⚠️ **① Batch 10 が 3 件、Batch 11 が 1 件の反例を出した通り、`欠陥がメニュー側とは限らない`。**
🔴 **② 本件では `Margaux` という列は `Haut-Médoc Giscours` を正しく除外している。すなわちこの列は機能している。**
**同一ブランドで AOC が分岐する 3 本目を、たった 1 語で正しく落としている。**
⚠️ **③ 店が「Giscours」の下に置いた 6 本が、実際にグラン・ヴァンだけである可能性は十分にある。**
**メニューが `Château Giscours` と書かなかったのは、プロデューサー見出しがすでに `Giscours` だからかもしれない。**
🔴 **しかしそれは`推測`であり、公式資料からは決められない。ゆえに書かない。**

#### 🔴 ④ 参考 —— **La Sirène は同じ年でもスペックが違う。ラベルが無くても、中身を突き合わせれば別物と分かる。**

✅ **公式 `/vin/la-sirene-de-giscours/` の当該 6 ミレジム（OBP と同年）:**

| VT | 🔴 **La Sirène のアッサンブラージュ** | 🔴 **La Sirène の熟成** | （対照）Château Giscours の熟成 |
|---|---|---|---|
| **2010** | **72% CS / 14% Cabernet Franc / 14% Merlot** | **50% bois neuf・`15 mois`** | 50% bois neuf・**17 mois** |
| **2011** | **55% CS / 40% Merlot / 5% Cabernet Franc** | **50% bois neuf・`15 mois`** | 50% bois neuf・**17 mois** |
| **2017** | **55% CS / 25% Merlot / 20% Cabernet Franc** | **50% bois neuf・`17 mois`** | 50% bois neuf・**17 mois** |
| **2018** | **66% CS / 21% Merlot / 13% Cabernet Franc** | 🔴 **`30%` bois neuf・`12 mois`** | 50% bois neuf・**17 mois** |
| **2019** | **70% CS / 12% Merlot / 9% CF / 9% Petit Verdot** | 🔴 **`30%` bois neuf・`12 mois`** | 50% bois neuf・**17 mois** |
| **2020** | **70% CS / 15% Cabernet Franc / 10% Merlot / 5% PV** | 🔴 **`30%` bois neuf・`12 mois`** | 50% bois neuf・**17 mois** |

🔴 **La Sirène は 6 年すべてで `Cabernet Franc を含む`。Château Giscours は 6 年すべてで `含まない`。**
🔴 **これは卓上で使える最も鋭い識別子である。**
🔴 **加えて 2018 年以降、La Sirène は新樽 30%・12 か月に切り替わっており、Château Giscours の 50%・17 か月と明確に分かれる。**
⚠️ **ただし 2010・2011・2017 は新樽比率が両者とも 50% で、熟成月数も 2017 は 17 か月で一致する。この 3 年は樽では切り分けられない。**

---

## Staff Notes

### 🔴 芯 3 点（**これだけ言えば、嘘をつかずに 6 本すべてを語れる**）

🔴 **① 「ラバルド村にある、1855 年格付第 3 級のマルゴー。畑は 95 ヘクタール。」**
**`Labarde` は AOC Margaux を構成する 5 コミューンのひとつで、シャトーは `Margaux 村` ではなくこの村にある（🏛 INSEE 33211）。**
**格付は `Troisième Grand Cru Classé`（🏛 Conseil des Grands Crus Classés en 1855 の公式一覧、および造り手自身の表記）。**
**`95 ha en production` は OBP 該当 6 ヴィンテージの公式フィッシュ 6 点すべてに同一値で書かれている。**

🔴 **② 「造り手が自分で掲げている言葉は 2 つ —— `芳香の輝き`と`タンニンの繊細さ`。抽出は『注入のように』行う。」**
**`l'éclat aromatique` と `la finesse des tannins` は 2019・2020 のフィッシュと商品ページが同じ語で反復する、造り手自身のキーワードである。**
**「`La macération est pensée sur la durée, comme une infusion`」「`Seule la dégustation guide nos choix`」も公式の原文。**
**造りは 6 ヴィンテージを通じて `Macération 35 jours à 28°C` ／ `barriques de chêne français, 50% bois neuf` ／ `17 mois` で一貫している。**

🔴 **③ 「品種構成は年ごとに大きく動く。固定比率で語ってはいけない。」**
**Cabernet Sauvignon は 6 年間で `55%〜75%`。**
🔴 **そして `この 6 ヴィンテージには Cabernet Franc が 1% も入っていない`（CS・Merlot・Petit Verdot のみ）。**
**年別に言える正確な数字は §Winemaking の表にある。年が分かっているなら、その年の数字を読むのが最も安全である。**

### 🔴 ⚠️ 言ってはいけないこと（must-not-say）

⚠️ 🔴 **① 2000 年代半ばの規制・司法問題について、何も言ってはならない。**
**Légifrance の判例検索（`Giscours` で 15 件）、Cour de cassation、造り手自身のサイト全ページを走査したが、**
**`醸造実務に関する 2000 年代半ばの公式記録は 1 件も特定できなかった`（検索でヒットした判例はいずれも 1999〜2003 年の相続・GFA・賃貸借および 2018 年の民事で、主題が異なる）。**
🔴 **本件は「広く流布した第三者言説であり、公式出典を確認できなかったもの」である。**
🔴 **ゲストから問われた場合、`肯定も否定も憶測もしない`。「その件については当店として確認した一次資料がありません」と述べ、話題を造りとヴィンテージに戻すこと。**
🔴 **この価格帯のワインではゲストが持ち出す可能性が現実にある。事前に決めておくべき応答である。**

⚠️ 🔴 **② `Margaux` は 3 つの別物の名前である。**
**①シャトー・マルゴー（Château Margaux、1 級）②コミューン名（現 `Margaux-Cantenac`）③AOC 名。**
**OBP の `Margaux` は ③ である。「マルゴーです」とだけ言うとゲストが ① と受け取る恐れがある。**
**「マルゴーというアペラシオンの、ジスクールというシャトーです」と 2 語で言うこと。**

⚠️ 🔴 **③ 「有機」「ビオ」「ビオディナミ」の語を、この 6 本について使ってはならない。**
🔴 **栽培法人（SIRET 47220071600034）は Agence Bio に登録が無い（完全一致クエリで `nbTotal: 0`）。**
🔴 **有機登録を持つのは同住所の卸法人 `AJ DOMAINES` で、scope は `Distribution / Grossistes`（酒類・食用油脂の卸売）、状態 `ENGAGEE`、`datePremierEngagement 2020-02-25`。**
🔴 **6 本のうち 5 本はこの日付より前の収穫である。**
⚠️ **同時に「有機ではありません」も言ってはならない。造り手自身が「畑の半分（あるいは半分超）は有機農法で耕している」と公式に書いている。**
**安全な言い方は事実の引用のみ ——「造り手は畑の約半分を有機農法で耕していると公表しています。認証については当店で確認していません。」**

⚠️ 🔴 **④ 「HVE」「Terra Vitis」「Demeter」「Biodyvin」を言ってはならない。**
**これらの語は公式サイト全ページ・全 6 フィッシュに一度も現れない。**

⚠️ 🔴 **⑤ 「ビオディナミ」を Giscours に持ち込んではならない。**
🔴 **公式サイトで `biodynamique` が現れるのは `Caiarossa`（トスカーナの姉妹蔵、2004 年取得）についての 1 箇所だけである。**
**AJ Domaines のページを読んだ人が取り違えやすい。Caiarossa と Giscours は別の蔵である。**

⚠️ 🔴 **⑥ 「シャトー・デュ・テルトルも同じオーナーです」と言ってはならない。**
🔴 **公式 AJ Domaines ページは所有を `Giscours（Bordeaux）` と `Caiarossa（Toscane）` の 2 つとのみ記す。**
🔴 **🏛 du Tertre の現行操業法人（SIREN 894341353）の gérant は `HELFRICH Joseph`、社員は `LES GRANDS CHAIS DE FRANCE` と `TERRES BORDELAISES`。**
**canonical にはこの記述が残っているが、公式・公的登録の両方から反証されている。**

⚠️ 🔴 **⑦ 「ビロードの手袋の中の鉄の手」を Giscours の評として言ってはならない。**
**これは造り手が `Margaux というアペラシオン全体` の性格を説明した比喩であり、この 1 本の評ではない。**

⚠️ 🔴 **⑧ 「セカンドは若木から造られます」と言ってはならない。**
**公式は La Sirène について `樹齢` を一言も述べていない。書かれているのは「Château Giscours と同じ哲学で、春から畑で構想される」ことだけである。**

⚠️ 🔴 **⑨ 「Giscours はクラシック・グロウスのロゼの先駆者です」と言ってはならない。**
🔴 **公式は `Rosé x Giscours` を「2019 年に創った」「`Dernier né de la gamme`（レンジの末っ子）」と明記する。先駆者ではなく最新作である。**
**なお `Rosé x Giscours` は AOC Margaux ではありえない（🏛 CDC が Margaux を赤のみに限定）。今回の 6 本とは無関係。**

⚠️ 🔴 **⑩ 「1885 年格付」と言ってはならない。**
🔴 **公式サイトの `<title>` は FR/EN とも `Grand Cru Classé en 1885` と誤記しているが、正しくは `1855` である。造り手側のタイポ。**

⚠️ 🔴 **⑪ 「CS 60%、メルロ 32%、カベルネ・フラン 5%、プティ・ヴェルド 3%」と言ってはならない。**
🔴 **canonical に載っているこの比率は、OBP の 6 ヴィンテージのどれとも一致しない。しかも 6 年すべて Cabernet Franc を含まない。**

⚠️ 🔴 **⑫ 「発酵は 18〜28 日」「収量は 40〜45 hl/ha」「ドゥーブル・ギュイヨ仕立て」と言ってはならない。**
🔴 **1 つ目は公式の `Macération 35 jours à 28°C` と食い違う。2 つ目と 3 つ目は公式のどこにも書かれていない。**

⚠️ 🔴 **⑬ 「14 世紀の防御塔に起源を持ちます」と言ってはならない。**
**公式沿革は 1552 年の Pierre de Lhomme を起点とし、それ以前について一切述べない。**

⚠️ 🔴 **⑭ 6 本のどれについても「これはグラン・ヴァンです」と断言してはならない。**
🔴 **`Château Giscours` と `La Sirène de Giscours` はどちらも AOC Margaux で、6 ヴィンテージすべてが両方に実在する。**
🔴 **メニューには銘柄名が印字されていない（`product_name` が空）。ボトルのラベルを見るまで、どちらかは決まらない。**
**卓上で確認する最速の方法: ラベルに `LA SIRÈNE` の語があるか。無く `CHÂTEAU GISCOURS` だけならグラン・ヴァン。**
**裏ラベルまで見られるなら、`Cabernet Franc` の記載があれば La Sirène 側である（グラン・ヴァンはこの 6 年 CF ゼロ）。**

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

🔍 **走査方法**: `migration/out/export/db_wine_canonical.json`（**928 件**）を全件走査。
**レコード全体を JSON 文字列化して `giscours` を検索 → 8 件ヒット。**

| ヒット種別 | 件数 | 内訳 |
|---|---|---|
| 🔴 **`producer` フィールド一致** | **1** | **`giscours-1855`** |
| 🔴 **prose のみの誤検出（`D-2026-08-05-08` の実例）** | **7** | **`bordeaux-vintage-1967/1970/1972/1976/1978/1979-guide`（6 件。`obp_note` の「ベストワイン」列に `Giscours` の名が出るだけ）＋ `du-tertre-1855`（1 件。`description` に「Château Giscours も所有」と書かれているだけ）** |
| 🔴 **ヴィンテージ・レコード** | **0** | 🔴 **OBP 6 行すべてが `vintage gap`** |

🔴 **すなわち、名前の部分文字列一致は 8 件中 7 件（87.5%）が誤検出だった。`D-2026-08-05-08` はボルドーで実測再現された。**

⚠️ **加えて `du-tertre-1855` は、`Giscours` の名が別レコードの prose に埋まっている例であり、**
🔴 **その prose の内容（所有関係）自体が本ドシエで反証された。誤検出であると同時に誤情報でもある。**

🔍 **canonical 全体の形**: `vintage: "—"`（U+2014）を持つレコードは **328 件**。
**うち `subregion: "Margaux"` かつ `classification` が `1855 Médoc Classification · …` のものは **21 件**（Margaux の 1855 格付シャトー全 21 軒に対応）。**
🔴 **`giscours-1855` はその 1 つであり、`ボトルではなく格付そのもの`を符号化したレコードである。**（ブリーフ §4 の指摘どおりの形。**修正はしていない**）

---

### 🔴 検証結果サマリ

| | 件数 |
|---|---|
| **検証したレコード** | **1**（`giscours-1855`） |
| **検証した項目（フィールドおよび prose 内の個別主張）** | **34** |
| ✅ **公式と一致** | **11** |
| 🔴 **contradicted（公式・公的登録に反証された）** | **8** |
| ⚠️ **unsourced（公式が沈黙、または禁止出典由来）** | **13** |
| 🔴 **absent as key（あるべき記述の欠落）** | **2** |

🔴 **すなわち 34 項目中 23 項目（67.6%）が公式資料に対して失敗した。**
🔴 **ブリーフ §4 の「14 軒中 13 軒で canonical の値が公式に対して失敗した」という base rate は、15 軒目でも崩れなかった。**
🔴 **失敗は prose だけでなく、面積・品種比率・浸漬日数といった `事実上の typed field` にも及んでいる（Batch 10 の所見の再現）。**

---

### 🔴 ① `giscours-1855` —— **面積・品種比率・浸漬日数が公式と食い違う（contradicted）**

| # | canonical の値 | ✅🏛 **公式の値** | 判定 | OBP 影響 |
|---|---|---|---|---|
| **1** | **「`94ha` のマルゴー AOC」** | 🔴 ✅ **`95 ha en production`。OBP 該当 6 ヴィンテージのフィッシュ 6 点すべてが同一値** | 🔴 **contradicted** | **6 本** |
| **2** | **「`CS 60% / Merlot 32% / CF 5% / PV 3%`」** | 🔴 ✅ **2010 `71/29`／2011 `75/20/5PV`／2017 `71/24/5PV`／2018 `55/39/6PV`／2019 `65/35`／2020 `56/44`。**🔴 **6 年すべて Cabernet Franc ゼロ** | 🔴 **contradicted（6/6 で不一致）** | **6 本** |
| **3** | **「発酵：ステンレス＋コンクリートタンク `26〜28℃`、`18〜28 日`」** | 🔴 ✅ **`Cuves béton et inox` は一致。しかし `Macération 35 jours à 28°C`（6 点すべて）** | 🔴 **contradicted（日数）／partial（容器・温度）** | **6 本** |
| **4** | **「1995 年より…エリック・アルバダ・イェルヘルスマ氏が取得し、建物の改修と畑整備を`継続`」** | 🔴 ✅ **公式沿革 2018 年:「`父 Eric Albada Jelgersma の逝去のあと`、Dennis・Derk・Valérie が手綱を取る」**🏛 **AJ DOMAINES の現 DG は子 3 名** | 🔴 **contradicted（stale）** | **6 本** |
| **5** | 🔴 **「シャトー・テルトルも所有」**（`description` / `description_en` / `obp_note` / `obp_note_en` の **4 箇所**） | 🔴 ✅ **AJ Domaines ページ:「AJ Domaines regroupe les propriétés vinicoles de la famille Albada Jelgersma : `Giscours (Bordeaux), et Caiarossa (Toscane)`」**<br>🔴 🏛 **du Tertre 現行法人 SIREN 894341353 の gérant `HELFRICH Joseph`／社員 `LES GRANDS CHAIS DE FRANCE`・`TERRES BORDELAISES`。旧法人 950360271 は `etat C`** | 🔴 **contradicted（公式・登録の両方から）** | **6 本** |
| **6** | **「格付けシャトーとして`ロゼワインを作った先駆者`のひとつ」** | 🔴 ✅ **「2019 年に…創りたいと望んだ」「`Dernier né de la gamme`」** | 🔴 **contradicted（先駆者ではなく最新作）** | **6 本**（卓上の誤り） |
| **7** | **「Rosé（`若木 CS 主体`）」** | 🔴 ✅ **「`une parcelle de Cabernet Sauvignon` を年間通じて専用に管理」「`100% Cabernet Sauvignon`」。`若木` の語は無い** | 🔴 **contradicted（樹齢）／partial（品種は 100% CS で近い）** | **0 本**（レンジ記述） |
| **8** | **`vintage: "—"`（U+2014）** | 🔴 **これはボトルではなく格付を符号化したレコード。造り手は 2000〜2024 の 25 ミレジムを公表している** | 🔴 **empty shell** | **6 本** |

---

### 🔴 ② `giscours-1855` —— **公式が沈黙している、または禁止出典由来（unsourced）**

| # | canonical の値 | ✅ **公式の状態** | 判定 |
|---|---|---|---|
| **9** | **「`14 世紀`に起源を持つ…かつて荒涼とした平原にあった`防御塔`が原点」** | ⚠️ **公式沿革は `1552 年` を起点とし、それ以前に一切言及しない** | ⚠️ **unsourced** |
| **10** | **「`「ジスクーツ（Guyscoutz）」の貴族の館`を購入」** | ⚠️ **`Guyscoutz` の綴りは公式のどこにも現れない**（1552 年・Pierre de Lhomme・毛織物商・植樹は ✅ 一致） | ⚠️ **unsourced（綴りのみ）** |
| **11** | **「`銘酒街道 2 号線`（Route des Châteaux N°2）沿い」** | ⚠️ **公式サイトに記載が無い** | ⚠️ **unsourced** |
| **12** | **「（総面積に含むと`約 300ha`）」** | ⚠️ **公式は沿革 1952 年の項で「Nicolas Tari が `所有地の 300 ha を再編した`」と書くのみ。現在の総面積の言明ではない** | ⚠️ **unsourced（時制・帰属が違う）** |
| **13** | **「`ドゥーブル・ギュイヨ`仕立て」** | ⚠️ **公式に記載が無い（`Guyot` の語は全ページに 0 件）** | ⚠️ **unsourced** |
| **14** | **「収量 `40〜45 hl/ha`」** | ⚠️ **公式に記載が無い** | ⚠️ **unsourced** |
| **15** | **「熟成：フレンチオーク `15〜18 ヶ月`、新樽 50%」** | ⚠️ **新樽 50% は ✅ 一致。月数は 6 点すべて `17 mois` で単一値。**⚠️ **なお公式の 2000〜2002 年の項は `12-15 mois` と書く。canonical の `15〜18` はどちらの実測値とも一致しない範囲である** | ⚠️ **partial／unsourced（月数）** |
| **16** | **「樹齢：`15%＝4〜10 年、50%＝10〜25 年、33%＝25 年以上`」**（obp_note） | ⚠️ **公式に記載が無い。**🔴 **かつ 15+50+33 = `98%` で内部的にも閉じていない** | ⚠️ **unsourced ＋ 内部矛盾** |
| **17** | **「ロバート・パーカーは…2001・2000・1999 を『`ジスクール史上最上の三部作`』と評した」** | 🔴 **第三者批評家。ブリーフ §2-6 により事実出典として使用不可。公式サイトにも掲載が無い** | ⚠️ **unsourced（禁止出典）** |
| **18** | **`drinking_window`「ヴィンテージにより `8〜20 年`の熟成ポテンシャル」** | ⚠️ **公式に数値の記載が無い（「Beaucoup d'années s'écouleront avant qu'il ne prenne une ride」という定性表現のみ）** | ⚠️ **unsourced** |
| **19** | **`serving_temp`「`17–19°C`」** | ⚠️ **公式に記載が無い** | ⚠️ **unsourced** |
| **20** | **`food_pairings`（仔羊・鴨胸肉・和牛・熟成チーズ）** | ⚠️ **公式は料理との相性を一切記さない** | ⚠️ **unsourced** |
| **21** | **`tasting` / `tasting_en`（カシス・スミレ・スパイス…）** | ⚠️ **公式はヴィンテージごとに固有のノートを持つ（§Style 参照）。この総論的記述は公式のどの文とも対応しない** | ⚠️ **unsourced** |

---

### 🔴 ③ `giscours-1855` —— **あるべき記述の欠落（absent as key）**

| # | 欠落 | ✅ **公式の記述** | OBP 影響 |
|---|---|---|---|
| **22** | 🔴 **所有者系統 `Nicolas Tari et ses héritiers`（1952–1995、43 年間）が完全に欠落。canonical は「19 世紀 → 1995 年」と飛ぶ** | ✅ **公式沿革は Tari を「`L'homme providentiel`」と呼び、「第二次大戦後の Giscours を立て直し、`300 ha を再編した`」と記す**<br>🏛 **`GFA CHATEAU GISCOURS`（SIREN 429716632）に `TARI` 姓の役員が現在も 4 名残る** | **0 本**（History のみ） |
| **23** | 🔴 **`Haut-Médoc Giscours` が `AOC Haut-Médoc` という別アペラシオンであることが書かれていない。canonical は「オー・メドック区画」とのみ記す** | ✅ **「nos vignes en `appellation Haut-Médoc` (60 ha au total)」「`troisième vin`」「1992 年創出」** | 🔴 **6 本**（`Margaux` 行の消し込みに直結する情報） |

---

### 🔴 ④ OBP 影響 —— **6 本すべてが `vintage gap`**

🔴 **canonical は Château Giscours について `ヴィンテージ・レコードを 1 件も持たない`。**
🔴 **一方、造り手は `2000〜2024 の 25 ミレジム` を公式に、フィッシュ・テクニック PDF 付きで公表している。**
→ 🔴 **すなわち OBP 6 行が `unresolved` である原因は、メニューでも造り手でもなく、`canonical に受け皿の行が無い` ことである。**
→ ⚠️ **これは `V-*` 族（vintage 軸の破綻）ではない。単に行が無いだけの `vintage gap` である。**

---

### 🔴 ⑤ 登録ファミリーへの証拠追加（**番号は開かない。REGISTER.md は触っていない**）

| 既存 ID | 本ドシエが追加する証拠 |
|---|---|
| 🔴 **`D-2026-08-05-08`（名前の部分文字列一致は危険）** | 🔴 **ボルドーでの実測: `giscours` の全件走査 8 件中 `7 件（87.5%）が誤検出`。うち 6 件は「ヴィンテージ・ガイド」の勧奨銘柄リスト、1 件は `du-tertre-1855` の prose。**🔴 **さらに企業登録側でも `giscours` 23 件中、蔵に関係するのは 3 法人のみで、残りは `ROUTE DE GISCOURS` という`街路名`に住むだけの無関係事業者だった。`名前が同時に街路名でもある` 形は新しい変種である** |
| 🔴 **`S-2`（`vintage: "—"` サーロゲート／マッチングから不可視）** | 🔴 **`vintage: "—"` は canonical 全体で `328 件`（実測再現）。うち `subregion: Margaux` かつ 1855 分類を持つものが `21 件`。**🔴 **`giscours-1855` はその 1 つで、`ボトルではなく格付を符号化`している。造り手は 25 ミレジムを公表しているので、この 1 行では 25 本のいずれとも突合できない** |
| ⚠️ **`C-6`（matcher が節見出しを読んでいない／evidence の同一性）** | ⚠️ **本件では 6 行とも `unresolved` であり evidence 比較の対象にならなかった。追加証拠なし** |
| 🔴 **`P-2` 系（canonical の生産者メタデータが公式と矛盾）** | 🔴 **本件は 34 項目中 `contradicted 8 / unsourced 13 / absent as key 2` = `23 件失敗`。**🔴 **特筆すべきは `シャトー・テルトルも所有` が `4 つのフィールドに複製されて` 誤りごと反復されている点（Roederer の `house_style` 16 複製、Allemand の `description` 5 複製と同型）** |

### 🔴 ⑥ 未採番の形 —— **「unnumbered — CTO's call」**

🔴 **【新形 A】`パーサはキュヴェ名の不在を検出しており、マッチャがそれを無視してキュヴェを提案している`。**

🔴 **これは「アペラシオンが銘柄名の列に印字された」形（ブリーフ §3 の想定）ではない。3 つの層すべてが `銘柄名は無い` と正しく言っている:**

| 層 | artifact | 銘柄名についての記述 |
|---|---|---|
| **印字メニュー** | `beverage_menu_bottles.doc` p.17 | 🔴 **列が空**（`2020\t\tMargaux\t\t…\t300`） |
| **store 層** | `research/out/t-01/inventory.json` | 🔴 **`product_name: ""`／`classification_text: "Margaux"`。正しく保存** |
| **intake 層** | `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` | 🔴 **`_parts.label: null`／`_parts.appellation: "margaux"`。`Margaux` をラベルではなくアペラシオンとして正しく分類** |

🔴 **にもかかわらず、同じ intake 行が `cuvee_state: "exact"` と `proposed_canonical_cuvee: "Château Giscours"` を出力する。**

🔴 **コーパス全体での実測（`obp_intake_normalized_20260804.json`、704 行、本ドシエで再現確認済み）:**

| 測定 | 値 |
|---|---|
| **全行** | **704** |
| 🔴 **`_parts.label is null`** | 🔴 **292 / 704** |
| 🔴 **Bordeaux セクション内で `_parts.label is null`** | 🔴 **69 / 69 —— `例外なく全行`** |
| 🔴 **`_parts.label is null` かつ `proposed_canonical_cuvee` を発行** | 🔴 **152 行** |
| 🔴 **`_parts.label is null` かつ `cuvee_state: "exact"`** | 🔴 **147 行**（本ドシエによる追加測定） |

🔴 **すなわち欠陥はメニューでもパーサでもなく `マッチャ` にある。キュヴェ名が無いと分かっている 152 行に、キュヴェを提案している。**
🔴 **Bordeaux ブロックはその最も濃い塊（69/69）であり、Batch 12 の 8 軒すべてが `キュヴェ名を 1 つも名乗らない行` に `cuvee_state: exact` を持つ理由がこれである。**
🔴 **本件ではその提案が `Château Giscours`（グラン・ヴァン）—— 本ドシエが「公式資料からは決められない」と証明した二択を、証拠ゼロで片方に倒している。**
→ ⚠️ **ブリーフ §4「`exact` は canonical との一致度であって存在の裏づけではない」の、最も鮮明な実例。**

🔴 **【新形 B】`同一生産者・同一 AOC・同一ヴィンテージに、公式に 2 本のワインが並存する`。**
**`Château Giscours` と `La Sirène de Giscours` は 6 ヴィンテージすべてで共存する。**
🔴 **したがって `producer + appellation + vintage` は canonical において `一意キーになりえない`。**

🔴 **これは Giscours 固有ではなく、Batch 12 の Bordeaux ブロック全体で確定した。理由も判明している ——**
🔴 **本バッチの全セカンド／サードワイン名を 704 行に対して全走査した結果、`両層あわせてヒット 0 件`:**
**`Pagodes`・`Goulée`・`Labory`・`Alter Ego`・`Sirène`・`Petit Mouton`・`Aile d`・`Clarence`・`Clarté`・`Forts de`・`Pavillon`・`Ygrec`・`Carruades` —— `0 / 704`。**
🔴 **すなわちメニューはセカンドワインを名指しで載せたことが一度も無い。**
🔴 **ゆえに「この行はグラン・ヴァンである」と仮定してよい根拠は、コーパス側には `存在しない`。区別する情報がそもそも入っていない。**
**→ 番号を開くかどうかは CTO の判断。本ドシエは形状の記述にとどめる。**

🔴 **【新形 C】`公的登録の est_bio フラグが、同一住所・同一経営者の別法人に付く`。**
**`CHATEAU GISCOURS`（01.21Z、栽培）は `est_bio: false`、`AJ DOMAINES`（46.34Z、卸）は `est_bio: true / liste_id_bio: [10839]`。**
🔴 **住所も経営者（Alexander van Beek）も同一。自動照合が住所や名前で寄せると、`栽培していない法人の卸売認証`を蔵の有機認証として拾う。**
🔴 **`§2e` の「practised vs certified」の一段深い変種 —— `certified, but the wrong legal person and the wrong scope`。**

⚠️ **上記はいずれも **推奨であって実行ではない**。canonical・REGISTER.md は一切変更していない。**

### 推奨（**実行しない**）

| 対象 | 推奨 | 確度 |
|---|---|---|
| `giscours-1855` の `94ha` | **`95 ha en production` に訂正**（公式フィッシュ 6 点で裏付け） | **High** |
| `giscours-1855` の品種比率 | 🔴 **固定比率をレコードから削除し、ヴィンテージ・レコード側に年別で持たせる。固定比率は 6 年すべてで誤り** | **High** |
| `giscours-1855` の「シャトー・テルトルも所有」 | 🔴 **4 フィールドすべてから削除**（公式・公的登録の両方から反証） | **High** |
| `giscours-1855` の「1995 年より Eric が…」 | **「1995 年に Eric Albada Jelgersma が取得、2018 年より子 Dennis・Derk・Valérie」に更新** | **High** |
| `giscours-1855` の「ロゼの先駆者」 | 🔴 **削除。公式は 2019 年創出の「レンジの末っ子」と明記** | **High** |
| `giscours-1855` の Parker 引用 | **削除、または第三者評として明示的にタグ付け**（ブリーフ §2-6） | **Medium-High** |
| OBP 6 行 | 🔴 **ヴィンテージ・レコード新設。ただし `Château Giscours` か `La Sirène` かは`実物ラベル確認まで確定できない`** → Open Questions 1 | **High（gap の存在）／Low（どちらの銘柄か）** |
| `subregion` | ⚠️ **`Margaux` は AOC 名として正しい。ただし `commune` を別フィールドで持てるなら `Labarde`。現行スキーマでは変更不要** | **Medium** |

---

## Sources

### ✅ 採用した公式サイト

| URL | レイヤー | 用途 |
|---|---|---|
| **`https://giscours.com/fr/`** | ✅ | **公式サイト（FR 原本）。トップ** |
| `https://giscours.com/fr/mentions-legales-politique-de-confidentialite/` | ✅ | **真正性チェックの根拠。`Château Giscours / 10 route de Giscours / 33460 LABARDE`** |
| `https://giscours.com/fr/nos-vins/` | ✅ | 現行レンジ 4 品目 |
| `https://giscours.com/fr/vin/chateau-giscours/` | ✅ | グラン・ヴァン。**ミレジム 2000〜2024 の一覧＋フィッシュ PDF 25 点へのリンク** |
| `https://giscours.com/fr/vin/la-sirene-de-giscours/` | ✅ | **セカンド。ミレジム 2010〜2021・2023・2024。AOC Margaux の明記** |
| `https://giscours.com/fr/vin/haut-medoc-giscours/` | ✅ | **3 本目。`appellation Haut-Médoc`／`60 ha`／1992 年創出** |
| `https://giscours.com/fr/vin/le-rose-de-giscours/` | ✅ | ロゼ。2021〜2025。100% CS |
| `https://giscours.com/fr/nos-vins/le-terroir-de-giscours/` | ✅ | **3 つの croupe、標高、土壌** |
| `https://giscours.com/fr/nos-vins/de-la-vigne-au-chai/` | ✅ | **醸造工程、1923 年植栽、「半分超が有機農法」** |
| `https://giscours.com/fr/nos-vins/la-philosophie-de-giscours/` | ✅ | **「半分が有機農法」、Natura 2000、sélection massale** |
| `https://giscours.com/fr/decouvrez-giscours/lhistoire/` | ✅ | **沿革年表（全 17 項目）** |
| `https://giscours.com/fr/decouvrez-giscours/les-gens-de-giscours/` | ✅ | **チーム。「Dennis, Derk & Valérie — Propriétaires」** |
| `https://giscours.com/fr/aj-domaines/` | ✅ | 🔴 **グループの所有一覧＝`Giscours` と `Caiarossa` のみ** |
| `https://giscours.com/fr/2022/03/14/chateau-giscours-un-domaine-viticole-en-agro-ecologie/` | ✅ | **除草剤 10 年不使用、被覆作物 80/160 ha、Jérôme Poisson の言** |
| `https://giscours.com/fr/sitemap_index.xml` ＋ 下位 6 本 | ✅ | 走査元（page 90 / wine 8 / post 34 / product 22 / offer 7 / product_cat 4） |

### ✅ 公式フィッシュ・テクニック（**全 6 点、`%PDF` 実体を検証済み**）

| PDF | サイズ | 内容 |
|---|---|---|
| `/wp-content/uploads/2021/05/CHATEAU-GISCOURS-2010.pdf` | 292 948 B | ⭐OBP。71/29、17 mois、Denis Dubourdieu |
| `/wp-content/uploads/2021/05/CHATEAU-GISCOURS-2011.pdf` | 272 814 B | ⭐OBP。75/20/5 |
| `/wp-content/uploads/2021/05/CHATEAU-GISCOURS-2017.pdf` | 271 334 B | ⭐OBP。71/24/5、Lavigne–Marchal |
| `/wp-content/uploads/2021/05/CHATEAU-GISCOURS-2018.pdf` | 269 365 B | ⭐OBP。55/39/6 |
| `/wp-content/uploads/2021/05/CHATEAU-GISCOURS-2019.pdf` | 280 624 B | ⭐OBP。65/35、Thomas Duclos |
| `/wp-content/uploads/2021/05/CHATEAU-GISCOURS-2020.pdf` | 290 019 B | ⭐OBP。56/44 |

⚠️ **公式は 2000〜2024 の 25 点を配信している（`2021/06/` に 2000–2009、`2021/05/` に 2010–2020、`2021/03/` に 2021–2024）。本ドシエは OBP 該当の 6 点のみを取得・転記した。**

### 🏛 公的登録・法令

| 出典 | 内容 |
|---|---|
| **`recherche-entreprises.api.gouv.fr`** | **SIREN `472200716`（CHATEAU GISCOURS）／`320528037`（AJ DOMAINES）／`429716632`（GFA）／`894341353`・`950360271`（du Tertre）／`484841663`（Conseil GCC 1855）／`q=giscours` 23 件** |
| **`opendata.agencebio.org/api/gouv/operateurs/`** | **SIRET `47220071600034` → `nbTotal 0`／`32052803700056` → `numeroBio 10839`／`42971663200014` → `nbTotal 0`** |
| 🔴 **統合版 CDC「Margaux」（2023-03-31 homologué／2023-04-05 JORF）** | 🔴 🏛 **現行の施行テキスト。`Arsac, Labarde, Margaux-Cantenac, Soussans` の 4 コミューン。**⚠️ **Batch 12 の別エージェントが確定させたもの。本ドシエは独自取得していない** |
| **`https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000021063626/2025-05-20`** | 🏛 ⚠️ **`superseded`。décret n° 2009-1137 du 18 septembre 2009、annexe AOC MARGAUX。2017 年合併前の 5 コミューン表記** |
| **`https://extranet.inao.gouv.fr/fichier/3-CDC-Margaux.pdf`** | 🏛 ⚠️ **`draft`（確定文ではない）。CDC Margaux（2022-09-08 意見に伴う PNO 案）。`%PDF` 検証済み。**🔴 **コミューン列は取り消し線の生き残りにより 5 つに見える（`§2c`）。赤限定・encépagement・植栽密度は本文から採用** |
| **`https://extranet.inao.gouv.fr/fichier/PNOCDCMargaux.pdf`** | 🏛 ⚠️ **`draft`。CDC Margaux（2010-10-21 意見に伴う PNO 案）。`%PDF` 検証済み。`Margaux` を含む旧リスト** |
| **`https://geo.api.gouv.fr/communes`** | 🏛 **Labarde = INSEE `33211`、人口 623**<br>🔴 **`/communes/33268` → `{"nom":"Margaux-Cantenac","anciensCodes":["33091"]}`／`/communes/33091` → `HTTP 404`（旧 Cantenac は消滅）** |
| **`https://gcc-1855.fr/`（`/chateau/chateau-giscours/`・`/mentions-legales/`）** | 🏛 **Conseil des Grands Crus Classés en 1855。「Château GISCOURS ／ `Troisième Cru` ／ Appellation Margaux」。SIRET `48484166300012` が登録と一致（真正性チェック合格）** |
| **`https://www.legifrance.gouv.fr/search/juri?query=Giscours`** | 🏛 **判例検索 15 件（1969・1999×3・2001×4・2003×2・2007・2018 ほか）。**🔴 **醸造実務に関する 2000 年代半ばの決定は 1 件も含まれない** |
| **`https://www.legifrance.gouv.fr/juri/id/JURITEXT000006950326`** | 🏛 **Cour d'appel de Bordeaux, 2006-05-30。**🔴 **Bommes（Sauternes）の別事業者の架空シャトー名事件。Giscours とは無関係と確認** |
| **AFNIC whois `chateau-giscours.fr`** | 🏛 **holder `SOC D'EXPLOITATION DU CHATEAU GISCOURS`／registrar `IDLINE-INTERPC`／`created 1996-06-05`／`last-update 2026-06-30`／`status ACTIVE`** |
| **Internet Archive CDX** | 📄 **`giscours.com` は `2002-05-24` から捕捉あり（最古 302、2011 以降 200）。**🔴 **`chateau-giscours.fr` は `捕捉 0 件`** |

### 🔴 §2a により REJECTED したドメイン（**1 語も使用していない**）

| ドメイン | 状態 | 却下理由 |
|---|---|---|
| 🔴 **`chateau-giscours.fr` / `www.chateau-giscours.fr`** | 🔴 **DNS は `164.132.21.77` に解決するが、HTTPS 証明書が `sal.kaizen-hosting.com` で不一致。HTTP は同ホストへ転送されて `403 Forbidden`（本文 239 バイト）** | 🔴 **`内容を 1 バイトも配信していない`。**⚠️ 🔴 **ただし whois の holder は `SOC D'EXPLOITATION DU CHATEAU GISCOURS`＝蔵自身であり、`look-alike の罠ではなく、蔵が保有したまま公開していないドメイン`である。**🔴 **Internet Archive の捕捉 `0 件`＝一度も公開されたことがない。**🔴 **ブリーフ §5 の 6 形のうち `domain owned but never published` に該当。**🔴 **ホスティング業者（Kaizen）は公式 `giscours.com` と同一である** |
| ⚠️ **`chateau-giscours.com` / `www.chateau-giscours.com`** | **HTTP 応答なし（curl が 1 行も返さず）** | **未登録または未設定。使用せず** |
| ⚠️ **`giscours.fr`** | **HTTP 応答なし** | **未登録または未設定。使用せず** |

⚠️ 🔴 **注意: 複数の第三者サイト（観光局・ネゴシアン等）および検索結果の要約が、公式サイトを `www.chateau-giscours.fr` と案内している。**
🔴 **これは実測で誤りである。現行の公式ドメインは `giscours.com`（Internet Archive で 2002 年から継続捕捉）。**

### ⚠️ 事実出典として使用しなかったもの

- ⚠️ **`bordeaux.com`（CIVB）** — 「Labarde は Margaux を構成する `4 コミューン` のひとつ」という記述に接したが、**業際団体であり §2 の `producer-authored` にも `public register / statutory instrument` にも該当しないため採用しない。**⚠️ **なお `4` は 2017 年の Margaux＋Cantenac 合併後の行政上の数、`5` は法令テキストの数であり、両者は矛盾していない。**
- ⚠️ **`societe.com`、観光局サイト（margaux-medoc-tourisme.com、bordeaux-tourisme.com、labarde.fr）、UGCB** — 第三者。参照のみ、引用せず。
- ⚠️ **Wikipedia** — ブリーフ §2-6 により全面禁止。閲覧・引用ともに行っていない。

---

## Open Questions

🔴 **1.【物理ラベル・最優先】OBP 6 行のボトルは `Château Giscours` か `La Sirène de Giscours` か。**
**両者は同一 AOC（Margaux）で、6 ヴィンテージすべてが両方に実在する。メニューには銘柄名が印字されていない。**
**店の在庫ボトル 6 本のラベルを撮り、次の 4 点を読めば全行が一度に決着する:**
**① 表ラベルに `LA SIRÈNE` の語があるか ② `CHÂTEAU GISCOURS` の表記の有無 ③ ミレジム表記 ④ 裏ラベルの品種表示に `Cabernet Franc` があるか（あれば La Sirène、無ければグラン・ヴァン）。**
🔴 **6 行が同一銘柄とは限らない。1 本ずつ確認すること。**

🔴 **2.【物理ラベル】アルコール度数。公式は 6 ヴィンテージのいずれについても度数を公表していない。ラベルで確認するほかない。**

⚠️ **3.【要・蔵への照会】1552 年より前の所有史。canonical は「14 世紀の防御塔」「Guyscoutz」と書くが、公式沿革はそれ以前に一切触れない。蔵に一次資料の有無を尋ねる価値がある。**

⚠️ **4.【要・蔵への照会】2017 年フィッシュの `PRESIDENT` 欄が、同一 PDF 内で FR 版 `Eric Albada Jelgersma` / EN 版 `Albada Jelgersma Family` と食い違う。2017 年収穫時点の代表者はどちらか。**

⚠️ **5.【要・確認】環境認証の有無。公式サイトに `HVE`・`Terra Vitis`・`Demeter`・`Biodyvin` の語は 1 度も現れない。取得していないのか、単に掲載していないのかは不明。蔵に照会するのが最短。**

🔴 **6.【要・Akio 判断】2000 年代半ばの規制・司法問題。**
🔴 **Légifrance 判例（15 件）・Cour de cassation・造り手のサイト全走査で、`公式出典を 1 件も特定できなかった`。**
🔴 **本ドシエはその内容を記述せず、`言ってはいけないことリスト ①` に置いた。**
🔴 **仏の第一審・控訴審の判決は Légifrance／Judilibre に網羅公開されないため、`見つからないこと` は `存在しないこと` の証明にはならない。**
**この価格帯の格付シャトーであり、ゲストが持ち出す現実的可能性がある。卓上での応答方針を Akio が確定すべき事項である。**

⚠️ **7.【canonical 側】`vintage: "—"` の 1855 格付レコードは Margaux だけで 21 件、canonical 全体で 328 件ある。**
**`giscours-1855` を修正するか、ヴィンテージ・レコードを別途新設するかは、この 328 件の設計方針と不可分である。単独では決められない。**

⚠️ **8.【要・確認】公式の「80 hectares sur les 160」の `160` が何の総面積を指すか。**
**Margaux 95 ha ＋ Haut-Médoc 60 ha ＝ 155 ha に近いが、`合算してよいとは公式のどこにも書かれていない`。**

⚠️ **9.【要・確認】`Rosé x Giscours` のアペラシオン。公式は明示しない。**🏛 **AOC Margaux は赤のみなので Margaux ではありえない。**

⚠️ **10.【軽微・蔵への通知価値あり】公式サイトの `<title>` が FR/EN とも `Grand Cru Classé en 1885` と誤記している（正しくは 1855）。**

⚠️ **11.【要・確認】公式サイト内で有機農法の面積比が `la moitié`（半分）と `plus de la moitié`（半分超）に割れている。どちらが現行値か。**

⚠️ **12.【要・確認】公式 mentions légales が同一ページ内で `33460 LABARDE` と `33460 MARGAUX` を併記している。**🏛 **登記上の commune は `LABARDE`（INSEE 33211）。**
