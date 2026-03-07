# Active Task: EXPANSION-002 - Wolfpoint as Living Hub

**Status:** IN PROGRESS
**Owner:** Copilot
**Started:** 2026-03-06

## Goal

Expand Wolfpoint from reference to operational crossroads showing northern trade nexus with frontier energy and mixed-tier grimoire access.

## Constraints

- Far north location, constant 45°F cold, wind-resistant architecture
- Voss family leadership and Hypertext development center (do not modify core canon)
- Existing economic operations: Cold-Forge Works (Trel Vann), Mountain Game Collective (Dren Vass, Morra Keld), Upland Herding Network (Lenna Tors)
- Small permanent population (few hundred) with rotating practitioners
- Names must follow WORLD_STATE.md conventions (short, terse, Germanic/Nordic)
- Voice must follow STYLE_GUIDE.md (matter-of-fact, people in motion)

## Output Target

6-8 notes total:
- 2-3 port/trade district notes (showing what flows through)
- 2-3 trade house/merchant operation notes (who profits from position)
- 2-3 NPC notes (merchants, operators, frontier characters)
- 1-2 courier operation notes (information movement)
- Update [[Wolfpoint]] with operational detail

## Execution Plan

1. Read existing Wolfpoint page fully
2. Identify gaps in operational detail (port structure, trade houses, couriers)
3. Design 2-3 districts/areas showing trade flow
4. Design 2-3 merchant operations and 2-3 NPCs
5. Design 1-2 courier/information operations
6. Write all content notes
7. Update Wolfpoint page with links
8. Refresh navigation artifacts
9. Mark complete in TASK_QUEUE.md

## Current Step

Reading Wolfpoint canon...

---

## PERMANENT TASK - Keep AI Navigation Artifacts Current

Use cached navigation as the default method for agent work. This is the token-efficient path and should be used before any full markdown scan.

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
