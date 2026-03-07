#!/usr/bin/env python3
"""Central launcher for Python utilities in this repo.

All Python scripts are consolidated in scripts/python/.
This script provides one stable entry point for humans and agentic tools.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent


def discover_scripts() -> dict[str, Path]:
    """Discover all Python scripts in scripts/python/ directory."""
    scripts: dict[str, Path] = {}
    for path in sorted(SCRIPT_DIR.glob("*.py")):
        if path.name in {"pyhub.py", "__init__.py"}:
            continue
        scripts[path.stem] = path
    return scripts


def build_registry() -> dict[str, Path]:
    """Build script registry with hub: prefix for all scripts."""
    registry: dict[str, Path] = {}
    for name, path in discover_scripts().items():
        registry[f"hub:{name}"] = path
    return registry


def cmd_list(args: argparse.Namespace) -> int:
    """List all available scripts."""
    registry = build_registry()
    payload = [
        {
            "name": name,
            "path": str(path.relative_to(REPO_ROOT)),
        }
        for name, path in sorted(registry.items())
    ]
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for item in payload:
            print(f"{item['name']:<30} {item['path']}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    registry = build_registry()
    script = registry.get(args.script)
    if script is None:
        print(f"error: script '{args.script}' not found", file=sys.stderr)
        print("hint: run `python scripts/python/pyhub.py list`", file=sys.stderr)
        return 2

    cmd = [sys.executable, str(script), *args.script_args]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT))
    return proc.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Central Python script launcher")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List available Python scripts")
    p_list.add_argument("--json", action="store_true", help="Machine-readable output")
    p_list.set_defaults(func=cmd_list)

    p_run = sub.add_parser("run", help="Run a script by registry name")
    p_run.add_argument("script", help="Script name from `list`")
    p_run.add_argument("script_args", nargs=argparse.REMAINDER, help="Arguments passed to the script")
    p_run.set_defaults(func=cmd_run)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
