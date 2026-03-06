#!/usr/bin/env python3
"""
Rebuild grimoires with:
1. Proper fantasy spell names (not descriptive, not procedural)
2. Simple format: Name → Description → Wattage only
3. Names that sound like actual spells
"""

import random
from pathlib import Path
from typing import Dict, List
import re

# Fantasy spell name components - adjectives and nouns
ADJECTIVES = [
    "Bright", "Dark", "Swift", "Slow", "Sharp", "Dull", "Cold", "Warm", "Deep", "Shallow",
    "Still", "Whirling", "Quiet", "Loud", "Clear", "Murky", "Weak", "Strong", "Pale", "Vivid",
    "Ancient", "Fresh", "Tainted", "Pure", "Wild", "Tame", "Hollow", "Solid", "Gentle", "Fierce",
    "Humble", "Grand", "Hidden", "Naked", "Curved", "Straight", "Fragile", "Hardy", "Heavy", "Light",
    "Twin", "Lone", "Vast", "Tiny", "Burning", "Frozen", "Drifting", "Anchored", "Restless", "Steady"
]

NOUNS = [
    "Mark", "Ward", "Seal", "Sigil", "Lock", "Key", "Bond", "Chain", "Knot", "Web",
    "Ring", "Pulse", "Breath", "Touch", "Flame", "Frost", "Storm", "Calm", "Echo", "Silence",
    "Path", "Gate", "Door", "Wall", "Bridge", "Void", "Core", "Shell", "Root", "Crown",
    "Eye", "Hand", "Heart", "Voice", "Soul", "Spirit", "Wisp", "Shroud", "Veil", "Mirror",
    "Thread", "Net", "Cage", "Halo", "Aura", "Curse", "Boon", "Rune", "Glyph", "Charm"
]

# Longer poetic spell names (alternative to adjective+noun)
SPELL_NAME_PREFIXES = [
    "Shatter", "Pierce", "Weave", "Bind", "Break", "Transform", "Dissolve", "Kindle",
    "Chill", "Surge", "Drift", "Anchor", "Rise", "Fall", "Twist", "Sweep",
    "Guard", "Pierce", "Release", "Capture", "Flow", "Freeze", "Burn", "Calm"
]

SPELL_NAME_SUFFIXES = [
    "strike", "blessing", "curse", "dance", "song", "scar", "mark", "brand",
    "veil", "sight", "touch", "breath", "pulse", "bond", "road", "way",
    "light", "shadow", "thought", "dream", "storm", "tide", "flame", "frost"
]

def generate_spell_name():
    """Generate a proper fantasy spell name."""
    choice = random.randint(0, 2)
    
    if choice == 0:
        # Adjective + Noun (e.g., "SweetMarrow", "SharpEdge")
        adj = random.choice(ADJECTIVES)
        noun = random.choice(NOUNS)
        return adj + noun
    elif choice == 1:
        # Verb + adjective + noun (e.g., "WeavingFrost")
        verb = random.choice(SPELL_NAME_PREFIXES)
        noun = random.choice(NOUNS)
        # Remove 'ing' if needed
        if verb.endswith('e'):
            verb = verb[:-1] + 'ing'
        else:
            verb = verb + 'ing'
        return verb.rstrip('ing') + noun
    else:
        # Two syllable poetic names
        prefix = random.choice(SPELL_NAME_PREFIXES)
        suffix = random.choice(SPELL_NAME_SUFFIXES)
        return prefix + suffix.capitalize()

def parse_spell_from_backup(text: str) -> Dict:
    """Parse spell from the backup files."""
    lines = text.strip().split('\n')
    if not lines or not lines[0].startswith('**'):
        return None
    
    spell = {}
    
    # Find description - skip formula lines
    desc_idx = 1
    while desc_idx < len(lines):
        if not lines[desc_idx].startswith('|') and lines[desc_idx].strip():
            spell['description'] = lines[desc_idx].strip()
            break
        desc_idx += 1
    
    # Parse variables from table
    in_vars = False
    for line in lines[desc_idx+1:]:
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
                value = value.replace('_(default — ', '').replace(')_', '').replace('_(default – ', '').strip()
                value = re.sub(r'_?\(default [–—] ', '', value).rstrip(')_')
                spell[key] = value
        elif in_vars and not line.startswith('|'):
            break
    
    return spell if 'Wattage' in spell else None

def generate_description_from_recipe(spell: Dict) -> str:
    """Generate a single-sentence description from the recipe."""
    hook = spell.get('Hook', '')
    discipline = spell.get('Discipline', '')
    pattern = spell.get('Pattern', '')
    reach = spell.get('Reach', '')
    persistence = spell.get('Persistence', '')
    target = spell.get('Target', '')
    
    # Verb by hook
    verbs = {
        "Emit": "releases",
        "Transform": "alters",
        "Sense": "detects",
        "Bind": "constrains",
        "Filter": "filters",
        "Move": "displaces",
        "Ward": "shields against",
        "Counter": "opposes",
        "Control": "manipulates"
    }
    
    verb = verbs.get(hook, "affects")
    
    # Build simple one-sentence description
    parts = [f"{verb.capitalize()} {discipline.lower()}"]
    
    if pattern and pattern not in ["Plane", "default"]:
        parts.append(f"in a {pattern.lower()}")
    else:
        parts.append("across surfaces")
    
    if reach and reach not in ["Self", "default"]:
        parts.append(f"at {reach.lower()}")
    
    if target and target not in ["Where Written", "default"]:
        parts.append(f"targeting {target.lower()}")
    
    desc = " ".join(parts) + "."
    return desc

def spell_to_markdown(name: str, description: str, spell: Dict) -> str:
    """Convert to format: Name → Description → Full Recipe Table."""
    md = f"**{name}**\n"
    md += f"{description}\n"
    md += "| Variable | Value |\n"
    md += "|---|---|\n"
    
    # Add variables in order
    variables = ['Shape', 'Hook', 'Mode', 'Control Tier', 'Discipline', 'Output',
                 'Pattern', 'Reach', 'Persistence', 'Target', 'Wattage']
    
    for var in variables:
        if var in spell and spell[var]:
            md += f"| {var} | {spell[var]} |\n"
    
    md += "\n---\n\n"
    return md

def rebuild_grimoire_with_recipes(intro: str, backup_file: str, output_file: str) -> int:
    """Rebuild grimoire with proper format."""
    # Read backup
    with open(backup_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Parse spells
    blocks = content.split('\n---\n\n')
    spells = []
    used_names = set()
    
    for block in blocks:
        if block.strip():
            spell = parse_spell_from_backup(block)
            if spell and 'Wattage' in spell:
                # Generate unique name
                name = generate_spell_name()
                attempts = 0
                while name in used_names and attempts < 10:
                    name = generate_spell_name()
                    attempts += 1
                
                if name not in used_names:
                    used_names.add(name)
                    desc = generate_description_from_recipe(spell)
                    spells.append((name, desc, spell))
    
    # Build output
    output = intro + '\n'
    for name, desc, spell in spells:
        output += spell_to_markdown(name, desc, spell)
    
    # Write
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
    
    print("Rebuilding grimoires with names, descriptions, and full recipe tables...\n")
    for output, intro, backup in grimoires:
        count = rebuild_grimoire_with_recipes(intro, backup, output)
        name = Path(output).name
        print(f"✓ {name}: {count} spells")
    
    print("\nAll grimoires rebuilt with proper format!")
