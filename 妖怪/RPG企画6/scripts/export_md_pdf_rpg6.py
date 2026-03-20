from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from tempfile import TemporaryDirectory


DEFAULT_OUTPUT_NAME = "RPG企画6_統合資料.pdf"
DEFAULT_TITLE = "RPG企画6 統合資料"

# Minimal built-in CSS for PDF export to avoid external dependency.
DEFAULT_EMBEDDED_CSS = """
body { font-family: 'Noto Sans JP', 'Arial', sans-serif; line-height: 1.5; }
pre, code { font-family: 'Consolas', 'Courier New', monospace; }
h1, h2, h3, h4, h5, h6 { font-weight: bold; }
table { border-collapse: collapse; }
td, th { border: 1px solid #888; padding: 4px; }
"""

BROWSER_CANDIDATES = [
    shutil.which("msedge"),
    shutil.which("chrome"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="RPG企画6配下のMarkdownを統合し、PDFをRPG企画6フォルダに出力します。"
    )
    parser.add_argument(
        "--output-name",
        default=DEFAULT_OUTPUT_NAME,
        help="出力PDFファイル名（RPG企画6フォルダ内）",
    )
    parser.add_argument(
        "--title",
        default=DEFAULT_TITLE,
        help="PDFタイトル",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="詳細ログを出力します。",
    )
    return parser.parse_args()


def extract_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text.lstrip("\ufeff")

    lines = text.split("\n")
    metadata: dict[str, str] = {}
    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, text.lstrip("\ufeff")

    for line in lines[1:end_index]:
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        metadata[key.strip()] = value.strip().strip("\"'")

    body = "\n".join(lines[end_index + 1 :]).lstrip()
    return metadata, body


def first_heading(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


def normalize_heading_levels(markdown_text: str) -> str:
    return re.sub(r"^(#{1,5})\s", r"#\1 ", markdown_text, flags=re.MULTILINE)


def _anchor_for_relpath(rel_path: str) -> str:
    base = rel_path.replace(".md", "").replace("/", "-").replace("_", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "-", base)
    base = re.sub(r"-+", "-", base).strip("-")
    return f"doc-{base}"


def _rewrite_links_to_internal_anchors(markdown_text: str, current_rel: str, anchor_map: dict[str, str]) -> str:
    current_parts = current_rel.split("/")
    current_dir = "/".join(current_parts[:-1])

    def _replace(match: re.Match[str]) -> str:
        label = match.group(1)
        raw_target = match.group(2).strip()

        if raw_target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        path_only, sep, fragment = raw_target.partition("#")
        if not path_only.lower().endswith(".md"):
            return match.group(0)

        # Resolve relative .md links against current file directory.
        if path_only.startswith("/"):
            normalized = path_only.lstrip("/")
        else:
            joined = f"{current_dir}/{path_only}" if current_dir else path_only
            parts: list[str] = []
            for token in joined.split("/"):
                if token in ("", "."):
                    continue
                if token == "..":
                    if parts:
                        parts.pop()
                    continue
                parts.append(token)
            normalized = "/".join(parts)

        anchor = anchor_map.get(normalized)
        if not anchor:
            return match.group(0)

        return f"[{label}](#{anchor})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _replace, markdown_text)


def collect_markdown_files(project_root: Path, output_stem: str) -> list[Path]:
    readme = project_root / "README.md"
    excluded_names = {
        f"{output_stem}.md",
        f"{output_stem}.html",
        f"{output_stem}.merged.md",
        f"{output_stem}.merged.html",
    }
    excluded_paths = {
        "99_Archive_and_References/REF-00_merged_gemini.md",
    }

    all_md = []
    for path in project_root.rglob("*.md"):
        if not path.is_file():
            continue
        relpath = path.relative_to(project_root).as_posix()
        if path.name in excluded_names or relpath in excluded_paths:
            continue
        all_md.append(path.resolve())

    all_md = sorted(
        set(all_md),
        key=lambda p: (0 if p == readme.resolve() else 1, p.relative_to(project_root).as_posix().lower()),
    )
    if not all_md:
        raise SystemExit("RPG企画6配下でMarkdownファイルを検出できませんでした。")
    return all_md


def _toc_label_for_path(rel_path: str) -> str:
    labels = {
        "README.md": "RPG企画6 ドキュメント入口",
        "00_Welcome_and_Introduction/README.md": "アシブネノミコト 〜天降る御子と、星屑の大地〜",
        "00_Welcome_and_Introduction/WRD-02_Protected_Vocabulary.md": "Protected Vocabulary Hub (Zero-Loss)",
        "01_Story_and_Characters/NAR-10_Narrative_and_Characters.md": "アシブネノミコト 〜天降る御子と、星屑の大地〜 (NAR-10_Narrative_and_Characters)",
        "02_How_to_Play_and_Mechanics/SYS-20_Player_Manual.md": "Player Manual: Systems, World, and Flow",
        "02_How_to_Play_and_Mechanics/SYS-22_Skill_Matrix.md": "[SYS-22] Skill Matrix (Player Facing)",
        "02_How_to_Play_and_Mechanics/SYS-30_Data_and_Logic_Architecture.md": "Data and Logic Architecture",
        "03_Art_and_Graphics/ART-40_Art_Direction_and_Assets.md": "Art Direction and Assets",
        "90_For_Developers/ARC-00_Architecture_and_Governance.md": "Architecture and Governance (Implementation Charter)",
        "90_For_Developers/ARC-01_UID_Registry.md": "UID Registry",
        "90_For_Developers/DEV-10_Gameplay_Logic_Formulas_and_Flags.md": "DEV-10 Gameplay Logic Formulas and Flags",
        "90_For_Developers/DEV-11_Doc_Reference_and_Mapping.md": "DEV-11 Doc Reference and Mapping",
        "90_For_Developers/DEV-12_Art_Production_and_Prompt_Protocol.md": "Art Production and Prompt Protocol",
        "90_For_Developers/DEV-13_Document_Metadata_and_Reading_Order.md": "DEV-13 Document Metadata and Reading Order",
        "99_Archive_and_References/REF-00_merged_gemini.md": "gemini-conversation",
        "99_Archive_and_References/REF-00_References_and_Archive.md": "[REF-00] References and Archive",
        "99_Archive_and_References/REF-50_External_RPG_Reference_Dictionary.md": "External RPG Reference Dictionary (DQ Series)",
    }
    return labels.get(rel_path, rel_path)


def build_merged_markdown(paths: list[Path], title: str, project_root: Path) -> str:
    sections: list[str] = [f"# {title}", "", '<div style="page-break-after: always;"></div>', "", "## 目次", ""]
    cleaned_sections: list[tuple[str, str, Path, str]] = []
    seen_titles: dict[str, int] = {}
    anchor_map: dict[str, str] = {}

    for path in paths:
        rel = path.relative_to(project_root).as_posix()
        anchor_map[rel] = _anchor_for_relpath(rel)

    for path in paths:
        rel = path.relative_to(project_root).as_posix()
        raw_text = path.read_text(encoding="utf-8")
        meta, body = extract_front_matter(raw_text)
        body = _rewrite_links_to_internal_anchors(body.strip(), rel, anchor_map)

        heading = meta.get("title") or first_heading(body, path.stem)
        count = seen_titles.get(heading, 0) + 1
        seen_titles[heading] = count
        if count > 1:
            heading = f"{heading} ({path.stem})"

        cleaned_sections.append((heading, normalize_heading_levels(body), path, rel))

    for index, (_, _, _, rel) in enumerate(cleaned_sections, start=1):
        sections.append(f"{index}. {_toc_label_for_path(rel)}")

    for heading, body, _, rel in cleaned_sections:
        anchor = anchor_map[rel]
        sections.extend(
            [
                "",
                '<div style="page-break-after: always;"></div>',
                "",
                f"<a id=\"{anchor}\"></a>",
                "",
                f"# {heading}",
                "",
                f"> Source: {rel}",
                "",
                body,
            ]
        )

    return "\n".join(sections).strip() + "\n"


def find_browser() -> Path:
    for candidate in BROWSER_CANDIDATES:
        if not candidate:
            continue
        candidate_path = Path(candidate)
        if candidate_path.is_file():
            return candidate_path
    raise SystemExit("EdgeまたはChromeが見つかりませんでした。")


def run_command(command: list[str], cwd: Path, verbose: bool = False) -> None:
    if verbose:
        print(f"[run] {' '.join(command)}")
    start = time.perf_counter()
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    elapsed = time.perf_counter() - start
    print(f"[done] {command[0]} (elapsed: {elapsed:.2f}s)")

    if completed.returncode != 0:
        details = completed.stderr.strip() or completed.stdout.strip() or "詳細不明"
        raise SystemExit(details)


def run_browser_print(command: list[str], cwd: Path, output_pdf: Path, verbose: bool = False) -> None:
    if verbose:
        print(f"[run] {' '.join(command)}")
    start = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        if output_pdf.is_file() and output_pdf.stat().st_size > 0:
            return
        raise SystemExit("ブラウザ印刷がタイムアウトし、PDFを生成できませんでした。")

    elapsed = time.perf_counter() - start
    print(f"[done] {command[0]} (elapsed: {elapsed:.2f}s)")

    if completed.returncode != 0:
        details = completed.stderr.strip() or completed.stdout.strip() or "詳細不明"
        raise SystemExit(details)


def export_pdf(project_root: Path, output_pdf: Path, title: str, verbose: bool = False) -> None:
    output_stem = output_pdf.stem
    input_paths = collect_markdown_files(project_root, output_stem)

    pandoc_path = shutil.which("pandoc")
    if not pandoc_path:
        raise SystemExit("pandoc が見つかりません。PATHを確認してください。")

    browser_path = find_browser()
    css_path = project_root.parent.parent / "Scripts" / "pdf_style.css"
    if not css_path.is_file():
        css_path = None

    merged_markdown = build_merged_markdown(input_paths, title, project_root)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"[info] source markdown files: {len(input_paths)}")
        print(f"[info] output: {output_pdf}")

    with TemporaryDirectory() as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        merged_md_path = temp_dir / "merged.md"
        merged_html_path = temp_dir / "merged.html"

        merged_md_path.write_text(merged_markdown, encoding="utf-8")

        if css_path is None:
            css_path = temp_dir / "pdf_style.css"
            css_path.write_text(DEFAULT_EMBEDDED_CSS, encoding="utf-8")

        pandoc_command = [
            pandoc_path,
            str(merged_md_path),
            "--from",
            "gfm+hard_line_breaks+yaml_metadata_block",
            "--to",
            "html5",
            "--standalone",
            "--toc",
            "--toc-depth=3",
            "--css",
            str(css_path),
            "--metadata",
            f"title={title}",
            "--output",
            str(merged_html_path),
        ]
        run_command(pandoc_command, cwd=project_root.parent.parent, verbose=verbose)

        browser_command = [
            str(browser_path),
            "--headless",
            "--disable-gpu",
            "--allow-file-access-from-files",
            f"--print-to-pdf={output_pdf.resolve()}",
            "--print-to-pdf-no-header",
            merged_html_path.resolve().as_uri(),
        ]
        run_browser_print(browser_command, cwd=project_root.parent.parent, output_pdf=output_pdf, verbose=verbose)

def main() -> None:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    output_pdf = project_root / args.output_name

    start = time.perf_counter()
    export_pdf(project_root, output_pdf, args.title, verbose=args.verbose)
    elapsed = time.perf_counter() - start
    print(f"PDFを出力しました: {output_pdf} (total: {elapsed:.2f}s)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        script_dir = Path(__file__).resolve().parent
        project_root = script_dir.parent
        fallback_pdf = project_root / DEFAULT_OUTPUT_NAME
        if fallback_pdf.is_file() and fallback_pdf.stat().st_size > 0:
            print(f"割り込みを受けましたがPDFは生成済みです: {fallback_pdf}")
            sys.exit(0)
        sys.exit("中断されました。")
