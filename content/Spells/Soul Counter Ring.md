# Soul Counter Ring

Disrupts soul flux as a ring perimeter at medium reach, targeting one object with immediate discharge by creating a fresh flux expression.

## Effect

Disrupts soul flux as a ring perimeter at medium reach, targeting one object with immediate discharge by creating a fresh flux expression. A circle counter/create recipe that channels soul discipline into soul output. It applies a ring pattern against object across medium reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Medium | +15 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 15 + 0 + 2 + 0 = 32 W
- Subtotal: 4157 W
- Hook/Mode complexity multiplier: x2.9899999999999998
- Hook/Mode flat addition: +0 W
- Total: **12429 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Counter Ring** | Circle | Counter | Create | T6 | Soul | Soul | Ring | Medium | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Soul Counter Ring",
  "summary": "Disrupts soul flux as a ring perimeter at medium reach, targeting one object with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Disrupts soul flux as a ring perimeter at medium reach, targeting one object with immediate discharge by creating a fresh flux expression. A circle counter/create recipe that channels soul discipline into soul output. It applies a ring pattern against object across medium reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Ring",
  "reach": "Medium",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 15,
    "reach_w": 15,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4157,
    "hook_mode_multiplier": 2.9899999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 12429,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
