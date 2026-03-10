# RPG企画5 - 40 Art Direction and Assets (アートと演出)

本ドキュメントは視覚・質感・演出の原則を定義する。状態判定や数値は記述せず、30のSSOT参照を徹底する。

## 1. 同一キャンバス原則 [#ID:R5_Art_Single_Canvas]
世界は和紙を基底に、岩絵具と墨の層で描く。神と人の差は素材差ではなく、筆致差で表現する。

- 神側: 凍結した輪郭、細線、低滲み。
- 人側: 掠れ、滲み、剥落、修復痕。

## 2. 核心モチーフ [#ID:R5_Art_Motifs]
- 泥と星屑
- 金継ぎの脈
- 乾いた赤から戻らない退色

## 3. 状態演出マッピング [#ID:R5_State_Visual_Map]
- 死狂い: 輪郭割れ、残像、金継ぎ光の逆流。
- 空殻: 彩度低下、筆致停止、白い粉塵。
- 過熱・沈黙: 焼け筋、煤、微細なひび。

※判定条件は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Boundary_States] と [#ID:R5_Resonance_Burst] を参照。

## 4. 場ルール演出 [#ID:R5_Field_Art]
- 無菌の帳: 音の減衰、粒子静止、照度平坦化。
- 血の泥沼: 粒子密度増、滲み拡散、暗部の粘性。

※内部フラグは `30_Data_and_Logic_Architecture.md` の [#ID:R5_Field_Rules] を参照。

## 5. UI視覚ノイズ規則 [#ID:R5_UI_Noise]
ノイズは装飾ではなく意味を持つ。予測が外れた瞬間、ノイズがわずかに増幅し「理の破綻」を示す。

※共鳴過熱連動は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Resonance_Burst] を参照。

## 6. 禁止表現
- SF的インターフェース（無機HUD、機械診断表示）を使わない。
- 直輸入語をロゴやアイコン名へ使わない。

※禁止語監査は `30_Data_and_Logic_Architecture.md` の [#ID:R5_Forbidden_Terms_Guard] を参照。