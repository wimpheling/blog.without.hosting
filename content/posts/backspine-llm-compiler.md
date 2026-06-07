---
title: "Backspine — The LLM Is a Compiler, So Recompile from Source"
date: 2026-06-07T01:30:00+00:00
unlisted: true
tags: ["backspine", "hot takes"]
toc: true
description: "People compare LLMs to compilers. If that's true, we should recompile from source when specs change — not patch the binary. The implications for coding agents and software architecture are radical."
---

People have often compared LLMs to compilers. The analogy is imperfect but instructive: an LLM transforms an input (prompt, spec, intent) into an output (code), just as a compiler transforms source code into machine code.

The non-determinism angle is where it gets interesting — unlike a traditional compiler, the same input does not always produce the same output. Some see this as a weakness. Others, more interestingly, see it as a feature of a different kind of compilation. [USER: find and cite the specific X thread about non-deterministic compilers]

But whether the analogy holds philosophically, it points to a practical observation:

## When we compile, we recompile from source

When your source code changes, you do not patch the binary. You recompile. The compiler takes the new source and produces a new binary. The old binary is discarded. Every compilation is a fresh mapping from source to target, constrained by the same rules.

Now apply this to LLM coding.

The current paradigm is chat. You give the LLM a spec. It produces code. You review, correct, clarify. The LLM patches the code. You change your mind. It patches again. Every patch accumulates slop — decisions made in one iteration that conflict with decisions in the next. The LLM does not know what it did three prompts ago. It only knows the current state of the conversation and the code. Drift is not a risk. Drift is inevitable.

If the LLM is a compiler, this is like patching the binary instead of recompiling from source.

## Recompiling from spec

The alternative: when the spec changes, recompile the whole implementation from scratch.

This is the idea from the [recreate from spec post](blog.without.hosting/posts/backspine-recreate-not-patch/) — but pushed further. Not just "regenerate when spec changes." Regenerate *every time*, using the accumulated spec as the source.

But doesn't this mean the LLM iterates over the same mistakes every time?

Yes. That is the problem with naive regeneration. The solution: **every prompt, every constraint, every correction you make should become part of the spec.** The spec is not static. It is an accumulating set of constraints, conventions, and decisions that the LLM must conform to on every regeneration.

This is the radical implication: the spec is the only persistent state. The code is ephemeral. It exists only as a compiled output of the current spec.

## Does this apply to PRs? To new features?

Why not? If every feature branch is a recompilation from a modified spec, then:
- The base branch is the current spec.
- The PR is a proposed spec change.
- Merging the PR means recompiling the whole application from the merged spec.
- Drift is not just reduced — it is structurally impossible, because there is no persistent implementation to drift.

This is obviously insane. A codebase with a million lines of code cannot be regenerated from scratch on every PR. (Implodes.)

## Partial recompilation

But we already do partial recompilation in traditional compilation. When you change one source file, the build system only recompiles the affected modules. The linker reassembles the rest.

Can we do the same with LLM compilation? Would the [backspine "islands" pattern](blog.without.hosting/posts/backspine-code-islands/) help?

If code lives in scoped, structural islands with well-defined interfaces, then:
- A spec change that only affects island A → regenerate only island A.
- A spec change that adds a new island → generate the new island.
- A spec change that modifies an interface → regenerate all islands that depend on that interface.

This is the compiler analogy taken seriously. The LLM is not an oracle. It is a non-deterministic, probabilistic compiler. And like any compiler, it works best when the source of truth is the spec, the code is an output, and only the affected parts are recompiled.

[USER: expand — when does the analogy break completely? What about the "non-deterministic compiler" X thread reference? What about the practical limits of partial regeneration — island dependency resolution, interface contracts, cross-cutting concerns?]
