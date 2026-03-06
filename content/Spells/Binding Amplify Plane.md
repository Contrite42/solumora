# Binding Amplify Plane

Boosts binding constraint flux as a planar spread at touch reach, targeting a filtered selection with long timed hold with active regulation while it runs.

## Effect

Boosts binding constraint flux as a planar spread at touch reach, targeting a filtered selection with long timed hold with active regulation while it runs. A circle amplify/control recipe that channels binding discipline into constraint output. It applies a plane pattern against filter across touch reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Touch | +2 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 10 = 550 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 2 + 25 + 60 + 0 = 87 W
- Subtotal: 637 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **1892 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Binding Amplify Plane** | Circle | Amplify | Control | T5 | Binding | Constraint | Plane | Touch | Timed Long | Filter |

## AI Spell Data

```json
{
  "name": "Binding Amplify Plane",
  "summary": "Boosts binding constraint flux as a planar spread at touch reach, targeting a filtered selection with long timed hold with active regulation while it runs.",
  "effect_description": "Boosts binding constraint flux as a planar spread at touch reach, targeting a filtered selection with long timed hold with active regulation while it runs. A circle amplify/control recipe that channels binding discipline into constraint output. It applies a plane pattern against filter across touch reach with timed long persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Plane",
  "reach": "Touch",
  "persistence": "Timed Long",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 10,
    "core_discipline_w": 550,
    "pattern_w": 0,
    "reach_w": 2,
    "persistence_w": 25,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 637,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 1892,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
