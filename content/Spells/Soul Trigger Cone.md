# Soul Trigger Cone

Arms soul flux as a fan spread at linked reach, targeting one object with immediate discharge with active regulation while it runs.

## Effect

Arms soul flux as a fan spread at linked reach, targeting one object with immediate discharge with active regulation while it runs. A circle trigger/control recipe that channels soul discipline into soul output. It applies a cone pattern against object across linked reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Trigger | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Linked | +150 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 150 + 0 + 2 + 0 = 162 W
- Subtotal: 4287 W
- Hook/Mode complexity multiplier: x2.43
- Hook/Mode flat addition: +0 W
- Total: **10417 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Trigger Cone** | Circle | Trigger | Control | T6 | Soul | Soul | Cone | Linked | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Soul Trigger Cone",
  "summary": "Arms soul flux as a fan spread at linked reach, targeting one object with immediate discharge with active regulation while it runs.",
  "effect_description": "Arms soul flux as a fan spread at linked reach, targeting one object with immediate discharge with active regulation while it runs. A circle trigger/control recipe that channels soul discipline into soul output. It applies a cone pattern against object across linked reach with immediate persistence.",
  "hook": "Trigger",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cone",
  "reach": "Linked",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 10,
    "reach_w": 150,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4287,
    "hook_mode_multiplier": 2.43,
    "hook_mode_flat_w": 0,
    "total_w": 10417,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
