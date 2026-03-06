# Raw Lantern Mark

Creates a short-lived neutral flux marker for close work.

## Effect

Projects a compact neutral flux marker that remains stable long enough for routine tasks.

## Sigil Variables

| Variable    | Assigned Value | Cost Rule                                                     |
| ----------- | -------------- | ------------------------------------------------------------- |
| Hook        | Emit           | Center core variable (complexity handled via multiplier/flat) |
| Mode        | Create         | Center core variable (complexity handled via multiplier/flat) |
| Shape       | Triangle       | Base 3 W, outer slots 3                                       |
| Discipline  | Raw            | x1 multiplier                                                 |
| Output Mode | Raw            | +0 W premium                                                  |
| Pattern     | Point          | +0 W                                                          |
| Reach       | Self           | +0 W                                                          |
| Persistence | Immediate      | +0 W                                                          |
| Target Spec | Where Written  | +0 W                                                          |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 \* 1 = 3 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 0 + 0 = 0 W
- Subtotal: 3 W
- Hook/Mode complexity multiplier: x1.15
- Hook/Mode flat addition: +0 W
- Total: **3 W**
- Required Control Tier: **T0**
- Rarity bucket: **Common**

## All Grimoire Row

| **Raw Lantern Mark** | Triangle | Emit | Create | T0 | Raw | Raw | Point | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Raw Lantern Mark",
  "summary": "Creates a short-lived neutral flux marker for close work.",
  "effect_description": "Projects a compact neutral flux marker that remains stable long enough for routine tasks.",
  "hook": "Emit",
  "mode": "Create",
  "shape": "Triangle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 1,
    "core_discipline_w": 3,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 3,
    "hook_mode_multiplier": 1.15,
    "hook_mode_flat_w": 0,
    "total_w": 3,
    "required_tier": "T0",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```

## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
