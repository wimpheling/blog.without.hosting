---
title: "Building an Open-Source Quick for Backspine"
date: 2026-06-11T23:45:00+00:00
unlisted: true
tags: ["backspine"]
toc: true
description: "Shopify's Quick is the best model for an AI-generated site host. Let's build the open-source version — Cloudflare-first, with an abstraction layer so you can self-host anywhere."
---

[Shopify's Quick](https://shopify.engineering/quick) is the best model I have seen for hosting AI-generated sites. Drop a folder, get a URL with a zero-config backend — database, AI, file storage, websockets, identity. One VM, $200/month, 50,000 sites.

The question is: how do we build the open-source version, adapted for backspine?

## The architecture: adapter pattern from day one

The mistake most Quick-like projects make is building for one cloud and locking in. The fix is boring but necessary: define the backend capabilities as interfaces, implement them once per target.

```
backspine/
├── core/               # interfaces and types
│   ├── db.ts           # collection, query, subscribe
│   ├── storage.ts      # upload, serve, delete
│   ├── ai.ts           # chat, image, embed
│   ├── realtime.ts     # pub/sub, presence, cursors
│   ├── identity.ts     # user, auth, session
│   └── deploy.ts       # spec → output pipeline
├── adapters/
│   ├── cloudflare/     # Workers + D1 + R2 + Durable Objects
│   ├── local/          # SQLite + filesystem for dev
│   └── vps/            # Postgres + S3-compatible + nginx
└── cli/
    └── deploy.ts       # backspine deploy <target>
```

The user-facing API is the same regardless of backend:

```js
const posts = backspine.db.collection('posts');
await posts.create({ title: 'hello', body: 'world' });

const res = await backspine.ai.chat([
  { role: 'user', content: 'summarize this' }
]);
```

This is Quick's client API adapted. The difference: Quick exposes it from a single Go VM. We expose it from an adapter layer that runs on Workers, a VPS, or your laptop.

## Cloudflare-first

Cloudflare is the obvious first target because:

- **Workers**: global edge compute, generous free tier (100k requests/day)
- **D1**: SQLite-compatible database with replication. Maps directly to Quick's `db.collection()` pattern.
- **R2**: S3-compatible storage, no egress fees. Covers file uploads.
- **Durable Objects**: real-time websockets and presence. Covers Quick's websocket API.
- **Workers AI**: LLM inference on the edge (Llama, Mistral). Covers `ai.chat()`.
- **Pages**: static file hosting with git integration. Covers the "drop a folder" deploy.

The Cloudflare adapter implements all six Quick capabilities. The deploy command becomes `backspine deploy --target cloudflare` and pushes your spec + assets to Workers + R2 + D1.

The cost for a personal site: zero, unless you exceed free tier limits. Compare to Quick's $200/month VM that serves 50k internal sites — personal scale is free on Workers.

## The VPS fallback

The abstraction layer's value proposition: when Cloudflare's limits or policies don't fit, you move to a $5 VPS without rewriting anything.

```
backspine deploy --target vps
```

The VPS adapter uses the same interfaces:
- SQLite or Postgres for `db.collection()`
- Local filesystem or MinIO for storage
- Your own LLM API keys for AI
- nginx + websocket server for real-time
- Caddy for TLS

The spec output compiles to the same deployable structure. The cost model changes (you pay for the VPS + your own API keys) but the development model does not.

## The backspine integration

Quick is agnostic about code structure — you upload whatever files your AI generated. A Quick-like platform for backspine should treat the spec as the deployable unit.

The deploy pipeline:

```
spec.yml ──→ backspine compile ──→ generated code ──→ backspine deploy ──→ live site
                                                         │
                                                    ┌────┴────┐
                                                    │  D1     │ R2
                                                    │  DB     │ Files
                                                    │  AI     │ WS
                                                    └─────────┘
```

The spec is the source of truth. The generated code is ephemeral — the platform can regenerate it from the spec on every deploy without losing state (because state lives in the backend services, not in the generated code).

This is the [recompile from spec](https://blog.without.hosting/posts/backspine-llm-compiler/) pattern at the hosting level. The platform does not just serve files — it manages the relationship between the spec and its compiled output.

## What ships first

The minimum viable project:

1. **Core interfaces** — the six capability types (db, storage, ai, realtime, identity, deploy). A TypeScript package.
2. **Cloudflare adapter** — Workers implementation of all six. Deploy with `wrangler`.
3. **CLI** — `backspine init` (scaffolds a spec), `backspine dev` (runs locally), `backspine deploy --target cloudflare`.
4. **Spec format** — YAML that describes the site: routes, data models, AI features, style constraints. Compiler converts to Workers code.
5. **VPS adapter** — the self-host fallback. SQLite, filesystem, nginx.

The goal is not to build another platform. It is to build a *tool* that gives you Quick's capabilities on your own infrastructure, with Cloudflare as the generous free tier and a VPS as the escape hatch.

[USER: write — what is the first real use case? Your own blog? A site generator for this blog's backspine experiments? An internal tool for your team? Pick one and scope the MVP around it.]