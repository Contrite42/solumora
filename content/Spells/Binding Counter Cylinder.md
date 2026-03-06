# Binding Counter Cylinder

Disrupts binding kinetic flux as a column volume at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression.

## Effect

Disrupts binding kinetic flux as a column volume at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression. A triangle counter/create recipe that channels binding discipline into kinetic output. It applies a cylinder pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Kinetic | +10 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 0 + 0 + 0 + 10 = 30 W
- Subtotal: 60 W
- Hook/Mode complexity multiplier: x2.9899999999999998
- Hook/Mode flat addition: +0 W
- Total: **179 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Binding Counter Cylinder** | Triangle | Counter | Create | T3 | Binding | Kinetic | Cylinder | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Binding Counter Cylinder",
  "summary": "Disrupts binding kinetic flux as a column volume at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Disrupts binding kinetic flux as a column volume at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression. A triangle counter/create recipe that channels binding discipline into kinetic output. It applies a cylinder pattern against where written across self reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Create",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Kinetic",
  "pattern": "Cylinder",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 20,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 60,
    "hook_mode_multiplier": 2.9899999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 179,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
