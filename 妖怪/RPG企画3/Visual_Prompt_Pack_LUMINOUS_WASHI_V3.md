# RPG企画3 ビジュアルプロンプト集（LUMINOUS WASHI V3 - Beautiful Bleeding Edition）

## 0. 運用方針（ハイエンドな美しさと「生者の滲み」の共存）

- **AIの「綺麗なイラスト」を肯定しつつ、テクスチャでメタファーを語る。**
- キャラクターの造形（顔立ち、プロポーション）は、現代のメインストリームが好む「最高に美しく/魅力的」な造形を許容する。
- しかし、単なるフラットなセルルックにはさせない。塗り（マチエール）を **「和紙のテクスチャと、予測不可能な水彩・岩絵具の滲み（Bokashi/Bleeding）」** に限定する。
- **人間側（生者のノイズ）:** 美しい造形でありながら、色彩が滲み、和紙の繊維に吸い込まれるようなアナログな温もりと「コントロール不能な揺らぎ」を持たせる。
- **神・天側（無菌の理）:** 滲みの一切ない、工業製品のように滑らかな白磁の彫刻、または完璧な3Dベクターアートの質感を強制する。
- 両者が接する箇所にのみ、**淡い金色のライン**が輝く。

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
(for divine elements): extremely flawless white porcelain sculpture, perfectly smooth ceramic surface, completely inorganic, geometric perfection, modern 3D render feel, zero bleeding, zero texture,
(for shared/magic elements): subtle glowing metallic accents along boundaries,
NO thick impasto, NO oil painting, NO messy mud, NO western horror styles, NO flat cel-shading,
```

---

## 2. 主人公「ミコト」冒険者初期装備（赤スカーフ版）

### Prompt for Mikoto (protagonist)

```markdown
# NANOBANANAPRO_PROMPT_MIKOTO_WASHI
> (remove comments and headers before using)

# PROMPT
Prompt:
masterpiece, exquisitely beautiful facial features, an expressive young adventurer character standing on a windy cliff.
style: traditional Japanese watercolor on textured Washi paper, beautiful chromatic bleeding, translucent mineral pigments.
details (the figure): pure white short bob hair painted with soft, luminous watercolor bleeds. Wearing an off-white sleeveless tunic and baggy pants. A LONG, FLOWING SCARF of a BOLD RED color wraps around the neck, the red pigment bleeding organically into the surrounding paper texture. A thick coarse rope (shimenawa) around the waist.
texture contrast: delicate, glowing accents map across the clothing, contrasting with the soft watercolor washes. The background is a vast, ancient landscape painted with atmospheric ink washes (sumi-e style) and desaturated earth-tone watercolors.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, modern gacha game 3D model, perfectly smooth clothing, western medieval armor, sci-fi
Params:
--ar 2:3 --stylize 250 --quality high --seed 55831
```

---

## 3. 追加キャラクター（和紙・岩絵具仕様）

```markdown
### Prompt for Uzu (ritual shrine dancer)
# NANOBANANAPRO_PROMPT_UZU_WASHI
> (remove comments and headers before using)

# PROMPT
Prompt:
masterpiece, extremely beautiful and mischievous facial features, an energetic female ritual dancer in mid-air.
style: vibrant Japanese watercolor on textured Washi paper, dynamic splashes of color, beautiful unpredictable bleeding.
details: high twin-tails painted with sweeping, soft watercolor strokes. Asymmetrical, multi-layered hemp outfit with Jomon motifs. A giant, translucent ribbon (hagoromo) floats around her, the colors bleeding softly into the background. Bronze magatama bells hang loosely.
mood: ancient high-energy ritual dance. The ruins in the background are suggested with loose, expressive watercolor washes.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, 3D render, modern idol outfit, perfectly clean lines
Params:
--ar 2:3 --stylize 250 --quality high --seed 44821
```

```markdown
### Prompt for Mahito (one-eyed blacksmith)
# NANOBANANAPRO_PROMPT_MAHITO_WASHI
> (remove comments and headers before using)

# PROMPT
Prompt:
masterpiece, handsome but fiercely rugged facial features, a muscular, one-eyed blacksmith.
style: heavy Japanese mineral pigments (Iwa-enogu) on rough Washi paper, strong contrast, somber watercolor bleeding.
details: short, bristly dark hair bound by cloth. Heavily scarred but dignified single eye. Thick, cracked leather apron and baggy pants rendered with deep, earthy watercolor pigments that bleed slightly at the edges. Leaning on an anvil, holding a blunt warhammer. The forge embers are painted as intense, glowing splashes of red and orange pigment soaking into the paper.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, skinny anime boy, perfect flawless skin, modern sci-fi forge
Params:
--ar 3:4 --stylize 250 --quality high --seed 44822
```

```markdown
### Prompt for Tachibana (the sacrificed warrior)
# NANOBANANAPRO_PROMPT_TACHIBANA_WASHI

# PROMPT
Prompt:
masterpiece, stunningly beautiful with a gentle, even cute innocence in her facial features, a slender female warrior standing on a rocky shore.
style: melancholic Japanese watercolor on Washi paper, cold color palette softened by a hint of warmth, soft translucent washes of deep blues and greens.
details: long, straight hair clinging to her as if wet, painted with elegant, flowing ink lines. A flowing white robe stained softly at the hem with dark, bleeding earth colors. She holds a driftwood-like primitive spear. The turbulent ocean behind her is depicted with moody, overlapping watercolor bleeds and sea-green washes, but the overall mood hints at fragile beauty rather than fear.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, cheerful sunny anime, bright pop colors, dry flawless hair
Params:
--ar 2:3 --stylize 250 --quality high --seed 44823
```

```markdown
### Prompt for Wakahiko (the cynical archer)
# NANOBANANAPRO_PROMPT_WAKAHIKO_WASHI

# PROMPT
Prompt:
masterpiece, highly attractive, cynical smirking facial features, a male archer with subtle divine accents.
style: striking contrast on Washi paper.
details: medium-length, silver hair painted softly. His tunic is primarily rendered with organic, slightly bleeding watercolors depicting rough hemp cloth, with a small patch or shoulder piece of flawless porcelain-like texture suggesting divine interference. Subtle metallic accents trace the edge of this detail without bisecting the outfit. He casually holds a massive, asymmetrical mythological Japanese longbow (yumi) painted with loose watercolor strokes.

Negative Prompt:
oil painting, thick impasto, ugly, horror, messy all over, completely symmetrical, modern archery gear, western fantasy ranger
Params:
--ar 3:4 --stylize 250 --quality high --seed 44824
```

```markdown
### Prompt for Sukuna (the child alchemist)
# NANOBANANAPRO_PROMPT_SUKUNA_WASHI

# PROMPT
Prompt:
masterpiece, beautifully detailed with expressive yet natural eyes, a tiny scholar child.
style: rich Japanese mineral pigments on Washi paper, detailed with organic, soft bleeding edges maintaining watercolor warmth.
details: extremely short hair under a woven cap. Hauling a disproportionately massive mortar and pestle rendered with heavy, granulated watercolor washes. A leather satchel bulging with botanical roots. The surrounding paper is splattered elegantly with vibrant, bleeding drops of alchemical ink (crushed minerals and plant juices).

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, modern laboratory, glass beakers, completely clean environment
Params:
--ar 4:5 --stylize 250 --quality high --seed 44825
```

```markdown
### Prompt for Ukami (the wild scout)
# NOTE: AI models often associate "scout" with elven/pointed ears due to fantasy bias.  We explicitly enforce round human ears below and include this comment to remind future editors.
# NANOBANANAPRO_PROMPT_UKAMI_WASHI

# PROMPT
Prompt:
masterpiece, fiercely handsome yet fully human facial features, a highly agile, tanned male scout character – unmistakably Japanese with regular rounded human ears (no pointiness at all) and no animalistic traits.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: wild, flowing dark hair held by a frayed rope. Deeply tanned, lean, and highly muscular physique painted with warm, organic watercolor washes. Primitive clothing of hide, bone, and rope. Standing in a ready stance with a confident grin, holding a stone-tipped spear. The primordial forest background is created with deep, overlapping washes of green and brown ink.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, sophisticated weapons, perfectly neat hair, pointed ears, elven features, animal ears, exaggerated anime ears, "ears must be rounded human" (affirmative restriction)
Params:
--ar 2:3 --stylize 250 --quality high --seed 44826


### Prompt for Ukami (the ascetic 行者 variant)
# NANOBANANAPRO_PROMPT_UKAMI_GYOJA_WASHI

# PROMPT
Prompt:
masterpiece, fiercely handsome yet fully human facial features, a solemn male ascetic (行者) with tanned skin and regular rounded ears. He is dressed in weathered saffron robes and has prayer beads around his neck, carrying a wooden staff stamped with sacred symbols and topped with a traditional shakujo ringed staff. His pose is meditative but alert, standing amidst a primordial forest background rendered with deep, overlapping washes of green and brown ink.
style: dynamic Japanese watercolor and ink on Washi paper, fast brushstrokes, beautiful earthy pigment bleeding.
details: long, flowing dark hair tied back with a frayed rope, lean muscular build painted with warm, organic watercolor washes. Robes and simple sandals show signs of wear from pilgrimage. The environment remains the same primordial forest.

Negative Prompt:
oil painting, thick impasto, ugly, horror, flat cel-shading, clean modern clothes, sophisticated weapons, perfectly neat hair, pointed ears, elven features, animal ears, exaggerated anime ears, "ears must be rounded human" (affirmative restriction)
Params:
--ar 2:3 --stylize 250 --quality high --seed 44826
```

---

## 4. 神の眷属（白化神）の描画例

※ 天側のシステムや敵対存在を描画する場合は、人間側（滲み・和紙）の対極である「無機質・幾何学・ベクター/3D」の質感を強制します。顔立ちの美しさという概念すら超越した、完全な対称物です。

```markdown
### Prompt for Hakka-shin (Divine Emissary)
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

---

## 5. 生成チェックリスト（実制作時）

- **大衆性と造形の担保:** キャラクターの顔面や体型は、しっかり「美麗・魅力的（可愛い/かっこいい）」になっているか。ホラーや奇形になっていないか。
- **テクスチャコントラスト（コアテーマ）:** 
  - 人間側は、デジタルな「セル塗り」ではなく、「和紙の繊維感」と「水彩・岩絵具の予測不能な滲み（ノイズ）」を帯びているか。
  - 神側は、一切の滲みがない「ツルツルに磨き上げられた無菌の白磁・3DCG感」が出ているか。
- **因果のアクセント:** 滲む塗りと、無機質な**黄金のライン**が高いコントラストを描いているか。
