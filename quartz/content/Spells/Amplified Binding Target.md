# Amplified Binding Target

Boosts binding constraint flux as a directed line at self reach, targeting the inscribed anchor.

## Effect

A triangle amplify/affect recipe that channels binding discipline into constraint output.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Constraint | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 0 + 0 = 5 W
- Subtotal: 35 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **77 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Amplified Binding Target** | Triangle | Amplify | Affect | T2 | Binding | Constraint | Beam | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Amplified Binding Target",
  "summary": "Boosts binding constraint flux as a directed line at self reach, targeting the inscribed anchor.",
  "effect_description": "A triangle amplify/affect recipe that channels binding discipline into constraint output.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Constraint",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 10,
    "core_discipline_w": 30,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 35,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 77,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Spell Note:** Amplified Binding Target\n\n* **Effect:** Boosts binding constraint at a directed line extending from the caster's body.\n* **Likely Use:** Binding and containment magic, particularly for anchoring or stabilizing magical connections.\n* **Operational Constraint:** Requires a clear anchor or target written on a surface to direct the amplified binding flux."
}
```

## Ollama Interpretation

**Spell Note:** Amplified Binding Target

* **Effect:** Boosts binding constraint at a directed line extending from the caster's body.
* **Likely Use:** Binding and containment magic, particularly for anchoring or stabilizing magical connections.
* **Operational Constraint:** Requires a clear anchor or target written on a surface to direct the amplified binding flux.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
