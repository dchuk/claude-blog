---
name: blog-sprint
description: >
  Plan a focused 30-day sprint that concentrates internal links, on-page
  completeness, and evidence upgrades on one money page stuck in positions
  5 to 20. Picks the target from first-party evidence, front-loads the
  changes in week 1, and measures instead of tweaking daily. Produces a
  sprint plan, change log format, and review dates; outreach is drafted,
  never sent. Use when user says "blitz seo", "seo sprint", "rank one page",
  "push to page one", "stuck on page 2", or "focus on one money keyword".
user-invokable: true
argument-hint: "[url-or-file] [--keyword <query>]"
license: MIT
metadata:
  version: "1.9.1"
  upstream: "https://github.com/Illyism/seo-skills/tree/3bf48be44675c5595e082f47bf162c4280ca0bbf/seo/blitz-seo"
  upstream-license: MIT
---

# Blog Sprint: Concentrate on One Money Page

Most sites spread effort across many pages that each sit past position 10.
A sprint picks one page that already ranks on page 1 or 2 for a query with
revenue behind it, and points every available signal at that page.

## Project contract first

If the repository has `docs/agents/content-workflow.md`, read it first. Its
invariants, approval rules, change log, and measurement windows govern this
sprint. In particular, if the project tracks content changes (for example
`site-analytics changes recent --url <path>`), a page edited in the last 90
days is not a sprint candidate without the user's override.

## Step 1: Pick the target

Use first-party evidence (a `site-performance` snapshot, `/blog google gsc`,
or a list from the user). A good target has all four:

1. **Position 5 to 20** for the query over the last 28 days, with real
   impressions. The page is indexed and close.
2. **Revenue intent.** A commercial roundup, comparison, or review whose
   visitors click affiliate or conversion links. Check affiliate-click or
   conversion evidence when the project has it.
3. **Beatable SERP.** At least one top-5 result is thinner, older, or less
   specific than this page could be.
4. **No cannibalization.** No other URL on the site ranks for the same query.
   Run `/blog cannibalization` if unsure.

Pick one query (three related queries at most) and one page. Present the top
two or three candidates with their evidence and wait for the user's choice.

Do not run a sprint on a brand-new domain, a query without revenue intent, or a
page that is not yet indexed.

## Step 2: Diagnose the gap

Read the current top 5 for the query (DataForSEO preferred, web search as
fallback). Apply `skills/blog/references/serp-gap-analysis.md` to find what
the winners have that this page lacks. Classify the gap as one or more of
intent match, coverage, evidence freshness, trust signals, internal links, or
snippet CTR.

## Step 3: Week 1, ship the concentrated change

Make every change in one batch so the measurement window starts clean:

- **On-page.** Answer the query in the first two sentences. Close the
  high-priority gaps. Refresh product data, prices, and sources. Route a
  snippet problem through `/blog titles`.
- **Internal links.** Add contextual links from the strongest related pages
  on the site, with descriptive anchors that vary naturally. Link from a hub
  or navigation surface if the page is a primary money page.
- **Trust.** Add real test notes, photos, measurements, or sourced data the
  competitors lack. Never fabricate any of them.
- **Technical.** Confirm the canonical, indexability, schema, and load speed.

Log the batch once in the project's change log (for example
`site-analytics changes add`). Run the project's validation and release gate.

## Step 4: Weeks 2 to 4, earn signals without editing the page

- Draft outreach to sites that link to the current top results. Name a
  specific article and a specific reason the page improves on it. Save drafts
  for the user; do not send email, submit forms, or post anywhere.
- List relevant community threads where the page answers a real question.
  The user decides whether to post.
- Request indexing once after the week-1 deploy if the user has Search
  Console access. Daily resubmission does nothing.
- Do not edit the target page again during the window unless a factual error
  appears. Each extra edit makes the result harder to attribute.

## Step 5: Measure

Review at day 28 and again at day 56 against the same windows before the
sprint. Report position, impressions, CTR, clicks, and affiliate or
conversion clicks for the target query and page. A single provider or an
unfinalized window is not enough to declare success or failure.

## Output

Return:

1. Target page and query, with the evidence that selected them.
2. The gap diagnosis.
3. The week-1 change list, specific to this page.
4. The internal link plan: source page, anchor text, target section.
5. The outreach draft list (drafts only).
6. Review dates and the metrics to read on each.

Do not promise a position or a traffic number.

## Attribution

Adapted from `blitz-seo` in Illyism/seo-skills (MIT). See NOTICE. The upstream
daily-tweak ritual was replaced with a front-loaded batch so results stay
attributable.
