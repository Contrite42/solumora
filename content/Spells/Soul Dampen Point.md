# Soul Dampen Point

Reduces soul flux as a point focus at long reach, targeting one object with immediate discharge by changing existing conditions.

## Effect

Reduces soul flux as a point focus at long reach, targeting one object with immediate discharge by changing existing conditions. A circle dampen/affect recipe that channels soul discipline into soul output. It applies a point pattern against object across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 40 + 0 + 2 + 0 = 42 W
- Subtotal: 4167 W
- Hook/Mode complexity multiplier: x1.9
- Hook/Mode flat addition: +0 W
- Total: **7917 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Dampen Point** | Circle | Dampen | Affect | T6 | Soul | Soul | Point | Long | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Soul Dampen Point",
  "summary": "Reduces soul flux as a point focus at long reach, targeting one object with immediate discharge by changing existing conditions.",
  "effect_description": "Reduces soul flux as a point focus at long reach, targeting one object with immediate discharge by changing existing conditions. A circle dampen/affect recipe that channels soul discipline into soul output. It applies a point pattern against object across long reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Point",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4167,
    "hook_mode_multiplier": 1.9,
    "hook_mode_flat_w": 0,
    "total_w": 7917,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
