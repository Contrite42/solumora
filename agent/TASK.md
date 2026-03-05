# Task: Update Spell Pages to Reflect Calibrated Cost System

## What Changed (Background)

The Flux cost system was fully calibrated with specific Watt values. All pages describing
how spells cost Flux need to reflect the correct formula, the correct shape/slot rules,
and the newly established Hook/Mode multiplier — which is the mechanism that makes
T7–T9 reachable.

---

## THE CORRECT SYSTEM (use these exact values — do not invent alternatives)

### Formula
Total W = ( (Shape base W × Discipline multiplier) + Pattern W + Reach W + Persistence W + Target W + Output Mode W ) × Hook/Mode multiplier

### Shape: Base W cost AND slot constraint (dual role)
Each outer point is one variable slot. Discipline always occupies one slot.

| Shape    | Total Outer Slots | Discipline | Remaining free slots | Base W |
|----------|-------------------|------------|----------------------|--------|
| Triangle | 3                 | 1          | 2                    | 3 W    |
| Square   | 4                 | 1          | 3                    | 8 W    |
| Pentagon | 5                 | 1          | 4                    | 20 W   |
| Circle   | 6                 | 1          | 5 (all)              | 55 W   |

A Triangle sigil cannot hold more than 2 explicitly specified outer variables beyond Discipline,
regardless of the caster's tier. This is geometric, not a capacity limit.

### Discipline multipliers (apply to Shape base W)
Raw x1 | Force x2 | Heat x2 | Light x3 | Sound x4 | Electric x5 | Chemical x5 | Binding x10 | Mind x25 | Soul x75

### Variable flat additions (added after core, before Hook/Mode)
Pattern: Point=0, Plane(default)=0, Beam=+5, Cone=+10, Ring=+15, Cylinder=+20, Sphere=+30, Field=+60
Reach: Self(default)=0, Touch=+2, Short=+5, Medium=+15, Long=+40, Line-of-Sight=+80, Linked=+150
Persistence: Immediate(default)=0, Timed Short=+5, Timed Long=+25, Sustained=0(+10W/10min ongoing), Conditional=+20, Latched=+40, Permanent=+400
Target: Where Written(default)=0, Self=0, Object=+2, Surface=+5, Individual=+8, Marked=+15, Group=+35, Filter=+60
Output Mode: Natural=0, Adjacent discipline=+10, Cross-type=+30, Extreme cross=+60

### Hook/Mode Multiplier — CENTER CORE variable, not an outer slot
Hook/Mode is the complexity of the spell's core ACTION. It is not an outer variable and
does not use a slot. It multiplies the outer variable total.

| Level        | Multiplier | Examples                                                         |
|--------------|------------|------------------------------------------------------------------|
| Basic        | x1         | push, heat, light, seal, detect, surface thought read            |
| Moderate     | x2         | sustained suppression, deep binding, complex physical altering   |
| Significant  | x4         | deep mind read, emotional alteration, precise state detection    |
| Extreme      | x10        | forced identity changes, soul severance, partial memory erasure  |
| Transcendent | x30        | revival from death, rewriting local physical laws                |
| Absolute     | x100       | interacts with the Flux system architecture itself               |

WITHOUT Hook/Mode elevation (all at x1), the formula tops out at approximately 5,000W — the floor
of T6. The outer variables describe sigil STRUCTURE. Hook/Mode describes what you are DOING with
that structure. T7–T9 effects require extreme Hook/Mode on top of high-end sigil geometry.

### Tier W thresholds
T0:1-10 | T1:11-40 | T2:41-130 | T3:131-400 | T4:401-1,300 | T5:1,301-4,000
T6:4,001-13,000 | T7:13,001-40,000 | T8:40,001-130,000 | T9:130,001+

### Verified canon examples (do not change these numbers anywhere)
- Room illumination: Triangle Light + Timed Long = (3x3)+25 = 34W -> T1
- Container seal: Triangle Binding + Touch + Latched + Object = (3x10)+2+40+2 = 74W -> T2
- Force sphere barrier: Pentagon Force + Sphere + Timed Long = (20x2)+30+25 = 95W -> T2
- Heat signature tracking: Circle Heat + Medium + Sustained + Individual = (55x2)+15+0+8 = 133W base -> T3
- Complete immobilization: Circle Binding + Touch + Sustained + Individual = (55x10)+2+0+8 = 560W -> T4
- Surface thought read: Pentagon Mind + Touch + Individual = (20x25)+2+8 = 510W -> T4 (Hook Basic x1)
- Broadcast neuro disruption: Circle Mind + Field + LoS + Timed Short + Group = (55x25)+60+80+5+35 = 1,555W -> T5
- Permanent Soul mark: Pentagon Soul + Touch + Permanent + Individual = (20x75)+2+400+8 = 1,910W -> T5
- Forced Soul brand (outer vars only): Circle Soul + Touch + Permanent + Individual = (55x75)+2+400+8 = 4,535W -> T6
- Forced Soul brand (full identity rewrite): same sigil x Extreme(x10) = 45,350W -> T8
- Full bodily revival: Circle Soul + Touch + Permanent + Individual x Transcendent(x30) = 136,050W -> T9

---

## FILES TO UPDATE

### 1. content/Flux Expenditure.md — WRITE (replace entire file)

The "Additive Effect" section currently has two errors:
(a) It says "Discipline base cost x Shape multiplier" — WRONG. Shape is the BASE and Discipline is
the MULTIPLIER. The correct relationship is: core = Shape base W x Discipline multiplier.
(b) It says Circle Soul sits in "T6 to T8 range" without Hook/Mode. The correct ceiling without
Hook/Mode is approximately T6 (4,535W). T8 requires Hook/Mode x10.

Fix both errors in the Additive Effect section. Keep all other existing prose identical.

Then add a new section called "## Hook and Mode — Core Action Complexity" inserted BEFORE the
final *See also* line. Write it in the existing voice (matter-of-fact, dense, no purple prose).
The section must cover:
- Hook/Mode is the center-core cost multiplier (not an outer slot variable)
- Include the exact multiplier table from above
- Explain that outer variables alone top out at ~5,000W (T6 floor)
- Explain WHY: the outer variables encode sigil structure; Hook/Mode encodes the nature of what
  you are asking the Flux to distinguish and act upon. Soul discipline already requires the Flux
  to find and interact with soul-signature. A Hook that says "permanently rewrite what this person
  IS" requires the Flux to hold a different kind of distinction — one the field resists more.
- T7-T9 require elevated Hook/Mode on top of high-end outer variable structure. The sigil may
  be constructable; the action is what places the effect beyond most practitioners' reach.

### 2. content/Spell Variables.md — WRITE (replace entire file)

Two additions needed:

(a) In the Shape section (outer variable #1): after the existing bullet list of shapes
(Circle provides most control, Triangle is simplest), add the explicit slot table:

  | Shape    | Outer Slots | Discipline | Remaining Variable Slots |
  |----------|-------------|------------|--------------------------|
  | Triangle | 3           | 1          | 2                        |
  | Square   | 4           | 1          | 3                        |
  | Pentagon | 5           | 1          | 4                        |
  | Circle   | 6           | 1          | 5 (all)                  |

  Then one sentence: "A Triangle sigil cannot specify more than 2 outer variables beyond
  Discipline — this is a geometric constraint, not a tier limit."

(b) In the Center Core section, after the existing Hook and Mode bullet points, add:

  "Hook and Mode together carry a cost multiplier that applies to the spell's total outer
  variable cost. Simple physical interactions default to x1. Effects operating at the
  identity, soul, or fundamental-law level carry multipliers from x10 to x100. This is
  how T7–T9 costs are reached: the outer variables describe what the sigil is shaped to
  do; Hook and Mode describe how deeply the Flux must reach to do it. See [[Flux Cost Reference]]
  for the full multiplier table."

Keep all other text identical.

### 3. content/Discipline.md — WRITE (replace entire file)

Two additions needed:

(a) Add "(xN)" after each discipline name in the Disciplines list. Exact values:
Raw (x1), Force (x2), Heat (x2), Light (x3), Sound (x4), Electric (x5), Chemical (x5),
Binding (x10), Mind (x25), Soul (x75)

(b) Add a new section "## Cost Multipliers" after the discipline list and before
"## Discipline vs Output Mode". Write in the existing voice. Must cover:
- Each discipline multiplies Shape base W to produce the core Flux demand
- Raw x1: no discriminating precision required — unfiltered Flux
- Soul x75: the finest discrimination the Flux system supports — must find and interact
  with soul-signature specifically
- The gap (x1 vs x75) means Triangle Soul (3x75=225W, T3) costs more than Circle Force
  (55x2=110W, T2) before any variable additions
- Mass grimoires favor Force, Heat, Binding (x2, x2, x10) because their multipliers
  produce effects at tiers common practitioners can access. Mind (x25) and Soul (x75)
  floor their total cost above T3–T4 even in the simplest Triangle configurations.
- Include this reference table:

  | Discipline | Multiplier | Triangle core W | Circle core W |
  |------------|------------|-----------------|---------------|
  | Raw        | x1         | 3 W             | 55 W          |
  | Force      | x2         | 6 W             | 110 W         |
  | Heat       | x2         | 6 W             | 110 W         |
  | Light      | x3         | 9 W             | 165 W         |
  | Sound      | x4         | 12 W            | 220 W         |
  | Electric   | x5         | 15 W            | 275 W         |
  | Chemical   | x5         | 15 W            | 275 W         |
  | Binding    | x10        | 30 W            | 550 W         |
  | Mind       | x25        | 75 W            | 1,375 W       |
  | Soul       | x75        | 225 W           | 4,125 W       |

### 4. content/Control Tier.md — APPEND (add one section before the final See also line)

Add this section inserted before the *See also* line:

## Watt Cost Ranges

Every tier corresponds to a Flux cost range measured in [[Watts]]. The ranges below reflect
outer-variable costs from the [[Flux Cost Reference]] — the structural cost of the sigil
geometry before Hook/Mode action complexity is applied.

| Tier | W Range           | Canonical example                                        |
|------|-------------------|----------------------------------------------------------|
| T0   | 1–10 W            | Triangle Raw, single default                             |
| T1   | 11–40 W           | Triangle Light + Timed Long (34W)                        |
| T2   | 41–130 W          | Triangle Binding + Touch + Latched + Object (74W)        |
| T3   | 131–400 W         | Circle Heat + Medium + Sustained + Individual (133W)     |
| T4   | 401–1,300 W       | Circle Binding + Touch + Sustained + Individual (560W)   |
| T5   | 1,301–4,000 W     | Circle Mind + Field + LoS + Group (1,555W)               |
| T6   | 4,001–13,000 W    | Circle Soul + Touch + Permanent + Individual (4,535W)    |
| T7   | 13,001–40,000 W   | Hook/Mode Extreme (x10) applied to T5–T6 outer structure |
| T8   | 40,001–130,000 W  | Hook/Mode Transcendent (x30) on T6 outer structure       |
| T9   | 130,001+ W        | Hook/Mode Absolute (x100), or Transcendent on max structure|

T0–T6 are reachable through outer sigil variables alone. T7–T9 require elevated Hook/Mode
complexity — the outer variables alone cannot produce costs above approximately 5,000W regardless
of configuration. A practitioner may have the tier ceiling to execute a T7 effect. Whether they
can construct the action its Hook requires is a separate question.

---

## RULES FOR THIS TASK

- Do NOT invent new lore, characters, locations, or factions.
- Do NOT change any content beyond what is explicitly described above.
- Preserve all existing prose, links, and See Also sections exactly unless instructed otherwise.
- Write in the existing voice: matter-of-fact, dense, no purple prose.
- Every WRITE block must contain the FULL file content, not just the changed section.
- Every number in this task is canon. Do not round, estimate, or substitute.
- These are 4 files total. Plan them as 2 batches of 2.
