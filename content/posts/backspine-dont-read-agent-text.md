---
title: "Stop Reading What Your Coding Agent Says"
date: 2026-06-07T00:40:00+00:00
unlisted: true
tags: ["backspine", "hot takes"]
toc: true
description: "Coding agents are here to produce code, not blabla about it. The textual output is noise, and evaluating what the agent says instead of what it implements creates a bad feedback loop."
---

Stop reading what your coding agent says. Read what it produces.

Coding agents are here to produce code. Not blabla about it. The textual output — the stream of "I'll fix this by doing X, then Y, then Z" — is noise.

## The bad feedback loop

Instead of evaluating the agent's output (the code, the diff, the structural changes), you evaluate what it tells you about its output. Research has shown that what agents actually implement does not necessarily match the discourse they have about it. The agent sounds confident. You approve. The code is wrong.

This is the same dynamic as the "thinking" token phenomenon. At first, we loved watching it live on DeepSeek — peeking into the model's "reasoning." Now most of us hide it. It was additive for about a week, then became noise.

But the full coding agent UI is noise of the same kind. A wall of streaming text about what the agent *intends* to do, while the actual code changes scroll past in the same feed, indistinguishable from the blabla.

## The counter-argument

"But there's too much code output. The AI's verbal explanation is the only usable presentation layer."

That's exactly the problem. The presentation layer *happens* to be LLM-generated text because no one designed a real one. The agent talks because that's the default mode of the tool — it speaks. Not because speech is the right interface for code review.

## The thesis

We need a presentation layer that is not created by an LLM. Or barely.

What that means:

- **Define structural elements.** Present changes in the clearest possible form — a real research field, not an afterthought.
- **Code lives in islands** inside structural elements. Not in a linear stream of text. Isolated, scoped, reviewable. ([draft: backspine code islands])
- **The UI should surface structural changes semantically.** You should see what changed at the architecture level, not the token level. And be able to zoom in on a particular implementation when you need to. ([draft: backspine structural changes semantic])

Shameless self-promotion: I'm working on the answer. Backspine is that answer, or at least the attempt at it.
