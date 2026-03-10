from pathlib import Path
import json

# list of markdowns to import
MD_FILES = [
    "妖怪/RPG企画4/00_Core_Vision_and_Theme.md",
    "妖怪/RPG企画4/10_Narrative_and_Characters.md",
    "妖怪/RPG企画4/20_Game_Systems_and_Flow.md",
    "妖怪/RPG企画4/30_Data_and_Logic_Architecture.md",
    "妖怪/RPG企画4/40_Art_Direction_and_Assets.md",
    "妖怪/RPG企画4/50_Reference_DQ_Master_Data.md",
    "妖怪/RPG企画4/99_Archive_and_Changelog.md",
]

ROOT = Path("c:/Users/kaito/Documents/GitHub/KAMEN-RIDER")
OUTPUT = ROOT / "RPG" / "data" / "md_texts.json"

def main():
    data = {}
    for rel in MD_FILES:
        path = ROOT / rel
        if path.exists():
            data[rel] = path.read_text(encoding="utf-8")
        else:
            data[rel] = ""  # missing
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Imported {len(data)} markdowns into {OUTPUT}")

if __name__ == "__main__":
    main()
