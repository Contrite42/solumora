# Soul Counter Beam 2

Disrupts soul flux as a directed line at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.

## Effect

Disrupts soul flux as a directed line at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A pentagon counter/create recipe that channels soul discipline into soul output. It applies a beam pattern against filter across linked reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Linked | +150 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 150 + 0 + 60 + 0 = 215 W
- Subtotal: 1715 W
- Hook/Mode complexity multiplier: x2.9899999999999998
- Hook/Mode flat addition: +0 W
- Total: **5128 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Counter Beam 2** | Pentagon | Counter | Create | T6 | Soul | Soul | Beam | Linked | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Soul Counter Beam 2",
  "summary": "Disrupts soul flux as a directed line at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Disrupts soul flux as a directed line at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A pentagon counter/create recipe that channels soul discipline into soul output. It applies a beam pattern against filter across linked reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Create",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Beam",
  "reach": "Linked",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 5,
    "reach_w": 150,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1715,
    "hook_mode_multiplier": 2.9899999999999998,
    "hook_mode_flat_w": 0,
    "total_w": 5128,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
