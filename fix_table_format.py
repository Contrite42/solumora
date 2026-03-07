import re
import os

grimoire_files = [
    'Common Grimoire.md',
    'Uncommon Grimoire.md',
    'Rare Grimoire.md',
    'Legendary Grimoire.md',
    'Mythic Grimoire.md',
    'Pale Grimoire.md'
]

base_path = r'C:\Users\Contrite42\quartz\content'

def fix_spell_tables(content):
    """Add table separator after Wattage line to properly format tables"""
    
    # Pattern to find wattage line followed by recipe rows
    # We want to insert |---|---| after the wattage line
    pattern = r'(\| Wattage \| .+? \|)\n(\| Shape \|)'
    replacement = r'\1\n|---|---|\n\2'
    
    fixed = re.sub(pattern, replacement, content)
    return fixed

for filename in grimoire_files:
    filepath = os.path.join(base_path, filename)
    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count how many wattage lines exist
    wattage_count = len(re.findall(r'\| Wattage \|', content))
    
    fixed_content = fix_spell_tables(content)
    
    # Count separators added
    separator_count = len(re.findall(r'\|---\|---\|', fixed_content))
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"  ✓ Added {separator_count} table separators (found {wattage_count} spells)")

print("\n✓ All grimoire tables fixed!")
