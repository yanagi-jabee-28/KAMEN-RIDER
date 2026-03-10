# RPG企画5 - 30 Data and Logic Architecture (データと論理)

本ドキュメントはRPG企画5の**唯一の実装正本（SSOT）**である。変数、計算式、フラグ、閾値の追加変更は必ず本書で行う。

## 0. アンカーマップ [#ID:R5_Anchor_Map]
- `[#ID:R5_Resource_Core]`: 三条熱源の定義
- `[#ID:R5_Boundary_States]`: 境界状態判定
- `[#ID:R5_Durability_Model]`: 武器耐久度モデル
- `[#ID:R5_Resonance_Burst]`: 共鳴過熱の処理
- `[#ID:R5_Field_Rules]`: 場ルール（無菌の帳/血の泥沼）
- `[#ID:R5_Story_Flag_Master]`: 進行フラグ
- `[#ID:R5_Maintenance_Tiers]`: 鍛造段階解放
- `[#ID:R5_Forbidden_Terms_Guard]`: 禁止語ガード

## 1. 三条熱源定義 [#ID:R5_Resource_Core]
| リソース | 変数名 | 型 | 範囲 | 説明 |
| --- | --- | --- | --- | --- |
| 活魂 | `Kakkon_Value` | int | 0..`Kakkon_Max` | 肉体生命と持久力 |
| 情念 | `Jonetsu_Value` | int | 0..`Jonetsu_Max` | 執念と未練の燃料 |
| 武器耐久度 | `Weapon_Durability` | int | 0..`Durability_Max` | 摩擦・熱・劣化を集約 |

### 1.1 情念増減
```text
Jonetsu_Gain = floor(Damage_Taken * Char_Factor) + floor(Ally_Crisis * Sync_Factor)
Jonetsu_Value = min(Jonetsu_Max, Jonetsu_Value + Jonetsu_Gain)

Jonetsu_Value = max(0, Jonetsu_Value - Skill_Cost)
```

## 2. 境界状態 [#ID:R5_Boundary_States]
```text
IF Kakkon_Value <= 0 AND Jonetsu_Value > 0 THEN
  State_Shigurui = TRUE
END IF

IF Kakkon_Value > 0 AND Jonetsu_Value <= 0 THEN
  State_Karakara = TRUE
END IF

IF Kakkon_Value <= 0 AND Jonetsu_Value <= 0 THEN
  State_Dead = TRUE
END IF
```

- `State_Shigurui`: 被物理ダメージ軽減 + 行動短期加速。
- `State_Karakara`: 特技封鎖 + 被弾クリティカル率増。
- `State_Dead`: 戦闘不能。

## 3. 武器耐久度モデル [#ID:R5_Durability_Model]
```text
Durability_Cost = Base_Durability_Cost + Skill_Durability_Cost + Intentional_Cost
Weapon_Durability = max(0, Weapon_Durability - floor(Durability_Cost * Stance_Multiplier))
```

- `Stance_Multiplier`
1. 訓練者の副腕併用: `1.0`
2. 非訓練者の副腕併用: `1.2`
3. 付喪神化武器: 追加で `Tsukumogami_Penalty(1.5..3.0)` を乗算

## 4. 共鳴過熱（新ゲージ非採用） [#ID:R5_Resonance_Burst]
```text
Can_Trigger_ResonanceBurst = (Jonetsu_Value >= Burst_Jonetsu_Min) AND (Weapon_Durability > 0)

IF Can_Trigger_ResonanceBurst THEN
  Jonetsu_Value = max(0, Jonetsu_Value - Burst_Jonetsu_Cost)
  Weapon_Durability = 0
  Damage_Mult = 1.0 + Burst_Damage_Bonus
  State_SearedSilence = TRUE
END IF
```

## 5. 場ルール [#ID:R5_Field_Rules]
```text
IF Field_State == STERILE_CURTAIN THEN
  Heal_Value = floor(Heal_Value * Sterile_Heal_Mult)
  Jonetsu_Skill_Seal = TRUE
END IF

IF Field_State == BLOOD_MUDPIT THEN
  Heal_Value = floor(Heal_Value * Blood_Heal_Mult)
  Jonetsu_Gain = floor(Jonetsu_Gain * Blood_Jonetsu_Gain_Mult)
  Durability_Cost = floor(Durability_Cost * Blood_Durability_Cost_Mult)
END IF
```

## 6. 進行フラグマスター [#ID:R5_Story_Flag_Master]
| フラグ | 型 | 意味 |
| --- | --- | --- |
| `MAHITO_JOINED_ACT2` | bool | マヒト加入 |
| `MAHITO_FIELD_LV2_UNLOCKED` | bool | 野外Lv2鍛造解禁 |
| `SHRINE_FORGE_LV3_UNLOCKED` | bool | 大型神社Lv3鍛造解禁 |
| `IS_DESTINY_BATTLE` | bool | 極大代受苦許可戦闘 |
| `ACT_INDEX` | int | 現在幕（1..5） |

## 7. 鍛造段階解放 [#ID:R5_Maintenance_Tiers]
```text
Camp_Level = 0
IF MAHITO_JOINED_ACT2 THEN Camp_Level = 1 END IF
IF MAHITO_FIELD_LV2_UNLOCKED THEN Camp_Level = 2 END IF

Base_Level = 1
IF MAHITO_JOINED_ACT2 THEN Base_Level = 2 END IF
IF SHRINE_FORGE_LV3_UNLOCKED THEN Base_Level = 3 END IF

Can_Use_Kintsugi = (Current_Location_Level >= 1)
Can_Use_Tsukumogami_Awakening = (Current_Location_Level >= 2)
Can_Use_Mythic_Forging = (Current_Location_Level >= 3) AND (ACT_INDEX >= 4)
Can_Use_Extreme_Daijuku = IS_DESTINY_BATTLE AND Can_Use_Tsukumogami_Awakening
```

## 8. 付喪神継承 [#ID:R5_Tsukumogami_Inheritance]
```text
IF Can_Use_Extreme_Daijuku THEN
  Delete_Weapon_Instance = TRUE
  Generate_Core_of_Regret = TRUE
END IF

Can_Inherit = Can_Use_Tsukumogami_Awakening
  AND Core_of_Regret_Exists
  AND (Base_Weapon_ID != Core_Source_Weapon_ID)
```

## 9. 禁止語ガード [#ID:R5_Forbidden_Terms_Guard]
以下の語彙は実装語として使用禁止。検出時は翻訳語へ置換する。
- 直輸入禁止語: `metal slime`, `seal skill`, `tension`, `reflect`
- SF語禁止: `nanomachine`, `AI`, `supernova remnant`, `short circuit`

推奨翻訳語:
- `剥落の星屑`
- `凍結の真空`
- `共鳴過熱`
- `理の反射鏡`

## 10. 参照規約
30以外のファイルは本書アンカーを参照し、詳細の複写を禁止する。