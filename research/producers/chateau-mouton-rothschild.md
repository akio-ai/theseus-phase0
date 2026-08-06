# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical にこの生産者のレコードは 3 件（`mouton-rothschild-1855` / `mouton-rothschild-2001` / `mouton-rothschild-1996`）。**
> 🔍 **`producer` フィールド完全一致 3 件 / prose のみの一致 0 件。**
> ⚠️ **`Mouton` 文字列は canonical 全 928 件中 24 件に当たるが、そのうち 21 件は別レコード**
> **（`bordeaux-vintage-*-guide` 13 件・`darmailhac-1855`・`clerc-milon-1855`・`opus-one`・`kapcsandy-state-lane` ほか）。**
> **`D-2026-08-05-08` の部分文字列誤検出は本件で実際に発生する。SIRET で切り分けた。**
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **シャトー自身のサイト `chateau-mouton-rothschild.com`／自社ボトルショットのラベル面**（一次資料）
> `🏛` **公的登録**（recherche-entreprises.api.gouv.fr / Agence Bio / INAO 官報 CDC / INAO 委員会報告 / Légifrance）
> `📄` **Internet Archive 由来**（本ドシエでは使用ゼロ）
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://www.chateau-mouton-rothschild.com/`（EN 原本）**
> 走査元: **`robots.txt` → `sitemap_index.xml`（13 サブマップ）→ `page-sitemap.xml`（952 URL）＋
> `vintage-sitemap.xml`（23）＋ `vin-sitemap.xml`（23）＋ `etiquette-sitemap.xml`（24）**
> 併用: ✅ **公式ヴィンテージ・ページ 6 点（1996 / 2001 / 2009 / 2010 / 2015 / 2019 ＝ OBP 6 行の全ヴィンテージ）**
> 併用: ✅ **公式ボトルショット 5 点（Mouton 2019・Mouton 2001・Mouton 1996・Aile d'Argent 2019・Le Petit Mouton 2015）のラベル面を実読**
> 併用: 🏛 **INAO CDC「Pauillac」2 版（PNO 版と BO 官報の consolidated 版）／INAO 委員会報告 `CNAOV-2016-428`（112 頁）**
>
> ---
>
> 🔴 **① OBP 6 行の `Pauillac` は「グラン・ヴァン」と断定できない。ただし「白ではない」ことは証明した。**
> 🔴 ✅ **`Aile d'Argent 2019` の公式ラベルは `Bordeaux / Appellation Bordeaux Contrôlée` と刷っている。`Pauillac` ではない。**
> 🔴 🏛 **AOC Pauillac の cahier des charges は `réservée aux vins tranquilles rouges`（赤の静止ワイン専用）。2 版で相互検証済み。**
> → 🔴 **よって OBP の `Pauillac` 行に白（Aile d'Argent）が入る余地は無い。ブリーフの想定どおりだが、これは仮定ではなく実測で潰した。**
> 🔴 ⚠️ **しかしセカンド `Le Petit Mouton de Mouton Rothschild` は AOC Pauillac であり、
> そのラベルには `MOUTON ROTHSCHILD` の語が大書されている（2015 年ラベルで実読）。**
> → 🔴 **`source_producer_raw = "Mouton-Rothschild"` ＋ `source_wine_raw = "Pauillac"` だけでは、
> グラン・ヴァンとセカンドを区別できない。決着は物理ラベルのみ。** → §Open Questions 1
>
> 🔴 **② 6 ヴィンテージすべてのセパージュを公式で取得した。canonical は 3 件中 3 件で外している。**
> 🔴 ✅ **公式値: 1996 = CS 77 / M 13 / CF 10 ／ 2001 = CS 86 / M 12 / CF 2 ／ 2009 = CS 88 / M 12 ／
> 2010 = CS 94 / M 6 ／ 2015 = CS 82 / M 16 / CF 2 ／ 2019 = CS 90 / M 9 / PV 1。**
> 🔴 **canonical の 1996 は `CS 79 / M 11 / CF 8 / PV 2` —— 4 値すべて誤りで、しかも公式が挙げていない
> プティ・ヴェルドを創作している。canonical の 2001 は `CS 86 / M 8 / CF 4 / PV 2` —— CS だけ当たり、
> メルロ・カベルネフランが誤り、やはりプティ・ヴェルドを創作。** → §Canonical Conflict
>
> 🔴 **③ canonical の `aging: "24 months barrel (new oak 100%)"` は 3 レコード全部に入っており、
> かつ 3 レコード全部で間違っている。公式は `about twenty months`。**
> 🔴 🔴 **しかも同じ `mouton-rothschild-1855` レコードの `obp_note` には「熟成：オーク樽約20ヶ月」と正しく書いてある。**
> **すなわち 1 レコードの内部で、typed field と prose が互いに矛盾している。**
> **Batch 10 の「typed field にも及ぶ」に、`同一レコード内で typed と prose が割れる` という下位形を足す。** → §Canonical Conflict ②
>
> 🔴 **④ アーティスト・ラベル一覧（1973–2023、51 件）は canonical が全件正しい。**
> 🔴 **公式 `label-art` の一覧（1924 ＋ 1945–2023、計 81 件）と 51 件すべてが一致した。**
> **`Batch 8–11 の「canonical は全部間違っている」base rate に対する、明確な反例である。**
> **canonical の失敗は「網羅的な列挙」ではなく「数値スペック」に集中している。** → §Canonical Conflict ⑤
>
> 🔴 **⑤ ラベルには格付が一文字も刷られていない。canonical の `classification` 2 文字列はどちらもラベル由来ではない。**
> 🔴 ✅ **Mouton 1996・2001・2019 の実ラベル 3 本を読んだ。刷られているのは
> `Château Mouton Rothschild` / 年号 / `toute la récolte a été mise en bouteilles au Château` /
> `PAUILLAC` / `APPELLATION PAUILLAC CONTRÔLÉE` / `Baronne Philippine de Rothschild g.f.a` / `PROPRIÉTAIRE`。**
> 🔴 **`Premier Grand Cru Classé` も `1er Cru Classé` も `1855` も、3 本のいずれにも存在しない。**
> 🔴 **この 3 本は 1996–2019 に散らばっており、OBP 6 行のヴィンテージ幅をそのまま覆う。
> すなわち「古いヴィンテージには刷ってあった」という逃げ道も塞がっている。**
> ⚠️ **一方でシャトー自身は EN サイトのタイトルで `Premier Cru Classé`、FR の OG タイトルで `Premier grand cru classé` と、
> 2 通りに書き分けている。どちらか一方に寄せてはならない。** → §Location・§Canonical Conflict ③
>
> 🔴 **⑥ ハイフンの問題は決着した。シャトー自身は `Mouton-Rothschild` と綴らない。**
> 🔴 ✅ **取得した公式ページの散文中に `Mouton-Rothschild`（ハイフンあり）は 0 件。**
> **67 件のヒットはすべて画像ファイル名（`Mouton-Rothschild-bouteille-2001-web1.jpg` 等）である。**
> 🔴 ✅ **ラベル・サイトタイトル・本文はすべて `Château Mouton Rothschild`（ハイフンなし）。**
> 🔴 🏛 **逆に INAO の公式委員会報告は `Mouton-Rothschild en 1973` とハイフンで書く。**
> → 🔴 **`producer` フィールドの `Château Mouton-Rothschild` は行政系の綴りで、造り手の綴りではない。
> 2 件の vintage レコードの `name`（ハイフンなし）のほうが造り手表記に一致する。**
> **canonical は 1 生産者の中で 2 系統を混在させている。** → §Identity・§Canonical Conflict ③
>
> 🔴 **⑦ 「Mouton Rothschild は有機である」も「有機でない」も言ってはならない。SIRET で切り分けた。**
> 🔴 🏛 **グループ会社 `BARON PHILIPPE DE ROTHSCHILD SA`（siège SIRET `45920264400017`）は Agence Bio に登録がある**
> **（`numeroBio 1816`／通称 `LA BARONNIE`／Ecocert France `FR-BIO-01`／`ENGAGEE`／`datePremierEngagement 2019-09-04`）。**
> 🔴 🏛 **しかしシャトーの畑の事業所 —— `enseigne: CHATEAU MOUTON ROTHSCHILD`、SIRET `45920264400033`、
> NAF `01.21Z`、Le Pouyalet-Sud —— を SIRET 完全一致で照会すると `{"nbTotal":0,"items":[]}`。**
> 🔴 **さらに Agence Bio 側が列挙する `lieux d'activité` に Le Pouyalet は入っていない
> （入っているのは Saint-André-du-Bois の Domaine de Maillard、Saint-Laurent-Médoc の Mouton Cadet 醸造センター、
> Pauillac の本社）。すなわち有機の登録はグループの別事業に付いている。**
> 🔴 **加えて OBP の 6 ヴィンテージは 1996–2019 で、`datePremierEngagement 2019-09-04` を全て遡る
> （2019 年の赤の収穫は 9/18–10/5 で、登録日の 2 週間後にすぎない）。温度差の罠がそのまま当たる。** → §Farming
>
> ⚠️ **調査上の制約**
> ⚠️ **① `Légifrance` は Cloudflare の bot チャレンジで直接取得が 403。回避行為はしていない（`D-2026-08-05` の gated 扱い）。**
> **1921 年デクレ第 13 条は `WebFetch` 経由でのみ本文を得た。1973 年の昇格デクレの原文そのものには到達できていない。**
> ⚠️ **② 公式サイトは 952 頁ある。本ドシエが実読したのは約 25 頁である。「公式に記載が無い」はすべて
> `取得した範囲に無い` の意味であり、全サイトの網羅的な陰性証明ではない。**
> ⚠️ **③ 公式は栽培・認証について何も書いていない。13 語（HVE / biodynamie / organic / durable / Terra Vitis 等）の
> 検索結果が取得全頁で 0 件。これは「書いていない」の実測であって、「やっていない」ではない。**

---

## Identity

🔴 **最初に押さえるべきこと —— `Château Mouton Rothschild` という名の法人は存在しない。**
**シャトーは 2 つの法人にまたがる「銘柄かつ事業所」であり、その 2 つは SIRET で完全に分離できる。**

| | |
|---|---|
| **OBP 印字** | 🔍 **`Mouton-Rothschild`**（`source_producer_raw`。全 6 行で同一） |
| 🔴 **公式表記（造り手自身）** | 🔴 ✅ **`Château Mouton Rothschild`（ハイフンなし）**<br>✅ **ラベル面（2019・2001 の 2 本で実読）／EN サイトタイトル `Château Mouton Rothschild - Premier Cru Classé, Bordeaux` ／全ページ本文** |
| 🔴 **行政系の表記** | 🔴 🏛 **`Mouton-Rothschild`（ハイフンあり）。**INAO 委員会報告 `2016-CN428` 本文: 「**Avec aujourd'hui 18 crus classés (dont les premiers Lafite-Rothschild, Latour en 1855 et `Mouton-Rothschild en 1973`)**」<br>🔴 **企業登録の enseigne は `CHATEAU MOUTON ROTHSCHILD`（ハイフンなし・アクセントなし・全大文字）** |
| 🔴 **畑の事業所（🏛 実体）** | 🔴 🏛 **SIRET `45920264400033`／`enseigne: ["CHATEAU MOUTON ROTHSCHILD"]`／NAF `01.21Z`（ブドウ栽培）／`LE POUYALLET-SUD 33250 PAUILLAC`／`état: A`**<br>🔴 **親法人は `BARON PHILIPPE DE ROTHSCHILD SA`（SIREN `459202644`）** |
| 🔴 **運営会社（🏛 ＋ ✅）** | 🔴 ✅ **`Baron Philippe de Rothschild SA`**（`/legal`）<br>✅ **「a French société anonyme with an Executive Committee and a Supervisory Board」／`Share capital: €6,250,000`／`Registered office: rue de Grassi – 33250 Pauillac`／`RCS Bordeaux n° B 459 202 644`**<br>🏛 **SIREN `459202644`／siège SIRET `45920264400017`／NAF `46.34Z`（飲料卸）／企業レベル NAF `11.02B`／`nature_juridique 5599`／`catégorie ETI`／`date_creation 1959-01-01`／事業所 16（開設 15）／`10 RUE DE GRASSI 33250 PAUILLAC`**<br>🔴 **`/legal` の `RCS B 459 202 644` と 🏛 SIREN が完全一致 →（§2a 合格条件 a）** |
| 🔴 **畑の所有者（ラベル記載＝🏛 実体）** | 🔴 ✅ **ラベル最下段: `Baronne Philippine de Rothschild g.f.a` / `PROPRIÉTAIRE`（2019・2001 の両ラベル）**<br>🔴 🏛 **`GROUPEMENT FONCIER AGRICOLE DES VIGNOBLES DE LA BARONNE PHILIPPINE DE ROTHSCHILD`／SIREN `314750274`／SIRET `31475027400016`／NAF `68.20B`（土地賃貸）／`nature_juridique 6534`（GFA）／`date_creation 1979-01-01`**<br>🔴 **登記住所が `CHATEAU MOUTON ROTHSCHILD LE POUYALLET-SUD 33250 PAUILLAC` —— ラベルの記載と登録簿がここで一致する** |
| 🔴 **GFA の gérants（🏛）** | 🔴 🏛 **`SEREYS DE ROTHSCHILD PHILIPPE`／`ÖGREN (SEREYS DE ROTHSCHILD) CAMILLE`／`DELARUE CARON DE BEAUMARCHAIS DE ROTHSCHILD JULIEN`（3 名とも `Gérant et associé indéfiniment responsable`）＋ `DELARUE CARON DE BEAUMARCHAIS JEAN-PIERRE`（`Associé indéfiniment responsable`）**<br>🔴 ✅ **公式の「3 人の子供が共同所有者」（key-date 2014）と、登記の gérant 3 名が完全に一致する** |
| ⚠️ **代表者（公式 vs 公式）** | ⚠️ ✅ **`/legal`: `Chairman and CEO: Philippe Sereys de Rothschild`**<br>⚠️ ✅ **`key-date-2014`: `Philippe, Chairman of the Supervisory Board of Baron Philippe de Rothschild SA`**<br>🔴 **同一サイト内で肩書が食い違う。どちらも公式。両論を保存する。** → Open Questions 6 |
| **執行体制（公式）** | ✅ **`Executive Committee: Véronique Hombroekx, Ariane Khaida and Emmanuel Fourton`／`Publishing Manager: Ariane Khaida`**<br>🏛 **登記の `dirigeants` に `KHAIDA (GUYOT) ARIANE`（Directeur général délégué）・`FOURTON EMMANUEL JÉRÔME JACQUES`（同）・`DELARUE CARON DE BEAUMARCHAIS DE ROTHSCHILD JULIEN GABRIEL`（Vice-Président）を確認。**⚠️ **`Hombroekx` は取得した登記 dirigeants 一覧（8 名分）には現れなかった** |
| **サイトのホスティング／制作** | ✅ **`Systonic, Parc Magellan, 10 rue Thomas Edison, 33600 Pessac`／`Design: AFK-CS, 21 bd Haussmann 75009 Paris, Baron Philippe de Rothschild S.A.`** |
| 🔴 **認証（🏛 有機）** | 🔴 🏛 **シャトーの畑の SIRET `45920264400033` → `{"nbTotal":0,"items":[]}`（有効な陰性）**<br>🔴 🏛 **GFA の SIRET `31475027400016` → `{"nbTotal":0,"items":[]}`（有効な陰性）**<br>🔴 🏛 **親会社 SA の siège SIRET `45920264400017` → `nbTotal 1`（numeroBio 1816）**<br>→ §Farming。**この 3 行を混ぜたら即座に嘘になる。** |
| **canonical id** | 🔍 **3 件**（`mouton-rothschild-1855` / `mouton-rothschild-2001` / `mouton-rothschild-1996`。§Canonical Conflict） |

### 🔴 ⚠️ 同名・近名の別事業者 —— **SIRET で切り分けた**

#### ① **同じ SIREN・同じ住所にいる姉妹シャトー（＝本ドシエの対象ではない）**

🔴 🏛 **`BARON PHILIPPE DE ROTHSCHILD SA`（SIREN 459202644）は、`LE POUYALLET-SUD 33250 PAUILLAC` という
同一住所に、NAF `01.21Z` の事業所を 3 つ持っている。enseigne が唯一の識別子である。**

| 🏛 SIRET | 🏛 enseigne | 判定 |
|---|---|---|
| 🔴 **45920264400033** | 🔴 **`CHATEAU MOUTON ROTHSCHILD`** | 🔴 **本ドシエの対象** |
| ⚠️ **45920264400041** | ⚠️ **`CHATEAU CLERC MILON`** | ⚠️ **別シャトー。canonical に `clerc-milon-1855` が独立して存在する。本ドシエは一切扱わない** |
| ⚠️ **45920264400058** | ⚠️ **`CHATEAU D'ARMAILHAC`** | ⚠️ **別シャトー。canonical に `darmailhac-1855` が独立して存在する。本ドシエは一切扱わない** |

🔴 **`Opus One` は canonical に `opus-one` として独立レコードを持ち、OBP にも独自の行を持つ。本ドシエの対象外であり、
本ドシエは Opus One について一語も検証していない。** ⚠️ **canonical の `mouton-rothschild-1855` は `obp_note` の中で
Opus One と Almaviva の開始年を主張しているが、本ドシエはその 2 件を検証していない。** → Open Questions 8

🔴 **`Mouton Cadet` はグループのブランドであり、シャトーの畑ではない。**
🏛 **Agence Bio が列挙する `lieux d'activité` に `Centre vinicole mouton cadet`（33112 Saint-Laurent-Médoc）が
独立した所在地として現れる。畑（Le Pouyalet）とは別の場所である。**

#### ② **無関係な同名（`D-2026-08-05-08` が実際に当たる例）**

🏛 **ジロンド県（33）× ワイン系 NAF で `MOUTON` を引くと 5 件。うち 4 件は完全な別事業者である。**

| 🏛 SIREN | 名称 | 住所 | 備考 |
|---|---|---|---|
| ⚠️ **412826695** | ⚠️ **`SCEA CHATEAU CROIX MOUTON`** | ⚠️ **`3 CHATEAU MOUTON` 33240 LUGON-ET-L'ILE-DU-CARNAY** | 🔴 **住所そのものが「Château Mouton」。文字列一致で最も危険。Pauillac ですらない（右岸側）** |
| ⚠️ **433096971** | ⚠️ **`YVES BLONDY`** | ⚠️ **`LE POUYALET 4 LA FON DE MOUTON` 33250 PAUILLAC** | 🔴 **同じ集落（Le Pouyalet）の別事業者。地名で切ると誤爆する** |
| **388108532** | **`EARL MOUTON DE BEAUCAILLAT`** | **33230 MARANSIN** | 別事業者 |
| **805375722** | **`LE MOUTON NOIR GIROND'1`** | **33390 ANGLADE** | 別事業者 |

🔴 **さらに canonical 内部でも、`Mouton` 文字列は `bordeaux-vintage-1964-guide` 以下 13 件のヴィンテージ解説記事に当たる。**
**これらは生産者レコードではない。SIRET でも `producer` フィールドでも切り分けられる。** → §Canonical Conflict ①

---

## Overview

✅ **シャトー・ムートン・ロートシルトはポイヤックにある。畑は「Plateau de Mouton」と呼ばれる海抜 27 m の小丘の上に広がる。
1853 年、英国分家の Nathaniel de Rothschild 男爵が `Château Brane-Mouton` を競売で取得し、以後シャトーは彼の名を帯びた。
1922 年、Nathaniel の曾孫 Baron Philippe de Rothschild が 20 歳そこそこで経営を握り、生涯をこの地に捧げた。**

🔴 ✅ **シャトー自身が自らの署名として名指しするものは、はっきりしている。**

🔴 ✅ **① カベルネ・ソーヴィニヨンの卓越。**
「**ポイヤック —— カベルネ・ソーヴィニヨンが 19 世紀初頭にこの地に初めて植えられ、その最も見事な表現に達する場所。**」（`/the-vineyard/the-terroir`）
「**しかしカベルネ・ソーヴィニヨンは常に支配的である。ムートンに豊かなタンニン、香りと風味の豊穣さ、そして熟成能力を与えるのはカベルネ・ソーヴィニヨンである。
一方でメルロは、切り離せない伴侶として、しなやかさ、丸み、そして並外れた余韻をもたらす。**」（`/the-vineyard/from-vine-to-wine`）

🔴 ✅ **② 1945 年以来、毎ヴィンテージのラベルが同時代の芸術家の作品で飾られていること。**
「**連合国の勝利を祝い、自らの領地への帰還を記すため、Baron Philippe は画家 Philippe Jullian にムートン・ロートシルトのラベルを描かせる。
勝利の `V` がボトルに現れ、万人の喝采を浴びた。以来、各ヴィンテージのラベルは、
ムートンのために同時代の芸術家が特別に制作したオリジナル作品の複製で飾られている。**」（`key-date-1945`）

🔴 ✅ **③ 1973 年の昇格。**
「**Baron Philippe の長い闘いののち、Château Mouton Rothschild は `Premier Cru Classé`（Classified First Growth）の地位を得る ——
1855 年の格付けにおいて不当に奪われていた地位である。当時の農業大臣 Jacques Chirac が署名したデクレを経て、
ムートンは、事実上長年属していたエリートに正式に加わった。**」（`key-date-1973`）

🔴 ✅ **④ シャトー自身が掲げる標語は「わたし、ムートンは変わらない」である。**
「**ヴィンテージごとに異なりながら常に同じ —— その伝説的なカシスの風味が証人である —— そして常に頂点にある。
シャトーはその標語 `I, Mouton, do not change` に完全に値する。**」（`/the-vineyard/the-skills`）

⚠️ 🔴 **より有名な「Premier je suis, second je fus, Mouton ne change」の全文は、
取得した公式ページのどこにも現れなかった。**
🔴 **canonical はこれを「名言」として日英両方で引用しているが、本調査では造り手の一次資料で裏づけられていない。** → §Staff Notes ⚠️ ⑤

🔍 **THÉSEUS における状態は、Batch 11 までの典型とはやや異なる。
canonical はこの生産者について 3 レコードを持ち、そのうち 2 件は OBP の 2 行と `exact / confidence 1.0` で当たっている。
だが本調査の結論は、その `exact` が「何が正しいか」を一切保証していない、というものである
（数値スペックが 3 件中 3 件で公式と食い違う）。同時に、アーティスト一覧 51 件は全件正しい。
すなわち本件の主題は `矛盾 か 不在 か` ではなく、`同一レコード内で正しい部分と誤った部分が同居している` ことである。**

---

## History

✅ **公式沿革は `/the-history/key-dates`（16 の年）と `/the-history/the-history-of-mouton`（3 章）に分かれる。**

| 年 | 出来事 ✅ |
|---|---|
| **18 世紀** | ✅ **`Lafite`・`Latour` とともに「ブドウの君主」`Marquis Nicolas-Alexandre de Ségur` の所有。次いで `Barons de Brane`** |
| 🔴 **1853** | 🔴 ✅ **`Baron Nathaniel de Rothschild`（1812-1870、英国分家）が `Château Brane-Mouton` を競売で取得。**「**自らの賓客に自らのワインを供したいと願って**」。**「シャトーは以後、彼の名を帯びる —— `Château Mouton Rothschild`」** |
| ⚠️ **1855–1922** | ⚠️ ✅ **「ワインの質がますます認められていたにもかかわらず、ムートンは所有者たちの関心をほとんど惹かなかった —— 当時なお顧みられなかった地方へ旅する気になれなかったのである」** |
| 🔴 **1922** | 🔴 ✅ **`Baron Philippe de Rothschild`（1902-1988）、Nathaniel の曾孫。「かろうじて 20 歳」で経営を掌握** |
| 🔴 **1924** | 🔴 ✅ **「就任 2 年後、彼は、それまでボルドーのネゴシアンに樽で渡されていたワインを、`すべてシャトーで瓶詰めする` よう強く求める。**<br>**同じ 1924 年、Baron Philippe は `Jean Carlu` にラベルの意匠を依頼するが、時代に先んじたこの試みは繰り返されなかった」** |
| **1926** | ✅ **公式 key-date に存在（本調査では未取得）** |
| **1933** | ✅ **公式 key-date に存在（本調査では未取得）** |
| 🔴 **1945** | 🔴 ✅ **`Philippe Jullian` による勝利の `V` ラベル。**「**以来、各ヴィンテージのラベルは同時代の芸術家のオリジナル作品で飾られる**」 |
| **1962** | ✅ **文化大臣 `André Malraux` が `Museum of Art in Wine` を開館。Baron Philippe と 2 番目の妻 Baroness Pauline の構想。Grand Chai に隣接** |
| 🔴 **1973** | 🔴 ✅ **`Premier Cru Classé` への昇格。「当時の農業大臣 `Jacques Chirac` が署名したデクレを経て」**<br>🔴 🏛 **INAO 委員会報告 `2016-CN428`（2016-11-23）が独立に確認: 「`Mouton-Rothschild en 1973`」** |
| **1981** | ✅ **公式 key-date に存在（本調査では未取得）** |
| 🔴 **1988** | 🔴 ✅ **Baron Philippe 逝去。娘 `Baroness Philippine de Rothschild`（1933-2014）が継承。**「**著名な女優であった彼女は、父の仕事を継ぐために舞台の経歴を終える決断に躊躇しなかった。彼女は家族企業 Baron Philippe de Rothschild SA の監査役会長となる**」 |
| 🔴 **1991** | 🔴 ✅ **`Aile d'Argent` の最初のボトル。**「**1980 年代初頭に白ブドウ品種を植えた、ムートン・ロートシルトの畑の 7 ヘクタール（20 エーカー）から生産される**」 |
| 🔴 **1993** | 🔴 ✅ **Baroness Philippine がセカンドワイン `Le Petit Mouton de Mouton Rothschild` を創出** |
| **2003** | ✅ **公式 key-date に存在（本調査では未取得）**⚠️ **ラベル一覧では `150th Anniversary`。1853 年取得の 150 周年と整合する** |
| **2006** | ✅ **公式 key-date に存在（本調査では未取得）** |
| **2012** | ✅ **公式 key-date に存在（本調査では未取得）** |
| 🔴 **2014** | 🔴 ✅ **Baroness Philippine 逝去。**「**いまや 3 人の子 `Camille Sereys de Rothschild`・`Philippe Sereys de Rothschild`・`Julien de Beaumarchais de Rothschild` が `シャトーの共同所有者` として…** `Philippe` は `Baron Philippe de Rothschild SA` の監査役会長」<br>🔴 🏛 **この 3 名が、ラベルに `PROPRIÉTAIRE` として刷られる GFA の gérant 3 名と完全に一致する** |

⚠️ **1926 / 1933 / 1981 / 2003 / 2006 / 2012 の 6 つの key-date は、公式に存在するが本調査では本文を取得していない。**
**「公式が沈黙している」ではなく「本調査が読んでいない」である。** → Open Questions 7

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Bordeaux — Médoc** ✅ |
| 🔴 **Appellation** | 🔴 ✅ **`Pauillac`。ラベル面に `PAUILLAC` ／ 2001 年ラベルには `APPELLATION PAUILLAC CONTRÔLÉE` も刷られている** |
| 🔴 **Commune / 所在** | 🔴 🏛 **`LE POUYALLET-SUD 33250 PAUILLAC`（畑の事業所 SIRET `45920264400033` の登記住所）**<br>🏛 **GFA の登記住所は `CHATEAU MOUTON ROTHSCHILD LE POUYALLET-SUD 33250 PAUILLAC`**<br>✅ **運営会社の登記本社は `rue de Grassi 33250 Pauillac`（＝畑ではない）** |
| 🔴 ⚠️ **面積** | 🔴 ⚠️ **公式が同一ページ内で 2 つの数字を出す。**<br>✅ **スライダー見出し: 「Château Mouton Rothschild spans `84 hectares (207 acres)` of vines」**<br>✅ **本文: 「Château Mouton Rothschild spans `90 hectares (222 acres)` of vines」**<br>🔴 **どちらも `/the-vineyard/the-terroir` の同じ HTML に存在する。造り手が自分と食い違っている。両論を保存する** → Open Questions 2 |
| 🔴 **標高・地形** | 🔴 ✅ **「`Plateau de Mouton` と呼ばれる小丘の上に大部分が位置し、海抜 `27 m` に達する」**<br>✅ **「地形は一般に 40 m 未満の小丘の連なりで、緩斜面が自然な排水と日照を助ける」**<br>✅ **「`Mouton` はおそらく動物ではなく、`motte` あるいは `mothon` —— 隆起や塚を意味する古フランス語 —— に由来する」** |
| 🔴 **土壌** | 🔴 ✅ **「砂利 —— 太陽の熱を保つ石と小石 —— に砂といくらかの粘土が混ざる。薄く痩せた砂利質の土壌が、`粘土石灰質の基盤` の上に数メートルにわたって続く」** |
| 🔴 **植栽（畑全体の比率）** | 🔴 ✅ **`Cabernet Sauvignon 81% / Merlot 15% / Cabernet Franc 3% / Petit Verdot 1%`**<br>🔴 ✅ **「これらの比率はワインにそのまま反映されない。`アッサンブラージュはヴィンテージごとの性格に応じて変わる` からである」**<br>🔴 **この一文が、なぜ canonical の生産者レベルの `grapes` が原理的に成立しないかを説明している** |
| 🔴 **植栽密度・樹齢** | 🔴 ✅ **`10,000 vines per hectare`／`average age of the vines is around 44 years`** |
| 🔴 **AOC の法的性質（🏛）** | 🔴 🏛 **「`L'appellation d'origine contrôlée « Pauillac » est réservée aux vins tranquilles rouges.`」**<br>🔴 **2 版で相互検証: ① INAO extranet `PNOCDCPauillac.pdf`（PNO 版、17 頁、`%PDF` 実体確認）／② BO du MAA `2017-12-07` 公表の consolidated 版（16 頁、`%PDF` 実体確認）**<br>🏛 **「初めに `décret du 14 novembre 1936` により認められた」／CDC は `décret n° 2011-1746 du 1er décembre 2011`（`décret n°2012-1308 du 26 novembre 2012` および `arrêté du 22 novembre 2017` により改正）で homologué** |
| 🔴 **AOC の地理的範囲（🏛）** | 🔴 🏛 **「収穫・醸造・熟成は Pauillac 市の territoire、および付表に示された `Cissac-Médoc`・`Saint-Estèphe`・`Saint-Julien-Beychevelle`・`Saint-Sauveur` の区画で行われる」**<br>🏛 **区画境界の承認は comité national の `1997-11-06` および `2016-11-23` の会期による** |
| 🔴 **AOC の認可品種（🏛）** | 🔴 🏛 **`cabernet franc N, cabernet-sauvignon N, carmenère N, cot N (ou malbec), merlot N, petit verdot N`**<br>🏛 **最低植栽密度 `7 000 pieds/ha`（→ ムートンの 10,000 本/ha は法定下限を大きく上回る）** |
| 🔴 **AOC 内の位置づけ（🏛 ＋ ✅）** | 🔴 ✅ **「Pauillac の約 `1,200 ヘクタール` は、`Premiers Crus Classés du Médoc et de Graves` 5 つのうち 3 つ —— Lafite・Latour・Mouton —— を含む。その輝かしい三者を、1855 年格付の 60 のメドックのシャトーのうち 15 が取り囲む」**（＝計 18）<br>🔴 🏛 **INAO `2016-CN428`: 「`Avec aujourd'hui 18 crus classés`… cette commune compte le plus grand nombre de crus classés」——`18` で公式と INAO が一致する** |

### 🔴 格付の表記 —— **ラベルは沈黙し、サイトは 2 通りに書く**

| 出典 | 実際の文字列 |
|---|---|
| 🔴 ✅ **ボトルのラベル（1996・2001・2019 の 3 本）** | 🔴 **3 本とも格付の表記なし。`Premier Grand Cru Classé` も `1er Cru Classé` も `1855` も刷られていない** |
| ✅ **EN サイト `<title>`** | **`Château Mouton Rothschild - Premier Cru Classé, Bordeaux`** |
| ⚠️ ✅ **FR の共有用タイトル（OG）** | ⚠️ **`Château Mouton Rothschild - Premier grand cru classé, Bordeaux`** |
| ✅ **`key-date-1973` 本文** | **`Premier Cru Classé (Classified First Growth)`** |
| 🔴 🏛 **法的根拠（Légifrance、`WebFetch` 経由）** | 🔴 **`Décret du 19 août 1921`（消費法典 L.412-1 の適用）第 13 条 3° b):「`Les vins de Bordeaux provenant de domaines viticoles figurant dans le classement de 1855; Pour l'étiquetage de ces vins, les termes: «cru classé» ou «grand cru classé» peuvent être utilisés`」**<br>🔴 **すなわち `cru classé` と `grand cru classé` は法的にどちらも許される。「Grand が入っているから誤り」ではない。だが `造り手が使う語` でもない** |
| 🔴 ⚠️ **AOC Pauillac の CDC** | 🔴 **CDC の `XII. ― Règles de présentation et étiquetage` は `Pas de disposition particulière`（特段の定めなし）。**<br>🔴 **CDC 本文に `cru classé` も `1855` も一度も現れない。1855 年格付は AOC の cahier des charges の一部ではない** |

→ 🔴 **したがって「ムートンの格付表記」を 1 つの正解に収斂させることはできない。3 系統（ラベル＝無表記／EN＝Premier Cru Classé／FR＝Premier grand cru classé）を並置するのが唯一正しい扱いである。** → §Canonical Conflict ③

---

## Farming

🔴 **本節の要点は 3 つ ——**
🔴 **① シャトー自身は栽培・認証について何一つ公表していない。**
🔴 **② グループ会社には有機登録があるが、その活動場所にシャトーの畑は含まれない。**
🔴 **③ OBP の 6 ヴィンテージは、その登録日を全て遡る。**

### 🔴 ✅ 公式サイトの沈黙 —— **13 語すべてゼロ件**

🔴 **取得した公式ページ全件（約 25 頁、うち `/the-vineyard/the-skills`・`/the-vineyard/from-vine-to-wine`・`/the-vineyard/the-terroir` を含む）に対し、
以下の語を検索した結果はすべて 0 件である。**

`HVE` / `Haute Valeur` / `biodynam` / `biologique` / `organic` / `Terra Vitis` / `Demeter` / `certifi` /
`ISO 14001` / `durable` / `sustainab` / `environnement` / `environment`

⚠️ **これは「取得した範囲に無い」の実測である。サイト全 952 頁の網羅的な陰性証明ではない。**
🔴 **同時に、栽培哲学を語るはずの 3 頁（terroir / from-vine-to-wine / the-skills）にゼロというのは、
このシャトーが認証を売り文句にしていないことを強く示す。**

### 🔴 🏛 Agence Bio —— **SIRET を 4 つ叩いた。3 つが陰性、1 つが陽性**

| 🏛 照会 SIRET | 対象 | 結果 |
|---|---|---|
| 🔴 **`45920264400033`** | 🔴 **シャトーの畑の事業所（enseigne `CHATEAU MOUTON ROTHSCHILD`、NAF `01.21Z`、Le Pouyalet-Sud）** | 🔴 **`{"nbTotal":0,"items":[]}` —— 完全に解決するクエリのゼロ件＝有効な陰性** |
| 🔴 **`31475027400016`** | 🔴 **ラベルが `PROPRIÉTAIRE` と刷る GFA** | 🔴 **`{"nbTotal":0,"items":[]}` —— 有効な陰性** |
| ⚠️ **`45920264400041` / `45920264400058`** | **姉妹シャトー 2 件（対象外だが誤爆防止のため実測）** | **いずれも `{"nbTotal":0,"items":[]}`** |
| 🔴 **`45920264400017`** | 🔴 **親法人 `BARON PHILIPPE DE ROTHSCHILD SA` の siège** | 🔴 **`nbTotal: 1` —— 下表** |

### 🔴 🏛 陽性側の中身 —— **登録簿が言っていることを、そのまま書く**

| 項目 | 🏛 Agence Bio の記載 |
|---|---|
| **raisonSociale** | **`BARON PHILIPPE DE ROTHSCHILD SA`** |
| 🔴 **denominationcourante** | 🔴 **`LA BARONNIE`** |
| **numeroBio** | **`1816`** |
| **codeNAF** | **`11.02B`** |
| **gerant** | **`SEREYS Philippe`** |
| 🔴 **certificats** | 🔴 **`numeroControleEu: FR-BIO-01`／`organisme: Ecocert France`／`etatCertification: **ENGAGEE**`／`dateEngagement: **2021-07-27**`／`dateNotification: 2019-09-04`／`dateSuspension: null`／`dateArret: null`** |
| 🔴 **datePremierEngagement** | 🔴 **`2019-09-04`** |
| **activites** | **`Production`（id 1）＋ `Préparation`（id 2）** |
| 🔴 **categories** | 🔴 **`Grossistes`（卸売）** |
| 🔴 **mixite** | 🔴 **`Oui`（＝有機と慣行の混在事業者）** |
| **annuaireActivites** | **`Viticulture`** |
| **productions** | **`Raisin de cuve`（01.21.12）: `AB` および `CS`、いずれも `anneeReferenceControle 2026`／`Vins de raisin`（11.02）: `AB`、`2026`** |
| 🔴 **lieux d'activité（4 か所）** | 🔴 **① `Le Bourg N`, 33490 **Saint-André-du-Bois**（Lieux d'activité）**<br>🔴 **② `10 RUE DE GRASSI`, 33250 PAUILLAC（Siège social ＋ Lieux d'activité）**<br>🔴 **③ `DOMAINE DE MAILLARD`, 33490 SAINT ANDRE DU BOIS（Lieux d'activité）**<br>🔴 **④ `Centre vinicole mouton cadet`, 33112 Saint Laurent Medoc（Lieux d'activité）** |
| 🔴 **列挙に無い場所** | 🔴 **`Le Pouyalet` / `Le Pouyallet-Sud` / `Château Mouton Rothschild` は 4 か所のいずれにも現れない** |

🏛 **企業登録側の相互参照: SIREN `459202644` の `complements.est_bio: **true**`。
一方 GFA（SIREN `314750274`）は `est_bio: **false**`。**

### 🔴 したがって言えること・言えないこと

🔴 **言ってよい（🏛 登録どおり）** ——
「**このシャトーを運営する会社（Baron Philippe de Rothschild SA）は Agence Bio に登録があり、
Ecocert France による有機の `engagement` 状態にある。登録上の活動場所は Saint-André-du-Bois の Domaine de Maillard、
Saint-Laurent-Médoc の Mouton Cadet 醸造センター、および Pauillac の本社である。**」

🔴 **言ってはならない ①** —— 「**シャトー・ムートン・ロートシルトは有機認証を受けている**」。
**畑の事業所の SIRET も、ラベルに刷られた所有者 GFA の SIRET も、Agence Bio でゼロ件である。**

🔴 **言ってはならない ②** —— 「**ムートンは有機ではない／慣行栽培である**」。
**シャトーは栽培について何も公表していない。実践は不明である。`mixite: Oui` は、
同じ会社の中に有機と非有機が併存することを登録簿自身が認めている、という意味でしかない。**

🔴 **言ってはならない ③（温度差の罠）** —— 「**このボトルは有機だ**」。
🔴 **OBP の 6 ヴィンテージは 1996・2001・2009・2010・2015・2019。
`datePremierEngagement` は `2019-09-04`、`dateEngagement` は `2021-07-27`。**
🔴 **最も新しい 2019 年でさえ、赤の収穫は公式によれば `18 September to 5 October`。
すなわち登録通知日の 2 週間前後であり、しかもその登録は畑の事業所に付いていない。**
**現行の認証は、1996–2019 のどのボトルについても何も語らない。**（Moussé・Giraud・Dauvissat と同型）

### ✅ 公式が実際に書いている栽培・収穫の実務（認証とは別の話）

🔴 ✅ **「ブドウは `手摘み` され、果粒を無傷に保つ `開いた籠（open baskets）` に置かれる。
除梗のあと、`振動テーブル` の上で `手選果` される。この厳格な試験を通ったものだけが可動ビンに移され、
`重力だけの作用で` 発酵槽へ送られる。こうして畑から槽まで、果実はいかなる非自然な圧力も拘束も受けない。**」
✅ **「ブドウ栽培者が `耕し、剪定し、防除し、摘芯し、間引き`、畑長がブドウの成熟を監視し、
カーヴ長が醸造を統括し、技術長が全工程に責任を負ってアッサンブラージュを決める。**」（`/the-vineyard/the-skills`）

⚠️ **除草の方式、防除の薬剤、被覆作物、馬耕、カーボン、灌漑の有無は、取得した公式ページに一切記載が無い。** → Open Questions 3

---

## Winemaking

### 🔴 ✅ 醸造 —— **重力式・木槽 44 基＋ステンレス 20 基**

🔴 ✅ **「技術の最先端にある `重力式（gravity-feed）の醗酵槽室` が、ムートンの歴史の新しい時代を開く。
優美な金属の柱で結ばれた 2 層構造で、木と鋼の調和した結婚のうちに、`オーク槽というムートンの伝統に忠実` であり続ける。
容量の異なる槽は、`ドメーヌの区画それぞれに対応` し、収穫時の選別とワインのアッサンブラージュの双方を最適化する。
ムートンの槽の大多数は `オーク製（44 基。醸造の進行を監視できるよう透明な樽板を備える）` で、
残りは `ステンレス製（20 基）` である。**」（`/the-vineyard/from-vine-to-wine`）

### 🔴 ✅ 熟成 —— **`about twenty months`。canonical の `24 months` はここで落ちる**

🔴 ✅ **「醸造ののち、ワインは `新しいオーク樽（new oak barrels）` で熟成され、
熟成の各段階は `伝統的なメドックの手法` で行われる —— `補酒（topping-up）` を含み、
そして `卵白による清澄（fining with egg-white）`。これは懸濁する粒子を沈殿させることでワインを清澄・安定させるためのものである。
`約 20 か月（about twenty months）` 続く熟成の間に、樽は `Grand Chai` から `2 年目のカーヴ` へ移され、
シャトーでの滞在が終わるまでワインは冷涼に保たれる。**」

⚠️ **公式は `new oak barrels` と書くが、`100%` という語は使っていない。**
🔴 **「新樽 100%」は公式の文言ではない。「新しいオーク樽で熟成される」が公式の文言である。** → §Staff Notes ⚠️ ⑦

### 🔴 ✅ OBP 6 ヴィンテージのセパージュ（**公式ヴィンテージ・ページから機械転記**）

| ヴィンテージ | ✅ 公式 `Varietal mix` | ✅ 公式 `Harvest` | ✅ ラベル画家 |
|---|---|---|---|
| 🔴 **1996** | 🔴 **Cabernet Sauvignon 77% / Merlot 13% / Cabernet Franc 10%**（**PV なし**） | **27 September to 9 October** | **Gu Gan (1942)** |
| 🔴 **2001** | 🔴 **Cabernet Sauvignon 86% / Merlot 12% / Cabernet Franc 2%**（**PV なし**） | **27 September to 10 October** | **Robert Wilson (1941–2025)** |
| 🔴 **2009** | 🔴 **Cabernet Sauvignon 88% / Merlot 12%**（**CF・PV なし**） | ⚠️ **`23 September to 13 October`（表）／本文は「メルロ 9/23 開始、カベルネ・ソーヴィニヨン `6 October` 終了」——**⚠️ **公式内部で不一致** | **Anish Kapoor (1954)** |
| 🔴 **2010** | 🔴 **Cabernet Sauvignon 94% / Merlot 6%**（**CF・PV なし**） | ⚠️ **`29 september to 13 October`（表）／本文は「`28 September` から 13 October」——**⚠️ **公式内部で不一致** | **Jeff Koons (1955)** |
| 🔴 **2015** | 🔴 **82% Cabernet Sauvignon / 16% Merlot / 2% Cabernet Franc**（**PV なし**） | ⚠️ **`14 September to 2 October 2015`（表）／本文は「3 つの estate を通じて 23 日間、最初のメルロ 9/14 から最後のカベルネ・ソーヴィニヨン `6 October` まで」——**⚠️ **本文は 3 シャトー合計の期間である** | **Gerhard Richter (1932-)** |
| 🔴 **2019** | 🔴 **90% Cabernet Sauvignon / 9% Merlot / 1% Petit Verdot** | **From 18 September to 5 October**（赤。白 Aile d'Argent は 9/5 開始・9/11 完了） | **Olafur Eliasson (1967 -)** |

🔴 **6 ヴィンテージのうち、プティ・ヴェルドが blend に現れるのは 2019 の 1 件（1%）のみ。
カベルネ・フランが現れるのは 1996・2001・2015 の 3 件。**
🔴 **すなわち「CS / M / CF / PV の 4 品種がいつも入っている」は、この造り手については誤りである。**

⚠️ **アルコール度数（ラベルに 2001 で読み取れず、Aile d'Argent 2019 は `13,5%vol.`）・
pH・総酸・収量（hl/ha）・生産本数・新樽比率の数値・樽の tonnelier・アッサンブラージュ決定日は、
取得した公式ページに一切記載が無い。** → Open Questions 4

⚠️ **AOC の法定上限（🏛 CDC）: `rendement butoir 60 hl/ha`。これは AOC の上限であって、ムートンの実収量ではない。**

---

## Style

### ✅ 公式テイスティングノート（**OBP 6 行の全ヴィンテージ。すべてシャトー自身の言葉**）

| VT | ✅ 公式ノート（`Tasting notes`、全文） |
|---|---|
| 🔴 **1996** | **「魅力的な赤で、縁がわずかにオレンジに寄る。開いた強度のある香りは、`チェリーやブラックベリーのような黒い果実` の香りに、`シダー材`、`フレッシュなミント`、いくらか `より花的な調子`、そして `完璧に統合された樽` を伴う。**<br>**最初から、満ちた口中が豊満さと魅力的な密度を差し出し、`際立った風味の奥行き` を持つ。厳格な中盤が、`洗練された絹のようなタンニン` の質感を、制御された力の顕示のうちに供し、そののちに `より優しいフィニッシュ` へ向かう。」** |
| 🔴 **2001** | **「ワインは `進化したガーネット・レッド` の色で、輝くハイライトを持つ。**<br>**香りは複雑な果実を示し、`ビルベリーやカシスのような熟した液果` の香りに富み、`煙と革` の心地よい調子と `わずかに動物的な` 傾きを伴う。**<br>**よく構成されたアタックから、丸みを帯びたタンニンに支えられて、`満足のいく密度の風味` が口中に現れ、果実に満ちる。**<br>**フィニッシュは長く優雅で実質に富み、`優れたポテンシャル` を明かす。」** |
| 🔴 **2009** | **「`ほとんど黒い` きわめて深い色で、きらめくハイライトを持つ。**<br>**上品で複雑な香りは広い香りの配列を差し出し、`ビルベリー、カシス、金髪のタバコ` が `繊細なシダー材とスパイス` と混ざり合う。**<br>**口中は直ちにワインの密度と洗練を示す。`きわめて前面に出た熟した果実の風味` が、`貴族的で丸みのあるタンニン` と完璧に統合され、際立った構造と均衡を明かす。**<br>**豊満で長いフィニッシュが、このムートン・ロートシルトの非常な成功を確証する。」** |
| 🔴 **2010** | **「暗く強度のある赤。`カベルネ・ソーヴィニヨンが支配的` で、複雑な香りの配列を示す。**<br>**`軽くトーストしたヴァニラ` の調子から、空気に触れると香りが開き、`とりわけカシスとブラックチェリー` の果実香を展開する。**<br>**アタックは大きな複雑さを示し、`力強くよく統合されたタンニン` が並外れた奥行きと丸みを明かす。`フレッシュでミネラルなフィニッシュ` がこのきわめて優雅なワインを締めくくる。**<br>**ムートン・ロートシルト 2010 は、その `際立った長さと調和` によって際立つ。」** |
| 🔴 **2015** | **「魅力的で深く暗い色に、`紫の色調`。**<br>**洗練され優雅な香りは、`野生のブラックベリーとビルベリー` の果実香を明かす。次いで `トースト、リコリス、金髪のタバコ` の調子が現れ、豊かで複雑な香りの配列を満たす。**<br>**`フレッシュで、コクがあり、わずかに塩味を帯びた` アタックが大きな強度を示し、絹のような質感を包む `なめらかでクリーミーなタンニン` へ開き、`ミネラルのひと触れ` がそれを持ち上げる。**<br>**口中の印象はきわめて満ちており、`熟した果実と胡椒のスパイス` の風味に富む。`並外れて長いフィニッシュ` が、際立って均衡したワインを締めくくる。」** |
| 🔴 **2019** | **「`紫がかった色合いを持つ強度のあるガーネット・レッド`。**<br>**香りはフレッシュで、きわめて表情豊かで精確。`ブラックベリー、ブラックチェリー、リコリス` の香りを `わずかにミネラルな` 傾きとともに明かす。**<br>**口中はなめらかで豊満、`魅力的な甘やかさ` を伴い、`見事に貴族的で丸みがあり力強いタンニン` を包み込む。**<br>**全体に美しく豊かで、`上品で果汁感に富み、きわめて調和のとれたフィニッシュ` に至る。」** |

### 🔴 ✅ 造り手が自分のスタイルをどう語るか

🔴 ✅ **「ヴィンテージごとに異なりながら常に同じ —— その `伝説的なカシスの風味（legendary blackcurrant flavour）` が証人である。」**（`/the-vineyard/the-skills`）
🔴 ✅ **「カベルネ・ソーヴィニヨンがムートンに `豊かなタンニン`、`香りと風味の豊穣さ`、そして `熟成能力` を与える。
メルロは、切り離せない伴侶として、`しなやかさ`、`丸み`、`並外れた余韻` をもたらす。」**（`/the-vineyard/from-vine-to-wine`）

⚠️ 🔴 **公式サイトには点数・受賞・第三者評価が一切掲載されていない。取得した全ページで確認した。**
🔴 **canonical が持つ `points: 94`（2001）／`points: 97`（1996）に、造り手側の裏づけは無い。** → §Canonical Conflict

---

## Important Cuvées

### ✅ 公式の現行レンジ（**全 3 品目。トップナビ `Vintages` の 3 項目と完全に一致**）

| # | 公式のキュヴェ名 | 種別 | 🔴 **appellation（ラベル実読）** | 初ヴィンテージ |
|---|---|---|---|---|
| 1 | 🔴 **`Château Mouton Rothschild`** | 🔴 **グラン・ヴァン（赤）** | 🔴 ✅ **`PAUILLAC` / `APPELLATION PAUILLAC CONTRÔLÉE`** | — |
| 2 | 🔴 **`Le Petit Mouton de Mouton Rothschild`** | 🔴 **セカンド（赤）** | 🔴 ✅ **`PAUILLAC` / `APPELLATION PAUILLAC CONTRÔLÉE`** | 🔴 ✅ **1993**（下記） |
| 3 | 🔴 **`Aile d'Argent`** | 🔴 **白（辛口）** | 🔴 ✅ **`Bordeaux` / `Appellation Bordeaux Contrôlée`** | 🔴 ✅ **1991** |

🔴 **この 3 品目の外に、公式が現在紹介しているワインは無い。**
⚠️ **`Mouton Cadet`・`Opus One`・`Almaviva`・`Domaine de Baronarques` はフッターから外部ドメインへリンクされる
「Baron Philippe de Rothschild の他の estates」であり、シャトーの `Vintages` メニューには入っていない。**

### 🔴 ✅ Aile d'Argent —— **ラベルが `Bordeaux` と刷っている。決着済み**

🔴 ✅ **公式ボトルショット `Aile_Argent_2019_210-210x764.png` のラベル面（実読）:**
**`Aile d'Argent®` / `2019` / 🔴 **`Bordeaux`** / 🔴 **`Appellation Bordeaux Contrôlée`** /
`Toute la Récolte a été produite, vinifiée et mise en Bouteilles à` / `Château Mouton Rothschild` /
`Baronne Philippine de Rothschild GFA — Pauillac - Gironde - France` / `13,5%vol.` / `Produit de France` / `75cl`**

🔴 **すなわちラベルは「Château Mouton Rothschild で造られた」とは書くが、appellation は `Bordeaux` である。**
🔴 🏛 **これは AOC Pauillac の CDC（`réservée aux vins tranquilles rouges`）と完全に整合する。**
→ 🔴 **OBP の `Pauillac` 行に Aile d'Argent が入る可能性は消えた。**

✅ **公式の Aile d'Argent 記述（`/aile-dargent` ＋ `key-date-1991`）:**
「**メドックの祖先伝来の伝統を新たにして、1980 年代初頭、Philippine de Rothschild は畑の数エーカーに白ブドウ品種を植えることを決めた。
`砂質・砂利質の土壌` に `Sauvignon Blanc (53%)`, `Semillon (35%)`, `Sauvignon Gris (11%)`, `Muscadelle (1%)` が
`9,000 vines per hectare` の密度で植えられている。`ワインの 50% が新しいオーク樽で熟成される`。**」
✅ **`key-date-1991`: 「1991 ヴィンテージをもって、Château Mouton Rothschild は Aile d'Argent の最初のボトルに署名する。
この高品質の辛口白ワインは、ムートン・ロートシルトの畑の `7 ヘクタール（20 エーカー）` から生産される。」**
✅ **名の由来（Philippine 自身の文）: 父 Baron Philippe が幼い彼女のために創った、魔法のティーポットを主人公にした童話 `Aile d'Argent`。
獄中で記憶から書き起こされ、`Aile d'Argent la Magique` の題で 1947 年に Gallimard から出版された。**

### 🔴 ✅ Le Petit Mouton de Mouton Rothschild —— **AOC Pauillac。ラベルに `MOUTON ROTHSCHILD` と大書される**

🔴 ✅ **公式ボトルショット `Bouteille_Petit_Mouton_2015_web-210x716.jpg` のラベル面（実読）:**
**`MIS EN BOUTEILLE À LA PROPRIÉTÉ` /（Jean Carlu の赤いブドウ房の意匠）/
🔴 **`LE PETIT MOUTON DE MOUTON ROTHSCHILD`** / 🔴 **`PAUILLAC`** / 🔴 **`APPELLATION PAUILLAC CONTRÔLÉE`** /
`BARONNE PHILIPPINE DE ROTHSCHILD G.F.A.` / `PAUILLAC - GIRONDE - FRANCE - PRODUIT DE FRANCE` / `2015` / `75cl`**

✅ **公式の説明:**
「**例外的なテロワールから生まれる Le Petit Mouton de Mouton Rothschild は、Château Mouton Rothschild の `セカンドワイン` である。
名高い第一級の畑の中で `選ばれた若い樹` のブドウから造られ、同じ細心の注意をもって収穫され、醸造され、瓶詰めされる。
小さな開いた籠で収穫され、`ムートンのオーク槽` で発酵され、伝統的な方法で `オーク樽` で熟成される。**」
🔴 ✅ **「`最初のヴィンテージである 1993 年は Le Second Vin de Mouton Rothschild と呼ばれた` が、
`翌 1994 年から` その決定的な名（Petit Mouton は estate の中心にある Baroness Philippine の住居の名でもある）を帯びている。」**
✅ **ラベル意匠は、ポスター画家 `Jean Carlu` の素描にもとづく。「1927 年に作られたもので、
同時期に同じ画家が `Château Mouton Rothschild 1924` のラベルのために描いた意匠に続くものである」**

🔴 **セカンドのラベルは、グラン・ヴァンと 3 点で見分けられる ——**
🔴 **① 上段の帯（アーティストの原画）が無い。② `MIS EN BOUTEILLE À LA PROPRIÉTÉ`（グラン・ヴァンは `Toute la récolte a été mise en bouteilles au Château`）。
③ 名称が `LE PETIT MOUTON DE MOUTON ROTHSCHILD` の 3 行組。**

### 🔴 ✅ アーティスト・ラベル（**公式 `label-art` の全一覧を実読。1924 ＋ 1945–2023 の計 81 エントリ**）

🔴 **OBP 6 行のヴィンテージの画家は、いずれも公式に名指しされている。**

| VT | ✅ 公式が名指しする画家 |
|---|---|
| 🔴 **1996** | 🔴 **Gu Gan（顧剛）(1942)** |
| 🔴 **2001** | 🔴 **Robert Wilson (1941 – 2025)** |
| 🔴 **2009** | 🔴 **Anish Kapoor (1954)** |
| 🔴 **2010** | 🔴 **Jeff Koons (1955)** |
| 🔴 **2015** | 🔴 **Gerhard Richter (1932-)** |
| 🔴 **2019** | 🔴 **Olafur Eliasson (1967 -)** |

⚠️ 🔴 **公式一覧には「同時代の芸術家」ではないエントリが 4 つある ——
`1953: Centenary year` / `1977: Tribute to HM Queen Elizabeth the Queen Mother` /
`2000: The Augsburg Ram` / `2003: 150th Anniversary`。**
🔴 **したがって「1945 年以来、毎年ちがう芸術家が描いている」は、シャトー自身の一覧に照らすと正確ではない。**
⚠️ **シャトー自身も `key-date-1945` では「以来、各ヴィンテージのラベルは同時代の芸術家のオリジナル作品で飾られる」と
無条件に書いている。造り手が自分の一覧と食い違っている。両論を保存する。** → §Staff Notes ⚠️ ⑧

### 🔴 ✅ 1993 年ラベル —— **公式が語る唯一の版本。folklore ではなくこれを言う**

🔴 ✅ **公式 `label-art/discover-the-artwork/balthus` 本文（全訳）:**
「**ムートン・ロートシルト 1993 のための素描は、彼の作品に繰り返し現れる主題に立ち戻る —— 夢見がちな少女、優美で、脆い……**
**このラベルは、`2 つの異なる版が存在する数少ないラベルのひとつ` である点で異例である。
合衆国での発売の直後、`そして合衆国 Bureau of Alcohol, Tobacco, Firearms and Explosives（BATF）によって承認されていたにもかかわらず`、
ラベルは一部の界隈で反発を招いた。この論争に応えて、`Baroness Philippine de Rothschild は、
合衆国市場に出したボトルを回収することを決め、BATF にラベルの承認を取り消すよう求めた`。
彼女はそのうえで、`Balthus の素描を除き、パステルの背景だけを残した` 特別なラベルを合衆国市場向けに作った。**」

🔴 **すなわち公式の記述では、`BATF が禁止した` のではない。`BATF は承認していた` のであり、
`承認の取り消しを求めたのは Baroness 自身` である。**
🔴 **卓上で「アメリカで発禁になった」と言うと、造り手の記述と逆になる。** → §Staff Notes ⚠️ ④

---

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 6 本。exact 2 / unresolved 4**）

🔍 **6 行すべてが `source_producer_raw = "Mouton-Rothschild"` ／ `source_wine_raw = "Pauillac"` ／
セクション `FRANCE | RED > BORDEAUX`。キュヴェ名は 1 行も印字されていない。**

| # | VT | 価格 | 🔍 match_state | 🔍 confidence | 🔴 **本調査の判定** |
|---|---|---|---|---|---|
| 1 | **2019** | **$2,880** | **`unresolved`**（vintage） | **0.0** | 🔴 ✅ **公式ヴィンテージ・ページ実在（CS 90 / M 9 / PV 1、収穫 9/18–10/5、Olafur Eliasson）。canonical に行が無い＝vintage gap** |
| 2 | **2015** | **$2,920** | **`unresolved`**（vintage） | **0.0** | 🔴 ✅ **公式実在（CS 82 / M 16 / CF 2、Gerhard Richter）。canonical に行が無い＝vintage gap** |
| 3 | **2010** | **$3,700** | **`unresolved`**（vintage） | **0.0** | 🔴 ✅ **公式実在（CS 94 / M 6、Jeff Koons）。canonical に行が無い＝vintage gap** |
| 4 | **2009** | **$3,580** | **`unresolved`**（vintage） | **0.0** | 🔴 ✅ **公式実在（CS 88 / M 12、Anish Kapoor）。canonical に行が無い＝vintage gap** |
| 5 | **2001** | **$1,800** | 🔴 **`exact`** | 🔴 **1.0** | 🔴 ✅ **公式実在（CS 86 / M 12 / CF 2、Robert Wilson）。**🔴 **canonical レコードは存在するが、その `grapes` と `aging` が公式と食い違う** |
| 6 | **1996** | **$2,200** | 🔴 **`exact`** | 🔴 **1.0** | 🔴 ✅ **公式実在（CS 77 / M 13 / CF 10、Gu Gan）。**🔴 **canonical レコードは存在するが、その `grapes` と `aging` が公式と食い違う** |

### 🔴 6 行すべてに共通する未決着点 —— **グラン・ヴァンかセカンドか**

🔴 **確定していること:**
1. 🔴 🏛 **白（Aile d'Argent）ではない。** AOC Pauillac は赤専用であり、Aile d'Argent のラベルは `Bordeaux` と刷る。
2. 🔴 ✅ **グラン・ヴァンとセカンドは、どちらも AOC Pauillac である。** 両方のラベルを実読して確認した。
3. 🔴 ✅ **セカンドのラベルにも `MOUTON ROTHSCHILD` の語が大書されている。**
   したがって `source_producer_raw = "Mouton-Rothschild"` はセカンドを排除しない。
4. 🔴 ✅ **6 ヴィンテージすべてについて、グラン・ヴァンもセカンドも実在する**
   （セカンドの公式ヴィンテージ選択は 1995–2022 を並べ、初ヴィンテージは 1993）。

⚠️ **したがって、`メニューが誤っている` とも `メニューが正しい` とも断定しない。**
🔴 **メニューが省いているのはキュヴェ名であって、appellation は正しく `Pauillac` である。
Batch 10・11 の教訓どおり、defective な側を決めつけない。**
🔴 **決着は物理ラベル 1 点で付く。** → §Open Questions 1

⚠️ **なお価格（$1,800–$3,700）は 🔍 OBP 由来のデータであって造り手の出荷価格ではない。
公式サイトは価格を一切掲載していない。価格から品目を推定することは本ドシエの証拠基準を満たさない。**

---

## Staff Notes

### 🔴 芯 3 点（**これだけで卓上に立てる。すべて造り手の一次資料または公的登録**）

🔴 **①「メドックの 1855 年格付で、順位が動いた唯一のシャトーです。1973 年に第 2 級から第 1 級へ。」**
✅ **シャトー自身の言葉:「Baron Philippe の長い闘いののち、1855 年の格付けで不当に奪われていた `Premier Cru Classé` の地位を得た。
当時の農業大臣 `Jacques Chirac` が署名したデクレを経て。」**
🔴 🏛 **INAO の公式委員会報告（2016-CN428）が独立に裏づける:「`Lafite-Rothschild, Latour en 1855 et Mouton-Rothschild en 1973`」。**
**Pauillac には今日 18 の crus classés があり、フランスのどのコミューンより多い。**

🔴 **②「ラベルは 1945 年から、そのヴィンテージのために画家が描き下ろした作品です。このヴィンテージは ◯◯ が描いています。」**
✅ **1996 = Gu Gan ／ 2001 = Robert Wilson ／ 2009 = Anish Kapoor ／ 2010 = Jeff Koons ／
2015 = Gerhard Richter ／ 2019 = Olafur Eliasson。全 6 点、シャトーの公式ページに画家名と生年が載っている。**
🔴 **1945 年の最初の 1 枚は Philippe Jullian の勝利の `V`。連合国の勝利と Baron Philippe の帰還を祝うものだった。**

🔴 **③「カベルネ・ソーヴィニヨンのワインです。畑の 81% がカベルネで、樹齢は平均 44 年。
熟成は新しいオーク樽で約 20 か月、清澄は卵白です。」**
✅ **すべて `/the-vineyard/from-vine-to-wine` の文言。**
🔴 **そのうえで —— `アッサンブラージュはヴィンテージごとに変わる` とシャトー自身が明記している。
だから「毎年 CS 何 % です」とは言わず、そのヴィンテージの数字を言う（上表の 6 行）。**

### ⚠️ 言ってはいけないこと（must-not-say）

🔴 **A 群 —— canonical をそのまま読むと出てしまう嘘（6 件）**

⚠️ **① 「セパージュはカベルネ・ソーヴィニヨン 86%、メルロ 8%、カベルネ・フラン 4%、プティ・ヴェルド 2% です」。**
🔴 **canonical の 3 レコード全部にこの値が入っている（1996 だけ 79/11/8/2）。公式はどのヴィンテージでもこの数字を出していない。**
🔴 **とくに `プティ・ヴェルド 2%` は、1996 にも 2001 にも公式のブレンドに存在しない。**

⚠️ **② 「24 か月、新樽 100% で熟成します」。**
🔴 **公式は `about twenty months` で、`100%` という語を使っていない。**
🔴 **canonical 自身の `obp_note` も「オーク樽約20ヶ月」と書いており、同じレコードの `aging` フィールドと矛盾している。**

⚠️ **③ 「畑は 90 ヘクタールです」（あるいは「84 ヘクタールです」）と断定すること。**
🔴 **公式の同一ページが両方を書いている。「公式が 84 とも 90 とも書いている」と言うのが正しい。**

⚠️ **④ 「アイル・ダルジャンはポイヤックの白です」。**
🔴 **ラベルは `Bordeaux / Appellation Bordeaux Contrôlée`。🏛 AOC Pauillac は赤専用である。**
⚠️ **セパージュも canonical の値（SB/SG 56% ＋ Sémillon 43% ＋ Muscadelle 1%）は公式と違う。
公式は `Sauvignon Blanc 53 / Semillon 35 / Sauvignon Gris 11 / Muscadelle 1`。**

⚠️ **⑤ 「ムートンの標語は『Premier je suis, second je fus, Mouton ne change』です」。**
🔴 **取得した公式ページのどこにも、この全文は現れなかった。シャトーが自分のサイトで掲げている標語は
`I, Mouton, do not change`（わたし、ムートンは変わらない）である。**
⚠️ **この couplet が偽であるという意味ではない。`造り手の一次資料で裏が取れていない` という意味である。**

⚠️ **⑥ 「94 点／97 点です」。**
🔴 **公式サイトは点数を一切掲載していない。canonical の `points` の出典は不明である。**

🔴 **B 群 —— 現場で出やすい嘘（6 件）**

⚠️ **⑦ 「ビオです／有機認証です」。**
🔴 **シャトーの畑の事業所（SIRET `45920264400033`）も、ラベルの所有者 GFA（`31475027400016`）も、
Agence Bio でゼロ件。有機登録があるのは親会社の本社 SIRET であり、その活動場所は
Saint-André-du-Bois と Mouton Cadet の醸造センターと Pauillac の本社である。畑ではない。**
⚠️ **同時に「有機ではありません」も言ってはならない。シャトーは栽培について何も公表していない。**
🔴 **とくに「このボトルは有機です」は二重に誤り —— 登録は 2019-09-04 以降であり、OBP の 6 本すべてがそれを遡る。**

⚠️ **⑧ 「1945 年から毎年ちがう芸術家が描いています」を無条件に言うこと。**
🔴 **公式一覧の 4 年（1953 Centenary / 1977 Queen Mother へのトリビュート / 2000 Augsburg Ram / 2003 150 周年）は
「その年のために描いた同時代の芸術家」ではない。**

⚠️ **⑨ 「1993 年のバルテュスのラベルはアメリカで発禁になりました」。**
🔴 **シャトーの記述は逆である。`BATF は承認していた`。回収を決め、承認の取り消しを求めたのは
`Baroness Philippine de Rothschild 自身` である。彼女がそのうえで、素描を外してパステルの背景だけを残した
米国向けラベルを作った。**

⚠️ **⑩ 「ラベルに『Premier Grand Cru Classé』と書いてあります」。**
🔴 **1996・2001・2019 の実ラベル 3 本のいずれにも、格付の表記が一文字も無い。
刷られているのは名前・年号・瓶詰め文言・`PAUILLAC` / `APPELLATION PAUILLAC CONTRÔLÉE`・所有者名・度数・容量だけである。**
🔴 **この 3 本は OBP の 6 ヴィンテージの幅（1996–2019）を覆っている。**

⚠️ **⑪ 「オーパス・ワンやアルマヴィーヴァもこのシャトーのワインです」。**
🔴 **🏛 それらは同じ SIREN の別事業所ですらない。別法人・別ドメインである。
`Château Clerc Milon`（SIRET `45920264400041`）と `Château d'Armailhac`（`45920264400058`）は
同じ SIREN の別事業所だが、別のシャトーであり、別の canonical レコードを持つ。混ぜてはならない。**
⚠️ **`Opus One` は OBP に独自の行があり、本ドシエは一語も検証していない。**

⚠️ **⑫ 「このグラスはグラン・ヴァンです」と、ラベルを見ずに断定すること。**
🔴 **セカンド `Le Petit Mouton de Mouton Rothschild` も AOC Pauillac であり、そのラベルにも `MOUTON ROTHSCHILD` と大書される。
メニューはキュヴェ名を印字していない。ラベルの上段にアーティストの帯があるか、
瓶詰め文言が `Toute la récolte a été mise en bouteilles au Château`（グラン・ヴァン）か
`MIS EN BOUTEILLE À LA PROPRIÉTÉ`（セカンド）か —— この 2 点で確認してから言う。**

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

🔒 **本節は escalation のみ。`REGISTER.md` は書き換えていない。番号の採否は CTO の判断である。**

### 🔍 canonical の実測（`migration/out/export/db_wine_canonical.json`、928 要素・読み取りのみ）

| 走査 | 結果 |
|---|---|
| **`mouton` を含むレコード（全文字列、大小無視）** | 🔍 **24 件** |
| 🔴 **`producer` フィールドが `Château Mouton-Rothschild`** | 🔴 **3 件**（`mouton-rothschild-1855` / `-2001` / `-1996`） |
| 🔴 **誤検出（本生産者ではない）** | 🔴 **21 件**。内訳: `bordeaux-vintage-*-guide` 13 件（prose 中の Mouton 言及）／`darmailhac-1855`・`clerc-milon-1855`・`opus-one`（`Baron Philippe` 言及）／`montrose-1855`・`lagrange-sj-1855`・`calon-segur-1855`・`grand-puy-ducasse-1855`（1855 格付一覧の prose）／`kapcsandy-state-lane` |
| 🔴 **`vintage: "—"`（U+2014）を持つレコード全体** | 🔍 **328 件**（Batch 11 の実測値と一致。本件では `mouton-rothschild-1855` がそれ） |

→ 🔴 **`D-2026-08-05-08`（部分文字列一致の誤検出）は本件で実際に発生する。21/24 が誤検出である。
`producer` フィールドの完全一致と SIRET でのみ安全に切れる。**

---

### 🔴 ① `mouton-rothschild-1855` —— **既知の shape。ボトルではなく格付を符号化している**

🔴 **`vintage: "—"`。ブリーフが警告した「classification を格納したレコード」に該当する。**
⚠️ **ただし `cos-destournel-parker-profile` のような第三者評論家プロファイルではない。
内容はシャトー自身の沿革・畑・レンジの要約であり、出所は不明だが評論家の署名は無い。**
🔴 **本ドシエはこれを「修正すべき対象」としては扱わない。実在するのは 3 品目のキュヴェであり、
この 1 件が対応する現実の瓶は無い。**

---

### 🔴 ② 数値スペックの矛盾 —— **3 レコード全部で失敗。ただし失敗は数値に偏っている**

🔴 **3 レコードの全フィールドを、公式ヴィンテージ・ページ・公式栽培/醸造ページ・実ラベル・🏛 CDC と 1 件ずつ突き合わせた。
検証した個別アサーションは **48 件**。内訳は **✅ 一致 25 件 / 🔴 矛盾 11 件 / ⚠️ 出典なし・過度な一般化 12 件**。**

#### 🔴 A. 3 レコードに共通する矛盾（typed field）

| フィールド | canonical の値 | ✅ 造り手の値 | 判定 |
|---|---|---|---|
| 🔴 **`aging`（3 件とも同一文字列）** | **`"24 months barrel (new oak 100%)"`** | 🔴 **`about twenty months`／`matured in new oak barrels`（`100%` の語は無い）** | 🔴 **矛盾。3 レコードすべて。**🔴 **しかも `mouton-rothschild-1855` の `obp_note` は「オーク樽約20ヶ月」と正しく書いており、同一レコード内で typed と prose が割れている** |
| 🔴 **`classification`** | **`1855`: `"1855 Médoc Classification · 1er Grand Cru Classé"`**<br>**`2001`/`1996`: `"Premier Grand Cru Classé (1855)"`** | 🔴 **実ラベル 2 本: 格付の表記なし**／✅ **EN サイト: `Premier Cru Classé`**／⚠️ **FR OG: `Premier grand cru classé`** | 🔴 **① 同一生産者の 3 レコードで 2 通りの文字列。② どちらも造り手の表記と一致しない。③ ラベルは沈黙している。**⚠️ **🏛 1921 年デクレ第 13 条は `grand cru classé` を許すので「違法」ではない** |
| 🔴 **`producer`（3 件とも）** | **`"Château Mouton-Rothschild"`（ハイフン）** | 🔴 **造り手の散文中のハイフン使用 0 件。ラベル・タイトル・本文すべて `Château Mouton Rothschild`**<br>🏛 **INAO は `Mouton-Rothschild` とハイフンで書く** | 🔴 **`C-1` 族。`name` フィールド（2001/1996、ハイフンなし）が造り手表記に一致し、`producer` フィールドが行政表記。canonical が 1 生産者の中で 2 系統を混在させている** |

#### 🔴 B. `mouton-rothschild-1996`

| フィールド | canonical | ✅ 公式 | 判定 |
|---|---|---|---|
| 🔴 **`grapes`** | **CS 79% / M 11% / CF 8% / PV 2%** | 🔴 **CS 77% / M 13% / CF 10%（PV は列挙されていない）** | 🔴 **4 値すべて誤り。存在しない品種を 1 つ追加している** |
| 🔴 **`winemaking` / `_en`** | **同じ 79/11/8/2 ＋「24ヶ月新樽100%」** | 同上 | 🔴 **矛盾（`grapes` と `aging` の誤りを prose に複製）** |
| ⚠️ **`points: 97`** | **97** | ⚠️ **公式は点数を一切掲載しない** | ⚠️ **出典なき評点** |
| ⚠️ **`drinking_window`** | **`Now–2040`** | ⚠️ **公式は飲み頃を書かない** | ⚠️ **出典なし** |
| ⚠️ **`tasting` / `_en`** | **カシス、スグリ、セーダー、シガーボックス、グラファイト、スパイス、ミント、なめし革** | ⚠️ **公式 1996 ノート: `チェリー・ブラックベリー`、`シダー材`、`フレッシュなミント`、`花的な調子`、`統合された樽`。カシス／グラファイト／シガーボックス／なめし革は無い** | ⚠️ **造り手の言葉ではない。`ミント` と `シダー` だけが重なる** |
| ⚠️ **`terroir` / `_en`** | **「1996年はポイヤックにとって傑出したカベルネ・ヴィンテージ」** | ⚠️ **公式 1996: 「vintage was very good, almost ideal」。品種別の優劣づけはしていない** | ⚠️ **出典なき格付け** |
| ✅ **`subregion` / `color` / `country` / `region`** | **Pauillac / Rouge / France / Bordeaux** | ✅ **ラベル `PAUILLAC` ／ 🏛 CDC 赤専用** | ✅ **一致** |

#### 🔴 C. `mouton-rothschild-2001`

| フィールド | canonical | ✅ 公式 | 判定 |
|---|---|---|---|
| 🔴 **`grapes`** | **CS 86% / M 8% / CF 4% / PV 2%** | 🔴 **CS 86% / M 12% / CF 2%（PV は列挙されていない）** | 🔴 **CS のみ一致。M・CF が誤り、PV を追加している。**🔴 **「CS が合っている」ことが、他の 3 値の誤りを見えにくくする** |
| 🔴 **`winemaking` / `_en`** | **同じ 86/8/4/2 ＋「24ヶ月新樽100%」** | 同上 | 🔴 **矛盾** |
| ⚠️ **`points: 94`** | **94** | ⚠️ **公式は点数を掲載しない** | ⚠️ **出典なき評点** |
| ⚠️ **`drinking_window` `Now–2035`／`tasting`（カシス・グラファイト・シガーボックス）** | | ⚠️ **公式 2001 ノート: `ビルベリー・カシス`、`煙と革`、`わずかに動物的`。グラファイト／シガーボックスは無い** | ⚠️ **部分的にのみ重なる。造り手の言葉ではない** |
| ✅ **`subregion` / `color`** | **Pauillac / Rouge** | ✅ | ✅ **一致** |

#### 🔴 D. `mouton-rothschild-1855` の `obp_note`（**12 の主張に分解して検証**）

| 主張 | ✅ 公式 | 判定 |
|---|---|---|
| **「90ha、標高27m緩斜面」** | ⚠️ **公式が同一ページで `84 ha` と `90 ha` の両方／`27m` は一致** | ⚠️ **面積は造り手が自己矛盾。canonical は片方だけを断定している** |
| 🔴 **「CS 80% / Merlot 16% / CF 3% / PV 1%」（畑の植栽）** | 🔴 **`Cabernet Sauvignon (81%), Merlot (15%), Cabernet Franc (3%), Petit Verdot (1%)`** | 🔴 **矛盾（CS・M の 2 値）** |
| **「平均樹齢44年」** | ✅ **`around 44 years`** | ✅ **一致** |
| **「木製醗酵槽44基＋ステンレス20基」** | ✅ **`44 vats` oak ＋ `20 vats` stainless** | ✅ **一致** |
| **「厳格な選果後、重力流下」** | ✅ **手選果・振動テーブル・重力給送** | ✅ **一致** |
| 🔴 **「熟成：オーク樽約20ヶ月」** | ✅ **`about twenty months`** | 🔴 ✅ **一致。**🔴 **だが同じレコードの `aging` フィールドは `24 months`。内部矛盾** |
| **「清澄：卵白使用」** | ✅ **`fining with egg-white`** | ✅ **一致** |
| **「Le Petit Mouton（1993年〜）」** | ✅ **初ヴィンテージ 1993。**⚠️ **ただし 1993 は `Le Second Vin de Mouton Rothschild` の名で出され、決定的な名は 1994 から** | ⚠️ **不完全** |
| **「Aile d'Argent（1991年〜…新樽50%）」** | ✅ **1991 が最初のボトル／`50% of the wine is matured in new oak barrels`** | ✅ **一致** |
| 🔴 **「Aile d'Argent … SB/SG 56%＋Sémillon 43%＋Muscadelle 1%」** | 🔴 **`Sauvignon Blanc 53% / Semillon 35% / Sauvignon Gris 11% / Muscadelle 1%`（SB+SG = 64%、Sémillon = 35%）** | 🔴 **矛盾** |
| 🔴 **「アーティストラベル全履歴（1973〜2023）」51 件** | 🔴 ✅ **公式 `label-art` 一覧の該当 51 件と全件一致（`2011: Rougemont` を「ギィ・ド・ルージュモン」と補って書く点を含め、齟齬なし）** | 🔴 ✅ **全件一致。本ドシエ最大の「canonical が正しい」ブロック** |
| ⚠️ **「1945年から毎年異なる現代美術家のオリジナル作品」** | ⚠️ **公式一覧に 4 つの非・同時代芸術家エントリ（1953/1977/2000/2003）** | ⚠️ **過度な一般化。ただしシャトー自身も同じ一般化をしている** |
| ⚠️ **「Opus One（1979年〜）/ Almaviva（1997年〜）」** | ❓ **本ドシエは検証していない（他エージェントの担当領域）** | ❓ **未検証。判定を出さない** |

---

### 🔴 ③ 未採番として提案する形 —— **「同一レコード内で typed field と prose が互いに矛盾する」**

🔴 **`mouton-rothschild-1855` は、`aging: "24 months barrel (new oak 100%)"` という typed field と、
`obp_note` 中の「熟成：オーク樽約20ヶ月」という prose を、同時に持っている。**
🔴 **公式は `about twenty months`。すなわち `prose のほうが正しく、typed field が誤っている`。**

⚠️ **これは Batch 10 が確立した「失敗は typed field にも及ぶ」とは向きが逆である。**
**Batch 10 の形は「prose も typed も同じ誤りを持つ」だったが、本件は
`同一レコードの中で正しい値と誤った値が並存し、正しいほうが prose 側にある`。**
🔴 **したがって「typed field を信頼して prose を捨てる」という自然な整備方針は、本件では悪化を招く。**

🔴 **本ドシエは番号を開かない。形として記述するにとどめる。**
⚠️ **`P-*` 族（prose と typed の乖離）に接続しうるが、それは CTO の判断である。**
**→ **unnumbered — CTO's call**。**

---

### 🔴 ④ 未採番として提案する形 —— **`cuvee_state: exact` の evidence 文字列が、それ自身を反証している**

🔴 **OBP 6 行すべての intake evidence の 2 行目は、逐語で次のとおりである。**

```
名称トークン集合一致: 'pauillac' ≡ 'Château Mouton-Rothschild'
```

🔴 **`{pauillac}` と `{château, mouton, rothschild}` は共通要素を 1 つも持たない。
「トークン集合一致」はこの 2 つの間には成立しない。evidence 文字列が主張そのものを反証している。**

🔴 **にもかかわらず 6 行すべてが `cuvee_state: "exact"` を持つ。**
🔴 **さらに同じレコードの `_parts` は `{"label": null, "appellation": "pauillac", "appellation_display": "Pauillac"}` である ——
`パーサは「これは appellation であって label ではない」と正しく判定している` のに、
`マッチャはその判定を無視して cuvée の exact 一致を宣言している`。**

🔴 **結果として、2001 行と 1996 行は `match_state: "exact" / confidence: 1.0` になる。
その 1.0 を成立させている唯一の実質的な条件は「canonical に当該 vintage の行が存在する」ことだけである。**

⚠️ **これは Batch 10 の「matcher は節見出しを読んでいない」とも、Batch 11 の
「`exact` は canonical 一致を測るだけで実在を測らない」とも異なる、第 3 の形である。**
🔴 **本件では、`matcher が自分の parser の出力と矛盾する evidence を発行している`。**
**→ **unnumbered — CTO's call**。**

🔴 **実務上の含意: この生産者の `confidence 1.0` は、キュヴェの同定を一切保証しない。
`Le Petit Mouton` のボトルが刺さっていても、同じ 1.0 が出る。**

---

### 🔴 ⑤ canonical gap（**4 行分。conflict ではない**）

🔴 **`D-2026-08-05-14` の方針どおり、`不在` は conflict ではなく gap として記録する。番号は開かない。**

| OBP 行 | 状態 | 判定 |
|---|---|---|
| **2019 / 2015 / 2010 / 2009** | 🔴 **canonical に vintage 行が無し（保有は 1996・2001 のみ）** | 🔴 **vintage gap。4 行すべて公式ヴィンテージ・ページが実在し、セパージュ・収穫日・画家まで公式で取れる。**🔴 **`unreachable`（別綴りで存在する）ではない —— 928 件を `mouton` で走査し、当該生産者の行は 3 件しかないことを確認した** |

🔴 **OBP インパクト（本数）:**
- 🔴 **vintage gap: 4 本**（2019・2015・2010・2009）
- 🔴 **矛盾値を抱えたまま `exact` で当たっている行: 2 本**（2001・1996）
- 🔴 **キュヴェ同定が未決着の行: 6 本すべて**（グラン・ヴァン／セカンドの区別が付いていない）

---

### ⚠️ ⑥ 公式サイト内部の不一致（**canonical とは無関係。造り手側の問題。両論を保存する**）

| 項目 | 公式の値 A | 公式の値 B |
|---|---|---|
| 🔴 **畑の面積** | 🔴 **`84 hectares (207 acres)`**（`/the-vineyard/the-terroir` のスライダー見出し） | 🔴 **`90 hectares (222 acres)`**（同じページの本文） |
| ⚠️ **2009 の収穫終了日** | **`13 October`**（`Harvest` 欄） | **`6 October`**（`Climatic conditions` 本文、カベルネ・ソーヴィニヨン） |
| ⚠️ **2010 の収穫開始日** | **`29 september`**（`Harvest` 欄） | **`28 September`**（本文） |
| ⚠️ **2015 の収穫終了日** | **`2 October 2015`**（`Harvest` 欄） | **`6 October`**（本文。ただし「3 つの estate を通じて」と明記されており、対象が異なる可能性が高い） |
| ⚠️ **Philippe Sereys de Rothschild の肩書** | **`Chairman and CEO`**（`/legal`） | **`Chairman of the Supervisory Board`**（`key-date-2014`・`key-date-1988`） |
| ⚠️ **アーティスト・ラベルの一般化** | **「1945 年以来、各ヴィンテージは同時代の芸術家のオリジナル作品」**（`key-date-1945`） | **一覧に 4 つの例外（1953 / 1977 / 2000 / 2003）** |

→ ⚠️ **どちらも公式である。`A producer can contradict itself` の実例として両論を保存する。どちらかを選ばない。**

---

### 🔴 ⑦ ブリーフの前提に対する反証・補正

🔴 **① ブリーフは「canonical の `Premier Grand Cru Classé (1855)` は 1996 と 2001 のボトルについては arguably fine」とした。
実測の結論はより厳しい —— `ラベルに格付の表記が一文字も無い`。1996・2001・2019 の 3 本で確認した。**
**したがって「1855 のカッコが妥当か」以前に、`このシャトーはボトルに格付を刷らない` という事実が先に立つ。**
⚠️ **なお 🏛 1921 年デクレは `grand cru classé` の使用を許すので、canonical の文字列は違法ではない。
問題は合法性ではなく、`造り手の表記ではない` こと、および `同一生産者の 3 レコードで 2 通りある` ことである。**

🔴 **② ブリーフは「Aile d'Argent は AOC Pauillac ではない」と正しく予測していた。実測で確認した。
ただし本ドシエはそれを CDC だけでなく `造り手自身のラベル` で確認した点で一段強い。**

🔴 **③ ブリーフは 6 行の正体を「grand vin / second / white のいずれか」と設定した。
白は消えたが、`grand vin と second を分ける情報は OBP の 2 列には存在しない`。
セカンドのラベルにも `MOUTON ROTHSCHILD` が大書されるため、生産者名では切れない。
この点は「メニューが不完全」であって「メニューが誤っている」ではない。**

🔴 **④ Batch 8–11 の base rate（14 軒中 13 軒で canonical が失敗）は本件でも維持されるが、
`一様ではない`。数値スペック（grapes / aging / points）は全滅、
列挙（アーティスト 51 件）は全問正解、地理（subregion / color / region）も正解である。**
**「canonical は間違っている」ではなく「canonical は数値で間違う」と言うほうが、本件の証拠には忠実である。**

---

## Sources

### 🔴 ⚠️ サイト真正性の事前チェック（`D-2026-08-05-09`）—— **2 件検査、1 件採用、1 件は別レイヤーとして分離**

| ドメイン | 判定 | 根拠 |
|---|---|---|
| ✅ 🔴 **`www.chateau-mouton-rothschild.com`** | ✅ **合格・採用（§2a の (a) と (c) を同時に満たす）** | ✅ **(a) `/legal` が発行者を `Baron Philippe de Rothschild SA` と明記し、`RCS Bordeaux n° B 459 202 644`・`Share capital €6,250,000`・`Registered office: rue de Grassi – 33250 Pauillac` を名乗る。**<br>🏛 **これが 🏛 SIREN `459202644`／siège SIRET `45920264400017`／住所 `10 RUE DE GRASSI 33250 PAUILLAC` と完全一致。**<br>🏛 **(c) 郵便住所が公的登録と一致。**<br>✅ **加えて相互リンク: フッターが `chateau-clerc-milon.com`・`chateau-darmailhac.com`・`opusonewinery.com`・`almavivawinery.com`・`domaine-de-baronarques.com`・`bpdr.com` を「Other Baron Philippe de Rothschild estates」として列挙し、🏛 登録の姉妹事業所（SIRET `…041` / `…058`）と対応する。**<br>✅ **`robots.txt` は SEO クローラを弾くのみで、通常取得を妨げない。年齢確認ゲート・bot チャレンジ無し（回避行為なし）。** |
| ⚠️ **`www.bpdr.com`** | ⚠️ **真正だが `別の著者レイヤー` として扱い、本ドシエでは引用ゼロ** | ⚠️ **HTTP 200・同一 `Server: PWS/8.3.1.0.8`。`chateau-mouton-rothschild.com` のフッターから `Site institutionnel du groupe` として相互リンクされる。**<br>🔴 **しかしこれはグループ（Baron Philippe de Rothschild SA）の企業サイトであり、シャトーのページとは著者レイヤーが異なる。**<br>🔴 **本ドシエは 1 語も引用していない。**<br>⚠️ **なお `chateau-mouton-rothschild.com` の `/legal` 自体も発行者は `Baron Philippe de Rothschild SA` である。すなわち「シャトーのサイト」と「グループのサイト」は法的な発行者が同一で、URL とコンテンツの主題だけが異なる。この区別は名目的である点を明記する。** |
| 🔴 ❌ **`mouton-rothschild.com`（www 無し）** | 🔴 **却下（正しい所有者だが、別のシャトーを配信する）** | 🔴 **`https://` は接続失敗（`%{http_code} 000`。当該ホスト名の証明書が無い）。**<br>🔴 **`http://mouton-rothschild.com/` は `HTTP 200` を返すが、`url_effective` は 🔴 **`https://www.chateau-darmailhac.com/`** —— `姉妹シャトー Château d'Armailhac のサイトへリダイレクトされる`。**<br>🔴 **DNS: `A 5.44.162.218`、`MX mx1/mx2.mouton-rothschild.com` —— メール系が自ドメインに立っており、グループ所有と見てよい。**<br>🔴 **すなわちこれは「売却パーキング」でも「ファンサイト」でもない。**🔴 **`真の所有者が持っているのに、別の château を配信している` という新しい罠の形である。**<br>🔴 **「最も自明に見えるドメイン」を検証せずに使っていたら、本ドシエは Château d'Armailhac の内容を Mouton の内容として書いていた —— ブリーフが警告した姉妹シャトー混同が、ドメイン経由で現実に起きる経路である。**<br>🔴 **本ドシエは本ドメインの内容を 1 語も使用していない。** |

🔴 **look-alike の「売却パーキング／ファンサイト／一文字違い」型は 0 件。本件では従来型の偽サイトを踏んでいない。**
🔴 **代わりに 2 つの新しい衝突形を記録する ——**
🔴 **① `mouton-rothschild.com` —— 正規の所有者が持ちながら別シャトーへリダイレクトするドメイン（上表）。**
⚠️ **② `SCEA CHATEAU CROIX MOUTON`（🏛 SIREN 412826695）—— 名前ではなく `住所` が literally `3 CHATEAU MOUTON` である別事業者。
しかも Pauillac ですらない（33240 Lugon-et-l'Île-du-Carnay、右岸）。住所文字列での照合は誤爆する。**
⚠️ **③ `YVES BLONDY`（🏛 SIREN 433096971）—— `LE POUYALET 4 LA FON DE MOUTON 33250 PAUILLAC`。
ムートンと同じ集落・同じ郵便番号で、地名にも `MOUTON` を含む別事業者。集落名での照合も誤爆する。**

### ✅ シャトー自身のサイト（`https://www.chateau-mouton-rothschild.com/`、EN 原本）

- ✅ `robots.txt` → `sitemap_index.xml`（13 サブマップ）→ `page-sitemap.xml`（**952 URL**）
- ✅ `vintage-sitemap.xml`（23）／`vin-sitemap.xml`（23）／`etiquette-sitemap.xml`（24）
- ✅ **`/chateau-mouton-rothschild/chateau-mouton-rothschild-{1996,2001,2009,2010,2015,2019}`（OBP 6 行の全ヴィンテージ。気象・収穫日・セパージュ・公式ノート・画家）**
- ✅ `/the-vineyard/the-terroir`（🔴 **84 ha と 90 ha の同一ページ内不一致**・土壌・地形・Pauillac 1,200 ha・18 crus classés）
- ✅ `/the-vineyard/from-vine-to-wine`（🔴 **植栽 81/15/3/1・10,000 本/ha・樹齢 44 年・27 m・槽 44+20・`about twenty months`・卵白清澄**）
- ✅ `/the-vineyard/the-skills`（🔴 **標語 `I, Mouton, do not change`**・栽培/醸造の役割分担）
- ✅ `/the-house/the-mouton-style`（建築・Museum of Wine in Art）
- ✅ `/aile-dargent`（🔴 **SB 53 / Sém 35 / SG 11 / Musc 1・9,000 本/ha・新樽 50%**）／`/aile-dargent/aile-dargent-2019`
- ✅ `/le-petit-mouton-de-mouton-rothschild`（🔴 **初 VT 1993、名称は 1994 から**・Jean Carlu 1927）／`/le-petit-mouton-de-mouton-rothschild-2015`
- ✅ `/label-art` ／ `/label-art/discover-the-artwork/balthus`（🔴 **1993 年ラベルの公式版本 ＋ 全 81 エントリの画家一覧**）
- ✅ `/the-history/key-dates/key-date-{1853,1924,1945,1962,1973,1988,1991,1993,2014}`
- ✅ `/the-history/the-history-of-mouton/from-marquis-to-barons`
- ✅ `/legal`（🔴 **法人・RCS・資本金・本社・執行体制・掲載責任者・ホスティング**）

### ✅ シャトー自身のボトルショット（**producer's own domain 由来。ラベル面を実読**）

| 画像 | 🔴 実読したラベル文字列 |
|---|---|
| ✅ `/cellar/uploads/Chateau_Mouton_Rothschild_2019.jpg` | 🔴 **`Château Mouton Rothschild` / `2019` / `Toute la récolte a été mise en bouteilles au Château` / `PAUILLAC` / `Baronne Philippine de Rothschild g.f.a` / `PROPRIÉTAIRE`（上帯に Olafur Eliasson の原画と署名）**🔴 **格付表記なし** |
| ✅ `/cellar/uploads/Mouton-Rothschild-bouteille-2001-web1.jpg` | 🔴 **`CHÂTEAU MOUTON ROTHSCHILD` / `2°01` / `toute la récolte a été mise en bouteilles au Château` / `PAUILLAC` / `APPELLATION PAUILLAC CONTRÔLÉE` / `Baronne Philippine de Rothschild g.f.a` / `PRODUCE OF FRANCE` / `PROPRIÉTAIRE`（上帯に Robert Wilson の原画・`FOR PHILIPPINE`）**🔴 **格付表記なし** |
| ✅ 🔴 `/cellar/uploads/Mouton-Rothschild-bouteille-1996-HR-210x777.jpg`（**OBP 6 行目そのもの**） | 🔴 **`Château Mouton Rothschild` / `1996` / `toute la récolte a été mise en bouteilles au Château` / 赤い署名 `Philippine de Rothschild` / `PAUILLAC` / `APPELLATION PAUILLAC CONTRÔLÉE` / `Baronne Philippine de Rothschild g.f.a` / `PRODUCE OF FRANCE` / `PROPRIÉTAIRE` / `12,5%vol` / `75cl`**<br>🔴 **上帯に Gu Gan の水墨の原画、左に `Encre de Chine par Gu Gan`、右に画家の落款**<br>🔴 **格付表記なし。ハイフンなし** |
| ✅ `/cellar/uploads/Aile_Argent_2019_210-210x764.png` | 🔴 **`Aile d'Argent®` / `2019` / `Bordeaux` / `Appellation Bordeaux Contrôlée` / `Château Mouton Rothschild` / `Baronne Philippine de Rothschild GFA` / `13,5%vol.` / `75cl`** |
| ✅ `/cellar/uploads/Bouteille_Petit_Mouton_2015_web-210x716.jpg` | 🔴 **`MIS EN BOUTEILLE À LA PROPRIÉTÉ` / `LE PETIT MOUTON DE MOUTON ROTHSCHILD` / `PAUILLAC` / `APPELLATION PAUILLAC CONTRÔLÉE` / `BARONNE PHILIPPINE DE ROTHSCHILD G.F.A.` / `2015`** |

### 🏛 公的登録・規制一次資料

| 出典 | 取得内容 |
|---|---|
| 🏛 **`recherche-entreprises.api.gouv.fr/search?q=CHATEAU%20MOUTON%20ROTHSCHILD`** | **4 法人。うち `BARON PHILIPPE DE ROTHSCHILD SA`（459202644）と GFA（314750274）** |
| 🏛 **同 `?q=BARON%20PHILIPPE%20DE%20ROTHSCHILD&code_postal=33250`** | 🔴 **事業所 10 件。`45920264400033 = CHATEAU MOUTON ROTHSCHILD`／`…041 = CHATEAU CLERC MILON`／`…058 = CHATEAU D'ARMAILHAC`（3 件とも NAF 01.21Z・同一住所）** |
| 🏛 **同 `?q=MOUTON&departement=33&activite_principale=01.21Z,…`** | 🔴 **同名の別事業者 5 件（`SCEA CHATEAU CROIX MOUTON` ほか）** |
| 🏛 **`opendata.agencebio.org/api/gouv/operateurs/?siret=45920264400033`** | 🔴 **`{"nbTotal":0,"items":[]}` —— 有効な陰性（シャトーの畑）** |
| 🏛 **同 `?siret=31475027400016`** | 🔴 **`{"nbTotal":0,"items":[]}` —— 有効な陰性（ラベルの所有者 GFA）** |
| 🏛 **同 `?siret=45920264400017`** | 🔴 **`nbTotal 1`。numeroBio 1816 / `LA BARONNIE` / Ecocert `FR-BIO-01` / `ENGAGEE` / `dateEngagement 2021-07-27` / `datePremierEngagement 2019-09-04` / `mixite: Oui` / lieux d'activité 4 か所（Le Pouyalet を含まない）** |
| 🏛 **同 `?q=MOUTON%20ROTHSCHILD`** | ⚠️ **`nbTotal 0`。**🔴 **`D-2026-08-05-08` により、名前クエリのゼロ件は陰性の証明にならない。上の SIRET クエリのほうが証拠である** |
| 🏛 **`extranet.inao.gouv.fr/fichier/PNOCDCPauillac.pdf`** | 🔴 **AOC Pauillac CDC（PNO 版、17 頁、`%PDF` 実体確認）。`réservée aux vins tranquilles rouges`／認可 6 品種／密度 7,000 本/ha／`rendement butoir 60 hl/ha`／étiquetage は `Pas de disposition particulière`** |
| 🏛 **`info.agriculture.gouv.fr/gedei/site/bo-agri/document_administratif-51ec7a83-…/telechargement`** | 🔴 **同 CDC の consolidated 版（BO du MAA 2017-12-07、16 頁、`%PDF` 実体確認）。`décret n° 2011-1746 du 1er décembre 2011`（`n°2012-1308` と `arrêté du 22 novembre 2017` により改正）で homologué。**🔴 **PNO 版と赤専用条項が一致（§2c の相互検証）** |
| 🏛 **`extranet.inao.gouv.fr/fichier/CNAOV-2016-428-Pauillac.pdf`** | 🔴 **INAO 委員会報告（2016-11-23、112 頁）。「`Avec aujourd'hui 18 crus classés (dont les premiers Lafite-Rothschild, Latour en 1855 et Mouton-Rothschild en 1973)`」＝ 1973 年昇格の 🏛 側の裏づけ ＋ 行政表記のハイフン** |
| 🏛 **Légifrance `LEGIARTI000025830820`（`Décret du 19 août 1921` 第 13 条、版 2012-07-01）** | 🔴 **`cru classé` の使用制限とその例外 b)「`Les vins de Bordeaux provenant de domaines viticoles figurant dans le classement de 1855; …les termes «cru classé» ou «grand cru classé» peuvent être utilisés`」** |

### ⚠️ 到達できなかった一次資料

- ⚠️ 🔴 **1973 年の昇格デクレそのもの。**`Légifrance` は直接 curl で `HTTP 403`（Cloudflare の JS/bot チャレンジ）。**回避行為はしていない（§1.8 に従い `gated — not evidence of absence` と記録する）。**`WebFetch` 経由でも 1973 年のテキストは特定できなかった。シャトー（大臣名 Jacques Chirac）と 🏛 INAO（年次 1973）の 2 系統で事実は確認済みだが、**官報の原文には到達していない。** → Open Questions 5
- ⚠️ **`inao.gouv.fr` の検索エンドポイントは `HTTP 301` で本文を返さなかった。CDC は extranet と bo-agri から取得した。**
- ⚠️ **eAmbrosia（EU GI レジスタ）の Pauillac エントリは JS シェルのみで内容が取れなかった。**

### 🔍 THÉSEUS 内部

- 🔍 `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行中 `Mouton-Rothschild` 6 行。`evidence` と `_parts` を全件読み出し）
- 🔍 `migration/out/export/db_wine_canonical.json`（928 要素。**読み取りのみ。書き込みゼロ**）

### ❌ 使用していない出典

- **Wikipedia・小売・オークション・評論家・アグリゲータ（Wine-Searcher / Vivino / Decanter / Wine Advocate / Vinous / CellarTracker 等）・輸入元資料は一切使用していない。**
- **`bpdr.com`（グループ企業サイト）は真正だが、著者レイヤーが異なるため引用ゼロ。**

**キャッシュ先**: `research/producers/_sources/chateau-mouton-rothschild/`（gitignored、55 ファイル）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🔴 **`/legal` の RCS と 🏛 SIREN が完全一致し、§2a に合格。**🔴 **シャトーを 2 法人（運営 SA ＋ 所有 GFA）と 1 事業所 SIRET に分解し、姉妹 2 シャトーを enseigne で切り分けた。**🔴 **ラベルの `PROPRIÉTAIRE` と GFA の登記住所が一致するという、ラベル↔登録簿の閉じを作った。**⚠️ **代表者の肩書が公式内部で 2 通り** |
| 🔴 **Overview** | 🔴 **High** | 🔴 **CS 主体・アーティストラベル・1973 昇格・標語という自己規定が、すべて一次で取れた** |
| **History** | **Medium-High** | ✅ **1853 / 1922 / 1924 / 1945 / 1962 / 1973 / 1988 / 1991 / 1993 / 2014 の 10 点を公式本文で確定。**⚠️ **1926 / 1933 / 1981 / 2003 / 2006 / 2012 の 6 点は公式に存在するが本調査で未取得** |
| 🔴 **Location** | 🔴 **High** | 🔴 **土壌・地形・27 m・植栽 81/15/3/1・密度・樹齢を公式で確定。**🔴 **AOC が赤専用であることを 🏛 CDC の 2 版（PNO ＋ BO consolidated）で相互検証。**🔴 **18 crus classés を公式と 🏛 INAO で二重確認。**🔴 **格付表記の 3 系統（ラベル無表記／EN／FR）を実測で分離。**⚠️ **面積が公式内部で 84 と 90 に割れる（保存済み）** |
| 🔴 **Farming** | 🔴 **Medium-High** | 🔴 **有機登録の不在を、畑の事業所 SIRET と GFA SIRET の 2 本の完全一致クエリで有効に証明した。**🔴 **陽性側（親会社）の登録内容を全項目転記し、活動場所に畑が含まれないことまで示した。**🔴 **温度差の罠を日付で定量化した。**⚠️ **公式が栽培について何も書いていないため、`実践` は完全に不明のまま。ここは埋まらない** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **OBP 6 ヴィンテージ全部のセパージュ・収穫日・公式ノート・画家を機械転記。**🔴 **醸造（重力式・44+20 槽）と熟成（約 20 か月・新樽・卵白）を公式本文で確定。**⚠️ **度数・pH・収量・生産本数・新樽比率の数値は公式に無い** |
| 🔴 **Style** | 🔴 **High** | 🔴 **OBP 6 行すべてについて、造り手自身のテイスティングノートを全文取得した。第三者の言葉は一切混ぜていない**⚠️ **公式は点数・受賞を一切掲載しない** |
| 🔴 **Important Cuvées** | 🔴 **Medium-High** | 🔴 **公式の現行 3 品目を確定し、3 品目すべての appellation を実ラベルで読んだ。**🔴 **白を排除する証明（ラベル＋CDC）を完了。**🔴 **1993 年ラベルの公式版本と、アーティスト 81 件の一覧を取得。**🔴 **しかし OBP 6 行がグラン・ヴァンかセカンドかは決着していない —— これは調査の不備ではなく、メニューの 2 列に情報が存在しないためである** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **3 レコード・48 アサーションを 1 件ずつ突き合わせ、✅ 25 / 🔴 11 / ⚠️ 12 に分類した。**🔴 **`unreachable` の可能性を 928 件走査で潰し、4 行を gap と断定できる状態にした。**🔴 **未採番の形を 2 つ（typed↔prose の内部矛盾／evidence 文字列の自己反証）具体例つきで提示した。**🔴 **同時に、canonical が全問正解した 51 件のブロックを明示し、base rate を無条件に一般化しないようにした** |
| 🔴 **Staff Notes** | 🔴 **High** | 🔴 **芯 3 点＋ must-not-say 12 項目。canonical をそのまま読むと出る 6 つの嘘（86/8/4/2・24 か月新樽 100%・90 ha 断定・Aile d'Argent が Pauillac・Premier je suis の couplet・点数）と、現場で出やすい 6 つの嘘を塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を超過。実感としては 88% 前後）。** | **OBP 6 行すべてについて、シャトーの正式名・appellation・そのヴィンテージのセパージュ・収穫日・公式テイスティングノート・ラベル画家を、造り手の言葉のまま言える。格付の由来は公式と 🏛 INAO の両方で言え、栽培については「シャトーが何も公表していない」と正確に言える。有機については断定的に「畑には登録が無い」と言え、同時に「実践は不明」と言える。**<br>**欠けているのは ① 6 行がグラン・ヴァンかセカンドか、② 1973 年デクレの官報原文、③ 醸造の分析値、④ 未取得の key-date 6 件。**<br>**① は物理ラベルで決着し、②③④ は「言わない」で回避できる。卓上で嘘をつく経路は塞いである。** |

**reached_70: YES (~88%)。**

---

## Open Questions

1. 🔴 **【物理ラベル・タスク／最優先】OBP 6 行の実ボトルは、グラン・ヴァンかセカンドか。**
   🔴 **メニューは `Mouton-Rothschild / Pauillac` としか印字しておらず、この 2 列には区別する情報が存在しない。**
   **確認すべきは 4 点 —— ① 肩の上に `アーティストの原画の帯` があるか（グラン・ヴァンのみ）、
   ② 瓶詰め文言が `Toute la récolte a été mise en bouteilles au Château`（グラン・ヴァン）か
   `MIS EN BOUTEILLE À LA PROPRIÉTÉ`（セカンド）か、
   ③ 名称が 1 行の `Château Mouton Rothschild` か 3 行の `LE PETIT MOUTON DE MOUTON ROTHSCHILD` か、
   ④ ヴィンテージ表記。**
   🔴 **6 本すべてについて必要。オンラインの一次資料はここまでしか到達できない。**

2. 🔴 **【物理ラベル・タスク】格付表記の有無。**
   **取得した 2 本のボトルショット（2019・2001）に格付の刷りは無かったが、
   ① バックラベル、② 輸入業者ラベル、③ 1996 年など古いヴィンテージの表ラベル
   のいずれかに `Premier Grand Cru Classé` があるかは、実物でしか分からない。**
   🔴 **canonical の `classification` をどう扱うかは、これが取れてから決めるべきである。**

3. **畑の面積は 84 ha か 90 ha か。**
   🔴 **公式の同一ページが両方を書いている。片方は古い版の残骸である可能性が高いが、断定はしない。
   シャトーに直接確認するのが最短。**

4. **栽培の実務。除草・防除・被覆作物・馬耕・カーボン・灌漑について、公式は一語も書いていない。
   HVE / Terra Vitis / ISO14001 などの認証の有無も、公式サイトからは分からない。**
   ⚠️ **`est_bio: true` は親会社に付いており、その活動場所に畑は含まれない。畑側の実践は完全に不明である。**

5. 🔴 **1973 年昇格のデクレの官報原文。**
   **シャトーは「Jacques Chirac 農業大臣が署名したデクレ」と書き、🏛 INAO は「Mouton-Rothschild en 1973」と書く。
   しかし `Légifrance` が Cloudflare の bot チャレンジで gated であり、番号・日付・JORF 掲載日には到達していない。**
   🔴 **これは「存在しない」証拠ではない。gated である。**

6. ⚠️ **`Philippe Sereys de Rothschild` の正確な肩書。**
   **`/legal` は `Chairman and CEO`、`key-date-2014` と `key-date-1988` は `Chairman of the Supervisory Board`。
   🏛 登記の `dirigeants` にも彼の名は現れず（GFA 側では `Gérant`）、SA 側の代表権が確定していない。**

7. **未取得の公式 key-date 6 件（1926 / 1933 / 1981 / 2003 / 2006 / 2012）。**
   **公式に頁が存在することは `page-sitemap.xml` で確認済み。本調査が読んでいないだけである。**

8. ⚠️ **canonical の `obp_note` が主張する `Opus One（1979年〜）` と `Almaviva（1997年〜）`。**
   🔴 **本ドシエは意図的に検証していない。`Opus One` は OBP に独自の行を持つ別生産者であり、
   別のエージェントの担当領域である。判定を出さない。**

9. **醸造の分析値 —— アルコール度数、pH、総酸、実収量（hl/ha）、生産本数、新樽比率の実数、tonnelier。**
   **公式は `new oak barrels` と `about twenty months` しか書かない。**

10. ⚠️ **「Premier je suis, second je fus, Mouton ne change」の出典。**
    **取得した公式ページに全文は無く、シャトーが掲げるのは `I, Mouton, do not change` のみ。
    未取得の 6 つの key-date（とくに 1973）や FR 版のページに全文がある可能性は残る。**

11. 🔴 **`mouton-rothschild.com`（www 無し）が Château d'Armailhac へリダイレクトされているのは意図的か。**
    🔴 **DNS・MX から見てグループ所有だが、`http://mouton-rothschild.com/` は
    `https://www.chateau-darmailhac.com/` に着地する。設定ミスの可能性が高い。**
    🔴 **THÉSEUS 側の含意は明確 —— このドメインを「Mouton の公式サイト」として扱ってはならない。**
    ⚠️ **`https://` が接続失敗である点も含め、今後 canonical の `url` フィールドに入れてはならない。**
