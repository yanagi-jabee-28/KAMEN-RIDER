---
uid: [ART-40]
role: art-direction
status: active
depends_on:
  - ../00_Welcome_and_Introduction/README.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md
influences:
  - ../99_Archive_and_References/REF-00_References_and_Archive.md
---

# [ART-40] Art Direction and Assets

このファイルは「視覚演出ディレクター」および「アセット制作担当」のための正本です。世界観を損なわず、誰が制作しても一貫した画面に着地するための基準を定義します。

## 1. デザインの根幹：同一キャンバス原則

- **神も人も同じ和紙・同じ岩絵具で描く**: 素材の差ではなく、「筆致」の差で対立を表現します。
- **神の筆致**: 制御された細線、低ノイズ、冷たい白（冷白）と深い群青。
- **人の筆致**: 滲み、掠れ、泥と錆の温度、粗い粒状感。

## 2. 幕別カラー設計

- **第1幕【胎】**: 白と硬い輪郭、静止した緊張感。
- **第2幕【融】**: 滲む境界、異なる色が混ざり合う流動感。
- **第3幕【熾】**: 赤のフレア、飛散する粒子、過熱する臨界点。
- **第4幕【結】**: 金継ぎ線の脈動、闇の中に走る再結晶の光。
- **終幕【還】**: 熱の減衰、土へと還る穏やかな温度。

## 3. キャラクター・ビジュアル要件

| 対象 | キーワード | ビジュアルの要点 |
|---|---|---|
| **ミコト** | 余白、器 | 白髪ボブ、赤いスカーフ。感情を書き込む前の「無」の状態。 |
| **うかみ** | 重量感、土 | 土色主体、使い込まれた鉄。仲間を守る壁としての説得力。 |
| **スクナ** | 毒性、知性 | 酸性の色調、細身のシルエット。危険な薬理の気配。 |
| **ウズ** | 攪乱、残像 | 曲線、捉えどころのないシルエット。動きのリズム破壊。 |
| **タチバナ** | 透明感、損耗 | 損耗（キズ）と美しさが同居。脆さと強さ。 |
| **マヒト** | 破壊、修復 | 煤、火花。鍛冶師としての無骨さと、武器を壊す暴力性。 |
| **ワカヒコ** | 対称性、停止 | 冷白、凛とした姿勢。天津神の理を体現する線。 |

## 4. プロンプト・ライブラリ（実務用）

### 基本スタイルアンカー
```text
masterpiece, traditional Japanese painting on highly textured Washi paper, mineral pigments, 
divine disciplined lines vs human chaotic bleeding, tragic beauty, muddy warmth, 
no 3D render, no glossy CGI.
```

### キャラクター生成用（例：ミコト）
```text
mikoto: mid-shot, white bob hair, distinct red scarf, porcelain skin like a vessel, 
void expression, Japanese myth attire, red-line cracked weapon "Kintsugi" style.
```

### 背景・領域生成用（例：黄泉）
```text
yomi: dark violet landscape, stagnation particles, bleeding borders, decaying minerals, 
cold static air, mineral blue highlights on deep black shadows.
```

### ネガティブプロンプト（厳禁要素）
```text
no sci-fi UI, no cyber gadgets, no plastic textures, no cel-shading, 
no glossy metal, no western medieval mismatch, no modern typography.
```

---
**参照先**
- **物語・感情曲線**: [../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md](../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md)
- **体験・テンポ**: [../02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md](../02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md)
- **世界観の根幹**: [../00_Welcome_and_Introduction/README.md](../00_Welcome_and_Introduction/README.md)
