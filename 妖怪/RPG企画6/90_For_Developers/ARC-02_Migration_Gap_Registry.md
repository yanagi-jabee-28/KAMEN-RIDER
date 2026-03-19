---
uid: [ARC-02]
role: migration-gap-registry
status: active
depends_on:
  - ARC-00_Implementation_Charter.md
  - ARC-01_UID_Registry.md
  - ../99_Archive_and_References/WRD-99_Archive_and_Changelog.md
influences:
  - ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
  - ../02_How_to_Play_and_Mechanics/SYS-21_Enemy_Ecology_and_UI.md
  - ../02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix_PlayerFacing.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../03_Art_and_Graphics/ART-41_Prompt_Library.md
  - ../99_Archive_and_References/REF-50_Reference_DQ_Master_Data.md
  - ../99_Archive_and_References/REF-51_Translation_Map.md
---

# [ARC-02] Migration Gap Registry

この台帳は、RPG企画5からRPG企画6への完全移植を「重複ゼロ」で実行するための作業正本です。

## 1. 運用原則

- 詳細仕様は1ファイルのみを正本にする。
- 他ファイルは要約と参照リンクのみを持つ。
- 同一情報の二重正本を禁止する。
- 移植時は「追加」と同時に「重複節の参照化」を行う。

## 2. 情報オーナーシップ（正本境界）

| 情報カテゴリ | 正本ファイル | 非正本の扱い |
|---|---|---|
| 世界観定義 | ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md | 要約のみ可 |
| 幕構造・物語主線 | ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md | NAR-11は実装注記のみ |
| イベント実装注記 | ../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md | NAR-10へ再説明しない |
| 体験原則 | ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md | 敵詳細・実装値を持たない |
| 敵系統/UI読解 | ../02_How_to_Play_and_Mechanics/SYS-21_Enemy_Ecology_and_UI.md | SYS-20/22は参照のみ |
| 初心者向け技選択 | ../02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix_PlayerFacing.md | 詳細値は持たない |
| 計算式・閾値・フラグ | ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md | 他文書で再記述禁止 |
| 美術方針 | ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md | 実行用プロンプトはART-41 |
| 実行用プロンプト詳細 | ../03_Art_and_Graphics/ART-41_Prompt_Library.md | ART-40は方針のみ |
| 実装規約 | ARC-00_Implementation_Charter.md | 他文書に規約重複を持たない |
| UID台帳 | ARC-01_UID_Registry.md | UID定義の二重管理禁止 |
| 参照辞書/翻訳表 | ../99_Archive_and_References/REF-50_Reference_DQ_Master_Data.md / ../99_Archive_and_References/REF-51_Translation_Map.md | 本文側は参照リンクのみ |

## 3. 移植ギャップ台帳（RPG5 -> RPG6）

ステータス定義:
- `Not Started`: 未着手
- `In Progress`: 実装中
- `Done`: 完了

### 3.1 Governance / Reference

| ID | 移植元 | 移植先 | 内容 | 優先度 | 重複対策 | 検証 | Status |
|---|---|---|---|---|---|---|---|
| G-01 | RPG5 ARC-00 1.2 | ARC-00 | SF/メタ語彙の許容/厳禁の明確化 | Critical | ARC-00のみ正本化 | 禁止語混入監査 | Done |
| G-02 | RPG5 ARC-00 1.3 | ARC-00 | 時代考証4条件チェックの明文化 | Critical | ARC-00へ一本化 | 4条件適合レビュー | Done |
| G-03 | RPG5 ARC-00 4 | ARC-00 | 正本優先順（SSOT）の固定 | Critical | ARC-00のみ保持 | 相反記述ゼロ確認 | Done |
| G-04 | RPG5 ARC-01 | ARC-01 | UID廃止時の削除禁止運用 | Critical | ARC-01のみ保持 | UID差分監査 | Done |
| G-05 | RPG5 REF-50補助 | REF-51 | 外部語彙翻訳の拡張表 | High | REF-51正本化 | 用語揺れ監査 | Done |

### 3.2 WRD / NAR

| ID | 移植元 | 移植先 | 内容 | 優先度 | 重複対策 | 検証 | Status |
|---|---|---|---|---|---|---|---|
| WN-01 | RPG5 WRD-01 0.2 | WRD-01 | メタファー補助線の完全移植 | High | WRD-01正本化 | 用語整合 | Done |
| WN-02 | RPG5 WRD-01 3.3 | REF-51 | 外部参照翻訳テーブル再編 | High | REFへ移管 | 重複節ゼロ | Done |
| WN-03 | RPG5 NAR-10 | NAR-10/NAR-11 | 幕説明の二重正本解消 | Critical | NAR-10正本、NAR-11実装注記化 | 重複段落監査 | In Progress |
| WN-04 | RPG5 NAR-10 位相語 | NAR-11 | 位相語運用の完成度向上 | Medium | NAR-11へ限定 | 用語辞書一致 | In Progress |

### 3.3 SYS

| ID | 移植元 | 移植先 | 内容 | 優先度 | 重複対策 | 検証 | Status |
|---|---|---|---|---|---|---|---|
| S-01 | RPG5 SYS-20 敵系統 | SYS-21 | 敵属性/領域詳細の完全移植 | High | SYS-21正本化 | SYS-20重複ゼロ | Done |
| S-02 | RPG5 SYS-20 スキル群 | SYS-30 | 技名/効果/条件の実装表（Wave3で大幅拡張） | Critical | SYS-30正本化 | 値漏れ監査 | In Progress |
| S-03 | RPG5 SYS-20 初心者導線 | SYS-22 | 優先10技の判断導線と再編ルール整備 | High | SYS-22は要約のみ | 仕様値混入ゼロ | Done |
| S-04 | RPG5 SYS-30 | SYS-30 | フラグ・コスト・副作用列の完全化 | Critical | SYS-30のみで管理 | フラグ突合 | Done |
| S-05 | RPG5 SYS-20 導線章 | SYS-23 | ワールド導線/加入順/難度学習の分離移植 | High | SYS-23を導線専用正本化 | NAR重複監査 | In Progress |

### 3.4 ART

| ID | 移植元 | 移植先 | 内容 | 優先度 | 重複対策 | 検証 | Status |
|---|---|---|---|---|---|---|---|
| A-01 | RPG5 ART-40 キャラ詳細 | ART-41 | キャラ詳細プロンプトの再移植 | High | ART-41正本化 | プロンプト重複監査 | Not Started |
| A-02 | RPG5 ART-40 敵神詳細 | ART-41 | 敵神フルプロンプト群移植 | High | ART-41正本化 | 欠落項目ゼロ | Not Started |
| A-03 | RPG5 ART-40 環境5種 | ART-41 | 環境プロンプト群移植 | High | ART-41正本化 | テーマ整合 | Not Started |
| A-04 | RPG5 ART-40 Negative 12項 | ART-41 | ネガティブプロンプト詳細復元 | High | ART-41へ集約 | 禁止要素監査 | Not Started |

## 4. 実行Wave（着手順）

1. Wave-1: Governance/Reference固定（G-05, WN-01, WN-02）
2. Wave-2: NAR重複整流（WN-03, WN-04）
3. Wave-3: SYS完全化（S-01, S-02, S-03, S-04）
4. Wave-4: ART完全化（A-01〜A-04）
5. Wave-5: 横断監査（重複・リンク・front matter・用語）

## 5. 完了判定

- 全IDが `Done`。
- NAR/SYS/ARTで二重正本がない。
- リンク切れゼロ。
- front matterエラーゼロ。
- 用語統一監査で禁止語混入ゼロ。

## 6. 変更履歴

- 2026-03-19: 初版作成（完全移植と重複ゼロ運用の作業台帳として追加）。
- 2026-03-19: REF-51へ拡張翻訳表（DQ由来 + SF/メタ語彙）を追加し、G-05/WN-02を完了化。
- 2026-03-19: NAR-10/NAR-11の責務境界を明文化し、幕説明の二重正本を削減する整理を開始。
- 2026-03-19: SYS-30へCritical欠落（状態異常7種、ICEサブタイプ式、Enemy_Behavior_Tag、不足Story_Flag）を追補し、S-04を着手状態へ更新。
- 2026-03-19: SYS-30へEnemy_Tier_Template追補を追加し、S-04を完了へ更新。
- 2026-03-19: SYS-21を参照中心へ整流し、Tier/行動タグ/状態IDの正本導線を追加（S-01完了）。
- 2026-03-19: SYS-22へ実装参照マップを追加し、初心者向け責務を再固定（S-03完了）。
- 2026-03-19: NAR-11の主要イベント節を「背景/実装要件/検証観点」の3行構造へ整形し、実装注記の可読性を強化（WN-03/04継続）。
- 2026-03-19: SYS-30へWave3として装備実装マスター（スロット/武器カテゴリ/携行具）と全キャラ術式ID群を追補。SYS-22を「優先10技」構成へ拡張し、装備・技の可読性を強化（S-02継続、S-03維持）。
- 2026-03-19: Phase1拡張としてSYS-20/21/30へ体験文脈・脅威可視化・導線/UI実装マスターを追加。新規 `SYS-23_World_Flow_and_Party_Composition.md` を作成し、導線章の分離移植を開始（S-05着手）。
