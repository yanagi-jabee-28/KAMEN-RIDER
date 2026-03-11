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

## 編集前の必読事項

> **このファイルだけ読んでも編集はできない。** 以下の2ファイルを先に読むこと。

### 1. 語彙ルール — SF語彙は混入禁止

ゲーム内テキスト（セリフ・アイテム説明・システムメッセージ）に現代語・SF語彙を使用してはならない。
変換表の全体は [ARC-00 §1.1](00_Governance/ARC-00_Implementation_Charter.md) に定義されている。

代表例：

| 禁止語 | 使うべき語 |
|---|---|
| AI / システム | 神託 / 神意 |
| ナノマシン | 祟りの粒 / 呪い |
| データ | 神話記録 / 神の理 |
| クラッシュ | 破綻 / 崩落 |

なお、仕様書・開発ドキュメント内での実務的な技術語（UI、バグ、Tick等）は許容されている（[ARC-00 §1.2](00_Governance/ARC-00_Implementation_Charter.md) 参照）。

### 2. コアテーマ — 全仕様の判断基準

本作の世界観は **「永遠の結晶化（停滞）vs 傷を抱えた命の還流（変転）」** の一文で要約される。

- **天の神々（イザナギの理）**：悲哀を恐れ、世界を不変の琥珀に凍らせようとする。
- **地上の者たち**：壊れたものを金継ぎしながら、命を次代へ還流させようとする。
- **主人公ミコト**：天の使者として降された「空の器」が、地上の熱に触れ「ただの人間」へ脱皮する。

この対立軸に照らして矛盾する記述を書いてはならない。詳細は [WRD-01 §2](01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md) 参照。

### 3. 変更手順 — UIDと影響範囲の明示が必須

1. 変更対象の UID を明示する。
2. `depends_on` と `influences` を洗い出し、影響範囲を分析する。
3. 本文を変更し、参照先ファイルの整合性差分を反映する。

手順の詳細と影響範囲分析テンプレートは [ARC-00 §2〜3](00_Governance/ARC-00_Implementation_Charter.md) 参照。

### 4. 正本の優先順

矛盾が生じた場合は以下の順で上位ファイルを優先する：

1. `03_Systems/SYS-30_Data_and_Logic_Architecture.md`
2. `03_Systems/SYS-20_Game_Systems_and_Flow.md`
3. `01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md`

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
