# Soul Move Cylinder

Repositions soul kinetic flux as a column volume at long reach, targeting a grouped cluster with immediate discharge by changing existing conditions.

## Effect

Repositions soul kinetic flux as a column volume at long reach, targeting a grouped cluster with immediate discharge by changing existing conditions. A circle move/affect recipe that channels soul discipline into kinetic output. It applies a cylinder pattern against group across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Kinetic | +60 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 40 + 0 + 35 + 60 = 155 W
- Subtotal: 4280 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **6420 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Move Cylinder** | Circle | Move | Affect | T6 | Soul | Kinetic | Cylinder | Long | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Soul Move Cylinder",
  "summary": "Repositions soul kinetic flux as a column volume at long reach, targeting a grouped cluster with immediate discharge by changing existing conditions.",
  "effect_description": "Repositions soul kinetic flux as a column volume at long reach, targeting a grouped cluster with immediate discharge by changing existing conditions. A circle move/affect recipe that channels soul discipline into kinetic output. It applies a cylinder pattern against group across long reach with immediate persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Kinetic",
  "pattern": "Cylinder",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 20,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 4280,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 6420,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
