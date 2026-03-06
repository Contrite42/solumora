# Mind Transform Point

Reconfigures mind neuro flux as a point focus at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Reconfigures mind neuro flux as a point focus at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle transform/control recipe that channels mind discipline into neuro output. It applies a point pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Transform | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 25 = 75 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 0 + 0 = 0 W
- Subtotal: 75 W
- Hook/Mode complexity multiplier: x2.295
- Hook/Mode flat addition: +0 W
- Total: **172 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Mind Transform Point** | Triangle | Transform | Control | T3 | Mind | Neuro | Point | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Mind Transform Point",
  "summary": "Reconfigures mind neuro flux as a point focus at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Reconfigures mind neuro flux as a point focus at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle transform/control recipe that channels mind discipline into neuro output. It applies a point pattern against where written across self reach with immediate persistence.",
  "hook": "Transform",
  "mode": "Control",
  "shape": "Triangle",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 25,
    "core_discipline_w": 75,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 75,
    "hook_mode_multiplier": 2.295,
    "hook_mode_flat_w": 0,
    "total_w": 172,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
