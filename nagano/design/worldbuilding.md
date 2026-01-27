---
title: Worldbuilding — Alps‑Gear
kind: design
audience: internal
owners: [worldbuilding-team]
status: draft
references: [regions_nagano.csv, timeline_statistics_nagano.csv, references_nagano.csv]
version: 0.1
---

# Worldbuilding — 信州アルプス・ギア（抜粋）

## 概要（結論先出し）
Alps‑Gear の世界観は「積層性」「適応力」「境界性」を軸に設計する。地理・産業・食文化など長野県実データを設定の根拠とし、敵モチーフや弱点、物語の代償をすべて現実の課題へ結びつける。

## キー事実と設定起点（データ紐付け）
- フォッサマグナ／高山帯（regions_nagano.csv） → 境界性・地形を物語装置にする。
- 精密機械・航空宇宙（products_nagano.csv） → フォームの技術的根拠（Alps/Gear の“精密”表現）。
- 野生動物被害・外来種（wildlife_issues_nagano.csv） → 敵のモチーフ（シカ、ブラックバス等）。
- 発酵・昆虫食（products_nagano.csv, lifestyle_details_nagano.csv） → 暴走克服ロジック（Prime Ferment）。

## 敵組織（要約）
- 名称: 海帝國 アトラン・ナシ
- 本質: 「海への憧れ」が集合的無意識として具現化した存在。外敵ではなく、地域の内的課題の寓意。
- 階層: 四方統領（北/東/中/南）→ 特異個体（地域課題ボス）→ 幹部群（外来種・害獣）

## 世界観ガイド（制作で必ず守ること）
- 最低1つのCSV/一次資料で設定を裏取りすること（検証の連鎖）。
- 社会問題を扱う際は、直接的な実名事件や被害描写を避ける（AGENTS.md:C 禁止参照）。
- 子供向け表現と大人向け深掘りは別ファイルで管理し、表現切替用の短縮版を `docs/public/` に置く。

## 参照（抜粋）
- regions_nagano.csv — 地域特性
- products_nagano.csv — 産業・食文化
- wildlife_issues_nagano.csv — 害獣・外来種データ
