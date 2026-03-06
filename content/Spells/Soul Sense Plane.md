# Soul Sense Plane

Detects soul flux as a planar spread at medium reach, targeting one object with short timed hold with active regulation while it runs.

## Effect

Detects soul flux as a planar spread at medium reach, targeting one object with short timed hold with active regulation while it runs. A circle sense/control recipe that channels soul discipline into soul output. It applies a plane pattern against object across medium reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Medium | +15 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 15 + 5 + 2 + 0 = 22 W
- Subtotal: 4147 W
- Hook/Mode complexity multiplier: x2.43
- Hook/Mode flat addition: +0 W
- Total: **10077 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Sense Plane** | Circle | Sense | Control | T6 | Soul | Soul | Plane | Medium | Timed Short | Object |

## AI Spell Data

```json
{
  "name": "Soul Sense Plane",
  "summary": "Detects soul flux as a planar spread at medium reach, targeting one object with short timed hold with active regulation while it runs.",
  "effect_description": "Detects soul flux as a planar spread at medium reach, targeting one object with short timed hold with active regulation while it runs. A circle sense/control recipe that channels soul discipline into soul output. It applies a plane pattern against object across medium reach with timed short persistence.",
  "hook": "Sense",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Plane",
  "reach": "Medium",
  "persistence": "Timed Short",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 15,
    "persistence_w": 5,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4147,
    "hook_mode_multiplier": 2.43,
    "hook_mode_flat_w": 0,
    "total_w": 10077,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
