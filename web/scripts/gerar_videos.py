#!/usr/bin/env python3
"""Vídeos dos players: amostras 9:16 e o mapa de episódios.

Uso (dentro de web/):  python3 scripts/gerar_videos.py

- AMOSTRA: para cada título de src/data/titulos.gerado.json, cria
  public/videos/<id>/amostra.mp4 a partir da foto sem texto (public/fotos/<arquivo>.jpg):
  12 s, 720×1280, 24 quadros/s, com um empurrão lento de câmera. É só um vídeo de
  exemplo para testar os players; só é refeito se a foto mudar.
- EPISÓDIOS DE VERDADE: coloque em public/videos/<id>/ep-001.mp4, ep-002.mp4…
  (ou .webm). O script encontra os arquivos e escreve src/data/videos.gerado.json.
- PRÉVIA: nas séries com episódio de verdade, cria public/videos/<id>/previa.mp4 com os
  primeiros 12 s do ep. 1 (720×1280, leve). O feed "Para você" toca a prévia, nunca o
  episódio inteiro. Essas séries não precisam de amostra.
  O player usa o episódio real quando existe. Numa série que já tem algum episódio
  real, os que faltam aparecem como "em breve"; a amostra só toca nas séries que
  ainda não têm nenhum episódio.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TITULOS = RAIZ / "src" / "data" / "titulos.gerado.json"
FOTOS = RAIZ / "public" / "fotos"
VIDEOS = RAIZ / "public" / "videos"
SAIDA = RAIZ / "src" / "data" / "videos.gerado.json"

DURACAO_S = 12
FPS = 24
QUADROS = DURACAO_S * FPS
EPISODIO = re.compile(r"^ep-(\d+)\.(mp4|webm)$", re.IGNORECASE)


def gerar_amostra(foto: Path, destino: Path) -> str:
    """Recorte 9:16 do centro da foto, ampliado, com zoom lento de 1,00 a 1,12 (um pouco acima do meio, onde ficam os rostos)."""
    filtro = (
        "crop=w='ih*9/16':h=ih,scale=1440:2560:flags=lanczos,"
        f"zoompan=z='1+0.12*on/{QUADROS - 1}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)*0.4'"
        f":d={QUADROS}:s=720x1280:fps={FPS},format=yuv420p"
    )
    destino.parent.mkdir(parents=True, exist_ok=True)
    temporario = destino.with_suffix(".tmp.mp4")
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(foto), "-vf", filtro, "-frames:v", str(QUADROS),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "30", "-profile:v", "high", "-movflags", "+faststart",
            "-an", str(temporario),
        ],
        check=True,
    )
    temporario.replace(destino)
    return destino.name


def gerar_previa(episodio: Path, destino: Path) -> str:
    """Primeiros 12 s do episódio 1, em 720×1280 e com som (o feed deixa ligar o áudio)."""
    temporario = destino.with_suffix(".tmp.mp4")
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(episodio), "-t", str(DURACAO_S),
            "-vf", "scale=720:1280:flags=lanczos,format=yuv420p", "-r", str(FPS),
            "-c:v", "libx264", "-preset", "slow", "-crf", "27", "-profile:v", "high", "-movflags", "+faststart",
            "-c:a", "aac", "-b:a", "64k", "-ac", "2", str(temporario),
        ],
        check=True,
    )
    temporario.replace(destino)
    return destino.name


def tem_episodio(pasta: Path) -> Path | None:
    """O ep. 1 de verdade da série, se existir."""
    for arq in sorted(pasta.iterdir()) if pasta.exists() else []:
        m = EPISODIO.match(arq.name)
        if m and int(m.group(1)) == 1:
            return arq
    return None


def main() -> int:
    titulos = json.loads(TITULOS.read_text(encoding="utf-8"))
    tarefas = []
    for t in titulos:
        foto = FOTOS / f"{t['arquivo']}.jpg"
        destino = VIDEOS / t["id"] / "amostra.mp4"
        ep1 = tem_episodio(VIDEOS / t["id"])
        if ep1:
            # série com episódio de verdade: prévia curta do ep. 1 no lugar da amostra
            destino.unlink(missing_ok=True)
            previa = VIDEOS / t["id"] / "previa.mp4"
            if not previa.exists() or previa.stat().st_mtime < ep1.stat().st_mtime:
                print(f"  prévia {t['id']}")
                gerar_previa(ep1, previa)
            continue
        if not foto.exists():
            print(f"  sem foto: {foto.name}", file=sys.stderr)
            continue
        if destino.exists() and destino.stat().st_mtime >= foto.stat().st_mtime:
            continue
        tarefas.append((t["id"], foto, destino))

    if tarefas:
        print(f"Gerando {len(tarefas)} amostra(s)…")
        with ThreadPoolExecutor(max_workers=4) as pool:
            for (ident, _, _), _nome in zip(tarefas, pool.map(lambda x: gerar_amostra(x[1], x[2]), tarefas)):
                print(f"  ok {ident}")

    mapa = {}
    for t in titulos:
        pasta = VIDEOS / t["id"]
        episodios = {}
        if pasta.exists():
            for arq in sorted(pasta.iterdir()):
                m = EPISODIO.match(arq.name)
                if m:
                    episodios[str(int(m.group(1)))] = f"/videos/{t['id']}/{arq.name}"
        amostra = pasta / "amostra.mp4"
        previa = pasta / "previa.mp4"
        mapa[t["id"]] = {
            "amostra": f"/videos/{t['id']}/amostra.mp4" if amostra.exists() else None,
            "previa": f"/videos/{t['id']}/previa.mp4" if previa.exists() else None,
            "episodios": episodios,
        }

    SAIDA.write_text(json.dumps(mapa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    reais = sum(len(v["episodios"]) for v in mapa.values())
    print(f"Mapa escrito em {SAIDA.relative_to(RAIZ)}: {len(mapa)} títulos, {reais} episódio(s) de verdade.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
