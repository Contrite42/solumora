# Chemical Move Cone

Repositions chemical reactive flux as a fan spread at self reach, targeting a filtered selection with immediate discharge by changing existing conditions.

## Effect

Repositions chemical reactive flux as a fan spread at self reach, targeting a filtered selection with immediate discharge by changing existing conditions. A square move/affect recipe that channels chemical discipline into reactive output. It applies a cone pattern against filter across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Reactive | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 5 = 40 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 60 + 0 = 70 W
- Subtotal: 110 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **165 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Chemical Move Cone** | Square | Move | Affect | T3 | Chemical | Reactive | Cone | Self | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Chemical Move Cone",
  "summary": "Repositions chemical reactive flux as a fan spread at self reach, targeting a filtered selection with immediate discharge by changing existing conditions.",
  "effect_description": "Repositions chemical reactive flux as a fan spread at self reach, targeting a filtered selection with immediate discharge by changing existing conditions. A square move/affect recipe that channels chemical discipline into reactive output. It applies a cone pattern against filter across self reach with immediate persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Chemical",
  "output_mode": "Reactive",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 5,
    "core_discipline_w": 40,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 110,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 165,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
