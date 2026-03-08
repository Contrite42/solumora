# Current Task: Story Bundle - Three Nights to First Shot

**Status:** Complete
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** 2026-03-07

## Summary

Created a decision-neutral war-edge story bundle that increases constitutional-war pressure without selecting creator-only arc options in Decision F.

## Completed Outputs (This Cycle)

- Created: `content/Stories/Three Nights to First Shot - Scout.md`
- Created: `content/Stories/Three Nights to First Shot - Quartermaster.md`
- Created: `content/Stories/Three Nights to First Shot - Courier.md`
- Updated: `content/The Three Near-Wars.md` (new story-bundle index section + see-also links)

## Verification

- Story files include cross-links to active escalation hubs and avoid introducing canon-breaking outcomes.
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
