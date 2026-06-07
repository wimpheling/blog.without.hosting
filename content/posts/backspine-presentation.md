---
title: "Backspine — Project Presentation"
date: 2026-06-07T00:20:00+00:00
unlisted: true
tags: ["backspine"]
toc: true
description: "A presentation of the backspine framework: what it is, why it exists, and what problems it solves for AI-assisted web development."
---

## Current Backbone v1 grounding

This is not only a thought experiment anymore. The working codebase is public as [`wimpheling/backbone-template-v1`](https://github.com/wimpheling/backbone-template-v1). The public concept is Backspine, but the repo and packages still use the first working name: Backbone.

The current template already encodes several of the ideas in this draft:

- client pages are split into page components, route adapters, state, stories, and tests under `template/client/src/pages/`;
- the React design system is separated into `@backbone/design-system-contract`, `@backbone/design-system-basic`, and the public facade `@backbone/design-system`;
- app code is pushed toward the design-system vocabulary instead of raw JSX;
- a custom `design-system-lint` package forbids raw DOM JSX in app code and blocks direct imports from external UI libraries;
- end-to-end behavior is specified with Gherkin features and Playwright tests under `template/e2e/`;
- the backend is Rust, with SQL migrations, database modules, and ConnectRPC wiring.

So when this post says "Backspine," read it as the methodology emerging from that Backbone template, not as a blank framework fantasy.

[USER: write — this is the project pitch. What is backspine? What problem does it solve? What makes AI-assisted web development different from traditional web development, and why does it need its own framework? What's the elevator pitch?]
