#!/usr/bin/env python3
"""
Sigil Maker for Solumora spell design.

Creates validated spell definitions from a JSON spec, calculates Watts cost from
canon rules, and exports AI-readable spell data plus markdown compatible with
grimoire pages.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

# Canon rules sourced from content/Flux Cost Reference.md and related spell docs.
SHAPES = {
    "Triangle": {"outer_slots": 3, "base_w": 3},
    "Square": {"outer_slots": 4, "base_w": 8},
    "Pentagon": {"outer_slots": 5, "base_w": 20},
    "Circle": {"outer_slots": 6, "base_w": 55},
}

DISCIPLINE_MULTIPLIERS = {
    "Raw": 1,
    "Force": 2,
    "Heat": 2,
    "Light": 3,
    "Sound": 4,
    "Electric": 5,
    "Chemical": 5,
    "Binding": 10,
    "Mind": 25,
    "Soul": 75,
}

HOOKS = {
    "Emit",
    "Shape",
    "Bind",
    "Ward",
    "Trigger",
    "Transform",
    "Move",
    "Sense",
    "Filter",
    "Amplify",
    "Dampen",
    "Counter",
}

MODES = {"Create", "Affect", "Control"}

OUTPUT_MODES = {
    "Raw",
    "Thermal",
    "Kinetic",
    "Shock",
    "Reactive",
    "Photonic",
    "Sonic",
    "Neuro",
    "Constraint",
    "Soul",
}

PATTERN_COSTS = {
    "Point": 0,
    "Plane": 0,
    "Beam": 5,
    "Cone": 10,
    "Ring": 15,
    "Cylinder": 20,
    "Sphere": 30,
    "Field": 60,
}

REACH_COSTS = {
    "Self": 0,
    "Anchored": 0,  # Canon list includes Anchored but no explicit premium table value.
    "Touch": 2,
    "Short": 5,
    "Medium": 15,
    "Long": 40,
    "Line-of-Sight": 80,
    "Linked": 150,
}

PERSISTENCE_COSTS = {
    "Immediate": 0,
    "Timed Short": 5,
    "Timed Long": 25,
    "Sustained": None,  # +10 per 10 minutes active
    "Conditional": 20,
    "Latched": 40,
    "Permanent": 400,
}

TARGET_COSTS = {
    "Where Written": 0,
    "Self": 0,
    "Object": 2,
    "Surface": 5,
    "Individual": 8,
    "Marked": 15,
    "Group": 35,
    "Filter": 60,
}

DEFAULTS = {
    "output_mode": "Raw",
    "pattern": "Plane",
    "reach": "Self",
    "persistence": "Immediate",
    "target_spec": "Where Written",
}

NATURAL_OUTPUT_BY_DISCIPLINE = {
    "Raw": "Raw",
    "Force": "Kinetic",
    "Heat": "Thermal",
    "Light": "Photonic",
    "Sound": "Sonic",
    "Electric": "Shock",
    "Chemical": "Reactive",
    "Binding": "Constraint",
    "Mind": "Neuro",
    "Soul": "Soul",
}

# Adjacent examples from canon include "Kinetic from Heat". Remaining pairs are
# documented assumptions to keep deterministic pricing for generated spells.
ADJACENT_OUTPUT_BY_DISCIPLINE = {
    "Force": {"Thermal", "Constraint"},
    "Heat": {"Kinetic", "Reactive"},
    "Light": {"Sonic", "Thermal"},
    "Sound": {"Photonic", "Kinetic"},
    "Electric": {"Reactive", "Kinetic"},
    "Chemical": {"Shock", "Thermal"},
    "Binding": {"Kinetic", "Reactive"},
    "Raw": set(),
    "Mind": set(),
    "Soul": set(),
}

PHYSICAL_OUTPUTS = {
    "Thermal",
    "Kinetic",
    "Shock",
    "Reactive",
    "Photonic",
    "Sonic",
    "Constraint",
}

PERSISTENCE_ALIASES = {
    "timed short": "Timed Short",
    "timed (short)": "Timed Short",
    "timed_short": "Timed Short",
    "timed long": "Timed Long",
    "timed (long)": "Timed Long",
    "timed_long": "Timed Long",
}

REACH_ALIASES = {
    "los": "Line-of-Sight",
    "line of sight": "Line-of-Sight",
    "line-of-sight": "Line-of-Sight",
}


@dataclass
class SpellSpec:
    name: str
    summary: str
    effect_description: str
    hook: str
    mode: str
    shape: str
    discipline: str
    output_mode: str
    pattern: str
    reach: str
    persistence: str
    target_spec: str
    sustained_minutes: int = 0
    hook_mode_multiplier: float = 1.0
    hook_mode_flat_w: int = 0
    notes: str = ""


@dataclass
class SpellCostBreakdown:
    shape_base_w: int
    discipline_multiplier: int
    core_discipline_w: int
    pattern_w: int
    reach_w: int
    persistence_w: int
    target_w: int
    output_mode_premium_w: int
    subtotal_outer_w: int
    hook_mode_multiplier: float
    hook_mode_flat_w: int
    total_w: int
    required_tier: str
    rarity: str


def normalize_token(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def canonicalize(value: str, valid: set[str], aliases: dict[str, str] | None = None) -> str:
    aliases = aliases or {}
    key = normalize_token(value)
    if key in aliases:
        return aliases[key]
    for candidate in valid:
        if normalize_token(candidate) == key:
            return candidate
    raise ValueError(f"Unknown value '{value}'. Allowed: {sorted(valid)}")


def parse_spec(spec_data: dict[str, Any]) -> SpellSpec:
    required = [
        "name",
        "summary",
        "effect_description",
        "hook",
        "mode",
        "shape",
        "discipline",
        "output_mode",
        "pattern",
        "reach",
        "persistence",
        "target_spec",
    ]
    missing = [key for key in required if key not in spec_data]
    if missing:
        raise ValueError(f"Spec missing required keys: {missing}")

    return SpellSpec(
        name=str(spec_data["name"]).strip(),
        summary=str(spec_data["summary"]).strip(),
        effect_description=str(spec_data["effect_description"]).strip(),
        hook=canonicalize(str(spec_data["hook"]), HOOKS),
        mode=canonicalize(str(spec_data["mode"]), MODES),
        shape=canonicalize(str(spec_data["shape"]), set(SHAPES)),
        discipline=canonicalize(str(spec_data["discipline"]), set(DISCIPLINE_MULTIPLIERS)),
        output_mode=canonicalize(str(spec_data["output_mode"]), OUTPUT_MODES),
        pattern=canonicalize(str(spec_data["pattern"]), set(PATTERN_COSTS)),
        reach=canonicalize(str(spec_data["reach"]), set(REACH_COSTS), REACH_ALIASES),
        persistence=canonicalize(
            str(spec_data["persistence"]), set(PERSISTENCE_COSTS), PERSISTENCE_ALIASES
        ),
        target_spec=canonicalize(str(spec_data["target_spec"]), set(TARGET_COSTS)),
        sustained_minutes=int(spec_data.get("sustained_minutes", 0)),
        hook_mode_multiplier=float(spec_data.get("hook_mode_multiplier", 1.0)),
        hook_mode_flat_w=int(spec_data.get("hook_mode_flat_w", 0)),
        notes=str(spec_data.get("notes", "")).strip(),
    )


def output_mode_premium(spec: SpellSpec) -> int:
    natural = NATURAL_OUTPUT_BY_DISCIPLINE[spec.discipline]
    if spec.output_mode == natural:
        return 0

    if spec.output_mode in ADJACENT_OUTPUT_BY_DISCIPLINE[spec.discipline]:
        return 10

    discipline_is_extreme = spec.discipline in {"Mind", "Soul"}
    output_is_extreme = spec.output_mode in {"Neuro", "Soul"}

    if discipline_is_extreme and spec.output_mode in PHYSICAL_OUTPUTS:
        return 60
    if output_is_extreme and spec.discipline not in {"Mind", "Soul"}:
        return 60

    return 30


def persistence_cost(spec: SpellSpec) -> int:
    if spec.persistence != "Sustained":
        return int(PERSISTENCE_COSTS[spec.persistence] or 0)
    if spec.sustained_minutes <= 0:
        raise ValueError("Sustained persistence requires sustained_minutes > 0")
    intervals = max(1, math.ceil(spec.sustained_minutes / 10))
    return intervals * 10


def validate_shape_slots(spec: SpellSpec) -> list[str]:
    non_default_outer = []
    if spec.output_mode != DEFAULTS["output_mode"]:
        non_default_outer.append("output_mode")
    if spec.pattern != DEFAULTS["pattern"]:
        non_default_outer.append("pattern")
    if spec.reach != DEFAULTS["reach"]:
        non_default_outer.append("reach")
    if spec.persistence != DEFAULTS["persistence"]:
        non_default_outer.append("persistence")
    if spec.target_spec != DEFAULTS["target_spec"]:
        non_default_outer.append("target_spec")

    remaining_slots = SHAPES[spec.shape]["outer_slots"] - 1
    if len(non_default_outer) > remaining_slots:
        raise ValueError(
            f"{spec.shape} supports {remaining_slots} non-default outer variables, "
            f"but spec uses {len(non_default_outer)}: {non_default_outer}"
        )
    return non_default_outer


def tier_for_cost(total_w: int) -> str:
    if total_w <= 0:
        return "Invalid"
    if total_w <= 10:
        return "T0"
    if total_w <= 40:
        return "T1"
    if total_w <= 130:
        return "T2"
    if total_w <= 400:
        return "T3"
    if total_w <= 1300:
        return "T4"
    if total_w <= 4000:
        return "T5"
    if total_w <= 13000:
        return "T6"
    if total_w <= 40000:
        return "T7"
    if total_w <= 130000:
        return "T8"
    return "T9"


def rarity_for_tier(tier: str) -> str:
    if tier in {"T0", "T1", "T2"}:
        return "Common"
    if tier in {"T3", "T4"}:
        return "Uncommon"
    if tier in {"T5", "T6"}:
        return "Rare"
    if tier in {"T7", "T8"}:
        return "Legendary"
    if tier == "T9":
        return "Mythic"
    return "Unknown"


def calculate_cost(spec: SpellSpec) -> SpellCostBreakdown:
    validate_shape_slots(spec)

    shape_base = SHAPES[spec.shape]["base_w"]
    multiplier = DISCIPLINE_MULTIPLIERS[spec.discipline]
    core = shape_base * multiplier
    pattern = PATTERN_COSTS[spec.pattern]
    reach = REACH_COSTS[spec.reach]
    persistence = persistence_cost(spec)
    target = TARGET_COSTS[spec.target_spec]
    output = output_mode_premium(spec)

    subtotal = core + pattern + reach + persistence + target + output
    total = int(round((subtotal * spec.hook_mode_multiplier) + spec.hook_mode_flat_w))

    tier = tier_for_cost(total)
    rarity = rarity_for_tier(tier)

    return SpellCostBreakdown(
        shape_base_w=shape_base,
        discipline_multiplier=multiplier,
        core_discipline_w=core,
        pattern_w=pattern,
        reach_w=reach,
        persistence_w=persistence,
        target_w=target,
        output_mode_premium_w=output,
        subtotal_outer_w=subtotal,
        hook_mode_multiplier=spec.hook_mode_multiplier,
        hook_mode_flat_w=spec.hook_mode_flat_w,
        total_w=total,
        required_tier=tier,
        rarity=rarity,
    )


def slugify(name: str) -> str:
    text = re.sub(r"[^\w\s-]", "", name).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def grimoire_row(spec: SpellSpec, breakdown: SpellCostBreakdown) -> str:
    return (
        f"| **{spec.name}** | {spec.shape} | {spec.hook} | {spec.mode} | "
        f"{breakdown.required_tier} | {spec.discipline} | {spec.output_mode} | "
        f"{spec.pattern} | {spec.reach} | {spec.persistence} | {spec.target_spec} |"
    )


def markdown_page(spec: SpellSpec, breakdown: SpellCostBreakdown) -> str:
    sustained_note = ""
    if spec.persistence == "Sustained":
        sustained_note = f" ({spec.sustained_minutes} min planned active window)"

    ai_payload = {
        "name": spec.name,
        "summary": spec.summary,
        "effect_description": spec.effect_description,
        "hook": spec.hook,
        "mode": spec.mode,
        "shape": spec.shape,
        "discipline": spec.discipline,
        "output_mode": spec.output_mode,
        "pattern": spec.pattern,
        "reach": spec.reach,
        "persistence": spec.persistence,
        "target_spec": spec.target_spec,
        "sustained_minutes": spec.sustained_minutes,
        "cost": asdict(breakdown),
        "ai_interpretation_hint": (
            "Use name + summary + effect_description to explain what the spell does in plain language."
        ),
    }

    return f"""# {spec.name}

{spec.summary}

## Effect

{spec.effect_description}

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | {spec.hook} | Center core variable (complexity handled via multiplier/flat) |
| Mode | {spec.mode} | Center core variable (complexity handled via multiplier/flat) |
| Shape | {spec.shape} | Base {breakdown.shape_base_w} W, outer slots {SHAPES[spec.shape]["outer_slots"]} |
| Discipline | {spec.discipline} | x{breakdown.discipline_multiplier} multiplier |
| Output Mode | {spec.output_mode} | +{breakdown.output_mode_premium_w} W premium |
| Pattern | {spec.pattern} | +{breakdown.pattern_w} W |
| Reach | {spec.reach} | +{breakdown.reach_w} W |
| Persistence | {spec.persistence}{sustained_note} | +{breakdown.persistence_w} W |
| Target Spec | {spec.target_spec} | +{breakdown.target_w} W |

## Cost Breakdown

- Core discipline cost: {breakdown.shape_base_w} * {breakdown.discipline_multiplier} = {breakdown.core_discipline_w} W
- Pattern + Reach + Persistence + Target + Output premium:
  {breakdown.pattern_w} + {breakdown.reach_w} + {breakdown.persistence_w} + {breakdown.target_w} + {breakdown.output_mode_premium_w} = {breakdown.pattern_w + breakdown.reach_w + breakdown.persistence_w + breakdown.target_w + breakdown.output_mode_premium_w} W
- Subtotal: {breakdown.subtotal_outer_w} W
- Hook/Mode complexity multiplier: x{breakdown.hook_mode_multiplier}
- Hook/Mode flat addition: +{breakdown.hook_mode_flat_w} W
- Total: **{breakdown.total_w} W**
- Required Control Tier: **{breakdown.required_tier}**
- Rarity bucket: **{breakdown.rarity}**

## All Grimoire Row

{grimoire_row(spec, breakdown)}

## AI Spell Data

```json
{json.dumps(ai_payload, indent=2)}
```

## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
"""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def append_all_grimoire(path: Path, row: str) -> None:
    current = path.read_text(encoding="utf-8")
    if row in current:
        return
    if not current.endswith("\n"):
        current += "\n"
    current += row + "\n"
    path.write_text(current, encoding="utf-8")


def command_create(args: argparse.Namespace) -> int:
    spec_path = Path(args.spec)
    spec_data = json.loads(spec_path.read_text(encoding="utf-8-sig"))
    spec = parse_spec(spec_data)
    breakdown = calculate_cost(spec)

    slug = slugify(spec.name)
    markdown_out = Path(args.markdown_out) if args.markdown_out else Path("content/Spells") / f"{spec.name}.md"
    json_out = (
        Path(args.json_out)
        if args.json_out
        else Path("quartz/static/spell_exports") / f"{slug}.json"
    )
    row_out = (
        Path(args.grimoire_row_out)
        if args.grimoire_row_out
        else Path("quartz/static/spell_exports") / f"{slug}.all_grimoire_row.md"
    )

    md = markdown_page(spec, breakdown)
    row = grimoire_row(spec, breakdown)
    payload = {"spec": asdict(spec), "cost": asdict(breakdown), "all_grimoire_row": row}

    write_text(markdown_out, md)
    write_json(json_out, payload)
    write_text(row_out, row + "\n")

    if args.append_all_grimoire:
        append_all_grimoire(Path(args.append_all_grimoire), row)

    print(f"Created spell: {spec.name}")
    print(f"Total cost: {breakdown.total_w} W ({breakdown.required_tier}, {breakdown.rarity})")
    print(f"Markdown: {markdown_out}")
    print(f"AI JSON: {json_out}")
    print(f"All Grimoire row: {row_out}")
    return 0


def command_schema(_: argparse.Namespace) -> int:
    schema = {
        "name": "Heatshield",
        "summary": "Sustained personal thermal buffering for Zakros transit.",
        "effect_description": (
            "Maintains a stable thermal envelope around the caster to absorb day/night desert swings."
        ),
        "hook": "Ward",
        "mode": "Affect",
        "shape": "Circle",
        "discipline": "Heat",
        "output_mode": "Thermal",
        "pattern": "Sphere",
        "reach": "Self",
        "persistence": "Sustained",
        "target_spec": "Self",
        "sustained_minutes": 30,
        "hook_mode_multiplier": 1.0,
        "hook_mode_flat_w": 0,
        "notes": "Optional freeform notes for designers.",
    }
    print(json.dumps(schema, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create validated Solumora sigil spells.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create = subparsers.add_parser("create", help="Create spell artifacts from a JSON spec.")
    create.add_argument("--spec", required=True, help="Path to spell spec JSON.")
    create.add_argument("--markdown-out", help="Output markdown spell page path.")
    create.add_argument("--json-out", help="Output AI JSON path.")
    create.add_argument(
        "--grimoire-row-out",
        help="Output markdown file containing a single All Grimoire table row.",
    )
    create.add_argument(
        "--append-all-grimoire",
        help="Optional path to All Grimoire markdown file to append row if missing.",
    )
    create.set_defaults(func=command_create)

    schema = subparsers.add_parser("schema", help="Print a spell spec JSON template.")
    schema.set_defaults(func=command_schema)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
