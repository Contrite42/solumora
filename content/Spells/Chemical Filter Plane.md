# Chemical Filter Plane

Screens chemical thermal flux as a planar spread at medium reach, targeting one individual with immediate discharge with active regulation while it runs.

## Effect

Screens chemical thermal flux as a planar spread at medium reach, targeting one individual with immediate discharge with active regulation while it runs. A pentagon filter/control recipe that channels chemical discipline into thermal output. It applies a plane pattern against individual across medium reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Thermal | +10 W premium |
| Pattern | Plane | +0 W |
| Reach | Medium | +15 W |
| Persistence | Immediate | +0 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 5 = 100 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 15 + 0 + 8 + 10 = 33 W
- Subtotal: 133 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **287 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Chemical Filter Plane** | Pentagon | Filter | Control | T3 | Chemical | Thermal | Plane | Medium | Immediate | Individual |

## AI Spell Data

```json
{
  "name": "Chemical Filter Plane",
  "summary": "Screens chemical thermal flux as a planar spread at medium reach, targeting one individual with immediate discharge with active regulation while it runs.",
  "effect_description": "Screens chemical thermal flux as a planar spread at medium reach, targeting one individual with immediate discharge with active regulation while it runs. A pentagon filter/control recipe that channels chemical discipline into thermal output. It applies a plane pattern against individual across medium reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Chemical",
  "output_mode": "Thermal",
  "pattern": "Plane",
  "reach": "Medium",
  "persistence": "Immediate",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 5,
    "core_discipline_w": 100,
    "pattern_w": 0,
    "reach_w": 15,
    "persistence_w": 0,
    "target_w": 8,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 133,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 287,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
