"""Monta a capa 3:4: foto realista + degradê inferior + título (PNG transparente) com sombra e grão.

Uso:
  python -I montar_capa.py FOTO TITULO SAIDA.png [--largura 0.88] [--base 0.865] [--altura-max 0.30]
                           [--degrade-inicio 0.52] [--degrade-max 0.85] [--web SAIDA_WEB.jpg]
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter


def recortar_transparente(img, limiar=8):
    a = np.array(img.getchannel("A"))
    ys, xs = np.where(a > limiar)
    if len(xs) == 0:
        return img
    return img.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("foto"); ap.add_argument("titulo"); ap.add_argument("saida")
    ap.add_argument("--largura", type=float, default=0.88)      # largura do título / largura da capa
    ap.add_argument("--base", type=float, default=0.865)        # base do título (fração da altura)
    ap.add_argument("--altura-max", type=float, default=0.30)   # altura máxima do título (fração da altura)
    ap.add_argument("--degrade-inicio", type=float, default=0.52)
    ap.add_argument("--degrade-max", type=float, default=0.85)
    ap.add_argument("--grao", type=float, default=5.0)          # desvio do grão aplicado sobre o título
    ap.add_argument("--web", default=None)
    a = ap.parse_args()

    foto = Image.open(a.foto).convert("RGB")
    W, H = foto.size

    # 1) degradê escuro na parte de baixo (legibilidade do título + faixa do "▶ N Episódios")
    y = np.arange(H, dtype=np.float32) / H
    t = np.clip((y - a.degrade_inicio) / (1 - a.degrade_inicio), 0, 1)
    alpha = (t ** 1.6) * a.degrade_max
    mask = Image.fromarray((np.repeat(alpha[:, None], W, axis=1) * 255).astype(np.uint8), "L")
    foto = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), foto, mask)

    # 2) título: recorta margens transparentes e escala
    tit = recortar_transparente(Image.open(a.titulo).convert("RGBA"))
    tw = int(W * a.largura)
    th = int(tit.height * tw / tit.width)
    if th > H * a.altura_max:
        th = int(H * a.altura_max)
        tw = int(tit.width * th / tit.height)
    tit = tit.resize((tw, th), Image.LANCZOS)
    x0 = (W - tw) // 2
    y0 = int(H * a.base) - th

    # 3) sombra suave por baixo do título
    base = foto.convert("RGBA")
    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    a_t = tit.getchannel("A").point(lambda v: int(v * 0.65))
    blk = Image.new("RGBA", (tw, th), (0, 0, 0, 255)); blk.putalpha(a_t)
    sombra.paste(blk, (x0, y0 + int(W * 0.006)), blk)
    sombra = sombra.filter(ImageFilter.GaussianBlur(radius=W * 0.012))
    base = Image.alpha_composite(base, sombra)

    # 4) título por cima
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    camada.paste(tit, (x0, y0), tit)
    base = Image.alpha_composite(base, camada)

    # 5) grão só onde há título, para casar com o filme da foto
    arr = np.array(base.convert("RGB")).astype(np.float32)
    am = np.array(camada.getchannel("A")).astype(np.float32) / 255.0
    rng = np.random.default_rng(7)
    ruido = rng.normal(0, a.grao, (H, W)).astype(np.float32)
    arr += (ruido * am)[:, :, None]
    out = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    out.save(a.saida, optimize=True)
    if a.web:
        out.resize((600, 800), Image.LANCZOS).save(a.web, quality=85, optimize=True)
    print(f"ok {a.saida} {W}x{H} titulo {tw}x{th} em y={y0}..{y0+th}")


if __name__ == "__main__":
    main()
