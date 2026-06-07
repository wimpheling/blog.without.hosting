---
title: "Backspine — Put the Vibe Back in Vibe Coding"
date: 2026-06-07T01:25:00+00:00
unlisted: true
tags: ["backspine", "ai", "vibe coding"]
toc: true
description: "Vibe coding should not mean staring at chatbot slop or agent logs. It should mean staying focused on the product surface: routes, payloads, database, pages, and tests."
---

I want to put the vibe back in vibe coding.

Not the fake vibe where you watch a chatbot narrate its own thoughts. Not the agent theater where five processes produce a galaxy of logs and you pretend the noise means intelligence is happening.

I mean the actual vibe: staying close to the thing you are building.

The feature. The page. The route. The payload. The database shape. The test that proves the user journey works.

That is where the attention should go.

## Conversation is noise

I do not want to see chatbot slop.

The agent saying "I'll update the route, modify the schema, and ensure the tests pass" is not work. It is a weather report about work. Sometimes it is useful for debugging the assistant. Most of the time it is just another stream competing for attention.

This is the same point as [Stop Reading What Your Coding Agent Says](https://blog.without.hosting/posts/backspine-dont-read-agent-text/): coding agents are not valuable because they can talk about coding. They are valuable if they move the artifact forward.

The conversation is not the artifact.

The artifact is the app.

## What I want to look at

When I build with AI, I want the interface to keep me focused on the product structure:

- **Routes** — what exists, what changed, what endpoint serves what behavior.
- **Payloads** — what data crosses boundaries, with what schema, validation, and failure modes.
- **Database** — what tables, collections, migrations, indexes, and invariants changed.
- **Pages** — what the user sees, what states exist, what interactions are possible.
- **End-to-end tests** — what user journeys are now covered, broken, or missing.

This is the material of the product.

A coding assistant should surface this material directly. Not bury it under a transcript.

If the agent touched a route, show me the route. If it changed a payload, show me the payload. If it claims the feature works, show me the e2e test. If it created a page, show me the page.

The UI should be calm, minimal, and structural.

## Minimal AI, not maximal theater

There is a weird tendency to make AI development interfaces look like mission control.

Agents everywhere. Logs everywhere. Subagents negotiating with other subagents. Fancy dashboards showing tokens, traces, plans, reflections, tool calls, and little status messages from digital interns.

Maybe sometimes you need that. If you are running a serious multi-agent workflow, fine. Swarms have their place.

But the point is not to keep your nose inside the swarm's output logs.

That is not vibe coding. That is babysitting an orchestra of interns.

The point is to hide as much of the machinery as possible and keep the developer's attention on the evolving product.

A nice minimalist AI should do less in the interface, not more. It should reduce the surface area of coordination. It should make the app feel more present, not the assistant.

## The Backspine interface

Backspine should not be a chatbot with a filesystem attached.

It should be a product-structure editor with AI attached.

The default view should be something like:

- feature map
- routes
- components/pages
- data model
- tests
- current diff
- preview

The assistant can exist, but as a side control surface. You ask it to create, modify, or regenerate parts of the product. Then the interface shows what changed in product terms.

Not "the agent says it updated auth."

Show:

- new `/login` route
- updated session payload
- changed `users` table
- login page states
- e2e test: successful login
- e2e test: invalid password

That is the vibe.

The vibe is not mystical. It is not letting the model vomit code while you trust the magic. It is a tight feedback loop where the AI does the boring implementation work and you stay focused on feature semantics.

## Less chat, more product

The best AI coding interface may look less like a chat app and more like a focused admin panel for your application.

A place where the assistant is present, but not constantly performing.

A place where changes are shown as routes, payloads, pages, tests, and structural diffs.

A place where you can still summon more power when needed — multiple agents, deeper analysis, rebuilds from spec — but where the everyday workflow stays quiet.

The computer should not ask you to read its monologue.

It should show you the thing you are making.

## Backbone's actual focus surface

The current repo already rejects the "watch the agent type" interface. The interesting surfaces are structured:

- pages in `template/client/src/pages/`;
- design-system vocabulary in `template/client/packages/design-system-*`;
- state/action wiring in route adapters and Zustand stores;
- backend data/RPC modules in `template/server/src/`;
- SQL migrations;
- Gherkin features and Playwright tests.

That is the vibe I want: not chatbot transcript as product UI, but a small set of product structures the agent can modify. The human should review routes, payloads, pages, tests, and design-system vocabulary — not the assistant's theatrical monologue.

[USER: expand — make this more concrete as a Backspine UI proposal. What are the exact panels? What does a feature change screen look like? How do we separate useful agent trace from chatbot slop without hiding evidence when something breaks?]
