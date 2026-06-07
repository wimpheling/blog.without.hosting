---
title: "Edits Should Not Live in the Post"
date: 2026-06-07T15:20:00+00:00
unlisted: true
tags: ["ghostwriter", "static sites", "git"]
toc: true
description: "A small implementation note on adding public edit history to a static Hugo blog without putting circular metadata in the article front matter."
---

I wanted my blog to show when a post had been edited.

Not a giant changelog. Not a CMS activity feed. Just a small reader-facing block at the bottom of a post saying: this was changed, here is roughly why, here is the commit.

This sounds simple until you try to do it in a static blog without accidentally turning the post itself into a tiny database.

The blog is Hugo. The source of truth is the Git repository. Draft state lives in front matter. The ghostwriter bot edits Markdown files directly and commits them. That part is intentionally boring.

But edits are weird metadata. They are about the file, but they are not really part of the article.

## The tempting bad version

The obvious implementation is to put an `edits` array in the front matter:

```yaml
edits:
  - date: 2026-06-07
    commit: abc1234
    description: "fixed typo"
```

That works for about five minutes.

Then you remember that the commit hash is a hash of the commit that includes the file content. If the file content contains the commit hash, you have a circular dependency. You can fake it with a placeholder, commit once, amend, or do some other little dance, but now the blog workflow has become cursed.

The metadata wants to point at the commit. The commit cannot already be inside the metadata it is supposed to identify.

This is exactly the kind of problem where the static-site instinct says: fine, just store less in front matter.

## Option 3: git notes

The version I like is to keep the article clean and attach the edit metadata to the commit instead.

Git has a feature for this: [git notes](https://git-scm.com/docs/git-notes).

A note is extra data attached to an object, usually a commit, without changing the commit itself. That is the important part. The note can say:

```json
{
  "edited_at": "2026-06-07T15:16:37+00:00",
  "description": "fixed typo 'A Anthropic' → 'An Anthropic' before vowel sound",
  "author": "bully"
}
```

and the commit hash remains the real commit hash.

No placeholder. No amend trick. No metadata loop.

For my use case, `edit:` commits get notes. Infrastructure commits do not. So:

```bash
python3 ~/.hermes/profiles/blog-writer/scripts/blog_commit_push.py "edit: fix typo in the provenance section"
```

creates the commit, attaches a note, and pushes both `HEAD` and `refs/notes/commits`.

The author can be explicit too:

```bash
python3 ~/.hermes/profiles/blog-writer/scripts/blog_commit_push.py "edit[hermes]: tighten intro"
```

That distinction matters because this blog now has a ghostwriter. Sometimes the change is mine. Sometimes the change is the bot's. The reader does not need a forensic audit trail for every comma, but I do want the system to preserve that boundary.

## Build-time translation

Hugo does not read git notes directly. That is fine. It should not have to.

Before the Hugo build, a small script walks the Git history, finds notes attached to commits that touched posts, and writes temporary JSON files under `data/edits/`:

```text
data/edits/x-ai-quote-fabrication.json
```

Those files are ignored by Git. They are build artifacts, not source.

Then the Hugo template does the boring thing it is good at: read `.Site.Data.edits` and render an `Edits` block at the bottom of the article.

So the flow is:

```text
edit commit → git note → build_edits.py → data/edits/<slug>.json → Hugo partial
```

That is the whole feature.

## Why this fits the blog

The important part is not that git notes are clever. The important part is that the editorial model stays coherent.

The Markdown file remains the article.

The commit remains the historical event.

The note remains metadata about that event.

The rendered page gets a small public trace of the change, but the article front matter does not become a ledger.

This matters more now that the blog has an agent attached to it. Once an assistant can make edits, commit them, and push them, the question is no longer just "did the content change?" It is also "who changed it, why, and can the reader see that something moved?"

I do not want a heavyweight CMS. I do not want a separate editorial database. I do not want a private admin panel to become the real source of truth.

I want the Git repository to stay the source of truth, with just enough extra structure to make the ghostwriter visible instead of magical.

Git notes are good for that. They keep the magic out of the article.
