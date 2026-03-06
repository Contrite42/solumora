# EchoBreach

A reality-altering effect that disrupts raw energy in a spherical envelope with active regulation while it runs

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that disrupts raw energy in a spherical envelope with active regulation while it runs. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Permanent | +400 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 1 = 55 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 80 + 400 + 5 + 0 = 515 W
- Subtotal: 570 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **2001 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **EchoBreach** | Circle | Counter | Control | T5 | Raw | Raw | Sphere | Line-of-Sight | Permanent | Surface |

## AI Spell Data

```json
{
  "name": "EchoBreach",
  "summary": "A reality-altering effect that disrupts raw energy in a spherical envelope with active regulation while it runs",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that disrupts raw energy in a spherical envelope with active regulation while it runs. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Sphere",
  "reach": "Line-of-Sight",
  "persistence": "Permanent",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 1,
    "core_discipline_w": 55,
    "pattern_w": 30,
    "reach_w": 80,
    "persistence_w": 400,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 570,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 2001,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
