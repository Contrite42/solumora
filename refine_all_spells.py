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

# Helper to generate concrete examples based on spell mechanics
def get_concrete_examples(hook, discipline, output, pattern, target):
    examples = []
    
    # Hook-based actions
    if hook == 'Emit':
        if discipline in ['Force', 'Kinetic']:
            examples.append('invisible strikes')
        elif discipline == 'Fire':
            examples.append('flames')
        elif discipline == 'Cold':
            examples.append('freezing wind')
        elif discipline == 'Lightning':
            examples.append('crackling bolts')
    elif hook == 'Bind':
        if discipline in ['Force', 'Kinetic']:
            examples.append('locks')
        examples.append('holds')
    elif hook == 'Sense':
        examples.append('detects')
    elif hook == 'Transform':
        examples.append('alters')
        examples.append('reshapes')
    
    # Output-based results
    if output == 'Damage':
        examples.extend(['crushing impacts', 'destructive force'])
    elif output == 'Protection':
        examples.extend(['shields', 'barriers'])
    elif output == 'Movement':
        examples.extend(['pushes', 'pulls', 'slides'])
    elif output == 'Constraint':
        examples.extend(['pins', 'immobilizes', 'restrains'])
    
    return examples[:3] if examples else []

def get_practical_benefit(wattage, persistence, reach, control_tier):
    benefits = []
    
    # Low wattage = efficiency
    if wattage < 50:
        benefits.append('minimal flux drain makes it practical for repeated use')
    elif wattage < 200:
        benefits.append('affordable flux cost allows frequent casting')
    
    # Sustained = maintained effect
    if persistence == 'Sustained':
        benefits.append('can be maintained as long as concentration holds')
    elif 'Timed' in persistence and 'Long' in persistence:
        benefits.append('runs its full duration without further attention')
    
    # Long reach = tactical advantage
    if 'Long' in reach or 'Extreme' in reach:
        benefits.append('exceptional range provides tactical flexibility')
    
    # High control = precision
    if control_tier and int(control_tier.replace('T', '')) >= 5:
        benefits.append('requires advanced channeling skill')
    
    return benefits[0] if benefits else None

def refine_description(name, old_desc, recipe):
    hook = recipe.get('Hook', '')
    discipline = recipe.get('Discipline', '')
    output = recipe.get('Output', '')
    pattern = recipe.get('Pattern', '')
    reach = recipe.get('Reach', '')
    persistence = recipe.get('Persistence', '')
    target = recipe.get('Target', '')
    wattage = recipe.get('Wattage', 100)
    control_tier = recipe.get('Control Tier', '')
    
    # Start building refined description
    parts = []
    
    # Action verb based on hook
    action_verbs = {
        'Emit': 'Projects',
        'Bind': 'Anchors',
        'Sense': 'Detects',
        'Transform': 'Reshapes',
        'Invoke': 'Summons',
        'Counter': 'Disrupts',
        'Amplify': 'Enhances',
        'Redirect': 'Deflects'
    }
    
    action = action_verbs.get(hook, 'Channels')
    
    # Energy type from discipline
    energy_types = {
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
        'Space': 'spatial distortion'
    }
    
    energy = energy_types.get(discipline, 'flux energy')
    
    # Pattern description
    pattern_desc = {
        'Beam': 'as a focused beam',
        'Cone': 'as a widening cone',
        'Sphere': 'in a spherical burst',
        'Wall': 'as a barrier wall',
        'Line': 'in a straight line',
        'Chain': 'that chains between targets',
        'Ray': 'as a precise ray',
        'Aura': 'as a surrounding aura',
        'Touch': 'through direct touch',
        'Area': 'across an area'
    }
    
    shape = pattern_desc.get(pattern, '')
    
    # Output effect
    output_effects = {
        'Damage': 'delivering destructive impact',
        'Protection': 'forming a defensive barrier',
        'Movement': 'forcing motion',
        'Constraint': 'immobilizing the target',
        'Healing': 'restoring vitality',
        'Detection': 'revealing hidden information',
        'Illusion': 'creating false sensory input',
        'Transformation': 'altering physical properties'
    }
    
    effect = output_effects.get(output, 'producing its effect')
    
    # Reach conversion
    reach_desc = ''
    if 'Short' in reach:
        reach_desc = 'within arm\'s reach'
    elif 'Medium' in reach:
        reach_desc = 'within 50 feet'
    elif 'Long (250 ft)' in reach:
        reach_desc = 'at up to 250 feet'
    elif 'Long' in reach:
        reach_desc = 'at extended range'
    elif 'Extreme' in reach:
        reach_desc = 'at extreme distances'
    elif 'Touch' in reach:
        reach_desc = 'at point of contact'
    
    # Target specification
    target_desc = ''
    if target == 'Object':
        target_desc = 'on objects'
    elif target == 'Surface':
        target_desc = 'across surfaces'
    elif target == 'Creature':
        target_desc = 'against living targets'
    elif target == 'Area':
        target_desc = 'across an area'
    elif target == 'Where Written':
        target_desc = 'at the marked location'
    
    # Build core sentence
    core = f"{action} {energy}"
    if shape:
        core += f" {shape}"
    if reach_desc:
        core += f" {reach_desc}"
    if target_desc:
        core += f" {target_desc}"
    core += f", {effect}"
    
    # Add persistence clause
    if persistence == 'Sustained':
        core += ". Must be actively maintained, but"
        benefit = get_practical_benefit(wattage, persistence, reach, control_tier)
        if benefit:
            core += f" the {benefit}"
        else:
            core += " can be held as long as concentration permits"
    elif 'Timed' in persistence:
        if 'Short' in persistence:
            core += ". Runs for roughly a minute before dissipating"
        elif 'Long' in persistence:
            core += ". Persists for several minutes without further attention"
        else:
            core += ". Holds for its duration then fades"
    elif persistence == 'Instantaneous':
        core += " in a single moment"
    elif persistence == 'Permanent':
        core += ". The effect becomes permanent once established"
    
    # Add practical benefit if not already included
    if 'Sustained' not in persistence:
        benefit = get_practical_benefit(wattage, persistence, reach, control_tier)
        if benefit and wattage < 100:
            core += f". The {benefit}"
    
    return core + "."

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
            continue
        
        # Extract spell name
        name_match = re.match(r'\*\*(.+?)\*\*', lines[0])
        if not name_match:
            continue
        
        name = name_match.group(1)
        
        # Find old description and wattage
        old_desc = ''
        wattage_line = ''
        recipe_start = -1
        
        for i, line in enumerate(lines[1:], 1):
            if line.startswith('| Wattage |'):
                wattage_line = line
                recipe_start = i + 1
                if i > 1:
                    old_desc = lines[i-1]
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
            if not line or line == '':
                continue
            if not line.startswith('|'):
                break
            
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                key = parts[0]
                value = parts[1]
                recipe[key] = value
        
        # Generate refined description
        new_desc = refine_description(name, old_desc, recipe)
        
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
    
    print(f"  Refined {count} spell descriptions")
    return count

# Process all grimoires
for filename, expected in grimoire_files:
    filepath = os.path.join(base_path, filename)
    process_grimoire(filepath, expected)

print("\n✓ All grimoires refined to user-friendly descriptions!")
