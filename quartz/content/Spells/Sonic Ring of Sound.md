# Sonic Ring of Sound

The spell creates a sustained sonic ring of sound that affects the marked area over long reach, but only for an immediate duration.

## Effect

The spell creates a sustained sonic ring of sound that affects the marked area over long reach, but only for an immediate duration. A pentagon shape/affect recipe that channels sound discipline into sonic output. It applies a ring pattern against marked across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Shape | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Sonic | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 4 = 80 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 40 + 0 + 15 + 0 = 70 W
- Subtotal: 150 W
- Hook/Mode complexity multiplier: x1.2
- Hook/Mode flat addition: +0 W
- Total: **180 W**
- Required Control Tier: **T3**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Sonic Ring of Sound** | Pentagon | Shape | Affect | T3 | Sound | Sonic | Ring | Long | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Sonic Ring of Sound",
  "summary": "The spell creates a sustained sonic ring of sound that affects the marked area over long reach, but only for an immediate duration.",
  "effect_description": "The spell creates a sustained sonic ring of sound that affects the marked area over long reach, but only for an immediate duration. A pentagon shape/affect recipe that channels sound discipline into sonic output. It applies a ring pattern against marked across long reach with immediate persistence.",
  "hook": "Shape",
  "mode": "Affect",
  "shape": "Pentagon",
  "discipline": "Sound",
  "output_mode": "Sonic",
  "pattern": "Ring",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 4,
    "core_discipline_w": 80,
    "pattern_w": 15,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 150,
    "hook_mode_multiplier": 1.2,
    "hook_mode_flat_w": 0,
    "total_w": 180,
    "required_tier": "T3",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "Here is the interpretation of the Solumora sigil as a practical spell note:\n\n**Spell:** Sonic Ring of Sound\n**Effect:** Creates a sustained sonic ring that affects a marked area over long reach for an immediate duration.\n**Likely Use:** Disorienting or distracting enemies in combat.\n**Operational Constraint:** The effect only lasts for an immediate duration, making it a temporary solution rather than a prolonged strategy."
}
```

## Ollama Interpretation

Here is the interpretation of the Solumora sigil as a practical spell note:

**Spell:** Sonic Ring of Sound
**Effect:** Creates a sustained sonic ring that affects a marked area over long reach for an immediate duration.
**Likely Use:** Disorienting or distracting enemies in combat.
**Operational Constraint:** The effect only lasts for an immediate duration, making it a temporary solution rather than a prolonged strategy.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
