# Chemical Move Cylinder

Repositions chemical thermal flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions.

## Effect

Repositions chemical thermal flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions. A square move/affect recipe that channels chemical discipline into thermal output. It applies a cylinder pattern against object across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Thermal | +10 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 5 = 40 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 0 + 0 + 2 + 10 = 32 W
- Subtotal: 72 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **108 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Chemical Move Cylinder** | Square | Move | Affect | T2 | Chemical | Thermal | Cylinder | Self | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Chemical Move Cylinder",
  "summary": "Repositions chemical thermal flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions.",
  "effect_description": "Repositions chemical thermal flux as a column volume at self reach, targeting one object with immediate discharge by changing existing conditions. A square move/affect recipe that channels chemical discipline into thermal output. It applies a cylinder pattern against object across self reach with immediate persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Chemical",
  "output_mode": "Thermal",
  "pattern": "Cylinder",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 5,
    "core_discipline_w": 40,
    "pattern_w": 20,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 72,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 108,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
