# Amplified Binding Triangle

Boosts binding constraint flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.

## Effect

A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a field pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 0 + 0 + 0 + 0 = 60 W
- Subtotal: 90 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **198 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Amplified Binding Triangle** | Triangle | Amplify | Affect | T3 | Binding | Constraint | Field | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Amplified Binding Triangle",
  "summary": "Boosts binding constraint flux as a field volume at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.",
  "effect_description": "A triangle amplify/affect recipe that channels binding discipline into constraint output. It applies a field pattern against where written across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Field",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 60,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 90,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 198,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Amplified Binding Triangle Spell**\n\nThis spell amplifies the binding constraint flux in a targeted area, creating a field of binding discipline that affects existing conditions. Likely use: securing or reinforcing a previously bound entity or location.\n\nOperational constraint: Requires direct physical contact with the inscribed anchor to activate the immediate discharge effect."
}
```

## Ollama Interpretation

**Amplified Binding Triangle Spell**

This spell amplifies the binding constraint flux in a targeted area, creating a field of binding discipline that affects existing conditions. Likely use: securing or reinforcing a previously bound entity or location.

Operational constraint: Requires direct physical contact with the inscribed anchor to activate the immediate discharge effect.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
