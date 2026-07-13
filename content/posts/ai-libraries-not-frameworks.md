---
title: "Build Your Own Framework (Now That AI Makes It Cheap)"
date: 2026-07-13T14:00:00+01:00
unlisted: true
tags: ["hot takes", "backspine"]
toc: false
description: "AI collapses the cost of producing code. That makes building your own project-specific framework the smart bet: maximally opinionated, no abstraction debt from generic conventions, and better output from AI coding agents."
---

AI makes producing code cheap. Really cheap. The marginal cost of a function, a module, a whole vertical slice collapses toward zero.

This changes one of the most fundamental tradeoffs in software architecture: the choice between adopting a generic framework and building your own.

The conventional wisdom was: use a framework because the cost of *organizing* code (routing, state management, build pipeline, testing conventions) dominates the cost of *writing* individual features. Batteries-included saves you from having to think about architecture.

But if the cost of writing code drops by an order of magnitude, the bottleneck shifts. It is no longer writing. It becomes *fighting abstractions that don't fit your problem*.

## Frameworks are pre-paid architecture

A generic framework is a bet. Someone else decided what routing should look like, how state flows through the system, where side effects belong, what patterns are idiomatic. If that bet aligns with your project, you win: zero architectural thinking, rapid output. If it doesn't — and it never aligns perfectly — you pay. Workarounds. Fighting the framework. Hooks that should be simple but aren't. Features that the framework makes hard because the framework author did not anticipate your use case.

Before AI, that tradeoff was often worth it. Writing your own routing + DI + state orchestration from scratch is expensive. You were buying the framework's conventions to avoid that cost, and you accepted the impedance mismatch as a smaller cost than building your own.

AI changes the relative prices. Building your own *relevant ad hoc set of invariants* — a thin layer of rules that serve your exact project, not a generalized framework for every project — becomes cheap. You write the orchestration once, in a few dozen lines of general code. An AI generates the actual feature code that plugs into it.

The cost of custom architecture collapses. The cost of fighting framework abstractions does not.

## The specificity advantage

When you design a framework for *everyone*, you have to lose specificity to cover the general case. The more projects you target, the more your conventions become watered-down compromises — hooks for this, overrides for that, extensibility points for things you cannot predict.

An ad-hoc project structure faces no such pressure. You can be aggressively opinionated:

- Ban entire categories of patterns that are technically valid but cause problems in *your* stack
- Enforce strict linting rules that would never make it into a shared standard
- Encode domain-specific constraints directly into the project skeleton — your `users` table has exactly this shape, authentication always goes through this middleware, all mutations follow this exact lifecycle

This is more rigid, which is good. Especially for AI.

## Why AI likes rigid conventions

An AI coding agent works best when the output space is constrained. Every ambiguity in the convention is a chance for the model to guess wrong — produce the wrong import path, the wrong lifecycle hook, the wrong error-handling pattern.

Your own framework is *maximally opinionated by construction*. There is exactly one way to add a route. Exactly one way to define a new API endpoint. Exactly one state management pattern. The AI does not need to choose between three competing approaches — it produces the right thing by default because the alternatives are structurally impossible.

Generic frameworks cannot do this. They need to support multiple ecosystems, multiple deployment targets, multiple schools of thought. Every option they support is one more way for an AI to produce wrong code.

## This extends to coding agents

The same principle applies to how you write the agents themselves. A coding agent is just code — it follows instructions, calls APIs, produces output. If you define your own agent-level conventions (prompt structure, tool selection rules, context format, output validation), you get the same specificity advantage. The agent's behaviour is constrained to what works for *your* project, not whatever the general-purpose agent prompt happened to optimize for.

Related: [coding agents are just code](https://blog.without.hosting/posts/coding-agents-are-just-code/).

## Even for large projects

The obvious pushback: "frameworks work well for large projects." And for very large projects, you have to build your own service orchestration anyway — the generic framework's conventions break at that scale every time. The question is whether the mid-sized project that used to be framework territory still needs one.

I think the answer is increasingly no. Not because frameworks are bad — they are excellent at what they optimize for — but because the cost of the fit gap is now higher than the cost of filling it yourself. The experienced developer knows this: even with excellent frameworks, you hit the structural limits quickly, and you spend more time finding workarounds than writing your own solutions. AI just makes the second option affordable for everyone.

## What this looks like

- Thin orchestration layer: 50–100 lines of plain code that compose library calls
- Powerful primitives — state management, HTTP, routing libraries that do one thing well
- No DI container, no config-driven state machine, no feature flags system
- Strict linting and structural conventions that leave no room for "AI guessed the wrong pattern"
- Every abstraction is justified by your actual project, not by what a framework vendor assumed

AI generates the feature code. You define the rules. The architecture stays flat, transparent, and editable.

## Backbone is this argument in code

I built a project template called [Backbone](https://github.com/wimpheling/backbone-template-v1) that is exactly what this post describes — a project-specific framework for a specific stack (Rust backend, React frontend, ConnectRPC, SQLite, Playwright) designed to work well with AI coding agents.

The template ships with custom lint rules that enforce architecture boundaries no generic framework would dare impose:

- **Rust (dylint):** `sqlx` calls only in database modules, environment variables only in configuration modules, each RPC method in its own file, `ConnectError` construction only through a central adapter, no HTTP clients outside integration modules, Axum endpoints only in rest modules.
- **React/TypeScript (oxlint plugin):** no direct imports from external UI libraries (MUI, Chakra, Antd, etc.) — all UI goes through the design-system boundary, no raw DOM JSX in app code — must use design system components, no direct `Error.message` access in catch blocks — must use the structured RPC error mapper. These rules would be absurd in a general-purpose framework. They make perfect sense when the framework is authored for *your* class of problems.

The README says it explicitly: *"AI coding agents are surprisingly good at working inside rigid systems. They are much less reliable when the project leaves every architectural choice open."*

This is not a thought experiment. The constraint-first approach is packaged, published (`npm create backbone-template`), and used for real projects. It is the argument this post makes, shipped as a template.

For the full project pitch: [Backspine — Project Presentation](https://blog.without.hosting/posts/backspine-presentation/).

*This constraint-first approach suggests a broader methodology for vibe coding. The follow-up post develops it: [three layers — invariants, structural content, and unstructured content — and what each means for AI generation](https://blog.without.hosting/posts/backspine-three-layer-architecture/).*