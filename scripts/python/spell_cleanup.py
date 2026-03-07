#!/usr/bin/env python3
"""
Clean up and improve spell descriptions across all grimoires.
Removes header rows and generates accurate descriptions based on spell mechanics.
"""

import re
from pathlib import Path
from typing import List, Tuple, Dict

# Description templates based on hook + discipline combinations
HOOK_DESCRIPTIONS = {
    "Emit": {
        "Light": "projects photonic energy",
        "Heat": "releases thermal energy",
        "Force": "releases a kinetic blast",
        "Electric": "discharges electrical energy",
        "Chemical": "releases reactive compounds",
        "Binding": "projects constraining force",
        "Raw": "emits raw flux energy",
        "Mind": "broadcasts mental energy",
        "Sound": "releases sonic energy",
        "Soul": "projects soul-aligned energy"
    },
    "Transform": {
        "Light": "alters light properties",
        "Heat": "transfers or removes heat",
        "Force": "reshapes kinetic properties",
        "Electric": "transforms electrical charge",
        "Chemical": "alters chemical state",
        "Binding": "transforms constraint structure",
        "Raw": "transforms raw material properties",
        "Mind": "restructures mental patterns",
        "Sound": "transforms sonic properties",
        "Soul": "alters soul-aligned properties"
    },
    "Sense": {
        "Light": "detects photonic signatures",
        "Heat": "senses thermal patterns",
        "Force": "detects kinetic disruption",
        "Electric": "senses electrical charge",
        "Chemical": "detects chemical composition",
        "Binding": "senses constraint structure",
        "Raw": "reads raw flux signatures",
        "Mind": "senses mental signatures",
        "Sound": "detects sonic disturbance",
        "Soul": "reads soul signatures"
    },
    "Bind": {
        "Light": "constrains photonic energy",
        "Heat": "binds thermal properties",
        "Force": "constrains kinetic force",
        "Electric": "binds electrical charge",
        "Chemical": "binds chemical compounds",
        "Binding": "creates constraining bonds",
        "Raw": "binds raw flux",
        "Mind": "binds mental patterns",
        "Sound": "constrains sonic energy",
        "Soul": "binds soul-aligned force"
    },
    "Filter": {
        "Light": "filters light and photonics",
        "Heat": "filters thermal energy",
        "Force": "filters kinetic force",
        "Electric": "filters electrical discharge",
        "Chemical": "filters chemical compounds",
        "Binding": "filters constraining force",
        "Raw": "filters raw flux",
        "Mind": "filters mental interference",
        "Sound": "filters sonic disturbance",
        "Soul": "filters soul-aligned interference"
    },
    "Move": {
        "Light": "redirects light and photonics",
        "Heat": "displaces thermal energy",
        "Force": "displaces objects and kinetic force",
        "Electric": "redirects electrical discharge",
        "Chemical": "displaces chemical compounds",
        "Binding": "displaces constraints",
        "Raw": "redirects raw flux",
        "Mind": "redirects mental patterns",
        "Sound": "redirects sonic waves",
        "Soul": "displaces soul-aligned energy"
    },
    "Ward": {
        "Light": "shields against photonic disturbance",
        "Heat": "shields against thermal effects",
        "Force": "shields against kinetic impact",
        "Electric": "shields against electrical discharge",
        "Chemical": "shields against chemical compounds",
        "Binding": "shields against constraints",
        "Raw": "shields against raw flux",
        "Mind": "shields against mental intrusion",
        "Sound": "shields against sonic disturbance",
        "Soul": "shields against soul-aligned effects"
    },
    "Counter": {
        "Light": "counters photonic effects",
        "Heat": "counters thermal effects",
        "Force": "counters kinetic force",
        "Electric": "counters electrical discharge",
        "Chemical": "counters chemical effects",
        "Binding": "counters constraining bonds",
        "Raw": "counters raw flux effects",
        "Mind": "counters mental effects",
        "Sound": "counters sonic disturbance",
        "Soul": "counters soul-aligned effects"
    },
    "Control": {
        "Light": "controls photonic manifestations",
        "Heat": "controls thermal manifestations",
        "Force": "controls kinetic manifestations",
        "Electric": "controls electrical manifestations",
        "Chemical": "controls chemical reactions",
        "Binding": "controls constraint structures",
        "Raw": "controls raw flux manifestations",
        "Mind": "controls mental manifestations",
        "Sound": "controls sonic manifestations",
        "Soul": "controls soul-aligned manifestations"
    }
}

# Pattern cost descriptions
PATTERN_DESCRIPTIONS = {
    "Point": "at a single point",
    "Plane": "across a flat surface",
    "Beam": "in a concentrated beam",
    "Cone": "in a spreading cone",
    "Ring": "in a circular pattern",
    "Cylinder": "in a cylindrical column",
    "Sphere": "in a spherical radius",
    "Field": "across a sustained field area"
}

# Reach descriptions
REACH_DESCRIPTIONS = {
    "Self": "from the caster",
    "Touch": "at touch range",
    "Short (10 ft)": "up to 10 feet away",
    "Medium (50 ft)": "up to 50 feet away",
    "Long (200 ft)": "up to 200 feet away",
    "Line-of-Sight": "anywhere in line of sight",
    "Linked": "through linked connections",
    "Anchored": "from a fixed anchor point"
}

# Persistence descriptions
PERSISTENCE_DESCRIPTIONS = {
    "Immediate": "on activation",
    "Timed (Short)": "for up to one minute",
    "Timed (Long)": "for up to one hour",
    "Sustained": "while maintained by the caster",
    "Conditional": "until a condition is met",
    "Latched": "until manually dismissed",
    "Permanent": "permanently"
}

def parse_spell_block(text: str) -> Dict:
    """Parse a single spell block from grimoire markdown."""
    lines = text.strip().split('\n')
    if not lines or not lines[0].startswith('**'):
        return None
    
    spell = {}
    spell['name'] = lines[0].strip('*')
    spell['description'] = lines[1] if len(lines) > 1 else ""
    
    # Parse variables
    in_variables = False
    for i, line in enumerate(lines[2:], start=2):
        if line.startswith('| Variable'):
            in_variables = True
            continue
        if in_variables and line.startswith('|---|'):
            continue
        if in_variables and line.startswith('|'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) == 2:
                key, value = parts
                # Clean up defaults notation
                value = value.replace('_(default — ', '').replace(')_', '').replace('_(default – ', '').replace('_(default – ', '').strip()
                # Also handle em-dash variants
                value = re.sub(r'_?\(default [–—] ', '', value).rstrip(')_')
                spell[key] = value
        elif in_variables and not line.startswith('|'):
            break
    
    return spell if spell.get('Hook') else None

def generate_description(spell: Dict) -> str:
    """Generate an accurate, detailed description based on spell mechanics."""
    hook = spell.get('Hook', '')
    discipline = spell.get('Discipline', '')
    pattern = spell.get('Pattern', 'Plane').strip()
    reach = spell.get('Reach', 'Self').strip()
    persistence = spell.get('Persistence', 'Immediate').strip()
    target = spell.get('Target', 'Where Written').strip()
    mode = spell.get('Mode', '')
    
    # Get base action
    base_action = HOOK_DESCRIPTIONS.get(hook, {}).get(discipline, f"{hook.lower()}s {discipline.lower()}")
    
    # Build description - only include non-default values
    parts = [base_action]
    
    # Only add pattern if not default (Plane)
    if pattern and pattern != "Plane":
        pattern_desc = PATTERN_DESCRIPTIONS.get(pattern, f"in a {pattern.lower()} pattern")
        parts.append(pattern_desc)
    else:
        parts.append("across a flat surface")  # Default pattern description
    
    # Only add reach if not default (Self)
    if reach and reach != "Self":
        reach_desc = REACH_DESCRIPTIONS.get(reach, f"at {reach.lower()} range")
        parts.append(reach_desc)
    else:
        parts.append("from the sigil location")  # Default reach description
    
    # Target-specific context
    target_context = {
        "Where Written": "where inscribed",
        "Self": "from the sigil location",
        "Object": "on objects",
        "Surface": "on surfaces", 
        "Individual": "on an individual target",
        "Group": "on groups of targets",
        "Filter": "filtering by specified criteria",
        "Marked": "on marked targets",
        "Search": "searching an area"
    }
    target_desc = target_context.get(target, target)
    parts.append(f"affecting {target_desc}")
    
    # Build final description
    description = " ".join(parts).rstrip() + "."
    
    # Add persistence note if not immediate
    if persistence and persistence != "Immediate":
        if persistence == "Sustained":
            description = description.rstrip(".") + " Requires sustained concentration."
        elif "Timed" in persistence:
            description = description.rstrip(".") + f" Persists {PERSISTENCE_DESCRIPTIONS.get(persistence, persistence.lower())}."
        elif persistence == "Permanent":
            description = description.rstrip(".") + f" The effect persists {PERSISTENCE_DESCRIPTIONS.get(persistence, persistence.lower())}."
    
    return description

def spell_block_to_clean_markdown(spell: Dict) -> str:
    """Convert spell to clean markdown with only wattage displayed."""
    # Generate new description
    new_desc = generate_description(spell)
    
    # Build markdown
    md = f"**{spell['name']}**\n"
    md += f"{new_desc}\n"
    
    # Only show wattage if present
    if 'Wattage' in spell:
        md += f"**Wattage:** {spell['Wattage']}\n"
    
    md += "\n---\n\n"
    return md

def clean_grimoire_file(filepath: str) -> str:
    """Process a grimoire file and return cleaned content."""
    # Try different encodings
    for encoding in ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']:
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    else:
        print(f"  Warning: Could not decode {filepath}, skipping")
        return ""
    
    # Split by spell separator
    intro = content.split('\n---\n\n')[0] + '\n\n---\n\n'
    spells_raw = '\n---\n\n'.join(content.split('\n---\n\n')[1:])
    
    # Process each spell
    spell_blocks = spells_raw.split('\n---\n\n')
    cleaned_spells = []
    
    for block in spell_blocks:
        if not block.strip():
            continue
        spell = parse_spell_block(block)
        if spell:
            cleaned_spells.append(spell_block_to_clean_markdown(spell))
    
    return intro + ''.join(cleaned_spells)

if __name__ == "__main__":
    grimoires = [
        "C:\\Users\\Contrite42\\quartz\\content\\Common Grimoire.md",
        "C:\\Users\\Contrite42\\quartz\\content\\Uncommon Grimoire.md",
        "C:\\Users\\Contrite42\\quartz\\content\\Rare Grimoire.md",
        "C:\\Users\\Contrite42\\quartz\\content\\Legendary Grimoire.md",
        "C:\\Users\\Contrite42\\quartz\\content\\Mythic Grimoire.md",
        "C:\\Users\\Contrite42\\quartz\\content\\Pale Grimoire.md"
    ]
    
    for grimoire_path in grimoires:
        if Path(grimoire_path).exists():
            print(f"Cleaning {Path(grimoire_path).name}...")
            cleaned = clean_grimoire_file(grimoire_path)
            if cleaned:
                # Write with proper encoding handling
                try:
                    with open(grimoire_path, 'w', encoding='utf-8') as f:
                        f.write(cleaned)
                    print(f"  ✓ Complete")
                except Exception as e:
                    print(f"  ✗ Error writing: {e}")
    
    print("\nAll grimoires cleaned and descriptions updated!")
