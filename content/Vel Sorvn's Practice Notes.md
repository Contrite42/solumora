Working practice notes maintained by [[Vel Sorvn]], [[Hypertext]] practitioner, [[Wolfpoint]]. Not formal research records — those are logged separately in the archive format. These are thinking on paper.

---

**On clause propagation errors**

A misplaced conditional in sequence position four does not fail at position four. It fails wherever the condition first becomes relevant — which might be position eleven, or might be position twenty, or might be during execution rather than during the write. This is the difference between sequence logic and sigil logic that nobody explains adequately before you write your first multi-conditional sequence and watch it execute correctly for three tests and then fail in a way you cannot immediately locate.

In a sigil, the error is in the shape. You can see it. The variable is in the wrong slot, the point is mis-drawn, the geometry has drifted. The failure is spatial and therefore locatable. In a sequence, the error is in the logic, and the logic only manifests as behavior. Finding the failure means reading back through the reasoning, not inspecting a drawing.

I have come to think of this as the difference between an error that exists in space and an error that exists in time.

---

**On the conditional threshold problem**

The nested IF structures that make Hypertext genuinely more expressive than sigils are also the structures most likely to produce behavior that surprises you. A conditional with a threshold value that is almost-but-not-quite what you intended will behave correctly in tests and incorrectly in the field when field conditions push the threshold value slightly across the boundary.

The fix is to build explicit range buffers into threshold values rather than using exact numbers. This is basic practice and I still occasionally skip it when I'm moving quickly through a development sequence, and I still occasionally produce surprises in exactly this way.

---

**On what sigils cannot express — a case study**

Last month I wrote a warming sequence for extended field use in cold conditions. The requirement: maintain heat output above threshold, reduce output when threshold is exceeded, detect and compensate for wind interference, and — this is the part that made sigils impractical — modify its own compensation behavior based on how long it had been running, because extended use in cold conditions changes the caster's Flux expenditure profile in ways that affect what the sequence needs to do to remain efficient.

A sigil warming effect cannot do this. A Circle sigil has six fixed variables. "Modify your own behavior based on elapsed time and caster state" is not a variable. It is logic that needs to read external conditions and write back to itself. The geometry of any current sigil shape has no mechanism for this.

The sequence I wrote does it. It is forty-one symbols, takes about four seconds to write, and has been tested in three Wolfpoint winter weeks. It works.

This is not a particularly complex sequence by the standards of the work happening at Wolfpoint now. It would have been considered remarkable five years ago. I write this down not to record the achievement but because I need to remember what it felt like to actually have the tool and not just the theory of the tool.

---

**On the gap between what the system can describe and what practitioners know**

The formal [[Hypertext]] research log tracks what sequences do. It does not track what it feels like to write a sequence that branches — the specific texture of holding two conditional threads simultaneously and maintaining coherent logic in both while the write is active.

This is a meaningful thing to know. It is not a thing the formal logs have a category for. The difference between a practitioner who can write conditional sequences fluently and one who cannot is partly about having internalized this dual-thread texture as a normal working state rather than a strenuous one. Teaching it formally has, in my observation, limited effectiveness. The people who develop it have usually practiced themselves into it rather than been instructed into it.

I don't know what to do with this observation except write it down here, where it will not be reviewed.

*See also: [[Vel Sorvn]], [[Wolfpoint]], [[Hypertext]], [[Flux Users]], [[Control Tier]]*
