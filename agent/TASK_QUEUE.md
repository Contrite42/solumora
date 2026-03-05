# Task Queue

> **Five-agent mode active.** CLI, VSCODE, Claude API, OpenAI, and Ollama all have defined roles.
> Protocol: `agent/COORDINATION.md` — Claims log: `agent/staging/CLAIMED.md`

## AGENT ROLES & COST PROFILE

| Agent | Cost | Role | What it handles |
|-------|------|------|-----------------|
| **Ollama** | Free (local) | Seed + name check | Generates name/rumor seeds; enforces name deduplication against WORLD_STATE |
| **OpenAI gpt-4o-mini** | ~$0.001/call | Planning + ground-level writing | Plans all tasks (JSON); writes ground-level characters, location texture, trade/life content |
| **Claude API claude-opus-4-6** | ~$0.05/call | Complex writing only | Principal characters (KEY_NARRATIVE_THREADS), High Demons, lore mechanics |
| **Claude Code CLI** | Free (sub) | Precision edits + pipeline oversight | Targeted appends, task verification, TASK_QUEUE management, DECISION resolution |
| **Claude Code VS Code** | Free (sub) | Gap checks + backlinks | Reads existing pages, finds gaps, makes small targeted edits, updates See Also |

**Complexity routing in orchestrator.py** (set in PLAN step):
- `"complexity": "ground-level"` → OpenAI writes
- `"complexity": "lore"` → Claude API writes
- `"complexity": "principal"` → Claude API writes
- `FORCE_CLAUDE=1` env var → bypass routing, use Claude for everything (debug)

**Target cost: Claude API used for ≤ 20% of batches per run.**

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

> **Dual-agent work**: Check `agent/staging/CLAIMED.md` before starting. Claim task, do work, log DONE. See `agent/COORDINATION.md` for full protocol.
> Suggested split — CLI: TASK-01 (larger content write). VSCODE: TASK-07, TASK-08 (targeted gap checks and small appends).

- [x] **TASK-01** — `content/Equatorial Desert.md` expansion `[CLI]`
  The existing page is a stub. Write it as a full lore page: what the desert actually feels like, why Halveth exists, what Rift Incursions look like in practice, what the ruins in the desert mean. Dense, sensory, no purple prose. Outbound links: Halveth, Rift Incursions, Flux Demons, Ancient Ruins, Emberfall, Auralis, Terravelle, Ascendant Path, High Demons.
  *(Note: the page has already been substantially expanded in a prior run. Read it first — it may need addition rather than a full rewrite.)*

- [x] **TASK-02** — Update backlinks for pipeline-generated characters (Veld Dorv, Life in Emberfall, and others from current run)
  Check what the pipeline created. Ensure Emberfall, The Advancement Corps, and relevant character pages link back to new pages.

- [x] **TASK-07** — `content/Davan Rhyce.md` gap check `[VSCODE]`
  Davan Rhyce is listed in content/ but not in WORLD_STATE.md's character list. Read the existing page and verify it's canon-consistent. Add to WORLD_STATE.md if missing.
  *(Note: Davan Rhyce IS in WORLD_STATE.md as of 2026-03-05 update. Verify the page matches and mark complete if consistent.)*

- [x] **TASK-08** — `content/Life in Halveth.md` expansion `[VSCODE]`
  Halveth is defined primarily by its garrison and desert proximity. The existing "Life in Halveth" page needs Wren's presence woven in (unnamed, as texture), and the reality of desert-edge life expanded. Reference Selt Orvn and Vorn Teld (Rift Incursion survivor).
  *(Note: this page was substantially expanded in a prior run and already includes Wren, Selt Orvn, and Vorn Teld in the See Also. Read it first — may already be complete.)*

---

## IN PIPELINE — current TASK.md queued

- [x] **TASK-03** — Wolfpoint in motion: append Sera Voss ("The First Test") + append Mira Solv ("The Notification Problem"). Both A+D simultaneously.
- [x] **TASK-04** — Drest current operation: append to Drest page (Option C — academic cover via Culmination ruins research)
- [x] **TASK-05** — Mave Daily Existence rewrite (sibling dynamic; Selvane has genuine warmth for Mave — their only "sweet spot") + minor Selvane update
- [x] **TASK-06** — Sorath in Hedun: append to Sorath page (Option C — passing through, Tolla Rend notices)
- [x] **FIX-1c** — Ostal Mrev corrected consultation notes (Square=8W, single discipline per sigil)

---

## NEXT PIPELINE — Grimoire & Spell Development

- [x] **TASK-12** — Create `content/WrittenWorks/The Zakros Crossing Compendium.md`
  Published survival grimoire. Author: Avel Coss (T4 desert guide) writing from field experience. Curated selection of ~12 spells from Common+Uncommon focused on desert crossing survival: thermal management, air filtration, fauna detection, structural shelter, rift-sign detection. Includes author's notes on which spells degrade under Zakros wind conditions and which to prioritize when reserves are low. Tone: spare, practical, slightly grim. Written Works format.

- [x] **TASK-13** — Create `content/WrittenWorks/Fifteen Sigils for the Young Practitioner.md`
  Educational T1 grimoire, guild-published (Valdenmoor Trade Guild). Not attributed to a single author — guild committee production. 15 T1 spells selected for teaching sequence, with margin notes from a specific copy owner (a parent? an apprentice master?). Notes on common errors, safety, which to teach first. The copy we see has been annotated by hand. Tone: pedagogical but human. Written Works format.

- [x] **TASK-14** — Append new spell entries to `content/All Grimoire.md` and relevant tier pages
  Add 6-8 new spells that fill obvious gaps:
  - **Dustlock** (T2): Chemical discipline, keeps particulate out of sigil surfaces and book pages. Critical for Zakros use.
  - **Heatshield** (T2): Heat discipline, sustained personal thermal buffering. More robust version of Warmbreath.
  - **Faunaread** (T2): Raw discipline, detects Flux signatures of living creatures in a sphere. Desert fauna detection.
  - **Waterward** (T2): Chemical discipline, seals a surface against water penetration permanently.
  - **Distressflag** (T3): Heat + Linked targeting — monitors a marked person's thermal state at distance. Expedition safety spell.
  - **Riftsense** (T3): Raw discipline, detects dimensional instability / rift formation probability in an area. Uncommon tier.
  Each entry must follow All Grimoire table format exactly. Watt costs must be calculated correctly per the formula.

- [x] **TASK-15** — Create `content/WrittenWorks/Ossal Meln's Workshop Notes.md`
  Ossal Meln (T3 Flux-embedded objects craftsperson, Valdenmoor) developing a new embedded object configuration. Shows iterative process: failed attempt at a combined thermal+light embedded sigil, cost calculation error, revised approach, final working configuration. Tone: craftsperson's notebook, numbers-heavy, brief. This is where new spell development is visible as a process.

---

## FUTURE (not yet scoped)
> For dual-agent runs, split these by scope. Larger content tasks → CLI. Targeted appends and verification → VSCODE. Claim before starting.

- [x] **TASK-09** — Ashford political atmosphere update `[VSCODE]`
  Doss Varn (border guard), Orre Cavlt (cross-border merchant), and Cavel Dorst (merchant house) all see the political shift from ground level. Update their pages or write a "Life in Ashford" expansion reflecting current Expansion Faction pressure.
  *(Note: Doss Varn and Orre Cavlt already had current-state language from prior runs. Appended ## Current Conditions to Cavel Dorst.)*

- [x] **TASK-10** — Cassia: what she actually knows
  Cassia is constrained but she's not passive. What information does she have access to that she hasn't shared? What is she doing with it? Needs a "People in Motion" style append.

- [x] **TASK-11** — Bren Ossve (rural T7) developed
  A T7 practitioner living rurally and declining Path service pressure is one of the world's most interesting tensions. Her page needed significant expansion.

---

## NEXT PIPELINE — Ground-Level Expansion + Narrative Thread Connectors

> **Cost target:** ≤ 2 Claude API calls per run. Claim before starting. Tag complexity in TASK.md when writing pipeline runs.

- [ ] **TASK-16** — `agent/orchestrator.py` rebalance `[CLI]` ✅ DONE 2026-03-05
  Moved planning to OpenAI (gpt-4o-mini). Added complexity routing: ground-level → OpenAI, principal/lore → Claude. Upgraded Claude model to claude-opus-4-6. Added Ollama name-dedup awareness. FORCE_CLAUDE=1 env var for debug override.

- [ ] **TASK-17** — `content/Life in Ashford.md` create `[OPENAI]`
  Ashford is referenced heavily (Cavel Dorst, Doss Varn, Orre Cavlt, Ashford.md) but the Life in Ashford page is likely a stub. Write ground-level texture: port city rhythms, documented vs. undocumented populations, Auralis border crossing as daily reality, what the eastern territory feels like from inside the city. Complexity: ground-level. No principal characters.

- [ ] **TASK-18** — `content/Eastern Coastal Territory.md` create `[OPENAI]`
  The coastal territory north of Ashford absorbed in Eddan's annexation campaign. What life actually looks like there: grey-zone loyalty, Auralis-adjacent shipping, how the communities experience their ambiguous administrative status. Complexity: ground-level. Davan Rhyce is background, not named POV.

- [ ] **TASK-19** — `content/Vorn Teld.md` verify/create `[VSCODE]`
  Referenced in Life in Halveth See Also. Rift Incursion survivor. If page is a stub, expand with: what Vorn survived, how it changed their relationship to the desert edge, what they do now. Complexity: ground-level.

- [ ] **TASK-20** — Sera Voss: the second test `[CLAUDE-API]`
  Sera's page states she discovered Watts = ancient civilization currency. She's building toward a second test. What did the first test actually do? What responded? Append a "The First Response" or "After the Test" section. This is a KEY_NARRATIVE_THREAD move. Complexity: principal.

- [ ] **TASK-21** — Drest + Aldric: what the expeditions are actually finding `[CLAUDE-API]`
  Drest uses Culmination Faction ruins research as cover. Aldric Mourne is finding things that go to Drest's office rather than the Corps archives. What specifically? What did the last expedition find? Append to Aldric Mourne or write `content/WrittenWorks/Aldric Mourne Field Notes.md`. Complexity: principal.

- [ ] **DECISION 5** — `content/People/Bren Ossve.md` duplicate resolution `[CLI]`
  Two pages: canonical T7 female (expanded ✅), pipeline-error T2 male hunter. See DECISIONS.md Decision 5 for options. Recommendation: Option B (rename T2 male hunter to a new valid name). **Needs user decision before CLI can act.**

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
| 2026-03-05 | Pipeline run | All 4 batches approved | TASK-03/04/05/06 + FIX-1c complete. Ostal Mrev duplicate cleaned. |
| 2026-03-05 | TASK-14 | Complete | Added 6 new spells: Dustlock, Warmcloak, Faunaread, Waterward (Common T2); Distressflag, Riftsense (Uncommon T3). Note: task spec named T2 "Heatshield" but T4 Heatshield already exists — renamed to Warmcloak to avoid conflict. |
| 2026-03-05 | TASK-12 | Complete | Created content/WrittenWorks/The Zakros Crossing Compendium.md. 12 spells, author notes on degradation conditions and reserve priorities. |
| 2026-03-05 | TASK-13 | Complete | Created content/WrittenWorks/Fifteen Sigils for the Young Practitioner.md. 15 T1 spells in teaching sequence, annotated copy with parent's margin notes. |
| 2026-03-05 | TASK-15 | Complete | Created content/WrittenWorks/Ossal Meln's Workshop Notes.md. Failed combined thermal/light attempt, interference analysis, revised two-object solution. |
| 2026-03-05 | TASK-02 | Complete | Backlinks updated: Emberfall +Veld Dorv +Aldric Mourne; Avel Coss +Zakros Crossing Compendium; Equatorial Desert +Emberfall +Ascendant Path +High Demons; Ossal Meln +Workshop Notes. |
| 2026-03-05 | Coordination | Setup | Created COORDINATION.md + staging/CLAIMED.md for dual-agent (CLI + VSCODE) parallel workflow. TASK_QUEUE updated with agent tags and protocol header. |
| 2026-03-05 | TASK-01 | Complete | Added ## Halveth and the Crossing Economy to Equatorial Desert.md. Who crosses, who can afford it, Auralis institutional funding, Ascendant Path credential incentive, Terravelle self-financing merchants, solo crossings by unspecified means (High Demon texture without naming). |
| 2026-03-05 | TASK-07 | Verified | Davan Rhyce page canon-consistent: T4, Expansion Faction, eastern coastal territory work, Brennan Solce relationship. No edits needed. |
| 2026-03-05 | TASK-08 | Verified | Life in Halveth confirmed complete from prior run: Wren woven in, rift section, children section, full off-season texture. No edits needed. |
| 2026-03-05 | TASK-09 | Complete | Appended ## Current Conditions to Cavel Dorst.md. Selective border friction, client predictability pressure, limits of what he can report upward. Added Davan Rhyce + Orre Cavlt to See Also. |
| 2026-03-05 | TASK-10 | Complete | Appended ## What She Carries to Cassia.md. Council observation model, library-based self-training, one council member identified as personally motivated. Added Castor Helme to See Also. |
| 2026-03-05 | TASK-11 | Complete | Expanded Bren Ossve.md substantially. T7/farm gap, ongoing pressure management, Covenant as tool not doctrine, community knowledge settling over 40 years, unwritten case knowledge and ambivalence, longevity applications unused and the unanswered question. Added Ascendant Path to See Also. |
