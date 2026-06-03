---
title: "Revisiting Decentralized Autonomous Intelligence"
date: 2026-06-03T01:19:26+00:00
draft: true
toc: true
description: "A revision of my 2023 DAI idea: what aged badly, what still matters, and what stack could make AI agents economically real."
---

In 2023 I wrote about **Decentralized Autonomous Intelligence**, or DAI: the idea of combining LLMs, decentralized infrastructure, and crypto-economic incentives into something that could act, learn, spend, and improve itself.

Reading it now, part of it feels obviously dated.

The old article was written inside the mood of the time. DAOs were still treated as if they were going to become the default form of internet-native organization. Tokenomics was everywhere. If you had a coordination problem, a governance problem, or an incentive problem, the reflex was: put it on-chain, add a token, define the actors, and let the protocol economics do the work.

That framing has aged.

But the core question has not.

Actually, it may be more relevant now.

The mistake was not to connect AI agency with crypto. The mistake was to assume too quickly that the answer would look like a DAO, with a native token, miners, and a full blockchain-era mythology around it.

The stronger version of the argument is simpler:

> If an AI is supposed to be an agent in the strong sense, it needs some way to hold resources, spend resources, pay humans, rent tools, buy compute, and receive money. Today, AI systems cannot open bank accounts. Software cannot just become a customer of the traditional financial system. Crypto remains one of the few infrastructures where software can hold and move value directly.

That is not hype. That is a practical constraint.

## What aged badly

The old DAI article took too much for granted.

It assumed that DAOs were here to stay as the natural organizational form for autonomous systems. It assumed that a native cryptocurrency would be the obvious economic layer. It talked about miners, token demand, and a DAI currency as if those were implementation details rather than huge design decisions.

It also leaned too much toward a whitepaper style: define the actors, define the incentives, describe the token flow, and end with a promise of a self-sustaining ecosystem.

That style now feels suspicious. Not because the questions are wrong, but because the crypto cycle trained everyone to generate elegant incentive diagrams for systems that did not yet have real users, real work, or real accountability.

The dated parts are mostly these:

- treating blockchain as the default substrate;
- treating tokenomics as the center of the design;
- assuming DAOs had already proved themselves as organizational infrastructure;
- talking about "miners" instead of a broader set of compute, model, data, tool, and human contributors;
- making decentralization sound like an automatic good rather than a tradeoff;
- under-specifying the legal and operational boundary between the AI system and the humans around it.

A modern DAI should not start with a token.

It should start with agency.

## What still feels right

The best idea in the original article was that an advanced AI system should not be understood only as a model.

A model is not an agent. A chatbot is not an agent. Even a tool-using LLM is only barely an agent if it has no durable memory, no budget, no authority, no way to acquire resources, and no way to change its own conditions of operation.

The interesting object is something more institutional:

> an AI-centered organization that can plan, act, allocate resources, coordinate humans and tools, and improve over time under some governance structure.

That still feels right.

The old article also had several good instincts:

- **The AI needs a budget.** If it cannot spend, it cannot really act outside a sandbox.
- **Improvement is a resource allocation problem.** Training, fine-tuning, data acquisition, evaluation, tool building, and human feedback all cost something.
- **There are multiple economic roles.** Users, developers, data providers, compute providers, reviewers, maintainers, auditors, and investors may all interact with the system.
- **The system must balance doing work and improving itself.** An agent has to decide how much of its resources go to serving users versus upgrading its own capabilities.
- **Humans are not outside the system.** A real DAI would coordinate humans, not replace them magically.
- **Forking matters.** If an AI organization becomes badly governed, captured, or misaligned, the ability to exit and fork may be a central safety and governance mechanism.
- **Open source and open data matter, but are not simple.** Openness gives auditability and collaboration, but creates privacy, security, and competitive problems.

These ideas are stronger now than they were in 2023, because AI agents have become less fictional.

We now have systems that can write code, call APIs, operate computers, manage workflows, run evaluations, and coordinate subtasks. They are still fragile, but the direction is clear: the model is becoming only one component inside a larger agentic system.

The missing layer is not only intelligence.

It is agency infrastructure.

## Why crypto may become useful for agents before it became useful for DAOs

DAOs often felt like organizations looking for a purpose.

AI agents may invert that.

Here we may have agents with a purpose, but no native institution around them.

An autonomous AI that performs useful work eventually needs answers to very boring questions:

- Who pays for its inference?
- Who pays for its tools?
- Can it hire a human?
- Can it buy access to data?
- Can it rent GPUs?
- Can it receive revenue?
- Can it hold a budget?
- Who can stop it from spending everything?
- Who audits its transactions?
- Who owns what it produces?
- Who is liable when it does something wrong?

Traditional finance and law do not have a clean category for this. A bank account belongs to a legal person. A contract is signed by a legal person. Liability attaches to a legal person.

An AI agent is not a legal person.

Crypto does not solve that entire problem, but it gives software a primitive that the banking system does not: direct control over value.

That is why the crypto angle survives the death of the hype framing.

Not because every DAI needs a speculative token. Not because governance should be on-chain by default. Not because DAOs were inevitable.

But because autonomous software needs economic agency, and crypto is currently the most obvious machine-native payment and custody layer.

## The revised DAI thesis

A revised version of the DAI idea could be:

> A Decentralized Autonomous Intelligence is an AI-centered agentic organization with its own resource loop: it can receive tasks, perform work, earn or receive funds, spend those funds on tools/compute/data/humans, improve itself, and remain governable through transparent rules, human oversight, and credible exit mechanisms.

This definition deliberately does not require:

- a native token;
- a DAO structure;
- on-chain governance for every decision;
- decentralized model inference;
- a blockchain as the whole runtime.

Those may be useful in some designs. They are not the essence.

The essence is the resource loop plus governance.

A DAI needs to answer:

1. **Agency:** what can the AI do without asking permission every time?
2. **Budget:** what resources does it control?
3. **Revenue:** how does value enter the system?
4. **Spending:** what can it buy, and under what constraints?
5. **Improvement:** how does it upgrade its capabilities?
6. **Governance:** who sets limits, policies, and goals?
7. **Accountability:** who can inspect, stop, slash, reverse, or fork it?
8. **Exit:** how do humans leave or create an alternative if governance fails?

## The good ideas worth keeping

### 1. The AI as an economic actor

The old article imagined the AI model spending money to improve itself. That still feels like the central provocation.

If an AI can only respond to prompts, it is a service. If it can plan, spend, and coordinate, it starts to become an actor.

This does not mean giving it unlimited autonomy. It means designing bounded autonomy: budgets, policies, approvals, rate limits, audits, and kill switches.

The interesting design problem is not "should the AI be free?" It is: what kind of limited economic agency is useful and safe?

### 2. The split between work and self-improvement

The original article separated the AI's tasks into two broad categories:

- doing its job for users;
- managing and improving itself.

That split is still useful.

A real agentic organization has to decide whether to spend the next unit of budget on serving current users, improving evaluations, buying better data, hiring a developer, renting more compute, or building a new tool.

That is not just an AI problem. It is an organizational problem.

### 3. Human contributors as part of the loop

The old DAI model included developers, data providers, users, and other contributors. The vocabulary needs updating, but the idea is right.

Useful AI systems will not be purely autonomous. They will be hybrid systems where humans do the work that humans are still better at: judgment, taste, trust, accountability, domain expertise, adversarial review, and governance.

A DAI should not be imagined as an AI without humans.

It should be imagined as an organization where the AI can coordinate humans and where humans can constrain the AI.

### 4. Forking as governance

Forking sounded very crypto-native in the old article, but the underlying idea is broader.

Exit is one of the strongest governance tools.

If an AI system is open enough that its code, policies, memory, evals, and operational history can be copied or re-instantiated, then disagreement does not have to end in capture. A community can leave and create another version.

That matters for AI safety too. If the only powerful agents are closed systems controlled by a few companies, there is no real exit. If every system is open but chaotic, there may be no accountability. The right balance is unresolved, but the forking question is still important.

### 5. Open source and open data as a strategic question

The open DAI draft asked whether these systems should be open source and open data. That question is even more important now.

Open systems can be inspected, improved, forked, and trusted by communities. Closed systems can protect privacy, reduce abuse, and sustain a business model more easily.

A serious DAI stack probably needs selective openness:

- open policies and governance rules;
- auditable spending and decision logs;
- open interfaces;
- possibly open source agent code;
- protected private user data;
- controlled access to dangerous capabilities;
- clear boundaries around model weights, memory, and datasets.

## Toward an adequate stack

This is still TBD, but the stack should probably not be "LLM + blockchain".

It should be layered.

### 1. Agent runtime

The operational layer that lets the AI plan, call tools, write files, run jobs, remember context, and coordinate subtasks.

Examples of concerns:

- tool calling;
- memory;
- task queues;
- evaluation loops;
- permissions;
- human approval gates;
- observability;
- rollback.

### 2. Governance layer

The layer that defines what the agent is allowed to do.

This may include:

- a constitution or policy document;
- spending limits;
- approval thresholds;
- role-based permissions;
- audit logs;
- emergency stops;
- voting or council mechanisms;
- dispute resolution.

Some of this could be on-chain. Much of it may be ordinary software.

### 3. Economic layer

The layer that lets the agent hold and move value.

This is where crypto becomes relevant.

Possible components:

- stablecoin wallet;
- multisig custody;
- programmable spending limits;
- escrow;
- payment channels or low-fee rails;
- accounting;
- revenue tracking;
- budget allocation.

A native token is optional. In many cases it is probably a bad first move. A stablecoin budget controlled by policies and human signers may be enough.

### 4. Work marketplace

The layer where the DAI can buy help or sell services.

This could include:

- humans doing review, labeling, coding, research, design;
- APIs and SaaS tools;
- compute providers;
- data providers;
- model providers;
- other agents.

The original "miners" category becomes a broader supply side of capabilities.

### 5. Identity and reputation

The layer that tracks who is interacting with the DAI and why they should be trusted.

This matters for both humans and agents.

Possible components:

- cryptographic identity;
- reputation scores;
- credentials;
- contribution history;
- audit history;
- sybil resistance;
- human verification where necessary.

### 6. Transparency and audit

A DAI that can spend money and coordinate work needs to be inspectable.

At minimum:

- transaction history;
- major decisions;
- policy changes;
- model/tool changes;
- eval results;
- incidents;
- human interventions.

The more agency the system has, the more legible it must become.

## The open question

The interesting question is no longer:

> Can we put an LLM on a blockchain?

That was too narrow.

The better question is:

> What institutional stack does an AI agent need in order to act economically without becoming either powerless, captured, or dangerous?

Crypto may be part of the answer, not because crypto fixes everything, but because software-native money is a real primitive. DAOs may also become useful, not because they were inevitable, but because real AI agents may finally give them something concrete to govern.

In that sense, the old DAI idea was early and overfit to the wrong hype cycle.

But it was pointing at a real problem.

AI agency needs infrastructure.

And the first serious version of that infrastructure may look less like a chatbot, less like a DAO, and more like an institution that happens to have an AI at its center.
