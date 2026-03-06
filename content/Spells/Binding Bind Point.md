# Binding Bind Point

Anchors binding raw flux as a point focus at self reach, targeting a marked signature with immediate discharge by creating a fresh flux expression.

## Effect

Anchors binding raw flux as a point focus at self reach, targeting a marked signature with immediate discharge by creating a fresh flux expression. A square bind/create recipe that channels binding discipline into raw output. It applies a point pattern against marked across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Bind | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Point | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 10 = 80 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 15 + 30 = 45 W
- Subtotal: 125 W
- Hook/Mode complexity multiplier: x1.8399999999999999
- Hook/Mode flat addition: +0 W
- Total: **230 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Binding Bind Point** | Square | Bind | Create | T3 | Binding | Raw | Point | Self | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Binding Bind Point",
  "summary": "Anchors binding raw flux as a point focus at self reach, targeting a marked signature with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Anchors binding raw flux as a point focus at self reach, targeting a marked signature with immediate discharge by creating a fresh flux expression. A square bind/create recipe that channels binding discipline into raw output. It applies a point pattern against marked across self reach with immediate persistence.",
  "hook": "Bind",
  "mode": "Create",
  "shape": "Square",
  "discipline": "Binding",
  "output_mode": "Raw",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 10,
    "core_discipline_w": 80,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 125,
    "hook_mode_multiplier": 1.8399999999999999,
    "hook_mode_flat_w": 0,
    "total_w": 230,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
