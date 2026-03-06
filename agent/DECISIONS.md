# Decisions

This file serves both operators and `agent/orchestrator.py`.
Do not remove the `REVIEW_DECISION` markers while an active review is open.

## Decision Policy
- Operators decide routine implementation and low-impact world-filling tasks.
- Escalate to creator only for changes that impact world structure, core storyline, principal characters, or major events.
- Creator escalations must provide multiple options (A/B/C) with concise tradeoffs.

<!-- REVIEW_DECISION_START -->
## Active Review Decision
- Batch: 2R1
- Scope: `content/Cassia.md`
- Source: `agent/staging/PENDING_REVIEW.md`
- Decision Owner: CREATOR
- Status: PENDING
- Notes: Manual rewrite staged after prior rejection; pending creator review.

### Escalation Reasons
- Touches principal character page: `content/Cassia.md`.

### Creator Options
- Option A: APPROVE batch as staged.
- Option B: REJECT and regenerate this batch.
- Option C: REJECT and request manual operator rewrite.

### Creator Action
- Set `- Status:` to `APPROVED` or `REJECTED`.
- If rejected, replace `- Notes:` with concise guidance and optional option label.
Approved

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
