from __future__ import annotations

from typing import Any


def _flag_map(data: dict[str, Any]) -> dict[str, bool]:
    return {item["id"]: bool(item["enabled"]) for item in data.get("flags", [])}


def validate_domain_rules(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    flags = _flag_map(payload["story_flags"])
    characters = payload["characters"].get("characters", [])
    skills = payload["skills"].get("skills", [])
    battle_rules = payload["battle_rules"]

    # Timeline rule: field lv2 must not unlock before Mahito joins.
    if flags.get("flag_mahito_field_lv2_unlocked") and not flags.get("flag_mahito_joined_act2"):
        errors.append("flag_mahito_field_lv2_unlocked requires flag_mahito_joined_act2=true")

    # Character domain rule: Ukami cannot operate in ground domain.
    for c in characters:
        if c["id"] == "char_ukami" and "ground" in c.get("domains", []):
            errors.append("char_ukami must not include ground domain")

    # Reference rule: skill owner must exist in characters.
    character_ids = {c["id"] for c in characters}
    for s in skills:
        if s["owner_id"] not in character_ids:
            errors.append(f"skill owner_id not found: {s['id']} -> {s['owner_id']}")

    # Legacy terminology should remain in archive only.
    for term in battle_rules.get("legacy_terms", []):
        warnings.append(f"Legacy term tracked (archive-only): {term}")

    return errors, warnings
