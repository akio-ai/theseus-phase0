# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件も存在しない。**
> **928 レコードの export 全体を機械走査し、`producer` フィールドが `Château-Figeac` / `Chateau Figeac` /
> `Figeac` / `Petit-Figeac` のいずれでもあるレコードが 0 件であることを実測した。OBP は 3 行。
> すなわち 3 行すべてが canonical の「欠落（gap）」である。**
> 🔒 **gap は conflict ではない（`CDX-23`）。canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式資料で確認**（`www.chateau-figeac.com` 本体・同ドメイン配信の公式 PDF・公式ボトルショット画像）
> `🏛` **公的登録簿／規制一次資料** —— **INAO（AOC「Saint-Emilion grand cru」cahier des charges・
>    classement 2022 の公式リストと communiqué）、Légifrance（1996 / 2012 / 2022 の 3 本の arrêté）、
>    `recherche-entreprises.api.gouv.fr`、Agence Bio OpenData、data.gouv.fr HVE 年鑑、Verisign RDAP**
> `📄` **生産者著作だが生産者ドメイン外で配信されている資料** —— **本書では Wayback に残る旧公式 PDF 2 種のみ**
> `⚠️` **出典間で食い違い／出典が沈黙している／第三者の主張であって未確認**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://www.chateau-figeac.com/`**
> 走査元: **`robots.txt` → `sitemap.xml`（子サイトマップ 6 本）**、
> **`page-sitemap.xml`（26 URL）/ `millesime-sitemap.xml`（26 URL）/ `article-sitemap.xml`（88 URL）/
> `post-` `category-` `author-sitemap.xml`**、および **Wayback CDX（`chateau-figeac.com` ドメイン全体 2,006 URL）**
> ⚠️ **公式サイト内検索（`/?s=`）は機能していない**（`2009` / `2010` / `Petit-Figeac` のいずれを投げても
> 同一の日付スタブ 1 件しか返さない）。**したがって「検索で出ない＝無い」は本サイトでは使えない。
> 本書の網羅性はすべてサイトマップと Wayback CDX の機械列挙に依っている。**
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ① —— OBP 3 行は、メニューの情報だけでは解けない。これは行の欠陥ではなく構造である。**
> 🔍 **3 行とも印字は `Figeac` / `Saint-Émilion Grand Cru` / 年号のみ。`_parts.label` は 3 行とも `null`。**
> 🔴 **`Saint-Émilion Grand Cru` は 🏛 AOC の名称そのものであって、キュヴェ名ではない（→ §Important Cuvées）。**
> 🔴 **そして Château-Figeac は同じ AOC でセカンドワインを出している。**
> 🔴 ✅ **しかもその名は年代で変わる ——「`La Grange Neuve de Figeac`（1945 年〜2011 年）」→
> 「`PETIT-FIGEAC`（2012 年ミレジムから）」。造り手が自分の年表で明記している。**
> → 🔴 **2018 行の取り違え先は `Petit-Figeac`、2010 / 2009 行の取り違え先は `La Grange Neuve de Figeac` であり、
> 同じ名前ですらない。行のどこにも grand vin と second vin を分ける語が無い。**
> 🔒 **本書は 3 行を grand vin に黙って寄せない。実ラベル案件として Open Questions 1 に送る。**
>
> 🔴 **本ドシエ最大の収穫 ② —— 格付けは `CDX-25` の教科書的な事例で、しかも 3 本とも「A」より前の酒である。**
> 🏛 **Légifrance『Arrêté du 15 décembre 2022』第 2 条：「`Le présent arrêté s'applique à compter de la
> récolte 2022.`」——同第 3 条で 2012 年の arrêté を廃止。リスト上の表記は「`Château FIGEAC (distinction A)`」。**
> 🔴 **OBP の 3 ヴィンテージ（2018 / 2010 / 2009）はいずれも 2022 年収穫より前である。
> したがって、この 3 本のラベルに「A」は載り得ない。本書は遡って付けない。**
> 🔴 **同じ事実について公式の言い方が 3 通りある（→ §Important Cuvées の表）:**
> **🏛 INAO =「14 premiers grands crus classés `dont 2 bénéficiant de la distinction A`」／「Château FIGEAC (distinction A)」·
> 🏛 ODG（Conseil des Vins de Saint-Émilion）=「14 Premiers Grands Crus Classés `dont 2 Premiers Grands Crus Classés « A »`」·
> ✅ 蔵 =「`Premier Grand Cru Classé "A"`」。**
> 🔴 **`CDX-25` の言うとおり、どれか 1 つが「正しい格付け文字列」なのではない。**
>
> 🔴 **本ドシエ最大の収穫 ③ —— 3 行のうち 2 行は、造り手の資料が存在しない。しかも 404 で確定できる。**
> 🔴 **公式ヴィンテージ頁は 12 年分しかない（1949 / 1964 / 1971 / 1995 / 2013 / 2015 / **2018** / 2019 / 2020 / 2021 / 2022 / 2023）。**
> 🔴 **`/millesime/2009/`・`/millesime/millesime-2009/`・`/millesime/2010/`・`/millesime/millesime-2010/` は
> すべて実 HTTP `404` を返す（ソフト 404 ではない）。**
> → 🔴 **2018 についてはセパージュも収穫日も気候も造り手の言葉で言える。2009 と 2010 については何も言えない。
> この非対称を卓上で潰さない。** → §Staff Notes ⚠️ ③
>
> 🔴 **本ドシエ最大の収穫 ④ —— `D-2026-08-05-08`（名前の部分一致）の危険が、法令の側から実証できた。**
> 🏛 **1996 年の classement（arrêté du 8 novembre 1996）の「B. - Saint-Emilion grands crus classés」の列挙に、
> `Tour du Pin Figeac (la) (Giraud-Belivier)` / `Tour du Pin Figeac (la) (Moueix)` / `Tour Figeac (la)` /
> `Yon-Figeac` の 4 軒が入っている —— いずれも Château-Figeac より下の格である。**
> 🏛 **2022 年の classement でも `Château LA TOUR FIGEAC` と `Château YON-FIGEAC` は Grands Crus Classés。**
> 🏛 **企業登録では郵便番号 33330（Saint-Emilion）だけで `figeac` を含む法人が 49 件ヒットする。**
> → 🔴 **本書は SIRET 完全一致でしか同定していない。**
>
> ⚠️ **調査上の制約 ① —— Légifrance は `curl` に対し HTTP `403`（bot 防御）を返した。**
> **3 本の arrêté は WebFetch 経由でしか読めていない。逐語は `_sources/.../NOTES-legifrance-verbatim.md` に退避した。**
> **⚠️ 403 は「条文が存在しない」ことの証拠ではない。**
>
> ⚠️ **調査上の制約 ② —— 該当 3 本の実ボトル（表ラベル・裏ラベル）を 1 枚も読めていない。**
> **読めたのは造り手が自社ドメインで配信する「ヴィンテージ欄が空白の見本ラベル」画像 1 枚のみ。** → Open Questions 1

---

## Identity

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Figeac`** |
| **Canonical Name** | ✅ **`Château-Figeac`**（造り手自身の表記は**ハイフン付き**。本文中で一貫して `Château-Figeac`、ラベル上は `CHATEAU - FIGEAC`） |
| 🔴 **法人名（サイト運営者）** | ✅ 🏛 🔴 **`SCEA Famille Manoncourt`**<br>✅ **Mentions Légales 冒頭：「`Le site www.chateau-figeac.com est édité par la SCEA Famille Manoncourt.` `Numéro RCS : 385 067 970` / `Numéro SIRET : 38506797000017` / `Numéro TVA : FR76385067970` / `Siège social : CHATEAU de FIGEAC 33330 Saint-Emilion FRANCE`」**<br>🏛 **`recherche-entreprises.api.gouv.fr` と完全一致：`SIREN 385067970` / `SIRET 38506797000017`（**établissement は 1 つだけ**）/ `NAF 01.21Z`（culture de la vigne）/ 本店 `CHATEAU FIGEAC 3572 ROUTE DE LIBOURNE 33330 SAINT-EMILION` / `date_creation 1992-03-24` / `état A`** |
| 🔴 **同一住所の別法人（混同注意）** | 🏛 🔴 **`CHATEAU FIGEAC-MANONCOURT PROPRIETAIRE`（SIREN `781985296` / SIRET `78198529600016` / 設立 `1957-06-28` / NAF `68.20B` 不動産賃貸）**、**`MANONCOURT`（`384796686`）**、**`LCBH DISTRIBUTION`（`504914540`）**、**`SOCIETE CIVILE MANONCOURT D'ARAMON`（`428652861`）**<br>🔴 **同じ「CHATEAU FIGEAC 3572 ROUTE DE LIBOURNE」に少なくとも 4 法人が登記されている。**⚠️ **Haut-Brion で「1 SIREN・3 SIRET」が起きた形の逆（複数 SIREN・同一住所）。本書は栽培法人＝`SCEA Famille Manoncourt`（NAF 01.21Z）を SIRET で特定し、他は使っていない** |
| 🔴 **Aliases（混同してはいけない別蔵）** | 🏛 🔴 **`Château La Tour Figeac`（`SOCIETE CIVILE LA TOUR FIGEAC` SIREN `304367253`。2022 年 classement で **Grand Cru Classé**）／`Château Yon-Figeac`（`393983929`。同じく **Grand Cru Classé**）／`Château Cormeil-Figeac`／`Château Cros Figeac`／`Château Grand Barrail Lamarzelle Figeac`／`Château La Grave Figeac`／`Château Bellevue Figeac` ほか**<br>🏛 **1996 年 classement の grands crus classés には `Tour du Pin Figeac (la) (Giraud-Belivier)` と `(Moueix)` の 2 軒も別個に載る**<br>⚠️ 🔴 **`Croque-Michotte` は本調査で読んだ公式・法令資料のいずれにも `Figeac` の語と結び付けて現れなかった。本書は言及しない** |
| **所在** | ✅ **`Château Figeac, 33330 Saint-Emilion, FRANCE` ／ `+33 (0)5 57 24 72 26` ／ Fax `+33 (0)5 57 74 45 74` ／ `chateau-figeac@chateau-figeac.com`**<br>🏛 **登記上は `3572 route de Libourne`（緯度 `44.9128267` / 経度 `-0.19243893`）** |
| 🔴 **Directeur de la publication** | ✅ **`Frédéric FAYE`**（Mentions Légales） |
| 🔴 **Directeur Général** | ✅ 🔴 **`Frédéric Faye`。**公式：「**Ingénieur agronome diplômé de Sciences Agro Bordeaux. Arrivé à Château-Figeac en 2002 comme stagiaire, il devient `chef de culture en 2008` puis `directeur technique en 2010`. Il assure la direction opérationnelle du domaine comme `Directeur Général de Château-Figeac depuis 2013`.**」<br>🔴 **すなわち 2009 年収穫時は chef de culture、2010 年収穫時は directeur technique、2018 年収穫時は DG。同じ人物だが役職が違う** |
| 🔴 **前 DG（2009・2010 当時）** | ✅ 🔴 **`Comte Eric d'Aramon`（Thierry Manoncourt の娘 Laure の夫）。**公式年表「**1988-2013**」の項：「**Eric d'Aramon, DG, devient membre de la Jurade de Saint-Emilion**」。📄 **2012 年の公式フィッシュにも `Comte Eric d'Aramon` と印字されている** |
| 🔴 **オーナー（現）** | ✅ 🔴 **`Famille Manoncourt`。**公式の役職名：**`Marie-France Manoncourt`（Présidente d'Honneur, cogérante, copropriétaire）／`Hortense Idoine Manoncourt`（Présidente du Conseil d'administration, cogérante, copropriétaire）／`Blandine de Brier Manoncourt`（Secrétaire Générale, copropriétaire, Jurat de Saint-Emilion）／`Jean-Valmy Nicolas`（Co-gérant）**<br>🏛 **登記上の `Gérant et associé indéfiniment responsable` は `MANONCOURT (DUBOYS DE LABARRE) Thérèse Marie France`（1935 年生）。**🔴 **公式サイトの「Marie-France」と登記の「Thérèse Marie France」は同一人物と読めるが、造り手はこの対応を明示していない。本書は登記名をそのまま記録する** |
| 🔴 **Directeur technique（現）** | ✅ **`Romain Jean-Pierre`** |
| 🔴 **Œnologue conseil** | ✅ 🔴 **`Michel Rolland`（2013 年〜）。**公式年表 2013 年の項：「**Michel Rolland succède à `Gilles Pauquet` comme Oenologue conseil.**」<br>🔴 **したがって 2009 年・2010 年の醸造顧問は `Gilles Pauquet`、2018 年は `Michel Rolland`。3 本を一括りにできない** |
| **Maître de chais（2012 年時点）** | 📄 **`Jean Albino`**（Wayback に残る 2012 年の公式フィッシュ）。⚠️ **現行サイトに氏名の記載は無い** |
| 🔴 **格付け（現）** | 🏛 🔴 **`premier grand cru classé` + `distinction A`（`Arrêté du 15 décembre 2022`、récolte 2022 から）**<br>✅ **蔵自身の言い方は `Premier Grand Cru Classé "A"`** → §Important Cuvées |
| 🔴 **格付け（1955〜2021）** | ✅ **「`Dès la création du classement de Saint-Emilion, Château-Figeac est Premier Grand Cru Classé.`」（公式年表 1955 年）**<br>🏛 **1996 年 arrêté では「A. - Saint-Emilion premiers grands crus classés」の `b)` 群（`a)` は Ausone と Cheval Blanc の 2 軒）**<br>🏛 **2012 年 arrêté では premiers grands crus classés に `Château Figeac`、distinction 表記なし** |
| **創業／家族所有** | ✅ **「`Château-Figeac appartient à la même famille depuis 1892`」。**取得者は **`Henriette de Chèvremont` と夫 `André Villepigue`**（Thierry Manoncourt の祖父母） |
| **canonical id** | 🔍 🔴 **無し（0 件）。**🔴 **文字列 `Figeac` を含む canonical レコードは 6 件あるが、6 件とも `producer = 'Bordeaux'` の**ヴィンテージ参考表**（`bordeaux-vintage-19XX-guide`）であり、ボトルのレコードではない** → §Canonical Conflict |
| 🏛 **ドメイン** | 🏛 **`chateau-figeac.com`：Verisign RDAP `registration 1997-05-22` / `expiration 2027-05-23` / registrar `OVH sas` / NS `DNS101.OVH.NET`・`NS101.OVH.NET`**<br>⚠️ **公式年表は「1990 年、ボルドーで最初期に自社サイトを作った」と書くが、`.com` の登録は 1997 年である。別ドメインの可能性もあり、本書はどちらとも主張しない** |

---

## Overview

✅ **サン=テミリオンの西端、ポムロールとの境に接する 54 ヘクタールの一枚地。1892 年以来同じ家族のもので、
現在の姿は 1947 年に入った Thierry Manoncourt（アグロノム）が 60 ミレジム以上かけて作った。**
公式：「**Propriété historique de Saint-Emilion, Château-Figeac appartient à la même famille depuis 1892…
De 1947 à 2010, Thierry Manoncourt a créé le ''style Figeac'', avec un sens de l'innovation et un respect du
vivant très en avance sur son temps.**」

🔴 ✅ **蔵の自己規定は「地質の例外」と「例外的なセパージュ」の 2 点に集約される。**
「**Le terroir viticole de Château-Figeac est une ''exception géologique'' de son appellation, avec
`trois croupes de graves` composées de `quartz et de silex` sur plusieurs mètres d'épaisseur et des
`argiles bleues` en sous-sol**」
「**Château-Figeac doit son caractère singulier à la combinaison unique de `trois croupes de graves
günziennes` aux sous-sols argileux, de plusieurs microclimats et d'un encépagement composé de
`cabernet sauvignon, cabernet franc et merlot`.**」

🔴 ⚠️ **ただしカベルネ比率について、造り手は同じ 1 頁の中で 2 つの数字を書いている。**
「**Ceux-ci induisant `70%` de l'assemblage**」と「**Cet assemblage original, dominé pour `2/3` de cabernets**」。
📄 **2012 年の公式フィッシュは植栽比率として `35% Cabernet Sauvignon / 35% Cabernet Franc / 30% Merlot` を挙げる。**
✅ **2021 年の公式データシート（EN）は「`Cabernet Sauvignon, Cabernet Franc and only 1/3 Merlot`」。**
→ 🔴 **これらはすべて「畑の植栽」の話であって、ある年のアッサンブラージュではない。
実際、公式が数字を出している唯一の該当年 **2018 年は `37% Merlot / 33% Cabernet Sauvignon / 30% Cabernet franc`
＝カベルネ計 63%** であり、70% でも 2/3 でもない。** → §Staff Notes ⚠️ ①

🔍 **THÉSEUS における状態は「3 行に対して 0 レコード」。生産者そのものが canonical に存在しない。**

---

## History

### Foundation（土地の起源 —— 造り手の年表の逐語）

| 年 | 出来事 | 典拠 |
|---|---|---|
| **II 〜 XV 世紀** | **`FIGEACUS` 家のガロ・ローマ期の大ヴィラが現在の château の位置にあった。ブドウが存在し、中世に seigneurie になる。** | ✅ **公式年表** |
| **XV 〜 XIX 世紀** | **`Decazes` 家、次いで姻戚で `de Carle` 家の seigneurie。** | ✅ **公式年表** |
| **1586** | **`Raymond de Cazes` が宗教戦争で焼けた城を再建。ルネサンスの痕跡（大中庭の柱、塔、ムニョン窓）。** | ✅ **公式年表** |
| **1654** | **`Marie Decazes` の婚姻により `Carle` 家へ。リブルネ地方の「近代的」ブドウ栽培の初期に深く関与し、パリと北欧に顧客を持つ。** | ✅ **公式年表** |
| 🔴 **1832** | 🔴 **`comtesse Félicité de Carle-Trajet` が家運の傾きから **Figeac の大所領の区画を初めて売却**。現在の propriété は旧所領の中心部（3 つの graves の丘と château の周り）にあたる。** | ✅ **公式年表** |
| 🔴 **1832–1838** | 🔴 **Thierry Manoncourt 自身の言葉：「**ce domaine qui `avait donné naissance à Cheval Blanc (1832 – 1838)`**」** | 📄 **公式 PDF `Le Parcours d'une vie`（造り手の講演からの抜粋）**<br>🔴 **造り手が名指しで書いている「Figeac から生まれた蔵」はこの 1 軒だけである。他の蔵を Figeac 由来として語らない** |
| **1876** | **フィラデルフィア万国博覧会に、サン=テミリオンから唯一 Château-Figeac が出品。** | ✅ **公式年表** |
| 🔴 **1892** | 🔴 **`Henriette de Chèvremont` と夫 `André Villepigue`（Thierry Manoncourt の祖父母）が取得。友人でフィロキセラ対策で知られたアグロノム `Albert Macquin` が購入を勧め、その後 10 年間 Château-Figeac を経営し、畑を再構成し、cuvier を再装備し、公園に珍しい植物を導入した。** | ✅ **公式年表** |
| **1906** | 🔴 **`Robert Villepigue`（Thierry Manoncourt の叔父／現所有者たちの大叔父、アグロノム）が 1906 年ミレジムのために現在のラベルを創作。**「**Pas de classique gravure du château… mais le nom manuscrit de Château-Figeac porté haut et fort, souligné d'un rouge un peu canaille… Le cachet de cire symbolise la garantie de fiabilité**」 | ✅ **公式年表／公式記事 `La fameuse étiquette`** |
| **1917** | **Thierry Manoncourt 誕生（Neuilly）。** | ✅ **公式年表／📄 `Le Parcours d'une vie`** |
| **1920** | **Château-Figeac は「pupilles de la nation」のための栽培実習センターになる。** | ✅ **公式年表** |

### Generations（Manoncourt 期）

| 年 | 出来事 | 典拠 |
|---|---|---|
| 🔴 **1947** | 🔴 **Thierry Manoncourt が「1 年だけのつもりで」Figeac に入る。**「**Il apporte à la viticulture et à la vinification une série d'innovations marquantes. On lui doit en particulier le `choix de l'encépagement unique` qui est à la base du « style » Figeac.**」 | ✅ **公式年表** |
| 🔴 **1945** | 🔴 **セカンドワインの誕生。**Thierry Manoncourt 自身の言葉：「**pour les 1945 que je n'avais pas vinifiés, j'ai dû faire leur mise en bouteilles. M'apercevant que suivant l'âge des barriques, il y avait quelques différences, j'en ai mis de côté certaines et j'en ai fait un second vin `« La Grange Neuve de Figeac »`.**」 | 📄 **`Le Parcours d'une vie`**／✅ **公式年表 2013 年の項** |
| **1950–1955** | **品種ごとの単独瓶詰め実験（merlot / malbec / cabernet sauvignon / cabernet franc を各 30 本、10 年後に比較試飲）。その結果 malbec を外しカベルネ・ソーヴィニヨンを増やす現在の encépagement を選んだ。** | 📄 **`Le Parcours d'une vie`** |
| 🔴 **1955** | 🔴 **「`Dès la création du classement de Saint-Emilion, Château-Figeac est Premier Grand Cru Classé.`」** | ✅ **公式年表**<br>⚠️ 📄 **2012 年の公式フィッシュは「`1er Grand Cru Classé depuis l'origine du classement en 1954`」と 1954 年を書く。**🏛 **CDC の歴史欄は「1954 年 10 月 7 日の décret が 4 つの appellation を階層化し、`Le premier classement eut lieu en 1955`」。**→ **1954 は法令の年、1955 は最初の classement の年。両方を記録する** |
| **1956** | **Marie-France Duboÿs de Labarre と結婚。2 人で「style Figeac」を定義する。** | ✅ **公式年表** |
| **1964–1988** | **Thierry Manoncourt が 23 年にわたり Saint-Emilion の `1er Jurat`。** | ✅ **公式年表** |
| **1967** | **Chaban-Delmas 率いる最初のボルドー訪米団に参加。以後アジア・日本を含む世界行脚。** | ✅ **公式年表** |
| 🔴 **1970** | 🔴 **「`Décision de vinifier 100% en barriques neuves et de mettre en bouteilles 100% au château.`」**<br>本人の言葉：「**dès 1970 j'ai mis tout le vin de Figeac en barriques neuves, cela veut dire à `100 %` mais pour un `temps contrôlé`. A cette époque seuls les Premiers Crus et deux autres domaines utilisaient cette méthode**」 | ✅ **公式年表**／📄 **`Le Parcours d'une vie`** |
| **1971–1972** | **1,800 m² の設備、地下の丸天井のカーヴ 6 室、ステンレス cuvier（ボルドーで 3 番目。本人いわく 1971 年時点で `Haut Brion`, `Latour`, `Figeac` の 3 蔵のみ）。** | ✅ **公式年表**／📄 **`Le Parcours d'une vie`** |
| **1973** | **Pierre Tari（Giscours）、Bruno Prats（Cos d'Estournel）と `Union des Grands Crus` を創設。** | 📄 **`Le Parcours d'une vie`**<br>⚠️ **公式年表本文は「co-créa l'Union des Grands Crus de Bordeaux」とのみ書き、年を書いていない** |
| **1988–2013** | **`comte Eric d'Aramon` と妻 `Laure`（Thierry と Marie-France の娘）が Figeac に移り 25 年務める。d'Aramon は DG、Jurade メンバー、Premiers grands crus classés 協会会長。** | ✅ **公式年表** |
| **1990** | **「Château-Figeac est l'un des premiers domaines bordelais à créer son site Internet.」** | ✅ **公式年表**（⚠️ RDAP の `.com` 登録は 1997 年） |
| **1993 / 1995** | **家族による 100 回目の収穫（1993）と Thierry Manoncourt の 50 ミレジム（1995）を、それぞれ特別ラベルで記念。** | ✅ **公式年表** |
| 🔴 **2009** | 🔴 **「`Réalisation d'une carte de la géorésistivité des sols et repérage de la vigueur des vignes par rayonnement infra-rouge.`」**<br>🔴 **公式年表が 2009 年について書いているのはこの 1 文だけである。ワインについては何も書かれていない** | ✅ **公式年表** |
| 🔴 **2010** | 🔴 **「`Disparition de Thierry Manoncourt à la veille de son 65ème millésime.` Son œuvre est poursuivie et portée par son épouse, Marie-France Manoncourt et ses enfants.」**<br>🔴 **公式年表が 2010 年について書いているのもこの 1 文だけである** | ✅ **公式年表** |
| **2013** | 🔴 **①`Frédéric Faye` に DG を委任、`Jean-Valmy Nicolas` を迎える ②`Michel Rolland` が `Gilles Pauquet` の後任として œnologue conseil に ③**セカンドワインが 2012 年ミレジムから `PETIT-FIGEAC` に改名**（「sous le nom `La Grange Neuve de Figeac` jusqu'en 2011」）④歴史的区画を 5 年休ませて植え替え ⑤`Réserve de chasse et de faune sauvage`（RCFS）に指定** | ✅ **公式年表** |
| **2015** | **`ISO 14001` 認証（CIVB の SME 経由、ボルドー最初の SME）。同年から Semaine des Primeurs に毎年 1,800〜2,000 名の professionnels を迎える。**「**Le vin de Château-Figeac est `100% vendu en primeurs` aux négociants de la Place de Bordeaux, pour chaque millésime, depuis longtemps.**」 | ✅ **公式年表** |
| 🔴 **2018** | 🔴 **「`Lancement de grands travaux des chais cuviers` avec une préférence, à compétences égales, aux entreprises locales et régionales. `Label "Haute Valeur Environnementale" (HVE, niveau3)`, renouvelé chaque année. Cette démarche est axée sur la préservation de la biodiversité.」**<br>🔴 **すなわち 2018 年ヴィンテージは「工事が始まった年」であり、新 cuvier で造られてはいない** | ✅ **公式年表／2018 ヴィンテージ頁** |
| **2020** | **馬による耕作（`labour à cheval`）を一般化し畑の 50% をカバー。個別の ISO 14001 認証手続きを開始。** | ✅ **公式年表** |
| 🔴 **2021** | 🔴 **新 chai / cuvier の落成（5,000 m² 超、地下 2 層、重力式、フレンチオーク大樽 8 基＋ステンレス円錐タンク 40 基、R&D 専用 cuvier）。R&D 責任者ポストを創設。** | ✅ **公式年表／`Le Vin` 頁** |
| 🔴 **2022** | 🔴 **「`Le nouveau classement de Saint-Emilion vient d'élever Château-Figeac au rang de Premier Grand Cru Classé "A".`」** | ✅ **公式年表／公式記事／公式 PDF `Chateau-Figeac_1er-Grand-Cru-Classe-A.pdf`** |
| **2023** | **「Le millésime 2023 marque le `130-ème millésime` de la Famille Manoncourt au Château-Figeac.」** | ✅ **公式年表** |

---

## Location

| | |
|---|---|
| **Country / Region** | **France / Bordeaux（rive droite, Libournais）** |
| 🔴 **Appellation** | 🏛 🔴 **AOC / AOP `Saint-Emilion grand cru`。**🏛 **CDC 第 I 章 III：「`L'appellation d'origine contrôlée « Saint-Emilion grand cru » est réservée aux vins tranquilles rouges.`」**<br>🏛 **同 II：「`Le nom de l'appellation peut être complété par les mentions « grand cru classé » ou « premier grand cru classé »`」**<br>→ 🔴 **`Saint-Émilion Grand Cru` は**アペラシオン名**であって格ではない。格（classement）はその名に**付け加えられる mention** である。この 2 つを混ぜない** |
| 🏛 **アペラシオンの地理的範囲** | 🏛 **Gironde 県の 9 コミューン：`Saint-Christophe-des-Bardes, Saint-Emilion, Saint-Etienne-de-Lisse, Saint-Hippolyte, Saint-Laurent-des-Combes, Saint-Pey-d'Armens, Saint-Sulpice-de-Faleyrens, Vignonet` および `Libourne` の一部（Capelle 川以南 ほか）**<br>🏛 **区画域は 1938 年 11 月 16 日と 2017 年 5 月 3 日の comité national により承認** |
| 🏛 **AOC の栽培規則（抜粋）** | 🏛 **主要品種 `cabernet franc N, cabernet-sauvignon N, carmenère N, cot N (ou malbec), merlot N` ／ 補助品種 `petit verdot N`（10% 以下）**<br>🏛 **植栽密度 最低 5,500 本/ha、畝間 2 m 以下、株間 0.50 m 以上**<br>🏛 **rendement `46 hl/ha` / rendement butoir `55 hl/ha`**<br>⚠️ **これらは本調査が読めた「2023 年 2 月 7 日の comité national が採択した**修正案（PNO 版）**」の値である。**🏛 **同文書が引く homologation は `décret n° 2011-1779 du 5 décembre 2011`、`décret n° 2015-659 du 10 juin 2015`、`arrêté du 22 novembre 2017`（JORF 2017-12-01）。**🔴 **2009 / 2010 / 2018 の各収穫年に効力を持っていた CDC の版は本調査では特定していない** → Open Questions 6 |
| 🔴 **蔵の位置** | ✅ **「`Situé à l'ouest de Saint-Emilion, en bordure de Pomerol`」**（📄 2012 年公式フィッシュ）／🏛 **登記座標 `44.9128267, -0.19243893`** |
| 🔴 **面積** | ✅ 🔴 **`54 ha` 一枚地（`d'un seul tenant`）、その `全体` が Premier Grand Cru Classé の区画。**<br>✅ **うち **ブドウ `41 ha`**（2021 年公式データシート）／📄 **`40 ha`**（2012 年公式フィッシュ）<br>✅ 🔴 **`約 12 ha` を自然区域として意図的に非植栽で保存（「`près du quart de la propriété est conservé sans vignes`」）** |
| 🔴 **土壌・地形** | ✅ 🔴 **`3 croupes de graves günziennes`。**「**composées de `quartz et de silex` sur plusieurs mètres d'épaisseur et des `argiles bleues` en sous-sol**」<br>⚠️ ✅ **2021 年公式データシート（EN のみ）は数値を付す：「`3 Gunzian gravel outcrops (altitude 39m, depth. approx. 7m) flint and quartz on blue clay`」。**🔴 **この `39 m` / `約 7 m` の 2 つの数値は仏語資料には現れない。EN 側にしか無い数字である** |
| 🔴 **樹齢・植栽** | ✅ 🔴 **`275,000` 本（「`chacun des 275 000 ceps de vigne, que nous considérons individuellement`」）。平均樹齢 `35 年`。最古は `1921 年植えのメルロ`。**<br>✅ **マサル・セレクション用の「parcelle de collection」`0.65 ha`（3 品種の優良株のクローン）**<br>⚠️ **EN 頁のみ「`In recent years, 35% of the vineyard has been replanted`」と書く。仏語頁に対応する記述が無い** |
| 🔴 **生物多様性** | ✅ **12 ha の内訳：`prairies`, 池 1、`arboretum`, `bambouseraie`, `garenne`（chênes pédonculés / verts / lièges）、`3 km の haies`、Madame Manoncourt の `1001 rosiers de Bengale`。**<br>✅ 🔴 **「`Château-Figeac est la seule propriété parmi les Premiers Grands Crus Classés de Saint-Émilion à avoir conservé des espaces naturels aussi importants`」**（**造り手自身の主張であり、本書は第三者検証していない**） |
| **世界遺産** | 🏛 **CDC：「Premier paysage viticole labellisé patrimoine mondial par l'`UNESCO en 1999`」（対象は AOC「Saint-Emilion」の 5,000 ha と旧 juridiction の 8 コミューン）** |

🔴 ⚠️ **「Figeac から切り出された蔵」について。**
✅ **公式が書くのは 2 点だけである：① 1832 年に comtesse Félicité de Carle-Trajet が「grand domaine de Figeac」の
区画売却を始め、現在の propriété は旧所領の中心部にあたる ② 📄 Thierry Manoncourt 自身が
「**ce domaine qui avait donné naissance à `Cheval Blanc` (1832 – 1838)**」と書いている。**
→ 🔴 **造り手が名指ししているのは Cheval Blanc の 1 軒のみ。「いくつもの格付けシャトーが Figeac から出た」は
本書では主張しない。**

---

## Farming

🔴 **本節は「ヴィンテージごとに射程が違う」ことが結論である。3 本を同じ言葉で語れない。**

### Organic

🔴 🏛 **`Agence Bio` OpenData を SIRET 完全一致で照会した。**
```
GET https://opendata.agencebio.org/api/gouv/operateurs/?siret=38506797000017
→ {"nbTotal":0,"items":[]}
```
🏛 **同じ形で `78198529600016`（CHATEAU FIGEAC-MANONCOURT PROPRIETAIRE）、`42865286100017`、`38479668600028`
も照会。いずれも `nbTotal: 0`。**
🏛 **`recherche-entreprises.api.gouv.fr` の `complements.est_bio` も `false`、`liste_id_bio` は `null`。**
✅ **公式サイトにも `bio` / `agriculture biologique` / `Ecocert` の語は本調査で読んだ頁に一件も無い。**
→ 🔴 **有機認証は無い。2009・2010・2018 のいずれについても「オーガニック」と言ってはいけない。**
（⚠️ **名前検索は使っていない。ブリーフ通り SIRET 完全一致のみ**）

### Biodynamic

🔴 ⚠️ **本調査で読んだ公式頁・公式 PDF のいずれにも `biodynamie` / `biodynamic` / `Demeter` / `Biodyvin` の語は
一件も現れなかった。** → **ビオディナミは主張しない。**

### Sustainable —— 🔴 **ここが本蔵の環境面の実体である。年表と照合すること。**

| 年 | ✅ 造り手の記述 | 🏛 登録簿での確認 |
|---|---|---|
| 🔴 **2013** | **「`Dès 2013, les 54 hectares sont inscrits comme ''réserve de faune naturelle''`」／年表では「`Réserve de chasse et de faune sauvage (RCFS)`」** | ⚠️ **本調査では対応する公的登録簿を取得していない** |
| 🔴 **2015** | **「`Château-Figeac est certifié ISO 14001 via la démarche SME du CIVB`」（ボルドー最初の SME）** | ⚠️ **認証番号・発効日・認証機関を示す一次文書を取得できていない** |
| 🔴 **2018** | 🔴 **「`Obtention du label "Haute Valeur Environnementale" (HVE, niveau3), renouvelé chaque année.`」**（**2018 ヴィンテージ頁と年表の両方に同文**） | 🏛 🔴 **data.gouv.fr『Annuaire des exploitations certifiées HVE』（2025-06-01 時点、25,445 行）に実在：**<br>**`SCEA FAMILLE MANONCOURT; Château de Figeac; 33330; Nouvelle-Aquitaine; Gironde; SAINT-EMILION; VITICULTURE; Vente directe NON; Date de certification 10/07/2024`** |
| 🔴 **2020** | **「`Généralisation du labour à cheval. Il couvre 50% de la surface du vignoble.`」／個別 ISO 14001 手続きの開始** | — |

🔴 **OBP 3 本への当てはめ（1 本ずつ確認した）**

| OBP 行 | VT | 収穫時点で主張できる環境認証 | 判定 |
|---|---|---|---|
| **3. 2009** | **2009** | 🔴 **無し。**RCFS は 2013 年、ISO 14001 は 2015 年、HVE は 2018 年。**いずれも 2009 年収穫より後である** | 🔴 **「環境認証」を一切語らない** |
| **2. 2010** | **2010** | 🔴 **無し。同上** | 🔴 **同上** |
| **1. 2018** | **2018** | ⚠️ 🔴 **`HVE niveau 3` を「2018 年に取得」と造り手は書く。ただし**取得日を公表していない**。2018 年の収穫は `9/17〜10/12`。取得がその前か後かは不明** | ⚠️ 🔴 **「2018 年に HVE 3 を取得した蔵です」は言える。「この 2018 年のボトルは HVE です」は言えない**<br>🏛 **HVE 年鑑が持つ日付は `10/07/2024`＝現行証書の日付であって 2018 年の初回取得日ではない** |

⚠️ **`D-2026-08-05-XX` の温度差ルールどおり、認証の engagement 日が収穫より後なら、そのボトルについては
どちらの方向にも何も主張できない。2018 については「不明」で止める。**

### Other（造り手の栽培哲学）

✅ **サイト内の温度差を記録する。**📄 **2012 年の公式フィッシュは「`culture agronomique raisonnée`」
（EN 版は「environmentally-friendly integrated crop management」）と書いていた。**
✅ **2021 年の公式データシートは「`sustainable viticulture`」。**
→ 🔴 **蔵は一貫して「raisonnée / sustainable」であり、一度も「bio」を名乗っていない。**

✅ **マサル・セレクション：「`Investie en matière de sélection massale sur des vignes anciennes, l'équipe s'attache
à préserver le patrimoine génétique et l'identité de Château-Figeac.`」**
✅ **R&D：「`Depuis que la famille des Manoncourt est à Figeac, plusieurs ingénieurs agronomes s'y sont succédés…`
la propriété `finance aujourd'hui plusieurs thèses et recherches`」。**
🔴 ✅ **具体例として造り手が挙げるもの：`土壌の抵抗率を考古学の技術で計測`／`赤外線カメラによる樹勢観察`／
`ディジョン大学との terroir 研究`／`マサル・セレクション`／`農業会議所ネットワークと連携した害虫観察`／
`vime（柳の自然な結束材）への回帰`／`labour à cheval`。**
🔴 **このうち「géorésistivité の地図」と「赤外線による樹勢の把握」は、公式年表が `2009 年` の出来事として
名指ししている。2009 年のボトルについて造り手の言葉で言える唯一の内容である。**

---

## Winemaking

### ✅ 造り手の原則

✅ **区画別・区画内別の醸造：「`40 cuves tronconiques en inox dimensionnées pour des vinifications parcellaires
et intra-parcellaires`」（2021 年以降の新 cuvier）。**
✅ 🔴 **アッサンブラージュの決め方：「`Chaque parcelle doit pouvoir s'exprimer au moment du choix d'assemblage
mais aussi, chacun des 275 000 ceps de vigne, que nous considérons individuellement`」（Frédéric Faye, DG）。**
✅ 🔴 **「`Tout le monde goûte les primeurs… Et l'assemblage est présenté à la famille Manoncourt, afin de
s'assurer de la permanence de l'esprit Figeac.`」／「`Et c'est la famille, in fine, qui valide nos choix`」
（Romain Jean-Pierre, directeur technique）。**
✅ **重力式：「`Les processus de vinification et d'élevage sont gravitaires`」（2021 年以降）。**

### 🔴 ✅ OBP 3 本の技術仕様 —— **「1 本だけ完全、2 本は空白」がそのまま結論である**

| 項目 | 🔴 **2018（OBP 行 1）** | 🔴 **2010（OBP 行 2）** | 🔴 **2009（OBP 行 3）** |
|---|---|---|---|
| **公式ヴィンテージ頁** | ✅ **`/millesime/2018/` が存在** | 🔴 **`404`** | 🔴 **`404`** |
| 🔴 **セパージュ** | ✅ 🔴 **`37% Merlot / 33% Cabernet Sauvignon / 30% Cabernet franc`**（FR・EN 両版で一致） | ❓ **公表無し** | ❓ **公表無し** |
| 🔴 **収穫** | ✅ 🔴 **`du 17 septembre au 12 octobre 2018`** | ❓ **公表無し** | ❓ **公表無し** |
| **収量** | ❓ **公表無し**（蔵の平均値のみ、下記） | ❓ | ❓ |
| **アルコール / pH** | ❓ **公表無し** | ❓ | ❓ |
| 🔴 **樽・新樽率** | ⚠️ **当該年の記載は無い。**📄 **同時代の公式フィッシュは蔵の標準として「`100% barriques neuves` / `Durée de l'élevage : 15 à 18 mois` / `Cuves bois et inox`」** | ⚠️ **同左（2012 年フィッシュは 2010 年ボトルと同時代の資料）** | ⚠️ **同左** |
| **醸造設備** | 🔴 **旧 cuvier。2018 年は工事の着工年であり、新 cuvier の初ヴィンテージは 2021 年** | 🔴 **旧 cuvier** | 🔴 **旧 cuvier** |
| 🔴 **œnologue conseil** | ✅ **`Michel Rolland`**（2013 年〜） | ✅ 🔴 **`Gilles Pauquet`**（Rolland の前任） | ✅ 🔴 **`Gilles Pauquet`** |
| **DG / 技術責任者** | ✅ **DG `Frédéric Faye`（2013〜）** | ✅ **DG `Eric d'Aramon`／directeur technique `Frédéric Faye`（2010〜）** | ✅ **DG `Eric d'Aramon`／chef de culture `Frédéric Faye`（2008〜）** |

🔴 **蔵の「標準値」として造り手が公表しているもの（＝ヴィンテージ値ではない）**

| 項目 | ✅ 2021 年公式データシート | 📄 2012 年公式フィッシュ（Wayback） |
|---|---|---|
| **植栽比率** | **`Cabernet Sauvignon, Cabernet Franc and only 1/3 Merlot`** | **`35% Cabernet Sauvignon / 35% Cabernet Franc / 30% Merlot`** |
| 🔴 **平均収量** | 🔴 **`Average yield: 40hl/ha`**（🏛 **AOC の rendement は 46 hl/ha、butoir 55 hl/ha。蔵はそれより低い**） | — |
| 🔴 **élevage** | 🔴 **`100% in new oak barrels, 15 to 18 months`** | 🔴 **`100% barriques neuves` / `15 à 18 mois` / `Elevage traditionnel` / `Cuves bois et inox`** |
| **収穫** | **`Grapes harvested by hand`** | **`Vendanges manuelles`** |
| 🔴 **生産量** | 🔴 **`Approx. 120,000 bottles of Château-Figeac/year, 40,000 for Petit-Figeac`** | **`Production moyenne : 120 000 bouteilles`** |
| **œnologue conseil** | **`Michel Rolland`** | **（記載なし。`Directeur technique : Frédéric Faye` / `Maître de chais : Jean Albino`）** |

🔴 ⚠️ **`100% 新樽` の由来は 1970 年の Thierry Manoncourt の決断である。本人の言葉には条件が付く：**
「**j'ai mis tout le vin de Figeac en barriques neuves, cela veut dire à 100 % `mais pour un temps contrôlé`**」
→ **「常時 100% 新樽で 18 か月」ではない。「新樽 100%、ただし期間を管理して」である。**
⚠️ **本調査では 2009 / 2010 / 2018 の各年について、樽の内訳を造り手が述べた資料を 1 件も取得していない。**

✅ **なお、造り手が per-vintage で公表する形式は存在する（2021 年 primeurs フィッシュ）：**
**`VENDANGES`（品種ごとの収穫期間）／`ASSEMBLAGE`／`ELEVAGE`（「`100% barriques neuves de chêne français`」）／
`pH`／`ALCOOL`。**🔴 **同じ形式のフィッシュが 2018 / 2010 / 2009 について存在するかは不明。**
🔴 **Wayback CDX で `chateau-figeac.com` ドメイン全体の PDF を列挙したところ 15 件で、
そのいずれもこの 3 年のヴィンテージ・フィッシュではなかった。** → Open Questions 2

---

## Style

### ✅ 造り手自身のスタイル記述（逐語）

✅ 🔴 **「**Cru historique, il séduit par ses `merlots charmeurs`, l'élégance de ses `cabernets francs` et la
`texture minérale` de ses `cabernets sauvignons`.**」**
✅ 🔴 **「**Figeac murmure tel un ténor de son appellation en se glissant dans le verre… d'une `note de graphite`
qui donne la percussion ; l'énergie empreinte d'élégance se fait persistante… La vraie dimension des vins
apparaît avec le temps et les `accents de cèdre subtilement épicés`**」**
✅ 🔴 **「**Cet assemblage original, dominé pour 2/3 de cabernets, confère au vin à la fois `structure, finesse,
fraicheur et suavité`. Depuis le début de ce siècle le vin de Château-Figeac sait se rendre disponible dès ses
premières années avec un `toucher de bouche plus caressant` sans se départir de sa `verticalité incomparable`**」**
✅ **「**la pivoine, les fruits infusés, le graphite… Les 2/3 de cabernets sculptent littéralement la matière…
développant la `colonne vertébrale longue, tendue, vibrante`, avec des notes minérales très pures sur la finale.
Le toucher de tannin `satiné et pulpeux`… dans un style très `haute couture`… Au fil des ans le vin prend des
flaveurs de `feuille de tabac`, quelques nuances de `truffe noire`**」**
✅ **「**La fraicheur est dans l'ADN de Figeac grâce aux `sols graveleux` et aux `cabernets`. Aussi, Figeac semble
bien paré pour résister aux impacts du réchauffement climatique.**」**

### 🔴 ✅ 2018 年のヴィンテージノート（**該当 3 年のうち唯一存在する**）

✅ 🔴 **「`CHATEAU-FIGEAC 2018, symphonie fantastique.` La grandeur du millésime se trouve ici incarnée dans une
harmonie remarquable entre le `Merlot enveloppant et rond`, le `Cabernet franc frais et élégant` et le
`Cabernet Sauvignon à la texture fine et caressante`. Le CHATEAU-FIGEAC 2018 livre ici un accord parfait de ses
fameux trois cépages.」**

✅ **2018 年の気候（公式 `CLIMATOLOGIE ET CONDITIONS DE RECOLTE` の逐語要旨）:**
**初夏まで激しい雨と雷雨 ／ 4 月は平年より高温で樹が動く ／ `floraison précoce et rapide le 25 mai` ／
5 月〜7 月中旬は周辺で雹を伴う雷雨が繰り返されたが「`Figeac est épargné à chaque fois`」 ／
7 月中旬から収穫終了まで理想的な天候 ／ `véraison début août` ／
「`Les pépins, d'une belle couleur brun foncé, annoncent des tanins d'une grande finesse dès la fin du mois d'août.
Ce phénomène est rarement observé par les vignerons.`」／「`l'état sanitaire est excellent`」**

⚠️ **英語版 `/en/vintage/2018-vintage/` を突き合わせた。セパージュ（37/33/30）も収穫日（Sept 17–Oct 12）も
一致しており、本件では機械翻訳による数値のずれは発生していない。**

### 🔴 ❓ 2009 年・2010 年について造り手が書いていること

🔴 **ワインについては何も書いていない。**公式年表の当該年の記述は
**2009 =「土壌の géorésistivité 地図の作成と赤外線による樹勢の把握」**、
**2010 =「Thierry Manoncourt の逝去（65 回目のミレジムを前に）」**の 2 文のみである。
→ 🔴 **卓上でこの 2 本の「味わい」を造り手の言葉として語ることはできない。** → §Staff Notes ⚠️ ③

---

## Important Cuvées

### 🔴 まず「Saint-Émilion Grand Cru」が何なのか —— 🏛 法令で確定させる

| 問い | 🏛 実測による答え |
|---|---|
| 🔴 **`Saint-Émilion Grand Cru` は格付けか** | 🔴 **違う。アペラシオンの名である。**🏛 **CDC 第 I 章 I：「`Seuls peuvent prétendre à l'appellation d'origine contrôlée « Saint-Emilion grand cru », initialement reconnue par le décret du 7 octobre 1954, les vins répondant aux dispositions particulières fixées ci-après.`」** |
| 🔴 **では格付けはどこに書かれるのか** | 🏛 **同 II：「`Le nom de l'appellation peut être complété par les mentions « grand cru classé » ou « premier grand cru classé » pour les vins répondant aux dispositions fixées pour ces mentions dans le présent cahier des charges.`」**<br>🔴 **すなわち `premier grand cru classé` は**アペラシオン名に付加される mention**である** |
| 🔴 **「A」の法的根拠** | 🏛 **CDC 第 I 章 XII-2°-b：「`Il peut être décerné des distinctions (A et B) aux vins proposés pour la mention « premier grand cru classé » compte-tenu de leur notoriété et de leur aptitude au vieillissement.`」**<br>🔴 **条文は `A` と `B` の**両方**を定めている。「A がある／ない」ではなく「A か B か」である** |
| 🔴 **classement の有効期間** | 🏛 **同：「`Le classement susvisé est valable pour dix ans à compter de la parution de l'arrêté d'homologation.`」** |
| **1984 年以降の整理** | 🏛 **CDC 第 I 章 X：「`Depuis 1984, seules les appellations « Saint-Emilion » et « Saint-Emilion grand cru » subsistent, les « crus classés » n'appartenant qu'à cette dernière.`」** |
| ⚠️ **CDC 本文の古さ** | 🔴 ⚠️ **同じ CDC の第 X 章はいまも「`avec en tête les célèbres châteaux Ausone et Cheval-Blanc, de notoriété mondiale`」と書いている。**🏛 **しかし 2022 年の classement のリストに `Ausone` も `Cheval Blanc` も**一切現れない**。**⚠️ **その理由（辞退か否か）を述べた公式一次資料を本調査は取得していない。本書は「2022 年のリストに載っていない」という**リストそのものの事実**しか主張しない** |

### 🔴 格付けの「3 つの公式表記」—— `CDX-25` の実例

| 出典 | 逐語 |
|---|---|
| 🏛 **Légifrance『Arrêté du 15 décembre 2022』**（JORF n°0296, 2022-12-22, texte n° 40, NOR `AGRT2228032A`） | **見出し「`1) Premiers grands crus classés :`」／エントリ「`Château FIGEAC (distinction A)`」**<br>🔴 **第 2 条「`Le présent arrêté s'applique à compter de la récolte 2022.`」**<br>**第 3 条「`L'arrêté du 29 octobre 2012 … est abrogé.`」** |
| 🏛 **INAO 公式（2022-09-08 の communiqué とニュース頁）** | **「`Le comité national … a approuvé le nouveau classement qui comprend : 14 « premiers grands crus classés » dont 2 bénéficiant de la distinction A ; 71 « grands crus classés ».`」／リストは「`Château FIGEAC (distinction A)`」** |
| 🏛 **ODG（Conseil des Vins de Saint-Émilion）公式 dossier de presse** | **「`Ce classement vient consacrer 71 Grands Crus Classés et 14 Premiers Grands Crus Classés dont 2 Premiers Grands Crus Classés « A ».`」／見出しブロックは「`2 PREMIERS GRANDS CRUS CLASSÉS « A » : Château FIGEAC / Château PAVIE`」** |
| ✅ **蔵自身（公式記事と公式 PDF）** | **「`La commission du Classement des Grands Crus de Saint-Emilion 2022, sous l'égide de l'INAO, vient d'élever Château-Figeac au rang de Premier Grand Cru Classé "A".`」／「`Château-Figeac, Premier Grand Cru Classé « A » dans le classement 2022 de Saint-Emilion`」** |

🔴 **同じ 1 つの事実に対し、法令は `(distinction A)`、INAO は `bénéficiant de la distinction A`、
ODG は `Premiers Grands Crus Classés « A »`、蔵は `Premier Grand Cru Classé "A"` と書く。**
🔒 **`CDX-25` の言うとおり、この 4 つのどれかが「正しい格付け文字列」なのではない。canonical に 1 本の文字列を
持たせようとすると必ずどれかを捨てることになる。本書は決めない。**

### 🔴 OBP 3 ヴィンテージの「その年のラベルが名乗れた格」

| 収穫年 | 🏛 効力を持つ arrêté | 🏛 Figeac の記載 | 🔴 ラベルが名乗り得る格 |
|---|---|---|---|
| **2009** | 🏛 **`Arrêté du 8 novembre 1996`（「`Le présent arrêté s'applique à partir de la récolte 1996`」）** | 🏛 **「`A. - Saint-Emilion premiers grands crus classés.` / `b) Châteaux : Angélus, Beau-Séjour (Bécot), Beauséjour (Duffau-Lagarrosse), Belair, Canon, Clos Fourtet, `Figeac`, Gaffelière (la), Magdelaine, Pavie, Trottevielle.`」** | 🔴 **`premier grand cru classé`。**🔴 **`a)` 群（Ausone / Cheval Blanc）ではない** |
| **2010** | 🏛 **同上** | 🏛 **同上** | 🔴 **同上** |
| **2018** | 🏛 **`Arrêté du 29 octobre 2012`（「`Le présent arrêté s'applique à compter de la récolte 2012`」）** | 🏛 **premiers grands crus classés に「`Château Figeac`」。distinction の表記なし**（同 arrêté で distinction A を得たのは `Angélus` / `Ausone` / `Cheval Blanc` / `Pavie`） | 🔴 **`premier grand cru classé`。A ではない** |
| **（2022〜）** | 🏛 **`Arrêté du 15 décembre 2022`** | 🏛 **「`Château FIGEAC (distinction A)`」** | **`premier grand cru classé` + `distinction A`** |

⚠️ 🔴 **1996 年 arrêté の `A` / `B` は「格の A・B」ではなく、リストの節番号（`A.` = premiers grands crus classés、
`B.` = grands crus classés）である。世上「A」「B」と呼ばれるのはその中の `a)` と `b)` である。
現行 CDC はこれを「`distinctions (A et B)`」と書く。同じ文字が別のものを指す。ここを混ぜない。**
⚠️ **2009・2010 の 2 収穫年に 1996 年 classement が実際に効力を持ち続けていたか（2006 年 classement の
司法による取消しと、その後の立法措置の経緯）は、本調査では一次資料で追い切れていない。** → Open Questions 5

### 🔴 ✅ ラベル実読（**造り手が自社ドメインで配信する見本ボトル画像**）

| ボトル | 🔴 表ラベルの逐語 |
|---|---|
| 🔴 **`Château-Figeac`（ヴィンテージ欄が空白の見本。`/wp-content/uploads/2021/02/Figeac-Neutre.png`、2021 年 2 月アップロード＝**2022 年の昇格より前**）** | 🔴 **`CHATEAU - FIGEAC` ／ `PREMIER GRAND CRU CLASSÉ` ／ `St ÉMILION` ／ （空白のヴィンテージ枠） ／ `Thierry Manoncourt` の署名 ／ 蝋印の紋章 ／ ボトル番号 `N° 058815`**<br>🔴 **`A` の文字は無い。`GRAND CRU`（アペラシオンの語）も無い。表ラベルが名乗るのは `St ÉMILION` と `PREMIER GRAND CRU CLASSÉ` の 2 行である** |
| 🔴 **`PETIT-FIGEAC 2017`（`/wp-content/uploads/2020/11/PETIT-FIGEAC-2017.png`）** | 🔴 **`FAMILLE MANONCOURT` ／ 蝋印の紋章 ／ `PETIT-FIGEAC` ／ `2017`**<br>🔴 **`CHÂTEAU` の語も `FIGEAC` 単独の語も `SAINT-ÉMILION` の語も表ラベルに無い。ブランド名は `PETIT-FIGEAC` の 1 語である** |

⚠️ **上記 2 枚はいずれも造り手の公表画像であって、2018 / 2010 / 2009 の実ボトルではない。
特に `Figeac-Neutre` はヴィンテージ欄が空白の見本であり、各年の実際の刷りを保証しない。**

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 3 行。3 行とも `match_state = unresolved` / `confidence 0.0`**）

🔍 **3 行はいずれも `source_section = "FRANCE | RED > BORDEAUX"`、`source_producer_raw = "Figeac"`、
`source_wine_raw = "Saint-Émilion Grand Cru"`。**
🔍 **`_parts` は 3 行とも `label: null` / `appellation: "saint emilion"` / `appellation_display: "Saint-Émilion"` /
`printed_rest: "Saint-Émilion Grand Cru"` / `varietal: null` / `rank: "Grand Cru"` / `_collision_risk: "LOW"`。**
🔍 **`producer_state` / `cuvee_state` / `vintage_state` は 3 行とも `unresolved`。evidence は 3 行とも
「`canonical 384 生産者に一致・別名・近似いずれも無し: 'Figeac'`」の 1 行のみ。**

| # | `source_row_id` | VT | 価格 | 🔴 **本書の判定** |
|---|---|---|---|---|
| **1** | **`obp-beverage-2026-08:e2f3761f88`** | **2018** | **$1,220** | 🔴 **行から一意に決まらない。**同一 AOC・同一年に `Château-Figeac 2018` と `Petit-Figeac 2018` が併存する |
| **2** | **`obp-beverage-2026-08:5148c37c64`** | **2010** | **$1,380** | 🔴 **同じく決まらない。**ただし取り違え先の名は `Petit-Figeac` ではなく **`La Grange Neuve de Figeac`** である |
| **3** | **`obp-beverage-2026-08:8cde6f49a2`** | **2009** | **$1,320** | 🔴 **同じく決まらない。**取り違え先は **`La Grange Neuve de Figeac`** |

#### 🔴 「bare `Saint-Émilion Grand Cru` が何を指すか」—— **本件では確定できない**

| 問い | 実測による答え |
|---|---|
| 🔴 **メニューの `Saint-Émilion Grand Cru` はキュヴェ名か** | 🔴 **違う。🏛 AOC の名称そのものである。**🔴 **Bordeaux セクション 60 行すべてで `_parts.label` が `null` であり、これは 1 行の欠陥ではなくセクション全体の構造である**（Batch 12 で報告済みの形） |
| 🔴 **grand vin か second vin か** | 🔴 **メニューのデータだけでは決まらない。**<br>✅ **造り手：「`Depuis le millésime 1945 Château-Figeac produit un second vin, crée par Thierry Manoncourt… Rebaptisé PETIT-FIGEAC à partir du millésime 2012 il est, depuis toujours, uniquement élaboré à partir de raisins récoltés au domaine de Château-Figeac.`」**<br>✅ **年表：「`Depuis 1945 Château-Figeac est un des premiers à produire un second vin… (sous le nom La Grange Neuve de Figeac jusqu'en 2011)`」**<br>🔴 **second vin も同じ 🏛 AOC Saint-Emilion grand cru である。したがってメニューの 3 語では区別できない** |
| 🔴 **状況証拠は何を示すか** | ⚠️ 🔴 **価格帯（$1,220 / $1,380 / $1,320）と、✅ 生産量の比（grand vin 約 120,000 本 / Petit-Figeac 約 40,000 本）と、🔍 producer heading が `Figeac` であって `Petit-Figeac` でないことは、いずれも grand vin を指す方向に働く。**<br>🔴 ⚠️ **しかしこれらはすべて状況証拠であり、ラベル証拠ではない。`3f-10`（パターンの存在は個々の行の証拠ではない）に従い、本書は確定させない** |
| 🔒 **本書の処理** | 🔒 🔴 **3 行とも「未解決」のまま Open Questions 1（実ボトル案件）に送る。grand vin に黙って寄せない。**<br>🔴 **これは Batch 12 で見つかった pipeline 欠陥（キュヴェ名なしを検知した後に matcher が grand vin を提案する）と同型の状況であり、本書はその轍を踏まない** |
| 🔍 **`Petit-Figeac` / `La Grange Neuve` は intake に現れるか** | 🔴 **現れない。**🔍 **OBP 704 行の全文（正規化・非正規化の両方を含む JSON 全体）を走査し、`petit-figeac` `petit figeac` `grange neuve` `la grange neuve` はいずれも **0 件**。文字列 `figeac` を含むのは本件の 3 行のみ。**<br>🔴 **Batch 12 の「セカンドワイン名 13 種が 704 行・2 レイヤーで 0 ヒット」がそのまま再現した** |

### ✅ 生産者の現行ラインナップ（**canonical には 1 件も無い**）

| # | ✅ 公式のワイン名 | 🏛 AOC | ✅ 公式の位置づけ | OBP |
|---|---|---|---|---|
| **1** | 🔴 **`Château-Figeac`** | 🏛 **Saint-Emilion grand cru** | **le grand vin。約 120,000 本/年** | 🔴 **OBP 3 行の最有力対応（ただし未確定）** |
| **2** | 🔴 **`Petit-Figeac`**（2012 年ミレジム〜） | 🏛 **Saint-Emilion grand cru** | ✅ **「`Plus léger et moins ample que son grand frère… Petit-Figeac n'est pas un vin par défaut, il offre une parfaite introduction à l'esprit de la propriété.`」約 40,000 本/年** | — |
| **3** | 🔴 **`La Grange Neuve de Figeac`**（1945〜2011 年ミレジム） | ⚠️ **公式は AOC を明記していない** | ✅ **同じセカンドワインの旧名。1951 年は収穫全量をこの名で出したと Thierry Manoncourt 本人が書いている** | — |

🔴 **公式サイトには EC も価格表も無く、「`Le vin de Château-Figeac est 100% vendu en primeurs aux négociants de
la Place de Bordeaux`」と書かれている。蔵出し価格は公表されていない。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① サン=テミリオンで「地質の例外」と呼ばれる蔵。ボルドー右岸なのにカベルネが主役。**
「**サン=テミリオンの西の端、ポムロールとの境にある 54 ヘクタールの一枚地**です。
**造り手自身が『このアペラシオンの地質的な例外』と書いています。石灰岩ではなく、
`3 つの砂利の丘（croupes de graves günziennes）`——石英と燧石が数メートル積もり、その下が青粘土。**
だから右岸では珍しく**カベルネ・ソーヴィニヨンとカベルネ・フランが植栽の 7 割**を占めます。
**1892 年から同じマノンクール家のもの**で、いまの姿は**1947 年に入ったティエリー・マノンクール**が
60 ミレジム以上かけて作りました。**畑には 27 万 5 千本の樹があり、最古は 1921 年植えのメルロ、
平均樹齢 35 年。54 ヘクタールのうち 12 ヘクタールは意図的に植えず、
牧草地・池・アルボレータム・竹林・3 km の生垣として残しています。**」

**② 格付けは 2022 年に「A」に上がった。ただし今日の 3 本はどれもそれより前の酒である。**
「🔴 **2022 年 9 月、INAO のもとで行われた新しいサン=テミリオンの格付けで、
Château-Figeac は `Premier Grand Cru Classé « A »` に上がりました。A は 2 軒だけです。**
🔴 ⚠️ **ただし、この格付けを承認した法令（2022 年 12 月 15 日の arrêté）は
『**2022 年の収穫から適用する**』と明記しています。今日の 3 本は 2018・2010・2009 ですから、
**このボトルのラベルに『A』は載っていません**。
**2018 年は 2012 年の格付けで『premier grand cru classé』、2009 年と 2010 年は 1996 年の格付けで
同じく『premier grand cru classé』です。**」

**③ メニューの `Saint-Émilion Grand Cru` はワインの名前ではない。アペラシオンの名である。**
「🔴 **`Saint-Émilion Grand Cru` は**産地の呼称**です。格付けではありません。
**格付けは、その呼称に『grand cru classé』『premier grand cru classé』という語を**足す**形で表示されます。**
🔴 **実際、Château-Figeac の表ラベルに刷られているのは `CHATEAU-FIGEAC` / `PREMIER GRAND CRU CLASSÉ` /
`St ÉMILION` の 3 行で、『Grand Cru』というアペラシオンの綴りはそこにありません。**」

### 追加で使える一手（**すべて公式一次資料**）

- 🔴 **2018 年だけは年の話ができる**：「**造り手が『**交響曲**』と呼んだ年です。
  セパージュは **メルロ 37%・カベルネ・ソーヴィニヨン 33%・カベルネ・フラン 30%**、
  収穫は **9 月 17 日から 10 月 12 日**。
  初夏まで激しい雨が続き、**5 月から 7 月中旬まで周囲で何度も雹を伴う雷雨があったが Figeac は毎回免れた**と
  造り手が書いています。7 月中旬から収穫終了まで理想的な天候。
  **8 月末には種が濃い茶色になっていて、『これは栽培者がめったに見ない現象だ』と。**」
- 🔴 **セカンドワインの名前の話**：「**この蔵は 1945 年、ボルドーで最も早い時期にセカンドワインを作った蔵の一つです。
  ティエリー・マノンクール本人が『樽の齢で差が出ることに気づいて別に取り分けた』と書いています。
  名前は `La Grange Neuve de Figeac`。**🔴 **2012 年ミレジムから `PETIT-FIGEAC` に改名しました。**
  **年産は Château-Figeac が約 12 万本、Petit-Figeac が約 4 万本です。**」
- 🔴 **ラベルの話**：「**このラベルは 1906 年ミレジムのために、ティエリー・マノンクールの叔父
  ロベール・ヴィルピーグというアグロノムが作りました。シャトーの銅版画を載せる定型を拒んで、
  手書きの名前と赤い下線、そして蝋印。造り手いわく蝋印は『信頼の保証と時間への定着』の象徴です。
  ティエリー・マノンクールの署名は、2010 年の逝去のあとも家族が残しています。**」
- 🔴 **蔵の環境の話（認証名を出さずに）**：「**54 ヘクタールのうち 12 ヘクタールを植えずに残しています。
  マダム・マノンクールの 1001 株のバラが畝の間に並び、3 km の生垣、池、竹林、樫のガレンヌがある。
  2020 年からは畑の半分を馬で耕しています。**」
- **新しい蔵**：「**2021 年に落成した 5,000 m² 超の重力式の蔵です。フレンチオークの大樽 8 基を円形に配し、
  区画別・区画内別の醸造用にステンレスの円錐タンクを 40 基。R&D 専用の cuvier まであります。
  ただし今日の 3 本はいずれもこの蔵より前の酒です。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／第三者の主張にすぎない**）

1. 🔴 ⚠️ **『Premier Grand Cru Classé A です』とこの 3 本について言わない。**
   🏛 **2022 年 12 月 15 日の arrêté 第 2 条が『**à compter de la récolte 2022**』と明記している。
   2018・2010・2009 のラベルは『premier grand cru classé』までである。
   『2022 年に A に昇格した蔵の、それ以前のヴィンテージです』という言い方に留める。**
2. 🔴 ⚠️ **『これは Château-Figeac です』と断定しない（メニューだけを根拠にする場合）。**
   🔴 **メニューが印字しているのは生産者名・アペラシオン・年号だけで、キュヴェ名が無い。
   同じアペラシオンにセカンドワイン（2018 は `Petit-Figeac`、2009・2010 は `La Grange Neuve de Figeac`）がある。
   価格と生産量から grand vin である可能性が高いが、それは状況証拠である。ボトルを見れば 1 秒で決着する。**
3. 🔴 ⚠️ **2009 年と 2010 年のワインの味わい・セパージュ・収穫日を語らない。**
   🔴 **造り手はこの 2 年のヴィンテージ頁を公開していない（`/millesime/2009/` も `/millesime/2010/` も HTTP 404）。
   公式年表がこの 2 年について書いているのは『土壌の地電気抵抗マップと赤外線による樹勢把握』（2009）と
   『ティエリー・マノンクールの逝去』（2010）だけである。**
   **2018 年のセパージュ（37/33/30）を 2009・2010 に流用しない。**
4. 🔴 ⚠️ **『植栽の 7 割がカベルネだから、このワインの 7 割がカベルネです』と言わない。**
   🔴 **7 割（または 2/3）は**畑の植栽比率**である。造り手が数字を出している唯一の該当年 2018 は
   **メルロが最大の 37%**で、カベルネ合計は 63% にとどまる。年で動く。**
5. 🔴 ⚠️ **『オーガニックです』『ビオディナミです』と言わない。**
   🏛 **Agence Bio に SIRET `38506797000017` で照会して 0 件。企業登録の `est_bio` も `false`。
   公式サイトに `bio` の語も `Demeter` の語も無い。造り手が名乗るのは `culture raisonnée` / `sustainable` である。**
6. 🔴 ⚠️ **『HVE 認証のワインです』とこの 3 本について言わない。**
   🔴 **HVE 3 の取得は造り手いわく 2018 年だが、**取得日が公表されていない**。2018 年の収穫は 9/17〜10/12 で、
   取得がその前か後か分からない。2009・2010 に至っては HVE も ISO 14001（2015）も RCFS（2013）も存在しない。
   『蔵として HVE 3 を 2018 年に取得し毎年更新している』は言える。『このボトルが HVE』は言わない。**
7. 🔴 ⚠️ **『新樽 100% で 18 か月熟成です』とこの 3 本について断定しない。**
   🔴 **`100% barriques neuves / 15 à 18 mois` は蔵の**標準値**として公式フィッシュに書かれているもので、
   各年の実測値ではない。しかもティエリー・マノンクール本人は 1970 年の決断について
   『**100%、ただし期間を管理して**（`mais pour un temps contrôlé`）』と条件を付けている。**
8. 🔴 ⚠️ **『Château La Tour Figeac』『Château Yon-Figeac』などと混ぜない。**
   🏛 **2022 年の格付けで両者は **Grands Crus Classés**（Château-Figeac とは別の格・別の法人）。
   1996 年の格付けには `Tour du Pin Figeac (la)` が 2 軒（Giraud-Belivier / Moueix）別々に載っている。
   Saint-Emilion の郵便番号 33330 だけで、名前に `figeac` を含む法人が 49 件ある。**
9. 🔴 ⚠️ **『Ausone と Cheval Blanc は 2022 年に格を外された』と言わない。**
   🔴 **本調査で確認できるのは『2022 年の公式リストに両者の名が無い』ことだけである。
   その理由を述べた公式一次資料を本書は取得していない。**
10. 🔴 ⚠️ **『Figeac から多くの格付けシャトーが生まれた』と広げて言わない。**
    ✅ **造り手が名指しで書いているのは `Cheval Blanc`（1832–1838）の 1 軒のみ（ティエリー・マノンクール本人の言葉）。
    1832 年に comtesse de Carle-Trajet が区画の売却を始めた、という事実までが公式の記述である。**
11. ⚠️ **標高 39 m・砂利層の厚さ 7 m を仏語の話として引用しない。**
    ⚠️ **この 2 つの数値は**英語版データシートにしか無い**。仏語の頁は「plusieurs mètres d'épaisseur」としか書かない。**
12. ⚠️ **『畑は 41 ヘクタール』を 2009・2010 のボトルの話として言わない。**
    📄 **同時代（2012 年）の公式フィッシュは `40 ha` と書いている。41 ha は 2021 年の数値である。**
13. ⚠️ **第三者の点数・評価を蔵の説明として使わない。**
    ⚠️ **公式年表には Global Wine Score / Liv-ex Power 100 / Wine Spectator への言及があるが、
    いずれも第三者媒体の指標であり、本書は事実の典拠として採用していない。**
14. ⚠️ **『1954 年から Premier Grand Cru Classé』と『1955 年から』を混ぜて使わない。**
    🏛 **CDC は「1954 年 10 月 7 日の décret が 4 つの appellation を階層化」「`Le premier classement eut lieu en 1955`」。
    蔵の現行サイトは 1955 年、📄 2012 年のフィッシュは 1954 年と書いている。両方が造り手の資料である。**

---

## Akio's Insight

🖋 （この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **canonical（`migration/`）も `research/canonical_conflicts/REGISTER.md` も一切変更していない。**
🔒 **以下はすべて記録であり、番号は開いていない。**

---

### 🔴 ① **gap —— 生産者そのものが canonical に存在しない（`CDX-23`）**

1. **衝突する canonical ID**: 🔴 **無い（これは衝突ではなく不在である）。**
   🔍 **928 レコードを機械走査。`producer` フィールドの distinct 値 383 個のうち、`figeac` を含むものは **0 個**。**
2. **なぜ「ヒット」に見えるか**: 🔴 ⚠️ **レコード全体を部分一致で走査すると 6 件ヒットする。
   `bordeaux-vintage-1968-guide` / `-1970-` / `-1972-` / `-1982-` / `-1983-` / `-1984-guide` の 6 件である。
   6 件とも `producer = 'Bordeaux'`、`name = 'Bordeaux 19XX Vintage Guide'`、
   `classification = 'Vintage Reference — Parker's Bordeaux'` の**ボトルではない参照表**であり、
   `Figeac` は本文（`obp_note` / `description_en`）の中に第三者評者の列挙として現れているにすぎない。**
   🔴 **`D-2026-08-05-08` の警告どおり、部分一致は本件でも誤爆した。本書は `producer` の完全一致でのみ判定している。**
   🔴 **なお該当 34 件の `bordeaux-vintage-*-guide` は 1964〜1997 年しかなく、OBP の 2009 / 2010 / 2018 に
   対応する年は 1 件も無い。**
3. **証拠**: 🔍 **intake 3 行の `proposed_canonical_producer` / `_producer_id` / `_cuvee` / `_cuvee_id` がすべて `null`。
   evidence は「canonical 384 生産者に一致・別名・近似いずれも無し: 'Figeac'」。**
   ✅ **一方、生産者側には公式サイト・公式データシート・2018 年ヴィンテージ頁・公式ボトル画像・
   🏛 格付け法令・🏛 企業登録・🏛 HVE 年鑑が揃っている。**
4. **OBP への影響**: 🔴 **$1,220 + $1,380 + $1,320 = **$3,920** 分が canonical から見えない。**
5. **推奨する解決（実行しない）**: 🔒 **`CDX-23`。純粋な gap であり `unreachable` ではない（生産者サイトは健在で情報も豊富）。**
6. **Confidence**: 🔴 **High**

---

### 🔴 ② **Batch 12 の Bordeaux 所見の再現 —— セクション全体で `_parts.label` が `null`**

🔍 **`FRANCE | RED > BORDEAUX` セクションは 60 行あり、`_parts.label` が `null` なのは **60 行中 60 行**である。**
🔴 **これは 1 行の欠陥ではなく、メニューが Bordeaux ではキュヴェ名の位置にアペラシオンを刷るという構造である。**
🔴 **本生産者の 3 行はその教科書的な事例であり、しかも**同一 AOC のセカンドワインが実在する**ため、
`label: null` が実害（別のワインを語る）に直結する。**
🔒 **既知の族として 1 行で記録し、深追いしない。**

---

### ⚠️ ③ **既存の族に該当するもの（新しい番号は開かない）**

- ⚠️ 🔴 **パーサがアペラシオン名の一部を「格」に変えている。**
  🔍 **`_parts.rank = "Grand Cru"`。しかしこの語は 🏛 AOC 名『Saint-Emilion **grand cru**』の一部であって、
  classement の mention（`grand cru classé` / `premier grand cru classé`）ではない。**
  🔍 **Bordeaux 60 行のうち `rank` が立っているのは 5 行だけで、その 5 行は Figeac 3 行と Cheval Blanc 2 行、
  すなわち `Saint-Émilion Grand Cru` と印字された行のみである。**
  🔴 **`CDX-15`（カテゴリー語をキュヴェ名にする）の親戚であり、方向が逆（アペラシオン語を格にする）。**
- ⚠️ 🔴 **同一行内の矛盾。**🔍 **`cuvee_state: "unresolved"` かつ `_parts.label: null` でありながら、
  `normalized_cuvee` には `"Saint-Émilion"`（＝アペラシオン）が入っている。
  「キュヴェは不明」と「キュヴェはこれ」が同じレコードに同居している。**（`CDX-2` と同型。1 行で記録）
- ⚠️ **intake の evidence は「canonical **384** 生産者」と書くが、本調査が 928 レコードから数えた
  distinct `producer` は **383** である。1 件の差。スナップショットの違いか数え方の違いか、本書は判定しない。**
- ⚠️ **`CDX-25`** —— **格付け文字列に「正しい 1 つ」は存在しない。本件では 🏛 法令 `(distinction A)` /
  🏛 INAO `bénéficiant de la distinction A` / 🏛 ODG `Premiers Grands Crus Classés « A »` /
  ✅ 蔵 `Premier Grand Cru Classé "A"` の 4 通りが並立する。さらに**同じ蔵でもヴィンテージによって
  名乗れる格が違う**（2009/2010 と 2018 と 2022 以降で 3 段階）。
  → 🔴 **格付けを生産者属性として静的に持つ設計そのものが本件では成立しない。`cru × 収穫年` の粒度が要る。**
  🔒 **設計判断であり本書では決めない。**
- ⚠️ **`CDX-23`** —— **本件 3 行は純粋な gap。`unreachable` ではない。**
- ⚠️ 🔴 **`D-2026-08-05-08`（名前の部分一致）** —— **本生産者は特に危険である。
  🏛 1996 年 classement の grands crus classés に `Tour du Pin Figeac (la)` 2 軒・`Tour Figeac (la)`・`Yon-Figeac`、
  🏛 2022 年 classement に `Château LA TOUR FIGEAC`・`Château YON-FIGEAC`、
  🏛 企業登録では 33330 だけで `figeac` を含む法人が 49 件。
  canonical 側でも `Figeac` の部分一致は 6 件全部が誤爆だった。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY / `D-2026-08-05-09`**）

🔴 **本ブリーフは候補ドメインを名指ししていない。以下は本調査が自力で特定し、検証した結果である。**

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の運営者名** | ✅ 🔴 **合格。**`https://www.chateau-figeac.com/mentions-legales/` に「`Le site www.chateau-figeac.com est édité par la SCEA Famille Manoncourt.` `Numéro RCS : 385 067 970` / `Numéro SIRET : 38506797000017` / `Numéro TVA : FR76385067970` / `Siège social : CHATEAU de FIGEAC 33330 Saint-Emilion FRANCE` / `Directeur de la publication : Frédéric FAYE`」 |
| **(b) 公的登録簿との突合** | ✅ 🏛 🔴 **合格（本ドシエで最も強い検証）。**🏛 `recherche-entreprises.api.gouv.fr` で `SIREN 385067970` / `SIRET 38506797000017` / `NAF 01.21Z`（culture de la vigne）/ `SCEA FAMILLE MANONCOURT` / 本店 `CHATEAU FIGEAC 3572 ROUTE DE LIBOURNE 33330 SAINT-EMILION` / `état A`。**サイト記載の RCS・SIRET・TVA・所在がすべて一致する。**<br>🏛 **さらに data.gouv.fr の HVE 年鑑にも `SCEA FAMILLE MANONCOURT / Château de Figeac / 33330 SAINT-EMILION` として実在** |
| **(c) 格付け機関側からの照合** | ✅ 🏛 🔴 **合格。**🏛 **INAO の 2022 年 classement 公式リストと 🏛 Légifrance の arrêté に `Château FIGEAC` が実在し、蔵の自己申告と一致する** |
| **(d) 商業・法務フッターの整合** | ✅ **合格。**`Conditions générales d'utilisation` / `Mentions Légales` / `Politique de confidentialité` / `Contact` が全頁末尾に揃い、フランスの酒類広告表示（`L'abus d'alcool est dangereux pour la santé`）も全頁にある。FR / EN の 2 言語構成で、EN 側にも `Legal Notice` / `Privacy and Cookie Policy` が対応 |
| **(e) ドメイン登録** | 🏛 **Verisign RDAP：`chateau-figeac.com` は `1997-05-22` 登録、`2027-05-23` まで、registrar `OVH sas`、NS は OVH。**⚠️ **登録者情報は RDAP では非公開** |
| **年齢ゲート** | ✅ **無し。**Cookie バナー（「J'accepte」）のみで、静的取得は一切妨げられなかった |
| **bot 検出の兆候** | **`www.chateau-figeac.com` 側は無し。**⚠️ **Légifrance 側は `curl` に対し HTTP `403` を返した** |

🔴 **本調査で `NOT_THE_PRODUCER_*` として退けたサイトは無い。**
（**WebSearch は URL 候補の発見にのみ用い、検索結果の要約文は事実として一切採用していない。**
**Wikipedia は検索結果に出現したが、規約どおり開いておらず、参照もしていない。**
**merchant / auction / critic / importer のサイトは 1 件も開いていない。**）

### 一次資料（**`www.chateau-figeac.com` および同ドメイン配信の公式 PDF・公式画像**）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt` → `sitemap.xml`** | **子サイトマップ 6 本（post / page / article / millesime / category / author）。WordPress + Yoast SEO 構成** |
| 🔴 **`millesime-sitemap.xml`（26 URL）** | 🔴 **公開ヴィンテージ頁は FR / EN 対で 12 年分のみ：`1949 / 1964 / 1971 / 1995 / 2013 / 2015 / 2018 / 2019 / 2020 / 2021 / 2022 / 2023`。**🔴 **2009 と 2010 は存在しない（4 通りの URL パターンすべてが実 `404`）** |
| **`page-sitemap.xml`（26 URL）/ `article-sitemap.xml`（88 URL）** | **サイト全体の構成を機械的に確定** |
| 🔴 **`/millesime/2018/`（＋ `/en/vintage/2018-vintage/`）** | 🔴 **OBP 行 1。**`37% Merlot / 33% Cabernet Sauvignon / 30% Cabernet franc`・収穫 `17 septembre – 12 octobre 2018`・気候記述全文・**「Obtention du label HVE niveau 3, renouvelé chaque année」**。**FR / EN で数値の食い違いなし** |
| 🔴 **`/le-vin/`（＋ `/en/the-wine/`）** | 🔴 **本ドシエの中核の 1 つ。**スタイル記述の全文、**`Petit-Figeac` の定義と 2012 年改名**、`275 000 ceps`、Frédéric Faye と Romain Jean-Pierre と Blandine de Brier Manoncourt の引用、2021 年の新 chai の仕様、`Fiche d'identité` へのリンク |
| 🔴 **`/la-terre-chateau-figeac/`（＋ `/en/the-place/`）** | 🔴 **`54 ha` 一枚地・全体が Premier Grand Cru Classé・`12 ha` の自然区域・`3 croupes de graves günziennes`（quartz + silex / argiles bleues）・`0.65 ha` の parcelle de collection・平均樹齢 35 年・最古 1921 年・2013 réserve de faune・2015 ISO 14001・HVE 3** |
| 🔴 **`/les-batisseurs/`** | 🔴 **本ドシエの中核の 1 つ。**年表 28 項目（II 世紀〜2023 年）、現体制の役職と氏名、**2013 年の項に `Michel Rolland` が `Gilles Pauquet` を継いだこと・セカンドワインの改名（`La Grange Neuve de Figeac` → `PETIT-FIGEAC`）**、1970 年の「100% 新樽・100% 自社瓶詰め」決定、1955 年の初格付け |
| 🔴 **`/mentions-legales/`** | 🏛 **法人名・RCS・SIRET・TVA・本店・電話・FAX・Directeur de la publication** |
| 🔴 **`/sur-mesure/authentification-des-vins/`** | 🔴 **実ボトル案件に直結。**「`Toutes les bouteilles de Château-Figeac étiquetées à partir de 2016 sont équipées d'un système de sécurité par code qui permet d'en vérifier l'authenticité. Ce système vient s'ajouter aux nombreuses mesures que nous avons prises depuis le millésime 1989 (code laser, capsules sécurisées).`」／「`SAISISSEZ LE CODE INSCRIT DANS L'ENCADRÉ DE LA CONTRE-ÉTIQUETTE`」／認証後に「`des informations complémentaires sur le millésime`」が得られる |
| 🔴 **`/article/chateau-figeac-1er-grand-cru-classe-a-au-classement-2022-…/` ＋ `/article/classement-2022-de-saint-emilion/` ＋ `/wp-content/uploads/2022/09/Chateau-Figeac_1er-Grand-Cru-Classe-A.pdf`** | 🔴 **蔵自身の格付け表記の逐語（3 経路で同一）** |
| **`/article/la-fameuse-etiquette/`** | **1906 年ミレジムのためのラベル創作、`Robert Villepigue`** |
| 🔴 **`/wp-content/uploads/2021/03/CHATEAU-FIGEAC-Datasheet-March-2021.pdf`（EN）** | 🔴 **公式データシート。**54 ha / 41 ha / second wine の新旧名と期間 / 120,000 + 40,000 本 / 3 Gunzian outcrops（**altitude 39 m・depth ≈ 7 m**）/ 平均樹齢 35・最古 1921 / 275,000 vines / **average yield 40 hl/ha** / **maturing 100% new oak 15–18 months** / **consultant winemaker Michel Rolland** / ISO 14001 2015・HVE 3・wildlife reserve 2013 / 100% en primeur<br>⚠️ 🔴 **仏語版 `Fiches-Identité.pdf` は `/le-vin/` からリンクされているが実 `404`（リンク切れ）。本書は EN 版に依らざるを得なかった** |
| 🔴 **`/wp-content/uploads/2021/02/Le-Parcours-dune-vie-fr.pdf`（8 頁）** | 🔴 **Thierry Manoncourt 本人の講演抜粋。**1892 年の購入経緯 / 1947 年の着任 / 1950–55 年の品種別瓶詰め実験と malbec の排除 / **1968 年の話** / **1970 年の「100% 新樽、ただし期間を管理して」** / **1945 年の `La Grange Neuve de Figeac` の誕生と 1951 年の全量使用** / 1971 年のステンレス cuvier（ボルドーで 3 番目） / **「ce domaine qui avait donné naissance à Cheval Blanc (1832–1838)」** / 1973 年 Union des Grands Crus / 1962 年「groupe A」 |
| 🔴 **公式ボトル画像 `Figeac-Neutre.png`（2021-02）／`PETIT-FIGEAC-2017.png`（2020-11）** | 🔴 **表ラベル実読（拡大して逐語転記）。**`CHATEAU - FIGEAC / PREMIER GRAND CRU CLASSÉ / St ÉMILION / （空白の年枠）/ 署名 / N° 058815` と `FAMILLE MANONCOURT / 紋章 / PETIT-FIGEAC / 2017` |
| **`/wp-content/uploads/2022/06/2021-CHATEAU-FIGEAC-Primeurs-Fiche-Vin-FR.pdf`** | **蔵の per-vintage フィッシュの書式の実例（品種別収穫期間・assemblage・`100% barriques neuves de chêne français`・pH・アルコール）。**⚠️ **2018 / 2010 / 2009 の同種フィッシュは存在を確認できていない** |

### 🏛 公的登録簿・規制一次資料

| 資料 | 取得した情報 |
|---|---|
| 🔴 🏛 **Légifrance『Arrêté du 15 décembre 2022 portant homologation du classement des crus de l'AOC « Saint-Emilion grand cru »』**（`JORFTEXT000046772378`、JORF n°0296 du 22/12/2022 texte n° 40、NOR `AGRT2228032A`） | 🔴 **第 1〜4 条の逐語。**「`Le présent arrêté s'applique à compter de la récolte 2022.`」「`L'arrêté du 29 octobre 2012 … est abrogé.`」／リスト表記「`Château FIGEAC (distinction A)`」 |
| 🔴 🏛 **Légifrance『Arrêté du 29 octobre 2012』**（`JORFTEXT000026585161`、NOR `AGRT1234369A`、JORF 07/11/2012） | 🔴 **「`… s'applique à compter de la récolte 2012`」／`Château Figeac` は distinction 表記なしの premier grand cru classé ／ distinction A は `Angélus` `Ausone` `Cheval Blanc` `Pavie`** |
| 🔴 🏛 **Légifrance『Arrêté du 8 novembre 1996』**（`JORFTEXT000000195838`） | 🔴 **「`… s'applique à partir de la récolte 1996`」／Article 1 の見出し逐語「`A. - Saint-Emilion premiers grands crus classés.` `a) Châteaux : Ausone, Cheval Blanc.` `b) Châteaux : Angélus, … Figeac, … Trottevielle.`」「`B. - Saint-Emilion grands crus classés.`」／**B 群に `Tour du Pin Figeac (la) (Giraud-Belivier)`・`(Moueix)`・`Tour Figeac (la)`・`Yon-Figeac`** |
| 🔴 🏛 **INAO 公式ニュース＋ communiqué de presse PDF（2022-09-08）** | 🔴 **「14 « premiers grands crus classés » dont 2 bénéficiant de la distinction A ; 71 « grands crus classés »」／リスト全文（`Château FIGEAC (distinction A)`）／「Le classement … existe depuis 1955, et est révisable tous les dix ans. Le dernier classement datant de 2012 consacrait 18 « premiers grands crus classés » et 64 « grands crus classés ».」／4 基準と配点（dégustation 50%）／Bureau Veritas Certification France の関与** |
| 🔴 🏛 **INAO 『Cahier des charges de l'AOP « Saint-Emilion Grand Cru »』**（`extranet.inao.gouv.fr/fichier/CDCSaint-Emilion-Grand-cru-PNO2023.pdf`、16 頁、**Content-Type `application/pdf` を確認**） | 🔴 **第 I 章 I / II / III（アペラシオンの定義・mention の付加・赤の静止ワインに限る）、IV（9 コミューン）、V（品種）、VI（栽培・環境認証要件）、VIII（46 / 55 hl/ha）、X（歴史欄）、XII-2°-b（`distinctions (A et B)`・classement の 10 年有効）**<br>⚠️ 🔴 **これは 2023 年 2 月 7 日採択の**修正案（PNO 版）**であり、冒頭に「`Cette modification du cahier des charges ne saurait préjuger de la rédaction finale`」「修正は太字、削除は打ち消し線」と明記されている。Palmer で記録された「PNO 草案と consolidated を混ぜる罠」に該当する。同文書が引く homologation は `décret n° 2011-1779 du 5 décembre 2011` / `décret n° 2015-659 du 10 juin 2015` / `arrêté du 22 novembre 2017`** |
| 🏛 **INAO 『FAQ - Classement Saint-Emilion』PDF（13 頁、2021-06-18 版）** | **手続の一次情報。`règlement de classement` は `arrêté du 14 mai 2020`（JORF 16/05/2020）で homologué。配点は 20% notoriété / 20% caractérisation / 10% conduite / 50% dégustation。Bureau Veritas Certification が第三者機関** |
| 🏛 **ODG（Conseil des Vins de Saint-Émilion）『Classement des Crus de Saint-Émilion 2022 — dossier de presse』PDF** | 🔴 **「71 Grands Crus Classés et 14 Premiers Grands Crus Classés dont 2 Premiers Grands Crus Classés « A »」／`2 PREMIERS GRANDS CRUS CLASSÉS « A » : Château FIGEAC / Château PAVIE`／141 dossiers retirés・114 déposés・43 dégustateurs・1,343 échantillons／`Grand Cru Classé` は 2010–2019 の 10 ミレジム、`Premier Grand Cru Classé` は 2005–2019 の 15 ミレジムを提出／各ワインをミレジムごとに 12 回試飲／`Château LA TOUR FIGEAC` と `Château YON-FIGEAC` は Grands Crus Classés** |
| 🔴 🏛 **`recherche-entreprises.api.gouv.fr`** | 🔴 **`SCEA FAMILLE MANONCOURT`（SIREN 385067970 / SIRET 38506797000017 / NAF 01.21Z / 設立 1992-03-24 / 事業所 1 / `est_bio: false` / `liste_id_bio: null` / gérant `MANONCOURT (DUBOYS DE LABARRE) Thérèse Marie France` 1935 年生）**<br>🔴 **同住所の別法人（`CHATEAU FIGEAC-MANONCOURT PROPRIETAIRE` 781985296 / NAF 68.20B / 設立 1957 ほか）**<br>🔴 **`figeac` × 郵便番号 33330 の検索で 49 件** |
| 🔴 🏛 **Agence Bio OpenData（SIRET 完全一致）** | 🔴 **`38506797000017` → `{"nbTotal":0,"items":[]}`。関連 3 SIRET も同じく 0 件** |
| 🔴 🏛 **data.gouv.fr『Annuaire des exploitations certifiées HVE』（2025-06-01 時点、25,445 行）** | 🔴 **`SCEA FAMILLE MANONCOURT; Château de Figeac; 33330; Nouvelle-Aquitaine; Gironde; SAINT-EMILION; VITICULTURE; NON; 10/07/2024`**（同一ファイル内に `SAS CHÂTEAU YON FIGEAC` `SC CHÂTEAU LA TOUR FIGEAC` 等も別行で存在） |
| 🏛 **Verisign RDAP `chateau-figeac.com`** | **registration `1997-05-22` / expiration `2027-05-23` / registrar `OVH sas`** |

### 📄 生産者著作・生産者ドメイン外（**Wayback Machine の当該ドメインの過去キャプチャ**）

| 資料 | 取得した情報 |
|---|---|
| 🔴 📄 **`http://www.chateau-figeac.com/PDF/FICHE-TECHNIQUE-FIGEAC.pdf`（capture `2012-04-17`）＋ `_Eng.pdf`（capture `2012-07-11`）** | 🔴 **2009・2010 ボトルと同時代の公式フィッシュ。**`54 ha dont 40 destinés à la vigne` / `3 collines de graves güntziennes` / **`Encépagement : 35% Cabernet Sauvignon, 35% Cabernet Franc, 30% Merlot`** / `Vendanges manuelles` / `Elevage traditionnel` / `Cuves bois et inox` / **`Durée de l'élevage : 15 à 18 mois`** / **`100% barriques neuves`** / `Production moyenne : 120 000 bouteilles` / `Comte Eric d'Aramon` / `Directeur technique : Frédéric Faye` / `Maître de chais : Jean Albino` / `Propriétaires : Madame Thierry Manoncourt et ses enfants` / **`Classement : 1er Grand Cru Classé depuis l'origine du classement en 1954`** / **`culture agronomique raisonnée`** |
| 📄 **Wayback CDX（`chateau-figeac.com` ドメイン全体、2,006 URL／PDF フィルタで 15 件）** | 🔴 **旧サイトの構造を機械的に確定。**2001–2006 年版にはヴィンテージ別フィッシュ画像（`m49.jpg`〜`m99.jpg`）が存在したが **1999 年で止まっている**。2013–2020 年版は Flash / AJAX（`fr/ajax/accueil.php`）で、内容がほとんどアーカイブされていない。**したがって 2009・2010 のヴィンテージ資料はアーカイブからも回収できない** |

### 取得できなかったもの / 読めなかったもの

- 🔴 **2009 年・2010 年のヴィンテージ資料が生産者側に存在しない。**
  **`/millesime/2009/`・`/millesime/millesime-2009/`・`/millesime/2010/`・`/millesime/millesime-2010/` が
  すべて実 HTTP `404`。公式ヴィンテージ頁は 12 年分のみ。Wayback にも該当年の資料は無い。**
  → 🔴 **これは「publishing が止まっている」形ではなく「**公開ヴィンテージが意図的な抜粋**」の形である。
  蔵自身が「`Nous nous proposons, dans notre vinothèque, de vous raconter une sélection de millésimes…
  Si vous êtes curieux d'un autre millésime, interrogez-nous…`」と書いている。**
  → **remedy は archive recovery ではなく **procurement（蔵への直接照会）** である。**
- 🔴 ⚠️ **Légifrance が `curl` に対し HTTP `403` を返した。**
  **3 本の arrêté は WebFetch 経由でしか読めておらず、逐語は
  `_sources/chateau-figeac/NOTES-legifrance-verbatim.md` に退避した。**
  **⚠️ 403 は「条文が存在しない」ことの証拠ではない。**
- 🔴 **CDC の consolidated（homologué）版を取得できていない。**
  **読めたのは 2023 年 2 月 7 日採択の PNO 修正案のみ。`décret n° 2011-1779` 系の統合本文は未取得。**
  **したがって 2009 / 2010 / 2018 の各収穫年に効力を持っていた CDC の条文（特に rendement）は確定していない。**
- 🔴 **該当 3 本の実ボトル（表ラベル・裏ラベル）を 1 枚も読めていない。**
  **読めたのはヴィンテージ欄が空白の見本ラベルと Petit-Figeac 2017 の 2 枚のみ。**
- ⚠️ **公式サイト内検索（`/?s=`）が壊れている。**
  **`2009` / `2010` / `Petit-Figeac` のいずれを投げても同一の日付スタブ 1 件しか返さない。
  → 「検索で出ない＝存在しない」は本サイトでは使えない。**
- ⚠️ **仏語版 `Fiches-Identité.pdf` が実 `404`（`/le-vin/` からのリンク切れ）。**
  **本書の蔵レベル数値は英語版データシートに依っている。**
  **したがって `altitude 39 m` / `depth ≈ 7 m` / `average yield 40 hl/ha` は**英語資料のみの数値**である。**
- ⚠️ **`ISO 14001` と `Réserve de chasse et de faune sauvage` の認証番号・発効日・対象範囲を示す
  一次文書を取得していない。**
- ⚠️ **HVE 3 の初回取得日（2018 年のいつか）が公表されていない。**
  **🏛 HVE 年鑑が持つのは現行証書の日付 `10/07/2024` のみ。**
- ⚠️ **2022 年の classement に `Ausone` と `Cheval Blanc` の名が無い理由を述べた公式一次資料を取得していない。**
- ⚠️ **蔵出し価格が取得できない。**「100% vendu en primeurs」であり、公式に価格の記載が無い。
- ⚠️ **TTB COLA は本調査では照会していない**（本件は米国向けラベルの問いではないため）。

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical: `migration/out/export/db_wine_canonical.json`（928 レコード）を機械走査。
`producer` の distinct 値 383 個に `figeac` を含むものは 0 個。
`Château-Figeac` / `Chateau Figeac` / `Figeac` / `Petit-Figeac` のいずれでも 0 件。**
🔍 **⚠️ レコード全体の部分一致では 6 件ヒットするが、6 件とも `producer='Bordeaux'` の
`bordeaux-vintage-19XX-guide`（ボトルではない参照表）である（`D-2026-08-05-08`）。**
🔍 **OBP: `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）に 3 行。
`source_row_id` = `obp-beverage-2026-08:e2f3761f88`（2018 / $1,220）/ `:5148c37c64`（2010 / $1,380）/
`:8cde6f49a2`（2009 / $1,320）。3 行すべて `match_state = unresolved`・`confidence = 0.0`・
`producer_state = unresolved`・`source_quality_flags = []`・`reviewer_note = ""`。**
🔍 **⚠️ 同ファイルで `petit-figeac` / `petit figeac` / `grange neuve` はいずれも 0 件。
文字列 `figeac` を含む行は本件の 3 行のみである。**
🔍 **⚠️ `FRANCE | RED > BORDEAUX` は 60 行あり、`_parts.label` が `null` なのは 60 行中 60 行。**
⚠️ **本書の数値はすべて `obp_intake_normalized_20260804.json` から取ったものであり、
`research/out/t-01/mapping.json` は参照していない（両者が食い違うことは既知のため出所を明記する。`CDX-4`）。**
🔒 **canonical・`REGISTER.md`・intake のいずれも編集していない。**

---

## Confidence

```
reached_70: YES (~75%)
confidence: Medium-High
```

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | 🔴 **法人名・RCS・SIRET・TVA・本店が Mentions Légales と 🏛 企業登録で完全一致。事業所は 1 つのみ。責任者（DG / 技術責任者 / œnologue conseil / 前 DG）が氏名と就任年つきで確定し、**ヴィンテージごとに誰だったかまで割り当てられた**。同名別蔵 6 軒以上を 🏛 法令と登録簿で分離した** |
| **Overview** | **High** | **蔵の自己規定（地質の例外・カベルネ優位・家族所有）がすべて公式の言葉で取れた。**⚠️ **カベルネ比率に公式内の食い違い（70% / 2/3）があり、そこは封じた** |
| 🔴 **History** | 🔴 **High** | 🔴 **28 項目の公式年表と、造り手本人の講演 PDF の二重取り。1832 / 1892 / 1906 / 1945 / 1947 / 1955 / 1970 / 1971 / 1988 / 2009 / 2010 / 2013 / 2015 / 2018 / 2021 / 2022 がすべて公式で確定。**⚠️ **1954 / 1955 の食い違いのみ両論併記** |
| 🔴 **Location** | 🔴 **High** | 🏛 **AOC が CDC で確定（9 コミューン・品種・密度・rendement）。**🔴 **54 ha / 41 ha / 12 ha / 3 croupes / 275,000 本 / 平均樹齢 35 / 最古 1921 / 0.65 ha が公式で確定**<br>⚠️ **標高と砂利層厚は EN 資料のみ。CDC は PNO 草案版しか読めていない** |
| 🔴 **Farming** | 🔴 **High（ただし内容は「証明された不在」）** | 🔴 **🏛 Agence Bio 完全一致 0 件・`est_bio: false` で有機の不在を確定。🏛 HVE 年鑑で HVE の実在を確定。**🔴 **3 ヴィンテージすべてについて「その収穫時点で何が言えるか」を 1 本ずつ確定した（2009 / 2010 = 何も無し、2018 = 不明）**<br>⚠️ **ISO 14001 と RCFS の一次文書は未取得** |
| 🔴 **Winemaking** | ⚠️ 🔴 **Medium** | 🔴 **2018 はセパージュと収穫日が確定。**🔴 **2009 / 2010 は**造り手の資料が存在しない**（404 で確定）。樽・収量・分析値はどの年についても per-vintage の公表が無く、蔵の標準値しか無い**<br>🔴 **この Medium は調査不足ではなく、生産者の公表範囲そのものである** |
| **Style** | ⚠️ **Medium-High** | ✅ **蔵のスタイル記述は逐語で豊富。2018 のヴィンテージノートと気候記述も完備。**🔴 **2009 / 2010 については造り手のテイスティング記述が 1 行も存在しない** |
| 🔴 **Important Cuvées** | ⚠️ 🔴 **Medium-High** | 🔴 **アペラシオンと格付けの構造を 🏛 法令 4 本で完全に確定し、3 ヴィンテージそれぞれが名乗れる格を年単位で割り出した。ラベルの逐語も 2 枚読めた。セカンドワインの新旧名と適用期間も確定した**<br>🔴 ⚠️ **しかし「この 3 行が grand vin か second vin か」は**原理的にメニューからは決まらず**、実ボトルでしか決着しない。ここが 70% を大きく超えられない理由である** |
| **Canonical Conflict** | 🔴 **High** | 🔴 **gap は 928 レコードの機械走査で確定。部分一致の誤爆 6 件も内容まで実読して非ボトルと確定した** |
| **Staff Notes** | 🔴 **High** | 🔴 **14 項目。「A を遡って付ける」「grand vin と断定する」「2018 の数字を 2009/2010 に流用する」「植栽比率をアッサンブラージュとして語る」「オーガニック」「HVE のボトル」「新樽 100%/18 か月の断定」「同名別蔵との混同」「Ausone/Cheval Blanc の除外理由」の 9 つの誤りを塞いだ** |
| **総合** | ⚠️ 🔴 **Medium-High — staff-usable（70% は超える。実感としては 75% 前後）。** | 🔴 **言えること：蔵の素性・所有・責任者（年別）・テロワール・面積・樹齢・生産量・スタイル・ラベルの由来と実文言・格付けの正確な歴史（1955 / 1996 / 2012 / 2022 の 4 段階）・セカンドワインの新旧名・環境認証の年別射程・2018 年のセパージュと収穫日と気候。**<br>🔴 **言えないこと：① 3 行が grand vin か second vin か ② 2009 / 2010 のワインについて造り手の言葉が一切無い ③ 3 本の樽・収量・分析値 ④ 蔵出し価格。**<br>🔴 **①②③④ はいずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。**<br>🔴 **ただし ① は $3,920 分の行の同定そのものであり、回避では解決しない。実ボトル 1 本で全部片づく。** |

---

## Open Questions

1. 🔴 **OBP 3 本の実ボトル（実ラベル案件・最優先）。**
   🔴 **確認すべきはただ 1 点：`表ラベルのブランド名は `CHATEAU-FIGEAC` か `PETIT-FIGEAC` か
   （2009・2010 なら `LA GRANGE NEUVE DE FIGEAC` か）`。**
   🔴 **メニューには生産者名・アペラシオン・年号しか無く、この 1 語がどこにも無い。
   ボトルを 1 本見るだけで 3 行すべての判定基準が決まる。**
   **ついでに確認できると良いもの：② 表ラベルの格付け表記の実文言（`PREMIER GRAND CRU CLASSÉ` のみか）
   ③ 裏ラベルの記載事項（AOC 表記・アルコール度数・瓶詰め者）
   ④ **2018 のボトルなら contre-étiquette の authentification コード**。
   🔴 ✅ **蔵は「2016 年以降にラベリングされた全ボトルにコード認証システムがあり、認証すると
   `des informations complémentaires sur le millésime` にアクセスできる」と公表している。
   すなわち 2018 のボトルは、蔵の公式ルートで millésime 情報を引き出せる可能性がある。**
2. 🔴 **2009 年・2010 年のヴィンテージ資料を蔵に直接照会する。**
   🔴 **公式ヴィンテージ頁は 12 年分の「抜粋」であり、蔵自身が
   「`Si vous êtes curieux d'un autre millésime, interrogez-nous…`」と書いている。**
   **欲しいもの：セパージュ・収穫日・収量・élevage（新樽率と月数）・アルコール・pH。**
   **これが埋まれば Winemaking と Style が Medium → High になる。**
3. 🔴 **2018 年の技術データの残り。**
   **公式頁にあるのはセパージュと収穫日だけで、収量・élevage・アルコール・pH が無い。
   2021 年の primeurs フィッシュと同じ書式の 2018 年版が存在するか。**
4. 🔴 **HVE 3 の初回取得日（2018 年の何月何日か）。**
   **2018 年の収穫は 9/17〜10/12。取得がその前なら 2018 年のボトルについて HVE を語れるが、
   後なら語れない。🏛 HVE 年鑑は現行証書の日付（`10/07/2024`）しか持たない。**
5. ⚠️ **2009 年・2010 年の収穫時に、1996 年の classement が実際に効力を持ち続けていたかの確認。**
   🏛 **1996 年 arrêté は「à partir de la récolte 1996」、2012 年 arrêté は「à compter de la récolte 2012」で、
   その間に 2006 年 classement の司法による取消しと立法措置があったことが知られている。
   本調査はその経緯を一次資料で追い切れていない。**
   🔴 **ただし結論（この 2 本のラベルに「A」は載らない）はどちらに転んでも変わらない。**
6. ⚠️ **各収穫年に効力を持っていた CDC の版と rendement。**
   **読めたのは 2023 年の PNO 修正案のみ。consolidated（homologué）本文が要る。**
7. ⚠️ **`ISO 14001` 証書と `Réserve de chasse et de faune sauvage` の指定書。**
   **番号・発効日・対象範囲が取れれば Farming が完全になる。**
8. ⚠️ **仏語版 `Fiches-Identité.pdf` のリンク切れ。**
   **`/le-vin/` からリンクされているが実 `404`。蔵に指摘する価値がある（そして仏語の正値が得られる）。**
9. ⚠️ **カベルネ比率の公式内の食い違い（`70%` と `2/3`）。**
   **同一頁の別段落にある。蔵への照会案件。**
10. 🔒 ⚠️ **canonical に載せるときの粒度。**
    🔴 **本生産者では ①キュヴェ名がヴィンテージで変わる（`La Grange Neuve de Figeac` → `Petit-Figeac`、2012 年）
    ②格付け文字列がヴィンテージで変わる（1996 群 / 2012 / 2022 の 3 段階）
    ③環境認証の射程がヴィンテージで変わる（2013 / 2015 / 2018）。**
    🔴 **すなわち `producer` に静的な `classification` を持たせる設計は本件では必ず嘘になる。
    `cru × 収穫年` の粒度が要る。**
    🔒 **設計判断であり本書では決めない。**
