# KAMEN-RIDER

このリポジトリは「仮面ライダー」系の設定・構想・プロット・素材をまとめるための個人用ワークスペースです。

---

## 📌 目的
- 世界観設定、シナリオ、キャラクター、メカニクスなどのアイデアを文章化・整理する
- Markdown 形式での編集を中心とし、必要に応じて PDF や資料化を自動生成する
- 長期的な知見・調査を蓄積し、アップデートしやすくする

---

## 🗂️ リポジトリ構成（ざっくり）
- `AGENTS/`：AI エージェント用プロンプト・設定
- `妖怪/`、`ナノマシン/`、`亜人/` など：企画別の構造化ドキュメント
- `Scripts/`：Markdown の結合・PDF 出力などのツール群
- `Legacy/`：過去の調査・メモ

---

## 🛠️ 使い方（典型的なワークフロー）
### 1) Markdown を編集
- フォルダ別に分かれている MD ファイルを更新

### 2) Markdown を結合・PDF 出力
- `Scripts/merge_md.py`：Markdown を結合して1つのファイルを作る
- `Scripts/export_md_pdf.py --keep-temp`：PDF を生成（内部で `merge_md.py` を利用）

```powershell
python Scripts/export_md_pdf.py --keep-temp
```

---

## 🧩 Windows の `desktop.ini` について（無視設定）
このリポジトリでは以下の対応を行い、Windows が自動生成する `desktop.ini` を **Git 管理対象から除外**し、**VS Code で表示しない**ようにしています。

### ✅ 現在の設定内容
- `.gitignore` に `desktop.ini` と `**/desktop.ini` を追加
- `.vscode/settings.json` で `files.exclude` に `**/desktop.ini` を追加

### 🔁 もし `desktop.ini` を将来必要とする場合の戻し方
1. `git status` で `desktop.ini` が現れるか確認
2. 追跡中なら（必要に応じて）`git rm --cached **/desktop.ini` を実行
3. `.gitignore` から `desktop.ini` の行を削除
4. `.vscode/settings.json` の `files.exclude` から `"**/desktop.ini": true` を削除

> 補足: `desktop.ini` は Windows がフォルダの表示設定やアイコン情報を保存するためのシステムファイルであり、通常はソース管理に含める必要はありません。

