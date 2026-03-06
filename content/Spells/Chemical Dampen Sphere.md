# Chemical Dampen Sphere

Reduces chemical reactive flux as a spherical envelope at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.

## Effect

Reduces chemical reactive flux as a spherical envelope at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A triangle dampen/affect recipe that channels chemical discipline into reactive output. It applies a sphere pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Reactive | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 5 = 15 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 0 + 0 + 0 + 0 = 30 W
- Subtotal: 45 W
- Hook/Mode complexity multiplier: x1.9
- Hook/Mode flat addition: +0 W
- Total: **86 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Chemical Dampen Sphere** | Triangle | Dampen | Affect | T2 | Chemical | Reactive | Sphere | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Chemical Dampen Sphere",
  "summary": "Reduces chemical reactive flux as a spherical envelope at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.",
  "effect_description": "Reduces chemical reactive flux as a spherical envelope at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions. A triangle dampen/affect recipe that channels chemical discipline into reactive output. It applies a sphere pattern against where written across self reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Chemical",
  "output_mode": "Reactive",
  "pattern": "Sphere",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 5,
    "core_discipline_w": 15,
    "pattern_w": 30,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 45,
    "hook_mode_multiplier": 1.9,
    "hook_mode_flat_w": 0,
    "total_w": 86,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
