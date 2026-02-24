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

本作のアートワークは、鳥山明氏の系譜にある「明瞭なシルエット」と「生命力あふれる描線」を基調としつつ、古代日本の土着的な「泥臭さ」を融合させる。

- **西洋ファンタジーの禁止:**
  - 革鎧、プレートアーマー、西洋剣、マント、SFガジェットは原則排除する。
  - 代わりに「貫頭衣」「麻布」「縄」「骨」「石」「青銅」「鉄滓」を用いる。
- **対立構造の視覚化:**
  - **人（縄文・熱量）:** 非対称（アシンメトリー）、有機的、過剰な装飾、粗い質感、金継ぎの痕跡。泥臭い生命力。
  - **神（弥生・理）:** 左右対称（シンメトリー）、幾何学的、無機質な白磁や鏡面、冷たい青銅。傷一つない無菌の美しさ。
- **シルエット重視:**
  - キャラクターは黒塗りのシルエットでも判別可能な「特異なパーツ（巨大なリボン、ハンマー、注連縄など）」を持つ。

## 2. スタイルアンカー（AI生成用共通プロンプト）

全アセット生成時に適用する基本スタイル定義。

> 実制作で使用する最新版プロンプト一式は `Visual_Prompt_Pack_TORIYAMA_V2.md` を参照。
> 本章は「世界観・美術制約の正本」、Promptファイルは「運用テンプレート」として扱う。

```text
# 00_STYLE_ANCHOR_ANCIENT_JRPG
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Chrono Trigger), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, primitive and organic textures,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi, NO western medieval armor,
```

## 3. キャラクター・プロンプト定義

### 3.0 運用制約（2026-02-24 追加）
- **古代コンセプト固定:** 近代衣装・西洋甲冑・SF意匠は採用しない。
- **髪型シルエット分離:** 主要キャラ間で輪郭が被らないこと。特に「黒い逆立ちサイヤ人型」に収束させない。
- **画風より役割優先:** 画風は共通化しつつ、役割が読める装備・姿勢・表情を優先する。

### 主人公「ミコト」【古代アレンジ版】
- **コンセプト:** 空の器、白と赤、金継ぎ、アシンメトリーな防具。
```text
Prompt:
Full body character design of the protagonist "Mikoto" in their first adventurer's outfit.
hairstyle: a perfectly symmetrical, short bob of pure white hair.
costume: An ancient Japanese sleeveless "Kantoui" (primitive tunic) made of rough, off-white woven fabric, tied with a thick, coarse rope (shimenawa) around the waist. A LONG, FLOWING SCARF of a BOLD RED color is wrapped around their neck. The clothes show subtle signs of being repaired with glowing gold lacquer (Kintsugi). Asymmetrical arm guards made of crude clay and bone.
appearance: Their large, expressive eyes show a newfound determination.
pose: Standing on a cliff with the wind blowing their red scarf, creating a dynamic silhouette.
environment: A windy cliff overlooking a vast primitive landscape.

Negative Prompt:
western armor, medieval clothes, modern clothing, uniform, goku hairstyle, black spiky saiyan hair
Params:
--ar 2:3 --stylize 350 --quality high --seed 55831
```

### 狂騒の踊り子「ウズ」【古代アレンジ版】
- **コンセプト:** アメノウズメ、非対称な舞衣、巨大なリボン（羽衣）、神楽鈴。
```text
Prompt:
Full body character design of the female dancer "Uzu".
hairstyle: High twin-tails tied with ancient cords, messy and energetic.
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

- ミコト冒険者初期装備（赤スカーフ版）を含む生成実行は `Visual_Prompt_Pack_TORIYAMA_V2.md` を使用。
- 生成結果の採否判定は同ファイル末尾のチェックリスト（古代感・非SF・シルエット・髪型重複・物語整合）に従う。