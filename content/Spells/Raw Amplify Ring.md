# Raw Amplify Ring

Boosts raw flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Boosts raw flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle amplify/control recipe that channels raw discipline into raw output. It applies a ring pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 1 = 3 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 0 + 0 + 0 + 0 = 15 W
- Subtotal: 18 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **53 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Raw Amplify Ring** | Triangle | Amplify | Control | T2 | Raw | Raw | Ring | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Raw Amplify Ring",
  "summary": "Boosts raw flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Boosts raw flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle amplify/control recipe that channels raw discipline into raw output. It applies a ring pattern against where written across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Triangle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Ring",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 1,
    "core_discipline_w": 3,
    "pattern_w": 15,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 18,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 53,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
