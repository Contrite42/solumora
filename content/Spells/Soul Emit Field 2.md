# Soul Emit Field 2

Releases soul reactive flux as a field volume at touch reach, targeting one object with long timed hold by creating a fresh flux expression.

## Effect

Releases soul reactive flux as a field volume at touch reach, targeting one object with long timed hold by creating a fresh flux expression. A circle emit/create recipe that channels soul discipline into reactive output. It applies a field pattern against object across touch reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Reactive | +60 W premium |
| Pattern | Field | +60 W |
| Reach | Touch | +2 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 2 + 25 + 2 + 60 = 149 W
- Subtotal: 4274 W
- Hook/Mode complexity multiplier: x1.15
- Hook/Mode flat addition: +0 W
- Total: **4915 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Emit Field 2** | Circle | Emit | Create | T6 | Soul | Reactive | Field | Touch | Timed Long | Object |

## AI Spell Data

```json
{
  "name": "Soul Emit Field 2",
  "summary": "Releases soul reactive flux as a field volume at touch reach, targeting one object with long timed hold by creating a fresh flux expression.",
  "effect_description": "Releases soul reactive flux as a field volume at touch reach, targeting one object with long timed hold by creating a fresh flux expression. A circle emit/create recipe that channels soul discipline into reactive output. It applies a field pattern against object across touch reach with timed long persistence.",
  "hook": "Emit",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Reactive",
  "pattern": "Field",
  "reach": "Touch",
  "persistence": "Timed Long",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 60,
    "reach_w": 2,
    "persistence_w": 25,
    "target_w": 2,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 4274,
    "hook_mode_multiplier": 1.15,
    "hook_mode_flat_w": 0,
    "total_w": 4915,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
