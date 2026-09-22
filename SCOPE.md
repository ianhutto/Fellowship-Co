# SCOPE.md — Fellowship Coffee Co. website

Status: v0.5 — 2026-09-22 — FAST TRACK · design and build only · red-team fixes applied
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
| 1.1 | ✅ COPY.md v1.1: §A templates — Home (9), Weddings / Corporate / Celebrations (10 each), Quote, Menu, Coffee Shop, About, FAQ, Privacy, 404. Gaps marked, never invented | COPY.md |
| 1.2 | Style sample v0.2 to match DESIGN v0.2 restraint pass (two brand codes only) | Design canvas |
| 1.3 | ✅ Quality rubric (§D) + red team (reviews/) | SCOPE, reviews/ |
| 1.4 | Framer build spec: tokens list, every component + variants, CMS schemas, page-by-page build order and Claude Code prompts, ready to run the moment Framer is connected | BUILD.md |
| 1.5 | ✅ Night Owl vertical spacing measured → DESIGN.md tokens. Re-check on the weddings page | DESIGN.md |

### Track 2 — Ian (today)
| # | Action |
|---|---|
| 2.1 | Push the repo to GitHub (or add it to this session so Claude can) |
| 2.2 | Create the Framer project on a plan that supports the Claude Code connection; run Framer's setup; send the project URL |
| 2.3 | Send the owner the request list (Track 3) |
| 2.4 | ✅ Chrome access approved |
| 2.5 | React to style sample v0.2 → lock design |

### Track 3 — Owner (the critical path)
Priority order; the first two gate "premium".
1. **Photography + video:** cart at events, drinks, baristas, café. See the shot list in DESIGN.md: 4 heroes, 4 numbered-tab images per service page, café and founder photos. This is the single biggest factor in looking premium.
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
| G1 · Copy locked | COPY.md v1.1+ approved by Ian |
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

### Service page — 10 sections (Weddings, Corporate, Celebrations; mapped from Night Owl's weddings page)
1 Header · 2 Hero (large image, H1, sub, CTA) · 3 Trust strip (6; real only, else press line) · 4 Three benefit cards · 5 Testimonials (5; min 3 real, else hidden) · 6 Three stat tiles · 7 Four numbered tabs, one image each · 8 FAQ accordion (5) · 9 CTA with 3 benefits · 10 Footer
Confirm this order visually on Night Owl's weddings page before G1 (text-read counts varied).

### Quote page (mirrors /book)
1 Hero · 2 Single-step form: name, email, phone (optional), date, event type, venue/city, guest count, start + end time (30-min), how you heard, notes; success + error states · 3 Stats · 4 Reviews · 5 Footer

### Other pages (built from the same components)
Menu · The Coffee Shop · About · FAQ · Privacy · 404

### Redirects
/cart → / · /contact → /quote · /gallery → /the-coffee-shop · keep /the-coffee-shop, /about

## §B Design system (Fellowship's own)
Color styles · type scale per breakpoint · spacing scale (measured Night Owl rhythm) · grid · components with variants (nav, dropdown, buttons, eyebrow, section header, feature block L/R, benefit card, numbered tabs, stat tile, review card, trust strip, gallery, accordion, form fields, CTA band, footer) · motion (one easing, fade-up, reduced-motion) · imagery rules.

## §B2 Launch essentials
- Breakpoints: Desktop 1440 · Tablet 810 · Phone 390, plus a 480 breakpoint so 480–809 keeps tablet spacing (matches measured rhythm)
- Local SEO: LocalBusiness/CafeOrCoffeeShop structured data for the café (address, phone, hours); Service data on each event page; FAQ data on FAQ sections; Google Business Profile link in footer and café page
- Analytics: tool TBD; conversion events on quote submit and phone-link tap
- Form: destination, spam protection, auto-reply email
- Accessibility: pause controls on marquee and carousels; visible focus states; alt text; ≥4.5:1 contrast including small mono labels; keyboard-operable tabs and accordions
- Privacy page (form + newsletter collect personal data)
- Favicon, share images per page

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
Pass = ≥4 on 1–6, no item below 3. Item 2 is scored on real photography only; G4 cannot pass on placeholders.

## Acceptance
All pages match §A; every visual value from DESIGN.md; nav, accordions, carousels, marquee work on desktop and mobile; quote form delivers end to end; redirects work; SEO title, description and share image on every page; no invented facts, reviews, numbers or logos; owner can edit text, images, menu, reviews, FAQs and logos in Framer; G4 passed.
