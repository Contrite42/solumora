#!/usr/bin/env python3
"""Query pre-exported concept graph without re-scanning markdown.

Fast path for agentic tools that already have tmp/concept-graph.json.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from pathlib import Path


DEFAULT_GRAPH = Path("tmp/concept-graph.json")


def load_graph(path: Path) -> tuple[dict[str, set[str]], dict[str, set[str]], set[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    out_edges: dict[str, set[str]] = defaultdict(set)
    in_edges: dict[str, set[str]] = defaultdict(set)
    nodes: set[str] = set()

    for node in data.get("nodes", []):
        node_id = node.get("id")
        if node_id:
            nodes.add(node_id)

    for edge in data.get("edges", []):
        src = edge.get("source")
        tgt = edge.get("target")
        if not src or not tgt:
            continue
        out_edges[src].add(tgt)
        in_edges[tgt].add(src)
        nodes.add(src)
        nodes.add(tgt)

    for n in nodes:
        out_edges.setdefault(n, set())
        in_edges.setdefault(n, set())

    return out_edges, in_edges, nodes


def resolve(name: str, nodes: set[str]) -> str | None:
    if name in nodes:
        return name

    lower = {n.lower(): n for n in nodes}
    if name.lower() in lower:
        return lower[name.lower()]

    base = {n.split("/")[-1].lower(): n for n in nodes}
    return base.get(name.lower())


def output(payload: dict, fmt: str):
    if fmt == "json":
        print(json.dumps(payload, indent=2))
        return

    for key, value in payload.items():
        if isinstance(value, list):
            print(f"{key} ({len(value)}):")
            for item in value:
                print(f"- {item}")
        else:
            print(f"{key}: {value}")


def cmd_stats(args: argparse.Namespace) -> int:
    out_edges, _in_edges, nodes = load_graph(Path(args.graph))
    payload = {
        "nodes": len(nodes),
        "edges": sum(len(v) for v in out_edges.values()),
    }
    output(payload, args.format)
    return 0


def cmd_backlinks(args: argparse.Namespace) -> int:
    out_edges, in_edges, nodes = load_graph(Path(args.graph))
    concept = resolve(args.concept, nodes) or args.concept
    payload = {
        "concept": concept,
        "backlinks": sorted(in_edges.get(concept, set())),
        "outlinks": sorted(out_edges.get(concept, set())),
    }
    output(payload, args.format)
    return 0


def cmd_related(args: argparse.Namespace) -> int:
    out_edges, in_edges, nodes = load_graph(Path(args.graph))
    concept = resolve(args.concept, nodes) or args.concept

    score: dict[str, int] = defaultdict(int)
    for src in in_edges.get(concept, set()):
        for tgt in out_edges.get(src, set()):
            if tgt != concept:
                score[tgt] += 1
    for tgt in out_edges.get(concept, set()):
        for src in in_edges.get(tgt, set()):
            if src != concept:
                score[src] += 1

    ranked = sorted(score.items(), key=lambda kv: (-kv[1], kv[0]))[: args.top]
    payload = {
        "concept": concept,
        "related": [{"concept": c, "score": s} for c, s in ranked],
    }
    output(payload, args.format)
    return 0


def cmd_path(args: argparse.Namespace) -> int:
    out_edges, _in_edges, nodes = load_graph(Path(args.graph))
    src = resolve(args.source, nodes) or args.source
    tgt = resolve(args.target, nodes) or args.target

    prev: dict[str, str | None] = {src: None}
    q: deque[str] = deque([src])

    while q:
        cur = q.popleft()
        if cur == tgt:
            break
        for nxt in sorted(out_edges.get(cur, set())):
            if nxt not in prev:
                prev[nxt] = cur
                q.append(nxt)

    path: list[str] = []
    if tgt in prev:
        cur = tgt
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()

    payload = {
        "source": src,
        "target": tgt,
        "found": bool(path),
        "path": path,
        "hops": max(0, len(path) - 1),
    }
    output(payload, args.format)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Query cached concept graph JSON")
    p.add_argument("--graph", default=str(DEFAULT_GRAPH), help="Path to graph JSON export")
    p.add_argument("--format", choices=["json", "text"], default="json")

    sub = p.add_subparsers(dest="command", required=True)

    s_stats = sub.add_parser("stats", help="Show node/edge counts")
    s_stats.set_defaults(func=cmd_stats)

    s_back = sub.add_parser("backlinks", help="Show backlinks/outlinks for a concept")
    s_back.add_argument("concept")
    s_back.set_defaults(func=cmd_backlinks)

    s_rel = sub.add_parser("related", help="Show related concepts")
    s_rel.add_argument("concept")
    s_rel.add_argument("--top", type=int, default=20)
    s_rel.set_defaults(func=cmd_related)

    s_path = sub.add_parser("path", help="Shortest path between two concepts")
    s_path.add_argument("source")
    s_path.add_argument("target")
    s_path.set_defaults(func=cmd_path)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
