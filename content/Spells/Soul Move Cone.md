# Soul Move Cone

Repositions soul flux as a fan spread at line-of-sight reach, targeting a filtered selection with short timed hold by changing existing conditions.

## Effect

Repositions soul flux as a fan spread at line-of-sight reach, targeting a filtered selection with short timed hold by changing existing conditions. A circle move/affect recipe that channels soul discipline into soul output. It applies a cone pattern against filter across line-of-sight reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 80 + 5 + 60 + 0 = 155 W
- Subtotal: 4280 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **6420 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Move Cone** | Circle | Move | Affect | T6 | Soul | Soul | Cone | Line-of-Sight | Timed Short | Filter |

## AI Spell Data

```json
{
  "name": "Soul Move Cone",
  "summary": "Repositions soul flux as a fan spread at line-of-sight reach, targeting a filtered selection with short timed hold by changing existing conditions.",
  "effect_description": "Repositions soul flux as a fan spread at line-of-sight reach, targeting a filtered selection with short timed hold by changing existing conditions. A circle move/affect recipe that channels soul discipline into soul output. It applies a cone pattern against filter across line-of-sight reach with timed short persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cone",
  "reach": "Line-of-Sight",
  "persistence": "Timed Short",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 10,
    "reach_w": 80,
    "persistence_w": 5,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4280,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 6420,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
