# Mind Counter Beam

Disrupts mind neuro flux as a directed line at self reach, targeting a grouped cluster with sustained channeling with active regulation while it runs.

## Effect

Disrupts mind neuro flux as a directed line at self reach, targeting a grouped cluster with sustained channeling with active regulation while it runs. A circle counter/control recipe that channels mind discipline into neuro output. It applies a beam pattern against group across self reach with sustained persistence. The sustained window is set to 40 minutes.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Neuro | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Sustained (40 min planned active window) | +40 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 40 + 35 + 0 = 80 W
- Subtotal: 1455 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **5107 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Counter Beam** | Circle | Counter | Control | T6 | Mind | Neuro | Beam | Self | Sustained | Group |

## AI Spell Data

```json
{
  "name": "Mind Counter Beam",
  "summary": "Disrupts mind neuro flux as a directed line at self reach, targeting a grouped cluster with sustained channeling with active regulation while it runs.",
  "effect_description": "Disrupts mind neuro flux as a directed line at self reach, targeting a grouped cluster with sustained channeling with active regulation while it runs. A circle counter/control recipe that channels mind discipline into neuro output. It applies a beam pattern against group across self reach with sustained persistence. The sustained window is set to 40 minutes.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Neuro",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Sustained",
  "target_spec": "Group",
  "sustained_minutes": 40,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 40,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1455,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 5107,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
