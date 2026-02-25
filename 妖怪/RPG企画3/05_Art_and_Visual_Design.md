**【プロジェクト・コア・フィロソフィー】**
* **タイトル:** アシブネノミコト —泥と星の神話—
* **テーマ:** 「完璧な神の理」に対する、「不完全な人間の熱量」の肯定。
* **デザイン原則:**
  * 神（敵・システム）は、傷を恐れ、無機質で完璧な予測（エントロピーの凍結）を行う。
  * 人（味方・プレイヤー）は、傷を歴史として引き受け、摩擦やエラー（ノイズ）で神の理を砕く。
* **すべての仕様は、「効率的な消費」ではなく「泥臭い修復と継承」をプレイヤーに体感させるために存在する。**

---

# 05_Art_and_Visual_Design

## 1. ビジュアル・フィロソフィー

本作のアートワークは、「和紙と岩絵具の滲み」と「白磁・幾何学」という全く異なる二つの質感を衝突させ、その間を「金継ぎ」で繋ぐ「ハイブリッド・ディコンストラクション（脱構築）」のアプローチを採用する。鳥山明風の均一な描線やポップな記号性からは完全に脱却し、同時に大衆性を損なうホラー的厚塗りも排し、質感の暴力的なコントラストによってテーマを視覚化する。

- **西洋ファンタジーの禁止:**
  - 革鎧、プレートアーマー、西洋剣、マント、SFガジェットは原則排除する。
  - 代わりに「貫頭衣」「麻布」「縄」「骨」「石」「青銅」「鉄滓」を用いる。
- **対立構造の視覚化:**
  - **人（縄文・熱量）:【和紙・水彩・岩絵具の滲み】** キャラクターの造形自体は現代的で万人に愛される美しさを担保する。しかし塗りの質感は、和紙の繊維に吸い込まれるような水彩・岩絵具の予測不要な滲み（Bokashi/Bleeding）に限定する。デジタルに制御しきれない「生者のノイズと温もり」をアナログなマチエールで表現する。
  - **神（弥生・理）:【白磁・幾何学ベクターアート】** 筆致やノイズを一切排除した無機質で滑らかな質感。傷ひとつない鏡面反射と冷たい発光。左右対称（シンメトリー）、幾何学的で無菌の美しさ。有機的な揺らぎの一切の排除。
  - **金継ぎの介入（摩擦と修復）:** 両者の衝突時の被弾エフェクト、拠点（社）の修復時、移動ルートの描写においてのみ、「鋭く発光する黄金（金漆・箔）」を介入させる。泥と白磁の隙間を金漆が縫い合わせる構成。
  - **三貴子の視覚メタファー（特異点）:** 
    - **アマテラス:** システムの中核として「凍りついた白磁」と「完璧な円環（停止）」で表現され、一切の揺らぎがない。
    - **ツクヨミ:** 無菌化の執行者として「影（立体感）を消し去るフラットな光」と「瑕瑾のない純白」を放ち、画面から泥臭いコントラストを奪い取る。
    - **スサノオの遺産（天叢雲剣）:** 「極限の摩擦」と「赤錆」、そして夥しいまでの「金継ぎの歴史（歴代の傷）」の集合体として描画する。
- **物理的質感とシルエットの融合:**
  - 各キャラクターの「傷・生存・執着」の痛切さが、特異なシルエットと、和紙の上で予測不可能に広がる「色彩の滲み」の両面から直感的に伝わる設計とする。
- **ウズとうかみの共犯者感:** 彼らは神話的夫婦像からのロマンスではなく、互いの「場を壊す能力」に気付いた泥臭い同士として描写される。視覚的には二人が並んだとき、動きのリズムや色彩がひそやかに響き合うよう演出する。

## 2. スタイルアンカー（AI生成用共通プロンプト）

全アセット生成時に適用する基本スタイル定義。

> 実制作で使用する最新版プロンプト一式は `Visual_Prompt_Pack_LUMINOUS_WASHI_V3.md` を参照。
> 本章は「世界観・美術制約の正本」、Promptファイルは「運用テンプレート」として扱う。

```text
# 00_STYLE_ANCHOR_LUMINOUS_WASHI
masterpiece, highly detailed, exquisitely beautiful character faces,
(for human elements): traditional Japanese watercolor style, painted on textured Washi paper, mineral pigments (Iwa-enogu), beautiful unpredictable chromatic bleeding, soft ink washes, organic analog warmth, visible paper fibers,
(for divine elements): extremely flawless white porcelain sculpture, perfectly smooth ceramic surface, completely inorganic, geometric perfection, modern 3D render feel, zero bleeding, zero texture,
(for shared/magic elements): glowing raised metallic gold kintsugi lacquer filling cracks and boundaries,
NO thick impasto, NO oil painting, NO messy mud, NO western horror styles, NO flat cel-shading,
```

## 3. キャラクター・プロンプト定義

### 3.0 運用制約（2026-02-24 更新）
- **古代コンセプト固定:** 近代衣装・西洋甲冑・SF意匠は採用しない。
- **質感コントラスト厳守:** 人間側は泥・油彩の重さ、神（敵・システムUI）側は白磁の無機質さを徹底する。
- **画風より役割優先:** ポップな記号記法を捨て、役割と「傷」が重厚な質感とシルエットから読み取れる姿勢・表情を優先する。
- **造形美と華の担保:** 泥臭い世界観であっても、キャラクターの顔立ちや骨格は「万人受けする圧倒的な美しさ・華やかさ」を大前提とする。無骨さや男らしさは、骨格を崩す醜悪さ（ブサイク）としてではなく、整った顔立ちの上に添えられた「色気のある傷」や「力強い視線」として表現する。

### 主人公「ミコト」【古代アレンジ版】
- **コンセプト:** 空の器、白と赤、金継ぎ、アシンメトリーな防具。赤いスカーフは漁村アマで贈られた英雄の証として常時巻かれ、物語の旅路を通じて“形見”“呪い”と意味が変化する。見た目は海風と血に晒されたように端が擦り切れ、ところどころ泥汚れが滲んでいる。
```text
Prompt:
Full body character design of the protagonist "Mikoto" in their first adventurer's outfit.
style: heavy impasto painting, thick clay-like textures, rough analog strokes.
hairstyle: a short bob of pure white hair, textured like thick white paint.
costume: An ancient Japanese sleeveless "Kantoui" (primitive tunic) made of rough, off-white woven fabric, tied with a thick, coarse rope (shimenawa) around the waist. A LONG, FLOWING SCARF of a BOLD RED color is wrapped around their neck. The clothes show subtle signs of being repaired with glowing gold lacquer (Kintsugi). Asymmetrical arm guards made of crude clay and bone.
appearance: Their large, expressive eyes show a newfound determination.
pose: Standing on a cliff with the wind blowing their red scarf, creating a dynamic silhouette.
environment: A windy cliff overlooking a vast primitive landscape, painted with heavy, textured earth tones.

Negative Prompt:
anime style, toriyama style, cel shading, clean crisp lines, western armor, medieval clothes, modern clothing, uniform
Params:
--ar 2:3 --stylize 350 --quality high --seed 55831
```

### 狂騒の踊り子「ウズ」【古代アレンジ版】
- **コンセプト:** アメノウズメ、非対称な舞衣、巨大なリボン（羽衣）、神楽鈴。**道化やピエロ的な要素は排除し、あくまで古代の奉納舞を強調する。**
- **髪型アイデア:** しめ縄を模した編み込みを取り入れ、神聖さと土地感を視覚化する。
```text
Prompt:
Full body character design of the female dancer "Uzu".
style: heavy impasto painting, thick clay-like textures, rough analog strokes.
hairstyle: High twin-tails tied with ancient cords, messy and energetic, rendered with thick brushstrokes.
costume: A revealing, asymmetrical ancient dancer's outfit made of colorful hemp layers. A GIANT, FLOATING RIBBON (hagoromo) made of translucent fabric wraps around her, creating a distinct silhouette. She holds a cluster of bronze bells (kagura suzu).
appearance: Mischievous grin, dynamic pose mid-dance.
details: Jomon-style pottery patterns on the fabric, barefoot.
```

### 3.4 スクナ（冷徹な薬学者）
- **コンセプト:** 外見は小児体型だが、視線と立ち振る舞いはまるで老練な化学者。可愛げを排し、知的な不気味さと狂気の匂いを前面に出す。臨場感のため、通常は薬鉢をロープで肩にかけ引きずるように運ぶ（地面に痕跡が残るイメージ）スタイルと、必要に応じて背負って担ぐスタイルの両方を運用する。
- **表情:** 三白眼、冷徹な侮蔑の視線、ニヒルな笑み。ダークサークルを強調し、睡眠不足と研究疲れを示す。
- **雰囲気:** 水彩の滲みは毒や薬品を想起させる酸緑や傷紫。背景は危険な実験室の汚れと毒液の飛沫。
```text
Prompt:
masterpiece, highly detailed, a small boy with a sharp, intellectual, and slightly menacing aura.
style: traditional Japanese watercolor on textured Washi paper, mineral pigments (Iwa-enogu), but the bleeding colors suggest toxins and chemicals (acid green, bruised purple).
facial features: NOT CUTE, NOT CHERUBIC. He has sharp, narrowing "Sanpaku" eyes with a cold, analytical gaze that dissects the viewer. Dark circles under his eyes from sleepless research. A cynical, arrogant smirk (sneer) on his face. He looks like a weary adult soul trapped in a child's body.
details: extremely short hair under a rough woven cap. He is dragging a disproportionately MASSIVE, heavy iron mortar used for crushing medicine; a long, thick wooden pestle-like club (杵) is slung or carried with him, the club showing wear from repeated pounding. The mortar and stick are stained with dark, suspicious residues. He wears a heavy leather apron stained with soot and chemical burns.
atmosphere: The washi paper texture around him is stained with splatters of black ink and poisonous colorful washes, suggesting a dangerous laboratory environment.

Negative Prompt:
innocent, adorable, cute, cherubic, blush, happy smile, disney style, ghibli style, soft pastel colors, clean clothes, mascot character, cheerful, round eyes, childish innocence
Params:
--ar 4:5 --stylize 350 --quality high --seed 44899
```
### 3.3 うかみ（野生の斥候／行者）
- **コンセプト:** 25歳前後の洗練された美青年。普段は俊敏な野生の斥候として行動し、のちに荒野を巡礼する行者へと変貌する二面性を持つ。年齢表記を明示しつつ、中年化バイアスを排除するためクリーンシェーブを徹底。
  * **成熟バリエーション:** 物語の別視点用として、猿田ヒコ的な渋みと威厳を持った40歳前後の「rugged mature」ウカミ版も運用可能。こちらは短い髭と厚い胸板、weathered但気品ある風貌をプロンプトに含める。
- **視覚ディテール:** 風に乱れる暗髪、引き締まった筋肉美、丸い人間耳。斥候装備は麻と革の実用的なギア。行者版では色あせた斎衣と祈りの念珠、錆びた錫杖を持つ。

```text
Prompt:
masterpiece, exquisitely beautiful and universally appealing facial features, an exceptionally handsome 25-year-old young male scout with a clean-shaven, sharply defined jawline. He possesses an elegant yet masculine heroic aura, piercing yet reliable eyes, and fully human facial features. He is a youthful yet highly capable young adult with commanding presence and stoic dignity – unmistakably Japanese with regular rounded human ears (no pointiness at all) and no animalistic traits. He should look like someone respected and loved by his companions, dressed in simple yet functional gear befitting an early civilization.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: wind‑tousled dark hair tied back with a cloth band. Lean, athletic build painted with warm, organic watercolor washes. Clothing made of woven hemp and soft leather with some decorative stitching and a faded sash. Standing in a relaxed, alert pose with a calm, resolute expression, holding a wooden spear with a shaped stone tip. The ancient woodland background is hinted with deep, overlapping washes of green and brown ink.

Negative Prompt:
old, middle-aged, facial hair, stubble, wrinkles, rugged veteran, uncle, oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, sophisticated weapons, perfectly neat hair, pointed ears, elven features, animal ears, exaggerated anime ears, nudity, exposed torso, undressing, "ears must be rounded human" (affirmative restriction)
Params:
--ar 2:3 --stylize 250 --quality high --seed 44826
```

```text
Prompt:
Use the uploaded scout image as the base – edit and transform it into a masterpiece featuring a solemn yet exquisitely beautiful 25-year-old young male ascetic (行者). He is exceptionally handsome, clean-shaven, with an elegant yet masculine heroic aura, tanned skin and regular rounded ears, keeping the original scout’s posture and proportions. He is dressed in weathered saffron robes and has prayer beads around his neck. He holds an ancient Shakujo (Khakkhara) staff. The metal is rendered with the texture of aged, oxidized bronze and rust that bleeds into the paper. His pose remains meditative but alert, set amidst a primordial forest background rendered with deep, overlapping washes of green and brown ink.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: long, flowing dark hair tied back with a frayed rope, lean muscular build painted with warm, organic watercolor washes. Robes and simple sandals show signs of wear from pilgrimage. The environment remains the same primordial forest.

Negative Prompt:
old, middle-aged, facial hair, stubble, wrinkles, rugged veteran, uncle, oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, sophisticated weapons, perfectly neat hair, pointed ears, elven features, animal ears, exaggerated anime ears, nudity, exposed torso, undressing, "ears must be rounded human" (affirmative restriction)
Params:
--ar 2:3 --stylize 250 --quality high --seed 44826
```

## 4. UI/マップ・ビジュアル定義

- **UIデザイン:**
  - **神のUI（タイムライン等）:** 弥生土器や銅鐸のラインを模した、細く幾何学的なデザイン。青白く発光する。
    * ツクヨミ撃破時の「白化」（画面UI全体を純白に染め、文字がひび割れる）演出はこのUIの極端な応用として実装すること。フラットな無影照明を用い、ユーザーに一瞬の勝利感と不穏な違和感を同時に与える。
  - **人のUI（コマンド等）:** 縄文土器の荒々しい粘土の質感。金継ぎのラインで枠が補修されている。
- **マップ表現:**
  - 世界地図は「ひび割れた陶器」。移動ルートは「金継ぎのライン」として描画される。

## 5. Prompt運用導線（追加）

- ミコト冒険者初期装備（赤スカーフ版）などを含む生成実行は新設の `Visual_Prompt_Pack_DECONSTRUCTION_V1.md` を使用。
- 生成結果の採否判定は同ファイル末尾のチェックリスト（古代感・非SF・人間側の泥絵具感・神側の白磁幾何学感・シルエット・物語整合）に従う。