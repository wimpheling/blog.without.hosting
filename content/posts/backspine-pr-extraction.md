---
title: "Backspine — Deterministic PR Message Extraction"
date: 2026-06-07T00:15:00+00:00
unlisted: true
tags: ["backspine"]
toc: false
description: "Extracting structural parts from PR messages deterministically, without relying on LLM interpretation of the overall structure."
---

## PR extraction against Backbone

In Backbone terms, a useful extracted PR should probably be a vertical slice, not a random diff chunk.

A coherent feature PR might include:

- one page folder;
- the route adapter and state store;
- any design-system vocabulary needed by that page;
- server RPC/database changes;
- migrations;
- story states;
- component tests;
- Gherkin + Playwright scenarios.

That is a more meaningful unit than "whatever files the agent happened to edit during the chat."

[USER: write — the idea is deterministic extraction of structural parts from PR messages. Not LLM-based parsing of the whole thing, but targeted extraction of specific structural elements. What are those parts? What format do PR messages follow? What makes non-deterministic extraction a problem?]
