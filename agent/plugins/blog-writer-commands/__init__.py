"""Blog-writer profile slash commands."""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

REPO_PATH = Path("/home/ubuntu/.hermes/profiles/blog-writer/repo/blog.without.hosting")
POSTS_DIR = REPO_PATH / "content" / "posts"


def _run_git(args: list[str]) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=str(REPO_PATH),
        text=True,
        stderr=subprocess.DEVNULL,
        timeout=5,
    ).strip()


def _github_base_url() -> str:
    try:
        remote = _run_git(["remote", "get-url", "origin"])
    except Exception:
        remote = "https://github.com/wimpheling/blog.without.hosting"
    remote = remote.strip()
    if remote.startswith("git@github.com:"):
        repo = remote[len("git@github.com:"):].removesuffix(".git")
        return f"https://github.com/{repo}"
    if remote.startswith("https://github.com/"):
        return remote.removesuffix(".git")
    return "https://github.com/wimpheling/blog.without.hosting"


def _branch() -> str:
    try:
        return _run_git(["branch", "--show-current"]) or "master"
    except Exception:
        return "master"


def _extract_front_matter(text: str) -> dict[str, str]:
    """Tiny YAML/TOML-ish front matter parser for simple scalar fields."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end == -1:
            return {}
        block = text[3:end]
    elif text.startswith("+++"):
        end = text.find("\n+++", 3)
        if end == -1:
            return {}
        block = text[3:end]
    else:
        return {}

    data: dict[str, str] = {}
    for raw in block.splitlines():
        line = raw.strip().rstrip("\r")
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
        elif "=" in line:
            key, value = line.split("=", 1)
        else:
            continue
        key = key.strip().lower()
        value = value.strip().strip('"\'')
        data[key] = value
    return data


def _is_true(value: str | None) -> bool:
    return str(value or "").strip().strip('"\'').lower() in {"true", "yes", "1"}


def _title_from_file(path: Path, fm: dict[str, str]) -> str:
    title = fm.get("title") or fm.get("name") or ""
    title = re.sub(r"\s+", " ", title).strip()
    if title:
        return title
    return path.stem.replace("-", " ").replace("_", " ").strip().title()


def _github_file_url(path: Path) -> str:
    rel = path.relative_to(REPO_PATH).as_posix()
    # Quote path segments but keep slashes readable.
    quoted_rel = "/".join(quote(part) for part in rel.split("/"))
    return f"{_github_base_url()}/blob/{quote(_branch())}/{quoted_rel}"


def list_drafts() -> str:
    if not POSTS_DIR.exists():
        return f"Drafts folder not found: `{POSTS_DIR}`"

    drafts: list[tuple[str, str]] = []
    for path in sorted(POSTS_DIR.rglob("*.md"), key=lambda p: p.name.lower()):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fm = _extract_front_matter(text)
        if _is_true(fm.get("draft")):
            drafts.append((_title_from_file(path, fm), _github_file_url(path)))

    if not drafts:
        return "No draft articles found."

    return "\n".join(f"{title} {url}" for title, url in drafts)


def _handle_drafts(raw_args: str = "") -> str:
    return list_drafts()


def _run_nudge_command(mode: str) -> str:
    script = Path("/home/ubuntu/.hermes/profiles/blog-writer/scripts/nudge_tick.py")
    try:
        result = subprocess.run(
            ["python3", str(script), mode],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=220,
            env={**os.environ, "HERMES_HOME": "/home/ubuntu/.hermes/profiles/blog-writer"},
        )
    except subprocess.TimeoutExpired:
        return "Nudge generation timed out."
    out = (result.stdout or "").strip()
    if result.returncode != 0:
        err = (result.stderr or "").strip()
        return f"Nudge command failed: {err or 'unknown error'}"
    return out or "No nudge output."


def _handle_nudge(raw_args: str = "") -> str:
    return _run_nudge_command("nudge")


def _handle_nudge_state(raw_args: str = "") -> str:
    return _run_nudge_command("state")


def register(ctx) -> None:
    ctx.register_command(
        "drafts",
        handler=_handle_drafts,
        description="List current draft articles with GitHub links.",
    )
    ctx.register_command(
        "nudge",
        handler=_handle_nudge,
        description="Generate one blog-writing nudge now.",
    )
    ctx.register_command(
        "nudge-state",
        handler=_handle_nudge_state,
        description="Show the current blog nudge scheduler state.",
    )
