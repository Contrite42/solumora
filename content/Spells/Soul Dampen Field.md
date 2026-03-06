# Soul Dampen Field

Reduces soul sonic flux as a field volume at self reach, targeting a filtered selection with immediate discharge by changing existing conditions.

## Effect

Reduces soul sonic flux as a field volume at self reach, targeting a filtered selection with immediate discharge by changing existing conditions. A square dampen/affect recipe that channels soul discipline into sonic output. It applies a field pattern against filter across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Sonic | +60 W premium |
| Pattern | Field | +60 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 75 = 600 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 0 + 0 + 60 + 60 = 180 W
- Subtotal: 780 W
- Hook/Mode complexity multiplier: x1.9
- Hook/Mode flat addition: +0 W
- Total: **1482 W**
- Required Control Tier: **T5**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Dampen Field** | Square | Dampen | Affect | T5 | Soul | Sonic | Field | Self | Immediate | Filter |

## AI Spell Data

```json
{
  "name": "Soul Dampen Field",
  "summary": "Reduces soul sonic flux as a field volume at self reach, targeting a filtered selection with immediate discharge by changing existing conditions.",
  "effect_description": "Reduces soul sonic flux as a field volume at self reach, targeting a filtered selection with immediate discharge by changing existing conditions. A square dampen/affect recipe that channels soul discipline into sonic output. It applies a field pattern against filter across self reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Soul",
  "output_mode": "Sonic",
  "pattern": "Field",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 75,
    "core_discipline_w": 600,
    "pattern_w": 60,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 60,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 780,
    "hook_mode_multiplier": 1.9,
    "hook_mode_flat_w": 0,
    "total_w": 1482,
    "required_tier": "T5",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
