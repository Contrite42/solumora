*Workshop development notes, [[Ossal Meln]], [[Valdenmoor]]. These are working notes, not a finished document. They are kept because the failure record is as useful as the success record.*

---

## Configuration Attempt 1 — Combined Thermal/Light Object

**Objective:** A single embedded-object configuration that maintains both thermal output (keeping a contained space warm) and photonic output (ambient light). Client requirement: a workshop lamp that also functions as a heat source. Wanted a single object rather than two separate embedded pieces.

**First approach:** Square base with Heat and Light disciplines simultaneously specified.

This is not how sigil geometry works. Heat and Light are separate disciplines. A Square sigil has four variable slots. You can use one discipline. You cannot distribute the discipline slot across two. I knew this. I was thinking about the client's problem and not about the formula.

The test piece failed to hold. The inscription was trying to do two incompatible things from a single discipline specification and produced neither cleanly. The thermal output was irregular — approximately 40% of target. The photonic output did not materialize. I have recorded this under my standard failure taxonomy (Error type: discipline conflict at inscription stage).

**Assessment:** The client's request is achievable. It requires two separate embedded sigils, not one. This is a communication problem more than a technical one. The client assumed combined effect meant combined object. It does not.

---

## Configuration Attempt 2 — Two-Object Solution, Initial Estimate

**Client briefing after Attempt 1:** Explained that the combined-discipline approach is not viable. A single sigil can manage one discipline. Two functions require two inscriptions, which means two objects or two inscriptions on the same object if the surface has sufficient geometry.

Client accepted this without significant pushback. Had been under impression that "more complex sigils do more things." Corrected: more complex sigils do one thing with more precision and more variable control. They do not do multiple things simultaneously.

**Revised approach:** Two Square inscriptions on the same workshop stone — one for thermal, one for photonic.

**Cost estimate, thermal (Warmstone-class application):**
- Square base, Heat discipline, Sustained persistence for continuous output
- Client wants this to run unattended. Sustained requires active Flux input. Unattended sustained operation is not what Sustained persistence means.
- Revised: Timed (Long) gives up to one hour per activation. Permanent gives indefinite hold but no controllability — the object stays warm forever at a fixed level, cannot be adjusted or turned off.
- Client preference after explanation: Permanent thermal at low level (ambient warmth, not working heat). This is achievable at T2 and within my capacity.

**Cost estimate, photonic (Glowmark-class application):**
- Triangle base, Light discipline, Permanent persistence for indefinite glow.
- T1 work. Straightforward.

**Combined inscription viability on single object:** Yes. Two separate inscriptions on the same surface. The thermal runs on the stone's underside. The photonic runs on the top face. The two disciplines do not interact through the stone — they are separate inscriptions with separate Flux channels. The object does two things because it has two inscriptions, not because any single inscription does two things.

---

## Configuration Attempt 2 — Execution and Failure

**Test piece: thermal inscription, underside.**

Applied the Permanent thermal inscription. Tested under standard conditions. Thermal output confirmed at target level — consistent ambient warmth across the stone surface.

**Test piece: photonic inscription, top face.**

Here is where it failed.

The photonic inscription on the top face produced a faint glow, but the glow output was inconsistent — pulsing at irregular intervals rather than holding steady. My initial reading was that the Light discipline inscription had a sigil error. Reinspected the inscription under good light. No visible line breaks, no spacing errors, no geometry problems.

Extended testing: the pulsing corresponded to the thermal output pattern on the underside. The Heat discipline's Flux channel on the underside was introducing interference into the Light discipline's Flux channel on the top face. The two channels were treating each other as environmental Flux — the thermal output was raising the ambient Flux level around the stone, and the photonic inscription was reading that as signal noise.

This is a known interaction pattern. I had not anticipated it at this scale because the thermal output here is low — ambient warmth, not working heat. The interference threshold is apparently lower than my working model had suggested.

**Assessment:** The two-inscription approach requires either physical separation of the inscriptions (different objects) or sufficient distance on a single large object. The standard workshop stone I was using is too small. The interference radius at this thermal output level is approximately 15cm.

---

## Configuration Attempt 3 — Revised Two-Object Solution

**Revised approach:** Two separate objects. Thermal embedded in a larger hearth stone (sufficient mass to maintain thermal output without interference concerns). Photonic embedded in a separate ceiling fixture.

This is a more expensive installation than the client originally wanted. Client accepted after explanation. The practical result — a workshop that is warm and lit without requiring a practitioner's ongoing attention — is what they were asking for, regardless of whether it is one object or two.

**Execution:**

Thermal hearth stone (30cm × 20cm base):
- Square inscription, Heat discipline, Permanent persistence
- Thermal output calibrated to ambient warmth at 2m radius
- Tested over four days. Output consistent. No interference observed.
- Client can turn off by covering the inscription with the fitted cap (included). Breaking the visual continuity of the sigil interrupts the channel. This is the standard off-mechanism for Permanent embedded objects.

Photonic ceiling fixture (standard bracket design):
- Triangle inscription, Light discipline, Permanent persistence
- Photonic output: steady ambient glow, consistent with client's specification
- Off-mechanism: same cap approach

**Combined installation test:** Both objects operating simultaneously in the same space. No interference. The hearth stone and the ceiling fixture are at sufficient distance. Thermal Flux from the hearth stone does not reach the ceiling fixture's inscription at intensity sufficient to produce interference.

**Result:** Client installation complete. Both objects performing to specification. Thermal output steady at 72-hour check and 120-hour check. Photonic output steady at same checks.

---

## Notes for Future Reference

The interference threshold between simultaneous Heat and Light discipline inscriptions on a single small surface is lower than my prior experience suggested. Add to testing protocol: for any configuration involving two disciplines on the same object, test for inter-channel interference before client delivery, regardless of prior success with similar configurations.

The practical lesson here is familiar: a configuration that works on the bench at standard conditions may behave differently when additional variables are introduced. In this case, the additional variable was the interaction between two Flux channels on the same physical object. My failure model did not adequately account for this at low thermal output levels.

Updated failure taxonomy: Error type — inter-channel interference at sub-threshold input levels. This is a new entry.

*See also: [[Ossal Meln]], [[Valdenmoor]], [[Sigils]], [[Flux]], [[Common Grimoire]], [[Control Tier]], [[Trade Guilds]]*
