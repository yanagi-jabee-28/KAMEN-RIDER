---
uid: [WRD-01]
role: core-vision-and-theme
status: active
depends_on:
  - ../90_For_Developers/ARC-00_Implementation_Charter.md
  - ../90_For_Developers/ARC-01_UID_Registry.md
influences:
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md
  - ../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../99_Archive_and_References/WRD-99_Archive_and_Changelog.md
---

# [WRD-01] Core Vision and Theme

このファイルは「世界観設計者の視点」から書かれています。何を正義とし、何を拒絶する物語かを定義する正本です。

## 読み方

1. まず「コア対立」で判断軸を固定する
2. 次に「デザイン原則」で仕様へ落とし込む
3. そのあと NAR-10 / SYS-20 / ART-40 へ展開する

## メタファー補助線

本ファイルには位相・物理・設計由来の語が含まれる。運用時は次の和語補助を使う。

- エントロピーの凍結: 一切の変化と崩壊を許さない完全な静止
- 引力: 抗いがたい熱のうねり
- SSOT: 唯一の正本となるマスターデータ
- 固相: 停滞の始まり
- 液相: 交じり合う摩擦
- プラズマ相: 臨界を超える熱量の爆発
- 再結晶: 砕けた破片の再構成
- 相転移: 永遠の拒絶と命の循環への回帰
- ルードナラティブ: 遊びの体験を通じた物語表現
- ホルミシス効果: 致死域の負荷で生命活性を引き出す逆説効果
- マチエール: 岩絵具の厚塗りが作る物理的な凹凸
- シンコペーション: 完璧な拍を崩す裏拍の乱れ

翻訳語彙の運用表は [../99_Archive_and_References/REF-51_Translation_Map.md](../99_Archive_and_References/REF-51_Translation_Map.md) を参照する。

## コア対立

- 天の理: 悲しみを消すため、世界を永遠の結晶へ固定する
- 地の情念: 傷と劣化を抱えたまま、命を次へ還流させる

本作は善悪の二元論ではなく、二つの救済思想の衝突として構成する。

## 時代考証の運用原則

- 神話語彙で説明できる揺らぎは許容する
- 祭具由来、神意由来、常世由来の異時代性は許容する
- 未来文明を直接示す描写は非許容とする

この原則により、神話世界の手触りを守る。

## 主人公ミコトの定義

- 起点: 感情を持たない処刑者として設計された空の器
- 断絶: カガセオとの決戦で情念逆流を受け、記録を焼失
- 漂流: 葦舟で捨てられ、現世へ押し戻される
- 変転: 仲間と破損の履歴を積むことで、ただの人間へ相転移する

補足:
- ミコトは本来、地上平定後に結晶世界を支える要石として設計されていた
- スサノオの反逆により、狭間から現世へ戻る一度きりの道が開いた
- タイトルの「アシブネ」は、この漂流神話の中心事実を指す

## 世界構造

- 高天原: 絶対零度の無菌領域。停滞の理が優先される
- 葦原中国: 死と修復が循環する地上世界
- 黄泉の国: 未練と静止が堆積し、回復すら綻びになる領域
- 常世の国: 永遠保存を完成させるための最終牢獄
- 根の堅州国: 神の理が届かない、反逆後の到達点

## デザイン原則

1. テーマ優先
- すべての仕様は「停滞 vs 還流」を体験として可視化する

2. 破損の肯定
- 強化ではなく、破損履歴をつなぐ行為を成長の中心に置く

3. 神話語彙の保持
- SF語彙をゲーム内テキストへ持ち込まず、神話語彙で統一する

4. 相転移の物語曲線
- 固相 → 液相 → プラズマ相 → 再結晶 → 相転移 の位相遷移を、幕構成と戦闘体験に同期させる

5. 神話翻訳の徹底
- 外部RPG記号はそのまま使わず、本作語彙へ翻訳して採用する

6. 便利機能の抑制
- 都合のよい万能機能を避け、代償と選択が残る仕様を優先する

## 外部参照の翻訳指針

- 例: テンション → 共鳴過熱（新ゲージ非採用）
- 例: メタル系 → 剥落の星屑（低確率混入の報酬型レア雑魚）
- 例: 反射 → 理の反射鏡（限定反射）

翻訳時は「名称」だけでなく「効果・条件・コスト・対象」をセットで置換する。

## 実装ドキュメントへの橋渡し

- 物語設計: [../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md](../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md)
- 体験設計: [../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md](../02_How_to_Play_and_Mechanics/SYS-20_Game_Systems_and_Flow.md)
- 数理正本: [../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md](../02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md)
- アート指針: [../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md](../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md)
