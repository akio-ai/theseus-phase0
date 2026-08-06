# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔍 **canonical にこの生産者のレコードは 3 件存在する**
> （`giraud-fut-de-chene` / `henri-giraud-esprit-nature` / `henri-giraud-argonne-2016`）。
> **3 件はすべて `producer` フィールドでの一致であり、他生産者の散文に名前が現れただけの prose-only hit は 0 件。**
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **現在稼働中の生産者自身のドメインで確認**（`champagne-giraud.com` ／ `manoir-henri-giraud.com`）
> `📄` 🔴 **生産者自身が書いた頁だが、現在は生産者のドメインから配信されていない**
>    （**Internet Archive に残る `champagne-giraud.com` の旧版。生産者自身の HTML・生産者自身の mentions légales・
>    生産者自身のフィッシュ PDF であることを本文中で毎回確認している**）
> `🏛` **公的登録**（recherche-entreprises.api.gouv.fr / Agence Bio / INAO cahier des charges / WHOIS / DNS）
> `⚠️` **出典間で食い違っている／出典が沈黙している／第三者の未検証情報**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://champagne-giraud.com/`（FR 原本）**
> 走査元: **`robots.txt` が `Sitemap: https://champagne-giraud.com/wp-sitemap.xml` を明示 → 取得できた頁は 8 件のみ**
>
> ---
>
> 🔴 **本ドシエ最大の収穫 —— この生産者は「現在、何も公表していない」。それ自体が最重要の事実である。**
>
> **① 公式サイト `champagne-giraud.com` は、現在キュヴェの情報を 1 文字も載せていない。**
> ✅ **`wp-sitemap` が返す公開頁は `accueil` / `contact` / `fiche-client` / `fiche-client-avec-liste` /
> `mentions-legales` / `legal-notices` / `politique-de-confidentialite` / `privacy-policy` の 8 件だけ。**
> ✅ **WP REST API（`/wp-json/wp/v2/pages`）が返す固定頁も同じ 8 件。**
> ✅ **メディアライブラリ 65 件のうち PDF は 4 件で、いずれも 2025 年のイベント進行表であり、フィッシュ・テクニックは 1 件も無い。**
> ✅ **`mentions-legales` は自ら「本サイトは電子商取引プラットフォームではない」と書く。**
> → 🔴 **すなわち「造り手の公式スペック」は現時点で存在しない。**
> **本ドシエのキュヴェ記述は、すべて `📄`（Internet Archive に残る生産者自身の旧頁）に依拠している。**
>
> **② 🔴 OBP 2 行目（`Grand Cru Brut` / NV / $800）を 1 本に絞ることはできなかった。候補は 3 本まで絞れた。**
> 📄 **公式の「Expériences Champagne」頁（2022-01-21 版）が、レンジ全 8 本を自ら列挙している ——**
> **`Esprit Nature | MV | MV Rosé | Hommage | Blanc de Craie | Dame-Jane | ArG̈onne | ArG̈onne Rosé`。**
> **このうち NV の白は `MV` / `Hommage` / `Blanc de Craie` の 3 本（`Esprit Nature` は 1 行目で確定済み）。**
> 🔴 **`Fût de Chêne MV17` は最有力仮説だが、公式は価格を一切公表していないため、$800 では確定できない。**
> **名前は書かない。** → §Important Cuvées 2 行目
>
> **③ 🔴 `MV` の意味は公式が自分で書いている —— `MV, comme Multi Vintage.`**
> 📄 **「`MV, comme Multi Vintage.` …小収量・小容器・原産品種という 3 本の柱に立つ、
> `la cuvée Fût de Chêne` は 1990 年以来シャンパーニュに消えない痕跡を残している。…
> `Colonne vertébrale de notre collection`（われわれのコレクションの背骨）、それが MV である。」**
> → 🔴 **`Fût de Chêne` と `MV` は別のキュヴェではない。MV は Fût de Chêne の現行呼称であり、
> `MV13` `MV17` の数字は「ベースとなる年」であって millésime ではない。**
> → 🔴 **これは Krug `Édition` と完全に同型であり、`V-1` 族に直接該当する。** → §Canonical Conflict
>
> **④ 🔴 OBP 4 行目（ROSÉ セクション）は canonical の「色の軸の gap」である。conflict ではない。**
> 📄 **公式レンジのロゼは `MV Rosé` / `ArG̈onne Rosé` / `Dame-Jane` の 3 本。実在する。**
> 🔍 **一方 canonical の 3 レコードは `color` がすべて `Blanc`。ロゼのレコードは綴り違いも含めて 1 件も無い。**
> → 🔴 **「レコードが存在するが綴りが違って当たらない（unreachable）」のではなく、**
> **「レコード自体が存在しない（gap）」。** → §Canonical Conflict
> 🔴 **かつ Batch 10 の実測どおり、matcher はメニューのセクション見出し `… | ROSÉ` を読んでいない。**
> **intake の evidence が `'rose'` を照合キーにしているのは `_parts.appellation` を拾ったからであって、
> セクションを読んだからではない。**
>
> ⚠️ **調査上の制約**
> **① 公式が最後に内容を持っていたのは 2023 年頃であり、`Argonne 2016` と「2022 年のロゼ」を裏づける
>    公式資料は、稼働中サイトにも Internet Archive にも 1 件も存在しない。**
> **② 本ドシエはドザージュの g/L 値・セパージュ比率（OBP 4 本について）・自社畑面積・年産本数を一切書かない。
>    公式が公表していないためである。** → §Staff Notes ⚠️

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Henri Giraud** |
| **公式表記** | ✅ **`Champagne Henri Giraud`**（mentions légales・トップ頁のコンタクト欄）／📄 **`Champagne Henri Giraud`**（旧サイト全頁のフッター） |
| 🔴 **法人（公式）** | ✅ **`SA Champagne Henri Giraud`、Société Anonyme。**<br>**資本金 `349 725 €`／`SIREN : 303891048`／`RCS ou RM : Reims B 303891048`／TVA `FR32303891048`**（mentions légales） |
| 🔴 **法人（🏛 公的登録）** | 🏛 **SIREN `303891048`／`nom_complet: CHAMPAGNE HENRI GIRAUD`／`nom_commercial: null`**<br>🏛 **SIRET 本店 `30389104800017`／NAF `01.21Z`（ブドウ栽培）／`date_creation: 1975-01-01`／`etat_administratif: A`／`nature_juridique: 5599`（SA à conseil d'administration）** |
| 🔴 **第 2 事業所** | 🏛 **SIRET `30389104800025`／`83 BD CHARLES DE GAULLE 51150 AY-CHAMPAGNE`／NAF `55.10Z`（宿泊業）／`date_creation: 2020-12-19`**<br>→ ✅ **これが `Manoir Henri Giraud`（`www.manoir-henri-giraud.com`）である。同一 SIREN の別事業所であり、別法人ではない。** |
| **住所（公式）** | ✅ **`71 boulevard Charles De Gaulle – 51160 Aÿ-Champagne – FRANCE`**（mentions légales） |
| **住所（🏛 登録）** | 🏛 **`71 BD CHARLES DE GAULLE 51150 AY-CHAMPAGNE`**／`code_commune 51030`／`lat 49.0532, long 3.9997` |
| ⚠️ **郵便番号の揺れ** | ⚠️ 🔴 **`51160`（公式 mentions légales・Agence Bio・旧サイト・2010 年のフィッシュ）と `51150`（企業登録）で食い違う。**<br>**同一の `code_commune 51030` を指すため同一施設と判断したが、どちらが現行かは確定していない。**<br>🔴 **Billecart-Salmon で観測されたのと同じ揺れが、同じコミューンで再現している。** |
| **電話 / メール** | ✅ **`+33 (0)3 26 55 18 55`**（公式トップ／mentions légales）<br>🏛 **`slegolvet@champagne-giraud.com`**（Agence Bio 登録上の連絡先）<br>📄 **`contact@champagne-giraud.com`**（2010 年のフィッシュ・テクニック） |
| **サイト掲載責任者** | ✅ **`Directeur de la publication : Emmanuelle Giraud-Patour, Présidente du Champagne Henri Giraud`** |
| **ホスティング** | ✅ **O2Switch（222 Boulevard Gustave Flaubert, 63000 Clermont-Ferrand）**<br>⚠️ 📄 **旧サイトの制作・ホスティングは `Agence Boomerang`（2 Rue Anatole France, 51530 Magenta）。現サイトの WP 投稿者にも `agence-boomerang` が残る。** |
| 🔴 **会長** | 🏛 ✅ **`Emmanuelle GIRAUD PATOUR`（旧姓 GIRAUD、1976 年 3 月生）、`Président du conseil d'administration`。**<br>**公式 mentions légales の `Présidente` と公的登録が一致する。** |
| 🔴 **社長 / 醸造長** | 🏛 **`Sébastien LE GOLVET`（1973 年 8 月生）、`Directeur Général`。**<br>📄 **旧公式 Argonne 頁: 「`Sébastien Le Golvet` は今日、繊細なワインと新しい樫樽とのこの生きた関係を統御する、おそらく唯一の `Chef de Cave` である。」**<br>→ 🔴 **「社長」と「醸造長」を同一人物が兼ねる。公的登録が前者を、公式が後者を裏づける。** |
| **その他役員** | 🏛 **`Anne LE GOLVET`（旧姓 GIRAUD、1978 年 6 月生）`Administrateur`／`Edith Marie HILBERT`（旧姓 EGROT、1959 年生）`Administrateur`** |
| ⚠️ 🔴 **Claude Giraud** | ⚠️ 🔴 **`Claude Giraud` は 🏛 現在の `dirigeants` 一覧に含まれていない。**<br>📄 **旧公式は `Claude Giraud, his president` として 2017 年の「No pesticide」表明の主体に据えている。**<br>→ 🔴 **canonical `henri-giraud-esprit-nature` の「当主クロード・ジローは 12 代目」は、少なくとも**<br>**現時点の法人代表としては公的登録と一致しない。** → §Canonical Conflict |
| ⚠️ 🔴 **創業年** | ⚠️ 🔴 **「1625 年創業」は公式の書き方ではない。**<br>📄 **公式が書くのは「`Né à Aÿ en 1625, François Hémart`, ancêtre de la famille Giraud-Hémart, était vigneron」——**<br>**すなわち 1625 は「一族の祖の生年」であって創業年ではない。**<br>📄 **公式の言い方は一貫して「`les origines du domaine Henri Giraud remontent au XVIIème siècle`」「`depuis le 17ème siècle`」。**<br>🏛 **法人としての `date_creation` は `1975-01-01`。**<br>→ 🔴 **「1625 年創業」と言ってはならない。** → §Staff Notes ⚠️ ① |
| ⚠️ 🔴 **世代数** | ⚠️ 🔴 **公式内で食い違う。**<br>📄 **`Hommage / Famille`: 「12 世代（`the 12 generations`）が Giraud の旗を掲げた」**<br>📄 **`Argonne / Parcelle Miraculeuse`（FR 原文）: 「`La légende de « La Valnon » … a bercé 13 générations de vignerons Giraud-Hémart`」**<br>→ **12 と 13 が公式内で並立する。断定しない。** → §Staff Notes ⚠️ ② |
| 🔴 **認証（🏛 登録）** | 🏛 🔴 **Agence Bio `numeroBio 121737`。認証機関 `Ocacia`、`numeroControleEu: FR-BIO-20`、`etatCertification: ENGAGEE`。**<br>🏛 🔴 **`activites: [{"nom": "Production"}]` のみ（＝栽培。`Préparation` は入っていない）／`mixite: "Non"`**<br>🏛 🔴 **`productions: Raisin de cuve`、`etatProduction: C2`、`anneeReferenceControle: 2025`**<br>🏛 **`datePremierEngagement: 2014-10-06`／`dateEngagement: 2024-10-07`／`dateNotification: 2014-08-18`** → §Farming |
| ⚠️ **認証（HVE / VDC）** | ⚠️ 🔴 **canonical は HVE と VDC の取得を断言するが、本調査では公式にも公的登録にも裏づけが取れなかった。**<br>**稼働中の公式サイトに認証の記述は無く、Internet Archive の旧サイトにも `HVE` `Haute Valeur Environnementale` `VDC` の語は現れなかった。** → §Farming / §Canonical Conflict |
| **canonical id** | 🔍 **3 件**（下記 §Canonical Conflict） |

### 🔴 ⚠️ サイト真正性の事前確認（`D-2026-08-05-09`）—— 合格。ただし「そっくりドメイン」を 1 件掴んだ

| 判定 | ドメイン | 根拠 |
|---|---|---|
| ✅ **合格** | **`champagne-giraud.com`** | 🏛 **(a) mentions légales が `SA Champagne Henri Giraud` / `SIREN 303891048` / `RCS Reims B 303891048` を明記し、これが 🏛 企業登録の SIREN と完全一致。**<br>🏛 **(c) Agence Bio が SIRET `30389104800017` の `siteWebs` に `typeSiteWeb: "Site Officiel"` として `https://www.champagne-giraud.com` を登録している（＝公的登録側からの相互リンク）。**<br>🏛 **(d) 住所 `71 BD Charles de Gaulle, Aÿ-Champagne` が企業登録の本店住所と一致。**<br>🏛 **WHOIS: `Creation Date 2003-04-18` / Registrar `OVH sas` / NS `dns12.ovh.net`（＝フランスの一般事業者ホスティング。パーキングではない）** |
| ✅ **合格（同一 SIREN の別事業所）** | **`manoir-henri-giraud.com`** | ✅ **公式トップ頁が自らこのドメインを掲示。**<br>🏛 **サイトの mentions légales の住所 `83 boulevard Charles de Gaulle, 51160 Aÿ` が、企業登録の第 2 事業所 SIRET `30389104800025`（NAF `55.10Z` 宿泊業）と一致。**<br>→ 🔴 **別ブランドだが別法人ではない。**ワインのスペックは持たない（オエノツーリズムのみ）。**混同しないこと。** |
| 🔴 ❌ **不合格（使用禁止）** | **`champagnegiraud.com`（ハイフン無し）** | 🏛 🔴 **WHOIS: `Creation Date 2016-06-25` / Registrar `Dynadot Inc` / Name Server `NS1.AFTERNIC.COM` `NS2.AFTERNIC.COM`。**<br>🔴 **Afternic は売り出し中ドメインのパーキング DNS。本文長 114 バイト。**<br>→ 🔴 **`ramonet.fr`（ドメイン売出し中）と同型。1 語も使用していない。** |
| 🏛 **存在しない（絶対的不在の証明）** | **`henri-giraud.com`** | 🏛 **`dig` が A レコードも MX も返さない（NXDOMAIN）。** |
| ⚠️ **要注意** | **`boutique.champagne-giraud.com`** | ✅ **生産者ドメイン配下だが、中身は 2 枚の画像だけの旧「トンネル」頁で、`<meta name="robots" content="noindex, nofollow">`。**<br>**リンク先の一つが上記の不合格ドメイン `boutique.champagnegiraud.com` を指している（コメントアウトされた旧リダイレクトも同ドメイン）。**<br>→ 🔴 **生産者自身の古い頁が、現在は他人が持つドメインを指している状態。ここから先へは進んでいない。** |

---

## Overview

✅ 📄 **アイ（Aÿ、現・行政名 Aÿ-Champagne）の 71 boulevard Charles de Gaulle に本拠を置く、家族経営のシャンパーニュ・メゾン。
シャンパーニュの中でも例外的に「アイ・グラン・クリュ 1 村」に軸足を置き、
かつ「アルゴンヌの森の樫樽」というもう一つのテロワールを自らの署名として掲げる。**

🔴 📄 **メゾンが自分の言葉で書いた綱領（旧公式「Expériences Champagne」頁）——**
「**シャンパーニュが再び『`Le grand vin de Champagne`（シャンパーニュの偉大なワイン）』となるために、
最初の時から関与してきたドメーヌとして、われわれのキュヴェのそれぞれが新しい美学を探究し、
自然の女神の背後に消えていく職人＝ヴィニュロンの祖先の身振りの単なる反復を、はるかに超える強い
メッセージを届ける。そしてそれは、それらの身振りからその精髄を剥ぎ取って大量生産に供する
産業的な単純化とは、まったく正反対である。**」

🔴 📄 **同頁が続けて書く、器と品種の宣言 ——**
「**歴史の教えに耳を傾け、革命を恐れることなく、Pinots Noirs と Chardonnay は高貴な素材の核心においてのみ
その姿を現す —— `Fût de chêne d'Argonne`（アルゴンヌの樫樽）、`terre cuite`（テラコッタ）、あるいは `Grès`（炻器）。
`Sans inox` かつ最小限の介入と硫黄によって、われわれの創造的で自然な醸造が、
ワインをテロワールと品種の真実にもっとも近いところへ導く。**」

→ 🔴 **すなわち「品種は 2 つ（ピノ・ノワールとシャルドネ）」「ステンレスは使わない」「器は樫樽・テラコッタ・炻器の 3 種」。
これがこのメゾンの identity の核である。**

🔴 📄 **`MV` の定義も公式が自分で書いている。**
「**`MV, comme Multi Vintage.` この愛着あるキュヴェは、シャンパーニュが再び『シャンパーニュの偉大なワイン』
となるためのわれわれの関与の刻印を帯びている。それら偉大なワインの 3 本の柱 ——
`Petits rendements, petits contenants et cépage d'origine`（小さな収量、小さな容器、原産の品種）—— に立脚し、
`la cuvée Fût de Chêne` は 1990 年以来シャンパーニュに消えない痕跡を残している。**」

🔍 **THÉSEUS における状態は Billecart-Salmon とは異なり、「レコードが足りていない」形である。
canonical は OBP 4 行に対して 3 レコードしか持たず、しかも 3 件すべて `color = Blanc`。
公式レンジ 8 本のうち canonical に対応物があるのは 3 本だけで、ロゼは 3 本とも欠落している。**

---

## History

⚠️ 🔴 **注記 —— 本節の出典はすべて `📄`（Internet Archive に残る生産者自身の頁）である。
稼働中の公式サイトに沿革頁は存在しない。**

| 年 | 出来事 |
|---|---|
| 🔴 **1625** | 🔴 📄 **`François Hémart` がアイに生まれる。**「**Né à Aÿ en 1625, François Hémart, ancêtre de la famille Giraud-Hémart, était vigneron.**」<br>🔴 **これは「一族の祖の生年」であって創業年ではない。** → §Staff Notes ⚠️ ① |
| **1670** | 📄 **「アイからほど近いオートヴィレールの修道院で、Dom Pérignon が完璧なワインを創るためにアッサンブラージュする葡萄の選別に最善を尽くしていた」**（メゾンが自らの年代記に置く同時代の参照点） |
| **17 世紀** | 📄 **「シャンパーニュにおけるピノ・ノワールの近時の使用とともに、ヴィニュロンたちは `vins gris`、すなわち黒葡萄から造る白ワインを生産し始めた」／ヴェルサイユでルイ 14 世がこの「新しい」ワインを愛でた** |
| **1650–1850** | 🔴 📄 **「小氷期（`little ice age`）」。**「**シャンパーニュがあまりに寒く、白葡萄で良い白ワインを、黒葡萄で良い赤ワインを、もはや造れなくなった。こうしてシャンパーニュのヴィニュロンたちはこの気候的事故を乗り越えることを決め、『黒葡萄による偉大な白ワイン』の造り方を学ぶことで圧搾と醸造に革命を起こした。**」 |
| 🔴 **1952 / 1954** | 🔴 📄 **区画 `La Valnon` の逸話。**「**1954 年のあれほど厳しい冬を、リザーヴに満ちた枝で切り抜けた。あるいは 1952 年、その小さなピノ・ノワールが許容最大値 13% vol を超えた。**」 |
| **20 世紀半ば** | 📄 **祖父 `Léon Giraud` による `sélection massale`（マッサル選抜）。「今なおその選抜が、われわれの忠実な収穫チームに、充実し、粘り、スパイシーな果実を差し出している」**<br>📄 **「前世紀半ばに `La Croix-Courcelles` のシャルドネがアッサンブラージュを補完するようになった」** |
| 🔴 **〜1950** | 🔴 📄 **「1950 年まで、タンクは存在せず、シャンパーニュのワインはすべて樫樽で醸造されていた。そのうち 90% がアルゴンヌの森から来ていた。」**<br>📄 **「その後、大量流通・産業化・ステンレスタンクが到来した。4 世紀以上にわたってシャンパーニュ地方の質的成長に関与してきたアルゴンヌの樽工房は、深い眠りに落ちた。」** |
| 🔴 **1990** | 🔴 📄 **転換点が 2 つ同時に起きる。**<br>**(a) 📄「`la cuvée Fût de Chêne` は 1990 年以来シャンパーニュに消えない痕跡を残している」**<br>**(b) 📄「`Homemade perpetual reserve`（自家製の永久リザーヴ）は 1990 年のヴィンテージから始まり、以後の収穫ごとに養われてきた」**<br>**(c) ⚠️ 📄 同じ 1990 年に「シャンパーニュ地方で最初のサーモレギュレーテッド・ステンレスタンクが、われわれの樽の醸造所を補完するものとして設置された」**<br>→ 🔴 **1990 年は「樽の復活」と「ステンレスの導入」が同時に起きた年である。矛盾ではなく、後に否定される実験である。** |
| 🔴 **2005 前後〜** | 🔴 📄 **`Dame-Jane` のためのテラコッタ、次いで炻器（`grès`）の卵形容器を「10 年間」試験。** |
| 🔴 **2015** | 🔴 📄 **「`Since 2015`、25 年後にして、われわれのワインはアルゴンヌの樫樽か炻器の甕でしか醸造されない。」**<br>🔴 **これが「0% INOX」の起点である。canonical が書く「2016 年のステンレス・ゼロ転換」とは 1 年ずれる。** → §Canonical Conflict |
| **2015-07-04** | 📄 **「2015 年 7 月 4 日以来、われわれの名高い街の丘陵は UNESCO 世界遺産に登録されている」** |
| 🔴 **2017 年末** | 🔴 📄 **「No pesticide」表明。**「**ワインの世界で『No pesticide』は 2017 年末に大きく報じられた。Champagne Henri Giraud のこのイニシアティヴの告知 —— 世界で初めての種類のもの —— は大変な衝撃であり、社長の `Claude Giraud` はこのアプローチをさらに進めることを促された。**」<br>📄 **Claude Giraud の一人称: 「DECANTER 誌の Jane Anson のある記事が、われわれにとって啓示だった。…この 1 月からわれわれはさらに先へ進み、バックラベルに貼った QR コードを通じてワインの完全な分析へのアクセスを提供する。」**<br>→ 🔴 **`Esprit Nature` の「New Generation」情報ラベル（QR で分子分析にアクセス）はここから来ている。** |
| **2020-12-19** | 🏛 **第 2 事業所（NAF `55.10Z` 宿泊業、`83 BD Charles de Gaulle`）を開設 → `Manoir Henri Giraud`。** |
| ⚠️ **2023 年頃〜** | ⚠️ 🔴 **公式サイトからキュヴェ情報が消える。**<br>**Internet Archive 上、`/fr/les-experiences/*` の最終捕捉は 2023-03-28。2024 年以降の捕捉は splash と法務頁のみ。** |
| ✅ **2025-06-10** | ✅ **ドメーヌでの終日イベント。公式 PDF 進行表が現存する唯一の「中身のある」公式 PDF。**<br>**`Barrel toasting workshop by the Tonnellerie de Champagne` / `5 senses chalk workshop on the ground floor of the Belvédère` / `Terroir workshop on the Belvédère terrace` / `Cellar tour` / `Gilding workshop` / `Walk to Pressoria` / `Gala Dinner orchestrated by Philippe Mille`** |

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| **本拠** | ✅ **`71 boulevard Charles de Gaulle`、Aÿ-Champagne（🏛 `code_commune 51030`／`lat 49.0532, long 3.9997`）** |
| 📄 **メゾン自身の座標表示** | 📄 **旧公式トップ頁が全画面で表示していた文言: 「`You are in Aÿ-Champagne - Latitude: 49.053552 | Longitude: 4.000027 - Altitude: 74 meters.`」** |
| 🔴 🏛 **アイのグラン・クリュ格** | 🔴 🏛 **INAO「AOC Champagne」cahier des charges 第 I 章 II-b が、`grand cru` および `premier cru` の表示を許す 17 コミューンを列挙し、そのなかに `Ay` が含まれる。**<br>**（Ambonnay, Avize, **Ay**, Beaumont-sur-Vesle, Bouzy, Chouilly, Cramant, Louvois, Mailly-Champagne, Le Mesnil-sur-Oger, Oger, Oiry, Puisieulx, Sillery, Tours-sur-Marne, Verzenay, Verzy）**<br>→ 🔴 **「アイ・グラン・クリュ」は造り手の自称ではなく、appellation の法文に根拠がある。** |
| ⚠️ **「グランド・ヴァレ・ド・ラ・マルヌ」** | ⚠️ 🔴 **canonical `henri-giraud-esprit-nature` は `subregion` に「Aÿ Grand Cru — Grande Vallée de la Marne」と書き、terroir 欄で「公式にはグランド・ヴァレ・ド・ラ・マルヌに属する（モンターニュ・ド・ランスではない）」と断定する。**<br>⚠️ **INAO の cahier des charges にはこの下位区分の概念が存在しない。生産者の公式頁にも現れない。**<br>→ ⚠️ **否定はしないが、本ドシエは一次資料で裏づけられなかったことを記録する。** → Open Questions 5 |
| 🔴 📄 **区画（ブドウ側）** | 🔴 📄 **`La Valnon`（「`parcelle miraculeuse`」）—— 「アイ・グラン・クリュのテロワールのど真ん中、`la côte Châtillon` の真下に位置する」。**<br>🔴 📄 **`La Croix-Courcelles` —— 前世紀半ばからアッサンブラージュを補完するシャルドネの区画。**<br>❓ **他の区画名・面積は非公表。** |
| 🔴 📄 **区画（森側）** | 🔴 📄 **`Les Châtrices` —— アルゴンヌの森の南向き区画。「非常に貧しく乾いた `gaize` 土壌」。**<br>📄 **`Hauts-Bâtis` の森 —— 「少なくとも樹齢 3 世紀の `Giraud oak tree`（ジローの樫）」がある。** |
| 🔴 📄 **アイの白亜** | 🔴 📄 **「アイの白亜は、7 千万年前に白亜紀の海が置き去りにした。極度に貧しく柔らかい。場所によって 200 メートルを超える厚さがあり、その上をわずか 20 センチの肥沃土が覆うだけである。…爪で簡単に傷がつくほど柔らかい。…南向きで、貧栄養で、熱と水を蓄えて規則的に返す。過剰を排水し、吸収する。微細な海洋化石に富み、母のような関係でブドウ樹に最良のものを与え、ワインにこの特異な構造と比類ない塩味を与える。」**<br>📄 **同頁が掲げる引用: 「`La Champagne : Un pays pauvre qu'un vin de craie fit somptueux.` - Salvador Dali」** |
| 🔴 **アルゴンヌの森の距離** | 🔴 📄 **「シャンパーニュのヴィニュロンたちが 16 世紀以来、樽を造るために `almost eighty kilometres`（およそ 80 km）離れたこの森を選んだ理由は…」**<br>📄 **別頁は「80 km 離れたアルゴンヌで、ジローの樫が…」と書く。** |
| ❓ **自社畑面積** | ❓ 🔴 **公式は面積を公表していない。**<br>⚠️ **canonical `henri-giraud-argonne-2016` は「自社畑は 5.67ha、年産は約 25 万本」と断定するが、本調査では公式にも公的登録にも裏づけが取れなかった。** → §Canonical Conflict |
| 🏛 **規模の間接指標** | 🏛 **企業登録の `tranche_effectif_salarie: 12`（本店）／`03`（Manoir）。`annee_tranche_effectif_salarie: 2023`。**<br>🏛 **`liste_idcc: ["0493"]`（ワイン卸売の労働協約）。** |

### 🔴 📄 アルゴンヌの森 —— 「もう一つのテロワール」（**客が必ず訊く**）

📄 **「ヴィニュロンたちがこの森を選んだ理由は、そこから大きな利を得ていたからである ——
その `tannins` の繊細さと控えめさは、栄養分を持たない `gaize` 土壌の極度の貧しさによってのみ匹敵される。
`staves`（樽板）の木目と目はあまりに緻密で、木は完全に金髪のワイン（＝シャンパーニュ）の背後へ退き、
それに寄り添い、それを光のもとへ連れ出す。**」

🔴 📄 **「小さなアルゴンヌ樫樽での醸造と熟成の仕事から、われわれは
`the oak tree bears its terroir as the vine does`（樫はブドウ樹と同じように自らのテロワールを担う）ことを学んだ。
だがブドウ樹が毎年ワインを与えるのに対し、森は樹齢 200 年の樫を、その生涯に一度しか与えない。**」

🔴 📄 **森林との具体的な関係（数字が公表されている数少ない箇所）——**
- 📄 **「われわれは `ONF`（Office National des Forêts、フランス国有林野庁）と協働し、
  `Save the Argonne Forest` キャンペーンを通じて毎年およそ **8,000 本**の新しい樫の植樹に出資している。」**
- 📄 **「それぞれの樹は森のなかで注意深く選ばれ、すべてが `geolocated`（位置情報付き）され、森林事務所で標識される。」**
- 📄 **「`merrandier`（樽材職人）が割ったそれぞれの `stave` は、末広がりの円形に下向きに配置される前に、標識され彫られる。
  そして `bottoms`（鏡板）は、グルテン残渣を排除するために `buckwheat flour`（そば粉）で接がれる。」**
- 🔴 📄 **「われわれの樫樽は **5 年間**働く。それから、それらの樽はそのテロワールの歌を囁き続けるために
  `to Japan`（日本へ）渡り、そこで `sake`（日本酒）を仕込むために再利用される。」**

---

## Farming

🔴 **本節は「公式サイトが完全に沈黙しており、公的登録だけが事実を持っている」という理由で、
本ドシエで最も誤りやすい節である。両方を書き、どちらも断定しない。**

### 🔴 🏛 公的登録が持っている事実（Agence Bio）

🏛 **企業登録の本店レコードに `liste_id_bio: [121737]` が入っている。これを手がかりに
Agence Bio のオープンデータを引くと、次が得られる。**

| 項目 | 🏛 Agence Bio / Ocacia の値 |
|---|---|
| **numeroBio** | **121737** |
| **raisonSociale** | **CHAMPAGNE HENRI GIRAUD**（`denominationcourante: SA CHAMPAGNE HENRI GIRAUD`） |
| **siret** | **30389104800017**（企業登録の本店 SIRET と一致） |
| **gerant** | **Emmanuelle GIRAUD PATOUR**（公式 mentions légales の `Présidente` と一致） |
| 🔴 **認証機関** | 🔴 **`Ocacia`、`numeroControleEu: FR-BIO-20`** |
| 🔴 **状態** | 🔴 **`etatCertification: ENGAGEE`** |
| 🔴 **生産** | 🔴 ⚠️ **`Raisin de cuve`（コード 01.21.12）、`etatProduction: C2`、`anneeReferenceControle: 2025`** |
| 🔴 **活動区分** | 🔴 **`activites: [{"nom": "Production"}]` のみ。`Préparation`（＝醸造・加工）は入っていない。** |
| 🔴 **混合経営** | 🔴 **`mixite: "Non"`** |
| **日付** | 🔴 ⚠️ **`datePremierEngagement: 2014-10-06`／`dateEngagement: 2024-10-07`／`dateNotification: 2014-08-18`** |
| **siteWebs** | **`https://www.champagne-giraud.com`（`Site Officiel`）／Facebook／Instagram** |
| ⚠️ **年鑑上の区分** | ⚠️ **`annuaireActivites: [{"nom": "Culture céréalière"}]`（穀物栽培）。**<br>⚠️ **明らかに年鑑の分類ミスと読めるが、登録値としてそのまま記録する。** |
| **販売区分** | **`venteParticuliers: true` / `venteProsDetail: true` / `venteRestauCommerciale: true` / `venteProsGros: false`** |
| **公開証明書** | **`https://webgate.ec.europa.eu/tracesnt/directory/publication/organic-operator/index?121737`**（EU TRACES） |

### 🔴 ⚠️ この 4 行を重ねると、事実はこうなる —— **言い方を誤ると即座に嘘になる**

**① 🔴 このメゾンは EU 有機規則のもとで `Ocacia`（FR-BIO-20）に登録されており、状態は `ENGAGEE` である。**
**② 🔴 ただし 2025 年の管理年における生産状態は `C2` —— すなわち「有機転換 2 年目」であって、
`AB`（認証取得済み）ではない。**
**③ 🔴 登録上の活動は `Production`（＝栽培）のみであり、`Préparation`（＝醸造）は登録されていない。**
**（🔴 Billecart-Salmon はこの正反対で `Préparation` のみだった。両者を同じ言い方で説明してはならない。）**
**④ 🔴 `mixite: "Non"` は、有機と非有機を併存させていない事業者であることを意味する。**

⚠️ 🔴 **日付が矛盾している。`datePremierEngagement` は `2014-10-06` なのに、
現行の `dateEngagement` は `2024-10-07`、生産状態は 2025 年基準で `C2` である。**
→ 🔴 **もっとも自然な読みは「2014 年に一度関与し、中断があり、2024 年 10 月に改めて関与を開始した」だが、
Agence Bio のレコードは中断の有無を書いていない。断定しない。** → Open Questions 3

### 🔴 OBP のヴィンテージと転換時期の関係（**タスクの問い**）

| OBP 行 | ヴィンテージ | 🏛 有機との関係 |
|---|---|---|
| 3 行目 `'Argonne,' Grand Cru Brut` | **2016** | 🔴 **`dateEngagement: 2024-10-07` の 8 年前、現行転換サイクルの開始より前。**<br>**仮に 2014 年の初回関与が継続していたとしても、有機ブドウとして認証された果実であることを示す記録は無い。** |
| 4 行目 `Grand Cru Brut Rosé` | **2022** | 🔴 **同じく現行転換サイクル（2024-10-07）より前。**<br>**2025 年基準でようやく `C2` である以上、2022 年の果実が有機認証を受けていた可能性は登録上ゼロである。** |

→ 🔴 **したがって「OBP に載っている Henri Giraud は有機です」は言ってはならない。**
→ 🔴 **同時に「有機の登録はありません」も言ってはならない。両方とも事実に反する。** → §Staff Notes ⚠️ ④

### ⚠️ 🔴 HVE / VDC —— canonical の断定に裏づけが取れない

⚠️ 🔴 **canonical `henri-giraud-esprit-nature` は「HVE（高環境価値）および Viticulture Durable en Champagne の
認証を取得し」と断定し、`henri-giraud-argonne-2016` も「畑は HVE 認証」と断定する。**
⚠️ 🔴 **本調査では、稼働中の公式サイト（8 頁すべて）にも、Internet Archive に残る旧公式サイトのキュヴェ頁・
マーカー頁にも、`HVE` `Haute Valeur Environnementale` `VDC` `Viticulture Durable` の語を 1 度も見つけられなかった。**
⚠️ **Agence Bio は HVE を扱わないため、これは Agence Bio の沈黙では否定も肯定もできない。**
→ ⚠️ 🔴 **「HVE 認証です」と口頭で断定してはならない。** → §Staff Notes ⚠️ ⑤ / Open Questions 2

### 📄 公式が名指しする栽培・醸造上の姿勢（認証ではなく実践）

| 主題 | 📄 公式の記述 |
|---|---|
| 🔴 **農薬** | 🔴 **2017 年末の「`No pesticide`」表明。「世界で初めての種類のもの」と自称。** |
| 🔴 **透明性** | 🔴 **`Esprit Nature` のバックラベルに QR コードを貼り、「ワインの完全な分析」へのアクセスを提供する `New Generation` ラベル。「100% の皆さんが `obligation of means` より `outcome obligation` を選ぶ」** |
| 🔴 **硫黄** | 🔴 **「`Sans inox` かつ `avec le minimum d'intervention et de souffre`（最小限の介入と硫黄で）」**<br>📄 **甕について「ワインはそのなかで守られ、`few sulphites` しか必要としない」**<br>⚠️ **数値（mg/L）は公表されていない。** |
| **森林** | **ONF と協働、`Save the Argonne Forest` で年 8,000 本の植樹に出資** |
| **象徴** | **敷地内に Claudine DIVRY による高さ 4 m の「`Paper Tree`」（再生新聞紙の彫刻）** |

---

## Winemaking

### 🔴 📄 メゾンの署名 —— `0% INOX`

🔴 📄 **`Dame-Jane / Vinification en Amphore` 頁（公式）の全経緯 ——**
「**1990 年、シャンパーニュ地方で最初のサーモレギュレーテッド・ステンレスタンクが、
われわれの樽の醸造所を補完するものとして設置された。こうしてわれわれは、ステンレスタンクにおける
発酵温度の制御について多くを学んだ。われわれはこの大きな近代的投資を大変誇りに思っていた。
しかし年を追うごとに、経験はわれわれの最も偉大なワインが樫樽で醸造されたワインであることを示した。
そこでわれわれはこの格言が真であると知った ——『`Great wines need small containers`』。
別様に考える自由、謙虚さ、そして最良の結果への要求が、われわれを自然に、そして漸進的に
醸造における『`0% INOX`』の道へ導いた。ステンレスの唯一の証明された利点は、
非常に大きな容器を造ることを可能にする点だけだからである。**」

🔴 📄 **同頁: 「`Since 2015`、25 年後にして、われわれのワインはアルゴンヌの樫樽か炻器の甕でしか醸造されない。」**
🔴 📄 **`Blanc de Craie / Décalé` 頁: 「30 年以上の綿密な仕事と探究ののち、われわれは
『`0% STAINLESS STEEL`』の道を選び、小さな容器のみを使う。」**

→ 🔴 **公式の起点は `2015` である。canonical は `2016` と書く。** → §Canonical Conflict

### 🔴 📄 器 —— 3 種類しかない

| 器 | 📄 公式の記述 |
|---|---|
| 🔴 **アルゴンヌ樫の小樽** | **「1950 年まで、タンクは存在せず、シャンパーニュのワインはすべて樫樽で醸造され、その 90% がアルゴンヌの森から来ていた」／樽の稼働年数は **5 年**、その後日本へ渡り日本酒の仕込みに再利用される**<br>⚠️ **容量（リットル）は公式に記載が無い。** |
| 🔴 **テラコッタ（`terre cuite`）／炻器（`grès`）の卵形甕** | 🔴 **「`DAME-JANE` の醸造のために、われわれは 10 年にわたって新しい卵形のテラコッタ容器を、次いで炻器の容器を試験した。炻器が果実に深さ、新鮮さ、振動をもたらすからである。」**<br>🔴 **「今日、**50 の amphorae** が `DAME-JANE` の醸造と熟成のためだけに使われている。」**<br>🔴 **「甕の面を通じた最小限のゆるやかな空気の循環が、この偉大なロゼに完璧な呼吸を保証する。」** |
| ❌ **ステンレス** | 🔴 **2015 年以降、使用していないと公式が明言。** |

### 🔴 📄 永久リザーヴ（`Réserve Perpétuelle`）

🔴 📄 **`MV / Mark 02 Réserve Perpétuelle` 頁 ——**
「**MV はまた、たった一年の像の単なる再現をはるかに超えて、ミレジムのワインを表現する
われわれの特異で唯一の仕方を翻訳している。最も偉大な香水の造り手たちのように、
われわれはワインをその最高の表現へ押し上げる芳香の `teaser` に取り組む。
`The Homemade perpetual reserve` は **1990 年のヴィンテージから始まり**、以後の収穫ごとに養われてきて、
ミレジムのワインの微妙な香りが戯れる動物的な `teaser` を与える。
ピノ・ノワールの `heart` が、美しいミネラルの苦味とアイ・グラン・クリュの塩味に照らされた果実を差し出す。**」

⚠️ 🔴 **canonical `henri-giraud-esprit-nature` は「永久リザーヴを 3 分の 1 ブレンド」と断定するが、
公式は永久リザーヴの比率をどこにも書いていない。** → §Canonical Conflict

### 🔴 📄 唯一入手できた公式フィッシュ・テクニック（**2 点。いずれも旧サイト配下の PDF**）

⚠️ 🔴 **重要 —— この 2 点は OBP の 4 行のどれにも対応しない。**
**同じメゾンの、別のキュヴェ／別の時代のスペックである。OBP の 4 本に流用してはならない。**

| フィッシュ | 📄 公式の記載内容 |
|---|---|
| 🔴 **`Fiche_hommage.pdf`**（`Hommage - Aÿ Grand Cru`） | 🔴 **`Composition : 70% Pinot Noir, 30% Chardonnay, exclusivement cueillis sur le terroir d'Aÿ.`**<br>🔴 **`Vinification en cuve thermorégulée et élevage 6 mois en petits fûts de chêne.`**<br>**Dégustation: 「深く軽く琥珀を帯びた色調が élevage を刻む。細やかで豊かな泡が絶えず更新される美しいコルドンをなす。スイカズラ、黄色い果実、そして綺麗にメントール香を帯びた青いアーモンドの、非常に美しく優雅で新鮮な香り。口中は大きな優雅さで、丸く美味、洋梨に黄色い果実、干した杏、そしてオレンジの皮とチョコレートの終盤。このワインのビロードのような gras と、その終盤の白亜的で新鮮な調子との、微妙な均衡。」**<br>**Accords: `À 12°` でその力強さと強い個性が非常に広いガストロノミーの幅を開く（ウイキョウ添えのスズキ、蜂蜜の豚ミニヨン、柑橘の鴨…）／あるいは `à 8°` 氷で冷やして** |
| ⚠️ 🔴 **`ch-giraud_esprit-brut.pdf`**（`Esprit de Giraud`） | ⚠️ 🔴 **これは `Esprit Nature` ではない。名称が違う。混同しないこと。**<br>🔴 **`Composition : 70% Pinot Noir 30% Chardonnay.`**<br>🔴 **`Vinification thermorégulée en cuve inox durant une année sans soutirage sur lie entière.`**（＝ステンレスタンクでの醸造。0% INOX 以前の仕様）<br>**A l'œil: 成熟に達したピノ・ノワールに典型的な、美しい金の色調と金髪の照り。**<br>**Au nez: 核果（洋梨、桃）、ヴァニラ、香辛料（白胡椒）が砂糖漬けレモンの下地の上に。続いて成熟と美味しさ。**<br>**En bouche: アタックは新鮮、次いで控えめになり、全体の `vinosité` を表現させる。ミネラリティと軽いタンニンが、長く、ヴィノーゼで、温かく、絹のような収斂性を持つ最終構造に寄与し、苦扁桃とビスケットの香りを伴う。**<br>⚠️ 🔴 **`Dégustation:` の署名は `Franck Wolfert - Vins & Atmosphères - Mailly-Champagne`。**<br>→ ⚠️ **テイスティングノートは外部の第三者が書いてメゾンのフィッシュに載せたものである。メゾン自身の官能表現ではない。** |

### ❓ 公式が一切公表していない数値（**本ドシエは書かない**）

❓ 🔴 **ドザージュの g/L 値 —— 全キュヴェについて、いかなる公式資料にも 1 件も存在しない。**
❓ 🔴 **OBP 4 本のセパージュ比率。**（上表の 70/30 は `Hommage` と `Esprit de Giraud` の値であって、OBP の 4 本の値ではない）
❓ **澱との接触期間（月数）、デゴルジュマン日、アルコール度数、生産本数（`Argonne Rosé` の 328 本を除く）、圧搾比率、マロラクティック発酵の有無。**
🔴 **したがって本ドシエは、OBP の 4 本について MLF・熟成月数・ドザージュ数値を一切主張しない。**

---

## Style

### 🔴 📄 公式が自らの言葉で書くキュヴェ像（**スペック表ではなく散文しか存在しない**）

⚠️ 🔴 **注記 —— 以下はすべて旧公式サイトの散文であり、テイスティングノートの体裁を取っていない。
`A L'ŒIL / AU NEZ / EN BOUCHE` の構造化ノートは、`Hommage` と `Esprit de Giraud` の 2 点のフィッシュにしか存在しない。**

| キュヴェ | 📄 公式の記述 |
|---|---|
| 🔴 **ESPRIT NATURE**<br>⭐ **OBP 1** | **「`L'ESPRIT NATURE`, Henri Giraud のスタイルへの入門。良いワインを 1 杯分かち合うという単純な喜びを取り戻す。」**<br>**「この輝くワインは、`obligation de moyens`（手段の義務）より `obligation de résultats`（結果の義務）を優先する、自然と人間の健康の保護に対するわがメゾンの関与の旗を高く掲げる。」**<br>🔴 **「`Esprit Nature` はまた、われわれの自然派ワインの見方を提示する。その紋章である `Chêne de papier`（紙の樫）は、生あるものの脆さと、同時にそれを再建する人間の能力を語る。」**<br>🔴 **「`Pailleté de beaux amers minéraux`（美しいミネラルの苦味をちりばめられ）、それはシャンパーニュの偉大なワインの扉を押し、その比類ない果実は分かち合う喜びへと誘う。」**<br>**「`Il suffit de le mettre en bouche et il parle.`（口に含めばいい、それで語る。）」** |
| 🔴 **MV**<br>（`Fût de Chêne`） | **「`MV, comme Multi Vintage.`」**<br>🔴 **「小収量・小容器・原産品種という 3 本の柱に立ち、`la cuvée Fût de Chêne` は 1990 年以来シャンパーニュに消えない痕跡を残している。」**<br>🔴 **「`Colonne vertébrale de notre collection`、MV は樫樽におけるトレーサビリティと醸造についての前例のない仕事の成果であり、それがわれわれに森のテロワールを自分自身のブドウのテロワールとして理解させた。」**<br>📄 **「ピノ・ノワールの `heart` が、美しいミネラルの苦味とアイ・グラン・クリュの塩味に照らされた果実を差し出す。」** |
| 🔴 **ARG̈ONNE**<br>⭐ **OBP 3** | **「`ARG̈ONNE, la belle et la bête`（美女と野獣）。」**<br>🔴 **「金の葉に覆われただけで、Argonne は、18 世紀にシャンパーニュとその後光がその上に築かれた 2 つの偉大な歴史的テロワール、すなわちブドウと森との融合的な関係を宿す。」**<br>🔴 **「それはアイのワインと、20 世紀半ばまですべてのシャンパーニュのワインを育てた大きな樫を持つアルゴンヌの森との共生を語る。」**<br>🔴 **「`Seuls de très grands millésimes peuvent présider à l'union prolifique de la belle et la bête.`（きわめて偉大なミレジムだけが、美女と野獣の実り多い結合を主宰しうる。）こうしてシャンパーニュにおいてまったく特異で唯一の例外的な作品が生まれる。」** |
| 🔴 **MV ROSÉ** | 🔴 **「`MV ROSÉ`、ベル・エポックの偉大なロゼ・シャンパーニュ。」**<br>🔴 **「その `robe œil-de-perdrix`（山鶉の目の色調）が、成熟したワインの自然な魅力を際立たせる。」**<br>🔴 **「その名高い先達のキュヴェたちのように、`MV ROSÉ` はアルゴンヌの森で選ばれた最良の樫から造られた小樽で、大切に扱われた醸造の恩恵を受ける。」**<br>🔴 **「Henri Giraud の偉大な年と、われわれの名高い `Aÿ Rouge Grand Cru` との、崇高で高貴な同盟。」**<br>**「アイの白亜が口中に現れ、赤い果実、マンダリン、そしてこの醸造に典型的な `smoked meat` の調子と混ざり合う。塩味と美しい苦味が、これを非常に偉大なロゼ・シャンパーニュにしている。」** |
| 🔴 **ARG̈ONNE ROSÉ** | 🔴 **「`ARGONNE 2004 ROSÉ`, Queen of Saba（シバの女王）。」**<br>🔴 **「2002 年の冬に `Châtrices` の森から造られた唯一の小樽で生産され、Argonne Rosé は `ARGONNE 2004` の最良の部分の極端な選別と、並外れた Henri Giraud の `red Aÿ Grand Cru` の数リットルとの融合の果実である。」**<br>🔴 **「その家族的生産は **328 本**に限られた。」**<br>**「金細工師 `Uwe Schäfer` が `Dream Gold` の金箔を吹きつけて貼る。」** |
| 🔴 **DAME-JANE** | 🔴 **「`DAME-JANE`, attractive and greedy. 偉大なロゼ・シャンパーニュをテラコッタで醸造するのは、きわめて異例である。」**<br>**「`Luminous hue.` 果実の結晶的な純度の振動。ほとんど触覚的な新鮮さの感覚。澱のゆるやかな `riddling` によって高められた柔らかいタンニン。」**<br>📄 **語源: `Dâmghân`（シルクロード、テヘランから 300 km）→ `Damajana` → **1614 年**に `Dame-Jane`。** |
| **HOMMAGE** | **「`HOMMAGE`, 祖先への献辞。このキュヴェで Henri Giraud のドメーヌは、Giraud-Hémart 家の祖であり先駆者であった `François Hémart`（1625–1705）に敬意を表する。」**<br>🔴 **「小さな樫樽における醸造の振動が、ピノ・ノワールの驚くべき芳香の幅を昇華させ、それが例外的に複雑な炸裂を統べる、定義しがたくスパイシーな柔らかさを明かす。」** |
| **BLANC DE CRAIE** | **「`BLANC DE CRAIE`, 独創性の経験。アイに植えられ、南の白亜のなかで、シャルドネという品種は天才である！」**<br>🔴 **「ピノ・ノワールの土壌でシャルドネを仕事することで、われわれは自らの差異を示すことを恐れない。」**<br>**「`Blanc de Craie` はブラン・ド・ブランの古典的な清澄さを迂回し、典型性と寛大さをもってその独創性を押し出す。」** |

⚠️ 🔴 **第三者評点は本ドシエに 1 件も記載しない。公式サイトが第三者評点を掲載していないためである。**
**（Billecart-Salmon と異なり、このメゾンは自サイトに点数を載せていない。）**

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 4 本。exact 1 / alias 1 / unresolved 2**）

| # | OBP 印字 | VT | 価格 | セクション | intake | 📄 **公式での確認結果** |
|---|---|---|---|---|---|---|
| 1 | **`'Esprit Nature,' Brut Nature`** | NV | $250 | `… \| BLENDS` | `exact` → `cuvee:henri-giraud-esprit-nature` | 📄 **キュヴェは実在。公式の見出しは `L'ESPRIT NATURE`。**<br>🔴 ⚠️ **ただし `Brut Nature` を裏づける公式記述は 1 件も無い。下記参照** |
| 2 | **`Grand Cru Brut`**（キュヴェ名の印字が 1 語も無い） | NV | $800 | `… \| BLENDS` | 🔴 **`unresolved`** | ❓ 🔴 **候補を 3 本まで絞ったが、公式では 1 本に確定できない。名前は書かない。下記参照** |
| 3 | **`'Argonne,' Grand Cru Brut`** | **2016** | $2,640 | `… \| BLENDS` | `alias` → `cuvee:henri-giraud-argonne-ay-grand-cru` | 📄 **キュヴェは実在（`ARG̈ONNE`）。**<br>🔴 ⚠️ **だが「2016」というミレジムを裏づける公式記述は存在しない。下記参照** |
| 4 | **`Grand Cru Brut Rosé`**（キュヴェ名の印字が 1 語も無い） | **2022** | $735 | 🔴 `… \| **ROSÉ**` | 🔴 **`unresolved`** | ❓ 🔴 **公式のロゼは 3 本実在するが、1 本に絞れない。かつ canonical に受け皿が 1 件も無い。下記参照** |

---

### 🔴 1 行目 —— `Esprit Nature` は実在する。だが **`Brut Nature` は誰も裏づけていない**

📄 ✅ **キュヴェの実在は確実。公式の見出しは `L'ESPRIT NATURE`、レンジ一覧の先頭に置かれる。**
📄 **公式の位置づけは「`Initiez-vous au style Henri Giraud`（Henri Giraud のスタイルへの入門）」。**

🔴 ⚠️ **ここからが問題である。**

| 主体 | ドザージュ区分の表記 |
|---|---|
| **OBP メニュー** | 🔴 **`Brut Nature`**（＝糖の添加なし。0–3 g/L） |
| **canonical** | 🔴 **`classification: "Brut"`**／`dosage: "Brut — 公式テクニカルシートに数値の記載なし"` |
| 📄 **公式** | 🔴 **どちらも書いていない。`Esprit Nature` のドザージュ区分に触れた公式記述は 1 件も存在しない。** |

→ 🔴 **メニューと canonical が食い違っており、造り手はどちらも支持していない。**
→ 🔴 **`Nature` はキュヴェ名の一部であって、ドザージュ区分ではない可能性が高い。**
**しかし「高い」は根拠ではないので、本ドシエは判定しない。**
→ 🔴 ⚠️ **`match_state` が `exact` であることに騙されてはならない。**
**intake の evidence は「名称トークン集合一致: `Esprit Nature` ≡ `Esprit Nature`」の 1 点だけであり、
`_parts.style = "brut nature"` と canonical の `classification = "Brut"` は照合されていない。**
→ 🔴 **すなわち `exact` は「名前が一致した」以上のことを何も保証していない。** → §Canonical Conflict（未採番）

⚠️ 🔴 **`Esprit de Giraud`（2010 年のフィッシュ）を `Esprit Nature` の旧称として扱ってはならない。**
**別の名前であり、公式に両者を結ぶ記述は存在しない。**
**（`Esprit de Giraud` は `Vinification thermorégulée en cuve inox` と書いており、
これは 2015 年の `0% INOX` 転換の前の仕様である。もし同一キュヴェの旧版なら、この点も断層になる。）**

---

### 🔴 2 行目 —— キュヴェ名が 1 語も印字されていない `Grand Cru Brut`（$800）

🔍 **intake の生データ**: `source_wine_raw = "Grand Cru Brut"` / `_parts.label = null` /
`_parts.printed_rest = "Grand Cru Brut"` / `_parts.rank = "Grand Cru"` /
`evidence = "'Henri Giraud' の canonical キュヴェ 3 件に一致無し: 'Grand Cru Brut'"`。
🔴 **メニューが印字しているのは格付語（`Grand Cru`）とドザージュ区分（`Brut`）だけである。
生産者を特定する語も、キュヴェを特定する語も、1 語も無い。**

#### 📄 候補集合の境界（**ここまでが公式で言えること**）

🔴 📄 **公式「Expériences Champagne」頁が、自らレンジ全 8 本を列挙している ——**
`Esprit Nature | MV | MV Rosé | Hommage | Blanc de Craie | Dame-Jane | ArG̈onne | ArG̈onne Rosé`

| キュヴェ | 色 | NV / VT | 2 行目の候補か | 根拠 |
|---|---|---|---|---|
| **Esprit Nature** | 白 | NV | ❌ **除外** | **1 行目が同じメニュー内で $250 として別行に載っている** |
| 🔴 **MV** | 白 | 🔴 **NV（Multi Vintage）** | 🔴 ✅ **候補** | **`MV, comme Multi Vintage.`／`Colonne vertébrale de notre collection`** |
| 🔴 **Hommage** | 白 | **NV** | 🔴 ✅ **候補** | **フィッシュ見出しが `Hommage - Aÿ Grand Cru`。ミレジム表記なし** |
| 🔴 **Blanc de Craie** | 白 | **NV** | 🔴 ✅ **候補** | **公式にミレジム表記なし。ただしブラン・ド・ブランであり、メニューがそれを印字しないのは不自然** |
| **Dame-Jane** | 🔴 **ロゼ** | — | ❌ **除外** | **「偉大なロゼ・シャンパーニュ」。セクションが `BLENDS` である** |
| **MV Rosé** | 🔴 **ロゼ** | NV | ❌ **除外** | **同上** |
| **ArG̈onne** | 白 | 🔴 **VT** | ❌ **除外** | **「きわめて偉大なミレジムだけが」。かつ 3 行目が同じメニュー内に載っている** |
| **ArG̈onne Rosé** | 🔴 **ロゼ** | VT | ❌ **除外** | **同上** |

→ 🔴 **候補は `MV` / `Hommage` / `Blanc de Craie` の 3 本に絞られる。**

#### 🔴 `Fût de Chêne MV17` 仮説の検証結果 —— **有力だが確定できない**

🔴 📄 **公式が `MV = Fût de Chêne` であることは確定した。**
「**`MV, comme Multi Vintage.` …小収量・小容器・原産品種という 3 本の柱に立脚し、
`la cuvée Fût de Chêne` は 1990 年以来シャンパーニュに消えない痕跡を残している。**」
🔴 📄 **旧公式サイトの URL 構造もこれを裏づける。`MV` のマーカー 3 枚は
`mv-mark-01-fut-de-chene` / `mv-mark-02-reserve-perpetuelle` / `mv-mark-03-ay-grand-cru` である。**
**すなわち `Fût de Chêne` は MV の 3 つの識別標のうちの 1 つであって、別キュヴェではない。**
🔴 📄 **公式のキュヴェ頁のタイトルは `MV13`。すなわち `MV` は「ベース年 2 桁」を伴って表記される。**

🔴 **しかし ——**
- ❓ **公式は価格を 1 件も公表していない。$800 という数字は候補を絞る材料にならない。**
- ❓ **`Hommage` も `Blanc de Craie` も NV のアイ・グラン・クリュであり、`Grand Cru Brut` という印字と等しく整合する。**
- ❓ 🔴 **canonical に `giraud-fut-de-chene`（`Fût de Chêne MV17 Grand Cru`）が存在することは、
  「メニューがそれを指している」ことの証拠にはならない。canonical はメニューの出典ではない。**

→ 🔴 **したがって本ドシエは 2 行目に名前を書かない。**
→ 🔴 **候補を 3 本に限定できたこと自体が成果であり、そこから先は物理ラベルの確認が要る。** → §Staff Notes 物理確認タスク ①

#### 🔴 `MV` 表記が canonical に投げかける問題（**タスクの問い**）

🔴 **`MV` = `Multi Vintage`。数字（`MV13` / `MV17`）は「ベースとなる年」であって millésime ではない。**
🔴 **appellation 上は NV であり、canonical も `vintage: "NV"` と持っている。**
🔴 **だが `MV17` と `MV13` は別のワインである。両者を区別する識別子は「17」「13」しかない。**
→ 🔴 **これは Krug `Grande Cuvée` の `162ème〜173ème Édition` と完全に同じ形であり、`V-1` 族に該当する。**
→ 🔴 **canonical の id `giraud-fut-de-chene` には MV 番号が入っていない（name にだけ `MV17` がある）。
`MV18` が来た瞬間に id が衝突する。** → §Canonical Conflict

---

### 🔴 3 行目 —— `Argonne` は実在する。だが **2016 というミレジムを公式は書いていない**

📄 ✅ **キュヴェの実在は確実。公式の綴りは `ARG̈ONNE`（G の上にトレマ）。**
📄 **由来: 「テロワールの再会を祝して、われわれは最も美しいキュヴェを `ARGONNE` と名づけ、
`G` の大文字を『`Aÿ Grand Cru`』のトレマで戴冠させた。」**
→ 🔴 **すなわち `Aÿ Grand Cru` は、ロゴの中に組み込まれた形でキュヴェ名に結びついている。**
**canonical が `Argonne Aÿ Grand Cru` と綴り、メニューが `Argonne` と綴るのは、
どちらも造り手の表記と矛盾しない。** → **タスクの問いへの回答**

| 項目 | 📄 公式（旧サイトのマーカー頁） |
|---|---|
| 🔴 **ブドウ側テロワール** | 🔴 **`Les Valnons` のピノ・ノワール（`La Valnon` 区画、アイ・グラン・クリュ、`côte Châtillon` の真下）。**<br>📄 **「前世紀半ばに `La Croix-Courcelles` のシャルドネがアッサンブラージュを補完するようになった」** |
| 🔴 **森側テロワール** | 🔴 **アルゴンヌの森の `Châtrices` 区画。「南向きで非常に貧しく乾いた `gaize` 土壌」** |
| 🔴 **樽** | 🔴 **`fût de chêne neuf`（新樽）。「Sébastien Le Golvet は今日、繊細なワインと新しい樫樽とのこの生きた関係を統御する、おそらく唯一の Chef de Cave である。」** |
| 🔴 **香りの構造（公式の言い方）** | 🔴 **「香りの構造は `graphite`（黒鉛）に刻まれ、アイ・グラン・クリュの繊細で酸のある性格を明かすミネラリティを与える。」** |
| ❓ **セパージュ比率** | ❓ 🔴 **公式に数値の記載が無い。**（canonical は「PN 90% / Ch 10%」と断定する。§Canonical Conflict） |
| ❓ **ドザージュ** | ❓ 🔴 **公式に記載が無い（区分も数値も）。** |
| ❓ **熟成期間** | ❓ 🔴 **公式に記載が無い。** |
| 🔴 **公式が列挙するミレジム** | 🔴 **`ARGONNE 2002` / `2004` / `2008` / `2011` の 4 つ。**<br>**（`argonne-marqueur-millesimes` 頁、2021-09-24 捕捉）**<br>🔴 ⚠️ **`2016` はこの一覧に無い。** |

#### 🔴 ⚠️ `Argonne 2016` について本ドシエが言えること

⚠️ 🔴 **稼働中の公式サイトにも、Internet Archive に残る旧公式サイトのどの頁にも、
`Argonne 2016` を裏づける記述は 1 件も見つからなかった。**
⚠️ 🔴 **`Argonne 2016` のフィッシュ・テクニックも見つからなかった。**
**生産者ドメイン配下で Internet Archive が保持している PDF は生涯を通じて 4 件しか無く
（`ARGONNE 2012 NY Times_fr.pdf` / `ch-giraud_esprit-brut.pdf` / `Fiche_hommage.pdf` / `plan.pdf`）、
うちフィッシュ・テクニックは 2 件だけである。**

→ 🔴 ⚠️ **これは「2016 が存在しない」ことの証明ではない。**
**公式サイトのキュヴェ情報は 2023 年頃に消えており、その後にリリースされたミレジムは
そもそも公表される場を失っている。ミレジム一覧の最終更新は 2021 年である。**
→ 🔴 **したがって: 「Argonne 2016 は存在する」も「存在しない」も言ってはならない。**
**言えるのは「メニューにそう書いてある」「造り手はそれを公表していない」の 2 点だけである。**
→ 🔴 **canonical `henri-giraud-argonne-2016` の `description` は
「（Champagne Henri Giraud, Argonne 2016 technical sheet）」と出典を明示するが、
本調査ではその文書を生産者ドメイン上（現行・アーカイブとも）に発見できなかった。** → §Canonical Conflict

---

### 🔴 4 行目 —— `Grand Cru Brut Rosé` 2022（**ROSÉ セクション**）。**canonical の色の軸の gap**

🔍 **intake の生データ**: `source_section = "FRANCE | SPARKLING > CHAMPAGNE | ROSÉ"` /
`source_wine_raw = "Grand Cru Brut Rosé"` / `_parts.label = null` / `_parts.appellation = "rose"` /
`evidence = "'Henri Giraud' の canonical キュヴェ 3 件に一致無し: 'rose'"`。

#### 🔴 ① 公式のロゼは実在する —— **3 本ある**

| キュヴェ | 📄 色の確認 | 📄 造り方（公式の記述） | 📄 ドザージュ |
|---|---|---|---|
| 🔴 **MV Rosé** | 🔴 **`robe œil-de-perdrix`** | 🔴 **`assemblage`。「Henri Giraud の偉大な年と、われわれの名高い `Aÿ Rouge Grand Cru` との…同盟」＋アルゴンヌ樫の小樽での醸造** | ❓ **公式に記載なし** |
| 🔴 **ArG̈onne Rosé** | 🔴 **ロゼ** | 🔴 **`assemblage`。「`ARGONNE 2004` の最良の部分の極端な選別と、Henri Giraud の `red Aÿ Grand Cru` の数リットルとの融合」／2002 年冬に Châtrices の森から造った唯一の小樽／`328 本`** | ❓ **公式に記載なし** |
| 🔴 **Dame-Jane** | 🔴 **「偉大なロゼ・シャンパーニュ」** | 🔴 **テラコッタ／炻器の卵形甕 50 基で醸造・熟成。**⚠️ **ロゼの造り方（saignée / assemblage / macération）は公式が書いていない** | ❓ **公式に記載なし** |

🔴 🏛 **法的な枠組み（INAO cahier des charges「Champagne」第 IX 章 2°-a）——**
「**`Les vins rosés sont élaborés soit à partir de vins de base issus soit de pressurage direct,
soit d'une macération ou d'une saignée, soit par assemblage, avant tirage, de vins blancs et rouges.`**」
→ 🔴 **シャンパーニュでは 4 通りすべてが合法である。**
**したがって「シャンパーニュのロゼはアッサンブラージュ」という一般論を口にしてはならない。**
→ 🔴 **Henri Giraud について公式が明記しているのは、`MV Rosé` と `ArG̈onne Rosé` の 2 本が
アッサンブラージュ（アイ・グラン・クリュの赤を加える）であることだけである。**

#### 🔴 ② 2022 年のロゼは公式に存在しない

⚠️ 🔴 **`2022` を裏づける公式記述は 1 件も無い。**
- 📄 **`ArG̈onne Rosé` として公式が語るのは `ARGONNE 2004 ROSÉ` ただ 1 つで、生産量 328 本。**
- 📄 **`MV Rosé` は Multi Vintage であり、`MV13` と同じ規則に従うなら「2022」は
  **ベース年の 2 桁**（`MV22 Rosé`）である可能性がある。** ⚠️ **だがこれは仮説であり、
  `MV Rosé` にベース年表記が付くことを示す公式資料を、本調査は見つけていない。**
- 📄 **`Dame-Jane` にヴィンテージ表記があるかどうかも公式に記載が無い。**

→ 🔴 **したがって 4 行目にも名前を書かない。候補は 3 本。**
→ 🔴 ⚠️ **「2022 はミレジムではなくベース年かもしれない」という可能性は、
`V-1` 族（Krug Édition / Prévost lot）と同型であり、記録しておく価値がある。**

#### 🔴 ③ canonical 側は「gap」であって「unreachable」ではない —— **`C-4` か `C-6` か**

🔍 **canonical の Henri Giraud レコードは 3 件で、`color` はすべて `Blanc`。**
🔍 **ロゼのレコードは、綴り違い・語順違いを含めて 1 件も存在しない。**
**（`producer` フィールド一致 3 件 / prose-only hit 0 件。全 928 件を走査して確認済み。）**

→ 🔴 **すなわち「レコードは存在するが識別子の綴りが違って当たらない」という `unreachable` ではない。**
**受け皿そのものが無い、純然たる gap である。**
→ 🔴 **標準指針（Batch 8–10 の caution ④）に従い、これは conflict として登録しない。gap として記録する。**

🔴 **`C-6` か `C-4` かという問い（タスクの指定）への回答:**

| 族 | 該当するか | 理由 |
|---|---|---|
| ⚠️ **`C-6`**（1 レコードが 2 色を兼ねる形として Taittinger で提起された） | ❌ **該当しない** | 🔴 **Batch 10 が実測したとおり、matcher はメニューのセクション見出しを読んでいない。**<br>🔴 **本行の intake evidence が使った照合キーは `'rose'` であり、これは `_parts.appellation` から来ている。`source_section` の `… \| ROSÉ` は照合に一切使われていない。**<br>🔴 **かつ canonical には「2 色を兼ねる 1 レコード」が存在しない（ロゼのレコードが 0 件）。したがって `C-6` の前提が成立しない。** |
| 🔴 **`C-4`** | ✅ **該当する** | 🔴 **`Grand Cru Brut Rosé` は格付語＋ドザージュ区分＋色の 3 語だけで構成され、生産者もキュヴェも特定しない。**<br>🔴 **`C-4` の定義「名前がスタイル語のみで構成され、その生産者を特定する語を 1 つも含まない」に文字どおり当てはまる。**<br>🔴 **2 行目 `Grand Cru Brut` も同じく `C-4`。**<br>🔴 **すなわち本生産者は `C-4` の実害を 4 行中 2 行（50%）で受けている。** |
| 🔴 **加えて gap** | ✅ | **`C-4` は「当てる先が特定できない」問題だが、本行はそれ以前に「当てる先が無い」。2 つが重なっている。** |

---

## Staff Notes

### 芯 3 点（**これだけ言えば外さない**）

**① 🔴 「アイ・グラン・クリュ 1 村と、アルゴンヌの森の樫。テロワールが 2 つあるメゾンです。」**
📄 **造り手自身の言葉 —— 「樫はブドウ樹と同じように自らのテロワールを担う。
だがブドウ樹が毎年ワインを与えるのに対し、森は樹齢 200 年の樫を、その生涯に一度しか与えない。」**
🏛 **アイのグラン・クリュ格は INAO の cahier des charges に根拠がある（`grand cru` を名乗れる 17 コミューンの 1 つ）。**
📄 **1950 年まで、シャンパーニュのワインはすべて樫樽で造られ、その 90% がアルゴンヌの樽だった。
それが忘れられ、このメゾンが 1990 年に呼び戻した。**

**② 🔴 「ステンレスを使いません。器は樫樽か、テラコッタ／炻器の甕だけです。」**
📄 **公式の言い方: 「`Sans inox` かつ最小限の介入と硫黄で」「`0% STAINLESS STEEL`」。**
📄 **起点は **2015 年**。「25 年後にして、われわれのワインはアルゴンヌの樫樽か炻器の甕でしか醸造されない。」**
📄 **皮肉なことに、1990 年にシャンパーニュ地方で最初のサーモレギュレーテッド・ステンレスタンクを
入れたのもこのメゾンである。「経験が、われわれの最も偉大なワインは樫樽のワインだと示した」ので捨てた。**

**③ 🔴 「`MV` は `Multi Vintage`。ミレジムではありません。」**
📄 **「`MV, comme Multi Vintage.`」「`Colonne vertébrale de notre collection`」**
📄 **`Fût de Chêne` は MV の別名ではなく、MV の 3 つの識別標の 1 つ。1990 年から続く。**
📄 **`永久リザーヴ`（1990 年のヴィンテージに始まり、以後の収穫ごとに養われる）が MV の背骨。**
🔴 **したがって `MV17` の「17」を「2017 年ヴィンテージ」と説明してはならない。**

### ⚠️ 言ってはいけないこと（**このドシエは薄い。だからこのリストは長い**）

**① 🔴 「1625 年創業のメゾンです」—— 言ってはならない。**
📄 **公式が書くのは「1625 年に**アイで生まれた** `François Hémart` が、Giraud-Hémart 家の祖であり
ヴィニュロンだった」であり、これは**創業年ではなく祖の生年**である。**
📄 **公式の言い方は一貫して「起源は 17 世紀に遡る」。**
🏛 **法人としての設立は 1975 年。**
→ **安全な言い方: 「一族は 17 世紀からアイでブドウを作っています。」**

**② 🔴 「12 代目です」／「13 代目です」—— どちらも断定してはならない。**
📄 **公式は `Hommage/Famille` 頁で「12 世代」、`Argonne/Parcelle Miraculeuse` 頁で「13 générations」と書く。**
→ **安全な言い方: 「何世代も続く家族経営です。」**

**③ 🔴 「当主はクロード・ジローです」—— 現在形で言ってはならない。**
🏛 **現在の `dirigeants` は Emmanuelle Giraud-Patour（会長）と Sébastien Le Golvet（社長）。
`Claude Giraud` は登録上の役員に含まれていない。**
📄 **`Claude Giraud` は 2017 年の「No pesticide」表明の主体として公式に登場する（過去の文脈）。**
→ **安全な言い方: 「現在は Emmanuelle Giraud-Patour が会長、Sébastien Le Golvet が社長兼醸造長です。」
（この 2 人はいずれも公的登録と公式サイトの両方で裏が取れている。）**

**④ 🔴 「オーガニックのシャンパーニュです」—— 言ってはならない。**
🏛 **Agence Bio 上の生産状態は 2025 年基準で `C2`（有機転換 2 年目）であり、`AB`（認証取得済み）ではない。**
🏛 **かつ登録されている活動は `Production`（栽培）のみで、`Préparation`（醸造）は登録されていない。**
🏛 **OBP の 2 ヴィンテージ（2016 / 2022）はいずれも現行の関与開始（2024-10-07）より前である。**
**🔴 同時に「有機の登録はありません」も言ってはならない** —— `numeroBio 121737`、認証機関 `Ocacia`、
状態 `ENGAGEE` は実在する。
→ **安全な言い方: 「畑を有機に転換中で、公的登録上は転換 2 年目です。まだ認証取得済みではありません。」**

**⑤ 🔴 「HVE 認証を取っています」—— 断定してはならない。**
⚠️ **canonical は 2 レコードで HVE / VDC を断定するが、公式サイト（現行・アーカイブとも）に
その語が 1 度も現れず、本調査では裏づけが取れなかった。**
→ **安全な言い方: 「環境への姿勢は強く打ち出していますが、認証名は team に確認中です。」**

**⑥ 🔴 「Argonne 2016 は…」と造り手の言葉として語ってはならない。**
⚠️ **公式が列挙するミレジムは 2002 / 2004 / 2008 / 2011 で、公式のキュヴェ情報は 2023 年頃に消えている。
2016 のフィッシュ・テクニックは存在を確認できていない。**
→ **安全な言い方: 「Argonne は選ばれた年にだけ造られるトップ・キュヴェです。
このヴィンテージの詳細スペックは造り手が公表していません。」**

**⑦ 🔴 ドザージュの数値を言ってはならない。**
🔴 **全キュヴェについて、公式資料に g/L の記載が 1 件も存在しない。**
🔴 **canonical `giraud-fut-de-chene` の `Brut — 7 g/L` は、本調査では裏づけが取れなかった。**

**⑧ 🔴 OBP 4 本のセパージュ比率を言ってはならない。**
🔴 **`70% PN / 30% Ch` は `Hommage` と `Esprit de Giraud` のフィッシュの値であって、OBP の 4 本の値ではない。**
🔴 **canonical の「PN 90% / Ch 10%」（Fût de Chêne）と「PN 80% / Ch 20%」（Esprit Nature）は
いずれも本調査で裏づけが取れなかった。**
→ **安全な言い方: 「ピノ・ノワール主体にシャルドネ。品種はこの 2 つだけです。」
（📄 公式「Pinots Noirs と Chardonnay は高貴な素材の核心においてのみその姿を現す」に依拠。）**

**⑨ 🔴 マロラクティック発酵の有無を言ってはならない。**
🔴 **公式資料に MLF への言及が 1 件も無い。canonical `giraud-fut-de-chene` の「マロラクティック発酵あり」は
裏づけが取れなかった。**

**⑩ 🔴 「自社畑 5.67 ha」「年産 25 万本」「樽は 400L」を言ってはならない。**
🔴 **いずれも canonical にあるが、公式にも公的登録にも裏づけが無い。**
**公式が数字で書いているのは「毎年 8,000 本の樫の植樹に出資」「樽は 5 年働く」「甕は 50 基」
「Argonne Rosé は 328 本」の 4 つだけである。**

**⑪ 🔴 `Esprit Nature` を「ブリュット・ナチュール（ノンドゼ）」と説明してはならない。**
🔴 **メニューは `Brut Nature`、canonical は `Brut`、造り手はどちらも書いていない。**
→ **安全な言い方: 「`Esprit Nature` というキュヴェ名です。ドザージュは造り手が公表していません。」**

**⑫ 🔴 `Manoir Henri Giraud` を「別のメゾン」と説明してはならない。**
🏛 **同一 SIREN（303891048）の第 2 事業所（SIRET …0025、NAF 55.10Z）であり、宿泊・オエノツーリズム部門である。**

**⑬ 🔴 `champagnegiraud.com`（ハイフン無し）を公式サイトとして案内してはならない。**
🏛 **Afternic のパーキング DNS に載った売り出し中ドメインである。公式は `champagne-giraud.com`（ハイフン有り）。**

**⑭ 🔴 「シャンパーニュのロゼはアッサンブラージュです」と一般論で言ってはならない。**
🏛 **INAO の cahier des charges は `pressurage direct` / `macération` / `saignée` / `assemblage` の 4 通りを認めている。**
🔴 **Henri Giraud について公式が明記しているのは `MV Rosé` と `ArG̈onne Rosé` の 2 本がアッサンブラージュ
（アイ・グラン・クリュの赤を加える）であることだけで、`Dame-Jane` の方法は公表されていない。**

### 🔴 追加の一手（**客に喜ばれる、かつ全部公式で裏が取れている**）

- 📄 **「この蔵の樫樽は 5 年働いたあと、日本へ渡って日本酒の仕込みに再利用されます。」**
  （公式の原文: 「they continue to whisper songs of their terroir to Japan where they are reused to elaborate the sake」）
- 📄 **「アルゴンヌの森の樫は、1 本ずつ位置情報を付けて選ばれます。樽板はそば粉で接がれる —— グルテンを残さないためです。」**
- 📄 **「Dom Pérignon はアルゴンヌの森の中心、Sainte-Menehould の生まれです。この蔵はそこから樽材を取っています。」**
- 📄 **「`Dame-Jane` という名前は、シルクロードの街 `Dâmghân` が `Damajana` を経て 1614 年にフランス語になったものです。」**
- 📄 **「アイの白亜は場所によって 200 m の厚さがあり、その上をわずか 20 cm の土が覆うだけです。爪で傷がつくほど柔らかい。」**
- 🏛 **「アイが `Grand Cru` を名乗れるのは、AOC シャンパーニュの法文が 17 のコミューンを列挙していて、
  その中にアイが入っているからです。」**

### 🔴 物理ラベル確認タスク（**オンラインの一次資料では決着しない。現物が要る**）

**① 🔴 OBP 2 行目（`Grand Cru Brut` / NV / $800）—— ボトルのラベルを見て、
`MV` / `Hommage` / `Blanc de Craie` のどれかを確定する。`MV` の場合は数字（`MV17` 等）も控える。**
**② 🔴 OBP 4 行目（`Grand Cru Brut Rosé` / 2022 / $735）—— ボトルのラベルを見て、
`MV Rosé` / `Dame-Jane` / `ArG̈onne Rosé` のどれかを確定する。**
🔴 **とくに「2022」がラベル上で `MILLÉSIME 2022` と書かれているのか、`MV22` のような
ベース年表記なのかを必ず確認すること。この 1 点で `V-1` 族か通常のミレジムかが決まる。**
**③ 🔴 OBP 1 行目 —— `Esprit Nature` のバックラベルに `Brut Nature` の表示があるかを確認する。
（`Esprit Nature` には QR コードのバックラベルがあるはずで、そこに分析値が載っている可能性がある。）**
**④ 🔴 OBP 3 行目 —— `Argonne` のラベルに `2016` の表示があるか、
およびボトルに個体番号が刻まれているかを確認する。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔒 **本節は escalation のみである。`REGISTER.md` は一切書き換えていない。番号の採否は CTO の判断である。**

### 🔍 canonical の 3 レコード（走査結果）

🔍 **全 928 件を走査。`giraud` に一致したのは 3 件で、3 件とも `producer` フィールドでの一致。
他生産者の散文に名前が現れただけの prose-only hit は 0 件。**
（`D-2026-08-05-08` の部分文字列一致の defect は、本生産者では発生していない。）

| id | name | vintage | color | classification |
|---|---|---|---|---|
| `giraud-fut-de-chene` | `Fût de Chêne MV17 Grand Cru` | `NV` | `Blanc` | `Grand Cru Brut` |
| `henri-giraud-esprit-nature` | `Esprit Nature` | `NV` | `Blanc` | `Brut` |
| `henri-giraud-argonne-2016` | `Argonne Aÿ Grand Cru` | `2016` | `Blanc` | `Aÿ Grand Cru — Brut Millésimé` |

---

### 🔴 A. 既存の族に該当するもの

#### 🔴 A-1. `C-4` 族 —— 識別語を持たないキュヴェ名。**OBP 4 行中 2 行（50%）**

🔴 **2 行目 `Grand Cru Brut` と 4 行目 `Grand Cru Brut Rosé` は、いずれも
格付語＋ドザージュ区分（＋色）だけで構成され、生産者もキュヴェも特定する語を 1 語も含まない。**
🔴 **`C-4` の定義に文字どおり該当する。**
🔴 **加えて `giraud-fut-de-chene` の `classification` も `Grand Cru Brut` であり、canonical 側も同じ形を持っている。**

⚠️ 🔴 **ただし Batch 10 の caution ② に従い、「メニュー側が category 語をキュヴェ名として印字した」型
（Grgich `'Estate,'` / Mayacamas `Red Wine` / Harlan `Proprietary Blend` / Abreu `Cabernet Sauvignon`）
と同一視してはならない。**
🔴 **本件は「メニューがキュヴェ名を印字していない」のであって、
「category 語をキュヴェ名として印字した」のではない。`_parts.label` は `null` である。**
🔴 **`Argonne` と `Esprit Nature` の 2 行ではメニューは正しくキュヴェ名を印字している。
すなわち同じメニューの同じ生産者の中で、印字の粒度が 2 段階に割れている。**

#### 🔴 A-2. `V-1` 族 —— `MV` のベース年が層をまたぐ。**Krug `Édition` と同型**

🔴 📄 **公式: 「`MV, comme Multi Vintage.`」／公式のキュヴェ頁のタイトルは `MV13`。**
🔍 **canonical: `id = giraud-fut-de-chene` / `name = "Fût de Chêne MV17 Grand Cru"` / `vintage = "NV"`。**

🔴 **問題は 3 つある。**
1. 🔴 **`MV17` は appellation 上 NV だが、`MV13` とは別のワインである。
   両者を区別する識別子は「17」「13」の 2 桁しかない。`(cuvée, vintage)` が一意でない。**
   → **`V-1`（Krug `162ème〜173ème Édition`）と完全に同型。**
2. 🔴 **canonical の **id に MV 番号が入っていない**。`giraud-fut-de-chene` は
   `MV18` が来た瞬間に衝突する。`name` にだけ `MV17` があり、id は世代非依存になっていない。**
   → 🔴 **これは Batch 10 が Grand Siècle で観測した「`V-1` に surrogate key が無い」問題の再現である。**
3. 🔴 **canonical は `Fût de Chêne` を cuvée 名として持つが、公式では
   `Fût de Chêne` は **MV のマーカーの 1 つ**（`mv-mark-01-fut-de-chene`）であって、
   現行のキュヴェ名は `MV` である。すなわち canonical は旧称を canonical 名として保持している。**
   ⚠️ **Billecart-Salmon の `Brut Réserve → Le Réserve` と同じ「改称の過渡期」型だが、
   Billecart では公式が両表記を併存させていたのに対し、こちらは公式が現行表記を撤去してしまっている
   （サイトが空になった）ため、確認手段が Internet Archive しかない。**

---

### 🔴 B. gap（conflict ではない）—— **登録しない。gap として記録する**

#### 🔴 B-1. **ロゼのレコードが 1 件も存在しない（色の軸の gap）**

📄 **公式レンジのロゼは `MV Rosé` / `ArG̈onne Rosé` / `Dame-Jane` の 3 本。**
🔍 **canonical の 3 レコードは `color` がすべて `Blanc`。ロゼは 0 件。**
🔴 **綴り違いによる `unreachable` ではなく、受け皿が無い純然たる gap である。**
🔴 **Batch 8–10 の caution ④ に従い、conflict として登録しない。**

#### 🔴 B-2. **公式レンジ 8 本のうち 5 本が canonical に存在しない**

| 公式のキュヴェ | canonical |
|---|---|
| `Esprit Nature` | ✅ `henri-giraud-esprit-nature` |
| `MV`（＝`Fût de Chêne`） | ⚠️ `giraud-fut-de-chene`（旧称で保持） |
| `ArG̈onne` | ✅ `henri-giraud-argonne-2016` |
| 🔴 `MV Rosé` | ❌ **gap** |
| 🔴 `ArG̈onne Rosé` | ❌ **gap** |
| 🔴 `Dame-Jane` | ❌ **gap** |
| 🔴 `Hommage` | ❌ **gap** |
| 🔴 `Blanc de Craie` | ❌ **gap** |

🔴 **とくに `Hommage` と `Blanc de Craie` の欠落は、OBP 2 行目を解決不能にしている直接の原因の一部である
（候補 3 本のうち 2 本が canonical に存在しない）。**

---

### 🔴 C. canonical の格納値と公式の食い違い —— **10/10 の base rate が 11 例目でも成立**

🔴 **Batch 8–10 の caution ① が本生産者でも再現した。`typed field` にも及んでいる。**

| # | canonical | 格納値 | 📄 公式 / 🏛 登録 | 判定 |
|---|---|---|---|---|
| **C-a** | `giraud-fut-de-chene.dosage` | 🔴 **`Brut — 7 g/L`** | ❓ **全キュヴェについてドザージュの g/L 値が公式に 1 件も存在しない** | 🔴 **裏づけ無し（typed field）** |
| **C-b** | `giraud-fut-de-chene.grapes` | 🔴 **`Pinot Noir ~90%` / `Chardonnay ~10%`** | ❓ **公式に比率の記載が無い** | 🔴 **裏づけ無し（typed field）** |
| **C-c** | `giraud-fut-de-chene.aging` | 🔴 **`36+ months sur lie`** | ❓ **公式に月数の記載が無い** | 🔴 **裏づけ無し（typed field）** |
| **C-d** | `giraud-fut-de-chene.winemaking` | 🔴 **「アルゴンヌ産の小樽（`400L`）」「マロラクティック発酵あり」** | ❓ **公式に樽容量の記載が無い／MLF への言及が 1 件も無い** | 🔴 **裏づけ無し** |
| **C-e** | `giraud-fut-de-chene.name` | **`Fût de Chêne MV17 Grand Cru`** | 📄 **公式の現行キュヴェ名は `MV`。`Fût de Chêne` はそのマーカー** | ⚠️ **旧称の保持（A-2 参照）** |
| **C-f** | `henri-giraud-esprit-nature.grapes/description` | 🔴 **「ピノ・ノワール 80%、シャルドネ 20%」** | ❓ **公式に比率の記載が無い。**📄 **最も近い公式値は `Hommage` と `Esprit de Giraud` の `70/30`** | 🔴 **裏づけ無し** |
| **C-g** | `henri-giraud-esprit-nature.description` | 🔴 **「`2016 年`の『ステンレス・ゼロ』転換」** | 🔴 📄 **公式は `Since 2015`** | 🔴 **1 年ずれる** |
| **C-h** | `henri-giraud-esprit-nature.description` | 🔴 **「永久リザーヴのワインを `3 分の 1` 加え」** | ❓ **公式は永久リザーヴの比率を書いていない** | 🔴 **裏づけ無し** |
| **C-i** | `henri-giraud-esprit-nature.aging` | 🔴 **`24+ months sur lie（最低2年）`** | ❓ **公式に月数の記載が無い。**🏛 **なお INAO の法定最低は NV で `15 ヶ月`（tirage から）** | 🔴 **裏づけ無し（typed field）** |
| **C-j** | `henri-giraud-esprit-nature.description` | 🔴 **「1625 年からアイ村に根を張る」「当主クロード・ジローは 12 代目」** | 🔴 📄 **1625 は `François Hémart` の**生年**。**🏛 **`Claude Giraud` は現在の役員一覧に無い。**📄 **世代数は公式内で 12 と 13 に割れる** | 🔴 **3 点とも要修正** |
| **C-k** | `henri-giraud-esprit-nature.terroir/obp_note` | 🔴 **「HVE および Viticulture Durable en Champagne の認証を取得」** | ⚠️ **公式（現行・アーカイブとも）に該当語が 1 度も現れない** | 🔴 **裏づけ無し** |
| **C-l** | `henri-giraud-argonne-2016.winemaking/obp_note` | 🔴 **「畑は HVE 認証」** | ⚠️ **同上** | 🔴 **裏づけ無し** |
| **C-m** | `henri-giraud-argonne-2016.obp_note` | 🔴 **「自社畑は `5.67ha`、年産は約 `25 万本`」** | ❓ **公式にも公的登録にも記載が無い** | 🔴 **裏づけ無し** |
| **C-n** | `henri-giraud-argonne-2016.description` | 🔴 **「（`Argonne 2016 technical sheet`）」という出典明示** | ⚠️ 🔴 **生産者ドメイン上（現行・Internet Archive とも）に該当文書を発見できなかった。アーカイブに残る同ドメインの PDF は生涯 4 件で、フィッシュは `Fiche_hommage` と `ch-giraud_esprit-brut` の 2 件のみ** | 🔴 **出典を確認できず** |
| **C-o** | `henri-giraud-argonne-2016.description` | 🔴 **「ボトルは一本ずつ番号が刻まれる」** | ⚠️ **公式が「1 本ずつ手で彫る」と書くのは `MV Rosé` の flacon（ダイヤ彫り＋ピンクゴールドの agrafe）であって、`Argonne` の個体番号ではない** | ⚠️ **要検証** |
| **C-p** | `henri-giraud-esprit-nature.subregion/terroir` | 🔴 **「Aÿ Grand Cru — `Grande Vallée de la Marne`」「公式にはグランド・ヴァレ・ド・ラ・マルヌに属する（モンターニュ・ド・ランスではない）」** | ⚠️ 🏛 **INAO の cahier des charges にこの下位区分の概念が無い。公式サイトにも現れない** | ⚠️ **一次資料で裏づけられず** |
| **C-q** | `henri-giraud-esprit-nature.obp_note` | 🔴 **「市場価格帯はおよそ `$70〜95`」** | ⚠️ **OBP は同キュヴェを `$250` で提供している。canonical が価格帯を持つこと自体が層の逸脱** | ⚠️ **記録のみ** |

🔴 **要約: 3 レコードのうち 3 件すべてが公式と食い違う値を持つ。
うち **`dosage` / `grapes` / `aging` という typed field が 5 件**含まれる。**

---

### 🔴 D. 未採番の形（**番号は付けない。CTO の判断**）

#### 🔴 D-1. **`match_state = exact` がドザージュ区分の矛盾を内包している**

🔍 **1 行目は `match_state: exact` / `confidence: 1.0` である。**
🔍 **しかしメニューは `Brut Nature`、canonical の `classification` は `Brut`。**
🔍 **intake の evidence 3 行は「生産者トークン一致」「名称トークン一致」「vintage NV 実在」だけで、
`_parts.style = "brut nature"` と canonical の `classification` を照合した形跡が無い。**
→ 🔴 **`exact` は「キュヴェ名が一致した」以上のことを保証しない。
ドザージュ軸は照合対象に入っていない。**
→ 🔴 **これは `C-4` とも `V-1` とも異なる新しい形である。「exact の意味論が未定義」という
メタデータ規約の問題であり、`S-2` に近いが同一ではない。**

#### 🔴 D-2. **同一生産者の 2 行で、matcher のキュヴェ候補抽出が別のフィールドから来ている**

| 行 | `_parts.label` | 使われた照合キー | 由来 |
|---|---|---|---|
| 2 行目 | `null` | **`'Grand Cru Brut'`** | 🔴 **`_parts.printed_rest`** |
| 4 行目 | `null` | **`'rose'`** | 🔴 **`_parts.appellation`** |

🔴 **どちらも `label` が `null` という同じ状況にありながら、フォールバック先が異なる。**
🔴 **4 行目は `Grand Cru Brut Rosé` という 3 語のうち、色の 1 語だけを小文字化して照合キーにしている。**
→ 🔴 **matcher のフォールバック順序が決定論的でないか、`appellation` の判定が
`Rosé` を「appellation」として誤って埋めている。**
→ 🔴 **加えて、これは Batch 10 の「matcher は節見出しを読んでいない」の再確認でもある。
`source_section` に `ROSÉ` が明示されているにもかかわらず、
matcher はそれを使わず `_parts.appellation` から `'rose'` を取っている。**

#### 🔴 D-3. **生産者が自らの公表を停止した場合、canonical の検証可能性が失われる**

🔴 **本生産者は 2023 年頃に公式サイトからキュヴェ情報を全撤去した。**
🔴 **その結果、canonical の 3 レコードのどの値も、稼働中の一次資料では検証できない。**
🔴 **Internet Archive を使わなければ、本ドシエは 30% にも届かなかった。**
→ 🔴 **「生産者が沈黙した」という状態を、canonical のどのフィールドも表現できない。
`obp_note` は 2 レコードとも、あたかも公式が現在も公表しているかのように書かれている。**
→ 🔴 **これはデータの誤りではなく、**モデルに「情報源の生存状態」の軸が無い**という問題である。**

---

## Sources

### ✅ 生産者自身のドメイン（現在稼働中）

| URL | 取得 | 内容 |
|---|---|---|
| `https://champagne-giraud.com/` | **HTTP 200 / 171,393 bytes** | 🔴 **splash 頁。連絡先と年齢自己申告のみ。キュヴェ情報ゼロ** |
| `https://champagne-giraud.com/robots.txt` | **200** | **`Sitemap: https://champagne-giraud.com/wp-sitemap.xml`** |
| `https://champagne-giraud.com/wp-sitemap-posts-page-1.xml` | **200** | 🔴 **公開頁 8 件のみ** |
| `https://champagne-giraud.com/wp-json/wp/v2/pages?per_page=50` | **200** | 🔴 **固定頁 8 件（sitemap と一致）** |
| `https://champagne-giraud.com/wp-json/wp/v2/media?per_page=100` | **200** | 🔴 **65 件。PDF は 4 件のみ、すべて 2025 年のイベント進行表。フィッシュ・テクニックは 0 件** |
| `https://champagne-giraud.com/mentions-legales/` | **200** | 🔴 **SIREN 303891048 / RCS Reims B 303891048 / 資本金 349 725 € / TVA FR32303891048 / Directeur de la publication: Emmanuelle Giraud-Patour / Hébergeur: O2Switch** |
| `…/wp-content/uploads/2025/06/2025_09_06_Program_ENG.pdf` ほか 3 件 | **200 / `application/pdf`（`%PDF-1.6` を確認）** | ✅ **2025-06-10 のドメーヌ開放イベント進行表。`Barrel toasting workshop by the Tonnellerie de Champagne` / `Belvédère` / `Pressoria` / `Gala Dinner orchestrated by Philippe Mille`** |
| `https://www.manoir-henri-giraud.com/fr/` | **200** | ✅ **同一 SIREN の宿泊事業所。`83 boulevard Charles de Gaulle, 51160 Aÿ`／`Hébergement touristique N°51030000010AF`／「la maison Henri Giraud travaille la vigne depuis le 17ème siècle」** |
| `https://boutique.champagne-giraud.com/` | **200 / 1,215 bytes** | ⚠️ **`noindex, nofollow` の旧「トンネル」頁。リンク先が下記の不合格ドメインを指す** |

### 📄 生産者自身が書いた頁（**Internet Archive 経由。現在は生産者ドメインから配信されていない**）

⚠️ 🔴 **本ドシエのキュヴェ記述はこの層に依存している。**
**いずれも生産者自身の HTML であることを、各頁のフッターに埋め込まれた
`Champagne Henri Giraud / 71 Boulevard Charles de Gaulle - 51160 Ay - FRANCE / Tél. : 03 26 55 18 55`
という mentions légales で確認している（＝ ✅ で確認した現行 mentions légales の住所・電話と一致）。**

| URL（原本） | 捕捉日 | 内容 |
|---|---|---|
| `/fr/champagne/les-experiences-champagne` | **2022-01-21** | 🔴 **レンジ全 8 本の自己列挙＋「`Sans inox`」「Pinots Noirs et Chardonnay」「Fût de chêne d'Argonne, terre cuite ou Grès」** |
| `/fr/les-experiences/mv.html` ／ `/en/champagne/mv13-2` | **2019-12-14 / 2021-07-27** | 🔴 **`MV, comme Multi Vintage.`／`la cuvée Fût de Chêne … depuis 1990`／`Colonne vertébrale de notre collection`** |
| `/en/marker-anglais/mv-mark-01-fut-de-chene` | **2021-09-24** | 🔴 **1950 年まで全量樫樽・うち 90% がアルゴンヌ／ONF と年 8,000 本の植樹／樽板はそば粉で接ぐ／樽は 5 年働いたのち日本で日本酒に再利用** |
| `/en/marker-anglais/mv-mark-02-reserve-perpetuelle` | **2021-09-24** | 🔴 **永久リザーヴは 1990 年のヴィンテージに始まる** |
| `/en/marker-anglais/mv-mark-03-ay-grand-cru` | **2021-10-20** | **アイ・グラン・クリュの散文（`Valnon coast`）** |
| `/fr/les-experiences/argonne.html` ／ `/en/champagne/argonne-3` | **2019-12-14 / 2021-07-27** | 🔴 **`la belle et la bête`／`Seuls de très grands millésimes`／Sébastien Le Golvet = Chef de Cave** |
| `/en/marker-anglais/argonne-mark-03-argonne` | **2021-10-20** | 🔴 **`G` のトレマ＝`Aÿ Grand Cru`／`Châtrices` 区画・`gaize` 土壌／`Valnon` の小さなピノ／黒鉛の香り** |
| `/en/marker-anglais/argonne-mark-04-agrafe`（＝ Parcelle Miraculeuse） ／ `/fr/les-experiences/argonne/parcelle-miraculeuse.html` | **2021-09-24 / 2022-08-10** | 🔴 **`La Valnon`／`côte Châtillon`／1952・1954 の逸話／`Léon Giraud` のマッサル選抜／`La Croix-Courcelles` のシャルドネ／`13 générations`** |
| `/en/marker-anglais/argonne-marqueur-millesimes` | **2021-09-24** | 🔴 **公式が列挙するミレジムは `2002` / `2004` / `2008` / `2011` の 4 つ。`2016` は無い** |
| `/en/champagne/argonne-rose-2` ＋ marker 01–03 | **2021-07-27 / 09-24** | 🔴 **`ARGONNE 2004 ROSÉ`／2002 年冬の Châtrices の唯一の小樽／Aÿ Grand Cru の赤とのアッサンブラージュ／`328 本`／金細工師 `Uwe Schäfer`** |
| `/fr/les-experiences/mv13-rosé.html` ＋ marker 01–03 | **2019-12-14 / 2021-09-24** | 🔴 **`robe œil-de-perdrix`／アルゴンヌ小樽での醸造／`Aÿ Rouge Grand Cru` とのアッサンブラージュ／ダイヤ彫り＋24 金ピンクゴールドの agrafe** |
| `/en/champagne/dame-jane-2` ＋ marker 01–03 | **2021-07-27 / 09-24** | 🔴 **テラコッタ→炻器を 10 年試験／`Since 2015` 樫樽か炻器の甕のみ／`50 amphorae`／`Dâmghân → Damajana → Dame-Jane（1614）`** |
| `/fr/les-experiences/esprit-nature.html` ／ `/en/champagne/esprit-nature-3` ＋ marker 01–04 | **2019-12-14 / 2021-07-27 / 09-24** | 🔴 **`Pailleté de beaux amers minéraux`／2017 年末の「No pesticide」／QR コードによる分子分析の開示／Claude Giraud の一人称／`Paper Tree`（Claudine DIVRY）／ONF** |
| `/en/champagne/hommage-2` ＋ marker 01–03 | **2021-07-27 / 09-24** | 🔴 **`François Hémart (1625–1705)`／`Né à Aÿ en 1625`／`the 12 generations`／2015-07-04 の UNESCO 登録** |
| `/en/champagne/blanc-de-craie-2` ＋ marker 01–02 ／ `/fr/les-experiences/blanc-de-craie/craie.html` | **2021-07-27 / 09-24 / 2022-06-27** | 🔴 **アイの白亜（7 千万年前・200 m・20 cm・Dali の引用）／`0% STAINLESS STEEL`** |
| 📄 **`/champagne/cuvees/pdf/Fiche_hommage.pdf`** | **2015-12-11 捕捉** | 🔴 **`%PDF-1.5` を確認。`Hommage - Aÿ Grand Cru`／`70% Pinot Noir, 30% Chardonnay, exclusivement cueillis sur le terroir d'Aÿ`／`Vinification en cuve thermorégulée et élevage 6 mois en petits fûts de chêne`／提供温度 12° と 8°** |
| ⚠️ 📄 **`/champagne/cuvees/pdf/ch-giraud_esprit-brut.pdf`** | **2010-06-12 捕捉** | 🔴 **`%PDF-1.4` を確認。`Esprit de Giraud`（`Esprit Nature` ではない）／`70% Pinot Noir 30% Chardonnay`／`Vinification thermorégulée en cuve inox durant une année sans soutirage sur lie entière`**<br>⚠️ **`Dégustation` の署名は外部の `Franck Wolfert - Vins & Atmosphères`。メゾン自身の官能表現ではない** |
| 🏛 **CDX 走査（`matchType=domain`, `from=2018`, 600 件）** | — | 🔴 **生産者ドメイン配下で Internet Archive が保持する PDF は生涯 4 件のみ（上記 2 件＋`ARGONNE 2012 NY Times_fr.pdf`＋`plan.pdf`）。`Argonne 2016` のフィッシュは存在しない** |

### 🏛 公的登録・規制一次資料

| 出典 | 取得 | 内容 |
|---|---|---|
| **`recherche-entreprises.api.gouv.fr/search?q=henri+giraud+champagne`** | **200** | 🔴 **SIREN `303891048`／SIRET 本店 `30389104800017`（NAF `01.21Z`）／第 2 事業所 `30389104800025`（NAF `55.10Z`）／`date_creation 1975-01-01`／役員 4 名＋会計監査人 2 社／`liste_id_bio: [121737]`／`liste_idcc: ["0493"]`** |
| **`opendata.agencebio.org/api/gouv/operateurs/?numeroBio=121737`** | **200** | 🔴 **`Ocacia` `FR-BIO-20`／`ENGAGEE`／`Raisin de cuve` `C2` 2025／`activites: [Production]`／`mixite: "Non"`／`datePremierEngagement 2014-10-06`／`dateEngagement 2024-10-07`／`siteWebs` に公式サイトを `Site Officiel` として登録** |
| **`extranet.inao.gouv.fr/fichier/PNOCDCChampagne.pdf`** | **200 / `application/pdf`（`%PDF` 確認）／244,863 bytes** | 🔴 **AOC「Champagne」cahier des charges（2015-11-05 の全国異議申立手続版）。`Ay` を含む grand cru 17 コミューン／`rendement 12 400 kg/ha`・`butoir 15 500 kg/ha`・`charge maximale 19 700 kg/ha`／圧搾 `102 L / 160 kg`／ロゼ 4 方式／`dégorgement` は tirage から 12 ヶ月以降／熟成最低 NV `15 ヶ月`・millésimé `36 ヶ月`／millésimé はその年の量の 80% 以下**<br>⚠️ **これは「異議申立手続版」であり、最終的な統合版とは異なりうる。** |
| **WHOIS `champagne-giraud.com`** | — | **`Creation Date 2003-04-18` / Registrar `OVH sas` / NS `dns12.ovh.net`, `ns12.ovh.net`** |
| **WHOIS `champagnegiraud.com`** | — | 🔴 **`Creation Date 2016-06-25` / Registrar `Dynadot Inc` / NS `NS1.AFTERNIC.COM`, `NS2.AFTERNIC.COM` → 売り出し中ドメイン** |
| **DNS `henri-giraud.com`** | — | 🔴 **A も MX も返らない（NXDOMAIN）。絶対的不在の証明** |
| **DNS `champagne-giraud.com` / `manoir-henri-giraud.com`** | — | **A `109.234.164.179` / `78.40.11.128`、いずれも MX は `mail.ovh.net` 系** |

### 🔍 THÉSEUS 内部

| 出典 | 内容 |
|---|---|
| **`~/Desktop/obp_intake_20260804/obp_intake_normalized_20260804.json`**（全 704 行） | 🔍 **`Henri Giraud` の 4 行を `source_row_id` 単位で取得（`c80473a870` / `545526f301` / `4b63eaafe7` / `47dbbddcc6`）。`_parts` と `evidence` を原文で確認** |
| **`migration/out/export/db_wine_canonical.json`**（928 件） | 🔍 **Python で読み取りのみ。`producer` フィールド一致 3 件 / prose-only hit 0 件を確認** |
| **`research/canonical_conflicts/REGISTER.md`** | 🔍 **`C-4` / `V-1` / `S-2` の定義を読み取りのみ。書き換えていない** |

### ❌ 拒絶した情報源

| 情報源 | 拒絶理由 |
|---|---|
| 🔴 **`champagnegiraud.com`（ハイフン無し）** | 🔴 **Afternic のパーキング DNS に載った売り出し中ドメイン。本文 114 バイト。生産者との関係を示すものが 1 つも無い。1 語も使用していない** |
| **`boutique.champagnegiraud.com`** | **上記ドメイン配下。TLS ハンドシェイクが `unrecognized name` で失敗。接続していない** |
| **Wikipedia / 販売店 / オークション / 評論家サイト / Vivino / CellarTracker / Wine-Searcher / 輸入元資料** | **briefing §1 により全面禁止。1 件も参照していない** |
| **TTB Public COLA Registry** | **briefing §1 により米国生産者専用。本生産者はフランス法人のため使用しなかった（gated ではない。適用外）** |

---

## Confidence

| 節 | 判定 | 根拠 |
|---|---|---|
| **Identity** | 🔴 **High** | ✅ **mentions légales の SIREN と 🏛 企業登録が完全一致。会長・社長の氏名も両者で一致。🏛 Agence Bio が公式サイトを `Site Officiel` として相互リンク。サイト真正性は 4 条件のうち 3 つで確認済み** |
| **Identity（創業年・世代数）** | 🔴 **Low** | 🔴 **「1625 年創業」は公式の書き方ではなく、世代数は公式内で 12 と 13 に割れる。⚠️ リスト ①② で運用回避** |
| **Overview** | **Medium-High** | 📄 **公式の自己記述に完全に依拠。ただし出典は 2022 年の archive** |
| **History** | **Medium** | 📄 **年表の全項目が旧公式頁で裏取り済みだが、稼働中の沿革頁が存在しないため再確認手段が archive しかない** |
| **Location（法的枠組み）** | 🔴 **High** | 🏛 **アイのグラン・クリュ格は INAO の cahier des charges の法文で確認。住所は公式と登録の両方** |
| **Location（区画・森）** | **Medium** | 📄 **`La Valnon` / `La Croix-Courcelles` / `Les Châtrices` / `Hauts-Bâtis` は公式が名指し。面積・全区画は非公表** |
| **Farming（有機の状態）** | 🔴 **High** | 🏛 **Agence Bio の全フィールドを原文で取得。`C2` / `Production` のみ / `mixite: Non` / 日付 3 種すべて確認済み** |
| **Farming（日付の解釈）** | ⚠️ **Low** | 🔴 **`datePremierEngagement 2014` と `dateEngagement 2024` と `C2 (2025)` の関係を登録が説明していない。中断の有無は不明** |
| **Farming（HVE / VDC）** | 🔴 **Low** | 🔴 **canonical が断定する一方、公式に該当語が 1 度も現れない。⚠️ リスト ⑤ で運用回避** |
| **Winemaking（哲学・器）** | 🔴 **High** | 📄 **`0% INOX` / 樫樽・テラコッタ・炻器 / 永久リザーヴ 1990 / 樽 5 年 / 甕 50 基 / ONF 8,000 本、すべて公式の直接記述** |
| **Winemaking（数値）** | 🔴 **Low** | 🔴 **ドザージュ g/L・熟成月数・セパージュ比率・MLF・アルコール度数が全キュヴェについて非公表。本ドシエは 1 つも書いていない** |
| **Style** | **Medium** | 📄 **公式の散文は全 8 キュヴェ分そろっている。ただし構造化テイスティングノートは `Hommage` と `Esprit de Giraud` の 2 点のみ** |
| **Important Cuvées — 1 行目（Esprit Nature）** | **Medium** | 📄 **キュヴェの実在と位置づけは確実。**🔴 **`Brut Nature` の裏づけが無く、メニューと canonical が食い違う** |
| **Important Cuvées — 2 行目** | 🔴 **Low（ただし候補は確定）** | 🔴 **候補を `MV` / `Hommage` / `Blanc de Craie` の 3 本に絞れた。1 本には絞れない。物理ラベル確認が必要** |
| **Important Cuvées — 3 行目（Argonne）** | **Medium** | 📄 **キュヴェ・区画・森・樽・命名の由来まで公式で確定。**🔴 **`2016` というミレジムだけが裏づけられない** |
| **Important Cuvées — 4 行目** | 🔴 **Low（ただし候補と構造は確定）** | 🔴 **公式のロゼ 3 本を特定し、うち 2 本の造り方（アッサンブラージュ）を公式で確認。**🔴 **`2022` は裏づけられず、canonical に受け皿が 0 件（gap）** |
| **Staff Notes / ⚠️ リスト** | 🔴 **High** | 🔴 **全 14 項目が、公式内の矛盾・公的登録との食い違い・公式の沈黙のいずれかの直接の帰結** |
| **Canonical Conflict** | 🔴 **High** | 🔍 **canonical 3 件を全フィールド精査。`C-4` / `V-1` の該当を REGISTER.md の定義に照らして確認。gap と conflict を分離済み** |
| | | |
| 🔴 **総合** | 🔴 **Medium** | **70% 基準は満たす。Identity / Overview / Location / Farming / Winemaking（哲学）/ Style / OBP 全 4 行の紐付け / ⚠️ リスト / 物理確認タスクがすべて揃っている。**<br>🔴 **High に届かない理由は 1 つ —— 生産者が現在キュヴェ情報を一切公表しておらず、本ドシエの中核が Internet Archive 経由の旧公式頁に依存しているため。稼働中の一次資料で再確認する手段が存在しない。**<br>🔴 **数値（ドザージュ・セパージュ・熟成月数・面積・生産量）は 1 つも書けなかったが、これは §2 の「deferrable」に当たり、⚠️ リスト ⑦⑧⑨⑩ で運用上カバーしている。** |

**reached_70: YES (~76%)**

---

## Open Questions

1. 🔴 **OBP 2 行目（`Grand Cru Brut` / NV / $800）の実体は `MV` / `Hommage` / `Blanc de Craie` のどれか。**
   **公式に価格の開示が無く、オンラインでは決着しない。→ 物理ラベル確認タスク ①。**
   **`MV` だった場合は、ラベル上のベース年 2 桁（`MV17` 等）も必ず控えること。**
2. 🔴 **OBP 4 行目（`Grand Cru Brut Rosé` / 2022 / $735）の実体は `MV Rosé` / `Dame-Jane` / `ArG̈onne Rosé` のどれか。**
   **とくに「2022」がラベル上で `MILLÉSIME 2022` なのか `MV22` 的なベース年表記なのか。**
   **前者なら通常のミレジム、後者なら `V-1` 族である。→ 物理ラベル確認タスク ②。**
3. 🔴 **Agence Bio の `datePremierEngagement: 2014-10-06` と `dateEngagement: 2024-10-07`、
   および 2025 年基準の `etatProduction: C2` の関係。**
   **2014〜2024 のあいだに認証の中断があったのか。Agence Bio のレコードは説明していない。**
   **EU TRACES の公開証明書ページ（`webgate.ec.europa.eu/tracesnt/…?121737`）で履歴が取れる可能性がある。**
4. 🔴 **`Argonne 2016` のフィッシュ・テクニックは実在するか。**
   **生産者ドメイン（現行・Internet Archive とも）には無い。輸入元経由で配布されている可能性がある。**
   **⚠️ ただし輸入元の三人称マーケティング資料は briefing §1 により authorship で拒絶される。
   メゾンの letterhead を持つ PDF であれば `📄` として採用できる。**
5. ⚠️ **アイを「Grande Vallée de la Marne」に属するとする分類の一次的根拠は何か。**
   **INAO の cahier des charges にはこの下位区分の概念が無く、生産者も使っていない。**
   **Comité Champagne の刊行物が出典である可能性があるが、本調査では確認していない。**
6. 🔴 **HVE / VDC の認証は実際に存在するか。**
   **公式サイト（現行・アーカイブとも）に該当語が 1 度も現れない。**
   **HVE には公的な事業者名簿があるはずだが、本調査では照会していない。**
7. ⚠️ **`Esprit de Giraud`（2010 年のフィッシュ）と `Esprit Nature` は同一キュヴェの新旧か、別キュヴェか。**
   **公式に両者を結ぶ記述が無い。同一なら「`cuve inox` → `0% INOX`」という醸造の断層が同一キュヴェ内に生じる。**
8. ⚠️ **`Esprit Nature` のバックラベルの QR コード（`New Generation` ラベル）が指す分子分析の開示先は
   現在も生きているか。生きていれば、公式が公表していないドザージュ等の数値が取れる可能性がある。**
9. ⚠️ **公式サイトが 2023 年頃にキュヴェ情報を撤去した理由。**
   **改装中なのか、方針転換なのかで、本ドシエの再取得計画が変わる。**
   **`fiche-client` / `fiche-client-avec-liste` という 2 つの未公開然とした固定頁が存在することから、
   B2B 向けの限定公開に移行した可能性がある。**
10. ⚠️ **`boutique.champagne-giraud.com` が、現在は第三者の売り出し中ドメイン
    `boutique.champagnegiraud.com` を指している状態は、生産者が把握しているか。**
    **THÉSEUS の課題ではないが、記録しておく。**
