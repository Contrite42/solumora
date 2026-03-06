# Soul Counter Cone 3

Disrupts soul flux as a fan spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression.

## Effect

Disrupts soul flux as a fan spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression. A circle counter/create recipe that channels soul discipline into soul output. It applies a cone pattern against individual across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 40 + 0 + 8 + 0 = 58 W
- Subtotal: 4183 W
- Hook/Mode complexity multiplier: x2.9899999999999998
- Hook/Mode flat addition: +0 W
- Total: **12507 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Counter Cone 3** | Circle | Counter | Create | T6 | Soul | Soul | Cone | Long | Immediate | Individual |

## AI Spell Data

```json
{
  "name": "Soul Counter Cone 3",
  "summary": "Disrupts soul flux as a fan spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Disrupts soul flux as a fan spread at long reach, targeting one individual with immediate discharge by creating a fresh flux expression. A circle counter/create recipe that channels soul discipline into soul output. It applies a cone pattern against individual across long reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cone",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 10,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4183,
    "hook_mode_multiplier": 2.9899999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 12507,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
