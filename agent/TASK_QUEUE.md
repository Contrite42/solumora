# Task Queue

## ✅ FOREVER TASK — Canon + Links Integrity (Run Every Cycle)

- [ ] **Goal:** Maintain world coherence and navigability after every content expansion.
- **Constraints:**
  - **Backlinks:** Every new or updated note must be reachable from at least one appropriate hub page (ex: [[Solumora]], [[Auralis]], [[Terravelle]], [[Desert Zakros]], [[Flux]], [[Grimoires]], [[Factions]], [[Religions]], [[History]], [[People]]).
  - **No Orphans:** No new note should exist without at least **3 outbound links** and at least **1 inbound link** from a hub or parent topic.
  - **No “Admin” leaks:** Do not link to hidden/administrative pages that would spoil discovery for a reader (avoid meta-control pages in adventure-facing reading paths).
  - **History coherence:** No timeline contradictions (dates, causality, travel times, tech/magic progression). If a contradiction is found, record it as a flagged issue rather than silently rewriting canon.
  - **Geography coherence:** No impossible travel routes (equator crossing rules, climate belts, distance logic). Anything that violates [[Solumora]]’s geography must be corrected or explicitly marked as “rare/mage-only.”
  - **Magic coherence:** No spellcasting contradictions (Flux limits, Tier rules, misbehavior on failure, exponential cost). If a page violates these, flag it.
- **Output (every cycle):**
  - Update backlink structure and hub pages as needed (append-only blocks).
  - Write/update: `agent/reports/inconsistencies.md`
  - Write/update: `agent/reports/links_applied.md`
  - If contradictions require a decision: write options to `agent/DECISIONS.md` and stop.

  
Tasks in priority order. Check off when done. Add next steps as discovered.
Blocked tasks are marked with their dependency.


- [ ] **Goal:** Create the **Trade & Travel spine** of Solumora (routes, nodes, risks, costs).  
  **Constraints:** Must explain how people move goods/info between [[Terravelle]], [[Auralis]], [[Wolfpoint]], and around [[Desert Zakros]]. Include courier, river, coastal, and overland systems. Everyone is mid-journey.  
  **Output:** 10 new notes (routes + hubs) + update [[Solumora]] + update [[World Primer]] with a “How people move” section.

- [ ] **Goal:** Define the **Equatorial Crossing Economy** as a lived reality, not lore.  
  **Constraints:** Crossing is rare; only grimoires/mages/extreme resistance. Build 3 crossing methods, 3 failure modes, and 3 organizations that profit from it. Everyone mid-journey.  
  **Output:** 8 notes (3 orgs, 3 methods, 2 key crossing sites) + update [[Desert Zakros]].

- [ ] **Goal:** Build the **Grimoire Economy** (copying, licensing, fraud, black markets).  
  **Constraints:** Flux cost exponential; most are low-tier; society optimizes low-cost spells. Show how grimoires spread power without creating a caste.  
  **Output:** 10 notes (guilds, copyists, regulation, black market, “common grimoire” tiers) + update [[Grimoires]].

- [ ] **Goal:** Create the **Factions hub** and populate it with real institutions.  
  **Constraints:** Factions must have logistics: funding, recruitment, rules, enemies, and what they trade in (information, grimoires, routes, protection).  
  **Output:** 1 hub note [[Factions]] + 12 faction notes + link each into relevant kingdom pages.

- [ ] **Goal:** Create the **Religion hub** tied to Flux + the equator barrier.  
  **Constraints:** 3–5 religions. Each must have: core doctrine, rituals, taboo, political relationship to grimoires, and how common people practice it.  
  **Output:** [[Religions]] hub + 5 religion notes + update [[Solumora]].

- [ ] **Goal:** Make **Auralis** feel like a place by building 1 capital city + 3 districts + the people moving inside them.  
  **Constraints:** Dense urban basin, engineered with Flux. Each district must have its own economy + social pressure + recurring NPCs.  
  **Output:** 8 notes (capital + districts + 4 people) + update [[Auralis]].

- [ ] **Goal:** Make **Terravelle** feel like a place by building 1 northern megacity + 3 districts + rural supply chain feeding it.  
  **Constraints:** Rural/pragmatic kingdom; Flux as trade skill. City must depend on farms/river valleys and trade.  
  **Output:** 8 notes (megacity + districts + rural supply chain + 3 people) + update [[Terravelle]].

- [ ] **Goal:** Integrate [[Wolfpoint]] / [[Hypertext]] into the geopolitical world as a third pole, not a lore island.  
  **Constraints:** Why it matters, who wants it, what it exports, what it refuses, what it fears. Everyone has a personal stake.  
  **Output:** 6 notes (institutions + exports + conflicts + 3 people) + update [[Wolfpoint]] + update [[Hypertext]].

- [ ] **Goal:** Build the **timeline backbone** of Solumora (eras that explain current institutions).  
  **Constraints:** Must explain why the equator became uninhabitable, how grimoires spread, and how Terravelle/Auralis diverged culturally.  
  **Output:** [[History]] hub + 8 era notes + add timeline section to [[Solumora]].

- [ ] **Goal:** Make “everyone mid-journey” structurally real: create **People Web Index** + minimum viable cast.  
  **Constraints:** 30 people. Every person must link to 3–6 others. Include smugglers, copyists, guards, farmers, priests, couriers, and 2–3 high-tier isolates.  
  **Output:** [[People]] hub + 30 people notes + update 5 major hubs with “People in Motion” sections.
---

## IMMEDIATE (no decisions needed)

- [ ] **TASK-01** — Write `content/Equatorial Desert.md` expansion
  The existing page is a stub. Write it as a full lore page: what the desert actually feels like, why Halveth exists, what Rift Incursions look like in practice, what the ruins in the desert mean. Dense, sensory, no purple prose. Outbound links: Halveth, Rift Incursions, Flux Demons, Ancient Ruins, Emberfall, Auralis, Terravelle, Ascendant Path, High Demons.

- [ ] **TASK-02** — Update backlinks for pipeline-generated characters (Veld Dorv, Life in Emberfall, and others from current run)
  Check what the pipeline created. Ensure Emberfall, The Advancement Corps, and relevant character pages link back to new pages.

- [ ] **TASK-07** — Write `content/Davan Rhyce.md` gap check
  Davan Rhyce is listed in content/ but not in WORLD_STATE.md's character list. Read the existing page and verify it's canon-consistent. Add to WORLD_STATE.md if missing.

- [ ] **TASK-08** — Write `content/Life in Halveth.md` expansion
  Halveth is defined primarily by its garrison and desert proximity. The existing "Life in Halveth" page needs Wren's presence woven in (unnamed, as texture), and the reality of desert-edge life expanded. Reference Selt Orvn and Vorn Teld (Rift Incursion survivor).

---

## IN PIPELINE — current TASK.md queued

- [ ] **TASK-03** — Wolfpoint in motion: append Sera Voss ("The First Test") + append Mira Solv ("The Notification Problem"). Both A+D simultaneously.
- [ ] **TASK-04** — Drest current operation: append to Drest page (Option C — academic cover via Culmination ruins research)
- [ ] **TASK-05** — Mave Daily Existence rewrite (sibling dynamic; Selvane has genuine warmth for Mave — their only "sweet spot") + minor Selvane update
- [ ] **TASK-06** — Sorath in Hedun: append to Sorath page (Option C — passing through, Tolla Rend notices)
- [ ] **FIX-1c** — Ostal Mrev corrected consultation notes (Square=8W, single discipline per sigil)

---

## NEXT PIPELINE — Grimoire & Spell Development

- [ ] **TASK-12** — Create `content/WrittenWorks/The Zakros Crossing Compendium.md`
  Published survival grimoire. Author: Avel Coss (T4 desert guide) writing from field experience. Curated selection of ~12 spells from Common+Uncommon focused on desert crossing survival: thermal management, air filtration, fauna detection, structural shelter, rift-sign detection. Includes author's notes on which spells degrade under Zakros wind conditions and which to prioritize when reserves are low. Tone: spare, practical, slightly grim. Written Works format.

- [ ] **TASK-13** — Create `content/WrittenWorks/Fifteen Sigils for the Young Practitioner.md`
  Educational T1 grimoire, guild-published (Valdenmoor Trade Guild). Not attributed to a single author — guild committee production. 15 T1 spells selected for teaching sequence, with margin notes from a specific copy owner (a parent? an apprentice master?). Notes on common errors, safety, which to teach first. The copy we see has been annotated by hand. Tone: pedagogical but human. Written Works format.

- [ ] **TASK-14** — Append new spell entries to `content/All Grimoire.md` and relevant tier pages
  Add 6-8 new spells that fill obvious gaps:
  - **Dustlock** (T2): Chemical discipline, keeps particulate out of sigil surfaces and book pages. Critical for Zakros use.
  - **Heatshield** (T2): Heat discipline, sustained personal thermal buffering. More robust version of Warmbreath.
  - **Faunaread** (T2): Raw discipline, detects Flux signatures of living creatures in a sphere. Desert fauna detection.
  - **Waterward** (T2): Chemical discipline, seals a surface against water penetration permanently.
  - **Distressflag** (T3): Heat + Linked targeting — monitors a marked person's thermal state at distance. Expedition safety spell.
  - **Riftsense** (T3): Raw discipline, detects dimensional instability / rift formation probability in an area. Uncommon tier.
  Each entry must follow All Grimoire table format exactly. Watt costs must be calculated correctly per the formula.

- [ ] **TASK-15** — Create `content/WrittenWorks/Ossal Meln's Workshop Notes.md`
  Ossal Meln (T3 Flux-embedded objects craftsperson, Valdenmoor) developing a new embedded object configuration. Shows iterative process: failed attempt at a combined thermal+light embedded sigil, cost calculation error, revised approach, final working configuration. Tone: craftsperson's notebook, numbers-heavy, brief. This is where new spell development is visible as a process.

---

## FUTURE (not yet scoped)

- [ ] **TASK-09** — Ashford political atmosphere update
  Doss Varn (border guard), Orre Cavlt (cross-border merchant), and Cavel Dorst (merchant house) all see the political shift from ground level. Update their pages or write a "Life in Ashford" expansion reflecting current Expansion Faction pressure.

- [ ] **TASK-10** — Cassia: what she actually knows
  Cassia is constrained but she's not passive. What information does she have access to that she hasn't shared? What is she doing with it? Needs a "People in Motion" style append.

- [ ] **TASK-11** — Bren Ossve (rural T7) developed
  A T7 practitioner living rurally and declining Path service pressure is one of the world's most interesting tensions. His page likely needs significant expansion.

---

## WORKLOG

| Date | Task | Action | Notes |
|------|------|---------|-------|
| 2026-03-05 | Setup | Created TASK_QUEUE.md and DECISIONS.md | Pipeline running current TASK.md batch |
| 2026-03-05 | Pipeline review | Approved Batch 2 | Veld Dorv + Selvane Daily Existence. Maren Sollis added to WORLD_STATE |
| 2026-03-05 | Pipeline review | Rejected Batch 3 | Mave/Selvane both "infrastructure consultant" — role conflict |
| 2026-03-05 | Pipeline review | Approved Batch 4 | Wren Daily Existence + Osvin Brack Watt entries. All correct. |
| 2026-03-05 | Pipeline review | Approved Batch 5 | Rell Hadv + Toven Ral Watt entries. Both correct. |
| 2026-03-05 | Pipeline review | Rejected Batch 6 | Ostal Mrev formula errors: Square=4W (should be 8W), two disciplines applied simultaneously, invented scale modifier |
| 2026-03-05 | WORLD_STATE | Updated | Added Davan Rhyce, Maren Sollis, Castor Helme, Yara Venn, Brennan Solce, Orla Fest |
| 2026-03-05 | DECISIONS | All 4 resolved | D1: Both A+D. D2: Mave orbits Selvane socially. D3: Option C academic cover. D4: Option C Hedun. |
| 2026-03-05 | TASK.md | Written | Fix pipeline failures + 4 unblocked narrative tasks. Ready to run. |
