# Soul Dampen Cone

Reduces soul photonic flux as a fan spread at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.

## Effect

Reduces soul photonic flux as a fan spread at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon dampen/control recipe that channels soul discipline into photonic output. It applies a cone pattern against group across touch reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Photonic | +60 W premium |
| Pattern | Cone | +10 W |
| Reach | Touch | +2 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 2 + 0 + 35 + 60 = 107 W
- Subtotal: 1607 W
- Hook/Mode complexity multiplier: x2.565
- Hook/Mode flat addition: +0 W
- Total: **4122 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Dampen Cone** | Pentagon | Dampen | Control | T6 | Soul | Photonic | Cone | Touch | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Soul Dampen Cone",
  "summary": "Reduces soul photonic flux as a fan spread at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.",
  "effect_description": "Reduces soul photonic flux as a fan spread at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon dampen/control recipe that channels soul discipline into photonic output. It applies a cone pattern against group across touch reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Photonic",
  "pattern": "Cone",
  "reach": "Touch",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 10,
    "reach_w": 2,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 1607,
    "hook_mode_multiplier": 2.565,
    "hook_mode_flat_w": 0,
    "total_w": 4122,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
