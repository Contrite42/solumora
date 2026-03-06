# Raw Cargo Stitch

Secures a single object against routine jolts using neutral flux.

## Effect

Writes a compact lock-state into one marked object so handling stress does not break its tuned balance.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Bind | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Object | +2 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 1 = 8 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 2 + 0 = 2 W
- Subtotal: 10 W
- Hook/Mode complexity multiplier: x1.6
- Hook/Mode flat addition: +0 W
- Total: **16 W**
- Required Control Tier: **T1**
- Rarity bucket: **Common**

## All Grimoire Row

| **Raw Cargo Stitch** | Square | Bind | Affect | T1 | Raw | Raw | Point | Self | Immediate | Object |

## AI Spell Data

```json
{
  "name": "Raw Cargo Stitch",
  "summary": "Secures a single object against routine jolts using neutral flux.",
  "effect_description": "Writes a compact lock-state into one marked object so handling stress does not break its tuned balance.",
  "hook": "Bind",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Object",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 1,
    "core_discipline_w": 8,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 2,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 10,
    "hook_mode_multiplier": 1.6,
    "hook_mode_flat_w": 0,
    "total_w": 16,
    "required_tier": "T1",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
