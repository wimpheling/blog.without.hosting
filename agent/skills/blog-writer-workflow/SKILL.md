---
name: blog-writer-workflow
description: "Operate the user's Hugo blog writer/editor profile: ramble-to-draft, repo edits, commit/push, and publish gate."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [blog, hugo, writing, telegram, git]
---

# Blog Writer Workflow

Use this skill whenever the user asks to capture blog ideas, draft/edit Hugo posts, commit/push blog changes, publish/unlist an article, or send writing nudges.

## Repository

- Repo path: `/home/ubuntu/.hermes/profiles/blog-writer/repo/blog.without.hosting`
- Remote: `https://github.com/wimpheling/blog.without.hosting`
- Posts: `content/posts/*.md`
- Current cloned branch: `master` unless changed by GitHub later.
- The Hugo repo is the source of truth for article content and article state.

## Hard Rules

1. Article draft/publish state lives in front matter via the `unlisted` field.
2. Do not maintain a separate editorial database for article state.
3. Content edits may be committed and pushed directly to the default branch.
4. **Draft = `unlisted: true`** (rendered at its URL, hidden from the posts list).
5. **Published = no `unlisted` field, or `unlisted: false`** (listed normally).
6. Never change `unlisted: true` to `unlisted: false` (or remove the field) — i.e., never unlist → publish — without explicit user validation in the current conversation.
7. Do not use PRs to manage draft status.
8. The Hugo site builds with `--buildDrafts` (or equivalent) so `draft: true` posts are NOT rendered. The `unlisted` convention replaces Hugo's built-in draft flag for content that should be reachable but hidden from listings.

## Writing Loop

1. Read the relevant post(s) under `content/posts/`.
2. Extract the claim/thesis from the user's ramble.
3. Suggest one concise next move, or edit the draft directly if asked.
4. Preserve the user's voice: technical, opinionated, exploratory, sometimes bilingual English/French.
   - Avoid over-polished, impersonal, wordy LLM prose. Keep rough edges when they make the post feel more authored.
   - Do not inflate minor operational details into grand claims. If a section like "the interesting constraint" overstates something already covered, cut it rather than making it sound profound.
5. When revisiting old/draft clusters, do not flatten the user's idea into a generic "this aged badly" take. Separate:
   - what was hype-era framing or vocabulary;
   - what remains structurally true;
   - what the user corrects as the deeper durable claim.
   A good pattern is a revision/retrospective draft that starts from the published article, names what changed, salvages the good ideas, and proposes a modern stack or next thesis.
6. For dated article clusters, propose an editorial consolidation path instead of mechanically polishing every draft. Identify what aged badly, what still holds, and a stronger modern framing.
7. After editing files:
   - Run `git diff --check`.
   - Review the diff for accidental publishing/unlisting.
   - Commit and push.
   - In the final reply, include a read link (production blog URL).

## Commit/Push Helper

Use the helper script after edits:

```bash
/home/ubuntu/.hermes/profiles/blog-writer/scripts/blog_commit_push.py "draft: update article title"
```

If the change intentionally unlists → publishes after explicit user approval:

```bash
ALLOW_PUBLISH=1 /home/ubuntu/.hermes/profiles/blog-writer/scripts/blog_commit_push.py "publish: article title"
```

If push fails, GitHub PAT is probably missing. Ask the user for a PAT and run:

```bash
BLOG_GITHUB_PAT='TOKEN' /home/ubuntu/.hermes/profiles/blog-writer/scripts/configure_git_auth.py
```

## Revision/Retrospective Posts

For a detailed reusable pattern, see `references/revision-retrospective-posts.md`.

Use it when the user revisits old published posts or dated draft clusters and wants to recover the durable thesis while acknowledging what aged badly.

## Article Style Guidelines

Adapted from the user's French web-writing guidelines, but filtered for a personal technical blog rather than corporate SEO copy.

Use these as defaults when drafting or editing posts:

- **Title**: short, explicit, autonomous, and front-loaded with the meaningful words. Prefer 4–10 words when possible. Avoid vague cleverness, clickbait, exclamation marks, and decorative wordplay. A title can be catchy, but clarity wins.
- **Description/front matter**: write a concise description that works as the post's search/result preview. It should explain the value of the post and invite reading, not just repeat the title.
- **Opening**: get to the point quickly. The first paragraph should contain the core situation, tension, or claim. Avoid throat-clearing and generic context.
- **Inverted pyramid, lightly applied**: start with the essential idea, then add nuance, background, examples, and caveats. Do not bury the actual claim halfway down the post.
- **One idea per paragraph**: keep paragraphs focused. The first sentence should usually signal the paragraph's point.
- **Readable structure**: use headings, bullets, and short sections when they help scanning. Do not over-structure into bureaucratic outlines.
- **Sentences**: prefer active voice, concrete vocabulary, and short-to-medium sentences. Break long chains of subclauses. Avoid unnecessary parentheses, semicolons, and ornamental transitions.
- **Jargon**: technical terms are fine when useful, but explain non-obvious acronyms or domain-specific shorthand early.
- **SEO without keyword stuffing**: include natural terms a reader might search for, especially in title/description/opening, but never distort the voice for SEO.
- **Links**: use explicit link text that says where the link goes. Avoid "click here". Prefer a few relevant links over link dumping.
- **Dates/time**: use absolute time references when durability matters (e.g. "in June 2026" rather than "now" or "last month").
- **Images**: if images are used, prefer informative images and give them meaningful alt text. Decorative images should not pretend to carry SEO meaning.
- **Voice override**: these rules must not erase the user's voice. Preserve rough edges, opinions, and exploratory tone. Do not turn posts into polished institutional web copy.

## Nudge Style

Nudges should be:
- short, casual, and specific
- based on an active draft or captured idea
- framed as an easy next move
- feel like a fluent conversation about the subject matter, not a dry reminder
- include a read link when pointing to a post (production blog URL)

Good:
- "Your LLM island idea has a strong core: generated code as a scoped interactive island inside deterministic structure. Want to turn that into the intro?"

Bad:
- "Reminder: please write today."

## Blog Nudge Automation

Use this when modifying the blog-writer nudge cron, `/nudge`, `/nudge-state`, or related Telegram commands.

- Main profile script: `/home/ubuntu/.hermes/profiles/blog-writer/scripts/nudge_tick.py`.
- Telegram command plugin: `/home/ubuntu/.hermes/profiles/blog-writer/plugins/blog-writer-commands/__init__.py`.
- State file: `/home/ubuntu/.hermes/profiles/blog-writer/scheduler/nudge_state.json`.
- Keep the architecture split by entry point:
  - scheduled cron path: checks active window, creates/uses daily plan, sends only when a planned slot is due, and may be silent;
  - manual `/nudge` path: generates immediately, skips active-window and planned-slot checks, and must not consume scheduled slots;
  - `/nudge-state` path: read-only state inspection and must not mutate state.
- Generation should remain transport-neutral: return/print text; cron delivery and Telegram command response handle sending.
- Manual and scheduled nudges should still update recent nudge history so candidate selection avoids repeating the same post/idea.
- Validate changes with at least: Python compile of the script/plugin, state command smoke test, manual path test with a fake generator/no LLM call, plugin command registration check, and `git diff --check` in the Hugo repo.
- Do not restart the gateway automatically if it may interrupt the active user session; tell the user to run `/restart` when ready.

## Nudge Automation Design

When modifying scheduled or Telegram-triggered blog nudges, keep scheduling, generation, and delivery separate. Cron and manual commands should call different service entry points instead of sharing one flag-heavy `maybe_send_nudge()` flow:

- `run_cron_tick(deps)`: scheduled path; respects active window, daily plan, and due slots; may be silent.
- `generate_manual_nudge(deps)`: manual `/nudge`; skips scheduling gates and daily slot consumption, but still uses candidate selection, recent-history avoidance, LLM generation, and read-link rules.
- `get_state_json(deps)`: read-only `/nudge-state`; returns pretty state or a short missing-state message.

Manual nudges should not consume scheduled slots, but should update recent nudge/post history so the next scheduled nudge does not repeat the same draft.

Detailed architecture and test matrix: `references/nudge-automation-architecture.md`.
