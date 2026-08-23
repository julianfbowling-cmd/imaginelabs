// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import { SITE } from './src/config.js';

export default defineConfig({
  // TODO: cambiar por el dominio real cuando esté definido (también en src/config.js)
  site: SITE.url,
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
