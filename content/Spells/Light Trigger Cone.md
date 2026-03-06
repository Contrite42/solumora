# Light Trigger Cone

Arms light photonic flux as a fan spread at long reach, targeting a marked signature with short timed hold by changing existing conditions.

## Effect

Arms light photonic flux as a fan spread at long reach, targeting a marked signature with short timed hold by changing existing conditions. A circle trigger/affect recipe that channels light discipline into photonic output. It applies a cone pattern against marked across long reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Trigger | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Light | x3 multiplier |
| Output Mode | Photonic | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Long | +40 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 3 = 165 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 40 + 5 + 15 + 0 = 70 W
- Subtotal: 235 W
- Hook/Mode complexity multiplier: x1.8
- Hook/Mode flat addition: +0 W
- Total: **423 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Light Trigger Cone** | Circle | Trigger | Affect | T4 | Light | Photonic | Cone | Long | Timed Short | Marked |

## AI Spell Data

```json
{
  "name": "Light Trigger Cone",
  "summary": "Arms light photonic flux as a fan spread at long reach, targeting a marked signature with short timed hold by changing existing conditions.",
  "effect_description": "Arms light photonic flux as a fan spread at long reach, targeting a marked signature with short timed hold by changing existing conditions. A circle trigger/affect recipe that channels light discipline into photonic output. It applies a cone pattern against marked across long reach with timed short persistence.",
  "hook": "Trigger",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Light",
  "output_mode": "Photonic",
  "pattern": "Cone",
  "reach": "Long",
  "persistence": "Timed Short",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 3,
    "core_discipline_w": 165,
    "pattern_w": 10,
    "reach_w": 40,
    "persistence_w": 5,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 235,
    "hook_mode_multiplier": 1.8,
    "hook_mode_flat_w": 0,
    "total_w": 423,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
