#!/usr/bin/env python3
"""
Fix script to correct Control Tier values in all grimoire files based on recalculated wattage.
"""

import re
import sys
from pathlib import Path
from typing import Optional

# Import calculation logic from sigil_maker
sys.path.insert(0, str(Path(__file__).parent / "quartz"))
from sigil_maker import (
    SHAPES, DISCIPLINE_MULTIPLIERS, PATTERN_COSTS, REACH_COSTS,
    PERSISTENCE_COSTS, TARGET_COSTS, DEFAULTS, canonicalize,
    HOOKS, MODES, OUTPUT_MODES, tier_for_cost,
    default_hook_mode_multiplier, PERSISTENCE_ALIASES, REACH_ALIASES,
    NATURAL_OUTPUT_BY_DISCIPLINE, ADJACENT_OUTPUT_BY_DISCIPLINE, PHYSICAL_OUTPUTS
)

def output_mode_premium(discipline: str, output_mode: str) -> int:
    """Calculate output mode premium (from sigil_maker logic)."""
    natural = NATURAL_OUTPUT_BY_DISCIPLINE[discipline]
    if output_mode == natural:
        return 0

    if output_mode in ADJACENT_OUTPUT_BY_DISCIPLINE.get(discipline, set()):
        return 10

    discipline_is_extreme = discipline in {"Mind", "Soul"}
    output_is_extreme = output_mode in {"Neuro", "Soul"}

    if discipline_is_extreme and output_mode in PHYSICAL_OUTPUTS:
        return 60
    if output_is_extreme and discipline not in {"Mind", "Soul"}:
        return 60

    return 30


def clean_value(value: str) -> str:
    """Clean up value from grimoire format."""
    # Strip default format wrapping (handle various encoding issues)
    value = re.sub(r'_\(default — (.+?)\)_', r'\1', value)
    value = re.sub(r'_\(default - (.+?)\)_', r'\1', value)
    value = re.sub(r'_\(default � (.+?)\)_', r'\1', value)  # Handle encoding issues
    value = re.sub(r'_\(default . (.+?)\)_', r'\1', value)  # Handle any separator
    # Handle "Timed (Short)" or "Timed (Long)" format
    value = re.sub(r'Timed\s*\(Short\)', 'Timed Short', value)
    value = re.sub(r'Timed\s*\(Long\)', 'Timed Long', value)
    # If just "Timed" appears, leave it for later handling
    return value.strip()


def parse_grimoire_for_fix(filepath: Path) -> list[dict]:
    """Parse grimoire and extract spell blocks with line numbers for fixing."""
    content = filepath.read_text(encoding='utf-8', errors='replace')
    lines = content.split('\n')
    
    spells = []
    current_spell = None
    spell_start_line = 0
    in_table = False
    
    for i, line in enumerate(lines):
        # Detect spell name
        if re.match(r'^\*\*[^*]+\*\*$', line.strip()):
            if current_spell:
                spells.append(current_spell)
            current_spell = {
                'name': line.strip().strip('*'),
                'start_line': i,
                'variables': {},
                'lines': [line]
            }
            in_table = False
        elif current_spell:
            current_spell['lines'].append(line)
            
            # Check for separator (end of spell)
            if line.strip() == '---':
                current_spell['end_line'] = i
                spells.append(current_spell)
                current_spell = None
                in_table = False
            # Parse table rows
            elif '|' in line and line.strip().startswith('|'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 3 and parts[1] and parts[2]:
                    if parts[1] == 'Variable':
                        in_table = True
                    elif in_table and parts[1] != '---':
                        current_spell['variables'][parts[1]] = clean_value(parts[2])
    
    # Handle last spell if no final separator
    if current_spell:
        current_spell['end_line'] = len(lines) - 1
        spells.append(current_spell)
    
    return spells


def calculate_correct_tier(variables: dict) -> tuple[Optional[str], Optional[int], Optional[str]]:
    """Calculate correct tier from spell variables. Returns (tier, wattage, error)."""
    try:
        # Canonicalize variables with better error handling
        shape = canonicalize(variables.get('Shape', 'Triangle'), set(SHAPES))
        discipline = canonicalize(variables.get('Discipline', 'Raw'), set(DISCIPLINE_MULTIPLIERS))
        hook = canonicalize(variables.get('Hook', 'Emit'), HOOKS)
        mode = canonicalize(variables.get('Mode', 'Create'), MODES)
        output_mode = canonicalize(variables.get('Output', DEFAULTS['output_mode']), OUTPUT_MODES)
        pattern = canonicalize(variables.get('Pattern', DEFAULTS['pattern']), set(PATTERN_COSTS))
        
        # Handle reach - skip if placeholder
        reach_val = variables.get('Reach', DEFAULTS['reach'])
        if reach_val == '__':
            reach_val = DEFAULTS['reach']
        reach = canonicalize(reach_val, set(REACH_COSTS), REACH_ALIASES)
        
        # Handle persistence
        persist_val = variables.get('Persistence', DEFAULTS['persistence'])
        if persist_val in ('__', ''):
            persist_val = DEFAULTS['persistence']
        # Clean up malformed values (in case clean_value didn't catch everything)
        persist_val = re.sub(r'\s+', ' ', persist_val)  # Collapse multiple spaces
        # Map variations to canonical names
        if 'Short' in persist_val and 'Long' not in persist_val:
            persist_val = 'Timed Short'
        elif 'Long' in persist_val:
            persist_val = 'Timed Long'
        elif persist_val == 'Timed':
            persist_val = 'Timed Short'  # Default to Short if just "Timed"
        persistence = canonicalize(persist_val, set(PERSISTENCE_COSTS), PERSISTENCE_ALIASES)
        
        target_spec = canonicalize(variables.get('Target', DEFAULTS['target_spec']), set(TARGET_COSTS))
        
        # Calculate wattage
        shape_base = SHAPES[shape]["base_w"]
        multiplier = DISCIPLINE_MULTIPLIERS[discipline]
        core = shape_base * multiplier
        
        pattern_w = PATTERN_COSTS[pattern]
        reach_w = REACH_COSTS[reach]
        target_w = TARGET_COSTS[target_spec]
        
        # Persistence cost
        if persistence == "Sustained":
            persistence_w = 10  # Assume 10 min default
        else:
            persistence_w = int(PERSISTENCE_COSTS[persistence] or 0)
        
        output_w = output_mode_premium(discipline, output_mode)
        
        subtotal = core + pattern_w + reach_w + persistence_w + target_w + output_w
        
        # Apply hook/mode multiplier
        hook_mode_mult = default_hook_mode_multiplier(hook, mode)
        total_w = int(round(subtotal * hook_mode_mult))
        
        tier = tier_for_cost(total_w)
        
        return tier, total_w, None
        
    except Exception as e:
        return None, None, str(e)


def fix_grimoire(filepath: Path, dry_run: bool = True) -> dict:
    """Fix Control Tier values in grimoire file."""
    spells = parse_grimoire_for_fix(filepath)
    
    fixes = []
    errors = []
    
    for spell in spells:
        if 'Control Tier' not in spell['variables']:
            continue
        
        stated_tier = spell['variables']['Control Tier']
        correct_tier, wattage, error = calculate_correct_tier(spell['variables'])
        
        if error:
            errors.append({
                'name': spell['name'],
                'error': error
            })
            continue
        
        if correct_tier != stated_tier:
            fixes.append({
                'name': spell['name'],
                'old_tier': stated_tier,
                'new_tier': correct_tier,
                'wattage': wattage,
                'spell': spell
            })
    
    # Apply fixes if not dry run
    if not dry_run and fixes:
        content = filepath.read_text(encoding='utf-8', errors='replace')
        
        for fix in fixes:
            spell = fix['spell']
            old_block = '\n'.join(spell['lines'])
            
            # Replace Control Tier value in the block
            new_block = old_block
            for i, line in enumerate(spell['lines']):
                if '| Control Tier |' in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        parts[2] = f" {fix['new_tier']} "
                        spell['lines'][i] = '|'.join(parts)
                        new_block = '\n'.join(spell['lines'])
                        break
            
            # Replace in content
            content = content.replace(old_block, new_block, 1)
        
        # Write back
        filepath.write_text(content, encoding='utf-8')
    
    return {
        'fixes': fixes,
        'errors': errors,
        'total_spells': len(spells)
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fix Control Tier values in grimoires')
    parser.add_argument('--apply', action='store_true', help='Apply fixes (default is dry-run)')
    args = parser.parse_args()
    
    content_dir = Path(__file__).parent / "content"
    
    grimoires = [
        "Common Grimoire.md",
        "Uncommon Grimoire.md",
        "Rare Grimoire.md",
        "Legendary Grimoire.md",
        "Mythic Grimoire.md",
        "Pale Grimoire.md"
    ]
    
    total_fixes = 0
    total_errors = 0
    
    for grimoire_name in grimoires:
        grimoire_path = content_dir / grimoire_name
        if not grimoire_path.exists():
            print(f"MISSING: {grimoire_name}")
            continue
        
        result = fix_grimoire(grimoire_path, dry_run=not args.apply)
        
        print(f"\n{'='*60}")
        print(f"{grimoire_name}: {result['total_spells']} spells")
        print(f"{'='*60}")
        
        if result['fixes']:
            print(f"\n{'FIXES APPLIED' if args.apply else 'FIXES NEEDED'} ({len(result['fixes'])} spells):")
            for fix in result['fixes']:
                print(f"  {fix['name']}: {fix['old_tier']} -> {fix['new_tier']} ({fix['wattage']}W)")
            total_fixes += len(result['fixes'])
        else:
            print("No fixes needed")
        
        if result['errors']:
            print(f"\nERRORS ({len(result['errors'])} spells):")
            for err in result['errors']:
                print(f"  {err['name']}: {err['error']}")
            total_errors += len(result['errors'])
    
    print(f"\n{'='*60}")
    print(f"SUMMARY: {total_fixes} {'FIXED' if args.apply else 'TO FIX'}, {total_errors} errors")
    print(f"{'='*60}")
    
    if not args.apply and total_fixes > 0:
        print("\nRun with --apply to apply these fixes")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
