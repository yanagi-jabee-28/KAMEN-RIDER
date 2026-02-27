# RPG企画3 ビジュアルプロンプト集（LUMINOUS WASHI V3 - Beautiful Bleeding Edition）

## 0. 運用方針（ハイエンドな美しさと「生者の滲み」の共存）

- **AIの「綺麗なイラスト」を肯定しつつ、テクスチャでメタファーを語る。**
- **ロール対応:** キャラデザインは画面上の配置だけでなく、それぞれのRPGロール（リレイヤー、ヴァンガード・ガイド、トリックスターなど）を視覚的に伝えることにも配慮する。
- キャラクターの造形（顔立ち、プロポーション）は、現代のメインストリームが好む「最高に美しく/魅力的」な造形を許容する。
- しかし、単なるフラットなセルルックにはさせない。塗り（マチエール）を **「和紙のテクスチャと、予測不可能な水彩・岩絵具の滲み（Bokashi/Bleeding）」** に限定する。
- **人間側（生者のノイズ）:** 美しい造形でありながら、色彩が滲み、和紙の繊維に吸い込まれるようなアナログな温もりと「コントロール不能な揺らぎ」を持たせる。
- **神・天側（無菌の理）:** 滲みの一切ない、工業製品のように滑らかな白磁の彫刻、または完璧な3Dベクターアートの質感を強制する。
- 両者が接する箇所にのみ、**淡い金色のライン（砕かれた星・カガセオの光＝金継ぎ）**が輝く。

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
(for shared/magic elements): subtle glowing metallic gold kintsugi accents along boundaries (representing shattered stardust),
NO thick impasto, NO oil painting, NO messy mud, NO western horror styles, NO flat cel-shading,

```

---

## 2. 主人公「ミコト」冒険者初期装備（赤スカーフ版）

> ※赤いマフラーは漁村アマで村人から贈られ、うかみが無造作に巻いた「英雄の印」。第2幕で形見となる重要小道具として描写する。
> 
> 

### Prompt for Mikoto (protagonist)

```markdown
# NANOBANANAPRO_PROMPT_MIKOTO_WASHI

# PROMPT
Prompt:
masterpiece, exquisitely beautiful and universally appealing facial features, an expressive young adventurer character standing on a windy cliff.
style: traditional Japanese watercolor on textured Washi paper, beautiful chromatic bleeding, translucent mineral pigments.
details (the figure): pure white short bob hair painted with soft, luminous watercolor bleeds. Wearing an off-white sleeveless tunic and baggy pants. A LONG, FLOWING SCARF of a BOLD RED color wraps around the neck, the red pigment bleeding organically into the surrounding paper texture. A thick coarse rope (shimenawa) around the waist. He appears as a fragile but beautiful mortal human vessel, not a deity.
texture contrast: delicate, glowing accents map across the clothing, contrasting with the soft watercolor washes. The background is a vast, ancient landscape painted with atmospheric ink washes (sumi-e style) and desaturated earth-tone watercolors.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, modern gacha game 3D model, perfectly smooth clothing, western medieval armor, sci-fi, (regal, emperor, divine ruler, god:1.5)
Params:
--ar 2:3 --stylize 250 --quality high --seed 55831

```

---

## 3. 追加キャラクター（和紙・岩絵具仕様）

### キャラクタービジュアル注意

* **うかみ（行者）**: 本編の正史で使用するのは猿田彦的に渋みと威厳のある中年・壮年版である。若々しい25歳前後の青年版はサイドストーリーやクリア後のIF用として別途管理する。**これ以降、デザイン資料や運用テンプレートでは必ず「渋イケオジ」40歳前後のルックを採用し、若年フェイスの生成は禁止する。**

### Prompt for Uzu (ritual shrine dancer)

```markdown
# NANOBANANAPRO_PROMPT_UZU_WASHI

# PROMPT
Prompt:
masterpiece, extremely beautiful facial features with an irresistibly cute, bright smile that still reads as elegant and captivating; an energetic female ritual dancer in mid-air.
style: vibrant Japanese watercolor on textured Washi paper, dynamic splashes of color, beautiful unpredictable bleeding.
details: high twin-tails painted with sweeping, soft watercolor strokes; the hair is braided in a loose shimenawa‑style rope pattern to suggest ritual purity. Asymmetrical, multi-layered hemp outfit with Jomon motifs. A giant, translucent ribbon (hagoromo) floats around her, the colors bleeding softly into the background. Bronze magatama bells hang loosely.
mood: ancient high-energy ritual dance. The ruins in the background are suggested with loose, expressive watercolor washes.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, 3D render, modern idol outfit, perfectly clean lines
Params:
--ar 2:3 --stylize 250 --quality high --seed 44821

```

### Prompt for Mahito (one-eyed blacksmith)

```markdown
# NANOBANANAPRO_PROMPT_MAHITO_WASHI

# PROMPT
Prompt:
masterpiece, strikingly handsome and highly charismatic facial features, a rugged and fiercely masculine one-eyed blacksmith with an undeniably glamorous aura.
style: heavy Japanese mineral pigments (Iwa-enogu) on rough Washi paper, strong contrast, somber watercolor bleeding.
details: short, bristly dark hair bound by cloth. Heavily scarred but dignified single eye. Thick, cracked leather apron and baggy pants rendered with deep, earthy watercolor pigments that bleed slightly at the edges. He is resting his left hand heavily on a large, realistic iron anvil, while his right hand grips a single, short-handled heavy iron forging hammer. The background is a strictly utilitarian, dark traditional forge consisting ONLY of soot-stained walls and a brick furnace, completely devoid of any statues or ornaments. The forge embers are painted as intense, glowing splashes of red and orange pigment soaking into the paper.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, skinny anime boy, perfect flawless skin, modern sci-fi forge, crutches, walking stick, statues, porcelain figures
Params:
--ar 3:4 --stylize 250 --quality high --seed 44822

```

### Prompt for Tachibana (the sacrificed warrior)

```markdown
# NANOBANANAPRO_PROMPT_TACHIBANA_WASHI

# PROMPT
Prompt:
masterpiece, stunningly beautiful with a gentle, even cute innocence in her facial features and a luminous, universally appealing elegance, a slender female warrior standing on a rocky shore.
style: melancholic Japanese watercolor on Washi paper, cold color palette softened by a hint of warmth, soft translucent washes of deep blues and greens.
details: long, straight hair clinging to her as if wet, painted with elegant, flowing ink lines. A flowing white robe stained softly at the hem with dark, bleeding earth colors. She holds a driftwood-like primitive spear. The turbulent ocean behind her is depicted with moody, overlapping watercolor bleeds and sea-green washes, but the overall mood hints at fragile beauty rather than fear.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, cheerful sunny anime, bright pop colors, dry flawless hair
Params:
--ar 2:3 --stylize 250 --quality high --seed 44823

```

### Prompt for Wakahiko (the cynical archer)

```markdown
# NANOBANANAPRO_PROMPT_WAKAHIKO_WASHI

# PROMPT
Prompt:
masterpiece, strikingly handsome and highly charismatic facial features, a cynical smirking male archer with subtle divine accents.
style: striking contrast on Washi paper.
details: medium-length, silver hair painted softly. His tunic is primarily rendered with organic, slightly bleeding watercolors depicting rough hemp cloth, with a small patch or shoulder piece of flawless porcelain-like texture suggesting divine interference. Subtle metallic accents trace the edge of this detail without bisecting the outfit. He is casually gripping only ONE single, massive, asymmetrical mythological Japanese longbow (yumi) in his left hand, painted with loose watercolor strokes.

Negative Prompt:
oil painting, thick impasto, ugly, horror, messy all over, completely symmetrical, modern archery gear, western fantasy ranger, multiple bows, two bows
Params:
--ar 3:4 --stylize 250 --quality high --seed 44824

```

### Prompt for Sukuna (Revised: The Toxic Scholar)

```markdown
# NANOBANANAPRO_PROMPT_SUKUNA_WASHI_V2

# PROMPT
Prompt:
masterpiece, highly detailed, a diminutive alchemist (think Sukunabikona) with a sharp, intellectual aura tinged with wry mischief and relentless focus.
style: traditional Japanese watercolor on textured Washi paper, mineral pigments (Iwa-enogu), but the bleeding colors suggest toxins and chemicals (acid green, bruised purple).
facial features: not overtly cherubic; there remains a faint youthful softness beneath the severity of his expression. He has sharp, narrowing "Sanpaku" eyes with a cold, analytical gaze that still allows a brief amused glint. Dark circles under his eyes from sleepless research. A cynical, arrogant smirk (sneer) on his face, more weary than menacing. He has the look of a weary adult soul in a diminutive form.
details: extremely short hair under a rough woven cap. He is dragging a disproportionately MASSIVE, ancient stone mortar or grinding usu along the ground, pulling it by a thick rope looped over one shoulder; the mortar leaves a smear of dark residue in its wake. The stone is scarred and stained with suspicious residues; the pestle is heavy and worn. He wears a heavy leather apron stained with soot and chemical burns.
atmosphere: The washi paper texture around him is stained with splatters of black ink and poisonous colorful washes, suggesting a dangerous laboratory environment.

Negative Prompt:
innocent, adorable, cute, cherubic, blush, happy smile, disney style, ghibli style, soft pastel colors, clean clothes, mascot character, cheerful, round eyes, childish innocence
Params:
--ar 4:5 --stylize 350 --quality high --seed 44899

```

### Prompt for Sukuna (Revised: The Toxic Scholar, Backpack Variant)

```markdown
# NANOBANANAPRO_PROMPT_SUKUNA_WASHI_V2_BACKPACK

# PROMPT
Prompt:
masterpiece, highly detailed, a diminutive alchemist (think Sukunabikona) with a sharp, intellectual aura tinged with wry mischief and relentless focus.
style: traditional Japanese watercolor on textured Washi paper, mineral pigments (Iwa-enogu), but the bleeding colors suggest toxins and chemicals (acid green, bruised purple).
facial features: not overtly cherubic; there remains a faint youthful softness beneath the severity of his expression. He has sharp, narrowing "Sanpaku" eyes with a cold, analytical gaze that still allows a brief amused glint. Dark circles under his eyes from sleepless research. A cynical, arrogant smirk (sneer) on his face, more weary than menacing. He has the look of a weary adult soul in a diminutive form.
details: extremely short hair under a rough woven cap. He carries an enormous ancient stone mortar or grinding usu on his back, secured by heavy ropes or a wooden frame; the mortar is scarred and stained with dark, suspicious residues. The pestle either hangs at his side or is tucked in the frame. He wears a heavy leather apron stained with soot and chemical burns.
atmosphere: The washi paper texture around him is stained with splatters of black ink and poisonous colorful washes, suggesting a dangerous laboratory environment.

Negative Prompt:
innocent, adorable, cute, cherubic, blush, happy smile, disney style, ghibli style, soft pastel colors, clean clothes, mascot character, cheerful, round eyes, childish innocence
Params:
--ar 4:5 --stylize 350 --quality high --seed 44898

```

### Prompt for Ukami (the mature guide)

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_MATURE_WASHI

# PROMPT
Prompt:
masterpiece, ruggedly handsome mature male guide in his early forties, exuding the gravitas of a wandering sage. His build is solid and weathered; he wears tattered saffron robes and carries an oxidized bronze shakujo (khakkhara) staff, the rings of which emit a faint metallic chime. His face is lined with age and battle scars, his short hair peppered with grey, and a short trimmed beard adds to his venerable presence. His posture is grounded, feet planted in mud, and his eyes hold a fierce determination tempered by deep patience.
style: traditional Japanese watercolor on textured Washi paper, warm earthy pigment bleeding with controlled drips.
details: a faded rope (shimenawa) draped over one shoulder, mud splatters on his sleeves, and subtle golden kintsugi patterns running along the staff. Background hints at a misty field with distant mountains.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, youthful, clean modern clothing, western armor, sci-fi props
Params:
--ar 2:3 --stylize 250 --quality high --seed 77891

```

### Prompt for Ukami (the wild scout)

> ※注: AIモデルは「scout」という語彙からエルフ耳等のファンタジー要素を連想する傾向があるため、プロンプト内で人間の丸い耳であることを明示的に指定しています。
> 
> 

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_WASHI

# PROMPT
Prompt:
masterpiece, exquisitely beautiful and universally appealing facial features, an exceptionally handsome 25-year-old young male scout with a clean-shaven, sharply defined jawline. He possesses an elegant yet masculine heroic aura, piercing yet reliable eyes, and fully human facial features. He is a youthful yet highly capable young adult with commanding presence and stoic dignity – unmistakably Japanese with regular rounded human ears (no pointiness at all) and no animalistic traits. He should look like someone respected and loved by his companions, dressed in simple yet functional gear befitting an early civilization.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: wind‑tousled dark hair tied back with a cloth band. Lean, athletic build painted with warm, organic watercolor washes. Clothing made of woven hemp and soft leather with some decorative stitching and a faded sash. Standing in a relaxed, alert pose with a calm, resolute expression, holding a wooden spear with a shaped stone tip. The ancient woodland background is hinted with deep, overlapping washes of green and brown ink.

Negative Prompt:
old, middle-aged, facial hair, stubble, wrinkles, rugged veteran, uncle, oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, sophisticated weapons, perfectly neat hair, pointed ears, elven features, animal ears, exaggerated anime ears, nudity, exposed torso, undressing, "ears must be rounded human" (affirmative restriction)
Params:
--ar 2:3 --stylize 250 --quality high --seed 44826

```

### Prompt for Ukami (the ascetic 行者 variant)

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_GYOJA_WASHI

# PROMPT
Prompt:
Use the uploaded scout image as the base – edit and transform it into a masterpiece featuring a solemn yet exquisitely beautiful 25-year-old young male ascetic (行者). He is exceptionally handsome, clean-shaven, with an elegant yet masculine heroic aura, tanned skin and regular rounded ears, keeping the original scout’s posture and proportions. He is dressed in weathered saffron robes and has prayer beads around his neck. He holds an ancient Shakujo (Khakkhara) staff; the top of the staff is a single, large hand-forged iron hoop featuring six smaller, loose metal rings dangling and looping from the main large ring. The metal is rendered with the texture of aged, oxidized bronze and rust that bleeds into the paper. His pose remains meditative but alert, set amidst a primordial forest background rendered with deep, overlapping washes of green and brown ink.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: long, flowing dark hair tied back with a frayed rope, lean muscular build painted with warm, organic watercolor washes. Robes and simple sandals show signs of wear from pilgrimage. The environment remains the same primordial forest.

Negative Prompt:
old, middle-aged, facial hair, stubble, wrinkles, rugged veteran, uncle, oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, sophisticated weapons, perfectly neat hair, pointed ears, elven features, animal ears, exaggerated anime ears, nudity, exposed torso, undressing, "ears must be rounded human" (affirmative restriction)
Params:
--ar 2:3 --stylize 250 --quality high --seed 44826

```

### Prompt for Ukami (the wild scout - Rugged Mature Variant)

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_WASHI_MATURE

# PROMPT
Prompt:
masterpiece, strikingly handsome and highly charismatic facial features of a **dignified middle-aged male warrior**, approximately 40 years old. He has a ruggedly attractive face with a well-groomed, short beard and mustache that adds to his mature charm. Piercing, wise eyes that have seen many battles, a sharp aquiline nose, and a strong, defined jawline. A commanding, "Sarutahiko-like" presence that exudes reliability and authority. Fully human facial features with regular rounded ears.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: wind‑tousled dark hair with subtle silver strands, tied back. Broad, muscular build painted with warm, organic watercolor washes. Wearing a combination of woven hemp, thick leather armor pieces, and a faded sash. Standing in a powerful, grounded pose, holding a heavy wooden spear with a broad stone tip. The ancient woodland background is rendered with deep, atmospheric washes of ink.

Negative Prompt:
boyish, feminine, skinny, immature, weak, oil painting, thick impasto, ugly, horror, flat cel-shading, modern clothes, pointed ears, elven features, animal ears, nudity, exposed torso, "ears must be rounded human"
Params:
--ar 2:3 --stylize 300 --quality high --seed 44827

```

### Prompt for Ukami (the ascetic 行者 variant - Rugged Mature Variant)

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_GYOJA_WASHI_MATURE

# PROMPT
Prompt:
Use the uploaded scout image as the base – transform him into a masterpiece featuring a **rugged and heroic middle-aged male ascetic (行者)**. He is exceptionally handsome in a mature way, with a dignified beard and weathered, tanned skin. His expression is stoic and deeply spiritual. He wears layered, weathered saffron robes and heavy prayer beads. He holds an ancient **Shakujo (Khakkhara) staff; the top features a single large iron hoop with six smaller, loose metal rings dangling and looping from the main ring.** The metal is rendered with the texture of aged, oxidized bronze and rust that bleeds into the paper. His build is powerful and imposing, reflecting a life of pilgrimage and physical discipline.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: long, flowing dark hair tied back with a frayed rope. The environment is a primordial forest rendered with deep, overlapping washes of green and brown ink.

Negative Prompt:
youthful, weak, clean-shaven, oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, pointed ears, animal ears, "ears must be rounded human"
Params:
--ar 2:3 --stylize 300 --quality high --seed 44827

```

---

## 4. 神の眷属（白化神・三貴子）の描画例

※ 天側のシステムや敵対存在を描画する場合は、人間側（滲み・和紙）の対極である「無機質・幾何学・ベクター/3D」の質感を強制します。顔立ちの美しさという概念すら超越した、完全な対称物です。

### Prompt for Hakka-shin (Divine Emissary)

```markdown
# PROMPT_DIVINE_EMISSARY_PORCELAIN

# PROMPT
Prompt:
Macro photography of a flawless, absolutely smooth white porcelain sculpture representing a divine emissary.
style: extremely clean 3D render feel, utterly perfect geometric vector-art, zero watercolor, zero bleeding, zero paper texture.
details: A perfectly symmetrical, humanoid-adjacent shape composed of hovering, mirror-polished porcelain shards and cold, reflective bronze plates. The surface has a wet, glossy, ceramic sheen. A cold, neon blue sigil glows from its center.
environment: Suspended in a sterile void of pure, white ambient lighting.

Negative Prompt:
watercolor, ink, washi paper, bleeding, organic lines, human face, illustration, drawing, uneven textures, dirt, mud
Params:
--ar 2:3 --stylize 400 --quality ultra --seed 99911

```

### Prompt for Amaterasu (System Core Freeze)

```markdown
# PROMPT_DIVINE_AMATERASU_CORE_OS

# PROMPT
Prompt:
masterpiece, an overwhelmingly flawless and utterly symmetrical white porcelain female deity entombed within a sterile geometric system.
style: extremely clean 3D render feel, perfectly smooth ceramic surface, totally inorganic and static, absolute geometric perfection, zero watercolor bleeding, zero paper texture, zero human warmth.
details: Dressed in stiff, origami-like porcelain layers that have zero fabric drape. Her eyes are closed, her expression completely frozen and devoid of any emotion or life. She is encased within perfectly radiating concentric rings that look like polished white metal and glass. She represents a frozen operating system, terrifyingly perfect.
environment: A completely sterile, glaring white void with no shadows, no dirt, and no depth beyond sharp geometry.

Negative Prompt:
watercolor, ink, washi paper, bleeding, organic lines, human emotion, messy, dirt, mud, shadows, asymmetric, moving, dynamic
Params:
--ar 2:3 --stylize 400 --quality ultra --seed 99912

```

### Prompt for Tsukuyomi (Anti-Virus Executioner)

> ＊中盤の偽終幕を飾るため、プレイヤーに“勝利の白化”を感じさせつつ、その異質さが後半への不穏な伏線となるような冷徹な表現を目指す。無菌の美と憎悪を顔面に凝縮させる。
> 
> 

```markdown
# PROMPT_DIVINE_TSUKUYOMI_ANTIVIRUS

# PROMPT
Prompt:
masterpiece, a terrifyingly flawless and completely sterile white porcelain male executioner deity composed of sharp, merciless geometric angles.
style: extremely clean 3D render feel, perfectly smooth ceramic surface, completely inorganic, severe clinical lighting that erases all cast shadows and organic depth, zero watercolor bleeding.
details: His expression is a perfectly symmetrical, mask-like stare conveying absolute disgust for organic life. He holds a perfectly straight, razor-thin blade of polished white light/metal. He wears pristine, highly structured white ceremonial garments that look like folded ceramic plates.
environment: A brutally bright, clinically white space without a single speck of dust or shadow. Flat lighting that makes everything look overwhelmingly sterile and two-dimensional despite being 3D.

Negative Prompt:
watercolor, ink, washi paper, bleeding, organic lines, human warmth, messy, dirt, mud, shadows, asymmetric, soft lighting, texture
Params:
--ar 2:3 --stylize 400 --quality ultra --seed 99913

```

---

## 5. 環境 / ステージ用プロンプト

### Prompt for White Porcelain Tower (ツクヨミの白磁塔)

```markdown
# NANOBANANAPRO_PROMPT_WHITE_TOWER_WASHI

# PROMPT
Prompt:
masterpiece, breathtaking architectural scene of a towering white porcelain structure reaching into the clouds.  the tower is perfectly smooth, flawless, and geometric, with no visible seams or texture, giving it the feel of a divine cathedral.  the base of the tower is embedded into a cracked, mud-rich earth that bleeds golden kintsugi lines down its sides, hinting at a hidden connection to something beneath.  the sky around it is overcast with flat, sterile light that eliminates shadows, evoking an uneasy, surgical cleanliness.  faint cracks reveal glimpses of dripping golden lacquer (star-sand) and the diffuse glow suggests an internal vertical chasm leading downward.
style: traditional Japanese watercolor on textured Washi paper for the ground and mud elements, bleeding earth tones; the tower itself rendered as flawless white porcelain with zero bleeding, zero texture, almost like a modern 3D render.  subtle metallic gold accents highlight the kintsugi seams.

Negative Prompt:
oil painting, thick impasto, horror, flat cel-shading, western cathedral, sci-fi cityscape, moss, vines, ancient ruins, rustic wood
Params:
--ar 9:16 --stylize 250 --quality high --seed 12345

```

### Prompt for Muddy Underground Chasm (ヤマト地下迷宮の楔部分)

```markdown
# NANOBANANAPRO_PROMPT_UNDERGROUND_CHASM_WASHI

# PROMPT
Prompt:
masterpiece, claustrophobic subterranean cave filled with dark mud and fetid water, the walls studded with giant glowing kintsugi veins that pulse like arteries.  at the center, a massive white porcelain wedge pierces the earth downward, its surface slick and unblemished, contrasting violently with the viscous brown surroundings.  pools of reflective, oily water show distorted reflections of the porcelain above, giving a sense of vertical drop.
style: traditional Japanese watercolor on Washi paper for the mud and organic textures, bleeding deep browns and greens.  the porcelain wedge is rendered with hyperreal geometric perfection, zero bleeding.  the glowing veins use golden metallic pigment bleeds.

Negative Prompt:
oil painting, thick impasto, medieval dungeon, clean stone, fantasy torchlight, colorful crystals, lush vegetation
Params:
--ar 16:9 --stylize 250 --quality high --seed 54321

```

---

## 6. 生成チェックリスト（実制作時）

* **大衆性と造形の担保:** キャラクターの顔面や体型は、しっかり「美麗・魅力的（可愛い/かっこいい）」になっているか。ホラーや奇形になっていないか。
* **テクスチャコントラスト（コアテーマ）:** - 人間側は、デジタルな「セル塗り」ではなく、「和紙の繊維感」と「水彩・岩絵具の予測不能な滲み（ノイズ）」を帯びているか。

* 神側は、一切の滲みがない「ツルツルに磨き上げられた無菌の白磁・3DCG感」が出ているか。
* **因果のアクセント:** 滲む塗りと、無機質な**黄金のライン**が高いコントラストを描いているか。

これで、不完全な乱れは修復され、金継ぎのごとく美しくひとつの文書として整えられました。もし他にご要望や調整が必要な箇所がございましたら、なんなりとお申し付けください。

---
