# Spell Management Workflow

This document describes the complete lifecycle for spells in the Solumora grimoire system.

## Overview

The grimoire system follows a consistent pattern:
1. **Individual Spell Pages**: Every spell has its own page in `content/Spells/`
2. **Grimoire Organization**: Spells are organized by rarity in grimoire pages (Common, Uncommon, Rare, Legendary, Mythic)
3. **Bidirectional Linking**: Grimoire pages contain inline spell recipes with links to individual pages
4. **Central Index**: All Grimoire.md serves as the top-level index

## Spell Lifecycle

### 1. Creating a New Spell (Automated via sigil_maker.py)

When using `sigil_maker.py` in auto mode, spells are generated and automatically integrated:

```bash
python quartz/sigil_maker.py auto \
  --generate-count 5 \
  --min-tier T1 \
  --max-tier T4 \
  --llm-provider sonnet \
  --sync-grimoire-indexes \
  --sync-spells-hub
```

**What happens:**
1. Generates spell spec with chosen LLM provider (local, ollama, sonnet, openai)
2. Calculates Flux cost and determines tier/rarity
3. Creates individual spell page in `content/Spells/SpellName.md`
4. Adds entry to appropriate rarity grimoire (`content/Common Grimoire.md`, etc.)
5. Adds link to `content/All Grimoire.md` (if --append-all-grimoire)
6. Adds entry to `content/Spells.md` hub (if --sync-spells-hub)

**Individual Spell Page Format:**
```markdown
# Spell Name

One-sentence summary.

## Sigil Variables

| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| ... | ... |

**Rarity:** Common
**Grimoire:** [[Common Grimoire]]
```

**Grimoire Entry Format:**
```markdown
**Spell Name**
One-sentence summary.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| ... | ... |
| Spell Page | [[Spells/Spell Name|Spell Name]] |

---
```

### 2. Creating a New Spell (Manual)

For handcrafted spells:

1. **Create the individual spell page** in `content/Spells/SpellName.md`
   - Include full recipe table
   - Add rarity and grimoire reference at bottom

2. **Add entry to rarity grimoire** (e.g., `content/Common Grimoire.md`)
   - Include spell name (bolded)
   - Add one-sentence summary
   - Add full variable table
   - **IMPORTANT:** Add `| Spell Page | [[Spells/SpellName|SpellName]] |` as last table row

3. **Link from All Grimoire.md** (optional, for generated index section)
   - Add to "## Sigil Maker Generated Index" section
   - Format: `- [[Spells/SpellName|SpellName]] - X W - TX - [[Rarity Grimoire|Rarity]]`

### 3. Validation and Migration

Use `spell_validator.py` to audit and fix spell organization:

**Check current state:**
```bash
python quartz/spell_validator.py --report-only
```

**Generate missing individual spell pages:**
```bash
python quartz/spell_validator.py --generate-missing
```

**Add missing grimoire links:**
```bash
python quartz/spell_validator.py --add-links
```

**Full migration (generate + link):**
```bash
python quartz/spell_validator.py --generate-missing --add-links
```

**What the validator checks:**
- Every spell entry in grimoire pages has an individual page in `content/Spells/`
- Every spell entry has a `| Spell Page | [[Spells/...]] |` link
- Reports mismatches and can auto-fix

### 4. Bulk Operations

**Process queue of spell specs:**
```bash
python quartz/sigil_maker.py auto \
  --spec-dir specs/queue \
  --generate-count 10 \
  --sync-grimoire-indexes
```

**Validate all grimoires after bulk changes:**
```bash
python quartz/spell_validator.py --report-only
```

## File Structure

```
content/
├── Spells/                      # Individual spell pages
│   ├── Hearthlight.md
│   ├── Warmstone.md
│   ├── Longbolt.md
│   └── ...
├── Common Grimoire.md           # T1-T2 spells
├── Uncommon Grimoire.md         # T3-T4 spells
├── Rare Grimoire.md             # T5-T6 spells
├── Legendary Grimoire.md        # T7-T8 spells
├── Mythic Grimoire.md           # T9 spells
├── All Grimoire.md              # Top-level index
└── Spells.md                    # Alternative hub page
```

## LLM Provider Options

The `sigil_maker.py` tool supports multiple LLM providers for generating spell names and summaries:

- **local**: Deterministic recipe-based generation (no API)
- **ollama**: Local Ollama subprocess (e.g., `llama3.2`)
- **sonnet**: Anthropic Claude Sonnet API (requires ANTHROPIC_API_KEY in secrets.json)
- **openai**: OpenAI API (requires OPENAI_API_KEY in secrets.json)

**Secrets file format** (`agent/secrets.json`):
```json
{
  "ANTHROPIC_API_KEY": "sk-ant-...",
  "OPENAI_API_KEY": "sk-..."
}
```

**Command example:**
```bash
python quartz/sigil_maker.py auto \
  --llm-provider sonnet \
  --sonnet-model claude-sonnet-4-20250514 \
  --secrets-path agent/secrets.json \
  --generate-count 5
```

## Common Tasks

### Add a new handcrafted spell
1. Create `content/Spells/SpellName.md` with full recipe
2. Add entry to appropriate rarity grimoire with `| Spell Page | [[Spells/SpellName|SpellName]] |`
3. Run `python quartz/spell_validator.py --report-only` to verify

### Generate 10 new spells
```bash
python quartz/sigil_maker.py auto \
  --generate-count 10 \
  --min-tier T2 --max-tier T5 \
  --llm-provider sonnet \
  --sync-grimoire-indexes
```

### Audit spell organization
```bash
python quartz/spell_validator.py --report-only
```

### Fix missing links after manual edits
```bash
python quartz/spell_validator.py --add-links
```

### Migrate legacy inline-only spells
```bash
python quartz/spell_validator.py --generate-missing --add-links
```

## Maintenance

### Regular checks
- Run validator after bulk spell generation
- Verify `content/Spells/` stays synchronized with grimoire pages
- Check that all grimoire entries have `| Spell Page |` links

### Backup before bulk operations
```bash
# Copy grimoire files before major migrations
cp content/*Grimoire.md backups/
```

## Tools Reference

### sigil_maker.py
- **Purpose**: Generate and validate spells from JSON specs
- **Key Commands**: `create`, `auto`, `recursive`, `gui`
- **Key Flags**: `--sync-grimoire-indexes`, `--generate-count`, `--llm-provider`

### spell_validator.py
- **Purpose**: Audit and fix spell organization
- **Key Flags**: `--report-only`, `--generate-missing`, `--add-links`
- **Safe to run**: Read-only with `--report-only`, writes with modification flags

## Troubleshooting

**Problem: Spell appears in grimoire but has no individual page**
```bash
python quartz/spell_validator.py --generate-missing
```

**Problem: Spell has individual page but grimoire doesn't link to it**
```bash
python quartz/spell_validator.py --add-links
```

**Problem: Duplicate spell entries**
- Manually edit grimoire file to remove duplicates
- Re-run validator to ensure links are correct

**Problem: Generated spell not appearing in grimoire**
- Check that `--sync-grimoire-indexes` flag was used
- Verify rarity tier is within `--min-tier` and `--max-tier` range
- Check terminal output for errors during generation
