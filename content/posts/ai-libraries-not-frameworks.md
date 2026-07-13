---
title: "Libraries, Not Frameworks: The AI Tax on Batteries-Included"
date: 2026-07-13T14:00:00+01:00
unlisted: true
tags: ["hot takes", "backspine"]
toc: false
description: "AI makes code generation nearly free. That changes the economics of framework vs. library choice: one-size-fits-all abstractions become a tax you can no longer justify."
---

AI makes producing code cheap. Really cheap. The marginal cost of a function, a module, a whole vertical slice collapses toward zero.

This changes one of the most fundamental tradeoffs in software architecture: the choice between frameworks and libraries.

The conventional wisdom has been: use a framework for medium-to-large projects because the cost of *organizing* code (routing, DI, lifecycle, state management) dominates the cost of *writing* code. Batteries-included saves you from having to think about architecture.

But if the cost of writing code drops by an order of magnitude, that calculus flips. The bottleneck is no longer writing. It becomes *fighting abstractions that don't fit your problem*.

## Frameworks are pre-paid architecture

A framework is a bet. Someone else decided what routing should look like, how state flows through the system, where side effects belong. If that bet aligns with your project, you win: zero architectural thinking, rapid output. If it doesn't — and it never aligns perfectly — you pay. Workarounds. Fighting the framework. Hooks that should be simple but aren't. Features that the framework makes hard because the framework author did not anticipate them.

Before AI, that tradeoff was often worth it. Writing your own routing + DI + state orchestration from scratch is expensive. You were buying the framework's conventions to avoid that cost, and you accepted the impedance mismatch as a smaller cost than building your own.

AI changes the relative prices. Building your own *relevant ad hoc set of invariants* — a thin layer of rules that serve your exact project, not a generalized framework for every project — becomes cheap. You write the orchestration logic once, in thirty lines of general code. An AI generates the library calls that connect to it.

The cost of custom architecture collapses. The cost of fighting framework abstractions does not.

## AI favors composition

AI models produce better code from powerful libraries than from opinionated frameworks. Why? Because libraries are compositional: they expose primitives that combine freely. The AI can call `map`, `filter`, `reduce`, `useEffect`, `fetch`, `addEventListener` — general computing primitives — and orchestrate them with plain logic. The result is idiomatic, minimal, and correct.

Frameworks ask the AI to produce code *against a convention*. The AI needs to understand not just what the code should do, but how the framework expects it to be expressed. It needs to produce the right decorator, the right lifecycle hook, the right config key. When the framework's mental model diverges from the AI's training distribution — and it will, because frameworks are moving targets and LLMs train on snapshots — the output gets weird. Boilerplate. Wrong abstractions. Code that compiles but smells.

This is not a theory. Anyone using LLMs for real-world coding has felt the difference between asking it to "use lodash" and asking it to "implement an Angular service." The first produces clean, idiomatic code. The second produces code that looks like someone read the docs once and guessed.

## Even for small projects

The interesting implication: this shift applies even to small projects. The old heuristic was "small project → libraries, large project → framework." But the price floor for building your own orchestration is now so low that the framework threshold moves. Maybe it disappears entirely.

I am increasingly convinced that a small, well-chosen set of powerful libraries + plain orchestration logic beats any framework for most projects. Not because frameworks are bad — they are excellent at what they optimize for — but because the cost of the fit gap is now higher than the cost of filling the gap yourself.

The experienced developer knows this already: even with excellent frameworks, you hit the structural limits quickly. You spend more time finding workarounds for the framework's logic than you would writing your own. AI just makes the second option affordable.

## What this looks like in practice

- Thin orchestration layer: 50–100 lines of plain code that compose library calls
- Powerful primitives: lodash, React hooks, native fetch, Zustand — things that do one thing well
- No DI container, no lifecycle manager, no config-driven state machine
- Every abstraction is justified by your actual project structure, not by what the framework assumes

AI generates the calls. You define the composition rules. The architecture stays flat, transparent, and editable.

[USER: write — the actual experience of this approach with Backspine or another project, concrete example of a framework fight that went away when switching to library + orchestration.]