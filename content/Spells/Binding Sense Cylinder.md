# Binding Sense Cylinder

Detects binding constraint flux as a column volume at long reach, targeting a filtered selection with short timed hold by creating a fresh flux expression.

## Effect

Detects binding constraint flux as a column volume at long reach, targeting a filtered selection with short timed hold by creating a fresh flux expression. A circle sense/create recipe that channels binding discipline into constraint output. It applies a cylinder pattern against filter across long reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Long | +40 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 10 = 550 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 40 + 5 + 60 + 0 = 125 W
- Subtotal: 675 W
- Hook/Mode complexity multiplier: x2.07
- Hook/Mode flat addition: +0 W
- Total: **1397 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Binding Sense Cylinder** | Circle | Sense | Create | T5 | Binding | Constraint | Cylinder | Long | Timed Short | Filter |

## AI Spell Data

```json
{
  "name": "Binding Sense Cylinder",
  "summary": "Detects binding constraint flux as a column volume at long reach, targeting a filtered selection with short timed hold by creating a fresh flux expression.",
  "effect_description": "Detects binding constraint flux as a column volume at long reach, targeting a filtered selection with short timed hold by creating a fresh flux expression. A circle sense/create recipe that channels binding discipline into constraint output. It applies a cylinder pattern against filter across long reach with timed short persistence.",
  "hook": "Sense",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Cylinder",
  "reach": "Long",
  "persistence": "Timed Short",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 10,
    "core_discipline_w": 550,
    "pattern_w": 20,
    "reach_w": 40,
    "persistence_w": 5,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 675,
    "hook_mode_multiplier": 2.07,
    "hook_mode_flat_w": 0,
    "total_w": 1397,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
