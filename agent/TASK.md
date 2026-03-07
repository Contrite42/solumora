# Active Task: EXPANSION-013 - Currency & Banking

**Status:** NOT STARTED
**Owner:** Copilot
**Started:** 2026-03-07

## Goal

Define money systems, banking institutions, credit mechanisms, and cross-kingdom financial exchange. Show how Flux affects finance (detection, verification, transportation security). Include both formal banks and informal lending.

## Constraints

- Two kingdoms may have different currencies
- Flux affects financial systems (protective measures, verification, security)
- Show both institutional (banks, formal credit) and informal (lending, debt-bonding) systems
- Financial systems under war preparation pressure: institutional funding crises, currency instability, credit system strain, institutional prioritization of military funding over economic support
- Names must follow WORLD_STATE.md conventions (short, terse, Germanic/Nordic descriptors)
- Voice must follow STYLE_GUIDE.md (matter-of-fact, people in motion, practical operational focus)
- Contemporary war pressure: military requisitions straining institutional funding, institutional lending predatory toward civilian ventures, currency instability from military resource exploitation, credit collateral demands inflated from institutional competition

## Output Target

5-7 notes total:
- 1-2 currency system notes defining money types, denominations, verification mechanisms
- 1-2 banking institution notes (formal banks, institutional structures, credit mechanisms)
- 1-2 informal lending/credit system notes (debt-bonding, money-lenders, alternative financing)
- 1-2 financier/banker NPCs showing different relationship approaches to institutional/civilian economy
- Create [[Economy]] hub synthesizing financial systems with broader resource management
- Update [[Solumora]], [[Auralis]], [[Terravelle]] with financial infrastructure references

## Execution Plan

1. Query navigation cache for Currency, Banking, Economy context
2. Read [[Grimoire Economy]] and [[Trade & Travel]] for existing financial infrastructure foundation
3. Grep search for existing banker/merchant/wealth references
4. Create 1-2 currency system notes (denominations, verification, Flux security, cross-kingdom exchange)
5. Create 1-2 banking institution notes (formal banks, credit structures, institutional relationships)
6. Create 1-2 informal lending notes (alternative financing, debt systems, protection mechanisms)
7. Create 1-2 financier NPC profiles showing institutional vs. civilian economy positioning
8. Create [[Economy]] hub synthesizing all financial content with broader economic systems
9. Update [[Solumora]], [[Auralis]], [[Terravelle]] with finance/banking references
10. Refresh navigation artifacts
11. Mark complete in TASK_QUEUE.md

## Current Step

Ready to query navigation cache for Currency/Banking context...

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
