# Raw Transform Beam

Reconfigures raw flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Reconfigures raw flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle transform/control recipe that channels raw discipline into raw output. It applies a beam pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 1 = 3 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 0 + 0 = 5 W
- Subtotal: 8 W
- Hook/Mode complexity multiplier: x2.295
- Hook/Mode flat addition: +0 W
- Total: **18 W**
- Required Control Tier: **T1**
- Rarity bucket: **Common**

## All Grimoire Row

| **Raw Transform Beam** | Triangle | Transform | Control | T1 | Raw | Raw | Beam | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Raw Transform Beam",
  "summary": "Reconfigures raw flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Reconfigures raw flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle transform/control recipe that channels raw discipline into raw output. It applies a beam pattern against where written across self reach with immediate persistence.",
  "hook": "Transform",
  "mode": "Control",
  "shape": "Triangle",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 1,
    "core_discipline_w": 3,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 8,
    "hook_mode_multiplier": 2.295,
    "hook_mode_flat_w": 0,
    "total_w": 18,
    "required_tier": "T1",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
