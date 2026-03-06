# Chemical Dampen Plane

Reduces chemical reactive flux as a planar spread at long reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression.

## Effect

Reduces chemical reactive flux as a planar spread at long reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression. A pentagon dampen/create recipe that channels chemical discipline into reactive output. It applies a plane pattern against surface across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Reactive | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 5 = 100 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 40 + 0 + 5 + 0 = 45 W
- Subtotal: 145 W
- Hook/Mode complexity multiplier: x2.1849999999999996
- Hook/Mode flat addition: +0 W
- Total: **317 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Chemical Dampen Plane** | Pentagon | Dampen | Create | T3 | Chemical | Reactive | Plane | Long | Immediate | Surface |

## AI Spell Data

```json
{
  "name": "Chemical Dampen Plane",
  "summary": "Reduces chemical reactive flux as a planar spread at long reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Reduces chemical reactive flux as a planar spread at long reach, targeting a prepared surface with immediate discharge by creating a fresh flux expression. A pentagon dampen/create recipe that channels chemical discipline into reactive output. It applies a plane pattern against surface across long reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Create",
  "shape": "Pentagon",
  "discipline": "Chemical",
  "output_mode": "Reactive",
  "pattern": "Plane",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 5,
    "core_discipline_w": 100,
    "pattern_w": 0,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 145,
    "hook_mode_multiplier": 2.1849999999999996,
    "hook_mode_flat_w": 0,
    "total_w": 317,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
