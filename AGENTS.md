# AGENTS.md — blog.without.hosting

Operational notes for any AI agent (Hermes, Claude Code, Codex, etc.) working in this repo.

## Commits: never raw `git commit` for content edits

Content edits must be committed via the helper script — it is the **only** path that attaches the git-note metadata that powers the public "Edits" log.

```bash
# From anywhere — the script chdir's into the repo itself.
python3 ~/.hermes/profiles/blog-writer/scripts/blog_commit_push.py "edit: <description>"
```

The script also handles the publish-guard (refuses to flip `unlisted: true` → published without `ALLOW_PUBLISH=1`) and pushes the `refs/notes/commits` ref alongside `HEAD`.

### Commit-message conventions

| Prefix                          | Behaviour                                            |
| ------------------------------- | ---------------------------------------------------- |
| `edit: <description>`           | Attaches a git note. Author = `$HERMES_AUTHOR` or `bully`. |
| `edit[<author>]: <description>` | Same, with explicit author (e.g. `edit[hermes]: …`). |
| Anything else (e.g. `chore:`, `draft:`) | Normal commit. **No git note.** Use for infrastructure, scaffolds, content-only-no-render, agent state. |

Keep the description short and human — it shows up on the public post as the edit label. Examples that read well: `fix typo "a anthropic" → "an anthropic"`, `expand the "agent failure modes" section`, `correct the link to the X thread`.

## Drafts: use `unlisted: true`, not `draft: true`

- `draft: true` ⇒ the post **does not build** on Netlify. Hidden entirely.
- `unlisted: true` ⇒ the post builds and is reachable at its prod URL, but hidden from the post list. This is the working state for a draft the user wants to preview.

**Never** remove `unlisted: true` (or change it to `false`) on your own. Publishing requires explicit user validation in the current chat. The commit script blocks it; the publish override is `ALLOW_PUBLISH=1` — only set it when the user has said "publish it" in this conversation.

## Environment knobs

- `SKIP_PUSH=1` — stage + commit only. No push, no notes push. Use for review.
- `ALLOW_PUBLISH=1` — bypass the unlisted→published guard. Only with user approval.
- `HERMES_AUTHOR=<name>` — overrides the default author (`bully`) on `edit:` commits. The agent-self convention is `hermes`.

## Build pipeline (Netlify)

`netlify.toml` runs this in order:

```
python3 scripts/build_edits.py && hugo --gc --minify --buildFuture
```

- `build_edits.py` walks all commits, extracts `refs/notes/commits` notes for rendered posts, and writes `data/edits/<slug>.json` (gitignored, regenerated each build).
- The Hugo partial `layouts/partials/posts/edits.html` reads from `.Site.Data.edits` and renders the log at the bottom of each post.
- `data/edits/` is in `.gitignore` — never commit it.

If the Edits block disappears from prod, check (in order): (1) the commit was actually pushed, (2) `refs/notes/commits` was pushed (`git push origin refs/notes/commits`), (3) `build_edits.py` ran in the Netlify build log.

## Layout / Hugo specifics

- Hugo pinned to `0.111.3 extended` locally (Netlify deploys with `0.89.4`; both work, but the theme's SCSS requires `extended`).
- `--buildFuture` is required or future-dated posts 404 silently.
- Theme is consumed as a git submodule under `themes/` — don't edit theme files directly; use `layouts/posts/single.html` and `layouts/partials/posts/*.html` to override.

## Do not touch

- `agent/` — runtime state for the blog-writer Hermes profile. Out of scope for content work.
- `public/`, `resources/`, `data/edits/` — build artifacts.
- `themes/*` — read-only submodule.
