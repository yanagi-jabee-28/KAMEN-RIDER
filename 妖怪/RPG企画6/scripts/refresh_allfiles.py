#!/usr/bin/env python3
"""Refresh canonical copies under `ALL-files-RPG_6`.

Run this from anywhere; it copies selected files from:
- 妖怪/RPG企画6

into:
- 妖怪/ALL-files-RPG_6

This script is copy-only. PDF generation is handled separately by:
- scripts/export_md_pdf_rpg6.py
"""

from __future__ import annotations

import shutil
from pathlib import Path

PDF_NAME = "RPG企画6_統合資料.pdf"


# List of source paths, relative to the root of "妖怪/RPG企画6".
# The destination is 妖怪/ALL-files-RPG_6, which is one directory above this script.
FILES = [
    "README.md",
    PDF_NAME,
    "00_Welcome_and_Introduction/README.md",
    "00_Welcome_and_Introduction/WRD-02_Protected_Vocabulary.md",
    "01_Story_and_Characters/NAR-10_Narrative_and_Characters.md",
    "02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md",
    "02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix.md",
    "02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md",
    "03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md",
    "90_For_Developers/ARC-00_Architecture_and_Governance.md",
    "90_For_Developers/ARC-01_UID_Registry.md",
    "90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md",
    "90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md",
    "90_For_Developers/DEV-12_Art_Production_and_Prompt_Protocol.md",
    "90_For_Developers/DEV-13_Document_Metadata_and_Reading_Order.md",
    "99_Archive_and_References/REF-00_merged_gemini.md",
    "99_Archive_and_References/REF-00_References_and_Archive.md",
    "99_Archive_and_References/REF-50_External_RPG_Reference_Dictionary.md",
]


def copy_to_allfiles(root: Path) -> None:
    allfiles_dir = root.parent / "ALL-files-RPG_6"
    allfiles_dir.mkdir(parents=True, exist_ok=True)

    print("Refreshing ALL-files-RPG_6 copies...")
    for rel in FILES:
        src = root / rel
        dst = allfiles_dir / Path(rel).name
        if not src.exists():
            print(f"  [!] source missing: {src}")
            continue
        try:
            shutil.copy2(src, dst)
            print(f"  copied: {rel}")
        except Exception as err:
            print(f"  error copying {rel}: {err}")
    print("Done.")


def main() -> None:
    scripts_dir = Path(__file__).resolve().parent
    root = scripts_dir.parent
    copy_to_allfiles(root)


if __name__ == "__main__":
    main()
