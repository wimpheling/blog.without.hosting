---
title: "Backspine for Music — Don't Generate Audio, Generate Instructions"
date: 2026-06-11T20:00:00+00:00
unlisted: true
tags: ["backspine", "music"]
toc: true
description: "The backspine pattern applied to AI music generation: instead of generating raw audio (Suno-style, with inevitable drift), generate deterministic MIDI + instrument parameters from an agent listening to your DAW."
---

I keep bumping into the same problem with AI music generation: **drift.**

Not musical drift (key changes, genre shifts). *Parametric* drift. I ask for a drum track. I get drums with bass. Then some guitar. Then a pad. The model interpreted "drum track" as "a song built around drums" and kept adding instruments until it was a full track I didn't ask for.

This is exactly the same structural problem as [patching the binary instead of recompiling from source](https://blog.without.hosting/posts/backspine-llm-compiler/). The intermediate representation — raw audio — is opaque, so the model has no way to *hold the constraint* across generations. Every generation is a new probabilistic roll of the dice.

## What changed

Two things make this worth revisiting:

1. **Ableton just released a plugin SDK** that lets you integrate tightly with plugins inside Live. Your agent can talk to Ableton at the VST level — read state, set parameters, route audio.

2. **Audio LLMs are getting good enough to treat raw audio as an input.** Stable Audio, Google Magenta, and the newer models can analyze a waveform and extract musical structure. They are not just generators anymore — they are *listeners*.

Together, these unlock a different architecture.

## The backspine pattern for music

The [backspine philosophy](https://blog.without.hosting/tags/backspine/) says: keep the spec clean, treat generated artifacts as ephemeral, use deterministic boundaries between agents and execution.

For music production:

- **Spec**: "a drum track, kick on quarters, snare on 2 and 4, hat on 8ths, no other instruments, snare skin at medium tension"
- **Compilation output**: MIDI clip + VST preset parameters (not audio)
- **Deterministic layer**: Ableton's transport, the VST itself, the MIDI protocol
- **Non-deterministic layer**: the model that listens to raw audio and decides what MIDI + params to output next

The spec compiles to instructions, not audio. Audio is the output of the *instruments* executing those instructions deterministically.

## Why this fixes drift

Suno drift happens because the model generates audio directly. Audio is a single medium — you cannot separate "kick pattern" from "kick sound" from "snare presence" in a waveform. Every generation is a fresh probabilistic sample where the constraints have to be re-inferred from the prompt.

If instead:

1. An agent listens to the raw Ableton output
2. It outputs a MIDI clip (notes, velocities, timing)
3. It outputs VST parameter maps ("snare skin tension 0.6", "kick decay 120ms", "hi-hat level -6dB")
4. Ableton plays these through the actual VSTs deterministically

Then the model only has to get the *intent* right. The execution is handed off to the DAW and the VST, which are deterministic by construction. On the next iteration, the model hears the actual output and adjusts the MIDI/params — not probabilities over raw samples, but precise edits to structured data.

This is the [recompile from spec](https://blog.without.hosting/posts/backspine-recreate-not-patch/) pattern applied to sound. The spec accumulates: "tighter snare" becomes "snare skin tension 0.6 → 0.75". The MIDI is regenerated with the updated parameter. The audio is a side effect.

[USER: write — how does the loop actually work? Agent hears Ableton out, decides on next MIDI/param change, Ableton loops, next iteration. What's the latency model? Can this be real-time or does it need regions/bars?]

## Parametric drumkits, not sample banks

The other half of this: **choose parametric VSTs, not sample banks.**

Sample banks give you fixed recordings. A snare hit is a snare hit. You cannot tighten the skin, move the microphone, or change the shell depth. The model's output is a sample index — a catalog lookup, not a parameter change.

Parametric drumkits (like Ableton's Drum Machine or third-party physical-modeling VSTs) expose every dimension of the sound as a continuous parameter. Skin tension. Shell resonance. Mic position. Room size. The model can output *floats*, not indices.

This is the [code islands](https://blog.without.hosting/posts/backspine-code-islands/) pattern in sound: the snare is a scoped, parameterized unit with well-defined inputs. Changing the tension does not change the kick. The sound designer can optimize the snare without side effects.

[USER: write — what parametric VSTs actually work well for this? Ableton Drum Machine? Physical modeling? What's the MIDI/parameter mapping latency?]

## What exists today

The parts exist:

- **Ableton SDK** (2026) — plugin integration, parameter access, audio routing
- **Stable Audio** / **Google Magenta** — audio analysis and structured output extraction
- **MIDI** — deterministic, well-understood instruction format
- **Parametric drum VSTs** — continuous parameter surfaces for physical sound modeling

What does not exist yet is the *agent layer* that connects them: a model that hears raw Ableton output, decides "the snare needs more body, tighten the skin from 0.6 to 0.72 and move the mic from 0.3 to 0.4", and outputs those parameters — without trying to generate the actual waveform.

[USER: write — is this just a MIDI effects rack with an LLM backend? Or does it need a full plugin host? Where does the backspine boundary between agent and execution sit?]

## The harder question: melody, harmony, structure

Drums are the easy case. Deterministic parameters map naturally to percussion — hit or don't hit, at what velocity, with what timbre.

Melody and harmony are harder. A chord progression is not a set of MIDI notes — it is a *constraint* on which notes are available, at what density, over what time span. The model that generates a drum pattern from "tight snare, no bass" is simpler than the model that generates a chord voicing from "suspended, open voicing, avoid the third."

But the same pattern holds: output MIDI + VST params, not audio. The piano VST plays the MIDI deterministically. The model only decides the notes and the timbre.

[USER: write — where does this pattern break? Melody generation with expressive orchestral VSTs? Acoustic instruments where the VST model is the sound?]