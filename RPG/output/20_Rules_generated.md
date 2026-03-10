# Core Rules (Generated)

## Story Flags
- `flag_ukami_joined_early` (UKAMI_JOINED_EARLY): OFF
- `flag_mahito_joined_act2` (MAHITO_JOINED_ACT2): ON
- `flag_white_corridor_cleared` (WHITE_CORRIDOR_CLEARED): OFF
- `flag_mahito_field_lv2_unlocked` (MAHITO_FIELD_LV2_UNLOCKED): OFF
- `flag_shrine_forge_lv3_unlocked` (SHRINE_FORGE_LV3_UNLOCKED): OFF
- `flag_tachibana_joined_act2` (TACHIBANA_JOINED_ACT2): OFF
- `flag_ukami_left_katsuragi` (UKAMI_LEFT_KATSURAGI): OFF
- `flag_wakahiko_antagonist_phase` (WAKAHIKO_ANTAGONIST_PHASE): OFF
- `flag_wakahiko_joined_act3` (WAKAHIKO_JOINED_ACT3): OFF
- `flag_act3_kagaseo_resonance` (ACT3_KAGASEO_RESONANCE): OFF
- `flag_tsukuyomi_tower_deployed` (TSUKUYOMI_TOWER_DEPLOYED): OFF
- `flag_tsukuyomi_fake_lastboss` (TSUKUYOMI_FAKE_LASBOSS): OFF
- `flag_tsukuyomi_celebration_conducted` (TSUKUYOMI_CELEBRATION_CONDUCTED): OFF
- `flag_ukami_returned_yomotsu` (UKAMI_RETURNED_YOMOTSU): OFF
- `flag_kagaseo_reboot_drive_acquired` (KAGASEO_REBOOT_DRIVE_ACQUIRED): OFF
- `flag_ameno_iwatowake_forced_reboot` (AMENO_IWATOWAKE_FORCED_REBOOT): OFF
- `flag_eternity_rejected_death_implemented` (ETERNITY_REJECTED_DEATH_IMPLEMENTED): OFF
- `flag_gyojagaeshi_cleared` (GYOJAGAESHI_CLEARED): OFF
- `flag_susanoo_trial_cleared` (SUSANOO_TRIAL_CLEARED): OFF
- `flag_sterile_curtain_unlocked` (STERILE_CURTAIN_UNLOCKED): OFF
- `flag_blood_mudpit_unlocked` (BLOOD_MUDPIT_UNLOCKED): OFF
- `flag_routeb_choice` (RouteB_Choice): OFF


## Boundary States
- `shigurui`: `kakkon <= 0 and jonetsu > 0`
  - 物理無効、行動ごとに情念を消費
- `karakara`: `kakkon > 0 and jonetsu <= 0`
  - スキル使用不可、回避率0
- `dead`: `(kakkon <= 0 and jonetsu <= 0) or (kakkon <= 0 and anchor_count == 0)`
  - 泥への還り


## Maintenance Levels
- Camp: default=0, joined_act2=1, field_lv2_unlocked=2
- Base: default=1, joined_act2=2, shrine_lv3_unlocked=3