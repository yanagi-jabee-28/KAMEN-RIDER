---
uid: [ARC-01]
project_code: RPG企画6
title: UID Registry
role: uid-registry
status: active
owner: Architecture Guardian
depends_on:
  - ARC-00_Architecture_and_Governance.md
influences:
  - ../00_Welcome_and_Introduction/README.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../99_Archive_and_References/REF-00_References_and_Archive.md
---

# [ARC-01] UID Registry

本台帳はプロジェクト内の全ドキュメントUIDを管理する「正本」です。命名と参照の基準を定義します。

## 運用メモ
- UIDの削除・改名は原則禁止です。
- 読みやすさ向上のための追記を行う際も、UIDの関係性は保持してください。

## ドキュメントUID一覧

| UID | ドキュメント名 | 配置パス (RPG企画6標準) |
|---|---|---|
| `[WRD-01]` | Core Vision and Theme | `00_Welcome_and_Introduction/README.md` |
| `[NAR-10]` | Narrative and Characters | `01_Story_and_Characters/NAR-10_Narrative_and_Characters.md` |
| `[NAR-11]` | Act Detail Guide | `01_Story_and_Characters/NAR-11_Act_Detail_Guide.md` |
| `[SYS-20]` | Player Manual | `02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md` |
| `[SYS-21]` | Enemy Ecology and UI | `02_How_to_Play_and_Mechanics/SYS-21_Enemy_Ecology_and_UI.md` |
| `[SYS-22]` | Skill Matrix | `02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix.md` |
| `[SYS-30]` | Data and Logic Architecture | `02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md` |
| `[ART-40]` | Art Direction and Assets | `03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md` |
| `[ARC-00]` | Architecture and Governance | `90_For_Developers/ARC-00_Architecture_and_Governance.md` |
| `[ARC-01]` | UID Registry | `90_For_Developers/ARC-01_UID_Registry.md` |
| `[REF-00]` | References and Archive | `99_Archive_and_References/REF-00_References_and_Archive.md` |

## 採番規則 (Naming Convention)

- **Worldbuilding**: `WRD-xx`
- **Narrative**: `NAR-xx`
- **Systems**: `SYS-xx`
- **Art**: `ART-xx`
- **Governance**: `ARC-xx`
- **Reference**: `REF-xx`
- **Archive**: 末尾 `99` (または `REF-xx` 内の履歴セクション)

## 拡張ルール
- 新規システム資料: `SYS-31` 以降
- 新規人物資料: `NAR-12` 以降
- 新規美術資料: `ART-41` 以降
- 新規世界設定: `WRD-02` 以降
