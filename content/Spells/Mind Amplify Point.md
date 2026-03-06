# Mind Amplify Point

Boosts mind neuro flux as a point focus at short reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.

## Effect

Boosts mind neuro flux as a point focus at short reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon amplify/control recipe that channels mind discipline into neuro output. It applies a point pattern against group across short reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Short | +5 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 25 = 500 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 5 + 0 + 35 + 0 = 40 W
- Subtotal: 540 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **1604 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Amplify Point** | Pentagon | Amplify | Control | T5 | Mind | Neuro | Point | Short | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Mind Amplify Point",
  "summary": "Boosts mind neuro flux as a point focus at short reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.",
  "effect_description": "Boosts mind neuro flux as a point focus at short reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon amplify/control recipe that channels mind discipline into neuro output. It applies a point pattern against group across short reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Point",
  "reach": "Short",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 25,
    "core_discipline_w": 500,
    "pattern_w": 0,
    "reach_w": 5,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 540,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 1604,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
