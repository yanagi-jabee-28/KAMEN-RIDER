# DEV-10 Gameplay Logic Formulas and Flags

この文書は一般向け文書から分離した、実装向けロジック正本です。

## 0. 作業目的別インデックス

開発作業の起点として、最短で参照先へ移動するための導線です。

| 作業目的 | まず見る節 | 次に見る節 |
|---|---|---|
| 状態遷移の挙動を確認したい | 1.1 State Transition | 1.6 Field and Curse Logic |
| 耐久・金継ぎの計算を確認したい | 1.2 Durability Model | 1.3 Kintsugi Cycle / 1.4 Core Inheritance |
| キャラ固有ロジックを確認したい | 1.5 Character-Specific Logic | 3.1 / 3.4（うかみ時代差分） |
| クリア後導線や儀式条件を確認したい | 2.4 Gyoja Gaeshi Condition | 2.5 Story_Flag_Definition_Master |
| フラグの副作用・参照元を確認したい | 2.5 Story_Flag_Definition_Master | DEV-11 三点対応表 |

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
// ミコト：実体刀2本同時保持による過熱・耐久消耗・腕摩擦の倍化
IF Character == MIKOTO AND Mikoto_Gauntlet_Permanent == TRUE
 AND Offhand_Weapon_Equipped == TRUE
 AND Trigger_Dual_Stance == TRUE
 AND Can_Unlock_Dual_Stance == TRUE THEN
  DualStanceActive = TRUE
  // 両手に実体刀を同時に保持するため、武器過熱と腕への摩擦が倍になる
  Weapon_Heat_Accumulation_Rate *= 2.0
  Durability_Loss_Rate *= 2.0
  Arm_Friction_Cost *= 2.0
  Stance_Multiplier = 1.3  // 圧力出力増加
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

// ミコト二刀流のナラティブ・ロック
// 序盤は同調補助のため片腕制御系が占有され、継承手甲恒久化後にのみ解放される
IF StoryFlag.UKAMI_LEFT_KATSURAGI == TRUE
 AND Mikoto_Gauntlet_Permanent == TRUE
 AND Sync_Control_Occupied_By_Ukami == FALSE THEN
  Can_Unlock_Dual_Stance = TRUE
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

IF Use_Item == Yomotsu_Mud_Fruit AND Can_Use_Yomotsu_Command == TRUE THEN
  Kakkon_Value = Kakkon_Max
  Jonetsu_Value = Jonetsu_Max
END IF

// 黄泉戸喫の段階解放（遭遇 -> 理解 -> 解放）
IF StoryFlag.YOMOTSU_ENCOUNTERED == TRUE THEN
  Yomotsu_Knowledge_Shown = TRUE
END IF

IF StoryFlag.YOMOTSU_UNDERSTOOD == TRUE THEN
  Yomotsu_Command_Visible = TRUE
END IF

Can_Use_Yomotsu_Command = (
  Yomotsu_Command_Visible == TRUE
  AND Yomotsu_UseWarning_Acknowledged == TRUE
)

IF Use_Item == Yomotsu_Mud_Fruit AND User != UKAMI_GYOJA THEN
  Inventory -= 1
  Apply_State(YOMOTSU_CURSE)
END IF

IF Use_Item == Yomotsu_Mud_Fruit AND User == UKAMI_GYOJA THEN
  Inventory = Inventory
  Skip_State_Inflict(YOMOTSU_CURSE)
END IF

IF StoryFlag.UKAMI_RETURNED_YOMOTSU == TRUE
 AND Ukami_Autonomy == TRUE
 AND Yomotsu_Curse_Pressure >= Ukami_AutoYomotsu_Threshold THEN
  Auto_Consume_Yomotsu_By_Ukami = TRUE
  Inventory = Inventory
  Pause_Yomotsu_Decay_Tick = TRUE
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

### 1.8 Recovery / Daijuku / Phase Priority Notes
```text
// 空殻復帰は自然回復禁止。注入か摩擦熱余波のみ許可
Has_Karakara_Override_Tag = (
  SkillTag.JONETSU_RECOVERY == TRUE
  OR SkillTag.MORALE_BOOST == TRUE
  OR SkillTag.RESTART == TRUE
  OR SkillTag.GEKIYAKU == TRUE
)

Can_Recover_From_Karakara = (
  (Receive_Jonetsu_Injection == TRUE AND Has_Karakara_Override_Tag == TRUE)
  OR Friction_Heat_After_Daijuku >= 1
)

IF State_Karakara == TRUE AND Can_Recover_From_Karakara == TRUE THEN
  Jonetsu_Value = max(1, Jonetsu_Value)
  State_Karakara = FALSE
END IF

// 死狂いは「情念が尽きるまで」の境界状態
IF State_Shigurui == TRUE THEN
  Jonetsu_Value -= Shigurui_Jonetsu_Drain_Per_Action
  IF Jonetsu_Value <= 0 THEN
    State_Dead = TRUE
  END IF
END IF

// 代受苦は通常ガードではなく、武器へ致死因果を肩代わりさせる契約処理
Can_Trigger_Daijuku = (Incoming_Damage >= Fatal_Threshold AND Weapon_Durability > 0)
Can_Trigger_Extreme_Daijuku = (
  Can_Trigger_Daijuku == TRUE
  AND Is_Tsukumogami == TRUE
  AND Is_Destiny_Battle == TRUE
)

IF Can_Trigger_Daijuku == TRUE THEN
  Damage_Redirect_To_Weapon = Incoming_Damage
END IF

// 位相の最小公開値（SYS-20公開整合用）
// STERILE_CURTAIN: Heal_Output_Mult=0.6, SelfCost_Mult=1.25
// BLOOD_MUDPIT: Jonetsu_Gain_Mult=1.2, Recovery_Reversal_Rate=YomotsuRecoveryReversalRate
```

## 2. Story Flags

### 2.1 Story_Flag_Master
- UKAMI_JOINED_EARLY
- MAHITO_JOINED_ACT2
- KAGUTSUCHI_QUELLED
- WHITE_CORRIDOR_CLEARED
- TAKEMIKAZUCHI_REVENGE_CLEARED
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
- YOMOTSU_ENCOUNTERED
- YOMOTSU_UNDERSTOOD

### 2.2 Camp Maintenance Logic
```text
Can_Use_Daijuku = (
  StoryFlag.MAHITO_JOINED_ACT2 == TRUE
)

Can_Use_Mahito_Lv1_Forge = (
  StoryFlag.MAHITO_JOINED_ACT2 == TRUE
)

Can_Use_Forbidden_Forging_Lv2 = (
  StoryFlag.FORBIDDEN_FORGING_LV2_UNLOCKED == TRUE
  AND (CurrentContext == BASE_CAMP OR StoryFlag.TAKEMIKAZUCHI_REVENGE_CLEARED == TRUE)
)

Can_Use_Mahito_Field_Lv2 = (
  Can_Use_Forbidden_Forging_Lv2 == TRUE
  AND StoryFlag.TAKEMIKAZUCHI_REVENGE_CLEARED == TRUE
)

IF Can_Use_Mahito_Field_Lv2 == TRUE THEN
  StoryFlag.MAHITO_FIELD_LV2_UNLOCKED = TRUE
END IF

Can_Use_Tsukumogami_Awakening = (
  Can_Use_Forbidden_Forging_Lv2 == TRUE
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
OnTrigger:
  ShinUtsushi_Slot_Capacity: "+=2"
  FixedInheritedSlotCount: "+=2"
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

### 2.5 Story_Flag_Definition_Master

命名規約・発火条件・副作用・参照元文書を同一フォーマットで管理します。

| Flag_ID | 発火条件（要約） | 主な副作用 | 参照元文書 |
|---|---|---|---|
| `UKAMI_JOINED_EARLY` | 第1幕でうかみ初期加入が成立 | うかみ斥候ロジック有効化 | NAR-10 / SYS-20 |
| `TACHIBANA_JOINED_ACT2_EARLY` | 第2幕序盤で白堊の回廊迂回ルート到達時 | タチバナ加入、流動的逸らし戦術スロット解放 | NAR-10 / SYS-20 |
| `MAHITO_JOINED_ACT2` | 第2幕序盤でマヒト加入（灼熱たたら場） | Lv1鍛造導線の基点解放 | NAR-10 / SYS-20 |
| `FORBIDDEN_FORGING_LV2_UNLOCKED` | 第2幕中盤でカグツチの怨念覚醒時点 | 禁忌鋳造Lv2の初解放（拠点のみ） | NAR-10 / SYS-20 |
| `WHITE_CORRIDOR_CLEARED` | 禁忌Lv2習得後に白堊の回廊を突破 | 第2幕後半導線を開く | NAR-10 |
| `TAKEMIKAZUCHI_REVENGE_CLEARED` | 第3幕後半の雪辱戦を突破 | 野外鍛造Lv2解放条件を満たす | NAR-10 / SYS-20 |
| `MAHITO_FIELD_LV2_UNLOCKED` | `TAKEMIKAZUCHI_REVENGE_CLEARED` が成立 | 野外での禁忌Lv2運用を許可 | SYS-20 / DEV-12 |
| `SHRINE_FORGE_LV3_UNLOCKED` | 拠点鍛造Lv3の条件成立 | 神器級鍛造導線を開放 | SYS-20 / DEV-12 |
| `UKAMI_LEFT_KATSURAGI` | 葛城山離脱イベント発生 | 継承手甲・強制継承スキル発火 | NAR-10 |
| `NAKIME_BATTLE_ACTIVE` | ワカヒコ加入戦の特殊戦闘中 | 返し矢反動ルールを一時変更 | SYS-20 |
| `WAKAHIKO_JOINED_ACT3` | 第3幕でワカヒコ加入 | 弓系高精度妨害ロジック有効化 | NAR-10 / SYS-20 |
| `TSUKUYOMI_FAKE_LASBOSS` | ツクヨミ撃破の節目到達 | 偽終幕後の暗黒導線へ遷移 | NAR-10 |
| `TSUKUYOMI_CELEBRATION_CONDUCTED` | 偽終幕演出を完了 | 祝祭後イベント分岐を確定 | NAR-10 |
| `UKAMI_RETURNED_YOMOTSU` | 行者うかみ帰還成立 | 黄泉・常世で自律介入を有効化 | NAR-10 / SYS-20 |
| `GYOJAGAESHI_CLEARED` | 行者還し三相を完了 | スサノオ試練導線を解放 | NAR-10 / SYS-20 |
| `SUSANOO_TRIAL_UNLOCKED` | 行者還し完了時に付与 | 試練コンテンツ開放 | NAR-10 |
| `AMENO_IWATOWAKE_REBOOT` | 天岩戸再起動の成立 | 天球再駆動系の遷移を確定 | NAR-10 |
| `SUSANOO_TRIAL_CLEARED` | スサノオ試練突破 | 真裏ボス導線を前提化 | NAR-10 |
| `OROCHI_TAIL_BREACHED` | 真裏ボス戦で尾破断発生 | 剣核露出イベント発火 | NAR-10 |
| `ETERNITY_REJECTED` | 終幕で永遠拒絶を選択 | 終幕分岐と後日譚条件を固定 | NAR-10 |
| `AMENO_MURAKUMO_AWAKENED` | 剣核接合イベント完了 | 最終武器覚醒状態へ遷移 | NAR-10 / SYS-30 |

## 3. Ukami Era Data Tables (Moved from SYS-30)

### 3.1 Character_Skill_Base_Master (UKAMI_SCOUT / UKAMI_GYOJA)
うかみを「斥候」「行者」の別キャラとして管理するためのスキル正規化テーブルです。

| Skill_ID | Char_ID | Name | Skill_Type | Cost_Resource | Cost_Amount | Primary_Effect | Use_Case |
|---|---|---|---|---|---|---|---|
| `UKAMI_SCOUT_SKILL_001` | `UKAMI_SCOUT` | 獣の咆哮 | Interrupt | 情念 | 18 | 危険行動中断 | 危険技を止めたい時 |
| `UKAMI_SCOUT_SKILL_002` | `UKAMI_SCOUT` | 牙城割り | Break | 情念 | 22 | 装甲剥離 | 敵が硬い時 |
| `UKAMI_SCOUT_SKILL_003` | `UKAMI_SCOUT` | 法螺の轟き | Support | 情念 | 16 | 情念循環補助 | 連続運用したい時 |
| `UKAMI_SCOUT_SKILL_004` | `UKAMI_SCOUT` | 野性の代受苦 | GuardBurst | 武器耐久 | 100% | 単体肩代わり+反撃起点 | 単体を落としたい時 |
| `UKAMI_SCOUT_SKILL_005` | `UKAMI_SCOUT` | 荒ぶる大旋風 | AoE | 情念 | 28 | 全体圧 | 敵が複数の時 |
| `UKAMI_SCOUT_SKILL_006` | `UKAMI_SCOUT` | 獣道の駆け抜け | Tempo | 情念 | 14 | 自身Tick前倒し | 先に割り込みたい時 |
| `UKAMI_SCOUT_SKILL_007` | `UKAMI_SCOUT` | 捨て身の突進 | Delay | 活魂 | 20 | 大遅延 | 大技前に遅延したい時 |
| `UKAMI_SCOUT_SKILL_008` | `UKAMI_SCOUT` | 導きの泥轍 | Support | 情念 | 20 | 味方行動順補助 | 味方の行動を早めたい時 |
| `UKAMI_SCOUT_SKILL_009` | `UKAMI_SCOUT` | 獣の息継ぎ | SelfRecover | 情念 | 12 | 小回復 | 自己立て直し時 |
| `UKAMI_SCOUT_SKILL_010` | `UKAMI_SCOUT` | 泥玉つぶて | Debuff | 情念 | 10 | 命中低下 | 命中を落としたい時 |
| `UKAMI_GYOJA_SKILL_001` | `UKAMI_GYOJA` | 行者の割込護り | Rescue | 情念 | 24 | 割込救助 | 戦闘不能が出そうな時 |
| `UKAMI_GYOJA_SKILL_002` | `UKAMI_GYOJA` | 泥祓いの祈祷 | Cleanse | 情念 | 20 | 呪い解除補助 | 黄泉の呪いが重い時 |
| `UKAMI_GYOJA_SKILL_003` | `UKAMI_GYOJA` | 黄泉戸喫・反転 | Sustain | 情念 | 26 | 回復反転貫通 | 回復反転を越えたい時 |
| `UKAMI_GYOJA_SKILL_004` | `UKAMI_GYOJA` | 帰還の法螺 | Support | 情念 | 18 | 再行動補助 | 立て直し局面 |
| `UKAMI_GYOJA_SKILL_005` | `UKAMI_GYOJA` | 逆巻く錫杖 | Interrupt | 情念 | 22 | 停止+受け | 危険行動を止めたい時 |
| `UKAMI_GYOJA_SKILL_006` | `UKAMI_GYOJA` | 根の境界踏破 | Tempo | 情念 | 16 | Tick再調整 | 行動順を取り戻したい時 |
| `UKAMI_GYOJA_SKILL_007` | `UKAMI_GYOJA` | 行者還し・脈継ぎ | Ritual | 情念 | 30 | 儀式進行補助 | 儀式系の山場 |
| `UKAMI_GYOJA_SKILL_008` | `UKAMI_GYOJA` | 常世の導き縄 | Guard | 情念 | 20 | ヘイト安定化 | 事故を減らしたい時 |
| `UKAMI_GYOJA_SKILL_009` | `UKAMI_GYOJA` | 黄泉の息継ぎ | SelfRecover | 情念 | 14 | 小回復+安定化 | 長期戦の維持 |
| `UKAMI_GYOJA_SKILL_010` | `UKAMI_GYOJA` | 土還りの終止符 | Finisher | 情念 | 32 | 収束打点 | 終盤の押し切り |

### 3.2 Character_Stat_Curve_Master (UKAMI_SCOUT / UKAMI_GYOJA)
斥候期と行者期を別キャラとして管理する成長帯テーブルです。

| Stat_Curve_ID | Char_ID | Growth_Phase | Kakkon | Jonetsu | Main_Role | Unlock_Notes |
|---|---|---|---|---|---|---|
| `UKAMI_SCOUT_GROWTH_01` | `UKAMI_SCOUT` | 序盤（第1-2幕） | 200-240 | 80-95 | 壁/受け | 獣の咆哮、牙城割り、法螺の轟き |
| `UKAMI_SCOUT_GROWTH_02` | `UKAMI_SCOUT` | 中盤（第3幕） | 241-290 | 96-115 | 壁/受け+支援 | 導きの泥轍、捨て身の突進 |
| `UKAMI_GYOJA_GROWTH_01` | `UKAMI_GYOJA` | 帰還直後（第4幕） | 230-280 | 120-150 | 自律介入/救助 | 行者の割込護り、泥祓いの祈祷 |
| `UKAMI_GYOJA_GROWTH_02` | `UKAMI_GYOJA` | 終盤（第4幕-終幕） | 281-340 | 151-190 | 儀式維持/収束 | 行者還し・脈継ぎ、土還りの終止符 |

### 3.3 Character_Interaction_Master (UKAMI_SCOUT / UKAMI_GYOJA)
うかみの時代差を反映した特殊相互作用テーブルです。

| Interaction_ID | Char_ID | Trigger | Condition | Result | Note |
|---|---|---|---|---|---|
| `UKAMI_SCOUT_INTERACT_001` | `UKAMI_SCOUT` | 地上通常戦 | 第1-3幕 | ヘイト集約と受け運用が主軸 | 斥候期の標準挙動 |
| `UKAMI_GYOJA_INTERACT_001` | `UKAMI_GYOJA` | 黄泉の泥果実使用 | User == UKAMI_GYOJA | 呪い付与をスキップ | プレイヤー在庫を消費しない処理と整合 |
| `UKAMI_GYOJA_INTERACT_002` | `UKAMI_GYOJA` | キャンプ祈祷（泥祓い） | UKAMI_GYOJA同行または在営 | 黄泉の呪い解除 | 通常回復無効の解除点 |
| `UKAMI_GYOJA_INTERACT_003` | `UKAMI_GYOJA` | 行者還し儀式 | Story節目到達 | 試練導線の解放へ寄与 | 進行節目の再接続役 |

### 3.4 AI_Behavior_Master (UKAMI_GYOJA)
行者うかみの自律介入を、優先度付きで確認するためのテーブルです。

| Behavior_ID | Char_ID | Active_Condition | Priority | Behavior | Resource_Usage | Area_Limit |
|---|---|---|---|---|---|---|
| `UKAMI_GYOJA_AI_001` | `UKAMI_GYOJA` | `UKAMI_RETURNED_YOMOTSU == TRUE` | 1 | 戦闘不能回避の割り込み救助 | 共有リソース非消費 | 黄泉比良坂/黄泉/常世 |
| `UKAMI_GYOJA_AI_002` | `UKAMI_GYOJA` | 同上 | 2 | 黄泉呪い関連の解除支援 | 共有リソース非消費 | 黄泉比良坂/黄泉/常世 |
| `UKAMI_GYOJA_AI_003` | `UKAMI_GYOJA` | 同上 | 3 | ヘイト集約と被弾吸収 | 共有リソース非消費 | 黄泉比良坂/黄泉/常世 |
| `UKAMI_GYOJA_AI_004` | `UKAMI_GYOJA` | 同上 | 4 | 行動順補助（泥轍系） | 共有リソース非消費 | 黄泉比良坂/黄泉/常世 |
