---
uid: [SYS-30]
role: data-and-logic
status: active
depends_on:
  - SYS-20_Game_Systems_and_Flow.md
  - ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
  - ../90_For_Developers/ARC-00_Implementation_Charter.md
influences:
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../99_Archive_and_References/WRD-99_Archive_and_Changelog.md
---

# [SYS-30] Data and Logic Architecture

> ※このファイルはゲーム内部の計算式・フラグ・マスターデータを記載する開発者向け正本です。遊び方を知りたい読者は [SYS-20_Game_Systems_and_Flow.md](SYS-20_Game_Systems_and_Flow.md) を参照してください。

## 三条の熱源（実装定義）

- `Kakkon_Value`: 活魂（器）
- `Jonetsu_Value`: 情念（熱）
- `Weapon_Durability`: 武器耐久度（摩耗）

## 境界状態判定

```text
IF Kakkon_Value <= 0 AND Jonetsu_Value > 0 AND Has_Shigurui_Passive == TRUE THEN
  State_Shigurui = TRUE
END IF

IF Kakkon_Value > 0 AND Jonetsu_Value <= 0 THEN
  State_Karakara = TRUE
END IF

IF (Kakkon_Value <= 0 AND (Jonetsu_Value <= 0 OR Has_Shigurui_Passive == FALSE))
 OR (Kakkon_Value <= 0 AND Anchor_Equipped_Count == 0) THEN
  State_Dead = TRUE
END IF
```

## 武器耐久度モデル

```text
Durability_new = max(0, Durability_old - (
    Base_Weapon_DurabilityCost * Stance_Multiplier
  + Combo_DurabilityCost
  + Skill_DurabilityCost
  + Intentional_Cost
))
```

- `Stance_Multiplier`:
- 両手持ち（2H）: `1.5`
- 一刀流（1H）: `1.0`
- 二刀流（Dual）: `1.3`

## 主要フラグ

- `DualStanceActive`: ミコト専用二刀流の一時フラグ
- `Mikoto_Gauntlet_Permanent`: 継承手甲の恒久接続
- `Red_Scarf_Event_Key`: 赤いスカーフの永続イベントキー
- `MAHITO_JOINED_ACT2`: 第2幕中盤の加入判定
- `MAHITO_FIELD_LV2_UNLOCKED`: 野外Lv2鍛造解禁
- `SUSANOO_TRIAL_CLEARED`: クリア後試練突破

## メンテナンス段階

```text
Camp_Maintenance_Level = 0
IF StoryFlag.MAHITO_JOINED_ACT2 THEN Camp_Maintenance_Level = 1
IF StoryFlag.MAHITO_FIELD_LV2_UNLOCKED THEN Camp_Maintenance_Level = 2

Base_Maintenance_Level = 1
IF StoryFlag.MAHITO_JOINED_ACT2 THEN Base_Maintenance_Level = 2
IF StoryFlag.SHRINE_FORGE_LV3_UNLOCKED THEN Base_Maintenance_Level = 3
```

## SSOTテーブル運用

- 物語整合は [../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md](../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md)
- プレイヤー体験は [SYS-20_Game_Systems_and_Flow.md](SYS-20_Game_Systems_and_Flow.md)
- 実装値変更は本ファイルを正本として扱う
