---
title: "No Prompt, Just Linters"
date: 2026-06-06T23:00:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "Two composition rules enforced by custom linters — and an AI code generator that started managing its own design system without a single prompt about it."
---

AI code generators produce unstructured slop easily when it comes to UI. Ask one to build a page and it will generate a unique constellation of divs with raw Tailwind classes — different spacing, different layout, slightly different everything — every single time. The same conceptual element rendered twelve ways across twelve files because there is no structural reason not to. The token cost of inlining is zero. The cost of composing is non-zero. The AI optimizes for token cost.

This is not a prompting problem. You cannot ask an AI to "be consistent with components" and expect it to work — the incentive is wrong. The AI will agree and then inline everything anyway, because that is what token optimization looks like at the generation step.

The fix is structural: make the wrong thing impossible.

I built two lint rules:

1. **Components** can contain HTML, CSS, and raw JSX elements.
2. **Pages** cannot. Pages compose components and nothing else.

Ten minutes, custom linters written by the same agent that was writing the code. No prompt about design system discipline, no "please follow this pattern" in any instruction file. Just two rules that fail the build if a page tries to use a bare `div` with inline styles.

And the agent adapted.

## The Emergent Behavior

The agent stopped slopping. It started checking the component library before creating new elements. When a component almost worked, it extended it rather than spawning a sibling. It composed pages from existing pieces with a limited grammar of UI elements.

This was not an accident — it was the expected result. The constraints were designed to flip the cost surface. Before the linters, the cheapest token path was to inline everything. After the linters, the cheapest path is the correct one: raw HTML in a page means a build failure, which means a regeneration cycle, which costs more tokens than doing it right the first time. The agent adapted because it had no cheaper option.

The design system emerged from constraints, not from documentation. Components are few and general. Pages are compositions. Visual consistency is not the result of a curated palette or a spacing scale — it is the mechanical consequence of the same small set of components rendering everything. The grammar of available elements is small. The output is coherent.

## The Enforcement

The linters themselves are trivial. They check two things:

- Does a file outside the components directory contain JSX elements that map to raw HTML tags (`div`, `span`, `input`, etc.)? Fail.
- Does a file outside the components directory import CSS modules or use inline styles? Fail.

That covers the surface. The linter was written by the agent in ten minutes. The code generator built the fence that keeps itself in check.

The linters run on every file save during development and as part of the build step. When a page tries to use a raw `div` with inline styles, the build fails. The agent gets a lint error and self-corrects. It does not override the linter — it composes differently.

This is the part that still feels like it should not work: the agent wrote its own constraints. But it works because the constraints are structural, not rhetorical. The linter does not say "please consider using a component." It says `exit code 1`. There is no negotiation.

## The Implementation

The package structure behind this is straightforward. A contract package (`design-system-contract`) defines typed component APIs. A basic implementation (`design-system-basic`) provides React components plus CSS. A facade package (`design-system`) exposes the public import surface. The linters sit at the top of this stack.

The same architecture maps onto a React Native client currently in progress. The same contract, the same linters, the same component-vs-page boundary — just a different render target. The constraints translate without modification.

## Why This Works

This is the old insight about programming language ergonomics applied to AI code generation: constraints produce better emergent behavior than instructions. Tell the AI what it *cannot* do, and it will find the right way to do what it *can* — without you having to describe what "right" looks like.

The linters are not a design system. They are a boundary that forces a design system into existence. The agent does the curation itself, because the alternative is a failing build. No prompts, no examples, no few-shot context wasted on convention enforcement.

The result is a codebase where the AI manages its own component library with the kind of discipline you would expect from a human engineer who has been burned by component proliferation. And it doest it without ever being told to.