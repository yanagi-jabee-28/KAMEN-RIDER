---
uid: [ARC-01]
role: uid-registry
status: active
depends_on:
  - ARC-00_Implementation_Charter.md
influences:
  - ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
  - ../99_Archive_and_References/WRD-99_Archive_and_Changelog.md
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

# [ARC-01] UID Registry

> ※このフォルダはゲーム内部の管理台帳です。物語や遊び方を知りたい方は 00〜03 番台を先に読んでください。

## UID一覧（RPG企画6）

- `[ARC-INDEX]` : 00_Welcome_and_Introduction/README.md
- `[ARC-00]` : 90_For_Developers/ARC-00_Implementation_Charter.md
- `[ARC-01]` : 90_For_Developers/ARC-01_UID_Registry.md
- `[WRD-01]` : 00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
- `[NAR-10]` : 01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
- `[NAR-11]` : 01_Story_and_Characters/NAR-11_Act_Detail_Guide.md
- `[SYS-00]` : 02_How_to_Play_and_Mechanics/00_Beginner_Guide.md
- `[SYS-20]` : 02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
- `[SYS-21]` : 02_How_to_Play_and_Mechanics/SYS-21_Enemy_Ecology_and_UI.md
- `[SYS-22]` : 02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix_PlayerFacing.md
- `[SYS-30]` : 02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
- `[ART-40]` : 03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
- `[ART-41]` : 03_Art_and_Graphics/ART-41_Prompt_Library.md
- `[WRD-99]` : 99_Archive_and_References/WRD-99_Archive_and_Changelog.md
- `[REF-50]` : 99_Archive_and_References/REF-50_Reference_DQ_Master_Data.md
- `[REF-51]` : 99_Archive_and_References/REF-51_Translation_Map.md

## 命名規則

- 接頭辞は役割を示す（ARC/WRD/NAR/SYS/ART/REF）
- ハイフン後の数値は領域内の固定番号
- 既存UIDの再利用は禁止
- 廃止時も台帳から削除せず、WRD-99へ移管記録を残す
