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
