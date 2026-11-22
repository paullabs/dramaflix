#!/usr/bin/env python3
"""Importa o catálogo de capas para o site.

Lê  ../capas/catalogo.json  (gerado pela sessão de capas) e:
  1. otimiza as imagens em web/public:
       capas/<arquivo>.jpg      capa 3:4 600×800 (fileiras, cards)
       fotos/<arquivo>.jpg      foto 3:4 sem texto 1200×1600 (destaque no celular, player)
       logos/<arquivo>.webp     título-logo recortado, fundo transparente (WebP, leve)
       banners/<arquivo>.jpg    banner 16:9 sem texto (destaque no desktop/tablet, modal)
  2. escreve web/src/data/titulos.gerado.json, que o catalogo.ts lê.

Só reprocessa o que mudou. Uso, dentro de web/:
    python3 scripts/importar_catalogo.py
"""
import json
import shutil
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parents[2]
WEB = RAIZ / "web"
PUB = WEB / "public"
CATALOGO = RAIZ / "capas" / "catalogo.json"
SAIDA = WEB / "src" / "data" / "titulos.gerado.json"


def precisa(destino: Path, origem: Path) -> bool:
    return not destino.exists() or destino.stat().st_mtime < origem.stat().st_mtime


def jpg(origem: Path, destino: Path, largura: int, altura: int, qualidade: int = 84):
    if not precisa(destino, origem):
        return
    img = Image.open(origem).convert("RGB")
    if img.size != (largura, altura):
        img = img.resize((largura, altura), Image.LANCZOS)
    img.save(destino, "JPEG", quality=qualidade, optimize=True, progressive=True)


def logo(origem: Path, destino: Path) -> tuple[int, int]:
    if precisa(destino, origem):
        img = Image.open(origem).convert("RGBA")
        caixa = img.getchannel("A").point(lambda a: 255 if a > 10 else 0).getbbox()
        if caixa:
            img = img.crop(caixa)
        margem = int(max(img.size) * 0.02)
        tela = Image.new("RGBA", (img.width + 2 * margem, img.height + 2 * margem), (0, 0, 0, 0))
        tela.paste(img, (margem, margem))
        if tela.width > 1000:
            tela = tela.resize((1000, round(tela.height * 1000 / tela.width)), Image.LANCZOS)
        tela.save(destino, "WEBP", quality=88, method=6)
    with Image.open(destino) as pronto:
        return pronto.size


def cor_media(origem: Path) -> str:
    img = Image.open(origem).convert("RGB").resize((24, 32), Image.BILINEAR)
    px = list(img.getdata())
    media = [sum(p[i] for p in px) / len(px) for i in range(3)]
    return "#" + "".join(f"{int(c * 0.55):02x}" for c in media)


def main():
    dados = json.loads(CATALOGO.read_text(encoding="utf-8"))
    for pasta in ("capas", "fotos", "logos", "banners"):
        (PUB / pasta).mkdir(parents=True, exist_ok=True)

    saida = []
    for t in sorted(dados["titulos"], key=lambda x: x["numero"]):
        a = {k: RAIZ / v for k, v in t["arquivos"].items()}
        arquivo = f"{t['numero']:02d}-{t['id']}"

        if precisa(PUB / "capas" / f"{arquivo}.jpg", a["capa_web"]):
            shutil.copyfile(a["capa_web"], PUB / "capas" / f"{arquivo}.jpg")
        jpg(a["fundo"], PUB / "fotos" / f"{arquivo}.jpg", 1200, 1600)
        jpg(a["banner"], PUB / "banners" / f"{arquivo}.jpg", 1920, 1084, 82)
        lw, lh = logo(a["logo_titulo"], PUB / "logos" / f"{arquivo}.webp")

        saida.append(
            {
                "numero": t["numero"],
                "id": t["id"],
                "arquivo": arquivo,
                "titulo": t["titulo"],
                "genero": t["genero"],
                "tags": t["tags"],
                "sinopse": t["sinopse"],
                "gancho": t.get("gancho") or t["sinopse"].split(". ")[0],
                "episodios": t["episodios"],
                "dublado": bool(t.get("dublado")),
                "lote": t.get("lote", ""),
                "logo": {"w": lw, "h": lh},
                "cor": cor_media(a["fundo"]),
            }
        )
        print(f"ok  {arquivo}")

    SAIDA.write_text(json.dumps(saida, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n{len(saida)} títulos → {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
