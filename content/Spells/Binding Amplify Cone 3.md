# Binding Amplify Cone 3

Boosts binding constraint flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.

## Effect

A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a cone pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Cone | +10 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  10 + 0 + 0 + 0 + 0 = 10 W
- Subtotal: 40 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **88 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Binding Amplify Cone 3** | Triangle | Amplify | Affect | T2 | Binding | Constraint | Cone | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Binding Amplify Cone 3",
  "summary": "Boosts binding constraint flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.",
  "effect_description": "A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a cone pattern against where written across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Cone",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 10,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 40,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 88,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "This sigil, \"Binding Amplify Cone 3\", amplifies binding constraint flux in a fan-like pattern at the user's reach. It targets an inscribed anchor and causes immediate discharge by altering existing conditions.\n\nLikely use: Defense or protective magic for anchoring a spell within one's personal space.\n\nOperational constraint: Requires precise inscription of the target anchor to ensure accurate targeting and effective amplification."
}
```

## Ollama Interpretation

This sigil, "Binding Amplify Cone 3", amplifies binding constraint flux in a fan-like pattern at the user's reach. It targets an inscribed anchor and causes immediate discharge by altering existing conditions.

Likely use: Defense or protective magic for anchoring a spell within one's personal space.

Operational constraint: Requires precise inscription of the target anchor to ensure accurate targeting and effective amplification.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
