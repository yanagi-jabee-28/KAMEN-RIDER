# RPG企画5 - 10 Narrative and Characters (物語と人物)

本ドキュメントは物語層の定義書であり、数値や内部変数は記述しない。実装詳細は `30_Data_and_Logic_Architecture.md` を参照する。

## 1. 物語コンセプト [#ID:R5_Narrative_Concept]
主人公ミコトは、結晶化された秩序へ従う器として地上へ降ろされたが、旅路で出会う破損した器と喪失の連鎖によって、自ら「還流する側」へ立つ決断を強いられる。

※三条熱源の挙動詳細は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Resource_Core] を参照。

## 2. 時系列（五幕） [#ID:R5_Act_Timeline]
1. **胎（きざし）**: 器としての出自と、最初の綻び。
2. **融（とろけ）**: 白化の秩序へ抗い、仲間の傷が連鎖する。
3. **熾（たぎり）**: 情念の過熱が顕在化し、代受苦の意味が反転する。
4. **結（むすび）**: 付喪神化と継承で、喪失を次代へ結ぶ。
5. **還（めぐり）**: 永遠の停止を拒み、壊れながら循環する終幕。

※幕進行フラグは `30_Data_and_Logic_Architecture.md` の [#ID:R5_Story_Flag_Master] を参照。

## 3. キャラクター弧（要約） [#ID:R5_Character_Arcs]
- **ミコト**: 完璧な器から、欠けを引き受ける人間へ。
- **マヒト**: 鍛える者から、継ぐ者へ。禁忌鍛造の責任を背負う。
- **うかみ**: 救済者から、距離と限界を受け入れる守護者へ。
- **スクナ**: 機転と逸脱で、理の穴を穿つ触媒。

※鍛造解放条件は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Maintenance_Tiers] を参照。

## 4. トラウマ設計と回復不可逆性 [#ID:R5_Trauma_Design]
本作の回復は「元に戻す」ではなく、「傷を抱えたまま進行する」設計を徹底する。キャラクターの痛みは消去されず、戦闘と会話の文脈で再解釈される。

※境界状態の条件は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Boundary_States] を参照。

## 5. 世界環境 [#ID:R5_World_Environment]
- 白化領域: 音・色・温度が均質化した秩序領域。
- 泥濁領域: 粒子・湿度・残滓が蓄積する還流領域。

※場ルールの内部処理は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Field_Rules] を参照。

## 6. 禁止表現の運用
- DQ固有記号や語彙を、物語地の文へ直書きしない。
- SF語で痛みや世界の異常を説明しない。

※監査規則は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Forbidden_Terms_Guard] を参照。