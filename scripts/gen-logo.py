# -*- coding: utf-8 -*-
"""Genera los assets del logotipo AlquimIA a partir de los contornos reales de
Archivo (OFL): ALQUIM en ExtraLight (200) tracionado + IA en ExtraBold (800).

Salidas (todas se sobrescriben):
  public/favicon.svg                 avatar |A sobre azul profundo
  public/logo-alquimia.svg           logotipo horizontal, positivo
  public/logo-alquimia-negativo.svg  logotipo horizontal, negativo
  src/components/Logo.astro          logotipo como SVG en linea
  src/components/LogoMark.astro      isotipo |A como SVG en linea

Uso:  python3 scripts/gen-logo.py     (requiere fontTools)
"""
import io
import os
import urllib.request

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, 'scripts', '.fonts')
UPEM = 1000.0

# Instancias estaticas de Archivo servidas por Google Fonts (css2, formato ttf)
SOURCES = {
    200: 'https://fonts.gstatic.com/s/archivo/v25/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTtDNp8A.ttf',
    800: 'https://fonts.gstatic.com/s/archivo/v25/k3k6o8UDI-1M0wlSV9XAw6lQkqWY8Q82sJaRE-NWIDdgffTTtDRp8A.ttf',
}

INK, ACTION, WHITE, CYAN, DEEP = '#0D1440', '#2440D6', '#FFFFFF', '#6FE3F4', '#0A1236'


def load_fonts():
    if not os.path.isdir(CACHE):
        os.makedirs(CACHE)
    fonts = {}
    for weight, url in SOURCES.items():
        path = os.path.join(CACHE, 'archivo-%d.ttf' % weight)
        if not os.path.exists(path):
            print('descargando Archivo %d...' % weight)
            urllib.request.urlretrieve(url, path)
        fonts[weight] = TTFont(path)
    return fonts


FONTS = load_fonts()


def adv(w, ch):
    return FONTS[w]['hmtx'][ch][0]


def path_of(w, ch):
    gs = FONTS[w].getGlyphSet()
    pen = SVGPathPen(gs)
    gs[ch].draw(pen)
    return pen.getCommands()


def bounds_of(w, ch):
    gs = FONTS[w].getGlyphSet()
    pen = BoundsPen(gs)
    gs[ch].draw(pen)
    return pen.bounds


def layout(pieces, em):
    """pieces: [(peso, texto, tracking_em, clave_de_color, gap_previo_em)]."""
    scale = em / UPEM
    out, x = [], 0.0
    ink = [None, None, None, None]
    for weight, text, track, key, gap in pieces:
        x += gap * em
        for ch in text:
            b = bounds_of(weight, ch)
            if b:
                box = (x + b[0] * scale, b[1] * scale, x + b[2] * scale, b[3] * scale)
                ink[0] = box[0] if ink[0] is None else min(ink[0], box[0])
                ink[1] = box[1] if ink[1] is None else min(ink[1], box[1])
                ink[2] = box[2] if ink[2] is None else max(ink[2], box[2])
                ink[3] = box[3] if ink[3] is None else max(ink[3], box[3])
            out.append((x, path_of(weight, ch), key))
            x += adv(weight, ch) * scale + track * em
    return out, ink


def render(pieces, em, colors, bg=None, size=None):
    """SVG suelto para /public. colors mapea clave -> color."""
    glyphs, ink = layout(pieces, em)
    scale = em / UPEM
    ix0, iy0, ix1, iy1 = ink
    if size:  # lienzo cuadrado (avatar): centra la mancha de tinta
        w = h = float(size)
        ox = (size - (ix1 - ix0)) / 2 - ix0
        oy = (size - (iy1 - iy0)) / 2 + iy1
    else:
        w, h = ix1 - ix0, iy1 - iy0
        ox, oy = -ix0, iy1
    body = []
    if bg:
        body.append('  <rect width="%g" height="%g" rx="%g" fill="%s"/>' % (w, h, w * 0.22, bg))
    for gx, d, key in glyphs:
        body.append('  <path fill="%s" transform="translate(%.2f %.2f) scale(%.5f %.5f)" d="%s"/>'
                    % (colors[key], ox + gx, oy, scale, -scale, d))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g">\n%s\n</svg>\n'
            % (round(w, 2), round(h, 2), '\n'.join(body)))


COMPONENT = u'''---
// %(doc)s
// Va en contornos y no en texto con webfont para que el contraste de peso sea
// exacto desde el primer pintado y sin cargar una familia extra.
// Generado por scripts/gen-logo.py: no editar a mano.
const { variant = 'negativo', size = '%(size)s', class: className = '' } = Astro.props;

const tone = {
  negativo: { word: 'fill-white', sigla: 'fill-cyan' },
  positivo: { word: 'fill-ink', sigla: 'fill-action' },
  mono: { word: 'fill-current', sigla: 'fill-current' },
}[variant];
---

<svg
  viewBox="0 0 %(w)s %(h)s"
  role="img"
  aria-label="AlquimIA"
  class={`w-auto ${size} ${className}`}
>
  <g class={tone.word}>
%(word)s
  </g>
  <g class={tone.sigla}>
%(sigla)s
  </g>
</svg>
'''


def component(pieces, doc, default_size):
    glyphs, ink = layout(pieces, 100)
    scale = 100 / UPEM
    ix0, iy0, ix1, iy1 = ink
    ox, oy = -ix0, iy1
    groups = {'word': [], 'sigla': []}
    for gx, d, key in glyphs:
        groups[key].append('    <path transform="translate(%.2f %.2f) scale(%.5f %.5f)" d="%s"/>'
                           % (ox + gx, oy, scale, -scale, d))
    return COMPONENT % {
        'doc': doc, 'size': default_size,
        'w': round(ix1 - ix0, 2), 'h': round(iy1 - iy0, 2),
        'word': '\n'.join(groups['word']), 'sigla': '\n'.join(groups['sigla']),
    }


WORDMARK = [(200, 'ALQUIM', 0.20, 'word', 0), (800, 'IA', 0.04, 'sigla', 0.10)]
MARK = [(200, 'I', 0.10, 'word', 0), (800, 'A', 0.0, 'sigla', 0)]

FILES = {
    'public/logo-alquimia.svg': render(WORDMARK, 100, {'word': INK, 'sigla': ACTION}),
    'public/logo-alquimia-negativo.svg': render(WORDMARK, 100, {'word': WHITE, 'sigla': CYAN}),
    'public/favicon.svg': render(MARK, 44, {'word': WHITE, 'sigla': WHITE}, bg=DEEP, size=64),
    'src/components/Logo.astro': component(
        WORDMARK,
        u'Logotipo AlquimIA, dirección "Punto de fusión": ALQUIM en ExtraLight\n// tracionado + IA en ExtraBold, misma familia (Archivo, OFL), sin símbolo.',
        'h-[19px]'),
    'src/components/LogoMark.astro': component(
        MARK,
        u'Isotipo AlquimIA: las dos letras de la sigla con el mismo salto de peso\n// del logotipo. Para avatares, marcadores y espacios cuadrados.',
        'h-[28px]'),
}

for rel, content in FILES.items():
    path = os.path.join(ROOT, rel)
    io.open(path, 'w', encoding='utf-8').write(content)
    print('%-34s %d bytes' % (rel, len(content)))
