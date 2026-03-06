# Soul Amplify Field

Boosts soul flux as a field volume at anchored reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.

## Effect

Boosts soul flux as a field volume at anchored reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon amplify/control recipe that channels soul discipline into soul output. It applies a field pattern against group across anchored reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Anchored | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 0 + 0 + 35 + 0 = 95 W
- Subtotal: 1595 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **4737 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Amplify Field** | Pentagon | Amplify | Control | T6 | Soul | Soul | Field | Anchored | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Soul Amplify Field",
  "summary": "Boosts soul flux as a field volume at anchored reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.",
  "effect_description": "Boosts soul flux as a field volume at anchored reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A pentagon amplify/control recipe that channels soul discipline into soul output. It applies a field pattern against group across anchored reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Field",
  "reach": "Anchored",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 60,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1595,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 4737,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
