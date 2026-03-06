# Soul Dampen Cone 2

Reduces soul constraint flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Reduces soul constraint flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A circle dampen/control recipe that channels soul discipline into constraint output. It applies a cone pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Constraint | +60 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 0 + 60 = 70 W
- Subtotal: 4195 W
- Hook/Mode complexity multiplier: x2.565
- Hook/Mode flat addition: +0 W
- Total: **10760 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Dampen Cone 2** | Circle | Dampen | Control | T6 | Soul | Constraint | Cone | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Soul Dampen Cone 2",
  "summary": "Reduces soul constraint flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Reduces soul constraint flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A circle dampen/control recipe that channels soul discipline into constraint output. It applies a cone pattern against where written across self reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Constraint",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 4195,
    "hook_mode_multiplier": 2.565,
    "hook_mode_flat_w": 0,
    "total_w": 10760,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
