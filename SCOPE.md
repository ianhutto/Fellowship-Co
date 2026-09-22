# SCOPE.md — Fellowship Coffee Co. website rebuild

Status: DRAFT v0.1 — 2026-09-22
Client: Fellowship Coffee Co. (Missouri City / Houston, TX)
Provider: [confirm — Ian / IML Labs]
Platform: Framer · Source of truth: github.com/ianhutto/Fellowship-Co

Timelines below are estimates in working days, assuming the client answers within 2 business days. They are not commitments until both sides agree.

---

## 1. Objective
Replace fellowshipcoffeetx.com with a Framer site that turns visitors into event-catering quote requests, and sends café visitors to the Missouri City shop. Fellowship's own content, palette and voice; page structure follows a proven event-coffee-cart funnel.

Success looks like:
- Every page leads to one action (Get a Quote, or Get directions for the café)
- Quote requests arrive where the owner wants them
- Owner can edit text, photos, menu, reviews and FAQs in Framer without a developer
- No live claim that the owner hasn't confirmed

## 2. Status — done
| Item | Status |
|---|---|
| Build process (9 steps, Framer edition) | ✅ done |
| Repo set up as source of truth | ✅ done locally — push to GitHub pending access |
| CONTEXT.md — facts, sourced and fact-checked | ✅ v0.4 draft — owner answers pending |
| COPY.md — every page drafted | ✅ v0.2 — 4 key headlines picked; full lock pending |
| Address + plaza | ✅ confirmed via Google listing |

## 3. In scope — remaining

### Phase A — Lock the content (Steps 1–3)
| # | Deliverable | Owner | Est. |
|---|---|---|---|
| A1 | Owner answers the open questions (see §5) | Client | — |
| A2 | CONTEXT.md v1.0, every fact confirmed | Provider | 0.5 d |
| A3 | COPY.md final — all [confirm] lines resolved; reviews, FAQ answers, menu filled in | Provider + Ian | 1 d |
| A4 | Headline approval table signed off → "COPY locked" | Ian (+ owner) | 0.5 d |

### Phase B — Design system (Step 4)
| # | Deliverable | Owner | Est. |
|---|---|---|---|
| B1 | Brand assets collected: logo, colors, fonts, photos, video (or current-site screenshots) | Client | — |
| B2 | Up to 5 reference sites + what's loved about each | Ian / owner | — |
| B3 | DESIGN.md: color styles, text styles, breakpoints, spacing, motion, components | Provider | 1 d |
| B4 | One-page style sample for review; up to 2 revision rounds → "DESIGN locked" | Provider | 0.5–1 d |

### Phase C — Build in Framer (Steps 5–6)
| # | Deliverable | Est. |
|---|---|---|
| C1 | Framer project + Claude Code connection; all work on a branch | 0.5 d |
| C2 | Color and text styles, breakpoints (Desktop / Tablet / Phone) | 0.5 d |
| C3 | Components with states: nav, buttons, section header, feature block, card, review, CTA band, form, footer | 1 d |
| C4 | CMS collections: Reviews, Services, FAQs, Menu items | 0.5 d |
| C5 | 10 pages (below), copy verbatim from COPY.md, SEO title + description each | 2 d |
| C6 | Quote form wired to the owner's chosen inbox/tool, with success and error states | 0.5 d |
| C7 | Extra components where a section needs them (native Framer rebuild first) | 0.5 d |

Pages (10): Home · Weddings · Corporate · Celebrations · Menu · The Coffee Shop · About · FAQ · Quote · 404
Conditional 11th: Events at the Shop — only if the Suite 325 expansion is confirmed.

### Phase D — Media (Step 7)
| # | Deliverable | Est. |
|---|---|---|
| D1 | Hero: owner's own video if available; otherwise one AI-generated loop (commercial-use terms checked) or a strong still | 0.5–1 d |
| D2 | Photo prep: crop, compress, alt text for every image | 0.5 d |

### Phase E — Iterate and QA (Steps 8–9)
| # | Deliverable | Est. |
|---|---|---|
| E1 | Up to 3 rounds of revisions on the Framer branch | 1–2 d |
| E2 | Independent quality check: copy, design, mobile, accessibility, speed, forms, links, SEO | 0.5 d |
| E3 | Fix list closed, or items consciously accepted in DECISIONS.md | 0.5 d |

### Phase F — Launch
| # | Deliverable | Est. |
|---|---|---|
| F1 | Connect fellowshipcoffeetx.com to Framer (DNS) | 0.5 d |
| F2 | Redirects: /cart → /, /contact → /quote; keep /the-coffee-shop and /about | incl. |
| F3 | Favicon, social share image, analytics (tool TBD), Google Business Profile link updated | 0.5 d |
| F4 | Publish on explicit go; post-launch check of forms, redirects and mobile | 0.5 d |
| F5 | 30-minute owner handoff + short "how to edit" guide | 0.5 d |

**Estimated total: roughly 14–18 working days of provider effort**, plus client wait time. Actual time depends mostly on how fast assets and answers arrive.

## 4. Out of scope (unless added by change request)
- Logo or brand redesign — we use Fellowship's existing brand
- Professional photo or video shoot
- Online ordering, payments, or booking/deposit system (the quote form sends a request only)
- Blog or content writing beyond the pages above
- Spanish or other language versions
- Paid ads, ongoing SEO, or social media management
- Framer plan, domain, and any paid tool subscriptions (paid by the client)
- Ongoing maintenance after handoff
- Content from nightowlcoffeecart.com — structural reference only

## 5. What we need from the client (blockers)
Priority order — the first four unblock the most.
1. Brand assets: logo files, colors, fonts, photos, any video (or full-page screenshots of the current site)
2. Pricing: is "from $550" current, and may we publish it?
3. Current menu and signature drinks
4. 3–6 reviews you're happy to feature + one rating source to show
5. Public business name; how to credit Ryan and Janice; whether to mention faith
6. Full café hours for the week
7. Does the phone number take texts?
8. Event details for FAQ: space, power, travel area and fees, guest counts, service length, booking lead time
9. Suite 325 expansion — finished? Do you host events at the shop?
10. Where should quote requests go (email, tool)?
11. Domain/DNS access and current website host
12. Framer plan decision (confirm the plan supports the Claude Code connection)

## 6. Acceptance criteria
The site is accepted when:
- All 10 pages are live on fellowshipcoffeetx.com, matching locked COPY.md and DESIGN.md
- Works on phone, tablet and desktop with no layout breaks
- Quote form delivers to the agreed destination (tested end to end)
- Old URLs redirect correctly
- Every page has an SEO title, description and share image
- No unconfirmed facts, prices, reviews or client names on the live site
- Owner can edit text, images, menu, reviews and FAQs in Framer

## 7. Risks
| Risk | Effect | Mitigation |
|---|---|---|
| Assets or answers arrive late | Timeline slips | Build with current-site screenshots; swap assets in later |
| No reviews or proof yet | Weaker trust sections | Use "since 2021" + press; add reviews via CMS later |
| Framer's Claude Code connection changes or isn't on the plan | Slower build | Fall back to building on the canvas by hand from the same files |
| Hero video quality | Looks generic | Prefer owner's real footage; still image as fallback |
| DNS access unknown | Launch delay | Identify who holds the domain in Phase A |

## 8. Change process
Anything outside §3 is a change request: describe it, estimate it, agree it, log it in DECISIONS.md, then build it.

## 9. Open commercial terms [TBD]
- Fee and payment schedule
- Target launch date
- Who signs off for the client (owner name)
