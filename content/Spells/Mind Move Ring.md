# Mind Move Ring

repositions mind energy in a ring perimeter with active regulation while it runs

## Effect

The caster inscribes a sigil that repositions mind energy in a ring perimeter with active regulation while it runs. Effect range: line-of-sight. Persistence: timed long.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Ring | +15 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 80 + 25 + 60 + 30 = 210 W
- Subtotal: 1585 W
- Hook/Mode complexity multiplier: x2.0250000000000004
- Hook/Mode flat addition: +0 W
- Total: **3210 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Move Ring** | Circle | Move | Control | T5 | Mind | Raw | Ring | Line-of-Sight | Timed Long | Filter |

## AI Spell Data

```json
{
  "name": "Mind Move Ring",
  "summary": "repositions mind energy in a ring perimeter with active regulation while it runs",
  "effect_description": "The caster inscribes a sigil that repositions mind energy in a ring perimeter with active regulation while it runs. Effect range: line-of-sight. Persistence: timed long.",
  "hook": "Move",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Ring",
  "reach": "Line-of-Sight",
  "persistence": "Timed Long",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 15,
    "reach_w": 80,
    "persistence_w": 25,
    "target_w": 60,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1585,
    "hook_mode_multiplier": 2.0250000000000004,
    "hook_mode_flat_w": 0,
    "total_w": 3210,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
