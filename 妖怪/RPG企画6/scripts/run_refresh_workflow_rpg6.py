from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PDF_NAME = "RPG企画6_統合資料.pdf"


def run(cmd: list[str], cwd: Path) -> int:
    completed = subprocess.run(cmd, cwd=cwd)
    return completed.returncode


def main(argv: list[str]) -> int:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    export_script = script_dir / "export_md_pdf_rpg6.py"
    refresh_script = script_dir / "refresh_allfiles.py"
    output_pdf = project_root / PDF_NAME

    print("[1/2] Exporting PDF...")
    export_rc = run([sys.executable, str(export_script)], cwd=project_root)
    if export_rc != 0 and not (output_pdf.is_file() and output_pdf.stat().st_size > 0):
        print("PDF export failed. Stop processing.")
        return 1
    if export_rc != 0:
        print("PDF export returned non-zero, but PDF exists. Continue.")

    print("[2/2] Refreshing ALL-files-RPG_6...")
    refresh_rc = run([sys.executable, str(refresh_script), *argv], cwd=project_root)
    if refresh_rc != 0:
        print("Refresh failed.")
        return refresh_rc

    print("Completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
