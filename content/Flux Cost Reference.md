A reference table for calculating the [[Flux]] cost (in [[Watts]]) of any [[Sigils|sigil]]-based spell. Total cost determines the [[Control Tier]] requirement for the caster.

**Formula:** `Total W = (Shape base × Discipline multiplier) + Pattern + Reach + Persistence + Target`

All defaulted variables contribute 0W. Every variable specified beyond the default adds to the total.

---

## Shape Base Cost and Variable Slots

Shape determines two things simultaneously: the base Flux cost (multiplied by Discipline), and how many outer variables the caster can specify. Each outer point is one variable slot. One slot is always occupied by Discipline — the remaining slots are available for other outer variables (Pattern, Reach, Persistence, Target Spec, Output Mode). Unoccupied slots default.

| Shape | Outer Slots | Discipline | Remaining Variable Slots | Base W |
|-------|-------------|------------|--------------------------|--------|
| Triangle | 3 | 1 | 2 | 3 W |
| Square | 4 | 1 | 3 | 8 W |
| Pentagon | 5 | 1 | 4 | 20 W |
| Circle | 6 | 1 | 5 (all) | 55 W |

A Triangle sigil can only specify two outer variables beyond Discipline — the rest default. A Circle sigil can specify all five remaining outer variables simultaneously. This is why complex multi-variable effects require higher shapes: Triangle geometry cannot hold more than two specified outer variables regardless of the caster's tier.

---

## Discipline Multiplier

Applied to the shape base. A Triangle Force sigil starts at 3 × 2 = **6 W**. A Circle Soul sigil starts at 55 × 75 = **4,125 W**.

| Discipline | Multiplier | Shape × Mult (Triangle / Square / Pentagon / Circle) |
|-----------|-----------|------------------------------------------------------|
| Raw | ×1 | 3 / 8 / 20 / 55 W |
| Force | ×2 | 6 / 16 / 40 / 110 W |
| Heat | ×2 | 6 / 16 / 40 / 110 W |
| Light | ×3 | 9 / 24 / 60 / 165 W |
| Sound | ×4 | 12 / 32 / 80 / 220 W |
| Electric | ×5 | 15 / 40 / 100 / 275 W |
| Chemical | ×5 | 15 / 40 / 100 / 275 W |
| Binding | ×10 | 30 / 80 / 200 / 550 W |
| Mind | ×25 | 75 / 200 / 500 / 1,375 W |
| Soul | ×75 | 225 / 600 / 1,500 / 4,125 W |

---

## Geometry Pattern (flat addition)

| Pattern | W |
|---------|---|
| Point | 0 |
| Plane *(default)* | 0 |
| Beam | +5 |
| Cone | +10 |
| Ring | +15 |
| Cylinder | +20 |
| Sphere | +30 |
| Field | +60 |

---

## Reach (flat addition)

| Reach | W |
|-------|---|
| Self *(default)* | 0 |
| Touch | +2 |
| Short (10 ft) | +5 |
| Medium (50 ft) | +15 |
| Long (200 ft) | +40 |
| Line-of-Sight | +80 |
| Linked | +150 |

---

## Persistence (flat addition)

Sustained spells accrue cost continuously while active. All other values are paid once at casting.

| Persistence | W |
|-------------|---|
| Immediate *(default)* | 0 |
| Timed Short (≤ 1 min) | +5 |
| Timed Long (≤ 1 hr) | +25 |
| Sustained | +10 per 10 min active |
| Conditional | +20 |
| Latched | +40 |
| Permanent | +400 |

---

## Target Spec (flat addition)

| Target | W |
|--------|---|
| Where Written *(default)* | 0 |
| Self | 0 |
| Object | +2 |
| Surface | +5 |
| Individual | +8 |
| Marked | +15 |
| Group | +35 |
| Filter | +60 |

---

## Output Mode Premium

Natural pairings (Thermal←Heat, Kinetic←Force, Photonic←Light, Sonic←Sound, Shock←Electric, Reactive←Chemical, Constraint←Binding, Neuro←Mind, Soul←Soul) carry no additional cost. Crossing disciplines adds:

| Mismatch | Additional W |
|----------|-------------|
| Adjacent discipline (e.g. Kinetic from Heat) | +10 |
| Cross-type (e.g. Neuro from Force) | +30 |
| Extreme cross (e.g. Soul output from a physical discipline) | +60 |

---

## Total Cost → Control Tier Requirement

| Tier | Total W Range |
|------|--------------|
| T0 | 1 – 10 W |
| T1 | 11 – 40 W |
| T2 | 41 – 130 W |
| T3 | 131 – 400 W |
| T4 | 401 – 1,300 W |
| T5 | 1,301 – 4,000 W |
| T6 | 4,001 – 13,000 W |
| T7 | 13,001 – 40,000 W |
| T8 | 40,001 – 130,000 W |
| T9 | > 130,000 W |

---

## Daily Flux Capacity

Comfortable working range per day — the amount a practitioner can channel without significant fatigue. Pushing past these values is possible but carries increasing toll.

| Tier | Approx. W/day |
|------|--------------|
| T0 | ~20 W |
| T1 | ~80 W |
| T2 | ~300 W |
| T3 | ~1,000 W |
| T4 | ~3,000 W |
| T5 | ~10,000 W |
| T6 | ~30,000 W |
| T7 | ~100,000 W |
| T8 | ~300,000 W |
| T9 | not established |

A T2 practitioner can cast several T2-level spells in a working day. Single T1-level casts are negligible. Approaching the daily ceiling brings fatigue; exceeding it risks channel damage.

---

## Hook and Mode

The [[Spell Variables|center core variables]] — Hook (the spell's core action) and Mode (its intent) — also carry inherent Flux cost proportional to the complexity of what the spell is trying to do. Simple physical effects (move, heat, seal) add little beyond the discipline baseline. Effects that read or alter internal state (detect, read a thought, suppress), modify identity, or produce permanent structural changes to a person carry additional cost that the outer variable tables do not fully capture. This is why effects described as T7–T9 in practice (permanently erase memory, rewrite identity) cost more than Circle+Mind outer variables alone would calculate.

---

## Embedded Object Note

Sigils inscribed into objects during manufacture distribute their Flux cost across the inscription process rather than requiring the full amount to be channeled at once. A T3 practitioner can embed a Permanent effect that would exceed their single-cast ceiling, given sufficient inscription time. This is why embedded-object work — [[Ossal Meln|temperature containers]], load-bearing structural components, permanent seals — is an independent trade distinct from active casting.

---

## Worked Examples

**Room illumination** — Triangle Light, Plane, Self, Timed Long, Where Written
`9 + 0 + 0 + 25 + 0 = 34 W` → **T1**

**Container seal** — Triangle Binding, Plane, Touch, Latched, Object
`30 + 0 + 2 + 40 + 2 = 74 W` → **T2**

**Force sphere barrier** — Pentagon Force, Sphere, Self, Timed Long, Self
`40 + 30 + 0 + 25 + 0 = 95 W` → **T2**
*(Adding Group target to stop multiple people: +35 W → 130 W → T2/T3 boundary)*

**Heat signature tracking through walls** — Circle Heat, Plane, Medium, Sustained, Individual
`110 + 0 + 15 + (10/10 min) + 8 = 133 W base + ongoing` → **T3**

**Complete immobilization** — Circle Binding, Plane, Touch, Sustained, Individual
`550 + 0 + 2 + (10/10 min) + 8 = 560 W base + ongoing` → **T4**

**Surface thought read** — Pentagon Mind, Plane, Touch, Immediate, Individual
`500 + 0 + 2 + 0 + 8 = 510 W` → **T4**

**Broadcast neuro disruption** — Circle Mind, Field, Line-of-Sight, Timed Short, Group
`1,375 + 60 + 80 + 5 + 35 = 1,555 W` → **T5**

**Permanent Soul mark** — Pentagon Soul, Plane, Touch, Permanent, Individual
`1,500 + 0 + 2 + 400 + 8 = 1,910 W` → **T5**

**Permanent Soul brand (forced)** — Circle Soul, Plane, Touch, Permanent, Individual
`4,125 + 0 + 2 + 400 + 8 = 4,535 W` → **T6**

**Full bodily revival (theoretical)** — Circle Soul, Plane, Touch, Permanent, Individual
`4,125 + 0 + 2 + 400 + 8 = 4,535 W (outer variables only)` → **T6 floor**
Hook/Mode complexity for "restore a dead person to living" adds substantial cost beyond what the outer variable tables capture — the effect requires reading and restoring full soul-signature continuity, rebuilding the Flux relationship between identity and body, and overriding the death-state of every biological system simultaneously. Practitioners who have theorized this spell estimate the true total at **T7–T8 minimum**, scaling with how long the subject has been dead and how much physical damage is present. No working example exists. The calculation above is the floor, not the ceiling.

---

## The Power Gap: What the Numbers Mean

A worked comparison to make the tier gap concrete.

**Container seal** (everyday T2 work): Triangle Binding, Touch, Latched, Object
`30 + 0 + 2 + 40 + 2 = 74 W` → T2

**Theoretical revival** (T7–T8 level): Circle Soul + Permanent + estimated Hook/Mode cost
`4,535 W floor, ~15,000–50,000 W realistic total`

The revival spell costs **200–700× more** than a container seal — and the container seal is already meaningful, skilled work that a T0 practitioner cannot touch. A T2 practitioner's entire daily capacity (~300 W) is not enough to fund a single revival attempt. A T5 practitioner has the daily budget but would need to be T7 or higher to actually hold the precision required.

This is what the tier system describes. The gap between T2 and T7 is not a practitioner who got five levels better at the same thing. It is the difference between someone who can seal a box permanently and someone who can theoretically restore the dead — and the numbers are why.

A T2 Formulist's comfortable working day (300 W) covers about four container seals, or dozens of T1 utility casts, or one or two demanding T2 effects with margin to spare. A T7 practitioner's comfortable day (100,000 W) covers effects that a T2 practitioner could not execute once with their entire life's accumulated casting.

The ledger does not lie about this. Neither does the math.

*See also: [[Spell Variables]], [[Flux Expenditure]], [[Control Tier]], [[Sigils]], [[Discipline]], [[Grimoires]], [[Watts]]*
