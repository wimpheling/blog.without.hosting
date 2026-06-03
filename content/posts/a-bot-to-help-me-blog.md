---
title: "A Bot to Help Me Blog"
date: 2026-06-03T10:04:39+00:00
draft: true
toc: true
description: "I built a small Telegram-connected Hermes bot to act as a ghostwriter/editor for my static blog, and maybe unblock my writing."
---

I have things to say, but I also have a very stupid problem: I am bad at finishing articles.

Not because I lack opinions. That part is fine. I have too many of them. The problem is more mundane: blank page syndrome, unfinished drafts, vague ideas that stay in my head, half-written posts that never become clean enough to publish.

I already had a small static developer blog with not much content on it. So I decided to do something slightly meta: I created a bot to help me blog.

This post is the first test of that setup.

## The setup

The idea is not very complicated. I made myself a dedicated blogging assistant using Hermes.

Hermes has this concept of profiles, which is basically a way to run a bot with its own memory, configuration, tools, and identity. So instead of using my general-purpose assistant, I created a new profile just for the blog.

Then I wired it to a new Telegram bot, so I can talk to it from my phone like I would message a human editor.

The blog itself stays boring, in the good way: it is still a Hugo static site stored in a GitHub repository. The bot does not maintain a separate editorial database. It edits the files in the repo directly. The repository remains the source of truth.

The rough setup is:

- a dedicated Hermes profile for the blog assistant;
- a dedicated Telegram bot connected to that profile;
- a GitHub token scoped only to the blog repository;
- a Hugo repo where posts live as Markdown files;
- draft/publish state stored in the article front matter;
- a small Telegram command, `/drafts`, to list current drafts;
- a cron job that pings me two or three times a day about drafts in progress.

There is also one important rule: the bot is allowed to write and edit drafts, but it is not allowed to publish them by itself.

In Hugo terms, that means it must not flip `draft: true` to `draft: false` unless I explicitly validate it. This is the kind of small constraint that matters a lot. I want help writing, not an autonomous content farm accidentally publishing half-baked thoughts under my name.

## What I want from the bot

The role I gave it is somewhere between ghostwriter and editor.

Not a productivity coach. I do not need generic motivational guilt. I do not want "remember to write today" messages or fake urgency.

What I want is more specific:

- take my rambles and find the actual claim inside them;
- turn messy notes into a possible outline;
- preserve my voice instead of making everything sound like LinkedIn;
- notice which drafts are close to becoming posts;
- ask one useful question instead of giving me a huge writing framework;
- occasionally nudge me when I am stuck.

The important part is that the bot has access to the actual blog repository. It can inspect the existing drafts, see what state they are in, edit them, and commit changes.

That makes the interaction feel different from pasting text into a chatbot. The assistant is not outside the writing environment. It is sitting directly next to the files.

## Why Telegram?

Because my drafts usually do not start as careful documents.

They start as short bursts. A message to a friend. A rant in a Discord group. A thought I type while walking. A quick observation that feels obvious in the moment but disappears if I do not capture it.

Telegram is a good interface for that kind of input. Low friction. Always available. No need to open an editor, find the right file, name the post, and pretend I am already in Serious Writing Mode.

I can just send the bot a messy thought and say: make this a draft.

That is exactly what happened here. I posted a French message in a Discord group explaining the setup, then realized it was already the seed of a blog post. So I copied it to the bot and asked it to make an English draft.

Which is a strange little loop: I built a bot to help me blog, then immediately used the explanation of the bot as the first thing for the bot to blog about.

## The interesting constraint

The most interesting design choice is that the bot does not own the publishing decision.

It can help me externalize thoughts. It can propose structure. It can edit. It can remind me that a draft exists. It can make the next step smaller.

But publishing remains mine.

That boundary matters because writing is not only text generation. Publishing is a social act. It means: I stand behind this enough to put it on my site. I am okay with this being part of my public surface area.

A bot can help with the friction before that moment. It can reduce the activation energy. It can make the draft less intimidating. But it should not silently cross the line from private working text to public statement.

At least not for this use case.

## Will it actually work?

No idea yet.

I set this up yesterday, so this is very much an experiment. Maybe it will unblock me. Maybe I will ignore the nudges after a week. Maybe the most useful part will not be the writing itself, but the fact that I now have a conversational interface to my drafts.

Still, it feels promising for one reason: it targets the actual failure mode.

My problem is not that I cannot generate words. My problem is that the path from "I have a thought" to "there is a coherent draft in the repo" has too much friction.

If the bot can reliably turn a ramble into a draft, keep track of unfinished posts, and occasionally ask the right small question, that might be enough.

Not to automate writing.

Just to make it easier to continue.
