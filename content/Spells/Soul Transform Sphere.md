# Soul Transform Sphere

Reconfigures soul flux as a spherical envelope at linked reach, targeting a grouped cluster with conditional hold by creating a fresh flux expression.

## Effect

Reconfigures soul flux as a spherical envelope at linked reach, targeting a grouped cluster with conditional hold by creating a fresh flux expression. A circle transform/create recipe that channels soul discipline into soul output. It applies a sphere pattern against group across linked reach with conditional persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Linked | +150 W |
| Persistence | Conditional | +20 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 150 + 20 + 35 + 0 = 235 W
- Subtotal: 4360 W
- Hook/Mode complexity multiplier: x1.9549999999999998
- Hook/Mode flat addition: +0 W
- Total: **8524 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Transform Sphere** | Circle | Transform | Create | T6 | Soul | Soul | Sphere | Linked | Conditional | Group |

## AI Spell Data

```json
{
  "name": "Soul Transform Sphere",
  "summary": "Reconfigures soul flux as a spherical envelope at linked reach, targeting a grouped cluster with conditional hold by creating a fresh flux expression.",
  "effect_description": "Reconfigures soul flux as a spherical envelope at linked reach, targeting a grouped cluster with conditional hold by creating a fresh flux expression. A circle transform/create recipe that channels soul discipline into soul output. It applies a sphere pattern against group across linked reach with conditional persistence.",
  "hook": "Transform",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Sphere",
  "reach": "Linked",
  "persistence": "Conditional",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 30,
    "reach_w": 150,
    "persistence_w": 20,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4360,
    "hook_mode_multiplier": 1.9549999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 8524,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
