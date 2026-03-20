# DEV-10 Gameplay Logic Formulas and Flags

この文書は一般向け文書から分離した、実装向けロジック正本です。

## Source Scope
- Moved from: `02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md`
- Moved from: `01_Story_and_Characters/NAR-10_Narrative_and_Characters.md` (実装フラグ対応表)

## 1. Core Logic Formulas

### 1.1 State Transition
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

### 1.2 Durability Model
```text
Durability_new = max(0, Durability_old - (
    Base_Weapon_DurabilityCost * Stance_Multiplier
  + Combo_DurabilityCost
  + Skill_DurabilityCost
  + Intentional_Cost
))
```

### 1.3 Kintsugi Cycle
```text
Can_Use_Daijuku = (Weapon_Durability > 0)

IF Incoming_Damage >= Fatal_Threshold AND Can_Use_Daijuku THEN
  Weapon_Durability = max(0, Weapon_Durability - Daijuku_Durability_Cost)
  Incoming_Damage = 0
END IF

IF Is_Tsukumogami == TRUE AND Is_Destiny_Battle == TRUE AND Use_Extreme_Daijuku == TRUE THEN
  Weapon_Destroyed = TRUE
  Generate_Core_of_Regret = TRUE
END IF
```

### 1.4 Core Inheritance
```text
IF Global_Kintsugi_Count >= Tsukumogami_Awake_Threshold
 AND Cumulative_Durability_Hours >= Tsukumogami_Hours_Threshold THEN
  Is_Tsukumogami = TRUE
  Has_Tsukumogami_Persona = TRUE
END IF

IF Weapon_Destroyed == TRUE AND Is_Tsukumogami == TRUE THEN
  Core_of_Regret.Created = TRUE
  Core_of_Regret.Stored_Traits = Weapon.Stored_Traits
END IF

IF Core_of_Regret.Created == TRUE AND Kintsugi_Transfer_Executed == TRUE THEN
  Next_Weapon.Stored_Traits += Core_of_Regret.Stored_Traits * Core_of_RegretCarryRate
  Core_of_Regret.Consumed = TRUE
END IF
```

### 1.5 Character-Specific Logic
```text
IF Character == MIKOTO AND Mikoto_Gauntlet_Permanent == TRUE
 AND Offhand_Weapon_Equipped == TRUE AND Trigger_Dual_Stance == TRUE THEN
  DualStanceActive = TRUE
  Stance_Multiplier = 1.3
END IF

IF Character == WAKAHIKO AND MainWeapon_Category == BOW_RANGED THEN
  Jonetsu_Ratio = clamp(Consumed_Jonetsu_For_Attack / Jonetsu_Max, 0.0, 1.0)
  Damage_Mult = 1.0 + (Jonetsu_Ratio * WAKAHIKO_KAESHIYA_Damage_Mult)
  Recoil_Damage = floor(Bow_Base_Damage * Jonetsu_Ratio * WAKAHIKO_KAESHIYA_Recoil_Mult)
  IF StoryFlag.NAKIME_BATTLE_ACTIVE == TRUE THEN
    Recoil_Damage = 0
  END IF
  IF State_Inga_No_Kaeshiya == TRUE THEN
    Transfer_Damage = floor(Recoil_Damage * 0.5)
    Recoil_Damage = Recoil_Damage - Transfer_Damage
    Apply_Noise_Damage(Target, Transfer_Damage)
  END IF
END IF

IF StoryFlag.UKAMI_RETURNED_YOMOTSU == TRUE
 AND Battle_Location IN [YOMOTSU_HIRASAKA, YOMI_NO_KUNI, TOKOYO] THEN
  Ukami_Autonomy = TRUE
  Ukami_Uses_Party_Resource = FALSE
  Ukami_AutoIntercept = TRUE
END IF
```

### 1.6 Field and Curse Logic
```text
IF Field_State == STERILE_CURTAIN THEN
  Heal_Output_Mult = 0.6
  SelfCost_Mult = 1.25
END IF

IF Field_State == BLOOD_MUDPIT THEN
  Recovery_Reversal_Rate = YomotsuRecoveryReversalRate
  Jonetsu_Gain_Mult = 1.2
END IF

IF Item_Used == Yomotsu_Mud_Fruit AND User != UKAMI_GYOJA THEN
  Inventory -= 1
  Apply_State(YOMOTSU_CURSE)
END IF

IF Item_Used == Yomotsu_Mud_Fruit AND User == UKAMI_GYOJA THEN
  Inventory = Inventory
  Skip_State_Inflict(YOMOTSU_CURSE)
END IF

IF Use_Item == Yomotsu_Mud_Fruit THEN
  Kakkon_Value = Kakkon_Max
  Jonetsu_Value = Jonetsu_Max
  Apply_State(YOMOTSU_CURSE)
END IF

IF State_Yomotsu_Curse == TRUE THEN
  MaxKakkon = max(Min_MaxKakkon_Floor, floor(MaxKakkon * Yomotsu_MaxKakkon_Decay_Mult))
  Disable_Standard_Recovery = TRUE
END IF
```

### 1.7 Special Enemy / Learning AI
```text
IF Enemy_ID == Hakuraku_Stardust THEN
  Escape_Check = (Current_Tick >= Hakuraku_Return_Gravity_Tick)
  IF Escape_Check THEN
    Hakuraku_Despawn_Window -= 1
  END IF
  IF Hakuraku_Despawn_Window <= 0 THEN
    Enemy_Despawn = TRUE
  END IF
END IF

Ri_Level_1_Static = Uses(Current_Stats_Only)
Ri_Level_2_Adaptive = Uses(Current_Stats_And_History)
Ri_Level_25_Psychological = Uses(Pattern_Penalty)
Ri_Level_3_Absolute = Uses(Noise_Resistance_High)
```

## 2. Story Flags

### 2.1 Story_Flag_Master
- UKAMI_JOINED_EARLY
- MAHITO_JOINED_ACT2
- KAGUTSUCHI_QUELLED
- WHITE_CORRIDOR_CLEARED
- MAHITO_FIELD_LV2_UNLOCKED
- SHRINE_FORGE_LV3_UNLOCKED
- UKAMI_LEFT_KATSURAGI
- NAKIME_BATTLE_ACTIVE
- WAKAHIKO_JOINED_ACT3
- TSUKUYOMI_FAKE_LASBOSS
- TSUKUYOMI_CELEBRATION_CONDUCTED
- UKAMI_RETURNED_YOMOTSU
- GYOJAGAESHI_CLEARED
- SUSANOO_TRIAL_UNLOCKED
- AMENO_IWATOWAKE_REBOOT
- SUSANOO_TRIAL_CLEARED
- OROCHI_TAIL_BREACHED
- ETERNITY_REJECTED
- AMENO_MURAKUMO_AWAKENED

### 2.2 Camp Maintenance Logic
```text
Can_Use_Daijuku = (
  StoryFlag.MAHITO_JOINED_ACT2 == TRUE
)

Can_Use_Tsukumogami_Awakening = (
  StoryFlag.MAHITO_JOINED_ACT2 == TRUE
  AND StoryFlag.KAGUTSUCHI_QUELLED == TRUE
  AND (CurrentContext == BASE_CAMP OR StoryFlag.MAHITO_FIELD_LV2_UNLOCKED == TRUE)
)

Can_Use_Extreme_Daijuku = (
  Can_Use_Tsukumogami_Awakening == TRUE
  AND Is_Tsukumogami == TRUE
)
```

### 2.3 Forced Inheritance
```yaml
TriggerFlag: UKAMI_LEFT_KATSURAGI
TargetCharacter: MIKOTO
ForcedSkills:
  - SkillId: INHERITED_SARUTA_BREAK
    Name: 猿田の破岩撃 (剛)
  - SkillId: INHERITED_HORAGAI_ROAR
    Name: 法螺の轟き (導)
```

### 2.4 Gyoja Gaeshi Condition
```text
IF StoryFlag.TSUKUYOMI_FAKE_LASBOSS == TRUE
 AND StoryFlag.UKAMI_RETURNED_YOMOTSU == TRUE
 AND (Sum(Party.MaxKakkon) >= Required_Kakkon_Gravity)
 AND (Sum(Party.MaxJonetsu) >= Required_Jonetsu_Gravity) THEN
  Allow_Gyojagaeshi_Ritual = TRUE
END IF

IF Allow_Gyojagaeshi_Ritual == TRUE
 AND Ritual_Phase_1_Completed == TRUE
 AND Ritual_Phase_2_Completed == TRUE
 AND Ritual_Phase_3_Completed == TRUE THEN
  StoryFlag.GYOJAGAESHI_CLEARED = TRUE
  StoryFlag.SUSANOO_TRIAL_UNLOCKED = TRUE
END IF
```
