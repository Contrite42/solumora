# Constraint Volume Anchor

Boosts binding constraint flux as a column volume at self reach, targeting the inscribed anchor.

## Effect

A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a cylinder pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Cylinder | +20 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  20 + 0 + 0 + 0 + 0 = 20 W
- Subtotal: 50 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **110 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Constraint Volume Anchor** | Triangle | Amplify | Affect | T2 | Binding | Constraint | Cylinder | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Constraint Volume Anchor",
  "summary": "Boosts binding constraint flux as a column volume at self reach, targeting the inscribed anchor.",
  "effect_description": "A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a cylinder pattern against where written across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Cylinder",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 20,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 50,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 110,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "This spell note is for a \"Constraint Volume Anchor\" sigil. It does:\n\n* Boosts binding constraint flux as a column volume at self reach\n* Targets the inscribed anchor with a cylinder pattern\n\nLikely use: Anchoring and stabilizing structures or entities.\n\nOperational constraint: Requires immediate persistence, meaning the effect must be sustained in real-time without delay."
}
```

## Ollama Interpretation

This spell note is for a "Constraint Volume Anchor" sigil. It does:

* Boosts binding constraint flux as a column volume at self reach
* Targets the inscribed anchor with a cylinder pattern

Likely use: Anchoring and stabilizing structures or entities.

Operational constraint: Requires immediate persistence, meaning the effect must be sustained in real-time without delay.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
