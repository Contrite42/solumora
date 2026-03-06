#!/usr/bin/env python3
"""
Restore and rebuild grimoires from backup spell files with proper formatting.
"""

import re
from pathlib import Path

def clean_spell_block(block: str) -> str:
    """Remove Variable/Value header and clean up a spell block."""
    lines = block.strip().split('\n')
    
    if not lines or not lines[0].startswith('**'):
        return ""
    
    result = []
    result.append(lines[0])  # Spell name
    
    if len(lines) > 1:
        result.append(lines[1])  # Description
    
    # Skip the Variable/Value header and separator
    in_variables = False
    for i, line in enumerate(lines[2:], start=2):
        if line.startswith('| Variable'):
            in_variables = True
            continue
        if in_variables and line.startswith('|---|'):
            continue
        if in_variables and line.startswith('|'):
            # Only keep Wattage line
            if 'Wattage' in line:
                result.append(line)
        elif in_variables and not line.startswith('|'):
            break
    
    return '\n'.join(result)

def rebuild_grimoire(intro_text: str, spell_file: str, output_file: str):
    """Rebuild a grimoire from intro and spell file."""
    # Read spell file
    with open(spell_file, 'r', encoding='utf-8', errors='ignore') as f:
        spells = f.read()
    
    # Split into individual spells
    spell_blocks = spells.split('\n---\n\n')
    
    # Clean each spell
    cleaned_spells = []
    for block in spell_blocks:
        if block.strip():
            cleaned = clean_spell_block(block)
            if cleaned and '**' in cleaned:
                cleaned_spells.append(cleaned)
    
    # Rebuild content
    content = intro_text + '\n'
    for i, spell in enumerate(cleaned_spells):
        content += spell + '\n\n---\n\n'
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Rebuilt {Path(output_file).name} with {len(cleaned_spells)} spells")

if __name__ == "__main__":
    grimoires = [
        ("C:\\Users\\Contrite42\\quartz\\content\\Common Grimoire.md",
         "Common spells require [[Control Tier]] T1–T2 and represent the backbone of everyday [[Flux]] use across [[Solumora]]. The majority of the population can cast at least some of these. They are the spells found in every home, workshop, and market stall — mass-produced, widely copied, and deliberately simple.\n\n_Return to [[All Grimoire]]_",
         "C:\\Users\\Contrite42\\quartz\\new_common_spells.md"),
        
        ("C:\\Users\\Contrite42\\quartz\\content\\Uncommon Grimoire.md",
         "Uncommon spells require [[Control Tier]] T3–T4 and represent the threshold where casual Flux use ends and deliberate craft begins. A skilled Formulist can manage these, but they demand real training and precision. Most combat-ready spells live here, as do the first serious warding and detection tools.\n\n_Return to [[All Grimoire]]_",
         "C:\\Users\\Contrite42\\quartz\\new_uncommon_spells.md"),
        
        ("C:\\Users\\Contrite42\\quartz\\content\\Rare Grimoire.md",
         "Rare spells require [[Control Tier]] T5–T6 and are the exclusive territory of Channelers. At this level the exponential nature of [[Flux]] scaling means these casters are categorically different from the population below them. Rare spells are not found in mass-market [[Grimoires]] — they circulate through Scholars, private collections, and controlled institutional libraries. In [[Auralis]] some are openly studied; in [[Terravelle]] most require formal justification to possess.\n\n_Return to [[All Grimoire]]_",
         "C:\\Users\\Contrite42\\quartz\\new_rare_spells.md"),
        
        ("C:\\Users\\Contrite42\\quartz\\content\\Legendary Grimoire.md",
         "Legendary spells require [[Control Tier]] T7–T8 and exist at a tier of power where even possession becomes a political statement. These spells are theoretically documented, carefully locked away, and subject to formal scrutiny. Most major institutions hold only a handful of examples. The knowledge to create a Legendary-tier spell is itself considered classified in [[Terravelle]].\n\n_Return to [[All Grimoire]]_",
         "C:\\Users\\Contrite42\\quartz\\new_legendary_spells.md"),
        
        ("C:\\Users\\Contrite42\\quartz\\content\\Mythic Grimoire.md",
         "Mythic spells require [[Control Tier]] T9 and represent the upper bound of [[Flux]] theory. These spells demand everything a Conduit has to offer. Most exist only in fragments, theoretical notes, or as dangerous prototypes. The line between \"studied Mythic spell\" and \"uncontrolled Flux disaster\" is often a matter of luck, preparation, and nerve.\n\n_Return to [[All Grimoire]]_",
         "C:\\Users\\Contrite42\\quartz\\new_mythic_spells.md"),
        
        ("C:\\Users\\Contrite42\\quartz\\content\\Pale Grimoire.md",
         "Pale spells require [[Control Tier]] T9 and represent effects that brush against something beyond normal [[Flux]]. These are not simply powerful. A Pale spell is one whose effect operates at the boundary of what Flux can theoretically do. Where Mythic spells demand everything a Conduit has, Pale spells demand something more. Most [[Flux Users|Scholars]] who have studied them agree they should be documented. Fewer agree they should be cast.\n\n_Return to [[All Grimoire]]_",
         "C:\\Users\\Contrite42\\quartz\\new_pale_spells.md"),
    ]
    
    for output, intro, spell_file in grimoires:
        rebuild_grimoire(intro, spell_file, output)
    
    print("\nAll grimoires rebuilt!")
