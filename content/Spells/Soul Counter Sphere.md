# Soul Counter Sphere

disrupts soul energy in a spherical envelope with active regulation while it runs

## Effect

The caster inscribes a sigil that disrupts soul energy in a spherical envelope with active regulation while it runs. Effect range: line-of-sight. Persistence: latched.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Sphere | +30 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Latched | +40 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 80 + 40 + 35 + 30 = 215 W
- Subtotal: 4340 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **15233 W**
- Required Control Tier: **T7**
- Rarity bucket: **Legendary**

## All Grimoire Row

| **Soul Counter Sphere** | Circle | Counter | Control | T7 | Soul | Raw | Sphere | Line-of-Sight | Latched | Group |

## AI Spell Data

```json
{
  "name": "Soul Counter Sphere",
  "summary": "disrupts soul energy in a spherical envelope with active regulation while it runs",
  "effect_description": "The caster inscribes a sigil that disrupts soul energy in a spherical envelope with active regulation while it runs. Effect range: line-of-sight. Persistence: latched.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Sphere",
  "reach": "Line-of-Sight",
  "persistence": "Latched",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 30,
    "reach_w": 80,
    "persistence_w": 40,
    "target_w": 35,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4340,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 15233,
    "required_tier": "T7",
    "rarity": "Legendary"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
