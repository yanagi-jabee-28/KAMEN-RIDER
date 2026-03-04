# RPG企画3 ビジュアルプロンプト集（LUMINOUS WASHI V4 - Friction & Kasure Edition - Revised）

## 0. 運用方針（ハイエンドな美しさと「生者の滲み」の共存、および世界観の統一）

* **AIの「綺麗なイラスト」を肯定しつつ、テクスチャでメタファーを語る。**
* **ロール対応:** キャラデザインは画面上の配置だけでなく、それぞれのRPGロール（リレイヤー、ヴァンガード・ガイド、トリックスターなど）を視覚的に伝えることにも配慮する。
* キャラクターの造形（顔立ち、プロポーション）は、現代のメインストリームが好む「最高に美しく/魅力的」な造形を許容する。
* しかし、単なるフラットなセルルックにはさせない。塗り（マチエール）を **「和紙のテクスチャと、筆が引っかかる掠れ・岩絵具の粒子感（Friction/Kasure）」** に限定する。
* **世界観の統一（同一キャンバス原則）**: 神も人も、全て「和紙」という媒体の上に描く。素材の断絶（陶器/3D異物化）は採用しない。
* **武器プロンプト:** 武器は上記素材セット（石・骨・木・麻・和紙・泥）を強調し、破砕・修復（ひび割れ＋金継ぎ）の表現を積極的に指示する。日用品／祭具カテゴリは荒れた掠れと粒子の乱れを許容し、王道武器は機能美と泥汚れを併せ持つ。共有カテゴリを用いる場合は、各キャラ固有の装飾や色調で差別化するようプロンプトに明記する。
* **人間側（生者のノイズ）:** 和紙繊維に筆が引っかかる掠れや岩絵具の粒子感が残る奔放な筆致で「変化し続ける生命」を示す。色は泥・鉄錆・枯葉などの土系を主軸にする。
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
# 00_STYLE_ANCHOR_LUMINOUS_WASHI_V5

# PROMPT
Prompt:
masterpiece, highest quality, highly detailed, exquisitely beautiful character faces,
entirely painted on highly textured, fibrous Washi paper using traditional Japanese mineral pigments (Iwa-enogu) and soft ink washes. visible paper fibers, powdery mineral granulation, organic analog warmth.
The visual core is a breathtaking artistic harmony: ultra-refined, disciplined fine lines for divine elements, intersecting with ROUGH, SCRATCHY dry‑brush strokes and mineral granulation for human elements. Absolutely no smooth, synthetic, or 3D surfaces.
supernatural or magical elements are rendered strictly through traditional analog mediums, sumi-e strokes, kintsugi lacquer, or pigment splashes.

Negative Prompt:
3D render, CGI, glossy surface, plastic, ceramic, porcelain, metallic sheen, flat cel-shading, oil painting, thick impasto, modern digital VFX, western fantasy medieval armor, sci-fi, photorealistic, photography, ugly, deformed, noisy, jpeg artifacts, blurry, low resolution, poorly drawn, signature, watermark
```

---

## 2. 主人公「ミコト」冒険者初期装備（赤スカーフ版）

### ミコト（主人公）

ミコトの「泥臭さと熱量」を、スカーフから溢れ出す赤い岩絵具の激烈な**掠れと粒子の濃度**として定義しました。

```markdown
# NANOBANANAPRO_PROMPT_MIKOTO_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, highest quality, exquisitely beautiful and expressive young male adventurer standing on a windy cliff.
style application: aggressive, DRY BRUSH strokes that catch on the paper fibers focused entirely around his bold red muffler, contrasting with fragile, translucent white textures for his hair and tunic.
details: pure white short bob hair painted with soft, airy watercolor layers. Wearing a worn, off-white sleeveless tunic and baggy pants. A simple, BOLD RED muffler wrapped once around his neck, with exactly two distinct ends trailing in the wind. The red pigment of these two fabric tails **frays and scratches** the surrounding paper texture, symbolizing his inner heat and human friction. A thick coarse hemp rope (shimenawa) binds his waist. His physical form expresses a fragile yet profoundly beautiful mortal existence.
texture: natural, matte cloth textures defined entirely by paper fiber and raw pigment.
background: a vast, ancient landscape suggested through atmospheric, desaturated earth-tone ink washes.

Negative Prompt:
3D model, perfectly smooth clothing, porcelain skin, glossy surface, plastic texture, western medieval armor, sci-fi, regal, emperor, divine ruler, god, metallic ornaments, three ends, multiple tails, multiple scarves, extra fabric, tangled drapery, tentacle-like fabric, oil painting, thick impasto, ugly, flat cel-shading, signature, watermark
Params:
--ar 2:3 --stylize 250 --quality high --seed 55831
```

---

## 3. 追加キャラクター（和紙・岩絵具仕様）

### Uzu（踊り子）

「可愛い」と「古代の荒々しさ」の衝突を避け、躍動感あふれる爆発的な筆致のエネルギーとして可愛さを表現します。

```markdown
# NANOBANANAPRO_PROMPT_UZU_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, highest quality, extremely captivating and brightly expressive female ritual dancer leaping in mid-air.
style application: explosive, dynamic splashes of vibrant pigment and sweeping, fast brushstrokes that embody primal kinetic energy.
details: exceptionally charming facial features with a lively, fierce smile. High twin-tails painted with airy, sweeping watercolor strokes, **loosely braided like ancient shimenawa ropes**. She wears an asymmetrical, multi-layered rough hemp outfit adorned with bold **Jomon-period clay motifs**. A giant, translucent ribbon (hagoromo) aggressively swirls around her, its colors melting softly into the air. Chunky, unpolished bronze magatama bells swing wildly.
texture: skin rendered with warm, natural washes revealing the paper grain, emphasizing vital human warmth.
background: ancient ruins implied by loose, energetic ink washes.

Negative Prompt:
3D render, porcelain skin, smooth ceramic surface, modern idol outfit, perfectly clean lines, synthetic fabric, modern jewelry, oil painting, thick impasto, ugly, horror, flat cel-shading, signature, watermark
Params:
--ar 2:3 --stylize 250 --quality high --seed 44821
```

### Mahito（隻眼の鍛冶師）

鍛冶場の暗闇と、赤熱する火花の「焦げ跡」のような滲みにフォーカスし、男性的で野趣あふれる色気を強調します。

```markdown
# NANOBANANAPRO_PROMPT_MAHITO_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, highest quality, strikingly handsome, rugged, and fiercely masculine one-eyed blacksmith emitting a **powerful, grounded aura**.
style application: heavy, somber application of dark mineral pigments; intense glowing embers SCRATCHED into the dark paper like burn marks with abundant granulation.
details: bristly dark hair bound by a rough cloth. A dignified, heavily scarred single eye. He wears a thick, **cracked leather apron showing signs of repair and scorching**, and baggy pants rendered in deep, earthy tones with rough edges. He stands powerfully: his left hand rests heavily on a massive, realistic iron anvil scarred with hammered pits and rough granulation, while his right hand firmly grips a short-handled heavy iron forging hammer whose face bristles with tiny raised slag particles – the very tools seem to radiate DRY friction. His muscular physique is defined by bold ink washes and the rough texture of the Washi paper.
environment: strictly utilitarian, dark traditional forge (ONLY soot-stained walls and a brick furnace). Vivid red and orange splashes of watercolor depict the heat of the forge.

Negative Prompt:
skinny anime boy, flawless skin, porcelain skin, smooth surface, modern sci-fi forge, crutches, walking stick, statues, porcelain figures, decorative ornaments, oil painting, thick impasto, ugly, horror, flat cel-shading, signature, watermark
Params:
--ar 3:4 --stylize 250 --quality high --seed 44822
```

### タチバナ（贄の戦士）

「可愛さ」よりも「濡れたような透明感」と「悲哀」に全振りし、冷たい海の色が紙に滲み入るような美しさを追求します。

```markdown
# NANOBANANAPRO_PROMPT_TACHIBANA_WASHI_REVISED_V2

# PROMPT
Prompt:
masterpiece, highest quality, stunningly beautiful, slender female warrior standing on a rocky shore, exuding a luminous and fragile elegance.
style application: melancholic, textured DRY BRUSH strokes of deep ocean blues and sea-greens; delicate, fragile ink lines that catch on the paper grain.
details: incredibly pure, gentle facial features. Long, straight hair clinging to her pale skin as if soaked with seawater. She wears a simple, flowing white robe, its hem stained by dark, bleeding earth colors. **A subtle accent of blood-red is woven into the ties of her robe**, hinting at a shared fate. She gently holds **EXACTLY ONE single primitive spear carved from pale driftwood** with both of her hands.
texture: her skin has a translucent watercolor quality, allowing the paper grain to show through, deeply emphasizing her mortal fragility and quiet resolve.
environment: a turbulent, moody ocean behind her, depicted with overlapping, cold DRY‑BRUSH strokes and granular splatter.

Negative Prompt:
two spears, multiple spears, dual wielding, extra poles, twin spears, extra weapons, heavy weapons, metallic armor, dry flawless hair, porcelain skin, smooth ceramic surface, cheerful sunny anime, bright pop colors, oil painting, thick impasto, ugly, horror, flat cel-shading, signature, watermark
Params:
--ar 2:3 --stylize 250 --quality high --seed 44823
```

### ワカヒコ（天の貴人 / Divine Elegance）

泥の対極。一切の乱れを許さない「神の理」を、完璧に統制された筆使いと冷たい胡粉の層で表現します。

```markdown
# NANOBANANAPRO_PROMPT_WAKAHIKO_DIVINE_ELEGANCE_FRICTION_V4

# PROMPT
Prompt:
masterpiece, highest quality, strikingly beautiful, ethereal, and coldly arrogant youthful male archer, Wakahiko, standing in profile in a sharp Kyudo-inspired side-aiming pose.
style application: absolute brush discipline, ZERO chaotic bleeding. The aesthetic is defined by "Friction and Stillness": dry brush calligraphy (Kasure) and visible mineral granulation on textured Washi paper.
details: His skin is unnervingly perfect, rendered with pale gofun pigments that reveal the raw paper tooth but contain absolutely no human warmth or blemishes. His hair is beautifully short, sleek and silvered, emphasizing his austere features. He is frozen in a full draw (Kai), pulling a massive asymmetrical yumi (wa-kyu) to his ear; the bowstring is a razor-sharp, taut line with visible dry-rope friction texture. The white-lacquered wood of the bow is defined by SCRATCHED lines and gold leaf seams that catch light like worn, cold metal. He wears noble Heian-period inspired divine robes (Kariginu) in luminous pearl-white and pale gold; intricate patterns exist with terrifying, non-bleeding precision. A sharp accent of blood-red appears on his arrow fletchings, a cold visual echo of his connection to another.
environment: Takamanohara (celestial plain). A serene landscape suggested by dry, overlapping layers of ink and atmospheric sumi-e haze with minimal moisture.
mood: The suffocating, perfect stillness of divine logic.

Negative Prompt:
watercolor bleeding, soft blending, liquid flow, smudging, dirt, mud, messy brushwork, expressive splashes, human warmth, western fantasy, rough hemp, mechanical gear, modern clothes, vector art, glossy finish, 3D render, plastic, ceramic texture, porcelain skin, oil painting, thick impasto, signature, watermark, multiple bows, extra bows, twin bows, duplicate weapons, front-facing pose, looking at camera, eboshi

Params:
--ar 3:4 --stylize 350 --quality high --seed 44824
```

### スクナ（毒物学者）

```markdown
# NANOBANANAPRO_PROMPT_SUKUNA_WASHI

# PROMPT
Prompt:
masterpiece, highest quality, highly detailed alchemist boy with a sharp, weary, and fiercely intellectual adult aura.
style application: acidic and toxic mineral granulation (bruised purples, sickly acid greens) staining the paper around him, contrasting with his heavy, oppressive dark tools.
facial features: **NOT CUTE, NOT CHERUBIC**. He has sharp, narrowing **"Sanpaku" eyes** with a cold, analytical gaze. Dark circles under his eyes from sleepless research. A **cynical, arrogant sneer** on his lips.
details: He wears a rough woven cap over extremely short hair, and a heavy leather apron scarred by chemical burns. He **violently drags a disproportionately MASSIVE, ancient stone mortar (usu)** by a thick rope over his shoulder; the heavy stone leaves a dark, smudged residue trail on the paper.
texture: sallow, sickly watercolor washes for his skin, heavily emphasizing the rough paper grain.
atmosphere: a dangerous, toxic laboratory environment implied by splatters of poisonous ink.

Negative Prompt:
innocent, adorable, cute, cherubic, blush, happy smile, disney style, ghibli style, soft pastel colors, clean clothes, mascot character, cheerful, round eyes, childish innocence, porcelain skin, smooth surface, huge architecture, oil painting, thick impasto, signature, watermark
Params:
--ar 4:5 --stylize 350 --quality high --seed 44899
```

<!-- Canonical Ukami design: middle-aged (~40) appearance is primary. Youthful 25‑year-old variant is secondary/IF only; ensure AI workflows prioritize mature look and disable younger features for core assets. -->
### ウカミ（斥候・行者 / 共通ベース）

渋みのある中年の魅力を、和紙の「掠れ（Kasure）」と酸化した金属の滲みによって引き出します。

**【斥候（Scout）バージョン】**

### ウカミ（斥候）

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_WASHI_MATURE_REVISED

# PROMPT
Prompt:
masterpiece, highest quality, strikingly handsome, dignified middle-aged male warrior (approx 40 years old) with immense rugged charm.
style application: rough, dry brushstrokes (Kasure) and earthy pigment washes, emphasizing weathered textures and fast, aggressive movement.
details: a ruggedly attractive face, short well-groomed beard and mustache, sharp aquiline nose, piercing wise eyes, and a strong jawline. Fully human features with regular rounded ears. Wind-tousled dark hair with subtle silver strands, tied back. Broad, muscular build defined by warm, organic watercolor washes that highlight the paper grain. He wears worn woven hemp, thick leather armor pieces, and a faded sash. He stands grounded, holding a heavy wooden spear with a broad stone tip.
background: deep, atmospheric sumi-e washes of ancient woodland.

Negative Prompt:
young, boyish, feminine, skinny, immature, weak, clean-shaven, pointed ears, elfen features, animal ears, nudity, porcelain skin, smooth surface, modern clothes, oil painting, thick impasto, ugly, flat cel-shading, signature, watermark
Params:
--ar 2:3 --stylize 300 --quality high --seed 44827
```

### ウカミ（行者）

```markdown
# NANOBANANAPRO_PROMPT_UKAMI_GYOJA_WASHI_MATURE_REVISED

# PROMPT
Prompt:
masterpiece, highest quality, exceptionally handsome, rugged middle-aged male ascetic (Gyoja) radiating stoic spiritual weight.
style application: solemn, heavy earthy DRY‑BRUSH with tones of metallic oxidation (rust and verdigris) rubbing into the paper from his staff.
details: weathered, tanned skin painted with textural watercolor washes. A dignified beard and deep, wise eyes. He wears heavily layered, weathered saffron robes and thick wooden prayer beads. He firmly holds an ancient iron Shakujo (Khakkhara) staff; the top features a single large iron hoop with six smaller, loose metal rings. The metal is painted to look ancient and oxidized. His powerful build reflects decades of harsh physical pilgrimage.
background: a primordial forest rendered with deep, overlapping washes of muted green and brown ink.

Negative Prompt:
youthful, weak, boyish, clean-shaven, shiny metal, golden jewelry, porcelain skin, smooth surface, clean modern clothes, pointed ears, animal ears, oil painting, thick impasto, ugly, horror, flat cel-shading, signature, watermark
Params:
--ar 2:3 --stylize 300 --quality high --seed 44828
```

---

## 4. 天の理（三貴子）の描画例

※ 三貴子を天の理の三面相として扱う。天側のシステムや敵対存在を描画する場合も、人間側と同じ和紙媒体で統一する。差異は「滲みゼロの異物感」ではなく、筆致的な制御精度・構図の整然さ・格調色の運用で表現する。

### Prompt for Amaterasu (system-freeze cocoon)

```markdown
# PROMPT_AMATERASU_FREEZE_WASHI

# PROMPT
Prompt:
Masterpiece, highest quality, a terrifyingly serene yet pulsatingly regal female deity, Amaterasu, locked in self-imposed absolute isolation with an undeniable life‑force that radiates through the stillness.
Style: Traditional Japanese painting on Washi paper. The background features a matte Gofun (seashell white) wash with visible paper fibers and mineral grain. The subject herself is rendered with pristine, flawlessly smooth surfaces and controlled, subtle ink wash elements.
Details: Enveloped in intricate, sculptural multi-layered white ceremonial robes (Heian Kariginu style). The architectural draping mimics frozen lily petals, maintaining a slender, majestic silhouette. Her glossy, straight black silk hair flows beneath a translucent gossamer white veil. She wears an austere, feminine Amaterasu-style crown/kanzashi: a lacquered tiara shaped like a stylized rising sun braid with a tiny cracked gold ring motif. Deep within the immaculate white folds, elusive glimpses of a crimson silk lining cascade like a hidden red sash. A subtle golden luminescence emanates from beneath her skin and robes, trapping sunlight within her form. Her expression is flawlessly beautiful yet frozen in fragile, eternal fear, eyes closed or gazing blankly. The composition evokes an annular solar eclipse in a completely luminous palette: a brilliant, muted-gold corona radiates outward, while the cocooned core is obscured not by shadow, but by an intensely bright, pale overexposure (halation).

Negative Prompt:
chubby proportions, bulky cocoon mass, bright pop colors, plastic sheen, seamless synthetic surfaces, modern elements, high contrast shadows, hard 3D render look, depiction of spiky circles, cartoon sun icons, heavy blackness, dirty fabric, oil painting, thick impasto, ugly, horror, flat cel-shading, signature, watermark
```

### Prompt for Tsukuyomi (sterile execution)

```markdown
# PROMPT_TSUKUYOMI_PURGE_WASHI

# PROMPT
Prompt:
Masterpiece, highest quality, an exceedingly beautiful and flawlessly symmetrical male deity, Tsukuyomi, embodying extreme purification and absolute, ruthless execution, his very form crackling with contained vitality and sovereign menace.
Style: Traditional Japanese watercolor on Washi paper, executed with razor-sharp, ultra-controlled fine ink lines. Background retains visible paper fibers and matte mineral texture, with minimal, tightly controlled bleeding. Palette is strictly restricted to freezing Gofun white, intense ultramarine, and muted lunar silver-gray.
Details: Imposing, towering posture with absolute authority. Adorned in sharp-edged, Origami-like ancient court attire that cascades in architectural, flat planes. He wears a subtle, kabuto-like silver lunar circlet integrated seamlessly into his glossy black hair. Bold streams of deep ultramarine and midnight-blue silk elegantly spill from within the intricate layers of his blinding white robes. His face is terrifyingly symmetrical and expressionless, projecting cold arrogance through downward-gazing Sanpaku eyes. In one hand, he wields a massive, exquisite execution weapon: a breathtaking Naginata featuring an enormous, elegantly curved crescent-like blade. The sweeping lunar arc of the blade perfectly mimics a waning moon. Behind him, a perfectly simple, fine-line silver-platinum full-moon halo frames his figure.

Negative Prompt:
soft pastel tones, weak aura, plain costume, excessive bleeding, sloppy asymmetry, warm cinematic shadows, eboshi, bulky weapons, double-bladed haft, extra weapons, multiple weapons, secondary weapon, sheathed weapon, off-screen weapon, oil painting, thick impasto, horror, flat cel-shading, modern elements, synthetic 3D smoothness, signature, watermark
Params:
--ar 2:3 --stylize 300 --quality high --seed 23456
```

### Prompt for Susanoo (storm-clad bug)
```markdown
# PROMPT_SUSANOO_STORM_WASHI

# PROMPT
Prompt:
masterpiece, highest quality, an overwhelmingly handsome and fiercely masculine ancient storm god, Susanoo, radiating a wild, heroic aura.
style: traditional Japanese watercolor (Iwa-enogu) on fibrous Washi paper. A breathtaking fusion of immaculate divine line-work and the chaotic, dynamic bleeding of storm-cloud grays, deep ocean blues, and flashes of lightning-gold.
details: He has a fiercely attractive, battle-hardened face with piercing eyes that burn with untamed, primal passion. His wild, wind-whipped dark hair merges with aggressive ink washes of stormy skies. He wears ancient, asymmetrical divine garments (rough woven hemp mixed with torn celestial silk) whipping violently in a typhoon, adorned with massive magatama. His legendary **Ame-no-Murakumo sword** is held in a powerful grip—a massive, rugged blade **visibly patched with thick, glowing gold kintsugi, and studded with ancient iron and bone**, symbolizing the first defiant act of human repair. The edges of his form erupt into expressive, splashing watercolor strokes. He embodies the majestic violence of a storm, the very first emotional 'bug' to shatter the silent heavens.
atmosphere: Epic, tempestuous, and undeniably cool.

Negative Prompt:
modern fantasy armor, glossy surface, plastic texture, serene expression, 3D render, excessive literal mud, dirty face, weak, delicate, western mythology, oil painting, thick impasto, ugly, horror, flat cel-shading, signature, watermark
Params:
--ar 2:3 --stylize 300 --quality high --seed 77777
```
---

## 4.5. 黄泉の女陰／他

### Prompt for Yomotsu Shikome (Izanami-entity)

```markdown
# NANOBANANAPRO_PROMPT_YOMOTSU_SHIKOME_WASHI

# PROMPT
Prompt:
masterpiece, highest quality, terrifying female apparition born of rot and obsessive grief, a living amalgam of decayed court garments and writhing maggots, painted on fibrous Washi paper with Japanese watercolor.
style: the figure uses uncontrolled bleeding of acid greens, bruised purples, and black iron inks to suggest corruption; the surrounding void is composed of tight, controlled gold-lined cracks.
details: pale, gaunt face half-covered by tattered white kimono stained with ink-black blood; hair is long and matted with earth, interwoven with bones and dead leaves; multiple pale arms extend like roots, each ending in clawed fingers. Swarms of smaller yōkai (黄泉醜女) circle at her feet, their forms suggested by rapid, expressive ink splatters. Her eyes glow with a cold, otherworldly vermilion light.
mood: absolute dread.

Negative Prompt:
cute, beautiful, clean, serene, pastel colors, western fantasy, mechanical parts, comic style, glossy surfaces, oil painting, flat cel-shading, 3D render, signature, watermark
Params:
--ar 2:3 --stylize 350 --quality high --seed 99999
```

### Prompt for Hakka-shin (Divine Emissary)

```markdown
# PROMPT_DIVINE_EMISSARY_WASHI_REFINED

# PROMPT
Prompt:
masterpiece, highest quality, divine emissary rendered in unified Japanese watercolor on textured Washi paper, austere and perfectly balanced composition.
style: ultra-controlled sumi and Iwa-enogu brushwork, minimal bleeding, razor-clean contour rhythm, high ceremonial stillness.
details: humanoid-adjacent sacred figure with strict symmetry, layered gofun whites, muted gold leaf accents, ultramarine and vermilion glyph motifs, matte mineral surface with visible paper fibers.
environment: sacred empty court at dawn, thin mist, restrained palette, no modern elements.

Negative Prompt:
glossy ceramic, porcelain shards, plastic texture, neon sci-fi, mechanical parts, cyberpunk UI, western fantasy armor, chaotic splatter, cartoon cel-shading, 3D render, oil painting, signature, watermark
Params:
--ar 2:3 --stylize 400 --quality ultra --seed 99911
```

---

## 5. 原初の反逆者（反逆星神カガセオ）の描画例

※ 三貴子とは独立したカテゴリとして、カガセオは「熱暴走のバグ」及び人間側の荒々しさを併せ持った表現をする。

### Prompt for Kagaseo (shattered kintsugi giant)

```markdown
# PROMPT_KAGASEO_KINTSUGI_WASHI

# PROMPT
Prompt:
masterpiece, highest quality, a tragically beautiful and awe-inspiring human-like male deity, Kagaseo, the primal rebellious star.
style: high contrast Japanese watercolor on rough Washi paper. A violent collision of precise divine line-work and chaotic, expressive chromatic bleeding of dark earth tones, rust, and burning vermilion.
details: He has a powerful, god‑like presence with a war‑scarred, strikingly beautiful face and a veteran warrior's bearing. His entire silhouette suggests a walking constellation. He wears tattered ceremonial silks and battered divine armor pieces inset with meteorite fragments. Pale flesh-and-blood surfaces peek through gaps, marred by deep catastrophic fissures and scars. These scars are forcefully stitched by thick, glowing, raised golden Kintsugi lacquer. **Crucially, the kintsugi network must evoke constellation paths and celestial chart geometry, not random cracks**, reinforcing his cosmic motif. Intense inner heat radiates from the cracks as supernova-like flicker bursts, scorching the paper. One eye blazes with uncontainable rebellious thermal energy, like a dying star. His body itself is a map of the heavens.

Negative Prompt:
rock golem, full-stone monster, robotic, mechanical, non-human body, smooth lines, perfect symmetry, calm palette, serene expressions, minimalist backgrounds, oil painting, flat cel-shading, modern props, signature, watermark
Params:
--ar 2:3 --stylize 300 --quality high --seed 34567
```

### Prompt for Boss Orochi Tsurugizuka (Chimera of Discarded Swords)

```markdown
# PROMPT_OROCHI_TSURUGIZUKA_FRICTION_V7

# PROMPT
Prompt:
masterpiece, highest quality, an absolute mechanical-nightmare entity, **strictly composed of exactly eight (8) separate, isolated clusters of jagged metal rising from a singular central mound**.
**Count Enforcement:** Precisely eight distinct neck-like pillars of steel. Each of the eight (8) pillars ends in a **blade-cluster "head" lacking any biological features**. There are **NO eyes, NO scales, NO flesh, and NO biological faces**. The "mouths" are merely jagged gaps between broken katanas.
**Style Application:** **FRICTION-DRY-BRUSH STYLE (Kasure)**. Zero-bleeding, zero-blending. Painted on **highly textured, raw fibrous Washi paper**. Every stroke is a dry, scratchy line of mineral pigment. Visible paper grain through every layer.
**Material Detail:** Each of the 8 heads is a high-density, **unlubricated friction-grind of thousands of rusted ancient swords, jagged iron shards, and shattered bronze hilts**. The entire structure is violently stitched by **jagged, raised golden Kintsugi lacquer lines** that act as the only structural binding.
**Environment:** A stark, minimalist background of dry sumi-e fog. No extra structures. Only the 8-headed mountain of iron.
**Lighting:** Cold, harsh light catching on the dry edges of the rusted metal, rendered with **mineral granulation** to show the grit and rust.

Negative Prompt:
**biological snake, living eyes, reptile scales, animal teeth, monster flesh, organic skin, biological face, eyes in mouths, looking at camera**, watercolor bleeding, soft blending, liquid flow, smudging, blurry edges, washes, water, excessive shadows, extra heads beyond eight, fewer than eight heads, human shapes, modern technology, sci-fi, shiny chrome, oil painting, 3D render, plastic texture, signature, watermark.

Params:
--ar 16:9 --stylize 450 --quality ultra --seed 88888
```

### Prompt for Remnant Bone (Item Icon)

```markdown
# PROMPT_REMNANT_BONE_ITEM_WASHI

# PROMPT
Prompt:
masterpiece, highest quality, macro shot of a single, grotesque yet beautiful object: the "Remnant Bone" (遺骨) of a destroyed ancient weapon, resting on textured Washi paper.
style application: absolute rejection of watercolor bleeding and soft blending. Painted with heavy, SCRATCHY dry-brush strokes (Kasure) and dense mineral pigments (Iwa-enogu) emphasizing raw friction and material obsession.
details: A jagged, irregular chunk of deeply rusted, scorched iron fused uncontrollably with calcified, bone-like white material. The surface area is scarred with deep gouges. Thick, bulging, violent golden Kintsugi lacquer forcefully binds the disparate materials together, leaking a faint, dying ember-like heat. There is NO life, only the heavy, dry karma of a weapon that refused to disappear.
texture: the fibrous tooth of the Washi paper is highly visible, emphasizing the abrasive, unlubricated friction of the ruined metal.

Negative Prompt:
watercolor bleeding, soft blending, liquid flow, smudging, blurry edges, clean metal, shiny steel, smooth surfaces, perfect geometry, biological flesh, living tissue, 3D render, cel-shading, oil painting, signature, watermark
Params:
--ar 1:1 --stylize 300 --quality high --seed 11111
```

### Prompt for True Ame-no-Murakumo (Awakened Historical Vessel)

```markdown
# PROMPT_TRUE_AME_NO_MURAKUMO_WASHI

# PROMPT
Prompt:
masterpiece, highest quality, a single legendary ancient Japanese straight sword (tsurugi) resting or floating, radiating overwhelming heat and history.
style: traditional Japanese watercolor on Washi paper, striking contrast between the dark, rusted iron of the blade and blinding, raised golden Kintsugi lacquer.
details: The sword is thick, heavily weathered, and scarred by countless historical battles. Its entirety is intricately fractured and reconnected by a beautiful, glowing network of golden Kintsugi. The gold pulses with intense, supernova-like thermal energy. Small splatters of gold lacquer and black ink bleed into the surrounding Washi paper, suggesting a heat so intense it scorches reality. It is the ultimate vessel of human friction and repair.
background: minimal atmospheric sumi-e wash, keeping focus entirely on the weapon's presence.

Negative Prompt:
clean pristine blade, shiny typical katana, modern weapon, western longsword, smooth metal, plastic texture, 3D render, cel-shading, oil painting, character holding sword, human, signature, watermark
Params:
--ar 3:2 --stylize 300 --quality high --seed 77777
```

---

## 6. 環境 / ステージ用プロンプト

### Prompt for Yomotsu Hegui Ritual

```markdown
# NANOBANANAPRO_PROMPT_YOMOTSU_RITUAL_WASHI

# PROMPT
Prompt:
masterpiece, highest quality, a haunting ritual scene where weathered characters eat foul, glowing food in a cavernous, dripping shrine, painted on textured Washi paper in Japanese watercolor.
style: rich uncontrolled bleeding of dark greens, browns, and black inks for rot; contrasting sharp gold kintsugi lines outlining cracked earthenware bowls.
details: weary faces contort with pain and determination as they bite into mud-like offerings; wisps of black smoke rise; ritual implements (bamboo skewers, cracked bowls) are rendered with rough mineral pigments; background is a claustrophobic underground passage with wet stone and bone fragments.
mood: dread mixed with grim resolve, an act that seals characters to a corrupted fate.

Negative Prompt:
bright, cheerful, clean surfaces, modern props, pastel colors, western fantasy, cute, innocent, oil painting, cel-shading, 3D render, signature, watermark
Params:
--ar 16:9 --stylize 300 --quality high --seed 123456
```


### Prompt for Serene Tower (ツクヨミの静謐塔)

```markdown
# NANOBANANAPRO_PROMPT_SERENE_TOWER_WASHI_REVISED

# PROMPT
Prompt:
masterpiece, highest quality, breathtaking architectural scene of a towering sacred structure reaching into the clouds, painted entirely in unified Japanese watercolor and mineral pigments on Washi paper.
style: the tower uses disciplined, thin, highly controlled brushwork with restrained bleeding and dignified colors (gofun white, muted gold, ultramarine); surrounding mud-rich earth uses bold expressive bleeding and rough strokes.
details: cracked terrain is stitched by glowing kintsugi lines (star-sand lacquer) that climb toward the tower, emphasizing tension between wild life-noise and ritual stillness.
atmosphere: overcast sky, quiet flat illumination, solemn and ceremonial mood without modern or sci-fi texture.

Negative Prompt:
porcelain sheen, glossy ceramic, neon sci-fi cityscape, western cathedral, cyberpunk lighting, plastic texture, modern signage, cel-shading, 3D render, oil painting, signature, watermark
Params:
--ar 9:16 --stylize 250 --quality high --seed 12345
```

---

## 7. 生成チェックリスト（実制作時・更新版）

* **大衆性と造形の担保:** キャラクターの顔面や体型は、しっかり「美麗・魅力的（可愛い/かっこいい）」になっているか。ホラーや奇形になっていないか。
* **天体属性の即読性:** ツクヨミ=月（弧と夜）、アマテラス=太陽（隠れた日輪/コロナ）、カガセオ=星（星図状金継ぎと瞬き）が判別できるか（※カガセオは三貴子ではなく反逆星神）。
* **筆致コントラスト（コアテーマ・最重要）:**
* **人間側は、和紙の繊維感と水彩・岩絵具の予測不能な滲み（ノイズ）**を帯び、アナログな温もりを持っているか。
* 神側は、同じ和紙媒体のまま、**極度に制御された筆運び・最小滲み・格調色（胡粉/金箔/群青/朱）**で「静止した理」を示せているか。
* **因果のアクセント:** 滲む塗りと、儀礼的な**黄金のライン（金継ぎ）**が、異なる筆致階調を繋ぎ止め、高いコントラストを描いているか。
