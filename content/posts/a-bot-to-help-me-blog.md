---
title: "A Bot to Help Me Blog"
date: 2026-06-03T10:04:39+00:00
draft: false
toc: true
description: "I built a Telegram-connected bot that can draft and edit my blog posts but cannot publish them. Hugo draft state is enforced by the tool, not trusted to my discipline."
tags: ["ghostwriter"]
---

I built a Telegram bot that can write and edit my blog posts but cannot publish them. Hugo `draft: true` is enforced by the tool, not trusted to my discipline.

The bot reads and writes files in the Hugo repo directly. No separate editorial database — the Markdown files are the source of truth. When a diff would flip `draft: true` to `draft: false`, the commit script refuses. There is an override (`ALLOW_PUBLISH=1`) but the bot cannot set it. Only I can, at a terminal.

## What it does

It can turn a ramble into a structured draft: take a messy paragraph from Telegram, extract the actual claim, propose an outline, write a first version. It edits existing posts, tightens paragraphs, fixes typos. It tracks changes via git notes — each edit commit leaves metadata that gets rendered as a reader-facing Edits block at the bottom of the post.

It answers on demand. `/drafts` lists current unlisted posts with their URLs. `/nudge` generates a writing prompt immediately. There is also a scheduled nudge: every 21 minutes during waking hours, the bot looks at what is sitting in the drafts folder and, if a slot is due, sends a short message about one of them. Not a reminder to write — a continuation of whatever that draft is about.

It researches. It can find papers on arXiv, extract text from PDFs, verify quotes against actual documents. It can generate SVG diagrams by hand and save them directly into the repo as image files. It has image generation via ComfyUI, access to Notion, Google Workspace, maps, and email.

It remembers across conversations. Past sessions are searchable. Subagents can be spawned for parallel work — for example, checking sources while drafting a section.

None of this is autonomous. Every action goes through git, and git has a guard. The bot cannot publish, cannot set the env var that would allow publishing, and cannot bypass the commit script.

## Why Telegram

My drafts rarely start as documents. They start as messages to a friend, a rant in a Discord group, a thought I type while walking. Telegram is always available and requires no friction — no editor, no filename, no structure decision before writing. I can send the bot a messy thought and say: make this a draft.

That is what happened here. I posted a French message in a Discord group explaining the bot, realized it was the seed of a blog post, copied it to the bot, and asked for an English draft. A strange loop: I built a bot to help me blog, then immediately used the explanation of the bot as the first thing for the bot to blog about.

## Voice risk

Bot-written text sounds correct and loses the rough edges that make a post feel like someone actually reasoned through it. That is a real risk. The compromise is that the bot does the restructuring and the grunt work, but the actual claims and the framing come from me. If the bot's voice dominates, the experiment failed. The style guidelines explicitly prevent over-polished prose and rhetorical slop — mechanism first, no editorial.

## What the experiment actually tests

Not whether the bot can write. It obviously can, in the same way an LLM can write anything — passably, at length, with medium confidence. The question is whether reducing the friction from "I have a thought" to "there is a coherent draft in the repo" changes my actual output over months.

The failure mode it targets is not writer's block. It is the gap between having a thought and committing it to a file. If the bot can reliably close that gap — turn rambles into drafts, keep track of unfinished posts, ask the right small question — that might be enough.

Not to automate writing. Just to make it easier to continue.