# Blog nudge automation architecture

Use this when changing the blog-writer Telegram/cron nudge system.

## Separation of responsibilities

Keep three layers separate:

1. **Scheduling/orchestration** decides whether a cron tick should produce a nudge.
2. **Nudge generation** selects a candidate draft/idea and writes one conversational nudge.
3. **Transport/command integration** delivers the returned text through cron or Telegram command handlers.

Avoid one vague `maybe_send_nudge()` function with flags for every mode. Prefer explicit public flows:

```python
run_cron_tick(deps)          # scheduled path; may be silent
generate_manual_nudge(deps)  # manual path; always tries to generate now
get_state_json(deps)         # read-only introspection path
```

## Manual command behavior

`/nudge` should generate one nudge immediately. It should skip:

- active-window checks
- daily plan creation/due checks
- daily scheduled count limits

It should still use:

- repo/post inspection
- candidate selection
- recent post/nudge avoidance
- LLM nudge generation
- read-link rules
- recent history updates

Manual nudges should not consume a scheduled slot, but they should update recent-history state so the next scheduled nudge avoids repeating the same post.

`/nudge-state` should be read-only and return the current state JSON, pretty-printed. If state is missing, return a clear short message such as: `No nudge state exists yet. It will be created on the first cron tick inside the active window.`

## State shape

A useful state includes:

- `nudge_day`
- `timezone`
- generation timestamp
- active window start/end
- planned nudge slots with sent markers
- recent posts
- recent nudges, including `source: "manual" | "scheduled"`

## Test matrix

Cron flow tests:

- outside active window: no generator call
- inside window first tick: plan created, no generator call unless due
- before planned time: no generator call
- after planned time: generator called once
- successful scheduled nudge marks the planned slot sent

Manual flow tests:

- works outside active window
- works with no daily plan
- does not mark a planned item sent
- updates recent nudges
- generator called once

State command tests:

- returns state without mutating it
- handles missing state gracefully

## Delivery rule

The generation/service layer returns text. It should not send Telegram messages itself.

- Cron prints non-empty text; Hermes cron delivery sends it.
- Telegram command handler returns command output as the reply.
- Tests inspect returned text directly.
