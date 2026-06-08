---
title: "Anthropic Engineer or Quote Fabrication? An Open Investigation"
date: 2026-06-07T00:50:00+00:00
unlisted: false
tags: ["hot takes", "investigation", "ai-conferences"]
toc: true
description: "A 29-minute video on X claims to be a real Anthropic engineer giving a candid talk. The quote is good. The transcript says otherwise. This is an open investigation into who posted it and why."
---

> **Status: live, ongoing.** The account is a systematic content farm posting 2–3 fabricated quotes daily. The DAO behind it is a ~5-month-old shell with unverifiable leadership and a false "Official Polymarket Community" claim. Last updated: 2026-06-08.

I keep seeing videos on X attributed to "An Anthropic engineer" or "An OpenAI researcher" giving a 20–30 minute talk about agent reliability, prompt injection, or some other sharp operational topic. The quotes that come out of them are perfect. They sound like the inside view. They are also extremely shareable.

Last week, one of these videos showed up in my feed again. It had 29 minutes of content. The opening line was the one I quoted in [Stop Reading What Your Coding Agent Says](https://blog.without.hosting/posts/backspine-dont-read-agent-text/):

> "Every agent in production lies. We measured it. The good ones lie less, the great ones catch the lie before the user does."

The quote is good. *Really* good. The "we measured it" half is what makes it land. It is exactly the kind of line a senior engineer at a frontier lab would say if they had actually seen the failure data.

I tried to verify it. I couldn't. This post is the open investigation.

Here is what I have found so far, in brief:

- **The quote is not in the video.** I transcribed the full 29 minutes via Deepgram. It is an Elicit talk about a DSL for research workflows. The word "lie" does not appear once.
- **"James Brady" is not a person I can verify at Anthropic.** The only James Brady in the world's search indexes is a White House press secretary who died in 2014.
- **The poster, @0x_rody, runs a daily content farm.** 2–3 posts every day, each following the exact same template: a provocative quote attributed to an AI figure, paired with a real video from a different context, ending with "save the config below."
- **The DAO in rody's bio (ZSC DAO / zerosupercycle) is a ~5-month-old operation** with a false "Official Polymarket Community" designation, unverifiable leadership, no product, and no media footprint.
- **This is a systematic funnel, not a one-off.** The fabricated quotes drive engagement that routes toward Claude Code configs and, ultimately, Polymarket awareness.

The sections below walk through the receipts for each claim.

## The case

The video is [posted on X by @0x_rody](https://x.com/0x_rody/status/2063318596202242171). It is attributed in the tweet text to "Anthropic engineer James Brady." The 29 minutes is a single Twitter-native upload. The two links in the tweet's body both resolve back to the same status — there is no separate YouTube upload, no Anthropic engineering blog post, no conference page, no LinkedIn announcement, no GitHub repo, no LinkedIn profile for a James Brady at Anthropic that surfaces in search. Just the tweet, the video, and the quote.

**The trail ends at the tweet.** That should be a yellow flag for any reader, and a red flag for any writer who would put it in their own post without flagging the source. I almost did exactly that.

## What I found so far

### 1. @0x_rody is not an Anthropic employee

Pulling the X profile metadata for the poster:

- **Handle:** `@0x_rody`
- **Name:** rody
- **Bio:** "AI tools analyst | Code & consciousness | @zscdao"
- **Location:** San Diego, CA
- **Account age:** joined April 2021 (5 years old)
- **Posts:** 158 over 5 years — roughly 2–3 tweets per month
- **Followers:** 1,283 — small account
- **Following:** 51
- **Verified:** false (X Premium)

There is no Anthropic affiliation in the bio. The account is not institutional. "AI tools analyst" is a self-description; nothing on the profile suggests employment at any lab. "Code & consciousness" is a tagline that points at a philosophical / personal-brand register, not a corporate one.

The 1,283-follower / 1,240-likes-per-tweet ratio on the Brady post is a separate anomaly: this small account pulled a 1,000% engagement spike on a single tweet. That is a structural signal worth holding onto.

### 2. @0x_rody is part of a Polymarket DAO — but it is not what it claims

The bio cross-links to `@zscdao`, a separate X account:

- **Handle:** `@zscdao`
- **Name:** zerosupercycle
- **Bio:** "ZSC DAO is an organization building tools & community resources to bring Polymarket into the everyday lexicon."
- **Location:** Polymarket
- **Followers:** 10,618 — but less than 200 following. A broadcast account.
- **Website:** zscdao.com

ZSC DAO's website (zscdao.com) is a Next.js app on Vercel with a retro terminal aesthetic — CRT scanlines, boot animation. The tagline is **"Official Polymarket Community."**

This claim appears to be false. Polymarket's official Discord is `discord.gg/polymarket`, not `discord.gg/zscdao`. Polymarket does not list ZSC DAO anywhere on their site, in their docs, or on their social channels. The "Official" designation is self-applied.

The site has four pages:

- **HOME** — the boot screen and "Official Polymarket Community" claim
- **DATA** — a mission statement: "We find and unite people who want to achieve success in Prediction Markets. Our goal is to transform diverse opinions and experiences into wealth for every participant."
- **COMM** — a "Hall of Fame" listing the team
- **MAP** — ecosystem links (X, Telegram)

The team page lists three people:

- **Atlantislq** (@Atlantislq) — "Founder" — zero web presence outside this site
- **David Mozhaev** (@DavidMozhaev) — "CEO" — GitHub account created on **January 6, 2026**, blank profile, no repos, no commits
- **banana0x** (@banan_crypto) — "Ops Lead" — zero web presence

There is no whitepaper, no token, no revenue model, no legal entity. A search for "ZSC token" on CoinGecko, on chain registries, and across the web returns nothing. A search for "ZSC DAO" in news, Reddit, blogs, and Google returns nothing — zero media coverage, zero community discussion outside the DAO's own channels.

The **Discord** server ("zerosupercycle DAO") has ~3,985 members with ~757 online — suspicious ratios that could indicate botted engagement. I have not verified this directly.

The domain (zscdao.com) was registered through NameCheap with privacy shield routed through Iceland. The first Wayback Machine snapshot is **January 1, 2026** — the entire operation is roughly 5 months old. David Mozhaev's blank GitHub was created the same week. This timing cluster is not a coincidence.

So the source of the "Anthropic engineer" quote is not just adjacent to a Polymarket community — it is linked to a **~5-month-old operation with a false "official" designation, unverifiable leadership, no product, no token, and no media footprint**. The "ZSC DAO" label in rody's bio provides an institutional veneer that does not survive scrutiny.

### 3. The video is a quote-tweet of rody's *own* article

The first link inside the Brady tweet redirects to a **Quote Tweet** of rody's own X article. The full text:

> "Anthropic engineer James Brady:
> 'Every agent in production lies. We measured it. The good ones lie less, the great ones catch the lie before the user does.'
> In 29 minutes, he walks through the verification stack he built and the patterns the Claude Code team adopted to keep agents honest at scale. Watch the full talk, then save the config below!"

The post being quoted is rody's own article, posted **1 hour 32 minutes earlier** on the same day (2026-06-06), titled:

> "How to Make Claude Code Stop Making Stuff Up When It Doesn't Know (Exact Setup Inside)"

The article opens:

> "Claude Code lies to your face every day. Made-up functions, fake imports, 'tests pass' when nothing ran. The fix is a 4-layer setup that makes lying expensive."

These two pieces of content are the *same thesis*, in two formats. The article is rody's own Claude Code tutorial with a "4-layer honesty setup" (CLAUDE.md rules + verification layers). The tweet-with-video is the *same content* — but the pull-quote is attributed to "Anthropic engineer James Brady."

I do not have a final interpretation of what this means. I have three live hypotheses:

1. **The "James Brady" in the video is rody**, using a pseudonym or persona, dramatizing his own take. The 29 minutes is the same content as the article, just spoken.
2. **The "James Brady" is a real Anthropic engineer** whose real internal talk rody is reposting — but if so, that talk does not exist on Anthropic's `/engineering` blog, on their `/events` page, on YouTube, or on any conference site I can find.
3. **The "James Brady" is fictional**, a stock persona used to dramatize a position. The video is AI-generated and the attribution is a fiction that the algorithm rewards.

### 4. There is no James Brady at Anthropic

- **Anthropic `/engineering` blog** — every post has an author byline. None is "James Brady."
- **Anthropic `/events` page** — no "James Brady" in any speaker list.
- **Web search** — Brave, DuckDuckGo, Bing, and Google all return only the Wikipedia article for **James Brady the White House Press Secretary** (shot in the 1981 Reagan assassination attempt; died 2014). *The most indexed James Brady in the world is a man who died 12 years before the tweet was posted.* A search for "James Brady" + "Anthropic" + "agent" returns zero.

The simplest explanation: there is no James Brady at Anthropic. The name is either fictional, a pseudonym, or borrowed from elsewhere.

### 5. Anthropic does publish on agent reliability — in a different register

While looking for Brady, I found the *real* Anthropic engineering content on the same theme. None of it sounds like the Brady quote, but it is the genuine artifact:

- **"How we contain Claude across products"** — the closest match to "verification stack." Talks about caps, blast radius, containment, not "agents lying."
- **"An update on recent Claude Code quality reports"** (April 2026) — Anthropic's own honest accounting of failure modes.
- **"Scaling Managed Agents: Decoupling the brain from the hands"** (April 2026) — real engineering post on agent architecture.
- **"Harness design for long-running application development"** (March 2026) — agent design from the inside.
- **"Trustworthy agents in practice"** (April 2026) — Anthropic's own post on agent reliability. It does not use the word "lies." It uses "misread users' intent," "act with unintended consequences," and "prompt injection."

The contrast matters. The Brady quote is **sharper and more quotable** than anything in Anthropic's own engineering blog. That is not evidence of fraud — it is evidence of stylization. Real engineering writing is hedged. The Brady quote is not hedged. That puts it in a different genre from Anthropic's own writing on the topic.

### 6. The transcript: the 29-minute video is not about "agents lying"

This is the finding that shifted the investigation. I pulled the audio from the video and transcribed it through Deepgram's Nova-2 model. The transcript is 5,095 words.

**The video is a talk by someone from Elicit — the AI research assistant — about ASHPL, their domain-specific language for agentic workflows.** It is not an Anthropic talk. It is not about a "verification stack." It is not by "James Brady."

The speaker walks through:

- Why Elicit chose a DSL over freeform agent architectures;
- The ASHPL language design: a Turing-incomplete, pure functional subset of Python with domain primitives for retrieving academic papers and clinical trials;
- The event-sourcing pattern that drives iterative plan-and-execute loops;
- A live demo generating a research landscape table about foundation models for biology;
- How memoization and content-addressable storage make full-program reinterpretation efficient.

The word "lie" does not appear anywhere in the transcript. Neither does "lying," "fabrication," "caught," or "verification stack." The closest the speaker gets is a remark about trust: the mechanism of how an output is produced matters, not just the output itself. That is a general point about process legibility, not a claim about measuring agent dishonesty in production.

The talk is clearly from a conference or meetup. The speaker says "Elicit" repeatedly. The slide deck references elicit.com. The vocabulary — "research landscape," "clinical trials," "academic papers," "systematic review" — is the vocabulary of scientific research tooling, not agent-safety engineering.

**This closes one lead: we now know what is in the 29-minute video.** It is a real talk by a real person at Elicit. The quote has been superimposed onto it. The attribution to "Anthropic engineer James Brady" is text that wraps around a completely different piece of content.

But this raises the next question: **where did the video come from?** Is it a repurposed conference talk? Was it downloaded, cropped, and paired with the fabricated quote by rody, or did rody get it from somewhere else? The Elicit employee whose talk this is might not even know their video is being used this way.

### 7. The James Brady post is not a one-off — rody runs a daily content farm

The transcript answered "what is in the video." The next question was: is this a single bad tweet or a pattern?

I pulled rody's recent posting history. The answer is definitive.

**rody posts 2–3 times per day, every day. Every single post follows the exact same template:**

> *"[AI Figure]: '[provocative, slightly technical quote]' — In 29 minutes, he walks through [topic]. Watch the full talk, then save the config below 👇"*

Recent examples from a single two-week span:

| Date | Attributed To | Quote |
|------|--------------|-------|
| June 8 | "Anthropic's Chief Product Officer" | "Claude doesn't write code anymore" |
| June 7 | "Anthropic's main manager" | "Nobody types prompts from scratch" |
| June 6 | "Anthropic engineer James Brady" | **Our case.** |
| May 30 | Boris Cherny, head of Claude Code | "The default is now I'm going to have Claude prompt itself" |
| May 29 | Anthropic engineer Arnaud Doko | "Saying 'make it better' is the most expensive mistake" |
| May 26 | Dario Amodei, CEO of Anthropic | quoted from an Oprah interview |
| May 16 | Andrej Karpathy | "never felt more behind as a programmer" |
| May 13 | Boris Cherny | "It's not so much about deep work" |

(Note: I am deliberately not linking to these posts. The pattern is the evidence, not any individual post.)

Every post includes an amplify video and a link to another of rody's own articles. Every one is structured to drive engagement toward Claude Code configs, AI tooling setups, and ultimately — through the bio link — **ZSC DAO / Polymarket**.

The account joined X in **April 2021** and was largely inactive for years (158 total posts over 5 years). The pivot to daily content farming appears to have started recently — tightly clustered with the January 2026 launch of zscdao.com and David Mozhaev's GitHub account.

**This changes the investigation.** The "James Brady" quote is not a one-off viral spike. It is a single output in a systematic content production pipeline. The quote, the attribution, and the video mismatch are *features of the pipeline*, not bugs. The pipeline runs daily, targeting the AI Twitter audience, with a consistent call-to-action funnel toward the DAO ecosystem.

The question is no longer "who is James Brady?" The question is **"what is this funnel monetizing?"** — and the Polymarket DAO connection is the strongest lead.

## The genre

[USER: write — your read on the "long insider video + sharp pull-quote" pattern. Why does the form keep working? You have been seeing this for a year, you said. I want your voice on what is in the water, not mine.]

## Open leads

These are the next threads. I am putting them here so I (or anyone else) can pick them up.

1. **More cases.** I have seen several of these. I need the receipts: handles, dates, quotes, screenshots. The case above is one clean example; the genre is the question, not the one.
2. ~~**What is in the 29-minute video?**~~ **Resolved.** The transcript is in. It is an Elicit talk about their ASHPL DSL. The quote does not appear in it.
3. ~~**Rody's other posts.**~~ **Resolved.** 158 posts over 5 years, but the recent pattern is 2–3 posts daily following the exact same template. The account pivoted to content farming around January 2026. See section 7 above.
4. ~~**zscdao / Polymarket.**~~ **Partially resolved.** ZSC DAO is a ~5-month-old operation with a false "Official Polymarket Community" designation, unverifiable leadership, no product, and no media footprint. The connection between rody and ZSC DAO is confirmed. What remains open: is this a deliberate funnel on rody's part, or is rody genuinely part of a larger content operation orchestrated by ZSC DAO?
5. **Where did the video come from?** The Elicit talk — was it from a public conference? A meetup? Was it downloaded from YouTube or a conference site and repurposed? Finding the original upload would confirm the mismatch and potentially identify the actual speaker.
6. **Other Polymarket-DAO-adjacent accounts.** Are prediction-market communities *systematically* seeding content into AI Twitter? If so, that is its own piece.
7. **The CEO "David Mozhaev."** A blank GitHub created January 6, 2026 and an X handle is all that exists. Is this a real person or a fabricated identity? A deep search into the name, the X account history, and any cross-platform presence could reveal more.
8. **Rody's own identity.** Who is "rody"? No GitHub, no Reddit, no LinkedIn presence found. The account has been on X since 2021 but was largely inactive. What changed around January 2026?

## What I am not claiming

I am not claiming the quote is wrong. The quote is probably *true as a description of agent behavior* — the part I quoted in [Stop Reading What Your Coding Agent Says](https://blog.without.hosting/posts/backspine-dont-read-agent-text/) holds up regardless of who said it, because the structural dynamic it describes is real.

What I am claiming, with evidence:

1. **The trail of attribution ends at rody's own article.** The tweet is a quote-tweet of rody's article. The "Anthropic engineer" voice and the "rody" voice are the same thesis in two formats.
2. **"James Brady" is not a person I can verify at Anthropic.** The only indexed James Brady in the world is a 20th-century press secretary.
3. **The quote does not exist in the video.** The transcript is in. It is an Elicit talk about DSL design. The two things share no content.
4. **The quote is not a one-off.** rody posts 2–3 fabricated quotes daily. The James Brady post is one output in a systematic pipeline.
5. **ZSC DAO is not what it claims.** It is a ~5-month-old operation with a false "Official Polymarket Community" designation, unverifiable leadership, and no product.
6. **The genre — "long insider video + sharp pull-quote attributed to a vague insider" — is a content pattern, not a series of one-offs.** The shape of the content is too consistent to be coincidence.

## What to do if you see one of these

[USER: write — your move when you see a sharp, attributed AI quote on X. Do you screenshot it, bookmark it, share it, verify it? What is the right discipline? You were almost the next person to spread this one.]

---

*Last updated: 2026-06-08. Investigation continues. Filing date for next update: when the Elicit talk's original source is found, when additional cases are documented, and when ZSC DAO's leadership and rody's identity are further investigated.*