# Soul Amplify Ring

Boosts soul thermal flux as a ring perimeter at short reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.

## Effect

Boosts soul thermal flux as a ring perimeter at short reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A pentagon amplify/create recipe that channels soul discipline into thermal output. It applies a ring pattern against filter across short reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Thermal | +60 W premium |
| Pattern | Ring | +15 W |
| Reach | Short | +5 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 5 + 0 + 60 + 60 = 140 W
- Subtotal: 1640 W
- Hook/Mode complexity multiplier: x2.53
- Hook/Mode flat addition: +0 W
- Total: **4149 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Amplify Ring** | Pentagon | Amplify | Create | T6 | Soul | Thermal | Ring | Short | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Soul Amplify Ring",
  "summary": "Boosts soul thermal flux as a ring perimeter at short reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Boosts soul thermal flux as a ring perimeter at short reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A pentagon amplify/create recipe that channels soul discipline into thermal output. It applies a ring pattern against filter across short reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Create",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Thermal",
  "pattern": "Ring",
  "reach": "Short",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 15,
    "reach_w": 5,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 1640,
    "hook_mode_multiplier": 2.53,
    "hook_mode_flat_w": 0,
    "total_w": 4149,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
