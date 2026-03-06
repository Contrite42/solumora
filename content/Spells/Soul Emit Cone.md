# Soul Emit Cone

Releases soul flux as a fan spread at anchored reach, targeting the inscribed anchor with short timed hold with active regulation while it runs.

## Effect

Releases soul flux as a fan spread at anchored reach, targeting the inscribed anchor with short timed hold with active regulation while it runs. A circle emit/control recipe that channels soul discipline into soul output. It applies a cone pattern against where written across anchored reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Anchored | +0 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 5 + 0 + 0 = 15 W
- Subtotal: 4140 W
- Hook/Mode complexity multiplier: x1.35
- Hook/Mode flat addition: +0 W
- Total: **5589 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Emit Cone** | Circle | Emit | Control | T6 | Soul | Soul | Cone | Anchored | Timed Short | Where Written |

## AI Spell Data

```json
{
  "name": "Soul Emit Cone",
  "summary": "Releases soul flux as a fan spread at anchored reach, targeting the inscribed anchor with short timed hold with active regulation while it runs.",
  "effect_description": "Releases soul flux as a fan spread at anchored reach, targeting the inscribed anchor with short timed hold with active regulation while it runs. A circle emit/control recipe that channels soul discipline into soul output. It applies a cone pattern against where written across anchored reach with timed short persistence.",
  "hook": "Emit",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Cone",
  "reach": "Anchored",
  "persistence": "Timed Short",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 5,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4140,
    "hook_mode_multiplier": 1.35,
    "hook_mode_flat_w": 0,
    "total_w": 5589,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
