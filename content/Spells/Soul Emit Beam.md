# Soul Emit Beam

Releases soul flux as a directed line at medium reach, targeting one object with latched hold with active regulation while it runs.

## Effect

Releases soul flux as a directed line at medium reach, targeting one object with latched hold with active regulation while it runs. A circle emit/control recipe that channels soul discipline into soul output. It applies a beam pattern against object across medium reach with latched persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Medium | +15 W |
| Persistence | Latched | +40 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 15 + 40 + 2 + 0 = 62 W
- Subtotal: 4187 W
- Hook/Mode complexity multiplier: x1.35
- Hook/Mode flat addition: +0 W
- Total: **5652 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Emit Beam** | Circle | Emit | Control | T6 | Soul | Soul | Beam | Medium | Latched | Object |

## AI Spell Data

```json
{
  "name": "Soul Emit Beam",
  "summary": "Releases soul flux as a directed line at medium reach, targeting one object with latched hold with active regulation while it runs.",
  "effect_description": "Releases soul flux as a directed line at medium reach, targeting one object with latched hold with active regulation while it runs. A circle emit/control recipe that channels soul discipline into soul output. It applies a beam pattern against object across medium reach with latched persistence.",
  "hook": "Emit",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Beam",
  "reach": "Medium",
  "persistence": "Latched",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 5,
    "reach_w": 15,
    "persistence_w": 40,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4187,
    "hook_mode_multiplier": 1.35,
    "hook_mode_flat_w": 0,
    "total_w": 5652,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
