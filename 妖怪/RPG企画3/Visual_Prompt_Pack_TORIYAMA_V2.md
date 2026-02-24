# RPG企画3 ビジュアルプロンプト集（TORIYAMA V2）

## 0. 運用方針（古代コンセプト固定）

- 本プロンプト集は `05_Art_and_Visual_Design.md` の世界観制約に従う。
- すべてのキャラクターは「古代神話ファンタジー（縄文/弥生モチーフ）」を優先し、近代服・西洋鎧・SF意匠を排除する。
- 髪型は「悟空系の黒い逆立ちシルエット」を避け、各キャラの役割が一目で分かる個別シルエットを採用する。
- 画風指定はあくまで「90年代JRPGコンセプトアートの文法」を目標にし、キャラ固有性（シルエット、装備、姿勢）で差別化する。

> **注意:** 以下のプロンプトブロックはドキュメント用の例示であり、
> 実際に画像生成AIに入力する際は *コードフェンスや
> "# STYLE_ANCHOR" などのMarkdown記号を含めず*、
> `Prompt:` から始まる説明文のみをコピーしてください。
> 余分なテキストが含まれていると、生成画像に文字が
> 描き込まれる原因になります。

---

## 1. STYLE_ANCHOR（共通）

```markdown
# 00_STYLE_ANCHOR_TORIYAMA_V2
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,
```

---

## 2. 主人公「ミコト」冒険者初期装備（赤スカーフ版）

### Prompt for Mikoto (protagonist)

```markdown
# NANOBANANAPRO_PROMPT_MIKOTO_ADVENTURER_RED
> (For human reference; remove all lines starting with '#' before use)

# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Full body character design of the protagonist "Mikoto" in their first adventurer's outfit.
hairstyle: a perfectly symmetrical, short bob of pure white hair, looking clean but ready for a journey.
costume: A simple, sleeveless martial-arts-style tunic in an off-white color, and comfortable baggy pants. A LONG, FLOWING SCARF of a BOLD RED color is wrapped around their neck, adding a dynamic and heroic element. A thick sash is tied around the waist. They wear simple, flat-soled kung-fu style shoes.
appearance: Their large, expressive eyes now show a newfound determination mixed with their initial curiosity.
pose: Standing on a cliff with the wind blowing their red scarf, creating a dynamic silhouette against the blue sky.
environment: A windy cliff top overlooking a vast landscape, emphasizing their readiness for adventure.

Negative Prompt:
vest, complex armor, modern clothing, uniform, weak posture, goku hairstyle, black spiky saiyan hair

> (Don't include this label in your AI input; it's here for documentation.)

Params:
--ar 2:3 --stylize 350 --quality high --seed 55831
```

---

## 3. 追加キャラクター（髪型調整版）

```markdown

### Prompt for Uzu (ritual shrine dancer, avoid jester/clown imagery)
# NANOBANANAPRO_PROMPT_UZU_TORIYAMA_V2
> (remove comments and headers before using)

# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Full body character design of "Uzu", a ritualistic, wild female dancer inspired by ancient shrine ceremonies (not a circus jester),
hairstyle: a high, flowing ponytail tied with braided hemp cord and a large ribbon reminiscent of kagura stakes, creating a dynamic silhouette that moves with her,
costume: a layered hemp ensemble with Jomon pottery pattern prints, asymmetrical and torn, accented by a GIANT floating hagoromo-like ribbon; bronze magatama bells (kagura suzu) hang at strategic points, evoking primitive ritual,
expression: a confident, mischievous smirk, big expressive eyes full of life, classic Toriyama-style face,
pose: mid-jump in a high-energy dance, arms outstretched, fan in one hand, creating a sense of fun and motion,
environment: simple stone ruins on a grassy field under a bright blue sky, iconic JRPG setting,
visualizing a classic "Dancer/Jester" class character from a Dragon Quest game

Negative Prompt:
sad expression, modern clothing, realistic shading, dark atmosphere, spiky black hair like a saiyan, goku hairstyle, clown outfit, jester hat

Params:
--ar 2:3 --stylize 350 --quality high --seed 44821
```

```markdown

### Prompt for Mahito (one-eyed blacksmith)
# NANOBANANAPRO_PROMPT_MAHITO_TORIYAMA_V2
> (remove comments and headers before using)

# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Full body character design of "Mahito", a powerfully built one-eyed blacksmith,
hairstyle: short, bristly hair, almost a buzz cut, with a thick headband tied around his forehead, emphasizing his practical and tough nature,
physique: very muscular and stocky, with a strong jawline, stylized scar over one eye,
costume: simple and functional blacksmith's gear, leather apron, baggy pants, thick arm guards, all with clean lines and minimal texture,
expression: a stern but reliable look, the focused gaze of a master craftsman,
pose: holding a huge, stylized warhammer over his shoulder with one hand, standing confidently in front of his anvil,
environment: a simple, classic RPG blacksmith shop with a brick forge, clean and iconic,
visualizing a classic "Warrior/Blacksmith" party member from a JRPG

Negative Prompt:
slender body, clean clothes, smiling expression, detailed background, goku hairstyle, long spiky hair

Params:
--ar 3:4 --stylize 360 --quality high --seed 44822
```

```markdown

### Prompt for Tachibana (female warrior)
# NANOBANANAPRO_PROMPT_TACHIBANA_TORIYAMA_V2
> (remove comments and headers before using)

# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Full body character design of "Tachibana", a female warrior with a calm but determined spirit,
hairstyle: long, straight "hime-cut" hair, with blunt bangs and cheek-length sidelocks, giving her a classic, dignified look,
costume: a simple, flowing white robe with a colored sash, suggesting a mysterious past, Toriyama-style simple clothing folds,
appearance: slender but strong,
expression: calm, determined eyes, not overly sad but carrying a hidden strength, a classic stoic anime heroine,
pose: standing defiantly, holding a simple, elegantly designed spear, a determined stance against a strong wind,
environment: a cliff overlooking a stylized, churning sea, rendered with simple, powerful lines,
visualizing a cool and mysterious "Lancer" or "Priestess" character from Dragon Quest

Negative Prompt:
happy smile, overly detailed clothing, realistic water, comedic expression, goku hairstyle, spiky hair

Params:
--ar 2:3 --stylize 320 --quality high --seed 44823
```

```markdown

### Prompt for Wakahiko (archetypal archer)
# NANOBANANAPRO_PROMPT_WAKAHIKO_TORIYAMA_V2
# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Full body character design of "Wakahiko", a cool and handsome archer,
hairstyle: medium-length, silver hair, windswept and shaggy, with some locks falling over his face, reminiscent of a cool rival character like Terry from Dragon Quest VI,
costume: a stylish, simple adventurer's tunic in bold colors, with a long cape,
appearance: a lean and tall archer,
expression: a cool, slightly arrogant smirk, a classic rival-type character,
pose: confidently drawing a large, uniquely shaped fantasy longbow, aiming off-screen,
environment: standing on a large, stylized rock formation, with a few speed lines to indicate action, clear sky background,
visualizing a classic "Archer/Ranger" character, the cool and capable party member

Negative Prompt:
heavy armor, cheerful expression, firearm, cluttered background, goku hairstyle, black spiky saiyan hair

Params:
--ar 3:4 --stylize 340 --quality high --seed 44824
```

```markdown

### Prompt for Sukuna (child sage)
# NANOBANANAPRO_PROMPT_SUKUNA_TORIYAMA_V2
# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Full body character design of "Sukuna", a small, child-like sage,
hairstyle: a simple, short bowl-cut visible under a large, round scholar's cap,
appearance: a very short character with a large head and big, intelligent eyes,
expression: a serious, analytical look, the classic "child genius" trope,
pose: holding up a bubbling potion in a round flask, inspecting it with great focus,
equipment: carries a large, simple leather satchel, stylized alchemical tools,
environment: a clean, simple background suggesting a wizard's lab or a cave, focusing entirely on the character,
visualizing a classic "Sage/Alchemist" character from a JRPG

Negative Prompt:
large muscular body, casting flashy spells, smiling cutely, realistic lab, goku hairstyle, spiky hair

Params:
--ar 4:5 --stylize 300 --quality high --seed 44825
```

```markdown

### Prompt for Ukami (young scout hero)
# NANOBANANAPRO_PROMPT_UKAMI_SCOUT_TORIYAMA_V2
# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Full body character design of "Ukami" in his early form, a wild and adventurous young man,
hairstyle: wild, unkempt shoulder-length dark hair, held back from his face by a simple leather cord tied around his forehead,
physique: strong, lean, and energetic,
costume: simple, sleeveless adventurer's clothes, baggy pants, and martial arts style boots, perfect for a hero starting his journey,
expression: a big, confident, friendly grin, full of excitement for adventure,
pose: running forward with a simple spear in hand, a classic hero's dynamic pose,
environment: a classic Toriyama-style wilderness, grassy plains with a few round trees and distant mountains,
visualizing the archetypal, energetic JRPG hero at the start of his quest

Negative Prompt:
elegant clothing, frail body, fearful expression, city street, goku hairstyle, black spiky saiyan hair

Params:
--ar 2:3 --stylize 360 --quality high --seed 44826
```

```markdown

### Prompt for Ukami (ascetic warrior form)
# NANOBANANAPRO_PROMPT_UKAMI_ASCETIC_TORIYAMA_V2
# STYLE_ANCHOR
masterpiece, best quality, in the style of Akira Toriyama (Dragon Quest, Dragon Ball), 1990s classic JRPG concept art,
bold and confident outlines, clean linework, vibrant colors with sharp cel shading,
dynamic and adventurous fantasy theme, high energy, clear character silhouette,
japanese mythology inspired motifs,
NO photorealism, NO gritty textures, NO painterly blending, NO complex lighting, NO sci-fi,

# PROMPT
Prompt:
Epic full body key visual of "Ukami" in his awakened form, a powerful warrior sage,
hairstyle: his formerly loose hair is now pulled back into a high warrior's topknot, and has changed to a lighter color like white or silver, showing his transformation,
appearance: visibly more muscular and powerful,
costume: a mix of his old clothes and a stylized martial arts gi or ascetic's robes, with a weighted feel like Piccolo's cape,
expression: a sharp, focused, and incredibly powerful gaze, the grin replaced by the calm confidence of a master,
pose: a classic "powering up" stance, feet planted wide, fists clenched, with a stylized energy aura flaring up around him with clean, sharp lines,
environment: a cracked, barren wasteland, suggesting the aftermath of a great battle, iconic DBZ-style background,
visualizing a hero who has completed his training and returned as a top-tier warrior

Negative Prompt:
goofy expression, weak pose, pristine robes, powerless, realistic energy effects, goku hairstyle

Params:
--ar 3:4 --stylize 400 --quality ultra --seed 44827
```

---

## 4. 生成チェックリスト（実制作時）

- 古代感チェック: 麻布/縄/木/土/青銅モチーフが含まれているか。
- 非SFチェック: メカ・発光ガジェット・未来素材が混入していないか。
- シルエットチェック: 黒ベタで見てもキャラが判別できるか。
- 髪型重複チェック: 「黒逆立ちサイヤ人系」の類似が出ていないか。
- 物語整合チェック: 01〜03章で定義した役割・心理と矛盾しないか。
