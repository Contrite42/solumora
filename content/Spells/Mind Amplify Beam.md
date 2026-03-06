# Mind Amplify Beam

Boosts mind photonic flux as a directed line at line-of-sight reach, targeting the caster with conditional hold with active regulation while it runs.

## Effect

Boosts mind photonic flux as a directed line at line-of-sight reach, targeting the caster with conditional hold with active regulation while it runs. A circle amplify/control recipe that channels mind discipline into photonic output. It applies a beam pattern against self across line-of-sight reach with conditional persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Photonic | +60 W premium |
| Pattern | Beam | +5 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Conditional | +20 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 80 + 20 + 0 + 60 = 165 W
- Subtotal: 1540 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **4574 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Amplify Beam** | Circle | Amplify | Control | T6 | Mind | Photonic | Beam | Line-of-Sight | Conditional | Self |

## AI Spell Data

```json
{
  "name": "Mind Amplify Beam",
  "summary": "Boosts mind photonic flux as a directed line at line-of-sight reach, targeting the caster with conditional hold with active regulation while it runs.",
  "effect_description": "Boosts mind photonic flux as a directed line at line-of-sight reach, targeting the caster with conditional hold with active regulation while it runs. A circle amplify/control recipe that channels mind discipline into photonic output. It applies a beam pattern against self across line-of-sight reach with conditional persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Photonic",
  "pattern": "Beam",
  "reach": "Line-of-Sight",
  "persistence": "Conditional",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 5,
    "reach_w": 80,
    "persistence_w": 20,
    "target_w": 0,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 1540,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 4574,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
