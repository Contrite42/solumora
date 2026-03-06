# Sound Filter Plane

Screens sound sonic flux as a planar spread at self reach, targeting the caster with immediate discharge by changing existing conditions.

## Effect

Screens sound sonic flux as a planar spread at self reach, targeting the caster with immediate discharge by changing existing conditions. A square filter/affect recipe that channels sound discipline into sonic output. It applies a plane pattern against self across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Sonic | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 4 = 32 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 0 + 0 = 0 W
- Subtotal: 32 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **51 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Sound Filter Plane** | Square | Filter | Affect | T2 | Sound | Sonic | Plane | Self | Immediate | Self |

## AI Spell Data

```json
{
  "name": "Sound Filter Plane",
  "summary": "Screens sound sonic flux as a planar spread at self reach, targeting the caster with immediate discharge by changing existing conditions.",
  "effect_description": "Screens sound sonic flux as a planar spread at self reach, targeting the caster with immediate discharge by changing existing conditions. A square filter/affect recipe that channels sound discipline into sonic output. It applies a plane pattern against self across self reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Sound",
  "output_mode": "Sonic",
  "pattern": "Plane",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 4,
    "core_discipline_w": 32,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 32,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 51,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
