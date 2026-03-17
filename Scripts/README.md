# Scripts Dictionary

This folder contains utility scripts for the KAMEN-RIDER project.

## Scripts Overview

### [merge_md.py](./merge_md.py)
A tool to merge multiple Markdown files into a single document.
- **Usage (GUI):** Run without arguments to open a file picker.
  ```powershell
  python Scripts/merge_md.py
  ```
- **Usage (CLI):**
  ```powershell
  python Scripts/merge_md.py -o merged.md input1.md input2.md
  ```

### [export_md_pdf.py](./export_md_pdf.py)
Markdownファイル群を1本のPDFに書き出します。
- **Function:** YAML front matterを除去しつつMarkdownを結合し、PandocでHTML化したあと、EdgeまたはChromeのheadless印刷でPDF化します。
- **Default target:** `妖怪/RPG企画5` の正本10ファイルを、設計順そのままで統合して `妖怪/RPG企画5/yo-kai-project.pdf` を出力します。
- **Order rule:** 引数でファイルやディレクトリを混在させても、指定順を優先しつつ、重複ファイルは先に現れたものを採用します。
- **Usage (default set):**
  ```powershell
  python Scripts/export_md_pdf.py
  ```
- **Usage (keep intermediate files):**
  ```powershell
  python Scripts/export_md_pdf.py --keep-temp
  ```
- **Usage (custom files):**
  ```powershell
  python Scripts/export_md_pdf.py -o out.pdf file1.md file2.md file3.md
  ```
- **Prerequisites:** `pandoc` と `Microsoft Edge` または `Google Chrome` がインストール済みであること。

### [update_prompts.py](./update_prompts.py)
Automatically injects anatomical correction and quality-related negative prompts into `Visual_Prompt_Pack_LUMINOUS_WASHI_V3.md`.
- **Function:** Adds tags for `bad anatomy`, `deformed`, etc. to all `Negative Prompt:` blocks.
- **Usage:**
  ```powershell
  python Scripts/update_prompts.py
  ```

### [update_prompts_clutter.py](./update_prompts_clutter.py)
Automatically injects anti-clutter and anti-extra-weapon negative prompts into `Visual_Prompt_Pack_LUMINOUS_WASHI_V3.md`.
- **Function:** Adds tags for `extra weapons`, `random clutter`, etc. to all `Negative Prompt:` blocks.
- **Usage:**
  ```powershell
  python Scripts/update_prompts_clutter.py
  ```

---
> [!NOTE]
> These scripts use absolute paths or relative logic specifically tuned for this repository structure.
