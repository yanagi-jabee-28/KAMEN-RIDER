# 30 Data and Logic Architecture (データと論理) 〜天降（あまくだ）る御子と、星屑の大地〜

本ドキュメントはEngineer専用の実装要件・変数定義書（Single Source of Truth）である。物語的・情動的な表現はすべて `10_Narrative_and_Characters.md` と `20_Game_Systems_and_Flow.md` に委ね、ここでは変数・フラグ・計算式のみを純粋な形で定義する。バランス数値の変更は必ず本ファイルを唯一の更新点とすること。

---

## 1. コア計算式とリソース体系

### 術式駆動リソース（三条の熱源）
本作に汎用的な「魔法値（MP）」は存在せず、以下の3リソースで術式・状態を管理する。

1. **活魂（Kakkon_Value）**:
    - **定義**: 肉体の生命力と持久力の統合値（事象としての「器」）。主腕の振舞いや被ダメージで減算。
2. **情念（Jonetsu_Stock / Jonetsu_Value）**:
    - **定義**: 未練・執着のバグ燃料。従来の%ゲージではなく、**絶対値ストック**で管理される。
      たとえば最大値を `Jonetsu_Max` として 0〜`Jonetsu_Max` の整数または段階（炎3つ等）を用いる。
      UI上はMPと同様に「残り値が減っていく」形で表示される。
    - **蓄積**: 基本ロジックは変わらず、被ダメージや味方ピンチで増加。
      ```
      Jonetsu_new = min(Jonetsu_Max, Jonetsu_old + floor(Damage_Taken * Char_Factor)
                           + floor(Ally_Critical_Crisis * Sync_Factor))
      ```
      消費時は `Jonetsu_new = Jonetsu_old - Cost` のようにMP同様に減算される。
      ゲームプレイ上は「情念ストック2つだから必殺技が撃てる」と直感的に把握できる。

### 境界状態判定ロジック (Boundary States)
```
IF Kakkon_Value <= 0 AND Jonetsu_Value > 0 THEN
  State_Shigurui = TRUE
  // 物理ダメージ完全無効化・敵AI予測ルート完全遮断
  // 行動順（Tick）が回ってくるごと、または行動ごとに Jonetsu_Value が固有コストで減少
END IF

IF Kakkon_Value > 0 AND Jonetsu_Gauge <= 0 THEN
  State_Karakara = TRUE
  // スキル使用不可・回避率=0・被弾時確定クリティカル
END IF

IF (Kakkon_Value <= 0 AND Jonetsu_Gauge <= 0) OR (Kakkon_Value <= 0 AND Anchor_Equipped_Count == 0) THEN
  State_Dead = TRUE // 泥への還り（完全死）
END IF
```
3. **摩擦熱（Heat）** *（武器耐久度に統合）*:
    - **定義**: 独立リソースとしての摩擦熱ゲージは廃止され、すべて武器の耐久度 `Weapon_Durability` に任せる。
      特技・連続攻撃で従来「熱」が増えていた部分は、代わりに**耐久度直接減少**として計算される。UIは耐久度バーのみを表示し、管理負荷を単一化する。
    - **運用**: 技使用時に発生する「摩擦コスト」が耐久度を削り、耐久度0で『過熱・沈黙』になる。
      その前に金継ぎで回復するか、代受苦で残値を燃料にして大ダメージを撃つかという選択は従来通り。熱蓄積＝耐久減少と見なせば、表現も泥臭く保たれる。

### 武器耐久度（Durability）モデル
```
Durability_new = max(0, Durability_old - (
    Base_Weapon_Heat * Stance_Multiplier
  + Skill_Heat_Cost
  + Intentional_Cost
))
```
- `Stance_Multiplier`: 
    - 2H（主腕のみ）: **1.0**
    - 1H + 副腕なし: **1.0**
    - 1H + 副腕（訓練者: うかみ、タチバナ等）: **1.0**
    - 1H + 副腕（非訓練者: ミコト、スクナ等）: **1.2**（「構えの摩擦（Stance Friction）」による増加）
- `Intentional_Cost`: プレイヤーが任意に支払う自傷（活魂）・情念放出コスト。神の計算ノイズの源泉。
- **Yobitsugi_Penalty**: キメラ化武器は耐久減少係数が **1.5〜3.0倍** に跳ね上がる（強力だが即消耗する）。

### 神のターゲット計算 (God_AI_Logic)
```
// 各行動順（Tick）開始時、最適ターゲットを計算しUIに予告する
Target = f(Kakkon_current, DEF_current, action_history_weight)
```

**AI学習段階（AI_Evolution）:**
| レベル                | 参照情報                                                                   | 対象                                                 |
| --------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------- |
| Lv1 (Static)          | 現在活魂と防御力のみ                                                       | 序盤の神（静止の理）                                 |
| Lv2 (Adaptive)        | 自傷行動の過去頻度も参照                                                   | 中盤の神（変化への適応）                             |
| Lv2.5 (Psychological) | 同パターンの反復に `Pattern_Penalty` を付与                                | イザナギなど終盤の神（結晶化の完成／悲哀からの救済） |
| Lv3 (Absolute)        | 高い `Noise_Resistance`。`Autonomous_Noise` と `SoulIdea` 級でのみ突破可能 | 別天津神（絶対零度の理）                             |

※ アマテラスはこの曲線に含まれない。天岩戸フリーズ解除という専用イベントで処理される。

### うかみAIの自動介入と独立リソース (Ukami_Autonomous_Logic)
第4幕（黄泉・常世）で参戦する行者うかみは、プレイヤーの共有リソース（活魂・情念）を使用せず、AI内部で完結した**独立リソース**で駆動する。
- **Ukami_Internal_Vigor / Ukami_Internal_Heat**: AI内部でのみ管理されるパラメータ。被ダメージや技使用で変動するが、画面上のメインUIゲージには影響しない。
- **Ukami_AutoIntercept**: `Player_Takes_Fatal_Damage` 等の条件下で発動。成功率100%・行動順無視で割り込む。
- **肩代わりロジック**: プレイヤーが受ける `Invasion_Value`（侵食）の上昇を、うかみの `Internal_Vigor` を削ることで無効化する処理。
- **Ukami_Heal_Absolute**: うかみの法力による回復。`Yomotsu_Eat_State` による回復反転の影響を内部的に無効化し、常にプラスの回復値として処理する。
- **地上での制限**: 地上エリアにおいては物理的に参戦不可であり、遠隔守護フラグも存在しない（完全な断絶）。

### 神写し理解度
```
Understand(skill, ally) += action_count * context_bonus
context_bonus: Critical_Kakkon → x2.0 / Disadvantage_Match → x1.5
IF Understand >= Threshold → ミコトが該当技を習得
```

### 黄泉戸喫・侵食ゲージ
```
// 各行動順（Tick）ごとの蓄積値（Underworldエリア限定）
Turn_Invasion_Delta = (Damage_Taken_Sum + SelfHurt_Cost_Sum) * YomotsuInvasionThreshold
Invasion_Value = min(Max_Invasion, Invasion_Value + Turn_Invasion_Delta)

IF Invasion_Value > Warning_Threshold → 自身のTickが回ってくるたびに最大活魂（MaxKakkon）減少開始
```

### 共鳴（ユニゾン）計算
```
// 行動順（Tick）が回ってくる前に割り込んで発動する先制攻撃
Resonance_Attack_Damage = Base_Weapon_Damage * ResonanceRate
// 発動条件A: タイムライン上で行動順（Tick）が連続しており、かつ同カテゴリ（槍・鉾 / 打撃 等）の技を選択
// 発動条件B: [第4幕] ミコトの神写し技 ＋ うかみNPCの行動重複 → 確定発動
```

### 代受苦発動・データ遷移
```
// 任意タイミングで発動可（耐久値制限なし）
Daijuku_Trigger → State_Overheated = TRUE（武器を一時使用不能にする / 特大ダメージ付与）
// 非自発的な耐久尽き（代受苦不使用）
Durability_Zero_Natural → State_Overheated = TRUE (ダメージ特典なし / 完全な損)
// 極大代受苦（Is_Destiny_Battle フラグが立つボス戦限定）
Extreme_Daijuku → Item_Instance を完全消去し以下を生成:
  - Route A: SoulIdea（輪廻ルート・次の武器へのデータ継承）
  - Route B: Remnant_Bone（遺骨・キメラ接合専用素材）
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

## 2. マスターデータ定義

### Equipment_Slot_Master（可変スロット制）
| Slot_ID      | 名称     | 内容                                               | 属性フラグ            |
| ------------ | -------- | -------------------------------------------------- | --------------------- |
| `MAIN_ARM`   | 主腕     | 直接攻撃を担うメインスロット。                     | `1H` / `2H`           |
| `SUB_ARM`    | 副腕     | ノイズ具スロット。主腕が `2H` の場合は封印される。 | `1H` / `LOCKED_BY_2H` |
| `SHOZOKU`    | 装束     | 防御衣服。傷跡が防御力(PTG)になる。                | `UNIQUE`              |
| `KATASHIRO`  | 形代     | 遺品・未練。最大2個。                              | `STACKABLE_2`         |
| `FIXED_GEAR` | 固定装具 | スロットを消費しない特殊枠。                       | `SLOTLESS`            |

### Item_Master（主要フラグ）
| フィールド        | 説明                                                                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Slot_Type`       | どのスロットに帰属するかを指定                                                                                                                                               |
| `Remnant_Bone`    | 極大代受苦後の遺骨。元の武器IDと特性を保持。キメラ専用素材（星の砂と混同させない）                                                                                           |
| `Ame_no_Murakumo` | スサノオの遺産。`Global_Daijuku_Log_Data` を参照して威力変動。裏ボス撃破後に `Rinne_no_Kintsugi=true` フラグが解放され、致命傷時に自動過熱して持ち主を庇う機能が有効化される |

### Item_State_Extension（武器インスタンス付加情報）
| フィールド         | 説明                                                                               |
| ------------------ | ---------------------------------------------------------------------------------- |
| `TraumaLogDensity` | 履歴密度（付喪神覚醒・キメラ強度に影響）                                           |
| `TsukumogamiState` | `Dormant` / `Kibutsu`（棄物敵化） / `Musubi`（結和神覚醒）                         |
| `Is_Chimera`       | 呼び継ぎ（キメラ接合）フラグ。`TRUE`の場合再度の極限代受苦は遺骨を生成せず塵となる |
| `AbandonFlag`      | 遺棄判定。`TRUE`で棄物化進行が開始                                                 |

### Enemy_Master（主要ボス定義）
| ID                        | 名称             | 特殊仕様                                                                                                             |
| ------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| `Amaterasu_Core_OS`       | 天照大御神       | 戦闘対象ではなく「システムフリーズ状態」管理プロセス。天岩戸解除イベントで制御。                                     |
| `Takemikazuchi_Enforcer`  | タケミカヅチ     | 予告UI「裁きの神雷」。うかみの手甲（残留応力）による特殊防御（接地/アース）イベントをトリガーする。                  |
| `Tsukuyomi_AntiVirus`     | 月読命           | 代謝（回復）行動で `ActionError` 移行。確定全滅技「永遠の月食」時に、カガセオ乱入イベントで無敵状態を物理剥離する。  |
| `Kagaseo_Star_God`        | カガセオ         | 物理装甲ではなく高圧の情念でダメージ計算。引導を渡すため「熱量発散（特殊HP減算ルール）」が適用される。               |
| `Boss_AmenoIwatowake`     | アメノイワトワケ | `Damage_Multiplier = 0.0` 固定。`Event_Noise_Overload` でのみ撃破扱い。                                              |
| `Izanagi_Crystallizer`    | 伊邪那岐命       | 大いなる悲哀と完璧な拒絶の体現。UI予測は完璧であり、情動による「揺らぎ」を最も排除した究極の学習型AI（Lv2.5）。      |
| `Boss_Yamata_no_Ubusuna`  | 澱神・八岐の産土 | ステータスが `Global_Daijuku_Log_Data` と `Chimera_Craft_Count` で動的スケーリング。殻破壊後にUIジャック状態へ移行。 |
| `Boss_Yakusa_no_Ikazuchi` | 八雷神           | クリア後限定。行者還しの専用3フェーズ進行に従う。                                                                    |
| `Boss_Susanoo`            | スサノオ         | 活魂ゼロではなく `Timeline_Compression_Score` が勝利条件のスコアアタック制。                                         |

### Enemy_Behavior_Tag
| タグ                      | 対象   |
| ------------------------- | ------ |
| `Predictive_Fixed`        | 白化神 |
| `Predictive_Broken`       | 澱神   |
| `Predictive_Fluctuating`  | 荒魂獣 |
| `Trauma_Resentment`       | 棄物   |
| `Pseudo_Perfect_With_Gap` | 擬神兵 |

### 神社・祠関連データ
| マスター              | 主要フィールド                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------ |
| `Shrine_Master`       | `ShrineID`, `Type` (`JINJA`/`HOKORA`), `Prayer_Points_Base`, `Mitama_Slot`                 |
| `Shrine_Faith_Master` | 御霊ごとの恩恵（バフ・神写しツリー解放）                                                   |
| `Shrine_Network_Data` | `Total_Prayer_Points`（受容力）, `Connected_Shrines`（開通済みIDリスト）, `Unlocked_Buffs` |

### その他マスター
| マスター                       | 目的                                                                                                                                |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `Skill_Master`                 | 固有スキル・神写し可否・理解度閾値・共鳴タグ                                                                                        |
| `Kintsugi_Master`              | 修復素材と付与特性（被ダメ履歴参照）定義                                                                                            |
| `Daijuku_Master`               | 武器消滅時に生成する「魂のイデア」テーブル。クリア後は `Infinite_Idea_Chain` 解放。                                                 |
| `Tsukumogami_Awakening_Master` | `Awaken_Threshold_LogDensity`, `Awaken_Required_Kintsugi_MaterialKinds`, `Musubi_AutoAction_Chance`, `Kibutsu_Spawn_Weight_By_Area` |
| `Yomotsu_Eat_Master`           | 侵食ゲージ閾値、食材ID、回復反転係数、キャラ別耐性                                                                                  |
| `FastTravel_Master`            | 脈継ぎ演出・移動中掛け合いセリフ管理                                                                                                |
| `Sea_Exploration_Master`       | クリア後専用。海ノード生成ルール・サルベージテーブル・幻曜の代受苦コスト定義                                                        |

---

## 3. Story_Flag_Master（進行フラグ一覧）

物語のジェットコースター構造（うかみ離脱→偽終幕→黄泉帰還）をゲーム内トリガーとして再現する。

| フラグ名                              | 発火タイミング                                                   |
| ------------------------------------- | ---------------------------------------------------------------- |
| `UKAMI_JOINED_EARLY`                  | うかみがアマでパーティ合流                                       |
| `TACHIBANA_JOINED_ACT2`               | 忘却の海食洞でタチバナが加入                                     |
| `UKAMI_LEFT_KATSURAGI`                | 葛城山での一次離脱（タチバナ加入後）                             |
| `WAKAHIKO_ANTAGONIST_PHASE`           | ワカヒコによる執拗な追撃・対立期間                               |
| `WAKAHIKO_JOINED_ACT3`                | 天望の天守でのワカヒコ加入                                       |
| `ACT3_KAGASEO_RESONANCE`              | 第3幕の一度限りのカガセオ意識による加勢イベント                  |
| `TSUKUYOMI_TOWER_DEPLOYED`            | 静謐の塔建造・浄化プロトコル起動                                 |
| `TSUKUYOMI_FAKE_LASBOSS`              | ツクヨミ撃破・偽終幕祝祭発生                                     |
| `TSUKUYOMI_CELEBRATION_CONDUCTED`     | 偽終幕後の凍結UIジャック開始                                     |
| `UKAMI_RETURNED_YOMOTSU`              | 黄泉比良坂でうかみが行者として帰還                               |
| `KAGASEO_REBOOT_HEAT_ACQUIRED`        | 星屑の荒野（カガセオ戦）でリブート用の熱を獲得                   |
| `AMENO_IWATOWAKE_BROKEN`              | 神器とカガセオの熱量により天岩戸を強制リブート                   |
| `ETERNITY_REJECTED_DEATH_IMPLEMENTED` | 別天津神を破り、ただの人間としての死を受け入れた（エンディング） |
| `GYOJAGAESHI_CLEARED`                 | クリア後「行者還し」完了。うかみを完全フリーメンバー化。         |
| `SUSANOO_TRIAL_CLEARED`               | 根堅洲国スサノオのタイムライン試練完了                           |

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

| パラメータ名                  | 説明                             |
| ----------------------------- | -------------------------------- |
| `Threshold`                   | 神写し習得閾値                   |
| `ResonanceRate`               | 共鳴倍率                         |
| `FrictionBase`                | 基本摩擦係数                     |
| `Yobitsugi_Friction_Mult`     | キメラ化時の摩擦倍率（1.5〜3.0） |
| `YomotsuInvasionThreshold`    | 侵食ゲージ閾値                   |
| `YomotsuRecoveryReversalRate` | 黄泉戸喫時の回復反転係数         |
| `Tachibana_Kakkon_Cost_Mult`  | タチバナの自傷型術の係数         |
| `PTG_RareChance`              | PTG（外傷後成長）効果発生率      |
| `SoulIdeaCarryRate`           | 魂のイデア継承率                 |
| `TsukumogamiAwakeThreshold`   | 付喪神覚醒閾値                   |
| `KibutsuSpawnRate`            | 棄物（敵性付喪神）出現率         |
| `WildInstinctVariance`        | 荒魂獣の行動揺らぎ幅             |

> **Single Source of Truth**: 上記パラメータの実数値はすべて本ファイルのみで管理する。画面表示・物語表現・UX演出での独自変更を禁止する。

---

## 6. Visual_Prompt_Master（アセット管理メタデータ）

| フィールド                | 値                                                     |
| ------------------------- | ------------------------------------------------------ |
| `PromptSetId`             | `LUMINOUS_WASHI_V3`                                    |
| `SourcePath`              | `40_Art_Direction_and_Assets.md`                       |
| `AnchorId`                | `00_STYLE_ANCHOR_LUMINOUS_WASHI`                       |
| `AncientConstraint`       | `true`（西洋甲冑・SF意匠を禁止）                       |
| `WatercolorBleedEnforced` | `true`                                                 |
| `AnimeStyleBlocked`       | `true`                                                 |
| `BossPresenceBias`        | `TSUKUYOMI_HIGH`（偽ラスボス威圧感の優先）             |
| `KagaseoHumanityBias`     | `true`（岩塊主体を避け人間的骨格を優先）               |
| `DeityRegaliaOpulence`    | `HIGH`（アマテラス・ツクヨミの儀礼装束の華やかさ下限） |
