# Soul Amplify Point 2

Boosts soul flux as a point focus at short reach, targeting one individual with short timed hold by changing existing conditions.

## Effect

Boosts soul flux as a point focus at short reach, targeting one individual with short timed hold by changing existing conditions. A circle amplify/affect recipe that channels soul discipline into soul output. It applies a point pattern against individual across short reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Short | +5 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 5 + 5 + 8 + 0 = 18 W
- Subtotal: 4143 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **9115 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Amplify Point 2** | Circle | Amplify | Affect | T6 | Soul | Soul | Point | Short | Timed Short | Individual |

## AI Spell Data

```json
{
  "name": "Soul Amplify Point 2",
  "summary": "Boosts soul flux as a point focus at short reach, targeting one individual with short timed hold by changing existing conditions.",
  "effect_description": "Boosts soul flux as a point focus at short reach, targeting one individual with short timed hold by changing existing conditions. A circle amplify/affect recipe that channels soul discipline into soul output. It applies a point pattern against individual across short reach with timed short persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Point",
  "reach": "Short",
  "persistence": "Timed Short",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 5,
    "persistence_w": 5,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4143,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 9115,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
