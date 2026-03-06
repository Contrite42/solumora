# Plane Creation

The spell creates a raw magical plane on the caster's surface that lasts only momentarily and is not sustained beyond its initial emission.

## Effect

The spell creates a raw magical plane on the caster's surface that lasts only momentarily and is not sustained beyond its initial emission. A square emit/control recipe that channels raw discipline into raw output. It applies a plane pattern against surface across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Emit | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Raw | x1 multiplier |
| Output Mode | Raw | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Surface | +5 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 1 = 8 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 5 + 0 = 5 W
- Subtotal: 13 W
- Hook/Mode complexity multiplier: x1.35
- Hook/Mode flat addition: +0 W
- Total: **18 W**
- Required Control Tier: **T1**
- Rarity bucket: **Common**

## All Grimoire Row

| **Plane Creation** | Square | Emit | Control | T1 | Raw | Raw | Plane | Self | Immediate | Surface |

## AI Spell Data

```json
{
  "name": "Plane Creation",
  "summary": "The spell creates a raw magical plane on the caster's surface that lasts only momentarily and is not sustained beyond its initial emission.",
  "effect_description": "The spell creates a raw magical plane on the caster's surface that lasts only momentarily and is not sustained beyond its initial emission. A square emit/control recipe that channels raw discipline into raw output. It applies a plane pattern against surface across self reach with immediate persistence.",
  "hook": "Emit",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Raw",
  "output_mode": "Raw",
  "pattern": "Plane",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Surface",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 1,
    "core_discipline_w": 8,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 5,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 13,
    "hook_mode_multiplier": 1.35,
    "hook_mode_flat_w": 0,
    "total_w": 18,
    "required_tier": "T1",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "Here's the interpretation of the Solumora sigil as a practical spell note:\n\n**Spell Name:** Plane Creation\n**Effect:** Creates a raw magical plane on your body that lasts for a brief moment.\n**Likely Use:** Emergency situations where you need a temporary, intense magical effect.\n**Operational Constraint:** The spell only works immediately and has no sustained effect beyond its initial emission."
}
```

## Ollama Interpretation

Here's the interpretation of the Solumora sigil as a practical spell note:

**Spell Name:** Plane Creation
**Effect:** Creates a raw magical plane on your body that lasts for a brief moment.
**Likely Use:** Emergency situations where you need a temporary, intense magical effect.
**Operational Constraint:** The spell only works immediately and has no sustained effect beyond its initial emission.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
