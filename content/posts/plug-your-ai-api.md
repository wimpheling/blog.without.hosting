---
title: "Plug Your AI API"
date: 2026-06-07T01:15:00+00:00
unlisted: true
tags: ["ai", "indie web", "agents"]
toc: true
description: "Small AI apps should not have to resell inference. Users should be able to plug in their own Claude, DeepSeek, OpenAI, or local model account with a wallet-like permission flow."
---

Every small AI app has the same awkward question hidden inside it: who pays for inference?

If I build a small indie service — say, a blogging assistant — I do not necessarily want to become an inference reseller. I do not want to price tokens, manage abuse, absorb runaway usage, build billing dashboards, or pretend my actual product is an API margin business.

My product is the workflow.

The user may already have Claude. Or DeepSeek. Or OpenAI. Or a local model. Or a company-provided inference gateway. Why should my tiny app force them through my billing layer just to call a model they already pay for?

Inference is becoming a commodity. The interesting layer is not always the model call. It is the interface, the workflow, the memory, the document model, the taste, the integration, the weird little product around the model.

So the app should not sell inference by default.

It should let the user plug their AI API.

## Metamask for AI

The missing UX is basically Metamask for AI.

When a web3 app needs to interact with your wallet, it does not ask you to paste your private key into a form. It asks your wallet for permission. You see what the app wants to do. You approve or deny. The wallet becomes the boundary between your assets and the application.

AI apps need the same boundary.

A small app should be able to say:

> This app wants to use AI.
>
> Allowed providers: Claude, DeepSeek, OpenAI.
>
> Allowed models: Claude Sonnet, DeepSeek Chat, GPT-4.1 mini.
>
> Maximum budget: €10/month.
>
> Maximum context sent per request: 50k tokens.
>
> Permissions: read current document, edit current document, search previous drafts.

The user approves. The app can now call models through the user's AI wallet, within the allowed limits.

No API key pasted into random SaaS. No hidden token burn. No surprise bill. No app-specific subscription just because one feature calls an LLM.

## The wrong default

The current default is bad for indie software.

If I add AI to my app, I am expected to either:

1. pay for every user's inference myself and hide it inside a subscription price;
2. ask users to paste API keys into my settings page;
3. build my own provider abstraction, billing limits, key storage, retries, dashboards, and abuse controls;
4. or avoid AI features entirely because the economics are annoying.

This pushes every small AI product toward becoming a miniature OpenRouter plus a product UI.

That is backwards.

Most indie apps should not be in the business of selling tokens. They should be in the business of doing something useful with tokens.

## Bring your own model account

The better default is bring-your-own-inference.

The user already has an account somewhere. The app requests permission to use it. The user controls the allowed providers, models, budgets, and scopes.

For a blogging assistant, the permission might be:

- Use Claude or DeepSeek
- Maximum €5/month
- Read and edit posts in this repo
- No access to private notes unless explicitly selected
- No training/data retention if the provider supports that setting
- Ask before using models above a certain cost

For a coding assistant, the permission might be different:

- Use local model for cheap edits
- Use frontier model for architecture changes
- Maximum 2 million tokens/day
- Read repository files
- Write patches only after user approval

The point is that the AI budget becomes a user-owned capability, not an app-owned hidden cost.

## Not just API keys

This is not simply "let users paste their OpenAI key".

Pasting API keys is the bad version. It makes every random web app a secret manager. It gives users no readable permission model. It creates a weird trust cliff: either the app has your whole key or it has nothing.

The wallet version should expose constrained capabilities:

- provider allowlist
- model allowlist
- budget caps per day, month, or year
- per-request token caps
- tool/data scopes
- logging preferences
- revocation
- human confirmation for expensive calls

The user should be able to see:

- which apps are using AI
- how much they spent
- which models they called
- what permissions were granted
- when a permission expires

This is boring infrastructure, but it unlocks a lot of small software.

## Why this matters

AI will not only live inside giant AI-native SaaS products.

It will be sprinkled into thousands of tiny tools: blog assistants, note apps, local dashboards, personal CRMs, admin panels, code generators, browser extensions, spreadsheet helpers, weird weekend projects.

Those apps should not all need to become billing companies.

They need a standard way to request AI capability from the user.

"Use AI" should become a permission prompt.

Not a pricing page.

[USER: expand — find references for "inference is becoming a commodity" and existing attempts at AI wallets / model routers / user-owned API credentials. Also sharpen whether this is a browser extension, local agent, OAuth-like protocol, or provider-side delegated token system.]