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

// システム変数
`DualStanceActive` : BOOLEAN
  // ミコト専用フラグ。特定の技・状態でのみ真となり、
  // 仮想的な双腕スタンスを発現させる。装備スロットとは無関係。
`Mikoto_Gauntlet_Permanent` : BOOLEAN
  // 継承手甲がミコトに恒久的に接続されたことを示す。
  // 一度真になればそれ以降変更されない。装備欄とは無関係。



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

// 追加: 主腕一つという設計方針により、従来の「副腕装備」概念は廃止された。
// ミコトの二刀流は物理的なオフハンド装着ではなく、
// 特定術式発動時に瞬間的に `DualStanceActive` フラグが立つ「仮想的双腕状態」として
// モデル化される。スタンス乗数1.3はこのフラグに基づき適用される。



### 武器耐久度（Durability）モデル
```
Durability_new = max(0, Durability_old - (
    Base_Weapon_DurabilityCost * Stance_Multiplier
  + Skill_Durability_Cost
  + Intentional_Cost
))
```
- `Stance_Multiplier`: 
  - **両手持ち（2H）**: **1.5**（重量武器の質量衝突で摩耗が最も激しい）
  - **一刀流（1H）**: **1.0**（標準運用。攻撃力と摩耗の基準）
  - **二刀流 / 仮想双腕**: **1.3**（`DualStanceActive == TRUE` 時のみ適用される特別スタンス。手数で押す代わりに摩耗ペースが上がる）

// `DualStanceActive` はミコト専用の一時フラグであり、
// 技や状態異常でのみ立ち上がる。オフハンド装備は永続的に存在しない。
- `Intentional_Cost`: プレイヤーが任意に支払う自傷（活魂）・情念放出コスト。神の計算ノイズの源泉。
- **Tsukumogami_Awakening_Penalty**: 付喪神化武器は耐久減少係数が **1.5〜3.0倍** に跳ね上がる（強力だが即消耗する）。

### 構え（Stance Logic）
```
IF MainWeapon.Type == "2H" THEN
  Stance_Type = TWO_HANDED
  Stance_Multiplier = 1.5
  PTG_Penetration_Rate = TWO_HANDED_PTG_Penetration_Rate
  Counter_Stability_Bonus = TWO_HANDED_Counter_Stability_Bonus
END IF

IF MainWeapon.Type == "1H" AND DualStanceActive == FALSE THEN
  Stance_Type = SINGLE_BLADE
  Stance_Multiplier = 1.0
  Single_Blade_Grip_Mode = STANDARD_OR_MOROTE
  Mud_Intuition_Success_Mult = SINGLE_BLADE_Mud_Intuition_Success_Mult
END IF

// ミコト専用の仮想二刀流スタンス
IF Character == MIKOTO AND DualStanceActive == TRUE THEN
  Stance_Type = VIRTUAL_DUAL_BLADE
  Stance_Multiplier = 1.3
  Prophecy_Scramble_Intensity = DUAL_WIELD_Scramble_Intensity
  Hakuraku_HitCount_Bonus = DUAL_WIELD_Hakuraku_HitCount_Bonus
  // フラグは対応する技／状態が終了したタイミングで自動解除される。
END IF

// すべての非ミコトは副腕装備自体を保持できない。

// ワカヒコ特例: 仕込み短刀時の確定反撃状態
IF Character == WAKAHIKO AND MainWeapon.ID == "CONCEALED_DAGGER" THEN
  State_Wakahiko_Focused_Retaliation = TRUE
  Evasion_Rate += WAKAHIKO_Precision_Evasion_Bonus
  IF Evasion_Success == TRUE THEN
    Counter_Proc_Rate = 1.0  // 生存の足掻きは条件成立時100%確定
  END IF
END IF

```

- **補足:** `1H` 刀は通常一刀流として扱い、必要に応じて両手で握り込む「諸手」は `SINGLE_BLADE` の安定運用に内包する。明示的な二刀流ロジックはミコト専用。

### ワカヒコ固有パッシブ（返し矢の呪い）
```
// 弓攻撃時に常時適用
IF Character == WAKAHIKO AND MainWeapon.Category == "BOW_RANGED" THEN
  Jonetsu_Ratio = clamp(Jonetsu_Value / Jonetsu_Max, 0.0, 1.0)
  Bow_Damage_Mult = 1.0 + (Jonetsu_Ratio * WAKAHIKO_KAESHIYA_Damage_Mult)
  Self_Recoil_Damage = floor(Bow_Base_Damage * Jonetsu_Ratio * WAKAHIKO_KAESHIYA_Recoil_Mult)
  Apply_Damage(Target, floor(Bow_Base_Damage * Bow_Damage_Mult))
  Kakkon_Value = max(0, Kakkon_Value - Self_Recoil_Damage)
END IF

// 生存の足掻きは条件成立時100%反撃
IF Character == WAKAHIKO AND MainWeapon.ID == "CONCEALED_DAGGER" AND Evasion_Success == TRUE THEN
  Survival_Scramble_Guaranteed = TRUE
END IF
```

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
Can_Use_Extreme_Daijuku = Can_Use_Tsukumogami_Awakening
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
Hakuraku_Despawn_Window = 3

IF Hakuraku_EntropyBurst THEN
  Apply_Area_HeatScatter(Hakuraku_HeatScatter_Burst_Damage)
END IF

IF Hakuraku_Escape_Check AND Hakuraku_Despawn_Window > 0 THEN
  Hakuraku_Despawn_Window -= 1
END IF

IF Hakuraku_Escape_Check AND Hakuraku_Despawn_Window <= 0 THEN
  Enemy_Despawn = TRUE
END IF
```
- `Hakuraku_Damage_Reduction`: 高減衰係数（実値はバランス項で管理）
- `Hakuraku_Return_Gravity_Tick`: 玉座への帰還引力が飽和する判定Tick
- `Hakuraku_Despawn_Window`: 熱散逸発生後に与える攻撃猶予Tick

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
 | Lv3 (Absolute) | 高い `Noise_Resistance`。`Autonomous_Noise` と `Core_of_Regret` 級でのみ突破可能 | 別天津神（絶対零度の理） | 

※ アマテラスはこの曲線に含まれない。天岩戸フリーズ解除という専用イベントで処理される。

### うかみ自律介入と独立リソース (Ukami_Autonomous_Logic)
第4幕（黄泉・常世）で参戦する行者うかみは、プレイヤーの共有リソース（活魂・情念）を使用せず、内部で完結した**独立リソース**で駆動する。
- **Ukami_Internal_Vigor**: 内部でのみ管理される基幹パラメータ。被ダメージや祈祷実行で変動するが、画面上のメインUIゲージには影響しない。
- **Ukami_Internal_Durability**: 祈祷の摩耗量を扱う内部補助パラメータ。値が高いほど高強度介入を連打しにくくなる。`Ukami_Internal_Vigor` へ合算して評価してもよい。
- **Ukami_AutoIntercept**: `Player_Takes_Fatal_Damage` 等の条件下で発動。成功率100%・行動順無視で割り込む。
- **肩代わりロジック**: プレイヤーが受ける `Invasion_Value`（侵食）の上昇を、うかみの `Internal_Vigor` を削ることで無効化する処理。
- **Ukami_Heal_Absolute**: うかみの法力による回復。`Yomotsu_Eat_State` による回復反転の影響を内部的に無効化し、常にプラスの回復値として処理する。
  // 優位性: `Field_State == BLOOD_MUDPIT` による Heal_Value 乗算は
  // 反転適用前に評価されるため、Ukami_Heal_Absolute は最終値へ
  // 直接加算され、回復反転効果を貫通する。

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
IF Mikoto_Gauntlet_Permanent == TRUE AND Katashiro_Equipped_Count > 0 THEN
  Understand(skill, ally) += floor(Damage_Taken_Sum * Linked_ShinUtsushi_Resonance_Mult)
END IF
```

### 黄泉戸喫・黄泉の呪い（確定仕様）
```
// 発動導線: フィールドアイテム「黄泉の泥果実」の任意使用
IF Use_Item == Yomotsu_Mud_Fruit THEN
  // 回復基準値は減衰前の最大値を用いる。摂取は侵食ゲージへ影響しない。
  Kakkon_Value = Kakkon_Max
  Jonetsu_Value = Jonetsu_Max
  Apply_State(YOMOTSU_CURSE)
END IF

// 黄泉の呪い: 永続デバフ
IF State_Yomotsu_Curse == TRUE THEN
  MaxKakkon = max(Min_MaxKakkon_Floor, floor(MaxKakkon * Yomotsu_MaxKakkon_Decay_Mult))
  Disable_Standard_Recovery = TRUE  // 通常アイテム・通常休息回復を無効化
END IF

// 解除手段: 野営地の行者うかみのみ
IF CurrentContext == CAMP AND NPC == UKAMI_GYOJA AND Command == "Ukami_Camp_Purification" THEN
  Remove_State(YOMOTSU_CURSE)
  Disable_Standard_Recovery = FALSE
END IF

// 補足: うかみの自律摂取は侵食ゲージ遅延の内部処理であり、上記呪い仕様とは別系統
FUNCTION Ukami_Autonomous_Eat()
  IF Ukami_Satiation > 0 AND INVASION_GAUGE > 0 THEN
    Ukami_Satiation -= Ukami_Eat_Cost
    INVASION_GAUGE = max(0, INVASION_GAUGE - Ukami_Eat_Cooldown)
    // 在庫の黄泉の泥果実は消費しない。行者の法力による内部処理。
  END IF
END FUNCTION
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

// 極大代受苦（付喪神化済み武器のみ。全戦闘で発動可能）
IF Can_Use_Extreme_Daijuku AND Target_Weapon.Is_Tsukumogami == TRUE THEN
  Item_Instance = DELETE_PERMANENTLY
  IF Target_Weapon.CoreRegret_Extractable == TRUE THEN
    Generate(Core_of_Regret)
  END IF
END IF

// 付喪神化（禁忌鍛造）: 情念の核は必須条件ではない
// ただし、付喪神化直後に即座に武器を破壊しても
// 核は生成されない。再抽出が可能になるのは、
// 武器が付喪神状態で少なくとも1Tick経過し、かつ
// 耐久度>0である状態を一度でも通過した後である。
Tsukumogami_Awakening_Forge =
  Can_Use_Tsukumogami_Awakening
  AND Kintsugi_LogDensity >= TsukumogamiAwakeThreshold
  AND Kintsugi_Material_StarSand_Count >= Required_StarSand_Count

IF Tsukumogami_Awakening_Forge THEN
  Target_Weapon.Is_Tsukumogami = TRUE
  Target_Weapon.TsukumogamiState = "Musubi"
  Target_Weapon.CoreRegret_Extractable = TRUE
END IF

// 情念の核は「極大代受苦後の継承素材」として扱う（付喪神化の前提条件にはしない）
Tsukumogami_Inheritance_Forge =
  Can_Use_Tsukumogami_Awakening
  AND Item(Core_of_Regret).Exists
  AND Base_Weapon_ID != Core_of_Regret.Source_Weapon_ID

IF Tsukumogami_Inheritance_Forge THEN
  New_Weapon.Inherited_Traits = Core_of_Regret.Stored_Traits
  New_Weapon.Inherited_Memory = Core_of_Regret.Stored_LogDensity
  New_Weapon.CoreRegret_Extractable = FALSE
  Consume(Core_of_Regret)
END IF

// 魂の摩耗（Soul Attrition）
// 核継承直後の新器を即座に破壊しても核は再生成されない。
// 再抽出するには、新器で金継ぎ履歴を再び閾値まで蓄積し、付喪神化を経由する必要がある。
IF New_Weapon.CoreRegret_Extractable == FALSE AND New_Weapon.Is_Tsukumogami == FALSE THEN
  CoreRegret_Regen_Allowed = FALSE
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
 | `SHOZOKU` | 装束 | 防御衣服。傷跡が防御力(PTG)になる。 | `UNIQUE` | 
 | `KATASHIRO` | 形代 | 遺品・未練。最大2個。 | `STACKABLE_2` | 

> **注:** 赤いスカーフは装備スロットとは無関係の永続装飾／イベントキーとして扱う。

### Character_Carried_Items（常時携行物）
| Character_ID | 常時携行物 | 仕様上の扱い |
| --- | --- | --- |
| `MIKOTO` | 継承手甲、八咫鏡（終盤） | 人物設定に紐づく常時携行物。装備枠計算の対象外。手甲は接続後永久に `Mikoto_Gauntlet_Permanent = TRUE` となり、取り外し・移動は発生しない。 |
| `UKAMI` | 法螺貝 | 常時携行物として術式演出に使用。 |
| `SUKUNA` | 石乳鉢 | 足元据え置き前提の常時携行物。 |
| `UZU` | 神楽面 | 舞と攪乱術式の常時携行物。 |
| `TACHIBANA` | 呪具・土偶 | 自傷転写術式の常時携行物。 |
| `MAHITO` | 炉滓袋、鍛冶布 | 鍛造・修復演出の補助。主武器には含めない。 |
| `WAKAHIKO` | 矢筒、予備の弦束 | 弓術補給の常時携行物。 |

### Weapon_Category_Master（武器カテゴリ統合）
| Category_ID | 名称 | 代表武器 | 主な使用者 |
| --- | --- | --- | --- |
| `BLADE` | 刃 | 直刀、斥候刀、舞短刀、仕込み短刀 | ミコト、うかみ、ウズ、ワカヒコ |
| `SPEAR_HALBERD` | 槍・鉾 | 儀礼の長槍、石鉾、流木槍、海人銛 | ミコト、うかみ、タチバナ |
| `BLUNT` | 打撃 | 流木の打ち櫂、大槌、乳棒 | タチバナ、マヒト、スクナ |
| `GOHEI` | 大幣 | 共鳴の御幣、狂騒の荒幣、海淵の忌み幣 | ミコト、ウズ、タチバナ |
| `STAFF` | 杖 | 錫杖 | うかみ |
| `FAN` | 扇 | 鉄扇 | ウズ |
| `BOW_RANGED` | 弓・遠距離 | 天上弓 | ワカヒコ |

### Party_Role_Definition_Master（役割正本）
| Character_ID | 中核役割 | 主腕構成 | いると助かる局面 | 欠けると起きる破綻 |
| --- | --- | --- | --- | --- |
| `MIKOTO` | 共鳴の核 | 刀 / 槍 / 大幣 / 二刀流は専用特例 | 連携を束ねたい時、詰み盤面を反転したい時 | 神写しと役割間の橋渡しが切れる |
| `UKAMI` | 野性の楔 | 斥候=刀/槍、行者=錫杖/槍/刀 | 前線維持、境界固定、敵の進軍停止 | 後衛が守られず隊列が崩れる |
| `SUKUNA` | 劇薬師 | 乳棒のみ、薬は行動として扱う | 状態異常対処、回復、耐性剥がし | 長期戦で回復と補助が足りなくなる |
| `MAHITO` | 武具の守護者 | 大槌 / 大やっとこ | 武器破損圧が強い戦闘、装甲剥がしが必要な戦闘 | 修復と搦め手が不足し、武具が先に尽きる |
| `UZU` | 拍子の破壊者 | 鉄扇 / 舞短刀 / 大幣 | 行動順干渉、敵神託の破綻、場の攪乱 | 敵の確定行動を崩せず受け切れない |
| `TACHIBANA` | 執着の打ち手 | 流木槍 / 流木の打ち櫂 / 大幣 | 自傷貫通、拘束、泥沼化した近距離戦 | 硬い敵を削り切れず押し負ける |
| `WAKAHIKO` | 境界の狙撃手 | 天上弓 / 仕込み短刀 | 遠距離阻害、部位破壊、危機時の差し込み | ギミック解除と詠唱阻害が不足する |

### Field_Environment_Master（戦場位相）
 | Field_State | 名称 | 効果 |
 | --- | --- | --- |
 | `STERILE_CURTAIN` | 無菌の帳 | 回復効率低下、自傷コスト上昇、静止系異常の付与率上昇 |
 | `BLOOD_MUDPIT` | 血の泥沼 | 回復反転圧上昇、情念蓄積増幅、耐久コスト補正 |

### Item_Master（主要フラグ）
 | フィールド | 説明 | 
 | --- | --- | 
 | `Slot_Type` | どのスロットに帰属するかを指定 | 
| `Core_of_Regret` | 極大代受苦で `Is_Tsukumogami == TRUE` の武器を破壊した時のみ生成される情念の核。付喪神化の必須条件ではなく、継承鍛造時の追加素材として扱う（星の砂と混同させない）。 | 
 | `Ame_no_Murakumo` | スサノオの遺産。`Global_Daijuku_Log_Data` を参照して威力変動。裏ボス撃破後に `Rinne_no_Kintsugi=true` フラグが解放され、致命傷時に自動過熱して持ち主を庇う機能が有効化される | 
| `Mirror_Reflect_Class` | 鏡系装備の反射クラス。`ATTACK_ONLY` / `LIMITED_LOGIC` / `OFF` を持つ |
| `Yomotsu_Mud_Fruit` | 黄泉の泥果実 | 使用効果＝`Full_Recover(Kakkon, Jonetsu)` + `Apply_State(YOMOTSU_CURSE)` |

### Item_State_Extension（武器インスタンス付加情報）
 | フィールド | 説明 | 
 | --- | --- | 
| `TraumaLogDensity` | 履歴密度（付喪神覚醒・付喪神強度に影響） | 
| `TsukumogamiState` | `Dormant` / `Kibutsu`（棄物敵化） / `Musubi`（付喪神覚醒） | 
| `Is_Tsukumogami` | 付喪神化フラグ。`TRUE`時のみ極大代受苦で情念の核抽出判定を行う | 
| `CoreRegret_Extractable` | 情念の核抽出可能フラグ。継承直後は `FALSE` 固定。再抽出には新器で履歴を再蓄積し再付喪神化が必要 | 
 | `AbandonFlag` | 遺棄判定。`TRUE`で棄物化進行が開始 | 
| `HakurakuBonusDrop` | 剥落の星屑撃破時のドロップ倍率補正 | 
| `Linked_ShinUtsushi_Resonance` | 形代・常時携行物・神写し理解度を連結する補助フラグ | 
| `Mikoto_Carried_Item_State` | ミコト常時携行物の段階。`GAUNTLET_BASE` / `GAUNTLET_WITH_YATA` を保持 | 

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
 | `Boss_Yakusa_no_Ikazuchi` | 八雷神 | クリア後限定。行者還しの専用3フェーズ進行に従う。 <br> **【突入条件式】** <br> `IF (Sum(Party.MaxKakkon) >= Required_Kakkon_Gravity) AND (Sum(Party.MaxJonetsu) >= Required_Jonetsu_Gravity) THEN Allow_Battle = TRUE` | 
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
 | Attribute_ID | 名称 | 説明 |
 | --- | --- | --- |
 | `FIRE` | 炎 | 焼却・灼熱系の干渉 |
 | `ICE` | 氷 | 静止または冷却の干渉を扱う複合属性 |
| `ICE_COOLING` | 人の氷（冷却） | 暴走熱を奪って鎮める。過熱抑制と熱散逸誘発に使う。 |

// 冷却ダメージ倍率は熱散逸効果と連動
IF Target.Status == ICE_COOLING THEN
  Damage_Mult *= IceCooling_HeatScatter_Damage_Mult
END IF
 | `WIND` | 風 | 断裂・流動系の干渉 |
 | `THUNDER` | 雷 | 貫通・高電位系の干渉 |
 | `EARTH` | 土 | 重圧・地脈系の干渉 |
 | `WATER` | 水 | 浸食・波動系の干渉 |
 | `LIGHT` | 光 | 浄化・照射系の干渉 |
 | `DARK` | 闇 | 呪詛・侵食系の干渉 |
 | `NONE` | 無属性 | 純粋な質量・摩擦・打撃圧。属性相性の影響を受けにくい |

#### ICE_Subtype_Master（氷属性の位相分離）
 | Ice_Subtype | 呼称 | 効果定義 |
 | --- | --- | --- |
 | `ICE_STAGNATION` | 神の氷（静止） | 時間・行動を凍結し、琥珀化へ寄せる。天津神の主系統。 |
 | `ICE_COOLING` | 人の氷（冷却） | 暴走熱を奪って鎮める。過熱抑制と熱散逸誘発に使う。 |

```
// 氷の戦術効果
IF Attack.IceSubtype == ICE_COOLING AND Target.Tag == AMATSUKAMI THEN
  Damage_Mult *= IceCooling_vs_Amatsukami_Mult  // 天津神には耐性
END IF

IF Attack.IceSubtype == ICE_COOLING AND Target.Tag == WILDLIFE THEN
  Apply_State(SLOW)
END IF

IF Attack.IceSubtype == ICE_COOLING AND (Target.Tag == DEIGAMI OR Target.Tag == KIBUTSU) THEN
  Apply_State(HEAT_DISSIPATION_BREAK)
  Target.PTG = max(0, Target.PTG - IceCooling_PTG_Reduction)
  Damage_Mult *= IceCooling_HeatScatter_Damage_Mult
END IF
```

> 属性は相性計算レイヤーであり、術式駆動リソース（三条の熱源）とは分離して扱う。

### Status_Effect_Master（状態異常定義）
 | Effect_ID | 名称 | 説明 |
 | --- | --- | --- |
 | `POISON` | 毒 | 毎Tick活魂を減少させる継続ダメージ |
 | `BAD_POISON` | 猛毒 | 毒の強化。復帰困難 |
 | `PARALYSIS` | 麻痺 | 一定確率で行動不能 |
 | `SLEEP` | 睡眠 | 次自身Tickまで行動不能 |
 | `CONFUSION` | 混乱 | 行動がランダム化 |
 | `CHARM` | 魅了 | 味方への攻撃を強制 |
 | `BLIND` | 暗闇 | 命中率低下 |
 | `DESEASE` | 幻惑 | 属性耐性低下 |
 | `REST` | 休み | 1ターン確定行動不能 |
 | `CURSE` | 呪い | 装備効果無効化 | 
 | `INSTANT_KILL` | 即死 | 条件で一撃死亡 | 
 | `SKILL_SEAL` | 封印 | 特技使用不可（凍結の真空含む） | 
 | `CRYSTALLIZE` | 琥珀化 | 完全停止状態（消滅扱い） | 
 | `YOMOTSU_CURSE` | 黄泉の呪い | フィールドで黄泉アイテムを使用した際に付与される永続状態異常。解除手段は `Ukami_Camp_Purification` のみ。 |
| `WAKAHIKO_KAESHIYA_PASSIVE` | 返し矢の呪い | ワカヒコが弓攻撃するたび、情念蓄積比率に応じて威力上昇と自傷反動を同時に発生させる恒常パッシブ。 |

### その他マスター
 | マスター | 目的 | 
 | --- | --- | 
 | `Skill_Master` | 固有スキル・神写し可否・理解度閾値・共鳴タグ | 
 | `Kintsugi_Master` | 修復素材と付与特性（被ダメ履歴参照）定義 | 
 | `Daijuku_Master` | 武器消滅時に生成されうる情念の核（Core_of_Regret）と連動するマスターテーブル。クリア後は `Infinite_Idea_Chain` 解放。 | 
 | `Tsukumogami_Awakening_Master` | `Awaken_Threshold_LogDensity`, `Awaken_Required_Kintsugi_MaterialKinds`, `Musubi_AutoAction_Chance`, `Kibutsu_Spawn_Weight_By_Area` | 
| `Yomotsu_Eat_Master` | 黄泉戸喫の摂取導線、食材ID、全回復値、`YOMOTSU_CURSE` 付与条件、最大活魂減衰係数、通常回復無効化、`Ukami_Camp_Purification` の解除条件を管理する。行者うかみの自律摂取は内部法力のみで処理し、プレイヤー在庫を消費しない。 | 
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
| `MAHITO_JOINED_ACT2` | 第2幕・灼熱たたら場でマヒト加入（白堊の回廊→忘却の海食洞→灼熱たたら場の固定進行後。野営Lv1/拠点Lv2解禁） |
 | `KAGUTSUCHI_QUELLED` | 灼熱たたら場での付喪神顕現がカグツチ残滓を呼び覚まし、プレイヤーがこれを鎮魂した瞬間に立つフラグ。Lv2解放の前提にも連動。 |
 | `WHITE_CORRIDOR_CLEARED` | 白堊の回廊で白化神の防壁を突破（意図的な過負荷イベントの克服、レベル2探索トリガー） |
 | `MAHITO_FIELD_LV2_UNLOCKED` | マヒト個別イベント「野鍛冶の誓い」達成（野外Lv2解禁） |
 | `SHRINE_FORGE_LV3_UNLOCKED` | 大型神社の鍛造拡張完了（Lv3解禁） |
| `TACHIBANA_JOINED_ACT2` | 忘却の海食洞でタチバナが加入（第2幕固定進行） | 
| `ACT2_FIXED_ROUTE_CONFIRMED` | 第2幕固定導線（白堊の回廊→忘却の海食洞→灼熱たたら場）が確定した状態 | 
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
LearnMode: FORCE_AND_SIMULTANEOUS
UnderstandLevel: 100
PermanentLearned: true
UseDedicatedInheritedSlot: true
DoesNotConsumeShinUtsushiSlots: true
ForcedSkills:
  - SkillId: INHERITED_SARUTA_BREAK
    SkillName: 猿田の破岩撃
    Role: 攻撃/剛
    DurabilityCost: 0
    ResourceCost: KAKKON_AND_JONETSU
  - SkillId: INHERITED_HORAGAI_ROAR
    SkillName: 法螺の轟き
    Role: 補助/導
    Effect: PARTY_JONETSU_GAIN_UP
```

> * 猿田の破岩撃は、武器耐久度を消費せず活魂・情念を代償に敵単体へ無属性極大物理ダメージを与える。
> * 法螺の轟きは、うかみの遺志を継いで味方全体の情念上昇率を大幅に引き上げる。

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
 | `Core_of_RegretCarryRate` | 情念の核継承率 | 
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