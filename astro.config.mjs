import { defineConfig } from 'astro/config';

// SITE_URL / BASE_PATH are set by the deploy workflow.
// Custom domain later: SITE_URL=https://yourdomain.com, BASE_PATH=/
export default defineConfig({
  site: process.env.SITE_URL || 'https://tori-mitchell.github.io',
  base: process.env.BASE_PATH || '/Breanna-Eric-Wedding',
  trailingSlash: 'always',
});
