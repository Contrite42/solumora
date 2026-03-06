# Soul Counter Cone 2

Disrupts soul flux as a fan spread at line-of-sight reach, targeting the caster with long timed hold with active regulation while it runs.

## Effect

Disrupts soul flux as a fan spread at line-of-sight reach, targeting the caster with long timed hold with active regulation while it runs. A circle counter/control recipe that channels soul discipline into soul output. It applies a cone pattern against self across line-of-sight reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 80 + 25 + 0 + 0 = 115 W
- Subtotal: 4240 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **14882 W**
- Required Control Tier: **T7**
- Rarity bucket: **Legendary**

## All Grimoire Row

| **Soul Counter Cone 2** | Circle | Counter | Control | T7 | Soul | Soul | Cone | Line-of-Sight | Timed Long | Self |

## AI Spell Data

```json
{
  "name": "Soul Counter Cone 2",
  "summary": "Disrupts soul flux as a fan spread at line-of-sight reach, targeting the caster with long timed hold with active regulation while it runs.",
  "effect_description": "Disrupts soul flux as a fan spread at line-of-sight reach, targeting the caster with long timed hold with active regulation while it runs. A circle counter/control recipe that channels soul discipline into soul output. It applies a cone pattern against self across line-of-sight reach with timed long persistence.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cone",
  "reach": "Line-of-Sight",
  "persistence": "Timed Long",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 10,
    "reach_w": 80,
    "persistence_w": 25,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4240,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 14882,
    "required_tier": "T7",
    "rarity": "Legendary"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
