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

The other half of this: **choose parametric surfaces, not sample banks.**

A sample bank gives you a fixed recording. A snare hit is a snare hit. You cannot tighten the skin, move the microphone, or change the shell depth. The model's output is a sample index — a catalog lookup, not a parameter change.

A parametric surface exposes every dimension of the sound as a continuous value. The model outputs *floats*, not indices. This is the [code islands](https://blog.without.hosting/posts/backspine-code-islands/) pattern in sound: the snare is a scoped, parameterized unit. Changing the tension does not change the kick.

## Two kinds of parametric surfaces

My first version of this post drew a false line: "sample-based VSTs have no parameters, physical modeling VSTs do." That was wrong. Let me be more precise.

A drum VST exposes *two different parametric domains*, and they are not the same thing:

**1. Sound-modeling parameters** — change the drum itself. Shell depth, head material, tuning, skin tension, beater type. These only exist in physical-modeling engines like Modo Drum, where every drum component is a simulated physical object with continuous properties.

**2. Post-processing / mix parameters** — change how the recorded (or modeled) sound is shaped and blended. Mic mix, EQ, compression, envelope, transient shaping, bleed. These exist in *every* modern drum VST, regardless of whether the source is samples or a model.

Steven Slate Drums 5.5 is a good example of domain (2). The drum hits are pure samples — multi-velocity, multi-mic recordings of real kits in Slate's studios. You cannot change the shell resonance or the head material. But the mixer strip exposes a rich parametric surface:

- **Mic mix** — per-mic volume faders (Kick In, Kick Out, Snare Top, Snare Bottom, OH, Room, etc.). The agent can blend mic positions continuously.
- **3-band EQ** — gain and frequency per band, automatable.
- **Compressor** — threshold, ratio, attack, release, makeup gain. Full VST automation.
- **Envelope** — attack and release shaping per channel.
- **Reverb send**, master tone filter, pan, output routing.

That is roughly 15 automatable parameters per channel across 12+ channels — about 200 total. Not bad for a "sample player."

Superior Drummer 3 pushes this further: per-mic bleed sliders, dedicated transient shaper (attack + sustain), fully parametric 4-band EQ, and a modular FX rack. Hundreds of automatable parameters across a full kit. Addictive Drums 2 adds a "Sound Designer" tab with pitch and damping controls that *simulate* modeling on top of samples.

The real distinction:

| Domain | What it controls | Example | VSTs |
|--------|-----------------|---------|------|
| Sound modeling | The drum itself — shell, head, tuning | "Snare shell resonance: 0.72" | Modo Drum (paid) |
| Post-processing | Mix of the recorded sound — EQ, comp, blend | "Kick mic blend: close 0.6, room 0.3" | SSD 5.5, SD3, AD2, BFD3, EZD3 |
| Synthesis | The sound from scratch — oscillators, FM | "Kick: sine sub 80Hz, FM ratio 3, decay 200ms" | Operator, Analog (built into Live) |

All three are valid parametric surfaces for an agent. The difference is *what the parameter controls* — and therefore what the agent's spec can meaningfully adjust.

The constraint is real but specific: with sample-based VSTs, the drum *tone* is frozen at recording time. The agent cannot tighten the snare skin on a sample of a loose snare. But it can:
- Blend to a different mic that captured the snare differently
- EQ out the boom and emphasize the crack
- Compress and shape the transient
- Add room bleed for depth

That is not nothing. It is a different capability class from "change the shell depth from 5" to 6.5" and hear the difference," but both are parametric control surfaces. The blog post should not conflate mixing automation with sound synthesis.

[USER: write — for the agent loop, does it matter whether the parameter controls post-processing of a fixed sample vs physical properties of a model? The spec says "tighter snare" — the agent that has SSD has to achieve this via EQ + compression + mic blend. The agent that has Modo Drum can dial skin tension up. Are these equivalent from the spec perspective? Or does the agent need to know its parametric surface?]

## What exists today

The parts exist:

| Domain | What exists today | Automatable |
|--------|------------------|-------------|
| Sound modeling | Modo Drum (paid) | Shell depth, head material, tuning, tension — all floats |
| Post-processing | SSD 5.5, SD3, AD2, BFD3, EZD3 | Mic mix, EQ, compression, envelope, transient, bleed — all floats |
| Synthesis | Operator, Analog (built in Live) | Every oscillator, envelope, modulation parameter |
| Spec agent | Does not exist | The model that listens and decides what to change |

What does not exist yet is the *agent layer* that connects them: a model that hears raw Ableton output, decides "the snare needs more body, tighten the skin from 0.6 to 0.72 and move the mic from 0.3 to 0.4", and outputs those parameters — without trying to generate the actual waveform.

[USER: write — is this just a MIDI effects rack with an LLM backend? Or does it need a full plugin host? Where does the backspine boundary between agent and execution sit?]

## The harder question: melody, harmony, structure

Drums are the easy case. Deterministic parameters map naturally to percussion — hit or don't hit, at what velocity, with what timbre.

Melody and harmony are harder. A chord progression is not a set of MIDI notes — it is a *constraint* on which notes are available, at what density, over what time span. The model that generates a drum pattern from "tight snare, no bass" is simpler than the model that generates a chord voicing from "suspended, open voicing, avoid the third."

But the same pattern holds: output MIDI + VST params, not audio. The piano VST plays the MIDI deterministically. The model only decides the notes and the timbre.

[USER: write — where does this pattern break? Melody generation with expressive orchestral VSTs? Acoustic instruments where the VST model is the sound?]