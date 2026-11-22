"""Banner de billboard com logo: banner 16:9 sem texto + degradê à esquerda + fade inferior + título-logo.

Uso: python -I montar_banner.py BANNER LOGO SAIDA.jpg [--largura 0.36] [--base 0.74] [--altura-max 0.34] [--x 0.055]
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter

FUNDO = (20, 20, 20)  # cor da página (#141414)


def recortar(img, limiar=8):
    a = np.array(img.getchannel("A")); ys, xs = np.where(a > limiar)
    return img.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)) if len(xs) else img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("banner"); ap.add_argument("logo"); ap.add_argument("saida")
    ap.add_argument("--largura", type=float, default=0.36)
    ap.add_argument("--base", type=float, default=0.74)
    ap.add_argument("--altura-max", type=float, default=0.34)
    ap.add_argument("--x", type=float, default=0.055)
    a = ap.parse_args()

    im = Image.open(a.banner).convert("RGB")
    W, H = im.size
    arr = np.array(im).astype(np.float32)

    # degradê da esquerda (texto/logo legíveis), parecido com o da Netflix: preto 75% -> 0 em 62% da largura
    x = np.arange(W, dtype=np.float32) / W
    esq = np.clip(1 - x / 0.62, 0, 1) ** 1.4 * 0.78
    # fade inferior para a cor da página (as fileiras entram por cima)
    y = np.arange(H, dtype=np.float32) / H
    baixo = np.clip((y - 0.62) / 0.38, 0, 1) ** 1.5
    for c in range(3):
        canal = arr[:, :, c]
        canal = canal * (1 - esq[None, :])                       # escurece à esquerda
        canal = canal * (1 - baixo[:, None]) + FUNDO[c] * baixo[:, None]  # funde no fundo embaixo
        arr[:, :, c] = canal
    base = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB").convert("RGBA")

    logo = recortar(Image.open(a.logo).convert("RGBA"))
    lw = int(W * a.largura); lh = int(logo.height * lw / logo.width)
    if lh > H * a.altura_max:
        lh = int(H * a.altura_max); lw = int(logo.width * lh / logo.height)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    x0 = int(W * a.x); y0 = int(H * a.base) - lh

    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    blk = Image.new("RGBA", (lw, lh), (0, 0, 0, 255)); blk.putalpha(logo.getchannel("A").point(lambda v: int(v * 0.6)))
    sombra.paste(blk, (x0, y0 + int(W * 0.003)), blk)
    base = Image.alpha_composite(base, sombra.filter(ImageFilter.GaussianBlur(W * 0.008)))
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0)); camada.paste(logo, (x0, y0), logo)
    base = Image.alpha_composite(base, camada)

    out = np.array(base.convert("RGB")).astype(np.float32)
    am = np.array(camada.getchannel("A")).astype(np.float32) / 255.0
    out += (np.random.default_rng(3).normal(0, 4.5, (H, W)).astype(np.float32) * am)[:, :, None]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGB").save(a.saida, quality=88, optimize=True)
    print("ok", a.saida, f"{W}x{H}", f"logo {lw}x{lh} em x={x0} y={y0}")


if __name__ == "__main__":
    main()
