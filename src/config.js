// Datos centrales de la marca. Todo lo que está entre corchetes es un
// marcador pendiente: al definir nombre, dominio y contacto se cambia aquí
// una sola vez y se propaga a todo el sitio (SEO incluido).
export const SITE = {
  brand: 'ImagineLabs',
  // TODO: dominio real (usado por sitemap, canonical y JSON-LD)
  url: 'https://www.tudominio.com',
  email: 'hola@tudominio.com',
  whatsapp: '', // formato internacional sin signos, p. ej. '573001234567'
  city: '[Ciudad], Colombia',
  description:
    'Sitios web, agentes de IA y automatizaciones que capturan clientes, responden en segundos y liberan a tu equipo del trabajo repetitivo.',
  titleDefault: 'Web, IA y Automatización para Empresas',
};

export const NAV_LINKS = [
  { label: 'Servicios', href: '/#servicios' },
  { label: 'Proceso', href: '/#proceso' },
  { label: 'Por qué nosotros', href: '/#por-que' },
  { label: 'Contacto', href: '#contacto' },
];

// Tecnologías con logo (en /public/logos/). Cada página de servicio muestra
// las suyas con el componente TechStrip.
export const TECH = {
  n8n: { name: 'n8n', logo: '/logos/n8n.svg', wordmark: true, imgClass: 'h-8 w-auto' },
  claude: { name: 'Claude', logo: '/logos/claude.svg' },
  python: { name: 'Python', logo: '/logos/python.svg' },
  fastapi: { name: 'FastAPI', logo: '/logos/fastapi.svg' },
  react: { name: 'React', logo: '/logos/react.svg' },
  angular: { name: 'Angular', logo: '/logos/angular.svg' },
  aws: { name: 'AWS', logo: '/logos/aws.svg', wordmark: true, imgClass: 'h-8 w-auto' },
  azure: { name: 'Azure', logo: '/logos/azure.svg' },
  shopify: { name: 'Shopify', logo: '/logos/shopify.svg' },
  woocommerce: { name: 'WooCommerce', logo: '/logos/woocommerce.svg', iconClass: 'h-7 w-auto' },
};

export const SERVICES = [
  {
    id: 'ia-automatizacion',
    title: 'IA y automatización',
    badge: 'Especialidad',
    description:
      'Agentes y chatbots que atienden a tus clientes, y automatizaciones que ordenan tus procesos internos — conectados a WhatsApp, CRM y ERP.',
    icon: 'circuit',
    href: '/ia-y-automatizacion/',
  },
  {
    id: 'desarrollo-web',
    title: 'Desarrollo web',
    description:
      'Sitios que posicionan en Google y aplicaciones a la medida: portales, dashboards e integraciones con tus sistemas.',
    icon: 'browser',
    href: '/desarrollo-web/',
  },
  {
    id: 'ecommerce',
    title: 'Ecommerce',
    description:
      'Tiendas con checkout ágil, pagos locales y logística integrada para vender 24/7.',
    icon: 'bag',
    href: '/ecommerce/',
  },
  {
    id: 'soporte',
    title: 'Soporte y mantenimiento',
    description:
      'Monitoreo, seguridad y mejoras continuas con un plan mensual fijo.',
    icon: 'shield',
    href: '/soporte-y-mantenimiento/',
  },
];
