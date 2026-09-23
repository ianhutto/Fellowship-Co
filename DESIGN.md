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

### Direction v2 (2026-09-23) — replaces the serif + mono proposal
Ian's review: v1 (Fraunces + JetBrains Mono on cream/brown, labels everywhere) read as AI-generated. v2 is bolder and photography-led.
- Type: **Bricolage Grotesque** (display, 700, large sizes, tight tracking) + **Figtree** (body). No monospace labels. Section cues are a short accent line ("01 — Weddings"), used sparingly. Verify both in Framer's font library.
- Palette (proposal until Fellowship's brand arrives): Espresso #1C1410 · Warm white #FAF6F0 · Line #E6D9C8 · Ink muted #4E3F34 · Accent terracotta #B5532C (on dark: #E08A5E).
- Scale: hero H1 132px desktop / 52px phone; section H2 96–112px; feature H3 60px; statement paragraph 56px. Big contrast between display and body.
- Layout: 12-column grid; feature blocks 7/5 split with large photos; one large review quote instead of a card row; closing CTA as an inset photo band; oversized wordmark in the footer.
- Brand codes: the terracotta full stop in the wordmark ("Fellowship.") and the numbered section cues. The stamp is retired. Supporting graphics (v6): the line icon set and one hand-drawn underline on the closing CTA.
- Mockup: design canvas "Fellowship Style Sample", Home desktop + phone v2.

### Component styling (v6, 2026-09-23 — replaces the v1 serif/mono table)
Every component on Night Owl's homepage has a Fellowship counterpart. The function and position are mirrored; the styling is Fellowship's own. Source of truth for the mockup: design/mockup/gen.py.
| Component | Treatment |
|---|---|
| Icons | Fellowship line set: 24 grid, 1.75 stroke, round caps and joins, currentColor. Phone, pin, clock, calendar, arrows, chevron, rings, briefcase, balloon, cup, storefront, tag, check, mail, shield, Instagram, Facebook, pause |
| Buttons | Pill. Primary = terracotta #B5532C, white text, trailing calendar icon ("Get a quote" everywhere, header included). Secondary = 1.5px outline, trailing arrow |
| Section cue | "01 — What we do": terracotta number + 28px terracotta rule + label in ink. Numbered 01–04 down the homepage (What we do, Why Fellowship, Kind words, Get in touch) |
| Utility bar | Espresso bar, 44px, 15px icons before hours, address, phone |
| Hero | Masked photo/video right of the headline, eyebrow with a terracotta dot separator, primary + outline-light buttons, "Pause" video control bottom right |
| Trust strip | Warm band #F3ECE2; label "Serving Houston since 2021 · As featured in [confirm]"; marquee of publication names in Bricolage, coffee-bean separators, faded edges, pause button. Real logos replace the text only with permission |
| Service cards (3) | Card #FFFDF9, 1px line #EADFD1, 16px radius; photo with a 52px round icon badge overlapping the bottom-left edge; label, H3 (balanced wrap), body, divider, text link with arrow |
| Photo chip | Pill on photos: cup icon tile plus a short fact ("Hot or iced · dairy-free milks") |
| Difference band | Inset dark photo band, 20px radius; H2 ends in the terracotta full stop |
| Stat tiles (3) | Cards with a 48px icon tile, label bottom-left, big Bricolage figure right; middle tile filled terracotta |
| Review summary | Espresso card, soft terracotta glow, shield badge, stars, VERIFIED, big rating, count and date |
| Review cards | Source line with stars, terracotta quote-mark graphic, quote, divider, initials avatar, name, event pill; prev/next round arrow buttons and pagination dots |
| Closing CTA | Blurred photo + espresso overlay + two warm glow blobs; hand-drawn terracotta underline under "guest list." (the only swash on the page); checkmark benefit row |
| Footer | Wordmark, tagline, primary button, round social icons; Services / Resources / Visit the café columns with icons; newsletter card with envelope icon; legal bar; oversized pale "Fellowship." wordmark cropped at the bottom |
| FAQ accordion | Simple rows, Bricolage question, + / × indicator |
| Form | Clean fields with labels, clear focus and error states; button "SEND MY REQUEST" |

### Motion
Fade-up on scroll (short distance), underline draw on links, tab image crossfade, marquee and carousel with pause controls. One easing curve. All off under reduced-motion.

### Palette (v1 — superseded by Direction v2)
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
