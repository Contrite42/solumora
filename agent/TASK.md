# Current Task: Religion-in-Practice Expansion

**Status:** Complete
**Owner:** Codex (executing Copilot Auto task)
**Started:** 2026-03-08
**Completed:** 2026-03-08

## Summary

Completed religion-in-practice expansion: created 6 notes showing how rituals appear in households, workplaces, routes, and ports, plus 3 conflict notes documenting gaps between official doctrine and folk practice. Updated Religions.md and Solumora.md with "Practice vs Doctrine" synthesis sections.

## Completed Outputs (This Cycle)

- Added: `content/Household Religious Practice.md`
- Added: `content/Workplace Religious Practice and Tension.md`
- Added: `content/Religious Practice on Routes and Ports.md`
- Added: `content/Ascendant Path Doctrine and Folk Interpretation.md`
- Added: `content/Covenant Urban and Rural Practice Tensions.md`
- Added: `content/Ancestral Current and Institutional Friction.md`
- Updated: `content/Religions.md` (added "Practice vs. Doctrine" section)
- Updated: `content/Solumora.md` (added "Religion and Belief in Practice" section with navigation)
- Refreshed: `tmp/concept-graph.json` (796 nodes, 8758 edges, 643 pages)
- Refreshed: `tmp/context-index.json` (643 pages)
- Generated: `tmp/nav-religion-practice.json`

## Verification

- Build validation passed on 643 input files
- Navigation artifacts refreshed successfully
- All 6 new notes include ritual contexts and disagreement between official/folk practice per constraint
- Religions.md and Solumora.md updated with synthesis sections integrating new content

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
