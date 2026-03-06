# Mind Amplify Sphere

Boosts mind shock flux as a spherical envelope at touch reach, targeting one individual with immediate discharge by creating a fresh flux expression.

## Effect

Boosts mind shock flux as a spherical envelope at touch reach, targeting one individual with immediate discharge by creating a fresh flux expression. A circle amplify/create recipe that channels mind discipline into shock output. It applies a sphere pattern against individual across touch reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Shock | +60 W premium |
| Pattern | Sphere | +30 W |
| Reach | Touch | +2 W |
| Persistence | Immediate | +0 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 2 + 0 + 8 + 60 = 100 W
- Subtotal: 1475 W
- Hook/Mode complexity multiplier: x2.53
- Hook/Mode flat addition: +0 W
- Total: **3732 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Amplify Sphere** | Circle | Amplify | Create | T5 | Mind | Shock | Sphere | Touch | Immediate | Individual |

## AI Spell Data

```json
{
  "name": "Mind Amplify Sphere",
  "summary": "Boosts mind shock flux as a spherical envelope at touch reach, targeting one individual with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Boosts mind shock flux as a spherical envelope at touch reach, targeting one individual with immediate discharge by creating a fresh flux expression. A circle amplify/create recipe that channels mind discipline into shock output. It applies a sphere pattern against individual across touch reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Shock",
  "pattern": "Sphere",
  "reach": "Touch",
  "persistence": "Immediate",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 30,
    "reach_w": 2,
    "persistence_w": 0,
    "target_w": 8,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 1475,
    "hook_mode_multiplier": 2.53,
    "hook_mode_flat_w": 0,
    "total_w": 3732,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
