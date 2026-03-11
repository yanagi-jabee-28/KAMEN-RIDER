---
uid: [ARC-00]
role: implementation-charter
status: active
depends_on:
  - 00_Governance/ARC-01_UID_Registry.md
influences:
  - 01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md
  - 02_Narrative/NAR-10_Narrative_and_Characters.md
  - 03_Systems/SYS-20_Game_Systems_and_Flow.md
  - 03_Systems/SYS-30_Data_and_Logic_Architecture.md
  - 04_Art/ART-40_Art_Direction_and_Assets.md
  - 05_References/REF-50_Reference_DQ_Master_Data.md
---

# アシブネノミコト 〜天降る御子と、星屑の大地〜


# [ARC-00] Architecture Guardian実装憲章

## 1. 世界観厳守ルール

- SF語彙を正本仕様から排除する。
- 禁止語の例: AI, ナノマシン, データ, アルゴリズム, システムクラッシュ。
- 置換先の例: 神託, 呪い, 神の理, 祟り, 還流, 付喪神化。

### 1.1 語彙変換辞書（移行作業の審査基準）

| 禁止語彙 | 推奨語彙 | 備考 |
| --- | --- | --- |
| AI | 神託 / 神意 | 自律判断は「神意の執行」として記述 |
| ナノマシン | 呪い / 祟りの粒 | 微細干渉は呪術作用で表現 |
| データ | 神話記録 / 祭具記録 / 神の理 | 数理情報は「記録」「理」へ置換 |
| アルゴリズム | 儀式手順 / 理の段取り | 手続きは儀式・作法で表現 |
| クラッシュ | 破綻 / 崩落 / 断絶 | 異常停止は神話語彙へ転換 |
| ノイズ（機械文脈） | 情念の奔流 / 乱れ | 文脈に応じて使い分け |
| メタル系（直輸入） | 剥落の星屑 | 外部参照語彙は翻訳して導入 |

### 1.2 SF・メタ用語の資料内使用規則（読者・開発陣向けの例外）

ゲーム内表現の厳格さを保ちつつ、開発ドキュメント内での**実務的な説明効率を確保する**ため、以下の原則を定める：

**許容される場面（ドキュメント内）:**
- 仕様書・データ定義：UI、バグ、リサーチ、ティック、クラッシュ、サーチ、リブート等を使用可。
- 理由：技術的正確性の確保、開発陣間での意思疎通の加速。
- 記述例：「UIの崩壊を回避する」「バグ攪乱ゲージ」「行動Tickの遅延」など。

**厳禁される場面（ゲーム内テキスト）:**
- プレイヤーが目にするテキスト一切：セリフ、アイテム説明、システムメッセージ、実績テキスト等。
- 必ず和語へ翻訳して実装する。
- 翻訳例：UI崩壊 → 「神託崩壊」、バグ攪乱 → 「情念の奔流」、リブート → 「世界再起動」など。

**管理方法:**
本セクションで定めた**禁止語彙と推奨語彙の対応表** を実装ガイドとして参照し、コード・テキストの自動検査を推奨する。

## 2. 変更提案の標準手順

1. 変更対象のUIDを明示する。
2. 影響範囲の一次分析を行う。
3. `depends_on` と `influences` を相互更新する。
4. 本文変更を適用する。
5. 参照先ファイルの整合性差分を反映する。

## 3. 影響範囲分析テンプレート

```text
【影響範囲分析と構造提案 (Impact & Architecture Analysis)】
- 変更・追加対象: [ファイル名 / UID]
- 推奨される配置パス: [path]
- 波及するファイル:
  - [file A]: [change reason]
  - [file B]: [change reason]
- 整合性リスク: [risk]
```

## 4. 正本の優先順

- 第1正本: `03_Systems/SYS-30_Data_and_Logic_Architecture.md`
- 第2正本: `03_Systems/SYS-20_Game_Systems_and_Flow.md`
- 第3正本: `01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md`
- 物語・演出・参照資料は上記を破らない範囲で更新する。

## 5. 移行フェーズ開始条件

- `RPG企画4`を参照専用として扱う。
- 変更は必ず`RPG企画5`へ実施し、必要に応じて`WRD-99`へ履歴を追記する。
