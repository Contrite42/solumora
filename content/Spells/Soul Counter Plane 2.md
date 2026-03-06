# Soul Counter Plane 2

Disrupts soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs.

## Effect

Disrupts soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs. A pentagon counter/control recipe that channels soul discipline into soul output. It applies a plane pattern against object across line-of-sight reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 80 + 0 + 2 + 0 = 82 W
- Subtotal: 1582 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **5553 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Counter Plane 2** | Pentagon | Counter | Control | T6 | Soul | Soul | Plane | Line-of-Sight | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Soul Counter Plane 2",
  "summary": "Disrupts soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs.",
  "effect_description": "Disrupts soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs. A pentagon counter/control recipe that channels soul discipline into soul output. It applies a plane pattern against object across line-of-sight reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Plane",
  "reach": "Line-of-Sight",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 0,
    "reach_w": 80,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1582,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 5553,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
