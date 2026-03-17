from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from tempfile import TemporaryDirectory


DEFAULT_FILES = [
    "妖怪/RPG企画5/00_Governance/ARC-00_Implementation_Charter.md",
    "妖怪/RPG企画5/00_Governance/ARC-01_UID_Registry.md",
    "妖怪/RPG企画5/01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md",
    "妖怪/RPG企画5/01_Worldbuilding/WRD-99_Archive_and_Changelog.md",
    "妖怪/RPG企画5/02_Narrative/NAR-10_Narrative_and_Characters.md",
    "妖怪/RPG企画5/03_Systems/SYS-20_Game_Systems_and_Flow.md",
    "妖怪/RPG企画5/03_Systems/SYS-30_Data_and_Logic_Architecture.md",
    "妖怪/RPG企画5/04_Art/ART-40_Art_Direction_and_Assets.md",
    "妖怪/RPG企画5/05_References/REF-50_Reference_DQ_Master_Data.md",
    "妖怪/RPG企画5/README.md",
]

DEFAULT_OUTPUT = "妖怪/RPG企画5/yo-kai-project.pdf"
DOCUMENT_ORDER = {path: index for index, path in enumerate(DEFAULT_FILES)}

DEFAULT_TITLE = "妖怪企画資料統合版"

# Markdownファイルを自動で目次表示するときに用いる日本語名称マップ
# (ファイル名ではなく役割を明示したい場合に使用)
ROLE_NAMES: dict[str, str] = {
    "妖怪/RPG企画5/00_Governance/ARC-00_Implementation_Charter.md": "実装憲章",
    "妖怪/RPG企画5/00_Governance/ARC-01_UID_Registry.md": "UID台帳",
    "妖怪/RPG企画5/01_Worldbuilding/WRD-01_Core_Vision_and_Theme.md": "世界観・コアビジョン",
    "妖怪/RPG企画5/01_Worldbuilding/WRD-99_Archive_and_Changelog.md": "廃棄案と変更履歴",
    "妖怪/RPG企画5/02_Narrative/NAR-10_Narrative_and_Characters.md": "物語・登場人物設計",
    "妖怪/RPG企画5/03_Systems/SYS-20_Game_Systems_and_Flow.md": "ゲームシステムと体験フロー",
    "妖怪/RPG企画5/03_Systems/SYS-30_Data_and_Logic_Architecture.md": "データ・論理アーキテクチャ",
    "妖怪/RPG企画5/04_Art/ART-40_Art_Direction_and_Assets.md": "アート指針・資産",
    "妖怪/RPG企画5/05_References/REF-50_Reference_DQ_Master_Data.md": "外部参照資料（DQデータ）",
    "妖怪/RPG企画5/README.md": "プロジェクト概要",
}

BROWSER_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="複数Markdownを結合し、HTML経由でPDFへ出力します。"
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="対象Markdownまたはディレクトリ。未指定時は妖怪/RPG企画5の既定セットを使用します。",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        help="出力PDFパス",
    )
    parser.add_argument(
        "--title",
        default=DEFAULT_TITLE,
        help="PDFタイトル",
    )
    parser.add_argument(
        "--keep-temp",
        action="store_true",
        help="中間生成したmerged.mdとmerged.htmlをPDF横に残します。",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="実行ログを詳細に出力します。",
    )
    return parser.parse_args()


def extract_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Return (metadata dict, body text) from YAML front matter.

    If no front matter exists, returns ({}, text).
    """

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
        metadata[key.strip()] = value.strip().strip("\"\'")

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


def build_merged_markdown(paths: list[Path], title: str) -> str:
    sections: list[str] = [f"# {title}", "", "## 目次", ""]

    cleaned_sections: list[tuple[str, str, Path]] = []
    seen_titles: dict[str, int] = {}

    for path in paths:
        raw_text = path.read_text(encoding="utf-8")
        meta, body = extract_front_matter(raw_text)
        body = body.strip()

        # 優先順位: YAML title > 役割マップ > 見出し > ファイル名
        relative = path.resolve().relative_to(Path(__file__).resolve().parent.parent).as_posix()
        heading = meta.get("title") or ROLE_NAMES.get(relative) or first_heading(body, path.stem)

        count = seen_titles.get(heading, 0) + 1
        seen_titles[heading] = count
        if count > 1:
            heading = f"{heading} ({path.stem})"

        cleaned_sections.append((heading, normalize_heading_levels(body), path))

    for index, (heading, _, _) in enumerate(cleaned_sections, start=1):
        sections.append(f"{index}. {heading}")

    for heading, body, path in cleaned_sections:
        sections.extend(
            [
                "",
                "<div style=\"page-break-after: always;\"></div>",
                "",
                f"# {heading}",
                "",
                f"> Source: {path.as_posix()}",
                "",
                body,
            ]
        )

    return "\n".join(sections).strip() + "\n"


def resolve_files(raw_files: list[str], repo_root: Path) -> list[Path]:
    requested_items = raw_files or DEFAULT_FILES
    resolved: list[Path] = []
    seen: set[Path] = set()
    missing: list[Path] = []

    for item in requested_items:
        candidate = (repo_root / item).resolve()
        if candidate.is_file():
            if candidate.suffix.lower() == ".md" and candidate not in seen:
                resolved.append(candidate)
                seen.add(candidate)
            continue

        if candidate.is_dir():
            markdown_files = sorted(candidate.rglob("*.md"), key=lambda path: sort_key(path, repo_root))
            for path in markdown_files:
                normalized = path.resolve()
                if normalized not in seen:
                    resolved.append(normalized)
                    seen.add(normalized)
            continue

        missing.append(candidate)

    if missing:
        missing_paths = "\n".join(f"- {path}" for path in missing)
        raise SystemExit(f"入力ファイルが見つかりません。\n{missing_paths}")

    if not resolved:
        raise SystemExit("入力対象からMarkdownファイルを解決できませんでした。")

    return resolved


def sort_key(path: Path, repo_root: Path) -> tuple[int, str, str]:
    relative_path = path.resolve().relative_to(repo_root).as_posix()
    explicit_order = DOCUMENT_ORDER.get(relative_path, len(DOCUMENT_ORDER))
    return (explicit_order, str(path.parent).lower(), path.name.lower())


def find_browser() -> Path:
    for candidate in BROWSER_CANDIDATES:
        if candidate.is_file():
            return candidate
    raise SystemExit(
        "EdgeまたはChromeが見つかりませんでした。既定の候補パスを確認してください。"
    )


def run_command(command: list[str], cwd: Path, verbose: bool = False) -> None:
    # Avoid unicode decode errors on Windows terminals by forcing utf-8 and replacing invalid bytes.
    start = time.perf_counter()
    if verbose:
        print(f"[run] {command}")

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
    # Chromium-based headless print can emit bytes that don't decode under cp932.
    # Using utf-8 + replace prevents crashes while keeping output useful.
    start = time.perf_counter()
    if verbose:
        print(f"[run] {command}")

    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=45,
        )
    except subprocess.TimeoutExpired:
        if output_pdf.is_file() and output_pdf.stat().st_size > 0:
            return
        raise SystemExit("ブラウザ印刷がタイムアウトし、PDFも生成されませんでした。")

    elapsed = time.perf_counter() - start
    print(f"[done] {command[0]} (elapsed: {elapsed:.2f}s)")

    if completed.returncode != 0:
        details = completed.stderr.strip() or completed.stdout.strip() or "詳細不明"
        raise SystemExit(details)


def export_pdf(paths: list[Path], output_pdf: Path, title: str, keep_temp: bool, verbose: bool = False) -> None:
    repo_root = Path(__file__).resolve().parent.parent
    css_path = repo_root / "Scripts" / "pdf_style.css"

    pandoc_path = shutil.which("pandoc")
    if not pandoc_path:
        raise SystemExit("pandoc が見つかりません。PATHを確認してください。")

    browser_path = find_browser()
    merged_markdown = build_merged_markdown(paths, title)

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory() as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        merged_md_path = temp_dir / "merged.md"
        merged_html_path = temp_dir / "merged.html"

        if verbose:
            print(f"[step] write merged markdown to {merged_md_path}")
        merged_md_path.write_text(merged_markdown, encoding="utf-8")

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
        run_command(pandoc_command, cwd=repo_root, verbose=verbose)

        html_uri = merged_html_path.resolve().as_uri()
        browser_command = [
            str(browser_path),
            "--headless",
            "--disable-gpu",
            "--allow-file-access-from-files",
            f"--print-to-pdf={output_pdf.resolve()}",
            "--print-to-pdf-no-header",
            html_uri,
        ]
        if verbose:
            print(f"[step] run browser print (html_uri={html_uri})")
        run_browser_print(browser_command, cwd=repo_root, output_pdf=output_pdf, verbose=verbose)
        if verbose:
            print("[step] browser print finished")

        if keep_temp:
            output_pdf.with_suffix(".md").write_text(merged_markdown, encoding="utf-8")
            output_pdf.with_suffix(".html").write_text(
                merged_html_path.read_text(encoding="utf-8"),
                encoding="utf-8",
            )


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    input_paths = resolve_files(args.files, repo_root)
    output_pdf = (repo_root / args.output).resolve()

    if args.verbose:
        print(f"[info] output: {output_pdf}")
        print(f"[info] input files: {len(input_paths)}")

    start_all = time.perf_counter()
    export_pdf(input_paths, output_pdf, args.title, args.keep_temp, verbose=args.verbose)
    elapsed_all = time.perf_counter() - start_all

    print(f"PDFを出力しました: {output_pdf} (total: {elapsed_all:.2f}s)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("中断されました。")