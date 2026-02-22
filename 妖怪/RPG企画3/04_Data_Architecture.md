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
  - `D_new = D_old - (k * Friction)`
  - `Friction` は属性不一致、危険行動、自傷行動で増加し、金継ぎ結果の希少度へ影響する。
- **ダメージ計算思想:**
  人間武器は使用回数・耐久低下に伴い乱数幅が拡大し、神の計算を狂わせる。
- **神写し理解度:**
  - `Understand(skill, ally) += action_count * context_bonus`
  - `Understand >= Threshold` でミコトが当該特技を習得。
- **共鳴（ユニゾン）補正:**
  - `ResonanceDamage = BaseDamage * (1 + ResonanceRate)`
  - 条件: 同ターンにミコトと仲間が同一特技を使用。
- **代受苦発動条件:**
  - `Durability <= 1` かつ `PlayerIntent = true`
  - 発動時に武器を消去し、`SoulIdea` を加算。

## 2. マスターデータ定義

- **Item_Master:** 武器、防具、金継ぎ素材、消費アイテム。
- **Skill_Master:** キャラ固有スキル、神写し対象可否、理解度閾値、共鳴タグ。
- **Enemy_Master:** 白化神、澱神、裁定者（タケミカヅチ等）、別天津神。
- **Kintsugi_Result_Master:** 破損履歴タイプ、必要素材、付与特性、PTG変換先。
- **Party_Composition_Master:** 戦闘枠4、控え枠2、離脱時自動編成ルール。
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
