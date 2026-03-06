# Soul Shape Cylinder

Refines soul flux as a column volume at medium reach, targeting the caster with latched hold by creating a fresh flux expression.

## Effect

Refines soul flux as a column volume at medium reach, targeting the caster with latched hold by creating a fresh flux expression. A circle shape/create recipe that channels soul discipline into soul output. It applies a cylinder pattern against self across medium reach with latched persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Medium | +15 W |
| Persistence | Latched | +40 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 15 + 40 + 0 + 0 = 75 W
- Subtotal: 4200 W
- Hook/Mode complexity multiplier: x1.38
- Hook/Mode flat addition: +0 W
- Total: **5796 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Shape Cylinder** | Circle | Shape | Create | T6 | Soul | Soul | Cylinder | Medium | Latched | Self |

## AI Spell Data

```json
{
  "name": "Soul Shape Cylinder",
  "summary": "Refines soul flux as a column volume at medium reach, targeting the caster with latched hold by creating a fresh flux expression.",
  "effect_description": "Refines soul flux as a column volume at medium reach, targeting the caster with latched hold by creating a fresh flux expression. A circle shape/create recipe that channels soul discipline into soul output. It applies a cylinder pattern against self across medium reach with latched persistence.",
  "hook": "Shape",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cylinder",
  "reach": "Medium",
  "persistence": "Latched",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 20,
    "reach_w": 15,
    "persistence_w": 40,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4200,
    "hook_mode_multiplier": 1.38,
    "hook_mode_flat_w": 0,
    "total_w": 5796,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
