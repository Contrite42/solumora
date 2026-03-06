# Soul Ward Triangle

The spell creates a triangular ward that affects the caster's soul and can be immediately activated at the point where it is written.

## Effect

The spell creates a triangular ward that affects the caster's soul and can be immediately activated at the point where it is written. A triangle ward/affect recipe that channels soul discipline into constraint output. It applies a point pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Ward | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Constraint | +60 W premium |
| Pattern | Point | +0 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 75 = 225 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 0 + 0 + 60 = 60 W
- Subtotal: 285 W
- Hook/Mode complexity multiplier: x2.0
- Hook/Mode flat addition: +0 W
- Total: **570 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Soul Ward Triangle** | Triangle | Ward | Affect | T4 | Soul | Constraint | Point | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Soul Ward Triangle",
  "summary": "The spell creates a triangular ward that affects the caster's soul and can be immediately activated at the point where it is written.",
  "effect_description": "The spell creates a triangular ward that affects the caster's soul and can be immediately activated at the point where it is written. A triangle ward/affect recipe that channels soul discipline into constraint output. It applies a point pattern against where written across self reach with immediate persistence.",
  "hook": "Ward",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Soul",
  "output_mode": "Constraint",
  "pattern": "Point",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 75,
    "core_discipline_w": 225,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 285,
    "hook_mode_multiplier": 2.0,
    "hook_mode_flat_w": 0,
    "total_w": 570,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Soul Ward Triangle Spell Note**\n\nThis spell creates a triangular ward on the caster's soul, channeling soul discipline into constraint output. It can be activated immediately at the point where it is written and affects the caster within their self-reach.\n\n**Likely Use:** Defensive magic to protect against harm or negative energies.\n\n**Operational Constraint:** Requires immediate activation at the point of writing, limiting its use as a pre-emptive measure."
}
```

## Ollama Interpretation

**Soul Ward Triangle Spell Note**

This spell creates a triangular ward on the caster's soul, channeling soul discipline into constraint output. It can be activated immediately at the point where it is written and affects the caster within their self-reach.

**Likely Use:** Defensive magic to protect against harm or negative energies.

**Operational Constraint:** Requires immediate activation at the point of writing, limiting its use as a pre-emptive measure.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
