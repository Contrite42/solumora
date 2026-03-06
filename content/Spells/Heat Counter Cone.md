# Heat Counter Cone

Disrupts heat thermal flux as a fan spread at self reach, targeting a prepared surface with immediate discharge by changing existing conditions.

## Effect

Disrupts heat thermal flux as a fan spread at self reach, targeting a prepared surface with immediate discharge by changing existing conditions. A square counter/affect recipe that channels heat discipline into thermal output. It applies a cone pattern against surface across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Heat | x2 multiplier |
| Output Mode | Thermal | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 2 = 16 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 5 + 0 = 15 W
- Subtotal: 31 W
- Hook/Mode complexity multiplier: x2.6
- Hook/Mode flat addition: +0 W
- Total: **81 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Heat Counter Cone** | Square | Counter | Affect | T2 | Heat | Thermal | Cone | Self | Immediate | Surface |

## AI Spell Data

```json
{
  "name": "Heat Counter Cone",
  "summary": "Disrupts heat thermal flux as a fan spread at self reach, targeting a prepared surface with immediate discharge by changing existing conditions.",
  "effect_description": "Disrupts heat thermal flux as a fan spread at self reach, targeting a prepared surface with immediate discharge by changing existing conditions. A square counter/affect recipe that channels heat discipline into thermal output. It applies a cone pattern against surface across self reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Heat",
  "output_mode": "Thermal",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 2,
    "core_discipline_w": 16,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 31,
    "hook_mode_multiplier": 2.6,
    "hook_mode_flat_w": 0,
    "total_w": 81,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
