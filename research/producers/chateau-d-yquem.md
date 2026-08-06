# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical に `producer == "Château d'Yquem"` のレコードは 9 件存在する**（`yquem-2023` / `yquem-2022` / `yquem-2021` / `yquem-2020` / `yquem-2019` / `yquem-2016` / `yquem-2010` / `yquem-1984` / `yquem-ygrec-2017`）。
> 🔍 **`D-2026-08-05-08`（部分文字列の誤検出）は本件では発生しない。全文検索 18 件のうち 9 件は `Bordeaux <年> Vintage Guide` 系の別レコードで、`producer` は `Bordeaux` である。**
> 本書は昇格前の研究記録であり、**canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **造り手自身が現に公開しているもの**（`yquem.fr` / `2023.yquem.fr` / 造り手の署名を持つフィッシュ・テクニック PDF）
> `📄` **造り手の旧サイトを Internet Archive から復元したもの**（`yquem.fr/fr-en/…`。`✅` とは決して混ぜない）
> `🏛` **公的登録・法令**（`recherche-entreprises.api.gouv.fr` / Agence Bio / Ecocert 証明書レジストリ / INAO 官報 CDC / Conseil des Grands Crus Classés en 1855）
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: ✅ **`https://www.yquem.fr/`**（現行・**全 6 URL しかない**）／📄 **`http://yquem.fr/fr-en/…`（Wayback 復元。ミレジム頁 1893–2014 の 122 年分）**
> 走査元: ✅ `robots.txt` → `sitemap.xml`（**6 URL。しかも全 `<loc>` が `http://localhost/`**）／📄 Wayback CDX（`url=yquem.fr&matchType=domain`、2015 年以降 297 URL・ミレジム頁 179 URL）／✅ フィッシュ・テクニック PDF 8 点（**全点 `%PDF` 実体を検証済み**）
>
> ---
>
> 🔴 **① OBP 6 行すべてが `Sauternes (375 mL)` と刷られている。canonical には容量の軸が存在しない。**
> 🔍 **canonical 全 928 件の フィールド名は 55 種類あるが、容量・フォーマットを表す型付きフィールドは 1 つも無い。**
> **唯一の受け皿は `obp_format` という自由文字列で、その 928 件の分布は
> `By the bottle` 909 ／ `BTL 750ml` 8 ／ `By the bottle (Magnum)` 4 ／ `By the bottle · Magnum` 4 ／
> `By the glass · By the bottle` 1 ／ `By the bottle · Half bottle` 1 ／ `By the glass / By the bottle` 1。**
> 🔴 **すなわち「マグナム」という 1 つの軸が 2 通りの綴りで、「ハーフボトル」は canonical 全体で 1 件（`krug-grande-cuvee-170`）しか存在しない。**
> 🔴 **Yquem の 9 件は全件 `obp_format: "By the bottle"` である。375 mL の Yquem レコードは canonical に存在しない。** → §Canonical Conflict ②／`V-2`・`V-3` への証拠
>
> 🔴 **② 【intake 層】の `exact / confidence 1.0` の 2 行（2016・2010）が指す【canonical】レコードは、375 mL のボトルに対応していない。**
> **`yquem-2016` と `yquem-2010` の `obp_format` はいずれも `"By the bottle"` であり、容量の記述をどこにも持たない。**
> 🔴 **同一ヴィンテージの 375 mL と 750 mL は、canonical 上で区別できない。区別する場所が無いからである。**
> **ブリーフの「`exact` は canonical との一致を測っており、存在を測っていない」は本件で再現した。加えて `exact` は容量を一切見ていない。**
>
> 🔴 **③ 4 本の「不在」は、すべてメニューが正しく canonical が欠けている形である。**
> ✅ **2011・2013・2014・2017 は、いずれも造り手自身のフィッシュ・テクニックが実在し、分析値まで公表されている。**
> **2011 = 13.80%Vol / 残糖 144 g/L / pH 3.85 ／ 2013 = 13.1° / 140 g/L ／ 2014 = 13.5° / 146 g/L / pH 3.60 ／ 2017 = 14.00%Vol / 148 g/L / pH 3.80。**
> 🔴 **Batch 10・11 の「メニューが defective とは限らない」に、4 件まとめての反例を追加する。ここではメニューが正しい。** → §Canonical Conflict ①
>
> 🔴 **④ canonical が持つ「誰も売っていないヴィンテージ」は 5 本ではなく 6 本である（ブリーフの記述への反証）。**
> 🔍 **canonical のヴィンテージ集合 = {1984, 2010, 2016, 2019, 2020, 2021, 2022, 2023}。OBP = {2010, 2011, 2013, 2014, 2016, 2017}。**
> **canonical のみ = {1984, 2019, 2020, 2021, 2022, 2023} の 6 本。ブリーフは「五つ」としているが実測は 6 本である。** → §Canonical Conflict ①
>
> 🔴 **⑤ `"Y" Ygrec` は AOC Sauternes ではありえない。法令テキストで決着した。**
> 🏛 **AOC Sauternes の cahier des charges（`arrêté du 12 octobre 2021`、JORF 2021-10-20、BO MAA 2021-10-21）は、
> `Tout lot de vin commercialisé (en vrac) ou conditionné présente une teneur en sucres fermentescibles (glucose et fructose) supérieure ou égale à 45 grammes par litre.` と定める。**
> ✅ **造り手自身の `Y 2016` フィッシュは `Residual sugar: 7g/L` である。45 g/L の 6 分の 1 以下。**
> 🔴 **したがって canonical の `yquem-ygrec-2017.classification = "Sauternes — Dry White"` は、法令上ありえない文字列である。** → §Canonical Conflict ④
> 🏛 **同 CDC の「coefficient K」条項は `同一の生産面積について主張できる AOC は « Sauternes » と « Bordeaux » だけである` と定めており、Y の帰属先を 2 択に絞る。**
> ⚠️ **ただし Y のラベルに刷られた AOC 名そのものは、造り手のどの資料にも書かれていない。断定しない。** → Open Questions 1
>
> 🔴 **⑥ 1855 年の格付け文言は 4 通り流通しており、canonical はそのうち「どれでもない 1 つ」を 2 件に持っている。**
> 🏛 **Conseil des Grands Crus Classés en 1855 の公式一覧 = `Château d'YQUEM / Sauternes / Premier Cru Supérieur`**
> ✅ **現行サイトのタイトル = `Premier Cru Supérieur`（EN）／`1er Cru Supérieur`（FR）**
> ✅ **造り手の OnePager = `the only "Premier Cru Classé Supérieur"`**
> 📄 **旧サイト沿革 = `the one and only premier cru supérieur`**
> 🔴 **canonical は 7 件が `Sauternes Premier Cru Supérieur`（＝公式一致）、2 件（`yquem-2019` / `yquem-1984`）が `Sauternes 1er Grand Cru Classé Supérieur`。後者はどの一次資料の文言とも一致しない。** → §Canonical Conflict ③
>
> 🔴 **⑦ 造り手が「造らなかった年」を自ら 2 か所で列挙している。canonical はそれを「2 で終る年のジンクス」に矮小化している。**
> 📄 **`No Yquem was produced in 1910, 1915, 1930, 1951, 1952, 1964, 1972, 1974, 1992, and 2012.`（旧サイト `tips/days-without`、および 2012 年ミレジム頁に同一の列挙）**
> 🔴 **10 年のうち 6 年は「2」で終らない。**canonical `yquem-2022.obp_note` の「『2』で終るヴィンテージのジンクス（1952・1972・1992・2012 は生産なし）」は、
> **括弧内の 4 件は真だが、造り手自身の列挙の 4 割に過ぎない。**
> 🔴 **そして重要なのは —— OBP の 6 ヴィンテージ（2010・2011・2013・2014・2016・2017）に、非生産年は 1 つも無い。**
>
> 🔴 **⑧ フォーマットは intake 層で検知されている。失われるのは store 層である（層間の伝播損失）。**
> 🔍 **【intake 層】`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）の Yquem 6 行は、全件が `source_quality_flags: ['format_in_name']` を持つ。`match_state` / `confidence` も同ファイルにあり、2016・2010 が `exact` / `1.0`、他 4 行が `unresolved` / `0.0` である。**
> 🔴 **【intake 層】`format_in_name` は 704 行中 6 回しか発火せず、その 6 回すべてが Yquem である。すなわち本生産者がこのフラグの母集団そのものである。**（同ファイルのフラグ語彙は `missing_price` 28 ／ `producer_spelling` 13 ／ `cross_section_duplicate` 8 ／ `cuvee_spelling` 7 ／ `canonical_model_note` 6 ／ **`format_in_name` 6** ／ `disgorgement_in_name` 4 ／ `section_colour_conflict` 3 ／ `section_region_conflict` 2 ／ `malformed_vintage` 2 ／ `disgorgement_unknown` 1）
> 🔴 **【store 層】ところが `research/store/t-01/shells.json`（1047 shell）では、その 6 行が同一の shell `rs:pro:434164aa9498d56f` に畳まれている（`identity_basis: source_exact`、`level: product`、`source_lines` 6 本）。3 つの異なる価格（$1,180 / $850 / $980×4）と 6 つの異なるヴィンテージが 1 個の product shell を共有し、`source_transcription` は 2017 行しか保持していない。ヴィンテージは shell の identity に入っていない。**
> 🔴 **すなわち —— intake 層が現に立てたフラグの対象軸（フォーマット）と、識別に必要なもう 1 つの軸（ヴィンテージ）が、store 層に渡る途中で落ちている。**
> 🔴 **これは既知の intake↔store 乖離の 5 例目である（Bachelet-Monnot / Clos de Tart / Armand Heitz / Hundred Acre に続く）。かつ最も鋭い —— 落ちた軸を intake 層はすでに検知し、フラグとして明示していたからである。** → §Canonical Conflict ⑥
>
> ⚠️ **調査上の制約**
> ⚠️ **① 2010 のフィッシュ・テクニックはどこにも見つからなかった。**造り手の旧サイトのミレジム頁は散文のみで数値を持たない。
>    🔴 **これは「2010 が存在しない」証明ではない。**2010 はミレジム頁が存在し、造り手の非生産年リストにも入っていない。 → Open Questions 4
> ⚠️ **② 現行 `yquem.fr` はワイン頁もミレジム頁も持たない 6 URL のパンフレットである。**六形のうち **「publishing stopped but site live（→ archive recovery works）」** に該当し、実際に Archive 復元が効いた。
> ⚠️ **③ フィッシュ・テクニック PDF は négociant（`bordeaux-tradition.com`）がホストしている。**§2d に従い **ホストではなく署名で採否を決めた** —— 各 PDF のフッターが `Château d'Yquem 2016  1/6  29/05/2017` 形式で château 自身を名乗り、本文が一人称（"we", "at Yquem"）である点をもって造り手の署名と判断した。**négociant のページ本文は 1 語も使っていない。** → §Sources

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`D’Yquem`**（`producer_heading` / `producer_or_brand`。アポストロフィは U+2019） |
| **公式表記** | ✅ **`Château d’Yquem`**（現行サイト全頁・mentions légales・フィッシュ・テクニックのフッター） |
| **サイトのタイトル** | ✅ **`Château d’Yquem – 1er Cru Supérieur Sauternes – Site officiel`**（FR）／✅ **`Château d’Yquem – Premier Cru Supérieur Sauternes – Official Website`**（EN） |
| 🔴 **法人（公式）** | ✅ **`SA du Château d’Yquem`、`société anonyme au capital de 224 640 Euros`、`RCS de Bordeaux B384 809 281`、`siège social : Château d’Yquem, 33210 Sauternes, France`、`Tél. +33 5 57 98 07 07`**（`/mentions-legales`・`/en/legal-information`） |
| 🔴 **法人（🏛 公的登録）** | 🏛 **SIREN `384809281`／`nom_complet: SA DU CHATEAU D'YQUEM`／`nature_juridique 5599`（SA à conseil d'administration）**<br>🏛 **SIRET 本店 `38480928100015`／NAF `01.21Z`（culture de la vigne、naf25 `01.21Y`）／`date_creation: 1992-01-25`／`etat_administratif: A`**<br>🏛 **住所 `CHATEAU YQUEM 33210 SAUTERNES`（`commune 33504`、`lat 44.544613719 / long -0.328611569`）／`tranche_effectif_salarie: 21`／`liste_idcc: ["9331"]`**<br>🔴 🏛 **`liste_id_bio: [175057]`** → §Farming |
| 🔴 **役員（🏛 登録）** | 🏛 **`LURTON Pierre Marie`（1956 年生）— `Président du conseil d'administration`**<br>🏛 **`PASQUINI Lorenzo`（1989 年 2 月生）— `Directeur Général`**<br>🏛 **法人取締役 4 社: `MOET HENNESSY`（SIREN 338228414）／`LVMH MISCELLANEES`（380097881）／`EUTROPE`（409950268）／`UFIPAR`（475484689）**<br>🏛 **`DELOITTE & ASSOCIES`（572028041）— Commissaire aux comptes titulaire** |
| 🔴 **所有（登録と公式の言い方のみ）** | 🏛 **上記 4 法人はいずれも LVMH グループの法人である（登録上の事実は「この 4 社が取締役である」ことに限られる）。**<br>✅ **現行サイトのフッターは `lvmh.com` へリンクする。**<br>📄 **旧サイトの人物頁は `Pierre Lurton was appointed President of Château d’Yquem in 2004 by Bernard Arnault and the LVMH group` と書く。**<br>⚠️ 🔴 **本ドシエは `lvmh.com` のブランド頁を 1 語も使っていない。グループがホストする頁は château 自身の署名層ではない。** |
| ⚠️ **同一敷地のもう 1 法人** | ⚠️ 🏛 **`STE CIVILE CHATEAU YQUEM`／SIREN `782010888`／SIRET `78201088800017`／NAF `01.21Z`／`DOMAINE CHATEAU D'YQUEM 33210 SAUTERNES`／`date_creation: 1900-01-01`／`nature_juridique 6599`／`caractere_employeur: N`（従業員なし）／`liste_id_bio: null`／gérant `LURTON Pierre`**<br>🔴 **同一コミューン・同一代表・同一 NAF だが SIREN が別である。両者の関係（土地保有と operating の分離など）を述べる一次資料に到達していない。断定しない。** → Open Questions 6 |
| **canonical id** | 🔍 **9 件**（下記 §Canonical Conflict） |

### ⚠️ 同名・近名の別事業者 —— **`Yquem` は「城」でも「通り」でも「村」でもある**

🏛 **企業登録を `Yquem` で引くと 138 件が返る。ワイン以外に落ちるものが多数ある。**

| 🏛 SIREN | 名称 | 住所 | 判定 |
|---|---|---|---|
| 🔴 **384809281** | 🔴 **SA DU CHATEAU D'YQUEM** | **CHATEAU YQUEM 33210 SAUTERNES** | 🔴 **本ドシエの対象** |
| ⚠️ **782010888** | **STE CIVILE CHATEAU YQUEM** | **DOMAINE CHATEAU D'YQUEM 33210 SAUTERNES** | ⚠️ **同一敷地の別法人（上記）** |
| ❌ **987506904** | **YQUEM (LA CANTINE DES DUCS)** | **88 RUE DES GODRANS 21000 DIJON** | ❌ **ディジョンの飲食店（NAF 56.10C）。無関係** |
| ❌ **333986495** | **SCI RUE YQUEM** | **CHATEAU FAYAU 33410 CADILLAC-SUR-GARONNE** | ❌ **不動産 SCI。しかも所在は Château Fayau（別の生産者の住所）** |
| ❌ **443545256** | **SCI DU 12 RUE YQUEM** | **12 RUE YQUEM 33490 SAINT-MACAIRE** | ❌ **通り名。無関係** |
| ❌ **827919515 / 801133794 / 793042417 / 845084243** | **BUI PANI ／ AF BOIS COURTAGE ／ STE SDM ／ ZAKARIA DAIRA** | **`RUE D'YQUEM` 40600 BISCARROSSE** | ❌ **ランド県の `rue d'Yquem` に所在する 4 事業者。ワインではない** |

### ⚠️ 同じコミューン（Sauternes 33210）の別シャトー

🏛 **`code_commune=33504` × NAF `01.21Z` × `chateau` で 11 法人。Yquem 2 法人を除く 9 法人は別の生産者である。**

**CHATEAU DE MALLE（987535598）／CHATEAU D'ARCHE（412889636）／SCEA DU CHATEAU FILHOT（342371440）／
SCEA DU CHATEAU LAMOTHE DESPUJOLS（418637732）／SCEA CHATEAU CHERCHY-COMMARQUE（508102829）／
SOC CIVIL AGRI CHATEAU GUIRAUD（322519547）／SARL CHATEAU RAYMOND LAFON FAMILLE MESLI（353633316）／
SA STE DOLPHIN INTERNATIONAL（429040256、住所は CHATEAU GUIRAUD）／GAEC PHILIPPE-JACQUES GUIGNARD（324104819、住所は CHATEAU LAMOTHE）**

→ 🔴 **`Sauternes` は AOC 名・コミューン名・そして OBP のワイン名欄に刷られている文字列の 3 つを同時に指す。**
→ 🔴 **`Château Lamothe` と `Château Lamothe-Guignard` は 1855 年格付けでは別の 2 級である。卓上で混同してはならない。** → §Staff Notes ⚠️ ⑤

---

## Overview

✅ **Château d'Yquem は AOC Sauternes のコミューン Sauternes（ジロンド県 33210）にある単一のシャトーであり、
1855 年格付けにおいてソーテルヌで唯一の最上位に置かれた 1 軒である。**

🔴 **造り手が自らの署名として名指しするものは、はっきりと 3 つある。**

🔴 📄 **① 収穫を「複数回の選別摘み（tries successives）」で行い、そのために全部を失う危険を受け入れること。**
「**Botrytis cinerea は区画ごと、房ごと、果粒ごとに違う振る舞いをする。摘み手は最も熟し、最も「腐った」実だけを選ぶ。
基準に達しないものは次のパスに残す。1 ヴィンテージあたり平均 5〜6 回のパスを 6 週間にわたって行う。
しかしある年には、収穫が 10 月に始まって 12 月まで終わらず、10 回以上畑を通らねばならない —— そのヴィンテージが Yquem の名に値しなくなる危険を冒してでも。**」（📄 `/fr-en/expertise`）

🔴 📄 **② 「造らない」という選択を実行すること。**
📄 **`No Yquem was produced in 1910, 1915, 1930, 1951, 1952, 1964, 1972, 1974, 1992, and 2012.`**
📄 **2012 年のミレジム頁は同じ列挙を繰り返したうえで `no wine was sold under the château name` と書く。**
🔴 **すなわち造り手の言い方は「造らなかった」ではなく「シャトー名で売らなかった」である。**

🔴 📄 **③ ソーテルヌでは異例の、樽内発酵と 100% 新樽。**
「**Unusually in Sauternes, fermentation at Yquem takes place in barrel… Only new barrels are used each year.**」（📄 `/fr-en/expertise`）

📄 **収量は平均 9 hl/ha。**「**18° から 20° へ潜在アルコールが上がると、果汁量は平均 50% 減る。これが Yquem の極端に低い収量（平均 9 hl/ha）の主因である。**」

🔍 **THÉSEUS における状態は Billecart-Salmon 型（レコードは多いが、売っている行と噛み合わない）である。
canonical は 8 ヴィンテージ＋Ygrec 1 本を持つが、OBP の 6 行のうち当たるのは 2 行だけで、
canonical が厚く持つ 2019–2023 は 1 行も売られていない。**

---

## History

📄 **旧サイトの沿革頁（`/fr-en/history`）が造り手自身の記述として取得できた唯一の系統である。現行サイトに沿革頁は存在しない。**

- 📄 **中世、領地はアキテーヌ公を兼ねたイングランド王のものだった。1453 年、シャルル 7 世により南西フランスがフランス王権に復した。**
- 📄 **1593 年、地元貴族の家系の Jacques Sauvage が Yquem の封建的保有権（feudal tenure）を与えられる。ジロンド県文書館とシャトーの文書に、この時点ですでに特殊な栽培と遅摘みが存在したことが示される。**
- 📄 **1711 年、ルイ 14 世治下で Sauvage 家が完全な所有者となる。**
- 📄 **1785 年、Françoise Joséphine de Sauvage d'Yquem が Comte Louis Amédée de Lur-Saluces と結婚。1788 年に伯爵が落馬事故で死去し、若い未亡人が当主となる。1826 年に新しい醸造庫を建設。**📄 **「複数回パスで摘む方法が完成されたのは彼女の時代である。」**
- 🔴 📄 **1855 年 —— `In 1855, in posthumous recognition of the tremendous accomplishments of "the lady of Yquem", the estate was designated the one and only premier cru supérieur in the famous classification made at the request of Emperor Napoléon III.`**
- 📄 **19 世紀後半の繁栄。ロシア皇帝の弟 Constantine 大公が 1 樽に 2 万金フランを支払った。明治期の日本にも渡った。**
- 📄 **フィロキセラと第一次大戦。1914 年、シャトーは軍病院となる。Marquis Bertrand de Lur-Saluces が 30 歳で経営を継ぎ、半世紀を務める。補糖（chaptalisation）に反対し、`Union des Crus Classés de la Gironde` の会長を 40 年務め、ソーテルヌ AOC の法制面に関与し、真正性保証のためのシャトー元詰めを推進した。**
- 🏛 **法人 `SA DU CHATEAU D'YQUEM` の登録上の設立は 1992-01-25。**⚠️ **もう 1 法人 `STE CIVILE CHATEAU YQUEM` の `date_creation` は `1900-01-01` だが、これは INSEE の既定値である可能性があり、実際の設立年として扱わない。**
- 📄 **2004 年、Pierre Lurton が Bernard Arnault と LVMH グループにより社長に任命される。**
- 🏛 **現在（登録の最新更新 2026-07-17）は Pierre Lurton が会長、Lorenzo Pasquini が Directeur Général。**

⚠️ **`founded_year` に相当する年を造り手は 1 つに絞っていない。**「400 years of passion」という見出しと 1593 年（封建的保有）・1711 年（完全所有）が併存する。**canonical の 9 件はいずれも `founded_year` フィールドを持たない（＝矛盾も生じていない）。**

---

## Location

### 🏛 AOC Sauternes（法令テキスト）

🏛 **出典 = `info.agriculture.gouv.fr/gedei/site/bo-agri/…` の consolidated 版。`%PDF-1.5`・12 頁を実体検証済み。**
🔴 **`extranet.inao.gouv.fr/fichier/4-CDC-Sauternes-PNO.pdf`（PNO ドラフト）は §2c の警告どおり採用していない。**

| 項目 | 🏛 CDC の規定 |
|---|---|
| **法令** | **`Homologué par arrêté du 12 octobre 2021`／`publié au JORF du 20 octobre 2021`／`Publié au BO du MAA le 21 octobre 2021`** |
| **初回承認** | **`initialement reconnue par le décret du 30 septembre 1936`** |
| 🔴 **色・タイプ** | 🔴 **`L'appellation d'origine contrôlée « Sauternes » est réservée aux vins tranquilles blancs.`** |
| **アペラシオン地域** | **Barsac, Bommes, Fargues, Preignac, Sauternes（ジロンド県 5 コミューン）** |
| **区画界定** | **INAO 全国委員会 `19 février 1986` / `30 mai 2007` / `5 novembre 2015` の各会期で承認** |
| **近接地域（醸造・熟成の例外）** | **Budos, Cadillac, Cérons, Escoussans, Gabarnac, Illats, Ladaux, Langon, Mazères, Monprimblanc, Omet, Pujols-sur-Ciron, Roaillan, Sainte-Croix-du-Mont** |
| **品種** | **`muscadelle B, sauvignon B, sauvignon gris G, sémillon B`** |
| 🔴 **収穫** | 🔴 **`Les vins proviennent de raisins récoltés à surmaturité (présence de pourriture noble).`**／**`récoltés manuellement par tries successives`** |
| 🔴 **糖度** | 🔴 **`richesse en sucre` が `221 g/L` 未満の果実は「良熟」と見なされない** |
| **アルコール** | **潜在（naturel）最低 15%／実（acquis）最低 12%** |
| **収量** | **`25 hl/ha`／`rendement butoir 28 hl/ha`** |
| 🔴 **残糖** | 🔴 **`Tout lot de vin commercialisé (en vrac) ou conditionné présente une teneur en sucres fermentescibles (glucose et fructose) supérieure ou égale à 45 grammes par litre.`** |
| **揮発酸** | **`≤ 25 meq/L`（酢酸換算 1,5 g/L）** |
| **熟成** | **収穫翌年の `15 juin` まで最低熟成／`30 juin` 以降に消費者向け出荷** |
| 🔴 **coefficient K** | 🔴 **`Il ne peut être revendiqué pour les vins produits sur une même superficie déterminée de vignes en production que les appellations d'origine contrôlées « Sauternes » et « Bordeaux ».`** → §Important Cuvées（Y の帰属） |
| **禁止機材** | **`foulo-benne`／`égouttoir dynamique`／直径 400 mm 未満のスクリューを持つ連続式圧搾機** |

### 📄 シャトーの畑（造り手自身の数値。現行サイトには一切無い）

| 項目 | 値 | 出典 |
|---|---|---|
| 🔴 **植栽面積** | 🔴 **`113 hectares of vines, of which only one hundred produce grapes in a given vintage`** | 📄 `/fr-en/domain` |
| 🔴 **生産面積（2016 年時点）** | 🔴 **`104 ha en production`** | ✅ `Yquem-2016-FT-GB.pdf` p.2 |
| **同（marketing 文書）** | **`a hundred hectares of vineyards … planted on a mosaic of different soils`** | ✅ OnePager（2019 リリース時） |
| **非生産分** | **毎年 2〜3 ha を抜根し 1 年休閑。新植は基準に達するまで最低 5 年。結果として毎年 12 ha が非生産** | 📄 `/fr-en/domain` |
| **セパージュ（植栽比率）** | **`Sémillon (75%)` / `Sauvignon Blanc (25%)`** | 📄 `/fr-en/domain` |
| **樹数** | **`some 700,000 vines`（東側の除葉対象）** | 📄 `/fr-en/expertise` |
| **表土** | **`warm and dry, accumulating heat thanks to smooth flat pebbles and coarse gravel`** | 📄 `/fr-en/domain` |
| **下層土** | **`clay subsoil contains good water reserves and there are numerous springs on the estate`** | 📄 `/fr-en/domain` |
| 🔴 **排水** | 🔴 **`100 km of drains since the 19th century`** | 📄 `/fr-en/domain` |
| **微気候** | **`a 20 km strip of land along both sides of the Garonne Valley`（Sainte Croix du Mont, Loupiac, Cérons, Cadillac, Barsac が並ぶ帯）** | 📄 `/fr-en/domain` |
| **区画の安定性** | **`some 90% of the plots have remained unchanged`** | 📄 `/fr-en/expertise` |

⚠️ 🔴 **面積は 3 通りある。`113 ha 植栽 / 約 100 ha 生産`（📄 旧サイト）・`104 ha en production`（✅ 2016 フィッシュ）・`a hundred hectares`（✅ OnePager）。**
**いずれも造り手自身の数字であり、年によって生産面積が動くという同サイトの説明と整合する。どれか 1 つに丸めない。**
🔴 **canonical の `103ha` はこの 3 つのどれとも一致しない。** → §Canonical Conflict ②

### 🏛 1855 年格付け（Sauternes は Médoc とは別リスト）

🏛 **出典 = `Conseil des Grands Crus Classés en 1855 (Médoc & Sauternes)`。**
🏛 **§2a 検証: 同会の `mentions légales` が `Siret. 48484166300012 / Code APE. 9411Z / 1, cours du 30 Juillet – 33000 Bordeaux` を名乗り、
企業登録の `CONSEIL DES GRANDS CRUS CLASSES EN 1855 / SIREN 484841663 / SIRET 48484166300012 / NAF 94.11Z / 1 COURS DU XXX JUILLET 33000 BORDEAUX` と完全一致した。**

🔴 🏛 **公式一覧の該当行は `Château d'YQUEM ／ Sauternes ／ Premier Cru Supérieur` である（アペラシオン順ソート）。**

🏛 **同一覧の Sauternes / Barsac 部分の実測:**

| 階級 | Sauternes | Barsac | 計 |
|---|---|---|---|
| **Premier Cru Supérieur** | **d'YQUEM** | — | **1** |
| **Premier Cru** | **LA TOUR BLANCHE / LAFAURIE-PEYRAGUEY / Clos HAUT-PEYRAGUEY / de RAYNE-VIGNEAU / SUDUIRAUT / GUIRAUD / RIEUSSEC / RABAUD-PROMIS / SIGALAS-RABAUD**（9） | **COUTET / CLIMENS**（2） | **11** |
| **Second Cru** | **d'ARCHE / FILHOT / de MALLE / ROMER / ROMER-DU-HAYOT / LAMOTHE / LAMOTHE-GUIGNARD**（7） | **de MYRAT / DOISY DAËNE / DOISY-DUBROCA / DOISY-VEDRINES / BROUSTET / NAIRAC / CAILLOU / SUAU**（8） | **15** |
| | | | **合計 27** |

⚠️ 🔴 **造り手の旧サイトはこれと違う数を書く。**
📄 「**eleven first growths and twelve seconds** are located around Château d'Yquem – the only Premier Cru Supérieur」（📄 `/fr-en/domain`）
→ ⚠️ **1 級 11 は一致するが、2 級は 📄 12 と 🏛 15 で食い違う。両論を保存する。どちらかを選ばない。** → Open Questions 7

---

## Farming

### 🏛 Agence Bio —— **SIRET 完全一致クエリで 1 件ヒット**

🏛 `https://opendata.agencebio.org/api/gouv/operateurs/?siret=38480928100015` → `nbTotal: "1"`

| 項目 | 🏛 登録値 |
|---|---|
| **`numeroBio`** | **`175057`** |
| **`raisonSociale`** | **`SA DU CHATEAU D'YQUEM`** |
| **`denominationcourante`** | **`CHATEAU D'YQUEM PASQUINI Lorenzo`** |
| **`siret`** | **`38480928100015`**（企業登録の本店 SIRET と完全一致） |
| **`activites`** | **`Production` ＋ `Préparation`**（＝栽培と醸造の両方） |
| **`annuaireActivites`** | **`Viticulture`** |
| 🔴 **`certificats`** | 🔴 **`numeroControleEu: FR-BIO-01`／`organisme: Ecocert France`／`etatCertification: ENGAGEE`／`dateEngagement: 2019-08-12`／`dateNotification: 2019-07-10`／`dateSuspension: null`／`dateArret: null`** |
| 🔴 **`datePremierEngagement`** | 🔴 **`2019-08-12`** |
| **`mixite`** | **`Oui`** |
| **`dateMaj`** | **`2024-04-10`** |
| **`productions`（`anneeReferenceControle: 2026`）** | **`01.21.12 Raisin de cuve` = `AB` ＋ `CS`／`11.02 Vins de raisin` = `AB` ＋ `CNS`／`01.19.10.12 Prairie permanente` = `AB`／`01.91 Jachère…` = `C1` ＋ `CS` ＋ `AB`／`ACT.Prod.Inc Culture inconnue` = `AB` ＋ `C2`** |

🏛 **Ecocert の証明書レジストリ（`certificat.ecocert.com/entreprise/F7380666-…`）:
`CHATEAU D'YQUEM PASQUINI Lorenzo`／`Château d'YQUEM 33210 Sauternes, France`／
`Activités : Agriculteur (production végétale), Fabricant & Transformateur`／
`Certification Agriculture biologique Europe (EU) 2018/848 [FR]`／
製品カテゴリ `Boissons alcoolisées`・`Fruits, noix, légumes et dérivés`・`Surface de biodiversité`。**

### 🔴 温度差（temporal trap）—— **OBP の 6 本すべてが認証より前である**

🔴 **`datePremierEngagement = 2019-08-12`。OBP の 6 ヴィンテージは 2010・2011・2013・2014・2016・2017 で、全件がこれより前の収穫である。**

→ 🔴 **したがって OBP の 6 本について、「オーガニックである」とも「オーガミックでない」とも言ってはならない。**
→ 🔴 **Moussé・Giraud・Dauvissat と同型の 4 例目である。** → §Staff Notes ⚠️ ①

⚠️ **canonical `yquem-2022` の `2022年からオーガニック認証取得` / `First organic-certified vintage` は、
`2019-08-12` の engagement とブドウ樹の転換期間（EU 2018/848 の一般則）に照らして矛盾しない。
ただし「2022 が初の認証ヴィンテージである」と明言する造り手の一次資料には到達していない。** → Open Questions 5

### 📄 栽培の実務（造り手自身の記述。認証とは別の話）

- 📄 **`Fertiliser is exclusively organic and used sparingly. Furthermore, only 20 hectares are fertilised a year.`**
- 📄 **`Chemical weed killers are never used.`**
- 📄 **`The soil undergoes regular cycles of manual work: earthing up twice a year, unearthing twice a year…`**
- 📄 **剪定 —— `The Sémillon is spur pruned (two to three renewal spurs with two buds), whereas the more vigorous Sauvignon Blanc is 90% spur pruned and 10% Single Guyot pruned.`**
- 📄 **`Château d'Yquem's twenty female vineyard workers are each assigned specific plots, so they become familiar with virtually each vine.`**
- 📄 **収穫直前に `leaf thinning on the eastern side of some 700,000 vines`（西側は雨よけに残す）。**

⚠️ 🔴 **これらはすべて 2016 年前後の旧サイトの記述である。2026 年時点でも同じかは、現行サイトが沈黙しているため確認できない。**
⚠️ **HVE / Demeter については、企業登録の `liste_rge` が `null` であること以外の登録上の手掛かりに到達していない。「持っていない」とは言わない。** → Open Questions 8

---

## Winemaking

📄 **出典はすべて旧サイト `/fr-en/expertise`（造り手自身の記述）。現行サイトに醸造頁は存在しない。**

### 収穫

- 📄 **`Botrytis cinerea` が正常に進むと果皮が透過性になり果汁が蒸発する。糖度は通常の熟度をはるかに超えて `18-30° potential alcohol, i.e. 300-600 grams of sugar per litre` に達する。**
- 🔴 📄 **`Château d'Yquem's goal is to obtain musts with 20° potential alcohol (360 grams of sugar per litre).`**
- 🔴 📄 **`An increase from 18 to 20° alcohol decreases the volume of juice by an average of 50%. This largely accounts for Yquem's extraordinarily low yields (9 hectolitres per hectare on average).`**
- 📄 **収穫期は摘み手が 200 名増え、4 班に分かれる。平均 5〜6 パス／6 週間。年によっては 10 月開始・12 月終了で 10 回以上。**

### 圧搾

- 📄 **摘んでから醸造庫まで 1 時間以内。**
- 📄 **`The grapes are pressed three or four times at Yquem. As opposed to other white wines, the sugar content and quality increase with each pressing.`**
- 📄 **1 回目（空圧式）= 全果汁の 75%・潜在 19° 前後／2 回目 = 15%・21° 前後／3 回目 = 最大 25°。搾り粕は除梗して小容量の垂直式で圧搾。収穫が極小の年は垂直式のみ。**

### 発酵・熟成

- 🔴 📄 **`Unusually in Sauternes, fermentation at Yquem takes place in barrel…`／`Only new barrels are used each year.`（＝新樽 100%）／樽材は `the finest stave oak from forests in the eastern part of central France`。**
- 📄 **最も活発なマストは 2 週間、遅いもので 6 週間。`Fermentation stops naturally in all instances.`**
- 🔴 📄 **`The alcohol content at Château d'Yquem varies from 12.5° to 14.5°… The ideal figure is 13.5° with 120 to 150 g/l of residual sugar.`**
- 📄 **同じ日に摘んだ果実のワインは 6〜8 か月別々に熟成。翌春に予備アッサンブラージュ。**
- 🔴 📄 **`The barrels that have been retained are then moved to the ageing cellar where they will stay for twenty months.`**
- 📄 **各樽は週 2 回の補酒（ouillage）、15 回の澱引き（racking）、清澄（fining）。樽熟の終盤にブラインドテイスティングによる厳しい選別を行い、最終アッサンブラージュを決める。**

### 瓶詰め・容量

- 🔴 📄 **`The wine is bottled during the third winter after the harvest… using 54 mm corks, the only length suitable for a wine of such great ageing potential.`**
- 🔴 📄 **`At Yquem, most of the wine is put into 75 cl. bottles, but there are also many other sizes, from half-bottles to very large ones: magnums, double magnums (3 litres), impériales (4.5 litres), and a limited release of nebuchadnezzars (15 litres) for the 2005 vintage.`**
- 🔴 📄 **`Whether in adorable 0.375 litre or grandiose 15 litre bottles, Yquem comes in various sizes.`**（`/fr-en/tips/outsize-bottles`）

→ 🔴 **これが OBP の `(375 mL)` を裏づける造り手自身の記述である。ハーフボトルは実在する規格である。** → §Important Cuvées

### 提供温度（造り手自身の指定）

🔴 📄 **`Young vintages of Yquem are best enjoyed on the cool side (9°C), while it is preferable to serve older ones at a higher temperature (12°C).`**（`/fr-en/tips/9c`）
→ 🔴 **造り手は 1 つの温度ではなく「若いほど低く」という 2 段の指示を出している。** → §Canonical Conflict ②

---

## Style

🔴 **本節は造り手自身の言葉のみ。第三者の評点・評言は一切採用しない。**

📄 **`/fr-en/the-miracle-of-yquem`（The Style of Yquem）:**

- 📄 **「Yquem は口中に驚くほど長く留まる。フランス語にその余韻を言い表す美しい表現がある —— `il fait la queue du paon`（孔雀の尾のように広がる）。」**
- 📄 **「若いヴィンテージの香りは必ずしも開いていないが、果実（アプリコット、マンダリン、ときにトロピカルフルーツ）と樽（ヴァニラ、トースト香）に彩られる。」**
- 📄 **「熟成したヴィンテージは抜栓した瞬間から並外れて複雑な香りを持つ —— ドライアプリコット、プルーン、煮た果実、マーマレードといった乾果、シナモン・サフラン・リコリスの香辛料、そして菩提樹の花などの花。」**
- 📄 **「口に含んだ第一印象はつねに極めてシルキーで、しばしば豪奢である。それから膨らみ、`口を覆う`。強い、しかし決して押しつけがましくない性格。糖と酸（甘さと鮮度）のバランスをつねに保つ。わずかな苦味も全体の調和に寄与しうる。」**
- 📄 **「若い Yquem を飲むのは冒涜であり、30 歳を迎える前に開けるべきではないと考える愛好家もいる。逆に、Yquem は人生のどの段階でも楽しめると考える者もいる。」**

✅ **2023 年の技術チームによるテイスティングノート（`CY2023_VintageCard_EN.pdf`）は現行で取得できる唯一の造り手自身のノートである:**
✅ **「香りは純粋かつ凝縮しており、ローストしたルバーブ、ライラックの花、柑橘に、シダーと蜜蝋がひとつまみ。口中はビロードのように滑らかで広がりがあり、アーモンドを思わせるテクスチャーが躍動感と力を高める。」**

⚠️ **OBP の 6 ヴィンテージについては、造り手自身のテイスティングノートに到達していない（フィッシュ・テクニックは気象・収穫・分析値のみで、官能記述は第三者の引用欄に置かれている）。** → §Staff Notes ⚠️ ③

---

## Important Cuvées

### ✅ 公式の現行レンジ

| ワイン | 位置づけ | 出典 |
|---|---|---|
| ✅ **`Château d'Yquem`** | **グラン・ヴァン。貴腐甘口** | ✅ 現行サイト／✅ 全フィッシュ |
| ✅ **`"Y"`（Ygrec）** | 🔴 **セカンドワインではない。辛口白の独立したワイン** | 📄 `/fr-en/y-the-other-exception`／✅ `Y-2016-FT-GB` |

🔴 **`Y` について造り手自身が書いていること:**
📄 **`With an annual production of 10,000 bottles a year, Y (pronounced "ee-grek" in French) is a rare wine. It is made from the same outstanding terroir and the same vines as Château d'Yquem.`**
📄 **1959 年以来、少量かつ不定期に生産。1996 年にスタイルを変更。`It was decided in 2004 to make Y every year.`**
📄 **`Since it was created in 1959, only 33 vintages of Y have left the château cellars.`（`/fr-en/tips/every-other-year`）**
📄 **ソーヴィニヨン・ブランの一部区画を収穫初期に完熟で摘み、セミヨンは「最大熟度に達し、ボトリティスが現れたばかりで果皮がピンクに変わった」一瞬に摘む。**
📄 **発酵は専用のヴァットルームで温度管理。発酵の終わりと澱の上での熟成は樽で。`Only one third of these are new`、`bâtonnage for ten months`。**
📄 **`The final blend is made after tasting. It usually consists predominantly of Sauvignon Blanc and a few lots of Sémillon.`**
📄 **Pierre Lurton の言葉 —— `Y is a wine in its own right that has succeeded in emancipating itself from Yquem.`**

✅ **`Y 2016` フィッシュの分析値 = `Y 2016 : 75 % Sauvignon / 25% Sémillon ／ Alcohol content: 14.5° – Residual sugar: 7g/L – AT: 4g/L H2SO4`**

🔴 **AOC の帰属 ——**
🏛 **AOC Sauternes は瓶詰め時点で残糖 `≥ 45 g/L` を要求する。`Y` の 7 g/L はその 6 分の 1 以下である。したがって `Y` は AOC Sauternes ではありえない。**
🏛 **同 CDC の coefficient K 条項は、同一の生産面積について主張できる AOC を `« Sauternes »` と `« Bordeaux »` の 2 つに限定する。`Y` は 📄 造り手自身が `the same vines as Château d'Yquem` と書く畑から出る。**
⚠️ 🔴 **ここまでが法令と造り手の記述から言えることのすべてである。ラベルに実際に刷られた AOC 名を述べる一次資料には到達していない。断定しない。** → Open Questions 1

### 🔴 OBP 6 行 —— 1 行ずつ

🔍 **【store 層 / `research/out/t-01/inventory.json`】6 行はすべて `beverage_menu_bottles.doc` / `WINE` / `section_path: ["FRANCE | WHITE", "BORDEAUX"]` / `section_start_page: 17` / `layout: producer_heading`。`product_name` は 6 行とも空文字列、`classification_text` は 6 行とも `Sauternes (375 mL)`。**
🔴 **【intake 層 / `obp_intake_normalized_20260804.json`】6 行とも `source_quality_flags: ['format_in_name']` が立っている。corpus 704 行中この語彙が発火するのは 6 回だけで、その 6 回すべてが本生産者である。** → §Canonical Conflict ⑥

| # | 行 | 価格 | 🔍 canonical | 🔴 実際に何のワインか（一次資料） |
|---|---|---|---|---|
| **1** | **`2017  Sauternes (375 mL)`**（line 706） | **$1,180** | 🔴 **不在（gap）。canonical の 2017 は `yquem-ygrec-2017`＝辛口 `Y` のみ** | 🔴 ✅ **グラン・ヴァン `Château d'Yquem 2017`。造り手のフィッシュ（`06/09/2019`）が実在:**<br>✅ **`Alcohol content: 14.00%Vol. - Residual sugars: 148 g/L - Total acidity: 5.6 g/L H2T – pH: 3.80 ／ Sémillon 75% - Sauvignon 25%`**<br>✅ **4 月末の霜は `the temperature did not go below the freezing point at Château d'Yquem`。`Y` の収穫開始 8/16 は史上最速。主力は 9/26–10/9 の 11 日間、10/11–13 で終了**<br>🔴 **辛口 `Y` ではない。残糖 148 g/L は AOC Sauternes の 45 g/L を大きく超える** |
| **2** | **`2016  Sauternes (375 mL)`**（707） | **$850** | ✅ **`yquem-2016`（`exact` / 1.0）**<br>🔴 **ただし当該レコードは 375 mL を表さない** | 🔴 ✅ **グラン・ヴァン `Château d'Yquem 2016`。フィッシュ（`29/05/2017`、6 頁）:**<br>✅ **`Alcohol content: 14.20%Vol. - Residual sugars: 135 g/L - Total acidity: 4.8 g/L H2T – pH: 3.90`**<br>✅ **4 回のパス、9/27–28 開始・11/4 終了。`about 75% of the crop was picked in the last two weeks`。`104 ha en production`** |
| **3** | **`2014  Sauternes (375 mL)`**（708） | **$980** | 🔴 **不在（gap）** | 🔴 ✅ **グラン・ヴァン `Château d'Yquem 2014`。フィッシュ:**<br>✅ **`Alcoholic degree: 13.5° - Residual sugar: 146 g/L – Tartaric acidity: 7.5 g– pH: 3.60`**<br>✅ **収穫は 9 週間。`25 % of the grapes harvested before 15 September`。第 1 波 9/5–17、第 2 波 9/25–10/8、第 3・4 波 10/20–30** |
| **4** | **`2013  Sauternes (375 mL)`**（709） | **$980** | 🔴 **不在（gap）** | 🔴 ✅ **グラン・ヴァン `Château d'Yquem 2013`。フィッシュ（`07/10/2014`、3 頁）:**<br>✅ **`Alcoholic degree: 13.1° - Residual sugar: 140 g/L - Total acidity: 4.0 g/LH2SO4`**<br>✅ **第 1・2 パスが 9/25 と 10/2、10/11 に第 2 パス完了、10/21–24 に第 3 パス、第 4 パスで終了** |
| **5** | **`2011  Sauternes (375 mL)`**（710） | **$980** | 🔴 **不在（gap）** | 🔴 ✅ **グラン・ヴァン `Château d'Yquem 2011`。フィッシュ:**<br>✅ **`Alcohol by volume 13,80% Vol - Residual sugar 144gr/L – PH : 3,85`**<br>✅ **`Y` の収穫開始 8/17（`the earliest recorded date at Yquem`）。貴腐果の収穫開始 9/6 は `the 4th earliest harvest in the past 125 years, after 1893, 1960, and 1997`** |
| **6** | **`2010  Sauternes (375 mL)`**（711） | **$980** | ✅ **`yquem-2010`（`exact` / 1.0）**<br>🔴 **ただし当該レコードは 375 mL を表さない** | 🔴 📄 **グラン・ヴァン `Château d'Yquem 2010`。フィッシュには到達できず、造り手の記述は旧サイトのミレジム頁の散文のみ:**<br>📄 **`A cool year, but one made interesting thanks to a warm, dry summer. The weather was ideal during the harvest and the grapes were in great condition. It was vital to pick only the best terroirs and to avoid the temptation of too large a crop by a rigorous sorting and selection during blending. The result is brilliant and more profound that anyone had dared to hope.`**<br>⚠️ **分析値は不明。canonical の `138 g/L` を裏づける一次資料は無い** → Open Questions 4 |

### 🔴 非生産年の照合 —— **6 行すべて「造られた年」である**

📄 **造り手自身の列挙（2 か所で一致）= `1910, 1915, 1930, 1951, 1952, 1964, 1972, 1974, 1992, 2012`。**
🔴 **OBP の 6 ヴィンテージにこれらは 1 つも含まれない。かつ 6 件中 5 件は造り手のフィッシュ・テクニックで、残る 1 件（2010）は造り手のミレジム頁で、それぞれ生産が確認できた。**
→ 🔴 **「実在しないヴィンテージを売っている」という疑いは、この 6 行については消えた。**

### 🔴 `(375 mL)` の扱い

📄 **造り手はハーフボトル（0.375 L）を規格として明示している。すなわちメニューの `(375 mL)` は実在の容量である。**
🔍 **一方 canonical には容量の軸が無く、Yquem の 9 件はすべて `obp_format: "By the bottle"` である。**
🔴 **したがって「2016 の 375 mL」と「2016 の 750 mL」は canonical 上で同一のレコードに落ちる。値段が $850 と（仮に）その倍近くになりうる 2 つの商品が、1 つの識別子を共有する。** → §Canonical Conflict ②

---

## Staff Notes

### 🔴 芯 3 点（これだけ言えば、嘘をつかずに卓上で話せる）

🔴 **① 「ソーテルヌで唯一の最上位」は 1855 年格付けの事実である。ただし言い方は `Premier Cru Supérieur` で固定する。**
🏛 **1855 年格付けを管理する Conseil des Grands Crus Classés en 1855 の公式一覧が `Château d'YQUEM / Sauternes / Premier Cru Supérieur` と書いている。**
🏛 **同一覧のソーテルヌ／バルサック部分は 1 + 11 + 15 = 27 シャトーで、Yquem だけが最上段にいる。**
📄 **造り手自身も `the one and only premier cru supérieur` と書く（1855 年、Napoléon III の求めによる格付けにおいて）。**
🔴 **`1er Grand Cru Classé Supérieur` とは言わない。canonical の 2 件がその文字列を持っているが、どの一次資料とも一致しない。**

🔴 **② 数字で言えるのは「1 ヘクタールあたり 9 ヘクトリットル」と「複数回の摘み」である。**
📄 **`Yquem's extraordinarily low yields (9 hectolitres per hectare on average)`。AOC の上限は 25 hl/ha（butoir 28）だから、自主的に 3 分の 1 近くまで落としている。**
📄 **`There are an average of five or six passes per vintage, spread over six weeks.`**
🏛 **AOC 側の要件も `récoltés manuellement par tries successives`・`surmaturité (présence de pourriture noble)` であり、手摘み・複数回は法令上の義務でもある。**
📄 **樽内発酵・新樽 100%・熟成庫で 20 か月・収穫後 3 度目の冬に瓶詰め・コルクは 54 mm。**

🔴 **③ 目の前の 6 本の分析値は、5 本まで造り手自身の数字で言える。**
✅ **2017 = 14.00%・残糖 148 g/L・pH 3.80／2016 = 14.20%・135 g/L・pH 3.90／2014 = 13.5°・146 g/L・pH 3.60／2013 = 13.1°・140 g/L／2011 = 13.80%・144 g/L・pH 3.85。**
⚠️ **2010 だけは分析値が取れていない。数字を言わない。**
📄 **提供温度は造り手の指定で「若いヴィンテージは 9℃ 寄り、熟成したものは 12℃ 寄り」。2010–2017 はいずれも熟成側に寄せて構わない。**

### ⚠️ 言ってはいけないこと（must-not-say）

⚠️ 🔴 **① 「オーガニック」も「オーガニックではない」も言わない。**
🏛 **Agence Bio の `datePremierEngagement` は `2019-08-12`。OBP の 6 ヴィンテージ（2010–2017）は全件がそれより前の収穫である。**
**現在の認証はこの 6 本について何も語らない。認証の話をするなら「畑は 2019 年に有機の手続に入り、Ecocert が認証機関である」という現在形だけを言い、必ずヴィンテージから切り離す。**

⚠️ 🔴 **② `1er Grand Cru Classé Supérieur` と言わない。**
**canonical の `yquem-2019` と `yquem-1984` がその文字列を持っており、そのまま読み上げると格付け機関の公式文言と食い違う。正しくは `Premier Cru Supérieur`。**

⚠️ 🔴 **③ 「畑は 103 ヘクタール」と言わない。**
**canonical 9 件すべてが `103ha` という同一文を持つが、造り手の数字は `113 ha 植栽 / 約 100 ha 生産`（旧サイト）・`104 ha en production`（2016 フィッシュ）・`a hundred hectares`（OnePager）の 3 通りである。103 はどれでもない。**

⚠️ 🔴 **④ 「2 で終る年は造らないジンクスがある」と言わない。**
**造り手自身の非生産年リストは `1910, 1915, 1930, 1951, 1952, 1964, 1972, 1974, 1992, 2012` の 10 年で、6 年は 2 で終らない。canonical の `yquem-2022` にある「ジンクス」表現は造り手の言い方ではない。**

⚠️ 🔴 **⑤ `Château Lamothe` と `Château Lamothe-Guignard` を同じものとして扱わない。同じコミューンに `Château d'Arche`・`Filhot`・`de Malle`・`Guiraud`・`Raymond-Lafon`・`Cherchy-Commarque` もある。「ソーテルヌの」だけでは特定できない。**

⚠️ 🔴 **⑥ `Y`（Ygrec）を「ソーテルヌの辛口」と言わない。「セカンドワイン」とも言わない。**
**残糖 7 g/L は AOC Sauternes の下限 45 g/L を満たさない。造り手も `a wine in its own right that has succeeded in emancipating itself from Yquem` と書き、セカンドとは呼んでいない。ラベルの AOC 名を確認するまでは、AOC 名そのものを口にしない。**

⚠️ 🔴 **⑦ 「375 mL のこのヴィンテージは DB に登録済みです」と言わない。**
**canonical に容量の軸は無い。2016 と 2010 が `exact` で当たっているのは 750 mL でも 375 mL でも同じレコードだからであって、ハーフボトルとして登録されているからではない。**

⚠️ 🔴 **⑧ canonical の点数・受賞（`96点` `97点` `98点` `99点` `points: 98` `points: 88`）を造り手の言葉として読み上げない。**
**造り手のサイトにもフィッシュの本文にも点数は無い（フィッシュの点数は末尾の第三者引用欄にある別人の言葉である）。**

⚠️ 🔴 **⑨ 2010 について残糖・収穫期間・「パスクィーニが『エレガント』と連発した」を言わない。**
**canonical の `138g/L`・`9月3日〜11月5日`・Pasquini の発言はいずれも裏づけが取れていない。加えて Lorenzo Pasquini は 🏛 登録上 1989 年生の Directeur Général であり、2010 年当時の役職者として造り手の資料に現れない。**

⚠️ **⑩ 「毎年 5〜6 回摘む」を「必ず 5〜6 回」と言い切らない。**
📄 **造り手は `an average of five or six passes` と書き、`in certain years… more than 10 times` と続ける。実測でも 2013 は 4 パス、2016 は 4 パス、2017 は実質 2 期である。**

⚠️ **⑪ 「アルコール 13.5%・残糖 120〜150 g/L」を個々のボトルの値として言わない。**
📄 **これは造り手が示す `The ideal figure` であって実測値ではない。実測は 13.1°〜14.2°、135〜148 g/L と幅がある。**

⚠️ **⑫ ソーテルヌの 2 級の数を「12」とも「15」とも断定しない。**
📄 **造り手の旧サイトは `twelve seconds`、🏛 格付け機関の現行一覧は 15 である。両方あることだけを言う。**

⚠️ **⑬ 「収穫の約半分がブラインドテイスティングで格下げされる」を造り手の言葉として言わない。**
📄 **造り手は選別が行われることを書くが、割合を書いていない。canonical の「約半量」「収穫量の 40% のみ使用」は、2016 フィッシュ末尾の第三者引用欄と、そこに引用された技術部長の発言（`on a éliminé 60%`）に遡る。年ごとの数字であり一般則ではない。**

⚠️ **⑭ 「提供温度 10〜12℃」を造り手の指定として言わない。**
📄 **造り手の指定は `9°C`（若い）／`12°C`（熟成）の 2 段である。canonical の `10–12°C` は 9 件すべてに同じ値が入っている。**

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

🔒 **本節は escalation のみ。`REGISTER.md` は書き換えていない。番号の採否は CTO の判断である。**

### 🔍 canonical の実測（`migration/out/export/db_wine_canonical.json`、928 要素・フィールド名 55 種）

| 走査 | 結果 |
|---|---|
| **全文字列に `yquem` を含むレコード** | 🔍 **18 件** |
| 🔴 **`producer == "Château d'Yquem"` のレコード** | 🔴 **9 件** |
| **prose のみで当たるレコード（`producer` は `Bordeaux`）** | 🔍 **9 件**（`bordeaux-vintage-<年>-guide` 系）→ 🔴 **`D-2026-08-05-08` の誤検出は本件では実害なし** |
| **`vintage == "—"`（U+2014 sentinel）のレコード** | 🔍 **canonical 全体で 328 件。Yquem には 0 件** |
| **`cos-destournel-parker-profile` 型（第三者の château profile をワインとして格納）** | 🔍 **Yquem には該当なし** |

---

### 🔴 ① 網羅の形 —— **4 件の absent as key（gap）と、6 件の「誰も売っていない」**

| ヴィンテージ | canonical | OBP | 判定 |
|---|---|---|---|
| **1984** | ✅ `yquem-1984` | ❌ | **canonical のみ** |
| **2010** | ✅ `yquem-2010` | ✅ $980 | 🔴 **交差（2 件のうち 1）** |
| **2011** | ❌ | ✅ $980 | 🔴 **absent as key ＝ gap** |
| **2013** | ❌ | ✅ $980 | 🔴 **absent as key ＝ gap** |
| **2014** | ❌ | ✅ $980 | 🔴 **absent as key ＝ gap** |
| **2016** | ✅ `yquem-2016` | ✅ $850 | 🔴 **交差（2 件のうち 2）** |
| **2017** | ⚠️ `yquem-ygrec-2017`（**別のワイン**） | ✅ $1,180 | 🔴 **absent as key ＝ gap。かつ false friend** |
| **2019 / 2020 / 2021 / 2022 / 2023** | ✅ 5 件 | ❌ | **canonical のみ** |

🔴 **canonical のみ = `1984, 2019, 2020, 2021, 2022, 2023` の 6 本。**
🔴 **ブリーフは「五つのヴィンテージ」と記すが、実測は 6 である。1984 を数えていないと思われる。ここは訂正が要る。**

🔴 **`D-2026-08-05-14`（Abreu 先例）に従い、この 4 件は conflict ではなく gap として記録する。番号は開かない。**

🔴 **ただし本件の gap には Abreu と違う性質がある —— 4 件すべてについて、造り手自身のフィッシュ・テクニックが分析値まで公表している。**
🔴 **すなわち「造り手の世界に確実に存在するのに canonical に無い」形であり、`unreachable`（別綴りで潜んでいる）ではないことも 928 件走査で確認済みである（`Yquem` の綴り違いレコードは存在しない）。**
→ 🔴 **Batch 10・11 の「メニューが defective とは限らない」に対する 4 件同時の反例。ここではメニューが正しく、canonical が欠けている。**

🔴 **false friend の警告 —— canonical の唯一の 2017 レコードは `yquem-ygrec-2017`（辛口 `Y`）である。**
**OBP の 2017 行は `Sauternes (375 mL) / $1,180` で、残糖 148 g/L のグラン・ヴァンである。**
🔴 **`producer` ＋ `vintage` だけで突合するマッチャーは、この 2 行を高い確信度で結んでしまう。実際に $1,180 の甘口が、生産 1 万本の辛口のレコードに落ちる経路が開いている。**

---

### 🔴 ② `V-2` / `V-3` への証拠 —— **canonical に容量の軸が存在しない**

🔍 **canonical 全 928 件のフィールド名 55 種を列挙した。容量・ボトルサイズを表す型付きフィールドは 1 つも無い。**
（`alc` 6 / `alcohol` 8 / `ph` 1 / `so2` 1 / `soil` 2 / `planting_density` 1 のような希少フィールドは存在するが、容量は無い。）

🔍 **唯一の受け皿は `obp_format`（928 件全件が保持する自由文字列）で、その分布は次のとおり:**

| `obp_format` の値 | 件数 | 備考 |
|---|---|---|
| **`By the bottle`** | **909** | 🔴 **Yquem 9 件はすべてここ** |
| **`BTL 750ml`** | **8** | **容量を書く別綴り** |
| **`By the bottle (Magnum)`** | **4** | **Roederer Cristal 系** |
| **`By the bottle · Magnum`** | **4** | **Dom Pérignon 系** |
| **`By the glass · By the bottle`** | **1** | |
| 🔴 **`By the bottle · Half bottle`** | 🔴 **1** | 🔴 **canonical 全体で唯一のハーフボトル記述（`krug-grande-cuvee-170`）** |
| **`By the glass / By the bottle`** | **1** | |

🔴 **すなわち —— 1 つの軸（容量）が、提供形態を書くための自由文字列の中に、少なくとも 4 通りの綴りで混入している。**
🔴 **「マグナム」だけで 2 綴り（`(Magnum)` と `· Magnum`）、「ハーフボトル」は 928 件中 1 件、「750 ml」は 8 件。残る 909 件は容量について何も言っていない。**

🔴 **Yquem の帰結:**
- **OBP 6 行すべてが `(375 mL)` を名前文字列の中に持つ。**
- **canonical の Yquem 9 件はすべて `obp_format: "By the bottle"` で、375 mL のレコードは 1 件も無い。**
- 🔴 **【intake 層】が `exact` / `confidence 1.0` とした 2 行（2016・2010）が指す【canonical】の `yquem-2016` / `yquem-2010` は、375 mL のボトリングに対応していない。対応しようがない。**
- 🔴 **しかも同じ 2 行には、intake 層が `source_quality_flags: ['format_in_name']` を立てている。すなわち上流は「この行はフォーマットを名前に抱えている」と明示したうえで、下流の canonical にはそれを受け取る欄が無い。**
- 🔴 **同一生産者・同一ヴィンテージの 375 mL と 750 mL は、canonical 上で衝突する。識別子が 1 つしかないからである。**

→ 🔴 **Batch 10 の Roederer マグナム 4 件（うち 3 件は標準ボトルの兄弟レコードを持たない）と同じ族である。`V-2` / `V-3` に本件の証拠を加える。番号は開かない。**
→ 🔴 **本件が Roederer に足す新しい情報は 2 つ —— ①「フォーマットが `name` ではなく `classification_text` 側に入る」経路が実在すること、② **canonical にはハーフボトルの実装例が 928 件中 1 件しか無く、実質的に未実装であること。**

---

### 🔴 ③ `classification` —— **同じ格付けに 2 文字列。うち 1 つはどの一次資料とも一致しない**

| canonical レコード | `classification` | 判定 |
|---|---|---|
| **`yquem-2023` / `-2022` / `-2021` / `-2020` / `-2016` / `-2010`** | **`Sauternes Premier Cru Supérieur`** | ✅ 🏛 **Conseil des Grands Crus Classés en 1855 の公式一覧の文言（`Premier Cru Supérieur`）と一致** |
| 🔴 **`yquem-2019` / `yquem-1984`** | 🔴 **`Sauternes 1er Grand Cru Classé Supérieur`** | 🔴 **矛盾。🏛 格付け機関・✅ 現行サイト・✅ OnePager・📄 旧サイトのいずれの文言とも一致しない** |
| 🔴 **`yquem-ygrec-2017`** | 🔴 **`Sauternes — Dry White`** | 🔴 **法令上ありえない（下記 ④）** |

🔴 **流通している文言は実測で 4 通りある:**
🏛 **`Premier Cru Supérieur`（格付け機関）／✅ `Premier Cru Supérieur`（EN サイト）・`1er Cru Supérieur`（FR サイト）／✅ `Premier Cru Classé Supérieur`（OnePager）／📄 `premier cru supérieur`（旧サイト沿革）。**
🔴 **`1er Grand Cru Classé Supérieur` はこの 4 通りのどれでもない。**
⚠️ **なお同じ文字列（`1er Grand Cru Classe`）を商品名に用いる小売サイトが実在する。canonical の出所として疑わしいが、断定はしない。** → Open Questions 9

**OBP 影響: 0 本**（2019 と 1984 は OBP に無い）。**ただし 9 件中 2 件が誤っているという事実は、生産者頁を生成すれば表に出る。**

---

### 🔴 ④ `yquem-ygrec-2017` —— **法令上ありえない格付け＋ 2 つの言語フィールドが別のワインを記述している**

🔴 **(a) `classification: "Sauternes — Dry White"` は成立しない。**
🏛 **AOC Sauternes CDC: `Tout lot de vin commercialisé (en vrac) ou conditionné présente une teneur en sucres fermentescibles (glucose et fructose) supérieure ou égale à 45 grammes par litre.`**
✅ **造り手の `Y 2016` フィッシュ: `Residual sugar: 7g/L`。**
🔴 **辛口の Y は、定義上 AOC Sauternes を名乗れない。`subregion: "Sauternes"` も同様に、コミューン名としてなら真だがアペラシオンとしては偽である。**

🔴 **(b) `obp_note`（JA）と `obp_note_en`（EN）が別のワインを記述している。**

| フィールド | 内容 | 判定 |
|---|---|---|
| **`obp_note`（JA）** | **`1959年創設の辛口キュヴェ。ソーヴィニヨン・ブラン主体で毎年生産。2004年以降は辛口ワインとして定番化。セカンドワインではなく全く別のコンセプト。生産量1万本。`** | ✅ **ほぼ正しい。📄 造り手の 1959 / 2004 / 予定調和でない位置づけ / 10,000 bottles と一致する** |
| 🔴 **`obp_note_en`（EN）** | 🔴 **`A rare Yquem from a difficult vintage — elevated VA adds complexity rather than fault. RS 109 g/L. Drink now — at its absolute peak… 89 pts.`** | 🔴 **矛盾。`RS 109 g/L` は辛口ワインではありえない（Y 2016 は 7 g/L）。これは甘口の Yquem を記述した文である** |

🔴 **すなわち 1 レコードの 2 つの言語フィールドが、別々のワインを指している。これは「翻訳のずれ」ではなく「別レコードの内容の混入」である。**

⚠️ **`grapes: ["Sauvignon Blanc 75%", "Sémillon 25%"]` は、✅ `Y 2016` フィッシュの `75 % Sauvignon / 25% Sémillon` と数字が完全に一致する。**
⚠️ 🔴 **ただしレコードは 2017 である。2017 の Y の比率を述べる一次資料には到達していない。📄 造り手は `The final blend is made after tasting` と書き、年ごとに変わることを明言している。**
→ ⚠️ **「隣のヴィンテージの値の流用」の疑いがあるが、断定はしない。** → Open Questions 3

🔴 **`food_pairings` が 9 件すべて同一配列（`Foie Gras` / `Roquefort` / `Fruit Tart` / `Lobster with Cream Sauce`）で、辛口の Ygrec にもそのまま適用されている。**
📄 **造り手自身は `Y` について `A glass of Y and a dish of sushi is a perfect match!` と書く。**

**OBP 影響: 1 行（2017 / $1,180）が、この壊れたレコードに引き寄せられうる。**

---

### 🔴 ⑤ `yquem-2016` / `yquem-2010` の全フィールド照合

🔴 **ブリーフの指示どおり、OBP の 2 行が結ばれる 2 レコードを 1 フィールドずつ突き合わせた。**
**両レコードともフィールド数は 23。うち一次資料に対応物があるのは 19。**

#### 🔴 `yquem-2016` —— **照合 19 / 一致 12 / 矛盾 4 / 層混同・精度不足 3**

| フィールド | canonical | 一次資料 | 判定 |
|---|---|---|---|
| `producer` / `name` | `Château d'Yquem` | ✅ 同一 | ✅ |
| `vintage` | `2016` | ✅ フィッシュ実在 | ✅ |
| `country` / `region` | `France` / `Bordeaux` | 🏛 一致 | ✅ |
| `subregion` | `Sauternes` | 🏛 AOC・コミューンとも一致 | ✅ |
| `color` | `Blanc` | 🏛 `vins tranquilles blancs` | ✅ |
| `classification` | `Sauternes Premier Cru Supérieur` | 🏛 一致 | ✅ |
| `tags` | `["Vintage","Premier Cru Supérieur","Sauternes"]` | 🏛 一致 | ✅ |
| `grapes` | `["Sémillon 75%","Sauvignon Blanc 25%"]` | ⚠️ **フィッシュ p.2 の技術ブロックと第三者引用欄には `75% Sémillon 25% Sauvignon` があるが、シャトー自身の本文は比率を書いていない** | ⚠️ **一致するが層が弱い** |
| 🔴 **`tasting`（数値部）** | 🔴 **`アルコール14.2%、pH 3.90。残糖135g/L`** | ✅ **フィッシュ本文 `Alcohol content: 14.20%Vol. - Residual sugars: 135 g/L … pH: 3.90`** | ✅ 🔴 **3 値とも完全一致。canonical が造り手と合った稀な例** |
| `tasting`（官能部・`97点`） | 評点つき官能記述 | ⚠️ 造り手は点数を出さない | ⚠️ **第三者由来** |
| `tasting_en` | `97 pts` つき | ⚠️ 同上 | ⚠️ **第三者由来** |
| `obp_note` | `10月後半まで待ち続けること`／`収穫量の40%のみ使用` | ⚠️ **待機は ✅ フィッシュ本文と整合。`40%` はフィッシュ末尾の第三者引用欄（Decanter）と、そこに引用された技術部長 Francis Mayeur の `on a éliminé 60%` に遡る** | ⚠️ **層混同（造り手文書だが造り手本文ではない）** |
| `obp_note_en`（`RS 135 g/L`） | `135 g/L` | ✅ 一致 | ✅ |
| `obp_note_en`（`97 pts`） | 評点 | ⚠️ 第三者 | ⚠️ |
| 🔴 **`obp_format`** | 🔴 **`By the bottle`** | 🔴 **OBP 行は `(375 mL)`** | 🔴 **矛盾（②）** |
| 🔴 **`serving_temp`** | 🔴 **`10–12°C`** | 🔴 📄 **`9°C`（若い）／`12°C`（熟成）** | 🔴 **矛盾** |
| 🔴 **`terroir`** | 🔴 **`ソーテルヌのシャトー・ディケム所有の103haの単一畑`** | 🔴 📄 **`113 hectares… only one hundred produce`**／✅ **`104 ha en production`**／✅ **`a hundred hectares`** | 🔴 **矛盾** |
| 🔴 **`terroir_en`** | 🔴 **`Château d'Yquem's 103ha single estate`** | 🔴 同上 | 🔴 **矛盾** |
| `food_pairings` / `glassware` / `indicator` / `id` | — | 一次資料に対応物なし | — **照合対象外** |

#### 🔴 `yquem-2010` —— **照合 19 / 一致 10 / 矛盾 4 / 出典なし 5**

| フィールド | canonical | 一次資料 | 判定 |
|---|---|---|---|
| `producer` / `name` / `vintage` / `country` / `region` / `subregion` / `color` / `type` / `classification` / `tags` | — | 📄 **2010 のミレジム頁が実在し、非生産年リストにも入らない** | ✅ **10 件一致** |
| 🔴 **`grapes`** | 🔴 **`["Sémillon 70%","Sauvignon Blanc 30%"]`** | 🔴 **2010 の比率を述べる一次資料に到達できず。📄 旧サイトの `75% / 25%` は植栽比率であってアッサンブラージュではない** | 🔴 **出典なし（unsourced）** |
| 🔴 **`obp_format`** | 🔴 `By the bottle` | 🔴 OBP 行は `(375 mL)` | 🔴 **矛盾** |
| 🔴 **`serving_temp`** | 🔴 `10–12°C` | 🔴 📄 `9°C` / `12°C` | 🔴 **矛盾** |
| 🔴 **`terroir` / `terroir_en`** | 🔴 `103ha` | 🔴 113 / 104 / 100 | 🔴 **矛盾 ×2** |
| 🔴 **`obp_note`** | 🔴 **`パスクィーニが「エレガント」と連発したヴィンテージ`** | 🔴 **該当する発言の一次資料なし。🏛 Lorenzo Pasquini は 1989 年生で、📄 2016 年時点の旧サイト人物頁（Lurton / Garbay / Depierre / Mayeur）に登場しない** | 🔴 **出典なし** |
| 🔴 **`obp_note_en`** | 🔴 **`RS 138 g/L … 96 pts`** | 🔴 **2010 のフィッシュに到達できず、138 g/L を裏づける一次資料なし** | 🔴 **出典なし** |
| 🔴 **`tasting`** | 🔴 **`残糖138g/L。9月3日〜11月5日、2か月収穫。96点`** | 🔴 **同上。収穫期間も造り手の 2010 頁に書かれていない** | 🔴 **出典なし** |
| `tasting_en` | `96 pts` | ⚠️ 造り手は点数を出さない | ⚠️ **第三者由来** |

🔴 **総計 —— レコード 9 件を検分、うち 2 件を全フィールド照合（各 23 フィールド／照合対象 19）。**
🔴 **`yquem-2016`: 一致 12・矛盾 4・層混同 3。`yquem-2010`: 一致 10・矛盾 4・出典なし 5。**
🔴 **加えて 9 件横断で `terroir` / `terroir_en` / `serving_temp` / `glassware` / `food_pairings` が全件同一文字列である（Roederer の `house_style` 16 件複製・Allemand の `description` 5 件複製と同型）。**
🔴 **そのうち `terroir` は造り手と矛盾しており、`food_pairings` は辛口の Ygrec にも甘口の組合せがそのまま適用されている。**

⚠️ **他の 7 件で見つけた矛盾（OBP 影響ゼロだが記録する）:**
- 🔴 **`yquem-2019` / `yquem-1984` の `aging: "36+ months barrel"` と `winemaking: 36ヶ月以上の新樽熟成` は、📄 造り手の `the ageing cellar where they will stay for twenty months` ＋ `bottled during the third winter after the harvest` と矛盾する。**
- ⚠️ **同 2 件の `dosage: "N/A — Still Wine"` は、スティルワインにシャンパーニュ用フィールドが漏れている形である。**
- 🔴 **`yquem-2022.obp_note` の「2 で終るヴィンテージのジンクス」は、📄 造り手の 10 年リスト（6 年が 2 で終らない）と整合しない。**
- ✅ **`yquem-2023` は例外的に合っている —— `grapes: ["Sémillon 70%","Sauvignon Blanc 30%"]` と `残糖153g/L` は、✅ `2023.yquem.fr` および ✅ `CY2023_VintageCard_EN.pdf` の `70% Sémillon / 30% Sauvignon Blanc` `Residual sugar 153 g/L` と完全一致する。**
→ 🔴 **すなわち base rate（14 軒中 13 軒で失敗）は本件でも維持されるが、「全滅」ではない。最新ヴィンテージの、造り手が現に公開している数値だけが正しい。**
→ 🔴 **これは示唆的である —— canonical の誤りは「造り手が公開をやめた期間」に集中している。** → §Open Questions 10

---

### 🔴 ⑥ intake 層 → store 層の伝播損失 —— **フラグは立っている。落ちるのは次の層である（未採番の形）**

🔴 **本節の数値は 4 つの成果物に分かれる。層を混ぜないため、すべての件数に成果物名を併記する。**

| 層 | 成果物 | 本件の 6 行がそこでどう見えるか |
|---|---|---|
| 🔴 **intake** | 🔍 **`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）** | 🔴 **6 行とも `source_quality_flags: ['format_in_name']`。`match_state` / `confidence` も同ファイルにあり、2016・2010 が `exact` / `1.0`、2017・2014・2013・2011 が `unresolved` / `0.0`** |
| **store（転記）** | 🔍 **`research/out/t-01/inventory.json`（768 行）** | 🔍 **`product_name` は 6 行とも `""`、`classification_text` が 6 行とも `Sauternes (375 mL)`。**⚠️ **同ファイルの `flags` は corpus 全行で `[]` であり、これは intake 層の `source_quality_flags` とは別のフィールドである（store 層の空値をもって intake 層の検知の有無を論じてはならない）** |
| **store（解決）** | 🔍 **`research/out/t-01/mapping.json`** | 🔍 **6 行とも `resolved_to: "research_shell"` / `shell_id: "rs:pro:434164aa9498d56f"` / `canonical: {"producer": "producer:chateau-d-yquem"}`。この層には `match_state` / `confidence` の欄が無い** |
| **store（shell）** | 🔍 **`research/store/t-01/shells.json`（1047 shell）** | 🔴 **6 行が 1 shell に畳まれている（下記）** |
| **報告** | 🔍 **`~/Desktop/theseus_gap_report_20260804.md`（822–826 行）** | **2017・2014・2013・2011 の 4 行を「DB 保有年に無い」として列挙し、2016・2010 を列挙しない。intake 層の `match_state` と整合する** |

#### 🔴 (a) intake 層 —— **フォーマットは検知されている。しかも Yquem がその母集団の全部である**

🔍 **【intake 層】`obp_intake_normalized_20260804.json` の `source_quality_flags` 語彙と発火数（704 行中）:**
**`missing_price` 28 ／ `producer_spelling` 13 ／ `cross_section_duplicate` 8 ／ `cuvee_spelling` 7 ／ `canonical_model_note` 6 ／ 🔴 **`format_in_name` 6** ／ `disgorgement_in_name` 4 ／ `section_colour_conflict` 3 ／ `section_region_conflict` 2 ／ `malformed_vintage` 2 ／ `disgorgement_unknown` 1。**

🔴 **【intake 層】`format_in_name` の 6 件は、704 行中の Château d'Yquem の 6 行と完全に一致する。**
🔴 **すなわち本生産者は「フォーマットが名前文字列に紛れ込む」という形の corpus 唯一の実例であり、この語彙の母集団そのものである。**
🔍 **【intake 層】ただし文字列が入っているのはキュヴェ名欄ではなく格付け欄（store 層の転記では `classification_text`）である。フラグ名は `format_in_name` だが、実体は `format_in_classification` に近い。** → §Open Questions 11

#### 🔴 (b) store 層 —— **フラグの対象軸もヴィンテージ軸も、shell に渡っていない**

🔍 **【store 層】`research/store/t-01/shells.json` の `rs:pro:434164aa9498d56f`:**
```
level: "product" / identity_basis: "source_exact" / status: "research_pending"
canonical: { producer_id: "producer:chateau-d-yquem" }
source_transcription: { vintage_text: "2017", classification_text: "Sauternes (375 mL)", source_line_no: 706, … }
source_lines: [706, 707, 708, 709, 710, 711]   ← 6 本
```
🔴 **【store 層】3 つの異なる価格（$1,180 / $850 / $980×4）と 6 つの異なるヴィンテージが、1 個の product shell を共有している。**
🔴 **【store 層】`source_transcription` は 706（2017）しか保持しておらず、残る 5 ヴィンテージは `source_lines` の生文字列としてしか残っていない。ヴィンテージは shell の identity に入っていない。**
🔍 **【store 層】1047 shell 中、複数の `source_line` を持つのは 141 件。`identity_basis` は 1037 件が `source_exact`、10 件が `source_provisional`。**

#### 🔴 (c) 形の名前 —— **intake↔store 乖離の 5 例目。かつ最も鋭い**

🔴 **本件は「メニューが悪い」でも「intake が検知に失敗した」でもない。**
🔴 **intake 層はフォーマットの二重符号化を現に検知し、6 行すべてにフラグを立てている。にもかかわらず store 層では、そのフラグが指した軸（フォーマット）も、識別に不可欠なもう 1 つの軸（ヴィンテージ）も、shell の identity から消えている。**

🔴 **既知の intake↔store 乖離としては 5 例目である（Bachelet-Monnot / Clos de Tart / Armand Heitz / Hundred Acre に続く）。**
🔴 **そして 5 例中もっとも鋭い —— 先行 4 例は「上流が気づいていなかったものが下流で失われた」形だが、本件は **上流がすでに名前をつけて警告していた軸が、下流で捨てられている** 形だからである。**

→ 🔴 **これは `V-1`（surrogate key の不在）と根を共有するが層が違う。`V-1` は canonical 側の話で、こちらは store 層の shell identity の話である。**
→ 🔴 **`S-2`（マッチングから不可視）とも近い。`Sauternes (375 mL)` がキュヴェ名欄ではなく格付け欄にあるため、キュヴェ名によるマッチングの入口自体が存在しない。**
→ 🔴 **本ドシエは番号を開かない。形として記述するにとどめる —— **「intake 層でフラグ済みの軸を含め、同一生産者・同一アペラシオン表記の N 行が、価格もヴィンテージも異なるのに 1 product shell に畳まれる」。**⚠️ **`unnumbered — CTO's call`。**

---

## Sources

### 🔴 ⚠️ サイト真正性の事前チェック（`D-2026-08-05-09`）—— **採用 3、層として却下 1、事実源として却下多数**

| ドメイン | 判定 | 根拠 |
|---|---|---|
| ✅ **`www.yquem.fr` / `yquem.fr`** | ✅ **採用（条件 (a) を満たす）** | ✅ **`/mentions-legales` が発行者を `SA du Château d'Yquem, société anonyme au capital de 224 640 Euros, immatriculée au RCS de Bordeaux sous le numéro B384 809 281, siège social Château d'Yquem, 33210 Sauternes` と明記。**<br>🏛 **企業登録の SIREN `384809281`・本店住所 `CHATEAU YQUEM 33210 SAUTERNES` と完全一致。**<br>✅ **ホスティングは `Akamai Technologies SARL / 429 429 269 R.C.S. Paris`（自称と登録番号を併記）。**<br>⚠️ **年齢確認ゲートあり。bot チャレンジには遭遇していない（回避行為なし）。** |
| ✅ **`2023.yquem.fr`** | ✅ **採用** | ✅ **同一発行者・同一 RCS `B384 809 281` を名乗る。造り手の 2023 年ヴィンテージ専用マイクロサイト。フィッシュ PDF `CY2023_VintageCard_EN.pdf` を自ドメインから配布** |
| ✅ 🏛 **`gcc-1855.fr`** | ✅ **採用（格付け機関そのもの）** | 🏛 **`/mentions-legales/` が `Conseil des Grands Crus Classés en 1855 (Médoc & Sauternes), 1, cours du 30 Juillet – 33000 Bordeaux, Siret. 48484166300012, Code APE. 9411Z, TVA FR10 484 841 663` を名乗り、企業登録（SIREN 484841663 / SIRET 48484166300012 / NAF 94.11Z）と完全一致** |
| 🔴 ❌ **`bordeaux-tradition.com`** | 🔴 **著者層としては却下（§2d）。PDF のホストとしてのみ利用** | 🔴 **négociant（Négoce de Vins）。同社のページ本文・商品説明・ブログは 1 語も使っていない。**<br>🔴 **同社がホストする PDF のうち、フッターが `Château d'Yquem 2016  1/6  29/05/2017` 形式でシャトー自身を名乗り、本文が一人称（"we"、"at Yquem"、"the château's work force"）で書かれているものだけを、造り手の署名を持つフィッシュ・テクニックとして採用した。**<br>🔴 **各 PDF の末尾にある `SPECIALISTS ASSESSMENT`（第三者の評言・評点）欄は、造り手の言葉としては採用していない。** |
| ⚠️ ❌ **`lvmh.com` / `www-v2.lvmh.com` / Moët Hennessy** | ⚠️ **未使用（著者層が違う）** | ⚠️ **グループがホストするブランド頁は château 自身の署名層ではない。所有関係は 🏛 企業登録の取締役 4 法人と、✅ 現行サイトフッターの `lvmh.com` リンク、📄 旧サイトの `appointed… by Bernard Arnault and the LVMH group` から取った** |
| 🔴 ❌ **`extranet.inao.gouv.fr/fichier/4-CDC-Sauternes-PNO.pdf`** | 🔴 **意図的に不採用（§2c）** | 🔴 **PNO（異議手続）ドラフト。抹消線つき旧値と新値が抽出テキストで混ざる既知の罠。代わりに `info.agriculture.gouv.fr/gedei/site/bo-agri/…` の consolidated 版を使用し、`%PDF-1.5`・12 頁を実体検証した** |
| 🔴 ❌ **小売・オークション・評論家・アグリゲータ** | 🔴 **事実源として全面却下** | 🔴 **`millesima.fr` / `wineinvestment.com` / `farrvintners.com` / `comptoirdesmillesimes.com` / `thewinecellarinsider.com` / `thewineindependent.com` / `greatbordeauxwines.com` / `wiredforwine.com` / `klwines.com` / `manila-wine.com` / `woodwinters.com` / `lanigan-edwards.com` / `aries-vins.com` / `wineandco.com` / `esow.com` / `maison-wineted.com` / `lagunacellar.com` / `angrywinemerchant.com` / `frw.co.uk` / `wine.qantas.com` / `vinsetmillesimes.com` / `vin-paris.fr` / `vignobletiquette.com` / `sodivin.com` / `chateauloisel.com` / `qualibordeaux.org` / `fgvb.fr`。**<br>🔴 **これらの記述は本ドシエに 1 語も入っていない。`wiredforwine.com` の商品名に現れた `1er Grand Cru Classe` の綴りだけは、canonical の誤文字列の出所仮説として Open Questions 9 に「未検証の第三者主張」として記録した。**<br>🔴 **Wikipedia は使用していない。** |

🔴 **今回、パーキング／偽サイト／同名の別シャトーのドメインは 1 件も掴んでいない。`yquem.fr` は最初の照合で RCS が一致した。**

### ✅ 造り手が現に公開しているもの

- ✅ `https://www.yquem.fr/` ／ `/en` ／ `/mentions-legales` ／ `/en/legal-information`
- ✅ `https://www.yquem.fr/robots.txt` → 🔴 **`Sitemap: http://localhost/sitemap.xml`（ビルド設定の残骸）**
- ✅ `https://www.yquem.fr/sitemap.xml` → 🔴 **URL 6 本のみ。全 `<loc>` が `http://localhost/…`。ワイン頁・ミレジム頁は 1 本も無い**
- ✅ `https://2023.yquem.fr/en`（2023 の気象・収穫日・アッサンブラージュ・分析値・技術チームのノート）
- ✅ `https://2023.yquem.fr/CY2023_VintageCard_EN.pdf`（`%PDF-1.7` 実体検証済み）

### ✅ 造り手の署名を持つフィッシュ・テクニック（**全点 `%PDF` 実体を検証済み**）

| ファイル | 対象 | 本ドシエでの用途 |
|---|---|---|
| ✅ `Yquem-2017-PM-GB.pdf`（`Château d'Yquem 2017  1/4  06/09/2019`） | 🔴 **OBP 1 行目** | **気象・収穫・`14.00%Vol / 148 g/L / 5.6 g/L H2T / pH 3.80 / Sémillon 75% - Sauvignon 25%`** |
| ✅ `Yquem-2016-FT-GB.pdf`（`Château d'Yquem 2016  1/6  29/05/2017`） | 🔴 **OBP 2 行目** | **`14.20%Vol / 135 g/L / 4.8 g/L H2T / pH 3.90`、4 tris、`104 ha en production`** |
| ✅ `Yquem-2014-GB.pdf` | 🔴 **OBP 3 行目** | **`13.5° / 146 g/L / 酒石酸 7.5 g / pH 3.60`、9 週間の収穫** |
| ✅ `Yquem-2013-GB.pdf`（`2013 Vintage  1/3  07/10/2014`） | 🔴 **OBP 4 行目** | **`13.1° / 140 g/L / 4.0 g/L H2SO4`、4 パスの日付** |
| ✅ `Yquem-2011-FT-GB-176.pdf` | 🔴 **OBP 5 行目** | **`13,80% Vol / 144 gr/L / PH 3,85`、`Y` 8/17 開始・貴腐 9/6 開始** |
| ✅ `Y-2016-FT-GB-C0925.pdf` | 🔴 **`Y` の残糖決着** | **`75 % Sauvignon / 25% Sémillon ／ 14.5° ／ Residual sugar: 7g/L ／ AT 4g/L H2SO4`** |
| ✅ `Chateau-dYquem-OnePager-short-ENG-garamond.pdf` | **格付け文言の 3 つ目** | **`the only "Premier Cru Classé Supérieur"`／`a hundred hectares of vineyards`** |
| ✅ `Y-Yquem-2013-PM-GB-C0925-1.pdf` | **参考** | **`Y` の別ヴィンテージ** |

### 📄 造り手の旧サイト（Internet Archive 復元。`✅` とは混ぜない）

- 📄 `http://yquem.fr/fr-en/legal` — 🔴 **アーカイブ頁が同一の `SA du Château d'Yquem / RCS Bordeaux B384 809 281` を名乗ることを確認（アーカイブの帰属確認）**
- 📄 `/fr-en/domain`（畑 113 ha・土壌・排水・微気候・格付けの周辺）
- 📄 `/fr-en/expertise`（栽培・収穫・圧搾・樽内発酵・熟成 20 か月・瓶詰め・容量・環境）
- 📄 `/fr-en/history`（沿革・1855 年の文言）
- 📄 `/fr-en/artisans`（Pierre Lurton / Sandrine Garbay / Antoine Depierre / Francis Mayeur）
- 📄 `/fr-en/y-the-other-exception`（`Y` の全記述）
- 📄 `/fr-en/the-miracle-of-yquem`（The Style of Yquem）
- 📄 `/fr-en/tips/days-without` — 🔴 **非生産年 10 年の列挙**
- 📄 `/fr-en/tips/outsize-bottles` — 🔴 **`0.375 litre` から `15 litre` まで**
- 📄 `/fr-en/tips/9c` — 🔴 **提供温度 9℃／12℃**
- 📄 `/fr-en/tips/every-other-year`（`Y` は 1959 年以来 33 ヴィンテージ）
- 📄 `/fr-en/tips/naturally-versatile` ／ `/fr-en/tips/sushy`
- 📄 `/fr-en/millesimes/yquem/{2010,2011,2012,2013,2014}` — 🔴 **2012 頁が非生産年の列挙を再掲**
- 📄 **CDX 実測: `/fr-en/millesimes/yquem/` は 1893–2014 の 122 年分、`/fr-en/millesimes/y/` は 1959–2015 の 57 年分。2016 以降は 1 件も無い（旧サイトは 2015 年前後で更新停止）**

### 🏛 公的登録・法令一次資料

| 出典 | 取得内容 |
|---|---|
| 🏛 **`recherche-entreprises.api.gouv.fr/search?q=Yquem&per_page=25`** | **138 件。うちソーテルヌの 2 法人を特定、同名の無関係事業者 7 件を除外** |
| 🏛 **同 `?q=SA DU CHATEAU D'YQUEM`** | 🔴 **SIREN 384809281 / SIRET 38480928100015 / NAF 01.21Z / 役員 6（Lurton・Pasquini・LVMH 系 4 法人）・`liste_id_bio: [175057]`** |
| 🏛 **同 `?q=STE CIVILE CHATEAU YQUEM`** | ⚠️ **SIREN 782010888 / SIRET 78201088800017 / gérant Pierre Lurton / 従業員なし / bio 登録なし** |
| 🏛 **同 `?q=chateau&code_commune=33504&activite_principale=01.21Z`** | **コミューン Sauternes のブドウ栽培法人 11 件（同名混同の切り分け）** |
| 🏛 **同 `?q=48484166300012`** | **`CONSEIL DES GRANDS CRUS CLASSES EN 1855` の登録一致（gcc-1855.fr の真正性）** |
| 🔴 🏛 **`opendata.agencebio.org/api/gouv/operateurs/?siret=38480928100015`** | 🔴 **SIRET 完全一致で `nbTotal: 1`。`numeroBio 175057` / Ecocert France / FR-BIO-01 / `ENGAGEE` / `datePremierEngagement 2019-08-12`** |
| 🏛 **`certificat.ecocert.com/entreprise/F7380666-A9D9-4986-BC9E-427EFE4230D2`** | **`Certification Agriculture biologique Europe (EU) 2018/848 [FR]`／`Agriculteur (production végétale), Fabricant & Transformateur`** |
| 🔴 🏛 **`info.agriculture.gouv.fr/gedei/site/bo-agri/document_administratif-1d1c41fa-…/telechargement`** | 🔴 **AOC Sauternes CDC（consolidated、`%PDF-1.5`・12 頁）。色・品種・tries successives・221 g/L・15%/12%・25 hl/ha・45 g/L・coefficient K・熟成期限** |
| 🏛 **`gcc-1855.fr/the-1855-grand-cru-classification/the-gcc-1855-classification-by-appellation/`** | 🔴 **1855 年格付けの公式一覧（アペラシオン順）。Sauternes/Barsac の 27 シャトーを全列挙** |

### 🔍 THÉSEUS 内部（読み取りのみ）

🔴 **層ごとに成果物が違う。件数を引くときは必ず層名を添えること。**

| 層 | 成果物 | 本件で参照した内容 |
|---|---|---|
| 🔴 **intake** | 🔍 **`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）** | 🔴 **Yquem 6 行の `source_quality_flags: ['format_in_name']`、`match_state` / `confidence`、および corpus 全体のフラグ語彙 11 種の発火数。`research/producers/coverage.py` が coverage を計算する入力もこのファイルである** |
| **store（転記）** | 🔍 `research/out/t-01/inventory.json`（768 行中 Yquem 6 行、line 706–711） | `producer_heading` / `classification_text` / `product_name` / `layout` |
| **store（解決）** | 🔍 `research/out/t-01/mapping.json`（同 6 行） | `resolved_to` / `shell_id` |
| **store（shell）** | 🔍 `research/store/t-01/shells.json`（1047 shell） | `rs:pro:434164aa9498d56f` の identity と `source_lines` |
| **canonical** | 🔍 `migration/out/export/db_wine_canonical.json`（928 要素・フィールド名 55 種。**読み取りのみ**） | Yquem 9 件の全フィールド、`obp_format` の全分布、`vintage` sentinel 328 件 |
| **報告** | 🔍 `~/Desktop/theseus_gap_report_20260804.md`（`### D'Yquem` 節、822–826 行） | 4 行を gap として列挙 |

**キャッシュ先**: `research/producers/_sources/chateau-d-yquem/`（gitignored）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🔴 **社名・法人格・資本金・RCS・住所・電話が mentions légales で確定し、🏛 企業登録の SIREN・SIRET・NAF・住所と完全一致。役員 6 名（うち LVMH 系 4 法人）まで登録で取れた。同名の無関係事業者 7 件と、同コミューンの別シャトー 9 軒を切り分けた。**⚠️ **同一敷地の第 2 法人との関係だけが未解明** |
| **Overview** | **High** | 📄 **tries successives・非生産年・樽内発酵という自己規定 3 点が、すべて造り手の記述で取れた** |
| ⚠️ **History** | ⚠️ **Medium-High** | 📄 **1453 / 1593 / 1711 / 1785 / 1788 / 1826 / 1855 / 1914 / 2004 が造り手の沿革頁で取れた。**⚠️ **現行サイトに沿革が無く、2004 年以降（Pasquini の就任年など）が登録の更新日以外で追えない** |
| 🔴 **Location** | 🔴 **High** | 🔴 **AOC Sauternes の法令テキストを consolidated 版で全面取得（色・品種・糖度・収量・残糖下限・coefficient K・熟成期限）。**🔴 **1855 年格付けを格付け機関の公式一覧で確定し、真正性も SIRET で検証した。**⚠️ **面積が造り手内部で 3 通り（113 / 104 / 100）。両論保存** |
| 🔴 **Farming** | 🔴 **Medium-High** | 🔴 **Agence Bio を SIRET 完全一致で引き、`numeroBio` / 認証機関 / `ENGAGEE` / `datePremierEngagement 2019-08-12` まで確定。Ecocert 側のレジストリでも scope を確認した。**🔴 **temporal trap が明確に成立する（OBP 6 本すべてが engagement 前）。**⚠️ **HVE / Demeter の照会先に到達しておらず、「持っていない」とは言えない。栽培実務の記述が 2016 年時点の旧サイト由来** |
| 🔴 **Winemaking** | 🔴 **High** | 📄 **収穫・圧搾・発酵・熟成・瓶詰め・容量・提供温度が、造り手自身の記述で数値つきで揃った。**✅ **OBP 6 本のうち 5 本について、造り手のフィッシュから度数・残糖・酸・pH・パスの日付を機械転記した。**⚠️ **2010 だけ分析値が無い** |
| ⚠️ **Style** | ⚠️ **Medium** | 📄 **造り手の `The Style of Yquem` を全文取得。**⚠️ **しかし OBP の 6 ヴィンテージについて造り手自身の官能ノートが存在しない（フィッシュの官能欄は第三者の引用である）。第三者は使えないので、個別のノートは空である** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **6 行すべてについて「グラン・ヴァンか `Y` か」を決着させた（価格・残糖・フィッシュの実在の 3 点で）。**🔴 **非生産年リストと突き合わせ、6 行に非生産年が無いことを確認。**🔴 **`Y` が AOC Sauternes ではありえないことを法令と造り手の分析値で証明した。**⚠️ **`Y` のラベル上の AOC 名だけが未決着** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **9 件を検分し、OBP に当たる 2 件を 23 フィールド全数照合（照合対象 19）。**🔴 **canonical に容量の軸が無いことを 55 フィールド全列挙と `obp_format` 全分布で実証した。**🔴 **`Sauternes — Dry White` が法令上ありえないことを、CDC の 45 g/L と造り手の 7 g/L で決着させた。**🔴 **intake 側の 1-shell-6-vintage を実測した** |
| 🔴 **Staff Notes** | 🔴 **High** | **芯 3 点＋ must-not-say 14 項目。🔴 canonical をそのまま読むと出る 7 つの嘘（1er Grand Cru Classé / 103ha / 2 のジンクス / 10–12℃ / 138 g/L / Pasquini の 2010 発言 / 375 mL 登録済み）と、現場で出やすい 7 つを塞いだ** |
| **総合** | 🔴 **High — staff-usable。reached_70: YES（~88%）。** | **OBP 6 行のうち 5 行について、造り手自身の分析値・収穫日程・格付けの正式文言をそのまま言える。残る 1 行（2010）も「造られた年である」ことと造り手の散文までは言える。栽培は認証名と登録日を言え、6 本については有機を語らないという安全側の運用が確立している。**<br>**欠けているのは ① 2010 のフィッシュ、② `Y` のラベル AOC、③ OBP 6 本の造り手自身の官能ノート、④ 現行体制（2019 年以降）の一次情報。**<br>**①③④は「言わない」で回避でき、②は物理ラベルで決着する。卓上で嘘をつく経路は塞いである。** |

**reached_70: YES (~88%)。**
⚠️ **なお現行 `yquem.fr` は六形のうち「publishing stopped but site live」に該当する。ワイン頁もミレジム頁も持たない 6 URL のパンフレットで、`sitemap.xml` の `<loc>` が全て `http://localhost/` のまま公開されている。**
**本ドシエの実質は Archive 復元（📄）と、造り手の署名を持つフィッシュ PDF（✅）で成り立っている。この生産者については archive recovery が効く。**

---

## Open Questions

1. 🔴 **【物理ラベル・タスク】`"Y"`（Ygrec）の実ボトル —— ラベルに刷られた AOC 名は何か。**
   🏛 **AOC Sauternes は残糖 45 g/L 以上を要求し、`Y` は 7 g/L である。同 CDC の coefficient K 条項は同一畑で主張できる AOC を `Sauternes` と `Bordeaux` の 2 つに限る。**
   🔴 **しかし造り手のどの資料（旧サイトの `Y` 頁・`Y 2016` フィッシュ）にも AOC 名が書かれていない。ラベルでしか決まらない。**
   🔴 **canonical の `yquem-ygrec-2017.classification = "Sauternes — Dry White"` と `subregion = "Sauternes"` の是正案は、この確認の後でしか書けない。**

2. 🔴 **【物理ラベル・タスク】375 mL の Yquem の実ボトル。**
   **確認すべきは 4 点 —— ① 表ラベルに `37,5 cl` / `375 ml` の容量表示があるか、② 表ラベルの格付け表記が `Premier Cru Supérieur` か `1er Cru Supérieur` か、③ 750 mL 版とラベル意匠が異なるか、④ ロット番号・裏ラベルの表記。**
   🔴 **canonical に容量の軸を追加すべきか（`V-2`/`V-3` の設計判断）は、この観察が入力になる。**

3. 🔴 **【物理ラベル・タスク】OBP 2017 行（$1,180）の実ボトルは、グラン・ヴァンか `Y` か。**
   **価格・残糖・`Sauternes` 表記のいずれもグラン・ヴァンを示すが、canonical の唯一の 2017 レコードは `Y` である。実物で潰しておく価値がある。**

4. 🔴 **`Château d'Yquem 2010` のフィッシュ・テクニックは存在するか。**
   **négociant のホストする 8 点には 2010 が無く（2011・2013・2014・2015・2016・2017・2018・2019 以降はある）、URL 推測 3 パターンは全 404。造り手の旧サイトのミレジム頁は散文のみ。**
   🔴 **これは陰性の証明ではない。造り手に直接 2010 のフィッシュを請求するのが最短。canonical の `138 g/L` はこれが取れるまで裏づけられない。**

5. ⚠️ **有機認証の初認証ヴィンテージはどれか。**
   🏛 **`datePremierEngagement 2019-08-12` は取れているが、「2022 が初の認証ヴィンテージである」と造り手自身が述べる一次資料に到達していない。canonical の `yquem-2022` はそう主張している。**

6. ⚠️ **`SA DU CHATEAU D'YQUEM`（384809281）と `STE CIVILE CHATEAU YQUEM`（782010888）の関係。**
   **同一コミューン・同一代表（Pierre Lurton）・同一 NAF だが SIREN が別で、後者は従業員ゼロ・bio 登録なし。土地保有と operating の分離である可能性が高いが、それを述べる一次資料に到達していない。断定していない。**

7. ⚠️ **ソーテルヌ 1855 年格付けの 2 級は 12 か 15 か。**
   📄 **造り手の旧サイトは `twelve seconds`、🏛 格付け機関の現行一覧は 15 である。**⚠️ **`Romer` / `Romer-du-Hayot`、`Lamothe` / `Lamothe-Guignard`、`Doisy` 系 3 軒の分割が関係している可能性があるが、それを述べる一次資料に到達していない。両論を保存した。**

8. ⚠️ **HVE / Demeter / その他の認証を保有しているか。**
   **企業登録の `liste_rge` は `null` だが、これは環境系の別制度である。HVE のレジストリと Demeter France の照会先に到達していない。**🔴 **「持っていない」とは言っていない。**

9. ⚠️ **canonical の `Sauternes 1er Grand Cru Classé Supérieur` はどこから来たか。**
   ⚠️ **同じ綴り（`1er Grand Cru Classe`）を商品名に使う小売サイトが実在する（未検証の第三者主張として記録するのみ）。canonical の 2 件がそこから流入した可能性はあるが、断定しない。**

10. 🔴 **canonical の誤りが「造り手が公開をやめた期間」に集中しているのは偶然か。**
    🔍 **本件では、造り手が現に公開している 2023 のみが `grapes` も `残糖` も一致し、造り手が沈黙している 2010 は 5 フィールドが出典なしだった。**
    🔴 **他の生産者でも同じ相関があるなら、canonical の品質は「造り手の公開状況」の関数であることになる。これは Batch 全体で測れる仮説である。**

11. 🔴 **【intake 層】`format_in_name` というフラグ名は、実体と合っているか。**
    🔍 **`obp_intake_normalized_20260804.json` で 6 行に立っているフラグ名は `format_in_name` だが、`(375 mL)` が入っているのはキュヴェ名欄ではなく格付け欄である（store 層の転記では `classification_text`、`product_name` は空文字列）。**
    ⚠️ **`format_in_classification` に相当する別の形が、`format_in_name` という 1 つの名前に吸収されている可能性がある。corpus の 6 件がすべて Yquem なので、この 1 生産者だけで名前の妥当性が決まってしまっている。**

12. 🔴 **【intake→store】intake 層が立てたフラグは、store 層にどう伝わるべきか。**
    🔍 **intake 層の `source_quality_flags` に対応する受け皿が store 層に無い（`research/out/t-01/inventory.json` の `flags` は corpus 全行で `[]`）。フラグを store 層へ引き渡す経路が未実装なのか、意図的に切ってあるのかを確認する必要がある。**
    🔴 **これが本件の伝播損失の入口である。**

13. 🔴 **【store 層】`rs:pro:434164aa9498d56f` に 6 ヴィンテージが畳まれている件を、どの層で直すか。**
    🔍 **`identity_basis: source_exact` のまま `source_lines` を 6 本抱えており、ヴィンテージが shell の identity に入っていない。`research/store/t-01/shells.json` の 1047 shell 中 141 件が同型（複数 `source_line`）である。**
    🔴 **intake↔store 乖離の 5 例目（Bachelet-Monnot / Clos de Tart / Armand Heitz / Hundred Acre に続く）。本ドシエは修正案を実行していない。設計判断として CTO に上げる。**

14. ⚠️ **OBP の 2016 行が $850 で、他が $980、2017 が $1,180 である価格構造。**
    **同一容量（375 mL）で 3 段の価格差があり、2016 だけが下に外れている。仕入時期・仕入値・在庫年数のいずれによるものか、店側の情報が要る。**
