# Soul Filter Point 2

Screens soul raw flux as a point focus at touch reach, targeting one object with sustained channeling by changing existing conditions.

## Effect

Screens soul raw flux as a point focus at touch reach, targeting one object with sustained channeling by changing existing conditions. A circle filter/affect recipe that channels soul discipline into raw output. It applies a point pattern against object across touch reach with sustained persistence. The sustained window is set to 30 minutes.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Point | +0 W |
| Reach | Touch | +2 W |
| Persistence | Sustained (30 min planned active window) | +30 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 2 + 30 + 2 + 30 = 64 W
- Subtotal: 4189 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **6702 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Filter Point 2** | Circle | Filter | Affect | T6 | Soul | Raw | Point | Touch | Sustained | Object |

## AI Spell Data

```json
{
  "name": "Soul Filter Point 2",
  "summary": "Screens soul raw flux as a point focus at touch reach, targeting one object with sustained channeling by changing existing conditions.",
  "effect_description": "Screens soul raw flux as a point focus at touch reach, targeting one object with sustained channeling by changing existing conditions. A circle filter/affect recipe that channels soul discipline into raw output. It applies a point pattern against object across touch reach with sustained persistence. The sustained window is set to 30 minutes.",
  "hook": "Filter",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Point",
  "reach": "Touch",
  "persistence": "Sustained",
  "target_spec": "Object",
  "sustained_minutes": 30,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 2,
    "persistence_w": 30,
    "target_w": 2,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4189,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 6702,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
