---
title: "Backspine — Structural Changes Semantic"
date: 2026-06-07T00:50:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "The UI should surface structural changes semantically, not as token-level diffs, and let you zoom into implementations on demand."
---

## Structural changes in the current repo

The current Backbone template gives a concrete meaning to "structural change." It is not just editing a React file.

A real feature may touch:

- route registration in `App.tsx`;
- a page folder under `client/src/pages/`;
- static/dynamic prop types;
- Zustand state;
- design-system primitives;
- ConnectRPC client calls;
- Rust server modules;
- SQL migrations;
- Gherkin scenarios and Playwright tests.

Backspine's job is to make that structure explicit enough that the agent can modify it without turning the repo into a pile of local improvisations.

[USER: write — the interface for reviewing agent-generated code should show what changed at the architecture/structural level first, with the ability to zoom into a specific implementation. Not a flat wall of diff text.]

Referenced from: [backspine hot take — don't read agent text](blog.without.hosting/posts/backspine-dont-read-agent-text/)
