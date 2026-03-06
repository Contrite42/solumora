# Mind Filter Beam

Screens mind neuro flux as a directed line at self reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.

## Effect

Screens mind neuro flux as a directed line at self reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A circle filter/control recipe that channels mind discipline into neuro output. It applies a beam pattern against group across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 35 + 0 = 40 W
- Subtotal: 1415 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **3056 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Filter Beam** | Circle | Filter | Control | T5 | Mind | Neuro | Beam | Self | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Mind Filter Beam",
  "summary": "Screens mind neuro flux as a directed line at self reach, targeting a grouped cluster with immediate discharge with active regulation while it runs.",
  "effect_description": "Screens mind neuro flux as a directed line at self reach, targeting a grouped cluster with immediate discharge with active regulation while it runs. A circle filter/control recipe that channels mind discipline into neuro output. It applies a beam pattern against group across self reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1415,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 3056,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
