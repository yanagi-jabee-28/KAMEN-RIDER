**【プロジェクト・コア・フィロソフィー】**
* **タイトル:** アシブネノミコト —泥と星の神話—
* **テーマ:** 「完璧な神の理」に対する、「不完全な人間の熱量」の肯定。
* **デザイン原則:**
  * 神（敵・システム）は、傷を恐れ、無機質で完璧な予測（エントロピーの凍結）を行う。
  * 人（味方・プレイヤー）は、傷を歴史として引き受け、摩擦やエラー（ノイズ）で神の理を砕く。
* **すべての仕様は、「効率的な消費」ではなく「泥臭い修復と継承」をプレイヤーに体感させるために存在する。**

---

# 04_Data_Architecture

## 1. コア計算式（採用版）

- **武器耐久値の減衰モデル:**
  - `D_new = D_old - (k * Friction) - Intentional_Cost`
  - `Friction` は属性不一致や連続使用で増加する。
  - **Yobitsugi_Penalty:** 「呼び継ぎ」を行った武器は、`Friction` の基本係数 `k` が **1.5倍〜3.0倍** に跳ね上がる（強力だが脆い）。
  - `Intentional_Cost` はプレイヤーが任意に支払う「自傷・耐久過剰消費」コストであり、神の計算を狂わせる「ノイズ」の源泉となる。
- **神のターゲット計算式 (God_AI_Logic):**
  - 各ターン開始時、現状のステータスに基づき最適解（`Target`）をUI予告する。
  - **AI_Evolution (学習深度):**
    - **Lv1 (Static):** 現在HP/防御力のみを参照。
    - **Lv2 (Adaptive):** プレイヤーの過去の行動傾向（自傷頻度）を係数に組み込み、安易な自傷ではターゲットがブレない。
    - **Lv2.5 (Psychological):** 同じパターンの「自傷」や「摩擦行動」が繰り返された場合、`Pattern_Penalty` を付与し、その行動を無効化またはカウンターする（メタ合理の排除）。
    - **Lv3 (Absolute - 別天津神):** 高い `Noise_Resistance` を持ち、通常の `Intentional_Cost` を無効化する。これを突破するには `Autonomous_Noise`（うかみの自律行動）や `SoulIdea`（武器破壊級の熱量）が必要となる。
  - プレイヤーの `Intentional_Cost`（自傷等）や、**第4幕限定の `Autonomous_Noise`** が発生した際、AIはターゲットを再計算できず、空振りや `ActionError` 状態に陥る。
  - **Ukami_AI_Constraint:** うかみの自律行動は、ミコトが「うかみの技」を選択し、かつ一定以上の「Intentional_Cost（代受苦や自傷）」を払ったターンを検知して確定発動する。行動順を無視した割り込み（代受身）により、ミコトの自傷リスクを肩代わりしつつ神の予測を粉砕する。
- **神写し理解度:**
  - `Understand(skill, ally) += action_count * context_bonus` (Critical_HP: x2.0, Disadvantage: x1.5)
  - `Understand >= Threshold` でミコトが当該特技を習得。
- **共鳴（ユニゾン）補正:**
  - `ResonanceDamage = BaseDamage * (1 + ResonanceRate)`
  - 条件A: 同ターンにミコトと仲間が同一特技を使用。
  - **条件B (第4幕専用): ミコトが継承済みの「うかみの技」を使用し、NPC行者うかみが同ターンに行動した場合、確定で派生発動。**
- **代受苦発動条件:**
  - `Durability <= Critical_Threshold` (e.g. 10%)
  - 発動時にプレイヤーに二者択一を求め、武器データ（`Item_Instance`）消去と引き換えに以下の**どちらか1つ**を生成する。
    1. `SoulIdea`: 次期武器へ継承されるデータ特性（輪廻ルート）。
    2. `Remnant_Bone`: インベントリに残る「遺骨」アイテム（執着キメラルート）。
  - **オーバーフロー計算式:** 神の「無傷の合理性」を冷笑するため、残耐久値に反比例する倍率を掛ける。
  - `Sword_Mound_Damage = Base * (Global_Daijuku_Count * Log_Density_Sum) * (Max_Durability / max(1, Current_Durability))^2`

## 2. マスターデータ定義

- **Item_Master:** 武器、防具、金継ぎ素材、消費アイテム。
  - `Remnant_Bone`: 代受苦後の遺骨。元の武器IDと特性を保持。
- **Item_State_Extension:**
  - `TraumaLogDensity`（履歴密度）
  - `TsukumogamiState`（`Dormant` / `Kibutsu` / `Musubi`）
  - `Is_Chimera`（呼び継ぎフラグ）
  - `AbandonFlag`（遺棄判定）
- **Skill_Master:** キャラ固有スキル、神写し対象可否、理解度閾値、共鳴タグ。
- **Enemy_Master:** 白化神、澱神、荒魂獣、棄物、擬神兵、裁定者（タケミカヅチ等）、別天津神。**クリア後用の記憶残滓（ボスラッシュ用高ステータス・バグ行動版）を含む。**
- **Enemy_Behavior_Tag:**
  - `Predictive_Fixed`（白化神）
  - `Predictive_Broken`（澱神）
  - `Predictive_Fluctuating`（荒魂獣）
  - `Trauma_Resentment`（棄物）
  - `Pseudo_Perfect_With_Gap`（擬神兵）
- **Kintsugi_Master:** 耐久1より大きい武器への修復素材と付与特性（被ダメ履歴参照）。
 - **Daijuku_Master:** 耐久1武器の消滅と引き換えに生成される「魂のイデア」テーブル。**（クリア後は世代継承無制限フラグ `Infinite_Idea_Chain` が解放されるが、比例して `Fragility` も上昇する）**
- **Tsukumogami_Awakening_Master:**
  - `Awaken_Threshold_LogDensity`
  - `Awaken_Required_Kintsugi_MaterialKinds`
  - `Musubi_AutoAction_Chance`
  - `Kibutsu_Spawn_Weight_By_Area`
- **Sea_Exploration_Master（クリア後）:** 傷跡の海のノード生成ルール、サルベージテーブル、ボスラッシュの遭遇定義、**幻曜の代受苦（Phantom_Daijuku）に必要な泥コスト定義**。
- **Party_Composition_Master:** 戦闘枠4、控え枠2。**第4幕の帰還イベント以降（カガセオ戦および別天津神戦）、システム制御外の `5th_NPC_Slot` を解放する。**（※第3幕の正体不明の加勢は、システム上のスロットやバフではなく、イベント戦闘専用のスクリプト処理とする）
- **Story_Flag_Master:**
  - `UKAMI_JOINED_EARLY`
  - `UKAMI_LEFT_KATSURAGI`
  - `ACT3_SHADOW_INTERVENTION`
  - `UKAMI_RETURNED_YOMOTSU`
  - `KAGASEO_TRIAL_CLEARED`
  - `KOTOAMATSUKAMI_DEFEATED`

## 3. 数値調整の責務分離

- **Single Source of Truth:** 数値は本ファイル（または接続先スプレッドシート）を唯一の正とする。
- **分離原則:** 物語的意味は `01`、処理ロジックは `02`、UI/導線は `03` に記述し、重複を禁止する。

## 4. 初期バランス用パラメータ（暫定）

- `Threshold`（神写し習得閾値）
- `ResonanceRate`（共鳴倍率）
- `FrictionBase` / `FrictionPenaltyInventory`
- `Yobitsugi_Friction_Mult`（呼び継ぎ時の摩擦倍率）
- `PTG_RareChance`（PTG効果発生率）
- `SoulIdeaCarryRate`（魂のイデア継承率）
- `TsukumogamiAwakeThreshold`（付喪神覚醒閾値）
- `KibutsuSpawnRate`（棄物出現率）
- `WildInstinctVariance`（荒魂獣の行動揺らぎ幅）

※ 実数値はプレイテストで更新し、本ファイルを唯一の更新点とする。

## 5. 新規採用メモ（2026-02-23）

- 敵データは5系統（白化神/澱神/荒魂獣/棄物/擬神兵）を基本軸として管理。
- 武具データへ `TsukumogamiState` と履歴密度を追加し、敵化/味方化分岐をデータ上で担保。
- 代受苦の処理に `Remnant_Bone` 生成と `Global_Daijuku_Count` 加算を追加。
- 付喪神覚醒条件と棄物化条件をマスタ化し、シナリオ依存のハードコードを回避。

## 6. 会話ログ参照（根拠）

- 参照元: `チャット履歴/gemini-conversation-2026-02-22-21-36-20.md`
- 主要根拠トピック:
  - 摩擦係数を含む耐久減衰式
  - 神写し理解度閾値と共鳴倍率のデータ管理
  - 代受苦発動条件と魂のイデア継承
  - 進行フラグ（うかみ加入/離脱/帰還、カガセオ試練、別天津神撃破）
  - 雑魚敵系統の拡張に伴う敵行動タグ設計
  - 付喪神の敵味方分岐を支える状態管理項目
