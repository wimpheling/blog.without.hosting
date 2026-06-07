# Anti-Slop Style Rules

Rules extracted from editing a draft from generic LLM prose into something that sounds like a person wrote it.

## 1. Start with a specific constraint, not a generic desire

Bad: "I wanted my blog to do X."
Good: "The LLM finishes the post before the dev work finishes. You publish early, the article keeps changing."

The generic version sounds like a tutorial. The specific version sounds like someone who actually has the problem.

## 2. No numbered options

"The tempting bad version → Option 3 → Why this works" is the patented LLM blog pipeline. It signals *walkthrough* before the reader cares. State the problem and the solution without numbering them.

## 3. A mechanism is not a point

If an implementation detail does not change what the reader sees or experiences, cut it. The author-distinction section was technically true and completely unnecessary. The page already demonstrates it — the post does not need to explain itself.

## 4. No performative opinions

"Hugo does not read git notes. It should not have to" is fake attitude about a workflow choice. The honest version is "We need to plug git notes into the Hugo build."

Test: if you remove the line and the argument survives, the line is decoration.

## 5. No curtain lines

"The ghostwriter should be visible but not magical. Git notes keep the magic out of the article." — writer trying to sound like the paragraph ended intentionally. Adds nothing. End when the argument is complete, not when you found a catchy sentence.