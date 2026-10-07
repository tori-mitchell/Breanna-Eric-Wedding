# Remaining items before launch

Last updated with the desktop-layout release. Detailed history lives in `CONTENT-TODO.md`; this is the short list.

## Needs your input (links, content)
- [ ] **RSVP link**: the "Let us Know" button on Home goes nowhere (`#`). Set it in `src/pages/index.astro` (and add the URL to `src/data/links.ts` next to the registry/gallery links).
- [ ] **Hourly schedules**: each day's schedule on Itinerary shows "Details coming soon". The dummy rows are in `src/data/daily.ts`; set `showDailyRows = true` after replacing them with real times.
- [ ] **Transfers and train times**: "Recommended train options and exact pickup times" (The Journey) and the Thursday transfer details, once the 2027 rail schedule is out.
- [ ] **Dress code / attire** and any other "details to come" wording (Itinerary summary rows, FAQ).
- [ ] **Backup contact info** for missed transfers / delays (FAQ, The Journey).
- [ ] **Joy lodging and RSVP flow**: confirm the "shared privately through Joy" wording is accurate.
- [ ] Confirm the **venue gallery link** (`https://www.laticastelli.com/en/gallery`) opens correctly.

## Images
- [ ] **Placeholders (magenta) to replace**, 4 in total:
  - Accommodations: "Your Stay" (vertical), "Life at the Borgo" (horizontal), "Cars & Parking" (horizontal)
  - Itinerary: the one under the summary schedule / FAQ line (vertical)
- [ ] Not yet placed: the "BE wine bottle" graphic beyond the nav/favicon, the second terrace watercolor, the full-width border strips.
- [ ] Optional: a **social share image** (link previews) and a hi-res favicon check.
- Official venue photos are intentionally not used; the site links to the venue gallery instead.

## Site / hosting
- Done: custom domain is connected on Cloudflare Pages.
- Decided: no branch protection needed; the dev -> prod workflow in `AGENTS.md` is the guard rail (rollback is always available via GitHub revert or Cloudflare Deployments).
- Search indexing: the site is `noindex, nofollow` with a `robots.txt` disallow. Not a priority; leave as is unless it matters later.
- Decided: Cloudflare only. The GitHub Pages workflow was removed; turn Pages off in the repo's GitHub Settings -> Pages if it's still enabled.

## Polish ideas (optional)
- [ ] Re-check the 1024-1200px desktop range (two-column layouts with the hamburger nav).
- [ ] Phone quirk left on purpose: the Home ceremony painting overhangs its box on phones (fixed on desktop only); ask before changing.
- [ ] Real photo permissions/credits if any Our Story photos come from others.
- [ ] Final read-through of all copy on phone and desktop.
