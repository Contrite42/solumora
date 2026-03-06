# Soul Amplify Point

Boosts soul flux as a point focus at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.

## Effect

Boosts soul flux as a point focus at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon amplify/control recipe that channels soul discipline into soul output. It applies a point pattern against group across touch reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Touch | +2 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 2 + 0 + 35 + 0 = 37 W
- Subtotal: 1537 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **4565 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Amplify Point** | Pentagon | Amplify | Control | T6 | Soul | Soul | Point | Touch | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Soul Amplify Point",
  "summary": "Boosts soul flux as a point focus at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.",
  "effect_description": "Boosts soul flux as a point focus at touch reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon amplify/control recipe that channels soul discipline into soul output. It applies a point pattern against group across touch reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Point",
  "reach": "Touch",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 0,
    "reach_w": 2,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1537,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 4565,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
