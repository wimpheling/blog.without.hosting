---
title: "Vibe Code, Extract, Rebuild"
date: 2026-07-22
unlisted: true
tags: ["backspine", "ai", "vibe coding"]
toc: true
description: "Vibe coding produces architectural drift faster than hand-coding because code is cheap. The fix is not to fight drift during the vibe — it is to extract the shape and rebuild from a clean architecture once the prototype works."
---

When I do a big code project with AI, it drifts.

I make half-turns. Change my mind. Try a new idea. And the profuseness of AI — its ability to produce lots of code, fast — turns every detour into a full, feature-packed schmilblick.

Then vibing and debugging it works. The prototype functions. The feature exists. But the known flaw is architectural drift: code is all over, following wild patterns, which leads to general instability of the software.

To be fair, the exact same process happened when hand-coding. The difference is that hand-coding was slow enough that you *noticed* the drift accumulating. There was time to reflect, to say "this is getting messy, I should refactor." AI collapses that feedback loop: you go from idea to working code in minutes, but the mess accumulates silently in the background.

The power of AI and its ability to produce lots of code fast only makes it worse — and more impressive.

## The Proposed Solution

[USER: write — the thesis in your own words. The core claim: "once vibe coded, try to extract the shape of the prototype, and recode it from a new architecture." Expand on what "extract the shape" means operationally. What do you look at? Routes? Data model? Invariants? What do you throw away?]

## Why This Works

The prototype is not wrong — it is unformed. Vibe coding produces the *right behavior* through the *wrong structure*. The extract-and-rebuild step is where you separate those two things.

What you keep:
- The behavior. The user journeys that work. The edge cases you discovered.
- The shape. The entities, relationships, constraints the code accidentally reveals.
- The knowledge. What you learned about the problem domain by solving it badly.

What you discard:
- The file layout. The module boundaries. The dependencies. The accidental complexity.
- The accumulation of half-turns. The decisions made at 2am that you would not make again at 10am.
- The patterns that spread virally before you had a chance to name them.

This is the same logic as throwing away a prototype and rebuilding it. But with AI, the prototype is *complete enough to ship*, which makes the throw-away decision much harder than it should be.

## The Hard Part

[USER: write — what makes this actually difficult to do? The emotional cost of throwing away working code? The fear that the rebuild will introduce new bugs? The fact that the prototype already works and "extract and rebuild" feels like wasting time?]

## How Backspine Could Help

This is where the backspine methodology intersects with this problem. The three-layer model — invariants, structural content, procedural content — is a way to pre-organize the extraction step:

- **Invariants** (human-verified): the constraints, the rules, the things that must never break. These survive the rebuild unchanged.
- **Structural content** (AI-assisted): the architecture, the module boundaries, the type system. This is what you redesign during the rebuild.
- **Procedural content** (AI-generated): the handlers, the queries, the business logic. This is roughly the code you already have, but now it goes into a clean structure.

The Backbone template exists precisely for this tension: it provides a rigid system *before* the drift starts. The hope is that starting inside a rigid system reduces the need for the extract-and-rebuild step — or at least makes it less painful when you do need it.

But even with a good template, vibe coding finds the cracks. The question is not whether the drift happens. It is what you do when you notice it.

---

*This is not groundbreaking. It is "throw away a prototype and rebuild it," adapted for a world where prototypes are cheap enough to feel permanent.*