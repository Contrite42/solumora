#!/usr/bin/env python3
"""
Generate balanced spell rarity tiers following the exponential decay ratio.
Maintains: 100 Common : 50 Uncommon : 25 Rare : 13 Legendary : 6 Mythic : 3 Pale
"""

import random
import math
from typing import List, Tuple

# Common Grimoire spell templates (T0-T2)
COMMON_ADJECTIVES = [
    "Steady", "Quick", "Bright", "Dark", "Cold", "Warm", "Sharp", "Dull", "Clear", "Cloudy",
    "Swift", "Slow", "Strong", "Weak", "High", "Low", "Noble", "Base", "Pure", "Mixed",
    "Keen", "Blunt", "Clean", "Soiled", "Dry", "Wet", "Hard", "Soft", "Loud", "Quiet",
    "Deep", "Shallow", "Wide", "Narrow", "Long", "Short", "Thick", "Thin", "Fair", "Foul",
    "Fresh", "Stale", "Neat", "Messy", "Tight", "Loose", "Inner", "Outer", "Sure", "Unsure",
    "Still", "Active", "Light", "Heavy", "Dense", "Sparse", "Smooth", "Rough", "True", "False"
]

COMMON_NOUNS = [
    "Spark", "Flame", "Light", "Shadow", "Wind", "Wave", "Stone", "Leaf", "Frost", "Heat",
    "Mark", "Seal", "Ward", "Guard", "Lock", "Key", "Bond", "Link", "Core", "Gate",
    "Touch", "Push", "Pull", "Turn", "Shift", "Flow", "Bind", "Break", "Read", "Write",
    "Sense", "Filter", "Catch", "Hold", "Keep", "Send", "Draw", "Give", "Take", "Trace",
    "Pulse", "Echo", "Ring", "Hum", "Chime", "Tone", "Note", "Song", "Voice", "Call",
    "Point", "Line", "Plane", "Sphere", "Ring", "Mesh", "Web", "Net", "Cage", "Box",
    "Knot", "Weave", "Thread", "Loop", "Coil", "Spiral", "Anchor", "Tether", "Chain", "Rope",
    "Disk", "Plate", "Slab", "Block", "Cube", "Column", "Arch", "Beam", "Beam", "Frame"
]

# Spell mechanics for Common tier
COMMON_SHAPES = ["Triangle", "Square"]  # Common uses simpler shapes
COMMON_HOOKS = ["Emit", "Transform", "Sense", "Bind", "Filter", "Move", "Ward"]
COMMON_MODES = ["Create", "Affect"]  # Common uses simpler modes
COMMON_DISCIPLINES = ["Light", "Heat", "Force", "Chemical", "Electric", "Binding", "Raw"]
COMMON_OUTPUTS = {
    "Light": "Photonic",
    "Heat": "Thermal",
    "Force": "Kinetic",
    "Chemical": "Reactive",
    "Electric": "Shock",
    "Binding": "Constraint",
    "Raw": "Raw"
}
COMMON_PATTERNS = ["_(default — Plane)_", "Point", "Plane", "Cone"]
COMMON_REACHES = ["_(default — Self)_", "Touch", "Short (10 ft)"]
COMMON_PERSISTENCES = ["_(default — Immediate)_", "Timed (Short)", "Timed (Long)", "Sustained"]
COMMON_TARGETS = ["_(default — Where Written)_", "Object", "Surface"]

def generate_spell_name() -> str:
    """Generate a random spell name."""
    adj = random.choice(COMMON_ADJECTIVES)
    noun = random.choice(COMMON_NOUNS)
    # 20% chance of compound names
    if random.random() < 0.2:
        noun2 = random.choice(COMMON_NOUNS)
        return f"{adj}{noun}{noun2}"
    return f"{adj}{noun}"

def calculate_wattage(shape: str, discipline: str, pattern: str, reach: str, persistence: str, target: str) -> int:
    """Calculate Watts for a spell based on its components."""
    # Shape base
    shape_costs = {"Triangle": 3, "Square": 8, "Pentagon": 20, "Circle": 55}
    base_w = shape_costs.get(shape, 3)
    
    # Discipline multiplier
    discipline_multipliers = {
        "Raw": 1, "Force": 2, "Heat": 2, "Light": 3, "Sound": 4,
        "Electric": 5, "Chemical": 5, "Binding": 10, "Mind": 25, "Soul": 75
    }
    mult = discipline_multipliers.get(discipline, 1)
    core_w = base_w * mult
    
    # Pattern cost
    pattern_costs = {
        "$(default — Plane)$": 0, "Point": 0, "Plane": 0, "Beam": 5,
        "Cone": 10, "Ring": 15, "Cylinder": 20, "Sphere": 30, "Field": 60
    }
    pattern_w = pattern_costs.get(pattern, 0)
    
    # Reach cost
    reach_costs = {
        "$(default — Self)$": 0, "Touch": 2, "Short (10 ft)": 5,
        "Medium (50 ft)": 15, "Long (200 ft)": 40, "Line-of-Sight": 80, "Linked": 150
    }
    reach_w = reach_costs.get(reach, 0)
    
    # Persistence cost
    persistence_costs = {
        "$(default — Immediate)$": 0, "Timed (Short)": 5, "Timed (Long)": 25,
        "Sustained": 10, "Conditional": 20, "Latched": 40, "Permanent": 400
    }
    persistent_w = persistence_costs.get(persistence, 0)
    
    # Target cost
    target_costs = {
        "$(default — Where Written)$": 0, "Self": 0, "Object": 2,
        "Surface": 5, "Individual": 8, "Marked": 15, "Group": 35, "Filter": 60
    }
    target_w = target_costs.get(target, 0)
    
    total = core_w + pattern_w + reach_w + persistent_w + target_w
    return max(1, total)

def determine_control_tier(wattage: int) -> str:
    """Determine control tier based on wattage."""
    if wattage <= 10:
        return "T0"
    elif wattage <= 40:
        return "T1"
    elif wattage <= 130:
        return "T2"
    elif wattage <= 400:
        return "T3"
    elif wattage <= 1300:
        return "T4"
    elif wattage <= 4000:
        return "T5"
    else:
        return "T6"

def generate_common_spell() -> Tuple[str, dict]:
    """Generate a single Common tier spell."""
    shape = random.choice(COMMON_SHAPES)
    hook = random.choice(COMMON_HOOKS)
    mode = random.choice(COMMON_MODES)
    discipline = random.choice(COMMON_DISCIPLINES)
    output = COMMON_OUTPUTS[discipline]
    pattern = random.choice(COMMON_PATTERNS)
    reach = random.choice(COMMON_REACHES)
    persistence = random.choice(COMMON_PERSISTENCES)
    target = random.choice(COMMON_TARGETS)
    
    wattage = calculate_wattage(shape, discipline, pattern, reach, persistence, target)
    control_tier = determine_control_tier(wattage)
    
    # Ensure Common tier (T0-T2)
    if control_tier not in ["T0", "T1", "T2"]:
        # Retry until we get a Common tier spell
        return generate_common_spell()
    
    name = generate_spell_name()
    
    spell = {
        "name": name,
        "shape": shape,
        "hook": hook,
        "mode": mode,
        "control_tier": control_tier,
        "discipline": discipline,
        "output": output,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target": target,
        "wattage": wattage
    }
    
    return name, spell

def generate_description(spell: dict) -> str:
    """Generate a flavor text description for a spell."""
    hooks = {
        "Emit": "releases",
        "Transform": "alters",
        "Sense": "detects",
        "Bind": "constrains",
        "Filter": "filters",
        "Move": "displaces",
        "Ward": "protects against"
    }
    
    disciplines_flavor = {
        "Light": "light",
        "Heat": "thermal energy",
        "Force": "kinetic force",
        "Chemical": "reactive compounds",
        "Electric": "electrical charge",
        "Binding": "constraining force",
        "Raw": "raw energy"
    }
    
    hook_verb = hooks.get(spell["hook"], "affects")
    discipline_obj = disciplines_flavor.get(spell["discipline"], "energy")
    
    descriptions = [
        f"A practical spell that {hook_verb} {discipline_obj} across the inscribed surface.",
        f"Inscribed sigil that {hook_verb} {discipline_obj} in a controlled manner.",
        f"Common utility spell designed to {hook_verb} {discipline_obj} reliably.",
        f"Straightforward spell that {hook_verb} {discipline_obj} with precision.",
        f"Everyday spell that {hook_verb} {discipline_obj} for practical purposes.",
    ]
    
    return random.choice(descriptions)

def spell_to_markdown(name: str, spell: dict) -> str:
    """Convert a spell dict to markdown format."""
    description = generate_description(spell)
    
    pattern_display = spell["pattern"]
    reach_display = spell["reach"]
    persistence_display = spell["persistence"]
    target_display = spell["target"]
    
    md = f"""**{name}**
{description}
| Variable | Value |
|---|---|
| Shape | {spell['shape']} |
| Hook | {spell['hook']} |
| Mode | {spell['mode']} |
| Control Tier | {spell['control_tier']} |
| Discipline | {spell['discipline']} |
| Output | {spell['output']} |
| Pattern | {pattern_display} |
| Reach | {reach_display} |
| Persistence | {persistence_display} |
| Target | {target_display} |
| Wattage | {spell['wattage']} W |

---

"""
    return md

def generate_common_grimoire_additions(count: int = 400) -> str:
    """Generate new Common Grimoire spells."""
    output = ""
    generated_names = set()
    
    for _ in range(count):
        attempts = 0
        while attempts < 10:
            name, spell = generate_common_spell()
            if name not in generated_names:
                generated_names.add(name)
                output += spell_to_markdown(name, spell)
                break
            attempts += 1
    
    return output

# Uncommon Grimoire spell generation
def generate_uncommon_spell() -> Tuple[str, dict]:
    """Generate a single Uncommon tier spell (T3-T4)."""
    shapes = ["Square", "Pentagon"]
    hooks = ["Emit", "Transform", "Sense", "Bind", "Filter", "Move", "Ward", "Counter"]
    modes = ["Create", "Affect", "Control"]
    disciplines = ["Light", "Heat", "Force", "Chemical", "Electric", "Binding", "Mind", "Raw"]
    patterns = ["Plane", "Beam", "Cone", "Ring", "Cylinder"]
    reaches = ["Touch", "Short (10 ft)", "Medium (50 ft)"]
    persistences = ["_(default — Immediate)_", "Timed (Short)", "Timed (Long)", "Sustained", "Conditional"]
    targets = ["_(default — Where Written)_", "Object", "Surface", "Individual"]
    
    shape = random.choice(shapes)
    hook = random.choice(hooks)
    mode = random.choice(modes)
    discipline = random.choice(disciplines)
    output = COMMON_OUTPUTS.get(discipline, discipline)
    pattern = random.choice(patterns)
    reach = random.choice(reaches)
    persistence = random.choice(persistences)
    target = random.choice(targets)
    
    wattage = calculate_wattage(shape, discipline, pattern, reach, persistence, target)
    control_tier = determine_control_tier(wattage)
    
    # Ensure Uncommon tier (T3-T4)
    if control_tier not in ["T3", "T4"]:
        return generate_uncommon_spell()
    
    name = generate_spell_name()
    
    spell = {
        "name": name,
        "shape": shape,
        "hook": hook,
        "mode": mode,
        "control_tier": control_tier,
        "discipline": discipline,
        "output": output,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target": target,
        "wattage": wattage
    }
    
    return name, spell

def generate_rare_spell() -> Tuple[str, dict]:
    """Generate a single Rare tier spell (T5-T6)."""
    shapes = ["Pentagon", "Circle"]
    hooks = ["Emit", "Transform", "Sense", "Bind", "Filter", "Move", "Ward", "Counter", "Control"]
    modes = ["Create", "Affect", "Control"]
    disciplines = ["Light", "Heat", "Force", "Chemical", "Electric", "Binding", "Mind", "Soul", "Raw"]
    patterns = ["Plane", "Beam", "Cone", "Ring", "Cylinder", "Sphere"]
    reaches = ["Short (10 ft)", "Medium (50 ft)", "Long (200 ft)"]
    persistences = ["Timed (Short)", "Timed (Long)", "Sustained", "Conditional", "Latched", "Permanent"]
    targets = ["Object", "Surface", "Individual", "Group", "Filter"]
    
    shape = random.choice(shapes)
    hook = random.choice(hooks)
    mode = random.choice(modes)
    discipline = random.choice(disciplines)
    output = COMMON_OUTPUTS.get(discipline, discipline)
    pattern = random.choice(patterns)
    reach = random.choice(reaches)
    persistence = random.choice(persistences)
    target = random.choice(targets)
    
    wattage = calculate_wattage(shape, discipline, pattern, reach, persistence, target)
    control_tier = determine_control_tier(wattage)
    
    # Ensure Rare tier (T5-T6)
    if control_tier not in ["T5", "T6"]:
        return generate_rare_spell()
    
    name = generate_spell_name()
    
    spell = {
        "name": name,
        "shape": shape,
        "hook": hook,
        "mode": mode,
        "control_tier": control_tier,
        "discipline": discipline,
        "output": output,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target": target,
        "wattage": wattage
    }
    
    return name, spell

def generate_legendary_spell() -> Tuple[str, dict]:
    """Generate a single Legendary tier spell (T7-T8)."""
    shapes = ["Circle"]
    hooks = ["Emit", "Transform", "Sense", "Bind", "Filter", "Move", "Ward", "Counter", "Control"]
    modes = ["Create", "Affect", "Control"]
    disciplines = ["Light", "Heat", "Force", "Chemical", "Electric", "Binding", "Mind", "Soul"]
    patterns = ["Cone", "Ring", "Cylinder", "Sphere", "Field"]
    reaches = ["Medium (50 ft)", "Long (200 ft)", "Line-of-Sight"]
    persistences = ["Timed (Long)", "Sustained", "Conditional", "Latched", "Permanent"]
    targets = ["Individual", "Group", "Filter", "Marked"]
    
    shape = random.choice(shapes)
    hook = random.choice(hooks)
    mode = random.choice(modes)
    discipline = random.choice(disciplines)
    output = COMMON_OUTPUTS.get(discipline, discipline)
    pattern = random.choice(patterns)
    reach = random.choice(reaches)
    persistence = random.choice(persistences)
    target = random.choice(targets)
    
    wattage = calculate_wattage(shape, discipline, pattern, reach, persistence, target)
    wattage = max(13001, wattage)  # Force Legendary tier
    control_tier = "T7"
    
    name = generate_spell_name()
    
    spell = {
        "name": name,
        "shape": shape,
        "hook": hook,
        "mode": mode,
        "control_tier": control_tier,
        "discipline": discipline,
        "output": output,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target": target,
        "wattage": wattage
    }
    
    return name, spell

def generate_mythic_spell() -> Tuple[str, dict]:
    """Generate a single Mythic tier spell (T9)."""
    shapes = ["Circle"]
    hooks = ["Emit", "Transform", "Sense", "Bind", "Filter", "Move", "Ward", "Counter", "Control"]
    modes = ["Create", "Affect", "Control"]
    disciplines = ["Mind", "Soul"]  # Higher disciplines
    patterns = ["Sphere", "Field"]
    reaches = ["Line-of-Sight", "Linked"]
    persistences = ["Sustained", "Conditional", "Latched", "Permanent"]
    targets = ["Individual", "Group", "Filter"]
    
    shape = random.choice(shapes)
    hook = random.choice(hooks)
    mode = random.choice(modes)
    discipline = random.choice(disciplines)
    output = COMMON_OUTPUTS.get(discipline, discipline)
    pattern = random.choice(patterns)
    reach = random.choice(reaches)
    persistence = random.choice(persistences)
    target = random.choice(targets)
    
    wattage = calculate_wattage(shape, discipline, pattern, reach, persistence, target)
    wattage = max(130001, wattage)  # Force Mythic tier
    control_tier = "T9"
    
    name = generate_spell_name()
    
    spell = {
        "name": name,
        "shape": shape,
        "hook": hook,
        "mode": mode,
        "control_tier": control_tier,
        "discipline": discipline,
        "output": output,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target": target,
        "wattage": wattage
    }
    
    return name, spell

def generate_pale_spell() -> Tuple[str, dict]:
    """Generate a single Pale tier spell (T9+, beyond normal Flux)."""
    shapes = ["Circle"]
    hooks = ["Emit", "Transform", "Sense", "Bind", "Filter", "Move", "Ward", "Counter", "Control"]
    modes = ["Create", "Affect", "Control"]
    disciplines = ["Soul"]  # Primarily Soul
    patterns = ["Sphere", "Field"]
    reaches = ["Line-of-Sight", "Linked"]
    persistences = ["Permanent", "Latched"]
    targets = ["Individual", "Group", "Filter"]
    
    shape = "Circle"
    hook = random.choice(hooks)
    mode = random.choice(modes)
    discipline = "Soul"
    output = "Soul"
    pattern = random.choice(patterns)
    reach = random.choice(reaches)
    persistence = random.choice(persistences)
    target = random.choice(targets)
    
    # Pale spells are extremely expensive
    wattage = random.randint(150000, 500000)
    control_tier = "T9"
    
    name = generate_spell_name()
    
    spell = {
        "name": name,
        "shape": shape,
        "hook": hook,
        "mode": mode,
        "control_tier": control_tier,
        "discipline": discipline,
        "output": output,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target": target,
        "wattage": wattage
    }
    
    return name, spell

if __name__ == "__main__":
    # Generate spells for all rarities maintaining the 100:50:25:13:6:3 ratio
    # Adding 400 Common means: 200 Uncommon, 100 Rare, 50 Legendary, 25 Mythic, 12 Pale
    
    print("Generating balanced spell tiers...")
    print("  400 Common spells...")
    print("  200 Uncommon spells...")
    print("  100 Rare spells...")
    print("  50 Legendary spells...")
    print("  25 Mythic spells...")
    print("  12 Pale spells...")
    
    # Common spells (already done, but include reference)
    print("\nGenerating Uncommon tier...")
    uncommon_spells = ""
    generated_names = set()
    for _ in range(200):
        attempts = 0
        while attempts < 10:
            name, spell = generate_uncommon_spell()
            if name not in generated_names:
                generated_names.add(name)
                uncommon_spells += spell_to_markdown(name, spell)
                break
            attempts += 1
    
    print("Generating Rare tier...")
    rare_spells = ""
    for _ in range(100):
        attempts = 0
        while attempts < 10:
            name, spell = generate_rare_spell()
            if name not in generated_names:
                generated_names.add(name)
                rare_spells += spell_to_markdown(name, spell)
                break
            attempts += 1
    
    print("Generating Legendary tier...")
    legendary_spells = ""
    for _ in range(50):
        attempts = 0
        while attempts < 10:
            name, spell = generate_legendary_spell()
            if name not in generated_names:
                generated_names.add(name)
                legendary_spells += spell_to_markdown(name, spell)
                break
            attempts += 1
    
    print("Generating Mythic tier...")
    mythic_spells = ""
    for _ in range(25):
        attempts = 0
        while attempts < 10:
            name, spell = generate_mythic_spell()
            if name not in generated_names:
                generated_names.add(name)
                mythic_spells += spell_to_markdown(name, spell)
                break
            attempts += 1
    
    print("Generating Pale tier...")
    pale_spells = ""
    for _ in range(12):
        attempts = 0
        while attempts < 10:
            name, spell = generate_pale_spell()
            if name not in generated_names:
                generated_names.add(name)
                pale_spells += spell_to_markdown(name, spell)
                break
            attempts += 1
    
    # Write all to individual files
    with open("C:\\Users\\Contrite42\\quartz\\new_uncommon_spells.md", "w") as f:
        f.write(uncommon_spells)
    print("\nWrote 200 Uncommon spells to new_uncommon_spells.md")
    
    with open("C:\\Users\\Contrite42\\quartz\\new_rare_spells.md", "w") as f:
        f.write(rare_spells)
    print("Wrote 100 Rare spells to new_rare_spells.md")
    
    with open("C:\\Users\\Contrite42\\quartz\\new_legendary_spells.md", "w") as f:
        f.write(legendary_spells)
    print("Wrote 50 Legendary spells to new_legendary_spells.md")
    
    with open("C:\\Users\\Contrite42\\quartz\\new_mythic_spells.md", "w") as f:
        f.write(mythic_spells)
    print("Wrote 25 Mythic spells to new_mythic_spells.md")
    
    with open("C:\\Users\\Contrite42\\quartz\\new_pale_spells.md", "w") as f:
        f.write(pale_spells)
    print("Wrote 12 Pale spells to new_pale_spells.md")
    
    print("\nAll spell generation complete!")
