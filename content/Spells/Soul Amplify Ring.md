# Soul Amplify Ring

boosts soul energy in a ring perimeter by changing existing conditions

## Effect

The caster inscribes a sigil that boosts soul energy in a ring perimeter by changing existing conditions. Effect range: medium. Persistence: conditional.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Ring | +15 W |
| Reach | Medium | +15 W |
| Persistence | Conditional | +20 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 15 + 20 + 8 + 30 = 88 W
- Subtotal: 4213 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **9269 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Amplify Ring** | Circle | Amplify | Affect | T6 | Soul | Raw | Ring | Medium | Conditional | Individual |

## AI Spell Data

```json
{
  "name": "Soul Amplify Ring",
  "summary": "boosts soul energy in a ring perimeter by changing existing conditions",
  "effect_description": "The caster inscribes a sigil that boosts soul energy in a ring perimeter by changing existing conditions. Effect range: medium. Persistence: conditional.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Ring",
  "reach": "Medium",
  "persistence": "Conditional",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 15,
    "reach_w": 15,
    "persistence_w": 20,
    "target_w": 8,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4213,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 9269,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
