# Core Rules (Generated)

## Story Flags
- `flag_mahito_joined_act2` (MAHITO_JOINED_ACT2): ON
- `flag_mahito_field_lv2_unlocked` (MAHITO_FIELD_LV2_UNLOCKED): OFF
- `flag_shrine_forge_lv3_unlocked` (SHRINE_FORGE_LV3_UNLOCKED): OFF
- `flag_routeb_choice` (RouteB_Choice): OFF

## Boundary States
- `shigurui`: `kakkon <= 0 and jonetsu > 0`
  - 物理無効、行動ごとに情念を消費
- `karakara`: `kakkon > 0 and jonetsu <= 0`
  - スキル使用不可、回避率0
- `dead`: `(kakkon <= 0 and jonetsu <= 0) or (kakkon <= 0 and anchor_count == 0)`
  - 泥への還り

## Maintenance Levels
- Camp: default=0 , joined_act2=1 , field_lv2_unlocked=2
- Base: default=1 , joined_act2=2 , shrine_lv3_unlocked=3
