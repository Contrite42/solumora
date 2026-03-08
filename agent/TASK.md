# Current Task: USER-005 Desert Crossing Insurance and Death Ledger Economy

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** N/A

## Summary

Activated USER-005 from `agent/TASK_QUEUE.md` after completing USER-004 black-market grimoire risk-chain outputs.

This phase focuses on underwriting, claims adjudication, fraud controls, and survivor-benefit structures for high-risk expedition finance.

## Prior Cycle Completion (USER-004)

Completed outputs:
- `content/Illicit Grimoire Supply Nodes.md`
- `content/Counterfeit Grimoire Verification Failures.md`
- `content/Black-Market Transfer Laundering.md`
- `content/Seizure Escalation Procedures.md`
- `content/Solhaven Ledger Burn Case.md`
- Hub updates: `content/Black Market Grimoires.md`, `content/Grimoires.md`

## Execution Targets (USER-005)

- Create 4-6 notes covering underwriters, claim adjudication, fraud patterns, and survivor-benefit contracts.
- Update `content/Adventurer Support Network.md` and one economy/banking hub.
- Ensure each new note has >=3 outbound links and >=1 inbound hub link.

## Next Steps

- Add first USER-005 tranche:
  - `Crossing Risk Underwriters`
  - `Death Ledger Claim Adjudication`
  - `Expedition Insurance Fraud Patterns`
- Append compact synthesis to adventure/economy hubs.
- Refresh navigation artifacts after content changes.

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
