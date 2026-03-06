# Electric Emit Field

Releases electric shock flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.

## Effect

Releases electric shock flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle emit/control recipe that channels electric discipline into shock output. It applies a field pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Electric | x5 multiplier |
| Output Mode | Shock | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 5 = 15 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 0 + 0 + 0 + 0 = 60 W
- Subtotal: 75 W
- Hook/Mode complexity multiplier: x1.35
- Hook/Mode flat addition: +0 W
- Total: **101 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Electric Emit Field** | Triangle | Emit | Control | T2 | Electric | Shock | Field | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Electric Emit Field",
  "summary": "Releases electric shock flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs.",
  "effect_description": "Releases electric shock flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge with active regulation while it runs. A triangle emit/control recipe that channels electric discipline into shock output. It applies a field pattern against where written across self reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Control",
  "shape": "Triangle",
  "discipline": "Electric",
  "output_mode": "Shock",
  "pattern": "Field",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 5,
    "core_discipline_w": 15,
    "pattern_w": 60,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 75,
    "hook_mode_multiplier": 1.35,
    "hook_mode_flat_w": 0,
    "total_w": 101,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
