# Light Shape Cylinder

Refines light sonic flux as a column volume at anchored reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.

## Effect

Refines light sonic flux as a column volume at anchored reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A pentagon shape/create recipe that channels light discipline into sonic output. It applies a cylinder pattern against filter across anchored reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Light | x3 multiplier |
| Output Mode | Sonic | +10 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Anchored | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 3 = 60 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 0 + 0 + 60 + 10 = 90 W
- Subtotal: 150 W
- Hook/Mode complexity multiplier: x1.38
- Hook/Mode flat addition: +0 W
- Total: **207 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Light Shape Cylinder** | Pentagon | Shape | Create | T3 | Light | Sonic | Cylinder | Anchored | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Light Shape Cylinder",
  "summary": "Refines light sonic flux as a column volume at anchored reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Refines light sonic flux as a column volume at anchored reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A pentagon shape/create recipe that channels light discipline into sonic output. It applies a cylinder pattern against filter across anchored reach with immediate persistence.",
  "hook": "Shape",
  "mode": "Create",
  "shape": "Pentagon",
  "discipline": "Light",
  "output_mode": "Sonic",
  "pattern": "Cylinder",
  "reach": "Anchored",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 3,
    "core_discipline_w": 60,
    "pattern_w": 20,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 150,
    "hook_mode_multiplier": 1.38,
    "hook_mode_flat_w": 0,
    "total_w": 207,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
