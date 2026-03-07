import re
from pathlib import Path

files = [
    'Common Grimoire.md',
    'Uncommon Grimoire.md',
    'Rare Grimoire.md',
    'Legendary Grimoire.md',
    'Mythic Grimoire.md',
    'Pale Grimoire.md',
]

base = Path(r'C:\Users\Contrite42\quartz\content')

for name in files:
    path = base / name
    text = path.read_text(encoding='utf-8')

    # Normalize all line endings first.
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Replace any rule-like separator line with ***.
    text = re.sub(r'(?m)^\s*---+\s*$', '***', text)
    text = re.sub(r'(?m)^\s*\*\*\*+\s*$', '***', text)

    # Ensure blank lines around separators so they never underline previous lines.
    text = re.sub(r'\n*\*\*\n*', '\n\n***\n\n', text)

    # Collapse excessive blank lines while keeping readable spacing.
    text = re.sub(r'\n{3,}', '\n\n', text)

    path.write_text(text.rstrip() + '\n', encoding='utf-8')
    print(f'normalized {name}')
