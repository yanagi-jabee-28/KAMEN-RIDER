# 40 Art Direction and Assets (アートと演出)

本ドキュメントはArtist/AIプロンプター向けの「画風憲法」と「プロンプト集（LUMINOUS WASHI V3）」を一体化した正本である。`30_Data_and_Logic_Architecture.md` の `Visual_Prompt_Master` が参照するすべての美術基準と生成テンプレートがここに集約される。

---

## 1. ビジュアル・フィロソフィー（同一キャンバス原則）

本作のアートワークは「完璧な理への、不完全な熱量による抵抗」を最も直感的に伝えるための言語である。

### 大前提：同一キャンバス原則
- 神も、人も、世界も、すべて**「一枚の生きた和紙（Washi）」**の上に**「岩絵具（Iwa-enogu）」**という同じ画材で描かれる。
- 素材の断絶（神だけ3D・異質テクスチャ）は採用しない。両者の違いは**「筆致のあり方」**のみで表現する。

### 二項対立の視覚表現

| 属性 | 筆致 | 色彩 | 印象 |
|---|---|---|---|
| **人（縄文的・熱量）** | 和紙繊維への奔放な滲み・掠れ・岩絵具の粒子感を積極的に許容 | 泥・鉄錆・枯葉・血のアースカラー（暖色低彩度） | 粗野だが温かい、アナログな生命感 |
| **神（弥生的・静謐）** | 同じ和紙上で滲みを極限まで抑えた、迷いのない端正な細線。幾何学的構図 | 胡粉の白・鈍い金箔・群青・朱（格調高い伝統色） | 冷たく美しい、絶対的な秩序と静寂 |
| **金継ぎ（境界）** | **鋭く盛り上がって光る黄金（金漆・箔）**が、両者の境界にのみ介入する | 黄金 | カガセオの熱量が地上にもたらした唯一の光 |

### 絶対禁止事項（全アセット共通）
- **西洋ファンタジー意匠:** プレートアーマー・西洋剣・マント → 貫頭衣・麻布・縄・骨・石に純化
- **アニメ的記号性:** 均一な線・滑らかな肌 → 和紙質感・絵の具の滲み・筆の勢い
- **ホラー描写:** 不気味さは生命の温かみを損なわない範囲に留める。造形美は常に担保する
- **SF・近代意匠:** 武器・UIエフェクト・ダンジョン等すべてで神話ファンタジー基調を維持

---

## 2. スタイルアンカー（All Assetsに適用する共通プロンプト）

```text
# 00_STYLE_ANCHOR_LUMINOUS_WASHI_V6

Prompt:
masterpiece, highest quality, highly detailed, anatomically correct, perfect human proportions, natural and expressive posing, perfectly drawn hands and fingers, exquisitely beautiful character faces, entirely focused composition, STRICTLY NO extra items, NO random props,
entirely painted on highly textured, fibrous Washi paper using traditional Japanese mineral pigments (Iwa-enogu) and soft ink washes. visible paper fibers, powdery mineral granulation, organic analog warmth.
The visual core is a breathtaking artistic harmony: ultra-refined, disciplined fine lines for divine elements, intersecting with ROUGH, SCRATCHY dry-brush strokes and mineral granulation for human elements. Absolutely no smooth, synthetic, or 3D surfaces.
supernatural or magical elements are rendered strictly through traditional analog mediums, sumi-e strokes, kintsugi lacquer, or pigment splashes.

Negative Prompt:
extra weapons, multiple weapons, extra swords, dual wielding, unrequested items, random clutter, background clutter, extra props, bad anatomy, bad proportions, gross proportions, deformed, disconnected limbs, extra limbs, missing arms, missing legs, mutated hands, poorly drawn hands, extra fingers, floating objects, disconnected objects, surreal AI artifacts, 3D render, CGI, glossy surface, plastic, ceramic, porcelain, metallic sheen, flat cel-shading, oil painting, thick impasto, modern digital VFX, western fantasy medieval armor, sci-fi, photorealistic, photography, ugly, deformed, noisy, jpeg artifacts, blurry, low resolution, poorly drawn, signature, watermark
```

---

## 3. キャラクタービジュアル定義

### 運用制約（全キャラ共通）
- **古代コンセプト固定:** 近代衣装・西洋甲冑・SF意匠は採用しない。
- **造形美と華の担保:** 泥臭い世界観であっても、顔立ちと骨格は「万人受けする圧倒的な美しさ」を大前提とする。
- **同一媒体内コントラスト厳守:** 人間側は奔放な滲みと土色。神（敵・UI）側は制御された筆致と格調色を徹底。
- **共通の血アクセント:** タチバナとワカヒコには「血の赤」を共通アクセントとして入れ、ピアサポートの共鳴を視覚的に示唆する。

---

### ミコト（主人公 / 空の器）
**コンセプト:** 性別を超えた「人間そのもの」。白と赤（スカーフのみ）、アシンメトリーな防具。

> **スカーフ厳守ルール:** 赤いスカーフはただひとつの連続した布。前端はしまい込まれ、後ろに**1本のみ**尾を引く。分岐・二股・複数の尾は絶対禁止。白いボブヘアと赤いスカーフが**必ず同じ方向**になびく（Synchronized Wind Logic）。

```text
Prompt:
masterpiece, highest quality, exquisitely beautiful adventurer with a perfect balance of masculine and feminine Japanese (East Asian) youth features, standing on a windy cliff. The face is a masterwork of neutral Japanese androgyny — a strikingly handsome and beautiful profile; sharp yet balanced bone structure, straight noble nose, resolute gaze with straighter brows.
style: painted on highly absorbent, fibrous Washi paper, traditional Japanese watercolor (Iwa-enogu), emphasizing beautiful unpredictable chromatic bleeding and natural ink washes.
details: pure white short bob hair painted with soft, translucent watercolor washes. Off-white sleeveless tunic (Kantoui) and baggy pants. SCARF STRICT LOGIC: A SINGLE STRIP OF BOLD RED CLOTH wrapped securely around the neck. The front is tucked; ONLY ONE SINGLE TAIL trails in the wind behind. EXACTLY ONE VISIBLE TRAILING PIECE OF FABRIC. RED IS EXCLUSIVE TO THIS SCARF. NO front drape, NO branching, NO second tail. SYNCHRONIZED WIND LOGIC: The white bob hair and the single red scarf tail MUST flutter in the EXACT SAME DIRECTION. A thick coarse rope (shimenawa) around the waist.

Negative Prompt:
split scarf, bifurcated fabric, forked ends, multiple tails, divided scarf, overly feminine, girly facial features, long eyelashes, heavy makeup, oil painting, thick impasto, ugly, horror, flat cel-shading, modern clothes, western medieval armor, sci-fi
Params: --ar 2:3 --stylize 250 --quality high --seed 55831
```

**バリエーション:**
- **手甲継承版:** 左腕に手甲（BEAT GAUNTLET）を装着した中盤の姿。
- **三種の神器版:** 剣（右手）・鏡（左腕盾）・勾玉・手甲を全装備した最終決戦の姿。スカーフは金継ぎ後に「鈍く黒ばんだ赤（乾いた血の色）」へ変化。

---

### ウズ（狂騒の踊り子）
**コンセプト:** アメノウズメ。道化ではなく古代の奉納舞。しめ縄を模した編み込み髪。

```text
Prompt:
masterpiece, highest quality, extremely captivating and brightly expressive female ritual dancer leaping in mid-air.
style: explosive, dynamic splashes of vibrant pigment and sweeping, fast brushstrokes embodying primal kinetic energy.
details: exceptionally charming facial features with a lively, fierce smile. High twin-tails loosely braided to resemble thick shimenawa ropes. Asymmetrical, multi-layered rough hemp outfit with Jomon-period clay motifs. A giant, translucent ribbon (hagoromo) aggressively swirls around her, colors melting into the air. Chunky bronze magatama bells swing wildly.
texture: skin rendered with warm natural washes revealing paper grain.
background: ancient ruins implied by loose, energetic ink washes.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, 3D render, porcelain skin, modern idol outfit, perfectly clean lines
Params: --ar 2:3 --stylize 250 --quality high --seed 44821
```

---

### マヒト（隻眼の鉄打ち）
**コンセプト:** 加工硬化・破壊靱性のメタファー。傷が硬度を増す鋼。鍛冶場の煤と赤熱。

```text
Prompt:
masterpiece, highest quality, strikingly handsome, rugged, and fiercely masculine one-eyed blacksmith.
style: heavy, somber dark mineral pigments; intense glowing embers SCRATCHED into dark paper like burn marks.
details: bristly dark hair bound by rough cloth. Heavily scarred single eye. Thick cracked leather apron and baggy pants. Left hand rests on a massive iron anvil; right hand firmly grips a short-handled heavy forging hammer. Muscular physique defined by bold ink washes and rough Washi paper texture.
environment: dark traditional forge, soot-stained walls, vivid red/orange splashes for forge heat.

Negative Prompt:
extra weapons, unrequested items, skinny anime boy, flawless skin, smooth surface, modern sci-fi forge, oil painting, flat cel-shading
Params: --ar 3:4 --stylize 250 --quality high --seed 44822
```

---

### タチバナ（反逆の生贄）
**コンセプト:** 濡れたような透明感と悲哀。冷たい海の色が紙に滲み入る。血の赤をアクセントに。

```text
Prompt:
masterpiece, highest quality, stunningly beautiful, slender female warrior standing on a rocky shore, exuding luminous and fragile elegance.
style: melancholic, textured DRY BRUSH strokes of deep ocean blues and sea-greens; delicate ink lines catching on paper grain.
details: incredibly pure, gentle facial features. Long straight hair clinging to pale skin as if soaked with seawater. Simple flowing white robe, hem stained by dark bleeding earth colors. A subtle accent of blood-red woven into the ties of her robe. She gently holds EXACTLY ONE single primitive spear carved from pale driftwood.
texture: translucent watercolor quality skin, paper grain visible, emphasizing mortal fragility.

Negative Prompt:
two spears, multiple spears, dual wielding, heavy weapons, metallic armor, dry flawless hair, porcelain skin, smooth surface, cheerful anime
Params: --ar 2:3 --stylize 250 --quality high --seed 44823
```

---

### ワカヒコ（悲観的な狙撃手）
**コンセプト:** 神の理の体現。制御された筆使い・胡粉の冷たい層。血の赤を矢羽にアクセント。

> **弓の厳守ルール:** 日本の和弓は非対称（上弦が下弦より長い）。必ず非対称で生成すること。

```text
Prompt:
masterpiece, highest quality, strikingly beautiful, ethereal, coldly arrogant youthful male archer standing in profile in a sharp Kyudo side-aiming posture.
style: absolute brush discipline, ZERO chaotic bleeding. Dry brush calligraphy (Kasure) and visible mineral granulation on textured Washi paper.
details: perfect left-right symmetric face. Pale gofun-pigment skin, NO human warmth. Short sleek silvered hair. Noble Heian-period Kariginu robes in luminous pearl-white and pale gold. Frozen in perfect full draw (Kai) holding a massive asymmetrical white-lacquered asymmetric longbow (wa-kyu; upper limb significantly longer than lower). A taut straight white silk bowstring. On his back, an elegant quiver with ONLY blood-red fletching visible. A sharp accent of blood-red on arrow fletchings.

Negative Prompt:
extra weapons, multiple weapons, watercolor bleeding, soft blending, liquid flow, smudging, dirt, mud, messy brushwork, expressive splashes, human warmth, western fantasy, rough hemp, front-facing pose, multiple bows, eboshi
Params: --ar 3:4 --stylize 350 --quality high --seed 44824
```

---

### スクナ（小さな知恵者）
**コンセプト:** 老練な化学者が子供の身体に宿った。可愛げを完全排除。ホルミシスの毒色（酸緑・傷紫）。

```text
Prompt:
masterpiece, highest quality, highly detailed alchemist boy with a sharp, weary, and fiercely intellectual adult aura.
style: acidic and toxic mineral granulation (bruised purples, sickly acid greens) staining the paper around him.
facial features: NOT CUTE, NOT CHERUBIC. Sharp narrowing Sanpaku eyes with a cold analytical gaze. Dark circles from sleepless research. A cynical, arrogant sneer.
details: rough woven cap over extremely short hair. Heavy leather apron scarred by chemical burns. He violently drags a disproportionately MASSIVE ancient stone mortar by a thick rope over his shoulder.

Negative Prompt:
innocent, adorable, cute, cherubic, blush, happy smile, soft pastel colors, clean clothes, cheerful, round eyes, childish innocence
Params: --ar 4:5 --stylize 350 --quality high --seed 44899
```

---

### うかみ（野生と法力の指導者）
**コンセプト:** 本編正史は40歳前後の渋みと威厳ある中年（猿田彦的）を採用。25歳版はサイドエピソードのIF。

> **手甲の継承:** 斥候版は左腕にBEAT GAUNTLETを装着。行者版は手甲を外した素の左腕が遍歴を物語る。

**【斥候バージョン（成熟版）】**
```text
Prompt:
masterpiece, highest quality, strikingly handsome, dignified middle-aged male warrior (approx 40 years old) with immense rugged charm.
style: rough, dry brushstrokes (Kasure) and earthy pigment washes, emphasizing weathered textures.
details: ruggedly attractive face, short well-groomed beard and mustache, sharp aquiline nose, piercing wise eyes, strong jawline. Wind-tousled dark hair with subtle silver strands. Broad muscular build. High-collared dark hemp undershirt, rugged leather gambeson with integrated iron chest-plates, sturdy pants tucked into thick leather gaiters. Weathered hooded hemp travel cloak stained with mud. RIGHT HAND AND ARM BARE, firmly gripping a SINGLE-HEADED heavy wooden spear with EXACTLY ONE broad stone tip at the top. EXCLUSIVELY ON HIS LEFT ARM, HE WEARS THE SIGNATURE BEAT GAUNTLET: a sleek, ergonomic, asymmetrical gauntlet of refined antique black iron (Kurourushi), subtly hammered texture, central bronze disk with concentric ripple grooves, thick deep-indigo braided cord.

Negative Prompt:
gauntlet on right arm, two gauntlets, symmetrical armor, young, boyish, feminine, skinny, clean-shaven (for mature version), double-ended weapon, extra weapons, oil painting, flat cel-shading
Params: --ar 2:3 --stylize 300 --quality high --seed 44827
```

**【行者バージョン】**
```text
Prompt:
masterpiece, highest quality, exceptionally handsome, rugged middle-aged male ascetic (Gyoja) radiating stoic spiritual weight — the same man as the scout, transformed by pilgrimage.
style: solemn, heavy earthy DRY-BRUSH with tones of metallic oxidation (rust and verdigris).
details: ash-gray and silver-streaked hair at temples. Eyes carry deeper, solemn gravity. Heavily layered dark earth-tone and charcoal-gray robes. Thick wooden prayer beads worn smooth by years. HIS LEFT ARM IS NOW BARE OF THE GAUNTLET, SYMBOLIZING THE LEGACY PASSED TO MIKOTO.

Negative Prompt:
youthful, weak, boyish, bright saffron orange robes, vivid warm colors, gauntlet on arm, oil painting, flat cel-shading
Params: --ar 2:3 --stylize 300 --quality high --seed 44828
```

---

## 4. 神・敵ビジュアル定義

### アマテラス（凍結する光の繭）
- シルエットは日食。胡粉の衣は白百合の花弁のように展開。滲みは極小。外周に金環日食を思わせるコロナ状ハロー。表情は怯えたまなざしか、閉じたまま。

### ツクヨミ（無慈悲な刃としての月）
- 直線と鋭角。折り紙のように几帳面な皺。冷たい胡粉白・群青・銀灰。完璧な左右対称の冷たい三白眼。大型の三日月処刑刃を持ち、背後に満月ハロー。

### スサノオ（泥に塗れた原初の嵐）
- 端正な神格だが、肩と衣の縁から泥と血の飛沫が炸裂するハイブリッド。天叢雲剣は金継ぎで繋いだ傷だらけの「魂の器」として描く。根堅洲国での最終試練では残像とノイズが激しくブレる。

### カガセオ（黄金のバグ／再結晶）
- 破片化した神の姿が金継ぎで繋ぎ止められた「人間的な悲劇の英雄」。骨格と表情は読み取れるアシンメトリー。境界から盛り上がる金の漆が星図（星座）の軌跡を走る。岩塊主体を避け、人間的骨格を優先すること（`KagaseoHumanityBias=true`）。

### 澱神・八岐の産土（真エンドボス・キメラ）
- **前半（白化殻モード）:** 完全に滑らかな胡粉の殻。攻撃を無効化する冷たい白。
- **後半（UIジャック・狂宴モード）:** 殻が割れると、錆びた刃・折れた柄・極彩色の和紙の滲み・黒墨の泥が暴力的に噴出。黄金の金継ぎと黒墨が辛うじて繋ぎ止める。

### アメノイワトワケノカミ（絶対孤立システム）
- 高密度の胡粉で塗り込められた白のフラットな巨大防壁。キャラクター的造形を持たない。

---

## 5. 三種の神器ビジュアル定義と物理形状制約

「神が失った完品」ではなく「傷を負い人の手で修復された器」として設計する。

### 天叢雲剣（素体）
- **西洋剣・反りのある日本刀を絶対採用しない。**
- 極端に長く細い古代直刀（Chokuto）。刃幅は全長の1/10以下の平行刃。
- 柄尻に幅広の**円盤状の柄頭（DISC POMMEL）**。鍔はなく、小さな鉄のリング（鎺）のみ。
- 刀身は3セクション構成。繋ぎ目に**太く盛り上がった輝く黄金の金継ぎ**が走り発光。

### 真・天叢雲剣（覚醒状態）
- 固定の剣の形ではなく「任意の武器に宿った魂（状態）」として視覚化する。
- ベース武器のシルエットを保ちつつ、表面を突き破るように極太の黄金の金継ぎが脈打つ。
- 歴代の代受苦・呼び継ぎで消費した武器の幻影がオーラ状に明滅・付随する。

### 八咫鏡（Yata no Kagami）
- マヒトが新造した**無傷で亀裂のない青銅の円盤鏡**。ガラス鏡や古代の遺物ではない。
- 縁は温かみあるアンバーゴールド（縄文風巴紋）。中心部はオリーブグレー。
- 手磨きによる曇りと不均一な乱反射（ghost-like internal glow）を持つ。

### 八尺瓊勾玉（Yasakani no Magatama）
- コイル状・複数ループ・西洋式ネックレスの形状を採用しない。
- 翡翠と黒曜石の原石から粗く切り出した**単一の円状ネックレス（non-overlapping circular strand）**。
- 石器で削った粗い切削跡・天然の鉱脈がそのまま残り、太い麻紐で無造作に結ばれている。

---

## 6. 共通デザイン意匠：ウカミの継承手甲（THE BEAT GAUNTLET）

```text
Prompt Module (キャラクターのdetails:セクションに挿入):
wearing the signature "BEAT GAUNTLET" on the left arm: a sleek, ergonomic, and stylish asymmetrical gauntlet made of refined antique black iron (Kurourushi) with a hand-painted, subtly hammered texture. The lean design features slender, articulated finger plates following natural joint anatomy with bold sumi-e outlines. A central circular bronze disk is deeply etched with concentric ripple grooves showing subtle ink-bleed. The armor is bound by a thick deep-indigo braided cord wrapped with elegant tension, ending in a single dangling tassel. The entire piece exhibits coarse mineral granulation and expressive brushstrokes on textured Washi paper.
```

---

## 7. 武器・アイテムプロンプトおよび環境プロンプト

以下の各プロンプトIDがこのドキュメント内で管理される生成テンプレートである。各ブロックは各キャラクターの専用バリエーションプロンプトと結合して使用する。

| プロンプトID | 内容 |
|---|---|
| `PROMPT_AME_NO_MURAKUMO_VESSEL_WASHI` | 天叢雲剣・素体（魂の器）のアイテム単体プロンプト |
| `PROMPT_MODIFIER_CHIMERA_AND_TRUE_SOUL_WASHI` | 呼び継ぎ武器・真・天叢雲の魂 状態の修飾プロンプト |
| `PROMPT_REMNANT_BONE_ITEM_WASHI` | 遺骨（極大代受苦の産物）のアイテムアイコンプロンプト |
| `PROMPT_SANSHU_AME_NO_MURAKUMO_WASHI` | 天叢雲剣の精密アイテムプロンプト（画像リファレンス必須） |
| `PROMPT_SANSHU_YATA_NO_KAGAMI_WASHI` | 八咫鏡の精密アイテムプロンプト |
| `PROMPT_SANSHU_YASAKANI_NO_MAGATAMA_WASHI` | 八尺瓊勾玉の精密アイテムプロンプト |
| `PROMPT_SANSHU_TRINITY_STILL_LIFE_WASHI` | 三種の神器・集合アイコンプロンプト |
| `NANOBANANAPRO_PROMPT_BEAT_GAUNTLET_ITEM` | 手甲・単体アイテムプロンプト（マネキン腕装着版） |
| `NANOBANANAPRO_PROMPT_WAKAHIKO_CELESTIAL_BOW_AND_QUIVER_ANCHORED` | ワカヒコの天上弓と靭のプロンプト（画像リファレンス必須） |
| `PROMPT_AMATERASU_FREEZE_WASHI` | アマテラス（凍結の繭）キャラクタープロンプト |
| `PROMPT_TSUKUYOMI_PURGE_WASHI` | ツクヨミ（無慈悲な月）キャラクタープロンプト |
| `PROMPT_SUSANOO_STORM_WASHI` | スサノオ（泥の嵐）キャラクタープロンプト |
| `PROMPT_KAGASEO_KINTSUGI_WASHI` | カガセオ（黄金のバグ）キャラクタープロンプト |
| `PROMPT_YAMATA_NO_UBUSUNA_TRUE_END_V1` | 澱神ウブスナ（真エンドボス）のプロンプト |
| `NANOBANANAPRO_PROMPT_YOMOTSU_SHIKOME_WASHI` | 黄泉醜女（伊邪那美型怨念）のプロンプト |
| `NANOBANANAPRO_PROMPT_SERENE_TOWER_WASHI_REVISED` | ツクヨミの静謐塔・環境プロンプト |
| `NANOBANANAPRO_PROMPT_HAKUA_CORRIDOR_WASHI` | 白堊の回廊（ウズとの出会い場所）・環境プロンプト |
| `NANOBANANAPRO_PROMPT_AMAMI_WATCHTOWER_WASHI` | 天望の天守（ワカヒコとの出会い場所）・環境プロンプト |
| `NANOBANANAPRO_PROMPT_YOMOTSU_RITUAL_WASHI` | 黄泉戸喫の儀・環境プロンプト |
| `NANOBANANAPRO_PROMPT_UNIVERSAL_STYLE_TRANSFORMER` | 万能スタイル変換プロンプト（既存画像の和紙変換用） |

> **フル版プロンプトテキスト（英文）は旧 `RPG企画3/Visual_Prompt_Pack_LUMINOUS_WASHI_V3.md` を参照のこと。**
> 次バージョン更新時は本ドキュメントにプロンプト全文を統合する予定。

---

## 8. UI美術定義

- **神のUI（タイムライン等）:** 弥生土器・銅鐸のラインを模した細く幾何学的なデザイン。青白い胡粉・群青の岩絵具。ノイズ発生時、UIの線に物理的な亀裂が入り絵の具が滲み出す。
- **ツクヨミ撃破後の「白化」演出:** 画面UIを純白に染め、文字がひび割れる演出。フラットな無影照明。
- **人のUI（コマンド等）:** 縄文土器の荒々しい粘土の質感。金継ぎのラインで枠が補修されている。
- **マップ:** 「ひび割れた和紙」。移動ルートは「金継ぎのライン（星土の脈継ぎ）」で描画。
- **黄泉戸喫後のHPゲージ:** 和紙に黒墨が染み込み、金継ぎの輝きが走る独特グラフィック。回復時に赤黒いノイズを放つアニメーション。

---

## 9. 生成チェックリスト（実制作時）

1. **造形の担保:** 顔面・体型は「美麗・魅力的（可愛い/かっこいい）」か。ホラーや奇形になっていないか。
2. **構造的破綻の排除（最重要）:** 指の数・腕の本数・関節のねじれ・宙に浮く物体・不自然な武器の持ち方がないか。少しでも解剖学的に破綻している場合はリジェクトする。
3. **アイテム統制:** 指定外の武器・オブジェクトが生成されていないか。「EXACTLY ONE sword」等の数量指定を入れること。
4. **天体属性の即読性:** ツクヨミ＝月、アマテラス＝太陽（隠れた日輪）、カガセオ＝星（星図状金継ぎ）が判別できるか。
5. **筆致コントラスト（コアテーマ・最重要）:**
   - 人間側: 和紙繊維感・水彩の予測不能な滲み（ノイズ）・アナログな温もりがあるか。
   - 神側: 同じ和紙媒体のまま、極度に制御された筆運び・最小滲み・格調色で「静止した理」を示しているか。
6. **金継ぎの因果性:** 金のラインが「異なる筆致階調を縫い止める意味論的アクセント」として機能しているか。ランダムな装飾になっていないか。
