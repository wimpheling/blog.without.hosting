---
title: "Stop Reading What Your Coding Agent Says"
translationKey: "backspine-dont-read-agent-text"
date: 2026-06-18T10:36:22+00:00
tags: ["backspine", "hot takes"]
toc: true
description: "Coding agents are here to produce code, not chatter about it. The textual output is noise, and evaluating what the agent says instead of what it implements creates a bad feedback loop."
---

Stop reading what your coding agent says. Read what it produces.

Coding agents are here to produce code. Not chatter about it. The textual output — the stream of "I'll fix this by doing X, then Y, then Z" — is noise.

## The bad feedback loop

Instead of evaluating the agent's output (the code, the diff, the structural changes), you evaluate what it tells you about its output. The agent sounds confident. You approve. The code is wrong.

> "Every agent in production lies. We measured it. The good ones lie less, the great ones catch the lie before the user does."
> [(apocryphical quote from the dead internet)](https://blog.without.hosting/posts/x-ai-quote-fabrication/)

The "we measured it" part is what makes the line land. The structural point holds regardless of who said it: if an agent sounds confident, the confidence should not be mistaken for correctness. The rest of your team's review process should treat the agent's prose as a variable, not a fact.

This is the same dynamic as the "thinking" token phenomenon. At first, we loved watching it live on DeepSeek — peeking into the model's "reasoning." Now most of us hide it. It was additive for about a week, then became noise.

But the full coding agent UI is noise of the same kind. A wall of streaming text about what the agent *intends* to do, while the actual code changes scroll past in the same feed, indistinguishable from the chatter.

## The performative assistant

The chatbot interface is not neutral. It is a scene.

Just like the ["performative male"](https://knowyourmeme.com/memes/performative-male) became a recognizable aesthetic of staged sensitivity, the chatbot assistant is a staged version of what geek culture imagined a sci-fi assistant would be: endlessly helpful, emotionally available, slightly sycophantic, always ready to explain itself, always performing competence.

It cosplays the childhood fantasy of the nice best helpful friend inside the machine.

That fantasy is understandable. A lot of us grew up wanting this. The computer that talks back. The robot sidekick. The assistant who never gets tired, never judges, and always wants to help.

But coding is where the fantasy becomes expensive. The performance of helpfulness competes with the actual work. The assistant narrates intention, reassurance, apology, plan, and fake humility — while the artifact remains the only thing that matters.

The problem is not that the assistant has a personality. The problem is that the personality becomes the interface.

## The surface is the output

The surface of a coding agent should be the code. Not a chat about the code. Not a plan for the code. Not a summary of the code.

The code *is* the interface. The diff *is* the presentation layer. The artifact review *is* the conversation with the agent.

Everything else — the thinking tokens, the plans, the "I'll fix this by doing X" — is commentary on the work, not the work. And the more of it you read, the less you actually look at what was produced.

Stop reading what your coding agent says. Read what it produces.
