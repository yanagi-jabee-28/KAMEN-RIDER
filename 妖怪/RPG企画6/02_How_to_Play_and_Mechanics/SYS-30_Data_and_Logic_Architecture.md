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

## 情念回復ロジック（詳細）

```text
Jonetsu_recover_just = floor(Base_Just_Reward * Just_Action_Multiplier)
Jonetsu_recover_chain = floor(Base_Chain_Reward * Chain_Multiplier)
Jonetsu_recover_breath = floor(Jonetsu_Max * Breathing_Percent)  # 0.3-0.5

Jonetsu_new = min(
  Jonetsu_Max,
  Jonetsu_old + Jonetsu_recover_just + Jonetsu_recover_chain + Jonetsu_recover_breath
)
```

## 神写しコスト補正

```text
Cost = Base_Cost * (skill_owner == "Ukami" && Ukami_Gauntlet ? 1.0 : Cost_Mult)
Cost_Mult = 1.5-2.0  # 他キャラ技は重くする
```

## 構えと自動切替（詳細）

```text
IF Skill_Selected.Required_Weapon_Category != NONE
  AND MainWeapon.Category != Skill_Selected.Required_Weapon_Category THEN
  Auto_Swap_Candidate = Character.Inventory.Find(Skill_Selected.Required_Weapon_Category)
  IF Auto_Swap_Candidate.Found == TRUE THEN
    MainWeapon = Auto_Swap_Candidate
    DynamicStanceOverride = TRUE
    DynamicStance_Until_Tick = Current_Tick + 1
  END IF
END IF

IF DynamicStanceOverride == TRUE AND Current_Tick > DynamicStance_Until_Tick THEN
  RestoreWeapon_To_PreSwap()
  DynamicStanceOverride = FALSE
END IF
```

## 返し矢の呪い（ワカヒコ）

```text
IF Character == WAKAHIKO AND MainWeapon.Category == "BOW_RANGED" THEN
  Jonetsu_Consumption_Ratio = clamp(Consumed_Jonetsu_For_Attack / Jonetsu_Max, 0.0, 1.0)
  Bow_Damage_Mult = 1.0 + (Jonetsu_Consumption_Ratio * WAKAHIKO_KAESHIYA_Damage_Mult)
  Self_Recoil_Damage = floor(Bow_Base_Damage * Jonetsu_Consumption_Ratio * WAKAHIKO_KAESHIYA_Recoil_Mult)

  IF State_Inga_No_Kaeshiya == TRUE THEN
    Transfer_Damage = floor(Self_Recoil_Damage * 0.5)
    Self_Recoil_Damage = Self_Recoil_Damage - Transfer_Damage
    Apply_Noise_Damage(Target, Transfer_Damage)
  END IF

  Apply_Damage(Target, floor(Bow_Base_Damage * Bow_Damage_Mult))
  Kakkon_Value = max(0, Kakkon_Value - Self_Recoil_Damage)
END IF
```

## 代受苦・極大代受苦（詳細）

```text
Can_Use_Daijuku = (Weapon_Durability > 0) AND (Weapon_Usable == TRUE)

IF Can_Use_Daijuku THEN
  Weapon_Durability = 0
  Weapon_Usable = FALSE
  Apply_Damage(Target, Daijuku_Damage)
END IF

IF Can_Use_Extreme_Daijuku AND Target_Weapon.Is_Tsukumogami == TRUE THEN
  Item_Instance = DELETE_PERMANENTLY
  Generate(Core_of_Regret, Rate=1.0)
END IF
```

## 付喪神化・継承鍛造

```text
Tsukumogami_Awakening_Forge =
  Can_Use_Tsukumogami_Awakening
  AND Kintsugi_LogDensity >= TsukumogamiAwakeThreshold
  AND Kintsugi_Material_StarSand_Count >= Required_StarSand_Count

IF Tsukumogami_Awakening_Forge THEN
  Target_Weapon.Is_Tsukumogami = TRUE
  Target_Weapon.TsukumogamiState = "Musubi"
  Target_Weapon.CoreRegret_Extractable = TRUE
END IF

Tsukumogami_Inheritance_Forge =
  Can_Use_Tsukumogami_Awakening
  AND Item(Core_of_Regret).Exists
  AND Base_Weapon_ID != Core_of_Regret.Source_Weapon_ID
```

## 黄泉戸喫・黄泉の呪い

```text
IF Use_Item == Yomotsu_Mud_Fruit THEN
  Kakkon_Value = Kakkon_Max
  Jonetsu_Value = Jonetsu_Max
  Apply_State(YOMOTSU_CURSE)
END IF

IF State_Yomotsu_Curse == TRUE THEN
  MaxKakkon = max(Min_MaxKakkon_Floor, floor(MaxKakkon * Yomotsu_MaxKakkon_Decay_Mult))
  Disable_Standard_Recovery = TRUE
END IF

IF CurrentContext == CAMP_MENU
  AND Command == "Gyoja_Kito_Dobarai"
  AND (Ukami_In_Party == TRUE OR Ukami_In_Camp == TRUE) THEN
  Remove_State(YOMOTSU_CURSE)
  Disable_Standard_Recovery = FALSE
END IF
```

## 領域位相の補正

```text
IF Field_State == STERILE_CURTAIN THEN
  Heal_Value = floor(Heal_Value * Sterile_Heal_Mult)
  SelfHurt_Cost = floor(SelfHurt_Cost * Sterile_SelfHurt_Mult)
END IF

IF Field_State == BLOOD_MUDPIT THEN
  Heal_Value = floor(Heal_Value * Blood_Heal_Mult)
  Jonetsu_Gain = floor(Jonetsu_Gain * Blood_Jonetsu_Gain_Mult)
  Durability_Cost = floor(Durability_Cost * Blood_Durability_Cost_Mult)
END IF
```

## Story_Flag補足

- `KAGUTSUCHI_QUELLED`: 灼熱たたら場の鎮魂完了。
- `NAKIME_DEFEATED_ACT3`: ナキメ戦終了。
- `WAKAHIKO_KAESHIYA_AWAKENED`: 返し矢常時化。
- `KAGASEO_REBOOT_DRIVE_ACQUIRED`: 星屑の荒野で駆動片取得。
- `AMENO_MURAKUMO_AWAKENED`: オロチ尾剣核を現行武器へ接合。

## マスターデータ運用（実装チーム向け）

最低限、次のテーブルをSSOTとして維持する。

- `Equipment_Slot_Master`
- `Character_Equipment_Master`
- `Weapon_Category_Master`
- `Status_Effect_Master`
- `Enemy_Tier_Template_Master`
- `Forge_Access_Rule_Master`
- `Maintenance_Level_Master`
- `Story_Flag_Master`

注: スキル説明文側で数値を持たず、必ず本ファイルで一元管理する。

## スキル実装マスター（RPG5移植・Wave2）

初心者向けの簡潔な導線は `SYS-22` を正とし、ここでは実装側で保持すべき具体技を列挙する。

### ミコト（可変ハブ）

| スキルID候補 | 技名 | 実装メモ |
|---|---|---|
| `SKL_MIKOTO_KOTOTSUGI` | 言継ぎ | 神写し理解度上昇。次の神写し行動へボーナス付与。 |
| `SKL_MIKOTO_MIKENURI` | 泥繭の眠り | Tick継続回復。被弾で中断。 |
| `SKL_MIKOTO_KANRYU` | 命の還流 | 活魂コストで空殻復帰。 |
| `SKL_MIKOTO_DAIJUKEI` | 代受の誓い | 味方被ダメ肩代わり+情念変換。 |
| `SKL_MIKOTO_HAGAN` | 猿田の破岩撃 | 固定継承枠。活魂/情念消費の高火力。 |
| `SKL_MIKOTO_EIEN_KYOHI` | 永遠の拒絶 | 停止系状態異常の無効化。 |

### うかみ（壁・受け）

| スキルID候補 | 技名 | 実装メモ |
|---|---|---|
| `SKL_UKAMI_HORA` | 法螺の轟き | 味方全体の情念上昇率バフ。 |
| `SKL_UKAMI_KINGA` | 牙城割り | 敵装甲(PTG)を継続低下。 |
| `SKL_UKAMI_HOERU` | 獣の咆哮 | 危険行動の中断用スタン。 |
| `SKL_UKAMI_DOROWADACHI` | 導きの泥轍 | 味方1人の行動順前倒し。 |
| `SKL_UKAMI_DAIJUKU` | 野性の代受苦 | 耐久全消費の単発高火力。 |

### スクナ（剥離・制御）

| スキルID候補 | 技名 | 実装メモ |
|---|---|---|
| `SKL_SUKUNA_KYOUSAN` | 強酸の霧散 | PTG無視ダメージ。 |
| `SKL_SUKUNA_FORGET` | 忘却の霧 | 予告行動封印。 |
| `SKL_SUKUNA_COOL_DOSE` | 冷却の服用 | 回復+過熱段階を1戻す。 |
| `SKL_SUKUNA_COOL_THROW` | 冷却の投擲 | `ICE_COOLING` 付与。澱神/棄物へ追加脆化。 |
| `SKL_SUKUNA_STAR_EAT` | 理の簒奪（星喰い） | 敵情念の吸収変換。 |

### ウズ（攪乱）

| スキルID候補 | 技名 | 実装メモ |
|---|---|---|
| `SKL_UZU_RANCHO` | 乱調の裏拍 | 敵全体Tickを後退。 |
| `SKL_UZU_KYORAN` | 狂乱の裏拍 | Tick順ランダムシャッフル。 |
| `SKL_UZU_GENWAKU` | 幻惑の舞 | 着弾予測ズレ+命中低下。 |
| `SKL_UZU_KYOSOU_GRAV` | 狂騒の引力 | 敵リソース吸収→味方情念化。 |
| `SKL_UZU_FINALE` | 狂信のフィナーレ | 武器過熱(耐久0)と引き換えに行動強制不発。 |

### タチバナ（自傷デバフ）

| スキルID候補 | 技名 | 実装メモ |
|---|---|---|
| `SKL_TACHIBANA_HIAI` | 悲哀の波紋 | 全体ステータス低下。 |
| `SKL_TACHIBANA_DOGU` | 自傷・土偶 | 活魂消費の全体土属性+継続ダメージ+予測攪乱。 |
| `SKL_TACHIBANA_CHISHIO` | 執着の血潮 | 味方活魂共有による被害分散。 |
| `SKL_TACHIBANA_IKENIE` | 生贄の祈り | 活魂コストの確実蘇生。 |
| `SKL_TACHIBANA_SHUSHU` | 執着の修復 | 活魂コストの自己回復。 |

### マヒト（鍛造・粉砕）

| スキルID候補 | 技名 | 実装メモ |
|---|---|---|
| `SKL_MAHITO_BUKI_BREAK` | 武具叩き折り | 敵武器耐久をレッドゾーンへ。 |
| `SKL_MAHITO_HAMMER_ROAR` | 槌の轟き | 敵バフ強制リセット。 |
| `SKL_MAHITO_KINTSUGI_LIFE` | 命の金継ぎ | 活魂コストで単体大回復。 |
| `SKL_MAHITO_FOOTH_BLOW` | 鞴の大風 | 味方全体の属性被ダメ軽減。 |
| `SKL_MAHITO_ICE_SLAG` | 炉滓の氷噴 | `ICE_COOLING` 付与と追加脆化。 |

### ワカヒコ（停止・狙撃）

| スキルID候補 | 技名 | 実装メモ |
|---|---|---|
| `SKL_WAKAHIKO_SENKAKE` | 先駆けの矢 | 予告前先制。 |
| `SKL_WAKAHIKO_SHADOW_BIND` | 影縫いの刃 | 行動足止め。 |
| `SKL_WAKAHIKO_KAESHIYA` | 返し矢の呪い | 消費リソース比例の威力増+反動。 |
| `SKL_WAKAHIKO_INGA` | 因果の返し矢 | 反動の一部を敵側ノイズへ転写。 |
| `SKL_WAKAHIKO_SURVIVE` | 生存の足掻き | 条件成立時100%反撃。 |

### 運用ルール

- `SYS-22` に載せるのは各キャラ3-5技まで。ここにない値を `SYS-22` へ再記載しない。
- 物語イベントで強制解禁される技は `Story_Flag_Master` と同時に更新する。
- 返し矢系、土偶系、過熱系は必ず「コスト」「反動」「解除条件」を同一行で管理する。
