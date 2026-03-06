# Mind Transform Sphere

reconfigures mind energy in a spherical envelope by creating a fresh flux expression

## Effect

The caster inscribes a sigil that reconfigures mind energy in a spherical envelope by creating a fresh flux expression. Effect range: long. Persistence: conditional.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Sphere | +30 W |
| Reach | Long | +40 W |
| Persistence | Conditional | +20 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 40 + 20 + 60 + 30 = 180 W
- Subtotal: 1555 W
- Hook/Mode complexity multiplier: x1.9549999999999998
- Hook/Mode flat addition: +0 W
- Total: **3040 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Transform Sphere** | Circle | Transform | Create | T5 | Mind | Raw | Sphere | Long | Conditional | Filter |

## AI Spell Data

```json
{
  "name": "Mind Transform Sphere",
  "summary": "reconfigures mind energy in a spherical envelope by creating a fresh flux expression",
  "effect_description": "The caster inscribes a sigil that reconfigures mind energy in a spherical envelope by creating a fresh flux expression. Effect range: long. Persistence: conditional.",
  "hook": "Transform",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Sphere",
  "reach": "Long",
  "persistence": "Conditional",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 30,
    "reach_w": 40,
    "persistence_w": 20,
    "target_w": 60,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1555,
    "hook_mode_multiplier": 1.9549999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 3040,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
