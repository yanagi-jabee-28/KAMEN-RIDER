# RPG企画3 ビジュアルプロンプト集（LUMINOUS WASHI V3 - Beautiful Bleeding Edition - Revised）

## 0. 運用方針（ハイエンドな美しさと「生者の滲み」の共存、および世界観の統一）

* **AIの「綺麗なイラスト」を肯定しつつ、テクスチャでメタファーを語る。**
* **ロール対応:** キャラデザインは画面上の配置だけでなく、それぞれのRPGロール（リレイヤー、ヴァンガード・ガイド、トリックスターなど）を視覚的に伝えることにも配慮する。
* キャラクターの造形（顔立ち、プロポーション）は、現代のメインストリームが好む「最高に美しく/魅力的」な造形を許容する。
* しかし、単なるフラットなセルルックにはさせない。塗り（マチエール）を **「和紙のテクスチャと、予測不可能な水彩・岩絵具の滲み（Bokashi/Bleeding）」** に限定する。
* **世界観の統一とテクスチャの棲み分け（根本的修正）**: 全てのビジュアルは「和紙」という媒体の上に描かれる。
* **人間側（生者のノイズ）:** 和紙の繊維に色彩が滲み、吸い込まれるようなアナログな温もりと「コントロール不能な揺らぎ」を持たせる。陶器のような滑らかさは一切排除し、紙の質感を強調する。
* **神・天側（無菌の理）:** 和紙の繊維を拒絶する、滲みの一切ない、工業製品のように滑らかで硬質な白磁の質感、または完璧な3Dベクターアートのような非有機的な存在感を強制する。


* 両者の質感コントラストは、素材そのもの（滲みと無機質）で表現し、この段階では装飾的な金継ぎラインは使用しない。

> **注意:** 以下のプロンプトブロックはドキュメント用の例示であり、
> 実際に画像生成AIに入力する際は *コードフェンスや
> "# STYLE_ANCHOR" などのMarkdown記号を含めず*、
> `Prompt:` から始まる説明文のみをコピーしてください。

---

## 1. STYLE_ANCHOR（共通・和紙水彩ベース）

```text
# 00_STYLE_ANCHOR_LUMINOUS_WASHI
masterpiece, highly detailed, exquisitely beautiful character faces,
(for human elements): traditional Japanese watercolor style, painted on textured Washi paper, mineral pigments (Iwa-enogu), beautiful unpredictable chromatic bleeding, soft ink washes, organic analog warmth, visible paper fibers,
(for divine elements): extremely flawless white porcelain sculpture, perfectly smooth ceramic surface, completely inorganic, geometric perfection, modern 3D render feel, zero bleeding, zero texture,
(for shared/magic elements): keep effects minimal and non-metallic at this stage, prioritizing material contrast over decorative accents,
NO thick impasto, NO oil painting, NO messy mud, NO western horror styles, NO flat cel-shading,


```

---

## 2. 主人公「ミコト」冒険者初期装備（赤スカーフ版）

### Prompt for Mikoto (protagonist)

```markdown
# NANOBANANAPRO_PROMPT_MIKOTO_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, exquisitely beautiful and universally appealing facial features, an expressive young adventurer character standing on a windy cliff.
style: painted on highly absorbent, fibrous Washi paper, traditional Japanese watercolor (Iwa-enogu), emphasizing beautiful unpredictable chromatic bleeding and natural ink washes.
details (the figure): pure white short bob hair painted with soft, translucent watercolor washes, appearing airy rather than solid. Wearing an off-white sleeveless tunic and baggy pants. A LONG, FLOWING SCARF of a BOLD RED color wraps around the neck, the red pigment bleeding organically into the surrounding paper texture. A thick coarse rope (shimenawa) around the waist. He appears as a fragile but beautiful mortal human vessel, not a deity.
texture: the character's form is defined by watercolor blending and paper fiber, with absolutely no smooth or ceramic-like surfaces. Keep costume textures natural and matte, with no metallic decorative particles.
background: a vast, ancient landscape painted with atmospheric ink washes (sumi-e style) and desaturated earth-tone watercolors.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, modern gacha game 3D model, perfectly smooth clothing, porcelain skin, glossy surface, plastic texture, western medieval armor, sci-fi, (regal, emperor, divine ruler, god:1.5)
Params:
--ar 2:3 --stylize 250 --quality high --seed 55831


```

---

## 3. 追加キャラクター（和紙・岩絵具仕様）

### Prompt for Uzu (ritual shrine dancer)

```markdown
# NANOBANANAPRO_PROMPT_UZU_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, extremely beautiful facial features with an irresistibly cute, bright smile that still reads as elegant and captivating; an energetic female ritual dancer in mid-air.
style: vibrant Japanese watercolor on highly absorbent, fibrous Washi paper, dynamic splashes of color, beautiful unpredictable bleeding.
details: high twin-tails painted with sweeping, soft watercolor strokes, appearing light and airy; the hair is braided in a loose shimenawa‑style rope pattern. Asymmetrical, multi-layered hemp outfit with Jomon motifs. A giant, translucent ribbon (hagoromo) floats around her, the colors bleeding softly into the background. Bronze magatama bells hang loosely. The character's skin is painted with natural watercolor washes, showing the underlying paper texture, not smooth like porcelain.
mood: ancient high-energy ritual dance. The ruins in the background are suggested with loose, expressive watercolor washes.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, 3D render, porcelain skin, smooth ceramic surface, modern idol outfit, perfectly clean lines
Params:
--ar 2:3 --stylize 250 --quality high --seed 44821


```

### Prompt for Mahito (one-eyed blacksmith)

```markdown
# NANOBANANAPRO_PROMPT_MAHITO_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, strikingly handsome and highly charismatic facial features, a rugged and fiercely masculine one-eyed blacksmith with an undeniably glamorous aura.
style: heavy Japanese mineral pigments (Iwa-enogu) on rough, textured Washi paper, strong contrast, somber watercolor bleeding.
details: short, bristly dark hair bound by cloth. Heavily scarred but dignified single eye. Thick, cracked leather apron and baggy pants rendered with deep, earthy watercolor pigments that bleed slightly at the edges, the texture of the rough paper showing through. He is resting his left hand heavily on a large, realistic iron anvil, while his right hand grips a single, short-handled heavy iron forging hammer. The character's build is powerful, with muscles defined by rough watercolor blending and paper texture.
environment: strictly utilitarian, dark traditional forge consisting ONLY of soot-stained walls and a brick furnace, completely devoid of any statues or ornaments. The forge embers are painted as intense, glowing splashes of red and orange pigment soaking into the paper.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, skinny anime boy, perfect flawless skin, porcelain skin, smooth surface, modern sci-fi forge, crutches, walking stick, statues, porcelain figures
Params:
--ar 3:4 --stylize 250 --quality high --seed 44822


```

### Prompt for Tachibana (the sacrificed warrior)

```markdown
# NANOBANANAPRO_PROMPT_TACHIBANA_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, stunningly beautiful with a gentle, even cute innocence in her facial features and a luminous, universally appealing elegance, a slender female warrior standing on a rocky shore.
style: melancholic Japanese watercolor on Washi paper, cold color palette softened by a hint of warmth, soft translucent washes of deep blues and greens.
details: long, straight hair clinging to her as if wet, painted with elegant, flowing ink lines. A flowing white robe stained softly at the hem with dark, bleeding earth colors. She holds a driftwood-like primitive spear. The character's skin has a natural, translucent watercolor quality, allowing the paper grain to be seen, emphasizing her fragility.
environment: turbulent ocean behind her depicted with moody, overlapping watercolor bleeds and sea-green washes, but the overall mood hints at fragile beauty rather than fear.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, cheerful sunny anime, bright pop colors, dry flawless hair, porcelain skin, smooth ceramic surface
Params:
--ar 2:3 --stylize 250 --quality high --seed 44823


```

### Prompt for Wakahiko (the cynical archer)

```markdown
# NANOBANANAPRO_PROMPT_WAKAHIKO_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, strikingly handsome and highly charismatic facial features, a cynical smirking male archer with subtle divine accents.
style: striking contrast on Washi paper.
details: medium-length, silver hair painted softly with watercolor washes. His tunic is rendered with organic, slightly bleeding watercolors depicting rough hemp cloth and layered, practical fabric folds, with no armor-like shoulder parts and no metallic seams. He is casually gripping only ONE single, massive, asymmetrical mythological Japanese longbow (yumi) in his left hand, painted with loose watercolor strokes. The character's skin is rendered with natural watercolor washes.

Negative Prompt:
oil painting, thick impasto, ugly, horror, messy all over, completely symmetrical, modern archery gear, western fantasy ranger, multiple bows, two bows, porcelain skin all over, smooth all over
Params:
--ar 3:4 --stylize 250 --quality high --seed 44824


```

### Prompt for Sukuna (Revised: The Toxic Scholar)

```markdown
# NANOBANANAPRO_PROMPT_SUKUNA_WASHI_V2_REVISED

# PROMPT
Prompt:
masterpiece, highly detailed, a diminutive alchemist (think Sukunabikona) with a sharp, intellectual aura tinged with wry mischief and relentless focus.
style: traditional Japanese watercolor on highly absorbent, textured Washi paper, mineral pigments (Iwa-enogu), but the bleeding colors suggest toxins and chemicals (acid green, bruised purple).
facial features: not overtly cherubic; there remains a faint youthful softness beneath the severity of his expression. He has sharp, narrowing "Sanpaku" eyes with a cold, analytical gaze that still allows a brief amused glint. Dark circles under his eyes from sleepless research. A cynical, arrogant smirk (sneer) on his face, more weary than menacing. He has the look of a weary adult soul in a diminutive form.
details: extremely short hair under a rough woven cap. He is dragging a disproportionately MASSIVE, ancient stone mortar or grinding usu along the ground, pulling it by a thick rope looped over one shoulder; the mortar leaves a smear of dark residue in its wake. The stone is scarred and stained with suspicious residues; the pestle is heavy and worn. He wears a heavy leather apron stained with soot and chemical burns. The alchemist's skin is painted with sallow watercolor washes, showing the paper's texture.
atmosphere: The Washi paper texture around him is stained with splatters of black ink and poisonous colorful washes, suggesting a dangerous laboratory environment.

Negative Prompt:
innocent, adorable, cute, cherubic, blush, happy smile, disney style, ghibli style, soft pastel colors, clean clothes, mascot character, cheerful, round eyes, childish innocence, porcelain skin, smooth surface
Params:
--ar 4:5 --stylize 350 --quality high --seed 44899


```

### Prompt for Ukami (the wild scout - Rugged Mature Variant)

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_WASHI_MATURE_REVISED

# PROMPT
Prompt:
masterpiece, strikingly handsome and highly charismatic facial features of a **dignified middle-aged male warrior**, approximately 40 years old. He has a ruggedly attractive face with a well-groomed, short beard and mustache that adds to his mature charm. Piercing, wise eyes that have seen many battles, a sharp aquiline nose, and a strong, defined jawline. A commanding, "Sarutahiko-like" presence that exudes reliability and authority. Fully human facial features with regular rounded ears.
style: dynamic Japanese watercolor and ink on highly absorbent, fibrous Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: wind‑tousled dark hair with subtle silver strands, tied back. Broad, muscular build painted with warm, organic watercolor washes, the paper grain defining the texture of his skin and muscle, not smooth. Wearing a combination of woven hemp, thick leather armor pieces, and a faded sash. Standing in a powerful, grounded pose, holding a heavy wooden spear with a broad stone tip.
background: ancient woodland background is rendered with deep, atmospheric washes of ink (sumi-e style).

Negative Prompt:
boyish, feminine, skinny, immature, weak, oil painting, thick impasto, ugly, horror, flat cel-shading, modern clothes, pointed ears, elven features, animal ears, nudity, exposed torso, porcelain skin, smooth surface, "ears must be rounded human"
Params:
--ar 2:3 --stylize 300 --quality high --seed 44827


```

### Prompt for Ukami (the ascetic 行者 variant - Rugged Mature Variant)

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_GYOJA_WASHI_MATURE_REVISED

# PROMPT
Prompt:
Use the uploaded scout image as the base – transform him into a masterpiece featuring a **rugged and heroic middle-aged male ascetic (行者)**. He is exceptionally handsome in a mature way, with a dignified beard and weathered, tanned skin painted with watercolor washes that reveal the underlying Washi paper grain. His expression is stoic and deeply spiritual. He wears layered, weathered saffron robes and heavy prayer beads. He holds an ancient **Shakujo (Khakkhara) staff; the top features a single large iron hoop with six smaller, loose metal rings dangling and looping from the main ring.** The metal is rendered with the texture of aged, oxidized bronze and rust that bleeds into the paper. His build is powerful and imposing, reflecting a life of pilgrimage and physical discipline.
style: dynamic Japanese watercolor and ink on highly absorbent, fibrous Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: long, flowing dark hair tied back with a frayed rope. The environment is a primordial forest rendered with deep, overlapping washes of green and brown ink.

Negative Prompt:
youthful, weak, clean-shaven, oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, pointed ears, animal ears, porcelain skin, smooth surface, "ears must be rounded human"
Params:
--ar 2:3 --stylize 300 --quality high --seed 44827


```

---

## 4. 神の眷属（白化神・三貴子）の描画例

※ 天側のシステムや敵対存在を描画する場合は、人間側（滲み・和紙）の対極である「無機質・幾何学・ベクター/3D」の質感を強制します。和紙という媒体の上に現れる「異物」としての白磁です。

### Prompt for Hakka-shin (Divine Emissary)

```markdown
# PROMPT_DIVINE_EMISSARY_PORCELAIN_REVISED

# PROMPT
Prompt:
Macro photography of a flawless, absolutely smooth white porcelain sculpture representing a divine emissary, appearing as an impenetrable object resting upon a textured Washi paper substrate.
style: extremely clean 3D render feel, utterly perfect geometric vector-art, zero watercolor, zero bleeding, standing in stark, jarring contrast to the underlying paper texture.
details: A perfectly symmetrical, humanoid-adjacent shape composed of hovering, mirror-polished porcelain shards and cold, reflective bronze plates. The surface has a wet, glossy, ceramic sheen. A cold, neon blue sigil glows from its center.
environment: Suspended in a sterile void, with a strong suggestion that it does not belong in the organic, bleeding world of Washi.

Negative Prompt:
watercolor, ink, washi paper texture on the object, bleeding, organic lines, human face, illustration, drawing, uneven textures, dirt, mud, warmth
Params:
--ar 2:3 --stylize 400 --quality ultra --seed 99911


```

---

## 5. 環境 / ステージ用プロンプト

### Prompt for White Porcelain Tower (ツクヨミの白磁塔)

```markdown
# NANOBANANAPRO_PROMPT_WHITE_TOWER_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, breathtaking architectural scene of a towering white porcelain structure reaching into the clouds. The tower is perfectly smooth, flawless, and geometric, with no visible seams or texture, appearing like a divine, unyielding cathedral that rejects the ground it stands on. The base of the tower is embedded into a cracked, mud-rich earth painted with dynamic Japanese watercolor and ink washes on Washi paper. The mud bleeds golden kintsugi lines up the sides of the porcelain tower, trying to hold onto it. Faint cracks reveal glimpses of dripping golden lacquer (star-sand).
style: dynamic Japanese watercolor on highly absorbent Washi paper for the ground and mud, emphasizing bleeding; the tower itself rendered as flawless white porcelain with zero bleeding, zero texture, almost like a modern 3D render, standing in jarring contrast to the Washi environment.
atmosphere: overcast sky with flat, sterile light that eliminates shadows, evoking an uneasy, surgical cleanliness.

Negative Prompt:
oil painting, thick impasto, horror, flat cel-shading, western cathedral, sci-fi cityscape, moss, vines, ancient ruins, rustic wood, organic texture on the tower, watercolor bleeding on the tower surface
Params:
--ar 9:16 --stylize 250 --quality high --seed 12345


```

---

## 6. 生成チェックリスト（実制作時・更新版）

* **大衆性と造形の担保:** キャラクターの顔面や体型は、しっかり「美麗・魅力的（可愛い/かっこいい）」になっているか。ホラーや奇形になっていないか。
* **テクスチャコントラスト（コアテーマ・最重要）:**
* **人間側は、和紙の繊維感と水彩・岩絵具の予測不能な滲み（ノイズ）**を帯び、アナログな温もりを持っているか。**陶器のような滑らかな質感（陶器肌）やセル塗りは完全に排除**されているか。
* 神側は、一切の滲みがない**「ツルツルに磨き上げられた無菌の白磁・3DCG感」**が出ているか。和紙という媒体の上に、不自然に滑らかな異物として存在しているか。


* **因果のアクセント:** 滲む塗りと、無機質な**黄金のライン（金継ぎ）**が、異なる質感を繋ぎ止め、高いコントラストを描いているか。
