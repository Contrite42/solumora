# Resonant Sonic Barrier

This spell creates a ring-shaped sonic barrier that resonates at a specific sound frequency, affecting the area where it is written, with immediate effects.

## Effect

This spell creates a ring-shaped sonic barrier that resonates at a specific sound frequency, affecting the area where it is written, with immediate effects. A triangle filter/control recipe that channels sound discipline into sonic output. It applies a ring pattern against where written across self reach with immediate persistence.

## Sigil Variables

| Variable | Assigned Value | Cost Rule |
|---|---|---|
| Hook | Filter | Center core variable (complexity handled via multiplier/flat) |
| Mode | Control | Center core variable (complexity handled via multiplier/flat) |
| Shape | Triangle | Base 3 W, outer slots 3 |
| Discipline | Sound | x4 multiplier |
| Output Mode | Sonic | +0 W premium |
| Pattern | Ring | +15 W |
| Reach | Self | +0 W |
| Persistence | Immediate | +0 W |
| Target Spec | Where Written | +0 W |

## Cost Breakdown

- Shape control surface: Triangle explicit outer variables = discipline, output_mode, pattern
- Shape implied defaults: target_spec=Where Written, reach=Self, persistence=Immediate
- Core discipline cost: 3 * 4 = 12 W
- Pattern + Reach + Persistence + Target + Output premium:
  15 + 0 + 0 + 0 + 0 = 15 W
- Subtotal: 27 W
- Hook/Mode complexity multiplier: x2.16
- Hook/Mode flat addition: +0 W
- Total: **58 W**
- Required Control Tier: **T2**
- Rarity bucket: **Common**

## All Grimoire Row

| **Resonant Sonic Barrier** | Triangle | Filter | Control | T2 | Sound | Sonic | Ring | Self | Immediate | Where Written |

## AI Spell Data

```json
{
  "name": "Resonant Sonic Barrier",
  "summary": "This spell creates a ring-shaped sonic barrier that resonates at a specific sound frequency, affecting the area where it is written, with immediate effects.",
  "effect_description": "This spell creates a ring-shaped sonic barrier that resonates at a specific sound frequency, affecting the area where it is written, with immediate effects. A triangle filter/control recipe that channels sound discipline into sonic output. It applies a ring pattern against where written across self reach with immediate persistence.",
  "hook": "Filter",
  "mode": "Control",
  "shape": "Triangle",
  "discipline": "Sound",
  "output_mode": "Sonic",
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
    "output_mode_premium_w": 0,
    "subtotal_outer_w": 27,
    "hook_mode_multiplier": 2.16,
    "hook_mode_flat_w": 0,
    "total_w": 58,
    "required_tier": "T2",
    "rarity": "Common"
  },
  "ai_interpretation_hint": "Use name + summary + effect_description to explain what the spell does in plain language.",
  "ollama_interpretation": "**Spell Note: Resonant Sonic Barrier**\n\nThis spell creates a ring-shaped sonic barrier that resonates at a specific sound frequency, affecting the area where it is written.\n\n**Likely Use:** Sound-based protection or offense in combat situations, such as creating a shockwave around oneself to repel enemies.\n\n**Operational Constraint:** Requires concentration and intentional focus on the target area to effectively resonate the sonic barrier."
}
```

## Ollama Interpretation

**Spell Note: Resonant Sonic Barrier**

This spell creates a ring-shaped sonic barrier that resonates at a specific sound frequency, affecting the area where it is written.

**Likely Use:** Sound-based protection or offense in combat situations, such as creating a shockwave around oneself to repel enemies.

**Operational Constraint:** Requires concentration and intentional focus on the target area to effectively resonate the sonic barrier.


## See Also

[[All Grimoire]], [[Sigils]], [[Spell Variables]], [[Flux Cost Reference]], [[Control Tier]]
