# Decisions

This file serves both operators and `agent/orchestrator.py`.
Do not remove the `REVIEW_DECISION` markers while an active review is open.

## Decision Policy

- Operators decide routine implementation and low-impact world-filling tasks.
- Escalate to creator only for changes that impact world structure, core storyline, principal characters, or major events.
- Creator escalations must provide multiple options (A/B/C) with concise tradeoffs.

<!-- REVIEW_DECISION_START -->

## Active Review Decision

- Batch: 2
- Scope: `content/Cavel Dorst.md`, `content/Cassia.md`
- Source: `agent/staging/PENDING_REVIEW.md`
- Decision Owner: CREATOR
- Status: PENDING
- Notes: (set when rejecting)

### Escalation Reasons

- Touches principal character page: `content/Cassia.md`.

### Creator Options

- Option A: APPROVE batch as staged.
- Option B: REJECT and regenerate this batch.
- Option C: REJECT and request manual operator rewrite.

### Creator Action

- Set `- Status:` to `APPROVED` or `REJECTED`.
- If rejected, replace `- Notes:` with concise guidance and optional option label.
<!-- REVIEW_DECISION_END -->

---

## DECISION B - TASK-09/TASK-10 Batch 2 Execution Strategy

Status: RESOLVED (OPERATOR)

Options:

- A: Continue with standard review gate (generate batch 2, then review in this file).
- B: Manual operator write mode (skip generation and write both appends directly by operator).

Decision:

- Chosen: A
- Reason: Routine execution strategy; no creator-level canon impact.

---

## Archived Canon Decisions (Resolved)

- D1 Wolfpoint secret sequencing: both Sera test and Mira signal-awareness run in parallel.
- D2 Mave/Selvane relationship: social-orbit model, no independent Mave professional cover.
- D3 Drest operation mode: academic cover via Culmination expedition routing.
- D4 Sorath location: passing through Hedun.

---

## DECISION C - Story Slate Bundle Selection

Status: PENDING (CREATOR)
Prepared by: Codex
Source: `agent/staging/PENDING_REVIEW.md` (`[Copilot Auto][2026-03-05 19:32]` block)

Options:

- A: Border pressure and work survival (Ashford plus Terravelle labor systems). Candidate stories: `The Ledger Gatekeeper`, `After the Inspection Bell`, `Harvest Without Terms`, `Plate Four in Evidence`, `Certification Ink`.
  Tradeoff: strongest everyday-systems grounding; lower immediate geopolitical scope.
- B: Crossing risk and Zakros emergency pressure (desert routes plus response failures). Candidate stories: `Cache Mark Seven`, `Nineteen Survived`, `Bell During Burial`, `The Third Room at Milepost Nine`.
  Tradeoff: strongest travel-danger continuity; narrower council/power intrigue coverage.
- C: High-politics and Wolfpoint leverage (council, diplomacy, and restricted knowledge). Candidate stories: `The Donor's Shelf`, `Two Seals for Greyveil`, `The Unpublished Table`, `The Clause Mira Reads Twice`, `Six Missing Hours`, `Wrong Door, North Wind`.
  Tradeoff: strongest strategic arc progression; requires tighter canon checks around principal actors.

Creator Action:

- Set this section to `Status: APPROVED (A)` or `APPROVED (B)` or `APPROVED (C)`.
- If rejected, set `Status: REJECTED` and add a short replacement direction.

---

## DECISION D - Terravelle Megacity Scope (Protected File Preflight)

Status: PENDING (CREATOR)
Prepared by: Codex
Reason: `content/Terravelle.md` is protected and requires creator-approved scope before edits.

Options:

- A: Minimal-safe rollout. Create the 8 new Terravelle notes first, do not edit `content/Terravelle.md` yet. Add inbound links from non-protected hubs/pages only.
  Tradeoff: fastest unblocked content growth; Terravelle hub remains temporarily behind.
- B: Full rollout after approval. Create the 8 new Terravelle notes plus append one compact Terravelle hub section in `content/Terravelle.md`.
  Tradeoff: best reader navigation; touches protected canon file immediately.
- C: Staged rollout with review gate. Create 8 notes now, then submit a focused Terravelle hub append block to `agent/staging/PENDING_REVIEW.md` for explicit creator approval before applying.
  Tradeoff: slower, but strongest canon control and lowest overwrite risk with concurrent agents.

Creator Action:

- Set this section to `Status: APPROVED (A)` or `APPROVED (B)` or `APPROVED (C)`.
- If rejected, set `Status: REJECTED` and provide replacement scope.

---

## DECISION E - High Demon Layer Expansion Scope

Status: PENDING (CREATOR)
Prepared by: Copilot Auto
Reason: High Demons are sensitive canon (tier-9 scale threats, operating undetected for centuries). Operational detail expansion requires creator approval to preserve "nobody knows they exist" constraint while adding daily tradecraft/near-miss material.

**Current State:**
Five High Demon pages exist with strong character/goal documentation (Sorath, Selvane, Fennick, Mave, Wren). What's missing: territorial boundaries, day-to-day routines, detection-avoidance tradecraft beyond general description, near-miss incidents with ordinary people, operational friction points.

**Gap Analysis:**
- Sorath: "on the road" but no specific circuit, routes, or travel pattern detail
- Selvane/Mave: Both in Solhaven for decades but no territorial overlap management, close-call incidents, or daily cover maintenance detail
- Fennick: "crashes gatherings" but no specific social circuit, repeat venue patterns, or what happens when hosts remember him
- Wren: Halveth gatekeeper role clear but no incident log examples, failed expeditions she couldn't save, or rift emergence response protocols

Options:

- A: **Minimal Near-Miss Focus** — Create 3-4 near-miss incident notes only (ordinary people who almost discovered evidence). No demon territorial notes, no routine expansion. Lightest canon touch, preserves mystery through incident POV rather than demon operational detail.
  Tradeoff: Safest canon preservation; narrow scope may not justify task activation; reader learns about demons through absence/traces rather than presence.

- B: **Operational Detail Layer** — Create 2 notes per demon (10 total): territorial pattern + detection method for each. Add 2-3 near-miss incidents. Update demon pages with "Operational Pattern" sections. Full execution of original task scope showing what demons actually do day-to-day.
  Tradeoff: Maximum worldbuilding depth; higher risk of breaking "undetectable" constraint if tradecraft too visible; 10+ new pages with complex canon dependencies.

- C: **Hybrid: Routines + Select Incidents** — Create 1 operational note per demon (5 total) covering territory/routine/tradecraft in compact format, plus 2-3 compelling near-miss incidents. Update demon pages with brief operational subsections. Balanced approach between depth and canon safety.
  Tradeoff: Good worldbuilding/canon balance; moderate page count (7-8 notes); preserves mystery while grounding demon presence; agent can execute with clear boundaries.

Creator Action:

- Set this section to `Status: APPROVED (A)` or `APPROVED (B)` or `APPROVED (C)`.
- If rejected, set `Status: REJECTED` and provide alternative direction or task skip instruction.
