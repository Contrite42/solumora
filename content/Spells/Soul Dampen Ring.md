# Soul Dampen Ring

Reduces soul flux as a ring perimeter at linked reach, targeting a filtered selection with immediate discharge with active regulation while it runs.

## Effect

Reduces soul flux as a ring perimeter at linked reach, targeting a filtered selection with immediate discharge with active regulation while it runs. A circle dampen/control recipe that channels soul discipline into soul output. It applies a ring pattern against filter across linked reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Linked | +150 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 150 + 0 + 60 + 0 = 225 W
- Subtotal: 4350 W
- Hook/Mode complexity multiplier: x2.565
- Hook/Mode flat addition: +0 W
- Total: **11158 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Dampen Ring** | Circle | Dampen | Control | T6 | Soul | Soul | Ring | Linked | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Soul Dampen Ring",
  "summary": "Reduces soul flux as a ring perimeter at linked reach, targeting a filtered selection with immediate discharge with active regulation while it runs.",
  "effect_description": "Reduces soul flux as a ring perimeter at linked reach, targeting a filtered selection with immediate discharge with active regulation while it runs. A circle dampen/control recipe that channels soul discipline into soul output. It applies a ring pattern against filter across linked reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Ring",
  "reach": "Linked",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 15,
    "reach_w": 150,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4350,
    "hook_mode_multiplier": 2.565,
    "hook_mode_flat_w": 0,
    "total_w": 11158,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
