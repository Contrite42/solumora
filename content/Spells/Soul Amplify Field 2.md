# Soul Amplify Field 2

Boosts soul flux as a field volume at line-of-sight reach, targeting one individual with immediate discharge with active regulation while it runs.

## Effect

Boosts soul flux as a field volume at line-of-sight reach, targeting one individual with immediate discharge with active regulation while it runs. A circle amplify/control recipe that channels soul discipline into soul output. It applies a field pattern against individual across line-of-sight reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Immediate | +0 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 80 + 0 + 8 + 0 = 148 W
- Subtotal: 4273 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **12691 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Amplify Field 2** | Circle | Amplify | Control | T6 | Soul | Soul | Field | Line-of-Sight | Immediate | Individual |

## AI Spell Data

```json
{
  "name": "Soul Amplify Field 2",
  "summary": "Boosts soul flux as a field volume at line-of-sight reach, targeting one individual with immediate discharge with active regulation while it runs.",
  "effect_description": "Boosts soul flux as a field volume at line-of-sight reach, targeting one individual with immediate discharge with active regulation while it runs. A circle amplify/control recipe that channels soul discipline into soul output. It applies a field pattern against individual across line-of-sight reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Field",
  "reach": "Line-of-Sight",
  "persistence": "Immediate",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 60,
    "reach_w": 80,
    "persistence_w": 0,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4273,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 12691,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
