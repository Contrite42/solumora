#!/usr/bin/env python3
"""
Audit script to verify all grimoire spells have correct Control Tier based on their variables.
"""

import re
import sys
from pathlib import Path

# Import calculation logic from sigil_maker
sys.path.insert(0, str(Path(__file__).parent / "quartz"))
from sigil_maker import (
    SHAPES, DISCIPLINE_MULTIPLIERS, PATTERN_COSTS, REACH_COSTS,
    PERSISTENCE_COSTS, TARGET_COSTS, DEFAULTS, canonicalize,
    HOOKS, MODES, OUTPUT_MODES, tier_for_cost,
    default_hook_mode_multiplier, PERSISTENCE_ALIASES, REACH_ALIASES
)

def parse_grimoire_spell(spell_block: str) -> dict:
    """Extract spell variables from markdown block."""
    lines = spell_block.strip().split('\n')
    name_match = re.match(r'\*\*(.+)\*\*', lines[0])
    if not name_match:
        return None
    
    name = name_match.group(1)
    description = lines[1] if len(lines) > 1 else ""
    
    variables = {}
    for line in lines:
        if '|' in line and line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3 and parts[1] and parts[2]:
                key = parts[1]
                value = parts[2]
                # Clean up default format
                value = re.sub(r'_\(default — (.+?)\)_', r'\1', value)
                value = re.sub(r'_\(default - (.+?)\)_', r'\1', value)
                value = re.sub(r'\(.*?\)', '', value).strip()  # Remove parentheticals
                variables[key] = value
    
    return {
        'name': name,
        'description': description,
        'variables': variables
    }

def calculate_spell_wattage(spell_data: dict) -> tuple:
    """Calculate wattage and tier for a spell from its variables."""
    vars = spell_data['variables']
    
    try:
        # Extract and canonicalize variables
        shape = canonicalize(vars.get('Shape', 'Triangle'), set(SHAPES))
        discipline = canonicalize(vars.get('Discipline', 'Raw'), set(DISCIPLINE_MULTIPLIERS))
        hook = canonicalize(vars.get('Hook', 'Emit'), HOOKS)
        mode = canonicalize(vars.get('Mode', 'Create'), MODES)
        output_mode = canonicalize(vars.get('Output', DEFAULTS['output_mode']), OUTPUT_MODES)
        pattern = canonicalize(vars.get('Pattern', DEFAULTS['pattern']), set(PATTERN_COSTS))
        reach = canonicalize(vars.get('Reach', DEFAULTS['reach']), set(REACH_COSTS), REACH_ALIASES)
        persistence = canonicalize(vars.get('Persistence', DEFAULTS['persistence']), 
                                   set(PERSISTENCE_COSTS), PERSISTENCE_ALIASES)
        target_spec = canonicalize(vars.get('Target', DEFAULTS['target_spec']), set(TARGET_COSTS))
        
        # Calculate base cost
        shape_base = SHAPES[shape]["base_w"]
        multiplier = DISCIPLINE_MULTIPLIERS[discipline]
        core = shape_base * multiplier
        
        # Add outer costs
        pattern_w = PATTERN_COSTS[pattern]
        reach_w = REACH_COSTS[reach]
        target_w = TARGET_COSTS[target_spec]
        
        # Persistence cost
        if persistence == "Sustained":
            # Assume 10 minutes for sustained spells if not specified
            persistence_w = 10
        else:
            persistence_w = int(PERSISTENCE_COSTS[persistence] or 0)
        
        # Output mode premium (simplified - using basic logic)
        output_w = 0  # Would need full logic from sigil_maker
        
        subtotal = core + pattern_w + reach_w + persistence_w + target_w + output_w
        
        # Apply hook/mode multiplier
        hook_mode_mult = default_hook_mode_multiplier(hook, mode)
        total_w = int(round(subtotal * hook_mode_mult))
        
        tier = tier_for_cost(total_w)
        
        return total_w, tier, None
        
    except Exception as e:
        return None, None, str(e)

def audit_grimoire(filepath: Path) -> list:
    """Audit all spells in a grimoire file."""
    content = filepath.read_text(encoding='utf-8', errors='replace')
    
    # Split into spell blocks
    spell_blocks = re.split(r'\n---\n', content)
    
    issues = []
    spell_count = 0
    
    for block in spell_blocks:
        if '| Variable | Value |' not in block:
            continue
            
        spell = parse_grimoire_spell(block)
        if not spell:
            continue
        
        spell_count += 1
        stated_tier = spell['variables'].get('Control Tier', 'Unknown')
        
        calc_watts, calc_tier, error = calculate_spell_wattage(spell)
        
        if error:
            issues.append({
                'name': spell['name'],
                'issue': f"Calculation error: {error}",
                'stated': stated_tier
            })
        elif calc_tier != stated_tier:
            issues.append({
                'name': spell['name'],
                'issue': f"Tier mismatch: stated {stated_tier}, calculated {calc_tier} ({calc_watts}W)",
                'stated': stated_tier,
                'calculated': calc_tier,
                'watts': calc_watts
            })
    
    return issues, spell_count

def main():
    content_dir = Path(__file__).parent / "content"
    
    grimoires = [
        "Common Grimoire.md",
        "Uncommon Grimoire.md",
        "Rare Grimoire.md",
        "Legendary Grimoire.md",
        "Mythic Grimoire.md",
        "Pale Grimoire.md"
    ]
    
    total_issues = 0
    total_spells = 0
    
    for grimoire_name in grimoires:
        grimoire_path = content_dir / grimoire_name
        if not grimoire_path.exists():
            print(f"❌ {grimoire_name} not found")
            continue
        
        issues, spell_count = audit_grimoire(grimoire_path)
        total_spells += spell_count
        total_issues += len(issues)
        
        print(f"\n{'='*60}")
        print(f"{grimoire_name}: {spell_count} spells")
        print(f"{'='*60}")
        
        if issues:
            for issue in issues:
                print(f"⚠️  {issue['name']}")
                print(f"    {issue['issue']}")
        else:
            print("✅ All spells have correct Control Tier values")
    
    print(f"\n{'='*60}")
    print(f"SUMMARY: {total_spells} spells audited, {total_issues} issues found")
    print(f"{'='*60}")
    
    return 0 if total_issues == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
