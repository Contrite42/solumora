#!/usr/bin/env python3
"""
Solumora Sigil Calculator (Full System)
- Center: Hook + Mode + Control Tier (Tier 0–9)
- Shape controls which outer variables are explicitly specified:
  Triangle: Discipline, Output, Pattern (Reach/Target/Persistence default)
  Square:   + Target
  Pentagon: + Reach
  Circle:   + Persistence (full control surface)
- Defaults when omitted:
  Discipline RAW, Output RAW, Pattern PLANE, Reach SELF, Persistence IMMEDIATE, Target WRITTEN
"""

import tkinter as tk
from tkinter import ttk
import math

class SigilCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Solumora Sigil Calculator — Full System")
        self.root.geometry("1100x820")

        # ---------------------------
        # Shape (control surface)
        # ---------------------------
        # control_points = how many outer variables are explicit
        # complexity_cost_scale = exponential penalty for added control surface
        self.shapes = {
            "Triangle": {"control_points": 3, "scale": 1.0, "color": "#FFD700"},
            "Square":   {"control_points": 4, "scale": 1.6, "color": "#32CD32"},
            "Pentagon": {"control_points": 5, "scale": 2.7, "color": "#FF6347"},
            "Circle":   {"control_points": 6, "scale": 5.0, "color": "#9370DB"},
        }

        # ---------------------------
        # Center: Hook + Mode
        # ---------------------------
        # Hook is the "verb kernel" (behavior complexity)
        self.hooks = {
            "Emit":      {"mult": 1.0, "desc": "Release an effect into reality."},
            "Shape":     {"mult": 1.2, "desc": "Refine or stabilize an effect."},
            "Bind":      {"mult": 1.6, "desc": "Attach/lock behavior to a target or anchor."},
            "Ward":      {"mult": 2.0, "desc": "Standing boundary rule (barrier/zone)."},
            "Trigger":   {"mult": 1.8, "desc": "Wait for condition, then fire."},
            "Transform": {"mult": 1.7, "desc": "Change state of target (heat, harden, convert)."},
            "Move":      {"mult": 1.5, "desc": "Reposition/control motion."},
            "Sense":     {"mult": 1.8, "desc": "Detect/measure/locate."},
            "Filter":    {"mult": 1.6, "desc": "Gate/select/exclude targets or conditions."},
            "Amplify":   {"mult": 2.2, "desc": "Increase magnitude/efficiency within limits."},
            "Dampen":    {"mult": 1.9, "desc": "Suppress/neutralize/reduce effects."},
            "Counter":   {"mult": 2.6, "desc": "Interact with incoming spell signatures (hard)."},
        }

        # Mode is operating posture
        self.modes = {
            "Create":  {"mult": 1.15, "desc": "Bring effect into existence from Flux."},
            "Affect":  {"mult": 1.00, "desc": "Alter something that already exists."},
            "Control": {"mult": 1.35, "desc": "Continuously steer/maintain effect."},
        }

        # ---------------------------
        # Outer variables (with W cost + whether they demand extra control)
        # ---------------------------
        self.disciplines = {
            "RAW":   {"W": 0,   "name": "Raw"},
            "FORCE": {"W": 2,   "name": "Force"},
            "HEAT":  {"W": 3,   "name": "Heat"},
            "LIGHT": {"W": 4,   "name": "Light"},
            "SOUND": {"W": 5,   "name": "Sound"},
            "ELEC":  {"W": 8,   "name": "Electric"},
            "CHEM":  {"W": 10,  "name": "Chemical"},
            "MIND":  {"W": 40,  "name": "Mind"},
            "BIND":  {"W": 25,  "name": "Binding"},
            "SOUL":  {"W": 250, "name": "Soul"},
        }

        self.output_modes = {
            "RAW":        {"W": 0,   "name": "Raw"},
            "KINETIC":    {"W": 2,   "name": "Kinetic"},
            "THERMAL":    {"W": 5,   "name": "Thermal"},
            "PHOTONIC":   {"W": 8,   "name": "Photonic"},
            "SONIC":      {"W": 12,  "name": "Sonic"},
            "SHOCK":      {"W": 18,  "name": "Shock"},
            "REACTIVE":   {"W": 25,  "name": "Reactive"},
            "CONSTRAINT": {"W": 35,  "name": "Constraint"},
            "NEURO":      {"W": 50,  "name": "Neuro"},
            "SOUL":       {"W": 500, "name": "Soul"},
        }

        self.patterns = {
            "POINT":    {"W": 0,  "name": "Point"},
            "BEAM":     {"W": 5,  "name": "Beam"},
            "CONE":     {"W": 8,  "name": "Cone"},
            "CYLINDER": {"W": 15, "name": "Cylinder"},
            "SPHERE":   {"W": 25, "name": "Sphere"},
            "FIELD":    {"W": 30, "name": "Field"},
            "PLANE":    {"W": 40, "name": "Plane"},
            "RING":     {"W": 50, "name": "Ring"},
        }

        self.reaches = {
            "SELF":     {"W": 0,  "name": "Self"},
            "TOUCH":    {"W": 2,  "name": "Touch"},
            "SHORT":    {"W": 5,  "name": "Short (10ft)"},
            "MEDIUM":   {"W": 8,  "name": "Medium (50ft)"},
            "LONG":     {"W": 15, "name": "Long (200ft)"},
            "LOS":      {"W": 25, "name": "Line-of-sight"},
            "LINKED":   {"W": 60, "name": "Linked"},
            "ANCHORED": {"W": 80, "name": "Anchored"},
        }

        self.persistences = {
            "IMMEDIATE":    {"W": 0,   "name": "Immediate"},
            "TIMED_SHORT":  {"W": 8,   "name": "Timed (Short)"},
            "TIMED_LONG":   {"W": 25,  "name": "Timed (Long)"},
            "SUSTAINED":    {"W": 35,  "name": "Sustained"},
            "LATCHED":      {"W": 40,  "name": "Latched"},
            "CONDITIONAL":  {"W": 80,  "name": "Conditional"},
            "PERMANENT":    {"W": 400, "name": "Permanent"},
        }

        self.targets = {
            "WRITTEN":    {"W": 80,  "name": "Where written"},
            "SELF":       {"W": 0,   "name": "Self"},
            "INDIVIDUAL": {"W": 2,   "name": "Individual"},
            "OBJECT":     {"W": 5,   "name": "Object"},
            "SURFACE":    {"W": 8,   "name": "Surface"},
            "GROUP":      {"W": 35,  "name": "Group"},
            "MARKED":     {"W": 50,  "name": "Marked"},
            "FILTER":     {"W": 240, "name": "Filter"},
        }

        # Defaults when omitted
        self.defaults = {
            "Discipline": "RAW",
            "Output": "RAW",
            "Pattern": "PLANE",
            "Reach": "SELF",
            "Persistence": "IMMEDIATE",
            "Target": "WRITTEN",
        }

        # Shape -> which outer vars are explicit (Pattern is last to go)
        self.shape_outer = {
            "Triangle": ["Discipline", "Output", "Pattern"],
            "Square":   ["Discipline", "Output", "Pattern", "Target"],
            "Pentagon": ["Discipline", "Output", "Pattern", "Target", "Reach"],
            "Circle":   ["Discipline", "Output", "Pattern", "Target", "Reach", "Persistence"],
        }

        # Tier thresholds (W ranges)
        self.tiers = [
            {"tier": 0, "name": "T0: Null",        "min_W": 0,      "max_W": 10,      "daily": "∞",     "tagline": "A flicker — detects nothing, moves nothing, lasts nothing"},
            {"tier": 1, "name": "T1: Minimal",     "min_W": 11,     "max_W": 40,      "daily": "∞",     "tagline": "A candle — illuminates, warms, latches"},
            {"tier": 2, "name": "T2: Basic",       "min_W": 41,     "max_W": 130,     "daily": "~100",  "tagline": "A tool — seals, barriers, sustained effects"},
            {"tier": 3, "name": "T3: Practical",   "min_W": 131,    "max_W": 400,     "daily": "~30",   "tagline": "A weapon — tracking through walls, combat suppression"},
            {"tier": 4, "name": "T4: Serious",     "min_W": 401,    "max_W": 1300,    "daily": "~10",   "tagline": "A violation — surface thought reading, complete immobilization"},
            {"tier": 5, "name": "T5: Major",       "min_W": 1301,   "max_W": 4000,    "daily": "~3",    "tagline": "A marker — crowd-scale disruption, permanent inscription"},
            {"tier": 6, "name": "T6: Extreme",     "min_W": 4001,   "max_W": 13000,   "daily": "~1",    "tagline": "A power act — forced brands, peak structural effects"},
            {"tier": 7, "name": "T7: Critical",    "min_W": 13001,  "max_W": 40000,   "daily": "~1/3",  "tagline": "A rupture — deep identity erasure"},
            {"tier": 8, "name": "T8: Catastrophic","min_W": 40001,  "max_W": 130000,  "daily": "~1/10", "tagline": "A catastrophe — revival, local law rewrite"},
            {"tier": 9, "name": "T9: Absolute",    "min_W": 130001, "max_W": float('inf'), "daily": "~1/30", "tagline": "The architecture — interacts with Flux system itself"},
        ]

        self.setup_ui()

    # ---------------------------
    # UI
    # ---------------------------
    def setup_ui(self):
        main = ttk.Frame(self.root, padding="10")
        main.grid(row=0, column=0, sticky="nsew")

        left = ttk.LabelFrame(main, text="Sigil Configuration", padding="10")
        left.grid(row=0, column=0, sticky="nsw", padx=(0, 12))

        right = ttk.Frame(main)
        right.grid(row=0, column=1, sticky="nsew")

        self.vars = {}

        def add_row(label, key, values, default):
            r = len(self.vars)
            ttk.Label(left, text=label + ":").grid(row=r, column=0, sticky="w", pady=2)
            self.vars[key] = tk.StringVar(value=default)
            cb = ttk.Combobox(left, textvariable=self.vars[key], values=values, state="readonly", width=18)
            cb.grid(row=r, column=1, sticky="w", pady=2)
            self.vars[key].trace_add("write", lambda *_: self.calculate())
            return cb

        self.shape_cb = add_row("Shape", "Shape", list(self.shapes.keys()), "Triangle")
        self.hook_cb  = add_row("Hook", "Hook", list(self.hooks.keys()), "Emit")
        self.mode_cb  = add_row("Mode", "Mode", list(self.modes.keys()), "Affect")

        # Outer vars
        self.disc_cb = add_row("Discipline", "Discipline", list(self.disciplines.keys()), self.defaults["Discipline"])
        self.out_cb  = add_row("Output", "Output", list(self.output_modes.keys()), self.defaults["Output"])
        self.pat_cb  = add_row("Pattern", "Pattern", list(self.patterns.keys()), self.defaults["Pattern"])
        self.tgt_cb  = add_row("Target", "Target", list(self.targets.keys()), self.defaults["Target"])
        self.rch_cb  = add_row("Reach", "Reach", list(self.reaches.keys()), self.defaults["Reach"])
        self.per_cb  = add_row("Persistence", "Persistence", list(self.persistences.keys()), self.defaults["Persistence"])

        ttk.Separator(left).grid(row=99, column=0, columnspan=2, sticky="ew", pady=10)

        ttk.Button(left, text="Tier Overview", command=self.show_tier_overview).grid(row=100, column=0, columnspan=2, pady=6)

        # Visualization + results
        self.canvas = tk.Canvas(right, width=360, height=360, bg="black", highlightthickness=0)
        self.canvas.grid(row=0, column=0, pady=(0, 10), sticky="nw")

        self.results = tk.Text(right, width=60, height=26, font=("Courier", 10))
        self.results.grid(row=1, column=0, sticky="nsew")

        # grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(0, weight=1)
        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=1)

        # shape change triggers visible fields
        self.vars["Shape"].trace_add("write", lambda *_: self.apply_shape_visibility())

        self.apply_shape_visibility()
        self.calculate()

    def apply_shape_visibility(self):
        """Hide/show outer variable rows based on shape control surface."""
        shape = self.vars["Shape"].get()
        explicit = set(self.shape_outer[shape])

        # Always show D/O/P
        widgets = {
            "Discipline": self.disc_cb,
            "Output": self.out_cb,
            "Pattern": self.pat_cb,
            "Target": self.tgt_cb,
            "Reach": self.rch_cb,
            "Persistence": self.per_cb,
        }

        for k, cb in widgets.items():
            if k in explicit:
                cb.grid()
            else:
                cb.grid_remove()
                # reset omitted to defaults so user sees consistent behavior
                self.vars[k].set(self.defaults[k])

    # ---------------------------
    # Computation
    # ---------------------------
    def tier_from_W(self, W):
        for t in self.tiers:
            if t["min_W"] <= W <= t["max_W"]:
                return t
        return self.tiers[-1]

    def calculate(self):
        shape = self.vars["Shape"].get()
        hook = self.vars["Hook"].get()
        mode = self.vars["Mode"].get()

        explicit = self.shape_outer[shape]
        omitted = [v for v in ["Discipline","Output","Pattern","Target","Reach","Persistence"] if v not in explicit]

        # Resolve values (explicit chosen, omitted default)
        discipline = self.vars["Discipline"].get()
        output = self.vars["Output"].get()
        pattern = self.vars["Pattern"].get()
        target = self.vars["Target"].get()
        reach = self.vars["Reach"].get()
        persistence = self.vars["Persistence"].get()

        # W costs
        dW = self.disciplines[discipline]["W"]
        oW = self.output_modes[output]["W"]
        pW = self.patterns[pattern]["W"]
        tW = self.targets[target]["W"]
        rW = self.reaches[reach]["W"]
        sW = self.persistences[persistence]["W"]

        base_W = dW + oW + pW + tW + rW + sW

        # Shape scaling (control surface exponential cost)
        shape_scale = self.shapes[shape]["scale"]

        # Hook+Mode scaling
        hook_mult = self.hooks[hook]["mult"]
        mode_mult = self.modes[mode]["mult"]

        final_W = int(round(base_W * shape_scale * hook_mult * mode_mult))

        tier = self.tier_from_W(final_W)

        # Update drawing + results
        self.draw_sigil(shape, discipline)

        self.results.delete("1.0", tk.END)
        self.results.insert("1.0", self.render_results(
            shape, hook, mode,
            discipline, output, pattern, target, reach, persistence,
            base_W, shape_scale, hook_mult, mode_mult, final_W, tier,
            explicit, omitted
        ))

    def render_results(self, shape, hook, mode,
                       discipline, output, pattern, target, reach, persistence,
                       base_W, shape_scale, hook_mult, mode_mult, final_W, tier,
                       explicit, omitted):
        lines = []
        lines.append("SIGIL FORMULA (FULL SYSTEM)")
        lines.append("════════════════════════════════════════════════")
        lines.append("")
        lines.append(f"Shape: {shape}  (explicit vars: {len(explicit)}/6, scale ×{shape_scale})")
        lines.append(f"Center: Hook={hook} (×{hook_mult})  Mode={mode} (×{mode_mult})")
        lines.append("")
        lines.append("OUTER VARIABLES (resolved)")
        lines.append("────────────────────────────────────────────────")
        lines.append(f"Discipline:   {discipline:10}  +{self.disciplines[discipline]['W']}W" + ("  [explicit]" if "Discipline" in explicit else "  [default]"))
        lines.append(f"Output:       {output:10}  +{self.output_modes[output]['W']}W" + ("  [explicit]" if "Output" in explicit else "  [default]"))
        lines.append(f"Pattern:      {pattern:10}  +{self.patterns[pattern]['W']}W" + ("  [explicit]" if "Pattern" in explicit else "  [default]"))
        lines.append(f"Target:       {target:10}  +{self.targets[target]['W']}W" + ("  [explicit]" if "Target" in explicit else "  [default]"))
        lines.append(f"Reach:        {reach:10}  +{self.reaches[reach]['W']}W" + ("  [explicit]" if "Reach" in explicit else "  [default]"))
        lines.append(f"Persistence:  {persistence:10}  +{self.persistences[persistence]['W']}W" + ("  [explicit]" if "Persistence" in explicit else "  [default]"))
        lines.append("")
        lines.append(f"Base W (sum of outer costs): {base_W}W")
        lines.append(f"Scaled: base × shape × hook × mode")
        lines.append(f"FINAL COST: {final_W}W")
        lines.append("")
        lines.append("TIER RESULT")
        lines.append("────────────────────────────────────────────────")
        maxW = "∞" if tier["max_W"] == float('inf') else str(int(tier["max_W"]))
        lines.append(f"{tier['name']}  (range {tier['min_W']}–{maxW}W)")
        lines.append(tier["tagline"])
        lines.append("")
        lines.append("OMITTED VARIABLES (defaults applied)")
        lines.append("────────────────────────────────────────────────")
        if omitted:
            for v in omitted:
                lines.append(f"- {v}: default {self.defaults[v]}")
        else:
            lines.append("(none)")
        lines.append("")
        lines.append("NOTES")
        lines.append("────────────────────────────────────────────────")
        lines.append("- Pattern stays in low-control shapes; Persistence defaults to Immediate unless explicitly included.")
        lines.append("- If a caster cannot channel the required Flux, the spell misbehaves (misfires/backfires) rather than lashing out.")
        return "\n".join(lines)

    # ---------------------------
    # Drawing (simple + readable)
    # ---------------------------
    def draw_sigil(self, shape, discipline):
        self.canvas.delete("all")
        cx, cy = 180, 180
        col = "#e6e6e6"

        # discipline tint
        # (simple mapping)
        dcol = {
            "RAW":"#A0A0A0","FORCE":"#4169E1","HEAT":"#FF4500","LIGHT":"#FFD700","SOUND":"#00CED1",
            "ELEC":"#FF1493","CHEM":"#32CD32","MIND":"#9370DB","SOUL":"#DC143C","BIND":"#8B4513"
        }.get(discipline, col)

        if shape == "Triangle":
            pts = [(cx, cy-80), (cx-70, cy+40), (cx+70, cy+40)]
            self.canvas.create_polygon(pts, outline=dcol, fill="", width=3)
            for x,y in pts:
                self.canvas.create_line(x,y,cx,cy, fill=dcol, width=2)
            self.canvas.create_oval(cx-3,cy-3,cx+3,cy+3, fill=dcol, outline="")
        elif shape == "Square":
            s=80
            corners=[(cx-s,cy-s),(cx+s,cy-s),(cx+s,cy+s),(cx-s,cy+s)]
            self.canvas.create_polygon(corners, outline=dcol, fill="", width=3)
            self.canvas.create_line(corners[0][0],corners[0][1],corners[2][0],corners[2][1], fill=dcol, width=2)
            self.canvas.create_line(corners[1][0],corners[1][1],corners[3][0],corners[3][1], fill=dcol, width=2)
            inner=s//2
            ip=[(cx,cy-inner),(cx+inner,cy),(cx,cy+inner),(cx-inner,cy)]
            self.canvas.create_polygon(ip, outline=dcol, fill="", width=2)
        elif shape == "Pentagon":
            pts=[]
            for i in range(5):
                a = (2*math.pi*i/5) - (math.pi/2)
                pts.append((cx+85*math.cos(a), cy+85*math.sin(a)))
            self.canvas.create_polygon(pts, outline=dcol, fill="", width=3)
            for i in range(5):
                x1,y1=pts[i]; x2,y2=pts[(i+2)%5]
                self.canvas.create_line(x1,y1,x2,y2, fill=dcol, width=2)
        else:  # Circle
            R=95
            self.canvas.create_oval(cx-R,cy-R,cx+R,cy+R, outline=dcol, width=3)
            pts=[]
            for i in range(6):
                a=2*math.pi*i/6
                pts.append((cx+R*math.cos(a), cy+R*math.sin(a)))
            for i in range(6):
                for j in range(i+1,6):
                    self.canvas.create_line(pts[i][0],pts[i][1],pts[j][0],pts[j][1], fill=dcol, width=1)
            for x,y in pts:
                self.canvas.create_oval(x-3,y-3,x+3,y+3, fill=dcol, outline="")

    def show_tier_overview(self):
        win = tk.Toplevel(self.root)
        win.title("Tier Overview")
        win.geometry("850x620")
        frame = ttk.Frame(win, padding="10")
        frame.pack(fill="both", expand=True)

        txt = tk.Text(frame, font=("Courier", 10), wrap="word")
        sb = ttk.Scrollbar(frame, orient="vertical", command=txt.yview)
        txt.configure(yscrollcommand=sb.set)
        txt.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        out=[]
        out.append("SOLUMORA TIER SYSTEM OVERVIEW")
        out.append("════════════════════════════════════════════════════════")
        out.append("")
        for t in self.tiers:
            max_part = '∞' if t['max_W'] == float('inf') else f"{int(t['max_W']):,}"
            rng = f"{t['min_W']:,}–{max_part}W"
            out.append(f"{t['name']}")
            out.append(f"Range: {rng}")
            out.append(f"Daily: {t['daily']}")
            out.append(f"{t['tagline']}")
            out.append("-"*55)
        txt.insert("1.0", "\n".join(out))
        txt.config(state="disabled")

def main():
    app = SigilCalculator()
    app.root.mainloop()

if __name__ == "__main__":
    main()
