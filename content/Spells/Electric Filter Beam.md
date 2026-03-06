# Electric Filter Beam

Screens electric shock flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.

## Effect

Screens electric shock flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A triangle filter/affect recipe that channels electric discipline into shock output. It applies a beam pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Electric | x5 multiplier |
| Output Mode | Shock | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 5 = 15 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 0 + 0 = 5 W
- Subtotal: 20 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **32 W**
- Required Control Tier: **T1**
- Rarity bucket: **Common**

## All Grimoire Row

| **Electric Filter Beam** | Triangle | Filter | Affect | T1 | Electric | Shock | Beam | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Electric Filter Beam",
  "summary": "Screens electric shock flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.",
  "effect_description": "Screens electric shock flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A triangle filter/affect recipe that channels electric discipline into shock output. It applies a beam pattern against where written across self reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Electric",
  "output_mode": "Shock",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 5,
    "core_discipline_w": 15,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 20,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 32,
    "required_tier": "T1",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
