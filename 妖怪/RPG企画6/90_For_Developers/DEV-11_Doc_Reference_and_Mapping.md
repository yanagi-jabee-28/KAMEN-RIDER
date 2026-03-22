# DEV-11 Doc Reference and Mapping

一般向け文書から分離した、実装参照の逆引き表です。

## 0. 運用方針（公開文書との責務分離）

- 公開文書では、物語理解に不要なフラグIDや実装識別子を直接表示しない。
- 退避したID・内部名・順序依存は本ファイルで管理し、追跡可能性を維持する。
- 体験記述を変更した際は、本ファイルの対応行を先に更新してからDEV-10へ反映する。

## 1. 三点対応表（公開節 ↔ 実装ID/フラグ ↔ DEV-10節）

| 公開文書の節 | 実装ID / フラグ | DEV-10参照節 | 更新責任文書 | 更新順 |
|---|---|---|---|---|
| SYS-20: 1.1 核心的なテンション・ループ | `Can_Use_Daijuku`, `Use_Extreme_Daijuku` | 1.3 / 2.2 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 1.2 修復と継承の感情曲線 | `Core_of_Regret.Created` | 1.4 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 2 三条の熱源 | `Kakkon_Value`, `Jonetsu_Value`, `Durability_new` | 1.1 / 1.2 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 3 境界状態 | `State_Shigurui`, `State_Karakara` | 1.1 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 3.3 境界状態の復帰フロー（判断版） | `State_Karakara`, `State_Shigurui`, `State_Yomotsu_Curse`, `Disable_Standard_Recovery` | 1.1 / 1.6 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 3.2 空殻（タグ限定復帰） | `SkillTag.JONETSU_RECOVERY`, `SkillTag.MORALE_BOOST`, `SkillTag.RESTART`, `SkillTag.GEKIYAKU`, `Can_Recover_From_Karakara` | 1.8 | SYS-20 / SYS-22 | DEV-11 → DEV-10 → SYS-20/SYS-22 |
| SYS-20: 4.2.1 代受苦/極大代受苦の判断フロー | `Can_Use_Daijuku`, `Can_Use_Extreme_Daijuku`, `Weapon_Destroyed`, `Generate_Core_of_Regret` | 1.3 / 2.2 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 4.4.1 位相ごとの戦術優先順位 | `Heal_Output_Mult`, `SelfCost_Mult`, `Recovery_Reversal_Rate`, `Jonetsu_Gain_Mult` | 1.6 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 4.3 固有戦術の体感差（マヒト鍛造段階） | `MAHITO_JOINED_ACT2`, `FORBIDDEN_FORGING_LV2_UNLOCKED`, `TAKEMIKAZUCHI_REVENGE_CLEARED` | 2.2 / 2.5 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| SYS-20: 4.8 黄泉戸喫のリスク運用（段階解放） | `YOMOTSU_ENCOUNTERED`, `YOMOTSU_UNDERSTOOD`, `Yomotsu_Command_Visible`, `Can_Use_Yomotsu_Command`, `Auto_Consume_Yomotsu_By_Ukami` | 1.6 | SYS-20 / NAR-10 | DEV-11 → DEV-10 → SYS-20/NAR-10 |
| SYS-20: 4.3 固有戦術の体感差（ミコト二刀流ロック） | `Can_Unlock_Dual_Stance`, `Sync_Control_Occupied_By_Ukami`, `UKAMI_LEFT_KATSURAGI`, `Mikoto_Gauntlet_Permanent` | 1.5 | SYS-20 / NAR-10 | DEV-11 → DEV-10 → SYS-20/NAR-10 |
| SYS-20: 4.7 行者還し | `GYOJAGAESHI_CLEARED`, `SUSANOO_TRIAL_UNLOCKED` | 2.4 / 2.5 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| NAR-10: 第1幕終盤（白堊の回廊への初突入） | `WHITE_CORRIDOR_INITIAL_FAILED` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第2幕序盤（タチバナ加入） | `TACHIBANA_JOINED_ACT2_EARLY` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第2幕序盤～中盤（灼熱たたら場とマヒト加入） | `MAHITO_JOINED_ACT2` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第2幕中盤（禁忌鋳造Lv2の目覚めと白堊の突破） | `FORBIDDEN_FORGING_LV2_UNLOCKED`, `WHITE_CORRIDOR_CLEARED` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第2幕後半（葛城山の喪失と継承） | `UKAMI_LEFT_KATSURAGI` | 2.3 / 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第3幕後半（タケミカヅチ雪辱戦と野外Lv2拡張） | `TAKEMIKAZUCHI_REVENGE_CLEARED`, `MAHITO_FIELD_LV2_UNLOCKED` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第3幕（偽終幕と絶望の真実） | `TSUKUYOMI_FAKE_LASBOSS` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 位相と戦術の橋渡し（読解用） | `Field_State`, `StoryFlag.*`（幕遷移関連） | 1.6 / 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第4幕（再接続） | `UKAMI_RETURNED_YOMOTSU` | 1.5 / 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 終幕（永遠の拒絶） | `ETERNITY_REJECTED` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 真裏ボス導線 | `OROCHI_TAIL_BREACHED`, `AMENO_MURAKUMO_AWAKENED` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| SYS-30: 2.2 Status_Effect_Master（毒/混乱/服従の深度運用） | `POISON`, `CONFUSION`, `CHARM`, `StatusDepth_Internal` | 1.1 / 1.6 | SYS-30 | DEV-11 → DEV-10 → SYS-30 |
| SYS-30: 2.2 Status_Effect_Master（武器劣化3段階） | `WEAPON_SABI`, `WEAPON_SHOKU`, `WEAPON_KUCHI`, `Durability_new` | 1.2 / 1.6 | SYS-30 | DEV-11 → DEV-10 → SYS-30 |
| SYS-30: 2.4 Weapon_Evolution_Master | `OROCHI_TAIL_BREACHED` | 2.5 | SYS-30 | DEV-11 → DEV-10 → SYS-30 |
| SYS-30: 2.7b 耐性語の読み方（公開側定義） | `KUSANAGI_WEAR`, `HISTORY_ERASE`, `Durability_new` | 1.2 / 1.6 | SYS-30 | DEV-11 → DEV-10 → SYS-30 |
| SYS-30: 2.8a 属性×状態異常×位相の干渉早見表 | `ICE_STAGNATION`, `ICE_COOLING`, `PURE_PROVISION`, `WHITE_OATH` | 1.6 / 1.7 | SYS-30 | DEV-11 → DEV-10 → SYS-30 |
| ART-40: 付喪神化の視覚定義 | `Is_Tsukumogami`, `Generate_Core_of_Regret` | 1.3 / 1.4 | DEV-12 | DEV-11 → DEV-10 → DEV-12 |

## 1.5 保護語彙の三点対応（WRD-02基準）

| 保護語彙（公開側） | 実装ID / 判定軸 | DEV-10参照節 | 更新責任文書 | 更新順 |
|---|---|---|---|---|
| 活魂 | `Kakkon_Value`, `State_Dead` | 1.1 | WRD-02 / SYS-20 | DEV-11 → DEV-10 → WRD-02/SYS-20 |
| 情念 | `Jonetsu_Value`, `State_Karakara` | 1.1 | WRD-02 / SYS-20 | DEV-11 → DEV-10 → WRD-02/SYS-20 |
| 武器耐久度 | `Durability_new`, `Weapon_Durability` | 1.2 / 1.3 | WRD-02 / SYS-20 | DEV-11 → DEV-10 → WRD-02/SYS-20 |
| 代受苦 | `Can_Use_Daijuku`, `Incoming_Damage=0` | 1.3 / 2.2 | WRD-02 / SYS-20 | DEV-11 → DEV-10 → WRD-02/SYS-20 |
| 極大代受苦 | `Use_Extreme_Daijuku`, `Weapon_Destroyed` | 1.3 / 2.2 | WRD-02 / SYS-20 | DEV-11 → DEV-10 → WRD-02/SYS-20 |
| 空殻 | `State_Karakara`, `Can_Recover_From_Karakara`, `SkillTag.JONETSU_RECOVERY`, `SkillTag.MORALE_BOOST`, `SkillTag.RESTART`, `SkillTag.GEKIYAKU` | 1.1 / 1.8 | WRD-02 / SYS-20 / SYS-22 | DEV-11 → DEV-10 → WRD-02/SYS-20/SYS-22 |
| 死狂い | `State_Shigurui`, `Has_Shigurui_Passive` | 1.1 | WRD-02 / SYS-20 | DEV-11 → DEV-10 → WRD-02/SYS-20 |
| 位相 | `StoryFlag.*`（幕遷移関連） | 2.5 | WRD-02 / NAR-10 | DEV-11 → DEV-10 → WRD-02/NAR-10 |
| 金継ぎ | `Generate_Core_of_Regret`, `Kintsugi_Transfer_Executed` | 1.3 / 1.4 | WRD-02 / SYS-20 | DEV-11 → DEV-10 → WRD-02/SYS-20 |
| 黄泉戸喫 | `Use_Item==Yomotsu_Mud_Fruit`, `YOMOTSU_ENCOUNTERED`, `YOMOTSU_UNDERSTOOD`, `Yomotsu_Command_Visible`, `Can_Use_Yomotsu_Command`, `Auto_Consume_Yomotsu_By_Ukami`, `State_Yomotsu_Curse` | 1.6 | WRD-02 / SYS-20 / NAR-10 | DEV-11 → DEV-10 → WRD-02/SYS-20/NAR-10 |
| 継承（技継承/武器継承） | `ForcedSkills.*`, `Core_of_Regret.Stored_Traits`, `Kintsugi_Transfer_Executed` | 1.4 / 2.3 | WRD-02 / NAR-10 / SYS-20 | DEV-11 → DEV-10 → WRD-02/NAR-10/SYS-20 |
| 武器劣化段階（錆/蝕/朽） | `WEAPON_SABI`, `WEAPON_SHOKU`, `WEAPON_KUCHI`, `Weapon_Degradation_Stage`, `Durability_new` | 1.2 / 1.6 | WRD-02 / SYS-20 / SYS-30 | DEV-11 → DEV-10 → WRD-02/SYS-20/SYS-30 |
| 実体二刀流（ミコト） | `Can_Unlock_Dual_Stance`, `DualStanceActive`, `Sync_Control_Occupied_By_Ukami`, `Mikoto_Gauntlet_Permanent` | 1.5 | WRD-02 / SYS-20 / NAR-10 | DEV-11 → DEV-10 → WRD-02/SYS-20/NAR-10 |

## 1.6 整合性課題の解消状況

次の2点は仕様確定と同期反映が完了した。

| 論点 | 状態 | 確定内容 | 関連文書 |
|---|---|---|---|
| マヒト鍛造Lv2解放条件 | 解消済み | 拠点は加入直後、野外Lv2は雪辱戦突破後に固定 | SYS-20 / NAR-10 / DEV-10 / DEV-11 |
| 黄泉戸喫の説明密度 | 解消済み | 遭遇→理解→解放の段階導線に固定し、任意使用と行者うかみ自律摂取を併用 | SYS-20 / NAR-10 / WRD-02 / DEV-10 / DEV-11 |

## 2. イベント起点の逆引き（フラグ優先）

| 物語イベント | 対応フラグ | DEV-10参照節 | 公開側の主参照 |
| --- | --- | --- | --- |
| ツクヨミ撃破・偽終幕 | `TSUKUYOMI_FAKE_LASBOSS` | 2.5 | NAR-10 |
| 行者うかみ帰還成立 | `UKAMI_RETURNED_YOMOTSU` | 1.5 / 2.5 | NAR-10 / SYS-20 |
| 行者還し完了 | `GYOJAGAESHI_CLEARED` | 2.4 / 2.5 | NAR-10 / SYS-20 |
| スサノオ試練解禁 | `SUSANOO_TRIAL_UNLOCKED` | 2.4 / 2.5 | NAR-10 |
| スサノオ試練突破 | `SUSANOO_TRIAL_CLEARED` | 2.5 | NAR-10 |
| オロチ尾破断 | `OROCHI_TAIL_BREACHED` | 2.5 | NAR-10 / SYS-30 |
| 天叢雲剣覚醒 | `AMENO_MURAKUMO_AWAKENED` | 2.5 | NAR-10 / SYS-30 |

## 3. 参照運用ルール（短縮版）

| 変更対象 | 最初に更新 | 次に更新 | 最後に更新 |
|---|---|---|---|
| 体験記述の変更（公開文書） | DEV-11 | DEV-10 | 該当公開文書 |
| 計算式/条件変更（実装正本） | DEV-11 | DEV-10 | 公開文書（必要時） |
| フラグ増減 | DEV-11 | DEV-10 2.5 | NAR-10 / SYS-20 / SYS-30 |
| アート実務変更 | DEV-11 | DEV-12 | ART-40 |
