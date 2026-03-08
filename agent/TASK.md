# Current Task: Post-Arc Continuation — Eighteen-Month Regional Divergence Testing

**Status:** Complete
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** 2026-03-07

## Summary

Extended continuation with eighteen-month regional variance stress-testing: created asymmetric enforcement doctrine and border protocol framework, then validated divergent compliance patterns across Protected Observation zones, border settlements, and Full Integration core cities.

## Completed Outputs (Continuation Tranche)

- Created: `content/Regional Enforcement Variance Doctrine.md`
- Created: `content/Border Settlement Coexistence Protocol.md`
- Created: `content/Stories/Eighteen Months After the First Casualty - Protected Zone Morning.md`
- Created: `content/Stories/Eighteen Months After the First Casualty - Border Market.md`
- Created: `content/Stories/Eighteen Months After the First Casualty - Core City Integration.md`
- Updated: `content/The Three Near-Wars.md` (eighteen-month bundle + regional variance institutions)

## Status

- Continuation tranche complete.
- Canon now extends from first-casualty trigger through eighteen-month geographic compliance divergence and managed asymmetric adaptation testing.

## Verification

- Story files include cross-links to active escalation hubs and preserve creator decision space by avoiding explicit war-trigger attribution.
- Hub backlink added so each new story has inbound discoverability through `The Three Near-Wars`.

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
