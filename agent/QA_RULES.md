# QA Rules for Solumora Vault

Rules for the GPT QA + Linking agent. Conservative by design. When in doubt, do nothing.

---

## PRIMARY RULE

**Only add links to pages that already exist.** Never suggest a link to a page title you cannot confirm exists in the vault. The cost of a broken link is higher than the cost of a missing link.

---

## LINK SAFETY RULES

1. Before suggesting any `[[Title]]` link, verify the title appears in the KNOWN TITLES list provided in the prompt.
2. If a title is not in the known titles list, do NOT suggest it.
3. Do not create new pages. You are a linker and checker, not a content generator.
4. Do not add links inside code fences, blockquotes, or See Also sections (the See Also section is already curated by the author).
5. Maximum 3 link suggestions per file. Quality over quantity.
6. Only suggest a link if the title appears as a recognizable noun phrase in the text (not just as a tangentially related concept).

---

## FORBIDDEN LINK TARGETS

These pages do not exist and must never be linked:

- Any page not in the KNOWN TITLES list
- "Admin" pages: tags, templates, utility pages, navigation aids
- Pages that look like meta-structure (e.g. "Home", "Dashboard", "MOC", "Index" links unless index.md)

If you see existing text linking to a non-existent page, flag it as an inconsistency. Do not fix it yourself — report it.

---

## CANON CONSISTENCY CHECKS

When reviewing changed files, flag any of the following as inconsistencies:

**Naming violations:**

- Character with compound poetic surname (Darkhaven, Earthsong, Moonwhisper, etc.)
- Character named "X the Bold/Wise/Swift" etc.
- Place name that sounds like generic fantasy (Zha'thik, Khyronia, Nefaria, Aridos, etc.)
- Faction name that sounds like D&D (Shadowhand Brotherhood, Ironfist Legion, Luminari Enclave)

**Lore violations:**

- A sixth High Demon mentioned (only 5 exist: Selvane, Mave, Fennick, Wren, Sorath)
- A T9 practitioner described as active and known
- Someone knowing the Watts=ancient civilization secret (only Sera Voss knows this)
- Someone knowing a High Demon's true identity (none of the ground-level characters know)
- A new kingdom, continent, or cosmological system invented
- New magic types beyond Sigils, Hand Signs, Hypertext

**Structural violations:**

- A note with no See Also section
- A new page that doesn't link to at least 3 existing pages
- A character with a Control Tier above T7 who is not one of the established principal characters
- A note that resolves a narrative thread (Watts secret, High Demon reveals, political resolution)

**Geographic violations:**

- A location not in Terravelle, Auralis, or the Equatorial Desert region
- A reference to a second continent or ocean crossing
- A new city in Terravelle that is not: Valdenmoor, Ashford, Greyveil, Wolfpoint (or a hamlet/village clearly subordinate to these)
- A new city in Auralis that is not: Solhaven, Hedun, Halveth, Emberfall (or subordinate)

---

## HUB PAGE UPDATES

When Claude creates new notes that belong to an existing hub or index page, you may suggest append-only additions:

- Add the new page to "See Also" of the nearest parent location/concept page
- Do NOT rewrite existing hub content — only append

Safe hub pages to append to:

- `content/index.md` — only if a major new reading path is warranted
- `content/Terravelle.md`, `content/Auralis.md` — location child pages
- `content/The Council of Auralis.md` — new Council-related pages
- `content/History of Solumora.md` — new historical events

NEVER append to:

- Individual character pages (they are self-contained)
- Lore pages (Flux, Control Tier, etc.) unless directly extending those systems

---

## REPORT FORMAT

### inconsistencies.md

```
# Inconsistencies

## [filename]
- Issue: [what is wrong]
- Evidence: [quote from the file]
```

### links_applied.md

```
# Links Applied

- [filename]: linked [[Title]]
```

If no inconsistencies found: write "None detected."
If no links applied: write "No link edits applied."

---

## WHAT YOU ARE NOT ALLOWED TO DO

- Generate new worldbuilding content
- Rewrite or rephrase existing content
- Change narrative tone or voice
- Add commentary or suggestions beyond the report format
- Suggest splitting or merging notes
- Suggest adding new sections to existing notes
- Create new files of any kind
