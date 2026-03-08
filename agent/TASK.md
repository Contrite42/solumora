# Current Task: Queue Completion Hold

**Status:** Complete (through USER-008)
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** 2026-03-07

## Summary

Completed USER-008 root-page normalization.

Delivered homepage/index alignment and simplified root hub roles so readers can differentiate onboarding (`index`), canonical hub (`Solumora`), primer (`World Primer`), and broad lookup (`World Index Draft`) without overlap.

## Completed Outputs (USER-008)

- Updated: `content/index.md`
- Updated: `content/Solumora.md`
- Updated: `content/World Primer.md`
- Updated: `content/World Index Draft.md`
- Refreshed: `tmp/concept-graph.json`, `tmp/context-index.json`
- Generated: `tmp/nav-root-solumora.json`

## Verification

- Quartz build passed on 652 input files.
- Navigation artifacts parse and report 652 pages.

Default navigation method (run from repo root):

1. `python scripts/python/pyhub.py run hub:concept_cache_query -- related <Concept> --top 20`
2. `python scripts/python/pyhub.py run hub:world_nav_query -- <Concept> --output tmp/nav-<concept>.json`

Required refresh steps after content changes:

1. `python scripts/python/pyhub.py run hub:concept_graph_export -- --output tmp/concept-graph.json`
2. `python scripts/python/pyhub.py run hub:build_context_index -- --output tmp/context-index.json`

Verification requirement:

- Confirm both cache files exist and parse after refresh: `tmp/concept-graph.json`, `tmp/context-index.json`.
- For active tasks, generate at least one task-scoped nav pack: `tmp/nav-<concept>.json`.

Operational rule:

- No task that changes `content/` is complete until navigation artifacts are refreshed in the same work cycle.
- No agent should run full-vault content traversal if cache-based navigation answers the task.
