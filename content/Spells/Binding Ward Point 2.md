# Binding Ward Point 2

Establishes binding reactive flux as a point focus at line-of-sight reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.

## Effect

Establishes binding reactive flux as a point focus at line-of-sight reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A circle ward/control recipe that channels binding discipline into reactive output. It applies a point pattern against group across line-of-sight reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Ward | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Reactive | +10 W premium |
| Pattern | Point | +0 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 10 = 550 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 80 + 0 + 35 + 10 = 125 W
- Subtotal: 675 W
- Hook/Mode complexity multiplier: x2.7
- Hook/Mode flat addition: +0 W
- Total: **1823 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Binding Ward Point 2** | Circle | Ward | Control | T5 | Binding | Reactive | Point | Line-of-Sight | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Binding Ward Point 2",
  "summary": "Establishes binding reactive flux as a point focus at line-of-sight reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.",
  "effect_description": "Establishes binding reactive flux as a point focus at line-of-sight reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A circle ward/control recipe that channels binding discipline into reactive output. It applies a point pattern against group across line-of-sight reach with immediate persistence.",
  "hook": "Ward",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Binding",
  "output_mode": "Reactive",
  "pattern": "Point",
  "reach": "Line-of-Sight",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 10,
    "core_discipline_w": 550,
    "pattern_w": 0,
    "reach_w": 80,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 675,
    "hook_mode_multiplier": 2.7,
    "hook_mode_flat_w": 0,
    "total_w": 1823,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
