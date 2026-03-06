# Soul Sense Sphere

detects soul energy in a spherical envelope with active regulation while it runs

## Effect

The caster inscribes a sigil that detects soul energy in a spherical envelope with active regulation while it runs. Effect range: long. Persistence: permanent.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Sphere | +30 W |
| Reach | Long | +40 W |
| Persistence | Permanent | +400 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 40 + 400 + 35 + 30 = 535 W
- Subtotal: 4660 W
- Hook/Mode complexity multiplier: x2.43
- Hook/Mode flat addition: +0 W
- Total: **11324 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Sense Sphere** | Circle | Sense | Control | T6 | Soul | Raw | Sphere | Long | Permanent | Group |

## AI Spell Data

```json
{
  "name": "Soul Sense Sphere",
  "summary": "detects soul energy in a spherical envelope with active regulation while it runs",
  "effect_description": "The caster inscribes a sigil that detects soul energy in a spherical envelope with active regulation while it runs. Effect range: long. Persistence: permanent.",
  "hook": "Sense",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Sphere",
  "reach": "Long",
  "persistence": "Permanent",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 30,
    "reach_w": 40,
    "persistence_w": 400,
    "target_w": 35,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4660,
    "hook_mode_multiplier": 2.43,
    "hook_mode_flat_w": 0,
    "total_w": 11324,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
