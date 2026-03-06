# Mind Filter Field

screens mind energy in a field volume by changing existing conditions

## Effect

The caster inscribes a sigil that screens mind energy in a field volume by changing existing conditions. Effect range: line-of-sight. Persistence: conditional.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Field | +60 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Conditional | +20 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 80 + 20 + 8 + 30 = 198 W
- Subtotal: 1573 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **2517 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Filter Field** | Circle | Filter | Affect | T5 | Mind | Raw | Field | Line-of-Sight | Conditional | Individual |

## AI Spell Data

```json
{
  "name": "Mind Filter Field",
  "summary": "screens mind energy in a field volume by changing existing conditions",
  "effect_description": "The caster inscribes a sigil that screens mind energy in a field volume by changing existing conditions. Effect range: line-of-sight. Persistence: conditional.",
  "hook": "Filter",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Field",
  "reach": "Line-of-Sight",
  "persistence": "Conditional",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 60,
    "reach_w": 80,
    "persistence_w": 20,
    "target_w": 8,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1573,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 2517,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
