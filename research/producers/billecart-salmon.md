# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical にこの生産者のレコードは 4 件存在する**
> （`billecart-le-reserve` / `billecart-louis-salmon-2012` / `billecart-brut-rose` / `billecart-elizabeth-salmon-2012`）。
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagne-billecart.fr／公式フィッシュ・テクニックで確認**（一次資料）
> `🏛` **公的登録**（recherche-entreprises.api.gouv.fr / Agence Bio / Ecocert / TTB COLA / AFNIC）
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.champagne-billecart.fr/`（FR 原本）**
> 走査元: **`robots.txt` が `Sitemap: https://www.champagne-billecart.fr/sitemap.xml` を明示 → 79 URL 取得**
> 併用: ✅ **公式フィッシュ・テクニック 5 点（`/storage/products/fiches/`、全点 `application/pdf`・テキストレイヤーあり）**
>
> ---
>
> 🔴 **本ドシエ最大の収穫 —— タスク前提 3 つが実測で覆った。**
>
> **① OBP 1 行目 `'Le Réserve,' Extra Brut` は誤植ではない。メニューは名称もドザージュも正しい。**
> **公式フィッシュ・テクニックの見出しは `LE RÉSERVE`、スペック欄は `Dosage Extra Brut`。**
> **メゾンは NV レンジ全体を `Brut Réserve → Le Réserve`、`Brut Rosé → Le Rosé` へ改称し、
> かつ Collection レンジのドザージュを `Extra Brut` に移している。**
> **したがって「`réserve` は女性名詞だから `Le Réserve` は誤り」という前提は、
> 造り手自身の現行表記によって否定される。** → §Important Cuvées 1 / §Canonical Conflict
>
> **② OBP 4 行目の `Elizabeth Salmon`（z）も「メニューの誤り」と断定できない。**
> 🏛 **TTB COLA に `CUVEE ELIZABETH SALMON`（z）で承認された米国向けラベルが実在する**
> （2015-03-16 / 2015-12-22 / 2016-01-05、brand `BILLECART SALMON` ほか）。
> **フランス公式は一貫して `Élisabeth`。米国流通ラベルに `z` 綴りが実在した、という二層構造である。**
> → §Canonical Conflict `C-1` 族
>
> **③ canonical に `Élisabeth Salmon` のレコードは「存在する」。gap ではない。**
> 🔍 **`billecart-elizabeth-salmon-2012`（`name='Cuvée Elisabeth Salmon Brut Rosé'`）が実在し、
> かつ canonical はこの生産者に「白」と「ロゼ」の 2 本立てのプレスティージュを別レコードで持っている。**
> **すなわち Taittinger `Comtes de Champagne` で提起された `C-6`（1 レコードが 2 色を兼ねる形）は、
> Billecart-Salmon には当てはまらない。** **4 行目が `unresolved` な理由は色の軸ではなく、綴りである。**
>
> 🔴 **第四の収穫 —— 🏛 公的登録が、公式サイトの沈黙している事実を持っている。**
> **Agence Bio に `numeroBio 1813` で登録があり、Ecocert France（`FR-BIO-01`）の証明書が `Active`。**
> **ただし `activites` は `Préparation` のみ、`mixite: "Oui"`。** → §Farming。**言い方を誤ると即座に嘘になる。**
>
> ⚠️ **調査上の制約**
> **① `/fr/la-maison/*` の一部は `fullPage.js` による全画面スクロール構成で、
>    静的取得した HTML の中に本文は入っているが、素朴なタグ剥がしでは footer しか取れない。**
>    **本書は正規表現を修正して本文を取得し直している。**
> **② `myorigin.billecart.fr`（公式が全フィッシュから参照するセパージュ開示サイト）は本調査で内容未取得。** → Open Questions 6

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Billecart-Salmon** |
| **公式表記** | ✅ **Champagne Billecart-Salmon**／✅ **Maison Billecart-Salmon**（両方が公式サイト上で併用） |
| **タグライン** | ✅ **`L'instinct d'exception`**（トップページ）／✅ **「L'instinct d'exception depuis 6 générations.」**（沿革ページ見出し）⚠️ **世代数は下記の通り公式内で揺れる** |
| 🔴 **法人（公式）** | ✅ **`Champagne Billecart-Salmon`、Société anonyme。**<br>**資本金 `7.104.000 euros`／`immatriculée au RCS de Reims sous le numéro Siret : 335 480 075`／TVA `FR53335480075`**（mentions légales） |
| 🔴 **法人（🏛 公的登録）** | 🏛 **SIREN `335480075`／`nom_complet: CHAMPAGNE BILLECART-SALMON (GCB)`／`nom_commercial: GCB`**<br>🏛 **SIRET 本店 `33548007500019`／NAF `11.02A`／`date_creation: 1954-01-01`／`etat_administratif: A`** |
| **住所（公式）** | ✅ **`40 rue Carnot – BP8 – 51160 AY-CHAMPAGNE`**（mentions légales） |
| **住所（🏛 登録）** | 🏛 **`40 RUE CARNOT 51150 AY-CHAMPAGNE`**／`code_commune 51030`／`lat 49.0462, long 4.0363` |
| ⚠️ **郵便番号の揺れ** | ⚠️ 🔴 **`51160`（公式 mentions légales・Agence Bio・Ecocert）と `51150`（企業登録）で食い違う。**<br>**同一の `code_commune 51030` を指しているため同一施設と判断したが、どちらが現行かは確定していない。** |
| 🔴 **コミューン名** | 🏛 **登録上のコミューン名は `AY-CHAMPAGNE`。**<br>🏛 **Agence Bio は同一の `codeCommune: 51030` に対して、`Lieux d'activité` を `Mareuil sur Ay`、`Siège social` を `AY-CHAMPAGNE` と両方の名で持っている。**<br>→ 🔴 **INSEE コードが同一である以上、両者は同じコミューンを指す。**<br>⚠️ **`Mareuil-sur-Aÿ` は公式が「berceau familial（一族のゆりかご）」として語り続ける地名であり、行政上の現行コミューン名は `Aÿ-Champagne` である。** → Open Questions 2 |
| **電話 / メール** | ✅ **`+33 (0) 3 26 52 60 22`／`billecart@champagne-billecart.fr`** |
| **サイト掲載責任者** | ✅ **`Directeur de Publication : Maxime Renault`** |
| **ホスティング** | ✅ **OVH（SAS、RCS Roubaix n° 424 761 419、2 rue Kellermann - 59100 Roubaix）** |
| 🔴 **当主（7 代目）** | ✅ **Mathieu Roland-Billecart（1981 年生）。**「**Aujourd'hui, c'est Mathieu Roland-Billecart, 7ème génération qui est à la tête de la maison**」<br>🏛 **Agence Bio の `gerant` 欄も `Mathieu Roland-Billecart`。公式と公的登録が一致する。** |
| **副責任者** | ✅ **Antoine Roland-Billecart（1961 年生）、`directeur adjoint en charge de l'export`** |
| **総支配人** | ✅ **Alexandre Bader（`Directeur Général`）**。公式は「Le globetrotteur」と紹介 |
| 🔴 **醸造長** | ✅ **Florent Nys（`chef de cave`）。**「**François Domi の目の下で 2005 年から働き、いまや Billecart-Salmon の署名の保証人**」<br>🔴 **全 5 点のフィッシュ・テクニックが `Par Florent NYS, œnologue et chef de cave de la Maison Billecart-Salmon` で署名されている。** |
| **畑・ワイン責任者** | ✅ **Denis Blée（`directeur vignoble et vins`）。「20 年ほど」在任。剪定から収穫、樽熟成までを見る** |
| **創業年** | 🔴 ✅ **1818 年。**「**Nicolas François Billecart épouse Elisabeth Salmon. De leur union, ils décident de fonder la Maison Billecart-Salmon à Mareuil-sur-Aÿ, le berceau familial.**」<br>✅ **`Depuis sa création en 1818`**（`/les-hommes`）／✅ **サイトタイトル `Maison Familiale fondée en 1818`** |
| ⚠️ **世代数** | ⚠️ 🔴 **公式内で食い違う。**<br>**`/les-hommes`: 「Depuis sa création en 1818, ce sont **7 générations consécutives**」**<br>**`/histoire` 2018 の項: 「200 ans d'indépendance et de savoir-faire depuis **7 générations**」**<br>**同じ `/histoire` の直下の見出し: 「L'instinct d'exception depuis **6 générations**.」**<br>→ **7 が優勢だが、公式が 6 とも書いている。** → §Staff Notes ⚠️ ⑥ |
| **認証（公式）** | ✅ **HVE（Haute Valeur Environnementale）／VDC（Viticulture Durable en Champagne）＝ 2017 年／ISO 50001（APAVE）＝ 2023 年** |
| 🔴 **認証（🏛 登録）** | 🏛 🔴 **Agence Bio `numeroBio 1813`。Ecocert France `FR-BIO-01`、`etatCertification: ENGAGEE`。**<br>🏛 **`datePremierEngagement: 2019-07-31`／`dateEngagement: 2022-07-11`**<br>⚠️ **`activites: [Préparation]` のみ／`mixite: "Oui"`。** → §Farming。**「オーガニックのメゾン」とは言えない。** |
| **canonical id** | 🔍 **4 件**（下記 §Canonical Conflict） |

---

## Overview

✅ **1818 年、Nicolas François Billecart と Élisabeth Salmon の結婚から生まれたメゾン。
マルイユ＝シュル＝アイ（現・行政名 Aÿ-Champagne）の 40 rue Carnot に本拠を置き、
7 代にわたって家族の手を離れていない。**

🔴 ✅ **公式が自らの署名として名指しするのは、ただ一つ —— 低温での長い発酵。**
「**低温で醸造することによって発酵の過程が遅くなり、軽やかで繊細な香りを促し、
果実の純粋さのすべてを表現させる。これこそが Billecart-Salmon のスタイルの真の署名である。**」
（`/la-maison/la-cuverie`）

🔴 ✅ **その技術は 1958 年に、5 代目 Jean Roland-Billecart が持ち込んだものである。
そして公式はその着想源をはっきり書いている —— ビール醸造家である。**
「**伝統的な醸造家（brasseurs）の方法に着想を得て、彼はキュヴェ内での醸造過程に、
低温でのより長い発酵、次いで冷却による澱下げ（débourbage à froid）を導入した。
この技術が Billecart-Salmon のワインを特徴づける新鮮さと繊細さをもたらす。**」（`/histoire` 1958 年の項）

🔴 ✅ **メゾンは「全部自社畑」ではない。公式が数字で書いている。**
「**メゾンのシャンパーニュは何よりもまず、100 ヘクタールのドメーヌを厳格に慈しみ、
シャンパーニュの 40 のクリュにおいて総計 300 ヘクタールの面積からブドウを調達する、人の独自の savoir-faire に立脚する。**」
→ 🔴 **自社畑 100 ha ／調達を含めた総面積 300 ha。** → §Staff Notes ⚠️ ②

🔍 **THÉSEUS における状態は Taittinger とは正反対で、「4 件そろっているのに 2 本が当たらない」形。
canonical は OBP 4 行に対応する 4 レコードをすべて持っているが、
alias で当たっているのは 2 本だけで、`ROSÉ` セクションの 2 本がともに `unresolved` である。
原因は色の軸ではなく、① メニューがキュヴェ名を印字していない（3 行目）、
② 綴りが `Elizabeth` / `Elisabeth` で割れている（4 行目）、の 2 点。**

---

## History

✅ **公式沿革ページ（`/fr/la-maison/histoire`）は `fullPage.js` の全画面構成だが、本文は静的 HTML に含まれる。**

| 年 | 出来事 ✅ |
|---|---|
| 🔴 **1818** | 🔴 **`Nicolas François Billecart` が `Elisabeth Salmon` と結婚。**「**二人の結合から、彼らは一族のゆりかごであるマルイユ＝シュル＝アイに Maison Billecart-Salmon を創設することを決める。**」<br>🔴 **同時に Nicolas François は妻の兄弟 `Louis Salmon` と組む。**「**彼が商業活動を担当し、œnologie に情熱を持つ義兄がワインの造りに専念する。**」<br>→ 🔴 **`Louis Salmon` と `Élisabeth Salmon` は兄妹（姉弟）であり、夫婦ではない。** → §Staff Notes ⚠️ ④ |
| **1900** | **パリ万国博覧会に参加。シャンパーニュ商業組合が建てた `Palais du Champagne` のメセナの一つとなり、他の大ブランドと並んでグラス売りされる** |
| **1919** | **`Charles Roland-Billecart` が復員し、蔵に 75,000 本しか残らない空のメゾンを見出す。長い年月をかけて立て直し、1936 年には 217,000 本以上を販売** |
| 🔴 **1958** | 🔴 **`Jean Roland-Billecart`（Charles の長男）が質的革命に着手。伝統的なビール醸造家の方法に着想を得て、低温でのより長い発酵、次いで `débourbage à froid` を導入** |
| **1964** | **同名の創設者への敬意として、キュヴェ `Nicolas François` の最初のミレジムが誕生** |
| 🔴 **1970 年代** | 🔴 **「長らく二次的なシャンパーニュと見なされていた」ロゼに Jean Roland-Billecart が再び取り組む。**「**目標は、非常に淡い色調のローブを持ち、その味わいが新鮮さといくつかの繊細な赤い果実の調子によって際立つシャンパーニュを得ることだった。賭けは成功し、`Brut Rosé` はメゾンの象徴的なキュヴェとなった。**」<br>→ 🔴 **公式が「ロゼの伝統」の起点として書くのは 1970 年代である。** → §Canonical Conflict |
| **1993** | **`François Roland-Billecart`（Jean の長男、チェス愛好家）が経営を握る。大型量販店からシャンパーニュの在庫を全量買い戻し、独立カーヴィストと高級ガストロノミーへ流通を集中させる** |
| 🔴 **1995** | 🔴 **キュヴェ `Clos Saint-Hilaire` 創出。**「**数年の入念な手入れののち、1995 年の収穫は remarquable だった。これがこの類まれなキュヴェの第 1 ミレジムとなる。**」**各ボトルは番号入り、各ミレジムは 3,500〜7,500 本を超えない** |
| **1999** | **キュヴェ `Brut 1959` が、Richard Juhlin がストックホルムで催した最大手メゾン 150 ミレジムのブラインド試飲で、専門家審査団により「`champagne du Millénaire`（千年紀のシャンパーニュ）」に選ばれる。1961 年が 2 位** |
| 🔴 **2000** | 🔴 **新しいキュヴリー創設。**「**主要な選択は、セパージュと区画のトレーサビリティを尊重できる小型のサーモレギュレーテッド・タンクに集中している。**」 |
| **2010** | **祖先の醸造法への回帰が、400 を超える樽と 2 基のフードルを集めた壮麗な chai として結実。ミレジメ・ワインおよびキュヴェ `Brut Sous Bois` を高める** |
| **2018** | **新しいフードル蔵を開設。「卓越性の探求のなかで、最良の樽職人から 80 ヘクトリットルのフードル 24 基が厳格に選ばれた」** |
| 🔴 **2018** | 🔴 **メゾンが「7 世代にわたる 200 年の独立と savoir-faire」を祝う。二百年祭のために特別にアッサンブラージュされたキュヴェ `200` が限定版として提供され、`1818 本のマグナム`（番号入り）が世界に出た** |

### ✅ 歴代（公式の「Portrait de famille」）

| 世代 | 公式の呼称 | 名前 |
|---|---|---|
| **1** | **Les fondateurs passionnés** | 🔴 **NICOLAS FRANÇOIS BILLECART 1794–1858 ／ ÉLISABETH SALMON 1797–1860** |
| **2** | L'intrépide aventurier | **CHARLES BILLECART 1823–1888** |
| **3** | Le dandy esthète | **POL BILLECART 1854–1916** |
| **4** | Le pilote hardi | **CHARLES ROLAND-BILLECART 1886–1963** |
| **5** | Le perfectionniste attentif | 🔴 **JEAN ROLAND-BILLECART（1923 年生）** |
| **6** | Le poète visionnaire & l'ambassadeur enchanteur | **FRANÇOIS ROLAND-BILLECART（1947 年生）／ ANTOINE ROLAND-BILLECART（1961 年生）** |
| **7** | La relève | 🔴 **MATHIEU ROLAND-BILLECART（1981 年生）** |

🔴 ⚠️ **この一覧で公式は 1 代目を `ÉLISABETH SALMON`（アクセントつき）と書く。
一方、キュヴェのページとフィッシュ・テクニックの本文は `Elisabeth Salmon`（アクセントなし）と書く。
そして商品見出しは `ÉLISABETH SALMON 2012` である。**
→ 🔴 **アクセントの有無は公式内で揺れている。`z` 綴りは公式には一度も現れない。** → §Canonical Conflict

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| **本拠** | ✅ **`40 rue Carnot`、Mareuil-sur-Aÿ（🏛 行政上は `Aÿ-Champagne`、`code_commune 51030`）** |
| 🔴 **自社畑** | 🔴 ✅ **100 ヘクタール**（`un domaine de 100 hectares`） |
| 🔴 **調達を含む総面積** | 🔴 ✅ **300 ヘクタール／シャンパーニュの 40 クリュ**（`s'approvisionnent sur une superficie totale de 300 hectares en raisins dans 40 crus de la Champagne`） |
| 🔴 **産地の重心** | 🔴 ✅ **「醸造に使われるブドウの大部分は、エペルネから半径 20 km の範囲に由来する。そこではモンターニュ・ド・ランス、コート・デ・ブラン、ヴァレ・ド・ラ・マルヌの土地に、ピノ・ノワール、シャルドネ、ムニエのグラン・クリュが共存している。**」 |
| 🔴 **カーヴ** | 🔴 ✅ **白亜（craie）のカーヴ、2 キロメートルの通路。**「**17 世紀以来、これらの白亜のカーヴがわれわれのワインを見守り、高めてきた**」／「**17 世紀および 19 世紀に遡る白亜のカーヴ**」 |
| 🔴 **熟成方針** | 🔴 ✅ **「ノン・ミレジメのシャンパーニュは 3 年から 4 年のあいだ十全に開花する。すなわち appellation が定める規則の 2 倍の長さである。他方ミレジメのキュヴェは、成熟のすべてを明かすまでに 10 年を待つ。**」 |
| 🔴 **モノポール** | 🔴 ✅ **`Clos Saint-Hilaire` —— 1 ヘクタール。**下記参照 |

### 🔴 ✅ Clos Saint-Hilaire（**OBP には無いが、客が必ず訊く**）

✅ **「このユニークなキュヴェ `Blanc de Noirs` は、マルイユ＝シュル＝アイの守護聖人の名を担う。
この 1 ヘクタールのクロは厳しい規範に応える —— 単一の区画であり、囲われ、一区画にまとまり、
その場所に完全な醸造設備を備えていること。**」

✅ **6 代目 François Roland-Billecart の一人称の証言（公式サイト掲載）** —
「**1950 年代、祖母はわれわれの余暇のために、マルイユ＝シュル＝アイの家に隣接する、
いくらかのブドウ樹と花と果樹に彩られたこの緑地を充てていた。
この例外的なテロワールの潜在力を見抜いて、家族は 1964 年にそこに最初のピノ・ノワールを植える。
われわれはこのピノ・ノワールを小さなブルゴーニュ樽で白に仕込むことを試みる —— 例外的なシャンパーニュが生まれようとしていた。
数年の入念な手入れののち、1995 年の収穫は remarquable だった。これがこの類まれなキュヴェの第 1 ミレジムとなる。
マルイユ＝シュル＝アイの教会の守護聖人に敬意を表して、これを Clos Saint-Hilaire と名づけた。
以来、各ボトルには番号が振られている。**」

🔴 ✅ **馬耕。**「**Maison Billecart-Salmon はシャンパーニュの祖先の方法に立ち戻ることを決め、
挽き馬（cheval de trait）が数年前から Clos Saint-Hilaire に再び姿を現している。
この土壌の手入れ方法は多孔性と生物多様性を改善する。根が深く発達し、
土壌から抽出されたミネラルが、より小さく凝縮した果粒の成長を促し、このテロワール固有の味わいを明かす。**」

✅ **生産量: 現行の 2009 年について「各ミレジムは非常に少ない flacon しか持たない（4,500 本）」／
沿革ページは「各ミレジムは 3,500 〜 7,500 本を超えない」。**
⚠️ **この 2 つは矛盾ではなく「レンジと個別年」の関係と読めるが、staff は年ごとの本数を断定しない。**

✅ **提供温度はカーヴ温度（12/14°）。ピノ・ノワール 100%、樽で仕込む。ドザージュは「非常に少なく」とだけ書かれ、数値は無い。**

❓ **公式に無い**: 所有クリュの一覧、区画名の全体、買いブドウの供給者名、自社畑 100 ha の村別内訳。

---

## Farming

🔴 **本節は「公式サイトと公的登録が別のことを言っている」という理由で、本ドシエで最も慎重を要する節である。**
**両方を書き、どちらも断定しない。**

### ✅ 公式サイトが名指しする認証（`/la-maison/engagements-durables`）

✅ **「Haute Valeur Environnementale および Viticulture Durable en Champagne として 2017 年に資格を得るよりずっと前から、
Maison Billecart-Salmon はすでに自然を尊重した畑の管理に心を砕いていた。」**

| 認証 | 公式の記述 |
|---|---|
| 🔴 **VDC**（Viticulture Durable en Champagne） | ✅ **2017 年。**「**シャンパーニュの栽培者の自発的かつ日常的な関与を通じた、持続可能な発展の原則の栽培への適用。**」🔴 **「メゾンはその VDC 集団を通じてパートナー栽培者に認証の重要性を啓発している。2021 年、その調達の 75% が VDC 認証済みである。**」 |
| 🔴 **HVE** | ✅ **2017 年。**「**この環境認証は 3 つの要求水準からなる。そして最も高い水準であるレベル 3 が『Haute valeur environnementale』の証を得させる。4 つの指標が考慮される —— 生物多様性、施肥、植物防疫、水の管理。**」 |
| 🔴 **ISO 50001** | ✅ **2023 年、`APAVE` により取得。エネルギー管理。「消費を最適化し、コストとカーボンフットプリントを削減・抑制するための関与を示す」** |

### 🔴 ✅ 公式の「10 の鍵となる日付」（`Nos actions en 10 dates clés`）

| 年 | 公式の記述 |
|---|---|
| **2010** | 🔴 **`Premiers essais bio & permaculture`（有機とパーマカルチャーの最初の試み）** |
| **2014** | **`Fin des intrants plastiques`（プラスチック資材の終了）** |
| **2017** | **`Certification « VDC »`** |
| **2018** | **`100% amendements bio`（土壌改良材の 100% 有機化）** |
| **2019** | **`Préparation à base de plantes`（植物由来の調製剤）** |
| 🔴 **2020** | 🔴 **`100% sans désherbant`（除草剤 100% 不使用）** |
| 🔴 **2021** | 🔴 **`10 hectares en conversion bio`（10 ヘクタールが有機転換中）** |
| **2022** | **`Réserve biodiversité au Clos Saint-Hilaire`** |
| **2023** | **`Certification ISO 50001`** |
| ⚠️ **2025** | ⚠️ 🔴 **`100% du vignoble certifié`（畑の 100% が認証済み）。**<br>🔴 **公式はここで「何の」認証かを書いていない。文脈上 VDC / HVE と読むのが自然だが、公式はそう明記していない。** → §Staff Notes ⚠️ ③ |

### 🔴 🏛 公的登録が持っていて、公式サイトが沈黙している事実

🔴 🏛 **企業登録（`recherche-entreprises.api.gouv.fr`）の本店レコードに `liste_id_bio: [1813]` が入っている。**
**これを手がかりに Agence Bio のオープンデータを引くと、次が得られる。**

| 項目 | 🏛 Agence Bio / Ecocert の値 |
|---|---|
| **numeroBio** | **1813** |
| **raisonSociale** | **CHAMPAGNE BILLECART-SALMON** |
| **siret** | **33548007500019**（企業登録の本店 SIRET と一致） |
| **gerant** | **Mathieu Roland-Billecart**（公式の当主と一致） |
| 🔴 **認証機関** | 🔴 **Ecocert France、`numeroControleEu: FR-BIO-01`** |
| 🔴 **状態** | 🔴 **`etatCertification: ENGAGEE`**／**Ecocert 証明書ページの表示は `Active`** |
| 🔴 **規格** | 🔴 **`(EU) 2018/848 [FR]`**（EU 有機農業規則） |
| 🔴 **証明書の適用範囲** | 🔴 **`Manufacturer & Processor` ／ `Alcoholic Beverages`** |
| **日付** | **`datePremierEngagement: 2019-07-31`／`dateEngagement: 2022-07-11`** |
| **生産** | **`Vins de raisin`（コード 11.02）、`etatProduction: AB`、`anneeReferenceControle: 2026`** |
| 🔴 **活動区分** | 🔴 ⚠️ **`activites: [{"nom": "Préparation"}]` のみ。`Production`（＝栽培）は入っていない。** |
| 🔴 **混合経営** | 🔴 ⚠️ **`mixite: "Oui"`** |
| **年鑑上の区分** | **`Entreprise de transformation Agro-Alimentaire - Cave`** |
| **siteWebs** | **`[]`（空）** |

🔴 ⚠️ **この 2 つを重ねると、事実はこうなる。**
**① メゾンは EU 有機規則のもとで Ecocert に登録されており、その証明書は現に有効である。**
**② ただし登録上の活動は「Préparation（醸造・加工）」であり、栽培活動としての登録ではない。**
**③ `mixite: "Oui"` は、有機と非有機を併せ持つ事業者であることを意味する。**
**④ 公式サイト自身が「2021 年に 10 ヘクタールが有機転換中」と書いており、全畑ではない。**
→ 🔴 **したがって「Billecart-Salmon はオーガニックのメゾンです」は言ってはならない。**
→ 🔴 **同時に「有機認証は持っていません」も言ってはならない。両方とも事実に反する。** → §Staff Notes ⚠️ ③

⚠️ **`Demeter` / `Biodyvin` / `biodynamie` の語は、公式サイトにも Agence Bio のレコードにも一切現れない。**
⚠️ **公式サイトは `bio` の語を「essais bio」「amendements bio」「conversion bio」の 3 か所でしか使わず、
`Ecocert` `Agence Bio` `AB` `agriculture biologique` の語を一度も使っていない。**
→ 🔴 **すなわち、有機認証の存在は公的登録側からしか分からない。**

### ✅ 具体的な栽培実務（公式が名指しするもの）

🔴 ✅ **「ブドウ樹のいくつかの病害と戦うために、Billecart-Salmon は VDC 認証を超えて自然の療法を用いる。」**

| 対象 | 公式の「自家製の療法」 |
|---|---|
| **ODïUM（うどんこ病）** | ✅ **「硫黄またはスギナ（prêle）をベースとする自然の処理」** |
| **MANGE-BOURGEONS（芽を食う害虫）** | ✅ **「植物または微生物に由来する生物学的製品」** |
| **MILDIOU（べと病）** | ✅ **「自然由来の穏やかな医学（bio／銅）を優先する。合成製品の使用は最後の手段としてのみに限る」** |
| **POURRITURES（腐敗）** | ✅ **「日の出側の早期除葉（effeuillage précoce）の実践」** |

✅ **生物多様性**: **Clos Saint-Hilaire の 1 ヘクタールの花畑に養蜂箱 3 基を設置。うち 1 基はメゾンのワインを受けた樽で造られている。採れた花の蜜は Clos Saint-Hilaire の rucher に由来する。**
✅ **カーボン**: **電動のエンジャンブール（enjambeur électrique）と電気自動車を車両群に導入。原材料は短い流通経路を優先。**
✅ **水**: **「ワインを造るには多くの水が要る」ため、水道メーターで従業員の意識を高める日常的な持続可能管理。**

---

## Winemaking

### 🔴 メゾンの署名 —— 低温発酵と `débourbage à froid`

🔴 ✅ **`/la-maison/la-cuverie`（公式）** —
「**ワインの品質を絶えず向上させようと心を配り、メゾンは 1950 年代に `débourbage à froid` の技術を、
次いでより長い低温発酵のためのステンレスタンクの使用を確立した。
キュヴリーは主に小型のサーモレギュレーテッド・タンク（`47 hectolitres`）に集中しており、
それがセパージュと区画のトレーサビリティを尊重することを可能にする。
このクリュごと・セパージュごとの醸造が、テロワールの表現のあらゆるニュアンスを保つことを可能にする。
低温で醸造することによって発酵の過程が遅くなり、軽やかで繊細な香りを促し、
果実の純粋さのすべてを表現させる。これこそが Billecart-Salmon のスタイルの真の署名である。**」

⚠️ 🔴 **重大な注意 —— 公式の 2 ページが導入の順序を逆に書いている。**

| 出典 | 順序 |
|---|---|
| ✅ **`/histoire`（1958 年の項）** | 「**低温でのより長い発酵、`puis`（次いで）`débourbage à froid`**」 |
| ✅ **`/la-maison/la-cuverie`** | 「**`débourbage à froid` の技術を、`puis`（次いで）より長い低温発酵のためのステンレスタンクの使用を**」 |

→ 🔴 **どちらが先かは公式内で確定していない。両方を記録し、いずれも主張しない。**
⚠️ **また年も `1958`（histoire）と `dans les années 50`（cuverie）で粒度が違う。** → §Staff Notes ⚠️ ⑤

✅ **温度・時間の具体的数値は公式に一切無い。**「低温（basse température）」「より長い（plus longue）」という定性表現のみ。
🔴 **したがって本ドシエは摂氏の数値を一切書かない。** → Open Questions 4

### ✅ 木樽

| 年 | 公式の記述 |
|---|---|
| **2010** | ✅ **「祖先の醸造法への回帰が、`400 を超える樽と 2 基のフードル` を集めた壮麗な chai として結実」** |
| **2018** | ✅ **「新しいフードル蔵の開設。`80 ヘクトリットルのフードル 24 基` が最良の樽職人から厳格に選ばれた」** |

### 🔴 ✅ 公式フィッシュ・テクニックの全スペック（**5 点の PDF から機械的に転記**）

| キュヴェ | セパージュ | 醸造 | リザーヴ | 熟成 | ドザージュ |
|---|---|---|---|---|---|
| 🔴 **LE RÉSERVE**（NV）⭐OBP 1 | 🔴 **Pinot Noir 28% / Chardonnay 29% / Meunier 43%**（**2020 年基準**） | **`Vinification majoritairement en cuves à basse température`** | 🔴 **`Plus de 50% de vins de réserve`** | 🔴 **`en moyenne : 50 mois`** | 🔴 **`Dosage Extra Brut`（数値なし）** |
| 🔴 **LE ROSÉ**（NV）⭐OBP 3 候補 | 🔴 **Chardonnay 45% / Pinot Noir 35% / Meunier 20%**（**2020 年基準**）「**うち一部が赤に仕込まれる**」 | **`Vinification en cuves à basse température`** | — | 🔴 **`36 mois`** | 🔴 **`Dosage Extra Brut`（数値なし）** |
| **LE BLANC DE BLANCS**（NV） | **Chardonnay 100%、Côte des Blancs の村のグラン・クリュ: Avize / Chouilly / Cramant / Mesnil-sur-Oger** | **`Vinification en cuves à basse température`** | **`De 20 à 50%`** | **`5 ans`** | **`Dosage Extra Brut`** |
| 🔴 **LOUIS SALMON 2012** ⭐OBP 2 | 🔴 **`100% Chardonnay Grands Crus de la Côte des Blancs : 60% Mesnil-sur-Oger, 23% Cramant, 11% Chouilly et 6% Oiry`** | 🔴 **`25% des vins sont vinifiés en fûts`** | — | 🔴 **`115 mois`** | 🔴 **`3.9 g/l`** |
| 🔴 **ÉLISABETH SALMON 2012** ⭐OBP 4 | 🔴 **`100% grand cru et premier cru` / `55% Chardonnay de Chouilly, Avize, et Mesnil-sur-Oger` / `45% Pinot Noir de Mareuil-sur-Aÿ et Verzenay`** | 🔴 **`Moins de 10% du Pinot Noir est vinifié en rouge à partir de raisins de vieilles vignes de Mareuil-sur-Aÿ, exposées plein sud` ／ `2,90% des vins sont vinifiés en fûts`** | — | 🔴 **`115 mois`** | 🔴 **`3,8 g/l`** |

### ✅ 参考 —— OBP 外だが同レンジの公式スペック

| キュヴェ | 記述 |
|---|---|
| **BRUT NATURE**（NV） | **PN 30 / Ch 30 / Meunier 40。`Non dosé`。`Vinification en cuves`。`Fermentation malolactique`。`50 à 60% de vins de réserve`。`48 mois`** |
| **LE SOUS BOIS**（NV） | **Ch 43（Côte des Blancs GC）/ PN 28（Montagne de Reims・Aÿ・Mareuil-sur-Aÿ の 1er et GC）/ Meunier 29（2017 年基準）。🔴 `Vinification en vieux fûts à basse température`。リザーヴは 2006 年まで遡りうる。`5 ans`。`Dosage Extra Brut`** |
| **VINTAGE 2016** | **`100% de Grands crus`。PN 66 / Ch 34。`Vinification en cuves`。`64 mois`。🔴 `Dosage 1.9 g/l`** |
| **DEMI-SEC**（NV） | **PN 30 / Ch 30 / Meunier 40。🔴 `Dosage : 40 g/l`。`Vinification en cuves`。🔴 `Fermentation malolactique partielle`。`30 mois`** |

🔴 ⚠️ **マロラクティック発酵について、公式は極めて限定的にしか語らない。**
**`Brut Nature` に `Fermentation malolactique`、`Demi-Sec` に `Fermentation malolactique partielle` と書くのみ。**
🔴 **`Le Réserve` / `Le Rosé` / `Le Blanc de Blancs` / `Louis Salmon 2012` / `Élisabeth Salmon 2012` の
5 点のフィッシュ・テクニックには、マロラクティックについての記述が一切無い。**
→ 🔴 **したがって本ドシエは、OBP の 4 本について MLF の有無を一切主張しない。** → §Staff Notes ⚠️ ⑦

⚠️ **アルコール度数・デゴルジュマン日・生産本数（Clos Saint-Hilaire を除く）・
ルミュアージュの方式・圧搾比率は、公式に一切記載が無い。**
⚠️ **「手作業デゴルジュマン」を裏づける公式記述は本調査で見つからなかった。** → §Canonical Conflict

---

## Style

### ✅ 公式テイスティングノート（**OBP 関連 4 本。すべて Florent Nys の署名つき**）

| キュヴェ | 公式ノート（フィッシュ・テクニックより） |
|---|---|
| 🔴 **LE RÉSERVE**<br>「Harmonie et pureté」 | **「`Le Réserve` は軽やかで繊細で調和のとれたシャンパーニュのワインである。そのアッサンブラージュは、マルヌの最良のテロワールに由来する Pinot Noir、Chardonnay、Meunier の、**🔴 **平均して 15 年分の収穫から構成される。**」<br>**A L'ŒIL**: 淡い金の照り、非常に躍動的な泡の繊細さと、豊かで持続する泡の保ちに支えられる。輝く若さの明るい煌めき。<br>**AU NEZ**: 明快で精確な強度と軽やかな性格、続いて弾ける自然な果実の純度。**白い仁果と新鮮な果実**の芳香的精確さを備え、花的で香ばしくビスケット的な誘惑へ向かう。<br>**EN BOUCHE**: 繊細なテクスチャーの微妙な快楽が美しい芳香の凝縮と結びつく。**林檎、歯ごたえのある洋梨、柑橘**、そして焙煎の調子。**新鮮さとミネラリティを刻んだ、大きく持続する終盤。**<br>**提供温度 8°–10°** |
| 🔴 **LE ROSÉ**<br>「Un champagne de cœur」 | **「ロゼのなかの基準（`Référence parmi les rosés`）。」**<br>**A L'ŒIL**: 非常に明るく輝く強度のローブ、美しい淡いピンクの色調をまとう。優美な発泡を備えた優雅な視覚。<br>**AU NEZ**: **小さな赤い果実と柑橘の皮**の美味なる誘惑に向かう、繊細で細やかな香り。花的で爽やかな、大きな繊細さの芳香の輝き。<br>**EN BOUCHE**: 流れるようにクリーミーな甘美さの絶妙な触感、**野いちご**の性格を持つ非常に高貴な観念へと進み、**わずかにフランボワーズ的な**終盤へ。**顕著な精確さの、調和して美味な均衡。**<br>**提供温度 8°–10°** |
| 🔴 **LOUIS SALMON 2012**<br>「Pureté et minéralité」 | **「`Louis Salmon 2012` は remarquable な年の最良のシャルドネの精髄のすべてを明かす。**🔴 **Cramant はミネラリティを、Chouilly と Oiry は繊細さを、Mesnil-sur-Oger は構造と長命さをもたらす。**」<br>**A L'ŒIL**: 黄と緑のニュアンスに彩られた繊細な照りを持つ、淡い金のローブの結晶的な外観。<br>**AU NEZ**: **細かくヘーゼルナッツを帯びた花的な優雅さと、栗のパン。白亜的な性格を持つ、均衡した結晶的な芳香プロファイル（生バターとカスタードクリーム）。**<br>**EN BOUCHE**: 美しく彫琢された繊細さのクリーミーな触感。**アーモンドペースト、折り込みブリオッシュ、白い果実、白胡椒。**力強く伸びやかで荘厳な典型性を持ち、**カルダモン、フレッシュマンゴー、フィンガーライム**へと信じがたい長さの芳香的持続を伸ばす。<br>🔴 **「純粋で強烈な偉大なブラン・ド・ブランの唯一無二の次元、その率直さは低いドザージュと完璧に結びついている。」**<br>**提供温度 12°**（⚠️ 製品ページは `10 / 12°` とも書く） |
| 🔴 **ÉLISABETH SALMON 2012**<br>「Profondeur et complexité」 | **「1988 年に、メゾンの共同創設者（`co-fondatrice`）Elisabeth Salmon への敬意として創られた。」**<br>**A L'ŒIL**: 支えられ揺らめくサーモンの柔らかな照りを持つ、非常に明るい視覚的存在。成し遂げられた成熟の探求を象徴する、煌めく輝きと優美な発泡。<br>**AU NEZ**: **赤と黒のベリー**の爽やかで官能的な感覚表現。**ミルティーユ、グーズベリー、シャクヤク**という豊かで複雑な芳香の広がり。**香り高いバラと結晶化したスミレ**の模倣しがたい香りを敬意をもって展開する、洗練され成熟した嗅覚の調子。<br>**EN BOUCHE**: 測られた力強さと魅惑を同時に持つ、すべてが繊細な触覚の衝撃。**パネットーネ、チェリーのクラフティ**という美味で菓子的な風味の調和した開花。**白亜的な先端**へ進む繊細な口中構造、**杉材と血まみれオレンジのゼリー**の持続する終盤へ。<br>**提供温度 11°–12°** |

### ✅ 公式が掲げる第三者評価（**公式サイト上に掲載されているもののみ**）

⚠️ 🔴 **これは「公式が自分のサイトに載せている」という事実の記録であって、
THÉSEUS が点数を評価として採用したという意味ではない。**

| キュヴェ | 公式サイト掲載の評点 |
|---|---|
| **Le Réserve** | **92/100 BETTANE & DESSEAUVE - 2025 ／ 90/100 La Revue du Vin de France - 2025** |
| **Le Rosé** | **94/100 BETTANE & DESSEAUVE - 2025 ／ 91/100 La Revue du Vin de France - 2025** |
| 🔴 **Louis Salmon 2012** | **98/100 TERRE DE VINS - 2024 ／ 96/100 BETTANE & DESSEAUVE - 2025 ／ 95/100 REVUE DU VIN DE FRANCE - 2025** |
| 🔴 **Élisabeth Salmon 2012** | **97/100 REVUE DU VIN DE FRANCE - 2025**（「**この成熟して充実したミレジムにおけるシャンパーニュの最も偉大なロゼの一つ。並外れた芳香の充溢。**」）**／ 96/100 BETTANE & DESSEAUVE - 2025** |

### ✅ 公式のマリアージュ（シェフとの協働。公式サイトが名指しする）

- **Le Réserve** — ✅ **Michel Rostang（Maison Rostang**、パリ）。「20 年以上 Billecart-Salmon と仕事をしている」**
- **Le Rosé / Élisabeth Salmon 2012** — ✅ **Pierre Hermé。2012 のためにデセール「Antigone」を制作**
- **Louis Salmon 2012** — ✅ **Sébastien Carmona-Porto（restaurant Helen*、パリ 8 区）**
- **Brut Nature** — ✅ **Jean-Georges Vongerichten（Jean-Georges**、ニューヨーク）**
- **Clos Saint-Hilaire** — ✅ **Nicolas Beaumann（Maison Rostang**、パリ）**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 4 本。alias 2 本 / unresolved 2 本**）

| # | OBP 印字 | VT | 価格 | セクション | intake | ✅ **公式での確認結果** |
|---|---|---|---|---|---|---|
| 1 | **`'Le Réserve,' Extra Brut`** | NV | $200 | `… \| BLENDS` | `alias` → `cuvee:billecart-salmon-le-reserve-extra-brut` | 🔴 ✅ **メニューは正しい。公式フィッシュ・テクニックの見出しは `LE RÉSERVE`、スペック欄は `Dosage Extra Brut`。ナビゲーションも `LE RÉSERVE`。** |
| 2 | **`'Louis Salmon,' Grand Cru Brut`** | **2012** | $640 | `… \| BLANC DE BLANCS` | `alias` → `cuvee:billecart-salmon-blanc-de-blancs-cuvee-louis-salmon-brut` | ✅ 🔴 **実在。公式フィッシュ `LOUIS SALMON 2012`、製品ページ見出し `BRUT BLANC DE BLANCS MILLÉSIME 2012`。**⚠️ **`Grand Cru` は名称の一部ではない。下記参照** |
| 3 | **`Brut`**（キュヴェ名の印字が無い） | NV | $280 | 🔴 `… \| **ROSÉ**` | 🔴 **`unresolved`** | ❓ 🔴 **公式で「1 本に絞れる」ところまでは確定したが、断定しない。下記参照** |
| 4 | **`'Elizabeth Salmon,' Brut`** | **2012** | $700 | 🔴 `… \| **ROSÉ**` | 🔴 **`unresolved`** | ✅ 🔴 **実在。公式フィッシュ `ÉLISABETH SALMON 2012`、製品ページ見出し `BRUT ROSÉ MILLÉSIME 2012`。**🔴 **綴りは公式 `Élisabeth` / メニュー `Elizabeth`。下記参照** |

---

### 🔴 1 行目 —— `Le Réserve` は誤植ではない。**タスク前提の反証**

🔴 ✅ **公式フィッシュ・テクニック（`/storage/products/fiches/le-reserve-17401484221030248614.pdf`）の見出しは
`LE RÉSERVE`。副題は `Harmonie et pureté`。スペック欄の最終行は `Dosage Extra Brut`。**
🔴 ✅ **製品ページの `<h1>` は `Champagne Le Réserve`。グローバルナビの表記は `LE RÉSERVE`。**

→ 🔴 **メニューの `'Le Réserve,' Extra Brut` は、名称もドザージュ区分も、造り手の現行表記と一致している。**
→ 🔴 **canonical の `Le Réserve Extra Brut` もまた正しい。「canonical が誤りを継承した」という想定は成立しない。**

⚠️ **ただし公式内部に、旧称の残滓が 3 か所ある。記録しておく。**

| 場所 | 表記 |
|---|---|
| **HTML の `<title>`** | ⚠️ **`Champagne Brut Réserve : Cuvée Collection`**（旧称のまま） |
| **URL スラッグ** | ⚠️ **`/fr/collection/brut-reserve`**（旧称のまま） |
| **製品ページ本文の書き出し** | ⚠️ **「`Le Réserve` est un vin de champagne `brut` sans année…」**（本文は `brut`、スペック欄は `Extra Brut`） |
| **公式が引用する RVF の評** | ⚠️ **「Dans son style, le `brut réserve` se montre sapide et énergique」**（第三者の文章） |
| **`/histoire` 1970 年の項** | ⚠️ **「le `Brut Rosé` est devenu la cuvée iconique de la Maison」**（ロゼ側の旧称。沿革の文脈） |
| 🏛 **TTB COLA** | 🏛 **2023-04-14 承認の米国向けラベルの fanciful name は `BRUT RESERVE`（brand `BILLECART SALMON`）** |

→ 🔴 **すなわち「`Brut Réserve` → `Le Réserve`」への改称は現在進行中であり、
公式サイト内にも米国流通ラベルにも旧称が併存している。**
→ 🔴 **これは「メニューの誤り」でも「canonical の誤り」でもなく、`改称の過渡期` である。**
→ ⚠️ **staff は「ブリュット・レゼルヴ」と「ル・レゼルヴ」が同じワインだと説明できる必要がある。** → §Staff Notes 追加の一手

🔴 **なお「Billecart は複数の NV を造っているか」という問いの答えは `Yes` である。**
**Collection レンジだけで NV が 6 本（`Le Réserve` / `Le Rosé` / `Le Blanc de Blancs` / `Brut Nature` / `Le Sous Bois` / `Demi-Sec`）、
さらに `Les Rendez-vous` シリーズが 8 本ある。**
🔴 **そして `Le Réserve` / `Le Rosé` / `Le Blanc de Blancs` / `Le Sous Bois` の 4 本はすべて `Dosage Extra Brut` である。**
→ 🔴 **したがって `Extra Brut` はこの生産者では識別語として機能しない。** → §Canonical Conflict `C-4` 族

---

### 🔴 2 行目 —— `Louis Salmon 2012`。**`Grand Cru` は「果実の話」であって「名前」ではない**

✅ **公式の説明**: 「**メゾンの創設時からワインの造りに深く関わった、œnologie に情熱を持つ
`Elisabeth Salmon` の兄弟 `Louis` への敬意。コート・デ・ブランの最良の区画に由来し、
純度とミネラリティを刻んだミレジメのブラン・ド・ブランが彼を完璧に表す。**」

| 項目 | ✅ 公式（フィッシュ・テクニック `cuvee-louis-salmon-2012-…pdf`） |
|---|---|
| **公式のキュヴェ名** | 🔴 **`LOUIS SALMON 2012`**（フィッシュ見出し）／**`Cuvée Louis Salmon 2012`**（購入導線の文）／**`BRUT BLANC DE BLANCS MILLÉSIME 2012`**（製品ページ見出し） |
| **セパージュ** | 🔴 **`100% Chardonnay Grands Crus de la Côte des Blancs : 60% Mesnil-sur-Oger, 23% Cramant, 11% Chouilly et 6% Oiry`** |
| **木樽** | 🔴 **`25% des vins sont vinifiés en fûts`** |
| **熟成** | 🔴 **`Maturation sur lies / en cave : 115 mois`**（＝9 年 7 か月） |
| **ドザージュ** | 🔴 **`3.9 g/l`** |
| **フォーマット / 保存** | **`Bouteille et magnum : plus de 10 ans`**（⚠️ 製品ページは「`plus de 20 ans`」とも書く） |

🔴 **`Grand Cru` について（タスクの問い）。**
✅ **公式が `Grands Crus`（複数形）を付けるのは、常に「果実の産地」に対してである** ——
`100% Chardonnay Grands Crus de la Côte des Blancs`。
🔴 **メゾンの所在地 `Mareuil-sur-Aÿ` に対して `Grand Cru` を主張する記述は、公式のどこにも無い。**
🔴 **むしろ Élisabeth Salmon 2012 のフィッシュは `100% grand cru et premier cru` と書き、
その内訳に `Mareuil-sur-Aÿ` を含めている。すなわち公式は Mareuil-sur-Aÿ を Grand Cru と呼んでいない。**

→ 🔴 **結論: メニューの `Grand Cru` は「コート・デ・ブランのグラン・クリュ産シャルドネ」という
果実の来歴を指す限りにおいて、造り手の記述と整合する。**
→ ⚠️ **ただし `Grand Cru` は公式のキュヴェ名の一部ではない。canonical の `classification: 'Grand Cru Brut'` も同様に、
公式の名称ではなくスタイル記述である。**
→ ⚠️ **`Mareuil-sur-Aÿ` の格付けそのものは本調査で一次資料に当たっていない。** → Open Questions 3

---

### 🔴 3 行目 —— キュヴェ名が印字されていない `Brut`（ROSÉ セクション・$280）

🔍 **intake の生データ**: `source_wine_raw = "Brut"` / `_parts.label = null` /
`evidence = "'Billecart-Salmon' の canonical キュヴェ 4 件に一致無し: 'Brut'"`。
🔴 **メニューはキュヴェを特定する語を 1 語も印字していない。区別しているのはセクション見出し `ROSÉ` だけである。**

#### ✅ 候補集合の境界（**ここまでが公式で言えること**）

✅ **公式の現行 Collection レンジ 7 本のうち、ロゼは 1 本だけである。残り 6 本の色を 1 本ずつ潰した:**

| キュヴェ | 色 | 根拠 |
|---|---|---|
| **Le Réserve** | 白 | フィッシュ「Reflet or pâle」 |
| 🔴 **Le Rosé** | 🔴 **ロゼ** | 🔴 **フィッシュ「jolie teinte rose pâle」／`SAVOIR-FAIRE ROSÉ`** |
| **Le Blanc de Blancs** | 白 | フィッシュ「teinte or lumineuse」 |
| **Brut Nature** | 白 | 製品ページ「Intensité visuelle or pâle」 |
| **Le Sous Bois** | 白 | 製品ページのセパージュ（赤ワインの添加記述なし） |
| **Vintage 2016** | 白 | 製品ページ「100% de Grands crus / PN 66・Ch 34」、ロゼ表記なし |
| **Demi-Sec** | 白 | 製品ページ、ロゼ表記なし。**ドザージュ 40 g/l で `Brut` ではない** |

✅ **`Les Rendez-vous` シリーズ 8 本（N°1〜N°8・Cinq）はいずれも単一品種の `Extra Brut` / 無印で、ロゼの表示は無い。**
✅ **ミレジメのロゼは `Élisabeth Salmon` のみ（2012 / 2013）で、これは NV ではない。**

→ 🔴 **したがって「現行の公式レンジにおける NV のロゼ」は `Le Rosé` ただ 1 本に絞られる。**
→ 🔍 **canonical 側にも `billecart-brut-rose`（`name='Brut Rosé'` / `vintage='NV'` / `color='Rosé'`）が 1 件だけ存在する。**

#### 🔴 ⚠️ **それでも本ドシエは 3 行目に名前を書かない。**

**理由 ——**
1. ⚠️ 🔴 **ドザージュが合わない。** **メニューは `Brut` と印字しているが、公式の現行 `Le Rosé` は `Dosage Extra Brut` である。**
   **旧称 `Brut Rosé` 時代のボトルであれば `Brut` と印字されるのが自然だが、それは推論であって出典ではない。**
2. ⚠️ **`Le Rosé` / `Brut Rosé` の改称過渡期にあるため、卓上のボトルがどちらの表記かは分からない。**
3. ⚠️ **メゾンは限定シリーズ（`SÉRIES LIMITÉES & COFFRETS`）を持ち、本調査はその全数を確認していない。**
4. 🔴 **Batch 9 の Bergström 5 行目と同一の形である。** **4 本の収束する証拠は、依然として出典ではない。**

→ 🔴 **`## Open Questions 1` に「実ラベル確認タスク」として送る。**

---

### 🔴 4 行目 —— `Elizabeth Salmon 2012`。**綴りの二層構造**

| 項目 | ✅ 公式（フィッシュ `cuvee-elisabeth-salmon-2012-…pdf`） |
|---|---|
| **公式のキュヴェ名** | 🔴 **`ÉLISABETH SALMON 2012`**（フィッシュ見出し）／**`Cuvée Elisabeth Salmon 2012`**（購入導線）／**`BRUT ROSÉ MILLÉSIME 2012`**（製品ページ見出し） |
| **創出年** | 🔴 **`Créée en 1988 en hommage à Elisabeth Salmon, co-fondatrice de la Maison`** |
| **格付** | 🔴 **`100% grand cru et premier cru`** |
| **セパージュ** | 🔴 **`55% Chardonnay de Chouilly, Avize, et Mesnil-sur-Oger` / `45% Pinot Noir de Mareuil-sur-Aÿ et Verzenay`**<br>→ 🔴 **シャルドネ主体である。** |
| **赤ワイン** | 🔴 **`Moins de 10% du Pinot Noir est vinifié en rouge à partir de raisins de vieilles vignes de Mareuil-sur-Aÿ, exposées plein sud`**<br>⚠️ **製品ページは同じ箇所を「`8%`」と数値で書く。フィッシュは「`Moins de 10%`」。** |
| **木樽** | 🔴 **`2,90% des vins sont vinifiés en fûts`** |
| **熟成** | 🔴 **`Maturation sur lies / en cave : 115 mois`**（Louis Salmon 2012 と同一） |
| **ドザージュ** | 🔴 **`3,8 g/l`** |

#### 🔴 綴りについて（タスクの問い (d)）

| 層 | 綴り | 出典 |
|---|---|---|
| ✅ **フランス公式・世代表** | **`ÉLISABETH SALMON`**（アクセントあり） | `/histoire` の「Portrait de famille」 |
| ✅ **フランス公式・商品見出し** | **`ÉLISABETH SALMON 2012`** | ナビゲーション／フィッシュ見出し |
| ✅ **フランス公式・本文** | ⚠️ **`Elisabeth Salmon`**（アクセントなし） | 製品ページ本文／フィッシュ本文 |
| 🔍 **canonical** | **`Cuvée Elisabeth Salmon Brut Rosé`**（`s`・アクセントなし） | `billecart-elizabeth-salmon-2012`<br>⚠️ **ただしレコードの `id` は `billecart-`**`elizabeth`**`-salmon-2012` で `z`。名前と id で綴りが割れている** |
| 🔍 **OBP メニュー** | 🔴 **`Elizabeth Salmon`**（`z`） | `source_wine_raw` |
| 🏛 **TTB COLA（米国承認ラベル）** | 🔴 **両方が実在する** | 下記 |

🏛 🔴 **TTB COLA の実測（`productNameSearchType=F`、fanciful name 検索）:**

| 承認日 | fanciful name | brand |
|---|---|---|
| **2013-11-29** | **`CUVÉE ELISABETH SALMON BRUT ROSÉ`** | BILLECART-SALMON |
| **2014-03-10** | **`ELISABETH SALMON`** | BILLECART-SALMON |
| 🔴 **2015-03-16** | 🔴 **`CUVEE ELIZABETH SALMON`** | **BILLECART SALMON** |
| 🔴 **2015-12-22** | 🔴 **`CUVEE ELIZABETH SALMON BRUT ROSE`** | **CHAMPAGNE BILLECART-SALMON** |
| 🔴 **2016-01-05** | 🔴 **`ELIZABETH SALMON`** | **BILLECART-SALMON** |
| **2019-06-03** | **`CUVEE ELISABETH SALMON BRUT ROSE`** | BILLECART-SALMON |
| **2020-12-23 / 2021-01-06** | **`CUVEE ELISABETH SALMON`** | BILLECART-SALMON |

→ 🔴 **`z` 綴りは 2015〜2016 年の米国向けラベルに集中して実在し、2019 年以降は `s` 綴りに戻っている。**
→ 🔴 **したがってメニューの `Elizabeth` は「レストランの誤記」と断定できない。
米国流通で実際に承認されたラベル表記に一致しうる。**
→ 🔴 **これは「メニュー側の欠陥」ではなく、`producer-official 表記` と `US import ラベル表記` の
2 層が存在するという構造である。** → §Canonical Conflict `C-1` 族

⚠️ **`Élisabeth Salmon` が「妻」か「共同創設者」か。**
**公式は 1818 年の項で「Nicolas François Billecart が Elisabeth Salmon と結婚し、二人はメゾンを創設することを決めた」と書き、
フィッシュでは `co-fondatrice de la Maison`（女性形の共同創設者）と書く。**
🔴 **すなわち公式の枠組みは「創設者の妻」ではなく「共同創設者」である。** → §Canonical Conflict

---

### ✅ 公式の全キュヴェ一覧（**ナビゲーション「LES CHAMPAGNES」の実測**）

| レンジ | キュヴェ |
|---|---|
| 🔴 **Collection（NV 6 ＋ Vintage 1）** | **LE ROSÉ ⭐／LE RÉSERVE ⭐／LE BLANC DE BLANCS／BRUT NATURE／LE SOUS BOIS／VINTAGE（現行 2016）／DEMI-SEC** |
| **Les Rendez-vous（8）** | **N°1 MEUNIER EXTRA BRUT／N°2 PINOT NOIR EXTRA BRUT／N°3 MEUNIER EXTRA BRUT／N°4 CHARDONNAY EXTRA BRUT／CINQ PINOT NOIR EXTRA BRUT／N°6 CHARDONNAY／N°7 MEUNIER／N°8 MEUNIER** |
| 🔴 **Millésime（6）** | **CUVÉE NICOLAS FRANÇOIS 2008／CUVÉE NICOLAS FRANÇOIS 2012／ÉLISABETH SALMON 2012 ⭐／ÉLISABETH SALMON 2013／LOUIS SALMON 2012 ⭐／LOUIS SALMON 2013** |
| 🔴 **Clos**（1） | **CLOS SAINT-HILAIRE（現行 2009。ストア掲載は 2005 も）** |

🔴 **OBP の 2012 年 2 本は、いずれも「現行 2 ミレジムのうちの古い方」である。**
**公式は `Élisabeth Salmon` と `Louis Salmon` の双方について 2012 と 2013 を並行して掲げている。**
→ ⚠️ **したがって「2012 が最新」とは言えない。**

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① 1818 年創業、7 代続く家族経営。マルイユ＝シュル＝アイ。自社畑 100 ha ＋ 調達を含め 300 ha・40 クリュ。**
「**1818 年、ニコラ・フランソワ・ビルカールとエリザベット・サルモンの結婚から生まれたメゾンです。
以来一度も家族の手を離れず、いまは 7 代目のマチュー・ローラン＝ビルカールが率いています。
本拠はマルイユ＝シュル＝アイ**（**現在の行政区分ではアイ＝シャンパーニュ**）**。
**自社畑は 100 ヘクタール**で、それに加えて**シャンパーニュの 40 クリュ、総計 300 ヘクタール**から
ブドウを調達しています。**大部分はエペルネから半径 20 キロの範囲**です。
蔵は**17 世紀と 19 世紀の白亜のカーヴ、通路は 2 キロ**あります。」

**② 造り手の署名は「低温での長い発酵」と「冷やして澱を落とす（デブルバージュ・ア・フロワ）」。1958 年、ビール醸造家に学んだ。**
「🔴 **ビルカールのスタイルを決めているのは、低温での長い発酵です。**
**1958 年に 5 代目のジャン・ローラン＝ビルカールが導入しました。**
造り手自身が『**伝統的なビール醸造家（ブラッスール）の方法に着想を得た**』と書いています。
**2000 年に新しいキュヴリーを造り、47 ヘクトリットルの小さな温度管理タンク**で
**クリュごと・品種ごとに**仕込んでいます。
造り手の言葉では『**低温で醸造すると発酵が遅くなり、軽やかで繊細な香りを促し、果実の純粋さを表現させる。
これが真の署名だ**』。」

**③ NV は 3〜4 年、ミレジメは 10 年。しかも Collection レンジは全部エクストラ・ブリュットになっている。**
「**ノン・ヴィンテージは 3〜4 年寝かせます。造り手いわく『アペラシオンが定める規則の 2 倍』。
ミレジメは 10 年。**実際、**ルイ・サルモン 2012 もエリザベット・サルモン 2012 も、
公式のスペックは澱の上で 115 か月**です。
🔴 **そして重要なのは、ル・レゼルヴもル・ロゼもル・ブラン・ド・ブランもル・スー・ボワも、
公式のドザージュ表記が『エクストラ・ブリュット』だということ。**
**ミレジメは数値が出ていて、ルイ・サルモン 2012 が 3.9 g/L、エリザベット・サルモン 2012 が 3.8 g/L です。**」

### 追加で使える一手

- 🔴 **「ブリュット・レゼルヴ」と言われたら**: 「**同じワインです。**
  造り手が **`Brut Réserve` から `Le Réserve` へ名前を変えている途中**で、
  **公式サイトの中でも URL やページタイトルには旧称が残っています。**
  **メニューの『ル・レゼルヴ、エクストラ・ブリュット』は造り手の現行表記そのものです。**」
- 🔴 **ルイとエリザベットの関係**: 「**エリザベット・サルモンは共同創設者で、
  ルイ・サルモンはその兄弟**です。**夫婦ではありません。**
  ニコラ・フランソワ・ビルカールが商売を、義兄のルイがワイン造りを担当しました。
  **だから白のプレスティージュがルイ、ロゼのプレスティージュがエリザベットなのです。**」
- 🔴 **ルイ・サルモン 2012（$640）**: 「**コート・デ・ブランのグラン・クリュのシャルドネ 100%。
  ル・メニル＝シュル＝オジェ 60%、クラマン 23%、シュイイ 11%、オワリー 6%。**
  造り手は『**クラマンがミネラリティ、シュイイとオワリーが繊細さ、ル・メニルが構造と長命さ**』と書き分けています。
  **25% を樽で仕込み、澱の上で 115 か月、ドザージュ 3.9 g/L。提供温度は 12 度**が公式指定です。」
- 🔴 **エリザベット・サルモン 2012（$700）**: 「**1988 年創出のプレスティージュ・ロゼ。
  グラン・クリュとプルミエ・クリュ 100%。シャルドネ 55%、ピノ・ノワール 45%**——
  🔴 **ロゼですがシャルドネの方が多いのが特徴です。**
  **ピノ・ノワールの 10% 未満を、マルイユ＝シュル＝アイの真南向きの古樹から赤に仕込んで加えます。
  澱の上で 115 か月、ドザージュ 3.8 g/L。**
  **ピエール・エルメがこの 2012 のためにデセール『Antigone』を作っています。**」
- **クロ・サン＝ティレール**: 「**マルイユ＝シュル＝アイの教会の守護聖人の名を冠した 1 ヘクタールの囲い畑**です。
  **1964 年にピノ・ノワールを植え、1995 年が第 1 ミレジム。ブラン・ド・ノワールで、樽で仕込み、ボトルは番号入り。
  各ミレジムで 3,500〜7,500 本を超えません。**
  **数年前から挽き馬で耕しています。**」
- **千年紀のシャンパーニュ**: 「**1999 年、ストックホルムでリシャール・ジュランが催した
  150 ミレジムのブラインド試飲で、ビルカールの 1959 年が『千年紀のシャンパーニュ』に選ばれました。
  1961 年が 2 位**でした。」
- **環境**: 「**2017 年に HVE と VDC、2023 年に ISO 50001 を取得。
  2020 年から除草剤 100% 不使用**です。
  **クロ・サン＝ティレールには養蜂箱が 3 基**あって、うち 1 基は**メゾンのワインが入っていた樽で造られています。**」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／出典が矛盾している**）

1. 🔴 ⚠️ **メニューの `Le Réserve` を「誤植です」と説明しない。**
   **公式フィッシュ・テクニックの見出しが `LE RÉSERVE`、スペックが `Dosage Extra Brut` であり、
   メニューは名称もドザージュも造り手の現行表記に一致している。**
   **旧称 `Brut Réserve` が公式サイト内と米国ラベルに残っているだけである。**
2. 🔴 ⚠️ **「全部自社畑」と言わない。**
   **公式は「自社ドメーヌ 100 ヘクタール」と「40 クリュ・総計 300 ヘクタールからの調達」を明確に区別している。**
3. 🔴 ⚠️ **「オーガニックのメゾンです」と言わない。同時に「有機認証はありません」とも言わない。**
   **公的登録（Agence Bio `numeroBio 1813` / Ecocert `FR-BIO-01`）には有効な登録があるが、
   活動区分は `Préparation`（醸造・加工）のみで、`mixite: "Oui"`（有機・非有機の併営）である。**
   **公式サイト自身が「2021 年に 10 ヘクタールが有機転換中」と書いており、全畑ではない。**
   **公式サイトは `bio` の語を 3 か所（試み／土壌改良材／転換）でしか使わず、`Ecocert` も `AB` も一度も書いていない。**
   🔴 **言えるのは「HVE と VDC を 2017 年に取得、ISO 50001 を 2023 年に取得、2020 年から除草剤不使用」まで。**
   🔴 **公式の「2025 年 100% du vignoble certifié」は、何の認証かを公式が書いていないので引用しない。**
4. 🔴 ⚠️ **「エリザベット・サルモンは創業者の妻」で止めない。「ルイ・サルモンは夫」でもない。**
   **公式はエリザベットを `co-fondatrice de la Maison`（共同創設者）とし、
   ルイを `le frère de son épouse`（妻の兄弟）としている。**
5. 🔴 ⚠️ **低温発酵と `débourbage à froid` の「どちらが先か」を断定しない。**
   **`/histoire` は「低温発酵 → 次いで débourbage à froid」、`/la-cuverie` は「débourbage à froid → 次いで低温発酵」と、
   公式の 2 ページが逆に書いている。**
   **言うなら「1958 年に、ビール醸造家に着想を得て、この 2 つを導入した」まで。**
   🔴 ⚠️ **摂氏の数値を言わない。公式は「低温」としか書いておらず、温度も時間も一切数値が無い。**
6. ⚠️ **世代数を断定しない。** **公式は同じ沿革ページの中で「7 générations」と「6 générations」を併記している。**
   **`/les-hommes` と 2018 年の項は 7、見出しは 6。言うなら「7 代目のマチューが当主」という個別事実まで。**
7. 🔴 ⚠️ **OBP の 4 本についてマロラクティック発酵の有無を語らない。**
   **公式が MLF に触れるのは `Brut Nature`（実施）と `Demi-Sec`（部分実施）の 2 本だけで、
   `Le Réserve` / `Le Rosé` / `Le Blanc de Blancs` / `Louis Salmon 2012` / `Élisabeth Salmon 2012` の
   フィッシュ・テクニックには一切記述が無い。**
8. 🔴 ⚠️ **エリザベット・サルモンを「ピノ・ノワール主体」と説明しない。**
   **公式は `55% Chardonnay / 45% Pinot Noir` と書いており、シャルドネの方が多い。**
   **canonical は逆（PN 60 / Ch 40）を持っているが、公式と食い違う。**
9. 🔴 ⚠️ **ルイ・サルモンを「ル・メニル単一」と説明しない。「モン・ブランシュ区画」と言わない。**
   **公式は 4 つのクリュ（Mesnil 60 / Cramant 23 / Chouilly 11 / Oiry 6）を明示している。**
   **`Mont Blanche` という区画名は公式のどこにも現れない。**
10. 🔴 ⚠️ **ドザージュの数値を canonical から言わない。**
    **canonical は Louis Salmon を 5 g/L、Élisabeth Salmon を 6 g/L、Le Rosé を 7 g/L としているが、
    公式はそれぞれ 3.9 g/L、3.8 g/L、`Extra Brut`（数値なし）である。**
11. 🔴 ⚠️ **ロゼの伝統を「1830 年代から」と言わない。**
    **公式が書くのは「1970 年代にジャン・ローラン＝ビルカールがロゼに再び取り組んだ」である。**
    **1830 年代という記述は公式のどこにも無い。**
12. ⚠️ **創業年を 1816 年と言わない。公式・サイトタイトル・沿革のすべてが 1818 年である。**
13. ⚠️ **`Mareuil-sur-Aÿ` を「グラン・クリュ」と言わない。**
    **公式は Grand Cru を常に果実の産地（コート・デ・ブラン等）に対して使い、自らの村には使っていない。**
    **`Élisabeth Salmon` のフィッシュは Mareuil-sur-Aÿ を含めて `grand cru et premier cru` と書く。**
14. ⚠️ **アルコール度数・デゴルジュマン日・生産本数（Clos Saint-Hilaire を除く）・
    「手作業デゴルジュマン」を言わない。** **公式に一切根拠が無い。**
15. ⚠️ **3 行目（ROSÉ セクション・$280・キュヴェ名の印字なし）に名前を付けて説明しない。**
    **候補は公式レンジ上 `Le Rosé` 1 本に絞れるが、メニューの `Brut` と公式の `Extra Brut` が食い違っており、
    実ラベルの確認が済んでいない。** → Open Questions 1
16. ⚠️ **公式サイト掲載の点数を「評価です」と断定的に使わない。**
    **公式が自サイトに載せているという事実の記録にとどめる。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **本書では canonical も `research/canonical_conflicts/REGISTER.md` も一切編集していない。**
🔴 **既存の族に該当するものは既存 ID を引用し、新しい番号を開かない。**
🔴 **既存のどの族にも当たらないものは「未採番」とし、採番は CTO の判断に委ねる。**

---

### 🔴 前提の訂正 —— **`C-6` はこの生産者には当てはまらない**

🔴 **タスク前提は「canonical が Élisabeth Salmon を持たない可能性（gap）」および
「1 レコードが 2 色を兼ねる形（Taittinger `C-6`）」を想定していた。実測はどちらでもない。**

🔍 **canonical は Billecart-Salmon について 4 レコードを持ち、色の軸は既に分かれている:**

| canonical id | name | vintage | color | classification |
|---|---|---|---|---|
| `billecart-le-reserve` | `Le Réserve Extra Brut` | NV | Blanc | Extra Brut |
| `billecart-louis-salmon-2012` | `Blanc de Blancs Cuvée Louis Salmon Brut` | 2012 | **Blanc de Blancs** | Grand Cru Brut |
| `billecart-brut-rose` | `Brut Rosé` | NV | **Rosé** | Brut |
| `billecart-elizabeth-salmon-2012` | `Cuvée Elisabeth Salmon Brut Rosé` | 2012 | **Rosé** | Brut |

🔴 **プレスティージュは「白（Louis Salmon）」と「ロゼ（Élisabeth Salmon）」で別レコードとして既に存在する。**
→ 🔴 **したがって `C-6` に追加すべき証拠は無い。むしろ本件は `C-6` の反例として有用である ——
「同一メゾンの 2 色プレスティージュを別レコードで持つ」形が canonical 内に既に実在することを示す。**
🔴 **そして 2 本が `unresolved` である原因は、色の軸ではなく `名前の綴り` と `名前の不在` である。**

---

### 🔴 `C-1` 族に該当 —— **`Elizabeth` / `Élisabeth` の綴り分岐（4 行目）**

**`C-1`（Egly-Ouriet — 語順・アクセント揺れによる同一キュヴェの多重化）と同型。新しい番号は開かない。**

**1. 対象**
- **canonical**: `billecart-elizabeth-salmon-2012` / `name = 'Cuvée Elisabeth Salmon Brut Rosé'`
- **OBP 行**: `obp-beverage-2026-08:7ee23c2c81` / `source_wine_raw = "'Elizabeth Salmon,' Brut"` / 2012 / $700 /
  セクション `FRANCE | SPARKLING > CHAMPAGNE | ROSÉ`
- 🔍 **intake の判定**: `match_state = unresolved` / `confidence = 0.0` /
  `evidence = "'Billecart-Salmon' の canonical キュヴェ 4 件に一致無し: 'Elizabeth Salmon'"`

**2. なぜ当たらないのか**
🔴 **canonical 側は `Elisabeth`（`s`）、メニュー側は `Elizabeth`（`z`）。**
**`s` / `z` は正規化でも折りたたまれず、トークン一致が成立しない。**
🔴 **`C-1` が扱う「アクセント揺れ」と同じ層の問題だが、こちらは `子音の綴り` である点だけが違う。**

🔴 **さらに canonical レコード自身の内部で綴りが割れている:**
- **`id` = `billecart-`**`elizabeth`**`-salmon-2012`（`z`）**
- **`name` = `Cuvée `**`Elisabeth`**` Salmon Brut Rosé`（`s`）**
→ 🔴 **`id` の方はメニューと一致するのに、matcher が見ているのは `name` である。**

**3. 追加証拠（本ドシエの寄与）**
- ✅ **フランス公式は一貫して `Elisabeth` / `ÉLISABETH`。`z` は公式に一度も現れない。**
- 🏛 🔴 **しかし TTB COLA には `z` 綴りの米国承認ラベルが 3 件実在する**
  （2015-03-16 `CUVEE ELIZABETH SALMON` / 2015-12-22 `CUVEE ELIZABETH SALMON BRUT ROSE` /
  2016-01-05 `ELIZABETH SALMON`、brand は `BILLECART SALMON` / `CHAMPAGNE BILLECART-SALMON`）。
- 🏛 **2019 年以降の COLA は `ELISABETH` に戻っている。**
→ 🔴 **すなわちこれは単なる誤記ではなく、`producer-official 表記` と `US import ラベル表記` が
時期によって分岐した痕跡である。**
🔴 **`C-1` の記述は「語順・アクセント」に限定されているため、この事例は
`C-1` の適用範囲を「US 流通ラベルに由来する綴り分岐」へ拡張する証拠として使える。**

**4. OBP への影響**
🔴 **1 本（$700）が `unresolved`。canonical に正しい行き先が存在するのに到達できていない。**

**5. Confidence**
🔴 **High。** **公式・canonical・TTB の 3 者すべてを実測した。**

---

### 🔴 `C-4` 族に該当 —— **識別語を持たない印字 `Brut`（3 行目）**

**`C-4`（識別語を持たないキュヴェ名 — 最大の実害源）と同型。新しい番号は開かない。**
🔴 **`C-4` の Evidence 欄は、既に `Billecart-Salmon 'Brut Rosé'` を該当 38 レコードの一つとして名指ししている。
本件はその同じレコードが、メニュー側からも解決できないことを示す実例である。**

**1. 対象**
- **canonical**: `billecart-brut-rose` / `name = 'Brut Rosé'`（**スタイル語のみで構成された名前**）
- **OBP 行**: `obp-beverage-2026-08:063e4add79` / `source_wine_raw = "Brut"` / NV / $280 /
  セクション `FRANCE | SPARKLING > CHAMPAGNE | ROSÉ`
- 🔍 **intake**: `_parts.label = null`（**ラベル語が 1 つも抽出できていない**）/ `confidence = 0.0`

**2. 構造**
🔴 **canonical 側の名前 `Brut Rosé` はスタイル語 2 語のみ。
メニュー側の印字 `Brut` はスタイル語 1 語のみ。
両者を結ぶ「生産者を特定する語」がどちらにも無い。**
🔴 **区別に必要な情報（色）は、メニューではセクション見出し `ROSÉ` にしか存在せず、
matcher の入力になっていない。**
→ 🔴 **`C-4` が指摘する「名前が識別子として機能していない」の典型であり、
かつ Taittinger `C-6` が提案した「セクション見出しを matcher の入力信号にする」という
設計提案がそのまま効く事例でもある。**

**3. 本生産者に固有の悪化要因（追加証拠）**
🔴 ✅ **公式の現行 Collection レンジのうち 4 本（`Le Réserve` / `Le Rosé` / `Le Blanc de Blancs` / `Le Sous Bois`）が
すべて `Dosage Extra Brut` である。**
→ 🔴 **したがって `Brut` も `Extra Brut` も、この生産者では識別語として機能しない。**
🔴 **加えて `Les Rendez-vous` シリーズ 8 本のうち 5 本が名前に `Extra Brut` を含む。**

**4. OBP への影響**
🔴 **1 本（$280）が `unresolved`。**
⚠️ **canonical に `billecart-brut-rose` という「ほぼ確実に正しい行き先」が存在するが、
本ドシエはこれを確定と書かない。メニューの `Brut` と公式の `Extra Brut` が食い違っているためである。**

**5. Confidence**
**Medium-High。** **`C-4` 該当であることは High。行き先の同定は実ラベル待ち。**

---

### 🔴 既存の族に該当しない —— **未採番（採番は CTO の判断）**

#### 🔴 shape A: **canonical のフィールド値そのものが producer-official と矛盾する（4 レコード全件）**

🔴 **既存の登録票 20 件は「どのレコードとどのレコードが衝突するか」「名前が識別子として機能するか」を扱っており、
`レコードの属性値が造り手の公式スペックと違う` という形を扱う分類が無い。**
🔴 **`S-2`（裁定スキーマ）にも `C-*`（命名）にも `V-*`（層のずれ）にも入らない。**
🔴 **したがって新しい shape として記述のみ行い、番号は開かない。**

| canonical id | フィールド | canonical の値 | ✅ **公式の値** |
|---|---|---|---|
| `billecart-le-reserve` | `grapes` | **PN 40% / Ch 40% / Meunier 20%** | 🔴 **PN 28% / Ch 29% / Meunier 43%**（2020 年基準）。**ムニエが最多である** |
| 〃 | `aging` | `36+ months sur lie` | 🔴 **`en moyenne : 50 mois`** |
| 〃 | `dosage` | `Extra Brut — 3–4 g/L` | ⚠️ **`Dosage Extra Brut`。数値は公式に無い** |
| 〃 | `winemaking` | 「リザーヴワインを 30% 以上」 | 🔴 **`Plus de 50% de vins de réserve`** |
| 〃 | `winemaking` | 「マロラクティック発酵あり」 | ⚠️ **フィッシュに記述なし（出典が沈黙）** |
| `billecart-louis-salmon-2012` | `subregion` / `terroir` | `Le Mesnil-sur-Oger` / **「モン・ブランシュ区画」** | 🔴 **4 クリュ: Mesnil 60% / Cramant 23% / Chouilly 11% / Oiry 6%。**🔴 **`Mont Blanche` は公式に一度も現れない** |
| 〃 | `dosage` | `Brut — 5 g/L` | 🔴 **`3.9 g/l`** |
| 〃 | `aging` | `8+ years sur lie` | 🔴 **`115 mois`** |
| 〃 | `winemaking` | 「MLF あり／手作業デゴルジュマン」 | ⚠️ **どちらも公式に記述なし。**⚠️ **公式にある `25% des vins vinifiés en fûts` が canonical に無い** |
| `billecart-brut-rose` | `name` | `Brut Rosé` | ⚠️ **公式の現行名は `Le Rosé`（旧称 `Brut Rosé` は沿革と米国ラベルに残存）** |
| 〃 | `grapes` | **PN 30% / Ch 40% / Meunier 30%** | 🔴 **Ch 45% / PN 35% / Meunier 20%** |
| 〃 | `dosage` | `Brut — 7 g/L` | 🔴 **`Dosage Extra Brut`** |
| 〃 | `description` | 🔴 **「1830 年代から続くロゼ製造の伝統」** | 🔴 **公式は「1970 年代に Jean Roland-Billecart がロゼに再び取り組んだ」。1830 年代の記述は公式に無い** |
| `billecart-elizabeth-salmon-2012` | `grapes` | 🔴 **PN 60% / Ch 40%** | 🔴 **Ch 55% / PN 45%。比率が逆である** |
| 〃 | `dosage` | `Brut — 6 g/L` | 🔴 **`3,8 g/l`** |
| 〃 | `aging` | `8+ years sur lie` | 🔴 **`115 mois`** |
| 〃 | `description` | 🔴 **「1816 年にメゾンを設立した」** | 🔴 **公式は一貫して `1818`** |
| 〃 | `description` | 「創設者ニコラ・フランソワの妻」 | ⚠️ **公式は `co-fondatrice de la Maison`（共同創設者）** |
| 〃 | `terroir` | 「マルイユ＝シュル＝アイのグラン・クリュ区画」 | 🔴 **公式は `100% grand cru et premier cru`。Mareuil-sur-Aÿ を Grand Cru と呼んでいない** |
| 〃 | `winemaking` | 「MLF あり／手作業デゴルジュマン」 | ⚠️ **公式に記述なし。**⚠️ **公式にある `2,90% des vins vinifiés en fûts` が canonical に無い** |

🔴 **OBP への影響: 照合には影響しない（これらのフィールドは matcher の入力ではない）。**
🔴 **だが `obp_note` / `description` / `tasting` は staff 向け表示に使われる想定であり、
そのまま読み上げると、卓上で少なくとも次の 6 点の誤りが出る ——**
**① レゼルヴのセパージュ、② ロゼのセパージュ、③ エリザベットのセパージュの主従、
④ ドザージュの数値 3 件、⑤ 創業年 1816、⑥ 「1830 年代からのロゼ」。**
→ **§Staff Notes ⚠️ ③ ⑧ ⑨ ⑩ ⑪ ⑫ ですべて塞いだ。**

⚠️ **これは Batch 5–9 で 4 生産者について確認された「canonical の `obp_note` / `description` は信頼できない」
という所見の 5 例目であり、本件では 4 レコード全件に及んでいる。**

#### ⚠️ shape B: **改称の過渡期を canonical が表現できない**

⚠️ 🔴 **`Brut Réserve → Le Réserve`、`Brut Rosé → Le Rosé` という改称が進行中で、
公式サイト内（URL・`<title>`・沿革本文）と米国流通ラベルに旧称が残存している。**
🔴 **canonical は `Le Réserve Extra Brut`（新称）と `Brut Rosé`（旧称）を、
どちらが旧でどちらが新かを表現しないまま並存させている。**
⚠️ **`V-1`（Krug の `édition`）が扱うのは「NV の中の版」であって「名前の世代」ではない。**
→ ⚠️ **`cuvée` 層に `superseded_name` / `former_name` にあたる表現が無い、という設計上の欠落。**
🔒 **新しい番号は開かない。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY / 標準規則 `D-2026-08-05-09`**）

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の会社名** | ✅ 🔴 **合格。** `https://www.champagne-billecart.fr/fr/pages/mentions-legales` に **`Éditeur du Site : Champagne Billecart-Salmon`（Société anonyme）**、**資本金 `7.104.000 euros`**、**`RCS de Reims / Siret : 335 480 075`**、**TVA `FR53335480075`**、**`Directeur de Publication : Maxime Renault`** を明記 |
| **(b) 非提携を否認する免責表示** | ✅ **合格（存在しない）。** 「ファンサイト」「非公式」等の否認表示は無い。**トップページのタイトルが `Champagne Billecart-Salmon- Maison Familiale fondée en 1818 \| Site Officiel`** |
| **(c) 公的登録と一致する住所** | ✅ 🔴 **合格。** **公式 `40 rue Carnot – BP8 – 51160 AY-CHAMPAGNE` に対し、🏛 企業登録 `40 RUE CARNOT 51150 AY-CHAMPAGNE`（SIREN `335480075`）。番地・通り名・コミューン名が一致。**⚠️ **郵便番号のみ `51160` / `51150` で揺れる（記録済み）** |
| 🔴 **(c') 登録者の一致（AFNIC WHOIS）** | 🏛 🔴 **合格。`champagne-billecart.fr` の `holder-c: CTC5156963-FRNIC` は `type: ORGANIZATION` / `contact: Champagne Billecart Salmon` / `country: FR`。`created: 1998-02-25`。registrar は Orange Business Services（EOLAS）** |
| **(d) 整合した商業・法務フッター** | ✅ **合格。** 年齢確認ゲート（`/fr/verification-age-legal`）、法定表示 `L'ABUS D'ALCOOL EST DANGEREUX POUR LA SANTÉ, À CONSOMMER AVEC MODÉRATION.`、CGV（PDF 実体あり）、個人情報方針、ホスティング事業者（OVH / RCS Roubaix 424 761 419）まで完備 |

🔴 **もう一方の候補ドメイン `billecart-salmon.com` の判定 —— 情報源として使用していない。**

| 検証 | 結果 |
|---|---|
| **DNS** | 🔴 **`curl: (6) Could not resolve host: billecart-salmon.com`。名前解決しない（NXDOMAIN 相当）。HTTP 応答なし** |
| 🏛 **WHOIS** | 🏛 **`Creation Date: 2017-06-16` / `Registrar: IP Twins SAS` / NS は `ns1–ns4.iptwins.net/.com` / `Registrant Organization: REDACTED FOR PRIVACY`** |
| **判定** | 🔴 **`IP Twins` はブランド保護専業のレジストラであり、NS だけが設定され A レコードが無い。すなわち防衛的登録（defensive registration）と読めるが、登録者が秘匿されているため所有者は確定できない。**<br>🔴 **いずれにせよ「稼働していないドメイン」であり、真正性の判定以前に情報源になりえない。** |

🔴 **したがって公式ドメインは `champagne-billecart.fr` である。**
🔴 **本調査で `NOT_THE_PRODUCER_*` / `FANPAGE_*` として退けたサイトは無い。
偽サイト・そっくりサイトには遭遇していない。**
🔴 **公式ドメイン以外で事実の根拠に用いたのは、公的登録 4 種（recherche-entreprises / Agence Bio / Ecocert / TTB COLA）と
AFNIC WHOIS のみである。**
（**WebSearch は一切使用していない。全 URL は `robots.txt` → `sitemap.xml` → ページ内 `href` の連鎖から機械的に導出した。**）

**付随ドメインの真正性**
- ✅ **`myorigin.billecart.fr`** — **全 5 点の公式フィッシュ・テクニックが末尾で `Les secrets de votre cuvée sur myorigin.billecart.fr` と参照する、セパージュ開示サイト。HTTP 200、`<title>My Origin - Champagne Billecart-Salmon`。**
  🏛 **登録可能ドメイン `billecart.fr` の AFNIC holder は `CBS234-FRNIC`（registrar GANDI、`created: 2013-01-16`）。**
  ⚠️ **`champagne-billecart.fr` とは別の登録可能ドメインであるため、holder の同一性は本調査では確定していない。**
  🔴 **公式フィッシュが自ら参照している事実をもって真正と判断したが、内容は未取得。** → Open Questions 6

### 一次資料（✅ 公式ドメイン）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt`** | **`Sitemap: https://www.champagne-billecart.fr/sitemap.xml` を明示。`User-agent: * / Allow: /`。冒頭コメントは `# au revoir et merci`**（`sitemap_index.xml` / `sitemap.xml.gz` は 404） |
| **`/sitemap.xml`** | **79 URL。**Collection 7 / Millésime 5 / la-maison 10 / store 16 / **フィッシュ PDF 14 / cartographie PDF 4**。⚠️ **sitemap 収載の PDF は旧ヴィンテージ（2002 / 2003 / 2007 / 2008）で、現行の 2012 系は含まれない。現行 PDF は各ページの `href` から取得した** |
| 🔴 **`/fr/collection/brut-reserve`** | 🔴 **`<h1> Champagne Le Réserve`。ナビ `LE RÉSERVE`。スペック（28/29/43・`basse température`・`Plus de 50%` リザーヴ・`50 mois`・`Dosage Extra Brut`）。**⚠️ **`<title>` は旧称 `Champagne Brut Réserve`** |
| 🔴 **`/fr/collection/brut-rose`** | 🔴 **`<h1> Champagne Le Rosé`。スペック（Ch45/PN35/Meunier20・`36 mois`・`Dosage Extra Brut`）** |
| **`/fr/collection/blanc-de-blancs-grand-cru`** | **`<h1> Champagne Le Blanc de Blancs`。4 グラン・クリュ村・`5 ans`・`Dosage Extra Brut`** |
| **`/fr/collection/brut-nature` / `brut-sous-bois` / `vintage` / `demi-sec`** | **色の確定（全て白）＋ MLF の記述箇所の特定（Brut Nature = 実施 / Demi-Sec = 部分実施）＋ Vintage 2016 の `1.9 g/l`・Demi-Sec の `40 g/l`** |
| 🔴 **`/fr/millesime/cuvee-louis-salmon`** | 🔴 **`BRUT BLANC DE BLANCS MILLÉSIME 2012`。4 クリュの内訳、25% 樽、115 か月、3.9 g/L、公式ノート、Terre de Vins 98 / B&D 96 / RVF 95** |
| 🔴 **`/fr/millesime/cuvee-elisabeth-salmon`** | 🔴 **`BRUT ROSÉ MILLÉSIME 2012`。1988 年創出、`co-fondatrice`、Ch55/PN45、115 か月、3.8 g/L、公式ノート、RVF 97 / B&D 96** |
| 🔴 **`/fr/millesime/clos-saint-hilaire`** | 🔴 **1 ha モノポール、マルイユ＝シュル＝アイの守護聖人、1964 年植樹、1995 年第 1 ミレジム、ブラン・ド・ノワール、樽仕込み、番号入り、4,500 本（2009）、馬耕。François Roland-Billecart の一人称証言** |
| 🔴 **`/fr/la-maison/histoire`** | 🔴 **1818 / 1900 / 1919 / **1958**（低温発酵＋débourbage à froid、ビール醸造家）/ 1964 / 1970 年代（ロゼ復活）/ 1993 / 1995 / 1999 / 2000 / 2010 / 2018 ×2。7 世代の氏名と生没年** |
| 🔴 **`/fr/la-maison/la-cuverie`** | 🔴 **`47 hectolitres` の小型サーモレギュレーテッド・タンク、クリュ別・セパージュ別醸造、「低温醸造こそ真の署名」。**⚠️ **`débourbage à froid` と低温発酵の順序が `/histoire` と逆** |
| 🔴 **`/fr/la-maison/le-vignoble`** | 🔴 **自社 `100 hectares`／調達含め `300 hectares`・`40 crus`／エペルネから半径 20 km** |
| 🔴 **`/fr/la-maison/engagements-durables`** | 🔴 **HVE・VDC = 2017 / ISO 50001（APAVE）= 2023 / 10 の鍵となる日付（2010 essais bio 〜 2025 100% certifié）/ 2021 年に調達の 75% が VDC / 自然の療法 4 種 / 養蜂箱 3 基 / 電動車両 / 水管理** |
| **`/fr/la-maison/les-caves-de-craie`** | **白亜のカーヴ 2 km、17・19 世紀。NV は 3〜4 年（appellation 規則の 2 倍）、ミレジメは 10 年** |
| **`/fr/la-maison/les-hommes`** | **Mathieu（7 代目・当主）／Antoine（export 担当副責任者）／Alexandre Bader（DG）／Denis Blée（畑・ワイン責任者）／Florent Nys（chef de cave、2005 年から François Domi の下で）／3 世代が参加する試飲委員会** |
| 🔴 **公式フィッシュ・テクニック 5 点**（`/storage/products/fiches/`、全点 `application/pdf`・1 ページ・テキストレイヤーあり） | 🔴 **`le-reserve-17401484221030248614.pdf`／`le-rose-1728896194422329265.pdf`／`le-blanc-de-blancs-17289141221019767598.pdf`／`cuvee-louis-salmon-2012-1713530042988600823.pdf`／`cuvee-elisabeth-salmon-2012-1737368191500117414.pdf`**<br>🔴 **全スペックと全公式ノートの出典。全点が `Par Florent NYS, œnologue et chef de cave` 署名** |
| **`/fr/pages/mentions-legales`** | **真正性の検証。社名・法人格・資本金・RCS/SIRET・TVA・住所・掲載責任者・ホスティング** |

### 🏛 公的登録（**すべて本調査で直接照会**）

| 登録 | 取得した情報 |
|---|---|
| 🏛 **`recherche-entreprises.api.gouv.fr/search?q=335480075`** | **SIREN `335480075`／`CHAMPAGNE BILLECART-SALMON (GCB)`／`date_creation 1954-01-01`／NAF `11.02A`／本店 SIRET `33548007500019`／`40 RUE CARNOT 51150 AY-CHAMPAGNE`／`code_commune 51030`／`etat_administratif: A`。**🔴 **`liste_id_bio: [1813]` —— Agence Bio へのポインタ。これが §Farming の突破口になった** |
| 🏛 🔴 **`opendata.agencebio.org/api/gouv/operateurs/?numeroBio=1813`**（`?siret=33548007500019` でも同一レコード） | 🔴 **`CHAMPAGNE BILLECART-SALMON`／`gerant: Mathieu Roland-Billecart`／Ecocert France `FR-BIO-01`／`etatCertification: ENGAGEE`／`dateEngagement 2022-07-11`／`datePremierEngagement 2019-07-31`／`productions: Vins de raisin, etatProduction AB, anneeReferenceControle 2026`／**🔴 **`activites: [Préparation]` のみ／`mixite: "Oui"`／`annuaireActivites: Entreprise de transformation Agro-Alimentaire - Cave`／`siteWebs: []`（空）**<br>**住所は `Lieux d'activité: 40 rue Carnot, 51160 Mareuil sur Ay` と `Siège social: 40 RUE CARNOT, 51160 AY-CHAMPAGNE`。`codeCommune` はいずれも `51030`** |
| 🏛 **`certificat.ecocert.com/entreprise/AC6B0CA4-8702-49D5-B7A0-4C91C8B5498B`** | **`CHAMPAGNE BILLECART SALMON` / `40 rue carnot, 51160 Mareuil sur Ay` / 状態 `Active` / 適用範囲 `Manufacturer & Processor` `Alcoholic Beverages` / 規格 `(EU) 2018/848 [FR]`。**⚠️ **証明書番号と有効期限は当該ページに表示されない** |
| 🏛 🔴 **TTB COLA Public Registry**（`ttbonline.gov/colasonline/publicSearchColasBasicProcess.do`） | 🔴 **CAPTCHA・ボット検査は無く、公開検索が機能した。`Total Matching Records: 1159`（brand `BILLECART%`, 2011–2025）。**<br>🔴 **`ELIZABETH`（z）綴りの承認ラベル 3 件（2015–2016）と `ELISABETH`（s）綴りの承認ラベル多数（2012–2021）を実測。**<br>**`LOUIS SALMON` の fanciful name は 2019 年 `CUVEE LOUIS SALMON` → 2022 年以降 `LOUIS SALMON` → 2025-08-28 `LOUIS SALMON BLANC DE BLANCS` と推移。**<br>**2023-04-14 に `BRUT RESERVE` の承認あり（旧称が米国ラベルに残存している証拠）** |
| 🏛 **AFNIC WHOIS（`champagne-billecart.fr` / `billecart.fr`）** | **前者の holder は `type: ORGANIZATION` / `contact: Champagne Billecart Salmon` / registrar Orange Business Services（EOLAS）/ `created 1998-02-25`。後者は holder `CBS234-FRNIC` / registrar GANDI / `created 2013-01-16`** |
| 🏛 **WHOIS（`billecart-salmon.com`）** | **`created 2017-06-16` / registrar `IP Twins SAS` / NS `iptwins` / registrant 秘匿。DNS 解決せず** |

### 取得できなかったもの / 存在しなかったもの（**絶対の証明ではなく「本調査では出なかった」**）

- 🔴 **公式サイトに `Ecocert` / `Agence Bio` / `AB` / `agriculture biologique` の語が一つも無い。**
  **有機認証の存在は公的登録側からしか判明しない。**
- 🔴 **`Demeter` / `Biodyvin` / `biodynamie` / `biodynamique` の語は、公式サイトにも Agence Bio レコードにも無い。**
- 🔴 **低温発酵の温度・時間の数値が公式に一切無い。**「basse température」「plus longue」のみ。
- 🔴 **`Le Réserve` / `Le Rosé` の `Extra Brut` の g/L 数値が公式に無い。**区分名のみ。
- 🔴 **OBP 4 本のマロラクティック発酵の有無が公式に無い**（`Brut Nature` と `Demi-Sec` のみ記述あり）。
- ⚠️ **アルコール度数・デゴルジュマン日・生産本数（Clos Saint-Hilaire を除く）・ルミュアージュ・圧搾比率が公式に無い。**
- ⚠️ **自社畑 100 ha の村別内訳、所有区画名、買いブドウの供給者名が公式に無い。**
- ⚠️ **`Mareuil-sur-Aÿ` の格付（Premier Cru か否か）を、本調査は一次資料で確認していない。**
  **公式は自らの村を Grand Cru と呼んでいない、という否定形しか確認できていない。**
- ⚠️ **`myorigin.billecart.fr` の内容を取得していない。**
- ⚠️ **公式に「メゾンの年間生産本数」「輸出比率」の記述が無い。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical レコード 4 件**（`migration/out/export/db_wine_canonical.json`、全 928 件中）:
`billecart-le-reserve` / `billecart-louis-salmon-2012` / `billecart-brut-rose` / `billecart-elizabeth-salmon-2012`。
**全件 `producer='Billecart-Salmon'` / `region='Champagne'` / `type='Champagne'`。**
⚠️ **`subregion` は 3 件が `Mareuil-sur-Aÿ`、1 件（Louis Salmon）が `Le Mesnil-sur-Oger — Côte des Blancs`。**
🔍 **なお `hebrart-special-club-2019`（Marc Hébrart）の `terroir_en` が
「same region as Billecart-Salmon」と本生産者に言及するが、別生産者のレコードであり本ドシエの対象外。**

🔍 **OBP: 4 本**（`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` の index 0 / 62 / 129 / 130）。
**全 4 本が `producer_state = exact`、`proposed_canonical_producer_id = producer:billecart-salmon`。**
**`match_state` は 2 本が `alias`（confidence 0.9）、2 本が `unresolved`（confidence 0.0）。**
🔴 **`_collision_risk` は 4 本とも `LOW`。**
🔒 **canonical・`REGISTER.md`・intake のいずれも編集していない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | 🔴 **High** | 🔴 **社名・法人格・資本金・SIRET・TVA・住所・掲載責任者が mentions légales で確定し、企業登録と突き合わせ済み。当主名が公式と Agence Bio の 2 系統で一致。**⚠️ **郵便番号と世代数のみ揺れる（記録済み）** |
| **Overview** | **High** | 低温発酵という自己規定、自社 100 ha / 総 300 ha の区別、7 代の継続がすべて一次で取れた |
| **History** | 🔴 **High** | 🔴 **沿革ページが静的取得でき、1818 / 1900 / 1919 / 1958 / 1964 / 1970s / 1993 / 1995 / 1999 / 2000 / 2010 / 2018 が確定。7 世代の氏名と生没年まで公式** |
| **Location** | **Medium-High** | 🔴 **自社 100 ha・総 300 ha・40 クリュ・エペルネ半径 20 km・カーヴ 2 km（17/19 世紀）が確定。Clos Saint-Hilaire は一人称証言つき。**⚠️ **村別内訳と区画名が不在** |
| 🔴 **Farming** | 🔴 **High（ただし語り方が難しい）** | 🔴 **公式の認証 3 種（HVE / VDC 2017、ISO 50001 2023）＋ 10 の鍵となる日付＋自然の療法 4 種が一次。**🔴 **加えて公的登録から Ecocert `FR-BIO-01` の有効な登録を発見し、その適用範囲（Préparation のみ・mixite Oui）まで確定した。**⚠️ **「2025 100% certifié」の対象だけが公式で不明** |
| **Winemaking** | 🔴 **High** | 🔴 **OBP 4 本すべてについて、公式フィッシュ・テクニックからセパージュ・樽比率・熟成月数・ドザージュを取得。低温発酵の起源（1958・ビール醸造家）とキュヴリー（47 hl）も確定。**⚠️ **温度数値・MLF・デゴルジュマンが不在。**⚠️ **débourbage の順序が公式内で矛盾** |
| **Style** | 🔴 **High** | 🔴 **OBP 4 本すべての公式テイスティングノート（Florent Nys 署名）を全文取得。公式掲載の第三者評点も 4 本分** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **4 行中 3 行を公式の正式名・スペック・ノートまで確定。3 行目も候補集合を公式レンジ上で 1 本に絞り込んだ（断定はしない）。**🔴 **公式の全 22 キュヴェを列挙済み** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **`C-1` 族・`C-4` 族への該当を公式＋canonical＋TTB の 3 者実測で裏づけ。**🔴 **`C-6` が当てはまらないことも実データで反証。**🔴 **canonical 4 件全件のフィールド値矛盾を 1 行ずつ突き合わせ済み** |
| **Staff Notes** | 🔴 **High** | ⚠️ **16 項目。🔴「Le Réserve は誤植」「オーガニックのメゾン」「有機認証なし」「全部自社畑」「妻」「MLF」「エリザベットはピノ主体」「モン・ブランシュ」「ドザージュ数値」「1830 年代のロゼ」「1816 年創業」という 11 の誤りを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を大きく超過。実感としては 88% 前後）。** | **OBP 4 本のうち 3 本について、公式の正式名・セパージュ・樽比率・熟成月数・ドザージュ・造り手のノートをそのまま言える。栽培は認証名と取得年、さらに公的登録の有機ステータスまで言える。**<br>**欠けているのは ① 3 行目の実ラベル、② 醸造の一部数値（温度・MLF・分析値）、③ 村別の畑内訳。**<br>**いずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。** |

**reached_70: YES.**

---

## Open Questions

1. 🔴 ⚠️ **【物理ラベル確認タスク】OBP 3 行目 —— `ROSÉ` セクション・NV・$280・キュヴェ名の印字が無い `Brut`。**
   **公式の現行レンジ上、NV のロゼは `Le Rosé`（旧称 `Brut Rosé`）1 本に絞られ、
   canonical にも `billecart-brut-rose` が 1 件だけ存在する。**
   🔴 **それでも確定としない理由は、メニューが `Brut` と印字しているのに対し、
   公式の現行 `Le Rosé` のドザージュ表記が `Extra Brut` であるため。**
   → **確認事項: ① 実ボトルのラベルが `Brut Rosé` か `Le Rosé` か、
   ② ラベルのドザージュ表記が `Brut` か `Extra Brut` か、③ 背ラベルのデゴルジュマン／ロット表記。**
   → **これが取れれば `C-4` 該当のまま `billecart-brut-rose` へ解決できる。**
2. ⚠️ **コミューン名 `Mareuil-sur-Aÿ` と `Aÿ-Champagne` の関係。**
   **🏛 企業登録と Agence Bio が同一の `codeCommune 51030` に対して両方の名前を持っている。**
   **公式サイトは一貫して `Mareuil-sur-Aÿ` を用いる。**
   → **どちらを canonical の `subregion` に置くかは表示方針の問題。本ドシエでは判断していない。**
   → **併せて郵便番号 `51160` / `51150` の揺れも未解決。**
3. ⚠️ **`Mareuil-sur-Aÿ` の格付（Premier Cru か否か）を一次資料で確認していない。**
   **本調査で確認できたのは「公式は自らの村を Grand Cru と呼んでいない」という否定形のみ。**
   → **Comité Champagne / INAO の cahier des charges で échelle des crus を確認する必要がある。**
   → **OBP 2 行目の `Grand Cru` の解釈（果実の産地を指す）はこれと独立に成立するので、緊急度は低い。**
4. 🔴 ⚠️ **低温発酵の温度と時間、`débourbage à froid` の温度。公式に数値が一切無い。**
   **メゾンの最大の売りでありながら、公式は定性表現しか出していない。**
   → **蔵訪問、またはプレス向け資料でしか埋まらない。**
   → 🔴 **併せて、`débourbage à froid` と低温発酵の導入順序が `/histoire` と `/la-cuverie` で逆である点の解消。**
5. 🔴 ⚠️ **OBP 4 本のマロラクティック発酵の有無。**
   **公式は `Brut Nature`（実施）と `Demi-Sec`（部分実施）にしか書いていない。**
   **canonical は 4 件すべてに「MLF あり」と書いているが、公式の裏づけが無い。**
   → **フィッシュ・テクニックの英語版、または輸入元の技術資料が要る。**
6. ⚠️ **`myorigin.billecart.fr` の内容が未取得。**
   **公式フィッシュ 5 点すべてが「あなたのキュヴェの秘密は myorigin で」と誘導しており、
   セパージュのヴィンテージ別内訳（NV の「2020 年基準」以外の年）が置かれている可能性が高い。**
   → 🔴 **`Le Réserve` の「平均 15 年分の収穫」の内訳が取れれば、NV の release identifier 問題（`V-1` 族）にも効く。**
7. ⚠️ **`Le Réserve` / `Le Rosé` の `Extra Brut` の実 g/L。**
   **公式は区分名しか出さない。canonical は 3–4 g/L（Le Réserve）と 7 g/L（Le Rosé）を持つが、
   後者は `Extra Brut`（≤6 g/L）と両立しない。**
   → **背ラベルまたは輸入元資料が要る。**
8. ⚠️ **改称の完了時期。`Brut Réserve → Le Réserve`、`Brut Rosé → Le Rosé`。**
   **公式サイト内（URL・`<title>`・沿革本文）と 🏛 TTB COLA（2023-04-14 に `BRUT RESERVE` 承認）に旧称が残る。**
   → 🔴 **canonical に「旧称」を表現する場所が無い（§Canonical Conflict shape B）。設計判断。**
9. ⚠️ **世代数 6 / 7 の公式内矛盾。** **`/histoire` の見出しだけが 6 で、他はすべて 7。**
   **更新漏れと読めるが、公式に確認しない限り断定しない。**
10. ⚠️ **`Élisabeth Salmon 2012` の赤ワイン比率が「8%」（製品ページ）と「Moins de 10%」（フィッシュ）で粒度が違う。**
    **矛盾ではないが、staff は「10% 未満」と言うのが安全。**
11. ⚠️ **Clos Saint-Hilaire の生産本数が「4,500 本」（2009 の製品ページ）と
    「3,500〜7,500 本」（沿革ページ、全ミレジム共通）で並存。**
    **年ごとの本数は 2009 以外未確認。**
12. 🔴 **canonical 4 件のフィールド値が公式と広範に食い違っている（§Canonical Conflict shape A、19 項目）。**
    **`obp_note` / `description` / `tasting` を staff 向けに使うのであれば、
    公式スペックへの差し替えが要る。**
    → 🔒 **canonical への書き込みは本書では行っていない。昇格可否は Akio / CTO 判断。**
