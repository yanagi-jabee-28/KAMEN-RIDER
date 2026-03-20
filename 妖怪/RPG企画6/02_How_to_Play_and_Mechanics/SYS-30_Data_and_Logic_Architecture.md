---
uid: [SYS-30]
project_code: RPG企画6
title: Data and Logic Architecture
role: data-and-logic
status: active
owner: Architecture Guardian
depends_on:
  - SYS-20_Player_Manual.md
  - ../00_Welcome_and_Introduction/README.md
  - ../90_For_Developers/ARC-00_Architecture_and_Governance.md
influences:
  - ../01_Story_and_Characters/NAR-10_Narrative_and_Characters.md
  - ../03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md
  - ../99_Archive_and_References/REF-00_References_and_Archive.md
---

# [SYS-30] Data and Logic Architecture

> ※このファイルはゲーム内部の計算式・フラグ・マスターデータを記載する開発者向け正本です。遊び方を知りたい読者は [SYS-20_Player_Manual.md](SYS-20_Player_Manual.md) を参照してください。

## 1. コア数理モデル（Logic Architecture）

### 1.1 三条の熱源（実装定義）
- `Kakkon_Value`: 活魂（器）。キャラクターの基礎HP。
- `Jonetsu_Value`: 情念（熱）。スキル使用・同調の燃料。
- `Weapon_Durability`: 武器耐久度（摩耗）。0で破損状態へ遷移。

### 1.2 境界状態判定（State Transition）
```text
IF Kakkon_Value <= 0 AND Jonetsu_Value > 0 AND Has_Shigurui_Passive == TRUE THEN
  State_Shigurui = TRUE
END IF

IF Kakkon_Value > 0 AND Jonetsu_Value <= 0 THEN
  State_Karakara = TRUE
END IF

IF (Kakkon_Value <= 0 AND (Jonetsu_Value <= 0 OR Has_Shigurui_Passive == FALSE))
 OR (Kakkon_Value <= 0 AND Anchor_Equipped_Count == 0) THEN
  State_Dead = TRUE
END IF
```

### 1.3 武器耐久度モデル（Durability Calculation）
```text
Durability_new = max(0, Durability_old - (
    Base_Weapon_DurabilityCost * Stance_Multiplier
  + Combo_DurabilityCost
  + Skill_DurabilityCost
  + Intentional_Cost
))
```
- `Stance_Multiplier`:
  - 両手持ち (2H): `1.5`
  - 一刀流 (1H): `1.0`
  - 二刀流 (Dual): `1.3`

## 2. 実装マスターデータ（Master Tables）

### 2.1 Character_Base_Master
| Char_ID | 名称 | ロール | 基礎活魂 | 基礎情念 | 武器適正 |
|---|---|---|---|---|---|
| `MIKOTO` | ミコト | 万能/写し | 100 | 120 | 斬・刺・打 |
| `UKAMI` | うかみ | 壁/剛 | 200 | 80 | 打・突 |
| `SUKUNA` | スクナ | 毒/剥離 | 80 | 150 | 投・打 |
| `UZU` | ウズ | 攪乱/舞 | 90 | 110 | 扇・短 |
| `TACHIBANA` | タチバナ | 呪/自傷 | 110 | 100 | 杖・櫂 |
| `MAHITO` | マヒト | 鍛/砕 | 150 | 90 | 槌・鉗 |
| `WAKAHIKO` | ワカヒコ | 弓/停 | 95 | 130 | 弓・短 |

### 2.2 Status_Effect_Master（状態異常定義）
| Effect_ID | 名称 | 説明 | 関連 |
|---|---|---|---|
| `POISON` | 毒 | 毎Tick活魂減少 | スクナ、タチバナ |
| `CONFUSION` | 混乱 | ランダム行動/不発。UI予測線の絡まり | ウズ、澱神 |
| `CHARM` | 服従 | 味方攻撃。敵UIの駒化 | 天津神、澱神 |
| `BLIND` | 幻惑 | 命中率低下。着弾点座標の「泥」 | ウズ、ワカヒコ |
| `CRYSTALLIZE` | 琥珀化 | ダメージ・行動不能「永遠の保管」 | 天津神 |
| `WHITE_OATH` | 白の宣託 | 予測UI乖離。プレイヤー確率判断の崩壊 | 探女、白化神 |
| `TRUTH_OBSCURE` | 真実の隠匿 | バフ/付喪神段階の初期化巻き戻し | 豊玉姫、澱神 |
| `PURE_PROVISION` | 無垢なる配給 | 回復と引き換えに情念を枯渇固定 | 宇迦之御魂神 |
| `REGEN_BLOCK` | 再生停止 | 回復無効化 | 大宜都比売 |
| `SHIGURUI_ANCESTOR` | 死狂いの祖 | 連撃+予測攪乱 | 素戔嗚尊（試練） |
| `HISTORY_ERASE` | 歴史の抹消 | 金継ぎ履歴の一時消失 | 瀬織津姫 |
| `KUSANAGI_WEAR` | 草薙の摩耗 | 武器耐久の吸収・防御配分 | 日本武尊 |
| `YOMOTSU_CURSE` | 黄泉の呪い | 黄泉アイテム使用時の永続デバフ | 共有システム |

### 2.3 氷属性サブタイプ（静止/冷却）
属性は相性計算レイヤーであり、術式駆動リソースとは分離して扱う。

| IceSubtype_ID | 名称 | 意味 |
|---|---|---|
| `ICE_STAGNATION` | 神の氷（静止） | 時間・行動を凍結し、琥珀化へ寄せる |
| `ICE_COOLING` | 人の氷（冷却） | 暴走熱を奪って鎮める。過熱抑制、熱散逸 |

```text
IF Attack.IceSubtype == ICE_COOLING AND Target.Tag == AMATSUKAMI THEN
  Damage = floor(Damage * 0.85)
  Skip_State_Inflict(Freeze_Stun)
END IF

IF Attack.IceSubtype == ICE_COOLING AND (Target.Tag == DEIGAMI OR Target.Tag == KIBUTSU) THEN
  Apply_State(Defense_Down, Duration=2)
  Damage = floor(Damage * 1.1)
END IF
```

## 3. シナリオ進行・システムフラグ（System Flags）

### 3.1 Story_Flag_Master
| フラグ名 | 発火タイミング |
|---|---|
| `UKAMI_JOINED_EARLY` | うかみ合流 |
| `MAHITO_JOINED_ACT2` | マヒト加入（第2幕固定進行） |
| `KAGUTSUCHI_QUELLED` | 灼熱たたら場・鎮魂完了 |
| `WHITE_CORRIDOR_CLEARED` | 白堊の回廊突破 |
| `MAHITO_FIELD_LV2_UNLOCKED` | マヒト「野鍛冶の誓い」達成 |
| `SHRINE_FORGE_LV3_UNLOCKED` | 神社鍛造拡張 |
| `UKAMI_LEFT_KATSURAGI` | 葛城山での一次離脱、ミコトへのスキル継承 |
| `WAKAHIKO_JOINED_ACT3` | 返し矢降臨イベント後加入 |
| `TSUKUYOMI_FAKE_LASBOSS` | ツクヨミ撃破・偽終幕 |
| `UKAMI_RETURNED_YOMOTSU` | 行者うかみ帰還 |
| `AMENO_IWATOWAKE_REBOOT` | 天岩戸強制再起動 |
| `ETERNITY_REJECTED` | エンディング |
| `SUSANOO_TRIAL_CLEARED` | 根の国スサノオ撃破 |
| `AMENO_MURAKUMO_AWAKENED` | 天叢雲剣覚醒 |

### 3.2 継承の固定習得（Forced Inheritance）
```yaml
TriggerFlag: UKAMI_LEFT_KATSURAGI
TargetCharacter: MIKOTO
ForcedSkills:
  - SkillId: INHERITED_SARUTA_BREAK
    Name: 猿田の破岩撃 (剛)
  - SkillId: INHERITED_HORAGAI_ROAR
    Name: 法螺の轟き (導)
```

## 4. UI/UX制御ロジック（UI Logic）

| UI_ID | 表示対象 | 表示方針 |
|---|---|---|
| `UI_KAKKON_GAUGE` | 活魂 | 警告色、死狂い時の特殊表示 |
| `UI_JONETSU_GAUGE` | 情念 | 空殻遷移時の警告 |
| `UI_DURABILITY_METER` | 武器耐久 | 段階的劣化、代受苦推奨表示 |
| `UI_PREDICTION_LINE` | 予測線 | 乖離型・ノイズ型の歪み表示 |

## 5. 運用ルール（Maintenance Rules）

1.  **DRY原則**: スキル説明文側に直接数値を書かず、本マスターを参照すること。
2.  **SSOT**: 実装値、計算式、フラグの正本は常に本ファイルとする。
3.  **整合性**: 各幕の進行フラグ変更時は、必ず `Scenario_Capability_Master` も確認する。

---
**Single Source of Truth**: 上記パラメータの実数値はすべて本ファイルのみで管理する。画面表示・物語表現・UX演出での独自変更を禁止する。
