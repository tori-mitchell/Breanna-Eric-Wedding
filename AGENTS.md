# Working agreement (humans and AI agents)

Public wedding site for Breanna & Eric: Astro, plain CSS tokens, deployed on Cloudflare Pages only (the old GitHub Pages workflow was removed).

## Branches and releasing — READ FIRST
- **`dev`** is where all work happens. Commit and push to `dev` first.
- Cloudflare builds every non-`master` branch as a **preview** (e.g. `dev.<project>.pages.dev`). **Verify there** — on a phone-width screen and a desktop screen — before anything goes live.
- **`master`** is production. **Never push or merge to `master` unless the owner has explicitly said to ("push to prod").** Approval for one release does not carry over to the next.
- To release: merge `dev` into `master` (no force-push, no rewriting history), then confirm the production build is green.
- If something breaks in prod: revert the bad commit(s) on `master` (`git revert <sha>`, or the GitHub UI's **Revert** button on the merged PR), push, and fix forward on `dev`. You can also roll back instantly in Cloudflare (Workers & Pages -> project -> Deployments -> pick the last good one -> Rollback).
- Don't create PRs unless asked. Keep commits small and described in plain language.

## Before every push
1. `python3 scripts/audit-grid.py` must print `0 non-compliant` (spacing/size values must sit on the grid, or carry a `grid-exempt` comment with the reason).
2. `npm run build` must succeed.
3. Look at the result at ~393px wide (phone) and ~1440px wide (desktop). Phones are the default experience.

## Design rules (the owner is very particular — follow them)
- **Tokens first.** All colors, type, spacing and widths live in `src/styles/tokens.css`. Reuse an existing token; ask before inventing a new one. Key ones: `--block` (gap between sections: 48px phone / 72px desktop), `--flow` (16px between text), `--col-gap` (24px, every two-column layout), `--column` (552px single col), `--column-wide` (824px, two 400px cols), `--gutter-wide` (56px side padding from 600px up).
- **Grid:** spacing and container sizes are multiples of 8 (of 4 below 24px). Type sizes and leading are exempt.
- **Phones vs desktop:** desktop work (>= 1024px; nav row >= 1200px) must not change the phone layout. Verify phone page heights are unchanged when you touch shared components.
- **Style:** old-money luxury minimalism with a touch of whimsy. No right-aligned text. Script fonts are for page titles, chapter titles and step titles only. Eyebrows are small tracked caps above headings. Text links use the shared `.more` class.
- **Images:** official art lives in `public/images/art`, personal photos in `public/images/story`. Photos get soft watercolor-edge masks (`scripts/gen-photo-masks.py`) and washes in the palette colors (blue `--color-accent`, `--color-sage`, `--color-peach`). Placeholders render magenta. Never use official venue photos on the site; link to the venue gallery instead.
- **Content:** don't invent facts (times, names, links). Use clearly-labelled placeholders. The FAQ is self-contained and never redirects to another page. Track open items in `docs/CONTENT-TODO.md`.
- Mobile-first, no accessibility fussing beyond sensible defaults, noindex stays on.

## Handy
- Dev server: `npm run dev`; production build check: `npm run build` then `npx astro preview`.
- The site is served from the root (`/`) everywhere, locally too (`http://localhost:4321/`).
