#!/usr/bin/env python3
"""Concept-link discovery tools for Quartz content.

Designed for agentic workflows:
- deterministic CLI
- JSON output for automation
- no external dependencies
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict, deque
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_ROOT = REPO_ROOT / "content"
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def normalize_link_target(raw: str) -> str:
    # Handle aliases and anchors: [[A#B|Label]] -> A
    value = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return value


def page_id_for(path: Path) -> str:
    rel = path.relative_to(CONTENT_ROOT)
    without_ext = rel.with_suffix("")
    # Preserve nested paths like WrittenWorks/Foo
    return without_ext.as_posix()


def load_graph(content_root: Path) -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, Path]]:
    out_edges: dict[str, set[str]] = defaultdict(set)
    in_edges: dict[str, set[str]] = defaultdict(set)
    page_paths: dict[str, Path] = {}

    md_files = sorted(content_root.rglob("*.md"))
    for path in md_files:
        src = page_id_for(path)
        page_paths[src] = path

        text = path.read_text(encoding="utf-8", errors="replace")
        for match in WIKILINK_RE.findall(text):
            tgt = normalize_link_target(match)
            if not tgt:
                continue
            out_edges[src].add(tgt)
            in_edges[tgt].add(src)

    # Ensure pages with no links are still represented.
    for page in page_paths:
        out_edges.setdefault(page, set())
        in_edges.setdefault(page, set())

    return out_edges, in_edges, page_paths


def resolve_concept(name: str, page_paths: dict[str, Path]) -> str | None:
    if name in page_paths:
        return name

    # Case-insensitive exact match.
    lower_map = {k.lower(): k for k in page_paths}
    if name.lower() in lower_map:
        return lower_map[name.lower()]

    # Fallback: stem-style match for convenience.
    stem_map = {Path(k).name.lower(): k for k in page_paths}
    return stem_map.get(name.lower())


def command_index(args: argparse.Namespace) -> int:
    out_edges, in_edges, page_paths = load_graph(Path(args.content_root))

    nodes = sorted(set(out_edges) | set(in_edges))
    edge_count = sum(len(v) for v in out_edges.values())

    payload = {
        "content_root": str(Path(args.content_root)),
        "nodes": len(nodes),
        "edges": edge_count,
        "pages": len(page_paths),
    }

    if args.output:
        Path(args.output).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(json.dumps(payload, indent=2) if args.format == "json" else f"nodes={payload['nodes']} edges={edge_count} pages={payload['pages']}")
    return 0


def command_backlinks(args: argparse.Namespace) -> int:
    out_edges, in_edges, page_paths = load_graph(Path(args.content_root))
    concept = resolve_concept(args.concept, page_paths) or args.concept

    sources = sorted(in_edges.get(concept, set()))
    targets = sorted(out_edges.get(concept, set()))

    payload = {
        "concept": concept,
        "backlink_count": len(sources),
        "outlink_count": len(targets),
        "backlinks": sources,
        "outlinks": targets,
    }

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        print(f"concept: {concept}")
        print(f"backlinks ({len(sources)}):")
        for item in sources:
            print(f"- {item}")
        print(f"outlinks ({len(targets)}):")
        for item in targets:
            print(f"- {item}")
    return 0


def command_related(args: argparse.Namespace) -> int:
    out_edges, in_edges, page_paths = load_graph(Path(args.content_root))
    concept = resolve_concept(args.concept, page_paths) or args.concept

    neighbor_scores: dict[str, int] = defaultdict(int)

    # Related via common backlinks and outlinks.
    for src in in_edges.get(concept, set()):
        for tgt in out_edges.get(src, set()):
            if tgt != concept:
                neighbor_scores[tgt] += 1

    for tgt in out_edges.get(concept, set()):
        for src in in_edges.get(tgt, set()):
            if src != concept:
                neighbor_scores[src] += 1

    ranked = sorted(neighbor_scores.items(), key=lambda kv: (-kv[1], kv[0]))[: args.top]

    payload = {
        "concept": concept,
        "related": [{"concept": c, "score": s} for c, s in ranked],
    }

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        print(f"related concepts for {concept}:")
        for item in payload["related"]:
            print(f"- {item['concept']} (score={item['score']})")
    return 0


def command_path(args: argparse.Namespace) -> int:
    out_edges, _in_edges, page_paths = load_graph(Path(args.content_root))
    start = resolve_concept(args.source, page_paths) or args.source
    goal = resolve_concept(args.target, page_paths) or args.target

    q: deque[str] = deque([start])
    prev: dict[str, str | None] = {start: None}

    while q:
        cur = q.popleft()
        if cur == goal:
            break
        for nxt in sorted(out_edges.get(cur, set())):
            if nxt not in prev:
                prev[nxt] = cur
                q.append(nxt)

    path: list[str] = []
    if goal in prev:
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()

    payload = {
        "source": start,
        "target": goal,
        "found": bool(path),
        "path": path,
        "hops": max(0, len(path) - 1),
    }

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        if payload["found"]:
            print(" -> ".join(path))
        else:
            print(f"no path from {start} to {goal}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Find linked concepts in markdown wiki-link graph")
    p.add_argument("--content-root", default=str(CONTENT_ROOT), help="Path to content directory")
    p.add_argument("--format", choices=["json", "text"], default="json", help="Output format")

    sub = p.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="Report graph size summary")
    p_index.add_argument("--output", help="Optional path to write JSON summary")
    p_index.set_defaults(func=command_index)

    p_back = sub.add_parser("backlinks", help="Show backlinks/outlinks for a concept")
    p_back.add_argument("concept", help="Concept/page name")
    p_back.set_defaults(func=command_backlinks)

    p_rel = sub.add_parser("related", help="Find related concepts by link co-occurrence")
    p_rel.add_argument("concept", help="Concept/page name")
    p_rel.add_argument("--top", type=int, default=20, help="Number of related concepts")
    p_rel.set_defaults(func=command_related)

    p_path = sub.add_parser("path", help="Find shortest link path between concepts")
    p_path.add_argument("source", help="Source concept/page")
    p_path.add_argument("target", help="Target concept/page")
    p_path.set_defaults(func=command_path)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
