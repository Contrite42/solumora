# Soul Shape Cylinder

Refines soul flux as a column volume at self reach, targeting a marked signature with immediate discharge with active regulation while it runs.

## Effect

Refines soul flux as a column volume at self reach, targeting a marked signature with immediate discharge with active regulation while it runs. A square shape/control recipe that channels soul discipline into soul output. It applies a cylinder pattern against marked across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 75 = 600 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 0 + 0 + 15 + 0 = 35 W
- Subtotal: 635 W
- Hook/Mode complexity multiplier: x1.62
- Hook/Mode flat addition: +0 W
- Total: **1029 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Soul Shape Cylinder** | Square | Shape | Control | T4 | Soul | Soul | Cylinder | Self | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Soul Shape Cylinder",
  "summary": "Refines soul flux as a column volume at self reach, targeting a marked signature with immediate discharge with active regulation while it runs.",
  "effect_description": "Refines soul flux as a column volume at self reach, targeting a marked signature with immediate discharge with active regulation while it runs. A square shape/control recipe that channels soul discipline into soul output. It applies a cylinder pattern against marked across self reach with immediate persistence.",
  "hook": "Shape",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cylinder",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 75,
    "core_discipline_w": 600,
    "pattern_w": 20,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 635,
    "hook_mode_multiplier": 1.62,
    "hook_mode_flat_w": 0,
    "total_w": 1029,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
