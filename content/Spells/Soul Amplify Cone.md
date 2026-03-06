# Soul Amplify Cone

Boosts soul flux as a fan spread at self reach, targeting one individual with sustained channeling by creating a fresh flux expression.

## Effect

Boosts soul flux as a fan spread at self reach, targeting one individual with sustained channeling by creating a fresh flux expression. A circle amplify/create recipe that channels soul discipline into soul output. It applies a cone pattern against individual across self reach with sustained persistence. The sustained window is set to 50 minutes.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Sustained (50 min planned active window) | +50 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 50 + 8 + 0 = 68 W
- Subtotal: 4193 W
- Hook/Mode complexity multiplier: x2.53
- Hook/Mode flat addition: +0 W
- Total: **10608 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Amplify Cone** | Circle | Amplify | Create | T6 | Soul | Soul | Cone | Self | Sustained | Individual |

## AI Spell Data

```json
{
  "name": "Soul Amplify Cone",
  "summary": "Boosts soul flux as a fan spread at self reach, targeting one individual with sustained channeling by creating a fresh flux expression.",
  "effect_description": "Boosts soul flux as a fan spread at self reach, targeting one individual with sustained channeling by creating a fresh flux expression. A circle amplify/create recipe that channels soul discipline into soul output. It applies a cone pattern against individual across self reach with sustained persistence. The sustained window is set to 50 minutes.",
  "hook": "Amplify",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Sustained",
  "target_spec": "Individual",
  "sustained_minutes": 50,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 50,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4193,
    "hook_mode_multiplier": 2.53,
    "hook_mode_flat_w": 0,
    "total_w": 10608,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
