#!/usr/bin/env python3
"""Audit markdown section coverage across content pages.

Checks configurable section headings and writes a markdown report.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AuditResult:
    path: Path
    missing: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit required markdown sections")
    parser.add_argument(
        "--content-dir",
        default="content",
        help="Content directory to scan (default: content)",
    )
    parser.add_argument(
        "--required",
        nargs="+",
        default=["Appearance", "Relationships", "Use In Session"],
        help="Required section headings (without ##)",
    )
    parser.add_argument(
        "--output",
        default="agent/reports/section_audit.md",
        help="Markdown report output path",
    )
    return parser.parse_args()


def iter_markdown_files(content_dir: Path) -> list[Path]:
    return sorted(p for p in content_dir.rglob("*.md") if p.is_file())


def heading_present(text: str, heading: str) -> bool:
    needle = f"## {heading}"
    return needle.lower() in text.lower()


def audit_file(path: Path, required: list[str]) -> AuditResult:
    text = path.read_text(encoding="utf-8")
    missing = [name for name in required if not heading_present(text, name)]
    return AuditResult(path=path, missing=missing)


def write_report(output_path: Path, results: list[AuditResult], required: list[str]) -> None:
    total = len(results)
    complete = sum(1 for r in results if not r.missing)
    missing_any = total - complete

    lines: list[str] = []
    lines.append("# Section Audit Report")
    lines.append("")
    lines.append(f"- Files scanned: {total}")
    lines.append(f"- Fully compliant: {complete}")
    lines.append(f"- Missing one or more sections: {missing_any}")
    lines.append(f"- Required sections: {', '.join(required)}")
    lines.append("")

    for section in required:
        offenders = [r for r in results if section in r.missing]
        lines.append(f"## Missing `{section}` ({len(offenders)})")
        lines.append("")
        if not offenders:
            lines.append("- None")
        else:
            for item in offenders[:200]:
                lines.append(f"- `{item.path.as_posix()}`")
            if len(offenders) > 200:
                lines.append(f"- ... and {len(offenders) - 200} more")
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    content_dir = repo_root / args.content_dir
    output_path = repo_root / args.output

    files = iter_markdown_files(content_dir)
    results = [audit_file(path, args.required) for path in files]
    write_report(output_path, results, args.required)

    print(f"Wrote section audit report: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
