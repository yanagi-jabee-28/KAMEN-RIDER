from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st
import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.build_docs import load_all, render, validate_payload  # noqa: E402

DATA_FILES = {
    "core_constants": ROOT / "data" / "core_constants.yaml",
    "story_flags": ROOT / "data" / "story_flags.yaml",
    "characters": ROOT / "data" / "characters.yaml",
    "skills": ROOT / "data" / "skills.yaml",
    "battle_rules": ROOT / "data" / "battle_rules.yaml",
    "maintenance_rules": ROOT / "data" / "maintenance_rules.yaml",
}


def save_payload(payload: dict) -> None:
    for key, path in DATA_FILES.items():
        with path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(payload[key], f, sort_keys=False, allow_unicode=True)


st.set_page_config(page_title="RPG企画4 Manager", layout="wide")
st.title("RPG企画4 Management Tool (MVP)")
st.caption("SSOT YAMLを編集し、矛盾チェック後にMarkdownを再生成します。")

if "payload" not in st.session_state:
    st.session_state.payload = load_all()

left, right = st.columns([2, 1])

with left:
    selected = st.selectbox("Edit target", list(DATA_FILES.keys()))
    raw = st.text_area(
        "YAML editor",
        value=yaml.safe_dump(st.session_state.payload[selected], sort_keys=False, allow_unicode=True),
        height=500,
    )

    if st.button("Apply YAML to session"):
        try:
            st.session_state.payload[selected] = yaml.safe_load(raw) or {}
            st.success("Session updated")
        except yaml.YAMLError as exc:
            st.error(f"YAML parse error: {exc}")

with right:
    if st.button("Validate"):
        errors, warnings = validate_payload(st.session_state.payload)
        if errors:
            st.error("Validation errors")
            for e in errors:
                st.write(f"- {e}")
        else:
            st.success("Validation passed")
        if warnings:
            st.warning("Warnings")
            for w in warnings:
                st.write(f"- {w}")

    if st.button("Save + Generate"):
        errors, warnings = validate_payload(st.session_state.payload)
        if errors:
            st.error("Cannot save: fix validation errors first.")
            for e in errors:
                st.write(f"- {e}")
        else:
            save_payload(st.session_state.payload)
            render(st.session_state.payload)
            st.success("Saved and generated files into RPG/output/")
            if warnings:
                for w in warnings:
                    st.write(f"- {w}")

    if st.button("Reload from disk"):
        st.session_state.payload = load_all()
        st.info("Reloaded")
