# Beam Anchor Amp

Boosts binding kinetic flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.

## Effect

A triangle amplify/affect recipe that channels binding discipline into kinetic output. It applies a beam pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Binding | x10 multiplier |
| Output Mode | Kinetic | +10 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 10 = 30 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 0 + 10 = 15 W
- Subtotal: 45 W
- Hook/Mode complexity multiplier: x2.2
- Hook/Mode flat addition: +0 W
- Total: **99 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Beam Anchor Amp** | Triangle | Amplify | Affect | T2 | Binding | Kinetic | Beam | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Beam Anchor Amp",
  "summary": "Boosts binding kinetic flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.",
  "effect_description": "A triangle amplify/affect recipe that channels binding discipline into kinetic output. It applies a beam pattern against where written across self reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Binding",
  "output_mode": "Kinetic",
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
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 45,
    "hook_mode_multiplier": 2.2,
    "hook_mode_flat_w": 0,
    "total_w": 99,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Spell Note: Beam Anchor Amp**\n\nThis spell amplifies binding kinetic flux in a directed line, targeting an inscribed anchor with immediate discharge. It's likely used for combat or anchoring spells.\n\nOperational constraint: The target must be within the caster's reach and clearly defined by writing on themselves."
}
```

## Ollama Interpretation

**Spell Note: Beam Anchor Amp**

This spell amplifies binding kinetic flux in a directed line, targeting an inscribed anchor with immediate discharge. It's likely used for combat or anchoring spells.

Operational constraint: The target must be within the caster's reach and clearly defined by writing on themselves.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
