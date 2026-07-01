---
name: blog-writer-workflow
description: "Operate the user's Hugo blog writer/editor profile: ramble-to-draft, repo edits, commit/push, and publish gate."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [blog, hugo, writing, telegram, git]
---

# Blog Writer Workflow

Use this skill whenever the user asks to capture blog ideas, draft/edit Hugo posts, commit/push blog changes, publish/unlist an article, or send writing nudges.

## Bilingual / Multilingual Posts

The Hugo site has multilingual support via `config.toml` `[languages]` (en + fr). When producing a parallel post in another language:

1. **Place FR post in `content/fr/posts/`** — NOT in `content/posts/`. The English default goes in `content/posts/`.
2. **Add `_index.md`** in both `content/fr/` and `content/fr/posts/` — Hugo needs these branch bundle files to render section pages (e.g. `/fr/posts/`). Without them you get a 404.
3. **Add `translationKey`** to both frontmatters when filenames differ between languages. Same key value on both posts. This links them as translations.
4. **PaperMod's `translation_list.html`** can be overridden at `layouts/partials/translation_list.html`. The site uses a custom banner with flag emoji + clickable title, styled like the Edits section (CSS in `extend_head.html`).
5. **Banner logic**: check the translation's language (`.Lang` inside `range .Translations`), NOT the current page's language — more robust across Hugo language-detection edge cases.
6. **Publishing**: an already-published EN post with an FR version needs the `unlisted: true` removal on both independently.

For detail and the exact template: see `references/bilingual-hugo-setup.md`.

## Article Style Guidelines

Adapted from the user's French web-writing guidelines, but filtered for a personal technical blog rather than corporate SEO copy.

Use these as defaults when drafting or editing posts:

- **Title**: short, explicit, autonomous, and front-loaded with the meaningful words. Prefer 4–10 words when possible. Avoid vague cleverness, clickbait, exclamation marks, and decorative wordplay. A title can be catchy, but clarity wins.
- **Description/front matter**: write a concise description that works as the post's search/result preview. It should explain the value of the post and invite reading, not just repeat the title.
- **Opening**: get to the point quickly. The first paragraph should contain the core situation, tension, or claim. Avoid throat-clearing and generic context.
- **Inverted pyramid, lightly applied**: start with the essential idea, then add nuance, background, examples, and caveats. Do not bury the actual claim halfway down the post.
- **One idea per paragraph**: keep paragraphs focused. The first sentence should usually signal the paragraph's point.
- **Readable structure**: use headings, bullets, and short sections when they help scanning. Do not over-structure into bureaucratic outlines.
- **Sentences**: prefer active voice, concrete vocabulary, and short-to-medium sentences. Break long chains of subclauses. Avoid unnecessary parentheses, semicolons, and ornamental transitions.
- **Jargon**: technical terms are fine when useful, but explain non-obvious acronyms or domain-specific shorthand early.
- **SEO without keyword stuffing**: include natural terms a reader might search for, especially in title/description/opening, but never distort the voice for SEO.
- **Links**: use explicit link text that says where the link goes. Avoid "click here". Prefer a few relevant links over link dumping.
- **Dates/time**: use absolute time references when durability matters (e.g. "in June 2026" rather than "now" or "last month").
- **Images**: if images are used, prefer informative images and give them meaningful alt text. Decorative images should not pretend to carry SEO meaning.
- **Voice override**: these rules must not erase the user's voice. Preserve rough edges, opinions, and exploratory tone. Do not turn posts into polished institutional web copy.

### Editorial Pitfalls

- **"I see what nobody else sees" framing** — avoid this. The user called this out as presumptuous. When expressing frustration about a gap between perceived reality and market narrative, frame it as a gap between *hype and actual simplicity*, not as the user seeing something invisible to others. Acknowledge that plenty of people already see the same thing — the frustration is that *the public conversation* stays stuck on the wrong story.
- Do NOT inflate minor operational details into grand claims. If a section like "the interesting constraint" overstates something already covered, cut it rather than making it sound profound.
- Do NOT use numbered arcs, causality claims, triplet negatives (no X no Y just Z), curtain lines, meta-commentary, or bot self-justification.