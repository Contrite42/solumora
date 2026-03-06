# Heat Wave Burst

The spell creates a localized burst of intense heat that affects all nearby targets, radiating outward in a square pattern before dissipating immediately.

## Effect

The spell creates a localized burst of intense heat that affects all nearby targets, radiating outward in a square pattern before dissipating immediately. A square dampen/affect recipe that channels heat discipline into kinetic output. It applies a beam pattern against group across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Square | Base 8 W, outer slots 4 |
| Discipline | Heat | x2 multiplier |
| Output Mode | Kinetic | +10 W premium |
| Pattern | Beam | +5 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Square explicit outer variables = discipline, output_mode, pattern, target_spec
- Shape implied defaults: reach=Self, persistence=Immediate
- Core discipline cost: 8 * 2 = 16 W
- Pattern + Reach + Persistence + Target + Output premium:
  5 + 0 + 0 + 35 + 10 = 50 W
- Subtotal: 66 W
- Hook/Mode complexity multiplier: x1.9
- Hook/Mode flat addition: +0 W
- Total: **125 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Heat Wave Burst** | Square | Dampen | Affect | T2 | Heat | Kinetic | Beam | Self | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Heat Wave Burst",
  "summary": "The spell creates a localized burst of intense heat that affects all nearby targets, radiating outward in a square pattern before dissipating immediately.",
  "effect_description": "The spell creates a localized burst of intense heat that affects all nearby targets, radiating outward in a square pattern before dissipating immediately. A square dampen/affect recipe that channels heat discipline into kinetic output. It applies a beam pattern against group across self reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Affect",
  "shape": "Square",
  "discipline": "Heat",
  "output_mode": "Kinetic",
  "pattern": "Beam",
  "reach": "Self",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 8,
    "discipline_multiplier": 2,
    "core_discipline_w": 16,
    "pattern_w": 5,
    "reach_w": 0,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 10,
    "subtotal_outer_w": 66,
    "hook_mode_multiplier": 1.9,
    "hook_mode_flat_w": 0,
    "total_w": 125,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Spell Name:** Heat Wave Burst\n\n**Description:** Creates a localized burst of intense heat that affects all nearby targets in a square pattern.\n\n**Likely Use:** Clearing groups or clusters of enemies, or as an area denial tool against crowds.\n\n**Operational Constraint:** Can only be used within the caster's self-reach, limiting its effectiveness at long ranges."
}
```

## Ollama Interpretation

**Spell Name:** Heat Wave Burst

**Description:** Creates a localized burst of intense heat that affects all nearby targets in a square pattern.

**Likely Use:** Clearing groups or clusters of enemies, or as an area denial tool against crowds.

**Operational Constraint:** Can only be used within the caster's self-reach, limiting its effectiveness at long ranges.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
