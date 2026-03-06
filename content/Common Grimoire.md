Common spells require [[Control Tier]] T1–T2 and represent the backbone of everyday [[Flux]] use across [[Solumora]]. The majority of the population can cast at least some of these. They are the spells found in every home, workshop, and market stall — mass-produced, widely copied, and deliberately simple.

_Return to [[All Grimoire]]_

---

**Hearthlight**
A warm orb of light anchors to the written sigil and illuminates the surrounding area.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Light |
| Output | Photonic |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Glowmark**
Causes the inscribed sigil surface to emit a faint steady photonic glow, functioning as a permanent low-cost marker or waypoint light.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Light |
| Output | Photonic |
| Pattern | Point |
| Reach | _(default — Self)_ |
| Persistence | Sustained |
| Target | _(default — Where Written)_ |

---

**Warmstone**
Transfers steady heat into the inscribed object, keeping it warm for up to one hour.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T1 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | Plane |
| Reach | _(default — Self)_ |
| Persistence | Timed (Long) |
| Target | _(default — Where Written)_ |

---

**Chill Touch**
Draws heat out of a touched object on contact, rapidly cooling it to a safe handling temperature.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T1 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | _(default — Plane)_ |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Dryseal**
Accelerates evaporation across a flat surface, leaving it completely dry within moments of activation.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T1 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Heatcheck**
Takes an immediate thermal reading of a touched object, giving the caster a clear sense of its temperature and heat distribution.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Sense |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | _(default — Plane)_ |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Drycleave**
Instantly strips moisture and surface contaminants from the inscribed object using a reactive chemical burst.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Filter |
| Mode | Affect |
| Control Tier | T1 |
| Discipline | Chemical |
| Output | Reactive |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Inkmark**
Burns a faint but permanent sigil-compatible mark onto a surface or object on contact, usable as a pairing anchor for linked spells.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Bind |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Binding |
| Output | Constraint |
| Pattern | _(default — Plane)_ |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Knocksense**
Detects physical impact or pressure against the inscribed surface and logs its direction, used for structural monitoring and perimeter checking.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Sense |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Force |
| Output | Kinetic |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | Conditional |
| Target | _(default — Where Written)_ |

---

**Chargecheck**
Detects the presence and polarity of electrical charge in a touched object, used by engineers and artificers to diagnose mechanisms.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Sense |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Electric |
| Output | Shock |
| Pattern | _(default — Plane)_ |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Nudge**
Applies a brief directed kinetic push to a small object within reach, moving it a short distance without physical contact.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Move |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Force |
| Output | Kinetic |
| Pattern | _(default — Plane)_ |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | Object |

---

**Shove**
Releases a single raw kinetic burst from the written sigil, pushing anything in the immediate plane away from the point of origin.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Force |
| Output | Kinetic |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Crackle**
Discharges a small electrical spark from the sigil on contact, delivering a painful but non-lethal shock — common deterrent sigil on handles and locks.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T1 |
| Discipline | Electric |
| Output | Shock |
| Pattern | _(default — Plane)_ |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Coldbox Seal**
Draws heat out of the inscribed surface and holds it cold for up to one hour, functioning as a portable cold storage seal.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | Plane |
| Reach | _(default — Self)_ |
| Persistence | Timed (Long) |
| Target | Surface |

---

**Steadyflame**
Anchors a small sustained flame to the written sigil that burns cleanly without fuel for up to one hour.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Emit |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | Point |
| Reach | _(default — Self)_ |
| Persistence | Timed (Long) |
| Target | _(default — Where Written)_ |

---

**Mending Seal**
Applies a reactive chemical bond to a cracked or broken object on contact, fusing the material back together.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Chemical |
| Output | Reactive |
| Pattern | Plane |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | Object |

---

**Fumegate**
Releases a short-lived reactive chemical cloud from the sigil surface, neutralizing airborne contaminants and pests in the immediate area.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Emit |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Chemical |
| Output | Reactive |
| Pattern | Sphere |
| Reach | _(default — Self)_ |
| Persistence | Timed (Short) |
| Target | _(default — Where Written)_ |

---

**Breathclean**
Filters chemical contaminants and particulates out of the air within a short sphere around the caster for up to one minute.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Filter |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Chemical |
| Output | Reactive |
| Pattern | Sphere |
| Reach | Short |
| Persistence | Timed (Short) |
| Target | Self |

---

**Lockward**
Binds a door, chest, or container shut with a constraint force that holds until deliberately released by a keyed action.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Bind |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Binding |
| Output | Constraint |
| Pattern | Plane |
| Reach | Touch |
| Persistence | Latched |
| Target | Object |

---

**Silence Patch**
Suppresses all sound originating from the written sigil's surface for up to one minute.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Ward |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Sound |
| Output | Sonic |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | Timed (Short) |
| Target | _(default — Where Written)_ |

---

**Muffle**
Wraps a single object in a sustained sonic dampening field, significantly reducing the noise it produces while active.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Dampen |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Sound |
| Output | Sonic |
| Pattern | Plane |
| Reach | Touch |
| Persistence | Sustained |
| Target | Object |

---

**Sharpen**
Temporarily hardens and refines the edge of a bladed object on contact, improving its cutting ability for up to one minute.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Force |
| Output | Kinetic |
| Pattern | Plane |
| Reach | Touch |
| Persistence | Timed (Short) |
| Target | Object |

---

**Stonehard**
Temporarily increases the structural density of a surface or object, making it significantly harder to cut, break, or deform.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Force |
| Output | Kinetic |
| Pattern | Plane |
| Reach | Touch |
| Persistence | Timed (Long) |
| Target | Object |

---

**Insulationlayer**
Coats the inscribed surface in a thin reactive chemical layer that resists electrical conduction, protecting the object from shock-based damage.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Chemical |
| Output | Reactive |
| Pattern | Plane |
| Reach | Touch |
| Persistence | Timed (Long) |
| Target | Object |

---

**Copymark**
Transfers the exact surface impression of a sigil or inscription from one object to another on contact, used by Scribes for precision duplication.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Shape |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Binding |
| Output | Constraint |
| Pattern | Plane |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | Object |

---

**Tripwire**
Waits silently on the inscribed surface until a physical threshold is crossed, then fires a raw pulse to alert the caster.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Trigger |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Raw |
| Output | Raw |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | Conditional |
| Target | _(default — Where Written)_ |

---

**Fluxread**
Senses and maps the presence and intensity of active Flux within a short radius, revealing channeling or inscribed sigils nearby.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Sense |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Raw |
| Output | Raw |
| Pattern | Sphere |
| Reach | Short |
| Persistence | _(default — Immediate)_ |
| Target | Filter |

---

**Breathsense**
Detects the presence of living beings within a short radius by sensing the heat and chemical signature of respiration.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Sense |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Chemical |
| Output | Reactive |
| Pattern | Sphere |
| Reach | Short |
| Persistence | _(default — Immediate)_ |
| Target | Filter |

---

**Flashburst**
Emits a blinding burst of photonic light from the sigil, overwhelming the vision of anyone looking toward it.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Light |
| Output | Photonic |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Heatpalm**
Channels a focused thermal burst through direct contact, burning the touched target at the point of contact.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | _(default — Plane)_ |
| Reach | Touch |
| Persistence | _(default — Immediate)_ |
| Target | Individual |

---

**Forcepulse**
Releases a blunt kinetic burst in a directed cone from the caster, pushing everything in its spread away from the origin point.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Emit |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Force |
| Output | Kinetic |
| Pattern | Cone |
| Reach | Short |
| Persistence | _(default — Immediate)_ |
| Target | _(default — Where Written)_ |

---

**Hardenskin**
Applies a brief force-layer to the caster's body, slightly hardening the surface against incoming physical impact.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Force |
| Output | Kinetic |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | Timed (Short) |
| Target | _(default — Where Written)_ |

---

**Slickplane**
Coats a surface with a low-friction reactive chemical layer, causing anyone stepping on it to lose footing for up to one minute.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Transform |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Chemical |
| Output | Reactive |
| Pattern | Plane |
| Reach | Touch |
| Persistence | Timed (Short) |
| Target | Surface |

---

**Fluxhold**
An open Flux reservoir inscribed onto a physical object — slowly charges from ambient Flux over time, can be drawn from by anyone, and burns out entirely when depleted.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Bind |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Binding |
| Output | Constraint |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | Latched |
| Target | _(default — Where Written)_ |

---

**Fluxhold (Keyed)**
A keyed Flux reservoir inscribed onto a physical object — slowly charges from ambient Flux over time, can only be drawn from by the paired marked caster, and burns out entirely when depleted.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Bind |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Binding |
| Output | Constraint |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | Latched |
| Target | Marked |

---

**Fluxhold (Conditional)**
A conditional Flux reservoir inscribed onto a physical object — slowly charges from ambient Flux over time, releases its full stored charge only when a defined trigger condition is met, and burns out entirely on release.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Bind |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Binding |
| Output | Constraint |
| Pattern | _(default — Plane)_ |
| Reach | _(default — Self)_ |
| Persistence | Conditional |
| Target | _(default — Where Written)_ |

---

**Bluntedge**
Temporarily softens and dulls the cutting edge of a blade on contact, rendering it safe to handle without injury.

| Variable     | Value               |
| ------------ | ------------------- |
| Shape        | Triangle            |
| Hook         | Transform           |
| Mode         | Affect              |
| Control Tier | T1                  |
| Discipline   | Force               |
| Output       | Kinetic             |
| Pattern      | _(default — Plane)_ |
| Reach        | Touch               |
| Persistence  | Timed (Short)       |
| Target       | Object              |

---

**Chillbox**
Rapidly lowers the temperature of a small enclosed space to near-freezing, functioning as an emergency cold store.

| Variable     | Value              |
| ------------ | ------------------ |
| Shape        | Square             |
| Hook         | Transform          |
| Mode         | Affect             |
| Control Tier | T2                 |
| Discipline   | Heat               |
| Output       | Thermal            |
| Pattern      | Field              |
| Reach        | _(default — Self)_ |
| Persistence  | Timed (Long)       |
| Target       | Surface            |

---

**Coldbreath**
Chills the air immediately around the caster's face, providing brief relief from intense heat exposure.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Heat                        |
| Output       | Thermal                     |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | Timed (Short)               |
| Target       | _(default — Where Written)_ |

---

**Dimmer**
Gradually reduces the photonic output of a light source over a timed window, used for controlled dimming without extinguishing.

| Variable     | Value         |
| ------------ | ------------- |
| Shape        | Square        |
| Hook         | Dampen        |
| Mode         | Affect        |
| Control Tier | T2            |
| Discipline   | Light         |
| Output       | Photonic      |
| Pattern      | Plane         |
| Reach        | Touch         |
| Persistence  | Timed (Short) |
| Target       | Object        |

---

**Dustsweep**
Pushes loose debris, dust, and surface grime off a flat surface in a single raw kinetic pass.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Move                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Force                       |
| Output       | Kinetic                     |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | _(default — Immediate)_     |
| Target       | _(default — Where Written)_ |

---

**Echolocate**
Emits a low sonic pulse that bounces off nearby surfaces and returns a rough spatial map of the immediate environment to the caster.

| Variable     | Value                   |
| ------------ | ----------------------- |
| Shape        | Square                  |
| Hook         | Sense                   |
| Mode         | Create                  |
| Control Tier | T2                      |
| Discipline   | Sound                   |
| Output       | Sonic                   |
| Pattern      | Sphere                  |
| Reach        | Short                   |
| Persistence  | _(default — Immediate)_ |
| Target       | Self                    |

---

**Emberglow**
Sustains a faint thermal warmth across an inscribed object indefinitely, keeping it perpetually warm to the touch.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Heat                        |
| Output       | Thermal                     |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | Permanent                   |
| Target       | _(default — Where Written)_ |

---

**Flashmark**
Imprints a brief bright photonic impression of the sigil onto the retinas of anyone looking directly at it when activated.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Light                       |
| Output       | Photonic                    |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | _(default — Immediate)_     |
| Target       | _(default — Where Written)_ |

---

**Fogshroud**
Releases a brief reactive chemical fog from the sigil surface, obscuring vision in the immediate area for up to one minute.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Square                      |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T2                          |
| Discipline   | Chemical                    |
| Output       | Reactive                    |
| Pattern      | Sphere                      |
| Reach        | Short                       |
| Persistence  | Timed (Short)               |
| Target       | _(default — Where Written)_ |

---

**Forceanchor**
Pins a small object to a surface with a persistent kinetic force, holding it immobile until released.

| Variable     | Value   |
| ------------ | ------- |
| Shape        | Square  |
| Hook         | Bind    |
| Mode         | Create  |
| Control Tier | T2      |
| Discipline   | Force   |
| Output       | Kinetic |
| Pattern      | Plane   |
| Reach        | Touch   |
| Persistence  | Latched |
| Target       | Object  |

---

**Gripcoat**
Applies a tacky reactive layer to a surface or handle, significantly improving grip for up to one minute.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Transform                   |
| Mode         | Affect                      |
| Control Tier | T1                          |
| Discipline   | Chemical                    |
| Output       | Reactive                    |
| Pattern      | _(default — Plane)_         |
| Reach        | Touch                       |
| Persistence  | Timed (Short)               |
| Target       | _(default — Where Written)_ |

---

**Heatthread**
Runs a sustained line of precise thermal output along a defined path on a surface, used for controlled cutting, soldering, or cauterization.

| Variable     | Value     |
| ------------ | --------- |
| Shape        | Square    |
| Hook         | Emit      |
| Mode         | Create    |
| Control Tier | T2        |
| Discipline   | Heat      |
| Output       | Thermal   |
| Pattern      | Beam      |
| Reach        | Touch     |
| Persistence  | Sustained |
| Target       | Surface   |

---

**Hushfield**
Generates a sustained sound-dampening field around a single object, muffling all noise it produces while active.

| Variable     | Value              |
| ------------ | ------------------ |
| Shape        | Square             |
| Hook         | Ward               |
| Mode         | Affect             |
| Control Tier | T2                 |
| Discipline   | Sound              |
| Output       | Sonic              |
| Pattern      | Sphere             |
| Reach        | _(default — Self)_ |
| Persistence  | Sustained          |
| Target       | Object             |

---

**Lightbeam**
Projects a steady narrow beam of photonic light from the sigil in a fixed direction, functioning as a reliable hands-free torch.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Square                      |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T2                          |
| Discipline   | Light                       |
| Output       | Photonic                    |
| Pattern      | Beam                        |
| Reach        | _(default — Self)_          |
| Persistence  | Sustained                   |
| Target       | _(default — Where Written)_ |

---

**Lightpatch**
Applies a dim but permanent photonic glow to any flat surface, commonly used for stairwells, alley markers, and cheap indoor lighting.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Light                       |
| Output       | Photonic                    |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | Permanent                   |
| Target       | _(default — Where Written)_ |

---

**Mindnoise**
Floods the immediate area with low-level neuro-disrupting static, making it difficult to concentrate or hold fine detail for up to one minute.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Square                      |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T2                          |
| Discipline   | Mind                        |
| Output       | Neuro                       |
| Pattern      | Sphere                      |
| Reach        | Short                       |
| Persistence  | Timed (Short)               |
| Target       | _(default — Where Written)_ |

---

**Presspoint**
Delivers a precise focused pressure burst to a single point on contact — used medically to stop minor bleeding or test sensation.

| Variable     | Value                   |
| ------------ | ----------------------- |
| Shape        | Triangle                |
| Hook         | Emit                    |
| Mode         | Create                  |
| Control Tier | T1                      |
| Discipline   | Force                   |
| Output       | Kinetic                 |
| Pattern      | _(default — Plane)_     |
| Reach        | Touch                   |
| Persistence  | _(default — Immediate)_ |
| Target       | Individual              |

---

**Pulsecheck**
Sends a raw Flux pulse through a touched object, returning a basic sense of its structural integrity — cracks, hollow spaces, weak points.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Sense                       |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Raw                         |
| Output       | Raw                         |
| Pattern      | _(default — Plane)_         |
| Reach        | Touch                       |
| Persistence  | _(default — Immediate)_     |
| Target       | _(default — Where Written)_ |

---

**Rustblock**
Applies a thin reactive coating to a metal surface that halts oxidation on contact.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Transform                   |
| Mode         | Affect                      |
| Control Tier | T1                          |
| Discipline   | Chemical                    |
| Output       | Reactive                    |
| Pattern      | _(default — Plane)_         |
| Reach        | Touch                       |
| Persistence  | _(default — Immediate)_     |
| Target       | _(default — Where Written)_ |

---

**Scentstrip**
Chemically neutralizes odor from the inscribed surface, leaving it scent-neutral for a short window.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Filter                      |
| Mode         | Affect                      |
| Control Tier | T1                          |
| Discipline   | Chemical                    |
| Output       | Reactive                    |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | Timed (Short)               |
| Target       | _(default — Where Written)_ |

---

**Scorchdot**
Burns a precise small point onto a surface using focused thermal output — used for marking, branding, and controlled material removal.

| Variable     | Value                   |
| ------------ | ----------------------- |
| Shape        | Square                  |
| Hook         | Emit                    |
| Mode         | Create                  |
| Control Tier | T2                      |
| Discipline   | Heat                    |
| Output       | Thermal                 |
| Pattern      | Point                   |
| Reach        | Touch                   |
| Persistence  | _(default — Immediate)_ |
| Target       | Surface                 |

---

**Shockloop**
Runs a contained electrical current through a defined ring on a surface, creating a persistent shock barrier anyone crossing the loop will trigger.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Square                      |
| Hook         | Ward                        |
| Mode         | Create                      |
| Control Tier | T2                          |
| Discipline   | Electric                    |
| Output       | Shock                       |
| Pattern      | Ring                        |
| Reach        | _(default — Self)_          |
| Persistence  | Latched                     |
| Target       | _(default — Where Written)_ |

---

**Shockpad**
Stores a latent electrical charge in the inscribed surface, releasing it as a painful shock the next time the surface is touched without authorization.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Square                      |
| Hook         | Trigger                     |
| Mode         | Create                      |
| Control Tier | T2                          |
| Discipline   | Electric                    |
| Output       | Shock                       |
| Pattern      | Plane                       |
| Reach        | _(default — Self)_          |
| Persistence  | Conditional                 |
| Target       | _(default — Where Written)_ |

---

**Solventstrip**
Applies a reactive chemical dissolve to an adhesive bond, breaking glue, resin, or binding compounds on contact.

| Variable     | Value                   |
| ------------ | ----------------------- |
| Shape        | Square                  |
| Hook         | Transform               |
| Mode         | Affect                  |
| Control Tier | T2                      |
| Discipline   | Chemical                |
| Output       | Reactive                |
| Pattern      | Plane                   |
| Reach        | Touch                   |
| Persistence  | _(default — Immediate)_ |
| Target       | Object                  |

---

**Soundping**
Emits a single sharp sonic tone from the inscribed surface, audible up to 30 feet away — used as a simple alert or signal.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Sound                       |
| Output       | Sonic                       |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | _(default — Immediate)_     |
| Target       | _(default — Where Written)_ |

---

**Sparknail**
Drives a small focused kinetic point into a surface on contact, functioning as a precise fastening force for lightweight materials.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Bind                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Force                       |
| Output       | Kinetic                     |
| Pattern      | _(default — Plane)_         |
| Reach        | Touch                       |
| Persistence  | _(default — Immediate)_     |
| Target       | _(default — Where Written)_ |

---

**Staticsnap**
Releases a small but sharp electrical snap at the point of contact — startling but harmless, used as a deterrent on small valuables.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Electric                    |
| Output       | Shock                       |
| Pattern      | _(default — Plane)_         |
| Reach        | Touch                       |
| Persistence  | _(default — Immediate)_     |
| Target       | _(default — Where Written)_ |

---

**Stickbind**
Creates a strong adhesive reactive bond between two surfaces on contact, holding them together for up to one hour.

| Variable     | Value        |
| ------------ | ------------ |
| Shape        | Square       |
| Hook         | Bind         |
| Mode         | Create       |
| Control Tier | T2           |
| Discipline   | Chemical     |
| Output       | Reactive     |
| Pattern      | Plane        |
| Reach        | Touch        |
| Persistence  | Timed (Long) |
| Target       | Object       |

---

**Vibrasense**
Detects vibration patterns in a touched surface, allowing the caster to identify footsteps, machinery, or structural stress through solid material.

| Variable     | Value     |
| ------------ | --------- |
| Shape        | Square    |
| Hook         | Sense     |
| Mode         | Create    |
| Control Tier | T2        |
| Discipline   | Sound     |
| Output       | Sonic     |
| Pattern      | Plane     |
| Reach        | Touch     |
| Persistence  | Sustained |
| Target       | Surface   |

---

**Warmbreath**
Gently heats the air immediately around the caster's face and chest, taking the edge off cold exposure for a short window.

| Variable     | Value                       |
| ------------ | --------------------------- |
| Shape        | Triangle                    |
| Hook         | Emit                        |
| Mode         | Create                      |
| Control Tier | T1                          |
| Discipline   | Heat                        |
| Output       | Thermal                     |
| Pattern      | _(default — Plane)_         |
| Reach        | _(default — Self)_          |
| Persistence  | Timed (Short)               |
| Target       | _(default — Where Written)_ |

---

**Weightshift**
Temporarily reduces the effective weight of a touched object by dampening its interaction with downward kinetic force.

| Variable     | Value         |
| ------------ | ------------- |
| Shape        | Square        |
| Hook         | Dampen        |
| Mode         | Affect        |
| Control Tier | T2            |
| Discipline   | Force         |
| Output       | Kinetic       |
| Pattern      | Plane         |
| Reach        | Touch         |
| Persistence  | Timed (Short) |
| Target       | Object        |

---

**Raw Lantern Mark**
Creates a short-lived neutral flux marker for close work.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T0 |
| Rarity | Common |
| Watts | 3 W |
| Discipline | Raw |
| Output | Raw |
| Pattern | Point |
| Reach | Self |
| Persistence | Immediate |
| Target | Where Written |

---

**Force Lantern Mark**
Creates a short-lived kinetic force marker for close work.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T0 |
| Rarity | Common |
| Watts | 7 W |
| Discipline | Force |
| Output | Kinetic |
| Pattern | Point |
| Reach | Self |
| Persistence | Immediate |
| Target | Where Written |

---

**Heat Lantern Mark**
Creates a short-lived thermal transfer marker for close work.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Emit |
| Mode | Create |
| Control Tier | T0 |
| Rarity | Common |
| Watts | 7 W |
| Discipline | Heat |
| Output | Thermal |
| Pattern | Point |
| Reach | Self |
| Persistence | Immediate |
| Target | Where Written |


---

**Binding Amplify Beam**
Boosts binding constraint flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Amplify |
| Mode | Affect |
| Control Tier | T2 |
| Rarity | Common |
| Watts | 77 W |
| Discipline | Binding |
| Output | Constraint |
| Pattern | Beam |
| Reach | Self |
| Persistence | Immediate |
| Target | Where Written |


---

**Binding Amplify Cone**
Boosts binding constraint flux as a fan spread at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Amplify |
| Mode | Affect |
| Control Tier | T2 |
| Rarity | Common |
| Watts | 88 W |
| Discipline | Binding |
| Output | Constraint |
| Pattern | Cone |
| Reach | Self |
| Persistence | Immediate |
| Target | Where Written |


---

**Binding Amplify Cylinder**
Boosts binding constraint flux as a column volume at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Amplify |
| Mode | Affect |
| Control Tier | T2 |
| Rarity | Common |
| Watts | 110 W |
| Discipline | Binding |
| Output | Constraint |
| Pattern | Cylinder |
| Reach | Self |
| Persistence | Immediate |
| Target | Where Written |


---

**Constraint Flux Augment**
Boosts binding constraint flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Amplify |
| Mode | Affect |
| Control Tier | T2 |
| Rarity | Common |
| Watts | 77 W |
| Discipline | Binding |
| Output | Constraint |
| Pattern | Beam |
| Reach | Self |
| Persistence | Immediate |
| Target | Where Written |
| Spell Page | [[Spells/Heat Ring of Triangle|Heat Ring of Triangle]] |


---


---

**Light Trigger Beam**
Arms light sonic flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by creating a fresh flux expression.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Trigger |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Light |
| Output | Sonic |
| Pattern | Beam |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Sound Filter Beam**
Screens sound sonic flux as a directed line at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Filter |
| Mode | Affect |
| Control Tier | T1 |
| Discipline | Sound |
| Output | Sonic |
| Pattern | Beam |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Heat Emit Plane**
Releases heat thermal flux as a planar spread at self reach, targeting a grouped cluster with immediate discharge by creating a fresh flux expression.
| Variable | Value |
|---|---|
| Shape | Square |
| Hook | Emit |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Heat |
| Output | Thermal |
| Pattern | Plane |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | Group |


---

**Binding Filter Point**
Screens binding constraint flux as a point focus at self reach, targeting the inscribed anchor with immediate discharge by changing existing conditions.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Filter |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Binding |
| Output | Constraint |
| Pattern | Point |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Spell That Waits**
A spell that waits to release effects using electric magic.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Trigger |
| Mode | Affect |
| Control Tier | T1 |
| Discipline | Electric |
| Output | Shock |
| Pattern | Beam |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Spell That Changes**
A spell that changes effects using light magic.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Transform |
| Mode | Create |
| Control Tier | T2 |
| Discipline | Light |
| Output | Photonic |
| Pattern | Sphere |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Spell That Protects**
A spell that protects against effects using raw magic.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Ward |
| Mode | Control |
| Control Tier | T2 |
| Discipline | Raw |
| Output | Photonic |
| Pattern | Plane |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Spell That Detects**
A spell that detects effects using light magic.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Sense |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Light |
| Output | Photonic |
| Pattern | Field |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Shockstill**
A spell that dampens effects using electric magic.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Dampen |
| Mode | Affect |
| Control Tier | T2 |
| Discipline | Electric |
| Output | Shock |
| Pattern | Cylinder |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |


---

**Primaldrift**
A spell that moves effects using raw magic.
| Variable | Value |
|---|---|
| Shape | Triangle |
| Hook | Move |
| Mode | Affect |
| Control Tier | T1 |
| Discipline | Raw |
| Output | Raw |
| Pattern | Cylinder |
| Reach | _(default - Self)_ |
| Persistence | _(default - Immediate)_ |
| Target | _(default - Where Written)_ |

