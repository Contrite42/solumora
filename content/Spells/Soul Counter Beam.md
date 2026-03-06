# Soul Counter Beam

Disrupts soul flux as a directed line at long reach, targeting a prepared surface with long timed hold with active regulation while it runs.

## Effect

Disrupts soul flux as a directed line at long reach, targeting a prepared surface with long timed hold with active regulation while it runs. A circle counter/control recipe that channels soul discipline into soul output. It applies a beam pattern against surface across long reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Long | +40 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 40 + 25 + 5 + 0 = 75 W
- Subtotal: 4200 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **14742 W**
- Required Control Tier: **T7**
- Rarity bucket: **Legendary**

## All Grimoire Row

| **Soul Counter Beam** | Circle | Counter | Control | T7 | Soul | Soul | Beam | Long | Timed Long | Surface |

## AI Spell Data

```json
{
  "name": "Soul Counter Beam",
  "summary": "Disrupts soul flux as a directed line at long reach, targeting a prepared surface with long timed hold with active regulation while it runs.",
  "effect_description": "Disrupts soul flux as a directed line at long reach, targeting a prepared surface with long timed hold with active regulation while it runs. A circle counter/control recipe that channels soul discipline into soul output. It applies a beam pattern against surface across long reach with timed long persistence.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Beam",
  "reach": "Long",
  "persistence": "Timed Long",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 5,
    "reach_w": 40,
    "persistence_w": 25,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4200,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 14742,
    "required_tier": "T7",
    "rarity": "Legendary"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
