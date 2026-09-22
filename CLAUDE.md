# CLAUDE.md — rules for agents on this repo

## Canon
- CONTEXT.md, COPY.md and DESIGN.md are canon. This repo is the single source of truth.
- Use copy from COPY.md verbatim. Use only DESIGN.md styles.
- If a word, fact or style is missing, stop and ask. Never invent facts, reviews, numbers, prices or client names.
- Anything tagged [confirm], [TBD — ask] or [UNVERIFIED] does not go on the live site until the owner confirms it.
- Log every locked decision in DECISIONS.md with a date.

## Order of change
1. Words → COPY.md. Look → DESIGN.md. Facts → CONTEXT.md.
2. Commit.
3. Then update Framer.

## Framer
- Project URL: [TBD]
- Work on a Framer branch. Never publish unless the user explicitly says "publish".
- Prefer native Framer layers, styles and components over code components.

## Reference sites
- nightowlcoffeecart.com is a STRUCTURAL reference only (funnel order, page types). Do not copy its copy, images, logos, reviews, stats or visual design.
- fellowshipcoffeetx.com is the client's current site. Its content belongs to Fellowship and may be carried over once the owner provides it.

## Process
Follow process/framer-three-file-website.md. Never skip a gate; if the user chooses to, log it in DECISIONS.md.
