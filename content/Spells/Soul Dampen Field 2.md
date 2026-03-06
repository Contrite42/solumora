# Soul Dampen Field 2

Reduces soul flux as a field volume at linked reach, targeting a marked signature with immediate discharge with active regulation while it runs.

## Effect

Reduces soul flux as a field volume at linked reach, targeting a marked signature with immediate discharge with active regulation while it runs. A pentagon dampen/control recipe that channels soul discipline into soul output. It applies a field pattern against marked across linked reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Dampen | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Field | +60 W |
| Reach | Linked | +150 W |
| Persistence | Immediate | +0 W |
| Target Spec | Marked | +15 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 75 = 1500 W
- Pattern + Reach + Persistence + Target + Output premium:
  60 + 150 + 0 + 15 + 0 = 225 W
- Subtotal: 1725 W
- Hook/Mode complexity multiplier: x2.565
- Hook/Mode flat addition: +0 W
- Total: **4425 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Dampen Field 2** | Pentagon | Dampen | Control | T6 | Soul | Soul | Field | Linked | Immediate | Marked |

## AI Spell Data

```json
{
  "name": "Soul Dampen Field 2",
  "summary": "Reduces soul flux as a field volume at linked reach, targeting a marked signature with immediate discharge with active regulation while it runs.",
  "effect_description": "Reduces soul flux as a field volume at linked reach, targeting a marked signature with immediate discharge with active regulation while it runs. A pentagon dampen/control recipe that channels soul discipline into soul output. It applies a field pattern against marked across linked reach with immediate persistence.",
  "hook": "Dampen",
  "mode": "Control",
  "shape": "Pentagon",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Field",
  "reach": "Linked",
  "persistence": "Immediate",
  "target_spec": "Marked",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 75,
    "core_discipline_w": 1500,
    "pattern_w": 60,
    "reach_w": 150,
    "persistence_w": 0,
    "target_w": 15,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 1725,
    "hook_mode_multiplier": 2.565,
    "hook_mode_flat_w": 0,
    "total_w": 4425,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
