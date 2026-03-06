# Force Filter Field

Screens force kinetic flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Screens force kinetic flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A square filter/control recipe that channels force discipline into kinetic output. It applies a field pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Force | x2 multiplier |
| Output Mode | Kinetic | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 2 = 16 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 0 + 0 + 0 + 0 = 60 W
- Subtotal: 76 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **164 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Force Filter Field** | Square | Filter | Control | T3 | Force | Kinetic | Field | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Force Filter Field",
  "summary": "Screens force kinetic flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Screens force kinetic flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A square filter/control recipe that channels force discipline into kinetic output. It applies a field pattern against where written across self reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Force",
  "output_mode": "Kinetic",
  "pattern": "Field",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 2,
    "core_discipline_w": 16,
    "pattern_w": 60,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 76,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 164,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
