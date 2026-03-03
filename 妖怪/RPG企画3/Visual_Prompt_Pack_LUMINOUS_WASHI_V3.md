# RPG企画3 ビジュアルプロンプト集（LUMINOUS WASHI V3 - Beautiful Bleeding Edition - Revised）

## 0. 運用方針（ハイエンドな美しさと「生者の滲み」の共存、および世界観の統一）

* **AIの「綺麗なイラスト」を肯定しつつ、テクスチャでメタファーを語る。**
* **ロール対応:** キャラデザインは画面上の配置だけでなく、それぞれのRPGロール（リレイヤー、ヴァンガード・ガイド、トリックスターなど）を視覚的に伝えることにも配慮する。
* キャラクターの造形（顔立ち、プロポーション）は、現代のメインストリームが好む「最高に美しく/魅力的」な造形を許容する。
* しかし、単なるフラットなセルルックにはさせない。塗り（マチエール）を **「和紙のテクスチャと、予測不可能な水彩・岩絵具の滲み（Bokashi/Bleeding）」** に限定する。
* **世界観の統一（同一キャンバス原則）**: 神も人も、全て「和紙」という媒体の上に描く。素材の断絶（陶器/3D異物化）は採用しない。
* **武器プロンプト:** 武器は上記素材セット（石・骨・木・麻・和紙・泥）を強調し、破砕・修復（ひび割れ＋金継ぎ）の表現を積極的に指示する。日用品／祭具カテゴリは荒れた滲みと用途外の不均衡な形状を許容し、王道武器は機能美と泥汚れを併せ持つ。共有カテゴリを用いる場合は、各キャラ固有の装飾や色調で差別化するようプロンプトに明記する。
* **人間側（生者のノイズ）:** 和紙繊維に色彩が大きく滲み、掠れやにじみ戻りを含む奔放な筆致で「変化し続ける生命」を示す。色は泥・鉄錆・枯葉などの土系を主軸にする。
* **神・天側（静謐の理）:** 同じ和紙上で、滲みを最小化した端正な細線と制御された筆運びを徹底する。色は胡粉・鈍い金箔・群青・朱など、格調高い伝統色で統一する。
  * 三貴子（アマテラス・ツクヨミ・スサノオ）は天の理の三面相として一塊に扱い、原初の反逆者である星神カガセオは完全に独立した対極として位置付ける。三貴子側は「太陽」「月」「嵐（泥）」の天体モチーフを共有しつつ、カガセオは「星」の破片と熱暴走を表現し、人間側と同じく（あるいはそれ以上に）荒々しい滲みと熱量で描く。

* 両者のコントラストは素材差ではなく、**筆致の洗練度／色階の格調／静止と動揺**で表現する。金継ぎは境界を縫う意味論的アクセントとして用いる。

> **注意:** 以下のプロンプトブロックはドキュメント用の例示であり、
> 実際に画像生成AIに入力する際は *コードフェンスや
> "# STYLE_ANCHOR" などのMarkdown記号を含めず*、
> `Prompt:` から始まる説明文のみをコピーしてください。

---

## 1. STYLE_ANCHOR（共通・和紙水彩ベース）

```markdown
# 00_STYLE_ANCHOR_LUMINOUS_WASHI
masterpiece, highly detailed, exquisitely beautiful character faces,
(for human elements): traditional Japanese watercolor style, painted on textured Washi paper, mineral pigments (Iwa-enogu), beautiful unpredictable chromatic bleeding, soft ink washes, organic analog warmth, visible paper fibers,
(for divine elements): the same Washi + Iwa-enogu medium, ultra-refined disciplined brushwork with visible paper fibers and powdery mineral granulation, low but organic controlled bleeding at edges, matte chalk-like gofun layering, precise line control, dignified traditional colors (gofun white, muted gold leaf, ultramarine, vermilion), solemn stillness,
(for shared/magic elements): keep effects minimal and non-metallic at this stage, prioritizing brushwork hierarchy over decorative accents,
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

### Prompt for Wakahiko (Divine Elegance / 天の貴人)

```markdown
# NEW_WAKAHIKO_DIVINE_ELEGANCE_PROMPT

# PROMPT
Prompt:
masterpiece, strikingly beautiful and youthful male archer, Wakahiko.
Style: Traditional Japanese watercolor (Iwa-enogu) on textured fibrous Washi paper. Unified art style across all elements.
Character: He represents "Divine Order" through extreme refinement. His skin is rendered with pale, matte Gofun (seashell white) pigments, showing subtle paper texture but no blemishes. His silver hair is painted with precise, fine brushstrokes using dilute sumi ink and metallic silver pigment, flowing like silk thread.
Costume: Noble Heian-period inspired divine robes (Kariginu style) in luminous pearl-white and pale gold. The fabric patterns are intricate but elegant, with subtle chromatic bleeding only at the very edges of the ink lines.
Weapon: A massive asymmetrical Japanese yumi (wa-kyu) made of white-lacquered wood with visible brush streaks and gold leaf seams, glowing with a soft, ethereal inner light. No modern or plastic textures.
Environment: A serene, misty landscape of the celestial plain (Takamanohara). Atmospheric sumi-e haze, soft-focus mountains in the background.
Mood: Arrogant stillness, the quiet before a divine decree. A meticulously hand-painted entity whose restraint and brush discipline make him look distant from mud, but never synthetic.

Negative Prompt:
porcelain skin, plastic, ceramic texture, 3D render, glossy finish, vector art, modern clothes, mechanical gear, rough hemp (on this version), dirt, mud, chaotic bleeding, messy brushwork, western fantasy.
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

<!-- Canonical Ukami design: middle-aged (~40) appearance is primary. Youthful 25‑year-old variant is secondary/IF only; ensure AI workflows prioritize mature look and disable younger features for core assets. -->
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

## 4. 天の理（三貴子）の描画例

※ 三貴子を天の理の三面相として扱う。天側のシステムや敵対存在を描画する場合も、人間側と同じ和紙媒体で統一する。差異は「滲みゼロの異物感」ではなく、筆致的な制御精度・構図の整然さ・格調色の運用で表現する。

---

## 5. 原初の反逆者（反逆星神カガセオ）の描画例

※ 三貴子とは独立したカテゴリとして、カガセオは「熱暴走のバグ」及び人間側の荒々しさを併せ持った表現をする。


### Prompt for Amaterasu (system-freeze cocoon)

```markdown
# PROMPT_AMATERASU_FREEZE_WASHI

# PROMPT
Prompt:
Masterpiece, a terrifyingly serene and impeccably beautiful female deity, Amaterasu, locked in self-imposed absolute isolation.
Style: Traditional Japanese painting on Washi paper. The background features a matte Gofun (seashell white) wash with visible paper fibers and mineral grain, ensuring the hand-painted materiality. Controlled, subtle ink wash elements. The subject herself is rendered with pristine, flawlessly smooth surfaces.
Details: Enveloped in intricate, sculptural multi-layered white ceremonial robes (Heian Kariginu style). The architectural draping mimics frozen lily petals, maintaining a slender, majestic silhouette through structural tension rather than bulky mass, with her hands entirely hidden. Her glossy, straight black silk hair flows beneath a translucent gossamer white veil. The diaphanous veil naturally drapes over her head, allowing the exquisite head ornament beneath to remain fully visible and unobstructed. She wears an austere, feminine Amaterasu-style crown/kanzashi: a lacquered tiara shaped like a stylized rising sun braid with a tiny cracked gold ring motif, positioned high on the forehead. Deep within the immaculate white folds, elusive glimpses of a crimson silk lining cascade like a hidden red sash, accompanied by the faintest ancient, weathered brushstrokes of solar vermilion along the inner hems, suggesting ritual dye. A subtle golden luminescence emanates from beneath her skin and robes, trapping sunlight within her form. Her expression is flawlessly beautiful yet frozen in fragile, eternal fear, eyes closed or gazing blankly. The composition evokes an annular solar eclipse in a completely luminous palette: a brilliant, muted-gold corona radiates outward, while the cocooned core is obscured not by shadow, but by an intensely bright, pale overexposure (halation). The surrounding atmosphere is a pale shrine-like space with floating gold dust and washed-out ink, entirely devoid of heavy darkness or solid black discs.

Negative Prompt:
 oil painting, thick impasto, ugly, horror, flat cel-shading, chubby proportions, bulky cocoon mass, bright pop colors, plastic sheen, seamless synthetic surfaces, modern elements, high contrast shadows, hard 3D render look, depiction of spiky circles, cartoon sun icons, heavy blackness, dirty fabric
```

---

### Prompt for Tsukuyomi (sterile execution)

```markdown
# PROMPT_TSUKUYOMI_PURGE_WASHI

# PROMPT
Prompt:
Masterpiece, an exceedingly beautiful and flawlessly symmetrical male deity, Tsukuyomi, embodying extreme purification and absolute, ruthless execution.
Style: Traditional Japanese watercolor on Washi paper, executed with razor-sharp, ultra-controlled fine ink lines. Background retains visible paper fibers and matte mineral texture, with minimal, tightly controlled bleeding. Palette is strictly restricted to freezing Gofun white, intense ultramarine, and muted lunar silver-gray.
Details: Imposing, towering posture with absolute authority. Adorned in sharp-edged, Origami-like ancient court attire that cascades in architectural, flat planes like folded steel blades. He wears a subtle, kabuto-like silver lunar circlet integrated seamlessly into his glossy black hair; the hair flows just past his shoulders, weaving intricately through and around the silver ornament, creating a nocturnal diadem effect. Bold streams of deep ultramarine and midnight-blue silk elegantly spill and peek from within the intricate layers of his blinding white robes. These striking azure fabrics slice through the stark white folds like the night sky cutting through clouds, heavily emphasizing his nocturnal dominion. His face is terrifyingly symmetrical and expressionless, projecting cold arrogance through downward-gazing Sanpaku eyes. In one hand, he wields a massive, exquisite execution weapon: a breathtaking Naginata featuring an enormous, elegantly curved crescent-like blade. The sweeping lunar arc of the blade perfectly mimics a waning moon, serving as both a divine symbol and a devastating instrument of purge. Subtle crescent moon phases are etched into his armor trims and sash. The lighting scheme utilizes dramatic inverse silhouetting: he is set against a deep indigo-to-black night wash, yet his white body and garments emit a self-luminous, shadow-thin, flattened radiance. Behind him, a perfectly simple, fine-line silver-platinum full-moon halo frames his figure, devoid of excessive aura.

Negative Prompt:
soft pastel tones, weak aura, plain costume, excessive bleeding, sloppy asymmetry, warm cinematic shadows, oil painting, thick impasto, horror, flat cel-shading, portrait orientation inconsistency, modern elements, synthetic 3D smoothness, eboshi, bulky weapons, double-bladed haft
Params:
--ar 2:3 --stylize 300 --quality high --seed 23456
```

```markdown
# PROMPT_SUSANOO_STORM_WASHI

# PROMPT
Prompt:
masterpiece, an overwhelmingly handsome and fiercely masculine ancient storm god, Susanoo, radiating a wild, heroic aura.
style: traditional Japanese watercolor (Iwa-enogu) on fibrous Washi paper. A breathtaking fusion of immaculate divine line-work and the chaotic, dynamic bleeding of storm-cloud grays, deep ocean blues, and flashes of lightning-gold.
details: He has a fiercely attractive, battle-hardened face with piercing eyes that burn with untamed, primal passion. His wild, wind-whipped dark hair merges with aggressive ink washes of stormy skies. He wears ancient, asymmetrical divine garments (rough woven hemp mixed with torn celestial silk) whipping violently in a typhoon, adorned with massive magatama. His legendary Ame-no-Murakumo sword is held in a powerful grip—a massive, rugged blade visibly patched with thick, glowing gold kintsugi, studded with ancient iron and bone, symbolizing the first defiant act of human repair. The edges of his form and the background erupt into expressive, splashing watercolor strokes resembling crashing waves, driving rain, and thunderous gales. He embodies the majestic violence of a storm, the very first emotional 'bug' to shatter the silent heavens.
atmosphere: Epic, tempestuous, and undeniably cool. The Washi paper texture grounds the mythical storm in a heavy, organic, hand-painted reality.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, modern fantasy armor, glossy surface, plastic texture, serene expression, 3D render, excessive literal mud, dirty face, weak, delicate, western mythology
Params:
--ar 2:3 --stylize 300 --quality high --seed 77777
```
---

## 5. 原初の反逆者（反逆星神カガセオ）の描画例

※ 三貴子とは独立したカテゴリとして、カガセオは「熱暴走のバグ」及び人間側の荒々しさを併せ持った表現をする。

---

### Prompt for Kagaseo (shattered kintsugi giant)

```markdown
# PROMPT_KAGASEO_KINTSUGI_WASHI

# PROMPT
Prompt:
masterpiece, a tragically beautiful and awe-inspiring human-like male deity, Kagaseo, the primal rebellious star.
style: high contrast Japanese watercolor on rough Washi paper. A violent collision of precise divine line-work and chaotic, expressive chromatic bleeding of dark earth tones, rust, and burning vermilion.
details: He has a powerful, god‑like presence with a war‑scarred, strikingly beautiful face. His stance and bearing are those of a veteran warrior; his movements echo the precision of a seasoned martial artist. His entire silhouette suggests a walking constellation: armor plates are arranged like star-fields, and thin bands of glowing lacquer trace the paths of stellar charts across his body. Rather than being nude, he wears tattered ceremonial silks and battered divine armor pieces inset with meteorite fragments and gold leaf, arranged like ritual vestments that double as battle gear. The armor is dented and scorched, testament to innumerable celestial duels, yet still holds together through sheer divine will. Pale flesh-and-blood surfaces peek through ceremonial gaps and are marred by deep catastrophic fissures and scars, forcefully stitched by thick, glowing, raised golden Kintsugi lacquer. Shape the kintsugi network to evoke constellation paths and celestial chart geometry rather than random cracks, reinforcing the cosmic motif. Fragmented meteoric plates and mineral shards remain as partial overlays on shoulders, ribs, and limbs, integrated into his divine vestments. Intense inner heat radiates from the cracks as supernova-like flicker bursts and star-spark spray, scorching the paper. One eye blazes with uncontainable rebellious thermal energy, like a dying star. A visual representation of raw tragic human passion and divine rebellion crystallized, his body itself a map of the heavens.

Negative Prompt:
rock golem, full-stone monster, robotic, mechanical, non-human body, smooth lines, perfect symmetry, calm palette, flat cel-shading, oil painting, modern props, serene expressions, minimalist backgrounds
Params:
--ar 2:3 --stylize 300 --quality high --seed 34567
```

---

## 4.5 黄泉の女陰／怨念集合体

### Prompt for Yomotsu Shikome (Izanami-entity)

```markdown
# NANOBANANAPRO_PROMPT_YOMOTSU_SHIKOME_WASHI

# PROMPT
Prompt:
masterpiece, terrifying female apparition born of rot and obsessive grief, a living amalgam of decayed court garments and writhing maggots, painted on fibrous Washi paper with Japanese watercolor.
style: the figure uses uncontrolled bleeding of acid greens, bruised purples, and black iron inks to suggest corruption; the surrounding void is composed of tight, controlled gold-lined cracks.
details: pale, gaunt face half-covered by tattered white kimono stained with ink-black blood; hair is long and matted with earth, interwoven with bones and dead leaves; multiple pale arms extend like roots, each ending in clawed fingers. Swarms of smaller yōkai (黄泉醜女) circle at her feet, their forms suggested by rapid, expressive ink splatters. Her eyes glow with a cold, otherworldly vermilion light.
mood: absolute dread, the sensation of being pursued by a nightmare that knows your every weakness.

Negative Prompt:
cute, beautiful, clean, serene, oil painting, flat cel-shading, 3D render, pastel colors, western fantasy, mechanical parts, comic style, glossy surfaces
Params:
--ar 2:3 --stylize 350 --quality high --seed 99999

```

---

### Prompt for Hakka-shin (Divine Emissary)

```markdown
# PROMPT_DIVINE_EMISSARY_WASHI_REFINED

# PROMPT
Prompt:
masterpiece, divine emissary rendered in unified Japanese watercolor on textured Washi paper, austere and perfectly balanced composition.
style: ultra-controlled sumi and Iwa-enogu brushwork, minimal bleeding, razor-clean contour rhythm, high ceremonial stillness.
details: humanoid-adjacent sacred figure with strict symmetry, layered gofun whites, muted gold leaf accents, ultramarine and vermilion glyph motifs, matte mineral surface with visible paper fibers.
environment: sacred empty court at dawn, thin mist, restrained palette, no modern elements.

Negative Prompt:
3D render, glossy ceramic, porcelain shards, plastic texture, neon sci-fi, mechanical parts, cyberpunk UI, western fantasy armor, chaotic splatter, cartoon cel-shading
Params:
--ar 2:3 --stylize 400 --quality ultra --seed 99911


```

---

## 5. 環境 / ステージ用プロンプト

### Prompt for Yomotsu Hegui Ritual

```markdown
# NANOBANANAPRO_PROMPT_YOMOTSU_RITUAL_WASHI

# PROMPT
Prompt:
masterpiece, a haunting ritual scene where weathered characters eat foul, glowing food in a cavernous, dripping shrine, painted on textured Washi paper in Japanese watercolor.
style: rich uncontrolled bleeding of dark greens, browns, and black inks for rot; contrasting sharp gold kintsugi lines outlining cracked earthenware bowls.
details: weary faces contort with pain and determination as they bite into mud-like offerings; wisps of black smoke rise; ritual implements (bamboo skewers, cracked bowls) are rendered with rough mineral pigments; background is a claustrophobic underground passage with wet stone and bone fragments.
mood: dread mixed with grim resolve, an act that seals characters to a corrupted fate.

Negative Prompt:
bright, cheerful, oil painting, cel-shading, 3D render, clean surfaces, modern props, pastel colors, western fantasy, cute, innocent
Params:
--ar 16:9 --stylize 300 --quality high --seed 123456

```


### Prompt for Serene Tower (ツクヨミの静謐塔)

```markdown
# NANOBANANAPRO_PROMPT_SERENE_TOWER_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, breathtaking architectural scene of a towering sacred structure reaching into the clouds, painted entirely in unified Japanese watercolor and mineral pigments on Washi paper.
style: the tower uses disciplined, thin, highly controlled brushwork with restrained bleeding and dignified colors (gofun white, muted gold, ultramarine); surrounding mud-rich earth uses bold expressive bleeding and rough strokes.
details: cracked terrain is stitched by glowing kintsugi lines (star-sand lacquer) that climb toward the tower, emphasizing tension between wild life-noise and ritual stillness.
atmosphere: overcast sky, quiet flat illumination, solemn and ceremonial mood without modern or sci-fi texture.

Negative Prompt:
3D render, porcelain sheen, glossy ceramic, neon sci-fi cityscape, western cathedral, cyberpunk lighting, plastic texture, modern signage, cel-shading
Params:
--ar 9:16 --stylize 250 --quality high --seed 12345


```

---

## 6. 生成チェックリスト（実制作時・更新版）

* **大衆性と造形の担保:** キャラクターの顔面や体型は、しっかり「美麗・魅力的（可愛い/かっこいい）」になっているか。ホラーや奇形になっていないか。
* **天体属性の即読性:** ツクヨミ=月（弧と夜）、アマテラス=太陽（隠れた日輪/コロナ）、カガセオ=星（星図状金継ぎと瞬き）が判別できるか（※カガセオは三貴子ではなく反逆星神）。
* **筆致コントラスト（コアテーマ・最重要）:**
* **人間側は、和紙の繊維感と水彩・岩絵具の予測不能な滲み（ノイズ）**を帯び、アナログな温もりを持っているか。
* 神側は、同じ和紙媒体のまま、**極度に制御された筆運び・最小滲み・格調色（胡粉/金箔/群青/朱）**で「静止した理」を示せているか。


* **因果のアクセント:** 滲む塗りと、儀礼的な**黄金のライン（金継ぎ）**が、異なる筆致階調を繋ぎ止め、高いコントラストを描いているか。
