# DESIGN.md — Fellowship Coffee Co.

Status: v0.2 — proposal + measured spacing. Palette and logo pending Fellowship brand assets. Restraint pass applied 2026-09-22 (red team).

Needed before drafting:
- Logo files (SVG preferred) → assets/logo/
- Brand colors (hex codes) and fonts — or full-page screenshots of the current site → assets/screenshots/
- Photos and any video of the cart and café → assets/photos/, assets/video/
- Up to five reference sites the owner loves, and the one thing loved about each (nightowlcoffeecart.com already noted as a structural reference only)

## Design method (agreed 2026-09-22)
Goal: Night Owl's architecture at Night Owl's level of polish, unmistakably Fellowship.
1. Architecture mirrored per SCOPE.md §A.
2. Vertical rhythm MATCHES Night Owl (revised 2026-09-22 at Ian's call): measured — see Spacing below. Everything else is principles only: big editorial headlines against small caps eyebrows; full-bleed photo/video; restrained palette with one accent; subtle, smooth motion. Type, fonts, component styling, colors and motion values are Fellowship's own.
3. Four more references chosen for Fellowship's character (warm, community, faith-rooted, Filipino-inspired drinks). Each: the one principle borrowed. [owner/Ian to pick, or Provider proposes]
4. Fellowship tokens (below) each chosen to deliver a principle from step 2.
5. Parity review: side by side with Night Owl on polish, breathing room, type contrast and motion quality. Gaps fixed with Fellowship tokens only.
6. Literal match only with written permission from Night Owl or their credited studio (Aria Creative), stored in this repo.

## Proposed brand system v0.1 — type + components (for review)
Status: PROPOSAL. Fellowship's existing logo, colors and fonts override anything here once received.

### Brand idea
**"Pull up a chair."** Fellowship's name and story are about people gathering over coffee. Night Owl's look signals premium event production; Fellowship's signals warmth and hospitality. Every type and component choice below should feel like a well-run neighborhood café: crafted, warm, a little playful, never corporate.

### Brand codes (restraint: two only)
1. **The stamp:** a static round seal ("EST. 2021 · MISSOURI CITY, TX"). Footer and Quote page only. No rotation.
2. **Mono labels:** small uppercase monospace for eyebrows, card labels and stat labels. This is the main recurring code.
Dotted leaders appear on /menu only. Everything else stays quiet so the photography carries the premium feel.
Removed in the restraint pass: cup-ring texture, torn/perforated ticket edges, polaroid rotation, handwritten review cards, order-slip form styling, steam-rise hover, seal-style proof strip, menu-board FAQ.

### Type treatment
| Role | Proposal | Notes |
|---|---|---|
| Display / H1–H2 | **Fraunces** (Google Fonts), large optical size, soft axis 0, weight 400, tight leading, sentence case | Crisp editorial serif, not "cosy indie" |
| Body | **Instrument Sans** (Google Fonts) | |
| Labels | **JetBrains Mono** (Google Fonts), 12–13px, uppercase, tracking 0.16–0.18em | Check contrast at small size (≥4.5:1) |
| Accent | Italic Fraunces for one phrase in H1s only | H2/H3 stay roman |
Verify each font is available in Framer's font library before locking.

### Component styling
| Component | Treatment |
|---|---|
| Buttons | Pill; primary filled accent, white text; secondary text with underline that draws on hover; visible focus ring |
| Eyebrow | Mono label with a small accent dot |
| Feature blocks | Large photo, gently rounded corners, alternating sides |
| Benefit cards (3) | Clean card on paper tone, mono label, serif title, short body; no per-card CTA |
| Numbered tabs (4) | Tab list with serif numerals "No. 01–04"; selecting a tab swaps its image and line |
| Stat tiles | Big serif figure, mono label beneath; no receipt styling |
| Review cards | Plain card, stars, quote in body type, name + event in mono |
| Trust strip | Plain logo row or linked text line; no seals; marquee has a pause control |
| FAQ accordion | Simple rows, serif question, + / × indicator |
| Gallery (café, about) | Clean grid, no rotation |
| CTA band | Full-bleed photo, dark overlay, large serif line, button |
| Form | Clean fields with labels, clear focus and error states; button "SEND MY REQUEST" |
| Footer | Café address and hours, stamp, social, newsletter |

### Motion
Fade-up on scroll (short distance), underline draw on links, tab image crossfade, marquee and carousel with pause controls. One easing curve. All off under reduced-motion.

### Palette
Pending Fellowship's brand colors. If none exist, the proposal is a warm neutral base (cream / espresso brown) plus one accent from their signature drinks (ube purple or pandan green), for the owner to choose. No colors are locked until reviewed.

Template (to be filled in Step 4 — maps 1:1 onto Framer):
## Brand anchors (non-negotiable)
## References → principle borrowed
## Color styles (light + dark)
## Text styles (per breakpoint)
## Breakpoints
## Spacing — vertical rhythm (measured 2026-09-22)
Source: nightowlcoffeecart.com/services/mobile-activations-national-tours, computed styles, vertical spacing only.
Measured at 2559px and 991px (identical, so Desktop 1440 uses the same), 767px and 390px.

Scale: 16 · 24 · 32 · 40 · 48 · 80 · 96 · 160

| Token | Desktop (≥992) | Tablet (480–991) | Phone (≤479) | Used for |
|---|---|---|---|---|
| section-y | 80 | 80 | 40 | Standard section padding, top and bottom |
| section-y-lg | 96 | 96 | 40 | Closing CTA band |
| strip-y | 48 | 48 | 48 | Trust strip padding |
| hero-top | 80 | 80 | 160 | Hero top padding (phone value clears the fixed nav) |
| hero-bottom | 48 | 48 | 48 | Hero bottom padding |
| footer-top | 48 | 48 | 48 | Footer top padding |
| stack-gap | 16 | 16 | 16 | Eyebrow → heading → body → CTA |
| card-gap | 24 | 24 | 24 | Gap between cards in a row or grid |
| footer-col-gap | 96 | 96 | 32 | Gap between footer columns |

Note: at 767px most sections still used the tablet values (80); only the full-width image block had dropped to 40. At 390px everything used the phone values. So tablet values run down to 480 and phone values apply at 479 and below. Widths between 480 and 767 were only measured at 767. Framer breakpoints to set: Desktop 1440, Tablet 810, Phone 390.
Horizontal spacing, type, component styling, colors and motion are Fellowship's own (not measured).
## Radius / shadow / effects
## Motion
## Components (with variants)
## Imagery + video rules
Real Fellowship photography only. G4 cannot pass on placeholders.

Specs
- Hero video: 8–12 s seamless loop, 1080p, H.264 MP4 + WebM, ≤3 MB desktop / ≤1 MB phone version, muted, no text in frame, poster frame supplied
- Stills: min 2400 px on the long edge; export WebP/AVIF via Framer
- Ratios: hero 16:9 desktop / 4:5 phone · feature blocks 4:5 · full-width 21:9 · numbered-tab images 4:5 · benefit/review cards 1:1 · gallery 1:1 or 4:5
- Alt text on every image: what's in the shot, no keyword stuffing

Shot list for the owner (priority order)
1. The cart set up at a real event, wide, with guests (hero)
2. Barista pulling a shot / pouring latte art, close
3. Guests holding drinks, candid, at a wedding
4. Same at an office event
5. Same at a shower or birthday, including the cocoa bar with kids (with parents' permission)
6. Signature drinks styled on a plain surface (ube, biko, lavender)
7. The café interior and counter, pastries
8. Ryan and Janice together, natural light
9. Detail shots: cups, menu board, cart hardware
10. A short phone video walk-up to the cart for the hero loop

## Don'ts
