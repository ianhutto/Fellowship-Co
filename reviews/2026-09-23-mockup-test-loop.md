# Homepage mockup test loop — 2026-09-23

Method: render the mockup headless (Chromium, real fonts) at 1440 and 390 → compare with nightowlcoffeecart.com live (structure, containment, spacing, quality bar only) → independent reviewer scores against SCOPE §D → fix → repeat.

| Round | Change | Finding |
|---|---|---|
| r1 | v3 baseline | Layout drifted from Night Owl: full-bleed instead of ~1200px container; alternating blocks instead of 3-card row; no text+image intro; big empty footer gap |
| r2–r3 | v4 rebuild to Night Owl's structure, Fellowship styling | Reviewer: 3–4/5 across the board; orphans, stat labels backwards, price slot broken, accent overused, uneven padding |
| r4–r5 | Merged intro + cards; stats relabelled with price chip; accent limited to CTAs; card padding unified; balanced wrapping; darker phone scrim | Reviewer: type 5, restraint 5, most others 4; distinctiveness 3 |
| r6–r8 | Hero text clears the image; phone price "$"; review arrows stacked; CTA reply-time line [owner to confirm] | Hero readable; phone review header fits |

Final scores (r5 reviewer, before r6–r8 fixes): First 5s 4 · Type 5 · Spacing 4 · Restraint 5 · Distinctiveness 3 · Architecture 4 · Craft 4 · Mobile 4 · Conversion 4.

Disagreement noted: reviewer (text-only read) thought Night Owl's Difference section is open; live visual check shows an inset dark photo band. Kept the band.

Open: distinctiveness (needs real photography and one ownable brand moment); rubric item 2 (photography) cannot pass on placeholders.
| r9–r10 | v5: real Unsplash photography in all 7 image slots (see assets/PLACEHOLDERS.md); hero photo masked to the right of the headline; closing CTA photo blurred + 0.62 overlay so another café's signage is unreadable | Photography gap closed for mockup purposes; rubric item 2 still needs Fellowship's own photos |
| r11–r12 | v6: every Night Owl homepage component rebuilt in Fellowship styling. Adds the line icon set, icon badges on cards, stat tiles with icons, review summary and cards (stars, quote graphic, avatar, event pill), marquee with pause, CTA glow and check row, newsletter card, and the giant footer wordmark | Reviewer: parity 8 present / 3 partial; architecture 4.5, distinctiveness 3.5, craft 3 |
| r13 | Reviewer fixes: price tile shows [$X] on terracotta (dashed chip removed); swash only on "guest list."; band H2 ends in the terracotta full stop; decorative arcs removed; card titles balanced; marquee lists publications only; CTA text contrast raised; "03 — Kind words" cue added (COPY eyebrow), CTA renumbered 04; header CTA terracotta; footer wordmarks refit | Declined: "[N]+ events served" stat (not in COPY; third tile stays "2024 café opened" until a rating source is chosen) |
| r14–r16 | v7: rebuilt on Fellowship's real brand (logo, black/white/stone, Inter Tight + Montserrat, square buttons) with their own cart photos; COPY.md card lines restored verbatim | Reviewer: first 5s 3, brand fidelity 3, parity 4.5, overall 3 (hero crop, grey overlays, weight 600 type) |
| r17–r19 | Whole cart with wheels in hero, black gradient; phone hero stacked; 400px card photos; stat tiles restacked; weight 500; static trust strip; neutral overlays | Reviewer: first 5s 4.5, brand 3.5, type 4, photo 4, mobile 4, overall 4 |
| r20 | Desktop closing CTA dark + glow (Night Owl structure); hero gradient for contrast; stray wordmark crops fixed; trust strip in Montserrat caps; tile spacing; phone tiles stacked; phone footer wordmark edge to edge | Not yet re-scored |

Renders: reviews/renders/home-desktop-v4.png, home-phone-v4.png, home-desktop-v5.png, home-phone-v5.png, home-desktop-v6.png, home-phone-v6.png, home-desktop-v7.png, home-phone-v7.png
