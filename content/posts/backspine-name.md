---
title: "Backspine — What Will the Framework Be Called?"
date: 2026-06-06T22:55:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "Why the name matters: LLMs are proteiform, drift is inevitable, and finding the right metaphor for the structure that channels them is more than branding."
---

Backspine is the working name for a framework/methodology for AI-assisted web development. The name is still tentative. This post captures the rationale and alternatives as the idea develops.

## The proteiform problem

LLMs are proteiform. They span a problem space so vast and continuous that almost any prompt is a drop of ink in an ocean of meanings. Their quasi-omniscience is the property that makes them powerful and the property that makes them drift.

"Drift" here is not the model drifting off-topic in the vulgar sense. It is more structural: the prompt dissolves into the larger space of meaning latent in the model. Every specific instruction is in constant competition with everything else the model knows. The result is that LLM output has a natural tendency to return toward the local mean of the training data unless the constraint around it is very strong.

This is why prompt engineering exists. It is not about finding magic words. It is about building a container small enough that the prompt's signal dominates the noise of the model's vast latent space.

## The name as metaphor

The industry settled on "harness." It is not a bad word: a harness is how you control something stronger than you. You harness a horse, a dog team, a draft animal. The metaphor is control through attachment. But a harness is about restraint and direction — it does not say much about *shape*.

Backspine came from "backbone" — the central support structure. The problem: Backbone.js is already a thing, so the name is poisoned for a web framework. Backspine keeps the same structural intuition without the namespace collision.

But exactly what kind of support structure are we talking about?

## The candidate landscape

Several metaphors capture different angles of the same problem: how do you give useful shape to a system that has too much shape?

**Harness.** Restraint and direction. The animal is powerful, you guide it. The metaphor is about control but says nothing about the transformation the output undergoes. It is also already taken by the industry — which is fine for general use but makes it a weak differentiator for a specific framework.

**Backspine / Backbone.** Central support structure. The spine is what the rest of the body hangs on. In Backbone's case, the metaphor was about MVC structure for JavaScript applications. In Backspine's case, the spine is the set of architectural conventions that the code, the agent, the tests, and the human all attach to. The spine does not move — everything else does.

**Armature.** The internal wire skeleton inside a clay sculpture. Clay is the proteiform material: it has no inherent shape. The armature gives it structure from the inside. This is a strong metaphor because the scaffold is invisible in the finished piece — it is embedded. It is also a precise term from a domain (sculpture) that understands the interaction between shapeless material and structural constraint. The armature does not dictate the final form. It prevents collapse.

**Formwork.** In construction, concrete is poured liquid into formwork. The formwork shapes it until it sets, then it is removed. This maps elegantly to the proteiform property — the material is shapeless at the point of use, the structure is temporary, and the output retains its shape. Formwork is also explicitly infrastructure, not product. You build it to produce the shaped thing, then you move on. This is exactly the right relationship between a prompt structure and the code it produces.

**Scaffolding.** Also construction. Temporary external support for a building that is being built or repaired. The problem: "scaffolding" already means something specific in development — code generation boilerplate, project skeletons, the kind of thing `create-react-app` generates. The collision is real enough that using it for a prompt-workflow methodology would be confusing.

**Exoskeleton.** External rigid casing. An insect's exoskeleton is not just support — it is also armor. The metaphor leans militaristic, defensive, almost paranoid. It captures the containment angle well but the vibe is wrong for what should be a productive, not adversarial, relationship between human and LLM.

## What the implementation actually looks like

The name debate is not abstract. There is working code.

The public repository is [`wimpheling/backbone-template-v1`](https://github.com/wimpheling/backbone-template-v1). It is called Backbone because that was the first working name, before I realized the collision with the legacy framework. The code inside already encodes several of the ideas these names gesture at.

A page in the template has five files:

- **Page component**: typed React, using only design-system vocabulary (`Button`, `Navigation`, `Layout`, `Stack`, `Text`, `Form`, etc.) — no raw JSX, no random UI imports.
- **Route adapter**: binds the page to routing, separates concerns from the page component.
- **State store**: Zustand store for client state — separated from the page logic so the agent can regenerate either independently.
- **Stories**: Ladle stories for visual testing — because if a page is a compilation unit, it needs a standalone preview.
- **Tests**: unit tests for the page logic.

The design system is contract-first: a types-only package (`design-system-contract`), a concrete implementation (`design-system-basic`), and a facade package that app code imports from (`design-system`). An architectural linter and oxlint plugin enforce that app code cannot import raw DOM JSX or third-party UI libraries directly. The agent must speak through the design system vocabulary.

This is the bridge from metaphor to implementation. Whether you call it a spine, an armature, or formwork, the structural claim is the same: the template defines a set of architectural primitives that are stable, typed, and semantic. The LLM generates within those primitives. Drift is constrained not by prompt magic but by structural enforcement — the linter, the contracts, the type system, the test framework.

## The metaphor and the architecture

I keep coming back to the same tension. The LLM is proteiform. The codebase wants to be predictable. The name should capture what sits between them.

**Backspine** is still the leading candidate because it is simple, pronounceable, and carries the right structural implication without borrowing from a domain that already defines a conflicting concept. But **armature** has real conceptual weight — it is not just support, it is *embedded* support, invisible in the finished piece but preventing collapse during the shaping process. And **formwork** is the most precise for the actual workflow: you build structure, pour LLM output into it, let it set, and move on.

Right now, the package is called Backbone (legacy reasons), the methodology is called Backspine (working name), and the debate is live. The name should settle once the broader architecture is stable enough that the post — this one — stops being a draft and becomes an announcement.

[USER: write — what pushed you toward backspine over armature or formwork? Or is the name genuinely unsettled?]