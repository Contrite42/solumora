# Current Task: Awaiting Input
# Current Task: USER-002 Near-War Flashpoint Incident Ladder (Phase 1)

**Status:** In Progress
**Owner:** Codex
**Started:** 2026-03-07
**Completed:** N/A

## Summary

Activated USER-002 from `agent/TASK_QUEUE.md` to build the first concrete escalation layer beneath `[[The Three Near-Wars]]`.

This phase focuses on operational incidents and de-escalation mechanics that connect existing border-trade tension pages to lived outcomes.

**Phase 1 delivered (initial batch):**
- `content/Near-War Incident Ladder.md`
- `content/Halveth Customs Seizure Incident.md`
- `content/Ashford Courier Intercept Case.md`
- `content/Border De-Escalation Protocols.md`
- Hub updates: `content/The Three Near-Wars.md`, `content/Border Trade.md`

**Task-scoped navigation seed generated:**
- `tmp/nav-near-war-flashpoint.json`

**Navigation artifacts refreshed after edits:**
- `tmp/concept-graph.json` (781 nodes, 8280 edges, 628 pages)
- `tmp/context-index.json` (628 pages)

## Execution Targets (Phase 1)

- Create 4-6 notes covering incident progression and response mechanics.
- Update `content/The Three Near-Wars.md` with compact, cross-linked incident-ladder section.
- Update one border operations hub (`content/Border Trade.md` or `content/Cross-Border Trade.md`) with the new references.

## Next Steps

- Expand Phase 1 with 1-2 additional incident-response notes to reach target depth.
- Append compact operational synthesis to `content/Cross-Border Trade.md`.
- Run canon/link integrity pass for this batch and record results.

Default navigation method (run from repo root):

1. `python scripts/python/pyhub.py run hub:concept_cache_query -- related <Concept> --top 20`
2. `python scripts/python/pyhub.py run hub:world_nav_query -- <Concept> --output tmp/nav-<concept>.json`

Refresh artifacts only when `content/` changed in the current cycle (new page, deleted page, or material edit).

Required refresh steps after content changes:

1. `python scripts/python/pyhub.py run hub:concept_graph_export -- --output tmp/concept-graph.json`
2. `python scripts/python/pyhub.py run hub:build_context_index -- --output tmp/context-index.json`

Verification requirement:

- Confirm both cache files exist and parse after refresh: `tmp/concept-graph.json`, `tmp/context-index.json`.
- For active tasks, generate at least one task-scoped nav pack: `tmp/nav-<concept>.json`.

Operational rule:

- No task that changes `content/` is complete until navigation artifacts are refreshed in the same work cycle.
- No agent should run full-vault content traversal if cache-based navigation answers the task.

---

## Policy: Grimoire Spell Management

Active policy for all spell-related work:
- Do not create new `content/Spells/*.md` pages.
- Add and maintain spells only inside tiered grimoire files.
- Tiered grimoires are the canonical spell reference source.

Cassia is not passive. She has twenty-three years of being in rooms where things are decided, and she has learned to read what is not said. She cannot act on most of what she knows — her position is constrained in ways that have been reinforced across her entire life — but she observes accurately and she retains what she observes.

What she knows: The Expansion Faction is accelerating. She has watched Drest's voting alignment shift over three years in ways that tell her something is in motion. She knows that [[Castor Helme]] talks loudly about things and that [[Davan Rhyce]] does not talk at all, and she knows which of these is more dangerous. She has a working model of what Brennan Solce's "careful" reaction means when she reads it in briefing summaries.

What she is doing with it: She is writing. Not correspondence — private notes, kept in a cipher she developed at seventeen. Not for any audience. For herself, because the alternative is watching what she sees disappear into the administrative record in its managed form. She is also being very careful with what she asks to read, and why, and when — because her requests are noted and she has learned to arrange them so the pattern is not visible.

She has not told anyone about this. There is no one she trusts with it. [[Ysel Voss]] might be the nearest candidate, but Ysel is at Wolfpoint, and Cassia does not have communication with Wolfpoint that is not reviewed.

Voice: Direct. Controlled. No self-pity, no martyrdom. She is managing a situation, not performing tragedy.

Outbound links: [[The Council of Auralis]], [[Expansion Faction]], [[Drest]], [[Castor Helme]], [[Davan Rhyce]], [[Brennan Solce]], [[Ysel Voss]], [[Wolfpoint]]

---

## RULES

- APPENDS ONLY. Do not alter or rewrite existing content on any page.
- No new characters invented. Use only names that already exist in the vault.
- No new kingdoms, factions, or lore invented. Expansion Faction already exists.
- Each append connects to the political pressure already established — characters observe effects without naming causes.
- Plan ONLY these 4 file targets (3 Ashford characters + Cassia). Do not add extras.
- After each append, update the See Also for that page to include any new links introduced.
