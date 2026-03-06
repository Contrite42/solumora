# Task Queue
Permanant Task: The World Always Needs More. There is Always something to add a new adventure to play out in this world, a new friend, a new town, a new spell, a new description. There will always be more.

Whenever human interaction is needed, pop open a GUI that I can respond in

develop a method of file traversal more AI efficient that All three High level Agents can use.

e## CONCURRENT AGENT OWNERSHIP (ACTIVE)

Use this split while Codex and Copilot Auto run simultaneously (`Claude Code` currently offline).

- `Codex` (control plane owner): only agent allowed to edit `agent/TASK_QUEUE.md`, `agent/TASK.md`, `agent/COORDINATION.md`, `agent/DECISIONS.md`, and `agent/staging/CLAIMED.md`.
- `Claude Code` (core content lane): OFFLINE. Do not assign new active tasks until back online.
- `Copilot Auto` (content plus integrity lane): handles assigned content/story tasks, runs canon/link QA, and updates `agent/reports/inconsistencies.md` plus `agent/reports/links_applied.md`.
- Shared staging note: all agents may append status notes to `agent/staging/PENDING_REVIEW.md` using prefix `[Agent][YYYY-MM-DD HH:MM]`.
- Conflict rule: if another agent is already editing a file, stop and hand off through `agent/staging/PENDING_REVIEW.md` instead of writing.
- Assignment rule: only `Codex` may change task ownership labels in this queue.

## CURRENT REVIEW GATE (DO THIS FIRST)

- [x] **Operator decision first** - Resolve routine review outcomes without creator input.
  **How:** For low-impact batches, operators set `Active Review Decision` status directly.
  **Reject case:** If invalid links/canon mismatches appear, reject with fix notes and rerun.
  **Owner:** `Codex`
  **Status note:** Batch 2 was escalated correctly due principal-character scope (`content/Cassia.md`).

- [x] **Creator escalation only when needed**
  **Escalate only for:** world structure, core storyline, principal characters, or major events.
  **Format:** Write creator decision in `agent/DECISIONS.md` with at least 3 options (A/B/C).
  **Done when:** creator sets chosen option in `agent/DECISIONS.md`.
  **Owner:** `Codex`
  **Status note:** Batch 2 decision recorded as `APPROVED` in `agent/DECISIONS.md`; review gate cleared.
---
## âœ… FOREVER TASK â€” Canon + Links Integrity (Run Every Cycle)

- [ ] **Goal:** Maintain world coherence and navigability after every content expansion.
  **Owner:** `Copilot Auto` (default), `Codex` (fallback)
- **Constraints:**
  - **Backlinks:** Every new or updated note must be reachable from at least one appropriate hub page (ex: [[Solumora]], [[Auralis]], [[Terravelle]], [[Desert Zakros]], [[Flux]], [[Grimoires]], [[Factions]], [[Religions]], [[History]], [[People]]).
  - **No Orphans:** No new note should exist without at least **3 outbound links** and at least **1 inbound link** from a hub or parent topic.
  - **No â€œAdminâ€ leaks:** Do not link to hidden/administrative pages that would spoil discovery for a reader (avoid meta-control pages in adventure-facing reading paths).
  - **History coherence:** No timeline contradictions (dates, causality, travel times, tech/magic progression). If a contradiction is found, record it as a flagged issue rather than silently rewriting canon.
  - **Geography coherence:** No impossible travel routes (equator crossing rules, climate belts, distance logic). Anything that violates [[Solumora]]â€™s geography must be corrected or explicitly marked as â€œrare/mage-only.â€
  - **Magic coherence:** No spellcasting contradictions (Flux limits, Tier rules, misbehavior on failure, exponential cost). If a page violates these, flag it.
- **Output (every cycle):**
  - Update backlink structure and hub pages as needed (append-only blocks).
  - Write/update: `agent/reports/inconsistencies.md`
  - Write/update: `agent/reports/links_applied.md`
  - If contradictions require a decision: write options to `agent/DECISIONS.md` and stop.

  
Tasks in priority order. Check off when done. Add next steps as discovered.
Blocked tasks are marked with their dependency.


- [x] **Goal:** Create the **Trade & Travel spine** of Solumora (routes, nodes, risks, costs).
  **Constraints:** Must explain how people move goods/info between [[Terravelle]], [[Auralis]], [[Wolfpoint]], and around [[Desert Zakros]]. Include courier, river, coastal, and overland systems. Everyone is mid-journey.
  **Output:** 10 new notes (routes + hubs) + update [[Solumora]] + update [[World Primer]] with a â€œHow people moveâ€ section.

- [x] **Goal:** Define the **Equatorial Crossing Economy** as a lived reality, not lore.
  **Constraints:** Crossing is rare; only grimoires/mages/extreme resistance. Build 3 crossing methods, 3 failure modes, and 3 organizations that profit from it. Everyone mid-journey.
  **Output:** 8 notes (3 orgs, 3 methods, 2 key crossing sites) + update [[Desert Zakros]].

- [x] **Goal:** Build the **Grimoire Economy** (copying, licensing, fraud, black markets).
  **Constraints:** Flux cost exponential; most are low-tier; society optimizes low-cost spells. Show how grimoires spread power without creating a caste.
  **Output:** 10 notes (guilds, copyists, regulation, black market, â€œcommon grimoireâ€ tiers) + update [[Grimoires]].

- [x] **Goal:** Create the **Factions hub** and populate it with real institutions.  
  **Constraints:** Factions must have logistics: funding, recruitment, rules, enemies, and what they trade in (information, grimoires, routes, protection).  
  **Output:** 1 hub note [[Factions]] + 12 faction notes + link each into relevant kingdom pages.

- [x] **Goal:** Create the **Religion hub** tied to Flux + the equator barrier.  
  **Constraints:** 3â€“5 religions. Each must have: core doctrine, rituals, taboo, political relationship to grimoires, and how common people practice it.  
  **Output:** [[Religions]] hub + 5 religion notes + update [[Solumora]].

- [x] **Goal:** Make **Auralis** feel like a place by building 1 capital city + 3 districts + the people moving inside them.  
  **Constraints:** Dense urban basin, engineered with Flux. Each district must have its own economy + social pressure + recurring NPCs.  
  **Output:** 8 notes (capital + districts + 4 people) + update [[Auralis]].

- [x] **Goal:** Clarify Zakros crossing access limits for low tiers in world-facing pages.
  **Constraints:** Establish explicitly that [[Control Tier|Tier 1]] and [[Control Tier|Tier 0]] travelers cannot break into the active Flux zone around [[Desert Zakros]], which is one reason crossings require specialist support. Keep all existing crossing methods canon-consistent. No new factions, characters, or named locations.
  **Output:** Append clarifying language to existing desert crossing pages (minimum: [[Equatorial Desert]] plus two crossing-method/site notes) and add/verify at least one hub backlink.
  **Escalation note:** If scope expands to `content/Solumora.md` or `content/World Primer.md`, create a `agent/DECISIONS.md` escalation entry first.
  **Owner:** `Claude Code`

- [x] **Goal:** Preflight Terravelle canon-touch escalation before city buildout.
  **Constraints:** `content/Terravelle.md` is a protected major canon file and cannot be edited directly without creator-facing escalation. Do not write Terravelle content in this task.
  **Output:** Add `A/B/C` Terravelle scope options in `agent/DECISIONS.md` and define what can proceed before creator choice.
  **Owner:** `Codex`
  **Dependency:** Must be completed before the Terravelle megacity task below.

- [x] **Goal:** Make **Terravelle** feel like a place by building 1 northern megacity + 3 districts + rural supply chain feeding it.  
  **Constraints:** Rural/pragmatic kingdom; Flux as trade skill. City must depend on farms/river valleys and trade.  
  **Output:** 8 notes (megacity + districts + rural supply chain + 3 people) + update [[Terravelle]].
  **Owner:** `Copilot Auto` (temporary while Claude offline)

- [x] **Goal:** Integrate [[Wolfpoint]] / [[Hypertext]] into the geopolitical world as a third pole, not a lore island.  
  **Constraints:** Why it matters, who wants it, what it exports, what it refuses, what it fears. Everyone has a personal stake.  
  **Output:** 6 notes (institutions + exports + conflicts + 3 people) + update [[Wolfpoint]] + update [[Hypertext]].
  **Owner:** `Copilot Auto` (temporary while Claude offline)

- [x] **Goal:** Build the **timeline backbone** of Solumora (eras that explain current institutions).  
  **Constraints:** Must explain why the equator became uninhabitable, how grimoires spread, and how Terravelle/Auralis diverged culturally.  
  **Output:** [[History]] hub + 8 era notes + add timeline section to [[Solumora]].
  **Owner:** `Copilot Auto` (temporary while Claude offline)

- [x] **Goal:** Add a live map of Solumora with canonical positioning to the Solumora page.
  **Constraints:** Use existing world descriptions for relative placement (north Terravelle uplands, equatorial Zakros barrier, southern Auralis basin, far-north Wolfpoint). Do not edit protected canon content files directly.
  **Output:** Quartz component + script + styles (`quartz/components/SolumoraMap.tsx`, `quartz/components/scripts/solumoraMap.inline.ts`, `quartz/components/styles/solumoraMap.scss`) and layout wiring in `quartz.layout.ts`.
  **Owner:** `Codex`

- [x] **Goal:** Expand `content/The Bone Sea.md` from stub to usable travel/canon note.
  **Constraints:** Append-only to existing page. No new kingdoms/factions. Anchor it to existing route and risk systems; include at least 3 outbound links and a See Also block.
  **Output:** Expanded `content/The Bone Sea.md` plus at least one inbound-link append from a relevant existing hub/page.
  **Owner:** `Copilot Auto`

- [x] **Goal:** Resolve remaining spell-structure stubs and preserve glossary coherence.
  **Constraints:** `Binding.md`, `Pattern.md`, and `Filter.md` are currently zero-byte placeholders. Convert each into concise canon glossary notes aligned with existing spell-variable vocabulary; no contradictory mechanics.
  **Output:** Three populated glossary pages + inbound mentions from at least one anchor page (prefer [[Spell Variables]] or [[Spells]]).
  **Owner:** `Copilot Auto`

- [x] **Goal:** Stabilize legacy alias links introduced by older batches.
  **Constraints:** Run targeted alias cleanup for `Culmination Faction`/`The Culmination Faction`, `Persecution Era`/`The Persecution Era`, and similar known drift without changing narrative meaning.
  **Output:** Low-impact link fixes across touched files + report entry in `agent/reports/inconsistencies.md`.
  **Owner:** `Copilot Auto`

- [x] **Goal:** Make â€œeveryone mid-journeyâ€ structurally real: create **People Web Index** + minimum viable cast.
  **Constraints:** 30 people. Every person must link to 3â€“6 others. Include smugglers, copyists, guards, farmers, priests, couriers, and 2â€“3 high-tier isolates.
  **Output:** [[People]] hub + 30 people notes + update 5 major hubs with â€œPeople in Motionâ€ sections.
  **Owner:** `Copilot Auto` (temporary while Claude offline)

- [x] **Goal:** Write Ashford informal-economy story from the Maria seed as canon short fiction.
  **Constraints:** Story must be grounded in existing Ashford systems (registration, documentation, guild/city pressure) and current world tone. If `Maria` is used, treat as one-off story viewpoint only (no automatic new profile page). No out-of-world analysis section in final story file.
  **Output:** `content/Stories/Ashford False Papers.md` (800â€“1200 words) with at least 3 outbound wikilinks and a final See Also block.
  **Owner:** `Copilot Auto`

- [x] **Goal:** Generate broad story-option slate (specific + vague) for user selection.
  **Constraints:** Produce 12-18 canon-safe story pitches spanning Terravelle, Auralis, Zakros, and Wolfpoint. Each option must include: one-line premise, likely file path, canon anchors, and whether it introduces a new character.
  **Output:** Append option slate to `agent/staging/PENDING_REVIEW.md` in a single `[Copilot Auto]` block.
  **Owner:** `Copilot Auto`

- [x] **Goal:** Route story-option slate into creator-facing decision bundles.
  **Constraints:** Convert generated options into `A/B/C` bundles in `agent/DECISIONS.md` with concise tradeoffs and clear creator action line. Do not write story content in this task.
  **Output:** New story selection decision entry in `agent/DECISIONS.md`.
  **Dependency:** Story-option slate task above must be present in `agent/staging/PENDING_REVIEW.md`.
  **Owner:** `Codex`

- [x] **Goal:** Create **real purchasable grimoires** as in-universe books â€” actual written texts, not tier reference pages.
  **Constraints:** Common-tier grimoires should be purchasable (include price, who sells them, what they contain as a reader would see). Higher-tier should note where they can be found. Each grimoire is a real artifact: it has a publisher, an edition, margin notes from a previous owner or institutional stamp. Write them as the book itself, not a description of the book.
  **Output:** 4â€“6 grimoire entries in `content/WrittenWorks/` â€” at least 2 Common-tier (purchasable), 1 Uncommon-tier (harder to find), 1 Rare-tier (institutional only). Each is a fully written in-universe text.
  **Owner:** Copilot Auto

- [x] **Goal:** Write **â€The Screaming Shadeâ€** â€” a short story following an adventurer group who encounter a soul bound to a location that keeps screaming it is the strongest Flux user in Solumora.
  **Constraints:** Nobody in the party is strong enough to dispel it. The soul is genuinely distressed, not just malicious. The bound-soul mechanism should be consistent with existing lore (Flux, Binding discipline, Watts). End is unresolved â€” they leave it screaming. Tone: grounded, not comedic, slightly grim. Format: short fiction, 800â€“1200 words.
  **Output:** `content/Stories/The Screaming Shade.md`
  **Owner:** Copilot Auto
---

## IMMEDIATE (no decisions needed)

- [x] **TASK-01** â€” Write `content/Equatorial Desert.md` expansion
  The existing page is a stub. Write it as a full lore page: what the desert actually feels like, why Halveth exists, what Rift Incursions look like in practice, what the ruins in the desert mean. Dense, sensory, no purple prose. Outbound links: Halveth, Rift Incursions, Flux Demons, Ancient Ruins, Emberfall, Auralis, Terravelle, Ascendant Path, High Demons.

- [x] **TASK-02** â€” Update backlinks for pipeline-generated characters (Veld Dorv, Life in Emberfall, and others from current run)
  Check what the pipeline created. Ensure Emberfall, The Advancement Corps, and relevant character pages link back to new pages.

- [x] **TASK-07** â€” Write `content/Davan Rhyce.md` gap check
  Davan Rhyce is listed in content/ but not in WORLD_STATE.md's character list. Read the existing page and verify it's canon-consistent. Add to WORLD_STATE.md if missing.

- [x] **TASK-08** â€” Write `content/Life in Halveth.md` expansion
  Halveth is defined primarily by its garrison and desert proximity. The existing "Life in Halveth" page needs Wren's presence woven in (unnamed, as texture), and the reality of desert-edge life expanded. Reference Selt Orvn and Vorn Teld (Rift Incursion survivor).

---

## IN PIPELINE â€” current TASK.md queued

- [x] **TASK-03** â€” Wolfpoint in motion: append Sera Voss ("The First Test") + append Mira Solv ("The Notification Problem"). Both A+D simultaneously.
- [x] **TASK-04** â€” Drest current operation: append to Drest page (Option C â€” academic cover via Culmination ruins research)
- [x] **TASK-05** â€” Mave Daily Existence rewrite (sibling dynamic; Selvane has genuine warmth for Mave â€” their only "sweet spot") + minor Selvane update
- [x] **TASK-06** â€” Sorath in Hedun: append to Sorath page (Option C â€” passing through, Tolla Rend notices)
- [x] **FIX-1c** â€” Ostal Mrev corrected consultation notes (Square=8W, single discipline per sigil)

---

## NEXT PIPELINE â€” Grimoire & Spell Development

- [x] **TASK-12** â€” Create `content/WrittenWorks/The Zakros Crossing Compendium.md`
  Published survival grimoire. Author: Avel Coss (T4 desert guide) writing from field experience. Curated selection of ~12 spells from Common+Uncommon focused on desert crossing survival: thermal management, air filtration, fauna detection, structural shelter, rift-sign detection. Includes author's notes on which spells degrade under Zakros wind conditions and which to prioritize when reserves are low. Tone: spare, practical, slightly grim. Written Works format.

- [x] **TASK-13** â€” Create `content/WrittenWorks/Fifteen Sigils for the Young Practitioner.md`
  Educational T1 grimoire, guild-published (Valdenmoor Trade Guild). Not attributed to a single author â€” guild committee production. 15 T1 spells selected for teaching sequence, with margin notes from a specific copy owner (a parent? an apprentice master?). Notes on common errors, safety, which to teach first. The copy we see has been annotated by hand. Tone: pedagogical but human. Written Works format.

- [x] **TASK-14** â€” Append new spell entries to `content/All Grimoire.md` and relevant tier pages
  Add 6-8 new spells that fill obvious gaps:
  - **Dustlock** (T2): Chemical discipline, keeps particulate out of sigil surfaces and book pages. Critical for Zakros use.
  - **Heatshield** (T2): Heat discipline, sustained personal thermal buffering. More robust version of Warmbreath.
  - **Faunaread** (T2): Raw discipline, detects Flux signatures of living creatures in a sphere. Desert fauna detection.
  - **Waterward** (T2): Chemical discipline, seals a surface against water penetration permanently.
  - **Distressflag** (T3): Heat + Linked targeting â€” monitors a marked person's thermal state at distance. Expedition safety spell.
  - **Riftsense** (T3): Raw discipline, detects dimensional instability / rift formation probability in an area. Uncommon tier.
  Each entry must follow All Grimoire table format exactly. Watt costs must be calculated correctly per the formula.

- [x] **TASK-15** â€” Create `content/WrittenWorks/Ossal Meln's Workshop Notes.md`
  Ossal Meln (T3 Flux-embedded objects craftsperson, Valdenmoor) developing a new embedded object configuration. Shows iterative process: failed attempt at a combined thermal+light embedded sigil, cost calculation error, revised approach, final working configuration. Tone: craftsperson's notebook, numbers-heavy, brief. This is where new spell development is visible as a process.

---

## FUTURE (not yet scoped)

- [x] **TASK-09** â€” Ashford political atmosphere update
  Doss Varn (border guard), Orre Cavlt (cross-border merchant), and Cavel Dorst (merchant house) all see the political shift from ground level. Update their pages or write a "Life in Ashford" expansion reflecting current Expansion Faction pressure.

- [x] **TASK-10** â€” Cassia: what she actually knows
  Cassia is constrained but she's not passive. What information does she have access to that she hasn't shared? What is she doing with it? Needs a "People in Motion" style append.

- [x] **TASK-11** â€” Bren Ossve (rural T7) developed
  A T7 practitioner living rurally and declining Path service pressure is one of the world's most interesting tensions. His page likely needs significant expansion.

---

## WORKLOG

| Date | Task | Action | Notes |
|------|------|---------|-------|
| 2026-03-05 | Setup | Created TASK_QUEUE.md and DECISIONS.md | Pipeline running current TASK.md batch |
| 2026-03-05 | Pipeline review | Approved Batch 2 | Veld Dorv + Selvane Daily Existence. Maren Sollis added to WORLD_STATE |
| 2026-03-05 | Pipeline review | Rejected Batch 3 | Mave/Selvane both "infrastructure consultant" â€” role conflict |
| 2026-03-05 | Pipeline review | Approved Batch 4 | Wren Daily Existence + Osvin Brack Watt entries. All correct. |
| 2026-03-05 | Pipeline review | Approved Batch 5 | Rell Hadv + Toven Ral Watt entries. Both correct. |
| 2026-03-05 | Pipeline review | Rejected Batch 6 | Ostal Mrev formula errors: Square=4W (should be 8W), two disciplines applied simultaneously, invented scale modifier |
| 2026-03-05 | WORLD_STATE | Updated | Added Davan Rhyce, Maren Sollis, Castor Helme, Yara Venn, Brennan Solce, Orla Fest |
| 2026-03-05 | DECISIONS | All 4 resolved | D1: Both A+D. D2: Mave orbits Selvane socially. D3: Option C academic cover. D4: Option C Hedun. |
| 2026-03-05 | TASK.md | Written | Fix pipeline failures + 4 unblocked narrative tasks. Ready to run. |
| 2026-03-05 | Pipeline run | All 4 batches approved | TASK-03/04/05/06 + FIX-1c complete. Ostal Mrev duplicate cleaned. |
| 2026-03-05 | Pipeline run | TASK-01 + TASK-08 complete | Equatorial Desert expanded (Desert Edge + Rift Encounters). Life in Halveth: Selt Orvn + Vorn Teld in body. Duplicate See Also and misplaced paragraphs fixed manually. |
| 2026-03-05 | Pipeline run | TASK-12/13/14/15 complete | Grimoire batch: Zakros Compendium, Fifteen Sigils, All Grimoire appended (4 spells), Ossal Meln Workshop Notes. Batch 2 rejected (planner dupe). claimed.md + planner constraint fix applied. |
| 2026-03-05 | TASK-11 | Complete | Bren Ossve expanded with institutional pressure/refusal dynamics (`## The Requests`). |
| 2026-03-05 | Trade & Travel spine | Phase 1-2 in progress | Added 6 route notes and inbound links across Ashford, Valdenmoor, Halveth, Wolfpoint, Hedun, Greyveil. Staged creator-gated Solumora/World Primer appends (Batch 3R1). |
| 2026-03-05 | Trade & Travel spine | Complete | Batch 3R1 applied: Solumora.md + World Primer.md "How People Move" sections. TASK-09/10 marked complete. |
| 2026-03-05 | Equatorial Crossing Economy | Complete | 8 new pages: Halveth Cooperative, Relay Compact, Terravelle Desert Trade Office, Standard Guided Crossing, Express Route Crossing, Relay-Stage Crossing, The Southern Approaches, The Northern Narrows. Equatorial Desert.md updated. Backlinks added to Halveth.md, Avel Coss.md. |
| 2026-03-05 | Grimoire Economy | Complete | 10 new pages: Guild Scrivener Network, Independent Scrivener, Grimoire Authentication, Black Market Grimoire Circulation, Grimoire Rights and Restrictions, Grimoire Lending and Rental, Grimoire Commissioning, Cross-Border Grimoire Trade, Scrivener Regulation, Grimoire Repair and Preservation. Grimoires.md updated with comprehensive economy section. All notes linked from Grimoires hub. |
| 2026-03-05 | Queue update | Added task | Added explicit world-edit task: Tier 1/Tier 0 cannot break into active Flux zone around Desert Zakros; assigned to Claude Code. |
| 2026-03-05 | Factions hub | Complete | Created Factions hub + 12 institution notes. Appended inbound link blocks to index.md, Terravelle Administration.md, and The Council of Auralis.md. |
| 2026-03-05 | Review gate | Complete | Batch 2 creator escalation resolved as APPROVED in DECISIONS.md. Staged appends already present in Cavel Dorst.md and Cassia.md. |
| 2026-03-05 | Queue update | Added story intake tasks | Normalized raw prompt block into structured tasks: Ashford/Maria story (Copilot), broad story-option slate (Copilot), and DECISIONS routing task (Codex). |
| 2026-03-05 | Zakros access floor | Complete | Appended T0/T1 flux-entry constraint to Equatorial Desert.md, Standard Guided Crossing.md, and The Southern Approaches.md; verified hub links from Equatorial Desert crossing economy section. |
| 2026-03-05 | Pipeline continuation | Complete | Added missing `The Northern Founding` + `The Southern Founding`, added `Maren River`, repaired history aliases in `History.md` + `Solumora.md`, and marked Terravelle/Wolfpoint/History goals complete. |
| 2026-03-05 | Queue update | Added world-needs maintenance | Added tasks for remaining stubs (`Binding`, `Pattern`, `Filter`) and legacy alias-link stabilization pass. |
| 2026-03-06 | Story lane reconciliation | Complete | Marked completed Copilot outputs as done (Ashford False Papers, story-option slate, purchasable grimoires, The Screaming Shade) and completed Codex DECISIONS routing task. |
| 2026-03-06 | Queue ownership update | Updated | Set Claude offline mode, reassigned core unchecked content tasks to Copilot Auto, and added preflight Terravelle escalation + Bone Sea expansion tasks. |
| 2026-03-06 | Terravelle preflight escalation | Complete | Added `DECISION D` in `agent/DECISIONS.md` with creator A/B/C scope options for protected `content/Terravelle.md` handling. |
| 2026-03-06 | Glossary stub resolution | Complete | Populated `Binding.md`, `Pattern.md`, and `Filter.md`; added explicit inbound links from `Spell Variables.md`; link targets validated for touched files. |
| 2026-03-06 | Bone Sea expansion | Complete | Expanded `The Bone Sea.md` into travel/canon note; appended inbound logistics reference from `Equatorial Desert.md`; touched-file links validated. |
| 2026-03-06 | DECISIONS normalization | Complete | Repaired duplicate Active Review blocks and restored a single valid `REVIEW_DECISION` marker pair to keep orchestrator parsing stable. |
| 2026-03-06 | CLAIMED sync | Complete | Added 21 existing content paths missing from `agent/staging/CLAIMED.md` (stories, written works, Terravelle/Wolfpoint/history package files). |
| 2026-03-06 | Solumora live map | Complete | Added a live canonical-position map component on `Solumora` via layout injection, including auto-refreshing link resolution from `static/contentIndex.json`; validated with `npx tsc --noEmit` and `npx quartz build -d content`. |
| 2026-03-05 | Alias stabilization pass | Complete | Normalized legacy links (`Culmination Faction`, `Persecution Era`, `Isolation Period`, `Advancement Corps`) to canonical targets and mapped unresolved references (`Crestward Research Nexus`, `Ashford Blockade`) to existing canon pages. |
| 2026-03-05 | People Web hub integration | Complete | Confirmed `People.md` cast coverage and appended `People in Motion` sections to `Solumora.md`, `Terravelle.md`, `Auralis.md`, `Wolfpoint.md`, and `Equatorial Desert.md`; touched-file links validated. |
| 2026-03-05 | Integrity sweep | Complete | Ran vault-wide filtered link audit; applied low-impact alias fixes + added `Veld Dorv` and `WrittenWorks`; reduced meaningful missing targets to 12 and logged remainder in `agent/reports/inconsistencies.md`. |
| 2026-03-05 | Integrity closure | Complete | Added 12 missing target pages from prior flagged list and re-ran filtered vault scan with zero unresolved targets. |
