---
uid: [SYS-20]
role: systems-and-flow
status: active
depends_on:
  - SYS-30_Data_and_Logic_Architecture.md
  - ../00_Welcome_and_Introduction/WRD-01_Core_Vision_and_Theme.md
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
influences:
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - SYS-21_Enemy_Ecology_and_UI.md
  - SYS-22_Skill_Matrix_PlayerFacing.md
  - ../99_Archive_and_References/WRD-99_Archive_and_Changelog.md
---

# [SYS-20] Game Systems and Flow

このファイルは「プレイヤー体験設計の視点」から書かれています。遊ぶ人が何に悩み、何を選び、何を気持ちよく乗り越えるかを説明します。

## 先に結論

このゲームは、壊れることを前提に戦うRPGです。

- 壊れない最強装備を探すゲームではない
- 壊れた武器をつなぎ直し、履歴を育てるゲームである

初見向けの最短読本は [00_Beginner_Guide.md](00_Beginner_Guide.md) を参照。

## 用語の平易化

- 活魂（Kakkon）: 体力。ゼロで倒れる
- 情念（Jonetsu）: 気力。被弾や仲間危機で燃え、技の燃料になる
- 武器耐久度: 武器が壊れるまでの残量
- Tick遅延: 敵の行動順を遅らせること
- ヘイト管理: 敵の注意を自分へ引きつけること（壁役の仕事）
- 金継ぎと付喪神化: 同じ武器を修理し続けると魂が宿り、必殺技が解禁される育成サイクル（実装条件は [SYS-30_Data_and_Logic_Architecture.md](SYS-30_Data_and_Logic_Architecture.md) を参照）

## 体験ループ

1. 受ける
- 神側は予測可能で最適化された行動をしてくる
- プレイヤー側はまず圧を受ける

2. 崩す
- 盾役が注意を引き受ける
- 攪乱役が行動順を乱す
- 呪術・薬師が防御や行動制御を崩す

3. つなぐ
- 破損した武器を金継ぎする
- 同じ武器を使い続け、履歴を戦術価値に変える

4. 反転する
- 付喪神化が進むほど、苦境を返す手札が増える
- ただしコストも重くなり、無計画な連打は破綻する

## 情念の回復手段（プレイ感を支える核）

- ジャストアクション: ギリギリ防御や回避が成功すると大きく回復
- 連撃熱伝導: 味方連携が成立すると次行動者の情念が戻る
- 星砂の息吹: 1ターン使って情念を大きく回復する基本行動

この3手段で「攻めたいのに燃料が足りない」を解消する。

## ロールと幕の詳細参照

- ロール別の優先行動: [SYS-22_Skill_Matrix_PlayerFacing.md](SYS-22_Skill_Matrix_PlayerFacing.md)
- 幕ごとの背景と演出意図: [../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md](../01_Story_and_Characters/NAR-11_Act_Detail_Guide.md)

## 境界状態（平易版）

- 死狂い: 活魂が尽きても情念が残ると発生。短時間だけ理不尽を返せる
- 空殻: 情念が尽きた状態。技が回らず、被弾が重くなる
- 完全なる死: 活魂と情念の両方が尽きるか、アンカーを失った状態で活魂が尽きる

境界状態は「逆転の窓」でもあり「崩壊の直前」でもある。

## 第2幕の敗北設計（白堊の回廊）

- 目的: 早い段階で「今の装備では通らない」と体感させる
- 効果: マヒト加入と禁忌鍛造の価値を、説明ではなく実感で理解させる
- ルール: ここでの敗北感は失敗ではなく、次の学習導線の起点

## このファイルで扱う範囲

- 扱う: 体験意図、学習導線、ロール設計
- 扱わない: 数式、閾値、フラグ、疑似コード

## このファイルに含めないもの

- ダメージ計算式
- フラグ条件の擬似コード
- 閾値や係数の実装定義

これらは正本 [SYS-30_Data_and_Logic_Architecture.md](SYS-30_Data_and_Logic_Architecture.md) に隔離する。

## 詳細の読み分け

- 初見導線: [00_Beginner_Guide.md](00_Beginner_Guide.md)
- 敵生態系とUI: [SYS-21_Enemy_Ecology_and_UI.md](SYS-21_Enemy_Ecology_and_UI.md)
- 術式索引: [SYS-22_Skill_Matrix_PlayerFacing.md](SYS-22_Skill_Matrix_PlayerFacing.md)
