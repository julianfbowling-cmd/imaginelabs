# AlquimIA

Sitio web de AlquimIA, identidad **Azul profundo**.
Stack: [Astro](https://astro.build) + Tailwind CSS 4, desplegable en Vercel o Cloudflare Pages.

## Comandos

```bash
npm run dev      # servidor de desarrollo en http://localhost:4321
npm run build    # build de producción en dist/
npm run preview  # sirve el build localmente
```

## Al definir la marca

Todo lo pendiente está centralizado:

1. **`src/config.js`** — nombre, dominio, correo, WhatsApp, ciudad y textos de servicios.
2. **`public/robots.txt`** — URL del sitemap con el dominio real.
3. **`.env`** — copiar `.env.example`. El formulario usa el primer backend configurado:
   webhook de n8n (`PUBLIC_N8N_WEBHOOK_URL`, prioridad), **Supabase**
   (`PUBLIC_SUPABASE_URL` + `PUBLIC_SUPABASE_ANON_KEY`, tabla creada con
   `supabase/leads.sql`) o Web3Forms (`PUBLIC_WEB3FORMS_KEY`). Sin ninguno,
   el formulario avisa que no está conectado.

## Diseño

El diseño aprobado (home, paleta, psicología del color y direcciones exploradas) vive en el
lienzo "Identidad Web 2027" en claude.ai/code/artifacts. Paleta principal: fondo `#0A1236`,
azul real `#142878`, azul acción `#2440D6`, cian CTA `#6FE3F4`, perivinca `#8F8DF8`,
superficie `#F5F7FE`. Tipografías: Sora (display), Manrope (texto), JetBrains Mono (etiquetas).

## Próximas páginas

La estrategia (ver informe "Radiografía Quantum DS") es hub & spoke: `/servicios/` como hub +
una página por servicio + blog. El layout `src/layouts/Base.astro` ya trae SEO, JSON-LD y
canonical por página.
