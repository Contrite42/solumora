# Pre-Flight Checklist

Before starting any new content expansion cycle, complete this checklist to ensure clean, efficient, and canon-consistent work.

## ✅ Checklist

### 1. Define User Intent
- [ ] Fill `agent/USER_INPUT.md` with expansion request
  - [ ] Define scope (concepts, regions, factions, etc.)
  - [ ] List acceptance criteria
  - [ ] Note canon constraints/dependencies
- [ ] Copy next unchecked USER-* item from `agent/TASK_QUEUE.md` to `agent/TASK.md`

### 2. Generate Navigation Pack
- [ ] Identify seed concept(s) for expansion
- [ ] Generate task-scoped nav pack:
  ```bash
  python scripts/python/pyhub.py run hub:world_nav_query -- <Concept> --output tmp/nav-<concept>.json
  ```
- [ ] Review nav pack to understand existing canon and link targets

### 3. Query Cached Context
- [ ] Use cached lookup first (token-efficient):
  ```bash
  python scripts/python/pyhub.py run hub:concept_cache_query -- related <Concept> --top 20
  ```
- [ ] Identify related pages that need reading
- [ ] Use section line ranges from nav pack to read only relevant sections

### 4. Handle Decisions
- [ ] If canon decisions needed, add A/B/C options to `agent/DECISIONS.md`
- [ ] Get user confirmation before writing new canon
- [ ] Document chosen approach in `agent/DECISIONS.md`

### 5. Execute Work
- [ ] Create/edit content files
- [ ] Validate wiki-link syntax (`[[Concept]]` format)
- [ ] Ensure recipes use proper variables (Self, Filter, Where Written, etc.)
- [ ] Check grimoire formatting (`***` separators, bold spell names)

### 6. Refresh Navigation Artifacts
**REQUIRED after any content changes:**
- [ ] Refresh graph cache:
  ```bash
  python scripts/python/pyhub.py run hub:concept_graph_export
  ```
- [ ] Refresh context index:
  ```bash
  python scripts/python/pyhub.py run hub:build_context_index
  ```
- [ ] Verify new pages appear in cache:
  ```bash
  python scripts/python/pyhub.py run hub:concept_cache_query -- stats
  ```

## 🎯 Token Efficiency Rules

1. **Cache First**: Always use cached navigation before full markdown scans
2. **Section Targeting**: Use line ranges from nav packs to read only needed sections
3. **Focused Queries**: Generate task-specific nav packs instead of vault-wide traversals
4. **No Full Scans**: Never run full-vault content traversal if cache-based navigation answers the task

## 📋 Quick Commands Reference

```bash
# List all available scripts
python scripts/python/pyhub.py list

# Generate navigation pack
python scripts/python/pyhub.py run hub:world_nav_query -- <Concept> --output tmp/nav-<concept>.json

# Query cached graph
python scripts/python/pyhub.py run hub:concept_cache_query -- related <Concept> --top 20
python scripts/python/pyhub.py run hub:concept_cache_query -- backlinks <Concept>
python scripts/python/pyhub.py run hub:concept_cache_query -- stats

# Refresh caches (required after content changes)
python scripts/python/pyhub.py run hub:concept_graph_export
python scripts/python/pyhub.py run hub:build_context_index
```

## 🚨 Common Mistakes to Avoid

- ❌ Creating content without checking cache first (wastes tokens)
- ❌ Forgetting to refresh caches after content changes (navigation becomes stale)
- ❌ Using `---` separators in grimoire tables (renders as titles, use `***`)
- ❌ Creating wiki links to non-existent concept pages (use plain text for recipe variables)
- ❌ Running full markdown scans when cached queries would work
- ❌ Skipping decision documentation in `agent/DECISIONS.md`

---

**Last Updated**: 2026-03-06  
**Status**: Active checklist for all expansion cycles
