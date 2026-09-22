# Three-File Website — Framer edition

A repeatable 9-step process for designing and shipping a site in Framer. Adapted from a workflow Charlie Hills described publicly; the prompts here are our own.

## Core rules
1. No building in Framer until COPY.md is approved.
2. The site is built FROM the files. Word changes → COPY.md first; look changes → DESIGN.md first; then Framer.
3. Prefer native Framer layers, styles and components over code components, so the site stays editable on the canvas.
4. Never publish unless the user explicitly says "publish".

## Surfaces
- Steps 1–4: Claude Chat (strategy, interview, approval). Artifacts for style tiles.
- Steps 5–8: Claude Code connected to Framer + the Framer editor for review.
- DECISIONS.md logs every lock, with date.

## Framer connection (verify before each project)
Framer offers a native "External Agents" connection for Claude Code (framer.com/agents/external). As documented there:
1. Run Framer's install prompt in Claude Code (runs `npx @framer/agent setup`).
2. Run the `/framer` skill and grant project access in the browser.
3. Agent changes land on a Framer branch; review and merge in the editor.
This is new and may change — re-check that page for the current steps and plan requirements.

---

## Step 1 — CONTEXT.md (facts)
Interview in batches of 3–5 questions. Never invent; unknowns are `[TBD — ask]`. Cover entity, audience, offer, proof (verified only), positioning, constraints, sitemap with one conversion per page, and repeating content (→ Framer CMS). Gate: owner confirms every fact.

## Step 2 — COPY.md (every word)
Page by page: state the section's job; ask 1–2 questions; draft 3 options that differ in angle; user picks or rewrites. Every claim traces to CONTEXT.md.

## Step 3 — Approve every headline
One table: page | section | H1/H2 | sub | CTA. Mark ✅ / ✏️ until all ✅. Checks: headlines alone tell the story; no claim missing from CONTEXT.md; one CTA verb per page. Gate: "COPY locked — [date]" in DECISIONS.md.

## Step 4 — DESIGN.md (brand + five references)
Brand assets win conflicts. From five reference sites, extract principles (type scale, spacing rhythm, grid, color strategy, motion), not pixels. No cloning layouts, assets or recognizable designs. Write DESIGN.md to map 1:1 onto Framer: Color Styles, Text Styles, breakpoints, spacing, motion, components with variants, imagery rules, don'ts. Gate: "DESIGN locked — [date]".

## Step 5 — Build in Framer from all three files
Order: Color + Text Styles → breakpoints → components with variants → CMS collections → pages from COPY.md verbatim with SEO fields → gap list (missing words/styles/assets) instead of filling gaps. Review on the branch at all breakpoints.

## Step 6 — Production components (21st.dev → Framer)
21st.dev components are React/Tailwind for code projects. Preference: (1) rebuild the pattern natively in Framer, (2) licensed Framer Marketplace component, (3) port to a Framer code component — verify in Framer's docs how styling and imports work first. Check license and weight; no foreign colors, fonts or radii.

## Step 7 — Hero video (Higgsfield or similar)
Shot prompt from DESIGN.md imagery rules; confirm commercial-use terms; short compressed loop + poster frame; Framer Video component, muted autoplay loop; lighter version on Phone if needed. Skip if a still serves better.

## Step 8 — Iterate in natural language
One outcome per request. Words → COPY.md; look → DESIGN.md style, then the Framer style (not a one-off override). Canvas tweaks get written back to DESIGN.md.

## Step 9 — Taste pass before ship
Run by a fresh reviewer that didn't build the site.
- Copy: headlines tell the story; no filler; no claim absent from CONTEXT.md; camouflage test.
- Design: only DESIGN.md styles; consistent rhythm; nothing reads as a stock template.
- Craft: Desktop/Tablet/Phone; SEO titles/descriptions, OG image, favicon, 404; CMS pages; forms work; reduced motion; alt text, contrast, links; domain, redirects, analytics.
Ship: merge the Framer branch, publish only on explicit go, log "Shipped — [date]".
