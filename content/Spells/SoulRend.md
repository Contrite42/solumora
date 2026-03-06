# SoulRend

A reality-altering effect that reconfigures raw energy in a column volume by changing existing conditions

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that reconfigures raw energy in a column volume by changing existing conditions. Effect range: long. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Long | +40 W |
| Persistence | Permanent | +400 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 1 = 55 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 40 + 400 + 5 + 0 = 465 W
- Subtotal: 520 W
- Hook/Mode complexity multiplier: x1.7
- Hook/Mode flat addition: +0 W
- Total: **884 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **SoulRend** | Circle | Transform | Affect | T4 | Raw | Raw | Cylinder | Long | Permanent | Surface |

## AI Spell Data

```json
{
  "name": "SoulRend",
  "summary": "A reality-altering effect that reconfigures raw energy in a column volume by changing existing conditions",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that reconfigures raw energy in a column volume by changing existing conditions. Effect range: long. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Transform",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Cylinder",
  "reach": "Long",
  "persistence": "Permanent",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 1,
    "core_discipline_w": 55,
    "pattern_w": 20,
    "reach_w": 40,
    "persistence_w": 400,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 520,
    "hook_mode_multiplier": 1.7,
    "hook_mode_flat_w": 0,
    "total_w": 884,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
