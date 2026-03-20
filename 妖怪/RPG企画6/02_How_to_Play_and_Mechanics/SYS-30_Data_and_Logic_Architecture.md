---
uid: [SYS-30]
project_code: RPG企画6
title: Data and Logic Architecture
role: data-and-logic
status: active
owner: Architecture Guardian
depends_on:
  - SYS-20_Player_Manual.md
  - ../00_Welcome_and_Introduction/README.md
  - ../90_For_Developers/ARC-00_Architecture_and_Governance.md
influences:
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../99_Archive_and_References/REF-00_References_and_Archive.md
---

# [SYS-30] Data and Logic Architecture

> ※このファイルはゲーム内部の計算式・フラグ・マスターデータを記載する開発者向け正本です。遊び方を知りたい読者は [SYS-20_Player_Manual.md](SYS-20_Player_Manual.md) を参照してください。

## 1. コア数理モデル（Logic Architecture）

### 1.1 三条の熱源（実装定義）
- `Kakkon_Value`: 活魂（器）。キャラクターの基礎HP。
- `Jonetsu_Value`: 情念（熱）。スキル使用・同調の燃料。
- `Weapon_Durability`: 武器耐久度（摩耗）。0で破損状態へ遷移。

### 1.2 境界状態判定（State Transition）
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

### 1.3 武器耐久度モデル（Durability Calculation）
```text
Durability_new = max(0, Durability_old - (
    Base_Weapon_DurabilityCost * Stance_Multiplier
  + Combo_DurabilityCost
  + Skill_DurabilityCost
  + Intentional_Cost
))
```
- `Stance_Multiplier`:
  - 両手持ち (2H): `1.5`
  - 一刀流 (1H): `1.0`
  - 二刀流 (Dual): `1.3`

### 1.4 修復と鍛造の循環（Kintsugi Cycle）
```text
Can_Use_Daijuku = (Weapon_Durability > 0)

IF Incoming_Damage >= Fatal_Threshold AND Can_Use_Daijuku THEN
  // 代受苦: 武器が致命傷を肩代わり
  Weapon_Durability = max(0, Weapon_Durability - Daijuku_Durability_Cost)
  Incoming_Damage = 0
END IF

IF Is_Tsukumogami == TRUE AND Is_Destiny_Battle == TRUE AND Use_Extreme_Daijuku == TRUE THEN
  // 極大代受苦: 付喪神化武器を完全ロストして因果を切断
  Weapon_Destroyed = TRUE
  Generate_Core_of_Regret = TRUE
END IF
```
- この式が意図する体験: 「守るために壊す」選択が、次の世代の武器強化へつながる。

### 1.5 付喪神化と情念の核継承
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
- この式が意図する体験: ロストは罰ではなく「履歴の再配線」。喪失が無駄にならない。

### 1.6 固有戦術ロジック（ミコト/ワカヒコ/うかみ）
```text
// ミコト: 仮想二刀流
IF Character == MIKOTO AND Mikoto_Gauntlet_Permanent == TRUE
 AND Offhand_Weapon_Equipped == TRUE AND Trigger_Dual_Stance == TRUE THEN
  DualStanceActive = TRUE
  Stance_Multiplier = 1.3
END IF

// ワカヒコ: 返し矢の呪い / 因果の返し矢
IF Character == WAKAHIKO AND MainWeapon_Category == BOW_RANGED THEN
  Jonetsu_Ratio = clamp(Consumed_Jonetsu_For_Attack / Jonetsu_Max, 0.0, 1.0)
  Damage_Mult = 1.0 + (Jonetsu_Ratio * WAKAHIKO_KAESHIYA_Damage_Mult)
  Recoil_Damage = floor(Bow_Base_Damage * Jonetsu_Ratio * WAKAHIKO_KAESHIYA_Recoil_Mult)
  IF State_Inga_No_Kaeshiya == TRUE THEN
    Transfer_Damage = floor(Recoil_Damage * 0.5)
    Recoil_Damage = Recoil_Damage - Transfer_Damage
    Apply_Noise_Damage(Target, Transfer_Damage)
  END IF
END IF

// 行者うかみ: 第4幕の自律介入
IF StoryFlag.UKAMI_RETURNED_YOMOTSU == TRUE
 AND Battle_Location IN [YOMOTSU_HIRASAKA, YOMI_NO_KUNI, TOKOYO] THEN
  Ukami_Autonomy = TRUE
  Ukami_Uses_Party_Resource = FALSE
  Ukami_AutoIntercept = TRUE
END IF
```
- この式が意図する体験: 3人とも「同じ強さ」ではなく、別ルールで戦場を歪める存在として機能する。

### 1.7 位相ギミック（無菌の帳 / 血の泥沼 / 黄泉戸喫）
```text
IF Field_State == STERILE_CURTAIN THEN
  Heal_Output_Mult = 0.6
  SelfCost_Mult = 1.25
END IF

IF Field_State == BLOOD_MUDPIT THEN
  Recovery_Reversal_Rate = YomotsuRecoveryReversalRate
  Jonetsu_Gain_Mult = 1.2
END IF

// 黄泉戸喫: 使用者によって処理が異なる
IF Item_Used == Yomotsu_Mud_Fruit AND User != UKAMI_GYOJA THEN
  Inventory -= 1
  Apply_State(YOMOTSU_CURSE)
END IF

IF Item_Used == Yomotsu_Mud_Fruit AND User == UKAMI_GYOJA THEN
  Inventory = Inventory
  Skip_State_Inflict(YOMOTSU_CURSE)
END IF
```
- この式が意図する体験: 同じ回復でも「誰が使うか」で代償が変わる。

### 1.8 特殊敵と神AI学習段階
```text
// 剥落の星屑
IF Enemy_ID == Hakuraku_Stardust THEN
  Escape_Check = (Current_Tick >= Hakuraku_Return_Gravity_Tick)
  IF Escape_Check THEN
    Hakuraku_Despawn_Window -= 1
  END IF
  IF Hakuraku_Despawn_Window <= 0 THEN
    Enemy_Despawn = TRUE
  END IF
END IF

// 神AI「理の学習段階」
Ri_Level_1_Static = Uses(Current_Stats_Only)
Ri_Level_2_Adaptive = Uses(Current_Stats_And_History)
Ri_Level_25_Psychological = Uses(Pattern_Penalty)
Ri_Level_3_Absolute = Uses(Noise_Resistance_High)
```
- この式が意図する体験: 終盤ほど「いつもの手」が読まれ、非合理な打開策が価値を持つ。

## 2. 実装マスターデータ（Master Tables）

### 2.1 Character_Base_Master
| Char_ID | 名称 | ロール | 基礎活魂 | 基礎情念 | 武器適正 |
|---|---|---|---|---|---|
| `MIKOTO` | ミコト | 万能/写し | 100 | 120 | 斬・刺・打 |
| `UKAMI` | うかみ | 壁/剛 | 200 | 80 | 打・突 |
| `SUKUNA` | スクナ | 毒/剥離 | 80 | 150 | 投・打 |
| `UZU` | ウズ | 攪乱/舞 | 90 | 110 | 扇・短 |
| `TACHIBANA` | タチバナ | 呪/自傷 | 110 | 100 | 杖・櫂 |
| `MAHITO` | マヒト | 鍛/砕 | 150 | 90 | 槌・鉗 |
| `WAKAHIKO` | ワカヒコ | 弓/停 | 95 | 130 | 弓・短 |

### 2.2 Status_Effect_Master（状態異常定義）
| Effect_ID | 名称 | 説明 | 関連 |
|---|---|---|---|
| `POISON` | 毒 | 毎Tick活魂減少 | スクナ、タチバナ |
| `CONFUSION` | 混乱 | ランダム行動/不発。UI予測線の絡まり | ウズ、澱神 |
| `CHARM` | 服従 | 味方攻撃。敵UIの駒化 | 天津神、澱神 |
| `BLIND` | 幻惑 | 命中率低下。着弾点座標の「泥」 | ウズ、ワカヒコ |
| `CRYSTALLIZE` | 琥珀化 | ダメージ・行動不能「永遠の保管」 | 天津神 |
| `WHITE_OATH` | 白の宣託 | 予測UI乖離。プレイヤー確率判断の崩壊 | 探女、白化神 |
| `TRUTH_OBSCURE` | 真実の隠匿 | バフ/付喪神段階の初期化巻き戻し | 豊玉姫、澱神 |
| `PURE_PROVISION` | 無垢なる配給 | 回復と引き換えに情念を枯渇固定 | 宇迦之御魂神 |
| `REGEN_BLOCK` | 再生停止 | 回復無効化 | 大宜都比売 |
| `SHIGURUI_ANCESTOR` | 死狂いの祖 | 連撃+予測攪乱 | 素戔嗚尊（試練） |
| `HISTORY_ERASE` | 歴史の抹消 | 金継ぎ履歴の一時消失 | 瀬織津姫 |
| `KUSANAGI_WEAR` | 草薙の摩耗 | 武器耐久の吸収・防御配分 | 日本武尊 |
| `YOMOTSU_CURSE` | 黄泉の呪い | 黄泉アイテム使用時の永続デバフ | 共有システム |

### 2.3 氷属性サブタイプ（静止/冷却）
属性は相性計算レイヤーであり、術式駆動リソースとは分離して扱う。

| IceSubtype_ID | 名称 | 意味 |
|---|---|---|
| `ICE_STAGNATION` | 神の氷（静止） | 時間・行動を凍結し、琥珀化へ寄せる |
| `ICE_COOLING` | 人の氷（冷却） | 暴走熱を奪って鎮める。過熱抑制、熱散逸 |

```text
IF Attack.IceSubtype == ICE_COOLING AND Target.Tag == AMATSUKAMI THEN
  Damage = floor(Damage * 0.85)
  Skip_State_Inflict(Freeze_Stun)
END IF

IF Attack.IceSubtype == ICE_COOLING AND (Target.Tag == DEIGAMI OR Target.Tag == KIBUTSU) THEN
  Apply_State(Defense_Down, Duration=2)
  Damage = floor(Damage * 1.1)
END IF
```

### 2.4 Weapon_Evolution_Master
| Character_ID | Weapon_Category | Stage_1_初期 | Stage_2_中盤 | Stage_3_終盤 | Narrative_Class |
|---|---|---|---|---|---|
| `MIKOTO` | 刃 | 海揚がりの古錆刀 | 星喰みの黒太刀 | 天叢雲剣 | `INITIAL/MYTHIC` |
| `MIKOTO` | 槍・鉾 | 欠けた祭祀槍 | 隕鉄の剛鉾 | 天之沼矛 | `INITIAL/MYTHIC` |
| `UKAMI` | 槍・鉾 | 獣骨の石鉾 | 大蛇狩りの剛槍 | 国津神の荒鉾 | `INITIAL/MYTHIC` |
| `SUKUNA` | 打撃 | 欠けた石杵 | 毒喰みの乳棒 | 少名の神杵 | `INITIAL/MYTHIC` |
| `MAHITO` | 打撃 | 煤まみれの大槌 | 刃折りの業槌 | 天目の神火槌 | `INITIAL/MYTHIC` |
| `UZU` | 扇 | 破れた舞扇 | 緋色の鉄扇 | 天鈿女の狂扇 | `INITIAL/MYTHIC` |
| `TACHIBANA` | 槍・鉾 | 怨念の流木 | 血塗られた銛 | 弟橘の海人銛 | `INITIAL/MYTHIC` |
| `WAKAHIKO` | 遠距離 | 白木の上弓 | 泥塗れの猟弓 | 天若の返し弓 | `INITIAL/MYTHIC` |

### 2.5 Character_Equipment_Master
| Character_ID | 主腕（利用可カテゴリ） | 固有武器 | 装束 | 形代 |
|---|---|---|---|---|
| `MIKOTO` | 刀・槍 | 大幣（仮想双腕特例） | 星祝の防具 | 泥濘の勾玉 |
| `UKAMI` | 刀・槍・杖 | 錫杖 | 行者の法衣 | 風雷の獣牙 |
| `SUKUNA` | 打撃 | 乳棒 | 薬草師の衣 | 忘却の香炉 |
| `UZU` | 扇・刃・大幣 | 鉄扇・隠し短刀 | 狂乱の舞衣 | トランスの神楽鈴 |
| `TACHIBANA` | 槍・打撃・大幣 | 流木槍・打ち櫂 | 濡れ羽の衣 | 泥水の呪符 |
| `MAHITO` | 打撃 | 大槌・やっとこ | 鍛冶師の重装皮衣 | 炉心の火打石 |
| `WAKAHIKO` | 弓・短刀 | 天上弓・仕込み短刀 | 境界の隠秘服 | 影縫いの鏑矢 |

### 2.6 Enemy_Master
| Enemy_ID | 名称 | タイプ | 特殊仕様 | 撃破/進行フラグ |
|---|---|---|---|---|
| `Amaterasu_Core_OS` | 天照大御神 | システム体 | 戦闘対象ではなく凍結管理 | `AMENO_IWATOWAKE_REBOOT` |
| `Tsukuyomi_AntiVirus` | 月読命 | 偽終幕ボス | 撃破後に絶対暗黒と塔自由落下へ遷移 | `TSUKUYOMI_FAKE_LASBOSS` |
| `Kagaseo_Star_God` | カガセオ | 第4幕ボス | 帰還引力と拒絶理の衝突で特殊減衰 | `KAGASEO_REBOOT_DRIVE_ACQUIRED` |
| `Boss_Yakusa_no_Ikazuchi` | 八雷神 | クリア後ボス | 行者還し専用3フェーズ | `GYOJAGAESHI_CLEARED` |
| `Boss_Susanoo` | スサノオ | 試練ボス | 高密度連撃の監督者 | `SUSANOO_TRIAL_CLEARED` |
| `Boss_Yamata_no_Ubusuna` | 澱神・八岐の産土 | 真裏ボス | 尾破断で剣核露出 | `OROCHI_TAIL_BREACHED` |

### 2.7 Enemy_Tier_Template_Master（追補）
| Tier | Template_ID | 名称 | 系統 | 主属性/副属性 | 主干渉 |
|---|---|---|---|---|---|
| `T1` | `MIRE_BUBBLE_SLIME` | 泥泡の這い | 荒魂獣 | 水/闇 | 群体連撃 |
| `T1` | `WHITE_MOTH` | 白の迷い蛾 | 白化神末端 | 光/風 | 命中撹乱 |
| `T2` | `CHALK_SENTINEL` | 白堊の防人 | 擬神兵 | 光/氷 | 見切り・耐久削り |
| `T2` | `MOURNING_WAIL` | 未練の泣き女 | 澱神 | 闇/水 | 広域睡眠 |
| `T3` | `MIRROR_GUARDIAN` | 鏡面の守護像 | 白化神上位 | 光/氷 | 限定反射 |
| `T4` | `SAGUME_EXECUTOR` | 探女の執行体 | 天津神 | 光/水 | 予測線乖離 |

### 2.8 Attribute_Master（戦術的意味）
| Attribute_ID | 名称 | 戦術的意味 |
|---|---|---|
| `FIRE` | 炎 | 過熱を加速し、停滞に穴を開ける |
| `WATER` | 水 | 流動と浸食。回復・侵食の両義性 |
| `WIND` | 風 | 行動順と位置取りを崩す |
| `EARTH` | 土 | 受け止め、押し返す。重圧制御 |
| `LIGHT` | 光 | 予測と露呈。神側の制御に近い |
| `DARK` | 闇 | 隠匿と反転。予測線の外側を作る |
| `ICE_STAGNATION` | 神の氷 | 静止と凍結へ寄せる |
| `ICE_COOLING` | 人の氷 | 過熱の鎮静と散逸制御 |

### 2.9 星土の脈継ぎ（神社連動）
```text
IF Camp_Action == SHRINE_PRAYER THEN
  Shrine_Prayer_Accumulate += Prayer_Points_Base
END IF

IF Shrine_Prayer_Accumulate >= Prayer_To_Magatama_Threshold THEN
  Yasakani_Prayer_Slot += 1
  Shrine_Prayer_Accumulate -= Prayer_To_Magatama_Threshold
END IF

IF Field_State == BLOOD_MUDPIT THEN
  Yasakani_Stagnation_Slot += Mud_Stagnation_Gain
END IF
```
- この式が意図する体験: 祈りだけでも泥だけでも足りず、両方の履歴が神器を成立させる。

## 3. シナリオ進行・システムフラグ（System Flags）

### 3.1 Story_Flag_Master
| フラグ名 | 発火タイミング |
|---|---|
| `UKAMI_JOINED_EARLY` | うかみ合流 |
| `MAHITO_JOINED_ACT2` | マヒト加入（第2幕固定進行） |
| `KAGUTSUCHI_QUELLED` | 灼熱たたら場・鎮魂完了 |
| `WHITE_CORRIDOR_CLEARED` | 白堊の回廊突破 |
| `MAHITO_FIELD_LV2_UNLOCKED` | マヒト「野鍛冶の誓い」達成 |
| `SHRINE_FORGE_LV3_UNLOCKED` | 神社鍛造拡張 |
| `UKAMI_LEFT_KATSURAGI` | 葛城山での一次離脱、ミコトへのスキル継承 |
| `WAKAHIKO_JOINED_ACT3` | 返し矢降臨イベント後加入 |
| `TSUKUYOMI_FAKE_LASBOSS` | ツクヨミ撃破・偽終幕 |
| `TSUKUYOMI_CELEBRATION_CONDUCTED` | 偽終幕後の凍結UIジャック開始 |
| `UKAMI_RETURNED_YOMOTSU` | 行者うかみ帰還 |
| `GYOJAGAESHI_CLEARED` | クリア後「行者還し」完了 |
| `SUSANOO_TRIAL_UNLOCKED` | 行者還し完了後に試練解禁 |
| `AMENO_IWATOWAKE_REBOOT` | 天岩戸強制再起動 |
| `SUSANOO_TRIAL_CLEARED` | 根堅洲国スサノオ撃破 |
| `OROCHI_TAIL_BREACHED` | 真裏ボスで尾部破断、剣核露出 |
| `ETERNITY_REJECTED` | エンディング |
| `AMENO_MURAKUMO_AWAKENED` | 天叢雲剣覚醒 |

### 3.2 継承の固定習得（Forced Inheritance）
```yaml
TriggerFlag: UKAMI_LEFT_KATSURAGI
TargetCharacter: MIKOTO
ForcedSkills:
  - SkillId: INHERITED_SARUTA_BREAK
    Name: 猿田の破岩撃 (剛)
  - SkillId: INHERITED_HORAGAI_ROAR
    Name: 法螺の轟き (導)
```

## 4. UI/UX制御ロジック（UI Logic）

| UI_ID | 表示対象 | 表示方針 |
|---|---|---|
| `UI_KAKKON_GAUGE` | 活魂 | 警告色、死狂い時の特殊表示 |
| `UI_JONETSU_GAUGE` | 情念 | 空殻遷移時の警告 |
| `UI_DURABILITY_METER` | 武器耐久 | 段階的劣化、代受苦推奨表示 |
| `UI_PREDICTION_LINE` | 予測線 | 乖離型・ノイズ型の歪み表示 |

## 5. 運用ルール（Maintenance Rules）

1.  **DRY原則**: スキル説明文側に直接数値を書かず、本マスターを参照すること。
2.  **SSOT**: 実装値、計算式、フラグの正本は常に本ファイルとする。
3.  **整合性**: 各幕の進行フラグ変更時は、必ず `Scenario_Capability_Master` も確認する。

---
**Single Source of Truth**: 上記パラメータの実数値はすべて本ファイルのみで管理する。画面表示・物語表現・UX演出での独自変更を禁止する。
