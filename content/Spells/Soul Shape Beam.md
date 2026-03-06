# Soul Shape Beam

Refines soul flux as a directed line at short reach, targeting a filtered selection with latched hold by changing existing conditions.

## Effect

Refines soul flux as a directed line at short reach, targeting a filtered selection with latched hold by changing existing conditions. A circle shape/affect recipe that channels soul discipline into soul output. It applies a beam pattern against filter across short reach with latched persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Short | +5 W |
| Persistence | Latched | +40 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 5 + 40 + 60 + 0 = 110 W
- Subtotal: 4235 W
- Hook/Mode complexity multiplier: x1.2
- Hook/Mode flat addition: +0 W
- Total: **5082 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Shape Beam** | Circle | Shape | Affect | T6 | Soul | Soul | Beam | Short | Latched | Filter |

## AI Spell Data

```json
{
  "name": "Soul Shape Beam",
  "summary": "Refines soul flux as a directed line at short reach, targeting a filtered selection with latched hold by changing existing conditions.",
  "effect_description": "Refines soul flux as a directed line at short reach, targeting a filtered selection with latched hold by changing existing conditions. A circle shape/affect recipe that channels soul discipline into soul output. It applies a beam pattern against filter across short reach with latched persistence.",
  "hook": "Shape",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Beam",
  "reach": "Short",
  "persistence": "Latched",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 5,
    "reach_w": 5,
    "persistence_w": 40,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4235,
    "hook_mode_multiplier": 1.2,
    "hook_mode_flat_w": 0,
    "total_w": 5082,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
