---
title: "Backspine Design System and Ergonomics"
date: 2026-06-06T23:00:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "Early questions about the backspine design system: type system, mobile+React, hot reloading, and implementation strategy."
---

## Actual Backbone design-system boundary

The current design system is split into contract, implementation, and facade packages:

- `design-system-contract`: typed component API;
- `design-system-basic`: React implementation plus CSS/stories;
- `design-system`: public import surface.

It also includes lint tooling that checks the architecture and forbids app code from using raw DOM JSX or importing external UI kits directly.

So the design-system thesis should be read literally: this is not just a taste layer. It is an agent-control boundary.

[USER: write — these are the starting questions from the initial brainstorm]

- Is a separate type system necessary?
- Can we do mobile + React with it?
- Can we hot-reload implementations?
- Do we need multiple implementations?

[USER: expand each question into a proper section]
