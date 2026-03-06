# MindRend

A reality-altering effect that releases mind energy in a column volume by changing existing conditions

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that releases mind energy in a column volume by changing existing conditions. Effect range: long. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Long | +40 W |
| Persistence | Permanent | +400 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 40 + 400 + 60 + 30 = 550 W
- Subtotal: 1925 W
- Hook/Mode complexity multiplier: x1.0
- Hook/Mode flat addition: +0 W
- Total: **1925 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **MindRend** | Circle | Emit | Affect | T5 | Mind | Raw | Cylinder | Long | Permanent | Filter |

## AI Spell Data

```json
{
  "name": "MindRend",
  "summary": "A reality-altering effect that releases mind energy in a column volume by changing existing conditions",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that releases mind energy in a column volume by changing existing conditions. Effect range: long. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Emit",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Cylinder",
  "reach": "Long",
  "persistence": "Permanent",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 20,
    "reach_w": 40,
    "persistence_w": 400,
    "target_w": 60,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1925,
    "hook_mode_multiplier": 1.0,
    "hook_mode_flat_w": 0,
    "total_w": 1925,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
