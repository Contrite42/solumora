#!/usr/bin/env python3
"""Build a detail-preserving navigation index for content markdown.

The index is optimized for low-token discovery while preserving precise pointers
(file path + line ranges) so agents can fetch details on demand.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path


WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def normalize_link_target(raw: str) -> str:
    return raw.split("|", 1)[0].split("#", 1)[0].strip()


def page_id_for(content_root: Path, path: Path) -> str:
    rel = path.relative_to(content_root)
    return rel.with_suffix("").as_posix()


def parse_sections(lines: list[str]) -> list[dict]:
    headings: list[dict] = []
    for idx, line in enumerate(lines, start=1):
        m = HEADING_RE.match(line)
        if not m:
            continue
        headings.append({"line": idx, "level": len(m.group(1)), "title": m.group(2).strip()})

    sections: list[dict] = []
    if not headings:
        preview = ""
        for line in lines:
            t = line.strip()
            if t:
                preview = t[:220]
                break
        sections.append(
            {
                "title": "Document",
                "level": 0,
                "start_line": 1,
                "end_line": len(lines),
                "preview": preview,
            }
        )
        return sections

    for i, h in enumerate(headings):
        start = h["line"]
        end = headings[i + 1]["line"] - 1 if i + 1 < len(headings) else len(lines)

        preview = ""
        for ln in range(start, min(end + 1, start + 25)):
            t = lines[ln - 1].strip()
            if t and not HEADING_RE.match(t):
                preview = t[:220]
                break

        sections.append(
            {
                "title": h["title"],
                "level": h["level"],
                "start_line": start,
                "end_line": end,
                "preview": preview,
            }
        )

    return sections


def extract_outlinks(text: str) -> list[str]:
    links = []
    for raw in WIKILINK_RE.findall(text):
        target = normalize_link_target(raw)
        if target:
            links.append(target)
    return sorted(set(links))


def infer_title(path: Path, lines: list[str]) -> str:
    for line in lines[:30]:
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) == 1:
            return m.group(2).strip()
    for line in lines[:30]:
        m = HEADING_RE.match(line)
        if m:
            return m.group(2).strip()
    return path.stem


def build_index(content_root: Path) -> dict:
    pages: list[dict] = []
    for path in sorted(content_root.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        page_id = page_id_for(content_root, path)
        outlinks = extract_outlinks(text)
        sections = parse_sections(lines)

        page = {
            "id": page_id,
            "path": str(path.relative_to(content_root.parent)).replace("\\", "/"),
            "title": infer_title(path, lines),
            "line_count": len(lines),
            "char_count": len(text),
            "outlink_count": len(outlinks),
            "outlinks": outlinks,
            "sections": sections,
        }
        pages.append(page)

    return {
        "schema_version": 1,
        "generated_at_unix": int(time.time()),
        "content_root": str(content_root),
        "page_count": len(pages),
        "pages": pages,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build context navigation index")
    parser.add_argument("--content-root", default="content", help="Content folder path")
    parser.add_argument("--output", default="tmp/context-index.json", help="Output JSON path")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    args = parser.parse_args()

    content_root = Path(args.content_root)
    payload = build_index(content_root)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2) if args.pretty else json.dumps(payload, separators=(",", ":"))
    output.write_text(text + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "output": str(output),
                "page_count": payload["page_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
