-- Tabla de leads del formulario de AlquimIA.
-- Ejecutar en Supabase: Dashboard → SQL Editor → pegar y Run.

create table public.leads (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  nombre text not null check (char_length(nombre) between 1 and 200),
  correo text not null check (char_length(correo) between 3 and 320),
  whatsapp text check (whatsapp is null or char_length(whatsapp) <= 40),
  empresa text check (empresa is null or char_length(empresa) <= 200),
  mensaje text not null check (char_length(mensaje) between 1 and 5000),
  pagina text check (pagina is null or char_length(pagina) <= 200),
  origen text not null default 'web' check (char_length(origen) <= 40)
);

-- Seguridad: la clave pública (anon) SOLO puede insertar. Sin política de
-- SELECT/UPDATE/DELETE, nadie puede leer ni tocar los leads desde el
-- navegador; tú los ves en el Dashboard (Table Editor) o con la service key.
alter table public.leads enable row level security;

create policy "el formulario web puede insertar leads"
  on public.leads
  for insert
  to anon
  with check (true);
