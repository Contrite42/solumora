# Current Task: USER-007 Story Bundle: Five Days Before the Breakpoint

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** N/A

## Summary

Activated USER-007 from `agent/TASK_QUEUE.md` after completing USER-006 municipal friction outputs.

This phase will deliver three tightly linked stories across operator, merchant, and household perspectives anchored to current canon escalation conditions.

## Prior Cycle Completion (USER-006)

Completed outputs:
- `content/Greyveil Water Interruption Episodes.md`
- `content/District Boundary Mediation Routine.md`
- `content/Emergency Utility Work Crews.md`
- `content/Greyveil Maintenance Budget Conflicts.md`
- Hub updates: `content/Greyveil.md`, `content/Greyveil Civic Coordination.md`

## Execution Targets (USER-007)

- Create 3 story files in `content/Stories/` across three social layers.
- Anchor story events to established canon tensions and existing locations.
- Add one index-style link update in a relevant hub page.

## Next Steps

- Draft story set:
  - operator perspective (border/corridor)
  - merchant perspective (contract and risk)
  - household perspective (continuity under strain)
- Add story index block to a relevant hub (likely `Ordinary Life` or `The Three Near-Wars`).
- Refresh navigation artifacts and task-scoped nav pack.

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
