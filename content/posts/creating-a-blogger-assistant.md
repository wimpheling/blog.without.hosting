---
title: "Creating a Blogger Assistant"
date: 2026-06-07T01:05:00+00:00
unlisted: true
tags: ["blog", "ai", "self-hosting"]
toc: true
description: "A self-hosted blogging assistant should combine static-site performance, browser editing, and agent-assisted writing while keeping every meaningful change committed to git."
---

The thing I want is not exactly a CMS.

A CMS assumes the website is the application. You log in, write content, click publish, and the CMS owns the state. That is fine if you want WordPress. It is not what I want.

I want a static blog that keeps the core properties of a static blog:

- fast pages
- cheap hosting
- no database in the public path
- git as the source of truth
- readable markdown files
- deploys I can reason about

But I also want the editing experience of a modern application.

I want to open a post and edit it directly. I want a chat window on the right. I want to say: "make this sharper", "move this paragraph up", "this section is bullshit, find the real claim", and have the assistant edit the document with me.

Not generate a blob in a separate chat. Edit the thing.

## Static generation plus admin mode

The public blog should remain static. That is the whole point. Readers should get pre-rendered HTML from a CDN. No app shell, no login system, no dynamic server deciding how to render an article.

But the author should have an admin mode.

Something like:

`/admin/posts/creating-a-blogger-assistant/`

or even:

`/posts/creating-a-blogger-assistant/?edit=1`

In read mode, the page is static. In admin mode, the same content becomes editable. The markdown appears behind the rendered article. Sections can be clicked. The assistant can see the document structure and propose edits against it.

This is the split I care about: static for readers, dynamic for the writer.

## Inline editing and agent editing

There are two editing modes, and they should coexist.

The first is inline editing. Click a paragraph, change the sentence, save. This is the obvious CMS feature.

The second is agent editing. Select a section, ask the assistant to rewrite it, and inspect the diff. Or ask it to restructure the whole post. Or give it a ramble and let it place the new idea in the right draft.

The assistant should not be a separate chatbot that occasionally produces markdown to copy-paste. It should be inside the editing surface. The chat window is not the product. The document is the product.

The chat is a control surface for editing the document.

## The git problem

Every meaningful change should be committed.

That sounds simple until you try to reconcile it with live editing. If every keystroke becomes a commit, the history becomes garbage. If edits are only committed manually, the system starts behaving like a normal CMS with hidden transient state. If the assistant edits a paragraph five times before the user accepts it, which version is the commit?

There is a real tension here.

Git wants discrete snapshots with intention. Live editing wants continuous mutation. Agent editing wants speculative branches: try this rewrite, reject it, try another one, keep half of it.

A good blogger assistant probably needs three layers:

1. **Working state** — local/browser/server-side draft mutations that are not yet canonical.
2. **Accepted edits** — user-approved changes to the markdown file.
3. **Committed history** — meaningful checkpoints with human-readable commit messages.

The commit should not necessarily happen on every input. It should happen when an edit becomes semantically stable: "expand blogger assistant draft", "rewrite admin mode section", "publish creating a blogger assistant".

This means the assistant needs to understand not just text editing, but editorial intent.

## Self-hosted, not SaaS-first

I do not want the core system to depend on a proprietary CMS database.

The stack should be boring:

- Hugo or another static site generator
- markdown files in git
- an admin UI
- a small authenticated backend for edits
- an LLM assistant with access to the repo
- commits pushed to the main branch
- static deploy after each accepted checkpoint

The public surface stays dumb. The authoring surface can be smart.

This is not because self-hosting is aesthetically pure. It is because the blog itself should remain portable. If the assistant disappears, the content should still be there as markdown files and git history.

## The actual product

The product is not "AI writes blog posts".

The product is a writing environment where the blog is the source of truth, the assistant is aware of the blog, and every interaction moves the actual artifact forward.

A right-side chat window is useful only if it can edit the post, search related drafts, preserve voice, and commit changes.

Otherwise it is just ChatGPT with extra steps.

[USER: expand — what should the first prototype be? Decap-style CMS with an AI sidecar? A custom admin route? How do we handle auth, diffs, and commit grouping without rebuilding WordPress badly?]
