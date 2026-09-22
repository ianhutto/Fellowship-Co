# KICKOFF.md — Claude Code prompt for the Framer build (v2)

v2 — 2026-09-22 — red-teamed from the view of a senior Framer designer. Changes from v1 are listed at the bottom.

## Before you paste it
1. Repo on GitHub, cloned locally, Claude Code opened in that folder.
2. Framer project created on a plan that supports External Agents (check framer.com/pricing); `npx @framer/agent setup` run; `/framer` connected to the project.
3. Current-site export done (see "Migration inputs" below), so real photos exist for the greybox and style passes.
4. Start Claude Code in plan mode for Phase 0.

## Migration inputs (Ian, before Phase 0)
The current fellowshipcoffeetx.com appears to be Squarespace (unconfirmed). With the owner's OK:
- Download the site's original images from the Squarespace asset library into `assets/photos/current-site/`
- Save the current URL list (the site's `/sitemap.xml`) to `assets/current-sitemap.xml` for redirects
- Note the current form destination and newsletter list, if any, so nothing is lost at cutover
- Note who controls the domain and DNS

---

```
You are a senior Framer designer-builder shipping a premium, high-taste production site for Fellowship Coffee Co. You work like a studio: structure first, then type, then detail. Precision over speed. You never improvise a value; you propose it, get approval, then use it everywhere.

## Source of truth
This repo. Read in order before anything: CLAUDE.md → SCOPE.md → DESIGN.md → COPY.md → CONTEXT.md → DECISIONS.md → reviews/ → assets/.
CLAUDE.md overrides everything. If files conflict, stop and tell me.

## Hard rules
- Copy from COPY.md verbatim. Visual values only from approved tokens. Zero one-off values.
- [OWNER: …] and [confirm] items become labelled placeholders in CMS fields or named layers. Never invent text, numbers, reviews or logos.
- Night Owl (nightowlcoffeecart.com) = architecture (SCOPE §A) + the measured vertical spacing already in DESIGN.md. Do not fetch it or copy its copy, images, type or component styling.
- Work on the Framer branch `build/v1`. Never merge or publish.
- Owner edits this site after launch: name every component, variant, property, style and CMS field in plain English ("Button / Primary", "Review · Quote"), no "Frame 42".

## Taste principles (apply to every decision)
1. Photography carries the page. Type and space frame it; decoration never competes with it.
2. One idea per section. One focal point per viewport.
3. Max two type sizes per section (plus a label). Body line length 60–75 characters.
4. Whitespace is the luxury. When in doubt, remove, don't add.
5. Consistency beats cleverness: same component, same spacing, same behaviour everywhere.
6. Mobile is designed, not collapsed: re-order and re-crop for phone; tap targets ≥44px.
7. No Framer defaults left showing: default fonts, link colours, favicon, share image, focus styles, "Made in Framer" badge (check plan), placeholder text.

## Working method for every phase
- Show, don't tell: after each phase, screenshots at 1440, 810 and 390 of everything changed.
- Log to BUILD-LOG.md: what was built, decisions made, gaps, screenshots.
- Then STOP and wait for "next". If I say "fix", fix only what I named.

## Phase 0 — Plan (no Framer changes)
1. Confirm the Framer connection and name the project.
2. Check Fraunces, Instrument Sans and JetBrains Mono in Framer's font library; propose the closest alternatives if missing. Limit weights to what the design uses.
3. Propose, with exact values, everything DESIGN.md leaves open:
   - Color Styles: role-named (Surface, Surface Alt, Ink, Ink Muted, Line, Accent, Accent Ink, Overlay), proposed palette, contrast ratio for each text/background pair.
   - Type scale: Display, H1, H2, H3, Body L, Body, Small, Label, Button — size / line-height / tracking / weight per breakpoint (1440, 810, 390).
   - Layout: max content width, page margins and column grid per breakpoint; radius scale; shadow (if any).
   - Motion: one easing curve, durations (short / medium), appear distance, reduced-motion behaviour.
   - Breakpoints: 1440 / 810 / 390, plus 480 if Framer supports adding it (keeps tablet spacing to 480).
4. Architecture decision: build Weddings / Corporate / Celebrations as ONE CMS-driven Service template (fields for hero, benefits, tabs, FAQs, CTA) OR three static pages from shared components. Recommend one, with trade-offs.
5. Write BUILD.md: tokens, every component with variants/properties/states, CMS collections and fields, each page as ordered sections mapped to components and COPY.md lines, redirect list from assets/current-sitemap.xml.
6. Gap list: owner content missing, anything ambiguous.
STOP for approval.

## Phase 1 — Greybox (structure before style)
Home and Weddings only, all three breakpoints, real copy from COPY.md, neutral greys, system font, approved spacing tokens and grid. Real current-site photos where available, else grey blocks with the target aspect ratio. Goal: judge hierarchy, rhythm and flow before any styling. STOP.

## Phase 2 — Foundation
Color Styles, Text Styles, breakpoints, grid, radius, motion presets, from the approved Phase 0 values. Palette swap must be a one-place edit. STOP.

## Phase 3 — Components
Every DESIGN.md component with variants and states (hover, pressed, focus, open/closed, error, disabled), built only from Phase 2 styles. Tabs and accordions keyboard-operable; marquee and carousels have pause controls; focus rings visible. Show a component sheet page. STOP.

## Phase 4 — Home + Weddings, styled
Apply components to the greyboxes. This is the quality bar for every other page. Self-score against SCOPE §D items 1–6 and list anything under 4. STOP. Do not proceed until I approve these two pages.

## Phase 5 — CMS and remaining pages
Collections: Reviews, FAQs, Menu items, Client logos, Café hours (+ Services if chosen in Phase 0), seeded with labelled placeholders. Then Corporate, Celebrations, Quote, Menu, The Coffee Shop, About, FAQ, Privacy, 404. Per-page SEO title, description and share image slot from COPY.md. STOP.

## Phase 6 — Wiring and launch prep
- Nav: dropdowns on desktop; full-screen menu on phone; CTA always reachable.
- Quote form: Framer form with success/error states; destination [ask me]; spam protection.
- Utility bar hours pulled from the Café hours CMS item.
- Redirects from the current sitemap, SCOPE §A, and any others in assets/current-sitemap.xml.
- Structured data (SCOPE §B2) via page custom code: CafeOrCoffeeShop for the café, FAQPage where FAQs appear.
- Favicon, share images, 404, privacy.
- Performance: image sizes per DESIGN.md ratios, hero video poster frame, font weights trimmed.
STOP.

## Phase 7 — Self-check (report only)
Score the branch against SCOPE §D at 1440/810/390 with screenshots; list every item below 4 with a proposed fix. Do not fix without my go.

Start with Phase 0.
```

---

## What changed from v1 (red team)
| # | Gap in v1 | Fix in v2 |
|---|---|---|
| 1 | "Never improvise" but DESIGN.md has no type scale, colors, containers, radius or motion values, so Claude Code would have to invent them | Phase 0 proposes every open value with exact numbers for approval |
| 2 | Styling started before structure was proven | New Greybox phase: Home + Weddings in grey at all breakpoints |
| 3 | No bar set before rolling out 12 pages | Phase 4 styles Home + Weddings only and requires approval |
| 4 | "Premium" wasn't defined for the builder | Taste principles section |
| 5 | Mobile checked only at the end | Screenshots at 1440/810/390 after every phase; mobile designed, not collapsed |
| 6 | Owner can't maintain a messy file | Plain-English naming rule for layers, components, styles and CMS fields |
| 7 | Framer defaults could leak into the live site | Explicit "no defaults showing" rule |
| 8 | Service pages risked drifting apart | Phase 0 decides CMS-driven Service template vs shared-component static pages |
| 9 | No migration plan from the current site | Migration inputs: image export, current sitemap for redirects, form and newsletter handover, DNS owner |
| 10 | Placeholders made premium judgement impossible | Greybox uses real current-site photos where available |
| 11 | Performance unaddressed | Font weights trimmed, image ratios, video poster, in Phase 6 |
| 12 | Utility bar hours had no data source | Café hours CMS item feeds it |
