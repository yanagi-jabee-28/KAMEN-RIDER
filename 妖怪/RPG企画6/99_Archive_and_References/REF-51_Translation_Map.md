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

## 拡張対応表（運用正本）

### DQ由来要素の翻訳

| 外部語彙 | 本作語彙 | 効果翻訳の要点 | 適用先 |
|---|---|---|---|
| メタル系 | 剥落の星屑 | 高防御・短時間帰還・高報酬のレア雑魚として扱う | SYS-21 / REF-50 |
| テンション | 共鳴過熱 | 新ゲージを作らず、情念と武器耐久度の相互作用へ統合する | SYS-20 / SYS-30 |
| 特技封じ | 凍結の真空 | 行動の静止・封鎖として神話語彙へ置換する | SYS-21 / SYS-30 |
| 場ルール改変 | 無菌の帳 / 血の泥沼 | 環境圧として設計し、戦術再計画を要求する | SYS-21 |
| 反射 | 理の反射鏡 | 限定反射の条件を明示し、無制限反射を避ける | SYS-30 |

### SF/メタ語彙の翻訳

| 禁止語彙 | 推奨語彙 | 変換時の注意 | 適用先 |
|---|---|---|---|
| AI / システム | 神託 / 神意 | 判定主体を機械ではなく神話的意思へ置換する | WRD-01 / NAR-10 |
| ナノマシン | 祟りの粒 / 呪い | 微細干渉を呪術作用として記述する | WRD-01 / NAR-11 |
| データ | 神話記録 / 神の理 | 数値実装はSYS-30、本文は神話語彙へ分離する | SYS-30 / WRD-01 |
| アルゴリズム | 儀式手順 / 理の段取り | 手順は儀礼として説明し、実装式はSYS-30へ置く | ARC-00 / SYS-30 |
| クラッシュ | 破綻 / 崩落 / 断絶 | ゲーム内文言に機械語を残さない | NAR-10 / SYS-20 |

## 適用チェック

1. 名称だけでなく、効果・条件・コスト・対象をセットで翻訳したか。
2. 翻訳後の責務が正本へ収まっているか（値はSYS-30、物語はNAR-10など）。
3. ゲーム内文言へSF語彙が残っていないか。
4. 変換判断を [WRD-99_Archive_and_Changelog.md](WRD-99_Archive_and_Changelog.md) に記録したか。

## 翻訳手順

1. 名称だけでなく効果・条件・コスト・対象を同時に翻訳する
2. 神話語彙へ置換できない項目は採用しない
3. 採用時はWRD-99へ変更理由を記録する

## 参照

- 外部辞書: [REF-50_Reference_DQ_Master_Data.md](REF-50_Reference_DQ_Master_Data.md)
- 体験設計: [../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md](../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md)
- 実装正本: [../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md](../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md)
