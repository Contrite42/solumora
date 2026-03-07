# Active Task: EXPANSION-011 - Wilderness & Creatures

**Status:** NOT STARTED
**Owner:** Copilot
**Started:** 2026-03-07

## Goal

Build ecosystem layer with dangerous/useful creatures beyond [[Equatorial Fauna]] showing Flux effects on wildlife and creature-based economy (hunter culture, creature product trade, symbiotic relationships).

## Constraints

- Show Flux's effect on wildlife (mutations, behaviors, flux-beast category)
- Include both threats and resources (creature products: hides, organs, venom, etc.)
- Creatures visible across different biomes ([[Maren Valley]], [[Wolfpoint]] northern territories, [[Equatorial Desert]])
- Names must follow WORLD_STATE.md conventions (short, terse, Germanic/Nordic descriptors)
- Voice must follow STYLE_GUIDE.md (matter-of-fact, people in motion, practical focus)
- Contemporary war preparation pressure: hunting pressure increasing, creature products becoming strategic resources, traditional hunting territories requisitioned for military use

## Output Target

8-10 notes total:
- 4-6 specific creature types (different biomes, threat levels, resource value)
- 2 hunter/naturalist NPCs (showing professional hunter culture, knowledge specialization)
- 1-2 creature-product trade/hunting culture notes (equipment, safety, economics, contemporary pressures)
- Create [[Creatures]] hub synthesizing ecosystem and hunting cultures
- Link from [[Equatorial Fauna]], [[Maren Valley]], [[Wolfpoint]], settlement pages

## Execution Plan

1. Query navigation cache for Equatorial Fauna context
2. Read Equatorial Fauna page for existing foundation
3. Grep search for existing creature/fauna/hunting references
4. Create 4-6 specific creature type notes (varied biomes, threat levels, products)
5. Create 2 hunter/naturalist NPC profiles (showing field specialization)
6. Create hunting culture note (practical operations, safety, communities)
7. Create creature-product trade note (markets, economics, contemporary pressures)
8. Create [[Creatures]] hub synthesizing ecosystem and human interaction
9. Update Equatorial Fauna with new creature links
10. Link from settlement pages, [[Maren Valley]], [[Wolfpoint]], adventure infrastructure pages
11. Refresh navigation artifacts
12. Mark complete in TASK_QUEUE.md

## Current Step

Preparing to query navigation cache for Equatorial Fauna context...

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
