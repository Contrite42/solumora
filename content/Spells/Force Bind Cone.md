# Force Bind Cone

Anchors force kinetic flux as a fan spread at self reach, targeting a marked signature with immediate discharge with active regulation while it runs.

## Effect

Anchors force kinetic flux as a fan spread at self reach, targeting a marked signature with immediate discharge with active regulation while it runs. A square bind/control recipe that channels force discipline into kinetic output. It applies a cone pattern against marked across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Bind | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Force | x2 multiplier |
| Output Mode | Kinetic | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 2 = 16 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 15 + 0 = 25 W
- Subtotal: 41 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **89 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Force Bind Cone** | Square | Bind | Control | T2 | Force | Kinetic | Cone | Self | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Force Bind Cone",
  "summary": "Anchors force kinetic flux as a fan spread at self reach, targeting a marked signature with immediate discharge with active regulation while it runs.",
  "effect_description": "Anchors force kinetic flux as a fan spread at self reach, targeting a marked signature with immediate discharge with active regulation while it runs. A square bind/control recipe that channels force discipline into kinetic output. It applies a cone pattern against marked across self reach with immediate persistence.",
  "hook": "Bind",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Force",
  "output_mode": "Kinetic",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 2,
    "core_discipline_w": 16,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 41,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 89,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
