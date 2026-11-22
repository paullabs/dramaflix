#!/usr/bin/env python3
"""Refaz a pasta capas/ do DramaFlix a partir das imagens originais geradas no Higgsfield.

O que faz, na mesma ordem e com os mesmos parâmetros usados na criação (19/11/2026):
  1. baixa as fotos, os títulos (PNG transparente) e os banners listados em fontes_higgsfield.json;
  2. monta as 18 capas 3:4 com montar_capa.py (foto + degradê + título + grão) e a versão web 600x800;
  3. gera os banners web 1920x1084 e as prévias com logo (montar_banner.py);
  4. completa capas/catalogo.json com o lote v3 e os banners (atualizar_catalogo.py).

Depois disso, dentro de web/:  python3 scripts/importar_catalogo.py

Uso (da raiz do projeto ou de qualquer lugar):
    python3 capas/_scripts/restaurar_capas.py            # baixa só o que o site usa
    python3 capas/_scripts/restaurar_capas.py --todas    # baixa também as fotos alternativas (a/b/c/d)

Precisa de: Python 3.9+, Pillow e numpy (pip install pillow numpy).
"""
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
FONTES = json.loads((AQUI / "fontes_higgsfield.json").read_text(encoding="utf-8"))

# capa -> foto escolhida (as outras variações ficaram de fora na época)
CAPAS = [
    ("v2", "01", "01b", "ele-me-trocou"),
    ("v2", "02", "02a", "o-genro-humilhado"),
    ("v2", "03", "03a", "a-segunda-familia-do-meu-marido"),
    ("v2", "04", "04a", "nao-atenda-depois-da-meia-noite"),
    ("v2", "05", "05a", "troquei-de-corpo-com-a-minha-sogra"),
    ("v2", "06", "06a", "a-delegada-que-prendeu-o-proprio-pai"),
    ("v2", "07", "07a", "rejeitada-pelo-alfa"),
    ("v2", "08", "08a", "a-concubina-que-renasceu"),
    ("v2", "09", "09c", "fingi-namorar-meu-pior-inimigo"),
    ("v3", "10", "10a", "ganhei-na-mega-sena"),
    ("v3", "11", "11a", "o-motoboy-que-eu-humilhei"),
    ("v3", "12", "12a", "casei-com-o-mendigo"),
    ("v3", "13", "13a", "a-faxineira-herdou-80-bilhoes"),
    ("v3", "14", "14a", "gravida-de-trigemeos"),
    ("v3", "15", "15a", "ajudei-um-velhinho-e-ganhei-uma-ilha"),
    ("v3", "16", "16a", "largada-no-altar"),
    ("v3", "17", "17a", "minha-sogra-me-expulsou"),
    ("v3", "18", "18b", "o-cachorro-herdou-tudo"),
]


def baixar(rel: str, url: str):
    ext = url.rsplit(".", 1)[-1].split("?")[0]
    destino = RAIZ / f"{rel}.{ext}"
    if destino.exists() and destino.stat().st_size > 0:
        return destino
    destino.parent.mkdir(parents=True, exist_ok=True)
    tmp = destino.with_suffix(destino.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "dramaflix-restaurar/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(tmp, "wb") as f:
        shutil.copyfileobj(r, f)
    tmp.rename(destino)
    print("baixado", destino.relative_to(RAIZ))
    return destino


def py(script: str, *args: str):
    subprocess.run([sys.executable, str(AQUI / script), *map(str, args)], check=True)


def banner_web(origem: Path, destino: Path):
    destino.parent.mkdir(parents=True, exist_ok=True)
    if shutil.which("sips"):  # macOS: o mesmo comando usado na criação
        subprocess.run(["sips", "-z", "1084", "1920", str(origem), "--out", str(destino),
                        "-s", "format", "jpeg", "-s", "formatOptions", "84"],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        from PIL import Image
        Image.open(origem).convert("RGB").resize((1920, 1084), Image.LANCZOS).save(destino, "JPEG", quality=84)


def main():
    todas = "--todas" in sys.argv
    usadas = {f"capas/{lote}/fotos/{foto}" for lote, _, foto, _ in CAPAS}

    # 1) downloads
    for rel, v in FONTES["fotos"].items():
        if todas or rel in usadas:
            baixar(rel, v["url"])
    for rel, v in FONTES["titulos"].items():
        baixar(rel, v["url"])
    for rel, v in FONTES["banners"].items():
        baixar(rel, v["url"])

    # 2) capas
    for lote, n, foto, nome in CAPAS:
        V = RAIZ / "capas" / lote
        (V / "web").mkdir(parents=True, exist_ok=True)
        saida = V / f"{n}-{nome}.png"
        if not saida.exists():
            py("montar_capa.py", V / "fotos" / f"{foto}.png", V / "titulos" / f"{n}.png", saida,
               "--web", V / "web" / f"{n}-{nome}.jpg")

    # 3) banners
    Bn = RAIZ / "capas" / "banners"
    (Bn / "com-logo").mkdir(parents=True, exist_ok=True)
    for lote, n, _, nome in CAPAS:
        png = Bn / f"{n}-{nome}.png"
        web = Bn / "web" / f"{n}-{nome}.jpg"
        if not web.exists():
            banner_web(png, web)
        com_logo = Bn / "com-logo" / f"{n}-{nome}.jpg"
        if not com_logo.exists():
            py("montar_banner.py", png, RAIZ / "capas" / lote / "titulos" / f"{n}.png", com_logo)

    # 4) catálogo
    py("atualizar_catalogo.py")
    print("\nPronto. Agora, dentro de web/:  python3 scripts/importar_catalogo.py")


if __name__ == "__main__":
    main()
