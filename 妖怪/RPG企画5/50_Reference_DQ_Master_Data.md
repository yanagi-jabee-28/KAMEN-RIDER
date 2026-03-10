# RPG企画5 - 50 Reference DQ Master Data (外部参照翻訳辞書)

本ドキュメントは外部要素を本作へ翻訳するための対照表であり、直輸入を許可するものではない。実装詳細は30を参照する。

## 1. 翻訳原則 [#ID:R5_Translation_Principles]
- 直輸入禁止
- 機能意図は保持
- 語彙と演出は本作世界へ再記述

## 2. 翻訳対照表 [#ID:R5_DQ_Mapping]
| 外部記号（参照用） | 本作語彙 | 保持する機能意図 | SSOT参照 |
| --- | --- | --- | --- |
| 高防御・短時間離脱型敵 | 剥落の星屑 | 短時間攻略の緊張 | `30` の [#ID:R5_Forbidden_Terms_Guard] |
| 技封鎖フィールド | 凍結の真空 | 行動制限による判断圧 | `30` の [#ID:R5_Field_Rules] |
| バースト強化 | 共鳴過熱 | 高火力と代償の両立 | `30` の [#ID:R5_Resonance_Burst] |
| 反射系行動 | 理の反射鏡 | 対象選択の再考 | `30` の [#ID:R5_Forbidden_Terms_Guard] |

## 3. 監査ルール [#ID:R5_Reference_Audit]
- 直輸入語は最終文書から除去する。
- 本作語彙に翻訳できない要素は採用しない。
- 採用不可の理由は `99_Archive_and_Changelog.md` に記録する。

## 4. 注意事項
本ファイルは参照辞書であり、変数・式・フラグ定義を書かない。詳細は `30_Data_and_Logic_Architecture.md` を参照。