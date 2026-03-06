# Amplify Binding

Boosts binding constraint flux as a focus targeting the inscribed anchor.

## Effect

A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a point pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Point | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 0 + 0 = 0 W
- Subtotal: 30 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **66 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Amplify Binding** | Triangle | Amplify | Affect | T2 | Binding | Constraint | Point | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Amplify Binding",
  "summary": "Boosts binding constraint flux as a focus targeting the inscribed anchor.",
  "effect_description": "A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a point pattern against where written across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 30,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 66,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "Here is a concise interpretation of the Solumora sigil as a practical spell note:\n\n**Spell Name:** Amplify Binding\n**Effect:** Boosts binding constraint flux to amplify magical connections between anchors.\n**Likely Use:** Enhancing personal or group magical bindings for increased power and stability.\n**Operational Constraint:** Requires physical proximity to the inscribed anchor, limiting range of effect."
}
```

## Ollama Interpretation

Here is a concise interpretation of the Solumora sigil as a practical spell note:

**Spell Name:** Amplify Binding
**Effect:** Boosts binding constraint flux to amplify magical connections between anchors.
**Likely Use:** Enhancing personal or group magical bindings for increased power and stability.
**Operational Constraint:** Requires physical proximity to the inscribed anchor, limiting range of effect.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
