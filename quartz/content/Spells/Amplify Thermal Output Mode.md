# Amplify Thermal Output Mode

The spell amplifies sound to a thermal output mode at the point where it is written, persisting as long as it remains latched.

## Effect

The spell amplifies sound to a thermal output mode at the point where it is written, persisting as long as it remains latched. A circle amplify/affect recipe that channels sound discipline into thermal output. It applies a sphere pattern against where written across line-of-sight reach with latched persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Thermal | +30 W premium |
| Pattern | Sphere | +30 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Latched | +40 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 4 = 220 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 80 + 40 + 0 + 30 = 180 W
- Subtotal: 400 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **880 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Amplify Thermal Output Mode** | Circle | Amplify | Affect | T4 | Sound | Thermal | Sphere | Line-of-Sight | Latched | Where Written |

## AI Spell Data

```json
{
  "name": "Amplify Thermal Output Mode",
  "summary": "The spell amplifies sound to a thermal output mode at the point where it is written, persisting as long as it remains latched.",
  "effect_description": "The spell amplifies sound to a thermal output mode at the point where it is written, persisting as long as it remains latched. A circle amplify/affect recipe that channels sound discipline into thermal output. It applies a sphere pattern against where written across line-of-sight reach with latched persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Sound",
  "output_mode": "Thermal",
  "pattern": "Sphere",
  "reach": "Line-of-Sight",
  "persistence": "Latched",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 4,
    "core_discipline_w": 220,
    "pattern_w": 30,
    "reach_w": 80,
    "persistence_w": 40,
    "target_w": 0,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 400,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 880,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "Here is the interpretation of the Solumora sigil as a practical spell note:\n\n**Spell Name:** Amplify Thermal Output Mode\n**Effect:** Converts sound to thermal energy at the point of inscription, lasting as long as it remains active.\n**Likely Use:** Siege warfare or demolitions, where heat can be applied to break down fortifications or ignite flammable materials.\n**Operational Constraint:** Requires a clear line-of-sight to the target area and cannot be used in enclosed spaces due to the risk of accidental ignition."
}
```

## Ollama Interpretation

Here is the interpretation of the Solumora sigil as a practical spell note:

**Spell Name:** Amplify Thermal Output Mode
**Effect:** Converts sound to thermal energy at the point of inscription, lasting as long as it remains active.
**Likely Use:** Siege warfare or demolitions, where heat can be applied to break down fortifications or ignite flammable materials.
**Operational Constraint:** Requires a clear line-of-sight to the target area and cannot be used in enclosed spaces due to the risk of accidental ignition.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
