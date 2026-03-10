from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output"


def load_yaml_like(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    # attempt native yaml
    try:
        import yaml

        return yaml.safe_load(text) or {}
    except Exception:
        # naive conversion: quote keys
        text2 = re.sub(r'^([ \t]*)([A-Za-z0-9_]+):', r"\1\"\2\":", text, flags=re.M)
        # replace single quotes with double for safety
        text2 = text2.replace("'", '"')
        try:
            return json.loads(text2)
        except Exception as e:
            raise RuntimeError(f"failed naive yaml parse {path}: {e}")


def load_all() -> dict[str, Any]:
    data = {}
    for base in [
        "core_constants",
        "story_flags",
        "characters",
        "skills",
        "battle_rules",
        "maintenance_rules",
    ]:
        json_path = DATA_DIR / f"{base}.json"
        yaml_path = DATA_DIR / f"{base}.yaml"
        if json_path.exists():
            with json_path.open("r", encoding="utf-8") as f:
                data[base] = json.load(f)
        elif yaml_path.exists():
            data[base] = load_yaml_like(yaml_path)
        else:
            data[base] = {}
    return data


def validate_simple(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    flags = {f["id"]: f.get("enabled") for f in payload.get("story_flags", {}).get("flags", [])}
    chars = payload.get("characters", {}).get("characters", [])
    skills = payload.get("skills", {}).get("skills", [])
    battle_rules = payload.get("battle_rules", {})

    if flags.get("flag_mahito_field_lv2_unlocked") and not flags.get("flag_mahito_joined_act2"):
        errors.append("flag_mahito_field_lv2_unlocked requires flag_mahito_joined_act2=true")
    for c in chars:
        if c.get("id") == "char_ukami" and "ground" in c.get("domains", []):
            errors.append("char_ukami must not include ground domain")
    char_ids = {c.get("id") for c in chars}
    for s in skills:
        if s.get("owner_id") not in char_ids:
            errors.append(f"skill owner_id not found: {s.get('id')} -> {s.get('owner_id')}")
    for term in battle_rules.get("legacy_terms", []):
        warnings.append(f"Legacy term tracked (archive-only): {term}")

    return errors, warnings


def render_simple(payload: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # characters
    lines = ["# Characters (Generated)\n", "| id | name | role | first_act | domains |\n", "| --- | --- | --- | --- | --- |\n"]
    for c in payload.get("characters", {}).get("characters", []):
        lines.append(f"| {c.get('id')} | {c.get('display_name')} | {c.get('role')} | {c.get('first_act')} | {', '.join(c.get('domains', []))} |\n")
    (OUTPUT_DIR / "03_Characters_generated.md").write_text("".join(lines), encoding="utf-8")

    # rules
    lines = ["# Core Rules (Generated)\n\n"]
    lines.append("## Story Flags\n")
    for f in payload.get("story_flags", {}).get("flags", []):
        lines.append(f"- `{f.get('id')}` ({f.get('label')}): {'ON' if f.get('enabled') else 'OFF'}\n")
    lines.append("\n## Boundary States\n")
    for name, rule in payload.get("battle_rules", {}).get("rules", {}).items():
        lines.append(f"- `{name}`: `{rule.get('expression')}`\n  - {rule.get('notes')}\n")
    m = payload.get("maintenance_rules", {})
    lines.append("\n## Maintenance Levels\n")
    camp = m.get("levels", {}).get("camp", {})
    base = m.get("levels", {}).get("base", {})
    lines.append(f"- Camp: default={camp.get('default')} , joined_act2={camp.get('joined_act2')} , field_lv2_unlocked={camp.get('field_lv2_unlocked')}\n")
    lines.append(f"- Base: default={base.get('default')} , joined_act2={base.get('joined_act2')} , shrine_lv3_unlocked={base.get('shrine_lv3_unlocked')}\n")
    (OUTPUT_DIR / "20_Rules_generated.md").write_text("".join(lines), encoding="utf-8")

    # variables
    core = payload.get("core_constants", {})
    sks = payload.get("skills", {}).get("skills", [])
    lines = ["# Variables and Skills (Generated)\n\n"]
    lines.append("## Core Resources\n")
    res = core.get("resources", {})
    lines.append(f"- `MaxKakkon`: {res.get('max_kakkon')}\n")
    lines.append(f"- `MaxJonetsu`: {res.get('max_jonetsu')}\n")
    lines.append(f"- `CostMult`: {res.get('cost_mult_min')} - {res.get('cost_mult_max')}\n\n")
    lines.append("## Skills\n| id | name | owner | kakkon | jonetsu | durability |\n| --- | --- | --- | --- | --- | --- |\n")
    for s in sks:
        lines.append(f"| {s.get('id')} | {s.get('display_name')} | {s.get('owner_id')} | {s.get('cost_kakkon')} | {s.get('cost_jonetsu')} | {s.get('durability_cost')} |\n")
    (OUTPUT_DIR / "30_Variables_generated.md").write_text("".join(lines), encoding="utf-8")


def main() -> int:
    payload = load_all()
    errors, warnings = validate_simple(payload)
    report = {"errors": errors, "warnings": warnings}
    (OUTPUT_DIR / "validation_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1
    render_simple(payload)
    print("Build successful. Generated docs in RPG/output/")
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f"- {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())