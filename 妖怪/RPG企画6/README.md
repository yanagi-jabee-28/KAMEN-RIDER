# アシブネノミコト 〜天降る御子と、星屑の大地〜 ドキュメント入口

この企画は「泥臭い修復と継承」を体感する、和風神話ダークファンタジーRPGです。
あなたの役割に合わせて、次の導線から読み始めてください。

## 物語とビジュアルをつくる方へ（シナリオ・アート・全体把握）

最初に世界観へ没入し、次に物語と見た目の設計へ進む導線です。
読了後に、キャラクターの感情線とアート方向性を同じ言葉で共有できます。

1. **[00_Welcome_and_Introduction/README.md](00_Welcome_and_Introduction/README.md)**: 企画の根幹テーマと世界観
2. **[00_Welcome_and_Introduction/WRD-02_Protected_Vocabulary.md](00_Welcome_and_Introduction/WRD-02_Protected_Vocabulary.md)**: 保護語彙の共通ハブ（概念/体験/機能）
3. **[01_Story_and_Characters/NAR-10_Narrative_and_Characters.md](01_Story_and_Characters/NAR-10_Narrative_and_Characters.md)**: 人物・5幕構成・演出意図
4. **[03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md](03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md)**: 美術方針・キャラクター/環境指針

## 遊びの仕組みを設計する方へ（ゲームデザイン・レベル設計）

プレイヤーがどう戦い、どう成長し、どう詰まりを突破するかを把握する導線です。
読了後に、体験設計とデータ設計を往復しながら調整できます。

1. **[00_Welcome_and_Introduction/WRD-02_Protected_Vocabulary.md](00_Welcome_and_Introduction/WRD-02_Protected_Vocabulary.md)**: 語彙の基準合わせ
2. **[02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md](02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md)**: 遊び方・体験設計・戦闘の流れ
3. **[02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix.md](02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix.md)**: 術式・ロール索引
4. **[02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md](02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md)**: データカタログ（一般向け）

補足: 現行仕様では、代受苦は「防御型/攻撃型」に公式分離されています。極大代受苦は全員に行使権がありますが、武器履歴と同調条件を満たした場合のみ発動します。
補足2: 行動順は `Tick` ベースの待機値で進行します。読み方の入口は `SYS-20` の最短ガイドと `SYS-22` の運用節を参照してください。

## 実装と運用を担当する方へ（プログラミング・データ設計）

内部仕様、参照マッピング、制作プロトコルを扱う導線です。
読了後に、公開文書の記述から実装IDと条件式を逆引きできます。

1. **[90_For_Developers/ARC-00_Architecture_and_Governance.md](90_For_Developers/ARC-00_Architecture_and_Governance.md)**: 規約・文書管理
2. **[90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md](90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md)**: 数式・フラグ・実装仕様
3. **[90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md](90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md)**: 体験記述と実装の対応表
4. **[90_For_Developers/DEV-12_Art_Production_and_Prompt_Protocol.md](90_For_Developers/DEV-12_Art_Production_and_Prompt_Protocol.md)**: アート制作プロトコル
5. **[90_For_Developers/DEV-13_Document_Metadata_and_Reading_Order.md](90_For_Developers/DEV-13_Document_Metadata_and_Reading_Order.md)**: メタデータ運用と読解順

## 参考資料と履歴を確認したい方へ

外部参照、統合履歴、辞書情報を確認する導線です。
読了後に、過去案との差分と現在方針の根拠を追跡できます。

- **[99_Archive_and_References/REF-00_References_and_Archive.md](99_Archive_and_References/REF-00_References_and_Archive.md)**
- **[99_Archive_and_References/REF-50_External_RPG_Reference_Dictionary.md](99_Archive_and_References/REF-50_External_RPG_Reference_Dictionary.md)**
