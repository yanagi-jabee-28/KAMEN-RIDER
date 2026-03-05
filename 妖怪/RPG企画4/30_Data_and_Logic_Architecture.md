# 30 Data and Logic Architecture (データと論理)

本ドキュメントはEngineer専用の実装要件・変数定義書（Single Source of Truth）である。物語的・情動的な表現はすべて `10_Narrative_and_Characters.md` と `20_Game_Systems_and_Flow.md` に委ね、ここでは変数・フラグ・計算式のみを純粋な形で定義する。バランス数値の変更は必ず本ファイルを唯一の更新点とすること。

---

## 1. コア計算式

### 武器耐久値減衰モデル
```
D_new = D_old - (k * Friction) - Intentional_Cost
```
- `Friction`: 属性不一致・連続使用で増加する自然摩耗係数。
- `Intentional_Cost`: プレイヤーが任意に支払う自傷・耐久過剰消費コスト（神の計算ノイズの源泉）。
- **Yobitsugi_Penalty**: キメラ化武器は `k` が **1.5〜3.0倍** に跳ね上がる（強力だが脆い）。

### 神のターゲット計算 (God_AI_Logic)
```
// 各ターン開始時、最適ターゲットを計算しUIに予告する
Target = f(HP_current, DEF_current, action_history_weight)
```

**AI学習段階（AI_Evolution）:**
| レベル | 参照情報 | 対象 |
|---|---|---|
| Lv1 (Static) | 現在HPと防御力のみ | 序盤の神 |
| Lv2 (Adaptive) | 自傷行動の過去頻度も参照 | 中盤の神 |
| Lv2.5 (Psychological) | 同パターンの反復に `Pattern_Penalty` を付与 | 終盤の神 |
| Lv3 (Absolute) | 高い `Noise_Resistance`。`Autonomous_Noise` と `SoulIdea` 級でのみ突破可能 | 別天津神 |

※ アマテラスはこの曲線に含まれない。天岩戸フリーズ解除という専用イベントで処理される。

### うかみAIの自動介入制約 (Ukami_AI_Constraint)
フラグベースのシンプル仕様：
```
IF (Player_Action_Is_High_Friction OR Player_Takes_Fatal_Damage)
  → Ukami_AutoIntercept = TRUE  // 成功率100%・行動順無視・無条件介入
```
- 物理帯同不可エリア（地上）では `Remote_Intervention_Flag` を介し、ミコトの「手甲」を媒介として幻影（祈りの力）として発動する。

### 神写し理解度
```
Understand(skill, ally) += action_count * context_bonus
context_bonus: Critical_HP → x2.0 / Disadvantage_Match → x1.5
IF Understand >= Threshold → ミコトが該当技を習得
```

### 黄泉戸喫・侵食ゲージ
```
Invasion_new = Invasion_old + (Food_Value * k) + (SelfHurt_Count * h)
IF Invasion > YomotsuInvasionThreshold → 毎ターン侵食ダメージ + MaxHP減少
```

### 共鳴（ユニゾン）計算
```
ResonanceDamage = BaseDamage * (1 + ResonanceRate)
// 発動条件A: 同ターンにミコトと仲間が同一特技を使用した場合
// 発動条件B（第4幕専用）:ミコトが継承済みの「うかみの技」使用 + うかみNPCが同ターンに行動 → 確定発動
```

### 代受苦発動・データ遷移
```
// 任意タイミングで発動可（耐久値制限なし）
Daijuku_Trigger → State_Overheated = TRUE（武器を一時使用不能にする）
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

### HPコスト型攻撃（タチバナ等）
```
Damage = Base * (1 + HP_Cost_Mult * (MaxHP - CurrentHP))
```
- `HP_Cost_Attack` として `Intentional_Cost` の一種に分類。神AI的には通常摩擦と区別して管理。

---

## 2. マスターデータ定義

### Equipment_Slot_Master（4スロット制）
| Slot_ID | 名称 | 内容 |
|---|---|---|
| `SHU_WAN` | 主腕 | メインウェポン。物理破壊・直接攻撃。 |
| `FUKU_WAN` | 副腕 | ノイズ発生具（日用品・祭具・盾）。 |
| `SHOZOKU` | 装束 | 防御系を統合した単一衣服スロット。修復履歴が防御力になる。旧「兜・鎧・靴」は撤廃。 |
| `KATASHIRO` | 形代 | アクセサリ枠。最大2個。情念・未練の結晶を装備する。 |

### Item_Master（主要フラグ）
| フィールド | 説明 |
|---|---|
| `Slot_Type` | どのスロットに帰属するかを指定 |
| `Remnant_Bone` | 極大代受苦後の遺骨。元の武器IDと特性を保持。キメラ専用素材（星の砂と混同させない） |
| `Ame_no_Murakumo` | スサノオの遺産。`Global_Daijuku_Log_Data` を参照して威力変動。裏ボス撃破後に `Rinne_no_Kintsugi=true` フラグが解放され、致命傷時に自動過熱して持ち主を庇う機能が有効化される |

### Item_State_Extension（武器インスタンス付加情報）
| フィールド | 説明 |
|---|---|
| `TraumaLogDensity` | 履歴密度（付喪神覚醒・キメラ強度に影響） |
| `TsukumogamiState` | `Dormant` / `Kibutsu`（棄物敵化） / `Musubi`（結和神覚醒） |
| `Is_Chimera` | 呼び継ぎ（キメラ接合）フラグ。`TRUE`の場合再度の極限代受苦は遺骨を生成せず塵となる |
| `AbandonFlag` | 遺棄判定。`TRUE`で棄物化進行が開始 |

### Enemy_Master（主要ボス定義）
| ID | 名称 | 特殊仕様 |
|---|---|---|
| `Amaterasu_Core_OS` | 天照大御神 | 戦闘対象ではなく「システムフリーズ状態」管理プロセス。天岩戸解除イベントで制御。 |
| `Tsukuyomi_AntiVirus` | 月読命 | 代謝行動（回復等）を穢れとして検知し `ActionError` 移行するロジックを持つ。ミコトへの「座標リンクイベント」もここで管理。 |
| `Kagaseo_Star_God` | カガセオ | 金継ぎ（星の砂）の本体。人間の信仰と熱量で再結晶した「核」。岩塊ではなく人間的骨格ベースで実装。 |
| `Boss_AmenoIwatowake` | アメノイワトワケ | `Damage_Multiplier = 0.0` 固定。`Event_Noise_Overload` でのみ撃破扱い。 |
| `Boss_Yamata_no_Ubusuna` | 澱神・八岐の産土 | ステータスが `Global_Daijuku_Log_Data` と `Chimera_Craft_Count` で動的スケーリング。殻破壊後にUIジャック状態へ移行。 |
| `Boss_Yakusa_no_Ikazuchi` | 八雷神 | クリア後限定。行者還しの専用3フェーズ進行に従う。 |
| `Boss_Susanoo` | スサノオ | HPゼロではなく `Timeline_Compression_Score` が勝利条件のスコアアタック制。 |

### Enemy_Behavior_Tag
| タグ | 対象 |
|---|---|
| `Predictive_Fixed` | 白化神 |
| `Predictive_Broken` | 澱神 |
| `Predictive_Fluctuating` | 荒魂獣 |
| `Trauma_Resentment` | 棄物 |
| `Pseudo_Perfect_With_Gap` | 擬神兵 |

### 神社・祠関連データ
| マスター | 主要フィールド |
|---|---|
| `Shrine_Master` | `ShrineID`, `Type` (`JINJA`/`HOKORA`), `Prayer_Points_Base`, `Mitama_Slot` |
| `Shrine_Faith_Master` | 御霊ごとの恩恵（バフ・神写しツリー解放） |
| `Shrine_Network_Data` | `Total_Prayer_Points`（受容力）, `Connected_Shrines`（開通済みIDリスト）, `Unlocked_Buffs` |

### その他マスター
| マスター | 目的 |
|---|---|
| `Skill_Master` | 固有スキル・神写し可否・理解度閾値・共鳴タグ |
| `Kintsugi_Master` | 修復素材と付与特性（被ダメ履歴参照）定義 |
| `Daijuku_Master` | 武器消滅時に生成する「魂のイデア」テーブル。クリア後は `Infinite_Idea_Chain` 解放。 |
| `Tsukumogami_Awakening_Master` | `Awaken_Threshold_LogDensity`, `Awaken_Required_Kintsugi_MaterialKinds`, `Musubi_AutoAction_Chance`, `Kibutsu_Spawn_Weight_By_Area` |
| `Yomotsu_Eat_Master` | 侵食ゲージ閾値、食材ID、回復反転係数、キャラ別耐性 |
| `FastTravel_Master` | 脈継ぎ演出・移動中掛け合いセリフ管理 |
| `Sea_Exploration_Master` | クリア後専用。海ノード生成ルール・サルベージテーブル・幻曜の代受苦コスト定義 |

---

## 3. Story_Flag_Master（進行フラグ一覧）

物語のジェットコースター構造（うかみ離脱→偽終幕→黄泉帰還）をゲーム内トリガーとして再現する。

| フラグ名 | 発火タイミング |
|---|---|
| `UKAMI_JOINED_EARLY` | うかみがアマでパーティ合流 |
| `UKAMI_LEFT_KATSURAGI` | 葛城山での一次離脱が確定 |
| `ACT3_KAGASEO_RESONANCE` | 第3幕の一度限りのカガセオ意識による加勢イベント |
| `TSUKUYOMI_TOWER_DEPLOYED` | 静謐の塔建造・浄化プロトコル起動 |
| `TSUKUYOMI_FAKE_LASBOSS` | ツクヨミ撃破・偽終幕祝祭発生 |
| `TSUKUYOMI_CELEBRATION_CONDUCTED` | 偽終幕後の凍結UIジャック開始 |
| `UKAMI_RETURNED_YOMOTSU` | 黄泉比良坂でうかみが行者として帰還 |
| `UKAMI_AREA_LOCK_ACTIVE` | 行者の誓約による地域拘束が有効 |
| `AMENO_IWATOWAKE_BROKEN` | 狂騒によって天岩戸を強制リブート |
| `KAGASEO_TRIAL_CLEARED` | カガセオ試練を突破 |
| `ETERNITY_REJECTED_DEATH_IMPLEMENTED` | 別天津神を破り、ただの人間としての死を受け入れた（エンディング） |
| `GYOJAGAESHI_CLEARED` | クリア後「行者還し」完了。うかみを完全フリーメンバー化。 |
| `SUSANOO_TRIAL_CLEARED` | 根堅洲国スサノオのタイムライン試練完了 |

### Party_Area_Constraint_Master（うかみ拘束ルール）
```yaml
TargetCharacter: UKAMI_GYOJA
LockFromFlag: UKAMI_RETURNED_YOMOTSU
UnlockFlag: GYOJAGAESHI_CLEARED
LockedAreas: [TOKOYO, YOMI_NO_KUNI, YOMOTSU_HIRASAKA]
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
|---|---|
| `Threshold` | 神写し習得閾値 |
| `ResonanceRate` | 共鳴倍率 |
| `FrictionBase` | 基本摩擦係数 |
| `Yobitsugi_Friction_Mult` | キメラ化時の摩擦倍率（1.5〜3.0） |
| `YomotsuInvasionThreshold` | 侵食ゲージ閾値 |
| `YomotsuRecoveryReversalRate` | 黄泉戸喫時の回復反転係数 |
| `Tachibana_HP_Cost_Mult` | タチバナの自傷型術の係数 |
| `PTG_RareChance` | PTG（外傷後成長）効果発生率 |
| `SoulIdeaCarryRate` | 魂のイデア継承率 |
| `TsukumogamiAwakeThreshold` | 付喪神覚醒閾値 |
| `KibutsuSpawnRate` | 棄物（敵性付喪神）出現率 |
| `WildInstinctVariance` | 荒魂獣の行動揺らぎ幅 |

> **Single Source of Truth**: 上記パラメータの実数値はすべて本ファイルのみで管理する。画面表示・物語表現・UX演出での独自変更を禁止する。

---

## 6. Visual_Prompt_Master（アセット管理メタデータ）

| フィールド | 値 |
|---|---|
| `PromptSetId` | `LUMINOUS_WASHI_V3` |
| `SourcePath` | `40_Art_Direction_and_Assets.md` |
| `AnchorId` | `00_STYLE_ANCHOR_LUMINOUS_WASHI` |
| `AncientConstraint` | `true`（西洋甲冑・SF意匠を禁止） |
| `WatercolorBleedEnforced` | `true` |
| `AnimeStyleBlocked` | `true` |
| `BossPresenceBias` | `TSUKUYOMI_HIGH`（偽ラスボス威圧感の優先） |
| `KagaseoHumanityBias` | `true`（岩塊主体を避け人間的骨格を優先） |
| `DeityRegaliaOpulence` | `HIGH`（アマテラス・ツクヨミの儀礼装束の華やかさ下限） |
