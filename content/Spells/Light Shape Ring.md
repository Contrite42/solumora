# Light Shape Ring

Refines light photonic flux as a ring perimeter at long reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Refines light photonic flux as a ring perimeter at long reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A pentagon shape/control recipe that channels light discipline into photonic output. It applies a ring pattern against where written across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Light | x3 multiplier |
| Output Mode | Photonic | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 3 = 60 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 40 + 0 + 0 + 0 = 55 W
- Subtotal: 115 W
- Hook/Mode complexity multiplier: x1.62
- Hook/Mode flat addition: +0 W
- Total: **186 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Light Shape Ring** | Pentagon | Shape | Control | T3 | Light | Photonic | Ring | Long | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Light Shape Ring",
  "summary": "Refines light photonic flux as a ring perimeter at long reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Refines light photonic flux as a ring perimeter at long reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A pentagon shape/control recipe that channels light discipline into photonic output. It applies a ring pattern against where written across long reach with immediate persistence.",
  "hook": "Shape",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Light",
  "output_mode": "Photonic",
  "pattern": "Ring",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 3,
    "core_discipline_w": 60,
    "pattern_w": 15,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 115,
    "hook_mode_multiplier": 1.62,
    "hook_mode_flat_w": 0,
    "total_w": 186,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
