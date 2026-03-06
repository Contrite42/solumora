# Amplified Electric Shock Wave

The spell amplifies and releases a concentrated electric shock over a long range in the shape of a sphere, targeting a group of individuals immediately.

## Effect

The spell amplifies and releases a concentrated electric shock over a long range in the shape of a sphere, targeting a group of individuals immediately. A pentagon amplify/create recipe that channels electric discipline into shock output. It applies a sphere pattern against group across long reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Amplify | Center core variable (complexity handled via multiplier/flat) |
| Mode | Create | Center core variable (complexity handled via multiplier/flat) |
| Shape | Pentagon | Base 20 W, outer slots 5 |
| Discipline | Electric | x5 multiplier |
| Output Mode | Shock | +0 W premium |
| Pattern | Sphere | +30 W |
| Reach | Long | +40 W |
| Persistence | Immediate | +0 W |
| Target Spec | Group | +35 W |

## Cost Breakdown

- Shape control surface: Pentagon explicit outer variables = discipline, output_mode, pattern, target_spec, reach
- Shape implied defaults: persistence=Immediate
- Core discipline cost: 20 * 5 = 100 W
- Pattern + Reach + Persistence + Target + Output premium:
  30 + 40 + 0 + 35 + 0 = 105 W
- Subtotal: 205 W
- Hook/Mode complexity multiplier: x2.53
- Hook/Mode flat addition: +0 W
- Total: **519 W**
- Required Control Tier: **T4**
- Rarity bucket: **Uncommon**

## All Grimoire Row

| **Amplified Electric Shock Wave** | Pentagon | Amplify | Create | T4 | Electric | Shock | Sphere | Long | Immediate | Group |

## AI Spell Data

```json
{
  "name": "Amplified Electric Shock Wave",
  "summary": "The spell amplifies and releases a concentrated electric shock over a long range in the shape of a sphere, targeting a group of individuals immediately.",
  "effect_description": "The spell amplifies and releases a concentrated electric shock over a long range in the shape of a sphere, targeting a group of individuals immediately. A pentagon amplify/create recipe that channels electric discipline into shock output. It applies a sphere pattern against group across long reach with immediate persistence.",
  "hook": "Amplify",
  "mode": "Create",
  "shape": "Pentagon",
  "discipline": "Electric",
  "output_mode": "Shock",
  "pattern": "Sphere",
  "reach": "Long",
  "persistence": "Immediate",
  "target_spec": "Group",
  "sustained_minutes": 0,
  "cost": {
    "shape_base_w": 20,
    "discipline_multiplier": 5,
    "core_discipline_w": 100,
    "pattern_w": 30,
    "reach_w": 40,
    "persistence_w": 0,
    "target_w": 35,
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 205,
    "hook_mode_multiplier": 2.53,
    "hook_mode_flat_w": 0,
    "total_w": 519,
    "required_tier": "T4",
    "rarity": "Uncommon"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Spell Name:** Amplified Electric Shock Wave\n\n**Effect:** Releases a concentrated electric shock over a long range in the shape of a sphere, targeting a group of individuals.\n\n**Likely Use:** Crowd control, area denial, or anti-formation tactics against groups of enemies.\n\n**Operational Constraint:** Requires a T4 tier and sufficient magical resources to cast."
}
```

## Ollama Interpretation

**Spell Name:** Amplified Electric Shock Wave

**Effect:** Releases a concentrated electric shock over a long range in the shape of a sphere, targeting a group of individuals.

**Likely Use:** Crowd control, area denial, or anti-formation tactics against groups of enemies.

**Operational Constraint:** Requires a T4 tier and sufficient magical resources to cast.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
