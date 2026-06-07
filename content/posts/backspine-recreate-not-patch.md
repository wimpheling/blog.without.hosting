---
title: "Backspine — Recreate, Don't Patch"
date: 2026-06-07T01:10:00+00:00
unlisted: true
tags: ["backspine", "hot takes"]
toc: false
description: "LLM coding is not a conversation. It's a compile step. Every prompt should add to the spec, not patch the output. Partial recompilation via code islands is the only scalable architecture."
---

People often compare LLMs to compilers. The analogy has merit: both take a high-level input and transform it into executable code. Both have quirks around non-determinism (as anyone who's fought a flaky compiler flag will tell you).

But we miss the critical implication.

When you compile, you recompile from the *specification* every time. You don't compile once, then patch the binary on every edit. You change the source, recompile, and the compiler enforces consistency by having no memory of the previous binary.

LLM coding does the opposite. The dominant paradigm is the chat window — a long conversation where the LLM accumulates "context" like a patched binary accumulates cruft. You correct, it adjusts. You change your mind, it pivots. Every message carries the ghost of every previous misunderstanding, bad assumption, and abandoned direction.

This is patch culture. And it's wrong.

**The fix: every prompt should be added to the prompt.**

Not to the conversation. To the specification. If you discover a constraint while debugging, it goes into the spec, not into the chat history. If you realize a design choice was wrong, the spec changes, not the next message. The LLM's context should *be* the spec, not the editing session.

Every constraint you discover during iteration is permanent. The chat treats it as ephemeral — expressed once, forgotten when scrolling context pushes it out. The spec treats it as durable. There is no "context engineering." There is spec maintenance.

## The PR problem

Apply this to a pull request or a new feature. The process is the same: you give the LLM a diff, it generates code. You iterate. Drift accumulates.

The radical conclusion: if the spec *is* the source of truth, then shouldn't a PR be just a spec change? Shouldn't we just merge the spec diff and let the LLM rebuild the application from scratch?

Yes. And no.

The "yes" is correct in principle. A spec change *should* induce a full recompile. Every constraint is re-asserted, every architectural invariant re-verified. No legacy decisions leak through because the LLM has no memory of the previous implementation. The result is strict conformance to the spec, every time.

The "no" is practical. Full application recompilation doesn't scale. Even if the LLM is fast, re-generating an entire codebase on every spec change is wasteful, expensive, and unpredictable. The binary analogy breaks here — we don't need to re-link every library when one function changes.

## Partial recompilation via islands

This is where the [code islands](blog.without.hosting/posts/backspine-code-islands/) pattern becomes the linker.

An island is a bounded, self-contained module with:
- A defined spec (the island's contract)
- Stable structural context (the architecture, the imports, the parent system)
- Regeneratable content (the business logic inside the island)

When the spec changes, the agent identifies which islands are affected, regenerates only those islands, and validates that the structural invariants hold. The rest of the codebase stays untouched, not because we "preserved" it, but because the spec change didn't touch it.

This is selective recompilation. The LLM is the compiler. The islands are the compilation units. The spec is the source code.

The practical constraint is dependency resolution: does island A depend on island B's implementation or just its interface? If the latter, B can be regenerated independently. If the former, both need recompilation. A well-designed island graph has strict interface boundaries — just like a well-designed software project.

## What recompilation means in Backbone v1

In the actual Backbone template, "recompile the app" should not mean asking an LLM to rewrite the entire repository from a chat transcript.

The code already suggests smaller compilation targets:

- a page component with typed static and dynamic props;
- a route adapter that binds state to the page;
- a Zustand store for client state and RPC calls;
- a design-system contract and implementation boundary;
- backend migrations and RPC modules;
- Gherkin + Playwright behavior tests.

So the realistic Backspine move is: fold corrections back into the feature spec, then regenerate or patch the bounded slice that owns that behavior. The island is the compilation unit. Tests, stories, lint rules, and contracts are the linker.

[USER: expand — go find the X thread about LLM-as-compiler non-determinism for the reference. Also articulate: what breaks this model? When do constraints conflict and make regeneration oscillate? Is the island linker a human role or can it be automated?]
