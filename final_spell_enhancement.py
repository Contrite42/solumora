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

def generate_description(recipe):
    """Generate a rich, detailed description from recipe components"""
    
    hook = recipe.get('Hook', '')
    discipline = recipe.get('Discipline', '')
    output = recipe.get('Output', '')
    pattern = recipe.get('Pattern', '')
    reach = recipe.get('Reach', '')
    persistence = recipe.get('Persistence', '')
    target = recipe.get('Target', '')
    wattage = recipe.get('Wattage', 100)
    mode = recipe.get('Mode', '')
    
    # Build description components
    effect_desc = get_effect_description(hook, discipline, output, pattern, mode)
    spatial_desc = get_spatial_description(pattern, reach, target)
    persistence_desc = get_persistence_description(persistence, wattage)
    practical_desc = get_practical_note(hook, output, wattage, persistence, reach)
    
    # Assemble full description
    parts = []
    parts.append(effect_desc)
    if spatial_desc:
        parts.append(spatial_desc)
    if persistence_desc:
        parts.append(persistence_desc)
    if practical_desc:
        parts.append(practical_desc)
    
    return ' '.join(parts)

def get_effect_description(hook, discipline, output, pattern, mode):
    """Generate what the spell actually does"""
    
    # Damage/Kinetic/Force effects
    if output in ['Damage', 'Kinetic', 'Force']:
        if hook == 'Emit':
            if pattern == 'Beam':
                if discipline in ['Force', 'Kinetic']:
                    return "Fires a concentrated beam of kinetic force that punches through obstacles and hammers targets."
                elif discipline == 'Fire':
                    return "Launches a focused beam of flames that burns through targets and ignites flammable materials."
                elif discipline == 'Lightning':
                    return "Releases a crackling lightning bolt that electrocutes the target on impact."
                elif discipline == 'Cold':
                    return "Projects a freezing ray that chills targets to the bone and frosts surfaces."
            elif pattern == 'Cone':
                if discipline in ['Force', 'Kinetic']:
                    return "Unleashes a widening blast of kinetic force that sends enemies and objects tumbling backward."
                elif discipline == 'Fire':
                    return "Erupts in a cone of flames that engulfs everything in its path."
                elif discipline == 'Lightning':
                    return "Discharges branching electrical energy in a forward arc that shocks multiple targets."
            elif pattern == 'Sphere':
                return "Detonates in a spherical blast that hurls everything away from the epicenter."
            elif pattern == 'Ray':
                if discipline in ['Force', 'Kinetic']:
                    return "Strikes with a precise kinetic ray that impacts like an invisible hammer blow."
            else:
                if discipline in ['Force', 'Kinetic']:
                    return "Projects kinetic force that delivers crushing impact."
                elif discipline == 'Fire':
                    return "Releases flames that sear and burn targets."
                elif discipline == 'Lightning':
                    return "Discharges electrical energy that shocks and jolts."
                elif discipline == 'Cold':
                    return "Emanates freezing energy that numbs and chills."
    
    # Protection/Shielding
    elif output in ['Protection', 'Shielding', 'Defense', 'Defensive']:
        if discipline in ['Force', 'Kinetic']:
            return "Projects a kinetic barrier that blocks physical impacts—strikes, thrown objects, rushing bodies."
        elif discipline == 'Fire':
            return "Raises a heat-deflecting shield that repels flames and disperses thermal energy."
        elif discipline == 'Cold':
            return "Forms a freezing barrier that blocks cold-based attacks and stabilizes temperature."
        elif discipline == 'Lightning':
            return "Creates an electrical ground that dissipates lightning strikes and electrical discharges."
        elif discipline in ['Soul', 'Mind']:
            return "Establishes a psychic shield that blocks mental intrusion and soul-binding attempts."
        else:
            return "Generates a protective barrier that deflects incoming threats."
    
    # Constraint/Binding/Immobilization
    elif output in ['Constraint', 'Binding', 'Immobilization']:
        if discipline in ['Force', 'Kinetic']:
            return "Locks targets in place with kinetic force, preventing movement or escape."
        elif discipline == 'Binding':
            return "Pins limbs and joints, restricting physical motion and forcing immobility."
        elif discipline in ['Soul', 'Mind']:
            return "Paralyzes voluntary movement through psychic pressure and soul-binding."
        else:
            return "Restrains and immobilizes the target, holding them firmly in place."
    
    # Movement/Displacement
    elif output in ['Movement', 'Displacement']:
        if hook == 'Emit':
            return "Shoves targets forcefully in the desired direction, sending them staggering or flying."
        elif hook == 'Bind':
            return "Drags targets toward the marked location, pulling them against their will."
        else:
            return "Forces targets into motion, repositioning them tactically."
    
    # Detection/Sensing/Awareness
    elif output in ['Detection', 'Awareness', 'Information', 'Perception']:
        if discipline == 'Mind':
            return "Detects surface thoughts and immediate mental states, revealing intentions and emotional impressions."
        elif discipline == 'Soul':
            return "Exposes soul-signatures, binding marks, and metaphysical connections."
        elif discipline == 'Space':
            return "Maps spatial layout, revealing hidden passages, concealed objects, and structural features."
        elif discipline == 'Light':
            return "Illuminates the area and reveals hidden or invisible entities through radiant detection."
        else:
            return "Senses and reveals hidden information, detecting presences and anomalies."
    
    # Healing/Restoration
    elif output in ['Healing', 'Restoration', 'Vitality', 'Recovery']:
        return "Mends wounds, knits torn tissue, and restores physical integrity—effective for cuts, bruises, and minor trauma."
    
    # Transformation/Alteration
    elif output in ['Transformation', 'Alteration', 'Modification']:
        if target in ['Object', 'Material']:
            return "Alters physical properties—hardness, temperature, density, state of matter."
        elif target == 'Creature':
            return "Reshapes living tissue and organic structure, transforming biological form."
        else:
            return "Transforms and reconfigures the target's fundamental properties."
    
    # Illusion/Deception
    elif output in ['Illusion', 'Deception', 'Phantom']:
        return "Creates false sensory impressions—phantom sounds, deceptive images, illusory textures and smells."
    
    # Soul/Mind specific outputs
    elif output in ['Soul', 'Mind', 'Psychic']:
        if hook == 'Emit':
            if discipline == 'Mind':
                return "Projects psychic force that penetrates mental defenses and influences thought patterns."
            elif discipline == 'Soul':
                return "Releases soul-flux that resonates with targets' metaphysical essence."
        elif hook == 'Bind':
            if discipline == 'Soul':
                return "Anchors soul-energy to the marked location, creating a metaphysical binding."
            elif discipline == 'Mind':
                return "Locks mental patterns in place, preventing thought divergence."
        elif hook == 'Sense':
            if discipline == 'Soul':
                return "Detects soul-signatures and binding marks, revealing metaphysical connections."
            elif discipline == 'Mind':
                return "Reads surface thoughts and current mental states."
        elif hook == 'Filter':
            if discipline == 'Soul':
                return "Screens soul-flux by signature, blocking unwanted metaphysical influence while permitting recognized patterns."
            elif discipline == 'Mind':
                return "Filters psychic input, protecting against mental intrusion while allowing benign contact."
    
    # Reactive/Chemical
    elif output in ['Reactive', 'Chemical']:
        if hook == 'Emit':
            return "Releases reactive flux that triggers chemical responses—corrosion, combustion, crystallization."
        elif hook == 'Transform':
            return "Induces chemical transformation, altering molecular structure and material composition."
    
    # Photonic/Light
    elif output == 'Photonic':
        if hook == 'Emit':
            return "Emits radiant light energy that illuminates, heats, or burns depending on intensity."
        elif hook == 'Transform':
            return "Manipulates light itself, bending rays, shifting colors, or creating optical effects."
    
    # Raw flux (generic but give it character)
    elif output == 'Raw' or discipline == 'Raw':
        if hook == 'Emit':
            return "Releases unstructured flux energy in its rawest form—unpredictable and potent."
        elif hook == 'Bind':
            return "Anchors raw flux to the target, creating a volatile binding."
        elif hook == 'Transform':
            return "Channels raw flux to induce fundamental transformation."
    
    # Generic fallbacks based on hook
    if hook == 'Emit':
        return f"Projects {discipline.lower()} energy outward, delivering its effect."
    elif hook == 'Bind':
        return f"Anchors {discipline.lower()} flux to the target, holding it in place."
    elif hook == 'Sense':
        return f"Detects {discipline.lower()}-related phenomena and gathers information."
    elif hook == 'Transform':
        return f"Reshapes the target using {discipline.lower()} flux."
    elif hook == 'Counter':
        return f"Disrupts and negates {discipline.lower()} effects."
    elif hook == 'Amplify':
        return f"Enhances and intensifies {discipline.lower()} flux."
    elif hook == 'Filter':
        return f"Screens {discipline.lower()} flux, blocking unwanted elements while allowing valid ones through."
    elif hook == 'Reflect':
        return f"Bounces {discipline.lower()} energy back toward its source."
    else:
        return f"Channels {discipline.lower()} flux to produce its effect."

def get_spatial_description(pattern, reach, target):
    """Describe the spell's spatial characteristics"""
    
    parts = []
    
    # Pattern shape
    if pattern == 'Beam':
        parts.append("Travels in a straight line")
    elif pattern == 'Cone':
        parts.append("Spreads in a widening arc")
    elif pattern == 'Sphere':
        parts.append("Expands in all directions from the center")
    elif pattern == 'Wall':
        parts.append("Forms a vertical barrier")
    elif pattern == 'Plane':
        parts.append("Extends across a flat surface")
    elif pattern == 'Aura':
        parts.append("Radiates from the caster")
    elif pattern == 'Chain':
        parts.append("Jumps from target to target")
    elif pattern == 'Field':
        parts.append("Fills an enclosed volume")
    
    # Reach
    if 'Touch' in reach:
        parts.append("at point of contact")
    elif 'Short' in reach:
        parts.append("within 10 feet")
    elif 'Medium' in reach:
        parts.append("within 50 feet")
    elif 'Long (250 ft)' in reach:
        parts.append("at up to 250 feet")
    elif 'Long (200 ft)' in reach:
        parts.append("at up to 200 feet")
    elif 'Long (100 ft)' in reach:
        parts.append("at up to 100 feet")
    elif 'Extreme' in reach:
        parts.append("at extreme distances")
    elif 'Line-of-Sight' in reach:
        parts.append("anywhere visible")
    
    # Target type
    if target == 'Creature':
        parts.append("targeting living beings")
    elif target == 'Individual':
        parts.append("affecting a single person")
    elif target == 'Group':
        parts.append("hitting multiple targets")
    elif target == 'Area':
        parts.append("covering the entire area")
    
    if parts:
        return ', '.join(parts[: 2]) + '.'
    return ''

def get_persistence_description(persistence, wattage):
    """Describe how long the spell lasts"""
    
    if persistence == 'Sustained':
        if wattage < 100:
            return "Must be actively maintained, but the flux drain is minimal, making extended use practical."
        else:
            return "Requires continuous concentration to sustain."
    elif 'Timed (Short)' in persistence:
        return "Lasts roughly a minute before dissipating."
    elif 'Timed (Long)' in persistence:
        return "Persists for several minutes without further attention."
    elif persistence == 'Instantaneous' or persistence == 'Immediate':
        return "Takes effect in a single instant."
    elif persistence == 'Permanent':
        return "The effect becomes permanent once established."
    elif persistence == 'Conditional':
        return "Persists until a specified condition triggers its release."
    return ''

def get_practical_note(hook, output, wattage, persistence, reach):
    """Add practical use case or tactical note"""
    
    notes = []
    
    # Output-based applications
    if output in ['Protection', 'Shielding', 'Defense']:
        notes.append("Useful for defending doorways, covering retreat, or holding defensive positions.")
    elif output in ['Constraint', 'Binding']:
        notes.append("Ideal for subduing opponents or securing prisoners without lethal force.")
    elif output in ['Damage', 'Kinetic', 'Force']:
        if 'Long' in reach or 'Extreme' in reach:
            notes.append("Effective for engaging distant threats or eliminating targets beyond melee range.")
        else:
            notes.append("Suitable for close-quarters combat or breaching physical barriers.")
    elif output in ['Detection', 'Awareness']:
        notes.append("Practical for reconnaissance, searching rooms, or identifying hidden threats.")
    elif output in ['Movement', 'Displacement']:
        notes.append("Useful for tactical repositioning, creating distance, or knocking enemies prone.")
    elif output in ['Healing', 'Restoration']:
        notes.append("Essential for field medicine, stabilizing injuries, and emergency treatment.")
    
    # Cost notes (only if not already mentioned in persistence)
    if wattage < 50 and persistence != 'Sustained':
        notes.append("The minimal flux cost allows frequent casting without exhausting reserves.")
    elif wattage < 150 and persistence != 'Sustained':
        notes.append("Affordable flux cost makes it viable for routine use.")
    
    # Return first relevant note
    return notes[0] if notes else ''

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
        new_desc = generate_description(recipe)
        
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
    
    print(f"  ✓ Refined {count} spells with detailed, user-friendly descriptions")
    return count

# Process all grimoires
print("=" * 70)
print("ENHANCING ALL SPELL DESCRIPTIONS WITH CONCRETE DETAILS")
print("=" * 70)

total = 0
for filename, expected in grimoire_files:
    filepath = os.path.join(base_path, filename)
    count = process_grimoire(filepath, expected)
    total += count

print("=" * 70)
print(f"✓ COMPLETE: Enhanced {total} spells with concrete examples and practical use cases!")
print("=" * 70)
