# Chemical Shape Cone

Refines chemical reactive flux as a fan spread at linked reach, targeting a filtered selection with long timed hold with active regulation while it runs.

## Effect

Refines chemical reactive flux as a fan spread at linked reach, targeting a filtered selection with long timed hold with active regulation while it runs. A circle shape/control recipe that channels chemical discipline into reactive output. It applies a cone pattern against filter across linked reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Reactive | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Linked | +150 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 5 = 275 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 150 + 25 + 60 + 0 = 245 W
- Subtotal: 520 W
- Hook/Mode complexity multiplier: x1.62
- Hook/Mode flat addition: +0 W
- Total: **842 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Chemical Shape Cone** | Circle | Shape | Control | T4 | Chemical | Reactive | Cone | Linked | Timed Long | Filter |

## AI Spell Data

```json
{
  "name": "Chemical Shape Cone",
  "summary": "Refines chemical reactive flux as a fan spread at linked reach, targeting a filtered selection with long timed hold with active regulation while it runs.",
  "effect_description": "Refines chemical reactive flux as a fan spread at linked reach, targeting a filtered selection with long timed hold with active regulation while it runs. A circle shape/control recipe that channels chemical discipline into reactive output. It applies a cone pattern against filter across linked reach with timed long persistence.",
  "hook": "Shape",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Chemical",
  "output_mode": "Reactive",
  "pattern": "Cone",
  "reach": "Linked",
  "persistence": "Timed Long",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 5,
    "core_discipline_w": 275,
    "pattern_w": 10,
    "reach_w": 150,
    "persistence_w": 25,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 520,
    "hook_mode_multiplier": 1.62,
    "hook_mode_flat_w": 0,
    "total_w": 842,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
