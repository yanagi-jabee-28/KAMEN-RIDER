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
  - `Intentional_Cost` はプレイヤーが任意に支払う「自傷・耐久過剰消費」コストであり、神の計算を狂わせる「ノイズ」の源泉となる。
- **神のターゲット計算式 (God_AI_Logic):**
  - 各ターン開始時、現状のステータスに基づき最適解（`Target`）をUI予告する。
  - プレイヤーの `Intentional_Cost`（自傷等）や、**第4幕限定の `Autonomous_Noise`（行者うかみNPCの独立行動）** が発生した際、AIはターゲットを再計算できず、空振りや `ActionError` 状態に陥る。
- **神写し理解度:**
  - `Understand(skill, ally) += action_count * context_bonus`
  - `Understand >= Threshold` でミコトが当該特技を習得。
- **共鳴（ユニゾン）補正:**
  - `ResonanceDamage = BaseDamage * (1 + ResonanceRate)`
  - 条件A: 同ターンにミコトと仲間が同一特技を使用。
  - **条件B (第4幕専用): ミコトが継承済みの「うかみの技」を使用し、NPC行者うかみが同ターンに行動した場合、確定で派生発動。**
- **代受苦発動条件:**
  - `Durability == 1` かつ `PlayerIntent = true`
  - 発動時に武器データ（`Item_Instance`）を完全消去し、蓄積履歴から `SoulIdea` を抽出・加算（次期武器へ継承）。

## 2. マスターデータ定義

- **Item_Master:** 武器、防具、金継ぎ素材、消費アイテム。
- **Skill_Master:** キャラ固有スキル、神写し対象可否、理解度閾値、共鳴タグ。
- **Enemy_Master:** 白化神、澱神、裁定者（タケミカヅチ等）、別天津神。**クリア後用の記憶残滓（ボスラッシュ用高ステータス・バグ行動版）を含む。**
- **Kintsugi_Master:** 耐久1より大きい武器への修復素材と付与特性（被ダメ履歴参照）。
- **Daijuku_Master:** 耐久1武器の消滅と引き換えに生成される「魂のイデア」テーブル。**（クリア後は世代継承無制限フラグ `Infinite_Idea_Chain` が解放される）**
- **Sea_Exploration_Master（クリア後）:** 傷跡の海のノード生成ルール、サルベージテーブル、ボスラッシュの遭遇定義。
- **Party_Composition_Master:** 戦闘枠4、控え枠2。**最終ダンジョン「常世」進入時のみ、システム制御外の `5th_NPC_Slot` を解放する。**
- **Story_Flag_Master:**
  - `UKAMI_JOINED_EARLY`
  - `UKAMI_LEFT_KATSURAGI`
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
- `PTG_RareChance`（PTG効果発生率）
- `SoulIdeaCarryRate`（魂のイデア継承率）

※ 実数値はプレイテストで更新し、本ファイルを唯一の更新点とする。

## 5. 会話ログ参照（根拠）

- 参照元: `チャット履歴/gemini-conversation-2026-02-22-21-36-20.md`
- 主要根拠トピック:
  - 摩擦係数を含む耐久減衰式
  - 神写し理解度閾値と共鳴倍率のデータ管理
  - 代受苦発動条件と魂のイデア継承
  - 進行フラグ（うかみ加入/離脱/帰還、カガセオ試練、別天津神撃破）
