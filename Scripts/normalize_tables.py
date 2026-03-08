#!/usr/bin/env python3
"""Normalize Markdown tables by trimming spaces around pipes.

Scans all .md files under 妖怪/RPG企画4 and collapses extra spaces around '|'.
Writes modifications in place.
"""
import re
import pathlib

root = pathlib.Path(__file__).parent.parent / "妖怪" / "RPG企画4"
pattern = re.compile(r"\s*\|\s*")  # match pipe with surrounding spaces

# pattern to detect a markdown table separator row (contains only hyphens/colons between pipes)
sep_pattern = re.compile(r"^\s*\|.*\|\s*$")

# helper: convert any hyphen/colon sequence within a separator row to a canonical '---'
def normalize_separator_line(line: str) -> str:
    parts = line.strip().split("|")
    if len(parts) < 3:
        return line
    new_parts = []
    for part in parts:
        p = part.strip()
        if p == "":
            new_parts.append("")
            continue
        if re.fullmatch(r"[:\-]+", p):
            new_parts.append("---")
        else:
            new_parts.append(p)
    return " | ".join(new_parts)

for md in root.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    lines = text.splitlines()
    changed = False
    newlines = []
    for line in lines:
        if "|" in line:
            # normalize spacing around pipes first
            new = re.sub(r"\s*\|\s*", " | ", line)
            # if this looks like a separator row, canonicalize hyphen runs
            if sep_pattern.match(new):
                new2 = normalize_separator_line(new)
                if new2 != new:
                    changed = True
                    new = new2
            if new != line:
                changed = True
            newlines.append(new)
        else:
            newlines.append(line)
    if changed:
        md.write_text("\n".join(newlines), encoding="utf-8")
        print(f"Normalized {md}")
