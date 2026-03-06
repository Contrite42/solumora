# MindMark

A reality-altering effect that establishes soul energy in a field volume by changing existing conditions

## Effect

Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that establishes soul energy in a field volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Ward | Center core variable (complexity handled via multiplier/flat) |
| Mode | Affect | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Raw | +30 W premium |
| Pattern | Field | +60 W |
| Reach | Line-of-Sight | +80 W |
| Persistence | Permanent | +400 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 80 + 400 + 35 + 30 = 605 W
- Subtotal: 4730 W
- Hook/Mode complexity multiplier: x2.0
- Hook/Mode flat addition: +0 W
- Total: **9460 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **MindMark** | Circle | Ward | Affect | T6 | Soul | Raw | Field | Line-of-Sight | Permanent | Group |

## AI Spell Data

```json
{
  "name": "MindMark",
  "summary": "A reality-altering effect that establishes soul energy in a field volume by changing existing conditions",
  "effect_description": "Invokes a fundamental disruption to local Flux architecture. The caster inscribes a sigil that establishes soul energy in a field volume by changing existing conditions. Effect range: line-of-sight. Persistence: permanent. Side effects on caster and casting site are documented but not fully understood.",
  "hook": "Ward",
  "mode": "Affect",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Raw",
  "pattern": "Field",
  "reach": "Line-of-Sight",
  "persistence": "Permanent",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 60,
    "reach_w": 80,
    "persistence_w": 400,
    "target_w": 35,
    "output_mode_premium_w": 30,
    "subtotal_outer_w": 4730,
    "hook_mode_multiplier": 2.0,
    "hook_mode_flat_w": 0,
    "total_w": 9460,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
