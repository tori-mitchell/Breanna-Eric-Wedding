# Content & Asset TODO

Tracks everything that is a placeholder, cropped from a Canva screenshot, or needs verification before launch.

**Magenta outline = temporary screenshot crop.** Crops live in `public/images/placeholders/`; any image served from that folder gets the outline automatically. To replace one: drop the real file in `public/images/`, point the page's `src` at it, and the outline disappears. To hide all outlines at once, set `--temp-outline: none` in `src/styles/tokens.css`.

Venue photos (§2) are intentionally *not* committed (public repo, permission pending) and still show as text placeholders. Banner flourishes, footer hills strip, and all watercolors are screenshot crops too (§3). The olive/hydrangea sprigs are not included yet.

Legend: **[SS]** = cropped from screenshot (low-res, replace) · **[PH]** = placeholder · **[LIC]** = license/permission needed

---

## 1. Photos (personal) — need originals

| Page | Section | Description | Status |
|---|---|---|---|
| Our Story | Welcome | Couple on hiking trail, waterfall valley (Hawaii?) | [SS] |
| Our Story | Ch. 1 How We Met | Hockey arena selfie (red seats) | [SS] |
| Our Story | Ch. 1 | Selfie in front of red/gold Christmas tree | [SS] |
| Our Story | Ch. 1 | Couple at vineyard, sunset, wine glass | [SS] |
| Our Story | Ch. 1 (above) | Hurricanes parade, downtown street | [SS] |
| Our Story | Ch. 2 Life Together | Couple + dog at front door (Mets shirt) | [SS] |
| Our Story | Ch. 2 | Strawberry field | [SS] |
| Our Story | Ch. 2 thumbs | Group at brewery/bar (green shirts) | [SS] |
| Our Story | Ch. 2 thumbs | Couple + dog at giant wooden troll sculpture | [SS] |
| Our Story | Ch. 2 thumbs | Hockey game group selfie (Canes jerseys) | [SS] |
| Our Story | Ch. 3 Engagement | Proposal under floral arch | [SS] |
| Our Story | Ch. 3 | Reaction close-up (hand over mouth) | [SS] |
| Our Story | Ch. 3 | Group photo with family/friends at fence | [SS] |
| Our Story | Ch. 4 And Now, Tuscany | Couple on porch (rust dress, grey suit) | [SS] |
| Home | You're invited! | Couple kissing, holding hands w/ ring (portrait) | [SS] |

## 2. Venue photos (Borgo Laticastelli) — need originals + permission [LIC]

| Page | Section | Description | Status |
|---|---|---|---|
| Lodging | Below intro | Full-bleed terrace dining at sunset | [SS] |
| Lodging | Gallery | Aerial pool + hillside | [SS] |
| Lodging | Gallery | Stone doorway w/ topiaries (**photographer watermark visible**) | [SS] [LIC] |
| Lodging | Gallery | Bedroom w/ open window, robes on bed | [SS] |
| Lodging | Gallery | Terrace w/ red cushions & wicker chairs | [SS] |
| Lodging | Gallery | Balcony window, cypress view | [SS] |
| Lodging | Gallery | Brick-vaulted cellar restaurant | [SS] |
| Home | This is where our forever begins | Cobblestone borgo lane (**likely venue photo — permission**) | [SS] [LIC] |

## 3. Illustrations & decorative art — source/license unknown [LIC]

Confirm for each: Canva library element (can't be extracted) vs. your own upload/AI-generated (OK to use).

| Asset | Used on | Plan if not licensable |
|---|---|---|
| Home hero watercolor (Tuscan hills + villa) | Home | [SS] for now |
| Page-title banner (arches + vines, L & R) | All inner pages | [SS] for now |
| Footer hills strip | All pages | [SS] for now |
| Travel: illustrated route map | Travel | [SS] |
| Explore: Florence | Explore | [SS] |
| Explore: Dolomites | Explore | [SS] |
| Explore: Sorrento | Explore | [SS] |
| Hand-sketched double photo frame | Our Story | Redraw as SVG (no license needed) |
| Olive branch sprigs (RSVP/Registry on Home; also Our Story) | Home, Our Story | [SS] crops on Home; Our Story still [PH] — redraw or license |
| Hydrangea sprig | Our Story | [PH] — redraw or license |

## 4. Copy to verify

| Page | Item | Note |
|---|---|---|
| Travel | "Piza" heading | Typo → **Pisa** (fixing) |
| Travel | "BeforeYou Go" | Missing space → **Before You Go** (fixing) |
| Travel | Step 02 side rules | Only step with borders — keep, extend to all, or remove? |
| Lodging | "Getting Here and Having a Car" | Para 1 duplicates "Life at the Borgo" verbatim; para 2 repeats "no car needed" |
| Lodging / Travel | "Rental Cars" (Travel) vs. "Having a Car" (Lodging) | Overlapping content — keep both? |
| All | Dates | Thu Sep 16 – Sun Sep 19, 2027 (weekdays verified correct) |
| Lodging / Travel | Check-in 3:00 PM Thu, checkout 12:00 PM Sun | Verify with venue |
| Travel | Train routes (Florence→Siena→Rapolano Terme; Rome→Chiusi-Chianciano→Rapolano Terme; Pisa Centrale) | Verify |
| Lodging | Planner name "Ani" | Verify spelling; full name/contact to add? |
| Lodging | "shared privately through Joy" | Need Joy URL for RSVP link |
| Explore | Suggested stays (Florence 2–3, Dolomites 3–4 Ortisei/Val Gardena, Sorrento 3–4) | Verify |
| Our Story | Ch. 3 "Game 5 of the Hurricanes–Canadiens series", May 29 | Verify |
| Before You Go | "We'll link to the latest official guidance" | Links TBD |
| Delays | "backup contact information" | TBD closer to date |

### Home page: copy and links to verify
- "The borgo  will be reserved…" had a double space in Canva (fixed to one).
- "Dating back to the 12th century… Crete Senesi… name is said to mean 'the castle where light comes from all sides'" — verify claim.
- **"Let us Know" button** (RSVP): destination unknown — currently `#`. Mailto, form, or Joy link?
- **"View our Registry" button**: registry URL needed — currently `#`.
- "formal RSVP details will be shared with the invitation" vs Lodging page "RSVP … through Joy" — reconcile wording.
- Nav is sticky with a glass (blur) background on every page; footer is a normal end-of-page footer.

### Itinerary / FAQ (new)
- Weekend page is now **Itinerary** (`/itinerary/`): compact day-by-day rows, no watercolors (the four Weekend art crops were removed). Content: `src/data/itinerary.ts`.
- **Event times are not final** — rows show day/date only. Add a `time` to each item when known.
- New **FAQ** page (`/faq/`), content in `src/data/faq.ts`. Answers are drawn only from existing site copy; please review each, and say what's missing (kids/plus-ones, dress code, shuttle times, etc. were not on the site so weren't invented).
- **Travel is the comprehensive source for travel info; the FAQ is a quick reference** that may repeat it and link back. Don't trim Travel to match the FAQ.

## 5. Decisions made (best guess — confirm later)

| Decision | Choice | Confirm? |
|---|---|---|
| Hosting | GitHub Pages, **public repo** (source + git history are public) | ⚠️ Don't commit venue photos until permission is confirmed (§2). |
| Domain | Default `*.github.io` URL now; custom domain later | Add domain when purchased (CNAME + DNS) |
| Search indexing | Blocked (`noindex` meta + `robots.txt` disallow) | — |
| Body text weight | Regular everywhere (Canva mixed regular/semibold) | Yes |
| Justified text | Replaced with left/right alignment matching section | Yes |
| Text styles | Five: script hero, script header, subhead, eyebrow (sans caps, light blue — chapters, labels, dates), body (also nav/footer/small text; italic = `<em>` on body) | Yes — eyebrow contrast is ~2.4:1 (below WCAG AA 4.5:1); consider a darker `--color-label` |
| Typos | "Piza"→"Pisa", "BeforeYou"→"Before You" fixed | — |
| Lodging duplicate paragraph | Kept as-is for now (see §4) | Yes |
| Travel step dividers | Thin rules between all 3 steps | Yes |
| Buttons | Square corners, solid accent fill, eyebrow-style label in page color (no pill, ring, or arrow) | Yes |
| Body text alignment | Left-aligned everywhere except hero, title bars, and travel step cards; body letter-spacing 0.01em (Canva's was wider) | Yes |
| Fonts | Pinyon Script (script) + EB Garamond (serif), self-hosted | Verify against Canva font names |
| Nav active state | Correct page highlighted (Canva's was wrong on most pages) | — |
| Nav (mobile) | Two rows (3 + 4 items now that FAQ exists), no hamburger | Yes |
| Footer | Hills strip + "B & E · 09.2027" (Canva footer removed) | Yes — wording |
| Motion | Subtle fade-in on scroll; disabled for reduced-motion users | Yes |
| Layout priority | Mobile first; desktop pass later | — |

## 6. Pending features

- [ ] RSVP — link to Joy (URL needed)
- [ ] Custom domain (if any)
- [ ] Social share image + favicon (monogram?)
- [ ] Desktop layout (mobile-first now)
