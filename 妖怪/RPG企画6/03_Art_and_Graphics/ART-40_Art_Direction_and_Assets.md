---
uid: [ART-40]
role: art-direction
status: active
depends_on:
  - ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
influences:
  - ART-41_Prompt_Library.md
  - ../99_Archive_and_References/WRD-99_Archive_and_Changelog.md
---

# [ART-40] Art Direction and Assets

このファイルは「視覚演出ディレクターの視点」から書かれています。世界観を崩さず、誰が制作しても同じ画面に着地するための実務基準を定義します。

## 同一キャンバス原則

- 神も人も同じ和紙・同じ岩絵具で描く
- 差は素材ではなく筆致で出す
- 神: 制御された細線、低ノイズ、冷白と群青
- 人: 滲み、掠れ、粒状感、泥と錆の温度

この原則を破ると、思想の対立が素材差に見えてしまうため禁止する。

## 幕タイトルと色設計

- 第1幕【胎】: 白と硬い輪郭、静止の緊張
- 第2幕【融】: 滲み境界、混色と流動
- 第3幕【熾】: 赤のフレア、粒子飛散、臨界
- 第4幕【結】: 金継ぎ線の脈動、再構成の光
- 終幕【還】: 熱の減衰、土へ還る色温

## 付喪神化の演出規則

- 金継ぎ線は静止光ではなく脈動光で描く
- 覚醒時は赤寄りの熱を短時間だけ重ねる
- 背景全体に金線を撒かない。介入は武器境界だけに限定する

## キャラクタービジュアル運用

- ミコト: 白髪ボブと赤いスカーフ。器としての余白
- うかみ: 土色と鉄。壁役の重量感
- スクナ: 酸性の色調。薬理と危険性
- ウズ: リズム破壊を示す曲線と残像
- タチバナ: 透明感と損耗を同居させる
- マヒト: 煤と火花。修復と破壊の二面性
- ワカヒコ: 対称性、冷白、停止の線

## スタイルアンカー（短縮版）

```text
masterpiece, traditional Japanese painting on highly textured Washi paper,
mineral pigments, divine disciplined lines vs human chaotic bleeding,
tragic beauty, muddy warmth, no 3D render, no glossy CGI.
```

### ネガティブ指定（必須）

```text
no sci-fi UI, no cyber gadget, no plastic texture, no cel-shading,
no glossy metal world, no western medieval costume mismatch.
```

## キャラクター制作チェック

| 項目 | チェック内容 |
|---|---|
| ミコト | 白髪ボブ、赤いスカーフ、器の余白がある |
| うかみ | 土色主体、重量感、防壁の説得力がある |
| スクナ | 毒性の色調、知性と危険性が同居している |
| ウズ | 動きの軌跡が読めない、攪乱性がある |
| タチバナ | 透明感と痛みが同時に見える |
| マヒト | 鍛造段階が見分けられる（加入直後/拠点Lv2/野外Lv2） |
| ワカヒコ | 対称性、冷白、停止の気配がある |

## 実務フロー

1. WRD-01で対立軸を固定する
2. NAR-10で幕ごとの感情温度を確認する
3. SYS-20で体験テンポと演出密度を合わせる
4. キャラクター制作チェックで破綻を潰す
5. 最終出力を本ファイル基準でレビューする

Promptの詳細資産は [ART-41_Prompt_Library.md](ART-41_Prompt_Library.md) を参照。
