# RPG企画5 - 20 Game Systems and Flow (システムと進行)

本ドキュメントはプレイヤー体験設計とUI方針を定義する。実装値・計算式は記述せず、`30_Data_and_Logic_Architecture.md` を参照する。

## 1. バトル哲学 [#ID:R5_Battle_Philosophy]
- 神の理: 予測可能な最適解を押し付ける。
- 人の理: ノイズと摩擦で予測を外す。
- 目標: うまさだけでなく、傷を引き受ける判断をゲームプレイ化する。

※コアリソースは `30_Data_and_Logic_Architecture.md` の [#ID:R5_Resource_Core] を参照。

## 2. 基本戦闘フロー [#ID:R5_Battle_Flow]
1. 状態把握（活魂/情念/耐久）
2. 行動選択（通常、特技、防御、代受苦）
3. 場ルール評価（無菌の帳/血の泥沼）
4. 結果反映（耐久劣化、境界状態遷移）

※境界状態の遷移条件は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Boundary_States] を参照。

## 3. 代受苦とリスク管理 [#ID:R5_Daijuku_Experience]
代受苦は「便利な火力ボタン」ではなく、武器履歴を賭ける契約行為として演出する。通常代受苦と極大代受苦は明確に体験を分ける。

※発動可否と継承処理は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Maintenance_Tiers] および [#ID:R5_Tsukumogami_Inheritance] を参照。

## 4. UI設計原則 [#ID:R5_UI_Principles]
- 新規ゲージを増やさない。
- 三条熱源の相互関係を一画面で読める構成にする。
- 破損・修復・継承の文脈をアイコンと短文で明示する。

※共鳴過熱の内部処理は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Resonance_Burst] を参照。

## 5. 進行ロックと学習曲線 [#ID:R5_Progression_Locks]
鍛造機能は段階解放とし、加入イベントの価値を分散させる。加入直後に全機能を開放しない。

※ロック条件は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Story_Flag_Master] と [#ID:R5_Maintenance_Tiers] を参照。

## 6. DQ翻訳導入方針 [#ID:R5_DQ_Translation_Usage]
外部RPG要素は、体験目的を保持したまま本作語彙に翻訳して導入する。名称・記号の直輸入はしない。

※語彙監査は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Forbidden_Terms_Guard] を参照。