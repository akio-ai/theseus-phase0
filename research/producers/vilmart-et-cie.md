# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical にこの生産者のレコードは 1 件しか存在しない**（`vilmart-coeur-de-cuvee-2016`）。
> 🔍 **`producer` フィールド一致 1 件 / prose のみの一致 0 件**（`D-2026-08-05-08` の部分文字列誤検出はゼロ）。
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagnevilmart.fr／公式フィッシュ・テクニック（PDF）／公式ボトルショット画像で確認**（一次資料）
> `🏛` **公的登録**（recherche-entreprises.api.gouv.fr / Agence Bio / INAO 官報 CDC）
> `⚠️` **出典間で食い違っている／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.champagnevilmart.fr/`（FR 原本）**
> 走査元: **`sitemap.xml` → `page-sitemap1.xml`（34 URL）＋ `vins-sitemap1.xml`（18 URL）＋ `wp-json` の product / media 列挙**
> 併用: ✅ **公式フィッシュ・テクニック 12 点（`/wp-content/uploads/…`、全点 `%PDF` 実体・テキストレイヤーあり）**
> 併用: ✅ **公式ボトルショット 4 点（Grand Cellier NV / Grand Cellier d'Or 2021 / Cœur de Cuvée 2017 / Blanc de Noirs 2017 / Blanc de Blancs）のラベル面を実読**
>
> ---
>
> 🔴 **① 最初に踏んだのは罠だった —— `vilmart.fr` は公式サイトではない。**
> 🔴 **`https://vilmart.fr/` は `Dovendi` のドメイン売却ランディングページ（"This domain name is managed by Dovendi"）である。**
> **タスク指示は「公式サイトは `vilmart.fr` ドメイン族にあると思われる」としていたが、実測で否定された。**
> **本ドシエは `vilmart.fr` の内容を 1 語も使っていない。** → §Sources 冒頭
> **公式は `https://www.champagnevilmart.fr/`。mentions légales が `SA CHAMPAGNE VILMART ET CIE / RCS Reims B 308 076 744` を名乗り、
> 🏛 企業登録の SIREN `308076744`・代表 `Laurent CHAMPS` と完全に一致した（真正性チェック合格）。**
>
> 🔴 **② OBP 4 行のうち 3 行が canonical gap だが、その 3 行はいずれも「メニューが間違っている」形ではない。**
> **`Grand Cellier` は実在する現行 NV キュヴェで、ラベルに `GRAND CELLIER / PREMIER CRU / à Rilly la Montagne` と刷られている。**
> **`Cœur de Cuvée 2017` は実在する現行ミレジムで、ラベルに `CŒUR DE CUVÉE / 2017 / PREMIER CRU` と刷られている。**
> **canonical はこの生産者について 1 キュヴェ 1 ヴィンテージしか持っていない。** → §Canonical Conflict
>
> 🔴 **③ 4 行目 `Les Blanches Voies` は「キュヴェ名」ではなく「区画名」である。実ラベルで確認した。**
> **公式ボトルショットのラベルは 2 本とも 3 段組で、**
> **`BLANC DE BLANCS 2011` / `LES BLANCHES VOIES`、`BLANC DE NOIRS 2017` / `LES BLANCHES VOIES`。**
> 🔴 **すなわち `LES BLANCHES VOIES` は、ミレジム付きのキュヴェ名の下に添えられる区画の副題である。**
> 🔴 **公式の「L'expérience Les Blanches Voies」は、この 2 本を明示的に `quatre cuvées millésimées`（4 本のミレジメ）の一部として並べる。**
> → 🔴 **公式レンジに NV の Blanc de Blancs は 1 本も存在しない。したがって OBP の `NV` は造り手の表示と一致しない。**
> → ⚠️ **ただし Batch 10 の教訓に従い「メニューが defective」と断定はしない。**
> **`Extra Brut` の表示可否と現行ミレジムは実物ラベルでしか決着しない。** → §Staff Notes・§Open Questions 1
>
> 🔴 **④ canonical の 1 件は、typed field を含めて造り手と食い違っている。**
> **`grapes` 70/30 ⟷ 公式 80/20 ／ `dosage` 5 g/L ⟷ 公式 7 g/l ／
> `aging` "large Burgundy barrel" ⟷ 公式 `pièces de chêne de 228 l`（＝小樽）／
> `winemaking` "Partial MLF" ⟷ 公式 `Sans fermentation malo-lactique`（全 12 フィッシュ）。**
> 🔴 **とりわけ MLF は、公式が「メゾンの特質そのもの」と名指ししている点であり、canonical はそれを反転させている。**
> → §Canonical Conflict。**Batch 8–10 の「10/10 で矛盾」という base rate は、11 軒目でも崩れなかった。**
>
> ⚠️ **調査上の制約**
> **① `Cœur de Cuvée 2016` は公式のどこにも無い。**現行 shop は 2013 マグナムと 2017 ボトルのみ、
>    media library の PDF 18 点にも 2016 のフィッシュは無く、URL 推測（5 パターン）も全 404。
>    🔴 **これは「2016 が存在しない」証明ではない。造り手のサイトは現行在庫しか載せない。** → Open Questions 2
> **② Agence Bio は SIRET 一致で `nbTotal: 0` を返した（完全解決するクエリのゼロ件＝有効な陰性）。** → §Farming
> **③ RM / NM の matriculation コードは公式サイトにも取得したラベル面にも現れない。** → Open Questions 4

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Vilmart & Cie** |
| **公式表記** | ✅ **`Champagne Vilmart & Cie`**（全フィッシュ・テクニックのフッター）／✅ **`Maison Vilmart`**（本文）／✅ **ラベル面は `Vilmart & C<sup>ie</sup>`（筆記体、`ie` は上付き）** |
| **サイトのタイトル** | ✅ **`Champagne Vilmart - Maison de Champagne depuis 1890`** |
| 🔴 **法人（公式）** | ✅ **`SA CHAMPAGNE VILMART ET CIE`**（mentions légales）<br>**`RCS : Reims B 308 076 744`／`N° TVA Intracommunautaire : FR 82 308076744`** |
| 🔴 **法人（🏛 公的登録）** | 🏛 **SIREN `308076744`／`nom_complet: CHAMPAGNE VILMART ET COMPAGNIE`／`nature_juridique 5599`（SA à conseil d'administration）**<br>🏛 **SIRET 本店 `30807674400017`／NAF `01.21Z`（ブドウ栽培）／`date_creation: 1975-01-01`／`etat_administratif: A`／TVA `FR82308076744`** |
| 🔴 **住所（公式）** | ✅ **`BP 4 – 5, rue des Gravières – 51500 Rilly-la-Montagne`**（mentions légales・全フィッシュのフッター・全ページのフッターで一致） |
| ⚠️ **住所（🏛 登録）** | ⚠️ 🔴 **`4 RUE DE LA REPUBLIQUE 51500 RILLY-LA-MONTAGNE`**（`code_commune 51461`／`lat 49.1645, long 4.0442`）<br>🔴 **公式が一貫して使う `5 rue des Gravières` と、登録上の本店 `4 rue de la République` は別の街路である。**<br>**同一コミューン・同一 SIRET なので同一事業者だが、どちらが現行の実務所在かは確定していない。** → Open Questions 5 |
| **電話 / FAX / メール** | ✅ **`+33 3 26 03 40 01` / `03 26 03 46 57` / `patricia@champagnevilmart.fr`** |
| **サイト掲載責任者** | ✅ **`Directeur de publication : M. Laurent CHAMPS, Président Directeur Général`** |
| **サイト制作** | ✅ **`Rédaction, design et réalisation : SOWINE`** |
| 🔴 **当主 / 醸造長** | 🔴 ✅ **`Laurent Champs`。公式は `Chef de Cave` と明記。**<br>🏛 **企業登録の `dirigeants` 筆頭が `CHAMPS Laurent Christophe`（1968 年生）、qualité `Président du conseil d'administration et directeur général`。公式と公的登録が一致する。** |
| 🏛 **その他の役員** | 🏛 **`BIESSY (CHAMPS) Nathalie`（1970 年生、administrateur）／`CHAMPS René`（1937 年生、administrateur）／`CHAMPS (VILMART) Nicole`（1944 年生、administrateur）**<br>🔴 **`CHAMPS (VILMART) Nicole` の旧姓 Vilmart が、公式沿革の「René Champs は Renan Vilmart の gendre（娘婿）」という記述と符合する。** |
| **次世代** | ✅ **`Thomas Champs`（Laurent の息子）。2020 年に参画。「スポーツの起業・マネジメント修士」** |
| 🔴 **創業年** | 🔴 ✅ **1890 年。**「**Désiré Vilmart fonde la Maison au cœur du village de Rilly-la-Montagne**」<br>🔴 ✅ **ラベルの紋章直下に `Depuis 1890` が刷られている**（Grand Cellier NV / Cœur de Cuvée 2017 の実ラベルで確認） |
| ⚠️ **世代数** | ⚠️ **公式メタ記述は `un savoir-faire transmis depuis cinq générations`。**<br>**一方で沿革ページが名指しするのは Désiré → Charles → Renan → René Champs → Laurent Champs → Thomas Champs の 6 名。**<br>→ ⚠️ **「5 代」は Thomas を数えない読みと整合するが、公式は明示していない。** → §Staff Notes ⚠️ ⑧ |
| **認証（公式）** | ✅ 🔴 **`Viticulture Durable en Champagne (VDC)` と `Haute Valeur Environnementale (HVE)`。**<br>🔴 **全 12 点のフィッシュ・テクニックの冒頭段落に、同一文で毎回書かれている。** → §Farming |
| 🔴 **認証（🏛 有機）** | 🏛 🔴 **Agence Bio に登録なし。SIRET `30807674400017` で照会 → `{"nbTotal":0,"items":[]}`。**<br>🏛 **企業登録側も `est_bio: false`／`liste_id_bio: null`。** → §Farming。**「ビオ」と言ってはならない。** |
| **canonical id** | 🔍 **1 件のみ**（`vilmart-coeur-de-cuvee-2016`。下記 §Canonical Conflict） |

### ⚠️ 同名の別生産者 —— **同じ村に 3 軒の Vilmart がいる**

🏛 **企業登録を `VILMART` × 郵便番号 `51500` で引くと 10 件が返る。うち Rilly-la-Montagne のワイン関連は次の 3 系統である。**

| 🏛 SIREN | 名称 | 住所 | 備考 |
|---|---|---|---|
| 🔴 **308076744** | 🔴 **CHAMPAGNE VILMART ET COMPAGNIE** | **4 rue de la République** | 🔴 **本ドシエの対象。OBP の `Vilmart & Cie`** |
| ⚠️ **800821142** | ⚠️ **CHAMPAGNE VILMART PERE ET FILS** | **16 rue Kellermann** | ⚠️ 🔴 **別の生産者。`FRANCK VILMART`（SIREN 327768891）が `liste_enseignes: ["CHAMPAGNE VILMART PERE ET FILS"]` を持つ** |
| ⚠️ **503820144 / 504526120** | **VILMART-VATEL / DANIELE VILMART (VATEL)** | **53・57 rue de Chigny** | **NAF 01.21Z。別事業者** |

→ 🔴 **`Vilmart Père et Fils` は `Vilmart & Cie` ではない。卓上で混同してはならない。** → §Staff Notes ⚠️ ①

---

## Overview

✅ **1890 年、Désiré Vilmart がモンターニュ・ド・ランスの麓、リリー＝ラ・モンターニュの村の中心にメゾンを創設した。
以後、息子 Charles、孫 Renan と受け継がれ、1963 年に Renan の娘婿 René Champs が経営を引き継ぐ。
1995 年から Laurent Champs が当主かつ chef de cave を務め、2020 年に息子 Thomas が加わっている。**

🔴 ✅ **メゾンが自らの署名として名指しするものは、はっきりと 2 つである。**

🔴 ✅ **① 全キュヴェの木樽仕込み。**
「**ジュースは静かに foudres と fûts de chêne へ運ばれ、そこで一次アルコール発酵が始まる。
これがメゾンの特質のひとつである —— `全キュヴェの醸造は例外なく木の下で行われる`。
それがワインに独自の性格を、果実味と丸みと繊細さを与える。**」（`/faconner-philosophie-et-elaboration`）

🔴 ✅ **② マロラクティック発酵を行わないこと。**
「**マロラクティック発酵の不在は、Vilmart のシャンパーニュに固有のもうひとつの特質である。
新鮮さ、テンション、繊細さ、そして香りの典型性が、それによって保たれる。**」
🔴 **取得した公式フィッシュ・テクニック 12 点すべてに `Sans fermentation malo-lactique` の 1 行がある。例外はない。**

🔴 ✅ **メゾンは「買いブドウを混ぜる大メゾン」ではなく、11 ヘクタールの自社畑で完結する規模である。**
「**11 ヘクタールの畑。リリー＝ラ・モンターニュとヴィレール＝アルラン（Villers-Allerand）のテロワールに、
`もっぱらプルミエ・クリュのみ` 植えられている。**」

🔴 ✅ **セパージュ比率がシャンパーニュの常識と逆であることを、公式自身が売り文句にしている。**
「**70/30 シャルドネ／ピノ・ノワール。`シャンパーニュの伝統に逆らう独特の植栽比率`（un encépagement singulier, à contre-courant de la tradition champenoise）。**」

✅ **当主の言葉（公式トップ）** —
「**何よりもまず、そして特に、私はワインを造っている。シャンパーニュはそのあとに来る、私の最大の喜びとして。**」（Laurent Champs）

🔍 **THÉSEUS における状態は Billecart-Salmon の正反対で、「1 件しかないのに 4 行が当たりに来る」形。
canonical はこの生産者について `Cœur de Cuvée 2016` の 1 レコードしか持たず、
OBP の 4 行のうち 3 行（`Grand Cellier`・`Cœur de Cuvée 2017`・`Les Blanches Voies`）が
そもそも受け皿を欠いている。すなわち主たる問題は矛盾ではなく `不在` である。**

---

## History

✅ **公式沿革ページ（`/notre-histoire`）は縦スクロールの年表構成。全文が静的 HTML に含まれる。**

| 年 | 出来事 ✅ |
|---|---|
| 🔴 **1890** | 🔴 **`Désiré Vilmart` が、モンターニュ・ド・ランスの麓、リリー＝ラ・モンターニュの村の中心にメゾンを創設。**「**息子の Charles、次いで孫の Renan が彼を継ぐ。独立と大胆さが、すでにメゾンの精神を特徴づけていた。**」 |
| 🔴 **1939–1945** | 🔴 **`Renan` が経営体の破壊に立ち会う。**「**勇気と決意をもって、彼は難を免れた古いカーヴの上に建物と設備を再建する —— メゾンは今日もなおその建物を占めている。**」 |
| **1963** | **`René Champs`、Renan の `gendre`（娘婿）が経営を引き継ぐ。「彼は Renan の傍らで vigneron の仕事のすべてを学び、`Chevalier de l'Ordre du Mérite Agricole` に叙される」** |
| 🔴 **1995** | 🔴 **`Laurent Champs`（René の息子）が情熱的なエネルギーをメゾンに吹き込む。**「**彼の世界各地への定期的な旅が、今日、生産の半分以上を 30 か国ほどへ輸出することを可能にしている。**」 |
| **2020** | **`Thomas Champs`（Laurent の息子）が参画。「スポーツの起業・マネジメント修士を持ち、家族の savoir-faire を学びながら革新的な視点をもたらす」** |

⚠️ **公式沿革はこの 5 項目しか持たない。第一次大戦・フィロキセラ・échelle des crus への編入・キュヴェの創出年・
`Cœur de Cuvée` の初ミレジム年・`Les Blanches Voies` の植栽年は、いずれも公式に記載が無い。** → Open Questions 3

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| **本拠** | ✅ **`5, rue des Gravières`（BP 4）、51500 Rilly-la-Montagne**（⚠️ 🏛 登録上の本店は `4 rue de la République`。上記 §Identity） |
| 🔴 **自社畑** | 🔴 ✅ **11 ヘクタール**（`11 Hectares de vignoble`） |
| 🔴 **村** | 🔴 ✅ **`Rilly-la-Montagne` と `Villers-Allerand` の 2 村。**「**Plantés exclusivement en Premier Cru, sur les terroirs de Rilly-la-Montagne et Villers-Allerand**」 |
| 🔴 **格付（🏛 一次法令）** | 🔴 🏛 **AOC Champagne の cahier des charges は、`premier cru` を名乗れるコミューンを列挙する条項 c) に `Rilly-la-Montagne` と `Villers-Allerand` の両方を含む。**<br>🔴 🏛 **`grand cru` を名乗れるコミューンの列挙（条項 b、17 村）には、`Rilly-la-Montagne` も `Villers-Allerand` も入っていない。**<br>→ 🔴 **したがってこのメゾンの畑は 100% プルミエ・クリュであり、グラン・クリュではない。** |
| 🔴 **格付（造り手自身の表示）** | 🔴 ✅ **ラベル面に `PREMIER CRU` と `à Rilly la Montagne` が刷られている（Grand Cellier NV / Grand Cellier d'Or 2021 / Cœur de Cuvée 2017 の実ラベルで確認）。**<br>🔴 ✅ **全 12 フィッシュの冒頭も `classés Premier Cru`。** |
| 🔴 **セパージュ比率** | 🔴 ✅ **70% Chardonnay / 30% Pinot Noir。**「**`un encépagement singulier, à contre-courant de la tradition champenoise`**」 |
| 🔴 **樹齢** | 🔴 ✅ **平均 40 年。**「**最も古いものは 65 年で、メゾンの最も高名なキュヴェのために取り置かれている。**」<br>⚠️ **フィッシュ側は個別に `soixante ans`（60 年、Cœur de Cuvée / Blanc de Blancs / Émotion）と `cinquante ans`（50 年、Grand Cellier d'Or / Blanc de Noirs）と書き分ける。** |
| 🔴 **区画（唯一名指しされるもの）** | 🔴 ✅ **`Les Blanches Voies` —— リリー＝ラ・モンターニュの区画。**下記参照 |
| **カーヴ** | ✅ **`caves de craie`（白亜のカーヴ）。1939–45 の破壊を免れた旧カーヴの上に再建された建物を今も使う** |
| ⚠️ **熟成蔵** | ⚠️ ✅ **`foudrerie`（フードル蔵）が複数ある。**「**試飲は当家の `foudreries` のひとつ、空調された空間で行われます。**」（Les Secrets du Bois の案内） |

### 🔴 ✅ Les Blanches Voies（**OBP 4 行目の正体。区画である**）

🔴 ✅ **公式の「L'expérience Les Blanches Voies」ページ** —
「**Vilmart & Cie の最も高名なキュヴェのひとつを発見してください。
リリー＝ラ・モンターニュの `parcelle mythique Les Blanches Voies` に由来するものです。
この没入的な体験は、われわれの祖先伝来の savoir-faire の象徴である
`quatre cuvées millésimées`（4 本のミレジメ・キュヴェ）を通る稀な旅をご提案します。**」

🔴 ✅ **その 4 本として公式が列挙するもの:**
**`Grand Cellier d'Or` ／ `Cœur de Cuvée` ／ `Blanc de Noirs « Les Blanches Voies »` ／ `Blanc de Blancs « Les Blanches Voies »`**

🔴 ✅ **Blanc de Blancs のフィッシュ・テクニックも区画名を明記する** —
「**100% Chardonnay classé Premier Cru、リリー＝ラ・モンターニュの `(parcelle des Blanches Voies)` の樹齢 60 年の樹に由来**」

🔴 ✅ **公式ボトルショットのラベル面（実読）**
| ボトル | ラベルの 3 段組 |
|---|---|
| 🔴 **Blanc de Blancs** | **`CHAMPAGNE` / `Vilmart & Cie` / `BLANC DE BLANCS 2011` / `LES BLANCHES VOIES`** |
| 🔴 **Blanc de Noirs** | **`CHAMPAGNE` / `Vilmart & Cie` / `BLANC DE NOIRS 2017` / `LES BLANCHES VOIES`** |

→ 🔴 **`LES BLANCHES VOIES` はキュヴェ名ではなく、ミレジム付きキュヴェ名の下に添えられる区画の副題である。**
→ 🔴 **そしてこの副題を持つ 2 本は、いずれも `millésimé` である。**
⚠️ **なお Blanc de Blancs の商品画像は `blanc-de-blanc-2011-web.png`（2011）で、販売中の中身は 2013。
公式サイトが画像を差し替えていない。ラベル書式の証拠としては有効だが、年号の証拠としては使えない。**

⚠️ **Blanc de Noirs 2017 のフィッシュ本文は区画名を書かない**（`vignes de Rilly-la-Montagne de cinquante ans d'âge` のみ）。
**区画名はラベルと体験ページにあり、フィッシュに無い。公式内で情報の載る場所が揃っていない。**

❓ **公式に無い**: 区画の面積・植栽年・土壌断面・標高・向き、11 ha の村別内訳、`Les Blanches Voies` 以外の区画名。

---

## Farming

🔴 **本節の要点は 1 つ —— このメゾンは「持続可能」の認証を持ち、「有機」の認証は持っていない。**
**両者は別の主張であり、混ぜると即座に嘘になる。**

### ✅ 公式が名指しする認証（**全 12 フィッシュに同一文で反復される**）

✅ **「`Viticulture Durable (VDC)` および `Haute Valeur Environnementale (HVE)` の認証に沿って、
Maison Vilmart はそのテロワールへの最大限の敬意をもって畑を耕す。」**

| 認証 | 公式の記述 |
|---|---|
| 🔴 **VDC**（Viticulture Durable en Champagne） | ✅ **保有を明記。全フィッシュの冒頭段落。**⚠️ **取得年は公式に記載が無い** |
| 🔴 **HVE**（Haute Valeur Environnementale） | ✅ **保有を明記。全フィッシュの冒頭段落。**⚠️ **レベル（1/2/3）も取得年も公式に記載が無い** |

### 🔴 🏛 有機 —— **登録が「無い」ことを実測で確定した**

| 照会 | 🏛 結果 |
|---|---|
| 🔴 **Agence Bio（SIRET 完全一致）** | 🔴 **`GET /api/gouv/operateurs/?siret=30807674400017` → `{"nbTotal":0,"items":[]}`**<br>🔴 **完全に解決するクエリがゼロ件を返した。JS シェルでも Cloudflare gate でもない。有効な陰性である。** |
| **Agence Bio（名前 × 県）** | **`?q=VILMART&departement=Marne` → 1 件のみ。それは `VILMART Maxime`（numeroBio 131765、フィニステール県 `CHÂTEAUNEUF DU FAOU`、キャベツ・イチゴ・香草）。**<br>🔴 **同姓の完全な別事業者であり、しかも Ecocert 証明は `ARRETEE`（2019-02-28 停止）。本件とは無関係。** |
| **企業登録の相互参照** | 🏛 **SIREN `308076744` の `complements.est_bio: false`／`siege.liste_id_bio: null`。**<br>**（比較: Billecart-Salmon は同じフィールドに `liste_id_bio: [1813]` を持っていた。）** |

→ 🔴 **したがって「Vilmart は有機認証を受けています」は言ってはならない。**
→ ⚠️ **同時に「有機的な栽培をしていません」も言ってはならない。実践については公式が何も述べていない。**
⚠️ **`bio` / `biologique` / `biodynamie` / `Demeter` / `Biodyvin` / `Ecocert` の語は、
公式サイトの取得した全ページ・全フィッシュに一度も現れない。** → §Staff Notes ⚠️ ③

### ✅ 収穫と搾汁（公式が名指しする実務）

🔴 ✅ **「収穫の際、`各房は手で丁寧に摘まれ`、最良の果実を選び、`圧搾機に至るまで果粒を無傷に保つ`。」**
🔴 ✅ **`pressoir traditionnel`（伝統的圧搾機）を使う。**
🔴 ✅ **「`Le débourbage se fait par gravité`（澱下げは重力によって行われる）—— 品質を保つために。」**
✅ **全 12 フィッシュが `Vendanges manuelles`（手摘み）を年号つきで明記する。**

⚠️ **除草・防除・被覆作物・馬耕・カーボンについての記述は、公式サイトに一切無い。** → Open Questions 6

---

## Winemaking

### 🔴 メゾンの署名 —— **全キュヴェ木樽仕込み ＋ マロラクティック発酵なし**

🔴 ✅ **`/faconner-philosophie-et-elaboration`（公式）** —
「**ジュースは静かに `foudres` と `fûts de chêne` へ運ばれ、そこで `première fermentation alcoolique` が始まる。
これがメゾンの特質のひとつである —— `la vinification de l'ensemble des cuvées se fait exclusivement sous bois`
（全キュヴェの醸造は例外なく木の下で行われる）。それがワインに独自の性格を、果実味と丸みと繊細さを与える。**
**マロラクティック発酵の不在は、Vilmart のシャンパーニュに固有のもうひとつの特質である。
新鮮さ、テンション、繊細さ、そして香りの典型性が、それによって保たれる。**
**`dix mois` の木樽醸造ののち、ワインは瓶詰めされ、ドメーヌの白亜のカーヴに留まる ——
`ノン・ミレジメは 3 年から 4 年`、`ミレジメは 5 年から 8 年`。**」

### 🔴 ✅ 木の使い分け —— **`foudre` と `pièce de 228 l` は別の道具であり、キュヴェごとに分かれている**

🔴 ✅ **公式体験「Les Secrets du Bois」が、この対比を試飲の設計そのものに使っている。**
**「`Grand Cellier — vin clair tiré du foudre`（フードルから抜いた vin clair）／
`Grand Cellier — en Champagne` ／ `Cœur de Cuvée — d'un fût bourguignon`（ブルゴーニュ樽から）／
`Cœur de Cuvée — en Champagne`」**

| 容器 | ✅ 公式フィッシュがこの容器を指定するキュヴェ |
|---|---|
| 🔴 **`foudres de chêne`（大樽）** | **Grande Réserve ／ Grand Cellier ／ Cuvée Rubis**（＝いずれも NV） |
| 🔴 **`pièces de chêne de 228 l`（ブルゴーニュ小樽）** | 🔴 **Cœur de Cuvée ／ Grand Cellier d'Or ／ Blanc de Blancs ／ Émotion**（＝いずれもミレジメ） |
| **`pièces de chêne de 10 HL`** | **Blanc de Noirs 2017** |
| **`pièces de chêne de 400 et 600 l`** | **Ratafia Chardonnay**（7 年） |

→ 🔴 **すなわち「Vilmart はブルゴーニュの大樽（フードル）で熟成させる」という要約は、
このメゾンの `NV` にしか当たらず、`Cœur de Cuvée` には当たらない。** → §Canonical Conflict

⚠️ **樽の新樽比率、樽材の産地、樽職人（tonnelier）名、樽の更新サイクルは、公式に一切記載が無い。** → Open Questions 7

### 🔴 ✅ 公式フィッシュ・テクニックの全スペック（**12 点の PDF から機械的に転記。FR 原本のみ採用**）

| キュヴェ | セパージュ | ベース／リザーヴ | 木 | 瓶熟 | MLF | ドザージュ |
|---|---|---|---|---|---|---|
| 🔴 **GRAND CELLIER**（NV）⭐OBP 1 | 🔴 **Chardonnay 70% / Pinot Noir 30%** | 🔴 **`Vendanges manuelles 2022` ／ `Vins de réserve 2020/2021`** | 🔴 **`dix mois en foudres de chêne`** | ⚠️ **フィッシュに記載なし**（公式一般則: NV は 3–4 年） | 🔴 **`Sans`** | 🔴 **`8 g/l`** |
| 🔴 **CŒUR DE CUVÉE 2017** ⭐OBP 2 | 🔴 **Chardonnay 80% / Pinot Noir 20%**、樹齢 60 年 | 🔴 **`Vendanges manuelles 2017`**／🔴 **`Élaboré uniquement avec le cœur de la cuvée (1400 l au lieu de 2050 l)`** | 🔴 **`dix mois en pièces de chêne de 228 l`** | 🔴 **`Soixante-dix mois sur lies`**（＝70 か月＝5 年 10 か月） | 🔴 **`Sans`** | 🔴 **`7 g/l`** |
| **CŒUR DE CUVÉE 2013**（マグナム） | **Chardonnay 80% / Pinot Noir 20%**、樹齢 60 年 | **`2013` ／ 同じ 1400 l / 2050 l** | **`228 l`** | **`Soixante-dix mois`** | **`Sans`** | **`7 g/l`** |
| 🔴 **BLANC DE BLANCS 2013**（＝ `Les Blanches Voies`）⭐OBP 4 候補 | 🔴 **Chardonnay 100%、`parcelle des Blanches Voies`、樹齢 60 年** | **`Vendanges manuelles 2013`** | 🔴 **`dix mois en pièces de chêne de 228 l`** | 🔴 **`Quatre-vingt-quatre mois`**（84 か月＝7 年） | 🔴 **`Sans`** | 🔴 **`4 g/l`** |
| 🔴 **BLANC DE NOIRS 2017**（＝ `Les Blanches Voies`） | **Pinot Noir 100%、樹齢 50 年** | **`Vendanges manuelles 2017`** | 🔴 **`dix mois en pièces de chêne de 10 HL`** | 🔴 **`Quatre-vingts mois sur lies`**（80 か月） | 🔴 **`Sans`** | 🔴 **`4 g/l`** |
| **GRAND CELLIER D'OR 2021** | **Chardonnay 80% / Pinot Noir 20%**、樹齢 50 年 | **`2021`** | **`dix mois en pièces de chêne de 228 l`** | **`Trente-huit mois`**（38 か月） | **`Sans`** | **`7 g/l`** |
| **GRANDE RÉSERVE**（NV） | 🔴 **Pinot Noir 70% / Chardonnay 30%**（**比率が逆**） | **`2022` ／ `Vins de réserve 2020/2021`** | **`dix mois en foudres de chêne`** | ⚠️ **記載なし** | **`Sans`** | **`6 g/l`** |
| **CUVÉE RUBIS**（NV・ロゼ） | **Pinot Noir 90%（`dont 15 % de vin rouge`）/ Chardonnay 10%** | **`2023` ／ `Vins de réserve 2022/2021`** | **`dix mois en foudres de chêne`** | ⚠️ **記載なし** | **`Sans`** | **`6 g/l`** |
| **ÉMOTION 2016**（ミレジメ・ロゼ） | 🔴 **Pinot Noir 40%（`rosé de saignée`）/ Chardonnay 60%**、樹齢 60 年 | **`2016`** | **`dix mois en pièces de chêne de 228 l`** | **`Soixante mois`**（60 か月） | **`Sans`** | **`8 g/l`** |
| **RATAFIA CHARDONNAY** | **Chardonnay 100%（`moût de raisin`）** | **`septembre 2020`** | 🔴 **`sept ans en pièces de chêne de 400 et 600 l`** | — | — | 🔴 **`Blocage de la fermentation alcoolique par ajout d'alcool (fine de champagne)`／`50 cl`** |

### ⚠️ 版の比較 —— **スペックは版をまたいで安定している**

⚠️ **`Grand Cellier` は 2020 年版フィッシュ（ベース 2016、リザーヴ 2014/2015）と現行 T23 版（ベース 2022、リザーヴ 2020/2021）で、
`70% Chardonnay / 30% Pinot Noir`・`dix mois en foudres de chêne`・`Sans fermentation malo-lactique`・`Dosage 8 g/l` が完全に一致する。**
→ 🔴 **すなわち `Grand Cellier` は改称も再定義もされていない。同じ名前の同じワインが、ベース年だけを更新して続いている。**

⚠️ **`Cœur de Cuvée` も 2013 マグナムと 2017 ボトルで `80/20`・`1400 l / 2050 l`・`228 l`・`70 か月`・`7 g/l` が一致する。**
→ ⚠️ **これは強い規則性だが、`2016` について同じ値を主張してよいという意味ではない。** → Open Questions 2

⚠️ **アルコール度数・デゴルジュマン日・生産本数（Blanc de Blancs / Blanc de Noirs を除く）・
ルミュアージュの方式・圧搾比率・酵母・リキュール・使用糖は、公式に一切記載が無い。**

---

## Style

### ✅ 公式テイスティングノート（**OBP 関連 3 本 ＋ 主要 NV**）

| キュヴェ | 公式ノート（フィッシュ・テクニックより） |
|---|---|
| 🔴 **GRAND CELLIER**（NV）⭐OBP 1<br>「L'expression de l'audace et de l'élégance Vilmart」 | **色**: 明るい黄金のローブ。躍動する細かな泡、際立った持続性。<br>**香り**: 「**複雑にして洗練された芳香のパレット。第一の香りにミネラルの調子が現れ、`陽光の下の温かい石` を思わせる美しい新鮮さの上に立つ。このミネラルの性格に、`ジューシーなマンダリンとひと刺しのベルガモット` という柑橘の繊細さが伴う。**」続いて**白い花**、**アニス（八角）などの甘いスパイス**が**エキゾチックな木**の調子と溶け合い、奥行きを生む。<br>**味わい**: **均衡と優雅。スパイスと黄色い果実の香りに刻まれた長い余韻。**<br>**マリアージュ**: ✅ **「柔らかいテクスチャーの料理との一致を探す。舌平目や turbot に短いソースを添えたもの、牡蠣などの貝類。アペリティフとしても容易に飲める。」** |
| 🔴 **CŒUR DE CUVÉE 2017**⭐OBP 2<br>「Une richesse et une identité uniques」 | **色**: 純金の照りを持つローブ。極度に繊細な発泡が、ディスク表面に優美で規則的な cordon を形づくる。<br>**香り**: 「**稀な複雑さ。エキゾチックな芳香と大きな純度のアクセントが絡み合う。最初の瞬間から `野生のミント` と `八角` の調子が生き生きとした新鮮さを吹き込む。空気に触れると、`オーブンから出たヴィエノワズリー` を思わせる美味なニュアンスが、`オレンジの皮` で繊細に香りづけされて加わる。**」<br>**味わい**: 「**寛大で、香りの約束に忠実。`ローストしたパイナップル` の風味の上に開花し、このキュヴェに独特の奥行きを与える。`ジンジャー` と `レモングラス` のタッチが強壮なエネルギーで試飲を句読点づけ、`荘厳なテンションと均衡` を創り出す。**」<br>**余韻**: 「**美しい持続性の終盤が、微かにスパイシーな調子の上に伸び、柑橘とトロピカルフルーツの優雅な航跡で喜びを引き延ばす。**」<br>**マリアージュ**: ✅ **「ザリガニとポルチーニ、帆立のタルタル、あるいは中心までポワレしたフォアグラが、このシャンパーニュに奥行きと美しい香りの発展をもたらす。」** |
| 🔴 **BLANC DE BLANCS 2013**（＝ `Les Blanches Voies`）⭐OBP 4 候補<br>「Une minéralité sensuelle」 | **色**: ⚠️ **フィッシュは「明るいレモンイエロー、銀の照り」、製品ページは「麦わら色、淡い緑の照り」と書き分ける（下記 §Canonical Conflict の内部不一致）。**<br>**香り**: 「**強度と力。`ジャスミン、オレンジ、ペパーミント` の調子で開き、`ブルボン・ヴァニラ、クレーム・パティシエール、アップル・クランブル` へ進む。**」<br>**味わい**: 「**美味で包み込むような口中。`マーマレード`、`レモンタルト` のニュアンス。芳香の奥行きのあとに新鮮さの感覚が終盤を制し、`洋梨と白桃` の調子。**」<br>**マリアージュ**: ✅ **「アペリティフ、または帆立、リ・ド・ヴォー、牡蠣やキャビアなどの海産物に。」** |
| **GRANDE RÉSERVE**（NV） | **色**: **銀の照りを持つブロンドのローブ「ピノ・ノワール主体のワインを告げる」**<br>**香り**: **黄色い果実（桃、アプリコットのコンポート）、サンザシとアカシア。第二の香りに微かなメントールと香木**<br>**味わい**: **鋭く明晰なアタック。`コンファレンス梨` と `ゴールデン林檎`、`バタービスケット`。絹のような終盤** |
| **BLANC DE NOIRS 2017**（＝ `Les Blanches Voies`） | **色**: **深い黄金の色調、細かく持続する泡の cordon**<br>**香り**: **`シロップ漬けの桃、ライチ、生の無花果`。アカシアの花のタッチ。`乾燥コケモモ、アンジェリカ、リコリス`** |
| **ÉMOTION 2016**（ミレジメ・ロゼ） | **色**: **琥珀の照りを持つ輝くロゼ**<br>**香り**: **`グリオットチェリー、フランボワーズ、グロゼイユ`、`スミレと乾燥バラ`、ひと刺しのヴァニラ**<br>**味わい**: **`ピンクグレープフルーツ、苺、バラ`** |
| **CUVÉE RUBIS**（NV・ロゼ） | **色**: **琥珀の照りを持つ濃密なロゼ**<br>**香り**: **`ローズウォーター` の優雅な調子から、`ジューシーなザクロ` を含むエキゾチックな果実と新鮮な赤い果実へ。空気に触れると `ナツメグ` の微妙なタッチ** |

### ✅ 公式が掲げる第三者の言葉（**公式サイト上に掲載されているもののみ**）

⚠️ 🔴 **これは「公式が自分のサイトに載せている」という事実の記録であって、
THÉSEUS がこの評価を採用したという意味ではない。**

- ✅ **`/nos-vins` の見出しに掲げられた一文**: 「**シャンパーニュにおける finesse を思うとき、Maison Vilmart は真っ先に思い浮かぶ名前のひとつだ。**」— **Antonio Galloni**

⚠️ **点数・受賞・格付けの掲載は、公式サイトに一切無い。** → Open Questions 8

---

## Important Cuvées

### ✅ 公式の現行レンジ（**全 9 品目。`sitemap` の `vins-sitemap1.xml` と `/nos-vins` が完全に一致**）

| # | 公式のキュヴェ名 | 種別 | 現行表示 |
|---|---|---|---|
| 1 | **Grande Réserve** | NV | — |
| 2 | 🔴 **Grand Cellier** | 🔴 **NV** | 🔴 ⭐**OBP 1 行目** |
| 3 | **Grand Cellier d'Or 2021** | ミレジメ | — |
| 4 | 🔴 **Cœur de Cuvée 2017** | 🔴 **ミレジメ** | 🔴 ⭐**OBP 2 行目** |
| 5 | 🔴 **Blanc de Blancs 2013**（ラベル副題 `LES BLANCHES VOIES`） | 🔴 **ミレジメ** | 🔴 ⭐**OBP 4 行目の最有力対応** |
| 6 | **Blanc de Noirs 2017**（ラベル副題 `LES BLANCHES VOIES`） | ミレジメ | — |
| 7 | **Cuvée Rubis** | NV・ロゼ | — |
| 8 | **Emotion 2016** | ミレジメ・ロゼ | — |
| 9 | **Ratafia Chardonnay** | ラタフィア（50 cl） | — |

🔴 **この 9 品目の外に、公式が現在売っている、あるいは現在紹介しているワインは無い。**
🔴 **`Les Blanches Voies` という名前の単独の商品は、`/nos-vins`・`vins-sitemap`・WooCommerce の product 列挙（28 URL）のいずれにも存在しない。**

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 4 本。alias 1 本 / unresolved 3 本**）

| # | OBP 印字 | VT | 価格 | セクション | intake | ✅ **公式での確認結果** |
|---|---|---|---|---|---|---|
| 1 | **`'Grand Cellier,' Premier Cru Brut`** | NV | $235 | `… \| BLENDS` | 🔴 **`unresolved`** | 🔴 ✅ **実在。現行 NV。ラベルは `GRAND CELLIER / PREMIER CRU / à Rilly la Montagne`。メニューは正しい。**🔴 **canonical に受け皿が無い＝gap** |
| 2 | **`'Coeur de Cuvée,' Premier Cru Brut`** | **2017** | $535 | `… \| BLENDS` | 🔴 **`unresolved`**（cuvée は alias、**vintage** が unresolved） | 🔴 ✅ **実在。現行ミレジム。ラベルは `CŒUR DE CUVÉE / 2017 / PREMIER CRU`。メニューは正しい。**🔴 **canonical が 2016 しか持たない＝vintage gap** |
| 3 | **`'Coeur de Cuvée,' Premier Cru Brut`** | **2016** | $440 | `… \| BLENDS` | **`alias`**（confidence 0.9） | ❓ 🔴 **公式では確認できなかった。下記参照** |
| 4 | **`'Les Blanches Voies,' Premier Cru Extra Brut`** | **NV** | **$1,040** | 🔴 `… \| **BLANC DE BLANCS**` | 🔴 **`unresolved`** | 🔴 ⚠️ **`Les Blanches Voies` は区画名であり、キュヴェ名ではない。対応する公式の商品は `Blanc de Blancs « Les Blanches Voies »` で、`millésimé` である。下記参照** |

---

### 🔴 1 行目 —— `Grand Cellier` は実在する。**「一本のワイン」であり、レンジでも旧称でもない**

🔍 **intake の evidence**: `'Vilmart & Cie' の canonical キュヴェ 1 件に一致無し: 'Grand Cellier'`。
🔴 **canonical はこの生産者について 1 キュヴェしか持たないので、`Grand Cellier` が当たらないのは当然である。**

#### 🔴 タスクの問い —— **「一本か、レンジか、旧称か」**

| 問い | ✅ 実測による答え |
|---|---|
| **一本のワインか** | 🔴 ✅ **Yes。`Grand Cellier` という名称の単一の NV キュヴェが、フィッシュ・ラベル・商品・ナビのすべてで一貫している。** |
| **レンジ（範囲名）か** | ⚠️ 🔴 **部分的に Yes。`Grand Cellier` を語頭に持つ商品は 2 つある —— `Grand Cellier`（NV）と `Grand Cellier d'Or`（ミレジメ）。**<br>🔴 **ただし公式はこの 2 つを「レンジ」としてまとめて呼んではいない。`/nos-vins` は 9 品目を平坦に並べるだけである。** |
| 🔴 **旧称（superseded）か** | 🔴 ✅ **No。旧称ではない。**<br>🔴 **2020 年版フィッシュ（ベース 2016）と現行 T23 版（ベース 2022）が、名称・セパージュ・容器・MLF・ドザージュのすべてで一致する。**<br>🔴 **加えて現行のボトルショットのラベルに `GRAND CELLIER` が実際に刷られている。** |

→ 🔴 **したがって本行は、Batch 10 が Billecart で見つけた「改称の過渡期に旧称が残る」形（未採番）には該当しない。**
→ 🔴 **番号を開く必要も、その形を引用する必要もない。これは単純な `canonical gap` である。**

⚠️ **公式が過去に `Grand Cellier Rubis` という名を使っていたかどうかは、本調査では確認できなかった。**
**取得できた最古の公式フィッシュ（2019 年基準の EN 版、ベース 2018）の見出しはすでに `CUVÉE RUBIS` である。**
🔴 **「昔は Grand Cellier Rubis といった」は、公式で裏づけられないので言ってはならない。** → Open Questions 9

⚠️ **メニューの `Brut` について。**
🔴 **取得したラベル面（`grand-cellier.png`）に `Brut` の語は無い。刷られているのは
`CHAMPAGNE` / `Vilmart & Cie` / `GRAND CELLIER` / `PREMIER CRU` / `à Rilly la Montagne` / `Depuis 1890` のみ。**
⚠️ **フィッシュのドザージュは `8 g/l` で、EU 規則上 `Brut`（12 g/l 未満）の範囲に入る。**
→ ⚠️ **つまりメニューの `Brut` は矛盾しないが、`造り手が表ラベルに刷っている語` でもない。** → §Open Questions 10

---

### 🔴 2 行目 —— `Cœur de Cuvée 2017`。**メニューが正しく、canonical が持っていない**

✅ **公式の説明（フィッシュ見出し）**: `CŒUR DE CUVÉE 2017` — 副題 `Une richesse et une identité uniques`。
🔴 ✅ **実ラベル**: `CHAMPAGNE` / `Vilmart & Cie` / `CŒUR DE CUVÉE` / `2017` / `PREMIER CRU`（紋章下に `Depuis 1890`）。

| 項目 | ✅ 公式（フィッシュ `Coeur-de-Cuvee-2017-FR.pdf`） |
|---|---|
| **セパージュ** | 🔴 **`80 % de Chardonnay et 20 % de Pinot Noir classés Premier Cru`** |
| **樹齢** | 🔴 **`vignes de Rilly-la-Montagne de soixante ans d'âge`**（60 年） |
| 🔴 **名の由来（スペックとして書かれている）** | 🔴 **`Élaboré uniquement avec le cœur de la cuvée (1400 l au lieu de 2050 l)`**<br>🔴 **すなわち「キュヴェの心臓部」とは、`2050 l` 取れるところを `1400 l` しか使わない、という具体的な数字である。** |
| **木** | 🔴 **`Vieillissement dix mois en pièces de chêne de 228 l`**（＝ブルゴーニュ小樽） |
| **瓶熟** | 🔴 **`Soixante-dix mois sur lies en cave après mise en bouteilles`**（70 か月＝5 年 10 か月） |
| **MLF** | 🔴 **`Sans fermentation malo-lactique`** |
| **ドザージュ** | 🔴 **`Dosage : 7 g/l`** |
| **蔵出し価格** | ✅ **`116,00 € TTC`（ボトル）。`Rupture de stock`（在庫切れ）** |

→ 🔴 **メニューの `'Coeur de Cuvée,' Premier Cru Brut / 2017 / $535` は、名称・格付・ミレジムのいずれも造り手の表示と一致する。**
→ 🔴 **`unresolved` の原因は、メニューでも造り手でもなく、canonical が 2016 しか持っていないことである。**
→ 🔴 **これは `V-*` 族（vintage 軸の破綻）ではない。単に行が無いだけの `vintage gap` である。**

---

### 🔴 3 行目 —— `Cœur de Cuvée 2016`。**intake が「解決済み」とした唯一の行が、公式で裏が取れない**

🔍 **intake の evidence**: `canonical に vintage 2016 実在（保有: 2016）`／`match_state: alias`／`confidence 0.9`。

🔴 ⚠️ **しかし公式側に 2016 の痕跡が無い。次の 4 つを実測した。**

| 照会 | 結果 |
|---|---|
| **`/nos-vins`・`vins-sitemap1.xml`** | ⚠️ **`Cœur de Cuvée` は `2017` のみ** |
| **WooCommerce product 全列挙（28 URL）** | ⚠️ **`Coeur de Cuvée 2013`（マグナム）と `Coeur de Cuvée 2017`（ボトル）のみ。2016 は無い** |
| **media library の PDF 全列挙（18 点）** | ⚠️ **2016 の Cœur de Cuvée フィッシュは無い** |
| **URL 推測（3 綴り × 5 年フォルダ＝15 パターン）** | ⚠️ **全て HTTP 404** |

→ 🔴 **これは「2016 が存在しない」の証明ではない。造り手のサイトは現行在庫しか載せない設計であり、
実際 2014・2015・2016 の Cœur de Cuvée はいずれも載っていない。**
→ 🔴 **記録すべき事実はこうである —— OBP 4 行のうち intake が唯一 `alias`（解決）とした行が、
本調査で唯一、造り手の一次資料で裏が取れなかった行である。**
→ ⚠️ **すなわち intake の `confidence 0.9` は canonical との一致度であって、実在の裏づけではない。** → §Canonical Conflict

⚠️ **したがって staff は「2016 は 80/20 で 7 g/l です」と言ってはならない。
2013 と 2017 が同一スペックであるという規則性は強いが、それは 2016 の値の証拠ではない。** → §Staff Notes ⚠️ ⑤

---

### 🔴 4 行目 —— `Les Blanches Voies`。**区画名がキュヴェ名として印字され、ミレジムが落ちている**

🔍 **intake の生データ**: `source_wine_raw = "'Les Blanches Voies,' Premier Cru Extra Brut"` /
`_parts.label = "Les Blanches Voies"` / `_parts.appellation_display = "Extra Brut"` /
`source_vintage_raw = null` → `normalized_vintage = "NV"` / `$1,040` / セクション `BLANC DE BLANCS`。

#### 🔴 ✅ 公式で確定したこと

1. 🔴 **`Les Blanches Voies` はリリー＝ラ・モンターニュの区画名である。**
   ✅ 体験ページ「`la parcelle mythique Les Blanches Voies à Rilly-la-Montagne`」。
   ✅ Blanc de Blancs のフィッシュ「`(parcelle des Blanches Voies)`」。
2. 🔴 **この区画名を持つ商品は 2 つあり、どちらもラベルで `キュヴェ名＋ミレジム` の下段に置かれる。**
   ✅ `BLANC DE BLANCS 2011` / `LES BLANCHES VOIES`。✅ `BLANC DE NOIRS 2017` / `LES BLANCHES VOIES`。
3. 🔴 **公式はこの 2 本を明示的に `cuvées millésimées` と呼ぶ。**
   ✅ 「`quatre cuvées millésimées`: Grand Cellier d'Or / Cœur de Cuvée / Blanc de Noirs « Les Blanches Voies » / Blanc de Blancs « Les Blanches Voies »」。
4. 🔴 **公式の現行 9 品目に、`Blanc de Blancs` の NV は存在しない。**
   ✅ NV は `Grande Réserve` / `Grand Cellier` / `Cuvée Rubis` の 3 本だけで、いずれもブラン・ド・ブランではない。

#### 🔴 したがって

→ 🔴 **OBP が `BLANC DE BLANCS` セクションに置いた `Les Blanches Voies` に対応する造り手側の商品は、
`Blanc de Blancs « Les Blanches Voies »`（現行 2013）である。他に候補が無い。**
→ 🔴 **そしてその商品は `millésimé` である。公式の現行レンジに NV のブラン・ド・ブランは 1 本も無い。**

#### ⚠️ **それでも本ドシエは「メニューが誤っている」と断定しない。**

**理由 ——**

⚠️ **① Batch 10 が確立した通り、`メニューが defective な側` とは限らない。反例が 3 件出ている。**
⚠️ **② 店が在庫しているのが `2013` とは限らない。より新しいミレジムがすでに出荷されている可能性がある
（公式 shop は現行在庫しか載せず、Blanc de Blancs 2013 は `Rupture de stock`）。**
⚠️ **③ `Extra Brut` の表示は造り手の資料に一度も現れない。**
🔴 **取得した公式 HTML 全ページ・全 12 フィッシュを対象に `extra brut` を検索した結果はゼロ件である。**
**フィッシュはドザージュを `g/l` の数値でしか書かない。Blanc de Blancs は `4 g/l` で、
EU 規則上 `Extra Brut`（0–6 g/l）の範囲に入るので `Extra Brut` と表示することは可能だが、
`実際にラベルにそう刷ってあるか` は、取得できたボトルショットの解像度では読み取れなかった。**
⚠️ **④ したがって「`Les Blanches Voies` という単独名のキュヴェを最近リリースした」可能性を、完全には排除できない。**
**$1,040 という価格は Cœur de Cuvée 2017（$535）の 2 倍近く、公式の蔵出し価格（Blanc de Blancs 220 €）と比べても高い。**

→ 🔴 **本行は `物理ラベル・タスク` に回す。店の在庫ボトルのラベルを撮り、
① キュヴェ名の段組、② ミレジムの有無、③ `Extra Brut` の有無、④ RM/NM コードの 4 点を読めば決着する。** → §Open Questions 1

---

## Staff Notes

### 🔴 芯 3 点（**これだけ言えれば卓上で嘘をつかない**）

🔴 **①「リリー＝ラ・モンターニュのプルミエ・クリュに 11 ヘクタール。1890 年創業、5 代目の Laurent Champs が当主兼 chef de cave です。」**
**—— 造り手の規模と主体を一言で言う。11 ha は「大メゾンではない」ことを含意する。
🔴 グラン・クリュではなくプルミエ・クリュであることは、INAO の法令テキストで確認済み。**

🔴 **②「シャンパーニュには珍しく、`全てのキュヴェ` を木樽で仕込みます。フードルとブルゴーニュ樽で 10 か月です。」**
**—— 公式が `la vinification de l'ensemble des cuvées se fait exclusivement sous bois` と書く、メゾンの第一の署名。
🔴 ただし「大樽（フードル）で」と限定してはならない。フードルは NV 用で、
`Cœur de Cuvée` と `Blanc de Blancs` は 228 リットルのブルゴーニュ小樽である。**

🔴 **③「マロラクティック発酵は一切かけません。それが Vilmart の張りと香りの典型性を作っています。」**
**—— 公式が第二の署名として名指しする。🔴 取得した 12 点のフィッシュ全てに `Sans fermentation malo-lactique` がある。
🔴 これは canonical の記述と正面から食い違う点であり、卓上で最も間違えやすい。**

### ⚠️ 言ってはいけないこと（**must-not-say**）

⚠️ **① 「ヴィルマール・ペール・エ・フィス」と混同して話す。**
🔴 **同じリリー＝ラ・モンターニュに `CHAMPAGNE VILMART PERE ET FILS`（16 rue Kellermann、SIREN 800821142）という
別の生産者が実在する。🏛 企業登録で確認済み。OBP の `Vilmart & Cie` は SIREN 308076744 の別法人である。**

⚠️ **② 「マロラクティックは部分的にかけています」／「一部 MLF」。**
🔴 **公式は全キュヴェで `Sans fermentation malo-lactique` と書き、
さらに `L'absence de fermentation malo-lactique est l'une des spécificités propres aux champagnes Vilmart`
（MLF の不在は Vilmart のシャンパーニュ固有の特質のひとつ）と、メゾンの定義として書いている。**
🔴 **canonical の `winemaking` はこれを反転させている。canonical をそのまま読み上げてはならない。**

⚠️ **③ 「オーガニックの造り手です」／「ビオディナミです」。**
🔴 **🏛 Agence Bio に SIRET 完全一致で照会して `nbTotal: 0`。企業登録も `est_bio: false`。**
🔴 **公式が名乗るのは `VDC`（Viticulture Durable en Champagne）と `HVE`（Haute Valeur Environnementale）の 2 つだけである。**
⚠️ **同時に「有機的なことは何もしていません」も言ってはならない。実践については公式が沈黙している。**

⚠️ **④ 「グラン・クリュです」。**
🔴 **🏛 AOC Champagne の cahier des charges は、`grand cru` を名乗れる 17 コミューンを列挙するが、
そこに `Rilly-la-Montagne` も `Villers-Allerand` も入っていない。両村は `premier cru` の列挙のほうにある。**
🔴 **造り手自身もラベルに `PREMIER CRU` と刷っている。**

⚠️ **⑤ 「2016 は 80/20、ドザージュ 7 g/l です」。**
🔴 **`Cœur de Cuvée 2016` のフィッシュは公式に存在しない。2013 と 2017 が同じ数値であることは確認したが、
2016 の数値は誰も公表していない。数字を言うなら 2017 についてだけ言う。**

⚠️ **⑥ 「`Les Blanches Voies` というキュヴェです」。**
🔴 **`Les Blanches Voies` は区画名であり、ラベル上は `BLANC DE BLANCS <年>` の下段の副題である。**
🔴 **正しくは「`Blanc de Blancs`、区画は `Les Blanches Voies`」。**
⚠️ **そしてこのワインは公式ではミレジメである。メニューが `NV` と刷っていても「ノンヴィンテージです」とは言わない。
年号はボトルで確認する。**

⚠️ **⑦ 「フードル（大樽）で熟成させた `Cœur de Cuvée` です」。**
🔴 **`Cœur de Cuvée` は `pièces de chêne de 228 l`。フードルは `Grande Réserve` / `Grand Cellier` / `Cuvée Rubis` である。**
🔴 **公式の体験メニューが `Grand Cellier — 「du foudre」` と `Cœur de Cuvée — 「d'un fût bourguignon」` を
わざわざ対比させている。造り手にとって重要な区別である。**

⚠️ **⑧ 「6 代目です」／「4 代目です」。**
⚠️ **公式メタ記述は `cinq générations`（5 代）。沿革が名指しするのは 6 名（Thomas Champs は 2020 年参画）。
断定を避け、「5 代にわたる家族経営で、いまは Laurent Champs さん、息子の Thomas さんも入っています」と言う。**

⚠️ **⑨ 「1890 年に Champs 家が創業しました」。**
✅ **創業者は `Désiré Vilmart`。Champs 姓は 1963 年、Renan Vilmart の `gendre`（娘婿）である
`René Champs` が引き継いだところから入る。🏛 企業登録の役員に `CHAMPS (VILMART) Nicole` が残っている。**

⚠️ **⑩ 「Vilmart はブルゴーニュの大樽でシャンパーニュを熟成させる唯一無二の造り手です」。**
🔴 **canonical の `obp_note` にこの文言があるが、公式はどこにもそう主張していない。
「唯一」を裏づける一次資料は存在しない。** → §Canonical Conflict

⚠️ **⑪ 「コート・デ・ブランに近い東向き斜面です」。**
🔴 **canonical の `terroir` にこの記述があるが、公式は斜面の向きも、コート・デ・ブランとの関係も一切書いていない。
リリー＝ラ・モンターニュはモンターニュ・ド・ランスの村であり、コート・デ・ブランではない。**

⚠️ **⑫ 「セパージュはシャルドネ 70 / ピノ・ノワール 30 です」（`Cœur de Cuvée` について）。**
🔴 **`70/30` は畑全体の植栽比率であり、かつ `Grand Cellier` のアッサンブラージュ比率である。**
🔴 **`Cœur de Cuvée` は `80/20`。canonical はこの 2 つを取り違えている。**

### 🔴 追加の一手（**客に訊かれたら強い**）

🔴 ✅ **「`Cœur de Cuvée` という名前は比喩ではありません。2050 リットル取れるところを 1400 リットルしか使わない、という意味です。」**
**—— 公式フィッシュが `Élaboré uniquement avec le cœur de la cuvée (1400 l au lieu de 2050 l)` と数字で書いている。**

🔴 ✅ **「シャルドネ 70 / ピノ・ノワール 30。シャンパーニュの伝統とは逆の植栽です、と造り手自身が言っています。」**
**—— 公式の `un encépagement singulier, à contre-courant de la tradition champenoise` の直訳。**

✅ **「澱下げは重力だけで行います。圧搾機も伝統的なもので、房は手摘みのまま無傷で運ばれます。」**
**—— `Le débourbage se fait par gravité` / `pressoir traditionnel` / `conserver intacts les grains jusqu'au pressoir`。**

✅ **「白亜のカーヴで、ノンヴィンテージは 3〜4 年、ミレジメは 5〜8 年寝かせます。」**
**—— 公式の明示的な一般則。`Cœur de Cuvée 2017` は実測で 70 か月＝5 年 10 か月で、この幅に収まる。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **本節は escalation のみ。`REGISTER.md` は書き換えていない。番号の採否は CTO の判断である。**

### 🔍 canonical の実測（`migration/out/export/db_wine_canonical.json`、928 要素）

| 走査 | 結果 |
|---|---|
| **`vilmart` を含むレコード（全文字列）** | 🔍 **1 件** |
| 🔴 **`producer` フィールドが `Vilmart & Cie` のレコード** | 🔴 **1 件（`vilmart-coeur-de-cuvee-2016`）** |
| 🔴 **prose のみで `vilmart` に当たるレコード** | 🔴 **0 件** |

→ 🔴 **`D-2026-08-05-08`（部分文字列一致による誤検出）は本件では発生していない。1 件は本物である。**

### 🔴 ① canonical gap（**3 行分。conflict ではない**）

🔴 **`D-2026-08-05` の方針どおり、`不在` は conflict ではなく gap として記録する。番号は開かない。**

| OBP 行 | 状態 | 判定 |
|---|---|---|
| **`Grand Cellier`（NV）** | 🔴 **canonical にキュヴェ行が無い** | 🔴 **gap。公式に実在し、ラベルにもその名が刷られている。`unreachable`（別綴りで存在する）ではない —— canonical の当該生産者のレコードは 1 件しかなく、その 1 件は `Coeur de Cuvée` である** |
| **`Cœur de Cuvée 2017`** | 🔴 **cuvée はある。vintage 行が無い** | 🔴 **vintage gap。`V-1` 族（édition が層をまたぐ）とは異なる。層の設計ではなく、単に 1 行足りない** |
| **`Les Blanches Voies` → `Blanc de Blancs`** | 🔴 **canonical にキュヴェ行が無い** | 🔴 **gap。ただし「何を作るべきか」は物理ラベル待ち（下記 ④）** |

🔴 **`unreachable` の可能性は潰した。** canonical 全 928 件を `vilmart` で走査した結果が 1 件であり、
別綴り（`Vilmart et Cie` / `Champagne Vilmart` / `Vilmart & Compagnie`）で潜んでいるレコードは存在しない。
**Batch 10 が Roederer で踏みかけた「重複を作ってしまう」経路は、本件では閉じている。**

### 🔴 ② canonical の格納値と造り手の食い違い（**未採番の形。Batch 8–10 と同一族**）

🔴 **`vilmart-coeur-de-cuvee-2016` の 1 レコードを、公式フィッシュ（2013 / 2017 の 2 版）と 1 フィールドずつ突き合わせた。**

| フィールド | canonical の値 | ✅ 造り手の値 | 判定 |
|---|---|---|---|
| 🔴 **`grapes`** | **`["Chardonnay 70%", "Pinot Noir 30%"]`** | 🔴 **`80 % de Chardonnay et 20 % de Pinot Noir`**（2013 版・2017 版で一致） | 🔴 **矛盾。しかも `70/30` は畑全体の植栽比率であり、同時に `Grand Cellier` の比率でもある。他キュヴェの値の混入と読める** |
| 🔴 **`dosage`** | **`"Brut — 5 g/L"`** | 🔴 **`Dosage : 7 g/l`**（2013 版・2017 版で一致） | 🔴 **矛盾。⚠️ ただし 2016 版フィッシュは非公表なので、2016 の実値そのものは誰も知らない** |
| 🔴 **`aging`** | **`"6+ years sur lie; large Burgundy barrel primary aging"`** | 🔴 **`dix mois en pièces de chêne de 228 l` ＋ `Soixante-dix mois sur lies`**（＝10 か月木樽＋70 か月＝5 年 10 か月） | 🔴 **二重の矛盾。① `228 l` は `large` ではなく標準的なブルゴーニュ小樽。② `70 か月` は `6+ years` に達しない** |
| 🔴 **`winemaking` / `winemaking_en`** | 🔴 **`"100%大樽（フードル）発酵・熟成"` ／ `"Partial MLF"`（`マロラクティック発酵あり（一部）`）** | 🔴 **`pièces de chêne de 228 l` ／ `Sans fermentation malo-lactique`** | 🔴 🔴 **本ドシエ最大の矛盾。フードルは別キュヴェの容器であり、MLF は公式が「行わないことがメゾンの特質」と明言している。canonical は造り手の署名を反転させている** |
| 🔴 **`obp_note` / `obp_note_en`** | **`「ヴィルマールはブルゴーニュの大樽でシャンパーニュを熟成させる唯一無二の造り手」`／`6年以上の熟成`** | 🔴 **公式にこの主張は無い。`唯一無二`（unique in Champagne）を裏づける一次資料は存在しない。熟成は 70 か月** | 🔴 **矛盾＋出典なき最上級。カギ括弧つきの「ソムリエの声」形式で書かれている点が、卓上で読み上げられる危険を高める** |
| 🔴 **`description` / `description_en`** | **`「ブルゴーニュの大樽（フードル）で長期熟成させる独自のスタイル」`** | 🔴 **`Cœur de Cuvée` は 228 l。フードルは NV 用** | 🔴 **矛盾（`aging` と同じ誤り）** |
| 🔴 **`terroir` / `terroir_en`** | **`「コート・デ・ブランに近い東斜面」`／`East-facing slopes close to the Côte des Blancs character`** | 🔴 **公式は斜面の向きを一切書かない。コート・デ・ブランへの言及も無い。リリー＝ラ・モンターニュはモンターニュ・ド・ランスの村である** | 🔴 **出典なき創作。公式の沈黙を埋めている** |
| ⚠️ **`aging`（村の網羅）** | **`subregion: "Rilly-la-Montagne Premier Cru — Montagne de Reims"`** | ✅ **正しい。**⚠️ **ただし畑は `Villers-Allerand` にもある** | ✅ ⚠️ **唯一 canonical が正しかった typed field。ただし不完全** |
| ✅ **`classification`** | **`"Premier Cru Brut"`** | ✅ **`PREMIER CRU` はラベルに実在**／⚠️ **`Brut` は表ラベルに無い** | ✅ ⚠️ **概ね正しい** |
| ⚠️ **`points: 96`** | **96 点** | ⚠️ **公式サイトは点数を一切掲載していない。出典不明** | ⚠️ **出典なき評点** |
| — | **`founded_year`** | — | ✅ **このレコードに `founded_year` フィールドは存在しない。したがって創業年の矛盾は無い**（公式は 1890 年） |

→ 🔴 **これで Batch 8–10 の観測は 11 軒目でも再現した。**
**「canonical の格納値が typed field を含めて造り手と矛盾する」という形は、依然として未採番である。**
🔴 **本件は base rate をさらに強くする例であると同時に、`他キュヴェの値の混入` という新しい下位形を示している ——
`grapes 70/30`・`フードル` は、いずれも同じ生産者の `Grand Cellier` の正しい値である。
すなわち誤りはランダムではなく、`生産者内の別キュヴェからの取り違え` である。**

### 🔴 ③ 未採番の形 —— **「ラベルの副題（区画名）がキュヴェ名として印字される」**

🔴 **OBP 4 行目 `'Les Blanches Voies,' Premier Cru Extra Brut` は、
ラベルの 2 段目（`BLANC DE BLANCS <年>`）ではなく 3 段目（`LES BLANCHES VOIES`）を拾っている。**

⚠️ **これは `C-4`（識別語を持たないキュヴェ名）とも、Batch 10 の「category word をキュヴェ名として印字する」形
（Grgich `'Estate,'` / Mayacamas `Red Wine` / Harlan `Proprietary Blend` / Abreu `Cabernet Sauvignon`）とも異なる。**
**それらは `一般名詞を固有名として拾う` 形だが、本件は `固有名（区画名）を、より上位の固有名（キュヴェ名）の代わりに拾う` 形である。**
**しかも拾われた語は実在し、かつ造り手のラベルに実際に刷られている。**

🔴 **本ドシエは番号を開かない。形として記述するにとどめる。**
⚠️ **`CAT-4`（naming_convention）に分類しうるが、それは CTO の判断である。**

⚠️ **なお Batch 10 の警告に従い、`メニューが defective` とは断定しない。**
🔴 **決着させられるのは物理ラベルだけである。**

### 🔴 ④ intake の `resolved` が実在の裏づけではない件

🔴 **OBP 4 行のうち、intake が `alias`（confidence 0.9、解決済み）としたのは 3 行目（2016）だけである。**
🔴 **そして本調査で造り手の一次資料に当たらなかった唯一の行が、その 3 行目である。**
🔴 **逆に、intake が `unresolved` とした 1・2 行目は、公式サイトとラベルの両方で完全に裏が取れた。**

→ 🔴 **すなわち `match_state` は「canonical と一致するか」を測っており、「造り手の世界に実在するか」は測っていない。**
→ ⚠️ **`D-2026-08-05` の「intake と `research/out/t-01/mapping.json` が resolved の定義で食い違う」問題とは別の軸である。**
**本件で引用した `match_state` は、すべて `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json` 由来である。**

### ⚠️ ⑤ 公式サイト内部の不一致（**canonical とは無関係。造り手側の問題**）

| 項目 | フィッシュ・テクニック | 商品ページ |
|---|---|---|
| 🔴 **Blanc de Blancs 2013 の生産本数** | 🔴 **`Quantité limitée à 3600 bouteilles numérotées`** | 🔴 **`Quantité limitée à 2 900 bouteilles numérotées`** |
| ⚠️ **Blanc de Blancs 2013 の色** | **`jaune citron lumineuse aux reflets argentés`**（明るいレモンイエロー・銀の照り） | **`jaune paille avec de légers reflets verts pâles`**（麦わら色・淡い緑の照り） |

→ ⚠️ **どちらも公式である。`A producer can contradict itself` の実例として両論を保存する。どちらかを選ばない。**
🔴 **`3600` と `2900` は、Blanc de Noirs 2017 の `Production : 2 900 bouteilles` と一致する後者が
「別キュヴェの値の貼り間違い」である可能性を示唆するが、断定はしない。** → Open Questions 11

---

## Sources

### 🔴 ⚠️ サイト真正性の事前チェック（`D-2026-08-05-09`）—— **1 件却下、1 件合格**

| ドメイン | 判定 | 根拠 |
|---|---|---|
| 🔴 ❌ **`vilmart.fr` / `www.vilmart.fr`** | 🔴 **却下（look-alike / パーキング）** | 🔴 **HTTP 200 で返る本文が `Dovendi - Domain for sale` / `This domain name is managed by Dovendi` / `Dovendi brings buyers and sellers together. We manage over 250,000 international domain names`。CSP も `dovendi.b-cdn.net` を許可している。**<br>🔴 **これで捕捉した偽サイトは通算 6 件目（`comtes-lafon.com` / `ramonet.fr` / `caroline-morey.com` / `pierregirardin.com` / `themascotwine.com` に続く）。**<br>🔴 **本ドシエは本ドメインの内容を 1 語も使用していない。** |
| ✅ **`www.champagnevilmart.fr`** | ✅ **合格（(a) と (d) の 2 条件を同時に満たす）** | ✅ **(a) `mentions légales` が発行者を `SA CHAMPAGNE VILMART ET CIE / RCS : Reims B 308 076 744 / TVA FR 82 308076744 / Directeur de publication : M. Laurent CHAMPS, Président Directeur Général` と明記。**<br>🏛 **(d) 🏛 企業登録の SIREN `308076744`・TVA `FR82308076744`・代表 `CHAMPS Laurent Christophe（PDG）` と完全一致。**<br>✅ **加えて全 12 点のフィッシュ・テクニックのフッターが `Champagne Vilmart & Cie \| 5, rue des gravières \| 51500 Rilly-la-Montagne \| http://www.champagnevilmart.fr` を自称している（自己参照の閉じ）。**<br>✅ **免責・非提携の記載は無い。** |

⚠️ **アルコールの年齢確認ゲートは本サイトには無かった。bot チャレンジも遭遇していない（回避行為なし）。**

### ✅ 公式サイト（`https://www.champagnevilmart.fr/`、FR 原本）

- ✅ `robots.txt` → `sitemap.xml` → `page-sitemap1.xml`（34 URL）／`vins-sitemap1.xml`（18 URL）
- ✅ `/notre-histoire`（沿革・畑の数値・醸造の一般則・当主）
- ✅ `/faconner-philosophie-et-elaboration`（哲学・収穫・débourbage・木樽・MLF・熟成年数）
- ✅ `/nos-vins`（現行 9 品目の完全な列挙）
- ✅ `/mentions-legales`（法人・住所・掲載責任者・制作者）
- ✅ `/vins/…` 9 ページ（FR）＋ `/en/vins/…`（英仏の数値一致を確認。**採用したのは FR のみ**）
- ✅ `/lexperience-les-blanches-voies-_-test-hugo`（🔴 **区画 `Les Blanches Voies` と 4 本のミレジメ**）
- ✅ `/experience-les-secrets-du-bois-_-test-hugo`（🔴 **foudre と fût bourguignon の対比**）
- ✅ `/les-experiences-vilmart-cie-2`（訪問メニュー）
- ✅ `wp-json/wp/v2/search`（product 全 28 URL の列挙）／`wp-json/wp/v2/media`（PDF 全 18 点の列挙）
- ✅ 商品ページ: `produit/fr-blanc-de-blancs-2013` / `produit/fr-coeur-de-cuvee-2017-bouteille` / `produit/fr-coeur-de-cuvee-2013-magnum` / `produit/fr-grand-cellier` / `produit/blanc-de-noirs-2017`

### ✅ 公式フィッシュ・テクニック（**全点 `%PDF` 実体を確認済み。HTML が返る偽 PDF は無し**）

| ファイル | 対象 |
|---|---|
| ✅ `Coeur-de-Cuvee-2017-FR.pdf` | 🔴 **OBP 2 行目** |
| ✅ `Grand-Cellier-FR-T23.pdf` | 🔴 **OBP 1 行目（現行版）** |
| ✅ `Grand-Cellier-FR-3-2020.pdf` / `Grand-Cellier-EN-3-2020.pdf` | 🔴 **OBP 1 行目（2020 年版。改称の有無を検証するため）** |
| ✅ `Blanc-de-Blancs-2013-FR-1.pdf` | 🔴 **OBP 4 行目の対応候補** |
| ✅ `Blanc-de-Noirs-2017-FR.pdf` | **同じ区画のもう 1 本** |
| ✅ `Grand-Cellier-dOr-2021-FR.pdf` / `Grand-Cellier-dOr-2015-FR-2020.pdf` | **容器の使い分けの検証** |
| ✅ `Grande-Reserve-FR-T23.pdf` / `Cuvee-Rubis-FR-T24-1.pdf` / `Cuvee-Rubis-EN-T19.pdf` | **NV レンジ／`Grand Cellier Rubis` 旧称説の検証** |
| ✅ `Emotion-2016-FR.pdf` / `Ratafia-Chardonnay-FR.pdf` | **レンジの網羅** |

### ✅ 公式ボトルショット（**producer's own domain 由来。ラベル面を実読**）

- ✅ `/wp-content/uploads/2020/01/grand-cellier.png` → 🔴 **`GRAND CELLIER / PREMIER CRU / à Rilly la Montagne / Depuis 1890`**
- ✅ `/wp-content/uploads/2020/01/coeur-cuvee17tran-1-1920x3520.png` → 🔴 **`CŒUR DE CUVÉE / 2017 / PREMIER CRU`**
- ✅ `/wp-content/uploads/2020/01/blanc-de-blanc-2011-web.png` → 🔴 **`BLANC DE BLANCS 2011 / LES BLANCHES VOIES`**
- ✅ `/wp-content/uploads/2026/05/bn-2017.png` → 🔴 **`BLANC DE NOIRS 2017 / LES BLANCHES VOIES`**
- ✅ `/wp-content/uploads/2018/09/2t8a2764.jpg` → **`GRAND CELLIER D'Or 2021 / PREMIER CRU / à Rilly la Montagne`**

### 🏛 公的登録・規制一次資料

| 出典 | 取得内容 |
|---|---|
| 🏛 **`recherche-entreprises.api.gouv.fr/search?q=CHAMPAGNE%20VILMART%20ET%20COMPAGNIE`** | **SIREN 308076744、SIRET 30807674400017、NAF 01.21Z、SA、役員 4 名、TVA、`est_bio: false`** |
| 🏛 **同 `?q=VILMART&code_postal=51500`** | 🔴 **同村の Vilmart 系 10 法人。`CHAMPAGNE VILMART PERE ET FILS` が別法人であることの確認** |
| 🏛 **`opendata.agencebio.org/api/gouv/operateurs/?siret=30807674400017`** | 🔴 **`{"nbTotal":0,"items":[]}` —— 有効な陰性** |
| 🏛 **同 `?q=VILMART&departement=Marne`** | **`VILMART Maxime`（フィニステール県、無関係）1 件のみ** |
| 🏛 **`extranet.inao.gouv.fr/fichier/PNOCDCChampagne.pdf`** | 🔴 **AOC Champagne CDC。`premier cru` 列挙に `Rilly-la-Montagne`・`Villers-Allerand`、`grand cru` 列挙（17 村）に両村とも不在** |
| 🏛 **`extranet.inao.gouv.fr/fichier/3-CDC-Champagne-PNO.pdf`** | 🔴 **同上の別版。同一の列挙を確認（2 版で相互検証）** |

### 🔍 THÉSEUS 内部

- 🔍 `~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`（704 行中 `Vilmart` 4 行）
- 🔍 `migration/out/export/db_wine_canonical.json`（928 要素。**読み取りのみ。ハッシュ不変を検証済み**）

### ❌ 却下した出典

- 🔴 **`vilmart.fr` — Dovendi のドメイン売却ページ。`NOT_THE_PRODUCER_vilmart-fr-dovendi-parking` としてキャッシュ。内容不使用。**
- **Wikipedia・小売・オークション・評論家サイト・輸入元資料・Vivino・CellarTracker・Wine-Searcher は一切使用していない。**

**キャッシュ先**: `research/producers/_sources/vilmart-et-cie/`（gitignored）

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| 🔴 **Identity** | 🔴 **High** | 🔴 **社名・法人格・RCS・TVA・掲載責任者が mentions légales で確定し、🏛 企業登録の SIREN・役員と完全一致。当主名も 2 系統一致。同村の同名別法人 2 系統まで特定した。**⚠️ **住所が公式と登録で別街路（記録済み）／世代数が揺れる** |
| **Overview** | **High** | **11 ha・70/30・全キュヴェ木樽・MLF 無しという自己規定が、すべて一次で取れた** |
| ⚠️ **History** | ⚠️ **Medium** | ✅ **1890 / 1939–45 / 1963 / 1995 / 2020 の 5 点は公式で確定し、創業者名と継承の型（gendre）も取れた。**⚠️ **しかし公式沿革は 5 項目しかなく、キュヴェの創出年・区画の植栽年・échelle への編入がすべて不在** |
| 🔴 **Location** | 🔴 **High** | 🔴 **11 ha・2 村・70/30・樹齢（平均 40 / 最古 65）が公式。**🔴 **プルミエ・クリュであることを 🏛 INAO の法令テキスト 2 版で確認。**🔴 **区画 `Les Blanches Voies` の位置づけを公式 3 か所（体験ページ・フィッシュ・実ラベル）で確定。**⚠️ **面積内訳・土壌・向きは不在** |
| 🔴 **Farming** | 🔴 **Medium-High** | ✅ **VDC / HVE の保有が全 12 フィッシュで確定。収穫・圧搾・débourbage の実務も一次。**🔴 **有機の不在を 🏛 Agence Bio の SIRET 完全一致クエリで有効に証明した。**⚠️ **取得年・HVE レベル・防除の実務が公式に不在で、そこが埋まらない** |
| 🔴 **Winemaking** | 🔴 **High** | 🔴 **OBP 全 4 行を含む 10 キュヴェについて、セパージュ・容器・容量・瓶熟月数・MLF・ドザージュを公式フィッシュから機械転記。**🔴 **foudre と 228 l の使い分けを、公式の体験メニューという独立の証拠で裏づけた。**⚠️ **アルコール度数・デゴルジュマン・新樽比率・生産本数の大半が不在** |
| **Style** | **Medium-High** | ✅ **OBP 関連 3 本＋主要 NV の公式ノートを全文取得。**⚠️ **公式は点数も受賞も掲載しておらず、第三者の言葉は Galloni の一文のみ** |
| 🔴 **Important Cuvées** | 🔴 **High** | 🔴 **公式の現行 9 品目を 3 系統（`/nos-vins`・sitemap・WooCommerce 全列挙）で相互検証。**🔴 **4 行中 3 行を実ラベルまで確定。**🔴 **4 行目の `Les Blanches Voies` が区画名であることを実ラベルで確定した。**⚠️ **2016 と `Extra Brut` の 2 点だけが未決着で、いずれも物理ラベル待ち** |
| 🔴 **Canonical Conflict** | 🔴 **High** | 🔴 **canonical 1 件の全フィールドを公式と 1 行ずつ突き合わせ、7 フィールドの矛盾と 1 件の正解を確定。**🔴 **`unreachable` の可能性を 928 件走査で潰し、gap と断定できる状態にした。**🔴 **「別キュヴェからの値の取り違え」という下位形を、`70/30` と `フードル` の 2 例で示した** |
| **Staff Notes** | 🔴 **High** | ⚠️ **芯 3 点＋ must-not-say 12 項目。🔴 canonical をそのまま読むと出る 5 つの嘘（部分 MLF / フードル / 70:30 / 唯一無二 / コート・デ・ブラン東斜面）と、現場で出やすい 7 つの嘘を塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を超過。実感としては 85% 前後）。** | **OBP 4 行のうち 3 行について、造り手の正式名・格付・セパージュ・容器・熟成月数・ドザージュ・公式ノート・実ラベルの文字列をそのまま言える。栽培は認証名を言え、有機については断定的に「持っていない」と言える。**<br>**欠けているのは ① `Cœur de Cuvée 2016` の一次資料、② `Les Blanches Voies` の現行ミレジムと `Extra Brut` 表示、③ 醸造の分析値（度数・デゴルジュマン）、④ 認証の取得年。**<br>**①②は物理ラベルで決着し、③④は「言わない」で回避できる。卓上で嘘をつく経路は塞いである。** |

**reached_70: YES (~85%)。**

---

## Open Questions

1. 🔴 **【物理ラベル・タスク】OBP 4 行目 `'Les Blanches Voies,' Premier Cru Extra Brut / NV / $1,040` の実ボトル。**
   **確認すべきは 4 点 —— ① キュヴェ名の段組（`BLANC DE BLANCS <年>` が上段にあるか）、
   ② ミレジムの有無と年号、③ `Extra Brut` が刷られているか、④ RM/NM の matriculation コード。**
   🔴 **オンラインの一次資料はここまでしか到達できない。公式は `Extra Brut` の語を一度も使わず、
   ドザージュを `g/l` の数値でしか書かない。**
2. 🔴 **`Cœur de Cuvée 2016` は実在するか。**
   **公式サイトは 2013（マグナム）と 2017（ボトル）しか載せず、media library にも 2016 のフィッシュが無い。
   URL 推測 15 パターンは全 404。🔴 これは陰性の証明ではない。造り手に直接 2016 のフィッシュを請求するのが最短。**
   **（OBP は 2016 を $440 で現に売っているので、店に実ボトルがある可能性が高い。物理ラベル・タスクに合流しうる。）**
3. **`Cœur de Cuvée` と `Grand Cellier` の初ミレジム／創出年。公式沿革は 5 項目しかなく、キュヴェの誕生年を一切書いていない。**
4. 🔴 **このメゾンは `récoltant-manipulant (RM)` か。**
   **公式サイトにも取得したラベル面にも matriculation コードが無い。**
   ⚠️ **11 ha の自社畑のみという記述は RM と整合するが、`Champagne Vilmart & Cie` という商号と SA という法人格、
   および NAF `01.21Z`（栽培）だけでは決まらない。実ラベルの背面か CIVC の照会が要る。**
5. ⚠️ **公式の `5, rue des Gravières`（BP 4）と 🏛 登録本店の `4 rue de la République` の関係。**
   **同一 SIRET・同一コミューンだが別街路。醸造所と登記上の本店が分かれているのか、登録が古いのかが不明。**
6. **栽培の実務（除草・防除・被覆作物・馬耕・カーボン）。VDC / HVE の名前は分かるが、その中身を公式が一切書いていない。**
   **HVE のレベル（1/2/3）と、VDC / HVE の取得年も不明。**
7. **木樽の詳細 —— 新樽比率、樽材の産地、tonnelier 名、樽の更新サイクル、foudre の容量と基数。**
   🔴 **公式は `foudres` と `fûts de chêne` の語と、`228 l` / `10 HL` / `400・600 l` という容量しか書かない。**
8. **公式が第三者評価を一切掲載していない理由。点数・受賞・格付けがサイト上に無い（Galloni の一文のみ）。**
   ⚠️ **これは事実の記録であって、評価が無いという意味ではない。**
9. ⚠️ **`Cuvée Rubis` はかつて `Grand Cellier Rubis` と呼ばれていたか。**
   **取得できた最古の公式フィッシュ（2019 年基準）の見出しはすでに `CUVÉE RUBIS`。それ以前の公式資料に到達できていない。**
10. ⚠️ **NV レンジのラベルに `Brut` の語が刷られているか。**
    **取得した `Grand Cellier` のラベル面には無い。ドザージュ 8 g/l は `Brut` の範囲だが、表示の有無は別問題。**
11. ⚠️ **`Blanc de Blancs 2013` の生産本数は `3600` か `2900` か。**
    **公式フィッシュと公式商品ページが食い違う。`2900` は `Blanc de Noirs 2017` の生産本数と一致するため、
    貼り間違いの疑いがあるが、断定はしない。造り手に確認が要る。**
12. ⚠️ **世代数。公式メタ記述は `cinq générations`、沿革が名指しするのは 6 名。どこから数えるかが公式で明示されていない。**
