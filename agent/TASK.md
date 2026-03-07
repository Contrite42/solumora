# Current Task: EXPANSION-015 — Flux Research Institutions

**Status:** In Progress  
**Owner:** Copilot Auto  
**Started:** 2026-03-07

## Goal

Document institutional research into Flux in both Auralis and Terravelle, showing kingdom philosophical differences in how they approach the same questions. Build ground-level detail showing research priorities, grant mechanisms, and how military pressure is reshaping research agendas.

## Constraints

1. **Kingdom philosophical differences:** Auralis treats Flux as technical problem to solve; Terravelle approaches it as natural phenomenon to understand
2. **Institutional pressure:** Both kingdoms redirecting research toward military applications, creating internal institutional conflict
3. **Research institutions (4 minimum):**
   - 2 Auralis research centers (centralized institutional control, military coordination)
   - 2 Terravelle research centers (distributed, guild-affiliated, more autonomy)
4. **Multiple research perspectives:**
   - Pure theoretical researcher focused on fundamental Flux principles
   - Empirical/applied researcher developing practical applications
   - Researcher facing institutional pressure to militarize their work
   - Researcher resisting militarization of their research

## Output Target

6-8 notes total:
- 4 research institution notes (2 Auralis, 2 Terravelle) with funding models, research focus, internal tensions
- 3-4 researcher NPC profiles (T3-T5) showing different research paths and institutional relationships
- 1 update to [[Flux]] hub with "Contemporary Research Directions" section
- Cross-links to [[Grimoires]], [[Education]], [[Economy]], [[The Council of Auralis]], [[Trade Guilds]]

## Key Research Questions

1. What is Auralis researching? (Applications: weapons, industrial efficiency, precision control, military grade materials)
2. What is Terravelle researching? (Understanding: natural principles, sustainability, experimental alternatives, guild-safe applications)
3. How is research funded? (Auralis: Council grants, military contracts; Terravelle: guild contributions, merchant patronage, apprenticeship fees)
4. What institutional relationships shape research? (Military contracts, institutional autonomy, publication restrictions, researcher freedom)
5. What research questions are forbidden or restricted? (Equatorial barrier mechanisms, consciousness aspects of Flux, alternative Flux sources, reverse-engineering pre-collapse artifacts)

## Execution Plan

1. Read [[Flux]] to understand current framework and identify research gaps
2. Research existing Crestward content (what Auralis research is already documented)
3. Identify Terravelle research center anchors (guilds, institutions, individuals)
4. Create 2 Auralis research institution notes with military coordination detail
5. Create 2 Terravelle research institution notes with guild-federation structure
6. Create 3-4 researcher NPC profiles showing diverse research approaches
7. Update [[Flux]] hub with "Contemporary Research Directions" section linking all institutions
8. Cross-link from [[Grimoires]], [[Education]], [[The Council of Auralis]], [[Trade Guilds]]
9. Refresh navigation artifacts
10. Mark complete in TASK_QUEUE.md

## Current Step

Beginning research phase: reading Flux framework and existing research documentation...

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
