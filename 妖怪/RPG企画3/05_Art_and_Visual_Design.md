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
- **物理的質感とシルエットの融合:**
  - 各キャラクターの「傷・生存・執着」の痛切さが、特異なシルエットと、和紙の上で予測不可能に広がる「色彩の滲み」の両面から直感的に伝わる設計とする。

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
- **コンセプト:** 空の器、白と赤、金継ぎ、アシンメトリーな防具。
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

## 4. UI/マップ・ビジュアル定義

- **UIデザイン:**
  - **神のUI（タイムライン等）:** 弥生土器や銅鐸のラインを模した、細く幾何学的なデザイン。青白く発光する。
  - **人のUI（コマンド等）:** 縄文土器の荒々しい粘土の質感。金継ぎのラインで枠が補修されている。
- **マップ表現:**
  - 世界地図は「ひび割れた陶器」。移動ルートは「金継ぎのライン」として描画される。

## 5. Prompt運用導線（追加）

- ミコト冒険者初期装備（赤スカーフ版）などを含む生成実行は新設の `Visual_Prompt_Pack_DECONSTRUCTION_V1.md` を使用。
- 生成結果の採否判定は同ファイル末尾のチェックリスト（古代感・非SF・人間側の泥絵具感・神側の白磁幾何学感・シルエット・物語整合）に従う。