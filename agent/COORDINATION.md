# Five-Agent Coordination Protocol

Five agents work on this pipeline. Each has a defined cost tier and content scope.

| Agent | Identity | Cost | Scope |
|-------|----------|------|-------|
| **CLI** | Claude Code CLI (`vibrant-neumann` worktree) | Free (sub) | Batch content, pipeline management, DECISION resolution |
| **VSCODE** | Claude Code VS Code | Free (sub) | Targeted edits, gap checks, backlinks, small appends |
| **OPENAI** | `orchestrator.py` → gpt-4o-mini | ~$0.001/call | Planning (JSON) + ground-level writing |
| **CLAUDE-API** | `orchestrator.py` → claude-opus-4-6 | ~$0.05/call | Principal characters + lore mechanics only |
| **OLLAMA** | `orchestrator.py` → llama3.1:8b (local) | Free | Seed names, rumor hooks, name deduplication |

---

## Claiming a Task (CLI and VSCODE only)

Before starting any task:

1. Read `agent/staging/CLAIMED.md`
2. Confirm the task is not already claimed
3. Append a claim line:
   ```
   CLAIMED | TASK-XX | CLI | 2026-03-05 HH:MM
   ```
4. Begin work

On completion:
```
DONE | TASK-XX | CLI | 2026-03-05 HH:MM
```

If abandoned mid-work:
```
RELEASED | TASK-XX | CLI | 2026-03-05 HH:MM
```

OPENAI, CLAUDE-API, and OLLAMA are called by `orchestrator.py` automatically — they do not claim tasks in CLAIMED.md.

---

## Natural Division of Labor

**CLI** (larger writes, pipeline runs):
- WrittenWorks creation
- Multi-file appends
- Character page expansions (3+ paragraphs)
- Running the pipeline (`python agent/orchestrator.py`)
- Resolving DECISIONS.md entries
- Updating TASK_QUEUE.md worklog

**VSCODE** (targeted, interactive):
- Backlink updates and See Also additions
- Small character appends (1–2 paragraphs)
- Consistency fixes from `agent/reports/inconsistencies.md`
- Verifying pages match WORLD_STATE.md canon

**OPENAI via orchestrator** (ground-level batch content):
- Ground-level characters (ordinary people, daily life)
- Location texture (Life in X pages)
- Trade, supply chain, border life
- Anything tagged `"complexity": "ground-level"` in the plan

**CLAUDE-API via orchestrator** (high-quality complex content):
- Principal characters in KEY_NARRATIVE_THREADS
- High Demons
- Lore mechanics (magic system expansions, history)
- Anything tagged `"complexity": "principal"` or `"lore"` in the plan

**OLLAMA via orchestrator** (local seed):
- Name suggestions (with deduplication against WORLD_STATE)
- Rumor hooks for context seeding
- No canon-critical decisions

---

## Complexity Tagging (for orchestrator runs)

When writing `agent/TASK.md` for a pipeline run, or when the plan step runs, notes are tagged:

```
"complexity": "ground-level"  →  OpenAI writes (cheap, fast)
"complexity": "lore"          →  Claude API writes (quality)
"complexity": "principal"     →  Claude API writes (quality)
```

**Rule of thumb:** If the note involves a character named in WORLD_STATE's KEY_NARRATIVE_THREADS or is a High Demon, it's `principal`. If it's magic system mechanics or deep history, it's `lore`. Everything else is `ground-level`.

To bypass routing and force Claude for everything: set `FORCE_CLAUDE=1` environment variable before running orchestrator.

---

## File Conflict Rules

- **Never write to the same file at the same time.** Check CLAIMED.md for active claims.
- **Grimoire files** — sequential-append only. Claim the file name: `CLAIMED | Common Grimoire | CLI | ...`
- **TASK_QUEUE.md worklog** — append-only. Both agents write their own rows.
- **WORLD_STATE.md** — read-only during task execution. Update only as a dedicated claimed task.

---

## Checking What's Available

Read `agent/TASK_QUEUE.md` → sections:
- `## IMMEDIATE` — highest priority
- `## NEXT PIPELINE` — current batch (orchestrator runs)
- `## FUTURE` → now labeled with agent tags: `[CLI]`, `[VSCODE]`, `[OPENAI]`, `[CLAUDE-API]`

Cross-reference with `agent/staging/CLAIMED.md`.

---

## When a Decision Is Needed

If you discover a conflict, naming collision, or canon gap that requires a choice:
1. Write options to `agent/DECISIONS.md`
2. Mark task as `BLOCKED | TASK-XX | CLI | ...` in CLAIMED.md
3. Do not proceed until the user resolves it in DECISIONS.md
