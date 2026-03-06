# Binding Amplify Cylinder

Boosts binding neuro flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions.

## Effect

Boosts binding neuro flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions. A square amplify/affect recipe that channels binding discipline into neuro output. It applies a cylinder pattern against object across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Neuro | +60 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 10 = 80 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 0 + 0 + 2 + 60 = 82 W
- Subtotal: 162 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **356 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Binding Amplify Cylinder** | Square | Amplify | Affect | T3 | Binding | Neuro | Cylinder | Self | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Binding Amplify Cylinder",
  "summary": "Boosts binding neuro flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions.",
  "effect_description": "Boosts binding neuro flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions. A square amplify/affect recipe that channels binding discipline into neuro output. It applies a cylinder pattern against object across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Binding",
  "output_mode": "Neuro",
  "pattern": "Cylinder",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 10,
    "core_discipline_w": 80,
    "pattern_w": 20,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 162,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 356,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
