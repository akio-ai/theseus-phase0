# Canonical Conflict Register

> 🔴 **architecture の課題票。research の成果物ではない。**
> **自動で片方を選ばない。canonical を書き換えない。解決しない。ADR も書かない。エスカレーションする。**
>
> 更新: 2026-08-04（第 2 版）／ 対象 `theseus-phase0@main` `migration/out/resolved/`
> 生産者 384 / キュヴェ 781 / ヴィンテージ 568 ／ **読み取りのみ・canonical 無変更**
>
> ## ⏸ 停止条件に到達した
> **登録された真の衝突: 20 件**（目標 20–30 件の下限に到達）。
> 指示に従い**自動走査をここで停止**し、§D に**カテゴリ案**を提示する。**解決策は設計しない。**

---

## 走査の網羅範囲（何を見て、何を見ていないか）

| # | 走査 | 結果 |
|---|---|---|
| 1 | producer 名の正規化キー完全一致 | 1 組 → **P-1** |
| 2 | producer 名のトークン包含 | 13 組 → 真 5・誤検出 8 |
| 3 | 同一 producer 配下の cuvée 名重複・包含 | 50 組 → 真 5・誤検出 45 |
| 4 | 参照整合性（孤児 cuvée / 孤児 vintage） | **0 件。健全** |
| 5 | vintage の (cuvée × 年) 重複 | 5 組 → **V-1〜V-4** |
| 6 | legacy_id の衝突 | 同一 entity type 内 **0 件**。producer↔cuvée 間 891 → **S-3** |
| 7 | `superseded_live_ids` / `decisions` の残存 | 24 / 26 → **S-1, S-2** |
| 8 | cuvée 名がスタイル語のみ | 38 件 → **C-4** |
| 9 | cuvée 名 == producer 名 | 69 件 → **C-5** |
| 10 | nv フラグと vintage_year の矛盾 | 2 件 → **V-3** に内包 |
| 11 | entity_type の分離状況 | 36 件が 3 ファイルに分離 → **S-4** |
| 12 | OBP: 生産者一致だがキュヴェが別 producer に存在 | 134 行。**大半は「同じ畑を複数の造り手が造る」正常系** |

**見ていないもの**: `db_wine.json`（生成物）／ `intake/store/`（店舗実データ）／ 味わい記述の内容整合性。

---

## 登録一覧（20 件）

| # | 分類 | 対象 | 頻度 | OBP 影響 | Conf |
|---|---|---|---|---|---|
| **P-1** | 🔴 正規化キー衝突（**canonical は裁定済み**） | Domaine Leroy / Maison Leroy | 1 組（キー完全一致は全 DB でこれのみ） | **1 本が誤実体に割当** | High |
| **P-2** | 実体分裂 | Famille Mousse / Mousse Fils | 1 組 | **3 本が偽の未解決** | High |
| **P-3** | 実体分裂 | Agrapart & Fils / Pascal Agrapart | 1 組 | 2 本。Packet C で衝突確定 | High |
| **P-4** | 実体分裂 | Geoffroy / René Geoffroy | 1 組 | 3 本 | Med-High |
| **P-5** | 実体分裂の疑い | Cyprien Arlaud / Domaine Arlaud | 1 組 | 1 本（実害なし） | Medium |
| **P-6** | ブランド軸の実体化 | Charles Dufour / 同 Françoise Martinot | 1 組 | 2 本（実害なし） | Medium |
| **P-7** | ブランド軸の実体化（**統合禁止**） | Chave / Chave Sélections | 1 組 | 11 本（正しく分離） | Medium |
| **C-1** | 🔴 語順・アクセント揺れ | Egly-Ouriet ミレジム 4 件＋畑名 2 件 | 6 レコード | **1 本 candidate 滞留** | High |
| **C-2** | 非ワイン混入 | Parker's Château Profile ×2 | 2 レコード | 0 本（分母汚染） | High |
| **C-3** | 命名規約の二重化 | Denis Mortet Lavaux-Saint-Jacques | 2 レコード | 3 本 | Med-High |
| **C-4** | 🔴 識別語なしキュヴェ名 | スタイル語のみの名前 | **38 レコード** | **38 本中 26 本 unresolved** | High |
| **C-5** | 冗長エンコード | cuvée 名 == producer 名 | **69 レコード** | 63 本（暗黙規約に依存） | High |
| **V-1** | 🔴 層のずれ（édition） | Krug Grande Cuvée 162–173ème | 12 レコード | **3 本 unresolved** | High |
| **V-2** | 層のずれ（容量） | Roederer Cristal 2013 Magnum | 1 組 | 0 本 | Medium |
| **V-3** | 層のずれ（Plénitude） | Dom Pérignon P2 / P3 / Œnothèque | 4 レコード（うち 2 は year 欠落） | **3 本 unresolved** | High |
| **V-4** | 層のずれ（lot） | Prévost LC21 / LC23 | 2 レコード | **5 本中 4 本が未解決** | High |
| **S-1** | 符号化破損（**裁定済み**） | `ch-teau-*` → `chateau-*` | **24 producer** | 0 本 | High |
| **S-2** | 🔴 裁定スキーマの不統一 | `decisions` の形が 3 種＋category 欠落 | 26 producer / 3 件が category なし | 間接（P-1 の原因） | High |
| **S-3** | キーの非一意 | legacy_id が producer と cuvée で重複 | **891 組** | 間接 | High |
| **S-4** | entity 境界の未文書化 | 3 側ファイルに 36 レコード | 36 レコード | 間接 | Medium |

---

## P-1 🔴 Domaine Leroy / Maison Leroy — **canonical は既に裁定済み。壊れているのは matcher の側**

**分類**: 正規化キー衝突（duplicate ではない）／**頻度**: 全 DB でこの 1 組のみ／**影響**: OBP 1 本が誤実体

**衝突している canonical ID**
`producer:domaine-leroy` ／ `producer:maison-leroy`

**なぜ重複に見えるか**
正規化が `Domaine` / `Maison` を接頭辞として除去するため、**両者とも `leroy` に潰れる**。
384 生産者中、正規化キーが完全一致するのは**この 1 組だけ**。

**Evidence — 🔴 canonical 自身が「統合するな」と明記している**
```
producer:maison-leroy .decisions:
  { "not_the_same_as": "producer:domaine-leroy",
    "reason": "**別法人**。… 名前一致は norm_name が Maison/Domaine を除去することによる
               **誤検出**であり、統合してはならない（S2 の producer_keep_separate と同一判断）。" }
  { "keep_separate": "Domaine Leroy（自社畑）と Maison Leroy（ネゴシアン）は別法人・別ワイン。
                      統合しない。Rémi Leroy はさらに無関係のシャンパーニュ生産者。" }
```
配下も非対称: `domaine-leroy` はグラン・クリュ 7 件のみ、`maison-leroy` は **`Fixin` 1 件のみ**。

**OBP への影響** 🔴
`Leroy 2009 Fixin $1,600` は intake が **`domaine-leroy` に `exact`** で割り当てたが、
**`Fixin` は `maison-leroy` 側にしか無い。** 生産者は「一致」なのにキュヴェが解決しない不整合。
**canonical は正しく、intake の matcher が `decisions` を読んでいないことが原因。**

**推奨される解決策（実行しない）**
統合ではない。**`decisions.keep_separate` / `not_the_same_as` を matcher が消費する仕組み**が要る。
現状これらは人間向けの散文として置かれているだけで、機械可読な制約になっていない。

**Confidence: High**（canonical の裁定文・キュヴェ分布・OBP 実害すべて確認）

---

## P-2 🔴 Famille Mousse / Mousse Fils

**分類**: 実体分裂／**頻度**: 1 組／**影響**: OBP 3 本が「存在しないキュヴェ」として Packet B に計上

**ID** `producer:famille-mousse`（cuvée `Terre d'Illite…`）／ `producer:mousse-fils`（cuvée **`Les Fortes Terres Extra Brut Special Club`**）
**Evidence** OBP 5 本すべてが `famille-mousse` に割当。うち **`Les Fortes Terres` 3 本が未解決だが、そのキュヴェは `mousse-fils` に実在**。
メニューは同一生産者を `Famille Moussé`（BdN 節）と `Moussé Famille`（**SPÉCIAL CLUB** 節）の 2 表記で印字し、canonical のキュヴェ名も `Special Club` を含む。**節・表記・キュヴェ名の 3 点が符合。**
**影響** 3 本。統合されれば Packet B から 3 件消える。
**推奨（実行しない）** 公式確認後に統合 or 親子明示。**自動統合は禁止。** **Confidence: High**

---

## P-3 Agrapart & Fils / Pascal Agrapart

**分類**: 実体分裂／**頻度**: 1 組／**影響**: 2 本＋Packet C で確実に衝突

**Evidence** 同名キュヴェが**別ヴィンテージで両実体に分散**:
`Minéral…`（and-fils **2018** / pascal **2015**）、`Experience…`（and-fils **2019** / pascal **2015**）。
`agrapart-and-fils` 側の 7 キュヴェ（7 Crus / Avizoise / Complantée / Terroirs / Vénus …）は Avize の実ラインナップと整合。
**Confidence: High**

---

## P-4 Geoffroy / René Geoffroy
**分類**: 実体分裂／**頻度**: 1 組／**影響**: 3 本
`geoffroy`（3 キュヴェ・OBP 0）と `rene-geoffroy`（1 キュヴェ・OBP 3）。キュヴェ名の重複は無いが**ラインナップが相互補完的**で、同一生産者を 2 回取り込んだ典型形。**Confidence: Medium-High**

## P-5 Cyprien Arlaud / Domaine Arlaud
**分類**: 実体分裂の疑い／**頻度**: 1 組／**影響**: 1 本（実害なし）
姓一致とトークン包含のみ。キュヴェの符合が無い。**Confidence: Medium**

## P-6 Charles Dufour / Charles Dufour / Françoise Martinot
**分類**: ブランド軸の実体化／**頻度**: 1 組／**影響**: 2 本（実害なし）
**新 Evidence**: 両者の cuvée `subregion` が**別の村** — `Landreville — Côte des Bar` と `Villenauxe-la-Grande — Côte des Bar`。
共同醸造ラベルを producer として実体化したケース。**個別統合より先に方針が要る。Confidence: Medium**

## P-7 Chave / Chave Sélections — **統合禁止**
**分類**: ブランド軸の実体化（正しく分離済み）／**頻度**: 1 組／**影響**: 11 本すべて正しい
ラインナップが明確に階層分離（自社畑 Hermitage/Saint-Joseph ⟷ ネゴシアン Côtes du Rhône / Crozes / "Offerus"）。
**重複ではない。** ただし P-1・P-6 ＋ Esprit Leflaive ＋ Olivier Leflaive と**同一構造**。**Confidence: Medium**

---

## C-1 🔴 Egly-Ouriet — 語順・アクセント揺れによる同一キュヴェの多重化

**分類**: 語順／アクセント揺れ／**頻度**: 6 レコード（781 中、3 件以上でキー衝突するのはここだけ）／**影響**: 1 本 candidate 滞留

| id | 表記 | vintages |
|---|---|---|
| `cuvee:egly-ouriet-extra-brut-grand-cru-millesime` | `Extra Brut Grand Cru Millésime` | 2015 |
| `cuvee:egly-ouriet-grand-cru-millesime-extra-brut` | `Grand Cru Millésimé Extra Brut` | 2012 |
| `cuvee:egly-ouriet-millesime-grand-cru-extra-brut` | `Millesime Grand Cru Extra Brut` | 2014, 2016 |
| `cuvee:egly-ouriet-millesime-grand-cru-brut` | `Millésime Grand Cru Brut` | 2013 |
| `cuvee:egly-ouriet-les-vignes-de-bisseuil-1er-cru-extra-brut` | `'Les Vignes de Bisseuil' 1er Cru Extra Brut` | NV |
| `cuvee:egly-ouriet-les-vignes-de-bisseuil-extra-brut` | `Les Vignes de Bisseuil Extra Brut` | NV |

上 4 件は**構成語が同一で語順とアクセントだけが違う**。下 2 件は `1er Cru` の有無のみ。
**影響** `'Les Vignes de Bisseuil,' Premier Cru Extra Brut`（NV, $400）が 2 件に同程度一致し
**`candidate` で滞留 → どの packet にも載らない。** ミレジム系は 2012–2016 が 4 レコードに分散。
**⚠️ `Brut` と `Extra Brut` は実際に別キュヴェの可能性**があるため一律統合はできない。**Confidence: High**

## C-2 非ワインレコードの混入
**分類**: entity_type 誤り／**頻度**: 2 レコード／**影響**: 0 本（分母汚染）
`Calon-Ségur — Parker's Château Profile` / `Cos d'Estournel — Parker's Château Profile` が cuvée として存在。両者ヴィンテージ 0 件。
**S-4 の分離済み 36 レコードと同じ処置が妥当。Confidence: High**

## C-3 Denis Mortet — 命名規約の二重化
**分類**: 命名規約／**頻度**: 2 レコード（同型は Packet B に 7 件）／**影響**: 3 本
`Gevrey-Chambertin 1er Cru 'Lavaux Saint-Jacques'`(2023) と `"Lavaux-Saint-Jacques"`(2015)。
**同一の畑を 2 つの規約で保持。Confidence: Medium-High**

## C-4 🔴 識別語を持たないキュヴェ名 — **最大の実害源**

**分類**: 識別子の不足／**頻度**: **canonical 38 レコード**／**影響**: **OBP 38 本中 26 本が unresolved**

**Evidence** 名前が**スタイル語のみ**（Brut / Extra / Grand Cru / Blanc de Blancs / Millésime …）で
構成され、**その生産者を特定する語を 1 つも含まない** cuvée が 38 件:
`Egly-Ouriet 'Grand Cru Brut'` / `'Grand Cru Extra Brut'`、`Bollinger 'Special Cuvée Brut'`、
`Billecart-Salmon 'Brut Rosé'`、`Doyard 'Blanc de Blancs Grand Cru Extra Brut'`、
`Dunoyer de Segonzac 'Blanc de Blancs Extra Brut Premier Cru'`、`Gosset 'Grand Millésime Brut'` …

**OBP への影響** メニュー側も同じくスタイル語のみで印字する行が 38 本あり、
**exact 6 / alias 6 / unresolved 26**。走査 12 では、この型の行が**他生産者のキュヴェ名と衝突**する例が
多数出た（`Dom Pérignon` の "Brut" が `Egly-Ouriet 'Grand Cru Brut'` と一致するなど）。
**生産者スコープで閉じているから事故になっていないだけで、名前そのものは識別子として機能していない。**

**推奨（実行しない）** キュヴェの identity をどこに置くか（名前／畑／スタイル属性の組）という
**モデルの問題**。個別のリネームでは解けない。**Confidence: High**

## C-5 冗長エンコード — cuvée 名 == producer 名
**分類**: 命名規約／**頻度**: **69 レコード**／**影響**: OBP 63 本がこの暗黙規約に依存
Bordeaux グランヴァン型（`Château Batailley` producer → `Château Batailley` cuvée）。
**intake の matcher はこれを特別扱いする分岐を持たないと Bordeaux が一切解決しない。**
規約として文書化されておらず、暗黙の前提になっている。**Confidence: High**

---

## V-1 🔴 Krug Grande Cuvée — édition が層をまたぐ

**分類**: 層のずれ（cuvée と vintage の境界）／**頻度**: 12 レコード／**影響**: **OBP 3 本 unresolved**

**Evidence** `cuvee:krug-grande-cuvee` 配下に **vintage_year=null の行が 12 件**あり、
識別しているのは `release_label`（162ème〜173ème Édition）と `base_year`(2006–2017) のみ。
**(cuvée, vintage_year) は一意でない。**
**影響** OBP は `'Grande Cuvée, 173ème Édition,' Brut` 等 3 本を掲載し、**édition をキュヴェ名の一部として印字**。
canonical は édition を vintage 層に置いている → **3 本とも unresolved。**
**推奨（実行しない）** NV の édition/mise をどの層の識別子とするかの決定。**Confidence: High**

## V-2 Louis Roederer Cristal 2013 — 容量が vintage 行を分ける
**分類**: 層のずれ（フォーマット）／**頻度**: 1 組／**影響**: 0 本
`…-2013` と `…-2013-magnum` が別行。`bottle_format` が identity の一部になっている。
**Confidence: Medium**

## V-3 🔴 Dom Pérignon — Plénitude が層をまたぐ＋整合性欠落
**分類**: 層のずれ＋データ整合性／**頻度**: 4 レコード／**影響**: **OBP 3 本 unresolved**
- 2002 が 2 行（標準／`release_label=P2`）
- **`nv=false` なのに `vintage_year` が無い行が 2 件**: `P3 Réserve de l'Abbaye` / `Œnothèque`（DB 全体でこの 2 件のみ）
- OBP は `2003 'Plénitude 2,' Brut` を**キュヴェ名として印字** → unresolved。
  さらに `2015 Brut` `2013 Brut` も unresolved（C-4 と複合）。
**Confidence: High**

## V-4 🔴 Jérôme Prévost — lot が identity
**分類**: 層のずれ（lot）／**頻度**: 2 レコード／**影響**: **OBP 5 本中 4 本が未解決**
`…-nv-lc21` / `…-nv-lc23` が `lot` のみで区別され、両者 vintage_year=null。
OBP は `'La Closerie, &,'`（2023/2021）が unresolved、`Les Beguines` / `Grand Cru` 表記も vintage 未解決。
**メニューが lot を年として印字している可能性**があり、⚠️ `Gueux は Grand Cru 村ではない`ためメニュー側の誤りも混在。
**Confidence: High**

---

## S-1 符号化破損 — **既に裁定済みの前例**
**分類**: 符号化破損／**頻度**: **24 producer**／**影響**: 0 本（解決済み）
crawler の slugify がアクセントを落とし `producer:ch-teau-*` を生成 → `superseded_live_ids` で吸収済み。
`decisions.category = "encoding_damage"`（15）/ `"punctuation_variant"`（5）/ `"prefix_word"`（4）。
**これは「canonical が既に conflict を in-band で解決した前例」であり、§D のカテゴリ案の土台になる。Confidence: High**

## S-2 🔴 裁定スキーマが統一されていない
**分類**: メタデータ規約／**頻度**: 26 producer が `decisions` を持ち、**形が 3 種類**／**影響**: 間接（**P-1 の直接原因**）
observed shapes:
1. `{supersedes, category, reason}` — 符号化破損型（category あり）
2. `{keep_separate: "…"}` — 統合禁止（**category なし**）
3. `{not_the_same_as: <id>, reason}` — 統合禁止（**category なし**）
**3 件が category を持たない。** そして **形 2・3 は機械可読な制約になっていない**ため、
intake の matcher が読み飛ばし、**P-1 の誤割当が発生した。**
**Confidence: High**

## S-3 legacy_id が entity type をまたいで非一意
**分類**: キー設計／**頻度**: **891 組**／**影響**: 間接
同一 legacy_id を producer と cuvée が同時に主張する（legacy の 1 行から両方を導出したため）。
**同一 entity type 内の衝突は 0 件**なので破損ではないが、**legacy_id を単独の join key に使えない。**
**Confidence: High**

## S-4 entity 境界が未文書化
**分類**: entity_type 境界／**頻度**: 36 レコード（vintage_reports 34 / appellation_references 1 / non_wine_beverages 1）／**影響**: 間接
非ワインを別ファイルに分離する運用は**既に始まっている**が、
`non_wine_beverages.json` が **1 件しか無い**一方で C-2 の記事レコードは cuvée 側に残っている。
**分離の基準が文書化されていないため、適用が一貫していない。Confidence: Medium**

---

## §C 誤検出として除外（54 組）— 再走査で必ず再検出される

| 類型 | 例 | 理由 |
|---|---|---|
| 色違い | `Dom Pérignon` / `… Rosé`、`Cristal Brut` / `Cristal Rosé`、`Célébris` / `Célébris Rosé`、`Crozes-Hermitage` / `… Blanc` | 別ワイン |
| 別アペラシオン | `Chambertin` / `Charmes-` / `Latricières-` / `Mazis-` / `Clos de Bèze`、`Montrachet` / `Puligny-` / `Chevalier-` / `Bâtard-` / `Bienvenues-` / `Criots-`、`Échézeaux` / `Grands Échézeaux`、`Corton` / `Corton-Charlemagne` | **intake の `NEVER_SAME` に既出** |
| 別畑 | `CASK 23` / `S.L.V.`、`Le Cèdre` / `GC (Grand Cèdre)` | 別キュヴェ |
| 別シャトー | `Château Latour` / `Louis Latour`、`Château Haut-Brion` / `Les Carmes Haut-Brion`、`Château Batailley` / `Château Haut-Batailley`、`Ridge Vineyards` / `Switchback Ridge`、`Domaine Leroy` / `Rémi Leroy` | 姓・地名の偶然一致 |
| 階層 | `Chablis` / `Chablis Grand Cru Valmur`、`Mâcon Milly-Lamartine` / `… "Clos du Four"` | 上位／下位 |
| **同じ畑を複数の造り手が造る** | 走査 12 の 134 行の大半（Bonnes-Mares を 6 ドメーヌが所有 等） | **正常系。衝突ではない** |

---

## §D カテゴリ案（**分類のみ。解決策は設計しない**）

20 件は **5 つのカテゴリ**に収まる。カテゴリ名は **canonical が既に `decisions.category` で使っている語彙を出発点**にした
（`encoding_damage` / `punctuation_variant` / `prefix_word` が実在する）。

### CAT-1 `identity_collision` — 正規化が別実体を同一視する
**該当**: P-1 ／ **件数** 1 ／ **頻度** 稀（キー完全一致は DB 全体で 1 組）／ **影響** 最大（誤割当が起きる）
正規化規則（接頭辞除去・冠詞除去）が、**実在する別法人を同じキーに潰す**。
canonical 側は `keep_separate` で正しく裁定しているのに、**その裁定が機械可読でない**ため下流が従えない。
既存語彙 `prefix_word` の裏返し。

### CAT-2 `entity_split` — 同一実体が複数レコードに割れている
**該当**: P-2 P-3 P-4 P-5 ／ **件数** 4 ／ **頻度** 低（384 中 8 レコード）／ **影響** 中（偽の未解決を生む）
取り込み時に同じ生産者が 2 回登録された。**共有キュヴェ名**または**相互補完的ラインナップ**が指標。

### CAT-3 `brand_axis` — 同一家族の複数ブランドをどう持つか
**該当**: P-6 P-7 ＋（登録外だが同型）Esprit Leflaive・Domaines Leflaive・Olivier Leflaive・Louis Latour の
ドメーヌ/ネゴシアン ／ **件数** 2＋4 ／ **頻度** 中（確認できただけで 6 系統）／ **影響** 中（現場の誤説明）
Domaine / Maison / Sélections / Esprit / 共同醸造ラベル。**統合すべきでない**が、
**producer 軸で持つのか属性で持つのかが未定**。CAT-1 と紛らわしいが**逆方向**（こちらは分けるべきものを分けている）。

### CAT-4 `naming_convention` — キュヴェ名が identity として機能していない
**該当**: C-1 C-3 C-4 C-5 ／ **件数** 4 ／ **頻度** **最大（38＋69＋αで 110 超のレコード）**／
**影響** **最大（OBP の unresolved の主要因）**
- 語順・アクセントの揺れ（C-1）
- 同じ畑の 2 規約併存（C-3、Packet B に同型 7 件）
- **識別語ゼロの名前（C-4・38 件）**
- 名前が producer 名の複製（C-5・69 件）
**単一の規約が無いことの症状群。** 個別リネームでは解けない。

### CAT-5 `layer_boundary` — 属性がどの層に属するか未定
**該当**: V-1 V-2 V-3 V-4 ／ **件数** 4 ／ **頻度** 5 組・19 レコード／ **影響** 大（OBP 11 本が未解決）
édition（Krug）・Plénitude（Dom Pérignon）・lot（Prévost）・容量（Roederer）が
**vintage 層の識別子になっているが、メニューはキュヴェ名として印字する。**
`(cuvée, vintage_year)` が一意でない。`base_year` / `release_label` / `lot` / `bottle_format` の
**どれが identity でどれが属性か**が決まっていない。

### 横断カテゴリ（データではなく規約の問題）
| | 該当 | 性質 |
|---|---|---|
| **CAT-6 `record_hygiene`** | C-2 S-4 | 非ワインレコードの混入と、分離基準の未文書化 |
| **CAT-7 `decision_schema`** | S-2 | 裁定の記録形式が 3 種・category 欠落・機械可読でない。**CAT-1 の根本原因** |
| **CAT-8 `key_design`** | S-3 | legacy_id が entity type をまたいで非一意 |
| **CAT-9 `encoding`** | S-1 | 符号化破損。**既に解決済みで、唯一 category 語彙が確立している** |

### カテゴリ別の重み

| カテゴリ | 件数 | 影響レコード数 | OBP 未解決への寄与 |
|---|---|---|---|
| **CAT-4 naming_convention** | 4 | **110+** | **最大** |
| **CAT-5 layer_boundary** | 4 | 19 | 11 本 |
| CAT-2 entity_split | 4 | 8 | 3 本 |
| CAT-3 brand_axis | 2(+4) | 12+ | 0（誤説明リスク） |
| CAT-1 identity_collision | 1 | 2 | 1 本（誤割当） |
| CAT-6〜9 横断 | 5 | 953 | 間接 |

---

## この登録票の扱い

- **research 側はここで停止。** 20 件で停止条件に到達した。
- **canonical への書き込み・削除・統合は一切していない。ADR も書いていない。**
- **解決策は設計していない。** §D は分類のみ。
- 次の判断は Akio と CTO のもの。
