# Blog writer agent

This directory contains the source code and reusable instructions for the blog's Hermes-powered writing assistant.

Tracked here:

- `scripts/nudge_tick.py` — scheduled and manual blog nudge logic.
- `plugins/blog-writer-commands/` — Telegram slash commands such as `/drafts`, `/nudge`, and `/nudge-state`.
- `skills/blog-writer-workflow/` — the profile skill that describes the blog editing and nudge workflow.

Not tracked here:

- Telegram bot tokens, GitHub PATs, OAuth files, `.env`, or other secrets.
- Hermes runtime state: `state.db`, gateway sessions, logs, cron output, scheduler state, and caches.
- `scheduler/nudge_state.json`, which records recent nudges and planned slots at runtime.

The live Hermes profile should point to these files via symlinks/wrappers, while private runtime state stays under the Hermes profile directory.
