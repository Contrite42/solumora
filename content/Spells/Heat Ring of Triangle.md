# Heat Ring of Triangle

This spell creates a triangular ring of heat on its written location that lasts only briefly.

## Effect

This spell creates a triangular ring of heat on its written location that lasts only briefly. A triangle shape/create recipe that channels chemical discipline into thermal output. It applies a ring pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Chemical | x5 multiplier |
| Output Mode | Thermal | +10 W premium |
| Pattern | Ring | +15 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 5 = 15 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 0 + 0 + 0 + 10 = 25 W
- Subtotal: 40 W
- Hook/Mode complexity multiplier: x1.38
- Hook/Mode flat addition: +0 W
- Total: **55 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Heat Ring of Triangle** | Triangle | Shape | Create | T2 | Chemical | Thermal | Ring | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Heat Ring of Triangle",
  "summary": "This spell creates a triangular ring of heat on its written location that lasts only briefly.",
  "effect_description": "This spell creates a triangular ring of heat on its written location that lasts only briefly. A triangle shape/create recipe that channels chemical discipline into thermal output. It applies a ring pattern against where written across self reach with immediate persistence.",
  "hook": "Shape",
  "mode": "Create",
  "shape": "Triangle",
  "discipline": "Chemical",
  "output_mode": "Thermal",
  "pattern": "Ring",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 5,
    "core_discipline_w": 15,
    "pattern_w": 15,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 40,
    "hook_mode_multiplier": 1.38,
    "hook_mode_flat_w": 0,
    "total_w": 55,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "Here is a concise interpretation of the spell note:\n\n**Name:** Heat Ring of Triangle\n**Description:** Creates a brief triangular ring of heat on its written location.\n**Likely Use:** Briefly warming or irritating a small area, perhaps to mark a surface or deter pests.\n**Operational Constraint:** Lasts only briefly (immediate persistence), requiring re-casting for sustained effects."
}
```

## Ollama Interpretation

Here is a concise interpretation of the spell note:

**Name:** Heat Ring of Triangle
**Description:** Creates a brief triangular ring of heat on its written location.
**Likely Use:** Briefly warming or irritating a small area, perhaps to mark a surface or deter pests.
**Operational Constraint:** Lasts only briefly (immediate persistence), requiring re-casting for sustained effects.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
