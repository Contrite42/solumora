# Mind Counter Plane

Disrupts mind neuro flux as a planar spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression.

## Effect

Disrupts mind neuro flux as a planar spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression. A pentagon counter/create recipe that channels mind discipline into neuro output. It applies a plane pattern against individual across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 25 = 500 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 40 + 0 + 8 + 0 = 48 W
- Subtotal: 548 W
- Hook/Mode complexity multiplier: x2.9899999999999998
- Hook/Mode flat addition: +0 W
- Total: **1639 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Counter Plane** | Pentagon | Counter | Create | T5 | Mind | Neuro | Plane | Long | Immediate | Individual |

## AI Spell Data

```json
{
  "name": "Mind Counter Plane",
  "summary": "Disrupts mind neuro flux as a planar spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Disrupts mind neuro flux as a planar spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression. A pentagon counter/create recipe that channels mind discipline into neuro output. It applies a plane pattern against individual across long reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Create",
  "shape": "Pentagon",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Plane",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 25,
    "core_discipline_w": 500,
    "pattern_w": 0,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 548,
    "hook_mode_multiplier": 2.9899999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 1639,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
