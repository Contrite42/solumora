# Raw Dampen Ring

Reduces raw flux as a ring perimeter at line-of-sight reach, targeting one individual with long timed hold with active regulation while it runs.

## Effect

Reduces raw flux as a ring perimeter at line-of-sight reach, targeting one individual with long timed hold with active regulation while it runs. A circle dampen/control recipe that channels raw discipline into raw output. It applies a ring pattern against individual across line-of-sight reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 1 = 55 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 80 + 25 + 8 + 0 = 128 W
- Subtotal: 183 W
- Hook/Mode complexity multiplier: x2.565
- Hook/Mode flat addition: +0 W
- Total: **469 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Raw Dampen Ring** | Circle | Dampen | Control | T4 | Raw | Raw | Ring | Line-of-Sight | Timed Long | Individual |

## AI Spell Data

```json
{
  "name": "Raw Dampen Ring",
  "summary": "Reduces raw flux as a ring perimeter at line-of-sight reach, targeting one individual with long timed hold with active regulation while it runs.",
  "effect_description": "Reduces raw flux as a ring perimeter at line-of-sight reach, targeting one individual with long timed hold with active regulation while it runs. A circle dampen/control recipe that channels raw discipline into raw output. It applies a ring pattern against individual across line-of-sight reach with timed long persistence.",
  "hook": "Dampen",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Ring",
  "reach": "Line-of-Sight",
  "persistence": "Timed Long",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 1,
    "core_discipline_w": 55,
    "pattern_w": 15,
    "reach_w": 80,
    "persistence_w": 25,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 183,
    "hook_mode_multiplier": 2.565,
    "hook_mode_flat_w": 0,
    "total_w": 469,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
