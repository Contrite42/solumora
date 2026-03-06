#!/usr/bin/env python3
"""
Clean up spell linking after consolidating to grimoire-only source.
Removes "Spell Page" links from grimoire entries (no longer needed).
Updates All Grimoire and Spells.md to link to grimoire anchors.
"""

from __future__ import annotations

import re
from pathlib import Path

GRIMOIRES = [
    "content/Common Grimoire.md",
    "content/Uncommon Grimoire.md",
    "content/Rare Grimoire.md",
    "content/Legendary Grimoire.md",
    "content/Mythic Grimoire.md",
]

RARITY_TO_GRIMOIRE = {
    "Common": "Common Grimoire",
    "Uncommon": "Uncommon Grimoire",
    "Rare": "Rare Grimoire",
    "Legendary": "Legendary Grimoire",
    "Mythic": "Mythic Grimoire",
}


def remove_spell_page_links(grimoire_path: Path) -> int:
    """Remove '| Spell Page | [[Spells/...]] |' rows from grimoires."""
    if not grimoire_path.exists():
        return 0
    
    content = grimoire_path.read_text(encoding="utf-8")
    original = content
    
    # Remove | Spell Page | [[...]] | rows
    content = re.sub(r'\n\| Spell Page \| \[\[Spells/[^\]]+\]\] \|\n', '\n', content)
    
    if content != original:
        grimoire_path.write_text(content, encoding="utf-8")
        return 1
    return 0


def update_all_grimoire_links() -> bool:
    """Update All Grimoire links to point to grimoire pages instead of spell pages."""
    path = Path("content/All Grimoire.md")
    if not path.exists():
        return False
    
    content = path.read_text(encoding="utf-8")
    original = content
    
    # Change [[Spells/Name|Name]] to [[Grimoire#Name|Name]]
    # Find the grimoire for each spell and create proper anchor link
    def replace_link(match: re.Match[str]) -> str:
        spell_name = match.group(1)
        # Find which grimoire this spell is in
        for grimoire_path in GRIMOIRES:
            grim = Path(grimoire_path)
            if not grim.exists():
                continue
            grim_content = grim.read_text(encoding="utf-8")
            if f"**{spell_name}**" in grim_content:
                grimoire_name = grim.stem  # e.g., "Common Grimoire"
                return f"[[{grimoire_name}#{spell_name}|{spell_name}]]"
        # Fallback: keep original if spell not found (shouldn't happen)
        return match.group(0)
    
    # Replace spell links with grimoire anchor links
    content = re.sub(
        r'\[\[Spells/([^\]|]+)\|([^\]]+)\]\]',
        replace_link,
        content
    )
    
    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def update_spells_hub_links() -> bool:
    """Update Spells.md hub to link to grimoire entries."""
    path = Path("content/Spells.md")
    if not path.exists():
        return False
    
    content = path.read_text(encoding="utf-8")
    original = content
    
    # Change [[Spells/Name|Name]] to [[Grimoire#Name|Name]]
    def replace_link(match: re.Match[str]) -> str:
        spell_name = match.group(1)
        for grimoire_path in GRIMOIRES:
            grim = Path(grimoire_path)
            if not grim.exists():
                continue
            grim_content = grim.read_text(encoding="utf-8")
            if f"**{spell_name}**" in grim_content:
                grimoire_name = grim.stem
                return f"[[{grimoire_name}#{spell_name}|{spell_name}]]"
        return match.group(0)
    
    content = re.sub(
        r'\[\[Spells/([^\]|]+)\|([^\]]+)\]\]',
        replace_link,
        content
    )
    
    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main() -> None:
    print("Cleaning up spell links after consolidation...\n")
    
    # Remove Spell Page links from grimoires
    print("1. Removing 'Spell Page' link rows from grimoires...")
    for grimoire in GRIMOIRES:
        if remove_spell_page_links(Path(grimoire)):
            print(f"   ✓ {Path(grimoire).name}")
    
    # Update All Grimoire links
    print("\n2. Updating All Grimoire links...")
    if update_all_grimoire_links():
        print("   ✓ All Grimoire links updated to grimoire anchors")
    else:
        print("   - All Grimoire not found or no changes needed")
    
    # Update Spells.md hub links
    print("\n3. Updating Spells.md hub links...")
    if update_spells_hub_links():
        print("   ✓ Spells.md links updated to grimoire anchors")
    else:
        print("   - Spells.md not found or no changes needed")
    
    print("\n✓ Cleanup complete. Spells now consolidated to grimoires.")


if __name__ == "__main__":
    main()
