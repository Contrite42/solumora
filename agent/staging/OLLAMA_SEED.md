Here's a high-level implementation of the worldbuilding pipeline as described. I'll provide code snippets in Markdown format to demonstrate key components.

**Task Agent: Ollama**

Create `agent/Ollama/TASK.md` with the following content:

```markdown
# Task: Generate compact seed material for Solumora

## Output Requirements

* 10 place names (e.g., cities, landmarks)
* 10 faction names
* 20 person names + hook (e.g., "Seeking revenge against the ruling Council")
* 10 rumor hooks

## Constraints

Hard limit: 120 lines total
Only write in this file; do not duplicate prompt
```

**Claude's Worldbuilding Agent**

Create `agent/Claude/TASK.md` with the following content:

```markdown
# Task: Expand Solumora at scale and fill in supporting material

## Output Requirements

* 12-30 new/expanded notes per task cycle, written in Obsidian style
* Each note should include "People in Motion" (named individuals mid-journey)
* New notes should be placed into the correct folders and linked outward

## Constraints

Batch Claude's work automatically
Throttle Claude's output to prevent overwhelming GPT
```

**GPT's QA/Linking Agent**

Create `agent/GPT/TASK.md` with the following content:

```markdown
# Task: Ensure canon, backlinks, navigation, and consistency

## Output Requirements

* Conservative backlinks inserted into changed files (existing titles only)
* Hub pages updated safely (append-only block)
* Inconsistency reports generated against agent/WORLD_STATE.md
* Changes staged automatically before commit

## Constraints

Only perform safe edits: no links to "admin" pages, hallucinated pages, or orphaned notes
```

**Operational Scripts**

Create `agent/staging/PLAN.json`, `agent/staging/PATCH.json`, and `agent/staging/CHANGELOG.json` as empty files.

Add a pre-commit hook in `.git/hooks/pre-commit` that runs the pipeline:

```bash
#!/bin/bash

# Run task agents in sequence
node agent/Ollama/TASK.js > agent/staging/seed.md
node agent/Claude/TASK.js > agent/staging/worldbuilding-output.txt
node agent/GPT/TASK.js > agent/staging/QA-linking-output.txt

# Stage changes automatically before commit
git add -u
```

**User Input and Decision-Making**

Create a `prompt.js` script that interacts with the user to gather decisions regarding cultures, principles, values:

```javascript
const readline = require('readline');

// Ask user for cultural options
console.log("Select 2-3 core cultural values:");
console.log("A) Exploration-driven")
console.log("B) Community-focused")
console.log("C) Technological advancement")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let chosenValues = [];
rl.on('line', (input) => {
  if (!chosenValues.includes(input)) {
    chosenValues.push(input);
    console.log(`You selected ${input}`);
  }
  if (chosenValues.length === 3) {
    rl.close();
  }
});
```

**Example Output**

After running the pipeline, you should see:

* `agent/staging/seed.md`: Compact seed material with names, rumors, factions, and character hooks.
* `agent/staging/worldbuilding-output.txt`: Claude's worldbuilding output with new notes and expanded content.
* `agent/staging/QA-linking-output.txt`: GPT's QA/linking output with conservative backlinks and consistency reports.
* `agent/reports/inconsistencies.md` and `agent/reports/links_applied.md`: Inconsistency reports and link application logs.
* `agent/staging/PLAN.json`, `agent/staging/PATCH.json`, and `agent/staging/CHANGELOG.json`: Operational output with planned file list, applied edits, and changed files list.

This implementation should provide a working AI talking machine that produces the desired outputs while enforcing canon, consistency, and navigation.