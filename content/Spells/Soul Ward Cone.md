# Soul Ward Cone

Establishes soul shock flux as a fan spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs.

## Effect

Establishes soul shock flux as a fan spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs. A pentagon ward/control recipe that channels soul discipline into shock output. It applies a cone pattern against object across line-of-sight reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Ward | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Shock | +60 W premium |
| Pattern | Cone | +10 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 80 + 0 + 2 + 60 = 152 W
- Subtotal: 1652 W
- Hook/Mode complexity multiplier: x2.7
- Hook/Mode flat addition: +0 W
- Total: **4460 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Ward Cone** | Pentagon | Ward | Control | T6 | Soul | Shock | Cone | Line-of-Sight | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Soul Ward Cone",
  "summary": "Establishes soul shock flux as a fan spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs.",
  "effect_description": "Establishes soul shock flux as a fan spread at line-of-sight reach, targeting one object with immediate discharge with active regulation while it runs. A pentagon ward/control recipe that channels soul discipline into shock output. It applies a cone pattern against object across line-of-sight reach with immediate persistence.",
  "hook": "Ward",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Shock",
  "pattern": "Cone",
  "reach": "Line-of-Sight",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 10,
    "reach_w": 80,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 1652,
    "hook_mode_multiplier": 2.7,
    "hook_mode_flat_w": 0,
    "total_w": 4460,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
