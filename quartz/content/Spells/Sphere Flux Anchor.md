# Sphere Flux Anchor

Boosts binding constraint flux as a spherical envelope at self reach, targeting the inscribed anchor.

## Effect

A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a sphere pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 0 + 0 + 0 + 0 = 30 W
- Subtotal: 60 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **132 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Sphere Flux Anchor** | Triangle | Amplify | Affect | T3 | Binding | Constraint | Sphere | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Sphere Flux Anchor",
  "summary": "Boosts binding constraint flux as a spherical envelope at self reach, targeting the inscribed anchor.",
  "effect_description": "A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a sphere pattern against where written across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Sphere",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 30,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 60,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 132,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "Here's a practical interpretation of the Solumora sigil as a spell note:\n\n**Spell Name:** Sphere Flux Anchor\n**Effect:** Boosts binding constraint flux in a spherical pattern around yourself.\n**Likely Use:** Defending against incoming magical attacks by stabilizing your energy field.\n**Operational Constraint:** Requires 3 units of Shape Base cost, which may be impractical for low-level casters."
}
```

## Ollama Interpretation

Here's a practical interpretation of the Solumora sigil as a spell note:

**Spell Name:** Sphere Flux Anchor
**Effect:** Boosts binding constraint flux in a spherical pattern around yourself.
**Likely Use:** Defending against incoming magical attacks by stabilizing your energy field.
**Operational Constraint:** Requires 3 units of Shape Base cost, which may be impractical for low-level casters.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
