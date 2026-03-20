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

> ※このファイルは一般読者向けのデータカタログ版です。式・疑似コード・フラグ対応は [../90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md](../90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md) を参照してください。

## 1. コア要素（概要）

### 1.1 三条の熱源
- 活魂: 生存に直結する器。
- 情念: 技運用と同調の燃料。
- 武器耐久度: 攻勢維持と代受苦の前提になる摩耗資源。

### 1.2 戦闘体験の柱
- 代受苦と極大代受苦で「守るために壊す」判断を迫る。
- 付喪神化と継承で、喪失を次の強さへ接続する。
- 位相ギミックと学習神AIで、同じ戦法の反復を許さない。

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

実際の相性計算式は開発者向け資料（DEV-10）を参照。

### 2.4 Weapon_Evolution_Master
| Character_ID | Weapon_Category | Stage_1_初期 | Stage_2_中盤 | Stage_3_終盤 | Narrative_Class | 解禁条件 | 備考 |
|---|---|---|---|---|---|---|---|
| `MIKOTO` | 刃 | 海揚がりの古錆刀 | 星喰みの黒太刀 | 天叢雲剣 | `INITIAL/MYTHIC` | `OROCHI_TAIL_BREACHED` 後に金継ぎ接合 | 尾破断の剣核を現行武器へ接合して覚醒 |
| `MIKOTO` | 槍・鉾 | 欠けた祭祀槍 | 隕鉄の剛鉾 | 天之沼矛 | `INITIAL/MYTHIC` | 第4幕後半の神器鍛造段階 | 領域圧を物理的にかき混ぜる反逆系統 |
| `UKAMI` | 槍・鉾 | 獣骨の石鉾 | 大蛇狩りの剛槍 | 国津神の荒鉾 | `INITIAL/MYTHIC` | `UKAMI_RETURNED_YOMOTSU` | 黄泉・常世限定の自律介入と連動 |
| `SUKUNA` | 打撃 | 欠けた石杵 | 毒喰みの乳棒 | 少名の神杵 | `INITIAL/MYTHIC` | 第2幕中盤以降 | 状態異常と化学干渉を主軸化 |
| `MAHITO` | 打撃 | 煤まみれの大槌 | 刃折りの業槌 | 天目の神火槌 | `INITIAL/MYTHIC` | `MAHITO_JOINED_ACT2` 以降の段階鍛造 | 武器摩耗制御と禁忌鍛造の中核 |
| `UZU` | 扇 | 破れた舞扇 | 緋色の鉄扇 | 天鈿女の狂扇 | `INITIAL/MYTHIC` | 第2幕前半加入後 | Tick攪乱と狂騒ノイズを拡張 |
| `TACHIBANA` | 槍・鉾 | 怨念の流木 | 血塗られた銛 | 弟橘の海人銛 | `INITIAL/MYTHIC` | 第2幕中盤加入後 | 自傷を広域デバフへ変換 |
| `WAKAHIKO` | 遠距離 | 白木の上弓 | 泥塗れの猟弓 | 天若の返し弓 | `INITIAL/MYTHIC` | `WAKAHIKO_JOINED_ACT3` | 返し矢と因果転写を主導 |

### 2.5 Character_Equipment_Master
| Character_ID | 主腕（利用可カテゴリ） | 固有武器 | 装束 | 形代 | 制約/備考 |
|---|---|---|---|---|---|
| `MIKOTO` | 刀・槍 | 大幣（仮想双腕特例） | 星祝の防具 | 泥濘の勾玉 | `DualStanceActive` は継承手甲恒久化後に有効 |
| `UKAMI` | 刀・槍・杖 | 錫杖 | 行者の法衣 | 風雷の獣牙 | 地上では参戦不可。黄泉・常世でのみ自律介入 |
| `SUKUNA` | 打撃 | 乳棒 | 薬草師の衣 | 忘却の香炉 | 劇薬系の状態異常運用を優先 |
| `UZU` | 扇・刃・大幣 | 鉄扇・隠し短刀 | 狂乱の舞衣 | トランスの神楽鈴 | 攪乱役。命中撹乱/行動順破壊に特化 |
| `TACHIBANA` | 槍・打撃・大幣 | 流木槍・打ち櫂 | 濡れ羽の衣 | 泥水の呪符 | 活魂消費とデバフ拡散の両立 |
| `MAHITO` | 打撃 | 大槌・やっとこ | 鍛冶師の重装皮衣 | 炉心の火打石 | 金継ぎ・付喪神化・神話鍛造の解禁キー |
| `WAKAHIKO` | 弓・短刀 | 天上弓・仕込み短刀 | 境界の隠秘服 | 影縫いの鏑矢 | 返し矢運用時は反動管理が必須 |

### 2.6 Enemy_Master
| Enemy_ID | 名称 | タイプ | 特殊仕様 | 撃破/進行フラグ |
|---|---|---|---|---|
| `Amaterasu_Core_OS` | 天照大御神 | システム体 | 戦闘対象ではなく凍結管理 | `AMENO_IWATOWAKE_REBOOT` |
| `Tsukuyomi_AntiVirus` | 月読命 | 偽終幕ボス | 撃破後に絶対暗黒と塔自由落下へ遷移 | `TSUKUYOMI_FAKE_LASBOSS` |
| `Kagaseo_Star_God` | カガセオ | 第4幕ボス | 帰還引力と拒絶理の衝突で特殊減衰 | `KAGASEO_REBOOT_DRIVE_ACQUIRED` |
| `Boss_Yakusa_no_Ikazuchi` | 八雷神 | クリア後ボス | 行者還し専用3フェーズ | `GYOJAGAESHI_CLEARED` |
| `Boss_Susanoo` | スサノオ | 試練ボス | 高密度連撃の監督者 | `SUSANOO_TRIAL_CLEARED` |
| `Boss_Yamata_no_Ubusuna` | 澱神・八岐の産土 | 真裏ボス | 尾破断で剣核露出 | `OROCHI_TAIL_BREACHED` |

### 2.7 Enemy_Tier_Template_Master（完全版）
| Tier | Template_ID | 名称 | 系統 | 主属性/副属性 | 耐性傾向 | 弱点傾向 | 主干渉 | 状態異常依存 |
|---|---|---|---|---|---|---|---|---|
| `T1` | `MIRE_BUBBLE_SLIME` | 泥泡の這い | 荒魂獣 | 水/闇 | 斬撃軽減 | 風、雷 | 群体で押し切る連撃圧 | なし |
| `T1` | `NUMBING_JELLY` | 痺れ海月 | 荒魂獣 | 水/氷 | 水軽減 | 雷、炎 | 触手で行動阻害 | あり（`PARALYSIS`） |
| `T1` | `TAR_CROW` | 黒泥鴉 | 荒魂獣 | 風/闇 | 風軽減 | 雷、光 | 高回避で後衛へ刺突 | なし |
| `T1` | `MUD_VIPER` | 泥縞の蛇 | 荒魂獣 | 土/闇 | 土軽減 | 炎、光 | 毒牙で継続削り | あり（`POISON`） |
| `T1` | `WILD_MIRE_TOAD` | 泥塗れの蝦蟇 | 荒魂獣 | 水/土 | 打撃軽減 | 雷、風 | 毒噴霧による継続圧 | あり（`POISON`） |
| `T1` | `ASHEN_STRAY_DOG` | 灰野犬 | 荒魂獣 | 土/風 | 土軽減 | 氷、水 | 先制噛み付きでTick撹乱 | なし |
| `T1` | `STATIC_DUST` | 静止の塵 | 棄物 | 氷/光 | 斬撃軽減 | 炎 | 接触麻痺で行動阻害（`Trauma_Resentment`） | あり（`PARALYSIS`） |
| `T1` | `PRAYER_SCRAP_DOLL` | 祈布の切れ端人形 | 棄物 | 光/闇 | 光軽減 | 炎、雷 | 低威力連打で耐久摩耗を蓄積 | なし |
| `T1` | `WHITE_MOTH` | 白の迷い蛾 | 白化神末端 | 光/風 | 光軽減 | 闇、炎 | 鱗粉で命中計算を撹乱 | あり（`BLIND`） |
| `T1` | `RUSTED_BLADE_RELIC` | 錆びた刃具 | 棄物 | 土/闇 | 物理軽減 | 炎、雷 | 痛恨寄り単発重撃 | なし |
| `T1` | `HOLLOW_SHELL_CRAB` | 虚殻蟹 | 棄物 | 水/土 | 打撃強耐性 | 雷、風 | 殻閉じ防御で時間稼ぎ | なし |
| `T1` | `WHITE_INITIATE` | 白の初誓徒 | 狂信者 | 光/土 | 光軽減 | 闇、打撃 | 低位浄化で味方補助 | あり（`SKILL_SEAL`） |
| `T2` | `CHALK_SENTINEL` | 白堊の防人 | 擬神兵 | 光/氷 | 物理強耐性 | 打撃、雷 | 見切りで耐久だけを削る | なし |
| `T2` | `SANCTIFIED_BOWMAN` | 白戒の弓徒 | 狂信者 | 光/風 | 光軽減 | 闇、雷 | 後衛狙撃と封印支援 | あり（`SKILL_SEAL`） |
| `T2` | `MOURNING_WAIL` | 未練の泣き女 | 澱神 | 闇/水 | 闇軽減 | 光 | 広域の睡眠誘発 | あり（`SLEEP`） |
| `T2` | `GRUDGE_SWARM` | 怨群の羽虫 | 澱神 | 闇/風 | 闇軽減 | 光、炎 | 群れで混乱率を増幅 | あり（`CONFUSION`） |
| `T2` | `WHITE_CHAPLAIN` | 白の教誨師 | 狂信者 | 光/土 | 光軽減 | 闇、打撃 | 味方回復と封印支援 | あり（`SKILL_SEAL`） |
| `T2` | `FORGE_CINDER` | 過熱する鉄滓 | 棄物 | 炎/土 | 炎吸収 | 氷 | 自爆予告で防御択を強要（`Trauma_Resentment`） | なし |
| `T2` | `ABANDONED_GUNNERY` | 遺棄火筒 | 棄物 | 炎/土 | 炎軽減 | 水、雷 | 充填後の直線砲撃 | なし |
| `T2` | `SALT_MIRE_BANDIT` | 塩泥の賊徒 | 非神 | 水/闇 | 水軽減 | 雷、光 | 耐久摩耗付き多段攻撃 | なし |
| `T2` | `CAVE_ECHO_STALKER` | 洞哭の追い手 | 非神 | 闇/風 | 闇軽減 | 光、土 | 影縫いで行動遅延 | あり（`BLIND`） |
| `T2` | `RITUAL_BELL_WISP` | 祭鈴の残響 | 棄物 | 光/氷 | 光軽減 | 炎、闇 | 鈴音で短期封印を散布 | あり（`SKILL_SEAL`） |
| `T2` | `FIELD_SCOURER_BOAR` | 荒野牙猪 | 荒魂獣 | 土/雷 | 土軽減 | 氷、水 | 直進突撃で前衛崩し | なし |
| `T3` | `MIRROR_GUARDIAN` | 鏡面の守護像 | 白化神上位 | 光/氷 | 全属性半減傾向 | 無属性、極大代受苦 | 2回行動と限定反射 | なし |
| `T3` | `HISTORY_DROWNER` | 記録喰らいの禊神 | 非神 | 水/光 | 水軽減 | 雷、闇 | 武器履歴の一時消去 | あり（`HISTORY_ERASE`） |
| `T3` | `KUSANAGI_WRAITH` | 草薙の亡霊 | 非神 | 風/炎 | 風軽減 | 水、土 | 耐久吸収で自己再生 | あり（`KUSANAGI_WEAR`） |
| `T4` | `SAGUME_EXECUTOR` | 探女の執行体 | 天津神 | 光/水 | 光軽減 | 闇 | 予測線の乖離誘発 | あり（`WHITE_OATH`） |
| `T4` | `TOYOTAMA_SURGE` | 豊玉姫の潮影 | 澱神上位 | 水/闇 | 水軽減 | 雷、光 | 情念依存技への逆算妨害 | あり（`TRUTH_OBSCURE`） |
| `T4` | `UKA_SUPPLY_CORE` | 宇迦之御魂の配給核 | 天津神支援 | 土/光 | 土軽減 | 闇、炎 | 回復と情念枯渇の二択圧 | あり（`PURE_PROVISION`） |

### 2.8 Attribute_Master（戦術的意味）
| Attribute_ID | 名称 | 戦術的意味 |
|---|---|---|
| `FIRE` | 炎 | 過熱を加速し、停滞に穴を開ける |
| `WATER` | 水 | 流動と浸食。回復・侵食の両義性 |
| `WIND` | 風 | 行動順と位置取りを崩す |
| `EARTH` | 土 | 受け止め、押し返す。重圧制御 |
| `LIGHT` | 光 | 予測と露呈。神側の制御に近い |
| `DARK` | 闇 | 隠匿と反転。予測線の外側を作る |
| `ICE_STAGNATION` | 神の氷 | 静止と凍結へ寄せる |
| `ICE_COOLING` | 人の氷 | 過熱の鎮静と散逸制御 |

### 2.9 星土の脈継ぎ（神社連動）
祈りだけでも泥だけでも足りず、両方の履歴が神器を成立させる設計。

## 3. 進行イベント（概要）

シナリオ進行の内部フラグIDと発火条件は DEV-10 へ移管しました。

- 主な節目: うかみ離脱、偽終幕、行者還し、試練解禁、尾破断、天叢雲剣覚醒。
- 詳細な順序対応は [../90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md](../90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md) を参照。

## 4. UI/UX制御ロジック（UI Logic）

| UI_ID | 表示対象 | 表示方針 |
|---|---|---|
| `UI_KAKKON_GAUGE` | 活魂 | 警告色、死狂い時の特殊表示 |
| `UI_JONETSU_GAUGE` | 情念 | 空殻遷移時の警告 |
| `UI_DURABILITY_METER` | 武器耐久 | 段階的劣化、代受苦推奨表示 |
| `UI_PREDICTION_LINE` | 予測線 | 乖離型・ノイズ型の歪み表示 |

## 5. 開発者向け移管資料

- 数式・疑似コード・フラグ: [../90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md](../90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md)
- 参照マッピング: [../90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md](../90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md)
