# Force Sense Beam

Detects force kinetic flux as a directed line at self reach, targeting the caster with immediate discharge by changing existing conditions.

## Effect

Detects force kinetic flux as a directed line at self reach, targeting the caster with immediate discharge by changing existing conditions. A square sense/affect recipe that channels force discipline into kinetic output. It applies a beam pattern against self across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Force | x2 multiplier |
| Output Mode | Kinetic | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 2 = 16 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 0 + 0 = 5 W
- Subtotal: 21 W
- Hook/Mode complexity multiplier: x1.8
- Hook/Mode flat addition: +0 W
- Total: **38 W**
- Required Control Tier: **T1**
- Rarity bucket: **Common**

## All Grimoire Row

| **Force Sense Beam** | Square | Sense | Affect | T1 | Force | Kinetic | Beam | Self | Immediate | Self |

## AI Spell Data

```json
{
  "name": "Force Sense Beam",
  "summary": "Detects force kinetic flux as a directed line at self reach, targeting the caster with immediate discharge by changing existing conditions.",
  "effect_description": "Detects force kinetic flux as a directed line at self reach, targeting the caster with immediate discharge by changing existing conditions. A square sense/affect recipe that channels force discipline into kinetic output. It applies a beam pattern against self across self reach with immediate persistence.",
  "hook": "Sense",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Force",
  "output_mode": "Kinetic",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 2,
    "core_discipline_w": 16,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 21,
    "hook_mode_multiplier": 1.8,
    "hook_mode_flat_w": 0,
    "total_w": 38,
    "required_tier": "T1",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
