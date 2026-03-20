# DEV-11 Doc Reference and Mapping

一般向け文書から分離した、実装参照の逆引き表です。

## 1. Moved from SYS-20 (4.9)

| プレイヤー体験 | SYS-30対応箇所 |
|---|---|
| 「守るために壊す」代受苦の決断 | 1.4 修復と鍛造の循環（Kintsugi Cycle） |
| ロスト武器が次世代へ継承される感覚 | 1.5 付喪神化と情念の核継承 |
| ミコト/ワカヒコ/うかみで戦い方が変わる感覚 | 1.6 固有戦術ロジック（ミコト/ワカヒコ/うかみ） |
| 位相ごとにセオリーが反転する緊張 | 1.7 位相ギミック（無菌の帳 / 血の泥沼 / 黄泉戸喫） |
| 定石が読まれる終盤の圧迫感 | 1.8 特殊敵と神AI学習段階 |
| 祈りと泥の履歴で神器が成立する手触り | 2.9 星土の脈継ぎ（神社連動） |
| クリア後儀式が旅の総量で解放される納得感 | 3.3 行者還し（Gyoja Gaeshi）条件式 |
| ワカヒコ加入戦だけ反動ルールが切り替わる納得感 | 1.6 固有戦術ロジック（ミコト/ワカヒコ/うかみ） |
| 鍛造が段階解禁で広がる手応え | 3.1 Story_Flag_Master / Camp_Maintenance_Logic（拠点/野営の段階解禁） |

## 2. Moved from SYS-22 (参照マップ)

| 知りたい内容 | 参照先 |
|---|---|
| ダメージ式、倍率、閾値 | SYS-30「Data and Logic Architecture」 |
| 状態異常IDと効果定義 | SYS-30「Status_Effect_Master（状態異常定義）」 |
| 敵の行動パターン | SYS-30「Enemy_Master」 |
| 敵Tierと危険要因 | SYS-30「Enemy_Tier_Template_Master（完全版）」 |
| 氷の静止/冷却分岐 | SYS-30「氷属性サブタイプ（静止/冷却）」 |
| 黄泉戸喫のリスクと解除 | SYS-30「黄泉戸喫・黄泉の呪い（確定仕様）」 |
| 行者還しの条件式 | SYS-30「行者還し（Gyoja Gaeshi）条件式」 |
| 幕の物語背景 | NAR-10「Narrative, Characters, and Act Guide」 |

## 3. Moved from NAR-10 (実装フラグ順序対応)

| 物語イベント | 対応フラグ |
| --- | --- |
| ツクヨミ撃破・偽終幕 | TSUKUYOMI_FAKE_LASBOSS |
| 行者うかみ帰還成立 | UKAMI_RETURNED_YOMOTSU |
| 行者還し完了 | GYOJAGAESHI_CLEARED |
| スサノオ試練解禁 | SUSANOO_TRIAL_UNLOCKED |
| スサノオ試練突破 | SUSANOO_TRIAL_CLEARED |
| オロチ尾破断 | OROCHI_TAIL_BREACHED |
| 天叢雲剣覚醒 | AMENO_MURAKUMO_AWAKENED |
