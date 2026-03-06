# Soul Counter Plane

Disrupts soul flux as a planar spread at anchored reach, targeting a marked signature with conditional hold with active regulation while it runs.

## Effect

Disrupts soul flux as a planar spread at anchored reach, targeting a marked signature with conditional hold with active regulation while it runs. A circle counter/control recipe that channels soul discipline into soul output. It applies a plane pattern against marked across anchored reach with conditional persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Anchored | +0 W |
| Persistence | Conditional | +20 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 20 + 15 + 0 = 35 W
- Subtotal: 4160 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **14602 W**
- Required Control Tier: **T7**
- Rarity bucket: **Legendary**

## All Grimoire Row

| **Soul Counter Plane** | Circle | Counter | Control | T7 | Soul | Soul | Plane | Anchored | Conditional | Marked |

## AI Spell Data

```json
{
  "name": "Soul Counter Plane",
  "summary": "Disrupts soul flux as a planar spread at anchored reach, targeting a marked signature with conditional hold with active regulation while it runs.",
  "effect_description": "Disrupts soul flux as a planar spread at anchored reach, targeting a marked signature with conditional hold with active regulation while it runs. A circle counter/control recipe that channels soul discipline into soul output. It applies a plane pattern against marked across anchored reach with conditional persistence.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Plane",
  "reach": "Anchored",
  "persistence": "Conditional",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 20,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4160,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 14602,
    "required_tier": "T7",
    "rarity": "Legendary"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
