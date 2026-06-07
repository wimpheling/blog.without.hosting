---
title: "Backspine — My Abstract Design System Setup"
date: 2026-06-07T01:45:00+00:00
unlisted: true
tags: ["backspine", "design systems", "ai"]
toc: true
description: "The surprising part of an abstract design system is not reuse. It is watching the agent build a vocabulary organically around product use, instead of randomly inventing UI every time."
---

I am quite happy with my abstract design system setup.

Not because it is perfect. It is not. The interesting thing is that it gives the agent a place to grow a vocabulary.

That sounds a bit abstract, but it matters.

When you let an AI code React freely, it tends to invent UI locally. Every page becomes its own little island of arbitrary choices: a button here, a menu there, a hand-written flex layout, a slightly different card, a new naming pattern because why not. The agent is productive, but the interface slowly becomes a junk drawer.

A design system changes the failure mode.

It gives the agent words.

## The vocabulary emerges from use

The nice surprise is that the vocabulary does not need to be fully designed upfront.

You can start with a small abstract layer: layout primitives, buttons, panels, typography, page containers, navigation blocks, maybe a few state components. Then, as features appear, the agent starts discovering recurring needs.

At first it uses the primitives directly. Then it notices a pattern. Then it names the pattern. Then that name becomes part of the system.

This is the good version of AI-assisted design system work: not a giant abstract taxonomy invented before the app exists, but a vocabulary that emerges organically from product use.

The agent becomes quite ingenious when the abstraction boundary is clear.

It stops asking: "How do I style this div?"

It starts asking: "Is this a Navigation? Is this a PageHeader? Is this an ActionPanel? Is this a ResourceList?"

That is a much better question.

## Example: Navigation

Navigation is a good example.

A naive agent will build navigation as markup:

- a list
- links
- active classes
- maybe a mobile menu
- maybe breadcrumbs
- maybe tabs
- maybe duplicated logic between pages

That works once. Then it decays.

In an abstract design system, "Navigation" can become a product-level concept. Not just a component, but a vocabulary item.

A navigation object can express:

- where the user is
- what section this page belongs to
- what sibling pages exist
- what actions are available
- what should collapse on mobile
- what should be highlighted
- what route owns the current context

The agent can then use `Navigation` instead of re-solving navigation every time.

More importantly, it can extend the concept when the app needs it. Maybe the first version is simple links. Later, the product needs contextual navigation, then secondary actions, then route groups. The vocabulary grows around actual use.

This feels much better than asking the agent to generate UI from scratch on every prompt.

## Abstract, but not ornamental

The danger with design systems is abstraction theater.

You get beautiful names for things nobody needs. You build a component library that looks coherent in Storybook but does not actually help the product move faster. The abstraction exists because designers and frontend engineers enjoy abstraction.

That is not what I want.

Backspine's design system should be abstract only where abstraction improves agent behavior.

The test is simple:

- Does this concept reduce repeated local invention?
- Does it make product changes easier to express?
- Does it make generated UI more consistent?
- Does it give the agent a better vocabulary?
- Does it make diffs more semantic?

If not, it is probably decoration.

## Design systems as agent language

For humans, design systems are often about consistency and speed.

For agents, they are also about language.

The design system is the set of nouns and verbs the agent can safely use when changing the interface. The richer and cleaner that vocabulary is, the less the agent has to improvise.

This is why the abstraction layer matters. It is not just UI polish. It is a control surface.

A good Backspine design system should make the agent generate product concepts, not random JSX.

It should let the agent say:

- this page has a `PageHeader`
- this area is a `Navigation`
- this list is a `ResourceList`
- this empty state is an `EmptyState`
- this action is a `PrimaryAction`
- this form belongs to a `FormFlow`

Then the human reviews the product structure, not the CSS incidentals.

## Why I like this setup

The setup feels promising because it does not require the framework to know everything in advance.

The vocabulary can grow. The agent can propose new abstractions when repetition appears. The human can accept, reject, rename, or collapse them.

That is the right collaboration pattern.

Not: "AI, design my UI from nothing."

Not: "Here is a frozen enterprise design system, obey it forever."

But: "Here is a small abstract language. Use it. When the product teaches us a new word, add the word."

That is where Backspine gets interesting.

[USER: expand — add the concrete Navigation example from the actual project. What did the agent invent? What vocabulary emerged? What should be stabilized into the design system versus left as local implementation?]
