import re
from pathlib import Path

FILES = [
    'Common Grimoire.md',
    'Uncommon Grimoire.md',
    'Rare Grimoire.md',
    'Legendary Grimoire.md',
    'Mythic Grimoire.md',
    'Pale Grimoire.md',
]

BASE = Path(r'C:\Users\Contrite42\quartz\content')

SPELL_BLOCK_RE = re.compile(
    r'\*\*\*\n+([^\n*|][^\n]*)\n+\*\*\*\n+(.*?)(?=\n\*\*\*\n+[^\n*|][^\n]*\n+\*\*\*|\Z)',
    re.DOTALL,
)


def clean_body(body: str) -> str:
    body = body.replace('\\n\\n', '')
    lines = body.split('\n')
    cleaned = []
    for line in lines:
        t = line.strip()
        if t in {'*', '', '\\n', '\\n\\n', '*\\n', '*\\n\\n'}:
            if cleaned and cleaned[-1] != '':
                cleaned.append('')
            continue
        cleaned.append(line.rstrip())

    # Trim extra blank lines at both ends and collapse internal runs.
    while cleaned and cleaned[0] == '':
        cleaned.pop(0)
    while cleaned and cleaned[-1] == '':
        cleaned.pop()

    collapsed = []
    for line in cleaned:
        if line == '' and collapsed and collapsed[-1] == '':
            continue
        collapsed.append(line)

    return '\n'.join(collapsed)


def repair_file(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding='utf-8').replace('\r\n', '\n').replace('\r', '\n')

    first_sep = text.find('\n***\n')
    if first_sep == -1:
        return 0, 0

    intro = text[:first_sep].rstrip()
    body = text[first_sep + 1 :]

    matches = list(SPELL_BLOCK_RE.finditer(body))
    repaired_blocks = []

    for m in matches:
        name = m.group(1).strip()
        spell_body = clean_body(m.group(2))
        repaired_blocks.append(f"**{name}**\n{spell_body}")

    if not repaired_blocks:
        return 0, 0

    out = intro + '\n\n***\n\n' + '\n\n***\n\n'.join(repaired_blocks) + '\n'
    path.write_text(out, encoding='utf-8')
    return len(matches), len(repaired_blocks)


if __name__ == '__main__':
    for file_name in FILES:
        p = BASE / file_name
        found, rebuilt = repair_file(p)
        print(f"{file_name}: found={found} rebuilt={rebuilt}")
