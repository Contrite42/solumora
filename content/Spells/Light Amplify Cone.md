# Light Amplify Cone

Boosts light photonic flux as a fan spread at long reach, targeting one individual with immediate discharge by changing existing conditions.

## Effect

Boosts light photonic flux as a fan spread at long reach, targeting one individual with immediate discharge by changing existing conditions. A circle amplify/affect recipe that channels light discipline into photonic output. It applies a cone pattern against individual across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Light | x3 multiplier |
| Output Mode | Photonic | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 3 = 165 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 40 + 0 + 8 + 0 = 58 W
- Subtotal: 223 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **491 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Light Amplify Cone** | Circle | Amplify | Affect | T4 | Light | Photonic | Cone | Long | Immediate | Individual |

## AI Spell Data

```json
{
  "name": "Light Amplify Cone",
  "summary": "Boosts light photonic flux as a fan spread at long reach, targeting one individual with immediate discharge by changing existing conditions.",
  "effect_description": "Boosts light photonic flux as a fan spread at long reach, targeting one individual with immediate discharge by changing existing conditions. A circle amplify/affect recipe that channels light discipline into photonic output. It applies a cone pattern against individual across long reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Light",
  "output_mode": "Photonic",
  "pattern": "Cone",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 3,
    "core_discipline_w": 165,
    "pattern_w": 10,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 223,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 491,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
