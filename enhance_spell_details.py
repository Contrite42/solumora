import re
import os

grimoire_files = [
    ('Common Grimoire.md', 400),
    ('Uncommon Grimoire.md', 200),
    ('Rare Grimoire.md', 100),
    ('Legendary Grimoire.md', 50),
    ('Mythic Grimoire.md', 25),
    ('Pale Grimoire.md', 12)
]

base_path = r'C:\Users\Contrite42\quartz\content'

def get_concrete_effects(hook, discipline, output, pattern, target):
    """Generate specific examples of what the spell does"""
    
    # Protection/Barrier effects
    if output in ['Protection', 'Shielding', 'Defense']:
        if discipline in ['Force', 'Kinetic']:
            return 'blocks physical impacts—strikes, thrown objects, rushing bodies'
        elif discipline == 'Fire':
            return 'deflects flames and heat'
        elif discipline == 'Cold':
            return 'repels freezing attacks and ice'
        elif discipline == 'Lightning':
            return 'grounds electrical strikes'
        elif discipline == 'Acid':
            return 'neutralizes corrosive substances'
        elif discipline in ['Soul', 'Mind']:
            return 'shields against psychic intrusion and soul-binding'
        return 'forms a protective barrier'
    
    # Damage effects
    elif output in ['Damage', 'Destruction', 'Kinetic', 'Force']:
        if pattern == 'Beam':
            if discipline in ['Force', 'Kinetic']:
                return 'punches through obstacles with concentrated kinetic force'
            elif discipline == 'Fire':
                return 'burns through targets with focused heat'
            elif discipline == 'Lightning':
                return 'electrocutes with a lightning strike'
            return 'delivers focused destructive energy'
        elif pattern == 'Cone':
            if discipline in ['Force', 'Kinetic']:
                return 'sends enemies and objects flying backward'
            elif discipline == 'Fire':
                return 'engulfs everything in the path with flames'
            return 'scatters destructive force in a widening arc'
        elif pattern == 'Sphere':
            return 'blasts everything in the radius away from the center'
        return 'delivers destructive impact'
    
    # Constraint/Binding effects
    elif output in ['Constraint', 'Binding', 'Immobilization']:
        if discipline in ['Force', 'Kinetic']:
            return 'locks targets in place, preventing movement or escape'
        elif discipline == 'Binding':
            return 'pins limbs and restricts physical action'
        elif discipline in ['Soul', 'Mind']:
            return 'paralyzes voluntary movement through psychic pressure'
        return 'immobilizes and restrains the target'
    
    # Movement effects
    elif output in ['Movement', 'Displacement']:
        if hook == 'Emit':
            return 'shoves targets forcefully in the desired direction'
        elif hook == 'Bind':
            return 'drags or pulls targets to the marked location' 
        return 'forces targets into motion'
    
    # Detection/Sensing
    elif output in ['Detection', 'Awareness', 'Information']:
        if discipline == 'Mind':
            return 'reveals surface thoughts and immediate intentions'
        elif discipline == 'Soul':
            return 'exposes soul-signatures and binding marks'
        elif discipline == 'Space':
            return 'maps spatial layout and hidden passages'
        return 'detects hidden information or presences'
    
    # Healing/Restoration
    elif output in ['Healing', 'Restoration', 'Vitality']:
        return 'mends wounds, knits tissue, and restores physical integrity'
    
    # Transformation
    elif output in ['Transformation', 'Alteration']:
        if target in ['Object', 'Material']:
            return 'alters physical properties—hardness, temperature, state of matter'
        return 'reshapes form and substance'
    
    # Illusion
    elif output in ['Illusion', 'Deception']:
        return 'creates false sensory impressions—phantom sounds, false images, illusory textures'
    
    # Generic fallbacks based on hook
    if hook == 'Emit' and discipline in ['Force', 'Kinetic']:
        return 'projects kinetic force outward'
    elif hook == 'Bind':
        return 'anchors targets in a fixed state'
    elif hook == 'Sense':
        return 'gathers environmental information'
    elif hook == 'Transform':
        return 'alters the target\'s properties'
    
    return 'produces its effect'

def get_practical_application(hook, output, wattage, persistence, reach):
    """Add practical use cases and benefits"""
    
    apps = []
    
    # Applications based on output
    if output in ['Protection', 'Shielding', 'Defense']:
        apps.append('Useful for defending doorways, covering retreat, or protecting vulnerable positions')
    elif output in ['Constraint', 'Binding']:
        apps.append('Ideal for subduing opponents or securing prisoners without injury')
    elif output in ['Damage', 'Destruction', 'Kinetic']:
        if 'Long' in reach or 'Extreme' in reach:
            apps.append('Effective for ranged combat or eliminating distant threats')
        else:
            apps.append('Suitable for close-quarters combat or breaching barriers')
    elif output in ['Detection', 'Awareness']:
        apps.append('Practical for reconnaissance, searching rooms, or identifying threats')
    elif output in ['Movement', 'Displacement']:
        apps.append('Useful for creating distance, forced repositioning, or knocking enemies prone')
    elif output in ['Healing', 'Restoration']:
        apps.append('Essential for field medicine and stabilizing injuries')
    
    # Benefits based on cost and persistence
    if wattage < 50:
        apps.append('The minimal flux cost makes it practical for extended or repeated use')
    elif wattage < 200:
        apps.append('Affordable enough for routine use without draining reserves')
    
    if persistence == 'Sustained' and wattage < 100:
        apps.append('Can be maintained for extended periods at low flux drain')
    elif 'Timed' in persistence and 'Long' in persistence:
        apps.append('Runs without further attention, freeing concentration for other tasks')
    
    # Return the most relevant application
    return apps[0] if apps else None

def refine_description_advanced(name, old_desc, recipe):
    hook = recipe.get('Hook', '')
    discipline = recipe.get('Discipline', '')
    output = recipe.get('Output', '')
    pattern = recipe.get('Pattern', '')
    reach = recipe.get('Reach', '')
    persistence = recipe.get('Persistence', '')
    target = recipe.get('Target', '')
    wattage = recipe.get('Wattage', 100)
    control_tier = recipe.get('Control Tier', '')
    
    # Action verb based on hook
    action_map = {
        'Emit': 'Projects',
        'Bind': 'Anchors',
        'Sense': 'Detects',
        'Transform': 'Reshapes',
        'Invoke': 'Summons',
        'Counter': 'Disrupts',
        'Amplify': 'Enhances',
        'Redirect': 'Deflects',
        'Filter': 'Screens',
        'Absorb': 'Draws in',
        'Reflect': 'Bounces back'
    }
    action = action_map.get(hook, 'Channels')
    
    # Energy/effect type
    energy_map = {
        'Force': 'kinetic force',
        'Kinetic': 'kinetic energy',
        'Fire': 'flames',
        'Cold': 'freezing energy',
        'Lightning': 'electrical discharge',
        'Acid': 'corrosive flux',
        'Shadow': 'shadow-flux',
        'Light': 'radiant energy',
        'Soul': 'soul-bound flux',
        'Mind': 'psychic force',
        'Gravity': 'gravitational force',
        'Time': 'temporal flux',
        'Space': 'spatial distortion',
        'Binding': 'binding tension',
        'Raw': 'raw flux',
        'Photonic': 'light energy',
        'Thermal': 'heat energy'
    }
    energy = energy_map.get(discipline, 'flux')
    
    # Pattern shape
    pattern_map = {
        'Beam': 'as a focused beam',
        'Cone': 'as a widening cone',
        'Sphere': 'in a spherical burst',
        'Wall': 'as a barrier wall',
        'Line': 'in a straight line',
        'Chain': 'that chains between targets',
        'Ray': 'as a precise ray',
        'Aura': 'as a surrounding aura',
        'Touch': 'through direct contact',
        'Area': 'across an area',
        'Plane': 'across a flat plane',
        'Field': 'as a contained field',
        'Ring': 'in a circular perimeter'
    }
    shape_phrase = pattern_map.get(pattern, '')
    
    # Reach distance
    if 'Touch' in reach:
        reach_phrase = 'at point of contact'
    elif 'Short' in reach:
        reach_phrase = 'within 10 feet'
    elif 'Medium' in reach:
        reach_phrase = 'within 50 feet'
    elif 'Long (250 ft)' in reach:
        reach_phrase = 'at up to 250 feet'
    elif 'Long (200 ft)' in reach:
        reach_phrase = 'at up to 200 feet'
    elif 'Long (100 ft)' in reach:
        reach_phrase = 'at up to 100 feet'
    elif 'Long' in reach:
        reach_phrase = 'at extended range'
    elif 'Extreme' in reach:
        reach_phrase = 'at extreme distances'
    elif 'Line-of-Sight' in reach:
        reach_phrase = 'anywhere within line of sight'
    else:
        reach_phrase = ''
    
    # Target type
    if target == 'Object':
        target_phrase = 'targeting objects'
    elif target == 'Surface':
        target_phrase = 'across surfaces'
    elif target == 'Creature':
        target_phrase = 'against living targets'
    elif target == 'Area':
        target_phrase = 'affecting the entire area'
    elif target == 'Where Written':
        target_phrase = 'at the marked location'
    elif target == 'Individual':
        target_phrase = 'on a single person'
    elif target == 'Group':
        target_phrase = 'affecting multiple targets'
    elif target == 'Marked':
        target_phrase = 'at the designated point'
    else:
        target_phrase = ''
    
    # Build the core sentence
    parts = [action, energy]
    if shape_phrase:
        parts.append(shape_phrase)
    if reach_phrase:
        parts.append(reach_phrase)
    if target_phrase:
        parts.append(target_phrase)
    
    core = ' '.join(parts)
    
    # Add concrete effect description
    concrete = get_concrete_effects(hook, discipline, output, pattern, target)
    if concrete and concrete != 'produces its effect':
        core += f', {concrete}'
    else:
        core += f', delivering its effect'
    
    # Persistence
    if persistence == 'Sustained':
        core += '. Must be actively sustained'
        if wattage < 100:
            core += ', but the flux drain is minimal, making it practical for extended use'
    elif 'Timed (Short)' in persistence:
        core += '. Runs for roughly a minute before dissipating'
    elif 'Timed (Long)' in persistence:
        core += '. Persists for several minutes without further attention'
    elif 'Timed' in persistence:
        core += '. Holds for its duration then fades'
    elif persistence == 'Instantaneous' or persistence == 'Immediate':
        core += ' in a single instant'
    elif persistence == 'Permanent':
        core += '. The effect becomes permanent once established'
    elif persistence == 'Conditional':
        core += '. Persists until the specified condition triggers'
    
    # Add practical application
    practical = get_practical_application(hook, output, wattage, persistence, reach)
    if practical:
        core += f'. {practical}'
    
    return core + '.'

def process_grimoire(filepath, expected_count):
    print(f"\nProcessing {os.path.basename(filepath)}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into intro and spells
    spell_blocks = content.split('\n---\n')
    intro = spell_blocks[0]
    spells = spell_blocks[1:] if len(spell_blocks) > 1 else []
    
    refined_spells = []
    count = 0
    
    for spell_block in spells:
        lines = spell_block.strip().split('\n')
        if not lines or not lines[0].startswith('**'):
            refined_spells.append(spell_block)
            continue
        
        # Extract spell name
        name_match = re.match(r'\*\*(.+?)\*\*', lines[0])
        if not name_match:
            refined_spells.append(spell_block)
            continue
        
        name = name_match.group(1)
        
        # Find wattage and recipe start
        wattage_line = ''
        recipe_start = -1
        
        for i, line in enumerate(lines[1:], 1):
            if line.startswith('| Wattage |'):
                wattage_line = line
                recipe_start = i + 1
                break
        
        if not wattage_line or recipe_start == -1:
            refined_spells.append(spell_block)
            continue
        
        # Parse recipe
        recipe = {}
        wattage_match = re.search(r'(\d+)\s*W', wattage_line)
        recipe['Wattage'] = int(wattage_match.group(1)) if wattage_match else 100
        
        for i in range(recipe_start, len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            if not line.startswith('|'):
                break
            
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                key = parts[0]
                value = parts[1]
                recipe[key] = value
        
        # Generate refined description
        new_desc = refine_description_advanced(name, '', recipe)
        
        # Rebuild spell block
        new_block = f"**{name}**\n{new_desc}\n{wattage_line}"
        
        # Add recipe lines
        for i in range(recipe_start, len(lines)):
            if lines[i].strip().startswith('|') and '|' in lines[i]:
                new_block += '\n' + lines[i]
            elif not lines[i].strip():
                continue
            else:
                break
        
        refined_spells.append(new_block)
        count += 1
    
    # Reassemble file
    new_content = intro + '\n\n---\n' + '\n---\n'.join(refined_spells)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  Enhanced {count} spell descriptions with concrete details")
    return count

# Process all grimoires
total = 0
for filename, expected in grimoire_files:
    filepath = os.path.join(base_path, filename)
    count = process_grimoire(filepath, expected)
    total += count

print(f"\n✓ Enhanced {total} spells with concrete examples and practical applications!")
