# Current Task: USER-006 Municipal Friction in Greyveil (Scale vs. Governance)

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** N/A

## Summary

Activated USER-006 from `agent/TASK_QUEUE.md` after completing USER-005 expedition-risk finance outputs.

This phase focuses on recurring municipal failure loops in Greyveil where district systems remain active but governance coordination is too thin for stable service quality.

## Prior Cycle Completion (USER-005)

Completed outputs:
- `content/Crossing Risk Underwriters.md`
- `content/Death Ledger Claim Adjudication.md`
- `content/Expedition Insurance Fraud Patterns.md`
- `content/Survivor Benefit Contracts.md`
- Hub updates: `content/Adventurer Support Network.md`, `content/Banking Institutions.md`

## Execution Targets (USER-006)

- Create 4-5 notes covering waste/water breakdown episodes, district mediation routines, emergency work crews, and budget conflict.
- Update `content/Greyveil.md` and `content/Greyveil Civic Coordination.md`.
- Ensure each new note has >=3 outbound links and >=1 inbound hub link.

## Next Steps

- Add first USER-006 tranche:
  - `Greyveil Water Interruption Episodes`
  - `District Boundary Mediation Routine`
  - `Emergency Utility Work Crews`
- Append synthesis to Greyveil hub pages.
- Refresh navigation artifacts after content edits.

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
