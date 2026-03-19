---
uid: [ARC-INDEX]
project_code: RPG企画6
title: アシブネノミコト 〜天降る御子と、星屑の大地〜
status: active
owner: Architecture Guardian
depends_on:
  - ../90_For_Developers/ARC-00_Implementation_Charter.md
influences:
  - WRD-01_Core_Vision_and_Theme.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../99_Archive_and_References/REF-50_Reference_DQ_Master_Data.md
---

# RPG企画6 — アシブネノミコト 〜天降る御子と、星屑の大地〜

壊れながらも生き続ける命と、悲しみをなくすために世界を止める神が衝突する、和風神話ダークファンタジーRPGです。

この文書は、初見プレイヤーと初参加メンバーのための案内所です。

## 30秒で分かるこのゲーム

- 一言: 壊れた武器を金継ぎで直しながら進む、泥臭い再生RPG
- 戦いの軸: 活魂（体力）・情念（気力）・武器耐久度（壊れるまでの残量）
- 物語の軸: 永遠の静止を望む神と、有限の命を選ぶ人の衝突
- 主人公: 感情のない器だったミコトが、人として生きることを選び直す旅

## 最初に知ること

- 世界の対立構造: 命の還流 vs 永遠の停滞
- 独自の体験: 壊れた武器を金継ぎでつなぎ、痛みを分かち合って戦う
- 主人公像: 空の器だったミコトが、仲間との旅でただの人間へ変わる

## 世界の舞台

| 場所 | 役割 |
|---|---|
| 高天原 | 完璧だが冷たい、変化のない神の領域 |
| 葦原中国 | 人が傷つき、直し、次へ渡す地上 |
| 黄泉の国 | 未練が溜まり、回復すら毒に転ぶ領域 |
| 常世の国 | 神が目指す「永遠保存」の最終牢獄 |
| 根の堅州国 | 神の理が届かない、反逆後の到達点 |

## 主要人物（物語の見取り図）

| 区分 | 名前 | 立ち位置 |
|---|---|---|
| 主人公 | ミコト | 天の器として造られ、地上で人へ変わる |
| 仲間 | うかみ | 最前線で仲間を守る壁役 |
| 仲間 | スクナ | 劇薬と冷徹な判断で崩しを作る薬師 |
| 仲間 | ウズ | 行動順と予測を乱す攪乱役 |
| 仲間 | タチバナ | 自傷を代償に敵全体を弱める呪術役 |
| 仲間 | マヒト | 壊れた武具を再起動させる鍛冶師 |
| 仲間 | ワカヒコ | 危険行動を止める狙撃手 |
| 神側 | イザナギ | 世界停止を推し進める最終意志 |
| 神側 | アマテラス | 時を止める凍結の管理者 |
| 神側 | ツクヨミ | 処刑者であり同時に仮死維持の守護機能を持つ |
| 神側 | カガセオ | 天へ最初に反逆した星神 |

## 5幕のあらすじ

1. 第1幕【胎】: 漂着したミコトが、うかみとスクナと旅立つ
2. 第2幕【融】: 白堊の回廊で敗北し、禁忌鍛造へ至る
3. 第3幕【熾】: 真実と対峙し、神の理への反逆を選ぶ
4. 第4幕【結】: 黄泉で再起動し、天岩戸をこじ開ける
5. 終幕【還】: 劣化と死を受け入れ、永遠を拒絶する

## 遊び方の骨格

| 何を管理するか | どう感じるか | 失敗すると |
|---|---|---|
| 活魂（体力） | 前線に立てるか | ゼロで倒れる |
| 情念（気力） | 技を回せるか | 枯れると空殻になり行動が弱る |
| 武器耐久度 | 攻勢を維持できるか | 壊れて使用不能、修復が必要 |

死狂い（Shigurui）や付喪神化は「逆転の手札」です。強力ですが、無計画に使うと自壊します。

## 読者ガイド

- 物語を追う: [../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md](../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md)
- 幕の詳細を読む: [../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md](../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md)
- 戦い方を知る: [../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md](../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md)
- 初見向け最短ルート: [../02_How_to_Play_and_Mechanics/00_Beginner_Guide.md](../02_How_to_Play_and_Mechanics/00_Beginner_Guide.md)
- ビジュアル方針: [../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md](../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md)
- 開発者向け詳細: [../90_For_Developers/ARC-00_Implementation_Charter.md](../90_For_Developers/ARC-00_Implementation_Charter.md) と [../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md](../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md)

## 主人公と仲間の役割

- ミコト: 仲間の技を写し取る万能役
- うかみ: 攻撃を引き受ける盾役
- スクナ: 防御を溶かし、危機を劇薬でつなぐ薬師
- ウズ: 行動順とリズムを崩す攪乱役
- タチバナ: 呪術で敵全体を弱体化する削り役
- マヒト: 武器を破壊し、鍛え直して再起動させる鍛冶師
- ワカヒコ: 重要局面で敵行動を止める狙撃手

## よくある疑問

| 疑問 | 回答 |
|---|---|
| なぜ武器が壊れるのか | 破損と修復の履歴そのものを成長にするため |
| 神は悪なのか | 悪ではない。悲しみを消したいという別の救済思想 |
| ドラクエ要素はあるのか | 参照はするが直輸入はしない。必ず本作語彙へ翻訳する |

---

## 編集・運用ルール（下位配置）

- Zero-Loss原則: 固有語彙、数値、条件式を削らない
- 保護語彙: 情念 / 活魂 / 武器耐久度 / 付喪神化 / 代受苦 / 極大代受苦 / 神の理 / 金継ぎ / 剥落の星屑 / 神託崩壊 / 無菌の帳 / 血の泥沼
- 正本優先順: SYS-30 → SYS-20 → WRD-01
- 実装規約の正本: [../90_For_Developers/ARC-00_Implementation_Charter.md](../90_For_Developers/ARC-00_Implementation_Charter.md)
