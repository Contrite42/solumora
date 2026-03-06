[[Persistence]] defines how long a spell remains active and what causes it to end. It governs duration, shutdown conditions, and whether an effect is a single event or an ongoing state.

When Persistence is not specified by the spell’s [[Shape]], it defaults to Immediate.

## Persistence Options (Scholar Standard)

- **Immediate** (default)  
   The spell occurs once and ends. This is the safest and most common persistence for low-control casting.
  ![[Persistence__IMMEDIATE 1.png]]
- **Timed (Short)** — up to **1 minute**  
   The spell remains active for a brief, fixed window, then shuts down automatically.
  ![[Persistence__TIMED_SHORT 1.png]]
- **Timed (Long)** — up to **1 hour**  
   The spell remains active for an extended fixed window, then shuts down automatically.
  ![[Persistence__TIMED_LONG 1.png]]
- **Sustained**
  The spell remains active only while the caster continuously maintains it. If focus breaks or channeling stops, the spell ends.
  ![[Persistence__SUSTAINED 1.png]]
- **Conditional**
  The spell persists until a specified condition is met (a trigger, threshold, event, or rule resolution), then ends.
  ![[Persistence__CONDITIONAL 1.png]]
- **Latched**
  The spell stays active until deliberately released (by a known action, hand sign, keyed mark, or authorized cancellation). It can outlast the caster’s immediate attention.
  ![[Persistence__LATCHED 1.png]]
- **Permanent**
  The spell does not naturally expire. It persists indefinitely, though many permanent spells require periodic maintenance, refreshing, or a stable anchor to remain healthy over time.
  ![[Persistence__PERMANENT 1.png]]

## Practical notes

- Immediate spells are preferred for mass use because they minimize the time a spell can drift, degrade, or misbehave.
- Longer persistence generally demands better control and steadier channeling; if a caster cannot supply enough [[Flux]] to sustain a spell, the effect may weaken, stutter, or terminate early.
  _See also: [[Reach]], [[Spell Variables]], [[Sigils]], [[Control Tier]]_
