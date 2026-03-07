# Active Task: EXPANSION-008 - Arts & Entertainment

**Status:** IN PROGRESS
**Owner:** Copilot
**Started:** 2026-03-07

## Goal

Show what people do for leisure, beauty, and cultural expression (theater, music, visual arts, sports/competitions, festivals).

## Constraints

- Flux enables some art forms (illusion theater, light sculpture, sound manipulation)
- Art reflects power dynamics (who commissions, who performs, who watches)
- Include both high culture (noble patronage) and common culture (street performers, tavern music)
- Show regional differences (Auralis innovation-focused vs Terravelle traditional)
- Names must follow WORLD_STATE.md conventions (short, terse, Germanic/Nordic)
- Voice must follow STYLE_GUIDE.md (matter-of-fact, people in motion)
- Existing canon: Settlement pages mention festivals, celebrations, social gatherings

## Output Target

7-9 notes total:
- Art forms overview (theater, music, visual arts, Flux-enhanced performance)
- Major venues (theaters, performance spaces, galleries)
- Festivals and celebrations (seasonal events, kingdom holidays, local traditions)
- Competitions and sports (physical contests, flux demonstrations, gambling)
- 2-3 artist/performer NPC notes
- Create [[Arts & Culture]] hub page

## Execution Plan

1. Query navigation cache for arts/entertainment context (festivals, celebrations, settlements)
2. Read settlement pages for existing cultural references
3. Design art forms (theater, music, visual arts, Flux-enhanced performance)
4. Identify major venues in major settlements (Solhaven, Valdenmoor, Wolfpoint)
5. Create festival and celebration notes (seasonal, political, religious)
6. Design competition and sports notes (physical contests, Flux demonstrations)
7. Create 2-3 NPC notes (performers, artists, venue operators)
8. Create Arts & Culture hub page
9. Link from kingdom/settlement pages
10. Refresh navigation artifacts
11. Mark complete in TASK_QUEUE.md

## Current Step

Preparing to query navigation cache for arts and entertainment context...

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
