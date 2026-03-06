# RiftPulse

A reality-altering effect that reconfigures raw energy in a field volume with active regulation while it runs

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that reconfigures raw energy in a field volume with active regulation while it runs. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Permanent | +400 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 1 = 55 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 80 + 400 + 60 + 0 = 600 W
- Subtotal: 655 W
- Hook/Mode complexity multiplier: x2.295
- Hook/Mode flat addition: +0 W
- Total: **1503 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **RiftPulse** | Circle | Transform | Control | T5 | Raw | Raw | Field | Line-of-Sight | Permanent | Filter |

## AI Spell Data

```json
{
  "name": "RiftPulse",
  "summary": "A reality-altering effect that reconfigures raw energy in a field volume with active regulation while it runs",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that reconfigures raw energy in a field volume with active regulation while it runs. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Transform",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Field",
  "reach": "Line-of-Sight",
  "persistence": "Permanent",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 1,
    "core_discipline_w": 55,
    "pattern_w": 60,
    "reach_w": 80,
    "persistence_w": 400,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 655,
    "hook_mode_multiplier": 2.295,
    "hook_mode_flat_w": 0,
    "total_w": 1503,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
