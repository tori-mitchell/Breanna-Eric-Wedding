import { defineConfig } from 'astro/config';

// Hosting is auto-detected:
//  - Cloudflare Pages sets CF_PAGES: served from the site root.
//  - Otherwise (GitHub Pages) the site lives under /Breanna-Eric-Wedding.
// SITE_URL / BASE_PATH override either (e.g. a custom domain: SITE_URL=https://example.com BASE_PATH=/).
const onCloudflare = Boolean(process.env.CF_PAGES);

export default defineConfig({
  site: process.env.SITE_URL || (onCloudflare ? process.env.CF_PAGES_URL : 'https://tori-mitchell.github.io'),
  base: process.env.BASE_PATH ?? (onCloudflare ? '/' : '/Breanna-Eric-Wedding'),
  trailingSlash: 'always',
});
