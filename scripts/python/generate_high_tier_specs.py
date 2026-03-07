#!/usr/bin/env python3
"""
Generate JSON specs for high-tier spells (T7-T9) to complete the quota.
These tiers require specific combinations (Mind/Soul + Pentagon/Circle).
"""

import json
import random
from pathlib import Path

# High-tier capable combinations
LEGENDARY_MYTHIC_DISCIPLINES = ["Mind", "Soul"]
HIGH_SHAPES = ["Pentagon", "Circle"]
HOOKS = ["Emit", "Shape", "Bind", "Ward", "Trigger", "Transform", "Move", "Sense", "Filter", "Amplify", "Dampen", "Counter"]
MODES = ["Create", "Affect", "Control"]
PATTERNS = ["Point", "Plane", "Beam", "Cone", "Ring", "Cylinder", "Sphere", "Field"]
REACHES = ["Self", "Touch", "Short", "Medium", "Long", "Line-of-Sight"]
PERSISTENCES = ["Immediate", "Timed Short", "Timed Long", "Sustained", "Conditional", "Latched", "Permanent"]
TARGETS = ["Where Written", "Self", "Object", "Surface", "Individual", "Marked", "Group", "Filter"]

def generate_name(discipline, hook, pattern):
    """Generate a spell name"""
    return f"{discipline} {hook} {pattern}"

def generate_summary(discipline, hook, mode, pattern):
    """Generate a spell summary"""
    verbs = {
        "Emit": "releases", "Shape": "refines", "Bind": "anchors", "Ward": "establishes",
        "Trigger": "arms", "Transform": "reconfigures", "Move": "repositions", "Sense": "detects",
        "Filter": "screens", "Amplify": "boosts", "Dampen": "reduces", "Counter": "disrupts"
    }
    mode_phrases = {
        "Create": "by creating a fresh flux expression",
        "Affect": "by changing existing conditions",
        "Control": "with active regulation while it runs"
    }
    pattern_terms = {
        "Point": "point focus", "Plane": "planar spread", "Beam": "directed line",
        "Cone": "fan spread", "Ring": "ring perimeter", "Cylinder": "column volume",
        "Sphere": "spherical envelope", "Field": "field volume"
    }
    
    return f"{verbs[hook]} {discipline.lower()} energy in a {pattern_terms[pattern]} {mode_phrases[mode]}"

def generate_effect(discipline, hook, mode, pattern, reach, persistence):
    """Generate effect description"""
    return (f"The caster inscribes a sigil that {generate_summary(discipline, hook, mode, pattern).lower()}. "
            f"Effect range: {reach.lower()}. Persistence: {persistence.lower()}.")

def create_legendary_spec():
    """Create a spec targeting T7-T8 (13001-40000W)"""
    # Use Pentagon or Circle with Mind/Soul + expensive addons
    discipline = random.choice(LEGENDARY_MYTHIC_DISCIPLINES)
    shape = random.choice(HIGH_SHAPES)
    hook = random.choice(HOOKS)
    mode = random.choice(MODES)
    pattern = random.choice(["Ring", "Cylinder", "Sphere", "Field"])  # Higher cost patterns
    reach = random.choice(["Medium", "Long", "Line-of-Sight"])  # Higher cost reaches
    persistence = random.choice(["Timed Long", "Conditional", "Latched", "Permanent"])
    target = random.choice(["Individual", "Marked", "Group", "Filter"])
    
    name = generate_name(discipline, hook, pattern)
    
    return {
        "name": name,
        "summary": generate_summary(discipline, hook, mode, pattern),
        "effect_description": generate_effect(discipline, hook, mode, pattern, reach, persistence),
        "hook": hook,
        "mode": mode,
        "shape": shape,
        "discipline": discipline,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target_spec": target,
        "notes": "Auto-generated high-tier spell"
    }

def create_mythic_spec():
    """Create a spec targeting T9 (130001W+)"""
    # Circle + Soul + maximum complexity
    discipline = "Soul"
    shape = "Circle"
    hook = random.choice(["Amplify", "Counter", "Transform", "Ward"])  # High complexity hooks
    mode = random.choice(["Control", "Affect"])  # High complexity modes
    pattern = random.choice(["Sphere", "Field"])
    reach = random.choice(["Long", "Line-of-Sight"])
    persistence = random.choice(["Permanent", "Latched"])
    target = random.choice(["Group", "Filter"])
    
    name = generate_name(discipline, hook, pattern)
    
    return {
        "name": name,
        "summary": generate_summary(discipline, hook, mode, pattern),
        "effect_description": generate_effect(discipline, hook, mode, pattern, reach, persistence),
        "hook": hook,
        "mode": mode,
        "shape": shape,
        "discipline": discipline,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target_spec": target,
        "sustained_minutes": 60 if persistence == "Sustained" else 0,
        "notes": "Auto-generated T9 spell"
    }

def create_pale_spec():
    """Create a spec for Pale grimoire (reality-bending T9)"""
    # Similar to Mythic but with thematic weight
    discipline = random.choice(["Soul", "Mind", "Raw"])
    shape = "Circle"
    hook = random.choice(["Transform", "Counter", "Emit", "Ward"])
    mode = random.choice(["Affect", "Control"])
    pattern = random.choice(["Field", "Sphere", "Cylinder"])
    reach = random.choice(["Long", "Line-of-Sight"])
    persistence = "Permanent"
    target = random.choice(["Surface", "Group", "Filter"])
    
    prefixes = ["Void", "Rift", "Echo", "Pale", "Null", "Flux", "Reality", "World", "Soul", "Mind"]
    suffixes = ["collapse", "tear", "scar", "breach", "mark", "wound", "pulse", "storm", "shatter", "rend"]
    name = f"{random.choice(prefixes)}{random.choice(suffixes).capitalize()}"
    
    return {
        "name": name,
        "summary": f"A reality-altering effect that {generate_summary(discipline, hook, mode, pattern).lower()}",
        "effect_description": (
            f"Invokes a fundamental disruption to local Flux architecture. "
            f"{generate_effect(discipline, hook, mode, pattern, reach, persistence)} "
            f"Side effects on caster and casting site are documented but not fully understood."
        ),
        "hook": hook,
        "mode": mode,
        "shape": shape,
        "discipline": discipline,
        "pattern": pattern,
        "reach": reach,
        "persistence": persistence,
        "target_spec": target,
        "notes": "Pale-class spell - use with extreme caution"
    }

def main():
    queue_dir = Path("quartz/spell_queue")
    queue_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate 17 Legendary specs
    print("Generating 17 Legendary spell specs...")
    for i in range(17):
        spec = create_legendary_spec()
        output_path = queue_dir / f"legendary_{i+1:02d}.json"
        output_path.write_text(json.dumps(spec, indent=2))
        print(f"  Created: {output_path.name} - {spec['name']}")
    
    # Generate 20 Mythic specs
    print("\nGenerating 20 Mythic spell specs...")
    for i in range(20):
        spec = create_mythic_spec()
        output_path = queue_dir / f"mythic_{i+1:02d}.json"
        output_path.write_text(json.dumps(spec, indent=2))
        print(f"  Created: {output_path.name} - {spec['name']}")
    
    # Generate 20 Pale specs
    print("\nGenerating 20 Pale spell specs...")
    for i in range(20):
        spec = create_pale_spec()
        output_path = queue_dir / f"pale_{i+1:02d}.json"
        output_path.write_text(json.dumps(spec, indent=2))
        print(f"  Created: {output_path.name} - {spec['name']}")
    
    print(f"\n✓ Generated 57 high-tier spell specs in {queue_dir}")
    print("Run sigil_maker.py auto to process them")

if __name__ == "__main__":
    main()
