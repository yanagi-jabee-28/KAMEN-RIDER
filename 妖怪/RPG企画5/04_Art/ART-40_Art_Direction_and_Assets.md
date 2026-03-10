---
uid: [ART-40]
role: art-direction
status: migrating
depends_on:
	- ../01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md
	- ../02_Narrative/NAR-10_Narrative_and_Characters.md
	- ../03_Systems/SYS-20_Game_Systems_and_Flow.md
influences:
	- ../01_Worldbuilding/WRD-99_Archive_and_Changelog.md
---

# [ART-40] Art Direction and Assets

本ドキュメントはArtist/Prompt担当向けの「画風憲法」と「プロンプト集」を一体化した正本である。

## 幕タイトルとビジュアルの関係
本作における五つのサブタイトルは、各幕の色調や光の処理、テクスチャ表現の方向性を決定する指針でもある。例えば第1幕では「白の輪郭」を意識して極端なコントラストと硬質な線を重視し、第2幕では「滲む境界」としてブラシストロークや水彩の滲みを強調する。第3幕の「赫の瞬き」は鮮烈な赤いフレアや粒子飛散を演出するためのマッチポイントであり、第4幕と終幕では金色の脈動や土の温度感をアセット制作時に反映させること。これらは単なる章タイトルではなく、アートディレクションの抽象設計図である。

---

## 1. ビジュアル・フィロソフィー（同一キャンバス原則）

本作のアートワークは「完璧な理への、不完全な熱量による抵抗」を最も直感的に伝えるための言語である。

### 大前提：同一キャンバス原則
- 神も、人も、世界も、すべて**「一枚の生きた和紙（Washi）」**の上に**「岩絵具（Iwa-enogu）」**という同じ画材で描かれる。
- 素材の断絶（神だけ3D・異質テクスチャ）は採用しない。両者の違いは**「筆致のあり方」**のみで表現する。

### 二項対立の視覚表現
- **人（熱量）**: 奔放な滲み・掠れ、岩絵具の粒子感、アースカラー（泥・錆・血）。粗野で温かいアナログの生命感。
- **神（静謐）**: 滲みを極限まで抑えた端正な細線、幾何学的構図、胡粉の白と群青。冷たく美しい絶対秩序。
- **金継ぎ**: 傷を繋ぐ、鋭く光る黄金。両者の境界にのみ介入する、熱量と修復の証。
- **美しい呪いの具現:** 付喪神化が覚醒する瞬間、金継ぎの線が脈打ち赤く輝き、武器自身の「意志」が発動して神の完璧な見切りを裏切る。武器に宿った付喪神の力を視覚化するこの動的エフェクトは、戦闘中のカタルシスを高めるための必須要素である。

---

## 2. スタイルアンカー（共通プロンプト）

複雑な制約を捨て、世界観の表現力とAIの想像力に完全に委ねるシンプルで強力なベースプロンプト。

```text
# 00_STYLE_ANCHOR_LUMINOUS_WASHI_V7

Prompt:
masterpiece, highly detailed, beautifully expressive.
traditional Japanese painting entirely on highly textured, fibrous Washi paper using mineral pigments (Iwa-enogu) and soft ink washes.
The core visual is the breathtaking collision of two distinct brushstrokes: the ultra-refined, perfectly disciplined, and serene lines of the divine, clashing against the rough, scratchy dry-brush strokes, granular textures, and chaotic watercolor bleeding of human passion.
A world of tragic beauty, sorrow, and muddy warmth.

Negative Prompt:
gold lines, lightning, kintsugi on background, 3D render, CGI, glossy, plastic, modern, sci-fi, western medieval, thick oil painting, anime cel-shading, signature, watermark
```

---

## 3. キャラクタービジュアル定義

AIの想像力を最大化するため、構造的な制約を排除し、キャラクターの「美しさ」と「概念」を詩的に伝えるプロンプトを定義。

### ミコト（主人公 / 空の器）
コンセプト: 白いボブと風になびく一本の赤いスカーフ。世界の重責を背負う、中性的で美しい人間の器。

```text
Prompt:
masterpiece, an exquisitely beautiful adventurer with a perfect, androgynous Japanese profile, standing in the wind.
traditional Japanese watercolor on Washi paper, with organic pigment bleeding.
A striking white bob hair and a single, bold red scarf fluttering wildly in the same direction, symbolizing friction and rebellious heat. Wears a simple ancient white tunic and baggy pants.
A solitary figure carrying the weight of a broken world, painted with emotional resonance.
```

#### ミコト（手甲継承版）
```text
Prompt:
masterpiece, an exquisitely beautiful adventurer with a perfect, androgynous Japanese profile.
traditional Japanese watercolor on Washi paper.
White bob hair and a solitary, bold red scarf fluttering in the wind. On the left arm, wearing a sleek, antique black-iron asymmetrical rough gauntlet.
The weight of legendary inheritance rests on this slender human vessel.
```

#### ミコト（三種の神器装備・最終決戦版）
```text
Prompt:
masterpiece, an exquisitely beautiful, androgynous adventurer standing on a scarred battlefield.
traditional Japanese watercolor on Washi paper, contrasting divine stillness with muddy human passion.
Wielding three ancient, repaired relics: a dark iron straight sword mended with subtle golden seams; a solid bronze disc-mirror on the arm; and a heavy necklace of raw jade magatama.
The once-bright red scarf is now a dark, blood-stained muddy red, fluttering in the ash-filled wind. The ultimate mortal who defies the gods.
```

### ウズ（狂騒の踊り子）
コンセプト: 古代の神懸かった奉納舞。しめ縄のような髪と、生命力溢れる笑顔。

```text
Prompt:
masterpiece, a wildly captivating and beautifully fierce female ritual dancer leaping in mid-air.
traditional Japanese watercolor on Washi paper, emphasizing explosive, dynamic pigment splashes and frantic kinetic energy.
Charming, lively face with a fierce smile. Thick twin-tails styled like ancient shimenawa ropes. Dressed in asymmetrical, rough hemp garments. A translucent ribbon swirls around her, melting into the air like raw emotion.
```

### マヒト（隻眼の鉄打ち）
コンセプト: 傷跡こそが強度を証明する、隻眼の美しい屈強な鍛冶師。

```text
Prompt:
masterpiece, a rugged, remarkably handsome one-eyed blacksmith, embodying the toughness of work-hardened steel.
traditional Japanese painting on Washi paper, using heavy, somber dark mineral pigments with scratchy dry-brush textures.
Intense glowing embers and soot smudges evoke the heat of the forge. Bound dark hair, cracked leather apron, gripping a heavy forging hammer. A portrait of masculine resilience and silent warmth.
```

> **2026-03-09 演出追記:** マヒトの鍛造段階を視覚的に区別する。
> - 加入直後: 携行鍛冶具（小型金床、折り畳み火床、煤だらけの布）を背負わせる。
> - 拠点Lv2解禁後: 大金床、火花量、鉄屑の散乱を増やし「禁忌鍛造」の重量感を出す。
> - 野外Lv2解禁後: 野営地背景でも鍛造火花を許可し、拠点との差は規模と光量で表現する。

### タチバナ（反逆の生贄）
コンセプト: 透き通るような白さと、海に濡れたような悲哀を纏う、美しき戦士。

```text
Prompt:
masterpiece, a stunningly beautiful, slender female warrior standing on a rocky shore, exuding luminous and fragile elegance.
traditional Japanese watercolor on Washi paper, with melancholic dry brush strokes of deep ocean blues and sea-greens.
Long straight hair clinging to pale skin as if soaked with seawater. Simple flowing white robe, its hem stained by dark bleeding earth colors, with a subtle accent of blood-red woven into the ties. The beautiful fragility of mortal life.
```

### ワカヒコ（悲観的な狙撃手）
コンセプト: 神の理の体現。完璧に左右対称の美貌と、凍りつくような冷徹さ。

```text
Prompt:
masterpiece, a strikingly beautiful, ethereal, and coldly arrogant youthful male archer in a noble Kyudo stance.
traditional Japanese painting on Washi paper with absolute brush discipline. ZERO chaotic bleeding.
Pale seashell-white skin, sleek silvered hair, and luminous pearl-white ancient court robes. He holds a massive, elegantly curved asymmetrical Japanese longbow. On his back, a quiver showing only sharp, blood-red arrow fletchings. He embodies the terrifying perfection and frozen stillness of divine logic.
```

### スクナ（小さな知恵者）
コンセプト: 子供の姿に宿った、冷笑的で鋭い知性と毒。

```text
Prompt:
masterpiece, a small alchemist boy with a fiercely sharp, intellectual, and cynical adult aura.
traditional Japanese watercolor on Washi paper, stained with toxic, acidic mineral granulation of bruised purples and sickly greens.
Narrowing, cold eyes with dark circles of sleeplessness, projecting arrogant brilliance. Wearing a scarred leather apron and violently dragging a massive ancient stone mortar by a rope.
```

### うかみ（野生と法力の指導者・斥候版）
コンセプト: 大地の過酷さを体現する、渋く野性的な魅力をもつ中年の導き手。

```text
Prompt:
masterpiece, a strikingly handsome, intensely dignified middle-aged male warrior radiating rugged, wild charm.
traditional Japanese painting on Washi paper, using heavy, earthy dry-brush strokes and weathered textures.
Sharp features, a short beard, piercing eyes, and wind-tousled dark hair with silver strands. Wearing a muddy travelers cloak, holding a heavy wooden spear, while his left arm bears a sleek, antique black-iron gauntlet. The seasoned mentor of the savage lands.
```

### うかみ（行者版・遍歴の果て）
```text
Prompt:
masterpiece, an exceptionally handsome, rugged middle-aged male ascetic (Gyoja) radiating profound spiritual weight and stoic gravity.
traditional Japanese painting on Washi paper, dominated by solemn earthy dry-brush with rust and ash-gray tones.
Silver-streaked dark hair, deeply expressive eyes, dressed in heavy, layered dark charcoal robes with thick wooden prayer beads. His left arm is bare, symbolizing the legacy he has passed on.
```

---

## 4. 神・敵ビジュアル定義

### アマテラス（絶望と保存の繭）
```text
Prompt:
masterpiece, a terrifyingly serene and beautiful female deity, Amaterasu, locked in self-imposed absolute isolation.
traditional Japanese painting on Washi paper. Her form is perfectly smooth, painted with pristine, matte seashell-white (Gofun), devoid of chaotic bleeding.
Enveloped in sculptural, multi-layered white ceremonial robes resembling frozen lily petals. She wears a golden sun-braid crown. A brilliant, muted-gold corona radiates outward like an annular solar eclipse, while she remains a tragically beautiful, frozen cocoon of despair.
```

### ツクヨミ（悲哀と永遠の処刑者）
```text
Prompt:
masterpiece, an exceedingly beautiful, flawless male deity, Tsukuyomi, the cold and ruthless executor of eternity.
traditional Japanese painting on Washi paper with razor-sharp, ultra-controlled fine ink lines.
Dressed in stark, origami-like ancient court attire of blinding white, intense ultramarine, and lunar silver. He wields a massive, exquisitely curved crescent-blade naginata. A simple, fine-line silver full-moon halo frames his terrifyingly symmetrical, expressionless face.
```

### スサノオ（泥に塗れた嵐）
```text
Prompt:
masterpiece, an overwhelmingly handsome, fiercely masculine ancient storm god, Susanoo, radiating a wild and tragic aura.
traditional Japanese watercolor on Washi paper, blending pristine divine outlines with chaotic, explosive bleeding of storm-cloud grays, ocean blues, and lightning-gold.
Wild dark hair whipping in a typhoon, adorned with massive magatama. He grips a long dark iron straight sword mended with thick, glowing golden kintsugi. A tragic hero whose divine form erupts into the muddy, passionate heat of a storm.
```

### カガセオ（黄金のバグ／再結晶）
```text
Prompt:
masterpiece, a tragically beautiful, human-like male star deity, Kagaseo, the primal rebellious spark.
traditional Japanese watercolor on Washi paper. A brilliant collision of divine elegance and chaotic, expressive brushstrokes of dark earth, rust, and vermilion.
Massive fissures across his majestic, scarred body are violently stitched together by thick, glowing golden Kintsugi that maps out radiant celestial constellations. One of his eyes blazes with the uncontainable, supernova-like heat of a dying, rebellious star.
```

### 伊邪那岐命（イザナギ／究極の琥珀）
```text
Prompt:
masterpiece, a towering, terrifyingly perfect divine entity, Izanagi, the absolute embodiment of preservation and infinite sorrow.
traditional Japanese painting on Washi paper. Rendered entirely in flawless, unblemished seashell-white and translucent pale gold, like a frozen porcelain shell.
Crucially, a tiny, uncontrollable tear of vivid, chaotic watercolor (vermilion and bruised purple) leaks from a micro-fissure in his flawless surface, belying his suppressed, agonizing grief. A suffocating vision of eternal stasis.
```

> **2026-03-08 企画会議反映:** システム用語の脱SF化に伴い、アートプロンプト内の「UI」「ノイズ」といった現代的メタ表現を和語（神託崩壊、情念の奔流など）へと統合した。
### 澱神・八岐の産土（真エンドボス・怨念融合体）
```text
Prompt:
masterpiece, a colossal, terrifying chimera entity of eight serpentine heads violently erupting from a shattered, pure-white porcelain shell.
traditional Japanese watercolor on Washi paper. A grotesque collision of sterile, perfectly smooth divine surfaces and explosive, raw human karma.
The smooth outer husk forcefully shatters, unleashing wild, chaotic dry-brush strokes and bleeding neon-mineral colors. The heads are a horrific mix of ragged organic tissue, ancient bone, and countless rusted folding swords, all bound together by jagged, glowing golden Kintsugi.
```

### 黄泉醜女（伊邪那美型怨念）
```text
Prompt:
masterpiece, a terrifying female apparition born of rot and obsessive grief out of the underworld.
traditional Japanese watercolor on Washi paper. Explosive, uncontrolled bleeding of acid greens, bruised purples, and ink-black blood.
A pale, gaunt figure draped in a tattered, blood-stained white kimono. Her hair is a tangled mess of earth, dead leaves, and bone. Dark roots and clawed fingers emerge from the darkness, her eyes glowing with a cold, otherworldly vermilion light.
```

---

## 5. アイテム・神話的意匠

### 天叢雲剣（素体 / 魂の器）
```text
Prompt:
masterpiece, an incredibly long and narrow ancient Japanese straight sword (Chokuto) floating in a void.
traditional Japanese watercolor on Washi paper. The dark, near-black iron is matte and light-absorbing.
The blade is broken into three distinct segments, yet powerfully fused back together by thick, raised lines of glowing, brilliant golden Kintsugi lacquer that pulse with intense heat. The golden light bleeds softly into the textured paper surface.
```

### 八咫鏡（Yata no Kagami）
```text
Prompt:
masterpiece, a single, newly cast solid bronze disc-mirror resting on raw, textured Washi paper.
traditional Japanese watercolor painting with solemn dry-brush strokes.
The mirror has an intact, uncracked surface, with a warm amber-gold rim transitioning to a dull olive-grey center. Imperfectly polished by human hands, it gleams softly against the fibrous paper.
```

### 八尺瓊勾玉（Yasakani no Magatama）
```text
Prompt:
masterpiece, a single loop necklace made of large, beautifully rough-carved magatama beads resting on raw Washi paper.
traditional Japanese watercolor painting with vivid mineral pigments.
Deep green nephrite jade and dark obsidian, shaped into ancient teardrop forms, strung together on a thick, coarse hemp cord. The stones retain their raw, earthy texture, glowing with a subtle ancient light.
```

### 三種の神器・集合アイコン
```text
Prompt:
masterpiece, a breathtaking still-life composition of three ancient sacred objects on rough, textured Washi paper.
traditional Japanese watercolor painting.
A very long, dark iron straight sword with subtle golden repair seams; a beautiful, solid bronze disc-mirror with a warm amber rim; and a heavy loop of raw green jade and obsidian magatama beads. The items are connected by the exquisite tragedy of their shared history.
```

### 手甲パーツ（The Beat Gauntlet）
> *システム注釈: ゲーム内ではこの手甲は「固定装具」扱いで、装備スロットを圧縮しない特別な存在である。*
```text
Prompt:
masterpiece, a beautifully crafted antique black-iron asymmetrical left gauntlet worn on a ghostly white arm, resting on Washi paper.
traditional Japanese watercolor using ink washes and mineral pigments.
A sleek, elegant armor piece with articulated iron fingers and a subtly hammered texture. A circular bronze disk is bound tightly by a deep indigo braided cord, carrying the weight of ancient legacy.
```

### ワカヒコの天上弓と靭
```text
Prompt:
masterpiece, a breathtaking still-life of a massive, elegantly curved asymmetrical Japanese longbow (Wa-kyu) and a beautiful quiver.
traditional Japanese watercolor on Washi paper.
The bow is flawless white wood with subtle gold seams, strung tautly. Beside it, the quiver displays only the striking, blood-red fletchings of the arrows hidden within. Cold, divine perfection.
```

---

## 6. 環境プロンプト

### 白堊の回廊（ウズとの出会い）

> *システム注釈: 第2幕中盤に配置される意図的な過負荷イベント。完璧な静寂が狂騒で破壊され、敗北感がマヒトへの鍛造動機として宿題となる場所である。*
```text
Prompt:
masterpiece, a suffocating, flawlessly chalk-white celestial stone corridor that has been violently shattered from the inside out by a burst of chaotic energy.
traditional Japanese watercolor on Washi paper.
The perfect, sterile geometry of the divine architecture is ruptured by explosive, chaotic brush strokes of vibrant vermilion and gold, representing a sudden, muddy blast of human passion and noise breaking through calculated silence.
```

### ツクヨミの静謐塔
```text
Prompt:
masterpiece, a towering, terrifyingly serene sacred structure reaching into the clouds.
traditional Japanese watercolor on Washi paper.
The tower is painted with disciplined, cold precision in gofun white and muted gold. Below, the muddy earth below cracks open, stitched together by glowing golden kintsugi lines that attempt to climb the tower's absolute stillness.
```

### 天望の天守（ワカヒコ陣取る廃城）
```text
Prompt:
masterpiece, an ancient, windswept wooden celestial watchtower balancing menacingly on a jagged cliff edge high in the clouds.
traditional Japanese watercolor on Washi paper.
Cold, austere brushwork captures the dizzying height and arrogant divine isolation, looking far down upon a tragic, scarred muddy earth far below.
```

### 黄泉戸喫（ヨモツヘグイ）の儀
```text
Prompt:
masterpiece, a haunting ritual in an underground, dripping cavern, where weary survivors eat glowing, muddy offerings.
traditional Japanese watercolor on Washi paper.
Uncontrolled bleeding of dark greens and black ink clash with sharp gold kintsugi outlines on cracked earthenware bowls. The faces of the living are lit by a grim, supernatural resilience.
```

### 星屑の荒野（カガセオ決戦地）
```text
Prompt:
masterpiece, a haunting, desolate wasteland covered in fine volcanic ash and sharp obsidian.
traditional Japanese watercolor on Washi paper.
A world painted in monochrome sumi-e blacks and ashen grays, violently pierced by countless, fiercely glowing shards of golden stardust and meteorites embedded in the ground like thorns. The landscape tells the epic sorrow of a shattered star.
```

### 無菌の帳（白化神位相）
```text
Prompt:
masterpiece, a battle field swallowed by sterile white curtains, where all warmth and breath are denied.
traditional Japanese painting on Washi paper using restrained gofun-white and pale silver.
No chaotic splashes. The air itself looks filtered and still, as if life is being archived into perfect crystal layers.
Fine geometric lines close in from the horizon, pressing the human figures into silence.
```

### 血の泥沼（澱神位相）
```text
Prompt:
masterpiece, a battlefield transformed into a thick blood-mud swamp of grief and unfinished prayers.
traditional Japanese watercolor on Washi paper with violent bleeding of deep crimson, umber, and black-green.
Footprints collapse into viscous mud, and broken reflections ripple like wounded memory.
Rough dry-brush streaks and mineral granulation should dominate, emphasizing unstable life-force.
```

### 剥落の星屑（特殊敵）
```text
Prompt:
masterpiece, tiny but terrifying stardust entities with mirror-hard skins, about to return to the sky.
traditional Japanese painting on Washi paper.
Each fragment is rendered as a compact crystal seed, with almost no pigment bleeding, surrounded by faint golden dust trails.
They should feel evasive, short-lived, and tragic: pulled upward by irreversible throne-gravity while being violently rejected by the sterile heaven-system.
```

### 理の反射鏡（八咫鏡拡張演出）
```text
Prompt:
masterpiece, a close-up of a bronze sacred mirror reflecting not light alone, but broken divine decree.
traditional Japanese watercolor on Washi paper with subtle kintsugi seams along the mirror edge.
Inside the reflection, fine ink prediction lines fracture and reverse direction, while the outer world remains still.
Keep the scene analog and solemn, avoiding modern interface motifs.
```

---

## 7. UI／万能スタイル変換プロンプト

### UIとシステムのアート方針
本作におけるUIも「静止した神の理（神UI）」と「傷ついた人間の痕跡（人UI）」のコントラストで描かれる。
金継ぎによる補修、和紙のテクスチャ、岩絵具の発色をそのままシステムグラフィックとして適用する。

### 鍛造UI段階表現（Lv0〜Lv3）
- `Lv0`: 泥色の布と砥石のみ。火花はほぼ出さない。
- `Lv1`: 細い金継ぎ線と最小限の火花。修復成功時に細い金粉が走る。
- `Lv2`: 鍛造音・火花・煤の演出を強化。付喪神化時は武器に金継ぎ脈動エフェクトが同期する。
- `Lv3`: 神社背景の祈り粒子と鍛造火花を重ね、神話的錬成の到達点として演出。

### 万能スタイル変換プロンプト（画像入力用）
```text
Prompt:
masterpiece, professional painting on highly textured, fibrous Washi paper using traditional Japanese mineral pigments (Iwa-enogu) and sumi-e ink washes.
A breathtaking translation into traditional Japanese analog art. Replace all modern, 3D, and glossy elements with organic friction-dry-brush strokes. Highlights are unpainted paper or pale gofun-white.
A world defined by the collision of graceful stillness and chaotic, muddy watercolor bleeding, held together by the exquisite tragedy of golden Kintsugi.
```
