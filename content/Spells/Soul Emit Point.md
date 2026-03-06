# Soul Emit Point

Releases soul kinetic flux as a point focus at self reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression.

## Effect

Releases soul kinetic flux as a point focus at self reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression. A pentagon emit/create recipe that channels soul discipline into kinetic output. It applies a point pattern against surface across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Kinetic | +60 W premium |
| Pattern | Point | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 5 + 60 = 65 W
- Subtotal: 1565 W
- Hook/Mode complexity multiplier: x1.15
- Hook/Mode flat addition: +0 W
- Total: **1800 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Emit Point** | Pentagon | Emit | Create | T5 | Soul | Kinetic | Point | Self | Immediate | Surface |

## AI Spell Data

```json
{
  "name": "Soul Emit Point",
  "summary": "Releases soul kinetic flux as a point focus at self reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Releases soul kinetic flux as a point focus at self reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression. A pentagon emit/create recipe that channels soul discipline into kinetic output. It applies a point pattern against surface across self reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Create",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Kinetic",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 5,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 1565,
    "hook_mode_multiplier": 1.15,
    "hook_mode_flat_w": 0,
    "total_w": 1800,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
