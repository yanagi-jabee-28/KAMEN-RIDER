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

本ドキュメントでもキャラクターは単なる数学記号ではなく、
「リレイヤー」「ヴァンガード・ガイド」「洗浄使」など専門的な役割名で呼ばれる。
例として、うず効果として「一言法」「葛城の歪み」といった固有スキル名を
システム側でも扱う予定である。

- **武器耐久値の減衰モデル:**
  - `D_new = D_old - (k * Friction) - Intentional_Cost`
  - `Friction` は属性不一致や連続使用で増加する。
  - **Yobitsugi_Penalty:** 「呼び継ぎ」を行った武器は、`Friction` の基本係数 `k` が **1.5倍〜3.0倍** に跳ね上がる（強力だが脆い）。
  - `Intentional_Cost` はプレイヤーが任意に支払う「自傷・耐久過剰消費」コストであり、神の計算を狂わせる「ノイズ」の源泉となる。
- **神のターゲット計算式 (God_AI_Logic):**
  - 各ターン開始時、現状のステータスに基づき最適解（`Target`）をUI予告する。
  - **HPコスト型行動:** キャラクターが自身のHPを代償に発動する異能（例: タチバナの「冷たい水圧」）は`Intentional_Cost`の一種と見做され、神は通常のフリクションとは別に`HP_Cost_Attack`として扱う。発動式は `Damage = Base * (1 + HP_Cost_Mult * (MaxHP-CurrentHP))` のように設定できる。
  - **AI_Evolution (学習深度):**
  * アマテラスはこの進化曲線に含まれず、戦闘ではなく天岩戸のフリーズ解除という専用のイベントで扱われる。別天津神のみがこの曲線の終着点であり、最上位レベルの到達を意味する。
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
  - `Sword_Mound_Damage = Base * (
    Global_Daijuku_Count * Log_Density_Sum
    + Repair_Factor * Global_Kintsugi_Count
    + Usage_Factor * Cumulative_Durability_Hours
  ) * (Max_Durability / max(1, Current_Durability))^2`
  - **補足:**
    * `Global_Kintsugi_Count` は累計修復回数。修復（=金継ぎ）を重ねた武具の価値を高めるため、`Repair_Factor`（小さい定数）が掛けられる。
    * `Cumulative_Durability_Hours` は一本の武器をどれだけ長く使い込んだかを示す総耐久時間。時間経過や使用頻度に応じて増加し、`Usage_Factor` によって影響力を調整する。
    * これにより、「破壊した数だけ強くなる」だけでなく、「大切に使い続け、直してきた歴史そのものが威力に反映される」形となり、
      **泥臭い修復と継承というコアテーマ**が計算式にも織り込まれる。

## 2. マスターデータ定義

- **Item_Master:** 武器、防具、金継ぎ素材、消費アイテム。
  - `Remnant_Bone`: 代受苦後の遺骨。元の武器IDと特性を保持。
  - `Ame_no_Murakumo` (天叢雲剣): スサノオの遺産。過去のプレイで折られてきた `Global_Daijuku_Log_Data` (歴代の死の蓄積) を特殊パラメータとして参照・内包する究極の歴史集積武器。
- **Item_State_Extension:**
  - `TraumaLogDensity`（履歴密度）
  - `TsukumogamiState`（`Dormant` / `Kibutsu` / `Musubi`）
  - `Is_Chimera`（呼び継ぎフラグ）
  - `AbandonFlag`（遺棄判定）
- **Skill_Master:** キャラ固有スキル、神写し対象可否、理解度閾値、共鳴タグ。
- **Enemy_Master:** 白化神、澱神、荒魂獣、棄物、擬神兵、裁定者（タケミカヅチ等）、別天津神。**クリア後用の記憶残滓（ボスラッシュ用高ステータス・バグ行動版）を含む。**
  - `Amaterasu_Core_OS`: 戦闘対象ではなく、天岩戸の「システムフリーズ状態」を管理する特殊プロセスとして機能する。
  - `Tsukuyomi_AntiVirus`: 完全無菌化の執行者。プレイヤーの「食事（回復）」等代謝行動＝穢れを検知した際、特殊なエラー状態（行動キャンセル）へ移行するロジックを持つ。加えて、ミコトの身体に「空白の器」特有の異常が刻まれた場合、天の理の例外処理としてヤマト深淵への座標リンクイベントを発生させる仕様もこのデータで管理する。
  - `Kagaseo_Star_God`: 第4幕の試練ボス。無菌の星ではなく、熱と摩擦を放つ「原初の反逆者・最初の熱暴走」であり、金継ぎ（星の砂）の本体。
- **Enemy_Behavior_Tag:**
  - `Predictive_Fixed`（白化神）
  - `Predictive_Broken`（澱神）
  - `Predictive_Fluctuating`（荒魂獣）
  - `Trauma_Resentment`（棄物）
  - `Pseudo_Perfect_With_Gap`（擬神兵）
- **Kintsugi_Master:** 耐久1より大きい武器への修復素材と付与特性（被ダメ履歴参照）。**素材となる「星砂の白漆」などは、地に堕ちたカガセオの破片として定義されている。**
- **Daijuku_Master:** 耐久が**閾値以下**（例: 10%／赤ゲージ）になった武器の消滅と引き換えに生成される「魂のイデア」テーブル。耐久1以外で発動した場合でもデータ生成が発生する。**（クリア後は世代継承無制限フラグ `Infinite_Idea_Chain` が解放されるが、比例して `Fragility` も上昇する）**
- **Shrine_Part_Master:** 鳥居・参道・本殿など、各建築パーツのコスト（泥/木材/金漆）、受容力ボーナス、対応属性、敷地占有サイズを定義。
  - `PartType`: `INPUT` (鳥居), `LINE` (参道), `FILTER` (手水舎), `OUTPUT` (本殿), `OBSTACLE` (岩/水), `BUFFER` (鎮守の森).
  - `Impedance`: 信号通過時の抵抗値。
- **Shrine_Layout_Data:** プレイヤーが作成した社の配置情報。パーツIDとグリッド座標のセットを保持し、受容力算出に利用。
  - `ConnectionGraph`: パーツ間の接続状態を保持するグラフデータ。`Input` から `Output` へのパス到達可否を判定する。
- **Shrine_Faith_Master:** 祀った御霊ごとの恩恵バフと解放される神写しツリー枝などを紐付ける。
- **Shrine_Network_Master:** 祠や社など**祈りの場として設置された地点のみをノード**とし、ワープライン（ひび割れに沿った金継ぎ）の接続情報を管理する。ノード間の線は常に開通しており、視覚/音響演出パラメータを保持。
- **FastTravel_Master:** ファストトラベル固有の演出・UTXデータを定義。社受容力・澱みポイントが次戦闘ボーナスに変換される係数や、キャラクター台詞候補リストを含む。
  - `Weathering_Threshold`: **(Deprecated)** 仮設ラインが風化するまでの使用回数。現在はワープラインが恒久化される仕様に変更されたため使用されない。
  - `Reignition_Cost`: **(Deprecated)** 風化したラインを再点火するためのコスト係数。現在の仕様では関連項目は不要。

- **Tsukumogami_Awakening_Master:**
  - `Awaken_Threshold_LogDensity`
  - `Awaken_Required_Kintsugi_MaterialKinds`
  - `Musubi_AutoAction_Chance`
  - `Kibutsu_Spawn_Weight_By_Area`
- **Sea_Exploration_Master（クリア後）:** 傷跡の海のノード生成ルール、サルベージテーブル、ボスラッシュの遭遇定義、**幻曜の代受苦（Phantom_Daijuku）に必要な泥コスト定義**。
- **Party_Composition_Master:** 戦闘枠4、控え枠2。**第4幕の帰還イベント以降（カガセオ戦および別天津神戦）、システム制御外の `5th_NPC_Slot` を解放する。**（※第3幕の正体不明の加勢は、システム上のスロットやバフではなく、イベント戦闘専用のスクリプト処理とする）
- **Visual_Prompt_Master（追加）:** 画像生成プロンプトの版管理テーブル。複数のキャラクターバリエーション（若年／成熟など）を含むセットを一元管理できる。
  - `PromptSetId`: `LUMINOUS_WASHI_V3`
  - `SourcePath`: `Visual_Prompt_Pack_LUMINOUS_WASHI_V3.md`
  - `AnchorId`: `00_STYLE_ANCHOR_LUMINOUS_WASHI`
  - `AncientConstraint`: `true`
  - `WatercolorBleedEnforced`: `true`
  - `AnimeStyleBlocked`: `true`
- **Party_Area_Constraint_Master:** キャラ単位の地域拘束ルールを管理。
  - `TargetCharacter`: `UKAMI_GYOJA`
  - `LockFromFlag`: `UKAMI_RETURNED_YOMOTSU`
  - `UnlockFlag`: `KOTOAMATSUKAMI_DEFEATED`
  - `LockedAreas`: `TOKOYO`, `YOMI_NO_KUNI`, `YOMOTSU_HIRASAKA`
  - `ConstraintMode`: `CHARACTER_ONLY`（パーティ全体ではなく、うかみ本人のみに適用）
- **Story_Flag_Master:**
  <!-- フラグは物語進行の時系列を制御する。特に「うかみ離脱→ツクヨミ塔戦（偽終幕）→ヒルコ遭遇→黄泉比良坂帰還」といったジェットコースター構造を
       ゲーム内トリガーで再現するために用いられる。 -->
  - `UKAMI_JOINED_EARLY`
  <!-- ヒルコとミコトの船の象徴性は物語上常に意識されるため、該当フラグではないがメタ注釈を設計者文書へ残す。 -->
  - `UKAMI_LEFT_KATSURAGI`
  - `ACT3_KAGASEO_RESONANCE`  <!-- 元 ACT3_SHADOW_INTERVENTION。カガセオの星の瞬きによる一度きりの加勢 -->
  - `UKAMI_RETURNED_YOMOTSU`
  - `UKAMI_AREA_LOCK_ACTIVE`
  - `KAGASEO_TRIAL_CLEARED`
  - `ETERNITY_REJECTED_DEATH_IMPLEMENTED` <!-- 元 KOTOAMATSUKAMI_DEFEATED。別天津神を破り、ただの人間としての死（寿命バグ）を受け入れた証明 -->
  - `TSUKUYOMI_FAKE_LASBOSS` <!-- ツクヨミ戦が偽ラスボスとして祝祭が発生したフラグ -->
  - `TSUKUYOMI_TOWER_DEPLOYED` <!-- 白磁塔が建造され浄化プロトコルが起動された -->
  - `TSUKUYOMI_CELEBRATION_CONDUCTED` <!-- 偽終幕の祝祭が行われた -->

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
- `Tachibana_HP_Cost_Mult`（タチバナHP消費倍率）   <!-- 自傷型術の係数 -->

※ 実数値はプレイテストで更新し、本ファイルを唯一の更新点とする。

## 5. 新規採用メモ（2026-02-23 → 02-25更新）

- ツクヨミ戦の構造について、白磁塔＝地下ヒルコ浄化の楔という二段構成のジェットコースター型演出を導入。これに伴い、`TSUKUYOMI_TOWER_DEPLOYED` 等のストーリーフラグとイベントが追加される。
- ツクヨミ撃破後の「偽終幕祝祭」「天岩戸凍結」イベントを `TSUKUYOMI_FAKE_LASBOSS` / `TSUKUYOMI_CELEBRATION_CONDUCTED` フラグで切り替え、プレイヤー心理をリセットさせる設計。


- 敵データは5系統（白化神/澱神/荒魂獣/棄物/擬神兵）を基本軸として管理。
- 武具データへ `TsukumogamiState` と履歴密度を追加し、敵化/味方化分岐をデータ上で担保。
- 代受苦の処理に `Remnant_Bone` 生成と `Global_Daijuku_Count` 加算を追加。
- 付喪神覚醒条件と棄物化条件をマスタ化し、シナリオ依存のハードコードを回避。
- 行者うかみ再加入後〜別天津神撃破までの「うかみ本人のみ離脱不可（常世・黄泉の国・黄泉比良坂）」を `Party_Area_Constraint_Master` と進行フラグで管理する方針を追加。
- 拠点の神社建立機能に対応するため、`Shrine_Part_Master`・`Shrine_Layout_Data`・`Shrine_Faith_Master` を追加し、御霊と受容力の紐付けを行う。
- ワープネットワーク対応マスタとして `Shrine_Network_Master` と `FastTravel_Master` を追加し、社間接続と演出データを管理する。  
- **回路データ:** `Shrine_Part_Master` に `PartType` と `Impedance` を追加し、回路シミュレーションを可能にする。
- **風化データ:** （廃止）当初は仮設ラインの風化を管理していたが、永続的な祈り場方式へ変更されたため本項は不要。

## 6. 会話ログ参照（根拠）

- 参照元: `チャット履歴/gemini-conversation-2026-02-22-21-36-20.md`, `チャット履歴/gemini-conversation-2026-02-24-21-53-06.md`
- 主要根拠トピック:
  - 摩擦係数を含む耐久減衰式
  - 神写し理解度閾値と共鳴倍率のデータ管理
  - 代受苦発動条件と魂のイデア継承
  - 進行フラグ（うかみ加入/離脱/帰還、カガセオ試練、別天津神撃破）
  - 雑魚敵系統の拡張に伴う敵行動タグ設計
  - 付喪神の敵味方分岐を支える状態管理項目

## 7. ビジュアルデータ運用メモ（2026-02-24）

- 生成物アセットのメタデータには `PromptSetId` を必須付与し、再生成時の再現性を担保する。
- `AncientConstraint=true` のアセットは、レビュー時に西洋甲冑/SF意匠の混入チェックを必須にする。
