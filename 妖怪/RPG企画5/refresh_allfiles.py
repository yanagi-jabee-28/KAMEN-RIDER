#!/usr/bin/env python3
"""Utility script for updating the copies stored under `ALL-files`.

Run this from inside the `妖怪/RPG企画5/ALL-files` directory:

    python refresh_allfiles.py

The script will copy the latest version of each core markdown document
from the canonical location in the tree and overwrite the file in this
folder.  It is intentionally simple so that it works on any system with
Python installed.
"""

import shutil
from pathlib import Path
import sys

# List of source paths, relative to the root of "妖怪/RPG企画5".
# The destination is <root>/ALL-files, because the script lives one level
# above that directory.
FILES = [
    '00_Governance/ARC-00_Implementation_Charter.md',
    '00_Governance/ARC-01_UID_Registry.md',
    '04_Art/ART-40_Art_Direction_and_Assets.md',
    '02_Narrative/NAR-10_Narrative_and_Characters.md',
    '05_References/REF-50_Reference_DQ_Master_Data.md',
    '03_Systems/SYS-20_Game_Systems_and_Flow.md',
    '03_Systems/SYS-30_Data_and_Logic_Architecture.md',
    '01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md',
    '01_Worldbuilding/WRD-99_Archive_and_Changelog.md',
]


def main():
    here = Path(__file__).resolve().parent
    root = here  # script now lives at the project root
    allfiles_dir = root / 'ALL-files'

    print('Refreshing ALL-files copies...')
    for rel in FILES:
        src = root / rel
        dst = allfiles_dir / Path(rel).name
        if not src.exists():
            print(f'  [!] source missing: {src}')
            continue
        try:
            shutil.copy2(src, dst)
            print(f'  copied: {rel}')
        except Exception as e:
            print(f'  error copying {rel}: {e}')
    print('Done.')


if __name__ == '__main__':
    main()
