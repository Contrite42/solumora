# EchoShatter

A reality-altering effect that disrupts raw energy in a field volume by changing existing conditions

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that disrupts raw energy in a field volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Permanent | +400 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 1 = 55 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 80 + 400 + 5 + 0 = 545 W
- Subtotal: 600 W
- Hook/Mode complexity multiplier: x2.6
- Hook/Mode flat addition: +0 W
- Total: **1560 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **EchoShatter** | Circle | Counter | Affect | T5 | Raw | Raw | Field | Line-of-Sight | Permanent | Surface |

## AI Spell Data

```json
{
  "name": "EchoShatter",
  "summary": "A reality-altering effect that disrupts raw energy in a field volume by changing existing conditions",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that disrupts raw energy in a field volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Counter",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Field",
  "reach": "Line-of-Sight",
  "persistence": "Permanent",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 1,
    "core_discipline_w": 55,
    "pattern_w": 60,
    "reach_w": 80,
    "persistence_w": 400,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 600,
    "hook_mode_multiplier": 2.6,
    "hook_mode_flat_w": 0,
    "total_w": 1560,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
