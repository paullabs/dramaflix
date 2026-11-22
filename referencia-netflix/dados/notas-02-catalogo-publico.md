# Notas brutas — catálogo público (gênero e título), 19/11/2026, viewport 1512×862

Design novo (2025/26) das páginas públicas de catálogo: botões em pílula, cartões de vidro, fundo ambiente borrado.
Prefixos data-uia: "locp" (logged-out collection page) e "lodp" (logged-out details page).

## Elementos comuns
- Fundo ambiente: <img> fixed, cobre a viewport, filter blur(32px), opacity .15, mask-image linear-gradient(#d9d9d9 78.62%, transparente 100%) — cria um "glow" colorido pegando as cores da arte principal. Fundo base ~#141414/#181818.
- Header 72px: degradê linear-gradient(to top, transparente 0%, #000 100%), z 20; logo SVG 147×40 a 48px da esquerda/16px do topo; botão pílula branco "Sair" (14px/500, preto, pad 4px 16px, alt 32px, raio 100px).
  - Design tokens deste botão (variante branca): surface #FFF; hover rgba(255,255,255,.7); pressed rgba(255,255,255,.5); disabled rgba(255,255,255,.4); raio 6.25rem (pílula).
- Gutter lateral do main: 48px (1416px úteis em 1512). Conteúdo das fileiras: 152px de margem (1208px úteis).
- Botão ícone (ButtonIcon): 32×32 (raio 16px) ou 40×40 (raio 20px); surface transparente, hover rgba(128,128,128,.4), pressed rgba(128,128,128,.2). Nos controles de vídeo: fundo rgba(22,22,22,.7) + borda 1px rgba(128,128,128,.7).
- CTA pílula vermelho: #E50914, raio 100px, pad 6px 32px, 16px/500, alt 48px, largura 240px. Versão "flutuante" sticky no rodapé da viewport (container 64px, transição bottom 1s ease-in-out) que aparece ao rolar.
- Seta "Próximo" das fileiras: 24×80, fundo rgba(128,128,128,.4), raio 256px (pílula vertical), ícone chevron 24px, transição background-color/color .2s.
- Painel "vidro": fundo rgba(255,255,255,.1), borda 2px rgba(255,255,255,.04), raio 16px, padding 32px 24px.

## Página de gênero (/br/browse/genre/83 — "Séries")
- Hero 1416×678 com cantos arredondados e base em arco (curva convexa), colagem inclinada de capas 16:9 + degradê escuro à esquerda/baixo. Texto a 64px da borda esquerda do hero:
  - h1 48px/900 (Netflix Sans Black) "Séries"; p 18px/400 descrição (2 linhas, largura 640px); CTA pílula vermelho "Concluir cadastro"; legenda 16px "Diversão ilimitada a partir de R$ 25,90".
- Fileiras (div.locp-collections-title-row): h2 32px/700 branco; ícone-link "›" 32px ao lado do título quando a fileira tem página própria ("Descubra mais").
  - ul flex com overflow; li 198px (padding 10.4px 6px 10.4px 8px) → passo de 196px entre cartões.
  - Cartão: âncora 184px de largura, transição transform .2s ease-in-out (cresce no hover); arte vertical 184×257.6 (proporção ≈ 5:7 / 0,714), raio 12px; placeholder #262626/#353535 raio 16px; arte como background-image de um span absoluto (z 2).
  - Legenda do título abaixo: 14px/21px, branco, centralizado, margem-top 4px, até 2 linhas.
  - SELOS VÊM "QUEIMADOS" NA IMAGEM (não há HTML de selo): "N" vermelho no canto sup. esq. (originais), "TOP 10" (quadrado vermelho, "TOP" pequeno sobre "10" grande) no canto sup. dir., faixas na base centralizadas: "Nova temporada" (fundo vermelho, texto branco bold), "Novos episódios", e faixa dupla "Nova temporada" + "em breve" (2ª linha fundo branco texto preto).
  - Logo do título também faz parte da arte (terço inferior).
- Nomes de fileira vistos: "Descubra suas próximas histórias", "Séries premiadas", "Novelas" … (+ dezenas de títulos por fileira, ~40).
- Planos: h2 32px/700 "Um plano para atender ao seu estilo"; 3 cartões 395×221, raio 16px, padding ~26px:
  - Padrão com anúncios: linear-gradient(149deg, rgb(28,64,114) 6.96%, rgb(23,43,71) 40.17%, rgb(18,12,31) 73.39%)
  - Padrão: linear-gradient(149deg, rgb(89,33,110) 6.96%, rgb(37,23,67) 40.17%, rgb(18,12,31) 73.39%)
  - Premium: linear-gradient(149deg, rgb(108,30,65) 6.96%, rgb(37,23,67) 40.17%, rgb(18,12,31) 73.39%)
  - Conteúdo: nome 24px/500 branco; qualidade 18px/500 rgba(255,255,255,.7); benefícios com ✓ 16px rgba(255,255,255,.7); preço 18px/500 "R$ 25,90 /mês".
- Banner "Descubra seus próximos favoritos…" 1208×104 com colagem de capas ao fundo, texto 24px/700, botão pílula "Mais sobre a Netflix" (fundo rgba(22,22,22,.7), borda clara, 14px/500, 32px).
- Faixa Tudum: painel cinza translúcido raio 12px com ícone "T" + texto 14px rgba(255,255,255,.5) e link sublinhado.

## Página de título (/br/title/{id})
- Navegação âncora "jump-links" fixa no topo, centralizada: pílula 417×41, fundo rgba(0,0,0,.7), backdrop-filter blur(12px), raio 100px, sombra rgba(0,0,0,.5) 8px 8px 16px; itens "Episódios", "Mais títulos para assistir", "Planos" (14px/500, cinza claro).
- Hero 1416×659, cantos arredondados + base em arco: <video> do trailer em autoplay mudo (object-fit cover) sobre <picture> de fundo (crossfade opacity .4s). Logo do título (PNG, ~312×55, proporção ~5.7:1, object-fit contain) a 56px da esquerda; CTA + legenda abaixo do logo.
  - Controles do vídeo no canto inferior direito: 4 botões circulares 40px (Pausar, Som, Expandir, Legendas), fundo rgba(22,22,22,.7), borda 1px rgba(128,128,128,.7), gap 12px.
- Bloco de metadados = painel vidro 1208×189 (padding 26px 34px):
  - h2 24px/500 título; linha de metadados 14px/500 branco separada por "•" (pseudo-elemento, cinza): ano • nº de episódios/temporadas • classificação (ex. "A16") • gênero.
  - 2 colunas: sinopse 16px branco (largura ~547px) | divisor vertical 1px | "Elenco:" 14px/500 branco + nomes 14px rgba(255,255,255,.7).
- Episódios: h2 32px/700; carrossel de cartões 327×364 (painel vidro, padding 8px, raio 16px):
  - Thumb 16:9 307×173, raio 16px; selo de duração no canto inf. dir. ("48min", 13px/500, fundo rgba(0,0,0,.9), raio 4px, pad 1px 12px).
  - Título "1. Episódio 1" 16px/500/24px branco; sinopse 14px/21px rgba(255,255,255,.7) (até 5 linhas). Área de texto com padding 18px 16px 16px.
- "Mais detalhes": h2 32px/700 + 3 painéis vidro lado a lado (402×260, padding 32px 24px): pares rótulo (h4 14px/500 branco) / valor (14px/500 rgba(255,255,255,.7)): Assista offline, Gêneros, "Esta série é…" (tags de clima/tom), Áudio, Legendas, Elenco.
- "Talvez você também goste" e "Em alta": mesmas fileiras de capas verticais 184×258 (sem legenda nesta página).
- Depois: Planos, banner "Descubra…", CTA, rodapé.
- Observação de conteúdo: o título amostrado (C-drama de época, 30 episódios de ~50 min) recebeu tags "Gostinho de novela", "Do ódio ao amor", "Romântico", "Realeza" — o vocabulário de "Esta série é…" é exatamente o tipo de metadado que dramas curtos usam (tropes).
