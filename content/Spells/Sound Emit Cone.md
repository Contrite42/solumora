# Sound Emit Cone

Releases sound sonic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression.

## Effect

Releases sound sonic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression. A triangle emit/create recipe that channels sound discipline into sonic output. It applies a cone pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Sonic | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 4 = 12 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 0 + 0 = 10 W
- Subtotal: 22 W
- Hook/Mode complexity multiplier: x1.15
- Hook/Mode flat addition: +0 W
- Total: **25 W**
- Required Control Tier: **T1**
- Rarity bucket: **Common**

## All Grimoire Row

| **Sound Emit Cone** | Triangle | Emit | Create | T1 | Sound | Sonic | Cone | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Sound Emit Cone",
  "summary": "Releases sound sonic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Releases sound sonic flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression. A triangle emit/create recipe that channels sound discipline into sonic output. It applies a cone pattern against where written across self reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Create",
  "shape": "Triangle",
  "discipline": "Sound",
  "output_mode": "Sonic",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 4,
    "core_discipline_w": 12,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 22,
    "hook_mode_multiplier": 1.15,
    "hook_mode_flat_w": 0,
    "total_w": 25,
    "required_tier": "T1",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
