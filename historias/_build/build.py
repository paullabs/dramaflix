#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta as bíblias das séries em HTML e exporta PDF com o Chrome headless.

Uso:  python3 build.py            (as duas séries)
      python3 build.py A          (só a série A)
Saídas: historias/<slug>/<slug>-biblia.pdf, historias/<slug>/roteiros/epN.txt
"""
import html, importlib, json, math, os, subprocess, sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # raiz do projeto
HIST = f'{ROOT}/historias'
BUILD = f'{HIST}/_build'
WEB = f'{BUILD}/web'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
BRAND = '#EC1C5B'
os.makedirs(WEB, exist_ok=True)
sys.path.insert(0, BUILD)


def esc(s):
    return html.escape(str(s), quote=True)


def web(src, maxw=1700):
    """Copia reduzida em JPEG (PDF leve) e devolve a URL file://."""
    if not src or not os.path.exists(src):
        return None
    rel = os.path.relpath(src, ROOT).replace('/', '__')
    out = os.path.join(WEB, os.path.splitext(rel)[0] + f'_{maxw}.jpg')
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        im = Image.open(src)
        if im.mode in ('RGBA', 'LA'):
            bg = Image.new('RGB', im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            im = bg
        im = im.convert('RGB')
        if im.width > maxw:
            im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
        im.save(out, 'JPEG', quality=86, optimize=True)
    return 'file://' + out


def web_png(src, maxw=1400):
    """Para logos com transparência."""
    if not src or not os.path.exists(src):
        return None
    rel = os.path.relpath(src, ROOT).replace('/', '__')
    out = os.path.join(WEB, os.path.splitext(rel)[0] + f'_{maxw}.png')
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        im = Image.open(src).convert('RGBA')
        if im.width > maxw:
            im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
        im.save(out, 'PNG', optimize=True)
    return 'file://' + out


class Serie:
    def __init__(self, mod):
        m = importlib.import_module(mod)
        self.S, self.P, self.R = m.SERIE, m.PERSONAGENS, m.RELACOES
        self.L, self.O, self.E = m.LOCACOES, m.OBJETOS, m.EPISODIOS
        self.byid = {p['id']: p for p in self.P}
        self.loc = {l['id']: l for l in self.L}
        self.obj = {o['id']: o for o in self.O}
        self.slug = self.S['slug']
        reg = os.path.join(BUILD, 'assets.json')
        self.reg = json.load(open(reg)) if os.path.exists(reg) else {}
        ele = os.path.join(BUILD, f'elenco-{self.S["letra"]}.json')
        self.elenco = json.load(open(ele)) if os.path.exists(ele) else {'characters': {}}

    def asset(self, key):
        if not key:
            return None
        if key.startswith('_refs/'):
            return f'{HIST}/{key}'
        for t in ('personagens', 'locacoes', 'objetos'):
            p = f'{HIST}/{self.slug}/assets/{t}/{key}.png'
            if os.path.exists(p):
                return p
        return None

    def img(self, key, maxw=1700, cls='', alt=''):
        url = web(self.asset(key), maxw)
        if not url:
            return f'<div class="ph {cls}"><span>imagem em geração<br>{esc(key)}</span></div>'
        return f'<img class="{cls}" src="{url}" alt="{esc(alt)}">'

    def rosto(self, pid):
        p = self.byid[pid]
        return p['imagens'].get('rosto')


# ----------------------------------------------------------------------------- páginas

def page(X, section, body, cls=''):
    return (f'<section class="page {cls}"><div class="top"><span><b>{esc(X.S["titulo"])}</b></span>'
            f'<span>{esc(section)}</span></div><div class="content">{body}</div>'
            f'<div class="foot"><span>Bíblia da série · teste piloto · 3 episódios</span><span class="pnum"></span></div></section>')


def cover(X):
    S = X.S
    capa = web(f'{ROOT}/{S["capa"]}', 1700)
    return f'''<section class="page cover">
<img class="bg" src="{capa}" alt="">
<div class="shade"></div>
<div class="cv-top"><span class="brand">DRAMA</span><span class="cv-doc">Bíblia da série</span></div>
<div class="cv-bottom">
  <div class="cv-kicker">Teste piloto · 3 episódios · vertical 9:16 · live action</div>
  <div class="cv-line">{esc(S["genero"])}</div>
  <div class="cv-index">Série · Elenco e sheets · Locações · Objetos · Roteiros · Decupagem · Produção no short drama</div>
</div></section>'''


def p_serie(X):
    S = X.S
    banner = web(f'{ROOT}/{S["banner"]}', 1800)
    temas = ''.join(f'<li>{esc(t)}</li>' for t in S['temas'])
    body = f'''
<div class="kicker">A série</div>
<h1 class="disp">{esc(S["titulo"])}</h1>
<div class="chips"><span class="chip acc">{esc(S["genero"])}</span><span class="chip">{esc(S["formato"])}</span></div>
<div class="hero"><img src="{banner}" alt=""></div>
<p class="quote big">{esc(S["logline"])}</p>
<div class="box acc"><div class="box-k">O absurdo da abertura</div><p>{esc(S["gancho"])}</p></div>
<div class="grid3">
  <div><h3>Tom</h3><p>{esc(S["tom"])}</p></div>
  <div><h3>Temas</h3><ul class="dash">{temas}</ul></div>
  <div><h3>Público</h3><p>{esc(S["publico"])}</p><h3>Look (luz e cenário)</h3><p>{esc(S["look"])}</p></div>
</div>'''
    return page(X, 'A série', body)


def curva_svg(X):
    pts = X.S['curva']
    w, h, padx = 520, 120, 60
    xs = [padx + i * (w - 2 * padx) / (len(pts) - 1) for i in range(len(pts))]
    ys = [h - 18 - v / 100 * (h - 40) for _, _, v in pts]
    path = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
    area = path + f' L{xs[-1]:.1f},{h-18} L{xs[0]:.1f},{h-18} Z'
    dots = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{BRAND}"/>'
                   f'<text x="{x:.1f}" y="{y-11:.1f}" text-anchor="middle" class="sv-l">{esc(lbl)}</text>'
                   f'<text x="{x:.1f}" y="{h-4}" text-anchor="middle" class="sv-e">{esc(ep)}</text>'
                   for (ep, lbl, _), x, y in zip(pts, xs, ys))
    return (f'<svg viewBox="0 0 {w} {h}" class="curva"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{BRAND}" stop-opacity=".22"/><stop offset="1" stop-color="{BRAND}" stop-opacity="0"/>'
            f'</linearGradient></defs><line x1="{padx-30}" y1="{h-18}" x2="{w-padx+30}" y2="{h-18}" stroke="#E7E2DC"/>'
            f'<path d="{area}" fill="url(#g)"/><path d="{path}" fill="none" stroke="{BRAND}" stroke-width="3"/>{dots}</svg>')


def p_sinopse(X):
    S = X.S
    paras = ''.join(f'<p>{esc(t)}</p>' for t in S['sinopse'])
    cards = ''.join(f'''<div class="epcard"><div class="epn">{a["ep"]:02d}</div><div class="ept">{esc(a["titulo"])}</div>
<p>{esc(a["resumo"])}</p><div class="epg"><span>Gancho</span>{esc(a["gancho"])}</div></div>''' for a in S['arco'])
    prot = X.P[0]['nome'] if X.S['letra'] == 'A' else 'Téo'
    body = f'''
<div class="kicker">Sinopse</div>
<h2 class="disp2">A história dos 3 episódios</h2>
<div class="cols2 sin">{paras}</div>
<h3>Arco em 3 episódios</h3>
<div class="grid3 eps">{cards}</div>
<h3>Curva de status de {esc(prot)}</h3>
{curva_svg(X)}
<h3>Como a fórmula clichê funciona nesta série</h3>
<ol class="regras">{''.join(f'<li>{esc(r)}</li>' for r in S['regras'])}</ol>'''
    return page(X, 'Sinopse', body)


POS = {
    'A': {'dani': (0, 0), 'cleber': (-62, 2), 'neusa': (-38, -36), 'kelly': (-38, 40), 'tiago': (62, 2), 'valter': (38, 40)},
    'B': {'laura': (-27, -2), 'teo': (27, -2), 'augusto': (-64, -30), 'henrique': (-64, 26), 'juiz': (-30, 42),
          'celeste': (64, -30), 'osvaldo': (64, 26), 'barbeiro': (30, 42)},
}


def mapa_svg(X):
    pos = POS[X.S['letra']]
    W, H, cx, cy, sc, r = 640, 420, 320, 186, 4.0, 32
    def xy(pid):
        x, y = pos[pid]
        return cx + x * sc, cy + y * sc
    out = [f'<svg viewBox="0 0 {W} {H}" class="mapa">']
    for a, b, lbl in X.R:
        (x1, y1), (x2, y2) = xy(a), xy(b)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#CFC8C0" stroke-width="1.6"/>')
        tw = len(lbl) * 5.6 + 14
        mx = min(max(mx, tw / 2 + 4), W - tw / 2 - 4)
        out.append(f'<rect x="{mx-tw/2:.0f}" y="{my-9:.0f}" width="{tw:.0f}" height="17" rx="8.5" fill="#fff" stroke="#E7E2DC"/>'
                   f'<text x="{mx:.0f}" y="{my+3.5:.0f}" text-anchor="middle" class="sv-r">{esc(lbl)}</text>')
    for i, pid in enumerate(pos):
        p = X.byid[pid]
        x, y = xy(pid)
        url = web(X.asset(X.rosto(pid)), 400) or ''
        out.append(f'<clipPath id="c{i}"><circle cx="{x:.0f}" cy="{y:.0f}" r="{r}"/></clipPath>'
                   f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r+3}" fill="#fff" stroke="{BRAND if p["lado"].startswith("Protag") else "#D9D2CA"}" stroke-width="2.2"/>'
                   f'<image href="{url}" x="{x-r:.0f}" y="{y-r*1.1:.0f}" width="{2*r}" height="{2*r*1.33:.0f}" preserveAspectRatio="xMidYMin slice" clip-path="url(#c{i})"/>'
                   f'<text x="{x:.0f}" y="{y+r+16:.0f}" text-anchor="middle" class="sv-n">{esc(p["nome"])}</text>')
    out.append('</svg>')
    return ''.join(out)


def p_elenco(X):
    n = len(X.P)
    cols = 4 if n > 6 else 3
    cards = ''
    for p in X.P:
        url = web(X.asset(X.rosto(p['id'])), 500)
        face = f'<img src="{url}" alt="">' if url else '<div class="ph"></div>'
        cards += f'''<div class="cc"><div class="cc-face">{face}</div><div class="cc-t">
<div class="cc-n">{esc(p["nome"])} <span>{p["idade"]}</span></div><div class="cc-r">{esc(p["lado"])} · {esc(p["role_pt"])}</div>
<div class="cc-b">“{esc(p["bordao"])}”</div></div></div>'''
    body = f'''
<div class="kicker">Elenco</div>
<h2 class="disp2">Quem é quem</h2>
<div class="ccgrid c{cols}">{cards}</div>
<h3>Mapa de relações</h3>
{mapa_svg(X)}'''
    return page(X, 'Elenco', body)


def lista(items):
    return '<ul class="dash">' + ''.join(f'<li>{esc(i)}</li>' for i in items) + '</ul>'


def p_personagem(X, p):
    thumbs = ''
    ims = p['imagens']
    if p['rota'] == 'foto':
        u = web(X.asset(ims['rosto']), 500)
        thumbs = f'<figure><img src="{u}" alt=""><figcaption>Foto da capa (rosto aprovado)</figcaption></figure>'
    else:
        for k, lbl in (('rosto', 'Rosto'), ('figurino', 'Figurino')):
            u = web(X.asset(ims.get(k)), 500)
            thumbs += (f'<figure><img src="{u}" alt=""><figcaption>{lbl}</figcaption></figure>' if u else
                       f'<figure><div class="ph"></div><figcaption>{lbl}</figcaption></figure>')
    eps = ' · '.join(f'Ep {e}' for e in p['eps'])
    rel = ''.join(f'<span class="chip">{esc(r)}</span>' for r in p['relacoes'])
    body = f'''
<div class="ph-head">
  <div class="ph-id"><div class="kicker">{esc(p["lado"])} · {esc(p["role_pt"])}</div>
    <h1 class="disp">{esc(p["nome"])} <span class="age">{p["idade"]}</span></h1>
    <div class="sub">{esc(p["completo"])} · status {esc(p["status"])} · {eps}</div></div>
  <div class="thumbs">{thumbs}</div>
</div>
<div class="sheet">{X.img(ims["sheet"], 1800, "sheetimg", p["nome"])}</div>
<div class="pcols">
  <div class="pc-l">
    <p class="quote">{esc(p["leitura"])}</p>
    <h3>Aparência</h3><p>{esc(p["aparencia"])}</p>
    <h3>Figurino base</h3>{lista(p["figurino"])}
    <h3>Voz</h3><p>{esc(p["voz"])}</p>
  </div>
  <div class="pc-r">
    <h3>Personalidade</h3><p>{esc(p["personalidade"])}</p>
    <div class="two"><div><h3>O que quer</h3><p>{esc(p["objetivo"])}</p></div><div><h3>Segredo</h3><p>{esc(p["segredo"])}</p></div></div>
    <h3>Arco</h3>{lista(p["arco"])}
    <div class="bordao"><span>Bordão</span>“{esc(p["bordao"])}”</div>
    <h3>Relações</h3><div class="chips">{rel}</div>
  </div>
</div>'''
    return page(X, f'Elenco · {p["nome"]}', body, 'pp')


def p_look(X, p, lk):
    base_img = X.img(p['imagens']['sheet'], 900, '', 'sheet base')
    extra = ''
    if lk.get('rosto'):
        u = web(X.asset(lk['rosto']), 500)
        extra = f'<figure class="lk-f"><img src="{u}" alt=""><figcaption>Rosto do look (edição aprovada)</figcaption></figure>'
    objs = ''
    if lk.get('objetos'):
        objs = ('<h3>Objetos que acompanham este look</h3><div class="minis">' +
                ''.join(f'<div class="minio big">{X.img(o, 900, "", "")}<span>{esc(X.obj[o]["nome"])}: {esc(X.obj[o]["look"])}</span></div>'
                        for o in lk['objetos']) + '</div>')
    body = f'''
<div class="kicker">Look 2 · {esc(p["nome"])}</div>
<h1 class="disp">{esc(lk["nome"])}</h1>
<div class="sub">{esc(lk["eps"])}</div>
<div class="sheet">{X.img(lk["id"], 1800, "sheetimg", lk["nome"])}</div>
<div class="lk-row">
  <div class="lk-t"><h3>O que muda em relação ao look base</h3><p>{esc(lk["muda"])}</p>
  <h3>Regra de continuidade</h3><p>O rosto, o corpo e o cabelo seguem o sheet base, exceto o que está escrito acima. Objetos de mão (óculos, celular, cartão) ficam fora do sheet e entram pela lista de objetos.</p></div>
  <div class="lk-imgs">{extra}<figure class="lk-f">{base_img}<figcaption>Sheet base</figcaption></figure></div>
</div>{objs}'''
    return page(X, f'Elenco · {p["nome"]} · look 2', body, 'pp')


def planta_svg(l):
    m = l['mapa']
    return f'''<svg viewBox="0 0 300 220" class="planta">
<rect x="40" y="26" width="220" height="150" rx="4" fill="#F7F2EC" stroke="#CFC8C0" stroke-width="2"/>
<rect x="110" y="70" width="80" height="60" rx="3" fill="none" stroke="#E2DBD3" stroke-dasharray="4 4"/>
<circle cx="56" cy="101" r="11" fill="{BRAND}"/><text x="56" y="105" text-anchor="middle" class="sv-k">1</text>
<circle cx="244" cy="101" r="11" fill="{BRAND}"/><text x="244" y="105" text-anchor="middle" class="sv-k">2</text>
<circle cx="150" cy="42" r="11" fill="{BRAND}"/><text x="150" y="46" text-anchor="middle" class="sv-k">3</text>
<circle cx="150" cy="160" r="11" fill="{BRAND}"/><text x="150" y="164" text-anchor="middle" class="sv-k">4</text>
<path d="M150 214 L136 190 L164 190 Z" fill="#16141A"/><text x="176" y="206" class="sv-s">câmera (plano geral)</text>
<line x1="150" y1="190" x2="122" y2="60" stroke="#16141A" stroke-dasharray="3 4" stroke-width="1"/>
<line x1="150" y1="190" x2="178" y2="60" stroke="#16141A" stroke-dasharray="3 4" stroke-width="1"/>
<text x="150" y="104" text-anchor="middle" class="sv-s" stroke="#F7F2EC" stroke-width="6" style="paint-order:stroke">área livre</text>
</svg>
<ol class="leg"><li><b>Esquerda</b> {esc(m["Esquerda"])}</li><li><b>Direita</b> {esc(m["Direita"])}</li>
<li><b>Fundo</b> {esc(m["Fundo"])}</li><li><b>Frente</b> {esc(m["Frente"])}</li></ol>'''


def p_locacao(X, l, i):
    luz = lista(l['luz'])
    cenas = ''.join(f'<li><b>Ep {e["n"]} · cena {c["n"]}</b> <span>{esc(c["tempo"])}</span> {esc(c["cab"])}</li>'
                    for e in X.E for c in e['cenas'] if c['loc'] == l['id'])
    body = f'''
<div class="kicker">Locação {i} de {len(X.L)}</div>
<h1 class="disp">{esc(l["nome"])}</h1>
<div class="chips"><span class="chip acc">{esc(l["hora"])}</span><span class="chip">{esc(l["eps"])}</span></div>
<div class="sheet">{X.img(l["id"], 1800, "sheetimg", l["nome"])}</div>
<div class="loc-row">
  <div class="loc-t"><h3>Como é</h3><p>{esc(l["look"])}</p><h3>Luz</h3>{luz}<h3>Nota de cena</h3><p>{esc(l["nota"])}</p></div>
  <div class="loc-p"><h3>Planta do set</h3>{planta_svg(l)}</div>
</div>
<h3>Cenas nesta locação</h3><ul class="cenas">{cenas}</ul>'''
    return page(X, 'Locações', body)


def p_objetos(X, objs, k, total):
    rows = ''
    for o in objs:
        rows += f'''<div class="obj"><div class="obj-i">{X.img(o["id"], 1200, "", o["nome"])}</div><div class="obj-t">
<h2 class="disp3">{esc(o["nome"])}</h2>
<div class="chips"><span class="chip acc">Com: {esc(o["com"])}</span><span class="chip">{esc(o["eps"])}</span></div>
<p>{esc(o["look"])}</p><div class="why"><span>Por que importa</span>{esc(o["porque"])}</div></div></div>'''
    body = f'<div class="kicker">Objetos {k} de {total}</div><h2 class="disp2">Objetos de cena</h2>{rows}'
    return page(X, 'Objetos', body)


def p_ep_abre(X, e):
    bat = ''.join(f'<li>{esc(b)}</li>' for b in e['batidas'])
    faces = ''
    for pid in e['elenco']:
        u = web(X.asset(X.rosto(pid)), 400)
        faces += f'<div class="mini"><img src="{u}" alt=""><span>{esc(X.byid[pid]["nome"])}</span></div>'
    locs = ''.join(f'<div class="minil">{X.img(lid, 600, "", "")}<span>{esc(X.loc[lid]["nome"])}</span></div>' for lid in e['locacoes'])
    objs = ''.join(f'<div class="minio">{X.img(oid, 500, "", "")}<span>{esc(X.obj[oid]["nome"])}</span></div>' for oid in e['objetos'])
    looks = ''
    if e.get('looks'):
        looks = '<p class="small">Looks: ' + '; '.join(f'{esc(X.byid[k]["nome"])}: {esc(v)}' for k, v in e['looks'].items()) + '</p>'
    body = f'''
<div class="ep-head"><div class="ep-num">{e["n"]:02d}</div><div>
<div class="kicker">Episódio {e["n"]} · {esc(e["duracao"])}</div><h1 class="disp">{esc(e["titulo"])}</h1>
<p class="quote">{esc(e["logline"])}</p></div></div>
<h3>A fórmula do episódio</h3>
<div class="formula">
  <div class="fm f1"><span>1 · Abertura absurda</span>{esc(e["absurdo"])}</div>
  <div class="fm"><span>2 · Humilhação</span>{esc(e["humilhacao"])}</div>
  <div class="fm"><span>3 · Virada</span>{esc(e["virada"])}</div>
  <div class="fm f4"><span>4 · Gancho</span>{esc(e["gancho"])}</div>
</div>
<h3>Batidas</h3><ol class="beats">{bat}</ol>
<h3>Nesta corrida do short drama</h3>
<div class="run"><div class="run-k">Elenco com sheet ({len(e["elenco"])})</div><div class="minis">{faces}</div>
<div class="run-k">Locações ({len(e["locacoes"])})</div><div class="minis">{locs}</div>
<div class="run-k">Objetos ({len(e["objetos"])})</div><div class="minis">{objs}</div>{looks}</div>
<div class="frase"><span>A fala do episódio</span>“{esc(e["frase"][1])}”<em>— {esc(e["frase"][0])}</em></div>'''
    return page(X, f'Episódio {e["n"]}', body)


def parse_roteiro(txt):
    blocos = []
    for ln in txt.strip().split('\n'):
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith('@'):
            blocos.append(('ac', ln[1:].strip()))
        else:
            quem, par, fala = [x.strip() for x in ln.split('|', 2)]
            blocos.append(('dl', quem, par, fala))
    return blocos


def p_roteiro(X, e):
    out = []
    for c in e['cenas']:
        locu = web(X.asset(c['loc']), 500)
        out.append(f'<div class="sc keepnext"><div class="sc-t"><span class="scn">Cena {c["n"]}</span>'
                   f'<span class="sct">{esc(c["tempo"])}</span></div><div class="sch">{esc(c["cab"])}</div>'
                   + (f'<img class="sc-img" src="{locu}" alt="">' if locu else '') + '</div>')
        for b in parse_roteiro(c['roteiro']):
            if b[0] == 'ac':
                out.append(f'<p class="ac">{esc(b[1])}</p>')
            else:
                _, quem, par, fala = b
                par_h = f'<div class="par">({esc(par)})</div>' if par else ''
                out.append(f'<div class="dlg"><div class="who">{esc(quem)}</div>{par_h}<div class="line">{esc(fala)}</div></div>')
    out.append(f'<div class="fim">Fim do episódio {e["n"]}</div><div class="box dark"><div class="box-k">Gancho</div><p>{esc(e["gancho"])}</p></div>')
    out += decupagem_blocos(X, e)
    body = f'<div class="kicker">Episódio {e["n"]} · roteiro</div>' + ''.join(out)
    return '<div class="flowgroup">' + page(X, f'Episódio {e["n"]} · roteiro e decupagem', body, 'flow roteiro') + '</div>'


def seg(t):
    a, b = t.split('–')
    f = lambda s: int(s.split(':')[0]) * 60 + int(s.split(':')[1])
    return f(b) - f(a)


def decupagem_blocos(X, e):
    total = sum(seg(t) for _, t, _, _ in e['clipes'])
    maxclips = math.ceil(total / 15)
    elenco = ', '.join(f'{X.byid[p]["nome"]} ({X.byid[p]["idade"]})' for p in e['elenco'])
    locs = ', '.join(X.loc[l]['nome'] for l in e['locacoes'])
    objs = ', '.join(X.obj[o]['nome'] for o in e['objetos'])
    out = [f'<div class="dec-h keepnext"><div class="kicker">Episódio {e["n"]} · decupagem 9:16</div>'
           f'<h2 class="disp2">Clipes do episódio {e["n"]}</h2>'
           '<div class="drow dh"><span>Clipe</span><span>Tempo</span><span>Dur.</span><span>Cena</span><span>O que a câmera mostra</span></div></div>']
    for n, t, c, d in e['clipes']:
        out.append(f'<div class="drow"><span class="n">{n}</span><span>{esc(t)}</span><span>{seg(t)} s</span><span>{c}</span><span>{esc(d)}</span></div>')
    out.append(f'''<div class="check"><h3>Checklist da corrida no short drama</h3><ul class="dash">
<li>Duração do filme: {total} s (limite 180 s) · {len(e["clipes"])} clipes (máximo {maxclips}: um para cada 15 s iniciados) · cada clipe entre 4 e 30 s.</li>
<li>Elenco com sheet ({len(e["elenco"])} de 8): {esc(elenco)}.</li>
<li>Locações ({len(e["locacoes"])} de 4): {esc(locs)}.</li>
<li>Objetos com imagem ({len(e["objetos"])} de 4): {esc(objs)}.</li>
<li>Formato 9:16 · look realism_cinematic · falas em português, palavra por palavra · idades escritas no roteiro como NOME (idade).</li>
<li>Saltos de tempo mostrados pela imagem ou ditos em fala: nada de letreiro na tela.</li>
<li>Roteiro em texto, pronto para colar: roteiros/ep{e["n"]}.txt</li></ul></div>''')
    return out


def p_producao(X):
    S = X.S
    eprows = ''.join(f'<tr><td class="n">{e["n"]}</td><td>{esc(e["titulo"])}</td><td>{esc(e["duracao"])}</td>'
                     f'<td>{len(e["clipes"])}</td><td>{len(e["elenco"])}</td><td>{len(e["locacoes"])}</td><td>{len(e["objetos"])}</td></tr>'
                     for e in X.E)
    marca = ('<li>"Mega-Sena" é marca registrada: nos prompts de imagem e de clipe, diga "loteria" e "bilhete de loteria". '
             'As falas já usam "loteria" e "prêmio".</li>'
             '<li>Licença dramática: a cláusula de renúncia do divórcio (ep 3) não vale assim na vida real; é parte da comédia.</li>'
             if S['letra'] == 'A' else
             '<li>Banco Monteiro, Valente Têxtil e Lacerda são nomes fictícios. Nos prompts, descreva pela aparência, sem nomes.</li>'
             '<li>A cédula da rosa de origami é descrita como "cédula azul-acinzentada", sem reproduzir dinheiro real.</li>')
    atencao = ''
    if S.get('atencao'):
        atencao = '<h3>Ponto de atenção nas imagens</h3>' + lista(S['atencao'])
    body = f'''
<div class="kicker">Produção</div>
<h2 class="disp2">Como levar para o short drama do Higgsfield</h2>
<ol class="steps">
<li><b>Uma corrida por episódio.</b> Cada episódio é um filme de até 180 s, feito em ordem (1, 2, 3) no mesmo chat, com as mesmas pessoas e o mesmo look.</li>
<li><b>Cole o roteiro do episódio</b> (arquivo roteiros/epN.txt). As idades estão escritas no próprio texto, como "DANI (28)", para o sistema reconhecer todos como adultos.</li>
<li><b>Escolha</b> 9:16, o look realism_cinematic (live action) e a qualidade: rascunho em 480p para conferir e final em 1080p.</li>
<li><b>Mantenha a identidade:</b> use os sheets e os rostos deste documento como referência de cada personagem e repita os cartões de voz da página seguinte, palavra por palavra, em todas as corridas.</li>
<li><b>Confira na parada das imagens:</b> cada pessoa igual em todas as imagens, roupa de acordo com a cena e gente da mesma cena fácil de distinguir.</li>
</ol>
<h3>Os três episódios</h3>
<table class="dec"><thead><tr><th>Ep</th><th>Título</th><th>Duração</th><th>Clipes</th><th>Elenco</th><th>Locações</th><th>Objetos</th></tr></thead><tbody>{eprows}</tbody></table>
<h3>Regras que já estão respeitadas neste roteiro</h3>
<ul class="dash">
<li>No máximo 8 personagens com imagem, 4 locações e 4 objetos por episódio.</li>
<li>Clipes de 4 a 30 s; no máximo um clipe a cada 15 s iniciados de filme.</li>
<li>Todo mundo que fala ou age em cena tem idade adulta declarada no roteiro.</li>
<li>Nenhuma pessoa real, nenhuma marca de terceiros nas imagens.</li>
{marca}
</ul>{atencao}'''
    return page(X, 'Produção', body)


TIPO = {'locacoes': 'Locação', 'objetos': 'Objeto', 'personagens': 'Personagem'}


def p_cartoes_indice(X):
    out = ['<div class="kicker">Produção · cartões em inglês</div><h2 class="disp2">Cartões de personagem para colar</h2>'
           '<p class="small">Mesmos dados de elenco usados para escrever os prompts dos sheets. Repita-os sem mudar nada em todas as corridas, para manter rosto, roupa e voz iguais nos três episódios.</p>']
    chars = X.elenco.get('characters', {})
    for p in X.P:
        c = chars.get(p['id'], {})
        facts = '; '.join(f for f in c.get('facts', []) if not f.startswith('Base outfit'))
        outfit = next((f.split(':', 1)[1].strip() for f in c.get('facts', []) if f.startswith('Base outfit')), '')
        out.append(f'''<div class="card"><div class="card-h">{esc(p["nome"])} <span>{esc(p["role"])} · {p["idade"]}</span></div>
<div class="card-b"><b>Profile</b> {esc(facts)}<br><b>Wardrobe</b> {esc(outfit)}<br><b>Voice card</b> {esc(p["voz_en"])}</div></div>''')
    nf = [p['nome'] for p in X.P if p['rota'] == 'foto']
    fotos_txt = (f'O rosto de {nf[0]} vem da capa da série' if len(nf) == 1 else
                 f'Os rostos de {", ".join(nf[:-1])} e {nf[-1]} vêm das capas da série')
    out.append('<div class="keepnext idx-h"><div class="kicker">Produção · índice de imagens</div><h2 class="disp2">Arquivos e IDs no Higgsfield</h2>'
               f'<p class="small">Imagens em historias/{esc(X.slug)}/assets/. O ID de geração permite reaproveitar cada imagem como referência no Higgsfield. '
               f'{esc(fotos_txt)} (historias/_refs/).</p>'
               '<div class="irow ih"><span>Tipo</span><span>Arquivo</span><span>ID da geração no Higgsfield</span></div></div>')
    for key, v in sorted(X.reg.items(), key=lambda kv: (kv[1].get('tipo', ''), kv[0])):
        if v.get("serie") != X.S["letra"] or v.get("rejeitado"):
            continue
        out.append(f'<div class="irow"><span>{TIPO.get(v.get("tipo",""), "")}</span><span>{esc(key)}.png</span><span class="mono">{esc(v.get("job",""))}</span></div>')
    return '<div class="flowgroup">' + page(X, 'Produção · cartões e índice', ''.join(out), 'flow') + '</div>'


# ----------------------------------------------------------------------------- roteiro em texto

def roteiro_txt(X, e):
    L = [f'{X.S["titulo"].upper()} — EPISÓDIO {e["n"]}: {e["titulo"].upper()}', '']
    for c in e['cenas']:
        L += [f'CENA {c["n"]} — {c["cab"]}', '']
        for b in parse_roteiro(c['roteiro']):
            if b[0] == 'ac':
                L += [b[1], '']
            else:
                _, quem, par, fala = b
                L += [quem + (f' ({par})' if par in ('O.S.',) else '')]
                if par and par != 'O.S.':
                    L += [f'({par})']
                L += [fala, '']
    L += [f'FIM DO EPISÓDIO {e["n"]}']
    return '\n'.join(L) + '\n'


# ----------------------------------------------------------------------------- montagem

def build(letra):
    X = Serie('serie_a' if letra == 'A' else 'serie_b')
    css = open(os.path.join(BUILD, 'estilo.css')).read().replace('--acc-serie', X.S['cor'])
    pages = [cover(X), p_serie(X), p_sinopse(X), p_elenco(X)]
    for p in X.P:
        pages.append(p_personagem(X, p))
        for lk in p.get('looks', []):
            pages.append(p_look(X, p, lk))
    for i, l in enumerate(X.L, 1):
        pages.append(p_locacao(X, l, i))
    half = math.ceil(len(X.O) / 2)
    pages.append(p_objetos(X, X.O[:half], 1, 2))
    pages.append(p_objetos(X, X.O[half:], 2, 2))
    for e in X.E:
        pages += [p_ep_abre(X, e), p_roteiro(X, e)]
    pages += [p_producao(X), p_cartoes_indice(X)]
    js = open(os.path.join(BUILD, 'paginar.js')).read()
    doc = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{esc(X.S["titulo"])} — bíblia</title>'
           f'<style>{css}</style></head><body>{"".join(pages)}<script>{js}</script></body></html>')
    outdir = f'{HIST}/{X.slug}'
    os.makedirs(f'{outdir}/roteiros', exist_ok=True)
    for e in X.E:
        open(f'{outdir}/roteiros/ep{e["n"]}.txt', 'w').write(roteiro_txt(X, e))
    hp = f'{BUILD}/{X.slug}.html'
    open(hp, 'w').write(doc)
    pdf = f'{outdir}/{X.slug}-biblia.pdf'
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--allow-file-access-from-files',
                    '--run-all-compositor-stages-before-draw', '--virtual-time-budget=20000',
                    f'--print-to-pdf={pdf}', 'file://' + hp], check=True, capture_output=True)
    print('PDF', pdf, f'{os.path.getsize(pdf)/1e6:.1f} MB')


if __name__ == '__main__':
    for letra in (sys.argv[1:] or ['A', 'B']):
        build(letra)
