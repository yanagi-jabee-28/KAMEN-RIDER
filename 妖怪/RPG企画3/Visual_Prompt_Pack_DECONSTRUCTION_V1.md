# RPG企画3 ビジュアルプロンプト集（DECONSTRUCTION V1）

## 0. 運用方針（ハイブリッド・ディコンストラクション）

- 本プロンプト集は `05_Art_and_Visual_Design.md` の世界観制約に従う。
- すべてのキャラクターは「古代神話ファンタジー（縄文/弥生モチーフ）」を優先し、近代服・西洋鎧・SF意匠を排除する。
- **最大の特徴として、旧来の鳥山明風・セルルック等のアニメ調を完全廃止する。**
- **人間側は「泥絵具・油彩風」**の荒々しく重厚なテクスチャで。
- **神・天側は「白磁・幾何学」**の無機質で滑らかな質感で。
- それらが衝突する境界や修復の痕跡は、**「金継ぎ」の黄金の輝き**で表現する。

> **注意:** 以下のプロンプトブロックはドキュメント用の例示であり、
> 実際に画像生成AIに入力する際は *コードフェンスや
> "# STYLE_ANCHOR" などのMarkdown記号を含めず*、
> `Prompt:` から始まる説明文のみをコピーしてください。
> 余分なテキストが含まれていると、生成画像に文字が
> 描き込まれる原因になります。

---

## 1. STYLE_ANCHOR（共通）

```markdown
# 00_STYLE_ANCHOR_HYBRID_DECONSTRUCTION
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics,
(for human elements): heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, desaturated deep earth colors with crimson accents,
(for divine elements): smooth white porcelain, flawless geometric shapes, mirror-like symmetry, cold metallic reflections, neon blue glow, completely inorganic,
(for magic/combat effects): glowing kintsugi gold lacquer lines bridging or shattering elements,
NO toriyama style, NO cel shading, NO 1990s anime style, NO clean outlines for humans, NO sci-fi greebles, NO western medieval armor,
```

---

## 2. 主人公「ミコト」冒険者初期装備（赤スカーフ版）

### Prompt for Mikoto (protagonist)

```markdown
# NANOBANANAPRO_PROMPT_MIKOTO_ADVENTURER_RED_V3
> (For human reference; remove all lines starting with '#' before use)

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics,
(for human elements): heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, desaturated deep earth colors with crimson accents,
(for divine elements): smooth white porcelain, flawless geometric shapes, mirror-like symmetry, cold metallic reflections, neon blue glow, completely inorganic,
(for magic/combat effects): glowing kintsugi gold lacquer lines bridging or shattering elements,
NO toriyama style, NO cel shading, NO 1990s anime style, NO clean outlines for humans, NO sci-fi greebles, NO western medieval armor,

# PROMPT
Prompt:
Full body character design of the protagonist "Mikoto" in their first adventurer's outfit.
style: human, so apply heavy impasto, thick modeling clay textures, and rough analog strokes.
hairstyle: a short bob of pure white hair, textured like thick white paint strokes.
costume: A simple, sleeveless martial-arts-style tunic in an off-white color, and comfortable baggy pants. A LONG, FLOWING SCARF of a BOLD RED color is wrapped around their neck, painted with thick, dynamic impasto strokes. A thick coarse rope (shimenawa) is tied around the waist. The clothes show subtle but striking signs of being repaired with glowing gold lacquer (Kintsugi). Asymmetrical arm guards made of crude clay and bone.
appearance: Their large, expressive eyes show a newfound determination.
pose: Standing on a cliff with the wind blowing their red scarf, creating a heavy, dynamic silhouette.
environment: A windy cliff top overlooking a vast landscape, painted with heavy, textured earth tones.

Negative Prompt:
anime style, toriyama style, cel shading, clean crisp lines, western armor, medieval clothes, modern clothing, uniform
> (Don't include this label in your AI input; it's here for documentation.)

Params:
--ar 2:3 --stylize 350 --quality high --seed 55831
```

---

## 3. 追加キャラクター（泥絵具仕様へコンバート）

```markdown
### Prompt for Uzu (ritual shrine dancer)
# NANOBANANAPRO_PROMPT_UZU_DECONSTRUCTION
> (remove comments and headers before using)

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, glowing kintsugi details, NO anime style, NO cel shading,

# PROMPT
Prompt:
Full body character design of "Uzu", a ritualistic, wild female dancer inspired by ancient shrine ceremonies,
style: heavy impasto painting, thick clay-like textures, rough, energetic analog strokes.
hairstyle: a high, flowing ponytail tied with braided hemp cord and a large ribbon, rendered with thick, chaotic brushstrokes.
costume: a layered hemp ensemble with Jomon pottery pattern prints, asymmetrical and torn, accented by a GIANT floating hagoromo-like ribbon painted with sweeping impasto marks; bronze magatama bells hang at strategic points.
expression: a confident, mischievous smirk.
pose: mid-jump in a high-energy dance, moving heavy, textured air.
environment: simple stone ruins on a grassy field, painted with broad, earthy strokes.

Negative Prompt:
sad expression, modern clothing, clear anime faces, cel shading, toriyama style, clean outlines, jester hat, clown outfit
Params:
--ar 2:3 --stylize 350 --quality high --seed 44821
```

```markdown
### Prompt for Mahito (one-eyed blacksmith)
# NANOBANANAPRO_PROMPT_MAHITO_DECONSTRUCTION
> (remove comments and headers before using)

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, glowing kintsugi details, NO anime style, NO cel shading,

# PROMPT
Prompt:
Full body character design of "Mahito", a powerfully built one-eyed blacksmith,
style: extremely heavy impasto, looking almost sculpted from actual clay and rust.
hairstyle: short, bristly hair, bound by a thick, rough cloth headband.
physique: very muscular, stocky, with a scarred texture over one eye.
costume: primitive blacksmith's gear, a thick, cracked leather apron, baggy pants, heavy scorch marks and iron slag details.
pose: resting heavily against his anvil, holding a massive, blunt, roughly forged warhammer.
environment: a dark, smoky forge with glowing red embers cutting through the thick, muddy texture of the painting.

Negative Prompt:
clean anime lines, cel shading, slender body, bright colors, sci-fi forge, modern tools
Params:
--ar 3:4 --stylize 360 --quality high --seed 44822
```

```markdown
### Prompt for Tachibana (the sacrificed warrior)
# NANOBANANAPRO_PROMPT_TACHIBANA_DECONSTRUCTION

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, glowing kintsugi details, NO anime style, NO cel shading,

# PROMPT
Prompt:
Full body character design of "Tachibana", a female warrior who survived being drowned as a sacrifice,
style: heavy impasto, thick clay-like textures, colors layered like muddy seawater and dried blood.
hairstyle: long, straight hair that clumps together as if constantly wet or caked with dried clay.
costume: a flowing white robe that is torn, water-stained, and stained with deep earth colors at the hem, tied with a rough sash.
appearance: slender but possessing a terrifying, visceral intensity.
expression: a calm, determined gaze from eyes that have seen the bottom of the sea.
pose: standing defiantly, holding a primitive, driftwood-like spear coated in dried algae and mud.
environment: standing on a rocky shore, the ocean painted in thick, turbulent strokes of dark blues and greens.

Negative Prompt:
happy smile, clean robes, perfectly styled hair, anime style, cel shading, cheerful atmosphere
Params:
--ar 2:3 --stylize 320 --quality high --seed 44823
```

```markdown
### Prompt for Wakahiko (the cynical archer)
# NANOBANANAPRO_PROMPT_WAKAHIKO_DECONSTRUCTION

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, glowing kintsugi details, NO anime style, NO cel shading,

# PROMPT
Prompt:
Full body character design of "Wakahiko", a cynical former divine vanguard,
style: heavy impasto, with hints of his former "divine" white porcelain nature breaking through rough layers of mud and paint.
hairstyle: medium-length, silver hair painted with jagged, thick strokes.
costume: an asymmetrical adventurer's tunic; one side retains a smooth, inorganic geometric design (divine), while the other is heavily textured, crude hemp cloth (human), bridged by glowing kintsugi lines.
expression: a cynical smirk.
pose: carelessly holding a massive, asymmetrical mythological yumi (longbow).
environment: a barren, heavily textured landscape.

Negative Prompt:
anime hair, cel shading, perfectly symmetrical clothing (except for the divine half), modern archery gear
Params:
--ar 3:4 --stylize 340 --quality high --seed 44824
```

```markdown
### Prompt for Sukuna (the child alchemist)
# NANOBANANAPRO_PROMPT_SUKUNA_DECONSTRUCTION

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, glowing kintsugi details, NO anime style, NO cel shading,

# PROMPT
Prompt:
Full body character design of "Sukuna", a very tiny, intense scholar/alchemist,
style: heavy impasto, painted in thick layers like ancient mortar and ground herbs.
hairstyle: extremely short, rough-cut hair under an oversized, crude woven cap.
appearance: a small child with huge, analytically intense eyes, hands stained with dark juices and crushed minerals.
pose: hauling a massive, rough-hewn mortar and pestle, disproportionately large for his size.
equipment: a thick leather satchel bulging with strange, organic roots and crude botanical tools.
environment: surrounded by thick, muddy splatters of crushed alchemical ingredients.

Negative Prompt:
cute anime child, cel shading, clean laboratory equipment, modern glass flasks, perfectly round eyes
Params:
--ar 4:5 --stylize 300 --quality high --seed 44825
```

```markdown
### Prompt for Ukami (the wild scout)
# NANOBANANAPRO_PROMPT_UKAMI_DECONSTRUCTION

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, heavy impasto, thick modeling clay texture, rough organic strokes, asymmetrical, glowing kintsugi details, NO anime style, NO cel shading,

# PROMPT
Prompt:
Full body character design of "Ukami" as a wild scout from an ancestral fishing village,
style: extremely physical, heavy impasto, painted like raw earth and dried blood.
hairstyle: wild, matted dark hair, held back by a frayed rope.
physique: strong, lean, deeply tanned and scarred, painted with visceral, organic strokes.
costume: minimal, primitive clothing made of animal hide, crude bone armor, and thick rope holding it all together.
expression: a fierce, primal grin.
pose: crouching low to the earth like a predator, a crude stone-tipped spear in hand.
environment: deep inside a primordial, heavily textured green forest.

Negative Prompt:
clean clothes, anime style, cel shading, sophisticated weapons, Toriyama face, soft textures
Params:
--ar 2:3 --stylize 360 --quality high --seed 44826
```

---

## 4. 神の眷属（白化神）の描画例

※ 天側のシステムや敵対存在を描画する場合は、真逆のスタイル（白磁・幾何学）を適用します。

```markdown
### Prompt for Hakka-shin (Divine Emissary)
# PROMPT_DIVINE_EMISSARY_DECONSTRUCTION

# STYLE_ANCHOR
masterpiece, best quality, high contrast dual texture art style, deconstructionist fantasy, ancient japanese mythology inspired motifs, Jomon and Yayoi period aesthetics, smooth white porcelain, flawless geometric shapes, mirror-like symmetry, cold metallic reflections, neon blue glow, completely inorganic, NO impasto, NO human textures, NO organic lines,

# PROMPT
Prompt:
Design of a "Hakka-shin", a divine emissary implementing the absolute static order of Heaven.
style: smooth, flawless white porcelain rendering, perfect geometric vector-art feel, utterly sterile.
body: a perfectly symmetrical, humanoid-adjacent shape composed of hovering porcelain shards and mirror-like bronze plates. No facial features, only a cold, glowing neon blue sigil in the center.
pose: suspended in a static, mathematically perfect pose.
environment: a formless void of pure, cold light. No earthy ground.

Negative Prompt:
impasto, dirt, mud, asymmetrical, organic shapes, human faces, blood, rust, analog brushstrokes
Params:
--ar 2:3 --stylize 400 --quality ultra --seed 99911
```

---

## 5. 生成チェックリスト（実制作時）

- **古代感チェック:** 麻布/縄/木/土/青銅モチーフが主体か。SF・西洋ガジェットがないか。
- **テクスチャコントラスト:** 
  - 人間側は「泥・油絵の具の厚塗り感」で描かれているか。アニメ調の主線になっていないか。
  - 神側は「無機質な白磁・鏡面反射」で描かれ、人間側の泥と対比されているか。
- **因果の金継ぎ:** 両者の衝突地点や修復箇所に「発光する金漆（金継ぎ）」が表現できているか。
- **シルエットチェック:** 黒ベタで見てもキャラの特異なパーツが判別できるか。
- **物語整合チェック:** 各キャラが抱える傷跡やトラウマが、生々しい質感を通して伝わってくるか。
