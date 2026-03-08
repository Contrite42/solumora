# Current Task: Major Narrative Arc — War and Resolution (Phase 2)

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Expected Timeline:** Multi-phase development (8-12 stories + world state transformation)

## Summary

Executing Decision F through a multi-phase arc focused on competence-over-power leadership, rift cascade prevention, and forced High Demon revelation. Phase 1 completed the war trigger and core party entities; Phase 2 begins assembly through linked operational stories.

## Completed Outputs

### Phase 1: Foundation

- Updated: `agent/DECISIONS.md` (recorded Decision F approval with full selections)
- Created: `content/Kellvost Incursion.md` (war trigger event: rift catastrophe, 53 dead, Council negligence exposed)
- Created: `content/Merra Veld.md` (protagonist: T2 expedition rescue specialist, 12 years desert experience)
- Created: `content/Teren Voss.md` (High Demon Verath, 400+ years old, hiding as book dealer, forced to act by cascade threat)
- Created: `content/Jess Maren.md` (T0 logistics expert, 22 years supply chain experience, competence-over-power exemplar)
- Created: `content/Kess Tarren.md` (T4-5 ruins scholar, independent researcher, understands ancient stabilization mechanisms)

### Phase 2: Party Assembly (in progress)

- Created: `content/Stories/Forty-Five Days After the First Casualty - Rescue Summons.md`
- Created: `content/Stories/Forty-Five Days After the First Casualty - Archive Dealer.md`
- Created: `content/Stories/Forty-Five Days After the First Casualty - Dry Warehouse Nine.md`
- Updated: `content/The Three Near-Wars.md` (new story-bundle index section + see-also links)

## Status

- Phase 1 complete.
- Phase 2 in progress.
- Next phases after assembly: investigation/escalation, revelation/resolution, post-war world-state updates.

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
