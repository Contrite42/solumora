# Soul Trigger Beam

Arms soul neuro flux as a directed line at long reach, targeting the caster with short timed hold by changing existing conditions.

## Effect

Arms soul neuro flux as a directed line at long reach, targeting the caster with short timed hold by changing existing conditions. A circle trigger/affect recipe that channels soul discipline into neuro output. It applies a beam pattern against self across long reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Trigger | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Neuro | +30 W premium |
| Pattern | Beam | +5 W |
| Reach | Long | +40 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 40 + 5 + 0 + 30 = 80 W
- Subtotal: 4205 W
- Hook/Mode complexity multiplier: x1.8
- Hook/Mode flat addition: +0 W
- Total: **7569 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Trigger Beam** | Circle | Trigger | Affect | T6 | Soul | Neuro | Beam | Long | Timed Short | Self |

## AI Spell Data

```json
{
  "name": "Soul Trigger Beam",
  "summary": "Arms soul neuro flux as a directed line at long reach, targeting the caster with short timed hold by changing existing conditions.",
  "effect_description": "Arms soul neuro flux as a directed line at long reach, targeting the caster with short timed hold by changing existing conditions. A circle trigger/affect recipe that channels soul discipline into neuro output. It applies a beam pattern against self across long reach with timed short persistence.",
  "hook": "Trigger",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Neuro",
  "pattern": "Beam",
  "reach": "Long",
  "persistence": "Timed Short",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 5,
    "reach_w": 40,
    "persistence_w": 5,
    "target_w": 0,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4205,
    "hook_mode_multiplier": 1.8,
    "hook_mode_flat_w": 0,
    "total_w": 7569,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
