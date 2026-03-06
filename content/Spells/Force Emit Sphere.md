# Force Emit Sphere

Releases force kinetic flux as a spherical envelope at self reach, targeting a filtered selection with immediate discharge by changing existing conditions.

## Effect

Releases force kinetic flux as a spherical envelope at self reach, targeting a filtered selection with immediate discharge by changing existing conditions. A square emit/affect recipe that channels force discipline into kinetic output. It applies a sphere pattern against filter across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Force | x2 multiplier |
| Output Mode | Kinetic | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 2 = 16 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 0 + 0 + 60 + 0 = 90 W
- Subtotal: 106 W
- Hook/Mode complexity multiplier: x1.0
- Hook/Mode flat addition: +0 W
- Total: **106 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Force Emit Sphere** | Square | Emit | Affect | T2 | Force | Kinetic | Sphere | Self | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Force Emit Sphere",
  "summary": "Releases force kinetic flux as a spherical envelope at self reach, targeting a filtered selection with immediate discharge by changing existing conditions.",
  "effect_description": "Releases force kinetic flux as a spherical envelope at self reach, targeting a filtered selection with immediate discharge by changing existing conditions. A square emit/affect recipe that channels force discipline into kinetic output. It applies a sphere pattern against filter across self reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Force",
  "output_mode": "Kinetic",
  "pattern": "Sphere",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 2,
    "core_discipline_w": 16,
    "pattern_w": 30,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 106,
    "hook_mode_multiplier": 1.0,
    "hook_mode_flat_w": 0,
    "total_w": 106,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
