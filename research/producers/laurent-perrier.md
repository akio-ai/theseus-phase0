# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 2 件だけ存在する**
> （`laurent-perrier-grand-siecle-26` / `laurent-perrier-rose`。928 件エクスポートを機械走査して実測）。
> 本書は昇格前の研究記録であり、**canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト laurent-perrier.com で確認**（一次資料）
> `🏛` **公的登録**（`recherche-entreprises.api.gouv.fr` / Agence Bio / Demeter France）
> `🔍` **THÉSEUS DB / OBP intake から機械的に導出**
> `⚠️` **出典間で食い違っている／出典が沈黙している／言ってはいけない**
> `🔴` **重要度の高い発見** ／ `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.laurent-perrier.com/`（FR 原本を採用。EN は補助）**
> 走査元: **`robots.txt` が `Sitemap: /sitemap_index.xml` を明示** → `vins` / `la-maison` / `page` /
> `post` / `guide` の 8 sitemap を取得。**`/sitemap.xml` は 404（HTML を返す soft 404 ではなく真の 404）**
> 併用: ✅ **公式フィッシュ・テクニック PDF 5 点**（`GS20 / GS24 / GS25 / GS26 / GS27`、すべて `application/pdf`）
>
> ---
>
> 🔴 **本ドシエ最大の収穫 —— `Grand Siècle` の「番号」は、canonical が構造的に表現できない識別子である。**
>
> **① 公式の正式表記は `Grand Siècle Itération Nº27` である。**
> **メニューが印字する `Grande Cuvée` という語は、公式サイト上で Grand Siècle と結びついて一度も出現しない**
> （全取得ページを機械走査。0 件）。
>
> **② canonical は No. 26 のレコードを実は持っている。だが intake は到達できない。**
> **canonical の `name` は `Grand Siècle Itération #26 Brut`、メニューの印字は `Grand Siècle Grande Cuvée No. 26`、
> 公式は `Itération Nº26`。同一の release identifier が 3 通りに綴られており、
> intake の evidence は「canonical キュヴェ 2 件に一致無し」と記録している。**
> → 🔴 **これは「レコードが無い」のではなく「release identifier の綴りが層をまたいで揃っていない」。
> 既存登録票 `V-1`（Krug `Grande Cuvée` 162–173ème Édition）と同一の形である。**
>
> **③ `Les Réserves` が「鍵が 1 本では足りない」ことを証明している。**
> **同じ Itération 番号（Nº17・Nº20）が二度商品化されている** ——
> 通常リリースと、**未デゴルジュマンのまま 16 年／20 年以上置いた magnum**。
> → 🔴 **`cuvée × vintage` でも `cuvée × itération` でも一意にならない。
> `itération × format × デゴルジュマン状態` が要る。`V-3` と `V-2` の複合。**
>
> **④ 🔴 base vintage は itération 間で重複する。**
> **Nº25 = 2008 / 2007 / 2006、Nº26 = 2012 / 2008 / 2007、Nº27 = 2015 / 2013 / 2012。**
> **2008 と 2007 は Nº25 と Nº26 の両方に、2012 は Nº26 と Nº27 の両方に入る。**
> → 🔴 **したがって「`vintage` 欄に base year を書き込んで直す」ような一括マイグレーションは、
> このクラスのデータを復元不能に破壊する。base year から itération は逆算できない。**
>
> 🔴 **第二の収穫 —— canonical の散文が、公式が言っていないことを 2 件断定している。**
> **`laurent-perrier-rose` は「セニエ法」と「マロラクティック発酵あり」を断定するが、
> 公式は一貫して `macération` としか呼ばず、マロラクティックには全ページで沈黙している。**
> → §Canonical Conflict

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Laurent-Perrier** |
| **公式表記** | ✅ **`Laurent-Perrier`**（ハイフンつき）／**`Champagne Laurent-Perrier`**／**`Maison Laurent-Perrier`** |
| 🔴 **法人（サイト所有者）** | ✅ 🏛 **`Laurent-Perrier`、Société Anonyme à Directoire et Conseil de Surveillance、資本金 22 594 271,80 €、RCS Reims `B 335 680 096`**（mentions légales の記載）<br>🏛 **国家登録で一致**: SIREN `335680096` / SIRET 本店 `33568009600021` / NAF `70.10Z`（活動 = 本社機能）/ 設立登録 1956-01-01 |
| 🔴 **醸造の事業体** | 🏛 **`CHAMPAGNE LAURENT-PERRIER`、SIREN `351306022`、NAF `11.02A`（発泡性ワインの製造）、32 Avenue de Champagne 51150 Tours-sur-Marne**。登記上の別名に **`LAURENT-PERRIER - J.LEMOINE`**<br>🏛 **ブドウ栽培の事業体**: `SCEA DES GRANDS MONTS`、SIREN `388367534`、NAF `01.21Z`（ブドウ栽培）、同一住所 |
| **所在** | ✅ 🏛 **`32 Avenue de Champagne, 51150 Tours-sur-Marne, France`**。**mentions légales と国家登録が完全一致**（登録側の表記は `DOMAINE LAURENT PIERRIER 32 AVENUE DE CHAMPAGNE`。⚠️ **登録簿側の綴りが `PIERRIER` と誤記されている**） |
| **サイト掲載責任者** | ✅ **「Le directeur de la publication est Laurent-Perrier」**（個人名は挙げていない）。ホスティングも自社 |
| 🔴 **現 Chef de Cave** | ✅ 🔴 **Olivier Vigneron（2025 年〜）。**マルヌの農家出身、生化学の学士と **DNO（Diplôme national d'œnologue）を 1997 年に首席で取得**。ボルドーの Despagne で修業 →**2000 年に De Castellane（Alain Terrier に採用され）**→ **2004 年 Laurent-Perrier**、Michel Fauconnet のもとへ |
| 🔴 **歴代 Chef de Cave** | ✅ **Edouard Leclerc（1950–）→ Alain Terrier（1983–2004）→ Michel Fauconnet（2004–、1973 年入社。Chef de Cave 兼 Directeur de Production）→ Olivier Vigneron（2025–）** |
| **経営** | ✅ **1999 年に Second Marché（パリ証券取引所）へ上場し、Directoire / Conseil de Surveillance 構造へ移行。Alexandra Pereyre と Stéphanie Meneux de Nonancourt が Directoire 入り。Directoire 議長は 2014 年より Stéphane Dalyac** |
| **次世代** | ✅ **Lucie Pereyre de Nonancourt（2019 年 9 月入社、Alexandra の長女）。世界で Grand Siècle を代表する役割** |
| **創業年** | ✅ 🔴 **1812 年。André-Michel Pierlot が Tours-sur-Marne に Vins de Champagne の négociant として定着。**<br>🔍 **canonical の `founded_year = 1812` は公式と一致する**（Taittinger の `1734` のような齟齬は無い） |
| **認証** | ✅ 🔴 **VDC（Viticulture Durable en Champagne）＋ HVE（Haute Valeur Environnementale）。2018 年 2 月取得** |
| 🏛 **有機認証** | 🏛 🔴 **無し。Agence Bio の公的 API に Laurent-Perrier 系 4 SIRET すべてで登録が 0 件**（後述） |
| **canonical id** | 🔍 **`laurent-perrier-grand-siecle-26` と `laurent-perrier-rose` の 2 件のみ** |

⚠️ **`laurent-perrier.fr`（GDPR 窓口として mentions légales が挙げるドメイン）は
`https://` で SSL 証明書が期限切れであり、取得できなかった。本書は一切依拠していない。**

---

## Overview

✅ **Tours-sur-Marne。Marne 河畔、Montagne de Reims / Côte des Blancs / Vallée de la Marne の
3 大産地の交点に位置する Grand Cru 村。1812 年、樽職人・瓶詰業者だった André-Michel Pierlot が
`les Plaisances` と `La Tour Glorieux` という区画の上に、のちに Maison Laurent-Perrier となるものを興した。**

🔴 ✅ **公式が自らのスタイルとして繰り返す語は 3 つ、それだけである ——
`fraîcheur, élégance, pureté`（フレッシュさ、エレガンス、ピュアさ）。**
✅ 「**Bernard de Nonancourt が Laurent-Perrier のスタイルを創った —— fraîcheur, élégance, pureté。
そのために彼はシャンパーニュの伝統的な慣行を使いながら、
同時に新しい技術的アプローチを起こし、刺激した。**」

🔴 ✅ **公式が自認する「3 つの savoir-faire」は明示的に 3 つだけである。**
`/fr/la-maison/notre-savoir-faire/` に「**Nos 3 savoir-faire**」として列挙 ——
**① `L'assemblage des vins de réserve`（リザーヴワインのアッサンブラージュ）
② `La macération du pinot noir`（ピノ・ノワールのマセラシオン）
③ `Le non dosé`（ノン・ドゼ）。**
🔴 **OBP に載る 4 本のうち 3 本（Grand Siècle ×2、Cuvée Rosé、Alexandra）は、
この 3 つのうち ①（Grand Siècle）と ②（Cuvée Rosé / Alexandra）に正確に対応している。**

🔴 ✅ **ステンレスは「選択」として語られている。**
「**70 年代の終わり、Laurent-Perrier はステンレスのタンクを備えることを選んだ数少ないシャンパーニュ・メゾンの一つである。
第一発酵を低温で制御することで、タンクはワインにフレッシュさを残し、その香りの複雑さを保つ。
それがメゾンのスタイル —— fraîcheur, élégance, pureté —— の開花に与っている。
Bernard de Nonancourt は、最初の温度制御されたキュヴリーを建設させることで、Laurent-Perrier への野心を示した。**」
→ ⚠️ 🔴 **ただし公式は「木樽を使わない」とはどこにも書いていない。** → §Winemaking / §Staff Notes ⚠️ ⑤

🔍 **THÉSEUS における状態は、Taittinger より一段悪い形をしている。
canonical にあるのは 2 件（Grand Siècle Itération #26 と Cuvée Rosé）で、
OBP 掲載 4 本のうち alias で当たっているのは Cuvée Rosé の 1 本だけ。
No. 26 は canonical に実在するのに、印字文字列の綴りが違うために `unresolved` になっている。**

---

## History

✅ **公式の沿革ページ（`/fr/la-maison/notre-histoire/`）は静的取得で本文が返る。**

| 年 | 出来事 ✅ |
|---|---|
| 🔴 **1812** | 🔴 **André-Michel Pierlot（元・樽職人 `tonnelier` かつ瓶詰業者 `embouteilleur`）が Tours-sur-Marne に Vins de Champagne の négociant として定着。**「**Grand Cru に格付けされ、3 つの主要産地の交点に位置するこの村の、`les Plaisances` と `La Tour Glorieux` という区画の上に、のちに Maison Laurent-Perrier となるものを興す**」 |
| **（継承）** | **息子 Alphonse Pierlot が継ぐが、子がなく、Maison を自らの Chef de Cave `Eugène Laurent` に譲る** |
| **1887** | **Eugène Laurent が早世。未亡人 `Mathilde-Emilie Perrier` が経営を握り、自らの姓を夫の姓に加えて `Veuve Laurent-Perrier` とする**<br>🔴 **これが社名の由来である。`Laurent` と `Perrier` は 2 人の人物の姓であり、地名でも創業者一人の姓でもない** |
| 🔴 **1889** | 🔴 **Mathilde-Emilie Perrier が `Grand Vin Sans Sucre` を発売。**「**自らの嗜好と英国の顧客の嗜好により適うものとして**」<br>→ 🔴 **これが今日の `Ultra Brut`（ノン・ドゼ）の系譜の起点であり、公式が「3 つの savoir-faire」の 1 つに `le non dosé` を挙げる歴史的根拠である** |
| **1925** | **Eugénie-Hortense Laurent が母を継ぐ** |
| **1939** | **Eugénie-Hortense が Domaine を売却。`Marie-Louise de Nonancourt`（未亡人・4 児の母）が取得** |
| **第二次大戦** | **Bernard de Nonancourt と兄 Maurice が占領開始とともにレジスタンスに加わる。戻ったのは Bernard だけ** |
| 🔴 **1948** | 🔴 **Bernard de Nonancourt が Président Directeur Général に。**「**当時メゾンは 20 人ほどを雇い、8 万本を販売していた**」。**「わずか 40 年で Laurent-Perrier はシャンパーニュにおける真の革新者となる」** |
| **1950** | **Edouard Leclerc が初代 Chef de Cave**（歴代の起点として公式が明示） |
| 🔴 **1950 年代** | 🔴 **Coteaux champenois（静止ワイン）で名声を得る。**「**1950 年代から Laurent-Perrier は非常に評判の高い coteaux champenois を生産し、それがメゾンに比類のない醸造と香り抽出の技術をもたらした**」→ **これが 1968 年の Cuvée Rosé を可能にした** |
| 🔴 **1959** | 🔴 **`Grand Siècle` 誕生。**「**Bernard de Nonancourt は慣例を超えることを決める。各メゾンが例外的なミレジムに主に依拠していた時代に、彼は新しいシャンパーニュの表現を構想した —— 完全な年を再創造するための、ミレジム化された補完的なリザーヴワインのアッサンブラージュ。これが Cuvée de Prestige `Grand Siècle` の誕生である**」 |
| 🔴 **1960** | 🔴 **`Vins Natures de la Champagne` のレンジを展開（1974 年に `Coteaux Champenois` と呼ばれるようになる）** |
| 🔴 **1968** | 🔴 **`Cuvée Rosé` 発売。**「**1968 年、パリは沸き立っており、Laurent-Perrier は驚くほど創造的なワインを投じて波紋を起こした —— écusson（紋章）のボトルに入った Cuvée Rosé。50 年以上前、ロゼ・シャンパーニュは流行ってなどいなかった…**」 |
| **1974** | **`Vins Natures de la Champagne` が `Coteaux Champenois` に改称** |
| 🔴 **1970 年代末** | 🔴 **ステンレス・タンクを採用した数少ないメゾンの一つに。最初の温度制御キュヴリーを建設** |
| 🔴 **1981** | 🔴 **「ロゼ・シャンパーニュがシャンパーニュで一個のカテゴリーとして現れるのは 1981 年になってからである」**（公式）→ **Cuvée Rosé はカテゴリー成立の 13 年前に出ている** |
| 🔴 **1982** | 🔴 **`Alexandra Rosé` 創出**（公式の macération ページ: 「**創出以来 10 ミレジムしか公開されていない**」） |
| **1983–2004** | **Alain Terrier が Chef de Cave。**「**アッサンブラージュの芸術を完成させ…最良の区域のブドウを選び、各ロットを別々に醸造し、アッサンブラージュを厳格に監督した。この `vinification parcellaire`（区画別醸造）がメゾンの署名となる**」 |
| **1999** | **Groupe Laurent-Perrier がパリ証券取引所 Second Marché に上場、Directoire / Conseil de Surveillance 構造へ** |
| **2004** | **Michel Fauconnet が 3 代目 Chef de Cave（1973 年入社）** |
| 🔴 **2012** | 🔴 **メゾン創業 200 周年（Bicentenaire）。**この年、**Bernard de Nonancourt が個人のリザーヴに取り置いていた「各 Itération の未デゴルジュマンの magnum 数本」が娘たち（Alexandra・Stéphanie）と Michel Fauconnet により発見され、`Les Réserves` として初公開された**（Itération Nº17、澱の上 16 年） |
| **2018 年 2 月** | 🔴 **Groupe Laurent-Perrier が VDC と HVE の認証を取得** |
| **2019 年 9 月** | **Lucie Pereyre de Nonancourt 入社** |
| **2025** | **Olivier Vigneron が Chef de Cave に** |

✅ **Bernard de Nonancourt の言葉（公式が掲げるもの）** —
「**Qualité des hommes, qualité du vin.**（人の質、ワインの質。）」
「**このワインの造り方における卓越性と特異性の探求、常により良くあろうとし、
美食の最良の伴侶であろうとする意志 —— それは一つの要求であり、その先にある一つの哲学である。**」

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| 🔴 **本拠** | ✅ 🏛 **`32 Avenue de Champagne, 51150 Tours-sur-Marne`**（mentions légales と国家登録が一致） |
| 🔴 **Tours-sur-Marne の位置づけ** | ✅ 🔴 **公式は「Grand Cru に格付けされた村」「3 つの主要産地の交点」と書く。**⚠️ **INAO の échelle des crus 上、Tours-sur-Marne は Pinot Noir について Grand Cru（100%）だが Chardonnay については 100% ではない。公式サイトはこの区別を書いていない** → §Staff Notes ⚠️ ⑧ |
| **もう一つの拠点** | ✅ **`Château de Louvois`。**公式は「**Domaine Champagne Laurent-Perrier**」と呼び、その Orangerie でオレンジを育てたことを Grand Siècle の名の由来の説明に用いている |
| 🔴 **調達の枠組み** | ✅ 🔴 **「シャンパーニュ AOC の 319 の村（うち 17 の Grand Cru と 42 の Premier Cru）の最良のものの中から、最終的な組成に入る vins clairs を選ぶ」**（公式の savoir-faire ページ） |
| 🔴 **自社畑と買いブドウ** | ✅ 🔴 **公式は「自社畑（`le vignoble propre de la Maison`）」を持つと明示し、同時に「地域の viticulteurs との、長年にわたる、時に数世代にわたるパートナーシップが不可欠である」と明示している。**⚠️ 🔴 **自社畑の面積（ヘクタール）は公式サイト上に一切書かれていない** → Open Questions 3 |

### ✅ キュヴェ別の産地構成（公式の製品ページ＋フィッシュ・テクニック）

| キュヴェ | 産地 |
|---|---|
| 🔴 **Grand Siècle Itération Nº27** | 🔴 **8 Grands Crus。Chardonnay 60% = `Le Mesnil-sur-Oger` / `Oger` / `Avize` / `Cramant`。Pinot Noir 40% = `Tours-sur-Marne` / `Ambonnay` / `Bouzy` / `Verzy`** |
| 🔴 **Grand Siècle Itération Nº26** | 🔴 **8 Grands Crus。Chardonnay 58% = `Le Mesnil-sur-Oger` / `Oger` / `Cramant` / `Avize`。Pinot Noir 42% = `Tours-sur-Marne` / `Ambonnay` / `Bouzy` / `Verzy`**（フィッシュ・テクニック `GS26-FR.pdf` ＋ 公式リリース記事）<br>⚠️ **製品ページ本文だけが別の数字を書いている** → §Winemaking の ⚠️ |
| **Grand Siècle Itération Nº25** | **9 Grands Crus。Chardonnay 60% = `Avize` / `Cramant` / `Oger` / `Le Mesnil-sur-Oger`。Pinot Noir 40% = `Ambonnay` / `Bouzy` / `Verzy` / `Tours-sur-Marne` / `Mailly`** |
| **Grand Siècle « Les Réserves » Nº20** | **8 Grands Crus。Chardonnay 54% = `Avize` / `Cramant` / `Oger` / `Le Mesnil-sur-Oger`。Pinot Noir 46% = `Ambonnay` / `Bouzy` / `Tours-sur-Marne` / `Mailly`** |
| 🔴 **Cuvée Rosé** | 🔴 **「Montagne de Reims の南部と北部を主とする、10 ほどの Crus、その多くが Grands Crus」。**公式が名指しするのは **南部 = `Ambonnay` / `Bouzy` / `Louvois` / `Tours-sur-Marne`（有名な `Côte de Bouzy` を含む）、北部 = `Verzenay` / `Verzy` / `Mailly`、および `Aÿ` / `Mareuil-sur-Aÿ`** |
| 🔴 **Alexandra Rosé Millésimé 2012** | 🔴 **100% Grands Crus。Pinot Noir = Montagne de Reims の `Ambonnay` / `Bouzy` / `Mailly` / `Verzenay`。Chardonnay = Côte des Blancs の `Avize` / `Cramant` / `Le Mesnil-sur-Oger`** |

❓ **公式に無い**: 自社畑の面積・所有区画の一覧・買いブドウの供給者名・年間生産本数。

---

## Farming

🔴 **本節は「実践 (practised)」と「認証 (certified)」を厳密に分けて読む必要がある。
Laurent-Perrier の場合、認証は実在するが、その適用範囲が公式の言葉で限定されている。**

### ✅ 認証されているもの（公式の言葉）

🔴 ✅ **`/fr/la-maison/notre-vision/` の逐語** —
「**Le Groupe Laurent-Perrier, dans le cadre de sa stratégie environnementale pour le vignoble
et sur la totalité de ses parcelles, a obtenu en février 2018 la certification
Viticulture Durable en Champagne (VDC) et la certification Haute Valeur Environnementale (HVE).**」
（**Groupe Laurent-Perrier は、畑に対する環境戦略の枠内で、かつ自らの区画の全体において、
2018 年 2 月に VDC 認証と HVE 認証を取得した。**）

| 認証 | 状態 | 範囲についての公式の限定 |
|---|---|---|
| 🔴 **VDC**（Viticulture Durable en Champagne） | ✅ **取得済み。2018 年 2 月** | 🔴 **「sur la totalité de ses parcelles」＝ *ses* = Groupe 自身の区画。**⚠️ **買いブドウの供給元区画を含むとは書いていない** |
| 🔴 **HVE**（Haute Valeur Environnementale） | ✅ **取得済み。2018 年 2 月** | 🔴 **同上。**⚠️ **公式は HVE の「レベル」（3 等）を明示していない**（Taittinger は「レベル 3」と明記していた。Laurent-Perrier は書いていない） |

✅ **公式が併記する業界文脈** —
「**1980 年代から、シャンパーニュは環境を守る解決策を実行するために動いてきた。
今日、シャンパーニュ産業は 2030 年の地平で全表面積の 100% を認証済みとすることを目標としており、
3 つの主要領域に介入している —— テロワールと景観の保全と価値化／排水・廃棄物・副産物の管理／
カーボンフットプリントの削減。**」
✅ **「Groupe は廃棄物の生産を、ワイン生産に関わるものも製品の包装に関わるものも管理し、リサイクルを促進する。
Laurent-Perrier はまた、生産拠点における水・電気・ガスの消費を最小化することに努めている。**」

### 🏛 認証されていないもの（**公的登録による証明つきの不在**）

| 登録 | 照会 | 結果 |
|---|---|---|
| 🔴 🏛 **Agence Bio**（有機の公的登録） | **`opendata.agencebio.org/api/gouv/operateurs/?siret=…` に 4 SIRET を照会**<br>`33568009600021`（Laurent-Perrier SA 本店）<br>`35130602200036`（Champagne Laurent-Perrier）<br>`38836753400020`（SCEA des Grands Monts＝栽培会社）<br>`35130602200018` | 🔴 **全件 `{"nbTotal":0,"items":[]}`。有機の登録は存在しない** |
| 🏛 **国家企業登録の `liste_id_bio`** | **SIREN `335680096` / `351306022` / `388367534` の各 établissement** | **全件 `null`** |
| 🏛 **Demeter France** | **`demeter.fr/?s=laurent-perrier`** | **検索結果エントリ 0 件**（ページの chrome のみが返る） |
| **公式サイトの語彙** | **取得した全ページを機械走査** | 🔴 **`bio` / `biologique` / `organic` / `biodynamie` / `biodynamic` / `Demeter` / `Biodyvin` / `Ecocert` の語が一つも出現しない** |

→ 🔴 **有機・ビオディナミの認証も主張も、一切存在しない。** → §Staff Notes ⚠️ ③

### ✅ 名指しされている栽培実務

- 🔴 ✅ **`vendanges en vert`（グリーンハーヴェスト）** ——
  「**Cuvée Rosé のために、メゾンの自社畑の特定の区画がピノ・ノワールの生産に適応されており、
  必要と判明した場合には vendanges en vert のような特殊な栽培方法がとられる**」
- 🔴 ✅ **収穫時の 2 段階の選果** ——「**摘み取りの時点で第一の選別が行われ、最も美しい房だけが残される。
  収穫のあと、ピノ・ノワールの房はテーブルの上で二度目の選別を受け、そのうえで除梗される**」
- ✅ **Chef de Cave 自身による成熟度の追跡** ——「**収穫時、Michel Fauconnet は選ばれた各畑のブドウの成熟の推移を
  自ら追い、摘み取りの時機について自ら合意を与える**」
- ✅ **長期の栽培パートナーシップ** ——「**時に数世代にわたる、地域の viticulteurs との長年のパートナーシップが不可欠である**」

⚠️ 🔴 **除草剤・殺虫剤・耕起・草生・被覆作物についての具体的な記述は、公式サイトに一切無い。**
**Taittinger が「2005 年以降、除草剤も殺虫剤も使わない」と明記していたのとは対照的である。**
→ §Staff Notes ⚠️ ④

---

## Winemaking

### 🔴 ハウス全体の醸造（公式 `/fr/la-maison/notre-savoir-faire/`）✅

| 項目 | 公式の記述 |
|---|---|
| 🔴 **発酵容器** | 🔴 ✅ **ステンレス（`cuves en inox`）。**「**70 年代末、Laurent-Perrier はステンレスのタンクを備えることを選んだ数少ないメゾンの一つ**」 |
| 🔴 **第一発酵** | 🔴 ✅ **低温で制御。**「**第一発酵を低温で制御することで、タンクはワインにフレッシュさを残し、香りの複雑さを保つ**」。**Bernard de Nonancourt が最初の温度制御キュヴリー（`cuverie thermo régulée`）を建設させた** |
| 🔴 **区画別醸造** | 🔴 ✅ **`vinification parcellaire` がメゾンの署名。**「**各ロットを別々に醸造する…別々に扱われることで、各畑が Chef de Cave に非常に広い香り・テロワール・スタイルのパレットを差し出す**」（Alain Terrier 時代に確立） |
| **圧搾** | ✅ **「圧搾機において最良の果汁を選ぶ」** |
| **品種** | ✅ **「シャンパーニュの 2 大品種、Chardonnay と Pinot Noir でほぼ排他的に構成する」**（⚠️ `La Cuvée` のみ Meunier を含むと公式が別途明記） |
| 🔴 **リザーヴワインの保管** | 🔴 ✅ **「リザーヴワイン専用のキュヴリーはステンレスタンクで構成される。各 Cru と各品種を別々に低温で保存し、操作を最小限にすることで、フレッシュさと純度を保ち、あらゆる酸化を避けることを可能にする」** |
| ⚠️ **木樽** | ⚠️ 🔴 **公式は「木樽を使わない」とは一度も書いていない。**`fût` / `chêne` / `barrique` / `bois` / `oak` / `barrel` / `cask` の語は取得した全ページに 0 件。**「ステンレスを選んだ」という積極的記述はあるが、「木を使わない」という否定形の記述は無い** |
| ⚠️ 🔴 **マロラクティック発酵** | ⚠️ 🔴 **公式サイトに `malolactique` / `malolactic` の語が FR・EN いずれにも 1 件も無い。フィッシュ・テクニック 5 点にも無い。**🔴 **すなわち「する」とも「しない」とも公式は一切述べていない** → §Staff Notes ⚠️ ⑤ |
| ⚠️ **ドザージュ** | ⚠️ 🔴 **Grand Siècle のフィッシュ・テクニック 2 点（`GS26-FR` / `GS27-FR`）に `dosage` の語も `g/L` の値も存在しない。**製品ページにも無い |
| ⚠️ **デゴルジュマン日** | ⚠️ 🔴 **`dégorgement` の語も日付もフィッシュ・テクニックに無い**（ただし `Les Réserves` については別 —— 後述） |

### 🔴 Grand Siècle —— 「Itération」とは何か ✅

🔴 ✅ **公式の定義（`/fr/champagnes/grand-siecle/`、フィッシュ・テクニック 5 点にも同文）**
「**シャンパーニュにおいてミレジムは一般にプレスティージュ・キュヴェの卓越性の同義と見なされるが、
Laurent-Perrier では逆に、アッサンブラージュの芸術こそが、
ただ一つの年が差し出しうるものより高い完成度に到達させうる、というのがわれわれの確信である。**」

| 項目 | 公式の記述 |
|---|---|
| 🔴 **3 原則**（フィッシュ・テクニックに `3 PRINCIPES` として明記） | 🔴 **① 3 つの例外的な年が、その固有の性格と、アッサンブラージュを「完全な年」へ収斂させる能力ゆえに選ばれる。<br>② Chardonnay を主体とし Pinot Noir で補う。シャンパーニュの 319 Crus の中から選ばれた最大 11 の Grands Crus に由来する。<br>③ 澱の上での長期熟成 —— ボトル（75 cl）で 10 年、magnum（150 cl）ではさらに数年。** |
| 🔴 **番号の正体** | 🔴 ✅ **「Depuis 1959, il n'a été possible de recréer Grand Siècle que 27 fois en bouteille et 24 fois en Magnum.」**（**1959 年以来、Grand Siècle を再創造することができたのは、ボトルで 27 回、magnum で 24 回だけである。**）<br>→ 🔴 **番号は「1959 年以来 何回目のアッサンブラージュか」という通し番号である。ヴィンテージではなく、品質の序列でもない。** |
| **命名の由来** | ✅ **「Grand Siècle」＝フランス史上最も繁栄した時期の一つ（17 世紀）の呼称。ルイ 14 世とヴェルサイユ。「自然だけでは創れないものを人間が創る能力」の象徴として、メゾンのプレスティージュ・キュヴェの名に選ばれた** |
| 🔴 **Grands Crus の母数** | ✅ **「最大 11 の Grands Crus」。**別ページでは「**17 の Grands Crus のうち最大 11**」と書かれる（`/fr/la-maison/notre-savoir-faire/assemblage-vins-reserve/`）。**シャンパーニュの Grand Cru 村は 17 なので両者は整合する** |
| **提供温度** | ✅ **10 °C 〜 12 °C**（フィッシュ・テクニック `GS26` / `GS27`） |

### 🔴 OBP 該当 2 本の公式スペック ✅

| | 🔴 **Itération Nº27**（OBP 行 1・$920） | 🔴 **Itération Nº26**（OBP 行 2・$800） |
|---|---|---|
| **base vintages** | 🔴 **2015（65%）／ 2013（25%）／ 2012（10%）** | 🔴 **2012（65%）／ 2008（25%）／ 2007（10%）** |
| **Grands Crus 数** | **8** | **8** |
| **セパージュ** | **Chardonnay 60% / Pinot Noir 40%**（製品ページ・フィッシュ・公式リリース記事の 3 者が一致） | ⚠️ 🔴 **公式内で食い違う。**<br>**「58% / 42%」= フィッシュ・テクニック `GS26-FR.pdf` ＋ 公式リリース記事（2023 年 9 月）＋ 製品ページの見出し行**<br>**「52% / 48%」= 製品ページ本文ブロックのみ**（かつ村が 11 と多い: Chardonnay に `Chouilly`、Pinot Noir に `Mailly` `Verzenay` を追加）<br>🔴 **3 対 1 で 58/42 が優勢だが、本書はどちらも断定しない** |
| **熟成** | **75 cl ボトルで澱の上 10 年** | **75 cl ボトルで澱の上 10 年** |
| **フィッシュ日付** | **`Laurent-Perrier - 11 Septembre 2025`** | **`Laurent-Perrier - 21 Juillet 2025`** |
| **リリース告知** | ✅ **`/fr/magazine/nouveautes/grand-siecle-iteration-n27/`、2026 年 1 月** | ✅ **`/fr/magazine/nouveautes/grand-siecle-iteration-n26/`、2023 年 9 月** |
| **ドザージュ / デゴルジュマン / アルコール度数** | ⚠️ **公式に一切無し** | ⚠️ **公式に一切無し** |

### 🔴 参考 —— 他の Itération（**番号が vintage でないことの証拠**）✅

| Itération | base vintages | セパージュ | Grands Crus | 熟成 | フォーマット |
|---|---|---|---|---|---|
| **Nº27** | **2015 / 2013 / 2012** | 60 / 40 | 8 | **10 年** | **75 cl** |
| **Nº26** | **2012 / 2008 / 2007** | 58 / 42 ⚠️ | 8 | **10 年** | **75 cl** |
| **Nº25** | **2008 / 2007 / 2006** | 60 / 40 | **9** | 🔴 **12 年** | **75 cl** |
| 🔴 **« Les Réserves » Nº20** | **1999（60%）/ 1997（20%）/ 1996（20%）** | **54 / 46** | 8 | 🔴 **magnum で 20 年以上** | 🔴 **150 cl のみ** |

🔴 **この表が示すこと（本ドシエの中核）:**
1. 🔴 **base vintage の集合が itération 間で重複する。**`2008` と `2007` は Nº25 と Nº26 の両方に、
   `2012` は Nº26 と Nº27 の両方に入る。**base year から itération は一意に逆算できない。**
2. 🔴 **番号は熟成年数とも単調に対応しない。**Nº25 は 12 年、Nº26 と Nº27 は 10 年。
3. 🔴 **番号だけでは製品を特定できない。**Nº20 は 150 cl の `Les Réserves` としてしか存在しない。
4. 🔴 **公式サイトが itération ページを公開しているのは 8 つだけ**
   （Nº27 / Nº26 / Nº25 / Nº24 magnum / Nº23 magnum / Nº22 magnum /
   « Les Réserves » Nº20 / « Les Réserves » Nº17）。
   **27 の itération 全部の対応表は公式に存在しない。** → Open Questions 2

### 🔴 `Les Réserves` —— デゴルジュマンが identity になる唯一の箇所 ✅

🔴 ✅ **公式の逐語（`/fr/champagnes/grand-siecle/les-reserves-iteration-20/`）**
「**澱の上での長期熟成がワインに与える影響を観察するため、Bernard de Nonancourt は、
各 Itération の未デゴルジュマンの magnum を数本、自らの個人的なリザーヴに取り置くという決断をした。
2012 年、このリザーヴが娘たち Alexandra と Stéphanie、そして Chef de Cave の Michel Fauconnet によって発見され、
同年のメゾン創業 200 周年の祝典で初めて明かされた。
`Les Réserves` と名づけられたこの Grand Siècle の表現は、Itération Nº17 に対応するもので、
澱の上で 16 年を過ごしたのちに商品化された。**」
「**メゾンの歴史で二度目として、20 年以上カーヴで熟成させた Itération Nº20 を通じて、
再び Grand Siècle « Les Réserves » を明かす喜びを得ている。**」

→ 🔴 **すなわち、同じ Itération 番号が二度商品化される。**
**通常リリースと、`Les Réserves`（未デゴルジュマンのまま長期保持された magnum）。**
🔴 **公式はデゴルジュマンの「日付」は公開しないが、
「デゴルジュマンを遅らせたこと」そのものを製品の identity として語っている。**
→ §Canonical Conflict（`V-3` / `V-2` への証拠追加）

### 🔴 Cuvée Rosé —— マセラシオン ✅

🔴 ✅ **公式は「シャンパーニュのロゼには 2 つの方法がある」と自ら定義している**
（`/fr/la-maison/notre-savoir-faire/maceration/`）——
「**Il existe deux méthodes pour produire un champagne rosé :
l'assemblage de vin blanc et de vin rouge ou la macération.**」
🔴 **そしてそのうち後者だけを自らの方法として名乗る。**
「**もう一つの、macération と呼ばれる方法は、より稀な savoir-faire である。
黒ブドウの果皮が macération のタンクの中で果汁と接触したままにされ、
香りの表現を引き出し、天然の色素にワインを染めさせる。
macération のあと果汁は流し出され、別のタンクで低温での発酵が始まる。**」

| 項目 | 公式の記述 |
|---|---|
| 🔴 **方法** | 🔴 ✅ **`macération`（果皮浸漬）。**「**1968 年以来、Laurent-Perrier はシャンパーニュにおいて非常に特殊で稀な savoir-faire を修めてきた —— la macération**」 |
| ⚠️ 🔴 **`saignée` について** | ⚠️ 🔴 **公式の本文に `saignée` の語は一度も現れない。**唯一の出現は**記事の URL スラッグ `champagne-rose-maceration-saignee-assemblage` のみ**であり、その記事の本文タイトルは「**Cuvée Rosé, un rosé de macération**」で、本文は saignée に触れない。🔴 **さらに公式の定義ページはシャンパーニュのロゼの方法を「assemblage か macération」の 2 つとしか挙げていない** → §Canonical Conflict `LP-A` |
| **セパージュ** | ✅ **Pinot Noir 100%** |
| **産地** | ✅ **Montagne de Reims の 10 ほどの Crus、その多くが Grands Crus** |
| 🔴 **工程（逐語）** | 🔴 ✅ **「収穫のあと、ピノ・ノワールの房は選別され、除梗され、macération 専用のステンレスタンク（`cuves inox réservées à la macération`）に入れられる。macération の段階はピノ・ノワールの Cru ごとに行われ、果粒から果汁を抽出する。この工程の終わりに果汁は固形物から分離され、残った果粒は圧搾される。débourbage ののち、これらの moûts はキュヴリーへ送られ、別に醸造されて発酵を始める。」** |
| ⚠️ 🔴 **マセラシオンの時間** | ⚠️ 🔴 **公式内で食い違う。**<br>**「48 à 72 heures」**= savoir-faire ページ ＋ 製品ページ ＋ 2023-02-16 の記事<br>**「48 heures」**= 2024 年 4 月の記事 `cuvee-rose-lexpression-du-pinot-noir`<br>🔴 **本書はどちらも断定しない** |
| ⚠️ 🔴 **remontage の頻度** | ⚠️ 🔴 **公式内で食い違う。**<br>**「des remontages sont réalisés deux fois par jour」**（1 日 2 回）= savoir-faire ページ<br>**「le jus extrait est remis en suspension sur le marc toutes les 8 heures」**（8 時間ごと＝1 日 3 回）= 2024 年 4 月の記事 |
| ⚠️ **マセラシオンの温度** | ⚠️ 🔴 **公式に数値が一切無い。**一般論の説明として「macération のあと**低温での**発酵が別のタンクで始まる」とあるのみ |
| 🔴 **熟成** | 🔴 ✅ **カーヴで 5 年（`un vieillissement prolongé de 5 ans en caves`）** |
| **ドザージュ / デゴルジュマン / アルコール度数** | ⚠️ **公式に一切無し。フィッシュ・テクニックも存在しない** |

### 🔴 Alexandra Rosé Millésimé 2012 ✅

| 項目 | 公式の記述 |
|---|---|
| 🔴 **公式の正式名** | 🔴 ✅ **`Alexandra Rosé Millésimé`。**サイトのナビゲーション・製品ページ URL（`/fr/champagnes/alexandra-rose-millesime/`）・sitemap のいずれもこの形。**リリース記事の見出しは `Alexandra Rosé 2012`**<br>🔴 ⚠️ **`Grand Siècle Alexandra` という形は、本調査で取得した公式ページのどこにも現れなかった。**現行サイト上、Alexandra は Grand Siècle とは**別のキュヴェとして並列**に置かれている（「Découvrez nos cuvées」の列挙で Grand Siècle と Alexandra は別項目） |
| **セパージュ** | ✅ **Pinot Noir 80% / Chardonnay 20%** |
| **産地** | ✅ **100% Grands Crus。**Pinot Noir = `Ambonnay` / `Bouzy` / `Mailly` / `Verzenay`（Montagne de Reims）、Chardonnay = `Avize` / `Cramant` / `Le Mesnil-sur-Oger`（Côte des Blancs） |
| 🔴 **醸造の要点** | 🔴 ✅ **「マセラシオンされたピノ・ノワールとシャルドネの `fermentation conjointe`（共発酵）が、例外的な香りを得ることを可能にする」**<br>🔴 ✅ **難所は「ピノ・ノワールとシャルドネが同時に完璧な成熟に達すること」** ——「**この Prestige のロゼ・シャンパーニュの製造の難しさは、Grand Cru においてこの 2 品種の香りを抽出するために、ピノ・ノワールとシャルドネが同様の成熟に達している必要がある点にある**」 |
| **熟成** | ✅ **10 年** |
| 🔴 **稀少性** | 🔴 ✅ **「1982 年の創出以来、10 ミレジムしか公開されていない」** |
| **2012 年の性格** | ✅ **「2012 年の栽培年は、冬と春の霜、雹、隠花菌類の病害で複雑であり、収量にむしろ控えめな影響を与えた。乾いて日照のあった夏がブドウの例外的な成熟を可能にし、完璧な衛生状態で収穫された」** |
| **ドザージュ / デゴルジュマン / アルコール度数** | ⚠️ **公式に一切無し。フィッシュ・テクニックも存在しない** |

---

## Style

### ✅ 公式テイスティングノート（OBP 該当 4 本すべて）

| キュヴェ | 公式ノート（逐語訳） |
|---|---|
| 🔴 **Grand Siècle Itération Nº27** | **ROBE**「**きらめく金色の色調、繊細で持続する泡。**」<br>**NEZ**「**スイカズラ、砂糖漬けレモン、ヘーゼルナッツ、フレッシュなアーモンドの香りが混ざる非常に複雑な香り。それに続いてヴィエノワズリー、蜂蜜、焙煎の調子。活気づけるような、エネルギッシュで魅惑的な香り。**」<br>**PALAIS**「**フレッシュで振動的なアタックが嗅覚の感覚を確証し、熟した果実、干し杏、砂糖漬けの柑橘、ヘーゼルナッツの香り。口中は長く調和的で、洗練されたミネラリティを持ち、まろやかなニュアンスと生命力に満ちたワイン。**」 |
| 🔴 **Grand Siècle Itération Nº26** | **ROBE**「**白金色の色調に、繊細で持続する泡。**」<br>**NEZ**「**スイカズラ、レモン、クレメンティーヌ、フレッシュバターの香りが混ざる非常に複雑な香り。それに続いてヘーゼルナッツの調子と蜂蜜の一筆。**」<br>**PALAIS**「**繊細さとフレッシュさに満ちたアタック、砂糖漬けレモンとフレッシュなヘーゼルナッツの香り。口中は絹のようでミネラル、スイカズラ、スライスアーモンド、クレメンティーヌの調子。**」 |
| 🔴 **Cuvée Rosé** | **ŒIL**「**エレガントな色調で、色は美しいフランボワーズの色合いからサーモン色のニュアンスへと自然に推移する。**」<br>**NEZ**「**並外れたフレッシュさを持つ率直な香りと、赤い果実の広いパレット —— フランボワーズ、グロゼイユ、イチゴ、ブラックチェリー。**」<br>**PALAIS**「**しなやかで丸みのあるこのワインの、率直で酸を感じさせるアタック。口中では、摘みたての赤い果実の籠に飛び込むような感覚を差し出す。**」 |
| 🔴 **Alexandra Rosé Millésimé 2012** | **ŒIL**「**非常に細かく非常に持続する泡を伴う、深いブラッドオレンジ色の色調。**」<br>**NEZ**「**赤い果実（潰したイチゴ）の調子を持つ複雑な香り。**」<br>**PALAIS**「**赤い果実の香りと、ビターオレンジのフィニッシュを持つ、豊かで温かみのあるワイン。**」 |

### ✅ 公式の食事の合わせ

| キュヴェ | 公式の指定 |
|---|---|
| **Grand Siècle Nº27 / Nº26** | ✅ **`Viandes nobles` / `Poissons nobles` / `Crustacés` / `Truffes`**<br>**Nº26 のフィッシュはさらに具体的**: 「**海と陸の組み合わせ、白身肉、高貴な魚、甲殻類 —— たとえばタイ風の手長海老のタルタルやブレス鶏**」 |
| **Cuvée Rosé** | ✅ **`Cuisine exotique` / `Poissons marinés` / `Jambon de Parme` / **チーズ: `Chaource`** / `Desserts aux fruits rouges`**<br>記事版はさらに「**マリネした魚介、シャルキュトリー、スパイスの効いた料理、赤い果実のデザート**」 |
| **Alexandra Rosé 2012** | ✅ **`Viandes nobles` / `Poissons nobles` / `Caviar`** |

✅ 🔴 **公式は「`L'accord parfait` de Christian Le Squer ***」という枠を全キュヴェに設けている** ——
**Nº27** =「**鱗つきヒメジ、ディルのブイヨン、軽くサフランを効かせたじゃがいものニョッキ**」／
**Nº26** =「**ターボのプランチャ焼き、クレソンのマセラシオンと酢漬け洋梨**」／
**Cuvée Rosé** =「**ブーダン・ノワールのクリームを加えた黒米、パッションフルーツの汁**」／
**Alexandra 2012** =「**仔羊のエピグラム、野菜の細いラヴィオリ、辛みのある緑のジュ**」。
**提供温度は Grand Siècle について 10–12 °C を公式が指定**。

### ⚠️ 第三者点数（**公式サイトが自ら掲載しているもの。THÉSEUS はこれを事実として扱わない**）

⚠️ **公式は製品ページに点数を掲載している。以下は「公式がそう掲載している」という事実の記録であり、
本書はこれを品質の根拠として用いない。**
- **Nº27**: James Suckling 99/100 ／ Wine Advocate 95+/100 ／ Jancis Robinson 18,5+/20
  （⚠️ **製品ページは `97/100` と表示するが、リリース記事は Wine Advocate を `95+/100` とする。食い違っている**）
- **Nº26**: James Suckling 100/100（`Wine of the year 2023`）／ Jancis Robinson 19,5/20 ／ Bettane+Desseauve 98/100
- **Cuvée Rosé**: 95/100 ／ 95/100 ／ 94/100（**公式ページに評者名が表示されない**）
- **Alexandra Rosé 2012**: 98/100 ／ 99/100 ／ 97/100（**同上、評者名なし**）
- 🔍 **canonical は `laurent-perrier-grand-siecle-26` に `points: 96`、`laurent-perrier-rose` に `points: 92` を持つ。
  どちらも公式が掲載するどの数字とも一致しない。** → §Canonical Conflict `LP-B`

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 `obp_intake_normalized_20260804.json` より。**全 4 本。うち 1 本のみ alias、3 本 `unresolved`**）

| # | メニュー印字 | VT | 価格 | セクション | intake | ✅ **公式での確認結果** |
|---|---|---|---|---|---|---|
| **1** | **`'Grand Siècle Grande Cuvée No. 27,' Brut`** | — (NV) | **$920** | `CHAMPAGNE \| BLENDS` | 🔍 **`unresolved`**<br>`cuvee_state=unresolved`<br>evidence:「canonical キュヴェ 2 件に一致無し」 | ✅ 🔴 **実在。公式の正式名は `Grand Siècle Itération Nº27`。**<br>🔴 **`Grande Cuvée` は誤り** —— 公式サイト上で Grand Siècle と結びついたこの語は 0 件。<br>**2015(65%)/2013(25%)/2012(10%)、Chardonnay 60% / Pinot Noir 40%、8 Grands Crus、澱上 10 年、75 cl。**<br>**リリース 2026 年 1 月＝現行。フィッシュ `GS27-FR.pdf`（2025-09-11）**<br>🔴 **canonical に No. 27 のレコードは存在しない ＝ gap** |
| **2** | **`'Grand Siècle Grande Cuvée No. 26,' Brut`** | — (NV) | **$800** | `CHAMPAGNE \| BLENDS` | 🔍 **`unresolved`**（同上） | ✅ 🔴 **実在。公式の正式名は `Grand Siècle Itération Nº26`。**<br>**2012(65%)/2008(25%)/2007(10%)、8 Grands Crus、澱上 10 年、75 cl。**<br>⚠️ **セパージュは公式内で 58/42 と 52/48 に割れる**（3 対 1 で 58/42）。<br>**リリース 2023 年 9 月。フィッシュ `GS26-FR.pdf`（2025-07-21）**<br>🔴 **canonical に `laurent-perrier-grand-siecle-26` が実在する。だが `name='Grand Siècle Itération #26 Brut'` であり、メニュー印字と綴りが違うため到達できていない** → §Canonical Conflict `V-1` |
| **3** | **`'Cuvée Rosé,' Brut`** | — (NV) | **$250** | 🔴 `CHAMPAGNE \| **ROSÉ**` | 🔍 **`alias`**（confidence 0.9）<br>→ `cuvee:laurent-perrier-cuvee-rose-brut` | ✅ 🔴 **正しく解決している。公式の正式名も `Cuvée Rosé`。**<br>🔴 **Pinot Noir 100%、Montagne de Reims の 10 ほどの Cru、`macération`（48〜72 時間）、カーヴで 5 年。1968 年発売。**<br>🔴 **⚠️ ただし canonical の散文が方法を `saignée` と断定している** → §Canonical Conflict `LP-A` |
| **4** | **`'Alexandra,' Brut`** | **2012** | **$1,255** | 🔴 `CHAMPAGNE \| **ROSÉ**` | 🔍 **`unresolved`**（同上） | ✅ 🔴 **実在。公式の正式名は `Alexandra Rosé Millésimé`（リリース記事の見出しは `Alexandra Rosé 2012`）。**<br>🔴 **公式サイト上に `Grand Siècle Alexandra` という形は現れない。Alexandra は Grand Siècle と並列の別キュヴェとして扱われている。**<br>**Pinot Noir 80% / Chardonnay 20%、100% Grands Crus、共発酵、10 年熟成。1982 年創出以来 10 ミレジムのみ**<br>🔴 **canonical に Alexandra のレコードは存在しない ＝ gap** |

### 🔴 行 1 と行 2 の価格差について（**Staff Notes で扱う核心**）

🔍 **No. 27 = $920、No. 26 = $800。同じワインの、番号違いの 2 つのリリースである。**
🔴 ✅ **番号は品質の序列ではない。ヴィンテージでもない。**
**公式の定義は「1959 年以来、Grand Siècle をボトルで再創造できたのは 27 回だけ」——
すなわち番号は「何回目のアッサンブラージュか」の通し番号である。**
🔴 **したがって「27 のほうが 26 より良い」も「27 のほうが新しいヴィンテージ」も、どちらも誤りである。**
**言えるのは「No. 27 のほうが新しいリリースで、より新しい 3 年（2015/2013/2012）から組まれている」まで。**
**熟成年数はどちらも 10 年で同じ。** → §Staff Notes 芯 ②

### ✅ 公式の全 9 キュヴェ（`/fr/champagnes/`。**canonical にあるのはこのうち 2 つだけ**）

| # | 公式キュヴェ | URL | canonical |
|---|---|---|---|
| 1 | 🔴 **Grand Siècle**（Itération 制）⭐OBP ×2 | `/fr/champagnes/grand-siecle/` | 🔍 **Nº26 のみ 1 件** |
| 2 | **Héritage** | `/fr/champagnes/heritage/` | 🔍 **無し** |
| 3 | **Brut Millésimé** | `/fr/champagnes/brut-millesime/` | 🔍 **無し** |
| 4 | **La Cuvée** | `/fr/champagnes/la-cuvee/` | 🔍 **無し** |
| 5 | 🔴 **Alexandra Rosé Millésimé** ⭐OBP | `/fr/champagnes/alexandra-rose-millesime/` | 🔍 **無し（gap）** |
| 6 | 🔴 **Cuvée Rosé** ⭐OBP | `/fr/champagnes/cuvee-rose/` | 🔍 **`laurent-perrier-rose` 1 件** |
| 7 | **Blanc de Blancs Brut Nature** | `/fr/champagnes/blanc-de-blancs-brut-nature/` | 🔍 **無し** |
| 8 | **Ultra Brut** | `/fr/champagnes/ultra-brut/` | 🔍 **無し** |
| 9 | **Harmony**（Demi-Sec。⚠️ **FR の sitemap に無く EN/DE/ES/JA のみ**） | `/en/champagnes/harmony/` | 🔍 **無し** |

### 🔴 公式が itération ページを公開しているもの（**全 27 のうち 8 つだけ**）

**Nº27 / Nº26 / Nº25 / Nº24 en magnum / Nº23 en magnum / Nº22 en magnum /
« Les Réserves » Nº20 / « Les Réserves » Nº17**

🔴 ⚠️ **「Itération 番号 → base vintages」の完全な対応表は公式サイトに存在しない。**
**フィッシュ・テクニック PDF も 5 点（GS20 / GS24 / GS25 / GS26 / GS27）しか公開されていない。**
→ **したがって「No. ○○ は ○○ 年」を staff が言える範囲は、この 8 つに限られる。** → Open Questions 2

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① トゥール＝シュル＝マルヌ、1812 年創業。スタイルは「フレッシュさ・エレガンス・ピュアさ」の 3 語。**
「**マルヌ河畔の Tours-sur-Marne** に本拠を置く、**1812 年創業**のメゾンです。
**社名は 2 人の人物の姓**で、Chef de Cave だった**ウジェーヌ・ローランの未亡人マチルド＝エミリー・ペリエ**が、
夫の姓に自分の姓を足したのが由来です。
造り手が自らのスタイルとして繰り返す言葉は 3 つだけ ——
**フレッシュさ（fraîcheur）、エレガンス（élégance）、ピュアさ（pureté）**。
**70 年代末にステンレスタンクを選んだ数少ないメゾンの一つ**で、
**最初の温度制御キュヴリー**を建てたのもこの家です。
シャルドネとピノ・ノワールの 2 品種でほぼ排他的に組み、**区画ごとに別々に醸造します。**」

**② グラン・シエクルの「番号」はヴィンテージでも順位でもない。1959 年以来「何回目か」の通し番号です。**
「🔴 **『No. 27』『No. 26』は年号ではありませんし、27 のほうが上という意味でもありません。**
造り手の言葉では『**1959 年以来、グラン・シエクルを再創造できたのはボトルで 27 回だけ**』——
つまり**何回目のアッサンブラージュかという通し番号**です。
グラン・シエクルは**あえてミレジムを名乗らないワイン**で、**3 つの卓越した年をブレンド**します。
**No. 27 は 2015 年（65%）・2013 年（25%）・2012 年（10%）、
No. 26 は 2012 年（65%）・2008 年（25%）・2007 年（10%）。**
**熟成はどちらも澱の上で 10 年**、**8 つのグラン・クリュ**から。
造り手はこれを『**une seule année（ただ一つの年）が差し出しうるより高い完成度**』と説明しています。」

**③ ロゼは「マセラシオン」。造り手が自ら『稀な savoir-faire』と呼ぶ、この家の看板です。**
「🔴 **シャンパーニュのロゼの造り方は 2 つある、と造り手自身が書いています ——
白ワインと赤ワインのアッサンブラージュか、マセラシオンか。**
**シャンパーニュで圧倒的多数はアッサンブラージュで、ローラン＝ペリエはマセラシオンのほうです。**
**1968 年**、ロゼ・シャンパーニュがまだ流行っていなかった時代に発売しました
（**カテゴリーとして成立するのは 1981 年**です）。
**ピノ・ノワール 100%**、除梗してステンレスのマセラシオンタンクに入れ、**48〜72 時間**果皮と接触させ、
そのあと果汁を抜いて**別のタンクで**発酵させます。**カーヴで 5 年。**
**アレクサンドラ**も同じマセラシオンの savoir-faire の上にあり、
そちらは**マセラシオンしたピノ・ノワールとシャルドネを一緒に発酵させます。**」

### 追加で使える一手

- **アレクサンドラ 2012（$1,255）**: 「**1982 年に生まれて、以来 10 ミレジムしか出ていません。**
  **ピノ・ノワール 80%・シャルドネ 20%、すべてグラン・クリュ**で、
  ピノは**アンボネイ、ブジー、マイィ、ヴェルズネー**、シャルドネは**アヴィズ、クラマン、ル・メニル＝シュル＝オジェ**。
  **10 年熟成。**難しさは、**ピノとシャルドネが同時に完璧な成熟に達している必要がある**ことだと造り手は言います。」
- **『レ・レゼルヴ』の逸話**: 「**ベルナール・ド・ノナンクールが、各イテラシオンの
  未デゴルジュマンのマグナムを数本、自分の個人的なリザーヴに取り置いていました。
  2012 年、創業 200 周年の年に、娘たちと醸造長がそれを発見して初めて公開したのが『レ・レゼルヴ』です。**
  **最初は No. 17 で澱の上 16 年、二度目が No. 20 で 20 年以上。**」
- **名前の由来**: 「**『グラン・シエクル』はフランス史で最も繁栄した 17 世紀の呼び名です。
  ルイ 14 世とヴェルサイユ —— 『自然だけでは創れないものを人が創る』という象徴で、
  ワインの考え方そのものを名前にしています。**」
- **1889 年のノン・ドゼ**: 「**この家は 1889 年に『Grand Vin Sans Sucre』を出しています。**
  マチルド＝エミリー・ペリエが**自分と英国の顧客の嗜好に合うものとして**造ったもので、
  **『ノン・ドゼ』が造り手の掲げる 3 つの savoir-faire の 1 つ**である歴史的な理由がここにあります。」
- **栽培**: 「**2018 年 2 月に VDC（シャンパーニュ持続可能栽培）と HVE（環境価値重視）の
  両方を取得**しています。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／出典が矛盾している**）

1. 🔴 ⚠️ **『グラン・シエクル・グランド・キュヴェ』と言わない。**
   **公式の名は `Grand Siècle Itération Nº27` / `Itération Nº26` である。**
   **`Grande Cuvée` という語は、公式サイトの取得した全ページで Grand Siècle と結びついて 1 件も出現しない**
   （`Grande Cuvée` はむしろ **Krug の別の製品名**であり、混同の危険がある）。
   **メニューの印字がそうなっているだけである。**
2. 🔴 ⚠️ **『No. 27 は No. 26 より上のランク』『番号は年』と言わない。**
   **番号は 1959 年以来のアッサンブラージュ回数の通し番号である。**
   **熟成年数も同じ（どちらも 10 年）。価格差はリリースの新しさであって等級ではない。**
   **さらに No. 25 は 12 年熟成で、番号と熟成年数は単調に対応しない。**
3. 🔴 ⚠️ **『オーガニック』『ビオディナミ』と言わない。**
   🏛 **Agence Bio の公的登録に Laurent-Perrier 系 4 SIRET すべてで 0 件。Demeter France にも該当なし。**
   **公式サイトに `bio` / `organic` / `biodynamie` / `Demeter` / `Ecocert` の語が一つも無い。**
   言えるのは **「2018 年 2 月に VDC と HVE を取得」**まで。
4. 🔴 ⚠️ **『除草剤を使っていない』『畑を耕している』など、栽培の具体を言わない。**
   **公式サイトに除草剤・殺虫剤・耕起・草生についての記述が一切無い。**
   **また HVE の「レベル」（レベル 3 等）も公式は明示していない。**
   さらに 🔴 **認証の範囲は公式の言葉で「Groupe 自身の区画の全体」であり、
   買いブドウの供給元区画を含むとは書かれていない。**
   **『畑はすべて認証済みです』とは言わない。**
5. 🔴 ⚠️ **マロラクティック発酵の有無を語らない。とくに『マロをしない』と言ってはならない。**
   **公式サイト（FR・EN）にもフィッシュ・テクニック 5 点にも `malolactique` / `malolactic` の語が 1 件も無い。**
   **『する』とも『しない』とも公式は述べていない。**
   ⚠️ **同様に『木樽を一切使わない』とも断定しない。**
   **公式が言うのは「70 年代末にステンレスタンクを選んだ」という積極的事実までであり、
   「木を使わない」という否定形の記述は存在しない**（`fût` / `chêne` / `barrique` / `oak` は 0 件）。
6. 🔴 ⚠️ **キュヴェ・ロゼを『セニエ法』と説明しない。**
   **公式はシャンパーニュのロゼの方法を「アッサンブラージュか macération」の 2 つとしか挙げず、
   自らを一貫して `macération` としか呼ばない。**
   **`saignée` の語は公式の本文に一度も現れない**（1 本の記事の URL スラッグにのみ存在し、その本文は触れない）。
   🔴 **THÉSEUS の DB は現在これを『セニエ法』と断定しているが、公式の裏づけが無い。**
7. 🔴 ⚠️ **ドザージュの数値・デゴルジュマン日・アルコール度数・生産本数を言わない。**
   **公式サイトにもフィッシュ・テクニック 5 点にも一切記載が無い。**
   🔴 **canonical が持つ `7 g/L`（Grand Siècle）と `10 g/L`（Cuvée Rosé）には公式の裏づけが無い。**
8. ⚠️ **『トゥール＝シュル＝マルヌはグラン・クリュ村です』を無条件に言わない。**
   **公式はそう書いているが、échelle des crus 上、Tours-sur-Marne が 100% なのはピノ・ノワールについてであり、
   シャルドネについてではない。**公式サイトはこの区別を書いていない。
   言うなら「**造り手はグラン・クリュに格付けされた村だと書いています**」と出典を明示する形まで。
9. ⚠️ **No. 26 のセパージュ比率を単一の数字で断定しない。**
   **公式のフィッシュ・テクニックとリリース記事と製品ページ見出しは `58% / 42%`、
   製品ページの本文ブロックだけが `52% / 48%`（かつ村が 11）と書いている。**
   言うなら「**シャルドネ主体でピノ・ノワールが補う、8 つのグラン・クリュから**」まで。
10. ⚠️ **キュヴェ・ロゼのマセラシオン時間と remontage 回数を単一の数字で断定しない。**
    **公式は「48〜72 時間・1 日 2 回」と「48 時間・8 時間ごと」の 2 通りを書いている。**
    言うなら「**48 時間から 72 時間**」まで。
11. ⚠️ **第三者点数を断定しない。**
    **公式ページ自身が Wine Advocate の No. 27 を `97/100`（製品ページ）と `95+/100`（リリース記事）で食い違わせている。**
    **Cuvée Rosé と Alexandra の点数は公式ページに評者名すら表示されていない。**
12. ⚠️ **アレクサンドラを『グラン・シエクル・アレクサンドラ』と呼ばない。**
    **現行の公式サイト上、Alexandra は `Alexandra Rosé Millésimé` として Grand Siècle と並列の別キュヴェである。**
    **`Grand Siècle Alexandra` という形は本調査で取得したどの公式ページにも現れなかった**
    （**「存在しなかった」ではなく「現行サイトでは確認できなかった」**）。
13. ⚠️ **Salon / Delamotte / Champagne de Castellane を「ローラン＝ペリエのシャンパーニュ」として説明しない。**
    **これらは Groupe Laurent-Perrier の別ブランド・別メゾンであり、
    その内容は Laurent-Perrier の出典ではない。**
    ⚠️ **なお本調査では、この 4 ブランド体制を公式に取得可能な形で確認できていない**（後述）。

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **本件は 4 つの層に分かれる。**
**① 既存登録票 `V-1` への証拠追加（新番号は開かない）
② 既存登録票 `V-3` / `V-2` への証拠追加（同上）
③ canonical の散文が公式と矛盾する 2 件（既存の族に当たらない。番号は開かない）
④ canonical にレコードが存在しない 2 件 ＝ *gap*（衝突ではない。どの登録クラスも該当しない）**

🔒 **`REGISTER.md` も canonical も本書では一切編集していない。**

---

### 🔴 ① 既存 `V-1` への証拠追加 —— **Grand Siècle の Itération は Krug の Édition と同一の形である**

**1. 該当する既存登録票**
🔴 **`V-1`（層のずれ・édition）** —— 登録票の記述は
「`cuvee:krug-grande-cuvee` 配下に vintage_year=null の行が 12 件あり、識別しているのは
`release_label`（162ème〜173ème Édition）と `base_year`(2006–2017) のみ。**(cuvée, vintage_year) は一意でない。**
OBP は édition を**キュヴェ名の一部として印字**。canonical は édition を vintage 層に置いている → 3 本とも unresolved」。

🔴 **Laurent-Perrier `Grand Siècle` は、これと同一の構造を持つ 2 例目である。**

**2. 実測した証拠（🔍 読み取りのみ）**

| | 値 |
|---|---|
| **canonical レコード** | `id = laurent-perrier-grand-siecle-26`<br>`name = "Grand Siècle Itération #26 Brut"`<br>`vintage = "NV"`<br>`classification = "Brut Multi-Vintage"`<br>`aging = "8+ years sur lie; multi-vintage blend of 3 vintages"` |
| **OBP 印字（行 2）** | `'Grand Siècle Grande Cuvée No. 26,' Brut` |
| **公式の正式名** | `Grand Siècle Itération Nº26` |
| **intake の結果** | `match_state = unresolved` / `cuvee_state = unresolved` / `confidence = 0.0`<br>evidence 逐語: **「`'Laurent-Perrier'` の canonical キュヴェ 2 件に一致無し: `'Grand Siècle Grande Cuvée No. 26'`」** |

🔴 **すなわち、同一の release identifier が 3 通りに綴られている ——
`Itération #26`（canonical）／`Grande Cuvée No. 26`（メニュー）／`Itération Nº26`（公式）。**
**`#` と `Nº` と `No.` の記号差、`Itération` と `Grande Cuvée` の語そのものの差。**
🔴 **canonical はレコードを持っているのに、intake は「一致無し」と結論している。**
**これは `V-1` の「canonical は édition を vintage 層に置いている」よりさらに悪い形で、
`Laurent-Perrier` の場合 identifier は `name` 文字列の中に埋め込まれており、
構造化されたフィールドがどこにも無い。**

**3. `V-1` を強化する新しい証拠 —— 「番号は base year から復元できない」**

🔴 ✅ **公式のフィッシュ・テクニックが示す base vintages:**

| Itération | base vintages |
|---|---|
| **Nº25** | **2008（65%）/ 2007（25%）/ 2006（10%）** |
| **Nº26** | **2012（65%）/ 2008（25%）/ 2007（10%）** |
| **Nº27** | **2015（65%）/ 2013（25%）/ 2012（10%）** |

🔴 **`2008` と `2007` は Nº25 と Nº26 の両方に、`2012` は Nº26 と Nº27 の両方に現れる。**
🔴 **したがって `base_year` は itération の関数ではなく、`base_year` から itération は逆算できない。**
**Krug（`base_year` が 1 つ）では `base_year` が代理キーとして辛うじて機能しうるが、
Grand Siècle では base year が 3 つあり、しかも集合が重なるため、代理キーとしてすら機能しない。**

**4. 🔴 プロジェクト既定の論点を鋭くする点（ブリーフの問い）**

🔴 **「`vintage` 欄を一括で直す」マイグレーションは、このクラスのデータを復元不能に破壊する。**
**本件はその主張を、これまでで最も強い形で裏づける:**
- **Krug（`V-1`）では `vintage` に `base_year` が入っていれば、少なくとも 1 つの実在の年が残る。**
- 🔴 **Grand Siècle では、`vintage` に何を書いても情報が失われる。**
  **`2012` と書けば Nº26 か Nº27 か決まらない。`NV` と書けば Nº26 と Nº27 が区別できない
  （現に canonical は `vintage="NV"` であり、No. 27 のレコードが追加された瞬間に
  `(cuvée, vintage)` が衝突する）。**
- 🔴 **すなわち、`Grand Siècle` において `vintage` フィールドは
  「正しい値が存在しない」フィールドである。識別子は別の層に置くしかない。**

**5. 推奨（🔒 実行していない・番号は開かない）**
- **`V-1` の対象に `Laurent-Perrier Grand Siècle` を追加する。**
- **`release_label`（`Itération Nº26` / `173ème Édition`）を cuvée 層でも vintage 層でもない
  独立した識別軸として扱えるかどうかの設計判断。**
- **正規化するなら `Nº` / `No.` / `#` / `n°` の記号差と、`Itération` / `Grande Cuvée` の語差の両方を吸収する必要がある。**
  ⚠️ **ただし `Grande Cuvée` は Krug の実在のキュヴェ名でもあるため、
  「`Grande Cuvée` → `Itération` に読み替える」ような一般規則は絶対に作ってはならない。**
  **これは Laurent-Perrier のメニュー印字に固有の誤りである。**

**6. Confidence** 🔴 **High。** **公式の URL 構造（`/champagnes/grand-siecle/iteration-26/`）、
ナビゲーション表記、フィッシュ・テクニック PDF の見出し、リリース記事の見出しの 4 者すべてが `Itération` で一致。
`Grande Cuvée` は全取得ページで 0 件。canonical と intake の値は実測。**

---

### 🔴 ② 既存 `V-3` / `V-2` への証拠追加 —— **`Les Réserves` は「鍵が 1 本では足りない」の実例**

**1. 該当する既存登録票**
- 🔴 **`V-3`（層のずれ・Plénitude）** —— Dom Pérignon の P2 / P3。
  「一つの鍵では足りない」＝ 同じ cuvée・同じ vintage で、**熟成／デゴルジュマンの状態が違う複数の製品**が存在する。
- **`V-2`（層のずれ・容量）** —— Roederer Cristal 2013 と 2013 Magnum。**`bottle_format` が identity の一部**。

**2. 証拠（✅ 公式）**
🔴 **同一の Itération 番号が二度商品化される。**
- ✅ **`Les Réserves` Itération Nº17** —— 「**Bernard de Nonancourt が各 Itération の未デゴルジュマンの magnum を
  数本、個人のリザーヴに取り置いていた…2012 年に発見され、澱の上 16 年を経て商品化された**」
- ✅ **`Les Réserves` Itération Nº20** —— **1999/1997/1996、54/46、magnum で 20 年以上**
- ✅ **通常の Nº22 / Nº23 / Nº24 は「en magnum」として別ページ・別製品**
- ✅ **公式の一般規則: 「75 cl では澱の上 10 年、magnum ではさらに数年」**

🔴 **したがって Grand Siècle の一意な identity には最低 3 つの軸が要る:**
**`itération 番号` × `フォーマット（75 cl / 150 cl）` × `リリース系列（通常 / Les Réserves）`。**
**`Les Réserves` を分けているのは実質的に「デゴルジュマンをいつしたか」である。**
⚠️ **ただし公式はデゴルジュマンの日付を一切公開していない。
公開されているのは「澱の上で何年置いたか」（16 年 / 20 年以上）だけである。**

**3. `V-3` に対する新しい示唆**
🔴 **`V-3` は「一つの鍵（vintage_year）では足りない」と述べる。**
**Grand Siècle はさらに一歩進んで、「二つの鍵（cuvée, itération）でも足りない」ことを示す。**
**Dom Pérignon P2 は少なくとも vintage が残っているが、Grand Siècle には残る年が無い。**

**4. Confidence** 🔴 **High。** **公式の製品ページ 3 点とフィッシュ・テクニック 2 点で確認。**

---

### 🔴 ③ canonical の散文が公式と矛盾する —— **既存の族に当たらない。番号は開かない**

🔒 **以下は「どの登録クラスにも当てはまらない形」である。番号を開くのは CTO の判断であり、
本書では `LP-A` / `LP-B` という仮の呼称を本書内でのみ用いる。**

#### 🔴 `LP-A`（本書内の仮称）—— **`Cuvée Rosé` の醸造法の断定**

**1. canonical の記述（🔍 逐語）**
`id = laurent-perrier-rose`
- `description`: 「**ピノ・ノワール100%のセニエ法（マセレーション）で造られる珍しいアプローチが特徴。**」
- `description_en`: 「**Unusual for being made 100% from Pinot Noir by saignée (maceration), rather than the typical assemblage method.**」
- `obp_note`: 「**世界最高のロゼNV——セニエ法の100%ピノ・ノワール。**（中略）**ピノ・ノワール100%のセニエ法**」
- `obp_note_en`: 「**100% Pinot Noir, saignée method.**（中略）**saignée (skin maceration) not assemblage**」
- `winemaking`: 「**セニエ法（果皮と果汁を数時間マセレーション）でロゼカラーを得る**」
- `winemaking_en`: 「**Saignée method (skin maceration for several hours)**」
- 🔴 `winemaking` / `winemaking_en`: 「**マロラクティック発酵あり** / **MLF performed**」
- 🔴 `aging`: 「**36+ months sur lie**」／`terroir`: 「**12 地区以上の村から**」／`dosage`: 「**Brut — 10 g/L**」

**2. 公式との突き合わせ**

| canonical の主張 | ✅ 公式 | 判定 |
|---|---|---|
| 🔴 **`saignée`（セニエ法）** | 🔴 **公式は一貫して `macération` としか呼ばない。**公式の定義ページはシャンパーニュのロゼの方法を「**assemblage か macération**」の 2 つとしか挙げず、`saignée` を挙げない。**`saignée` の語は公式本文に 1 件も無い**（記事 1 本の URL スラッグにのみ存在し、その本文は触れない） | ⚠️ 🔴 **公式の裏づけが無い** |
| 🔴 **「マロラクティック発酵あり」** | 🔴 **公式サイト FR・EN、フィッシュ・テクニック 5 点のすべてに `malolactique` / `malolactic` が 1 件も無い** | ⚠️ 🔴 **公式は沈黙。断定は不可** |
| **「36+ months sur lie」** | 🔴 **公式は「カーヴで 5 年（`un vieillissement prolongé de 5 ans`）」と 3 か所で明記** | ⚠️ 🔴 **食い違う（36 か月 = 3 年 < 5 年）** |
| **「12 地区以上の村」「グラン・クリュとプルミエ・クリュ」** | 🔴 **公式は「Montagne de Reims の 10 ほどの Crus、その多くが Grands Crus（`majoritairement des Grands Crus`）」** | ⚠️ **数が食い違い、「プルミエ・クリュ」は公式に無い** |
| **「Brut — 10 g/L」** | ⚠️ **公式にドザージュの数値が一切無い** | ⚠️ **裏づけ無し** |
| **「果皮と果汁を数時間」** | 🔴 **公式は 48〜72 時間（または 48 時間）** | ⚠️ 🔴 **食い違う（「数時間」ではない）** |
| **Pinot Noir 100%** | ✅ **一致** | ✅ |
| **`founded_year = 1812`** | ✅ **一致**（公式の沿革が 1812 年） | ✅ |

**3. なぜ重要か**
🔴 **`saignée` と `macération` は別の技法である。**
**公式が説明する工程は「ロゼ専用のタンクに除梗した Pinot Noir を入れ、48〜72 時間浸漬し、
果汁を抜いて別タンクで発酵させ、残った果粒は別に圧搾する」——
すなわちバッチ全体がロゼのために組まれている。**
**`saignée` は本来「赤ワインを造るための槽から果汁の一部を抜く」技法を指す。**
🔴 **canonical の `obp_note` は staff がそのまま読み上げる文言であり、
「セニエ法の 100% ピノ・ノワール」は、この生産者が自らの看板と呼ぶ savoir-faire を
別の技法の名で紹介してしまう。**

**4. OBP への影響**
🔍 **OBP 行 3（$250）はこのレコードに `alias` で解決している（confidence 0.9）。**
🔴 **すなわち「正しく解決した唯一の行」が、間違った散文を引いてくる。**
**照合は成功しているのに、卓上に出る文言が誤っている。**

**5. 推奨（🔒 実行していない）**
- **`saignée` の語を落とし、`macération` に置き換える。**
- **`MLF performed` を落とす**（公式は沈黙しており、どちらの断定も不可）。
- **`36+ months` を公式の「5 年」に合わせる。**
- **`10 g/L` を落とすか、出典不明として明示する。**
- ⚠️ **いずれも canonical への書き込みであり、本書では実行していない。**

**6. Confidence** 🔴 **High。** **公式の専用ページ 3 点（savoir-faire / 製品ページ / 2023-02-16 の記事）と
2024 年 4 月の記事で、工程の記述が一致して `macération` である。語の走査は機械的に実施。**

#### 🔴 `LP-B`（本書内の仮称）—— **`Grand Siècle Itération #26` のスペックの断定**

**1. canonical の記述（🔍 逐語）**
`id = laurent-perrier-grand-siecle-26`
`grapes = ["Chardonnay 55%", "Pinot Noir 45%"]` ／ `aging = "8+ years sur lie; …"` ／
`dosage = "Brut — 7 g/L"` ／ `points = 96` ／
`winemaking` = 「**シャルドネ55%主体。マロラクティック発酵あり。最終的に8年以上のシュール・リー熟成。手作業デゴルジュマン。**」／
`obp_note` = 「**イテレーション番号が品質の継続性を保証します。**」／
`description` = 「**イテレーション#26は最新リリース**」

**2. 公式との突き合わせ**

| canonical | ✅ 公式 | 判定 |
|---|---|---|
| 🔴 **Chardonnay 55% / Pinot Noir 45%** | 🔴 **`58% / 42%`（フィッシュ `GS26-FR.pdf` ＋ リリース記事 ＋ 製品ページ見出し）または `52% / 48%`（製品ページ本文）** | ⚠️ 🔴 **`55/45` はどちらとも一致しない** |
| 🔴 **「8+ years sur lie」** | 🔴 **公式は「10 ans de vieillissement sur lies dans une bouteille de 75 cl」と 3 か所で明記** | ⚠️ 🔴 **食い違う** |
| 🔴 **「マロラクティック発酵あり」** | 🔴 **公式・フィッシュに `malolactique` が 1 件も無い** | ⚠️ 🔴 **公式は沈黙** |
| 🔴 **「手作業デゴルジュマン」** | 🔴 **公式にデゴルジュマンの方式についての記述が一切無い** | ⚠️ 🔴 **裏づけ無し** |
| **「Brut — 7 g/L」** | ⚠️ **公式にドザージュの数値が一切無い** | ⚠️ **裏づけ無し** |
| 🔴 **「イテレーション番号が品質の継続性を保証」** | 🔴 **公式は「1959 年以来 27 回だけ再創造できた」という回数の通し番号として説明する。「品質の継続性を保証する」という記述は無い** | ⚠️ 🔴 **公式に無い解釈** |
| 🔴 **「#26 は最新リリース」** | 🔴 **現行の最新は `Itération Nº27`（2026 年 1 月リリース）。#26 は 2023 年 9 月** | ⚠️ 🔴 **時点で誤り。OBP も 27 と 26 を並べている** |
| **`points = 96`** | ⚠️ **公式が掲載する Nº26 の点数は 100 / 19,5 / 98。96 はどれとも一致しない** | ⚠️ **出典不明** |
| **3 ヴィンテージのブレンド・8 年以上の個別熟成という枠組み** | ✅ **「3 années exceptionnelles」の枠組みは公式と一致** | ✅ **枠組みは正しい** |
| **`founded_year = 1812` / `subregion = Tours-sur-Marne`** | ✅ **一致** | ✅ |
| **`name` に `Itération #26` を含む** | ✅ 🔴 **公式の語 `Itération` を採用している点は正しい。**メニュー印字のほうが誤っている | ✅ |

**3. Confidence** 🔴 **High。** **フィッシュ・テクニック PDF の本文を直接抽出して照合。**

---

### 🔴 ④ **canonical に存在しない 2 件 ＝ gap（衝突ではない）**

🔴 **以下は「レコードが無い」形であり、`REGISTER.md` のどの登録クラスも
「record not present」を扱っていない。したがって衝突として番号を開くのは誤りである。**

| OBP 行 | 状態 |
|---|---|
| 🔴 **行 1: `Grand Siècle Itération Nº27`（$920）** | 🔍 **canonical に `Laurent-Perrier` のレコードは 2 件しかなく、Nº27 は含まれない。→ *gap*。**<br>⚠️ 🔴 **さらに、仮に Nº27 を現在のスキーマで追加すると、`vintage="NV"` の行が 2 本になり、
`(cuvée, vintage)` が一意でなくなる —— すなわち `V-1` の衝突が canonical 内部で顕在化する。**<br>**Nº27 の追加は、識別軸の設計判断を先に済ませないと実行できない。** |
| 🔴 **行 4: `Alexandra Rosé Millésimé 2012`（$1,255）** | 🔍 **canonical に Alexandra のレコードは存在しない。→ *gap*。**<br>**こちらは真のヴィンテージ・シャンパーニュであり、`cuvée × vintage_year` で素直に一意になる。
設計上の障害は無く、純粋な欠落である。** |

🔍 **参考: canonical には Laurent-Perrier の公式 9 キュヴェのうち 2 つしか無い。**
**`Héritage` / `Brut Millésimé` / `La Cuvée` / `Blanc de Blancs Brut Nature` / `Ultra Brut` / `Harmony` /
`Alexandra Rosé Millésimé` の 7 つが不在。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY**）

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の会社名** | ✅ **合格。** `https://www.laurent-perrier.com/fr/mentions-legales/` に逐語で「**Le site www.laurent-perrier.com est la propriété de Laurent-Perrier, Société Anonyme à Directoire et Conseil de Surveillance, au capital de 22 594 271,80 €, dont le siège social se situe en France, à Tours-sur-Marne (51150), 32 Avenue de Champagne, immatriculée au Registre du Commerce et des Sociétés de Reims, numéro B 335 680 096.**」 |
| 🔴 **(c) 公的登録と一致する住所** | ✅ 🏛 **合格。** **`recherche-entreprises.api.gouv.fr/search?q=335680096` が 1 件のみを返し、`nom_complet = LAURENT-PERRIER`、`siege.adresse = 32 AVENUE DE CHAMPAGNE 51150 TOURS-SUR-MARNE`、`siret = 33568009600021`。**<br>**mentions légales の RCS 番号 `B 335 680 096` と SIREN `335680096` が完全一致。** |
| **(b) 非関係の否認表示** | ✅ **合格。無し。**「ファンサイト」「非公式」等の記述は無い |
| **(d) 整合した商業・法務フッター** | ✅ **合格。**`L'abus d'alcool est dangereux pour la santé` の法定表示が全ページ、mentions légales、GDPR 窓口（`GDPR@laurent-perrier.fr`）、著作権表示 `©Laurent-Perrier`、制作会社（WESTON MILLS, 16 rue des Jeuneurs, 75002 Paris）まで完備。**ホスティングも自社（「Ce site est hébergé par Laurent-Perrier」）** |
| **ドメイン売却／パーキングの兆候** | **無し** |
| **年齢確認ゲート** | **本調査では遭遇しなかった**（静的取得で本文が返る）。**CAPTCHA にも遭遇していない** |

🔴 **本調査で `NOT_THE_PRODUCER_*` / `FANPAGE_*` として退けたサイトは無い。**
**公式ドメイン `www.laurent-perrier.com` 以外を、事実の根拠として一切使っていない。**
（**WebSearch は 1 回のみ、Groupe の企業情報の所在を探すために使用。
その要約文は事実として採用していない** —— §「取得できなかったもの」参照。）

⚠️ **付随ドメイン `laurent-perrier.fr`**（mentions légales が GDPR 窓口として挙げるもの）
—— **`https://` で SSL 証明書が期限切れ（curl error 60）。取得を中止し、一切依拠していない。**

### 一次資料（**公式ドメインと公的登録のみ**）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt`** | `Sitemap: https://www.laurent-perrier.com/sitemap_index.xml` を明示。**`/sitemap.xml` は 404** |
| **`sitemap_index.xml` → `vins` / `la-maison` / `page` / `post` / `guide` sitemap** | **9 キュヴェページ、8 itération ページ、3 savoir-faire ページ、`notre-histoire`、`notre-vision`、`le-chateau-de-louvois`、magazine 記事の全 URL（6 言語分）** |
| 🔴 **`/fr/champagnes/grand-siecle/`** | 🔴 **「Depuis 1959, il n'a été possible de recréer Grand Siècle que 27 fois en bouteille et 24 fois en Magnum.」＝ 番号の正体。3 原則。「最大 11 の Grands Crus」。名の由来（17 世紀・ルイ 14 世・Château de Louvois の Orangerie）** |
| 🔴 **`/fr/champagnes/grand-siecle/iteration-27/`** | 🔴 **OBP 行 1 の実体。2015(65%)/2013(25%)/2012(10%)、60/40、8 Grands Crus、村名 8、澱上 10 年、公式テイスティングノート、点数 3 種、提供温度 10–12 °C** |
| 🔴 **`/fr/champagnes/grand-siecle/iteration-26/`** | 🔴 **OBP 行 2 の実体。2012(65%)/2008(25%)/2007(10%)。**⚠️ **見出し行は 58/42・8 Grands Crus、本文ブロックは 52/48・11 村。同一ページ内で矛盾** |
| 🔴 **`GS27-FR.pdf` / `GS26-FR.pdf`（公式フィッシュ・テクニック）** | 🔴 **`application/pdf` を確認。テキストレイヤーを直接抽出。**<br>**GS27: 60/40、村 8、10 年、`Laurent-Perrier - 11 Septembre 2025`**<br>**GS26: 58/42、村 8、10 年、`Laurent-Perrier - 21 Juillet 2025`**<br>🔴 **両者に `dosage` / `dégorgement` / `malolactique` / `fût` / `chêne` / `g/L` の語が 1 件も無いことを機械走査で確認** |
| **`GS25-FR.pdf` / `GS24-FR.pdf` / `GS20-FR.pdf`** | **キャッシュ済み。**`GS25` = 2008/2007/2006、60/40、9 Grands Crus、12 年 |
| 🔴 **`/fr/champagnes/grand-siecle/les-reserves-iteration-20/`** | 🔴 **`V-3` / `V-2` の決定的証拠。**「各 Itération の未デゴルジュマンの magnum を個人リザーヴに取り置いた」「2012 年に発見」「Nº17 は澱上 16 年」「Nº20 は 20 年以上」。1999/1997/1996、54/46 |
| 🔴 **`/fr/champagnes/cuvee-rose/`** | 🔴 **OBP 行 3 の実体。Pinot Noir 100%、Montagne de Reims の 10 ほどの Cru、5 年、macération 48–72h、1968 年発売、公式ノート** |
| 🔴 **`/fr/la-maison/notre-savoir-faire/maceration/`** | 🔴 **`LP-A` の決定的証拠。**「シャンパーニュのロゼの方法は assemblage か macération の 2 つ」。工程の逐語（除梗 → ステンレスタンク → 48–72h → 1 日 2 回 remontage → 果汁分離 → 残果粒を圧搾 → débourbage → 別途発酵）。**Alexandra は 1982 年創出・10 ミレジムのみ** |
| 🔴 **`/fr/magazine/savoir-faire/champagne-rose-maceration-saignee-assemblage/`**（2023-02-16） | 🔴 **本文タイトルは「Cuvée Rosé, un rosé de macération」。**`saignée` は **URL スラッグにのみ**存在し本文に無いことを確認 |
| **`/fr/magazine/savoir-faire/cuvee-rose-lexpression-du-pinot-noir/`**（2024-04） | **Cru の具体名（Ambonnay / Bouzy / Louvois / Tours-sur-Marne / Verzenay / Verzy / Mailly / Aÿ / Mareuil-sur-Aÿ）、vendanges en vert、Michel Fauconnet の収穫追跡、5 年熟成。**⚠️ **remontage を「8 時間ごと・48 時間」とする（savoir-faire ページと食い違う）** |
| 🔴 **`/fr/champagnes/alexandra-rose-millesime/`** | 🔴 **OBP 行 4 の実体。公式名 `Alexandra Rosé Millésimé`、2012、PN 80/CH 20、100% Grands Crus、村名 7、共発酵、10 年、公式ノート** |
| **`/fr/magazine/nouveautes/alexandra-rose-2012/`**（2023-09-23） | **リリース告知。⚠️ ここでのみ「une Grande Cuvée Rosé Millésimé」という記述的表現が使われる（Grand Siècle についてではない）** |
| 🔴 **`/fr/la-maison/notre-savoir-faire/`** | 🔴 **「Nos 3 savoir-faire」の定義。ステンレス採用（70 年代末）、温度制御キュヴリー、`vinification parcellaire`、「319 villages AOC / 17 Grands Crus / 42 Premiers Crus」、買いブドウのパートナーシップ** |
| **`/fr/la-maison/notre-savoir-faire/assemblage-vins-reserve/`** | **リザーヴワイン専用のステンレス・キュヴリー、低温・低操作・酸化回避。Grand Siècle は「17 の Grands Crus のうち最大 11」。`La Cuvée` は 100 超の Cru とリザーヴ 30% まで** |
| 🔴 **`/fr/la-maison/notre-vision/`** | 🔴 **§Farming の中核。VDC ＋ HVE を「2018 年 2 月」「sur la totalité de ses parcelles」で取得。シャンパーニュ産業の 2030 年 100% 目標** |
| 🔴 **`/fr/la-maison/notre-histoire/`** | 🔴 **1812 / 1887 / 1889 / 1925 / 1939 / 1948 / 1999 / 2004 / 2019 / 2025。歴代 Chef de Cave 4 名。社名の由来** |
| 🔴 **`/fr/mentions-legales/`** | 🔴 **真正性の検証。法人形態・資本金・住所・RCS Reims B 335 680 096** |
| 🔴 🏛 **`recherche-entreprises.api.gouv.fr`** | 🔴 **SIREN `335680096`（LAURENT-PERRIER・NAF 70.10Z・本社機能）／`351306022`（CHAMPAGNE LAURENT-PERRIER・NAF 11.02A・発泡性ワイン製造）／`388367534`（SCEA DES GRANDS MONTS・NAF 01.21Z・ブドウ栽培）。全 17 件の関連法人が同一住所に登記。全件 `liste_id_bio = null`** |
| 🔴 🏛 **`opendata.agencebio.org/api/gouv/operateurs/?siret=…`** | 🔴 **4 SIRET すべてで `{"nbTotal":0,"items":[]}`。有機登録の不在の証明** |
| 🏛 **`demeter.fr/?s=laurent-perrier`** | **検索結果エントリ 0 件** |
| **EN 版（`/en/the-maison/savoir-faire/` ほか 5 ページ）** | **FR との突き合わせに使用。**🔴 **`malolactic` / `oak` / `barrel` / `cask` の出現数が全ページ 0 であることを機械走査で確認** |

### 取得できなかったもの / 存在しなかったもの

- 🔴 **`Cuvée Rosé` と `Alexandra Rosé Millésimé` に公式フィッシュ・テクニックが存在しない。**
  **製品ページに「Télécharger la fiche technique」のリンクが無く、
  `wp-content/uploads/2026/06/` 配下への 5 通りの命名推測はすべて 404。**
  **公式 PDF は Grand Siècle の 5 点（GS20 / GS24 / GS25 / GS26 / GS27）のみである。**
- 🔴 **公式サイトに「Itération 番号 → base vintages」の完全な対応表が無い。**
  **公開されている itération ページは 27 のうち 8 つだけ。**
- 🔴 **自社畑の面積（ヘクタール）が公式サイトに一切無い。**
- 🔴 **ドザージュの数値・デゴルジュマン日・アルコール度数・生産本数が、全キュヴェについて公式に無い。**
- 🔴 **マロラクティック発酵についての記述が、FR・EN・フィッシュ 5 点のいずれにも無い。**
- 🔴 **木樽の使用／不使用についての記述が無い**（`fût` / `chêne` / `barrique` / `oak` = 0 件）。
- 🔴 **除草剤・殺虫剤・耕起・草生・被覆作物についての記述が無い。HVE の「レベル」の明示も無い。**
- ⚠️ 🔴 **Groupe Laurent-Perrier の 4 ブランド体制（Laurent-Perrier / Salon / Delamotte / Champagne de Castellane）を、
  取得可能な公式ページで確認できていない。**
  **WebSearch は Euronext 上の公式財務コミュニケを指したが、
  当該ページは `WebFetch` に対して本文が空で返った（JS 描画）。**
  🔴 **したがって本書はこの体制を事実として主張しない。**
  **唯一 `laurent-perrier.com` 上にある関連記述は、沿革ページの
  「Olivier Vigneron は 2000 年に De Castellane に入り、Alain Terrier に採用された」という人事上の言及のみ。**
  🏛 **国家登録の検索では `Salon` / `Delamotte` / `de Castellane` に該当する
  シャンパーニュ・メゾンを特定できなかった**（API の全文検索が名寄せに弱く、無関係な同名法人を返す）。
  → **Open Questions 5。⚠️ この 3 ブランドはいずれにせよ OBP 行を持たず、`CAT-3`（ブランド軸）の管轄である。**
- ⚠️ **`laurent-perrier.fr` は SSL 証明書期限切れで取得不能。**
- ⚠️ **`Harmony` が FR の sitemap に無く EN / DE / ES / JA にのみ存在する。**
  **FR 市場で販売していないのか、単なる sitemap の欠落かは不明。**
- ⚠️ **magazine 記事は 170 件超あり、本調査で読んだのは Grand Siècle / Cuvée Rosé / Alexandra 関連の 8 件程度。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical レコード: 2 件のみ**（`migration/out/export/db_wine_canonical.json`、928 件を機械走査）
1. **`laurent-perrier-grand-siecle-26`** — `name='Grand Siècle Itération #26 Brut'` / `vintage='NV'` /
   `subregion='Tours-sur-Marne'` / `color='Blanc'` / `classification='Brut Multi-Vintage'` /
   `grapes=['Chardonnay 55%','Pinot Noir 45%']` / `aging='8+ years sur lie; …'` / `dosage='Brut — 7 g/L'` /
   `founded_year=1812` / `points=96` / `appellation_id='appellation:tours-sur-marne'`
2. **`laurent-perrier-rose`** — `name='Cuvée Rosé Brut'` / `vintage='NV'` / `color='Rosé'` /
   `grapes=['Pinot Noir 100%']` / `aging='36+ months sur lie'` / `dosage='Brut — 10 g/L'` /
   `founded_year=1812` / `points=92`

🔍 **OBP: 4 本**（`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`）。
**`source_row_id` = `86acf5e937`（No. 27）/ `1d124df864`（No. 26）/ `02e0c829d5`（Cuvée Rosé）/ `7cecc6ee97`（Alexandra）。**
**全 4 本が `producer_state = exact`（`producer:laurent-perrier`）。
`match_state` は Cuvée Rosé の 1 本が `alias`（0.9）、残り 3 本が `unresolved`（0.0）。**
🔍 **`unresolved` 3 本の evidence はいずれも
「`'Laurent-Perrier'` の canonical キュヴェ 2 件に一致無し」で同一。**
🔍 **`_collision_risk` は 4 本とも `LOW`。**

⚠️ **本書は `research/out/t-01/mapping.json` を参照していない。**
**上記の「resolved / unresolved」の数はすべて
`obp_intake_normalized_20260804.json` から読み出したものである**（両者が食い違う既知の問題のため、出典を明示）。

🔒 **canonical・`REGISTER.md`・`migration/` のいずれも編集していない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | 🔴 **法人形態・資本金・RCS 番号・住所が mentions légales と国家登録で完全一致。醸造法人と栽培法人を SIREN で分離して特定。歴代 Chef de Cave 4 名の氏名と就任年が公式** |
| **Overview** | **High** | **スタイル 3 語、3 つの savoir-faire、ステンレス採用が一次で取れた** |
| **History** | 🔴 **High** | 🔴 **1812 / 1887 / 1889 / 1939 / 1948 / 1959 / 1968 / 1981 / 2012 / 2018 / 2025 が公式沿革と各ページで確定。社名の由来（2 人の姓）も公式** |
| **Location** | **Medium-High** | **本拠と各キュヴェの村名は完全。**⚠️ **自社畑の面積が公式に無い。Tours-sur-Marne の Grand Cru 表記に品種の但し書きが要る** |
| 🔴 **Farming** | 🔴 **Medium-High** | 🔴 **VDC と HVE の取得（2018 年 2 月）とその範囲の限定が公式の逐語で取れ、有機の不在が公的登録 4 件で証明できた。**⚠️ **栽培実務の具体（除草剤等）が公式に完全に不在で、HVE のレベルも不明** |
| **Winemaking** | 🔴 **Medium-High** | 🔴 **Grand Siècle 2 本の base vintages・セパージュ・村名・熟成、Cuvée Rosé と Alexandra の工程が公式 PDF と製品ページで確定。**⚠️ **ドザージュ・デゴルジュマン・MLF・アルコール度数が全キュヴェで完全に不在。No. 26 のセパージュが公式内で割れている** |
| **Style** | **High** | 🔴 **OBP 4 本すべてについて公式のテイスティングノートと料理の合わせを取得** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **OBP 4 本すべての実体を公式で特定。うち 2 本は公式名がメニュー印字と違うことまで確定** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **`V-1` / `V-3` / `V-2` への証拠追加はいずれも公式 PDF と製品ページで裏づけ。canonical と intake の値はすべて実測。散文の矛盾は語の機械走査で確認** |
| **Staff Notes** | **High** | ⚠️ **13 項目。🔴「グランド・キュヴェ」「番号は等級／年」「オーガニック」「マロをしない」「セニエ法」「ドザージュの数値」「グラン・シエクル・アレクサンドラ」という 7 つの誤りを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を超過。実感としては 80% 前後）。** | **OBP 4 本すべてについて、公式の正式名・base vintages またはセパージュ・産地・熟成・造り手のテイスティングノートを言える。ロゼの製法は造り手自身の逐語で言える。栽培は認証名と取得年と範囲の限定まで言える。**<br>**欠けているのは ① 分析値（ドザージュ・アルコール度数・デゴルジュマン）、② MLF と木樽の有無、③ 自社畑の面積、④ 27 itération の完全な対応表。**<br>**いずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。** |

**reached_70: YES（~80%）。**

---

## Open Questions

1. 🔴 **canonical の `Grand Siècle` を、どの層で識別するか。**
   **`Itération 番号` は cuvée 名の一部か、vintage 層の `release_label` か、独立した第三の軸か。**
   🔴 **Nº27 を追加した瞬間に `(cuvée, vintage="NV")` が一意でなくなるため、
   この判断を先に済ませないと Nº27 は登録できない。**
   → 🔒 **設計判断。本書では実行していない。** → §Canonical Conflict ①

2. 🔴 **`Itération 番号 → base vintages` の完全な対応表が公式に存在しない。**
   **公開されているのは 8 つ（Nº27 / Nº26 / Nº25 / Nº24m / Nº23m / Nº22m / Réserves Nº20 / Réserves Nº17）のみ。**
   → **メゾンへの直接照会か、実ボトルのラベル確認でしか埋まらない。**
   → **それまで staff は、この 8 つ以外の番号について base vintages を語らない。**

3. 🔴 **自社畑の面積と所有区画が公式に一切無い。**
   **「自社畑がある」「買いブドウのパートナーシップが不可欠」という定性表現だけである。**
   → 🔴 **したがって「自給率」を数値で語ることはできない。**
   → **VDC / HVE の認証範囲が「Groupe の区画の全体」である以上、
   その区画が全体の何割かは、認証の意味を測るうえで本質的な数字である。**

4. 🔴 **マロラクティック発酵の有無、および木樽の使用／不使用。**
   **公式サイト FR・EN、フィッシュ・テクニック 5 点のいずれにも記述が無い。**
   🔴 **canonical は両レコードで「マロラクティック発酵あり」と断定しているが、出典が無い。**
   → **メゾンへの照会か、輸入元の技術資料（producer authorship が確認できるもの）が要る。**

5. ⚠️ **Groupe Laurent-Perrier のブランド体制（Salon / Delamotte / Champagne de Castellane）を
   公式に取得可能な形で確認できていない。**
   **Euronext 上の公式財務コミュニケが JS 描画で本文を返さなかった。**
   → **これは `CAT-3`（ブランド軸）の管轄であり、OBP 行も無い。本書の担当外として据え置く。**

6. ⚠️ **`Grand Siècle Alexandra Rosé` という歴史的な表記が実在したかどうか。**
   **現行の公式サイトでは `Alexandra Rosé Millésimé` であり、Grand Siècle とは別項目として並列に置かれている。**
   **過去のラベルやプレス資料に `Grand Siècle Alexandra` が存在したかは、本調査では確認も否定もできていない。**
   → **OBP の印字は `'Alexandra,' Brut` のみで Grand Siècle を含まないため、実務上の影響は無い。**

7. ⚠️ **`Grand Siècle Itération Nº26` のセパージュが公式内で `58/42` と `52/48` に割れている。**
   **フィッシュ・テクニックとリリース記事と製品ページ見出しが `58/42`、
   製品ページ本文ブロックのみ `52/48`（かつ村が 8 ではなく 11）。**
   **本文ブロックが旧 itération の残存である可能性が高いが、断定していない。**

8. ⚠️ **`Cuvée Rosé` のマセラシオン時間（48–72h / 48h）と remontage 頻度（1 日 2 回 / 8 時間ごと）が
   公式内で食い違う。** **どちらが現行かは未確定。**

9. ⚠️ **`Cuvée Rosé` と `Alexandra` に公式フィッシュ・テクニックが存在しない。**
   **ドザージュ・デゴルジュマン・アルコール度数がこの 2 本については永久に埋まらない可能性がある。**
   → **輸入元の技術資料（producer authorship 確認つき）か、実ボトルの裏ラベルが要る。**

10. ⚠️ **`Harmony` が FR の sitemap に存在せず EN / DE / ES / JA にのみ存在する。**
    **FR 市場での取り扱いの有無は不明。OBP 行は無い。**

11. 🔴 **物理ラベル確認タスク —— OBP 行 1 と行 2 のボトルのラベル表記。**
    **メニューは `Grand Siècle Grande Cuvée No. 27 / No. 26` と印字しているが、
    公式の表記は `Grand Siècle Itération Nº27 / Nº26` である。**
    → **実ボトルのラベルがどちらの表記を持つかを確認したい。**
    **これは「メニューの誤植」か「特定市場向けラベルの実在」かを分ける唯一の証拠である。**
    ⚠️ **確認できるまで、staff はメニューの印字ではなく公式の `Itération Nº` を用いて説明する。**
