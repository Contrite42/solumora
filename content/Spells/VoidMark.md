# VoidMark

A reality-altering effect that releases soul energy in a column volume by changing existing conditions

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that releases soul energy in a column volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Permanent | +400 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 80 + 400 + 60 + 30 = 590 W
- Subtotal: 4715 W
- Hook/Mode complexity multiplier: x1.0
- Hook/Mode flat addition: +0 W
- Total: **4715 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **VoidMark** | Circle | Emit | Affect | T6 | Soul | Raw | Cylinder | Line-of-Sight | Permanent | Filter |

## AI Spell Data

```json
{
  "name": "VoidMark",
  "summary": "A reality-altering effect that releases soul energy in a column volume by changing existing conditions",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that releases soul energy in a column volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Emit",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Cylinder",
  "reach": "Line-of-Sight",
  "persistence": "Permanent",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 20,
    "reach_w": 80,
    "persistence_w": 400,
    "target_w": 60,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4715,
    "hook_mode_multiplier": 1.0,
    "hook_mode_flat_w": 0,
    "total_w": 4715,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
