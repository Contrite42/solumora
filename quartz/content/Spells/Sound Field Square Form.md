# Sound Field Square Form

This spell creates a field of sound that takes the shape of a square and affects only a marked target with immediate effects.

## Effect

This spell creates a field of sound that takes the shape of a square and affects only a marked target with immediate effects. A square shape/create recipe that channels sound discipline into kinetic output. It applies a field pattern against marked across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Kinetic | +10 W premium |
| Pattern | Field | +60 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 4 = 32 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 0 + 0 + 15 + 10 = 85 W
- Subtotal: 117 W
- Hook/Mode complexity multiplier: x1.38
- Hook/Mode flat addition: +0 W
- Total: **161 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Sound Field Square Form** | Square | Shape | Create | T3 | Sound | Kinetic | Field | Self | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Sound Field Square Form",
  "summary": "This spell creates a field of sound that takes the shape of a square and affects only a marked target with immediate effects.",
  "effect_description": "This spell creates a field of sound that takes the shape of a square and affects only a marked target with immediate effects. A square shape/create recipe that channels sound discipline into kinetic output. It applies a field pattern against marked across self reach with immediate persistence.",
  "hook": "Shape",
  "mode": "Create",
  "shape": "Square",
  "discipline": "Sound",
  "output_mode": "Kinetic",
  "pattern": "Field",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 4,
    "core_discipline_w": 32,
    "pattern_w": 60,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 117,
    "hook_mode_multiplier": 1.38,
    "hook_mode_flat_w": 0,
    "total_w": 161,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "Here's a practical interpretation of the Solumora sigil as a spell note:\n\n**Spell:** Sound Field Square Form\n**Effect:** Creates a square-shaped field of sound that affects a marked target with immediate effects, channeling sound discipline into kinetic output.\n**Likely Use:** Defense or combat situations where precise targeting is needed.\n**Operational Constraint:** Requires marking the target before casting."
}
```

## Ollama Interpretation

Here's a practical interpretation of the Solumora sigil as a spell note:

**Spell:** Sound Field Square Form
**Effect:** Creates a square-shaped field of sound that affects a marked target with immediate effects, channeling sound discipline into kinetic output.
**Likely Use:** Defense or combat situations where precise targeting is needed.
**Operational Constraint:** Requires marking the target before casting.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
