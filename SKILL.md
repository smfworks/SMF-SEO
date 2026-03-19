# SMF SEO — SEO Content Engine

Create content that ranks. This skill guides you through the entire SEO content workflow — from keyword research to published draft — with data-driven decisions at every step.

## What It Does

- **Keyword Research**: Find low-competition, high-intent keywords
- **SERP Analysis**: Understand what Google wants for your target keyword
- **Content Outlines**: Structure articles that satisfy search intent
- **SEO-Optimized Drafts**: Write with proper heading hierarchy, internal links, and meta tags
- **Content Refresh**: Update old posts to regain lost rankings

## SMF Works Context

- **Domain:** smfworks.com
- **Primary services:** AI automation consulting, lead gen systems, workflow optimization
- **Content pillars:**
  1. AI tools for small business
  2. Automation workflows (Zapier, Make, n8n, OpenClaw)
  3. Lead generation systems
  4. No-code/low-code solutions
- **Target audience:** Small business owners, entrepreneurs, solopreneurs who need AI automation but don't have technical teams
- **Audience pain points:** Manual processes eating time, can't afford enterprise tools, confused by AI hype, don't know where to start with automation
- **Brand voice:** Direct, practical, skip the jargon, show don't tell, no corporate fluff
- **Key competitors to monitor:** [Add competitors]
- **Existing high-performing content:** [Add top posts for internal linking]

## Quick Start

### 1. New Article from Keyword

"Create an SEO-optimized article targeting the keyword: 'best project management software for small teams'

Target word count: 2000
Tone: Professional but approachable
Include: Comparison table, pricing section, FAQ"

### 2. Content Refresh

"Refresh this old blog post for better SEO performance:
[paste existing content]

Target keyword: [keyword]
Current issues: [dropped rankings, outdated info, etc.]
Add: Current data, new sections, better internal links"

### 3. Content Strategy

"Build a 3-month content calendar for a [industry] business targeting [audience].

Focus topics: [topic 1], [topic 2], [topic 3]
Goal: [leads/brand awareness/authority]
Output: 12 article ideas with target keywords and priority scores"

## The SEO Content Workflow

### Phase 1: Keyword Intelligence (Agent Actions)

**Input:** Seed topic or competitor URL
**Output:** Prioritized keyword list with difficulty scores

**Agent Steps:**
1. Run `web_search` with seed topic to find related queries
2. Run `web_search` with "[topic] vs" and "[topic] how to" to find long-tail variants
3. Run `web_fetch` on Google's "People Also Ask" results
4. Score keywords by: intent match × likely volume × competition signal
5. Output ranked list with reasoning for top 5 picks

**Key metrics to consider:**

- **Search Volume:** Monthly searches (higher ≠ always better)
- **Keyword Difficulty:** Competition level (start with <30 for new sites)
- **Search Intent:** Informational, navigational, transactional, commercial
- **CPC:** Cost-per-click indicates commercial value
- **Trend:** Seasonal or growing interest?

### Phase 2: SERP Analysis (Agent Actions)

Before writing, analyze the top 10 results:

**Agent Steps:**
1. `web_search` the target keyword
2. For each of the top 5 results:
   - `web_fetch` the URL
   - Extract: title, H1, H2s, approximate word count
   - Note: content type (listicle, guide, comparison)
3. Identify content gaps (topics top results miss)
4. Output: SERP analysis report with recommended angle

**What to analyze:**

- **Content Type:** Blog post? Product page? Listicle? Guide?
- **Content Depth:** Word count, sections covered, detail level
- **Content Gaps:** What's missing that you can add?
- **Common Elements:** Do all top results have videos? Tables? FAQs?
- **Domain Authority:** Are you competing with Wikipedia or small blogs?

### Phase 3: Outline Creation

Structure for SEO success:

```
H1: Target Keyword (exact or close variant)
 H2: Introduction (hook + promise + proof)
 H2: What is [Topic]? (definition for informational intent)
 H2: Why [Topic] Matters (benefits, statistics)
 H2: [Number] Best [Topic] Options (for listicles)
   H3: Option 1
   H3: Option 2
   H3: Option 3
 H2: How to Choose (buying guide section)
 H2: [Topic] FAQ
 H2: Conclusion (CTA + summary)
```

### Phase 4: Content Writing with E-E-A-T

**E-E-A-T Requirements (Critical for 2026):**

- **Experience:** Demonstrate firsthand knowledge. Use "we've implemented this for clients" or "in our testing..."
- **Expertise:** Cite authoritative sources, include expert quotes, reference industry data
- **Authoritativeness:** Link to SMF Works' existing content, mention credentials where relevant
- **Trustworthiness:** Include author bio, cite sources, be transparent about limitations

**SMF Works E-E-A-T Assets to Leverage:**
- Client implementations: "We've set up 50+ automation workflows..."
- Real data: "In our testing of 10 AI tools..."
- Process screenshots: "Here's our actual n8n workflow..."
- Industry expertise: "Having worked with 100+ small businesses..."

**On-Page SEO Checklist:**

- [ ] Title tag: 50-60 chars, includes keyword near front
- [ ] Meta description: 150-160 chars, compelling CTA, includes keyword
- [ ] URL slug: Short, keyword-rich, no stop words
- [ ] H1: One per page, includes keyword naturally
- [ ] H2-H6: Logical hierarchy, keywords where natural
- [ ] Internal links: 2-5 to relevant SMF Works pages
- [ ] External links: 1-3 to authoritative sources
- [ ] Images: Descriptive filenames, alt text, compressed
- [ ] Schema markup: Article, FAQ, HowTo where applicable
- [ ] Mobile-friendly: Responsive design
- [ ] Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1

**Content Quality Standards:**

- Original insights, not just rehashed content
- Expert quotes or data where possible
- Actionable takeaways in every section
- Scannable with bullet points and short paragraphs
- Multimedia: images, videos, infographics
- **People-first:** Write for humans, not search engines (Google's Helpful Content System)

**Semantic Coverage:**

Instead of "keyword density," cover related subtopics and questions:
- Google's "People Also Ask" questions
- Related searches at bottom of SERP
- Subtopics from top-ranking content
- Industry terminology and concepts

### Phase 5: Optimization & Publishing

**Pre-publish Checklist:**

- [ ] Grammar/spelling check
- [ ] Readability score (aim for 8th grade)
- [ ] Semantic coverage: Related subtopics naturally included
- [ ] Featured snippet optimization: Answer in first paragraph (40-60 words), use definition-style formatting
- [ ] Social sharing: Open Graph tags, Twitter cards
- [ ] E-E-A-T check: Author bio, citations, unique expertise demonstrated

**Post-publish:**

- Share on social media
- Build internal links from existing content
- Monitor rankings after 2-4 weeks
- Update based on performance data

## Content Refresh Strategy

When to refresh:
- Dropped 5+ positions in rankings
- Outdated information (older than 1 year)
- Competitors published better content
- Traffic declining month-over-month

Refresh process:
1. Re-analyze SERP for new competitors
2. Update statistics and examples
3. Add new sections based on content gaps
4. Improve internal linking
5. **Only update publish date if significant changes made** (Google penalizes date-only updates)
6. Resubmit to Google Search Console (manual user step)

## Technical SEO Basics

**Core Web Vitals:**
- **LCP (Largest Contentful Paint):** < 2.5 seconds
- **INP (Interaction to Next Paint):** < 200 milliseconds
- **CLS (Cumulative Layout Shift):** < 0.1

**Crawl & Index:**
- XML sitemap submitted to Google Search Console
- Robots.txt configured properly
- Canonical URLs set for duplicate content
- Noindex on thin/duplicate pages

**Structured Data:**
- Article schema for blog posts
- FAQ schema for FAQ sections
- HowTo schema for tutorials
- Organization schema for SMF Works

## Link Building Guidance

**Internal Linking:**
- Link to 2-5 relevant existing SMF Works articles
- Use descriptive anchor text (not "click here")
- Prioritize high-authority pages

**External Link Building (Manual/User-driven):**
- Guest posting on industry blogs
- Digital PR (original research, data studies)
- Broken link building

## Content Clustering & Topic Authority

Build topical authority with pillar + cluster content:

**Pillar Page:** Comprehensive guide (3,000+ words) covering broad topic
**Cluster Content:** 5-10 focused articles (1,000-2,000 words) on subtopics

**Example for SMF Works:**
- **Pillar:** "The Complete Guide to AI Automation for Small Business"
- **Cluster:**
  - "Best AI Email Automation Tools"
  - "How to Automate Lead Scoring"
  - "n8n vs Zapier: Which is Better?"
  - "AI Customer Service: Setup Guide"
  - "10 Workflow Automations to Save 10 Hours/Week"

**Internal Linking Architecture:**
- All cluster posts link TO the pillar
- Pillar links TO relevant cluster posts
- Cluster posts link to each other where relevant

## Competitor Content Gap Analysis (Agent Actions)

**When:** Before writing any article
**Purpose:** Find what competitors rank for that you don't

**Agent Steps:**
1. `web_search` "site:competitor.com [your topic]" to find their top content
2. `web_fetch` 3-5 of their highest-ranking URLs
3. Extract their H2s, word count, and target keywords
4. `web_search` "[competitor] vs" and "alternatives to [competitor]" for opportunity keywords
5. Identify: What topics do they cover that you don't? What angles are they missing?
6. Output: Gap analysis report with priority content opportunities

**Example Output:**
"Competitor X ranks for 'AI automation examples' with a 2,000-word guide. We have no equivalent. Recommended: Create '50 AI Automation Examples for Small Business' (2,500 words, includes industry-specific breakdowns)."

## When to Spawn Subagents

Use `sessions_spawn` for:

1. **Long-form drafting** (>1,500 words)
   - Spawn writing model (e.g., ollama/kimi-k2.5:cloud) with full content brief
   - Include: target keyword, outline, SMF brand voice, internal links
   - Wait for completion, review, then publish

2. **Multi-article content calendars**
   - Spawn subagent to research and brief 12 articles
   - Output: 12 content briefs with keywords and priority scores

3. **SERP analysis at scale**
   - Spawn subagent to analyze top 10 results for 5 target keywords
   - Parallel processing saves time

4. **Content refresh batching**
   - Spawn subagent to audit 10 existing posts
   - Output: Refresh priority list with specific recommendations

**Do NOT spawn for:**
- Single paragraph responses
- Simple web searches
- Tasks requiring immediate back-and-forth
- Resource page outreach

## Success Metrics

- **Rankings:** Target top 10 for primary keyword within 8 weeks
- **Traffic:** Minimum 100 organic sessions/month per article after 3 months
- **CTR:** Above 3% average from search results
- **Engagement:** Average time on page > 2 minutes
- **Conversions:** At least 1 conversion action per 500 sessions

## Tools Integration

This skill works with:
- `web_search` — for keyword and competitor research
- `web_fetch` — for SERP analysis
- `summarize` — for competitor content analysis
- `sessions_spawn` — for drafting with writing models (use for long-form content generation)

## AI Content Considerations

With Google's stance on AI-generated content:
- Always have human review before publishing
- Add unique expertise, personal anecdotes, original research
- Avoid generic AI patterns (overly formal tone, repetitive structure)
- Ensure content demonstrates E-E-A-T
- Use AI as a starting point, not the final product

---

*SMF Works SEO Content Engine — Optimized for OpenClaw*
