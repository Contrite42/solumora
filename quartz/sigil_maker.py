#!/usr/bin/env python3
"""
Sigil Maker for Solumora spell design.

Creates validated spell definitions from a JSON spec, calculates Watts cost from
canon rules, and exports AI-readable spell data plus markdown compatible with
grimoire pages.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import itertools
import json
import math
import re
import shutil
import subprocess
import threading
from dataclasses import asdict, dataclass
from datetime import datetime
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

TIER_OVERVIEW = [
    {"tier": "T0", "range": "1-10W", "tagline": "A flicker"},
    {"tier": "T1", "range": "11-40W", "tagline": "A candle"},
    {"tier": "T2", "range": "41-130W", "tagline": "A tool"},
    {"tier": "T3", "range": "131-400W", "tagline": "A weapon"},
    {"tier": "T4", "range": "401-1300W", "tagline": "A violation"},
    {"tier": "T5", "range": "1301-4000W", "tagline": "A marker"},
    {"tier": "T6", "range": "4001-13000W", "tagline": "A power act"},
    {"tier": "T7", "range": "13001-40000W", "tagline": "A rupture"},
    {"tier": "T8", "range": "40001-130000W", "tagline": "A catastrophe"},
    {"tier": "T9", "range": "130001W+", "tagline": "The architecture"},
]

RARITY_TO_GRIMOIRE_PAGE = {
    "Common": "Common Grimoire.md",
    "Uncommon": "Uncommon Grimoire.md",
    "Rare": "Rare Grimoire.md",
    "Legendary": "Legendary Grimoire.md",
    "Mythic": "Mythic Grimoire.md",
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

TIER_SEQUENCE = tuple(row["tier"] for row in TIER_OVERVIEW)

AUTO_DISCIPLINES = tuple(sorted(DISCIPLINE_MULTIPLIERS.keys()))

AUTO_INTERNAL_DIR_NAMES = {"_processed", "_failed", "_generated"}

AUTO_HOOK_VERBS = {
    "Emit": "releases",
    "Shape": "refines",
    "Bind": "anchors",
    "Ward": "establishes",
    "Trigger": "arms",
    "Transform": "reconfigures",
    "Move": "repositions",
    "Sense": "detects",
    "Filter": "screens",
    "Amplify": "boosts",
    "Dampen": "reduces",
    "Counter": "disrupts",
}

AUTO_MODE_PHRASES = {
    "Create": "by creating a fresh flux expression",
    "Affect": "by changing existing conditions",
    "Control": "with active regulation while it runs",
}

AUTO_PATTERN_TERMS = {
    "Point": "point focus",
    "Plane": "planar spread",
    "Beam": "directed line",
    "Cone": "fan spread",
    "Ring": "ring perimeter",
    "Cylinder": "column volume",
    "Sphere": "spherical envelope",
    "Field": "field volume",
}

AUTO_TARGET_TERMS = {
    "Where Written": "the inscribed anchor",
    "Self": "the caster",
    "Object": "one object",
    "Surface": "a prepared surface",
    "Individual": "one individual",
    "Marked": "a marked signature",
    "Group": "a grouped cluster",
    "Filter": "a filtered selection",
}

AUTO_PERSISTENCE_TERMS = {
    "Immediate": "immediate discharge",
    "Timed Short": "short timed hold",
    "Timed Long": "long timed hold",
    "Sustained": "sustained channeling",
    "Conditional": "conditional hold",
    "Latched": "latched hold",
    "Permanent": "permanent inscription",
}

AUTO_STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "it",
    "of",
    "on",
    "or",
    "the",
    "to",
    "while",
    "with",
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


def tier_index(tier: str) -> int:
    try:
        return TIER_SEQUENCE.index(tier)
    except ValueError:
        return len(TIER_SEQUENCE)


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


def markdown_page(
    spec: SpellSpec,
    breakdown: SpellCostBreakdown,
    ollama_interpretation: str | None = None,
) -> str:
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
    if ollama_interpretation:
        ai_payload["ollama_interpretation"] = ollama_interpretation

    interpretation_block = ""
    if ollama_interpretation:
        interpretation_block = f"""
## Ollama Interpretation

{ollama_interpretation}
"""

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
{interpretation_block}

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


def validate_rarity_alignment(breakdown: SpellCostBreakdown) -> None:
    expected = rarity_for_tier(breakdown.required_tier)
    if expected != breakdown.rarity:
        raise ValueError(
            f"Tier/rarity mismatch: tier {breakdown.required_tier} expects {expected}, "
            f"got {breakdown.rarity}"
        )


def rarity_page_entry(spec: SpellSpec, breakdown: SpellCostBreakdown) -> str:
    return (
        f"---\n\n"
        f"**{spec.name}**\n"
        f"{spec.summary}\n"
        f"| Variable | Value |\n"
        f"|---|---|\n"
        f"| Shape | {spec.shape} |\n"
        f"| Hook | {spec.hook} |\n"
        f"| Mode | {spec.mode} |\n"
        f"| Control Tier | {breakdown.required_tier} |\n"
        f"| Rarity | {breakdown.rarity} |\n"
        f"| Watts | {breakdown.total_w} W |\n"
        f"| Discipline | {spec.discipline} |\n"
        f"| Output | {spec.output_mode} |\n"
        f"| Pattern | {spec.pattern} |\n"
        f"| Reach | {spec.reach} |\n"
        f"| Persistence | {spec.persistence} |\n"
        f"| Target | {spec.target_spec} |\n"
        f"| Spell Page | [[Spells/{spec.name}|{spec.name}]] |\n"
    )


def append_rarity_page(
    rarity_pages_dir: Path, spec: SpellSpec, breakdown: SpellCostBreakdown
) -> Path | None:
    page_name = RARITY_TO_GRIMOIRE_PAGE.get(breakdown.rarity)
    if page_name is None:
        return None
    page_path = rarity_pages_dir / page_name
    marker = f"**{spec.name}**"
    entry = rarity_page_entry(spec, breakdown)

    if not page_path.exists():
        seed = (
            f"{breakdown.rarity} spells generated by Sigil Maker.\n\n"
            f"*Return to [[All Grimoire]]*\n\n"
            f"{entry}\n"
        )
        write_text(page_path, seed)
        return page_path

    current = page_path.read_text(encoding="utf-8")
    if marker in current:
        return page_path

    if not current.endswith("\n"):
        current += "\n"
    current += "\n" + entry + "\n"
    page_path.write_text(current, encoding="utf-8")
    return page_path


def append_spells_hub(path: Path, spec: SpellSpec, breakdown: SpellCostBreakdown) -> None:
    heading = "## Sigil Maker Generated Spells"
    link_token = f"[[Spells/{spec.name}|{spec.name}]]"
    line = f"- {link_token} - {breakdown.total_w} W - {breakdown.required_tier} ({breakdown.rarity})"

    if not path.exists():
        write_text(path, f"{heading}\n\n{line}\n")
        return

    current = path.read_text(encoding="utf-8")
    if link_token in current:
        return

    if heading not in current:
        if not current.endswith("\n"):
            current += "\n"
        current += f"\n{heading}\n\n{line}\n"
        path.write_text(current, encoding="utf-8")
        return

    # Insert at end of generated section if present, else append after heading.
    idx = current.find(heading)
    section = current[idx:]
    next_heading = section.find("\n## ", len(heading))
    if next_heading == -1:
        insertion_point = len(current)
    else:
        insertion_point = idx + next_heading

    prefix = current[:insertion_point]
    suffix = current[insertion_point:]
    if not prefix.endswith("\n"):
        prefix += "\n"
    prefix += line + "\n"
    path.write_text(prefix + suffix, encoding="utf-8")


def sync_spell_indexes(
    spec: SpellSpec,
    breakdown: SpellCostBreakdown,
    *,
    all_grimoire_path: Path,
    rarity_pages_dir: Path,
    spells_hub_path: Path | None = None,
) -> tuple[Path, Path | None, Path | None]:
    validate_rarity_alignment(breakdown)
    row = grimoire_row(spec, breakdown)
    append_all_grimoire(all_grimoire_path, row)
    rarity_page = append_rarity_page(rarity_pages_dir, spec, breakdown)
    if spells_hub_path is not None:
        append_spells_hub(spells_hub_path, spec, breakdown)
    return all_grimoire_path, rarity_page, spells_hub_path


def relative_subpath(path: Path, root: Path) -> Path:
    try:
        return path.relative_to(root)
    except ValueError:
        return Path(path.name)


def extract_json_object(text: str) -> dict[str, Any] | None:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    candidate = text[start : end + 1]
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    if not isinstance(parsed, dict):
        return None
    return parsed


def resolve_ollama_model(model: str, timeout_seconds: int = 20) -> str:
    requested = model.strip()
    if not requested:
        return ""
    try:
        process = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        print(f"[OLLAMA] Runtime unavailable, skipping Ollama model '{requested}'.")
        return ""
    if process.returncode != 0:
        print(f"[OLLAMA] Could not query models, skipping '{requested}'.")
        return ""
    if requested not in process.stdout:
        print(f"[OLLAMA] Model '{requested}' not found locally, using deterministic generator.")
        return ""
    return requested


def enrich_generated_spec_with_ollama(
    spec_data: dict[str, Any], *, model: str, timeout_seconds: int
) -> dict[str, Any]:
    prompt = (
        "You are naming a practical Solumora spell. Return JSON only with keys "
        '"name", "summary", "effect_description". '
        "Summary must be one sentence. Name must be derived from words in the summary. "
        "Keep the output grounded and functional, no lore backstory. "
        f"Use these sigil variables: {json.dumps(spec_data, ensure_ascii=True)}"
    )
    process = subprocess.run(
        ["ollama", "run", model, prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )
    if process.returncode != 0:
        raise ValueError(process.stderr.strip() or process.stdout.strip() or "ollama run failed")
    payload = extract_json_object(process.stdout.strip())
    if payload is None:
        raise ValueError("Ollama response did not include a valid JSON object.")

    updated = dict(spec_data)
    for key in ("name", "summary", "effect_description"):
        value = str(payload.get(key, "")).strip()
        if value:
            updated[key] = value
    return updated


def interpret_spell_with_ollama(
    spec: SpellSpec,
    breakdown: SpellCostBreakdown,
    *,
    model: str,
    timeout_seconds: int,
) -> str:
    spell_packet = {"spec": asdict(spec), "cost": asdict(breakdown)}
    prompt = (
        "Interpret this Solumora sigil as a practical spell note. "
        "State what it does, likely use, and one operational constraint. "
        "Keep it concise (max 120 words), plain text only.\n"
        f"{json.dumps(spell_packet, ensure_ascii=True)}"
    )
    process = subprocess.run(
        ["ollama", "run", model, prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )
    if process.returncode != 0:
        raise ValueError(process.stderr.strip() or process.stdout.strip() or "ollama run failed")
    content = process.stdout.strip().replace("```", "").strip()
    if not content:
        raise ValueError("Ollama returned an empty interpretation.")
    return content


def collect_existing_spell_names(markdown_dir: Path, all_grimoire_path: Path) -> set[str]:
    names: set[str] = set()

    if markdown_dir.exists():
        for page in markdown_dir.rglob("*.md"):
            if page.is_file():
                names.add(page.stem.strip())

    if all_grimoire_path.exists():
        for line in all_grimoire_path.read_text(encoding="utf-8").splitlines():
            match = re.search(r"\|\s*\*\*(.+?)\*\*\s*\|", line)
            if match:
                names.add(match.group(1).strip())

    return {name for name in names if name}


def titleize_token(token: str) -> str:
    lower = token.lower()
    if lower in {"of", "and", "for", "the"}:
        return lower
    return lower.capitalize()


def output_candidates_for_discipline(discipline: str) -> list[str]:
    natural = NATURAL_OUTPUT_BY_DISCIPLINE[discipline]
    adjacent = sorted(ADJACENT_OUTPUT_BY_DISCIPLINE.get(discipline, set()))
    pool = [natural] + adjacent
    for candidate in sorted(OUTPUT_MODES):
        if candidate not in pool:
            pool.append(candidate)
    return pool


def recipe_summary_from_variables(spec_data: dict[str, Any]) -> str:
    hook = str(spec_data["hook"])
    mode = str(spec_data["mode"])
    discipline = str(spec_data["discipline"])
    output_mode = str(spec_data["output_mode"]).lower()
    pattern = AUTO_PATTERN_TERMS.get(str(spec_data["pattern"]), str(spec_data["pattern"]).lower())
    reach = str(spec_data["reach"]).lower()
    target = AUTO_TARGET_TERMS.get(
        str(spec_data["target_spec"]), str(spec_data["target_spec"]).lower()
    )
    persistence = AUTO_PERSISTENCE_TERMS.get(
        str(spec_data["persistence"]), str(spec_data["persistence"]).lower()
    )
    hook_verb = AUTO_HOOK_VERBS.get(hook, "applies")
    mode_phrase = AUTO_MODE_PHRASES.get(mode, "while preserving structure")
    flux_phrase = f"{discipline.lower()} {output_mode} flux"
    if discipline.lower() == output_mode:
        flux_phrase = f"{discipline.lower()} flux"
    return (
        f"{hook_verb.capitalize()} {flux_phrase} as a {pattern} at {reach} reach, "
        f"targeting {target} with {persistence} {mode_phrase}."
    )


def recipe_effect_from_variables(spec_data: dict[str, Any]) -> str:
    shape = str(spec_data["shape"])
    hook = str(spec_data["hook"]).lower()
    mode = str(spec_data["mode"]).lower()
    discipline = str(spec_data["discipline"]).lower()
    output_mode = str(spec_data["output_mode"]).lower()
    pattern = str(spec_data["pattern"]).lower()
    target = str(spec_data["target_spec"]).lower()
    reach = str(spec_data["reach"]).lower()
    persistence = str(spec_data["persistence"]).lower()
    sustained = int(spec_data.get("sustained_minutes", 0))
    sustained_tail = ""
    if persistence == "sustained":
        sustained_tail = f" The sustained window is set to {max(1, sustained)} minutes."
    return (
        f"A {shape.lower()} {hook}/{mode} recipe that channels {discipline} discipline into {output_mode} output. "
        f"It applies a {pattern} pattern against {target} across {reach} reach with {persistence} persistence."
        f"{sustained_tail}"
    )


def derive_name_from_summary(summary: str, spec_data: dict[str, Any]) -> str:
    tokens = [token for token in re.findall(r"[A-Za-z]+", summary) if token.lower() not in AUTO_STOPWORDS]
    preferred = [
        str(spec_data.get("discipline", "")),
        str(spec_data.get("hook", "")),
        str(spec_data.get("pattern", "")),
        str(spec_data.get("output_mode", "")),
    ]
    name_tokens: list[str] = []
    for token in preferred:
        clean = re.sub(r"[^A-Za-z]", "", token).strip()
        if clean and clean.lower() not in {value.lower() for value in name_tokens}:
            name_tokens.append(clean)
        if len(name_tokens) >= 3:
            break
    if len(name_tokens) < 3:
        for token in tokens:
            if token.lower() in {value.lower() for value in name_tokens}:
                continue
            name_tokens.append(titleize_token(token))
            if len(name_tokens) >= 3:
                break
    if len(name_tokens) < 2:
        name_tokens.extend(["Flux", "Working"])
    return " ".join(name_tokens[:3]).strip()


def ensure_unique_name(base_name: str, reserved_names: set[str]) -> str:
    candidate = base_name.strip() or "Flux Working"
    if candidate not in reserved_names:
        return candidate
    counter = 2
    while True:
        trial = f"{candidate} {counter}"
        if trial not in reserved_names:
            return trial
        counter += 1


def iter_auto_recipe_dicts():
    shapes = ("Triangle", "Square", "Pentagon", "Circle")
    hooks = sorted(HOOKS)
    modes = sorted(MODES)
    disciplines = AUTO_DISCIPLINES
    patterns = sorted(PATTERN_COSTS.keys())
    targets = sorted(TARGET_COSTS.keys())
    reaches = sorted(REACH_COSTS.keys())
    persistences = [
        "Immediate",
        "Timed Short",
        "Timed Long",
        "Sustained",
        "Conditional",
        "Latched",
        "Permanent",
    ]

    for shape, hook, mode, discipline in itertools.product(shapes, hooks, modes, disciplines):
        explicit = set(explicit_outer_variables(shape))
        output_options = output_candidates_for_discipline(discipline)
        pattern_options = patterns if "pattern" in explicit else [DEFAULTS["pattern"]]
        target_options = targets if "target_spec" in explicit else [DEFAULTS["target_spec"]]
        reach_options = reaches if "reach" in explicit else [DEFAULTS["reach"]]
        persistence_options = (
            persistences if "persistence" in explicit else [DEFAULTS["persistence"]]
        )

        for (
            output_mode,
            pattern,
            target_spec,
            reach,
            persistence,
        ) in itertools.product(
            output_options,
            pattern_options,
            target_options,
            reach_options,
            persistence_options,
        ):
            sustained_minutes = 0
            if persistence == "Sustained":
                sustained_minutes = 20
            yield {
                "hook": hook,
                "mode": mode,
                "shape": shape,
                "discipline": discipline,
                "output_mode": output_mode,
                "pattern": pattern,
                "reach": reach,
                "persistence": persistence,
                "target_spec": target_spec,
                "sustained_minutes": sustained_minutes,
                "hook_mode_multiplier": default_hook_mode_multiplier(hook, mode),
                "hook_mode_flat_w": 0,
                "notes": "Generated automatically from sigil variable synthesis.",
            }


def generate_auto_specs(
    *,
    count: int,
    existing_names: set[str],
    min_tier: str,
    max_tier: str,
    ollama_model: str | None = None,
    ollama_timeout_seconds: int = 90,
) -> list[SpellSpec]:
    if count <= 0:
        return []

    min_idx = tier_index(min_tier)
    max_idx = tier_index(max_tier)
    if min_idx > max_idx:
        raise ValueError(f"min_tier ({min_tier}) must be <= max_tier ({max_tier}).")

    generated: list[SpellSpec] = []
    reserved_names = set(existing_names)
    recipes = iter_auto_recipe_dicts()

    for recipe in recipes:
        base_spec_data = dict(recipe)
        base_summary = recipe_summary_from_variables(base_spec_data)
        base_name = derive_name_from_summary(base_summary, base_spec_data)
        base_name = ensure_unique_name(base_name, reserved_names)
        base_spec_data["summary"] = base_summary
        base_spec_data["effect_description"] = recipe_effect_from_variables(base_spec_data)
        base_spec_data["name"] = base_name

        candidate_data = dict(base_spec_data)

        if ollama_model:
            try:
                candidate_data = enrich_generated_spec_with_ollama(
                    candidate_data,
                    model=ollama_model,
                    timeout_seconds=ollama_timeout_seconds,
                )
            except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
                print(f"[OLLAMA] Using deterministic recipe text for '{base_name}': {exc}")

        candidate_name = ensure_unique_name(
            str(candidate_data.get("name", "")).strip() or base_name,
            reserved_names,
        )
        candidate_data["name"] = candidate_name

        try:
            spec = parse_spec(candidate_data)
            breakdown = calculate_cost(spec)
        except ValueError:
            continue

        idx = tier_index(breakdown.required_tier)
        if idx < min_idx or idx > max_idx:
            continue

        if spec.name in reserved_names:
            continue
        reserved_names.add(spec.name)
        generated.append(spec)
        if len(generated) >= count:
            return generated

    return generated


def discover_spec_files(spec_dir: Path, pattern: str, recursive: bool) -> list[Path]:
    iterator = spec_dir.rglob(pattern) if recursive else spec_dir.glob(pattern)
    files: list[Path] = []
    for path in iterator:
        if not path.is_file():
            continue
        relative = relative_subpath(path, spec_dir)
        if any(part in AUTO_INTERNAL_DIR_NAMES for part in relative.parts):
            continue
        files.append(path)
    return sorted(files)


def archive_spec_file(spec_path: Path, *, spec_root: Path, archive_root: Path, run_stamp: str) -> Path:
    relative = relative_subpath(spec_path, spec_root)
    destination = archive_root / run_stamp / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        destination = destination.with_name(
            f"{destination.stem}.{datetime.now().strftime('%H%M%S%f')}{destination.suffix}"
        )
    shutil.move(str(spec_path), str(destination))
    return destination


def save_generated_spec(spec: SpellSpec, output_dir: Path, run_stamp: str) -> Path:
    path = output_dir / run_stamp / f"{slugify(spec.name)}.json"
    write_json(path, asdict(spec))
    return path


def command_auto(args: argparse.Namespace) -> int:
    run_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    spec_dir = Path(args.spec_dir)
    spec_dir.mkdir(parents=True, exist_ok=True)

    print("Auto pipeline started.")
    print(f"- Queue directory: {spec_dir}")
    print(f"- Recursive queue scan: {not args.no_recursive}")
    print(f"- Auto generation target: {args.generate_count} spells")
    print(f"- Tier window: {args.min_tier} to {args.max_tier}")
    resolved_ollama_model = resolve_ollama_model(
        str(getattr(args, "ollama_model", "") or ""),
        timeout_seconds=max(5, int(getattr(args, "ollama_timeout_seconds", 20))),
    )
    args.ollama_model = resolved_ollama_model
    if resolved_ollama_model:
        print(f"- Ollama model: {resolved_ollama_model}")
    else:
        print("- Ollama model: disabled (deterministic naming/summaries active)")

    queue_files = discover_spec_files(spec_dir, args.spec_glob, recursive=not args.no_recursive)
    print(f"- Queue files discovered: {len(queue_files)}")

    queue_success = 0
    queue_fail = 0
    generated_success = 0
    generated_fail = 0
    fail_fast_triggered = False

    for spec_path in queue_files:
        print(f"\n[QUEUE] {spec_path}")
        try:
            spec = load_spec(spec_path)
            emit_artifacts(spec, args)
            queue_success += 1
            if args.archive_queue:
                archived = archive_spec_file(
                    spec_path,
                    spec_root=spec_dir,
                    archive_root=Path(args.processed_dir),
                    run_stamp=run_stamp,
                )
                print(f"Archived queue spec: {archived}")
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
            queue_fail += 1
            print(f"[FAIL] {spec_path}: {exc}")
            if args.archive_queue:
                archived = archive_spec_file(
                    spec_path,
                    spec_root=spec_dir,
                    archive_root=Path(args.failed_dir),
                    run_stamp=run_stamp,
                )
                error_note = archived.with_suffix(archived.suffix + ".error.txt")
                write_text(error_note, str(exc).strip() + "\n")
                print(f"Archived failed spec: {archived}")
            if args.fail_fast:
                fail_fast_triggered = True
                break

    if not args.skip_generation and args.generate_count > 0 and not fail_fast_triggered:
        existing = collect_existing_spell_names(
            Path(getattr(args, "markdown_dir", "content/Spells")),
            Path(getattr(args, "all_grimoire_path", "content/All Grimoire.md")),
        )
        try:
            generated_specs = generate_auto_specs(
                count=int(args.generate_count),
                existing_names=existing,
                min_tier=args.min_tier,
                max_tier=args.max_tier,
                ollama_model=(resolved_ollama_model or "").strip() or None,
                ollama_timeout_seconds=int(args.ollama_timeout_seconds),
            )
        except ValueError as exc:
            print(f"[AUTO FAIL] {exc}")
            return 1

        if not generated_specs:
            print("\n[AUTO] No eligible new generated spells found for current tier window.")
        else:
            print(f"\n[AUTO] Generating {len(generated_specs)} spell(s).")
            for spec in generated_specs:
                try:
                    emit_artifacts(spec, args)
                    generated_success += 1
                    saved = save_generated_spec(
                        spec, Path(args.generated_spec_dir), run_stamp=run_stamp
                    )
                    print(f"Saved generated spec: {saved}")
                except ValueError as exc:
                    generated_fail += 1
                    print(f"[AUTO FAIL] {spec.name}: {exc}")
                    if args.fail_fast:
                        break

    total_success = queue_success + generated_success
    total_fail = queue_fail + generated_fail

    print("\nAuto pipeline summary")
    print(f"- Queue success: {queue_success}")
    print(f"- Queue fail: {queue_fail}")
    print(f"- Generated success: {generated_success}")
    print(f"- Generated fail: {generated_fail}")
    print(f"- Total success: {total_success}")
    print(f"- Total fail: {total_fail}")

    if total_success == 0:
        print("No spells were produced. Add queue specs or increase generation settings.")
        return 1
    if total_fail > 0:
        return 1
    return 0


def command_gui(args: argparse.Namespace) -> int:
    try:
        import tkinter as tk
        from tkinter import ttk
    except ImportError:
        print("Tkinter is not available in this Python environment.")
        return 1

    root = tk.Tk()
    root.title("Sigil Maker Auto Pipeline")
    root.geometry("980x720")

    queue_dir_var = tk.StringVar(value=str(getattr(args, "spec_dir", "quartz/spell_queue")))
    generate_count_var = tk.IntVar(value=int(getattr(args, "generate_count", 10)))
    min_tier_var = tk.StringVar(value=str(getattr(args, "min_tier", "T0")))
    max_tier_var = tk.StringVar(value=str(getattr(args, "max_tier", "T6")))
    recursive_var = tk.BooleanVar(value=True)
    archive_queue_var = tk.BooleanVar(value=True)
    sync_indexes_var = tk.BooleanVar(value=True)
    sync_spells_hub_var = tk.BooleanVar(value=True)
    ollama_model_var = tk.StringVar(value=str(getattr(args, "ollama_model", "")))
    ollama_timeout_var = tk.IntVar(value=int(getattr(args, "ollama_timeout_seconds", 90)))
    status_var = tk.StringVar(value="Idle")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    controls = ttk.LabelFrame(root, text="Auto Pipeline Settings", padding=12)
    controls.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
    controls.columnconfigure(1, weight=1)
    controls.columnconfigure(3, weight=1)

    ttk.Label(controls, text="Queue Directory").grid(row=0, column=0, sticky="w", padx=4, pady=4)
    ttk.Entry(controls, textvariable=queue_dir_var).grid(row=0, column=1, sticky="ew", padx=4, pady=4)

    ttk.Label(controls, text="Generate Count").grid(row=0, column=2, sticky="w", padx=4, pady=4)
    ttk.Spinbox(controls, from_=0, to=200, textvariable=generate_count_var, width=8).grid(
        row=0, column=3, sticky="w", padx=4, pady=4
    )

    ttk.Label(controls, text="Min Tier").grid(row=1, column=0, sticky="w", padx=4, pady=4)
    ttk.Combobox(
        controls, textvariable=min_tier_var, values=TIER_SEQUENCE, state="readonly", width=10
    ).grid(row=1, column=1, sticky="w", padx=4, pady=4)

    ttk.Label(controls, text="Max Tier").grid(row=1, column=2, sticky="w", padx=4, pady=4)
    ttk.Combobox(
        controls, textvariable=max_tier_var, values=TIER_SEQUENCE, state="readonly", width=10
    ).grid(row=1, column=3, sticky="w", padx=4, pady=4)

    ttk.Label(controls, text="Ollama Model (optional)").grid(
        row=2, column=0, sticky="w", padx=4, pady=4
    )
    ttk.Entry(controls, textvariable=ollama_model_var).grid(
        row=2, column=1, sticky="ew", padx=4, pady=4
    )

    ttk.Label(controls, text="Ollama Timeout (s)").grid(row=2, column=2, sticky="w", padx=4, pady=4)
    ttk.Spinbox(controls, from_=5, to=600, textvariable=ollama_timeout_var, width=8).grid(
        row=2, column=3, sticky="w", padx=4, pady=4
    )

    toggle_row = ttk.Frame(controls)
    toggle_row.grid(row=3, column=0, columnspan=4, sticky="w", padx=4, pady=(4, 2))
    ttk.Checkbutton(toggle_row, text="Recursive queue scan", variable=recursive_var).pack(
        side="left", padx=(0, 10)
    )
    ttk.Checkbutton(toggle_row, text="Archive queue files", variable=archive_queue_var).pack(
        side="left", padx=(0, 10)
    )
    ttk.Checkbutton(toggle_row, text="Sync grimoire indexes", variable=sync_indexes_var).pack(
        side="left", padx=(0, 10)
    )
    ttk.Checkbutton(toggle_row, text="Sync Spells hub", variable=sync_spells_hub_var).pack(
        side="left"
    )

    actions = ttk.Frame(root, padding=(10, 0, 10, 8))
    actions.grid(row=2, column=0, sticky="ew")
    actions.columnconfigure(0, weight=1)
    actions.columnconfigure(1, weight=1)
    actions.columnconfigure(2, weight=6)

    log_box = tk.Text(root, wrap="word", font=("Consolas", 10))
    log_box.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 8))
    log_box.insert("end", "Ready. Click 'Run Auto Pipeline' to generate and sync spells.\n")
    log_box.see("end")

    def append_log(text: str) -> None:
        if not text:
            return
        log_box.insert("end", text if text.endswith("\n") else text + "\n")
        log_box.see("end")

    def run_pipeline() -> None:
        run_button.configure(state="disabled")
        status_var.set("Running...")

        def worker() -> None:
            namespace = argparse.Namespace(
                spec_dir=queue_dir_var.get().strip() or "quartz/spell_queue",
                spec_glob="*.json",
                no_recursive=not recursive_var.get(),
                fail_fast=False,
                archive_queue=archive_queue_var.get(),
                processed_dir="quartz/spell_queue/_processed",
                failed_dir="quartz/spell_queue/_failed",
                generated_spec_dir="quartz/spell_queue/_generated",
                generate_count=max(0, int(generate_count_var.get())),
                skip_generation=False,
                min_tier=min_tier_var.get(),
                max_tier=max_tier_var.get(),
                markdown_dir="content/Spells",
                json_dir="quartz/static/spell_exports",
                row_dir="quartz/static/spell_exports",
                markdown_out=None,
                json_out=None,
                grimoire_row_out=None,
                append_all_grimoire=None,
                save_spec_out=None,
                sync_grimoire_indexes=sync_indexes_var.get(),
                all_grimoire_path="content/All Grimoire.md",
                rarity_pages_dir="content",
                sync_spells_hub=sync_spells_hub_var.get(),
                spells_hub_path="content/Spells.md",
                ollama_model=ollama_model_var.get().strip(),
                ollama_timeout_seconds=max(5, int(ollama_timeout_var.get())),
            )

            stream = io.StringIO()
            with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
                exit_code = command_auto(namespace)
            output = stream.getvalue()

            def finalize() -> None:
                append_log(output)
                append_log(f"[GUI] Pipeline exit code: {exit_code}")
                status_var.set("Idle")
                run_button.configure(state="normal")

            root.after(0, finalize)

        threading.Thread(target=worker, daemon=True).start()

    run_button = ttk.Button(actions, text="Run Auto Pipeline", command=run_pipeline)
    run_button.grid(row=0, column=0, sticky="w", padx=(0, 8))

    ttk.Button(actions, text="Clear Log", command=lambda: log_box.delete("1.0", "end")).grid(
        row=0, column=1, sticky="w"
    )
    ttk.Label(actions, textvariable=status_var).grid(row=0, column=2, sticky="e")

    root.mainloop()
    return 0


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
    markdown_dir = Path(getattr(args, "markdown_dir", "content/Spells"))
    json_dir = Path(getattr(args, "json_dir", "quartz/static/spell_exports"))
    row_dir = Path(getattr(args, "row_dir", "quartz/static/spell_exports"))
    markdown_out = (
        Path(args.markdown_out) if args.markdown_out else markdown_dir / f"{spec.name}.md"
    )
    json_out = (
        Path(args.json_out) if args.json_out else json_dir / f"{slug}.json"
    )
    row_out = (
        Path(args.grimoire_row_out)
        if args.grimoire_row_out
        else row_dir / f"{slug}.all_grimoire_row.md"
    )
    return markdown_out, json_out, row_out


def emit_artifacts(spec: SpellSpec, args: argparse.Namespace) -> SpellCostBreakdown:
    breakdown = calculate_cost(spec)
    markdown_out, json_out, row_out = resolve_output_paths(args, spec)

    ollama_interpretation: str | None = None
    ollama_model = (getattr(args, "ollama_model", "") or "").strip()
    if ollama_model:
        try:
            ollama_interpretation = interpret_spell_with_ollama(
                spec,
                breakdown,
                model=ollama_model,
                timeout_seconds=int(getattr(args, "ollama_timeout_seconds", 90)),
            )
        except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
            print(f"[OLLAMA] Interpretation skipped for '{spec.name}': {exc}")

    md = markdown_page(spec, breakdown, ollama_interpretation=ollama_interpretation)
    row = grimoire_row(spec, breakdown)
    payload = {"spec": asdict(spec), "cost": asdict(breakdown), "all_grimoire_row": row}
    if ollama_interpretation:
        payload["ollama_interpretation"] = ollama_interpretation

    write_text(markdown_out, md)
    write_json(json_out, payload)
    write_text(row_out, row + "\n")

    if getattr(args, "save_spec_out", None):
        write_json(Path(args.save_spec_out), asdict(spec))

    if getattr(args, "append_all_grimoire", None):
        append_all_grimoire(Path(args.append_all_grimoire), row)

    synced_all: Path | None = None
    synced_rarity: Path | None = None
    synced_hub: Path | None = None
    if getattr(args, "sync_grimoire_indexes", False):
        all_grimoire_path = Path(getattr(args, "all_grimoire_path", "content/All Grimoire.md"))
        rarity_pages_dir = Path(getattr(args, "rarity_pages_dir", "content"))
        spells_hub_path: Path | None = None
        if getattr(args, "sync_spells_hub", False):
            spells_hub_path = Path(getattr(args, "spells_hub_path", "content/Spells.md"))
        synced_all, synced_rarity, synced_hub = sync_spell_indexes(
            spec,
            breakdown,
            all_grimoire_path=all_grimoire_path,
            rarity_pages_dir=rarity_pages_dir,
            spells_hub_path=spells_hub_path,
        )

    print(f"Created spell: {spec.name}")
    print(f"Total cost: {breakdown.total_w} W ({breakdown.required_tier}, {breakdown.rarity})")
    print(f"Markdown: {markdown_out}")
    print(f"AI JSON: {json_out}")
    print(f"All Grimoire row: {row_out}")
    if synced_all is not None:
        print(f"Synced All Grimoire: {synced_all}")
    if synced_rarity is not None:
        print(f"Synced rarity page: {synced_rarity}")
    if synced_hub is not None:
        print(f"Synced world hub: {synced_hub}")
    if getattr(args, "save_spec_out", None):
        print(f"Saved input spec: {Path(args.save_spec_out)}")
    return breakdown


def load_spec(spec_path: Path) -> SpellSpec:
    if not spec_path.exists():
        raise FileNotFoundError(f"Spec file not found: {spec_path}")
    spec_data = json.loads(spec_path.read_text(encoding="utf-8-sig"))
    return parse_spec(spec_data)


def command_create(args: argparse.Namespace) -> int:
    try:
        spec = load_spec(Path(args.spec))
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


def command_recursive(args: argparse.Namespace) -> int:
    spec_dir = Path(args.spec_dir)
    if not spec_dir.exists() or not spec_dir.is_dir():
        print(f"Spec directory not found or not a directory: {spec_dir}")
        return 1

    pattern = args.spec_glob
    iterator = spec_dir.rglob(pattern) if not args.no_recursive else spec_dir.glob(pattern)
    spec_files = sorted([p for p in iterator if p.is_file()])
    if not spec_files:
        print(f"No spec files found in {spec_dir} using pattern '{pattern}'")
        return 1

    print(f"Found {len(spec_files)} spec files.")
    successes: list[str] = []
    failures: list[tuple[str, str]] = []

    for spec_path in spec_files:
        print(f"\n[PROCESS] {spec_path}")
        try:
            spec = load_spec(spec_path)
            emit_artifacts(spec, args)
            successes.append(str(spec_path))
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
            failures.append((str(spec_path), str(exc)))
            print(f"[FAIL] {spec_path}: {exc}")
            if args.fail_fast:
                break

    print("\nRecursive ingest summary")
    print(f"- Successful: {len(successes)}")
    print(f"- Failed: {len(failures)}")
    if failures:
        print("- Failure details:")
        for path, reason in failures:
            print(f"  - {path}: {reason}")
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
        "hook_mode_multiplier": 2.0,
        "hook_mode_flat_w": 0,
        "notes": "Optional freeform notes for designers.",
    }
    print(json.dumps(schema, indent=2))
    return 0


def command_tiers(_: argparse.Namespace) -> int:
    print("Solumora Control Tier Overview")
    print("-----------------------------")
    for row in TIER_OVERVIEW:
        print(f"{row['tier']}: {row['range']} - {row['tagline']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create validated Solumora sigil spells. "
            "Run with no command to execute the autonomous queue+generation pipeline."
        ),
        epilog=(
            "Examples:\n"
            "  python quartz/sigil_maker.py\n"
            "  python quartz/sigil_maker.py auto --generate-count 12\n"
            "  python quartz/sigil_maker.py create --spec spell.json\n"
            "  python quartz/sigil_maker.py tiers"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")

    def add_output_args(command_parser: argparse.ArgumentParser) -> None:
        command_parser.add_argument(
            "--markdown-dir",
            default="content/Spells",
            help="Directory for generated spell markdown pages (ignored if --markdown-out is set).",
        )
        command_parser.add_argument(
            "--json-dir",
            default="quartz/static/spell_exports",
            help="Directory for generated AI JSON exports (ignored if --json-out is set).",
        )
        command_parser.add_argument(
            "--row-dir",
            default="quartz/static/spell_exports",
            help="Directory for generated All Grimoire row snippets (ignored if --grimoire-row-out is set).",
        )
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

    def add_ollama_args(command_parser: argparse.ArgumentParser) -> None:
        command_parser.add_argument(
            "--ollama-model",
            default="",
            help=(
                "Optional Ollama model name. If provided, Sigil Maker requests an "
                "LLM interpretation for each emitted spell. Auto mode also uses it "
                "for generated spell naming/description polish."
            ),
        )
        command_parser.add_argument(
            "--ollama-timeout-seconds",
            type=int,
            default=90,
            help="Timeout in seconds for each Ollama request.",
        )

    def add_sync_args(command_parser: argparse.ArgumentParser) -> None:
        command_parser.add_argument(
            "--sync-grimoire-indexes",
            action=argparse.BooleanOptionalAction,
            default=False,
            help=(
                "Sync spell into All Grimoire and the derived rarity page "
                "(Common/Uncommon/Rare/Legendary/Mythic)."
            ),
        )
        command_parser.add_argument(
            "--all-grimoire-path",
            default="content/All Grimoire.md",
            help="Path to All Grimoire markdown table file.",
        )
        command_parser.add_argument(
            "--rarity-pages-dir",
            default="content",
            help="Directory containing rarity pages (e.g., Common Grimoire.md).",
        )
        command_parser.add_argument(
            "--sync-spells-hub",
            action=argparse.BooleanOptionalAction,
            default=False,
            help="Also append spell references to the world-facing spells hub.",
        )
        command_parser.add_argument(
            "--spells-hub-path",
            default="content/Spells.md",
            help="Path to spells hub page used for world-facing spell index links.",
        )

    create = subparsers.add_parser("create", help="Create spell artifacts from a JSON spec.")
    create.add_argument("--spec", required=True, help="Path to spell spec JSON.")
    add_output_args(create)
    add_sync_args(create)
    add_ollama_args(create)
    create.set_defaults(func=command_create)

    interactive = subparsers.add_parser(
        "interactive",
        help="Guided prompt flow for creating a spell without writing JSON manually.",
    )
    add_output_args(interactive)
    add_sync_args(interactive)
    add_ollama_args(interactive)
    interactive.set_defaults(func=command_interactive)

    recursive = subparsers.add_parser(
        "recursive",
        help="Recursively ingest many spell specs and publish them into grimoire/world indexes.",
    )
    recursive.add_argument("--spec-dir", required=True, help="Directory containing spell spec JSON files.")
    recursive.add_argument(
        "--spec-glob",
        default="*.json",
        help="Glob pattern for spec files inside --spec-dir.",
    )
    recursive.add_argument(
        "--no-recursive",
        action="store_true",
        help="Only scan top-level --spec-dir instead of recursive subdirectories.",
    )
    recursive.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop immediately when one spec fails validation/parsing.",
    )
    add_output_args(recursive)
    add_sync_args(recursive)
    add_ollama_args(recursive)
    recursive.set_defaults(
        func=command_recursive,
        sync_grimoire_indexes=True,
        sync_spells_hub=True,
    )

    auto = subparsers.add_parser(
        "auto",
        help="Run autonomous queue ingest + spell generation + vault index sync.",
    )
    auto.add_argument(
        "--spec-dir",
        default="quartz/spell_queue",
        help="Queue directory containing spell spec JSON files to ingest.",
    )
    auto.add_argument(
        "--spec-glob",
        default="*.json",
        help="Glob pattern for queued spec files inside --spec-dir.",
    )
    auto.add_argument(
        "--no-recursive",
        action="store_true",
        help="Only scan top-level --spec-dir for queue specs.",
    )
    auto.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop immediately on the first queue or generation failure.",
    )
    auto.add_argument(
        "--archive-queue",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Move processed queue specs into archive folders.",
    )
    auto.add_argument(
        "--processed-dir",
        default="quartz/spell_queue/_processed",
        help="Archive location for successfully processed queue specs.",
    )
    auto.add_argument(
        "--failed-dir",
        default="quartz/spell_queue/_failed",
        help="Archive location for failed queue specs.",
    )
    auto.add_argument(
        "--generated-spec-dir",
        default="quartz/spell_queue/_generated",
        help="Directory to store generated spell spec JSON snapshots per run.",
    )
    auto.add_argument(
        "--generate-count",
        type=int,
        default=10,
        help="How many new spells to generate per run in addition to queue ingestion.",
    )
    auto.add_argument(
        "--skip-generation",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Disable procedural spell generation and only process queued specs.",
    )
    auto.add_argument(
        "--min-tier",
        choices=TIER_SEQUENCE,
        default="T0",
        help="Lower tier bound for auto-generated spells.",
    )
    auto.add_argument(
        "--max-tier",
        choices=TIER_SEQUENCE,
        default="T6",
        help="Upper tier bound for auto-generated spells.",
    )
    add_output_args(auto)
    add_sync_args(auto)
    add_ollama_args(auto)
    auto.set_defaults(
        func=command_auto,
        sync_grimoire_indexes=True,
        sync_spells_hub=True,
        ollama_model="llama3.1:8b",
    )

    gui = subparsers.add_parser(
        "gui",
        help="Launch a desktop UI for one-click autonomous generation and sync.",
    )
    gui.add_argument(
        "--spec-dir",
        default="quartz/spell_queue",
        help="Initial queue directory shown in the UI.",
    )
    gui.add_argument(
        "--generate-count",
        type=int,
        default=10,
        help="Initial auto-generation count shown in the UI.",
    )
    gui.add_argument(
        "--min-tier",
        choices=TIER_SEQUENCE,
        default="T0",
        help="Initial minimum tier shown in the UI.",
    )
    gui.add_argument(
        "--max-tier",
        choices=TIER_SEQUENCE,
        default="T6",
        help="Initial maximum tier shown in the UI.",
    )
    gui.add_argument(
        "--ollama-model",
        default="llama3.1:8b",
        help="Initial Ollama model shown in the UI.",
    )
    gui.add_argument(
        "--ollama-timeout-seconds",
        type=int,
        default=90,
        help="Initial Ollama timeout shown in the UI.",
    )
    gui.set_defaults(func=command_gui)

    schema = subparsers.add_parser("schema", help="Print a spell spec JSON template.")
    schema.set_defaults(func=command_schema)

    tiers = subparsers.add_parser("tiers", help="Print control tier ranges and labels.")
    tiers.set_defaults(func=command_tiers)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, "func"):
        print("No command provided. Running autonomous pipeline.\n")
        args = parser.parse_args(["auto"])
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
