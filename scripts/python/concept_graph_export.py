#!/usr/bin/env python3
"""Export full markdown concept-link graph for agentic workflows.

Output is JSON and designed for deterministic downstream parsing.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

# Reuse graph parsing logic from concept_links.
from concept_links import CONTENT_ROOT, load_graph


def build_payload(content_root: Path) -> dict:
    out_edges, in_edges, page_paths = load_graph(content_root)

    nodes = sorted(set(out_edges) | set(in_edges))

    node_entries = []
    for node in nodes:
        node_entries.append(
            {
                "id": node,
                "is_page": node in page_paths,
                "path": str(page_paths[node].relative_to(content_root.parent)) if node in page_paths else None,
                "in_degree": len(in_edges.get(node, set())),
                "out_degree": len(out_edges.get(node, set())),
                "backlinks": sorted(in_edges.get(node, set())),
                "outlinks": sorted(out_edges.get(node, set())),
            }
        )

    edge_entries = []
    for src in sorted(out_edges):
        for tgt in sorted(out_edges[src]):
            edge_entries.append({"source": src, "target": tgt})

    payload = {
        "schema_version": 1,
        "content_root": str(content_root),
        "node_count": len(node_entries),
        "edge_count": len(edge_entries),
        "page_count": len(page_paths),
        "nodes": node_entries,
        "edges": edge_entries,
    }
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export full concept graph as JSON")
    parser.add_argument("--content-root", default=str(CONTENT_ROOT), help="Path to content directory")
    parser.add_argument(
        "--output",
        default="tmp/concept-graph.json",
        help="Destination JSON path (default: tmp/concept-graph.json)",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    content_root = Path(args.content_root)
    payload = build_payload(content_root)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.pretty:
        text = json.dumps(payload, indent=2)
    else:
        text = json.dumps(payload, separators=(",", ":"))

    out_path.write_text(text + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "output": str(out_path),
                "node_count": payload["node_count"],
                "edge_count": payload["edge_count"],
                "page_count": payload["page_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
