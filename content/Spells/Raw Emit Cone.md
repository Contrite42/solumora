# Raw Emit Cone

Releases raw flux as a fan spread at short reach, targeting a prepared surface with immediate discharge with active regulation while it runs.

## Effect

Releases raw flux as a fan spread at short reach, targeting a prepared surface with immediate discharge with active regulation while it runs. A pentagon emit/control recipe that channels raw discipline into raw output. It applies a cone pattern against surface across short reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Short | +5 W |
| Persistence | Immediate | +0 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 1 = 20 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 5 + 0 + 5 + 0 = 20 W
- Subtotal: 40 W
- Hook/Mode complexity multiplier: x1.35
- Hook/Mode flat addition: +0 W
- Total: **54 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Raw Emit Cone** | Pentagon | Emit | Control | T2 | Raw | Raw | Cone | Short | Immediate | Surface |

## AI Spell Data

```json
{
  "name": "Raw Emit Cone",
  "summary": "Releases raw flux as a fan spread at short reach, targeting a prepared surface with immediate discharge with active regulation while it runs.",
  "effect_description": "Releases raw flux as a fan spread at short reach, targeting a prepared surface with immediate discharge with active regulation while it runs. A pentagon emit/control recipe that channels raw discipline into raw output. It applies a cone pattern against surface across short reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Cone",
  "reach": "Short",
  "persistence": "Immediate",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 1,
    "core_discipline_w": 20,
    "pattern_w": 10,
    "reach_w": 5,
    "persistence_w": 0,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 40,
    "hook_mode_multiplier": 1.35,
    "hook_mode_flat_w": 0,
    "total_w": 54,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
