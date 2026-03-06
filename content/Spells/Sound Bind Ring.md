# Sound Bind Ring

Anchors sound sonic flux as a ring perimeter at self reach, targeting one object with immediate discharge by changing existing conditions.

## Effect

Anchors sound sonic flux as a ring perimeter at self reach, targeting one object with immediate discharge by changing existing conditions. A square bind/affect recipe that channels sound discipline into sonic output. It applies a ring pattern against object across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Bind | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Sonic | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 4 = 32 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 0 + 0 + 2 + 0 = 17 W
- Subtotal: 49 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **78 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Sound Bind Ring** | Square | Bind | Affect | T2 | Sound | Sonic | Ring | Self | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Sound Bind Ring",
  "summary": "Anchors sound sonic flux as a ring perimeter at self reach, targeting one object with immediate discharge by changing existing conditions.",
  "effect_description": "Anchors sound sonic flux as a ring perimeter at self reach, targeting one object with immediate discharge by changing existing conditions. A square bind/affect recipe that channels sound discipline into sonic output. It applies a ring pattern against object across self reach with immediate persistence.",
  "hook": "Bind",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Sound",
  "output_mode": "Sonic",
  "pattern": "Ring",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 4,
    "core_discipline_w": 32,
    "pattern_w": 15,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 49,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 78,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
