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

for filename in grimoire_files:
    filepath = os.path.join(base_path, filename)
    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the problematic |---|---| separator lines
    fixed_content = content.replace('|---|---|\n', '')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"  ✓ Removed table separators")

print("\n✓ All grimoire tables cleaned up!")
