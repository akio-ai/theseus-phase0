# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> 🔴 **canonical にこの生産者のレコードは 1 件だけ存在する**（`taittinger-comtes-2013`）。
> 本書は昇格前の研究記録であり、**canonical も REGISTER.md も一切書き換えていない。**
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト taittinger.com で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では使用していない**）
> `⚠️` **出典間で食い違い／出典が沈黙している**
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-05 ／ 一次資料: **`https://www.taittinger.com/`（FR 原本 / EN / DE / ES）**
> 走査元: **`robots.txt`（`User-agent: * / Disallow:` のみ。sitemap の指定は無い）**
> → **`/sitemap.xml` を直接叩いて 382 URL を取得**（`sitemap.php` も `sitemap_index.xml` も 404）
> 併用: ✅ **公式テクニカルシート 9 点（`medias.taittinger.com`）**／✅ **公式プレスルーム `digitalpressroom.taittinger.com`**
>
> 🔴 **本ドシエ最大の収穫 —— OBP 5 行目（メニュー `ROSÉ` セクション・2012・$955）の正体。**
> **`Comtes de Champagne Rosé` は Blanc de Blancs とは別個の、独立したヴィンテージ系列を持つキュヴェである。**
> **そして公式 webzine が「Out now are the elegant 2013 and the rich 2012」と、
> Rosé の 2012 が現行出荷中であることを明記している。**
> **したがって matcher は 5 行目を「色の境界」を越えて誤割当している。** → §Canonical Conflict `C-6`
>
> 🔴 **第二の収穫 —— canonical の `founded_year = 1734` は公式サイトのどこにも根拠が無い。**
> **公式が語る家の始まりは 1932 年。`1734` は Château de la Marquetterie という「建物の竣工年」である。**
> → §Canonical Conflict `P-8`
>
> ⚠️ **調査上の制約 2 点**
> **① `/sitemap.xml` は FR のみ 382 URL。EN 版 URL は hreflang からしか辿れず、
>    さらに sitemap に載っていない公式ページが実在する**（`/en/comtes-de-champagne`・`/en/legacy` 等）。
>    **したがって「公式ページの全数」は本調査では確定していない。**
> **② プレスルームの WP REST API（`/wp-json/wp/v2/media`）は `403 Forbidden`。**
>    **過去のテクニカルシート／プレスキットの全数列挙はできていない。** → Open Questions 1

---

## Identity

| | |
|---|---|
| **OBP 印字** | **Taittinger** |
| **公式表記** | **Champagne Taittinger** ✅／**Maison Taittinger** ✅（両方が公式サイト上で併用されている） |
| 🔴 **法人** | ✅ **Taittinger CCVC**（CGU の掲載責任表示。**SIRET `490 341 062 00035` / TVA `FR 59 490 341 062`**） |
| **所在** | ✅ **9, place Saint-Nicaise – CS 10011 – 51722 Reims Cedex – France**（CGU 記載）<br>⚠️ プレスルーム側の表記は **`9 rue Saint-Nicaise, 51100 Reims`**。**`place` と `rue` で揺れている** |
| **サイト掲載責任者** | ✅ **Madame Vitalie Taittinger** |
| **社長** | ✅ **Vitalie Taittinger（Présidente）**。2007 年入社、元イラストレーター（école Émile Cohl）。**FRAC Champagne-Ardenne 会長**、寄付基金 **Philanthropic Ars Nova** を創設 |
| **副社長格** | ✅ **Clovis Taittinger（Directeur général）**。2007 年入社、国際担当。🔴 **「売上の 75% が海外」** |
| **名誉会長** | ✅ **Pierre-Emmanuel Taittinger（Président d'honneur）**。1976 年入社。**2006 年に家族が Maison を買い戻す局面で決定的役割** |
| 🔴 **醸造長** | ✅ **Alexandre Ponnavoy（Chef de caves）。2015 年入社**、歴代醸造長 **Loïc Dupont** の後任。**3 年間の並走ののち継承** |
| 🔴 **畑責任者** | ✅ **Christelle Rinville（Directrice du vignoble）。2015 年入社、2020 年より畑統括** |
| **総支配人** | ✅ **Damien le Sueur（Managing director / General Manager）** |
| **家族の代数** | ✅ **「4 世代」**（`/en/the-taittinger-spirit`: 「At the helm is a family that has been involved for four generations」） |
| **家の始まり** | 🔴 ✅ **1932 年。**「**Since 1932, the Taittinger family has been building an adventure spanning several lifetimes**」 |
| **創業年** | 🔴 ⚠️ **公式サイトは「創業年」という数字を提示していない。** **1932 年に買収した `Forest-Fourneaux` を「シャンパーニュで最も古い一つ」と書くのみで、その創業年は書かれていない。** → §Canonical Conflict `P-8` |
| **認証** | ✅ **HVE（Haute Valeur Environnementale）レベル 3 ／ VDC（Viticulture Durable en Champagne）／ ISO 14001** |
| **世界遺産** | ✅ **Saint-Nicaise のクレイエールは「Champagne Hillsides, Houses and Cellars」として 2015 年 UNESCO 世界遺産に登録** |
| **canonical id** | 🔍 **`taittinger-comtes-2013` 1 件のみ**（`producer='Taittinger'` / `founded_year=1734`） |

---

## Overview

✅ **ランス、Saint-Nicaise。地下 18 メートルのガロ・ローマ期のクレイエール（白亜採掘坑）を蔵とする、
4 世代の家族経営メゾン。畑は 288 ヘクタール。**

🔴 ✅ **公式が自らの核心として繰り返す語はただ一つ —— `Chardonnay`。**
全 9 点のテクニカルシートに、同一の一段落が例外なく反復されている。
「**スタイルへの要求こそが究極の探究であり、最良のものだけを残し、誰にも似ないこと —— これがわれわれのワインの創造哲学である。
自然の力と人間の創造性のあいだの繊細な均衡、その導きの糸となるのが Chardonnay である。
流行の効果から自らを解き放ち、記憶に残る瞬間を差し出すための署名。**」

🔴 ✅ **公式は「買いブドウを使っている」ことを隠していない。同時に「自社畑がある」ことも明示している。**
「**これらの畑はメゾンの必要のおよそ半分を満たしており、
Les Folies de la Marquetterie のような特定のキュヴェに特定の区画を充てることを可能にし、アッサンブラージュの一貫性を保証する。
残りは、その厳格さと持続可能な栽培への取り組みで選ばれた栽培パートナーから来る。**」
→ 🔴 **すなわち「全部自社畑」でも「全部買いブドウ」でもない。約半分。** → §Staff Notes ⚠️ ②

🔴 ✅ **`Comtes de Champagne` はメゾンの DNA として位置づけられる、例外年のみのキュヴェ。**
「**Comtes de Champagne は例外的な年にのみ造られる —— 1952 年以来 42 のヴィンテージ。**」
⚠️ **ただしこの本数の数字は公式内部で揺れている。** → §Staff Notes ⚠️ ⑤

🔴 ✅ **`Comtes de Champagne` は Blanc de Blancs と Rosé の 2 つの姿を持つ。**
「**Comtes de Champagne は Blanc de blancs としても Rosé としても存在し、Maison Taittinger の DNA にある**」
（Alexandre Ponnavoy）。
→ 🔴 **これが OBP 5 行目の鍵である。** → §Important Cuvées / §Canonical Conflict `C-6`

🔍 **THÉSEUS における状態は「1 件だけ登録されている」という、最も誤解を生みやすい形。
canonical にあるのは `Comtes de Champagne Blanc de Blancs 2013` ただ 1 本で、
OBP 掲載 5 本のうち 1 本（2013）だけが alias で当たり、残り 4 本は `unresolved`。
そして 5 行目は色の境界を越えて誤って提案されている。**

---

## History

✅ **公式の沿革ページ（`/en/legacy`）は静的取得で本文が返る。**（Pol Roger と異なり JS 描画の障害は無かった。）

| 年 | 出来事 ✅ |
|---|---|
| **1717** | **ロシア皇帝ピョートル 1 世がランスと Saint-Nicaise 修道院を訪問**（現在の Taittinger のカーヴの場所）。**2017 年にメゾンが「Tricentenaire」として記念**（Fabergé 意匠の Brut Réserve 500 本限定） |
| **1734** | 🔴 **Château de la Marquetterie が、シャンパーニュの毛織物商の一族によって建てられる。**「**Built in 1734, at the dawn of Champagne, by a family of Champagne cloth merchants**」<br>🔴 **これは「建物の竣工年」であって、シャンパーニュ・メゾンの創業年ではない。** |
| **1760** | 作家 **Jacques Cazotte**（『悪魔の恋』）が Marquetterie に **Voltaire** ら啓蒙期の人々を迎える |
| **1911** | **Pierre Taittinger（25 歳）が Union Champenoise の商人としてシャンパーニュに出会う** |
| **1915** | **のちの連合軍元帥 Joseph Joffre が Marquetterie に司令部を置く。**若い将校 Pierre Taittinger がこの場所に打たれる |
| 🔴 **1932** | 🔴 **Pierre Taittinger が義兄 Paul Evêque とともに Château de la Marquetterie を取得し、同時に `Forest-Fourneaux` 社を買収。**「**one of the oldest in Champagne**」と公式は書くが、**その創業年は書かれていない**。**「1932 年以来、Taittinger 家は…」が公式の起点表現** |
| **1934** | **その 2 年後、Château de la Marquetterie が一族の冒険の出発点となる** |
| **1940 年 6 月** | **Michel Taittinger（20 歳、École Polytechnique）がセーヌ最後の橋を守って戦死。**死後にレジオンドヌール勲章と戦争十字章 |
| 🔴 **1952** | 🔴 **François Taittinger が `Comtes de Champagne Blanc de Blancs` を創出。**同時に **「家名を正式に確立し、Chardonnay をメゾンの署名品種として確定した」** |
| **1955** | **François Taittinger が 110 ヘクタールの畑を取得** |
| **1955（ヴィンテージ）** | **ド・ゴール将軍に招かれた Khrushchev が最初期のヴィンテージの一つを試飲し「これは我が国には無いものだ」と語ったと公式が記す** |
| **1960** | **François Taittinger 死去。Claude Taittinger が経営を引き継ぐ（1960–2005 社長）** |
| **1967** | **Claude Taittinger が `Prix Culinaire International Pierre Taittinger` を創設** |
| **1983** | **`Taittinger Collection` 開始。**Vasarely、Lichtenstein、Zao Wou-Ki らとヴィンテージ・キュヴェを組む |
| **1977** | **Jean Taittinger が政界を離れ Société du Louvre の経営へ**（ランス市長 1959–、法務大臣を歴任） |
| 🔴 **2005** | 🔴 **Pierre-Emmanuel Taittinger が持続可能な栽培への移行を開始**（除草剤・殺虫剤の停止、土壌の耕起、草生の管理） |
| 🔴 **2006** | 🔴 **家族が Maison を買い戻す。**「**getting the champagne house back under family control in 2006**」 |
| **2015** | **Alexandre Ponnavoy が入社**（Loïc Dupont の後任）／**Christelle Rinville 入社**／**シャンパーニュが UNESCO 世界遺産に登録** |
| **2017** | **畑が HVE と VDC の認証を取得** |
| **2020** | **Christelle Rinville が畑統括に** |

✅ **Comtes de Champagne の名の由来（公式）** —
「**このキュヴェは、8 世紀前に Thibault IV、Comte de Champagne にしてナバラ王によってシャンパーニュにもたらされた Chardonnay に敬意を表する。**」
✅ **ボトルに刻まれるのは `Demeure des Comtes de Champagne`（13 世紀建立、ランス）のシルエット。**
**戴冠式の際に貴族を迎えた建物で、大戦で損傷したのち Maison Taittinger が買い取り、
フランス美術省の支援を得て修復した。**

⚠️ **`Forest-Fourneaux` の創業年は公式サイトに一切書かれていない。**
**「シャンパーニュで最も古い一つ」という定性的な表現だけである。** → §Canonical Conflict `P-8`

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | **Champagne** ✅ |
| **本拠** | ✅ **Reims、`9 place Saint-Nicaise`** |
| 🔴 **カーヴ** | ✅ 🔴 **地下 18 メートル。ガロ・ローマ期に掘られた白亜の採掘坑（crayères）。**かつて初期キリスト教徒の避難所、大戦時の防空壕。**2015 年 UNESCO 世界遺産**。公式は「**地下の大聖堂（underground cathedrals）**」と呼ぶ |
| **カーヴの条件** | ✅ **「一定した温度、暗黒、自然の湿度」** |
| **畑の規模** | ✅ **288 ヘクタール** |
| ⚠️ **畑の順位** | ⚠️ 🔴 **公式内で食い違っている。** `/en/the-vineyard` は「**シャンパーニュで 2 番目に大きい畑（the second largest vineyard in Champagne）**」、**テクニカルシート全 9 点は「3 番目に大きい所有地（the 3rd largest estate in Champagne）**」 → §Staff Notes ⚠️ ④ |
| **畑の品種構成** | ✅ **Chardonnay 37% / Pinot Noir 48% / Meunier 15%**（テクニカルシート全点） |
| **畑の広がり** | ✅ **40 のクリュ**（テクニカルシート）／**37 の畑、Côte des Blancs・Vallée de la Marne・Montagne de Reims・Aube**（`/en/the-vineyard`） |
| **自給率** | 🔴 ✅ **メゾンの必要のおよそ半分**（`nearly half of the champagne house's needs`） |

### ✅ キュヴェ別の産地構成（公式テクニカルシート）

| キュヴェ | 産地 |
|---|---|
| 🔴 **Comtes de Champagne Blanc de Blancs** | 🔴 **Côte des Blancs のグラン・クリュ 5 村のみ —— `Avize` / `Cramant` / `Chouilly` / `Oger` / `Le Mesnil-sur-Oger`** |
| 🔴 **Comtes de Champagne Rosé** | 🔴 **Côte des Blancs（Chouilly / Avize / Le Mesnil-sur-Oger）＋ Montagne de Reims（Mailly-Champagne / Bouzy / Ambonnay）。赤ワインは Bouzy** |
| **Brut Millésimé** | **Bouzy / Ambonnay / Chouilly / Avize ほか** |
| **Prélude Grands Crus** | **Bouzy / Ambonnay / Chouilly / Avize ほか** |
| **Prestige Rosé** | **Ambonnay / Ecueil / Rilly-la-Montagne / Verzenay / Hautvillers / Loches-sur-Ource ほか** |
| **Folies de la Marquetterie** | **Verzenay（Les Rochelles）ほか、単一区画由来** |

🔴 ✅ **赤ワイン用の区画（プレスキットより）** —
「**Montagne de Reims（Ambonnay、Verzenay、Mailly-Champagne、Rilly-la-Montagne）と
Côte des Bar（Loches-sur-Ource、Les Riceys）に、差別化された赤ワインを得るための区画選抜がある。
Bouzy については歴史的なパートナーシップが質の高い供給を保証している。**」

❓ **公式に無い**: 所有クリュの一覧・区画名の全体・買いブドウの供給者名。

---

## Farming

🔴 **Pol Roger と違い、Taittinger の栽培は公式で相当程度まで確定できる。本節は本ドシエの強い部分である。**

### ✅ 転換点 —— 2005 年

🔴 ✅ 「**2005 年、Pierre-Emmanuel Taittinger は持続可能な畑への移行を開始した ——
耕起された土壌、管理された草生、そして除草剤も殺虫剤も使わないこと。
生きているものを尊重するアプローチであり、品質の要求として設計されたものである。**」

✅ **「Taittinger はおよそ 20 年前に除草剤の使用をやめた」**（`/en/the-vineyard`、2026 年時点の記述）。
✅ **プレスキット（Comtes Rosé 2009）**: 「**10 年以上前から、288 ヘクタールの畑は完全に草生栽培されている**」

### ✅ 認証（公式が名指しするもの）

| 認証 | 公式の記述 |
|---|---|
| 🔴 **HVE レベル 3**（Haute Valeur Environnementale） | ✅ **テクニカルシート全 9 点に明記。**「**処理の持続可能な管理、施肥の管理、生物多様性の保全という 3 つの領域を規定する**」。**2011 年導入の制度** |
| 🔴 **VDC**（Viticulture Durable en Champagne） | ✅ **シャンパーニュ固有。2014 年から展開、2020 年に強化。**「**規制遵守と HVE 要件に加え、テロワールの保護、景観の向上、責任ある廃棄物管理、カーボンフットプリントの削減を組み込む**」 |
| 🔴 **ISO 14001** | ✅ **テクニカルシート全 9 点に明記** |
| **取得年** | ✅ **2017 年**（`/une-belle-equipe`: 「**Sous son impulsion, le vignoble obtient les certifications environnementales HVE et VDC en 2017**」） |

⚠️ **`organic` / `bio` / `biodynamic` / `Demeter` / `Biodyvin` / `Ecocert` / `Agence Bio` の語は公式サイトに一切出てこない。**
→ **有機・ビオディナミの認証は主張されていない。** → §Staff Notes ⚠️ ③

### ✅ 具体的な栽培実務（公式が名指しするもの）

- 🔴 **収穫前に 1,700 を超えるサンプルを採取。**「**区画選定、ブドウの試食、成熟度 —— 各収穫の前に 1,700 を超えるサンプルが採られ、
  赤ワイン用、Folies de la Marquetterie 用、Comtes de Champagne 用の区画には一層の注意が払われる**」
- 🔴 **エコ・グレージング（eco-grazing）** —「**トラクターの使用を減らし、自然な植生被覆を促進する**」
- ✅ **土壌の節度ある管理、投入資材の抑制、施肥の管理、生物多様性の保全**
- ✅ **赤ワイン用は自社畑 Pinot Noir の `sélection massale`（マサル・セレクション）から**（プレスキット）
- ✅ **コルドン剪定（taille en cordon）、芽かき（ébourgeonnage）、除葉（effeuillage）、
  果粒の精密な試食、収穫直後の圧搾センターでの醸造**（Alexandre Ponnavoy、プレスキット）

✅ **畑責任者の言葉（プレスキット）** —
「**畑の仕事は職人仕事である。美学は本質的であり、生物多様性とは均衡の達成である。
美しいブドウ樹が美しいブドウを実らせ、それが美しいキュヴェの起点となる。
われわれのエコレスポンシブルな取り組みは、環境・遺産・テロワールの尊重、したがって製品の品質に基づく。
これは流行ではなく、一貫した取り組みであり、長年にわたる思考と行動の哲学である。**」
—— Christelle Rinville

---

## Winemaking

### 🔴 Comtes de Champagne Blanc de Blancs（公式テクニカルシート `EN-CCB2014.pdf` ＋ 公式プレスリリース）✅

| 項目 | 記述 |
|---|---|
| **セパージュ** | 🔴 **Chardonnay 100%、グラン・クリュのみ**（Côte des Blancs 5 村） |
| 🔴 **圧搾** | 🔴 **第一プレスのワインのみ採用。**「**Seul le vin de la première presse est retenu, garant de finesse et d'une expression authentique du terroir.**」 |
| 🔴 **木樽** | 🔴 **ワインの 6〜8% を樽で 4〜6 か月熟成**（fiche）。**プレスリリースはこれを「新樽、3 分の 1 ずつ更新（fûts de chêne neufs, renouvelés par tiers）」とし、「複雑さとトースト香をもたらすため」と説明** |
| 🔴 **熟成** | 🔴 **Saint-Nicaise のガロ・ローマ期クレイエールで、澱の上でおよそ 10 年。その後デゴルジュマン** |
| 🔴 **ドザージュ** | 🔴 **8–9 g/L**（2014） |
| **熟成能力** | **10 年以上**（公式表記） |
| **フォーマット** | **Bottle / Magnum / Jeroboam / Methuselah** |
| **提供温度** | **11 °C**（公式指定） |
| **参考価格** | **215 € TTC**（2014 のプレスリリース） |

### 🔴 Comtes de Champagne Rosé（公式テクニカルシート `EN-CC2013.pdf` ＋ 製品ページ ＋ プレスキット）✅

| 項目 | 記述 |
|---|---|
| ⚠️ **セパージュ** | ⚠️ 🔴 **公式内で数字が違う。**<br>**製品ページ**: 「**Chardonnay Grands Crus 30%（Côte des Blancs）＋ Pinot Noir 70%（Montagne de Reims）。うち 12〜15% を Bouzy Rouge に仕立てる**」<br>**2013 のテクニカルシート**: 「**Pinot Noir 60%、Chardonnay 40%、Vins rouges Grands Crus 13%**」<br>**2009 のプレスキット**: 「**Chardonnay 30% ＋ Pinot Noir 70%、Bouzy の Pinot を赤に仕立てたものを 15%**」<br>🔴 **矛盾ではなく「移行」である可能性が高い。**醸造長は公式記事で「**Chardonnay は現在 40% を占め、長期的には 60% に達する可能性が高い**」と述べている。**だが staff が単一の比率を言うのは危険。** → §Staff Notes ⚠️ ⑦ |
| 🔴 **赤ワインの醸造** | 🔴 **Alexandre Ponnavoy が導入した長いマセラシオン ——「10–12 °C で 4〜5 日の低温プレ・ファーメンタリー・マセラシオン、続いて 23–24 °C で 8〜9 日のアルコール発酵を伴うマセラシオン」。搾りかすは乾いた状態、残糖なしで抜く** |
| 🔴 **熟成** | 🔴 **クレイエールで 12 年**（2013 の fiche。製品ページは「nearly twelve years」） |
| 🔴 **ドザージュ** | 🔴 **9 g/L**（2013） |
| **フォーマット** | **Bottle / Magnum** |

### ✅ 他キュヴェの公式スペック（テクニカルシートより。**canonical には 1 件も無い**）

| キュヴェ | セパージュ | 熟成 | ドザージュ |
|---|---|---|---|
| **Brut Réserve** | **Chardonnay 40% / Pinot Noir 35% / Pinot Meunier 25%**、40 以上のクリュ、**リザーヴワイン 30%** | **4 年以上** | **9 g/L** |
| **Brut Millésimé 2016** | **Pinot Noir 50% / Chardonnay 50%** | **5 年** | **9 g/L** |
| **Prélude Grands Crus** | **Pinot Noir 50% / Chardonnay 50%**、単一年 100% | **5 年** | **9 g/L** |
| **Folies de la Marquetterie** | **Pinot Noir 55% / Chardonnay 45%**、単一区画 | **5 年** | **9 g/L** |
| **Prestige Rosé** | **Pinot Noir 40% / Chardonnay 35%（＋Meunier）、静止赤ワイン 11〜14%** | **3 年** | **7–9 g/L** |
| **Nocturne** | **Chardonnay 40% / Pinot Noir 35%（＋Meunier）**、約 30 クリュ | — | 🔴 **17.5 g/L（Sec）** |
| **Nocturne Rosé** | **Pinot Noir 40% / Chardonnay 35%、静止赤ワイン 11〜14%** | **3 年** | 🔴 **17.5 g/L（Sec）** |

🔴 ⚠️ **デゴルジュマン日、アルコール度数、生産本数は公式に一切記載が無い。**
⚠️ **デブルバージュ・発酵温度・マロラクティックの有無・ルミュアージュの方式について、
公式サイトにも 9 点のテクニカルシートにも記述が無い。**
→ 🔴 **したがって本ドシエは「マロラクティックをする／しない」を一切主張しない。** → §Staff Notes ⚠️ ⑥

---

## Style

### ✅ 公式テイスティングノート（OBP 関連分）

| キュヴェ / VT | 公式ノート（抜粋） |
|---|---|
| 🔴 **Comtes de Champagne Blanc de Blancs 2014**<br>（**テクニカルシート**） | 「**結晶のように澄み、輝く黄色に、わずかな銀の閃き。泡は細かく繊細で、ほとんど絹のような手触り。**香りでは、**白亜的で、塩気を帯び、ミネラルの感触**から開く —— **それが生まれたテロワールへの愛にわれわれをつなぐ香り**。次いで香りは**ブリオッシュとレモンメレンゲ風味の焼き菓子、ヘーゼルナッツ、アーモンド**のトースト香へと広がる。空気に触れると、2014 のミレジムは**柑橘、白い花、白い果実、香草**の調子でその全エネルギーを表す。口中では泡が**皮のニュアンスと passion をわずかに帯びた優しい愛撫**を残す。**素晴らしく唾液を誘うフレッシュさ、軽やかな要素からなる優れた構造、洗練された苦み、そして長く塩味のある余韻。**」 |
| **同 2014（醸造長の言）** | 🔴 「**この Comtes de Champagne 2014 は、酸と苦みによって導かれた、制御されたエネルギーのリズムを持つ特異な建築を明かす。**」—— Alexandre Ponnavoy |
| **Comtes de Champagne Blanc de Blancs 2013** | 🔴 「**この 10 月のミレジムは、20 年で唯一、引き伸ばされた植物サイクルを持つという特異性があり、それが Chardonnay を通じて、際立ったミネラルの凝縮と強烈な白亜の純度を表現させている。**」—— Alexandre Ponnavoy。「香りはわれわれを清涼の宇宙へ運ぶ。**精確さ、密度、熟した柑橘と菓子の調子が絡み合う味わい**で魅了する。**Côte des Blancs の偉大なテロワールの塩気とミネラルの厳格さ**を見事に明かす」 |
| **Comtes de Champagne Blanc de Blancs 2012** | 🔴 「**2012 はフレッシュで、精確で、同時に熟した、美しい構造を持つワインを与えた。口中ではアカシアの力強い調子、多くの果実とテクスチャーが見出される。**」—— Alexandre Ponnavoy。「香りは**成熟と官能の宇宙**へ運ぶ。**砂糖漬けの柑橘、ウィリアムス梨、杏。レモンメレンゲ、ヌガー、アーモンド**といった菓子とブリオッシュの香り。**密で豊かな、大きなミネラルの力**を持ち、Chardonnay が**ヨード**の一点で際立つ」 |
| **Comtes de Champagne Blanc de Blancs 2011** | 🔴 「**パン・デピス、リコリス、メレンゲの美食的な調子を持つ官能的なワイン**で、**Côte des Blancs の Chardonnay のヨード的な性格**に高められている。**ミネラルの力を持ち、ヴィーニュの桃、マンダリンの皮、そしてアニスやコリアンダーといった甘い香辛料の香り**を明かす」—— Alexandre Ponnavoy |
| 🔴 **Comtes de Champagne Rosé 2013**<br>（**テクニカルシート**） | 「**美しく紅潮したサーモンピンク、優雅で結晶のように澄んだ輝き。**香りは繊細かつ蠱惑的で、**フレッシュで果実に前がかりな調子と、かすかな苦みを組み合わせた高い芳香的複雑さ**を明かす。**バラの花びら**の繊細な調子から開き、**野いちご、ラズベリー、チェリー、ザクロ**といった洗練された果実の色調へ向かう。ワインが温まるにつれ、**ブロンド・タバコとフレッシュな革**のニュアンスとともに香辛料の底流が余韻に現れる。アタックはフレッシュで振動的、**マンダリン、ピンクグレープフルーツ、ブラッドオレンジ**の洗練された風味に包まれる。絹のような発泡が**強く均衡した構造**を支え、**長く、フレッシュで、優雅な余韻**へ伸びる。」 |
| **同 Rosé（Vitalie Taittinger）** | 🔴 「**すべてのアッサンブラージュの中で最も官能的なもので、信じがたい品質ゆえに選ばれたブドウからなる。その効果は愛撫のようだ。**」 |
| **Comtes de Champagne Rosé 2012** | ⚠️ 🔴 **公式のテクニカルシートは存在しない。**公式 webzine の寄稿記事のみ —— 「**2013 が繊細さのすべてであるのに対し、2012 は大胆で振動する豊かさと力強い魅力である。白亜的なラズベリー、胡椒を利かせたストロベリー＆クリーム、トーストしたアーモンド・ブリオッシュの上のオレンジの花、そしてダークチョコレートの気配。**」 |
| **Comtes de Champagne Rosé 2011** | ✅ 「**当然ミネラルだが、この年としては非常に輝かしく、官能的で、包み込むような性格を併せ持つワイン。**」—— Alexandre Ponnavoy。**「数千本のみの生産」** |

✅ **Blanc de Blancs の食事の合わせ（公式 fiche 2014）** —
「**ホタテのカルパッチョ、青ロブスター、サーモンの卵、舌平目のムニエル。
ブリア・サヴァランと香辛料でローストした林檎／洋梨。**」

✅ **Rosé の食事の合わせ（公式 fiche 2013）** —
「**この Comtes de Champagne Rosé は美食の芸術を体現し、海と陸の双方からの、
洗練され均衡のとれた料理と難なく調和する。植物由来の前菜からローストした肉、
赤い果実のデザートまで、繊細な料理に優雅に寄り添う。**」

---

## Important Cuvées

### 🔴 OBP 掲載分（🔍 THÉSEUS intake より。**全 5 本。うち 1 本のみ alias で当たり、4 本 `unresolved`**）

| # | OBP 印字 | VT | 価格 | メニューのセクション | ✅ **公式での確認結果** |
|---|---|---|---|---|---|
| 1 | **'Comtes de Champagne,'** Grand Cru Brut | **2014** | $760 | `… \| BLANC DE BLANCS` | ✅ 🔴 **`Comtes de Champagne Grands Crus Blanc de Blancs 2014` として実在。現行リリース。** 公式テクニカルシート `EN-CCB2014.pdf` ＋ 公式プレスリリース `/comtes-de-champagne-grands-crus-blanc-de-blancs-2014/` |
| 2 | **'Comtes de Champagne,'** Grand Cru Brut | **2013** | $700 | `… \| BLANC DE BLANCS` | ✅ 🔴 **`… Blanc de Blancs 2013` として実在。** 公式 webzine 記事 ＋ **公式試飲会「Comtes en verticale」が 2014 / 2013 / 2012 の 3 ミレジムを供する**と明記 ＋ プレスルーム記事 |
| 3 | **'Comtes de Champagne,'** Grand Cru Brut | **2011** | $680 | `… \| BLANC DE BLANCS` | ✅ 🔴 **`… Blanc de Blancs 2011` として実在。** 公式プレスリリース「**le Comtes de Champagne Blanc de Blancs 2011 と le Comtes de Champagne Rosé 2008 の 2 つの新ミレジムがこの伝説の系譜に入る**」＋ 公式記事（Damien le Sueur インタビュー）|
| 4 | **'Comtes de Champagne,'** Grand Cru Brut | **2005** | $1,000 | `… \| BLANC DE BLANCS` | ❓ ⚠️ 🔴 **確認できなかった。公式サイト・全テクニカルシート・プレスルームの記事一覧のいずれにも `2005` の Comtes は現れない。** **「存在しない」と言っているのではなく、「公式が沈黙している」。** → Open Questions 2 |
| 5 | **'Comtes de Champagne,'** Grand Cru Brut | **2012** | $955 | 🔴 `… \| **ROSÉ**` | ⚠️ 🔴 **2012 は Blanc de Blancs にも Rosé にも実在する。**<br>**BdB 2012** = 「Comtes en verticale」で公式に供される。<br>🔴 **Rosé 2012** = 公式 webzine「**Out now are the elegant 2013 and the rich 2012**」（Comtes de Champagne Rosé について）。<br>🔴 **メニューのセクションが `ROSÉ` である以上、これは `Comtes de Champagne Rosé 2012` と読むのが正しい。** → §Canonical Conflict `C-6` |

🔴 **5 本中 4 本（2014 / 2013 / 2011 / 2012）は、公式に実在するミレジムであることを確認した。**
🔴 **2005 の 1 本だけが公式で裏が取れていない。**

### 🔴 OBP 5 行目の位置的証拠（🔍 intake から機械的に導出）

🔍 **`research/out/t-01/mapping.json` の実データ:**
- **行 314 / 315 / 316 / 317** = 2014 / 2013 / 2011 / 2005（連続した 4 行）
- 🔴 **行 422** = 2012・$955（**100 行以上離れた、別のセクション**）

🔴 **5 本すべてが同一の research shell `rs:pro:fbc2b74bd8242710` に解決されている。**
**しかし 4 本は BLANC DE BLANCS セクションに連続して並び、1 本だけが 100 行以上離れた ROSÉ セクションにある。**
**メニュー上の物理的な分離が、これが別キュヴェであることを裏づけている。**

### ✅ 公式の全 9 キュヴェ（`/en/champagnes`。**canonical には 1 件も無い**）

| # | 公式キュヴェ | URL |
|---|---|---|
| 1 | 🔴 **Comtes de Champagne Blanc de Blancs**（Grands crus）⭐OBP | `/en/champagnes/comtes-de-champagne-blanc-de-blancs` |
| 2 | 🔴 **Comtes de Champagne Rosé**（Grands crus）⭐**OBP 5 行目の正体** | `/en/champagnes/comtes-de-champagne-rose` |
| 3 | **Brut Réserve** | `/en/champagnes/brut-reserve` |
| 4 | **Prestige Rosé** | `/en/champagnes/prestige-rose` |
| 5 | **Prélude Grands Crus** | `/en/champagnes/prelude-grands-crus` |
| 6 | **Brut Millésimé** | `/en/champagnes/brut-millesime` |
| 7 | **Folies de la Marquetterie** | `/en/champagnes/folies-de-la-marquetterie` |
| 8 | **Nocturne**（Sec） | `/en/champagnes/nocturne` |
| 9 | **Nocturne Rosé**（Sec） | `/en/champagnes/nocturne-rose` |

🔴 **`Comtes de Champagne` は 1 つのキュヴェ名ではなく、`Blanc de Blancs` と `Rosé` という
2 つの独立した製品ラインの共通名である。両者は品種も産地も熟成期間もヴィンテージ系列も違う。**

### 🔴 ✅ 本調査で公式に確認できたヴィンテージ（**網羅ではない。確認できたものだけ**）

| キュヴェ | 公式に確認できたヴィンテージ | 出典 |
|---|---|---|
| 🔴 **Comtes de Champagne Blanc de Blancs** | **2014 ⭐ / 2013 ⭐ / 2012 / 2011 ⭐ / 2008 / 2007** | fiche・プレスリリース・webzine・「Comtes en verticale」 |
| 🔴 **Comtes de Champagne Rosé** | **2013 / 2012 ⭐ / 2011 / 2009 / 2008 / 2007** | fiche・プレスキット・webzine・プレスルーム記事一覧 |

⚠️ 🔴 **これは「公式が公開しているヴィンテージ一覧」ではない。**
**Pol Roger と違い、Taittinger の公式サイトはキュヴェごとのヴィンテージ一覧を掲示していない。
製品ページに出るのは現行リリースの 1 年だけである**（BdB = 2014、Rosé = 2013）。
**上の表は、プレスルームと webzine の記事を 1 件ずつ潰して積み上げた結果にすぎない。**
→ **したがって「2005 は存在しない」とは言えない。** → Open Questions 2

⚠️ **リリース総数についての公式の数字は 4 通りある（時系列で増えていくカウンタと解釈できるが、順序が合わない）:**
- **「Comtes Rosé 2009 = メゾンの 32 番目のミレジム」**（プレスキット）
- **「38 のミレジムのみ」**（BdB 2011 / Rosé 2008 のプレスリリース）
- **「37 のみ」**（`/en/comtes-de-champagne`、2020-10-30 付）
- **「41 のミレジムのみ」**（BdB 2014 のプレスリリース）／**「42 ヴィンテージ」**（現行 BdB 製品ページ）
- **「33 のみ」**（Rosé 2011 の記事、2023-03-31 付） ⚠️ **2020 年の「37」より後の記事なのに数が小さい**
→ 🔴 **staff は本数を言わない。** → §Staff Notes ⚠️ ⑤

---

## Staff Notes

### 芯 3 点（**これだけ覚えれば嘘をつかずに語れる**）

**① ランス・サン・ニケーズ、地下 18 メートルのガロ・ローマ期の白亜坑。畑 288 ヘクタール。導きの糸はシャルドネ。**
「**ランスのサン・ニケーズ**に本拠があり、蔵は**ガロ・ローマ期に掘られた地下 18 メートルの白亜の採掘坑**です。
造り手自身が『**地下の大聖堂**』と呼んでいて、**2015 年に UNESCO 世界遺産**に登録されています。
**畑は 288 ヘクタール**で、シャルドネ 37%・ピノ・ノワール 48%・ムニエ 15%。
造り手が繰り返し掲げる言葉はただ一つ、**『導きの糸となるのはシャルドネ』**です。」

**② コント・ド・シャンパーニュは『白』と『ロゼ』の 2 本立て。まったく別のワインです。**
「🔴 **『コント・ド・シャンパーニュ』は 1 つのワインの名前ではありません。**
**ブラン・ド・ブラン**は**コート・デ・ブランのグラン・クリュ 5 村（アヴィズ、クラマン、シュイイ、オジェ、ル・メニル・シュル・オジェ）
のシャルドネ 100%**、**クレイエールで約 10 年**。
**ロゼ**は**コート・デ・ブランのシャルドネとモンターニュ・ド・ランスのピノ・ノワール**に
**ブジーの赤ワインを加えたもの**で、**約 12 年**寝かせます。
**熟成期間も産地も違う、別のワインです。**」

**③ 2005 年から除草剤も殺虫剤も使っていない。HVE レベル 3・VDC・ISO 14001。**
「**2005 年に、ピエール＝エマニュエル・タッタンジェが持続可能な栽培への移行を始めました。**
造り手の言葉では『**耕起した土壌、管理された草生、そして除草剤も殺虫剤も使わない**』。
**HVE（環境価値重視認証）のレベル 3、VDC（シャンパーニュ持続可能栽培）、ISO 14001** の 3 つを取得していて、
**HVE と VDC は 2017 年取得**です。
**自社畑はメゾンの必要のおよそ半分**を賄い、**残りは選ばれた栽培パートナー**から来ます。」

### 追加で使える一手

- **Comtes de Champagne の名の由来**: 「**8 世紀前にシャンパーニュにシャルドネをもたらした
  ティボー 4 世、シャンパーニュ伯にしてナバラ王**への敬意です。
  ボトルに刻まれているのは**ランスの 13 世紀の建物『ドゥムール・デ・コント・ド・シャンパーニュ』のシルエット**で、
  大戦で傷んだのをメゾンが買い取って修復したものです。」
- **BdB 2014（$760・現行リリース）**: 「**第一プレスのワインだけを使います。
  一部（6〜8%）を樽で 4〜6 か月、そのあとクレイエールで約 10 年。ドザージュは 8〜9 g/L。**
  醸造長のアレクサンドル・ポナヴォワは『**酸と苦みに導かれた、制御されたエネルギー**』と評しています。
  **提供温度は 11 度を公式が指定**しています。」
- **BdB の年ごとの対比（造り手自身の言葉）**: 「**2014 は『制御されたエネルギー』、
  2013 は『20 年で唯一の 10 月のミレジム、際立ったミネラルの凝縮と白亜の純度』、
  2012 は『フレッシュで精確で同時に熟した、美しい構造』**——
  すべて同じ醸造長が書き分けています。」
- **ロゼ 2012（$955）**: 「**造り手のウェブジンが『いま出ているのは繊細な 2013 と豊かな 2012、
  ブルゴーニュの精神を持つ一卵性でない双子』**と書いています。
  **2012 は大胆で振動する豊かさ**の側です。」
- **稀少性**: 「**例外的な年にしか造られません。**造り手は『**収穫の質、ワインの質、
  そしてキュヴェの性格。これを満たさなければ造らない**』と明言しています。
  **ロゼ 2011 は数千本のみ**でした。」
- **家族**: 「**社長はヴィタリー・タッタンジェ**。イラストレーター出身で、
  **FRAC シャンパーニュ＝アルデンヌの会長**も務めています。
  **弟のクロヴィスが総支配人**で国際を見ています。**2006 年に一族が会社を買い戻した**のが、いまの体制の起点です。」

### ⚠️ 言ってはいけないこと（**公式に根拠が無い／出典が沈黙している／出典が矛盾している**）

1. 🔴 ⚠️ **メニューの 5 行目（2012・$955）を『ブラン・ド・ブラン』と説明しない。**
   **メニューのセクションは `ROSÉ` であり、`Comtes de Champagne Rosé 2012` は公式に現行出荷中である。**
   **THÉSEUS の DB は現在これを Blanc de Blancs 2013 のレコードに結びつけているが、それは誤りである。**
   **注文を受けたら実ボトルの色を必ず確認すること。**
2. 🔴 ⚠️ **「全部自社畑」と言わない。** 公式は
   「**これらの畑はメゾンの必要のおよそ半分を満たす。残りは栽培パートナーから来る**」と明記している。
3. 🔴 ⚠️ **「オーガニック」「ビオディナミ」と言わない。**
   **公式サイトに `organic` / `bio` / `biodynamic` / `Demeter` / `Biodyvin` / `Ecocert` の語が一つも無い。**
   言えるのは **HVE レベル 3 / VDC / ISO 14001** の 3 つと、**2005 年以降の除草剤・殺虫剤不使用**まで。
4. 🔴 ⚠️ **「シャンパーニュで 2 番目に大きい畑」と断定しない。**
   **公式サイトの畑ページは「2 番目」、公式テクニカルシート 9 点すべては「3 番目」と書いている。**
   言うなら「**288 ヘクタール、シャンパーニュでも最大級**」まで。
5. 🔴 ⚠️ **「コント・ド・シャンパーニュは○○回しか造られていない」と本数を言わない。**
   **公式の数字は 32 / 33 / 37 / 38 / 41 / 42 と揃っておらず、年代順にも整合しない。**
   言うなら「**例外的な年にしか造られない**」という定性表現まで。
6. 🔴 ⚠️ **マロラクティック発酵の有無、デブルバージュ、発酵温度、ルミュアージュの方式を語らない。**
   **公式サイトにも 9 点のテクニカルシートにも一切記述が無い。**
7. 🔴 ⚠️ **コント・ド・シャンパーニュ ロゼのセパージュ比率を単一の数字で言わない。**
   **製品ページは「シャルドネ 30 / ピノ・ノワール 70」、2013 年のテクニカルシートは「ピノ・ノワール 60 / シャルドネ 40」。**
   **造り手自身が「シャルドネを増やしていく途上」と述べており、年によって違う。**
   言うなら「**コート・デ・ブランのシャルドネとモンターニュ・ド・ランスのピノ・ノワール、
   そしてブジーの赤ワインを加える。近年はシャルドネの比率を高めている**」まで。
8. 🔴 ⚠️ **創業年を言わない。とくに「1734 年創業」と言ってはならない。**
   **公式サイトの 1734 は `Château de la Marquetterie` という建物の竣工年である。**
   **公式が家の起点として書くのは 1932 年**（Pierre Taittinger が Forest-Fourneaux を買収）。
   言うなら「**1932 年から続く一族の物語で、4 世代目**」まで。
9. ⚠️ **メニューの 2005 年を「公式に確認済み」として語らない。**
   **本調査では公式のどこにも 2005 年の Comtes を見つけられなかった。**
   **存在しないという意味ではなく、裏が取れていないという意味である。**
10. ⚠️ **アルコール度数・デゴルジュマン日・生産本数を言わない。** **公式に一切無い。**
    （ロゼ 2011 の「数千本」だけが唯一の量的記述である。）
11. ⚠️ **第三者点数を言わない。** **本調査で取得したどのページにも点数の掲載が無い。**
12. ⚠️ **Domaine Carneros（Napa）と Domaine Evremond（Kent）を「タッタンジェのシャンパーニュ」と混ぜない。**
    **公式は Domaine Carneros を Claude Taittinger が創設したものとし、Domaine Evremond を英国の別事業として扱っている。**

---

## Akio's Insight

（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）

---

## Canonical Conflict

🔴 **新規に 2 件を提起する。既存の登録票（`research/canonical_conflicts/REGISTER.md`、全 20 件）には
どちらも該当する項目が無い。**
🔒 **REGISTER.md も canonical も本書では一切編集していない。ID は「次に空いている番号」の提案にすぎない。**

---

### 🔴 `C-6`（新規提案）—— **色の軸をまたいだキュヴェの誤割当**

**1. 衝突している canonical ID**
- **`taittinger-comtes-2013`**
  （`producer='Taittinger'` / `name='Comtes de Champagne Blanc de Blancs'` / `vintage='2013'` /
  `color='Blanc de Blancs'` / `subregion='Côte des Blancs Grand Cru'` / `grapes=['Chardonnay 100%']`）
- **対する OBP 行**: `mapping.json` 行 **422** —
  `2012 ‘Comtes de Champagne,’ Grand Cru Brut … 955`、
  セクション **`FRANCE | SPARKLING > CHAMPAGNE | ROSÉ`**

**2. なぜ誤りに見えるのか**
🔴 **canonical には `Comtes de Champagne` のレコードが Blanc de Blancs 版 1 件しか存在しない。**
**したがって matcher が `Comtes de Champagne` という印字文字列から到達できる先は
機械的にこの 1 件しか無く、色の軸（`Blanc de Blancs` / `Rosé`）を判定する余地が構造的に存在しない。**
**結果として、メニューが `ROSÉ` セクションに置いた行が `Blanc de Blancs` のレコードに提案されている。**
🔴 **これは「似た名前の取り違え」ではなく、「識別に必要な軸が canonical に無い」ことに起因する。**

**3. 証拠**
- ✅ **`Comtes de Champagne Rosé` は独立した製品ページを持つ**
  （`/en/champagnes/comtes-de-champagne-rose`、sitemap にも独立して登録）。
- ✅ **独立した公式テクニカルシートを持つ**（`EN-CC2013.pdf`）。
  **Blanc de Blancs（`EN-CCB2014.pdf`）とは、品種・産地・熟成年数・ドザージュのすべてが違う。**
  **BdB = Chardonnay 100% / Côte des Blancs 5 村 / 10 年 / 8–9 g/L。
  Rosé = Pinot Noir 主体＋Bouzy の赤 / Montagne de Reims を含む / 12 年 / 9 g/L。**
- ✅ **独立したヴィンテージ系列を持つ。**Rosé で公式に確認できたのは **2013 / 2012 / 2011 / 2009 / 2008 / 2007**。
- 🔴 ✅ **`Comtes de Champagne Rosé 2012` は現行出荷中である。**
  公式 webzine（`/en/webzine/the-endless-summer`、2026-06-03）—
  「**Out now are the elegant 2013 and the rich 2012 – non-identical twins with a Burgundian spirit**」。
  ⚠️ **この記事は外部寄稿者（Dan Roznov）の署名記事だが、メゾンが自社ドメインで公開しているものである。
  Rosé 2012 の独立したテクニカルシートは公式に存在しない。**
- 🔍 **OBP 上の位置的証拠**: 他の 4 本は行 314–317 に連続、この 1 本だけが行 422。**別セクションである。**

**4. OBP への影響**
🔴 **1 本（$955）が誤った実体に提案されている。**
**staff がこの提案を信じると、`Blanc de Blancs`（Chardonnay 100% の白）の説明で
`Rosé`（Pinot Noir 主体のロゼ）を売ることになる。色が違うので、卓上で即座に破綻する。**
**さらに canonical にはそもそも Rosé のレコードが無いため、正しく解決する先が存在しない。**

**5. 推奨する解決（🔒 実行していない）**
- **`Comtes de Champagne Rosé` を Blanc de Blancs とは別の cuvée として登録する。**
- **cuvée 層に色（`color`）を識別属性として持たせ、
  `cuvée × vintage_year` ではなく `cuvée(color 込み) × vintage_year` で一意にする。**
- 🔴 **加えて、メニューのセクション見出し（`BLANC DE BLANCS` / `ROSÉ`）を
  matcher の入力信号として使えるようにする。**
  **本件は「印字文字列だけでは原理的に解けないが、セクション見出しを見れば解ける」典型例である。**
- ⚠️ **どちらも設計判断であり、本書では実行していない。**

**6. Confidence**
🔴 **High。** **Rosé が別キュヴェであることは公式一次資料（製品ページ＋テクニカルシート）で確定。
2012 が Rosé に実在することも公式ドメインの記事で確認済み。**
⚠️ **ただし「OBP 5 行目が BdB 2012 ではなく Rosé 2012 である」ことの最終確定には実ボトルの確認が要る。
BdB 2012 も実在するため、メニューのセクション見出しだけが根拠である。**

---

### 🔴 `P-8`（新規提案）—— **canonical の `founded_year` が生産者自身の記述に根拠を持たない**

**1. 衝突している canonical ID**
- **`taittinger-comtes-2013`** の **`founded_year = 1734`**

**2. なぜ誤りに見えるのか**
🔴 **公式サイト上に「1734」という数字は 1 か所にしか現れず、それは会社の創業年ではない。**

**3. 証拠**
- 🔴 ✅ **`/en/the-heritage`**: 「**Built in 1734, at the dawn of Champagne, by a family of
  Champagne cloth merchants, the site of the Chateau de la Marquetterie…**」
  → **1734 は `Château de la Marquetterie` という建物の竣工年である。**
  **同ページはさらに「the young officer Pierre Taittinger acquired it in 1932」と続ける。**
  **すなわち Taittinger 家がこの建物と関わるのは 1932 年からである。**
- 🔴 ✅ **`/en/legacy`（沿革ページ）**: 「**Since 1932, the Taittinger family has been building an adventure…**」
  **公式が家の起点として明示するのは 1932 年。**
- ⚠️ ✅ **1932 年に買収された `Forest-Fourneaux` について、公式は
  「**one of the oldest in Champagne**」という定性表現しか与えず、その創業年を書いていない。**
- ⚠️ **プレスルームの `Tricentenaire`（300 周年）記事は 1734 とは無関係で、
  1717 年のピョートル 1 世のランス訪問から 300 年（＝2017 年）を指す。**
  **「Taittinger の 300 周年」ではない。**
- 🔴 **したがって、公式サイトのどこにも「Taittinger は 1734 年創業」という記述は存在しない。**

**4. OBP への影響**
⚠️ **直接の照合影響はゼロ**（`founded_year` はマッチングに使われていない）。
🔴 **だが staff 向け表示や生成テキストに使われれば、卓上で「1734 年創業のメゾンです」という
公式に裏づけの無い発言を生む。** → §Staff Notes ⚠️ ⑧ で塞いだ。

**5. 推奨する解決（🔒 実行していない）**
- **`founded_year` を単一の整数で持つモデル自体が、この生産者では表現力不足である。**
  **「建物の年」「買収された前身企業の年」「一族が始めた年」「家名を掲げた年」が別々に存在する。**
- **暫定的には `founded_year` を `1932`（公式が明示する一族の起点）に置き換えるか、
  あるいは値を落として `founding_note` のような自由記述に移すのが公式記述と整合する。**
- ⚠️ **`1734` を残すのであれば、それが `Château de la Marquetterie` の竣工年であることを
  必ず併記しなければならない。**
- 🔒 **いずれも本書では実行していない。**

**6. Confidence**
🔴 **High。** **公式サイト全文で `1734` の出現箇所を機械的に走査し、
Château de la Marquetterie の記述 1 か所以外は
アセットのハッシュ文字列（例: `…69cfd942b3742761734017.jpg`）による誤検出であることを確認した。**

---

### 既存の族に該当するもの（**新しい番号は開かない**）

- **`S-2`（引用符の埋め込み）** — OBP の印字は **`'Comtes de Champagne,'`** で、
  **アポストロフィ（`‘` `’`）とカンマがキュヴェ名の内側に入っている**（`mapping.json` の生行で確認）。
  **canonical 側の名は `Comtes de Champagne Blanc de Blancs Brut`。**
  **照合は正規化に依存しており、`S-2` と同種である。**
- **`C-4`（識別語を持たないキュヴェ名）** — 🔴 **本件はこの族の一種でもある。**
  **OBP の印字 `'Comtes de Champagne,' Grand Cru Brut` には、
  `Blanc de Blancs` か `Rosé` かを決める語が一つも入っていない。**
  **`Grand Cru` も `Brut` も両方に当てはまるため、識別に寄与しない。**
  → **`C-6` の根本原因は `C-4` と同じ構造である。**
- ⚠️ **canonical の `name` は `Comtes de Champagne Blanc de Blancs Brut` だが、
  公式の正式名は `Comtes de Champagne Grands Crus Blanc de Blancs` である**
  （`Grands Crus` が入り、`Brut` は入らない）。**表記の不一致だが、新規の衝突としては開かない。**

---

## Sources

### 🔴 サイト真正性の事前確認（**MANDATORY**）

| 検証項目 | 結果 |
|---|---|
| **(a) 法的表示に実在の会社名** | ✅ **合格。** `https://www.taittinger.com/conditions-generales` に **`Taittinger CCVC`** を「サイトの所有者」として明記。**掲載責任者 `Madame Vitalie Taittinger`** |
| **(c) 公的登録と一致する住所** | ✅ **合格。** **`9, place Saint-Nicaise – CS 10011 – 51722 Reims Cedex`**、**SIRET `490 341 062 00035`**、**TVA `FR 59 490 341 062`** を明示。**Saint-Nicaise は公式が蔵の所在として全ページで語る場所と一致する** |
| **(d) 整合した商業・法務フッター** | ✅ **合格。** 年齢確認ゲート、`L'ABUS D'ALCOOL EST DANGEREUX POUR LA SANTÉ` の法定表示、CGU、個人情報・cookie ページ、ホスティング事業者（HEXANET SAS、RCS Reims 487 555 682）まで完備。**免責的な「ファンサイト」表記は無い** |
| **一人称の告白的記述** | **無し。** 過去バッチで掴んだ「`/history` が一人称で書かれたファンページ」の兆候は一切無い |
| **ドメイン売却ページの兆候** | **無し** |

**付随ドメインの真正性**
- ✅ **`medias.taittinger.com`** — 公式サイトの各キュヴェページから `href` で直接参照される CDN。
  **配信されるのは `Champagne Taittinger` 名義の公式テクニカルシート PDF。同一の登録可能ドメイン配下。**
- ✅ **`digitalpressroom.taittinger.com`** — 同一の登録可能ドメイン配下。
  **`www.taittinger.com` へ相互リンクし、`pressrequest@taittinger.com` と
  公式広報代理店（BUREAU DE PRESSE PASCALE VENOT, 6 rue Paul Baudry, 75008 Paris）を明示。**
  **記事に `Communiqué de Presse` の PDF が添付されている。**
  ⚠️ **住所表記が `9 rue Saint-Nicaise, 51100 Reims` と、CGU の `9 place Saint-Nicaise, 51722 Reims Cedex` で揺れている。**
  **同一施設の別表記と判断したが、この揺れ自体は記録する。**

🔴 **本調査で `NOT_THE_PRODUCER_*` として退けたサイトは無い。
公式ドメイン `taittinger.com`（およびその 2 つのサブドメイン）以外の情報源を、事実の根拠として一切使っていない。**
（**WebSearch は URL の発見にのみ用い、検索結果の要約文は事実として採用していない。**
**発見した URL は必ず公式ドメイン上で直接取得し直して検証した。**）

### 一次資料（**公式ドメインのみ。非公式ソースは一切使用していない**）

| 資料 | 取得した情報 |
|---|---|
| **`robots.txt`** | `User-agent: * / Disallow:` のみ。**sitemap の指定が無い。** `/sitemap.xml` を直接叩いて **382 URL** を取得（`sitemap.php` / `sitemap_index.xml` / `wp-sitemap.xml` はすべて 404） |
| **`/sitemap.xml`** | **FR の 382 URL と、各 URL の `hreflang`（fr / en / de / es）。** **EN 版 URL はここからしか辿れない。** 9 キュヴェページ、`/l-histoire`、`/le-vignoble`、`/le-patrimoine`、`/l-esprit-taittinger`、`/caracteristiques-environnementales` と 352 件の webzine |
| 🔴 **`/en/champagnes/comtes-de-champagne-blanc-de-blancs`** | 🔴 **「1952 年以来 42 ヴィンテージ」「Côte des Blancs のグラン・クリュ 5 村」「Thibault IV への敬意」「Saint-Nicaise のガロ・ローマ期クレイエールで 10 年」。テクニカルシートへのリンク（`EN-CCB2014.pdf`）→ 現行リリースが 2014 であることが確定** |
| 🔴 **`/en/champagnes/comtes-de-champagne-rose`** | 🔴 **Rosé が独立したキュヴェであることの決定的証拠。**「Chardonnay Grands Crus 30% ＋ Pinot Noir 70%、うち 12〜15% を Bouzy Rouge に」「クレイエールで約 12 年」。テクニカルシート `EN-CC2013.pdf` → **現行リリースが 2013** |
| 🔴 **`medias.taittinger.com` のテクニカルシート 9 点**（全点 `application/pdf`・テキストレイヤーあり） | 🔴 **`EN-CCB2014`（BdB 2014）/ `EN-CC2013`（Rosé 2013）/ Brut Réserve / Brut Millésimé 2016 / Prélude / Folies / Nocturne / Nocturne Rosé / Prestige Rosé。** **セパージュ・熟成年数・ドザージュ・区画名・フォーマット・HVE 3 / VDC / ISO 14001・288 ha・37/48/15・40 クリュ** |
| 🔴 **`/en/the-vineyard`** | 🔴 **§Farming の中核。**「2005 年、Pierre-Emmanuel が持続可能な畑へ移行を開始」「除草剤・殺虫剤なし」「37 の畑」「必要のおよそ半分」「1,700 超のサンプル」「エコ・グレージング」「HVE 2011 / VDC 2014・2020」「UNESCO 2015」「20 年前に除草剤停止」 |
| 🔴 **`/en/legacy`**（**sitemap に無い。WebSearch で URL を発見し、公式上で直接検証**） | 🔴 **「Since 1932」「1932 年に Forest-Fourneaux を買収」「François が 1952 年に Comtes BdB を創出」「1955 年に 110 ha 取得」「Claude 社長 1960–2005」「2006 年に家族が買い戻す」。**`P-8` の根拠** |
| 🔴 **`/en/the-heritage`** | 🔴 **「Built in 1734 … Château de la Marquetterie」＝ `P-8` の決定的根拠。**地下 18 m、ガロ・ローマ期クレイエール、UNESCO、Demeure des Comtes de Champagne（13 世紀） |
| **`/une-belle-equipe`** | **Vitalie（Présidente）/ Clovis（DG・海外 75%）/ Pierre-Emmanuel（名誉会長）/ Christelle Rinville（畑・2020–）/ Alexandre Ponnavoy（醸造長・2015–、Loïc Dupont の後任）。HVE・VDC は 2017 年取得** |
| **`/en/the-taittinger-spirit`** | **「4 世代」「288 ha」「one of the largest in Champagne」** |
| 🔴 **`/webzine/comtes-en-verticale`** | 🔴 **公式試飲会が BdB の 2014 / 2013 / 2012 を供すると明記。3 年分の醸造長コメント付き。OBP 行 2 の裏づけ** |
| 🔴 **`/en/webzine/the-endless-summer`**（2026-06-03） | 🔴 **`C-6` の決定的証拠。**「**Out now are the elegant 2013 and the rich 2012**」（Comtes de Champagne Rosé について）。⚠️ **外部寄稿者 Dan Roznov の署名記事だが、メゾンが自社ドメインで公開** |
| **`/en/webzine/the-comtes-de-champagne-rose-2011`**（2023-03-31） | **「Rosé は 1970 年代に開発」「直前のヴィンテージは 2009」「数千本のみ」「Chardonnay は現在 40%、長期的には 60% へ」「33 ヴィンテージ」「ブレンド後 12 年で発売」** |
| **`/en/webzine/the-creation-of-an-exceptional-cuvee-comtes-de-champagne`**（2021-09-15） | 🔴 **「Maison Taittinger is releasing the Comtes de Champagne Blanc de Blancs 2011」＝ OBP 行 3 の裏づけ。**造るか造らないかの判断基準（Damien le Sueur） |
| **`/en/comtes-de-champagne`**（2020-10-30。**sitemap に無い**） | **BdB 2008 のリリース。「地下 18 m」「1952 年創出」「37 ヴィンテージ」「Khrushchev / 1955」「Périco Légasse の『シャンパーニュのモンラッシェ』」** |
| 🔴 **`digitalpressroom.taittinger.com/post-sitemap.xml`** | 🔴 **プレスリリース全 URL の列挙。**ここから **BdB 2014 / 2013 / 2012 / 2011 / 2008 / 2007、Rosé 2011 / 2009 / 2008 / 2007** の各リリース記事の存在を機械的に確定 |
| 🔴 **`digitalpressroom…/comtes-de-champagne-grands-crus-blanc-de-blancs-2014/`** | 🔴 **「1952 年創出、41 ミレジムのみ」「第一プレスのみ」「新樽 4〜6 か月、3 分の 1 ずつ更新」「約 10 年」「215 € TTC」** |
| 🔴 **`digitalpressroom…/comtes-champagne-taittinger/`** | 🔴 **「BdB 2011 と Rosé 2008 の 2 つの新ミレジム」「38 ミレジムのみ」「Loïc Dupont → Alexandre Ponnavoy」「地下 18 m」** |
| **`digitalpressroom…/wp-content/uploads/2022/07/DPComtes2009-Fr.pdf`** | **Rosé 2009 のプレスキット。「メゾンの 32 番目のミレジム」「10 年以上前から 288 ha 完全草生」「HVE と VDC の二重認証」「赤ワインの醸造詳細（10–12 °C で 4〜5 日 → 23–24 °C で 8〜9 日）」「Christelle Rinville の言葉」** |
| **`/conditions-generales`** | **真正性の検証。`Taittinger CCVC` / SIRET / TVA / 住所 / 掲載責任者** |
| **`/caracteristiques-environnementales`** | **AGEC 法（Décret n° 2022-748）に基づく包装の環境情報開示。`Taittinger CCVC` 名義。`contactus@taittinger.fr`** |
| **`digitalpressroom…/taittinger-the-tricentenaire/`** | **`Tricentenaire` が 1717 年のピョートル 1 世訪問の 300 周年（＝2017 年）であり、創業 300 年ではないことの確認。`P-8` の傍証** |

### 取得できなかったもの / 存在しなかったもの

- 🔴 **`digitalpressroom.taittinger.com/wp-json/wp/v2/media` が `403 Forbidden`。**
  **過去のテクニカルシート／プレスキットの全数を列挙できていない。**
  **`2005` のミレジムが存在するかどうかは、ここが開けば判明する可能性が高い。** → Open Questions 1 / 2
- 🔴 **公式サイトはキュヴェごとの「ヴィンテージ一覧」を持っていない。**
  **製品ページに出るのは現行リリース 1 年のみ**（BdB=2014 / Rosé=2013）。
  **Pol Roger の `sitemap.php` のような、一覧を機械的に取れる場所が存在しない。**
- 🔴 **`Comtes de Champagne Rosé 2012` の独立したテクニカルシートが公式に無い。**
  **存在の根拠は webzine の署名記事 1 本のみ。**
- 🔴 **`2005` の Comtes は、公式サイト・9 点のテクニカルシート・プレスルームの記事一覧のいずれにも現れない。**
- 🔴 **`Forest-Fourneaux` の創業年が公式に書かれていない。**
- 🔴 **醸造工程の一部（デブルバージュ・発酵温度・マロラクティック・ルミュアージュ）が
  公式にもテクニカルシートにも一切記述が無い。**
- ⚠️ **アルコール度数・デゴルジュマン日・生産本数がどのキュヴェにも無い。**
- ⚠️ **`/sitemap.xml` に載っていない公式ページが実在する**（`/en/comtes-de-champagne`、`/en/legacy`、`/ja/…`）。
  **公式ページの全数は本調査で確定していない。**
- ⚠️ **352 件の webzine 記事のうち、本調査で読んだのは Comtes 関連の 10 件程度である。**

### canonical / OBP（🔍 THÉSEUS DB。**読み取りのみ・無変更**）

🔍 **canonical レコード: `taittinger-comtes-2013` の 1 件のみ**
（`producer='Taittinger'` / `name='Comtes de Champagne Blanc de Blancs'` / `vintage='2013'` /
`region=Champagne` / `subregion='Côte des Blancs Grand Cru'` / `color='Blanc de Blancs'` /
`appellation_id=appellation:champagne` / `grapes=['Chardonnay 100%']` / `founded_year=1734`）
🔍 **OBP: 5 本**（`research/out/t-01/mapping.json` 行 314 / 315 / 316 / 317 / **422**）。
**全 5 本が `producer_state = exact`、shell `rs:pro:fbc2b74bd8242710` に解決。
`match_state` は 2013 の 1 本が `alias`、残り 4 本が `unresolved`。**
🔍 **canonical に `Comtes de Champagne Rosé` のレコードは存在しない。**
🔍 **canonical に他の 8 キュヴェ（Brut Réserve ほか）のレコードも存在しない。**
🔒 **canonical・`REGISTER.md`・`mapping.json` のいずれも編集していない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| **Identity** | **High** | 🔴 **法人名・SIRET・住所・掲載責任者が CGU で確定。現経営陣 5 名の氏名と役職・就任年がすべて公式。**⚠️ 創業年のみ公式が沈黙 |
| **Overview** | **High** | Chardonnay を軸とする自己規定、自給率およそ半分、Comtes が白とロゼの 2 系統であることが一次で取れた |
| **History** | **Medium-High** | 🔴 **沿革ページが静的取得でき、1911 / 1932 / 1940 / 1952 / 1955 / 1960 / 1967 / 1983 / 2005 / 2006 / 2015 / 2017 が確定。**⚠️ **前身 Forest-Fourneaux の創業年のみ空白** |
| **Location** | **High** | Reims / Saint-Nicaise / 地下 18 m / UNESCO / 288 ha / 品種構成 / キュヴェ別の村名まで確定。⚠️ **畑の順位表記だけが公式内で矛盾** |
| 🔴 **Farming** | 🔴 **High** | 🔴 **Pol Roger と対照的に、本節が最も強い。2005 年の転換、除草剤・殺虫剤の不使用、HVE 3 / VDC / ISO 14001、取得年 2017、自給率、1,700 サンプル、エコ・グレージング、マサル・セレクションまで一次で取れた** |
| **Winemaking** | **Medium-High** | 🔴 **Comtes 両キュヴェのセパージュ・第一プレス・樽比率・熟成年数・ドザージュ、および他 7 キュヴェのスペックが公式 PDF で確定。**⚠️ **デブルバージュ・発酵温度・マロラクティック・ルミュアージュ・分析値が完全に不在** |
| **Style** | **High** | 🔴 **BdB は 2014 / 2013 / 2012 / 2011 の 4 年分、Rosé は 2013 / 2012 / 2011 の 3 年分の公式ノートを取得。うち複数は醸造長の署名つき** |
| **Important Cuvées** | **Medium-High** | 🔴 **OBP 5 本中 4 本のミレジムが公式に実在することを確認。**⚠️ **2005 が未確認**、⚠️ **公式にヴィンテージ一覧が存在しないため「網羅」は原理的に不可能** |
| **Canonical Conflict** | **High** | 🔴 **`C-6` は公式の製品ページ＋テクニカルシート＋現行出荷情報で裏づけ。`P-8` は公式全文の機械走査で裏づけ** |
| **Staff Notes** | **High** | ⚠️ **12 項目。🔴 「5 行目をブラン・ド・ブランと呼ぶ」「1734 年創業」「全部自社畑」「オーガニック」「2 番目に大きい」「ロゼの比率」「本数」という 7 つの誤りを塞いだ** |
| **総合** | 🔴 **High — staff-usable（70% を大きく超過。実感としては 85% 前後）。** | **OBP 5 本のうち 4 本について、公式の正式名・セパージュ・熟成・ドザージュ・造り手のテイスティングノートを言える。栽培は認証名と取得年まで言える。**<br>**欠けているのは ① 2005 の裏づけ、② 醸造工程の一部（MLF 等）、③ 分析値。**<br>**いずれも「言わない」で回避でき、卓上で嘘をつく経路は塞いである。** |

**reached_70: YES.**

---

## Open Questions

1. 🔴 **プレスルームの WP REST API（`/wp-json/wp/v2/media`）が `403 Forbidden`。**
   **公式テクニカルシートとプレスキットの全数が列挙できていない。**
   → **プレス登録（`pressrequest@taittinger.com`）を通せば、過去ミレジムの fiche が一括で得られる可能性が高い。**
   **これが本ドシエで最も費用対効果の高い次の一手である。**
2. 🔴 ⚠️ **OBP 4 行目 `Comtes de Champagne 2005`（$1,000）が公式で裏づけられていない。**
   **公式サイト・テクニカルシート 9 点・プレスルームの記事一覧のいずれにも 2005 が現れなかった。**
   **「存在しない」の証明ではなく「公式が沈黙している」。**
   → **① プレスルームのアーカイブ、② 輸入元のテクニカルシート、③ 実ボトルのラベル、のいずれかで確認が要る。**
   → **確認できるまで、staff は 2005 を公式確認済みとして語らない。**
3. 🔴 **OBP 5 行目（2012・$955・`ROSÉ` セクション）が `Comtes de Champagne Rosé 2012` であることの最終確定。**
   **BdB 2012 も Rosé 2012 も公式に実在するため、メニューのセクション見出しだけが判断根拠である。**
   → **実ボトルの確認が要る。** → §Canonical Conflict `C-6` の Confidence 注記
4. 🔴 **canonical に `Comtes de Champagne Rosé` を登録するかどうか。**
   **登録しない限り、5 行目は永久に正しく解決できない。**
   **同時に「cuvée の識別軸に色を入れるか」という設計判断が発生する。**
   → 🔒 **canonical への書き込みは本書では行っていない。昇格可否は Akio / CTO 判断。**
5. 🔴 **canonical の `founded_year = 1734` をどう扱うか。**
   **公式は 1932 年を家の起点とし、1734 は建物の竣工年である。**
   **`founded_year` を単一整数で持つモデル自体が、この生産者では表現力不足である。**
   → 🔒 **本書では変更していない。** → §Canonical Conflict `P-8`
6. ⚠️ **`Comtes de Champagne Rosé 2012` の公式テクニカルシートが存在しない。**
   **セパージュ・ドザージュ・熟成年数が 2012 について確定していない。**
   （**2013 の値を 2012 に流用してはならない。**）
7. ⚠️ **醸造工程の空白 —— デブルバージュ、発酵温度、マロラクティック発酵の有無、ルミュアージュの方式。**
   **公式サイトにも 9 点のテクニカルシートにも一切記述が無い。**
   → **プレスキットの技術セクション、または蔵訪問でしか埋まらない。**
8. ⚠️ **アルコール度数・デゴルジュマン日・生産本数。** 公式に一切無い。
   → **輸入元のテクニカルシートが要る。**
9. ⚠️ **畑の順位表記の矛盾**（サイト＝「2 番目」／テクニカルシート 9 点＝「3 番目」）。
   **どちらが現行の公式見解か未確定。**
10. ⚠️ **Comtes のリリース総数の数字が公式内で 32 / 33 / 37 / 38 / 41 / 42 と揃わず、年代順にも整合しない。**
    **とくに 2020 年の記事の「37」より、2023 年の記事の「33」が小さいのは説明がつかない。**
11. ⚠️ **352 件の webzine 記事のうち約 10 件しか読んでいない。**
    **残りに追加のミレジム情報（とくに 2005）が埋まっている可能性がある。**
12. ⚠️ **`Domaine Carneros`（Napa）と `Domaine Evremond`（Kent）は本調査の対象外とした。**
    **どちらも Taittinger 関連の別事業であり、canonical にどう置くかは未検討。**
