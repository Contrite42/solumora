# Light Amplify Cone 2

Boosts light photonic flux as a fan spread at self reach, targeting a filtered selection with immediate discharge with active regulation while it runs.

## Effect

Boosts light photonic flux as a fan spread at self reach, targeting a filtered selection with immediate discharge with active regulation while it runs. A square amplify/control recipe that channels light discipline into photonic output. It applies a cone pattern against filter across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Light | x3 multiplier |
| Output Mode | Photonic | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 3 = 24 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 60 + 0 = 70 W
- Subtotal: 94 W
- Hook/Mode complexity multiplier: x2.9700000000000006
- Hook/Mode flat addition: +0 W
- Total: **279 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Light Amplify Cone 2** | Square | Amplify | Control | T3 | Light | Photonic | Cone | Self | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Light Amplify Cone 2",
  "summary": "Boosts light photonic flux as a fan spread at self reach, targeting a filtered selection with immediate discharge with active regulation while it runs.",
  "effect_description": "Boosts light photonic flux as a fan spread at self reach, targeting a filtered selection with immediate discharge with active regulation while it runs. A square amplify/control recipe that channels light discipline into photonic output. It applies a cone pattern against filter across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Light",
  "output_mode": "Photonic",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 3,
    "core_discipline_w": 24,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 94,
    "hook_mode_multiplier": 2.9700000000000006,
    "hook_mode_flat_w": 0,
    "total_w": 279,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
