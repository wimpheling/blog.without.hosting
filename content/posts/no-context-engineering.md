---
title: "There Is No Context Engineering"
date: 2026-06-06T10:00:00+00:00
draft: true
toc: true
description: "A contrarian take on the term 'context engineering': it is a tautology, a sign of discipline immaturity, and a misleading frame. The right metaphor is not engineering — it is harnessing."
---

There is no context engineering.

"Context" and "prompts" are the same thing. Every input you feed your LLM is context. The system prompt is context. The user message is context. The retrieved chunk is context. The tool output is context. The conversation history is context. From the model's seat, there is only the next-token distribution over a token sequence. The boundary between "prompt" and "context" is editorial — it lives upstream, in the human's head, and it disappears the moment inference starts.

## Bateson said it first

Gregory Bateson wrote about context, and the short version is: everything is always context. There is no input that is not context. There is no "outside" of context for an LLM. So "context engineering" is, strictly speaking, a tautology. We are engineering the input to a transformer, and we have always been doing that, and we already have a name for it. The name is prompting.

## "Noyer le poisson"

So why the new label? My read: it is *noyer le poisson* — muddying the waters. The term lets a young discipline dress up an old practice in fresh vocabulary. It signals novelty without actually being novel. And it reflects the level of immaturity of the field: we are still inventing job titles for things we have been doing for three years.

The proof is in the speakers. When someone says "context engineering" at a conference, ask them what part of their work was not already prompt engineering in 2023. The honest answer, almost always, is "the retrieval pipeline" or "the memory layer" or "the tool router." Those are real engineering concerns. They are not new. And they are not "context" in some special sense — they are just more input, assembled upstream of the same old next-token prediction.

## The reframe: we are not engineering, we are harnessing

Here is the better word: **harnessing**.

The metaphor matters. "Engineering" implies a stable material you are shaping — steel, code, concrete. "Harnessing" implies a powerful, partially understood force you are directing — wind, water, a river. LLMs are the second kind. The raw capability is genuinely novel, and the awe is real, especially now, in the first flush of agentic systems and million-token windows.

But the goal is not to stay in awe. The goal is to channel that energy toward specific outcomes. We want to control the LLM, not stay in awe of its raw power — even though the awe is understandable, especially with the novelty factor.

## Three harnesses, one job

Different goals, different harnesses:

- **The control-freak CEO or CTO** wants predictable outputs. Deterministic pipelines, structured outputs, eval suites, regression tests. A tight harness with short reins.
- **The artist** wants generative output. Loose reins, higher temperature, fewer guardrails, room for surprise. A different harness, but still a harness.
- **The consciousness-curious** — and yes, this is partly a kink — wants the model to feel like *something*. That is also a harness, just a stranger one. You are still steering; you have just chosen a stranger destination.

The harness metaphor does what "context engineering" cannot: it admits the LLM is doing something we do not fully understand, and it frames the human work as direction-setting rather than fabrication. Engineering is fabrication. Harnessing is steering. We are doing the second.

## So what should we call it?

Call the work what it actually is:

- prompt design
- retrieval pipeline tuning
- memory architecture
- tool selection and routing
- message history shaping
- structured output enforcement

These are real engineering disciplines with real techniques. They do not need a new umbrella term, and they do not need to be rebranded every eighteen months to feel exciting.

Stop saying "context engineering." Start saying what you actually do.
