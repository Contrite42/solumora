#!/usr/bin/env python3
"""
Spell Validator and Migration Tool for Solumora grimoires.

This tool:
1. Scans grimoire pages for spell entries
2. Checks if each spell has an individual page in content/Spells/
3. Verifies that grimoire entries link to individual pages
4. Can generate missing individual spell pages from grimoire entries
5. Can add "Spell Page" links to grimoire entries that lack them
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class SpellEntry:
    """Represents a spell found in a grimoire page."""
    name: str
    summary: str
    variables: dict[str, str]
    grimoire_file: str
    line_number: int
    has_spell_page_link: bool
    spell_page_path: str | None = None


def extract_spells_from_grimoire(grimoire_path: Path) -> list[SpellEntry]:
    """Extract all spell entries from a grimoire markdown file."""
    if not grimoire_path.exists():
        return []
    
    content = grimoire_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    spells: list[SpellEntry] = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Look for spell entry: "**SpellName**"
        if line.startswith("**") and line.endswith("**") and len(line) > 4:
            spell_name = line[2:-2].strip()
            
            # Next line should be summary
            if i + 1 < len(lines):
                summary = lines[i + 1].strip()
                
                # Parse the variable table that follows
                variables: dict[str, str] = {}
                has_spell_page_link = False
                spell_page_path: str | None = None
                
                j = i + 2
                # Skip to table start
                while j < len(lines) and not lines[j].startswith("|"):
                    j += 1
                
                # Skip table header
                if j < len(lines) and lines[j].startswith("|"):
                    j += 1  # Header row
                if j < len(lines) and lines[j].startswith("|"):
                    j += 1  # Separator row
                
                # Parse table rows
                while j < len(lines) and lines[j].startswith("|"):
                    parts = [p.strip() for p in lines[j].split("|")]
                    if len(parts) >= 3:
                        key = parts[1].strip()
                        value = parts[2].strip()
                        
                        if key == "Spell Page":
                            has_spell_page_link = True
                            # Extract link from [[Spells/Name|Name]] format
                            match = re.search(r'\[\[Spells/([^\]|]+)', value)
                            if match:
                                spell_page_path = f"content/Spells/{match.group(1)}.md"
                        else:
                            variables[key] = value
                    j += 1
                
                entry = SpellEntry(
                    name=spell_name,
                    summary=summary,
                    variables=variables,
                    grimoire_file=grimoire_path.name,
                    line_number=i + 1,
                    has_spell_page_link=has_spell_page_link,
                    spell_page_path=spell_page_path
                )
                spells.append(entry)
                i = j
                continue
        
        i += 1
    
    return spells


def check_spell_page_exists(spell_name: str, content_dir: Path) -> Path | None:
    """Check if a spell has an individual page in content/Spells/."""
    spell_path = content_dir / "Spells" / f"{spell_name}.md"
    return spell_path if spell_path.exists() else None


def generate_spell_page(entry: SpellEntry, output_path: Path) -> None:
    """Generate an individual spell page from a grimoire entry."""
    content_parts = [
        f"# {entry.name}\n",
        f"\n{entry.summary}\n",
        "\n## Sigil Variables\n",
        "\n| Variable | Value |\n",
        "|---|---|\n",
    ]
    
    for key, value in entry.variables.items():
        # Clean up default markers
        clean_value = value.replace("_(default — ", "").replace(")_", "")
        content_parts.append(f"| {key} | {clean_value} |\n")
    
    # Add grimoire reference
    grimoire_name = entry.grimoire_file.replace(".md", "")
    content_parts.append(f"\n**Grimoire:** [[{grimoire_name}]]\n")
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(content_parts), encoding="utf-8")


def add_spell_page_link_to_grimoire(grimoire_path: Path, spell_name: str, line_number: int) -> bool:
    """Add a 'Spell Page' row to a spell's variable table in the grimoire."""
    content = grimoire_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # Find the end of the variable table for this spell
    # Start from line_number (which should be the "**Name**" line)
    i = line_number - 1  # Convert to 0-indexed
    
    # Skip past spell name and summary
    i += 2
    
    # Skip to table
    while i < len(lines) and not lines[i].startswith("|"):
        i += 1
    
    # Skip header and separator
    if i < len(lines) and lines[i].startswith("|"):
        i += 1
    if i < len(lines) and lines[i].startswith("|"):
        i += 1
    
    # Find last table row
    last_table_row = i
    while i < len(lines) and lines[i].startswith("|"):
        last_table_row = i
        i += 1
    
    # Insert Spell Page link after last table row
    spell_link = f"| Spell Page | [[Spells/{spell_name}|{spell_name}]] |"
    lines.insert(last_table_row + 1, spell_link)
    
    grimoire_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def validate_grimoires(content_dir: Path, grimoire_files: list[str], fix: bool = False, generate: bool = False) -> dict[str, Any]:
    """
    Validate all spells in grimoire files.
    
    Returns a report with:
    - Total spells found
    - Spells with individual pages
    - Spells missing individual pages  
    - Spells with grimoire links
    - Spells missing grimoire links
    """
    report: dict[str, Any] = {
        "total_spells": 0,
        "with_individual_pages": 0,
        "missing_individual_pages": [],
        "with_grimoire_links": 0,
        "missing_grimoire_links": [],
        "generated_pages": [],
        "added_links": [],
    }
    
    for grimoire_file in grimoire_files:
        grimoire_path = content_dir / grimoire_file
        if not grimoire_path.exists():
            continue
        
        spells = extract_spells_from_grimoire(grimoire_path)
        report["total_spells"] += len(spells)
        
        for spell in spells:
            # Check if individual page exists
            spell_page = check_spell_page_exists(spell.name, content_dir)
            
            if spell_page:
                report["with_individual_pages"] += 1
            else:
                report["missing_individual_pages"].append({
                    "name": spell.name,
                    "grimoire": spell.grimoire_file
                })
                
                if generate:
                    output_path = content_dir / "Spells" / f"{spell.name}.md"
                    generate_spell_page(spell, output_path)
                    report["generated_pages"].append(str(output_path))
                    print(f"Generated: {output_path}")
                    spell_page = output_path
            
            # Check if grimoire entry has link
            if spell.has_spell_page_link:
                report["with_grimoire_links"] += 1
            else:
                report["missing_grimoire_links"].append({
                    "name": spell.name,
                    "grimoire": spell.grimoire_file,
                    "line": spell.line_number
                })
                
                if fix and spell_page:
                    if add_spell_page_link_to_grimoire(grimoire_path, spell.name, spell.line_number):
                        report["added_links"].append({
                            "name": spell.name,
                            "grimoire": spell.grimoire_file
                        })
                        print(f"Added link: {spell.name} in {spell.grimoire_file}")
    
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate and fix spell organization in grimoire files"
    )
    parser.add_argument(
        "--content-dir",
        type=str,
        default="content",
        help="Path to content directory (default: content)"
    )
    parser.add_argument(
        "--grimoires",
        nargs="*",
        default=[
            "Common Grimoire.md",
            "Uncommon Grimoire.md",
            "Rare Grimoire.md",
            "Legendary Grimoire.md",
            "Mythic Grimoire.md",
        ],
        help="Grimoire files to validate"
    )
    parser.add_argument(
        "--generate-missing",
        action="store_true",
        help="Generate individual spell pages for spells that lack them"
    )
    parser.add_argument(
        "--add-links",
        action="store_true",
        help="Add 'Spell Page' links to grimoire entries that lack them"
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Only generate a report, don't modify any files"
    )
    
    args = parser.parse_args()
    
    content_dir = Path(args.content_dir)
    if not content_dir.exists():
        print(f"Error: Content directory not found: {content_dir}")
        return 1
    
    fix = args.add_links and not args.report_only
    generate = args.generate_missing and not args.report_only
    
    print(f"Validating grimoires in: {content_dir}")
    print(f"Generate missing pages: {generate}")
    print(f"Add missing links: {fix}")
    print()
    
    report = validate_grimoires(content_dir, args.grimoires, fix=fix, generate=generate)
    
    print("\n=== VALIDATION REPORT ===")
    print(f"Total spells found: {report['total_spells']}")
    print(f"Spells with individual pages: {report['with_individual_pages']}")
    print(f"Spells with grimoire links: {report['with_grimoire_links']}")
    print()
    
    if report["missing_individual_pages"]:
        print(f"Missing individual pages: {len(report['missing_individual_pages'])}")
        for spell in report["missing_individual_pages"][:10]:
            print(f"  - {spell['name']} (in {spell['grimoire']})")
        if len(report["missing_individual_pages"]) > 10:
            print(f"  ... and {len(report['missing_individual_pages']) - 10} more")
        print()
    
    if report["missing_grimoire_links"]:
        print(f"Missing grimoire links: {len(report['missing_grimoire_links'])}")
        for spell in report["missing_grimoire_links"][:10]:
            print(f"  - {spell['name']} (in {spell['grimoire']}, line {spell['line']})")
        if len(report["missing_grimoire_links"]) > 10:
            print(f"  ... and {len(report['missing_grimoire_links']) - 10} more")
        print()
    
    if report["generated_pages"]:
        print(f"Generated {len(report['generated_pages'])} spell pages")
    
    if report["added_links"]:
        print(f"Added {len(report['added_links'])} grimoire links")
    
    return 0


if __name__ == "__main__":
    exit(main())
