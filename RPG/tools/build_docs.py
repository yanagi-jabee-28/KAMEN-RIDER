from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader
from pydantic import ValidationError

import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from schema.models import (  # noqa: E402
    BattleRules,
    Characters,
    CoreConstants,
    MaintenanceRules,
    Skills,
    StoryFlags,
)
from validators.consistency import validate_domain_rules  # noqa: E402

DATA_DIR = ROOT / "data"
TEMPLATE_DIR = ROOT / "templates"
OUTPUT_DIR = ROOT / "output"


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_all() -> dict[str, Any]:
    return {
        "core_constants": _load_yaml(DATA_DIR / "core_constants.yaml"),
        "story_flags": _load_yaml(DATA_DIR / "story_flags.yaml"),
        "characters": _load_yaml(DATA_DIR / "characters.yaml"),
        "skills": _load_yaml(DATA_DIR / "skills.yaml"),
        "battle_rules": _load_yaml(DATA_DIR / "battle_rules.yaml"),
        "maintenance_rules": _load_yaml(DATA_DIR / "maintenance_rules.yaml"),
    }


def validate_payload(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        CoreConstants.model_validate(payload["core_constants"])
        StoryFlags.model_validate(payload["story_flags"])
        Characters.model_validate(payload["characters"])
        Skills.model_validate(payload["skills"])
        BattleRules.model_validate(payload["battle_rules"])
        MaintenanceRules.model_validate(payload["maintenance_rules"])
    except ValidationError as exc:
        errors.extend([f"schema: {err['loc']} {err['msg']}" for err in exc.errors()])

    domain_errors, domain_warnings = validate_domain_rules(payload)
    errors.extend(domain_errors)
    warnings.extend(domain_warnings)

    return errors, warnings


def render(payload: dict[str, Any]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=False)

    rendered = {
        "03_Characters_generated.md": env.get_template("characters.md.j2").render(
            characters=payload["characters"]["characters"]
        ),
        "20_Rules_generated.md": env.get_template("rules.md.j2").render(
            flags=payload["story_flags"]["flags"],
            rules=payload["battle_rules"]["rules"],
            maintenance=payload["maintenance_rules"],
        ),
        "30_Variables_generated.md": env.get_template("variables.md.j2").render(
            core=payload["core_constants"],
            skills=payload["skills"]["skills"],
        ),
    }

    for filename, content in rendered.items():
        (OUTPUT_DIR / filename).write_text(content, encoding="utf-8")


def main() -> int:
    payload = load_all()
    errors, warnings = validate_payload(payload)

    report = {
        "errors": errors,
        "warnings": warnings,
    }
    (OUTPUT_DIR / "validation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    if errors:
        print("Validation failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    render(payload)
    print("Build successful. Generated docs in RPG/output/")
    if warnings:
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
