#!/usr/bin/env python3
"""Token-efficient world navigation query over cached graph + context index."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


DEFAULT_GRAPH = Path("tmp/concept-graph.json")
DEFAULT_INDEX = Path("tmp/context-index.json")


def load_graph(path: Path) -> tuple[dict[str, set[str]], dict[str, set[str]], set[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    out_edges: dict[str, set[str]] = defaultdict(set)
    in_edges: dict[str, set[str]] = defaultdict(set)
    nodes: set[str] = set()

    for n in data.get("nodes", []):
        node_id = n.get("id")
        if node_id:
            nodes.add(node_id)

    for e in data.get("edges", []):
        src = e.get("source")
        tgt = e.get("target")
        if not src or not tgt:
            continue
        out_edges[src].add(tgt)
        in_edges[tgt].add(src)
        nodes.add(src)
        nodes.add(tgt)

    return out_edges, in_edges, nodes


def load_index(path: Path) -> tuple[dict[str, dict], dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    by_id: dict[str, dict] = {}
    stem_map: dict[str, str] = {}
    for page in data.get("pages", []):
        page_id = page.get("id")
        if not page_id:
            continue
        by_id[page_id] = page
        stem_map[page_id.split("/")[-1].lower()] = page_id
    return by_id, stem_map


def resolve_concept(name: str, nodes: set[str], index_map: dict[str, dict], stem_map: dict[str, str]) -> str:
    if name in nodes:
        return name

    lower_nodes = {n.lower(): n for n in nodes}
    if name.lower() in lower_nodes:
        return lower_nodes[name.lower()]

    if name.lower() in stem_map:
        return stem_map[name.lower()]

    # Last fallback: if it exists in index ids but not graph nodes.
    if name in index_map:
        return name

    return name


def rank_candidates(seed: str, out_edges: dict[str, set[str]], in_edges: dict[str, set[str]]) -> list[tuple[str, int, str]]:
    scored: dict[str, tuple[int, str]] = {}

    def push(node: str, score: int, why: str):
        prev = scored.get(node)
        if prev is None or score > prev[0]:
            scored[node] = (score, why)

    push(seed, 10_000, "seed")

    for node in out_edges.get(seed, set()):
        s = 300 + len(in_edges.get(node, set()))
        push(node, s, "seed_outlink")

    for node in in_edges.get(seed, set()):
        s = 250 + len(out_edges.get(node, set()))
        push(node, s, "seed_backlink")

    # Second-order neighbors to keep navigation breadth.
    for node in list(out_edges.get(seed, set()))[:80]:
        for node2 in out_edges.get(node, set()):
            if node2 == seed:
                continue
            s = 60 + len(in_edges.get(node2, set()))
            push(node2, s, "second_order")

    ranked = sorted(((k, v[0], v[1]) for k, v in scored.items()), key=lambda t: (-t[1], t[0]))
    return ranked


def build_read_plan(page: dict, section_limit: int) -> list[dict]:
    plan = []
    for sec in page.get("sections", [])[:section_limit]:
        plan.append(
            {
                "section": sec.get("title", ""),
                "start_line": sec.get("start_line", 1),
                "end_line": sec.get("end_line", 1),
                "preview": sec.get("preview", ""),
            }
        )
    return plan


def run_query(args: argparse.Namespace) -> int:
    out_edges, in_edges, nodes = load_graph(Path(args.graph))
    index_map, stem_map = load_index(Path(args.index))

    seed = resolve_concept(args.concept, nodes, index_map, stem_map)
    ranked = rank_candidates(seed, out_edges, in_edges)

    pages = []
    for node, score, why in ranked[: args.top_pages]:
        page = index_map.get(node)
        if not page:
            continue
        pages.append(
            {
                "id": node,
                "path": page.get("path"),
                "title": page.get("title"),
                "why": why,
                "score": score,
                "line_count": page.get("line_count"),
                "outlink_count": page.get("outlink_count"),
                "read_plan": build_read_plan(page, args.sections_per_page),
            }
        )

    payload = {
        "concept": seed,
        "top_pages": pages,
        "neighbors": {
            "backlinks": sorted(in_edges.get(seed, set()))[: args.top_neighbors],
            "outlinks": sorted(out_edges.get(seed, set()))[: args.top_neighbors],
        },
    }

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        print(f"concept: {seed}")
        print("top pages:")
        for p in payload["top_pages"]:
            print(f"- {p['id']} ({p['why']}, score={p['score']}) -> {p['path']}")
            for sec in p["read_plan"]:
                print(f"  section: {sec['section']} [{sec['start_line']}:{sec['end_line']}] {sec['preview']}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Query cached world navigation data")
    parser.add_argument("concept", help="Seed concept/page id")
    parser.add_argument("--graph", default=str(DEFAULT_GRAPH), help="Concept graph JSON")
    parser.add_argument("--index", default=str(DEFAULT_INDEX), help="Context index JSON")
    parser.add_argument("--top-pages", type=int, default=12)
    parser.add_argument("--sections-per-page", type=int, default=4)
    parser.add_argument("--top-neighbors", type=int, default=30)
    parser.add_argument("--format", choices=["json", "text"], default="json")
    parser.add_argument("--output", help="Optional file path for query payload")

    args = parser.parse_args()
    return run_query(args)


if __name__ == "__main__":
    raise SystemExit(main())
