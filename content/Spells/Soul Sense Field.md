# Soul Sense Field

Detects soul reactive flux as a field volume at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs.

## Effect

Detects soul reactive flux as a field volume at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs. A pentagon sense/control recipe that channels soul discipline into reactive output. It applies a field pattern against surface across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Reactive | +60 W premium |
| Pattern | Field | +60 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 40 + 0 + 5 + 60 = 165 W
- Subtotal: 1665 W
- Hook/Mode complexity multiplier: x2.43
- Hook/Mode flat addition: +0 W
- Total: **4046 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Sense Field** | Pentagon | Sense | Control | T6 | Soul | Reactive | Field | Long | Immediate | Surface |

## AI Spell Data

```json
{
  "name": "Soul Sense Field",
  "summary": "Detects soul reactive flux as a field volume at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs.",
  "effect_description": "Detects soul reactive flux as a field volume at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs. A pentagon sense/control recipe that channels soul discipline into reactive output. It applies a field pattern against surface across long reach with immediate persistence.",
  "hook": "Sense",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Reactive",
  "pattern": "Field",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 60,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 5,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 1665,
    "hook_mode_multiplier": 2.43,
    "hook_mode_flat_w": 0,
    "total_w": 4046,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
