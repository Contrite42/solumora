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

HOOK_COMPLEXITY_MULTIPLIERS = {
    "Emit": 1.0,
    "Shape": 1.2,
    "Bind": 1.6,
    "Ward": 2.0,
    "Trigger": 1.8,
    "Transform": 1.7,
    "Move": 1.5,
    "Sense": 1.8,
    "Filter": 1.6,
    "Amplify": 2.2,
    "Dampen": 1.9,
    "Counter": 2.6,
}

MODE_COMPLEXITY_MULTIPLIERS = {"Create": 1.15, "Affect": 1.0, "Control": 1.35}

SHAPE_CONTROL_SURFACE = {
    "Triangle": ("discipline", "output_mode", "pattern"),
    "Square": ("discipline", "output_mode", "pattern", "target_spec"),
    "Pentagon": ("discipline", "output_mode", "pattern", "target_spec", "reach"),
    "Circle": ("discipline", "output_mode", "pattern", "target_spec", "reach", "persistence"),
}

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


def explicit_outer_variables(shape: str) -> tuple[str, ...]:
    return SHAPE_CONTROL_SURFACE[shape]


def default_hook_mode_multiplier(hook: str, mode: str) -> float:
    return HOOK_COMPLEXITY_MULTIPLIERS[hook] * MODE_COMPLEXITY_MULTIPLIERS[mode]


def parse_spec(spec_data: dict[str, Any]) -> SpellSpec:
    required = ["name", "summary", "effect_description", "hook", "mode", "shape", "discipline"]
    missing = [key for key in required if key not in spec_data]
    if missing:
        raise ValueError(f"Spec missing required keys: {missing}")

    hook = canonicalize(str(spec_data["hook"]), HOOKS)
    mode = canonicalize(str(spec_data["mode"]), MODES)
    shape = canonicalize(str(spec_data["shape"]), set(SHAPES))
    discipline = canonicalize(str(spec_data["discipline"]), set(DISCIPLINE_MULTIPLIERS))
    hook_mode_multiplier = (
        float(spec_data["hook_mode_multiplier"])
        if "hook_mode_multiplier" in spec_data
        else default_hook_mode_multiplier(hook, mode)
    )

    return SpellSpec(
        name=str(spec_data["name"]).strip(),
        summary=str(spec_data["summary"]).strip(),
        effect_description=str(spec_data["effect_description"]).strip(),
        hook=hook,
        mode=mode,
        shape=shape,
        discipline=discipline,
        output_mode=canonicalize(
            str(spec_data.get("output_mode", DEFAULTS["output_mode"])), OUTPUT_MODES
        ),
        pattern=canonicalize(str(spec_data.get("pattern", DEFAULTS["pattern"])), set(PATTERN_COSTS)),
        reach=canonicalize(
            str(spec_data.get("reach", DEFAULTS["reach"])), set(REACH_COSTS), REACH_ALIASES
        ),
        persistence=canonicalize(
            str(spec_data.get("persistence", DEFAULTS["persistence"])),
            set(PERSISTENCE_COSTS),
            PERSISTENCE_ALIASES,
        ),
        target_spec=canonicalize(
            str(spec_data.get("target_spec", DEFAULTS["target_spec"])), set(TARGET_COSTS)
        ),
        sustained_minutes=int(spec_data.get("sustained_minutes", 0)),
        hook_mode_multiplier=hook_mode_multiplier,
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
    explicit = set(explicit_outer_variables(spec.shape))
    blocked_values = {
        "output_mode": spec.output_mode,
        "pattern": spec.pattern,
        "target_spec": spec.target_spec,
        "reach": spec.reach,
        "persistence": spec.persistence,
    }
    blocked_defaults = {
        "output_mode": DEFAULTS["output_mode"],
        "pattern": DEFAULTS["pattern"],
        "target_spec": DEFAULTS["target_spec"],
        "reach": DEFAULTS["reach"],
        "persistence": DEFAULTS["persistence"],
    }

    for key, value in blocked_values.items():
        if key in explicit:
            continue
        if value != blocked_defaults[key]:
            raise ValueError(
                f"{spec.shape} does not expose '{key}' for explicit assignment. "
                f"Use default '{blocked_defaults[key]}' or choose a higher-control shape."
            )

    if "persistence" not in explicit and spec.sustained_minutes > 0:
        raise ValueError(
            f"{spec.shape} does not expose persistence, so sustained_minutes must be 0."
        )

    assigned_explicit = []
    for key in explicit:
        if key == "discipline":
            assigned_explicit.append(key)
            continue
        if blocked_values.get(key) != blocked_defaults.get(key):
            assigned_explicit.append(key)
    return sorted(assigned_explicit)


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

    explicit = explicit_outer_variables(spec.shape)
    implied_defaults = []
    for key in ["output_mode", "pattern", "target_spec", "reach", "persistence"]:
        if key in explicit:
            continue
        implied_defaults.append(f"{key}={DEFAULTS[key]}")

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

- Shape control surface: {spec.shape} explicit outer variables = {", ".join(explicit)}
- Shape implied defaults: {", ".join(implied_defaults) if implied_defaults else "(none)"}
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
    if not path.exists():
        write_text(path, row + "\n")
        return
    current = path.read_text(encoding="utf-8")
    if row in current:
        return
    if not current.endswith("\n"):
        current += "\n"
    current += row + "\n"
    path.write_text(current, encoding="utf-8")


def comma_list(values: list[str]) -> str:
    return ", ".join(values)


def prompt_text(label: str, default: str | None = None, required: bool = True) -> str:
    while True:
        prompt = f"{label}"
        if default not in {None, ""}:
            prompt += f" [{default}]"
        prompt += ": "
        raw = input(prompt).strip()
        if raw:
            return raw
        if default not in {None, ""}:
            return str(default)
        if not required:
            return ""
        print("Value is required.")


def prompt_choice(
    label: str, options: list[str], default: str | None = None, aliases: dict[str, str] | None = None
) -> str:
    while True:
        print(f"{label} options: {comma_list(options)}")
        raw = prompt_text(label, default=default, required=True)
        try:
            return canonicalize(raw, set(options), aliases)
        except ValueError as exc:
            print(exc)


def prompt_int(label: str, default: int = 0, min_value: int | None = None) -> int:
    while True:
        raw = prompt_text(label, default=str(default), required=True)
        try:
            value = int(raw)
        except ValueError:
            print("Enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Enter a value >= {min_value}.")
            continue
        return value


def prompt_float(label: str, default: float = 1.0, min_value: float | None = None) -> float:
    while True:
        raw = prompt_text(label, default=str(default), required=True)
        try:
            value = float(raw)
        except ValueError:
            print("Enter a number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Enter a value >= {min_value}.")
            continue
        return value


def collect_spec_interactive() -> SpellSpec:
    print("Guided spell creation. Press Enter to accept defaults.\n")
    shape_options = sorted(SHAPES)
    discipline_options = sorted(DISCIPLINE_MULTIPLIERS)
    hook_options = sorted(HOOKS)
    mode_options = sorted(MODES)
    output_options = sorted(OUTPUT_MODES)
    pattern_options = sorted(PATTERN_COSTS)
    reach_options = sorted(REACH_COSTS)
    persistence_options = sorted(PERSISTENCE_COSTS)
    target_options = sorted(TARGET_COSTS)

    draft: dict[str, Any] = {
        "name": "",
        "summary": "",
        "effect_description": "",
        "hook": "Ward",
        "mode": "Affect",
        "shape": "Triangle",
        "discipline": "Raw",
        "output_mode": DEFAULTS["output_mode"],
        "pattern": DEFAULTS["pattern"],
        "reach": DEFAULTS["reach"],
        "persistence": DEFAULTS["persistence"],
        "target_spec": DEFAULTS["target_spec"],
        "sustained_minutes": 0,
        "hook_mode_multiplier": default_hook_mode_multiplier("Ward", "Affect"),
        "hook_mode_flat_w": 0,
        "notes": "",
    }

    while True:
        draft["name"] = prompt_text("Spell name", default=draft["name"])
        draft["summary"] = prompt_text("Short summary", default=draft["summary"])
        draft["effect_description"] = prompt_text(
            "Effect description", default=draft["effect_description"]
        )
        draft["hook"] = prompt_choice("Hook", hook_options, default=draft["hook"])
        draft["mode"] = prompt_choice("Mode", mode_options, default=draft["mode"])
        draft["shape"] = prompt_choice("Shape", shape_options, default=draft["shape"])
        explicit = set(explicit_outer_variables(draft["shape"]))
        print(
            "Shape control surface explicit vars: "
            + ", ".join(explicit_outer_variables(draft["shape"]))
        )
        draft["discipline"] = prompt_choice(
            "Discipline", discipline_options, default=draft["discipline"]
        )
        draft["output_mode"] = prompt_choice("Output mode", output_options, default=draft["output_mode"])
        draft["pattern"] = prompt_choice("Pattern", pattern_options, default=draft["pattern"])

        if "target_spec" in explicit:
            draft["target_spec"] = prompt_choice(
                "Target spec", target_options, default=draft["target_spec"]
            )
        else:
            draft["target_spec"] = DEFAULTS["target_spec"]

        if "reach" in explicit:
            draft["reach"] = prompt_choice(
                "Reach", reach_options, default=draft["reach"], aliases=REACH_ALIASES
            )
        else:
            draft["reach"] = DEFAULTS["reach"]

        if "persistence" in explicit:
            draft["persistence"] = prompt_choice(
                "Persistence",
                persistence_options,
                default=draft["persistence"],
                aliases=PERSISTENCE_ALIASES,
            )
        else:
            draft["persistence"] = DEFAULTS["persistence"]

        if draft["persistence"] == "Sustained" and "persistence" in explicit:
            draft["sustained_minutes"] = prompt_int(
                "Sustained minutes (active window)",
                default=max(10, draft["sustained_minutes"]),
                min_value=1,
            )
        else:
            draft["sustained_minutes"] = 0

        suggested_multiplier = default_hook_mode_multiplier(draft["hook"], draft["mode"])
        print(
            f"Suggested hook/mode multiplier from full-system table: {suggested_multiplier:.2f}"
        )
        draft["hook_mode_multiplier"] = prompt_float(
            "Hook/mode multiplier",
            default=float(suggested_multiplier),
            min_value=0.0,
        )
        draft["hook_mode_flat_w"] = prompt_int(
            "Hook/mode flat Watts addition", default=int(draft["hook_mode_flat_w"])
        )
        draft["notes"] = prompt_text("Design notes (optional)", default=draft["notes"], required=False)

        try:
            spec = parse_spec(draft)
            calculate_cost(spec)
            return spec
        except ValueError as exc:
            print(f"\nValidation issue: {exc}")
            print("Adjust inputs and try again.\n")


def resolve_output_paths(args: argparse.Namespace, spec: SpellSpec) -> tuple[Path, Path, Path]:
    slug = slugify(spec.name)
    markdown_out = (
        Path(args.markdown_out) if args.markdown_out else Path("content/Spells") / f"{spec.name}.md"
    )
    json_out = (
        Path(args.json_out) if args.json_out else Path("quartz/static/spell_exports") / f"{slug}.json"
    )
    row_out = (
        Path(args.grimoire_row_out)
        if args.grimoire_row_out
        else Path("quartz/static/spell_exports") / f"{slug}.all_grimoire_row.md"
    )
    return markdown_out, json_out, row_out


def emit_artifacts(spec: SpellSpec, args: argparse.Namespace) -> SpellCostBreakdown:
    breakdown = calculate_cost(spec)
    markdown_out, json_out, row_out = resolve_output_paths(args, spec)

    md = markdown_page(spec, breakdown)
    row = grimoire_row(spec, breakdown)
    payload = {"spec": asdict(spec), "cost": asdict(breakdown), "all_grimoire_row": row}

    write_text(markdown_out, md)
    write_json(json_out, payload)
    write_text(row_out, row + "\n")

    if getattr(args, "save_spec_out", None):
        write_json(Path(args.save_spec_out), asdict(spec))

    if getattr(args, "append_all_grimoire", None):
        append_all_grimoire(Path(args.append_all_grimoire), row)

    print(f"Created spell: {spec.name}")
    print(f"Total cost: {breakdown.total_w} W ({breakdown.required_tier}, {breakdown.rarity})")
    print(f"Markdown: {markdown_out}")
    print(f"AI JSON: {json_out}")
    print(f"All Grimoire row: {row_out}")
    if getattr(args, "save_spec_out", None):
        print(f"Saved input spec: {Path(args.save_spec_out)}")
    return breakdown


def command_create(args: argparse.Namespace) -> int:
    try:
        spec_path = Path(args.spec)
        if not spec_path.exists():
            raise FileNotFoundError(f"Spec file not found: {spec_path}")
        spec_data = json.loads(spec_path.read_text(encoding="utf-8-sig"))
        spec = parse_spec(spec_data)
        emit_artifacts(spec, args)
    except FileNotFoundError as exc:
        print(exc)
        return 1
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in '{args.spec}': {exc}")
        return 1
    except ValueError as exc:
        print(f"Spec validation failed: {exc}")
        return 1
    return 0


def command_interactive(args: argparse.Namespace) -> int:
    try:
        spec = collect_spec_interactive()
        emit_artifacts(spec, args)
    except KeyboardInterrupt:
        print("\nCancelled.")
        return 130
    except ValueError as exc:
        print(f"Could not create spell: {exc}")
        return 1
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
    parser = argparse.ArgumentParser(
        description=(
            "Create validated Solumora sigil spells. "
            "Run with no command to launch guided interactive mode."
        )
    )
    subparsers = parser.add_subparsers(dest="command")

    def add_output_args(command_parser: argparse.ArgumentParser) -> None:
        command_parser.add_argument("--markdown-out", help="Output markdown spell page path.")
        command_parser.add_argument("--json-out", help="Output AI JSON path.")
        command_parser.add_argument(
            "--grimoire-row-out",
            help="Output markdown file containing a single All Grimoire table row.",
        )
        command_parser.add_argument(
            "--append-all-grimoire",
            help="Optional path to All Grimoire markdown file to append row if missing.",
        )
        command_parser.add_argument(
            "--save-spec-out",
            help="Optional path to save the final normalized input spec JSON.",
        )

    create = subparsers.add_parser("create", help="Create spell artifacts from a JSON spec.")
    create.add_argument("--spec", required=True, help="Path to spell spec JSON.")
    add_output_args(create)
    create.set_defaults(func=command_create)

    interactive = subparsers.add_parser(
        "interactive",
        help="Guided prompt flow for creating a spell without writing JSON manually.",
    )
    add_output_args(interactive)
    interactive.set_defaults(func=command_interactive)

    schema = subparsers.add_parser("schema", help="Print a spell spec JSON template.")
    schema.set_defaults(func=command_schema)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, "func"):
        print("No command provided. Starting guided interactive mode.\n")
        interactive_args = argparse.Namespace(
            markdown_out=None,
            json_out=None,
            grimoire_row_out=None,
            append_all_grimoire=None,
            save_spec_out=None,
        )
        return command_interactive(interactive_args)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
