# Soul Sense Cylinder

Detects soul photonic flux as a column volume at linked reach, targeting a grouped cluster with immediate discharge by changing existing conditions.

## Effect

Detects soul photonic flux as a column volume at linked reach, targeting a grouped cluster with immediate discharge by changing existing conditions. A circle sense/affect recipe that channels soul discipline into photonic output. It applies a cylinder pattern against group across linked reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Photonic | +60 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Linked | +150 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 150 + 0 + 35 + 60 = 265 W
- Subtotal: 4390 W
- Hook/Mode complexity multiplier: x1.8
- Hook/Mode flat addition: +0 W
- Total: **7902 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Sense Cylinder** | Circle | Sense | Affect | T6 | Soul | Photonic | Cylinder | Linked | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Soul Sense Cylinder",
  "summary": "Detects soul photonic flux as a column volume at linked reach, targeting a grouped cluster with immediate discharge by changing existing conditions.",
  "effect_description": "Detects soul photonic flux as a column volume at linked reach, targeting a grouped cluster with immediate discharge by changing existing conditions. A circle sense/affect recipe that channels soul discipline into photonic output. It applies a cylinder pattern against group across linked reach with immediate persistence.",
  "hook": "Sense",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Photonic",
  "pattern": "Cylinder",
  "reach": "Linked",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 20,
    "reach_w": 150,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 4390,
    "hook_mode_multiplier": 1.8,
    "hook_mode_flat_w": 0,
    "total_w": 7902,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
