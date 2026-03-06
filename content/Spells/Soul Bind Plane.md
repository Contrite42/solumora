# Soul Bind Plane

Anchors soul flux as a planar spread at self reach, targeting a filtered selection with short timed hold with active regulation while it runs.

## Effect

Anchors soul flux as a planar spread at self reach, targeting a filtered selection with short timed hold with active regulation while it runs. A circle bind/control recipe that channels soul discipline into soul output. It applies a plane pattern against filter across self reach with timed short persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Bind | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Circle | Base 55 W, outer slots 6 |
| Discipline | Soul | x75 multiplier |
| Output Mode | Soul | +0 W premium |
| Pattern | Plane | +0 W |
| Reach | Self | +0 W |
| Persistence | Timed Short | +5 W |
| Target Spec | Filter | +60 W |

## Cost Breakdown

- Shape control surface: Circle explicit outer variables = discipline, output_mode, pattern, target_spec, reach, persistence
- Shape implied defaults: (none)
- Core discipline cost: 55 * 75 = 4125 W
- Pattern + Reach + Persistence + Target + Output premium:
  0 + 0 + 5 + 60 + 0 = 65 W
- Subtotal: 4190 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **9050 W**
- Required Control Tier: **T6**
- Rarity bucket: **Rare**

## All Grimoire Row

| **Soul Bind Plane** | Circle | Bind | Control | T6 | Soul | Soul | Plane | Self | Timed Short | Filter |

## AI Spell Data

```json
{
  "name": "Soul Bind Plane",
  "summary": "Anchors soul flux as a planar spread at self reach, targeting a filtered selection with short timed hold with active regulation while it runs.",
  "effect_description": "Anchors soul flux as a planar spread at self reach, targeting a filtered selection with short timed hold with active regulation while it runs. A circle bind/control recipe that channels soul discipline into soul output. It applies a plane pattern against filter across self reach with timed short persistence.",
  "hook": "Bind",
  "mode": "Control",
  "shape": "Circle",
  "discipline": "Soul",
  "output_mode": "Soul",
  "pattern": "Plane",
  "reach": "Self",
  "persistence": "Timed Short",
  "target_spec": "Filter",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 55,
    "discipline_multiplier": 75,
    "core_discipline_w": 4125,
    "pattern_w": 0,
    "reach_w": 0,
    "persistence_w": 5,
    "target_w": 60,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 4190,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 9050,
    "required_tier": "T6",
    "rarity": "Rare"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language."
}
```


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
