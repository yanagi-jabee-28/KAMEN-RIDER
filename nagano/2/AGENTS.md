---
title: 長野県ご当地ヒーロー企画創作ガイドライン (Project AGENTS) v2.0
kind: guideline
audience: internal|contributors
owners: [creative-leads, worldbuilding-team]
status: draft
version: 2.0
references: [regions_nagano.csv, products_nagano.csv, wildlife_issues_nagano.csv, social_issues_nagano.csv, dialect_linguistic_traps_nagano.csv]
---

# 長野県ご当地ヒーロー企画創作ガイドライン — Project AGENTS v2.0 ✅

このドキュメントは、プロジェクト『四信戦士 シナノ・フォーゼ』において、長野県のリアルなデータと物語性を高次元で融合するための共通プロトコルです。人間・AIを含む全ての共同作業者は、本ガイドラインを参照し、主要設定ファイルには**準拠を強く推奨**します。

---

## A. 基本方針：3つの鉄則 (Core Principles) 🔧
1. 「事実」を物語の最強の武器にする (Fact‑Based Fiction)
   - 長野の地理・産業・歴史・食文化などの実データを、能力・弱点・物語展開の根拠にする。
   - NG: なんとなくのモチーフ → OK: `浅間山` の地熱データを参照した能力設定など。

2. 「光」と「影」を描き、深みを出す (Light & Shadow)
   - 地域の課題（影）を敵の動機やヒーローの葛藤に変換する。

3. 「なぜ？」から考え、期待を超える (First Principles)
   - 常に「なぜこの能力か？なぜこの敵か？」を第一に掘る。

---

## B. 適用範囲とオプトアウト (Scope & Governance) ⚖️
- 適用対象（強く推奨）: キャラクター設定、世界観（Bible）、メイン脚本。
- オプトアウト: 実験的サイドストーリー等はファイル先頭の front‑matter で明示すること。

```yaml
---
guidelines:
  adherence: optional   # required | recommended | optional | excluded
  reason: "Experimental spin-off"
---
```

---

## C. 創作プロセス：面白さを最大化する5ステップ (5‑Step Creative Flow) 🎯
1. Step 1 — 「長野の根っこ」を探す (Source Discovery)
   - 参照例: `products_nagano.csv`, `regions_nagano.csv`, `wildlife_issues_nagano.csv`
2. Step 2 — 「表と裏」を設定する (Dual Nature)
   - メリットとリスクを必ず併記する（例：強力な武器＝代償がある）
3. Step 3 — 「代償」を支払わせる (Cost & Consequence)
   - 物理的／社会的コストを物語に反映する
4. Step 4 — 「届けたい相手」を意識する (Targeting)
   - 解像度を子供／大人向けで切替える
5. Step 5 — 「物語のその後」を想像する (Evolution)
   - 戦いの社会的帰結（例：直売所が復活する等）を描写する

---

## D. データ活用マニュアル (Where to use which CSV) 📊
- `regions_nagano.csv` — 地域性、出身設定、対立軸
- `products_nagano.csv` — 能力源、回復アイテム、弱点の素材
- `wildlife_issues_nagano.csv` — 怪人モチーフ／生態系テーマ
- `social_issues_nagano.csv` — エピソードの社会的背景
- `dialect_linguistic_traps_nagano.csv` — セリフ監修（方言誤用禁止）

実装ルール: 各主要設定（キャラ／怪人／重要アイテム）には**最低1つの根拠ファイル**と該当行の参照を記載すること。

---

## E. 表現プロトコル：創る（内部）と見せる（外部）の分離 🧩
- 内部設計（Iceberg）: 詳細なSF考証・出典・検証は `docs/internal/` に保存
- 外部表現（Visible Tip）: 脚本・映像では「結論ファースト」「視覚で理解させる」を徹底

例: 内部には『EMMH の自己増殖メカニズム』を詳細に書き、脚本では「変身SE＋台詞」で要点のみ見せる。

---

## F. 禁止・注意事項 (Safety & Ethics) ⚠️
- 実在の被害（災害・事故）をそのまま描かない。被害者感情に配慮すること。
- 地域・個人・団体の差別や中傷は厳禁。実在企業を使う場合は名称変更またはリスペクト表現を必須とする。
- 地域ステレオタイプ化を避け、多面的な描写を行うこと。

---

## G. ファイル構成・命名規則 (Repository conventions) 🗂️
推奨構成（例）:

```
/bible/
  ├─ Shinano_Force_Settings.md
  ├─ character-profiles.md
  └─ mechanics.md
/scripts/
  ├─ ep01-first-contact.md
  └─ ep02-north-south.md
/data/
  ├─ products_nagano.csv  (読み取り専用)
  └─ ...
```

命名: スネーク/ケバブケース推奨。プレフィックス例: `spec-` (仕様), `script-` (脚本), `data-` (解析結果)

Front‑matter テンプレ（必須フィールド）:
- `title`, `kind`, `audience`, `owners`, `status`, `references`, `version`

CIチェック候補:
- front‑matter 必須フィールド検証
- `references:` に記載されたファイルが存在するかの検出

---

## H. 実務チェックリスト（PR のテンプレ） ✅
- [ ] この変更は単一責任か？
- [ ] 参照データ（CSV）を必ず記載したか？ (`references:`)
- [ ] 方言・文化表現は `dialect_linguistic_traps_nagano.csv` と突き合わせたか？
- [ ] 危険表現（災害・実名中傷）が含まれていないか？

---

## I. 付録：オプトアウト例／方言監修ワークフロー
- オプトアウトはファイル先頭の `guidelines.adherence` で管理
- 方言監修: 初稿→地域担当レビュー→言語学チェック（`dialect_linguistic_traps_nagano.csv` に照合）→最終反映

---

## Next actions (短期) — 推奨順序 🔜
1. このファイルを `2/AGENTS.md` としてコミットしてください（このリポジトリに追加済み）。
2. 主要ドキュメント（例: `1/hero-design-alpsgear.md`）をガイドラインに沿って**分割案**を作成する（必要なら自動分割プランを作成します）。
3. front‑matter と CI チェックを1つ追加し、PR テンプレに統合する（希望があれば PR を作成します）。

---

短く要約すると: **根拠→代償→社会的帰結** の順で設定を構築し、内部は深く、外部はシンプルに見せる。データ参照を必須化することで、長期的に愛される“長野らしい”世界観を作ります。✨

---

If you want: 1) 私が `1/hero-design-alpsgear.md` の分割プランを作成する、2) その分割を実際に行って PR を作る、または 3) CI チェックの雛形を追加する — どれを次に進めますか？
