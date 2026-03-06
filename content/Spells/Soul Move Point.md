# Soul Move Point

Repositions soul flux as a point focus at short reach, targeting a prepared surface with short timed hold by changing existing conditions.

## Effect

Repositions soul flux as a point focus at short reach, targeting a prepared surface with short timed hold by changing existing conditions. A circle move/affect recipe that channels soul discipline into soul output. It applies a point pattern against surface across short reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Short | +5 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 5 + 5 + 5 + 0 = 15 W
- Subtotal: 4140 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **6210 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Move Point** | Circle | Move | Affect | T6 | Soul | Soul | Point | Short | Timed Short | Surface |

## AI Spell Data

```json
{
  "name": "Soul Move Point",
  "summary": "Repositions soul flux as a point focus at short reach, targeting a prepared surface with short timed hold by changing existing conditions.",
  "effect_description": "Repositions soul flux as a point focus at short reach, targeting a prepared surface with short timed hold by changing existing conditions. A circle move/affect recipe that channels soul discipline into soul output. It applies a point pattern against surface across short reach with timed short persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Point",
  "reach": "Short",
  "persistence": "Timed Short",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 5,
    "persistence_w": 5,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4140,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 6210,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
