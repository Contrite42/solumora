# Sound Wave Impact

The spell causes a resonant triangle-shaped sound wave to affect the caster's soul where they are written or marked, having an immediate effect with no sustained duration.

## Effect

The spell causes a resonant triangle-shaped sound wave to affect the caster's soul where they are written or marked, having an immediate effect with no sustained duration. A triangle move/affect recipe that channels sound discipline into soul output. It applies a ring pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Move | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Soul | +60 W premium |
| Pattern | Ring | +15 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 4 = 12 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 0 + 0 + 0 + 60 = 75 W
- Subtotal: 87 W
- Hook/Mode complexity multiplier: x1.5
- Hook/Mode flat addition: +0 W
- Total: **130 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Sound Wave Impact** | Triangle | Move | Affect | T2 | Sound | Soul | Ring | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Sound Wave Impact",
  "summary": "The spell causes a resonant triangle-shaped sound wave to affect the caster's soul where they are written or marked, having an immediate effect with no sustained duration.",
  "effect_description": "The spell causes a resonant triangle-shaped sound wave to affect the caster's soul where they are written or marked, having an immediate effect with no sustained duration. A triangle move/affect recipe that channels sound discipline into soul output. It applies a ring pattern against where written across self reach with immediate persistence.",
  "hook": "Move",
  "mode": "Affect",
  "shape": "Triangle",
  "discipline": "Sound",
  "output_mode": "Soul",
  "pattern": "Ring",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Where Written",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 3,
    "discipline_multiplier": 4,
    "core_discipline_w": 12,
    "pattern_w": 15,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 60,
    "subtotal_outer_w": 87,
    "hook_mode_multiplier": 1.5,
    "hook_mode_flat_w": 0,
    "total_w": 130,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Spell Name:** Sound Wave Impact\n\n**Effect:** Causes a resonant triangle-shaped sound wave to affect the caster's soul at marked locations, producing an immediate effect with no lasting impact.\n\n**Likely Use:** Marking areas of the body for temporary protection or enhancement during combat.\n\n**Operational Constraint:** The spell requires specific marks on the caster's body to be effective."
}
```

## Ollama Interpretation

**Spell Name:** Sound Wave Impact

**Effect:** Causes a resonant triangle-shaped sound wave to affect the caster's soul at marked locations, producing an immediate effect with no lasting impact.

**Likely Use:** Marking areas of the body for temporary protection or enhancement during combat.

**Operational Constraint:** The spell requires specific marks on the caster's body to be effective.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
