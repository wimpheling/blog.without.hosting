---
title: "Backspine — How to Add a Security Layer"
date: 2026-06-07T01:00:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "How to add a security layer in the backspine framework: where does security sit, what does it verify, and how does it interact with agent-generated code?"
---

## Existing enforcement layer

Backbone already has a small but telling security/control layer: lint rules around the design-system boundary.

The `design-system-lint` package forbids app code from bypassing the vocabulary with raw DOM JSX and blocks direct imports from common external UI libraries. That is not "security" in the auth sense, but it is control: it prevents the agent from quietly escaping the framework's intended surface.

That pattern should generalize. Backspine safety is not one giant permission prompt. It is many boring boundaries: design-system imports, route conventions, generated files, DB migrations, RPC contracts, e2e coverage, and tool permissions.

[USER: write — how does a security layer fit into the backspine architecture? Does it sit between the agent output and the codebase? Between structural elements? What does it verify — dependency safety, injection, permissions, data flow? Does it run on every change or only on certain events? Is it deterministic or LLM-assisted? A security boundary that's aware of the AI-assisted development context is different from traditional application security.]
