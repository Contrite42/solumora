# RealityMark

A reality-altering effect that disrupts raw energy in a column volume by changing existing conditions

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that disrupts raw energy in a column volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Permanent | +400 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 1 = 55 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 80 + 400 + 35 + 0 = 535 W
- Subtotal: 590 W
- Hook/Mode complexity multiplier: x2.6
- Hook/Mode flat addition: +0 W
- Total: **1534 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **RealityMark** | Circle | Counter | Affect | T5 | Raw | Raw | Cylinder | Line-of-Sight | Permanent | Group |

## AI Spell Data

```json
{
  "name": "RealityMark",
  "summary": "A reality-altering effect that disrupts raw energy in a column volume by changing existing conditions",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that disrupts raw energy in a column volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Counter",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Cylinder",
  "reach": "Line-of-Sight",
  "persistence": "Permanent",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 1,
    "core_discipline_w": 55,
    "pattern_w": 20,
    "reach_w": 80,
    "persistence_w": 400,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 590,
    "hook_mode_multiplier": 2.6,
    "hook_mode_flat_w": 0,
    "total_w": 1534,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
