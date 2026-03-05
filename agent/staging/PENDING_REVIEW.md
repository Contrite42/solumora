# Pending Batch 1 of 2
Notes in this batch: ['content/Flux Expenditure.md', 'content/Spell Variables.md']

## WRITE: content/Flux Expenditure.md

```
[[Flux]] expenditure is the cost of channeling — the physical and mental toll that moving [[Flux]] through a person demands. Every [[Sigils|sigil]]-based spell requires the caster to hold multiple variables simultaneously in precise geometric relationship while channeling the energy to activate them. The cost scales with the complexity of what is being attempted and determines the [[Control Tier]] requirement for execution.

The expenditure is measured in [[Watts]], the same unit used for the currency system, though the two applications are entirely separate. Casting a 100W spell does not debit your bank account. The Watt measurement describes the precision demand the spell places on the caster's ability to channel [[Flux]] accurately.

## Immediate vs Sustained Cost

Most spells require their full cost to be channeled at the moment of casting. A 500W spell demands that the caster hold 500W worth of precision for the duration of the casting process — typically seconds to minutes depending on complexity. Once the spell activates, the cost is paid and the effect continues according to its [[Persistence]] setting.

Sustained spells work differently. The caster pays the base cost at activation, then continues to channel a maintenance cost for as long as the effect remains active. A spell with Sustained persistence typically adds 10W per 10-minute interval to its base cost, paid continuously while the effect operates. This maintenance cost is lower than the activation cost but accumulates over time, making sustained effects expensive for long-duration use.

The daily capacity limits documented in the [[Flux Cost Reference]] represent comfortable working ranges — the amount a practitioner can channel without significant fatigue. Pushing past these limits is possible but carries increasing physical and mental toll. Exceeding them substantially risks channel damage that can reduce a practitioner's effective tier permanently.

## Additive Effect

The total cost of a [[Sigils|sigil]]-based spell is calculated as: [[Shape]] base W × [[Discipline]] multiplier, plus flat additions from all specified outer variables, multiplied by the Hook/Mode complexity factor.

The core cost comes from the intersection of Shape and Discipline. Shape provides the base Watt value — Triangle (3W), Square (8W), Pentagon (20W), Circle (55W). Discipline provides the multiplier — Raw (×1), Force (×2), Heat (×2), Light (×3), Sound (×4), Electric (×5), Chemical (×5), Binding (×10), Mind (×25), Soul (×75). A Circle Soul sigil starts at 55 × 75 = 4,125W before any other variables are added.

The outer variables — [[Pattern]], [[Reach]], [[Persistence]], [[Target Spec]], [[Output Mode]] — add flat costs to this core. A Circle Soul sigil with Touch (+2W), Permanent (+400W), and Individual (+8W) totals 4,535W, placing it at the T6 level.

Without Hook/Mode elevation, the outer variables alone cannot produce costs above approximately 5,000W regardless of configuration. This represents the
```
## WRITE: content/Spell Variables.md

```
[[Sigils]] encode spells as geometric arrangements of variables. Each variable occupies a specific position in the shape and defines one aspect of what the spell does — its discipline, reach, duration, targeting, and output characteristics. The [[Flux Cost Reference]] provides the complete cost tables; this page explains what each variable controls and how they interact.

## Shape (Outer Variable #1)

Shape determines the spell's base [[Flux]] cost and constrains how many other variables can be specified. Each outer point of the shape represents one variable slot. [[Discipline]] always occupies one slot, leaving the remainder available for other outer variables.

| Shape | Outer Slots | Discipline | Remaining Variable Slots |
|-------|-------------|------------|--------------------------|
| Triangle | 3 | 1 | 2 |
| Square | 4 | 1 | 3 |
| Pentagon | 5 | 1 | 4 |
| Circle | 6 | 1 | 5 (all) |

A Triangle sigil cannot specify more than 2 outer variables beyond Discipline — this is a geometric constraint, not a tier limit.

- **Triangle**: Simplest construction, lowest base cost (3W), limited to two additional variables
- **Square**: Moderate complexity, higher base cost (8W), allows three additional variables  
- **Pentagon**: Complex construction, significant base cost (20W), allows four additional variables
- **Circle**: Most complex geometry, highest base cost (55W), allows all five additional variables simultaneously

Higher shapes enable more sophisticated effects by permitting multiple variables to be specified together. A Triangle sigil with Heat discipline can add Touch and Timed Long, but cannot also specify Individual targeting — the geometry lacks a fourth outer point. A Circle sigil can specify Heat + Touch + Timed Long + Individual + Field pattern all in the same casting.

## Discipline (Outer Variable #2)

Discipline determines what type of [[Flux]] the spell channels and multiplies the Shape base cost. Each discipline represents a different level of discrimination the [[Flux]] system must maintain.

- **Raw** (×1): Unfiltered [[Flux]], no specific discrimination required
- **Force** (×2): Kinetic energy, mechanical effects, physical manipulation
- **Heat** (×2): Thermal energy, temperature control, thermal detection
- **Light** (×3): Photonic energy, illumination, optical effects, visual concealment
- **Sound** (×4): Acoustic energy, vibration, auditory effects
- **Electric** (×5): Electrical energy, shock effects, electrical system interaction
- **Chemical** (×5): Molecular manipulation, chemical reactions, material transformation
- **Binding** (×10): Constraint effects, sealing, structural reinforcement, immobilization
- **Mind** (×25): Neural interaction, thought reading, emotional influence, memory work
- **Soul** (×75): Soul-signature interaction, identity effects, spiritual manipulation

The multiplier gap reflects the precision demand each discipline places on the [[Flux]] field. Raw requires no discriminating precision. Soul req
```

---
To approve: write `APPROVED` to agent/staging/REVIEW_RESPONSE.md
To reject:  write `REJECTED` (optionally followed by notes) to agent/staging/REVIEW_RESPONSE.md
