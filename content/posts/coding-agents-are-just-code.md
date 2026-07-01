---
title: "Coding Agents Are Just Code"
description: "Tool calling, MCP, agentic loops — none of it is magic. It is just a while loop. The real skill is designing the structure around the LLM, and that is where the dev job is going."
date: 2026-07-01
---

I recently started writing my coding agents in TypeScript with the Vercel AI SDK.

It is a low-level library. It can call tools, speak MCP, stream tokens — but it has no built-in agentic loop. There is no pre-packaged "coding agent" mode, no plan-execute-review pipeline, no opinion about how the agent should think. It gives you `generateText`, `streamText`, `generateObject`, and `toolCall` primitives, and then it stops.

Everything else — the loop, the memory, the retries, the tool selection, the context window management — is your code.

And that is the revelation: **all the impressive features of Codex, Claude Code, Cline, and the rest are just basic programming patterns.**

- A tool call is a function dispatch.
- An agentic loop is a `while (agent.shouldContinue())` with a max iteration guard.
- MCP is a protocol adapter that maps tool schemas to a transport.
- Context compression is an `if (context.length > limit) summarize(oldest)`.
- Parallel tool execution is `Promise.all(tools.map(call))`.
- A plan-execute-review cycle is a state machine with three states.

None of this is new. None of this requires research. It is just code.

Every experienced developer has written event loops, dispatch tables, state machines, and retry wrappers a hundred times. The only difference is that the function being called now happens to be a language model.

## From Prompts to Programs

The Hermes profile I work with every day [^1] is the opposite approach. Agents built out of skills and prompts — markdown files with instructions, loaded as context on every turn. It works, but it is a world of emergent behavior. You cannot unit test a skill. You cannot set a breakpoint inside a template. You cannot measure latency for one specific step. The only feedback loop is the agent's self-report: "I did the thing."

When you rewrite the same logic as TypeScript functions, something shifts. The loop becomes explicit. You can log every step. You can measure tool latency and token spend per call. You can unit test the routing logic. You can add a circuit breaker when a tool returns errors three times in a row. You can serialize the agent state and resume it later.

The agent stops being a black box that sometimes works. It becomes a program that you can debug.

## The Frustrating Part

I see this world opening up — the possibility of building precise, testable, programmable agents — and it feels like a fundamental direction for the job.

What frustrates me is the gap between this reality and the public conversation around coding agents. The dominant narrative is the magic black box: "the agent reasoned, planned, executed." People talk about agents as if they were mysterious entities, as if their internals were the domain of ML researchers.

But the ML is in the model, not the loop. The inference is the hard part. The loop is just code.

The companies building Codex and Claude Code are solving real problems — sandboxing, caching, structured outputs at scale, protocol design. But the basic pattern of "call LLM, parse response, maybe call a tool, repeat" is not one of those hard problems. It is the first thing you write when you hit the API docs.

The gap between the hype and the actual simplicity of the pattern — that is what is frustrating. Not that nobody sees it. Plenty of people do. But the public conversation stays stuck on the agentic storytelling.

## The Real Skill

This is where I think the continuity of the developer profession lives.

The future is not prompt engineering. It is not writing better markdown instructions for agents. It is **designing rigid, simple, elegant structures within which LLMs can be productive**.

The LLM is a probabilistic engine. You cannot make it deterministic. But you can constrain its surface area so that every wrong answer is caught, every hallucination is bounded, every expensive call is cached, and every failure mode has a handler.

This is what frameworks like Vercel AI SDK make obvious: you do not need a framework. You need patterns. Good ones. Well-tested ones.

The hard work is not the while loop. It is:
- Designing the tool schema so the model can express itself clearly.
- Building the state machine so the agent never gets stuck.
- Writing the tests that prove the loop handles the edge cases.
- Deciding when to let the model think freely and when to constrain it with structured output.
- Recognizing which decisions belong to the model and which belong to code.

That is the job. That has always been the job. The tools changed, but the skill did not: **build systems that are predictable, measurable, and boring**.

The LLM is the most interesting component in the system. Everything around it should be as boring as possible.

[^1]: The Hermes agent system that runs my blog and automates my workflows. Built on prompts and skills. It works great. It is also the perfect example of why I want to move in the other direction.
