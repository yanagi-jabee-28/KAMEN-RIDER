---
title: Forms — Alps‑Gear (spec)
kind: design
audience: internal
owners: [mechanics-team]
status: draft
references: [products_nagano.csv, wildlife_issues_nagano.csv]
version: 0.1
---

# フォーム仕様（要旨）
目的: 各フォームを「何を解決するか／いつ使うか／代償は何か」の3軸で定義し、脚本・玩具設計・演出に一貫性を与える。

## フォーム一覧（短縮表）
| フォーム | 担当地域 / モチーフ | 主要役割 | 強み | 代償・運用制約 |
|---|---:|---|---|---|
| Alps‑Gear (基本) | 中信 / 精密時計 | 指揮・精密格闘 | 高スタミナ・精密制御 | 決定打不足 |
| Fortress Onbashira | 中信〜南信 / 御柱・城 | 絶対防御・群体停止 | 防壁・突進 | 機動力低 |
| Aero Linear / Ground | 南信 / リニア・航空 | 広域索敵・搬送 | 迅速展開・レーダー | 紙装甲 |
| Shadow Obsidian | 北信 / 忍者・黒曜石 | 潜入・瞬走・根系ハック | ステルス・奇襲 | 神経負荷・開放地不可 |
| Magma Asama / Kiln | 東信 / 火山・窯 | 熱殲滅 → 精密焼成 | 汚染焼成・寄生除去 | オーバーヒート・暴走誘発 |
| Prime Ferment | 発酵・昆虫食 | 暴走克服・循環バフ | 敵制御・再生 | 機動微低下 |
| Grand Symphony | 全県統合 | 法則指揮・広域再生 | 合意増幅・同時奏 | 参加疲労・時間制限 |

## 実装ノート（設計への落とし込み）
- 各フォームは「オン／オフ」ではなく『部分同時奏（micro‑threading）』をサポートする。演出、玩具ギミックは部分的展開を優先すること。
- 代償は必ず“プレイの戦略要素”にする（例: 瞬走＝1回の挽回/高リスク）。
- テストケース: 各フォームごとに『最適シーン』『避けるべき状況』『連携例』を1ページにまとめる。
---

# デザイン・ガイドライン：「統一の中の多様性」

目的: すべてのフォームが「同じヒーローの異なる表情」として認識されるよう、共通の意匠・デザイン言語を定める。地域ごとの個性を損なわずに、視覚的な一体性を実現する。

## コア要素（全フォーム必須）

### 1. シルエット & 立ち姿（視認性の核）
**コンセプト**: 「アルプスの峰々が立ち並ぶ姿」
- 肩幅は狭めに、頭部から腰にかけて三角錐のシルエット
- 胸部から脚部にかけて「稜線」を意識した硬角的な輪郭
- 頭部は「山頂」をイメージ（やや尖り気味）

**具体例**:
- 基本形 (Alps-Gear): 肩甲骨～肋部に精密な幾何学模様で「稜線」を表現
- Shadow Obsidian: 肩が落ちて見えるが、脚から背中にかけて鋭い「峰」をつくる
- Fortress Onbashira: 円柱状だが、上下に絞りをつけて「山」の視覚的リズムを保つ

### 2. アーマー配置 & 菌糸パターン（統一デバイス）
**コンセプト**: 「フィラメント菌糸体が身体を守り、地脈を読む」

- **菌糸ラインの共通ルール**:
  - 脊柱軸に沿って背中を上下貫く「主軸線」→ 全フォーム共通
  - 肋部から関節周辺にかけて放射状パターン → 地域ごとに「密度」と「色」で差別化
  - 四肢の外側に「縦線」、内側に「横線」で双方向の力を表現
  
- **色別の菌糸表現**:
  - 基本形・南信: 明るい群青 + シルバーの複合メッシュ
  - 北信: 黒曜石の光沢を模した黒 + 深紫の微細ライン
  - 東信: 赤銅色 + 橙のグラデーション
  - 発酵・最終形: 虹色の微細フィラメント（イリデッセンス）

### 3. カラーパレット（長野四季モデル）
**基調色の選定理由**: 長野県の自然環境と産業を反映

| フォーム | 主色 | 副色 | アクセント | 根拠 |
|---|---|---|---|---|
| Alps-Gear (基本) | 群青 | シルバー | 透明感のあるライトブルー | 信州の澄んだ空気と精密機械 |
| Fortress Onbashira | 土色 (焦茶) | 白（漆喰） | 赤系（朱） | 御柱祭と城郭建築 |
| Aero Linear | スカイブルー | ホワイト | 新幹線黄色系 | 航空宇宙と長野新幹線 |
| Shadow Obsidian | 黒 (深黒) | 深紫 | 深緑 | 黒曜石と北信の忍者伝承 |
| Magma Asama | 赤銅色 | オレンジ～赤 | 黒（溶岩冷却） | 浅間山の火山と窯業 |
| Prime Ferment | 深緑 + 茶色 | クリーム色 | 金色（発酵） | 発酵食と自然循環 |
| Grand Symphony | 全色のハーモニー | - | 白（統合） | 県全体の共鳴 |

### 4. ロゴ & シンボル（胸部マーク共通）
**デザイン言語**: 「フォッサマグナの大地裂」と「菌糸の結節点」の融合

- **基本形態**: 
  - 中央に X 字形の地裂（フォッサマグナを意識）
  - 交点に発光する円形ノード（菌糸体の心核）
  - 円周を囲む 8 方向の小さな峰（8 つの関係機構 or 県内地域）

- **各フォーム版のバリエーション**:
  - **北信**: X がより鋭角的 (45°より急斜)、紫色発光
  - **東信**: X のラインが炎っぽくうねる、赤色発光
  - **中信**: X が完全対称、青白い発光
  - **南信**: X の太さが不均等（非対称美学）、金色発光
  - **Prime Ferment**: X の交点から放射状に「菌糸」が伸びる、虹色
  - **Grand Symphony**: 全色が同時に点滅する、白～七色

---

## 各フォームの視覚的個性化（地域性の実装）

### 北信フォーム：Shadow Obsidian（黒曜石の密黒）
**印象**: 「谷底の秘密、切り裂く光」

- **素材感**: 黒曜石の鏡面光沢 → 表面が濡れたようにテカテカ
- **肉付き**: 細身で、筋肉線が浮き立つ（忍者のしなやかさ）
- **オーラ**: 紫色の微かな光（まるで夜間暗視）
- **装飾**: 肋部に「忍びのマーク」（古い様式）、肩甲骨にネットワークライン
- **足元**: ブーツのラインが黒 → 音を立てない走行を連想

**他フォームとの見分けポイント**:
- 何より「黒い」「細身」が特徴 → 遠目でも Shadow Obsidian と判定可能

### 東信フォーム：Magma Asama / Kiln（炎熱のラッパ）
**印象**: 「焚火のゆらめき、白く燃える鍛冶」

- **素材感**: 赤銅色の鈍い光沢、随所に「亀裂」が浮かぶ（溶岩冷却跡）
- **肉付き**: 胸部・上腕が張り出す（熱で膨張する感じ）
- **オーラ**: 炎っぽい赤～橙のグラデーション、随時揺らぐ
- **装飾**: 胸部に「窯」のシンボル、腕甲が厚い（耐熱）、背中に排熱スリット
- **足元**: 足の裏が発光（歩くたびに足跡が焦げる）

**他フォームとの見分けポイント**:
- 「赤い」「膨張感」「熱オーラ」が特徴 → 中～遠距離でも温度感で判別

### 中信フォーム：Alps-Gear 基本形（精密時計の冷徹）
**印象**: 「磨き上げた歯車、止まらぬ秒針」

- **素材感**: ポリッシュされたシルバー、かすかなブルーティント
- **肉付き**: 自然で均整の取れた体型（完成度の高さ）
- **オーラ**: 透明感のある青白い光、稜線に沿って幾何学的に点滅
- **装飾**: 胸部に「時計盤」、腕甲に「歯車」刻印、肩甲骨に「精密回路」
- **足元**: 足底に「コンパス用のポイント」（大地を測る）

**他フォームとの見分けポイント**:
- 「青白い」「几帳面」「対称性」が特徴 → 静止画でも存在感がある

### 南信フォーム：Fortress Onbashira（杉の柱、動かぬ威厳）
**印象**: 「樹の根、大地の重さ」

- **素材感**: 焦茶色の木質感（杉の樹皮っぽい）、白い部分は漆喰
- **肉付き**: 太く短く、円柱的（御柱そのもの）
- **オーラ**: 暖色系のゆっくりした光、地面から湧き上がる感じ
- **装飾**: 胸部に「御柱祭の輪」、肩甲骨に「朱色の曲線」（桃山建築風）、足に鎖足輪（根の表現）
- **足元**: 土ぼこり、地響き → 重さと安定感を視覚化

**他フォームとの見分けポイント**:
- 「太い」「地の色」「動かない感」が特徴 → 走るより立つ絵面

### 最終形態：Prime Ferment & Grand Symphony（虹色の共鳴）
**Prime Ferment の視覚的特徴**:
- 各フォームの「いいとこ取り」の細身シルエット
- 全身が虹色に光る菌糸パターン → 複数フォームの特性を同時保持する象徴
- 胸部マークが「複数の色が同時に回転」

**Grand Symphony の視覚的特徴**:
- あらゆる色が調和した状態 → 複数フォームの全カラーが「レイヤー状に重なる」
- 輪郭の「稜線」が 8 本以上に増える（複雑さと統合性の両立）
- 全身から「音の波紋」が放射状に伝わる（不可視の力を可視化）

---

## 実装時の注意点（CGI・実写・玩具展開）

### CGI表現での実装指針
- **菌糸パターンのライティング**: 自発光ではなく「内部照明」の質感で、奥行きを出す
- **色の発光度**: 基本形は低彩度落ち着き、Final Forms は高彩度点滅で「変身」を強調
- **アーマー表面の質感**: Shadow は鏡面、Magma は粗面、Alps は研磨面と区別

### 実写/スーツ表現での実装指針
- **生地の素材**: 全フォーム共通で「光沢系ストレッチスーツ」ベース、色と装飾で差別化
- **装飾パーツ**: 3D プリント装甲 + 刺繍による菌糸ライン → 予算内で実現可能
- **LED埋込み**: 胸部マークと菌糸の主軸線のみ LED を埋め込む（視認性×コスト最適化）

### 玩具展開での実装指針
- **共通フレーム**: ボディは同じ金型を使用、頭部・胸部・四肢の装甲パーツを交換可能に設計
- **カラーバリエーション**: 各フォーム 3 色展開で十分（主色 + 副色 + 白基調版）
- **変身ギミック**: 基本形 → 各フォーム への段階的な部位追加で「進化」を表現

---

## 視覚的な統一性チェックリスト

製作・イラスト・CGI チーム向け：
- [ ] このフォームの「シルエット」は「アルプスの峰」をイメージしているか？
- [ ] 胸部マークに「X字の地裂 + 発光ノード」が含まれているか？
- [ ] 背中～腰の「主軸線」は垂直に通っているか？
- [ ] 指定カラーパレットを 3 色以上含んでいるか？
- [ ] 他フォームとの「見分けポイント」が、遠景でも機能しているか？

---

# AI生成プロンプト設計：基本フォーム（Alps-Gear）

目的: 定義されたデザイン仕様から、画像生成AI（NanoBananaPro など）に投入するためのプロンプトを生成する。視覚的イメージの一貫性を保ちながら、反復的な改善を支援する。

## 【基本形式】NanoBananaPro用プロンプト・テンプレート

```
【被写体・キャラ】
Humanoid cyborg hero in a silver and navy blue armor suit, named "Alps-Gear Basic Form".
Standing in a powerful, balanced stance with narrowed shoulders and a triangular silhouette.
Inspired by the peaks of the Japanese Alps and the precision of Swiss watches.

【シルエット・ポーズ】
- Narrow shoulders tapering upward, forming a mountain-peak-like profile from head to torso.
- Defined ridgelines visible along the chest, shoulder blades, and spine.
- Slight forward lean as if surveying the landscape; one hand at chest level, the other relaxed.
- Proportions: head is 1/7 of body, ensuring humanoid believability.

【アーマー・素材感】
- Polished matte-silver armor plates with subtle blue undertones on the main chest and arms.
- Mycelium-inspired threading patterns in glowing navy blue along the spine (vertical axis) and radiating from the chest.
- Rib section features geometric geometric mesh patterns combining silver and pale blue.
- Surface sheen is semi-gloss: not fully reflective, but luminous with internal lighting.
- Joint articulation visible but seamless, suggesting both rigidity and flexibility.

【色彩】
- **Primary Color**: Navy Blue (RGB: 25, 55, 109) — represents Shinshu's clear alpine air.
- **Secondary Color**: Polished Silver (RGB: 192, 192, 192) — represents precision engineering and local watch industries.
- **Accent Color**: Translucent pale blue (RGB: 173, 216, 230) with subtle glow — represents purity and clarity.

【胸部シンボル・マーク】
- Central X-shaped fissure (inspired by the Fossa Magna geological rift) in deep navy.
- Intersection point contains a glowing circular node (represents mycelium core) emitting soft blue-white light.
- Surrounding the node: 8 small mountain peaks in navy outline, arranged radially.
- Overall effect: a mandala-like emblem of unity and geological harmony.

【装飾・ディテール】
- Chest: watch-dial symbol (Roman numerals I–XII subtly etched) beneath the X-mark.
- Arm gauntlets: gear tooth patterns in relief, suggesting mechanical precision.
- Shoulder blades: intricate circuit-board-like line pattern in silver.
- Feet: small compass-point markings on the soles (visible when stepping), suggesting "measuring the earth."
- Spine: continuous glowing line from neck to lower back, representing the "main axis" of mycelium body.

【環境・背景提案】
- Set against a soft, mountain backdrop: distant alpine peaks in cooler tones, misty valleys.
- Ground texture: rocky alpine terrain or polished metallic platform (no clutter).
- Lighting: cool-toned three-point lighting, with the primary light source from upper-left, casting sharp shadows.
- Glow effect: subtle radiance from the chest emblem and spine line, casting soft blue light onto surrounding armor.

【スタイル・トーン】
- Digital illustration or 3D render quality.
- Anime-influenced proportions but with realistic material shaders.
- Heroic yet measured (not overly dramatic); conveys calm authority and precision.
- No extreme action poses; emphasize the standing composure of a tactical commander.

【何をしない（禁止指示）】
- Do NOT add weapons or oversized props.
- Do NOT include human skin exposure; full suit coverage is required.
- Do NOT use bright neon colors; maintain cool, professional palette.
- Do NOT add battle damage or distress; pristine condition only.
- Do NOT include background characters or other figures.
- Do NOT use sci-fi tropes like "energy beams" or "holographic elements" — keep grounded in material design.

【出力形式】
- Resolution: 1024×1024 px (square composition).
- Format: PNG with transparency preferred; JPG acceptable.
- Aspect ratio: full-body vertical shot, with head at 1/6 height from top.
```

## 活用ガイド

### ステップ1：プロンプトの検証チェック
生成前に、以下が含まれているか確認：
- [ ] シルエット指示（「山形」「三角錐」など） → 識別可能性
- [ ] カラーパレット（RGB値）→ 色の一貫性
- [ ] 菌糸パターン描写（「スパイン軸」「放射状」） → 統一デバイスの可視化
- [ ] 胸部シンボル（「X字」「ノード」「8峰」） → ブランド性
- [ ] 禁止指示 → 不要な要素の排除

### ステップ2：AIツールへの入力方法
- **NanoBananaPro**: 上記プロンプトをそのまま投入（英語推奨）。
- **日本語版AI**: 以下の簡略版を使用：

```
【日本語版・簡潔プロンプト】

長野県のアルプス・ギア基本形態。
中信地域のモチーフで、精密時計と山々の峰をイメージしたシルエット。

**シルエット**: 肩幅が狭く、頭から腰にかけて三角形。頭頂がやや尖った山頂っぽい形状。

**色**: 群青色（深い青）とシルバーの組み合わせ。透明感のあるライトブルーをアクセント。

**アーマー**: ポリッシュされたシルバー。背中に群青色の菌糸ラインが脊柱軸に沿って走っている。肋部には幾何学的なメッシュパターン。

**胸部マーク**: X字形の地裂を中央に、交点に発光する円形ノード。周囲に8つの小さな山峰を配置。

**装飾**: 胸に時計盤マーク、腕甲に歯車の刻印、肩甲骨に回路パターン、足裏にコンパスのポイント。

**背景**: アルプス山脈の山々、靄がかった谷。ヒーローは岩場か金属プラットフォームの上に立つ。

**スタイル**: 高品質な3D画像またはアニメ調のデジタルイラスト。落ち着いた、指揮官のような雰囲気。派手ではなく精密さを強調。

**禁止**: 武器なし。肌は見えない（全身スーツ）。ダメージなし。背景に他のキャラなし。
```

### ステップ3：生成結果の評価フォーム

| 評価項目 | 合格基準 | 結果 |
|---|---|---|
| **シルエット一貫性** | 「三角形の山」と認識できるか | ○/△/✗ |
| **カラーパレット** | 群青 + シルバー + 薄い青の3色が識別できるか | ○/△/✗ |
| **菌糸パターン** | 背中の主軸線と肋部の放射状パターンが見えるか | ○/△/✗ |
| **胸部シンボル** | X字 + ノード + 8峰の要素がすべて含まれているか | ○/△/✗ |
| **他フォームとの差別化** | Black Obsidian や Magma Asama との違いが明らかか | ○/△/✗ |
| **全体の統一性** | 「同じヒーローの基本形」に見えるか | ○/△/✗ |

合格数が 5/6 以上なら採用；4/6 以下の場合は、不合格項目を指摘してプロンプトを改善。

### ステップ4：プロンプト改善の例

**生成結果が「シルエットが丸い」の場合**:
```diff
- Standing in a powerful, balanced stance
+ Standing with angular, mountainous posture; shoulders pulled back and inward
+ Add: "Emphasize sharp, angular silhouette over rounded curves"
```

**生成結果が「菌糸パターンが不可視」の場合**:
```diff
- Mycelium-inspired threading patterns in glowing navy blue along the spine
+ Add precise instruction: "Bright glowing navy-blue lines must be clearly visible running vertically down the spine and radiating outward from the chest like a starburst pattern. These lines should contrast sharply with the silver background."
```

**生成結果が「色が明るすぎる」の場合**:
```diff
- Navy Blue (RGB: 25, 55, 109)
+ Navy Blue (RGB: 15, 35, 80) — darker, more saturated version
+ Add: "Keep colors cool and professional; no bright, glowing neon colors."
```

### ステップ5：バリエーション生成の指示

基本形態が確定したら、以下のバリエーションもプロンプトで生成：

1. **アップショット**（胸部マークのクローズアップ）
   - プロンプト追加：`"Crop to show only the chest emblem and upper torso, with 70% of frame dedicated to the X-shaped mark and glowing node."`

2. **シルエット版**（背光の上でのシルエット）
   - プロンプト追加：`"Backlighting; the figure is rendered as a dark silhouette against a bright sky, with only the glowing spine and chest node visible as light sources."`

3. **360° ターンテーブル視点**
   - プロンプト：3方向（正面・側面・背面）を別々に生成し、動きのある表現に