# Heat Move Beam

Repositions heat thermal flux as a directed line at self reach, targeting the caster with immediate discharge by creating a fresh flux expression.

## Effect

Repositions heat thermal flux as a directed line at self reach, targeting the caster with immediate discharge by creating a fresh flux expression. A square move/create recipe that channels heat discipline into thermal output. It applies a beam pattern against self across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Heat | x2 multiplier |
| Output Mode | Thermal | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 2 = 16 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 0 + 0 = 5 W
- Subtotal: 21 W
- Hook/Mode complexity multiplier: x1.7249999999999999
- Hook/Mode flat addition: +0 W
- Total: **36 W**
- Required Control Tier: **T1**
- Rarity bucket: **Common**

## All Grimoire Row

| **Heat Move Beam** | Square | Move | Create | T1 | Heat | Thermal | Beam | Self | Immediate | Self |

## AI Spell Data

```json
{
  "name": "Heat Move Beam",
  "summary": "Repositions heat thermal flux as a directed line at self reach, targeting the caster with immediate discharge by creating a fresh flux expression.",
  "effect_description": "Repositions heat thermal flux as a directed line at self reach, targeting the caster with immediate discharge by creating a fresh flux expression. A square move/create recipe that channels heat discipline into thermal output. It applies a beam pattern against self across self reach with immediate persistence.",
  "hook": "Move",
  "mode": "Create",
  "shape": "Square",
  "discipline": "Heat",
  "output_mode": "Thermal",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 2,
    "core_discipline_w": 16,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 21,
    "hook_mode_multiplier": 1.7249999999999999,
    "hook_mode_flat_w": 0,
    "total_w": 36,
    "required_tier": "T1",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
