Here is a starting point for building a local-first, multi-agent worldbuilding pipeline that meets the requirements.

**Agent Task Structure**
------------------------

The agent task structure will consist of three main agents:

1. **Claude**: Responsible for generating large-scale output (new notes, major expansions, character webs)
2. **Ollama**: Limited to short seed material generation (names, micro-lists, 1-2 line stubs)
3. **GPT** (Conversational Partner): Conservative and corrective edits, ensures no hallucinated pages, updates hubs/indexes in append-only blocks

**Agent Task Files**
-------------------

### agent/TASK.md
```markdown
# Solumora Worldbuilding Pipeline

## Agent Tasks

* `claude`: Expand Solumora at scale ( Claude )
* `ollama`: Fill in low-level supporting material in small bursts ( Ollama )
* `gpt`: Enforce canon + backlinks + navigation + consistency by directly editing the Obsidian /content vault
```
### agent/WORLD_STATE.md
```markdown
# World State

## Inconsistencies Report

* List of inconsistencies detected during pipeline run
```
### agent/staging/seed.md
```markdown
# Seed Material

## Names
* 10 place names
	+ Aridian Oasis
	+ Khyron Desert
	+ ...
* 10 faction names
	+ Kraelion Brotherhood
	+ Aridian Guild
	+ ...
* 20 person names + 1-line hook
	+ Aurélien Dantès (former thief)
	+ Elara Vex (mysterious sorceress)
	+ ...
```
### agent/staging/seed.md (Ollama's output)

**Claude's Output**
------------------

Claude will generate large-scale output in the following format:

### new_notes/*.md
```markdown
# [Note Title]

## Summary

* Brief summary of note content

## People in Motion

* Named individuals mid-journey:
	+ Aurélien Dantès (former thief)
	+ Elara Vex (mysterious sorceress)

## Links

* [Link to existing page]
```
**GPT's Output**
-----------------

GPT will generate conservative backlinks, update hubs/indexes in append-only blocks, and provide inconsistency reports.

### agent/reports/inconsistencies.md
```markdown
# Inconsistencies Report

## List of inconsistencies detected during pipeline run
```
### agent/reports/links_applied.md
```markdown
# Links Applied Report

## List of links applied to changed files
```
**Pre-Commit Hook**
-------------------

The pre-commit hook will ensure the pipeline runs before anything is committed.

### .git/hooks/pre-commit
```bash
#!/bin/sh

# Run pipeline before commit
./pipeline.sh
```
This starting point should provide a solid foundation for building a local-first, multi-agent worldbuilding pipeline that meets the requirements. Note that this is just the beginning, and further development will be necessary to fully implement the system.

To proceed, I'll need clarification on some aspects:

1. **User Decision-Making**: How will users make decisions regarding cultures, principles, values? Should we provide options/choices for users to pick from?
2. **Token/Rate-Limit Safety**: How will we ensure token/rate-limit safety during pipeline runs?
3. **Context Retrieval and Chunking**: How will we retrieve and chunk context for each agent task?

Please let me know which areas you'd like to focus on next, and I'll be happy to help!