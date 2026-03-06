# Soul Ward Field

establishes soul energy in a field volume by changing existing conditions

## Effect

The caster inscribes a sigil that establishes soul energy in a field volume by changing existing conditions. Effect range: long. Persistence: latched.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Ward | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Field | +60 W |
| Reach | Long | +40 W |
| Persistence | Latched | +40 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 40 + 40 + 35 + 30 = 205 W
- Subtotal: 4330 W
- Hook/Mode complexity multiplier: x2.0
- Hook/Mode flat addition: +0 W
- Total: **8660 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Ward Field** | Circle | Ward | Affect | T6 | Soul | Raw | Field | Long | Latched | Group |

## AI Spell Data

```json
{
  "name": "Soul Ward Field",
  "summary": "establishes soul energy in a field volume by changing existing conditions",
  "effect_description": "The caster inscribes a sigil that establishes soul energy in a field volume by changing existing conditions. Effect range: long. Persistence: latched.",
  "hook": "Ward",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Field",
  "reach": "Long",
  "persistence": "Latched",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 60,
    "reach_w": 40,
    "persistence_w": 40,
    "target_w": 35,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4330,
    "hook_mode_multiplier": 2.0,
    "hook_mode_flat_w": 0,
    "total_w": 8660,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
