# Binding Move Cone

Repositions binding kinetic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.

## Effect

Repositions binding kinetic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A triangle move/affect recipe that channels binding discipline into kinetic output. It applies a cone pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Kinetic | +10 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 0 + 10 = 20 W
- Subtotal: 50 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **75 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Binding Move Cone** | Triangle | Move | Affect | T2 | Binding | Kinetic | Cone | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Binding Move Cone",
  "summary": "Repositions binding kinetic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.",
  "effect_description": "Repositions binding kinetic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A triangle move/affect recipe that channels binding discipline into kinetic output. It applies a cone pattern against where written across self reach with immediate persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Kinetic",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 50,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 75,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
