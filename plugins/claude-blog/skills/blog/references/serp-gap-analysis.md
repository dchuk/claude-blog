# SERP Gap Analysis

Shared method for comparing an existing post against the pages that outrank
it. Used by `blog-rewrite` (Phase 2), `blog-sprint` (Step 2), and any project
refresh skill that cites it.

Adapted from `blog-refresher` in Illyism/seo-skills (MIT). See NOTICE.

## Rules

- Use live data. Fetch the SERP with DataForSEO or web search and read the
  competitor pages. Never describe what ranks from memory.
- Record the query, market, language, device, and retrieval date.
- The output is a delta. Close the gaps that matter; do not add length for its
  own sake.

## Step 1: Baseline the post

Record title, URL, primary query, word count, last updated date, H2 and H3
count, tables, images, internal and external links, and first-party rank and
traffic when available. Mark missing evidence as missing.

Then list strengths to keep, weaknesses, and quick wins (stale stats, broken
links, missing snippet answer).

## Step 2: Read the SERP

From the top 10, extract the titles, the featured snippet and its format,
People Also Ask questions, related searches, and the dominant page type.

Pick 5 competitors. Prefer positions 1 to 3, direct competitors, and pages
updated recently. For each, record position, word count, H2 and H3 outline,
unique elements (original data, test results, tools, visuals), and last
modified date.

## Step 3: Build the gap table

| Element | This post | C1 | C2 | C3 | C4 | C5 | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Snippet-format answer | | | | | | | |
| [Subtopic] | | | | | | | |
| Original data or tests | | | | | | | |
| Current statistics (with year) | | | | | | | |
| Comparison table | | | | | | | |
| FAQ from People Also Ask | | | | | | | |
| Schema types | | | | | | | |

Priority by coverage:

- **High:** 4 or more competitors cover it.
- **Medium:** 2 or 3 cover it.
- **Low:** 1 covers it.
- **Differentiator:** none covers it, and this site can do it credibly.

Finish with each competitor's unique angle and this post's best
differentiator.

## Step 4: Plan the delta

List exact changes: sections to keep, modify, or add; stats and sources to
refresh; snippet answer to write; links to add; schema to add only where the
page earns it. Every high-priority gap is either addressed or skipped with a
stated reason.

Present the plan and wait for approval before rewriting. Do not promise
ranking or traffic gains.

## Step 5: Preserve what works

Keep the URL, the anchors other pages link to, the sections that already earn
impressions, and the original voice. Change the visible H1 or slug only with
explicit approval.
