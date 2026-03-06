# Soul Counter Point

Disrupts soul neuro flux as a point focus at line-of-sight reach, targeting one individual with sustained channeling by creating a fresh flux expression.

## Effect

Disrupts soul neuro flux as a point focus at line-of-sight reach, targeting one individual with sustained channeling by creating a fresh flux expression. A circle counter/create recipe that channels soul discipline into neuro output. It applies a point pattern against individual across line-of-sight reach with sustained persistence. The sustained window is set to 20 minutes.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Neuro | +30 W premium |
| Pattern | Point | +0 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Sustained (20 min planned active window) | +20 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 80 + 20 + 8 + 30 = 138 W
- Subtotal: 4263 W
- Hook/Mode complexity multiplier: x2.9899999999999998
- Hook/Mode flat addition: +0 W
- Total: **12746 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Counter Point** | Circle | Counter | Create | T6 | Soul | Neuro | Point | Line-of-Sight | Sustained | Individual |

## AI Spell Data

```json
{
  "name": "Soul Counter Point",
  "summary": "Disrupts soul neuro flux as a point focus at line-of-sight reach, targeting one individual with sustained channeling by creating a fresh flux expression.",
  "effect_description": "Disrupts soul neuro flux as a point focus at line-of-sight reach, targeting one individual with sustained channeling by creating a fresh flux expression. A circle counter/create recipe that channels soul discipline into neuro output. It applies a point pattern against individual across line-of-sight reach with sustained persistence. The sustained window is set to 20 minutes.",
  "hook": "Counter",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Neuro",
  "pattern": "Point",
  "reach": "Line-of-Sight",
  "persistence": "Sustained",
  "target_spec": "Individual",
  "sustained_minutes": 20,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 80,
    "persistence_w": 20,
    "target_w": 8,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4263,
    "hook_mode_multiplier": 2.9899999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 12746,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
