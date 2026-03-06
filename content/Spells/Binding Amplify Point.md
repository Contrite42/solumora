# Binding Amplify Point

Boosts binding constraint flux as a point focus at long reach, targeting the caster with permanent inscription by creating a fresh flux expression.

## Effect

Boosts binding constraint flux as a point focus at long reach, targeting the caster with permanent inscription by creating a fresh flux expression. A circle amplify/create recipe that channels binding discipline into constraint output. It applies a point pattern against self across long reach with permanent persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Long | +40 W |
| Persistence | Permanent | +400 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 10 = 550 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 40 + 400 + 0 + 0 = 440 W
- Subtotal: 990 W
- Hook/Mode complexity multiplier: x2.53
- Hook/Mode flat addition: +0 W
- Total: **2505 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Binding Amplify Point** | Circle | Amplify | Create | T5 | Binding | Constraint | Point | Long | Permanent | Self |

## AI Spell Data

```json
{
  "name": "Binding Amplify Point",
  "summary": "Boosts binding constraint flux as a point focus at long reach, targeting the caster with permanent inscription by creating a fresh flux expression.",
  "effect_description": "Boosts binding constraint flux as a point focus at long reach, targeting the caster with permanent inscription by creating a fresh flux expression. A circle amplify/create recipe that channels binding discipline into constraint output. It applies a point pattern against self across long reach with permanent persistence.",
  "hook": "Amplify",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Point",
  "reach": "Long",
  "persistence": "Permanent",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 10,
    "core_discipline_w": 550,
    "pattern_w": 0,
    "reach_w": 40,
    "persistence_w": 400,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 990,
    "hook_mode_multiplier": 2.53,
    "hook_mode_flat_w": 0,
    "total_w": 2505,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
