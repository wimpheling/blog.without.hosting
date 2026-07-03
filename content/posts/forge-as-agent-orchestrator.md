---
title: "Your Next Agent Platform Is a Git Forge"
description: "Hermes taught me that agent platforms are mostly reinventing infrastructure. The next step is thinner: a forge, a runner, a gateway, and a standard library of boring patterns."
date: 2026-07-03
tags: ["hot takes"]
unlisted: true
---

I run a Hermes agent that helps me write this blog. It's a prompt-injected agent system — skills, tools, templates, all in markdown files, loaded as context on every turn. It works. I've written dozens of posts with it, it nudges me when I'm slacking, it edits front matter, commits, and pushes.

But the profile that runs it — the whole patchwork of skills, setup scripts, cron jobs, tool configurations, prompts, and reference files — is a repository. A directory tree with conventions, version history, and a lot of implicit structure.

It should be in git. It should be *the* git repo. The agent should be able to modify itself by committing its own changes.

This is the direction I've been circling since the "Coding Agents Are Just Code" post. If agents are just code — a `while` loop, a tool dispatch table, a state machine — then the orchestrator that runs them doesn't need to be a platform. It needs to be a forge with a runtime.

## The Recent History

My previous post made the case that agentic loops are not magic. Tool calls are function dispatch. Context compression is `if (context.length > limit) summarize(oldest)`. A plan-execute-review cycle is a state machine with three states. The ML is in the model, not the loop. Everything around the LLM should be as boring as possible.

The logical next step is [BAM](https://github.com/wimpheling/boring-agent-framework) — a standard library of those boring patterns. Reusable `while` loops, retry wrappers, context managers, tool dispatch tables. Not a framework you inherit from. A collection of helpers you compose into your own agent loop.

This post asks the question after that: if your agent loop is just code in a repo, what does the orchestrator look like?

## The Realization

Hermes profiles are a directory tree with a specific layout. Skills live in `skills/`. Tools in `plugins/`. Cron jobs in `cron/`. The agent reads these files, loads them into context, and follows their instructions. The whole thing is a convention over a directory structure.

That's a repo. The convention is the schema. The version history is the audit trail. The branch protection is the deployment environment.

The moment you put it in git, things open up:

- **The agent commits its own changes.** A tool adds a skill → the agent writes the file, commits, pushes. The PR is the review gate. The blame is the debugger.
- **Multiple agents, same forge.** Each agent is a repo. Same auth, same permissions, same backup. No multi-tenant platform to build.
- **Branch = environment.** `main` is production. A feature branch is staging. The agent runs in its branch context.
- **Webhooks are triggers.** A push to `main` restarts the agent. A PR comment triggers a review. The forge already has this plumbing.

The forge becomes the orchestration surface. The agent platform abstraction collapses to a convention on top of standard infrastructure.

## The Stack

If you're building this today, the bill of materials is short:

| Layer | Component |
|-------|-----------|
| **Code** | BAM + your agent loop in a repo |
| **Versioning** | Gitea or Forgejo |
| **Auth** | Authentik or Dex (OIDC) |
| **Runner** | VM (dev/bare metal) or gVisor/WASM (VPS) |
| **Model gateway** | LiteLLM, OpenRouter, or a custom proxy |
| **Everything else** | BYO — DBs, queues, bots, standard tools |

Every component is a well-known open source project or a simple piece of code. No custom agent platform, no plugin system, no proprietary runtime. The integration cost is the wiring between them.

## The Runner

This is the piece that's secretly the product. Not the forge — the thing that executes the agent.

The forge hosts the code and fires webhooks. The runner picks up the event, spawns the agent, feeds it the trigger, collects the output, and routes it back to wherever it needs to go.

For local development and bare metal: a VM per agent, full isolation, full resource control. You can debug it, profile it, attach a debugger.

For a VPS: gVisor or WASM. The same agent code, sandboxed, with a fraction of the overhead. No full VM, no Docker daemon to manage. The agent runs in a sandbox that can only see its own filesystem and the network ports it needs.

The runner's contract is simple:
- Accept a webhook event
- Load the agent code from the repo
- Execute it with the event as input
- Capture stdout, errors, and structured output
- Deliver the result (webhook callback, commit, message)

That's it. No agent lifecycle management, no state persistence, no conversation threading. The agent manages its own state. The runner just runs and reports.

## What the Forge Gives You for Free

The forge does the work that every agent platform reinvents:

- **Auth.** OIDC, LDAP, OAuth2. The forge handles it. You don't build a user model.
- **Permissions.** Per-repo, per-branch, per-user. Read, write, admin. The forge handles it.
- **Backup.** Git. Push to a second remote. `git clone` is a disaster recovery plan.
- **Audit.** Every change is a commit. Every commit has an author, a timestamp, a message.
- **Review.** Branch protection. PRs. CI checks. The same workflow you use for code, applied to agent configuration.
- **Discovery.** The forge has a UI. Users browse repos, read READMEs, fork, star. The agent platform's "marketplace" is just a forge topic.

None of these are hard to build. But they are all time you don't spend building them when the forge already exists.

## Programmable Permissions

The forge gives you read/write/admin per repo. The runtime needs another layer: which agents a user can run, with which models, under which budget.

This is the part that sounds hard until you realize there are existing mental models. Kubernetes RBAC. AWS IAM policy documents. OpenFGA. The problem is not "how to express permissions." It's "which model to adopt."

A simple starting point: a `permissions.yaml` in each agent repo, committed alongside the agent code. The runner reads it, applies it. No separate admin panel, no database. Git is the source of truth for permissions too.

```
agent:
  name: blog-writer
  owners: [bully]
  executors: [bully, ci-bot]
  models:
    default: deepseek/deepseek-v4-flash
    fallback: anthropic/claude-sonnet-4
  budget:
    per_run: 0.50
    daily: 5.00
```

The runner checks this before every execution. The forge enforces repo-level access. The two layers compose: you need forge access to read the permission file, and the permission file constrains what you can do with the agent.

## The Model Gateway

The forge doesn't call LLMs. The runner doesn't call LLMs. The agent code calls LLMs through a gateway layer.

This is a solved problem: LiteLLM handles 100+ providers with a unified interface. OpenRouter routes between providers with fallback. A custom proxy is a dozen lines of code.

The gateway is where operational concerns live: caching, rate limiting, structured output formatting, token counting, cost tracking. None of it belongs in the agent loop. The agent says "generate text with model X, schema Y, temperature Z." The gateway handles the rest.

## What Hermes Got Right

I want to be clear about this: Hermes is not wrong. The profile model is genuinely good for discoverability and onboarding. The skill abstraction works for people who don't want to write TypeScript. The prompt-injected approach makes agent behavior transparent in a way that code doesn't always achieve.

The critique is not "Hermes is bad." It's "the abstraction is thinner than it looks."

Hermes was a useful exploration of what happens when you treat agent configuration as a first-class concern. The next step is to peel off the platform layer and see how much of it is just standard infrastructure with different labels.

## The Name

[USER: write — the name for this thing. Not "Hermes." Not "BAM." Something between the two.]

## The Gap

This post is a direction, not a blueprint. The pieces exist but the wiring does not. There is no package that installs a forge, a runner, a gateway, and a standard library with a single command. You can build it in an afternoon if you already run the components. You cannot buy it.

That is the gap this post is naming. The agent platform abstraction is paper-thin. The alternative is not a better platform. It is a forge with a runtime, a gateway, and a set of boring patterns that let you write agents as code, manage them with git, and run them anywhere.