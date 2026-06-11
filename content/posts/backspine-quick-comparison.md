---
title: "We Need a Quick for Backspine"
date: 2026-06-11T23:30:00+00:00
unlisted: true
tags: ["backspine"]
toc: true
description: "Shopify's Quick is a zero-config hosting platform for AI-generated HTML sites. Backspine needs the same thing: a hosting platform where the spec is the unit of deployment, not files."
---

[Shopify just published the story of Quick](https://shopify.engineering/quick), an internal platform where you drop a folder of HTML and get a secure URL. It provides a zero-config client-side API for databases, AI, file storage, websockets, and identity — all running on a single $200/month VM.

It hosts over 50,000 internal sites. More than half of Shopify has created at least one. The key insight: *AI-generated HTML was the catalyst, but the zero-config backend was the unlock.* People could vibe-code a site, and Quick gave it persistence, AI capabilities, real-time collaboration, and a URL — in seconds.

This is exactly right. And it makes the gap for backspine very obvious.

## What Quick gets right

Quick is not clever. It is opinionated and constrained. A fixed set of capabilities — database, file uploads, AI, websockets, identity — exposed as a client-side JavaScript API. No config files, no deployment pipelines, no permissions model (all sites are open to all employees, because it runs inside Shopify's trust bubble). The constraints are the point: a small surface keeps the platform simple to understand, maintain, and build on.

The architecture is almost comically straightforward:
- Static files in a GCS bucket, mounted via gcsfuse, served by NGINX
- A single Go server behind it handling the API services
- IAP for auth (every request is already authenticated before it reaches the site)
- That is it. One VM, $200/month.

## What Quick does not touch

Quick is agnostic about code structure. It serves whatever you upload. The AI generation side is entirely in the user's hands — they prompt, they get HTML, they upload it to Quick via `quick deploy`.

This is where backspine enters. Backspine is not about serving files. It is about the *relationship between the spec and the generated code*. If Quick is the deployment platform for vibe-coded sites, backspine is the *architecture* that keeps those sites coherent across generations.

The gap: there is no platform that combines both.

## What a "Quick for backspine" would look like

Instead of deploying files, you deploy a *spec*. The platform:

1. **Hosts the spec** as the unit of truth. Not a folder of HTML — a document that describes what the site does, its data model, its visual style, its constraints.
2. **Compiles the spec into code** on deploy. Every deploy is a fresh compilation from the current spec, using the [recompile from spec](https://blog.without.hosting/posts/backspine-llm-compiler/) pattern.
3. **Provides the zero-config backend** — Quick's database, AI, websockets, identity, file storage. The same bundle, but integrated at the spec level rather than the client-side API level.
4. **Manages code islands**. The spec defines structural boundaries. Changes to one island do not recompile the others. The [code islands](https://blog.without.hosting/posts/backspine-code-islands/) pattern becomes a runtime concept, not just a build-time convention.
5. **Accumulates the spec**. Every user correction, every design system update, every data model change becomes part of the spec. The site is always one recompile away from the correct state.

The deploy loop becomes: edit spec → `backspine deploy` → platform recompiles → new site is live. The agent never touches generated code. It only touches the spec.

## The philosophical difference

Quick is **hosting for generated artifacts**. It takes the output of an AI generation and serves it with a backend. The generation is a separate step, owned by the user and their agent.

Backspine is **hosting for the generation process itself**. The platform owns the spec, the compilation, and the deployment. The agent works at the spec level, and the platform handles the rest.

This matters because the backspine pattern *structurally prevents drift*. Quick does not prevent drift — it gives you a place to put the drifted artifact. With backspine, the spec is the only persistent state. The generated code is ephemeral.

## What can be open-sourced

The Quick model is simple enough to replicate — a VM, a static file server, a database, an AI proxy, websocket support. The value is in the constraints and the integration, not in novel infrastructure.

An open-source backspine host would be different. The core challenges:

- **Spec language**: What does a spec look like? YAML? A subset of Markdown? A JSON Schema? The platform needs a spec format that is human-writable, LLM-generatable, and compilable into working code.
- **Compiler infrastructure**: The spec → code pipeline. This is the hard part. It is not a transpiler — it is an LLM call that produces structured output against a known template system. The platform needs to manage this predictably.
- **Island boundary resolution**: When a spec change only affects one code island, the platform must detect that and recompile only the affected module. This is the equivalent of a build system knowing which source files changed.
- **Spec accumulation**: Every user correction becomes a spec entry. The platform needs a versioned, mergeable spec history.

These are not insurmountable. They are the problems that backspine exists to solve.

[USER: write — what is the minimum viable version? A CLI that takes a spec YAML and produces a Quick-compatible folder of HTML + a backend config? A server that hosts both the spec and the generated site? A hosted platform with auth, billing, and deployment? Where does the open-source boundary sit?]

## The Quick philosophy that carries over

The strongest lesson from Quick is the constraint discipline. A small, fixed set of capabilities — database, AI, real-time — is more powerful than a flexible platform with infinite options, *because it forces creativity into a bounded space*. The backspine equivalent: a small, fixed set of structural primitives (spec, islands, compiler, deploy) is more powerful than a general-purpose code-generation platform, because it forces the architecture to stay coherent.

Quick also proves the trust-bubble model works. A backspine host for personal projects needs no permissions model, no user management, no site ownership. Every site is open to the world. You overwrite a site by deploying over it. This is the [lrnwerkstatt](https://blog.without.hosting/posts/backspine-put-the-vibe-back-in-vibe-coding/) pattern — share everything, overwrite anything, learn from what others built.

## The counterargument

Quick works at Shopify because it runs behind IAP — every user is a trusted employee. An open-source backspine host on the public internet cannot assume trust. The moment you expose a spec-to-deploy pipeline to the public, you have an abuse problem: people will deploy spam sites, phishing pages, crypto drainers using your infrastructure.

Quick's answer ("internal trust bubble") does not translate to the open web. A backspine host needs either:
- A managed service with vetting (like Netlify but for specs)
- A personal hosting model (you run your own instance, the spec is yours)
- A protocol layer (the spec format is open-source, anyone can host it)

My bet is on the personal hosting model: **backspine-as-a-compiler, not backspine-as-a-service**. The spec format and compiler are open-source. You run your own VM (or use any static host) and the CLI compiles your spec into deployable output. The "Quick for backspine" is not a platform you sign up for — it is a tool you run.

[USER: write — is that enough? A CLI that turns a spec into a deployable site is a build tool, not a platform. Does the platform add enough value over the tool to justify building it? Or is backspine best as a file format and a compiler, with hosting as an implementation detail?]