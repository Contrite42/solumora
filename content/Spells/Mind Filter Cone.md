# Mind Filter Cone

Screens mind shock flux as a fan spread at medium reach, targeting the caster with immediate discharge by changing existing conditions.

## Effect

Screens mind shock flux as a fan spread at medium reach, targeting the caster with immediate discharge by changing existing conditions. A pentagon filter/affect recipe that channels mind discipline into shock output. It applies a cone pattern against self across medium reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Shock | +60 W premium |
| Pattern | Cone | +10 W |
| Reach | Medium | +15 W |
| Persistence | Immediate | +0 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 25 = 500 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 15 + 0 + 0 + 60 = 85 W
- Subtotal: 585 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **936 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Mind Filter Cone** | Pentagon | Filter | Affect | T4 | Mind | Shock | Cone | Medium | Immediate | Self |

## AI Spell Data

```json
{
  "name": "Mind Filter Cone",
  "summary": "Screens mind shock flux as a fan spread at medium reach, targeting the caster with immediate discharge by changing existing conditions.",
  "effect_description": "Screens mind shock flux as a fan spread at medium reach, targeting the caster with immediate discharge by changing existing conditions. A pentagon filter/affect recipe that channels mind discipline into shock output. It applies a cone pattern against self across medium reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Affect",
  "shape": "Pentagon",
  "discipline": "Mind",
  "output_mode": "Shock",
  "pattern": "Cone",
  "reach": "Medium",
  "persistence": "Immediate",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 25,
    "core_discipline_w": 500,
    "pattern_w": 10,
    "reach_w": 15,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 585,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 936,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
