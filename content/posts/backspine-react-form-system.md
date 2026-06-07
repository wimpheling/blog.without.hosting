---
title: "Backspine — Adding a React Form System"
date: 2026-06-07T01:35:00+00:00
unlisted: true
tags: ["backspine", "react", "forms"]
toc: true
description: "Backspine probably needs a declarative React form system: routes and payloads are not enough if the framework cannot express input, validation, errors, and submission flows cleanly."
---

Backspine probably needs a React form system.

Not because forms are exciting. Forms are never exciting. Forms are where web applications go to become annoying.

But if Backspine wants to focus on product structure — routes, payloads, database, pages, and e2e tests — then forms are unavoidable. Most application behavior eventually becomes: show fields, validate input, submit payload, handle errors, update state.

If the framework cannot express that cleanly, the whole "AI-assisted web development" story will collapse into handcrafted form glue.

## The requirement

The form system should be declarative enough that an agent can reason about it.

I do not want the agent to invent a new messy React form implementation every time a page needs user input. I want forms to be part of the product structure.

Something like:

- fields
- types
- validation
- default values
- conditional visibility
- payload mapping
- submit action
- optimistic behavior
- error states
- success states
- e2e expectations

The important part is not just rendering inputs. The important part is that the form describes the user interaction as a structured object.

If the assistant creates a signup feature, I want to see:

- route: `/signup`
- payload: `SignupPayload`
- database effect: create user
- page: signup form
- validation: email, password, terms
- tests: valid signup, invalid email, weak password, duplicate email

The form is the bridge between page, payload, validation, and test.

## Use an A-grade system if it exists

The first move should not be to implement a form framework from scratch.

The first move should be to find the best declarative-oriented React form system and see if it fits Backspine.

Candidates to investigate:

- **React Hook Form** — probably the default serious React form library; good performance, schema resolver ecosystem, but not necessarily declarative enough at the product-structure level.
- **TanStack Form** — more recent, typed, headless, and potentially closer to a framework-level abstraction.
- **Formik** — historically important, but likely too old/heavy for this direction.
- **Uniforms** — interesting because it generates forms from schemas, which is closer to the Backspine idea.
- **JSON Forms** — declarative JSON-schema-driven forms; maybe too enterprise/JSON-schema-ish, but worth checking.
- **React JSON Schema Form** — old but relevant if the goal is schema-to-form.
- **Conform** — interesting if the stack leans into web standards and server actions rather than purely client-side form state.

The question is not "which library has the nicest input components?"

The question is: which system lets us describe forms as stable product structure that an AI agent can modify without turning the UI into spaghetti?

## What Backspine needs from it

A Backspine form system should probably be:

- **declarative** — the form can be represented as data/spec, not only JSX control flow;
- **typed** — payloads and validation should line up with TypeScript types;
- **schema-aware** — Zod, Valibot, JSON Schema, or something equivalent;
- **headless** — the design system owns the rendering;
- **testable** — e2e cases can be derived from validation and states;
- **agent-friendly** — an LLM can add a field, change validation, or wire a submit action without touching five unrelated files;
- **diffable** — changes should be legible as product changes, not as random React noise.

This last point matters.

If adding a field requires editing JSX, validation, payload type, server handler, database mutation, and test manually, the agent will drift. It will miss one. Or it will patch three different patterns together.

A declarative form spec gives the agent a smaller target.

## Maybe we implement it ourselves

If there is an A-grade system that fits, use it.

If not, implement the minimal Backspine form layer ourselves.

Not a full form library. That would be a trap.

A thin layer:

- form spec
- field registry
- schema binding
- generated React component
- generated payload type
- generated tests or test hints
- design-system rendering adapter

The form library underneath could still be React Hook Form or TanStack Form. Backspine does not need to own focus management and dirty state unless absolutely necessary.

Backspine should own the product-level declaration:

```ts
const signupForm = form({
  payload: "SignupPayload",
  fields: {
    email: field.email().required(),
    password: field.password().minLength(12),
    acceptTerms: field.boolean().mustBeTrue(),
  },
  submit: action("signup"),
  tests: [
    "reject invalid email",
    "reject weak password",
    "create user on valid submit",
  ],
})
```

The exact syntax does not matter yet. The boundary matters.

The AI should edit the form spec, not improvise a bespoke React form.

## Why this belongs in Backspine

Forms are one of the places where application semantics are most visible.

A route without a form is often just a page. A form is where the user gives intent to the system. It is where payloads are born. It is where validation becomes UX. It is where backend rules become visible.

So forms should not be an afterthought.

If Backspine is about keeping the developer focused on product structure, then forms are a first-class structure.

The nice version: find a great declarative React form system and wrap it.

The brutal version: implement the missing layer ourselves.

[USER: expand — actually evaluate the candidate libraries. Which one is most compatible with Backspine: React Hook Form + Zod, TanStack Form, Uniforms, JSON Forms, RJSF, Conform, or a custom spec layer over a headless library?]
