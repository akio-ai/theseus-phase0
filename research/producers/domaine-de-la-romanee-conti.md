# Producer

> **Research Layer / status: `research_in_progress` / published: false / canonical 未昇格**
> canonical `producer:domaine-de-la-romanee-conti` は一切変更していない。本書は昇格前の研究記録。
>
> **レイヤー記号（混ぜない）**
> `✅` **公式サイト romanee-conti.fr で確認**（一次資料）
> `📄` 非公式資料のみ（**本書では 1 件も使用していない**）／ `⚠️` 食い違い・注意。両方を残す
> `🔍` THÉSEUS DB / OBP intake から機械的に導出
> `❓` 未解決 ／ `🖋` Akio's Insight。**Akio 専用。他者は書かない・書き換えない**
>
> 更新: 2026-08-04 ／ 一次資料: `https://www.romanee-conti.fr/`
>
> 🔴🔴 **最重要の取得上の発見 — 英語版サイトは「空」である。**
> `/en/*` の各ページは HTML の `<p>` が**すべて空タグ**で配信される（テキストが入っていない）。
> ブラウザで開いても本文は表示されない。**本文が入っているのは `/fr/*` だけ。**
> 前回の実行が英語版で止まっていたのはこのため。**以後の再調査も必ず `/fr/` を読むこと。**
>
> **参照した公式ページ（すべて `/fr/`・全 24 ページ）**
> `/`（Olney 引用）`/fr/familles` `/fr/philosophie-du-domaine` `/fr/un-prince-de-sang`
> `/fr/1500-histoire`（年表 47 件・全件取得）`/fr/9-grand-crus`
> `/fr/9-grand-crus/{1..9}/{corton, echezeaux, montrachet, grands-echezeaux, la-tache, richebourg, romanee-conti, romanee-st-vivant, corton-charlemagne}`（**9 クリュ個別ページ = 面積・収穫本数の一次データ**）
> `/fr/9-grands-crus/bouteilles-recoltees` `/fr/notes-de-degustation` `/fr/mentions` `/fr/avertissement` `/fr/galerie`
> **`/fr/millesimes/{2009…2022}` = 収穫報告（Rapport de vendanges）14 年分** ← **Farming / Winemaking の実質的な一次資料はここにしか無い**
>
> ⚠️ **キュヴェ別テクニカルシート PDF は存在しない**（Louis Latour で使えた `/pdf/en/*.pdf` 方式は無い）。
> **その代わりに、収穫報告 14 年分が事実上のテクニカル資料として機能する。**
> ⚠️ **公式サイトの内容は 2022 年 10 月で止まっている**（最新の収穫報告 = 2022/10/4、収穫本数データ = 2019 年まで、
> テイスティングノート = 2013 VT まで）。**2023 年以降の事実は公式サイトからは一切取れない。**
> 取得済み HTML / テキストは `research/producers/_sources/domaine-de-la-romanee-conti/` に保存。

---

## 🔴 統合禁止境界（intake の保護境界。canonical 昇格時に必ず参照）

| これ | ≠ | あれ |
|---|---|---|
| **Domaine de la Romanée-Conti**（本書） | ≠ | **Domaine Leroy / Maison Leroy** — Leroy 家は 1942 年以降 DRC の**株主の半分**であり、Lalou Bize-Leroy は 1974–1991 年に共同経営者だった。**しかし別法人・別ドメーヌ。**公式 DRC サイトは Domaine Leroy に一切言及しない。REGISTER **P-1** は Leroy 側の課題であり、DRC の課題ではない |
| **DRC の Corton** | ≠ | **Domaine Prince Florent de Mérode の Corton** — DRC の Corton は**メロード家の畑を 2008 年から fermage（賃借）**して造っている ✅。畑の出自は同じでもワインは別生産者 |
| **Romanée-Conti**（クリマ／DRC のワイン） | ≠ | **Romanée-Saint-Vivant / La Romanée / Romanée** — いずれも別 AOC。REGISTER §C の「別アペラシオン」誤検出クラス |
| **Corton** | ≠ | **Corton-Charlemagne** — 別 AOC・別色。REGISTER §C に明記済みの誤検出クラス。**統合するな** |
| **Échézeaux** | ≠ | **Grands Échézeaux** — 同上 |

---

## Identity

| | |
|---|---|
| **Canonical Name** | Domaine de la Romanée-Conti |
| **法人名（Raison sociale）** | **Société Civile du Domaine de la Romanée Conti** ✅（`/fr/mentions`） |
| **登記** | **RCS Dijon D 778 269 407** ✅ |
| **所在** | **21700 Vosne-Romanée, France** ✅ |
| **連絡先** | `contact@romanee-conti.fr` ✅（`/fr/galerie`） |
| **Aliases** | ❓ canonical `aliases` は**空**。実務上の略称 **DRC** は公式サイトに単独では現れない（ページ内見出しは "Romanée-Conti"）。canonical に `DRC` を alias として入れるかは未決 |
| **業態** | **民事会社（société civile）形態の家族ドメーヌ。2 家族が半分ずつ保有** ✅。ネゴシアン部門なし |
| **設立** | **1942 年 7 月 31 日、société civile du Domaine de la Romanée-Conti を設立** ✅ |
| canonical id | `producer:domaine-de-la-romanee-conti` |
| canonical entity confidence | 0.2（`legacy_app`, legacy_ids 12）— エンティティ同定の確度であり、本書の充実度とは別軸 |

---

## Overview

✅ ヴォーヌ・ロマネに本拠を置く、**9 つのグラン・クリュだけを造るドメーヌ**。公式サイトの構成そのものが
「Des Familles（家族）」「9 Grands Crus」「La philosophie du Domaine」の 3 本柱で、**ワインの商品説明も、
価格も、販売も、ヴィンテージ評価も一切載せていない。**

✅ **1869 年以来、実質的にひとつの家系の手にある。** 同年、79 歳の **Jacques-Marie Duvault Blochet**（1789–1874）が
ロマネ・コンティを買い戻した。以後この畑は分割されつつも家族内に留まり、**1942 年に民事会社化**、
現在は **Villaine 家（Gaudin de Villaine）と Leroy 家（Roch / Fenal）が半分ずつ**保有する。

✅ **経営は「2 人の associé-gérant（共同経営者）＋ 各家族 1 名ずつの監査役会」という形で 80 年以上変わっていない。**
公式サイトが確認できる最新の体制（2021 年 12 月時点）は **Bertrand de Villaine ＋ Perrine Fenal**、
監査役会は **Henri de Villaine ＋ Isabelle Roch**。

✅ **ビオディナミ。** 収穫報告に「notre option biodynamique（我々のビオディナミという選択）」
「notre choix de la biodynamie où les seuls produits de défense autorisés sont **le cuivre en quantité mesurée et le soufre**
（防除に許されるのは計量された銅と硫黄だけ）」と繰り返し書かれている。

⚠️ **公式サイトは「ワインの説明」をほとんどしない。** 各クリュのページにあるのは
**面積（小数点 4 桁）／年ごとの収穫本数／第三者の詩的な引用 1 つ／3 行程度の人格化された描写**だけである。
醸造の具体は**すべて収穫報告（Rapport de vendanges）の地の文の中にしか無い。**
**「語らないこと」自体がこの造り手の姿勢**であり、Staff Notes ではこれを説明できるようにしてある。

---

## History

### Foundation — 修道院から王族へ ✅（`/fr/1500-histoire` 全 47 件より）

| 年 | 出来事 |
|---|---|
| **900** | Manassès（sire de Vergy）が **Saint-Vivant 修道院を創建** |
| **1131** | 11/13、ブルゴーニュ公 Hugues II が Flagey と Vosne の森林・未耕地（**将来のロマネ・コンティの畑を含む**）を Saint-Vivant 修道院に譲渡 |
| **1241** | Saint-Vivant の修道院長たちが畑を取得（将来のロマネ・コンティを含む）。Saint-Vivant が **Cluny 修道院に帰属** |
| **1512** | 「**Cloux de Saint-Vivant**」の最初の申告と記述 |
| **1584** | 2/19、修道院長が **Cros des Cloux（＝将来のロマネ・コンティ）を Claude Cousin に永代賃貸借で売却** |
| 1603 / 1621 / 1631 | Germain Danon が相続 ／ Jacques Venot が購入 ／ 8/28 Venot が娘婿 **Philippe de Croonembourg** に譲渡 |
| **1651** | **Cros des Cloux に対する「Romanée」の最初の文書上の言及** |
| **1760** | **7/18、ロマネの売買契約。**Jean-François Joly de Fleury が「彼または彼の指名する友人のために」買い、所有権は「**セレニッシム殿下 Louis François de Bourbon、コンティ公、王族**」に移る |
| **1763** | コンティ公が隣接 2 区画（lieu-dit «au meix Caillot»、**今日の La Goillotte**）を購入。**ロマネ専用の醸造・保存用のカーヴと、耕作人・管理人の住居を建てるため** |
| **1776** | Louis François de Bourbon 死去。息子 **Louis François-Joseph**（この名の最後の人）が継承 |
| **1789** | **ロマネ・コンティとロマネ・サン・ヴィヴァンが没収される**（教会財産の世俗化） |
| **1793** | 4 月、コンティ公が逮捕されマルセイユの Saint-Jean 要塞に投獄 |
| **1794** | **2/13、最初の鑑定。ここで「Romanée-Conty」の名が現れる。** 7/6 二度目の鑑定。**12/24、最高額入札者 Nicolas Defer de la Nouerre に売却** |
| **1797** | 9/5、共和暦 5 年フリュクティドール 19 日法により**ブルボン家全員が追放**。最後のコンティ公はバルセロナへ亡命（1814 年死去） |

### 19 世紀 — Ouvrard から Duvault Blochet へ ✅

| 年 | 出来事 |
|---|---|
| **1819** | 9/22、**Julien-Jules Ouvrard がロマネ・コンティを購入** |
| 1828 / 1830 | Ouvrard が Gilly 城に移る ／ **ロマネ・コンティが Clos de Vougeot で醸造される** |
| 1852 / 1861 | Ouvrard が Côte d'Or 選出の代議士に ／ 6/22 Ouvrard 死去、Rochechouart 家の甥姪が相続 |
| **1869** | 8/7、Rochechouart 一族から Paul Guillemot へ売却。**11/25、Jacques-Marie Duvault Blochet がロマネ・コンティを買い戻す。**彼はすでに **Gaudichots・Richebourg・Grands-Échézeaux・Échézeaux の所有者**でもあった |
| **1874** | 2/23、Duvault Blochet 死去（1789–1874） |
| **1876** | 財産が 2 人の娘 **Claudine-Constance Massin と Henriette Dupuis** に分割される |

### 20 世紀以降 ✅

| 年 | 出来事 |
|---|---|
| **1911** | **Edmond Gaudin de Villaine** が **Louis Clin を régisseur に採用** |
| **1912** | Edmond Gaudin de Villaine と **Jacques Chambon** が Guyot 家いとこ達の持分を購入 |
| **1933** | **La Tâche（Joly de Bévy）を取得** |
| **1940** | Louis Clin が **André Noblet を採用** |
| **1942** | **7/31、société civile du Domaine de la Romanée-Conti を設立。Henri Leroy が Jacques Chambon の持分を購入** |
| **1950** | 11/24、Edmond Gaudin de Villaine 死去。**Henri de Villaine が Henri Leroy と共同経営者に** |
| **1963** | **Montrachet の畑を取得** |
| **1966** | **Romanée-Saint-Vivant Marey-Monge を、最後の当主 Marey-Monge 嬢から fermage（賃借）で受ける** |
| **1974** | 民事会社の新定款。**Lalou Bize-Leroy と Aubert de Villaine が共同経営者**、Henri de Villaine と Henri Leroy が監査役会 |
| **1979** | **La Goillotte の家と畑（コンティ公の旧醸造所）を取得** |
| **1980** | Henri Leroy 死去。長女 Pauline が監査役会を引き継ぐ |
| **1984** | **André Noblet 引退。息子 Bernard Noblet が chef de cave、Gérard Marlot が chef de culture に** |
| 1986 | 5/30、André Noblet 死去 |
| **1988** | **9 月、Romanée-Saint-Vivant Marey-Monge をドメーヌの出資者が買い取る**（賃借 → 所有） |
| **1992** | 1 月、**Charles Roch が Lalou Bize-Leroy に代わって共同経営者に。3/10、Charles Roch 事故死。弟 Henry-Frédéric Roch が引き継ぐ** |
| 1993 / 1998 | Henri de Villaine が同名の甥に交代 ／ Henri de Villaine（1950–74 の経営者）死去 |
| **2005** | **Perrine Fenal**（Lalou Bize-Leroy の娘）が Pauline Roch に代わり監査役会へ |
| **2008** | **Bertrand de Villaine がドメーヌに参加。11/11、Corton グラン・クリュの畑を fermage で受ける** |
| **2010** | 12 月、**管理部門が Saint-Vivant 修道士の旧 vendangeoir（収穫小屋）に移転** |
| **2015** | 7/4、**ブルゴーニュのクリマがユネスコ世界遺産に登録。推進協会の会長は Aubert de Villaine** |
| **2018** | **11/11、Corton-Charlemagne グラン・クリュの畑を métayage（分益小作）で受ける。11/17、Henry-Frédéric Roch 死去** |
| **2019** | 1 月、**Perrine Fenal が共同経営者に、Isabelle Roch が監査役会に**（1/23 総会） |
| **2021** | **12/3 総会で Bertrand de Villaine が叔父 Aubert de Villaine の後任として共同経営者に**（`/fr/familles`。年表には未反映） |

### 2 つの家族 ✅（`/fr/familles`）

| 系統 | 内容 |
|---|---|
| **Villaine 系** | Duvault Blochet → Gabrielle Chambon（1857–1903）→ **Marie-Dominique Madeleine Gaudin de Villaine 旧姓 Chambon（1883–1915）**。以後 **Edmond（1881–1950）→ Henri（1909–1998）→ Aubert** と続き、**société civile の半分を今日まで保有**。現在は Henri（妻 Hélène Zinoviev）と弟 Jean（1910–1975、妻 Simone-Marie de France）の子・孫・曾孫たちで構成 |
| **Leroy 系** | **Jacques Chambon（1889–1969）が 1942 年に持分を Henri Leroy（1894–1980、Auxey-Duresses の propriétaire récoltant 兼ネゴシアン）へ売却。**Henri Leroy → 娘 **Pauline Roch（1929–2009）**と **Marcelle（Lalou）Bize**。Pauline の子は Charles（1957–1992）／ Isabelle ／ Henry-Frédéric（1962–2018）、Lalou の娘は **Perrine** |

✅ **Perrine Fenal は 1992–2005 年、自社 Perrine Fenal S.A. を通じてスイス・ロマンド地域における
ドメーヌのワインの輸入・販売元だった。**
✅ **Bertrand de Villaine は 2008 年からドメーヌで働いている** — 最初は畑、次にカーヴ、その後
2 人の共同経営者の傍らで経営全般に関与。

⚠️🔴 **「現当主は Aubert de Villaine」は 2021 年 12 月時点で既に誤り。**
公式は「Bertrand de Villaine が**叔父 Aubert の後任として（prendre la suite de son oncle Aubert）**」と明記する。
Aubert は 2015 年のユネスコ登録推進協会会長としては現れるが、**共同経営者としては後任が立っている。**
⚠️ ただし**公式サイトは 2022 年 10 月で更新が止まっている**ため、**2026 年現在の体制は公式では確認できない。**
→ **「現在性未確認」。** Open Questions 1

---

## Location

| | |
|---|---|
| **Country** | France ✅ |
| **Region** | Bourgogne / Côte de Nuits（＋ Côte de Beaune に Corton・Corton-Charlemagne・Montrachet）✅ |
| **Village** | **Vosne-Romanée（21700）** ✅ |
| **管理部門** | **Saint-Vivant 修道士の旧 vendangeoir**（2010 年 12 月に移転）✅ |
| **歴史的建物** | **La Goillotte** — コンティ公が 1763 年に「ロマネ専用の醸造・保存用カーヴと、耕作人・管理人の住居」を建てるために買った区画。**ドメーヌが 1979 年に取得** ✅ |

### Key Vineyards — 9 グラン・クリュ（面積は公式の 4 桁表記のまま）✅

| クリュ | 村 | 色 | **面積（ha）** | 取得・保有形態 |
|---|---|---|---|---|
| **Romanée-Conti** | Vosne-Romanée | 赤 | **1.8140** | 1869 年に Duvault Blochet が買い戻し。以後家族内 |
| **La Tâche** | Vosne-Romanée | 赤 | **6.0620** | **1933 年取得**（La Tâche Joly de Bévy） |
| **Richebourg** | Vosne-Romanée | 赤 | **3.5110** | 1869 年時点で Duvault Blochet が既に所有 |
| **Romanée-Saint-Vivant** | Vosne-Romanée | 赤 | **5.2858** | **1966 年 fermage → 1988 年 9 月に買取** |
| **Grands Échézeaux** | Flagey-Échézeaux | 赤 | **3.5263** | 1869 年時点で既に所有 |
| **Échézeaux** | Flagey-Échézeaux | 赤 | **4.6737** | 1869 年時点で既に所有 |
| **Corton** | Aloxe-Corton | 赤 | **2.2746** | 🔴 **2008/11/11 から fermage（賃借）。Domaine Prince Florent de Mérode の畑**。climat は **Clos du Roi / Bressandes / Renardes**。**初収穫 2009** |
| **Corton-Charlemagne** | Aloxe-Corton | 白 | **2.9132** | 🔴 **2018/11/11 から métayage（分益小作）。初収穫 2019** |
| **Montrachet** | Puligny-Montrachet | 白 | **0.6759** | **1963 年に畑を取得** |
| **9 クリュ合計** | | | **30.7365**（🔍 加算） | |

❓ **ドメーヌの総面積は公式に一つの数字が無い。** 上の 30.7365 ha は**グラン・クリュ 9 つの合計にすぎず、
ドメーヌの全所有面積ではない**（下記のとおり 1er cru と Bâtard-Montrachet の畑が別に存在する）。

🔴 **公式サイトの「9 Grands Crus」に載っていないが、公式文中に存在が確認できる畑が 2 つある。**

| 畑 | 根拠 |
|---|---|
| **Vosne-Romanée 1er Cru "Les Petits-Monts"** | ✅ **2022 年収穫報告**に収穫日程として明記 —「**Le Vosne-Romanée Petits-Monts : le 10 septembre**」。canonical にも `Les Petits Monts`（Vosne-Romanée Premier Cru）として登録済み 🔍 |
| **Bâtard-Montrachet** | ✅ **2016 年収穫報告** —「4/27 の朝、**Montrachet、Bâtard-Montrachet、Échézeaux、Grands-Échézeaux の畑が霜にやられているのを見つけた**」。**専用ページも面積表記も無い** |

→ **どちらも「9 Grands Crus」の枠外**であり、公式は面積・生産量・存在の説明を一切していない。
**現場で「DRC はグラン・クリュしか造らない」と言うと、この 2 つで足元をすくわれる。** Open Questions 3

---

## Farming

✅ **ビオディナミ。公式に明記されている。** ただし**専用ページは無く、記述はすべて収穫報告の地の文にある。**

> ✅ 「…au Domaine, Nicolas Jacob, notre chef de culture et son équipe, ont dû, à partir de fin mai,
> **dans le strict respect de notre option biodynamique**, s'ingénier à protéger les vignes du mildiou et de l'oïdium,
> effectuer les labours en temps voulu…」（2013 年収穫報告）
> ✅ 「…tout en restant dans le cadre de **notre choix de la biodynamie où les seuls produits de défense autorisés
> sont le cuivre en quantité mesurée et le soufre**」（2012 年収穫報告）
> ✅ 「Celles-ci résistent cependant avec d'autant plus d'aisance que **des années de biodynamie** leur ont apporté
> **une précieuse autonomie dans leur défense contre les excès de la Nature**」（2011 年収穫報告）
> ✅ 「Cette aisance de la vigne à traverser des conditions extraordinairement difficiles fut bien sûr confortée
> par **la culture en biodynamie**, par **l'âge moyen élevé de vignes qui sont donc profondément enracinées**,
> et par **les faibles rendements**…」（2019 年収穫報告）

| 実践 | 内容 | 出典 |
|---|---|---|
| **防除** | **許可されるのは「計量された銅」と「硫黄」のみ** | ✅ 2012 |
| **耕耘（labours）** | **除草剤を使わず耕す。**雨で入れない年は草が伸び放題になり、晴れ間を突いて年 3 回耕すこともある | ✅ 2012 / 2013 / 2016 |
| **格言** | 乾いた年の耕耘は控えめに —「**un bon binage vaut deux arrosages**（よい中耕は二度の灌水に値する）」 | ✅ 2020 |
| **畑作業** | taille（剪定）・ébourgeonnage（芽かき）・relevage・accolage・rognage・épamprage を手作業で順に | ✅ 2020 / 2022 |
| **樹齢・収量** | **高い平均樹齢 → 深根 → 低収量**が乾燥・熱波への耐性の理由と公式が説明 | ✅ 2019 |
| **植栽材料** | **旧ロマネ・コンティ由来の「非常に繊細な（très fin）ピノ・ノワール」の選抜と増殖**。これを「比類のない遺伝的資産」と位置づける | ✅ `/philosophie-du-domaine` |
| **台木** | 2022 年報告で「**極端な気候に適した台木の選択が今後の要**」と明言。**適応能力は「タイプの繊細な（de types fins）ピノ・ノワールとシャルドネを、よい台木に接いだ場合」に限る**とする | ✅ 2022 |
| **収穫** | **手摘み。約 80 人の収穫チーム**。畑での選果（焼けた粒・botrytis・大粒で未熟な房を落とす）＋ **必要な年は二度摘み（deuxième passage）** | ✅ 2011 / 2019 |

❓ **認証機関（Demeter / Biodyvin）も、ビオディナミ転換の開始年も、公式サイトに一切記載が無い。**
**有機認証（AB）についても記載が無い。** → Open Questions 2

⚠️ **Louis Latour（ISO 14001 の減農薬農法・認証オーガミックではない）／ Domaine Leflaive（ビオディナミ 25 年超・馬耕）
との三者比較で、DRC は「ビオディナミだが認証機関を公表しない」という第三の型に入る。**
⚠️ **DRC の公式サイトには「馬で耕す」という記述は無い。**Leflaive と混ぜて語らないこと。

---

## Winemaking

### 人（現場の指揮系統）✅ — **公式に名前が出る**

| 役割 | 人物 | 期間 |
|---|---|---|
| régisseur | **Louis Clin** | 1911 年採用 |
| chef de cave | **André Noblet** | 1940 年採用 → 1984 年引退（1986 年死去） |
| chef de cave | **Bernard Noblet**（André の息子） | ⚠️ **1984 か 1986 か公式内で不一致**（下記）。**–2017**。2017 年の Paulée が「醸造責任者としての最後の収穫」 |
| chef de cave | **Alexandre Bernier** | **2017 年に Bernard Noblet の後任として並走 → 2018 年から単独で醸造を指揮** |
| chef de culture | **Gérard Marlot** | 1984 年〜 |
| chef de culture | **Nicolas Jacob** | 少なくとも 2011–2022 年の全報告に登場 |
| chefs de culture（複数） | **Nicolas Jacob ＋ Didier Dubois** | **2022 年報告で 2 名体制**（"nos chefs de culture"） |

⚠️ **Bernard Noblet の就任年が公式内で食い違う。両方を残す。**
- `/fr/1500-histoire` **1984** の項:「**Retraite d'André Noblet ; son fils Bernard Noblet chef de cave** ; Gérard Marlot chef de culture」
- **2017 年収穫報告**:「Bernard Noblet, **chef de cave du Domaine depuis 1986** à la suite de son père André Noblet」
→ **1984（父の引退）と 1986（父の死去年でもある）のどちらを就任年とするか、公式が決めていない。**
**現場では「1980 年代半ばから 2017 年まで」と言うのが安全。** → Open Questions 9

⚠️ **Bernard Noblet の引退年は「2017 年収穫が最後」と読むのが正確。**「2018 年に引退」とは言わない。
❓ 2026 年現在の chef de cave / chef de culture は公式では確認できない（サイトが 2022 年で止まっているため）。

### 収穫からタンクまで ✅

- **選果は 2 段構え** — ①畑で収穫人が落とす（焼けた粒・霜や雹の被害粒・botrytis・大粒で未熟な房） ②**キュヴリーの選果台（table de tri）で 14 人**が仕上げる（2020 年報告）。
- ✅ 難しい年の選果を公式は **「travail de haute couture（オートクチュールの仕事）」**と呼ぶ。**房の柄（queues des grappes）まで丁寧に切り落として、タンクに入る梗の量を減らす**（2017 年報告）。
- ✅ **除梗（éraflage）は最小限、年によってはゼロ。**
  - 2015: 「La maturité phénolique parfaitement achevée du raisin nous a amenés à choisir de faire les vinifications
    **en vendange entière, c'est-à-dire sans aucun éraflage**」＝ **全房・除梗ゼロ**
  - 2016: 「Ils sont soumis à **un très léger éraflage**」＝ ごく軽い除梗
  - 2017: 「L'éraflage… a été **minime, parfois nul pour certaines vignes comme la Romanée-Conti, vinifiée en vendange entière**」
  - 2020: 「La vinification se fera avec **90 à 100% de grappes entières**, c'est-à-dire sans éraflage」
  → 🔴 **全房比率は固定値ではなく、年ごと・区画ごとに 0〜100% の間で判断される。**

### 発酵 ✅

| 項目 | 内容 |
|---|---|
| **プレ発酵浸漬** | **数日間、自然に成立する**（冷たい葡萄・冷たい搬入温度 15℃前後）。「macération pré-fermentaire de quelques jours **obtenue naturellement**」（2016）。2013 は「**5〜6 日**」 |
| **醗酵の立ち上がり** | 「**lent et progressif**（ゆっくり漸進的）」。人為的な加温・急発酵をしない |
| **醸し期間** | **キュヴェにより 18〜21 日**（2020）。2010 年は最初のタンクで 17 日 |
| **作業** | **remontage（ポンプオーバー）と pigeage（櫂入れ）のみ。**「**sans autres interventions que les remontages et les pigeages habituels**」。**pigeage は「très ralenti（極端に遅いリズム）」で、抽出が自然な水準を超えないようにする**（2020） |
| **足での pigeage** | ✅ **人が素足でタンクに入る。**「quand, pour les « pigeages », on entre… **avec les jambes nues dans le vin nouveau**, qui fermente à **34/35°C**」（2017） |
| **タンク数** | 2017 年は **24 キュヴ**（前年のほぼ倍） |

### 熟成 ✅

- ✅ **樽熟成 18 ヶ月。**「les vins… vont vivre pendant **les 18 mois d'élevage**, si importants, qui les séparent de la mise en bouteilles」（2016 年報告）。**これが公式に確認できる唯一の熟成期間の数字。**
- ✅ 赤は「**l'élevage en fûts de chêne**（オーク樽での熟成）」と書かれる。
- ✅ **白（Corton-Charlemagne 2019、初ヴィンテージ）**: 「Après pressurage, le moût a été écoulé
  **pour sa plus grande partie en fûts neufs de haute qualité** et pour une petite partie（**l'équivalent de 4 pièces**）
  **en un joli foudre de chêne fabriqué pour l'occasion**」＝ **大部分が高品質の新樽、一部（4 pièce 相当）はこのために造らせたフードル。**
- ✅ 白は**樽とフードルで発酵**（2022 年報告「Les vins blancs, eux, **fermentent encore en fûts et foudres**」）、
  **マロラクティック発酵も樽で**（2019 年報告、Corton-Charlemagne）。

🔴⚠️ **赤の新樽比率は公式に一度も書かれていない。**
公式が「新樽（fûts neufs）」と明記しているのは **2019 年の Corton-Charlemagne 1 件だけ**である。
**「DRC は赤も 100% 新樽」と現場で言ってはいけない。**（→ Staff Notes ⚠️ リスト）
❓ 樽の産地・樽元・トースト・バトナージュ・天然酵母・SO2・清澄／濾過の有無 — **公式に記述ゼロ。** Open Questions 4

### 収量と収穫日（公式が数値を出している年）✅ 🔍

| 年 | 収量（hl/ha） | 備考 |
|---|---|---|
| **2009** | 平均 **30** | 2012 年報告内の比較として |
| **2012** | 赤 平均 **約 20**（「正常値と考える **25** の 25% 減」） | **公式が「normale = 25hl/ha」と明言した唯一の箇所** |
| **2015** | Montrachet 30 ／ Grands-Éch 30 ／ RSV 26 ／ Éch 25 ／ La Tâche 25 ／ Richebourg 24 ／ **Romanée-Conti 22** ／ Corton 22 | 全クリュの数値が出ている年 |
| **2016** | La Tâche 31 ／ RSV 27 ／ **Romanée-Conti 24** ／ Corton 22 ／ **Grands-Éch 7 ／ Éch 6**（4/27 の霜） | |
| **2018** | **Romanée-Conti 18** ／ Grands-Éch 32 ／ Corton 35 | 「vieilles vignes と生産の抑制により赤の収量は非常に穏当」 |
| **2019** | Grands-Éch 28 ／ RSV 27 ／ **Corton-Charlemagne 26** ／ Éch 23 ／ La Tâche 23+ ／ Richebourg 21+ | |
| **2021** | **Vosne-Romanée 全体 約 15**（RC と Grands-Éch は 22–23）／ **Montrachet 7**（通常 10 pièce → 4 pièce）／ **Corton rouge 4.5** | 🔴 **霜害の年。壊滅的** |

### 収穫本数（公式データ・`/fr/9-grand-crus/*` 各クリュページ）✅ 🔍

| クリュ | 2015 | 2016 | 2017 | 2018 | **2019** |
|---|---|---|---|---|---|
| **Romanée-Conti** | 4,831 | 5,281 | 7,521 | 4,029 | **4,906** |
| **La Tâche** | 16,644 | 21,770 | 24,981 | 14,275 | **11,929** |
| **Richebourg** | 10,185 | 10,418 | 15,482 | 8,227 | **8,135** |
| **Romanée-St-Vivant** | 16,777 | 15,657 | 20,318 | 12,709 | **16,214** |
| **Grands Échézeaux** | 12,672 | **（記載なし）** | 15,136 | 12,176 | **10,606** |
| **Échézeaux** | 13,758 | **（記載なし）** | 15,467 | 14,047 | **10,453** |
| **Corton** | 4,583 | 5,047 | 7,818 | 7,947 | **4,403** |
| **Montrachet** | 2,579 | **（記載なし）** | 2,686 | 4,116 | **2,204** |
| **Corton-Charlemagne** | — | — | — | — | **9,110**（初ヴィンテージ） |

⚠️ **2016 年の Échézeaux / Grands Échézeaux / Montrachet は本数欄が空白**だが、
**2016 年収穫報告には「Échézeaux 6hl/ha、Grands-Échézeaux 7hl/ha を収穫した」と書かれている。**
**公式内での不整合。両方残す。** 収穫はしたが本数表に未記入なのか、格下げしたのかは不明 → Open Questions 5
⚠️ **本数データは 2019 年で止まっている。** OBP の 2020–2023 は公式データの対象外。
🔍 **Romanée-Conti は最も生産本数が少ない**（1953–2019 の全 65 年で年 2,915〜9,627 本、**1968 年は 0 本**）。

---

## Style

⚠️ **この造り手は「ハウススタイル」を語らない。** 公式サイトにテイスティングノートに準ずるものは
①各クリュページの 3 行の描写、②`/fr/notes-de-degustation`（**2013 VT までで停止**）しか無い。
**造りから構造的に言えることと、公式が採用した表現とを分けて記す。**

### 造りから構造的に言えること ✅

1. **抽出を「自然な水準」で止める設計。** pigeage を意図的に遅いリズムで行い、「抽出が自然な水準を超えないように」する。remontage と pigeage 以外の介入をしない。
2. **全房が骨格に効く。** 除梗は最小、年により 0%。「phenolic maturity（皮・種・**梗**の成熟）が糖度と揃うまで待つ」ことを収穫判断の基準にしている（＝梗を使う前提の熟度判断）。
3. **プレ発酵浸漬を数日、自然に。** 冷たい葡萄・15℃前後の搬入・ゆっくりした発酵開始。
4. **樽 18 ヶ月。** 熟成期間はクリュ横断で同じと読める（クリュ別の記述は無い）。
5. **低収量は「意図」ではなく「高樹齢の結果」として説明される。** 公式は「vieilles vignes と生産の抑制」「深く根を張った古木」「低収量」を耐性の理由として挙げる。

### 公式が採用しているクリュ別の性格づけ ✅（第三者の引用を含む。**ドメーヌが自ら選んで掲げている文言**）

| クリュ | 公式ページの表現（要点） | 掲げられた引用 |
|---|---|---|
| **Romanée-Conti** | 「**Vin de Prince**。ヴェルヴェット、誘惑、神秘。**最もプルースト的な偉大なワイン** — 1956 年のわずかに萎れた薔薇の花弁の秘めた香りの下に、失われた時を取り戻す感覚が押し寄せる」 | **Richard Olney** ―「神々がこの一片の土地に、時を超えた完全性の痕跡を記念に遺したかのようだ」 |
| **La Tâche** | 「**エレガンスと力強さ**。しばしば硬いタンニンの下で情熱が燃えており、それを冷徹な宮廷的エレガンスが制御している」 | Philippe de Champaigne による**リシュリューの肖像**に喩える（剣の柄に置かれた神経質な手が、白貂と天鵞絨の豪奢な包みに沈んでいる） |
| **Richebourg** | 「隣人ロマネ・コンティの**絹のような性格**と、ラ・ターシュの**堅牢さ**を併せ持つ。**王の銃士**」 | **Camille Rodier** ―「ブルゴーニュ最も豪奢なワインのひとつ」 |
| **Romanée-St-Vivant** | 「**誘惑者**。優美さの背後に、完璧に均衡しているがゆえに一見して気づかない力がある」 | **J-F Bazin** ―「女性性と繊細さの奇跡。抗いがたい魅了の意志」 |
| **Grands Échézeaux** | 「**Échézeaux である前に Grands である。**田舎の貴族にして夢想家。苔・落葉・腐葉土・獣の匂いに満ちた森を馬の歩みで行く。**モーツァルトの四重奏のように洗練され、音楽的で、簡潔で、純粋**」 | J-F Bazin ―「Échézeaux である前に偉大なワイン。齢とともに静謐となる、碩学のためのワイン」 |
| **Échézeaux** | 「**ドメーヌの全クリュ中で最も早熟で、最も複雑さが少ない。**鋼の骨格を優美な柔らかさが包む。**Grands Échézeaux の弟**」 | J-F Bazin ―「回り道も複雑さもなく素直に近づける」 |
| **Corton** | — | **Camille Rodier** ―「アロース・コルトンのワインは Côte d'Or の筆頭。堅固で率直で、非常に長命」 |
| **Corton-Charlemagne** | — | **Jean-François Bazin** ―「黄金の樹液、少しの活力で味付けられた甘やかさ、長さと広がり」 |
| **Montrachet** | 「**比類なき複雑さ。**エレガンスと力強さが例外的なワインにしている」 | **Dr Lavalle** ―「Côte d'Or の、そしておそらく世界の白ワインの疑いなく第一位」 |

❓ **第三者による点数評価は公式に一切無い**（Burghound / WS / JS の類の掲載欄が存在しない）。
❓ **飲み頃・Cellaring Potential の公式表示も無い。**

---

## Important Cuvées

### OBP リスト掲載 — **19 本。全ボトルが単一生産者としては最高価格帯** 🔍

| ワイン（OBP 印字） | 掲載ヴィンテージ | 価格帯（$） | 公式で確認 | **canonical** |
|---|---|---|---|---|
| **Romanée-Conti Grand Cru** | 2022, 2020 | **21,000 / 30,600** | ✅ 1.8140 ha | **登録済**（vintage: 2020 のみ） |
| **La Tâche Grand Cru** | 2022, 2020, 2018, 2017 | 9,900 / 10,000 | ✅ 6.0620 ha | **登録済**（vintage 0 件） |
| **Richebourg Grand Cru** | 2022, 2017 | 8,200 | ✅ 3.5110 ha | **登録済**（vintage 0 件） |
| **Romanée-Saint-Vivant Grand Cru** | 2022, 2021, 2019, 2009, 1993 | 7,800 / 8,000 / 8,200 / 15,000 / 15,980 | ✅ 5.2858 ha | **登録済**（vintage: 1993, 2009, 2019, 2021。**2022 が欠**） |
| **Grands Échézeaux Grand Cru** | 2023, 2015 | 5,600 / 16,000 | ✅ 3.5263 ha | **登録済**（vintage 0 件） |
| **Échézeaux Grand Cru** | 2023, 2022 | 3,040 / 3,480 | ✅ 4.6737 ha | **登録済**（vintage 0 件） |
| **Corton Grand Cru** | 2023 | 3,380 | ✅ 2.2746 ha・**fermage 2008〜** | **登録済**（vintage 0 件） |
| 🔴 **Corton-Charlemagne Grand Cru**（白） | 2023 | **7,200** | ✅ **2.9132 ha・métayage 2018/11/11〜・初収穫 2019** | 🔴 **未登録 — OBP 唯一の未解決 1 本** |

🔍 **OBP 19 本／canonical 保有キュヴェ 9 件／未解決 1 本。**

### 🔴 未解決 1 本 — **Corton-Charlemagne は「新規キュヴェ」として素性が完全にクリーン**

- ✅ **公式サイトに専用ページが存在する**（`/fr/9-grand-crus/9/corton-charlemagne`）。
- ✅ **面積 2.9132 ha**、`/philosophie-du-domaine` の「**2,91 ha de Corton Charlemagne**」と一致。
- ✅ **2018 年 11 月 11 日に métayage（分益小作）で受領**、**初収穫 2019 年**（9,110 本、収量 26hl/ha、9/22–9/25 収穫）。
- ⚠️ **公式内に小さな食い違いがある。** `/philosophie-du-domaine` は「**La première récolte devrait être présentée en 2022**
  （初収穫は 2022 年に披露される予定）」と書き、クリュページは「**avons effectué notre première récolte en 2019**
  （2019 年に初収穫を行った）」と書く。**収穫は 2019、リリースは 2022 と読むのが自然だが、公式は明示していない。**
  **両方を残す。** → Open Questions 6
- 🔍 **Packet B（新規キュヴェ）候補として confidence は高い。** ただし**登録は architecture の判断であり、research では行わない。**

### canonical にあって OBP に無いキュヴェ 🔍

| canonical キュヴェ | subregion | 公式での裏取り |
|---|---|---|
| **Montrachet** | Montrachet | ✅ 0.6759 ha、1963 年取得。年産 2,204–4,116 本（2015–2019）。**極小量**なので OBP に無いのは妥当 |
| **Les Petits Monts** | Vosne-Romanée Premier Cru | ✅ **2022 年収穫報告に「Le Vosne-Romanée Petits-Monts : le 10 septembre」**と明記。**専用ページは無い**が実在は公式で確認できる |

### 公式に存在が確認できるが canonical にも OBP にも無いもの

- **Bâtard-Montrachet** — ✅ 2016 年収穫報告に「nos vignes de … **Bâtard-Montrachet** …」。
  **面積・生産量・ラベルの有無は公式に一切記述が無い。** → Open Questions 3

⚠️ **価格データの読み方の注意（intake 由来）** 🔍
`prices` 配列は**ヴィンテージと 1:1 対応していない**。例: La Tâche は 4 VT に対し価格 2 件、
Richebourg は 2 VT に対し 1 件しかない。**「2018 の La Tâche は $9,900」と断定できない。**
価格を口頭で言う前に必ず現物のリストを見ること。
⚠️ **Grands Échézeaux は 2023 が $5,600、2015 が $16,000 で約 2.9 倍。**
Romanée-Saint-Vivant も 2022 $7,800 に対し 1993 $15,980。**熟成在庫のプレミアムが極端に大きい。**

---

## Staff Notes

> この節は上記の ✅ と 🔍 からのみ構成している。裏の取れていない事柄は書いていない。

**一行で言うと** — 「**ヴォーヌ・ロマネの 9 つのグラン・クリュだけを造るドメーヌ。**
1869 年から実質ひとつの家系にあり、1942 年から **2 つの家族が半分ずつ**持っている。ビオディナミ。**樽で 18 ヶ月。**」

### ゲストへの説明の芯（4 点）

**1. 「9 つのグラン・クリュ」という構成そのものが説明になる。**
赤 7 つ（**Romanée-Conti 1.81ha / La Tâche 6.06 / Romanée-St-Vivant 5.29 / Échézeaux 4.67 /
Grands Échézeaux 3.53 / Richebourg 3.51 / Corton 2.27**）と白 2 つ（**Corton-Charlemagne 2.91 / Montrachet 0.68**）。
**面積を言えるのが一番強い。**公式が小数点 4 桁まで公表している。
**ロマネ・コンティは 1.8140ha しかなく、生産は年 3,000〜7,500 本程度**（2015–2019 は 4,029〜7,521 本）。

**2. 2 つの家族が半分ずつ持っている。**
**1869 年に 79 歳の Jacques-Marie Duvault Blochet がロマネ・コンティを買い戻した。**
その血筋が **Villaine 家**。もう半分は **1942 年に Henri Leroy が Jacques Chambon から買った持分**で、
これが **Leroy 家（現在は Roch / Fenal）**。
**経営は常に 2 人の共同経営者 — 各家族から 1 人ずつ。**公式サイトが確認できる最後の体制（2021 年 12 月）は
**Bertrand de Villaine と Perrine Fenal**。

**3. 醸造は「余計なことをしない」ことで組み立てられている。**
- **除梗しない年がある。**2015 年は**除梗ゼロの全房**、2020 年は **90〜100% 全房**。年ごとに変える。
- **プレ発酵浸漬は数日、自然に成立するのを待つ**（葡萄が冷たいので勝手に始まる）。
- **醸しは 18〜21 日。作業は remontage と pigeage だけ。**しかも **pigeage はわざと遅いリズム**で、
  「**抽出が自然な水準を超えないように**」する。**素足でタンクに入る**（発酵中は 34–35℃）。
- **樽で 18 ヶ月。**
- **選果台には 14 人。**難しい年の選果を彼ら自身が「**オートクチュールの仕事**」と呼ぶ。

**4. 栽培はビオディナミ。防除に使うのは銅と硫黄だけ。**
公式の言い方は「**notre choix de la biodynamie où les seuls produits de défense autorisés sont
le cuivre en quantité mesurée et le soufre**」。**除草剤は使わず耕す。**
公式は「**古木で根が深く、収量が低い**からこそ極端な気候を越えられる」と説明する。

### 小話が要るとき（すべて公式・`/fr/1500-histoire` `/fr/un-prince-de-sang`）

- **名前の由来。** **1760 年 7 月 18 日**、ロマネの畑が **Louis-François de Bourbon, prince de Conti（1717–1776）**の
  ものになった。**Clos de Bèze の 10 倍を超える値**（公式「un prix supérieur de dix fois à celui du Clos de Bèze」）で買った。
  **彼はこのワインを自分の食卓にしか出さなかった。**
  **1794 年 2 月 13 日の革命政府の鑑定書に、初めて「Romanée-Conty」という名が現れる。**
  つまり**「コンティ」の名が畑についたのは、コンティ家がその畑を失ったあと**である。所有していたのは 30 年足らず。
- **畑の名は 1651 年から。**「Romanée」という呼称の最初の文書上の記録が 1651 年。
  それ以前は「**Cros des Cloux**」「**Cloux de Saint-Vivant**」と呼ばれていた。起源は **900 年創建の Saint-Vivant 修道院**。
- **La Goillotte。** コンティ公が **1763 年**に「ロマネ専用の醸造・保存用カーヴを建てるため」に買った区画。
  **ドメーヌは 1979 年にこれを取得した。**
- **醸造長は 3 人だけ。** **André Noblet（1940 年採用）→ 息子 Bernard Noblet（1980 年代半ば–2017）→ Alexandre Bernier（2018〜）。**
  **1940 年から 2017 年までの 77 年間を、父と子の 2 人で担った。**
- **Corton は借りている畑。** **2008 年 11 月 11 日から Domaine Prince Florent de Mérode の畑を fermage で。**
  **Clos du Roi・Bressandes・Renardes** の 3 つのクリマの古木を、**「Corton」という共通の名の下でまとめて醸造**している。
  **初収穫は 2009 年。**
- **Corton-Charlemagne は 2018 年 11 月 11 日から**（métayage）。**初収穫 2019 年、9,110 本。**
  **ドメーヌにとって Montrachet 以来 55 年ぶりの新しい白。**
- **ユネスコ。** 2015 年 7 月 4 日のブルゴーニュのクリマ世界遺産登録を推進した協会の会長は **Aubert de Villaine**。

### 🔴 偽造への注意喚起 — **公式が自ら警告している**

✅ 公式サイトに **`/fr/avertissement`「IMPORTANT : CONTREFAÇONS !」**という専用ページがある。
> 「近年の贋作ネットワーク摘発は、**とりわけロマネ・コンティの近年のヴィンテージ**に関するものだった。
> …出所に完全な確信が無い限り、**我々のワインは公式の流通経路（我々のディストリビューターと、彼らが選んだカーヴィスト）
> 以外からは決して買わないこと**。それが真正性と、そして**保存状態の健全性**の唯一の保証である。」

→ **店として「どこから仕入れたか」を答えられる状態にしておくこと。**
**ゲストから出所を問われるのは、この造り手では失礼ではなく正常な質問である。**

### ⚠️🔴 現時点で言ってはいけないこと

- 🔴 **「赤も新樽 100%」— 公式には一度も書かれていない。**
  公式が「新樽（fûts neufs）」と書いたのは **2019 年の Corton-Charlemagne（白）1 件だけ**。
  **赤の新樽比率は非開示。**「樽で 18 ヶ月」だけを言うこと。
- 🔴 **「現当主は Aubert de Villaine」— 2021 年 12 月に甥の Bertrand de Villaine が後任になっている。**
  公式は「叔父 Aubert の後を継ぐ」と明記。**Aubert の名は世界遺産推進協会の会長としてなら安全。**
- 🔴 **「モノポール」— 公式サイトはこの語を一度も使っていない。**
  面積（Romanée-Conti 1.8140ha / La Tâche 6.0620ha）は公式だが、
  **「AOC 全体を単独所有している」という言明は公式サイトからは取れない。**言うなら INAO 等の別の一次資料が要る。
- 🔴 **「Demeter 認証」「ビオディナミ認証」— 認証機関も認証年も公式に一切記載が無い。**
  言ってよいのは「**ビオディナミ**」まで。**「オーガニック認証」も言わない。**
- 🔴 **「DRC と Domaine Leroy は同じ造り手」— 違う。**
  Leroy 家が DRC の株主の半分であることは公式（1942 年〜）。
  **しかし Domaine Leroy は別法人で、DRC 公式サイトは一言も触れていない。**
- 🔴 **「Corton も自社畑」— 違う。fermage（賃借）。Corton-Charlemagne は métayage（分益小作）。**
  どちらも **2008 年／2018 年からの新参**であり、100 年以上持っている Vosne-Romanée のクリュとは性格が違う。
- ⚠️ **「グラン・クリュしか造らない」— 断定しない。**
  **Vosne-Romanée 1er Cru "Les Petits-Monts"** が 2022 年収穫報告に、**Bâtard-Montrachet** が 2016 年収穫報告に出てくる。
  公式は説明していないが、**存在は公式文中にある。**
- ⚠️ **「馬で耕している」— DRC の公式サイトには記述が無い。**（Domaine Leflaive の話と混ぜない）
- ⚠️ **点数・評価を DRC の公式見解として語らない。**公式サイトに第三者点数の掲載は一切無い。
- ⚠️ **リストの価格をヴィンテージごとに口頭で断定しない**（intake の価格配列が VT と 1:1 でない）。

### 3 軒の対比（リスト上で効く）

| | Louis Latour | Domaine Leflaive | **Domaine de la Romanée-Conti** |
|---|---|---|---|
| 栽培 | ISO 14001 の減農薬。**認証オーガニックではない** | **ビオディナミ 25 年超・馬耕** | **ビオディナミ。防除は銅と硫黄のみ。認証機関は非公表** |
| 除梗 | ❓ | （白のみ） | **年により 0〜100% 全房** |
| 熟成 | 白 8–10ヶ月／赤 10–12ヶ月、**GC 新樽 100%** | **樽 1 年＋タンク 6 ヶ月＝18 ヶ月** | **樽 18 ヶ月。新樽比率は非開示** |
| 情報開示 | **キュヴェ別 PDF あり（最も厚い）** | サイトのみ（PDF なし） | 🔴 **商品説明が存在しない。開示は面積と収穫本数と収穫日誌のみ** |
| 規模 | 自社畑 48ha（GC 27ha） | Puligny の GC 4.8ha | **9 GC 合計 30.7365ha** |

---

## Akio's Insight

*（この節は Akio 専用。未記入。他の情報源からの記述で埋めない。）*

---

## Canonical Conflict

**なし。** `producer:domaine-de-la-romanee-conti` に重複する canonical 生産者レコードは検出されていない。
配下キュヴェ 9 件にも重複・語順違い・命名規約の二重化は無い。

⚠️ **以下は衝突では「ない」。REGISTER.md §C の誤検出クラスに既出であり、重複報告しない。**

| ペア | 分類 |
|---|---|
| `Corton` / `Corton-Charlemagne` | **別 AOC・別色。**§C「別アペラシオン」に**明示済み** |
| `Échézeaux` / `Grands Échézeaux` | **別 AOC。**§C に**明示済み** |
| `Romanée-Conti` / `Romanée-Saint-Vivant` | **別 AOC。**§C の同クラス |
| `Domaine de la Romanée-Conti` / `Domaine Leroy` / `Maison Leroy` | **姓・資本関係の一致にすぎない。**Leroy 側の課題は **REGISTER P-1** で既登録。**DRC 側から重ねて起票しない** |

🔴 **REGISTER.md への追記は不要と判断する。**（新規の衝突を検出していないため）

📌 **ただし architecture 側で別途扱うべき事項が 2 件ある — これらは「衝突」ではなく「モデルの欠落」である。**

1. **`Corton-Charlemagne` キュヴェが canonical に存在しない**（OBP 1 本が未解決）。
   公式で実在・面積・取得年・初収穫年まで確定しているので、**Packet B の新規キュヴェ候補として素性は最良**。
   **research では登録しない。**
2. **保有形態（所有 / fermage / métayage）を canonical が表現できない。**
   DRC の Corton は 2008 年から fermage、Corton-Charlemagne は 2018 年から métayage であり、
   **畑の出自は Domaine Prince Florent de Mérode 等の他生産者**にある。
   Romanée-Saint-Vivant も **1966 年 fermage → 1988 年に所有へ転換**している。
   **「そのキュヴェをいつから、どういう権原で造っているか」は現在 canonical のどこにも入らない。**
   → **Louis Latour のドメーヌ／ネゴシアン区分、Leflaive の 3 ブランド構造と同じ「生産形態の軸」の問題。**
   REGISTER の共通課題 1（同一家族の複数ブランドのモデル化）に**隣接するが同一ではない**。
   **Akio / CTO の判断が要る。research では動かさない。**

---

## Sources

### 一次資料（公式サイト・2026-08-04 参照）✅

`https://www.romanee-conti.fr/` — **`/fr/` のみ。`/en/` は本文が空で使用不可。**

| ページ | 得た主な事実 |
|---|---|
| `/`（トップ） | Richard Olney『Romanée-Conti』(Flammarion, 1991) からの引用 2 文 |
| `/fr/familles` | **2 家族の全系譜と生没年**、1869 Duvault Blochet、1942 Henri Leroy、共同経営者の交代史、**2019 Perrine Fenal / 2021 Bertrand de Villaine**、監査役会の変遷 |
| `/fr/philosophie-du-domaine` | 312 年 Eumène の頌詞、クリマ論、**GC はブルゴーニュの面積・生産の 1% 未満**、**7 クリュ＋2008/11 Corton ＋ 2018/11 Corton-Charlemagne 2.91ha**、**3 つの作業軸**（土壌／旧 RC 由来の très fin ピノの選抜／チームの資質） |
| `/fr/un-prince-de-sang` | **コンティ公 Louis-François de Bourbon（1717–1776）**、**Clos de Bèze の 10 倍の価格**、自分の食卓専用、Mme de Genlis の評、Rousseau の庇護者、息子 Louis-François-Joseph（1734–1814)、革命による「bien national」売却 |
| `/fr/1500-histoire` | **年表 47 件を全件取得**（900–2019）。Saint-Vivant 創建、1131 Hugues II、1512 Cloux、1584 Claude Cousin、**1651 「Romanée」初出**、**1760 コンティ公取得**、1763 La Goillotte、**1794 「Romanée-Conty」初出**、1819 Ouvrard、**1869 Duvault Blochet**、1911 Louis Clin、**1933 La Tâche**、1940 André Noblet、**1942 société civile ＋ Henri Leroy**、**1963 Montrachet**、**1966 RSV fermage**、1974 新定款、**1979 La Goillotte**、**1984 Bernard Noblet / Gérard Marlot**、**1988 RSV 買取**、1992 Roch 兄弟、**2008 Corton fermage ＋ Bertrand 参加**、2010 移転、**2015 ユネスコ**、**2018 Corton-Charlemagne métayage**、2019 Perrine Fenal |
| `/fr/9-grand-crus` ＋ **個別 9 ページ** | 🔴 **9 クリュの面積（小数点 4 桁）／1953–2019 の年別収穫本数／クリュ別の性格づけと引用**。Corton の fermage 経緯（Mérode・Clos du Roi/Bressandes/Renardes・初収穫 2009）、Corton-Charlemagne の métayage 経緯（初収穫 2019） |
| `/fr/9-grands-crus/bouteilles-recoltees` | ドメーヌ全体の年別総収穫本数（1953–2019） |
| **`/fr/millesimes/{2009…2022}`（14 年分）** | 🔴 **Farming / Winemaking の実質的な一次資料。**ビオディナミの明言と防除資材（銅・硫黄）、耕耘、選果 2 段構え＋14 人の選果台、**除梗の年変動（0〜100% 全房）**、プレ発酵浸漬、**醸し 18–21 日**、pigeage の遅いリズム、素足の pigeage（34–35℃）、**樽 18 ヶ月**、白の樽・フードル発酵、**Corton-Charlemagne 2019 の新樽＋専用フードル**、**クリュ別収量と収穫日**、Noblet → Bernier の交代、Nicolas Jacob / Didier Dubois、**Petits-Monts と Bâtard-Montrachet の存在**、Duvault-Blochet の 1870 年の小冊子『De la Vendange』 |
| `/fr/notes-de-degustation` | クリュ別・年別のテイスティングノート（**2013 VT まで**） |
| `/fr/mentions` | **法人名・RCS Dijon D 778 269 407・所在地 21700 Vosne-Romanée** |
| `/fr/avertissement` | 🔴 **偽造への公式警告と、公式流通経路以外から買わないよう求める文言** |
| `/fr/galerie` | 連絡先 `contact@romanee-conti.fr`、写真クレジット |

保存先: `research/producers/_sources/domaine-de-la-romanee-conti/`（HTML 24 件 ＋ 抽出テキスト 24 件 ＋ 年表整形 1 件）

### 二次資料
**なし。本書は全面的に公式サイトのみに基づく。** 小売・EC・インポーター・レビュー集約サイト・
Wikipedia・検索スニペットは**一切使用していない。**

---

## Confidence

| 節 | Confidence | 理由 |
|---|---|---|
| Identity | **High** | 法人名・RCS・所在地まで公式 |
| **History** | **High** | **公式年表 47 件＋家族ページの全系譜。生没年つき。この生産者で最も厚い節** |
| Location | **High**（畑）／ **Low**（総面積） | 9 クリュは 4 桁精度で公式。**ドメーヌ総面積は公式に数字が無く、1er cru と Bâtard の面積も不明** |
| **Farming** | **Medium-High** | **ビオディナミと防除資材は公式に明言。**ただし**専用ページが無く、認証機関・転換年が不明** |
| **Winemaking** | **Medium-High** | 除梗・浸漬・醸し日数・pigeage・樽 18 ヶ月まで公式で取れた。**新樽比率・酵母・SO2・清澄濾過が非開示** |
| Style | **Medium** | 造りからの構造的説明は可能。**公式の表現は詩的で、第三者点数も飲み頃も無い** |
| Important Cuvées | **High** | 全 8 キュヴェが公式で実在・面積・取得年まで確定。未解決 1 本も公式で解消できる |
| Staff Notes | **High** | すべて上記から構成。⚠️ リストが 10 項目と厚い |
| **総合** | **High — staff-usable。70% を明確に超える。** | 薄いのは Style と新樽比率のみ。**その薄さは「この造り手は語らない」という事実そのもの**であり、⚠️ リストで代替してある |

---

## Open Questions

**残り 9 件。いずれも staff 運用を止めるものではない。**

1. 🔴 **2026 年現在の経営体制。** 公式サイトは **2021 年 12 月（Bertrand de Villaine 就任）で止まっている。**
   Perrine Fenal・Isabelle Roch・Henri de Villaine の現況、および現在の chef de cave / chef de culture が
   Alexandre Bernier / Nicolas Jacob のままかは**公式では確認できない。「現在性未確認」。**
2. **ビオディナミの認証機関（Demeter / Biodyvin）と転換開始年。** 公式に一切記載が無い。有機認証の有無も不明。
3. 🔴 **「9 Grands Crus」の枠外の畑。** **Vosne-Romanée 1er Cru "Les Petits-Monts"**（2022 年報告に収穫日あり）と
   **Bâtard-Montrachet**（2016 年報告に畑あり）の**面積・生産量・独立ラベルの有無**が公式に無い。
   canonical は Petits Monts のみ登録しており、Bâtard-Montrachet は未登録。
4. **赤の新樽比率・樽元・樽材・トースト・天然酵母・SO2・清澄／濾過の有無。** 公式に記述ゼロ。
5. **2016 年の Échézeaux / Grands Échézeaux / Montrachet の収穫本数。**
   収穫報告は「Éch 6hl/ha、Grands-Éch 7hl/ha を収穫」と書くのに、**クリュページの本数表は空欄。公式内の不整合。**
6. **Corton-Charlemagne の「初収穫」と「初リリース」。**
   `/philosophie-du-domaine`「2022 年に披露予定」対 クリュページ「2019 年に初収穫」。**両立するが公式は明示していない。**
7. **ドメーヌの総面積と、9 クリュ以外の保有一覧。** 公式に一つの数字が無い。
8. **2020–2023 ヴィンテージの収穫本数・収量。** 公式データは 2019 年（本数）／2022 年（報告）で停止。
   **OBP に載る 2023 は公式の射程外。**
9. **Bernard Noblet の chef de cave 就任年。** 年表は **1984**（父 André の引退年）、
   2017 年収穫報告は **1986**（父 André の死去年）。**公式内で不一致。**

### 前回実行からの差分（解決済み）
~~英語公式サイトが読めない~~ → **英語版は HTML の `<p>` が空。`/fr/` を読むのが唯一の正解** ✅
~~公式サイトは情報が薄いのではないか~~ → **薄いのは「商品説明」だけ。年表 47 件と収穫報告 14 年分は極めて厚い** ✅
~~テクニカルシート PDF の有無~~ → **存在しない。収穫報告 14 年分がその代わりになる** ✅
~~OBP 未解決の Corton-Charlemagne が何者か~~ → **2018/11/11 métayage・2.9132ha・初収穫 2019・9,110 本。完全に確定** ✅
~~Farming が書けるか~~ → **ビオディナミ、防除は銅と硫黄のみ、と公式に明言あり** ✅
