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

注記:
- このロジックは「ギリギリの生還が次の燃料になる」という体験目標を実装化したもの。
- 係数調整時は [SYS-20_Game_Systems_and_Flow.md](SYS-20_Game_Systems_and_Flow.md) の体験ループを同時に確認する。

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

注記:
- 苦境条件（瀕死、属性不利、領域不利）での使用は、学習速度を意図的に高める設計。
- 数値を上げ下げする時は「苦境で学ぶ価値」を失わないことを優先する。

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
- `KAGUTSUCHI_AWAKENED`: 灼熱たたら場でカグツチ残滓が顕現。
- `NAKIME_DEFEATED_ACT3`: ナキメ戦終了。
- `WAKAHIKO_KAESHIYA_AWAKENED`: 返し矢常時化。
- `STERILE_CURTAIN_UNLOCKED`: 無菌の帳を展開する敵位相が解放。
- `BLOOD_MUDPIT_UNLOCKED`: 血の泥沼位相が解放。
- `KAGASEO_REBOOT_DRIVE_ACQUIRED`: 星屑の荒野で駆動片取得。
- `AMENO_MURAKUMO_AWAKENED`: オロチ尾剣核を現行武器へ接合。

## 氷属性サブタイプ定義（静止/冷却）

| IceSubtype_ID | 名称 | 意味 |
|---|---|---|
| `ICE_STAGNATION` | 神の氷（静止） | 時間・行動を凍結し、琥珀化へ寄せる。 |
| `ICE_COOLING` | 人の氷（冷却） | 暴走熱を奪って鎮める。過熱抑制と熱散逸誘発に使う。 |

```text
IF Attack.IceSubtype == ICE_COOLING AND Target.Tag == AMATSUKAMI THEN
  Damage = floor(Damage * 0.85)
  Skip_State_Inflict(Freeze_Stun)
END IF

IF Attack.IceSubtype == ICE_COOLING AND Target.Tag == WILDLIFE THEN
  Apply_State(Slow, Duration=1)
END IF

IF Attack.IceSubtype == ICE_COOLING AND (Target.Tag == DEIGAMI OR Target.Tag == KIBUTSU) THEN
  Apply_State(Defense_Down, Duration=2)
  Damage = floor(Damage * 1.1)
END IF
```

## Status_Effect_Master（追補）

| Effect_ID | 名称 | 効果 | 主な使用者 |
|---|---|---|---|
| `WHITE_OATH` | 白の宣託 | 予測UIの表示線と実行結果を乖離させる。確率判断を崩す攪乱干渉。 | 探女、白化神上位 |
| `TRUTH_OBSCURE` | 真実の隠匿 | 情念依存技の発動契機で、対象のバフや付喪神段階を初期化側へ巻き戻す。 | 豊玉姫、澱神上位 |
| `PURE_PROVISION` | 無垢なる配給 | 活魂回復と引き換えに情念を枯渇側へ固定し、連撃熱伝導を分断する。 | 宇迦之御魂神、白化神支援 |
| `REGEN_BLOCK` | 再生停止の呪い | 回復系処理を無効化し、再生前提の持久戦を破綻させる。 | 大宜都比売、国津神上位 |
| `SHIGURUI_ANCESTOR` | 死狂いの祖 | 高密度連撃と予測攪乱を同時付与する裏ボス専用危険状態。 | 素戔嗚尊（試練） |
| `HISTORY_ERASE` | 歴史の抹消 | 武器の金継ぎ履歴を一時消失させ、履歴依存補正を遮断する。 | 瀬織津姫、非神上位 |
| `KUSANAGI_WEAR` | 草薙の摩耗 | 攻撃時に対象の武器耐久を吸収して敵自身の耐久と防御へ再配分する。 | 日本武尊、非神上位 |
| `WAKAHIKO_KAESHIYA_PASSIVE` | 返し矢の呪い | 弓攻撃ごとに消費情念比率で威力上昇と自傷反動を同時発生させる。 | ワカヒコ固有 |
| `INGA_NO_KAESHIYA` | 因果の返し矢 | 返し矢反動の一部を敵へ予測線ノイズとして転写する。 | ワカヒコ固有 |
| `MIREN_HEAT_BUFF` | 未練の熱伝導 | 反動自傷直後、次行動のみ威力補正を与える。 | ワカヒコ固有 |

## Enemy_Behavior_Tag

| Tag_ID | 概要 | 主な挙動 |
|---|---|---|
| `PREDICTION_SKEW` | 予測線乖離型 | 表示予測と実行結果をずらす。 |
| `JONETSU_DRAIN` | 情念枯渇型 | 情念回復導線を分断し、燃料不足を誘発する。 |
| `REPAIR_PUNISH` | 修復罰型 | 回復・修復行動へ反応して追加圧を発生させる。 |
| `HISTORY_CUT` | 履歴遮断型 | 金継ぎ履歴や付喪神段階へ直接干渉する。 |
| `DURABILITY_LEECH` | 耐久吸収型 | 武器耐久を吸収して自己強化へ変換する。 |
| `LOCKDOWN_FIELD` | 位相拘束型 | 無菌/泥沼などの領域圧で選択肢を絞る。 |
| `CHAIN_BREAK` | 連鎖断絶型 | 連撃熱伝導・共鳴連携を中断する。 |
| `EXECUTION_RUSH` | 処刑加速型 | 危険ターンの密度を上げ、停止失敗を致命化する。 |

## Enemy_Tier_Template_Master（追補）

| Tier | Template_ID | 名称 | 系統 | 主属性 / 副属性 | 主干渉 | 状態異常依存 | 行動タグ |
|---|---|---|---|---|---|---|---|
| T1 | `MIRE_BUBBLE_SLIME` | 泥泡の這い | 荒魂獣 | 水 / 闇 | 群体で押し切る連撃圧 | なし | `CHAIN_BREAK` |
| T1 | `NUMBING_JELLY` | 痺れ海月 | 荒魂獣 | 水 / 氷 | 触手で行動阻害 | `PARALYSIS` | `EXECUTION_RUSH` |
| T2 | `CHALK_SENTINEL` | 白堊の防人 | 擬神兵 | 光 / 氷 | 見切りで耐久のみ削る | なし | `PREDICTION_SKEW` |
| T2 | `MOURNING_WAIL` | 未練の泣き女 | 澱神 | 闇 / 水 | 広域の睡眠誘発 | `SLEEP` | `JONETSU_DRAIN` |
| T3 | `HISTORY_DROWNER` | 記録喰らいの禊神 | 非神 | 水 / 光 | 武器履歴の一時消去 | `HISTORY_ERASE` | `HISTORY_CUT` |
| T3 | `KUSANAGI_WRAITH` | 草薙の亡霊 | 非神 | 風 / 炎 | 耐久吸収で自己再生 | `KUSANAGI_WEAR` | `DURABILITY_LEECH` |
| T4 | `SAGUME_EXECUTOR` | 探女の執行体 | 天津神 | 光 / 水 | 予測線の乖離誘発 | `WHITE_OATH` | `PREDICTION_SKEW` |
| T4 | `TOYOTAMA_SURGE` | 豊玉姫の潮影 | 澱神上位 | 水 / 闇 | 情念依存技への逆算妨害 | `TRUTH_OBSCURE` | `JONETSU_DRAIN` |
| T4 | `UKA_SUPPLY_CORE` | 宇迦之御魂の配給核 | 天津神支援 | 土 / 光 | 回復と情念枯渇の二択圧 | `PURE_PROVISION` | `REPAIR_PUNISH` |

補足:
- 敵系統の読解導線は [SYS-21_Enemy_Ecology_and_UI.md](SYS-21_Enemy_Ecology_and_UI.md) を参照。
- 値・フラグ・状態の正本は本テーブルと `Status_Effect_Master` を優先。

## Scenario_Capability_Master（ワカヒコ）

| Capability_ID | 名称 | 効果 | 解禁条件 |
|---|---|---|---|
| `WAKAHIKO_PROPHECY_TAP` | 神託傍受 | 予測線ノイズの先読み補助。 | `WAKAHIKO_KAESHIYA_AWAKENED` |
| `WAKAHIKO_DOMAIN_SPOOF` | 神域通行偽装 | 一部神域で検知率低下。 | 第3幕加入後 |
| `WAKAHIKO_ARCHIVE_READ` | 天側記録参照 | 敵行動の補助ヒントを開示。 | 第3幕加入後 |
| `WAKAHIKO_YOMI_COORD` | 黄泉座標補助 | 黄泉領域の導線補正。 | 第4幕進行 |

## World_Milestone_Master（導線と難度段階）

| Milestone_ID | 主幕 | 主イベント | 解放要素 | 難度意図 |
|---|---|---|---|---|
| `MS_WHITE_CHALK_LOOP` | 第2幕前半 | 白堊の回廊 | ウズ加入導線 | 予定調和への敗北学習 |
| `MS_FORGET_CAVE_PRESSURE` | 第2幕中盤 | 忘却の海食洞 | タチバナ加入導線 | 全体圧への対処学習 |
| `MS_TATARA_KAGUTSUCHI` | 第2幕中盤 | 灼熱たたら場 | マヒト加入、Lv2鍛造導線 | 耐久破綻からの再構築 |
| `MS_KATSURAGI_DEPARTURE` | 第2幕終盤 | 葛城山離脱 | うかみ固定継承 | 不在下での再編学習 |
| `MS_TENSHU_JOIN_WAKAHIKO` | 第3幕中盤 | 天望の天守 | ワカヒコ加入、返し矢導線 | 停止と先制の導入 |
| `MS_YOMI_MIXED_FIELD` | 第4幕 | 黄泉領域混在 | 行者うかみ自律介入 | 毎戦再計画の定着 |

## UI_Implementation_Master

| UI_ID | 表示対象 | 表示方針 | 実装備考 |
|---|---|---|---|
| `UI_KAKKON_GAUGE` | 活魂 | 破断直前で警告色を強調 | 死狂い遷移と同時に状態表示を更新 |
| `UI_JONETSU_GAUGE` | 情念 | 増減速度を視覚化 | 空殻遷移で行動制限ヒントを表示 |
| `UI_DURABILITY_METER` | 武器耐久 | 段階的劣化を表示 | レッド帯で代受苦推奨ヒント |
| `UI_FIELD_PHASE` | 領域位相 | 無菌/泥沼を常時表示 | 混在時は優先相を明示 |
| `UI_PREDICTION_LINE` | 予測線 | 変化量を強調表示 | 乖離型敵では注意表示を追加 |

## Post_Game_Content_Master（検討段階）

| Content_ID | 名称 | 概要 | 実装ステータス |
|---|---|---|---|
| `PG_SCAR_SEA` | 傷跡の海 | クリア後高難度探索 | Draft |
| `PG_GYOJA_RETURN` | 行者還しの儀 | うかみ地上帰還の多段試練 | Draft |
| `PG_YAKUSA_BOSS` | 八雷神試練 | 儀式導線ボス戦 | Draft |
| `PG_MURAKUMO_AWAKEN` | 天叢雲覚醒導線 | 剣核接合の最終鍛造 | Draft |

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

## 装備実装マスター（RPG5移植・Wave3）

### Equipment_Slot_Master（追補）

| Slot_ID | 名称 | 基本仕様 | 備考 |
|---|---|---|---|
| `SLOT_MAIN_WEAPON` | 主腕 | 全員共通。戦闘計算の主参照。 | 2H装備時は副武器を無効化。 |
| `SLOT_OFFHAND_WEAPON` | 副武器 | ミコト専用。通常時は待機。 | `DualStanceActive == TRUE` の間のみ攻撃計算に参加。 |
| `SLOT_ARMOR` | 装束 | 全員共通。被ダメと耐性へ寄与。 | 耐久は武器と別管理。 |
| `SLOT_KATASHIRO_1` | 形代1 | 任意。補助効果枠。 | 形代は最大2枠。 |
| `SLOT_KATASHIRO_2` | 形代2 | 任意。補助効果枠。 | 形代未装備時は空枠。 |

### Weapon_Category_Master（追補）

| Category_ID | 主な使用者 | 片手/両手 | 代表用途 |
|---|---|---|---|
| `SWORD_STRAIGHT` | ミコト | 1H | 基本斬撃、継承運用。 |
| `SPEAR_LONG` | ミコト | 2H | 貫通、重圧、先手割込み。 |
| `GOHEI_RESONANCE` | ミコト | 1H | 共鳴補助、反射補助。 |
| `SCOUT_BLADE` | うかみ | 1H | 中断、破砕、生存反撃連携。 |
| `STONE_PIKE` | うかみ | 2H | 重打・行動阻害。 |
| `GAUNTLET_BEAT` | うかみ/ミコト | 1H | 固定継承技の媒体。 |
| `CLUB_MILK` | スクナ | 1H | 劇薬起点、毒・酸制御。 |
| `HAMMER_HEAVY` | マヒト | 2H | 武器破砕、バフ粉砕。 |
| `TONGS_HEAVY` | マヒト | 2H | 捕捉、耐久剥離。 |
| `FAN_IRON` | ウズ | 1H | 攪乱、多段、風圧。 |
| `DAGGER_DANCE` | ウズ | 1H | 裏拍割込み、対バリア。 |
| `POLE_DRIFTWOOD` | タチバナ | 2H | 呪詛、遅延、分散。 |
| `OAR_DRIFTWOOD` | タチバナ | 2H | 打撃、沈底、遅延罠。 |
| `BOW_HEAVEN` | ワカヒコ | 2H | 先制、停止、返し矢軸。 |
| `DAGGER_SURVIVAL` | ワカヒコ | 1H | 接近時の生存反撃。 |

### Carry_Tool_Master（装備スロット外の常時携行）

| Tool_ID | 対象キャラ | 扱い | 主な連動 |
|---|---|---|---|
| `HOURAGAI` | うかみ | 常時携行 | 法螺の轟き、導線バフ。 |
| `MORTAR_STONE` | スクナ | 常時携行 | 劇薬調合、散布系スキル。 |
| `KAGURA_MASK` | ウズ | 常時携行 | 狂騒の視線、攪乱演出。 |
| `CURSE_DOGU_SET` | タチバナ | 常時携行 | 自傷・土偶、痛み転写。 |
| `QUIVER_SET` | ワカヒコ | 常時携行 | 鏑矢系、時限矢系。 |

## Character_Skill_Master（RPG5移植・Wave3）

### ミコト

| Skill_ID | 技名 | ロール | コスト/反動タグ |
|---|---|---|---|
| `SKL_MIKOTO_DORONAGI` | 泥薙ぎの太刀 | 全体斬撃 | `DURABILITY_LIGHT` |
| `SKL_MIKOTO_KOHAKU_BREAK` | 琥珀砕きの太刀 | 白化神特効 | `PTG_PIERCE` |
| `SKL_MIKOTO_RAIMEI` | 雷鳴の刺突 | 貫通 | `DURABILITY_PLUS_IF_2H` |
| `SKL_MIKOTO_SOUSEI` | 直刀・双星突き | 連撃 | `DUAL_REQUIRED` |
| `SKL_MIKOTO_DOKAI_PRESS` | 泥界の重圧 | 全体遅延 | `TICK_PUSH` |
| `SKL_MIKOTO_KEISHO_BLADE` | 継承の刃 | 属性付与 | `INHERIT_LINK` |
| `SKL_MIKOTO_STARDUST_BLADE` | 星屑の絶刀 | 全体光 | `JONETSU_COST` |
| `SKL_MIKOTO_KOTOTSUGI` | 言継ぎ | 神写し補助 | `INHERIT_GAIN_UP` |
| `SKL_MIKOTO_MIKENURI` | 泥繭の眠り | 自己再生 | `CHANNEL_BREAK_ON_HIT` |
| `SKL_MIKOTO_PRAYER_SAND` | 祈りの星砂 | 単体回復 | `KAKKON_SELF_COST` |
| `SKL_MIKOTO_KANRYU` | 命の還流 | 空殻復帰 | `KAKKON_SELF_COST` |
| `SKL_MIKOTO_DAIJUKEI` | 代受の誓い | 肩代わり | `DAMAGE_SHARE` |
| `SKL_MIKOTO_HAGAN` | 猿田の破岩撃 | 固定継承火力 | `FIXED_INHERIT_SLOT` |
| `SKL_MIKOTO_OVERHEAT` | 共鳴過熱・焔陣 | バースト | `WEAPON_BURNOUT` |
| `SKL_MIKOTO_EIEN_KYOHI` | 永遠の拒絶 | 異常無効 | `KAKKON_SELF_COST` |

### うかみ（斥候時代）

| Skill_ID | 技名 | ロール | コスト/反動タグ |
|---|---|---|---|
| `SKL_UKAMI_JUGOSO` | 獣の剛槍 | 単体重打 | `DURABILITY_COST` |
| `SKL_UKAMI_DAISENPU` | 荒ぶる大旋風 | 全体打撃 | `DURABILITY_PERCENT_COST` |
| `SKL_UKAMI_HIREKI` | 飛礫落とし | 全体物理 | `NO_DURABILITY_COST` |
| `SKL_UKAMI_KINGA` | 牙城割り | 装甲剥離 | `PTG_DOWN` |
| `SKL_UKAMI_HOERU` | 獣の咆哮 | 中断 | `STUN` |
| `SKL_UKAMI_DOROTSUBUTE` | 泥玉つぶて | 命中低下 | `HIT_DOWN` |
| `SKL_UKAMI_DAIJUKU` | 野性の代受苦 | 耐久変換火力 | `WEAPON_BREAK_ON_USE` |
| `SKL_UKAMI_TOSHIN` | 捨て身の突進 | 大遅延 | `KAKKON_SELF_COST` |
| `SKL_UKAMI_HORA` | 法螺の轟き | 全体情念補助 | `JONETSU_GAIN_UP` |
| `SKL_UKAMI_DOROWADACHI` | 導きの泥轍 | 味方加速 | `DURABILITY_COST` |

### スクナ

| Skill_ID | 技名 | ロール | コスト/反動タグ |
|---|---|---|---|
| `SKL_SUKUNA_DOKU_KINE` | 劇毒の杵打ち | 毒付与 | `HP_RATIO_POISON` |
| `SKL_SUKUNA_KYOUSAN` | 強酸の霧散 | 防御無視 | `PTG_PIERCE` |
| `SKL_SUKUNA_CHAOS_SPRAY` | 錯乱の散布 | 混乱 | `CONFUSE` |
| `SKL_SUKUNA_FORGET` | 忘却の霧 | 封印 | `SEAL_SPECIAL` |
| `SKL_SUKUNA_COOL_DOSE` | 冷却の服用 | 回復+過熱抑制 | `HEAT_DOWN` |
| `SKL_SUKUNA_COOL_THROW` | 冷却の投擲 | 冷却属性攻撃 | `ICE_COOLING` |
| `SKL_SUKUNA_PAINLESS` | 劇薬：痛覚麻痺 | 被ダメ半減 | `AFTER_RECOIL` |
| `SKL_SUKUNA_BERSERK` | 劇薬：狂戦士 | 攻撃強化 | `DURABILITY_DRAIN_UP` |
| `SKL_SUKUNA_REVIVE_MIX` | 劇薬：起死回生 | 情念再起動 | `KAKKON_SELF_COST` |
| `SKL_SUKUNA_STAR_EAT` | 理の簒奪（星喰い） | 吸収 | `JONETSU_DRAIN` |

### マヒト

| Skill_ID | 技名 | ロール | コスト/反動タグ |
|---|---|---|---|
| `SKL_MAHITO_HASAMI` | 挟み込みの業 | 耐久+装甲削り | `DUAL_BREAK` |
| `SKL_MAHITO_BLADE_BREAK` | 刃折りの大槌 | 武器破壊 | `WEAPON_BREAK_PRESSURE` |
| `SKL_MAHITO_LAND_SPLIT` | 灼熱の大地割り | 全体中断 | `INTERRUPT` |
| `SKL_MAHITO_FOOTHI` | 踏鞴の火柱 | 足止め | `DURABILITY_COST` |
| `SKL_MAHITO_ICE_SLAG` | 炉滓の氷噴 | 冷却脆化 | `ICE_COOLING` |
| `SKL_MAHITO_HAMMER_ROAR` | 槌の轟き | バフ解除 | `BUFF_RESET` |
| `SKL_MAHITO_BUKI_BREAK` | 武具叩き折り | 武器耐久圧 | `RED_ZONE_FORCE` |
| `SKL_MAHITO_KINTSUGI_LIFE` | 命の金継ぎ | 単体大回復 | `KAKKON_SELF_COST` |
| `SKL_MAHITO_FUIGO` | 鞴の大風 | 全体属性軽減 | `AURA_DEF_UP` |
| `SKL_MAHITO_IRON_WALL` | 鉄の城壁 | ヘイト集約 | `FORCE_TARGET` |

### ウズ

| Skill_ID | 技名 | ロール | コスト/反動タグ |
|---|---|---|---|
| `SKL_UZU_KYOFU` | 狂風の舞 | 全体風圧 | `AOE` |
| `SKL_UZU_RANBU` | 鉄扇の乱舞 | 多段 | `DURABILITY_HIGH` |
| `SKL_UZU_GENWAKU` | 幻惑の舞 | 命中妨害 | `AIM_SKEW` |
| `SKL_UZU_SHISEN` | 狂騒の視線 | 混乱 | `CONFUSE` |
| `SKL_UZU_RANCHO` | 乱調の裏拍 | 遅延 | `TICK_PUSH` |
| `SKL_UZU_KYORAN` | 狂乱の裏拍 | シャッフル | `TICK_SHUFFLE` |
| `SKL_UZU_ARAHEI_STOP` | 荒幣の逆撫で | 単体停止 | `TICK_STOP` |
| `SKL_UZU_KASSAI` | 喝采の舞 | 味方加速 | `ALLY_TICK_UP` |
| `SKL_UZU_KYOSOU_GRAV` | 狂騒の引力 | 情念還流 | `RESOURCE_STEAL` |
| `SKL_UZU_FINALE` | 狂信のフィナーレ | 強制不発 | `WEAPON_BURNOUT` |

### タチバナ

| Skill_ID | 技名 | ロール | コスト/反動タグ |
|---|---|---|---|
| `SKL_TACHIBANA_ENNEN` | 怨念の渦潮 | 全体攻撃 | `KAKKON_SELF_PERCENT_COST` |
| `SKL_TACHIBANA_SENKETSU` | 鮮血の代償 | 単体固定打点 | `KAKKON_SELF_PERCENT_COST` |
| `SKL_TACHIBANA_KAIJU` | 海底の重圧 | 遅延圧 | `TICK_PUSH_HEAVY` |
| `SKL_TACHIBANA_DOROMIZU` | 泥水の呪詛 | 全体毒 | `POISON_ALL` |
| `SKL_TACHIBANA_FORGET_WAVE` | 忘却の海鳴り | 全体睡眠 | `SLEEP_ALL` |
| `SKL_TACHIBANA_HIAI` | 悲哀の波紋 | 全体弱体 | `ALL_STAT_DOWN` |
| `SKL_TACHIBANA_DOGU` | 自傷・土偶 | 攻撃型妨害 | `KAKKON_SELF_PERCENT_COST` |
| `SKL_TACHIBANA_CHISHIO` | 執着の血潮 | 被害分散 | `HP_LINK` |
| `SKL_TACHIBANA_IKENIE` | 生贄の祈り | 蘇生 | `KAKKON_SELF_COST` |
| `SKL_TACHIBANA_SHUSHU` | 執着の修復 | 自己再生 | `KAKKON_SELF_COST` |

### ワカヒコ

| Skill_ID | 技名 | ロール | コスト/反動タグ |
|---|---|---|---|
| `SKL_WAKAHIKO_SENKAKE` | 先駆けの矢 | 先制 | `PREEMPTIVE` |
| `SKL_WAKAHIKO_SAMIDARE` | 五月雨撃ち | 連撃 | `MULTI_HIT` |
| `SKL_WAKAHIKO_HISSATSU` | 必殺の矢 | 防御無視 | `PIERCE` |
| `SKL_WAKAHIKO_OTORIDORI` | 落鳥の矢 | 飛行特効 | `ANTI_AIR` |
| `SKL_WAKAHIKO_UGATEN` | 穿天の矢 | 天勢力特効 | `ANTI_HEAVEN` |
| `SKL_WAKAHIKO_SHADOW_BIND` | 影縫いの刃 | 足止め | `TICK_BIND` |
| `SKL_WAKAHIKO_TIME_ARROW` | 時限の鏑矢 | 時限爆発 | `DELAY_BOMB` |
| `SKL_WAKAHIKO_DECOY` | 霧の幻影 | 命中低下 | `DECOY` |
| `SKL_WAKAHIKO_KAESHIYA` | 返し矢の呪い | 反動火力 | `RECOIL` |
| `SKL_WAKAHIKO_INGA` | 因果の返し矢 | 反動転写 | `RECOIL_TRANSFER` |
| `SKL_WAKAHIKO_SURVIVE` | 生存の足掻き | 確定反撃 | `COUNTER_100` |

### 行者うかみ（第4幕限定・自律）

| Skill_ID | 技名 | 実行タイプ | 発動条件タグ |
|---|---|---|---|
| `SKL_GYOJA_HAJA` | 破邪の錫杖 | 自律祈祷 | `AUTO_ON_POLLUTION` |
| `SKL_GYOJA_RYUO` | 竜王の法印 | 自律祈祷 | `AUTO_ON_PARALYSIS` |
| `SKL_GYOJA_DORO_JIN` | 泥土の法陣 | 自律祈祷 | `AUTO_ON_DAMAGE_ACCUM` |
| `SKL_GYOJA_KITO` | 行者の祈祷 | 自律祈祷 | `AUTO_PERIODIC_HEAL` |
| `SKL_GYOJA_HANKON` | 反魂の祈祷 | 自律祈祷 | `AUTO_ON_ALLY_DEATH` |

## 運用ルール（Wave3追補）

- `SYS-22` は「優先順・運用判断」を持ち、本ファイルは「技ID・タグ・反動管理」を持つ。
- 技名の追加・削除時は `Character_Skill_Master` と `Status_Effect_Master` の突合を同時実施する。
- 装備カテゴリを伴う技は、`Weapon_Category_Master` のID変更を禁止する（セーブ互換維持）。
