---
uid: [SYS-30]
role: data-and-logic
status: active
depends_on:
  - SYS-20_Game_Systems_and_Flow.md
  - ../01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md
  - ../00_Governance/ARC-00_Implementation_Charter.md
influences:
  - ../02_Narrative/NAR-10_Narrative_and_Characters.md
  - ../04_Art/ART-40_Art_Direction_and_Assets.md
  - ../01_Worldbuilding/WRD-99_Archive_and_Changelog.md
---

# アシブネノミコト 〜天降る御子と、星屑の大地〜

# [SYS-30] Data and Logic Architecture

本ドキュメントはRPG企画5における実装要件・変数定義の最上位正本である。物語的・情動的な表現は `../02_Narrative/NAR-10_Narrative_and_Characters.md` と `SYS-20_Game_Systems_and_Flow.md` に委ね、ここでは変数・フラグ・計算式を定義する。バランス数値の変更は本ファイルを唯一の更新点とすること。

## 幕タイトルがコードに与える影響
本ファイルの設計には、各幕のサブタイトルが示す位相（固・液・プラズマ・再結晶・相転移）が暗黙の前提として組み込まれている。例えば第2幕では「滲む境界」を表現するために環境圧フラグ `FreezeVacuum` や `BloodMud` の計算式が液相的挙動を模倣し、第3幕のピーク戦闘では共鳴イベントトリガー `Spark_Flare` がプラズマ相の爆発的発生を再現する。終幕での`HeatDissipation`係数は「還り着く熱」の相転移特性を反映する等、記録設計者はサブタイトルの位相を参照しながら数値を調整すること。


---

## 1. コア計算式とリソース体系

### 術式駆動リソース（三条の熱源）
本作に汎用的な「魔法値（MP）」は存在せず、以下の3リソースで術式・状態を管理する。

1. **活魂（Kakkon_Value）**:
    - **定義**: 肉体の生命力と持久力の統合値（事象としての「器」）。主腕の振舞いや被ダメージで減算。
2. **情念（Jonetsu_Value）**:
  - **定義**: 戦う気力と魂の熱。`Jonetsu_Max` を上限とする**ゲージ値**で管理する。
      UI上はMPと同様に「残り値が減っていく」形で表示される。
    - **蓄積**: 基本ロジックは変わらず、被ダメージや味方ピンチで増加。
      ```
      Jonetsu_new = min(Jonetsu_Max, Jonetsu_old + floor(Damage_Taken * Char_Factor)
                           + floor(Ally_Critical_Crisis * Sync_Factor))
      ```
      消費時は `Jonetsu_new = Jonetsu_old - Cost` のようにMP同様に減算される。
      ゲームプレイ上は「必要コストを満たす残量があるか」で直感的に把握できる。
    - **回復手段（ゲーム中アクション）**:
      ```
      Jonetsu_recover_just = floor(Base_Just_Reward * Just_Action_Multiplier)
      Jonetsu_recover_chain = floor(Base_Chain_Reward * Chain_Multiplier)
      Jonetsu_recover_breath = floor(Jonetsu_Max * Breathing_Percent)  # 0.3〜0.5
      ```
      *`Just_Action_Multiplier` はジャスト防御/回避成功時に適用される。
      *`Chain_Multiplier` は連続行動コンボ時に適用される。
    - **補足: 神写しのコスト計算**
      ミコトが他キャラの技を使用する際、情念消費に乗算ペナルティを加える。
      ```
      Cost = Base_Cost * (skill_owner == "Ukami" && Ukami_Gauntlet ? 1.0 : Cost_Mult)
      ```
      `Cost_Mult` は1.5〜2.0の範囲で調整。
    - **スロット管理**:
      ミコトの神写し可能枠は成長と各種イベントで拡張される。
      ```
      ShinUtsushi_Slots = min(Max_Slots, Base_Slots + Growth_Factor)
      ```
      戦闘中の入れ替えは不可。キャンプやセーブ時のみ編集。
### 境界状態判定ロジック (Boundary States)
```
IF Kakkon_Value <= 0 AND Jonetsu_Value > 0 AND Has_Shigurui_Passive == TRUE THEN
  State_Shigurui = TRUE
  // 物理ダメージ完全無効化・敵の理による予測ルート完全遮断
  // 行動順（Tick）が回ってくるごと、または行動ごとに Jonetsu_Value が固有コストで減少
END IF

// 死狂い状態からの回復判定
IF State_Shigurui == TRUE AND Kakkon_Value >= 1 THEN
  State_Shigurui = FALSE
  // 通常状態へ復帰
END IF

IF Kakkon_Value > 0 AND Jonetsu_Value <= 0 THEN
  State_Karakara = TRUE
  // スキル使用不可・回避率=0・被弾時確定クリティカル
END IF

IF (Kakkon_Value <= 0 AND (Jonetsu_Value <= 0 OR Has_Shigurui_Passive == FALSE)) OR (Kakkon_Value <= 0 AND Anchor_Equipped_Count == 0) THEN
  State_Dead = TRUE // 泥への還り（完全死）
END IF

IF FreezeVacuum_Turns > 0 THEN
  State_FreezeVacuum = TRUE
  // 情念依存技を封印、行動順補正に負値
  Jonetsu_Skill_Seal = TRUE
  Tick_Speed_Mult = Tick_Speed_Mult * FreezeVacuum_Tick_Mult
END IF
```
3. **武器摩耗（Durability Drain）**:
    - **定義**: 独立した熱ゲージは存在せず、摩擦・負荷はすべて武器耐久度 `Weapon_Durability` の減衰として扱う。
      特技・連続攻撃・意図的負荷で発生する消耗は、常に**耐久度直接減少**へ集約される。UIは耐久度バーのみ表示する。
    - **運用**: 技使用時に発生する「摩耗コスト」が耐久度を削り、耐久度0で武器は**破損・使用不可**になる。
      再使用には野営地または拠点で `Lv1` 以上（金継ぎ以上）の修復実行が必須。
      耐久が尽きる前に金継ぎで維持するか、代受苦で残値を燃料にして大ダメージを撃つかという選択は従来通り。

### 武器耐久度（Durability）モデル
```
Durability_new = max(0, Durability_old - (
    Base_Weapon_DurabilityCost * Stance_Multiplier
  + Skill_Durability_Cost
  + Intentional_Cost
))
```
- `Stance_Multiplier`: 
    - 2H（主腕のみ）: **1.0**
    - 1H + 副腕なし: **1.0**
    - 1H + 副腕（訓練者: うかみ、タチバナ等）: **1.0**
    - 1H + 副腕（非訓練者: ミコト、スクナ等）: **1.2**（「構えの摩擦（Stance Friction）」による増加）
- `Intentional_Cost`: プレイヤーが任意に支払う自傷（活魂）・情念放出コスト。神の計算ノイズの源泉。
- **Tsukumogami_Awakening_Penalty**: 付喪神化武器は耐久減少係数が **1.5〜3.0倍** に跳ね上がる（強力だが即消耗する）。

### 武器メンテナンス段階ロジック（Maintenance Tier）
マヒト加入前後で「何がどこで実行できるか」を厳密に制御する。

```
# Camp / Field
Camp_Maintenance_Level = 0
IF StoryFlag.MAHITO_JOINED_ACT2 THEN
  Camp_Maintenance_Level = 1
END IF
IF StoryFlag.MAHITO_FIELD_LV2_UNLOCKED THEN
  Camp_Maintenance_Level = 2
END IF

# Base / Settlement Forge
Base_Maintenance_Level = 1
IF StoryFlag.MAHITO_JOINED_ACT2 THEN
  Base_Maintenance_Level = 2
END IF
IF StoryFlag.SHRINE_FORGE_LV3_UNLOCKED THEN
  Base_Maintenance_Level = 3
END IF

Can_Use_Kintsugi = (Current_Location_Level >= 1)
Can_Use_Tsukumogami_Awakening = (Current_Location_Level >= 2) AND Mahito_InParty
Can_Use_Mythic_Forging = (Current_Location_Level >= 3) AND Mahito_InParty AND Act_Index >= 4

Can_Use_Daijuku = (Weapon_Durability > 0) AND (Weapon_Usable == TRUE)
Can_Use_Extreme_Daijuku = Is_Destiny_Battle
  AND Can_Use_Tsukumogami_Awakening
  AND (TsukumogamiState == "Musubi" OR Is_Tsukumogami == TRUE)

Can_Repair_Weapon = (Current_Location_Level >= 1)
IF Weapon_Durability <= 0 THEN
  Weapon_Usable = FALSE
END IF
IF Can_Repair_Weapon THEN
  Weapon_Usable = TRUE
END IF
```

- `MAHITO_JOINED_ACT2` が立った時点で「野営Lv1」「拠点Lv2」を同時解禁。これは、同時にカグツチ顕現イベントが終了し`KAGUTSUCHI_QUELLED`（または `KAGUTSUCHI_AWAKENED` を含む）フラグが立った瞬間である。
- `MAHITO_FIELD_LV2_UNLOCKED` は第3幕タケミカヅチ戦クリア後にのみ立てる。野鍛冶の誓いイベントがこのタイミングに含まれる。
- `SHRINE_FORGE_LV3_UNLOCKED` は大型神社拡張と第4幕条件の複合解禁。
- `KAGUTSUCHI_QUELLED` / `KAGUTSUCHI_AWAKENED` は灼熱たたら場における最初の付喪神顕現がカグツチ残滓を呼び覚まし、プレイヤーがこれを鎮魂したことで設定される。このフラグはストーリー進行及びシステム解放（Lv2解放の前提）に利用される。

### 共鳴過熱（新ゲージ非採用）
共鳴過熱は新規リソースを持たず、`Jonetsu_Value` と `Weapon_Durability` を直接操作して表現する。
```
Can_Trigger_ResonanceBurst = (Jonetsu_Value >= ResonanceBurst_Jonetsu_Min) AND (Weapon_Durability > 0)

IF Can_Trigger_ResonanceBurst THEN
  Jonetsu_Value = max(0, Jonetsu_Value - ResonanceBurst_Jonetsu_Cost)
  Damage_Mult = 1.0 + ResonanceBurst_Damage_Bonus
  Weapon_Durability = 0
  Weapon_Usable = FALSE
END IF
```

### 剥落の星屑（特殊敵）
- **出現域:** 黄泉の深層、星屑の荒野、終幕手前の高難度遭遇戦。
- **特徴:** 物理・属性を極小化し、数Tick以内に「玉座への帰還引力」が飽和して離脱を試みる。帰還衝動と天の拒絶理が衝突した個体は、短時間だけ異常な熱散逸を起こす。

---

## 12. 新規状態異常とギミック（プレースホルダ）
以下は2026-03-11の議論により追加が提案されたシステム干渉名である。具体的な数値・フラグは `SYS-20` の該当箇所を参照しつつ設計チームで決定する。

| 名称 | 変数/フラグ | 説明 |
| --- | --- | --- |
| 白の宣託 | `State_White_Oath` | 探女が使用。プレイヤーUIの予測線を曲げ、表示と実際の行動を乖離させる。
| 真実の隠匿 | `State_Truth_Obscure` | 豊玉姫が使用。情念依存技発動時にバフ状態を白初期化する。
| 無垢なる配給 | `State_Pure_Provision` | 宇迦之御魂神が使用。味方活魂全快・情念0固定。
| 再生停止の呪い | `State_Regeneration_Block` | 大宜都比売が付与。回復処理が完全に無効化される。
| 死狂いの祖 | `State_Shigurui_Ancestor` | 素戔嗚尊（クリア後）用。高密度連撃と予測攪乱を持つ裏ボス状態。
| 歴史の抹消 | `State_History_Erase` | 瀬織津姫が付与。対象武器の金継ぎ履歴を一時消失。
| 草薙の摩耗 | `State_Kusanagi_Wear` | 日本武尊が使用。攻撃時に味方武器耐久度を吸収して自身回復。

# Note
上記変数の型は `bool` または `int` で構わない。必要に応じて `Duration` / `Cooldown` / `Intensity` を追加する。

- **報酬:** 撃破時は星の砂、低確率で高純度星砂をドロップ。
- **攻略導線:** 命中補助、行動順前倒し、多段Hitを重ねて短時間で削り切る設計。

```
Hakuraku_Damage = max(1, floor(Input_Damage * Hakuraku_Damage_Reduction))
Hakuraku_Escape_Check = (Current_Tick >= Hakuraku_Return_Gravity_Tick)
Hakuraku_EntropyBurst = Hakuraku_Escape_Check AND Sky_System_Rejects_Impurity

IF Hakuraku_Escape_Check THEN
  Enemy_Despawn = TRUE
END IF
```
- `Hakuraku_Damage_Reduction`: 高減衰係数（実値はバランス項で管理）
- `Hakuraku_Return_Gravity_Tick`: 玉座への帰還引力が飽和する判定Tick

### 神のターゲット計算 (God_Ri_Logic)
```
// 各行動順（Tick）開始時、最適ターゲットを計算しUIに予告する
Target = f(Kakkon_current, DEF_current, action_history_weight)
```

**理の学習段階（Ri_Evolution）:**
 | レベル | 参照情報 | 対象 | 
 | --- | --- | --- | 
 | Lv1 (Static) | 現在活魂と防御力のみ | 序盤の神（静止の理） | 
 | Lv2 (Adaptive) | 自傷行動の過去頻度も参照 | 中盤の神（変化への適応） | 
 | Lv2.5 (Psychological) | 同パターンの反復に `Pattern_Penalty` を付与 | イザナギなど終盤の神（結晶化の完成／悲哀からの救済） | 
 | Lv3 (Absolute) | 高い `Noise_Resistance`。`Autonomous_Noise` と `SoulIdea` 級でのみ突破可能 | 別天津神（絶対零度の理） | 

※ アマテラスはこの曲線に含まれない。天岩戸フリーズ解除という専用イベントで処理される。

### うかみ自律介入と独立リソース (Ukami_Autonomous_Logic)
第4幕（黄泉・常世）で参戦する行者うかみは、プレイヤーの共有リソース（活魂・情念）を使用せず、内部で完結した**独立リソース**で駆動する。
- **Ukami_Internal_Vigor**: 内部でのみ管理される基幹パラメータ。被ダメージや祈祷実行で変動するが、画面上のメインUIゲージには影響しない。
- **Ukami_Internal_Durability**: 祈祷の摩耗量を扱う内部補助パラメータ。値が高いほど高強度介入を連打しにくくなる。`Ukami_Internal_Vigor` へ合算して評価してもよい。
- **Ukami_AutoIntercept**: `Player_Takes_Fatal_Damage` 等の条件下で発動。成功率100%・行動順無視で割り込む。
- **肩代わりロジック**: プレイヤーが受ける `Invasion_Value`（侵食）の上昇を、うかみの `Internal_Vigor` を削ることで無効化する処理。
- **Ukami_Heal_Absolute**: うかみの法力による回復。`Yomotsu_Eat_State` による回復反転の影響を内部的に無効化し、常にプラスの回復値として処理する。
- **地上での制限**: 地上エリアにおいては物理的に参戦不可であり、遠隔守護フラグも存在しない（完全な断絶）。

### 神写し理解度
```
Understand(skill, ally) += action_count * context_bonus
context_bonus: Critical_Kakkon → x2.0 / Disadvantage_Match → x1.5
IF Understand >= Threshold → ミコトが該当技を習得

// 第4幕以降: うかみが自律NPCの場合も学習対象として扱う
IF ally == UKAMI_GYOJA AND StoryFlag.UKAMI_RETURNED_YOMOTSU THEN
  Understand(skill, UKAMI_GYOJA) += action_count * context_bonus
END IF
```

### 神写し・形代連結補正
```
IF Mikoto_FixedGear_Gauntlet_Equipped AND Katashiro_Equipped_Count > 0 THEN
  Understand(skill, ally) += floor(Damage_Taken_Sum * Linked_ShinUtsushi_Resonance_Mult)
END IF
```

### 黄泉戸喫・侵食ゲージ
> 現在ステータス: **仕様検討中**。摂取タイミング、入力導線、侵食処理の最終仕様は確定していない。

```
// 黄泉戸喫はプレイヤー操作による摂取コマンドを持たない。
// 代わりに Ukami_Autonomous_Eat() が内部タイマー／条件で自動呼び出され、
// 侵食ゲージの進行を一時停止する。プレイヤーUIにYomotsuコマンドは表示されない。

// サンプルロジック:
IF CurrentLocation == "YOMOTSU" THEN
    INVASION_GAUGE = min(Max_Invasion, INVASION_GAUGE + Invasion_Increase_Rate)
END IF

FUNCTION Ukami_Autonomous_Eat()
    IF Ukami_Satiation > 0 AND INVASION_GAUGE > 0 THEN
        Ukami_Satiation -= Ukami_Eat_Cost
        INVASION_GAUGE = max(0, INVASION_GAUGE - Ukami_Eat_Cooldown)
        // 画面演出トリガー: うかみが泥の供物を咀嚼するアニメ
    END IF
END FUNCTION

// 暫定方針: 侵食ゲージ計算と解除条件は設計レビューまで確定値を持たない
// Turn_Invasion_Delta / Yomotsu_Eat_State / Invasion_Value の更新式は保留
```

### フィールド位相（無菌の帳 / 血の泥沼）
```
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

### 共鳴（ユニゾン）計算
```
// 行動順（Tick）が回ってくる前に割り込んで発動する先制攻撃
Resonance_Attack_Damage = Base_Weapon_Damage * ResonanceRate
// 発動条件A: タイムライン上で行動順（Tick）が連続しており、かつ同カテゴリ（槍・鉾 / 打撃 等）の技を選択
// 発動条件B: [第4幕] ミコトの神写し技 ＋ うかみNPCの行動重複 → 確定発動
```

### 代受苦発動・記録遷移
```
// 任意タイミングで発動可（使用可能武器のみ）
Daijuku_Trigger → Weapon_Durability = 0（特大ダメージ付与 / 発動後は武器破損・使用不可）

// 非自発的な耐久尽き（代受苦不使用）
Durability_Zero_Natural → Weapon_Durability = 0（ダメージ特典なし / 武器破損・使用不可）

// 破損武器の復旧
IF Weapon_Durability <= 0 THEN
  Weapon_Usable = FALSE
END IF
IF Repair_Level >= 1 THEN
  Weapon_Usable = TRUE
END IF

// 極大代受苦（Is_Destiny_Battle かつ付喪神化済み武器限定）
IF Can_Use_Extreme_Daijuku THEN
  Item_Instance = DELETE_PERMANENTLY
  Generate(Core_of_Regret)
END IF

// 付喪神化（禁忌鍛造）: 情念の核は必須条件ではない
Tsukumogami_Awakening_Forge =
  Can_Use_Tsukumogami_Awakening
  AND Kintsugi_LogDensity >= TsukumogamiAwakeThreshold
  AND Kintsugi_Material_StarSand_Count >= Required_StarSand_Count

IF Tsukumogami_Awakening_Forge THEN
  Target_Weapon.Is_Tsukumogami = TRUE
  Target_Weapon.TsukumogamiState = "Musubi"
END IF

// 情念の核は「極大代受苦後の継承素材」として扱う（付喪神化の前提条件にはしない）
Tsukumogami_Inheritance_Forge =
  Can_Use_Tsukumogami_Awakening
  AND Item(Core_of_Regret).Exists
  AND Base_Weapon_ID != Core_of_Regret.Source_Weapon_ID

IF Tsukumogami_Inheritance_Forge THEN
  New_Weapon.Inherited_Traits = Core_of_Regret.Stored_Traits
  New_Weapon.Inherited_Memory = Core_of_Regret.Stored_LogDensity
  Consume(Core_of_Regret)
END IF
```

**代受苦（剣塚の共鳴）威力計算式:**
```
Sword_Mound_Damage = Base * (
  Global_Daijuku_Count * Log_Density_Sum
  + Repair_Factor * Global_Kintsugi_Count
  + Usage_Factor * Cumulative_Durability_Hours
) * (Max_Durability / max(1, Current_Durability))^2
```
- `Global_Kintsugi_Count`: 累計金継ぎ回数（修復の歴史が威力に加算される）
- `Cumulative_Durability_Hours`: 一本の武器を使い続けた総時間

### 活魂・情念消費型攻撃（タチバナ・マヒト等）
```
Damage = Base * (1 + Resource_Cost_Mult * (MaxKakkon - CurrentKakkon + ConsumedJonetsu))
```
- `Kakkon_Cost_Attack` として `Intentional_Cost` の一種に分類。神AI的には通常摩擦と区別して管理。

---

## 2. マスター記録定義

### Equipment_Slot_Master（可変スロット制）
 | Slot_ID | 名称 | 内容 | 属性フラグ | 
 | --- | --- | --- | --- | 
 | `MAIN_ARM` | 主腕 | 直接攻撃を担うメインスロット。 | `1H` / `2H` | 
 | `SUB_ARM` | 副腕 | ノイズ具スロット。主腕が `2H` の場合は封印される。 | `1H` / `LOCKED_BY_2H` | 
 | `SHOZOKU` | 装束 | 防御衣服。傷跡が防御力(PTG)になる。 | `UNIQUE` | 
 | `KATASHIRO` | 形代 | 遺品・未練。最大2個。 | `STACKABLE_2` | 
| `FIXED_GEAR` | 固定装具 | スロットを消費しない特殊枠。ミコトは初期状態から空の受け皿を保持し、葛城山以降の継承手甲が常駐する。八咫鏡は手甲上に積層される拡張マウントとして扱い、装備スロット圧縮は発生しない。ワカヒコの矢筒・予備弦束も固定装具として扱う。 | `SLOTLESS` | 

> **注:** 赤いスカーフは装備スロットとは無関係の永続装飾／イベントキーとして扱う。

### Field_Environment_Master（戦場位相）
 | Field_State | 名称 | 効果 |
 | --- | --- | --- |
 | `STERILE_CURTAIN` | 無菌の帳 | 回復効率低下、自傷コスト上昇、静止系異常の付与率上昇 |
 | `BLOOD_MUDPIT` | 血の泥沼 | 回復反転圧上昇、情念蓄積増幅、耐久コスト補正 |

### Item_Master（主要フラグ）
 | フィールド | 説明 | 
 | --- | --- | 
 | `Slot_Type` | どのスロットに帰属するかを指定 | 
| `Core_of_Regret` | 極大代受苦後の情念の核。元の武器IDと特性を保持。付喪神化の必須条件ではなく、継承鍛造時の追加素材として扱う（星の砂と混同させない）。付喪神武器を破壊することで必ず生成され、それを保存しておけば同じ魂を別武器に移すことが可能なため、愛着のある付喪神を何度でも用いるための鍵ともなる。 | 
 | `Ame_no_Murakumo` | スサノオの遺産。`Global_Daijuku_Log_Data` を参照して威力変動。裏ボス撃破後に `Rinne_no_Kintsugi=true` フラグが解放され、致命傷時に自動過熱して持ち主を庇う機能が有効化される | 
| `Mirror_Reflect_Class` | 鏡系装備の反射クラス。`ATTACK_ONLY` / `LIMITED_LOGIC` / `OFF` を持つ |

### Item_State_Extension（武器インスタンス付加情報）
 | フィールド | 説明 | 
 | --- | --- | 
| `TraumaLogDensity` | 履歴密度（付喪神覚醒・付喪神強度に影響） | 
| `TsukumogamiState` | `Dormant` / `Kibutsu`（棄物敵化） / `Musubi`（付喪神覚醒） | 
| `Is_Tsukumogami` | 付喪神化フラグ。`TRUE`の場合再度の極限代受苦は情念の核を生成せず粉砕される | 
 | `AbandonFlag` | 遺棄判定。`TRUE`で棄物化進行が開始 | 
| `HakurakuBonusDrop` | 剥落の星屑撃破時のドロップ倍率補正 | 
| `Linked_ShinUtsushi_Resonance` | 形代・固定装具・神写し理解度を連結する補助フラグ | 
| `FixedGearMountTier` | 固定装具の積層段階。`GAUNTLET_BASE` / `GAUNTLET_WITH_YATA` を保持 | 

### Enemy_Master（主要ボス定義）
 | ID | 名称 | 特殊仕様 | 
 | --- | --- | --- | 
 | `Amaterasu_Core_OS` | 天照大御神 | 戦闘対象ではなく「システムフリーズ状態」管理プロセス。天岩戸解除イベントで制御。 | 
| `Takemikazuchi_Enforcer` | タケミカヅチ | 予告UI「裁きの神雷」。継承手甲に刻まれた猿田の破岩撃による一度きりの防御イベントをトリガーする。 | 
 | `Tsukuyomi_AntiVirus` | 月読命 | 代謝（回復）行動で `ActionError` 移行。確定全滅技「永遠の月食」時に、カガセオ乱入イベントで無敵状態を物理剥離する。 | 
| `Kagaseo_Star_God` | カガセオ | 物理装甲ではなく高圧の情念でダメージ計算。砕かれた玉座への帰還引力と天の拒絶理が衝突し、特殊HP減算（暴走散逸）が発生する。 | 
 | `Boss_AmenoIwatowake` | アメノイワトワケ | `Damage_Multiplier = 0.0` 固定。`Event_Noise_Overload` でのみ撃破扱い。 | 
 | `Izanagi_Crystallizer` | 伊邪那岐命 | 大いなる悲哀と完璧な拒絶の体現。UI予測は完璧であり、情動による「揺らぎ」を最も排除した究極の学習型AI（Lv2.5）。 | 
| `Boss_Yamata_no_Ubusuna` | 澱神・八岐の産土 | ステータスが `Global_Daijuku_Log_Data` と `Tsukumogami_Awakening_Craft_Count` で動的スケーリング。殻破壊後にUIジャック状態へ移行。 | 
 | `Boss_Yakusa_no_Ikazuchi` | 八雷神 | クリア後限定。行者還しの専用3フェーズ進行に従う。 | 
| `Boss_Susanoo` | スサノオ | 高耐久・高火力の正統派裏ボス。勝利条件は `Boss_HP <= 0` のみ。 | 
| `Hakuraku_Stardust` | 剥落の星屑 | 高減衰・高回避・帰還Tick持ち。短期撃破時に星砂報酬が増える。 |

### Enemy_Behavior_Tag
 | タグ | 対象 | 
 | --- | --- | 
 | `Predictive_Fixed` | 白化神 | 
 | `Predictive_Broken` | 澱神 | 
 | `Predictive_Fluctuating` | 荒魂獣 | 
 | `Trauma_Resentment` | 棄物 | 
 | `Pseudo_Perfect_With_Gap` | 擬神兵 | 
| `SkillLock_Enforcer` | 凍結の真空を扱う白化神上位個体 |
| `Field_Overwriter` | 無菌の帳 / 血の泥沼を展開する個体 |

### 神社・祠関連記録
 | マスター | 主要フィールド | 
 | --- | --- | 
 | `Shrine_Master` | `ShrineID`, `Type` (`JINJA`/`HOKORA`), `Prayer_Points_Base`, `Mitama_Slot` | 
 | `Shrine_Faith_Master` | 御霊ごとの恩恵（バフ・神写しツリー解放） | 
 | `Shrine_Network_Data` | `Total_Prayer_Points`（受容力）, `Connected_Shrines`（開通済みIDリスト）, `Unlocked_Buffs` | 

### Forge_Access_Rule_Master（鍛造アクセス制御）
 | フィールド | 説明 |
 | --- | --- |
 | `Context` | `CAMP` / `BASE` / `SHRINE_FORGE` |
 | `Maintenance_Level` | その地点で実行可能な上限Lv（0〜3） |
 | `RequireMahito` | マヒト同行必須か |
 | `RequireFlag` | 解禁に必要なStoryFlag |

### Maintenance_Level_Master（武具整備段階）
 | Level | 名称 | 主機能 |
 | --- | --- | --- |
 | `0` | 泥拭い | 微量耐久回復のみ、履歴定着なし |
 | `1` | 金継ぎ | 全回復、履歴定着、成長反映 |
| `2` | 付喪神化 | 星の砂金継ぎ履歴が閾値を超えた武器へ禁忌鍛造を行い、宿りかけた付喪神を顕現 |
 | `3` | 神話的錬成 | 神器作成、終盤限界突破 |

### Attribute_Master（属性定義）
+
+### Status_Effect_Master（状態異常定義）
+ | Effect_ID | 名称 | 説明 |
+ | --- | --- | --- |
+ | `POISON` | 毒 | 毎Tick活魂を減少させる継続ダメージ |
+ | `BAD_POISON` | 猛毒 | 毒の強化。復帰困難。
+ | `PARALYSIS` | 麻痺 | 一定確率で行動不能 |
+ | `SLEEP` | 睡眠 | 次自身Tickまで行動不能 |
+ | `CONFUSION` | 混乱 | 行動がランダム化 |
+ | `CHARM` | 魅了 | 味方への攻撃を強制 |
+ | `BLIND` | 暗闇 | 命中率低下 |
+ | `DESEASE` | 幻惑 | 属性耐性低下 |
+ | `REST` | 休み | 1ターン確定行動不能 |
+ | `CURSE` | 呪い | 装備効果無効化 |
+ | `INSTANT_KILL` | 即死 | 条件で一撃死亡 |
+ | `SKILL_SEAL` | 封印 | 特技使用不可（凍結の真空含む） |
+ | `CRYSTALLIZE` | 琥珀化 | 完全停止状態（消滅扱い） |

 | Attribute_ID | 名称 | 説明 |
 | --- | --- | --- |
 | `FIRE` | 炎 | 焼却・灼熱系の干渉 |
 | `ICE` | 氷 | 冷却・停滞系の干渉 |
 | `WIND` | 風 | 断裂・流動系の干渉 |
 | `THUNDER` | 雷 | 貫通・高電位系の干渉 |
 | `EARTH` | 土 | 重圧・地脈系の干渉 |
 | `WATER` | 水 | 浸食・波動系の干渉 |
 | `LIGHT` | 光 | 浄化・照射系の干渉 |
 | `DARK` | 闇 | 呪詛・侵食系の干渉 |
 | `NONE` | 無属性 | 純粋な質量・摩擦・打撃圧。属性相性の影響を受けにくい |

> 属性は相性計算レイヤーであり、術式駆動リソース（三条の熱源）とは分離して扱う。

### その他マスター
 | マスター | 目的 | 
 | --- | --- | 
 | `Skill_Master` | 固有スキル・神写し可否・理解度閾値・共鳴タグ | 
 | `Kintsugi_Master` | 修復素材と付与特性（被ダメ履歴参照）定義 | 
 | `Daijuku_Master` | 武器消滅時に生成する「魂のイデア」テーブル。クリア後は `Infinite_Idea_Chain` 解放。 | 
 | `Tsukumogami_Awakening_Master` | `Awaken_Threshold_LogDensity`, `Awaken_Required_Kintsugi_MaterialKinds`, `Musubi_AutoAction_Chance`, `Kibutsu_Spawn_Weight_By_Area` | 
| `Yomotsu_Eat_Master` | 黄泉戸喫の摂取タイミング、侵食ゲージ閾値、食材ID、回復反転係数、キャラ別耐性、適用範囲、解除条件を管理する。現在は仕様検討中のため確定値を持たない。 | 
 | `FastTravel_Master` | 脈継ぎ演出・移動中掛け合いセリフ管理 | 
 | `Sea_Exploration_Master` | クリア後専用。海ノード生成ルール・サルベージテーブル・幻曜の代受苦コスト定義 | 
| `Field_Environment_Master` | 戦場位相（無菌の帳 / 血の泥沼）の効果定義 |
| `Mirror_Reflection_Master` | 反射可能干渉の分類、対象、反射率、反射不可例外を管理 |

---

## 3. Story_Flag_Master（進行フラグ一覧）

物語のジェットコースター構造（うかみ離脱→偽終幕→黄泉帰還）をゲーム内トリガーとして再現する。

 | フラグ名 | 発火タイミング | 
 | --- | --- | 
 | `UKAMI_JOINED_EARLY` | うかみがアマでパーティ合流 | 
| `MAHITO_JOINED_ACT2` | 第2幕・灼熱たたら場でマヒト加入（分岐A/Bいずれでも成立。野営Lv1/拠点Lv2解禁） |
 | `KAGUTSUCHI_QUELLED` | 灼熱たたら場での付喪神顕現がカグツチ残滓を呼び覚まし、プレイヤーがこれを鎮魂した瞬間に立つフラグ。Lv2解放の前提にも連動。 |
 | `WHITE_CORRIDOR_CLEARED` | 白堊の回廊で白化神の防壁を突破（意図的な過負荷イベントの克服、レベル2探索トリガー） |
 | `MAHITO_FIELD_LV2_UNLOCKED` | マヒト個別イベント「野鍛冶の誓い」達成（野外Lv2解禁） |
 | `SHRINE_FORGE_LV3_UNLOCKED` | 大型神社の鍛造拡張完了（Lv3解禁） |
| `TACHIBANA_JOINED_ACT2` | 忘却の海食洞でタチバナが加入（分岐A/Bいずれでも成立） | 
| `ROUTE_A_ORDER_RESOLVED` | 分岐A（忘却の海食洞→灼熱たたら場）成立 | 
| `ROUTE_B_ORDER_RESOLVED` | 分岐B（灼熱たたら場→忘却の海食洞）成立 | 
| `UKAMI_LEFT_KATSURAGI` | 葛城山での一次離脱（`MAHITO_JOINED_ACT2` と `TACHIBANA_JOINED_ACT2` の両成立後） | 
 | `WAKAHIKO_ANTAGONIST_PHASE` | ワカヒコによる執拗な追撃・対立期間 | 
 | `WAKAHIKO_JOINED_ACT3` | 天望の天守でのワカヒコ加入 | 
 | `ACT3_KAGASEO_RESONANCE` | 第3幕の一度限りのカガセオ意識による加勢イベント | 
 | `TSUKUYOMI_TOWER_DEPLOYED` | 静謐の塔建造・浄化プロトコル起動 | 
 | `TSUKUYOMI_FAKE_LASBOSS` | ツクヨミ撃破・偽終幕祝祭発生 | 
 | `TSUKUYOMI_CELEBRATION_CONDUCTED` | 偽終幕後の凍結UIジャック開始 | 
 | `UKAMI_RETURNED_YOMOTSU` | 黄泉比良坂でうかみが行者として帰還 | 
 | `KAGASEO_REBOOT_DRIVE_ACQUIRED` | 星屑の荒野（カガセオ戦）でリブート駆動片を獲得 | 
 | `AMENO_IWATOWAKE_FORCED_REBOOT` | 神器とカガセオの駆動片で天岩戸を強制リブート | 
 | `ETERNITY_REJECTED_DEATH_IMPLEMENTED` | 別天津神を破り、ただの人間としての死を受け入れた（エンディング） | 
 | `GYOJAGAESHI_CLEARED` | クリア後「行者還し」完了。うかみを完全フリーメンバー化。 | 
| `SUSANOO_TRIAL_CLEARED` | 根堅洲国スサノオ撃破（活魂削り切り）完了 | 
| `STERILE_CURTAIN_UNLOCKED` | 無菌の帳を展開する敵位相が解放 | 
| `BLOOD_MUDPIT_UNLOCKED` | 血の泥沼位相が解放 | 

### Forced_Inheritance_Rule_Master（葛城山継承の固定習得）
```yaml
TriggerFlag: UKAMI_LEFT_KATSURAGI
TargetCharacter: MIKOTO
ForcedSkillId: INHERITED_TAKEMIKAZUCHI
ForcedSkillName: 猿田の破岩撃
UnderstandLevel: 100
PermanentLearned: true
CanUnequipFromShinUtsushiSlot: false
```

> * 猿田の破岩撃は、武器耐久度に依存せず活魂・情念を大量消費して敵単体へ無属性極大物理ダメージを与える高火力ロマン技である。
> * 追加の継承技（例：泥壁の咆哮によるヘイト固定、獣道の退路による確定逃走）は別途検討/実装予定であり、現仕様では猿田の破岩撃のみが強制習得される。

### Party_Area_Constraint_Master（うかみ拘束ルール）
```yaml
TargetCharacter: UKAMI_GYOJA
LockFromFlag: UKAMI_RETURNED_YOMOTSU
UnlockFlag: GYOJAGAESHI_CLEARED
LockedAreas: [TOKOYO, YOMI_NO_KUNI, YOMOTSU_HIRASAKA, HOSHIKUZU_N_ARANO]
ConstraintMode: CHARACTER_ONLY  # うかみ本人のみ。パーティ全体には適用しない
```

---

## 4. Party_Composition_Master

- 通常: 戦闘枠4・控え枠2
- **第4幕（カガセオ戦・別天津神戦）:** `5th_NPC_Slot` を解放。うかみは命令不可の自律NPCとして常時参戦。
- ※第3幕の「名もなき影の加勢」は常駐スロットではなく、単発イベントスクリプトとして処理する。

---

## 5. バランス調整パラメータ（実数はプレイテストで決定）

 | パラメータ名 | 説明 | 
 | --- | --- | 
 | `Threshold` | 神写し習得閾値 | 
 | `MudWipe_Recovery_Rate` | Lv0泥拭いの回復率（例: 0.3） |
 | `FieldLv2_Unlock_Quest_Req` | 野外Lv2解禁イベントの必要達成量 |
 | `Forge_Lv2_Bonus_Mult` | 拠点Lv2鍛造時の追加補正 |
 | `Forge_Lv3_Mythic_Mult` | Lv3神器錬成時の補正係数 |
 | `ResonanceRate` | 共鳴倍率 | 
 | `FrictionBase` | 基本摩擦係数 | 
| `Tsukumogami_Awakening_Friction_Mult` | 付喪神化時の摩擦倍率（1.5〜3.0） | 
 | `YomotsuInvasionThreshold` | 侵食ゲージ閾値 | 
| `YomotsuRecoveryReversalRate` | 黄泉戸喫時の回復反転係数（プレイヤーは戦闘中一時適用） | 
 | `Tachibana_Kakkon_Cost_Mult` | タチバナの自傷型術の係数 | 
 | `PTG_RareChance` | PTG（外傷後成長）効果発生率 | 
 | `SoulIdeaCarryRate` | 魂のイデア継承率 | 
 | `TsukumogamiAwakeThreshold` | 付喪神覚醒閾値 | 
 | `KibutsuSpawnRate` | 棄物（敵性付喪神）出現率 | 
 | `WildInstinctVariance` | 荒魂獣の行動揺らぎ幅 | 

> **Single Source of Truth**: 上記パラメータの実数値はすべて本ファイルのみで管理する。画面表示・物語表現・UX演出での独自変更を禁止する。

---

## 6. Visual_Prompt_Master（アセット管理メタ記録）

 | フィールド | 値 | 
 | --- | --- | 
 | `PromptSetId` | `LUMINOUS_WASHI_V3` | 
 | `SourcePath` | `../04_Art/ART-40_Art_Direction_and_Assets.md` | 
 | `AnchorId` | `00_STYLE_ANCHOR_LUMINOUS_WASHI` | 
 | `AncientConstraint` | `true`（西洋甲冑・SF意匠を禁止） | 
 | `WatercolorBleedEnforced` | `true` | 
 | `AnimeStyleBlocked` | `true` | 
 | `BossPresenceBias` | `TSUKUYOMI_HIGH`（偽ラスボス威圧感の優先） | 
 | `KagaseoHumanityBias` | `true`（岩塊主体を避け人間的骨格を優先） | 
 | `DeityRegaliaOpulence` | `HIGH`（アマテラス・ツクヨミの儀礼装束の華やかさ下限） | 