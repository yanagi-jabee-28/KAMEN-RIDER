import os
import argparse
import tkinter as tk
from tkinter import filedialog


def merge_markdown_files(file_paths=None, output_path=None) -> None:
    if file_paths is not None and output_path is not None:
        selected_files = list(file_paths)
        save_path = output_path
    else:
        root = tk.Tk()
        root.withdraw()

        selected_files = filedialog.askopenfilenames(
            title="統合するMarkdownファイルを選択してください",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
        )

        if not selected_files:
            print("ファイルの選択がキャンセルされました。処理を終了します。")
            return

        save_path = filedialog.asksaveasfilename(
            title="結合後の保存先とファイル名を指定してください",
            defaultextension=".md",
            initialfile="merged_document.md",
            filetypes=[("Markdown files", "*.md")],
        )

        if not save_path:
            print("保存先の指定がキャンセルされました。処理を終了します。")
            return

    if not selected_files:
        print("入力ファイルがありません。処理を終了します。")
        return

    missing_files = [
        path for path in selected_files if not os.path.isfile(path)]
    if missing_files:
        print("エラー: 以下のファイルが見つかりません。")
        for path in missing_files:
            print(f"- {path}")
        return

    try:
        with open(save_path, "w", encoding="utf-8") as outfile:
            for index, file_path in enumerate(selected_files):
                filename = os.path.basename(file_path)
                outfile.write(f"## {filename}\n\n")

                with open(file_path, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())

                if index < len(selected_files) - 1:
                    outfile.write("\n\n---\n\n")

        print(f"成功: {len(selected_files)} 個のファイルを '{save_path}' に統合しました。")
    except Exception as error:
        print(f"エラーが発生しました: {error}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Markdownファイルを1つに結合します。引数未指定ならGUIを開きます。"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="出力先Markdownファイルパス（CLIモード時に必須）",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="結合するMarkdownファイル（CLIモード）",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.files:
        if not args.output:
            raise SystemExit("エラー: CLIモードでは -o/--output を指定してください。")
        merge_markdown_files(file_paths=args.files, output_path=args.output)
    else:
        merge_markdown_files()
