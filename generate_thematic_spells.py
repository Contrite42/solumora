#!/usr/bin/env python3
"""
Create thematic Mythic and Pale spell entries using worldbuilding narrative.
These are high-tier, reality-affecting spells for Conduit-level casters.
"""

import json
from pathlib import Path

MYTHIC_SPELLS = [
    {
        "name": "Hierarchy Collapse",
        "summary": "Permanently severs the Flux-structural dominance of one individual over another.",
        "effect": (
            "The caster inscribes a sigil connecting two individuals through their Flux signatures. "
            "Upon activation, the target's Flux ceiling is permanently reduced to match or become subordinate to the reference individual. "
            "The effect is irreversible and affects only Control Tier capacity, not raw casting ability. "
            "Historical use suggests this spell was primary enforcement mechanism in early Council disputes."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Affect",
        "discipline": "Mind", "output": "Neuro", "pattern": "Point",
        "reach": "Linked", "persistence": "Permanent", "target": "Individual",
        "notes": "Rewrite spell - changes fundamental Flux relationship between two people"
    },
    {
        "name": "Covenant Burn",
        "summary": "Permanently terminates institutional power structures by dissolving the binding sigils that hold them.",
        "effect": (
            "Affects a defined institutional sigil network — trade guilds, Council holdings, or Kingdom administrative marks. "
            "Upon casting, ALL binding sigils anchored to that institution cease functioning simultaneously. "
            "The institution itself does not disappear, but loses all Flux-backed authority and protection. "
            "Effects are permanent. No counter-ritual exists in recorded history."
        ),
        "shape": "Circle", "hook": "Counter", "mode": "Control",
        "discipline": "Soul", "output": "Soul", "pattern": "Field",
        "reach": "Line-of-Sight", "persistence": "Permanent", "target": "Group",
        "notes": "Targets institutional bonds, not individuals"
    },
    {
        "name": "Threshold Breaking",
        "summary": "Forcibly elevates one individual's Flux ceiling by up to two Control Tiers.",
        "effect": (
            "Involves prolonged channeling (minimum 30 minutes) and a permanent Conduit-to-target link. "
            "The target gains access to higher Control Tier spells but faces permanent physiological stress. "
            "Known side effects: cascading nerve damage, Flux bleed-through, shortened lifespan. "
            "Ethical use is strongly disputed."
        ),
        "shape": "Circle", "hook": "Amplify", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Elevation spell with severe consequences"
    },
    {
        "name": "Memory Fortress",
        "summary": "Locks memories behind a Conduit-only barrier, making them inaccessible to all forms of Flux-based recall.",
        "effect": (
            "Seals specific memories in the target using nested Soul-frequency encryption. "
            "No other spellcaster can access, read, or influence sealed memories. "
            "Only the original Conduit who cast it, or another Conduit with explicit permission sigil, can unseal. "
            "Used extensively by scholars to protect classified knowledge."
        ),
        "shape": "Circle", "hook": "Ward", "mode": "Control",
        "discipline": "Mind", "output": "Neuro", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Information security spell"
    },
    {
        "name": "Bloodline Echo",
        "summary": "Imprints a genetic Flux signature that passes to all descendants of the target.",
        "effect": (
            "Creates a permanent hereditary Flux marker visible only to Conduits. "
            "Can be used to track bloodlines, identify distant relatives, or mark criminal lineages. "
            "Effect persists for a minimum of 7 generations. Some scholars believe the mark is truly permanent on the family strand."
        ),
        "shape": "Circle", "hook": "Bind", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Hereditary marking spell"
    },
    {
        "name": "Cascade Unweave",
        "summary": "Unravels a complex spell network by attacking its foundational sigil.",
        "effect": (
            "Requires knowledge of the target spell's base sigil structure. "
            "Upon casting, the entire spell network collapses in a Flux shockwave. "
            "All secondary effects terminate simultaneously. "
            "Counter-spells cannot prevent the unweaving if the base sigil is compromised."
        ),
        "shape": "Circle", "hook": "Counter", "mode": "Affect",
        "discipline": "Raw", "output": "Raw", "pattern": "Beam",
        "reach": "Line-of-Sight", "persistence": "Immediate", "target": "Where Written",
        "notes": "Anti-spell weapon for Conduits"
    },
    {
        "name": "Identity Anchor",
        "summary": "Locks an individual's consciousness into a defined state, preventing all Flux-based mental alteration.",
        "effect": (
            "Protects the target's mind from Mindread, Memory alteration, and personality rewriting. "
            "The anchor itself acts as a barrier that even Conduit-level spells cannot bypass. "
            "Requires the target's consent to cast. Cannot be removed by any known method."
        ),
        "shape": "Circle", "hook": "Ward", "mode": "Create",
        "discipline": "Mind", "output": "Neuro", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Defensive mental protection"
    },
    {
        "name": "Conduit Severance",
        "summary": "Permanently breaks a Conduit's connection to the Flux.",
        "effect": (
            "One of the most controversial spells. Terminates the target's Flux sensitivity entirely. "
            "The victim retains no ability to channel, sense, or interact with Flux. "
            "Functionally equivalent to declaring someone non-magical for life. "
            "Used only as ultimate punishment. Ethical debate continues over whether this violates Flux law itself."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Affect",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Long", "persistence": "Permanent", "target": "Individual",
        "notes": "Ultimate magical punishment"
    },
    {
        "name": "Epoch Seal",
        "summary": "Marks a historical moment or artifacts with a Conduit signature that identifies the era of creation.",
        "effect": (
            "Embeds temporal and identity metadata into objects or locations. "
            "Scholars use this to authenticate ancient artifacts and verify historical claims. "
            "The seal cannot be forged or removed without destroying the sealed object."
        ),
        "shape": "Circle", "hook": "Bind", "mode": "Create",
        "discipline": "Raw", "output": "Raw", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Object",
        "notes": "Scholarly authentication and archival spell"
    },
    {
        "name": "Faction Anchor",
        "summary": "Binds a faction, order, or group identity into Flux-structural reality.",
        "effect": (
            "Creates a permanent group identity marker that persists even if individual members change. "
            "Allows Conduits to locate any member of the faction across any distance. "
            "Requires consensus binding ritual from founding members."
        ),
        "shape": "Circle", "hook": "Bind", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Sphere",
        "reach": "Linked", "persistence": "Permanent", "target": "Group",
        "notes": "Institutional binding spell"
    },
    {
        "name": "Deathless Vigil",
        "summary": "Suspends death indefinitely by maintaining biological function through Flux channeling.",
        "effect": (
            "Keeps a dying individual alive by replacing their natural life force with direct Flux input. "
            "Requires continuous Conduit attention or an inscribed perpetual generator. "
            "The preserved individual exists in a suspended state — not truly alive, not dead. "
            "Long-term psychological effects are unknown."
        ),
        "shape": "Circle", "hook": "Trigger", "mode": "Control",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Life preservation through Flux replacement"
    },
    {
        "name": "Conspiracy Veil",
        "summary": "Hides the details of an agreement or pact from all non-signatories.",
        "effect": (
            "Creates a Flux barrier around information known to signatories. "
            "Non-signatories cannot perceive, remember, or act upon the hidden details. "
            "Attempts to extract the information produce only confusion in the inquirer's mind."
        ),
        "shape": "Circle", "hook": "Filter", "mode": "Create",
        "discipline": "Mind", "output": "Neuro", "pattern": "Field",
        "reach": "Linked", "persistence": "Permanent", "target": "Group",
        "notes": "Information hiding spell for pacts and secrets"
    },
    {
        "name": "Kingmaker's Mark",
        "summary": "Certifies an individual as having legitimate claim to rule through permanent Flux authentication.",
        "effect": (
            "Applied by established Conduits to legitimize political succession. "
            "The mark is visible to all Conduits and functions as unbreakable proof of ordained authority. "
            "Historical records suggest kingdoms without this mark face Flux-based challenges from neighboring powers."
        ),
        "shape": "Circle", "hook": "Emit", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Political legitimacy certification"
    },
    {
        "name": "Wound Binding",
        "summary": "Permanently seals a grievous wound using Flux to replace severed flesh.",
        "effect": (
            "Halts bleeding and infection by coating the wound interior with solidified Flux energy. "
            "Does not restore lost limbs but prevents death from injury. "
            "The 'sealed' area remains sensitive and can be re-opened by focused Flux pressure."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Affect",
        "discipline": "Heat", "output": "Thermal", "pattern": "Cone",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Emergency medical spell for Conduits"
    },
    {
        "name": "Lineage Theft",
        "summary": "Transfers knowledge, memories, or skills directly from one mind to another.",
        "effect": (
            "Extracts specific knowledge from target and imprints it into the caster's mind. "
            "Target retains the knowledge but cannot prevent the transfer if the Conduit is stronger. "
            "Extremely invasive and often used in espionage or succession disputes."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Affect",
        "discipline": "Mind", "output": "Neuro", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Aggressive knowledge transfer spell"
    },
    {
        "name": "Resonance Plague",
        "summary": "Imprints a Flux frequency into an area that causes dissonance in all casters within it.",
        "effect": (
            "Creates a permanent Flux distortion. Any spellcaster attempting to cast within the affected zone loses control. "
            "Spells misfire, unravel, or produce chaotic results. "
            "The plague persists for years and can only be cleansed by another Conduit using specialized counter-ritual."
        ),
        "shape": "Circle", "hook": "Emit", "mode": "Affect",
        "discipline": "Electric", "output": "Shock", "pattern": "Field",
        "reach": "Line-of-Sight", "persistence": "Permanent", "target": "Surface",
        "notes": "Area denial spell"
    },
    {
        "name": "Conduit's Ascension",
        "summary": "Permanently elevates a talented spellcaster into Conduit status.",
        "effect": (
            "Grants full Conduit access to a non-Conduit. "
            "Requires voluntary participation and intact bloodline Flux potential. "
            "The ceremony is irreversible. New Conduits experience months of adjustment and psychological strain."
        ),
        "shape": "Circle", "hook": "Amplify", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "notes": "Conduit elevation ritual"
    },
    {
        "name": "Archival Weaving",
        "summary": "Encodes entire libraries into a single Flux-inscribed artifact.",
        "effect": (
            "Translates written or verbal knowledge into compressed Flux form stored in a durable matrix. "
            "Knowledge can be extracted and read by any spellcaster. "
            "Single artifact can contain the equivalent of thousands of books."
        ),
        "shape": "Circle", "hook": "Bind", "mode": "Create",
        "discipline": "Raw", "output": "Raw", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Object",
        "notes": "Information storage and transmission spell"
    },
    {
        "name": "Verdict Absolute",
        "summary": "Imposes a binding judgment that cannot be appealed or circumvented.",
        "effect": (
            "A Conduit can declare a judgment of justice that becomes Flux-inscribed law. "
            "Anyone subject to the judgment finds themselves unable to violate its terms through any means. "
            "The judgment persists even across death (affecting reincarnated individuals in some theories)."
        ),
        "shape": "Circle", "hook": "Counter", "mode": "Control",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Medium", "persistence": "Permanent", "target": "Individual",
        "notes": "Cosmic law enforcement spell"
    },
    {
        "name": "Inheritance Lock",
        "summary": "Ensures that power, property, or knowledge passes to a designated heir according to specific conditions.",
        "effect": (
            "Creates an unbreakable contractual link through Flux. "
            "Upon the caster's death, the specified inheritance automatically transfers to the chosen heir. "
            "The heir cannot reject or refuse the inheritance."
        ),
        "shape": "Circle", "hook": "Bind", "mode": "Create",
        "discipline": "Raw", "output": "Raw", "pattern": "Point",
        "reach": "Linked", "persistence": "Permanent", "target": "Individual",
        "notes": "Succession and legacy spell"
    }
]

PALE_SPELLS = [
    {
        "name": "Void Genesis",
        "summary": "Creates a permanent void in Flux density that cannot be repaired.",
        "effect": (
            "The caster designates an area and severs all Flux connection to it. "
            "Nothing that depends on Flux can function or live in the affected zone. "
            "The void persists indefinitely. Scholars have discovered only three documented instances in recorded history. "
            "The casting site itself is left scarred — Flux refuses to flow there anymore."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Affect",
        "discipline": "Raw", "output": "Raw", "pattern": "Field",
        "reach": "Long", "persistence": "Permanent", "target": "Surface",
        "residue": "Casting site becomes permanently sterile — no Flux activity possible"
    },
    {
        "name": "Identity Erasure",
        "summary": "Removes an individual from all records, memories, and Flux signatures simultaneously.",
        "effect": (
            "The target ceases to exist in any meaningful way. Their name, image, and existence vanish from living memory. "
            "Witnesses of the spell forget the target's face immediately. "
            "Historical documents spontaneously rewrite themselves to exclude the target. "
            "The effect may be permanent or may wear off after 7-10 years (accounts vary). "
            "A caster who uses this spell leaves a mark on local Flux that attracts unwanted attention."
        ),
        "shape": "Circle", "hook": "Counter", "mode": "Control",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Long", "persistence": "Permanent", "target": "Individual",
        "residue": "Distortion in local timeline — Flux timestamps become unreliable"
    },
    {
        "name": "Famine Inscription",
        "summary": "Permanently prevents any life-sustaining Flux from functioning in an area.",
        "effect": (
            "Severs all biological processes dependent on Flux. "
            "Plants wilt unable to photosynthesize. Animals collapse. Humans in the zone experience starvation within hours. "
            "The effect persists for years or decades. Only another Pale-tier ritual can reverse it."
        ),
        "shape": "Circle", "hook": "Dampen", "mode": "Affect",
        "discipline": "Chemical", "output": "Reactive", "pattern": "Field",
        "reach": "Line-of-Sight", "persistence": "Permanent", "target": "Surface",
        "residue": "Dead zone — all life-Flux permanently weakened in surrounding regions"
    },
    {
        "name": "Obsidian Sky",
        "summary": "Blocks sunlight from reaching an area indefinitely.",
        "effect": (
            "The caster inscribes a sigil that warps atmospheric Flux to refract and absorb light. "
            "The area remains in perpetual darkness even during day. "
            "Only visible to those sensitive to Flux warping. "
            "The spell consumes vast amounts of ambient energy and may slowly drain the local area's Flux density."
        ),
        "shape": "Circle", "hook": "Filter", "mode": "Create",
        "discipline": "Light", "output": "Photonic", "pattern": "Field",
        "reach": "Line-of-Sight", "persistence": "Permanent", "target": "Surface",
        "residue": "Light-bending distortion persists for years; affected area becomes a dead zone for photonic spells"
    },
    {
        "name": "Shattered Will",
        "summary": "Fragments a person's consciousness into independent, competing voices.",
        "effect": (
            "The target's mind splinters into multiple personalities that may oppose or ignore each other. "
            "The effect may be reversible but the victim becomes functionally broken. "
            "Some fragments may be hostile to others. "
            "The fragmentation leaves permanent scars in the Flux architecture of the mind; healing is incomplete."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Affect",
        "discipline": "Mind", "output": "Neuro", "pattern": "Point",
        "reach": "Long", "persistence": "Permanent", "target": "Individual",
        "residue": "Target's Flux signature becomes permanently chaotic — cannot be reliably read by other Conduits"
    },
    {
        "name": "Ancestral Severance",
        "summary": "Cuts all bloodline and family Flux connections permanently.",
        "effect": (
            "The target is magically disowned and severed from all hereditary Flux marks. "
            "Their bloodline becomes 'foreign' to their own family's Flux signatures. "
            "They can no longer inherit family magical properties or access family-locked spells. "
            "The casting site becomes permanently marked as the location of a family curse."
        ),
        "shape": "Circle", "hook": "Counter", "mode": "Affect",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "residue": "Family-Flux becomes destabilized for a generation; inherited spells misfire"
    },
    {
        "name": "Reality Knot",
        "summary": "Creates a permanent knot in Flux space that distorts causality.",
        "effect": (
            "The affected area becomes a zone of causality breakdown. "
            "Effect and cause may reverse. Time may loop locally. "
            "The knot persists indefinitely and may spread very slowly. "
            "Nothing enters the zone willingly twice."
        ),
        "shape": "Circle", "hook": "Emit", "mode": "Control",
        "discipline": "Raw", "output": "Raw", "pattern": "Field",
        "reach": "Short", "persistence": "Permanent", "target": "Surface",
        "residue": "Space itself becomes unstable; Flux pathways become unreliable for years after"
    },
    {
        "name": "Conduit Draining",
        "summary": "Slowly extracts a Conduit's accumulated Flux power over years.",
        "effect": (
            "A parasitic spell that feeds on the target's Flux reserves. "
            "The Conduit weakens imperceptibly, losing access to higher-tier spells gradually. "
            "Extremely difficult to detect. The caster gains the drained power. "
            "Can take years or decades to fully drain a Conduit."
        ),
        "shape": "Circle", "hook": "Move", "mode": "Affect",
        "discipline": "Soul", "output": "Soul", "pattern": "Beam",
        "reach": "Linked", "persistence": "Permanent", "target": "Individual",
        "residue": "Both caster and target become permanently linked; draining site remains Flux-scarred"
    },
    {
        "name": "Bloodcursed Land",
        "summary": "Marks a location so that anyone who causes violence there is cursed.",
        "effect": (
            "Any act of violence in the affected area causes the perpetrator a wasting curse. "
            "The curse spreads to their bloodline for three generations. "
            "Affected individuals become increasingly weak and susceptible to disease. "
            "The curse is nearly impossible to remove and serves as powerful deterrent against warfare."
        ),
        "shape": "Circle", "hook": "Ward", "mode": "Control",
        "discipline": "Soul", "output": "Soul", "pattern": "Field",
        "reach": "Long", "persistence": "Permanent", "target": "Surface",
        "residue": "Cursed ground becomes permanent scar; Flux refuses to flow cleanly for generations"
    },
    {
        "name": "Echoing Scream",
        "summary": "Traps a dying person's final moment and forces all nearby listeners to experience it eternally.",
        "effect": (
            "At the moment of death in the spell's zone, the victim's consciousness is captured. "
            "All nearby witnesses are cursed to relive that moment of death repeatedly in their memory. "
            "The experience is indistinguishable from reality. Victims may go mad. "
            "The effect persists for the victims' remaining lives unless a powerful ritual unbinds it."
        ),
        "shape": "Circle", "hook": "Bind", "mode": "Create",
        "discipline": "Mind", "output": "Neuro", "pattern": "Field",
        "reach": "Medium", "persistence": "Permanent", "target": "Group",
        "residue": "The location becomes psychically toxic; sensitive individuals avoid it naturally"
    },
    {
        "name": "Succession Venom",
        "summary": "Ensures that power cannot be safely transferred to the next generation.",
        "effect": (
            "Any heir who attempts to claim the caster's power or position becomes afflicted with a wasting disease. "
            "The only cure is to surrender all Flux ability or die attempting to resist. "
            "Effectively prevents succession indefinitely."
        ),
        "shape": "Circle", "hook": "Trigger", "mode": "Create",
        "discipline": "Chemical", "output": "Reactive", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "residue": "Bloodline becomes magically poisonous; family members inherit weakened Flux capacity"
    },
    {
        "name": "Cosmic Witness",
        "summary": "Embeds an event permanently into Flux itself so it can be recalled by any Conduit forever.",
        "effect": (
            "The caster marks a moment in time. The event becomes permanently readable in Flux by any Conduit. "
            "Cannot be forgotten or rewritten. "
            "The knowledge spreads slowly through Flux networks to all Conduits over time. "
            "Typically used to document genocide, betrayals, or historical atrocities."
        ),
        "shape": "Circle", "hook": "Emit", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Sphere",
        "reach": "Self", "persistence": "Permanent", "target": "Where Written",
        "residue": "Casting site becomes permanently attuned to Flux memory; others can read it there"
    },
    {
        "name": "Covenant Rebellion",
        "summary": "Creates a permanent Flux rebellion against any institutional authority.",
        "effect": (
            "Spells and sigils belonging to an institution become unpredictable and dangerous. "
            "Institutional magic frequently misfires or produces chaotic results. "
            "The institution's control over Flux weakens across a region. "
            "Takes years or decades to fully manifest."
        ),
        "shape": "Circle", "hook": "Counter", "mode": "Affect",
        "discipline": "Raw", "output": "Raw", "pattern": "Field",
        "reach": "Line-of-Sight", "persistence": "Permanent", "target": "Surface",
        "residue": "Institutional Flux signatures become permanently tainted; power structures weaken"
    },
    {
        "name": "Mindless Hunger",
        "summary": "Transforms a person into a being driven entirely by incomprehensible hunger.",
        "effect": (
            "The victim loses higher consciousness and becomes driven only by consuming Flux energy. "
            "They become dangerous to all around them, draining Flux from people and places. "
            "Cannot be reversed. The afflicted become immortal as long as they can feed."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Affect",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Long", "persistence": "Permanent", "target": "Individual",
        "residue": "Target becomes a permanent hazard to their environment; Flux around them weakens permanently"
    },
    {
        "name": "Foundational Crack",
        "summary": "Introduces a permanent flaw into the Flux bedrock itself.",
        "effect": (
            "Weakens the underlying Flux structure of reality in an area. "
            "All spellcasting becomes less reliable. Over generations, the area becomes uninhabitable. "
            "The only remedy is to completely rebuild the location's Flux from first principles (nearly impossible)."
        ),
        "shape": "Circle", "hook": "Dampen", "mode": "Control",
        "discipline": "Raw", "output": "Raw", "pattern": "Field",
        "reach": "Short", "persistence": "Permanent", "target": "Surface",
        "residue": "Fundamental reality in the zone becomes damaged; 'thin places' where Flux barely exists"
    },
    {
        "name": "Soulbound Debt",
        "summary": "Creates an unpayable magical debt that binds two souls together until death.",
        "effect": (
            "One person owes the other an unpayable debt written into their Flux. "
            "The debtor will be compelled to obey reasonable commands from the creditor. "
            "The debt transfers partially to bloodline members (1/10th per generation). "
            "Can only be fully resolved by death of the debtor."
        ),
        "shape": "Circle", "hook": "Bind", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Touch", "persistence": "Permanent", "target": "Individual",
        "residue": "Both parties' souls become permanently marked as connected; family lines remain magically entangled"
    },
    {
        "name": "Temporal Fracture",
        "summary": "Causes an area to experience multiple time rates simultaneously.",
        "effect": (
            "Part of the zone may age rapidly while another part remains frozen. "
            "Living things in the zone may experience contradictory aging. "
            "The effect is permanent and may spread slowly. "
            "The caster's connection to normal time is permanently altered; they may age unpredictably."
        ),
        "shape": "Circle", "hook": "Transform", "mode": "Control",
        "discipline": "Raw", "output": "Raw", "pattern": "Field",
        "reach": "Short", "persistence": "Permanent", "target": "Surface",
        "residue": "Space-time becomes unstable; visitors experience temporal dissonance for visits afterward"
    },
    {
        "name": "Apotheosis Threshold",
        "summary": "Marks a location where a being can transcend mortal form entirely.",
        "effect": (
            "Anyone who successfully completes the ascension ritual in this location ceases to be human. "
            "They become a being of pure Flux, immortal and alien. "
            "Very few have attempted it. Those who failed are trapped as semi-conscious Flux spirits. "
            "The site itself becomes sacred/cursed and resists ordinary habitation."
        ),
        "shape": "Circle", "hook": "Ward", "mode": "Create",
        "discipline": "Soul", "output": "Soul", "pattern": "Point",
        "reach": "Self", "persistence": "Permanent", "target": "Where Written",
        "residue": "Location becomes permanently 'thin' — boundaries between human and Flux breakdown"
    }
]

def create_spell_entries():
    """Generate markdown spell entries for Mythic and Pale grimoires."""
    
    mythic_entries = []
    for spell in MYTHIC_SPELLS:
        notes_line = f"\n_{spell.get('notes', '')}_\n" if spell.get('notes') else ""
        entry = f"""
**{spell['name']}**
{spell['summary']}
| Variable | Value |
|---|---|
| Shape | {spell['shape']} |
| Hook | {spell['hook']} |
| Mode | {spell['mode']} |
| Control Tier | T9 |
| Discipline | {spell['discipline']} |
| Output | {spell['output']} |
| Pattern | {spell['pattern']} |
| Reach | {spell['reach']} |
| Persistence | {spell['persistence']} |
| Target | {spell['target']} |
{notes_line}
{spell['effect']}
"""
        mythic_entries.append(entry)
    
    pale_entries = []
    for spell in PALE_SPELLS:
        notes_line = f"\n_{spell.get('notes', '')}_\n" if spell.get('notes') else ""
        residue_line = f"\n_Residue effect: {spell['residue']}_" if spell.get('residue') else ""
        entry = f"""
**{spell['name']}**
{spell['summary']}
| Variable | Value |
|---|---|
| Shape | {spell['shape']} |
| Hook | {spell['hook']} |
| Mode | {spell['mode']} |
| Control Tier | T9 |
| Discipline | {spell['discipline']} |
| Output | {spell['output']} |
| Pattern | {spell['pattern']} |
| Reach | {spell['reach']} |
| Persistence | {spell['persistence']} |
| Target | {spell['target']} |
{notes_line}
{spell['effect']}
{residue_line}
"""
        pale_entries.append(entry)
    
    return mythic_entries, pale_entries

if __name__ == "__main__":
    mythic, pale = create_spell_entries()
    
    # Write to files
    mythic_content = "\n---\n".join(mythic)
    pale_content = "\n---\n".join(pale)
    
    Path("mythic_spells_output.txt").write_text(mythic_content)
    Path("pale_spells_output.txt").write_text(pale_content)
    
    print(f"Generated {len(mythic)} Mythic spells")
    print(f"Generated {len(pale)} Pale spells")
    print("Output written to mythic_spells_output.txt and pale_spells_output.txt")
