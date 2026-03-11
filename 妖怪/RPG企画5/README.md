---
uid: [ARC-INDEX]
project_code: RPG企画5
title: アシブネノミコト 〜天降る御子と、星屑の大地〜
status: draft
owner: Architecture Guardian
depends_on:
  - 00_Governance/ARC-00_Implementation_Charter.md
influences:
  - 01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md
  - 02_Narrative/NAR-10_Narrative_and_Characters.md
  - 03_Systems/SYS-20_Game_Systems_and_Flow.md
  - 03_Systems/SYS-30_Data_and_Logic_Architecture.md
  - 04_Art/ART-40_Art_Direction_and_Assets.md
  - 05_References/REF-50_Reference_DQ_Master_Data.md
---

# RPG企画5

本ディレクトリは、RPG企画4の知見を継承しつつ、以下を初期条件として再構築した新世代プロジェクトである。

> 運用宣言（2026-03-11）: `妖怪/RPG企画5` を唯一の編集先とする。`妖怪/RPG企画4` は参照専用で運用する。

- [ARC-00]: 変更時は必ず影響範囲分析を先に行う。
- [ARC-01]: すべての正本ドキュメントにUID、depends_on、influencesを必須化する。
- [WRD-01]: SF語彙を禁止し、神話語彙へ統一する。

## ディレクトリ構造

- `00_Governance/`: 実装思想、UID台帳、運用ルール。
- `01_Worldbuilding/`: コア思想、世界観、アーカイブ。
- `02_Narrative/`: 物語設計、人物設計、幕構造。
- `03_Systems/`: 体験設計、数理設計。
- `04_Art/`: ビジュアル設計、演出。
- `05_References/`: 外部参照資料。

## ジャンクション・リンクの運用

作業の便宜上、ルート直下に `ALL-files` というディレクトリを用意し、
主要ドキュメントへの**シンボリックリンク**を配置しています。これは
ファイルそのものを複製せずに別名アクセスできるだけでなく、
編集時に元ファイルと自動的に同期されるため、参照や検索が容易になります。

新しいドキュメントを追加した場合は以下のいずれかの手順を踏んでください。

```powershell
# ALL-files 配下にリンクを作成
cd '...\妖怪\RPG企画5\ALL-files'
New-Item -ItemType SymbolicLink -Path <リンク名> -Value '..\<相対パス>'
```

またはワンライナーで複数リンクを生成するスクリプトを用意しても構いません。
将来的に自動化したい場合は、`Scripts/` に簡易 PowerShell スクリプトを
追加しておくと良いでしょう。

この仕組みはディレクトリ単位のジャンクション（`ALL-files` 自身）が
あらかじめ設定されているため、フォルダ構成を変更してもリンクは
壊れません。リンクと実体のバージョン管理は Git で行えますが、
シンボリックリンクをコミットする際はプラットフォーム間の互換性に
留意してください。

## ドキュメント一覧

UID | パス | ステータス | 説明
---|---|---|---
ARC-00 | 00_Governance/ARC-00_Implementation_Charter.md | active | Architecture Guardian 実装憲章（運用ルール）
ARC-01 | 00_Governance/ARC-01_UID_Registry.md | active | UID 台帳（UID と命名規則）
WRD-01 | 01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md | active | 世界観・コアビジョン
WRD-99 | 01_Worldbuilding/WRD-99_Archive_and_Changelog.md | active | 廃棄案・変更履歴とアーカイブ
NAR-10 | 02_Narrative/NAR-10_Narrative_and_Characters.md | active | 物語・登場人物設計
SYS-20 | 03_Systems/SYS-20_Game_Systems_and_Flow.md | active | ゲームシステムと体験フロー
SYS-30 | 03_Systems/SYS-30_Data_and_Logic_Architecture.md | active | データ・論理アーキテクチャ（数値定義）
ART-40 | 04_Art/ART-40_Art_Direction_and_Assets.md | active | アート指針・プロンプト集
REF-50 | 05_References/REF-50_Reference_DQ_Master_Data.md | reference-only | 外部参照資料（RPG4 ドラクエデータ）

## RPG企画4からの移行マップ

- `妖怪/RPG企画4/00_Core_Vision_and_Theme.md` -> `01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md`
- `妖怪/RPG企画4/10_Narrative_and_Characters.md` -> `02_Narrative/NAR-10_Narrative_and_Characters.md`
- `妖怪/RPG企画4/20_Game_Systems_and_Flow.md` -> `03_Systems/SYS-20_Game_Systems_and_Flow.md`
- `妖怪/RPG企画4/30_Data_and_Logic_Architecture.md` -> `03_Systems/SYS-30_Data_and_Logic_Architecture.md`
- `妖怪/RPG企画4/40_Art_Direction_and_Assets.md` -> `04_Art/ART-40_Art_Direction_and_Assets.md`
- `妖怪/RPG企画4/50_Reference_DQ_Master_Data.md` -> `05_References/REF-50_Reference_DQ_Master_Data.md`
- `妖怪/RPG企画4/99_Archive_and_Changelog.md` -> `01_Worldbuilding/WRD-99_Archive_and_Changelog.md`

## 移行方式

- 方針: 再編集優先（重複削減・語彙統一・依存関係正規化）
- 優先順: `SYS-30` -> `SYS-20` -> `WRD-01` -> `NAR-10` -> `ART-40` -> `REF-50` -> `WRD-99`
- 凍結対象: `妖怪/RPG企画4`（参照専用）

> **アーカイブ注意:** 旧フォルダ内の7ファイルにはそれぞれYAMLメタデータ
> が追加され、`status: frozen` と `migrated_to` が記録されました。編集は
> 一切行わず、必要な箇所はRPG企画5側で参照または修正してください。
