#!/usr/bin/env python3
import os, re, json, time, hashlib, argparse, traceback
from pathlib import Path

import requests

# Watch mode is optional (script still runs without it)
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except Exception:
    WATCHDOG_AVAILABLE = False

# -----------------------------
# Paths
# -----------------------------
ROOT = Path(r"C:\Users\Contrite42\quartz")
CONTENT_DIR = ROOT / "content"
AGENT_DIR = ROOT / "agent"
REPORTS_DIR = AGENT_DIR / "reports"
STAGING_DIR = AGENT_DIR / "staging"

TASK_FILE = AGENT_DIR / "TASK.md"
WORLD_STATE = AGENT_DIR / "WORLD_STATE.md"
STYLE_GUIDE = AGENT_DIR / "STYLE_GUIDE.md"
QA_RULES = AGENT_DIR / "QA_RULES.md"
CLAIMED_FILE = AGENT_DIR / "claimed.md"
SECRETS_PATH = AGENT_DIR / "secrets.json"

PLAN_FILE = STAGING_DIR / "PLAN.json"
SEED_FILE = STAGING_DIR / "OLLAMA_SEED.md"
PATCH_FILE = STAGING_DIR / "PATCH.json"
CHANGELOG = STAGING_DIR / "CHANGELOG.json"
CONVO_LOG = STAGING_DIR / "conversation.log"

REPORT_LINKS = REPORTS_DIR / "links_applied.md"
REPORT_INCONSIST = REPORTS_DIR / "inconsistencies.md"
LAST_ERROR_TXT = REPORTS_DIR / "last_error.txt"
LAST_ERROR_JSON = REPORTS_DIR / "last_error.json"

# -----------------------------
# Models / knobs
# -----------------------------
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

CLAUDE_MAX_BATCH_NOTES = int(os.getenv("CLAUDE_MAX_BATCH_NOTES", "2"))
CLAUDE_SLEEP_SECONDS = float(os.getenv("CLAUDE_SLEEP_SECONDS", "8"))
MAX_CONTEXT_FILES = int(os.getenv("MAX_CONTEXT_FILES", "12"))

# -----------------------------
# Helpers
# -----------------------------
def ensure_dirs():
    for d in [AGENT_DIR, REPORTS_DIR, STAGING_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    if not CONTENT_DIR.exists():
        raise RuntimeError(f"CONTENT_DIR not found: {CONTENT_DIR}")

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""

def write_text(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def append_text(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    old = read_text(p)
    p.write_text(old + s, encoding="utf-8")

def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]

def now_tag():
    return time.strftime("%Y%m%d_%H%M%S")

def log_error(stage: str, err: Exception, extra: dict = None):
    t = traceback.format_exc()
    write_text(LAST_ERROR_TXT, f"[{stage}]\n{t}\n")
    payload = {
        "stage": stage,
        "time": time.time(),
        "error": str(err),
        "traceback": t,
        "extra": extra or {}
    }
    write_text(LAST_ERROR_JSON, json.dumps(payload, indent=2))
    print(f"\n❌ ERROR @ {stage}: {err}\n(see agent/reports/last_error.*)\n")

def log_convo(role: str, text: str, limit: int = 12000):
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    snippet = (text or "")[:limit]
    append_text(CONVO_LOG, f"\n\n[{stamp}] {role}\n{snippet}\n")

def load_secrets():
    if not SECRETS_PATH.exists():
        raise RuntimeError(f"Missing secrets.json: {SECRETS_PATH}")
    data = json.loads(SECRETS_PATH.read_text(encoding="utf-8"))
    for k, v in data.items():
        if v:
            os.environ[k] = str(v).strip()

def strip_code_fences(raw: str) -> str:
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return raw.strip()

def list_md_files():
    return list(CONTENT_DIR.rglob("*.md"))

def basic_retrieve(task: str, k: int = MAX_CONTEXT_FILES):
    files = list_md_files()
    terms = [t.lower() for t in re.findall(r"[A-Za-z]{3,}", task)]
    if not terms:
        return []
    scored = []
    for f in files:
        txt = read_text(f)
        blob = (f.stem + "\n" + txt[:6500]).lower()
        score = 0
        for t in terms[:50]:
            if t in blob:
                score += 1
        if score > 0:
            scored.append((score, f))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [f for _, f in scored[:k]]

def pack_context(task: str):
    canon = read_text(WORLD_STATE)[:20000]
    style = read_text(STYLE_GUIDE)[:16000]
    qa = read_text(QA_RULES)[:12000]
    claimed = read_text(CLAIMED_FILE)[:12000] if CLAIMED_FILE.exists() else ""

    ctx_files = basic_retrieve(task)
    ctx_blobs = []
    for f in ctx_files:
        rel = str(f.relative_to(ROOT))
        txt = read_text(f)[:14000]
        ctx_blobs.append(f"\n--- FILE: {rel} ---\n{txt}\n")

    bundle = ("\n".join(ctx_blobs))[:180000]
    return {"canon": canon, "style": style, "qa": qa, "claimed": claimed, "files": ctx_files, "bundle": bundle}

# -----------------------------
# HTTP retry/backoff
# -----------------------------
def http_post_with_retry(url, headers, payload, timeout, label, max_attempts=6):
    for attempt in range(1, max_attempts + 1):
        r = requests.post(url, headers=headers, json=payload, timeout=timeout)
        if r.status_code == 200:
            return r
        if r.status_code in (429, 500, 502, 503, 504, 529):
            wait = min(60, 2 ** attempt)
            msg = r.text[:400]
            print(f"[retry:{label}] status={r.status_code} attempt={attempt}/{max_attempts} wait={wait}s msg={msg}")
            time.sleep(wait)
            continue
        raise RuntimeError(f"{label} hard failure {r.status_code}: {r.text[:2000]}")
    raise RuntimeError(f"{label} failed after retries (rate limit/transient).")

# -----------------------------
# Model Calls
# -----------------------------
def call_openai(system: str, user: str) -> str:
    key = (os.getenv("OPENAI_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY missing.")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {
        "model": OPENAI_MODEL,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.2,
    }
    log_convo("GPT_INPUT", user)
    r = http_post_with_retry(url, headers, payload, timeout=180, label="openai")
    out = r.json()["choices"][0]["message"]["content"]
    log_convo("GPT_OUTPUT", out)
    return out

def call_claude(system: str, user: str, max_tokens: int = 3500, temperature: float = 0.35) -> str:
    key = (os.getenv("ANTHROPIC_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY missing.")

    # print once
    if not getattr(call_claude, "_printed", False):
        print("Anthropic key prefix:", key[:12])
        call_claude._printed = True

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    payload = {
        "model": CLAUDE_MODEL,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
        "temperature": temperature,
    }

    log_convo("CLAUDE_INPUT", user)
    r = http_post_with_retry(url, headers, payload, timeout=240, label="anthropic")
    data = r.json()
    blocks = data.get("content", [])
    out = []
    for b in blocks:
        if b.get("type") == "text":
            out.append(b.get("text", ""))
    text = "\n".join(out).strip()
    log_convo("CLAUDE_OUTPUT", text)
    return text

def call_ollama(prompt: str) -> str:
    url = f"{OLLAMA_URL}/api/generate"
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    log_convo("OLLAMA_INPUT", prompt, limit=4000)
    r = requests.post(url, json=payload, timeout=240)
    if r.status_code != 200:
        raise RuntimeError(f"ollama failure {r.status_code}: {r.text[:800]}")
    out = (r.json().get("response", "") or "").strip()
    log_convo("OLLAMA_OUTPUT", out, limit=6000)
    return out

# -----------------------------
# Patch Apply (safe)
# -----------------------------
def apply_patch(patch: dict):
    writes = patch.get("writes", [])
    appends = patch.get("appends", [])
    changed = []

    for w in writes:
        p = ROOT / w["path"]
        write_text(p, w["content"])
        changed.append(str(p.relative_to(ROOT)))

    for a in appends:
        p = ROOT / a["path"]
        old = read_text(p)
        new = old.rstrip() + "\n\n" + a["append"].strip() + "\n"
        write_text(p, new)
        changed.append(str(p.relative_to(ROOT)))

    return sorted(set(changed))

# -----------------------------
# Plan step (Claude JSON only, small)
# -----------------------------
def step_plan_claude(task: str, ctx: dict, seed: str) -> dict:
    schema_hint = f"""{{
  "notes": [
    {{
      "path": "content/Folder/Note.md",
      "action": "create|append",
      "purpose": "1 sentence",
      "links": ["[[A]]","[[B]]","[[C]]"]
    }}
  ],
  "batches": [ [0,1], [2,3] ]
}}"""

    system = """
You are the Solumora Builder.
You are PLANNING files only. Do not write note bodies yet.
Return ONLY JSON matching the schema. No markdown.
""".strip()

    user = f"""
TASK:
{task}

WORLD_STATE:
{ctx['canon']}

STYLE_GUIDE:
{ctx['style']}

SEED (optional):
{seed}

CONTEXT NOTES (partial):
{ctx['bundle']}

CLAIMED (files that already exist — do NOT include unless TASK explicitly targets for append):
{ctx['claimed']}

Return JSON exactly in this schema:
{schema_hint}

Constraints:
- Plan ONLY the files explicitly specified in TASK.md. Do not invent additional notes.
- Do NOT include any file listed in CLAIMED unless TASK.md explicitly targets it for append.
- Each note includes at least 3 outbound links.
- Batches must be <= {CLAUDE_MAX_BATCH_NOTES} notes.
""".strip()

    raw = call_claude(system, user, max_tokens=2200, temperature=0.2)
    raw = strip_code_fences(raw)

    # attempt parse; if malformed, ask Claude to repair
    try:
        plan = json.loads(raw)
    except Exception:
        repair_system = "You repair malformed JSON. Return ONLY valid JSON. No markdown."
        repair_user = f"""
Repair into VALID JSON matching this schema exactly.

SCHEMA:
{schema_hint}

MALFORMED:
{raw}
""".strip()
        fixed = call_claude(repair_system, repair_user, max_tokens=2200, temperature=0.0)
        fixed = strip_code_fences(fixed)
        plan = json.loads(fixed)

    write_text(PLAN_FILE, json.dumps(plan, indent=2))
    return plan

# -----------------------------
# File-block protocol parser (Claude batch output)
# -----------------------------
def parse_file_blocks(raw: str) -> dict:
    """
    Parse Claude output:

    ===WRITE: content/path.md===
    <markdown>
    ===END===

    ===APPEND: content/path.md===
    <markdown>
    ===END===

    Returns patch dict.
    """
    raw = raw.replace("\r\n", "\n")
    lines = raw.split("\n")

    patch = {"writes": [], "appends": []}
    mode = None
    path = None
    buf = []

    def flush():
        nonlocal mode, path, buf
        if mode and path:
            content = "\n".join(buf).strip("\n")
            if content.strip():
                if mode == "WRITE":
                    patch["writes"].append({"path": path, "content": content})
                elif mode == "APPEND":
                    patch["appends"].append({"path": path, "append": content})
        mode = None
        path = None
        buf = []

    header_re = re.compile(r"^===\s*(WRITE|APPEND)\s*:\s*([^\=]+)\s*===\s*$")
    end_re = re.compile(r"^===\s*END\s*===\s*$")

    for line in lines:
        m = header_re.match(line.strip())
        if m:
            flush()
            mode = m.group(1).strip().upper()
            path = m.group(2).strip()
            continue
        if end_re.match(line.strip()):
            flush()
            continue
        if mode:
            buf.append(line)

    flush()

    if not patch["writes"] and not patch["appends"]:
        write_text(STAGING_DIR / f"fileblock_parse_fail_{now_tag()}.txt", raw)
        raise RuntimeError("No WRITE/APPEND blocks found. Saved raw to agent/staging/fileblock_parse_fail_*.txt")

    return patch

# -----------------------------
# Batch write step (Claude file blocks)
# -----------------------------
def step_build_batch_claude(task: str, ctx: dict, seed: str, plan: dict, batch_idxs: list) -> dict:
    notes = plan["notes"]
    batch = [notes[i] for i in batch_idxs]

    system = """
You are the Solumora Builder.
Write Obsidian Markdown. Everyone is mid-journey. Dense detail. No fluff.

OUTPUT FORMAT (MANDATORY):
Use ONLY these block types, exactly:

===WRITE: content/path.md===
<full markdown file content>
===END===

===APPEND: content/path.md===
<markdown to append>
===END===

Rules:
- No JSON.
- No code fences.
- No commentary outside blocks.
- Every created note must include at least 3 outbound [[links]].
""".strip()

    user = f"""
TASK:
{task}

WORLD_STATE:
{ctx['canon']}

STYLE_GUIDE:
{ctx['style']}

SEED:
{seed}

CONTEXT (partial):
{ctx['bundle']}

BATCH TO WRITE:
{json.dumps(batch, indent=2)}

Mapping rules:
- If action=create -> output a WRITE block with the full file.
- If action=append -> output an APPEND block with only the new section.
""".strip()

    raw = call_claude(system, user, max_tokens=4200, temperature=0.45)

    # Save raw batch output for debugging
    write_text(STAGING_DIR / f"batch_fileblocks_{now_tag()}.txt", raw)

    return parse_file_blocks(raw)

# -----------------------------
# GPT QA + conservative linking
# -----------------------------
def step_gpt_qa_and_link(ctx: dict, changed_files: list):
    titles = sorted({p.stem for p in CONTENT_DIR.rglob("*.md")})
    title_set = set(titles)

    blobs = []
    for rel in changed_files[:40]:
        p = ROOT / rel
        txt = read_text(p)
        blobs.append(f"\n--- FILE: {rel} ---\n{txt[:12000]}\n")

    system = """
You are the Solumora QA + Linker.
Return JSON only:
{
 "inconsistencies":[{"file":"...","issue":"...","evidence":"..."}],
 "link_suggestions":[{"file":"...","title":"ExactExistingTitle"}]
}
Rules:
- Conservative: suggest only exact existing titles.
- Prefer fewer high-confidence suggestions.
""".strip()

    user = f"""
WORLD_STATE:
{ctx.get('canon','')}

CHANGED FILES:
{''.join(blobs)}

KNOWN TITLES (exact):
{', '.join(titles[:900])}
""".strip()

    try:
        out = call_openai(system, user)
        out = strip_code_fences(out)
        rep = json.loads(out)
    except Exception as e:
        write_text(REPORTS_DIR / f"gpt_fail_{now_tag()}.txt", str(e))
        write_text(REPORT_INCONSIST, "# Inconsistencies\nGPT unavailable / rate-limited. See agent/reports/gpt_fail_*.txt\n")
        write_text(REPORT_LINKS, "# Links Applied\nGPT unavailable / rate-limited. See agent/reports/gpt_fail_*.txt\n")
        return {"applied": [], "inconsistencies": []}

    inconsistencies = rep.get("inconsistencies", [])
    suggestions = rep.get("link_suggestions", [])

    applied = []

    def safe_link_once(text: str, title: str):
        if f"[[{title}]]" in text:
            return text, False
        parts = re.split(r"(```.*?```)", text, flags=re.S)
        pat = re.compile(rf"(?<!\[\[)(?<!\w)({re.escape(title)})(?!\]\])(?!\w)")
        replaced = False
        outp = []
        for part in parts:
            if part.startswith("```") and part.endswith("```"):
                outp.append(part)
                continue
            if replaced:
                outp.append(part)
                continue
            m = pat.search(part)
            if m:
                part = part[:m.start(1)] + f"[[{title}]]" + part[m.end(1):]
                replaced = True
            outp.append(part)
        return "".join(outp), replaced

    for s in suggestions:
        f = s.get("file", "")
        t = s.get("title", "")
        if not f or not t or t not in title_set:
            continue
        p = ROOT / f
        if not p.exists():
            continue
        old = read_text(p)
        new, did = safe_link_once(old, t)
        if did and new != old:
            write_text(p, new)
            applied.append((f, t))

    # Reports
    inc_md = ["# Inconsistencies\n"]
    if inconsistencies:
        for it in inconsistencies:
            inc_md.append(f"## {it.get('file','')}")
            inc_md.append(f"- Issue: {it.get('issue','')}")
            inc_md.append(f"- Evidence: {it.get('evidence','')}\n")
    else:
        inc_md.append("None detected.\n")
    write_text(REPORT_INCONSIST, "\n".join(inc_md))

    link_md = ["# Links Applied\n"]
    if applied:
        for f, t in applied:
            link_md.append(f"- {f}: linked [[{t}]]")
    else:
        link_md.append("No link edits applied.\n")
    write_text(REPORT_LINKS, "\n".join(link_md))

    return {"applied": applied, "inconsistencies": inconsistencies}

# -----------------------------
# Pipeline
# -----------------------------
def step_seed_ollama(task: str) -> str:
    prompt = f"""
You generate compact seed material. Hard limit: 120 lines total.
Return:
- 10 place names
- 10 faction names
- 20 person names + 1-line hook
- 10 rumor hooks

World: Solumora. Equator is lethal desert; two belts.
Task:
{task}
""".strip()
    seed = call_ollama(prompt)
    write_text(SEED_FILE, seed)
    return seed

def run_pipeline():
    ensure_dirs()
    load_secrets()

    # clear convo log per run (optional)
    write_text(CONVO_LOG, "")

    task = read_text(TASK_FILE).strip()
    if not task:
        print("TASK.md empty. Nothing to do.")
        return

    ctx = pack_context(task)

    # Ollama seed (small)
    seed = ""
    try:
        seed = step_seed_ollama(task)
        print("Ollama seed written to:", SEED_FILE)
    except Exception as e:
        seed = "(ollama seed skipped)"
        write_text(SEED_FILE, seed)
        write_text(REPORTS_DIR / f"ollama_fail_{now_tag()}.txt", str(e))

    # Claude plan
    plan = step_plan_claude(task, ctx, seed)

    all_changed = []
    all_patches = []

    review_mode = getattr(run_pipeline, "_review_mode", False)

    for batch_num, batch in enumerate(plan.get("batches", []), 1):
        patch = step_build_batch_claude(task, ctx, seed, plan, batch)

        if review_mode:
            # Write pending review file for Claude Code to inspect
            notes = plan["notes"]
            pending_notes = [notes[i] for i in batch]
            lines = [f"# Pending Batch {batch_num} of {len(plan.get('batches',[]))}\n"]
            lines.append(f"Notes in this batch: {[n['path'] for n in pending_notes]}\n\n")
            for op in patch.get("writes", []):
                lines.append(f"## WRITE: {op['path']}\n\n```\n{op['content'][:3000]}\n```\n")
            for op in patch.get("appends", []):
                lines.append(f"## APPEND: {op['path']}\n\n```\n{op['append'][:3000]}\n```\n")
            lines.append("\n---\nTo approve: write `APPROVED` to agent/staging/REVIEW_RESPONSE.md\n")
            lines.append("To reject:  write `REJECTED` (optionally followed by notes) to agent/staging/REVIEW_RESPONSE.md\n")
            write_text(STAGING_DIR / "PENDING_REVIEW.md", "".join(lines))
            # Remove stale response file
            resp_path = STAGING_DIR / "REVIEW_RESPONSE.md"
            if resp_path.exists():
                resp_path.unlink()

            print(f"\n⏸  REVIEW GATE — Batch {batch_num}: {[n['path'] for n in pending_notes]}")
            print(f"   Inspect: agent/staging/PENDING_REVIEW.md")
            print(f"   Then write APPROVED or REJECTED to agent/staging/REVIEW_RESPONSE.md")

            # Poll for response
            while True:
                time.sleep(0.5)
                if resp_path.exists():
                    response = read_text(resp_path).strip()
                    if response.upper().startswith("APPROVED"):
                        print(f"✅ Batch {batch_num} approved — applying.")
                        break
                    elif response.upper().startswith("REJECTED"):
                        notes_text = response[8:].strip()
                        print(f"❌ Batch {batch_num} rejected. Notes: {notes_text or '(none)'}")
                        append_text(CONVO_LOG, f"\n[REVIEW REJECTED batch {batch_num}]\n{notes_text}\n")
                        patch = {"writes": [], "appends": []}  # empty patch = skip
                        break

        changed = apply_patch(patch)
        all_changed.extend(changed)
        all_patches.append(patch)
        time.sleep(CLAUDE_SLEEP_SECONDS)

    all_changed = sorted(set(all_changed))
    write_text(PATCH_FILE, json.dumps({"patches": all_patches}, indent=2))
    write_text(CHANGELOG, json.dumps({"changed_files": all_changed}, indent=2))

    # GPT QA + links
    step_gpt_qa_and_link(ctx, all_changed)

    print("\n✅ PIPELINE COMPLETE")
    print("Changed files:", len(all_changed))
    print("Conversation log:", CONVO_LOG)
    print("Reports:")
    print(" - agent/reports/inconsistencies.md")
    print(" - agent/reports/links_applied.md")

# -----------------------------
# Watcher
# -----------------------------
if WATCHDOG_AVAILABLE:
    class TaskWatcher(FileSystemEventHandler):
        def __init__(self):
            self.last_hash = ""

        def on_modified(self, event):
            if Path(event.src_path) != TASK_FILE:
                return
            txt = read_text(TASK_FILE).strip()
            h = sha(txt)
            if h == self.last_hash:
                return
            self.last_hash = h

            print("\nTASK changed -> running pipeline...\n")
            try:
                run_pipeline._review_mode = getattr(run_pipeline, "_review_mode", False)
                run_pipeline()
            except Exception as e:
                log_error("watch_run_pipeline", e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="Run pipeline when TASK.md changes")
    parser.add_argument("--loop", action="store_true",
                        help="Run pipeline now, then loop: re-run whenever TASK.md changes")
    parser.add_argument("--review", action="store_true",
                        help="Pause after each batch for human/Claude Code review before applying")
    args = parser.parse_args()

    ensure_dirs()

    if not TASK_FILE.exists():
        write_text(TASK_FILE, "Goal:\nConstraints:\nOutput:\n")

    if args.review:
        run_pipeline._review_mode = True
        print("Review mode enabled — each batch will pause for approval before applying.")

    if args.loop:
        def file_hash():
            try:
                return hashlib.md5(TASK_FILE.read_bytes()).hexdigest()
            except Exception:
                return ""

        print("Loop mode: running pipeline now, then polling for TASK.md changes...")
        while True:
            try:
                run_pipeline()
            except Exception as e:
                log_error("loop_run", e)
            last_hash = file_hash()
            print("\nPipeline complete. Waiting for TASK.md to change (loop mode)...")
            while file_hash() == last_hash:
                time.sleep(3)
            print("\nTASK.md changed -> starting next pipeline run...\n")
        return

    if args.watch:
        if not WATCHDOG_AVAILABLE:
            print("watchdog not installed. Install: python -m pip install watchdog")
            print("Running single-shot instead.\n")
            try:
                run_pipeline()
            except Exception as e:
                log_error("single_run", e)
            return

        print("Watching agent/TASK.md ...")
        observer = Observer()
        handler = TaskWatcher()
        observer.schedule(handler, str(AGENT_DIR), recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        try:
            run_pipeline()
        except Exception as e:
            log_error("single_run", e)


if __name__ == "__main__":
    main()