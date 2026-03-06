# Mind Shape Ring

Refines mind reactive flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Refines mind reactive flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle shape/control recipe that channels mind discipline into reactive output. It applies a ring pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Reactive | +60 W premium |
| Pattern | Ring | +15 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 25 = 75 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 0 + 0 + 0 + 60 = 75 W
- Subtotal: 150 W
- Hook/Mode complexity multiplier: x1.62
- Hook/Mode flat addition: +0 W
- Total: **243 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Mind Shape Ring** | Triangle | Shape | Control | T3 | Mind | Reactive | Ring | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Mind Shape Ring",
  "summary": "Refines mind reactive flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Refines mind reactive flux as a ring perimeter at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle shape/control recipe that channels mind discipline into reactive output. It applies a ring pattern against where written across self reach with immediate persistence.",
  "hook": "Shape",
  "mode": "Control",
  "shape": "Triangle",
  "discipline": "Mind",
  "output_mode": "Reactive",
  "pattern": "Ring",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 25,
    "core_discipline_w": 75,
    "pattern_w": 15,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 150,
    "hook_mode_multiplier": 1.62,
    "hook_mode_flat_w": 0,
    "total_w": 243,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
