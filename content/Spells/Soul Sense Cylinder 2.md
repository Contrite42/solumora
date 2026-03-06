# Soul Sense Cylinder 2

Detects soul flux as a column volume at medium reach, targeting a marked signature with immediate discharge by creating a fresh flux expression.

## Effect

Detects soul flux as a column volume at medium reach, targeting a marked signature with immediate discharge by creating a fresh flux expression. A circle sense/create recipe that channels soul discipline into soul output. It applies a cylinder pattern against marked across medium reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Medium | +15 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 15 + 0 + 15 + 0 = 50 W
- Subtotal: 4175 W
- Hook/Mode complexity multiplier: x2.07
- Hook/Mode flat addition: +0 W
- Total: **8642 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Sense Cylinder 2** | Circle | Sense | Create | T6 | Soul | Soul | Cylinder | Medium | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Soul Sense Cylinder 2",
  "summary": "Detects soul flux as a column volume at medium reach, targeting a marked signature with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Detects soul flux as a column volume at medium reach, targeting a marked signature with immediate discharge by creating a fresh flux expression. A circle sense/create recipe that channels soul discipline into soul output. It applies a cylinder pattern against marked across medium reach with immediate persistence.",
  "hook": "Sense",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cylinder",
  "reach": "Medium",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 20,
    "reach_w": 15,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4175,
    "hook_mode_multiplier": 2.07,
    "hook_mode_flat_w": 0,
    "total_w": 8642,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
