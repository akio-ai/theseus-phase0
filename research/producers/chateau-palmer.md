# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical に `producer` フィールド一致は 1 件のみ**（`palmer-1855`）。**prose のみの一致 11 件は全て別レコード**（Bordeaux ヴィンテージ・ガイド 8 件＋Margaux の他シャトー 3 件）。
> 🔴 **`D-2026-08-05-08` の「Champagne Palmer & Co との混同」は canonical には発生していない**（実測。→ §Identity）。
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト `chateau-palmer.com`／公式フィッシュ・ミレジム PDF** （一次資料・producer-authored）
> `🏛` **公的登録／法令**（recherche-entreprises.api.gouv.fr / Agence Bio / Ecocert / Demeter France / Biodyvin (SIVCBD) / INAO CDC / geo.api.gouv.fr）
> `📄` 造り手の旧ページを Internet Archive から復元したもの
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出 ／ `❓` 未解決
> `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 (JST) ／ 一次資料: **`https://www.chateau-palmer.com/`（FR 原本）**
> 走査元: **`robots.txt` → `sitemap.xml`（134 URL）→ FR 側 67 ページを全件取得・全文検索**
> 併用: ✅ **公式「Fiche Millésime」PDF 5 点（1996 / 2012 / 2013 / 2014 / 2017。全点 `%PDF` 実体・テキストレイヤーあり）**
> 併用: 🏛 **INAO CDC「MARGAUX」consolidated 版（2023-03-31 homologué・JORF 2023-04-05）＋ PNO 草案版の 2 版**
> 併用: 🏛 **企業登録・Agence Bio（SIRET 完全一致）・Ecocert 証明ページ・Demeter France 加盟者ページ・Biodyvin 会員リスト**
>
> ---
>
> 🔴 **① `Alter Ego` を「セカンドワイン」と言ってはならない。造り手がその枠組みを拒否している。**
> ✅ **公式レンジ見出し: `alter ego / L'autre grand vin de château palmer`**（EN 版は `THE OTHER WINE OF CHÂTEAU PALMER`）。
> ✅ **本文: 「Palmer et son Alter Ego, son « autre moi », sont `deux expressions distinctes du même terroir`, deux interprétations d'une même partition, deux étiquettes en miroir」／「cet `« autre vin »`」。**
> 🔴 **取得した FR 67 ページ＋EN 2 ページを全文検索して、`second vin` / `second wine` / `deuxième vin` は 0 件。**
> 🔴 **canonical の `obp_note` は「セカンド」「second wine」と書いている。** → §Canonical Conflict ②
>
> 🔴 **② AOC Margaux は赤のみ。白は Vin de France である —— 出典は Demeter France の登録。**
> 🏛 **CDC（2023 homologué）III 章: 「L'appellation d'origine contrôlée « Margaux » est `réservée aux vins tranquilles rouges`」。**
> 🏛 **Demeter France の加盟者ページ `SC CHATEAU PALMER` の製品リストが、**
> 🏛 **`Vin blanc Vin de France "Blanc de Palmer"` と `Vin rouge margaux "château palmer"` / `Vin rouge Margaux "Alter Ego"` を並べて登録している。**
> ⚠️ **公式サイトは白について一語も書かない**（`vin blanc` / `blanc de palmer` の検索結果 0 件）。
> ✅ **ただし îlot `Le Cassena` について「en plus des rouges, `quatre cépages de blanc`」とは書いている。** → §Important Cuvées
>
> 🔴 **③ `Historical XIXth Century Wine` —— 公式は名称・シラー比率・ラベル表示を自ら明記している。**
> ✅ **「Voilà un vin qui porte bien son nom troublant : `Historical XIXth Century Wine`. `Aucune trace de Palmer, de son château, ni même d'une appellation` sur l'étiquette bleu nuit」**
> ✅ **「les `10%` de syrah qui se marieront avec le merlot et le cabernet sauvignon du domaine」／「autour des `cinq mille bouteilles` annuelles」／「Expérimenté sur des lots de `2004`, s'étoffe en `2006` puis éblouit en `2010`」**
> 🔴 **canonical は「Blend」「シラー 15%」「Vin de France 表記」と書く。名称も比率も違い、`Vin de France` は公式が一度も書いていない。** → §Canonical Conflict ③
> 🏛 **CDC V 章の主要品種は `cabernet franc N, cabernet-sauvignon N, carmenère N, cot N (ou malbec), merlot N, petit verdot N`。シラーは無い。**
>
> 🔴 **④ コミューンは `Cantenac` ではない。`Margaux-Cantenac` である。—— ブリーフの前提を実測で訂正する。**
> 🏛 **`geo.api.gouv.fr/communes/33268` → `{"nom":"Margaux-Cantenac","code":"33268","anciensCodes":["33091"]}`。`33091` は旧 Cantenac。**
> 🏛 **企業登録の本店表記も `CHATEAU PALMER LD ISSAN 33460 MARGAUX-CANTENAC`（`commune: 33268`）。**
> 🏛 **consolidated CDC のコミューン列挙は 4 つ ——「`Arsac, Labarde, Margaux-Cantenac et Soussans`」。**
> 🔴 ⚠️ **一方 PNO 草案版（2022-09-08）の抽出テキストは 5 つ ——「`Arsac, Cantenac, Labarde, Margaux-Cantenac et Soussans`」。**
> 🔴 **これは §2c の罠（打ち消し線と新値が抽出時に混ざる）の実例そのものである。数えるなら consolidated を数える。** → §Location
>
> 🔴 **⑤ 栽培が本ドシエ最大の節。登録は 3 系統あり、3 つとも別のことを言っている。そして OBP の 5 本には 1 つも適用できない。**
> 🏛 **Agence Bio（SIRET 完全一致）: `numeroBio 157054` / `Ecocert France` / `FR-BIO-01` / `etatCertification: ENGAGEE` / `datePremierEngagement: 2011-09-08` / 活動 `Production` ＋ `Préparation`。**
> 🔴 🏛 **`Raisin de cuve` の `etatProduction` は 2026 年参照で `AB` と `C1` の**両方**が立っている（＝一部区画は今も 1 年目転換中）。**
> 🏛 **Demeter France 加盟（`SC CHATEAU PALMER`）／🏛 Biodyvin (SIVCBD) 会員リストに `Château Palmer / 33460 / Margaux / Bordeaux`。**
> ✅ **造り手自身の年表: 2009 年に 1 ha の試験（`parcelle Boulibranne`）→ 翌年 2 ha →「`Le domaine sera intégralement converti à la biodynamie à partir du millésime 2014`」。**
> 🔴 **したがって OBP の `1996` は転換開始の 13〜15 年前、`2012`/`2013` は移行途中、`2014`/`2017` は転換後。**
> 🔴 **どの 1 本についても「オーガニックです」「ビオディナミです」「Demeter です」「Biodyvin です」と言ってはならない。** → §Farming・§Staff Notes
>
> 🔴 **⑥ canonical `palmer-1855` はボトルではなく「1855 格付の名簿行」である。**
> 🔍 **`vintage: "—"`（U+2014）。`subregion = Margaux` の同型レコードが canonical に 21 件ある。**
> 🔴 🏛 **そして CDC 自身が「le célèbre classement de 1855 … en la dotant d'un `éventail unique de 21 grands crus classés`」と書く。21 という数が一致する。**
> 🔴 **すなわち canonical のこの一群は、意図的に格付名簿を encode したものと読める。OBP 5 行はすべて `vintage gap`。** → §Canonical Conflict ①
>
> 🔴 **⑦ canonical の格納値は、検証可能な 27 主張のうち 15 が失敗した（矛盾 8 / 出典なし 7）。**
> 🔴 **とりわけ `CS約47% / Merlot約47% / PV約6%` は「畑の植栽比率」として提示されているが、**
> 🔴 **公式 Livre de cave の `2016` ヴィンテージのアッサンブラージュ（Merlot 47% / Cabernet sauvignon 47% / Petit verdot 6%）と完全に一致する。**
> 🔴 **＝ 1 ヴィンテージのブレンド値が、生産者の恒久的な植栽比率として格納されている。** → §Canonical Conflict ④
>
> 🔴 **⑧ intake の evidence 文字列が事実として偽である。5 行すべてで同一。**
> 🔍 **`"名称トークン集合一致: 'margaux' ≡ 'Château Palmer'"` —— `{margaux}` と `{château, palmer}` はトークンを 1 つも共有しない。**
> 🔴 **にもかかわらず `cuvee_state: "exact"`。canonical にこの生産者のキュヴェ行が 1 件しかないため、**
> 🔴 **単一候補フォールバックが「トークン集合一致」を名乗って出力していると読める。** → §Canonical Conflict ⑤
>
> ⚠️ **調査上の制約**
> ⚠️ **① 畑の面積（ha）は公式サイトのどこにも無い。**FR 67 ページ全文検索で出るのは歴史上の数値のみ（1814 年以降 Charles Palmer が `163 hectares` まで拡大／1853 年に Pereire 兄弟が `83 hectares` を取得／îlot Domec が `treize hectares`／動物が `28 hectares`）。**canonical の `66ha` は公式で裏が取れない。**
> ⚠️ **② 白ワインについて造り手は完全に沈黙している。**designation の一次確認は Demeter France の登録 1 系統のみ。**ラベル実物での確認が要る。** → Open Questions 2
> ⚠️ **③ プレス素材（Fiches Millésimes / Toolkits / Packshots / Médias）は公式 `presse` ページから Google Drive フォルダへ外部リンクされており、本調査では中身に到達していない。** → Open Questions 6

---

## Identity

| | |
|---|---|
| **OBP 印字** | 🔍 **`Palmer`**（`source_producer_raw`。5 行すべて同一） |
| **公式表記** | ✅ **`Château Palmer`**（サイト全体・`<title>` は `Château Palmer \| Time Always Tells`） |
| 🔴 **法人（公式 mentions légales）** | ✅ **`Identité de l'éditeur du site internet : CHÂTEAU PALMER`**<br>✅ **`Dénomination sociale : Société Civile du Château Palmer`**<br>✅ **`Siège social : Château Palmer, Lieu-dit Issan, 33460 Margaux-Cantenac, France`**<br>✅ **`Numéro d'inscription au RCS : RCS BORDEAUX 781.863.428`**／✅ **`Capital social : 4000 euros`**<br>✅ **`Siret : 781 863 428 00012`**／✅ **`Numéro de TVA intracommunautaire : FR 25781863428`**<br>✅ **`Tél. : +33 (0)5 57 88 72 72`**／✅ **`Directeur de la publication : Thomas Duroux`** |
| 🔴 **法人（🏛 公的登録）** | 🏛 **SIREN `781863428` / `nom_complet: SOCIETE CIVILE DU CHATEAU PALMER`**<br>🏛 **SIRET 本店 `78186342800012`／NAF `01.21Z`（ブドウ栽培）／`nature_juridique 6599`（その他の société civile）**<br>🏛 **住所 `CHATEAU PALMER LD ISSAN 33460 MARGAUX-CANTENAC`（`commune: 33268`／`lat 45.036140302, long -0.668633189`）**<br>🏛 **`etat_administratif: A`／TVA `FR25781863428`／`est_bio: true`／`liste_id_bio: [157054]`**<br>⚠️ **`date_creation: 1900-01-01`（INSEE のプレースホルダ値。創業年ではない）** |
| 🔴 **真正性チェック（§2a）** | 🔴 ✅ **合格。(a) mentions légales の `RCS BORDEAUX 781.863.428` / `Siret 781 863 428 00012` / `TVA FR 25781863428` が 🏛 企業登録と完全一致。**<br>🔴 🏛 **(b) 相互リンクも成立 —— Demeter France の加盟者ページ `SC CHATEAU PALMER` が `http://www.chateau-palmer.com` を掲載している。**<br>🏛 **(c) 住所も一致（`Issan / 33460 Margaux-Cantenac`）。3 条件のうち 3 つを満たす。** |
| 🔴 **経営** | ✅ **`Thomas Duroux` —— 公式表記は `directeur général` および `directeur`。2004 年就任（→ §History）。mentions légales の `Directeur de la publication` でもある。**<br>🏛 **企業登録の gérant に `SASU THDUROUX`（SIREN `891533663`）が入っている。** |
| 🔴 **技術責任者** | ✅ **`Sabrina Pernet` —— 公式表記は `directrice technique`。** |
| 🔴 **株主構成（🏛 実測）** | 🏛 **`dirigeants` は 152 件。内訳は `personne physique` 148 / `personne morale` 4。**<br>🏛 **法人 4 件: `SOCIETE SICHEL`（SIREN `456204445`、`Gérant et associé indéfiniment responsable`）／`FRITZ`（SIREN `518992706`、同）／`SASU THDUROUX`（`Gérant`）／`COMPAGNIE FIDUCIAIRE AUDIT`（`Commissaire aux comptes titulaire`）**<br>🏛 **自然人 148 件のうち 146 件が `Associé indéfiniment responsable`。姓の頻度上位は `BOUTEILLER`(22) / `LODEIZEN`(12) / `BAZIL`(9) / `LACOSTE`(9) / `MAURIAC`(7) / `MÄHLER`系(9)。**<br>🔴 **すなわち「2 家族が共同所有」という要約は、登録上の姿と一致しない。実体は 148 名の無限責任社員を抱える société civile であり、`Société Sichel` と `FRITZ` が gérant を務める。** → §Canonical Conflict ② |
| **その他の役職者（✅ 公式が名指し）** | ✅ **`Nicolas Pescina — technicien du chai`／`Jean-Denis Le Bras — chef exécutif`／`Emilie Husson — bergère`／`Viviane Vincent-Tejero — maraîchère`** |
| **canonical id** | 🔍 **1 件のみ**（`palmer-1855`。下記 §Canonical Conflict） |

### ⚠️ 同名の別事業者 —— **`D-2026-08-05-08` の実測**

| 対象 | 🏛 実測 | 判定 |
|---|---|---|
| 🔴 **Champagne Palmer & Co**（Reims, Marne 51） | 🏛 **`?q=PALMER&departement=51` は 15 件を返すが、`CHAMPAGNE PALMER & CO` という商号の法人は返らない。**同住所（`ZI LA POMPELLE 51100 REIMS`）に `PALM SAS`（SIREN `612028282`、NAF `70.10Z`）と `PALM PACKAGING CHAMPAGNE`（SIREN `808490080`、NAF `17.21A`）が実在する。 | 🔴 **いずれにせよ département 51（Marne）の別法人であり、SIREN `781863428`（Gironde）とは無関係。**⚠️ **Champagne 側の正確な法人特定は本調査では未完了（Open Questions 7）。ただし混同の可能性は SIREN で完全に切れている。** |
| 🔴 **canonical 内の混同** | 🔍 **canonical 928 件を `palmer` で全文走査 → 12 件。うち `producer` 一致 1 件（`palmer-1855`）、prose のみ 11 件。**<br>🔍 **prose 11 件の内訳: `bordeaux-vintage-####-guide` 8 件（1966/1967/1970/1971/1978/1979/1983/1992）＋ `rauzan-gassies-1855` / `durfort-vivens-1855` / `desmirail-1855`。** | 🔴 **11 件すべて Bordeaux 文脈で Château Palmer に言及しているだけで、シャンパーニュとの取り違えは 1 件も無い。**<br>🔴 **canonical に Champagne Palmer & Co のレコードは存在しない。** |
| ⚠️ **`Château Boston`** | 🏛 **`SCEA DU CHATEAU BOSTON`（SIREN `442326526`）の旧本店が `CHATEAU PALMER CANTENAC 33460 MARGAUX-CANTENAC`。2017-06-23 に `etat_administratif: F`（閉鎖）。** | ⚠️ **住所として `Château Palmer` を使っていた別法人。閉鎖済み。**✅ **`Boston` は Palmer の îlot 名として公式に出てくる（`Boston-Boulibranne`）。** |

### ⚠️ §2a で却下・到達不能だったドメイン

| ドメイン | 判定 | 根拠 |
|---|---|---|
| ✅ **`www.chateau-palmer.com`** | ✅ **採用** | **上記のとおり 3 条件を満たす。Webflow ホスティング／`Hébergement: Webflow, inc. + AWS`／`Création du site Internet: NEW NORMAL, 55 boulevard de la Villette, 75010 Paris`。** |
| ⚠️ **`chateaupalmer.com` / `chateau-palmer.fr`** | ⚠️ **到達不能（接続不成立）** | **HTTP コード `000`。パーキングページですらない。内容不使用。** |
| ⚠️ **`palmer.fr` / `chateaupalmer.fr`** | ⚠️ **却下（`HTTP 406 Not Acceptable`）** | **本文が返らない。**⚠️ **これは「Palmer のサイトではない」証明ではなく、単に到達できなかったという記録である。内容不使用。** |
| ✅ **`gcc-1855.fr`**（Conseil des Grands Crus Classés en 1855） | ✅ **採用（限定的）** | 🏛 **mentions légales の `SIRET 48484166300012` が 🏛 企業登録の `CONSEIL DES GRANDS CRUS CLASSES EN 1855`（SIREN `484841663`、`1 COURS DU XXX JUILLET 33000 BORDEAUX`、NAF `94.11Z`、TVA `FR10484841663`）と一致。**⚠️ **ただし本サイトは 1855 年の法令テキストそのものは掲載していない。**→ Open Questions 4 |
| ⚠️ **`biodyvin.com`** | ⚠️ **採用（会員名簿としてのみ）** | **ラベル発行団体自身の会員リストなので membership の一次出典として使う。**⚠️ **サイト自体は「2012 ©」表記で、`Un nouveau site est en cours de préparation ! Début 2026` と告知している。加入年は載っていない。** |
| ❌ **小売／オークション／評論家／アグリゲータ** | ❌ **一切不使用** | **`Vin Blanc de Palmer` の検索で idealwine / Vivino / CellarTracker / Wine-Searcher / Falstaff 等が返ったが、事実出典としては 1 語も使っていない。**→ §Open Questions 2 に「未検証の第三者主張」として名前のみ記録。 |

---

## Overview

✅ **Château Palmer は Gironde 県 Margaux-Cantenac の Lieu-dit Issan にある。AOC Margaux の 3ème cru（1855）。
運営は `Société Civile du Château Palmer`（SIREN 781863428）。2004 年から `Thomas Duroux` が directeur général、
技術は `Sabrina Pernet` が directrice technique を務める。**

🔴 ✅ **公式が自らの署名として名指しするものは、はっきりと 3 つある。**

🔴 ✅ **① 「2 本の兄弟」であって「グラン・ヴァンとセカンド」ではない。**
「**Palmer et son Alter Ego, son « autre moi », sont `deux expressions distinctes du même terroir`,
deux interprétations d'une même partition, `deux étiquettes en miroir`. L'outre bleu et la lumière qu'il réfléchit.**」（`/gamme`）
🔴 **`Alter Ego` のページ見出しは `L'autre grand vin de château palmer`。本文は `cet « autre vin »`。**
🔴 **`second vin` / `second wine` / `deuxième vin` は公式のどこにも無い（FR 67 ページ＋EN 2 ページを全文検索、0 件）。**

🔴 ✅ **② カベルネ・ソーヴィニヨンとメルロが同率という植栽。**
「**le domaine compose avec une grammaire en `trois piliers` : `le cabernet sauvignon et le merlot à part égale`,
complétés par `une touche de petit verdot`. Un `encépagement singulier pour la région`,
dont le corps et le cœur sont constitués de `vieux merlots plantés dans les années 1930` sur de grands terroirs à cabernet.**」（`/domaine`）
⚠️ 🔴 **公式は「同率（à part égale）」としか書かず、パーセンテージを一切出さない。**
🔴 **数字が出るのは `Livre de cave` の**ヴィンテージごとのアッサンブラージュだけであり、それは年ごとに大きく振れる**（下記 §Important Cuvées）。**

🔴 ✅ **③ ビオディナミを軸にした「ferme holistique」。**
「**L'un des principes fondateurs de la biodynamie est de considérer chaque élément du vivant comme faisant partie d'un tout.
… le vignoble de Château Palmer est un `vaste écosystème, une ferme holistique et circulaire`,
un organisme vivant dont l'essence, la vraie nature, est d'être `autonome et équilibré`.**」（`/domaine`）
✅ **Duroux の一文: 「`Faire un grand vin, c'est mettre un lieu dans un verre.`」**

🔍 **THÉSEUS における状態は「1 行しかないのに 5 行が当たりに来る」形。
canonical はこの生産者について `palmer-1855` の 1 レコードしか持たず、しかもそれは `vintage: "—"` の名簿行である。
OBP の 5 行はすべて実在するヴィンテージだが、受け皿となる行が 1 つも無い。
すなわち主たる問題は矛盾ではなく `不在` であり、その上に `格納値の誤り` が重なっている。**

---

## History

✅ **公式の沿革は `/domaine` の `HÉRITAGE` 節と、`/theme/heritage` 配下の記事群にある。以下は公式の記述のみ。**

| 年 | 出来事 ✅ |
|---|---|
| 🔴 **1814** | 🔴 **`Charles Palmer` が `domaine de Gascq` を取得。**✅ **公式の記述は「`En 1814, le Lieutenant-Colonel Charles Palmer` fait parler de lui … ce `futur Major Général` de l'armée britannique et `aide de camp du Prince régent, le futur roi George IV`」。**<br>✅ **「`Madame Marie Brunet de Ferrière, veuve de Gascq`, n'y résiste pas. Lors d'un long voyage de Bordeaux à Paris, assise à ses côtés, la jeune veuve lui vend `en une journée` la propriété viticole médocaine dont elle vient d'hériter. `Sans même l'avoir visité`, ce `fils de brasseur de Bath` devient propriétaire du domaine de Gascq, `réputé pour la qualité de ses vins depuis le début du XVIIIe`」**<br>🔴 ⚠️ **取得時の階級は `Lieutenant-Colonel`。`Major Général` は「futur」と明記されている。** |
| **1814–1843** | ✅ **「`En près de 30 ans`, le gentleman s'emploie à l'agrandir, à le moderniser et à lui donner un style intemporel」**<br>✅ **別記事: 「Il acheta terres et vignobles alentour jusqu'à atteindre bientôt `163 hectares`, de `Cantenac à Issan et Margaux`. Il fit construire des logements …, un chai abritant `15 fûts de chêne et trois pressoirs`」**<br>✅ **「… la Caisse hypothécaire, en `1843`」／「Charles Palmer `mourra avant` de voir le château portant son nom entrer … dans le célèbre classement de 1855」** |
| 🔴 **1853** | 🔴 **`Émile et Isaac Pereire` が取得。**✅ **「Chemins de fer, immobilier, banque … En `1853`, ils font l'acquisition du domaine, l'organisent autour d'un `château néo-Renaissance` et donnent vie au fameux `« village »`」**<br>✅ **別記事: 「Ils rachètent alors le domaine et son `vignoble de 83 hectares` à la `Caisse hypothécaire`」** |
| 🔴 **1855** | 🔴 ✅ **公式の言い回しはこうである ——「alors que `le rang de troisième cru`, `attribué depuis longtemps à Palmer par les négociants et les grands prescripteurs`, `est consacré par le Classement impérial`」**<br>🔴 **すなわち公式は「3 級に留まった」とは書かない。「以前から与えられていた 3 級という順位が、帝国の格付によって追認された」と書く。** → §Staff Notes ⚠️ ① |
| **19 世紀末〜第一次大戦** | ✅ **「Malgré l'oïdium, le phylloxera et le mildiou, qui sévissent à la fin du XIXe siècle, malgré les horreurs de la Grande Guerre, les frères Pereire n'auront de cesse de développer Château Palmer」** |
| 🔴 **1938** | 🔴 ✅ **「`Depuis 1938`, Château Palmer se distingue parmi les plus grands crus bordelais. En moins d'un siècle, `quatre dynasties d'abord, puis deux d'entre elles`, conduisent le domaine vers la reconnaissance」**<br>✅ **「D'un côté, la famille `Mähler-Besse`, originaire des `Pays-Bas`, qui s'est imposée dans `le commerce du textile et le négoce des vins`. De l'autre, la famille `Sichel`, spécialisée en `Angleterre, France et Allemagne` dans la `distribution de grands crus`」**<br>🔴 ⚠️ **公式は「4 家族 → うち 2 家族」と書く。「4 回のオーナー交代」ではない。** |
| **戦後** | ✅ **「Ensemble, leurs descendants `reconstruisent le vignoble après-guerre`, signent plusieurs millésimes d'exception, `dont un légendaire 1961`」** |
| 🔴 **1998** | 🔴 ✅ **`Alter Ego` 誕生。「`Alter Ego a été lancé avec le millésime 1998`, dans l'idée de produire `une autre facette de Palmer`」** |
| 🔴 **2004** | 🔴 ✅ **`Thomas Duroux` に direction を委ねる。「avant de confier `en 2004` à `Thomas Duroux` la direction de Château Palmer et de continuer à faire évoluer le domaine `dans un esprit plus responsable`」**<br>✅ **同年、`Historical XIXth Century Wine` が `lots de 2004` で実験開始。** |
| **2005** | ✅ **「Invité en `2005` par un collectionneur californien, Thomas Duroux est … bouleversé par la dégustation d'un `Château Palmer 1869`」→ Historical XIXth Century Wine の着想。** |
| 🔴 **2009** | 🔴 ✅ **ビオディナミ第 1 歩。「les principes de l'agriculture biodynamique s'invitent `en 2009` avec `un premier essai sur une parcelle témoin d'un hectare`, porté sur `deux hectares l'année suivante`」**<br>✅ **Pernet の証言: 「Nous avons expérimenté la biodynamie sur `un premier hectare, en 2009, sur la parcelle Boulibranne`」** |
| 🔴 **2014** | 🔴 ✅ **全面転換。「`Le domaine sera intégralement converti à la biodynamie à partir du millésime 2014`」／「Château Palmer … `parachève avec panache sa conversion à 100% en agriculture biologique et biodynamique`」**<br>✅ **同年、ヴァンダンジュへの亜硫酸添加を初めて全面停止（下記 §Winemaking）。**<br>✅ **同年末、「`Fin 2014`, les premières vaches rejoignent les brebis landaises pour fournir la propriété en compost」（品種は `La Bordelaise`、`Conservatoire des Races d'Aquitaine` の助力）** |
| **2016** | ✅ **「A l'élevage s'ajoute, `fin 2016`, un projet d'`agroforesterie` initié avec la plantation de `plus d'un kilomètre de haies` mais aussi, le repiquage des `cent premiers fruitiers` au milieu des vignes」** |
| **2018** | ✅ **「`Depuis 2018`, le domaine est découpé en `cinq îlots`」** |
| **2020** | ✅ **「En `2020`, Palmer accueille sa maraîchère, `Viviane Vincent-Tejero`」／初収穫は 2020 年 7 月。** |
| **2023** | ✅ **現行サイトの公開。`Date de publication du Site Internet : Juin 2023`（mentions légales）。** |

⚠️ **公式沿革に無いもの**: 1843–1938 の所有者の系列（「4 家族」の内訳）、Mähler-Besse / Sichel が入った正確な年、
Alter Ego 以前の第 2 のワインの有無、白ワインの歴史、`Vin Blanc de Palmer` / `Blanc de Palmer` の初リリース年。 → Open Questions 2・8

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Bordeaux — Médoc** ✅ |
| 🔴 **Appellation** | 🔴 🏛 **`AOC Margaux`。**🏛 **「Seuls peuvent prétendre à l'appellation d'origine contrôlée « Margaux », `initialement reconnue par le décret du 10 août 1954` …」**<br>🔴 🏛 **「L'appellation d'origine contrôlée « Margaux » est `réservée aux vins tranquilles rouges`」（III 章）** |
| 🔴 **Commune** | 🔴 🏛 **`Margaux-Cantenac`（INSEE `33268`、CP `33460`）。`anciensCodes: ["33091"]` ＝ 旧 `Cantenac`。**<br>🔴 **すなわち Cantenac と Margaux は commune nouvelle に統合されており、現在「Cantenac というコミューン」は存在しない。**<br>✅ **公式 mentions légales の本店表記も `33460 Margaux-Cantenac`。**<br>⚠️ **ただし公式の歴史記事は今も `de Cantenac à Issan et Margaux` という 19 世紀の地名を使う。歴史記述と現在の行政区画は別物である。** |
| 🔴 **所在（lieu-dit）** | 🔴 ✅ 🏛 **`Lieu-dit Issan`。**公式・企業登録・Agence Bio・Ecocert・Demeter の 5 系統すべてが `Issan` を言う。<br>🏛 **企業登録の座標 `45.036140302, -0.668633189`。** |
| 🔴 **CDC のコミューン列挙（🏛 consolidated）** | 🔴 🏛 **「La récolte des raisins, la vinification, l'élaboration et l'élevage des vins sont assurés sur le territoire des communes suivantes du département de la Gironde sur la base du `code officiel géographique en date du 1er janvier 2022` : `Arsac, Labarde, Margaux-Cantenac et Soussans`」**<br>**出典: `Cahier des charges de l'AOC « MARGAUX » homologué par arrêté du 31 mars 2023, publié au JORF du 5 avril 2023`（BO du MASA、2023-04-13）** |
| 🔴 ⚠️ **CDC のコミューン列挙（🏛 PNO 草案）** | 🔴 ⚠️ **`extranet.inao.gouv.fr/fichier/3-CDC-Margaux.pdf`（PNO、2022-09-08 の Comité national の avis に続く手続き版）は、同じ箇所を `Arsac, Cantenac, Labarde, Margaux-Cantenac et Soussans` と抽出する。**<br>🔴 **これは §2c の罠そのもの ——「Les dispositions proposées à la suppression apparaissent en caractères barrés」と冒頭で明言されており、抽出テキストでは打ち消し線が消える。**<br>🔴 **数えるなら consolidated（4 コミューン）を数える。5 と書いてはならない。** |
| 🔴 **CDC の品種（🏛）** | 🔴 🏛 **主要品種: `cabernet franc N`, `cabernet-sauvignon N`, `carmenère N`, `cot N (ou malbec)`, `merlot N`, `petit verdot N`。**<br>🏛 **`variété d'intérêt à fin d'adaptation`: `castets N`（`≤ 5%` of encépagement、INAO/ODG との convention 締結が条件）。**<br>🔴 **シラーは無い。白品種も無い。** |
| 🏛 **CDC の主要数値** | 🏛 **植栽密度 最低 `7 000 pieds/ha`／畝間 `≤ 1,50 m`／株間 `≥ 0,80 m`／1 株あたり最大 `1,43 m²`**<br>🏛 **最低自然アルコール度数 `11 %`／rendement `57 hl/ha`／rendement butoir `63 hl/ha`（畝間 1,40–1,50 m かつ葉層高が畝間の 0,6–0,7 倍の場合は `60 hl/ha`）**<br>🏛 **仕立て: `taille dite « médocaine » à astes` 等、`maximum de douze yeux francs par pied`** |
| 🏛 **CDC のラベル規定** | 🏛 **「L'étiquetage peut préciser l'unité géographique plus grande `« Vin de Bordeaux - Médoc »` ou `« Grand Vin de Bordeaux - Médoc »`」（文字は AOC 名の 2/3 以下）** |
| 🔴 **土壌（✅ 公式）** | 🔴 ✅ **`Plateau des Brauzes` —— 「`première terrasse de graves charriés par la Garonne à la faveur de deux périodes glaciaires`」**<br>✅ **「Sous nos pieds par milliers, `les graves`, un ensemble de pierres … `lydiennes, quartzites, calcédoines`, héritage de l'ère quaternaire … `Il y a plus d'un million d'années, la Garonne les a déposées là, en terrasses`」**<br>✅ **「Dans ces `sols lessivés et pauvres … en matières organiques`, elles n'autorisent pas la vigne à pousser fort … En couches successives, elles assurent `un parfait drainage` et `restituent la chaleur emmagasinée`」**<br>✅ **「véritable `mosaïque de sols` regardant `l'estuaire de la Gironde`」／Médoc の格言「`Les grands terroirs sont ceux qui regardent la rivière.`」** |
| 🔴 **区画構成（✅ 公式）** | 🔴 ✅ **「`Depuis 2018`, le domaine est découpé en `cinq îlots`」。公式が名指しする 5 つ ——**<br>✅ **`Boston-Boulibranne`（最も外れた・最も野生的な îlot。20 年ほど前に植えた若い cabernet-sauvignon。2017 年は霜で収穫が全滅。防霜用の éolienne と bougie〈2021 年に初点火〉）**<br>✅ **`Les 40s-50s`（`une vingtaine de parcelles` を鉄道が分断。主に merlot、少量の cabernet sauvignon と petit verdot）**<br>🔴 ✅ **`Le Cassena`（城から 3 km、森に接し果樹が点在。`le plus varié` の îlot で、**`en plus des rouges, quatre cépages de blanc`**を含む）**<br>✅ **`Le Plateau`（最も古い樹、河口に最も近い。`plateau des Brauzes`。城の真裏。`parcelle 46` は株数を倍にして `20.000 pieds par hectare`、`parcelle 16` は `palissage à 1m80`）**<br>✅ **`Domec`（`un ensemble de treize hectares entre le chai et la route des vins`）** |
| 🔴 **植栽密度（✅ 公式）** | 🔴 ✅ **「Nous avons `10 000 pieds par hectare`, chaque plan de vigne a donc `un mètre carré` pour s'exprimer」（Sabrina Pernet）**<br>✅ **一部区画は `20.000 pieds par hectare`（parcelle 46）。**🏛 **CDC の下限 `7 000` を大きく上回る。** |
| 🔴 **樹齢（✅ 公式）** | 🔴 ✅ **「dont le corps et le cœur sont constitués de `vieux merlots plantés dans les années 1930` sur de grands terroirs à cabernet」** |
| 🔴 ⚠️ **面積** | 🔴 ⚠️ **公式サイトに現在の栽培面積の記載が無い。**FR 67 ページ全文検索で得られる ha 値は歴史・別用途のもののみ ——<br>✅ **`163 hectares`（Charles Palmer が拡大した先、19 世紀）／`83 hectares`（1853 年に Pereire 兄弟が Caisse hypothécaire から取得した vignoble）／`treize hectares`（îlot Domec）／`28 hectares`（家畜が使う面積。「Il en faudrait presque le double pour atteindre l'autonomie visée」）**<br>🔴 **canonical の `66ha` は公式で裏づけられない。** → §Canonical Conflict ④・Open Questions 3 |
| 🏛 **活動所在地（Agence Bio）** | 🏛 **2 か所が `Lieux d'activité` として登録されている ——`LD ISSAN 33460 MARGAUX-CANTENAC`（`Siège social` 兼）と `28 ROUTE DU PORT ISSAN 33460 MARGAUX-CANTENAC`。** |
| ⚠️ **Ecocert の住所表記** | ⚠️ **Ecocert の証明ページは `Issan / 33460 / MARGAUX` と表記する（`-Cantenac` が無い）。**⚠️ **同一事業者だが、登録ごとにコミューン名の書き方が揃っていない。** |

❓ **公式に無い**: 現在の総栽培面積、区画数、区画別の面積・土壌断面・標高、5 つの îlot の面積内訳、白品種の 4 つの名前。

---

## Farming

🔴 **本節の要点は 2 つ。**
🔴 **① Palmer は有機・ビオディナミの登録を「3 系統」持っている。それぞれ別のことを保証している。**
🔴 **② そして OBP の 5 本（1996 / 2012 / 2013 / 2014 / 2017）には、そのどれ 1 つも適用できない。**

### 🔴 🏛 ① 有機（EU）—— Agence Bio ＋ Ecocert

🔴 **`GET https://opendata.agencebio.org/api/gouv/operateurs/?siret=78186342800012` → `nbTotal: 1`（SIRET 完全一致の陽性）**

| 項目 | 🏛 登録値（verbatim） |
|---|---|
| **raisonSociale** | **`SOCIETE CIVILE DU CHATEAU PALMER`** |
| 🔴 **numeroBio** | 🔴 **`157054`**（企業登録の `liste_id_bio: [157054]` と一致） |
| **codeNAF** | **`01.21Z`** |
| 🔴 **certificats[0].organisme** | 🔴 **`Ecocert France`** |
| 🔴 **numeroControleEu** | 🔴 **`FR-BIO-01`** |
| 🔴 **etatCertification** | 🔴 **`ENGAGEE`**（`dateSuspension: null` / `dateArret: null`） |
| 🔴 **dateEngagement / datePremierEngagement** | 🔴 **`2011-09-08`**（`dateNotification: 2011-09-06T22:00:00Z`） |
| 🔴 **activites** | 🔴 **`Production` ＋ `Préparation`（2 つとも）** |
| **mixite** | **`Non`** |
| **dateMaj** | **`2025-02-03`** |
| **証明 URL** | 🏛 **`https://certificat.ecocert.com/entreprise/D3C0543A-52D4-4E50-A128-65CC0AEF0DBA`** |

🔴 **Ecocert 証明ページ（実読）**

- 🏛 **`CHATEAU PALMER` / `Issan / 33460 MARGAUX / France`**
- 🔴 🏛 **`Certification Agriculture biologique Europe (EU) 2018/848 [FR]`／表示は `Document en vigueur`（現行）**
- 🔴 🏛 **`Activités : Agriculteur (production végétale), Agriculteur (production animale), Fabricant & Transformateur`**
- 🏛 **`4 Catégories de produits`: `Animaux et dérivés`（Animaux et produits animaux）／`Boissons`（Boissons alcoolisées）／`Végétaux et dérivés`（Fruits, noix, légumes et dérivés／`Surface de biodiversité`）**
- ⚠️ **証明書番号と有効期間は HTML 上に表示されない（PDF ダウンロードが別導線）。** → Open Questions 5

🔴 **`etatProduction` の実測（`anneeReferenceControle: 2026`）—— ブドウだけが 2 状態を持つ**

| production | code | 🏛 etatProduction |
|---|---|---|
| 🔴 **Raisin de cuve** | **`01.21.12`** | 🔴 **`C1` と `AB` の**両方** |
| 🔴 **Vins de raisin** | **`11.02`** | 🔴 **`AB`** |
| **Prairie temporaire** | `01.19.10.11` | `AB` |
| **Prairie permanente** | `01.19.10.12` | `CS` と `AB` |
| **Vaches allaitantes** | `01.42.11.1` | `AB` と `CNS` |
| **Bœufs / Génisses / Veaux** | `01.42.11.2` 他 | `AB` |
| **Taureaux (>24 mois)** | `01.42.11.3` | `CNS` |
| **Brebis viande / Agneaux / Béliers / Chèvres / Bouc** | `01.45.*` | `AB` |
| **Truies / Porcs charcutiers / Porcelets / Verrats** | `01.46.10.*` | `AB` |

→ 🔴 **`Raisin de cuve` に `C1`（転換 1 年目）の行が 2026 年参照で立っている。**
→ ⚠️ **これは「Palmer 全体がまだ転換中」を意味しない。同一 production コードに複数の区画状態が並ぶのが登録の仕様である。**
→ 🔴 **しかし「Palmer の畑は 100% 有機認証済みです」と断定してはならない、という制約にはなる。**

### 🔴 🏛 ② ビオディナミ —— Demeter France ＋ Biodyvin

🔴 **Demeter France の加盟者ページ `https://www.demeter.fr/adherents/sc-chateau-palmer/`（実読）**

- 🏛 **名称 `SC CHATEAU PALMER`／`Types de produits: Vins, bières et spiritueux`**
- 🏛 **`Coordonnées: Issan / 33460 MARGAUX CANTENAC / +33 (0)5 57 88 72 72 / http://www.chateau-palmer.com`**
- 🔴 🏛 **`Liste de produits`（全 8 件、verbatim）**

| # | 🏛 Demeter 登録上の製品名 |
|---|---|
| 1 | **`Vin blanc 2024 - 2025`** |
| 2 | 🔴 **`Vin blanc Vin de France "Blanc de Palmer" 2020 - 2021`** |
| 3 | 🔴 **`Vin blanc Vin de France "Blanc de Palmer" 2022 - 2023`** |
| 4 | **`Vin rouge 2024 - 2025`** |
| 5 | 🔴 **`Vin rouge Margaux "Alter Ego" 2019 - 2020`** |
| 6 | 🔴 **`Vin rouge margaux "alter ego" 2021 - 2022`** |
| 7 | 🔴 **`Vin rouge margaux "château palmer" 2019 - 2020`** |
| 8 | 🔴 **`Vin rouge margaux "château palmer" 2021 - 2022`** |

→ 🔴 **これが白ワインの designation を裏づける唯一の一次資料である。`Vin de France`、名称は `Blanc de Palmer`。**
→ 🔴 **そして登録の年レンジは `2019-2020` / `2021-2022` / `2024-2025` のみ。OBP の 1996–2017 を覆う行は 1 つも無い。**
→ 🔴 **`Historical XIXth Century Wine` はこのリストに存在しない。**
⚠️ **`2019 - 2020` 等が「ヴィンテージの対」なのか「認証の参照年度」なのかは、Demeter のページからは決まらない。文字列のまま記録する。** → Open Questions 5

🔴 **Biodyvin（SIVCBD）会員リスト `https://www.biodyvin.com/fr/liste-des-membres-biodyvin.html`（実読）**

- 🏛 **表題は `224 adhérents en 2025`。行 `Château Palmer / 33460 / Margaux / Bordeaux` が実在する。**
- 🏛 **ラベルの仕組み（同サイト `le label biodyvin`）: 「le syndicat a décidé de mandater un organisme indépendant, `ECOCERT SAS FRANCE`, afin qu'il vérifie sur chaque exploitation … `A la fin des 4 années de conversion à la bio-dynamie`, le SIVCBD délivre le label `BIODYVIN` aux adhérents ayant été contrôlés sur cette période」**
- ⚠️ **会員リストに加入年は無い。したがって「いつから Biodyvin なのか」は本調査では決まらない。** → Open Questions 5

### 🔴 ✅ ③ 造り手自身の年表 —— **転換は段階的で、2014 に完了したと公式が言う**

| 年 | ✅ 公式の記述 |
|---|---|
| 🔴 **2009** | 🔴 **「les principes de l'agriculture biodynamique s'invitent `en 2009` avec `un premier essai sur une parcelle témoin d'un hectare`」／Pernet「Nous avons expérimenté la biodynamie sur `un premier hectare, en 2009, sur la parcelle Boulibranne`. Nous avons étudié les `micro-vinifications`, organisé des `dégustations à l'aveugle`」** |
| **2010** | **「porté sur `deux hectares l'année suivante`. `Et ainsi de suite.`」** |
| 🔴 **2013 →** | 🔴 **Duroux「`Après 2013`, nous nous sentions prêts à prendre nos responsabilités et à `convertir la totalité du vignoble en biodynamie`」** |
| 🔴 **2014** | 🔴 **「`Le domaine sera intégralement converti à la biodynamie à partir du millésime 2014`」**<br>🔴 **「Château Palmer bouscule les conventions et `parachève avec panache sa conversion à 100% en agriculture biologique et biodynamique`. `En 2014, la biodynamie n'est ainsi plus une intuition ou une promesse, mais un acquis` déterminant pour la décennie à venir」**<br>**Pernet「`En 2014`, l'écosystème tend vers son équilibre et nous pouvons `franchir cette étape décisive` de notre vision」** |

### 🔴🔴 温度差の罠 —— **OBP の 5 本に、どのラベルも貼れない**

🔴 **`datePremierEngagement = 2011-09-08`（🏛）と「2014 年ミレジムから全面転換」（✅）を、OBP の 5 行に突き合わせる。**

| OBP VT | 🏛 有機（Agence Bio） | ✅ 造り手のビオディナミ | 🏛 Demeter | 🏛 Biodyvin | 🔴 卓上で言えること |
|---|---|---|---|---|---|
| 🔴 **1996** | **engagement の 15 年前** | **最初の 1 ha 試験の 13 年前** | **登録に該当行なし** | **不明** | 🔴 **「オーガニック」も「ビオディナミ」も**一切言えない**。同時に「有機的なことは何もしていなかった」も言えない（当時の実務を公式が何も書いていない）** |
| 🔴 **2012** | **engagement の翌年（＝転換期）** | **段階的拡大の途中。全面転換前** | **該当行なし** | **不明** | 🔴 **「オーガニック」と言ってはならない。「ビオディナミ」とも言ってはならない。「2009 年から段階的にビオディナミの試験を進めていた時期のワインです」までが言える上限** |
| 🔴 **2013** | **同上** | 🔴 **Duroux が「`Après 2013` … 全面転換を決めた」と書く年。すなわち 2013 は転換前** | **該当行なし** | **不明** | 🔴 **同上。加えて「2013 の経験が全面転換の引き金になった」とは公式に基づいて言える** |
| 🔴 **2014** | ⚠️ **engagement から 3 年目。ただし操作者の `etatCertification` は今も `ENGAGEE`** | 🔴 **公式が「100% 転換を完遂した年」と明言する** | **該当行なし** | **不明** | 🔴 **「造り手は 2014 年ミレジムで畑の 100% をビオディナミへ転換し終えたと公表しています」は言える。**🔴 **「このボトルはオーガニック認証です／Demeter です／Biodyvin です」は言ってはならない（ラベル未確認・登録の年レンジ外）** |
| 🔴 **2017** | ⚠️ **同上** | 🔴 **全面転換の 3 年後** | **該当行なし** | **不明** | 🔴 **同上。**⚠️ **加えて 2017 は霜の年で、公式が「`En 2017, le gel avait condamné la récolte`」と書くのは `Boston-Boulibranne` の îlot についてである（畑全体ではない）** |

→ 🔴 **結論。5 本すべてについて、「認証」を語る言葉を使ってはならない。**
→ 🔴 **語ってよいのは「造り手が公表している転換の年表」であり、それは 2009 → 2014 という 2 つの年だけである。**
→ ⚠️ **`D-2026-08-05` の 3 例（Moussé / Giraud / Dauvissat）と同じ形が、ここでは 5 本中 5 本に当たっている。**

### ✅ 栽培の実務（公式が名指しするもの）

🔴 ✅ **家畜と堆肥。**「`Fin 2014`, les premières vaches rejoignent les brebis landaises pour `fournir la propriété en compost`.
Les équipes, avec l'aide du `Conservatoire des Races d'Aquitaine`, choisissent une race du cru. L'élue ? `La Bordelaise` …
Ayant débuté avec `trois têtes de bétail`, le troupeau … en compte désormais `une trentaine`, cohabitant … avec `les chèvres, les brebis, les porcs gascons et diverses volailles`.
Les vaches de Palmer produisent `un précieux fumier` qui, `mélangé à des sarments de vignes broyés et à des rafles de vendanges`, produit `un fertilisant unique`.」

🔴 ✅ **アグロフォレストリー。**「`fin 2016`, un projet d'`agroforesterie` … `plus d'un kilomètre de haies` … `cent premiers fruitiers` au milieu des vignes.
`En moins de trois ans`, ce sont `plus d'un millier d'arbres` qui auront été plantés au milieu des parcelles, `à raison d'une quinzaine de plants par hectare`.
… `Cerisiers Napoléon, poiriers Williams, abricotiers Bergeron`」

✅ **防霜。**`Boston-Boulibranne` について「`éoliennes de secours contre le gel tardif`, `arsenal de bougies allumées pour la première fois en 2021`, `pulvérisations régulières de tisane sur la vigne`」

✅ **農薬。**vigneronne の証言として「l'`absence de pesticide`」が引用されている。
⚠️ 🔴 **ただしこれは従業員の発言の引用であり、公式が制度として「無農薬」を宣言した文ではない。断定に使ってはならない。**

⚠️ **公式に無い**: 認証の取得年（公式は Ecocert / Demeter / Biodyvin / AB のどの語も一度も使わない — **全 67 ページ検索で 0 件**）、
HVE / Terra Vitis の有無（**0 件**）、調合剤の種類と散布回数、被覆作物、馬耕、銅の使用量。 → Open Questions 5

---

## Winemaking

### 🔴 ✅ 醸造施設（`/domaine` の `AU CHAI`）

🔴 ✅ **`LE CUVIER`** — 「il accueille les raisins fraîchement vendangés dans des `cuves tronconiques` d'une contenance de
`89 à 195 hectolitres` où ils débuteront leur fermentation. `54 cuves thermorégulées` pour un travail `parcellaire, voire même intra-parcellaire`, des plus pointus.
À la clef, l'expression exacte de la typicité de chaque terroir, et `le moins d'intervention possible`.」
🔴 **EN 版 Alter Ego ページも「the vinification process is adapted to `each of the 54 vats` depending on which wine they will contain」と 54 を反復する。**

🔴 ✅ **`LE CUVIER EXPÉRIMENTAL`** — 「Un lieu unique en son genre, où `un laboratoire et neuf micro-cuves` foisonnent d'essais permanents.
Les recherches menées ici ont, par exemple, permis de `réduire l'utilisation du soufre de moitié` lors des vinifications
`par l'élaboration de pieds de cuve en propre`.」

### 🔴 ✅ 熟成 —— **「二段階」。20〜22 か月**

🔴 ✅ **「`L'élevage en deux temps`. … Ici, aux `« Jasmins »` comme dans la pénombre de l'historique chai des `« Marronniers »`, règne un silence monacal.
… En l'occurrence `vingt à vingt-deux mois d'élevage`, d'abord `en barriques de 225 litres` – `du bois neuf pour moins de la moitié d'entre elles`, le respect du vin en ligne de mire… –
puis `en foudres de 30 hectolitres` qui viendront `patiner le vin dans sa seconde année`.」（`/domaine`）

🔴 ✅ **グラン・ヴァンのページも同じ数字を独立に言う** — 「car `un long vieillissement de 20 à 22 mois`, `en fûts puis en foudres`, est nécessaire pour imprimer dans le vin le message de son sol」

🔴 ✅ **瓶詰前の均一化** — 「`Les barriques de chêne neuf et usagé sont assemblées en cuves quelques semaines avant la mise` afin d'homogénéiser les vins.」

🔴 ✅ **瓶熟の第一段階** — 「le `caveau historique` de la propriété peut accueillir une partie des précieuses bouteilles pour `un premier cycle de dix ans de garde`.
Pour Palmer, `ces dix ans marquent un âge de raison`」

🔴 **canonical は `18〜21ヶ月` と書く。公式は 2 か所で `20 à 22 mois` と書く。** → §Canonical Conflict ④

### 🔴 ✅ 亜硫酸 —— **2014 年ヴァンダンジュから無添加**

🔴 ✅ **「Au cuvier, l'innovation est à l'honneur, puisqu'`après deux ans d'expérimentation sur la réduction des doses de soufre` dans nos vins,
nous décidons de `ne plus sulfiter la vendange` et de laisser le raisin exprimer immédiatement sa complexité.」（Fiche Millésime 2014）**
🔴 ✅ **「`pour la première fois de l'histoire moderne de la propriété, on ne sulfite plus la vendange`.
`Retarder les apports de soufre` permet de mieux goûter les cuves, de mieux comprendre l'extraction des tanins」（記事 2014）**
⚠️ 🔴 **これは「収穫物への添加をやめた」であって「亜硫酸無添加ワイン」ではない。公式は `Retarder les apports` と書いている。混同してはならない。**

### 🔴 ✅ アッサンブラージュ —— **2 本は収穫の時点で分かれる**

🔴 ✅ **「pour `Alter Ego`, le choix est fait de `privilégier les maturités technologiques et aromatiques` afin de créer une expression centrée sur `le fruit et la souplesse`, plus abordable dans la jeunesse du vin.」**
🔴 ✅ **「Pour `Palmer`, c'est davantage sur leur `maturité phénolique, leur densité et leur profondeur` que les raisins sont sélectionnés.
`Palmer et son Alter Ego naissent ainsi dès la vendange`. Une fois au chai, les vinifications s'adaptent en fonction de `l'attribution de chacune des cuves à l'un ou l'autre des vins`.」**
✅ **「`L'assemblage, comme un geste de peintre.`」**

⚠️ **公式に無い**: 発酵温度、酵母（`pieds de cuve en propre` の記述はあるが詳細なし）、マセラシオン日数、圧搾方式、
瓶詰日、アルコール度数、生産本数（`Historical XIXth Century Wine` の約 5000 本を除く）、樽職人名。

---

## Style

### ✅ 公式のスタイル記述（**造り手自身の言葉のみ**）

| 対象 | ✅ 公式の記述 |
|---|---|
| 🔴 **Château Palmer**（`/chateau-palmer`） | **「Château Palmer a toujours `transcendé les modes et les tendances` pour n'écouter qu'une seule voix : `celle de son terroir`.<br>`Finesse et élégance de son enracinement margalais`, `texture de la soie`, `noblesse du cuir`, `caresse du velours` :<br>`un assemblage quasi identique de cabernet sauvignon et de merlot, auquel s'ajoute une touche de petit verdot`, signe le style Palmer.<br>On plonge le nez dans `un bouquet de fleurs, de fruits, d'épices`, enveloppés dans une `structure charnue et généreuse`.」** |
| 🔴 **Alter Ego**（`/alterego`） | **「`Spontané, rond, généreux, sur la soie`, cet « autre vin » est tout à la fois `intense et léger, riche et délicat`.<br>Il possède `l'élégance et le grain de tanin de son aîné`.」**<br>**「né dans `la soie et les fines graves sableuses` typiques de son appellation, Alter Ego développe `la délicatesse poudrée des grands vins de Margaux` …<br>Avec `un assemblage dans lequel prédomine souvent le merlot`, sa dimension aromatique séduit, sa texture originelle se laisse aborder.<br>`Plus ouvert dans sa jeunesse que son aîné`, il n'empêche que l'âge lui profite aussi.」**<br>**Duroux: 「`Alter Ego se bonifie avec le temps.` Si vous ouvrez aujourd'hui un 2009, vous comprendrez l'intérêt d'avoir été patient…」** |
| 🔴 **2 本の関係（`/gamme`）** | **「Palmer et son Alter Ego, son « autre moi », sont `deux expressions distinctes du même terroir`, `deux interprétations d'une même partition`, `deux étiquettes en miroir`.」**<br>**Alter Ego ページの見出し: 「`SI PALMER EST UNE SYMPHONIE ORCHESTRALE À BASE DE GRAVES, ALTER EGO EST UNE FULGURANCE D'UN THÈME DE JAZZ.`」**<br>⚠️ **EN 版は「IF PALMER IS AN `ORCHESTRAL SYMPHONY COMPOSED FROM GIRONDE GRAVELS`, ALTER EGO IS A `JAZZ RIFF EMERGING FROM THE SAME WONDROUS GEOLOGY`.」— 直訳ではない。** |
| **品種の役割（`/domaine`）** | **「Cépage précoce, `le merlot` confère `de la générosité, de la souplesse` et signe `le velours unique` des vins de Château Palmer.<br>Fait d'un bois dur, `le cabernet` donne à Château Palmer `sa puissance contenue et la richesse de sa matière`.<br>Longtemps indompté, `le petit verdot` finit l'assemblage, en lui apportant `cette touche d'épice nécessaire`.」** |
| **引用（公式が掲げるもの）** | ✅ **「`Le grand vin est une œuvre d'art évolutive, jamais définitivement fixée, un peu comme les mobiles de Calder.`」— `Émile Peynaud — Le vin et les jours`**（公式が `/chateau-palmer` に掲げている） |

⚠️ 🔴 **公式サイトに点数・受賞・格付比較の掲載は一切無い。**
⚠️ **公式は「スーパーセカンド」「1 級に匹敵」に相当する表現を一度も使っていない。** → §Staff Notes ⚠️ ①

### ✅ ヴィンテージ評（OBP 5 本について。公式 Fiche Millésime の冒頭要約より）

| VT | ✅ 公式の一文 |
|---|---|
| 🔴 **2017**「Sous l'influence du fleuve」 | **「Terroir en vue. Après un départ optimal de la végétation, `des gels tardifs jettent le doute`. `Le fleuve fait heureusement rempart`. Suivent d'excellentes conditions climatiques. Au chai, la typicité de chaque parcelle nous guide. `Les vins en ressortent précis, fidèles à eux-mêmes.`」**<br>**「Le millésime 2017 est `précis, sans excès`. `Les tanins caressants et la profondeur aromatique` laissent présager `une belle longévité`.」** |
| 🔴 **2014**「Le vin du bicentenaire」 | **「`Et si la biodynamie nous rapprochait de notre terroir ?` Deux-cents ans après l'acquisition du domaine par le Major Général Charles Palmer, le millésime 2014 répond simplement à cette question : `son énergie intègre magnifiquement l'élevage et libère fruit et minéralité.`」**<br>**「2014 est un millésime `énergique et soyeux`, fort de sa vigueur aromatique, avec ses belles notes de `fruits noirs, d'épices, de poivre et de bois noble`. `Le grain est fin, caressant.` Le vin, `plus soyeux que velouté`, d'une belle harmonie.」** |
| 🔴 **2013**「L'art de l'assemblage」 | **「Jamais nos vignerons n'avaient connu hiver aussi humide. S'ensuivent des vendanges tardives, menées à la hâte, et `la crainte de tanins rustiques`. Un travail de vinification attentionné évite cet écueil. Au final, `seul un tiers de la récolte est retenu dans l'assemblage final`…」**<br>**「Un grand vin est affaire d'équilibre. Château Palmer 2013 nous le rappelle en jouant subtilement sur `un style atypique`.」** |
| 🔴 **2012**「Un équilibre entre ciel et soleil」 | **「Trois temps : pluies de printemps, soleil d'été et humidité de rentrée. Deux caractères : d'un côté, `des merlots exubérants` ; de l'autre, `des cabernets sauvignons aussi droits que précis`. `Deux millésimes en un` : un mariage heureux pour des vins tout en harmonie.」**<br>**「Ce mariage atypique met harmonieusement en avant `l'onctuosité, la délicatesse et la subtilité` des vins de Château Palmer.」** |
| 🔴 **1996**「Une touche de modernité」 | **「Des cabernets sauvignons `droits et puissants` associés à des merlots `plus charmeurs` ont produit un Château Palmer `qui dénote dans le contexte des grands vins médocains de ce millésime : tout aussi profond mais bien plus accessible`. `Encore de bien belles années en perspective.`」**<br>**「`Sauvignons et francs` signent ainsi un vin `particulièrement dense, aux arômes épicés et complexes, aux tanins délicats`. Un millésime `d'un grand raffinement`.」** |

---

## Important Cuvées

### ✅ 公式の現行レンジ（`/gamme` の `Les Vins` ナビ）

🔴 **公式の「les vins」ナビが並べるのは 3 項目だけである —— `Château Palmer` / `Alter Ego` / `Livre de cave`。**
🔴 **`Livre de cave` はワインではなくヴィンテージ・アーカイブのページである。すなわち公式が「商品」として提示するワインは 2 本しかない。**

| # | 公式のワイン名 | AOC | 公式の位置づけ | OBP |
|---|---|---|---|---|
| 1 | 🔴 **`Château Palmer`** | 🏛 **AOC Margaux** | ✅ **`le grand vin`** | 🔴 **OBP 5 行すべての最有力対応** |
| 2 | 🔴 **`Alter Ego`** | 🏛 **AOC Margaux**（🏛 Demeter 登録が `Vin rouge Margaux "Alter Ego"` と明記） | 🔴 ✅ **`L'autre grand vin de Château Palmer` / `THE OTHER WINE OF CHÂTEAU PALMER` / `cet « autre vin »`。1998 年ミレジムから** | — |

### 🔴 公式サイトが商品として並べないが、公式／登録に実在する 2 本

#### 🔴 ③ `Historical XIXth Century Wine`（公式記事 `/article/quelques-gouttes-du-rhone`、2022-05）

✅ **「Voilà un vin qui porte bien son nom troublant : `« Historical XIXth Century Wine »`.
`Aucune trace de Palmer, de son château, ni même d'une appellation sur l'étiquette bleu nuit` de ce vin rare qui emballe les amateurs.」**

| 項目 | ✅ 公式の記述 |
|---|---|
| 🔴 **由来** | **「Au XIXe siècle, les négociants bordelais `tonifiaient certains clairets en ajoutant à l'assemblage un peu de vin de L'Hermitage` … Certains grands crus de Bordeaux furent eux aussi `« hermitagés »` au fil du siècle.」**<br>**「Invité en `2005` par un collectionneur californien, Thomas Duroux est … bouleversé par la dégustation d'un `Château Palmer 1869` dans lequel il croit déceler une subtilité d'un autre temps. `La bouteille est-elle hermitagée ? À défaut de certitude`, l'expérience lui inspire une idée」** |
| 🔴 **構成** | 🔴 **「Chaque hiver, la direction … sillonne … `les côtes du Rhône septentrionales` pour débusquer `les 10% de syrah` qui se marieront avec `le merlot et le cabernet sauvignon du domaine`」** |
| 🔴 **調達** | **「Thomas Duroux et Sabrina Pernet partent déguster les syrahs les plus intenses … et rapportent de leur pérégrination `deux ou trois barriques` dont `l'origine est soigneusement gardée secrète depuis le début de l'aventure`」** |
| 🔴 **年表** | 🔴 **「`Expérimenté sur des lots de 2004`, Historical XIXth Century Wine `s'étoffe en 2006` puis `éblouit en 2010`. Et `s'installe depuis comme une signature de la maison`」** |
| 🔴 **数量** | 🔴 **「Avec son volume confidentiel – `autour des cinq mille bouteilles annuelles` –, il s'agit d'une `cuvée de collection`」** |
| 🔴 **アペラシオン** | 🔴 **「L'incarnation d'un vin rare qui `brave les appellations et s'affranchit des normes`」**<br>🔴 ⚠️ **公式は `Vin de France` という語を一度も使っていない。書いているのは「ラベルにアペラシオンの記載が無い」ということだけである。** |
| 🏛 **法令側の裏づけ** | 🔴 🏛 **CDC V 章の Margaux 主要品種にシラーは無い。したがってシラーを含むワインは AOC Margaux を名乗れない。**<br>⚠️ **「では何を名乗っているのか」は、公式にも Demeter の登録にも書かれていない。** → Open Questions 1 |
| **Duroux の言葉** | ✅ **「`C'est une création collective, la libre interprétation d'une tradition oubliée qui pique notre imagination et nous invite à l'audace.`」** |

#### 🔴 ④ 白 —— 🏛 **`Vin blanc Vin de France "Blanc de Palmer"`**

| 出典 | 記述 |
|---|---|
| 🔴 🏛 **Demeter France 加盟者ページ** | 🔴 **`Vin blanc Vin de France "Blanc de Palmer" 2020 - 2021`／`Vin blanc Vin de France "Blanc de Palmer" 2022 - 2023`／`Vin blanc 2024 - 2025`** |
| 🔴 ⚠️ **公式サイト** | 🔴 **白ワインについて一語も無い。`vin blanc` / `blanc de palmer` / `sauvignon` / `muscadelle` の検索結果は FR 67 ページで 0 件。** |
| 🔴 ✅ **ただし白品種の存在は公式が書いている** | 🔴 **îlot `Le Cassena` について「L'ensemble `le plus varié` du domaine, puisqu'il compte, `en plus des rouges, quatre cépages de blanc`」** |
| 🏛 **法令** | 🔴 **AOC Margaux は「réservée aux vins tranquilles rouges」。したがって白は定義上 AOC Margaux ではありえない。** |
| ⚠️ **第三者主張（不使用）** | ⚠️ **検索では idealwine / Vivino / CellarTracker / Wine-Searcher / Falstaff 等が `Vin Blanc de Palmer`（Demeter 登録の綴り `Blanc de Palmer` とは異なる）を `Vin de France` として扱っている。**⚠️ **本ドシエはこれらを事実として採用していない。名称の綴りの差は実ラベルでしか決着しない。** → Open Questions 2 |

🔴 **canonical はこの白の存在を一切持っていない（`palmer-1855` の `obp_note` のラインナップに白が無い）。**

---

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本。全て `unresolved`**）

🔍 **5 行はいずれも `source_section = "FRANCE | RED > BORDEAUX"`、`source_producer_raw = "Palmer"`、`source_wine_raw = "Margaux"`。**
🔍 **`_parts` は 5 行とも `label: null` / `appellation: "margaux"` / `appellation_display: "Margaux"` / `printed_rest: "Margaux"` / `varietal: null` / `rank: null`。**
🔍 **`_collision_risk: "LOW"`。**

| # | OBP 印字 | VT | 価格 | intake | 🔴 **実際に何のワインか（公式による判定）** |
|---|---|---|---|---|---|
| 1 | **`Palmer` / `Margaux`** | **2017** | **$1,280** | 🔴 **`unresolved`**（`producer_state: exact` / `cuvee_state: exact` / `vintage_state: unresolved` / `confidence: 0.0`） | 🔴 ✅ **`Château Palmer 2017`（grand vin、AOC Margaux）。公式 Fiche Millésime 2017 が実在。**<br>🔴 **`Merlot 54% / Cabernet sauvignon 42% / Petit verdot 4%`／収穫 `Du 13 septembre au 5 octobre 2017`** |
| 2 | **`Palmer` / `Margaux`** | **2014** | **$1,280** | 🔴 **`unresolved`**（同上） | 🔴 ✅ **`Château Palmer 2014`。公式 Fiche Millésime 2014 が実在。**<br>🔴 **`Merlot 45% / Cabernet sauvignon 49% / Petit verdot 6%`／収穫 `Du 22 septembre au 14 octobre 2014`／公式副題 `Le vin du bicentenaire`** |
| 3 | **`Palmer` / `Margaux`** | **2013** | **$960** | 🔴 **`unresolved`**（同上） | 🔴 ✅ **`Château Palmer 2013`。公式 Fiche Millésime 2013 が実在。**<br>🔴 **`Merlot 49% / Cabernet sauvignon 51%`（`Petit verdot` の行が無い）／収穫 `Du 27 septembre au 11 octobre 2013`／`seul un tiers de la récolte est retenu`** |
| 4 | **`Palmer` / `Margaux`** | **2012** | **$1,400** | 🔴 **`unresolved`**（同上） | 🔴 ✅ **`Château Palmer 2012`。公式 Fiche Millésime 2012 が実在。**<br>🔴 **`Merlot 48% / Cabernet sauvignon 46% / Petit verdot 6%`／収穫 `Du 27 septembre au 15 octobre 2012`** |
| 5 | **`Palmer` / `Margaux`** | **1996** | **$2,080** | 🔴 **`unresolved`**（同上） | 🔴 ✅ **`Château Palmer 1996`。公式 Fiche Millésime 1996 が実在。**<br>🔴 **`Merlot 40% / Cabernet sauvignon 55% / Cabernet franc 4% / Petit verdot 1%`（**4 品種**）／収穫 `Du 23 septembre au 8 octobre 1996`**<br>🔴 **このフィッシュには `ALTER EGO` のブロックが無い（＝Alter Ego は 1998 年から、と整合）** |

#### 🔴 「bare `Margaux` が何を指すか」—— **本件では確定できる**

| 問い | 実測による答え |
|---|---|
| 🔴 **grand vin か、`Alter Ego` か、白か** | 🔴 ✅ **`Château Palmer`（grand vin）である。理由は 3 つ。**<br>🔴 **① セクションが `RED > BORDEAUX` で、白は排除される。**<br>🔴 **② 印字が `Palmer / Margaux` であり、`Alter Ego` は印字されていない。公式は `Alter Ego` を必ず `Alter Ego` と表記し、`Palmer` 単独では呼ばない（`/gamme` のナビ・ラベル・Demeter 登録の 3 系統で一致）。**<br>🔴 **③ 価格。$960–$2,080 という帯は、同一メニューの他の行と比べて grand vin の水準にある。**<br>⚠️ **ただし ③ は状況証拠である。決着は実ラベルでつく。** → Open Questions 9 |
| 🔴 **`Margaux` は誰の語か** | 🔴 🏛 **AOC 名である。**🏛 **CDC XII 章はラベルに `Vin de Bordeaux - Médoc` / `Grand Vin de Bordeaux - Médoc` を併記してよいと定めるが、それは AOC 名より小さい文字でなければならない。**<br>🔴 **すなわちラベル上、`MARGAUX` は最も大きく刷られる語の 1 つである。メニューがこれを「ワイン名」の列に拾うのは、Bordeaux では構造的に起こる。** |
| 🔴 **メニューが defective か** | 🔴 ⚠️ **断定しない。**<br>🔴 **メニューは `Palmer` + `Margaux` + 年号を印字しており、これは実在するボトルを一意に指し得る情報量を持っている。**<br>🔴 **一方 canonical は、この生産者について**ヴィンテージ行を 1 つも持っていない**。**<br>🔴 **したがって `unresolved` の原因は、メニュー側ではなく canonical 側にある。**<br>⚠️ **Batch 10・11 の教訓どおり両方向の可能性を残すが、本件は canonical 側が原因である証拠のほうが強い。** |
| 🔴 **1996 の特殊性** | 🔴 **公式フィッシュが `Cabernet franc 4%` を明記する。**<br>🔴 **公式の現在の記述「`trois piliers`（cabernet sauvignon / merlot / petit verdot）」は現在の話であって、1996 のボトルには当たらない。**<br>🔴 **1996 について「カベルネ・ソーヴィニヨンとメルロと少量のプティ・ヴェルドです」と言うと、事実に反する。** → §Staff Notes ⚠️ ⑤ |

---

## Staff Notes

### 🔴 芯 3 点（**これだけ言えれば卓上で嘘をつかない**）

🔴 **①「マルゴーの 3 級、シャトー・パルメです。コミューンは現在マルゴー＝カントナックで、蔵はイサンという地区にあります。
畑はカベルネ・ソーヴィニヨンとメルロが同率で、そこにプティ・ヴェルドが少し。造り手自身が『この地方では独特の植栽』と言っています。」**
**—— ✅ 公式 `/domaine` の `trois piliers` / `à part égale` / `un encépagement singulier pour la région` の直訳。**
🔴 **🏛 コミューンは `geo.api.gouv.fr` で `Margaux-Cantenac`（INSEE 33268、旧 Cantenac は 33091）と確認済み。**
🔴 **🏛 AOC Margaux が赤専用であることは INAO の CDC（2023-03-31 homologué）で確認済み。**

🔴 **②「熟成は二段階です。まず 225 リットルの樽で、新樽は半分未満。そのあと 30 ヘクトリットルのフードルに移して、
合わせて 20〜22 か月です。」**
**—— ✅ 公式 `/domaine` と `/chateau-palmer` の 2 か所が独立に `vingt à vingt-deux mois` / `20 à 22 mois` と書く。**
🔴 **`18〜21 か月`（canonical の値）と言ってはならない。**
🔴 **`barriques de 225 litres`（小樽）と `foudres de 30 hectolitres`（大樽）は別の道具で、順番がある。**

🔴 **③「造り手は 2009 年に 1 ヘクタールでビオディナミを試し、2014 年ミレジムで畑の全面転換を完了したと公表しています。」**
**—— ✅ 公式 `/article/la-terre-nourriciere`（`un premier essai sur une parcelle témoin d'un hectare` en 2009 → `intégralement converti à la biodynamie à partir du millésime 2014`）。**
🔴 **これは「認証の話」ではなく「造り手の公表した年表」である。この区別を崩すと即座に嘘になる。**
🔴 **リストにある 1996 / 2012 / 2013 は、いずれもこの完了年より前のボトルである。**

### ⚠️ 言ってはいけないこと（**must-not-say**）

⚠️ **①「スーパーセカンドです」／「3 級ですが 1 級並みです」／「1 級に匹敵する深みに昇華します」。**
🔴 **公式サイトのどこにもそのような主張は無い。公式が 1855 について書く唯一の文はこうである ——
「`le rang de troisième cru, attribué depuis longtemps à Palmer par les négociants et les grands prescripteurs, est consacré par le Classement impérial`」。**
🔴 **canonical の `description` / `description_en` / `tasting` / `tasting_en` / `tags` の 5 か所にこの主張が入っている。canonical をそのまま読み上げてはならない。**

⚠️ **②「Alter Ego はセカンドワインです」。**
🔴 **公式は `L'autre grand vin de Château Palmer`（FR）/ `THE OTHER WINE OF CHÂTEAU PALMER`（EN）/ `cet « autre vin »` と書く。**
🔴 **取得した公式 FR 67 ページ＋EN 2 ページを全文検索して `second vin` / `second wine` / `deuxième vin` は 0 件。**
🔴 **正しい言い方 ——「もう 1 本のワインです。造り手は『もう一人の自分』と呼んでいて、収穫の時点でどちらに行くか決まります。」**
🔴 **canonical の `obp_note` / `obp_note_en` は「セカンド」「second wine」と書いている。**

⚠️ **③「オーガニックです」／「ビオディナミのワインです」／「Demeter です」／「Biodyvin です」（1996 / 2012 / 2013 / 2014 / 2017 のボトルについて）。**
🔴 **🏛 Agence Bio の `datePremierEngagement` は `2011-09-08`。1996 はその 15 年前である。**
🔴 **🏛 Demeter France の登録製品リストは `2019-2020` / `2021-2022` / `2024-2025` しか覆っていない。**
🔴 **🏛 Biodyvin の会員リストは `224 adhérents en 2025` という現在のスナップショットで、加入年が無い。**
🔴 **🏛 `Raisin de cuve` の `etatProduction` は 2026 年参照で `C1` と `AB` の両方が立っている。**
⚠️ **同時に「オーガニックではありません」も言ってはならない。造り手は 2014 年に 100% 転換を完了したと公表している。**
🔴 **言えるのは②の芯 3 点③だけである。「認証」という語をボトルに結びつけない。**

⚠️ **④「シラーを 15% 入れた特別なキュヴェがあります」／「Vin de France と表記されています」。**
🔴 **✅ 公式は `10% de syrah` と書く。名称は `Historical XIXth Century Wine`（`Blend` ではない）。**
🔴 **✅ 公式が書くのは「`Aucune trace de Palmer, de son château, ni même d'une appellation` sur l'étiquette bleu nuit」であって、`Vin de France` ではない。**
🔴 **canonical の `obp_note` は「Historical XIXth Century Blend」「シラー 15%」「Vin de France 表記」の 3 点すべてを書いている。3 点とも公式と一致しない。**
🔴 **なお「Palmer は 100% ボルドー品種ですか」と訊かれたら —— ✅ 公式の言葉で「北ローヌのシラーを 10% 入れた別のワインを毎年 5000 本ほど造っています。ラベルにはパルメの名前もアペラシオンも入っていません」と答えるのが正確である。**

⚠️ **⑤「1996 はカベルネ・ソーヴィニヨンとメルロとプティ・ヴェルドです」。**
🔴 **✅ 公式 Fiche Millésime 1996 は `Merlot 40% / Cabernet sauvignon 55% / Cabernet franc 4% / Petit verdot 1%` の 4 品種を明記する。**
🔴 **カベルネ・フランが入っている。「3 品種」は現在の話であって 1996 には当たらない。**
🔴 **フィッシュ本文も「`Sauvignons et francs` signent ainsi un vin particulièrement dense」と、フランを名指ししている。**

⚠️ **⑥「カベルネ 47%、メルロ 47%、プティ・ヴェルド 6% です」。**
🔴 **✅ 公式は畑の植栽比率にパーセンテージを一切与えていない（`à part égale` としか書かない）。**
🔴 **そして `47/47/6` は公式 Livre de cave の `2016` ヴィンテージのアッサンブラージュそのものである。**
🔴 **リストの 5 本の実際の比率は、2017=`54/42/4`、2014=`45/49/6`、2013=`49/51/0`、2012=`48/46/6`、1996=`40/55/4(CF)/1` と大きく振れる。**
🔴 **数字を言うなら「そのヴィンテージの数字」を言う。畑の比率として言ってはならない。**

⚠️ **⑦「66 ヘクタールです」。**
🔴 **✅ 公式サイトに現在の栽培面積の記載が無い（67 ページ全文検索）。出てくる ha はすべて歴史上の数値か別用途である。**
🔴 **`163 ha` は 19 世紀の Charles Palmer 時代、`83 ha` は 1853 年に Pereire 兄弟が取得した面積、`13 ha` は îlot Domec、`28 ha` は家畜の面積。**
🔴 **canonical の `66ha` は出典が確認できない。数字を言わないのが正解。**

⚠️ **⑧「カントナック村にあります」。**
🔴 **🏛 現在そのコミューンは存在しない。`Margaux-Cantenac`（INSEE 33268）に統合済みで、旧 Cantenac のコード 33091 は `anciensCodes` にある。**
🔴 **🏛 2023 年 homologué の CDC のコミューン列挙も `Arsac, Labarde, Margaux-Cantenac et Soussans` の 4 つである。**
🔴 **正しい言い方 ——「マルゴー＝カントナックというコミューンの、イサンという地区です。歴史的にはカントナック村と呼ばれていた場所です。」**

⚠️ **⑨「シシェル家とマレール・ベス家の 2 家族が所有しています」。**
🔴 **🏛 企業登録の `dirigeants` は 152 件（自然人 148 / 法人 4）。うち 146 名が `Associé indéfiniment responsable` である。**
🔴 **法人の gérant は `SOCIETE SICHEL`（SIREN 456204445）と `FRITZ`（SIREN 518992706）の 2 社、加えて `SASU THDUROUX`（891533663）。**
🔴 **姓の分布は `BOUTEILLER`(22) / `LODEIZEN`(12) / `BAZIL`(9) / `LACOSTE`(9) / `MAURIAC`(7) / `MÄHLER` 系(9) と広い。**
⚠️ **✅ 公式が書くのは「`quatre dynasties d'abord, puis deux d'entre elles`」であって「2 家族が所有」ではない。**
✅ **安全な言い方 ——「1938 年以降、複数の一族が支えてきた家族経営で、いまはオランダ出身の Mähler-Besse 家と、英仏独でグラン・クリュの流通を担ってきた Sichel 家が中心です。」**

⚠️ **⑩「シャンパーニュのパルメと同じ造り手です」。**
🔴 **🏛 別法人。`Société Civile du Château Palmer` は SIREN `781863428`、Gironde（33）。Champagne Palmer & Co は Marne（51）の Reims。**
🔴 **canonical にシャンパーニュ側のレコードは存在せず、混同も起きていない（928 件走査済み）。卓上でだけ気をつければよい。**

⚠️ **⑪「亜硫酸無添加のワインです」（2014 以降について）。**
🔴 **✅ 公式が書くのは「`ne plus sulfiter la vendange`（収穫物に亜硫酸を添加しない）」と「`Retarder les apports de soufre`（亜硫酸の投入を遅らせる）」である。**
🔴 **「無添加」ではない。工程の一段階の話である。**

⚠️ **⑫「発酵タンクは 54 基の木製です」。**
✅ **公式は `cuves tronconiques d'une contenance de 89 à 195 hectolitres` / `54 cuves thermorégulées` と書くだけで、材質を書いていない。**
✅ **`imposante charpente de bois` は cuvier の建物の梁の話である。**

⚠️ **⑬「ジロンド河を見下ろす丘です」。**
✅ **公式は `Plateau des Brauzes`、`première terrasse de graves charriés par la Garonne`、`mosaïque de sols regardant l'estuaire de la Gironde` と書く。**
⚠️ **「テラス（段丘）」であって「丘陵」とは書いていない。また河は `l'estuaire de la Gironde` と `la Garonne` が使い分けられている。**

### 🔴 追加の一手（**客に訊かれたら強い。すべて公式の言葉**）

🔴 ✅ **「発酵槽は 54 基で、89 から 195 ヘクトリットルまで大きさが違います。区画ごと、時には区画の中まで分けて仕込みます。」**
**—— `cuves tronconiques d'une contenance de 89 à 195 hectolitres` / `un travail parcellaire, voire même intra-parcellaire`。**

🔴 ✅ **「実験用の醸造所が別にあって、研究室と 9 基のマイクロ・キュヴが常時動いています。自前の pied de cuve を造ることで、硫黄の使用量を半分に減らせたそうです。」**
**—— `un laboratoire et neuf micro-cuves` / `réduire l'utilisation du soufre de moitié … par l'élaboration de pieds de cuve en propre`。**

🔴 ✅ **「畑の中心は 1930 年代に植えたメルロの古木です。しかもそれが、本来カベルネ向きのテロワールに植わっている。」**
**—— `vieux merlots plantés dans les années 1930 sur de grands terroirs à cabernet`。**

🔴 ✅ **「2018 年から畑を 5 つの島に分けていて、それぞれ担当チームが固定されています。名前は Boston-Boulibranne、40s-50s、Le Cassena、Le Plateau、Domec。」**
**—— `/article/les-cinq-iles-de-palmer`。**

✅ **「牛と羊と山羊と豚と家禽を飼っていて、その堆肥にブドウの剪定枝と果梗を混ぜて肥料にしています。牛はボルドレーズという地元の在来種です。」**
**—— `fumier` + `sarments de vignes broyés` + `rafles de vendanges` / `La Bordelaise` / `Conservatoire des Races d'Aquitaine`。**

✅ **「畑の中に 1000 本以上の果樹を植えました。ナポレオン・チェリー、ウィリアムズ梨、ベルジュロン杏です。」**
**—— `Cerisiers Napoléon, poiriers Williams, abricotiers Bergeron` / `une quinzaine de plants par hectare`。**

✅ **「1 ヘクタールに 1 万本。1 本のブドウが 1 平方メートルを使う計算です、と技術責任者が言っています。」**
**—— Sabrina Pernet、`10 000 pieds par hectare` / `un mètre carré pour s'exprimer`。**

🔴 ✅ **「2013 は難しい年で、最終的に収穫の 3 分の 1 しかグラン・ヴァンに入れていません。」**
**—— 公式 Fiche Millésime 2013、`seul un tiers de la récolte est retenu dans l'assemblage final`。**

🔴 ✅ **「2017 は霜の年でしたが、河が防波堤になったと造り手は書いています。」**
**—— `Le fleuve, véritable protecteur thermique, préserve l'essentiel du vignoble`。**

🔴 ✅ **「2014 は創立 200 周年の年で、造り手はこれを『Le vin du bicentenaire（200 周年のワイン）』と呼んでいます。」**
**—— 公式 Fiche Millésime 2014 の副題。**

✅ **「2009 年以降のボトルには QR コードが入っていて、公式サイトで真贋を確認できます。蔵で詰め直したボトルには黒い封蝋があります。」**
**—— `Seuls les millésimes à partir de 2009 en sont équipés, ainsi que les millésimes reconditionnés à la propriété, disposant d'un scellé noir`。**
🔴 **リストの `2012` / `2013` / `2014` / `2017` はこの範囲に入る。`1996` は入らない。**

---

## Akio's Insight

🖋 （Akio 記入欄。未記入）

---

## Canonical Conflict

🔒 **本節は escalation のみ。`REGISTER.md` は書き換えていない。番号の採否は CTO の判断である。**

### 🔍 canonical の実測（`migration/out/export/db_wine_canonical.json`、928 要素）

| 走査 | 結果 |
|---|---|
| **`palmer` を含むレコード（全文字列）** | 🔍 **12 件** |
| 🔴 **`producer` フィールドが `Château Palmer` のレコード** | 🔴 **1 件（`palmer-1855`）** |
| 🔍 **prose のみで `palmer` に当たるレコード** | 🔍 **11 件** — `bordeaux-vintage-{1966,1967,1970,1971,1978,1979,1983,1992}-guide`（8 件）＋ `rauzan-gassies-1855` / `durfort-vivens-1855` / `desmirail-1855` |
| 🔴 **Champagne Palmer & Co との混同** | 🔴 **0 件。11 件すべて Bordeaux 文脈の Château Palmer への言及。**`D-2026-08-05-08` の懸念は本件では実現していない |
| 🔴 **`vintage: "—"`（U+2014）のレコード総数** | 🔴 **328 件**（Batch 11 の実測値と一致。再現した） |
| 🔴 **`subregion: "Margaux"` のレコード** | 🔴 **21 件**（1er 1・2ème 5・3ème 10・4ème 3・5ème 2） |

### 🔴 ① 構造の観察 —— **`palmer-1855` は「ボトル」ではなく「1855 格付名簿の 1 行」である**

🔴 **`subregion: Margaux` の 21 件は、すべて `<slug>-1855` という id を持ち、すべて `vintage: "—"` で、
すべて `classification: "1855 Médoc Classification · Nème Grand Cru Classé"` の形をしている。**

🔴 🏛 **そして INAO の CDC（consolidated、2023）自身がこう書く ——
「Le célèbre classement de 1855 … `consacre la future appellation « Margaux » en la dotant d'un éventail unique de 21 grands crus classés`」。**

🔴 **21 という数が一致する。すなわち canonical のこの一群は、偶然できた重複ではなく、
1855 格付の Margaux 名簿を意図的に encode したものと読むのが自然である。**

⚠️ **これは Batch 12 のブリーフが指摘した `cos-destournel-parker-profile`（第三者評論家のシャトー・プロファイルがワイン・レコードとして格納されている）とは別の形である。**
⚠️ **こちらは「第三者の記事」ではなく「法的格付の名簿」であり、出典の性格が違う。**
🔴 **本ドシエは番号を開かない。形として記述するにとどめる。**

### 🔴 ② OBP 5 行はすべて `vintage gap`（**conflict ではない**）

🔴 **`D-2026-08-05-14`（Abreu 先例）の方針どおり、`不在` は conflict ではなく gap として記録する。**

| OBP 行 | 状態 | 判定 |
|---|---|---|
| **`Palmer / Margaux / 2017`** | 🔴 **canonical にヴィンテージ行が無い** | 🔴 **vintage gap。公式 Fiche Millésime 2017 で実在を確認済み** |
| **`… / 2014`** | 🔴 **同上** | 🔴 **vintage gap。公式 Fiche Millésime 2014 で確認済み** |
| **`… / 2013`** | 🔴 **同上** | 🔴 **vintage gap。公式 Fiche Millésime 2013 で確認済み** |
| **`… / 2012`** | 🔴 **同上** | 🔴 **vintage gap。公式 Fiche Millésime 2012 で確認済み** |
| **`… / 1996`** | 🔴 **同上** | 🔴 **vintage gap。公式 Fiche Millésime 1996 で確認済み** |

🔴 **`unreachable`（別綴りで存在する）の可能性は潰した。**
928 件を `palmer` で全文走査した結果が 12 件であり、`producer` 一致は 1 件のみ。
`Chateau Palmer` / `Ch. Palmer` / `Palmer` 単独などの別綴りで潜んでいるレコードは存在しない。

🔴 **加えて、canonical はこの生産者について次の 4 つを持っていない ——**
🔴 **① ヴィンテージ行（0 件）／② `Alter Ego` の行／③ 白（`Blanc de Palmer`）の行／④ `Historical XIXth Century Wine` の行。**
🔴 **①〜④ はいずれも `gap` であり `conflict` ではない。**

### 🔴 ③ 格納値の実測 —— **検証可能な 27 主張のうち 15 が失敗**

🔴 **`palmer-1855` の全 23 フィールドを走査し、公式・法令と突き合わせ可能な主張 27 件に分解して 1 件ずつ検証した。**

| # | canonical の主張 | ✅/🏛 の値 | 判定 |
|---|---|---|---|
| 1 | `producer: "Château Palmer"` | ✅ **公式表記と一致** | ✅ **PASS** |
| 2 | `name: "Château Palmer"` | ✅ **一致** | ✅ **PASS** |
| 3 | `country: "France"` / `region: "Bordeaux"` | 🏛 **一致** | ✅ **PASS** |
| 4 | `subregion: "Margaux"` | 🏛 **AOC 名としては正しい。**⚠️ **コミューンは `Margaux-Cantenac`** | ⚠️ **PASS（ただし「地区」ではなく「アペラシオン」を格納している）** |
| 5 | `color: "Rouge"` | 🏛 **CDC「réservée aux vins tranquilles rouges」** | ✅ **PASS** |
| 6 | `classification: "1855 Médoc Classification · 3ème Grand Cru Classé"` | ✅ **公式は `le rang de troisième cru`。**🏛 **`gcc-1855.fr` は `Troisième Cru / Margaux`** | ⚠️ **PASS（実質一致）。**⚠️ **ただし公式・GCC の表記は `Troisième Cru` であり、`3ème Grand Cru Classé` は語の合成である** |
| 7 | **「スーパーセカンドの象徴」「1 級に迫る品質・評価・価格」** | 🔴 **公式にこの主張は無い。1855 について公式が書く唯一の文は「以前から与えられていた 3 級が Classement impérial に追認された」** | 🔴 **FAIL（出典なき最上級）** |
| 8 | **「1814年にイギリスの`将軍`チャールズ・パルメ氏が…購入」** | ✅ **公式は `Lieutenant-Colonel Charles Palmer` / `ce futur Major Général`** | 🔴 **FAIL（購入時の階級が違う）** |
| 9 | **「恋に落ちた未亡人から購入」「当時の名は『ドメーヌ・ド・ガスク』」** | ✅ **`Madame Marie Brunet de Ferrière, veuve de Gascq` / `le domaine de Gascq`** | ✅ **PASS** |
| 10 | **「将軍は30年かけて畑を拡大し設備を整え」** | ✅ **`En près de 30 ans, le gentleman s'emploie à l'agrandir, à le moderniser`** | ✅ **PASS** |
| 11 | **「1853年にペレール兄弟（エミールとイザック）が購入」** | ✅ **`En 1853, ils font l'acquisition du domaine` / `Émile et Isaac Pereire`** | ✅ **PASS** |
| 12 | **「1年足らずで大改革を断行したが、1855年の格付けでは`3級に留まった`」** | 🔴 **公式は逆の枠組みで書く（`consacré par le Classement impérial`）。「1 年足らずの大改革」も公式に無い** | 🔴 **FAIL（出典なき評価的枠組み）** |
| 13 | **「その後`4回のオーナー交代`を経て」** | ✅ **公式は「`Depuis 1938` … `quatre dynasties d'abord, puis deux d'entre elles`」** | 🔴 **FAIL（「4 家族」を「4 回の交代」に読み替えている）** |
| 14 | **「シシェル家（英、ワイン商）＋マレール・ベス家（蘭、織物・ワイン）が`共同で経営`」** | ✅ **家系と出自の記述は公式と一致。**🔴 **🏛 ただし登録上の実体は 148 名の無限責任社員＋法人 gérant 3 社** | ⚠️ **PARTIAL FAIL（家系は正しいが、所有構造の記述としては不正確）** |
| 15 | **「2004年よりトーマス・デュロー氏が経営を担い」** | ✅ **`en 2004 … la direction de Château Palmer`** | ✅ **PASS** |
| 16 | **「ビオディナミを推進」** | ✅ **公式の記述と整合** | ✅ **PASS（ただし §Farming の時間軸の但し書きが要る）** |
| 17 | **「マルゴー`北寄り`に位置する」** | 🔴 **公式は方位を一切書かない** | 🔴 **FAIL（出典なし）** |
| 18 | **「`66ha`」** | 🔴 **公式サイト 67 ページに現在の面積の記載が無い** | 🔴 **FAIL（出典なし）** |
| 19 | **「CS約`47%` / Merlot約`47%` / PV約`6%`」（＝畑の植栽比率として提示）** | 🔴 **公式は植栽比率に数字を与えない（`à part égale` のみ）。**🔴 **`47/47/6` は公式 Livre de cave の`2016 ヴィンテージのアッサンブラージュ`と完全一致** | 🔴🔴 **FAIL（別レイヤーの値の混入）** |
| 20 | **「マルゴー格付シャトー`屈指の高Merlot比率`」** | ⚠️ **公式は `un encépagement singulier pour la région` としか書かない。他シャトーとの比較は書かない** | ⚠️ **FAIL（出典なき比較）** |
| 21 | **「`54基`の円錐型発酵タンクで区画別テロワール管理」** | ✅ **`54 cuves thermorégulées` / `cuves tronconiques` / `un travail parcellaire, voire même intra-parcellaire`** | ✅ **PASS** |
| 22 | **「`18〜21ヶ月`樽熟成」** | 🔴 **公式は 2 か所で `vingt à vingt-deux mois` / `20 à 22 mois`** | 🔴 **FAIL（矛盾）** |
| 23 | **「新樽`50%未満`」** | ✅ **`du bois neuf pour moins de la moitié d'entre elles`** | ✅ **PASS** |
| 24 | **「Alter Ego de Palmer（`セカンド`、`1998年〜`）」** | 🔴 **`1998` は PASS。**🔴 **`セカンド` / `second wine` は公式に 0 件、公式は `l'autre grand vin` / `the other wine` / `cet « autre vin »`** | 🔴 **FAIL（造り手が明示的に拒否している枠組み）** |
| 25 | **「Historical XIXth Century `Blend`」** | 🔴 **公式の名称は `Historical XIXth Century Wine`** | 🔴 **FAIL（名称違い）** |
| 26 | **「`シラー15%`ブレンド」** | 🔴 **公式は `les 10% de syrah`** | 🔴 **FAIL（矛盾）** |
| 27 | **「→ `Vin de France`表記」** | 🔴 **公式は「ラベルに Palmer の名も château もアペラシオンも無い」としか書かない。`Vin de France` の語は公式に 0 件** | 🔴 **FAIL（出典なし。ただし白については Demeter 登録が `Vin de France` と書く ——**別のワインの designation と取り違えている可能性がある**）** |

🔴 **集計 —— 検証: 27 / PASS: 12 / FAIL: 15（矛盾 8・出典なし 7）。失敗率 55.6%。**
🔴 **さらに、公式が沈黙しているために検証不能だった項目が別に 5 件ある ——
`drinking_window`（12〜35 年以上）／`food_pairings` 5 件／`glassware`（Bordeaux）／`serving_temp`（17–19°C）／`tags` の `Super-Second`（＝主張 7 と同じ）。**

🔴 **Batch 8–11 の「canonical の格納値が造り手と矛盾する」という base rate は、15 軒目でも崩れなかった。**

### 🔴 ④ 未採番の下位形 —— **「1 ヴィンテージのアッサンブラージュが、生産者の恒久的な植栽比率として格納される」**

🔴 **canonical の `CS約47% / Merlot約47% / PV約6%` は、恒久的な事実（`品種・栽培` の見出しの下）として提示されている。**
🔴 **しかし公式 Livre de cave の実測値はこうである ——**

| VT | ✅ Château Palmer のアッサンブラージュ |
|---|---|
| **2024** | Merlot 41% / Cabernet sauvignon 59% |
| **2023** | Merlot 46% / CS 50% / PV 4% |
| **2022** | Merlot 45% / CS 51% / PV 4% |
| **2021** | Merlot 56% / CS 41% / PV 3% |
| **2020** | Merlot 48% / CS 48% / PV 4% |
| **2019** | Merlot 43% / CS 53% / PV 4% |
| **2018** | Merlot 40% / CS 53% / PV 7% |
| 🔴 **2016** | 🔴 **Merlot 47% / Cabernet sauvignon 47% / Petit verdot 6%** ← **canonical の値と完全一致** |
| 🔴 **2017**⭐OBP | 🔴 **Merlot 54% / CS 42% / PV 4%** |
| 🔴 **2014**⭐OBP | 🔴 **Merlot 45% / CS 49% / PV 6%** |
| 🔴 **2013**⭐OBP | 🔴 **Merlot 49% / CS 51%**（PV なし） |
| 🔴 **2012**⭐OBP | 🔴 **Merlot 48% / CS 46% / PV 6%** |
| 🔴 **1996**⭐OBP | 🔴 **Merlot 40% / CS 55% / Cabernet franc 4% / PV 1%** |

🔴 **すなわち canonical は、**2016 という 1 年のブレンド比率**を、**畑の植栽比率**として格納している。**
🔴 **そしてその値は、OBP に載っている 5 本のどれとも一致しない。**

⚠️ **これは Vilmart（Batch 11）で観測した「同一生産者内の別キュヴェからの値の取り違え」と同族だが、軸が違う。**
⚠️ **Vilmart は `キュヴェ間` の取り違え、本件は `ヴィンテージ ↔ 恒久属性` のレイヤー混同である。**
🔴 **本ドシエは番号を開かない。形として記述する: **「時間軸を持つ値が、時間軸を持たないフィールドに格納される」**。**
⚠️ **`V-1`（édition が層をまたぐ）に近いが、`V-1` は surrogate key の不在の問題であり、こちらは値の出所の問題である。CTO の判断。**

### 🔴 ⑤ intake の evidence 文字列が事実として偽である

🔍 **OBP 5 行の `evidence` は 5 行とも同型で、3 行目だけがヴィンテージによって変わる ——**

```
"正規化トークン集合一致: 'Palmer' ≡ 'Château Palmer'",
"名称トークン集合一致: 'margaux' ≡ 'Château Palmer'",
"canonical の 'Château Palmer' に vintage 2017 無し（保有: ゼロ件）"
```

🔴 **2 行目が偽である。`'margaux'` のトークン集合は `{margaux}`、`'Château Palmer'` は `{château, palmer}`。共通トークンは 0 個である。**
🔴 **にもかかわらず `cuvee_state: "exact"` が出力されている（`confidence` は 0.0）。**
🔴 **canonical にこの生産者のキュヴェ行が 1 件しかないため、**単一候補フォールバック**が発火し、
その結果を「トークン集合一致」という文言で報告していると読むのが最も整合的である。**

⚠️ **これは Batch 10 の `C-6`（matcher が節見出しを読んでいない／evidence が byte 同一）と隣接するが、同一ではない。**
⚠️ **`C-6` は「evidence が情報を持っていない」問題。本件は **「evidence が持っている情報が事実でない」** 問題である。**
🔴 **危険度が違う。byte 同一の evidence は「怪しい」と分かるが、具体的な照合根拠を名乗る偽の evidence は、レビュアーを誤誘導する。**
🔴 **本ドシエは番号を開かない。形として記述する: **「単一候補フォールバックが、実行していない照合を evidence として名乗る」**。CTO の判断。**

⚠️ **なお `match_state = exact` の危険についてのブリーフの警告は、本件では逆向きに現れている。**
⚠️ **5 行はいずれも `match_state: unresolved` かつ `confidence: 0.0` であり、**intake は正しく「解決していない」と言っている**。**
⚠️ **問題は上位フィールド（`cuvee_state: exact`）と evidence 文字列のほうにある。**

### ⚠️ ⑥ 公式資料の内部不一致（**canonical とは無関係。造り手側の問題**）

| 対象 | ✅ Fiche のヘッダ | ✅ Fiche の本文 |
|---|---|---|
| 🔴 **2017 の収穫日** | 🔴 **`Du 13 septembre au 5 octobre 2017`** | 🔴 **「Nous commençons les vendanges `le 20` avec de très beaux merlots」** |
| 🔴 **2012 の収穫日** | 🔴 **`Du 27 septembre au 15 octobre 2012`** | 🔴 **「Les vendanges se déroulent entredu `1er au 15 octobre`」**（原文に `entredu` という誤植あり） |

→ ⚠️ **どちらも同一の公式 PDF の中での食い違いである。両論を保存し、どちらかを選ばない。**
🔴 **収穫日を卓上で口にするなら「9 月下旬から 10 月上旬」とだけ言うのが安全である。** → Open Questions 10

⚠️ **もう 1 件 ——`Alter Ego` の見出しの FR / EN 差。**
🔴 **FR: `L'autre grand vin de château palmer` ／ EN: `THE OTHER WINE OF CHÂTEAU PALMER`。EN は `grand` を落としている。**
⚠️ **本ドシエは FR を原本として採用した。ただし「もう 1 本のグラン・ヴァン」と訳すか「もう 1 本のワイン」と訳すかは、造り手の中でも揺れている。**

---

## Sources

### 🔴 ✅ サイト真正性の事前チェック（`D-2026-08-05-09`）

| ドメイン | 判定 | 根拠 |
|---|---|---|
| ✅ **`www.chateau-palmer.com`** | ✅ **合格（3 条件すべて）** | ✅ **(a) `mentions légales` が `Dénomination sociale : Société Civile du Château Palmer` / `RCS BORDEAUX 781.863.428` / `Siret : 781 863 428 00012` / `TVA FR 25781863428` / `Directeur de la publication : Thomas Duroux` を明示。**<br>🏛 **企業登録の SIREN `781863428`・SIRET `78186342800012`・TVA `FR25781863428` と完全一致。**<br>🏛 **(b) 相互リンク成立 —— Demeter France の加盟者ページ `SC CHATEAU PALMER` が `http://www.chateau-palmer.com` を掲載。**<br>🏛 **(c) 住所一致 —— `Château Palmer, Lieu-dit Issan, 33460 Margaux-Cantenac` ⟷ 登録 `CHATEAU PALMER LD ISSAN 33460 MARGAUX-CANTENAC`。**<br>✅ **ホスティングは Webflow + AWS、制作は `NEW NORMAL`（75010 Paris）と自己開示。**<br>⚠️ **年齢確認ゲート・bot チャレンジには遭遇していない（回避行為なし）。Cookie バナーは `refuser` を選択。** |
| ⚠️ **`chateaupalmer.com`** | ⚠️ **到達不能** | **HTTP `000`（接続不成立）。内容不使用。** |
| ⚠️ **`chateau-palmer.fr`** | ⚠️ **到達不能** | **HTTP `000`（接続不成立）。内容不使用。** |
| ⚠️ **`palmer.fr`** | ⚠️ **却下** | **`HTTP 406 Not Acceptable`。本文が返らない。**⚠️ **「Palmer のサイトではない」証明ではない。内容不使用。** |
| ⚠️ **`chateaupalmer.fr`** | ⚠️ **却下** | **同じく `406 Not Acceptable`。内容不使用。** |
| ✅ **`gcc-1855.fr`** | ✅ **合格（限定用途）** | 🏛 **`mentions-legales` の `SIRET 48484166300012` が 🏛 企業登録の `CONSEIL DES GRANDS CRUS CLASSES EN 1855`（SIREN `484841663`、`1 COURS DU XXX JUILLET 33000 BORDEAUX`、NAF `94.11Z`、TVA `FR10484841663`）と一致。**<br>⚠️ **用途は「Palmer が `Troisième Cru / Margaux` として掲載されている」という事実のみ。1855 年の法令原文は掲載されていない。** |
| ⚠️ **`biodyvin.com`** | ⚠️ **合格（会員名簿としてのみ）** | **ラベル発行主体（SIVCBD）自身のサイト。会員リストの一次出典として使用。**⚠️ **`2012 ©` 表記で、`Un nouveau site est en cours de préparation ! Début 2026` と自ら告知している。加入年の情報は無い。** |
| ❌ **小売・オークション・評論家・アグリゲータ** | ❌ **一切不使用** | **`Vin Blanc de Palmer` の検索で idealwine / Vivino / CellarTracker / Wine-Searcher / Falstaff / 各種 e-commerce が返ったが、事実出典として 1 語も使っていない。** |
| ❌ **Wikipedia** | ❌ **不使用** | — |

### ✅ 公式サイト（`https://www.chateau-palmer.com/`、FR 原本）

- ✅ `robots.txt` → `sitemap.xml`（**134 URL**）→ **FR 側 67 ページを全件取得し全文検索**
- ✅ `/mentions-legales`（法人・RCS・SIRET・TVA・資本金・掲載責任者・ホスティング・制作者・クレジット）
- ✅ `/gamme`（🔴 **`Les Vins` ナビが `Château Palmer` / `Alter Ego` / `Livre de cave` の 3 項目しか持たないこと**）
- ✅ `/chateau-palmer`（グラン・ヴァン。**20〜22 か月・fûts → foudres・新旧樽のキュヴェ内均一化・10 年の caveau**）
- ✅ `/alterego`（🔴 **`L'autre grand vin` / `cet « autre vin »` / `lancé avec le millésime 1998`**）
- ✅ `/domaine`（🔴 **哲学・Plateau des Brauzes・graves・trois piliers・54 cuves 89–195 hl・cuvier expérimental・élevage en deux temps・Charles Palmer / Pereire / 1938 以降**）
- ✅ `/livre-de-cave`（🔴 **1950 年代〜2024 の全ヴィンテージのアッサンブラージュ・収穫日・年評。PDF リンク 56 本**）
- ✅ `/presse`（プレス素材の外部リンク 4 本。中身未取得）
- ✅ `/article/quelques-gouttes-du-rhone`（🔴 **Historical XIXth Century Wine の全文**）
- ✅ `/article/la-terre-nourriciere`（🔴 **ビオディナミの年表・家畜・堆肥・アグロフォレストリー・菜園**）
- ✅ `/article/2014-un-voile-sest-leve`（🔴 **2014 年の 100% 転換・亜硫酸無添加**）
- ✅ `/article/sabrina-pernet-une-vigne-sous-influence`（🔴 **2009 年 parcelle Boulibranne**）
- ✅ `/article/les-cinq-iles-de-palmer`（🔴 **5 つの îlot・Le Cassena の `quatre cépages de blanc`・植栽密度**）
- ✅ `/article/la-saga-des-freres-pereire`（🔴 **83 ha・1855 の公式な言い回し**）
- ✅ `/article/clairet-de-charles-palmer`（🔴 **163 ha・15 fûts・trois pressoirs・hermitagé の説明**）
- ✅ `/article/le-serment-du-tailleur` / `/article/symphonie-en-sous-sol` / `/article/les-reines-animales` / `/article/le-jardinier-du-chateau` ほか（栽培・畜産・区画の実務）
- ✅ `/en/range` / `/en/alterego`（🔴 **`THE OTHER WINE OF CHÂTEAU PALMER`。FR との差の確認用。採用は FR**）

### ✅ 公式 Fiche Millésime PDF（**全点 `%PDF` 実体を確認。HTML が返る偽 PDF は無し**）

| ファイル | 対象 | サイズ |
|---|---|---|
| ✅ `Fiche_millesime_FR_1996.pdf` | 🔴 **OBP 5 行目**（4 品種・Cabernet franc 4%・**Alter Ego ブロック無し**） | 317,054 B |
| ✅ `Fiche_millesime_FR_2012.pdf` | 🔴 **OBP 4 行目** | 316,993 B |
| ✅ `Fiche_millesime_FR_2013.pdf` | 🔴 **OBP 3 行目**（`un tiers de la récolte`） | 317,212 B |
| ✅ `Fiche_millesime_FR_2014.pdf` | 🔴 **OBP 2 行目**（`Le vin du bicentenaire`・亜硫酸） | 321,631 B |
| ✅ `Fiche_millesime_FR_2017.pdf` | 🔴 **OBP 1 行目** | 317,222 B |

⚠️ **`/livre-de-cave` には合計 56 本の Fiche PDF がリンクされている。本調査で取得したのは OBP に対応する 5 本のみ。**

### 🏛 公的登録・規制一次資料

| 出典 | 取得内容 |
|---|---|
| 🏛 **`recherche-entreprises.api.gouv.fr/search?q=CHATEAU PALMER&code_postal=33460`** | 🔴 **SIREN `781863428`／SIRET `78186342800012`／NAF `01.21Z`／`nature_juridique 6599`／TVA `FR25781863428`／`est_bio: true`／`liste_id_bio: [157054]`／`dirigeants` 152 件** |
| 🏛 **同 `?q=PALMER&departement=51`** | 🔴 **Marne（Champagne）側の同名法人 15 件。`CHAMPAGNE PALMER & CO` の商号は返らない。Gironde 側との SIREN の非同一を確認** |
| 🏛 **同 `?q=484841663`** | **`CONSEIL DES GRANDS CRUS CLASSES EN 1855`（gcc-1855.fr の真正性確認）** |
| 🔴 🏛 **`opendata.agencebio.org/api/gouv/operateurs/?siret=78186342800012`** | 🔴 **`nbTotal: 1`。`numeroBio 157054` / `Ecocert France` / `FR-BIO-01` / `ENGAGEE` / `datePremierEngagement 2011-09-08` / `activites: Production + Préparation` / `Raisin de cuve: C1 + AB` / `Vins de raisin: AB`** |
| 🔴 🏛 **`certificat.ecocert.com/entreprise/D3C0543A-52D4-4E50-A128-65CC0AEF0DBA`** | 🔴 **`Certification Agriculture biologique Europe (EU) 2018/848 [FR]`／`Document en vigueur`／`Agriculteur (production végétale), Agriculteur (production animale), Fabricant & Transformateur`／4 カテゴリ** |
| 🔴 🏛 **`www.demeter.fr/adherents/sc-chateau-palmer/`** | 🔴 **`SC CHATEAU PALMER`。製品 8 件（`Vin blanc Vin de France "Blanc de Palmer"` × 2、`Vin rouge Margaux "Alter Ego"` × 2、`Vin rouge margaux "château palmer"` × 2、無名の白・赤 各 1）。相互リンク `http://www.chateau-palmer.com`** |
| 🔴 🏛 **`www.demeter.fr/adherents-sitemap.xml`** | **加盟者 993 件を列挙。`palmer` に一致するのは `sc-chateau-palmer` の 1 件のみ（同名の別加盟者なし）** |
| 🔴 🏛 **`www.biodyvin.com/fr/liste-des-membres-biodyvin.html`** | 🔴 **`224 adhérents en 2025`。`Château Palmer / 33460 / Margaux / Bordeaux` の行が実在** |
| 🏛 **`www.biodyvin.com/fr/le-label-biodyvin.html`** | **ラベルの仕組み（Ecocert SAS France による監査、4 年の転換期間）** |
| 🔴 🏛 **`info.agriculture.gouv.fr/gedei/site/bo-agri/document_administratif-e303df21-…/telechargement`** | 🔴 **AOC「MARGAUX」CDC **consolidated**（`homologué par arrêté du 31 mars 2023, publié au JORF du 5 avril 2023`、BO du MASA 2023-04-13）。`%PDF` 実体・685,416 B。**<br>🔴 **赤専用・コミューン 4 件・品種 6+1・植栽密度・収量・度数・ラベル規定** |
| 🔴 ⚠️ **`extranet.inao.gouv.fr/fichier/3-CDC-Margaux.pdf`** | 🔴 **同 CDC の **PNO 草案版**（2022-09-08 の avis に続く手続き）。`%PDF` 実体・162,062 B。**<br>🔴 **抽出テキストが `Cantenac` を含む 5 コミューンを返す ＝ §2c の罠の実例。数値の引用には使わない** |
| ⚠️ **`extranet.inao.gouv.fr/fichier/PNOCDCMargaux.pdf`** | **もう 1 つの PNO 版（147,554 B）。相互検証用に取得** |
| 🔴 🏛 **`geo.api.gouv.fr/communes/33268`** | 🔴 **`{"nom":"Margaux-Cantenac","code":"33268","codesPostaux":["33460"],"anciensCodes":["33091"]}`。`?nom=Cantenac&departement=33` は `Margaux-Cantenac` 1 件のみを返す** |
| ✅ **`gcc-1855.fr/the-1855-grand-cru-classification/the-gcc-1855-classification-by-appellation/`** | **Palmer が `Troisième Cru` / `Margaux` として掲載されていること**⚠️ **1855 年の法令原文そのものは掲載されていない** |

### 🔍 THÉSEUS 内部

- 🔍 `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行中 `Palmer` 5 行）
- 🔍 `migration/out/export/db_wine_canonical.json`（928 要素。**読み取りのみ**）

**キャッシュ先**: `research/producers/_sources/chateau-palmer/`（gitignored）
`sitemap.xml` / `site/*.html`（FR 67 ページ）＋ `site/*.txt`（抽出済み）/ `pg_*.html` / `en_*.html` /
`fiche_{1996,2012,2013,2014,2017}.pdf` / `cdc_boagri_margaux.pdf` / `cdc_3-CDC-Margaux.pdf` / `cdc_PNOCDCMargaux.pdf` /
`cdc_margaux.txt` / `agencebio_siret.json` / `palmer_siren.json` / `ecocert.html` / `demeter_palmer.html` / `cdx2.txt`

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🔴 **社名・法人格・RCS・SIRET・資本金・TVA・掲載責任者が mentions légales で確定し、🏛 企業登録と完全一致。**🔴 **株主構成 152 件を実測し、`Société Sichel` / `FRITZ` / `SASU THDUROUX` の gérant 3 社まで特定。**🔴 **Champagne Palmer & Co との混同が canonical に無いことを 928 件走査で確認。**⚠️ **Champagne 側の法人特定だけが未完了** |
| **Overview** | **High** | **「2 本の兄弟」「同率の植栽」「ferme holistique」という 3 つの自己規定が、すべて一次で取れた** |
| 🔴 **History** | 🔴 **Medium-High** | ✅ **1814 / 1843 / 1853 / 1855 / 1938 / 1961 / 1998 / 2004 / 2005 / 2009 / 2014 / 2016 / 2018 / 2020 の 14 点を公式で確定。**🔴 **1855 についての公式の言い回しを verbatim で取れたのが大きい。**⚠️ **1843–1938 の所有者系列と「4 家族」の内訳が不在** |
| 🔴 **Location** | 🔴 **High** | 🔴 **🏛 コミューンを `geo.api.gouv.fr` と CDC の 2 系統で確定し、`Cantenac` という前提を実測で訂正した。**🔴 **🏛 CDC の consolidated / PNO 2 版を突き合わせて §2c の罠を実証。**🔴 **赤専用・品種リスト・植栽密度・収量を 🏛 法令から直接取得。**✅ **5 つの îlot と土壌を公式で確定。**🔴 ⚠️ **面積だけが公式に無く、そこが埋まらない** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **3 系統（Agence Bio / Ecocert / Demeter / Biodyvin）を SIRET 完全一致と加盟者ページで確定し、`etatProduction` レベルまで実測。**🔴 **造り手側の転換年表（2009 → 2014）を公式 3 記事で確定。**🔴 **その 2 つを突き合わせて、OBP 5 本すべてについて per-vintage の判断を書き切った。**⚠️ **証明書番号・有効期間・Demeter / Biodyvin の加入年が不明** |
| 🔴 **Winemaking** | 🔴 **Medium-High** | 🔴 **54 基 89–195 hl・cuvier expérimental 9 micro-cuves・20〜22 か月・225 l → 30 hl foudre・新樽半分未満・2014 の亜硫酸・アッサンブラージュの選別基準が公式。**⚠️ **発酵温度・マセラシオン・酵母・度数・生産本数・瓶詰日が全面的に不在** |
| **Style** | **Medium-High** | ✅ **2 本の公式スタイル記述と、OBP 5 ヴィンテージすべての公式年評を全文取得。**⚠️ **公式は点数も受賞も一切掲載しておらず、第三者の言葉は Peynaud の引用 1 件のみ** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **OBP 5 行すべてについて、公式 Fiche Millésime の実在・アッサンブラージュ・収穫日・年評を確定。**🔴 **`Alter Ego` の位置づけを造り手の言葉で確定し、「セカンド」を否定した。**🔴 **`Historical XIXth Century Wine` を公式全文で確定。**🔴 **白の designation を 🏛 Demeter 登録で確定。**⚠️ **白の正確な名称の綴りと、Historical の実際の designation だけが未決着** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **27 主張を 1 件ずつ検証して 15 の失敗を確定。**🔴 **`palmer-1855` が名簿行であることを 21 件の同型レコードと CDC の「21 grands crus classés」の一致で示した。**🔴 **`47/47/6` の出所を 2016 ヴィンテージまで特定した。**🔴 **intake の evidence 文字列が偽であることを示した** |
| **Staff Notes** | 🔴 **High** | 🔴 **芯 3 点＋ must-not-say 13 項目。canonical をそのまま読むと出る 8 つの嘘（スーパーセカンド / セカンドワイン / シラー 15% / Vin de France / 66 ha / 18–21 か月 / 47:47:6 / 北寄り）と、現場で出やすい 5 つを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を超過。実感としては 85% 前後）。** | **OBP 5 行すべてについて、造り手の正式名・格付・そのヴィンテージのアッサンブラージュ・収穫日・公式の年評・熟成仕様をそのまま言える。**<br>**栽培は 3 系統の登録を正確に述べたうえで、5 本すべてに「認証を結びつけない」という安全な線が引けている。**<br>**欠けているのは ① 現在の栽培面積、② 白と Historical の実ラベル、③ 醸造の分析値、④ 認証の取得年・証明書番号。**<br>**①③④ は「言わない」で回避でき、② は物理ラベルで決着する。卓上で嘘をつく経路は塞いである。** |

**reached_70: YES (~85%)。**

---

## Open Questions

1. 🔴 **【物理ラベル・タスク】`Historical XIXth Century Wine` の実ボトル。**
   **確認すべきは 3 点 —— ① 表ラベルの記載事項の全て（公式は「Palmer の名も château もアペラシオンも無い」と書くだけ）、
   ② 裏ラベルの法定表示（`Vin de France` か、それ以外か。瓶詰者の名称と住所）、③ 実際のヴィンテージ表示の有無。**
   🔴 **公式は `brave les appellations et s'affranchit des normes` としか書かず、designation を明かさない。オンラインの一次資料はここまでしか到達できない。**
   🔴 **canonical は `Vin de France` と断定しているが、その根拠は本調査では確認できなかった。**

2. 🔴 **【物理ラベル・タスク】白の正確な名称。**
   🏛 **Demeter France の登録は `Blanc de Palmer`。**⚠️ **一方、検索で返る第三者サイト（idealwine / Vivino / CellarTracker / Wine-Searcher / Falstaff 等。いずれも本ドシエでは不使用）は `Vin Blanc de Palmer` と綴る。**
   🔴 **公式サイトは白について完全に沈黙している。実ラベルで ① 名称の綴り、② `Vin de France` の表示、③ 品種表示の有無、④ 初リリース年を読む必要がある。**
   ✅ **公式が唯一書いているのは、îlot `Le Cassena` に「en plus des rouges, `quatre cépages de blanc`」があるということだけである。その 4 品種の名前も公式に無い。**

3. 🔴 **現在の栽培面積（ha）。**
   **公式サイト 67 ページを全文検索しても現在の面積が出てこない。出るのは `163 ha`（19 世紀）、`83 ha`（1853）、`13 ha`（îlot Domec）、`28 ha`（家畜）のみ。**
   **canonical の `66 ha` の出所が不明。造り手に直接請求するか、`presse` の Toolkit（Open Questions 6）に当たるのが最短。**

4. ⚠️ **1855 年格付の法令原文。**
   **本調査では `gcc-1855.fr`（Conseil、SIREN 一致で真正性確認済み）が Palmer を `Troisième Cru / Margaux` として掲載していることまでしか取れなかった。**
   ⚠️ **1855 年 4 月 18 日の分類そのものは、Chambre de commerce / courtiers の文書であって現代の法令ではない。**🏛 **INAO の CDC は「21 grands crus classés」という総数には触れるが、個別のシャトー名と順位を列挙していない。**
   🔴 **canonical の `classification` 文字列（`3ème Grand Cru Classé`）と、公式・Conseil の表記（`Troisième Cru`）のどちらを正典とするかは、CTO の判断が要る。**

5. ⚠️ **認証の細部。**
   ⚠️ **① Ecocert 証明書の番号と有効期間（HTML には出ず、PDF ダウンロードが別導線）。**
   ⚠️ **② Demeter France の加入年と、製品リストの `2019 - 2020` 等が「ヴィンテージの対」なのか「認証の参照年度」なのか。**
   ⚠️ **③ Biodyvin の加入年（会員リストに無い）。**
   🔴 **④ `Raisin de cuve` に `C1` が立っている区画がどこか（新規取得地か、植え替えか）。**
   🔴 **これらが埋まれば、2014 / 2017 のボトルについて言えることがもう一段増える。現状は「造り手の公表した転換年表」までが上限である。**

6. ⚠️ **公式プレス素材（未取得）。**
   **`/presse` は `Fiches Millésimes` / `Toolkits` / `Packshots` / `Médias & logos` の 4 つを Google Drive フォルダへ外部リンクしている。**
   **本調査ではフォルダの中身に到達していない。`Toolkits` に面積・生産本数・ラベル画像が含まれる可能性が高い。**

7. ⚠️ **Champagne Palmer & Co の法人特定。**
   🏛 **`?q=PALMER&departement=51` の 15 件に `CHAMPAGNE PALMER & CO` という商号は無い。同社の住所域（`ZI LA POMPELLE 51100 REIMS`）には `PALM SAS`（SIREN `612028282`、NAF `70.10Z`）と `PALM PACKAGING CHAMPAGNE`（`808490080`）がある。**
   ⚠️ **`D-2026-08-05-08` の disambiguation としては「Gironde と Marne で SIREN が別」で十分だが、シャンパーニュ側にドシエを起こす日が来たら、この商号と SIREN の対応を先に決める必要がある。**

8. ⚠️ **Alter Ego 以前の「もう 1 本」の有無。**
   ✅ **公式は「Alter Ego a été lancé avec le millésime 1998」と書くだけで、それ以前に別ラベルがあったかを書かない。**
   🔴 **公式 Fiche Millésime の 1996 と 1995 には `ALTER EGO` のブロックが無く、2012 以降には必ずある。切り替わりの正確な年は 56 本の Fiche をすべて見れば決まる（本調査では 5 本のみ取得）。**

9. ⚠️ **【物理ラベル・タスク】OBP 5 行が `Château Palmer`（grand vin）であることの最終確認。**
   🔴 **公式の表記体系（`Alter Ego` は必ず `Alter Ego` と書く）と価格帯から grand vin と判定したが、決着は実ラベルでつく。**
   ✅ **2009 年以降のボトルには QR コードがあり、公式の `Authentifier votre bouteille` / `/authentification` で照合できる。2012 / 2013 / 2014 / 2017 の 4 本はこの範囲に入る。1996 は入らない。**

10. ⚠️ **公式 Fiche Millésime の内部不一致（2 件）。**
    🔴 **2017: ヘッダ `Du 13 septembre au 5 octobre` ⟷ 本文「Nous commençons les vendanges `le 20`」。**
    🔴 **2012: ヘッダ `Du 27 septembre au 15 octobre` ⟷ 本文「Les vendanges se déroulent entredu `1er au 15 octobre`」（原文に誤植 `entredu`）。**
    ⚠️ **どちらも同一 PDF 内の食い違い。造り手に確認が要る。両論を保存してある。**

11. ⚠️ **`FRITZ`（SIREN `518992706`）の性格。**
    🏛 **`Société Civile du Château Palmer` の `Gérant et associé indéfiniment responsable` である法人。本店は `8 RUE MONTESQUIEU 75001 PARIS`、NAF `64.20Z`（持株会社）。**
    🏛 **旧établissement が `CHATEAU PALMER 33460 MARGAUX-CANTENAC` にあり、2009-12-31 に閉鎖されている。**
    ⚠️ **どの一族の持株会社かは登録からは決まらない。ドシエの記述には使っていない。**

12. ⚠️ **`Les Jasmins` と `Les Marronniers` という 2 つの chai の関係。**
    ✅ **公式は「aux `« Jasmins »` comme dans la pénombre de l'`historique chai des « Marronniers »`」と並べるが、どちらでどの段階（barrique か foudre か）を行うかを書いていない。**
