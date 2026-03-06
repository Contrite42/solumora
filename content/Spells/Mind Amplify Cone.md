# Mind Amplify Cone

Boosts mind neuro flux as a fan spread at self reach, targeting the inscribed anchor with long timed hold with active regulation while it runs.

## Effect

Boosts mind neuro flux as a fan spread at self reach, targeting the inscribed anchor with long timed hold with active regulation while it runs. A circle amplify/control recipe that channels mind discipline into neuro output. It applies a cone pattern against where written across self reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 25 + 0 + 0 = 35 W
- Subtotal: 1410 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **4188 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Amplify Cone** | Circle | Amplify | Control | T6 | Mind | Neuro | Cone | Self | Timed Long | Where Written |

## AI Spell Data

```json
{
  "name": "Mind Amplify Cone",
  "summary": "Boosts mind neuro flux as a fan spread at self reach, targeting the inscribed anchor with long timed hold with active regulation while it runs.",
  "effect_description": "Boosts mind neuro flux as a fan spread at self reach, targeting the inscribed anchor with long timed hold with active regulation while it runs. A circle amplify/control recipe that channels mind discipline into neuro output. It applies a cone pattern against where written across self reach with timed long persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Timed Long",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 25,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1410,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 4188,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
