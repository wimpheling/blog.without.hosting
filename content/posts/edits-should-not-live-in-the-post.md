---
title: "Edits Should Not Live in the Post"
date: 2026-06-07T15:20:00+00:00
unlisted: true
tags: ["ghostwriter", "static sites", "git"]
toc: true
description: "LLMs turn rambles into readable posts faster than the dev work finishes. You publish early, the article evolves — git notes track that cleanly."
---

My blog has a ghostwriter. The bot writes drafts, tightens paragraphs, fixes typos, commits them. That works well.

It also creates an interesting constraint: because the LLM can turn a ramble into something readable in minutes, the post is often ready to publish long before the dev task it documents is actually finished. You want to publish early — the writing is there, readers can engage — but you are still iterating on the thing the post is about. The article will change as the work progresses.

That means you need to let readers see the change history. Not a forensic audit. Just a small block at the bottom saying: this was edited, roughly when, by whom.

This is perfectly compatible with a static, git-based blog. Hugo does not need a database to track editorial history. Git already has the tools.

## The front matter trap

The obvious move is to put an `edits` array in the YAML front matter:

```yaml
edits:
  - date: 2026-06-07
    commit: abc1234
    description: "fixed typo"
```

This works for about five minutes. Then you remember that the commit hash is a hash of the commit that includes the file content. If the file content contains the commit hash, you have a circular dependency. You can work around it — placeholder, amend, second commit — but now the workflow is cursed.

The real problem is not the circular hash though. The real problem is: you turned the article into a ledger. The front matter now has to be updated every time someone sneezes near the file. That means the ghostwriter has to maintain editorial state inside the same file it is editing. The bot becomes responsible for its own paper trail, inside the thing it is changing. There is no boundary.

## Git notes

Git has a feature for attaching arbitrary data to a commit without changing the commit. It is called [git notes](https://git-scm.com/docs/git-notes). I had heard of it. I had never used it. It turned out to be exactly what I needed.

When the commit script sees an `edit:` message, it attaches a JSON note:

```json
{
  "edited_at": "2026-06-07T15:16:37+00:00",
  "description": "fixed typo 'A Anthropic' → 'An Anthropic' before vowel sound",
  "author": "bully"
}
```

The commit stays the same. The note is separate. The metadata stops trying to contain the thing it is about.

## The build bridge

We need to plug git notes into the Hugo build. Before the build, a small script walks the commit history, collects notes attached to commits that touched posts, and writes temporary JSON files under `data/edits/`:

```text
data/edits/x-ai-quote-fabrication.json
```

Those files are gitignored. They are build artifacts, not source. Then a Hugo partial reads `.Site.Data.edits` and renders an `Edits` block on relevant posts.

The flow:

```text
edit commit → git note → build_edits.py → data/edits/<slug>.json → Hugo partial
```

That is the whole feature. It is not complicated.

## Why this matters for the ghostwriter problem

The important constraint is not technical cleverness. It is editorial parsimony.

The Markdown file remains the article and nothing else.
The commit remains the event.
The note remains metadata about the event.
The rendered page shows the reader a small public trace.

None of these layers absorb the job of the other. The front matter does not become a changelog. The commit message does not become a CMS field. The build script does not become a database.

I think this is the right shape for a blog that has a bot writing for it. If the source of truth spreads across too many layers — if the article front matter, a JSON file, a CMS admin panel, and a build step all have opinions about what happened — then you end up with a system that is hard to reason about. You cannot trust the file anymore.

The ghostwriter should be visible but not magical. Git notes keep the magic out of the article.