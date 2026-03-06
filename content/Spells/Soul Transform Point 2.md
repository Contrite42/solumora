# Soul Transform Point 2

Reconfigures soul flux as a point focus at medium reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.

## Effect

Reconfigures soul flux as a point focus at medium reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A circle transform/create recipe that channels soul discipline into soul output. It applies a point pattern against filter across medium reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Medium | +15 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 15 + 0 + 60 + 0 = 75 W
- Subtotal: 4200 W
- Hook/Mode complexity multiplier: x1.9549999999999998
- Hook/Mode flat addition: +0 W
- Total: **8211 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Transform Point 2** | Circle | Transform | Create | T6 | Soul | Soul | Point | Medium | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Soul Transform Point 2",
  "summary": "Reconfigures soul flux as a point focus at medium reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Reconfigures soul flux as a point focus at medium reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A circle transform/create recipe that channels soul discipline into soul output. It applies a point pattern against filter across medium reach with immediate persistence.",
  "hook": "Transform",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Point",
  "reach": "Medium",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 15,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4200,
    "hook_mode_multiplier": 1.9549999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 8211,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
