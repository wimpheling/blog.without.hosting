---
title: "Anthropic Engineer or Quote Fabrication? The Transcript Tells the Story"
date: 2026-06-07T00:50:00+00:00
unlisted: true
tags: ["hot takes", "investigation", "ai-conferences"]
toc: true
description: "A quote about agents lying in production went viral on X, attributed to 'Anthropic engineer James Brady.' I transcribed the 29-minute video. The quote does not appear in it."
---

I keep seeing videos on X attributed to "An Anthropic engineer" or "An OpenAI researcher" giving a 20–30 minute talk about agent reliability, prompt injection, or some other sharp operational topic. The quotes out of them are perfect. They sound like the inside view. They are also extremely shareable.

Last week, one of these showed up in my feed with this opening line:

> "Every agent in production lies. We measured it. The good ones lie less, the great ones catch the lie before the user does."

The "we measured it" half is what makes it land. Not vibes. Not a hot take. Someone inside a frontier lab is asserting that agent confidence is a measurable signal, and the metric is a liar. I quoted it myself in an earlier post.

Then I tried to verify it. The trail ended at the tweet. So I pulled the audio from the video and transcribed it.

**The quote is not in the video.** The video is a conference talk by someone at Elicit (the AI research assistant), presenting their ASHPL DSL for agentic research workflows. It has nothing to do with agents lying, and nothing to do with Anthropic.

Here is what I found by pulling every thread.

## 1. @0x_rody is not an Anthropic employee

The poster's profile metadata:

- **Handle:** `@0x_rody`
- **Name:** rody
- **Bio:** "AI tools analyst | Code & consciousness | @zscdao"
- **Location:** San Diego, CA
- **Account age:** joined April 2021
- **Posts:** 158 over 5 years — roughly 2–3 tweets per month
- **Followers:** 1,283
- **Verified:** false (X Premium)

No Anthropic affiliation anywhere. "AI tools analyst" is a self-description; nothing on the profile suggests employment at any lab. The account also has a structural anomaly: 1,283 followers, but the Brady tweet pulled ~1,240 likes — a 1,000% engagement spike on a single post from a small account.

## 2. @0x_rody is part of a Polymarket DAO

The bio cross-links to `@zscdao`, a separate X account:

- **Name:** zerosupercycle
- **Bio:** "ZSC DAO is an organization building tools & community resources to bring Polymarket into the everyday lexicon."

Polymarket is a crypto prediction market. ZSC DAO builds tooling around it. So the source of the "Anthropic engineer" quote is not in the AI-lab orbit — it is in the **crypto prediction-market DAO** orbit, with an AI-tools side interest.

The non-obvious part: prediction-market DAOs have a strong incentive to publish content that the AI Twitter audience finds credible, because they sell picks, signals, and tools to that audience. An "Anthropic engineer says X" pull-quote travels far in that demographic. I am not accusing anyone of anything — I am naming a structural fit: the people who benefit most from a sharp AI quote going viral are the people whose day job is monetizing AI Twitter's attention.

## 3. The 29-minute video is a quote-tweet of rody's *own* article

This is the part I did not expect.

The first link inside the tweet resolves to a **Quote Tweet** of rody's own X article, posted **1 hour 32 minutes earlier** on the same day, titled:

> "How to Make Claude Code Stop Making Stuff Up When It Doesn't Know (Exact Setup Inside)"

The article opens:

> "Claude Code lies to your face every day. Made-up functions, fake imports, 'tests pass' when nothing ran. The fix is a 4-layer setup that makes lying expensive."

These two pieces of content are the *same thesis* in two formats. The article is rody's own Claude Code tutorial with a "4-layer honesty setup." The tweet-with-video is the *same message* — but the pull-quote is attributed to "Anthropic engineer James Brady."

The trail from the quote back to the source ends inside the same account that posted the tweet.

## 4. There is no James Brady at Anthropic

- **Anthropic `/engineering` blog** — every post has an author byline. None is "James Brady."
- **Anthropic `/events` page** — no "James Brady" in any speaker list.
- **Web search** — Brave, DuckDuckGo, Bing, and Google all return only the Wikipedia article for **James Brady the White House Press Secretary** (shot in the 1981 Reagan assassination attempt; died 2014). *The most indexed James Brady in the world is a man who died 12 years before the tweet was posted.* A search for "James Brady" + "Anthropic" + "agent" returns zero.

The simplest explanation: there is no James Brady at Anthropic. The name is either fictional, a pseudonym, or borrowed from somewhere else.

## 5. The transcript: the 29-minute video is not about "agents lying"

This is the finding that closes the case. I pulled the audio from the video and transcribed it through Deepgram's Nova-2 model. The transcript is 5,095 words.

**The video is a talk by someone from Elicit — the AI research assistant — about ASHPL, their domain-specific language for agentic workflows.** It is not an Anthropic talk. It is not about a "verification stack." It is not by "James Brady."

The speaker walks through:

- Why Elicit chose a DSL over freeform agent architectures;
- The ASHPL language design: a Turing-incomplete, pure functional subset of Python with domain primitives for retrieving academic papers and clinical trials;
- The event-sourcing pattern that drives iterative plan-and-execute loops;
- A live demo generating a research landscape table about foundation models for biology — searching academic papers, web sources, filtering, extracting, and joining results across multiple passes;
- How memoization and content-addressable storage make full-program reinterpretation efficient.

The word "lie" does not appear anywhere in the transcript. Neither does "lying," "fabrication," "caught," or "verification stack." The closest the speaker gets is a general remark about trust: the mechanism of how an output is produced matters, not just the output itself. That is a point about process legibility, not a claim about measuring agent dishonesty in production.

The talk is clearly from a conference or meetup. The speaker says "Elicit" repeatedly. The slide deck references elicit.com. The vocabulary — "research landscape," "clinical trials," "academic papers," "systematic review" — is the vocabulary of scientific research tooling, not agent-safety engineering.

## The verdict

The evidence converges:

- **The video is real.** It is a legitimate conference talk about Elicit's DSL architecture.
- **The quote is not in the video.** The 24-word opening line attributed to "James Brady" was not said by the speaker.
- **The name "James Brady" is not verifiable at Anthropic.** He does not appear in any public record that is not a 20th-century press secretary.
- **The tweet's headline quote describes rody's own article, not the video.** The quote-tweet is from rody's own article. The headline and the video content are mismatched.
- **The poster sits in a Polymarket DAO ecosystem** that has structural incentives to produce viral AI content.

This is not an accident or a misunderstanding. A real talk was taken, paired with a quote that does not appear in it, and attributed to a person who cannot be found. The quote itself — "Every agent in production lies. We measured it" — is a sharp and memorable claim, which is probably why it was written in the first place. But it was written by the poster, not spoken by an Anthropic engineer.

## What to do when you see one of these

Before you share a sharp AI quote from X, check three things:

1. **Can you find the original source outside the tweet?** YouTube, a conference page, a blog post, a LinkedIn announcement. If the trail ends at the tweet, that is a red flag.
2. **Does the poster have a verifiable affiliation with the lab they are quoting?** Check their bio, their history, their other posts. An "AI tools analyst" whose bio mentions a Polymarket DAO is not an Anthropic engineer.
3. **Does the quote actually match the content?** The quote in the tweet I investigated describes a "verification stack" for agents that "catch the lie before the user does." The actual video is about a DSL for academic research. These are not the same thing.

I almost shared the quote myself. The discipline costs nothing and prevents propagating something that was never said.

---

*First published: 2026-06-07. Updated with transcript evidence: 2026-06-08.*