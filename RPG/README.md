# RPG企画4 管理ツール (MVP)

`妖怪/RPG企画4` の設定矛盾を防ぐための管理ツールです。

## Purpose
- SSOTを `RPG/data/*.yaml` に集約
- 保存前に整合性チェック
- `RPG/output/*.md` を自動生成

## Structure
- `RPG/data/`: 編集対象のマスターデータ
- `RPG/schema/models.py`: Pydanticスキーマ
- `RPG/validators/consistency.py`: ドメイン整合性チェック
- `RPG/tools/build_docs.py`: CLIビルド（検証 + 生成）
- `RPG/app/streamlit_app.py`: Web UI
- `RPG/templates/`: Markdownテンプレート
- `RPG/output/`: 生成物

## Quick Start
1. 依存導入
```bash
pip install -r RPG/requirements.txt
```
2. CLIで検証 + 生成
```bash
python RPG/tools/build_docs.py
```
3. Streamlit UI起動
```bash
streamlit run RPG/app/streamlit_app.py
```

## Operating Rules
- 編集は `RPG/data/` を正本にする
- `RPG/output/` は生成物として扱う
- 旧語（例: キメラ、結和神）は履歴参照のみで、新規設計では使用しない
