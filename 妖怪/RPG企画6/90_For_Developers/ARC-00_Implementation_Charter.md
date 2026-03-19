---
uid: [ARC-00]
role: governance
status: active
depends_on:
  - ARC-01_UID_Registry.md
influences:
  - ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md
  - ../02_How_to_Play_and_Mechanics/00_Beginner_Guide.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
  - ../02_How_to_Play_and_Mechanics/SYS-21_Enemy_Ecology_and_UI.md
  - ../02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix_PlayerFacing.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../03_Art_and_Graphics/ART-41_Prompt_Library.md
  - ../99_Archive_and_References/REF-50_Reference_DQ_Master_Data.md
  - ../99_Archive_and_References/REF-51_Translation_Map.md
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

### SF/メタ語彙の許容場面

| 場面 | 扱い | 例 |
|---|---|---|
| ゲーム内テキスト（台詞/説明文） | 非許容 | UI, バグ, ティック, クラッシュ |
| 仕様書・実装メモ | 条件付き許容 | Tick, Flag, Cooldown |
| 準ゲーム内文（物語本文） | 原則非許容 | 必要時は神話語彙へ置換 |

例外規則:
- スクナの科白に限り、医学・薬学語彙（毒物学、薬理、ホルミシス等）を限定許容する。

### 禁止語の代表変換

| 禁止語 | 推奨語 |
|---|---|
| AI / システム | 神託 / 神意 |
| ナノマシン | 祟りの粒 / 呪い |
| データ | 神話記録 / 神の理 |
| クラッシュ | 破綻 / 崩落 |

## 時代考証の判定基準

- 許容: 神話語彙で説明可能な異時代要素
- 許容: 常世由来、祭具由来、神意由来の超常要素
- 非許容: 未来文明を直接想起させる機械・通信前提描写

迷った場合は、WRD-01の対立軸を損なうかどうかで判定する。

### 時代考証4条件チェック

1. 神話語彙へ無理なく翻訳できるか。
2. 常世由来・祭具由来・神意由来のいずれかで説明できるか。
3. 近現代の固有技術知識を前提にしないか。
4. 説明の主軸が神術・魔術・儀礼に置かれているか。

運用:
- 4条件をすべて満たす場合のみ採用候補とする。
- 判定が割れた案件は [../99_Archive_and_References/WRD-99_Archive_and_Changelog.md](../99_Archive_and_References/WRD-99_Archive_and_Changelog.md) に記録して保留判断する。

## 正本の優先順（SSOT）

1. [../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md](../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md)
2. [../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md](../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md)
3. [../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md](../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md)

説明:
- 数式・閾値・フラグはSYS-30を最優先する。
- 体験意図の解釈はSYS-20を優先する。
- 物語・世界観の整合はWRD-01を優先する。

## 変更手順

1. 対象UIDを特定する
2. depends_on と influences を確認する
3. 正本を先に更新し、下流文書へ波及させる
4. WRD-99へ変更履歴を記録する

## 影響範囲分析テンプレート

1. 変更対象UID
2. 変更目的（何を改善するか）
3. 影響を受ける depends_on / influences
4. 同時更新が必要なファイル
5. テスト項目（リンク、用語、責務分離）

## 品質ゲート

- 参照パスが解決する
- 用語の改変がない
- SYS-20に実装式が混入していない
- SYS-30に体験文だけの重複が増えていない
