# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 15 件存在する。**
> **928 レコードの export 全体を機械走査し、`producer` フィールドが `Dom Pérignon` であるレコードが
> 15 件（`name` は 6 種類）であることを実測した。OBP は 3 行。**
> 🔴 **そして OBP 3 行のすべてに、キュヴェ名もヴィンテージも一致する canonical レコードが実在する。**
> 🔒 **canonical も `REGISTER.md` も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **生産者自身の公式資料で確認**（`www.domperignon.com` 本体。**本調査では法務・環境表示ページのみが読めた**）
> `🏛` **公的登録簿／規制一次資料** —— **AOC Champagne 明細書（arrêté AGRT2230908A / 2024年1月25日 homologation）**、
>    **`recherche-entreprises.api.gouv.fr`（RNE / INSEE）**、**Agence Bio 事業者登録簿**
> `📄` **生産者著作だが生産者ドメイン外で配信されている資料**（**本書では Wayback Machine が捉えた
>    `www.domperignon.com` 自身の旧ページ。埋め込みの mentions légales で真正性を確認済み**）
> `⚠️` **出典間で食い違い／出典が沈黙している／第三者の主張であって未確認**（**LVMH の Maison 頁を含む。
>    LVMH は所有者であって生産者ではない**）
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-06 ／ 一次資料: **`https://www.domperignon.com/`**
> 走査元: **`robots.txt` → `sitemap.xml` / `sitemap2.xml`（約 550 KB）**、**`fr-fr` URL 全一覧**、
> **Wayback Machine CDX（2015 / 2017 / 2019 / 2021 / 2022 の各時点、および個別製品頁 8 本）**、
> 🏛 **`recherche-entreprises.api.gouv.fr`（SIREN `509553459`）**、🏛 **Agence Bio（n° bio `18379`）**、
> 🏛 **BO-agri（AOC Champagne 明細書 PDF 2 本）**、⚠️ **`lvmh.com` の Dom Pérignon Maison 頁 5 本**
>
> ---
>
> 🔴 **本ドシエ最大の収穫 ① —— OBP 3 行すべてに、canonical の「正解レコード」が最初から存在していた。**
> **intake の evidence は 3 行とも「`'Dom Pérignon'` の canonical キュヴェ 2 件に一致無し」と書く。
> しかし canonical は `producer == 'Dom Pérignon'` を 15 件保持しており、しかも——**
>
> | OBP 行 | 存在する canonical レコード | intake の判定 |
> |---|---|---|
> | **1. `Brut` / VT 2015** | 🔴 **`dom-perignon-2015`**（`name='Dom Pérignon Vintage'` / `vintage='2015'`） | ⚠️ **`unresolved` / `confidence 0.0` / `proposed_canonical_cuvee_id: null`** |
> | **2. `Brut` / VT 2013** | 🔴 **`dom-perignon-2013`**（`name='Dom Pérignon Brut'` / `vintage='2013'`） | ⚠️ **同上** |
> | **3. `'Plénitude 2,' Brut` / VT 2003** | 🔴 **`dom-perignon-p2-2003`**（`name='Dom Pérignon Plénitude 2'` / `vintage='2003'`） | ⚠️ **同上** |
>
> 🔴 **これは Krug で観測された「evidence が canonical を過小申告する」形（`CDX-1` の逆）の、より強い事例である。**
> **Krug は 2 件と書いて実際は 13 件だった。ここは 2 件と書いて実際は 15 件で、
> かつ 3 行とも正解が実在するのに 1 行も当たっていない。**
> → §Canonical Conflict ①（**1 節で記録し、深追いはしない**）
>
> 🔴 **本ドシエ最大の収穫 ② —— `Brut` はキュヴェ名ではない。そしてメニューは defective ではない。**
> 🔴 **メゾン自身の公表物 397 KB（旧サイト全頁テキスト・現サイト・法務頁・環境表示頁）を機械走査し、
> 文字列 `Brut` が 1 件も現れないことを実測した。**
> 🔴 **さらに 🏛 AOC Champagne 明細書（2024年1月25日 homologation）にも `brut` は 1 件も現れない。
> 明細書が定めるのは「prise de mousse 後の発酵性糖分 10 g/L 以下」——ドザージュ前の値であって、
> `Brut` という表示区分ではない。**
> 🔴 **メゾン自身の製品名は環境表示頁（現サイト・仏 AGEC 法の法定開示）で確認できる：
> `Dom Pérignon 75cl Vintage Millésimé` / `Vintage Plénitude 2` / `Vintage Plénitude 3` /
> `Rosé Vintage Plénitude 1`。`Brut` はどの SKU 名にも入っていない。**
> → 🔴 **しかしこれは「メニューが壊れている」ことの証明ではない。`Brut` は瓶のラベルに刷られる
> 残糖表示（sugar-content term）である可能性が高く、本調査はラベル現物を 1 枚も読めていない。**
> **`_parts.label: null` は「キュヴェ名の印字が無い」の正しい検出であり、メニューは
> 製品名（`Dom Pérignon Vintage`）ではなく糖度表示を印字している、というだけの可能性がある。**
> → §Important Cuvées 行 1・2 ／ Open Questions 1（**実ボトル案件**）
>
> 🔴 **本ドシエ最大の収穫 ③ —— P2 が「別キュヴェ」か「同一ワインの後期リリース」かは、メゾンの言葉で決着する。**
> 📄 **「**For each vintage and from its inception, a limited number of bottles are set aside in the cellars,
> predestined for longer maturation.**」**
> 📄 **「**Dom Pérignon Vintage 2003 Plénitude 2 offers a rereading of history and a second life of the
> Vintage 2003.**」**
> → 🔴 **すなわち P2 は「同じ 2003 年のワインを、仕込みの時点から取り分けて長く寝かせ、後に出したもの」。
> 別の年でも別のアッサンブラージュでもない。メゾンは `second life`（第二の生）と呼ぶ。**
> ⚠️ **これは `V-1` / `CDX-8` の同一性軸そのものである。モデル上の帰結は 1 行だけ記す：
> 「`cuvée × vintage` では足りず、`cuvée × vintage × plénitude（リリース段階）` の粒度が要る」。
> 番号は開かない。** → §Canonical Conflict ③
>
> 🔴 **本ドシエ最大の収穫 ④ —— 有機は「ヴィンテージごとに見る」と、3 本とも何も言えないことが確定する。**
> 🏛 **Agence Bio 登録簿：MHCS（n° bio `18379`）の `datePremierEngagement` は `2020-10-15`。**
> 🔴 **OBP の 3 ヴィンテージは 2015 / 2013 / 2003 —— すべてこの日付より前の収穫である。**
> 🔴 **したがって 3 本については、有機についても非有機についても、何も主張できない。**
> **さらに登録上の区分は `Grossistes`（卸）、活動は `Préparation` / `Distribution` / `Importation` であり、
> `Production végétale`（栽培）ではない。** → §Farming
>
> ⚠️ **調査上の制約 ① —— 現行サイトは全頁が年齢ゲートである。**
> 🔴 **`sitemap` から取得した 187 頁のうち、法務 4 頁を除く 183 頁がすべてバイト単位で同一の
> ゲート用シェル（1,067 文字）を返した。製品情報は 1 文字も含まれない。**
> **これは §70% ルールの「6 つの形」でいえば「ドメインは生きているが本文が到達不能」であり、
> gap でも publishing 停止でもない。**
> → **本書の製品記述はすべて Wayback Machine が捉えた同ドメインの旧ページ（`📄`）に依る。
> 各キャプチャに埋め込まれた mentions légales で真正性を個別に確認した。**
>
> ⚠️ **調査上の制約 ② —— Vintage 2015 についてのメゾン自身の記述を 1 文も取得できていない。**
> 🔴 **`/fr-fr/product/vintage/2015` は現行サイトに実在するが年齢ゲートの向こうにあり、
> Wayback にも本文キャプチャが無い。2013 と 2003 は取れたが、2015 は取れなかった。**
> → 🔴 **OBP 1 行目（$600）について、年の性格をメゾンの言葉で語ることはできない。** → Open Questions 3
>
> ⚠️ **調査上の制約 ③ —— 🏛 TTB Public COLA Registry は本調査でも bot 防御でゲートされていた。**
> **`TSPD` / `bobcmn` および `captcha` の実在を確認。ルールに従い突破は試みていない。**
> **⚠️ ゲートされたことは「ラベルが存在しない」ことの証拠ではない。**
>
> ⚠️ **調査上の制約 ④ —— 🏛 INAO 側は取得できていない。**
> **`inao.json` / `inao_prod.html` はいずれも INAO サイトのエラー頁（Drupal 404）であった。
> 代替として BO-agri 掲載の明細書 PDF 本体を用いている。こちらは一次資料として十分である。**

---

## Identity

| | |
|---|---|
| **OBP 印字（producer heading）** | 🔍 **`Dom Pérignon`** |
| **Canonical Name** | 🔍 **`Dom Pérignon`**（15 レコードすべての `producer` 値） |
| 🔴 **法人名** | ✅ 🏛 🔴 **`MHCS`**（正式表記 `M H C S`）。<br>✅ **現行 mentions légales（2023年6月更新）：「**Le site Internet www.domperignon.com … est édité par MHCS, société anonyme : capital social : 433 193 789 euros ／ numéro d'immatriculation : 509 553 459 RCS Reims ／ numéro de TVA : FR 44 509 553 459 ／ adresse du siège social : 9 Avenue de Champagne 51200 EPERNAY, France**」**<br>🏛 **RNE/INSEE：`SIREN 509553459` ／ `SIRET`（本社）`50955345900033` ／ TVA `FR44509553459` ／ 本店 `9 AVENUE DE CHAMPAGNE 51200 EPERNAY` —— 完全一致** |
| 🔴 **法形態の変遷** | ⚠️ 🔴 **出典が食い違うのではなく、時期が違う。両方記録する。**<br>📄 **2018年4月4日版 T&C（旧サイト）：「**MHCS, a French company (**société en commandite simple**)**」**<br>✅ **2023年6月版 mentions légales：「**MHCS, **société anonyme**」**<br>🏛 **RNE の現行 `nature_juridique` = `5599`（SA à conseil d'administration）→ 現在は SA。**<br>⚠️ **旧版は資本金を同一文書内で `433 193 798` と `433 193 789` の 2 通りに書いている。現行版は `433 193 789`。本書は現行値を採る** |
| 🔴 **設立・規模（法人）** | 🏛 **企業設立 `2008-12-12`／本社事業所 `2009-12-21`。主活動 `11.02A`（発泡性ワイン製造）。<br>企業区分 `GE`（大企業）。事業所 17、うち稼働 12。**<br>🏛 🔴 **2024年度：売上高 `2,591,647,130 €` ／ 当期純利益 `413,108,331 €`**<br>⚠️ **これは MHCS 全体の数値であって Dom Pérignon 単独ではない** |
| 🔴 **企業グループ** | 🏛 🔴 **登記上の取締役に法人が 3 社入っている：`MOET HENNESSY`（SIREN `338228414`）／`MOET HENNESSY INVESTISSEMENTS`（`429646920`）／`SOCIETE JAS HENNESSY & CO`（`905620035`）。**<br>⚠️ **LVMH は自社サイトで Dom Pérignon を Wines & Spirits 部門の Maison として掲げる。**<br>⚠️ **出資比率は公的登録簿にも生産者サイトにも記載が無い。本書は主張しない** |
| 🔴 **登記上の役員** | 🏛 **`GUIONY Jean-Jacques`（1961-12生）Président du conseil d'administration et directeur général ／ `DUFOUR Frédéric`（1962-05生）Directeur général délégué ／ `BRIFFOTEAUX Hervé`（1967-10生）Administrateur。**会計監査人 `FORVIS MAZARS SA`<br>⚠️ 🔴 **現行 mentions légales は Directeur de Publication を「**Jaques Giraco, Directeur Général**」とする。この氏名は 🏛 登記簿の役員一覧に存在しない。**📄 **2018年版は「**Sonia Voskoboinikoff, International Marketing Director of Dom Perignon**」であった。**<br>→ **両方記録し、いずれも断定しない。サイト上の「発行責任者」と会社法上の代表者は別概念である** |
| 🔴 **Chef de Cave** | 📄 🔴 **`Vincent Chaperon`。**メゾンの言葉：「**On January 1, 2019 Vincent Chaperon became the Dom Pérignon Chef de Cave. He succeeded Richard Geoffroy, with whom he has been working closely since 2005.**」<br>⚠️ **本調査で読めた生産者著作は 2022 年以前のキャプチャである。2026 年時点での在任を生産者ドメインで再確認できていない**（⚠️ LVMH の Maison 頁は現在も Chaperon を Chef de Cave として掲げる） |
| **前任 Chef de Cave** | 📄 **`Richard Geoffroy`。**「**Between 1990 and 2009 Richard Geoffroy declared no fewer than 15 vintages in the cellars of Dom Pérignon… His interpretations of the Dom Pérignon vision gave birth to the creation of the Plénitudes.**」 |
| 🔴 **創業（メゾンの自己記述）** | 📄 🔴 **1668年。**「**In 1668, Dom Pierre Pérignon, a young Benedictine monk is appointed procurator at the Abbey of Hautvillers, overlooking Champagne.**」<br>⚠️ 🔴 **これは「メゾンの創業年」ではなく、メゾンが自ら掲げる `THE FOUNDING MYTH`（創設神話）の年である。メゾン自身がその見出しを使っている。混ぜない** → §History |
| **Aliases** | 🔍 **`Dom Pérignon`**（OBP 印字・canonical `producer` 値）／✅ **`MHCS`**（法人）／📄 **`P2`**（2019年頃まで自社が使っていた略称。→ §Important Cuvées 行 3） |
| **canonical id** | 🔍 🔴 **15 件。**うち OBP に対応するのは **`dom-perignon-2015` / `dom-perignon-2013` / `dom-perignon-p2-2003`** の 3 件 → §Canonical Conflict |

---

## Overview

📄 **シャンパーニュ、エペルネ。メゾンの自己規定は 1 行に尽きる ——「Dom Pérignon is vintage champagne only.」**
📄 **「**Dom Pérignon is driven by one unyielding, absolute commitment: every vintage bears witness to a single year.**」**
📄 🔴 **そしてその裏返しを、メゾン自身が同じ頁で明言している：
「**Dom Pérignon never compromises on this creative ideal – choosing to remain silent and not declare a vintage
when a year falls short of this ideal.**」**
→ 🔴 **「良い年にだけ造る」ではなく「基準に満たない年は宣言しないことを選ぶ（remain silent）」がメゾンの言い方である。**

📄 **各ヴィンテージの位置づけも定型文で公表されている：
「**Each vintage is a creation, singular and unique, that expresses both the character of the year, and the
character of Dom Pérignon. After at least eight years of elaboration in the cellars, the wine embodies the
perfect balance of Dom Pérignon, the Plénitude of harmony.**」**

🔴 **ここで `Plénitude`（プレニチュード）という語が最初に出る。メゾンの体系では熟成の「段階」を指す。**
📄 **Richard Geoffroy の業績としてメゾンが挙げるのが、まさにこの概念の創出である：
「**gave birth to the creation of the Plénitudes and their vocation: express the successive plateaus of a
champagne as it matures**」**

⚠️ **所有者 LVMH は自社サイトで熟成期間を 3 段階の数字で掲げる：
`8 YEARS OR MORE TO ELABORATE VINTAGE` / `12 YEARS OR MORE TO ELABORATE VINTAGE ROSÉ` /
`15 YEARS OR MORE TO ELABORATE PLÉNITUDE 2`。**
🔴 **このうち `8年` と `15年` は生産者自身の記述でも裏づけが取れている**（→ §Important Cuvées）。

🔍 🔴 **THÉSEUS における状態は「3 行に対して 15 レコード、うち 3 行とも正解レコードが実在、しかし 3 行とも未解決」。
Ridge が「gap（当てる先が無い）」だったのに対し、Dom Pérignon は「当てる先はあるのに当たっていない」型である。
両者は remedy が正反対であり、混同すると誤った修正をすることになる。**

---

## History

### Foundation（メゾンが `THE FOUNDING MYTH` と呼ぶもの）

| 年 | 出来事 | 典拠 |
|---|---|---|
| 🔴 **1668** | 🔴 **ベネディクト会修道士 Dom Pierre Pérignon が、シャンパーニュを見下ろす Hautvillers 修道院の procurator（財務管理者）に任じられる。** | 📄 **公式 `SPIRIT` 頁：「**In 1668, Dom Pierre Pérignon, a young Benedictine monk is appointed procurator at the Abbey of Hautvillers, overlooking Champagne.**」** |
| **—** | **「ワインをシャンパーニュへと変える」試みを通じ、シャンパーニュの原初的・神秘的な創造行為を体現した人物と位置づけられる。** | 📄 **「**Successfully endeavoring to transmute wine into champagne, Dom Pierre Pérignon embodies champagne's original and mystical act of creation.**」** |
| **—** | **47年間「世界最高のワイン」を造ろうとした、と所有者側は記す。** | ⚠️ **LVMH Maison 頁：「**For 47 years, he worked to make the "best wine in the world".**」**（**生産者ドメインでは「47年」の数字を確認できていない**） |

⚠️ 🔴 **重要な区別 —— メゾンはこの節を `THE FOUNDING MYTH`（創設神話）という見出しで語っている。
「1668年創業のシャンパーニュ・メゾン」とは書いていない。**
🏛 **法人 MHCS の登記上の設立は `2008-12-12` であり、これはまったく別の事実である。**
❓ **ブランドとしての Dom Pérignon の最初のヴィンテージ発売年を、生産者ドメイン上で確認できていない。** → Open Questions 4

🔴 🏛 **なお Hautvillers は、AOC Champagne 明細書が列挙する `premier cru` の 41 コミューンの 1 つである
（`grand cru` 17 コミューンには含まれない）。修道院の所在地であって、grand cru の村ではない。**

### Generations（Chef de Cave の系譜。メゾンが公表している唯一の「世代」である）

| 年 | 出来事 | 典拠 |
|---|---|---|
| **1990–2009** | 🔴 **Richard Geoffroy が 15 のヴィンテージを宣言。** | 📄 **「**Between 1990 and 2009 Richard Geoffroy declared no fewer than 15 vintages in the cellars of Dom Pérignon**」** |
| **—** | 🔴 **Geoffroy が `Plénitudes` の概念を創出。** | 📄 **「**His interpretations of the Dom Pérignon vision gave birth to the creation of the Plénitudes and their vocation: express the successive plateaus of a champagne as it matures.**」** |
| **2005** | **Vincent Chaperon が Geoffroy のもとで働き始める。** | 📄 **公式 News 頁** |
| **2005–2018** | 🔴 **Chaperon は Geoffroy と 13 の収穫を共にし、4 つのヴィンテージを共同で宣言した —— 宣言順に `2005`, `2006`, `2009`, そして `2008`。** | 📄 **「**Vincent Chaperon has taken part in thirteen harvests and declared four vintages with him. They are, in the order in which they were declared, the 2005, 2006, 2009 and, most recently, 2008.**」**<br>🔴 **宣言の順序が年号順ではない（2009 が 2008 より先）。P1 のリリース設計そのものが年号順ではないことの、メゾン自身による証拠である** |
| 🔴 **2019-01-01** | 🔴 **Vincent Chaperon が Chef de Cave に就任。13 年の随伴を経ての承継。** | 📄 **「**On January 1, 2019 Vincent Chaperon became the Dom Pérignon Chef de Cave.**」／✅ 公式 `SPIRIT` 頁「after a thirteen-year apprenticeship alongside Richard Geoffroy」** |

🔴 **OBP 3 行はちょうどこの承継をまたいでいる。**
**2003（P2）と 2013 は Geoffroy が宣言した年、2015 は Chaperon が Chef de Cave になった後にリリースされた年である。**
⚠️ **ただし「2015 を誰が宣言したか」を生産者ドメインで確認できていない。断定しない。**

### 呼称の変遷（🔴 本書が Wayback で実測した）

| 時点 | サイト上のナビゲーション表記 | 典拠 |
|---|---|---|
| **2017-01-01** | **`P2`**（トップに「THE ULTIMATE DOM PERIGNON / Discover P2」） | 📄 **Wayback キャプチャ** |
| **2019-01-01** | **`P2`** | 📄 **同上** |
| 🔴 **2021-06-01** | 🔴 **`Plénitude 2`**（「Plénitude 2 / Dom Pérignon elevated to its second life」） | 📄 **同上** |
| **現行** | **`Plénitude 2`**（URL は `/product/plenitude-2/…`） | ✅ **現行 `sitemap` / `fr-fr` URL 一覧** |

→ 🔴 **すなわち「P2」から「Plénitude 2」への表記変更は 2019〜2021 年の間に起きている。
OBP が `'Plénitude 2,'` と印字しているのは、現行のメゾン表記どおりである。** → §Important Cuvées 行 3

---

## Location

| | |
|---|---|
| **Country** | **France**（Champagne） |
| 🔴 **AOC** | 🏛 🔴 **`Champagne`。**明細書：「**Seuls peuvent prétendre à l'appellation d'origine contrôlée " Champagne ", **reconnue initialement par le décret du 29 juin 1936**, les vins répondant aux dispositions du présent cahier des charges ainsi qu'aux dispositions de la **loi du 6 mai 1919** relative à la protection des appellations d'origine.**」<br>🏛 **現行明細書は `arrêté du 25 janvier 2024` で homologué、JORF `28 janvier 2024` 公示、BO du MASA `22/02/2024` 掲載（整理番号 `AGRT2230908A`）** |
| 🏛 **産品の型** | **「**L'appellation d'origine contrôlée " Champagne " est réservée aux vins mousseux blancs ou rosés.**」** |
| 🔴 **法人所在** | ✅ 🏛 🔴 **`9 avenue de Champagne, 51200 Épernay`（Marne）。**<br>**現行 mentions légales・🏛 RNE・🏛 Agence Bio の 3 経路で一致する。緯度経度 `49.043787 / 3.960370`** |
| 🏛 **もう 1 つの登録住所** | 🏛 **`Rue des Mardilles, Parc Industriel, 51520 Recy`。**Agence Bio 登録簿が MHCS の「Lieux d'activité」として保持する（Châlons-en-Champagne 近郊） |
| 🔴 **畑** | ❓ 🔴 **メゾンは自社の畑・区画・村を一切公表していない。**<br>🔴 **本調査で読めた生産者著作のいずれにも、村名・区画名・所有面積・grand cru 比率の記述が無い。**<br>→ 🔴 **卓上で「どの村のブドウか」を語ることはできない。** → §Staff Notes ⚠️ ③ |

### 🏛 AOC Champagne 明細書から言えること（**メゾン固有ではないが、3 本すべてに法的に当てはまる**）

| 項目 | 🏛 明細書の規定 |
|---|---|
| 🔴 **主要品種** | **`Arbane B` / `Chardonnay B` / `Meunier N` / `Petit meslier B` / `Pinot blanc B` / `Pinot gris G` / `Pinot noir N` の 7 品種。**<br>**＋「適応目的の関心品種」`Voltis B`（栽培面積の 5% 以下、INAO・ODG との協定締結が条件）** |
| **アッサンブラージュの構成比** | **主要品種の合計が 90% 以上、`Voltis B` は 10% 以下** |
| **grand cru の村** | 🔴 **17 コミューン：`Ambonnay, Avize, Aÿ, Beaumont-sur-Vesle, Bouzy, Chouilly, Cramant, Louvois, Mailly-Champagne, Le Mesnil-sur-Oger, Oger, Oiry, Puisieulx, Sillery, Tours-sur-Marne, Verzenay, Verzy`** |
| **premier cru の村** | **41 コミューン。🔴 `Hautvillers`・`Cumières`・`Dizy`・`Pierry`・`Vertus` などを含む** |
| 🔴 **tirage の解禁** | **「**Le tirage en bouteilles dans lesquelles s'effectue la prise de mousse ne peut avoir lieu qu'à partir du 1er janvier de l'année qui suit celle de la récolte.**」（収穫翌年の 1 月 1 日以降）** |
| 🔴 **糖分** | **「**Les vins présentent, après prise de mousse, une teneur en sucres fermentescibles (glucose et fructose) inférieure ou égale à 10 grammes par litre.**」**<br>🔴 **これは prise de mousse 後＝ドザージュ前の値である。`Brut` という表示区分の規定ではない** |
| 🔴 **最低熟成期間** | 🔴 **非ミレジメ：tirage から `15 か月`。**<br>🔴 **ミレジメ（millésimés）：tirage から `36 か月`。**<br>→ 🔴 **法定下限は 3 年。メゾンが自ら課す `8年以上` はこれを大きく上回る** |
| 🔴 **ミレジメの上限** | 🔴 **「**les volumes de vins présentés avec l'indication du millésime (millésimés) sont inférieurs ou égaux à **80 %** des volumes de vin de l'année considérée, achetés ou produits par l'opérateur**」**（当該年の 80% 以下） |
| 🔴 **ミレジメの表示場所** | 🔴 **「**En cas d'indication du millésime, celui-ci figure sur le bouchon**」——**年号はコルクに刻まれる。**さらに送り状・出荷書類にも記載義務がある | 
| **その他** | **木片（morceaux de bois）の使用は禁止。補糖後の総アルコール度数は prise de mousse 後 13% を超えない** |

🔴 **`brut` の語は、この明細書 28 頁のどこにも 1 件も現れない（機械走査で確認）。** → §Important Cuvées 行 1・2

---

## Farming

### Organic

🏛 🔴 **Agence Bio 事業者登録簿（`numeroBio 18379`、SIRET `50955345900033` = MHCS 本社）**

| 項目 | 🏛 登録簿の値 |
|---|---|
| **事業者名** | **`M H C S`（通称 `MHCS`）** |
| 🔴 **最初の関与日** | 🔴 **`datePremierEngagement: 2020-10-15`** |
| **認証機関 ①** | **`FR-BIO-10` Bureau Veritas Certification France —— 関与 `2020-10-19`、**🔴 **`ARRETEE`（停止）`2023-10-31`** |
| **認証機関 ②** | **`FR-BIO-01` Ecocert France —— 関与 `2022-07-02`、`ENGAGEE`（関与中）** |
| 🔴 **登録区分** | 🔴 **`Grossistes`（卸売）** |
| 🔴 **登録活動** | 🔴 **`Préparation`（調製）／`Distribution`（流通）／`Importation`（輸入）。**<br>🔴 **`Production végétale`（栽培）は登録されていない** |
| **生産品目** | **`11.02 Vins de raisin` —— 状態 `AB`、管理参照年 `2026`。ほか卸売コード 3 件** |
| **混在（mixité）** | **`Oui`（有機と非有機を併営）** |
| **公表サイト** | 🔴 **`siteWebs: []`（空）** |
| **登録更新** | **`2025-06-30`** |

🔴 **OBP 3 本への当てはめ（ヴィンテージごとに 1 本ずつ確認した）**

| OBP 行 | VT | 収穫年と関与日の関係 | 判定 |
|---|---|---|---|
| **1. Vintage** | **2015** | 🔴 **収穫は関与日（2020-10-15）より 5 年前** | 🔴 **有機についても非有機についても、何も言えない** |
| **2. Vintage** | **2013** | 🔴 **同 7 年前** | 🔴 **同上** |
| **3. Plénitude 2** | **2003** | 🔴 **同 17 年前** | 🔴 **同上** |

🔴 ⚠️ **「関与日が収穫より後である」ことは、「そのボトルが有機でない」ことの証明ではない。
同時に「有機である」ことの根拠にも一切ならない。どちらの向きにも使わない。**
🔴 ⚠️ **さらに登録区分が `Grossistes` / 活動が `Préparation・Distribution・Importation` である以上、
この登録は「MHCS が有機ブドウを栽培している」ことを示すものですらない。**
→ §Staff Notes ⚠️ ④

### Biodynamic

🔴 ⚠️ **Biodyvin の会員一覧頁を取得し、`MHCS` / `Moët` / `Dom Pérignon` / `Hautvillers` の
いずれの文字列も 0 件であることを機械走査で確認した。**
🔴 ⚠️ **Demeter のサイトマップにも同 4 語は 0 件である。**
🔴 ⚠️ **生産者著作のいずれにも `biodynamie` / `biodynamic` / `Demeter` の語が現れない。**
→ **ビオディナミは主張しない。**

### Sustainable

⚠️ 🔴 **本調査で読めた生産者著作に、サステナビリティ認証（`VDC`、`HVE`、`Terra Vitis` 等）の
記述は 1 件も無い。**
✅ **ただし現行サイトの環境表示頁（`décret 2022-748 du 29 avril 2022` / loi AGEC 13-I に基づく法定開示）は、
全 SKU について包装の環境特性を逐一開示している。これは唯一取得できた、現行サイト由来の実質的な公式情報である。**

| 🔴 OBP 3 本に関係する SKU | ✅ 公式開示 |
|---|---|
| **`Dom Pérignon 75cl Vintage Millésimé`** | **瓶：`entièrement recyclable`（完全にリサイクル可能）／再生材 `87%` 以上** |
| **`Dom Pérignon 75cl Vintage Plénitude 2`** | **瓶：`majoritairement recyclable`（主としてリサイクル可能）／再生材 `87%` 以上／**⚠️ **`COFFRET`（化粧箱）は `n'est pas recyclable`（リサイクル不可）・再生材なし** |

⚠️ 🔴 **`Vintage Millésimé` の瓶が `entièrement`、`Vintage Plénitude 2` の瓶が `majoritairement` と
異なる記述になっている。メゾン自身の表記どおりであり、本書は理由を推測しない。**
⚠️ **これは包装の性質の開示であって、栽培・醸造のサステナビリティ認証ではない。混ぜない。**

### Other（メゾンが公表する「成分」）

🔴 📄 **メゾンが成分について公表しているのは、`GUIDELINES FOR STORING CHAMPAGNE AND COMPOSITION` 頁の
1 行だけである：**
📄 **「**COMPOSITION —— All our champagnes contain sulphites.**」**
→ 🔴 **これで全部である。ドザージュ量も、品種比率も、収穫日も、デゴルジュマン日も、
本調査で読めた生産者著作のどこにも記載が無い。** → §Staff Notes ⚠️ ①

---

## Winemaking

### 📄 メゾンの原則

📄 🔴 **「**Dom Pérignon is vintage champagne only.**」——**ノン・ヴィンテージを造らない。**
📄 🔴 **宣言しない自由を明示：「**Dom Pérignon never compromises on this creative ideal – choosing to remain
silent and not declare a vintage when a year falls short of this ideal.**」**
⚠️ **所有者 LVMH の記述：「**Dom Pérignon is always an assemblage, forming the foundation of the Dom Pérignon
style. It is guided by timeless principles that have always taken precedence over winemaking techniques and
their evolution.**」**
⚠️ **同：「**During the time of active maturation on the lees, in the darkness of the cellars, the aesthetic and
sensory values of each vintage are played out: precision, intensity, touch, minerality, and complexity.**」**
（🔴 **この 5 語 —— precision / intensity / touch / minerality / complexity —— は所有者側の記述であり、
生産者ドメインでは確認できていない。卓上で「メゾンが掲げる 5 つの価値」として語らない**）

### 🔴 熟成期間（**3 段階。数字はすべて出典つき**）

| 段階 | 期間 | 典拠 |
|---|---|---|
| 🔴 **Vintage（第 1 のプレニチュード）** | 🔴 **`8 年以上`** | 📄 🔴 **生産者：「**After at least eight years of elaboration in the cellars, the wine embodies the perfect balance of Dom Pérignon, the Plénitude of harmony.**」**<br>⚠️ **LVMH：`8 YEARS OR MORE TO ELABORATE VINTAGE`（一致）** |
| **Rosé** | **`12 年以上`** | ⚠️ **LVMH のみ（`12 YEARS OR MORE TO ELABORATE VINTAGE ROSÉ`）。生産者ドメインで未確認**（OBP に該当行なし） |
| 🔴 **Plénitude 2** | 🔴 **`約 15 年`** | 📄 🔴 **生産者：「**After **close to 15 years** of slow transformation in the cellars…**」（P2 2003 頁）／「**A slow and controlled transformation takes place over **almost fifteen years**…**」（P2 2000 頁）**<br>⚠️ **LVMH：`15 YEARS OR MORE TO ELABORATE PLÉNITUDE 2`（一致）** |
| **Plénitude 3** | ❓ **本調査では数値を取得できていない** | **製品としては現行サイトに `Vintage Plénitude 3` の SKU が実在する**（OBP に該当行なし） |

🔴 ⚠️ **canonical は P2 を「16+ years on lees」とするが、メゾンは 2 頁で一貫して「約 15 年」と書く。** → §Canonical Conflict ②

### 🔴 Plénitude 2 の仕組み（**メゾン自身の説明。逐語**）

📄 🔴 **「**For each vintage and from its inception, a limited number of bottles are set aside in the cellars,
predestined for longer maturation. With this extra time, the inner activity in the bottle increases.
The yeast transfers its energy to the wine... a mysterious transfer of life. Dom Pérignon is patiently
elevated to a new summit of expression. We call this elevation Plénitude 2, the second life of Dom Pérignon.**」**

🔴 **ここから読み取れる事実は 3 つで、いずれもメゾンの言葉に直接ある：**
1. 🔴 **取り分けは「from its inception」——仕込みの時点で行われる。後から選ぶのではない。**
2. 🔴 **本数は「a limited number of bottles」——限定である（数値は非公表）。**
3. 🔴 **長期熟成中に起きているのは「the yeast transfers its energy to the wine」——澱との接触である。**

❓ 🔴 **デゴルジュマン（澱抜き）の時期・回数・年月日は、本調査で読めた生産者著作のどこにも記載が無い。**
🔴 **「再デゴルジュマン」という語をメゾンは一度も使っていない。** → §Staff Notes ⚠️ ②

### ❓ 取得できなかった醸造情報（**すべて「メゾンが公表していない」であって「調べ漏れ」ではない**）

❓ **品種構成比（3 本とも）／ドザージュ量（3 本とも）／収穫日（3 本とも）／
発酵容器・マロラクティック発酵の有無／デゴルジュマン日／生産本数／アルコール度数。**
🔴 **これらはいずれも生産者著作・🏛 登録簿のどちらにも無い。本書は数値を一切書かない。**

---

## Style

### 📄 メゾン自身のテイスティングノート（**OBP 3 行のうち 2 行について逐語で存在する**）

#### 🔴 Vintage 2013（OBP 行 2）

📄 **`SEASONS`：「**The 2013 winemaking year proved a welcome reconnection with the glorious past of late
harvest vintages. After a cold, wet winter, spring was gray, quite cool and extremely rainy. The hot and dry
summer was particularly beneficial for the quality of the grapes.**」**
📄 **`NOSE`：「**The delicate nose unfolds in swaths of color. The green of eucalyptus, mint and vetiver, the
yellow-orange of mirabelle plums, apricot and orange blossom, the brown of pepper, cardamom and licorice
sticks, and finally silvery saline and toasty hues.**」**
📄 **`PALATE`：「**The mouthfeel is elegant, expressing luxuriant simplicity and precision. The attack is
enveloping and ethereal. The refined and silky foundation becomes more pronounced at the heart. The finish is
dominated by a salinity that leaves a deep sensation of consistency.**」**

🔴 **メゾンは 2013 を「遅摘みヴィンテージの輝かしい過去との、喜ばしい再会」と表現している。
「気候変動前の最後の 10 月収穫」ではない。この言い換えはメゾンの言葉ではない。** → §Canonical Conflict ②

#### 🔴 Vintage 2003 Plénitude 2（OBP 行 3）

📄 **年の位置づけ：「**2003 is a year that will remain forever the year that changed the history of Champagne.
A scorching summer imposed the **earliest harvest since 1822**, leading Dom Pérignon to interpret this unique
year with an approach inspired by intuition and forward-looking choices.**」**
📄 **ワインの位置づけ：「**Dom Pérignon Vintage 2003 Plénitude 2 offers a rereading of history and a second
life of the Vintage 2003, revealing an **insolent freshness**. The enveloping flow is magnified, an unabashed
embrace.**」**
📄 **`THE NOSE`：「**Out of the floral softness of lime tree emerges the grey, toasted, ashy minerality so
typical of Dom Pérignon. A taste of dried fruit – apricot – appears, then the candied fruitiness of raspberry
and fig. Unexpectedly, the freshness of lemon verbena, white pepper and rosemary rises for an instant, before
plunging into the darkness of spices and liquorice root.**」**
📄 **`THE PALATE`：「**This is a physical wine. It calls to you and draws you in, more tactile and vibrant than
aromatic. Like a wave, it is built on rhythm and breaks: first it unfolds, then envelops – generous and
structured – before withdrawing into a deep, dark verticality that slowly stretches towards a bitter, sapid
iodine sensation.**」**

🔴 **さらにメゾンは、同じ 2003 年の「第 1 のプレニチュード」のノートを Vintage Library に別途置いている。
2 つを並べると P1 → P2 の変化がメゾンの言葉だけで語れる（本ドシエで最も強い一手）：**

| | 📄 **Vintage 2003（P1）** | 📄 **Vintage 2003 Plénitude 2** |
|---|---|---|
| **口中** | **「**The wine is currently still physical. It is compelling, tactile and vibrant rather than aromatic. **The rhythm and tempo are more dominant than the melody.** At first mild and delicate, then strongly, confidently mineral, persistent, precise, with a refined bitterness, and an iodine, saline tang.**」** | **「**This is a physical wine… more tactile and vibrant than aromatic. **Like a wave, it is built on rhythm and breaks**: first it unfolds, then envelops – generous and structured – before withdrawing into a deep, dark verticality…**」** |
| **香り** | **「**The bouquet spirals through sweet, bright floral notes and the lively minerality so typical of Dom Pérignon, then notes of candied fruit, plants, **the incredible freshness of camphor leaf** and finally the dark hints of spices and liquorice root.**」** | **「**…the grey, toasted, ashy minerality so typical of Dom Pérignon… **the freshness of lemon verbena, white pepper and rosemary**… before plunging into the darkness of spices and liquorice root.**」** |
| 🔴 **共通する語** | 🔴 **`physical` / `tactile` / `vibrant` / `minerality` / `spices and liquorice root` / `iodine`** | 🔴 **同じ語彙が両方に出る。メゾンは「別のワイン」としては書いていない** |

📄 **2003 年の収穫（メゾンの記述）：「**After a particularly cold, dry and severe winter, the spring frosts of
**7 to 11 April** left a lasting mark in Champagne. Summer was immediately scorching, **the hottest for 53
years**. Anything that had miraculously escaped the frost and hail was subjected to intense heat until
harvest. The crop was perfectly ripe and healthy, like those of **1947, 1959 and 1976**.**」**

#### ⚠️ Vintage 2015（OBP 行 1）—— **メゾンの言葉が 1 文も取れていない**

🔴 ⚠️ **`/fr-fr/product/vintage/2015` は現行サイトに実在するが年齢ゲートの向こうにあり、
Wayback にも本文キャプチャが無い。**
🔴 **本書は 2015 年の天候・収穫・香味について何も書かない。**
⚠️ **取得できた 2015 関連の生産者・所有者情報は、包装の話だけである：**
⚠️ **LVMH（2024-10-31 公開）：「**Dom Pérignon has unveiled a Vintage 2015 Special Edition in collaboration
with the estate of Jean-Michel Basquiat… For this Special Edition Vintage 2015, Dom Pérignon chose Jean-Michel
Basquiat's masterpiece *In Italian* (1983). Dom Pérignon's shield fuses with Basquiat's iconic crown on the
label.**」**
🔴 ⚠️ **これは限定版パッケージの話であって、OBP の通常版 Vintage 2015 の中身の話ではない。混ぜない。**
→ **行 1 については、メゾンの「Vintage 全般」の定型文（vintage only / 8 年以上 / assemblage）までしか語れない。**

### 📄 メゾンによる供出・保管の指針（**卓上でそのまま使える。全 3 本共通**）

📄 **温度：`7 – 18°C`（`45 – 65°F`）。急激な温度変化を避ける。**
📄 **湿度：`70%` 以上（コルクの柔軟性と密度を保つ）。**
📄 **光：「**Champagne is particularly sensitive to light.**」**
📄 🔴 **圧力：「**There are 6 to 8 bars of pressure inside the bottle, i.e. three times the pressure in a car tyre.**」**
📄 🔴 **開栓：「**Do not sabre the bottle.**」——メゾン自身がサブラージュを明確に否定している。**
📄 🔴 **飲み頃について：「**All the bottles of champagne that we sell have been aged in our cellars and they can
be opened as soon as they are purchased.**」／「**There is no benefit in keeping champagne longer than the
recommended time.**」**
📄 **「**The cellaring time for vintage champagnes is longer. They may be opened between 7 and 10 years after
purchase, or even later than that.**」**

---

## Important Cuvées

### 🔴 まずメゾン自身の製品名（**現行サイトの法定環境表示頁が唯一の一次証拠**）

✅ 🔴 **`décret 2022-748`（loi AGEC 13-I）に基づく法定開示のため、メゾンは全 SKU 名を実名で列挙している。
これが「メゾンが自社製品を何と呼んでいるか」の、現行サイトから取れた唯一の直接証拠である。**

| ✅ メゾンの SKU 名（75cl） | 対応 |
|---|---|
| 🔴 **`Dom Pérignon 75cl Vintage Millésimé`** | 🔴 **OBP 行 1・2 に対応する製品** |
| 🔴 **`Dom Pérignon 75cl Vintage Plénitude 2`** | 🔴 **OBP 行 3 に対応する製品** |
| **`Dom Pérignon 75cl Vintage Plénitude 3`** | **（OBP になし）** |
| **`Dom Pérignon 75cl Rosé Vintage Plénitude 1` / `Plénitude 2` / `Rosé Vintage Millésimé`** | **（OBP になし）**🔴 **`Plénitude 1` という語が実在することの証拠** |

🔴 **この一覧のどこにも `Brut` は現れない。**

---

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 3 行。3 行とも `match_state = unresolved` / `producer_state = exact` / `cuvee_state = unresolved` / `confidence 0.0`**）

#### 🔴 行 1 —— `obp-beverage-2026-08:5cbde63539`
**印字 `Brut` / VT 2015 / $600 / `FRANCE | SPARKLING > CHAMPAGNE | BLENDS`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。**`/fr-fr/product/vintage/2015` が現行サイトに実在し、SKU 名は ✅ **`Dom Pérignon Vintage Millésimé`** |
| 🔴 **メゾンは何と呼ぶか** | 🔴 **製品名は `Dom Pérignon Vintage`（環境表示頁では `Vintage Millésimé`）。**<br>🔴 **`Brut` はメゾンの製品名ではない。**メゾンの公表物 397 KB を機械走査し、`Brut` は 0 件 |
| 🔴 **では `Brut` は何か** | 🔴 **キュヴェ名ではなく、残糖表示（sugar-content term）である可能性が高い。**<br>🏛 **AOC Champagne 明細書 28 頁にも `brut` は 0 件。明細書が定めるのは prise de mousse 後の発酵性糖分 `10 g/L` 以下（＝ドザージュ前）であり、表示区分ではない。**<br>❓ **`Brut` を定義する EU 規則の条文そのものは本調査で取得していない。本書は閾値の数値を書かない** |
| 🔴 ⚠️ **メニューは間違っているか** | 🔴 **判定しない。**`_parts.label` は正しく `null`（＝キュヴェ名の印字なし）であり、パーサは正確である。<br>🔴 **ラベル現物を 1 枚も読めていない以上、「メニューが誤ってカテゴリー語をキュヴェ名にした」（`CDX-15` 型）とは断定できない。**瓶に `BRUT` と刷られていれば、メニューはラベルを写しているだけである。<br>→ 🔴 **`3f-10`（パターンの存在は個々の行の証拠ではない）に従い、この行では判定を保留する。** → Open Questions 1 |
| 📄 **メゾンの言葉で言えること** | **「ヴィンテージのみを造る」「基準に満たない年は宣言しない」「セラーで 8 年以上」「常にアッサンブラージュ」** |
| ⚠️ **言えないこと** | 🔴 **2015 年の天候・収穫・香味。メゾンの記述を 1 文も取得できていない** |
| 🔍 **canonical** | 🔴 **`dom-perignon-2015` が実在する**（`name='Dom Pérignon Vintage'` / `vintage='2015'`）。**にもかかわらず未解決** → §Canonical Conflict ① |

#### 🔴 行 2 —— `obp-beverage-2026-08:5a8f29e841`
**印字 `Brut` / VT 2013 / $600 / `FRANCE | SPARKLING > CHAMPAGNE | BLENDS`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。**`/fr-fr/product/vintage/2013` が現行サイトに実在。📄 **旧サイトの `Vintage 2013` 頁も取得済み** |
| 🔴 **`Brut` の扱い** | 🔴 **行 1 と同じ。判定を保留する** |
| 📄 🔴 **年の性格（メゾンの言葉）** | 🔴 **「**The 2013 winemaking year proved a welcome reconnection with the glorious past of late harvest vintages. After a cold, wet winter, spring was gray, quite cool and extremely rainy. The hot and dry summer was particularly beneficial for the quality of the grapes.**」** |
| 📄 🔴 **香りと味わい** | 🔴 **香り・口中とも逐語で取得済み（→ §Style）。ユーカリ／ミント／ヴェチヴェール／ミラベル／杏／オレンジフラワー／胡椒／カルダモン／甘草、そして塩気とトースト香** |
| 📄 **メゾンの位置づけ** | **`Harmony achieved`（調和の達成）。これが Vintage（P1）の見出し語である** |
| ⚠️ **言えないこと** | ❓ **収穫日・品種比率・ドザージュ・デゴルジュマン日。いずれもメゾンが公表していない** |
| 🔍 **canonical** | 🔴 **`dom-perignon-2013` が実在する**（`name='Dom Pérignon Brut'` / `vintage='2013'`）。**にもかかわらず未解決**<br>⚠️ 🔴 **なお canonical はこの製品を `Dom Pérignon Brut` と呼び、2015 のほうを `Dom Pérignon Vintage` と呼んでいる。同じ製品ラインに 2 つの名前がある** → §Canonical Conflict ② |

#### 🔴 行 3 —— `obp-beverage-2026-08:eb2f3e1d35`
**印字 `'Plénitude 2,' Brut` / VT 2003 / $1,800 / `FRANCE | SPARKLING > CHAMPAGNE | BLENDS`**

| | 結果 |
|---|---|
| ✅ **実在するか** | 🔴 **する。**`/fr-fr/product/plenitude-2/2003` が**現行サイトに実在する**（現行の Plénitude 2 のラインナップは `2003 / 2004 / 2006 / 2008`）。📄 **旧サイトの `Vintage 2003 Plénitude 2` 頁も取得済み** |
| 🔴 **正式表記** | 🔴 **`Plénitude 2`。OBP の印字は正しい。**<br>🔴 **アクセント付き `é`、算用数字 `2`、`P2` ではない。**<br>📄 **ただしメゾンは 2019 年頃まで自ら `P2` と表記していた**（2017・2019 年キャプチャ）**。2021 年キャプチャでは `Plénitude 2` に変わっている。**<br>🔴 **すなわち OBP は現行のメゾン表記に追随している。ここは OBP のほうが正確である** |
| 🔴 **メゾンによる定義** | 🔴 **「**Plénitude 2 is the second life of Dom Pérignon, patiently brought to a new elevation and set on a path to eternity. After close to 15 years of slow transformation in the cellars, Dom Pérignon expands its energy and rises to an apex of essential, radiant vitality, in its state of Plénitude.**」** |
| 🔴 **2003 年版とは何か** | 🔴 **「**a rereading of history and a **second life of the Vintage 2003****」——同じ 2003 年のワインである。**<br>🔴 **「**For each vintage and from its inception, a limited number of bottles are set aside in the cellars, predestined for longer maturation.**」——仕込み時点で取り分けられた限定本数** |
| 🔴 **別キュヴェか、後期リリースか** | 🔴 **メゾンの言葉では「同一ヴィンテージのワインの、第二の生」である。別のアッサンブラージュではない。**<br>⚠️ **モデル上の帰結は 1 行だけ：`cuvée × vintage` の粒度では P1 と P2 を分けられない。`plénitude`（リリース段階）が要る。**🔒 **設計判断であり本書では決めない。番号も開かない** |
| ❓ **リリース年・デゴルジュマン** | 🔴 **取得できていない。**メゾンは「約 15 年」としか書かず、2003 年版の具体的なデゴルジュマン日・リリース年を公表していない。<br>⚠️ **「2003 + 約 15 年」から逆算した年を口にしない。それは推測である** → Open Questions 2 |
| 📄 🔴 **年の性格** | 🔴 **「**the year that changed the history of Champagne**」「**A scorching summer imposed the earliest harvest since 1822**」／春の霜は `4月7日〜11日`、夏は `53 年で最も暑い`、収穫できたブドウは `1947 / 1959 / 1976` 年並みに完熟・健全** |
| 📄 🔴 **香りと味わい** | 🔴 **逐語で取得済み（→ §Style）。菩提樹の花、灰のようなミネラル、乾杏、木苺と無花果のコンフィ、レモンヴァーベナ、白胡椒、ローズマリー、香辛料と甘草の根。口中は「physical」、波のようなリズム、深く暗い垂直性、そしてヨードの苦みと旨味** |
| 🔍 **canonical** | 🔴 **`dom-perignon-p2-2003` が実在する**（`name='Dom Pérignon Plénitude 2'` / `vintage='2003'`）。**にもかかわらず未解決** → §Canonical Conflict ① |

### ✅ メゾンの現行ラインナップ（**参考。`sitemap` / `fr-fr` URL 一覧から機械的に確定**）

✅ **`Vintage`（`2012` / `2013` / `2015` / `2017`）** ⭐OBP 行 1・2
✅ **`Plénitude 2`（`2003` / `2004` / `2006` / `2008`）** ⭐OBP 行 3
✅ **`Rosé`（`2005` / `2006` / `2008` / `2009` / `2010`）**
✅ **`Vintage 2015 Édition Spéciale`（design bleu / jaune / vert）／`Édition Limitée Murakami`（Vintage 2015 / Rosé 2010）**
🔴 ✅ **`Wine Cellar`（旧 `Vintage Library`）—— `1921` から現在まで、年ごとに `vintage` / `rosé` /
`plénitude-2` / `plénitude-3` の個別頁が並ぶ。メゾンが「宣言した年」の全体像がここで機械的に確認できる。**
📄 **旧サイトには `Oenothèque`（例：`Oenothèque 1996`）の頁も存在した。現行サイトでは `Plénitude` 体系に整理されている**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① Dom Pérignon は「ヴィンテージしか造らない」メゾン。そして「造らない年を選ぶ」ことを自分で明言している。**
「**ドン・ペリニヨンはノン・ヴィンテージを一切造りません。メゾンの言葉では
『すべてのヴィンテージが、たった一年を証言する』。**
🔴 **そして裏返しも公表しています ——『理想に満たない年は、宣言しないことを選ぶ（choosing to remain silent）』。
造れない年ではなく、黙ることを選ぶ年、という言い方をします。**
**セラーでの熟成は最低 8 年。**🏛 **ちなみに AOC シャンパーニュの法定下限は、ミレジメで tirage から 36 か月です。
つまりメゾンは法定の倍以上を自らに課しています。**
**創設神話は 1668 年、オーヴィレール修道院に着任したベネディクト会修道士ドン・ピエール・ペリニヨン。
現在の醸造最高責任者は 2019 年 1 月 1 日就任のヴァンサン・シャプロン、前任はリシャール・ジョフロワです。**」

**② `Plénitude 2` は「別のワイン」ではなく「同じ 2003 年の、第二の生」。ここがこのボトルの全部。**
「🔴 **メゾンの説明そのままお伝えします。『それぞれのヴィンテージについて、**仕込みの時点から**、
限られた本数を長期熟成用にセラーへ取り分けておく』。その取り分けた分を、**約 15 年**寝かせて出したのが
`Plénitude 2` です。メゾンはこれを **second life（第二の生）** と呼びます。**
🔴 **つまり今日の 2003 年の P2 は、2003 年のドン・ペリニヨンそのものが、15 年後に別の姿で出てきたもの。
別のブレンドでも別の畑でもありません。**
🔴 **メゾンいわく、その間に瓶の中で起きているのは『酵母がワインへエネルギーを渡す』こと。
**a mysterious transfer of life** —— 生命の神秘的な受け渡し、という表現を使っています。**」

**③ 2003 年は「シャンパーニュの歴史を変えた年」。メゾン自身がそう書いている。**
「🔴 **メゾンの言葉です ——『2003 年は、シャンパーニュの歴史を変えた年として永遠に残るだろう』。**
**厳しく寒く乾いた冬のあと、4 月 7 日から 11 日の春の霜がシャンパーニュに深い傷を残しました。
夏は一転して灼熱、53 年ぶりの暑さ。**🔴 **その結果、1822 年以来もっとも早い収穫になった、と。**
**霜と雹を奇跡的に免れたブドウだけが強烈な暑さに晒され、収穫できたものは完璧に熟して健全だった ——
1947 年、1959 年、1976 年並みだった、とメゾンは書いています。**
🔴 **P2 の 2003 年についてメゾンが使う言葉は `insolent freshness` ——『不遜なほどの、生意気なほどの新鮮さ』。
酷暑の年から 20 年以上経ってなお、そう表現しているのが面白いところです。**」

### 追加で使える一手（**すべて出典つき**）

- 🔴 **P1 と P2 を同じ年で並べて語る（本ドシエ最強の一手）**：「**メゾンは同じ 2003 年について、
  最初のリリース（P1）と `Plénitude 2` の両方のノートを公表しています。読み比べると同じ語が繰り返される ——
  `physical`（身体的）、`tactile`（触覚的）、`vibrant`、そして香辛料と甘草の根、ヨード。**
  🔴 **P1 では『**リズムとテンポが、メロディーよりも支配的**』と書き、P2 では『**波のように、リズムと砕けで
  できている**』と書く。同じワインの同じ性格を、15 年隔てて別の言葉で言い直しているわけです。**」
- 🔴 **`Brut` の話を振られたら**：「🔴 **実は『ブリュット』はドン・ペリニヨンのキュヴェ名ではありません。
  メゾンが自社製品を呼ぶときの名前は `Dom Pérignon Vintage` です。**
  🔴 **『ブリュット』は残糖の表示区分のほうで、シャンパーニュの AOC 規定にすら出てこない語です。
  AOC が決めているのは、ドザージュ前の段階で発酵性の糖が 1 リットルあたり 10 グラム以下、というところまで。**」
  ⚠️ **（`メニューが間違っている` とは言わない。ラベルにそう刷ってある可能性がある）**
- 🔴 **法定熟成との対比**：「🏛 **AOC シャンパーニュの明細書では、ミレジメを名乗るワインは tirage から
  36 か月以上寝かせないと市場に出せません。ノン・ミレジメなら 15 か月。**
  🔴 **ドン・ペリニヨンは 8 年以上、`Plénitude 2` は約 15 年。桁が違います。**
  🔴 **もうひとつ面白い規定があって、ミレジメにできるのはその年に扱った量の 80% まで。
  残りは必ずリザーヴワインに回さなければならない ——『全部を当たり年にはできない』が制度に書き込まれています。**」
- 🔴 **年号はコルクにある**：「🏛 **明細書は『年号はコルクに記す』と定めています（`celui-ci figure sur le
  bouchon`）。抜いたコルクをお持ちしましょうか。**」
- 🔴 **サービスの話**：「📄 **メゾン自身が『**Do not sabre the bottle**』——サーブルで開けないでください、と
  はっきり書いています。瓶の中は 6〜8 気圧、自動車のタイヤの 3 倍です。**
  **保管は 7〜18℃、湿度 70% 以上、光を避けて。**
  🔴 **それと、メゾンは『**うちが売るボトルはすべて自社セラーで熟成済みで、買ったその日に開けてよい**』
  とも書いています。寝かせ直す必要はない、と造り手自身が言っているわけです。**」
- **2013 の年の性格**：「📄 **メゾンは 2013 を『**遅摘みヴィンテージの輝かしい過去との、喜ばしい再会**』と
  書いています。冬は寒く雨、春は灰色で冷涼かつ極端に雨がち、そして夏は暑く乾いてブドウの質に効いた、と。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／第三者の主張にすぎない**）

1. 🔴 ⚠️ **品種比率を言わない。**
   **『ピノ・ノワール ◯%、シャルドネ ◯%』は 3 本とも言わない。**
   🔴 **メゾンは品種構成比を一切公表していない。本調査で読めた生産者著作のどこにも数値が無い。**
   **（THÉSEUS の DB は 2013 に `PN49/CH51`、2003 P2 に `PN62/CH38` と書くが、造り手の言葉ではない。）**
2. 🔴 ⚠️ **ドザージュ量を言わない。**
   🔴 **『5 g/L』は造り手の公表値ではない。メゾンが成分について公表しているのは
   『**All our champagnes contain sulphites.**』の 1 行だけである。**
3. 🔴 ⚠️ **畑・村を語らない。**
   🔴 **『コート・デ・ブランのクラマン、アヴィズ、ル・メニル』『モンターニュ・ド・ランスのアイ、ブジー、
   ヴェルズネ』『モエの 1,200 ヘクタール』『17 のグラン・クリュ』——**
   🔴 **これらはいずれもメゾンが公表していない。本調査で読めた生産者著作に村名は 1 つも出てこない。**
   🏛 **grand cru 17 コミューンの一覧は AOC 明細書に載っているが、そこから「このワインがどの村か」は導けない。**
4. 🔴 ⚠️ **『オーガニックです』とも『オーガニックではありません』とも言わない。**
   🏛 **MHCS の Agence Bio 登録の最初の関与日は `2020-10-15`。OBP の 3 本は 2015・2013・2003 年収穫で、
   すべてそれより前である。したがってこの 3 本については、どちらの向きにも何も言えない。**
   🔴 **さらに MHCS の登録区分は `Grossistes`（卸）で、活動は調製・流通・輸入。栽培ではない。**
5. 🔴 ⚠️ **『ビオディナミ』と言わない。** **Biodyvin の会員一覧にも Demeter のサイトマップにも、
   `MHCS` / `Moët` / `Dom Pérignon` / `Hautvillers` は 0 件である。生産者資料にも語が無い。**
6. 🔴 ⚠️ **『再デゴルジュマンされています』と言わない。**
   🔴 **メゾンはその語を一度も使っていない。メゾンの説明は『仕込みの時点から限られた本数をセラーに
   取り分けておく』であって、一度出したものを開け直したとは書いていない。デゴルジュマンの時期・回数も非公表。**
7. 🔴 ⚠️ **P2 の熟成を『16 年以上』と言わない。**
   🔴 **メゾンは 2 つの頁で一貫して『**close to 15 years**』『**almost fifteen years**』と書く。
   所有者 LVMH の表記も『15 YEARS OR MORE』である。**
8. 🔴 ⚠️ **2003 年の収穫開始日を『8 月 21 日』と言わない。**
   🔴 **メゾンが書いているのは『1822 年以来もっとも早い収穫』までで、日付は書いていない。**
   **同様に『コート・デ・ブランのシャルドネの 70% が失われた』もメゾンの記述ではない。**
9. 🔴 ⚠️ **2013 年の収穫日を『9 月 28 日〜10 月 15 日』と言わない。**
   🔴 **メゾンは 2013 について収穫日を書いていない。『遅摘みヴィンテージへの再会』とだけ書いている。**
   **『気候変動前の最後の 10 月収穫ヴィンテージ』という言い回しも造り手の言葉ではない。**
10. 🔴 ⚠️ **2015 年について、年の性格を語らない。**
    🔴 **本調査ではメゾンの 2015 年の記述を 1 文も取得できていない。
    『猛暑』『45 年で最も暑い 8 月』『9 月 7 日収穫開始』はいずれも造り手の言葉として確認できていない。**
    → **行 1 は『ヴィンテージのみ・8 年以上熟成・アッサンブラージュ』までにとどめる。**
11. 🔴 ⚠️ **『メニューの "Brut" は誤りです』と言わない。**
    🔴 **メゾンの製品名でないことは確かだが、瓶のラベルに残糖表示として `BRUT` が刷られている可能性が高い。
    本調査はラベル現物を 1 枚も読めていない。「メゾンは `Dom Pérignon Vintage` と呼びます」までにとどめる。**
12. 🔴 ⚠️ **『1668 年創業のメゾン』と言わない。**
    🔴 **メゾン自身がこの節を `THE FOUNDING MYTH`（創設神話）と題している。**
    🏛 **法人 MHCS の登記上の設立は 2008 年 12 月 12 日で、まったく別の事実である。**
    **ブランドとしての最初のヴィンテージ発売年は、本調査では確認できていない。**
13. ⚠️ **第三者の点数を蔵の説明として使わない。**
    **THÉSEUS の DB は 3 本すべてに `96点` を持つが、いずれも造り手の言葉ではない。**
14. ⚠️ **『LVMH がこう言っています』を造り手の言葉として引かない。**
    🏛 **LVMH は MHCS の所有者側であって生産者ではない。**
    **本書が LVMH の記述を採用したのは、生産者自身の記述と一致する箇所（8 年 / 15 年）に限る。**
15. ⚠️ **『バタール・モンラッシェのよう』と造り手の表現として言わない。**
    **メゾンの P2 2003 のノートにブルゴーニュへの言及は無い。**
16. ⚠️ **売上高・利益を Dom Pérignon の数字として言わない。**
    🏛 **`25.9 億ユーロ` は MHCS 全体（Moët & Chandon 等を含む）の 2024 年度数値である。**

---

## Akio's Insight

🖋 （この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **canonical（`migration/`）も `research/canonical_conflicts/REGISTER.md` も一切変更していない。**
🔒 **以下はすべて escalate であり、実行はしていない。**

---

### 🔴 ① **evidence が canonical を過小申告し、3 行とも正解を取り逃している（`CDX-1` の逆・最強事例）**

1. **衝突する canonical ID**: 🔴 **`dom-perignon-2015` / `dom-perignon-2013` / `dom-perignon-p2-2003`**
2. **なぜ重複に見えるか**: 🔴 **重複ではない。「当てる先はあるのに当たっていない」型である。**
3. **証拠**:
   🔍 **intake の 3 行すべての evidence が「`'Dom Pérignon'` の canonical キュヴェ **2 件** に一致無し」。**
   🔍 🔴 **canonical 928 レコードを機械走査した実測値は、`producer == 'Dom Pérignon'` が **15 件**、
   `name` の異なり数が **6 種**（`Dom Pérignon Brut` / `Dom Pérignon Vintage` / `Dom Pérignon Rosé` /
   `Dom Pérignon Plénitude 2` / `Dom Pérignon Réserve de l'Abbaye (P3)` / `Dom Pérignon Œnothèque`）。**
   🔍 🔴 **かつ、OBP 3 行それぞれに `name` も `vintage` も一致するレコードが実在する（→ 前掲の表）。**
   🔍 **にもかかわらず 3 行とも `proposed_canonical_cuvee_id: null` / `cuvee_state: unresolved` /
   `confidence: 0.0`。**
4. **OBP への影響**: 🔴 **$600 + $600 + $1,800 = $3,000 分が canonical から見えない。
   しかも「データが無いから見えない」のではなく「あるのに繋がらない」。**
   🔴 **Ridge 型の gap（`CDX-23`）とは remedy が正反対である。ここでデータ投入を処方すると重複を作る。**
5. **推奨する解決（実行しない）**: 🔒 **`CDX-1` の**逆**の族（Krug で記録済み：evidence が 2 件と主張し
   canonical は 13 件）に属する。本件は 2 件 vs 15 件で、より強い。新番号は開かない。**
6. **Confidence**: 🔴 **High**（機械走査 + intake の実読の両方向で確定）

---

### 🔴 ② **`CDX-5`（canonical 格納値が一次資料と矛盾する）—— 本生産者でも base rate が再現した**

1. **衝突する canonical ID**: 🔴 **`dom-perignon-2015` / `dom-perignon-2013` / `dom-perignon-p2-2003`**
2. **なぜ重複に見えるか**: 🔴 **重複ではない。単一レコード群の内容の問題である。**
3. **証拠**:

| # | canonical の記述 | 一次資料 | 判定 |
|---|---|---|---|
| **②-1** | 🔴 **`dom-perignon-p2-2003.aging` = 「**16+ years on lees (P2)**」** | 📄 🔴 **メゾンは 2 頁で「**close to 15 years**」「**almost fifteen years**」。⚠️ LVMH も「15 YEARS OR MORE」** | 🔴 **数値が食い違う** |
| **②-2** | 🔴 **`dom-perignon-2013.grapes` = `["Pinot Noir 49%","Chardonnay 51%"]`／`dom-perignon-p2-2003.grapes` = `["Pinot Noir 62%","Chardonnay 38%"]`** | 🔴 **メゾンは品種比率を一切公表していない。**🔴 **しかも同じ canonical の `dom-perignon-2015` 自身が「**The house does not officially publish the varietal proportions or the dosage figure**」と明記している** | 🔴 **同一生産者の canonical 内部で自己矛盾。`CDX-16`（属性の出所）と同型** |
| **②-3** | 🔴 **`dosage` = `5 g/L`（2013・2003 P2）／`Brut — not officially disclosed`（2015）** | 🔴 **メゾンが成分について公表するのは「**All our champagnes contain sulphites.**」の 1 行のみ** | 🔴 **同上。3 レコードのうち 1 つだけが「非公表」と正しく書き、2 つが数値を書いている** |
| **②-4** | 🔴 **`dom-perignon-p2-2003.terroir_en` に「**+10°C above normal, **per Krug's Julie Cavil**」** | 🔴 **競合メゾン（Krug）の Chef de Cave の発言が、Dom Pérignon のレコード内に典拠として埋め込まれている** | 🔴 **`CDX-16`（属性の出所）の最も露骨な形。UI に流れれば「ドン・ペリニヨンの説明としてクリュッグの発言を読む」ことになる** |
| **②-5** | **`dom-perignon-p2-2003`：収穫開始 `8月21日`／コート・デ・ブランの CH `70%` 喪失** | 📄 **メゾンは「**earliest harvest since 1822**」「春の霜 `4月7〜11日`」「`53 年で最も暑い`夏」「収穫は `1947/1959/1976` 並みに完熟・健全」と書き、日付も 70% も書いていない** | ⚠️ **出所不明** |
| **②-6** | **`dom-perignon-2013`：収穫 `9月28日–10月15日`／「気候変動前の最後の 10 月収穫ヴィンテージ」** | 📄 **メゾンは収穫日を書かず、「**a welcome reconnection with the glorious past of late harvest vintages**」とだけ書く** | ⚠️ **出所不明。言い回しも造り手のものではない** |
| **②-7** | 🔴 **`name` の不統一：`dom-perignon-2015` = `Dom Pérignon Vintage`／`dom-perignon-2013`・`2012`・`2010`・`2008`・`2002`・`2000`・`1996` = `Dom Pérignon Brut`** | ✅ 🔴 **メゾンの SKU 名は `Dom Pérignon 75cl Vintage Millésimé`。`Brut` はメゾンの公表物 397 KB に 0 件、🏛 AOC 明細書 28 頁にも 0 件** | 🔴 **同一製品ラインに canonical 内で 2 つの名前がある。①の「2 件」という誤集計の一因である可能性が高いが、本書はここで止める** |
| **②-8** | **`classification` = `Millésimé Brut`（10 レコード）** | 🏛 **`Millésimé` は AOC 明細書の実在する法定表示（Ch.I, II-a）。`Brut` は同明細書に 0 件** | ⚠️ **法定用語と非法定用語が 1 フィールドに混在。`CDX-16` 型** |
| **②-9** | **`points: 96`（3 本とも）／`obp_note` に Cristal・Bollinger VVF・Pol Roger SWC への言及／日本国内希望小売価格 `¥38,940`** | 🔍 **いずれも第三者情報・市場情報** | ⚠️ **市場価格と第三者評価を canonical に静的に持つ設計問題。Ridge・Montelena で報告済みの形と同型** |

4. **OBP への影響**: 🔴 **②-2・②-3 が最も重い。メゾンが「公表していない」と canonical 自身が書いている数値を、
   同じ canonical の別レコードが具体値で持っている。staff 表示に流れれば $1,800 のボトルについて
   造り手が公表していない数値を語ることになる。**
   🔴 **②-4 は競合メゾンの発言が典拠として混入しており、性質が異なる（誤りではなく汚染である）。**
5. **推奨する解決（実行しない）**: 🔒 **`CDX-5`（約 10/10 の base rate）および `CDX-16`（属性の出所）の族。
   新番号は開かない。**
6. **Confidence**: 🔴 **High**（②-1〜②-4、②-7、②-8）／⚠️ **Medium-High**（②-5・②-6 ——
   「読んだ範囲に無い」であって「存在しない」ではない。現行サイトは年齢ゲートで読めていない）

---

### ⚠️ ③ **既存の族に該当するもの（新しい番号は開かない）**

- ⚠️ 🔴 **パーサの判定が下流で捨てられている（Batch 12 で報告済みの形の変種）** ——
  🔍 **行 1・2 の `_parts` は `label: null` / `style: "brut"` と、`Brut` を**スタイル語として正しく分類している**。
  🔍 **にもかかわらず `normalized_cuvee` は `"Brut"` となり、evidence も
  「canonical キュヴェ 2 件に一致無し: **'Brut'**」——スタイル語をキュヴェ名として canonical に照合している。**
  🔴 **Batch 12 では「キュヴェ名なしを検知した後に matcher が grand vin を提案する」形だったが、
  ここでは「スタイル語をキュヴェ名スロットに昇格させる」形である。同じ根（パーサの構造化出力が
  matcher に届いていない）に見えるが、本書はここで止める。**
- ⚠️ 🔴 **`V-1` / `CDX-8`（同一性の軸）** —— 🔴 **行 3 の `Plénitude 2` は、メゾンの言葉では
  「同一ヴィンテージのワインの第二のリリース」であって別キュヴェではない。**
  🔴 **モデル上の帰結は 1 行：`cuvée × vintage` では P1 と P2 を区別できず、`plénitude`（リリース段階）が要る。**
  🔒 **番号は開かない。設計判断は本書では行わない。**
- ⚠️ **`CDX-15`（メニューがカテゴリー語をキュヴェ名として印字）** —— 🔴 **行 1・2 の `Brut` は
  この型**に見える**が、本書は判定していない。ラベル現物が無く、`Brut` が瓶に刷られている可能性を
  排除できないためである（`3f-10`：パターンの存在は個々の行の証拠ではない）。**
- ⚠️ **`CDX-9`（生産者名の部分一致）** —— 🔍 **canonical 内で文字列 `Pérignon` を含むレコードには、
  別生産者の記述文中の言及（`Gosset` / `Pierre Péters` / `Alfred Gratien` の各レコード）が混じる。
  本書はすべて `producer` フィールドの完全一致（`Dom Pérignon`）で判定し、部分一致は使っていない。**
- ⚠️ **`CDX-23`** —— **本件は gap では**ない**。canonical にレコードは存在する。
  gap（Ridge 型）と混同すると、重複投入という逆方向の誤った修正を招く。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY / `D-2026-08-05-09`**）

🔴 **本ブリーフは候補ドメインを名指ししていない。以下は本調査が自力で特定し、検証した結果である。**

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の運営者名** | ✅ 🔴 **合格。**`https://www.domperignon.com/` の `mentions légales`（2023年6月更新）冒頭に「**Le site Internet www.domperignon.com … est édité par MHCS, société anonyme : capital social : 433 193 789 euros ／ numéro d'immatriculation : 509 553 459 RCS Reims ／ numéro de TVA : FR 44 509 553 459 ／ adresse du siège social : 9 Avenue de Champagne 51200 EPERNAY, France**」 |
| **(b) 公的登録簿と一致するか** | ✅ 🏛 🔴 **合格（本ドシエで最も強い検証）。**<br>🏛 **`recherche-entreprises.api.gouv.fr` の `SIREN 509553459` = `M H C S`、本店 `9 AVENUE DE CHAMPAGNE 51200 EPERNAY`、TVA `FR44509553459`。**<br>🔴 **法人番号・TVA 番号・住所の 3 点が完全一致。**<br>🏛 **さらに Agence Bio 登録簿の `siret 50955345900033` と本店 SIRET も一致する** |
| **(c) 非関連の免責表示が無い** | ✅ **合格。**「ファンサイト」「非公式」の類の表記は無い。全ページ末尾に `© Dom Pérignon`。年齢ゲートには「**Par le biais du groupe Moët Hennessy auquel elle appartient, MHCS est membre de spiritseurope…**」とあり、運営主体を MHCS と自認している |
| **(d) 商業・法務フッターの整合** | ✅ **合格。**`Conditions générales d'utilisation` / `Charte de données personnelles and cookies` / `Accessibilité` / `Qualités et caractéristiques environnementales`（仏 AGEC 法の法定開示）が揃う。ホスティングは `Vercel Inc.`（`340 S Lemon Ave 4133, Walnut, California 91789`、法人番号 `C3840731`）と明記 |
| 🔴 **(e) Wayback キャプチャの真正性** | ✅ 📄 🔴 **合格。**本書が事実の典拠に用いた旧ページのキャプチャには、いずれもフッターに当時の T&C が埋め込まれており、そこに **`MHCS` / `509 553 459` / `9 Avenue de Champagne 51200 EPERNAY`** が明記されている。すなわち各キャプチャは `domperignon.com` 本体の内容であることが文書内部で自己証明されている |
| **年齢ゲート** | 🔴 ⚠️ **静的取得では全頁がゲートされた。**`sitemap` 由来の 187 頁のうち 183 頁がバイト単位で同一のゲート用シェルを返した。**ゲートは自己申告であって bot 検出ではないが、本調査の取得手段（静的 fetch）では通過できていない** |
| **bot 検出の兆候** | **`domperignon.com` 側には無し。CAPTCHA・チャレンジには一度も遭遇していない** |

🔴 **本調査で `NOT_THE_PRODUCER_*` として退けたサイトは無い。**
🔴 **⚠️ `lvmh.com` は「生産者ドメイン」ではない。**MHCS の登記上の取締役に `MOET HENNESSY` 等が入ることは
🏛 登録簿で確認したが、LVMH の Maison 頁は**所有者側の著作**であって生産者著作ではない。
**本書は LVMH の記述を、生産者自身の記述と一致する箇所（熟成 8 年 / 15 年）の裏づけと、
生産者側に対応する記述が無い箇所の明示的な `⚠️` 表示にのみ用いた。**

### 一次資料

| 資料 | レイヤー | 取得した情報 |
|---|---|---|
| **`/fr-fr/legal/conditions-generales-d-utilisation`（`mentions légales`）** | ✅ | **法人名 `MHCS`・法形態 `société anonyme`・資本金 `433 193 789 €`・`509 553 459 RCS Reims`・TVA・本店住所・電話・Directeur de Publication・ホスティング（Vercel）** |
| 🔴 **`/fr-fr/legal/qualites-et-caracteristiques-environnementales`** | ✅ 🔴 | 🔴 **仏 `décret 2022-748`（loi AGEC 13-I）に基づく法定開示。**🔴 **メゾン自身の SKU 名の全一覧（`Vintage Millésimé` / `Vintage Plénitude 2` / `Vintage Plénitude 3` / `Rosé Vintage Plénitude 1` ほか）と、瓶・化粧箱ごとのリサイクル性・再生材比率（`86–87%`）** |
| **`/fr-fr/legal/charte-de-donnees-personnelles-and-cookies` / `/legal/accessibilite`** | ✅ | **真正性の補強** |
| **`robots.txt` / `sitemap.xml` / `sitemap2.xml` / `fr-fr` URL 全一覧** | ✅ | 🔴 **現行ラインナップの機械的確定（`Vintage` 2012/2013/2015/2017、`Plénitude 2` 2003/2004/2006/2008、`Rosé` 2005–2010、`Édition Spéciale` / `Édition Limitée Murakami`、`Wine Cellar` の 1921 年以降の年別頁）** |
| 🔴 **`/product/plenitude-2/2003`（旧 `Vintage 2003 Plénitude 2`）** | 📄 🔴 | 🔴 **OBP 行 3。**`Plénitude 2` の定義（`second life` / `close to 15 years`）、`SET ON A PATH TO ETERNITY`（仕込み時点からの取り分け・酵母のエネルギー移譲）、2003 年の位置づけ（`the year that changed the history of Champagne` / `earliest harvest since 1822` / `insolent freshness`）、`THE NOSE` と `THE PALATE` の逐語 |
| 🔴 **`/vintage-library/2003`（`Vintage 2003`）** | 📄 🔴 | 🔴 **同一ヴィンテージの P1 のノート。**`ON THE PALATE` / `ON THE NOSE` / `The 2003 Harvest`（春の霜 4月7–11日、53 年で最も暑い夏、1947/1959/1976 並みの完熟）。**P1 と P2 の対比が可能になった** |
| 🔴 **`/product/vintage/2013`（旧 `Vintage 2013`）** | 📄 🔴 | 🔴 **OBP 行 2。**`Harmony achieved`、`Dom Pérignon is vintage champagne only.`、`After at least eight years of elaboration in the cellars`、`SEASONS` / `NOSE` / `PALATE` の逐語 |
| **`/spirit`（`The spirit of Champagne`）** | 📄 | **`INSPIRE THE WORLD TO ELEVATION`、`every vintage bears witness to a single year`、`choosing to remain silent`、`THE FOUNDING MYTH`（1668年・Hautvillers・procurator）、Chaperon の就任と引用句** |
| **`/news/vincent-chaperon-new-dom-perignon-chef-de-cave`** | 📄 | 🔴 **`On January 1, 2019`、Geoffroy の `15 vintages`（1990–2009）と `Plénitudes` の創出、Chaperon の `13 harvests` と共同宣言した 4 ヴィンテージ（2005・2006・2009・2008、宣言順）** |
| **`/guidelines-for-storing-champagne-and-composition`** | 📄 | 🔴 **保管条件（7–18℃ / 湿度 70% 以上 / 遮光）、`6 to 8 bars`、`Do not sabre the bottle`、`can be opened as soon as they are purchased`、**🔴 **`COMPOSITION — All our champagnes contain sulphites.`（メゾン唯一の成分表示）** |
| **`/product/plenitude-2/2000` / `/product/vintage/2008` / `/vintage-library/1999` / `/vintage-library/1996`（Oenothèque）／`/vintage-library/1970`（P3）** | 📄 | **`almost fifteen years` の再確認、`Vintage` 定型文の再確認、旧 `Oenothèque` 体系の存在確認** |
| **Wayback 各時点キャプチャ（2015 / 2017-01-01 / 2019-01-01 / 2021-06-01 / 2022-06-01）** | 📄 | 🔴 **`P2` → `Plénitude 2` の呼称変更が 2019〜2021 年の間に起きたことの実測。**📄 **2018年4月4日版 T&C（法形態 `société en commandite simple`、旧ホスティング LINKBYNET、旧 Chief Editor）** |

### 🏛 公的登録簿・規制一次資料

| 資料 | 取得した情報 |
|---|---|
| 🔴 🏛 **`recherche-entreprises.api.gouv.fr`（`SIREN 509553459`、RNE / INSEE）** | 🔴 **`M H C S`／本店 `9 AVENUE DE CHAMPAGNE 51200 EPERNAY`（SIRET `50955345900033`）／主活動 `11.02A`／法形態 `5599`（SA à conseil d'administration）／企業設立 `2008-12-12`／区分 `GE`／事業所 17（稼働 12）／TVA `FR44509553459`。**<br>🔴 **役員：`GUIONY Jean-Jacques`（Président du CA et DG）／`DUFOUR Frédéric`（DG délégué）／`BRIFFOTEAUX Hervé`（Administrateur）。法人取締役：`MOET HENNESSY`・`MOET HENNESSY INVESTISSEMENTS`・`SOCIETE JAS HENNESSY & CO`。CAC：`FORVIS MAZARS SA`。**<br>🔴 **2024年度 CA `2,591,647,130 €` / 純利益 `413,108,331 €`** |
| 🔴 🏛 **Agence Bio 事業者登録簿（`numeroBio 18379`）** | 🔴 **`datePremierEngagement 2020-10-15`／認証機関 `FR-BIO-10` Bureau Veritas（関与 2020-10-19、`ARRETEE` 2023-10-31）と `FR-BIO-01` Ecocert France（関与 2022-07-02、`ENGAGEE`）／区分 `Grossistes`／活動 `Préparation`・`Distribution`・`Importation`／生産品目 `11.02 Vins de raisin`（`AB`、参照年 2026）／`mixité: Oui`／`siteWebs: []`／登録住所 2 件（Épernay 本店・Recy）／更新 2025-06-30** |
| 🔴 🏛 **AOC Champagne 明細書（BO-agri 掲載 PDF、`AGRT2230908A`、arrêté du 25 janvier 2024、JORF 2024-01-28、BO du MASA 2024-02-22）** | 🔴 **AOC の根拠（décret du 29 juin 1936 / loi du 6 mai 1919）／白・ロゼの発泡性ワインに限定／主要 7 品種＋`Voltis B`／grand cru 17 コミューン・premier cru 41 コミューン（`Hautvillers` は premier cru）／tirage は収穫翌年 1月1日以降／prise de mousse 後の発酵性糖分 `≤10 g/L`／**🔴 **最低熟成 `15 か月`、ミレジメ `36 か月`／ミレジメは当該年の `80%` 以下／年号はコルクに記載／木片使用禁止・総アルコール `≤13%`。**<br>🔴 **`brut` の語は 0 件** |
| ⚠️ 🏛 **Biodyvin 会員一覧** | 🔴 **`MHCS` / `Moët` / `Dom Pérignon` / `Hautvillers` が 0 件（機械走査）** |
| ⚠️ 🏛 **Demeter サイトマップ** | 🔴 **同 4 語が 0 件** |

### 取得できなかったもの / 読めなかったもの

- 🔴 ⚠️ **現行サイトの製品頁を 1 頁も読めていない。**
  **`sitemap` 由来の 187 頁のうち 183 頁が、バイト単位で同一の年齢ゲート用シェル（1,067 文字）を返した。
  年齢ゲートは自己申告であって bot 検出ではないが、本調査の静的取得では通過できていない。**
  → **製品記述はすべて Wayback 由来（`📄`）である。**
- 🔴 ⚠️ **`Vintage 2015` についてのメゾンの記述を 1 文も取得できていない。**
  **現行頁はゲートの向こう、Wayback に本文キャプチャなし。**→ **OBP 行 1 の年の性格が語れない。**
- 🔴 ⚠️ **🏛 TTB Public COLA Registry が bot 防御でゲートされていた。**
  **`TSPD` / `bobcmn` および `captcha` の実在を確認。突破は試みていない。**
  → **本書は TTB 承認ラベルの記録（brand name / fanciful name / class-type / 承認日）を 1 件も持たない。**
  → **⚠️ ゲートは「ラベルが存在しない」ことの証拠ではない。**
- 🔴 ⚠️ **ラベル現物（表・裏とも）を 1 枚も読めていない。**
  **`Brut` の印字の有無、`Plénitude 2` か `P2` かの印字、デゴルジュマン表示、コルクの年号がすべて未確認。**
- ⚠️ **🏛 INAO 側のデータを取得できなかった。**
  **`www.inao.gouv.fr` は Drupal の 404 頁を返した。代替として BO-agri 掲載の明細書 PDF 本体を用いており、
  一次資料としての要件は満たしている。**
- ⚠️ **`Brut` を定義する EU 規則の条文そのものを取得していない。**
  **本書は「AOC 明細書に `brut` は無い」「メゾンの公表物に `Brut` は無い」までを実測で述べ、
  残糖の閾値は一切書かない。**
- ❓ **品種比率・ドザージュ・収穫日・デゴルジュマン日・生産本数・アルコール度数（3 本とも）。**
  **これらは「調べ漏れ」ではなく「メゾンが公表していない」である。**
- ❓ **Dom Pérignon ブランドとしての最初のヴィンテージ発売年。**
- ❓ **蔵出し価格。**EC 導線が現行サイトに無く、価格を示す公式資料が取得できていない。
  → **本書は $600 / $600 / $1,800 の位置づけを一切主張しない。**
- ⚠️ **`Jaques Giraco` の身元。**現行 mentions légales が Directeur de Publication として掲げるが、
  🏛 登記簿の役員一覧に該当氏名が無い。**両方記録し、いずれも断定していない。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical: `migration/out/export/db_wine_canonical.json`（928 レコード）を機械走査。
`producer == 'Dom Pérignon'` は 15 件、`name` の異なり数は 6 種。**
🔍 **OBP 行に対応するレコード：`dom-perignon-2015`（VT 2015）／`dom-perignon-2013`（VT 2013）／
`dom-perignon-p2-2003`（VT 2003）—— 3 行すべてに正解が実在する。**
🔍 **⚠️ 部分一致は使っていない（`D-2026-08-05-08` / `CDX-9`）。文字列 `Pérignon` は
`Gosset` / `Pierre Péters` / `Alfred Gratien` の各レコードの記述文中にも現れる。**
🔍 **OBP: `/Users/akiomatsumoto/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行）に 3 行。
`source_row_id` = `obp-beverage-2026-08:5cbde63539` / `:5a8f29e841` / `:eb2f3e1d35`。
3 行すべて `match_state = unresolved`・`confidence = 0.0`・`producer_state = exact`・
`cuvee_state = unresolved`・`vintage_state = unresolved`・`source_quality_flags = []`・
`_collision_risk = LOW`。**
🔍 🔴 **`_parts`：行 1・2 は `label: null` / `style: "brut"` / `appellation_display: "Brut"`、
行 3 は `label: "Plénitude 2"` / `style: "brut"`。**
⚠️ **本書の件数はすべて `obp_intake_normalized_20260804.json` から取ったものであり、
`research/out/t-01/mapping.json` は参照していない（`CDX-4`）。**
🔒 **canonical・`REGISTER.md`・intake のいずれも編集していない。**

---

## Confidence

```
reached_70: YES (~78%)
confidence: Medium-High
```

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🔴 **法人名・法人番号・TVA・本店住所が、現行 mentions légales と 🏛 RNE と 🏛 Agence Bio の 3 経路で完全一致。役員・資本金・売上高まで登録簿で確定。法形態の変遷（SCS → SA）も 2 時点の一次資料で追えた**<br>⚠️ **`Jaques Giraco` の身元と、LVMH の出資比率のみ不明** |
| **Overview** | **High** | **メゾンの自己規定（vintage only / remain silent / 8 年以上 / Plénitudes）がすべてメゾンの言葉で取れた** |
| 🔴 **History** | ⚠️ **Medium-High** | 🔴 **Chef de Cave の系譜（Geoffroy 1990–2009 の 15 ヴィンテージ／Chaperon 2019-01-01 就任／共同宣言 4 ヴィンテージ）が公式で確定。1668 年が「創設神話」であることもメゾン自身の見出しで確定**<br>⚠️ 🔴 **ブランドとしての沿革（初ヴィンテージ、Moët 傘下入り、Plénitude 体系の導入年）が公表されていない。生産者が「歴史」をほとんど書かないメゾンである** |
| 🔴 **Location** | ⚠️ **Medium** | 🏛 **AOC が明細書レベルで確定し、法人所在も 3 経路一致。**<br>🔴 ⚠️ **しかし畑が完全に不明である。村名・区画・面積・grand cru 比率のいずれもメゾンが公表していない。「シャンパーニュのどこか」以上を語れない** |
| 🔴 **Farming** | 🔴 **High（ただし内容は「言えない」の確定）** | 🔴 **🏛 Agence Bio の関与日 `2020-10-15` が確定し、OBP 3 ヴィンテージすべてがそれより前であることを 1 本ずつ確認した。登録区分が `Grossistes` であることも確定。Biodyvin・Demeter の不在も機械走査で確定。**🔴 **「何も言えない」ことが高い確度で確定した節である** |
| **Winemaking** | ⚠️ **Medium** | 🔴 **熟成期間（8 年 / 約 15 年）と Plénitude 2 の仕組みがメゾンの言葉で確定。🏛 AOC の法定要件も全項目確定。**<br>❓ 🔴 **品種比率・ドザージュ・デゴルジュマン・発酵の詳細は 1 つも公表されていない。ただしこれは調査の失敗ではなく、メゾンの方針である** |
| 🔴 **Style** | ⚠️ **Medium-High** | 🔴 **3 行中 2 行（2013・2003 P2）にメゾンの逐語ノートがあり、しかも 2003 は P1 と P2 の両方が取れて対比できる。年の性格も 2 行分は公式で確定。**<br>🔴 ⚠️ **2015 は 1 文も取れていない。3 行中 1 行が空白である** |
| 🔴 **Important Cuvées** | ⚠️ **Medium-High** | 🔴 **3 行すべてについて製品の実在・メゾンの正式名称・URL を確定。`Plénitude 2` の正書法と定義、P2 の同一性の性質をメゾンの言葉で決着させた。`Brut` がメゾンの語でも AOC の語でもないことを両方向の機械走査で確定**<br>🔴 ⚠️ **ラベル現物が無いため、行 1・2 の `Brut` の身分を確定できていない。判定を意図的に保留した** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **①（15 件 vs evidence の 2 件、3 行とも正解が実在）は 928 レコードの機械走査と intake の実読で確定。②の 9 点のうち 7 点は一次資料との直接照合**<br>⚠️ **②-5・②-6 のみ「読んだ範囲に無い」という消極的証拠（現行サイトがゲートされているため）** |
| **Staff Notes** | 🔴 **High** | ⚠️ **16 項目。🔴「品種比率」「ドザージュ」「畑・村」「オーガニック」「ビオディナミ」「再デゴルジュマン」「16 年以上」「8月21日」「2013 の収穫日」「2015 の年の性格」「メニューが誤り」「1668 年創業」の 12 の誤りを塞いだ** |
| **総合** | ⚠️ 🔴 **Medium-High — staff-usable（70% は超えるが、Ridge のような余裕はない）。** | 🔴 **強い：メゾンの哲学（vintage only / remain silent）、熟成体系（8 年・約 15 年・Plénitude の仕組み）、法人と AOC の法的枠組み、行 2 と行 3 の逐語ノート、そして「何を言ってはいけないか」。**<br>🔴 **弱い：行 1（2015）の年の性格が空白。畑が完全に不明。ラベル未読。**<br>🔴 **欠けているものはすべて「言わない」で回避でき、卓上で嘘をつく経路は塞いである。ただし行 1 は $600 のボトルとしては薄い。** |

---

## Open Questions

1. 🔴 **OBP 3 本のラベル現物（実ボトル案件）。**
   🔴 **確認すべき点：① 表ラベルまたは裏ラベルに `BRUT` の語があるか（あれば行 1・2 の `Brut` は
   メニューの創作ではなくラベルの写しであり、`CDX-15` 型ではないことが確定する）
   ② 行 1・2 の表記が `Vintage 2015` / `Millésime 2013` のどちらか
   ③ 行 3 が `Plénitude 2` と `P2` のどちらで刷られているか
   ④ 🏛 明細書が義務づけるコルクの年号（`2003` / `2013` / `2015`）
   ⑤ デゴルジュマン表示の有無。**
   🔴 **① は本ドシエで唯一「保留」にした判定であり、瓶 1 本で決着する。**
2. 🔴 **`Plénitude 2` 2003 のリリース年とデゴルジュマン時期。**
   **メゾンは「約 15 年」としか書かず、2003 年版の具体的な年月を公表していない。
   ⚠️ 「2003 + 15」の逆算は推測であり、本書は行っていない。**
   → **メゾンへの直接照会、または年齢ゲートを通過した上での製品頁の再取得が要る。**
3. 🔴 **`Vintage 2015` についてのメゾン自身の記述。**
   🔴 **`/fr-fr/product/vintage/2015` は実在するが年齢ゲートの向こうにあり、Wayback にも本文が無い。**
   🔴 **OBP 3 行のうち 1 行がこれで空白になっている。本ドシエの最大の欠落である。**
   → **年齢ゲートを通過できる取得手段（ブラウザ経由）での再訪に、明確な価値がある。**
4. ⚠️ **Dom Pérignon ブランドとしての最初のヴィンテージ発売年。**
   **メゾンは 1668 年の「創設神話」と、1990 年以降の Chef de Cave の系譜しか書いていない。
   その間（18〜20 世紀）の沿革が生産者資料に存在しない。**
5. ⚠️ **畑の所在。**
   🔴 **村名・区画・面積・grand cru 比率のいずれもメゾンが公表していない。
   これは「探し漏れ」ではなく「メゾンが書かない」である可能性が高いが、
   年齢ゲートの向こうに `La Maison` 系の頁が存在するため断定できない。**
6. ⚠️ **`Jaques Giraco`（現行 mentions légales の Directeur de Publication）の身元。**
   🏛 **登記簿の役員一覧に該当氏名が無い。表記揺れ（`Jacques` の誤植）の可能性もある。**
7. ⚠️ **Vincent Chaperon の 2026 年時点での在任。**
   **生産者ドメイン上で確認できたのは 2022 年以前のキャプチャまでである。**
8. ⚠️ **canonical に載せるときの `name` をどれにするか。**
   🔴 **canonical は同じ製品ラインを `Dom Pérignon Brut`（2013 ほか 6 件）と
   `Dom Pérignon Vintage`（2015）の 2 通りで持っている。**
   ✅ **メゾンの SKU 名は `Dom Pérignon Vintage Millésimé` であり、`Brut` は使われていない。**
   → 🔒 **設計判断であり本書では決めない。**
9. 🔴 ⚠️ **`plénitude`（リリース段階）を canonical のどの粒度に置くか。**
   🔴 **メゾンの言葉では P2 は「同一ヴィンテージのワインの第二の生」であって別キュヴェではない。
   `cuvée × vintage` では P1 と P2 を区別できない。**
   → 🔒 **`V-1` / `CDX-8` の同一性軸そのもの。設計判断であり本書では決めない。番号も開いていない。**
