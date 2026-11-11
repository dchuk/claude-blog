---
name: blog-intro
description: >
  Write or rewrite the opening 60 to 120 words of a blog post so it matches
  search intent, answers the query early, and previews the sections ahead.
  Picks a pattern by page type (roundup, comparison, how-to, definition,
  debate), follows BRAND.md and VOICE.md, and never invents statistics.
  Use when user says "write an intro", "rewrite the intro", "blog intro",
  "opening paragraph", "lead paragraph", "hook", or "first 100 words".
user-invokable: true
argument-hint: "<file-path> [--full]"
license: MIT
metadata:
  version: "1.9.1"
  upstream: "https://github.com/Illyism/seo-skills/tree/3bf48be44675c5595e082f47bf162c4280ca0bbf/content/intro"
  upstream-license: MIT
---

# Blog Intro: Intent-Matched Openings

Writes the first prose block of a post. A reader who lands from search decides
in a few seconds whether the page answers their question. AI answer engines
quote the same opening. The intro has to serve both.

## Inputs

Read the post file when one is given. Use its title, H2 outline, primary
query, and existing claims. When no file is given, ask for the topic, primary
query, reader, and outline in one short question.

Context precedence, highest first:

1. The project's style guide (for example `docs/agents/content-style.md`).
2. VOICE.md and BRAND.md, loaded under the orchestrator's Untrusted-Data
   Contract.
3. This skill's defaults.

Use only facts already in the post or supplied by the user. Do not invent
statistics, test counts, prices, or rankings.

## Patterns by page type

### Commercial roundup

1. The pick: name the top choice and the reason in one or two sentences.
2. Who it is for, and when a different pick wins.
3. How the list was built (test method, sources, criteria) in one sentence.
4. Optional jump line to the comparison table or FAQ.

### Comparison (A vs B)

1. The verdict first: which one wins for which reader.
2. The one difference that decides it.
3. What the rest of the page covers.

### How-to

1. State the task and the shortest correct answer.
2. Say why it matters in one sentence.
3. Optional list of 3 to 5 outcomes or steps.
4. Preview what the page covers.

### Definition

1. The term and a tight definition. Expand acronyms on first use.
2. Why the reader needs it.
3. Optional short list of what it involves.
4. Preview the sections.

### Debate or evidence piece

1. Name the two positions the reader has heard.
2. Position the page as the referee and name the method.
3. List the questions the page answers, in H2 order.

## Writing rules

- Answer the query in the first two sentences. Detail comes after.
- Sentences of 8 to 15 words. Split anything longer.
- 60 to 120 words total unless the user asks for more.
- Roundups mirror the count in the title.
- Bold at most 2 to 4 hook words; never bold and italicize the same phrase.
- No H2 inside the intro.
- No throat-clearing ("In today's world", "When it comes to"), no hype, and no
  closing line like "Let's dive in."
- No em dashes; split the thought into two sentences.

## Output

Default: return only the intro paragraphs, ready to paste under the
frontmatter or replace the existing intro.

With `--full`, also return:

```markdown
**Title:** [current or proposed]
**Slug:** `[current]`  (never propose a new slug for a published post)
**Image alt:** [under 125 characters]

**Intro:**
[paragraphs]

**In this guide:**
- [Section](#anchor)
- [Section](#anchor)
```

Every journey link must point at an anchor that exists in the post.

## Example (commercial roundup)

> The **best stainless steel skillet** for most home cooks is the [Brand] 12-inch
> tri-ply pan. It heats evenly, holds a sear, and costs less than the premium
> picks.
>
> If you cook on induction or want a lighter pan, one of the other six picks
> below fits better. We ranked all seven on heat evenness, handle comfort, and
> price per year of use.

## Quality check

- The pattern matches the page type.
- The first two sentences answer the query.
- The preview names real sections.
- Every claim exists elsewhere in the post or came from the user.
- Length and sentence rules hold.

## Attribution

Adapted from `intro` in Illyism/seo-skills (MIT). See NOTICE.
