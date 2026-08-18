#!/usr/bin/env python3
import json
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ICON_DIR_NAME = "icon"
ICON_DIR = os.path.join(ROOT_DIR, ICON_DIR_NAME)
JSON_FILE = os.path.join(ROOT_DIR, "test_icon.json")
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")
REF_NAME = os.environ.get("GITHUB_REF_NAME", "main")
RAW_BASE = f"https://raw.githubusercontent.com/{REPOSITORY}/{REF_NAME}"

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".ico")


def generate_json() -> None:
    os.makedirs(ICON_DIR, exist_ok=True)
    icons = []
    for filename in sorted(os.listdir(ICON_DIR), key=str.casefold):
        if filename.startswith("."):
            continue
        if filename.lower().endswith(IMAGE_EXTS):
            name, _ext = os.path.splitext(filename)
            rel = f"{ICON_DIR_NAME}/{filename}".replace("\\", "/")
            icons.append({"name": name, "url": f"{RAW_BASE}/{rel}"})

    data = {
        "name": REPOSITORY or "Icon Library",
        "description": "Generated icon index",
        "icons": icons,
    }
    os.makedirs(os.path.dirname(JSON_FILE) or ".", exist_ok=True)
    with open(JSON_FILE, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    generate_json()
