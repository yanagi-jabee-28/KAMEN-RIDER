---
uid: [ARC-00]
role: governance
status: active
depends_on:
  - ARC-01_UID_Registry.md
influences:
  - ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../99_Archive_and_References/REF-50_Reference_DQ_Master_Data.md
---

# [ARC-00] Implementation Charter

> ※このフォルダはゲーム内部の実装ルールと開発規約を記載しています。遊び方を知りたい方は [../00_Welcome_and_Introduction/README.md](../00_Welcome_and_Introduction/README.md) を参照してください。

## Zero-Loss編集ポリシー

- 固有語彙・数値・条件式を削除しない
- 平易化は要約ではなく補助説明の追加で行う
- 仕様矛盾時の優先順は `SYS-30 -> SYS-20 -> WRD-01`

## 保護語彙（変更禁止）

情念 / 活魂 / 武器耐久度 / 付喪神化 / 代受苦 / 極大代受苦 / 神の理 / 金継ぎ / 剥落の星屑 / 神託崩壊 / 無菌の帳 / 血の泥沼

## 語彙運用

- ゲーム内文脈では神話語彙を優先
- 現代SF語彙はゲーム内文へ混入させない
- 実装文書では必要な技術語のみ許可

## 変更手順

1. 対象UIDを特定する
2. depends_on と influences を確認する
3. 正本を先に更新し、下流文書へ波及させる
4. WRD-99へ変更履歴を記録する

## 品質ゲート

- 参照パスが解決する
- 用語の改変がない
- SYS-20に実装式が混入していない
- SYS-30に体験文だけの重複が増えていない
