---
uid: [ARC-00]
role: governance
status: active
depends_on:
  - ../00_Welcome_and_Introduction/README.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
---

# [ARC-00] Architecture and Governance

このファイルは「開発・実装担当」のためのガイドラインおよび管理台帳です。一貫した品質と SSOT（Single Source of Truth）を維持するための規約を定義します。

## 1. 実装規約 (Charter)

### Zero-Loss 編集ポリシー
- **固有語彙・数値・条件式を削除しない**: 平易化は要約ではなく、補助説明の追加で行います。
- **仕様矛盾時の優先順**: `SYS-30 (数理)` > `SYS-20 (体験)` > `WRD-01 (世界観)`。

### 語彙運用ルール
- **神話語彙の優先**: ゲーム内テキスト（台詞・説明文）では、Ref-00 の翻訳表に基づき、SF/メカ語彙を徹底排除します。
- **禁止語の置換例**:
  - `AI / システム` → `神託 / 神意`
  - `データ` → `神話記録 / 神の理 / 履歴`
  - `クラッシュ` → `破綻 / 崩落 / 断絶`

---

## 2. UID 台帳 (Registry)

すべてのドキュメントは以下の UID で管理されます。廃棄された UID も欠番扱いにし、再利用は禁止します。

| UID | カテゴリ | ファイルパス | 役割 |
|---|---|---|---|
| `[WRD-01]` | Welcome | 00_Welcome_and_Introduction/README.md | 世界観・デザイン原則 |
| `[NAR-10]` | Story | 01_Story_and_Characters/NAR-10_Narrative_and_Characters.md | 物語・人物・幕 |
| `[SYS-20]` | System | 02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md | 遊び方・体験・生態系 |
| `[SYS-22]` | Skill | 02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix.md | 術式・ロール索引 |
| `[SYS-30]` | Logic | 02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md | 数理・フラグ・SSOT |
| `[ART-40]` | Art | 03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md | 美術・プロンプト |
| `[ARC-00]` | Dev | 90_For_Developers/ARC-00_Architecture_and_Governance.md | 規約・管理（本書） |
| `[REF-00]` | Ref | 99_Archive_and_References/REF-00_References_and_Archive.md | 外部参照・翻訳表 |

---

## 3. 移植・ギャップ管理 (Migration)

RPG企画5から6への移行において、特に以下の重複対策を徹底します。

- **重複正本の禁止**: 同一の情報（例：武器のダメージ倍率）が複数のファイルに記述されている場合、SYS-30 のみを正本とし、他は参照リンクのみを置きます。
- **責務の分離**:
  - 体験・意図（「なぜそうするか」）は **SYS-20**
  - 実装・値（「どう動くか」）は **SYS-30**
  - 演出・背景（「どんな雰囲気か」）は **ART-40 / NAR-10**

### 時代考証チェックリスト
1. 神話語彙に無理なく翻訳できるか。
2. 常世・祭具・神意のいずれかで説明可能か。
3. 近現代の固有技術知識を前提としていないか。
4. 説明の主軸が神術・魔術・儀礼に置かれているか。

---
**変更履歴・差し戻し案の保管は [../99_Archive_and_References/REF-00_References_and_Archive.md](../99_Archive_and_References/REF-00_References_and_Archive.md) を参照してください。**
