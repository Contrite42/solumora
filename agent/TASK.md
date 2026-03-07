# Current Task: WORLD ROUNDING — Terravelle Governance Mechanics

**Status:** In Progress  
**Owner:** Copilot Auto  
**Started:** 2026-03-07

## Objective

Build Terravelle governance mechanics to parity with Auralis council detail. Auralis has operational governance pages (Council Orders Registry, Council Compliance Directorate, Council Review Board); Terravelle needs matching bureaucratic depth showing order routing, enforcement, compliance review, and field implementation.

## Requirements

- 5-7 institutional pages (registries, enforcement units, review offices)
- 3-4 implementer NPC pages showing field-level governance work
- Append Terravelle governance-operations section to Terravelle Administration.md
- No principal-character retcons
- Maintain Terravelle's distributed guild-based model (not centralized like Auralis)
- Show operational mechanics, recurring actors, and failure modes

## Target Institutions

Based on Terravelle's guild-coordinated distributed governance:

1. **Guild Coordination Office** — Inter-guild policy coordination and dispute mediation
2. **Crown Compliance Monitor** — Field verification of Crown directive implementation
3. **Settlement Registry Network** — Population tracking, birth runes, practitioner certification
4. **Guild Arbitration Bench** — Cross-guild commercial dispute resolution
5. **Crown-Guild Liaison Office** — Communication bridge between Wolfpoint and guild councils
6. Additional institutions as needed for parity

## Deliverables

- [ ] 5-7 governance institution pages
- [ ] 3-4 implementer NPC pages
- [ ] Terravelle Administration.md governance section appended
- [ ] Cross-linking complete
- [ ] Navigation artifacts refreshed

## Deliverables ✓

**All 9 Bridge Concept Pages Expanded:**

1. **Kingdoms.md** (~230 lines) — Shared systems (language, currency, Control Tier, grimoire structure), governance contrasts (Auralis centralized vs Terravelle horizontal), recurring conflicts (border friction, trade route competition, resource access), failure modes (communication breakdown, escalation without intent, institutional commitment traps), wartime pressure impacts showing divergence

2. **Guilds.md** (~260 lines) — Guild types (Trade, Scrivener, specialty), kingdom differences (Auralis supervised vs Terravelle autonomous), certification systems (apprenticeship → journeyman → assessment), documentation standards and failure modes, wartime pressure (practitioner conscription, material scarcity, institutional capture risk)

3. **Infrastructure.md** (~280 lines) — Physical networks and administrative systems, maintenance practitioners and cost structures, failure modes (cascade failures, capacity collapse, administrative breakdown, maintenance death spirals), wartime degradation and deferred maintenance accumulation

4. **Border Trade.md** (~320 lines) — Inspection mechanics (documentation requirements, physical inspection, Flux-detection), enforcement personnel (Sorn Veld and customs operations), smuggling methods (document cover, timing exploitation), failure modes (inspection overload, documentation breakdown, enforcement asymmetry), wartime escalation patterns

5. **Cross-Border Trade.md** (~340 lines) — Network requirements (merchant houses, guild coordination, relationship maintenance), documentation complexity, specific trade routes (Ashford-Halveth corridor, maritime circuits, northern coastal), merchant operations, failure modes (relationship breakdown, documentation divergence, enforcement unpredictability), wartime impacts

6. **Cross-Border Commerce.md** (~320 lines) — Merchant house operations, payment systems (letters of credit, authentication, currency verification), dispute resolution through guild arbitration, trust networks and reputation, wartime degradation (relationship strain, merchant withdrawal, trust system collapse, payment fragility)

7. **Political Dynamics.md** (~350 lines) — Factional alignments (Auralis Council factions vs Terravelle distributed power), resource allocation patterns, information access controls (hierarchical vs distributed), voting patterns and informal coordination, alliance/betrayal patterns, wartime acceleration

8. **Political Intelligence.md** (~380 lines) — Collection methods (customs surveillance, message interception, document analysis by Cassia, merchant networks, institutional reporting), pattern recognition (voting analysis, resource shifts, communication volume, behavioral patterns), constraints on use (positional, institutional, relationship, evidence standards), intelligence asymmetries, wartime escalation

9. **Council Dynamics.md** (~370 lines) — Factional coordination (pre-session coordination, sustained alliances, minority faction influence), agenda control (setting authority, emergency sessions, information timing), voting mechanics, informal networks, implementation chain (Registry → Compliance → Review Board), external pressure integration, wartime acceleration dynamics

**Cross-Linking:**

All 9 pages include comprehensive cross-references to each other and operational content. Each page has 15-20 outbound links integrating bridge concepts with existing world systems.

**Navigation:**

- Concept-graph: 671 nodes (+2 from 669), 7247 edges (+318 from 6929), 563 pages
- Context-index: 563 pages
- Growth reflects extensive cross-linking within bridge concept pages

**Recurring Actors Integrated:**

Sorn Veld (T3 Ashford customs coordinator), Cavel Dorst (merchant house coordinator), Vessa Rolt (Registry Coordinator), Torn Hess (Compliance Directorate), Helva Drost (Review Board chair), Cassia (intelligence documentation), Drest (factional coordination), Eddan Voss (Terravelle Crown), Varn Kest (infrastructure maintenance), Osvin Brack (guild assessor), Lorn Kess (operational worker), Maren Sollis (Council member), Tovan Ashce (strategic voting), Casten Miel (research director), Marn Drest (Timber Collective coordinator)

**Failure Modes Documented:**

Cascade failures, capacity collapse, relationship breakdown, documentation gaps, enforcement overload, administrative bottlenecks, maintenance death spirals, trust system collapse, payment fragility, intelligence overload, deliberative space collapse, irreversible commitments

**Wartime Pressure Themes:**

Historical near-war pattern recognition throughout all pages, showing current conditions matching escalation patterns from previous crises. Documentation of resource constraints, practitioner conscription impacts, institutional degradation, and projected breakdown timelines matching established precedents.

---

## Next Task

Ready for next task assignment from TASK_QUEUE.md.

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
