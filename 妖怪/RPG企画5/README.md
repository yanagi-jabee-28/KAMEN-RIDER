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

## `ALL-files` の運用

`ALL-files` フォルダは主要ドキュメントの**実体コピー**を置く場所として運用します。
このディレクトリは**追跡除外**とし、リポジトリにはコミットしないようにしてください。
（`.gitignore` に `ALL-files/` を追加するのが手っ取り早いです。）

シンボリックリンクではなくファイルそのものを複製するのは、
他者に渡す際や VS Code や検索ツールから直接開きたい状況に対応するためです。

**自動同期が必要な場合**

ALL-files 配下の各ファイルを「個別シンボリックリンク」に差し替えることで、
元ファイルを編集するとそのリンク先も即時に更新されるようにできます。
以下はディレクトリごとではなく **ファイル単位で**リンクを張る例です。

```powershell
# 例: 00_Governance 内の Markdown を個別リンクに置換する
cd '...\妖怪\RPG企画5\ALL-files'

# 既存コピーを削除
Get-ChildItem -Filter *.md | Remove-Item

# 元ファイルをループしてリンク作成
Get-ChildItem ..\00_Governance -Filter *.md | ForEach-Object {
    $target = $_.FullName
    $link   = Join-Path (Get-Location) $_.Name
    New-Item -ItemType SymbolicLink -Path $link -Value $target
}

# 他のサブフォルダでも同様。
# たとえば 01_Worldbuilding:
# Get-ChildItem ..\01_Worldbuilding -Filter *.md | ForEach-Object { ... }
```

PowerShell の `New-Item -ItemType SymbolicLink` はファイル単位でも機能します。
ジャンクション (`-ItemType Junction`) はディレクトリ専用のため、個別ファイル
では上記のように `SymbolicLink` を使ってください。リンクを作成すると、
直接編集した同じファイルが ALL-files でも反映されます。

リンクは Git 管理下に含めても問題ありませんが、**リンク先が存在しないと
無効になる**ので、クローン先でも同じディレクトリ構造が必要です。


他のマシンへクローンした際にはまずフォルダ自体のジャンクションを再作成します：
```powershell
cd '...\妖怪\RPG企画5'
New-Item -Path .\ALL-files -ItemType Junction -Value .\
```
```
コピーを作成する手順（PowerShell）:

```powershell
# 例: ARC-00 をコピーする
cd '...\妖怪\RPG企画5\ALL-files'
Copy-Item -Path '..\00_Governance\ARC-00_Implementation_Charter.md' -Destination .
```

新しいドキュメントを追加したら、同じように `Copy-Item` を実行して
`ALL-files` へファイルをコピーしてください。複数ファイルをまとめて
コピーするワンライナーやスクリプトを `Scripts/` に置いておくと便利です。

フォルダ単位のジャンクション（`ALL-files` 自身）はすでに設定されて
いるため、ディレクトリ構造を変更してもこのコピー作業には影響しません。

なお、コピーされたファイルは元と内容が同じですが、以降の編集は元
ファイルで行い、必要に応じて同期を手動で行ってください。Gitには
どちらも含めることができますが、重複が煩雑になる場合は `ALL-files`
を `.gitignore` に追加する運用も検討してください。

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
