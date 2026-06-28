---
title: "What if WordPress Was a Proved Theorem"
date: 2026-06-28T10:00:00+00:00
unlisted: true
tags: ["backspine", "formal systems", "wordpress", "ai"]
toc: true
description: "WordPress lowered the barrier to web authoring. AI can do the same for app development. What if you could prove your whole app correct, then prompt anything into it without breaking anything?"
---

WordPress is great software. It is also terrible software. Both are true.

For developers, WordPress is an embarrassment of outdated PHP, global state, SQL injection vectors disguised as an API, a plugin ecosystem where nobody can prove the composition is safe. It has been unfashionable since before fashion mattered to web devs. If you asked a modern framework enthusiast to design a system that violates every principle of sound engineering, they would struggle to match WordPress's achievement.

And yet. WordPress powers ~43% of the web. That number is not an accident.

WordPress succeeded because it solved the right problem: **it lowered the friction between "I have something to say on the internet" and "there is a published, styled, URL-addressable page saying it."** Before WordPress, publishing a blog meant: buy hosting, configure Apache, install PHP, write HTML or install a CMS that felt like configuring a nuclear reactor, theme it, deploy it. WordPress turned that into: install, pick a theme, write, publish. The technical knowledge required dropped from "can configure a LAMP stack" to "can use a web form."

That is not a blog. That is a web app. And WordPress is, in disguise, a framework for building it.

## The CMS-MVC Mirror

Think about what WordPress does at the structural level:

- **Content types** define your model. A "post" has title, body, date, author, categories. A "custom post type" is just another table with columns.
- **The admin interface** is a CRUD controller, generated from the model definition.
- **Themes** are views, templates rendering model data into HTML.
- **Plugins** extend the controller layer with hooks and filters.

This is architecturally close to the MVC pattern that dominated web development in WordPress's heyday. Rails, Django, CakePHP, Symfony — they all had models, views, controllers, and migrations. WordPress had posts, themes, plugins, and `ALTER TABLE` queries hidden in plugin activation hooks.

Drupal saw this more explicitly. Drupal's CCK (Content Construction Kit) let you define content types through the admin UI — create a "Product" type with "price" and "SKU" fields without writing a single SQL statement. This was the correct insight: **if content types are just tables, why can't non-developers create them?**

But Drupal's data model punished this insight. The `node` table was a god table. CCK stored field data in a way that made every query a complex join chain. Performance cratered as content types multiplied. The model was too generic — it tried to be everything and paid for it in query planner misery. WordPress's model stayed simpler and dumber, which made it faster for the common case, which made it win.

The lesson: **making a database-backed web app accessible to non-developers requires an abstraction that is generic enough to be flexible but specific enough to be performant.** WordPress found that sweet spot accidentally, through years of incremental PHP cruft. Drupal found a better abstraction and was punished for it.

## AI Does the Same Thing, Better

This is the Backspine thesis.

The WordPress insight was: if you give people forms instead of SQL, they can build web apps. The next insight: if you give people natural language instead of forms, the same barrier drops again.

Backspine's approach has two parts:

1. **Declarative surfaces** — the developer's interface is not a chatbot transcript. It is routes, payloads, database shape, pages, and e2e tests. These are the *material of the product*, and Backspine surfaces them directly. You stay close to the thing you are building, not to the agent's internal monologue. ([Put the Vibe Back in Vibe Coding](https://blog.without.hosting/posts/backspine-put-the-vibe-back-in-vibe-coding/))

2. **A rigorous engine** — the spec is the source of truth. Code is a compiled output of the spec. When the spec changes, you recompile the affected islands. The agent does not patch a binary; it regenerates from the spec. Every constraint you discover during iteration goes into the spec, not into chat history. Drift is structurally impossible because there is no persistent implementation to drift. ([Recreate, Don't Patch](https://blog.without.hosting/posts/backspine-recreate-not-patch/), [The LLM Is a Compiler](https://blog.without.hosting/posts/backspine-llm-compiler/))

Together, these let a moderately tech-savvy person manipulate a Postgres-backed webapp by prompting. They describe what they want — "add a product page with a price field and a reviews section" — and the spec updates, the islands recompile, the app evolves. This is WordPress for apps, but with actual engineering discipline.

## Now Take It Further

What if the engine were not just rigorous, but *proved*?

The current limit on app development in a formal system is complexity. With a reduced set of primitives — types, functions, transactions, state transitions — you can express an arbitrarily complex system with unprovable properties. This is the shadow of Gödel: any sufficiently expressive formal system contains true statements that cannot be proved within the system.

But is a WordPress blog "sufficiently expressive"?

A blog engine, in its simplest form, is dramatically less complex than a general-purpose programming language. It is a database with migrations, a CRUD surface, a template renderer, and an authentication layer. The state space is bounded. The invariants are enumerable:

- Every migration runs exactly once, in order.
- Every database write validates against its schema.
- Every template renders without uncaught errors.
- Every authenticated request has a session.
- Every public URL maps to exactly one post or returns 404.

These are not deep mathematical truths. They are *engineering facts* about a specific, finite system. And finite systems are precisely the kind that formal verification handles well.

## A Proved Blog Engine

Imagine starting with a system that is a proved theorem.

You define the blog as a set of assertions: the database schema is sound, migrations are reversible, the template renderer is total (every input produces valid HTML), authentication cannot be bypassed, access control is enforced at the right layer.

The system is minimal. It is a proved WordPress: a database with migrations, a CRUD surface, a renderer. Not 43% of the web. Just one correct blog.

Then you extend it. A comment system. A plugin hook. A custom content type. Each extension must keep the system provable. This is the hard constraint — the interesting limitation. You cannot just add features. You must add them *while maintaining the proof*. The extension must come with its own assertions, and those assertions must compose with the existing ones without contradiction.

This is the constraint that forces architectural beauty. You cannot take shortcuts. You cannot add global state "just this once." You cannot have a SQL injection in a plugin that was written by someone who never met your database schema. Every edge case is named, bounded, and verified.

The tradeoff is obvious: this is harder. Much harder. Formal verification of a simple blog engine is a significant engineering effort. Doing it for every extension is harder still.

But the payoff is radical.

## Maximum Reliability, Prompted

If the system is a proved theorem, then prompting it changes meaning.

Today, prompting "add a product catalog with a search filter" means: the agent generates code, you review it, you hope it works, you test it, you deploy it, you discover at 3 AM that the search query is vulnerable to injection because the agent forgot to parameterize it.

In a proved system, prompting means: the agent generates a spec change, the assertion checker validates that the change preserves every invariant, and only then does it regenerate the island. If the change breaks something, the checker tells you *exactly* what breaks and where. If the change passes, the system is still proved.

This is the WordPress dream inverted: not a system that works despite being held together by duct tape and global state. A system that works *because* it was proved to work, and the prompt is just how you ask for the next extension.

The real question is not technical. The hard part is designing the set of primitives that is expressive enough to be useful — to let non-developers manipulate a real database-backed app — but bounded enough to be provable. That is the architecture problem. Everything else is an implementation detail.

Let me know when you want to expand on the primitives, the assertion system, or the practical limits of what such a system can prove.
