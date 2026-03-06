# Soul Emit Field

Releases soul flux as a field volume at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.

## Effect

Releases soul flux as a field volume at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A circle emit/create recipe that channels soul discipline into soul output. It applies a field pattern against filter across linked reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Linked | +150 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 150 + 0 + 60 + 0 = 270 W
- Subtotal: 4395 W
- Hook/Mode complexity multiplier: x1.15
- Hook/Mode flat addition: +0 W
- Total: **5054 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Emit Field** | Circle | Emit | Create | T6 | Soul | Soul | Field | Linked | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Soul Emit Field",
  "summary": "Releases soul flux as a field volume at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Releases soul flux as a field volume at linked reach, targeting a filtered selection with immediate discharge by creating a fresh flux expression. A circle emit/create recipe that channels soul discipline into soul output. It applies a field pattern against filter across linked reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Create",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Field",
  "reach": "Linked",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 60,
    "reach_w": 150,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4395,
    "hook_mode_multiplier": 1.15,
    "hook_mode_flat_w": 0,
    "total_w": 5054,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
