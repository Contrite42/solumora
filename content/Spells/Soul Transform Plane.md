# Soul Transform Plane

Reconfigures soul flux as a planar spread at line-of-sight reach, targeting a filtered selection with immediate discharge by changing existing conditions.

## Effect

Reconfigures soul flux as a planar spread at line-of-sight reach, targeting a filtered selection with immediate discharge by changing existing conditions. A circle transform/affect recipe that channels soul discipline into soul output. It applies a plane pattern against filter across line-of-sight reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 80 + 0 + 60 + 0 = 140 W
- Subtotal: 4265 W
- Hook/Mode complexity multiplier: x1.7
- Hook/Mode flat addition: +0 W
- Total: **7250 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Transform Plane** | Circle | Transform | Affect | T6 | Soul | Soul | Plane | Line-of-Sight | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Soul Transform Plane",
  "summary": "Reconfigures soul flux as a planar spread at line-of-sight reach, targeting a filtered selection with immediate discharge by changing existing conditions.",
  "effect_description": "Reconfigures soul flux as a planar spread at line-of-sight reach, targeting a filtered selection with immediate discharge by changing existing conditions. A circle transform/affect recipe that channels soul discipline into soul output. It applies a plane pattern against filter across line-of-sight reach with immediate persistence.",
  "hook": "Transform",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Plane",
  "reach": "Line-of-Sight",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 80,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4265,
    "hook_mode_multiplier": 1.7,
    "hook_mode_flat_w": 0,
    "total_w": 7250,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
