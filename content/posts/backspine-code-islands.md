---
title: "Backspine — Code Islands"
date: 2026-06-07T00:45:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "Code lives in islands inside structural elements, not in a linear stream of token-level output."
---

## Current Backbone island shape

The existing template already points toward islands, even if it does not call them that yet.

A page is not one blob. The hello-world feature is split across:

- `hello-page.tsx`: the mostly-presentational page component;
- `hello-page-route.tsx`: the route adapter that binds real state/actions;
- `hello-page-state.ts`: Zustand state and ConnectRPC client calls;
- `hello-page.stories.tsx`: preview states;
- `hello-page.test.tsx`: component-level tests;
- `e2e/features/helloworld.feature` and `e2e/tests/helloworld.spec.ts`: behavior-level coverage;
- server database/RPC modules and SQL migrations.

That is close to a compilation unit. A Backspine "island" is probably not just a React component. It is the vertical slice: page, route adapter, state, payloads, backend endpoint, migrations, stories, and e2e behavior.

The practical version of "recreate, don't patch" is therefore not regenerate the whole app. It is regenerate a bounded island and verify its contracts.

[USER: write — the idea that generated code should be scoped into isolated, reviewable islands within structural elements, rather than delivered as a continuous diff or stream of tokens.]

Referenced from: [backspine hot take — don't read agent text](blog.without.hosting/posts/backspine-dont-read-agent-text/)
