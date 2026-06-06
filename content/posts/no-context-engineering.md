---
title: "There Is No Context Engineering"
date: 2026-06-06T10:00:00+00:00
unlisted: true
toc: true
description: "A contrarian take on the term 'context engineering': it is a tautology, a sign of discipline immaturity, and a misleading frame. The right metaphor is not engineering — it is harnessing."
---

There is no context engineering.

"Context" and "prompts" are the same thing. Every input you feed your LLM is context. The system prompt is context. The user message is context. The retrieved chunk is context. The tool output is context. The conversation history is context. From the model's seat, there is only the next-token distribution over a token sequence. The boundary between "prompt" and "context" is editorial — it lives upstream, in the human's head, and it disappears the moment inference starts.

## Bateson said it first

Gregory Bateson saw this structure — not about LLMs, but about mammals at play. In a 1955 essay called *A Theory of Play and Fantasy*, he watches two young animals roughhousing.

They nip each other. The nip looks like a bite, sounds like a bite, resembles a bite in every observable way. But it is not a bite. The other animal does not flinch, flee, or retaliate. They keep playing.

Why? Because both animals are communicating on two levels simultaneously. One level: the action. The other level: a message *about* the action. Bateson called this **metacommunication**:

> "The other set of levels of abstraction we will call metacommunicative (e.g., 'My telling you where to find the cat was friendly,' or 'This is play'). In these, the subject of discourse is the relationship between the speakers."

The metacommunicative message — "this is play" — tells the receiver how to interpret the action. The same gesture, without that frame, would be aggression. With the frame, it is play.

And here is the line that matters:

> "The playful nip denotes the bite, but it does not denote what would be denoted by the bite."

The nip carries two meanings simultaneously: the denotative content (a bite-like action) and the metacommunicative frame (this is not a real bite). The frame is not separate from the action. The frame *is* the action, at a higher logical type. There is no "bite" without "this is play" layered on top. There is no content without context. They are the same emission.

This is exactly what happens in an LLM prompt. Every token you put in the window carries information at multiple levels: the denotative content (the instruction, the user question, the fact) and the metacommunicative frame (system prompt, role assignment, preceding conversation, retrieved context, tool outputs). From the model's seat, these are all just tokens in a sequence. The boundary between "prompt" and "context" is editorial. The transformer does not see a system prompt versus a user message versus a RAG chunk. It sees a sequence of tokens and predicts the next one.

## The paradox

There is a contradiction sitting in the open. I said "there is no context engineering," then spent the last section arguing that everything is context. If everything is context, then you are *always already* engineering context. The term is not false. It is not even misleading.

It is empty.

"Context engineering" claims the discovery of something that has always been true of every communication since the first mammal nipped another and the nip was understood as play. Every message carries its own context. Every frame is a message at a higher logical type. There is no "outside" the frame. There is no input that is not already contextualized by every other input in the window. The term sounds like a new discipline but describes a structural constant. It is a tautology dressed as innovation.

That is the real problem with the label. Not that it is wrong — but that it signals novelty where none exists, and in doing so, reveals how young the field still is.

## "Noyer le poisson"

So why keep using the label? My read: it is *noyer le poisson* — muddying the waters. The term lets a young discipline dress up an old practice in fresh vocabulary. It signals novelty without actually being novel. And it reflects the level of immaturity of the field: we are still inventing job titles for things we have been doing for three years.

The proof is in the speakers. When someone says "context engineering" at a conference, ask them what part of their work was not already prompt engineering in 2023. The honest answer, almost always, is "the retrieval pipeline" or "the memory layer" or "the tool router." Those are real engineering concerns. They are not new. And they are not "context" in some special sense — they are just more input, assembled upstream of the same old next-token prediction.

## The reframe: we are not engineering, we are harnessing

**[USER: write the harnessing section here — this is the load-bearing reframe of the post. The metaphor matters. Engineering implies a stable material you shape. Harnessing implies a powerful, partially understood force you direct. LLMs are the second kind.]**

## Three harnesses, one job

**[USER: write the spectrum here — CEO/CTO (predictable) → artist (generative) → consciousness-curious (different destination, same harness).]**

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