#!/usr/bin/env python3
import re
from pathlib import Path

FILES = [
    "content/Common Grimoire.md",
    "content/Uncommon Grimoire.md",
    "content/Rare Grimoire.md",
    "content/Legendary Grimoire.md",
    "content/Mythic Grimoire.md",
    "content/Pale Grimoire.md",
]

VERB = {
    "Emit": "Releases",
    "Transform": "Alters",
    "Sense": "Detects",
    "Bind": "Constrains",
    "Filter": "Filters",
    "Move": "Displaces",
    "Ward": "Shields against",
    "Counter": "Counters",
    "Control": "Manipulates",
}

PATTERN_PHRASE = {
    "Point": "at a single point",
    "Plane": "across a surface",
    "Beam": "in a focused beam",
    "Cone": "in a spreading cone",
    "Ring": "in a ring",
    "Cylinder": "in a cylinder",
    "Sphere": "in a sphere",
    "Field": "across a field",
}

REACH_PHRASE = {
    "Self": "from the sigil",
    "Touch": "at touch range",
    "Short (10 ft)": "within 10 feet",
    "Medium (50 ft)": "within 50 feet",
    "Long (200 ft)": "within 200 feet",
    "Line-of-Sight": "at line of sight",
    "Linked": "through a linked anchor",
    "Anchored": "from an anchored point",
}

TARGET_PHRASE = {
    "Where Written": "centered on the inscribed location",
    "Self": "targeting the caster",
    "Object": "targeting an object",
    "Surface": "targeting a surface",
    "Individual": "targeting an individual",
    "Marked": "targeting a marked subject",
    "Group": "targeting a group",
    "Filter": "targeting a filtered set",
    "Search": "targeting the search area",
}

PERSISTENCE_SENTENCE = {
    "Immediate": "",
    "Timed (Short)": " It lasts up to one minute.",
    "Timed (Long)": " It lasts up to one hour.",
    "Sustained": " It persists while actively sustained.",
    "Conditional": " It persists until the set condition is met.",
    "Latched": " It remains latched until dismissed.",
    "Permanent": " It is permanent once established.",
}


def clean_value(key: str, value: str) -> str:
    v = value.strip()
    v = v.replace("â€”", "-").replace("â€“", "-")
    v = re.sub(r"_?\(default\s*[\-–—]?\s*", "", v, flags=re.IGNORECASE)
    v = v.replace(")_", ")")
    v = v.strip(" _")

    low = v.lower()

    if key == "Pattern":
        if "point" in low:
            return "Point"
        if "plane" in low or "default" in low:
            return "Plane"
        if "beam" in low:
            return "Beam"
        if "cone" in low:
            return "Cone"
        if "ring" in low:
            return "Ring"
        if "cylinder" in low:
            return "Cylinder"
        if "sphere" in low:
            return "Sphere"
        if "field" in low:
            return "Field"

    if key == "Reach":
        if "touch" in low:
            return "Touch"
        if "short" in low or "10 ft" in low:
            return "Short (10 ft)"
        if "medium" in low or "50 ft" in low:
            return "Medium (50 ft)"
        if "long" in low or "200 ft" in low:
            return "Long (200 ft)"
        if "line-of-sight" in low or "line of sight" in low:
            return "Line-of-Sight"
        if "linked" in low:
            return "Linked"
        if "anchored" in low:
            return "Anchored"
        if "self" in low or "default" in low:
            return "Self"

    if key == "Persistence":
        if "timed" in low and "short" in low:
            return "Timed (Short)"
        if "timed" in low and "long" in low:
            return "Timed (Long)"
        if "sustained" in low:
            return "Sustained"
        if "conditional" in low:
            return "Conditional"
        if "latched" in low:
            return "Latched"
        if "permanent" in low:
            return "Permanent"
        if "immediate" in low or "default" in low:
            return "Immediate"

    if key == "Target":
        if "where written" in low or "default" in low:
            return "Where Written"
        if low == "self":
            return "Self"
        if "object" in low:
            return "Object"
        if "surface" in low:
            return "Surface"
        if "individual" in low:
            return "Individual"
        if "marked" in low:
            return "Marked"
        if "group" in low:
            return "Group"
        if "filter" in low:
            return "Filter"
        if "search" in low:
            return "Search"

    return v


def build_description(fields: dict) -> str:
    hook = fields.get("Hook", "")
    discipline = fields.get("Discipline", "flux")
    pattern = fields.get("Pattern", "Plane")
    reach = fields.get("Reach", "Self")
    target = fields.get("Target", "Where Written")
    persistence = fields.get("Persistence", "Immediate")

    verb = VERB.get(hook, "Affects")
    pattern_phrase = PATTERN_PHRASE.get(pattern, "across a surface")
    reach_phrase = REACH_PHRASE.get(reach, "from the sigil")
    target_phrase = TARGET_PHRASE.get(target, "centered on the inscribed location")
    persist_tail = PERSISTENCE_SENTENCE.get(persistence, "")

    return f"{verb} {discipline.lower()} {pattern_phrase} {reach_phrase}, {target_phrase}.{persist_tail}"


def repair_file(path: Path) -> tuple[int, int]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()

    out = []
    i = 0
    repaired = 0
    spells = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith("**") and line.endswith("**"):
            spells += 1
            out.append(line)

            # Existing description line
            if i + 1 < len(lines):
                i += 1
                # skip old description and rebuild later
            else:
                out.append("Casts a documented sigil effect.")
                break

            # Parse table rows immediately after description
            fields = {}
            table_start = i + 1
            j = table_start
            while j < len(lines) and lines[j].startswith("|"):
                m = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", lines[j])
                if m:
                    k = m.group(1).strip()
                    v = m.group(2).strip()
                    if k not in ("Variable", "---"):
                        fields[k] = clean_value(k, v)
                j += 1

            # Write repaired description
            out.append(build_description(fields))

            # Rewrite table preserving rows, normalized values
            # Keep header removed per user's previous request.
            ordered = [
                "Shape", "Hook", "Mode", "Control Tier", "Discipline", "Output",
                "Pattern", "Reach", "Persistence", "Target", "Wattage",
            ]
            for k in ordered:
                if k in fields:
                    out.append(f"| {k} | {fields[k]} |")

            # Continue from first non-table line
            i = j
            repaired += 1
            continue

        out.append(line)
        i += 1

    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return repaired, spells


def main() -> None:
    for rel in FILES:
        p = Path(rel)
        repaired, spells = repair_file(p)
        print(f"{p.name}: repaired={repaired} spells={spells}")


if __name__ == "__main__":
    main()
