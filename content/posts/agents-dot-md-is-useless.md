---
title: "AGENTS.md Is Useless"
date: 2026-07-22
tags: ["hot takes", "agents"]
description: "The convention of writing special agent documentation files is based on a sci-fi trope — that LLMs need an esoteric format to understand a project. They don't. They read README.md just fine."
unlisted: false
---

There is a growing convention in open source: an `AGENTS.md` file, sometimes `CLAUDE.md`, sometimes `.cursorrules`. It is supposed to be the documentation *for the AI*, separate from the documentation *for the humans*.

This is based on a sci-fi trope. The idea that an artificial intelligence needs a special language, a special format, a special protocol. That the machine cannot just read what the humans wrote — it needs its own annotated version.

## The Vaporwave Interface

You know the aesthetic. Green text on black background. ASCII art skulls. Greek letters. Binary sequences. The Macintosh Plus *[Floral Shoppe]* album cover. The idea that communicating with an AI requires something that *looks* like machine language, that *feels* like hacking the mainframe.

AGENTS.md is the same aesthetic, translated into markdown convention. It says: this document is not for you, human. It is for the *other* intelligence. The one that needs things in a special format.

The problem is that LLMs are not that kind of intelligence. They are trained on *our* language. They understand README.md, CONTRIBUTING.md, architecture docs, inline comments, and commit messages — because those are all written in natural language, which is what they process.

There is no alien intelligence that needs a Rosetta Stone. There is a next-token predictor that reads English as well as it reads anything.

## The Fragmentation Tax

Even if you accept the premise, the execution is broken. Every agent platform wants a different format:

- Claude Code parses `CLAUDE.md` with specific markdown conventions — sections, bullet points, particular phrasing that triggers its internal instruction parser.
- Cursor uses `.cursorrules` with its own structure.
- Copilot has its own conventions.
- Windsurf, Zed, Codex — each one reinvents the format.

Pick any three and you are maintaining three versions of the same rules, in three incompatible formats, all saying roughly the same thing: "here is how this project works."

This is not documentation. This is configuration fragmentation.

## The Real Cost: Schizophrenia

Here is the part nobody talks about. If you maintain an AGENTS.md, you now have *two* documentation surfaces:

1. The docs for humans: README.md, the wiki, the architecture docs.
2. The docs for agents: AGENTS.md, CLAUDE.md, .cursorrules.

These diverge on day one. You update the README but forget the AGENTS.md. Or you put a critical constraint in AGENTS.md that a human developer never sees because they read the README. The project develops a split personality — one version of itself for people, another for machines.

The implied solution — "just write good documentation and the agents will figure it out" — is dismissed as naive. But it is actually the correct default.

## What Agents Actually Need

Agents need what human developers need:

- A clear README that explains what the project is and how to run it.
- Well-named files and modules.
- Meaningful function signatures and types.
- Good comments in tricky code.
- A reasonable directory structure.

That is it. The model processes English. You do not need to write in a special register. You do not need to prefix every instruction with `[AGENT INSTRUCTION]`. You do not need to create a second documentation layer.

The v0 of a real solution is to improve the existing documentation until the agent can navigate it. If the agent cannot understand your project from the README, the problem is the README, not the lack of AGENTS.md.

## The Exception That Proves the Rule

There is one legitimate use case for AGENTS.md-like files: **project-specific behavioral constraints** that would be noise in human docs.

"Never edit this file." "Always prefer X library over Y." "Only modify files under src/ — everything else is generated."

These are useful. But they are not documentation. They are configuration. And they should be formatted in a way that survives fragmentation — which means keeping them small, specific, and tool-independent.

If your AGENTS.md is longer than 20 lines, you have a documentation problem masked as an agent problem.
