# Spell Blueprint (Scholar System)

These variables form the blueprint of every spell, dictating both its structure and execution.
[[All Grimoire]]
## Center Core
At the center of every spell lie three defining elements: [[Hook]], [[Mode]], and [[Control Tier]].

- **[[Hook]]**: The spell’s core action.

- **[[Mode]]**: The spell’s intent.

- **[[Control Tier]]**: Complexity measured from Tier 0 (simplest) to Tier 9 (most advanced). The tier also determines the spell’s “shape control” level (how many variables are explicitly controlled).

## The Six Outer Variables

1. **[[Shape]]**  
   The [[Shape]] corresponds to shapes that define how many spell variables are explicitly controlled.  
   - A Circle (six points + center) provides the most control.  
   - A Pentagon (five points + center) reduces control.  
   - A Square (four points + center) simplifies further.  
   - A Triangle (three points + center) is the simplest.

   **Defaults when omitted:**  
   - [[Discipline]] defaults to Raw  
   - [[Output Mode]] defaults to Raw  
   - [[Geometry Pattern]] defaults to Plane  
   - [[Reach]] defaults to Self  
   - [[Persistence]] defaults to Immediate  
   - [[Target Spec]] defaults to **Where Written**

2. **[[Discipline]]**  
   [[Discipline]] defines the fundamental method through which a spell interacts with reality. Each discipline shapes [[Flux]] differently.  
   - Default: Raw (unfiltered)  
   - Options: Force, Heat, Electric, Chemical, Light, Sound, Mind, Binding, Soul  
   The chosen discipline determines *how* the spell’s core effect is shaped.

3. **[[Output Mode]]**  
   [[Output Mode]] defines the type of energy or interaction the spell generates.  
   - Default: Raw  
   - Options: Thermal, Kinetic, Shock, Reactive, Photonic, Sonic, Neuro, Constraint, Soul  
   The chosen output determines *what kind* of effect manifests.

4. **[[Geometry Pattern]]**  
   [[Geometry Pattern]] defines how the spell manifests in space.  
   - Default: Plane (the space of the written rune / casting surface)  
   - Options: Point, Beam, Cone, Sphere, Cylinder, Ring, Field  
   The chosen pattern determines the spell’s spatial footprint.

5. **[[Reach]]**  
   [[Reach]] determines how the spell connects to its target.  
   - Default: Self  
   - Options: Anchored, Touch, Short (10 ft), Medium (50 ft), Long (200 ft), Line-of-Sight, Linked  
   The chosen reach defines distance or connection method.

6. **[[Persistence]]**  
   [[Persistence]] determines how long the spell lasts and how it ends.  
   - Default: Immediate (instant, then ends)  
   - Options: Timed (Short) (up to 1 minute), Timed (Long) (up to 1 hour), Sustained while maintained, Conditional until trigger, Latched (until released), Permanent (indefinite, may require maintenance)  
   The chosen persistence defines duration and termination.

7. **[[Target Spec]]**  
   [[Target Spec]] specifies what the spell acts upon.  
   - Default: **Where Written** (the inscribed surface/object)  
   - Options: Self, Individual, Object, Surface, Group, Filter, Marked  
   The chosen target determines exactly who or what the spell affects.
*See also: [[Hook]], [[Mode]], [[Control Tier]], [[Flux Expenditure]], [[Shape]], [[Discipline]], [[Output Mode]], [[Geometry Pattern]], [[Reach]], [[Persistence]], [[Target Spec]], [[Sigils]]*
