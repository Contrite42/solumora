# Current Task: Major Narrative Arc Foundation — War and Resolution (Phase 1)

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Expected Timeline:** Multi-phase development (8-12 stories + world state transformation)

## Summary

Building foundation for major narrative arc following Decision F approval. Arc centers on rift cascade threat, party-based resolution, and High Demon revelation. Protagonist: Merra Veld (T2 rescue specialist). Party composition: Merra + High Demon + T0 Logistics + Ruins Scholar + Cassia. Resolution: High Demons forced to reveal themselves to prevent dimensional collapse.

## Completed Outputs (Phase 1: Foundation)

- Updated: `agent/DECISIONS.md` (recorded Decision F approval with full selections)
- Created: `content/Kellvost Incursion.md` (war trigger event: rift catastrophe, 53 dead, Council negligence exposed)
- Created: `content/Merra Veld.md` (protagonist: T2 expedition rescue specialist, 12 years desert experience)
- Created: `content/Teren Voss.md` (High Demon Verath, 400+ years old, hiding as book dealer, forced to act by cascade threat)
- Created: `content/Jess Maren.md` (T0 logistics expert, 22 years supply chain experience, competence-over-power exemplar)
- Created: `content/Kess Tarren.md` (T4-5 ruins scholar, independent researcher, understands ancient stabilization mechanisms)

## Phase 1 Status: Foundation Complete

All core party members created. War trigger event documented. Next phases:
- Phase 2: Party assembly and initial crisis recognition
- Phase 3: Investigation and escalation
- Phase 4: Resolution and revelation
- Phase 5: Post-war world state transformation

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
