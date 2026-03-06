# Mind Counter Sphere

disrupts mind energy in a spherical envelope with active regulation while it runs

## Effect

The caster inscribes a sigil that disrupts mind energy in a spherical envelope with active regulation while it runs. Effect range: line-of-sight. Persistence: timed long.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Sphere | +30 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 80 + 25 + 35 + 30 = 200 W
- Subtotal: 1575 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **5528 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Counter Sphere** | Circle | Counter | Control | T6 | Mind | Raw | Sphere | Line-of-Sight | Timed Long | Group |

## AI Spell Data

```json
{
  "name": "Mind Counter Sphere",
  "summary": "disrupts mind energy in a spherical envelope with active regulation while it runs",
  "effect_description": "The caster inscribes a sigil that disrupts mind energy in a spherical envelope with active regulation while it runs. Effect range: line-of-sight. Persistence: timed long.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Sphere",
  "reach": "Line-of-Sight",
  "persistence": "Timed Long",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 30,
    "reach_w": 80,
    "persistence_w": 25,
    "target_w": 35,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1575,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 5528,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
