---
title: "Backspine — Recreate, Don't Patch"
date: 2026-06-07T01:10:00+00:00
unlisted: true
tags: ["backspine", "hot takes"]
toc: false
description: "To avoid drift, recreate the whole implementation as specs change. Incremental patching accumulates inconsistencies; regeneration enforces specification conformance."
---

To avoid drift, recreate the whole implementation as specs change.

Incremental patching is the default mode of coding agents: take the existing codebase, understand what changed in the spec, and apply a surgical edit. This is how humans work. It is not how agents should work.

Every patch carries the ghost of every previous patch. The codebase accumulates structural inconsistencies — a variable name choice here, a pattern established there, an assumption baked into the first implementation that the third patch didn't know about. The LLM does not have a mental model of the codebase's accumulated idiosyncrasies. It has the current state in context, a diff to the spec, and a prompt to "preserve everything else." Drift is inevitable.

The alternative: recreate from spec.

When the spec changes, the agent regenerates the full implementation from scratch, constrained by the spec and the structural elements. No legacy decisions leak through. Every regeneration is an opportunity to enforce consistency — the same patterns, the same conventions, the same architecture, because the spec and structural model enforce them.

This only works if:

- **The spec is the source of truth.** Not the code. If you're patching spec violation drift, you've already lost.
- **Structural elements are stable.** The code lives in islands ([code islands](blog.without.hosting/posts/backspine-code-islands/)) within a defined architecture. Regeneration replaces island content, not the structure.
- **Regeneration is cheap.** If recreating an island costs seconds, you do it on every spec change. If it costs minutes, you think twice and drift creeps back in.

Counter-argument: "This throws away working code." Yes. That is the point. Working code that matches an outdated spec is a liability, not an asset. The goal is not to preserve code. The goal is to preserve conformance to the spec.

[USER: expand — when does this break? When is patching actually the right answer? What's the boundary condition where regeneration becomes wasteful?]
