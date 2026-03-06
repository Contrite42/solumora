# Soul Ward Plane

Establishes soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge by changing existing conditions.

## Effect

Establishes soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge by changing existing conditions. A circle ward/affect recipe that channels soul discipline into soul output. It applies a plane pattern against object across line-of-sight reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Ward | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 80 + 0 + 2 + 0 = 82 W
- Subtotal: 4207 W
- Hook/Mode complexity multiplier: x2.0
- Hook/Mode flat addition: +0 W
- Total: **8414 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Ward Plane** | Circle | Ward | Affect | T6 | Soul | Soul | Plane | Line-of-Sight | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Soul Ward Plane",
  "summary": "Establishes soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge by changing existing conditions.",
  "effect_description": "Establishes soul flux as a planar spread at line-of-sight reach, targeting one object with immediate discharge by changing existing conditions. A circle ward/affect recipe that channels soul discipline into soul output. It applies a plane pattern against object across line-of-sight reach with immediate persistence.",
  "hook": "Ward",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Plane",
  "reach": "Line-of-Sight",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 80,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4207,
    "hook_mode_multiplier": 2.0,
    "hook_mode_flat_w": 0,
    "total_w": 8414,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
