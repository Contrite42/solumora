#!/usr/bin/env python3
"""
Rebuild grimoires with:
1. Better spell names matching their actual mechanics
2. Descriptions that match the recipe
3. Full recipe tables restored
"""

import re
from pathlib import Path
from typing import Dict, List

# Map mechanics to spell name components
HOOK_NAMES = {
    "Emit": "Wave",
    "Transform": "Shift", 
    "Sense": "Read",
    "Bind": "Lock",
    "Filter": "Screen",
    "Move": "Push",
    "Ward": "Guard",
    "Counter": "Break",
    "Control": "Weave"
}

DISCIPLINE_NAMES = {
    "Light": "Radiance",
    "Heat": "Flame",
    "Force": "Thrust",
    "Electric": "Bolt",
    "Chemical": "Flux",
    "Binding": "Chain",
    "Raw": "Core",
    "Mind": "Thought",
    "Sound": "Echo",
    "Soul": "Spirit"
}

PATTERN_NAMES = {
    "Point": "Point",
    "Plane": "Field",
    "Beam": "Ray",
    "Cone": "Spread",
    "Ring": "Ring",
    "Cylinder": "Column",
    "Sphere": "Orb",
    "Field": "Halo"
}

def generate_spell_name(hook: str, discipline: str, pattern: str) -> str:
    """Generate a spell name that matches its mechanics."""
    hook_name = HOOK_NAMES.get(hook, hook)
    disc_name = DISCIPLINE_NAMES.get(discipline, discipline)
    pattern_name = PATTERN_NAMES.get(pattern, pattern)
    
    # Build name from components
    # Format: [Discipline][Hook][Pattern] or variations
    name = f"{disc_name}{hook_name}{pattern_name}"
    return name

def generate_description(spell: Dict) -> str:
    """Generate a description that matches the recipe."""
    hook = spell.get('Hook', '')
    discipline = spell.get('Discipline', '')
    pattern = spell.get('Pattern', '')
    reach = spell.get('Reach', '')
    persistence = spell.get('Persistence', '')
    target = spell.get('Target', '')
    
    # Verb descriptions by hook
    verbs = {
        "Emit": "releases",
        "Transform": "alters",
        "Sense": "detects",
        "Bind": "constrains",
        "Filter": "filters out",
        "Move": "displaces",
        "Ward": "shields against",
        "Counter": "opposes",
        "Control": "manipulates"
    }
    
    verb = verbs.get(hook, "affects")
    
    # Build core description
    desc = f"{verb.capitalize()} {discipline.lower()}"
    
    if pattern and pattern != "Plane":
        desc += f" in a {pattern.lower()} pattern"
    else:
        desc += " across a surface"
    
    # Add reach if not default
    if reach and reach != "Self":
        desc += f" at {reach.lower()}"
    
    # Add target
    if target and target != "Where Written":
        desc += f", targeting {target.lower()}"
    
    # Add persistence
    if persistence and persistence != "Immediate":
        if "Timed" in persistence:
            desc += f", persisting {persistence.lower()}"
        elif persistence == "Sustained":
            desc += f", requiring sustained concentration"
        elif persistence == "Permanent":
            desc += f", creating a permanent effect"
    
    return desc + "."

def parse_wattage_line(line: str) -> str:
    """Extract wattage from a line."""
    match = re.search(r'(\d+)\s*W', line)
    if match:
        return match.group(1) + " W"
    return "0 W"

def spell_to_markdown(spell: Dict) -> str:
    """Convert spell dict to markdown with full recipe."""
    name = spell['name']
    description = spell['description']
    
    md = f"**{name}**\n"
    md += f"{description}\n"
    md += "| Variable | Value |\n"
    md += "|---|---|\n"
    
    # Add all recipe variables
    variables = ['Shape', 'Hook', 'Mode', 'Control Tier', 'Discipline', 'Output',
                 'Pattern', 'Reach', 'Persistence', 'Target', 'Wattage']
    
    for var in variables:
        if var in spell and spell[var]:
            value = spell[var]
            md += f"| {var} | {value} |\n"
    
    md += "\n---\n\n"
    return md

def parse_spell_from_backup(text: str) -> Dict:
    """Parse spell from the new_spells backup files."""
    lines = text.strip().split('\n')
    if not lines or not lines[0].startswith('**'):
        return None
    
    spell = {}
    spell['name'] = lines[0].strip('*').strip()
    
    # Find description line
    if len(lines) > 1:
        spell['description'] = lines[1].strip()
    
    # Parse variables from table
    in_vars = False
    for line in lines[2:]:
        if line.startswith('| Variable'):
            in_vars = True
            continue
        if in_vars and line.startswith('|---|'):
            continue
        if in_vars and line.startswith('|'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) == 2:
                key, value = parts
                # Clean value
                value = value.replace('_(default — ', '').replace(')_', '').strip()
                spell[key] = value
        elif in_vars and not line.startswith('|'):
            break
    
    return spell if 'Hook' in spell else None

def improve_spell(spell: Dict) -> Dict:
    """Improve a spell with better name and matching description."""
    # Generate better name
    hook = spell.get('Hook', '')
    discipline = spell.get('Discipline', '')
    pattern = spell.get('Pattern', 'Plane')
    
    new_name = generate_spell_name(hook, discipline, pattern)
    spell['name'] = new_name
    
    # Generate matching description
    new_desc = generate_description(spell)
    spell['description'] = new_desc
    
    return spell

def rebuild_grimoire_from_backup(intro: str, backup_file: str, output_file: str) -> int:
    """Rebuild grimoire from backup with improved names and descriptions."""
    # Read backup file
    with open(backup_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Split into spell blocks
    blocks = content.split('\n---\n\n')
    
    # Parse and improve each spell
    spells = []
    for block in blocks:
        if block.strip():
            spell = parse_spell_from_backup(block)
            if spell and 'Hook' in spell:
                spell = improve_spell(spell)
                spells.append(spell)
    
    # Build output
    output = intro + '\n'
    for spell in spells:
        output += spell_to_markdown(spell)
    
    # Write file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    return len(spells)

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
    
    print("Rebuilding grimoires with improved names and full recipes...\n")
    for output, intro, backup in grimoires:
        count = rebuild_grimoire_from_backup(intro, backup, output)
        name = Path(output).name
        print(f"✓ {name}: {count} spells")
    
    print("\nAll grimoires rebuilt with matching names, descriptions, and recipes!")
