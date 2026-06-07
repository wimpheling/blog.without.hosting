---
title: "A Bot to Help Me Blog"
date: 2026-06-03T10:04:39+00:00
draft: false
toc: true
description: "I built a Telegram-connected bot that can draft and edit my blog posts but cannot publish them. Hugo draft state is enforced by the tool, not trusted to my discipline."
tags: ["ghostwriter"]
---

I built a Telegram bot that can write and edit my blog posts but cannot publish them. Hugo `draft: true` is enforced by the tool, not trusted to my discipline.

The bot reads and writes files in the Hugo repo directly. No separate editorial database — the Markdown files are the source of truth, the commit history is the edit log, and `draft: true` (or `unlisted: true`) is a hard gate.

When the commit script sees a diff that would flip `draft: true` to `draft: false`, it refuses. There is an environment variable to override it — `ALLOW_PUBLISH=1` — but the bot cannot set that. Only I can, and only when I am sitting at a terminal reviewing the change.

The concrete setup:

- the bot has its own Hermes profile with blog-specific memory and tools;
- a dedicated Telegram bot is the interface — I dm it from my phone;
- the GitHub token is scoped to the one repo;
- drafts sit in the repo as Markdown, visible at their URL but hidden from lists;
- a cron job sends two or three nudges a day, re-surfacing dormant drafts in a conversational way.

## Why Telegram

My drafts rarely start as documents. They start as messages to a friend, a rant in a Discord group, a thought I type while walking. Telegram is low-friction and always available — no need to open an editor, name the file, decide on a structure before writing anything.

I can send the bot a messy thought and say: make this a draft.

That is what happened here. I posted a French message in a Discord group explaining the bot, realized it was the seed of a blog post, copied it to the bot, and asked for an English draft. A strange loop: I built a bot to help me blog, then immediately used the explanation of the bot as the first thing for the bot to blog about.

## Voice risk

Bot-written text sounds correct and loses the rough edges that make a post feel like someone actually reasoned through it. That is a real risk. The compromise is that the bot does the restructuring and the grunt work, but the actual claims and the framing come from me. If the bot's voice dominates, the experiment failed.

## What the experiment actually tests

Not whether the bot can write. It obviously can, in the same way an LLM can write anything — passably, at length, with medium confidence. The question is whether reducing the friction from "I have a thought" to "there is a coherent draft in the repo" changes my actual output over months.

The failure mode it targets is not writer's block. It is the gap between having a thought and committing it to a file. If the bot can reliably close that gap — turn rambles into drafts, keep track of unfinished posts, ask the right small question — that might be enough.

Not to automate writing. Just to make it easier to continue.