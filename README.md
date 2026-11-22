# DRAMAFLIX

App de dramas curtos: episódios de 1 a 2 minutos, em vídeo vertical.
São 18 séries, com destaque, feed "Para você", ranking, Minha lista, busca, moedas, VIP e perfil.
Os 10 primeiros episódios de cada série são grátis; depois, cada um custa 40 moedas ou sai pelo VIP.

Dá para instalar como app: no celular, "Adicionar à tela inicial"; no computador, o ícone de instalar na barra do navegador.

Login e pagamento são **simulados**: nada é cobrado, e moedas, lista, histórico e nome ficam só no aparelho.
Em **Perfil → Recomeçar**, o app apaga tudo e volta ao início.

## Rodar

Precisa de **Node.js 20 ou mais novo**.

```bash
cd web
npm install
npm run dev          # http://localhost:3000
```

Versão de produção:

```bash
cd web
npm run build
npm start
```

Não precisa rodar nenhum script: imagens, vídeos e dados gerados já estão no repositório.

## Pastas

| Pasta | O que tem |
|---|---|
| `web/` | O app (Next.js 16, React 19, TypeScript, CSS Modules). Detalhes em `web/README.md`. |
| `web/public/` | Capas, fotos, logos (WebP), banners, ícones do app e vídeos. |
| `capas/` | `catalogo.json` com as 18 séries (título, gancho, sinopse, episódios), prompts e fichas das capas. |
| `capas/_scripts/` | Como as capas foram montadas, e `restaurar_capas.py`, que baixa os originais em alta. |
| `referencia-netflix/` | Especificação de layout e tokens de design usados como base. |
| `historias/_build/` | Roteiros e bíblias das séries Mega-Sena e Mendigo (gerador dos PDFs). |

## Vídeos

- **Episódios reais:** *Casei com o Mendigo* (ep. 1, 1080p) e *Ganhei na Mega-Sena* (ep. 1, 720p).
- **Prévia do feed:** 12 s do episódio 1, com cerca de 1 MB. O feed nunca baixa o episódio inteiro.
- **Amostra:** as outras séries tocam uma amostra de 12 s feita a partir da foto.
- **Novo episódio:** salve em `web/public/videos/<id>/ep-002.mp4` (H.264 + AAC, com `+faststart`) e rode
  `python3 scripts/gerar_videos.py` dentro de `web/`, que precisa do `ffmpeg`.
- **Texto queimado no vídeo:** nada à direita de 80% da largura entre 35% e 95% da altura, porque os botões do player ficam ali.

## Mexer no catálogo

1. Baixe os originais das capas: `python3 capas/_scripts/restaurar_capas.py` (precisa de `pip install pillow numpy`).
2. Edite `capas/catalogo.json`.
3. Rode `python3 scripts/importar_catalogo.py` dentro de `web/`.

**Ícones:** o mapa fica em `web/scripts/gerar_icones.mjs`. Depois de mudar, rode `node scripts/gerar_icones.mjs`.
As fontes são Solar (CC BY 4.0) e Phosphor (MIT).

**Marca:** "DRAMA" e a cor #EC1C5B são provisórias. Elas ficam em `web/src/lib/marca.ts` e `web/src/app/globals.css`.
