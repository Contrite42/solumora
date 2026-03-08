# Current Task: Character Stub Upgrade Batches

**Status:** Complete
**Owner:** Codex (executing Copilot Auto task)
**Started:** 2026-03-08
**Completed:** 2026-03-08

## Summary

Completed the thin-character upgrade cycle by expanding 24 `<=12`-line cast pages in four themed batches: port workers, border workers, rural workers, and institutional staff. Each upgraded page now includes explicit operational details for routine, non-public fact, institutional tie, and practical stakes.

## Completed Outputs (This Cycle)

- Updated (Port batch): `content/Lenne Sosk.md`, `content/Oryen Veld.md`, `content/Korvin Selt.md`, `content/Drev Oln.md`, `content/Pell Vastl.md`, `content/Nara Celd.md`
- Updated (Border batch): `content/Selt Orvn.md`, `content/Vorn Teld.md`, `content/Cor Meln.md`, `content/Collen Mast.md`, `content/Celn Vard.md`, `content/Ossen Drel.md`
- Updated (Rural batch): `content/Maret Doss.md`, `content/Reth Caln.md`, `content/Hallen Vors.md`, `content/Prenn Aldv.md`, `content/Teva Orrn.md`, `content/Mella Seln.md`
- Updated (Institutional batch): `content/Ren Valdh.md`, `content/Essa Rolt.md`, `content/Osten Reld.md`, `content/Miren Thask.md`, `content/Sorren Kael.md`, `content/Vessa Oln.md`
- Updated: `agent/staging/PENDING_REVIEW.md` with four `[Copilot Auto]` batch summary blocks

## Verification

- Confirmed 24 profile files now include `## Operational Profile Update (2026-03-08)` sections
- Required fields present in each upgraded profile: job routine, non-public fact, institutional tie, practical stakes

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
