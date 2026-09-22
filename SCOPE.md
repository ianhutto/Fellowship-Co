# SCOPE.md — Fellowship Coffee Co. website

Status: DRAFT v0.3 — 2026-09-22 — design and build only
Client: Fellowship Coffee Co. (Missouri City / Houston, TX)
Platform: Framer · Source of truth: github.com/ianhutto/Fellowship-Co
Standard: production-grade, high-taste build. Every value is decided and documented in DESIGN.md; nothing is improvised on the canvas.

---

## 1. What this build is

| Layer | Rule |
|---|---|
| **Architecture**: sitemap, nav + dropdown groupings, page templates, section order, section makeup (item counts, cards, accordions, galleries), CTA routing | **Mirrors nightowlcoffeecart.com**, mapped from their live pages (§3). Deviations only where Fellowship lacks the content; each is listed. |
| **Content**: every word, fact, photo, review, number | **Fellowship only**, from CONTEXT.md and COPY.md. Nothing from Night Owl. |
| **Visual design**: palette, type, spacing system, components, motion | **Fellowship's own**, built from Fellowship's brand assets to a production standard. Not measured or copied from Night Owl. Spacing is a deliberate, documented system in DESIGN.md. |

Why the split: page architecture is a common pattern. Night Owl's visual design and content are their (and their design studio's) work; copying them would produce their site with Fellowship's colors on it.

## 2. Status — done
| Item | Status |
|---|---|
| Build process (9 steps, Framer edition) | ✅ |
| Repo as source of truth | ✅ local — GitHub push pending access |
| CONTEXT.md — sourced, fact-checked | ✅ v0.4 — owner answers pending |
| COPY.md — all pages drafted | ✅ v0.2 — needs restructure to the templates below (A3) |
| Night Owl architecture mapped: Home, Service page, Book page | ✅ 2026-09-22 |

## 3. Architecture spec (mirrors Night Owl)

### 3.1 Global
- **Utility bar:** contact line + phone
- **Header:** logo · About · Services ▾ · Resources ▾ · primary CTA button, always visible
- **Footer:** logo + tagline + CTA · 4 columns (Company · Services · Resources · Newsletter signup) · social links · legal links

Dropdown mapping:
| Night Owl | Fellowship | Note |
|---|---|---|
| Services ▾ — 6 service pages | Services ▾ — Weddings · Corporate · Celebrations | 3, not 6: only services Fellowship offers. A 4th (Events at the Shop) if the owner confirms. |
| Resources ▾ — 5 links (blog, case studies, FAQs, brand guidelines, careers) | Resources ▾ — FAQs · Menu · The Coffee Shop | No Fellowship content exists for a blog, case studies, careers or brand guidelines. Not built unless the owner supplies content. |
| "Latest blog" promo in the nav | Omitted | No blog |

CTA routing: every CTA → /quote (the café page's CTA → directions).

### 3.2 Home template — 9 sections
| # | Section | Makeup | Fellowship content |
|---|---|---|---|
| 1 | Utility bar | contact line + phone | COPY.md |
| 2 | Hero | background video · eyebrow (service + area) · H1 · one sentence · 1 CTA | Fellowship video or still |
| 3 | Trust strip | scrolling logo marquee | Real, permissioned client logos only. Until then, one proof line in the same slot ("Serving Houston since 2021") |
| 4 | What we do | eyebrow · H2 · paragraph · text link to services | COPY.md |
| 5 | Feature blocks | 3 blocks, alternating image / text; each: icon · H3 · paragraph · CTA | Weddings · Corporate · Celebrations |
| 6 | Difference | eyebrow · H2 · paragraph · CTA · 3 stat tiles with icons | Real numbers only |
| 7 | Reviews | review carousel; each card: stars · quote · name | Owner-supplied, permissioned |
| 8 | Closing CTA | eyebrow · H2 · supporting line · CTA · 3 short benefit lines · background image | COPY.md; no urgency statistic unless real |
| 9 | Footer | global | — |

### 3.3 Service page template — 12 sections (Weddings, Corporate, Celebrations)
Mapped from nightowlcoffeecart.com/services/mobile-activations-national-tours.
| # | Section | Makeup |
|---|---|---|
| 1 | Header | global |
| 2 | Hero | H1 · sub · CTA · image |
| 3 | Trust strip | 6 logo tiles; same fallback rule as Home §3 |
| 4 | Service overview | 3-column cards: headline · description · CTA link |
| 5 | Feature image | single full-width image |
| 6 | Testimonials | 5 cards: stars · quote · attribution |
| 7 | Stats | 3 metric tiles |
| 8 | Built-for | 4 numbered cards: headline · description · CTA |
| 9 | Gallery | 4 images |
| 10 | FAQ | accordion, 5 Q&A |
| 11 | CTA | H2 · sub · 3 benefit bullets · CTA |
| 12 | Footer | global |

Content rule: sections 3, 6 and 7 render only with real Fellowship proof. With fewer than 5 permissioned reviews, the section shows what exists (minimum 3) or is hidden. It is never filled with invented quotes.

### 3.4 Quote page template (mirrors /book)
| # | Section | Makeup |
|---|---|---|
| 1 | Hero | H1 · sub |
| 2 | Form | single step. Fields: name · email · phone · event date · event type (Wedding / Corporate / Celebration / Other) · venue or city · guest count · service start time · service end time (30-minute dropdowns) · how you heard about us · notes. Success + error states. |
| 3 | Stats | real numbers only |
| 4 | Reviews | permissioned reviews |
| 5 | Footer | global |

### 3.5 Other pages
Night Owl has no direct equivalent mapped yet. Built from the Service template's components:
- /menu: hero · menu categories (CMS) · signature drinks · CTA
- /the-coffee-shop: hero · hours + address + directions · gallery · CTA
- /about: hero · story · founders · gallery · CTA
- /faq: hero · accordion by category (CMS) · CTA
- 404

To mirror these too, name the Night Owl page for each (e.g. their About or FAQs page) and it gets mapped the same way.

## 4. Design standard (Fellowship's own, production grade)
DESIGN.md defines these tokens, and Framer uses only them:
- **Color styles** from Fellowship's brand
- **Type scale:** display, H1–H3, body, small, eyebrow, button; sizes per breakpoint
- **Spacing system:** one base unit and scale; fixed section padding per breakpoint (Desktop / Tablet / Phone); max content width; card and grid gaps. Every section uses these values; no one-off spacing.
- **Grid:** columns and gutters per breakpoint
- **Components with variants:** nav (open/closed) · dropdown · buttons (primary/secondary × default/hover/pressed) · eyebrow · section header · feature block (image-left / image-right) · card · numbered card · stat tile · review card · logo strip · gallery · accordion item · form fields (default/focus/error) · CTA band · footer
- **Motion:** one easing, 2–3 durations, appear-on-scroll, marquee speed, carousel behavior, reduced-motion fallback
- **Imagery:** crops, aspect ratios, treatment, alt-text rule
- Style sample reviewed and locked before any page is built

## 5. In scope — remaining

### Phase A — Lock the content
| # | Deliverable | Owner |
|---|---|---|
| A1 | Owner answers open questions (§7) | Client |
| A2 | CONTEXT.md v1.0: every fact confirmed | Provider |
| A3 | COPY.md v1.0 restructured to §3: Home (9 sections), 3 service pages × 12 sections, Quote, Menu, Coffee Shop, About, FAQ, 404 | Provider |
| A4 | Headline table approved → "COPY locked" | Ian (+ owner) |

### Phase B — Design system
| # | Deliverable | Owner |
|---|---|---|
| B1 | Brand assets: logo, colors, fonts, photos, video (or current-site screenshots) | Client |
| B2 | DESIGN.md per §4 | Provider |
| B3 | Style sample (tokens + key components); up to 2 rounds → "DESIGN locked" | Provider |

### Phase C — Build in Framer
| # | Deliverable |
|---|---|
| C1 | Framer project + Claude Code connection; all work on a branch |
| C2 | Color and text styles, spacing, breakpoints, grid from DESIGN.md |
| C3 | All §4 components with variants |
| C4 | CMS: Reviews · Services · FAQs · Menu items · Client logos |
| C5 | Templates: Home, Service, Quote; then Menu, Coffee Shop, About, FAQ, 404 |
| C6 | Pages: Home · Weddings · Corporate · Celebrations · Quote · Menu · The Coffee Shop · About · FAQ · 404. Copy verbatim; SEO title + description on each |
| C7 | Nav with Services ▾ and Resources ▾ dropdowns; desktop and mobile menu |
| C8 | Quote form wired to the owner's chosen destination; success + error states |

### Phase D — Media
| # | Deliverable |
|---|---|
| D1 | Hero video: Fellowship footage preferred; otherwise one AI-generated loop (commercial terms checked) or a still |
| D2 | Photo set: crops per DESIGN.md ratios, compressed, alt text; a 4-image gallery per service page |

### Phase E — QA
| # | Deliverable |
|---|---|
| E1 | Architecture check: every page matches §3 section order and makeup; deviations only as listed |
| E2 | Design check: only DESIGN.md tokens used; spacing consistent at every breakpoint |
| E3 | Independent quality pass: copy, mobile, accessibility, speed, forms, links, SEO |
| E4 | Up to 3 revision rounds on the branch |

### Phase F — Publish
| # | Deliverable |
|---|---|
| F1 | Connect fellowshipcoffeetx.com (DNS) |
| F2 | Redirects: /cart → / · /contact → /quote · keep /the-coffee-shop and /about |
| F3 | Favicon, share image, analytics snippet |
| F4 | Publish on explicit go; live check of forms, redirects and mobile |

## 6. Out of scope
- Copying Night Owl's visual design, measured spacing, copy, images, logos, reviews or stats
- Blog, Case Studies, Careers, Brand Guidelines pages (no Fellowship content)
- Logo or brand redesign; photo or video shoot
- Online ordering, payments, deposits (the form sends a request only)
- Spanish or other languages
- Ads, ongoing SEO, social, maintenance after publish

## 7. Needed from the client
1. Brand assets: logo, colors, fonts, photos (enough for heroes and a 4-image gallery per service page), video
2. Reviews: up to 5 per service page, with permission; one rating source
3. Real numbers for stat tiles (events served, years, rating), or approval to use "since 2021" / "from $550"
4. Client logos with permission for the trust strips, or confirmation there are none
5. Pricing: is "from $550" current and publishable?
6. Current menu and signature drinks
7. 5 FAQ answers per service: space, power, travel area and fees, guest counts, service length, lead time
8. Public name; credit for Ryan and Janice; whether to mention faith
9. Full café hours; does the phone take texts?
10. Suite 325: events at the shop? (adds a 4th service page)
11. Quote form destination
12. Domain/DNS access; a Framer plan that supports the Claude Code connection

## 8. Acceptance criteria
- Every page matches its §3 template in section order and makeup, with only the listed deviations
- Every visual value comes from DESIGN.md; spacing consistent on Desktop, Tablet and Phone
- Nav dropdowns, accordions, carousels and marquee work on desktop and mobile
- Quote form delivers end to end
- Old URLs redirect
- SEO title, description and share image on every page
- No invented or unconfirmed facts, reviews, numbers or logos
- Owner can edit text, images, menu, reviews, FAQs and logos in Framer
