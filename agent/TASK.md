Goal: Build a local-first, multi-agent worldbuilding pipeline that lets you write a single task once and automatically:

expands Solumora at scale (Claude),

fills in low-level supporting material in small bursts (Ollama), and

enforces canon + backlinks + navigation + consistency by directly editing the Obsidian /content vault (GPT) before anything gets committed.
Constraints: One input surface: you only write in agent/TASK.md. No duplicate prompting.

Direct file editing: agents must write and modify markdown notes directly inside C:\Users\Contrite42\quartz\content.

Claude does the heavy writing: Claude generates all large output (new notes, major expansions, character webs).

Ollama stays small: Ollama is limited to short seed material only (names, micro-lists, 1–2 line stubs). Never large documents.

GPT is a conversational partner of claude to help world building: conservative + corrective: GPT only performs safe edits:

makes sure there are no links to "admin" pages that could ruin the adventurer for a user reading through

adds links only to existing pages (no hallucinated pages),

updates hubs/indexes in append-only blocks,

generates inconsistency reports against agent/WORLD_STATE.md.

Token/rate-limit safety: no agent may “load the entire vault.” Context must be retrieved and chunked:

only canon + style + relevant notes + diff/changed files.

Claude work must be batched and throttled automatically.

Pre-commit enforcement: GPT QA/linking must run before commit and stage its changes automatically.

You stay in control: everything is versioned through Git, and auto-edits are logged to reports.

User must be asked for any decisions that need to be made regarding cultures, principles, values. Provide options/choices for the user to pick. 
Output: A working “AI talking machine” that produces:

Worldbuilding Output (Claude):

12–30 new/expanded notes per task cycle, written in Obsidian style

every note includes “People in Motion” (named individuals mid-journey)

new notes are placed into the correct folders and linked outward

Seed Output (Ollama):

agent/staging/seed.md containing compact lists only:

names, rumors, districts, factions, small character hooks

hard-limited length so it never balloons

QA + Linking Output (GPT, auto-applied):

conservative backlinks inserted into changed files (existing titles only)

hub pages updated safely (append-only block)

agent/reports/inconsistencies.md

agent/reports/links_applied.md

changes staged automatically before commit

Operational Output (system behavior):

agent/staging/PLAN.json (Claude’s planned file list)

agent/staging/PATCH.json (exact applied edits)

agent/staging/CHANGELOG.json (changed files list)

pre-commit hook ensures the pipeline runs before anything is committed
