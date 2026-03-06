# MindStorm

A reality-altering effect that releases mind energy in a field volume with active regulation while it runs

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that releases mind energy in a field volume with active regulation while it runs. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Field | +60 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Permanent | +400 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 80 + 400 + 5 + 30 = 575 W
- Subtotal: 1950 W
- Hook/Mode complexity multiplier: x1.35
- Hook/Mode flat addition: +0 W
- Total: **2632 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **MindStorm** | Circle | Emit | Control | T5 | Mind | Raw | Field | Line-of-Sight | Permanent | Surface |

## AI Spell Data

```json
{
  "name": "MindStorm",
  "summary": "A reality-altering effect that releases mind energy in a field volume with active regulation while it runs",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that releases mind energy in a field volume with active regulation while it runs. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Emit",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Field",
  "reach": "Line-of-Sight",
  "persistence": "Permanent",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 60,
    "reach_w": 80,
    "persistence_w": 400,
    "target_w": 5,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1950,
    "hook_mode_multiplier": 1.35,
    "hook_mode_flat_w": 0,
    "total_w": 2632,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
