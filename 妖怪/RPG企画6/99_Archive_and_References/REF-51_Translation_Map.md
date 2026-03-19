---
uid: [REF-51]
role: translation-map
status: reference-only
depends_on:
  - REF-50_Reference_DQ_Master_Data.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
influences:
  - WRD-99_Archive_and_Changelog.md
  - ../90_For_Developers/ARC-00_Implementation_Charter.md
---

# [REF-51] Translation Map

このファイルは「外部参照の翻訳辞書」です。REF-50の内容を本作語彙へ落とすための対応表を保持します。

## 基本対応

| 外部語彙 | 本作語彙 | 適用先 |
|---|---|---|
| テンション | 共鳴過熱 | SYS-20 / SYS-30 |
| メタル系 | 剥落の星屑 | SYS-21 |
| 反射 | 理の反射鏡 | SYS-20 |
| 封印 | 神託崩壊系干渉 | SYS-21 |
| 呪文封じ | 凍結の真空 | SYS-21 |

## 翻訳手順

1. 名称だけでなく効果・条件・コスト・対象を同時に翻訳する
2. 神話語彙へ置換できない項目は採用しない
3. 採用時はWRD-99へ変更理由を記録する

## 参照

- 外部辞書: [REF-50_Reference_DQ_Master_Data.md](REF-50_Reference_DQ_Master_Data.md)
- 体験設計: [../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md](../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md)
- 実装正本: [../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md](../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md)
