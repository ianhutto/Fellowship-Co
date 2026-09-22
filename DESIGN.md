# DESIGN.md — Fellowship Coffee Co.

Status: NOT STARTED — blocked on brand assets from the owner.

Needed before drafting:
- Logo files (SVG preferred) → assets/logo/
- Brand colors (hex codes) and fonts — or full-page screenshots of the current site → assets/screenshots/
- Photos and any video of the cart and café → assets/photos/, assets/video/
- Up to five reference sites the owner loves, and the one thing loved about each (nightowlcoffeecart.com already noted as a structural reference only)

## Design method (agreed 2026-09-22)
Goal: Night Owl's architecture at Night Owl's level of polish, unmistakably Fellowship.
1. Architecture mirrored per SCOPE.md §3.
2. Vertical rhythm MATCHES Night Owl (revised 2026-09-22 at Ian's call): section padding, heading → body → CTA gaps, card/grid gaps, and their scaling per breakpoint — measured from their live pages, not guessed. Everything else is principles only: big editorial headlines against small caps eyebrows; full-bleed photo/video; restrained palette with one accent; subtle, smooth motion. Type, fonts, component styling, colors and motion values are Fellowship's own.
3. Four more references chosen for Fellowship's character (warm, community, faith-rooted, Filipino-inspired drinks). Each: the one principle borrowed. [owner/Ian to pick, or Provider proposes]
4. Fellowship tokens (below) each chosen to deliver a principle from step 2.
5. Parity review: side by side with Night Owl on polish, breathing room, type contrast and motion quality. Gaps fixed with Fellowship tokens only.
6. Literal match only with written permission from Night Owl or their credited studio (Aria Creative), stored in this repo.

## Proposed brand system v0.1 — type + components (for review)
Status: PROPOSAL. Fellowship's existing logo, colors and fonts override anything here once received.

### Brand idea
**"Pull up a chair."** Fellowship's name and story are about people gathering over coffee. Night Owl's look signals premium event production; Fellowship's signals warmth and hospitality. Every type and component choice below should feel like a well-run neighborhood café: crafted, warm, a little playful, never corporate.

### Brand codes (repeat everywhere so the site is recognisably Fellowship)
1. **The order ticket:** cards styled like café order slips: thin rule borders, a perforated or dashed edge, small monospaced labels (ORDER · FOR · QTY), a torn-edge option for accents.
2. **The stamp:** a round badge mark (e.g. "EST. 2021 · MISSOURI CITY, TX") used as a seal on hero, footer and quote page. Rotates slowly on scroll.
3. **The cup ring:** a faint coffee-ring mark as a background texture behind section headers. Used sparingly, never behind body text.
4. **The chalk menu:** menu and pricing set like a café menu board, with dotted leaders between item and detail.

### Type treatment
| Role | Proposal | Why |
|---|---|---|
| Display / H1–H2 | **Fraunces** (Google Fonts, variable serif), set large, soft axis up, tight leading, sentence case | Warm and crafted. Signals café and hospitality, not event agency. |
| Body | **Instrument Sans** (Google Fonts) | Clean and legible; lets the serif carry the personality |
| Labels / eyebrows / tickets | **a monospace** (e.g. JetBrains Mono or IBM Plex Mono, Google Fonts), small, uppercase, wide tracking | Order-ticket and receipt feel. It replaces the generic small-caps eyebrow with a Fellowship code. |
| Accent | **Italic Fraunces** for one word per headline ("Your event, with a coffee shop *in the room*.") | A signature move people will remember |
Verify each font is available in Framer's font library before locking.

### Component styling
| Component | Fellowship treatment |
|---|---|
| Buttons | Pill shape; primary filled in the brand accent; hover: a small steam-rise micro-animation (arrow nudges up); secondary: text + underline that draws on hover |
| Eyebrow | Monospace label inside a thin ticket outline, with a small dot bullet: `● WEDDINGS` |
| Feature blocks | Photos with a slightly rounded crop and a stamped caption tag in the corner; alternating sides per the SCOPE §3 layout |
| Service cards (3-col) | Order-ticket cards: dashed top edge, mono label, serif title, short body, arrow link |
| Numbered cards (4) | Large serif numerals set like menu numbers ("No. 01"), not generic circles |
| Stat tiles | Receipt style: mono label, big serif figure, dotted leader line |
| Review cards | Handwritten-note feel: off-white card, serif italic quote, small stamp with star rating, name in mono |
| Logo / proof strip | Stamp-row treatment: proof items in circular seals instead of a flat logo marquee |
| FAQ accordion | Menu-board rows: question in serif, dotted leader, + turns to × |
| Gallery (4) | Polaroid-adjacent: thin white border, slight alternating rotation on desktop (0 on mobile) |
| CTA band | Full-bleed photo, dark overlay, large serif line, the stamp seal rotating beside the button |
| Form | Styled as an order slip: numbered fields, mono labels, dashed dividers; submit button "Send my order" [confirm copy] |
| Footer | Café sign-off: address and hours set like a shop window decal, stamp seal, social |

### Motion
Warm, not flashy: fade-up on scroll (short distance), the stamp rotating slowly, underline draws, a steam-rise on button hover. One easing curve for everything. All of it off under reduced-motion.

### Palette
Pending Fellowship's brand colors. If none exist, the proposal is a warm neutral base (cream / espresso brown) plus one accent from their signature drinks (ube purple or pandan green), for the owner to choose. No colors are locked until reviewed.

Template (to be filled in Step 4 — maps 1:1 onto Framer):
## Brand anchors (non-negotiable)
## References → principle borrowed
## Color styles (light + dark)
## Text styles (per breakpoint)
## Breakpoints
## Spacing
(Measured from nightowlcoffeecart.com at Desktop / Tablet / Phone — values pending measurement)
## Radius / shadow / effects
## Motion
## Components (with variants)
## Imagery + video rules
## Don'ts
