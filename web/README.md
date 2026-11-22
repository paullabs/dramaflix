# web — o app

Next.js 16 (App Router), React 19, TypeScript e CSS Modules. Sem backend: o estado fica no `localStorage`.
O app pode ser instalado (manifesto em `src/app/manifest.ts`, ícones em `public/icone-*.png`).

```bash
npm install
npm run dev      # http://localhost:3000
npm run build    # produção
```

## Telas

| Rota | O que tem |
|---|---|
| `/` | Destaque que gira a cada 9 s, com logo e gancho; fileiras por tema; Top 10; "Continuar" (só aparece depois de assistir algo) |
| `/para-voce` | Feed vertical, uma série por tela, com prévia em vídeo |
| `/em-alta` | Ranking Hoje / Semana / Mês |
| `/minha-lista` | Séries salvas com o + |
| `/buscar` | Busca por título, gênero, tema ou gancho, sem ligar para acentos |
| `/categoria/[slug]` | Grade de cada tema |
| `/moedas` | Saldo, pacotes de moedas e planos VIP (mostra o plano ativo) |
| `/perfil` | Nome, "Continuar", atalhos e Recomeçar |
| `/ajuda` | Perguntas frequentes |
| `/assistir/[id]?ep=N` | Player 9:16: episódios 1 a 10 grátis; os outros pedem 40 moedas ou VIP |

Tocar numa capa abre os detalhes: banner, sinopse completa, grade de episódios e parecidos.

## Player

- **Gestos:** tocar pausa; segurar acelera para 2x; deslizar ↑/↓ (ou a roda do mouse) troca de episódio.
- **Barra de tempo:** arrastável, com o tempo em cima do dedo.
- **Botões:** som, tela cheia (computador), velocidade 1x / 1,5x / 2x, curtir, lista, episódios e enviar.
- **Fim do episódio:** contagem de 3 s para o próximo, que dá para cancelar.
- **Paywall:** "Liberar por 40", "VIP" e "Voltar ao ep. N", onde N é o último episódio que a pessoa pode ver.
- **Onde parou:** guarda episódio e segundo; ao voltar, continua dali.
- **Teclado:** espaço/K pausa; ←/→ 5 s; ↑/↓ troca de episódio; M som; F tela cheia; Esc sai.

## Vídeos (`public/videos/<id>/`)

| Arquivo | O que é |
|---|---|
| `ep-001.mp4`, `ep-002.mp4`… | Episódios reais (H.264 + AAC, `+faststart`). Hoje: Mendigo ep. 1 (1080p) e Mega-Sena ep. 1 (720p). |
| `previa.mp4` | 12 s do ep. 1, em 720p (~1 MB). O feed toca a prévia, nunca o episódio inteiro. |
| `amostra.mp4` | Nas séries sem episódio real: 12 s feitos a partir da foto. O player avisa "Vídeo de exemplo". |

Numa série com episódio real, os que faltam aparecem como "em breve". Depois de pôr um episódio novo,
rode `python3 scripts/gerar_videos.py`: ele refaz prévias e amostras e escreve `src/data/videos.gerado.json`.

**Texto queimado no vídeo:** nada à direita de 80% da largura entre 35% e 95% da altura (os botões do player ficam ali).

## Catálogo

```bash
python3 scripts/importar_catalogo.py
```

O script lê `../capas/catalogo.json` e os originais em `../capas/`
(baixe com `python3 ../capas/_scripts/restaurar_capas.py`). Ele gera:
- `public/capas/`: capa 600×800;
- `public/fotos/`: foto sem texto, 1200×1600;
- `public/logos/`: logo do título em WebP transparente;
- `public/banners/`: banner 16:9, 1920×1084;
- `src/data/titulos.gerado.json`.

## Onde mexer

| O quê | Arquivo |
|---|---|
| Cores, espaçamentos, movimento | `src/app/globals.css` |
| Nome da marca (provisório: "DRAMA") | `src/lib/marca.ts` |
| Fileiras, temas, destaques, ranking, classificação | `src/data/catalogo.ts` |
| Lista, moedas, VIP, perfil, Recomeçar | `src/lib/estado.ts` |
| Onde parou / "Continuar" | `src/lib/historico.ts` |
| Ícones | `scripts/gerar_icones.mjs` → `node scripts/gerar_icones.mjs` |
| Barra lateral e abas | `src/components/navegacao.ts` |

## Regras de interface

- **Pouco texto:** figura + número + uma palavra ("10 ep. grátis", "Nº 1 hoje", "Liberar por 40"). O gancho tem uma frase só; a sinopse completa fica nos detalhes.
- **Nenhum botão morto:** tudo o que aparece leva a algum lugar ou faz alguma coisa.
- **Diagramação:** barra lateral de 92 px no desktop (≥ 960 px); no celular, barra no topo e abas embaixo. Capas sempre 3:4.
- **Movimento:** discreto, com caminho para "reduzir movimento".
- **Leve:** o destaque só carrega a arte atual e a próxima; logos em WebP; o feed usa prévias curtas.
