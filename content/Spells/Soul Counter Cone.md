# Soul Counter Cone

Disrupts soul flux as a fan spread at self reach, targeting the caster with immediate discharge with active regulation while it runs.

## Effect

Disrupts soul flux as a fan spread at self reach, targeting the caster with immediate discharge with active regulation while it runs. A square counter/control recipe that channels soul discipline into soul output. It applies a cone pattern against self across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Counter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 75 = 600 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 0 + 0 = 10 W
- Subtotal: 610 W
- Hook/Mode complexity multiplier: x3.5100000000000002
- Hook/Mode flat addition: +0 W
- Total: **2141 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Counter Cone** | Square | Counter | Control | T5 | Soul | Soul | Cone | Self | Immediate | Self |

## AI Spell Data

```json
{
  "name": "Soul Counter Cone",
  "summary": "Disrupts soul flux as a fan spread at self reach, targeting the caster with immediate discharge with active regulation while it runs.",
  "effect_description": "Disrupts soul flux as a fan spread at self reach, targeting the caster with immediate discharge with active regulation while it runs. A square counter/control recipe that channels soul discipline into soul output. It applies a cone pattern against self across self reach with immediate persistence.",
  "hook": "Counter",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 75,
    "core_discipline_w": 600,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 610,
    "hook_mode_multiplier": 3.5100000000000002,
    "hook_mode_flat_w": 0,
    "total_w": 2141,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
