# Solumora Style Guide

Writing conventions for all vault notes. Violating these breaks the reader experience.

---

## VOICE AND TONE

- **Matter-of-fact**. The world is real to its inhabitants. Write like an encyclopedia or field guide, not a fantasy novel.
- **No purple prose**. Never: "gleaming towers", "ancient mystical power", "destined hero", "dark evil"
- **Dense, specific**. Every sentence should carry information. No filler sentences.
- **Present tense** for facts about the world. Past tense for historical events.
- **People are in motion**. Characters have jobs, routines, specific problems. They are not archetypes.

**GOOD voice:**

> Osvin Brack keeps a running ledger of every Flux assessment in Valdenmoor's merchant quarter going back eleven years. He knows who upgraded, who tested out, who was reassessed after an accident. He does not share this information freely.

**BAD voice:**

> In the mystical land of Solumora, brave heroes wield ancient powers to protect their realm from darkness...

---

## NOTE STRUCTURE

Every note follows this pattern:

```
[1–3 opening paragraphs establishing what this is and why it matters]

[Body: specific details, relationships, tensions, ongoing situations]

[Optional: subsections with ## headers for long notes]

*See also: [[Link1]], [[Link2]], [[Link3]]*
```

- **Opening**: No "Introduction" header. Start directly.
- **See Also**: Always at the end. Always uses `*italics*`. Minimum 3 links.
- **Headers**: Use `##` for subsections only when a note is long enough to need navigation (>400 words). Never use headers just for visual decoration.
- **No bullet lists as the main content**. Prose paragraphs. Bullets only for reference lists (like an inventory or a roster).

---

## NAMING RULES

### Character names

Short, terse, grounded. Germanic/Nordic feel. No melodrama.

**CORRECT patterns:**
| First | Surname |
|-------|---------|
| Sera | Voss |
| Eddan | Soln |
| Drest | Mourne |
| Cassia | Osl |
| Toven | Ral |
| Cor | Meln |
| Vel | Sorvn |
| Selt | Orvn |
| Brenne | Kalt |

**FORBIDDEN patterns — reject any name matching these:**

- Compound poetic surnames: Darkhaven, Earthsong, Moonwhisper, Blackwood, Stonefist, Greenhaven, Ironhand, Silvermist
- Epithets in names: "the Bold", "the Wise", "the Swift"
- Irish/Celtic: Niamh, Caoimhe, Aoife, Ciarán, Siobhán
- High-fantasy feel: Kaelin, Lila, Aria, Thrain, Zara, Lyra, Elara, Kira
- Apostrophe-containing names unless clearly from a specific existing culture reference

When creating new characters, follow this formula:

- 1–2 syllable first name (e.g. Coss, Veld, Orre, Teva, Ressa)
- 1–2 syllable surname (e.g. Dolt, Norn, Aldst, Cors, Vend)
- Check WORLD_STATE.md name conflict rules before finalizing

### Place names

Existing established places only unless the task explicitly calls for new ones. New place names must follow the same Germanic/grounded convention: Valdenmoor, Ashford, Greyveil, Wolfpoint, Halveth, Hedun, Emberfall, Solhaven.

FORBIDDEN new place names: Zha'thik, Aridos, Valtania, Khyronia, Nefaria, Luminara, Shadowmere, etc.

### Faction/Institution names

Functional and descriptive. FORBIDDEN: The Shadowhand Brotherhood, The Luminari Enclave, The Ironfist Legion. These are D&D names, not Solumora names.
CORRECT: Trade Guilds, Advancement Corps, Culmination Faction, Expansion Faction, Covenant of Measure.

---

## WIKI-LINKS

- Format: `[[Page Name]]` for exact page title
- Alias: `[[Page Name|display text]]` when you need different display text
- Only link to pages that exist. NEVER invent a link target.
- Link naturally in prose — first mention of a concept or person in a note.
- See Also section at the end lists the 3–8 most important related pages.

---

## WHAT EVERY NOTE MUST INCLUDE

**Location notes:**

- What is the place and what makes it distinct
- Who lives/works there (name specific individuals, including at least one ground-level person from WORLD_STATE.md if applicable)
- What tensions or ongoing situations exist there
- How it connects to the wider world

**Character notes:**

- What they do (job, role, daily life)
- Their Control Tier and what that means practically for them
- One specific thing they know or are doing that is NOT common knowledge
- Their relationship to at least one institution or faction
- See Also linking to relevant location and lore pages

**Lore/concept notes:**

- What it is, how it works
- Who uses it and why
- Specific examples grounded in named people/places
- Cost, limits, risks

---

## WHAT TO NEVER DO

- Do not invent new lore that contradicts WORLD_STATE.md
- Do not invent High Demons beyond Selvane, Mave, Fennick, Wren, Sorath
- Do not resolve narrative threads (Watts secret, High Demon reveals, etc.) — document the tension, do not end it
- Do not write from a hero's perspective
- Do not use the word "magical" — use "Flux-based" or "sigil-work" etc.
- Do not add new kingdoms, continents, gods, or cosmological systems
- Do not write about T9 practitioners as if they exist and are active
- Do not have characters know things they shouldn't (e.g. ground-level characters knowing High Demon identities)

---

## CONTENT FOLDER STRUCTURE

```
content/
  [root]          — world overview, index, geography, history
  Places/         — location notes
  People/         — character notes (both principal and ground-level)
  Factions/       — institutions, organizations, political blocs
  Lore/           — magic system, Watts, economics, Flux mechanics
  Life/            — "Life in X" pages, daily life, ordinary experience
  WrittenWorks/   — in-world documents (journals, ledgers, letters)
```

Note: many pages are in the content root, not subfolders. Check before creating.
