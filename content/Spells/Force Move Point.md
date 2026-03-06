# Force Move Point

Repositions force kinetic flux as a point focus at long reach, targeting one individual with short timed hold by changing existing conditions.

## Effect

Repositions force kinetic flux as a point focus at long reach, targeting one individual with short timed hold by changing existing conditions. A circle move/affect recipe that channels force discipline into kinetic output. It applies a point pattern against individual across long reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Force | x2 multiplier |
| Output Mode | Kinetic | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Long | +40 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Individual | +8 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 2 = 110 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 40 + 5 + 8 + 0 = 53 W
- Subtotal: 163 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **244 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Force Move Point** | Circle | Move | Affect | T3 | Force | Kinetic | Point | Long | Timed Short | Individual |

## AI Spell Data

```json
{
  "name": "Force Move Point",
  "summary": "Repositions force kinetic flux as a point focus at long reach, targeting one individual with short timed hold by changing existing conditions.",
  "effect_description": "Repositions force kinetic flux as a point focus at long reach, targeting one individual with short timed hold by changing existing conditions. A circle move/affect recipe that channels force discipline into kinetic output. It applies a point pattern against individual across long reach with timed short persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Force",
  "output_mode": "Kinetic",
  "pattern": "Point",
  "reach": "Long",
  "persistence": "Timed Short",
  "target_spec": "Individual",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 2,
    "core_discipline_w": 110,
    "pattern_w": 0,
    "reach_w": 40,
    "persistence_w": 5,
    "target_w": 8,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 163,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 244,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
