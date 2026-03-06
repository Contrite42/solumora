# Soul Trigger Sphere

arms soul energy in a spherical envelope by creating a fresh flux expression

## Effect

The caster inscribes a sigil that arms soul energy in a spherical envelope by creating a fresh flux expression. Effect range: medium. Persistence: permanent.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Trigger | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Sphere | +30 W |
| Reach | Medium | +15 W |
| Persistence | Permanent | +400 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 15 + 400 + 35 + 30 = 510 W
- Subtotal: 4635 W
- Hook/Mode complexity multiplier: x2.07
- Hook/Mode flat addition: +0 W
- Total: **9594 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Trigger Sphere** | Circle | Trigger | Create | T6 | Soul | Raw | Sphere | Medium | Permanent | Group |

## AI Spell Data

```json
{
  "name": "Soul Trigger Sphere",
  "summary": "arms soul energy in a spherical envelope by creating a fresh flux expression",
  "effect_description": "The caster inscribes a sigil that arms soul energy in a spherical envelope by creating a fresh flux expression. Effect range: medium. Persistence: permanent.",
  "hook": "Trigger",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Sphere",
  "reach": "Medium",
  "persistence": "Permanent",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 30,
    "reach_w": 15,
    "persistence_w": 400,
    "target_w": 35,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4635,
    "hook_mode_multiplier": 2.07,
    "hook_mode_flat_w": 0,
    "total_w": 9594,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
