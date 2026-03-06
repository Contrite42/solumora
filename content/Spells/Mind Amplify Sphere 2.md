# Mind Amplify Sphere 2

Boosts mind neuro flux as a spherical envelope at long reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.

## Effect

Boosts mind neuro flux as a spherical envelope at long reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A circle amplify/affect recipe that channels mind discipline into neuro output. It applies a sphere pattern against where written across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 40 + 0 + 0 + 0 = 70 W
- Subtotal: 1445 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **3179 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Amplify Sphere 2** | Circle | Amplify | Affect | T5 | Mind | Neuro | Sphere | Long | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Mind Amplify Sphere 2",
  "summary": "Boosts mind neuro flux as a spherical envelope at long reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.",
  "effect_description": "Boosts mind neuro flux as a spherical envelope at long reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A circle amplify/affect recipe that channels mind discipline into neuro output. It applies a sphere pattern against where written across long reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Sphere",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 30,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1445,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 3179,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
