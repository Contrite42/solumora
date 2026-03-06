# Binding Emit Ring

Releases binding reactive flux as a ring perimeter at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs.

## Effect

Releases binding reactive flux as a ring perimeter at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs. A pentagon emit/control recipe that channels binding discipline into reactive output. It applies a ring pattern against surface across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Reactive | +10 W premium |
| Pattern | Ring | +15 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 10 = 200 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 40 + 0 + 5 + 10 = 70 W
- Subtotal: 270 W
- Hook/Mode complexity multiplier: x1.35
- Hook/Mode flat addition: +0 W
- Total: **364 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Binding Emit Ring** | Pentagon | Emit | Control | T3 | Binding | Reactive | Ring | Long | Immediate | Surface |

## AI Spell Data

```json
{
  "name": "Binding Emit Ring",
  "summary": "Releases binding reactive flux as a ring perimeter at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs.",
  "effect_description": "Releases binding reactive flux as a ring perimeter at long reach, targeting a prepared surface with immediate discharge with active regulation while it runs. A pentagon emit/control recipe that channels binding discipline into reactive output. It applies a ring pattern against surface across long reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Binding",
  "output_mode": "Reactive",
  "pattern": "Ring",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 10,
    "core_discipline_w": 200,
    "pattern_w": 15,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 5,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 270,
    "hook_mode_multiplier": 1.35,
    "hook_mode_flat_w": 0,
    "total_w": 364,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
