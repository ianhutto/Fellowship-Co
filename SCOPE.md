# SCOPE.md — Fellowship Coffee Co. website

Status: v0.4 — 2026-09-22 — FAST TRACK · design and build only
Client: Fellowship Coffee Co. (Missouri City / Houston, TX)
Platform: Framer · Source of truth: github.com/ianhutto/Fellowship-Co

## Objective
A premium, high-taste Framer site for Fellowship that mirrors Night Owl's site architecture and vertical rhythm, with Fellowship's own content, type and component design, and converts visitors into event-catering quote requests.

## The build rules (settled — see DECISIONS.md)
| Layer | Rule |
|---|---|
| Architecture: sitemap, nav + dropdowns, page templates, section order and makeup, CTA routing | Mirrors nightowlcoffeecart.com (§A) |
| Vertical spacing rhythm | Matches Night Owl, measured per breakpoint (not guessed) |
| Content: words, facts, photos, reviews, numbers | Fellowship only |
| Type, component styling, color, motion | Fellowship's own (DESIGN.md) |
| Quality bar | Scores ≥4/5 on rubric items 1–6 (§D) side by side with Night Owl |

---

## Delivery plan — three tracks in parallel

### Track 1 — Claude (starts now, needs no one)
| # | Deliverable | Output |
|---|---|---|
| 1.1 | COPY.md v1.0 restructured to §A templates: Home (9), Weddings / Corporate / Celebrations (12 each), Quote, Menu, Coffee Shop, About, FAQ, 404. Gaps marked, never invented | COPY.md |
| 1.2 | Style sample v0.2: restraint pass — keep serif type, stamp, order-ticket cards; cut handwritten-note reviews; menu-board styling only on the menu; simplify stats | Design canvas |
| 1.3 | Quality rubric added to the process (§D) | process file |
| 1.4 | Framer build spec: tokens list, every component + variants, CMS schemas, page-by-page build order and Claude Code prompts, ready to run the moment Framer is connected | BUILD.md |
| 1.5 | Measure Night Owl's vertical spacing at Desktop / Tablet / Phone (in your Chrome, with your approval) → DESIGN.md spacing tokens | DESIGN.md |

### Track 2 — Ian (today)
| # | Action |
|---|---|
| 2.1 | Push the repo to GitHub (or add it to this session so Claude can) |
| 2.2 | Create the Framer project on a plan that supports the Claude Code connection; run Framer's setup; send the project URL |
| 2.3 | Send the owner the request list (Track 3) |
| 2.4 | Approve Chrome access for 1.5, or send measured values |
| 2.5 | React to style sample v0.2 → lock design |

### Track 3 — Owner (the critical path)
Priority order; the first two gate "premium".
1. **Photography + video:** cart at events, drinks, baristas, café. Enough for 4 heroes and a 4-image gallery per service page. This is the single biggest factor in looking premium.
2. **Brand assets:** logo (SVG), existing colors and fonts if any
3. Reviews: up to 5 per service, with permission; one rating source
4. Pricing: "from $550" current and publishable?
5. Current menu + signature drinks
6. FAQ answers: space, power, travel area/fees, guest counts, service length, lead time
7. Public name; credit for Ryan and Janice; mention faith or not
8. Full café hours; does the phone take texts?
9. Real numbers for stat tiles, or approval for "since 2021"
10. Client logos with permission, or confirmation there are none
11. Suite 325 — events at the shop?
12. Quote form destination; domain/DNS access

**Fallback so nothing stalls:** the build proceeds with labelled placeholders held in Framer CMS. Owner content drops in without rebuilding.

---

## Gates
| Gate | Done when |
|---|---|
| G1 · Copy locked | COPY.md v1.0 approved by Ian |
| G2 · Design locked | Style sample approved; DESIGN.md tokens (incl. measured spacing) final |
| G3 · Build complete | All pages built on a Framer branch from BUILD.md; placeholders only where owner content is missing |
| G4 · Quality pass | Independent reviewer scores ≥4 on rubric 1–6, all breakpoints; fix list closed |
| G5 · Publish | Owner content in, domain connected, redirects live, published on explicit go |

G3 can start as soon as G1 + G2 pass and Framer is connected. Owner content is not required to start building.

---

## §A Architecture spec (mirrors Night Owl)

### Global
- Utility bar: contact line + phone
- Header: logo · About · Services ▾ · Resources ▾ · CTA button (always visible)
- Footer: logo + tagline + CTA · Company · Services · Resources · Newsletter · social · legal
- Services ▾: Weddings · Corporate · Celebrations (+ Events at the Shop if confirmed)
- Resources ▾: FAQs · Menu · The Coffee Shop
- Every CTA → /quote (café page → directions)

### Home — 9 sections
1 Utility bar · 2 Hero (video, eyebrow, H1, sentence, CTA) · 3 Trust strip (marquee; real logos only, else one proof line) · 4 What we do · 5 Three alternating feature blocks · 6 Difference + 3 stat tiles · 7 Review carousel · 8 Closing CTA (3 benefit lines, background image) · 9 Footer

### Service page — 12 sections (Weddings, Corporate, Celebrations)
1 Header · 2 Hero (H1, sub, CTA, image) · 3 Trust strip (6 tiles, same fallback) · 4 Three overview cards · 5 Full-width image · 6 Testimonials (5; min 3 real, else hidden) · 7 Three stat tiles · 8 Four numbered cards · 9 Gallery (4) · 10 FAQ accordion (5) · 11 CTA (3 bullets) · 12 Footer

### Quote page (mirrors /book)
1 Hero · 2 Single-step form: name, email, phone, date, event type, venue/city, guest count, start + end time (30-min), how you heard, notes; success + error states · 3 Stats · 4 Reviews · 5 Footer

### Other pages (built from the same components)
Menu · The Coffee Shop · About · FAQ · 404

### Redirects
/cart → / · /contact → /quote · keep /the-coffee-shop, /about

## §B Design system (Fellowship's own)
Color styles · type scale per breakpoint · spacing scale (measured Night Owl rhythm) · grid · components with variants (nav, dropdown, buttons, eyebrow, section header, feature block L/R, overview card, numbered card, stat tile, review card, trust strip, gallery, accordion, form fields, CTA band, footer) · motion (one easing, fade-up, reduced-motion) · imagery rules.

## §C Out of scope
Night Owl's copy, images, logos, reviews, stats, type or component styling · blog / case studies / careers / brand guidelines pages · brand redesign · photo shoot · online ordering or payments · other languages · ads, ongoing SEO, maintenance after publish.

## §D Quality rubric (G4) — score 1–5, side by side with Night Owl at the same viewport
1. First 5 seconds: what, where, next step, feels premium
2. Photography: real, consistent, sells with text covered
3. Type hierarchy: one focal point per section; squint test
4. Spacing rhythm: consistent, generous, matches measured tokens
5. Restraint: one accent; brand codes used sparingly
6. Distinctiveness: recognisably Fellowship with the logo covered
7. Copy: short, specific, true; headlines tell the story
8. Craft: hover states, motion, alignment, no default styling
9. Mobile: designed for phone; one-handed use
10. Conversion: quote always one tap away; short form
Pass = ≥4 on 1–6, no item below 3.

## Acceptance
All pages match §A; every visual value from DESIGN.md; nav, accordions, carousels, marquee work on desktop and mobile; quote form delivers end to end; redirects work; SEO title, description and share image on every page; no invented facts, reviews, numbers or logos; owner can edit text, images, menu, reviews, FAQs and logos in Framer; G4 passed.
