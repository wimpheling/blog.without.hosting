#!/usr/bin/env python3
"""Generate data/edits/<slug>.json for each post whose commits have git notes.

For each content/posts/*.md, walks its git log. For each commit that has a
JSON-formatted note, parses the note and adds an entry to the post's data file.
The Hugo partial `layouts/partials/posts/edits.html` reads these data files at
build time and renders the Edits block at the bottom of the post.

This script is meant to run as a build step before `hugo` (locally and on
Netlify). Output is in `data/edits/`, which is gitignored — it's a build
artifact regenerated on every build.

Note: a single commit can touch multiple posts; the same edit metadata appears
in each post's data file, which is the desired reader-facing behavior.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_DIR = REPO / "data" / "edits"
POSTS_DIR = REPO / "content" / "posts"


def run(*args):
    r = subprocess.run(
        args, cwd=REPO, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    return r


def get_commits_for_file(rel_path):
    r = run("git", "log", "--pretty=format:%H", "--", rel_path)
    if r.returncode != 0 or not r.stdout.strip():
        return []
    return r.stdout.strip().split("\n")


def get_note(commit_hash):
    r = run("git", "notes", "show", commit_hash)
    if r.returncode != 0 or not r.stdout:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def existing_post_slugs():
    return {p.stem for p in POSTS_DIR.glob("*.md") if p.name != "_index.md"}


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    valid_slugs = existing_post_slugs()
    generated_files = set()
    total_edits = 0

    for post_file in sorted(POSTS_DIR.glob("*.md")):
        if post_file.name == "_index.md":
            continue
        slug = post_file.stem
        rel_path = f"content/posts/{post_file.name}"
        commits = get_commits_for_file(rel_path)
        edits = []
        for commit_hash in commits:
            note = get_note(commit_hash)
            if not note:
                continue
            edits.append({
                "edited_at": note.get("edited_at", ""),
                "description": note.get("description", ""),
                "author": note.get("author", ""),
                "commit": commit_hash[:7],
            })
        out_path = DATA_DIR / f"{slug}.json"
        generated_files.add(out_path.name)
        if edits:
            out_path.write_text(
                json.dumps(edits, indent=2, ensure_ascii=False)
            )
            total_edits += len(edits)
            print(f"  {post_file.name}: {len(edits)} edit(s)")
        elif out_path.exists():
            out_path.unlink()
            print(f"  {post_file.name}: cleared stale data")

    # Clean up data files for slugs that no longer correspond to a post
    for stale in DATA_DIR.glob("*.json"):
        if stale.name not in generated_files:
            stale.unlink()
            print(f"  removed orphan: {stale.name}")

    n_posts = len(list(POSTS_DIR.glob("*.md"))) - (1 if (POSTS_DIR / "_index.md").exists() else 0)
    print(f"Total: {total_edits} edit(s) across {n_posts} post(s).")


if __name__ == "__main__":
    sys.exit(main())
