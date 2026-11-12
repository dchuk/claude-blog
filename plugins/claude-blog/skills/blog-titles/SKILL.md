---
name: blog-titles
description: >
  Rewrite SEO titles and meta descriptions to win more clicks for pages that
  already earn impressions. Picks pages from Search Console CTR and position
  evidence, reads the live SERP titles for each target query, drafts 3 to 5
  options per page, and returns a before/after table for approval before
  editing any file. Protects the visible H1, slug, and canonical by default.
  Use when user says "rewrite titles", "improve CTR", "title optimization",
  "SERP titles", "low click-through rate", "title tags across the site", or
  "bulk title rewrite". For a pass/fail check of one finished post, use
  blog-seo-check instead.
user-invokable: true
argument-hint: "[file-or-directory] [--from-gsc]"
license: MIT
metadata:
  version: "1.9.1"
  upstream: "https://github.com/Illyism/seo-skills/tree/3bf48be44675c5595e082f47bf162c4280ca0bbf/seo/seo-title-optimization"
  upstream-license: MIT
---

# Blog Titles: CTR-Driven Title Rewrites

Rewrites titles and meta descriptions for pages that rank but do not earn the
click. The live SERP is the brief. Never write a title from intuition alone.

## Project contract first

If the repository has `docs/agents/content-workflow.md`, read it before
anything else. Its rules govern which fields may change, which approvals are
required, and how changes are logged. Where it conflicts with this skill, the
project workflow wins.

Default invariants when no project contract exists:

- The slug and canonical URL never change.
- The visible H1 stays stable. Change it only when the user approves a
  specific H1 change.
- If the content schema has a separate SEO title field (for example
  `seoTitle` or `metaTitle`), change that field and leave the H1 alone.

If the project tracks content changes (for example
`site-analytics changes recent --url <path>`), run that check per page. Skip
any page edited in the last 90 days unless the user overrides it, because a
second change inside the measurement window destroys attribution.

## Step 1: Pick pages from evidence

Pull page and query rows from the best first-party source available, in this
order:

1. A project performance snapshot (for example the `site-performance` skill
   output) for the last 28 and 90 days.
2. `/blog google gsc` when Search Console credentials are configured.
3. A list the user supplies.

If none exists, say so and ask for a page list. Do not guess which pages
underperform.

Classify each candidate:

| Evidence | Diagnosis | Action |
| --- | --- | --- |
| Position 1-10, CTR clearly below the site's own CTR at that position | Snippet problem | Rewrite title and description |
| Position 8-20 with real impressions | Ranking depth problem | Route to `/blog rewrite` or the project refresh track, not here |
| Impressions spread across queries the title never names | Query mismatch | Rewrite title around the query that earns the most impressions |
| No impressions | Indexing or intent problem | Out of scope; report it |

Compare CTR against the site's own position curve when enough rows exist.
Generic industry CTR curves are a weak fallback; label them as such.

## Step 2: Read the SERP for each target query

Fetch the current top 10 for the primary query. Prefer DataForSEO
(`claude-seo:seo-dataforseo`) when it is configured; fall back to web search.
Record the market, language, device, and retrieval date.

From the SERP, note:

- repeated structures (numbers, year, "best", "vs", "how to");
- the dominant page type (listicle, guide, comparison, product page);
- typical title length and where Google rewrote titles;
- what no ranking title promises that this page can deliver.

## Step 3: Draft options

Draft 3 to 5 options per page, then pick one. Rules:

- Put the primary query near the front.
- Match the page type the SERP rewards. Pick one pattern from the table
  below; do not mix patterns unless the SERP does.
- Keep the important words inside roughly 580 pixels (about 50 to 60
  characters). Front-load so truncation cuts only the brand.
- Say something only this page can claim: a test count, a named method, a
  year of real data, a specific audience.
- Every title on the site is unique.
- Use a year only if the page is genuinely updated for that year. Do not put a
  year in the slug.
- No hype words the SERP does not use ("Ultimate", "Shocking", "Guaranteed").
- Never claim testing, rankings, or numbers the page does not support.

| Intent | Pattern |
| --- | --- |
| Commercial roundup | `[N] Best [Product] for [Audience or Use] ([Year])` |
| Comparison | `[A] vs [B]: [Which Wins for Decision]` |
| Single review | `[Product] Review: [Verdict in a Few Words]` |
| How-to | `How to [Task] ([Qualifier])` |
| Definition | `What Is [Term]? [Short Payoff]` |
| Troubleshooting | `[Problem]: Causes and Fixes` |
| Checklist | `[Topic] Checklist: [N] Steps to [Outcome]` |

Rewrite the meta description in the same pass: 140 to 160 characters, answer
the query in the first clause, and name the concrete payoff.

## Step 4: Approval checkpoint

Return one table and stop. Do not edit files until the user approves.

```markdown
| Page | Query (impr / CTR / pos) | Current title | Proposed title | Why |
| --- | --- | --- | --- | --- |
| `/best-skillets/` | best stainless skillet (4.1k / 0.9% / 6.2) | Stainless Skillets | 7 Best Stainless Steel Skillets (2026 Tested) | Names query; matches listicle SERP |
```

Keep each "Why" to one line.

## Step 5: Apply and log

For approved rows only:

1. Edit the title field (and description) in the source file.
2. Leave the H1, slug, and canonical unchanged unless that row was approved
   for an H1 change.
3. If the project logs changes (for example `site-analytics changes add`),
   log each edited page with the reason "title CTR".
4. Rerun `/blog seo-check` on each edited file.
5. Report the next review date: two finalized 28-day windows after deploy.
   Do not judge a title change on less data.

## Anti-patterns

- Rewriting a title for a page whose problem is ranking depth.
- Changing many fields on one page at once, so the CTR change cannot be
  attributed.
- Copying a competitor's title structure word for word.
- Treating a missing CTR value as zero.

## Attribution

Adapted from `seo-title-optimization` in Illyism/seo-skills (MIT). See NOTICE.
