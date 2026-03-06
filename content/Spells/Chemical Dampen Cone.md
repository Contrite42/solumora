# Chemical Dampen Cone

Reduces chemical reactive flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression.

## Effect

Reduces chemical reactive flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression. A triangle dampen/create recipe that channels chemical discipline into reactive output. It applies a cone pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Reactive | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 5 = 15 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 0 + 0 = 10 W
- Subtotal: 25 W
- Hook/Mode complexity multiplier: x2.1849999999999996
- Hook/Mode flat addition: +0 W
- Total: **55 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Chemical Dampen Cone** | Triangle | Dampen | Create | T2 | Chemical | Reactive | Cone | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Chemical Dampen Cone",
  "summary": "Reduces chemical reactive flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Reduces chemical reactive flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression. A triangle dampen/create recipe that channels chemical discipline into reactive output. It applies a cone pattern against where written across self reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Create",
  "shape": "Triangle",
  "discipline": "Chemical",
  "output_mode": "Reactive",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 5,
    "core_discipline_w": 15,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 25,
    "hook_mode_multiplier": 2.1849999999999996,
    "hook_mode_flat_w": 0,
    "total_w": 55,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
