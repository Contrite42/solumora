# Current Task: USER-004 Black-Market Grimoire Risk Chain

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** N/A

## Summary

Activated USER-004 from `agent/TASK_QUEUE.md` after completing USER-003 civilian continuity outputs.

This phase will build an end-to-end black-market grimoire risk chain from source and copying through laundering, transit, enforcement response, and fallout.

## Prior Cycle Completion (USER-003)

Completed outputs:
- `content/Queue Management Offices.md`
- `content/Ration Substitution Practices.md`
- `content/Care Triage Workflows.md`
- `content/Temporary Housing Pressure.md`
- `content/District Continuity Coordinators.md`
- `content/Shelter Rotation Contracts.md`
- Hub updates: `content/Clinical Care Systems.md`, `content/Ordinary Life in Terravelle.md`, `content/Ordinary Life.md`, `content/Ordinary Life in Auralis.md`

## Execution Targets (USER-004)

- Create 5-6 notes covering supply chain nodes, counterfeit verification failures, seizure process, laundering channels, and one case study.
- Update `content/Black Market Grimoires.md` and `content/Grimoires.md` with compact integration blocks.
- Ensure each new note has >=3 outbound links and >=1 inbound hub link.

## Next Steps

- Add first USER-004 tranche:
  - `Counterfeit Grimoire Verification Failures`
  - `Seizure Escalation Procedures`
  - `Black-Market Transfer Laundering`
- Append synthesis to black-market hubs.
- Refresh navigation artifacts after each content cycle.

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
