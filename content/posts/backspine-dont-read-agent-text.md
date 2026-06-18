---
title: "Stop Reading What Your Coding Agent Says"
date: 2026-06-07T00:40:00+00:00
unlisted: true
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

## The counter-argument

"But there's too much code output. The AI's verbal explanation is the only usable presentation layer."

That's exactly the problem. The presentation layer *happens* to be LLM-generated text because no one designed a real one. The agent talks because that's the default mode of the tool — it speaks. Not because speech is the right interface for code review.

## The thesis

We need a presentation layer that is not created by an LLM. Or barely.

What that means:

- **Define structural elements.** Present changes in the clearest possible form — a real research field, not an afterthought.
- **Code lives in islands** inside structural elements. Not in a linear stream of text. Isolated, scoped, reviewable. ([draft: backspine code islands])
- **The UI should surface structural changes semantically.** You should see what changed at the architecture level, not the token level. And be able to zoom in on a particular implementation when you need to. ([draft: backspine structural changes semantic])

Shameless self-promotion: I'm working on the answer. [Backspine](https://blog.without.hosting/posts/backspine-presentation/) is my answer, or at least the attempt at it.
