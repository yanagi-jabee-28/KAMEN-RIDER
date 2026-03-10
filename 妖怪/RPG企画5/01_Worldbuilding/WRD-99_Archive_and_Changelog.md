---
uid: [WRD-99]
role: archive-and-changelog
status: active
depends_on:
  - WRD-01_Core_Vision_and_Theme.md
  - ../03_Systems/SYS-20_Game_Systems_and_Flow.md
  - ../03_Systems/SYS-30_Data_and_Logic_Architecture.md
influences:
  - ../README.md
---

# [WRD-99] Archive and Changelog

## 目的

- 不採用案と変更理由を記録し、再発を防ぐ。
- 設計変更の履歴をUID単位で追跡可能にする。

## 初期移行記録

- 2026-03-11: `[ARC-00]`導入。変更時の影響分析を義務化。
- 2026-03-11: `[ARC-01]`導入。UIDとメタデータ運用を正本化。
- 2026-03-11: `RPG企画4`の7正本について、`RPG企画5`向け移行マップと新構造を定義。
- 2026-03-11: `RPG企画4/README_FREEZE.md` を追加し、RPG企画4を参照専用へ凍結。
- 2026-03-11: `SYS-30` と `SYS-20` をRPG企画4から再編集移行開始（`status: migrating`）。
- 2026-03-11: `ARC-00` に語彙変換辞書を追加し、禁止語の置換基準を正本化。
- 2026-03-11: `WRD-01` と `NAR-10` の旧参照（`10_*` / `20_*` / `30_*`）をRPG企画5パスへ統一し、禁止語（`AI` `データ` `アルゴリズム` `クラッシュ`）の正規化を完了。
- 2026-03-11: `WRD-01` のプロジェクトコードを `RPG企画5` へ修正。`SYS-20` / `SYS-30` の旧短縮参照（`99_*` / `10_*` / `30_*` / `40_*`）をRPG企画5の正本参照へ統一。

## 廃棄語彙ポリシー

- SF的語彙は廃棄語彙として保持し、正本へ再流入させない。
- 旧語の再利用時は、先にこのファイルへ理由と置換先を追記する。
