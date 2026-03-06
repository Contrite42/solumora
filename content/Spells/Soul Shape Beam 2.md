# Soul Shape Beam 2

Refines soul flux as a directed line at long reach, targeting one object with short timed hold by changing existing conditions.

## Effect

Refines soul flux as a directed line at long reach, targeting one object with short timed hold by changing existing conditions. A circle shape/affect recipe that channels soul discipline into soul output. It applies a beam pattern against object across long reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Long | +40 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 40 + 5 + 2 + 0 = 52 W
- Subtotal: 4177 W
- Hook/Mode complexity multiplier: x1.2
- Hook/Mode flat addition: +0 W
- Total: **5012 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Shape Beam 2** | Circle | Shape | Affect | T6 | Soul | Soul | Beam | Long | Timed Short | Object |

## AI Spell Data

```json
{
  "name": "Soul Shape Beam 2",
  "summary": "Refines soul flux as a directed line at long reach, targeting one object with short timed hold by changing existing conditions.",
  "effect_description": "Refines soul flux as a directed line at long reach, targeting one object with short timed hold by changing existing conditions. A circle shape/affect recipe that channels soul discipline into soul output. It applies a beam pattern against object across long reach with timed short persistence.",
  "hook": "Shape",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Beam",
  "reach": "Long",
  "persistence": "Timed Short",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 5,
    "reach_w": 40,
    "persistence_w": 5,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4177,
    "hook_mode_multiplier": 1.2,
    "hook_mode_flat_w": 0,
    "total_w": 5012,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
