# Mind Counter Point

Disrupts mind raw flux as a point focus at anchored reach, targeting a filtered selection with immediate discharge with active regulation while it runs.

## Effect

Disrupts mind raw flux as a point focus at anchored reach, targeting a filtered selection with immediate discharge with active regulation while it runs. A circle counter/control recipe that channels mind discipline into raw output. It applies a point pattern against filter across anchored reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Mind | x25 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Point | +0 W |
| Reach | Anchored | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 25 = 1375 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 60 + 30 = 90 W
- Subtotal: 1465 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **5142 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Mind Counter Point** | Circle | Counter | Control | T6 | Mind | Raw | Point | Anchored | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Mind Counter Point",
  "summary": "Disrupts mind raw flux as a point focus at anchored reach, targeting a filtered selection with immediate discharge with active regulation while it runs.",
  "effect_description": "Disrupts mind raw flux as a point focus at anchored reach, targeting a filtered selection with immediate discharge with active regulation while it runs. A circle counter/control recipe that channels mind discipline into raw output. It applies a point pattern against filter across anchored reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Mind",
  "output_mode": "Raw",
  "pattern": "Point",
  "reach": "Anchored",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 25,
    "core_discipline_w": 1375,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 1465,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 5142,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
