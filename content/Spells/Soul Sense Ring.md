# Soul Sense Ring

Detects soul flux as a ring perimeter at short reach, targeting the inscribed anchor with short timed hold with active regulation while it runs.

## Effect

Detects soul flux as a ring perimeter at short reach, targeting the inscribed anchor with short timed hold with active regulation while it runs. A circle sense/control recipe that channels soul discipline into soul output. It applies a ring pattern against where written across short reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Sense | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Short | +5 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 5 + 5 + 0 + 0 = 25 W
- Subtotal: 4150 W
- Hook/Mode complexity multiplier: x2.43
- Hook/Mode flat addition: +0 W
- Total: **10084 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Sense Ring** | Circle | Sense | Control | T6 | Soul | Soul | Ring | Short | Timed Short | Where Written |

## AI Spell Data

```json
{
  "name": "Soul Sense Ring",
  "summary": "Detects soul flux as a ring perimeter at short reach, targeting the inscribed anchor with short timed hold with active regulation while it runs.",
  "effect_description": "Detects soul flux as a ring perimeter at short reach, targeting the inscribed anchor with short timed hold with active regulation while it runs. A circle sense/control recipe that channels soul discipline into soul output. It applies a ring pattern against where written across short reach with timed short persistence.",
  "hook": "Sense",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Ring",
  "reach": "Short",
  "persistence": "Timed Short",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 15,
    "reach_w": 5,
    "persistence_w": 5,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4150,
    "hook_mode_multiplier": 2.43,
    "hook_mode_flat_w": 0,
    "total_w": 10084,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
