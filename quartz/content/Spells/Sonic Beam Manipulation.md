# Sonic Beam Manipulation

This spell creates a sonic beam that emanates from the caster and persists for an immediate duration, potentially manipulating sound waves around them.

## Effect

This spell creates a sonic beam that emanates from the caster and persists for an immediate duration, potentially manipulating sound waves around them. A square filter/control recipe that channels sound discipline into sonic output. It applies a beam pattern against self across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Sonic | +0 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Self | +0 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 4 = 32 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 0 + 0 = 5 W
- Subtotal: 37 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **80 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Sonic Beam Manipulation** | Square | Filter | Control | T2 | Sound | Sonic | Beam | Self | Immediate | Self |

## AI Spell Data

```json
{
  "name": "Sonic Beam Manipulation",
  "summary": "This spell creates a sonic beam that emanates from the caster and persists for an immediate duration, potentially manipulating sound waves around them.",
  "effect_description": "This spell creates a sonic beam that emanates from the caster and persists for an immediate duration, potentially manipulating sound waves around them. A square filter/control recipe that channels sound discipline into sonic output. It applies a beam pattern against self across self reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Control",
  "shape": "Square",
  "discipline": "Sound",
  "output_mode": "Sonic",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Self",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 4,
    "core_discipline_w": 32,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 0,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 37,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 80,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Spell:** Sonic Beam Manipulation\n\n**Description:** Creates a sonic beam that emanates from the caster and persists for an immediate duration, potentially manipulating sound waves around them.\n\n**Likely Use:** Disrupting or escaping enemy attacks in close combat situations.\n\n**Operational Constraint:** Requires a clear line of sight to effectively direct the sonic beam."
}
```

## Ollama Interpretation

**Spell:** Sonic Beam Manipulation

**Description:** Creates a sonic beam that emanates from the caster and persists for an immediate duration, potentially manipulating sound waves around them.

**Likely Use:** Disrupting or escaping enemy attacks in close combat situations.

**Operational Constraint:** Requires a clear line of sight to effectively direct the sonic beam.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
