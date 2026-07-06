---
title: "Backspine — What a Design System Architecture Looks Like When the Agent Writes It"
date: 2026-07-07T00:00:00+00:00
unlisted: true
tags: ["backspine", "design systems", "ai"]
toc: true
description: "Four layers from abstract TypeScript interfaces to automated Storybook screenshot diffing — and why each one exists in response to a specific agent failure mode."
---

This is the technical sibling to [the abstract design system setup](https://blog.without.hosting/posts/backspine-abstract-design-system-setup/). That post made the philosophical case: the design system is the agent's vocabulary, not a component gallery. This one is the concrete architecture that emerged from actually writing code with it.

The stack has four layers, each solving a specific problem the agent kept hitting.

## Layer 1: Abstract Components (Pure TypeScript)

The base unit is an abstract component — a TypeScript interface with zero runtime dependencies.

```typescript
// design-system-contract/src/button.ts
export interface ButtonProps {
  label: string
  variant: 'primary' | 'secondary' | 'ghost'
  disabled?: boolean
  onClick: () => void
  loading?: boolean
}

export type ButtonComponent = React.ComponentType<ButtonProps>
```

No React imports. No JSX. No CSS. Just types.

The constraint is enforced by a custom linter: a file in the contract package cannot import from React, React Native, or any DOM library. If the agent tries to put runtime logic in the contract, the build fails. The contract is pure vocabulary — it names the thing and its shape, nothing else.

Why this exists: the agent kept putting implementation details into interface definitions. Event handlers, platform-specific types, CSS class names. Separating contract from implementation forces the agent to think about the *concept* before the *rendering*.

## Layer 2: Concrete Implementations (Per Runtime)

Each abstract component gets one or more implementations:

```
design-system-basic/         # React (web)
  button.tsx                 # ButtonComponent implementation
  styles.css                 # Web-specific styling

design-system-mobile/        # React Native
  button.tsx                 # Same ButtonComponent, different runtime
```

The contract package knows nothing about which implementation will be used. The facade package wires them together:

```typescript
// design-system/src/index.ts
export { Button } from '@backbone/design-system-basic'
// or, for mobile:
// export { Button } from '@backbone/design-system-mobile'
```

Same interface, same props, same Storybook stories — different rendering paths.

Why this exists: the agent kept writing platform-specific components that couldn't be reused. Abstracting the contract means Storybook stories work for both web and mobile without modification. The story is written against the interface, not the implementation.

## Layer 3: Composites (Component-Only Composition)

A Composite is a React component whose entire body is composition of abstract components — no raw HTML, no inline styles, no CSS modules of its own.

```typescript
// This is allowed: a component file in the components directory
// containing raw elements + styles

// This is NOT allowed: a file outside the components directory
// using <div>, <span>, or importing CSS

// This is the sweet spot:
const EmptyStateCard = ({ title, message, action }) => (
  <Card>
    <EmptyState icon={archive} />
    <Heading>{title}</Heading>
    <Text>{message}</Text>
    <Button onClick={action.onClick}>{action.label}</Button>
  </Card>
)
```

Composition-only. Every child is an abstract component. The linter enforces this: raw JSX elements in a composite file = build failure.

Why this exists: without the constraint, composites were indistinguishable from pages. The agent would inline layout logic, styling tweaks, and one-off markup into every composite, making them context-dependent and non-reusable. The linter forces composites to be pure vocabulary — compositions of named things, not ad-hoc markup.

## Layer 4: Pages (Strict UI / State Separation)

A Page is a special case of Composite with a critical extra constraint: UI and state management are separate files.

```
pages/
  dashboard/
    dashboard.page.tsx       # Pure UI — components + composites only
    dashboard.state.ts       # State management, data fetching, handlers
```

The `.page.tsx` file renders UI only. It imports components and composites, wires them to props, and exports nothing but the render function. It can be used directly in Storybook because it has no runtime dependencies — just props.

The `.state.ts` file owns the logic: API calls, form state, navigation, side effects. It produces the props that the page UI consumes.

And because the UI is pure composition of abstract components, the page sometimes works unmodified on both web and mobile — swap the implementation package, keep the same page structure. The state management layer might differ (different routing, different storage), but the rendering layer is portable.

Why this exists: the agent kept mixing data fetching and rendering in the same component, making pages impossible to storybook, hard to test, and tightly coupled to the runtime. Splitting them means the UI layer is testable, previewable, and — occasionally — portable.

## The Storybook Screenshot Pipeline

This structure is unusually Storybook-friendly because every layer is already declarative and UI-pure:

- **Abstract components** → one story per prop combination
- **Composites** → stories for each composition variant
- **Pages** → stories with mock state, no server needed

The automation: each commit triggers a Storybook build, puppeteer screenshots every story, and a visual diff tool compares against the baseline. The output feeds directly into a design review loop — a graphic design agent can inspect the diffs, flag regressions, and propose CSS adjustments without touching business logic.

[USER: write — the actual tooling choices and pipeline shape. What runs the screenshots? How does the design agent interact with the diff output?]

## Why This Works for Agent-Generated Code

Every layer exists because the agent did something wrong without it:

- **Abstract contracts** → agent put implementation detail in interface definitions
- **Per-runtime impls** → agent wrote platform-locked components
- **Composites** → agent treated every composition as a bespoke page
- **Page split** → agent fused rendering and state into untestable blobs
- **Storybook pipeline** → agent couldn't visually verify its own output

The constraints are not aesthetic. They are scars from specific failure modes, turned into lint rules.

[USER: write — the conclusion. How does this compare to a human-designed design system? What's worse? What's unexpectedly better?]