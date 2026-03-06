# Soul Sense Sphere

Detects soul shock flux as a spherical envelope at long reach, targeting one individual with conditional hold with active regulation while it runs.

## Effect

Detects soul shock flux as a spherical envelope at long reach, targeting one individual with conditional hold with active regulation while it runs. A circle sense/control recipe that channels soul discipline into shock output. It applies a sphere pattern against individual across long reach with conditional persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Shock | +60 W premium |
| Pattern | Sphere | +30 W |
| Reach | Long | +40 W |
| Persistence | Conditional | +20 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 40 + 20 + 8 + 60 = 158 W
- Subtotal: 4283 W
- Hook/Mode complexity multiplier: x2.43
- Hook/Mode flat addition: +0 W
- Total: **10408 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Sense Sphere** | Circle | Sense | Control | T6 | Soul | Shock | Sphere | Long | Conditional | Individual |

## AI Spell Data

```json
{
  "name": "Soul Sense Sphere",
  "summary": "Detects soul shock flux as a spherical envelope at long reach, targeting one individual with conditional hold with active regulation while it runs.",
  "effect_description": "Detects soul shock flux as a spherical envelope at long reach, targeting one individual with conditional hold with active regulation while it runs. A circle sense/control recipe that channels soul discipline into shock output. It applies a sphere pattern against individual across long reach with conditional persistence.",
  "hook": "Sense",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Shock",
  "pattern": "Sphere",
  "reach": "Long",
  "persistence": "Conditional",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 30,
    "reach_w": 40,
    "persistence_w": 20,
    "target_w": 8,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 4283,
    "hook_mode_multiplier": 2.43,
    "hook_mode_flat_w": 0,
    "total_w": 10408,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
