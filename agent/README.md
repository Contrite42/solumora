# Agent Workflow

Simplified single-agent workflow for Solumora world expansion.

## Core Files (Use These)

1. **USER_INPUT.md** - Fill this with your expansion request, acceptance criteria, and constraints
2. **TASK_QUEUE.md** - Pipeline intake with all queued expansion tasks
3. **TASK.md** - Active task specification (copy from TASK_QUEUE.md when starting work)
4. **DECISIONS.md** - Canon decisions requiring user approval (A/B/C options)
5. **PRE_FLIGHT.md** - Checklist to run before each expansion cycle

## Workflow

```
Start new work:
1. Fill USER_INPUT.md with request
2. Copy next task from TASK_QUEUE.md to TASK.md
3. Run PRE_FLIGHT.md checklist
4. Execute work
5. If decisions needed, add to DECISIONS.md
6. Delete completed task entries from TASK_QUEUE.md and clear completed task detail from TASK.md
```

## Completion Policy

- Completed tasks should be deleted from `agent/TASK_QUEUE.md` rather than retained as checked historical entries.
- `agent/TASK.md` should only contain active work. When work is complete, delete the completed task detail instead of preserving it there.
- If a short completion record is still needed for human coordination, keep it to a brief note in a non-control review surface rather than an archive-style task ledger.

## Reference Documentation

World-building rules and conventions moved to `docs/reference/`:
- `WORLD_STATE.md` - Naming conventions and canon rules
- `STYLE_GUIDE.md` - Writing voice and structure patterns
- `QA_RULES.md` - Link validation rules

## Navigation Tools

All Python scripts consolidated in `scripts/python/`:
- Use `python scripts/python/pyhub.py list` to see available tools
- Use `python scripts/python/pyhub.py run hub:<script-name> -- [args]` to run scripts
- See `scripts/python/USAGE.txt` for navigation toolkit details

## QA Automation Command

- Run section coverage audit: `python scripts/python/pyhub.py run hub:section_audit -- --required Appearance Relationships "Use In Session" --output agent/reports/section_audit.md`
