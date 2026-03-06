# Mind Trigger Cone

Arms mind neuro flux as a fan spread at long reach, targeting a marked signature with immediate discharge with active regulation while it runs.

## Effect

Arms mind neuro flux as a fan spread at long reach, targeting a marked signature with immediate discharge with active regulation while it runs. A pentagon trigger/control recipe that channels mind discipline into neuro output. It applies a cone pattern against marked across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Trigger | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 25 = 500 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 40 + 0 + 15 + 0 = 65 W
- Subtotal: 565 W
- Hook/Mode complexity multiplier: x2.43
- Hook/Mode flat addition: +0 W
- Total: **1373 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Trigger Cone** | Pentagon | Trigger | Control | T5 | Mind | Neuro | Cone | Long | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Mind Trigger Cone",
  "summary": "Arms mind neuro flux as a fan spread at long reach, targeting a marked signature with immediate discharge with active regulation while it runs.",
  "effect_description": "Arms mind neuro flux as a fan spread at long reach, targeting a marked signature with immediate discharge with active regulation while it runs. A pentagon trigger/control recipe that channels mind discipline into neuro output. It applies a cone pattern against marked across long reach with immediate persistence.",
  "hook": "Trigger",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Cone",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 25,
    "core_discipline_w": 500,
    "pattern_w": 10,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 565,
    "hook_mode_multiplier": 2.43,
    "hook_mode_flat_w": 0,
    "total_w": 1373,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
