import { defineConfig } from 'astro/config';

// Hosted on Cloudflare Pages only: always served from the site root.
// SITE_URL (full address, e.g. the custom domain) and BASE_PATH can still be set to override.
export default defineConfig({
  site: process.env.SITE_URL || process.env.CF_PAGES_URL || 'http://localhost:4321',
  base: process.env.BASE_PATH ?? '/',
  trailingSlash: 'always',
  // Clean, unhashed asset URLs: /assets/Base.css, /assets/<font>.woff2
  build: { assets: 'assets' },
  vite: {
    build: {
      rollupOptions: {
        output: {
          entryFileNames: 'assets/[name].js',
          chunkFileNames: 'assets/[name].js',
          assetFileNames: 'assets/[name][extname]',
        },
      },
    },
  },
});
