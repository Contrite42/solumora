#!/usr/bin/env python3
import os, re, json, time, hashlib, argparse, traceback
from pathlib import Path

import requests

# Optional watch mode (script still runs without it)
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
SECRETS_PATH = AGENT_DIR / "secrets.json"

PLAN_FILE = STAGING_DIR / "PLAN.json"
SEED_FILE = STAGING_DIR / "OLLAMA_SEED.md"
PATCH_FILE = STAGING_DIR / "PATCH.json"
CHANGELOG = STAGING_DIR / "CHANGELOG.json"

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

# Keep Claude calls smaller = fewer rate problems + less malformed JSON
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

def extract_first_json_object(raw: str) -> str:
    m = re.search(r"\{.*\}", raw, flags=re.S)
    return m.group(0) if m else ""

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
    ctx_files = basic_retrieve(task)
    ctx_blobs = []
    for f in ctx_files:
        rel = str(f.relative_to(ROOT))
        txt = read_text(f)[:14000]
        ctx_blobs.append(f"\n--- FILE: {rel} ---\n{txt}\n")
    bundle = ("\n".join(ctx_blobs))[:180000]
    return {"canon": canon, "style": style, "qa": qa, "files": ctx_files, "bundle": bundle}

# -----------------------------
# Network calls with retry/backoff
# -----------------------------
def http_post_with_retry(url, headers, payload, timeout, label, max_attempts=6):
    for attempt in range(1, max_attempts + 1):
        r = requests.post(url, headers=headers, json=payload, timeout=timeout)
        if r.status_code == 200:
            return r
        # retry on rate / transient
        if r.status_code in (429, 500, 502, 503, 504, 529):
            wait = min(60, 2 ** attempt)
            msg = r.text[:400]
            print(f"[retry:{label}] status={r.status_code} attempt={attempt}/{max_attempts} wait={wait}s msg={msg}")
            time.sleep(wait)
            continue
        # hard fail
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
    r = http_post_with_retry(url, headers, payload, timeout=180, label="openai")
    return r.json()["choices"][0]["message"]["content"]

def call_claude(system: str, user: str, max_tokens: int = 3500, temperature: float = 0.35) -> str:
    key = (os.getenv("ANTHROPIC_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY missing.")
    print("Anthropic key prefix:", key[:12])

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
    r = http_post_with_retry(url, headers, payload, timeout=240, label="anthropic")
    data = r.json()
    blocks = data.get("content", [])
    out = []
    for b in blocks:
        if b.get("type") == "text":
            out.append(b.get("text", ""))
    return "\n".join(out).strip()

def call_ollama(prompt: str) -> str:
    url = f"{OLLAMA_URL}/api/generate"
    payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    r = requests.post(url, json=payload, timeout=240)
    if r.status_code != 200:
        raise RuntimeError(f"ollama failure {r.status_code}: {r.text[:800]}")
    return (r.json().get("response", "") or "").strip()

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
# Claude JSON parsing with self-repair retries
# -----------------------------
def parse_json_or_retry_with_claude(raw: str, schema_hint: str, repair_label: str, max_retries: int = 2):
    """
    Try parse -> extract -> parse.
    If malformed, ask Claude to repair into strict JSON.
    """
    raw0 = strip_code_fences(raw)

    # attempt 1: direct parse
    try:
        return json.loads(raw0)
    except Exception:
        pass

    # attempt 2: extract object parse
    j = extract_first_json_object(raw0)
    if j:
        try:
            return json.loads(j)
        except Exception:
            pass

    # fallback: Claude repairs its own output (no GPT dependency)
    repair_system = "You are a JSON repair function. Output ONLY valid JSON. No commentary. No markdown."
    repair_user = f"""
Repair this into VALID JSON that matches the schema exactly.

SCHEMA:
{schema_hint}

MALFORMED:
{raw0}
""".strip()

    last = raw0
    for i in range(max_retries):
        fixed = call_claude(repair_system, repair_user, max_tokens=2200, temperature=0.0)
        fixed = strip_code_fences(fixed)
        try:
            return json.loads(fixed)
        except Exception:
            last = fixed
            write_text(STAGING_DIR / f"{repair_label}_repair_fail_{now_tag()}.txt", fixed)

    # if still failing
    write_text(STAGING_DIR / f"{repair_label}_raw_{now_tag()}.txt", raw0)
    raise RuntimeError(f"{repair_label}: Could not parse JSON after repairs. Saved raw to agent/staging/")

# -----------------------------
# Pipeline Steps
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
  "batches": [ [0,1,2], [3,4,5] ]
}}"""

    system = """
You are the Solumora Builder.
You are planning files only. Do not write note bodies yet.
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

Return JSON exactly in this schema:
{schema_hint}

Constraints:
- Make 8–16 notes total (keep it tight).
- Each note includes at least 3 outbound links.
- Batches must be <= {CLAUDE_MAX_BATCH_NOTES} notes.
""".strip()

    raw = call_claude(system, user, max_tokens=2200, temperature=0.2)
    plan = parse_json_or_retry_with_claude(raw, schema_hint, "plan")
    write_text(PLAN_FILE, json.dumps(plan, indent=2))
    return plan

def parse_file_blocks(raw: str) -> dict:
    """
    Parse Claude output in this format:

    ===WRITE: content/path.md===
    <markdown...>
    ===END===

    ===APPEND: content/path.md===
    <markdown...>
    ===END===

    Returns patch dict:
    {"writes":[{"path":..,"content":..}], "appends":[{"path":..,"append":..}]}
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
        # Save raw for debugging
        write_text(STAGING_DIR / f"fileblock_parse_fail_{now_tag()}.txt", raw)
        raise RuntimeError("No WRITE/APPEND blocks found. Saved raw to agent/staging/fileblock_parse_fail_*.txt")

    return patch

def step_build_batch_claude(task: str, ctx: dict, seed: str, plan: dict, batch_idxs: list) -> dict:
    notes = plan["notes"]
    batch = [notes[i] for i in batch_idxs]

    schema_hint = """{
  "writes": [{"path":"content/Folder/Note.md","content":"...markdown..."}],
  "appends": [{"path":"content/Folder/Note.md","append":"...markdown section..."}]
}"""

    system = """
You are the Solumora Builder.
Write Obsidian Markdown. Everyone is mid-journey. Dense detail.
Return ONLY JSON patch in the given schema. No code fences. No commentary.
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

Rules:
- If action=create -> full file markdown in writes[]
- If action=append -> appended section only in appends[]
- Use conservative [[links]] you believe exist or you just created.
""".strip()

    raw = call_claude(system, user, max_tokens=3800, temperature=0.45)
    patch = parse_json_or_retry_with_claude(raw, schema_hint, f"batch_{sha(json.dumps(batch))}")
    return patch

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
- No extra commentary outside blocks.
- Every note must include at least 3 outbound [[links]].
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

    # parse the file-block protocol into a normal patch dict
    patch = parse_file_blocks(raw)

    # log raw output for debugging if needed
    write_text(STAGING_DIR / f"batch_fileblocks_{now_tag()}.txt", raw)

    return patch
    system = """
You are the Solumora QA + Linker.
Return JSON only:
{
 "inconsistencies":[{"file":"...","issue":"...","evidence":"..."}],
 "link_suggestions":[{"file":"...","title":"ExactExistingTitle"}]
}
Rules:
- Conservative links only (exact titles).
- Prefer fewer high-confidence suggestions.
""".strip()

    user = f"""
WORLD_STATE:
{ctx['canon']}

CHANGED FILES:
{''.join(blobs)}

KNOWN TITLES (exact):
{', '.join(titles[:900])}
""".strip()

    try:
        out = call_openai(system, user)
        rep = json.loads(strip_code_fences(out))
    except Exception as e:
        # log and return without blocking pipeline
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
                outp.append(part); continue
            if replaced:
                outp.append(part); continue
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

    # write reports
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

def run_pipeline():
    ensure_dirs()
    load_secrets()

    task = read_text(TASK_FILE).strip()
    if not task:
        print("TASK.md empty. Nothing to do.")
        return

    ctx = pack_context(task)

    # Ollama seed (small, optional)
    seed = ""
    try:
        seed = step_seed_ollama(task)
    except Exception as e:
        seed = "(ollama seed skipped)"
        write_text(SEED_FILE, seed)
        write_text(REPORTS_DIR / f"ollama_fail_{now_tag()}.txt", str(e))

    # Claude plan
    plan = step_plan_claude(task, ctx, seed)

    all_changed = []
    all_patches = []

    for batch in plan.get("batches", []):
        patch = step_build_batch_claude(task, ctx, seed, plan, batch)
        changed = apply_patch(patch)
        all_changed.extend(changed)
        all_patches.append(patch)
        time.sleep(CLAUDE_SLEEP_SECONDS)

    all_changed = sorted(set(all_changed))
    write_text(PATCH_FILE, json.dumps({"patches": all_patches}, indent=2))
    write_text(CHANGELOG, json.dumps({"changed_files": all_changed}, indent=2))

    # GPT QA + links (non-blocking)
    step_gpt_qa_and_link(ctx, all_changed)

    print("\n✅ PIPELINE COMPLETE")
    print("Changed files:", len(all_changed))
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
                run_pipeline()
            except Exception as e:
                log_error("watch_run_pipeline", e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="Run pipeline when TASK.md changes")
    args = parser.parse_args()

    ensure_dirs()

    if not TASK_FILE.exists():
        write_text(TASK_FILE, "Goal:\nConstraints:\nOutput:\n")

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