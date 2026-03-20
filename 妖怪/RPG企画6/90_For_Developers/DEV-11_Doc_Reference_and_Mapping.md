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
| SYS-20: 4.7 行者還し | `GYOJAGAESHI_CLEARED`, `SUSANOO_TRIAL_UNLOCKED` | 2.4 / 2.5 | SYS-20 | DEV-11 → DEV-10 → SYS-20 |
| NAR-10: 第2幕（葛城山） | `UKAMI_LEFT_KATSURAGI` | 2.3 / 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第3幕（逆転する勝利） | `TSUKUYOMI_FAKE_LASBOSS` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 第4幕（再接続） | `UKAMI_RETURNED_YOMOTSU` | 1.5 / 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 終幕（永遠の拒絶） | `ETERNITY_REJECTED` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| NAR-10: 真裏ボス導線 | `OROCHI_TAIL_BREACHED`, `AMENO_MURAKUMO_AWAKENED` | 2.5 | NAR-10 | DEV-11 → DEV-10 → NAR-10 |
| SYS-30: 2.4 Weapon_Evolution_Master | `OROCHI_TAIL_BREACHED` | 2.5 | SYS-30 | DEV-11 → DEV-10 → SYS-30 |
| ART-40: 付喪神化の視覚定義 | `Is_Tsukumogami`, `Generate_Core_of_Regret` | 1.3 / 1.4 | DEV-12 | DEV-11 → DEV-10 → DEV-12 |

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
