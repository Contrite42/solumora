# Electric Sense Plane

Detects electric kinetic flux as a planar spread at line-of-sight reach, targeting the caster with long timed hold by changing existing conditions.

## Effect

Detects electric kinetic flux as a planar spread at line-of-sight reach, targeting the caster with long timed hold by changing existing conditions. A circle sense/affect recipe that channels electric discipline into kinetic output. It applies a plane pattern against self across line-of-sight reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Electric | x5 multiplier |
| Output Mode | Kinetic | +10 W premium |
| Pattern | Plane | +0 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 5 = 275 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 80 + 25 + 0 + 10 = 115 W
- Subtotal: 390 W
- Hook/Mode complexity multiplier: x1.8
- Hook/Mode flat addition: +0 W
- Total: **702 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Electric Sense Plane** | Circle | Sense | Affect | T4 | Electric | Kinetic | Plane | Line-of-Sight | Timed Long | Self |

## AI Spell Data

```json
{
  "name": "Electric Sense Plane",
  "summary": "Detects electric kinetic flux as a planar spread at line-of-sight reach, targeting the caster with long timed hold by changing existing conditions.",
  "effect_description": "Detects electric kinetic flux as a planar spread at line-of-sight reach, targeting the caster with long timed hold by changing existing conditions. A circle sense/affect recipe that channels electric discipline into kinetic output. It applies a plane pattern against self across line-of-sight reach with timed long persistence.",
  "hook": "Sense",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Electric",
  "output_mode": "Kinetic",
  "pattern": "Plane",
  "reach": "Line-of-Sight",
  "persistence": "Timed Long",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 5,
    "core_discipline_w": 275,
    "pattern_w": 0,
    "reach_w": 80,
    "persistence_w": 25,
    "target_w": 0,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 390,
    "hook_mode_multiplier": 1.8,
    "hook_mode_flat_w": 0,
    "total_w": 702,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
