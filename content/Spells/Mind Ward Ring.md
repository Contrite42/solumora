# Mind Ward Ring

establishes mind energy in a ring perimeter with active regulation while it runs

## Effect

The caster inscribes a sigil that establishes mind energy in a ring perimeter with active regulation while it runs. Effect range: line-of-sight. Persistence: latched.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Ward | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Ring | +15 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Latched | +40 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 80 + 40 + 35 + 30 = 200 W
- Subtotal: 1575 W
- Hook/Mode complexity multiplier: x2.7
- Hook/Mode flat addition: +0 W
- Total: **4252 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Ward Ring** | Circle | Ward | Control | T6 | Mind | Raw | Ring | Line-of-Sight | Latched | Group |

## AI Spell Data

```json
{
  "name": "Mind Ward Ring",
  "summary": "establishes mind energy in a ring perimeter with active regulation while it runs",
  "effect_description": "The caster inscribes a sigil that establishes mind energy in a ring perimeter with active regulation while it runs. Effect range: line-of-sight. Persistence: latched.",
  "hook": "Ward",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Ring",
  "reach": "Line-of-Sight",
  "persistence": "Latched",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 15,
    "reach_w": 80,
    "persistence_w": 40,
    "target_w": 35,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1575,
    "hook_mode_multiplier": 2.7,
    "hook_mode_flat_w": 0,
    "total_w": 4252,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
