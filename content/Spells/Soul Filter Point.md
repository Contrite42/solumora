# Soul Filter Point

Screens soul raw flux as a point focus at self reach, targeting a marked signature with immediate discharge with active regulation while it runs.

## Effect

Screens soul raw flux as a point focus at self reach, targeting a marked signature with immediate discharge with active regulation while it runs. A square filter/control recipe that channels soul discipline into raw output. It applies a point pattern against marked across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Point | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 75 = 600 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 15 + 30 = 45 W
- Subtotal: 645 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **1393 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Filter Point** | Square | Filter | Control | T5 | Soul | Raw | Point | Self | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Soul Filter Point",
  "summary": "Screens soul raw flux as a point focus at self reach, targeting a marked signature with immediate discharge with active regulation while it runs.",
  "effect_description": "Screens soul raw flux as a point focus at self reach, targeting a marked signature with immediate discharge with active regulation while it runs. A square filter/control recipe that channels soul discipline into raw output. It applies a point pattern against marked across self reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 75,
    "core_discipline_w": 600,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 645,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 1393,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
