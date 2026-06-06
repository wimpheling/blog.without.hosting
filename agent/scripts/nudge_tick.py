#!/usr/bin/env python3
"""Blog-writer nudger.

Modes:
- cron (default): silent unless a scheduled nudge is due.
- nudge: generate one manual nudge immediately.
- state: print current nudge state JSON.
"""
from __future__ import annotations

import json
import os
import random
import re
import subprocess
import sys
from datetime import datetime, time, timedelta
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo

PROFILE_HOME = Path(os.environ.get("HERMES_HOME", "/home/ubuntu/.hermes/profiles/blog-writer"))
STATE_DIR = PROFILE_HOME / "scheduler"
STATE_PATH = STATE_DIR / "nudge_state.json"
REPO = PROFILE_HOME / "repo" / "blog.without.hosting"
POSTS_DIR = REPO / "content" / "posts"
IDEAS = Path("/home/ubuntu/tgbots/data/blog_ideas.json")
TZ = ZoneInfo("Europe/Lisbon")
ACTIVE_START_HOUR = 6
ACTIVE_END_HOUR = 1
TICK_MINUTES = 21
RECENT_LIMIT = 12


def now_lisbon() -> datetime:
    return datetime.now(TZ)


def active_window_bounds(now: datetime) -> tuple[datetime, datetime]:
    # Active window is 06:00 today -> 01:00 next day. For 00:xx, window started yesterday.
    if now.hour < ACTIVE_END_HOUR:
        start_date = (now - timedelta(days=1)).date()
    else:
        start_date = now.date()
    start = datetime.combine(start_date, time(ACTIVE_START_HOUR, 0), TZ)
    end = datetime.combine(start_date + timedelta(days=1), time(ACTIVE_END_HOUR, 0), TZ)
    return start, end


def in_active_window(now: datetime) -> bool:
    start, end = active_window_bounds(now)
    return start <= now < end


def plan_key(now: datetime) -> str:
    start, _ = active_window_bounds(now)
    return start.date().isoformat()


def load_state() -> dict:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text())
        except Exception:
            return {}
    return {}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True))
    tmp.replace(STATE_PATH)


def make_plan(key: str, start: datetime, end: datetime) -> dict:
    rng = random.Random(f"blog-writer-nudges:{key}")
    target = rng.choice([2, 3])
    total_minutes = int((end - start).total_seconds() // 60)
    margin = 45
    usable = max(60, total_minutes - 2 * margin)
    planned = []
    for i in range(target):
        band_start = margin + int(i * usable / target)
        band_end = margin + int((i + 1) * usable / target)
        minute = rng.randint(band_start, max(band_start, band_end - 1))
        minute += rng.randint(-17, 17)
        minute = max(margin, min(total_minutes - margin, minute))
        planned.append({
            "time": (start + timedelta(minutes=minute)).isoformat(),
            "sent": False,
            "sent_at": None,
            "post": None,
            "message": None,
        })
    planned.sort(key=lambda x: x["time"])
    # Keep legacy fields so old state readers do not break.
    return {"key": key, "target": target, "slots": [p["time"] for p in planned], "sent": [], "planned": planned}


def get_or_create_plan(state: dict, now: datetime) -> dict:
    key = plan_key(now)
    start, end = active_window_bounds(now)
    plan = state.get("plan")
    if not plan or plan.get("key") != key:
        plan = make_plan(key, start, end)
        state["plan"] = plan
        state["timezone"] = str(TZ)
        state["active_window"] = {"start": "06:00", "end": "01:00"}
        state["generated_at"] = now.isoformat()
        save_state(state)
    elif "planned" not in plan:
        sent = set(plan.get("sent", []))
        plan["planned"] = [{
            "time": slot,
            "sent": slot in sent,
            "sent_at": None,
            "post": None,
            "message": None,
        } for slot in plan.get("slots", [])]
        state["plan"] = plan
        save_state(state)
    return plan


def due_planned_nudge(plan: dict, now: datetime) -> dict | None:
    planned = plan.get("planned") or []
    for item in planned:
        if item.get("sent"):
            continue
        dt = datetime.fromisoformat(item["time"])
        if dt <= now <= dt + timedelta(minutes=TICK_MINUTES + 8):
            return item
    return None


def _extract_front_matter(text: str) -> dict[str, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        block = text[3:end] if end != -1 else ""
    elif text.startswith("+++"):
        end = text.find("\n+++", 3)
        block = text[3:end] if end != -1 else ""
    else:
        block = ""
    data: dict[str, str] = {}
    for raw in block.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        sep = ":" if ":" in line else "=" if "=" in line else None
        if not sep:
            continue
        key, value = line.split(sep, 1)
        data[key.strip().lower()] = value.strip().strip('"\'')
    return data


def _is_true(value: str | None) -> bool:
    return str(value or "").strip().strip('"\'').lower() in {"true", "yes", "1"}


def _run_git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=str(REPO), text=True, stderr=subprocess.DEVNULL, timeout=5).strip()
def _github_file_url(path: Path) -> str:
    rel = path.relative_to(REPO).as_posix()
    quoted_rel = "/".join(quote(part) for part in rel.split("/"))
    return f"https://github.com/wimpheling/blog.without.hosting/blob/master/{quoted_rel}"


def _title(path: Path, fm: dict[str, str]) -> str:
    title = re.sub(r"\s+", " ", fm.get("title", "")).strip()
    return title or path.stem.replace("-", " ").title()


def collect_candidates() -> list[dict]:
    candidates: list[dict] = []
    if POSTS_DIR.exists():
        for path in sorted(POSTS_DIR.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            fm = _extract_front_matter(text)
            unlisted = _is_true(fm.get("unlisted"))
            candidates.append({
                "kind": "post",
                "id": path.relative_to(REPO).as_posix(),
                "title": _title(path, fm),
                "unlisted": unlisted,
                "url": f"https://blog.without.hosting/posts/{path.stem}/",
                "mtime": path.stat().st_mtime,
                "excerpt": text[:900].replace("\n", " "),
            })
    if IDEAS.exists():
        try:
            for idea in json.loads(IDEAS.read_text())[-8:]:
                txt = str(idea.get("text") or "").strip()
                if txt:
                    candidates.append({"kind": "idea", "id": f"idea:{idea.get('id')}", "title": txt[:80], "unlisted": True, "url": None, "mtime": 0, "excerpt": txt})
        except Exception:
            pass
    return candidates


def select_candidate(candidates: list[dict], state: dict) -> dict | None:
    if not candidates:
        return None
    recent_posts = [x.get("post") for x in state.get("recent_nudges", [])[-5:]]
    fresh = [c for c in candidates if c["id"] not in recent_posts]
    pool = fresh or candidates
    unlisted = [c for c in pool if c.get("unlisted")]
    pool = unlisted or pool
    return sorted(pool, key=lambda c: c.get("mtime", 0), reverse=True)[0]


def build_context(candidate: dict | None, state: dict) -> str:
    parts = []
    if candidate:
        parts.append("Selected candidate:\n" + json.dumps(candidate, ensure_ascii=False, indent=2))
    candidates = collect_candidates()[:8]
    if candidates:
        parts.append("Other recent drafts/posts/ideas:\n" + "\n".join(
            f"- {c['title']} ({c['id']}) unlisted={c.get('unlisted')} link={c.get('url') or 'none'}" for c in candidates
        ))
    recent = state.get("recent_nudges", [])[-5:]
    if recent:
        parts.append("Recent nudges to avoid repeating:\n" + "\n".join(f"- {x.get('message')}" for x in recent))
    return "\n\n".join(parts) if parts else "No repo/idea context found."


def generate_nudge(context: str) -> str:
    prompt = f"""
You are the user's casual blog-writing partner. Generate exactly ONE short Telegram nudge.

Rules:
- 1-3 sentences max.
- Casual, specific, writer/editor vibe.
- No generic productivity guilt.
- Reference one current draft or idea if possible.
- Offer one easy next move.
- If the selected candidate has a link, include it naturally at the end.
- Do not modify files. Return only the message text.

Context:
{context}
""".strip()
    cmd = ["blog-writer", "chat", "-Q", "-t", "file,terminal", "-q", prompt]
    env = os.environ.copy()
    env["HERMES_HOME"] = str(PROFILE_HOME)
    try:
        result = subprocess.run(cmd, cwd=str(REPO) if REPO.exists() else str(PROFILE_HOME), env=env,
                                text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180)
    except subprocess.TimeoutExpired:
        return "You’ve got a few draft threads open — want to pick one and turn the messiest bit into a clean thesis?"
    out = (result.stdout or "").strip()
    if result.returncode != 0 or not out:
        return "You’ve got a few draft threads open — want to pick one and turn the messiest bit into a clean thesis?"
    lines = []
    for ln in out.splitlines():
        s = ln.strip()
        if not s or s.startswith("⚠") or s.startswith("session_id:"):
            continue
        lines.append(s)
    return "\n".join(lines[-4:])[:1200]


def _record_recent(state: dict, now: datetime, candidate: dict | None, msg: str, source: str) -> None:
    state.setdefault("recent_nudges", []).append({
        "at": now.isoformat(),
        "post": candidate.get("id") if candidate else None,
        "title": candidate.get("title") if candidate else None,
        "message": msg,
        "source": source,
    })
    state["recent_nudges"] = state["recent_nudges"][-RECENT_LIMIT:]
    state["last_sent_at"] = now.isoformat()


def generate_manual_nudge() -> str:
    now = now_lisbon()
    state = load_state()
    candidate = select_candidate(collect_candidates(), state)
    msg = generate_nudge(build_context(candidate, state))
    _record_recent(state, now, candidate, msg, "manual")
    save_state(state)
    return msg


def run_cron_tick() -> str | None:
    now = now_lisbon()
    if not in_active_window(now):
        return None
    state = load_state()
    plan = get_or_create_plan(state, now)
    if sum(1 for x in plan.get("planned", []) if x.get("sent")) >= int(plan.get("target", 2)):
        return None
    item = due_planned_nudge(plan, now)
    if not item:
        return None
    candidate = select_candidate(collect_candidates(), state)
    msg = generate_nudge(build_context(candidate, state))
    item["sent"] = True
    item["sent_at"] = now.isoformat()
    item["post"] = candidate.get("id") if candidate else None
    item["message"] = msg
    plan["sent"] = [x["time"] for x in plan.get("planned", []) if x.get("sent")]
    state["plan"] = plan
    _record_recent(state, now, candidate, msg, "scheduled")
    save_state(state)
    return msg


def state_json() -> str:
    state = load_state()
    if not state:
        return "No nudge state exists yet. It will be created on the first cron tick inside the active window."
    return json.dumps(state, indent=2, sort_keys=True, ensure_ascii=False)


def main(argv: list[str] | None = None) -> int:
    argv = list(argv or sys.argv[1:])
    mode = argv[0] if argv else "cron"
    if mode in {"state", "nudge-state"}:
        print(state_json())
        return 0
    if mode in {"nudge", "manual"}:
        print(generate_manual_nudge())
        return 0
    msg = run_cron_tick()
    if msg:
        print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
