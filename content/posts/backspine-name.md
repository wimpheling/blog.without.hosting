---
title: "Backspine — What Will the Framework Be Called?"
date: 2026-06-06T22:55:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "Working title for a new AI-assisted web development framework."
---

Backspine is the working name for a framework/methodology for AI-assisted web development. The name is still tentative. This post captures the rationale and alternatives as the idea develops.

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

[USER: write — what's the origin of "backspine"? Why this name? What alternatives were considered?]
