# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:pierre-peters` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト champagne-peters.com で確認**（一次資料）
> `📄` 単一の非公式資料のみ（**本書では未使用**）／ `⚠️` 出典間で食い違い。両方を残す
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 一次資料: `https://champagne-peters.com/`
> **EN 15 ページ**: `/en/home` `/en/historical` `/en/vineyard` `/en/winemaking` `/en/vintage`
> `/en/awards` `/en/node/62`(contact) `/en/cuvee-reserve` `/en/cuvee-grande-reserve`
> `/en/cuvee-extra-brut` `/en/cuvee-esprit` `/en/cuvee-les-chetillons` `/en/cuvee-les-montjolys`
> `/en/cuvee-l-etonnant-monsieur-victor` `/en/cuvee-heritage`
> **FR 6 ページ**: `/fr/accueil` `/fr/historique` `/fr/vignoble` `/fr/elaboration` `/fr/cuvees` `/fr/palmares`
>
> ✅ **Louis Latour と同じく、キュヴェ別テクニカルシート PDF が全 7 キュヴェ分ある。**
> `/sites/default/files/*.pdf` — HTML 上の「Fact sheet」リンクから。7 本すべて取得済み:
> `_sources/pierre-peters/{reserve,grande-reserve,extra-brut,esprit,les-chetillons,les-montjolys,etonnant-monsieur-victor}.pdf`
> 🔴 **PDF と HTML で内容が食い違う箇所が 5 つある。すべて §⚠️ 公式内の食い違い（全 8 件）に列挙した。**
> うち 1 件は **OBP の未解決ボトルの解釈に直結する**（`TB` / `TM`）。
>
> 🔴 **FR ページにしか無い事実が 1 つある（HVE 認証）。EN だけ読むと Farming を丸ごと落とす。**

---

## ⚠️ 公式内の食い違い（すべて両方を残す）

| # | 項目 | A | B | 採用 |
|---|---|---|---|---|
| 1 | **Monsieur Victor の頭文字** | HTML `/en/cuvee-l-etonnant-monsieur-victor`: **「TM for Tim Burton」** | PDF: **「TB for Tim Burton」** | **B（PDF）。**Tim Burton の頭文字は TB、OBP 印字も `TB.17` |
| 2 | **永久リザーヴの層の数** | `/en/winemaking`: リザーヴワイン **20 年分以上** | Réserve PDF: **25 年分以上・1988 年から** | **B（PDF）。**より具体的で新しい。A も残す |
| 3 | **Les Chétillons を造る年** | HTML: 単一収穫年、かつ **「最良の年のみ」** | PDF: 単一収穫年、**「年を問わず（whatever the year）」** | **判定不能。**現場では「単一収穫年のミレジム」までにとどめる |
| 4 | **Extra Brut の正体** | HTML: 「**実際には単一の高品質収穫年のミレジム**」で、4 つのグラン・クリュ畑から | PDF: **Grande Réserve と一字一句同じ**（4 区画＋永久リザーヴ約 20%＋36 ヶ月）。ドザージュだけ 2 g/L | **判定不能。**OBP 未掲載なので実害なし |
| 5 | **平均樹齢** | EN: 「現在 **30 年**」 | FR: 「平均 **30 年超**」 | **B（FR）** |
| 6 | **HVE 認証** | EN `/en/vineyard`: **記載なし**（"sustainable farming methods"） | FR `/fr/vignoble`: **HVE 認証を明記** | **B（FR）。**EN は翻訳が古い |
| 7 | **Héritage のヴィンテージ数** | 本文: **19 ヴィンテージ** | 列挙されているのは **18 年**（＋ブレンド相手の 2010） | 両方残す |
| 8 | **Réserve の格付表記** | HTML 本文: 「コート・デ・ブランの**グラン・クリュ村の**シャルドネのみ」 | PDF 見出し: **「BLANC DE BLANCS」のみで "GRAND CRU" が無い**（7 本中このキュヴェだけ） | **未解決。**→ Open Questions 4 |

---

## Identity

| | |
|---|---|
| **Canonical Name** | Pierre Péters |
| **公式表記** | **Champagne Pierre Péters** ✅ |
| **Aliases** | ❓ canonical `aliases` は空。旧ブランド名 **`Camille Péters`**(1929–1945) が歴史上存在する ✅ |
| **業態** | **récoltant（栽培家兼醸造家）**。「我々のワインは自社畑からのみ来る」と明記 ✅ |
| **所在** | **9 rue de l'Église, 51190 Le Mesnil-sur-Oger** ✅ |
| **世代** | **6 代続く家族経営** ✅（Gaspar → Louis Joseph → Camille → Pierre → François → Rodolphe） |
| **現当主** | **Rodolphe Péters**（醸造家・エノログ。2007 年入社 / **2008 年に経営継承**）✅ ❓**現在性未確認** |
| **7 代目** | **Victor Péters**（Rodolphe の息子。`L'Étonnant Monsieur Victor` のラベル画を描く）✅ |
| **創業起点** | **1919 年**（Camille Péters が自身の名で瓶詰め・販売を開始）✅ |
| canonical id | `producer:pierre-peters` |
| canonical entity confidence | 0.2（`legacy_app`）— エンティティ同定の確度。本書の充実度とは別軸 |

❓ **現在性未確認の理由**: 公式サイトの年表は **2019 年で止まっており**、Rodolphe が 2026 年現在も
当主であることを日付付きで示す記述は無い。Monsieur Victor のページが Rodolphe の一人称（「息子の Victor」）で
書かれていることが唯一の傍証。**「現当主は Rodolphe Péters」と言い切る場合は、2019 年時点の記述に
基づくことを認識しておく。**（→ Open Questions 1）

---

## Overview

✅ コート・デ・ブランのグラン・クリュ村 **Le Mesnil-sur-Oger** に本拠を置く **récoltant**。**1919 年から
ブラン・ド・ブラン（シャルドネ 100%）のグラン・クリュ・シャンパーニュだけを造り続けている**家。
**6 世代続く家族経営**で、ワインは**すべて自社畑**から来る。

✅ 自社畑は **19ha 強**。**Le Mesnil-sur-Oger / Oger / Cramant / Avize** — コート・デ・ブランの
グラン・クリュ村 4 つに集中している。畑はエペルネの数 km 南、**露出した白亜（craie affleurante）**の上にあり、
公式は白亜を「本物の貯水槽」と表現する。斜面は**東向き**で西風から守られる。

✅ **セレクション・マサル（sélection massale）を代々自家で維持**しており、平均樹齢は 30 年超。

✅ この家の骨格は 2 つ。**①「Les Chétillons」** — 1930 年に取得した Le Mesnil の銘醸 lieu-dit の
古樹 3 区画から、**1971 年以来**造られる単一畑ミレジム。**②「Réserve Perpétuelle」** — ソレラ方式に
着想を得た永久リザーヴで、**1988 年を起点に 25 年以上のヴィンテージが積層**している。
NV の `Réserve` も最高級の `L'Étonnant Monsieur Victor` も、どちらもこの永久リザーヴから生まれる。

---

## History

| 年 | 出来事 | |
|---|---|---|
| **1858** | **Gaspar Péters**（**ルクセンブルク出身**）が Le Mesnil に畑を持つ Doué 家の女性と結婚し、**約 2ha** で操業開始 | ✅ |
| 〜19 世紀末 | Gaspar と息子 **Louis Joseph Péters** は栽培・商いを営みつつ、**収穫は全量ネゴシアンに売っていた** | ✅ |
| **1919** | **Camille Péters**（Louis Joseph の息子）が、**シャンパーニュで最初期の栽培家の一人として、自ら収穫・醸造し自分の名で瓶売りすることを決断** ← **house の起点。2019 年がその 100 周年** | ✅ |
| **1929** | 世界恐慌のさなか、Camille が販売を強化し **ブランド名「Camille Péters」で出荷開始** | ✅ |
| **1930** | Camille が **"Les Chétillons" と呼ばれる場所に 2.5ha を取得** | ✅ |
| **1932** | Camille の長男 **Pierre Péters が 12 歳で単身、見本市に出て販売を担い始める** | ✅ |
| **1944** | **Camille が急死**。Pierre が経営を引き継ぐ | ✅ |
| **1946** | **ブランド「Pierre Péters」名義の最初のミレジム（1944 年）をリリース** | ✅ |
| 1949 | 母の死後、Pierre が妹たちの教育を支える。以後 **35 年**、ブランドとコート・デ・ブランの畑の拡張に費やす | ✅ |
| **1967** | 健康問題により、Pierre が**次男 François** に家業を移譲。François は **2008 年までの 40 年**で **面積を 17.5ha まで拡大**し、国内外の販売を大きく伸ばす | ✅ |
| **2007** | **Rodolphe Péters**（醸造家・エノログ）が、ワイン／シャンパーニュ周辺企業での **12 年の経験**を経て家業に戻る | ✅ |
| **2008** | **Rodolphe が経営を継承。**醸造設備（winemaking tool）の質的向上に注力。ブランドの評価と像の構築に注力し、**出荷本数の 80% 超が輸出**になる | ✅ |
| **2009** | **「Rosé for Albane」リリース。**「常にブラン・ド・ブランだけを造ってきた我が家にとって小さな革命」と公式が書く | ✅ |
| **2016** | **「L'Étonnant Monsieur Victor」シリーズをリリース** | ✅ |
| **2019** | **新拠点へ移転。**ドメーヌ **100 周年**。記念キュヴェ **HÉRITAGE**（4 世代・19 ヴィンテージ）をリリース。**Le Mesnil-sur-Oger の lieu-dit「Montjoly」の新区画を立ち上げ** | ✅ |
| 2020〜 | ❓ **公式年表はここで終わる。以降の記述が無い** | ❓ |

**⚠️ 「6 世代」と「4 世代」は矛盾しない。**
公式トップは「**6 世代の家族経営**」（Gaspar 1858 から数える）と書き、Héritage のページは
「**当主を務めた 4 世代**（Camille, Pierre, François, Rodolphe）」と書く。
**最初の 2 代（Gaspar, Louis Joseph）はブドウを売る側で、自分の名では瓶詰めしていない。**
現場でどちらを言っても正しいが、**混ぜると破綻するので使い分ける。**

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Champagne — **Côte des Blancs** ✅ |
| **Village（本拠）** | **Le Mesnil-sur-Oger**（Grand Cru）✅ |
| **保有村** | **Le Mesnil-sur-Oger / Oger / Cramant / Avize**（いずれも Grand Cru）✅ |
| **総面積** | **19ha 強**（"a little over 19 hectares" / "un peu plus de 19 hectares"）✅ |
| **土壌** | **露出した白亜（chalky outcrop / craie affleurante）**。公式は「本物の貯水槽」と表現 ✅ |
| **向き** | **東向きの斜面**。西風から守られる ✅ |
| **平均樹齢** | ⚠️ EN「現在平均 30 年」／ FR「平均 **30 年超**」 ✅ |
| **品種** | **シャルドネ 100%** ✅ |

### 主要 lieu-dit

**Les Chétillons**（Le Mesnil-sur-Oger, Grand Cru）✅
- **1930 年に Camille が 2.5ha を取得** ✅
- 現在は **古樹 3 区画**（**樹齢 45 年超**）。**区画ごとに別々に醸造してからアッサンブラージュ** ✅
- **1971 年から**このキュヴェを造っている ✅
- 公式は英国のシャンパーニュ著述家 Michael Edwards の評として、Les Chétillons を
  "one of the most beautiful pieces of land of Champagne" と引用している ✅
- ⚠️ **現在の面積は非公表。**「1930 年に 2.5ha 取得」と「3 区画」しか書かれておらず、
  **今の作付面積が 2.5ha のままかは不明。**（→ Open Questions 3）

**Le Montjoly**（Le Mesnil-sur-Oger, Grand Cru）✅
- **Le Mesnil の他の区画より粘土（clay）の比率が高く、火打石（flints）を含み、土壌が深い** ✅
- **7 区画**。**それぞれ別々に、異なる方法で醸造される** ✅
- **2019 年に新区画として立ち上げ**（＝ラインナップ中もっとも新しい畑）✅

⚠️ **「19ha すべてがグラン・クリュ」とは公式に書かれていない。**
公式は一貫して「**principalement / mainly**（主に）この 4 村」という言い方をする。
**残りがどこかは公式に記述が無い。**（→ Open Questions 2、および §⚠️ 言ってはいけないこと）

---

## Farming

| 項目 | 公式の記述 | |
|---|---|---|
| **認証** | 🔴 **HVE（Haute Valeur Environnementale／高環境価値）認証** | ✅ **FR ページのみ** |
| **オーガニック** | **記述が一切無い** | ❓ |
| **ビオディナミ** | **記述が一切無い** | ❓ |
| **収穫** | **房ごと（whole bunches / grappes entières）手摘み**。圧搾機まで丁寧に運搬 | ✅ |
| **植栽** | **セレクション・マサル（sélection massale）を代々自家で開発・維持** | ✅ |
| **樹齢管理** | 畑を維持・高齢化させ、現在平均 **30 年超** | ✅ |
| **姿勢** | 「稀少な宝の頭に立っているという自覚」のもと、**土地・人・環境を尊重して最良のブドウを得る**ことを目的に栽培法を毎年適応させる | ✅ |
| 除草剤・耕起・被覆作物 | **記述なし** | ❓ |
| 収量 | **記述なし** | ❓ |

### 🔴 EN と FR の非対称（重要）

| | 記述 |
|---|---|
| **FR** `/fr/vignoble` | 「nos modes de culture **certifiée HVE (Haute Valeur Environnementale)**」＝ **HVE 認証を明示** ✅ |
| **EN** `/en/vineyard` | 「we use **sustainable farming methods**」＝ **HVE への言及なし** ✅ |

⚠️ 同じ段落の EN/FR で、**FR にだけ認証名がある。**これは矛盾ではなく**翻訳の非対称**（EN が古い）と読める。
**採用するのは FR の「HVE 認証」**。ただし**取得年・認証レベル（Niveau 3 か否か）は公式に無い**。
→ 現場では「**HVE（高環境価値）認証を取得している**」まで。**それ以上を足さない。**

🔴 **オーガニックでもビオディナミでもない。公式は一言も書いていない。**
Champagne の grower を「自然派」と括る客の期待に、**この house は乗らない。**（→ §⚠️ 言ってはいけないこと）

---

## Winemaking

### 工程（公式 `/en/winemaking` ＋ `/fr/elaboration`）✅

1. **成熟度を厳密に追跡**したうえで、**房ごと手摘み**、丁寧に圧搾機へ運ぶ
2. **圧搾に最も注意を払う。ゆっくり・繊細に**行い、**果汁を分割（fractionner）して、キュヴェに使う最良の画分だけを隔離する**
3. **小型ステンレスタンクで温度管理下に発酵。**タンクの中身は**テロワール名と圧搾画分の別で明確に識別**される
4. **細かい澱の上で熟成（élevés sur lies fines）。**定期的に試飲してアッサンブラージュに備える
5. アッサンブラージュ → 瓶詰め → **セラーで二次発酵と緩慢な熟成**。**遮光・定温**が第三アロマ（tertiary）を作る
6. **デゴルジュマン → ドザージュ（brut / extra-brut などタイプに応じて量を変える）→ 打栓**

### 🔴 Réserve Perpétuelle（永久リザーヴ）— この house の中核 ✅

| | |
|---|---|
| **方式** | **ソレラ方式に着想を得た（inspired by the Solera Method）**永久リザーヴ ✅ |
| **起点** | **1988 年**。以降のヴィンテージが積層 ✅ |
| **層の数** | ⚠️ **25 年分以上**（Réserve テクニカルシート）／ **20 年分以上**（`/en/winemaking` 本文） |
| **容器** | **ステンレスタンク・コンクリートタンク・大樽（big casks）** ✅（Monsieur Victor シートに記載） |
| **使われるキュヴェ** | `Réserve`（**リザーヴワイン 45% 以上**）／ `Grande Réserve` `Extra Brut`（**最良部分を約 20%**）／ `L'Étonnant Monsieur Victor`（**1988 年以降の最良のタンクを厳選し、ほぼ等量**） ✅ |

🔴 **公式サイト全体で木（樽）が出てくるのは、この永久リザーヴの「big casks」ただ 1 箇所である。**
発酵は**小型ステンレス**、と明記されている。**「樽発酵」「新樽◯%」は公式に存在しない。**

### MLF（マロラクティック発酵）

✅ **`Les Montjolys` のシートにのみ「Partial Malo（部分的マロ）」の記載がある。**
❓ **他の 6 キュヴェについては、公式に MLF の記述が一切無い。**
→ **「マロをブロックしている」とも「完全マロ」とも言えない。**（→ Open Questions 5）

### 熟成期間（公式シートより）✅

| キュヴェ | シュール・リー | 追加 |
|---|---|---|
| `Grande Réserve` / `Extra Brut` | **最低 36 ヶ月** | — |
| `Les Montjolys` | **最低 6 年** | — |
| `Les Chétillons` | **最低 72 ヶ月（6 年）** | **デゴルジュマン後さらに 1 年**コルクを打った状態で寝かせてからリリース |
| `L'Étonnant Monsieur Victor` | — | **6 年間、天然コルク栓の下で熟成**（王冠ではなくコルクで二次発酵・熟成） |

### 哲学 ✅
公式のモットー: **「どのワインの背後にも、ひとつの土壌と、それを造る土地の人間がいる」**
（"Behind every wine, there is a soil and a local man who makes it." / "Derrière chaque vin, il y a un terroir et l'homme qui le fait."）

---

## Style

✅ 公式が自らのブラン・ド・ブランを表す語は 7 つ、EN/FR で完全に一致している:
**finesse（繊細さ）／ elegance（優雅さ）／ freshness（新鮮さ）／ droiture（真直ぐさ・righteousness）／
purity（純度）／ texture（テクスチャー）／ minerality（ミネラリティ）**

✅ 醸造の目的は「**シャルドネの全体的なバランスと品種アロマを守ること**」。
圧搾直後からアッサンブラージュまで、**テロワールの最も代表的な性格を保存する**ことに専念する。

✅ 果汁の選別・画分の隔離は、**ミネラリティ・柑橘・繊細さ**という
「Pierre Péters のシャンパーニュ固有の性格」を得るために行われる、と明記されている。

✅ **`Les Chétillons` はレンジの中で最も要求の厳しいワイン**であり、**純粋な Mesnil の単一畑**。
公式の形容は **racé（気品と骨格）／ powerful ／ mineral**、
FR は「**Le Mesnil sur Oger の白亜の力を全面的に表現する**」と書く。

✅ **`Les Montjolys` は Chétillons の兄弟だが、粘土質ゆえに「若いうちの厳格さ（youthful austerity）が
おそらく Les Chétillons より少ない」**とシートが明記する。**この 2 本の対比は公式が自ら立てている。**

---

## Important Cuvées

### 公式の現行ラインナップ = **7 キュヴェ** ✅
ナビゲーション `/en/vintage` の並び順そのまま:
**Réserve → La Grande Réserve → Extra Brut → L'Esprit → Les Chétillons → Les Montjolys → L'Étonnant Monsieur Victor**

⚠️ **`Héritage` はページが残っているがナビの現行 7 本に含まれない**（2019 年 100 周年の限定）。
⚠️ **`Rosé for Albane` は 2009 年の年表に出てくるだけで、キュヴェページが存在しない。**

### OBP リスト掲載 6 本 🔍✅

| # | OBP 印字 | VT | 価格 | 公式キュヴェ | 公式シート | canonical |
|---|---|---|---|---|---|---|
| 1 | `'Cuvée de Réserve,' Grand Cru Brut` | NV | $235 | **Cuvée de Réserve**（Blanc de Blancs） | ✅ PDF | **登録済**（NV） |
| 2 | `'L'Esprit,' Grand Cru Brut` | **2018** | $390 | **Cuvée Millésimée L'ESPRIT** | ✅ PDF | **登録済**（2013 / 2018） |
| 3 | `'Les Montjolys,' Grand Cru Brut` | **2015** | $800 | **Cuvée Les Montjolys** | ✅ PDF | **登録済**（2015） |
| 4 | `'L'Étonnant Monsieur Victor, Edition TB.17,' Grand Cru Brut` | NV | $860 | **L'Étonnant Monsieur Victor / Collection MK** | ✅ PDF | 🔴 **キュヴェは登録済だが OBP は `unresolved`** |
| 5 | `'Les Chétillons,' Grand Cru Brut` | **2012** | $1,580 | **Cuvée Spéciale Les Chétillons** | ✅ PDF | キュヴェ登録済／**2012 は未登録ヴィンテージ** |
| 6 | `'Les Chétillons,' Grand Cru Brut` | **2007** | $1,580 | 同上 | ✅ PDF | **登録済**（2007） |

**canonical 保有キュヴェ 5 件はすべて公式の現行 7 本に含まれる。誤登録は無い。**
**canonical に無い公式キュヴェ**: `La Grande Réserve` / `Extra Brut`（どちらも OBP 未掲載なので実害なし）。

---

### 🔴 #4 の解決 — **「Edition TB.17」が何かは公式に書いてある**

公式テクニカルシート `L'étonnant Monsieur Victor - EN.pdf` の記述 ✅:

> **各エディションに付されるコードは、①Victor が深く敬愛しパロディにしたアーティストの頭文字と、
> ②アッサンブラージュのベース年（09 = 2009、10 = 2010 …）を指す。**
> 例として **「TB for Tim Burton」** が挙げられている。

**したがって `Edition TB.17` = 「Tim Burton」に因むエディション ＋ ベース年 2017。** ✅

🔴 **`.17` はヴィンテージではない。**このワインは**マルチヴィンテージ**であり、
**1988 年以降の永久リザーヴの最良タンク**と、**Chétillon のテロワールの直近収穫のワイン**を
**ほぼ等量でブレンド**したものである。**17 はそのブレンドのベース年にすぎない。**
公式は「**古いヴィンテージが若いワインを教育し、若いワインがその個性と若さで全体を豊かにする**」と書く。
OBP が `NV` として印字しているのは**正しい**。

⚠️ **HTML ページと PDF で頭文字が食い違う。**
`/en/cuvee-l-etonnant-monsieur-victor` の HTML は **「(TM for Tim Burton)」**、
テクニカルシート PDF は **「(TB for Tim Burton)」**。
**Tim Burton の頭文字は TB であり、OBP の印字も `TB.17`。PDF が正・HTML が誤植**と判断する。
両方を残す。**現場で「TM」を口にしない。**

✅ 公式のもう一つの表記: このワインは **「Collection MK」** と題されている。
❓ **MK が何の略かは公式に記述が無い。**（→ Open Questions 8）

✅ **なぜこのワインが存在するか（公式の言葉）**: 単一ヴィンテージ・単一畑シャンパーニュという
**現在の潮流に逆らい**、**マルチヴィンテージのアッサンブラージュというシャンパーニュ本来の savoir-faire** で
**造りうる最高のマルチヴィンテージ**を提示する、という宣言。**Chétillons のアンチテーゼとして設計されている。**

---

### キュヴェ別の技術情報（全 7 本・公式シートより）✅

| キュヴェ | 構成 | ドザージュ | 熟成 |
|---|---|---|---|
| **Cuvée de Réserve** BdB | シャルドネ 100%・コート・デ・ブランのグラン・クリュ村。**リザーヴワイン 45% 以上**を加える。永久リザーヴは**ソレラ着想・25 年分以上・1988 年起点** | **6–7 g/L** | ❓ 非公表 |
| **La Grande Réserve** BdB GC | **Le Mesnil / Avize / Cramant / Oger の最上区画 4 つを厳選**し、**永久リザーヴの最良部分を約 20%** ブレンド | **5 g/L** | **最低 36 ヶ月シュール・リー** |
| **Extra Brut** BdB GC | ⚠️ **PDF は Grande Réserve と全く同じ記述**（4 区画＋永久リザーヴ 20%）。**HTML は「実際には単一収穫年のミレジム」**と書く | **2 g/L** | **最低 36 ヶ月シュール・リー**（PDF） |
| **Cuvée Millésimée L'ESPRIT** BdB GC | **Le Mesnil / Avize / Cramant / Oger の 4 つの単一畑**。**グラン・クリュ・シャルドネ 100%**。**最良の収穫年のみ** | **4.5–5.5 g/L**（ヴィンテージと成熟度で変える） | ❓ 非公表 |
| **Cuvée Spéciale LES CHÉTILLONS** BdB GC | **Le Mesnil の lieu-dit Les Chétillons の古樹 3 区画。**グラン・クリュ・シャルドネ 100%・単一畑ミレジム | **3.5–4.5 g/L** | **最低 72 ヶ月シュール・リー ＋ デゴルジュ後 1 年** |
| **Cuvée LES MONTJOLYS** BdB GC | **Le Mesnil の lieu-dit Le Montjoly の 7 区画**。粘土＋火打石・深い土壌。**区画別に異なる醸造**。**Partial Malo**。極めて稀少 | **3.5–4.5 g/L** | **最低 6 年シュール・リー** |
| **L'ÉTONNANT MONSIEUR VICTOR** BdB GC（Collection MK） | **永久リザーヴ（1988 年〜、inox・コンクリート・大樽）の最良タンク** ＋ **Chétillon の直近収穫**を**ほぼ等量**。ラベルは息子 Victor の作品で**1 本ずつ異なる** | **3.5–4.5 g/L** | **6 年間、天然コルク栓下で熟成** |
| *(参考)* **Cuvée HÉRITAGE** BdB GC | **1921/1947/1959/1964/1966/1969/1973/1976/1979/1982/1985/1988/1990/1996/2002/2004/2006/2008 の秘蔵ボトルを開栓し、2010 年の最良のワインとブレンドして再瓶詰め・再発泡させた**。Camille / Pierre / François / Rodolphe の 4 世代へのオマージュ。**2019 年 100 周年限定** | **4 g/L** | ❓ |

⚠️ **Héritage の公式説明は「19 ヴィンテージ」だが、列挙されているのは 18 年。**
**2010 年（ブレンド相手）を数えて 19** と読むのが自然だが、**公式には明示が無い。** 両方残す。

### 公式掲載の第三者評価（`Professional Rating`、公式サイト上の更新表記は **2018 年 9 月**）✅

| キュヴェ | 主な点数 |
|---|---|
| Cuvée de Réserve | Wine Spectator 93 / Tyson Stelzer 94 / Vinous 92 / Wine Advocate 91 / Gault-Millau 16.5 |
| Extra Brut | Gault-Millau **17.5** / Wine Advocate 92 |
| L'Esprit 2010 | Bettane & Desseauve **17.5** / Wine Advocate 93 / Vinous 92 |
| L'Esprit 2012 | Wine Spectator 93 / Vinous 93 / Wine Advocate 92 |
| L'Esprit 2013 | Vinous 93 / Wine Advocate 92+ |
| **Les Chétillons 2008** | **Decanter 99** / Wine Advocate 96 / Wine Spectator 95 / Vinous 95+ / RVF 18.5 |
| **Les Chétillons Œnothèque 2002** | **Wine Spectator 97** / Vinous 96 / Wine Advocate 95 / **RVF 19/20** |
| Les Chétillons 2009 | Wine Advocate 95 / Tyson Stelzer 96 / Vinous 95 |
| Les Chétillons 2010 | Wine Spectator 95 / Wine Advocate 93 / Bettane & Desseauve 18.5 |
| Les Chétillons 2011 | Wine Advocate 94 / Vinous 93 |
| L'Étonnant Monsieur Victor | Wine Advocate 94 / RVF 18 / Vinous 93 / Bettane & Desseauve 17 |

🔴 **OBP に載っている 2 本のヴィンテージ（Chétillons 2012 / 2007）の点数は公式に無い。**
**リストの 2 本について「◯点」と言わない。**（→ §⚠️ 言ってはいけないこと）

---

## Staff Notes

> この節は上記の ✅ からのみ構成している。裏の取れていない事柄は書いていない。

**一行で言うと** — 「**Le Mesnil の生粋のブラン・ド・ブラン専門家。1919 年から自社畑のシャルドネだけ、
6 世代。1988 年から積み上げた永久リザーヴと、1930 年に買った Les Chétillons の古樹**」。

### ゲストへの説明の芯（3 点）

**1. 全部が Le Mesnil を中心としたグラン・クリュのシャルドネ。他は何も造らない。**
19ha 強、**Le Mesnil-sur-Oger / Oger / Cramant / Avize** の 4 村。**露出した白亜**の上、**東向き斜面**。
**ブドウは買わない — 自社畑だけ**（récoltant）。**1919 年に Camille Péters が、シャンパーニュの
栽培家として最初期に「ネゴシアンに売らず、自分の名で瓶詰めする」と決めた**ところから始まっている。
**セレクション・マサルを代々自家で維持**していて、平均樹齢は 30 年超。

**2. 🔴 Réserve Perpétuelle — この家を語るなら、まずこれ。**
**ソレラ方式に着想を得た永久リザーヴ**。**1988 年を起点に、25 年分以上のヴィンテージが積層**している。
容器は**ステンレス・コンクリート・大樽**。
- **`Cuvée de Réserve`（$235）は、このリザーヴを 45% 以上入れている。**
  NV の入門であって、実際には「四半世紀分の記憶が半分近く入っているワイン」。
  **この一言でグラス売り／ボトル最安のシャンパーニュの説得力が変わる。**
- **`L'Étonnant Monsieur Victor`（$860）は、その永久リザーヴの最良タンクと、
  Chétillon の直近収穫を「ほぼ等量」でブレンドしたもの。**
  公式の言葉で「**古いヴィンテージが若いワインを教育し、若いワインが全体を若さで豊かにする**」。
  **6 年間、王冠ではなく天然コルクの下で熟成**する。**ラベルは当主の息子 Victor が描いており、1 本ごとに違う。**

**3. Les Chétillons — 1930 年に買った 3 区画、樹齢 45 年超、1971 年から。**
Le Mesnil の lieu-dit。**区画ごとに別々に醸造してからアッサンブラージュ**する単一畑ミレジム。
**最低 72 ヶ月シュール・リー、さらにデゴルジュマン後 1 年コルクの下で寝かせてから出荷。**
**リストの中でこの house が最も要求の厳しいワインだと公式が自認している。**
英国の著述家 Michael Edwards が "one of the most beautiful pieces of land of Champagne" と評した、と
**公式サイト自身が引用している**（だから安全に言える）。

### 🔴 リストで気をつけること

**① `Edition TB.17` を訊かれたら**
「**TB は Victor が敬愛してパロディにしたアーティスト Tim Burton の頭文字、17 はブレンドのベース年 2017 です。
ヴィンテージではありません。**これはマルチヴィンテージで、1988 年からの永久リザーヴと
Chétillon の若いワインをほぼ半々にしたものです」
→ **`.17` を「2017 年のシャンパン」と説明した瞬間に間違い。**

**② Les Chétillons が 2012 と 2007 の 2 ヴィンテージある（同価格 $1,580）**
どちらも同じ畑・同じ造り。**差は年と熟成期間だけ。**
2007 は 2012 より **5 年長く**セラーで時間を過ごしている。
**縦で 2 本並べられる数少ない機会**であり、**この 2 本を並べて提案できることが、このリストの最大の武器。**
⚠️ **ただし公式に 2007 / 2012 の点数もテイスティングノートも無い。**
ヴィンテージの性格を語らず、**「畑が同じで、時間だけが違う」**という軸で語る。

**③ Montjolys（$800）と Chétillons（$1,580）の対比 — 公式が自分で立てている軸**
どちらも **Le Mesnil の単一 lieu-dit**。違いは土壌。
- **Chétillons = 白亜。**力とミネラル、若いうちは厳格。**3 区画・樹齢 45 年超・1930 年取得。**
- **Montjolys = 粘土＋火打石で土壌が深い。7 区画・区画別に異なる醸造・部分マロ。**
  公式が「**Chétillons ほど若いうちの厳格さが無い**」と書いている。
  **2019 年に立ち上げた新しい畑で、極めて稀少。**
→ **「今夜開けるなら Montjolys、寝かせるなら Chétillons」**という提案が、**公式の記述の範囲内で成立する。**

**④ 価格の階段が説明できる**
$235 Réserve（永久リザーヴ 45%・NV）→ $390 L'Esprit 2018（**4 つのグラン・クリュ村の単一畑・最良年のみ**）
→ $800 Montjolys 2015（**単一 lieu-dit・粘土**）→ $860 Monsieur Victor（**永久リザーヴの最良タンク半分**）
→ $1,580 Chétillons（**単一 lieu-dit・白亜・古樹・7 年熟成**）
**「村 → 4 つの畑 → ひとつの畑 → 時間そのもの」**という登り方になっている。

### ⚠️ 現時点で言ってはいけないこと

- 🔴 **「ビオ／オーガニック／ビオディナミ」** — **公式サイトに一言も無い。**
  言えるのは **「HVE（高環境価値）認証」** まで。**認証年もレベルも公式に無いので足さない。**
- 🔴 **「Demeter」「Biodyvin」「Ecocert」** などの認証機関名 — **一切記述が無い。言わない。**
- 🔴 **「樽発酵」「新樽◯%」「木樽熟成」** — 発酵は**小型ステンレス**と明記されている。
  公式で木が出るのは**永久リザーヴを貯める「大樽」1 箇所だけ。**
- 🔴 **「マロラクティック発酵をブロックしている」／「完全マロ」** — どちらも公式に無い。
  **書かれているのは `Les Montjolys` の「部分マロ」だけ。**他のキュヴェは不明。
- 🔴 **`Edition TB.17` を「2017 年ヴィンテージ」と説明する** — 誤り。**マルチヴィンテージ。**
- 🔴 **「TM」** — HTML 側の誤植。**PDF と OBP 印字の「TB」が正。**
- 🔴 **「Pierre Péters さんが今も造っている」** — 誤り。**Pierre は 1967 年に引退**（1944–1967 が在任）。
  **現当主は 2008 年から Rodolphe Péters。`Pierre Péters` は 1946 年からのブランド名。**
- ⚠️ **「Rodolphe が現在の当主です」と断定する場合** — 公式年表は **2019 年で止まっている**。
  2019 年時点の記述に基づく。**より新しい確認は取れていない。**
- 🔴 **「19ha すべてがグラン・クリュ」** — 公式は一貫して「**主に**この 4 村」。断定しない。
- 🔴 **Chétillons 2012 / 2007 の点数・評価** — **公式が載せているのは 2002 / 2008 / 2009 / 2010 / 2011 だけ。**
  **リストの 2 本の点数は公式に存在しない。**
- 🔴 **「Les Chétillons は最良年にしか造らない」と断定する** — **公式内で食い違っている**（§⚠️ 参照）。
  安全な言い方は「**単一収穫年のミレジム**」まで。
- ⚠️ **「Rosé for Albane があります」** — **現行キュヴェ一覧に無い。**2009 年に出たという年表の記述のみ。
- ⚠️ **「Héritage」** — **2019 年 100 周年の限定。**現行ラインナップではない。
- ⚠️ **「ソレラ方式です」と断定** — 公式は「**ソレラ方式に着想を得た（inspired by）**」。この差を守る。
- ⚠️ **Chétillons の現在の面積** — **「1930 年に 2.5ha 取得」しか公式に無い。**
  **「2.5ha を今も耕している」とは書かれていない。**

---

## Akio's Insight

*（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）*

---

## Canonical Conflict

**重複 canonical レコードは無い。**
`producer:pierre-peters` は 1 件のみで、姓・屋号を共有する別レコードは存在しない。
配下 5 キュヴェもすべて別物であり（`Réserve` / `L'Esprit` / `Monsieur Victor` / `Les Chétillons` / `Les Montjolys`）、
**公式の現行 7 キュヴェと 1:1 で対応する。誤登録・重複ともに検出されなかった。**
既存の `research/canonical_conflicts/REGISTER.md`（**第 2 版・登録 20 件**）を先に確認したが、
**Pierre Péters は P-1〜P-7 / C-1〜C-5 / V-1〜V-4 / S-1〜S-4 のいずれにも登場しない。新規の重複衝突も無い。**

**ただしモデル上の衝突が 1 件ある。**
🔴 **これは REGISTER.md（第 2 版）の既存カテゴリ `CAT-5 layer_boundary` の新規インスタンスである。**
**Pierre Péters は REGISTER.md に未登録。V-1（Krug）V-3（Dom Pérignon）V-4（Prévost）と同型として
`V-5` の追記が必要。**（**REGISTER.md 自体は編集していない。**）

**① 衝突している canonical ID**
`cuvee:pierre-peters-l-etonnant-monsieur-victor-blanc-de-blancs-grand-cru`（相当）
— canonical 上は `L'Étonnant Monsieur Victor Blanc de Blancs Grand Cru`、**vintages = `["NV"]` の 1 行のみ**。
**レコード同士は衝突していない。衝突しているのは「エディション」がどの層に属するかである。**

**② なぜ衝突（＝層の境界の破綻）か**
このキュヴェは **NV（マルチヴィンテージ）でありながら、`TB.17` のような「エディション」単位で
別個のワインとして流通する。**エディションは **①アーティスト頭文字 ②アッサンブラージュのベース年**の
2 要素からなり、**ヴィンテージではない。**
🔴 **V-1（Krug）とは失敗の向きが逆である。**

| | Krug Grande Cuvée（V-1） | **Pierre Péters Monsieur Victor（本件）** |
|---|---|---|
| canonical の状態 | **12 行**。`release_label`(162–173ème) と `base_year`(2006–2017) を**vintage 層に置いている** | **1 行だけ（`NV`）。エディションがどこにも記録されていない** |
| 失敗の型 | 層に**置いてはいけないものを置いた** | 層に**置く場所が無いので消えた** |
| OBP | 3 本 unresolved | **1 本 unresolved** |

**どちらも同じ根（`(cuvée, vintage_year)` が NV のリリース単位を表現できない）から出ている。**

**③ Evidence**
- ✅ 公式テクニカルシート `L'étonnant Monsieur Victor - EN.pdf`:
  「各エディションのコードは、**アーティストの頭文字（TB = Tim Burton）**と
  **アッサンブラージュのベース年**（09 = 2009、10 = 2010 …）を指す」
  → **`TB.17` は「Tim Burton エディション／ベース年 2017」。ヴィンテージではない。**
- ✅ 公式は 2016 年の年表でこれを **「シリーズ（vintage series）」** と呼んでいる。
  **リリースが反復することを公式が前提にしている。**
- 🔍 OBP 印字: `'L'Étonnant Monsieur Victor, Edition TB.17,' Grand Cru Brut` / **VT = NV** / $860
  → **メニューはエディションをキュヴェ名の一部として印字している**（V-1 の Krug、V-3 の Plénitude と同じ挙動）
- 🔍 **canonical にキュヴェは存在するのに、OBP の該当ボトルは `cuvee_state=unresolved` で滞留。**
  印字の `, Edition TB.17,` がキュヴェ名の一部として照合され、一致しなかったためと考えられる。

**④ OBP への影響**
**6 本中 1 本**（$860、**この生産者で 2 番目に高い**）が **未解決のまま。**
canonical に受け皿があるのに紐づかない。
将来 `TB.18` `TB.19` 等が入荷すれば、**同じキュヴェの別エディションが毎回新規キュヴェ候補として湧き続ける。**
🔍 これで **CAT-5 の OBP 未解決寄与は 11 本 → 12 本になる。**

**⑤ 推奨される解決策（実行しない）**
**個別対応しない。CAT-5 の決定（`base_year` / `release_label` / `lot` / `bottle_format` の
どれが identity でどれが属性か）に従属させる。**
本件が CAT-5 に足す論点は 1 つだけ:
🔴 **V-1 は「エディションが vintage 層に入っている」ケースだが、本件は「エディションがどこにも無い」ケースである。**
**規約は「どの層に置くか」だけでなく「置かれていない既存レコードをどう検出するか」も決める必要がある。**
（Péters のように 1 行しか無いレコードは、走査 5「(cuvée × 年) 重複」では**原理的に検出できない**。
本件は**メニュー印字と公式資料の突き合わせでしか見つからなかった。**）

**⑥ Confidence: High**
（エディション記法の意味を**公式 PDF で確定**・OBP の `unresolved` を実測・
canonical に受け皿が 1 行だけ存在することを確認済み。
**CAT-5 の新規インスタンスであるという判定への確信は高い。実装方針は未決。**）

---

## Sources

**すべて公式ドメイン `champagne-peters.com` の一次情報。非公式ソースは 1 件も使用していない。**

### HTML（EN 15 / FR 6）
| URL | 内容 |
|---|---|
| `/en/home` ・ `/fr/accueil` | 6 世代・1919 年・19ha・4 村・sélection massale・平均樹齢 |
| `/en/historical` ・ `/fr/historique` | **1858–2019 の公式年表**（本書 History の全出典） |
| `/en/vineyard` ・ `/fr/vignoble` | 19ha・白亜・東向き・**HVE 認証（FR のみ）**・Les Chétillons |
| `/en/winemaking` ・ `/fr/elaboration` | 圧搾・小型ステンレス発酵・シュール・リー・**リザーヴ 20 年分以上**・デゴルジュ |
| `/en/vintage` ・ `/fr/cuvees` | **現行 7 キュヴェの一覧**・スタイル 7 語・Chétillons の位置づけ |
| `/en/cuvee-reserve` … `/en/cuvee-heritage`（8 ページ） | 各キュヴェの説明・ドザージュ・**第三者評価（2018 年 9 月更新）** |
| `/en/awards` ・ `/fr/palmares` | 評価媒体のロゴのみ。**本文コンテンツ無し** |
| `/en/node/62` | 住所 **9 rue de l'Église, 51190 Le Mesnil sur Oger**・見学規定 |

### テクニカルシート PDF（7 本・全件取得済み）✅
`/sites/default/files/` 配下。HTML の「Fact sheet」リンクから。
`_sources/pierre-peters/` に保存:

| ファイル | 元 URL（末尾） | 本書で使った固有情報 |
|---|---|---|
| `reserve.pdf` | `Réserve - EN.pdf` | **リザーヴワイン 45% 以上・ソレラ着想・25 年分以上・1988 年起点** |
| `grande-reserve.pdf` | `Grande Reserve - EN.pdf` | **4 区画・永久リザーヴ約 20%・36 ヶ月シュール・リー** |
| `extra-brut.pdf` | `Extra Brut - EN.pdf` | 同上（⚠️ HTML と矛盾） |
| `esprit.pdf` | `L'esprit - EN.pdf` | **4 つの単一畑・最良年のみ・4.5–5.5 g/L** |
| `les-chetillons.pdf` | `Les Chétilons - EN.pdf` | **72 ヶ月シュール・リー＋デゴルジュ後 1 年**・⚠️「年を問わず」 |
| `les-montjolys.pdf` | `LES MONTJOLYS - EN.pdf` | **7 区画・粘土＋火打石・部分マロ・最低 6 年**・Chétillons との対比 |
| `etonnant-monsieur-victor.pdf` | `L'étonnant Monsieur Victor - EN.pdf` | 🔴 **エディション記法（TB = Tim Burton＋ベース年）**・**1988 年〜の永久リザーヴ＋Chétillon 直近収穫をほぼ等量**・**6 年コルク下熟成**・**永久リザーヴの容器（inox / コンクリート / 大樽）** |

❌ `heritage.pdf` は未取得（Héritage は OBP 未掲載・現行外のため優先度低）。

### 使用していないもの
Wikipedia / 小売・EC サイト / インポーター資料 / wine-searcher / Vivino / レビュー集約 / ブログ — **すべて不使用。**
公式サイト内に引用されている第三者評価（Wine Advocate / Wine Spectator / Vinous / RVF /
Bettane & Desseauve / Gault-Millau / Decanter / Tyson Stelzer / Richard Juhlin / Michael Edwards）は、
**公式が自ら掲載しているものだけ**を、**公式掲載の事実として**記載した。

---

## Confidence

| 節 | 判定 | 根拠 |
|---|---|---|
| **Identity** | **High** | 住所・世代数・業態・当主すべて公式。⚠️ 当主の**現在性のみ Medium** |
| **Overview** | **High** | すべて公式トップ＋畑ページ |
| **History** | **High** | **1858–2019 の年表が公式に存在する。**年号・人名・面積とも一次資料 |
| **Location** | **Medium-High** | 総面積・村・土壌・向きは確定。**村別内訳・区画面積は非公表** |
| **Farming** | **Medium** | **HVE 認証（FR のみ）**と手摘み・マサルは確定。**耕作の実務・収量・被覆作物は全面的に記述なし** |
| **Winemaking** | **Medium-High** | 工程・容器・熟成期間・ドザージュは PDF で確定。**MLF は 1 キュヴェのみ・圧搾歩留り/酵母は記述なし** |
| **Style** | **High** | 公式が自ら 7 語で定義し、EN/FR が完全一致 |
| **Important Cuvées** | **High** | **現行 7 キュヴェ全部に公式テクニカルシートがある。OBP 6 本すべてが公式キュヴェに確定した。**未解決だった 1 本も公式記述で解決 |
| **Staff Notes** | **High** | すべて ✅ からのみ構成 |
| **Canonical Conflict** | **High** | 重複無しを確認・モデル衝突 1 件を公式記述と実測で確定 |
| | | |
| **総合** | **Medium-High** | **70% の基準を満たす。**必須項目（Identity / Overview / Location / **Farming** / Important Cuvées（**OBP 紐付け 6/6**）/ Staff Notes の芯 3 点 / ⚠️ リスト）がすべて埋まり、**OBP の未解決 1 本を公式一次資料で解決した。**薄いのは Farming の実務と MLF |

---

## Open Questions

1. ❓ 🔴 **Rodolphe Péters は 2026 年現在も当主か。**公式年表は **2019 年で終わっている。**
   2019 年以降の経営・技術陣の異動は公式に記述が無い。**「現在性未確認」。**
2. ❓ **19ha の村別内訳。**公式は「**主に**（principalement / mainly）Le Mesnil / Oger / Cramant / Avize」
   としか書かず、**残りの所在も、グラン・クリュ以外の保有の有無も不明。**
3. ❓ **Les Chétillons の現在の面積。**公式にあるのは「**1930 年に 2.5ha 取得**」と「**3 区画**」のみ。
   現在の作付面積は非公表。
4. ❓ **`Cuvée de Réserve` はラベル上グラン・クリュか。**PDF の見出しで **7 本中このキュヴェだけ
   "GRAND CRU" が無い**（本文は「グラン・クリュ村のシャルドネのみ」）。OBP と canonical は
   どちらも "Grand Cru" を含めている。**表記の根拠が公式で確認できない。**
5. ❓ **MLF の方針。**`Les Montjolys` の「**Partial Malo**」以外、7 キュヴェのどれにも記述が無い。
6. ❓ **Réserve Perpétuelle の運用詳細。**容器の比率（inox / コンクリート / 大樽）、年間の引き出し・
   補充量、⚠️ 現在の層数（**20 年分以上 / 25 年分以上**の食い違い）。
7. ❓ **`Extra Brut` はミレジムか NV か。**HTML と PDF が真っ向から矛盾する（§⚠️ #4）。
8. ❓ **`L'Étonnant Monsieur Victor` の既刊エディション一覧。**公式は記法（頭文字＋ベース年）を
   説明するのみで、**発売済みエディションの一覧が無い。**`TB.17` 以外に何が存在するか不明。
   **「Collection MK」の MK が何の略かも記述が無い。**
9. ❓ **`Rosé for Albane` と `Héritage` の現況。**Rosé は 2009 年の年表にあるだけで**キュヴェページが無い**。
   Héritage は**ページはあるがナビの現行 7 本に入らない**。どちらも生産継続か不明。
10. ❓ **HVE 認証の取得年・レベル（Niveau 3 か）。**FR ページに認証名があるだけ。
11. ❓ **栽培の実務**（除草剤の使用有無・耕起・被覆作物・防除方針）と**収量**。全面的に記述なし。
12. ❓ **Victor Péters の役割。**ラベルの作者としてのみ登場し、**経営・醸造への関与は不明。**
13. ❓ **圧搾の詳細。**「ゆっくり・繊細に、画分を隔離する」とあるが、**cuvée / taille の切り分け基準、
    使用する圧搾機、歩留りは非公表。**酵母（自然発酵か培養か）も記述なし。
14. ❓ **`Cuvée de Réserve` と `L'Esprit` の熟成期間。**他の 5 キュヴェには明記があるが、
    この 2 本だけ公式に月数が無い。
