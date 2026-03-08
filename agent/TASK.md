# Current Task: USER-003 Civilian Continuity Under Strain (Food, Care, Shelter)

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** N/A

## Summary

Activated USER-003 from `agent/TASK_QUEUE.md` to model civilian continuity under sustained but non-collapse pressure.

This phase focuses on practical household and district adaptation in food access, care throughput, and service prioritization across `[[Terravelle]]` and `[[Auralis]]`.

## USER-003 Progress (current cycle)

Completed outputs:
- `content/Queue Management Offices.md`
- `content/Ration Substitution Practices.md`
- `content/Care Triage Workflows.md`
- Hub updates: `content/Clinical Care Systems.md`, `content/Ordinary Life in Terravelle.md`

Carryover from prior completion in same session:
- USER-002 marked complete (6 notes + 3 hub updates)

## Execution Targets (USER-003)

- Create 5-7 notes covering queue systems, ration substitutions, care triage, temporary housing pressure, and local coordinator roles.
- Ensure each new note has at least 3 outbound links and at least one inbound hub link.
- Update required hubs with compact integration blocks.

## Next Steps

- Add 2-4 more USER-003 notes:
  - `Temporary Housing Pressure`
  - `District Continuity Coordinators`
  - optional locality case note (Terravelle district + Auralis district)
- Append one synthesis block to a cross-system hub (`Ordinary Life` or `Auralis`).
- Refresh nav artifacts after each content-edit cycle.

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
