#!/usr/bin/env python3
"""Build a self-contained click-to-edit HTML editor for a hand-drawn photo."""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
from pathlib import Path
from typing import Any


def load_text_items(path: Path) -> list[dict[str, Any]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc

    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and isinstance(data.get("textItems"), list):
        items = data["textItems"]
    else:
        raise SystemExit("Text JSON must be an array or an object containing a textItems array.")

    required = {"text"}
    normalized: list[dict[str, Any]] = []
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict) or not required.issubset(item):
            raise SystemExit(f"Text item #{index} must be an object containing at least a 'text' field.")
        row = dict(item)
        row.setdefault("id", f"note-{index}")
        row.setdefault("x", 0.5)
        row.setdefault("y", 0.5)
        row.setdefault("fontSize", 40)
        row.setdefault("color", "#FFFFFF")
        row.setdefault("outlineColor", "#806994")
        row.setdefault("outlineWidth", 0.8)
        row.setdefault("rotation", 0)
        row.setdefault("maxWidth", 0.36)
        row.setdefault("fontFamily", "hand-cn")
        normalized.append(row)
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Embed a background image and editable handwritten text into editor-template.html."
    )
    parser.add_argument("--image", required=True, type=Path, help="Background image with no newly-added diary text")
    parser.add_argument("--texts", required=True, type=Path, help="JSON array or object with textItems")
    parser.add_argument("--output", required=True, type=Path, help="Output self-contained HTML path")
    parser.add_argument(
        "--template", type=Path,
        default=Path(__file__).with_name("editor-template.html"),
        help="Editor HTML template (defaults to editor-template.html next to this script)",
    )
    parser.add_argument("--alt", default="Pastel hand-drawn photo artwork", help="Accessible image description")
    args = parser.parse_args()

    for path in (args.image, args.texts, args.template):
        if not path.is_file():
            raise SystemExit(f"File not found: {path}")

    mime_type, _ = mimetypes.guess_type(args.image.name)
    if not mime_type or not mime_type.startswith("image/"):
        raise SystemExit(f"Unsupported or unknown image type: {args.image.name}")

    image_bytes = args.image.read_bytes()
    encoded_image = base64.b64encode(image_bytes).decode("ascii")
    data_url = f"data:{mime_type};base64,{encoded_image}"
    text_items = load_text_items(args.texts)

    html = args.template.read_text(encoding="utf-8")
    replacements = {
        '"__IMAGE_DATA_URL__"': json.dumps(data_url, ensure_ascii=False),
        '"__IMAGE_ALT__"': json.dumps(args.alt, ensure_ascii=False),
        '"__IMAGE_NAME__"': json.dumps(args.image.name, ensure_ascii=False),
        "__TEXT_ITEMS__": json.dumps(text_items, ensure_ascii=False, separators=(",", ":")),
    }
    for marker, replacement in replacements.items():
        if marker not in html:
            raise SystemExit(f"Template marker not found: {marker}")
        html = html.replace(marker, replacement, 1)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Created: {args.output} ({args.output.stat().st_size:,} bytes)")
    print("Open this HTML file in a modern browser. Click a text object to edit it and use '导出 PNG' to save the result.")


if __name__ == "__main__":
    main()
