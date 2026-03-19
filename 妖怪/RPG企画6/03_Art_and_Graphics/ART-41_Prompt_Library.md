---
uid: [ART-41]
role: prompt-library
status: active
depends_on:
  - ART-40_Art_Direction_and_Assets.md
  - ../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md
  - ../02_How_to_Play_and_Mechanics/SYS-21_Enemy_Ecology_and_UI.md
influences:
  - ../99_Archive_and_References/WRD-99_Archive_and_Changelog.md
---

# [ART-41] Prompt Library

このファイルは「制作実務者の視点」から書かれています。ART-40の原則を崩さず、生成作業に即投入できるPrompt資産を集約します。

## キャラクターPrompt（短縮）

- ミコト（標準）: 白髪ボブ、赤スカーフ、余白のある中性的シルエット
- ミコト（手甲継承）: 左腕に古鉄の継承手甲、風化した質感
- ミコト（最終）: 三種の神器を修復済みで装備、赤スカーフは退色しない
- うかみ（斥候）: 土色、木槍、重量感、風化した旅装
- うかみ（行者）: 深色法衣、祈祷具、断ち切った継承の余韻
- スクナ: 酸性彩度、病理的知性、小型体躯と重い道具の対比
- ウズ: 高速軌跡、乱拍、奉納舞の破調
- タチバナ: 海色と透過感、喪失と執着の同居
- マヒト: 煤、火花、鍛造段階の可視化
- ワカヒコ: 対称構図、冷白、停止の気配

## 神・敵Prompt（短縮）

- アマテラス: 保存と拒絶、滑らかな白、冷光
- ツクヨミ: 処刑者の端正さ、月光の凍結性
- スサノオ: 粗野な反逆、暴風の運動線
- カガセオ: 砕けた星核、反逆光の残滓
- 澱神系: 泥濁、侵食、複層ノイズ

## 環境Prompt（短縮）

- 白堊の回廊: 白の圧力、行動制限の視覚化
- 灼熱たたら場: 鍛造火花、熱歪み、禁忌感
- 黄泉比良坂: 深色と沈降、未練の堆積
- 星屑の荒野: 灰と金粒、静かな爆心地
- 常世深部: 無菌性、保存圧、絶対秩序

## 実務ルール

- ART-40の同一キャンバス原則を優先
- 背景全面への金線散布は禁止
- SF記号と現代UI記号を混入しない

参照元: [ART-40_Art_Direction_and_Assets.md](ART-40_Art_Direction_and_Assets.md)

## 1. 共通スタイルアンカー（再利用用）

```text
masterpiece, highly detailed, beautifully expressive.
traditional Japanese painting entirely on highly textured, fibrous Washi paper using mineral pigments (Iwa-enogu) and soft ink washes.
The core visual is the collision of two brush systems: disciplined divine lines versus rough human dry-brush bleeding.
tragic beauty, sorrow, muddy warmth.
```

Negative:

```text
3D render, CGI, glossy, plastic, modern UI icons, sci-fi neon interface, photoreal metal shader,
western medieval armor, flat digital gradient only, watermark, signature
```

## 2. キャラクターPrompt（詳細版）

### ミコト（標準）

```text
androgynous Japanese adventurer, white bob hair, single vivid red scarf fluttering in wind,
simple ancient tunic and loose pants, solemn but warm expression,
washi texture and mineral pigment granulation, no modern props.
```

### ミコト（継承手甲）

```text
same as standard Mikoto, with antique asymmetrical black-iron gauntlet on left arm,
subtle hammered texture and indigo binding cord, inheritance weight emphasized.
```

### ミコト（最終）

```text
Mikoto with repaired dark straight sword, bronze mirror, jade magatama,
red scarf keeps pure crimson without fading, battlefield ash and gold dust around.
```

### うかみ（斥候）

```text
rugged middle-aged warrior, muddy traveler cloak, wooden spear, short beard,
earth palette, heavy dry-brush strokes, weathered wild charisma.
```

### うかみ（行者）

```text
ascetic middle-aged man in dark layered robes, prayer beads, solemn expression,
mud and bone traces, spiritual gravity, restrained but intense brushwork.
```

### スクナ

```text
small alchemist with sharp adult-like intellect, toxic green/purple accents,
large stone mortar as constant companion, cynical and precise mood.
```

### ウズ

```text
fierce ritual dancer with explosive movement, asymmetrical garments,
dynamic pigment splashes, playful but dangerous expression.
```

### タチバナ

```text
slender female warrior with sea-soaked melancholic presence,
pale robe with dark stains, water and blood tonal contrast, quiet obsession.
```

### マヒト

```text
one-eyed blacksmith, soot, embers, scarred apron, massive hammer,
material texture should feel heavy, repaired scars as beauty.
```

### ワカヒコ

```text
beautiful cold archer with strict symmetry, pearl-white robes, giant asymmetrical longbow,
blood-red arrow fletchings only, frozen divine precision.
```

## 3. 神・ボスPrompt（詳細版）

### アマテラス

```text
female deity sealed in layered white ceremonial cocoon,
annular eclipse-like muted gold corona, stillness and isolation, no chaotic bleed.
```

### ツクヨミ

```text
perfectly composed male deity, crescent execution blade, moon halo,
ultra-clean fine lines, severe white and ultramarine palette.
```

### スサノオ

```text
storm god with wild masculine energy, refined divine linework mixed with muddy chaotic splashes,
long dark sword with glowing kintsugi scars.
```

### カガセオ

```text
human-like fallen star deity, body fissures stitched as constellation-like gold seams,
supernova eye glow, sorrow and rebellion coexisting.
```

### 八岐の産土

```text
colossal chimera emerging from shattered white shell, eight serpentine heads,
organic tissue + rusted relic fragments + jagged kintsugi bonds, UI-jack mood but analog rendering.
```

## 4. 環境Prompt（詳細版）

### 白堊の回廊

```text
sterile white celestial corridor, geometric perfection ruptured by inner chaotic burst,
vermilion and gold splashes breaking silence.
```

### 灼熱たたら場

```text
forge abyss with heat distortion, sparks, ash, broken weapons,
forbidden forging mood, dense red-orange mineral lighting.
```

### 黄泉比良坂

```text
descending underworld slope, damp dark wash, unresolved grief layers,
bone fragments and mud traces in paper fibers.
```

### 星屑の荒野

```text
ashen wasteland with embedded golden stardust shards,
near-monochrome sumi base with sharp gold punctures.
```

### 常世深部

```text
beautiful sterile prison-like divine space, cold symmetry,
preservation pressure and emotional suffocation emphasized.
```

## 5. 実務チェックリスト

- 同一キャンバス原則を必ず維持する。
- 金線は「傷の境界」に限定し、背景全面には撒かない。
- 付喪神化は脈動する金継ぎ線で表現し、単なる発光にしない。
- 章ごとの位相色（白/滲み/赫/金/還流）を混同しない。
- 迷ったらART-40の原則を優先し、ART-41は運用辞書として使う。

## 6. アイテム・神話意匠Prompt

### 天叢雲剣（素体）

```text
ancient long dark straight sword, segmented and rejoined by thick glowing kintsugi seams,
matte iron surface, strong washi fiber texture, solemn tragic heat.
```

### 八咫鏡

```text
solid bronze disc mirror, warm amber rim and dull olive center,
hand-polished imperfect reflection, ritual object mood, no sci-fi shine.
```

### 八尺瓊勾玉

```text
large rough-carved jade and obsidian magatama beads on coarse cord,
ancient handcraft texture, subtle sacred glow, earthy dignity.
```

### 継承手甲（Beat Gauntlet）

```text
asymmetrical antique black-iron left gauntlet, articulated fingers,
bronze disk binding with indigo cord, inheritance weight and battle scars.
```

## 7. UI・画面演出Prompt

### 予測線崩壊演出

```text
fine ink prediction lines cracking on washi surface,
pigment bleeding from fractures, solemn analog glitch feeling, no digital HUD look.
```

### 無菌の帳UI

```text
sterile white overlay with restrained geometric lines,
minimal noise, suffocating preservation pressure, calm but hostile stillness.
```

### 血の泥沼UI

```text
deep crimson and umber fluid overlays, rough dry-brush intrusion,
unstable readability, emotional pressure, analog texture first.
```

## 8. 失敗例と修正テンプレ

| 失敗パターン | 原因 | 修正指示 |
|---|---|---|
| 背景に金線が散りすぎる | kintsugi指定が広すぎる | 「kintsugi only on repaired seams, not background」追加 |
| 神側が人側と同じ筆致になる | chaos指定が強すぎる | divine側に「ultra-controlled fine lines」を追加 |
| 近未来感が出る | UI語彙が混入 | 「no sci-fi interface, no cyber motifs」を追記 |
| 暗いだけで位相差がない | 幕ごとの色温指定不足 | 幕位相キーワード（白/滲み/赫/金/還流）を明記 |

## 9. 運用メモ

- 短縮Promptは試行速度重視、詳細Promptは再現性重視で使い分ける。
- 神・敵・環境は同セッションで連続生成し、色温と紙質を揃える。
- 迷ったら [ART-40_Art_Direction_and_Assets.md](ART-40_Art_Direction_and_Assets.md) の原則へ戻る。
