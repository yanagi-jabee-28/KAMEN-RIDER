# 40 Art Direction and Assets (アートと演出) 〜天降（あまくだ）る御子と、星屑の大地〜

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
details: incredibly pure, gentle facial features. Long straight hair clinging to pale skin as if soaked with seawater. Simple flowing white robe, hem stained by dark bleeding earth colors. A subtle accent of blood-red woven into the ties of her robe. (NO WEAPONS).
texture: translucent watercolor quality skin, paper grain visible, emphasizing mortal fragility.

Negative Prompt:
spear, naginata, sword, two weapons, multiple weapons, dual wielding, heavy weapons, metallic armor, dry flawless hair, porcelain skin, smooth surface, cheerful anime
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

---

### フル版プロンプトテキスト集（LUMINOUS WASHI V3）

> **運用注意:** 以下のプロンプトブロックはAIへ入力する際、コードフェンスや `#` マークダウン記号を含めず、`Prompt:` から始まる文章のみを入力すること。

#### ミコト（手甲継承バリエーション） — `NANOBANANAPRO_PROMPT_MIKOTO_GAUNTLET_INHERITANCE`

```text
Prompt:
OPERATIONAL INSTRUCTION (NANOBANANA): Transform and edit using exactly TWO uploaded reference images: 1) Mikoto's base adventurer image, and 2) the Beat Gauntlet image. Use Mikoto as the base and transform his left arm. CRITICAL FIT INSTRUCTION: The gauntlet MUST be resized and re-proportioned to TIGHTLY FIT Mikoto's slender arm. It must NOT appear bulky, loose, or baggy.
masterpiece, highest quality, exquisitely beautiful adventurer with neutral gender identity standing in a windswept ancient landscape.
details:
[CHARACTER] The same Japanese youth with white short bob hair. SCARF STRICT LOGIC: A SINGLE solid red strip wrapped securely. ONLY ONE SINGLE TAIL trails in the wind. The front is tucked. THERE IS EXACTLY ONE END VISIBLE. RED IS EXCLUSIVE TO THE SCARF. The scarf is ONE SOLID PIECE, never splitting or forking. SYNCHRONIZED WIND LOGIC: The white bob hair and the single red scarf tail MUST flutter dynamically in the EXACT SAME DIRECTION. Wearing the off-white sleeveless tunic and baggy pants.
[GAUNTLET — THE BEAT GAUNTLET] ON THE LEFT ARM, HE WEARS UKAMI'S LEGACY: a sleek, ergonomic, and stylish asymmetrical gauntlet (THE BEAT GAUNTLET) made of refined antique black iron with a subtly hammered texture and hand-painted aesthetic. A central circular bronze disk is deeply etched with concentric ripple grooves showing beautiful earthy pigment bleeding. Bound by a thick deep-indigo braided cord wrapped with elegant tension, ending in a single dangling tassel. Slender, articulated finger sections follow natural joint anatomy with bold sumi-e outlines. THE GAUNTLET IS TIGHTLY FITTED EXCLUSIVELY TO HIS SLENDER LEFT ARM; NO BULKINESS. NO sword, NO mirror-shield, NO magatama necklace yet.
mood: the burden of inheritance; a fragile human vessel beginning to carry the weight of legend.

Negative Prompt:
Ame-no-Murakumo, sword, weapon, Yata no Kagami, mirror, shield, Yasakani no Magatama, necklace, jewels, photorealistic, photography, 3D render, CGI, smooth digital painting, overly feminine, girly, split scarf, bifurcated fabric, bad anatomy, signature, watermark

Params: --ar 2:3 --stylize 250 --quality high
```

#### ミコト（三種の神器装備バリエーション） — `NANOBANANAPRO_PROMPT_MIKOTO_SANSHU_NO_JINGI_WASHI`

```text
Prompt:
OPERATIONAL INSTRUCTION (NANOBANANA): Transform and edit using exactly FIVE uploaded reference images: 1) Mikoto's default adventurer image, 2) the Ame-no-Murakumo sword, 3) the Yata no Kagami mirror, 4) the Yasakani no Magatama necklace, and 5) the Beat Gauntlet.
masterpiece, highest quality, exquisitely beautiful and determined adventurer with neutral gender identity standing on a windswept, scarred battlefield.
details:
[SWORD — Ame-no-Murakumo type] Gripping EXACTLY ONE ancient primitive Japanese straight sword (Ame-no-Murakumo) firmly in the right hand. THE LEFT HAND AND BACK ARE EMPTY OF WEAPONS. The blade is EXTREMELY LONG, NARROW, AND HAS PARALLEL SIDES. DARK NEAR-BLACK matte iron. The blade is segmented in construction: EXACTLY THREE visible sections joined by THICK, RAISED golden Kintsugi seams that glow with ember heat. Hilt is simple with a DISC POMMEL at the end; NO western crossguard, NO quillons.
[SHIELD — Yata no Kagami type] Strapped to the left forearm is EXACTLY ONE freshly cast solid bronze disc-mirror (kagami) used as a buckler shield — newly made, NOT an ancient relic. MUST BE A SOLID METAL DISC. NO glass mirror. The face is UNCRACKED AND INTACT.
[GAUNTLET — THE BEAT GAUNTLET] ON THE LEFT ARM, UNDER THE MIRROR-SHIELD, MIKOTO WEARS UKAMI'S LEGACY: a sleek, ergonomic, and stylish asymmetrical gauntlet of refined antique black iron. Central circular bronze disk etched with concentric ripple grooves. Bound by a thick deep-indigo braided cord. THE GAUNTLET IS TIGHTLY FITTED TO HIS SLENDER PROPORTIONS.
[JEWEL — Yasakani no Magatama type] Draped around the neck as a heavy collar-necklace is a single, simple non-wrapped strand of large, freshly carved, curved teardrop-shaped magatama beads (nephrite jade and obsidian).
STRICT SCARF LOGIC (POST-RITUAL VARIANT): The SINGLE SCARF has lost its bright vivid red. It is now a dull, blackened dried-blood red (dark muddy reddish-black). THIS DULL RED IS EXCLUSIVE TO THIS SCARF. ONLY ONE SINGLE TAIL trails behind. NO front drape, NO second tail, NO branching. SYNCHRONIZED WIND LOGIC applies.
background: a scorched, broken landscape; golden kintsugi cracks spread across the earth like roots.
mood: not divine ascension — a mortal who refused to let the tools of heaven remain broken.

Negative Prompt:
split scarf, bifurcated fabric, multiple tails, extra weapons, extra swords, western longsword, crossguard, two shields, bad anatomy, oil painting, 3D render, signature, watermark

Params: --ar 2:3 --stylize 300 --quality high --seed 55832
```

#### 天叢雲剣（素体） — `PROMPT_AME_NO_MURAKUMO_VESSEL_WASHI`

```text
Prompt:
OPERATIONAL INSTRUCTION (NANOBANANA): Transform and edit the uploaded reference image of the sword. Re-render the surfaces into Japanese watercolor while preserving the sword's long, straight structure.
masterpiece, highest quality, the legendary Ame-no-Murakumo in its dormant vessel state — an exceptionally long and narrow Japanese straight sword (Chokuto) floating horizontally, radiating overwhelming heat and the weight of history.
style: traditional Japanese watercolor on Washi paper, extreme contrast between the NEAR-BLACK matte iron of the blade and blinding, raised golden Kintsugi lacquer seams.
details: The blade is long, narrow, and dark as charcoal — NOT a katana, but a primitive Japanese straight sword. The blade is built in EXACTLY THREE visible segmented sections joined end-to-end, each join sealed by THICK, RAISED golden Kintsugi lacquer lines that pulse with thermal energy. NO western crossguard — the hilt is a simple cylinder with a wide DISC POMMEL at the end. The blade surface is entirely matte and light-absorbing — Kintsugi veins are the ONLY source of light. Gold lacquer droplets bleed into the Washi paper.
background: minimal sumi-e void, faint scorched paper texture radiating outward from the sword.

Negative Prompt:
clean pristine blade, shiny typical katana, modern weapon, western longsword, smooth metal, plastic texture, 3D render, cel-shading, oil painting, character holding sword, human, signature, watermark

Params: --ar 3:2 --stylize 300 --quality high --seed 77777
```

#### 呼び継ぎ武器・真魂修飾プロンプト — `PROMPT_MODIFIER_CHIMERA_AND_TRUE_SOUL_WASHI`

```text
PROMPT MODIFIER (Append to the base weapon prompt):
details (Chimera/Soul state): The weapon is grotesquely yet beautifully fused with jagged, mismatched iron fragments from other destroyed weapons, bound violently together by thick, raised, intensely glowing golden Kintsugi seams. These golden seams pulse like veins overflowing with supernova heat. Faint, ghostly afterimages (sumi-e blurred silhouettes) of the consumed weapons' original forms linger around the blade like a mirage. The weapon transcends its original shape, radiating the immense, abrasive, uncontainable history of "Daijuku" self-sacrifice.
```

#### 遺骨アイテム — `PROMPT_REMNANT_BONE_ITEM_WASHI`

```text
Prompt:
masterpiece, highest quality, macro shot of a single, grotesque yet beautiful object: the "Remnant Bone" (遺骨) of a destroyed ancient weapon, resting on textured Washi paper.
style: absolute rejection of watercolor bleeding and soft blending. Painted with heavy, SCRATCHY dry-brush strokes (Kasure) and dense mineral pigments (Iwa-enogu) emphasizing raw friction and material obsession.
details: A jagged, irregular chunk of deeply rusted, scorched iron fused uncontrollably with calcified, bone-like white material. The surface area is scarred with deep gouges. Thick, bulging, violent golden Kintsugi lacquer forcefully binds the disparate materials together, leaking a faint, dying ember-like heat. There is NO life, only the heavy, dry karma of a weapon that refused to disappear.

Negative Prompt:
watercolor bleeding, soft blending, liquid flow, smudging, clean metal, shiny steel, smooth surfaces, perfect geometry, biological flesh, living tissue, 3D render, cel-shading, oil painting, signature, watermark

Params: --ar 1:1 --stylize 300 --quality high --seed 11111
```

#### 天叢雲剣（精密アイテム） — `PROMPT_SANSHU_AME_NO_MURAKUMO_WASHI`

```text
Prompt:
OPERATIONAL INSTRUCTION (NANOBANANA): Transform and edit the uploaded reference image of the sword. Use the reference as the structural skeleton while re-rendering every surface using the following painting styles and textures.
masterpiece, highest quality, painted close-up composition of the legendary Japanese mythological sword Ame-no-Murakumo (天叢雲剣) — an ancient Japanese straight sword (Chokuto / Tsurugi) — lying diagonally on raw fibrous Washi paper. THIS IS A JAPANESE WATERCOLOR PAINTING, NOT A PHOTOGRAPH.
SHAPE (critical): EXTREMELY LONG and NARROW Japanese straight sword. The blade width is NO MORE THAN ONE-TENTH of the total blade length. Long, straight, PARALLEL-SIDED. Reference silhouette: Kofun-era iron tsurugi.
HILT STRUCTURE (critical): This is an ANCIENT JAPANESE STRAIGHT SWORD. POMMEL: At the very END of the handle, a DISTINCTIVE WIDE FLAT DISC POMMEL. BLADE-GRIP JUNCTION: EXACTLY TWO OR THREE small flat iron ring-bands (habaki). NO large protruding crossguard.
details: DARK NEAR-BLACK iron blade. EXACTLY THREE distinct sections joined end-to-end, each seam filled with THICK RAISED golden Kintsugi lacquer glowing with faint ember heat.
background: near-void; scorched sumi-e wash radiating outward.

Negative Prompt:
photography, photorealistic, 3D render, CGI, crossguard, tsuba, quillons, western longsword, short blade, wide blade, curved blade, katana silhouette, shiny polished metal, pristine clean surface, signature, watermark

Params: --ar 3:1 --stylize 300 --quality high --seed 22201
```

#### 八咫鏡 — `PROMPT_SANSHU_YATA_NO_KAGAMI_WASHI`

```text
Prompt:
masterpiece, highest quality, painted close-up composition of a single mythological bronze disc-mirror — the Yata no Kagami — resting face-up on raw fibrous Washi paper. THIS IS A JAPANESE WATERCOLOR PAINTING, NOT A PHOTOGRAPH.
style: solemn DRY-BRUSH painting with a warm bronze, amber-gold, and dull olive-grey palette. Paper grain visible beneath all surfaces.
details: A single, newly cast bronze disc-mirror — freshly made by human hands, NOT an ancient relic. MUST BE A SOLID METAL DISC. NO glass mirror. The face is UNCRACKED AND INTACT. Fresh bronze is warm amber-gold at the rim, transitioning to dull olive-grey at the center where it has been partially hand-polished. The polishing is imperfect — the reflective surface shows faint wobbly tool-marks and irregular patches of matte and dim shine. The rim shows simple, freshly incised Jomon-style spiral motifs (tomoe). The mirror cord (himo) — thick, undyed hemp — is freshly knotted, still stiff.

Negative Prompt:
cracked mirror, broken mirror, shattered mirror, extra items, multiple mirrors, shiny perfect clean mirror, modern glass, porcelain, human figure, character, western decorative mirror, cel-shading, oil painting, signature, watermark

Params: --ar 1:1 --stylize 300 --quality high --seed 22202
```

#### 八尺瓊勾玉 — `PROMPT_SANSHU_YASAKANI_NO_MAGATAMA_WASHI`

```text
Prompt:
masterpiece, highest quality, painted close-up composition of the Yasakani no Magatama — a sacred necklace of ancient magatama beads — arranged in a clear, wide circular loop on raw fibrous Washi paper so that every individual bead is fully visible without overlapping. THIS IS A JAPANESE WATERCOLOR PAINTING, NOT A PHOTOGRAPH.
style: intimate, mineral-rich DRY-BRUSH painting. Jade tones rendered with granulating Iwa-enogu pigments and scratchy brushstrokes.
details: A single, non-overlapping circular strand (necklace) of large, freshly carved, curved teardrop-shaped magatama beads. EVERY BEAD MUST BE DISTINCT AND SEPARATED. Primary stones are carved from raw nephrite jade — rough-cut, still showing stone-tool marks. Matte deep green with visible natural mineral veining. Interspersed are several freshly knapped pieces of raw black obsidian. The threading cord is thick, undyed hemp — a single, clear line freshly cut and tied with a prominent, heavy knot.

Negative Prompt:
coiled strand, wrapped strand, multiple loops, spiral necklace, stacked necklaces, metal setting, gold setting, jewelry box, modern gemstone cut, faceted crystal, sparkle, shine, glossy gem surface, porcelain, human figure, character, signature, watermark

Params: --ar 1:1 --stylize 300 --quality high --seed 22203
```

#### 三種の神器・集合アイコン — `PROMPT_SANSHU_TRINITY_STILL_LIFE_WASHI`

```text
Prompt:
masterpiece, highest quality, a painted still-life composition of EXACTLY THREE sacred objects on raw, textured Washi paper. THIS IS A TRADITIONAL JAPANESE WATERCOLOR PAINTING, NOT A PHOTOGRAPH.
style: disciplined FRICTION-DRY-BRUSH painting. Unified mineral pigment palette. Paper fiber texture visible beneath all surfaces.
arrangement: loose triangular composition. Center-top: dark iron tsurugi sword lying diagonally, Kintsugi seams glowing. Bottom-left: newly cast bronze disc-mirror face-up, INTACT surface, warm amber-gold rim. Bottom-right: single circular strand (necklace) of jade and obsidian magatama.
each object:
— SWORD: near-black matte iron, three-section Bronze-Age straight tsurugi with a wide DISC POMMEL and NO CROSSGUARD; raised gold Kintsugi at seams.
— MIRROR: newly cast solid bronze disc, INTACT face, warm amber-gold rim, imperfectly hand-polished — NO cracks. NO glass mirror.
— JEWEL: single non-overlapping circular strand, freshly carved curved teardrop-shaped magatama beads (jade and obsidian) on hemp cord, rough-cut surfaces.
unifying detail: hairline golden kintsugi cracks in the Washi paper surface itself connect the three objects.

Negative Prompt:
extra items, additional weapons, multiple swords, extra mirrors, extra bead strands, unrequested clutter, human figure, character, hands holding items, elaborate background, 3D render, cel-shading, oil painting, signature, watermark

Params: --ar 3:2 --stylize 350 --quality ultra --seed 22200
```

#### 手甲・単体アイテム — `NANOBANANAPRO_PROMPT_BEAT_GAUNTLET_ITEM`

```text
Prompt:
masterpiece, highest quality, an exquisite close-up study of a legendary artifact: THE BEAT GAUNTLET (Tekko).
CRITICAL COMPOSITION: The gauntlet is securely EQUIPPED on the LEFT ARM AND HAND of a completely featureless, pure white mannequin (a translucent, ghost-like human arm).
details: a sleek, ergonomic, and stylish silhouette made of refined antique black iron (Kurourushi) with a hand-painted, subtly hammered texture. The design is lean and well-proportioned, consisting of a curved forearm guard, a precisely fitted hand plate exclusively for the left hand, and COMPREHENSIVE FINGER ARMOR. Every single finger is fully protected by slender, articulated black iron segmented plates (kozane) that meticulously follow natural joint anatomy. In the center of the forearm is a large, recessed circular bronze disk deeply etched with concentric "ripple" grooves; the bronze shows beautiful earthy pigment bleeding. A thick, deep-indigo braided cord (kumihimo) is wrapped with elegant tension partially around the iron, ending in a single dangling tassel.
style: entirely painted on highly textured, fibrous off-white Washi paper using traditional Japanese mineral pigments (Iwa-enogu) and soft ink washes.

Negative Prompt:
real human skin, living arm, bare fingers, exposed fingertips, clunky, bulky, bloated, oversized, thick-edged, low-detail, photorealistic, 3D render, CGI, glossy, plastic, perfectly smooth, bad anatomy, deformed, signature, watermark

Params: --ar 3:2 --stylize 300 --seed 12345
```

#### ワカヒコの弓と靭 — `NANOBANANAPRO_PROMPT_WAKAHIKO_CELESTIAL_BOW_AND_QUIVER_ANCHORED`

```text
Prompt:
OPERATIONAL INSTRUCTION (NANOBANANA): Transform and edit the uploaded reference image of the bow and quiver. Use the reference as the structural skeleton while re-rendering every surface into high-quality Japanese watercolor on Washi paper.
masterpiece, highest quality, a breathtaking painted still-life composition of EXACTLY TWO (2) distinct items: ONE strung bow and ONE quiver, resting side-by-side on raw, textured off-white Washi paper.
[BOW — Ame-no-Makakumi] A massive, asymmetrical Japanese longbow (wa-kyu) lying horizontally. CRITICAL STRUCTURE: Preserve the single, elegant, crescent-moon curve from the reference. ASYMMETRY LOGIC: The bow is vertically asymmetrical (traditional Wa-kyu), where the upper part above the grip is longer than the lower part. The bow is FULLY STRUNG with a taut, razor-sharp straight bowstring (tsuru). The wood is a SINGLE continuous piece of white-lacquered (Gofun) wood with thin gold leaf seams.
[QUIVER — Yugi] Beside the bow is EXACTLY ONE (1) elegant wood and leather quiver. ARROW LOGIC: Only the blood-red fletching (feathers) are visible; ALL arrowheads are hidden deep inside the body of the quiver.

Negative Prompt:
unstrung bow, loose string, detached string, coiled string, broken string, S-curve bow, arrowheads at quiver opening, reversed arrows, multiple bows, multiple quivers, photography, photorealistic, 3D render, human, oil painting, signature, watermark

Params: --ar 3:2 --stylize 350 --quality high --seed 44825
```

#### アマテラス（凍結の繭） — `PROMPT_AMATERASU_FREEZE_WASHI`

```text
Prompt:
Masterpiece, highest quality, a terrifyingly serene yet pulsatingly regal female deity, Amaterasu, locked in self-imposed absolute isolation with an undeniable life-force that radiates through the stillness.
Style: Traditional Japanese painting on Washi paper. The background features a matte Gofun (seashell white) wash with visible paper fibers and mineral grain. The subject herself is rendered with pristine, flawlessly smooth surfaces and controlled, subtle ink wash elements.
Details: Enveloped in intricate, sculptural multi-layered white ceremonial robes (Heian Kariginu style). The architectural draping mimics frozen lily petals, maintaining a slender, majestic silhouette. Her glossy, straight black silk hair flows beneath a translucent gossamer white veil. She wears an austere, feminine Amaterasu-style crown/kanzashi: a lacquered tiara shaped like a stylized rising sun braid with a tiny cracked gold ring motif. A subtle golden luminescence emanates from beneath her skin and robes, trapping sunlight within her form. Her expression is flawlessly beautiful yet frozen in fragile, eternal fear, eyes closed or gazing blankly. The composition evokes an annular solar eclipse in a completely luminous palette: a brilliant, muted-gold corona radiates outward, while the cocooned core is obscured not by shadow, but by an intensely bright, pale overexposure (halation).

Negative Prompt:
chubby proportions, bulky cocoon mass, bright pop colors, plastic sheen, modern elements, hard 3D render look, cartoon sun icons, heavy blackness, dirty fabric, oil painting, thick impasto, ugly, horror, flat cel-shading, signature, watermark
```

#### ツクヨミ（無慈悲な月） — `PROMPT_TSUKUYOMI_PURGE_WASHI`

```text
Prompt:
Masterpiece, highest quality, an exceedingly beautiful and flawlessly symmetrical male deity, Tsukuyomi, embodying extreme purification and absolute, ruthless execution, his very form crackling with contained vitality and sovereign menace.
Style: Traditional Japanese watercolor on Washi paper, executed with razor-sharp, ultra-controlled fine ink lines. Background retains visible paper fibers and matte mineral texture, with minimal, tightly controlled bleeding. Palette is strictly restricted to freezing Gofun white, intense ultramarine, and muted lunar silver-gray.
Details: Imposing, towering posture with absolute authority. Adorned in sharp-edged, Origami-like ancient court attire that cascades in architectural, flat planes. He wears a subtle, kabuto-like silver lunar circlet integrated seamlessly into his glossy black hair. Bold streams of deep ultramarine and midnight-blue silk elegantly spill from within the intricate layers of his blinding white robes. His face is terrifyingly symmetrical and expressionless, projecting cold arrogance through downward-gazing Sanpaku eyes. In one hand, he wields a massive, exquisite execution weapon: a breathtaking Naginata featuring an enormous, elegantly curved crescent-like blade. The sweeping lunar arc of the blade perfectly mimics a waning moon. Behind him, a perfectly simple, fine-line silver-platinum full-moon halo frames his figure.

Negative Prompt:
bad anatomy, soft pastel tones, weak aura, excessive bleeding, sloppy asymmetry, extra weapons, multiple weapons, eboshi, bulky weapons, oil painting, thick impasto, horror, flat cel-shading, modern elements, synthetic 3D smoothness, signature, watermark

Params: --ar 2:3 --stylize 300 --quality high --seed 23456
```

#### スサノオ（泥に塗れた嵐） — `PROMPT_SUSANOO_STORM_WASHI`

```text
Prompt:
masterpiece, highest quality, an overwhelmingly handsome and fiercely masculine ancient storm god, Susanoo, radiating a wild, heroic aura.
style: traditional Japanese watercolor (Iwa-enogu) on fibrous Washi paper. A breathtaking fusion of immaculate divine line-work and the chaotic, dynamic bleeding of storm-cloud grays, deep ocean blues, and flashes of lightning-gold.
details: He has a fiercely attractive, battle-hardened face with piercing eyes that burn with untamed, primal passion. His wild, wind-whipped dark hair merges with aggressive ink washes of stormy skies. He wears ancient, asymmetrical divine garments (rough woven hemp mixed with torn celestial silk) whipping violently in a typhoon, adorned with massive, curved teardrop-shaped magatama. His legendary Ame-no-Murakumo sword is held in a powerful grip — a massive, rugged straight blade built from three dark iron segments, bound seamlessly by thick, glowing gold kintsugi, symbolizing the first defiant act of human repair. The edges of his form erupt into expressive, splashing watercolor strokes.

Negative Prompt:
extra weapons, modern fantasy armor, glossy surface, plastic texture, serene expression, 3D render, excessive literal mud, dirty face, weak, delicate, western mythology, oil painting, ugly, horror, flat cel-shading, signature, watermark

Params: --ar 2:3 --stylize 300 --quality high --seed 77777
```

#### カガセオ（黄金のバグ） — `PROMPT_KAGASEO_KINTSUGI_WASHI`

```text
Prompt:
masterpiece, highest quality, a tragically beautiful and awe-inspiring human-like male deity, Kagaseo, the primal rebellious star.
style: high contrast Japanese watercolor on rough Washi paper. A violent collision of precise divine line-work and chaotic, expressive chromatic bleeding of dark earth tones, rust, and burning vermilion.
details: He has a powerful, god-like presence with a war-scarred, strikingly beautiful face and a veteran warrior's bearing. His entire silhouette suggests a walking constellation. He wears tattered ceremonial silks and battered divine armor pieces inset with meteorite fragments. Pale flesh-and-blood surfaces peek through gaps, marred by deep catastrophic fissures and scars. These scars are forcefully stitched by thick, glowing, raised golden Kintsugi lacquer. Crucially, the kintsugi network must evoke constellation paths and celestial chart geometry, not random cracks, reinforcing his cosmic motif. Intense inner heat radiates from the cracks as supernova-like flicker bursts, scorching the paper. One eye blazes with uncontainable rebellious thermal energy, like a dying star.

Negative Prompt:
rock golem, full-stone monster, robotic, mechanical, non-human body, smooth lines, perfect symmetry, calm palette, serene expressions, oil painting, flat cel-shading, modern props, signature, watermark

Params: --ar 2:3 --stylize 300 --quality high --seed 34567
```

#### 澱神・八岐の産土（真エンドボス） — `PROMPT_YAMATA_NO_UBUSUNA_TRUE_END_V1`

```text
Prompt:
masterpiece, highest quality, a colossal and terrifying living-chimera entity, composed of exactly eight (8) distinct serpentine heads erupting violently from a shattered, pure-white porcelain-like sensory deprivation shell (Gofun-painted Washi).
Structural Detail: A grotesque collision of false divine sterility and violent human karma. The lower half and edges of the entity are an expanding blast of absolute visual noise — vivid, chaotic watercolor bleeding (intense vermilion, bruised purple, rust, and neon Iwa-enogu pigments) — shattering outward through the flawlessly smooth, stark-white outer husk. The heads feature exposed, raw organic tissue wrapping around thousands of rusted swords and broken blades. Ancient bone fragments serve as jagged structural supports.
Biological Features: Vengeful, glowing vermilion eyes buried deep within the metal-and-meat clusters. The "mouths" are a horrific mix of broken katana shards and stark white, jagged bone fangs. NO smooth animal skin; the surface is a mix of dried, fractured reptilian scales and scorched iron.
Style Application: The shattered husk uses rigid, perfectly smooth lines with ZERO bleeding, while the erupting heads and inner mass use EXPLOSIVE FRICTION-DRY-BRUSH (Kasure) and uncontrolled chromatic bleeding.
Details: The entity is violently bound together by jagged, over-thick golden Kintsugi lacquer lines and jet-black Sumi-e ink streaks that glow like boiling blood.

Negative Prompt:
extra heads beyond eight, fewer than eight heads, human faces, 3D render, plastic texture, smooth porcelain skin on the heads, healthy animal flesh, cute features, happy expressions, clean shiny scales, mechanical robot, sci-fi technology, signature, watermark

Params: --ar 16:9 --stylize 450 --quality ultra --seed 88888
```

#### 黄泉醜女（伊邪那美型怨念） — `NANOBANANAPRO_PROMPT_YOMOTSU_SHIKOME_WASHI`

```text
Prompt:
masterpiece, highest quality, terrifying female apparition born of rot and obsessive grief, a living amalgam of decayed court garments and writhing maggots, painted on fibrous Washi paper with Japanese watercolor.
style: the figure uses uncontrolled bleeding of acid greens, bruised purples, and black iron inks to suggest corruption; the surrounding void is composed of tight, controlled gold-lined cracks.
details: pale, gaunt face partially obscured by a tattered white kimono draped over her head, stained with ink-black blood; hair is long and matted with earth, interwoven with bones and dead leaves; multiple pale arms extend like roots, each ending in clawed fingers. Swarms of smaller yōkai circle at her feet, their forms suggested by rapid, expressive ink splatters. Her eyes glow with a cold, otherworldly vermilion light.

Negative Prompt:
cute, beautiful, clean, serene, pastel colors, western fantasy, mechanical parts, comic style, glossy surfaces, oil painting, flat cel-shading, 3D render, signature, watermark

Params: --ar 2:3 --stylize 350 --quality high --seed 99999
```

#### 白堊の回廊（ウズとの出会い場所） — `NANOBANANAPRO_PROMPT_HAKUA_CORRIDOR_WASHI`

```text
Prompt:
masterpiece, highest quality, an ancient, oppressive celestial corridor (Hakua no Kairou) made of flawless, chalk-white stone walls, suddenly shattered from the inside out, painted in traditional Japanese watercolor on Washi paper.
style: the corridor features perfect, sterile geometry with controlled gofun white and pale silver ink. The explosive breach is rendered with chaotic, wild friction-dry-brush strokes and aggressive, vibrant splashes of vermilion and gold mineral pigments bleeding into the white space.
details: A stark contrast between the claustrophobic, silent perfection of divine architecture and the explosive, muddy heat of human rebellion. The corridor acts as an absolute choke-point, its perfect silence ruptured by the physical friction and explosive noise of an escaping dancer. The cracked white stone walls crumble outward, revealing a chaotic burst of color and energy.
atmosphere: the sudden, jarring destruction of absolute silence; a dynamic visual noise.

Negative Prompt:
modern explosives, fireballs, realistic smoke, sci-fi corridors, cyberpunk, neon lights, characters, human figures, 3D render, glossy surface, cel-shading, oil painting, signature, watermark

Params: --ar 16:9 --stylize 300 --quality high --seed 12346
```

#### ツクヨミの静謐塔 — `NANOBANANAPRO_PROMPT_SERENE_TOWER_WASHI_REVISED`

```text
Prompt:
masterpiece, highest quality, breathtaking architectural scene of a towering sacred structure reaching into the clouds, painted entirely in unified Japanese watercolor and mineral pigments on Washi paper.
style: the tower uses disciplined, thin, highly controlled brushwork with restrained bleeding and dignified colors (gofun white, muted gold, ultramarine); surrounding mud-rich earth uses bold expressive bleeding and rough strokes.
details: cracked terrain is stitched by glowing kintsugi lines (star-sand lacquer) that climb toward the tower, emphasizing tension between wild life-noise and ritual stillness.
atmosphere: overcast sky, quiet flat illumination, solemn and ceremonial mood without modern or sci-fi texture.

Negative Prompt:
porcelain sheen, glossy ceramic, neon sci-fi cityscape, western cathedral, cyberpunk lighting, plastic texture, modern signage, cel-shading, 3D render, oil painting, signature, watermark

Params: --ar 9:16 --stylize 250 --quality high --seed 12345
```

#### 天望の天守（ワカヒコとの出会い場所） — `NANOBANANAPRO_PROMPT_AMAMI_WATCHTOWER_WASHI`

```text
Prompt:
masterpiece, highest quality, an ancient, windswept abandoned celestial watchtower (Amami no Tenshu) perched on a terrifyingly high cliff edge, painted in traditional Japanese watercolor on Washi paper.
style: elegant, cold, and austere brushwork with muted sky-blues and pale grays for the high altitude, contrasting with heavy, dark sumi-e ink washes for the dizzying drop into the muddy earth below.
details: A dilapidated but formerly majestic Japanese-style wooden watchtower balancing precariously on jagged rocks. Fierce winds whip through the open structure. The perspective emphasizes an arrogant, dizzying height looking down upon a scarred, imperfect muddy earth far below, contrasting the celestial coldness with the crawling, mud-stained heat of human struggle. Faint traces of kintsugi-like golden lacquer attempt to hold the crumbling foundation together.
atmosphere: cold, desolate, and observant; the suffocating isolation of the sky.

Negative Prompt:
modern skyscrapers, futuristic towers, european castle, cozy cabin, warm sunlight, characters, human figures, 3D render, glossy surface, cel-shading, oil painting, signature, watermark

Params: --ar 9:16 --stylize 300 --quality high --seed 12347
```

#### 黄泉戸喫の儀 — `NANOBANANAPRO_PROMPT_YOMOTSU_RITUAL_WASHI`

```text
Prompt:
masterpiece, highest quality, a haunting ritual scene where weathered characters eat foul, glowing food in a cavernous, dripping shrine, painted on textured Washi paper in Japanese watercolor.
style: rich uncontrolled bleeding of dark greens, browns, and black inks for rot; contrasting sharp gold kintsugi lines outlining cracked earthenware bowls.
details: weary faces contort with pain and determination as they bite into mud-like offerings; wisps of black smoke rise; ritual implements (bamboo skewers, cracked bowls) are rendered with rough mineral pigments; background is a claustrophobic underground passage with wet stone and bone fragments.
mood: dread mixed with grim resolve, an act that seals characters to a corrupted fate.

Negative Prompt:
bright, cheerful, clean surfaces, modern props, pastel colors, western fantasy, cute, innocent, oil painting, cel-shading, 3D render, signature, watermark

Params: --ar 16:9 --stylize 300 --quality high --seed 123456
```

#### 万能スタイル変換 — `NANOBANANAPRO_PROMPT_UNIVERSAL_STYLE_TRANSFORMER`

```text
Prompt:
OPERATIONAL INSTRUCTION (NANOBANANA): Transform and re-render the uploaded image into the following specific artistic style. Preserve the original composition, subject placement, and character silhouettes exactly, but translate all materials, lighting, and textures into traditional Japanese analog art.
masterpiece, highest quality, professional painting on highly textured, fibrous Washi paper using traditional Japanese mineral pigments (Iwa-enogu) and sumi-e ink washes.
style core: FRICTION-DRY-BRUSH (Kasure) strokes throughout. Every surface must show the organic tooth and raw fiber of the Washi paper. No smooth digital gradients or 3D surfaces.
color & light: powdery mineral granulation, organic analog warmth, ZERO chaotic bleeding, and tightly controlled moisture. Highlights are rendered as unpainted paper or pale gofun-white pigment. Darkest tones are scratchy charcoal-grey sumi ink.
key accent: STRICTLY ONLY if visible cracks or breakage already exist in the source image, they may be subtly emphasized with thin, raised golden Kintsugi lacquer lines. DO NOT add kintsugi or gold lines where none exist in the original composition.

Negative Prompt:
photography, photorealistic, 3D render, CGI, glossy, smooth, plastic, ceramic, porcelain, digital VFX, neon, modern, sci-fi, oil painting, thick impasto, cel-shading, flat vector, bleeding, messy washes, chaotic smudging, unrequested kintsugi, hallucinated gold lines, unnecessary decorative cracks, signature, watermark
```



---

## 8. UI美術定義

- **神のUI（タイムライン等）:** 弥生土器・銅鐸のラインを模した細く幾何学的なデザイン。青白い胡粉・群青の岩絵具。ノイズ発生時、UIの線に物理的な亀裂が入り絵の具が滲み出す。
- **ツクヨミ撃破後の「白化」演出:** 画面UIを純白に染め、文字がひび割れる演出。フラットな無影照明。
- **人のUI（コマンド等）:** 縄文土器の荒々しい粘土の質感。金継ぎのラインで枠が補修されている。
- **マップ:** 「ひび割れた和紙」。移動ルートは「金継ぎのライン（星土の脈継ぎ）」で描画。
- **黄泉戸喫後の活魂（Kakkon）ゲージ:** 和紙に黒墨が染み込み、金継ぎの輝きが走る独特グラフィック。回復時に赤黒いノイズを放つアニメーション。

---

## 9. 演出・音響定義（Actionable Direction）

| 要素 | 演出意図 | サウンド表現 |
|---|---|---|
| **カガセオ（影）** | 宇宙的な異質さと、うかみとの差別化 | 「超新星的な瞬きノイズ」「ガラスが砕けるような高く冷たい音」。獣の咆哮は禁止。 |
| **うかみ（法螺貝）** | 野性的な生存の咆哮、場の繋ぎ止め | 重低音の法螺貝。残響に地鳴りのようなノイズ。 |
| **金継ぎ発動** | 修復の瞬間の熱量と輝き | 金属の激突音 ＋ 瞬間的なホワイトノイズ（再起動音）。 |
| **過熱・沈黙** | 機能を失った武具の無機質な沈黙 | 高音のキーンという耳鳴り。その後、全てのSEから低音が削ぎ落とされる減衰処理。 |
| **天岩戸（凍結）** | 絶対零度の、理による世界の停止 | 完全な無音（デジタルな0）。空調音や環境音も遮断する。 |

---

## 10. 生成チェックリスト（実制作時）

1. **造形の担保:** 顔面・体型は「美麗・魅力的（かっこいい/美しい）」か。ホラーや奇形になっていないか。
2. **構造的破綻の排除（最重要）:** 指の数・腕の本数・関節のねじれ・宙に浮く物体・不自然な武器の持ち方がないか。
3. **アイテム統制:** 指定外の武器・オブジェクトが生成されていないか。
4. **天体属性の即読性:** ツクヨミ＝月、アマテラス＝日輪、カガセオ＝星図状の輝き。
5. **うかみ誤認防止（Act3）:** 第3幕の影に泥・獣・毛並みの質感が混じっていないか。「高く冷たい」印象を維持しているか。
6. **筆致コントラスト:** 人間側の「滲み・熱」と、神側の「細線・静止」が一枚の和紙の上で衝突しているか。
7. **金継ぎの因果性:** 金のラインが「意味のある修復の跡」として機能しているか。
