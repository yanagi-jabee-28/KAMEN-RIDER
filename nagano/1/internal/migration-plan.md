---
title: Migration plan — split `hero-design-alpsgear.md`
kind: design
audience: internal
owners: [docs-maintainers]
status: draft
references: [AGENTS.md]
version: 0.1
---

# Migration plan — hero-design-alpsgear.md → modular docs
目的: 既存の大型ドキュメントを AGENTS.md の設計思想に従って安全に分割し、CI とレビューで品質を担保する。

## 1. 変更サマリ（今回のコミットに含める項目）
- 新規ファイル: `design/worldbuilding.md`, `design/forms.md`, `scripts/ep01-initial-transformation.md`, `docs/internal/migration-plan.md`
- 保存: 完全版を `legacy/hero-design-alpsgear-full.md` に保管
- 既存 `hero-design-alpsgear.md` は短い INDEX に差し替え

## 2. 手順（開発者向け）
1. 新ブランチ作成: `docs/split-hero-design`
2. 新ファイルを追加（このPRに含める）
3. `hero-design-alpsgear.md` を INDEX に差し替え（リンクと移行注記を追加）
4. CI: markdownlint + front‑matter チェックを通す
5. PR: RFC スタイルの本文（変更理由、影響範囲、レビュワー）を作成
6. マージ後: レンダリング確認、docs/public の短縮版更新

## 3. テスト & QA
- 表示確認: GitHub Pages/markdown renderer で目次と相互リンクをチェック
- 参照検証: `references:` にある CSV が実在するか自動チェック
- レビュー: worldbuilding + scripts + legal（表現面）の3チームレビューを必須にする

## 4. ロールバック手順
- 未マージ: ブランチを削除して破棄
- マージ済: 1) Revert コミット 2) 緊急パッチで元の `hero-design-alpsgear.md` を復元（legacy を source とする）

## 5. PR テンプレ（コピーして利用）
Title: docs: split `hero-design-alpsgear.md` into modular files
Body:
- 概要（1‑2行）
- 変更点（ファイル一覧）
- 理由（AGENTS.md の『分割ルール』に準拠）
- 影響範囲（CI・リンク・参照データ）
- レビュワー候補: @worldbuilding‑team, @scripts‑team, @legal

---

作業完了後に PR を自動生成します（`gh pr create --fill` が使える場合）。