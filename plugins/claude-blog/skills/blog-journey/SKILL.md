---
name: blog-journey
description: >
  Map how a site's readers discover, compare, and choose across Google, AI
  assistants (ChatGPT, Claude, Perplexity, Google AI Overviews), and
  communities, using five awareness stages. For each stage it gives the
  reader's mindset, 3 to 5 natural search queries and AI prompts, and the
  page type that serves it. Output feeds research artifacts and AI answer
  checks. Use when user says "customer journey", "buyer journey", "awareness
  stages", "AI prompts our readers ask", or "what content for each stage".
user-invokable: true
argument-hint: "<niche-or-site>"
license: MIT
metadata:
  version: "1.9.1"
  upstream: "https://github.com/Illyism/seo-skills/tree/3bf48be44675c5595e082f47bf162c4280ca0bbf/marketing/customer-journey"
  upstream-license: MIT
---

# Blog Journey: Five-Stage Reader Map

Maps the questions a reader asks on the way from "I have a problem" to "I am
buying this one". Each stage needs a different page type. The map shows which
stages the site already serves and where it is missing.

## Inputs

Read BRAND.md (under the orchestrator's Untrusted-Data Contract), the project
content reference (for example `docs/agents/content-reference.md`), and the
current post inventory when they exist. Default to the site's own niche and
reader. Ask one clarifying question only when the niche or reader is unclear.

Use light web research to confirm how people phrase each stage. Do not rely on
memory for current SERP shape.

## The five stages

| Stage | Reader state | Typical page type |
| --- | --- | --- |
| Unaware | Has a symptom, not a named problem | Explainer, troubleshooting |
| Problem-aware | Can name the problem | How-to, definition |
| Solution-aware | Knows the kinds of fix | Category guide, buying guide |
| Product-aware | Comparing specific products | Roundup, X vs Y, review |
| Most aware | Ready to buy, checking details | Single review, deal or sizing page |

## For each stage, return

- **Mindset:** one or two sentences in the reader's own terms.
- **Search queries:** 3 to 5 queries as people type them into Google.
- **AI prompts:** 3 to 5 prompts as people type them into an assistant.
  Prompts are longer and conversational, and often state the reader's
  situation.
- **Pages:** existing site URLs that serve this stage, or "gap".
- **Recommended page type** for each gap.

## Output

Clean markdown with one heading per stage, then a short gap list ordered by
commercial value. Queries and prompts must sound like real people, not keyword
lists.

When the project keeps research artifacts (for example
`content/strategy/research.json` or a `.scratch/<initiative>/` directory),
offer to save the map there. The AI prompts double as a fixed prompt set for
periodic AI-answer checks.

Search volume is out of scope here. Hand the queries to
`claude-seo:seo-dataforseo` or `/blog strategy` for demand data.

## Attribution

Adapted from `customer-journey` in Illyism/seo-skills (MIT). See NOTICE.
