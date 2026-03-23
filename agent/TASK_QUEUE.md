# Task Queue
Systematically check all files for continuity breaks, impossibilities, continuity drift, and operational blockers.

## USER QUEUE (Pipeline Intake)

Add creator/user-requested work items here first. `agent/TASK.md` should always mirror the next unchecked item from this section when a new cycle starts.

- [ ] **USER-001 - Execute Media Adaptation Milestone Board**
      **Source:** Direct user request (2026-03-17)
      **Goal:** Operationalize the Solumora media plan into milestone-gated execution with no date-based scheduling.
      **Scope:** Track and drive Milestones 1-8 from `agent/MEDIA_ADAPTATION_PLAN.md` using gate-based progression and continuity control.
      **Required outputs:** Milestone-by-milestone checklist updates, scope lock decisions, prototype validation notes, and launch expansion gate decision.
      **Owner:** `Copilot Auto`
- Add new tasks as unchecked entries using this pattern:

```markdown
- [ ] **USER-### - Task Title**
      **Source:** Direct user request (YYYY-MM-DD)
      **Goal:** One-sentence outcome target.
      **Scope:** Concrete deliverable boundaries.
      **Required outputs:** Files and updates expected.
      **Owner:** `Copilot Auto`
```

---

**Permanent Tasks:**

- The World Always Needs More. There is always something to add: a new adventure to play out in this world, a new friend, a new town, a new spell, a new description. There will always be more.
- Whenever human interaction is needed, pop open a GUI that I can respond in.
- Develop a method of file traversal more AI efficient that all three high level agents can use.
- Develop efficiencies for the current pipeline leaning towards time and token cost. Do not allow quality to drop in final outputs.
- **Clean up completed tasks:** When tasks are marked complete, delete their detailed content from `agent/TASK.md` and remove completed entries from `agent/TASK_QUEUE.md` so only active work remains.
- **Clean up resolved decisions:** When decisions are resolved (APPROVED, REJECTED, or RESOLVED status), delete their detailed content from `agent/DECISIONS.md` to keep the file focused on pending/active decisions.
- **Git push after big changes:** After completing significant content expansions, navigation rebuilds, or component updates, commit and push changes to the repository to preserve progress and enable backup/collaboration.

---

## CONCURRENT AGENT OWNERSHIP (ACTIVE)

Use this split while Copilot Auto and Codex run simultaneously (`Claude Code` currently offline).

- `Copilot Auto` (control plane owner): only agent allowed to edit `agent/TASK_QUEUE.md`, `agent/TASK.md`, `agent/COORDINATION.md`, `agent/DECISIONS.md`, and `agent/staging/CLAIMED.md`.
- `Codex` (content and implementation lane): handles assigned content/story tasks, canon/link QA, and supporting implementation work outside control-plane ownership unless explicitly reassigned.
- `Claude Code` (core content lane): OFFLINE. Do not assign new active tasks until back online.
- Shared staging note: all agents may append status notes to `agent/staging/PENDING_REVIEW.md` using prefix `[Agent][YYYY-MM-DD HH:MM]`.
- Conflict rule: if another agent is already editing a file, stop and hand off through `agent/staging/PENDING_REVIEW.md` instead of writing.
- Assignment rule: only `Copilot Auto` may change task ownership labels in this queue.
