# Soul Bind Point

Anchors soul thermal flux as a point focus at touch reach, targeting a marked signature with long timed hold by changing existing conditions.

## Effect

Anchors soul thermal flux as a point focus at touch reach, targeting a marked signature with long timed hold by changing existing conditions. A circle bind/affect recipe that channels soul discipline into thermal output. It applies a point pattern against marked across touch reach with timed long persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Bind | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Thermal | +60 W premium |
| Pattern | Point | +0 W |
| Reach | Touch | +2 W |
| Persistence | Timed Long | +25 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 2 + 25 + 15 + 60 = 102 W
- Subtotal: 4227 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **6763 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Bind Point** | Circle | Bind | Affect | T6 | Soul | Thermal | Point | Touch | Timed Long | Marked |

## AI Spell Data

```json
{
  "name": "Soul Bind Point",
  "summary": "Anchors soul thermal flux as a point focus at touch reach, targeting a marked signature with long timed hold by changing existing conditions.",
  "effect_description": "Anchors soul thermal flux as a point focus at touch reach, targeting a marked signature with long timed hold by changing existing conditions. A circle bind/affect recipe that channels soul discipline into thermal output. It applies a point pattern against marked across touch reach with timed long persistence.",
  "hook": "Bind",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Thermal",
  "pattern": "Point",
  "reach": "Touch",
  "persistence": "Timed Long",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 2,
    "persistence_w": 25,
    "target_w": 15,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 4227,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 6763,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
