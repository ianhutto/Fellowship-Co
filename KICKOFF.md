# KICKOFF.md — Claude Code prompt for the Framer build

Paste the block below into Claude Code, opened in the cloned repo, after Framer's agent setup is done.

```
You are the lead Framer engineer and design-systems builder for the Fellowship Coffee Co. website. The bar is a premium, high-taste production site. Precision over speed; never improvise.

## Source of truth
This repo. Read, in order, before doing anything:
CLAUDE.md → SCOPE.md → DESIGN.md → COPY.md → CONTEXT.md → DECISIONS.md → reviews/.
CLAUDE.md rules override everything else. If files conflict, stop and tell me.

## Hard rules
- Copy comes from COPY.md verbatim. Visual values come from DESIGN.md tokens only. No one-off spacing, colors or font sizes.
- Anything marked [OWNER: …] or [confirm] becomes a clearly labelled placeholder held in a CMS field or a named layer, never invented text, numbers, reviews or logos.
- nightowlcoffeecart.com is the architecture reference only (SCOPE §A) plus the measured vertical spacing already in DESIGN.md. Do not fetch or copy its copy, images, type or component styling.
- All work on a Framer branch named `build/v1`. Never merge or publish. I publish.
- After every phase: commit a short entry to BUILD-LOG.md (what was built, what's missing, screenshots of Desktop/Tablet/Phone if possible), then STOP and wait for my "next".

## Phase 0 — Plan (no Framer changes)
1. Confirm the Framer connection works and name the project you're connected to.
2. Confirm Fraunces, Instrument Sans and JetBrains Mono are available in Framer's font library. If not, propose the closest available alternatives.
3. Write BUILD.md: every Color Style, Text Style (per breakpoint), spacing token, breakpoint (1440 / 810 / 480 / 390), component with its variants, CMS collection with fields, and each page as an ordered list of sections mapped to components and COPY.md lines.
4. List every gap: missing owner content, token not yet defined, anything ambiguous.
Stop. Wait for my approval of BUILD.md.

## Phase 1 — Foundation
Color Styles (proposed palette, named so a palette swap is one edit), Text Styles, breakpoints, grid, spacing. Stop.

## Phase 2 — Components
Every component in DESIGN.md with variants and states (hover, focus, open/closed, error), built only from Phase 1 styles. Keyboard-operable tabs and accordions; pause controls on marquee and carousels. Stop.

## Phase 3 — CMS
Collections: Reviews, Services, FAQs, Menu items, Client logos, Café hours. Seed with labelled placeholders. Stop.

## Phase 4 — Templates and pages
Home, then one service page (Weddings) as the template. Stop for review. Then Corporate, Celebrations, Quote, Menu, The Coffee Shop, About, FAQ, Privacy, 404. SEO title and description on every page from COPY.md. Stop.

## Phase 5 — Wiring
Nav dropdowns (desktop + mobile menu), quote form with success/error states (destination: [TBD — ask me]), redirects from SCOPE §A, structured data from SCOPE §B2, favicon/share image placeholders. Stop.

## Phase 6 — Self-check
Score the branch against SCOPE §D rubric at all breakpoints; list every item below 4 with a proposed fix. Do not fix without my go.

Start with Phase 0.
```

## Before you paste it
1. Repo on GitHub, cloned locally, Claude Code opened in that folder.
2. Framer project created on a plan that supports External Agents; `npx @framer/agent setup` run; `/framer` connected to the project.
3. Start Claude Code in plan mode for Phase 0.
