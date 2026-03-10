# NanoBananaPro ミコト画像生成プロンプト集

以下はNanoBananaProでミコトの画像を生成するための一連のMarkdownコードブロックです。

```markdown
# 00_STYLE_ANCHOR（全プロンプト共通の先頭に付与）
masterpiece, best quality, high detail, mythic fantasy JRPG key visual, japanese mythology inspired,
NO sci-fi, NO mecha, NO nanomachine, NO spaceship, NO cyberpunk,
theme: imperfect human heat vs sterile divine order,
texture keywords: mud, lacquer, rusted iron, cracked ceramic, kintsugi gold seams, wet cloth, ritual rope,
mood: sacred yet gritty, painful but hopeful,
color script: white -> mud red -> lacquer black -> kintsugi gold,
cinematic volumetric lighting, dramatic contrast, painterly realism + anime precision,
authentic emotional expression, physically plausible fabric and materials
```

```markdown
# 01_ミコト 初期形態「白の器」立ち絵
Prompt:
Full body character design of "Mikoto", amnesiac second Ashibune vessel, androgynous young hero,
pure white asymmetry-free ceremonial outfit, smooth unblemished porcelain-like armor plates over cloth,
minimal ornaments, quiet vacant eyes, expression: learning human emotion for the first time,
standing on tidal shore at dawn, faint shrine remains, wind and sea mist,
pose: upright but uncertain, hands slightly open as if receiving memories,
silhouette clean and iconic for JRPG protagonist, no weapon yet, no party members,
ultra detailed costume seams and subtle water stains hinting future scars

Negative Prompt:
modern clothing, gun, robot parts, sci-fi UI, neon city, comedic style, chibi, excessive fanservice, gore

Params:
--ar 2:3 --stylize 250 --quality high --seed 11821
```

```markdown
# 02_ミコト 継承進行「ノイズの侵食」中間形態
Prompt:
Mikoto mid-evolution full body, originally white vessel now patched by inherited comrades' traces,
non-symmetrical patchwork: burnt iron mark on shoulder, mud-dyed hem, lacquer mending lines,
small ritual talismans and repaired tears, emotional conflict in the eyes,
background: pilgrimage road between village and mountain under red dusk sky,
visualize "kata-shiro carrying others' pain", subtle ghosted afterimages of allies' gestures around Mikoto,
pose: one hand gripping chest, one hand reaching forward, determination mixed with fear,
dynamic cloth motion, weathered textures, grounded material realism

Negative Prompt:
clean perfect armor, futuristic hologram, tech implants, robotic limbs, glossy plastic

Params:
--ar 2:3 --stylize 300 --quality high --seed 11822
```

```markdown
# 03_ミコト 自我崩壊寸前 クローズアップ
Prompt:
Cinematic close-up portrait of Mikoto in identity crisis,
tears and rain mixing with mud, trembling lips, eyes reflecting fragmented memories of companions,
fine cracks spreading on skin like ceramic fracture, black lacquer trying to hold them together,
lighting: harsh side light + deep shadow, intense emotional realism,
background abstract shrine darkness, shallow depth of field, dramatic bokeh of ritual fire embers,
theme: "Are these feelings mine, or borrowed scars?"

Negative Prompt:
smiling expression, cute idol makeup, sci-fi screens, sterile white studio

Params:
--ar 4:5 --stylize 200 --quality high --seed 11823
```

```markdown
# 04_ミコト 覚醒形態「金継ぎの英雄」最重要キーアート
Prompt:
Epic full body key visual of awakened Mikoto,
body and armor visibly cracked then repaired with glowing kintsugi gold seams,
black urushi lacquer + scarred white ceramic + muddy cloth layers,
gold light leaking from fractures, expression fierce and compassionate,
weapon: repaired ritual blade with chipped edge and lacquer-gold mending, not futuristic,
environment: Yomotsu slope opening into eternal twilight sea, storm clouds split by starlight,
symbolism: accepts pain as own history, protects companions behind,
composition: heroic low angle, cape and prayer cords whipping in wind, monumental scale

Negative Prompt:
perfect pristine armor, laser sword, machine motifs, urban neon, comedy tone

Params:
--ar 3:4 --stylize 350 --quality ultra --seed 11824
```

```markdown
# 05_最終決戦ビジュアル「神の予知を砕く瞬間」
Prompt:
Action scene, Mikoto shattering divine prediction,
foreground: Mikoto executes inherited technique with desperate forward step,
midground: cracks tearing through sacred geometric fate-lines in the air like broken glass calligraphy,
background: colossal abstract god presence collapsing into noise and errors,
effects: reverse-flow particles, glitched kanji fragments, gold-lacquer shockwaves, mud splashes,
emotion: imperfect human heat overwhelming sterile omniscience,
high motion clarity, readable anatomy, impactful composition for poster art

Negative Prompt:
mecha boss, firearm muzzle flash, cyberpunk HUD dominance, slapstick expression

Params:
--ar 16:9 --stylize 320 --quality high --seed 11825
```

```markdown
# 06_キャラクター設定資料用（ターンアラウンド）
Prompt:
Character turnaround sheet of Mikoto in three stages:
A) White Vessel (initial), B) Noise-Patched Heir (mid), C) Kintsugi Hero (final),
front/side/back views for each stage, clean neutral background parchment texture,
clear costume construction lines, material callouts (porcelain, cloth, lacquer, iron scorch, mud),
consistent face identity across all stages, proportion chart included,
JRPG production-ready concept sheet style, highly legible and organized

Negative Prompt:
photoreal random fashion, sci-fi armor kits, chaotic background, unreadable layout

Params:
--ar 16:9 --stylize 120 --quality high --seed 11826
```

```markdown
# 07_表情差分シート（感情の継承）
Prompt:
Expression sheet for Mikoto, 12 expressions in grid:
blank curiosity, awkward smile mimic, quiet empathy, suppressed fear, rage at loss, self-denial panic,
resolve, protective tenderness, sorrow, kintsugi awakening ecstasy, battle cry, calm after storm,
same hairstyle and costume neckline, emotional continuity from vessel to human completion,
ink + painterly anime hybrid rendering, production design sheet clarity

Negative Prompt:
comedic deform, meme faces, excessive blush trope, modern emoji icons

Params:
--ar 4:3 --stylize 100 --quality high --seed 11827
```

> 必要なら次に、これをそのまま一括投入できる「コピペ用プロンプト集（短文化版）」も作れます。
