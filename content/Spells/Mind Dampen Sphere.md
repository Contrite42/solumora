# Mind Dampen Sphere

Reduces mind neuro flux as a spherical envelope at long reach, targeting a filtered selection with conditional hold with active regulation while it runs.

## Effect

Reduces mind neuro flux as a spherical envelope at long reach, targeting a filtered selection with conditional hold with active regulation while it runs. A circle dampen/control recipe that channels mind discipline into neuro output. It applies a sphere pattern against filter across long reach with conditional persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Long | +40 W |
| Persistence | Conditional | +20 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 40 + 20 + 60 + 0 = 150 W
- Subtotal: 1525 W
- Hook/Mode complexity multiplier: x2.565
- Hook/Mode flat addition: +0 W
- Total: **3912 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Dampen Sphere** | Circle | Dampen | Control | T5 | Mind | Neuro | Sphere | Long | Conditional | Filter |

## AI Spell Data

```json
{
  "name": "Mind Dampen Sphere",
  "summary": "Reduces mind neuro flux as a spherical envelope at long reach, targeting a filtered selection with conditional hold with active regulation while it runs.",
  "effect_description": "Reduces mind neuro flux as a spherical envelope at long reach, targeting a filtered selection with conditional hold with active regulation while it runs. A circle dampen/control recipe that channels mind discipline into neuro output. It applies a sphere pattern against filter across long reach with conditional persistence.",
  "hook": "Dampen",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Neuro",
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
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1525,
    "hook_mode_multiplier": 2.565,
    "hook_mode_flat_w": 0,
    "total_w": 3912,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
