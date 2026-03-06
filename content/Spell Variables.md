[[Sigils]] encode spells as geometric arrangements of variables. Each variable occupies a specific position in the shape and defines one aspect of what the spell does — its discipline, reach, duration, targeting, and output characteristics. The [[Flux Cost Reference]] provides the complete cost tables; this page explains what each variable controls and how they interact.

## Shape (Outer Variable #1)

Shape determines the spell's base [[Flux]] cost and constrains how many other variables can be specified. Each outer point of the shape represents one variable slot. [[Discipline]] always occupies one slot, leaving the remainder available for other outer variables.

| Shape    | Outer Slots | Discipline | Remaining Variable Slots |
| -------- | ----------- | ---------- | ------------------------ |
| Triangle | 3           | 1          | 2                        |
| Square   | 4           | 1          | 3                        |
| Pentagon | 5           | 1          | 4                        |
| Circle   | 6           | 1          | 5 (all)                  |

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
- **[[Binding]]** (×10): Constraint effects, sealing, structural reinforcement, immobilization
- **Mind** (×25): Neural interaction, thought reading, emotional influence, memory work
- **Soul** (×75): Soul-signature interaction, identity effects, spiritual manipulation

The multiplier gap reflects the precision demand each discipline places on the [[Flux]] field. Raw requires no discriminating precision. Soul requires the finest discrimination the system supports — the [[Flux]] must locate and interact with soul-signature specifically, a task exponentially more complex than simple energy channeling.

## [[Pattern]] (Outer Variable #3)

Pattern defines the geometric shape of the spell's effect in physical space.

- **Point**: Effect concentrated at a single location (0W)
- **Plane**: Flat surface effect, default for most spells (0W)
- **Beam**: Linear projection (+5W)
- **Cone**: Expanding triangular area (+10W)
- **Ring**: Circular perimeter effect (+15W)
- **Cylinder**: Tube-shaped volume (+20W)
- **Sphere**: Spherical volume effect (+30W)
- **Field**: Large area coverage, irregular boundaries (+60W)

Pattern interacts with other variables to determine the spell's practical application. A Heat discipline with Sphere pattern creates a zone of elevated temperature. The same discipline with Beam pattern creates a focused thermal lance. The [[Flux]] cost difference reflects the geometric complexity of maintaining the effect's shape.

## Reach (Outer Variable #4)

Reach determines the maximum distance between caster and effect.

- **Self**: Effect originates from or affects the caster directly (0W)
- **Touch**: Effect requires physical contact with target (+2W)
- **Short**: Effective range approximately 10 feet (+5W)
- **Medium**: Effective range approximately 50 feet (+15W)
- **Long**: Effective range approximately 200 feet (+40W)
- **Line-of-Sight**: Effect can reach any point the caster can see clearly (+80W)
- **Linked**: Effect can reach a previously marked target regardless of distance (+150W)

Extended reach requires the [[Flux]] to maintain coherence across greater distances, increasing the precision demand exponentially. Line-of-Sight effects must account for atmospheric interference, obstacles, and the difficulty of maintaining targeting accuracy at distance. Linked effects require the most sophisticated targeting — the spell must locate a specific marked signature anywhere within the [[Flux]] field's range.

## Persistence (Outer Variable #5)

Persistence controls how long the spell's effect continues after casting.

- **Immediate**: Effect occurs once and ends (0W)
- **Timed Short**: Effect continues for up to one minute (+5W)
- **Timed Long**: Effect continues for up to one hour (+25W)
- **Sustained**: Effect continues as long as caster maintains it (+10W per 10-minute interval)
- **Conditional**: Effect continues until a specified condition is met (+20W)
- **Latched**: Effect continues until deliberately dispelled (+40W)
- **Permanent**: Effect continues indefinitely without maintenance (+400W)

Permanent effects require the spell to establish self-sustaining [[Flux]] patterns that continue operating without ongoing caster input. This represents one of the most complex tasks the [[Flux]] system can perform — creating stable, persistent alterations to local reality that maintain themselves indefinitely.

## Target Spec (Outer Variable #6)

Target Spec defines what the spell affects and how it identifies valid targets.

- **Where Written**: Effect occurs at the location where the sigil is inscribed (0W)
- **Self**: Effect targets the caster specifically (0W)
- **Object**: Effect targets a single inanimate object (+2W)
- **Surface**: Effect targets a defined surface area (+5W)
- **Individual**: Effect targets a single person or creature (+8W)
- **Marked**: Effect targets a previously marked person or object (+15W)
- **Group**: Effect targets multiple individuals simultaneously (+35W)
- **Filter**: Effect targets based on specified characteristics (+60W)

Complex targeting requires the [[Flux]] to distinguish between valid and invalid targets, often in real-time as conditions change. Filter targeting is the most sophisticated — the spell must evaluate potential targets against specified criteria and affect only those that match, while ignoring everything else in the area.

## Output Mode (Outer Variable #7)

Output Mode determines what type of effect the spell produces, which may differ from its [[Discipline]]. Natural pairings carry no additional cost. Cross-discipline outputs require additional [[Flux]] precision.

- **Natural pairing**: Heat→Thermal, Force→Kinetic, Light→Photonic, etc. (0W)
- **Adjacent discipline**: Heat→Kinetic, Force→Thermal, etc. (+10W)
- **Cross-type**: Force→Neuro, Heat→Soul, etc. (+30W)
- **Extreme cross**: Physical discipline→Soul output, etc. (+60W)

Cross-discipline outputs require the [[Flux]] to translate between different types of energy or effect. A Force discipline producing Neuro output must convert kinetic energy into neural stimulation — a complex transformation that increases the spell's precision requirements significantly.

## Center Core Variables

The center of every sigil contains two variables that do not occupy outer slots: [[Hook]] and [[Mode]]. These define the spell's core action — what it fundamentally does rather than how it reaches or affects its target.

**Hook** defines the primary action: detect, move, alter, create, destroy, read, write, bind, release. **Mode** defines the intent or method: gentle, forced, precise, broad, temporary, permanent, conditional, absolute.

Hook and Mode together carry a cost multiplier that applies to the spell's total outer variable cost. Simple physical interactions default to ×1. Effects operating at the identity, soul, or fundamental-law level carry multipliers from ×10 to ×100. This is how T7–T9 costs are reached: the outer variables describe what the sigil is shaped to do; Hook and Mode describe how deeply the [[Flux]] must reach to do it. See [[Flux Cost Reference]] for the full multiplier table.

## Variable Interaction

Variables do not operate independently — they interact to determine the spell's final behavior and cost. A Heat discipline with Sphere pattern and Group targeting creates a zone of temperature control that affects multiple people simultaneously. The same discipline with Beam pattern and Individual targeting creates a focused thermal effect on a single person. The [[Flux]] cost reflects not just the sum of the variables but the complexity of their interaction.

Some variable combinations are more efficient than others. Touch reach with Individual targeting is straightforward — the spell affects the person the caster is touching. Line-of-Sight reach with Filter targeting is complex — the spell must identify valid targets at distance based on specified criteria, then affect only those targets while ignoring everything else visible.

Understanding these interactions is essential for efficient spell design. A practitioner who can achieve the desired effect with simpler variable combinations will always have an advantage over one who requires complex interactions to produce the same result.

_See also: [[Sigils]], [[Flux]], [[Control Tier]], [[Flux Cost Reference]], [[Shape]], [[Discipline]], [[Hook]], [[Mode]], [[Flux Expenditure]], [[Reach]], [[Persistence]], [[Target Spec]], [[Output Mode]], [[Binding]], [[Pattern]], [[Filter]]_
